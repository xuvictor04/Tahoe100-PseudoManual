#!/usr/bin/env python3
"""Two-way test of TRIM72 (MG53) vs p53 output with the TP53 genotype as the control (the scaled-up D1 test), and
the same model as a screen of other MG53-linked pathways (D2). Tahoe-100M only (no new data), method-v3 effects.

Tahoe has no MG53 perturbation and measures mRNA, so every estimate here is an ASSOCIATION between TRIM72 mRNA and
read-out mRNA across cell lines inside the same drug-doses. p53 activity is read from p53-target mRNA. An MG53 -> p53
effect can only act where p53 works, so the primary estimand is the TRIM72 slope in TP53-WT lines MINUS the slope in
TP53-altered lines; what is equal in both groups is not via p53.

Unit: one (drug-dose, cell line) cell = the method-v3 corrected log2 effect r2 (plate x line baseline -> composition
shift -> two-pass position correction; per (well, line) from the panel's own T.expression_effects, or from
upstream_coregulation.corrected_effects() on atlas/pseudobulk for genes outside the panel), averaged over the
drug-dose's used wells (profiles with >= 30 cells). Model, per read-out Y, over every drug-dose x line cell with all
values present:

    Y = FE + b_WT * TRIM72 * WT + b_alt * TRIM72 * altered + sum_k (c_k,WT * C_k * WT + c_k,alt * C_k * altered) + e

FE, two structures, both reported (column fe): 'dd' = drug-dose FE + line FE (as specified); 'ddxg' = drug-dose x
TP53-group FE + line FE. With 'dd' the WT-only p53 response of each drug-dose stays in the WT residuals and, wherever
the drug-dose's TRIM72 response also differs between the groups, that drug-level gap enters b_WT - b_alt (the TP53
label permutation breaks the gap, so it does not protect against it). 'ddxg' compares lines only with lines of the
same TP53 group in the same wells; it is the preferred reading of D1.
C (per drug-dose x line): DD_beta (the line's strength of the drug's consensus response; 0 where the drug-dose has
< 20 significant genes and no consensus), DD_A (relative abundance: depletion), the line's S and G2M effects
(DD_r2_modules), and the line's mean |r2| over non-p53, non-screen panel genes (general responsiveness). Sensitivity
sets add the line's untreated TRIM72 level x the drug-dose's TRIM72 effect (full_base: fold inflation of
low-baseline lines) or the line's p53 responsiveness x the drug-dose's P53_ACTIVITY z (full_p53resp).
Estimand b_WT - b_alt (negative = more TRIM72 goes with less p53 output only where p53 works).

PRIMARY TEST (declared here and in the tables; every other fe x variant x covariate-set row is a sensitivity
analysis, column 'role' of d1_two_way_models.csv and key_results.csv): fe 'ddxg', variant i_all (all 1,132
drug-doses), covariate set 'full', read-out P53_SCORE, estimand b_WT - b_alt, inference by the conservative two-way
SE below. It was written down in the verifier round, after a first run, but it is the design the step specified from
the start (i_all = the data set as specified, ddxg = the FE structure already named the preferred reading of D1,
full = the specified covariates, P53_SCORE = the p53 read-out), not one picked for its result: not preregistered.
The other D1 read-outs of that model are secondary; P53_SCORE over the 9 variants also gets a Holm adjustment
(p_holm_variants_*).

Inference: cluster-robust SE by drug compound (CR1), by line, and two-way (drug, line). Every reported two-way SE,
CI, p and q uses the conservative se = sqrt(max(V_drug + V_line - V_inter, V_drug, V_line)) (the plain two-way
variance can fall below a one-way variance; se_diff_twoway_cgm keeps that plain value for the diff). A permutation
null that shuffles TRIM72 across lines within each FE cell (keeps the drug structure; tests b = 0); a TP53-label
permutation over lines (group sizes kept, the whole model refitted: for 'dd' through per-line Gram blocks, for
'ddxg' as two within-group two-way-FE regressions on the drug-dose x line grid), studentised by the line-cluster
SE. Both engines reproduce the main fit at the true labels (checks.csv). Minimum detectable b_WT - b_alt (80%
power, two-sided 5%) = 2.80 x the label-permutation SD. Second stage: per-line TRIM72 slopes (line-specific
covariate slopes), WT vs altered mean (Welch; label permutation of the Welch t) and ranks (Mann-Whitney,
Hodges-Lehmann shift). Which drug-doses and lines carry the estimate: per drug-dose contributions; leave-one-drug-out
and leave-one-line-out (active set); the active set inside one model with all drug-doses (line FE estimated from all
of them; separate active / inactive slopes and covariate slopes) and the difference-in-differences active minus
inactive.

Variants (D1): (i) all drug-doses; (ii) drug-doses that move TRIM72 (|z| >= 3) or activate p53 (P53_ACTIVITY
z >= 3), also each part alone and without the plate-3/13 wells; (iii) readthrough: iii_readthrough_cov (all
drug-doses) and iii_readthrough_cov_active (active set) put FUS r2 and PYCARD-AS1 r2 into the model as covariates
x TP53 group (covariate set full_rt); iii_readthrough_subtracted (the earlier version) uses X = TRIM72 r2 minus its
fit on FUS and PYCARD-AS1 r2 (slopes within drug-dose and line, pooled over lines); (iv) without the plate-3 and
plate-13 wells; (v) TRIM72 measurement error: split-half (cells of each well x line split at random, the method run
on each half) and replicate-well reliability of the residual TRIM72 variation, and the implied attenuation of b.
D2 screen: the same model for each MG53-linked module of mg53_p53/gene_modules.csv (NF-kB,
ferroptosis, apoptosis, stress, PI3K-AKT/FOXO/FAK, cell cycle + E2F targets, RAC1); BH across the screen within
each FE structure. Gene-level null: the same model for every non-p53 panel gene and for random background modules
the size of P53_SCORE (is a TRIM72 x TP53-group pattern specific to p53 targets?); the 21 members as a set vs the
background genes by a camera-style test (variance inflated for the correlation between the genes' estimates).

    python3 two_way.py [--data DIR (default $MG53_DATA, $TAHOE_DATA or ~/Tahoe-100M)] [--recompute]
                       [--perm 1000] [--label-perm 2000] [--screen-perm 500] [--screen-label-perm 1000]
                       [--modules 500] [--quick]

Reads <data>/atlas/effects, <data>/atlas/pseudobulk (one streamed pass over 20 GB: I/O-bound, 11-13 min from a
cold page cache), <data>/gene_panel (well_line, cells/*.parquet for the split-half, ~1 min; results/),
<data>/metadata/gene_metadata.parquet. A from-scratch run (empty cache/, cold page cache) took 29 min: 14 min of
caches, 16 min of models (4 CPUs shared with another job; peak RSS 1.4 GB); with the caches in place ~15 min (see
README below for the breakdown). The caches are keyed to the
inputs (cache/manifest.json: real path of --data, sizes and mtimes of atlas/effects/wells.csv,
atlas/pseudobulk/group*, gene_panel/well_line.parquet and gene_panel/cells) and rebuilt when they do not match.
Writes tables to $MG53_OUT/tables (default <this folder>/tables) and caches to $MG53_OUT/cache (default <this
folder>/cache); nothing under the data folder. numpy / pandas / scipy (+ pyarrow for the per-cell files) only.
"""
import argparse
import contextlib
import glob
import json
import os
import resource
import sys
import time
import warnings

# BLAS threads: with all cores busy (another job on the machine) a 4-thread OpenBLAS ran the tall-skinny products of
# this script up to 40x slower than 1-2 threads; set before numpy loads, and overridable from the environment
for _v in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "2")
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
from scipy import sparse, stats  # noqa: E402

sys.dont_write_bytecode = True        # no __pycache__ written into the sibling step folders imported below
HERE = os.path.dirname(os.path.abspath(__file__))
MGDIR = os.path.dirname(HERE)
REPO = os.path.dirname(MGDIR)
for _p in (REPO, os.path.join(MGDIR, "downstream_p53"), os.path.join(MGDIR, "upstream_coregulation")):
    if _p not in sys.path:
        sys.path.insert(0, _p)
import downstream_p53 as DP          # noqa: E402  (the panel effects cache, P53 score, NOT_BACKGROUND)
import upstream_coregulation as UC   # noqa: E402  (corrected_effects() for atlas-pseudobulk genes)

P, T = DP.P, DP.T
GENE = "TRIM72"
SEED = 20261025
Z80 = stats.norm.ppf(0.975) + stats.norm.ppf(0.80)         # 2.80: MDE = Z80 x null SD
D1 = ["P53_SCORE", "MDM2", "CDKN1A", "FDXR", "ZMAT3", "DDB2", "TP53I3", "BBC3", "TP53"]
E2F = ["E2F1", "CCNE1", "CDT1", "MCM3", "MCM7", "MYBL2", "CDC25A"]    # E2F targets outside the S_PHASE module
# (module, panel.csv module, genes, also a module score (same expected direction), covariate set)
SCREEN = [("NF-kB", "screen_NFkB", ["NFKBIA", "TNFAIP3", "CXCL8"], True, "full"),
          ("ferroptosis", "screen_ferroptosis", ["SLC7A11", "GPX4", "CHAC1"], False, "full"),
          ("apoptosis", "screen_apoptosis (+ PMAIP1)", ["BAX", "MCL1", "PMAIP1"], False, "full"),
          ("stress (ISR)", "stress_markers", ["ATF3", "DDIT3"], True, "full"),
          ("PI3K-AKT / FOXO / FAK", "screen_PI3K_AKT_FAK", ["TXNIP", "IRS1", "PTK2"], False, "full"),
          ("cell cycle", "screen_cell_cycle", ["CCND1", "KIF11"], False, "no_cycle"),
          ("E2F targets", "screen_cell_cycle (E2F targets added)", E2F, True, "no_cycle"),
          ("RAC1", "screen_RAC1", ["RAC1"], False, "full")]
SCREEN_GENES = sorted({g for s in SCREEN for g in s[2]})
VALIDATE = ["TRIM72", "MDM2", "CDKN1A", "NFKBIA"]           # also taken from the pseudobulk: checked vs the panel
PB_UNMASKED = {"PYCARD-AS1"}                               # below the atlas gene list: r2 kept in every line
COVSETS = {"full": ["beta", "A", "S", "G2M", "bg_abs_r2"], "no_cycle": ["beta", "A", "bg_abs_r2"], "none": [],
           "full_base": ["beta", "A", "S", "G2M", "bg_abs_r2", "trim72_base_x_dd"],
           "full_p53resp": ["beta", "A", "S", "G2M", "bg_abs_r2", "p53resp_x_dd"],
           "full_rt": ["beta", "A", "S", "G2M", "bg_abs_r2", "FUS", "PYCARD-AS1"]}
FES = ("dd", "ddxg")
FE_NAME = {"dd": "drug-dose + line FE (as specified)", "ddxg": "drug-dose x TP53-group + line FE"}
DROP_PLATES = ("plate3", "plate13")
# the primary test, declared up front; everything else is secondary (other read-outs of this model), sensitivity
# (other fe x variant x covariate set) or a check
PRIMARY = {"fe": "ddxg", "variant": "i_all", "covset": "full", "readout": "P53_SCORE"}
# each D1 variant at its main covariate set: the Holm family for P53_SCORE (per fe)
VARIANT_MAIN_COVSET = {"i_all": "full", "ii_active": "full", "ii_trim72": "full", "ii_p53": "full",
                       "ii_active_no_plate3_13": "full", "iii_readthrough_subtracted": "full",
                       "iii_readthrough_cov": "full_rt", "iii_readthrough_cov_active": "full_rt",
                       "iv_no_plate3_13": "full"}
CACHE_VERSION = 1           # bump when a cache builder changes


@contextlib.contextmanager
def quiet():
    with warnings.catch_warnings(), np.errstate(invalid="ignore", divide="ignore"):
        warnings.simplefilter("ignore", RuntimeWarning)
        yield


def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


def peak_gb():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6


bh = DP.bh


def holm(p):
    """Holm step-down adjusted p (NaN kept)."""
    p = np.asarray(p, float)
    out = np.full(len(p), np.nan)
    ok = np.isfinite(p)
    if ok.any():
        q = p[ok]
        m = len(q)
        o = np.argsort(q, kind="stable")
        adj = np.minimum(1.0, np.maximum.accumulate((m - np.arange(m)) * q[o]))
        r = np.empty(m)
        r[o] = adj
        out[ok] = r
    return out


def se_conservative(vd, vl, vi):
    """Two-way (drug, line) cluster SE, conservative: sqrt(max(V_drug + V_line - V_inter, V_drug, V_line)). Also the
    plain Cameron-Gelbach-Miller value (sqrt(V2), or the larger one-way SE where V2 <= 0: the earlier column) and
    which term gave the maximum. Works elementwise on arrays."""
    vd, vl, vi = (np.asarray(v, float) for v in (vd, vl, vi))
    v2 = vd + vl - vi
    m = np.maximum(v2, np.maximum(vd, vl))
    src = np.where(m == v2, "twoway", np.where(m == vd, "drug", "line"))
    with quiet():
        cgm = np.where(v2 > 0, np.sqrt(np.where(v2 > 0, v2, 0.0)), np.sqrt(np.maximum(vd, vl)))
    return np.sqrt(np.maximum(m, 0.0)), cgm, src


# ============================================================================= cache manifest (keyed to the inputs)
def cache_manifest(data):
    """What the caches are built from: the real path of --data and size + mtime of the input files they read."""
    def st(p):
        try:
            s = os.stat(p)
            return [int(s.st_size), int(s.st_mtime_ns)]
        except OSError:
            return None
    files = {}
    for rel in [os.path.join("atlas", "effects", "wells.csv"), os.path.join("gene_panel", "well_line.parquet")] + \
            sorted(os.path.relpath(p, data) for p in glob.glob(os.path.join(data, "atlas", "pseudobulk", "group*"))):
        files[rel] = st(os.path.join(data, rel))
    cells = glob.glob(os.path.join(data, "gene_panel", "cells", "*.parquet"))
    cst = [os.stat(p) for p in cells]
    return {"cache_version": CACHE_VERSION, "data_realpath": os.path.realpath(data), "files": files,
            "gene_panel/cells/*.parquet": [len(cst), int(sum(s.st_size for s in cst)),
                                           int(max((s.st_mtime_ns for s in cst), default=0))]}


def cache_files(cdir):
    return (glob.glob(os.path.join(cdir, "*.np[yz]")) + glob.glob(os.path.join(cdir, "*.parquet"))
            + ([os.path.join(cdir, "panel")] if os.path.isdir(os.path.join(cdir, "panel")) else []))


def validate_caches(cdir, data, recompute):
    """Delete the caches when --recompute is given or when cache/manifest.json does not match the current inputs
    (or is missing); returns the manifest to write once the caches are rebuilt."""
    import shutil
    want = cache_manifest(data)
    mp = os.path.join(cdir, "manifest.json")
    have = None
    if os.path.exists(mp):
        try:
            with open(mp, encoding="utf-8") as fh:
                have = json.load(fh)
        except (OSError, ValueError):
            have = None
    old = cache_files(cdir)
    if recompute or have != want:
        if old:
            if recompute:
                why = "--recompute"
            elif have is None:
                why = "no cache/manifest.json"
            else:
                diff = [k for k in ("cache_version", "data_realpath", "gene_panel/cells/*.parquet")
                        if have.get(k) != want[k]]
                diff += [k for k in sorted(set(want["files"]) | set(have.get("files", {})))
                         if have.get("files", {}).get(k) != want["files"].get(k)]
                why = "inputs changed: " + ", ".join(diff[:6]) + (" ..." if len(diff) > 6 else "")
            log(f"rebuilding the caches ({why})")
            for f in old:
                if os.path.isdir(f):
                    shutil.rmtree(f, ignore_errors=True)
                else:
                    os.remove(f)
        if os.path.exists(mp):
            os.remove(mp)
    return want


def write_manifest(cdir, man):
    mp = os.path.join(cdir, "manifest.json")
    with open(mp + ".tmp", "w", encoding="utf-8") as fh:
        json.dump(man, fh, indent=1)
    os.replace(mp + ".tmp", mp)


# ============================================================================= grid: drug-doses x lines (atlas order)
class Grid:
    def __init__(self, data):
        fxd = os.path.join(data, "atlas", "effects")
        self.fxd = fxd
        self.w = pd.read_csv(os.path.join(fxd, "wells.csv"), dtype={"sample": str, "plate": str})
        self.dd = pd.read_csv(os.path.join(fxd, "drugdose.csv"))
        self.lines = pd.read_csv(os.path.join(fxd, "lines.csv"), dtype={"cell_line_id": str})
        self.L = self.lines["cell_line_id"].tolist()
        self.nd, self.nw, self.nl = len(self.dd), len(self.w), len(self.L)
        used = self.w["used_in_drugdose"].astype(str).str.lower().eq("true").to_numpy()
        ddr = self.w["drugdose_row"].to_numpy()
        self.used = used & (ddr >= 0)
        self.ddr = ddr
        self.B = self.agg(np.ones(self.nw, bool))
        self.drug_id = pd.factorize(self.dd["drug"])[0]
        self.plate = self.w["plate"].astype(str).to_numpy()

    def agg(self, keep):
        """drug-doses x wells, 1 for the used wells that are kept."""
        m = self.used & keep
        return sparse.csr_matrix((np.ones(m.sum()), (self.ddr[m], np.flatnonzero(m))), shape=(self.nd, self.nw))

    @staticmethod
    def dd_mean(B, V):
        """nanmean over each drug-dose's wells of a wells x lines array."""
        f = np.isfinite(V)
        num = B @ np.where(f, V, 0.0)
        den = B @ f.astype(float)
        with quiet():
            return np.where(den > 0, num / den, np.nan)


# ============================================================================= caches
def build_panel_cache(data, cdir):
    """The panel's per (well, line) effects of all 116 panel genes (downstream_p53's builder, into our cache)."""
    pdir = os.path.join(cdir, "panel")
    need = ("effects.npz", "wells.csv", "lines.csv", "meta.json", "drug_effects_all_genes.csv.gz")
    if not all(os.path.exists(os.path.join(pdir, f)) for f in need):
        log("panel effects cache: T.expression_effects for every panel gene (~2 min)")
        DP.build_effects_cache(data, pdir)
    return DP.Eff(pdir)


