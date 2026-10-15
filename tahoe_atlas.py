#!/usr/bin/env python3
r"""
tahoe_atlas.py - every angle of Tahoe-100M with the artifact corrections worked out on MTAP and Gankyrin,
and a Claude agent at each endpoint that analyses one angle and writes a report on it.

Put this file next to tahoe_mtap_gankyrin.py in your Tahoe-100M folder and run from there:

    python3 tahoe_atlas.py check      # preflight: packages, data, disk, memory (+ API key and a tiny agent call)
    python3 tahoe_atlas.py compute    # all the computation, no agents: build + effects + angles, then bundle
    python3 tahoe_atlas.py agents     # one Claude agent per angle writes a report (needs ANTHROPIC_API_KEY)
    python3 tahoe_atlas.py all        # compute + agents in one go
    python3 tahoe_atlas.py bundle     # atlas_bundle.zip to upload to Claude: key tables, then reports too
    python3 tahoe_atlas.py lookup gene PSMD10     # cards: gene / drug / line / corr
  The computation steps can also run one at a time: build (one pass over all cells -> counts per well x cell
  line x gene), effects (corrected effect of every drug-dose on every gene and line), angles (one data package
  per angle).

Angles (one agent, one report each): quality, drugs, genes, classes, cell_lines, biomarkers, line_response, programs,
cell_state, one per focus gene (--focus-genes, default MTAP,PSMD10), and an overview that reads every report.
Every drug and every cell line also gets a card (angles/drugs/cards, angles/cell_lines/cards).

Agents:  --model sonnet|opus  --budget 5 (USD cap per agent)  --max-turns 80  --parallel 3
         --angles drugs,genes (subset)  --dry-run (write prompts only)  --redo (rerun finished reports)
         --web (let agents check the literature)  --sandbox (agent shell sandboxed; Linux/macOS only)
Output:  atlas/pseudobulk (counts), atlas/effects (matrices), atlas/angles/<angle> (data + brief + report),
         atlas/reports/NN_<angle>.md (one report per angle) and 00_overview.md.
Logs:    the script writes its own log: atlas/atlas.log (computation) and atlas/agents.log (agents), and keeps the
         computer from sleeping while it runs.
Long runs on Linux/macOS (survive logout):
             nohup python3 tahoe_atlas.py compute > /dev/null 2>&1 &      then: tail -f atlas/atlas.log
On Windows (PowerShell; leave the window open, no nohup):
             C:\tahoe\.venv\Scripts\python.exe tahoe_atlas.py compute     log: atlas\atlas.log
"""

import argparse
import asyncio
import dataclasses
import glob
import json
import math
import multiprocessing as mp
import os
import re
import shlex
import shutil
import sys
import time
import traceback
import warnings
import zipfile
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor

import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.compute as pc
import pyarrow.parquet as pq

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)
try:
    import tahoe_mtap_gankyrin as T
except ImportError:
    sys.exit("tahoe_atlas.py needs tahoe_mtap_gankyrin.py in the same folder")
if not all(hasattr(T, f) for f in ("start_run_log", "keep_awake", "py_cmd", "REINDEX_HINT")):
    sys.exit("tahoe_mtap_gankyrin.py next to tahoe_atlas.py is an older version: copy the current one over it "
             "(its MTAP/Gankyrin method and results are unchanged)")

log = T.log

# ----------------------------------------------------------------------------- settings
MIN_CELLS = 30             # cells of one line in one well needed to use its expression
MIN_LINES = 5              # lines needed for a well-level effect
MIN_CPM = 2.0              # genes kept: pooled level >= this many counts per million
EXPR_FRAC = 0.25           # a line expresses a gene if its level >= this fraction of the median line
LFC_MIN = math.log2(1.2)   # min fold change counted as a change
Q_CUT = 0.10               # FDR cut
N_PCS = 3                  # broad components removed before co-regulation and program finding
MODULE_K = 50              # gene programs (k-means clusters)
MODULE_MIN = 8             # smallest program kept
TOP = 25                   # top genes per drug, drugs per gene, etc.
ABUND_MIN_FRAC = 0.02      # lines with fewer cells than this fraction of the median line are left out of growth
MIN_SIG_BETA = 20          # significant genes a drug-dose needs before per-line response strength is measured
LOSS_MAX = 0.30            # expression-loss screen: lost lines read at most this fraction of the median line ...
LOSS_PRESENT = 0.5         # ... while >= 70% of lines sit at or above this fraction
LOSS_MIN_CPM = 10.0        # ... for genes at least this abundant in the median line
ANGLES = ["quality", "drugs", "genes", "classes", "cell_lines", "biomarkers", "line_response", "programs",
          "cell_state"]
TITLES = {"quality": "Data quality and artifacts",
          "drugs": "Drugs: what each drug does to the transcriptome",
          "genes": "Genes: which drugs move each gene",
          "classes": "Drug classes and shared targets",
          "cell_lines": "Cell lines: mutations, lineage, gene loss and selective depletion",
          "biomarkers": "Biomarkers: which genes' levels predict who a drug kills",
          "line_response": "Cell lines: who responds transcriptionally to each drug",
          "programs": "Gene programs and the drugs that drive them",
          "cell_state": "Cell state: cell cycle, proliferation and toxicity"}
BUILD_COLS = ["genes", "expressions", "BARCODE_SUB_LIB_ID", "sample", "plate", "drug", "cell_line_id"]
BAD_IDS = {"", "none", "nan", "<na>", "null"}
EFFECTS_VERSION = 2        # effects/complete.json: written last by 'effects'; angles, agents and lookups need it


def dirs(out):
    d = {"pb": os.path.join(out, "pseudobulk"), "fx": os.path.join(out, "effects"),
         "ang": os.path.join(out, "angles"), "rep": os.path.join(out, "reports")}
    for p in d.values():
        os.makedirs(p, exist_ok=True)
    return d


def quiet():
    """Silence numpy's all-NaN slice warnings (expected: lines missing from some wells)."""
    warnings.filterwarnings("ignore", category=RuntimeWarning)
    np.seterr(all="ignore")


def safe_name(s):
    return re.sub(r"[^\w.-]+", "_", str(s)).strip("_")[:80] or "x"


# ----------------------------------------------------------------------------- statistics helpers
try:
    from scipy.special import ndtr as _ndtr
    from scipy.stats import t as _tdist

    def norm_sf(z):
        return _ndtr(-np.asarray(z, dtype=float))

    def t_sf(t, df):
        return _tdist.sf(np.asarray(t, dtype=float), np.asarray(df, dtype=float))
except Exception:  # noqa: BLE001  (scipy not installed: pure-Python fallbacks)
    _erfc = np.vectorize(math.erfc, otypes=[float])

    def norm_sf(z):
        z = np.asarray(z, dtype=float)
        out = np.full(z.shape, np.nan)
        ok = np.isfinite(z)
        out[ok] = 0.5 * _erfc(z[ok] / math.sqrt(2.0))
        return out

    def _betacf(a, b, x):
        qab, qap, qam = a + b, a + 1.0, a - 1.0
        c, d = 1.0, 1.0 - qab * x / qap
        d = 1.0 / (d if abs(d) > 1e-300 else 1e-300)
        h = d
        for m in range(1, 300):
            m2 = 2 * m
            for aa in (m * (b - m) * x / ((qam + m2) * (a + m2)),
                       -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))):
                d = 1.0 + aa * d
                d = 1.0 / (d if abs(d) > 1e-300 else 1e-300)
                c = 1.0 + aa / c
                c = c if abs(c) > 1e-300 else 1e-300
                h *= d * c
            if abs(d * c - 1.0) < 3e-12:
                break
        return h

    def _betai(a, b, x):
        if x <= 0:
            return 0.0
        if x >= 1:
            return 1.0
        bt = math.exp(math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b) + a * math.log(x) + b * math.log(1 - x))
        if x < (a + 1) / (a + b + 2):
            return bt * _betacf(a, b, x) / a
        return 1.0 - bt * _betacf(b, a, 1 - x) / b

    def _t_sf1(t, df):
        if not (np.isfinite(t) and np.isfinite(df) and df > 0):
            return np.nan
        tail = 0.5 * _betai(df / 2.0, 0.5, df / (df + t * t))
        return tail if t > 0 else 1.0 - tail

    _t_sf_vec = np.vectorize(_t_sf1, otypes=[float])

    def t_sf(t, df):
        return _t_sf_vec(np.asarray(t, dtype=float), np.asarray(df, dtype=float))


def bh_columns(p):
    """Benjamini-Hochberg within each column of a 2-D array (NaN = not tested)."""
    p = np.asarray(p, dtype=float)
    D = p.shape[0]
    order = np.argsort(np.where(np.isfinite(p), p, np.inf), axis=0, kind="stable")
    ps = np.take_along_axis(p, order, axis=0)
    m = np.isfinite(p).sum(axis=0)
    ranks = np.arange(1, D + 1, dtype=float)[:, None]
    q = ps * m[None, :] / ranks
    q = np.where(np.isfinite(ps), q, np.inf)
    q = np.minimum.accumulate(q[::-1], axis=0)[::-1]
    q = np.where(np.isfinite(ps), np.minimum(q, 1.0), np.nan)
    out = np.empty_like(q)
    np.put_along_axis(out, order, q, axis=0)
    return out


def robust_cols(M, rows):
    """Per-column robust centre and scale (median, 1.4826*MAD) over the given rows."""
    sub = M[rows]
    c = np.nanmedian(sub, axis=0)
    s = 1.4826 * np.nanmedian(np.abs(sub - c), axis=0)
    sd = np.nanstd(sub, axis=0)
    s = np.where((s > 0) & np.isfinite(s), s, np.where(sd > 0, sd, 1.0))
    return c, s


def robust_z(v):
    v = np.asarray(v, dtype=float)
    c, s = T.robust_center_scale(v)
    return (v - c) / s


def spearman(a, b):
    a, b = np.asarray(a, dtype=float), np.asarray(b, dtype=float)
    ok = np.isfinite(a) & np.isfinite(b)
    if ok.sum() < 6:
        return np.nan
    ra = pd.Series(a[ok]).rank().to_numpy()
    rb = pd.Series(b[ok]).rank().to_numpy()
    if ra.std() == 0 or rb.std() == 0:
        return np.nan
    return float(np.corrcoef(ra, rb)[0, 1])


def loo_matrix(M, slot, drug, use, min_wells=T.MIN_SLOT_WELLS):
    """Leave-drug-out well-position effect for every column: for each well, the median of the wells in the
    same position (any plate) that hold a different drug."""
    M = np.asarray(M)
    eff = np.zeros(M.shape, dtype=np.float32)
    n_used = np.zeros(M.shape[0], dtype=int)
    slot = np.asarray(slot, dtype=float)
    drug = np.asarray(drug, dtype=object)
    use = np.asarray(use, dtype=bool)
    groups = defaultdict(list)
    for i, s in enumerate(slot):
        if np.isfinite(s):
            groups[s].append(i)
    for ii in groups.values():
        ii = np.asarray(ii)
        for i in ii:
            m = ii[use[ii] & (drug[ii] != drug[i])]
            n_used[i] = m.size
            if m.size >= min_wells:
                v = np.nanmedian(M[m], axis=0)
                eff[i] = np.where(np.isfinite(v), v, 0.0)
    return eff, n_used


def line_fit(X, y, min_n=10):
    """Per row of X (lines x genes): slope through the origin on y (the consensus effect) and correlation."""
    ok = np.isfinite(X) & np.isfinite(y)[None, :]
    n = ok.sum(axis=1)
    Xf = np.where(ok, X, 0.0).astype(np.float64)
    Yf = np.where(ok, y[None, :], 0.0).astype(np.float64)
    sxy, syy, sxx = (Xf * Yf).sum(1), (Yf ** 2).sum(1), (Xf ** 2).sum(1)
    sx, sy = Xf.sum(1), Yf.sum(1)
    nn = np.maximum(n, 1)
    beta = sxy / np.where(syy > 0, syy, np.nan)
    cov, vx, vy = sxy - sx * sy / nn, sxx - sx ** 2 / nn, syy - sy ** 2 / nn
    r = cov / np.sqrt(np.where((vx > 0) & (vy > 0), vx * vy, np.nan))
    beta[n < min_n] = np.nan
    r[n < min_n] = np.nan
    return beta.astype(np.float32), r.astype(np.float32)


def dose_shape(zs, thr=2.0):
    """How an effect behaves across ascending doses (z already signed so that positive = the effect)."""
    zs = [z for z in zs if np.isfinite(z)]
    if not zs or max(zs) < thr:
        return "none"
    if len(zs) == 1:
        return "single dose"
    if min(zs) >= thr:
        return "all doses, stronger at high dose" if zs[-1] - zs[0] >= 1.0 else "all doses, flat"
    if zs[-1] >= thr and max(zs[:-1]) < thr * 0.75:
        return "top dose only"
    if zs[-1] >= thr and all(b >= a - 0.5 for a, b in zip(zs, zs[1:])):
        return "rises with dose"
    if len(zs) >= 3 and min(zs[-2:]) >= thr:
        return "two highest doses"
    return "inconsistent across doses"


def flags_for(row):
    f = []
    if row.get("cells_log2_vs_plate", 0) < -1:
        f.append("toxic")
    if row.get("genes_per_cell_log2_vs_plate", 0) < -0.3 or row.get("umi_per_cell_log2_vs_plate", 0) < -0.5:
        f.append("transcription drop")
    if abs(row.get("G2M_PHASE_lfc", 0) or 0) > 0.5 or abs(row.get("S_PHASE_lfc", 0) or 0) > 0.5:
        f.append("cell-cycle shift")
    return "; ".join(f)


# ============================================================================= build
def _file_plate(path):
    try:
        b = next(pq.ParquetFile(path).iter_batches(batch_size=1, columns=["plate"]))
        return path, str(b.column(0)[0].as_py())
    except Exception:  # noqa: BLE001
        return path, "unknown"


def _build_group(job):
    """Sum the counts of every cell into its (well, cell line) profile, for one plate's files."""
    gid, name, files, G, pb, batch_size = job
    base = os.path.join(pb, f"group{gid:03d}")
    outs = [base + s for s in ("_profiles.csv", "_barcodes.csv", "_samples.csv", ".npy")]
    flist = base + "_files.txt"
    want = "\n".join(files)
    if all(os.path.exists(o) for o in outs) and os.path.exists(flist):
        with open(flist, encoding="utf-8", errors="replace") as fh:
            if fh.read() == want:
                return gid, name, 0, True
    try:
        pa.set_cpu_count(1)
    except Exception:  # noqa: BLE001
        pass
    cap = 5000
    acc = np.zeros((cap, G), dtype=np.float32)       # pages are only touched when used
    ncell = np.zeros(cap, dtype=np.int64)
    ngen = np.zeros(cap, dtype=np.float64)
    keys, key_list = {}, []
    bc = defaultdict(int)
    smeta = {}
    cells, t0 = 0, time.time()
    for k_file, f in enumerate(files, 1):
        pf = pq.ParquetFile(f)
        for batch in pf.iter_batches(batch_size=batch_size, columns=BUILD_COLS, use_threads=False):
            n = batch.num_rows
            if not n:
                continue

            def col(cname):
                return batch.column(batch.schema.get_field_index(cname))

            samples = pc.cast(col("sample"), pa.string()).to_pandas().astype(str)
            lines = pc.cast(col("cell_line_id"), pa.string()).to_pandas().astype(str)
            codes, uniq = pd.factorize(samples + "\t" + lines)
            rowmap = np.empty(len(uniq), dtype=np.int64)
            for j, u in enumerate(uniq):
                r = keys.get(u)
                if r is None:
                    r = len(key_list)
                    keys[u] = r
                    key_list.append(u)
                rowmap[j] = r
            if len(key_list) > cap:
                new = max(len(key_list) + 256, int(cap * 1.5))
                acc = np.concatenate([acc, np.zeros((new - cap, G), dtype=np.float32)])
                ncell = np.concatenate([ncell, np.zeros(new - cap, dtype=np.int64)])
                ngen = np.concatenate([ngen, np.zeros(new - cap)])
                cap = new
            prow = rowmap[codes]
            genes, expr = col("genes"), col("expressions")
            lens = pc.fill_null(pc.list_value_length(genes), 0).to_numpy(zero_copy_only=False).astype(np.int64)
            vals = np.asarray(genes.flatten().to_numpy(zero_copy_only=False)).astype(np.int64, copy=False)
            ex = np.array(expr.flatten().to_numpy(zero_copy_only=False), dtype=np.float32)
            bad = (vals < 0) | (vals >= G)
            if bad.any():
                vals = np.where(bad, 0, vals)
                ex[bad] = 0.0
            offs = np.zeros(n + 1, dtype=np.int64)
            np.cumsum(lens, out=offs[1:])
            for i in range(n):              # first entry of each row is a marker token: skipped
                s, e = offs[i] + 1, offs[i + 1]
                if e > s:
                    row = acc[prow[i]]
                    row[vals[s:e]] += ex[s:e]
            np.add.at(ncell, prow, 1)
            np.add.at(ngen, prow, np.maximum(lens - 1, 0))
            fields = pc.cast(col("BARCODE_SUB_LIB_ID"), pa.string()).to_pandas().astype(str) \
                .str.split("-", n=1).str[0].str.split("_", expand=True)
            for k in range(min(3, fields.shape[1])):
                v = pd.to_numeric(fields[k], errors="coerce")
                t = pd.DataFrame({"sample": samples.values, "value": v.values}).dropna()
                for (s_, v_), c_ in t.groupby(["sample", "value"]).size().items():
                    bc[(s_, k, float(v_))] += int(c_)
            first = ~samples.duplicated().values
            if first.any():
                pl = pc.cast(col("plate"), pa.string()).to_pandas().astype(str).values
                dr = pc.cast(col("drug"), pa.string()).to_pandas().astype(str).values
                for s_, p_, d_ in zip(samples.values[first], pl[first], dr[first]):
                    smeta.setdefault(s_, (p_, d_))
            cells += n
        if k_file % 25 == 0:
            el = time.time() - t0
            log(f"    {name}: {k_file}/{len(files)} files, {cells:,} cells, "
                f"~{el / k_file * (len(files) - k_file) / 60:.0f} min left")
    P = len(key_list)
    prof = pd.DataFrame({"row": np.arange(P), "sample": [k.split("\t")[0] for k in key_list],
                         "cell_line_id": [k.split("\t")[1] for k in key_list], "n_cells": ncell[:P],
                         "n_genes": ngen[:P], "total_counts": acc[:P].sum(axis=1, dtype=np.float64)})
    with open(base + ".tmp", "wb") as fh:
        np.save(fh, acc[:P])
    os.replace(base + ".tmp", outs[3])
    prof.to_csv(outs[0], index=False)
    pd.DataFrame([(s, f, v, c) for (s, f, v), c in bc.items()],
                 columns=["sample", "field", "value", "n"]).to_csv(outs[1], index=False)
    pd.DataFrame([(s, p, d) for s, (p, d) in smeta.items()],
                 columns=["sample", "plate", "drug"]).to_csv(outs[2], index=False)
    with open(flist, "w", encoding="utf-8") as fh:
        fh.write(want)
    return gid, name, cells, False


def cmd_build(args):
    D = dirs(args.out)
    idx = T.discover(args.data, args.out, refresh=args.reindex)
    exprs = idx["expression"]
    if not exprs:
        sys.exit("No expression parquet files found under " + os.path.abspath(args.data) + T.REINDEX_HINT)
    if args.limit_files:
        exprs = exprs[:args.limit_files]
    gm = T.read_tables(idx["gene"], ["token_id", "gene_symbol", "ensembl_id"])
    if gm is None:
        sys.exit("Gene metadata (token_id -> gene_symbol) not found" + T.REINDEX_HINT)
    G = int(gm["token_id"].max()) + 1
    log(f"Finding the plate of each of {len(exprs)} files ...")
    with ThreadPoolExecutor(16) as ex:
        fplate = dict(ex.map(_file_plate, exprs))
    by_plate = defaultdict(list)
    for f in exprs:
        by_plate[fplate[f]].append(f)
    plates = sorted(by_plate, key=lambda p: (len(p), p))
    jobs = [(gid, p, by_plate[p], G, D["pb"], args.batch_size) for gid, p in enumerate(plates)]
    for old in glob.glob(os.path.join(D["pb"], "group*_profiles.csv")):    # groups from an earlier, different run
        gid = int(re.search(r"group(\d+)_", old).group(1))
        if gid >= len(jobs):
            for f in glob.glob(old.replace("_profiles.csv", "*")):
                os.remove(f)
    workers = min(args.workers or T.auto_workers(), len(jobs))
    per_worker = 5000 * G * 4 / 1e9 * 1.3 + 1.0
    mem = T.mem_available_gb()
    if mem:
        workers = max(1, min(workers, int(mem / per_worker)))
    log(f"{len(exprs)} files on {len(by_plate)} plates -> one group per plate, {workers} at a time "
        f"(~{per_worker:.1f} GB each)")
    if not args.workers and workers > 2 and T.disk_kind(args.data) == "hdd":
        log("  the data seem to sit on a hard drive: if reading is slow, stop and rerun with --workers 2 "
            "(parallel readers make a hard drive seek; finished plates are kept)")
    t0, done, cells = time.time(), 0, 0
    ctx = mp.get_context("spawn")
    with ctx.Pool(workers) as pool:
        for _gid, name, nc, reused in pool.imap_unordered(_build_group, jobs, chunksize=1):
            done += 1
            cells += nc
            log(f"  {name} {'already built' if reused else 'done'} ({done}/{len(jobs)} plates, "
                f"{(time.time() - t0) / 60:.1f} min)")
    metas = sorted(glob.glob(os.path.join(D["pb"], "group*_profiles.csv")))
    prof = pd.concat([pd.read_csv(m, dtype={"sample": str, "cell_line_id": str}) for m in metas], ignore_index=True)
    bcf = pd.concat([pd.read_csv(m.replace("_profiles", "_barcodes"), dtype={"sample": str}) for m in metas],
                    ignore_index=True)
    smeta = pd.concat([pd.read_csv(m.replace("_profiles", "_samples"),
                                   dtype={"sample": str, "plate": str, "drug": str}) for m in metas],
                      ignore_index=True).drop_duplicates("sample")
    wl_like = prof.groupby("sample", as_index=False)["n_cells"].sum()
    sm, source, checks = T.build_sample_map(smeta, bcf, wl_like, idx, args.layout)
    sm.to_csv(os.path.join(args.out, "sample_map.csv"), index=False)
    checks.to_csv(os.path.join(args.out, "well_position_check.csv"), index=False)
    with open(os.path.join(args.out, "build_info.json"), "w", encoding="utf-8") as fh:
        json.dump({"G": G, "groups": len(jobs), "cells": int(prof["n_cells"].sum()), "profiles": len(prof),
                   "well_position_source": source, "limit_files": args.limit_files}, fh, indent=1)
    dup = sm.dropna(subset=["slot"]).duplicated(["plate", "slot"]).sum()
    log(f"Build done: {int(prof['n_cells'].sum()):,} cells in {len(prof):,} well x line profiles, "
        f"{sm['sample'].nunique()} wells; well positions from {source} "
        f"(median purity {sm['slot_purity'].median():.3f}, duplicate positions within a plate: {dup})")


