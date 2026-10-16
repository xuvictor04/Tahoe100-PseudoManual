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

Method v3 (effects): composition (library-size) normalisation per profile, per-plate z scale, unreliable plates
         kept out of pooled drug-doses (--unreliable-plates plate13 by default when present, or 'none'), two-pass
         well-position correction with clean donors; flags explained in every brief.
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
import textwrap
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
if not all(hasattr(T, f) for f in ("start_run_log", "keep_awake", "py_cmd", "REINDEX_HINT", "unreliable_plates",
                                    "cells_beyond_row", "feature_factors", "salt_base", "is_toxic")) or \
        getattr(T, "METHOD_VERSION", 0) < 3:
    sys.exit("tahoe_mtap_gankyrin.py next to tahoe_atlas.py is an older version: copy the current one over it "
             "(the atlas needs its method v3)")

log = T.log

# ----------------------------------------------------------------------------- settings
MIN_CELLS = 30             # cells of one line in one well needed to use its expression
MIN_LINES = getattr(T, "MIN_LINES", 5)   # lines needed for a well-level effect (one definition with T)
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
EFFECTS_VERSION = 3        # effects/complete.json: written last by 'effects'; angles, agents and lookups need it
# method v3 (one definition with tahoe_mtap_gankyrin.py; T's own constants win when it defines them)
COMP_MIN_CPM = getattr(T, "COMP_MIN_CPM", 10.0)    # composition shift: genes the line expresses at >= this CPM ...
COMP_MIN_GENES = getattr(T, "COMP_MIN_GENES", 200)  # ... at least this many per profile, else no shift (0)
COMPOSITION_FLAG = getattr(T, "COMPOSITION_FLAG", 0.2)          # |drug-dose composition shift| (log2) flagged
PLATE_SCALE_MIN_WELLS = getattr(T, "PLATE_SCALE_MIN_WELLS", 20)  # smaller (plate, dose) groups join the plate's largest
PLATE_SCALE_FLAG = T.NOISY_PLATE                  # drug-doses (or genes) on plates widened more than this: flagged
PLATE_SCALE_BAND = T.PLATE_SCALE_BAND             # a gene's own spread ratio / this widens it beyond its group
POS_CLEAN_Z = getattr(T, "POS_CLEAN_Z", 3.0)       # pass-2 position donors: |pass-1 z| below this for that gene
UNRELIABLE_PLATES = tuple(getattr(T, "UNRELIABLE_PLATES", ("plate13",)))   # default of --unreliable-plates
DISAGREE_R, DISAGREE_MIN_SIG, DISAGREE_TOP = 0.1, 100, 500   # 'wells disagree': r < 0.1 over the top 500 genes
NOISE_RNA_RE = re.compile(r"^(7SK|RN7SK|RNU|SNOR|SCARNA|MT-|MTND|MTCO|MTATP|MTCY|RP[LS]\d+[A-Z]*P\d|H1-\d|H[2-4]C\d|"
                          r"H2[AB]C\d|ENSG)")       # RULEBOOK rule 7: incl. H1-* histones, RPL13AP5-style pseudogenes
# flags that make a drug-dose (or a gene in it) unfit as a 'clean' inducer / repressor in the gene lists
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


_BRIEF = {"notes": None}          # facts of this run for the briefs (cmd_angles fills it once from the effects)


def write_brief(folder, title, task, files, extra=""):
    notes = _BRIEF["notes"] or {}
    with open(os.path.join(folder, "brief.md"), "w", encoding="utf-8") as fh:
        fh.write(f"# Angle: {title}\n\n## Your task\n{task.strip()}\n\n## Data in this folder\n")
        for name, desc in files:
            fh.write(f"- `{name}`: {desc}\n")
        fh.write("\n" + methods_text(notes) + "\n" + rulebook_text(notes) + "\n" + extra + "\n" + REPORT_RULES
                 + f"\n_Written by {os.path.abspath(__file__)} ('angles' step; method v{EFFECTS_VERSION})._\n")


def _join(items, n=8):
    items = list(items)
    return ", ".join(items[:n]) + (f" and {len(items) - n} more" if len(items) > n else "")


def replicate_pairs(fx):
    """Every pair of wells of one drug-dose (all its wells, also those on unreliable plates): r of their genome-wide
    W2 signatures (responsive genes, centred) and the pair type; and two nulls over wells on reliable plates: random
    pairs of different drugs on different plates, and such pairs at the SAME well position (which share the position
    artifact). Cached on fx."""
    cached = fx.__dict__.get("_reps")
    if cached is not None:
        return cached
    Xn = unit_rows(np.asarray(fx.W2)[:, responsive_genes(fx)])
    Xn = unit_rows(Xn - Xn.mean(axis=1, keepdims=True))
    w = fx.wells
    plate, slot = w["plate"].astype(str).to_numpy(), w["slot"].to_numpy(dtype=float)
    unrel = ~fx.reliable_w
    nc = w["position_not_correctable"].astype(str).str.lower().eq("true").to_numpy() \
        if "position_not_correctable" in w else np.zeros(len(w), dtype=bool)
    rows = []
    for (d, dose), gg in w[fx.drug_w].groupby(["drug", "dose"]):
        ii = gg.index.to_numpy()
        for x in range(len(ii)):
            for y in range(x + 1, len(ii)):
                a, b = ii[x], ii[y]
                typ = ("unreliable plate" if unrel[a] or unrel[b] else "same plate" if plate[a] == plate[b] else
                       "same position, other plate" if slot[a] == slot[b] else "different position")
                rows.append((d, dose, a, b, typ, float(Xn[a] @ Xn[b]), bool(nc[a] or nc[b])))
    pairs = pd.DataFrame(rows, columns=["drug", "dose", "a", "b", "pair_type", "r", "position_not_correctable"])
    rng = np.random.default_rng(0)
    idx = np.flatnonzero(fx.drug_w & fx.reliable_w)
    drugs = w["drug"].to_numpy(dtype=object)
    nulls = []
    if idx.size >= 2:
        for _ in range(3000):
            a, b = rng.choice(idx, 2, replace=False)
            if drugs[a] != drugs[b] and plate[a] != plate[b]:
                nulls.append(float(Xn[a] @ Xn[b]))
    same = []
    for s in np.unique(slot[idx][np.isfinite(slot[idx])]):
        jj = idx[slot[idx] == s]
        for x in range(len(jj)):
            for y in range(x + 1, len(jj)):
                a, b = jj[x], jj[y]
                if drugs[a] != drugs[b] and plate[a] != plate[b]:
                    same.append((a, b))
    if len(same) > 3000:
        same = [same[i] for i in rng.choice(len(same), 3000, replace=False)]
    snull = np.array([float(Xn[a] @ Xn[b]) for a, b in same])
    fx.__dict__["_reps"] = (pairs, np.array(nulls), snull)
    return fx.__dict__["_reps"]