def npy_layout(path):
    a = np.load(path, mmap_mode="r")
    if not a.flags.c_contiguous:
        raise ValueError(f"{path}: expected a C-ordered array")
    out = (int(a.offset), tuple(a.shape), a.dtype)
    del a
    return out


def build_pseudobulk_cache(data, cdir, grid):
    """One streamed pass over atlas/pseudobulk/groupNNN.npy: per atlas well x line counts of the extra genes, total
    counts and cells; (sample, line) profiles split over group files are summed."""
    out = os.path.join(cdir, "pseudobulk_counts.npz")
    if os.path.exists(out):
        return dict(np.load(out, allow_pickle=False))
    t0 = time.time()
    gm = pd.read_parquet(os.path.join(data, "metadata", "gene_metadata.parquet"))
    tok_of = dict(zip(gm["gene_symbol"].astype(str), gm["token_id"].astype(int)))
    syms = [g for g in ["FUS", "PYCARD-AS1"] + [g for g in SCREEN_GENES if g not in DP_PANEL] + VALIDATE
            if g in tok_of]
    syms = list(dict.fromkeys(syms))
    toks = np.array([tok_of[g] for g in syms])
    wi = {s: i for i, s in enumerate(grid.w["sample"])}
    li = {l_: i for i, l_ in enumerate(grid.L)}
    C = len(syms)
    counts = np.zeros((grid.nw, grid.nl, C))
    tot = np.zeros((grid.nw, grid.nl))
    nc = np.zeros((grid.nw, grid.nl))
    nsrc = np.zeros((grid.nw, grid.nl), dtype=np.int16)
    pb = os.path.join(data, "atlas", "pseudobulk")
    files = sorted(glob.glob(os.path.join(pb, "group*_profiles.csv")))
    chunk = 256
    for f in files:
        prof = pd.read_csv(f, dtype={"sample": str, "cell_line_id": str})
        prof = prof[prof["sample"].isin(wi) & prof["cell_line_id"].isin(li)].sort_values("row")
        if prof.empty:
            continue
        npy = f.replace("_profiles.csv", ".npy")
        off, shape, dt = npy_layout(npy)
        G = shape[1]
        rb = G * dt.itemsize
        rows = prof["row"].to_numpy()
        a_w = prof["sample"].map(wi).to_numpy()
        a_l = prof["cell_line_id"].map(li).to_numpy()
        buf = np.empty((chunk, G), dtype=dt)
        with open(npy, "rb") as fh:
            for s0 in range(0, shape[0], chunk):
                n = min(chunk, shape[0] - s0)
                lo, hi = np.searchsorted(rows, [s0, s0 + n])
                if hi <= lo:
                    continue
                fh.seek(off + s0 * rb)
                got = fh.readinto(buf[:n])
                if got != n * rb:
                    raise IOError(f"{npy}: short read at row {s0}")
                sub = buf[rows[lo:hi] - s0][:, toks].astype(np.float64)
                np.add.at(counts, (a_w[lo:hi], a_l[lo:hi]), sub)
        np.add.at(tot, (a_w, a_l), prof["total_counts"].to_numpy(dtype=float))
        np.add.at(nc, (a_w, a_l), prof["n_cells"].to_numpy(dtype=float))
        np.add.at(nsrc, (a_w, a_l), 1)
        log(f"  pseudobulk {os.path.basename(npy)}: {len(prof)} profiles ({time.time() - t0:.0f} s)")
    res = {"counts": counts.astype(np.float32), "tot": tot, "nc": nc, "nsrc": nsrc, "symbols": np.array(syms),
           "tokens": toks, "samples": grid.w["sample"].to_numpy().astype(str), "lines": np.array(grid.L)}
    np.savez_compressed(out, **res)
    log(f"pseudobulk pass: {C} genes, {int((nsrc > 0).sum())} profiles, {int((nsrc > 1).sum())} split over 2+ "
        f"files ({time.time() - t0:.0f} s)")
    return res


def pseudobulk_effects(data, cdir, grid, pbc):
    """corrected_effects() (upstream_coregulation; the atlas's per_line_columns steps) per extra gene: r2 per (well,
    line) and per drug-dose. Lines left out as the atlas's expr_mask; PYCARD-AS1 (not in the atlas) kept in all."""
    out = os.path.join(cdir, "pseudobulk_effects.npz")
    if os.path.exists(out):
        z = np.load(out, allow_pickle=False)
        return {k: z[k] for k in z.files}
    t0 = time.time()
    UC.DATA = data
    UC.FXD = os.path.join(data, "atlas", "effects")
    syms = [str(s) for s in pbc["symbols"]]
    ag = pd.read_csv(os.path.join(grid.fxd, "genes.csv"))
    ag = ag[ag["kind"] == "gene"]
    col_of = dict(zip(ag["token"].astype(int), ag["col"].astype(int)))
    em = np.load(os.path.join(grid.fxd, "expr_mask.npy"), mmap_mode="r")
    expressed = np.ones((grid.nl, len(syms)), bool)
    in_atlas = np.zeros(len(syms), bool)
    for j, (g, tk) in enumerate(zip(syms, pbc["tokens"])):
        if g not in PB_UNMASKED and int(tk) in col_of:
            expressed[:, j] = np.asarray(em[:, col_of[int(tk)]], bool)
            in_atlas[j] = True
    with quiet():
        fx, r1, r2, W2, zw, per, ddl, ddz = UC.corrected_effects(pbc["counts"].astype(np.float64), pbc["tot"],
                                                                 pbc["nc"], expressed)
    res = {"r2": r2.astype(np.float32), "per": per.astype(np.float32), "ddl": ddl, "ddz": ddz,
           "symbols": np.array(syms), "expressed": expressed, "in_atlas": in_atlas}
    np.savez_compressed(out, **res)
    log(f"corrected_effects for {len(syms)} pseudobulk genes ({time.time() - t0:.0f} s)")
    return res


def build_split_half_counts(data, cdir):
    """Per (well, line): TRIM72 counts, UMIs and cells of two random halves of the cells (per-cell panel files)."""
    out = os.path.join(cdir, "split_half_counts.parquet")
    if os.path.exists(out):
        return pd.read_parquet(out)
    import pyarrow.parquet as pq
    t0 = time.time()
    files = sorted(glob.glob(os.path.join(data, "gene_panel", "cells", "*.parquet")))
    parts, acc = [], None
    for k, f in enumerate(files):
        t = pq.read_table(f, columns=["sample", "cell_line_id", "total_counts", GENE]).to_pandas()
        if t.empty:
            continue
        t["half"] = np.random.default_rng([SEED, k]).integers(0, 2, len(t)).astype(np.int8)
        t["n"] = 1
        parts.append(t.groupby(["sample", "cell_line_id", "half"], observed=True)[["n", GENE, "total_counts"]].sum())
        if len(parts) >= 200 or k == len(files) - 1:
            cur = pd.concat(parts + ([acc] if acc is not None else []))
            acc = cur.groupby(level=[0, 1, 2]).sum()
            parts = []
        if k % 500 == 0:
            log(f"  split-half: {k + 1}/{len(files)} cell files ({time.time() - t0:.0f} s)")
    if parts:
        cur = pd.concat(parts + ([acc] if acc is not None else []))
        acc = cur.groupby(level=[0, 1, 2]).sum()
    res = acc.reset_index()
    res.to_parquet(out, index=False)
    log(f"split-half counts: {len(files)} files, {int(res['n'].sum())} cells ({time.time() - t0:.0f} s)")
    return res


def split_half_effects(data, cdir, sh, grid):
    """The panel's T.expression_effects on each half (full n_cells as the >= 30-cell gate, as the main analysis):
    per (well, line) r2 of TRIM72 from half A and from half B."""
    out = os.path.join(cdir, "split_half_r2.npz")
    if os.path.exists(out):
        z = np.load(out, allow_pickle=False)
        return z["A"], z["B"], json.loads(str(z["check"]))
    import shutil
    t0 = time.time()
    with quiet():
        S = DP.panel_setup(data)
    base = S.wl[["sample", "cell_line_id", "n_cells", "total_counts", GENE]].copy()
    base["sample"] = base["sample"].astype(str)
    base["cell_line_id"] = base["cell_line_id"].astype(str)
    piv = sh.pivot_table(index=["sample", "cell_line_id"], columns="half", values=["n", GENE, "total_counts"],
                         aggfunc="sum", fill_value=0)
    key = pd.MultiIndex.from_frame(base[["sample", "cell_line_id"]])
    chk = {"profiles": int(len(base)),
           "max_abs_diff_cells_halfA_plus_halfB_vs_well_line": float(np.nanmax(np.abs(
               piv[("n", 0)].reindex(key).fillna(0).to_numpy() + piv[("n", 1)].reindex(key).fillna(0).to_numpy()
               - base["n_cells"].to_numpy()))),
           "max_abs_diff_TRIM72_counts_halfA_plus_halfB_vs_well_line": float(np.nanmax(np.abs(
               piv[(GENE, 0)].reindex(key).fillna(0).to_numpy() + piv[(GENE, 1)].reindex(key).fillna(0).to_numpy()
               - base[GENE].to_numpy())))}
    excl = P.gene_exclusions(S, GENE)
    arrs = []
    for h in (0, 1):
        nm = f"{GENE}_half{'AB'[h]}"
        wl = base[["sample", "cell_line_id", "n_cells"]].copy()
        wl["total_counts"] = piv[("total_counts", h)].reindex(key).fillna(0).to_numpy()
        wl[nm] = piv[(GENE, h)].reindex(key).fillna(0).to_numpy()
        wl = wl[wl["total_counts"] > 0]
        with quiet():
            _res, _W, d, _cal = T.expression_effects(wl, S.sm, nm, excl, None, S.drugs, method=S.M)
        m = d.pivot(index="sample", columns="cell_line_id", values="r2").reindex(index=grid.w["sample"],
                                                                                 columns=grid.L)
        arrs.append(m.to_numpy(dtype=np.float32))
    shutil.rmtree(getattr(S, "R", ""), ignore_errors=True)
    np.savez_compressed(out, A=arrs[0], B=arrs[1], check=np.array(json.dumps(chk)))
    log(f"split-half effects ({time.time() - t0:.0f} s)")
    return arrs[0], arrs[1], chk


# ============================================================================= the two-way fixed-effects engine
class FE:
    """Projection off drug-dose and line fixed effects (unbalanced): dd-demeaning (exact), then off the dd-demeaned
    line dummies (exact, by an orthonormal basis)."""

    def __init__(self, d, l_):
        n = len(d)
        self.du, dinv = np.unique(d, return_inverse=True)
        self.lu, linv = np.unique(l_, return_inverse=True)
        self.D = sparse.csr_matrix((np.ones(n), (np.arange(n), dinv)), shape=(n, len(self.du)))
        self.cnt = np.bincount(dinv).astype(float)
        Lm = np.zeros((n, len(self.lu)))
        Lm[np.arange(n), linv] = 1.0
        Ld = self.dd_demean(Lm)
        U, s, _ = np.linalg.svd(Ld, full_matrices=False)
        self.Q = U[:, s > s[0] * 1e-9]

    def dd_demean(self, V):
        one = V.ndim == 1
        V2 = V[:, None] if one else V
        out = V2 - self.D @ ((self.D.T @ V2) / self.cnt[:, None])
        return out[:, 0] if one else out

    def M(self, V):
        Vd = self.dd_demean(V)
        return Vd - self.Q @ (self.Q.T @ Vd)


def orth(A, tol=1e-9):
    if A.shape[1] == 0:
        return np.zeros((A.shape[0], 0))
    U, s, _ = np.linalg.svd(A, full_matrices=False)
    return U[:, s > (s[0] if len(s) else 0) * tol] if len(s) and s[0] > 0 else np.zeros((A.shape[0], 0))


class Design:
    """The rows of one analysis (drug-dose x line cells with X, Y and every covariate present; drug-doses and lines
    with < 2 rows dropped), the FE projection and the covariate x TP53-group nuisance.
    fe = 'dd': drug-dose FE + line FE (as specified); 'ddxg': drug-dose x TP53-group FE + line FE (each drug-dose has
    its own WT mean and its own altered mean: the WT-only p53 response of a drug-dose is absorbed, and b_WT / b_alt
    come only from line-to-line variation inside the same group and the same wells)."""

    def __init__(self, ok, X, covs, wt_line, drug_id, fe="dd"):
        ok = ok.copy()
        for _ in range(10):                           # singletons carry no within information
            nd_ = ok.sum(axis=1)
            nl_ = ok.sum(axis=0)
            bad = (nd_ < 2)[:, None] | (nl_ < 2)[None, :]
            if not (ok & bad).any():
                break
            ok &= ~bad
        self.ok = ok
        self.d, self.l = np.nonzero(ok)
        self.n = len(self.d)
        self.wt = wt_line[self.l]
        self.wt_line = wt_line
        self.drug = drug_id[self.d]
        self.fe_kind = fe
        self.cell = self.d.astype(np.int64) if fe == "dd" else 2 * self.d.astype(np.int64) + self.wt
        self.fe = FE(self.cell, self.l)
        self.x = X[self.d, self.l].astype(float)
        self.K = len(covs)
        self.C = np.column_stack([c[self.d, self.l] for c in covs]) if covs else np.zeros((self.n, 0))
        N = np.column_stack([self.C * self.wt[:, None], self.C * (~self.wt)[:, None]])
        self.Qc = orth(self.fe.M(N)) if N.shape[1] else np.zeros((self.n, 0))
        self.xt = self.resid(np.column_stack([np.where(self.wt, self.x, 0.0), np.where(self.wt, 0.0, self.x)]))
        self.p_all = 2 + 2 * self.K + len(self.fe.du) + len(self.fe.lu) - 1
        self._P = None

    def resid(self, V):
        R = self.fe.M(V)
        if self.Qc.shape[1]:
            R = R - self.Qc @ (self.Qc.T @ R)
        return R

    def line_blocks(self):
        """M-projected per-line columns: TRIM72 x line l, and each covariate x line l (for the TP53-label permutation
        and the line-specific slopes)."""
        if self._P is None:
            k = len(self.fe.lu)
            li = np.searchsorted(self.fe.lu, self.l)
            m = k * (1 + self.K)
            Pm = np.zeros((self.n, m))
            Pm[np.arange(self.n), li] = self.x
            for j in range(self.K):
                Pm[np.arange(self.n), (1 + j) * k + li] = self.C[:, j]
            Pm = self.fe.M(Pm)
            H = np.empty((k, m, m))                   # per-line Gram blocks (line-cluster scores of any labelling)
            for j in range(k):
                r = Pm[li == j]
                H[j] = r.T @ r
            self._P = (Pm, Pm.T @ Pm, k, li, H)
        return self._P


def cluster_vcov(Xt, e, groups, bread, n, p):
    """CR1 cluster-robust covariance of the coefficients of Xt (FWL-partialled regressors)."""
    gid = pd.factorize(groups)[0]
    G = gid.max() + 1
    sc = Xt * e[:, None]
    S = np.zeros((G, Xt.shape[1]))
    np.add.at(S, gid, sc)
    c = G / max(G - 1, 1) * (n - 1) / max(n - p, 1)
    return c * bread @ (S.T @ S) @ bread, G


def tp(est, se, df):
    return float(2 * stats.t.sf(abs(est / se), df)) if np.isfinite(se) and se > 0 else np.nan


def perm_p(obs, null):
    null = np.asarray(null, float)
    null = null[np.isfinite(null)]
    if not np.isfinite(obs) or not len(null):
        return np.nan
    return float((1 + (np.abs(null) >= abs(obs) - 1e-12).sum()) / (len(null) + 1))


def within_dd_perm(des, ytil, B, rng, chunk=100):
    """TRIM72 shuffled across lines within each FE cell (drug-dose for fe 'dd', drug-dose x TP53 group for 'ddxg');
    refit. ytil: n x m residualised read-outs sharing this design (the same permutations serve all of them).
    Returns B x 3 x m: b_WT, b_alt, b_common. Uses ytil = R y (R = the FE + covariate residual maker, symmetric
    idempotent), so x~'y~ = v'y~ and x~'x~ = v'Rv = sum v^2 - sum_cell (cell sum of v)^2 / n_cell - |W'v|^2 with
    W = [line-FE basis, covariate basis] (both orthonormal, orthogonal to the cell dummies and to each other): no full
    projection per permutation."""
    n = des.n
    ytil = ytil.reshape(n, -1)
    order0 = np.argsort(des.cell, kind="stable")
    dkey = np.unique(des.cell, return_inverse=True)[1].astype(float)[:, None]
    W = np.column_stack([des.fe.Q, des.Qc]) if des.Qc.shape[1] else des.fe.Q
    D, cnt = des.fe.D, des.fe.cnt
    wtf = des.wt.astype(float)[:, None]
    out = np.empty((B, 3, ytil.shape[1]))
    for c0 in range(0, B, chunk):
        nb = min(chunk, B - c0)
        sh = np.argsort(dkey + rng.random((n, nb)), axis=0)
        XP = np.empty((n, nb))
        XP[order0] = des.x[sh]
        V1, V2 = XP * wtf, XP * (1.0 - wtf)
        S1, S2 = np.asarray(D.T @ V1), np.asarray(D.T @ V2)
        P1, P2 = W.T @ V1, W.T @ V2
        a11 = (V1 * V1).sum(0) - (S1 * S1 / cnt[:, None]).sum(0) - (P1 * P1).sum(0)
        a22 = (V2 * V2).sum(0) - (S2 * S2 / cnt[:, None]).sum(0) - (P2 * P2).sum(0)
        a12 = -(S1 * S2 / cnt[:, None]).sum(0) - (P1 * P2).sum(0)
        c1, c2 = ytil.T @ V1, ytil.T @ V2                    # m x nb
        det = a11 * a22 - a12 ** 2
        out[c0:c0 + nb, 0] = ((a22 * c1 - a12 * c2) / det).T
        out[c0:c0 + nb, 1] = ((a11 * c2 - a12 * c1) / det).T
        out[c0:c0 + nb, 2] = ((c1 + c2) / (a11 + 2 * a12 + a22)).T
    return out, sh[:, -1]


