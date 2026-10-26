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

    Y = drug-dose FE + line FE + b_WT * TRIM72 * WT + b_alt * TRIM72 * altered
        + sum_k (c_k,WT * C_k * WT + c_k,alt * C_k * altered) + e

C (per drug-dose x line): DD_beta (the line's strength of the drug's consensus response; 0 where the drug-dose has
< 20 significant genes and no consensus), DD_A (relative abundance: depletion), the line's S and G2M effects
(DD_r2_modules), and the line's mean |r2| over non-p53, non-screen panel genes (general responsiveness).
Primary estimand b_WT - b_alt (negative = more TRIM72 goes with less p53 output only where p53 works).

Inference: cluster-robust SE by drug compound (CR1), by line, and two-way (drug, line); a permutation null that
shuffles TRIM72 across lines WITHIN each drug-dose (keeps the drug structure; tests b = 0); a TP53-label permutation
over lines (group sizes kept, covariate interactions refitted; the null for b_WT - b_alt, lines being the units of
the genotype contrast), studentised by the line-cluster SE (primary p; robust to WT and altered lines differing in
spread). Minimum detectable b_WT - b_alt (80% power, two-sided 5%) = 2.80 x the label-permutation SD.
Second stage: per-line TRIM72 slopes (line-specific covariate slopes), WT vs altered mean (Welch; label permutation
of the Welch t). Which drug-doses carry the estimate: per drug-dose contributions; leave-one-drug-out (active set).
Covariate set full_base adds the line's untreated TRIM72 level x the drug-dose's TRIM72 effect (the fold-change
inflation of low-baseline lines).

Variants (D1): (i) all drug-doses (covariates: full, full_base, none); (ii) drug-doses that move TRIM72 (|z| >= 3) or
activate p53 (P53_ACTIVITY z >= 3) (full, full_base; and without the plate-3/13 wells); (iii) readthrough-corrected
TRIM72 = TRIM72 r2 minus its fit on FUS and
PYCARD-AS1 r2 (slopes within drug-dose and line, pooled over lines); (iv) without the plate-3 and plate-13 wells;
(v) TRIM72 measurement error: split-half (cells of each well x line split at random, the method run on each half)
and replicate-well reliability of the residual TRIM72 variation, and the implied attenuation of b.
D2 screen: the same model for each MG53-linked module of mg53_perturbation/assay_panel/panel.csv (NF-kB, ferroptosis,
apoptosis, stress, PI3K-AKT/FOXO/FAK, cell cycle + E2F targets, RAC1); BH across the screen.

    python3 two_way.py [--data DIR (default $MG53_DATA, $TAHOE_DATA or ~/Tahoe-100M)] [--recompute]
                       [--perm 1000] [--label-perm 2000] [--screen-perm 500] [--quick]