# ============================================================================= effects
def load_profiles(pb):
    metas = sorted(glob.glob(os.path.join(pb, "group*_profiles.csv")))
    if not metas:
        sys.exit("No pseudobulk found; run 'build' first")
    parts = []
    for m in metas:
        t = pd.read_csv(m, dtype={"sample": str, "cell_line_id": str})
        t["file"] = m.replace("_profiles.csv", ".npy")
        parts.append(t)
    return pd.concat(parts, ignore_index=True)


def gene_columns(gm, line_sum, line_tot, G):
    """Pick the genes worth testing and define the summed modules."""
    pooled = 1e6 * line_sum.sum(axis=0) / max(line_tot.sum(), 1.0)
    keep = np.flatnonzero(pooled >= MIN_CPM)
    sym = pd.Series(gm["gene_symbol"].astype(str).values, index=gm["token_id"].astype(int).values)
    sym = sym[~sym.index.duplicated()]
    ens = pd.Series(gm["ensembl_id"].astype(str).values if "ensembl_id" in gm else [""] * len(gm),
                    index=gm["token_id"].astype(int).values)
    ens = ens[~ens.index.duplicated()]
    keep = np.array([t for t in keep if t in sym.index and sym[t].lower() not in BAD_IDS], dtype=np.int64)
    symbols = sym.reindex(keep).values
    dup = pd.Series(symbols).duplicated(keep=False).values
    labels = [f"{s} ({ens.get(t, t)})" if d else s for s, t, d in zip(symbols, keep, dup)]
    allsym = sym.reindex(np.arange(G))
    modules = {
        "S_PHASE": np.flatnonzero(allsym.isin(T.S_GENES).values),
        "G2M_PHASE": np.flatnonzero(allsym.isin(T.G2M_GENES).values),
        "PROTEASOME": np.flatnonzero(allsym.fillna("").map(
            lambda s: bool(T.PROTEASOME_RE.match(s)) and s not in T.PROTEASOME_EXCLUDE).values),
    }
    return keep, symbols, labels, pooled, modules


def plate_block(prof_p, wells, lines, keep, modules):
    """counts (W, L, K), totals, cells, genes for one plate."""
    W, L = len(wells), len(lines)
    K = len(keep) + len(modules)
    counts = np.zeros((W, L, K), dtype=np.float32)
    tot = np.zeros((W, L))
    nc = np.zeros((W, L))
    ng = np.zeros((W, L))
    wi = {s: i for i, s in enumerate(wells)}
    li = {s: i for i, s in enumerate(lines)}
    for f, g in prof_p.groupby("file"):
        g = g.sort_values("row")
        arr = np.load(f, mmap_mode="r")
        sub = np.asarray(arr[g["row"].to_numpy()])
        block = np.empty((len(g), K), dtype=np.float32)
        block[:, :len(keep)] = sub[:, keep]
        for j, toks in enumerate(modules.values()):
            block[:, len(keep) + j] = sub[:, toks].sum(axis=1)
        w = g["sample"].map(wi).to_numpy()
        ln = g["cell_line_id"].map(li).to_numpy()
        np.add.at(counts, (w, ln), block)
        np.add.at(tot, (w, ln), g["total_counts"].to_numpy())
        np.add.at(nc, (w, ln), g["n_cells"].to_numpy())
        np.add.at(ng, (w, ln), g["n_genes"].to_numpy())
        del sub
    return counts, tot, nc, ng


def log_cpm(counts, tot, nc, expr_mask=None):
    Y = np.full(counts.shape, np.nan, dtype=np.float32)
    ok = nc >= MIN_CELLS
    Y[ok] = np.log2((counts[ok] + 0.5) / (tot[ok][:, None] + 1.0) * 1e6)
    if expr_mask is not None:
        Y[:, ~expr_mask] = np.nan
    return Y


def plate_residuals(prof, smp_, lines, keep, modules, expr_mask):
    """One plate: counts and the residual of every well x line x gene from the plate's drug-well median."""
    wells = list(smp_["sample"])
    counts, tot, nc, ng = plate_block(prof[prof["sample"].isin(wells)], wells, lines, keep, modules)
    Y = log_cpm(counts, tot, nc, expr_mask)
    drug = ~smp_["is_dmso"].to_numpy()
    base = np.nanmedian(Y[drug], axis=0)
    r1 = Y - base[None]
    del Y
    return counts, tot, nc, ng, r1, base