def within_dd_perm_check(des, ytil, rng):
    """One within-cell permutation by the fast formula and by explicit projection: max |difference| of the 3 slopes."""
    fast, last = within_dd_perm(des, ytil[:, :1], 1, rng, chunk=1)
    order0 = np.argsort(des.cell, kind="stable")
    xp = np.empty(des.n)
    xp[order0] = des.x[last]
    direct = within_dd_perm_direct(des, ytil[:, 0], xp)
    return float(np.max(np.abs(fast[0, :, 0] - np.array(direct))))


def within_dd_perm_direct(des, ytil, X_perm_rows):
    """The same refit by explicit projection, for one permuted TRIM72 vector (a check of within_dd_perm)."""
    R = des.resid(np.column_stack([np.where(des.wt, X_perm_rows, 0.0), np.where(des.wt, 0.0, X_perm_rows)]))
    b = np.linalg.solve(R.T @ R, R.T @ ytil)
    xc = R.sum(axis=1)
    return b[0], b[1], float(xc @ ytil / (xc @ xc))


def label_perm(des, MY, B, rng, chunk=250):
    """TP53 labels permuted over the analysed lines (group sizes kept); the fe 'dd' model (TRIM72 x group and every
    covariate x group) refitted through the per-line Gram blocks, with its line-cluster (CR1) SE, so the permuted
    statistic can be studentised (t = diff / SE_line: valid when the two groups differ in residual spread, e.g. WT
    lines responding more to p53 activators). MY: n x m FE-projected read-outs sharing the design (one set of
    permutations for all). Returns per read-out the observed diff and t (identity labels: a check of the main fit)
    and the null diffs and t (B x m)."""
    Pm, G, k, li, H = des.line_blocks()
    nb = 1 + des.K
    m, q, n = k * nb, 2 * nb, des.n
    MY = MY.reshape(n, -1)
    my = MY.shape[1]
    gy = Pm.T @ MY                                        # m x my
    Lsp = sparse.csr_matrix((np.ones(n), (li, np.arange(n))), shape=(k, n))
    h = np.stack([np.asarray(Lsp @ (Pm * MY[:, j:j + 1])) for j in range(my)], axis=2)  # per line: sum Pm_i MY_i
    Gb, gyb, Hf = G.reshape(nb, k, nb, k), gy.reshape(nb, k, my), H.reshape(k * m, m)
    cfac = k / (k - 1) * (n - 1) / max(n - des.p_all, 1)
    cvec = np.zeros(q)
    cvec[0], cvec[1] = 1.0, -1.0                          # (TRIM72, WT) minus (TRIM72, altered)

    def stat(U):
        Bc = U.shape[0]
        S = np.stack([U, 1.0 - U], axis=1)                 # (Bc, 2 groups, k lines)
        T1 = np.einsum("bsk,akcl->bsacl", S, Gb)
        Mx = np.einsum("bsacl,btl->basct", T1, S).reshape(Bc, q, q)
        g_ = np.einsum("bsk,akj->basj", S, gyb).reshape(Bc, q, my)
        beta = np.linalg.solve(Mx, g_)                     # Bc x q x my
        w = np.linalg.solve(Mx, np.broadcast_to(cvec, (Bc, q))[..., None])[..., 0]
        br, wr = beta.reshape(Bc, nb, 2, my), w.reshape(Bc, nb, 2)
        Ab = (br[:, :, 0, None, :] * U[:, None, :, None]
              + br[:, :, 1, None, :] * (1.0 - U)[:, None, :, None]).reshape(Bc, m, my)
        Aw = (wr[:, :, 0, None] * U[:, None, :] + wr[:, :, 1, None] * (1.0 - U)[:, None, :]).reshape(Bc, m)
        HAw = (Hf @ Aw.T).reshape(k, m, Bc)               # read-out free: computed once for all read-outs
        sl = np.einsum("kmj,bm->kbj", h, Aw) - np.einsum("kmb,bmj->kbj", HAw, Ab)   # per line contrast scores
        se = np.sqrt(cfac * (sl ** 2).sum(axis=0))        # Bc x my
        d = beta[:, 0, :] - beta[:, 1, :]
        return d, d / se

    wt0 = des.wt_line[des.fe.lu].astype(float)
    d0, t0 = stat(wt0[None, :])
    nd_, nt_ = [], []
    for c0 in range(0, B, chunk):
        U = np.stack([rng.permutation(wt0) for _ in range(min(chunk, B - c0))])
        d, t = stat(U)
        nd_.append(d)
        nt_.append(t)
    return d0[0], t0[0], np.concatenate(nd_), np.concatenate(nt_)


def label_perm_ddxg(des, Ys, B, rng):
    """TP53-label permutation for fe 'ddxg' (the FE themselves depend on the labels, so the per-line Gram blocks of
    label_perm do not apply). With drug-dose x group FE, line FE and every slope by group, the model separates exactly
    into a WT-lines regression and an altered-lines regression; for each labelling both are refitted on the drug-dose
    x line grid: two-way FE (drug-dose within group, line) by the concentrated normal equations for the line effects
    (one line per group pinned at 0), then the covariates partialled out (FWL), TRIM72 slope and line-cluster (CR1)
    scores. Ys: n x m read-outs sharing the design (one set of permutations for all). Returns per read-out the
    observed diff and t at the true labels (a check of the main fit) and the null diffs and t (B x m)."""
    k = len(des.fe.lu)
    li = np.searchsorted(des.fe.lu, des.l)
    _du, di = np.unique(des.d, return_inverse=True)
    nd, K = len(_du), des.K
    Ys = np.asarray(Ys, float).reshape(des.n, -1)
    m = Ys.shape[1]
    J = 1 + K + m
    V = np.zeros((J, nd, k))
    V[0, di, li] = des.x
    for j in range(K):
        V[1 + j, di, li] = des.C[:, j]
    for j in range(m):
        V[1 + K + j, di, li] = Ys[:, j]
    O = np.zeros((nd, k))
    O[di, li] = 1.0
    nrow = O.sum(axis=0)
    colsum = V.sum(axis=1)                                       # J x k
    n = des.n

    def group(idx):
        Og, Vg = O[:, idx], V[:, :, idx]
        kg = len(idx)
        c = Og.sum(axis=1)
        has = c > 0
        ci = np.where(has, 1.0 / np.where(has, c, 1.0), 0.0)
        S = Vg.sum(axis=2)                                        # J x nd: cell sums
        A = np.diag(nrow[idx]) - (Og * ci[:, None]).T @ Og        # concentrated normal equations, line effects
        r = colsum[:, idx] - (S * ci) @ Og
        al = np.zeros((J, kg))
        al[:, 1:] = np.linalg.lstsq(A[1:, 1:], r[:, 1:].T, rcond=None)[0].T
        de = (S - al @ Og.T) * ci
        R = ((Vg - de[:, :, None] - al[:, None, :]) * Og[None]).reshape(J, -1)   # FE residuals (0 off-design)
        if K:
            Gm = R @ R.T
            coef = np.linalg.lstsq(Gm[1:K + 1, 1:K + 1], Gm[1:K + 1, :], rcond=None)[0]
            Rt = R - coef.T @ R[1:K + 1]
        else:
            Rt = R
        xt = Rt[0]
        xx = xt @ xt
        yt = Rt[1 + K:]
        b = yt @ xt / xx
        e = yt - b[:, None] * xt[None, :]
        s = (e * xt[None, :]).reshape(m, nd, kg).sum(axis=1) / xx  # per-line contrast scores
        return b, (s ** 2).sum(axis=1), int(has.sum())

    def stat(u):
        bw, vw, cw = group(np.flatnonzero(u))
        ba, va, ca = group(np.flatnonzero(~u))
        p_all = 2 + 2 * K + cw + ca + k - 1
        cfac = k / (k - 1) * (n - 1) / max(n - p_all, 1)
        d = bw - ba
        return d, d / np.sqrt(cfac * (vw + va))

    wt0 = des.wt_line[des.fe.lu].astype(bool)
    d0, t0 = stat(wt0)
    nd_, nt_ = np.empty((B, m)), np.empty((B, m))
    for i in range(B):
        nd_[i], nt_[i] = stat(rng.permutation(wt0))
    return d0, t0, nd_, nt_


def line_slopes(des, MY):
    """Line-specific TRIM72 slopes with line-specific covariate slopes (both FE): one model, drug-cluster SE."""
    Pm, G, k, _li, _H = des.line_blocks()
    gy = Pm.T @ MY
    Gi = np.linalg.pinv(G)
    b = Gi @ gy
    e = MY - Pm @ b
    V, Gd = cluster_vcov(Pm, e, des.drug, Gi, des.n, Pm.shape[1] + len(des.fe.du) + k - 1)
    n_rows = np.bincount(np.searchsorted(des.fe.lu, des.l), minlength=k)
    return b[:k], np.sqrt(np.clip(np.diag(V)[:k], 0, None)), n_rows, Gd


def resid_y(des, Y):
    """FE projection (MY) and full residual (ytil: FE + covariates x group out) of one or more read-outs."""
    MY = des.fe.M(Y)
    if des.Qc.shape[1]:
        return MY, MY - des.Qc @ (des.Qc.T @ MY)
    return MY, MY


def fit(des, y, within=None, label=None, want_lines=False):
    """The main fit of one read-out; within = its B x 3 within-cell permutation null (or None), label = its
    TP53-label permutation (observed diff, observed t, null diffs, null t) or None."""
    n = des.n
    MY, ytil = resid_y(des, y)
    Xt = des.xt
    bread = np.linalg.inv(Xt.T @ Xt)
    b = bread @ (Xt.T @ ytil)
    e = ytil - Xt @ b
    Vd, Gd = cluster_vcov(Xt, e, des.drug, bread, n, des.p_all)
    Vl, Gl = cluster_vcov(Xt, e, des.l, bread, n, des.p_all)
    Vi, _ = cluster_vcov(Xt, e, des.drug.astype(np.int64) * 1000 + des.l, bread, n, des.p_all)
    c = np.array([1.0, -1.0])
    out = {"n_rows": n, "n_drugdoses": len(np.unique(des.d)), "n_fe_cells": len(des.fe.du), "n_drugs": int(Gd),
           "n_lines_WT": int(len(np.unique(des.l[des.wt]))), "n_lines_alt": int(len(np.unique(des.l[~des.wt])))}
    td, tl = stats.t.ppf(0.975, Gd - 1), stats.t.ppf(0.975, min(Gd, Gl) - 1)
    for i, nm in ((0, "WT"), (1, "alt")):
        se = np.sqrt(Vd[i, i])
        se2 = float(se_conservative(Vd[i, i], Vl[i, i], Vi[i, i])[0])      # conservative two-way
        out.update({f"b_{nm}": b[i], f"se_{nm}_drug": se, f"ci_{nm}_lo": b[i] - td * se, f"ci_{nm}_hi": b[i] + td * se,
                    f"p_{nm}_drug": tp(b[i], se, Gd - 1), f"se_{nm}_twoway": se2,
                    f"p_{nm}_twoway": tp(b[i], se2, min(Gd, Gl) - 1)})
    dif = b[0] - b[1]
    vd, vl, vi = c @ Vd @ c, c @ Vl @ c, c @ Vi @ c
    se_d, se_l = np.sqrt(vd), np.sqrt(vl)
    se_2, se_cgm, src = (x.item() for x in se_conservative(vd, vl, vi))
    out.update({"diff": dif, "se_diff_drug": se_d, "ci_diff_lo_drug": dif - td * se_d,
                "ci_diff_hi_drug": dif + td * se_d,
                "p_diff_drug": tp(dif, se_d, Gd - 1), "se_diff_line": se_l, "p_diff_line": tp(dif, se_l, Gl - 1),
                "se_diff_twoway": se_2, "ci_diff_lo_twoway": dif - tl * se_2, "ci_diff_hi_twoway": dif + tl * se_2,
                "p_diff_twoway": tp(dif, se_2, min(Gd, Gl) - 1), "se_diff_twoway_from": src,
                "se_diff_twoway_cgm": se_cgm, "p_diff_twoway_cgm": tp(dif, se_cgm, min(Gd, Gl) - 1)})
    # common slope (one TRIM72 slope for all lines, covariates still by group)
    xc = Xt.sum(axis=1)
    bc = float(xc @ ytil / (xc @ xc))
    ec = ytil - bc * xc
    bc_ = np.array([[1 / (xc @ xc)]])
    Vc, _ = cluster_vcov(xc[:, None], ec, des.drug, bc_, n, des.p_all - 1)
    Vcl, _ = cluster_vcov(xc[:, None], ec, des.l, bc_, n, des.p_all - 1)
    Vci, _ = cluster_vcov(xc[:, None], ec, des.drug.astype(np.int64) * 1000 + des.l, bc_, n, des.p_all - 1)
    sec = float(np.sqrt(Vc[0, 0]))
    sec2 = float(se_conservative(Vc[0, 0], Vcl[0, 0], Vci[0, 0])[0])
    out.update({"b_common": bc, "se_common_drug": sec, "ci_common_lo": bc - td * sec, "ci_common_hi": bc + td * sec,
                "p_common_drug": tp(bc, sec, Gd - 1), "se_common_twoway": sec2,
                "ci_common_lo_twoway": bc - tl * sec2, "ci_common_hi_twoway": bc + tl * sec2,
                "p_common_twoway": tp(bc, sec2, min(Gd, Gl) - 1)})
    # permutation nulls
    if within is not None:
        nul = within
        dn = nul[:, 0] - nul[:, 1]
        out.update({"p_WT_perm_within_dd": perm_p(b[0], nul[:, 0]), "p_alt_perm_within_dd": perm_p(b[1], nul[:, 1]),
                    "p_diff_perm_within_dd": perm_p(dif, dn), "sd_diff_perm_within_dd": float(np.nanstd(dn)),
                    "p_common_perm_within_dd": perm_p(bc, nul[:, 2]),
                    "sd_WT_perm_within_dd": float(np.nanstd(nul[:, 0])),
                    "sd_common_perm_within_dd": float(np.nanstd(nul[:, 2])), "n_perm_within_dd": len(nul)})
    if label is not None:
        obs, tobs, nl, ntt = label
        sd = float(np.nanstd(nl))
        out.update({"t_diff_line": dif / se_l, "p_diff_tp53_label_perm": perm_p(tobs, ntt),
                    "p_diff_tp53_label_perm_unstudentised": perm_p(dif, nl), "sd_diff_tp53_label_perm": sd,
                    "ci_diff_lo_labelsd": dif - 1.96 * sd, "ci_diff_hi_labelsd": dif + 1.96 * sd,
                    "n_perm_tp53_label": len(nl), "check_label_engine_minus_main": float(obs - dif),
                    "check_label_engine_t_minus_main": float(tobs - dif / se_l)})
        out["mde_diff_80"] = Z80 * sd
        out["mde_diff_80_line_se"] = Z80 * se_l
    if within is not None:
        out["mde_diff_80_within_dd"] = Z80 * out["sd_diff_perm_within_dd"]
    # scale: SD of the residual TRIM72 (FE + covariates out) per group, and of the residual read-out
    xr = Xt.sum(axis=1)
    out.update({"sd_TRIM72_resid_WT": float(np.std(xr[des.wt])), "sd_TRIM72_resid_alt": float(np.std(xr[~des.wt])),
                "sd_Y_resid": float(np.std(ytil))})
    out["b_WT_per_sd_TRIM72"] = b[0] * out["sd_TRIM72_resid_WT"]
    out["b_alt_per_sd_TRIM72"] = b[1] * out["sd_TRIM72_resid_alt"]
    if "mde_diff_80" in out:
        out["mde_diff_80_per_sd_TRIM72"] = out["mde_diff_80"] * float(np.std(xr))
    lines = line_slopes(des, MY) if want_lines else None
    return out, lines


# ============================================================================= assembling the per (drug-dose, line) data
def panel_well_arrays(E, grid, genes):
    """wells x lines (atlas order) r2 of panel genes."""
    wi = np.array([E.si[s] for s in grid.w["sample"]])
    li = np.array([E.lines.index(l_) for l_ in grid.L])
    return {g: E.mat(g)[np.ix_(wi, li)] for g in genes}


def module_mean(arrs):
    with quiet():
        return np.nanmean(np.stack(arrs), axis=0)


def covariates(grid, Bkeep=None):
    """DD_beta (0 where the drug-dose has no consensus), DD_A, S and G2M per (drug-dose, line); with Bkeep (some
    wells left out), drug-doses that lost a well take the mean of the per-well values of the wells kept."""
    fxd = grid.fxd
    beta = np.load(os.path.join(fxd, "DD_beta.npy")).astype(float)
    A = np.load(os.path.join(fxd, "DD_A.npy")).astype(float)
    m = np.load(os.path.join(fxd, "DD_r2_modules.npy")).astype(float)
    cv = {"beta": beta, "A": A, "S": m[:, :, 0].copy(), "G2M": m[:, :, 1].copy()}
    if Bkeep is not None:
        changed = np.asarray((grid.B - Bkeep).sum(axis=1)).ravel() > 0
        kept = np.asarray(Bkeep.sum(axis=1)).ravel() > 0
        wb = np.load(os.path.join(fxd, "beta.npy")).astype(float)
        wa = np.load(os.path.join(fxd, "A2.npy")).astype(float)
        wm = np.load(os.path.join(fxd, "r2_modules.npy")).astype(float)
        for k, V in (("beta", wb), ("A", wa), ("S", wm[:, :, 0]), ("G2M", wm[:, :, 1])):
            alt = Grid.dd_mean(Bkeep, V)
            cv[k][changed] = alt[changed]
            cv[k][~kept] = np.nan
    allnan = np.isnan(cv["beta"]).all(axis=1)
    cv["beta"][allnan] = 0.0                       # no consensus response (< 20 significant genes): no responder
    return cv