Reads <data>/atlas/effects, <data>/atlas/pseudobulk (one streamed pass, ~4 min), <data>/gene_panel (well_line,
cells/*.parquet for the split-half, ~5 min; results/), <data>/metadata/gene_metadata.parquet. Caches take ~11 min
once, the models ~10 min (4 CPUs, peak RSS ~1.4 GB). Writes tables to
$MG53_OUT/tables (default <this folder>/tables) and caches to $MG53_OUT/cache (default <this folder>/cache); nothing
under the data folder. numpy / pandas / scipy only.
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
           "full_base": ["beta", "A", "S", "G2M", "bg_abs_r2", "trim72_base_x_dd"]}
DROP_PLATES = ("plate3", "plate13")


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
    with < 2 rows dropped), the FE projection and the covariate x TP53-group nuisance."""

    def __init__(self, ok, X, covs, wt_line, drug_id):
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
        self.fe = FE(self.d, self.l)
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
    """TRIM72 shuffled across lines within each drug-dose (rows of the analysis); refit. Returns B x 3: b_WT,
    b_alt, b_common. Uses ytil = R y (R = the FE + covariate residual maker, symmetric idempotent), so x~'y~ = v'y~
    and x~'x~ = v'Rv = sum v^2 - sum_dd (dd sum of v)^2 / n_dd - |W'v|^2 with W = [line-FE basis, covariate basis]
    (both orthonormal, orthogonal to the dd dummies and to each other): no full projection per permutation."""
    n = des.n
    order0 = np.argsort(des.d, kind="stable")
    dkey = des.d.astype(float)[:, None]
    W = np.column_stack([des.fe.Q, des.Qc]) if des.Qc.shape[1] else des.fe.Q
    D, cnt = des.fe.D, des.fe.cnt
    wtf = des.wt.astype(float)[:, None]
    out = np.empty((B, 3))
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
        c1, c2 = ytil @ V1, ytil @ V2
        det = a11 * a22 - a12 ** 2
        out[c0:c0 + nb, 0] = (a22 * c1 - a12 * c2) / det
        out[c0:c0 + nb, 1] = (a11 * c2 - a12 * c1) / det
        out[c0:c0 + nb, 2] = (c1 + c2) / (a11 + 2 * a12 + a22)
    return out


def within_dd_perm_direct(des, ytil, X_perm_rows):
    """The same refit by explicit projection, for one permuted TRIM72 vector (a check of within_dd_perm)."""
    R = des.resid(np.column_stack([np.where(des.wt, X_perm_rows, 0.0), np.where(des.wt, 0.0, X_perm_rows)]))
    b = np.linalg.solve(R.T @ R, R.T @ ytil)
    xc = R.sum(axis=1)
    return b[0], b[1], float(xc @ ytil / (xc @ xc))


def label_perm(des, MY, B, rng, chunk=250):
    """TP53 labels permuted over the analysed lines (group sizes kept); the model (TRIM72 x group and every
    covariate x group) refitted through the per-line Gram blocks, with its line-cluster (CR1) SE, so the permuted
    statistic can be studentised (t = diff / SE_line: valid when the two groups differ in residual spread, e.g. WT
    lines responding more to p53 activators). Returns observed diff and t (identity labels: a check of the main
    fit) and the null diffs and t."""
    Pm, G, k, li, H = des.line_blocks()
    nb = 1 + des.K
    m, q, n = k * nb, 2 * nb, des.n
    gy = Pm.T @ MY
    Lsp = sparse.csr_matrix((np.ones(n), (li, np.arange(n))), shape=(k, n))
    h = np.asarray(Lsp @ (Pm * MY[:, None]))              # per line: sum of Pm_i * MY_i
    Gb, gyb, Hf = G.reshape(nb, k, nb, k), gy.reshape(nb, k), H.reshape(k * m, m)
    cfac = k / (k - 1) * (n - 1) / max(n - des.p_all, 1)
    cvec = np.zeros(q)
    cvec[0], cvec[1] = 1.0, -1.0                          # (TRIM72, WT) minus (TRIM72, altered)

    def stat(U):
        Bc = U.shape[0]
        S = np.stack([U, 1.0 - U], axis=1)                 # (Bc, 2 groups, k lines)
        T1 = np.einsum("bsk,akcl->bsacl", S, Gb)
        Mx = np.einsum("bsacl,btl->basct", T1, S).reshape(Bc, q, q)
        g_ = np.einsum("bsk,ak->bas", S, gyb).reshape(Bc, q)
        beta = np.linalg.solve(Mx, g_[..., None])[..., 0]
        w = np.linalg.solve(Mx, np.broadcast_to(cvec, (Bc, q))[..., None])[..., 0]
        br, wr = beta.reshape(Bc, nb, 2), w.reshape(Bc, nb, 2)
        Ab = (br[:, :, 0, None] * U[:, None, :] + br[:, :, 1, None] * (1.0 - U)[:, None, :]).reshape(Bc, m)
        Aw = (wr[:, :, 0, None] * U[:, None, :] + wr[:, :, 1, None] * (1.0 - U)[:, None, :]).reshape(Bc, m)
        HAw = (Hf @ Aw.T).reshape(k, m, Bc)
        sl = h @ Aw.T - np.einsum("kmb,bm->kb", HAw, Ab)  # per line: contrast-weighted score sum
        se = np.sqrt(cfac * (sl ** 2).sum(axis=0))
        d = beta[:, 0] - beta[:, 1]
        return d, d / se

    wt0 = des.wt_line[des.fe.lu].astype(float)
    d0, t0 = stat(wt0[None, :])
    nd_, nt_ = [], []
    for c0 in range(0, B, chunk):
        U = np.stack([rng.permutation(wt0) for _ in range(min(chunk, B - c0))])
        d, t = stat(U)
        nd_.append(d)
        nt_.append(t)
    return float(d0[0]), float(t0[0]), np.concatenate(nd_), np.concatenate(nt_)


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


def fit(des, y, B_within, B_label, rng, want_lines=False):
    n = des.n
    MY = des.fe.M(y)
    ytil = MY - des.Qc @ (des.Qc.T @ MY) if des.Qc.shape[1] else MY
    Xt = des.xt
    bread = np.linalg.inv(Xt.T @ Xt)
    b = bread @ (Xt.T @ ytil)
    e = ytil - Xt @ b
    Vd, Gd = cluster_vcov(Xt, e, des.drug, bread, n, des.p_all)
    Vl, Gl = cluster_vcov(Xt, e, des.l, bread, n, des.p_all)
    Vi, _ = cluster_vcov(Xt, e, des.drug.astype(np.int64) * 1000 + des.l, bread, n, des.p_all)
    V2 = Vd + Vl - Vi
    c = np.array([1.0, -1.0])
    out = {"n_rows": n, "n_drugdoses": len(des.fe.du), "n_drugs": int(Gd),
           "n_lines_WT": int(len(np.unique(des.l[des.wt]))), "n_lines_alt": int(len(np.unique(des.l[~des.wt])))}
    td, tl = stats.t.ppf(0.975, Gd - 1), stats.t.ppf(0.975, min(Gd, Gl) - 1)
    for i, nm in ((0, "WT"), (1, "alt")):
        se, se2 = np.sqrt(Vd[i, i]), np.sqrt(max(V2[i, i], 0)) if V2[i, i] > 0 else np.sqrt(max(Vd[i, i], Vl[i, i]))
        out.update({f"b_{nm}": b[i], f"se_{nm}_drug": se, f"ci_{nm}_lo": b[i] - td * se, f"ci_{nm}_hi": b[i] + td * se,
                    f"p_{nm}_drug": tp(b[i], se, Gd - 1), f"se_{nm}_twoway": se2,
                    f"p_{nm}_twoway": tp(b[i], se2, min(Gd, Gl) - 1)})
    dif = b[0] - b[1]
    vd, vl, v2 = c @ Vd @ c, c @ Vl @ c, c @ V2 @ c
    se_d, se_l = np.sqrt(vd), np.sqrt(vl)
    se_2 = np.sqrt(v2) if v2 > 0 else max(se_d, se_l)
    out.update({"diff": dif, "se_diff_drug": se_d, "ci_diff_lo_drug": dif - td * se_d, "ci_diff_hi_drug": dif + td * se_d,
                "p_diff_drug": tp(dif, se_d, Gd - 1), "se_diff_line": se_l, "p_diff_line": tp(dif, se_l, Gl - 1),
                "se_diff_twoway": se_2, "ci_diff_lo_twoway": dif - tl * se_2, "ci_diff_hi_twoway": dif + tl * se_2,
                "p_diff_twoway": tp(dif, se_2, min(Gd, Gl) - 1)})
    # common slope (one TRIM72 slope for all lines, covariates still by group)
    xc = Xt.sum(axis=1)
    bc = float(xc @ ytil / (xc @ xc))
    ec = ytil - bc * xc
    bc_ = np.array([[1 / (xc @ xc)]])
    Vc, _ = cluster_vcov(xc[:, None], ec, des.drug, bc_, n, des.p_all - 1)
    Vcl, _ = cluster_vcov(xc[:, None], ec, des.l, bc_, n, des.p_all - 1)
    Vci, _ = cluster_vcov(xc[:, None], ec, des.drug.astype(np.int64) * 1000 + des.l, bc_, n, des.p_all - 1)
    v2c = Vc[0, 0] + Vcl[0, 0] - Vci[0, 0]
    sec = float(np.sqrt(Vc[0, 0]))
    sec2 = float(np.sqrt(v2c)) if v2c > 0 else float(np.sqrt(max(Vc[0, 0], Vcl[0, 0])))
    out.update({"b_common": bc, "se_common_drug": sec, "ci_common_lo": bc - td * sec, "ci_common_hi": bc + td * sec,
                "p_common_drug": tp(bc, sec, Gd - 1), "se_common_twoway": sec2,
                "ci_common_lo_twoway": bc - tl * sec2, "ci_common_hi_twoway": bc + tl * sec2,
                "p_common_twoway": tp(bc, sec2, min(Gd, Gl) - 1)})
    # permutation nulls
    if B_within:
        nul = within_dd_perm(des, ytil, B_within, rng)
        dn = nul[:, 0] - nul[:, 1]
        out.update({"p_WT_perm_within_dd": perm_p(b[0], nul[:, 0]), "p_alt_perm_within_dd": perm_p(b[1], nul[:, 1]),
                    "p_diff_perm_within_dd": perm_p(dif, dn), "sd_diff_perm_within_dd": float(np.nanstd(dn)),
                    "p_common_perm_within_dd": perm_p(bc, nul[:, 2]),
                    "sd_WT_perm_within_dd": float(np.nanstd(nul[:, 0])),
                    "sd_common_perm_within_dd": float(np.nanstd(nul[:, 2])), "n_perm_within_dd": B_within})
    if B_label:
        obs, tobs, nl, ntt = label_perm(des, MY, B_label, rng)
        sd = float(np.nanstd(nl))
        out.update({"t_diff_line": dif / se_l, "p_diff_tp53_label_perm": perm_p(tobs, ntt),
                    "p_diff_tp53_label_perm_unstudentised": perm_p(dif, nl), "sd_diff_tp53_label_perm": sd,
                    "ci_diff_lo_labelsd": dif - 1.96 * sd, "ci_diff_hi_labelsd": dif + 1.96 * sd,
                    "n_perm_tp53_label": B_label, "check_label_engine_minus_main": float(obs - dif),
                    "check_label_engine_t_minus_main": float(tobs - dif / se_l)})
        out["mde_diff_80"] = Z80 * sd
        out["mde_diff_80_line_se"] = Z80 * se_l
    if B_within:
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


def build_tables(E, grid, pbe, Bkeep):
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
    return out, wells


# ============================================================================= analyses
def run_models(rows_spec, tabs, grid, wt_line, rng, args, want_lines_for=()):
    """rows_spec: list of dicts with keys readout, variant, covset, xname, X, Y, ddmask."""
    res, slopes = [], []
    cache = {}
    for spec in rows_spec:
        tb = tabs[spec["tabs"]]
        X, Y = spec["X"], tb[spec["readout"]]
        covs = [tb[c] for c in COVSETS[spec["covset"]]]
        ok = np.isfinite(X) & np.isfinite(Y) & spec["ddmask"][:, None]
        for c in covs:
            ok &= np.isfinite(c)
        key = (spec["tabs"], spec["xname"], spec["covset"], ok.tobytes())
        if key not in cache:
            cache.clear()                            # one design kept at a time (memory)
            cache[key] = Design(ok, X, covs, wt_line, grid.drug_id)
        des = cache[key]
        y = Y[des.d, des.l].astype(float)
        want = (spec["variant"], spec["covset"], spec["readout"]) in want_lines_for or \
            (spec["variant"], spec["covset"]) in want_lines_for
        t0 = time.time()
        o, ls = fit(des, y, spec["B_within"], spec["B_label"], rng, want)
        res.append({k: spec[k] for k in ("family", "module", "readout", "variant", "covset", "xname")} | o)
        if ls is not None:
            b, se, nr, Gd = ls
            lu = des.fe.lu
            for i, l_ in enumerate(lu):
                slopes.append({"readout": spec["readout"], "variant": spec["variant"], "covset": spec["covset"],
                               "cell_line_id": grid.L[l_], "cell_line": grid.lines.loc[l_, "cell_name"],
                               "tp53_group": "WT" if wt_line[l_] else "altered", "n_rows": int(nr[i]),
                               "slope": b[i], "se_drug": se[i],
                               "ci_lo": b[i] - stats.t.ppf(0.975, Gd - 1) * se[i],
                               "ci_hi": b[i] + stats.t.ppf(0.975, Gd - 1) * se[i],
                               "p_drug": tp(b[i], se[i], Gd - 1)})
        log(f"  {spec['family']} {spec['readout']} [{spec['variant']}, {spec['covset']}]: n {o['n_rows']}, "
            f"b_WT {o['b_WT']:+.3f}, b_alt {o['b_alt']:+.3f}, diff {o['diff']:+.3f} "
            f"(p label {o.get('p_diff_tp53_label_perm', np.nan):.3g}) ({time.time() - t0:.0f} s)")
    return pd.DataFrame(res), pd.DataFrame(slopes)


def slope_tests(slopes, n_perm, rng, min_rows=20):
    rows = []
    for (ro, va, cs), g in slopes.groupby(["readout", "variant", "covset"], sort=False):
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
        rows.append({"readout": ro, "variant": va, "covset": cs, "n_lines_WT": len(a), "n_lines_alt": len(b),
                     "mean_slope_WT": a.mean(), "mean_slope_alt": b.mean(), "median_slope_WT": np.median(a),
                     "median_slope_alt": np.median(b), "n_WT_negative": int((a < 0).sum()),
                     "n_alt_negative": int((b < 0).sum()), "diff_mean_WT_minus_alt": obs, "se_welch": se,
                     "ci_lo_welch": obs - stats.t.ppf(0.975, dfw) * se, "ci_hi_welch": obs + stats.t.ppf(0.975, dfw) * se,
                     "p_welch": float(t.pvalue), "p_tp53_label_perm": perm_p(obs / se, tnull),
                     "p_tp53_label_perm_unstudentised": perm_p(obs, null),
                     "sd_label_perm": float(null.std()), "mde_diff_80": Z80 * float(null.std()),
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


def reliability(XA, XB, ok_base, covs, wt_line, grid, extra=()):
    """Correlation of the residual (FE + covariates x group) TRIM72 from half A and half B (or well 1 / well 2) over
    common cells; Spearman-Brown for the full measure."""
    ok = ok_base & np.isfinite(XA) & np.isfinite(XB)
    for c in list(covs) + list(extra):
        ok &= np.isfinite(c)
    des = Design(ok, XA, list(covs) + list(extra), wt_line, grid.drug_id)
    ra = des.resid(XA[des.d, des.l].astype(float))
    rb = des.resid(XB[des.d, des.l].astype(float))
    out = []
    for gname, m in (("all lines", np.ones(des.n, bool)), ("TP53-WT", des.wt), ("TP53-altered", ~des.wt)):
        r = float(np.corrcoef(ra[m], rb[m])[0, 1])
        out.append({"tp53_group": gname, "n_rows": int(m.sum()), "n_drugdoses": len(np.unique(des.d[m])),
                    "r_halves": r, "reliability_full_spearman_brown": 2 * r / (1 + r) if r > -1 else np.nan,
                    "sd_resid_A": float(ra[m].std()), "sd_resid_B": float(rb[m].std())})
    return out


def breakdown(tb, grid, wt_line, ddmask, variant, covset="full", lodo=False):
    """Which drug-doses carry b_WT - b_alt: per drug-dose contributions from the FWL-partialled vectors of the full
    model (contrib_* = sum over the drug-dose's rows of x~ y~ / sum over all rows of x~^2; they add up to b_WT / b_alt
    up to the small WT-altered cross term), and (lodo) the model refitted without each drug (all its doses)."""
    covs = [tb[c] for c in COVSETS[covset]]
    X = tb[GENE]
    pdd, lo = [], []
    for ro in D1:
        Y = tb[ro]
        ok = np.isfinite(X) & np.isfinite(Y) & ddmask[:, None]
        for c in covs:
            ok &= np.isfinite(c)
        des = Design(ok, X, covs, wt_line, grid.drug_id)
        y = Y[des.d, des.l].astype(float)
        ytil = des.resid(y)
        x1, x2 = des.xt[:, 0], des.xt[:, 1]
        s1, s2 = (x1 * x1).sum(), (x2 * x2).sum()
        full, _ = fit(des, y, 0, 0, None)
        g = pd.DataFrame({"d": des.d, "wt": des.wt, "a1": x1 * ytil, "q1": x1 * x1, "a2": x2 * ytil, "q2": x2 * x2})
        agg = g.groupby("d").agg(n_WT=("wt", "sum"), n=("wt", "size"), a1=("a1", "sum"), q1=("q1", "sum"),
                                 a2=("a2", "sum"), q2=("q2", "sum"))
        for d_, r in agg.iterrows():
            pdd.append({"readout": ro, "variant": variant, "covset": covset, "drugdose_row": d_,
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
                d2 = Design(ok2, X, covs, wt_line, grid.drug_id)
                o, _ = fit(d2, Y[d2.d, d2.l].astype(float), 0, 0, None)
                lo.append({"readout": ro, "variant": variant, "covset": covset,
                           "dropped_drug": grid.dd["drug"].to_numpy()[np.flatnonzero(grid.drug_id == dr)[0]],
                           "n_rows": o["n_rows"], "n_drugdoses": o["n_drugdoses"], "b_WT": o["b_WT"],
                           "b_alt": o["b_alt"], "diff": o["diff"], "p_diff_line": o["p_diff_line"],
                           "p_diff_twoway": o["p_diff_twoway"], "diff_all_drugs": full["diff"],
                           "p_diff_line_all_drugs": full["p_diff_line"]})
    return pd.DataFrame(pdd), pd.DataFrame(lo)


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

Unit: one drug-dose x cell line cell. Values are method-v3 corrected log2 effects r2 (plate x line baseline ->
composition shift -> two-pass position correction) per (well, line), averaged over the drug-dose's used wells
(profiles with >= 30 cells): panel genes from the panel's T.expression_effects (downstream_p53's cache builder), other
genes from upstream_coregulation.corrected_effects() on atlas/pseudobulk. P53_SCORE = mean r2 of the 21 P53_ACTIVITY
members the line expresses. TP53 groups: the panel's (17 WT, 33 altered).
Model per read-out Y: Y = drug-dose FE + line FE + b_WT TRIM72 x WT + b_alt TRIM72 x altered + covariates x TP53
group. Covariate sets: full = DD_beta (0 where the drug-dose has no consensus response, < 20 significant genes),
DD_A (relative abundance), S and G2M per-line effects (DD_r2_modules), bg_abs_r2 (mean |r2| over the panel genes
that are not p53-related, not screen genes, not TRIM72); no_cycle = full without S and G2M (for cell-cycle read-outs,
which overlap those modules); none = fixed effects only. Units: b = log2 change in the read-out per log2 change in
TRIM72 (both corrected effects); *_per_sd_TRIM72 = per SD of the residual TRIM72 (FE and covariates out).
full_base = full + trim72_base_x_dd (the line's untreated TRIM72 level, log2 DMSO CPM z-scored over lines, x the
drug-dose's TRIM72 log2FC from the atlas: low-baseline lines get larger TRIM72 folds under a raiser).
NCI-H2122 and NCI-H596 have no DD_A (too few cells for the atlas growth analysis) and drop out of models with
covariates.
Primary estimand diff = b_WT - b_alt (negative = more TRIM72 with less p53 output only where p53 works); primary
p = p_diff_tp53_label_perm: TP53 labels permuted over lines (group sizes kept, the whole model refitted), statistic
t = diff / line-cluster SE (studentised, so a WT group with a larger spread than the altered group does not inflate
it); p_diff_tp53_label_perm_unstudentised permutes diff itself.

d1_two_way_models.csv     one row per read-out (P53_SCORE, MDM2, CDKN1A, FDXR, ZMAT3, DDB2, TP53I3, BBC3, TP53) x
                          variant x covariate set (full, none, full_base). Variants: i_all (all drug-doses),
                          ii_active (TRIM72 |z| >= 3 or
                          P53_ACTIVITY z >= 3; drugdose_sets.csv), ii_active_no_plate3_13 (the same without the
                          plate-3 / plate-13 wells), iii_readthrough (X = TRIM72_rt), iv_no_plate3_13 (wells of
                          plates 3 and 13 left out, drug-dose means and covariates recomputed).
                          Columns: n_rows / n_drugdoses / n_drugs / n_lines_WT / n_lines_alt; b_WT, b_alt with drug-
                          cluster SE (CR1), 95% CI (t, G-1 df), p_*_drug, two-way (drug, line) cluster SE/p, within-
                          drug-dose permutation p (TRIM72 shuffled across lines within each drug-dose); diff with
                          drug-cluster, line-cluster and two-way SE/CI/p, p_diff_perm_within_dd and its null SD,
                          t_diff_line, p_diff_tp53_label_perm (studentised; primary), the unstudentised version and
                          the null SD of diff (ci_diff_*_labelsd = diff +- 1.96 SD), mde_diff_80 = 2.80 x label-
                          permutation SD (smallest |b_WT - b_alt| detectable with 80% power, two-sided 5%),
                          mde_diff_80_line_se = 2.80 x line-cluster SE, mde_diff_80_within_dd from the within-drug-
                          dose null; b_common (one
                          slope for all lines); sd_TRIM72_resid_*, sd_Y_resid; attenuation_lambda_split_half (the
                          split-half reliability of the residual TRIM72 for that variant's cells, trim72_reliability.csv)
                          and mde_diff_80_attenuation_corrected = mde_diff_80 / lambda; q_bh_diff_label = BH over the
                          read-outs within variant x covariate set; check_label_engine_minus_main and
                          check_label_engine_t_minus_main (the permutation engine at the observed labels minus the
                          main fit: should be ~0).
d1_line_slopes.csv        variant i_all (full covariates) and ii_active: per line, the TRIM72 slope from one model with
                          line-specific TRIM72 AND covariate slopes (both FE), drug-cluster SE.
d1_line_slope_tests.csv   per read-out: mean line slope WT minus altered (lines with >= 20 cells of data), Welch t,
                          TP53-label permutation p of the Welch t (and of the plain difference), MDE from the
                          permutation SD of the difference; counts of negative slopes.
d1_per_drugdose_contributions.csv  i_all and ii_active (full covariates): per drug-dose and read-out, its rows' share
                          of the WT / altered TRIM72 variation (weight_share_*), its own slope on the partialled data
                          (slope_*_in_drugdose) and its contribution to b_WT, b_alt and diff (contrib_*: sum over its
                          rows of x~ y~ / total sum of x~^2; they add up to b_WT / b_alt up to the WT-altered cross term).
d1_active_leave_one_drug_out.csv  ii_active (full): the model refitted without each drug (all its doses): b_WT, b_alt,
                          diff, line-cluster and two-way p, next to the all-drug diff.
d2_screen_models.csv      the same model (variant i_all) for each MG53-linked gene and module (module = mean r2 of
                          the members a line expresses) of mg53_perturbation/assay_panel/panel.csv: NF-kB (NFKBIA,
                          TNFAIP3, CXCL8 + module), ferroptosis (SLC7A11, GPX4, CHAC1), apoptosis (BAX, MCL1, PMAIP1),
                          stress (ATF3, DDIT3 + module), PI3K-AKT/FOXO/FAK (TXNIP, IRS1, PTK2), cell cycle (CCND1,
                          KIF11), E2F targets (E2F1, CCNE1, CDT1, MCM3, MCM7, MYBL2, CDC25A + module; none in the
                          S_PHASE module), RAC1. primary = the covariate set used for the BH family (no_cycle for the
                          cell-cycle and E2F read-outs, full otherwise); q_bh_* over the primary rows: diff
                          (studentised TP53-label permutation p), b_common, b_WT and b_alt (two-way (drug, line)
                          cluster p; the within-drug-dose permutation p, also given, tests 'no association in any
                          drug-dose' and rejects whenever slopes vary across drugs, even with a zero mean). Non-primary rows
                          (full covariates for the cell-cycle read-outs) are sensitivity rows (no q).
                          source = panel (T.expression_effects) or pseudobulk (corrected_effects).
readthrough_correction_fit.csv  TRIM72 r2 on FUS r2 and PYCARD-AS1 r2 within drug-dose and line (all drug-doses):
                          slopes, drug-cluster SE, within-R2 (share of TRIM72's within variation explained);
                          PYCARD-AS1 r2 is kept in every line (it is below the atlas gene list).
trim72_reliability.csv    (v) measurement error of TRIM72: split-half (each well x line's cells split at random into
                          two halves, the panel's method run on each half, halves averaged per drug-dose like the
                          main data) and replicate wells (drug-doses with 2+ used wells on different plates: first
                          two wells; split-half is also given for those drug-doses alone, for comparison: the gap
                          between the two is plate-specific line variation). r_halves = correlation of the residual
                          TRIM72 (FE + covariates x group out, and
                          FUS / PYCARD-AS1 for the readthrough row) between the halves / wells;
                          reliability_full_spearman_brown = 2r/(1+r) (the full-data measure from two halves);
                          attenuation: observed b ~= lambda x true b for classical, independent measurement error.
drugdose_sets.csv         per drug-dose: TRIM72 z, P53_ACTIVITY z (panel), plates, whether in ii_active and in
                          iv_no_plate3_13.
analysis_cells.csv.gz     the per (drug-dose, line) values of the main data (all used wells): TRIM72 r2, TRIM72_rt,
                          D1 read-outs, screen read-outs, covariates, TRIM72 halves A and B.
checks.csv                pseudobulk vs gene_panel counts; corrected_effects vs the panel r2 and the atlas DD_lfc;
                          idarubicin per-line TRIM72 vs trim72_idarubicin/corrected; split-half bookkeeping.
key_results.csv           the headline numbers (D1 primary rows, line-slope tests, screen hits at q < 0.1,
                          reliability).
"""


# ============================================================================= main
def main():
    global DP_PANEL, BACKGROUND
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--data", default=os.environ.get("MG53_DATA") or os.environ.get("TAHOE_DATA")
                    or os.path.expanduser("~/Tahoe-100M"))
    ap.add_argument("--recompute", action="store_true", help="rebuild the caches")
    ap.add_argument("--perm", type=int, default=1000, help="within-drug-dose permutations per D1 model")
    ap.add_argument("--label-perm", type=int, default=2000, help="TP53-label permutations per model")
    ap.add_argument("--screen-perm", type=int, default=500, help="within-drug-dose permutations per D2 model")
    ap.add_argument("--quick", action="store_true", help="few permutations (a test run)")
    a = ap.parse_args()
    if a.quick:
        a.perm, a.label_perm, a.screen_perm = 100, 200, 50
    t0 = time.time()
    out = os.environ.get("MG53_OUT") or HERE
    cdir, tab = os.path.join(out, "cache"), os.path.join(out, "tables")
    os.makedirs(cdir, exist_ok=True)
    os.makedirs(tab, exist_ok=True)
    if a.recompute:
        for f in glob.glob(os.path.join(cdir, "*.np[yz]")) + glob.glob(os.path.join(cdir, "*.parquet")):
            os.remove(f)
        import shutil
        shutil.rmtree(os.path.join(cdir, "panel"), ignore_errors=True)
    rng = np.random.default_rng(SEED)
    log(f"data {a.data}; out {out}")
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
    active = ((dsets["TRIM72_z"].abs() >= 3) | (dsets["P53_ACTIVITY_z"] >= 3)).to_numpy()
    keep_w = ~np.isin(grid.plate, DROP_PLATES)
    B_iv = grid.agg(keep_w)
    kept_iv = np.asarray(B_iv.sum(axis=1)).ravel() > 0
    dsets["in_ii_active"] = active
    dsets["in_iv_no_plate3_13"] = kept_iv
    dsets.drop(columns="conc_key").to_csv(os.path.join(tab, "drugdose_sets.csv"), index=False)
    alldd = np.ones(grid.nd, bool)

    # per (drug-dose, line) data
    tabs = {}
    tabs["main"], wells_main = build_tables(E, grid, pbe, grid.B)
    tabs["iv"], _ = build_tables(E, grid, pbe, B_iv)
    rt, rtfit = readthrough_fit(tabs["main"], grid, alldd)
    tabs["main"]["TRIM72_rt"] = rt
    rtfit.to_csv(os.path.join(tab, "readthrough_correction_fit.csv"), index=False)
    halves = {"main": (Grid.dd_mean(grid.B, hA.astype(float)), Grid.dd_mean(grid.B, hB.astype(float))),
              "iv": (Grid.dd_mean(B_iv, hA.astype(float)), Grid.dd_mean(B_iv, hB.astype(float)))}
    log(f"per (drug-dose, line) data ready: {int(np.isfinite(tabs['main'][GENE]).sum())} cells with TRIM72; "
        f"active drug-doses {int(active.sum())}; drug-doses without plates 3/13 {int(kept_iv.sum())}")

    # (v) reliability of TRIM72 (split-half and replicate wells)
    rel_rows = []
    for vname, tk, ddm, extra in (("i_all", "main", alldd, ()), ("ii_active", "main", active, ()),
                                   ("ii_active_no_plate3_13", "iv", active & kept_iv, ()),
                                   ("iii_readthrough", "main", alldd, ("FUS", "PYCARD-AS1")),
                                   ("iv_no_plate3_13", "iv", kept_iv, ())):
        XA, XB = halves[tk]
        for cs in ("full", "none"):
            covs = [tabs[tk][c] for c in COVSETS[cs]]
            ex = [tabs[tk][e] for e in extra]
            for r in reliability(XA, XB, ddm[:, None] & np.isfinite(tabs[tk][GENE]), covs, wt_line, grid, ex):
                rel_rows.append({"method": "split-half (cells within each well x line)", "variant": vname,
                                 "residualised_on": "FE + " + (cs if cs != "none" else "nothing else") +
                                 (" + FUS, PYCARD-AS1" if extra else "")} | r)
    # replicate wells: first two used wells of drug-doses with 2+ used wells on different plates
    w = grid.w
    wsel = w[grid.used].copy()
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
    for r in reliability(XA, XB, rep_dd[:, None] & np.isfinite(tabs["main"][GENE]),
                         [tabs["main"][c] for c in COVSETS["full"]], wt_line, grid):
        rel_rows.append({"method": "split-half (cells within each well x line)",
                         "variant": f"the {n_rep} replicated drug-doses only (compare with the replicate-well rows)",
                         "residualised_on": "FE + full"} | r)
    for cs in ("full", "none"):
        covs = [tabs["main"][c] for c in COVSETS[cs]]
        for r in reliability(W1, W2, np.isfinite(tabs["main"][GENE]), covs, wt_line, grid):
            rr = dict(r)
            rr["reliability_single_well"] = rr.pop("r_halves")
            rr["reliability_full_spearman_brown"] = np.nan
            rel_rows.append({"method": "replicate wells (two plates)", "variant": f"{n_rep} drug-doses with 2+ wells",
                             "residualised_on": "FE + " + (cs if cs != "none" else "nothing else")} | rr)
    REL = pd.DataFrame(rel_rows)
    REL.to_csv(os.path.join(tab, "trim72_reliability.csv"), index=False)
    log("(v) reliability: " + "; ".join(f"{r['variant']} {r['residualised_on']}: r {r['r_halves']:.3f}"
                                        for _, r in REL[(REL["tp53_group"] == "all lines")
                                                        & REL["method"].str.startswith("split")].iterrows()))

    # D1
    specs = []
    for ro in D1:
        base = {"family": "D1 p53", "module": "p53", "readout": ro, "B_within": a.perm, "B_label": a.label_perm}
        specs += [base | {"variant": "i_all", "covset": "full", "xname": "TRIM72_r2", "tabs": "main",
                          "X": tabs["main"][GENE], "ddmask": alldd},
                  base | {"variant": "i_all", "covset": "none", "xname": "TRIM72_r2", "tabs": "main",
                          "X": tabs["main"][GENE], "ddmask": alldd},
                  base | {"variant": "i_all", "covset": "full_base", "xname": "TRIM72_r2", "tabs": "main",
                          "X": tabs["main"][GENE], "ddmask": alldd},
                  base | {"variant": "ii_active", "covset": "full", "xname": "TRIM72_r2", "tabs": "main",
                          "X": tabs["main"][GENE], "ddmask": active},
                  base | {"variant": "ii_active", "covset": "full_base", "xname": "TRIM72_r2", "tabs": "main",
                          "X": tabs["main"][GENE], "ddmask": active},
                  base | {"variant": "ii_active_no_plate3_13", "covset": "full", "xname": "TRIM72_r2", "tabs": "iv",
                          "X": tabs["iv"][GENE], "ddmask": active & kept_iv},
                  base | {"variant": "iii_readthrough", "covset": "full", "xname": "TRIM72_rt (FUS, PYCARD-AS1 out)",
                          "tabs": "main", "X": tabs["main"]["TRIM72_rt"], "ddmask": alldd},
                  base | {"variant": "iv_no_plate3_13", "covset": "full", "xname": "TRIM72_r2", "tabs": "iv",
                          "X": tabs["iv"][GENE], "ddmask": kept_iv}]
    specs.sort(key=lambda s: (s["variant"], s["covset"]))       # rows sharing a design run together
    log("D1: p53 read-outs")
    D1T, SL = run_models(specs, tabs, grid, wt_line, rng, a,
                         want_lines_for={("i_all", "full"), ("ii_active", "full")})
    lam = REL[(REL["method"].str.startswith("split")) & (REL["tp53_group"] == "all lines")
              & REL["residualised_on"].str.contains("full")].set_index("variant")["reliability_full_spearman_brown"]
    D1T["attenuation_lambda_split_half"] = D1T["variant"].map(lam)
    D1T["mde_diff_80_attenuation_corrected"] = D1T["mde_diff_80"] / D1T["attenuation_lambda_split_half"]
    D1T["q_bh_diff_label"] = np.nan
    for _k, g in D1T.groupby(["variant", "covset"]):
        D1T.loc[g.index, "q_bh_diff_label"] = bh(g["p_diff_tp53_label_perm"].to_numpy())
    order = {v: i for i, v in enumerate(D1)}
    D1T = D1T.sort_values(["variant", "covset", "readout"], key=lambda s: s.map(order) if s.name == "readout" else s)
    D1T.to_csv(os.path.join(tab, "d1_two_way_models.csv"), index=False, float_format="%.6g")
    SL.to_csv(os.path.join(tab, "d1_line_slopes.csv"), index=False, float_format="%.6g")
    ST = slope_tests(SL, 20000, rng)
    ST.to_csv(os.path.join(tab, "d1_line_slope_tests.csv"), index=False, float_format="%.6g")
    log("D1: per drug-dose contributions (i_all, ii_active) and leave-one-drug-out (ii_active)")
    pa, _ = breakdown(tabs["main"], grid, wt_line, alldd, "i_all")
    pb_, lo = breakdown(tabs["main"], grid, wt_line, active, "ii_active", lodo=True)
    pd.concat([pa, pb_]).to_csv(os.path.join(tab, "d1_per_drugdose_contributions.csv"), index=False,
                                float_format="%.6g")
    lo.to_csv(os.path.join(tab, "d1_active_leave_one_drug_out.csv"), index=False, float_format="%.6g")

    # D2 screen
    log("D2: screen of MG53-linked pathways")
    specs = []
    for name, pm, genes, as_module, cs in SCREEN:
        ros = genes + ([f"{name} module"] if as_module else [])
        for ro in ros:
            covsets = [cs] + (["full"] if cs != "full" else [])
            for c_ in covsets:
                specs.append({"family": "D2 screen", "module": name, "readout": ro, "variant": "i_all",
                              "covset": c_, "xname": "TRIM72_r2", "tabs": "main", "X": tabs["main"][GENE],
                              "ddmask": alldd, "B_within": a.screen_perm, "B_label": a.label_perm,
                              "primary": c_ == cs, "panel_module": pm})
    D2T, _ = run_models(specs, tabs, grid, wt_line, rng, a)
    D2T["primary"] = [s["primary"] for s in specs]
    D2T["panel_module"] = [s["panel_module"] for s in specs]
    D2T["source"] = ["panel" if r in DP_PANEL else ("module" if r.endswith("module") else "pseudobulk")
                     for r in D2T["readout"]]
    pr = D2T["primary"].to_numpy()
    for col, pc in (("q_bh_diff_label", "p_diff_tp53_label_perm"), ("q_bh_common", "p_common_twoway"),
                    ("q_bh_WT", "p_WT_twoway"), ("q_bh_alt", "p_alt_twoway")):
        D2T[col] = np.nan
        D2T.loc[pr, col] = bh(D2T.loc[pr, pc].to_numpy())
    D2T.to_csv(os.path.join(tab, "d2_screen_models.csv"), index=False, float_format="%.6g")

    # per-cell data table
    m = tabs["main"]
    d_, l_ = np.nonzero(np.isfinite(m[GENE]))
    cols = {"drugdose_row": d_, "drug": grid.dd["drug"].to_numpy()[d_], "conc": grid.dd["conc"].to_numpy()[d_],
            "cell_line_id": np.array(grid.L)[l_], "cell_line": grid.lines["cell_name"].to_numpy()[l_],
            "tp53_group": np.where(wt_line[l_], "WT", "altered"), "in_ii_active": active[d_],
            "TRIM72_r2": m[GENE][d_, l_], "TRIM72_rt": m["TRIM72_rt"][d_, l_],
            "TRIM72_r2_halfA": halves["main"][0][d_, l_], "TRIM72_r2_halfB": halves["main"][1][d_, l_],
            "FUS_r2": m["FUS"][d_, l_], "PYCARD-AS1_r2": m["PYCARD-AS1"][d_, l_]}
    for k in D1 + [s for s in SCREEN_GENES if s not in D1] + [f"{s[0]} module" for s in SCREEN if s[3]] + \
            COVSETS["full"]:
        cols[k] = m[k][d_, l_]
    pd.DataFrame(cols).to_csv(os.path.join(tab, "analysis_cells.csv.gz"), index=False, float_format="%.4g")

    CK = checks(E, grid, pbe, pbc, tabs, a.data, sh_check)
    CK.to_csv(os.path.join(tab, "checks.csv"), index=False)
    # key results
    kr = []
    for _, r in D1T[D1T["readout"].isin(["P53_SCORE", "MDM2", "CDKN1A"])].iterrows():
        pw_ = r.get("p_WT_perm_within_dd", np.nan)
        kr.append({"section": "D1", "what": f"{r['readout']} [{r['variant']}, {r['covset']}]: b_WT - b_alt",
                   "n": r["n_rows"], "estimate": r["diff"], "ci_lo": r["ci_diff_lo_twoway"],
                   "ci_hi": r["ci_diff_hi_twoway"], "p": r["p_diff_tp53_label_perm"], "q": r["q_bh_diff_label"],
                   "mde_80": r["mde_diff_80"], "detail": f"b_WT {r['b_WT']:.4f} (p perm {pw_:.3g}); b_alt "
                                                         f"{r['b_alt']:.4f}; CI two-way cluster; p TP53-label perm"})
    for _, r in ST.iterrows():
        if r["readout"] in ("P53_SCORE", "MDM2", "CDKN1A"):
            kr.append({"section": "D1 line slopes", "what": f"{r['readout']} [{r['variant']}]: mean line slope WT - "
                       "altered", "n": r["n_lines_WT"] + r["n_lines_alt"], "estimate": r["diff_mean_WT_minus_alt"],
                       "ci_lo": r["ci_lo_welch"], "ci_hi": r["ci_hi_welch"], "p": r["p_tp53_label_perm"],
                       "mde_80": r["mde_diff_80"]})
    for _, r in D2T[D2T["primary"]].iterrows():
        if min(r["q_bh_diff_label"], r["q_bh_common"]) < 0.1:
            kr.append({"section": "D2", "what": f"{r['readout']} ({r['module']}): b_common / diff", "n": r["n_rows"],
                       "estimate": r["b_common"], "ci_lo": r["ci_common_lo_twoway"],
                       "ci_hi": r["ci_common_hi_twoway"], "p": r["p_common_twoway"], "q": r["q_bh_common"],
                       "detail": f"diff {r['diff']:.4f}, q_diff {r['q_bh_diff_label']:.3g}; b_WT {r['b_WT']:.4f} "
                                 f"b_alt {r['b_alt']:.4f}"})
    for ro, g in lo.groupby("readout", sort=False):
        kr.append({"section": "D1 ii_active leave-one-drug-out", "what": f"{ro}: b_WT - b_alt without each drug",
                   "n": len(g), "estimate": g["diff_all_drugs"].iloc[0], "ci_lo": g["diff"].min(),
                   "ci_hi": g["diff"].max(), "p": g["p_diff_line"].max(),
                   "detail": "ci_lo / ci_hi = smallest / largest diff over the drops; p = largest line-cluster p over "
                             f"the drops (drop giving it: {g.loc[g['p_diff_line'].idxmax(), 'dropped_drug']})"})
    for _, r in REL[REL["tp53_group"] == "all lines"].iterrows():
        kr.append({"section": "(v) reliability", "what": f"{r['method']} [{r['variant']}; {r['residualised_on']}]",
                   "n": r["n_rows"], "estimate": r.get("r_halves") if pd.notna(r.get("r_halves")) else
                   r.get("reliability_single_well"), "detail": f"full-data reliability "
                   f"{r['reliability_full_spearman_brown']:.3f}" if pd.notna(r["reliability_full_spearman_brown"])
                   else "single-well reliability"})
    for _, r in rtfit.iterrows():
        kr.append({"section": "(iii) readthrough fit", "what": f"TRIM72 r2 on {r['predictor']} (within FE)",
                   "n": r["n_rows"], "estimate": r["slope"], "p": r["p_drug"],
                   "detail": f"within R2 of TRIM72 explained by FUS + PYCARD-AS1 {r['within_R2_of_TRIM72']:.3f}"})
    pd.DataFrame(kr).to_csv(os.path.join(tab, "key_results.csv"), index=False, float_format="%.6g")
    with open(os.path.join(tab, "README_tables.txt"), "w", encoding="utf-8") as fh:
        fh.write(README)
    print(CK.to_string(index=False))
    log(f"tables written to {tab}; peak RSS {peak_gb():.2f} GB; wall {time.time() - t0:.0f} s")


DP_PANEL, BACKGROUND = set(), []

if __name__ == "__main__":
    main()