def brief_notes(fx):
    """Facts about this run that the briefs state (all from the data; never hard-coded numbers)."""
    n = {}
    w, dd = fx.wells, fx.dd
    n["genes"], n["drug_doses"], n["drugs"] = int(fx.gi.size), int(len(dd)), int(dd["drug"].nunique())
    n["plates"], n["lines"], n["wells"] = len(fx.plates), int(len(fx.lines)), int(len(w))
    conc = sorted(set(pd.to_numeric(dd["conc"], errors="coerce").dropna()))
    n["doses"] = ", ".join(f"{c:g}" for c in conc[:-1]) + (" and " if len(conc) > 1 else "") + \
        (f"{conc[-1]:g}" if conc else "")
    # DMSO positions per plate
    dm = w[~fx.drug_w]
    pos = dm.groupby("plate")["well"].apply(lambda s: "/".join(sorted(map(str, s), key=lambda x: T.slot_from_well(x)
                                                                       or 0)))
    if len(pos):
        vc = pos.value_counts()
        other = pos[pos != vc.index[0]]
        n["dmso"] = (f"{vc.index[0]} on every plate" if other.empty else
                     f"{vc.index[0]} ({vc.iloc[0]} plates; " + ", ".join(f"{p}: {v}" for p, v in other.items()) + ")")
    else:
        n["dmso"] = "no DMSO wells found"
    off = np.asarray(fx.plate_offset)[:, fx.gmask]
    k = (np.abs(off) > LFC_MIN).sum(axis=1)
    if k.size:
        o = np.argsort(-k)[:2]
        n["dmso_off"] = "; ".join(f"{fx.plates[i]} {int(k[i])} genes" for i in o)
    # plate factors, unreliable plates (with their replicate agreement)
    ps_path = os.path.join(fx.d, "plate_scale.csv")
    ps = pd.read_csv(ps_path, dtype={"dose": str, "group": str}) if os.path.exists(ps_path) else pd.DataFrame()
    if len(ps):                    # one row per group: its own (plate, dose) row, not a joined DMSO / control dose
        own = (ps["group"].astype(str) == ps["plate"].astype(str) + " " + ps["dose"].astype(str)).astype(int)
        ps = ps.assign(_own=own).sort_values("_own", ascending=False, kind="stable")
    wide = ps[ps["factor"] > PLATE_SCALE_FLAG].drop_duplicates("group") if len(ps) else ps
    n["wide"] = _join(f"{r.plate} ({float(r.conc):g} uM) {r.factor:.2f}x" for r in
                      wide.sort_values("factor", ascending=False).itertuples()) if len(wide) else ""
    pairs, _, _ = replicate_pairs(fx)
    # inert drug-doses agree at r ~0 on every plate: the pairs of active ones (>= 10 significant genes) tell more
    # (each drug-dose counted once: its mean r over its well pairs; T.replicate_summary)
    nsig = dict(zip(zip(dd["drug"], dd["dose"].astype(str)), dd["n_sig_genes"])) if "n_sig_genes" in dd else {}
    active = {k for k, v in nsig.items() if v >= 10}
    un = []
    for p in fx.unreliable:
        pw = set(np.flatnonzero((w["plate"].astype(str) == p).to_numpy()))
        sub = pairs[(pairs["a"].isin(pw) | pairs["b"].isin(pw)).to_numpy()]
        t = T.replicate_summary(sub.assign(pair_type="pairs with its wells"), active)
        un.append(f"{p} ({T.replicate_text(t)})" if len(t) else f"{p} (no replicate pairs)")
    n["unreliable"] = "; ".join(un)
    n["reps"] = T.replicate_text(T.replicate_summary(pairs, active)) if len(pairs) else ""
    # do two wells of one drug-dose agree on cell loss? (the evidence behind a one-well 'toxic')
    if "cells_log2_beyond_row" in w:
        wd_ = w.assign(is_dmso=~fx.drug_w, unreliable_plate=~fx.reliable_w)[fx.used_w | ~fx.drug_w]
        n["cell_rep"] = T.cell_loss_replication_text(*T.cell_loss_replication(wd_))
    # drugs whose every drug-dose sits only on unreliable plates: unconfirmed as a whole
    if "unreliable_plate_only" in dd and len(dd):
        allu = dd.groupby("drug")["unreliable_plate_only"].all()
        n["p13only"] = _join(sorted(allu.index[allu]), 15)
        n["n_p13only"] = int(allu.sum())
    # drug-doses without data (their only well failed)
    try:
        sm = pd.read_csv(os.path.join(fx.out, "sample_map.csv"), dtype={"sample": str, "plate": str, "drug": str})
        sm = sm[~sm["is_dmso"].astype(bool)]
        sm["dose"] = T.dose_key(sm).values
        have = set(zip(dd["drug"], dd["dose"].astype(str)))
        miss = sm[[(a, b) not in have for a, b in zip(sm["drug"], sm["dose"])]].drop_duplicates(["drug", "dose"])
        n["nodata"] = _join(f"{r.drug} {float(r.conc):g} uM" for r in miss.sort_values(["drug", "conc"]).itertuples())
    except (OSError, KeyError, ValueError):
        n["nodata"] = ""
    # lines with usable expression in few wells
    if "pct_wells_usable" in fx.lines:
        sp = fx.lines[fx.lines["pct_wells_usable"] < 25].sort_values("pct_wells_usable")
        n["sparse"] = _join(f"{fx.line_name[i]} ({fx.lines.at[i, 'pct_wells_usable']:.0f}% of wells)" for i in sp.index)
    # salt forms: the same compound under two names (e.g. 'X' and 'X (hydrochloride)')
    base = defaultdict(list)
    for d in sorted(dd["drug"].unique()):
        base[T.salt_base(d).lower()].append(d)
    salts = [v for v in base.values() if len(v) >= 2]
    n["salts"] = (f"{len(salts)} compounds appear twice or more under salt / solvate names (e.g. "
                  + "; ".join(" / ".join(v) for v in salts[:3]) + ")") if salts else ""
    # one position at all doses (the layout confound)
    uw = w[fx.used_w & fx.drug_w]
    by = uw.groupby("drug").agg(n_dose=("dose", "nunique"), n_slot=("slot", "nunique"))
    multi = by[by["n_dose"] >= 2]
    n["layout"] = (f"{int((multi['n_slot'] == 1).sum())} of {len(multi)} drugs with several doses sit at one well "
                   f"position at all their doses") if len(multi) else ""
    nc = w[fx.drug_w & (w["position_not_correctable"].astype(str).str.lower().eq("true").to_numpy()
                        if "position_not_correctable" in w else False)]
    if len(nc):
        g = nc.groupby(["drug", "conc"]).agg(wells=("well", lambda s: "/".join(sorted(set(map(str, s))))),
                                             n=("well", "size")).reset_index().sort_values("n", ascending=False)
        n["notcorr"] = f"{len(nc)} drug wells: " + _join(f"{r.drug} {r.conc:g} uM ({r.wells}, {r.n} well"
                                                          f"{'s' if r.n > 1 else ''})" for r in g.itertuples())
    cs = dd[dd["composition_shift_log2"].abs() >= COMPOSITION_FLAG] if "composition_shift_log2" in dd else dd.iloc[:0]
    n["comp"] = (f"{len(cs)} drug-dose{'s' if len(cs) != 1 else ''} ("
                 + _join((f"{r.drug} {r.conc:g} uM {r.composition_shift_log2:+.2f}" for r in
                          cs.sort_values("composition_shift_log2").itertuples()), 4) + ")"
                 if len(cs) else "none")
    # the MTAP-null cut
    mc = fx.col_of("MTAP")
    if mc is not None:
        lc = np.asarray(fx.line_cpm)[:, mc]
        ratio = pd.Series(lc / np.median(lc))
        enough = (fx.lines["n_cells_total"] >= T.MIN_LINE_CELLS).to_numpy()
        thr, gap = T.null_threshold(ratio[enough])
        null = np.flatnonzero(enough & (ratio.values < thr))
        above = np.flatnonzero(enough & (ratio.values >= thr))
        if null.size:
            rv = ratio.values
            hi = null[np.argmax(rv[null])]
            nxt = above[np.argmin(rv[above])] if above.size else None
            gap_txt = (f"; the cut rests on a {2 ** gap:.2f}-fold gap between {fx.line_name[hi]} and "
                       f"{fx.line_name[nxt]} ({rv[nxt]:.2f}x)" if np.isfinite(gap) and nxt is not None
                       else "; no clear gap (default cut)")
            n["mtap"] = (f"{null.size} lines read MTAP below {thr:.2f}x of the median line ("
                         + ", ".join(f"{fx.line_name[i]} {rv[i]:.2f}x" for i in null[np.argsort(rv[null])]) + ")"
                         + gap_txt)
    return n


def rewrap(text, width=118):
    """Re-flow a Markdown text of headings, '- ' / 'N. ' bullets (also indented) and their continuation lines, so
    that bullets with numbers filled in from the data still read as tidy lines."""
    out, cur = [], None

    def flush():
        if cur:
            ind, mark, body = cur
            out.append(textwrap.fill(body, width, initial_indent=ind + mark, subsequent_indent=ind + " " * len(mark),
                                     break_on_hyphens=False, break_long_words=False))

    for line in text.splitlines():
        m = re.match(r"^(\s*)(- |\d+\. )(.*)$", line)
        if m:
            flush()
            cur = [m.group(1), m.group(2), m.group(3).strip()]
        elif not line.strip() or line.startswith("#") or cur is None:
            flush()
            cur = None
            out.append(line)
        else:
            cur[2] = (cur[2] + " " + line.strip()).strip()
    flush()
    return "\n".join(out) + "\n"


def layout_counts(n):
    """(drugs at one position at all their doses, drugs with several doses) from the notes, or (None, None)."""
    m = re.match(r"(\d+) of (\d+)", n.get("layout", ""))
    return (int(m.group(1)), int(m.group(2))) if m else (None, None)


def methods_text(n):
    def say(key, fmt):
        return fmt.format(n[key]) if n.get(key) else ""
    src = (f"{n['lines']} cancer cell lines pooled in every well; {n['drugs']} drugs at {n['doses']} uM "
           f"({n['drug_doses']:,} drug-doses with data); {n['plates']} plates of 96 wells; {n['genes']:,} genes tested"
           if n else "~50 cancer cell lines pooled in every well; ~380 drugs at 3 doses; 96-well plates")
    only = (f" {n['n_p13only']} drug{'s' if n['n_p13only'] != 1 else ''} sit only there at every dose, so nothing "
            f"about them is confirmed: {n['p13only']}." if n.get("p13only") else "")
    unrel = (f"Unreliable plates: {n['unreliable']}. Their wells are computed, but kept out of the centres, scales and "
             "plate-factor peers; a drug-dose with wells elsewhere uses only those; a drug-dose seen only there is "
             f"flagged 'unreliable plate only' (unconfirmed).{only}" if n.get("unreliable") else
             "Unreliable plates: none in this run (option --unreliable-plates).")
    one, multi = layout_counts(n)
    layout = (f"Layout: {n['layout']}: plates of one layout repeat it at the other doses, so the three doses of such a "
              "drug share one well position." if one else
              f"Layout: {n['layout']}." if n.get("layout") else "")
    return rewrap(f"""## How the numbers were made (method v{EFFECTS_VERSION})
- Source: Tahoe-100M: ~96M single cells; {src}; mRNA after 24 h. Cells of one line in one well are summed into a
  profile (profiles with < {MIN_CELLS} cells are left out).{say('nodata', ' No data (their only well failed): {}.')}
- Composition normalisation: each profile's composition (library-size) shift, the median residual of the genes its
  line expresses at >= {COMP_MIN_CPM:g} CPM (median-of-ratios, as DESeq2), is subtracted from every gene. Effects are
  relative to the median gene: when a drug makes a few genes take a large share of the counts, the other genes no
  longer read low. Drug-doses with |shift| >= {COMPOSITION_FLAG:g} log2 are flagged 'composition shift' (their raw
  CPM would differ by that much): {n.get('comp', '-')}.
- Effect of a drug-dose on a gene ('lfc', log2; fold change = 2^lfc): the profile's log2 CPM minus the median of all
  drug wells on the same plate for the same cell line (NOT the DMSO wells), minus the composition shift, median
  across cell lines, minus the well-position effect.
- Well-position correction, two passes: a well's position effect is the median of the other drugs' wells at the
  same position (any plate); in the second pass only those that are not themselves strongly moved for that gene
  (|z| < {POS_CLEAN_Z:g} in the first pass), so a strong drug sharing a position no longer leaves its mirror image on
  its neighbours. Fewer than 3 such wells: that gene is not corrected in that well ('position correction uncertain'
  in the per-gene tables); fewer than 3 other-drug wells at all: 'position not correctable' (whole well;
  {n.get('notcorr', 'none')}).
- z: the effect scored against the spread of the drug wells on reliable plates (median/MAD), divided by the factor
  of the well's plate and dose (the plate's spread over that of the same dose on the other reliable plates, never
  below 1): {n.get('wide') or 'no plate above ' + format(PLATE_SCALE_FLAG, 'g')}. A gene noisier on a plate than that
  plate's median gene (its own spread ratio > {PLATE_SCALE_BAND:g}x the factor) is widened further, never narrowed
  (quality/calibration_by_plate_gene.csv). Part of a wide plate's spread may be real drug activity, so the scaling
  only ever widens. Stouffer over the drug-dose's used wells. q_up / q_down:
  Benjamini-Hochberg within each gene across all drug-doses. 'Significant' means q < 0.10 and a fold change of at
  least 1.2x.
- {unrel} Replicate agreement by pair type (each drug-dose counted once: its mean r over its well pairs): {n.get('reps')
  or '-'}. Pairs at the same position share any position artifact, and few drug-doses have a replicate at a different
  position on reliable plates (only those listed), so these medians are not the reproducibility of a typical drug.
- Lines that barely express a gene (< 25% of the median line, e.g. deleted genes reading only background RNA from
  the other pooled lines) are left out for that gene. Failed wells (almost no cells while the same drug was fine
  elsewhere) are excluded.{say('sparse', ' Lines with usable expression in < 25% of wells (per-line results for '
                                         'them are thin): {}.')}
- {say('mtap', 'MTAP-null lines: {}.') or 'MTAP-null lines: see the cell_lines angle.'}
- Growth: each line's share of the cells in a well vs its usual share on that plate (log2 relative abundance);
  leave-drug-out position correction; its z includes counting noise. Negative = the line was depleted more.
- Per-line response strength (beta): for drug-doses with >= 20 significant genes, how strongly each line shows the
  consensus response over those genes (1 = like the typical line, 0 = no response, > 1 = stronger).
- Context per drug-dose: cells_log2_vs_plate (cell loss), umi/genes_per_cell_log2_vs_plate (transcription
  shutdown), their plate-row medians (row_*: the other drug wells in the same plate row), composition_shift_log2,
  plate_scale, replicate_r (mean r between its wells over its top 500 genes), S_PHASE / G2M_PHASE / PROTEASOME module
  shifts. 'flags' summarises them (rule 1).
- {layout} {say('salts', '{}: separate entries at other positions (a useful replicate), but one compound each.')}
""")