def build_tables(E, grid, pbe, Bkeep, p53resp_x_dd):
    """Per (drug-dose, line) arrays: TRIM72, D1 read-outs, screen genes and modules, covariates."""
    psyms = [str(s) for s in pbe["symbols"]]
    panel_genes = [GENE] + [g for g in D1 if g != "P53_SCORE"] + [g for g in SCREEN_GENES if g in E.gi]
    pw = panel_well_arrays(E, grid, list(dict.fromkeys(panel_genes + E.members + BACKGROUND)))
    wells = {g: pw[g] for g in panel_genes}
    wells["P53_SCORE"] = module_mean([pw[g] for g in E.members])
    with quiet():
        wells["bg_abs_r2"] = np.nanmean(np.abs(np.stack([pw[g] for g in BACKGROUND])), axis=0)
    for j, g in enumerate(psyms):
        if g not in wells:
            wells[g] = pbe["r2"][:, :, j].astype(float)
    for name, _pm, genes, as_module, _cs in SCREEN:
        if as_module:
            wells[f"{name} module"] = module_mean([wells[g] for g in genes])
    out = {k: Grid.dd_mean(Bkeep, v) for k, v in wells.items()}
    cv = covariates(grid, None if Bkeep is grid.B else Bkeep)
    out.update(cv)
    # the known fold-change artifact: a low untreated TRIM72 level inflates the line's TRIM72 fold under a raiser.
    # Covariate = line's untreated level (log2 DMSO CPM, z over lines) x the drug-dose's TRIM72 effect (atlas DD_lfc)
    base = np.log2(E.L.reindex(grid.L)[f"cpm_dmso_{GENE}"].to_numpy(dtype=float) + 0.1)
    base = (base - np.nanmean(base)) / np.nanstd(base)
    ag = pd.read_csv(os.path.join(grid.fxd, "genes.csv"))
    col = int(ag.loc[(ag["kind"] == "gene") & (ag["symbol"] == GENE), "col"].iloc[0])
    ddl = np.asarray(np.load(os.path.join(grid.fxd, "DD_lfc.npy"), mmap_mode="r")[:, col], dtype=float)
    out["trim72_base_x_dd"] = ddl[:, None] * base[None, :]
    # the line's p53 responsiveness (panel, z over lines) x the drug-dose's P53_ACTIVITY z: a line that answers p53
    # activators strongly answers them strongly in every drug-dose, whatever its TRIM72
    out["p53resp_x_dd"] = p53resp_x_dd
    return out, wells


# ============================================================================= analyses
def spec_ok(spec, tabs):
    tb = tabs[spec["tabs"]]
    ok = np.isfinite(spec["X"]) & np.isfinite(tb[spec["readout"]]) & spec["ddmask"][:, None]
    for c in COVSETS[spec["covset"]]:
        ok &= np.isfinite(tb[c])
    return ok


def run_models(rows_spec, tabs, grid, wt_line, rng, want_lines_for=()):
    """rows_spec: list of dicts (family, module, readout, variant, covset, fe, xname, tabs, X, ddmask, B_within,
    B_label). Specs with the same design (same rows, X, covariates, FE) are fitted together: one design, one set of
    within-cell and TP53-label permutations for all their read-outs. Rows come back in spec order."""
    groups = {}
    for i, spec in enumerate(rows_spec):
        ok = spec_ok(spec, tabs)
        key = (spec["tabs"], spec["xname"], spec["covset"], spec["fe"], ok.tobytes())
        groups.setdefault(key, (ok, []))[1].append(i)
    res, slopes = [None] * len(rows_spec), []
    for key, (ok, idxs) in groups.items():
        s0 = rows_spec[idxs[0]]
        tb = tabs[s0["tabs"]]
        t0 = time.time()
        des = Design(ok, s0["X"], [tb[c] for c in COVSETS[s0["covset"]]], wt_line, grid.drug_id, s0["fe"])
        Ym = np.column_stack([tabs[rows_spec[i]["tabs"]][rows_spec[i]["readout"]][des.d, des.l]
                              for i in idxs]).astype(float)
        _MY, ytil = resid_y(des, Ym)
        wn = within_dd_perm(des, ytil, s0["B_within"], rng)[0] if s0["B_within"] else None
        lab = None
        if s0["B_label"]:
            lab = (label_perm_ddxg(des, Ym, s0["B_label"], rng) if des.fe_kind == "ddxg"
                   else label_perm(des, _MY, s0["B_label"], rng))
        for j, i in enumerate(idxs):
            spec = rows_spec[i]
            want = (spec["variant"], spec["covset"], spec["readout"]) in want_lines_for or \
                (spec["variant"], spec["covset"]) in want_lines_for
            lj = None if lab is None else (lab[0][j], lab[1][j], lab[2][:, j], lab[3][:, j])
            o, ls = fit(des, Ym[:, j], None if wn is None else wn[:, :, j], lj, want)
            res[i] = {k: spec[k] for k in ("family", "module", "readout", "variant", "covset", "fe", "xname")} | o
            if ls is not None:
                b, se, nr, Gd = ls
                for q, l_ in enumerate(des.fe.lu):
                    slopes.append({"readout": spec["readout"], "variant": spec["variant"], "covset": spec["covset"],
                                   "fe": spec["fe"], "cell_line_id": grid.L[l_],
                                   "cell_line": grid.lines.loc[l_, "cell_name"],
                                   "tp53_group": "WT" if wt_line[l_] else "altered", "n_rows": int(nr[q]),
                                   "slope": b[q], "se_drug": se[q],
                                   "ci_lo": b[q] - stats.t.ppf(0.975, Gd - 1) * se[q],
                                   "ci_hi": b[q] + stats.t.ppf(0.975, Gd - 1) * se[q],
                                   "p_drug": tp(b[q], se[q], Gd - 1)})
            log(f"  {spec['family']} {spec['readout']} [{spec['variant']}, {spec['covset']}, FE {spec['fe']}]: "
                f"n {o['n_rows']}, b_WT {o['b_WT']:+.4f}, b_alt {o['b_alt']:+.4f}, diff {o['diff']:+.4f} "
                f"(p two-way {o['p_diff_twoway']:.3g}, p label {o.get('p_diff_tp53_label_perm', np.nan):.3g})")
        log(f"  ({len(idxs)} read-outs on one design: {time.time() - t0:.0f} s)")
    return pd.DataFrame(res), pd.DataFrame(slopes)


def slope_tests(slopes, n_perm, rng, min_rows=20):
    rows = []
    for (ro, va, cs, fe), g in slopes.groupby(["readout", "variant", "covset", "fe"], sort=False):
        g = g[(g["n_rows"] >= min_rows) & np.isfinite(g["slope"])]
        a = g.loc[g["tp53_group"] == "WT", "slope"].to_numpy()
        b = g.loc[g["tp53_group"] == "altered", "slope"].to_numpy()
        if len(a) < 3 or len(b) < 3:
            continue
        obs = a.mean() - b.mean()
        t = stats.ttest_ind(a, b, equal_var=False)
        allv = np.concatenate([a, b])
        idx = np.argsort(rng.random((n_perm, len(allv))), axis=1)
        pa, pb = allv[idx[:, :len(a)]], allv[idx[:, len(a):]]
        null = pa.mean(1) - pb.mean(1)
        tnull = null / np.sqrt(pa.var(1, ddof=1) / len(a) + pb.var(1, ddof=1) / len(b))
        se = np.sqrt(a.var(ddof=1) / len(a) + b.var(ddof=1) / len(b))
        dfw = float(t.df) if hasattr(t, "df") else len(allv) - 2
        # rank-based: Mann-Whitney (two-sided) and the Hodges-Lehmann shift (median of all WT - altered differences)
        mw = stats.mannwhitneyu(a, b, alternative="two-sided")
        rows.append({"readout": ro, "variant": va, "covset": cs, "fe": fe, "n_lines_WT": len(a), "n_lines_alt": len(b),
                     "mean_slope_WT": a.mean(), "mean_slope_alt": b.mean(), "median_slope_WT": np.median(a),
                     "median_slope_alt": np.median(b), "n_WT_negative": int((a < 0).sum()),
                     "n_alt_negative": int((b < 0).sum()), "diff_mean_WT_minus_alt": obs, "se_welch": se,
                     "ci_lo_welch": obs - stats.t.ppf(0.975, dfw) * se,
                     "ci_hi_welch": obs + stats.t.ppf(0.975, dfw) * se,
                     "p_welch": float(t.pvalue), "p_tp53_label_perm": perm_p(obs / se, tnull),
                     "p_tp53_label_perm_unstudentised": perm_p(obs, null),
                     "sd_label_perm": float(null.std()), "mde_diff_80": Z80 * float(null.std()),
                     "diff_median_WT_minus_alt": float(np.median(a) - np.median(b)),
                     "hodges_lehmann_WT_minus_alt": float(np.median(np.subtract.outer(a, b))),
                     "mannwhitney_U_WT": float(mw.statistic),
                     "auc_WT_gt_alt": float(mw.statistic) / (len(a) * len(b)), "p_mannwhitney": float(mw.pvalue),
                     "n_perm": n_perm, "min_rows_per_line": min_rows})
    return pd.DataFrame(rows)


def readthrough_fit(tab, grid, ddmask):
    """TRIM72 r2 on FUS r2 and PYCARD-AS1 r2 within drug-dose and line (pooled slopes); TRIM72_rt = TRIM72 r2 minus
    that fit (FE not removed; the model absorbs them)."""
    X, F, Pa = tab[GENE], tab["FUS"], tab["PYCARD-AS1"]
    ok = np.isfinite(X) & np.isfinite(F) & np.isfinite(Pa) & ddmask[:, None]
    des = Design(ok, X, [], np.ones(grid.nl, bool), grid.drug_id)
    fe = des.fe
    MX = fe.M(X[des.d, des.l])
    MF = fe.M(np.column_stack([F[des.d, des.l], Pa[des.d, des.l]]))
    bread = np.linalg.inv(MF.T @ MF)
    s = bread @ (MF.T @ MX)
    e = MX - MF @ s
    V, G = cluster_vcov(MF, e, des.drug, bread, des.n, 2 + len(fe.du) + len(fe.lu) - 1)
    rt = X - s[0] * np.where(np.isfinite(F), F, np.nan) - s[1] * np.where(np.isfinite(Pa), Pa, np.nan)
    rows = []
    for i, nm in enumerate(["FUS_r2", "PYCARD-AS1_r2"]):
        se = np.sqrt(V[i, i])
        rows.append({"predictor": nm, "slope": s[i], "se_drug": se, "p_drug": tp(s[i], se, G - 1),
                     "n_rows": des.n, "n_drugdoses": len(fe.du), "n_lines": len(fe.lu),
                     "within_R2_of_TRIM72": float(1 - (e @ e) / (MX @ MX)),
                     "within_r_TRIM72_vs_predictor_alone": float(np.corrcoef(MX, MF[:, i])[0, 1])})
    return rt, pd.DataFrame(rows)


def many_diffs(des, Ym, glob_dims=None):
    """b_WT, b_alt, diff = b_WT - b_alt and their conservative two-way (drug, line) CR1 SE for many read-outs on one
    design (the same numbers as fit(), vectorised over read-outs; no permutations). With glob_dims = (n drugs,
    n lines) also the per-cluster scores of diff (drug, line, drug x line clusters in global numbering, unscaled):
    the cross-read-out covariance of the diffs is their cross-product (for the camera-style set test)."""
    n = des.n
    _MY, yt = resid_y(des, Ym)
    Xt = des.xt
    bread = np.linalg.inv(Xt.T @ Xt)
    b = bread @ (Xt.T @ yt)
    e = yt - Xt @ b
    W = Xt @ bread                                              # per-row weights of b_WT, b_alt
    out = {"b_WT": b[0], "b_alt": b[1], "diff": b[0] - b[1]}
    V = {}
    for nm, g in (("drug", des.drug), ("line", des.l), ("inter", des.drug.astype(np.int64) * 1000 + des.l)):
        gid = pd.factorize(g)[0]
        G = gid.max() + 1
        S = sparse.csr_matrix((np.ones(n), (gid, np.arange(n))), shape=(G, n))
        c = G / max(G - 1, 1) * (n - 1) / max(n - des.p_all, 1)
        u0, u1 = np.asarray(S @ (W[:, [0]] * e)), np.asarray(S @ (W[:, [1]] * e))
        V[nm] = {"WT": c * (u0 ** 2).sum(0), "alt": c * (u1 ** 2).sum(0), "diff": c * ((u0 - u1) ** 2).sum(0), "G": G}
    for k in ("WT", "alt", "diff"):
        out[f"se_{k}_twoway"] = se_conservative(V["drug"][k], V["line"][k], V["inter"][k])[0]
    df = min(V["drug"]["G"], V["line"]["G"]) - 1
    out["t_diff_twoway"] = out["diff"] / out["se_diff_twoway"]
    out["p_diff_twoway"] = 2 * stats.t.sf(np.abs(out["t_diff_twoway"]), df)
    scores = None
    if glob_dims is not None:
        ndg, nlg = glob_dims
        sc = (W[:, [0]] - W[:, [1]]) * e
        scores = {}
        for nm, g, G in (("drug", des.drug, ndg), ("line", des.l, nlg),
                         ("inter", des.drug.astype(np.int64) * nlg + des.l, ndg * nlg)):
            S = sparse.csr_matrix((np.ones(n), (g, np.arange(n))), shape=(G, n))
            scores[nm] = np.asarray(S @ sc)                     # G x read-outs
    return out, scores


def gene_null(E, grid, tab, wt_line, variants, rng, R=200):
    """Is the TRIM72 x TP53-group pattern specific to p53 targets? The same model (full covariates) for every panel
    gene (the P53_ACTIVITY members and the non-p53 background genes) and for R random modules of background genes
    the size of P53_SCORE (mean r2 of the members a line expresses, like P53_SCORE); each D1 read-out's two-way t
    placed in the distribution of its reference (P53_SCORE: random modules; single genes: background genes)."""
    genes = list(dict.fromkeys(E.members + BACKGROUND))
    pw = panel_well_arrays(E, grid, genes)
    dd = {g: Grid.dd_mean(grid.B, pw[g]) for g in genes}
    bgw = np.stack([pw[g] for g in BACKGROUND]).astype(np.float32)
    msize = len(E.members)
    mods = [np.sort(rng.choice(len(BACKGROUND), msize, replace=False)) for _ in range(R)]
    with quiet():
        for i, mm in enumerate(mods):
            dd[f"bg_module_{i:03d}"] = Grid.dd_mean(grid.B, np.nanmean(bgw[mm], axis=0).astype(float))
    del bgw, pw
    for r in D1:
        dd.setdefault(f"readout:{r}", tab[r])
    X = tab[GENE]
    covs = [tab[c] for c in COVSETS["full"]]
    rows = []
    setg = list(E.members) + [g for g in BACKGROUND if g not in E.members]   # genes of the set test
    ndg, nlg = int(grid.drug_id.max()) + 1, grid.nl
    camera = {}
    for vname, ddm in variants.items():
        base = np.isfinite(X) & ddm[:, None]
        for c in covs:
            base &= np.isfinite(c)
        groups = {}
        for k, Y in dd.items():
            ok = base & np.isfinite(Y)
            groups.setdefault(ok.tobytes(), (ok, []))[1].append(k)
        for fe in FES:
            U = {nm: np.zeros((G_, len(setg))) for nm, G_ in (("drug", ndg), ("line", nlg), ("inter", ndg * nlg))}
            for ok, keys in groups.values():
                des = Design(ok, X, covs, wt_line, grid.drug_id, fe)
                for c0 in range(0, len(keys), 50):
                    kk = keys[c0:c0 + 50]
                    o, sc = many_diffs(des, np.column_stack([dd[k][des.d, des.l] for k in kk]).astype(float),
                                       (ndg, nlg))
                    for j, k in enumerate(kk):
                        kind = ("D1 read-out" if k.startswith("readout:") else "random background module"
                                if k.startswith("bg_module_") else "P53_ACTIVITY member" if k in E.members
                                else "background gene")
                        rows.append({"variant": vname, "fe": fe, "set": kind, "gene": k.replace("readout:", ""),
                                     "n_rows": des.n} | {m: float(v[j]) for m, v in o.items()})
                        if k in setg:
                            for nm in U:
                                U[nm][:, setg.index(k)] = sc[nm][:, j]
            camera[(vname, fe)] = U
    G = pd.DataFrame(rows)
    summ = []
    for (vname, fe), g in G.groupby(["variant", "fe"], sort=False):
        ref_mod = g[g["set"] == "random background module"]
        ref_gene = g[g["set"] == "background gene"]
        for _, r in g[g["set"] == "D1 read-out"].iterrows():
            ref = ref_mod if r["gene"] == "P53_SCORE" else ref_gene
            tr = ref["t_diff_twoway"].to_numpy()
            nle, nge = int((tr <= r["t_diff_twoway"]).sum()), int((tr >= r["t_diff_twoway"]).sum())
            summ.append({"variant": vname, "fe": fe, "readout": r["gene"], "diff": r["diff"],
                         "t_diff_twoway": r["t_diff_twoway"], "p_diff_twoway": r["p_diff_twoway"],
                         "reference": f"{len(ref)} random modules of {msize} background genes" if r["gene"] ==
                         "P53_SCORE" else f"{len(ref)} background genes", "n_ref": len(ref),
                         "ref_mean_diff": ref["diff"].mean(), "ref_sd_diff": ref["diff"].std(),
                         "ref_mean_t": float(tr.mean()), "ref_sd_t": float(tr.std()),
                         "frac_ref_t_le_obs": nle / len(tr),
                         "p_empirical_two_sided": min(1.0, 2 * min(nle + 1, nge + 1) / (len(tr) + 1))})
        summ.append(set_test(g, camera[(vname, fe)], setg, E.members, vname, fe))
    return G, pd.DataFrame(summ)