def set_min_cells(args, prof):
    """Cells needed per (well, line) profile: 30 on the full data; lower for trial runs with few files."""
    global MIN_CELLS
    per = prof.groupby(["sample", "cell_line_id"])["n_cells"].sum()
    med = float(per.median()) if len(per) else 0.0
    if args.min_cells:
        MIN_CELLS = args.min_cells
    elif med < 4 * MIN_CELLS:
        MIN_CELLS = max(3, int(med // 4))
        log(f"  only ~{med:.0f} cells per line per well (trial run?): using profiles with >= {MIN_CELLS} cells")
    with open(os.path.join(args.out, "effects", "info.json"), "w", encoding="utf-8") as fh:
        json.dump({"min_cells": MIN_CELLS, "median_cells_per_profile": med}, fh)


def line_driver_changes(idx):
    """'GENE p.X; ...' per cell line from the cell line metadata (protein changes only)."""
    cl = T.read_tables(idx["cell_line"])
    if cl is None or "Cell_ID_Cellosaur" not in cl or "Driver_Gene_Symbol" not in cl:
        return None
    col = next((c for c in cl.columns if "ProtEffect" in c), None)
    if col is None:
        return None
    out = {}
    for cid, g in cl.groupby("Cell_ID_Cellosaur"):
        items = set()
        for _, r in g.iterrows():
            ch = T.to_text(r.get(col)).strip()
            sym = T.to_text(r.get("Driver_Gene_Symbol")).strip()
            if re.match(r"^[A-Z][a-z]{0,2}\d+[A-Za-z*]", ch):          # 'G12C' -> 'p.G12C'
                ch = "p." + ch
            if sym and ch.startswith("p.") and len(ch) > 3 and " " not in ch:
                items.add(f"{sym} {ch}")
        out[cid] = "; ".join(sorted(items))
    return pd.Series(out, name="driver_changes")


def effects_ready(out):
    """True when <out>/effects is complete and from this version of tahoe_atlas.py (complete.json is written last)."""
    try:
        with open(os.path.join(out, "effects", "complete.json"), encoding="utf-8") as fh:
            return json.load(fh).get("version") == EFFECTS_VERSION
    except (OSError, ValueError, AttributeError):
        return False


def save_npy(path, arr):
    """np.save to a temporary file, then swap it in (an interrupted run never leaves a half-written matrix)."""
    tmp = path + ".tmp"
    with open(tmp, "wb") as fh:
        np.save(fh, arr)
    try:
        os.replace(tmp, path)
    except PermissionError:
        os.remove(tmp)
        sys.exit(f"Cannot replace {path}: another program has it open (an agent, a lookup or a Python session "
                 "reading atlas/effects?). Close it, then run 'effects' (or 'compute') again")


def cmd_effects(args):
    quiet()
    D = dirs(args.out)
    try:                                    # not complete until this run writes it again at the very end
        os.remove(os.path.join(D["fx"], "complete.json"))
    except FileNotFoundError:
        pass
    idx = T.discover(args.data, args.out)
    smp = os.path.join(args.out, "sample_map.csv")
    if not os.path.exists(smp):
        sys.exit("sample_map.csv not found; run 'build' first")
    sm = pd.read_csv(smp, dtype={"sample": str, "plate": str, "drug": str, "plate_num": str})
    sm["is_dmso"] = sm["is_dmso"].astype(bool)
    sm["well"] = sm["well"].fillna("")
    failed = T.find_failed_wells(sm)
    sm = sm[~sm["sample"].isin(failed["sample"])].reset_index(drop=True)
    sm["dose"] = T.dose_key(sm).values
    prof = load_profiles(D["pb"])
    prof = prof[prof["sample"].isin(sm["sample"])]
    prof = prof[~prof["cell_line_id"].astype(str).str.strip().str.lower().isin(BAD_IDS)]
    by_line = prof.groupby("cell_line_id")["n_cells"].sum()
    lines = sorted(by_line.index[by_line >= T.MIN_LINE_CELLS])
    dropped = sorted(set(by_line.index) - set(lines))
    prof = prof[prof["cell_line_id"].isin(lines)].reset_index(drop=True)
    set_min_cells(args, prof)
    gm = T.read_tables(idx["gene"], ["token_id", "gene_symbol", "ensembl_id"])
    with open(os.path.join(args.out, "build_info.json"), encoding="utf-8") as fh:
        G = json.load(fh)["G"]
    L = len(lines)
    li = {s: i for i, s in enumerate(lines)}
    log(f"Pass 1: gene levels per cell line ({L} lines, {len(prof):,} profiles"
        + (f"; left out {len(dropped)} ids with < {T.MIN_LINE_CELLS} cells" if dropped else "") + ") ...")
    line_sum = np.zeros((L, G))
    line_tot = np.zeros(L)
    line_cells = np.zeros(L)
    for f, g in prof.groupby("file"):
        arr = np.load(f, mmap_mode="r")
        for line, gg in g.groupby("cell_line_id"):
            rows = np.sort(gg["row"].to_numpy())
            line_sum[li[line]] += np.asarray(arr[rows]).sum(axis=0)
            line_tot[li[line]] += gg["total_counts"].sum()
            line_cells[li[line]] += gg["n_cells"].sum()
    keep, symbols, labels, pooled, modules = gene_columns(gm, line_sum, line_tot, G)
    gK = len(keep)
    K = gK + len(modules)
    log(f"  {gK:,} genes at >= {MIN_CPM:g} CPM (of {G:,} tokens) + modules {', '.join(modules)}")
    line_cpm = np.zeros((L, K), dtype=np.float32)
    line_cpm[:, :gK] = 1e6 * line_sum[:, keep] / line_tot[:, None]
    for j, toks in enumerate(modules.values()):
        line_cpm[:, gK + j] = 1e6 * line_sum[:, toks].sum(axis=1) / line_tot
    med = np.median(line_cpm, axis=0)
    expr_mask = line_cpm >= EXPR_FRAC * med[None, :]
    expr_mask[:, gK:] = True
    del line_sum

    cl = T.load_cell_lines(idx)
    lines_df = pd.DataFrame({"cell_line_id": lines, "n_cells_total": line_cells})
    if cl is not None:
        lines_df = lines_df.join(cl, on="cell_line_id")
    ch = line_driver_changes(idx)
    if ch is not None:
        lines_df = lines_df.join(ch, on="cell_line_id")
    abund_ok = line_cells >= ABUND_MIN_FRAC * np.median(line_cells)
    lines_df["in_growth_analysis"] = abund_ok

    log("Pass 2: corrected effects plate by plate ...")
    plates = sorted(sm["plate"].unique(), key=lambda p: (len(p), p))
    W1s, ctxs, As, VAs, R1m, offsets, wells_all = [], [], [], [], [], [], []
    mod_idx = [gK + j for j in range(len(modules))]
    for p in plates:
        smp_ = sm[sm["plate"] == p].reset_index(drop=True)
        wells = list(smp_["sample"])
        counts, tot, nc, ng, r1, base = plate_residuals(prof, smp_, lines, keep, modules, expr_mask)
        drug = ~smp_["is_dmso"].to_numpy()
        cnt = np.isfinite(r1).sum(axis=1)
        W1 = np.nanmedian(r1, axis=1)
        W1[cnt < MIN_LINES] = np.nan
        dm = ~drug
        if dm.any():
            dc = counts[dm].sum(axis=0)
            dt = tot[dm].sum(axis=0)
            dn = nc[dm].sum(axis=0)
            k = np.maximum((tot[dm] > 0).sum(axis=0), 1)[:, None]     # DMSO wells pooled per line: one pseudocount
            dy = np.where((dn >= MIN_CELLS)[:, None],                     # per well, as in the single-well base
                          np.log2((dc + 0.5 * k) / (dt[:, None] + k) * 1e6), np.nan)
            dy[~expr_mask] = np.nan
            offsets.append(np.nanmedian(base - dy, axis=0).astype(np.float32))
        else:
            offsets.append(np.full(K, np.nan, dtype=np.float32))
        cells = nc.sum(axis=1)
        ctx = pd.DataFrame({"sample": wells, "cells": cells,
                            "umi_per_cell": tot.sum(axis=1) / np.maximum(cells, 1),
                            "genes_per_cell": ng.sum(axis=1) / np.maximum(cells, 1)})
        for c in ["cells", "umi_per_cell", "genes_per_cell"]:
            ref = np.median(ctx.loc[drug, c])
            ctx[f"{c}_log2_vs_plate"] = np.log2(np.maximum(ctx[c], 1e-9) / ref)
        ncl = nc[:, abund_ok]
        frac = ncl / np.maximum(ncl.sum(axis=1, keepdims=True), 1)
        eps = 0.5 / max(np.median(ncl.sum(axis=1)), 1)
        ref = np.median(frac[drug], axis=0)
        A = np.full((len(wells), L), np.nan, dtype=np.float32)
        VA = np.full((len(wells), L), np.nan, dtype=np.float32)
        A[:, abund_ok] = np.log2((frac + eps) / (ref[None] + eps))
        VA[:, abund_ok] = 1.0 / ((ncl + 0.5) * math.log(2) ** 2)
        W1s.append(W1.astype(np.float32))
        ctxs.append(ctx)
        As.append(A)
        VAs.append(VA)
        R1m.append(r1[:, :, mod_idx].astype(np.float32))
        wells_all.append(smp_)
        log(f"  {p}: {len(wells)} wells")
        del counts, r1
    W1 = np.concatenate(W1s)
    A = np.concatenate(As)
    VA = np.concatenate(VAs)
    r1m = np.concatenate(R1m)
    wells_df = pd.concat(wells_all, ignore_index=True).merge(pd.concat(ctxs), on="sample", how="left")
    drug = ~wells_df["is_dmso"].to_numpy()
    slot = wells_df["slot"].to_numpy(dtype=float)
    dname = wells_df["drug"].to_numpy(dtype=object)

    log("Well-position correction (leave-drug-out) ...")
    slot_med = np.full((96, K), np.nan, dtype=np.float32)
    for s in range(1, 97):
        rows = np.flatnonzero((slot == s) & drug)
        if rows.size:
            slot_med[s - 1] = np.nanmedian(W1[rows], axis=0)
    eff, n_used = loo_matrix(W1, slot, dname, drug)
    W2 = W1 - eff
    c, s = robust_cols(W2, drug)
    Z = ((W2 - c) / s).astype(np.float32)
    wells_df["position_wells_used"] = n_used
    r2m = r1m - eff[:, None, mod_idx]

    log("Growth (relative abundance) ...")
    effA, _ = loo_matrix(A, slot, dname, drug)
    A2 = A - effA
    cA, sA = robust_cols(A2, drug)
    cvar = np.nanmedian(VA[drug], axis=0)
    wellvar = np.maximum(sA ** 2 - cvar, (0.25 * sA) ** 2)
    zA = ((A2 - cA) / np.sqrt(wellvar[None] + VA)).astype(np.float32)

    log("Per drug and dose ...")
    wd = wells_df[drug]
    groups = wd.groupby(["drug", "dose"], sort=True).indices
    keys = sorted(groups)
    wd_idx = np.flatnonzero(drug)
    Dn = len(keys)
    DD_lfc = np.full((Dn, K), np.nan, dtype=np.float32)
    DD_z = np.full((Dn, K), np.nan, dtype=np.float32)
    DD_A = np.full((Dn, L), np.nan, dtype=np.float32)
    DD_Az = np.full((Dn, L), np.nan, dtype=np.float32)
    DD_r2m = np.full((Dn, L, len(mod_idx)), np.nan, dtype=np.float32)
    dd_of_well = np.full(len(wells_df), -1)
    rows_dd = []
    for d, key in enumerate(keys):
        ii = wd_idx[groups[key]]
        dd_of_well[ii] = d
        DD_lfc[d] = np.nanmean(W2[ii], axis=0)
        k = np.isfinite(Z[ii]).sum(axis=0)
        DD_z[d] = np.where(k > 0, np.nansum(Z[ii], axis=0) / np.sqrt(np.maximum(k, 1)), np.nan)
        DD_A[d] = np.nanmean(A2[ii], axis=0)
        kA = np.isfinite(zA[ii]).sum(axis=0)
        DD_Az[d] = np.where(kA > 0, np.nansum(zA[ii], axis=0) / np.sqrt(np.maximum(kA, 1)), np.nan)
        DD_r2m[d] = np.nanmean(r2m[ii], axis=0)
        w = wells_df.iloc[ii]
        rows_dd.append({"drug": key[0], "dose": key[1], "conc": w["conc"].iloc[0], "n_wells": len(ii),
                        "wells": ",".join(sorted(set(w["well"].astype(str)))),
                        "plates": ",".join(sorted(set(w["plate"].astype(str)))),
                        "cells_log2_vs_plate": w["cells_log2_vs_plate"].mean(),
                        "umi_per_cell_log2_vs_plate": w["umi_per_cell_log2_vs_plate"].mean(),
                        "genes_per_cell_log2_vs_plate": w["genes_per_cell_log2_vs_plate"].mean()})
    dd = pd.DataFrame(rows_dd)
    for j, name in enumerate(modules):
        dd[f"{name}_lfc"] = DD_lfc[:, gK + j]
        dd[f"{name}_z"] = DD_z[:, gK + j]
    dd["flags"] = [flags_for(r) for _, r in dd.iterrows()]
    log("FDR within each gene ...")
    q_up = bh_columns(norm_sf(DD_z)).astype(np.float32)
    q_dn = bh_columns(norm_sf(-DD_z)).astype(np.float32)
    sig_up = (q_up < Q_CUT) & (DD_lfc >= LFC_MIN)
    sig_dn = (q_dn < Q_CUT) & (DD_lfc <= -LFC_MIN)
    sig_up[:, gK:] = False
    sig_dn[:, gK:] = False
    dd["n_genes_up"] = sig_up.sum(axis=1)
    dd["n_genes_down"] = sig_dn.sum(axis=1)
    dd["n_sig_genes"] = dd["n_genes_up"] + dd["n_genes_down"]
    drugs_meta = T.load_drugs(idx)
    dd = dd.join(drugs_meta, on="drug")

    log("Pass 3: how strongly each cell line shows each drug's consensus response ...")
    sig = sig_up | sig_dn
    n_sig = sig.sum(axis=1)
    beta = np.full((len(wells_df), L), np.nan, dtype=np.float32)
    rcor = np.full((len(wells_df), L), np.nan, dtype=np.float32)
    off = 0
    for p in plates:
        smp_ = sm[sm["plate"] == p].reset_index(drop=True)
        Wp = len(smp_)
        todo = [j for j in range(Wp) if dd_of_well[off + j] >= 0 and n_sig[dd_of_well[off + j]] >= MIN_SIG_BETA]
        if todo:
            r1 = plate_residuals(prof, smp_, lines, keep, modules, expr_mask)[4]
            for j in todo:
                d = dd_of_well[off + j]
                cols = np.flatnonzero(sig[d])
                X = r1[j][:, cols] - eff[off + j, cols][None, :]
                beta[off + j], rcor[off + j] = line_fit(X, DD_lfc[d, cols])
            del r1
        off += Wp
    DD_beta = np.full((Dn, L), np.nan, dtype=np.float32)
    DD_rcor = np.full((Dn, L), np.nan, dtype=np.float32)
    for d, key in enumerate(keys):
        ii = wd_idx[groups[key]]
        DD_beta[d] = np.nanmean(beta[ii], axis=0)
        DD_rcor[d] = np.nanmean(rcor[ii], axis=0)

    genes_df = pd.DataFrame({"col": np.arange(K),
                             "kind": ["gene"] * gK + ["module"] * len(modules),
                             "token": list(keep) + [-1] * len(modules),
                             "symbol": list(symbols) + list(modules),
                             "label": list(labels) + list(modules),
                             "pooled_cpm": list(pooled[keep]) + list(np.median(line_cpm[:, gK:], axis=0)),
                             "median_line_cpm": med, "n_lines_expressing": expr_mask.sum(axis=0)})
    out = D["fx"]
    genes_df.to_csv(os.path.join(out, "genes.csv"), index=False)
    lines_df.to_csv(os.path.join(out, "lines.csv"), index=False)
    wells_df.to_csv(os.path.join(out, "wells.csv"), index=False)
    dd.to_csv(os.path.join(out, "drugdose.csv"), index=False)
    failed.to_csv(os.path.join(out, "failed_wells.csv"), index=False)
    pd.DataFrame({"plate": plates}).to_csv(os.path.join(out, "plates.csv"), index=False)
    for name, arr in [("W1", W1), ("W2", W2.astype(np.float32)), ("Z", Z), ("slot_median", slot_med),
                      ("plate_offset", np.vstack(offsets)), ("DD_lfc", DD_lfc), ("DD_z", DD_z),
                      ("DD_qup", q_up), ("DD_qdn", q_dn), ("line_cpm", line_cpm), ("expr_mask", expr_mask),
                      ("A2", A2.astype(np.float32)), ("zA", zA), ("VA", VA), ("DD_A", DD_A), ("DD_Az", DD_Az),
                      ("r2_modules", r2m.astype(np.float32)), ("DD_r2_modules", DD_r2m),
                      ("beta", beta), ("rcor", rcor), ("DD_beta", DD_beta), ("DD_rcor", DD_rcor)]:
        save_npy(os.path.join(out, f"{name}.npy"), arr)
    with open(os.path.join(out, "modules.json"), "w", encoding="utf-8") as fh:
        json.dump({k: [int(t) for t in v] for k, v in modules.items()}, fh)
    with open(os.path.join(out, "README_effects.md"), "w", encoding="utf-8") as fh:
        fh.write(EFFECTS_README)
    with open(os.path.join(out, "complete.json"), "w", encoding="utf-8") as fh:
        json.dump({"version": EFFECTS_VERSION}, fh)
    log(f"Effects done: {gK:,} genes x {Dn:,} drug-doses x {L} lines -> {out}")


EFFECTS_README = """# effects/ - what each file holds (load .npy with numpy.load(path, mmap_mode='r'))
genes.csv      one row per COLUMN of the gene matrices: col, kind (gene/module), token, symbol, label, pooled_cpm,
               median_line_cpm, n_lines_expressing. Modules S_PHASE, G2M_PHASE, PROTEASOME are summed gene sets.
lines.csv      one row per cell line (row order = columns of the line matrices): id, cell_name, Organ, drivers,
               driver_changes (protein changes), n_cells_total, in_growth_analysis.
wells.csv      one row per well used (row order = rows of W1/W2/Z/A2/zA/beta): sample, plate, well, slot, drug, conc,
               dose, is_dmso, cells and per-cell UMI/gene counts vs plate (log2).
drugdose.csv   one row per drug and dose (row order = rows of DD_*): wells, plates, cell loss, transcription, module
               shifts, flags, n_genes_up/down (q < 0.1 and >= 1.2x), targets, moa_fine, moa_broad.
W1.npy, W2.npy wells x genes: log2 effect before / after the well-position correction (median over cell lines).
Z.npy          wells x genes: W2 scored against the spread of drug wells (robust z).
DD_lfc.npy     drug-doses x genes: corrected log2 fold change (mean over the drug-dose's wells). fold = 2**lfc.
DD_z.npy       drug-doses x genes: combined z (Stouffer over the drug-dose's wells/plates).
DD_qup.npy, DD_qdn.npy  drug-doses x genes: BH q-value for an increase / decrease (within each gene).
slot_median.npy 96 well positions (A1 = row 0 ... H12 = row 95) x genes: median shift of all drugs in that position.
plate_offset.npy plates (plates.csv order) x genes: how far the plate's DMSO wells sit below its drug median.
line_cpm.npy, expr_mask.npy  lines x genes: level (all wells pooled, CPM) and 'expressed' flag.
A2.npy, zA.npy, VA.npy  wells x lines: log2 relative abundance (position-corrected), its z, counting variance.
DD_A.npy, DD_Az.npy  drug-doses x lines: the same per drug and dose (negative = line depleted vs the others).
beta.npy, DD_beta.npy  wells / drug-doses x lines: how strongly each line shows the drug's consensus response
               (slope on the consensus over the drug-dose's significant genes; 1 = typical line, 0 = no response).
               Only for drug-doses with >= 20 significant genes. rcor.npy / DD_rcor.npy: the matching correlation.
r2_modules.npy wells x lines x 3 and DD_r2_modules.npy drug-doses x lines x 3: per-line S, G2M, PROTEASOME effects.
"""


# ============================================================================= shared loading for angles
class FX:
    """Lazy access to the effects."""

    def __init__(self, out):
        self.out = out
        self.d = os.path.join(out, "effects")
        if not effects_ready(out):
            sys.exit("effects missing, incomplete or from an older version of tahoe_atlas.py; "
                     "run 'compute' (or 'effects') again")
        global MIN_CELLS
        try:
            with open(os.path.join(self.d, "info.json"), encoding="utf-8") as fh:
                MIN_CELLS = json.load(fh)["min_cells"]
        except (OSError, KeyError, ValueError):
            pass
        self.genes = pd.read_csv(os.path.join(self.d, "genes.csv"))
        self.lines = pd.read_csv(os.path.join(self.d, "lines.csv"), dtype={"cell_line_id": str})
        self.wells = pd.read_csv(os.path.join(self.d, "wells.csv"),
                                 dtype={"sample": str, "plate": str, "drug": str, "dose": str})
        self.dd = pd.read_csv(os.path.join(self.d, "drugdose.csv"), dtype={"drug": str, "dose": str})
        for c in ("flags", "moa_fine", "moa_broad", "targets"):
            if c in self.dd:
                self.dd[c] = self.dd[c].fillna("").astype(str)
            else:
                self.dd[c] = ""
        for c in ("Organ", "drivers", "driver_changes", "cell_name"):
            if c in self.lines:
                self.lines[c] = self.lines[c].fillna("").astype(str)
            else:
                self.lines[c] = ""
        self.plates = pd.read_csv(os.path.join(self.d, "plates.csv"), dtype={"plate": str})["plate"].tolist()
        self._c = {}
        self.gmask = (self.genes["kind"] == "gene").to_numpy()
        self.gi = np.flatnonzero(self.gmask)
        self.mod_col = {r.symbol: int(r.col) for r in self.genes.itertuples() if r.kind == "module"}
        self.label = self.genes["label"].astype(str).to_numpy()
        nm = self.lines["cell_name"].astype(str)
        self.line_name = np.where(nm == "", self.lines["cell_line_id"], nm)
        self.drug_w = ~self.wells["is_dmso"].astype(bool).to_numpy()
        self.rows_of_drug = {d: g.sort_values("conc").index.to_numpy() for d, g in self.dd.groupby("drug")}

    def __getattr__(self, name):
        if name.startswith("_") or name in ("d",):
            raise AttributeError(name)
        if name not in self._c:
            path = os.path.join(self.d, f"{name}.npy")
            if not os.path.exists(path):
                raise AttributeError(name)
            self._c[name] = np.load(path, mmap_mode="r")
        return self._c[name]

    def col_of(self, symbol):
        g = self.genes
        s = symbol.upper()
        hit = g[(g["symbol"].astype(str).str.upper() == s) | (g["label"].astype(str).str.upper() == s)]
        return None if hit.empty else int(hit.iloc[0]["col"])

    def dose_pattern(self, col, drug, sign=1):
        """(pattern, z by dose) of one drug for one gene column."""
        rows = self.rows_of_drug.get(drug)
        if rows is None:
            return "", ""
        zs = (np.asarray(self.DD_z[rows, col], dtype=float) * sign).tolist()
        return dose_shape(zs), T.fmt_list([z * sign for z in zs])

    def svd(self):
        """Genes x drug wells (W2, standardised per gene) and its SVD; cached."""
        if getattr(self, "_svd", None) is None:
            X = np.nan_to_num(np.asarray(self.W2, dtype=np.float64)[self.drug_w][:, self.gi]).T
            X = X - X.mean(axis=1, keepdims=True)
            sd = X.std(axis=1, keepdims=True)
            sd[sd == 0] = 1
            X = X / sd
            U, S, Vt = np.linalg.svd(X, full_matrices=False)
            self._svd = (X, U, S, Vt)
        return self._svd


def signif(fx):
    q_up, q_dn, lfc = np.asarray(fx.DD_qup), np.asarray(fx.DD_qdn), np.asarray(fx.DD_lfc)
    up = (q_up < Q_CUT) & (lfc >= LFC_MIN)
    dn = (q_dn < Q_CUT) & (lfc <= -LFC_MIN)
    up[:, ~fx.gmask] = False
    dn[:, ~fx.gmask] = False
    return up, dn


def top_list(labels, values, n, reverse=True):
    values = np.asarray(values, dtype=float)
    o = np.argsort(-values if reverse else values)
    o = [i for i in o if np.isfinite(values[i])][:n]
    return "; ".join(f"{labels[i]} {values[i]:+.2f}" for i in o)


def drug_best_dose(fx):
    """Row of each drug's strongest dose (most significant genes; ties -> higher dose)."""
    t = fx.dd[["drug", "conc", "n_sig_genes"]].copy()
    best = t.sort_values(["drug", "n_sig_genes", "conc"], ascending=[True, False, False]).drop_duplicates("drug")
    return best.index.to_numpy()


def responsive_genes(fx, min_sig=3):
    up, dn = signif(fx)
    n = (up | dn).sum(axis=0)
    r = np.flatnonzero(fx.gmask & (n >= min_sig))
    return r if r.size >= 50 else fx.gi


def unit_rows(X):
    X = np.nan_to_num(np.asarray(X, dtype=np.float64))
    nrm = np.linalg.norm(X, axis=1)
    nrm[nrm == 0] = 1
    return X / nrm[:, None]


def write_brief(folder, title, task, files, extra=""):
    with open(os.path.join(folder, "brief.md"), "w", encoding="utf-8") as fh:
        fh.write(f"# Angle: {title}\n\n## Your task\n{task.strip()}\n\n## Data in this folder\n")
        for name, desc in files:
            fh.write(f"- `{name}`: {desc}\n")
        fh.write("\n" + METHODS.replace("< 30 cells", f"< {MIN_CELLS} cells") + "\n" + RULEBOOK + "\n" + extra
                 + "\n" + REPORT_RULES)


METHODS = """## How the numbers were made
- Source: Tahoe-100M: ~96M single cells; 50 cancer cell lines pooled in every well; 379 drugs at 0.05, 0.5 and
  5 uM; 14 plates of 96 wells; mRNA after 24 h. Cells of one line in one well are summed into a profile
  (profiles with < 30 cells are left out).
- Effect of a drug-dose on a gene ('lfc', log2; fold change = 2^lfc): the well's log2 CPM minus the median of all
  drug wells on the same plate for the same cell line (NOT the DMSO wells), median across cell lines, then minus
  the leave-drug-out well-position effect (median of the other drugs that sat in the same well position).
- z: the effect scored against the spread of all drug wells for that gene (median/MAD), combined over the
  drug-dose's wells (Stouffer) when it sat on two plates. q_up / q_down: Benjamini-Hochberg within each gene
  across all ~1,100 drug-doses. 'Significant' means q < 0.10 and a fold change of at least 1.2x.
- Lines that barely express a gene (< 25% of the median line, e.g. deleted genes reading only background RNA from
  the other pooled lines) are left out for that gene. Failed wells (almost no cells while the same drug was fine
  elsewhere) are excluded.
- Growth: each line's share of the cells in a well vs its usual share on that plate (log2 relative abundance);
  same position correction; its z includes counting noise. Negative = the line was depleted more than the others.
- Per-line response strength (beta): for drug-doses with >= 20 significant genes, how strongly each line shows the
  consensus response over those genes (1 = like the typical line, 0 = no response, > 1 = stronger).
- Context per drug-dose: cells_log2_vs_plate (cell loss), umi/genes_per_cell_log2_vs_plate (transcription
  shutdown), S_PHASE / G2M_PHASE / PROTEASOME module shifts. 'flags' summarises them.
"""

RULEBOOK = """## Rules for interpreting (learned on this dataset; follow them)
1. Artifacts first. Before calling an effect real, check: toxicity (wells that lost > half their cells);
   transcription or translation shutdown (UMIs or genes per cell drop: short, stable housekeeping, ribosomal and
   mitochondrial mRNAs then rise and long or unstable mRNAs fall, in relative terms); cell-cycle composition
   (drugs that hold cells in S or G2/M raise every cycle-linked mRNA); well position (some positions, e.g. H1 and
   D10, shifted specific genes on every plate; corrected, but see the quality angle). The DMSO controls sit in
   corner wells and plate 2's DMSO is off: never use DMSO-based numbers.
2. Dose consistency. Real effects usually grow with dose or appear at the top dose. A hit at a low dose only,
   absent at higher doses, is most likely noise. Say what the dose pattern is.
3. Breadth. Check how many cell lines move. An effect carried by one or two lines is a line-specific observation.
4. Specific vs broad. Many drugs move big programs together (growth and ribosome biogenesis, proteasome,
   chaperones, cell cycle, stress, cholesterol). Say whether a change belongs to such a program or is specific.
5. Statistics. With ~1,100 drug-doses and ~15,000 genes, z > 3 happens thousands of times by chance: rely on q,
   effect size and consistency. Report fold changes (not log2) with q and the number of lines.
6. Known biology as a check. Look for expected effects (e.g. mTOR/PI3K inhibitors lower proteasome and
   ribosome-biogenesis genes; proteasome inhibitors raise proteasome subunits; HSP90 inhibitors raise
   heat-shock genes; statins raise cholesterol-synthesis genes; BRAF/MEK inhibitors deplete BRAF-mutant lines;
   KRAS G12C inhibitors deplete G12C lines) and say whether the data show them.
7. mRNA after 24 h only: no claims about protein, function or causality. Label hypotheses as hypotheses.
   Treat non-polyadenylated or multi-mapping RNAs as noise in this assay: 7SK / RN7SK* pseudogenes, RNU*, snoRNAs,
   ribosomal-protein pseudogenes (RPS*P*, RPL*P*), MT-* pseudogenes (MTND*P*, MTATP*P*), unnamed ENSG lncRNAs and
   the replication-dependent histone genes (H1-*, H2AC*, H2BC*, H3C*, H4C*; these also follow S phase). Do not base
   a finding on them.
8. Every number in your report must come from a query you ran on the files; name the file it came from.
"""

REPORT_RULES = """## Your report
Write `report.md` in this folder, in Markdown:
- `# <title>`, then a first paragraph that answers the angle's main question with numbers.
- Short sections with the findings, most important first; tables (at most 15 rows each) for ranked items;
  fold changes with q-values and the number of cell lines.
- `## Caveats`: which artifact checks you ran and what they showed.
- `## Leads to test`: up to 5 concrete follow-ups (drug, dose, cell line, readout).
- Plain language, at most ~1,500 words, no methods recap beyond one sentence. Do not pad.
Work unattended: never ask questions; if something is unclear, decide, and say what you assumed.
"""


def deeper_queries(out):
    py, me = agent_python(), shell_quote(os.path.abspath(__file__))
    o = os.path.abspath(out)
    fx = os.path.join(o, "effects")
    cards = [os.path.join(o, "angles", a, "cards") + os.sep for a in ("drugs", "cell_lines")]
    return f"""## Deeper queries
- Cards: `{py} {me} --out {shell_quote(o)} lookup gene <SYMBOL>` (also `drug <NAME>`, `line <NAME>`, `corr <SYMBOL>`).
  Ready-made cards for every drug and line: `{cards[0]}` and `{cards[1]}`.
- Whole matrices: `{fx}` (read `{os.path.join(fx, "README_effects.md")}` first; numpy.load(path, mmap_mode='r')).
- Python (run it as `{py}`) with numpy, pandas and pyarrow is available (scipy or others may be missing: check
  before relying on them). Keep any scripts you write in this folder. Do not read the raw single-cell files
  (hundreds of GB).
"""


# ============================================================================= cards (every drug, every line)
def card_drug(fx, drug, n_genes=15):
    dd = fx.dd
    rows = fx.rows_of_drug.get(drug)
    if rows is None:
        return f"# {drug}\n\nNot in the data.\n"
    r0 = dd.loc[rows[0]]
    gi = fx.gi
    lab = fx.label
    lfc, z = np.asarray(fx.DD_lfc), np.asarray(fx.DD_z)
    qu, qd = np.asarray(fx.DD_qup), np.asarray(fx.DD_qdn)
    DA, DAz, DB = np.asarray(fx.DD_A), np.asarray(fx.DD_Az), np.asarray(fx.DD_beta)
    up, dn = signif(fx)
    out = [f"# {drug}", f"MoA: {r0['moa_fine'] or '-'} ({r0['moa_broad'] or '-'}); targets: {r0['targets'] or '-'}"]
    for i in rows:
        r = dd.loc[i]
        out.append(f"\n## {r['conc']:g} uM: wells {r['wells']} (plates {r['plates']})")
        out.append(f"cells {2 ** r['cells_log2_vs_plate']:.2f}x of plate median; UMIs/cell "
                   f"{2 ** r['umi_per_cell_log2_vs_plate']:.2f}x; genes/cell {2 ** r['genes_per_cell_log2_vs_plate']:.2f}x; "
                   f"flags: {r['flags'] or '-'}")
        mods = "; ".join(f"{m} {2 ** r[f'{m}_lfc']:.2f}x (z {r[f'{m}_z']:.1f})" for m in fx.mod_col if f"{m}_lfc" in r)
        out.append(f"modules: {mods}")
        out.append(f"significant genes (q < 0.1, >= 1.2x): {int(up[i].sum())} up, {int(dn[i].sum())} down")
        for name, mask, sign, qq in (("up", up[i], 1, qu), ("down", dn[i], -1, qd)):
            zz = np.where(mask[gi], z[i, gi] * sign, -np.inf)
            o = [k for k in np.argsort(-zz)[:n_genes] if np.isfinite(zz[k])]
            if o:
                out.append(f"top {name}: " + ", ".join(f"{lab[gi[k]]} {2 ** lfc[i, gi[k]]:.2f}x (q {qq[i, gi[k]]:.1g})"
                                                       for k in o))
        a, az = DA[i], DAz[i]
        o = [k for k in np.argsort(np.nan_to_num(az, nan=99))[:5] if np.isfinite(az[k])]
        if o:
            out.append("most depleted lines: " + ", ".join(f"{fx.line_name[k]} {2 ** a[k]:.2f}x (z {az[k]:.1f})" for k in o))
        b = DB[i]
        if np.isfinite(b).sum() >= 10:
            o = np.argsort(np.where(np.isfinite(b), b, np.inf))
            low = ", ".join(f"{fx.line_name[k]} {b[k]:.2f}" for k in o[:4] if np.isfinite(b[k]))
            out.append(f"response strength across lines (beta): median {np.nanmedian(b):.2f}; weakest: {low}")
    return "\n".join(out) + "\n"


def card_line(fx, i, n=12):
    r = fx.lines.iloc[i]
    dd = fx.dd
    DA, DAz, DB = np.asarray(fx.DD_A), np.asarray(fx.DD_Az), np.asarray(fx.DD_beta)
    lc = np.asarray(fx.line_cpm)
    gi = fx.gi
    out = [f"# {fx.line_name[i]} ({r['cell_line_id']})",
           f"organ: {r['Organ'] or '-'}; drivers: {r['drivers'] or '-'}",
           f"protein changes: {r['driver_changes'] or '-'}",
           f"cells: {int(r['n_cells_total']):,}; in growth analysis: {bool(r['in_growth_analysis'])}"]
    other = np.delete(np.arange(len(fx.lines)), i)
    ratio = np.log2((lc[i, gi] + 1) / (np.median(lc[other][:, gi], axis=0) + 1))
    out.append("genes highest vs other lines (log2): " + top_list(fx.label[gi], ratio, n))
    out.append("genes lowest vs other lines (log2): " + top_list(fx.label[gi], ratio, n, reverse=False))
    az = DAz[:, i]
    o = [k for k in np.argsort(np.nan_to_num(az, nan=99))[:n] if np.isfinite(az[k])]
    if o:
        out.append("\n## Most depleted relative to the other lines in the same wells")
        out += [f"- {dd.at[k, 'drug']} {dd.at[k, 'conc']:g} uM: {2 ** DA[k, i]:.2f}x (z {az[k]:.1f}; {dd.at[k, 'moa_fine'] or '-'})"
                for k in o]
    o = [k for k in np.argsort(-np.nan_to_num(az, nan=-99))[:5] if np.isfinite(az[k])]
    if o:
        out.append("\n## Most enriched (spared)")
        out += [f"- {dd.at[k, 'drug']} {dd.at[k, 'conc']:g} uM: {2 ** DA[k, i]:.2f}x (z {az[k]:.1f})" for k in o]
    b = DB[:, i]
    med_all = np.nanmedian(DB, axis=1)
    strong = np.isfinite(b) & (med_all >= 0.8) & (dd["n_sig_genes"].to_numpy() >= 50)
    if strong.sum() >= 5:
        out.append(f"\n## Transcriptional response (beta; 1 = typical line): median {np.nanmedian(b[strong]):.2f} over "
                   f"{int(strong.sum())} strong drug-doses")
        o = [k for k in np.argsort(np.where(strong, b, np.inf))[:6] if strong[k]]
        out.append("weakest vs other lines: " + ", ".join(f"{dd.at[k, 'drug']} {dd.at[k, 'conc']:g} ({b[k]:.2f})" for k in o))
        o = [k for k in np.argsort(np.where(strong, -b, np.inf))[:6] if strong[k]]
        out.append("strongest: " + ", ".join(f"{dd.at[k, 'drug']} {dd.at[k, 'conc']:g} ({b[k]:.2f})" for k in o))
    return "\n".join(out) + "\n"


def card_gene(fx, c, n=15):
    g = fx.genes.iloc[c]
    dd = fx.dd
    t = dd[["drug", "conc", "flags"]].copy()
    t["fold"] = 2 ** np.asarray(fx.DD_lfc)[:, c]
    t["z"] = np.asarray(fx.DD_z)[:, c]
    t["q_up"] = np.asarray(fx.DD_qup)[:, c]
    t["q_down"] = np.asarray(fx.DD_qdn)[:, c]
    t["z_by_dose_up"] = [fx.dose_pattern(c, d)[1] for d in t["drug"]]
    lc = np.asarray(fx.line_cpm)[:, c]
    sm = np.asarray(fx.slot_median)[:, c]
    w = int(np.nanargmax(np.where(np.isfinite(sm), np.abs(sm), -1)))
    lines = pd.DataFrame({"line": fx.line_name, "cpm": lc}).sort_values("cpm")
    out = [f"# {g['label']}",
           f"pooled {g['pooled_cpm']:.1f} CPM; expressed in {int(g['n_lines_expressing'])} lines; lowest lines: "
           + ", ".join(f"{a} {b:.1f}" for a, b in lines.head(5).values) + "; highest: "
           + ", ".join(f"{a} {b:.1f}" for a, b in lines.tail(3).values),
           f"largest well-position shift: {T.well_name(w + 1)} {2 ** sm[w]:.2f}x (corrected for)",
           "\n## Strongest increases", t.sort_values("z", ascending=False).head(n).round(3).to_string(index=False),
           "\n## Strongest decreases", t.sort_values("z").head(n).round(3).to_string(index=False)]
    return "\n".join(out) + "\n"


def card_corr(fx, c, n=20):
    X, U, S, Vt = fx.svd()
    k = int(np.flatnonzero(fx.gi == c)[0])
    out = [f"# Genes co-regulated with {fx.label[c]} across drug wells"]
    for npc in (0, N_PCS):
        M = X - (U[:, :npc] * S[:npc]) @ Vt[:npc] if npc else X
        r = (M @ M[k]) / (np.linalg.norm(M, axis=1) * np.linalg.norm(M[k]) + 1e-12)
        r[k] = np.nan
        o = np.argsort(-np.nan_to_num(r, nan=-9))
        tag = "raw" if npc == 0 else f"after removing {npc} broad components"
        out.append(f"\n{tag}\n  up:   " + ", ".join(f"{fx.label[fx.gi[i]]} {r[i]:.2f}" for i in o[:n])
                   + "\n  down: " + ", ".join(f"{fx.label[fx.gi[i]]} {r[i]:.2f}" for i in o[::-1][1:n + 1]))
    return "\n".join(out) + "\n"


def write_cards(fx, folder, kind):
    cd = os.path.join(folder, "cards")
    os.makedirs(cd, exist_ok=True)
    index = []
    if kind == "drug":
        for drug in sorted(fx.rows_of_drug):
            fn = safe_name(drug) + ".md"
            with open(os.path.join(cd, fn), "w", encoding="utf-8") as fh:
                fh.write(card_drug(fx, drug))
            r = fx.dd.loc[fx.rows_of_drug[drug]]
            index.append({"drug": drug, "card": f"cards/{fn}", "moa_fine": r["moa_fine"].iloc[0],
                          "max_sig_genes": int(r["n_sig_genes"].max())})
    else:
        for i in range(len(fx.lines)):
            fn = safe_name(fx.line_name[i]) + ".md"
            with open(os.path.join(cd, fn), "w", encoding="utf-8") as fh:
                fh.write(card_line(fx, i))
            index.append({"line": fx.line_name[i], "card": f"cards/{fn}", "organ": fx.lines.at[i, "Organ"]})
    pd.DataFrame(index).to_csv(os.path.join(cd, "index.csv"), index=False)


# ============================================================================= angles
def angle_quality(fx, folder):
    sm = np.asarray(fx.slot_median)
    g = fx.gmask
    gi = fx.gi
    labels = fx.label
    w = fx.wells
    # each gene's shift at a position scored against that gene's own spread over all 96 positions: a real
    # position artifact (MTAP at H1) stands out of its gene's spread; noisy low-level RNAs (7SK, RNU, pseudogenes)
    # shift a lot everywhere and do not. Ranked only among shifts of at least 1.2x.
    cen = np.nanmedian(sm, axis=0)
    mad = 1.4826 * np.nanmedian(np.abs(sm - cen), axis=0)
    zpos = (sm - cen) / np.where(mad > 0, mad, np.nan)
    zrank = np.where(np.isfinite(zpos) & (np.abs(sm) >= LFC_MIN), np.abs(zpos), -1)
    rows = []
    for s in range(96):
        v = sm[s, g]
        here = (w["slot"] == s + 1) & fx.drug_w
        big = int(np.argmax(np.where(np.isfinite(v), np.abs(v), -1)))
        art = int(np.argmax(zrank[s, g]))
        has_art = zrank[s, g][art] >= 0
        rows.append({"well": T.well_name(s + 1), "n_drug_wells": int(here.sum()),
                     "artifact_gene": labels[g][art] if has_art else "",
                     "artifact_shift_log2": float(v[art]) if has_art else np.nan,
                     "artifact_z_vs_gene_spread": float(zpos[s, g][art]) if has_art else np.nan,
                     "largest_shift_gene": labels[g][big] if np.isfinite(v[big]) else "",
                     "largest_shift_log2": float(v[big]),
                     "genes_up_over_1.2x": int((v > LFC_MIN).sum()), "genes_down_over_1.2x": int((v < -LFC_MIN).sum()),
                     "median_abs_shift": float(np.nanmedian(np.abs(v))),
                     "top_up": top_list(labels[g], v, 10), "top_down": top_list(labels[g], v, 10, reverse=False),
                     "drugs": ", ".join(sorted(set(w.loc[here, "drug"])))})
    # sorted by the strongest gene-specific artifact (z against the gene's own spread over positions), not by the
    # raw size of a shift, which noisy low-level RNAs dominate
    pd.DataFrame(rows).sort_values("artifact_z_vs_gene_spread", key=np.abs, ascending=False,
                                   na_position="last").to_csv(os.path.join(folder, "position_effects.csv"), index=False)
    zr = zrank[:, gi]
    best = np.argmax(zr, axis=0)
    ok = zr[best, np.arange(gi.size)] >= 0
    ps = pd.DataFrame({"gene": labels[gi], "worst_well": [T.well_name(b + 1) for b in best],
                       "shift_log2": sm[best, gi], "z_vs_gene_spread": zpos[best, gi]})[ok]
    ps = ps.assign(abs_shift=ps["shift_log2"].abs())
    ps.sort_values("z_vs_gene_spread", key=np.abs, ascending=False).head(500).to_csv(
        os.path.join(folder, "position_sensitive_genes.csv"), index=False)
    off = np.asarray(fx.plate_offset)
    prow = []
    for i, p in enumerate(fx.plates):
        v = off[i, g]
        dmso = w.loc[(w["plate"] == p) & ~fx.drug_w, "well"].tolist()
        prow.append({"plate": p, "dmso_wells": ",".join(map(str, dmso)), "median_offset": float(np.nanmedian(v)),
                     "genes_offset_over_1.2x": int((np.abs(v) > LFC_MIN).sum()),
                     "top_dmso_low": top_list(labels[g], v, 10), "top_dmso_high": top_list(labels[g], v, 10, False)})
    pd.DataFrame(prow).to_csv(os.path.join(folder, "plate_dmso_offsets.csv"), index=False)
    shutil.copy(os.path.join(fx.d, "failed_wells.csv"), os.path.join(folder, "failed_wells.csv"))
    # replicate agreement: drug-doses on two plates vs random pairs of different drugs on different plates
    Xn = unit_rows(np.asarray(fx.W2)[:, responsive_genes(fx)])
    Xn = Xn - Xn.mean(axis=1, keepdims=True)
    Xn = unit_rows(Xn)
    wd = w[fx.drug_w]
    reps = []
    for (d, dose), gg in wd.groupby(["drug", "dose"]):
        if len(gg) >= 2:
            a, b = gg.index[0], gg.index[1]
            reps.append({"drug": d, "dose": dose, "plates": ",".join(gg["plate"].astype(str)),
                         "wells": ",".join(gg["well"].astype(str)), "r": float(Xn[a] @ Xn[b])})
    rng = np.random.default_rng(0)
    idx = wd.index.to_numpy()
    nulls = []
    for _ in range(3000):
        a, b = rng.choice(idx, 2, replace=False)
        if w.at[a, "drug"] != w.at[b, "drug"] and w.at[a, "plate"] != w.at[b, "plate"]:
            nulls.append(float(Xn[a] @ Xn[b]))
    nulls = np.array(nulls)
    rep = pd.DataFrame(reps, columns=["drug", "dose", "plates", "wells", "r"])
    rep["pct_above_random_pairs"] = [100 * float((nulls < r).mean()) for r in rep["r"]]
    rep.sort_values("r").to_csv(os.path.join(folder, "replicates.csv"), index=False)
    Zd = np.asarray(fx.Z)[fx.drug_w][:, gi]
    cal = pd.DataFrame({"gene": labels[gi], "pct_abs_z_over_1.96": 100 * np.nanmean(np.abs(Zd) > 1.96, axis=0),
                        "pct_abs_z_over_3": 100 * np.nanmean(np.abs(Zd) > 3, axis=0)})
    cal.sort_values("pct_abs_z_over_3", ascending=False).to_csv(os.path.join(folder, "calibration_by_gene.csv"),
                                                                index=False)
    summary = {"genes": int(gi.size), "drug_wells": int(fx.drug_w.sum()), "drug_doses": int(len(fx.dd)),
               "cell_lines": int(len(fx.lines)),
               "median_pct_abs_z_over_1.96": float(cal["pct_abs_z_over_1.96"].median()),
               "median_pct_abs_z_over_3": float(cal["pct_abs_z_over_3"].median()),
               "replicate_pairs": int(len(rep)), "replicate_median_r": float(rep["r"].median()) if len(rep) else None,
               "random_pair_median_r": float(np.median(nulls)) if nulls.size else None,
               "random_pair_95th_pct_r": float(np.percentile(nulls, 95)) if nulls.size else None,
               "failed_wells": int(len(pd.read_csv(os.path.join(folder, "failed_wells.csv"))))}
    with open(os.path.join(folder, "summary.json"), "w", encoding="utf-8") as fh:
        json.dump(summary, fh, indent=1)
    write_brief(folder, TITLES["quality"], """
How trustworthy are these data, and where are the traps? Quantify the well-position artifacts (which positions,
how many genes, which genes), the plate DMSO offsets, the failed wells, how reproducible drug signatures are on the
replicate plates compared with random pairs, and whether the z-scores are calibrated (about 5% beyond 1.96 expected
when most drugs do nothing to a gene; much more means the noise is underestimated for that gene). Conclude with
what the other analyses should watch out for.
""", [("summary.json", "headline numbers"),
      ("position_effects.csv", "per well position, sorted by its strongest gene-specific artifact (artifact_gene: "
                               "the shift >= 1.2x that stands out most from that gene's spread over all positions, "
                               "artifact_z_vs_gene_spread); also its largest raw shift, genes shifted > 1.2x by every "
                               "drug placed there, top genes, drugs"),
      ("position_sensitive_genes.csv", "500 genes whose worst position stands out most from their own spread "
                                       "over positions (z_vs_gene_spread; shifts >= 1.2x only)"),
      ("plate_dmso_offsets.csv", "per plate: how far DMSO sits from the drug median (>0 = DMSO low), top genes"),
      ("failed_wells.csv", "excluded wells"),
      ("replicates.csv", "drug-doses on two plates: correlation of their genome-wide signatures (r) and its "
                         "percentile among random pairs of different drugs"),
      ("calibration_by_gene.csv", "per gene: % of drug wells with |z| > 1.96 and > 3")], deeper_queries(fx.out))


def angle_drugs(fx, folder):
    gi = fx.gi
    up, dn = signif(fx)
    lfc, z = np.asarray(fx.DD_lfc), np.asarray(fx.DD_z)
    qu, qd = np.asarray(fx.DD_qup), np.asarray(fx.DD_qdn)
    dd = fx.dd.copy()
    dd["median_abs_z"] = np.nanmedian(np.abs(z[:, gi]), axis=1)
    labels = fx.label
    tops = []
    for d in range(len(dd)):
        for sign, mask, qq in (("up", up[d, gi], qu), ("down", dn[d, gi], qd)):
            zz = np.where(mask, z[d, gi] * (1 if sign == "up" else -1), -np.inf)
            for i in np.argsort(-zz)[:TOP]:
                if not np.isfinite(zz[i]):
                    break
                c = gi[i]
                tops.append({"drug": dd.at[d, "drug"], "conc": dd.at[d, "conc"], "direction": sign,
                             "gene": labels[c], "fold_change": float(2 ** lfc[d, c]), "z": float(z[d, c]),
                             "q": float(qq[d, c])})
    pd.DataFrame(tops, columns=["drug", "conc", "direction", "gene", "fold_change", "z", "q"]).to_parquet(
        os.path.join(folder, "drug_top_genes.parquet"), index=False)
    best = drug_best_dose(fx)
    Xn = unit_rows(z[:, responsive_genes(fx)])
    B = Xn[best]
    sim = B @ B.T
    bd = dd.loc[best, ["drug", "conc", "moa_fine", "n_sig_genes"]].reset_index(drop=True)
    strong = bd["n_sig_genes"].to_numpy() >= 20
    pos = {d: i for i, d in enumerate(bd["drug"])}
    neigh = []
    for i in range(len(bd)):
        if not strong[i]:
            neigh.append("")
            continue
        o = [j for j in np.argsort(-sim[i]) if j != i and strong[j]][:5]
        neigh.append("; ".join(f"{bd.at[j, 'drug']} {bd.at[j, 'conc']:g} (r {sim[i, j]:.2f}; {bd.at[j, 'moa_fine'] or '-'})"
                               for j in o))
    drows = []
    for drug, gg in dd.groupby("drug"):
        gg = gg.sort_values("conc")
        ii = gg.index.to_numpy()
        nsg = gg["n_sig_genes"].to_numpy()
        act = gg["conc"].to_numpy()[nsg >= 10]
        drows.append({"drug": drug, "moa_fine": gg["moa_fine"].iloc[0], "targets": gg["targets"].iloc[0],
                      "doses": T.fmt_list(gg["conc"].tolist(), "{:g}"),
                      "n_sig_by_dose": " / ".join(str(int(x)) for x in nsg),
                      "max_sig": int(nsg.max()),
                      "lowest_active_dose": float(act.min()) if act.size else np.nan,
                      "signature_r_between_doses": T.fmt_list([float(Xn[a] @ Xn[b]) for a, b in zip(ii[:-1], ii[1:])]),
                      "flags_by_dose": " / ".join(f or "-" for f in gg["flags"]),
                      "cells_x_by_dose": T.fmt_list((2 ** gg["cells_log2_vs_plate"]).tolist()),
                      "most_similar_drugs": neigh[pos[drug]] if drug in pos else ""})
    pd.DataFrame(drows).sort_values("max_sig", ascending=False).to_csv(os.path.join(folder, "drug_summary.csv"),
                                                                       index=False)
    dd.to_csv(os.path.join(folder, "drug_dose_summary.csv"), index=False)
    write_cards(fx, folder, "drug")
    write_brief(folder, TITLES["drugs"], """
For every drug and dose: how much does it change the transcriptome, which genes, and why? Identify the drugs with
the strongest and the most specific (on-target-looking) signatures, the inactive ones, those dominated by toxicity,
transcription shutdown or cell-cycle effects, how signatures grow with dose (potency: lowest active dose), which
drugs look alike (and whether that matches their mechanism or reveals shared off-target effects), and surprises.
Use known pharmacology as a check. The cards/ folder has a one-page card per drug.
""", [("drug_summary.csv", "one row per drug: doses, significant genes per dose, lowest active dose (>= 10 genes), "
                           "signature similarity between doses, flags and cells per dose (x of plate median), most "
                           "similar drugs (cosine of z signatures at their strongest dose, with MoA)"),
      ("drug_dose_summary.csv", "one row per drug and dose: significant genes up/down, median |z|, context, flags, MoA"),
      ("drug_top_genes.parquet", f"per drug and dose: top {TOP} significant genes up and down (fold change, z, q)"),
      ("cards/", "one Markdown card per drug (all doses: context, top genes, depleted lines, response by line)")],
        deeper_queries(fx.out))


def angle_genes(fx, folder):
    gi = fx.gi
    up, dn = signif(fx)
    lfc, z = np.asarray(fx.DD_lfc), np.asarray(fx.DD_z)
    qu, qd = np.asarray(fx.DD_qup), np.asarray(fx.DD_qdn)
    dd = fx.dd
    labels = fx.label
    W2 = np.asarray(fx.W2)[fx.drug_w]

    def corr_with(v, M):
        v = v - v.mean()
        M = M - M.mean(axis=0)
        return (M.T @ v) / (np.linalg.norm(M, axis=0) * np.linalg.norm(v) + 1e-12)

    Wg = np.nan_to_num(W2[:, gi])
    cc_g2m = corr_with(np.nan_to_num(W2[:, fx.mod_col["G2M_PHASE"]]), Wg)
    cc_s = corr_with(np.nan_to_num(W2[:, fx.mod_col["S_PHASE"]]), Wg)
    del Wg
    sm = np.asarray(fx.slot_median)[:, gi]
    worst = np.argmax(np.where(np.isfinite(sm), np.abs(sm), -1), axis=0)
    flags = dd["flags"].to_numpy()
    drugs = dd["drug"].to_numpy()
    concs = dd["conc"].to_numpy()
    gcols = fx.genes.set_index("col")
    rows, tops = [], []
    for k, c in enumerate(gi):
        zc = z[:, c]
        rec = {"gene": labels[c], "pooled_cpm": gcols.at[c, "pooled_cpm"],
               "median_line_cpm": gcols.at[c, "median_line_cpm"], "n_lines_expressing": gcols.at[c, "n_lines_expressing"],
               "n_drugdoses_up": int(up[:, c].sum()), "n_drugdoses_down": int(dn[:, c].sum()),
               "corr_with_G2M": cc_g2m[k], "corr_with_S": cc_s[k],
               "worst_position": T.well_name(worst[k] + 1), "worst_position_shift_log2": sm[worst[k], k]}
        for sign, name, qq in ((1, "up", qu), (-1, "down", qd)):
            zz = np.where(np.isfinite(zc), zc * sign, -np.inf)
            o = np.argsort(-zz)[:10]
            b = o[0]
            rec[f"best_{name}_drug"] = drugs[b]
            rec[f"best_{name}_conc"] = concs[b]
            rec[f"best_{name}_fold"] = 2 ** lfc[b, c]
            rec[f"best_{name}_q"] = qq[b, c]
            rec[f"best_{name}_flags"] = flags[b]
            other = [i for i in o[1:] if drugs[i] != drugs[b]]
            rec[f"{name}_specificity_z_gap"] = zz[b] - (zz[other[0]] if other else np.nan)
            for r_, i in enumerate(o):
                tops.append((labels[c], name, r_ + 1, drugs[i], concs[i], float(2 ** lfc[i, c]), float(zc[i]),
                             float(qq[i, c]), flags[i]))
        rows.append(rec)
    gs = pd.DataFrame(rows)
    gs.to_parquet(os.path.join(folder, "gene_summary.parquet"), index=False)
    pd.DataFrame(tops, columns=["gene", "direction", "rank", "drug", "conc", "fold_change", "z", "q", "flags"]) \
        .to_parquet(os.path.join(folder, "gene_top_drugs.parquet"), index=False)
    col_of_label = dict(zip(labels[gi], gi))

    def candidates(direction):
        sign = 1 if direction == "up" else -1
        fold = gs[f"best_{direction}_fold"]
        t = gs[(gs[f"best_{direction}_q"] < 0.05) & ((fold >= 1.5) if sign > 0 else (fold <= 1 / 1.5))
               & (gs[f"best_{direction}_flags"] == "") & (gs["corr_with_G2M"].abs() < 0.5)].copy()
        pats = [fx.dose_pattern(col_of_label[g], d, sign) for g, d in zip(t["gene"], t[f"best_{direction}_drug"])]
        t["dose_pattern"] = [p[0] for p in pats]
        t["z_by_dose"] = [p[1] for p in pats]
        t = t[~t["dose_pattern"].isin(["inconsistent across doses", "none"])]
        return t.sort_values(f"best_{direction}_fold", ascending=(direction == "down"))

    candidates("up").to_csv(os.path.join(folder, "inducible_genes.csv"), index=False)
    candidates("down").to_csv(os.path.join(folder, "repressible_genes.csv"), index=False)
    write_brief(folder, TITLES["genes"], """
Across all genes: which are most drug-responsive, which have specific, dose-consistent inducers or repressors
(the genome-wide version of 'what raises MTAP or Gankyrin'), which gene families or pathways stand out, and which
genes' apparent responses are mostly artifacts (cell-cycle composition, transcription shutdown, well position).
Give the most actionable gene-drug pairs with their caveats.
""", [("gene_summary.parquet", "one row per gene: level, significant drug-doses up/down, best inducer and repressor "
                               "(fold change, q, flags), specificity (z gap to the next drug), correlation of its "
                               "responses with the G2M and S modules, worst well-position shift"),
      ("gene_top_drugs.parquet", "per gene: top 10 drug-doses up and down"),
      ("inducible_genes.csv", "genes with a clean inducer: >= 1.5x, q < 0.05, no flags, dose-consistent, not "
                              "cell-cycle driven (with the dose pattern)"),
      ("repressible_genes.csv", "the same for decreases (<= 0.67x)")], deeper_queries(fx.out))


def angle_classes(fx, folder):
    z = np.asarray(fx.DD_z)
    dd = fx.dd
    best = drug_best_dose(fx)
    resp = responsive_genes(fx)
    B = np.nan_to_num(z[best][:, resp])
    Bn = unit_rows(B)
    S_all = Bn @ Bn.T
    bd = dd.loc[best].reset_index(drop=True)
    rng = np.random.default_rng(1)
    labels = fx.label[resp]
    nb = len(bd)

    def groups_by(col, split=False):
        out = defaultdict(list)
        for i, v in enumerate(bd[col].astype(str)):
            items = [x.strip() for x in v.split(",")] if split else [v.strip()]
            for it in items:
                if it and it.lower() not in ("unclear", "unknown", "nan", "none", "n/a", "na", "x", "-", "[]"):
                    out[it].append(i)
        return {k: sorted(set(v)) for k, v in out.items() if len(set(v)) >= 3}

    rows, tops = [], []
    for kind, col, split in (("mechanism", "moa_fine", False), ("target", "targets", True)):
        for name, members in sorted(groups_by(col, split).items()):
            n = len(members)
            if n > nb - 2:
                continue
            within = (S_all[np.ix_(members, members)].sum() - n) / (n * (n - 1))
            nulls = []
            for _ in range(500):
                r = rng.choice(nb, n, replace=False)
                nulls.append((S_all[np.ix_(r, r)].sum() - n) / (n * (n - 1)))
            nulls = np.array(nulls)
            cent = B[members].mean(axis=0)
            cu = cent / (np.linalg.norm(cent) or 1)
            corr_each = [float(Bn[m] @ cu) for m in members]
            rows.append({"kind": kind, "group": name, "n_drugs": n,
                         "drugs": "; ".join(f"{bd.at[m, 'drug']} {bd.at[m, 'conc']:g}" for m in members),
                         "consistency_r": within, "random_r": float(nulls.mean()),
                         "consistency_z": (within - nulls.mean()) / (nulls.std() or 1),
                         "pct_random_sets_below": 100 * float((nulls < within).mean()),
                         "fit_of_each_drug": "; ".join(f"{bd.at[m, 'drug']} {c:.2f}" for m, c in zip(members, corr_each)),
                         "outlier_drug": bd.at[members[int(np.argmin(corr_each))], "drug"],
                         "top_up": top_list(labels, cent * n ** 0.5, 12),
                         "top_down": top_list(labels, cent * n ** 0.5, 12, reverse=False)})
            for i in np.argsort(-np.abs(cent))[:50]:
                tops.append({"kind": kind, "group": name, "gene": labels[i], "mean_z": float(cent[i])})
    cols = ["kind", "group", "n_drugs", "drugs", "consistency_r", "random_r", "consistency_z", "pct_random_sets_below",
            "fit_of_each_drug", "outlier_drug", "top_up", "top_down"]
    pd.DataFrame(rows, columns=cols).sort_values("consistency_z", ascending=False).to_csv(
        os.path.join(folder, "class_summary.csv"), index=False)
    pd.DataFrame(tops, columns=["kind", "group", "gene", "mean_z"]).to_parquet(
        os.path.join(folder, "class_top_genes.parquet"), index=False)
    # does each drug move the mRNA of its own target(s)?
    lfc, qu, qd = np.asarray(fx.DD_lfc), np.asarray(fx.DD_qup), np.asarray(fx.DD_qdn)
    trows = []
    for i, r in dd.iterrows():
        for tg in [x.strip() for x in str(r["targets"]).split(",") if x.strip()]:
            c = fx.col_of(tg)
            if c is None or not fx.gmask[c]:
                continue
            trows.append({"drug": r["drug"], "conc": r["conc"], "target": tg, "fold_change": float(2 ** lfc[i, c]),
                          "z": float(z[i, c]), "q_up": float(qu[i, c]), "q_down": float(qd[i, c]), "flags": r["flags"]})
    tm = pd.DataFrame(trows, columns=["drug", "conc", "target", "fold_change", "z", "q_up", "q_down", "flags"])
    tm.sort_values("z", key=np.abs, ascending=False).to_csv(os.path.join(folder, "target_mrna_response.csv"), index=False)
    write_brief(folder, TITLES["classes"], """
Do drugs that share a mechanism or a target produce a shared transcriptional signature? Which classes are coherent
(likely on-target biology) and which are not; what genes define each coherent class; which drugs are outliers in
their class (possible off-target effects, a dose too low, or a mislabelled mechanism). Do drugs move the mRNA of
their own targets (feedback, e.g. statins raising HMGCR)? Use known pharmacology to judge.
""", [("class_summary.csv", "one row per mechanism (moa_fine) or shared target with >= 3 drugs: drugs (strongest "
                            "dose), signature consistency vs 500 random drug sets (r, z, percentile), fit of each "
                            "drug to the class centre, outlier drug, top shared genes up/down (mean z x sqrt(n))"),
      ("class_top_genes.parquet", "per class: 50 genes with the largest mean z"),
      ("target_mrna_response.csv", "every drug-dose x annotated target gene: fold change, z, q up/down, flags")],
        deeper_queries(fx.out))


def genotype_features(fx):
    """Groups of cell lines: driver genes, specific protein changes, organs, MTAP loss by expression."""
    lines = fx.lines
    ok = lines["in_growth_analysis"].astype(bool).to_numpy()
    feats = defaultdict(set)
    for i, d in enumerate(lines["drivers"]):
        for item in [x.strip() for x in d.split(";") if x.strip()]:
            feats[f"{item.split('(')[0].strip()} altered"].add(i)
    for i, d in enumerate(lines["driver_changes"]):
        for item in [x.strip() for x in d.split(";") if x.strip()]:
            gene, _, ch = item.partition(" ")
            feats[f"{gene} {ch}"].add(i)
            m = re.match(r"p\.([A-Z][a-z]{0,2}\d+)", ch)
            if m and m.group(0) != ch:
                feats[f"{gene} {m.group(0)} (any change)"].add(i)
    for i, o in enumerate(lines["Organ"]):
        if o:
            feats[f"organ: {o}"].add(i)
    mc = fx.col_of("MTAP")
    if mc is not None:
        lc = np.asarray(fx.line_cpm)[:, mc]
        ratio = pd.Series(lc / np.median(lc))
        thr, _ = T.null_threshold(ratio[lines["n_cells_total"] >= T.MIN_LINE_CELLS])
        feats["MTAP not expressed"] = set(np.flatnonzero(ratio.values < thr).tolist())
    by_set = {}                       # identical line sets (e.g. CDKN2A altered = MTAP not expressed) -> one feature
    for k, v in feats.items():
        v = tuple(sorted(i for i in v if ok[i]))
        if 3 <= len(v) <= ok.sum() - 3:
            by_set.setdefault(v, []).append(k)
    return {" = ".join(names[:3]) + (f" (+{len(names) - 3})" if len(names) > 3 else ""): list(v)
            for v, names in by_set.items()}


def expression_loss_features(fx, max_lost=15, min_gap=0.8):
    """Genes that most lines express but some lines have lost (deletion/silencing), grouped by the set of lines.
    Lost lines often still read 10-25% of the median line (ambient RNA from the other lines in the well), so the
    call is a clear gap (>= 2^min_gap fold) between 3-15 low lines (<= LOSS_MAX of the median) and the rest."""
    lc = np.asarray(fx.line_cpm)
    ok = fx.lines["in_growth_analysis"].astype(bool).to_numpy() & \
        (fx.lines["n_cells_total"].to_numpy() >= T.MIN_LINE_CELLS)
    gi = fx.gi
    idx_ok = np.flatnonzero(ok)
    med = np.median(lc[ok][:, gi], axis=0)
    ratio = lc[:, gi] / np.where(med > 0, med, np.nan)
    present = (ratio[ok] >= LOSS_PRESENT).mean(axis=0)
    cand = np.flatnonzero((med >= LOSS_MIN_CPM) & (present >= 0.7))
    groups = defaultdict(list)
    max_lost = min(max_lost, idx_ok.size - 4)        # keep >= 4 lines above the cut (fewer lines: smaller groups)
    if cand.size and max_lost >= 3:
        S = np.sort(np.log2(np.maximum(ratio[ok][:, cand], 1e-4)), axis=0)       # ascending, per gene
        lower = S[2:max_lost]                         # value of the k-th lowest line, k = 3..max_lost
        gaps = np.where(lower <= math.log2(LOSS_MAX), S[3:max_lost + 1] - lower, -np.inf)
        k_best = np.argmax(gaps, axis=0)
        g_best = gaps[k_best, np.arange(cand.size)]
        for j in np.flatnonzero(g_best >= min_gap):
            cut = S[k_best[j] + 2, j] + g_best[j] / 2
            members = idx_ok[np.log2(np.maximum(ratio[ok][:, cand[j]], 1e-4)) < cut]
            groups[tuple(members)].append(cand[j])
    out = {}
    for members, ks in sorted(groups.items(), key=lambda t: -len(t[1])):
        ks = sorted(ks, key=lambda k: -med[k])
        names = [fx.label[gi[k]] for k in ks]
        nm = "loss: " + ", ".join(names[:6]) + (f" +{len(names) - 6} more" if len(names) > 6 else "")
        out[nm] = {"members": list(members), "genes": names}
    return out


def group_contrast(fx, members, use_lines):
    """Within-well comparison of a group of lines vs the rest: per drug-dose extra depletion, z, q."""
    A2, VA = np.asarray(fx.A2), np.asarray(fx.VA)
    w = fx.wells
    alt = np.zeros(A2.shape[1], bool)
    alt[members] = True
    alt &= use_lines
    rest = use_lines & ~alt
    k, m = alt.sum(), rest.sum()
    delta = np.nanmean(A2[:, alt], axis=1) - np.nanmedian(A2[:, rest], axis=1)
    var = np.nansum(VA[:, alt], axis=1) / k ** 2 + (math.pi / 2) * np.nansum(VA[:, rest], axis=1) / m ** 2
    eff, _ = loo_matrix(delta[:, None], w["slot"].to_numpy(dtype=float), w["drug"].to_numpy(dtype=object), fx.drug_w)
    d2 = delta - eff[:, 0]
    dw = fx.drug_w
    c = np.nanmedian(d2[dw])
    s = 1.4826 * np.nanmedian(np.abs(d2[dw] - c))
    wv = max(s ** 2 - np.nanmedian(var[dw]), (0.25 * s) ** 2)
    zz = (d2 - c) / np.sqrt(wv + var)
    below = (A2[:, alt] < np.nanmedian(A2[:, rest], axis=1)[:, None]).sum(axis=1)
    t = pd.DataFrame({"drug": w["drug"], "dose": w["dose"], "conc": w["conc"], "delta": d2 - c, "z": zz,
                      "below": below})[dw]
    g = t.groupby(["drug", "dose"])
    res = g.agg(conc=("conc", "first"), extra_log2_depletion=("delta", "mean"),
                group_lines_below_rest_median=("below", "mean"))
    res["z"] = g["z"].sum() / np.sqrt(g["z"].count())
    res["p"] = norm_sf(-res["z"].to_numpy())
    res["q"] = T.bh(res["p"].to_numpy())
    res["n_group_lines"] = int(k)
    return res.reset_index()


def angle_cell_lines(fx, folder):
    lines = fx.lines
    DA, DAz, DB = np.asarray(fx.DD_A), np.asarray(fx.DD_Az), np.asarray(fx.DD_beta)
    dd = fx.dd
    use = lines["in_growth_analysis"].astype(bool).to_numpy()
    lc = np.asarray(fx.line_cpm)
    gi = fx.gi
    labels = fx.label
    hi = (dd["conc"] == dd["conc"].max()).to_numpy()
    strong = (np.nanmedian(DB, axis=1) >= 0.8) & (dd["n_sig_genes"].to_numpy() >= 50)
    rows, longrows = [], []
    for i, r in lines.iterrows():
        other = np.delete(np.arange(len(lines)), i)
        ratio = np.log2((lc[i, gi] + 1) / (np.median(lc[other][:, gi], axis=0) + 1))
        az = DAz[:, i]
        sel = [j for j in np.argsort(np.nan_to_num(az, nan=99))[:10] if np.isfinite(az[j])]
        rows.append({"cell_line_id": r["cell_line_id"], "name": fx.line_name[i], "organ": r["Organ"],
                     "drivers": r["drivers"], "protein_changes": r["driver_changes"],
                     "n_cells_total": r["n_cells_total"], "in_growth_analysis": use[i],
                     "G2M_level_cpm": lc[i, fx.mod_col["G2M_PHASE"]],
                     "median_growth_log2_top_dose": float(np.nanmedian(DA[hi, i])) if use[i] else np.nan,
                     "median_response_beta": float(np.nanmedian(DB[strong, i])) if strong.any() else np.nan,
                     "most_selective_drugs": "; ".join(f"{dd.at[j, 'drug']} {dd.at[j, 'conc']:g} ({2 ** DA[j, i]:.2f}x, "
                                                       f"z {az[j]:.1f})" for j in sel) if use[i] else "",
                     "specific_genes_log2_vs_other_lines": top_list(labels[gi], ratio, 15)})
        if use[i]:
            longrows.append(pd.DataFrame({"cell_line_id": r["cell_line_id"], "name": fx.line_name[i],
                                          "drug": dd["drug"], "conc": dd["conc"], "growth_log2": DA[:, i],
                                          "z": DAz[:, i]}))
    pd.DataFrame(rows).to_csv(os.path.join(folder, "line_summary.csv"), index=False)
    ld = pd.concat(longrows, ignore_index=True)
    ld["q_within_line"] = ld.groupby("cell_line_id")["z"].transform(lambda s: T.bh(norm_sf(-s.to_numpy())))
    ld.to_parquet(os.path.join(folder, "line_drug_growth.parquet"), index=False)
    meta = dd.drop_duplicates("drug").set_index("drug")[["moa_fine", "targets"]]
    feats = genotype_features(fx)
    res = []
    for name, members in feats.items():
        r = group_contrast(fx, members, use)
        r.insert(0, "lines", ", ".join(fx.line_name[m] for m in members))
        r.insert(0, "feature", name)
        res.append(r)
    if res:
        ga = pd.concat(res, ignore_index=True).join(meta, on="drug")
        ga.sort_values("z").to_csv(os.path.join(folder, "genotype_selective_drugs.csv"), index=False)
    loss = expression_loss_features(fx)
    lrows, allres = [], []
    for name, info in loss.items():
        lrows.append({"group": name, "n_lines": len(info["members"]),
                      "lines": ", ".join(fx.line_name[m] for m in info["members"]), "n_genes": len(info["genes"]),
                      "genes": ", ".join(info["genes"])})
        r = group_contrast(fx, info["members"], use)
        r.insert(0, "lines", ", ".join(fx.line_name[m] for m in info["members"]))
        r.insert(0, "group", name)
        r["rank_in_group"] = r["z"].rank()
        allres.append(r)
    pd.DataFrame(lrows, columns=["group", "n_lines", "lines", "n_genes", "genes"]).to_csv(
        os.path.join(folder, "expression_loss_groups.csv"), index=False)
    if allres:
        el = pd.concat(allres, ignore_index=True)
        el["q_all_groups"] = T.bh(el["p"].to_numpy())
        el = el[(el["q"] < 0.25) | (el["rank_in_group"] <= 5)].drop(columns="rank_in_group").join(meta, on="drug")
        el.sort_values("z").to_csv(os.path.join(folder, "expression_loss_selective_drugs.csv"), index=False)
    write_cards(fx, folder, "line")
    files = [("genotype_selective_drugs.csv", "per feature (driver gene, specific protein change, organ, MTAP not "
                                              "expressed) and drug-dose: extra log2 depletion of the group's lines vs "
                                              "the other lines in the same wells, z, q (within feature), mean number "
                                              "of group lines below the rest's median"),
             ("expression_loss_groups.csv", "genes that >= 70% of lines express but 3-15 lines have lost (a clear "
                                            ">= 1.7-fold gap, lost lines <= 30% of the median line; they can still "
                                            "read 10-25% from ambient RNA of the other lines), grouped by the set of "
                                            "lines that lost them; groups of co-deleted neighbours share one row"),
             ("expression_loss_selective_drugs.csv", "the MTAP-null screen for every loss group: drug-doses that "
                                                     "deplete the lines lacking those genes (q < 0.25, or the top 5 "
                                                     "per group)"),
             ("line_summary.csv", "per line: organ, drivers, protein changes, cells, proliferation (G2M level), "
                                  "typical growth at the top dose, typical transcriptional response, most selective "
                                  "drugs, genes most specific to the line"),
             ("line_drug_growth.parquet", "per line and drug-dose: log2 relative abundance, z, q within line"),
             ("cards/", "one Markdown card per cell line")]
    write_brief(folder, TITLES["cell_lines"], """
Which drugs selectively deplete particular cell lines, and do mutations, lineage or gene loss explain it? Check the
known cases first (BRAF-mutant lines vs BRAF/MEK inhibitors, KRAS G12C lines vs G12C inhibitors, EGFR-altered lines
vs EGFR inhibitors, MTAP-null lines vs antifolates such as pemetrexed): if they come out, the method works and the
new hits deserve attention. Then report the strongest new genotype-, lineage- and gene-loss-selective drugs, and
line-specific vulnerabilities, each with how many of the group's lines actually follow
(group_lines_below_rest_median). Watch for groups that are really one lineage in disguise.
""", files, deeper_queries(fx.out))


def rank_rows(M):
    """Rank each row across its columns (NaN -> mean rank), centred; for Spearman by dot products."""
    R = pd.DataFrame(np.asarray(M, dtype=np.float64)).rank(axis=1).to_numpy()
    R = R - np.nanmean(R, axis=1, keepdims=True)
    return np.where(np.isfinite(R), R, 0.0)


def unit(R):
    n = np.linalg.norm(R, axis=1, keepdims=True)
    return R / np.where(n > 0, n, 1.0)


def angle_biomarkers(fx, folder):
    """Does a line's baseline level of a gene predict how a drug-dose affects its growth? Every gene x drug-dose,
    raw and within lineage (organ effects removed from both sides)."""
    lines = fx.lines
    use = lines["in_growth_analysis"].astype(bool).to_numpy() & (lines["n_cells_total"].to_numpy() >= T.MIN_LINE_CELLS)
    n = int(use.sum())
    gi = fx.gi
    X = np.log2(np.asarray(fx.line_cpm)[use][:, gi] + 1.0).T              # genes x lines
    keep = X.std(axis=1) >= 0.3                                            # genes whose level varies between lines
    gcols, X = gi[keep], X[keep]
    labels = fx.label[gcols]
    DA, DAz = np.asarray(fx.DD_A)[:, use], np.asarray(fx.DD_Az)[:, use]
    dd = fx.dd
    hit = (np.abs(np.nan_to_num(DA)) >= 0.5) & (np.abs(np.nan_to_num(DAz)) >= 1.5)   # >= 1.4x and z >= 1.5
    elig = np.flatnonzero((hit.sum(axis=1) >= 3) & (np.isfinite(DA).sum(axis=1) >= 0.8 * n))
    organs = lines.loc[use, "Organ"].to_numpy()
    big = [o for o in pd.unique(organs) if o and (organs == o).sum() >= 3]
    Dm = np.column_stack([np.ones(n)] + [(organs == o).astype(float) for o in big])
    H = Dm @ np.linalg.pinv(Dm)                                            # projection onto organ means
    k_org = int(np.linalg.matrix_rank(Dm)) - 1
    Rx = rank_rows(X)
    Ra = rank_rows(DA[elig]) if elig.size else np.zeros((0, n))
    rho = unit(Ra) @ unit(Rx).T                                            # drug-doses x genes, Spearman
    rho_w = unit(Ra - Ra @ H) @ unit(Rx - Rx @ H).T                        # within lineage
    z = np.arctanh(np.clip(rho, -0.999, 0.999)) * math.sqrt(max(n - 3, 1))
    zw = np.arctanh(np.clip(rho_w, -0.999, 0.999)) * math.sqrt(max(n - 3 - k_org, 1))
    q = bh_columns((2 * norm_sf(np.abs(z))).T).T if elig.size else z          # BH over genes, per drug-dose
    qw = bh_columns((2 * norm_sf(np.abs(zw))).T).T if elig.size else zw
    lin_r2 = (np.linalg.norm(unit(Ra) @ H, axis=1) ** 2) if elig.size else np.zeros(0)  # growth pattern explained by organ
    top, hits, sel = [], [], []
    for j, i in enumerate(elig):
        nsel = int(hit[i].sum())
        o = np.argsort(-np.abs(rho[j]))[:10]
        ow = np.argsort(-np.abs(rho_w[j]))[:5]
        sel.append({"drug": dd.at[i, "drug"], "conc": dd.at[i, "conc"], "moa_fine": dd.at[i, "moa_fine"],
                    "lines_strongly_affected": nsel, "growth_pattern_explained_by_organ_pct": 100 * lin_r2[j],
                    "best_marker": f"{labels[o[0]]} (rho {rho[j, o[0]]:+.2f}, q {q[j, o[0]]:.1g})",
                    "best_marker_within_lineage": f"{labels[ow[0]]} (rho {rho_w[j, ow[0]]:+.2f}, q {qw[j, ow[0]]:.1g})",
                    "n_genes_q_below_0.1": int((q[j] < 0.1).sum()),
                    "n_genes_q_below_0.1_within_lineage": int((qw[j] < 0.1).sum())})
        for r_, g in enumerate(o):
            top.append({"drug": dd.at[i, "drug"], "conc": dd.at[i, "conc"], "rank": r_ + 1, "gene": labels[g],
                        "rho": rho[j, g], "q": q[j, g], "rho_within_lineage": rho_w[j, g], "q_within_lineage": qw[j, g],
                        "direction": "high level -> more depleted" if rho[j, g] < 0 else "high level -> spared"})
        m = np.flatnonzero((q[j] < 0.1) | (qw[j] < 0.1))
        m = m[np.argsort(-np.abs(rho[j, m]))][:200]
        for g in m:
            hits.append((dd.at[i, "drug"], dd.at[i, "conc"], labels[g], float(rho[j, g]), float(q[j, g]),
                         float(rho_w[j, g]), float(qw[j, g])))
    cols = ["drug", "conc", "moa_fine", "lines_strongly_affected", "growth_pattern_explained_by_organ_pct", "best_marker",
            "best_marker_within_lineage", "n_genes_q_below_0.1", "n_genes_q_below_0.1_within_lineage"]
    pd.DataFrame(sel, columns=cols).sort_values("n_genes_q_below_0.1_within_lineage", ascending=False).to_csv(
        os.path.join(folder, "selective_drugs.csv"), index=False)
    pd.DataFrame(top, columns=["drug", "conc", "rank", "gene", "rho", "q", "rho_within_lineage", "q_within_lineage",
                               "direction"]).to_csv(os.path.join(folder, "biomarker_top10.csv"), index=False)
    pd.DataFrame(hits, columns=["drug", "conc", "gene", "rho", "q", "rho_within_lineage", "q_within_lineage"]) \
        .to_parquet(os.path.join(folder, "biomarker_hits.parquet"), index=False)
    # genes that predict response to many drugs (e.g. drug efflux pumps, proliferation)
    if elig.size:
        sig, sigw = (q < 0.1), (qw < 0.1)
        gm = pd.DataFrame({"gene": labels, "n_drug_doses_q_below_0.1": sig.sum(axis=0),
                           "n_within_lineage": sigw.sum(axis=0),
                           "pct_high_level_more_depleted": 100 * (sig & (rho < 0)).sum(axis=0) / np.maximum(sig.sum(axis=0), 1),
                           "sd_log2_across_lines": X.std(axis=1)})
        gm["top_drugs"] = ["; ".join(f"{dd.at[elig[j], 'drug']} {dd.at[elig[j], 'conc']:g} ({rho[j, g]:+.2f})"
                                     for j in np.argsort(-np.abs(rho[:, g]))[:5]) for g in range(len(labels))]
        gm.sort_values("n_within_lineage", ascending=False).head(2000).to_csv(
            os.path.join(folder, "marker_genes.csv"), index=False)
    # targets: does the level of a drug's own target predict who it kills?
    trows = []
    lab_pos = {lb: g for g, lb in enumerate(labels)}
    for j, i in enumerate(elig):
        for tg in [x.strip() for x in str(dd.at[i, "targets"]).split(",") if x.strip()]:
            g = lab_pos.get(tg)
            if g is not None:
                trows.append({"drug": dd.at[i, "drug"], "conc": dd.at[i, "conc"], "target": tg, "rho": rho[j, g],
                              "q": q[j, g], "rho_within_lineage": rho_w[j, g], "q_within_lineage": qw[j, g]})
    pd.DataFrame(trows, columns=["drug", "conc", "target", "rho", "q", "rho_within_lineage", "q_within_lineage"]) \
        .sort_values("rho").to_csv(os.path.join(folder, "target_level_vs_sensitivity.csv"), index=False)
    write_brief(folder, TITLES["biomarkers"], f"""
For every drug-dose that kills some cell lines more than others ({elig.size} drug-doses with >= 3 lines changed >= 1.4x
at z >= 1.5; lines compared within the
same wells), which genes' baseline expression predicts who dies or who is spared: the genome-wide version of
'does Gankyrin level predict response'. Lineage confounds this (lineage marker genes predict lineage-selective
drugs), so judge markers by rho_within_lineage (organ effects removed) and say when a drug's pattern is mostly
lineage (growth_pattern_explained_by_organ_pct). Check known biology first: ABCB1 (MDR1) or ABCG2 high lines
spared by their substrates (taxanes, anthracyclines, vinca alkaloids, some kinase inhibitors); a targeted drug's
own target predicting sensitivity (ERBB2 for HER2 inhibitors, EGFR for EGFR inhibitors, ESR1 for anti-estrogens);
proliferation genes predicting sensitivity to antimitotics. Then report the strongest new, lineage-independent
markers, and genes that predict response to many drugs. With ~{n} lines, |rho| below ~0.5 is rarely significant.
Correlation is weak for genes lost in only a few lines (deletions such as MTAP/CDKN2A): those are tested far more
sensitively by the expression-loss screen in ../cell_lines/expression_loss_selective_drugs.csv; cross-check there.
Note: here every usable line is included for every gene, also lines that do not express it (the 'left out for that
gene' rule below applies only to drug effects on expression, not to these baseline levels).
""", [("selective_drugs.csv", "per drug-dose with >= 3 lines strongly affected (>= 1.4x, z >= 1.5): how much of its pattern "
                              "organ explains, best marker raw and within lineage, number of genes with q < 0.1"),
      ("biomarker_top10.csv", "per drug-dose: the 10 genes whose baseline level best predicts growth (Spearman rho "
                              "across lines; negative = high-level lines depleted more), with within-lineage rho and q"),
      ("biomarker_hits.parquet", "all gene x drug-dose pairs with q < 0.1 (raw or within lineage; top 200 per drug-dose)"),
      ("marker_genes.csv", "per gene: how many drug-doses it predicts (raw / within lineage), direction, top drugs"),
      ("target_level_vs_sensitivity.csv", "every drug-dose x its annotated target: does target expression predict "
                                          "who is killed")], deeper_queries(fx.out))


def angle_line_response(fx, folder):
    DB, DR, DA = np.asarray(fx.DD_beta), np.asarray(fx.DD_rcor), np.asarray(fx.DD_A)
    dd = fx.dd
    names = fx.line_name
    L = len(fx.lines)
    nsig = dd["n_sig_genes"].to_numpy()
    nmeas = np.isfinite(DB).sum(axis=1)
    elig = np.flatnonzero((nsig >= MIN_SIG_BETA) & (nmeas >= 10))
    rows, longrows = [], []
    for i in elig:
        b = DB[i]
        ok = np.isfinite(b)
        q25, med, q75 = np.nanpercentile(b, [25, 50, 75])
        o = [x for x in np.argsort(np.where(ok, b, np.inf)) if ok[x]]
        rows.append({"drug": dd.at[i, "drug"], "conc": dd.at[i, "conc"], "moa_fine": dd.at[i, "moa_fine"],
                     "n_sig_genes": int(nsig[i]), "lines_measured": int(ok.sum()), "median_beta": med,
                     "iqr_beta": q75 - q25, "median_r": float(np.nanmedian(DR[i])),
                     "n_lines_beta_below_0.3": int((b[ok] < 0.3).sum()),
                     "weakest_lines": "; ".join(f"{names[x]} {b[x]:.2f}" for x in o[:5]),
                     "strongest_lines": "; ".join(f"{names[x]} {b[x]:.2f}" for x in o[::-1][:3]),
                     "spearman_response_vs_growth": spearman(b, DA[i]), "flags": dd.at[i, "flags"]})
        longrows.append(pd.DataFrame({"drug": dd.at[i, "drug"], "conc": dd.at[i, "conc"], "line": names,
                                      "beta": b, "r": DR[i], "growth_log2": DA[i]}))
    cols = ["drug", "conc", "moa_fine", "n_sig_genes", "lines_measured", "median_beta", "iqr_beta", "median_r",
            "n_lines_beta_below_0.3", "weakest_lines", "strongest_lines", "spearman_response_vs_growth", "flags"]
    per = pd.DataFrame(rows, columns=cols)
    per.sort_values("iqr_beta", ascending=False).to_csv(os.path.join(folder, "drug_response_heterogeneity.csv"),
                                                        index=False)
    if longrows:
        pd.concat(longrows, ignore_index=True).to_parquet(os.path.join(folder, "line_response_matrix.parquet"),
                                                          index=False)
    # genotype / lineage associations (Welch t on beta, per feature and drug-dose)
    feats = genotype_features(fx)
    feats.update({k: v["members"] for k, v in expression_loss_features(fx).items()})
    Bm = DB[elig]
    arows = []
    for fname, memb in feats.items():
        m = np.zeros(L, bool)
        m[memb] = True
        a, r = np.where(m[None, :], Bm, np.nan), np.where(~m[None, :], Bm, np.nan)
        na, nr = np.isfinite(a).sum(1), np.isfinite(r).sum(1)
        ma, mr = np.nanmean(a, 1), np.nanmean(r, 1)
        va, vr = np.nanvar(a, 1, ddof=1), np.nanvar(r, 1, ddof=1)
        se2 = va / np.maximum(na, 1) + vr / np.maximum(nr, 1)
        t = (ma - mr) / np.sqrt(np.where(se2 > 0, se2, np.nan))
        df = se2 ** 2 / ((va / np.maximum(na, 1)) ** 2 / np.maximum(na - 1, 1) +
                         (vr / np.maximum(nr, 1)) ** 2 / np.maximum(nr - 1, 1))
        p = 2 * t_sf(np.abs(t), df)
        p[(na < 3) | (nr < 3)] = np.nan
        q = T.bh(p)
        for j in np.flatnonzero(np.isfinite(p)):
            i = elig[j]
            arows.append((fname, int(m.sum()), dd.at[i, "drug"], dd.at[i, "conc"], dd.at[i, "moa_fine"],
                          float(ma[j]), float(mr[j]), float(ma[j] - mr[j]), float(t[j]), float(p[j]), float(q[j])))
    assoc = pd.DataFrame(arows, columns=["feature", "n_group_lines", "drug", "conc", "moa_fine", "group_mean_beta",
                                         "rest_mean_beta", "difference", "t", "p", "q_within_feature"])
    assoc["q_all"] = T.bh(assoc["p"].to_numpy()) if len(assoc) else []
    assoc.sort_values("p").to_parquet(os.path.join(folder, "feature_response_associations.parquet"), index=False)
    assoc.sort_values("p").head(1000).to_csv(os.path.join(folder, "feature_response_top.csv"), index=False)
    # per line and per line x mechanism
    strong = elig[(np.nanmedian(DB[elig], axis=1) >= 0.8) & (nsig[elig] >= 50)] if elig.size else elig
    lrows = []
    for k in range(L):
        b = DB[strong, k]
        ok = np.isfinite(b)
        o = [strong[x] for x in np.argsort(np.where(ok, b, np.inf)) if ok[x]]
        lrows.append({"line": names[k], "organ": fx.lines.at[k, "Organ"], "drivers": fx.lines.at[k, "drivers"],
                      "n_strong_drug_doses": int(ok.sum()), "median_beta": float(np.nanmedian(b)) if ok.any() else np.nan,
                      "weakest_responses": "; ".join(f"{dd.at[x, 'drug']} {dd.at[x, 'conc']:g} ({DB[x, k]:.2f})" for x in o[:6]),
                      "strongest_responses": "; ".join(f"{dd.at[x, 'drug']} {dd.at[x, 'conc']:g} ({DB[x, k]:.2f})"
                                                       for x in o[::-1][:6])})
    pd.DataFrame(lrows).sort_values("median_beta").to_csv(os.path.join(folder, "line_responsiveness.csv"), index=False)
    if elig.size:
        sub = dd.loc[elig, ["drug", "moa_fine"]].copy()
        sub["row"] = elig
        best = sub.assign(n=nsig[elig]).sort_values("n", ascending=False).drop_duplicates("drug")
        mats = {}
        for moa, g in best.groupby("moa_fine"):
            if moa and moa.lower() != "unclear" and len(g) >= 3:
                mats[f"{moa} (n={len(g)})"] = np.nanmean(DB[g["row"].to_numpy()], axis=0)
        if mats:
            pd.DataFrame(mats, index=names).T.round(3).to_csv(os.path.join(folder, "line_by_mechanism_beta.csv"))
    write_brief(folder, TITLES["line_response"], """
Do all 50 cell lines respond to a drug the same way, or only some? For each drug-dose with a clear signature,
'beta' says how strongly each line shows the consensus response (1 = typical, 0 = none). Find the drugs whose
response is uniform vs restricted to a subset of lines, the mutations, lineages or gene losses that predict who
responds (check known cases: EGFR inhibitors in EGFR-driven lines, BRAF/MEK inhibitors in MAPK-driven lines,
lineage-specific receptors), lines that are globally unresponsive (and whether that is low proliferation or few
cells), and whether transcriptional response predicts depletion (spearman_response_vs_growth < 0: responders die).
""", [("drug_response_heterogeneity.csv", "per drug-dose with >= 20 significant genes: median and spread (IQR) of "
                                          "beta across lines, weakest and strongest lines, link to growth"),
      ("line_response_matrix.parquet", "every eligible drug-dose x line: beta, correlation r, growth (log2)"),
      ("feature_response_top.csv", "top 1,000 associations: feature (driver, protein change, organ, gene loss) x "
                                   "drug-dose, group vs rest mean beta, Welch t, p, q (within feature and overall)"),
      ("feature_response_associations.parquet", "all of them"),
      ("line_responsiveness.csv", "per line: typical beta over strong drug-doses, weakest and strongest responses"),
      ("line_by_mechanism_beta.csv", "mean beta per mechanism (>= 3 drugs) x line")], deeper_queries(fx.out))


def per_line_columns(fx, specs):
    """Re-read the pseudobulk for a few columns (each = list of tokens summed) and return per-line corrected
    effects per drug-dose (drug-doses x lines x C)."""
    pb = os.path.join(fx.out, "pseudobulk")
    prof = load_profiles(pb)
    w = fx.wells
    lines = fx.lines["cell_line_id"].astype(str).tolist()
    prof = prof[prof["sample"].isin(w["sample"]) & prof["cell_line_id"].isin(lines)]
    wi = {s: i for i, s in enumerate(w["sample"])}
    li = {s: i for i, s in enumerate(lines)}
    N, L, C = len(w), len(lines), len(specs)
    counts = np.zeros((N, L, C), dtype=np.float32)
    tot = np.zeros((N, L))
    nc = np.zeros((N, L))
    M = None
    for f, g in prof.groupby("file"):
        g = g.sort_values("row")
        arr = np.load(f, mmap_mode="r")
        if M is None:
            M = np.zeros((arr.shape[1], C), dtype=np.float32)
            for j, toks in enumerate(specs.values()):
                M[np.asarray(toks, dtype=int), j] = 1.0
        rows = g["row"].to_numpy()
        for s0 in range(0, len(rows), 2000):          # chunks keep memory small
            sub = np.asarray(arr[rows[s0:s0 + 2000]])
            gg = g.iloc[s0:s0 + 2000]
            np.add.at(counts, (gg["sample"].map(wi).to_numpy(), gg["cell_line_id"].map(li).to_numpy()), sub @ M)
        np.add.at(tot, (g["sample"].map(wi).to_numpy(), g["cell_line_id"].map(li).to_numpy()), g["total_counts"].to_numpy())
        np.add.at(nc, (g["sample"].map(wi).to_numpy(), g["cell_line_id"].map(li).to_numpy()), g["n_cells"].to_numpy())
    Y = log_cpm(counts, tot, nc)
    r1 = np.full_like(Y, np.nan)
    for p in fx.plates:
        rows = np.flatnonzero((w["plate"] == p).to_numpy())
        drug = rows[fx.drug_w[rows]]
        base = np.nanmedian(Y[drug], axis=0)
        r1[rows] = Y[rows] - base[None]
    W1 = np.nanmedian(r1, axis=1)
    eff, _ = loo_matrix(W1, w["slot"].to_numpy(dtype=float), w["drug"].to_numpy(dtype=object), fx.drug_w)
    r2 = r1 - eff[:, None, :]
    dd = fx.dd
    groups = w[fx.drug_w].groupby(["drug", "dose"]).indices
    di = np.flatnonzero(fx.drug_w)
    out = np.full((len(dd), L, C), np.nan, dtype=np.float32)
    for d, r in dd.iterrows():
        key = (r["drug"], r["dose"])
        if key in groups:
            out[d] = np.nanmean(r2[di[groups[key]]], axis=0)
    return out


def angle_programs(fx, folder):
    gi = fx.gi
    dw = fx.drug_w
    Z = np.asarray(fx.Z)[dw][:, gi]
    var = np.nanvar(Z, axis=0)
    resp = responsive_genes(fx)
    sel_mask = np.isin(gi, resp)
    order = np.argsort(-np.where(sel_mask, var, -1))
    n_sel = int(min(max(sel_mask.sum(), 500), 5000, gi.size))
    sel = order[:n_sel]
    X = np.nan_to_num(Z[:, sel]).T.astype(np.float64)          # genes x wells
    X = X - X.mean(axis=1, keepdims=True)
    sd = X.std(axis=1, keepdims=True)
    sd[sd == 0] = 1
    X = X / sd
    U, S, Vt = np.linalg.svd(X, full_matrices=False)
    # remove a top component only if it is broad (hundreds to thousands of genes follow it, e.g. transcription
    # shutdown or growth); a component carried by a few dozen genes is itself a program and must stay
    gnorm = np.maximum(np.linalg.norm(X, axis=1), 1e-9)
    n_follow = (np.abs(U[:, :10] * S[None, :10] / gnorm[:, None]) >= 0.3).sum(axis=0)
    broad = [j for j in range(min(N_PCS, len(S) - 1)) if n_follow[j] >= max(200, 0.05 * X.shape[0])]
    Xr = X - (U[:, broad] * S[broad]) @ Vt[broad] if broad else X
    Xn = Xr / np.maximum(np.linalg.norm(Xr, axis=1, keepdims=True), 1e-9)
    rng = np.random.default_rng(2)
    K_ = min(MODULE_K, max(2, Xn.shape[0] // 20))
    C = Xn[rng.choice(Xn.shape[0], K_, replace=False)].copy()
    for _ in range(50):
        lab = np.argmax(Xn @ C.T, axis=1)
        for j in range(K_):
            m = Xn[lab == j]
            if len(m):
                c = m.mean(axis=0)
                C[j] = c / max(np.linalg.norm(c), 1e-9)
    lab = np.argmax(Xn @ C.T, axis=1)
    labels = fx.label[gi[sel]]
    wells = fx.wells[dw].reset_index(drop=True)
    var_ = S ** 2 / (S ** 2).sum()
    pcs = []
    for j in range(min(10, len(S))):
        ow, og = np.argsort(Vt[j]), np.argsort(U[:, j])
        pcs.append({"pc": j + 1, "variance_pct": 100 * var_[j],
                    "genes_following_r_over_0.3": int(n_follow[j]), "removed_before_programs": j in broad,
                    "wells_low": "; ".join(f"{wells.at[i, 'drug']} {wells.at[i, 'conc']:g} ({wells.at[i, 'plate']})"
                                           for i in ow[:6]),
                    "wells_high": "; ".join(f"{wells.at[i, 'drug']} {wells.at[i, 'conc']:g} ({wells.at[i, 'plate']})"
                                            for i in ow[::-1][:6]),
                    "genes_low": ", ".join(labels[og[:15]]), "genes_high": ", ".join(labels[og[::-1][:15]])})
    pd.DataFrame(pcs).to_csv(os.path.join(folder, "broad_components.csv"), index=False)
    DDz, DDl = np.asarray(fx.DD_z), np.asarray(fx.DD_lfc)
    dd = fx.dd
    specs, mods, members, md = {}, [], [], []
    mid = 0
    for j in range(K_):
        m = np.flatnonzero(lab == j)
        r = Xn[m] @ C[j]
        m, r = m[r >= 0.2], r[r >= 0.2]          # core members only: genes that actually follow the program
        if m.size < MODULE_MIN:
            continue
        mid += 1
        o = np.argsort(-r)
        cols = gi[sel[m]]
        name = f"P{mid:02d}"
        specs[name] = fx.genes.loc[cols, "token"].to_numpy(dtype=int)
        score = robust_z(np.nanmean(DDz[:, cols], axis=1))
        lf = np.nanmean(DDl[:, cols], axis=1)
        mods.append({"program": name, "n_genes": int(m.size), "top_genes": ", ".join(labels[m[o[:25]]]),
                     "top_drugs_up": "; ".join(f"{dd.at[i, 'drug']} {dd.at[i, 'conc']:g} ({2 ** lf[i]:.2f}x, z {score[i]:.1f})"
                                               for i in np.argsort(-score)[:8]),
                     "top_drugs_down": "; ".join(f"{dd.at[i, 'drug']} {dd.at[i, 'conc']:g} ({2 ** lf[i]:.2f}x, z {score[i]:.1f})"
                                                 for i in np.argsort(score)[:8])})
        members.append(pd.DataFrame({"program": name, "gene": labels[m[o]], "r_to_centre": r[o]}))
        md.append(pd.DataFrame({"program": name, "drug": dd["drug"], "conc": dd["conc"], "mean_fold_change": 2 ** lf,
                                "score_z": score, "flags": dd["flags"]}))
    pd.DataFrame(mods, columns=["program", "n_genes", "top_genes", "top_drugs_up", "top_drugs_down"]).to_csv(
        os.path.join(folder, "programs.csv"), index=False)
    pd.concat(members or [pd.DataFrame(columns=["program", "gene", "r_to_centre"])], ignore_index=True).to_csv(
        os.path.join(folder, "program_members.csv"), index=False)
    md = pd.concat(md or [pd.DataFrame(columns=["program", "drug", "conc", "mean_fold_change", "score_z", "flags"])],
                   ignore_index=True)
    md.to_parquet(os.path.join(folder, "program_drug_effects.parquet"), index=False)
    log(f"  {len(specs)} programs; per-line program responses (re-reading the pseudobulk) ...")
    per_dd = per_line_columns(fx, specs) if specs else np.zeros((len(dd), len(fx.lines), 0))
    feats = genotype_features(fx)
    names = list(specs)
    hits = md[md["score_z"].abs() >= 4].sort_values("score_z", key=np.abs, ascending=False).head(400)
    dd_index = {(r.drug, r.conc): i for i, r in dd.iterrows()}
    rows = []
    for h in hits.itertuples():
        i = dd_index.get((h.drug, h.conc))
        v = per_dd[i, :, names.index(h.program)]
        if np.isfinite(v).sum() < 10:
            continue
        sgn = 1 if h.score_z > 0 else -1
        rec = {"program": h.program, "drug": h.drug, "conc": h.conc, "score_z": h.score_z,
               "lines_measured": int(np.isfinite(v).sum()), "median_line_log2": float(np.nanmedian(v)),
               "lines_moving_same_way_over_1.2x": int((v * sgn > LFC_MIN).sum()),
               "most_lines": "; ".join(f"{fx.line_name[x]} {v[x]:+.2f}" for x in np.argsort(-np.nan_to_num(v * sgn, nan=-9))[:4]),
               "least_lines": "; ".join(f"{fx.line_name[x]} {v[x]:+.2f}" for x in np.argsort(np.nan_to_num(v * sgn, nan=9))[:4])}
        best = None
        for fname, memb in feats.items():
            a = v[memb]
            rest = np.delete(v, memb)
            a, rest = a[np.isfinite(a)], rest[np.isfinite(rest)]
            if len(a) >= 3 and len(rest) >= 3:
                sdp = np.sqrt((a.var(ddof=1) + rest.var(ddof=1)) / 2) or 1.0
                dval = (a.mean() - rest.mean()) / sdp
                if best is None or abs(dval) > abs(best[1]):
                    best = (fname, dval, a.mean() - rest.mean())
        if best:
            rec["most_different_group"], rec["group_effect_size_d"], rec["group_difference_log2"] = best
        rows.append(rec)
    pd.DataFrame(rows).to_csv(os.path.join(folder, "program_line_context.csv"), index=False)
    write_brief(folder, TITLES["programs"], """
What are the main gene programs that drugs switch on and off (name each from its genes, e.g. 'ribosome
biogenesis', 'cholesterol synthesis', 'interferon response', 'heat shock', 'unfolded protein response'), which
drugs drive each program up or down, and where a program's response depends on the cell line, lineage or mutation.
Start from the broad components (the biggest axes of drug response) and say what each represents. Flag programs
that are artifacts (shutdown, toxicity, cell-cycle composition, well position).
""", [("broad_components.csv", "the top 10 axes of drug response (variance, genes following each with |r| >= 0.3, "
                               "drug wells and genes at each end); broad ones (>= 200 genes or 5%) among the first 3 "
                               "were removed before programs were found"),
      ("programs.csv", "data-driven gene programs: size, 25 most central genes, drug-doses that raise and lower them "
                       "(mean fold change, score z = robust z of the program's mean z across all drug-doses)"),
      ("program_members.csv", "every member gene with its fit to the program"),
      ("program_drug_effects.parquet", "every program x drug-dose: mean fold change, score z, flags"),
      ("program_line_context.csv", "for the 400 strongest program x drug-dose effects (|score z| >= 4): spread across "
                                   "cell lines, most and least affected lines, the line group (mutation/organ) that "
                                   "differs most (Cohen's d)")], deeper_queries(fx.out))


def angle_cell_state(fx, folder):
    dd = fx.dd.copy()

    def classify(r):
        s, g2 = r["S_PHASE_lfc"], r["G2M_PHASE_lfc"]
        if g2 > 0.4 and g2 >= s:
            return "G2/M build-up"
        if s > 0.4:
            return "S-phase build-up"
        if s < -0.4 and g2 < -0.4:
            return "fewer cycling cells (G1 arrest or quiescence)"
        return ""

    dd["cell_cycle_call"] = [classify(r) for _, r in dd.iterrows()]
    dd["cells_x_of_plate"] = 2 ** dd["cells_log2_vs_plate"]
    cols = ["drug", "conc", "moa_fine", "targets", "S_PHASE_lfc", "S_PHASE_z", "G2M_PHASE_lfc", "G2M_PHASE_z",
            "cells_x_of_plate", "cells_log2_vs_plate", "umi_per_cell_log2_vs_plate", "genes_per_cell_log2_vs_plate",
            "n_sig_genes", "flags", "cell_cycle_call"]
    dd[[c for c in cols if c in dd]].sort_values("G2M_PHASE_z", ascending=False).to_csv(
        os.path.join(folder, "drug_cell_cycle.csv"), index=False)
    lines = fx.lines
    lc = np.asarray(fx.line_cpm)
    use = lines["in_growth_analysis"].astype(bool).to_numpy()
    prolif = lc[:, fx.mod_col["G2M_PHASE"]]
    DA = np.asarray(fx.DD_A)
    pr = fx.dd[["drug", "conc", "moa_fine"]].copy()
    pr["spearman_growth_vs_proliferation"] = [spearman(DA[i, use], prolif[use]) for i in range(len(dd))]
    n = use.sum()
    pr["z"] = np.arctanh(pr["spearman_growth_vs_proliferation"].clip(-0.999, 0.999)) * math.sqrt(max(n - 3, 1))
    pr["q"] = T.bh(2 * norm_sf(np.abs(pr["z"].to_numpy())))
    pr["cells_x_of_plate"] = 2 ** fx.dd["cells_log2_vs_plate"]
    pr.sort_values("z").to_csv(os.path.join(folder, "proliferation_dependent_drugs.csv"), index=False)
    pd.DataFrame({"cell_line_id": lines["cell_line_id"], "name": fx.line_name, "organ": lines["Organ"],
                  "S_level_cpm": lc[:, fx.mod_col["S_PHASE"]], "G2M_level_cpm": prolif}) \
        .sort_values("G2M_level_cpm", ascending=False).to_csv(os.path.join(folder, "line_proliferation.csv"), index=False)
    gi = fx.gi
    W2 = np.nan_to_num(np.asarray(fx.W2)[fx.drug_w])
    Xg = W2[:, gi] - W2[:, gi].mean(axis=0)
    out = pd.DataFrame({"gene": fx.label[gi]})
    for mod in ("G2M_PHASE", "S_PHASE"):
        v = W2[:, fx.mod_col[mod]]
        v = v - v.mean()
        out[f"corr_with_{mod}"] = (Xg.T @ v) / (np.linalg.norm(Xg, axis=0) * np.linalg.norm(v) + 1e-12)
    out.sort_values("corr_with_G2M_PHASE", ascending=False).to_csv(os.path.join(folder, "cell_cycle_genes.csv"),
                                                                   index=False)
    write_brief(folder, TITLES["cell_state"], """
Which drugs shift the cell cycle (S-phase or G2/M build-up, fewer cycling cells), which kill cells overall
(cells_x_of_plate) and which kill fast-growing lines more (proliferation-dependent killing), and which genes' drug
responses mostly reflect cell-cycle composition (so 'inductions' of those genes by cycle-arresting drugs should not
be trusted). Use known drugs as a check (taxanes, vinca alkaloids, Aurora/PLK inhibitors -> G2/M; antimetabolites
-> S phase; CDK4/6 inhibitors -> fewer cycling cells; transcription inhibitors -> transcription drop).
""", [("drug_cell_cycle.csv", "per drug-dose: S and G2M module shifts (log2, z), cells (x of plate median), "
                              "transcription (UMIs/genes per cell), significant genes, flags, call"),
      ("proliferation_dependent_drugs.csv", "per drug-dose: Spearman across lines of growth vs proliferation (G2M "
                                            "level), z, q; negative = fast-cycling lines depleted more"),
      ("line_proliferation.csv", "per line: S and G2M module levels"),
      ("cell_cycle_genes.csv", "per gene: correlation of its drug responses with the G2M and S module responses")],
        deeper_queries(fx.out))


def angle_focus(fx, folder, gene, per_line):
    c = fx.col_of(gene)
    if c is None or not fx.gmask[c]:
        with open(os.path.join(folder, "brief.md"), "w", encoding="utf-8") as fh:
            fh.write(f"# {gene}\n\n{gene} is not among the tested genes (too low or not found). "
                     "Write report.md saying so in one line.\n")
        return
    dd = fx.dd.copy()
    dd["fold_change"] = 2 ** np.asarray(fx.DD_lfc)[:, c]
    dd["z"] = np.asarray(fx.DD_z)[:, c]
    dd["q_up"] = np.asarray(fx.DD_qup)[:, c]
    dd["q_down"] = np.asarray(fx.DD_qdn)[:, c]
    if per_line is not None:
        v = per_line
        dd["lines_measured"] = np.isfinite(v).sum(axis=1)
        dd["pct_lines_up"] = 100 * (v > 0).sum(axis=1) / np.maximum(dd["lines_measured"], 1)
    pu = {d: fx.dose_pattern(c, d, 1) for d in fx.rows_of_drug}
    pdn = {d: fx.dose_pattern(c, d, -1) for d in fx.rows_of_drug}
    dd["z_by_dose"] = dd["drug"].map(lambda d: pu[d][1])
    dd["pattern_up"] = dd["drug"].map(lambda d: pu[d][0])
    dd["pattern_down"] = dd["drug"].map(lambda d: pdn[d][0])
    lead = ["drug", "conc", "fold_change", "z", "q_up", "q_down", "z_by_dose", "pattern_up", "pattern_down", "flags"]
    dd = dd[[x for x in lead if x in dd] + [x for x in dd.columns if x not in lead]]
    dd.sort_values("z", ascending=False).to_csv(os.path.join(folder, "drug_effects.csv"), index=False)
    X, U, S, Vt = fx.svd()
    k = int(np.flatnonzero(fx.gi == c)[0])
    res = {}
    for npc in (0, N_PCS, 10):
        npc_ = min(npc, len(S) - 1)
        M = X - (U[:, :npc_] * S[:npc_]) @ Vt[:npc_] if npc_ else X
        res[npc] = (M @ M[k]) / (np.linalg.norm(M, axis=1) * np.linalg.norm(M[k]) + 1e-12)
    co = pd.DataFrame({"gene": fx.label[fx.gi], "r": res[0], f"r_minus_{N_PCS}pcs": res[N_PCS],
                       "r_minus_10pcs": res[10]})
    co = co[co["gene"] != fx.label[c]]
    co["proteasome_gene"] = co["gene"].str.match(T.PROTEASOME_RE.pattern)
    pm = os.path.join(fx.out, "angles", "programs", "program_members.csv")
    pg = os.path.join(fx.out, "angles", "programs", "programs.csv")
    if os.path.exists(pm) and os.path.exists(pg):           # which data-driven program each gene belongs to
        mem = pd.read_csv(pm).drop_duplicates("gene").set_index("gene")["program"]
        tops = pd.read_csv(pg).set_index("program")["top_genes"].astype(str).map(lambda s: ", ".join(s.split(", ")[:6]))
        co["program"] = co["gene"].map(mem)
        co["program_top_genes"] = co["program"].map(tops)
    co.sort_values(f"r_minus_{N_PCS}pcs", ascending=False).to_csv(os.path.join(folder, "coregulated_genes.csv"),
                                                                  index=False)
    lc = np.asarray(fx.line_cpm)[:, c]
    lines = fx.lines
    pd.DataFrame({"cell_line_id": lines["cell_line_id"], "name": fx.line_name, "organ": lines["Organ"],
                  "drivers": lines["drivers"], "cpm": lc, "vs_median_line": lc / np.median(lc),
                  "expressing": np.asarray(fx.expr_mask)[:, c]}).sort_values("cpm").to_csv(
        os.path.join(folder, "baseline_by_line.csv"), index=False)
    use = lines["in_growth_analysis"].astype(bool).to_numpy()
    ratio = lc / np.median(lc)
    thr, gap = T.null_threshold(pd.Series(ratio)[lines["n_cells_total"] >= T.MIN_LINE_CELLS])
    nonexpr = [i for i in np.flatnonzero(ratio < thr) if use[i]]
    rest = ratio[use & (ratio >= thr)]
    clean = len(nonexpr) >= 3 and rest.size >= 3 and ratio[nonexpr].max() < 0.5 * rest.min()
    lsd = os.path.join(folder, "loss_selective_drugs.csv")
    if len(nonexpr) >= 3 and (np.isfinite(gap) or clean):
        r = group_contrast(fx, nonexpr, use)
        r.insert(0, "lines", ", ".join(fx.line_name[m] for m in nonexpr))
        r.join(fx.dd.drop_duplicates("drug").set_index("drug")[["moa_fine", "targets"]], on="drug") \
            .sort_values("z").to_csv(lsd, index=False)
    elif os.path.exists(lsd):
        os.remove(lsd)
    DA = np.asarray(fx.DD_A)
    xr = np.log2(lc + 0.5)
    lv = fx.dd[["drug", "conc", "moa_fine"]].copy()
    lv["spearman_growth_vs_level"] = [spearman(DA[i, use], xr[use]) for i in range(len(fx.dd))]
    lv["z"] = np.arctanh(lv["spearman_growth_vs_level"].clip(-0.999, 0.999)) * math.sqrt(max(use.sum() - 3, 1))
    lv["q"] = T.bh(2 * norm_sf(np.abs(lv["z"].to_numpy())))
    lv.sort_values("z").to_csv(os.path.join(folder, "level_vs_growth.csv"), index=False)
    files = [("drug_effects.csv", "every drug-dose: fold change, z, q up/down, z at each dose, dose pattern, flags, "
                                  "% of lines up, context"),
             ("coregulated_genes.csv", f"correlation with every gene across drug wells: raw, minus {N_PCS} and minus "
                                       "10 broad components (strong real modules can also be components: compare), "
                                       "and the data-driven program each gene belongs to (see ../programs/)"),
             ("baseline_by_line.csv", "level in each line (all wells pooled), vs the median line, expressing flag"),
             ("level_vs_growth.csv", "does a line's level of this gene predict how a drug-dose affects its growth "
                                     "(Spearman across lines, z, q; negative = high-expressing lines depleted more)")]
    if os.path.exists(lsd):
        files.append(("loss_selective_drugs.csv", "drugs that deplete the lines not expressing this gene more than "
                                                  "the other lines in the same wells"))
    write_brief(folder, f"Focus gene {gene}", f"""
Everything the data say about {gene}: which drugs raise or lower it (and whether each effect is clean: dose-consistent,
broad across lines, not toxic, not shutdown, not cell-cycle composition, not part of a broad program), what it is
co-regulated with (and so what probably controls it), which lines lack or over-express it, and whether its level or
loss creates selective vulnerabilities. For context, an earlier pass on MTAP and Gankyrin (PSMD10) found: MTAP
tracked the growth program and had no convincing inducer (bentamapimod 5 uM ~1.25x was the best); Gankyrin followed
the chaperone/heat-shock network rather than the proteasome recovery response; MTAP-null lines were selectively
depleted by pemetrexed. Confirm or revise these with the files here.
""", files, deeper_queries(fx.out))


def cmd_angles(args):
    quiet()
    D = dirs(args.out)
    fx = FX(args.out)
    sel = [a.strip() for a in args.angles.split(",") if a.strip()] if args.angles else ANGLES + ["focus"]
    failed = []
    for a in [a for a in ANGLES if a in sel]:
        folder = os.path.join(D["ang"], a)
        os.makedirs(folder, exist_ok=True)
        log(f"Angle: {a} ...")
        t0 = time.time()
        try:
            globals()[f"angle_{a}"](fx, folder)
            log(f"  {a} done in {time.time() - t0:.0f} s")
        except Exception:  # noqa: BLE001
            failed.append(a)
            log(f"  ERROR in angle {a} (the other angles continue):\n{traceback.format_exc()}")
    focus = [g.strip() for g in args.focus_genes.split(",") if g.strip()] if "focus" in sel else []
    if focus:
        specs = {}
        for gname in focus:
            c = fx.col_of(gname)
            if c is not None and fx.gmask[c]:
                specs[gname] = [int(fx.genes.at[c, "token"])]
        per = {}
        if specs:
            log(f"  per-line effects for focus genes: {', '.join(specs)} ...")
            per_dd = per_line_columns(fx, specs)
            per = {gname: per_dd[:, :, j] for j, gname in enumerate(specs)}
        for gname in focus:
            folder = os.path.join(D["ang"], f"focus_{safe_name(gname)}")
            os.makedirs(folder, exist_ok=True)
            log(f"Focus: {gname} ...")
            try:
                angle_focus(fx, folder, gname, per.get(gname))
            except Exception:  # noqa: BLE001
                failed.append(f"focus_{gname}")
                log(f"  ERROR in focus {gname}:\n{traceback.format_exc()}")
    log(f"Angles done -> {D['ang']}" + (f"; FAILED: {', '.join(failed)}" if failed else ""))


# ============================================================================= lookup
def cmd_lookup(args):
    quiet()
    fx = FX(args.out)
    kind, name = args.kind, " ".join(args.name)
    pd.set_option("display.width", 220)
    pd.set_option("display.max_columns", 20)
    if kind in ("gene", "corr"):
        c = fx.col_of(name)
        if c is None or not fx.gmask[c]:
            sys.exit(f"{name}: not among the tested genes")
        print(card_gene(fx, c) if kind == "gene" else card_corr(fx, c))
    elif kind == "drug":
        drugs = sorted(fx.rows_of_drug)
        hits = [d for d in drugs if d.lower() == name.lower()] or [d for d in drugs if name.lower() in d.lower()]
        if not hits:
            sys.exit(f"{name}: no such drug")
        for d in hits[:5]:
            print(card_drug(fx, d))
    elif kind == "line":
        names = pd.Series(fx.line_name).str.lower()
        ids = fx.lines["cell_line_id"].str.lower()
        n = name.lower()
        hit = np.flatnonzero((names == n) | (ids == n))
        if not hit.size:
            hit = np.flatnonzero(names.str.contains(n, regex=False) | ids.str.contains(n, regex=False))
        if not hit.size:
            sys.exit(f"{name}: no such cell line")
        print(card_line(fx, int(hit[0])))
    else:
        sys.exit("lookup kinds: gene, corr, drug, line")


# ============================================================================= commands shown to the user and agents
def shell_quote(p):
    """A path as the shell needs it: PowerShell on Windows ("..." when needed), sh elsewhere."""
    p = str(p)
    if sys.platform == "win32":
        return f'"{p}"' if not p or any(c in p for c in " &();,'{}") else p
    return shlex.quote(p)


def rel_path(p):
    """p relative to the current folder when it lies below it, else absolute (for messages)."""
    try:
        r = os.path.relpath(p)
    except ValueError:                          # another drive (Windows)
        return os.path.abspath(p)
    return os.path.abspath(p) if r.startswith("..") else r


def user_cmd(command, extra=""):
    """What the user types to run `tahoe_atlas.py <command>` with this Python."""
    me = os.path.abspath(__file__)
    here = os.path.normcase(os.path.dirname(me)) == os.path.normcase(os.getcwd())
    return f"{T.py_cmd()} {os.path.basename(me) if here else shell_quote(me)} {command}{extra}"


def long_run_hint(command, extra="", out="atlas"):
    """How to start a long run of `command` here, and where its log is (the script writes it itself)."""
    logf = rel_path(os.path.join(out, "agents.log" if command == "agents" else "atlas.log"))
    if sys.platform == "win32":
        return f"{user_cmd(command, extra)}   (leave the window open; log in {logf})"
    return f"nohup {user_cmd(command, extra)} > /dev/null 2>&1 &   then: tail -f {shell_quote(logf)}"


def same_folders(args, workers=0):
    """--data / --out (when not the defaults) and --workers, so a printed command works on the same folders."""
    s = ""
    if os.path.abspath(args.data) != os.path.abspath("."):
        s += " --data " + shell_quote(args.data)
    if os.path.abspath(args.out) != os.path.abspath(os.path.join(args.data, "atlas")):
        s += " --out " + shell_quote(args.out)
    return s + (f" --workers {workers}" if workers else "")


def key_hint():
    return ('$env:ANTHROPIC_API_KEY="sk-ant-..." (in the same window)' if sys.platform == "win32"
            else "export ANTHROPIC_API_KEY=sk-ant-...")


def sdk_hint():
    return f"{T.py_cmd()} -m pip install claude-agent-sdk"      # into this very Python, not whichever pip is first


def sandbox_problem():
    """Why --sandbox cannot work on this computer, or None (macOS: built in; Linux: bubblewrap + socat)."""
    if sys.platform == "win32":
        return ("--sandbox is not available on Windows (Claude Code cannot sandbox commands there); run without it: "
                "the refusal rules (delete, kill, network, installs) still apply")
    if sys.platform != "darwin" and not (shutil.which("bwrap") and shutil.which("socat")):
        return "--sandbox needs bubblewrap and socat:  sudo apt-get install -y bubblewrap socat"
    return None


def here_hints():
    return (f"On this computer:\n  long run:   {long_run_hint('compute')}\n  API key:    {key_hint()}\n"
            f"  agent SDK:  {sdk_hint()}")


# ============================================================================= agents
AGENT_APPEND = """You are a careful computational biologist analysing one angle of the Tahoe-100M single-cell drug
perturbation atlas. You run unattended: nobody will answer questions or grant permissions, so never ask; decide,
state your assumptions in the report, and keep going. Work in your current folder (write your scripts and report.md
there); the effects matrices and cards elsewhere in the atlas folder may be read. {shell}Compute every number you
report with Python: write a .py script in this folder and run it with `{py} script.py` (always allowed). If any
command is refused, do the same thing in Python instead; never stop because of a refusal.
Do not install packages, use the network, delete files or write anything outside the atlas folder (reading files
and running the look-up commands named in brief.md is allowed). Your job is finished only when report.md exists and
follows brief.md; a precise, well-checked report matters more than a long one."""

NUDGE = """{report} does not exist yet. Write it now, as your task (brief.md, if there is one) specifies: compute the
numbers you need with Python (write a script in this folder and run it with `{py} script.py`; that is always
allowed), then write {report}. Do not ask questions and do not stop until {report} is written."""

DENY = ["Bash(rm *)", "Bash(rm)", "Bash(rmdir *)", "Bash(sudo *)", "Bash(su *)", "Bash(kill *)", "Bash(pkill *)",
        "Bash(killall *)", "Bash(curl *)", "Bash(wget *)", "Bash(ssh *)", "Bash(scp *)", "Bash(rsync *)",
        "Bash(git *)", "Bash(pip *)", "Bash(pip3 *)", "Bash(conda *)", "Bash(apt *)", "Bash(apt-get *)",
        "Bash(shutdown *)", "Bash(reboot *)", "Bash(dd *)", "Bash(mkfs *)", "Bash(chown *)", "Bash(nohup *)",
        "Bash(*-m pip *)"]
# the same intents for the PowerShell tool (Windows); each command both with and without arguments
DENY_PS = [f"PowerShell({c}{a})" for c in (
    "Remove-Item", "rm", "del", "erase", "rd", "rmdir", "ri", "Clear-Content",                  # delete
    "Stop-Process", "kill", "spps", "taskkill",                                                 # kill
    "Stop-Computer", "Restart-Computer", "shutdown", "Format-Volume", "Clear-Disk",             # power, disk
    "Invoke-WebRequest", "iwr", "curl", "curl.exe", "wget", "Invoke-RestMethod", "irm",         # network
    "Start-BitsTransfer", "ssh", "scp",
    "git", "pip", "pip3", "conda", "winget", "choco",                                           # vcs, packages
    "Set-ExecutionPolicy", "Start-Process", "runas") for a in (" *", "")] + ["PowerShell(*-m pip *)"]


def agent_python():
    """How the agents run this Python (it has numpy, pandas, pyarrow): sys.executable; in PowerShell
    & "C:\\path with spaces\\python.exe" when the path needs quotes."""
    exe = sys.executable or "python3"
    if sys.platform == "win32":
        q = shell_quote(exe)
        return f"& {q}" if q != exe else exe
    return shlex.quote(exe)


def agent_text(template, **fields):
    """Fill {py} (how to run this Python), {shell} (on Windows: the shell is PowerShell), {report} (default
    report.md) and any other {fields} in an agent text."""
    shell = ("Your shell is PowerShell (Windows), not bash: use PowerShell syntax. In Python write Windows paths as "
             "raw strings (r'C:\\tahoe\\...') or with forward slashes ('C:/tahoe/...'), never as plain '...\\...' "
             "strings ('\\t' and '\\r' would become control characters). " if sys.platform == "win32" else "")
    return template.format(**{"py": agent_python(), "shell": shell, "report": "report.md", **fields})


def deny_rules():
    """Commands the agents may never run: the Bash list everywhere, plus the PowerShell list on Windows."""
    return DENY + (DENY_PS if sys.platform == "win32" else [])


def git_bash():
    """Git Bash on Windows (the agents' Bash tool needs it; WSL's bash.exe does not count), else None."""
    for p in (os.environ.get("CLAUDE_CODE_GIT_BASH_PATH"), shutil.which("bash"), r"C:\Program Files\Git\bin\bash.exe"):
        if p and os.path.exists(p) and not re.search(r"system32|windowsapps", p, re.I):
            return p
    return None


def agent_tools(web=False):
    """Files, search and a shell: Bash; on Windows PowerShell (plus Bash when Git Bash is installed)."""
    shells = (["PowerShell"] + (["Bash"] if git_bash() else [])) if sys.platform == "win32" else ["Bash"]
    return ["Read", "Write", "Edit", "Glob", "Grep"] + shells + (["WebSearch", "WebFetch"] if web else [])


SYNTH_TASK = """Read every report in this folder (all *.md files except 00_overview.md) and write 00_overview.md:
a single overview of what Tahoe-100M shows across all angles. Start with the 5-8 most important findings (each with
its numbers and which report it comes from), then where the angles agree or disagree, the main caveats about the
data, and a ranked list of the 10 best leads to test experimentally. At most ~1,500 words, plain language, Markdown.
Do not invent numbers: use only what the reports state. Run unattended; never ask questions."""

FALLBACK_TAG = "<!-- agent did not write its report; last messages below -->"


def agent_jobs(D, args, order=None, append=None):
    """One job per folder under D['ang'] with a brief.md; its report is copied to D['rep']/NN_<name>.md, NN = the
    folder's position in `order` (default ANGLES), 50 for the others. args.angles (if present) picks a subset.
    append: the agents' system-prompt addition (default: AGENT_APPEND for this computer)."""
    num = {a: i + 1 for i, a in enumerate(order or ANGLES)}
    want = {a.strip() for a in (getattr(args, "angles", "") or "").split(",") if a.strip()} or None
    append = agent_text(AGENT_APPEND) if append is None else append
    jobs = []
    for folder in sorted(glob.glob(os.path.join(D["ang"], "*"))):
        name = os.path.basename(folder)
        brief = os.path.join(folder, "brief.md")
        if not os.path.exists(brief):
            continue
        if want and name not in want and not (name.startswith("focus_") and "focus" in want):
            continue
        out = os.path.join(D["rep"], f"{num.get(name, 50):02d}_{name}.md")
        jobs.append({"name": name, "cwd": folder, "out": out, "report": os.path.join(folder, "report.md"),
                     "brief": brief, "append": append,
                     "prompt": "Read brief.md in this folder, analyse the data as it asks, and write report.md here."})
    return jobs


def up_to_date(job):
    out = job["out"]
    if not os.path.exists(out) or os.path.getsize(out) < 200:
        return False
    with open(out, encoding="utf-8", errors="replace") as fh:
        if FALLBACK_TAG in fh.read(500):
            return False
    return os.path.getmtime(out) >= os.path.getmtime(job["brief"])


def agent_options(job, args, resume=None, budget=None, max_turns=None):
    from claude_agent_sdk import ClaudeAgentOptions
    fields = {f.name for f in dataclasses.fields(ClaudeAgentOptions)}
    tools = agent_tools(args.web)
    want = {"cwd": job["cwd"], "tools": tools, "allowed_tools": list(tools), "disallowed_tools": deny_rules(),
            "permission_mode": args.permission_mode, "setting_sources": [], "add_dirs": [os.path.abspath(args.out)],
            "system_prompt": {"type": "preset", "preset": "claude_code", "append": job["append"]},
            "model": args.model, "max_turns": max_turns or args.max_turns,
            "max_budget_usd": args.budget if budget is None else budget}
    if sys.platform == "win32":                 # else any Bash deny rule silently switches the PowerShell tool off
        want["env"] = {"CLAUDE_CODE_USE_POWERSHELL_TOOL": "1"}
    if resume:
        want["resume"] = resume
    if args.sandbox:
        want["sandbox"] = {"enabled": True, "autoAllowBashIfSandboxed": True, "allowUnsandboxedCommands": False}
    missing = [k for k in want if k not in fields]
    if missing:
        log(f"  note: this claude-agent-sdk version has no option(s) {missing}; continuing without them")
    return ClaudeAgentOptions(**{k: v for k, v in want.items() if k in fields})


async def _one_query(prompt, options, logf, texts):
    from claude_agent_sdk import AssistantMessage, ResultMessage, TextBlock, ToolUseBlock, query
    result = None
    async for msg in query(prompt=prompt, options=options):
        if isinstance(msg, AssistantMessage):
            for b in msg.content:
                if isinstance(b, TextBlock):
                    texts.append(b.text)
                    logf.write(b.text + "\n")
                elif isinstance(b, ToolUseBlock):
                    logf.write(f"[tool] {b.name}: {json.dumps(b.input)[:600]}\n")
            logf.flush()
        elif isinstance(msg, ResultMessage):
            result = msg
    return result


async def run_agent(job, args, sem):
    async with sem:
        t0 = time.time()
        log(f"Agent {job['name']}: started")
        rep = job["report"]
        if os.path.exists(rep):
            os.replace(rep, rep + ".prev")        # never pass off an old report as new
        results, texts, err = [], [], ""
        with open(os.path.join(job["cwd"], "agent.log"), "w", encoding="utf-8") as logf:
            try:
                r = await _one_query(job["prompt"], agent_options(job, args), logf, texts)
                results.append(r)
                sid = getattr(r, "session_id", None)
                if not os.path.exists(rep) and sid:          # one nudge, in the same session, within the cap
                    left = args.budget - (getattr(r, "total_cost_usd", None) or 0.0)
                    name = os.path.basename(rep)
                    if left < max(0.25, 0.1 * args.budget):
                        logf.write(f"[harness] {name} missing; not resuming: ${left:.2f} of the "
                                   f"${args.budget:g} cap left\n")
                        log(f"Agent {job['name']}: no report and only ${left:.2f} of its cap left: not resuming")
                    else:
                        logf.write(f"[harness] {name} missing: resuming the session once (${left:.2f} left)\n")
                        log(f"Agent {job['name']}: no report yet, resuming once with the ${left:.2f} left of its cap")
                        nudge = agent_text(NUDGE, report=name)
                        results.append(await _one_query(nudge, agent_options(job, args, resume=sid, budget=left),
                                                        logf, texts))
            except Exception as e:  # noqa: BLE001  (CLI/process errors; the report may still exist)
                err = f"{type(e).__name__}: {e}"
                logf.write(f"[error] {err}\n")
        if os.path.exists(rep):
            if os.path.abspath(rep) != os.path.abspath(job["out"]):
                shutil.copy(rep, job["out"])
        elif texts:
            with open(job["out"], "w", encoding="utf-8") as fh:
                fh.write(f"# {job['name']}\n{FALLBACK_TAG}\n\n" + "\n\n".join(texts[-3:]))
        for old in glob.glob(os.path.join(os.path.dirname(job["out"]), f"[0-9][0-9]_{glob.escape(job['name'])}.md")):
            if os.path.exists(job["out"]) and os.path.abspath(old) != os.path.abspath(job["out"]):
                os.remove(old)               # same angle under an older number (angles were added since)
        results = [r for r in results if r is not None]
        last = results[-1] if results else None
        rec = {"agent": job["name"], "minutes": round((time.time() - t0) / 60, 1),
               "status": getattr(last, "subtype", "no result"), "is_error": getattr(last, "is_error", None),
               "turns": sum(getattr(r, "num_turns", 0) or 0 for r in results),
               "cost_usd": sum(getattr(r, "total_cost_usd", 0) or 0 for r in results),
               "tool_calls_denied": sum(len(getattr(r, "permission_denials", None) or []) for r in results),
               "resumed": len(results) > 1, "error": err,
               "report": job["out"] if os.path.exists(rep) else ("fallback" if texts else "")}
        log(f"Agent {job['name']}: {rec['status']} in {rec['minutes']} min, {rec['turns']} turns, "
            f"${(rec['cost_usd'] or 0):.2f}" + (f", ERROR {err}" if err else "")
            + ("" if os.path.exists(rep) else " (no report.md written)"))
        return rec


async def ping_agent(args):
    """One tiny agent call with the real settings: proves the SDK, its bundled engine, the key and the model work."""
    d = os.path.join(args.out, "check")
    os.makedirs(d, exist_ok=True)
    texts = []
    with open(os.path.join(d, "agent.log"), "w", encoding="utf-8") as logf:
        r = await _one_query("Reply with the single word: ready",
                             agent_options({"cwd": d, "append": "Reply briefly."}, args, budget=0.25, max_turns=2),
                             logf, texts)
    ok = r is not None and not getattr(r, "is_error", True) and any("ready" in t.lower() for t in texts)
    return ok, (f"{getattr(r, 'subtype', 'no result')}, model {args.model}, ${getattr(r, 'total_cost_usd', 0) or 0:.3f}"
                + ("" if ok else f"; reply: {' '.join(texts)[:200] or '-'} (see {os.path.join(d, 'agent.log')})"))


def cmd_check(args):
    """Preflight: is this machine ready for a full run? Prints one line per check."""
    bad = []

    def say(ok, msg, fatal=True):
        if not ok and fatal:
            bad.append(msg)
        print(f"[{'ok  ' if ok else ('FAIL' if fatal else 'warn')}] {msg}", flush=True)

    v = sys.version_info
    say(v >= (3, 10), f"Python {v.major}.{v.minor}.{v.micro}" + ("" if v >= (3, 10) else " (the agent SDK needs 3.10+)"))
    say(True, f"numpy {np.__version__}, pandas {pd.__version__}, pyarrow {pa.__version__}")
    try:
        import scipy
        say(True, f"scipy {scipy.__version__}")
    except ImportError:
        say(False, "scipy not installed (optional: built-in fallbacks are used)", fatal=False)
    idx = T.discover(args.data, args.out, refresh=args.reindex)
    ne = len(idx["expression"])
    say(ne > 0, f"{ne:,} expression files under {os.path.abspath(args.data)}" + ("" if ne else ": wrong --data folder?"))
    if 0 < ne < 3000:
        say(False, f"only {ne:,} expression files (the full dataset has ~3,388): is the download complete? "
            "When it is, run again with --reindex", fatal=False)
    if ne:
        miss = [c for c in BUILD_COLS if c not in set(pq.read_schema(idx["expression"][0]).names)]
        say(not miss, "expression columns present" if not miss else f"expression files lack columns {miss}")
    for k, fatal in (("gene", True), ("sample", True), ("cell_line", False), ("drug", False)):
        say(bool(idx[k]), f"{k} metadata: {len(idx[k])} file(s)" + ("" if idx[k] else
            (" - needed" if fatal else " - missing: mutation/organ or mechanism angles will be thin")), fatal=fatal)
    G = 62713
    gm = T.read_tables(idx["gene"], ["token_id"]) if idx["gene"] else None
    if gm is not None:
        G = int(gm["token_id"].max()) + 1
    need = 14 * 5000 * G * 4 / 1e9 + 3
    os.makedirs(args.out, exist_ok=True)
    free = shutil.disk_usage(args.out).free / 1e9
    say(free >= need, f"disk: {free:.0f} GB free at {os.path.abspath(args.out)}, ~{need:.0f} GB needed")
    kind = T.disk_kind(args.data)
    if kind == "hdd":
        say(False, "disk type: the data seem to sit on a hard drive (HDD); parallel readers make a hard drive seek "
            "constantly, so --workers 2 usually reads faster (added to the command below; some cloud SSDs also "
            "report as HDD: then leave it out)", fatal=False)
    else:
        say(True, "disk type: SSD" if kind == "ssd" else "disk type: could not be determined (SSD or hard drive; "
            "on a hard drive --workers 2 usually reads faster)")
    mem, cpus = T.mem_available_gb(), os.cpu_count() or 1
    per_worker = 5000 * G * 4 / 1e9 * 1.3 + 1.0
    workers = max(1, min(14, max(1, cpus - 1), int((mem or 0) / per_worker) or 1))
    say(mem is None or mem >= per_worker + 5, f"memory: {mem or 0:.0f} GB free, {cpus} CPUs -> {workers} build workers "
        f"(~{per_worker:.1f} GB each)" + ("" if workers >= 7 else "; fewer workers = slower build, still fine"),
        fatal=mem is not None and mem < per_worker + 3)
    agent_todo = []                       # the agents step only: warnings, not failures, for the computation
    sdk = False
    try:
        import claude_agent_sdk
        sdk = True
        say(True, f"claude-agent-sdk {getattr(claude_agent_sdk, '__version__', '?')}")
    except ImportError:
        agent_todo.append(sdk_hint())
        say(False, f"claude-agent-sdk not installed (needed only for the agents step): {sdk_hint()}", fatal=False)
    keys = ["ANTHROPIC_API_KEY", "ANTHROPIC_AUTH_TOKEN", "CLAUDE_CODE_USE_BEDROCK", "CLAUDE_CODE_USE_VERTEX",
            "CLAUDE_CODE_OAUTH_TOKEN"]
    auth = any(os.environ.get(k) for k in keys)
    if not auth:
        agent_todo.append(key_hint())
    say(auth, "API key found in the environment" if auth else
        "ANTHROPIC_API_KEY not set (needed only for the agents step)", fatal=False)
    if sdk and auth and not args.dry_run:
        try:
            ok, info = asyncio.run(ping_agent(args))
        except Exception as e:  # noqa: BLE001
            ok, info = False, f"{type(e).__name__}: {e}"
        if not ok:
            agent_todo.append("fix the live agent test above (key, network or model name)")
        say(ok, f"live agent test: {info}", fatal=False)
    if args.sandbox:
        prob = sandbox_problem()
        say(prob is None, prob or ("--sandbox: built in on macOS" if sys.platform == "darwin" else
                                   "--sandbox: bubblewrap and socat found"), fatal=False)
    print()
    if bad:
        print(f"{len(bad)} problem(s) to fix before computing (see FAIL lines above).")
        sys.exit(1)
    hint_workers = args.workers or (2 if kind == "hdd" else 0)
    print("Ready to compute:  " + long_run_hint("compute", same_folders(args, hint_workers), args.out))
    print("Agents step: " + (f"ready too, after compute:  {long_run_hint('agents', same_folders(args), args.out)}"
                             if not agent_todo else "before it: " + ";  ".join(agent_todo)))


DIAGNOSTICS = [   # (path under the atlas folder, max rows or None): what Claude needs to check the computation
    ("build_info.json", None), ("well_position_check.csv", None), ("sample_map.csv", None),
    ("effects/info.json", None), ("effects/complete.json", None), ("effects/drugdose.csv", None),
    ("effects/lines.csv", None),
    ("effects/failed_wells.csv", None), ("effects/plates.csv", None),
    ("angles/quality/summary.json", None), ("angles/quality/position_effects.csv", None),
    ("angles/quality/plate_dmso_offsets.csv", None), ("angles/quality/replicates.csv", None),
    ("angles/quality/position_sensitive_genes.csv", 300), ("angles/quality/calibration_by_gene.csv", 500),
    ("angles/drugs/drug_summary.csv", None), ("angles/genes/inducible_genes.csv", 500),
    ("angles/genes/repressible_genes.csv", 500), ("angles/classes/class_summary.csv", None),
    ("angles/classes/target_mrna_response.csv", 500),
    ("angles/cell_lines/line_summary.csv", None), ("angles/cell_lines/genotype_selective_drugs.csv", 1500),
    ("angles/cell_lines/expression_loss_groups.csv", None),
    ("angles/cell_lines/expression_loss_selective_drugs.csv", 1500),
    ("angles/biomarkers/selective_drugs.csv", None), ("angles/biomarkers/biomarker_top10.csv", 3000),
    ("angles/biomarkers/target_level_vs_sensitivity.csv", 500),
    ("angles/line_response/drug_response_heterogeneity.csv", None),
    ("angles/line_response/line_responsiveness.csv", None), ("angles/line_response/feature_response_top.csv", 500),
    ("angles/programs/programs.csv", None), ("angles/programs/broad_components.csv", None),
    ("angles/cell_state/drug_cell_cycle.csv", None), ("angles/cell_state/proliferation_dependent_drugs.csv", 300),
]
FOCUS_DIAGNOSTICS = [("drug_effects.csv", None), ("coregulated_genes.csv", 400), ("baseline_by_line.csv", None),
                     ("loss_selective_drugs.csv", 300), ("level_vs_growth.csv", 300)]


def cmd_bundle(args):
    """One small zip to upload to Claude: the computation's key tables (to check the numbers before the agents)
    and, once the agents have run, every report and agent log."""
    D = dirs(args.out)
    path = os.path.join(args.out, "atlas_bundle.zip")
    reps = sorted(glob.glob(os.path.join(D["rep"], "*.md")))
    items = list(DIAGNOSTICS)
    for fd in sorted(glob.glob(os.path.join(D["ang"], "focus_*"))):
        items += [(os.path.relpath(os.path.join(fd, f), args.out), n) for f, n in FOCUS_DIAGNOSTICS]
    n_tables = 0
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        for rel, nrows in items:
            src = os.path.join(args.out, rel)
            if not os.path.exists(src):
                continue
            arc = os.path.join("computation", rel)
            if nrows and src.endswith(".csv"):
                t = pd.read_csv(src, nrows=nrows)
                z.writestr(arc, t.to_csv(index=False))
            else:
                z.write(src, arc)
            n_tables += 1
        # the run logs the script writes, then console logs that older instructions redirected next to the data
        logs = [(os.path.join(args.out, "atlas.log"), "computation/atlas.log"),
                (os.path.join(args.out, "agents.log"), "agent_logs/agents.log")]
        logs += [(os.path.join(d, f"{n}.log"), f"{'computation' if n == 'atlas' else 'agent_logs'}/{n}_console.log")
                 for n in ("atlas", "agents") for d in (".", args.data)]
        seen = set()
        for src, arc in logs:
            src = os.path.abspath(src)
            if src not in seen and os.path.isfile(src):
                seen.add(src)
                add_log(z, src, arc)
        for f in reps + [os.path.join(D["rep"], "agents_summary.csv")]:
            if os.path.exists(f):
                z.write(f, os.path.join("reports", os.path.basename(f)))
        for f in sorted(glob.glob(os.path.join(D["ang"], "*", "agent.log"))):
            z.write(f, os.path.join("agent_logs", os.path.basename(os.path.dirname(f)) + ".log"))
    if not n_tables and not reps:
        os.remove(path)
        log("Nothing to bundle yet: run 'compute' first")
        return
    what = f"{n_tables} computation tables" + (f" and {len(reps)} reports" if reps else "")
    log(f"Bundled {what} -> {os.path.abspath(path)} ({os.path.getsize(path) / 1e6:.1f} MB). "
        + ("Upload it" if sys.platform == "win32" else "Download it (e.g. scp) and upload it") + " to Claude"
        + (" to turn each report into a doc." if reps else " to check the numbers before running the agents."))


def add_log(z, src, arc, cap=20_000_000):
    """Put a log into the zip; a log larger than cap bytes goes in as its last cap bytes."""
    size = os.path.getsize(src)
    if size <= cap:
        z.write(src, arc)
        return
    with open(src, "rb") as fh:
        fh.seek(size - cap)
        tail = fh.read(cap)
    z.writestr(arc, f"[first {(size - cap) / 1e6:.0f} MB of {os.path.basename(src)} left out]\n".encode() + tail)


def check_auth():
    keys = ["ANTHROPIC_API_KEY", "ANTHROPIC_AUTH_TOKEN", "CLAUDE_CODE_USE_BEDROCK", "CLAUDE_CODE_USE_VERTEX",
            "CLAUDE_CODE_OAUTH_TOKEN"]
    if not any(os.environ.get(k) for k in keys):
        sys.exit(f"Set your API key first:  {key_hint()}   (or run 'compute' for the computation alone)")


def cmd_agents(args, D=None, order=None, synth_task=None, append=None):
    """One agent per folder with a brief.md under D['ang'], reports in D['rep'], then an overview agent.
    Defaults are the atlas's: dirs(args.out), ANGLES order, SYNTH_TASK, AGENT_APPEND. Another script can run the
    same stage on its own folders with its own order, overview task and system-prompt addition (used verbatim;
    agent_text() fills {py} and {shell})."""
    D = D or dirs(args.out)
    os.makedirs(D["rep"], exist_ok=True)
    jobs = agent_jobs(D, args, order, append)
    if not jobs:
        sys.exit(f"No folders with a brief.md under {D['ang']} (atlas: run 'angles' first)")
    todo = [j for j in jobs if args.redo or not up_to_date(j)]
    skipped = [j["name"] for j in jobs if j not in todo]
    if skipped:
        log(f"Already reported (newer than their data; --redo to rerun): {', '.join(skipped)}")
    ov_out = os.path.join(D["rep"], "00_overview.md")
    reports = [j["out"] for j in jobs]
    if args.dry_run:
        for j in todo:
            with open(os.path.join(j["cwd"], "agent_prompt.txt"), "w", encoding="utf-8") as fh:
                fh.write("SYSTEM (appended to the Claude Code preset):\n" + j["append"] + "\n\nPROMPT:\n" + j["prompt"])
        n = len(todo) + (0 if args.skip_overview else 1)
        log(f"Dry run: {len(todo)} agents planned: {', '.join(j['name'] for j in todo) or '-'}"
            + ("" if args.skip_overview else " + overview")
            + f"; prompts written as agent_prompt.txt. Cost cap: {n} x ${args.budget:g} = ${n * args.budget:g} "
              f"(each agent stops at its cap; the SDK's cost estimate can overshoot it slightly; actual cost is "
              f"usually well below)")
        return
    check_auth()
    try:
        import claude_agent_sdk  # noqa: F401
    except ImportError:
        sys.exit(f"Install the agent SDK first:  {sdk_hint()}")
    if args.sandbox and sandbox_problem():
        sys.exit(sandbox_problem())
    log(f"Running {len(todo)} agents, {args.parallel} at a time, model {args.model}, "
        f"cap ${args.budget:g} and {args.max_turns} turns each")

    async def main():
        sem = asyncio.Semaphore(max(1, args.parallel))
        recs = list(await asyncio.gather(*(run_agent(j, args, sem) for j in todo)))
        have = [r for r in reports if os.path.exists(r)]
        newest = max((os.path.getmtime(r) for r in have), default=0)
        if not args.skip_overview and have and (args.redo or not os.path.exists(ov_out)
                                                or os.path.getmtime(ov_out) < newest):
            ov = {"name": "overview", "cwd": D["rep"], "out": ov_out, "report": ov_out, "brief": ov_out,
                  "prompt": synth_task or SYNTH_TASK,
                  "append": "You write the overview of a set of analysis reports. Work only in this folder and "
                            "never ask questions."}
            recs.append(await run_agent(ov, args, asyncio.Semaphore(1)))
        return recs

    recs = asyncio.run(main())
    summ = os.path.join(D["rep"], "agents_summary.csv")
    old = pd.read_csv(summ) if os.path.exists(summ) else pd.DataFrame()
    new = pd.DataFrame(recs)
    if len(old) and "agent" in old:
        old = old[~old["agent"].isin(new.get("agent", []))]
    pd.concat([old, new], ignore_index=True).to_csv(summ, index=False)
    total = sum((r.get("cost_usd") or 0) for r in recs)
    ok = sum(1 for r in recs if r["report"] and r["report"] != "fallback")
    log(f"Agents done: {ok}/{len(recs)} wrote their report -> {D['rep']} (cost this run ${total:.2f}; "
        f"details in agents_summary.csv and each angle's agent.log)")


# ============================================================================= main
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter,
                                 epilog=here_hints())
    ap.add_argument("command", choices=["check", "compute", "build", "effects", "angles", "agents", "all", "bundle",
                                        "lookup"])
    ap.add_argument("kind", nargs="?", help="lookup: gene | drug | line | corr")
    ap.add_argument("name", nargs="*", help="lookup: the gene, drug or line")
    ap.add_argument("--data", default=".", help="Tahoe-100M download folder (default: current folder)")
    ap.add_argument("--out", default=None, help="output folder (default: <data>/atlas)")
    ap.add_argument("--workers", type=int, default=0, help="build: plates read at once (default: from CPUs and "
                                                           "free memory; 2 is often faster from a hard drive)")
    ap.add_argument("--batch-size", type=int, default=20000, help="build: cells per batch per worker")
    ap.add_argument("--limit-files", type=int, default=0, help="trial run on the first N expression files "
                                                               "(use a separate --out)")
    ap.add_argument("--layout", default=None, help="CSV sample,well to override well positions")
    ap.add_argument("--min-cells", type=int, default=0, help="cells per line per well needed (default 30; "
                                                             "lowered automatically for small trial runs)")
    ap.add_argument("--reindex", action="store_true", help="rescan the download folder for its parquet files")
    ap.add_argument("--angles", default="", help="comma-separated subset of: " + ",".join(ANGLES) + ",focus")
    ap.add_argument("--focus-genes", default="MTAP,PSMD10", help="genes that get their own focus report")
    ap.add_argument("--model", default="sonnet", help="agent model: sonnet, opus, or a full model ID")
    ap.add_argument("--budget", type=float, default=5.0, help="USD cap per agent (its one 'write the report' "
                                                              "nudge only gets what is left of it)")
    ap.add_argument("--max-turns", type=int, default=80, help="turns per agent")
    ap.add_argument("--parallel", type=int, default=3, help="agents running at once")
    ap.add_argument("--permission-mode", default="dontAsk", help="Claude Code permission mode of the agents "
                                                                 "(dontAsk: anything not allowed is refused)")
    ap.add_argument("--web", action="store_true", help="let agents use web search to check the literature")
    ap.add_argument("--sandbox", action="store_true", help="run agent shell commands sandboxed (Linux: bubblewrap; "
                                                           "macOS: built in; not available on Windows)")
    ap.add_argument("--redo", action="store_true", help="agents: rerun even if a report is already up to date")
    ap.add_argument("--skip-overview", action="store_true", help="agents: no overview report")
    ap.add_argument("--dry-run", action="store_true", help="agents: write the prompts, call nothing")
    args = ap.parse_args()
    args.out = args.out or os.path.join(args.data, "atlas")
    os.makedirs(args.out, exist_ok=True)
    T.safe_console()
    if args.command == "lookup":
        if not args.kind or not args.name:
            sys.exit("usage: tahoe_atlas.py lookup gene|drug|line|corr NAME")
        return cmd_lookup(args)
    if args.command == "check":
        return cmd_check(args)
    if args.command == "bundle":
        return cmd_bundle(args)
    T.start_run_log(os.path.join(args.out, "agents.log" if args.command == "agents" else "atlas.log"),
                    "tahoe_atlas.py " + " ".join(sys.argv[1:]))
    try:
        with T.keep_awake(f"tahoe_atlas.py {args.command}"):
            run_steps(args)
    except SystemExit as e:
        T.log_exit(e)
        raise


def run_steps(args):
    if args.command == "all" and not args.dry_run:          # fail now, not after hours of computing
        check_auth()
        try:
            import claude_agent_sdk  # noqa: F401
        except ImportError:
            sys.exit(f"Install the agent SDK first ({sdk_hint()}), or run 'compute' for the computation alone")
        if args.sandbox and sandbox_problem():
            sys.exit(sandbox_problem())
    t0 = time.time()
    if args.command in ("build", "all", "compute"):
        cmd_build(args)
    if args.command in ("effects", "all", "compute"):
        cmd_effects(args)
    if args.command in ("angles", "all", "compute"):
        cmd_angles(args)
    if args.command == "compute":
        log(f"Computation done in {(time.time() - t0) / 60:.0f} min. No agent has been called.")
        cmd_bundle(args)
        if args.limit_files:                # a trial: the agents are for the full run
            full = os.path.join(args.data, "atlas")
            log(f"Trial done ({args.limit_files} file{'s' if args.limit_files != 1 else ''}): look at the tables in "
                f"{rel_path(args.out)} (or its "
                f"atlas_bundle.zip), then start the full run: "
                + long_run_hint("compute", same_folders(argparse.Namespace(data=args.data, out=full), args.workers),
                                full))
        else:
            log(f"Next: send atlas_bundle.zip to Claude to check the numbers; then run the agents: first {key_hint()} "
                f"and {sdk_hint()}, then {long_run_hint('agents', same_folders(args), args.out)}")
    if args.command in ("agents", "all"):
        if not effects_ready(args.out):     # the atlas's own agents only (cmd_agents is shared with the panel)
            sys.exit("effects missing, incomplete or from an older version of tahoe_atlas.py; run 'compute' (or "
                     "'effects' and 'angles') again before the agents")
        cmd_agents(args)
        if not args.dry_run:
            cmd_bundle(args)


if __name__ == "__main__":
    main()