def rulebook_text(n):
    cell_rep = n.get("cell_rep") or "how well wells agree on cell loss is not known here: weak evidence alone"
    nd = f"~{n['drug_doses']:,}" if n else "~1,100"
    ng = f"~{n['genes']:,}" if n else "~16,000"
    one, multi = layout_counts(n)
    dose_rule = (f"But {one} of {multi} drugs with several doses sit at the same well position at all their doses "
                 "(same-layout plates), so for them dose consistency does not rule out a position artifact; agreement "
                 "at a different position (a replicate on another layout, a salt form) is the stronger test."
                 if one else "Agreement at a different position (a replicate on another layout, a salt form) is "
                 "the strongest test.")
    return rewrap(f"""## Rules for interpreting (learned on this dataset; follow them)
1. Artifacts first: read the 'flags' column (per-gene tables add the position flags) and act on each:
   - 'toxic': dose-consistent cell loss: fewer than half the plate's median cells (also against its plate row where
     that row itself lost or gained cells), every used well lost cells, and no higher dose of the same drug
     recovers. Expression changes may be secondary to dying cells. At the top dose there is no higher dose to check
     and most drug-doses have one well, so 'toxic' then rests on one well's cell count ({cell_rep}); prefer the dose
     series and the drug's known biology.
   - 'low cells (technical?)': fewer than half the cells, but not confirmed as dose-consistent loss beyond its plate
     row. It may be technical (the row lost cells: see row_cells_log2), a non-monotonic dose response (antimitotics:
     a lower dose kills, a higher one arrests), a row of toxic neighbours at a high dose, or a well that did not
     replicate. Do not call the drug toxic from it alone. A drug-dose with many significant genes is active: read
     its effects with the cell-loss caveat, and check row_cells_log2 and another dose or plate.
   - 'plate-row cell shift': the well's whole plate row gained or lost cells or UMIs per cell (recovery and depth
     artifacts by row); trust a hit only when another dose or plate agrees.
   - 'transcription drop': UMIs or genes per cell fall (also against the plate row): short, stable housekeeping,
     ribosomal and mitochondrial mRNAs then rise and long or unstable mRNAs fall, in relative terms.
   - 'cell-cycle shift': S or G2/M composition changed: every cycle-linked mRNA follows.
   - 'composition shift': a few genes took (or gave up) a large share of the counts; effects are relative to the
     median gene, so the raw CPM of every other gene would differ by that shift.
   - 'noisy plate (z scaled)': its plate is noisier than the same dose elsewhere; z (not the fold change) was
     divided by the factor. A hit seen only there needs another dose or plate.
   - 'unreliable plate only': seen only on a plate whose wells do not reproduce: unconfirmed.
   - 'position not correctable' / 'position correction uncertain': the effect still contains any position artifact
     (no clean other-drug wells at that position); ignore it unless a different position agrees.
   - 'position effect removed' (per gene): the correction moved it by > 1.15x; check the raw position (quality angle).
   - 'wells disagree': its replicate wells do not correlate (r < {DISAGREE_R:g} over its top {DISAGREE_TOP} genes while
     it has >= {DISAGREE_MIN_SIG} significant genes): unconfirmed.
   - Well positions: some positions shift specific genes on every plate (corrected; see the quality angle). The DMSO
     controls sit at {n.get('dmso', 'two wells per plate')}, and plates' DMSO wells differ from their drug median
     (most: {n.get('dmso_off', '-')}): never use DMSO-based numbers.
2. Dose consistency. Real effects usually grow with dose or appear at the top dose. A hit at a low dose only,
   absent at higher doses, is most likely noise. Say what the dose pattern is. {dose_rule}
3. Breadth. Check how many cell lines move. An effect carried by one or two lines is a line-specific observation.
4. Specific vs broad. Many drugs move big programs together (growth and ribosome biogenesis, proteasome,
   chaperones, cell cycle, stress, cholesterol). Say whether a change belongs to such a program or is specific.
5. Statistics. With {nd} drug-doses and {ng} genes, z > 3 happens thousands of times by chance: rely on q,
   effect size and consistency. Report fold changes (not log2) with q and the number of lines.
6. Known biology as a check. Look for expected effects (e.g. mTOR/PI3K inhibitors lower proteasome and
   ribosome-biogenesis genes; proteasome inhibitors raise proteasome subunits; HSP90 inhibitors raise
   heat-shock genes; statins raise cholesterol-synthesis genes; BRAF/MEK inhibitors deplete BRAF-mutant lines;
   KRAS G12C inhibitors deplete G12C lines) and say whether the data show them. Cytostatic drugs (BRAF/MEK, EGFR
   inhibitors) deplete their lines only weakly within 24 h: weak or missing selectivity is expected, not a failure.
7. mRNA after 24 h only: no claims about protein, function or causality. Label hypotheses as hypotheses.
   Treat non-polyadenylated or multi-mapping RNAs as noise in this assay: 7SK / RN7SK* pseudogenes, RNU*, snoRNAs,
   ribosomal-protein pseudogenes (RPS*P*, RPL*P*), MT-* pseudogenes (MTND*P*, MTATP*P*), unnamed ENSG lncRNAs and
   the replication-dependent histone genes (H1-*, H2AC*, H2BC*, H3C*, H4C*; these also follow S phase). Do not base
   a finding on them.
8. Every number in your report must come from a query you ran on the files; name the file it came from.
""")


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
        extra = [f"plate row: cells {2 ** r['row_cells_log2']:.2f}x" if "row_cells_log2" in r else "",
                 f"composition shift {r['composition_shift_log2']:+.2f} log2" if "composition_shift_log2" in r else "",
                 f"plate factor {r['plate_scale']:.2f}" if "plate_scale" in r else "",
                 f"replicate r {r['replicate_r']:.2f}" if np.isfinite(r.get("replicate_r", np.nan)) else "",
                 f"left out (unreliable plate): {r['wells_left_out']}" if r.get("wells_left_out") else ""]
        if any(extra):
            out.append("; ".join(x for x in extra if x))
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
    t = dd[["drug", "conc"]].copy()
    t["fold"] = 2 ** np.asarray(fx.DD_lfc)[:, c]
    t["z"] = np.asarray(fx.DD_z)[:, c]
    t["q_up"] = np.asarray(fx.DD_qup)[:, c]
    t["q_down"] = np.asarray(fx.DD_qdn)[:, c]
    t["z_by_dose_up"] = [fx.dose_pattern(c, d)[1] for d in t["drug"]]
    t["position"] = position_flag(fx, c)
    t["plate_factor"] = fx.gene_plate_scale(c)
    t["flags"] = gene_flag_col(fx, c)              # the drug-dose's flags + this gene's position / plate flags
    lc = np.asarray(fx.line_cpm)[:, c]
    sm = np.asarray(fx.slot_median)[:, c]
    w = int(np.nanargmax(np.where(np.isfinite(sm), np.abs(sm), -1)))
    lines = pd.DataFrame({"line": fx.line_name, "cpm": lc}).sort_values("cpm")
    out = [f"# {g['label']}",
           f"pooled {g['pooled_cpm']:.1f} CPM; expressed in {int(g['n_lines_expressing'])} lines; lowest lines: "
           + ", ".join(f"{a} {b:.1f}" for a, b in lines.head(5).values) + "; highest: "
           + ", ".join(f"{a} {b:.1f}" for a, b in lines.tail(3).values),
           f"largest well-position shift: {T.well_name(w + 1)} {2 ** sm[w]:.2f}x (corrected for); position "
           f"correction for this gene: uncertain in {sum(p == 'uncertain' for p in t['position'])} drug-doses, not "
           f"correctable in {sum(p == 'not correctable' for p in t['position'])} (column 'position')",
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
    # replicate agreement by pair type: every pair of wells of a drug-dose vs random pairs of different drugs on
    # different plates, and vs such pairs at the same position (which share the position artifact)
    pairs, nulls, snull = replicate_pairs(fx)
    plate, wname = w["plate"].astype(str).to_numpy(), w["well"].astype(str).to_numpy()
    nsig = {(a, str(b)): int(v) for a, b, v in zip(fx.dd["drug"], fx.dd["dose"], fx.dd["n_sig_genes"])}
    reps = []
    for (d, dose, typ), gg in pairs.groupby(["drug", "dose", "pair_type"], sort=False):
        ww = sorted(set(gg["a"]) | set(gg["b"]))
        r = float(gg["r"].mean())
        reps.append({"drug": d, "dose": dose, "pair_type": typ, "n_pairs": len(gg), "n_wells": len(ww),
                     "plates": ",".join(sorted(set(plate[ww]), key=lambda p: (len(p), p))),
                     "wells": ",".join(f"{plate[i]}:{wname[i]}" for i in ww), "r": r,
                     "pct_above_random_pairs": 100 * float((nulls < r).mean()) if nulls.size else np.nan,
                     "pct_above_same_position_pairs": 100 * float((snull < r).mean()) if snull.size else np.nan,
                     "n_sig_genes": nsig.get((d, str(dose)), 0),
                     "position_not_correctable": bool(gg["position_not_correctable"].any())})
    cols = ["drug", "dose", "pair_type", "n_pairs", "n_wells", "plates", "wells", "r", "pct_above_random_pairs",
            "pct_above_same_position_pairs", "n_sig_genes", "position_not_correctable"]
    rep = pd.DataFrame(reps, columns=cols)
    rep.sort_values("r").to_csv(os.path.join(folder, "replicates.csv"), index=False)
    pp = pairs.assign(pa=plate[pairs["a"].to_numpy(dtype=int)], pb=plate[pairs["b"].to_numpy(dtype=int)])
    pp["plate_pair"] = [" + ".join(sorted({x, y}, key=lambda p: (len(p), p))) for x, y in zip(pp["pa"], pp["pb"])]
    pp["strong"] = [nsig.get((d, str(o)), 0) >= 200 for d, o in zip(pp["drug"], pp["dose"])]
    ppt = pp.groupby(["plate_pair", "pair_type"]).agg(n_pairs=("r", "size"), median_r=("r", "median"),
                                                      n_strong_pairs=("strong", "sum")).reset_index()
    ppt["median_r_strong"] = [pp.loc[(pp["plate_pair"] == a) & (pp["pair_type"] == b) & pp["strong"], "r"].median()
                              for a, b in zip(ppt["plate_pair"], ppt["pair_type"])]
    ppt.sort_values("n_pairs", ascending=False).to_csv(os.path.join(folder, "replicate_by_plate_pair.csv"), index=False)
    # calibration: per gene, and per plate x dose before / after the plate factors (shares of the MEASURED values:
    # a missing z is neither inside nor beyond 1.96)
    Zd = np.asarray(fx.Z)[fx.drug_w][:, gi]
    nfin = np.maximum(np.isfinite(Zd).sum(axis=0), 1)
    cal = pd.DataFrame({"gene": labels[gi], "pct_abs_z_over_1.96": 100 * (np.abs(Zd) > 1.96).sum(axis=0) / nfin,
                        "pct_abs_z_over_3": 100 * (np.abs(Zd) > 3).sum(axis=0) / nfin})
    cal.sort_values("pct_abs_z_over_3", ascending=False).to_csv(os.path.join(folder, "calibration_by_gene.csv"),
                                                                index=False)
    wd = w[fx.drug_w].reset_index(drop=True)
    fac = wd["plate_scale"].to_numpy(dtype=float) if "plate_scale" in wd else np.ones(len(wd))
    FGd = fx.gene_scale(gi, np.flatnonzero(fx.drug_w))         # each gene's divisor in each drug well

    def pct(a, t):
        return 100 * float((a > t).sum()) / max(int(np.isfinite(a).sum()), 1)
    crow = []
    for (p, dose), g_ in wd.groupby(["plate", "dose"], sort=False):
        ii = g_.index.to_numpy()
        za, zb = np.abs(Zd[ii]), np.abs(Zd[ii] * FGd[ii])
        zg = np.abs(Zd[ii] * FGd[ii] / fac[ii][:, None])       # the group factor only (no gene-specific widening)
        crow.append({"plate": p, "dose": dose, "conc": g_["conc"].iloc[0], "n_drug_wells": len(ii),
                     "plate_scale_group": str(g_["plate_scale_group"].iloc[0]) if "plate_scale_group" in g_ else "",
                     "unreliable_plate": p in fx.unreliable, "plate_factor": float(np.mean(fac[ii])),
                     "pct_genes_widened_beyond_group": 100 * float(np.mean(FGd[ii][0] > fac[ii][0] * 1.0001)),
                     "pct_abs_z_over_1.96_before_scaling": pct(zb, 1.96),
                     "pct_abs_z_over_1.96_group_factor_only": pct(zg, 1.96),
                     "pct_abs_z_over_1.96": pct(za, 1.96),
                     "pct_abs_z_over_3_before_scaling": pct(zb, 3),
                     "pct_abs_z_over_3": pct(za, 3), "pct_z_missing": 100 * float(np.mean(~np.isfinite(Zd[ii])))})
    order = {p: i for i, p in enumerate(fx.plates)}
    calp = pd.DataFrame(crow)
    calp = calp.assign(_o=calp["plate"].map(order)).sort_values(["conc", "_o"]).drop(columns="_o")
    calp.to_csv(os.path.join(folder, "calibration_by_plate.csv"), index=False)
    # the growth z (relative abundance, wells x lines) is NOT plate-scaled: its calibration per plate and dose, so a
    # noisy plate shows here before a growth hit from it is trusted
    zA = np.asarray(fx.zA)[fx.drug_w]
    grow = []
    for (p, dose), g_ in wd.groupby(["plate", "dose"], sort=False):
        za_ = np.abs(zA[g_.index.to_numpy()])
        grow.append({"plate": p, "dose": dose, "conc": g_["conc"].iloc[0], "n_drug_wells": len(g_),
                     "unreliable_plate": p in fx.unreliable, "pct_growth_abs_z_over_1.96": pct(za_, 1.96),
                     "pct_growth_abs_z_over_3": pct(za_, 3)})
    pd.DataFrame(grow).assign(_o=lambda x: x["plate"].map(order)).sort_values(["conc", "_o"]).drop(columns="_o") \
        .to_csv(os.path.join(folder, "calibration_growth_by_plate.csv"), index=False)
    del zA
    # per gene x plate group for the focus genes and the genes widened most beyond their group (one plate noisier
    # for that gene alone: its own factor; T's plate_scale_by_gene.csv holds the same for the gene panel)
    if hasattr(fx, "plate_scale_gene") and "plate_scale_group_id" in wd:
        FG = np.asarray(fx.plate_scale_gene)
        ps = pd.read_csv(os.path.join(fx.d, "plate_scale.csv"), dtype={"plate": str, "dose": str}) \
            if os.path.exists(os.path.join(fx.d, "plate_scale.csv")) else pd.DataFrame()
        gid_w = wd["plate_scale_group_id"].to_numpy(dtype=int)
        gf = {int(i): float(fac[gid_w == i][0]) for i in np.unique(gid_w) if i >= 0}
        names = {int(i): str(wd.loc[gid_w == i, "plate_scale_group"].iloc[0]) for i in gf}
        ids = sorted(gf)
        widen = FG[ids][:, gi] / np.array([gf[i] for i in ids])[:, None] if ids else np.zeros((0, gi.size))
        pick = [fx.col_of(gname) for gname in _BRIEF.get("focus") or ["MTAP", "PSMD10"]]
        pick = [c for c in pick if c is not None and fx.gmask[c]]
        if widen.size:
            top = np.argsort(-np.nanmax(widen, axis=0))[:30]
            pick += [int(gi[j]) for j in top if np.nanmax(widen[:, j]) > 1.0001 and int(gi[j]) not in pick]
        grow = []
        for c in pick:
            j = int(np.flatnonzero(gi == c)[0])
            for i in sorted(gf):
                ii = np.flatnonzero(gid_w == i)
                z = Zd[ii, j]
                grow.append({"gene": labels[c], "plate_scale_group": names[i], "n_drug_wells": int(ii.size),
                             "group_factor": gf[i], "gene_factor": float(FG[i, c]),
                             "pct_abs_z_over_1.96_group_factor_only": pct(np.abs(z * FG[i, c] / gf[i]), 1.96),
                             "pct_abs_z_over_1.96": pct(np.abs(z), 1.96)})
        pd.DataFrame(grow).to_csv(os.path.join(folder, "calibration_by_plate_gene.csv"), index=False)
    del Zd, FGd
    if os.path.exists(os.path.join(fx.d, "plate_scale.csv")):
        shutil.copy(os.path.join(fx.d, "plate_scale.csv"), os.path.join(folder, "plate_scale.csv"))
    # composition shifts and wells without a position correction
    dd = fx.dd
    comp = dd[["drug", "conc", "composition_shift_log2", "n_sig_genes", "flags"]].copy() \
        if "composition_shift_log2" in dd else pd.DataFrame(columns=["drug", "conc", "composition_shift_log2"])
    comp.sort_values("composition_shift_log2", key=np.abs, ascending=False).to_csv(
        os.path.join(folder, "composition_shifts.csv"), index=False)
    ncw = w[fx.drug_w & w["position_not_correctable"].astype(str).str.lower().eq("true").to_numpy()] \
        if "position_not_correctable" in w else w.iloc[:0]
    ncw[[c for c in ("plate", "well", "drug", "conc", "position_wells_used") if c in ncw]].to_csv(
        os.path.join(folder, "position_not_correctable_wells.csv"), index=False)
    # by pair type with each drug-dose counted once (its mean r; pairs with a well that had no position correction
    # reported apart): the same unit as the strong drug-doses below
    strong_set = {k for k, v in nsig.items() if v >= 200}
    rs = T.replicate_summary(pairs, strong_set)
    bytype = {r.pair_type: {"drug_doses": int(r.n_drug_doses), "drugs": int(r.n_drugs), "well_pairs": int(r.n_pairs),
                            "median_r": float(r.median_r), "drugs_named": r.drugs} for r in rs.itertuples()}
    strong = rep[rep["n_sig_genes"] >= 200]
    summary = {"genes": int(gi.size), "drug_wells": int(fx.drug_w.sum()), "drug_doses": int(len(fx.dd)),
               "cell_lines": int(len(fx.lines)), "unreliable_plates": fx.unreliable,
               "median_pct_abs_z_over_1.96": float(cal["pct_abs_z_over_1.96"].median()),
               "median_pct_abs_z_over_3": float(cal["pct_abs_z_over_3"].median()),
               "plates_z_scaled_over_1.2": {(r.plate_scale_group or f"{r.plate} {r.dose}"):
                                            round(float(r.plate_factor), 3) for r in calp.itertuples()
                                            if r.plate_factor > PLATE_SCALE_FLAG
                                            and r.n_drug_wells >= PLATE_SCALE_MIN_WELLS},
               "replicate_rows": int(len(rep)), "replicate_well_pairs": int(len(pairs)),
               "replicate_median_r": float(rep["r"].median()) if len(rep) else None,
               "replicate_median_r_by_pair_type": bytype,
               "replicate_median_r_strong_by_pair_type": {r.pair_type: float(r.median_r_active) for r in
                                                          rs.itertuples() if r.n_active},
               "replicate_median_r_strong": float(strong["r"].median()) if len(strong) else None,
               "random_pair_median_r": float(np.median(nulls)) if nulls.size else None,
               "random_pair_95th_pct_r": float(np.percentile(nulls, 95)) if nulls.size else None,
               "same_position_random_pair_median_r": float(np.median(snull)) if snull.size else None,
               "same_position_random_pair_95th_pct_r": float(np.percentile(snull, 95)) if snull.size else None,
               "drug_doses_composition_shift": int((comp["composition_shift_log2"].abs() >= COMPOSITION_FLAG).sum()),
               "drug_wells_position_not_correctable": int(len(ncw)),
               "failed_wells": int(len(pd.read_csv(os.path.join(folder, "failed_wells.csv"))))}
    with open(os.path.join(folder, "summary.json"), "w", encoding="utf-8") as fh:
        json.dump(summary, fh, indent=1)
    write_brief(folder, TITLES["quality"], """
How trustworthy are these data, and where are the traps? Quantify the well-position artifacts (which positions,
how many genes, which genes; which wells could not be corrected), the plate DMSO offsets, the failed wells, the
composition shifts, and how reproducible drug signatures are compared with random pairs, separately by pair type:
'same position, other plate' pairs share the position artifact (compare them with the same-position null),
'different position' pairs are the real test, 'same plate' and 'unreliable plate' pairs are reported apart. Count
each drug-dose once (replicates.csv has one row per drug-dose and pair type; summary.json gives drug-doses and
drugs per type): only the drug-doses listed there have a different-position replicate on reliable plates, so name
them and do not read their r as the reproducibility of a typical drug; pairs with a well that had no position
correction (position_not_correctable) share an uncorrected artifact and are reported apart; give
replicate r per plate pair (replicate_by_plate_pair.csv) so the choice of unreliable plates can be checked. Check
whether the z-scores are calibrated: the share beyond |z| 1.96 grows with dose because real effects grow with dose,
so compare plates of the SAME dose (calibration_by_plate.csv, before and after the plate factor): a plate far above
the others at its dose is miscalibrated, not active. Report that plate x dose table, and the same for the growth z
(calibration_growth_by_plate.csv: not plate-scaled). Conclude with what the other analyses should watch out for.
""", [("summary.json", "headline numbers (replicate r by pair type, also for strong drug-doses with >= 200 genes; "
                       "nulls; plates whose z were scaled)"),
      ("position_effects.csv", "per well position, sorted by its strongest gene-specific artifact (artifact_gene: "
                               "the shift >= 1.2x that stands out most from that gene's spread over all positions, "
                               "artifact_z_vs_gene_spread); also its largest raw shift, genes shifted > 1.2x by every "
                               "drug placed there, top genes, drugs (n_drug_wells: positions with < 3 hold too few "
                               "drugs to tell a position effect from those drugs)"),
      ("position_sensitive_genes.csv", "500 genes whose worst position stands out most from their own spread "
                                       "over positions (z_vs_gene_spread; shifts >= 1.2x only)"),
      ("position_not_correctable_wells.csv", "drug wells with < 3 other-drug wells at their position: no correction"),
      ("plate_dmso_offsets.csv", "per plate: how far DMSO sits from the drug median (>0 = DMSO low), top genes"),
      ("failed_wells.csv", "excluded wells"),
      ("composition_shifts.csv", "per drug-dose: composition shift (log2; subtracted from every gene), flags"),
      ("replicates.csv", "per drug-dose and pair type: every well used, mean r of the genome-wide signatures over "
                         "its well pairs, percentile among random pairs of different drugs on different plates and "
                         "among such pairs at the same position, position_not_correctable (a well without position "
                         "correction)"),
      ("calibration_by_plate_gene.csv", "per plate group, for the focus genes and the genes widened most beyond "
                                        "their group: group factor, the gene's own factor, % |z| > 1.96 with each"),
      ("calibration_growth_by_plate.csv", "per plate and dose: % of the growth (relative abundance) z beyond 1.96 "
                                          "and 3; these z are not plate-scaled, so a plate far above its dose's "
                                          "others makes growth hits from it suspect"),
      ("replicate_by_plate_pair.csv", "per plate pair and pair type: well pairs, median r (all, strong drug-doses)"),
      ("calibration_by_plate.csv", "per plate and dose: drug wells, plate factor, % of the measured |z| > 1.96 and "
                                   "> 3 before the plate factors, with the group factor only, and after the genes' "
                                   "own factors (all tested genes); % of z missing"),
      ("plate_scale.csv", "the plate factors (factor_raw = the group's spread over its same-dose peers on the other "
                          "reliable plates; factor = max(1, raw))"),
      ("calibration_by_gene.csv", "per gene: % of drug wells with |z| > 1.96 and > 3")], deeper_queries(fx.out))


def lowest_active_dose(conc, nsig, min_genes=10):
    """The lowest dose such that it and every higher dose have >= min_genes significant genes (ascending conc);
    'low dose only (noise?)' when only lower doses do; NaN when no dose does."""
    act = np.asarray(nsig) >= min_genes
    if not act.any():
        return np.nan
    if not act[-1]:
        return "low dose only (noise?)"
    k = len(act) - 1
    while k > 0 and act[k - 1]:
        k -= 1
    return float(conc[k])


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
        drows.append({"drug": drug, "moa_fine": gg["moa_fine"].iloc[0], "targets": gg["targets"].iloc[0],
                      "doses": T.fmt_list(gg["conc"].tolist(), "{:g}"),
                      "n_sig_by_dose": " / ".join(str(int(x)) for x in nsg),
                      "max_sig": int(nsg.max()),
                      "lowest_active_dose": lowest_active_dose(gg["conc"].to_numpy(dtype=float), nsg),
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
transcription shutdown or cell-cycle effects, how signatures grow with dose (potency: lowest active dose; 'low dose
only (noise?)' when the top dose is not active), which
drugs look alike (and whether that matches their mechanism or reveals shared off-target effects), and surprises.
Use known pharmacology as a check. The cards/ folder has a one-page card per drug.
""", [("drug_summary.csv", "one row per drug: doses, significant genes per dose, lowest active dose (the lowest dose "
                           "that, like every higher dose, has >= 10 genes; 'low dose only (noise?)' otherwise), "
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
    posu = np.asarray(fx.DD_posunc) if hasattr(fx, "DD_posunc") else np.zeros(lfc.shape, bool)
    pe = np.asarray(fx.DD_poseff) if hasattr(fx, "DD_poseff") else np.zeros(lfc.shape, np.float32)

    def gflag(i, c):                     # per-gene flags: the drug-dose's + this gene's position flags
        return gene_flags(flags[i], posu[i, c], pe[i, c])

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
            rec[f"best_{name}_flags"] = gflag(b, c)
            other = [i for i in o[1:] if drugs[i] != drugs[b]]
            rec[f"{name}_specificity_z_gap"] = zz[b] - (zz[other[0]] if other else np.nan)
            for r_, i in enumerate(o):
                tops.append((labels[c], name, r_ + 1, drugs[i], concs[i], float(2 ** lfc[i, c]), float(zc[i]),
                             float(qq[i, c]), gflag(i, c)))
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
               & ~gs[f"best_{direction}_flags"].map(has_artifact) & (gs["corr_with_G2M"].abs() < 0.5)
               & ~gs["gene"].astype(str).str.match(NOISE_RNA_RE.pattern)].copy()
        pats = [fx.dose_pattern(col_of_label[g], d, sign) for g, d in zip(t["gene"], t[f"best_{direction}_drug"])]
        t["dose_pattern"] = [p[0] for p in pats]
        t["z_by_dose"] = [p[1] for p in pats]
        t = t[~t["dose_pattern"].isin(["inconsistent across doses", "none"])]
        t = t.sort_values(f"best_{direction}_fold", ascending=(direction == "down"))
        # one global program (a drug that moves thousands of genes) would fill the list: <= 25 genes per drug-dose
        return t.groupby([f"best_{direction}_drug", f"best_{direction}_conc"], sort=False).head(25)

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
      ("inducible_genes.csv", "genes with a clean inducer: >= 1.5x, q < 0.05, no artifact flag (toxic, "
                              "transcription drop, cell-cycle shift, unreliable plate only, position not correctable "
                              "or uncertain, wells disagree), dose-consistent, not cell-cycle driven, not a noise-class "
                              "RNA (rule 7), at most 25 genes per best drug-dose (with the dose pattern)"),
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
    ref = fx.ref_w                       # centre and scale: drug wells on reliable plates
    c = np.nanmedian(d2[ref])
    s = 1.4826 * np.nanmedian(np.abs(d2[ref] - c))
    wv = max(s ** 2 - np.nanmedian(var[ref]), (0.25 * s) ** 2)
    zz = (d2 - c) / np.sqrt(wv + var)
    below = (A2[:, alt] < np.nanmedian(A2[:, rest], axis=1)[:, None]).sum(axis=1)
    t = pd.DataFrame({"drug": w["drug"], "dose": w["dose"], "conc": w["conc"], "delta": d2 - c, "z": zz,
                      "below": below})[fx.drug_w & fx.used_w]          # each drug-dose over its used wells
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


def growth_replication(fx, rows, use):
    """Per drug-dose row: r of its growth pattern (DD_A over the lines `use`) with the same drug's other doses (the
    best one), and the mean r between its own used wells (A2). A growth pattern seen once (one well, one dose) can
    correlate with thousands of genes by chance."""
    DA = np.asarray(fx.DD_A)[:, use]
    A2 = np.asarray(fx.A2)[:, use]

    def r_(a, b):
        ok = np.isfinite(a) & np.isfinite(b)
        if ok.sum() < 6 or a[ok].std() == 0 or b[ok].std() == 0:
            return np.nan
        return float(np.corrcoef(a[ok], b[ok])[0, 1])

    rd, rw = np.full(len(rows), np.nan), np.full(len(rows), np.nan)
    for k, i in enumerate(rows):
        other = [j for j in fx.rows_of_drug.get(fx.dd.at[i, "drug"], []) if j != i]
        rr = [r_(DA[i], DA[j]) for j in other]
        rr = [x for x in rr if np.isfinite(x)]
        rd[k] = max(rr) if rr else np.nan
        ww = fx.wells_of_dd.get(int(i), np.zeros(0, int))
        rr = [r_(A2[a], A2[b]) for x, a in enumerate(ww) for b in ww[x + 1:]]
        rr = [x for x in rr if np.isfinite(x)]
        rw[k] = float(np.mean(rr)) if rr else np.nan
    return rd, rw


def calibrate_cols(z, rows):
    """Robust z of each column (gene) against its own distribution over the drug-doses `rows` (empirical null):
    a gene whose level tracks growth under most drugs (proliferation) no longer counts as a marker for each of them.
    The scale is never below 1 (the textbook null): growth patterns shared by many drug-doses make a gene's
    spread narrow, and dividing by that would inflate small differences."""
    if z.shape[0] == 0 or not np.any(rows):
        return z
    c, s = robust_cols(z, rows)
    return (z - c) / np.maximum(s, 1.0)


def angle_biomarkers(fx, folder):
    """Does a line's baseline level of a gene predict how a drug-dose affects its growth? Every gene x drug-dose,
    raw and within lineage (organ effects removed from both sides); each gene calibrated against its own
    distribution over the drug-doses."""
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
    rel = ~dd["unreliable_plate_only"].to_numpy(dtype=bool)[elig]
    z, zw = calibrate_cols(z, rel), calibrate_cols(zw, rel)               # empirical null per gene
    q = bh_columns((2 * norm_sf(np.abs(z))).T).T if elig.size else z          # BH over genes, per drug-dose
    qw = bh_columns((2 * norm_sf(np.abs(zw))).T).T if elig.size else zw
    mk, mkw = (q < 0.1) & (np.abs(z) >= 3), (qw < 0.1) & (np.abs(zw) >= 3)   # markers
    lin_r2 = (np.linalg.norm(unit(Ra) @ H, axis=1) ** 2) if elig.size else np.zeros(0)  # growth pattern explained by organ
    r_doses, r_wells = growth_replication(fx, elig, use)
    top, hits, sel = [], [], []
    for j, i in enumerate(elig):
        nsel = int(hit[i].sum())
        o = np.argsort(-np.abs(rho[j]))[:10]                     # by effect size; markers pass the calibrated test
        ow = np.argsort(-np.abs(rho_w[j]))[:5]
        bm = np.flatnonzero(mk[j])
        bm = bm[np.argmax(np.abs(rho[j, bm]))] if bm.size else o[0]
        bmw = np.flatnonzero(mkw[j])
        bmw = bmw[np.argmax(np.abs(rho_w[j, bmw]))] if bmw.size else ow[0]
        repl = bool(np.nanmax([r_doses[j], r_wells[j], -1]) >= 0.3)
        sel.append({"drug": dd.at[i, "drug"], "conc": dd.at[i, "conc"], "moa_fine": dd.at[i, "moa_fine"],
                    "lines_strongly_affected": nsel, "growth_pattern_explained_by_organ_pct": 100 * lin_r2[j],
                    "replicated": repl, "growth_r_other_doses": r_doses[j], "growth_r_between_wells": r_wells[j],
                    "best_marker": f"{labels[bm]} (rho {rho[j, bm]:+.2f}, z {z[j, bm]:+.1f}, q {q[j, bm]:.1g}"
                                   + ("" if mk[j, bm] else "; no marker") + ")",
                    "best_marker_within_lineage": f"{labels[bmw]} (rho {rho_w[j, bmw]:+.2f}, z {zw[j, bmw]:+.1f}, "
                                                  f"q {qw[j, bmw]:.1g}" + ("" if mkw[j, bmw] else "; no marker") + ")",
                    "n_markers": int(mk[j].sum()), "n_markers_within_lineage": int(mkw[j].sum()),
                    "flags": dd.at[i, "flags"]})
        for r_, g in enumerate(o):
            top.append({"drug": dd.at[i, "drug"], "conc": dd.at[i, "conc"], "rank": r_ + 1, "gene": labels[g],
                        "rho": rho[j, g], "z": z[j, g], "q": q[j, g], "rho_within_lineage": rho_w[j, g],
                        "z_within_lineage": zw[j, g], "q_within_lineage": qw[j, g], "marker": bool(mk[j, g] or mkw[j, g]),
                        "replicated": repl,
                        "direction": "high level -> more depleted" if rho[j, g] < 0 else "high level -> spared"})
        m = np.flatnonzero(mk[j] | mkw[j])
        m = m[np.argsort(-np.abs(rho[j, m]))][:200]
        for g in m:
            hits.append((dd.at[i, "drug"], dd.at[i, "conc"], labels[g], float(rho[j, g]), float(z[j, g]), float(q[j, g]),
                         float(rho_w[j, g]), float(zw[j, g]), float(qw[j, g]), repl))
    cols = ["drug", "conc", "moa_fine", "lines_strongly_affected", "growth_pattern_explained_by_organ_pct", "replicated",
            "growth_r_other_doses", "growth_r_between_wells", "best_marker", "best_marker_within_lineage", "n_markers",
            "n_markers_within_lineage", "flags"]
    pd.DataFrame(sel, columns=cols).sort_values(["replicated", "n_markers_within_lineage", "n_markers"],
                                                ascending=False).to_csv(os.path.join(folder, "selective_drugs.csv"),
                                                                        index=False)
    pd.DataFrame(top, columns=["drug", "conc", "rank", "gene", "rho", "z", "q", "rho_within_lineage", "z_within_lineage",
                               "q_within_lineage", "marker", "replicated", "direction"]).to_csv(
        os.path.join(folder, "biomarker_top10.csv"), index=False)
    pd.DataFrame(hits, columns=["drug", "conc", "gene", "rho", "z", "q", "rho_within_lineage", "z_within_lineage",
                                "q_within_lineage", "replicated"]) \
        .to_parquet(os.path.join(folder, "biomarker_hits.parquet"), index=False)
    # genes that predict response to many drugs (e.g. drug efflux pumps, proliferation)
    if elig.size:
        repl = np.array([s_["replicated"] for s_ in sel], dtype=bool)
        gm = pd.DataFrame({"gene": labels, "n_drug_doses_marker": mk.sum(axis=0),
                           "n_within_lineage": mkw.sum(axis=0),
                           "n_within_lineage_replicated": (mkw & repl[:, None]).sum(axis=0),
                           "pct_high_level_more_depleted":
                               100 * (mk & (rho < 0)).sum(axis=0) / np.maximum(mk.sum(axis=0), 1),
                           "sd_log2_across_lines": X.std(axis=1)})
        gm["top_drugs"] = ["; ".join(f"{dd.at[elig[j], 'drug']} {dd.at[elig[j], 'conc']:g} ({rho[j, g]:+.2f})"
                                     for j in np.argsort(-np.abs(rho[:, g]))[:5]) for g in range(len(labels))]
        gm.sort_values(["n_within_lineage_replicated", "n_within_lineage"], ascending=False).head(2000).to_csv(
            os.path.join(folder, "marker_genes.csv"), index=False)
    # targets: does the level of a drug's own target predict who it kills?
    trows = []
    lab_pos = {lb: g for g, lb in enumerate(labels)}
    for j, i in enumerate(elig):
        for tg in [x.strip() for x in str(dd.at[i, "targets"]).split(",") if x.strip()]:
            g = lab_pos.get(tg)
            if g is not None:
                trows.append({"drug": dd.at[i, "drug"], "conc": dd.at[i, "conc"], "target": tg, "rho": rho[j, g],
                              "z": z[j, g], "q": q[j, g], "rho_within_lineage": rho_w[j, g],
                              "z_within_lineage": zw[j, g], "q_within_lineage": qw[j, g]})
    pd.DataFrame(trows, columns=["drug", "conc", "target", "rho", "z", "q", "rho_within_lineage", "z_within_lineage",
                                 "q_within_lineage"]) \
        .sort_values("rho").to_csv(os.path.join(folder, "target_level_vs_sensitivity.csv"), index=False)
    write_brief(folder, TITLES["biomarkers"], f"""
For every drug-dose that kills some cell lines more than others ({elig.size} drug-doses with >= 3 lines changed >= 1.4x
at z >= 1.5; lines compared within the
same wells), which genes' baseline expression predicts who dies or who is spared: the genome-wide version of
'does Gankyrin level predict response'. Lineage confounds this (lineage marker genes predict lineage-selective
drugs), so judge markers by rho_within_lineage (organ effects removed) and say when a drug's pattern is mostly
lineage (growth_pattern_explained_by_organ_pct). Each gene's z is calibrated against its own distribution over all
drug-doses (a proliferation gene that tracks growth under most drugs is no marker for each of them); a marker needs
that calibrated |z| >= 3 and q < 0.1. One well's growth pattern can still correlate with thousands of genes, so
trust drug-doses whose growth pattern replicates (replicated: r >= 0.3 with another dose of the drug or between its
wells; selective_drugs.csv lists them first) and treat the others as unconfirmed. Check known biology first: ABCB1
(MDR1) or ABCG2 high lines spared by their substrates (taxanes, anthracyclines, vinca alkaloids, some kinase
inhibitors); a targeted drug's own target predicting sensitivity (ERBB2 for HER2 inhibitors, EGFR for EGFR
inhibitors, ESR1 for anti-estrogens); proliferation genes predicting sensitivity to antimitotics. Then report the
strongest new, lineage-independent, replicated markers, and genes that predict response to many drugs. With ~{n}
lines, |rho| below ~0.5 is rarely significant.
Correlation is weak for genes lost in only a few lines (deletions such as MTAP/CDKN2A): those are tested far more
sensitively by the expression-loss screen in ../cell_lines/expression_loss_selective_drugs.csv; cross-check there.
Note: here every usable line is included for every gene, also lines that do not express it (the 'left out for that
gene' rule below applies only to drug effects on expression, not to these baseline levels).
""", [("selective_drugs.csv", "per drug-dose with >= 3 lines strongly affected (>= 1.4x, z >= 1.5): replicated "
                              "(growth pattern r >= 0.3 with another dose or between its wells; listed first), how much "
                              "of its pattern organ explains, best marker raw and within lineage, number of markers "
                              "(calibrated |z| >= 3 and q < 0.1), flags"),
      ("biomarker_top10.csv", "per drug-dose: the 10 genes whose baseline level best predicts growth (largest |rho|, "
                              "Spearman across lines; negative = high-level lines depleted more), calibrated z and q, "
                              "within-lineage rho / z / q, marker (passes the calibrated test), replicated"),
      ("biomarker_hits.parquet", "all markers (raw or within lineage; top 200 per drug-dose)"),
      ("marker_genes.csv", "per gene: how many drug-doses it is a marker for (raw / within lineage / within lineage and "
                           "replicated), direction, top drugs"),
      ("target_level_vs_sensitivity.csv", "every drug-dose x its annotated target: does target expression predict "
                                          "who is killed (rho, calibrated z, q)")], deeper_queries(fx.out))


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
        va = np.fmax(va, vr)             # the group's spread floored at the rest's (a few lines agree by chance)
        se2 = va / np.maximum(na, 1) + vr / np.maximum(nr, 1)
        t = (ma - mr) / np.sqrt(np.where(se2 > 0, se2, np.nan))
        df = se2 ** 2 / ((va / np.maximum(na, 1)) ** 2 / np.maximum(na - 1, 1) +
                         (vr / np.maximum(nr, 1)) ** 2 / np.maximum(nr - 1, 1))
        p = 2 * t_sf(np.abs(t), df)
        p[(na < 3) | (nr < 3)] = np.nan
        q = T.bh(p)
        for j in np.flatnonzero(np.isfinite(p)):
            i = elig[j]
            arows.append((fname, int(m.sum()), int(na[j]), int(m.sum()) <= 4, dd.at[i, "drug"], dd.at[i, "conc"],
                          dd.at[i, "moa_fine"], float(ma[j]), float(mr[j]), float(ma[j] - mr[j]), float(t[j]),
                          float(p[j]), float(q[j])))
    assoc = pd.DataFrame(arows, columns=["feature", "n_group_lines", "n_group_lines_measured", "small_group", "drug",
                                         "conc", "moa_fine", "group_mean_beta", "rest_mean_beta", "difference", "t",
                                         "p", "q_within_feature"])
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
The feature tests are Welch t-tests with the group's variance floored at the rest's; small_group marks features
of <= 4 lines (n_group_lines): such a group can differ by chance, so report it only with a large,
consistent difference and say that it is a small group.
""", [("drug_response_heterogeneity.csv", "per drug-dose with >= 20 significant genes: median and spread (IQR) of "
                                          "beta across lines, weakest and strongest lines, link to growth"),
      ("line_response_matrix.parquet", "every eligible drug-dose x line: beta, correlation r, growth (log2)"),
      ("feature_response_top.csv", "top 1,000 associations: feature (driver, protein change, organ, gene loss) x "
                                   "drug-dose, group size (small_group: <= 4 lines), group vs rest mean beta, "
                                   "Welch t (group variance floored at the rest's), p, q (within feature and overall)"),
      ("feature_response_associations.parquet", "all of them"),
      ("line_responsiveness.csv", "per line: typical beta over strong drug-doses, weakest and strongest responses"),
      ("line_by_mechanism_beta.csv", "mean beta per mechanism (>= 3 drugs) x line")], deeper_queries(fx.out))


def composition_matrix(fx):
    """wells x lines: the composition shift of every profile (effects/composition_shift.parquet; 0 when absent)."""
    S = np.zeros((len(fx.wells), len(fx.lines)), dtype=np.float32)
    path = os.path.join(fx.d, "composition_shift.parquet")
    if os.path.exists(path):
        t = pd.read_parquet(path)
        wi = t["sample"].astype(str).map({s: i for i, s in enumerate(fx.wells["sample"])})
        li = t["cell_line_id"].astype(str).map({s: i for i, s in enumerate(fx.lines["cell_line_id"].astype(str))})
        ok = wi.notna() & li.notna()
        S[wi[ok].to_numpy(dtype=int), li[ok].to_numpy(dtype=int)] = t.loc[ok, "shift_log2"].to_numpy()
    return S


def per_line_columns(fx, specs, gene_cols=None):
    """Re-read the pseudobulk for a few columns (each = list of tokens summed) and return per-line corrected
    effects per drug-dose (drug-doses x lines x C), by the steps of 'effects': plate baseline, composition shift,
    position correction, mean over the drug-dose's used wells. gene_cols {name: column} marks tested genes: their
    non-expressing lines are left out and their own position correction (W1 - W2) is used; other columns (program
    sums) get the two-pass correction on their own values, with the stored pass-1 plate factors."""
    gene_cols = gene_cols or {}
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
    names = list(specs)
    em = np.ones((L, C), dtype=bool)
    for j, nm in enumerate(names):
        if nm in gene_cols:
            em[:, j] = np.asarray(fx.expr_mask)[:, gene_cols[nm]]
    Y = log_cpm(counts, tot, nc)
    Y[:, ~em] = np.nan
    S = composition_matrix(fx)
    r1 = np.full_like(Y, np.nan)
    for p in fx.plates:
        rows = np.flatnonzero((w["plate"] == p).to_numpy())
        drug = rows[fx.drug_w[rows]]
        base = np.nanmedian(Y[drug], axis=0)
        r1[rows] = Y[rows] - base[None] - S[rows][:, :, None]
    W1 = np.nanmedian(r1, axis=1)
    W1[np.isfinite(r1).sum(axis=1) < MIN_LINES] = np.nan
    eff = np.zeros((N, C), dtype=np.float32)
    own = [j for j, nm in enumerate(names) if nm in gene_cols]
    for j in own:
        col = gene_cols[names[j]]
        eff[:, j] = np.nan_to_num(np.asarray(fx.W1)[:, col] - np.asarray(fx.W2)[:, col])
    other = [j for j in range(C) if j not in own]
    if other:
        slot, dname = w["slot"].to_numpy(dtype=float), w["drug"].to_numpy(dtype=object)
        f1 = w["plate_scale_pass1"].to_numpy(dtype=float) if "plate_scale_pass1" in w else np.ones(N)
        X = W1[:, other]
        e1, _, _ = loo_effect(X, slot, dname, fx.drug_w)
        c, s = robust_cols(X - e1, fx.ref_w)
        clean = np.abs((X - e1 - c) / (s * f1[:, None])) < POS_CLEAN_Z
        eff[:, other] = loo_effect(X, slot, dname, fx.drug_w, clean=clean)[0]
    # a well without a value for the column (< MIN_LINES lines) adds nothing per line either: the same wells as the
    # drug-dose's fold change
    r2 = np.where(np.isfinite(W1)[:, None, :], r1 - eff[:, None, :], np.nan)
    out = np.full((len(fx.dd), L, C), np.nan, dtype=np.float32)
    for d, ii in fx.wells_of_dd.items():
        if len(ii):
            out[d] = np.nanmean(r2[ii], axis=0)
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


def empirical_null_z(rho, n, ref):
    """Fisher z of a Spearman rho across n lines, robust-centred and scaled over the reliable drug-doses `ref`
    (T.robust_center_scale) before p: an empirical null. Correlated genes and drugs that deplete fast-growing lines
    shift every rho, so the textbook N(0, 1) null is far too permissive here. Returns (z_fisher, z, p)."""
    zf = np.arctanh(np.clip(np.asarray(rho, dtype=float), -0.999, 0.999)) * math.sqrt(max(n - 3, 1))
    c, s = T.robust_center_scale(zf[np.asarray(ref, dtype=bool)])
    z = (zf - c) / s
    return zf, z, 2 * norm_sf(np.abs(z))


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
            "cells_x_of_plate", "cells_log2_vs_plate", "row_cells_log2", "umi_per_cell_log2_vs_plate",
            "row_umi_per_cell_log2", "genes_per_cell_log2_vs_plate", "n_sig_genes", "flags", "cell_cycle_call"]
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
    pr["z_fisher"], pr["z"], pr["p"] = empirical_null_z(pr["spearman_growth_vs_proliferation"], n,
                                                         ~fx.dd["unreliable_plate_only"].to_numpy(dtype=bool))
    pr["q"] = T.bh(pr["p"].to_numpy())
    pr["n_sig_genes"] = fx.dd["n_sig_genes"]
    pr["flags"] = fx.dd["flags"]
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
(cells_x_of_plate; read it with row_cells_log2 and the flags: 'toxic' = dose-consistent loss beyond the plate row,
weak evidence alone at the top dose (one well's cell count); 'low cells (technical?)' = not confirmed: the plate
row lost cells (technical), a non-monotonic dose response (antimitotics: the lower dose kills, the higher one
arrests) or a row of toxic neighbours, so judge it with the dose series and the drug's significant genes;
'plate-row cell shift' = the whole row moved, confirm on another plate) and which kill fast-growing lines
more (proliferation-dependent killing; its z is calibrated against all drug-doses), and which genes' drug
responses mostly reflect cell-cycle composition (so 'inductions' of those genes by cycle-arresting drugs should not
be trusted). Use known drugs as a check (taxanes, vinca alkaloids, Aurora/PLK inhibitors -> G2/M; antimetabolites
-> S phase; CDK4/6 inhibitors -> fewer cycling cells; transcription inhibitors -> transcription drop).
""", [("drug_cell_cycle.csv", "per drug-dose: S and G2M module shifts (log2, z), cells (x of plate median), "
                              "transcription (UMIs/genes per cell), significant genes, flags, call"),
      ("proliferation_dependent_drugs.csv", "per drug-dose: Spearman across lines of growth vs proliferation (G2M "
                                            "level), z (Fisher z robust-centred and scaled over all reliable "
                                            "drug-doses: an empirical null; z_fisher = the uncalibrated one), p, q, "
                                            "significant genes, flags; negative = fast-cycling lines depleted more"),
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
    dd["flags"] = gene_flag_col(fx, c)             # the drug-dose's flags + this gene's position / plate flags
    dd["plate_scale_gene"] = fx.gene_plate_scale(c)
    dd["position"] = position_flag(fx, c)
    if hasattr(fx, "DD_poseff"):
        dd["position_effect_removed"] = np.asarray(fx.DD_poseff)[:, c]
    if per_line is not None:                       # expressing lines only (per_line_columns applies expr_mask)
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
    lv["z_fisher"], lv["z"], lv["p"] = empirical_null_z(lv["spearman_growth_vs_level"], use.sum(),
                                                         ~fx.dd["unreliable_plate_only"].to_numpy(dtype=bool))
    lv["q"] = T.bh(lv["p"].to_numpy())
    lv["n_sig_genes"] = fx.dd["n_sig_genes"]
    lv["flags"] = fx.dd["flags"]
    lv.sort_values("z").to_csv(os.path.join(folder, "level_vs_growth.csv"), index=False)
    files = [("drug_effects.csv", "every drug-dose: fold change, z, q up/down, z at each dose, dose pattern, flags "
                                  "(the drug-dose's plus this gene's position flags; position: 'uncertain' / 'not "
                                  "correctable' / the effect removed), % of the expressing lines up, replicate_r, "
                                  "context (S_PHASE_z, G2M_PHASE_z, PROTEASOME_z, cells, UMIs, composition shift)"),
             ("coregulated_genes.csv", f"correlation with every gene across drug wells: raw, minus {N_PCS} and minus "
                                       "10 broad components (strong real modules can also be components: compare), "
                                       "and the data-driven program each gene belongs to (see ../programs/)"),
             ("baseline_by_line.csv", "level in each line (all wells pooled), vs the median line, expressing flag"),
             ("level_vs_growth.csv", "does a line's level of this gene predict how a drug-dose affects its growth "
                                     "(Spearman across lines; z = Fisher z robust-centred and scaled over all reliable "
                                     "drug-doses (empirical null; z_fisher uncalibrated), p, q; negative = "
                                     "high-expressing lines depleted more)")]
    if os.path.exists(lsd):
        files.append(("loss_selective_drugs.csv", "drugs that deplete the lines not expressing this gene more than "
                                                  "the other lines in the same wells"))
    lsd_ref = "" if os.path.exists(lsd) or gene.upper() == "MTAP" else \
        f" For {gene} that file is ../focus_MTAP/loss_selective_drugs.csv."
    write_brief(folder, f"Focus gene {gene}", f"""
Everything the data say about {gene}: which drugs raise or lower it (and whether each effect is clean: dose-consistent,
broad across lines, not toxic, not shutdown, not cell-cycle composition, not part of a broad program), what it is
co-regulated with (and so what probably controls it), which lines lack or over-express it, and whether its level or
loss creates selective vulnerabilities. For context, the earlier MTAP / Gankyrin analysis of these data was
inconclusive: no drug convincingly raised MTAP or Gankyrin (PSMD10). Test this without assuming it: for every
candidate increase give the dose pattern, flags, S_PHASE_z / G2M_PHASE_z and PROTEASOME_z (a PSMD10 rise that comes
with the whole proteasome is not Gankyrin-specific) and umi_per_cell_log2_vs_plate (check across the inert wells
whether this gene's z falls with sequencing depth: then a rise in a low-UMI well is suspect), and say whether its
wells agree. Also check whether the
MTAP-null lines are selectively depleted by antifolates (pemetrexed; loss_selective_drugs.csv).{lsd_ref}
""", files, deeper_queries(fx.out))


def cmd_angles(args):
    quiet()
    D = dirs(args.out)
    fx = FX(args.out)
    sel = [a.strip() for a in args.angles.split(",") if a.strip()] if args.angles else ANGLES + ["focus"]
    failed = []
    stamp = os.path.join(D["ang"], "complete.json")       # written last: 'tahoe status' and the agents need it
    try:
        os.remove(stamp)
    except FileNotFoundError:
        pass
    _BRIEF["focus"] = [g.strip() for g in args.focus_genes.split(",") if g.strip()]
    try:                                    # the facts of this run that every brief states
        _BRIEF["notes"] = brief_notes(fx)
    except Exception:  # noqa: BLE001
        _BRIEF["notes"] = None
        log(f"  note: could not collect the run facts for the briefs (generic text used):\n{traceback.format_exc()}")
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
            drop_stale_brief(folder)
            log(f"  ERROR in angle {a} (the other angles continue):\n{traceback.format_exc()}")
    focus = [g.strip() for g in args.focus_genes.split(",") if g.strip()] if "focus" in sel else []
    if focus:
        specs, cols = {}, {}
        for gname in focus:
            c = fx.col_of(gname)
            if c is not None and fx.gmask[c]:
                specs[gname] = [int(fx.genes.at[c, "token"])]
                cols[gname] = c
        per = {}
        if specs:
            log(f"  per-line effects for focus genes: {', '.join(specs)} ...")
            per_dd = per_line_columns(fx, specs, cols)
            per = {gname: per_dd[:, :, j] for j, gname in enumerate(specs)}
        for gname in focus:
            folder = os.path.join(D["ang"], f"focus_{safe_name(gname)}")
            os.makedirs(folder, exist_ok=True)
            log(f"Focus: {gname} ...")
            try:
                angle_focus(fx, folder, gname, per.get(gname))
            except Exception:  # noqa: BLE001
                failed.append(f"focus_{gname}")
                drop_stale_brief(folder)
                log(f"  ERROR in focus {gname}:\n{traceback.format_exc()}")
    with open(stamp, "w", encoding="utf-8") as fh:
        json.dump({"effects_version": EFFECTS_VERSION, "angles": sel, "failed": failed,
                   "written": time.strftime("%Y-%m-%d %H:%M:%S")}, fh)
    log(f"Angles done -> {D['ang']}" + (f"; FAILED: {', '.join(failed)} (their old briefs removed: no agent runs "
                                         "on them)" if failed else ""))


def drop_stale_brief(folder):
    """An angle that failed keeps no brief.md from an earlier run (its tables and text describe other numbers)."""
    try:
        os.remove(os.path.join(folder, "brief.md"))
    except OSError:
        pass


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


_SCRIPT = r"tahoe_(?:atlas|gene_panel|mtap_gankyrin)\.py"
SCRIPT_REF = re.compile(rf"'([^'\n]*{_SCRIPT})'|\"([^\"\n]*{_SCRIPT})\"|([^\s`'\"]*{_SCRIPT})")  # as tahoe_status.py


def stale_brief_scripts(jobs):
    """{path: [job names]} for absolute tahoe_*.py paths named in the jobs' briefs that no longer exist: briefs
    written from a copy of the scripts that has since been deleted would send the agents to a missing look-up."""
    bad = {}
    for j in jobs:
        try:
            with open(j["brief"], encoding="utf-8", errors="replace") as fh:
                txt = fh.read()
        except OSError:
            continue
        for m in SCRIPT_REF.finditer(txt):         # quoted paths may hold spaces ('.../my copy/tahoe_atlas.py')
            p = next(x for x in m.groups() if x)
            if os.path.isabs(p) and not os.path.exists(p):
                bad.setdefault(p, []).append(j["name"])
    return bad


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
    ("effects/lines.csv", None), ("effects/wells.csv", None), ("effects/plate_scale.csv", None),
    ("effects/composition_shift.parquet", None), ("effects/genes.csv", None), ("effects/README_effects.md", None),
    ("effects/failed_wells.csv", None), ("effects/plates.csv", None),
    ("angles/quality/summary.json", None), ("angles/quality/position_effects.csv", None),
    ("angles/quality/plate_dmso_offsets.csv", None), ("angles/quality/replicates.csv", None),
    ("angles/quality/replicate_by_plate_pair.csv", None), ("angles/quality/calibration_by_plate.csv", None),
    ("angles/quality/composition_shifts.csv", None), ("angles/quality/position_not_correctable_wells.csv", None),
    ("angles/quality/position_sensitive_genes.csv", 300), ("angles/quality/calibration_by_gene.csv", 500),
    ("angles/quality/calibration_by_plate_gene.csv", None), ("angles/quality/calibration_growth_by_plate.csv", None),
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
    ("angles/cell_state/drug_cell_cycle.csv", None), ("angles/cell_state/proliferation_dependent_drugs.csv", None),
]
FOCUS_DIAGNOSTICS = [("drug_effects.csv", None), ("coregulated_genes.csv", 400), ("baseline_by_line.csv", None),
                     ("loss_selective_drugs.csv", 300), ("level_vs_growth.csv", None)]


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
        for f in sorted(glob.glob(os.path.join(D["ang"], "*", "brief.md"))):      # what each agent is told
            z.write(f, os.path.join("briefs", os.path.basename(os.path.dirname(f)) + ".md"))
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
    own = D is None                        # the atlas's own angles (not another script's folders)
    D = D or dirs(args.out)
    os.makedirs(D["rep"], exist_ok=True)
    jobs = agent_jobs(D, args, order, append)
    if not jobs:
        sys.exit(f"No folders with a brief.md under {D['ang']} (atlas: run 'angles' first)")
    cj = os.path.join(args.out, "effects", "complete.json")
    old = [j["name"] for j in jobs
           if own and os.path.exists(cj) and os.path.getmtime(j["brief"]) < os.path.getmtime(cj)]
    if old:                                # briefs (and tables) of an earlier effects run: other numbers
        msg = (f"{len(old)} brief(s) are older than the effects ({', '.join(old[:4])}{' ...' if len(old) > 4 else ''}"
               f"): run 'angles' first (minutes), then 'agents' again")
        if not args.dry_run:
            sys.exit(msg)
        log("  WARNING: " + msg)
    todo = [j for j in jobs if args.redo or not up_to_date(j)]
    stale = stale_brief_scripts(todo)
    if stale:
        p, names = next(iter(stale.items()))
        msg = (f"The briefs ({', '.join(names[:3])}{' ...' if len(names) > 3 else ''}) name {p}, which no longer "
               "exists (written from a copy since deleted or moved): rewrite them with the current scripts first "
               "('angles' for the atlas, 'analyze' for the gene panel; minutes), then run 'agents' again")
        if not args.dry_run:
            sys.exit(msg)
        log("  WARNING: " + msg)
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
    ap.add_argument("--unreliable-plates", default=None,
                    help="effects: plates whose wells do not reproduce, kept out of pooled drug-doses, centres and "
                         "plate-factor peers (comma list, or 'none'; default: " + ",".join(UNRELIABLE_PLATES)
                         + " when present)")
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
    if args.command == "angles":            # the redo path (effects, then angles): the bundle follows the briefs
        cmd_bundle(args)
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