def set_test(g, U, setg, members, vname, fe):
    """Camera-style competitive test of the P53_ACTIVITY members vs the background genes: statistic = mean member t
    minus mean background t (two-way t of diff); its variance = s^2 a'Ra (s^2 = pooled within-set variance of the t,
    a = +1/m1 for members, -1/m2 for background genes, R = correlation between the genes' diff estimates from their
    cluster scores: drug, line and two-way versions, the largest a'Ra used, never below independence 1/m1 + 1/m2);
    t distribution with m1 + m2 - 2 df. Unlike a Mann-Whitney of the t, it allows for the genes sharing lines and
    drug-doses (p53 targets move together)."""
    gs = g[g["set"].isin(["P53_ACTIVITY member", "background gene"])].set_index("gene")   # D1 read-outs repeat names
    tt, dif = gs["t_diff_twoway"], gs["diff"]
    have = [x for x in setg if x in gs.index]
    idx = [setg.index(x) for x in have]
    ism = np.array([x in members for x in have])
    t = tt.reindex(have).to_numpy(float)
    m1, m2 = int(ism.sum()), int((~ism).sum())
    a = np.where(ism, 1.0 / m1, -1.0 / m2)
    q0 = 1.0 / m1 + 1.0 / m2
    Cd, Cl, Ci = (U[nm][:, idx].T @ U[nm][:, idx] for nm in ("drug", "line", "inter"))
    qs, rho = {}, {}
    for nm, C in (("drug", Cd), ("line", Cl), ("twoway", Cd + Cl - Ci)):
        dg = np.diag(C)
        if (dg <= 0).any():
            continue
        R = C / np.sqrt(np.outer(dg, dg))
        qs[nm] = float(a @ R @ a)
        mm, bb = R[np.ix_(ism, ism)], R[np.ix_(~ism, ~ism)]
        rho[nm] = (float((mm.sum() - m1) / (m1 * (m1 - 1))), float(R[np.ix_(ism, ~ism)].mean()),
                   float((bb.sum() - m2) / (m2 * (m2 - 1))))
    src = max(qs, key=qs.get) if qs else "independence"
    q = max([q0] + list(qs.values()))
    if q == q0:
        src = "independence (floor)"
    s2 = (((t[ism] - t[ism].mean()) ** 2).sum() + ((t[~ism] - t[~ism].mean()) ** 2).sum()) / (m1 + m2 - 2)
    stat = float(t[ism].mean() - t[~ism].mean())
    se = float(np.sqrt(s2 * q))
    r_ = rho.get(src if src in rho else "line", (np.nan, np.nan, np.nan))
    tb_ = t[~ism]
    return {"variant": vname, "fe": fe, "readout": f"the {m1} P53_ACTIVITY members as a set",
            "diff": float(dif.reindex(have).to_numpy()[ism].mean()), "t_diff_twoway": float(t[ism].mean()),
            "reference": f"{m2} background genes", "n_ref": m2,
            "ref_mean_diff": float(dif.reindex(have).to_numpy()[~ism].mean()),
            "ref_sd_diff": float(dif.reindex(have).to_numpy()[~ism].std(ddof=1)),
            "ref_mean_t": float(tb_.mean()), "ref_sd_t": float(tb_.std()),
            "frac_ref_t_le_obs": float((tb_ <= t[ism].mean()).mean()), "p_empirical_two_sided": np.nan,
            "set_stat_mean_t_members_minus_background": stat, "set_se": se,
            "set_t": stat / se, "set_df": m1 + m2 - 2, "p_set_camera": float(2 * stats.t.sf(abs(stat / se), m1 + m2 - 2)),
            "p_set_independent": float(2 * stats.t.sf(abs(stat) / np.sqrt(s2 * q0), m1 + m2 - 2)),
            "set_vif_effective": q / q0, "set_vif_from": src,
            "set_vif_drug": qs.get("drug", np.nan) / q0, "set_vif_line": qs.get("line", np.nan) / q0,
            "set_vif_twoway": qs.get("twoway", np.nan) / q0,
            "rho_mean_members": r_[0], "rho_mean_members_background": r_[1], "rho_mean_background": r_[2],
            "note": "diff, t = mean over the members; p_set_camera = camera-style test of mean member t minus mean "
                    "background t, variance inflated for the correlation of the genes' estimates (rho_* from the "
                    "cluster version that gives the largest variance); p_set_independent = the same without the "
                    "inflation (genes treated as independent)"}


def reliability(XA, XB, ok_base, covs, wt_line, grid, extra=(), fe="dd"):
    """Correlation of the residual (FE + covariates x group) TRIM72 from half A and half B (or well 1 / well 2) over
    common cells; Spearman-Brown for the full measure."""
    ok = ok_base & np.isfinite(XA) & np.isfinite(XB)
    for c in list(covs) + list(extra):
        ok &= np.isfinite(c)
    des = Design(ok, XA, list(covs) + list(extra), wt_line, grid.drug_id, fe)
    ra = des.resid(XA[des.d, des.l].astype(float))
    rb = des.resid(XB[des.d, des.l].astype(float))
    out = []
    for gname, m in (("all lines", np.ones(des.n, bool)), ("TP53-WT", des.wt), ("TP53-altered", ~des.wt)):
        r = float(np.corrcoef(ra[m], rb[m])[0, 1])
        out.append({"tp53_group": gname, "n_rows": int(m.sum()), "n_drugdoses": len(np.unique(des.d[m])),
                    "r_halves": r, "reliability_full_spearman_brown": 2 * r / (1 + r) if r > -1 else np.nan,
                    "sd_resid_A": float(ra[m].std()), "sd_resid_B": float(rb[m].std())})
    return out


def breakdown(tb, grid, wt_line, ddmask, variant, covset="full", fe="dd", lodo=False):
    """Which drug-doses carry b_WT - b_alt: per drug-dose contributions from the FWL-partialled vectors of the full
    model (contrib_* = sum over the drug-dose's rows of x~ y~ / sum over all rows of x~^2; for 'ddxg' they add up to
    b_WT / b_alt exactly; for 'dd' the WT-altered cross term is left out, and the sums can differ from b), and
    (lodo) the model refitted without each drug (all its doses) and without each line."""
    covs = [tb[c] for c in COVSETS[covset]]
    X = tb[GENE]
    pdd, lo, ll = [], [], []
    for ro in D1:
        Y = tb[ro]
        ok = np.isfinite(X) & np.isfinite(Y) & ddmask[:, None]
        for c in covs:
            ok &= np.isfinite(c)
        des = Design(ok, X, covs, wt_line, grid.drug_id, fe)
        y = Y[des.d, des.l].astype(float)
        ytil = des.resid(y)
        x1, x2 = des.xt[:, 0], des.xt[:, 1]
        s1, s2 = (x1 * x1).sum(), (x2 * x2).sum()
        full, _ = fit(des, y)
        g = pd.DataFrame({"d": des.d, "wt": des.wt, "a1": x1 * ytil, "q1": x1 * x1, "a2": x2 * ytil, "q2": x2 * x2})
        agg = g.groupby("d").agg(n_WT=("wt", "sum"), n=("wt", "size"), a1=("a1", "sum"), q1=("q1", "sum"),
                                 a2=("a2", "sum"), q2=("q2", "sum"))
        for d_, r in agg.iterrows():
            pdd.append({"readout": ro, "variant": variant, "covset": covset, "fe": fe, "drugdose_row": d_,
                        "drug": grid.dd.loc[d_, "drug"], "conc": grid.dd.loc[d_, "conc"],
                        "plates": grid.dd.loc[d_, "plates"], "n_lines_WT": int(r["n_WT"]),
                        "n_lines_alt": int(r["n"] - r["n_WT"]),
                        "slope_WT_in_drugdose": r["a1"] / r["q1"] if r["q1"] > 0 else np.nan,
                        "slope_alt_in_drugdose": r["a2"] / r["q2"] if r["q2"] > 0 else np.nan,
                        "weight_share_WT": r["q1"] / s1, "weight_share_alt": r["q2"] / s2,
                        "contrib_WT": r["a1"] / s1, "contrib_alt": r["a2"] / s2,
                        "contrib_diff": r["a1"] / s1 - r["a2"] / s2})
        if lodo:
            for dr in np.unique(grid.drug_id[ddmask]):
                ok2 = ok & (grid.drug_id != dr)[:, None]
                d2 = Design(ok2, X, covs, wt_line, grid.drug_id, fe)
                o, _ = fit(d2, Y[d2.d, d2.l].astype(float))
                lo.append({"readout": ro, "variant": variant, "covset": covset, "fe": fe,
                           "dropped_drug": grid.dd["drug"].to_numpy()[np.flatnonzero(grid.drug_id == dr)[0]],
                           "n_rows": o["n_rows"], "n_drugdoses": o["n_drugdoses"], "b_WT": o["b_WT"],
                           "b_alt": o["b_alt"], "diff": o["diff"], "p_diff_line": o["p_diff_line"],
                           "p_diff_twoway": o["p_diff_twoway"], "diff_all_drugs": full["diff"],
                           "p_diff_line_all_drugs": full["p_diff_line"],
                           "p_diff_twoway_all_drugs": full["p_diff_twoway"]})
            for l0 in des.fe.lu:                       # leave one line out
                ok3 = ok.copy()
                ok3[:, l0] = False
                d3 = Design(ok3, X, covs, wt_line, grid.drug_id, fe)
                o, _ = fit(d3, Y[d3.d, d3.l].astype(float))
                ll.append({"readout": ro, "variant": variant, "covset": covset, "fe": fe,
                           "dropped_line_id": grid.L[l0], "dropped_line": grid.lines.loc[l0, "cell_name"],
                           "dropped_tp53_group": "WT" if wt_line[l0] else "altered",
                           "n_rows": o["n_rows"], "n_lines_WT": o["n_lines_WT"], "n_lines_alt": o["n_lines_alt"],
                           "b_WT": o["b_WT"], "b_alt": o["b_alt"], "diff": o["diff"],
                           "p_diff_line": o["p_diff_line"], "p_diff_twoway": o["p_diff_twoway"],
                           "diff_all_lines": full["diff"], "p_diff_line_all_lines": full["p_diff_line"],
                           "p_diff_twoway_all_lines": full["p_diff_twoway"]})
    return pd.DataFrame(pdd), pd.DataFrame(lo), pd.DataFrame(ll)


def joint_active(tb, grid, wt_line, active, fe, covset="full"):
    """The active-set estimate inside one model over all drug-doses: TRIM72 x TP53 group x (active, inactive) slopes,
    every covariate x group x (active, inactive), FE as fe ('ddxg': drug-dose x group cells, so the active and
    inactive drug-doses have their own cells; line FE shared, i.e. estimated from all drug-doses). Contrasts: the
    active diff (b_WT - b_alt), the inactive diff, their difference-in-differences (active minus inactive), and the
    four slopes; SE by drug, line, two-way and the conservative max."""
    covs = [tb[c] for c in COVSETS[covset]]
    X = tb[GENE]
    rows = []
    CON = [("active: b_WT - b_alt (line FE from all drug-doses)", [1, -1, 0, 0]),
           ("inactive: b_WT - b_alt", [0, 0, 1, -1]),
           ("difference-in-differences: active diff minus inactive diff", [1, -1, -1, 1]),
           ("active: b_WT", [1, 0, 0, 0]), ("active: b_alt", [0, 1, 0, 0]),
           ("inactive: b_WT", [0, 0, 1, 0]), ("inactive: b_alt", [0, 0, 0, 1])]
    for ro in D1:
        Y = tb[ro]
        ok = np.isfinite(X) & np.isfinite(Y)
        for c in covs:
            ok &= np.isfinite(c)
        des = Design(ok, X, covs, wt_line, grid.drug_id, fe)
        n = des.n
        ac, w = active[des.d], des.wt
        cells = [w & ac, ~w & ac, w & ~ac, ~w & ~ac]
        Xc = np.column_stack([np.where(c, des.x, 0.0) for c in cells])
        N = np.column_stack([des.C * c[:, None] for c in cells]) if des.K else np.zeros((n, 0))
        Qc = orth(des.fe.M(N)) if N.shape[1] else np.zeros((n, 0))

        def res(V):
            R = des.fe.M(V)
            return R - Qc @ (Qc.T @ R) if Qc.shape[1] else R
        Xt = res(Xc)
        yt = res(Y[des.d, des.l].astype(float))
        bread = np.linalg.inv(Xt.T @ Xt)
        b = bread @ (Xt.T @ yt)
        e = yt - Xt @ b
        p_all = 4 + N.shape[1] + len(des.fe.du) + len(des.fe.lu) - 1
        Vd, Gd = cluster_vcov(Xt, e, des.drug, bread, n, p_all)
        Vl, Gl = cluster_vcov(Xt, e, des.l, bread, n, p_all)
        Vi, _ = cluster_vcov(Xt, e, des.drug.astype(np.int64) * 1000 + des.l, bread, n, p_all)
        df = min(Gd, Gl) - 1
        tl = stats.t.ppf(0.975, df)
        for nm, cv in CON:
            c = np.array(cv, float)
            est = float(c @ b)
            vd, vl, vi = c @ Vd @ c, c @ Vl @ c, c @ Vi @ c
            se, cgm, src = (x.item() for x in se_conservative(vd, vl, vi))
            rows.append({"readout": ro, "fe": fe, "covset": covset, "contrast": nm, "n_rows": n,
                         "n_rows_active": int(ac.sum()), "n_drugdoses_active": len(np.unique(des.d[ac])),
                         "n_drugdoses_inactive": len(np.unique(des.d[~ac])), "n_drugs": int(Gd), "n_lines": int(Gl),
                         "estimate": est, "se_drug": float(np.sqrt(vd)), "p_drug": tp(est, np.sqrt(vd), Gd - 1),
                         "se_line": float(np.sqrt(vl)), "p_line": tp(est, np.sqrt(vl), Gl - 1),
                         "se_twoway_cgm": cgm, "se_twoway": se, "se_twoway_from": src,
                         "ci_lo_twoway": est - tl * se, "ci_hi_twoway": est + tl * se, "p_twoway": tp(est, se, df)})
    return pd.DataFrame(rows)


# ============================================================================= checks and outputs
def checks(E, grid, pbe, pbc, tabs, data, sh_check):
    rows = []

    def add(check, value, n=np.nan, note=""):
        rows.append({"check": check, "value": value, "n": n, "note": note})
    add("P53_SCORE members (panel P53_ACTIVITY, testable)", len(E.members), len(E.members), ", ".join(E.members))
    add("background genes for bg_abs_r2 (panel genes, not p53-related, not screen genes, not TRIM72)",
        len(BACKGROUND), len(BACKGROUND), ", ".join(BACKGROUND))
    psyms = [str(s) for s in pbe["symbols"]]
    # pseudobulk counts vs the panel's well_line counts (same cells, two extracts)
    wl = pd.read_parquet(os.path.join(data, "gene_panel", "well_line.parquet"),
                         columns=["sample", "cell_line_id", "total_counts", "n_cells", GENE])
    wi = {s: i for i, s in enumerate(grid.w["sample"])}
    li = {l_: i for i, l_ in enumerate(grid.L)}
    wl = wl[wl["sample"].astype(str).isin(wi) & wl["cell_line_id"].astype(str).isin(li)]
    a, b = wl["sample"].astype(str).map(wi).to_numpy(), wl["cell_line_id"].astype(str).map(li).to_numpy()
    j = psyms.index(GENE)
    add("pseudobulk vs gene_panel well_line: max |diff| TRIM72 counts", float(np.max(np.abs(
        pbc["counts"][a, b, j] - wl[GENE].to_numpy()))), len(wl))
    add("pseudobulk vs gene_panel well_line: max |diff| total counts", float(np.max(np.abs(
        pbc["tot"][a, b] - wl["total_counts"].to_numpy()))), len(wl))
    add("pseudobulk vs gene_panel well_line: max |diff| cells", float(np.max(np.abs(
        pbc["nc"][a, b] - wl["n_cells"].to_numpy()))), len(wl))
    # corrected_effects() on the pseudobulk vs the panel's T.expression_effects, per (well, line) r2
    pw = panel_well_arrays(E, grid, VALIDATE)
    for g in VALIDATE:
        x, y = pbe["r2"][:, :, psyms.index(g)].astype(float), pw[g]
        m = np.isfinite(x) & np.isfinite(y)
        add(f"{g} r2 per (well, line): corrected_effects (pseudobulk) vs panel, Pearson r", float(np.corrcoef(
            x[m], y[m])[0, 1]), int(m.sum()), f"median |diff| {np.median(np.abs(x[m] - y[m])):.2g}; max |diff| "
            f"{np.max(np.abs(x[m] - y[m])):.2g}")
    # corrected_effects drug-dose level vs the atlas DD_lfc
    ag = pd.read_csv(os.path.join(grid.fxd, "genes.csv"))
    ag = ag[ag["kind"] == "gene"]
    col_of = dict(zip(ag["symbol"].astype(str), ag["col"].astype(int)))
    lfc = np.load(os.path.join(grid.fxd, "DD_lfc.npy"), mmap_mode="r")
    jf = psyms.index("FUS")
    add("FUS per (drug-dose, line): our used-well mean of r2 vs corrected_effects' own, max |diff|", float(np.nanmax(
        np.abs(Grid.dd_mean(grid.B, pbe["r2"][:, :, jf].astype(float)) - pbe["per"][:, :, jf]))))
    for jj, g in enumerate(psyms):
        if g in col_of:
            al = np.asarray(lfc[:, col_of[g]], float)
            m = np.isfinite(al) & np.isfinite(pbe["ddl"][:, jj])
            add(f"{g} drug-dose log2FC: corrected_effects vs atlas DD_lfc, max |diff|", float(np.max(np.abs(
                al[m] - pbe["ddl"][m, jj]))), int(m.sum()))
    # idarubicin 5 uM per-line TRIM72 vs the repo's corrected table
    ref = os.path.join(REPO, "trim72_idarubicin", "corrected", "TRIM72_idarubicin_5uM_per_line_corrected.csv")
    r = grid.dd.index[(grid.dd["drug"] == "Idarubicin (hydrochloride)") & np.isclose(grid.dd["conc"], 5)]
    if os.path.exists(ref) and len(r):
        t = pd.read_csv(ref).set_index("cell_line_id")["log2FC_corrected"].reindex(grid.L).to_numpy(float)
        v = tabs["main"][GENE][int(r[0])]
        m = np.isfinite(t) & np.isfinite(v)
        add("idarubicin 5 uM per-line TRIM72 r2 (mean of 2 wells) vs trim72_idarubicin/corrected, max |diff|",
            float(np.max(np.abs(t[m] - v[m]))), int(m.sum()))
    for k, v in sh_check.items():
        add(f"split-half: {k}", v)
    return pd.DataFrame(rows)


