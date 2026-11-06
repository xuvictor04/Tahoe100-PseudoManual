"""atlas_core - the build (one pass over every cell -> counts per well x cell line x gene) and the method-v3 effects
(the corrected effect of every drug-dose on every gene and line), ported verbatim from the old tahoe_atlas.py.

Ported function by function (by syntax tree) from tahoe_atlas.py at commit 28cd834 of xuvictor04/Tahoe100-PseudoManual
(branch claude/tahoe100m-gene-pipeline-lodlx7). Only the module header (imports) is new; every function body is the
original. tahoemap.tensor re-derives the per-cell-line residuals from these same functions and checks itself against
the saved well effects. docs/method.md explains the method.
"""

import argparse
import glob
import json
import math
import multiprocessing as mp
import os
import re
import shutil
import sys
import time
import traceback
import warnings
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor

import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.compute as pc
import pyarrow.parquet as pq

from . import tlib as T

log = T.log


MIN_CELLS = 30             # cells of one line in one well needed to use its expression


MIN_LINES = getattr(T, "MIN_LINES", 5)   # lines needed for a well-level effect (one definition with T)


MIN_CPM = 2.0              # genes kept: pooled level >= this many counts per million


EXPR_FRAC = 0.25           # a line expresses a gene if its level >= this fraction of the median line


LFC_MIN = math.log2(1.2)   # min fold change counted as a change


Q_CUT = 0.10               # FDR cut


N_PCS = 3                  # broad components removed before co-regulation and program finding


TOP = 25                   # top genes per drug, drugs per gene, etc.


ABUND_MIN_FRAC = 0.02      # lines with fewer cells than this fraction of the median line are left out of growth


MIN_SIG_BETA = 20          # significant genes a drug-dose needs before per-line response strength is measured


BUILD_COLS = ["genes", "expressions", "BARCODE_SUB_LIB_ID", "sample", "plate", "drug", "cell_line_id"]


BAD_IDS = {"", "none", "nan", "<na>", "null"}


EFFECTS_VERSION = 3        # effects/complete.json: written last by 'effects'; angles, agents and lookups need it


COMP_MIN_CPM = getattr(T, "COMP_MIN_CPM", 10.0)    # composition shift: genes the line expresses at >= this CPM ...


COMP_MIN_GENES = getattr(T, "COMP_MIN_GENES", 200)  # ... at least this many per profile, else no shift (0)


COMPOSITION_FLAG = getattr(T, "COMPOSITION_FLAG", 0.2)          # |drug-dose composition shift| (log2) flagged


PLATE_SCALE_MIN_WELLS = getattr(T, "PLATE_SCALE_MIN_WELLS", 20)  # smaller (plate, dose) groups join the plate's largest


PLATE_SCALE_FLAG = T.NOISY_PLATE                  # drug-doses (or genes) on plates widened more than this: flagged


PLATE_SCALE_BAND = T.PLATE_SCALE_BAND             # a gene's own spread ratio / this widens it beyond its group


POS_CLEAN_Z = getattr(T, "POS_CLEAN_Z", 3.0)       # pass-2 position donors: |pass-1 z| below this for that gene


DISAGREE_R, DISAGREE_MIN_SIG, DISAGREE_TOP = 0.1, 100, 500   # 'wells disagree': r < 0.1 over the top 500 genes


NOISE_RNA_RE = re.compile(r"^(7SK|RN7SK|RNU|SNOR|SCARNA|MT-|MTND|MTCO|MTATP|MTCY|RP[LS]\d+[A-Z]*P\d|H1-\d|H[2-4]C\d|"
                          r"H2[AB]C\d|ENSG)")       # RULEBOOK rule 7: incl. H1-* histones, RPL13AP5-style pseudogenes


ARTIFACT_FLAGS = ("toxic", "transcription drop", "cell-cycle shift", "unreliable plate only",
                  "position not correctable", "position correction uncertain", "wells disagree")


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