README = """Tables of two_way.py (re-created by: python3 two_way.py --data <Tahoe-100M folder>). Associations only: Tahoe
has no MG53 perturbation and measures mRNA; p53 activity = transcription of p53 target genes.

PRIMARY TEST (the first row of key_results.csv): fe ddxg, variant i_all (all 1,132 drug-doses), covariate set
full, read-out P53_SCORE; estimand b_WT - b_alt; p and 95% CI from the conservative two-way SE. Declared in the
verifier round, after a first run, as the design the step specified from the start (the data set as specified, the
FE structure already named the preferred reading, the specified covariates): not preregistered. The other read-outs
of that model are 'secondary'; every other fe x variant x covariate-set row is 'sensitivity' (column role in
d1_two_way_models.csv and key_results.csv). For a claim from any of the 9 variants, P53_SCORE has a Holm adjustment
over the variants (p_holm_variants_*). An ii_active result is a sensitivity result, read with the Holm column.

Headline numbers of this run (P53_SCORE, b_WT - b_alt, fe ddxg, full covariates; key_results.csv):
  primary (i_all)  -0.0032 (95% CI -0.0085 to +0.0022; conservative two-way p 0.24; label-permutation p 0.26).
  ii_active        -0.030 (CI -0.054 to -0.006; two-way p 0.015, label p 0.018; Holm over the 9 variants 0.12 and
                   0.14). Not robust: with the line FE from all drug-doses (d1_active_joint_model.csv) -0.018 (p 0.22),
                   difference-in-differences active minus inactive -0.015 (p 0.29). Every single drug or line left
                   out keeps two-way p < 0.05 (largest 0.039 and 0.046). Line slopes: mean WT - altered -0.024
                   (Welch p 0.040), Hodges-Lehmann -0.018 (Mann-Whitney p 0.064). The 21 members as a set vs the
                   background genes: camera-style p 0.013 (i_all: 0.31).
  readthrough      FUS and PYCARD-AS1 r2 as covariates: i_all -0.0031 (p 0.19), ii_active -0.029 (p 0.032).

Unit: one drug-dose x cell line cell. Values are method-v3 corrected log2 effects r2 (plate x line baseline ->
composition shift -> two-pass position correction) per (well, line), averaged over the drug-dose's used wells
(profiles with >= 30 cells): panel genes from the panel's T.expression_effects (downstream_p53's cache builder), other
genes from upstream_coregulation.corrected_effects() on atlas/pseudobulk. P53_SCORE = mean r2 of the 21 P53_ACTIVITY
members the line expresses. TP53 groups: the panel's (17 WT, 33 altered). NCI-H661 (altered) does not express
TRIM72 by the panel's rule, so it has no TRIM72 value: models have at most 17 WT + 32 altered lines; NCI-H2122 and
NCI-H596 have no DD_A (too few cells for the atlas growth analysis) and drop out of every model with covariates
(17 WT + 30 altered lines).

Model per read-out Y: Y = FE + b_WT TRIM72 x WT + b_alt TRIM72 x altered + covariates x TP53 group. Two FE
structures (column fe):
  dd    drug-dose FE + line FE, as specified. Its drug-dose effect is shared by both TP53 groups, so the WT-only p53
        response of a drug-dose (what every p53 activator produces) stays in the WT residuals; wherever the
        drug-dose's TRIM72 response also differs between the groups (a WT lean among the raisers: p53_dependence)
        that drug-level gap enters b_WT - b_alt. The TP53-label permutation does not protect against it (it breaks
        the gap). Example: ii_active without covariates, P53_SCORE t_diff_line -10.4 with fe dd, -3.2 with ddxg.
  ddxg  drug-dose x TP53-group FE + line FE: each drug-dose has its own WT mean and its own altered mean, so
        b_WT and b_alt come only from line-to-line variation inside the same group and the same wells (more TRIM72
        than the other WT lines of that well, more or less p53 output than them). Exactly two separate regressions
        (WT lines, altered lines) sharing nothing. The FE of the primary test; dd rows are sensitivity rows.
Covariate sets: full = DD_beta (0 where the drug-dose has no consensus response, < 20 significant genes), DD_A
(relative abundance), S and G2M per-line effects (DD_r2_modules), bg_abs_r2 (mean |r2| over the 78 panel genes that
are not p53-related, not screen genes, not TRIM72; checks.csv lists them); no_cycle = full without S and G2M (for
cell-cycle read-outs, which overlap those modules); none = fixed effects only; full_base = full + trim72_base_x_dd
(the line's untreated TRIM72 level, log2 DMSO CPM z-scored over lines, x the drug-dose's TRIM72 log2FC from the
atlas: low-baseline lines get larger TRIM72 folds under a raiser); full_p53resp = full + p53resp_x_dd (the line's
p53 responsiveness from gene_panel/results/p53_functional_status.csv, z over lines, x the drug-dose's P53_ACTIVITY
z: a line that answers p53 activators strongly does so in every such drug-dose, whatever its TRIM72); full_rt =
full + FUS r2 + PYCARD-AS1 r2 (readthrough from FUS, each x TP53 group like the other covariates). Units: b = log2
change in the read-out per log2 change in TRIM72 (both corrected effects); *_per_sd_TRIM72 = per SD of the
residual TRIM72 (FE and covariates out).
Inference for diff = b_WT - b_alt (negative = more TRIM72 goes with less p53 output only where p53 works):
p_diff_twoway / ci_diff_*_twoway use the conservative two-way cluster SE, sqrt(max(V_drug + V_line - V_inter,
V_drug, V_line)) (drug compound and line clusters, CR1; t with min(G)-1 df): the plain two-way variance V_drug +
V_line - V_inter can fall below a one-way variance (for diff in 106 of the 270 D1 rows: 86 below V_line, 20 below
V_drug; e.g. P53_SCORE ii_active ddxg full: SE 0.0101 -> 0.0118, p 0.0054 -> 0.015, Holm over the variants 0.12),
so the larger of the three is used for every two-way SE, CI, p and q in these tables (also b_WT, b_alt, b_common,
the D2 q-values, the gene-level null, leave-one-out and joint-model tables). se_diff_twoway_from says which term
gave it; se_diff_twoway_cgm / p_diff_twoway_cgm keep the plain two-way value (the earlier p_diff_twoway, with the
larger one-way SE only where V2 <= 0), for comparison only. p_diff_tp53_label_perm permutes the TP53 labels over
the analysed lines (group sizes kept, whole model refitted, FE included for ddxg; statistic t = diff / line-cluster
SE, studentised) and is the design-based line-level test, conditional on the drug-doses analysed (it ignores
drug-to-drug variation, so in the 62 active drug-doses from 37 drugs it can be far smaller than the two-way p: fe
dd, P53_SCORE ii_active full, label p 0.028 vs two-way p 0.53). Read
a diff as supported only when both are small under fe ddxg. MDE: mde_diff_80 = 2.80 x the SD of the
label-permutation null of diff (smallest |b_WT - b_alt| detected with 80% power, two-sided 5%).

d1_two_way_models.csv     one row per read-out (P53_SCORE, MDM2, CDKN1A, FDXR, ZMAT3, DDB2, TP53I3, BBC3, TP53) x
                          fe x variant x covariate set; role = primary / secondary / sensitivity (above). Variants:
                          i_all (all drug-doses; covariates full, none, full_base, full_p53resp), ii_active (TRIM72
                          |z| >= 3 or P53_ACTIVITY z >= 3, 62 drug-doses; full, none, full_base, full_p53resp),
                          ii_trim72 (TRIM72 |z| >= 3 only, 23), ii_p53 (P53_ACTIVITY z >= 3 only, 50),
                          ii_active_no_plate3_13 (ii_active without the plate-3 / plate-13 wells, 58),
                          iii_readthrough_cov (all drug-doses, covariates full_rt: FUS and PYCARD-AS1 r2 in the
                          model), iii_readthrough_cov_active (ii_active, full_rt), iii_readthrough_subtracted (the
                          earlier readthrough variant: X = TRIM72_rt = TRIM72 r2 minus its pooled fit on FUS and
                          PYCARD-AS1 r2, readthrough_correction_fit.csv; covariates full), iv_no_plate3_13 (wells of
                          plates 3 and 13 left out, drug-dose means and covariates recomputed; 999 drug-doses);
                          drugdose_sets.csv. Columns: n_rows / n_drugdoses / n_fe_cells / n_drugs / n_lines_WT /
                          n_lines_alt; b_WT, b_alt with drug-cluster SE (CR1), 95% CI (t, G-1 df), p_*_drug,
                          conservative two-way SE/p; within-cell permutation p (TRIM72 shuffled across lines within
                          each FE cell: drug-dose for dd, drug-dose x group for ddxg; tests b = 0 and rejects
                          whenever slopes vary across drugs, even with a zero mean); diff with drug-cluster,
                          line-cluster and conservative two-way SE/CI/p (+ se_diff_twoway_from, *_cgm),
                          p_diff_perm_within_dd and its null SD, t_diff_line, p_diff_tp53_label_perm (studentised),
                          the unstudentised version, the null SD of diff (ci_diff_*_labelsd = diff +- 1.96 SD),
                          mde_diff_80, mde_diff_80_line_se = 2.80 x line-cluster SE, mde_diff_80_within_dd from the
                          within-cell null; b_common (one slope for all lines) with CI/p; sd_TRIM72_resid_*,
                          sd_Y_resid; attenuation_lambda_split_half (split-half reliability of the residual TRIM72 for
                          that variant, fe and covariate set; trim72_reliability.csv) and
                          mde_diff_80_attenuation_corrected = mde_diff_80 / lambda; q_bh_diff_label and
                          q_bh_diff_twoway = BH over the 9 read-outs within fe x variant x covariate set;
                          p_holm_variants_twoway / p_holm_variants_label = Holm over the 9 variants (each at its main
                          covariate set: full, full_rt for the iii_readthrough_cov variants) for P53_SCORE, within
                          fe (empty for the other rows); check_label_engine_minus_main and
                          check_label_engine_t_minus_main (the permutation engine at the true labels minus the main
                          fit: ~1e-16).
d1_line_slopes.csv        i_all and ii_active (full covariates), both fe: per line, the TRIM72 slope from one model with
                          line-specific TRIM72 AND covariate slopes (both FE), drug-cluster SE.
d1_line_slope_tests.csv   per read-out x variant x fe: line slopes WT vs altered (lines with >= 20 drug-dose rows):
                          mean difference with Welch t / CI / p, TP53-label permutation p of the Welch t (and of the
                          plain difference), MDE from the permutation SD of the difference; rank-based next to it:
                          median WT minus median altered, Hodges-Lehmann shift (median of all WT - altered slope
                          differences), Mann-Whitney U, AUC (P(WT slope > altered slope)) and p_mannwhitney; counts
                          of negative slopes. For fe ddxg the slopes are not refitted per permutation (the FE depend
                          on the labels): approximate.
d1_per_drugdose_contributions.csv.gz  i_all and ii_active (full covariates), both fe: per drug-dose and read-out, its
                          rows' share of the WT / altered TRIM72 variation (weight_share_*), its own slope on the
                          partialled data (slope_*_in_drugdose) and its contribution to b_WT, b_alt and diff (contrib_*:
                          sum over its rows of x~ y~ / total sum of x~^2). They add up to b_WT / b_alt exactly for
                          ddxg; for dd they leave out the WT-altered cross term (the two partialled TRIM72 columns
                          are correlated through the shared drug-dose FE), which is not small in the active set:
                          summed contrib_diff minus diff is at most 0.002 over the 9 read-outs in i_all (P53_SCORE
                          +0.0054 summed vs diff +0.0050) but up to 0.023 in ii_active (P53_SCORE -0.0278 vs
                          -0.0228); checks.csv rows 'per drug-dose contributions'. Read the dd contributions as a
                          ranking of drug-doses, not an exact decomposition.
d1_active_leave_one_drug_out.csv  ii_active (full), both fe: the model refitted without each drug (all its doses):
                          b_WT, b_alt, diff, line-cluster and conservative two-way p, next to the all-drug diff and p.
d1_active_leave_one_line_out.csv  ii_active (full), both fe: the model refitted without each line (dropped line, its
                          TP53 group): b_WT, b_alt, diff, line-cluster and conservative two-way p, next to the
                          all-line diff and p.
d1_active_joint_model.csv ii_active estimated inside one model over all drug-doses (full covariates, both fe): TRIM72
                          x TP53 group x (active, inactive) slopes and every covariate x group x (active, inactive),
                          so the line FE are estimated from all drug-doses (in ii_active alone they come from the 62
                          active drug-doses only). Contrasts: active b_WT - b_alt, inactive b_WT - b_alt, the
                          difference-in-differences active minus inactive (is the active-set diff different from
                          the rest, or the same slope gap with less noise?), and the four slopes; drug- and
                          line-cluster SE and p, the plain two-way SE (se_twoway_cgm) and the conservative two-way
                          SE (se_twoway, se_twoway_from), CI and p (min(G)-1 df).
d1_gene_null_genes.csv    gene-level null (is the pattern specific to p53 targets?): i_all and ii_active, full
                          covariates, both fe: the same model (b_WT, b_alt, diff, conservative two-way SE, t, p; no
                          permutations) for the D1 read-outs, each of the 21 P53_ACTIVITY members, each of the 78
                          non-p53 background panel genes and 500 random modules of 21 background genes (set column).
d1_gene_null_summary.csv  each D1 read-out's two-way t placed in its reference: P53_SCORE among the random background
                          modules, single genes among the background genes (reference mean / SD of diff and t,
                          fraction of reference t <= observed, empirical two-sided p). The modules share genes, lines
                          and drug-doses, so this is a competitive (specificity) test, not a test of a non-zero diff:
                          a read-out can sit outside the module null while its own CI includes 0. The row 'the 21
                          P53_ACTIVITY members as a set' is a camera-style competitive test (replaces the earlier
                          Mann-Whitney of member t vs background t, which treated the genes as independent): statistic
                          = mean member t minus mean background t (set_stat_*), variance = pooled within-set variance
                          of the t x a'Ra (a = 1/21 for members, -1/78 for background genes; R = correlation between
                          the genes' diff estimates from their drug-, line- and two-way cluster scores, the version
                          giving the largest variance used, never below independence), t with 97 df: p_set_camera;
                          set_vif_effective = a'Ra / (1/21 + 1/78) (variance inflation over independent genes),
                          set_vif_drug / _line / _twoway, rho_mean_members (mean correlation between two members'
                          estimates), rho_mean_members_background, rho_mean_background; p_set_independent = the same
                          test without the inflation. Caveat: the background genes also make up bg_abs_r2 (a
                          covariate).
d2_screen_models.csv      the same model (variant i_all, both fe) for each MG53-linked gene and module (module = mean
                          r2 of the members a line expresses) of mg53_p53/gene_modules.csv: NF-kB
                          (NFKBIA, TNFAIP3, CXCL8 + module), ferroptosis (SLC7A11, GPX4, CHAC1), apoptosis (BAX,
                          MCL1, PMAIP1), stress (ATF3, DDIT3 + module), PI3K-AKT/FOXO/FAK (TXNIP, IRS1, PTK2), cell
                          cycle (CCND1, KIF11), E2F targets (E2F1, CCNE1, CDT1, MCM3, MCM7, MYBL2, CDC25A + module;
                          none in the S_PHASE module), RAC1. primary = the covariate set of the BH family (no_cycle for
                          the cell-cycle and E2F read-outs, full otherwise); q_bh_* = BH over the primary rows within
                          each fe: diff (label-permutation p and conservative two-way p), b_common, b_WT and b_alt
                          (conservative two-way p). Non-primary rows (full covariates for the cell-cycle read-outs)
                          are sensitivity rows (no q). source = panel (T.expression_effects), pseudobulk
                          (corrected_effects) or module. The whole screen is secondary to the D1 primary test.
readthrough_correction_fit.csv  TRIM72 r2 on FUS r2 and PYCARD-AS1 r2 within drug-dose and line FE (all drug-doses):
                          slopes, drug-cluster SE, within-R2 (share of TRIM72's within variation explained);
                          PYCARD-AS1 r2 is kept in every line (it is below the atlas gene list). Used by
                          iii_readthrough_subtracted only.
trim72_reliability.csv    (v) measurement error of TRIM72, per variant, fe and covariate set (covset full / none):
                          split-half (each well x line's cells split at random into two halves, the panel's method
                          run on each half, halves averaged per drug-dose like the main data) and replicate wells
                          (drug-doses with 2+ used wells on different plates: first two wells; split-half is also given
                          for those drug-doses alone: the gap between the two is well- or plate-specific line
                          variation that both halves of a well share but another well does not). r_halves =
                          correlation of the residual TRIM72 (FE + covariates x group out, and FUS / PYCARD-AS1 x
                          group for the iii_readthrough rows) between the halves / wells;
                          reliability_full_spearman_brown = 2r/(1+r) (the full-data measure from two halves);
                          attenuation: observed b ~= lambda x true b for classical, independent measurement error.
drugdose_sets.csv         per drug-dose: TRIM72 z, P53_ACTIVITY z (panel), plates, membership of ii_trim72, ii_p53,
                          ii_active and iv_no_plate3_13.
analysis_cells.csv.gz     the per (drug-dose, line) values of the main data (all used wells): TRIM72 r2, TRIM72_rt,
                          D1 read-outs, screen read-outs, covariates (incl. trim72_base_x_dd, p53resp_x_dd, FUS and
                          PYCARD-AS1 r2), TRIM72 halves A and B.
checks.csv                pseudobulk vs gene_panel counts; corrected_effects vs the panel r2 and the atlas DD_lfc;
                          idarubicin per-line TRIM72 vs trim72_idarubicin/corrected; split-half bookkeeping; the
                          permutation engines (fast within-cell refit vs explicit projection; label engines at the
                          true labels vs the main fit) for both fe.
key_results.csv           the headline numbers, the primary test first. role = primary, secondary (other read-outs of
                          the primary model), sensitivity (every other fe x variant x covariate set, the line-slope
                          tests, leave-one-drug-out and leave-one-line-out ranges, the active set in the
                          all-drug-dose model), check (the gene-level null: P53_SCORE and the members as a set),
                          screen (D2) (rows with q < 0.1 and the D2 MDE range), context (reliability, readthrough
                          fit). Columns p_twoway (conservative), p_label_perm, q_twoway, q_label,
                          p_holm_variants_twoway, p_holm_variants_label, p_set_camera, mde_80 as defined above.

Runtime (4 CPUs, 15 GB RAM): the caches are keyed to the inputs (cache/manifest.json: real path of --data, sizes and
mtimes of atlas/effects/wells.csv, atlas/pseudobulk/group*, gene_panel/well_line.parquet and gene_panel/cells) and
rebuilt when they do not match (or with --recompute). Measured from scratch (empty cache/ and tables/, cold page
cache 11 min after a boot, another 4-process job running on the machine): 29.4 min wall, peak RSS 1.43 GB.
Caches 13.8 min: panel effects 1.6 min; the pseudobulk pass 11.3 min (it reads 20 GB of atlas/pseudobulk and is
I/O-bound: ~30 MB/s here; 12.9 min in the verifier's earlier cold run; faster when the files are in the page
cache); split-half counts 0.8 min. Models 15.6 min: D1 12 min (mostly the permutations), leave-one-out and joint
models 0.5 min, gene-level null 0.3 min, D2 2.7 min. With the caches in place ~15 min.
"""


# ============================================================================= main
def main():
    global DP_PANEL, BACKGROUND
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--data", default=os.environ.get("MG53_DATA") or os.environ.get("TAHOE_DATA")
                    or os.path.expanduser("~/Tahoe-100M"))
    ap.add_argument("--recompute", action="store_true", help="rebuild the caches")
    ap.add_argument("--perm", type=int, default=1000, help="within-drug-dose permutations per D1 design")
    ap.add_argument("--label-perm", type=int, default=2000, help="TP53-label permutations per D1 design")
    ap.add_argument("--screen-perm", type=int, default=500, help="within-drug-dose permutations per D2 design")
    ap.add_argument("--screen-label-perm", type=int, default=1000, help="TP53-label permutations per D2 design")
    ap.add_argument("--modules", type=int, default=500, help="random background modules for the gene-level null")
    ap.add_argument("--quick", action="store_true", help="few permutations (a test run)")
    a = ap.parse_args()
    if a.quick:
        a.perm, a.label_perm, a.screen_perm, a.screen_label_perm, a.modules = 100, 200, 50, 100, 100
    t0 = time.time()
    out = os.environ.get("MG53_OUT") or HERE
    cdir, tab = os.path.join(out, "cache"), os.path.join(out, "tables")
    os.makedirs(cdir, exist_ok=True)
    os.makedirs(tab, exist_ok=True)
    rng = np.random.default_rng(SEED)
    log(f"data {a.data}; out {out}")
    log("primary test (declared up front): fe {fe}, variant {variant}, covariates {covset}, read-out {readout}: "
        "b_WT - b_alt, conservative two-way SE; every other model is secondary or a sensitivity analysis"
        .format(**PRIMARY))
    manifest = validate_caches(cdir, a.data, a.recompute)
    grid = Grid(a.data)

    # one panel setup shared by the effects cache and the split-half (the setup takes ~20 s and ~1 GB)
    _setup, _held = DP.panel_setup, {}

    def setup_once(data):
        if data not in _held:
            _held[data] = _setup(data)
        return _held[data]
    DP.panel_setup = setup_once
    E = build_panel_cache(a.data, cdir)
    DP_PANEL = set(E.genes)
    BACKGROUND = [g for g in E.genes if g not in DP.NOT_BACKGROUND and g not in SCREEN_GENES and g != GENE]
    pbc = build_pseudobulk_cache(a.data, cdir, grid)
    pbe = pseudobulk_effects(a.data, cdir, grid, pbc)
    sh = build_split_half_counts(a.data, cdir)
    hA, hB, sh_check = split_half_effects(a.data, cdir, sh, grid)
    _held.clear()
    write_manifest(cdir, manifest)
    log(f"caches ready ({time.time() - t0:.0f} s; peak RSS {peak_gb():.2f} GB)")

    # TP53 groups (the panel's), drug-dose sets
    grp = E.L.reindex(grid.L)["tp53_group"]
    wt_line = (grp == "WT").to_numpy()
    if not ((grp == "WT") | (grp == "altered")).all():
        log("WARNING: lines without a TP53 group are kept as 'altered'")
    res_dir = os.path.join(a.data, "gene_panel", "results")
    tz = pd.read_csv(os.path.join(res_dir, f"{GENE}_drug_effects_by_dose.csv"))[["drug", "conc", "z_corrected"]]
    ps = pd.read_csv(os.path.join(res_dir, "pathway_scores_by_dose.csv"))
    ps = ps.loc[ps["score"] == "P53_ACTIVITY", ["drug", "conc", "z"]]
    dsets = grid.dd[["drug", "conc", "plates", "n_wells"]].copy()
    dsets["conc_key"] = dsets["conc"].round(6)
    for t_, c_, nm in ((tz, "z_corrected", "TRIM72_z"), (ps, "z", "P53_ACTIVITY_z")):
        t_ = t_.assign(conc_key=t_["conc"].round(6)).drop_duplicates(["drug", "conc_key"])
        dsets[nm] = dsets.merge(t_[["drug", "conc_key", c_]], on=["drug", "conc_key"], how="left")[c_].to_numpy()
    trim_mv = (dsets["TRIM72_z"].abs() >= 3).to_numpy()
    p53_act = (dsets["P53_ACTIVITY_z"] >= 3).to_numpy()
    active = trim_mv | p53_act
    keep_w = ~np.isin(grid.plate, DROP_PLATES)
    B_iv = grid.agg(keep_w)
    kept_iv = np.asarray(B_iv.sum(axis=1)).ravel() > 0
    dsets["in_ii_trim72"] = trim_mv
    dsets["in_ii_p53"] = p53_act
    dsets["in_ii_active"] = active
    dsets["in_iv_no_plate3_13"] = kept_iv
    dsets.drop(columns="conc_key").to_csv(os.path.join(tab, "drugdose_sets.csv"), index=False)
    alldd = np.ones(grid.nd, bool)
    # the line's p53 responsiveness (panel; z over lines) x the drug-dose's P53_ACTIVITY z
    fs = pd.read_csv(os.path.join(res_dir, "p53_functional_status.csv"), dtype={"cell_line_id": str})
    resp = fs.set_index("cell_line_id")["p53_responsiveness_log2"].reindex(grid.L).to_numpy(float)
    resp = (resp - np.nanmean(resp)) / np.nanstd(resp)
    p53resp_x_dd = dsets["P53_ACTIVITY_z"].to_numpy(float)[:, None] * resp[None, :]

    # per (drug-dose, line) data
    tabs = {"main": build_tables(E, grid, pbe, grid.B, p53resp_x_dd)[0],
            "iv": build_tables(E, grid, pbe, B_iv, p53resp_x_dd)[0]}
    rt, rtfit = readthrough_fit(tabs["main"], grid, alldd)
    tabs["main"]["TRIM72_rt"] = rt
    rtfit.to_csv(os.path.join(tab, "readthrough_correction_fit.csv"), index=False)
    halves = {"main": (Grid.dd_mean(grid.B, hA.astype(float)), Grid.dd_mean(grid.B, hB.astype(float))),
              "iv": (Grid.dd_mean(B_iv, hA.astype(float)), Grid.dd_mean(B_iv, hB.astype(float)))}
    log(f"per (drug-dose, line) data ready: {int(np.isfinite(tabs['main'][GENE]).sum())} cells with TRIM72; "
        f"active drug-doses {int(active.sum())} (TRIM72 |z| >= 3: {int(trim_mv.sum())}, P53_ACTIVITY z >= 3: "
        f"{int(p53_act.sum())}); drug-doses without plates 3/13 {int(kept_iv.sum())}")
    # variant -> (table, drug-dose mask, X column, extra residualisers for the reliability)
    VARIANTS = {"i_all": ("main", alldd, GENE, ()), "ii_active": ("main", active, GENE, ()),
                "ii_trim72": ("main", trim_mv, GENE, ()), "ii_p53": ("main", p53_act, GENE, ()),
                "ii_active_no_plate3_13": ("iv", active & kept_iv, GENE, ()),
                "iii_readthrough_subtracted": ("main", alldd, "TRIM72_rt", ("FUS", "PYCARD-AS1")),
                "iii_readthrough_cov": ("main", alldd, GENE, ("FUS", "PYCARD-AS1")),
                "iii_readthrough_cov_active": ("main", active, GENE, ("FUS", "PYCARD-AS1")),
                "iv_no_plate3_13": ("iv", kept_iv, GENE, ())}

    # (v) reliability of TRIM72 (split-half and replicate wells), under both FE structures
    rel_rows = []
    for fe in FES:
        for vname, (tk, ddm, _x, extra) in VARIANTS.items():
            XA, XB = halves[tk]
            for cs in ("full", "none"):
                covs = [tabs[tk][c] for c in COVSETS[cs]]
                ex = [tabs[tk][e] for e in extra]
                for r in reliability(XA, XB, ddm[:, None] & np.isfinite(tabs[tk][GENE]), covs, wt_line, grid, ex, fe):
                    rel_rows.append({"method": "split-half (cells within each well x line)", "variant": vname,
                                     "fe": fe, "covset": cs, "residualised_on": "FE + " +
                                     (cs if cs != "none" else "nothing else") + (" + FUS, PYCARD-AS1" if extra else "")}
                                    | r)
    # replicate wells: first two used wells of drug-doses with 2+ used wells on different plates
    wsel = grid.w[grid.used].copy()
    wsel["row"] = np.flatnonzero(grid.used)
    W1 = np.full((grid.nd, grid.nl), np.nan)
    W2 = np.full((grid.nd, grid.nl), np.nan)
    pw = panel_well_arrays(E, grid, [GENE])[GENE]
    n_rep = 0
    for d_, g in wsel.groupby("drugdose_row"):
        g = g.sort_values("plate")
        if len(g) >= 2 and g["plate"].nunique() >= 2:
            W1[d_], W2[d_] = pw[g["row"].iloc[0]], pw[g["row"].iloc[1]]
            n_rep += 1
    rep_dd = np.isfinite(W1).any(axis=1) & np.isfinite(W2).any(axis=1)
    XA, XB = halves["main"]
    for fe in FES:
        for r in reliability(XA, XB, rep_dd[:, None] & np.isfinite(tabs["main"][GENE]),
                             [tabs["main"][c] for c in COVSETS["full"]], wt_line, grid, (), fe):
            rel_rows.append({"method": "split-half (cells within each well x line)",
                             "variant": f"the {n_rep} replicated drug-doses only "
                                        "(compare with the replicate-well rows)",
                             "fe": fe, "covset": "full", "residualised_on": "FE + full"} | r)
        for cs in ("full", "none"):
            covs = [tabs["main"][c] for c in COVSETS[cs]]
            for r in reliability(W1, W2, np.isfinite(tabs["main"][GENE]), covs, wt_line, grid, (), fe):
                rr = dict(r)
                rr["reliability_single_well"] = rr.pop("r_halves")
                rr["reliability_full_spearman_brown"] = np.nan
                rel_rows.append({"method": "replicate wells (two plates)",
                                 "variant": f"{n_rep} drug-doses with 2+ wells",
                                 "fe": fe, "covset": cs,
                                 "residualised_on": "FE + " + (cs if cs != "none" else "nothing else")} | rr)
    REL = pd.DataFrame(rel_rows)
    REL.to_csv(os.path.join(tab, "trim72_reliability.csv"), index=False, float_format="%.6g")
    log("(v) reliability (split-half r, all lines, FE + full): " + "; ".join(
        f"{r['variant']} [{r['fe']}] {r['r_halves']:.3f}" for _, r in REL[
            (REL["tp53_group"] == "all lines") & REL["method"].str.startswith("split")
            & (REL["covset"] == "full")].iterrows()))

    # D1: both FE structures, every variant
    D1_COMBOS = [("i_all", "full"), ("i_all", "none"), ("i_all", "full_base"), ("i_all", "full_p53resp"),
                 ("ii_active", "full"), ("ii_active", "none"), ("ii_active", "full_base"),
                 ("ii_active", "full_p53resp"),
                 ("ii_trim72", "full"), ("ii_p53", "full"), ("ii_active_no_plate3_13", "full"),
                 ("iii_readthrough_subtracted", "full"), ("iii_readthrough_cov", "full_rt"),
                 ("iii_readthrough_cov_active", "full_rt"), ("iv_no_plate3_13", "full")]
    assert all(VARIANT_MAIN_COVSET[v] == c for v, c in D1_COMBOS if v not in ("i_all", "ii_active") or c == "full")
    specs = []
    for fe in FES:
        for vname, cs in D1_COMBOS:
            tk, ddm, xcol, _ex = VARIANTS[vname]
            xname = ("TRIM72_rt = TRIM72 r2 minus its fit on FUS, PYCARD-AS1 r2" if xcol != GENE else
                     "TRIM72_r2 (FUS, PYCARD-AS1 r2 x group as covariates)" if cs == "full_rt" else "TRIM72_r2")
            for ro in D1:
                specs.append({"family": "D1 p53", "module": "p53", "readout": ro, "variant": vname, "covset": cs,
                              "fe": fe, "xname": xname, "tabs": tk, "X": tabs[tk][xcol], "ddmask": ddm,
                              "B_within": a.perm, "B_label": a.label_perm})
    log(f"D1: p53 read-outs ({len(specs)} models)")
    # the readthrough-covariate variants draw their permutations from their own stream, so that adding them leaves
    # the random streams (and permutation p-values) of every other model as they were
    new_rt = np.array([s_["covset"] == "full_rt" for s_ in specs])
    D1a, SL = run_models([s_ for s_, k in zip(specs, new_rt) if not k], tabs, grid, wt_line, rng,
                         want_lines_for={("i_all", "full"), ("ii_active", "full")})
    D1b, _ = run_models([s_ for s_, k in zip(specs, new_rt) if k], tabs, grid, wt_line,
                        np.random.default_rng([SEED, 1]))
    D1T = pd.concat([D1a, D1b], ignore_index=True)
    order = {(s_["fe"], s_["variant"], s_["covset"], s_["readout"]): i for i, s_ in enumerate(specs)}
    D1T = D1T.iloc[np.argsort([order[k] for k in zip(D1T["fe"], D1T["variant"], D1T["covset"], D1T["readout"])],
                              kind="stable")].reset_index(drop=True)
    sh_ = REL[REL["method"].str.startswith("split") & (REL["tp53_group"] == "all lines")]
    lam = {(r["variant"], r["fe"], r["covset"]): r["reliability_full_spearman_brown"] for _, r in sh_.iterrows()}
    D1T["attenuation_lambda_split_half"] = [lam.get((v, f, "none" if c == "none" else "full"), np.nan)
                                            for v, f, c in zip(D1T["variant"], D1T["fe"], D1T["covset"])]
    D1T["mde_diff_80_attenuation_corrected"] = D1T["mde_diff_80"] / D1T["attenuation_lambda_split_half"]
    for col, pc in (("q_bh_diff_label", "p_diff_tp53_label_perm"), ("q_bh_diff_twoway", "p_diff_twoway")):
        D1T[col] = np.nan
        for _k, g in D1T.groupby(["fe", "variant", "covset"]):
            D1T.loc[g.index, col] = bh(g[pc].to_numpy())
    # role: the declared primary test, the other read-outs of its model (secondary), everything else sensitivity
    is_prim_model = ((D1T["fe"] == PRIMARY["fe"]) & (D1T["variant"] == PRIMARY["variant"])
                     & (D1T["covset"] == PRIMARY["covset"]))
    D1T.insert(0, "role", np.where(is_prim_model & (D1T["readout"] == PRIMARY["readout"]), "primary",
                                   np.where(is_prim_model, "secondary", "sensitivity")))
    # Holm over the variants (each at its main covariate set) for P53_SCORE, within fe
    for col, pc in (("p_holm_variants_twoway", "p_diff_twoway"), ("p_holm_variants_label", "p_diff_tp53_label_perm")):
        D1T[col] = np.nan
        for fe in FES:
            m_ = ((D1T["fe"] == fe) & (D1T["readout"] == "P53_SCORE")
                  & np.array([VARIANT_MAIN_COVSET.get(v) == c for v, c in zip(D1T["variant"], D1T["covset"])]))
            D1T.loc[m_, col] = holm(D1T.loc[m_, pc].to_numpy())
    D1T.to_csv(os.path.join(tab, "d1_two_way_models.csv"), index=False, float_format="%.6g")
    SL.to_csv(os.path.join(tab, "d1_line_slopes.csv"), index=False, float_format="%.6g")
    ST = slope_tests(SL, 20000, rng)
    ST.to_csv(os.path.join(tab, "d1_line_slope_tests.csv"), index=False, float_format="%.6g")
    log("D1: per drug-dose contributions (i_all, ii_active), leave-one-drug-out and leave-one-line-out (ii_active), "
        "the active set inside the all-drug-dose model, both FE")
    parts, lodos, lolos, joints = [], [], [], []
    for fe in FES:
        pa, _, _ = breakdown(tabs["main"], grid, wt_line, alldd, "i_all", fe=fe)
        pb_, lo_, ll_ = breakdown(tabs["main"], grid, wt_line, active, "ii_active", fe=fe, lodo=True)
        parts += [pa, pb_]
        lodos.append(lo_)
        lolos.append(ll_)
        joints.append(joint_active(tabs["main"], grid, wt_line, active, fe))
    PDD = pd.concat(parts)
    PDD.to_csv(os.path.join(tab, "d1_per_drugdose_contributions.csv.gz"), index=False, float_format="%.5g")
    # do the per drug-dose contributions add up to the fitted slopes? (exactly for ddxg; for dd the WT-altered cross
    # term of the shared drug-dose FE is left out): sum of the contributions minus the main fit, per read-out
    ctr = []
    for (fe, va, ro), g in PDD.groupby(["fe", "variant", "readout"], sort=False):
        r = D1T[(D1T["fe"] == fe) & (D1T["variant"] == va) & (D1T["covset"] == "full")
                & (D1T["readout"] == ro)].iloc[0]
        ctr.append({"fe": fe, "variant": va, "readout": ro, "diff": r["diff"],
                    "sum_contrib_diff": g["contrib_diff"].sum(), "gap_diff": g["contrib_diff"].sum() - r["diff"],
                    "gap_WT": g["contrib_WT"].sum() - r["b_WT"], "gap_alt": g["contrib_alt"].sum() - r["b_alt"]})
    CTR = pd.DataFrame(ctr)
    lo = pd.concat(lodos)
    lo.to_csv(os.path.join(tab, "d1_active_leave_one_drug_out.csv"), index=False, float_format="%.6g")
    LL = pd.concat(lolos)
    LL.to_csv(os.path.join(tab, "d1_active_leave_one_line_out.csv"), index=False, float_format="%.6g")
    JA = pd.concat(joints)
    JA.to_csv(os.path.join(tab, "d1_active_joint_model.csv"), index=False, float_format="%.6g")
    for _, r in JA[(JA["readout"] == "P53_SCORE") & JA["contrast"].str.contains("b_WT - b_alt|differences")].iterrows():
        log(f"  P53_SCORE [{r['fe']}] {r['contrast']}: {r['estimate']:+.4f} (p conservative two-way "
            f"{r['p_twoway']:.3g}, line {r['p_line']:.3g})")
    log("D1: gene-level null (p53 targets vs non-p53 panel genes and random background modules)")
    GN, GS = gene_null(E, grid, tabs["main"], wt_line, {"i_all": alldd, "ii_active": active}, rng, R=a.modules)
    GN.to_csv(os.path.join(tab, "d1_gene_null_genes.csv"), index=False, float_format="%.6g")
    GS.to_csv(os.path.join(tab, "d1_gene_null_summary.csv"), index=False, float_format="%.6g")

    # D2 screen, both FE structures
    specs = []
    for fe in FES:
        for name, pm, genes, as_module, cs in SCREEN:
            for ro in genes + ([f"{name} module"] if as_module else []):
                for c_ in [cs] + (["full"] if cs != "full" else []):
                    specs.append({"family": "D2 screen", "module": name, "readout": ro, "variant": "i_all",
                                  "covset": c_, "fe": fe, "xname": "TRIM72_r2", "tabs": "main",
                                  "X": tabs["main"][GENE], "ddmask": alldd, "B_within": a.screen_perm,
                                  "B_label": a.screen_label_perm, "primary": c_ == cs, "panel_module": pm})
    log(f"D2: screen of MG53-linked pathways ({len(specs)} models)")
    D2T, _ = run_models(specs, tabs, grid, wt_line, rng)
    D2T["primary"] = [s["primary"] for s in specs]
    D2T["panel_module"] = [s["panel_module"] for s in specs]
    D2T["source"] = ["panel" if r in DP_PANEL else ("module" if r.endswith("module") else "pseudobulk")
                     for r in D2T["readout"]]
    for col, pc in (("q_bh_diff_label", "p_diff_tp53_label_perm"), ("q_bh_diff_twoway", "p_diff_twoway"),
                    ("q_bh_common", "p_common_twoway"), ("q_bh_WT", "p_WT_twoway"), ("q_bh_alt", "p_alt_twoway")):
        D2T[col] = np.nan
        for fe in FES:
            m_ = D2T["primary"].to_numpy() & (D2T["fe"] == fe).to_numpy()
            D2T.loc[m_, col] = bh(D2T.loc[m_, pc].to_numpy())
    D2T.to_csv(os.path.join(tab, "d2_screen_models.csv"), index=False, float_format="%.6g")

    # per-cell data table
    m = tabs["main"]
    d_, l_ = np.nonzero(np.isfinite(m[GENE]))
    cols = {"drugdose_row": d_, "drug": grid.dd["drug"].to_numpy()[d_], "conc": grid.dd["conc"].to_numpy()[d_],
            "cell_line_id": np.array(grid.L)[l_], "cell_line": grid.lines["cell_name"].to_numpy()[l_],
            "tp53_group": np.where(wt_line[l_], "WT", "altered"), "in_ii_active": active[d_],
            "in_ii_trim72": trim_mv[d_], "in_ii_p53": p53_act[d_],
            "TRIM72_r2": m[GENE][d_, l_], "TRIM72_rt": m["TRIM72_rt"][d_, l_],
            "TRIM72_r2_halfA": halves["main"][0][d_, l_], "TRIM72_r2_halfB": halves["main"][1][d_, l_],
            "FUS_r2": m["FUS"][d_, l_], "PYCARD-AS1_r2": m["PYCARD-AS1"][d_, l_]}
    for k in D1 + [s for s in SCREEN_GENES if s not in D1] + [f"{s[0]} module" for s in SCREEN if s[3]] + \
            COVSETS["full"] + ["trim72_base_x_dd", "p53resp_x_dd"]:
        cols[k] = m[k][d_, l_]
    pd.DataFrame(cols).to_csv(os.path.join(tab, "analysis_cells.csv.gz"), index=False, float_format="%.4g")

    CK = checks(E, grid, pbe, pbc, tabs, a.data, sh_check)
    # the permutation engines: fast within-cell refit vs explicit projection; label engines at the true labels
    for fe in FES:
        X = tabs["main"][GENE]
        covs = [tabs["main"][c] for c in COVSETS["full"]]
        ok = np.isfinite(X) & np.isfinite(tabs["main"]["P53_SCORE"])
        for c in covs:
            ok &= np.isfinite(c)
        des = Design(ok, X, covs, wt_line, grid.drug_id, fe)
        _my, yt = resid_y(des, tabs["main"]["P53_SCORE"][des.d, des.l].astype(float)[:, None])
        CK.loc[len(CK)] = {"check": f"within-cell permutation, fast formula vs explicit projection, max |diff| of "
                                    f"b_WT, b_alt, b_common (i_all, full, P53_SCORE, FE {fe})",
                           "value": within_dd_perm_check(des, yt, rng), "n": des.n, "note": ""}
    for (fe, va), g in CTR.groupby(["fe", "variant"], sort=False):
        p5 = g[g["readout"] == "P53_SCORE"].iloc[0]
        CK.loc[len(CK)] = {"check": f"per drug-dose contributions ({va}, full, FE {fe}): sum of contrib_diff minus "
                                    "the fitted diff, max |gap| over the 9 D1 read-outs",
                           "value": float(g["gap_diff"].abs().max()), "n": len(g),
                           "note": f"P53_SCORE: sum {p5['sum_contrib_diff']:+.5f} vs diff {p5['diff']:+.5f}; "
                                   f"max |gap| of b_WT {g['gap_WT'].abs().max():.2g}, of b_alt "
                                   f"{g['gap_alt'].abs().max():.2g}"
                                   + (" (exact for ddxg)" if fe == "ddxg" else
                                      " (dd: the WT-altered cross term is left out)")}
    for nm_, T_ in (("D1", D1T), ("D2", D2T)):
        for fe in FES:
            g = T_[T_["fe"] == fe]
            CK.loc[len(CK)] = {"check": f"{nm_} TP53-label engine at the true labels minus the main fit (FE {fe}): "
                                        "max |diff| of b_WT - b_alt; of t",
                               "value": float(g["check_label_engine_minus_main"].abs().max()), "n": len(g),
                               "note": f"t: {g['check_label_engine_t_minus_main'].abs().max():.2g}"}
    CK.to_csv(os.path.join(tab, "checks.csv"), index=False)

    # key results (role: primary / secondary / sensitivity / check / screen / context; the primary row first)
    kr = []

    def model_row(section, r, what):
        return {"section": section, "role": r["role"], "what": what, "fe": r["fe"], "n": r["n_rows"],
                "estimate": r["diff"], "ci_lo": r["ci_diff_lo_twoway"], "ci_hi": r["ci_diff_hi_twoway"],
                "p_twoway": r["p_diff_twoway"], "p_label_perm": r["p_diff_tp53_label_perm"],
                "q_label": r["q_bh_diff_label"], "q_twoway": r["q_bh_diff_twoway"],
                "p_holm_variants_twoway": r["p_holm_variants_twoway"],
                "p_holm_variants_label": r["p_holm_variants_label"], "mde_80": r["mde_diff_80"],
                "detail": f"b_WT {r['b_WT']:+.4f} (two-way p {r['p_WT_twoway']:.3g}); b_alt {r['b_alt']:+.4f} "
                          f"(two-way p {r['p_alt_twoway']:.3g}); drug-cluster p {r['p_diff_drug']:.3g}; "
                          f"line-cluster p {r['p_diff_line']:.3g}; conservative SE from the {r['se_diff_twoway_from']} "
                          f"variance (plain two-way p {r['p_diff_twoway_cgm']:.3g}); {r['n_drugdoses']} drug-doses; "
                          f"MDE corrected for split-half attenuation {r['mde_diff_80_attenuation_corrected']:.3g}"}
    for _, r in D1T.iterrows():
        if (r["variant"], r["covset"]) in (("i_all", "full"), ("ii_active", "full")) or r["readout"] == "P53_SCORE":
            kr.append(model_row("D1", r, f"{r['readout']} [{r['variant']}, {r['covset']}]: b_WT - b_alt"))
    for _, r in ST.iterrows():
        if r["readout"] in ("P53_SCORE", "MDM2", "CDKN1A", "ZMAT3"):
            kr.append({"section": "D1 line slopes", "role": "sensitivity",
                       "what": f"{r['readout']} [{r['variant']}]: mean line slope WT - altered", "fe": r["fe"],
                       "n": r["n_lines_WT"] + r["n_lines_alt"],
                       "estimate": r["diff_mean_WT_minus_alt"], "ci_lo": r["ci_lo_welch"], "ci_hi": r["ci_hi_welch"],
                       "p_label_perm": r["p_tp53_label_perm"], "mde_80": r["mde_diff_80"],
                       "detail": f"Welch p {r['p_welch']:.3g}; rank-based: Hodges-Lehmann shift "
                                 f"{r['hodges_lehmann_WT_minus_alt']:+.4f}, median WT - median altered "
                                 f"{r['diff_median_WT_minus_alt']:+.4f}, Mann-Whitney p {r['p_mannwhitney']:.3g}; "
                                 f"{r['n_WT_negative']}/{r['n_lines_WT']} WT and "
                                 f"{r['n_alt_negative']}/{r['n_lines_alt']} altered lines with a negative slope"})
    for (fe, ro), g in lo.groupby(["fe", "readout"], sort=False):
        kr.append({"section": "D1 ii_active leave-one-drug-out", "role": "sensitivity",
                   "what": f"{ro}: b_WT - b_alt without each drug",
                   "fe": fe, "n": len(g), "estimate": g["diff_all_drugs"].iloc[0], "ci_lo": g["diff"].min(),
                   "ci_hi": g["diff"].max(), "p_twoway": g["p_diff_twoway"].max(),
                   "detail": "ci_lo / ci_hi = smallest / largest diff over the drops; p_twoway = largest two-way p "
                             f"over the drops (drop giving it: {g.loc[g['p_diff_twoway'].idxmax(), 'dropped_drug']}); "
                             f"all drugs: two-way p {g['p_diff_twoway_all_drugs'].iloc[0]:.3g}; drops with two-way "
                             f"p > 0.05: {int((g['p_diff_twoway'] > 0.05).sum())} of {len(g)}"})
    for (fe, ro), g in LL.groupby(["fe", "readout"], sort=False):
        kr.append({"section": "D1 ii_active leave-one-line-out", "role": "sensitivity",
                   "what": f"{ro}: b_WT - b_alt without each line",
                   "fe": fe, "n": len(g), "estimate": g["diff_all_lines"].iloc[0], "ci_lo": g["diff"].min(),
                   "ci_hi": g["diff"].max(), "p_twoway": g["p_diff_twoway"].max(),
                   "detail": "ci_lo / ci_hi = smallest / largest diff over the drops; p_twoway = largest two-way p "
                             f"over the drops (drop giving it: {g.loc[g['p_diff_twoway'].idxmax(), 'dropped_line']}); "
                             f"all lines: two-way p {g['p_diff_twoway_all_lines'].iloc[0]:.3g}; drops with two-way "
                             f"p > 0.05: {int((g['p_diff_twoway'] > 0.05).sum())} of {len(g)}"})
    for _, r in JA[JA["readout"].isin(["P53_SCORE", "MDM2", "CDKN1A", "ZMAT3"])
                   & JA["contrast"].str.contains("b_WT - b_alt|differences")].iterrows():
        kr.append({"section": "D1 ii_active in the all-drug-dose model", "role": "sensitivity",
                   "what": f"{r['readout']} [{r['covset']}]: {r['contrast']}", "fe": r["fe"], "n": r["n_rows"],
                   "estimate": r["estimate"], "ci_lo": r["ci_lo_twoway"], "ci_hi": r["ci_hi_twoway"],
                   "p_twoway": r["p_twoway"],
                   "detail": f"one model over all drug-doses (line FE from all of them; TRIM72 and covariate slopes "
                             f"separate for the {r['n_drugdoses_active']} active and {r['n_drugdoses_inactive']} "
                             f"inactive drug-doses); drug-cluster p {r['p_drug']:.3g}; line-cluster p "
                             f"{r['p_line']:.3g}; conservative SE from the {r['se_twoway_from']} variance"})
    for _, r in GS.iterrows():
        if r["readout"] == "P53_SCORE" or r["readout"].startswith("the "):
            st_ = r["readout"].startswith("the ")
            kr.append({"section": "D1 gene-level null", "role": "check", "what": f"{r['readout']} [{r['variant']}, "
                       f"full] vs {r['reference']}", "fe": r["fe"], "n": r["n_ref"], "estimate": r["diff"],
                       "p_twoway": r.get("p_diff_twoway", np.nan),
                       "detail": (f"camera-style set test: mean member t {r['t_diff_twoway']:+.2f} minus mean "
                                  f"background t {r['ref_mean_t']:+.2f} = {r['set_stat_mean_t_members_minus_background']:+.2f}"
                                  f" (SE {r['set_se']:.2f}; effective VIF {r['set_vif_effective']:.2f} from the "
                                  f"{r['set_vif_from']} correlation, mean member-member rho "
                                  f"{r['rho_mean_members']:.3f}); p {r['p_set_camera']:.3g} (genes treated as "
                                  f"independent: {r['p_set_independent']:.3g})") if st_ else
                                 (f"t {r['t_diff_twoway']:+.2f} vs reference mean t {r['ref_mean_t']:+.2f} (SD "
                                  f"{r['ref_sd_t']:.2f}), reference mean diff {r['ref_mean_diff']:+.4f}; fraction of "
                                  f"reference t <= observed {r['frac_ref_t_le_obs']:.3f}; empirical two-sided p "
                                  f"{r['p_empirical_two_sided']:.3g}")})
            if st_:
                kr[-1]["p_label_perm"] = np.nan
                kr[-1]["p_set_camera"] = r["p_set_camera"]
    for _, r in D2T[D2T["primary"]].iterrows():
        if min(r["q_bh_diff_label"], r["q_bh_diff_twoway"], r["q_bh_common"]) < 0.1:
            kr.append({"section": "D2 (q < 0.1)", "role": "screen (D2)",
                       "what": f"{r['readout']} ({r['module']}): b_WT - b_alt; b_common",
                       "fe": r["fe"], "n": r["n_rows"], "estimate": r["diff"], "ci_lo": r["ci_diff_lo_twoway"],
                       "ci_hi": r["ci_diff_hi_twoway"], "p_twoway": r["p_diff_twoway"],
                       "p_label_perm": r["p_diff_tp53_label_perm"], "q_label": r["q_bh_diff_label"],
                       "q_twoway": r["q_bh_diff_twoway"], "mde_80": r["mde_diff_80"],
                       "detail": f"b_common {r['b_common']:+.4f} (two-way p {r['p_common_twoway']:.3g}, q "
                                 f"{r['q_bh_common']:.3g}); b_WT {r['b_WT']:+.4f}; b_alt {r['b_alt']:+.4f}"})
    for fe in FES:
        g = D2T[D2T["primary"] & (D2T["fe"] == fe)]
        kr.append({"section": "D2 summary", "role": "screen (D2)", "what": "screen read-outs (primary covariate set)",
                   "fe": fe, "n": len(g),
                   "estimate": float(np.median(g["mde_diff_80"])), "ci_lo": float(g["mde_diff_80"].min()),
                   "ci_hi": float(g["mde_diff_80"].max()),
                   "detail": f"estimate / ci = median / min / max MDE (80%) of b_WT - b_alt; read-outs with "
                             f"q_label < 0.1: {int((g['q_bh_diff_label'] < 0.1).sum())}, q_twoway < 0.1: "
                             f"{int((g['q_bh_diff_twoway'] < 0.1).sum())}, q_common < 0.1: "
                             f"{int((g['q_bh_common'] < 0.1).sum())}"})
    for _, r in REL[REL["tp53_group"] == "all lines"].iterrows():
        kr.append({"section": "(v) reliability", "role": "context",
                   "what": f"{r['method']} [{r['variant']}; {r['residualised_on']}]",
                   "fe": r["fe"], "n": r["n_rows"], "estimate": r.get("r_halves") if pd.notna(r.get("r_halves")) else
                   r.get("reliability_single_well"), "detail": f"full-data reliability "
                   f"{r['reliability_full_spearman_brown']:.3f}" if pd.notna(r["reliability_full_spearman_brown"])
                   else "single-well reliability (correlation of two wells on two plates)"})
    for _, r in rtfit.iterrows():
        kr.append({"section": "(iii) readthrough fit", "role": "context",
                   "what": f"TRIM72 r2 on {r['predictor']} (within FE)",
                   "fe": "dd", "n": r["n_rows"], "estimate": r["slope"], "p_twoway": np.nan,
                   "detail": f"drug-cluster p {r['p_drug']:.3g}; within R2 of TRIM72 explained by FUS + PYCARD-AS1 "
                             f"{r['within_R2_of_TRIM72']:.3f}"})
    KR = pd.DataFrame(kr)
    KR = pd.concat([KR[KR["role"] == "primary"], KR[KR["role"] != "primary"]], ignore_index=True)
    KR.to_csv(os.path.join(tab, "key_results.csv"), index=False, float_format="%.6g")
    pr = KR.iloc[0]
    log(f"PRIMARY {pr['what']} [fe {pr['fe']}]: {pr['estimate']:+.4f} (95% CI {pr['ci_lo']:+.4f} to "
        f"{pr['ci_hi']:+.4f}; conservative two-way p {pr['p_twoway']:.3g}; label-permutation p "
        f"{pr['p_label_perm']:.3g})")
    for f in ("d1_per_drugdose_contributions.csv",):              # replaced by the gzipped version
        if os.path.exists(os.path.join(tab, f)):
            os.remove(os.path.join(tab, f))
    with open(os.path.join(tab, "README_tables.txt"), "w", encoding="utf-8") as fh:
        fh.write(README)
    print(CK.to_string(index=False, max_colwidth=60))
    log(f"tables written to {tab}; peak RSS {peak_gb():.2f} GB; wall {time.time() - t0:.0f} s")


DP_PANEL, BACKGROUND = set(), []

if __name__ == "__main__":
    main()