def nanmedian0(V):
    """Median over axis 0 ignoring NaN (by sorting: fast for a few dozen rows x many columns); all-NaN -> NaN."""
    V = np.asarray(V)
    k = np.isfinite(V).sum(axis=0)
    S = np.sort(V, axis=0)                                     # NaN sort last
    lo = np.take_along_axis(S, np.maximum((k - 1) // 2, 0)[None], axis=0)[0]
    hi = np.take_along_axis(S, np.maximum(k // 2, 0)[None], axis=0)[0]
    return np.where(k > 0, (lo + hi) / 2, np.nan)


def loo_effect(M, slot, drug, use, clean=None, min_wells=T.MIN_SLOT_WELLS):
    """Leave-drug-out well-position effect for every column: for each well, the median of the `use` wells in the
    same position (any plate) that hold a different drug (the donors). With `clean` (wells x columns, bool) only the
    donors that are clean for that column count. A column needs >= min_wells donors with a value, else its effect
    is 0. Returns eff, donors per well (n_total) and donors used per well x column (n_ok). Wells of the same drug at
    the same position share their donors, so each (position, drug) is computed once."""
    M = np.asarray(M)
    eff = np.zeros(M.shape, dtype=np.float32)
    n_ok = np.zeros(M.shape, dtype=np.int16)
    n_total = np.zeros(M.shape[0], dtype=int)
    slot = np.asarray(slot, dtype=float)
    drug = np.asarray(drug, dtype=object)
    use = np.asarray(use, dtype=bool)
    at_slot, by = defaultdict(list), defaultdict(list)
    for i, (s, d) in enumerate(zip(slot, drug)):
        if np.isfinite(s):
            at_slot[s].append(i)
            by[(s, d)].append(i)
    for (s, d), ii in by.items():
        jj = np.asarray(at_slot[s])
        m = jj[use[jj] & (drug[jj] != d)]
        n_total[ii] = m.size
        if m.size < min_wells:
            continue
        V = np.asarray(M[m], dtype=np.float32)
        ok = np.isfinite(V) if clean is None else np.isfinite(V) & np.asarray(clean[m], dtype=bool)
        k = ok.sum(axis=0)
        v = nanmedian0(np.where(ok, V, np.nan))
        eff[ii] = np.where(k >= min_wells, v, 0.0)
        n_ok[ii] = k
    return eff, n_total, n_ok


def loo_matrix(M, slot, drug, use, min_wells=T.MIN_SLOT_WELLS):
    """Leave-drug-out well-position effect with all other-drug donors (loo_effect without the clean rule)."""
    eff, n_total, _ = loo_effect(M, slot, drug, use, min_wells=min_wells)
    return eff, n_total


def plate_groups(w, drug, min_wells=PLATE_SCALE_MIN_WELLS):
    """Groups for the per-plate z scale: one per (plate, dose); a group with < min_wells drug wells (a control-dose
    well on another dose's plate, the DMSO wells) joins its plate's largest group. Returns the group of every well
    (-1: none) and one row per (plate, dose) present: plate, dose, conc, n_wells (drug wells), group (the index of
    the group it uses)."""
    t = pd.DataFrame({"plate": w["plate"].astype(str).to_numpy(), "dose": w["dose"].astype(str).to_numpy(),
                      "conc": pd.to_numeric(w["conc"], errors="coerce").to_numpy(), "drug": np.asarray(drug, bool)})
    n = t[t["drug"]].groupby(["plate", "dose"]).size()
    keys = [k for k, v in n.items() if v >= min_wells]
    for p in t["plate"].unique():                     # a plate without a big group: its largest one
        sub = n[n.index.get_level_values(0) == p]
        if len(sub) and not any(k[0] == p for k in keys):
            keys.append(sub.idxmax())
    gi = {k: i for i, k in enumerate(keys)}
    largest = {}
    for k in keys:
        if k[0] not in largest or n.get(k, 0) > n.get(largest[k[0]], 0):
            largest[k[0]] = k
    rows = []
    for (p, d), g in t.groupby(["plate", "dose"], sort=True):
        k = (p, d) if (p, d) in gi else largest.get(p)
        rows.append({"plate": p, "dose": d, "conc": g["conc"].iloc[0], "n_wells": int(g["drug"].sum()),
                     "group": gi[k] if k is not None else -1})
    tab = pd.DataFrame(rows)
    idx = {(r.plate, r.dose): r.group for r in tab.itertuples()}
    grp = np.array([idx.get((p, d), -1) for p, d in zip(t["plate"], t["dose"])], dtype=int)
    return grp, tab, keys


def plate_factors(W2, c, drug, grp, keys, reliable_plates, cols):
    """Per-group spread factor: mad of the group's drug wells around the gene's centre (1.4826 x median |W2 - c|)
    over the median mad of the same-dose groups on the OTHER reliable plates (its peers), median over the genes
    `cols`. factor = max(1, raw): a noisy plate is only ever widened, a quiet one never narrowed. No peers: 1.
    Also returns every column's own ratio (groups x columns, NaN without peers; T.feature_factors)."""
    G, K = len(keys), W2.shape[1]
    mad = np.full((G, K), np.nan)
    for g in range(G):
        rows = np.flatnonzero(drug & (grp == g))
        if rows.size:
            mad[g] = 1.4826 * nanmedian0(np.abs(np.asarray(W2[rows], dtype=np.float64) - c))
    raw, fac, npeer = np.full(G, np.nan), np.ones(G), np.zeros(G, dtype=int)
    ratios = np.full((G, K), np.nan)
    for g, (p, d) in enumerate(keys):
        peers = [h for h, (p2, d2) in enumerate(keys) if d2 == d and p2 != p and p2 in reliable_plates]
        npeer[g] = len(peers)
        if not peers:
            continue
        ref = nanmedian0(mad[peers])
        ratios[g] = mad[g] / np.where(ref > 0, ref, np.nan)
        ratio = ratios[g, cols]
        ratio = ratio[np.isfinite(ratio)]
        if ratio.size:
            raw[g] = float(np.median(ratio))
            fac[g] = max(1.0, raw[g])
    return raw, fac, npeer, ratios


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


def _num(row, key, default=0.0):
    """row[key] as a float; missing, empty or NaN -> default."""
    try:
        v = float(row.get(key, default))
    except (TypeError, ValueError):
        return default
    return v if math.isfinite(v) else default


def _true(row, key):
    v = row.get(key, False)
    return str(v).strip().lower() in ("true", "1", "1.0") if isinstance(v, str) else bool(v) and v == v


def flags_for(row):
    """The drug-dose flags (one definition with tahoe_mtap_gankyrin.flag_row; the strings are exact).
    row_* = median of the other drug wells in the same plate row (A-H) of the plate; drug-dose values = mean over
    the used wells. 'toxic' = T.is_toxic: cells_log2_best_well = the best used well's cell loss beyond a shifted
    plate row (T.cells_beyond_row), cells_log2_best_higher_dose = the best cell count of the same drug at a higher
    dose (NaN: none)."""
    f = []
    cells, rc = _num(row, "cells_log2_vs_plate"), _num(row, "row_cells_log2")
    if cells < -1:       # replicated cell loss beyond a shifted plate row, not undone at a higher dose = toxic
        higher = _num(row, "cells_log2_best_higher_dose", -np.inf)
        f.append("toxic" if T.is_toxic(cells, rc, _num(row, "cells_log2_best_well", np.nan), higher >= -1)
                 else "low cells (technical?)")
    if abs(rc) > T.ROW_SHIFT or _num(row, "row_umi_per_cell_log2") < -0.4:
        f.append("plate-row cell shift")
    gp, gr = _num(row, "genes_per_cell_log2_vs_plate"), _num(row, "row_genes_per_cell_log2")
    up, ur = _num(row, "umi_per_cell_log2_vs_plate"), _num(row, "row_umi_per_cell_log2")
    if (gp < -0.3 and gp - gr < -0.3) or (up < -0.5 and up - ur < -0.5):
        f.append("transcription drop")
    if any(abs(_num(row, f"{m}_lfc")) > 0.5 or (abs(_num(row, f"{m}_lfc")) > 0.25 and abs(_num(row, f"{m}_z")) >= 4)
           for m in ("S_PHASE", "G2M_PHASE")):
        f.append("cell-cycle shift")
    if abs(_num(row, "composition_shift_log2")) >= COMPOSITION_FLAG:
        f.append("composition shift")
    if max(_num(row, "plate_scale", 1.0), _num(row, "plate_scale_gene", 1.0)) > PLATE_SCALE_FLAG:
        f.append("noisy plate (z scaled)")
    if _true(row, "unreliable_plate_only"):
        f.append("unreliable plate only")
    if _true(row, "position_not_correctable"):
        f.append("position not correctable")
    if _num(row, "n_wells") >= 2 and _num(row, "n_sig_genes") >= DISAGREE_MIN_SIG and \
            _num(row, "replicate_r", 1.0) < DISAGREE_R:
        f.append("wells disagree")
    return "; ".join(f)


def gene_flags(base, posunc=False, poseff=0.0, notcorr=False, pscale=1.0):
    """Per-gene flags of a drug-dose: its drug-dose flags plus the position flags of that gene ('position not
    correctable' is already among the drug-dose flags when any used well had no position correction) and 'noisy
    plate (z scaled)' when the gene's own plate factor (pscale) is > PLATE_SCALE_FLAG."""
    f = [x for x in str(base or "").split("; ") if x]
    if np.isfinite(pscale) and pscale > PLATE_SCALE_FLAG and "noisy plate (z scaled)" not in f:
        nxt = [i for i, x in enumerate(f) if x in ("unreliable plate only", "position not correctable",
                                                     "wells disagree")]
        f.insert(nxt[0] if nxt else len(f), "noisy plate (z scaled)")
    if notcorr and "position not correctable" not in f:
        f.append("position not correctable")
    if posunc:
        f.append("position correction uncertain")
    if np.isfinite(poseff) and abs(poseff) > 0.2:
        f.append("position effect removed")
    return "; ".join(f)


def has_artifact(flags):
    """True when a flags string holds one of ARTIFACT_FLAGS."""
    fl = set(str(flags or "").split("; "))
    return any(a in fl for a in ARTIFACT_FLAGS)


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


def composition_shift(r1, comp_mask, min_genes=COMP_MIN_GENES):
    """Composition (library-size) shift of every profile (well x line): the median, over the genes the line
    expresses at >= COMP_MIN_CPM (comp_mask, lines x gene columns), of the profile's residual from the plate's median
    drug-well profile (median-of-ratios, as DESeq2's size factors). A drug that makes a few genes take a large share
    of the counts lowers every other gene's CPM by this much. < min_genes such genes (or no profile): 0."""
    W, L = r1.shape[:2]
    s = np.zeros((W, L), dtype=np.float32)
    for line in range(L):
        cols = np.flatnonzero(comp_mask[line])
        if cols.size < min_genes:
            continue
        X = r1[:, line, cols]
        k = np.isfinite(X).sum(axis=1)
        v = nanmedian0(X.T)
        s[:, line] = np.where(k >= min_genes, v, 0.0)
    return s


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


def unreliable_plates(spec, plates):
    """The plates whose wells stay out of pooled drug-doses, centres/scales and plate-factor peers
    (--unreliable-plates LIST|none; default UNRELIABLE_PLATES, those present in the data): one definition,
    tahoe_mtap_gankyrin.unreliable_plates (any case, plate numbers, 'none' / 'no')."""
    return T.unreliable_plates(pd.DataFrame({"plate": [str(p) for p in plates]}), spec)


def row_medians(ctx, well, drug):
    """Per well: the median of the OTHER drug wells in the same plate row (A-H) of the plate, for cells, UMIs and
    genes per cell (log2 vs plate). Recovery and depth shift by whole plate rows on some plates; 0 without a row."""
    rowl = pd.Series(list(well)).astype(str).str[:1].to_numpy()
    idx = np.arange(len(rowl))
    for c, name in (("cells_log2_vs_plate", "row_cells_log2"), ("umi_per_cell_log2_vs_plate", "row_umi_per_cell_log2"),
                    ("genes_per_cell_log2_vs_plate", "row_genes_per_cell_log2")):
        v = ctx[c].to_numpy(dtype=float)
        out = np.zeros(len(v))
        for i in idx:
            m = drug & (rowl == rowl[i]) & (idx != i) & np.isfinite(v)
            if rowl[i] and m.any():
                out[i] = float(np.median(v[m]))
        ctx[name] = out
    ctx["cells_log2_beyond_row"] = T.cells_beyond_row(ctx["cells_log2_vs_plate"], ctx["row_cells_log2"])


def best_higher_dose(dd):
    """Per drug-dose: the best (highest) cells_log2_vs_plate of the same drug at a higher dose (NaN: no higher dose)."""
    out = np.full(len(dd), np.nan)
    for _, g in dd.groupby("drug"):
        conc, cells = g["conc"].to_numpy(dtype=float), g["cells_log2_vs_plate"].to_numpy(dtype=float)
        for i, c in zip(g.index, conc):
            h = cells[conc > c]
            h = h[np.isfinite(h)]
            if h.size:
                out[i] = h.max()
    return out


def replicate_r(Z, used_of, DD_z, gK, top=DISAGREE_TOP):
    """Per drug-dose with >= 2 used wells: mean pairwise Pearson r of the wells' z over its top genes by |z|."""
    out = np.full(len(used_of), np.nan)
    for d, ii in enumerate(used_of):
        if len(ii) < 2:
            continue
        zz = np.abs(np.asarray(DD_z[d, :gK], dtype=float))
        fin = np.flatnonzero(np.isfinite(zz))
        cols = fin[np.argsort(-zz[fin])[:top]]
        X = np.asarray(Z[ii][:, cols], dtype=np.float64)
        rs = []
        for a in range(len(ii)):
            for b in range(a + 1, len(ii)):
                ok = np.isfinite(X[a]) & np.isfinite(X[b])
                if ok.sum() >= 10 and X[a, ok].std() > 0 and X[b, ok].std() > 0:
                    rs.append(float(np.corrcoef(X[a, ok], X[b, ok])[0, 1]))
        if rs:
            out[d] = float(np.mean(rs))
    return out


def update_info(out, **kv):
    """Merge keys into effects/info.json (min_cells etc. are written there first)."""
    p = os.path.join(out, "effects", "info.json")
    try:
        with open(p, encoding="utf-8") as fh:
            info = json.load(fh)
    except (OSError, ValueError):
        info = {}
    info.update(kv)
    with open(p, "w", encoding="utf-8") as fh:
        json.dump(info, fh, indent=1)


def cmd_effects(args):
    quiet()
    D = dirs(args.out)
    for f in (os.path.join(D["fx"], "complete.json"),    # not complete until this run writes it again at the end,
              os.path.join(args.out, "atlas_bundle.zip")):  # and no bundle of the earlier numbers to upload
        try:
            os.remove(f)
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
    unreliable = unreliable_plates(getattr(args, "unreliable_plates", None), sm["plate"].unique())
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

    # composition normalisation: genes each line expresses well (>= COMP_MIN_CPM) give the profile's size factor
    comp_mask = expr_mask[:, :gK] & (line_cpm[:, :gK] >= COMP_MIN_CPM)
    log(f"Pass 2: corrected effects plate by plate (composition shift per profile from "
        f"{int(np.median(comp_mask.sum(1))):,} genes per line at >= {COMP_MIN_CPM:g} CPM) ...")
    plates = sorted(sm["plate"].unique(), key=lambda p: (len(p), p))
    W1s, ctxs, As, VAs, R1m, offsets, wells_all, Ss, comp_rows = [], [], [], [], [], [], [], [], []
    usable = np.zeros(L, dtype=int)
    mod_idx = [gK + j for j in range(len(modules))]
    for p in plates:
        smp_ = sm[sm["plate"] == p].reset_index(drop=True)
        wells = list(smp_["sample"])
        counts, tot, nc, ng, r1, base = plate_residuals(prof, smp_, lines, keep, modules, expr_mask)
        drug = ~smp_["is_dmso"].to_numpy()
        shift = composition_shift(r1, comp_mask)
        r1 -= shift[:, :, None]                     # r1c: every gene (and module) relative to the profile's shift
        ok = nc >= MIN_CELLS
        usable += ok.sum(axis=0)
        wi, lj = np.nonzero(ok)
        comp_rows.append(pd.DataFrame({"sample": np.asarray(wells, dtype=object)[wi],
                                       "cell_line_id": np.asarray(lines, dtype=object)[lj],
                                       "shift_log2": shift[wi, lj].astype(np.float32)}))
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
        row_medians(ctx, smp_["well"], drug)
        ctx["composition_shift_log2"] = np.nanmedian(np.where(ok, shift, np.nan), axis=1)
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
        Ss.append(shift)
        wells_all.append(smp_)
        log(f"  {p}: {len(wells)} wells; median composition shift {np.nanmedian(ctx['composition_shift_log2']):+.3f} "
            f"(largest |shift| {np.nanmax(np.abs(ctx['composition_shift_log2'])):.2f})")
        del counts, r1
    W1 = np.concatenate(W1s)
    del W1s
    A = np.concatenate(As)
    VA = np.concatenate(VAs)
    r1m = np.concatenate(R1m)
    S = np.concatenate(Ss)
    wells_df = pd.concat(wells_all, ignore_index=True).merge(pd.concat(ctxs), on="sample", how="left")
    N = len(wells_df)
    drug = ~wells_df["is_dmso"].to_numpy()
    slot = wells_df["slot"].to_numpy(dtype=float)
    dname = wells_df["drug"].to_numpy(dtype=object)
    reliable = ~wells_df["plate"].isin(unreliable).to_numpy()
    wells_df["unreliable_plate"] = ~reliable
    ref = drug & reliable if (drug & reliable).any() else drug       # wells that set each gene's centre and scale
    grp, gtab, gkeys = plate_groups(wells_df, drug)
    rel_plates = set(wells_df["plate"]) - set(unreliable)
    gcols = np.arange(gK)

    def per_well(fac):
        return np.where(grp >= 0, fac[np.maximum(grp, 0)], 1.0).astype(np.float32)

    if unreliable:
        log(f"Unreliable plates (kept out of pooled drug-doses, centres and plate-factor peers): {', '.join(unreliable)}")
    log("Well-position correction, pass 1 (leave-drug-out: all other drugs at the same position) ...")
    slot_med = np.full((96, K), np.nan, dtype=np.float32)    # what every drug placed at a position shows there
    for sl in range(1, 97):
        rows = np.flatnonzero((slot == sl) & drug)
        if rows.size:
            slot_med[sl - 1] = np.nanmedian(W1[rows], axis=0)
    eff, n_total, _ = loo_effect(W1, slot, dname, drug)
    W2 = W1 - eff
    c, s = robust_cols(W2, ref)
    raw1, fac1, _, _ = plate_factors(W2, c, drug, grp, gkeys, rel_plates, gcols)
    f1 = per_well(fac1)
    clean = np.abs((W2 - c) / (s * f1[:, None])) < POS_CLEAN_Z
    log(f"  pass 2: clean donors only (|pass-1 z| < {POS_CLEAN_Z:g} for that gene) ...")
    eff, _, n_clean = loo_effect(W1, slot, dname, drug, clean=clean)
    del clean
    W2 = W1 - eff
    c, s = robust_cols(W2, ref)
    raw2, fac2, npeer, ratio2 = plate_factors(W2, c, drug, grp, gkeys, rel_plates, gcols)
    fw = per_well(fac2)
    # each gene's z divisor per group: the group factor, more where the gene alone is noisier there (T.feature_factors)
    FG = np.vstack([T.feature_factors(np.full(K, fac2[g]), ratio2[g]) for g in range(len(gkeys))]).astype(np.float32) \
        if len(gkeys) else np.ones((0, K), dtype=np.float32)
    Z = ((W2 - c) / s).astype(np.float32)
    for g in range(len(gkeys)):
        rows = np.flatnonzero(grp == g)
        Z[rows] /= FG[g][None, :]
    log(f"  gene-specific plate factors: {int((FG > fac2[:, None] * 1.0001).sum()):,} group x gene values widened "
        f"beyond their group (own spread ratio > {PLATE_SCALE_BAND:g} x the group factor)")
    notcorr = n_total < T.MIN_SLOT_WELLS
    posunc = (~notcorr)[:, None] & (n_clean < T.MIN_SLOT_WELLS) & np.isfinite(W1)
    wells_df["position_wells_used"] = n_total
    wells_df["position_clean_donors_median"] = np.median(n_clean[:, :gK], axis=1) if gK else 0.0
    wells_df["position_not_correctable"] = notcorr
    wells_df["plate_scale_group"] = [f"{gkeys[g][0]} {gkeys[g][1]}" if g >= 0 else "" for g in grp]
    wells_df["plate_scale_group_id"] = grp            # row of plate_scale_gene.npy (-1: none, factor 1)
    wells_df["plate_scale_pass1"] = f1
    wells_df["plate_scale"] = fw
    r2m = r1m - eff[:, None, mod_idx]
    gt = gtab.copy()
    gg = gt["group"].to_numpy()

    def pick(arr, dflt):
        return [float(arr[g]) if g >= 0 else dflt for g in gg]

    gt["factor_raw"], gt["factor"] = pick(raw2, np.nan), pick(fac2, 1.0)
    gt["group_n_wells"] = [int(gt.loc[gt["group"] == g, "n_wells"].sum()) if g >= 0 else 0 for g in gg]
    gt["n_peer_groups"] = [int(npeer[g]) if g >= 0 else 0 for g in gg]
    gt["factor_raw_pass1"], gt["factor_pass1"] = pick(raw1, np.nan), pick(fac1, 1.0)
    gt["unreliable_plate"] = gt["plate"].isin(unreliable)
    gt["group"] = [f"{gkeys[g][0]} {gkeys[g][1]}" if g >= 0 else "" for g in gg]
    order = {p: i for i, p in enumerate(plates)}
    gt = gt.assign(_o=gt["plate"].map(order)).sort_values(["_o", "conc"]).drop(columns="_o")
    plate_scale = gt[["plate", "dose", "n_wells", "factor_raw", "factor", "conc", "group", "group_n_wells",
                      "n_peer_groups", "factor_raw_pass1", "factor_pass1", "unreliable_plate"]]
    wide = plate_scale[plate_scale["factor"] > PLATE_SCALE_FLAG].drop_duplicates("group")
    log("  plate factors (z widened on noisy plates): "
        + (", ".join(f"{r.group} {r.factor:.2f}x" for r in wide.itertuples()) or f"none above {PLATE_SCALE_FLAG:g}")
        + f"; wells with no position correction (< {T.MIN_SLOT_WELLS} other-drug wells at the position): "
          f"{int((notcorr & drug).sum())} drug wells; correction uncertain for "
          f"{100 * posunc[drug][:, :gK].mean():.2f}% of drug-well x gene values")

    log("Growth (relative abundance) ...")
    effA, _ = loo_matrix(A, slot, dname, drug)
    A2 = A - effA
    cA, sA = robust_cols(A2, ref)
    cvar = np.nanmedian(VA[ref], axis=0)
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
    DD_posunc = np.zeros((Dn, K), dtype=bool)
    DD_poseff = np.zeros((Dn, K), dtype=np.float32)
    dd_of_well = np.full(N, -1)
    used = np.zeros(N, dtype=bool)
    used_of, rows_dd = [], []
    for d, key in enumerate(keys):
        ii_all = wd_idx[groups[key]]
        rel = reliable[ii_all]
        ii = ii_all[rel] if rel.any() else ii_all       # reliable wells only, unless there are none
        dd_of_well[ii_all] = d
        used[ii] = True
        used_of.append(ii)
        DD_lfc[d] = np.nanmean(W2[ii], axis=0)
        k = np.isfinite(Z[ii]).sum(axis=0)
        DD_z[d] = np.where(k > 0, np.nansum(Z[ii], axis=0) / np.sqrt(np.maximum(k, 1)), np.nan)
        DD_A[d] = np.nanmean(A2[ii], axis=0)
        kA = np.isfinite(zA[ii]).sum(axis=0)
        DD_Az[d] = np.where(kA > 0, np.nansum(zA[ii], axis=0) / np.sqrt(np.maximum(kA, 1)), np.nan)
        DD_r2m[d] = np.nanmean(r2m[ii], axis=0)
        DD_posunc[d] = posunc[ii].any(axis=0)
        DD_poseff[d] = np.nanmean(eff[ii], axis=0)
        w = wells_df.iloc[ii]
        left = wells_df.iloc[np.setdiff1d(ii_all, ii)]
        rows_dd.append({"drug": key[0], "dose": key[1], "conc": w["conc"].iloc[0], "n_wells": len(ii),
                        "n_wells_all": len(ii_all),
                        "wells": ",".join(sorted(set(w["well"].astype(str)))),
                        "plates": ",".join(sorted(set(w["plate"].astype(str)))),
                        "wells_left_out": ",".join(f"{a}:{b}" for a, b in zip(left["plate"], left["well"])),
                        "unreliable_plate_only": not rel.any(),
                        "cells_log2_vs_plate": w["cells_log2_vs_plate"].mean(),
                        "umi_per_cell_log2_vs_plate": w["umi_per_cell_log2_vs_plate"].mean(),
                        "genes_per_cell_log2_vs_plate": w["genes_per_cell_log2_vs_plate"].mean(),
                        "row_cells_log2": w["row_cells_log2"].mean(),
                        "row_umi_per_cell_log2": w["row_umi_per_cell_log2"].mean(),
                        "row_genes_per_cell_log2": w["row_genes_per_cell_log2"].mean(),
                        "composition_shift_log2": w["composition_shift_log2"].mean(),
                        "cells_log2_best_well": w["cells_log2_beyond_row"].max(),
                        "plate_scale": float(fw[ii].mean()),
                        "position_wells_used": float(n_total[ii].mean()),
                        "position_not_correctable": bool(notcorr[ii].any())})
    dd = pd.DataFrame(rows_dd)
    for j, name in enumerate(modules):
        dd[f"{name}_lfc"] = DD_lfc[:, gK + j]
        dd[f"{name}_z"] = DD_z[:, gK + j]
    dd["cells_log2_best_higher_dose"] = best_higher_dose(dd)
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
    dd["replicate_r"] = replicate_r(Z, used_of, DD_z, gK)
    dd.insert(int(dd.columns.get_loc("n_genes_up")), "flags", [flags_for(r) for _, r in dd.iterrows()])
    drugs_meta = T.load_drugs(idx)
    dd = dd.join(drugs_meta, on="drug")
    wells_df["drugdose_row"] = dd_of_well
    wells_df["used_in_drugdose"] = used
    nfl = {f: int(dd["flags"].str.contains(f, regex=False).sum()) for f in
           ("toxic", "low cells (technical?)", "plate-row cell shift", "composition shift", "noisy plate (z scaled)",
            "unreliable plate only", "position not correctable", "wells disagree")}
    log("  drug-doses flagged: " + ", ".join(f"{k} {v}" for k, v in nfl.items()))

    log("Pass 3: how strongly each cell line shows each drug's consensus response ...")
    sig = sig_up | sig_dn
    n_sig = sig.sum(axis=1)
    beta = np.full((N, L), np.nan, dtype=np.float32)
    rcor = np.full((N, L), np.nan, dtype=np.float32)
    off = 0
    for p in plates:
        smp_ = sm[sm["plate"] == p].reset_index(drop=True)
        Wp = len(smp_)
        todo = [j for j in range(Wp) if used[off + j] and n_sig[dd_of_well[off + j]] >= MIN_SIG_BETA]
        if todo:
            r1 = plate_residuals(prof, smp_, lines, keep, modules, expr_mask)[4]
            r1 -= S[off:off + Wp][:, :, None]
            for j in todo:
                d = dd_of_well[off + j]
                cols = np.flatnonzero(sig[d])
                X = r1[j][:, cols] - eff[off + j, cols][None, :]
                beta[off + j], rcor[off + j] = line_fit(X, DD_lfc[d, cols])
            del r1
        off += Wp
    DD_beta = np.full((Dn, L), np.nan, dtype=np.float32)
    DD_rcor = np.full((Dn, L), np.nan, dtype=np.float32)
    for d, ii in enumerate(used_of):
        DD_beta[d] = np.nanmean(beta[ii], axis=0)
        DD_rcor[d] = np.nanmean(rcor[ii], axis=0)

    genes_df = pd.DataFrame({"col": np.arange(K),
                             "kind": ["gene"] * gK + ["module"] * len(modules),
                             "token": list(keep) + [-1] * len(modules),
                             "symbol": list(symbols) + list(modules),
                             "label": list(labels) + list(modules),
                             "pooled_cpm": list(pooled[keep]) + list(np.median(line_cpm[:, gK:], axis=0)),
                             "median_line_cpm": med, "n_lines_expressing": expr_mask.sum(axis=0)})
    lines_df["wells_usable"] = usable
    lines_df["pct_wells_usable"] = 100.0 * usable / max(len(sm), 1)
    out = D["fx"]
    genes_df.to_csv(os.path.join(out, "genes.csv"), index=False)
    lines_df.to_csv(os.path.join(out, "lines.csv"), index=False)
    wells_df.to_csv(os.path.join(out, "wells.csv"), index=False)
    dd.to_csv(os.path.join(out, "drugdose.csv"), index=False)
    plate_scale.to_csv(os.path.join(out, "plate_scale.csv"), index=False)
    failed.to_csv(os.path.join(out, "failed_wells.csv"), index=False)
    pd.DataFrame({"plate": plates}).to_csv(os.path.join(out, "plates.csv"), index=False)
    comp = pd.concat(comp_rows, ignore_index=True)
    tmp = os.path.join(out, "composition_shift.parquet.tmp")
    comp.to_parquet(tmp, index=False)
    os.replace(tmp, os.path.join(out, "composition_shift.parquet"))
    for name, arr in [("W1", W1), ("W2", W2.astype(np.float32)), ("Z", Z), ("slot_median", slot_med),
                      ("plate_offset", np.vstack(offsets)), ("DD_lfc", DD_lfc), ("DD_z", DD_z),
                      ("DD_qup", q_up), ("DD_qdn", q_dn), ("line_cpm", line_cpm), ("expr_mask", expr_mask),
                      ("posunc", posunc), ("DD_posunc", DD_posunc), ("DD_poseff", DD_poseff),
                      ("plate_scale_gene", FG),
                      ("A2", A2.astype(np.float32)), ("zA", zA), ("VA", VA), ("DD_A", DD_A), ("DD_Az", DD_Az),
                      ("r2_modules", r2m.astype(np.float32)), ("DD_r2_modules", DD_r2m),
                      ("beta", beta), ("rcor", rcor), ("DD_beta", DD_beta), ("DD_rcor", DD_rcor)]:
        save_npy(os.path.join(out, f"{name}.npy"), arr)
    with open(os.path.join(out, "modules.json"), "w", encoding="utf-8") as fh:
        json.dump({k: [int(t) for t in v] for k, v in modules.items()}, fh)
    with open(os.path.join(out, "README_effects.md"), "w", encoding="utf-8") as fh:
        fh.write(EFFECTS_README)
    update_info(args.out, unreliable_plates=unreliable, comp_min_cpm=COMP_MIN_CPM, comp_min_genes=COMP_MIN_GENES,
                pos_clean_z=POS_CLEAN_Z, plate_scale_min_wells=PLATE_SCALE_MIN_WELLS, method_version=EFFECTS_VERSION)
    with open(os.path.join(out, "complete.json"), "w", encoding="utf-8") as fh:
        json.dump({"version": EFFECTS_VERSION, "unreliable_plates": unreliable}, fh)
    log(f"Effects done: {gK:,} genes x {Dn:,} drug-doses x {L} lines -> {out}")


EFFECTS_README = """# effects/ - what each file holds (load .npy with numpy.load(path, mmap_mode='r'))
Method v3 (complete.json version 3): composition shift per profile, per-plate z scale, unreliable plates kept out of
pooled drug-doses, two-pass (clean-donor) well-position correction. info.json names the unreliable plates.
genes.csv      one row per COLUMN of the gene matrices: col, kind (gene/module), token, symbol, label, pooled_cpm,
               median_line_cpm, n_lines_expressing. Modules S_PHASE, G2M_PHASE, PROTEASOME are summed gene sets.
lines.csv      one row per cell line (row order = columns of the line matrices): id, cell_name, Organ, drivers,
               driver_changes (protein changes), n_cells_total, in_growth_analysis, wells_usable / pct_wells_usable
               (wells with >= min_cells cells of the line, i.e. usable expression).
wells.csv      one row per well used (row order = rows of W1/W2/Z/A2/zA/beta): sample, plate, well, slot, drug, conc,
               dose, is_dmso, cells and per-cell UMI/gene counts vs plate (log2), row_cells_log2 / row_umi_per_cell_log2
               / row_genes_per_cell_log2 (median of the other drug wells in the same plate row), cells_log2_beyond_row
               (cell loss beyond the row where the row itself moved > 0.8 log2, else the plain value),
               composition_shift_log2 (median over the well's lines), unreliable_plate, plate_scale_group /
               plate_scale_group_id (row of plate_scale_gene.npy) / plate_scale (the group's factor; pass 1:
               plate_scale_pass1), position_wells_used (other-drug wells at the position), position_clean_donors_median,
               position_not_correctable (< 3 of them), drugdose_row (row of drugdose.csv; -1 none), used_in_drugdose.
drugdose.csv   one row per drug and dose (row order = rows of DD_*): n_wells (used wells: those on reliable plates, or
               all when the drug-dose sits only on unreliable plates), n_wells_all, wells, plates, wells_left_out, cell
               loss, transcription and their plate-row medians, cells_log2_best_well (the largest
               cells_log2_beyond_row of the used wells: 'toxic' needs it < -0.5), composition_shift_log2, plate_scale
               (mean group factor of the used wells), position_wells_used (mean over the used wells, as
               tahoe_mtap_gankyrin.py), position flags,
               module shifts, cells_log2_best_higher_dose, flags, n_genes_up/down (q < 0.1 and >= 1.2x), replicate_r
               (mean pairwise r of the used wells' z over the top 500 genes), targets, moa_fine, moa_broad.
composition_shift.parquet  sample, cell_line_id, shift_log2: each profile's composition (library-size) shift, the
               median residual of the genes the line expresses at >= 10 CPM (subtracted from every gene and module).
plate_scale.csv one row per plate and dose: n_wells (drug wells), factor_raw / factor (z divisor = max(1, raw): the
               group's spread over that of the same dose on the other reliable plates, median over genes), group (the
               plate-and-dose group it uses; small groups join the plate's largest), the pass-1 factors.
plate_scale_gene.npy groups (wells.csv plate_scale_group_id) x genes: each gene's z divisor in that group = max(group
               factor, the gene's own spread ratio / 1.3): a gene noisier on one plate than the group's median gene is
               widened further (never narrowed). The 'noisy plate (z scaled)' flag of a gene uses it.
W1.npy, W2.npy wells x genes: log2 effect before / after the well-position correction (median over cell lines).
Z.npy          wells x genes: W2 scored against the spread of drug wells (robust z), divided by the gene's plate
               factor (plate_scale_gene.npy).
posunc.npy     wells x genes (bool): position correction uncertain (fewer than 3 clean other-drug wells at the
               position for that gene: not corrected). DD_posunc.npy: the same per drug-dose (any used well).
DD_poseff.npy  drug-doses x genes: position effect removed (mean over the used wells, log2).
DD_lfc.npy     drug-doses x genes: corrected log2 fold change (mean over the drug-dose's used wells). fold = 2**lfc.
DD_z.npy       drug-doses x genes: combined z (Stouffer over the drug-dose's used wells).
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


class FX:
    """Lazy access to the effects."""

    def __init__(self, out):
        self.out = out
        self.d = os.path.join(out, "effects")
        if not effects_ready(out):
            sys.exit("effects missing, incomplete or from an older version of tahoe_atlas.py; "
                     "run 'compute' (or 'effects') again")
        global MIN_CELLS
        self.info = {}
        try:
            with open(os.path.join(self.d, "info.json"), encoding="utf-8") as fh:
                self.info = json.load(fh)
            MIN_CELLS = self.info["min_cells"]
        except (OSError, KeyError, ValueError):
            pass
        self.unreliable = list(self.info.get("unreliable_plates", []))
        self.genes = pd.read_csv(os.path.join(self.d, "genes.csv"))
        self.lines = pd.read_csv(os.path.join(self.d, "lines.csv"), dtype={"cell_line_id": str})
        self.wells = pd.read_csv(os.path.join(self.d, "wells.csv"),
                                 dtype={"sample": str, "plate": str, "drug": str, "dose": str,
                                        "plate_scale_group": str})
        self.dd = pd.read_csv(os.path.join(self.d, "drugdose.csv"), dtype={"drug": str, "dose": str})
        for c in ("flags", "moa_fine", "moa_broad", "targets", "wells_left_out"):
            if c in self.dd:
                self.dd[c] = self.dd[c].fillna("").astype(str)
            else:
                self.dd[c] = ""
        for c in ("unreliable_plate_only", "position_not_correctable"):
            self.dd[c] = self.dd[c].astype(str).str.lower().eq("true") if c in self.dd else False
        w = self.wells

        def wbool(c, default):
            return w[c].astype(str).str.lower().eq("true").to_numpy() if c in w else default
        drug_w = ~w["is_dmso"].astype(bool).to_numpy()
        self.reliable_w = ~wbool("unreliable_plate", np.zeros(len(w), dtype=bool))
        self.used_w = wbool("used_in_drugdose", drug_w.copy())
        self.ref_w = drug_w & self.reliable_w if (drug_w & self.reliable_w).any() else drug_w   # centre / scale
        ddr = w["drugdose_row"].to_numpy() if "drugdose_row" in w else np.full(len(w), -1)
        self.wells_of_dd = {int(d): np.flatnonzero((ddr == d) & self.used_w) for d in np.unique(ddr[ddr >= 0])}
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

    def gene_scale(self, cols, rows=None):
        """Per well (or `rows` of fx.wells) x column of `cols`: the z divisor (plate_scale_gene.npy row of the
        well's plate group: its factor, more where the gene alone is noisier on that plate; 1 without a group)."""
        w = self.wells
        rows = np.arange(len(w)) if rows is None else np.asarray(rows)
        cols = np.atleast_1d(np.asarray(cols, dtype=int))
        if "plate_scale_group_id" not in w or not os.path.exists(os.path.join(self.d, "plate_scale_gene.npy")):
            f = w["plate_scale"].to_numpy(dtype=float)[rows] if "plate_scale" in w else np.ones(rows.size)
            return np.repeat(f[:, None], cols.size, axis=1)
        gid = w["plate_scale_group_id"].to_numpy(dtype=int)[rows]
        FG = np.asarray(self.plate_scale_gene)[:, cols]
        out = np.ones((rows.size, cols.size), dtype=np.float32)
        ok = gid >= 0
        out[ok] = FG[gid[ok]]
        return out

    def gene_plate_scale(self, c):
        """Per drug-dose: the mean z divisor of gene column c over its used wells (T: plate_scale_gene)."""
        f = self.gene_scale([c])[:, 0]
        out = np.ones(len(self.dd))
        for d, ii in self.wells_of_dd.items():
            if len(ii):
                out[d] = float(np.mean(f[ii]))
        return out

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


def position_flag(fx, c):
    """Per drug-dose, for gene column c: 'not correctable' (a used well had < 3 other-drug wells at its position),
    'uncertain' (< 3 clean ones for this gene: not corrected), else the position effect removed when > 1.15x."""
    unc = np.asarray(fx.DD_posunc)[:, c] if hasattr(fx, "DD_posunc") else np.zeros(len(fx.dd), bool)
    pe = np.asarray(fx.DD_poseff)[:, c] if hasattr(fx, "DD_poseff") else np.zeros(len(fx.dd))
    nc = fx.dd["position_not_correctable"].to_numpy(dtype=bool)
    return ["not correctable" if a else "uncertain" if b else (f"removed {2 ** e:.2f}x" if abs(e) > 0.2 else "")
            for a, b, e in zip(nc, unc, pe)]


def gene_flag_col(fx, c, rows=None):
    """The per-gene flags of every drug-dose (or of `rows`) for gene column c: drug-dose flags + position flags +
    'noisy plate (z scaled)' from the gene's own plate factor."""
    rows = np.arange(len(fx.dd)) if rows is None else np.asarray(rows)
    unc = np.asarray(fx.DD_posunc)[rows, c] if hasattr(fx, "DD_posunc") else np.zeros(rows.size, bool)
    pe = np.asarray(fx.DD_poseff)[rows, c] if hasattr(fx, "DD_poseff") else np.zeros(rows.size)
    ps = fx.gene_plate_scale(c)[rows]
    base = fx.dd["flags"].to_numpy()[rows]
    return [gene_flags(b, u, e, pscale=f) for b, u, e, f in zip(base, unc, pe, ps)]


def signif(fx):
    q_up, q_dn, lfc = np.asarray(fx.DD_qup), np.asarray(fx.DD_qdn), np.asarray(fx.DD_lfc)
    up = (q_up < Q_CUT) & (lfc >= LFC_MIN)
    dn = (q_dn < Q_CUT) & (lfc <= -LFC_MIN)
    up[:, ~fx.gmask] = False
    dn[:, ~fx.gmask] = False
    return up, dn


def drug_best_dose(fx):
    """Row of each drug's strongest dose (most significant genes; ties -> higher dose)."""
    t = fx.dd[["drug", "conc", "n_sig_genes"]].copy()
    best = t.sort_values(["drug", "n_sig_genes", "conc"], ascending=[True, False, False]).drop_duplicates("drug")
    return best.index.to_numpy()
