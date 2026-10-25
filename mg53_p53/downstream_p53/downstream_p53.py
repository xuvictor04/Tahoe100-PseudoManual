#!/usr/bin/env python3
"""Downstream: does TRIM72 (MG53) associate with p53 activity?  Tahoe-100M, method-v3 corrected effects.

MG53 is an E3 ubiquitin ligase. If it destabilised p53 (or MDM2), cells or lines with more TRIM72 would show lower (or
higher) p53-target transcription at a given stimulus. Tahoe has NO MG53 perturbation and measures mRNA only, so every
test below is an ASSOCIATION between TRIM72 mRNA and p53-target mRNA; none of it is causal for MG53 -> p53, and p53
PROTEIN is never measured (p53 activity is read from its target genes).

Four angles, each designed to remove the confounders the data allow:
 (a) Across cell lines inside the same wells (strong TRIM72 raisers and the panel's p53 reference activators):
     per-line TRIM72 induction (r2) or treated TRIM72 level vs per-line p53-target induction (the panel's 21-gene
     P53_ACTIVITY score, CDKN1A, MDM2, BBC3, PMAIP1, TP53), separately in TP53-WT (17) and TP53-altered (33) lines;
     raw and partial Spearman (general responsiveness to the drug-dose = atlas DD_beta, or the line's mean |r2| over
     non-p53 panel genes, plus cell loss = atlas DD_A partialled out), permutation p, BH FDR; replicate-well
     reliability and cross-well correlations (TRIM72 from one plate's well, p53 from the other: shared per-profile
     noise cannot create them); TRIM72's correlation with every non-p53 panel gene as an empirical reference; a pooled
     test over drug-doses with a line-label permutation, and its WT-minus-altered difference (TP53-label permutation).
 (b) Baseline: DMSO wells only, TRIM72 level as observed / expected counts with the expected count from the plate's
     median line (indirect standardisation within each plate: removes the TRIM72 plate batch)
     vs basal p53 activity (within-plate and the panel's basal_p53_activity_log2) and p53 responsiveness
     (p53_functional_status.csv), by TP53 status; per plate and over plates; high- vs low-baseline plates.
 (c) Across all 1,132 drug-doses: TRIM72 z vs P53_ACTIVITY z, MDM2 z, CDKN1A z and the WT-minus-altered p53 contrast
     (raw and with drug activity partialled out; drug-level block bootstrap); drug-doses that raise TRIM72 without p53
     activation and vice versa, with their p53 targets.
 (d) Single cells: idarubicin 5 uM wells (plates 6 and 14) and the DMSO wells of the same plates; per line, quasi-
     Poisson GLM of each p53 target's counts on TRIM72-detected (>= 1 UMI) with a log(total UMI) offset and
     log(total UMI), S- and G2M-phase scores as covariates; random-effects meta-analysis over lines, WT and altered
     separately; non-p53 panel genes as negative-control outcomes; a depth-stratified Mantel-Haenszel rate ratio.

    python3 downstream_p53.py [--data DIR (default $MG53_DATA, $TAHOE_DATA or ~/Tahoe-100M)] [--recompute] [--perm 5000]

Caches (cache/; rebuilt with --recompute or when missing): effects.npz (per well x line r2, z_line, log2 CPM y of
every panel gene, from the panel's own setup and T.expression_effects), wells.csv, lines.csv, meta.json,
cells_selected.parquet (the per-cell rows of the 6 wells used in (d)). Tables: tables/ (see README_tables.txt there).
Nothing under the data folder is written.
"""
import argparse
import contextlib
import glob
import json
import os
import sys
import tempfile
import time
import warnings

import numpy as np
import pandas as pd
from scipy import stats

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, REPO)
import tahoe_gene_panel as P          # noqa: E402
import tahoe_mtap_gankyrin as T       # noqa: E402

GENE = "TRIM72"
P53_MEMBERS = list(P.P53_ACTIVITY)                                   # the panel's 21-gene P53_ACTIVITY score
NAMED = ["CDKN1A", "MDM2", "BBC3", "PMAIP1", "TP53"]                # named p53 targets / p53 itself
OUTCOMES = ["P53_SCORE"] + NAMED
# genes kept out of the 'general responsiveness' background: TRIM72, every p53 target or p53-related gene, ATF3
NOT_BACKGROUND = set([GENE, "TP53", "PMAIP1", "GADD45A", "SESN2", "TNFRSF10B", "CCNG1", "BTG2", "TIGAR", "ATF3"]
                     + P53_MEMBERS + P.CONTEXT["P53_EXT"])
RAISER_NAMES = ["Idarubicin", "Homoharringtonine", "Auranofin", "Dinaciclib", "Epirubicin", "Doxorubicin",
                "Topotecan", "Mitoxantrone"]
IDA = "Idarubicin (hydrochloride)"
IDA_WELLS = {"plate6": "smp_2010", "plate14": "smp_2778"}
DMSO_WELLS = {"plate6": ["smp_2069", "smp_2070"], "plate14": ["smp_2837", "smp_2838"]}
HIGH_TRIM72_PLATES = ["plate1", "plate2", "plate3", "plate14"]      # TRIM72 untreated ~10x higher (known batch)
SEED = 20261022


@contextlib.contextmanager
def quiet():
    with warnings.catch_warnings(), np.errstate(invalid="ignore", divide="ignore"):
        warnings.simplefilter("ignore", RuntimeWarning)
        warnings.simplefilter("ignore", pd.errors.PerformanceWarning)
        yield


def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


def bh(p):
    p = np.asarray(p, dtype=float)
    out = np.full(len(p), np.nan)
    ok = np.isfinite(p)
    if ok.sum():
        pv = p[ok]
        o = np.argsort(pv)
        r = pv[o] * len(pv) / np.arange(1, len(pv) + 1)
        r = np.minimum.accumulate(r[::-1])[::-1]
        q = np.empty_like(r)
        q[o] = np.minimum(r, 1)
        out[ok] = q
    return out


# ============================================================================= cache 1: per (well, line) effects
def read_only_discover(data_dir, out_dir, refresh=False):
    """T.discover without the write: the panel's file index is read, never rebuilt."""
    with open(os.path.join(out_dir, "file_index.json"), encoding="utf-8") as fh:
        return json.load(fh)


def panel_setup(data):
    T.discover = read_only_discover
    args = argparse.Namespace(command="analyze", data=data, out=os.path.join(data, "gene_panel"), workers=0,
                              batch_size=20000, limit_files=0, layout=None, min_cells=T.MIN_CELLS, reindex=False,
                              genes="", mtap_null=None, tp53_wt=None, tp53_altered=None, prior="none",
                              unreliable_plates=None, atlas=None)
    S = P.Run(args)
    S.R = tempfile.mkdtemp()           # side tables of the setup steps land here (never in gene_panel/results)
    P.load(S)
    P.step_baseline(S)
    P.step_expression(S)
    P.step_prepare(S)
    S.ctx = T.well_context(S.wl, S.sm, S.cols, S.M)
    return S


def build_effects_cache(data, cdir):
    import shutil
    t0 = time.time()
    with quiet():
        S = panel_setup(data)
    _order, todo = P.effect_genes(S)
    genes = [g for g in todo if g not in P.MODULES]
    samples = S.sm["sample"].astype(str).tolist()
    lines = list(S.base.index)
    shape = (len(genes), len(samples), len(lines))
    R2, ZL, Y = (np.full(shape, np.nan, dtype=np.float32) for _ in range(3))
    keep = ["drug", "conc", "call", "fold_change", "log2FC_corrected", "z_corrected", "fdr_up", "fdr_down",
            "n_lines", "n_lines_up", "n_lines_down", "flags", "plates", "wells"]
    res_all = []
    for k, g in enumerate(genes):
        with quiet():
            res, W, d, cal = T.expression_effects(S.wl, S.sm, g, P.gene_exclusions(S, g), S.ctx, S.drugs,
                                                  method=S.M)
        for arr, col in ((R2, "r2"), (ZL, "z_line"), (Y, "y")):
            arr[k] = d.pivot(index="sample", columns="cell_line_id", values=col).reindex(index=samples,
                                                                                          columns=lines)
        res_all.append(res[[c for c in keep if c in res]].assign(gene=g))
        if k % 25 == 0:
            log(f"  {k + 1}/{len(genes)} genes ({time.time() - t0:.0f} s)")
    os.makedirs(cdir, exist_ok=True)
    np.savez_compressed(os.path.join(cdir, "effects.npz"), R2=R2, ZL=ZL, Y=Y, genes=np.array(genes),
                        samples=np.array(samples), lines=np.array(lines))
    pd.concat(res_all, ignore_index=True).to_csv(os.path.join(cdir, "drug_effects_all_genes.csv.gz"), index=False)
    W = T.wells_of(S.sm).reindex(samples)
    Wd = W.loc[~W["is_dmso"]].copy()
    Wd["dose"] = T.dose_key(Wd)
    W["used"] = T.used_wells(Wd).reindex(W.index).fillna(False).astype(bool)
    W["reference"] = T.reference_wells(W)
    W.rename_axis("sample").reset_index().to_csv(os.path.join(cdir, "wells.csv"), index=False)
    L = pd.DataFrame({"cell_name": S.name, "organ": S.base["Organ"], "tp53_status": S.base["tp53_status"],
                      "tp53_group": S.base["tp53_group"], "tp53_changes": S.base["tp53_changes"]})
    L = pd.concat([L] + [pd.DataFrame({f"expr_{g}": S.E[g].reindex(L.index) if g in S.E else False,
                                       f"cpm_dmso_{g}": S.Cd[g].reindex(L.index) if g in S.Cd else np.nan})
                         for g in genes], axis=1)
    L.index.name = "cell_line_id"
    L.to_csv(os.path.join(cdir, "lines.csv"))
    meta = {"genes": genes, "status": {g: S.status.get(g) for g in genes},
            # the panel's rule (step_scores): the P53_ACTIVITY members that are 'testable'
            "p53_score_members": [g for g in P53_MEMBERS if g in genes and S.status.get(g) == "testable"],
            "expressed_threshold_cpm_TRIM72": float(S.thr[GENE]), "unreliable_plates": list(S.unreliable),
            "plate_factor_note": S.plate_scale_note, "composition": S.comp_note, "min_cells": T.MIN_CELLS,
            "failed_wells": S.failed["sample"].astype(str).tolist(), "built_seconds": round(time.time() - t0, 1)}
    with open(os.path.join(cdir, "meta.json"), "w", encoding="utf-8") as fh:
        json.dump(meta, fh, indent=1)
    shutil.rmtree(S.R, ignore_errors=True)
    log(f"effects cache built in {time.time() - t0:.0f} s")


class Eff:
    """Read access to the effects cache."""

    def __init__(self, cdir):
        z = np.load(os.path.join(cdir, "effects.npz"), allow_pickle=False)
        self.genes = [str(x) for x in z["genes"]]
        self.samples = [str(x) for x in z["samples"]]
        self.lines = [str(x) for x in z["lines"]]
        self.R2, self.ZL, self.Y = z["R2"].astype(float), z["ZL"].astype(float), z["Y"].astype(float)
        self.gi = {g: i for i, g in enumerate(self.genes)}
        self.si = {s: i for i, s in enumerate(self.samples)}
        self.W = pd.read_csv(os.path.join(cdir, "wells.csv"), dtype={"sample": str, "plate": str}).set_index(
            "sample")
        self.L = pd.read_csv(os.path.join(cdir, "lines.csv")).set_index("cell_line_id").reindex(self.lines)
        self.meta = json.load(open(os.path.join(cdir, "meta.json"), encoding="utf-8"))
        self.members = [g for g in self.meta["p53_score_members"] if g in self.gi]
        self.background = [g for g in self.genes if g not in NOT_BACKGROUND]

    def mat(self, g, kind="R2"):
        return getattr(self, kind)[self.gi[g]]

    def p53_score(self):
        """Per (well, line): mean r2 of the P53_ACTIVITY members the line expresses (= tahoe_gene_panel.p53_matrix)."""
        with quiet():
            return np.nanmean(np.stack([self.mat(g) for g in self.members]), axis=0)

    def bg_absr2(self):
        with quiet():
            return np.nanmean(np.abs(np.stack([self.mat(g) for g in self.background])), axis=0)


# ============================================================================= cache 2: per-cell rows of 6 wells
def build_cells_cache(data, cdir):
    import pyarrow.parquet as pq
    t0 = time.time()
    want = sorted(list(IDA_WELLS.values()) + [s for v in DMSO_WELLS.values() for s in v])
    plates = set(IDA_WELLS)
    files = sorted(glob.glob(os.path.join(data, "gene_panel", "cells", "*.parquet")))
    cols = None
    parts = []
    for f in files:
        pf = pq.ParquetFile(f)
        md = pf.metadata
        hit = False
        for r in range(md.num_row_groups):
            rg = md.row_group(r)
            st = {rg.column(i).path_in_schema: rg.column(i).statistics for i in range(rg.num_columns)
                  if rg.column(i).path_in_schema in ("sample", "plate")}
            sp, ss = st.get("plate"), st.get("sample")
            if sp is None or ss is None or not sp.has_min_max or not ss.has_min_max:
                hit = True
                break
            if sp.min == sp.max and sp.min not in plates:
                continue
            if any(ss.min <= s <= ss.max for s in want):
                hit = True
                break
        if not hit:
            continue
        if cols is None:
            cols = pf.schema_arrow.names
        t = pq.read_table(f, filters=[("sample", "in", want)])
        if t.num_rows:
            df = t.to_pandas()
            num = [c for c in df.columns if c not in ("barcode", "sample", "plate", "drug", "cell_line_id")]
            df[num] = df[num].astype(np.int32)
            parts.append(df)
    cells = pd.concat(parts, ignore_index=True)
    cells.to_parquet(os.path.join(cdir, "cells_selected.parquet"), index=False)
    log(f"cells cache: {len(cells)} cells of {cells['sample'].nunique()} wells from {len(parts)} files "
        f"({time.time() - t0:.0f} s)")


# ============================================================================= statistics helpers
def ranks(v):
    return stats.rankdata(v)


def resid_on(y, Z):
    """Residuals of y on the columns of Z (with intercept); y and Z already ranked, all finite."""
    X = np.column_stack([np.ones(len(y))] + ([Z] if Z is not None and Z.size else []))
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    return y - X @ beta


def pcorr(a, b):
    a = a - a.mean()
    b = b - b.mean()
    d = np.sqrt((a * a).sum() * (b * b).sum())
    return float((a * b).sum() / d) if d > 0 else np.nan


def partial_spearman(x, y, Z=None, n_perm=0, rng=None):
    """Spearman of x and y with the covariates Z (n x k) partialled out of both ranks (rank-based partial
    correlation). Returns n, rho, p (t test, df n - 2 - k), p_perm (two-sided, residual permutation)."""
    x, y = np.asarray(x, float), np.asarray(y, float)
    ok = np.isfinite(x) & np.isfinite(y)
    k = 0
    if Z is not None:
        Z = np.asarray(Z, float).reshape(len(x), -1)
        ok &= np.isfinite(Z).all(axis=1)
        k = Z.shape[1]
    n = int(ok.sum())
    if n < k + 5:
        return n, np.nan, np.nan, np.nan
    rx, ry = ranks(x[ok]), ranks(y[ok])
    if k:
        Zr = np.column_stack([ranks(Z[ok, j]) for j in range(k)])
        rx, ry = resid_on(rx, Zr), resid_on(ry, Zr)
    r = pcorr(rx, ry)
    df = n - 2 - k
    p = float(2 * stats.t.sf(abs(r) * np.sqrt(df / max(1e-12, 1 - r * r)), df)) if np.isfinite(r) else np.nan
    pp = np.nan
    if n_perm and np.isfinite(r):
        rng = rng or np.random.default_rng(SEED)
        X = np.stack([rx[rng.permutation(n)] for _ in range(n_perm)])
        X = X - X.mean(axis=1, keepdims=True)
        yy = ry - ry.mean()
        rp = (X @ yy) / np.sqrt((X * X).sum(axis=1) * (yy * yy).sum())
        pp = float((1 + (np.abs(rp) >= abs(r) - 1e-12).sum()) / (n_perm + 1))
    return n, r, p, pp


def fisher_diff(r1, n1, r2, n2, k=0):
    """Difference of two independent (partial) correlations: z1 - z2 and its two-sided normal p."""
    if not (np.isfinite(r1) and np.isfinite(r2)) or min(n1, n2) - 3 - k <= 0:
        return np.nan, np.nan
    d = np.arctanh(np.clip(r1, -0.999999, 0.999999)) - np.arctanh(np.clip(r2, -0.999999, 0.999999))
    se = np.sqrt(1 / (n1 - 3 - k) + 1 / (n2 - 3 - k))
    return float(d), float(2 * stats.norm.sf(abs(d / se)))


def rank_residuals(x, y, gm, Z=None):
    """Ranks of x and y over the lines in gm with all values finite, covariate ranks partialled out (NaN
    elsewhere): the vectors whose Pearson correlation is the partial Spearman."""
    ok = gm & np.isfinite(x) & np.isfinite(y)
    if Z is not None:
        ok &= np.isfinite(Z).all(axis=1)
    rx, ry = np.full(len(x), np.nan), np.full(len(x), np.nan)
    if ok.sum() >= 8:
        X_, Y_ = ranks(x[ok]), ranks(y[ok])
        if Z is not None:
            Zr = np.column_stack([ranks(Z[ok, j]) for j in range(Z.shape[1])])
            X_, Y_ = resid_on(X_, Zr), resid_on(Y_, Zr)
        rx[ok], ry[ok] = X_, Y_
    return rx, ry


def fisher_z_perm(x, y, perms):
    """Fisher z of corr(x[perm], y) over the finite pairs, for every row of perms (row 0 = identity)."""
    Xp = x[perms]
    m = np.isfinite(Xp) & np.isfinite(y)[None, :]
    n = m.sum(axis=1)
    X0 = np.where(m, Xp, 0.0)
    Y0 = np.where(m, y[None, :], 0.0)
    with quiet():
        mx, my = X0.sum(1) / n, Y0.sum(1) / n
        dx, dy = np.where(m, Xp - mx[:, None], 0.0), np.where(m, y[None, :] - my[:, None], 0.0)
        r = (dx * dy).sum(1) / np.sqrt((dx * dx).sum(1) * (dy * dy).sum(1))
    r = np.where(n >= 6, r, np.nan)
    return np.arctanh(np.clip(r, -0.999999, 0.999999))


# ============================================================================= atlas covariates
class Atlas:
    def __init__(self, data):
        a = os.path.join(data, "atlas", "effects")
        self.dd = pd.read_csv(os.path.join(a, "drugdose.csv"))
        self.w = pd.read_csv(os.path.join(a, "wells.csv"), usecols=["sample"])
        self.lines = pd.read_csv(os.path.join(a, "lines.csv"))["cell_line_id"].astype(str).tolist()
        self.DD_beta = np.load(os.path.join(a, "DD_beta.npy"), mmap_mode="r")
        self.DD_A = np.load(os.path.join(a, "DD_A.npy"), mmap_mode="r")
        self.beta = np.load(os.path.join(a, "beta.npy"), mmap_mode="r")
        self.A2 = np.load(os.path.join(a, "A2.npy"), mmap_mode="r")
        self.wi = {s: i for i, s in enumerate(self.w["sample"].astype(str))}

    def dd_row(self, drug, conc):
        r = self.dd.index[(self.dd["drug"] == drug) & np.isclose(self.dd["conc"].astype(float), float(conc))]
        return int(r[0]) if len(r) else None

    def cov(self, drug, conc, lines, wells=None):
        """beta and A per line: the drug-dose's (DD_beta, DD_A) or, for a subset of its wells, the mean of the per-well
        beta / A2 of those wells."""
        if wells is None:
            r = self.dd_row(drug, conc)
            b = pd.Series(np.asarray(self.DD_beta[r], float), index=self.lines) if r is not None else None
            A = pd.Series(np.asarray(self.DD_A[r], float), index=self.lines) if r is not None else None
        else:
            ii = [self.wi[s] for s in wells if s in self.wi]
            with quiet():
                b = pd.Series(np.nanmean(np.asarray(self.beta[ii], float), axis=0), index=self.lines)
                A = pd.Series(np.nanmean(np.asarray(self.A2[ii], float), axis=0), index=self.lines)
        nan = pd.Series(np.nan, index=lines)
        return (b.reindex(lines) if b is not None else nan), (A.reindex(lines) if A is not None else nan)


# ============================================================================= (a) across lines in the same wells
def select_drugdoses(res_dir):
    """Strong TRIM72 raisers (panel call 'up' with z >= 4) and the panel's p53 reference activators."""
    t = pd.read_csv(os.path.join(res_dir, "TRIM72_drug_effects_by_dose.csv"))
    ref = pd.read_csv(os.path.join(res_dir, "p53_reference_doses.csv"))
    rais = t[(t["call"] == "up") & (t["z_corrected"] >= 4)]
    rows = {}
    for d, c in zip(rais["drug"], rais["conc"]):
        rows[(d, float(c))] = "TRIM72 raiser"
    for d, c in zip(ref["drug"], ref["conc"]):
        k = (d, float(c))
        rows[k] = "TRIM72 raiser + p53 reference activator" if k in rows else "p53 reference activator"
    sel = pd.DataFrame([(d, c, r) for (d, c), r in rows.items()], columns=["drug", "conc", "role"])
    sel = sel.merge(t[["drug", "conc", "fold_change", "z_corrected", "P53_ACTIVITY_z", "flags", "plates"]]
                    .rename(columns={"fold_change": "TRIM72_fold_change", "z_corrected": "TRIM72_z"}),
                    on=["drug", "conc"], how="left")
    return sel.sort_values("TRIM72_z", ascending=False).reset_index(drop=True)


def scopes_of(E, drug, conc):
    """('all used wells', wells) and, for a drug-dose with used wells on >= 2 plates, each plate's well(s) alone."""
    W = E.W
    w = W[(W["drug"] == drug) & np.isclose(W["conc"].astype(float), float(conc)) & ~W["is_dmso"] & W["used"]]
    out = [("all used wells", list(w.index))]
    if w["plate"].nunique() >= 2:
        for p_, g in w.groupby("plate"):
            out.append((f"{p_} only", list(g.index)))
    return out


def line_table(E, wells, P53, BG, genes=()):
    """Per line: mean over the wells of r2 (TRIM72 and outcomes), TRIM72 treated level (log2 CPM), P53 score,
    background |r2|."""
    ii = [E.si[s] for s in wells]
    with quiet():
        t = pd.DataFrame({"TRIM72_r2": np.nanmean(E.mat(GENE)[ii], axis=0),
                          "TRIM72_level": np.nanmean(E.mat(GENE, "Y")[ii], axis=0),
                          "P53_SCORE": np.nanmean(P53[ii], axis=0),
                          "bg_abs_r2": np.nanmean(BG[ii], axis=0)}, index=E.lines)
        for g in set(NAMED) | set(genes):
            t[g] = np.nanmean(E.mat(g)[ii], axis=0)
    return t


def analysis_a(E, A, res_dir, tab, n_perm):
    log("(a) across lines within the same wells")
    rng = np.random.default_rng(SEED)
    sel = select_drugdoses(res_dir)
    sel.to_csv(os.path.join(tab, "a_selected_drugdoses.csv"), index=False)
    P53, BG = E.p53_score(), E.bg_absr2()
    L = E.L
    groups = {"TP53-WT": (L["tp53_group"] == "WT").to_numpy(), "TP53-altered": (L["tp53_group"] == "altered")
              .to_numpy()}
    rows, ref_rows, rep_rows, cross_rows, per_line = [], [], [], [], []
    bg_genes = [g for g in E.background]
    store = {}                                   # residual vectors for the pooled test
    dd_tables = {}                               # (drug, conc, role) -> (per-line table, covariates): all used wells
    for _, s in sel.iterrows():
        drug, conc = s["drug"], s["conc"]
        scopes = scopes_of(E, drug, conc)
        for scope, wells in scopes:
            if not wells:
                continue
            t = line_table(E, wells, P53, BG, genes=bg_genes if scope == "all used wells" else ())
            b, Acov = A.cov(drug, conc, E.lines, None if scope == "all used wells" else wells)
            t["atlas_beta"], t["atlas_A"] = b.to_numpy(), Acov.to_numpy()
            # the line's untreated TRIM72 level (log2 DMSO CPM, all plates pooled; its line ranking matches the
            # plate-standardised level of (b)): a fold change is larger where the baseline is low
            t["TRIM72_base"] = np.log2(E.L[f"cpm_dmso_{GENE}"].to_numpy(dtype=float) + 0.1)
            adjust = {"none": None, "beta+A": t[["atlas_beta", "atlas_A"]].to_numpy(),
                      "bg|r2|+A": t[["bg_abs_r2", "atlas_A"]].to_numpy(),
                      "beta+A+TRIM72base": t[["atlas_beta", "atlas_A", "TRIM72_base"]].to_numpy()}
            if scope == "all used wells":
                dd_tables[(drug, conc, s["role"])] = (t, adjust)
                pl = t[["TRIM72_r2", "TRIM72_level", "P53_SCORE"] + NAMED + ["bg_abs_r2", "atlas_beta", "atlas_A",
                                                                              "TRIM72_base"]]
                per_line.append(pl.assign(drug=drug, conc=conc, cell_line=L["cell_name"].to_numpy(),
                                          tp53_group=L["tp53_group"].to_numpy()).rename_axis("cell_line_id")
                                .reset_index())
            for gname, gm in groups.items():
                for pred in ("TRIM72_r2", "TRIM72_level"):
                    for out in OUTCOMES:
                        for adj, Z in adjust.items():
                            n, r, p, pp = partial_spearman(t[pred].to_numpy()[gm], t[out].to_numpy()[gm],
                                                           None if Z is None else Z[gm], n_perm, rng)
                            rows.append({"drug": drug, "conc": conc, "role": s["role"], "scope": scope,
                                         "wells": ",".join(wells), "tp53_group": gname, "predictor": pred,
                                         "outcome": out, "adjustment": adj, "n_lines": n, "rho": r, "p": p,
                                         "p_perm": pp})
                if scope != "all used wells":
                    continue
                # empirical reference: TRIM72 r2 vs every background (non-p53) panel gene, same lines and covariates
                for adj in ("none", "beta+A", "beta+A+TRIM72base"):
                    Z = adjust[adj]
                    bg = []
                    for g in bg_genes:
                        if np.isfinite(t[g].to_numpy()[gm]).sum() >= 8:
                            bg.append(partial_spearman(t["TRIM72_r2"].to_numpy()[gm], t[g].to_numpy()[gm],
                                                       None if Z is None else Z[gm])[1])
                    bg = np.array([v for v in bg if np.isfinite(v)])
                    for out in OUTCOMES:
                        r = partial_spearman(t["TRIM72_r2"].to_numpy()[gm], t[out].to_numpy()[gm],
                                             None if Z is None else Z[gm])[1]
                        ref_rows.append({"drug": drug, "conc": conc, "tp53_group": gname, "adjustment": adj,
                                         "outcome": out, "rho": r, "n_background_genes": len(bg),
                                         "background_median_rho": np.median(bg) if len(bg) else np.nan,
                                         "background_p05": np.quantile(bg, 0.05) if len(bg) else np.nan,
                                         "background_p95": np.quantile(bg, 0.95) if len(bg) else np.nan,
                                         "percentile_among_background": float(100 * (bg < r).mean())
                                         if len(bg) and np.isfinite(r) else np.nan})
                    # residual (rank, covariates partialled out) vectors for the pooled line-permutation test
                    for pred in ("TRIM72_r2", "TRIM72_level"):
                        for out in OUTCOMES:
                            store[(drug, conc, s["role"], gname, adj, pred, out)] = \
                                rank_residuals(t[pred].to_numpy(), t[out].to_numpy(), gm, Z)
        # replicate reliability and cross-well correlations for drug-doses with wells on two plates
        if len(scopes) >= 3:
            (p1, w1), (p2, w2) = scopes[1], scopes[2]
            t1, t2 = line_table(E, w1, P53, BG), line_table(E, w2, P53, BG)
            b, Acov = A.cov(drug, conc, E.lines)
            Z = np.column_stack([b.to_numpy(), Acov.to_numpy()])
            for gname, gm in groups.items():
                for feat in ["TRIM72_r2", "TRIM72_level"] + OUTCOMES:
                    n, r, p, _ = partial_spearman(t1[feat].to_numpy()[gm], t2[feat].to_numpy()[gm])
                    rep_rows.append({"drug": drug, "conc": conc, "tp53_group": gname, "feature": feat,
                                     "plates": f"{p1.split()[0]} vs {p2.split()[0]}", "n_lines": n,
                                     "rho_replicate": r, "p": p})
                for out in OUTCOMES:
                    for adj, ZZ in (("none", None), ("beta+A", Z)):
                        a1 = partial_spearman(t1["TRIM72_r2"].to_numpy()[gm], t2[out].to_numpy()[gm],
                                              None if ZZ is None else ZZ[gm], n_perm, rng)
                        a2 = partial_spearman(t2["TRIM72_r2"].to_numpy()[gm], t1[out].to_numpy()[gm],
                                              None if ZZ is None else ZZ[gm], n_perm, rng)
                        s1 = partial_spearman(t1["TRIM72_r2"].to_numpy()[gm], t1[out].to_numpy()[gm],
                                              None if ZZ is None else ZZ[gm])
                        s2 = partial_spearman(t2["TRIM72_r2"].to_numpy()[gm], t2[out].to_numpy()[gm],
                                              None if ZZ is None else ZZ[gm])
                        cross_rows.append({"drug": drug, "conc": conc, "tp53_group": gname, "outcome": out,
                                           "adjustment": adj, "well_A": p1.split()[0], "well_B": p2.split()[0],
                                           "n_lines": min(a1[0], a2[0]),
                                           "rho_TRIM72_wellA_vs_outcome_wellB": a1[1], "p_perm_AB": a1[3],
                                           "rho_TRIM72_wellB_vs_outcome_wellA": a2[1], "p_perm_BA": a2[3],
                                           "rho_cross_mean": np.nanmean([a1[1], a2[1]]),
                                           "rho_same_well_A": s1[1], "rho_same_well_B": s2[1],
                                           "rho_same_well_mean": np.nanmean([s1[1], s2[1]])})
    R = pd.DataFrame(rows)
    # BH over drug-doses x outcomes within each family (scope type x predictor x adjustment x TP53 group)
    R["scope_type"] = np.where(R["scope"] == "all used wells", "all used wells", "one plate's well")
    R["q_bh"] = np.nan
    for _key, g in R.groupby(["scope_type", "predictor", "adjustment", "tp53_group"]):
        R.loc[g.index, "q_bh"] = bh(g["p_perm"].to_numpy())
    # WT vs altered difference of the same test (Fisher z)
    k_of = {"none": 0, "beta+A": 2, "bg|r2|+A": 2, "beta+A+TRIM72base": 3}
    piv = R.pivot_table(index=["drug", "conc", "scope", "predictor", "outcome", "adjustment"], columns="tp53_group",
                        values=["rho", "n_lines"], aggfunc="first")
    dif = []
    for idx, r in piv.iterrows():
        d, p = fisher_diff(r[("rho", "TP53-WT")], r[("n_lines", "TP53-WT")], r[("rho", "TP53-altered")],
                           r[("n_lines", "TP53-altered")], k_of[idx[5]])
        dif.append(dict(zip(["drug", "conc", "scope", "predictor", "outcome", "adjustment"], idx),
                        rho_WT=r[("rho", "TP53-WT")], n_WT=r[("n_lines", "TP53-WT")],
                        rho_altered=r[("rho", "TP53-altered")], n_altered=r[("n_lines", "TP53-altered")],
                        fisher_z_WT_minus_altered=d, p_difference=p))
    Dd = pd.DataFrame(dif)
    R.to_csv(os.path.join(tab, "a_line_correlations.csv"), index=False)
    Dd.to_csv(os.path.join(tab, "a_line_correlations_WT_vs_altered.csv"), index=False)
    pd.DataFrame(ref_rows).to_csv(os.path.join(tab, "a_reference_background_genes.csv"), index=False)
    pd.DataFrame(rep_rows).to_csv(os.path.join(tab, "a_replicate_reliability.csv"), index=False)
    pd.DataFrame(cross_rows).to_csv(os.path.join(tab, "a_cross_well_correlations.csv"), index=False)
    pd.concat(per_line, ignore_index=True).to_csv(os.path.join(tab, "a_per_line_effects.csv"), index=False)
    # pooled over drug-doses: mean Fisher z, ONE line permutation applied to every drug-dose at once (the drug-doses
    # share lines and wells, so they are not independent; permuting line labels jointly keeps that dependence)
    pooled = []
    sets = (("TRIM72 raisers", ("TRIM72 raiser", "TRIM72 raiser + p53 reference activator")),
            ("p53 reference activators", ("p53 reference activator", "TRIM72 raiser + p53 reference activator")),
            ("p53 reference activators that do not raise TRIM72", ("p53 reference activator",)),
            ("all selected", ("TRIM72 raiser", "p53 reference activator", "TRIM72 raiser + p53 reference activator")))
    n_pool = max(1000, n_perm)
    for setname, roles in sets:
        for gname, gm in groups.items():
            idx = np.where(gm)[0]
            prng = np.random.default_rng(SEED)
            perms = np.stack([np.arange(len(idx))] + [prng.permutation(len(idx)) for _ in range(n_pool)])
            for adj in ("none", "beta+A", "beta+A+TRIM72base"):
                for pred in ("TRIM72_r2", "TRIM72_level"):
                    for out in OUTCOMES:
                        keys = [k for k in store if k[2] in roles and k[3] == gname and k[4] == adj
                                and k[5] == pred and k[6] == out]
                        if not keys:
                            continue
                        Zs = np.stack([fisher_z_perm(store[k][0][idx], store[k][1][idx], perms) for k in keys])
                        with quiet():
                            mz = np.nanmean(Zs, axis=0)
                        obs, null = mz[0], mz[1:]
                        pooled.append({"set": setname, "tp53_group": gname, "adjustment": adj, "predictor": pred,
                                       "outcome": out, "n_drugdoses": len(keys),
                                       "mean_rho": float(np.tanh(obs)),
                                       "n_drugdoses_rho_negative": int(np.sum(Zs[:, 0] < 0)),
                                       "p_line_permutation": float((1 + (np.abs(null) >= abs(obs) - 1e-12).sum())
                                                                   / (len(null) + 1)),
                                       "n_permutations": n_pool,
                                       "drugdoses": "; ".join(f"{k[0]} {k[1]:g}" for k in keys)})
    pooled = pd.DataFrame(pooled)
    pooled["q_bh_within_set_group_adjustment"] = np.nan
    for _k, g in pooled.groupby(["set", "tp53_group", "adjustment"]):
        pooled.loc[g.index, "q_bh_within_set_group_adjustment"] = bh(g["p_line_permutation"].to_numpy())
    pooled.to_csv(os.path.join(tab, "a_pooled_over_drugdoses.csv"), index=False)
    pooled_wt_vs_altered(dd_tables, groups, sets, tab, max(500, n_perm // 10))
    log(f"  (a) {len(sel)} drug-doses, {len(R)} tests")
    return R


def pooled_wt_vs_altered(dd_tables, groups, sets, tab, n_perm):
    """Is the pooled TRIM72_r2-vs-outcome correlation different in TP53-WT and TP53-altered lines? Observed
    difference of the mean Fisher z (WT minus altered) over the set's drug-doses; null: the TP53 labels permuted
    over the lines (group sizes kept), residuals recomputed within the permuted groups."""
    wt, alt = groups["TP53-WT"], groups["TP53-altered"]
    pool = np.where(wt | alt)[0]
    n_wt = int(wt.sum())
    rng = np.random.default_rng(SEED + 7)
    labels = [None] + [rng.permutation(pool) for _ in range(n_perm)]
    rows = []
    for setname, roles in sets:
        if setname == "p53 reference activators that do not raise TRIM72":
            continue
        keys = [k for k in dd_tables if k[2] in roles]
        for adj in ("none", "beta+A"):
            for out in ("P53_SCORE", "MDM2", "CDKN1A", "TP53", "BBC3", "PMAIP1"):
                diffs = []
                for lab in labels:
                    if lab is None:
                        g1, g2 = wt, alt
                    else:
                        g1 = np.zeros(len(wt), bool)
                        g1[lab[:n_wt]] = True
                        g2 = np.zeros(len(wt), bool)
                        g2[lab[n_wt:]] = True
                    zz = {1: [], 2: []}
                    for k in keys:
                        t, adjust = dd_tables[k]
                        Z = adjust[adj]
                        x, y = t["TRIM72_r2"].to_numpy(), t[out].to_numpy()
                        for gi, gm in ((1, g1), (2, g2)):
                            rx, ry = rank_residuals(x, y, gm, Z)
                            ok = np.isfinite(rx) & np.isfinite(ry)
                            if ok.sum() >= 6:
                                zz[gi].append(np.arctanh(np.clip(pcorr(rx[ok], ry[ok]), -0.999999, 0.999999)))
                    diffs.append(np.mean(zz[1]) - np.mean(zz[2]) if zz[1] and zz[2] else np.nan)
                obs, null = diffs[0], np.array(diffs[1:], float)
                null = null[np.isfinite(null)]
                rows.append({"set": setname, "adjustment": adj, "predictor": "TRIM72_r2", "outcome": out,
                             "n_drugdoses": len(keys), "fisher_z_WT_minus_altered": obs,
                             "p_tp53_label_permutation": float((1 + (np.abs(null) >= abs(obs) - 1e-12).sum())
                                                               / (len(null) + 1)), "n_permutations": len(null)})
    pd.DataFrame(rows).to_csv(os.path.join(tab, "a_pooled_WT_vs_altered.csv"), index=False)


# ============================================================================= (b) baseline (DMSO wells)
def perm_spearman(x, y, n_perm, rng):
    n, r, p, pp = partial_spearman(x, y, None, n_perm, rng)
    return n, r, p, pp


def analysis_b(E, data, tab, n_perm):
    log("(b) baseline: DMSO wells, within plates")
    rng = np.random.default_rng(SEED + 1)
    gp = os.path.join(data, "gene_panel")
    sm = pd.read_csv(os.path.join(gp, "sample_map.csv"), dtype={"sample": str, "plate": str})
    dm = sm[sm["is_dmso"].astype(bool) & ~sm["sample"].isin(E.meta["failed_wells"])]
    genes = [GENE] + E.members + [g for g in NAMED if g not in E.members]
    cols = ["sample", "cell_line_id", "n_cells", "total_counts"] + genes
    wl = pd.read_parquet(os.path.join(gp, "well_line.parquet"), columns=cols)
    wl = wl[wl["sample"].astype(str).isin(dm["sample"])].copy()
    wl["plate"] = wl["sample"].astype(str).map(dm.set_index("sample")["plate"])
    agg = wl.groupby(["plate", "cell_line_id"])[["n_cells", "total_counts"] + genes].sum()
    agg = agg[agg["n_cells"] >= T.MIN_CELLS]
    expr = {g: E.L[f"expr_{g}"].astype(bool) if f"expr_{g}" in E.L else pd.Series(True, index=E.lines)
            for g in genes}
    # Relative level = observed / expected counts, expected = the plate's median expressing line's CPM x the
    # profile's library size (indirect standardisation within each plate: removes the TRIM72 plate batch and lets
    # shallow profiles weigh little); summed over the plates of a set, log2((O + 0.5) / (E + 0.5)); NaN when the
    # expected count is < MIN_EXPECTED (too shallow to rank).
    MIN_EXPECTED = 2.0
    O, Ex = {}, {}
    for g in genes:
        cpm_g = (1e6 * agg[g] / agg["total_counts"])
        ok = cpm_g.index.get_level_values("cell_line_id").map(expr[g]).fillna(False).to_numpy(dtype=bool)
        med = cpm_g[ok].groupby(level="plate").median()
        e = agg["total_counts"] / 1e6 * agg.index.get_level_values("plate").map(med).to_numpy(dtype=float)
        O[g] = agg[g].where(ok).unstack("plate").reindex(E.lines)
        Ex[g] = e.where(ok).unstack("plate").reindex(E.lines)

    def rel_of(g, pl):
        o, e = O[g][pl].sum(axis=1, min_count=1), Ex[g][pl].sum(axis=1, min_count=1)
        r = np.log2((o + 0.5) / (e + 0.5))
        return r.where(e >= MIN_EXPECTED)

    cpm = (1e6 * agg[GENE] / agg["total_counts"]).unstack("plate").reindex(E.lines)
    cnt = agg[GENE].unstack("plate").reindex(E.lines)
    plates = sorted(cpm.columns, key=lambda p_: int(p_.replace("plate", "")))
    rel = {g: pd.concat({p_: rel_of(g, [p_]) for p_ in plates}, axis=1) for g in genes}   # per plate
    with quiet():
        basal_pl = pd.concat({p_: pd.concat({g: rel[g][p_] for g in E.members}, axis=1).mean(axis=1)
                              for p_ in plates}, axis=1)       # within-plate basal p53 activity (expressed members)
    reliable = [p_ for p_ in plates if p_ not in E.meta["unreliable_plates"]]
    high = [p_ for p_ in reliable if p_ in HIGH_TRIM72_PLATES]
    low = [p_ for p_ in reliable if p_ not in HIGH_TRIM72_PLATES]
    f = pd.read_csv(os.path.join(data, "gene_panel", "results", "p53_functional_status.csv")).set_index(
        "cell_line_id").reindex(E.lines)
    with quiet():
        basal_rel = pd.concat({g: rel_of(g, reliable) for g in E.members}, axis=1).mean(axis=1)
        lt = pd.DataFrame({"cell_line": E.L["cell_name"], "organ": E.L["organ"], "tp53_group": E.L["tp53_group"],
                           "TRIM72_expressed": expr[GENE],
                           "TRIM72_rel_reliable_plates": rel_of(GENE, reliable),
                           "TRIM72_rel_high_plates": rel_of(GENE, high),
                           "TRIM72_rel_low_plates": rel_of(GENE, low),
                           "TRIM72_rel_all_plates": rel_of(GENE, plates),
                           "TRIM72_expected_counts_reliable_plates": Ex[GENE][reliable].sum(axis=1, min_count=1),
                           "TRIM72_counts_DMSO_reliable_plates": cnt[reliable].sum(axis=1),
                           "TRIM72_cpm_median_high_plates": cpm[high].median(axis=1),
                           "TRIM72_cpm_median_low_plates": cpm[low].median(axis=1),
                           "basal_p53_within_plate": basal_rel,
                           "basal_p53_activity_log2_panel": f["basal_p53_activity_log2"],
                           "p53_responsiveness_log2_panel": f["p53_responsiveness_log2"],
                           "p53_functional_call_panel": f["functional_call"]})
        for g in NAMED:
            lt[f"{g}_rel_reliable_plates"] = rel_of(g, reliable)
    lt.loc[~lt["TRIM72_expressed"], [c for c in lt.columns if c.startswith("TRIM72_rel")]] = np.nan
    lt.index.name = "cell_line_id"
    lt.to_csv(os.path.join(tab, "b_baseline_per_line.csv"))
    # per plate: the TRIM72 relative level and the within-plate basal p53 activity, long
    long = pd.concat({"TRIM72_rel": rel[GENE].stack(), "basal_p53_within_plate": basal_pl.stack(),
                      "TRIM72_counts": cnt.stack(), "TRIM72_cpm": cpm.stack()}, axis=1).reset_index()
    long.columns = ["cell_line_id", "plate"] + list(long.columns[2:])
    long["tp53_group"] = long["cell_line_id"].map(E.L["tp53_group"])
    long.to_csv(os.path.join(tab, "b_baseline_per_plate_line.csv"), index=False)

    groups = {"TP53-WT": lt["tp53_group"] == "WT", "TP53-altered": lt["tp53_group"] == "altered",
              "all lines": lt["tp53_group"].notna()}
    rows = []
    # (1) does the line ranking of TRIM72 survive the plate batch? high- vs low-baseline plates
    for gname, gm in groups.items():
        n, r, p, pp = perm_spearman(lt.loc[gm, "TRIM72_rel_high_plates"], lt.loc[gm, "TRIM72_rel_low_plates"],
                                    n_perm, rng)
        rows.append({"test": "TRIM72 line ranking: high-baseline plates vs low-baseline plates", "x":
                     "TRIM72_rel_high_plates", "y": "TRIM72_rel_low_plates", "tp53_group": gname, "n_lines": n,
                     "rho": r, "p": p, "p_perm": pp})
    xs = ["TRIM72_rel_reliable_plates", "TRIM72_rel_high_plates", "TRIM72_rel_low_plates"]
    ys = ["basal_p53_within_plate", "basal_p53_activity_log2_panel", "p53_responsiveness_log2_panel"] + \
        [f"{g}_rel_reliable_plates" for g in NAMED]
    for gname, gm in groups.items():
        for x in xs:
            for y in ys:
                n, r, p, pp = perm_spearman(lt.loc[gm, x], lt.loc[gm, y], n_perm, rng)
                rw, pw = P.spearman_within(lt.loc[gm, x], lt.loc[gm, y], lt.loc[gm, "organ"])
                rows.append({"test": "TRIM72 untreated level vs p53 readout", "x": x, "y": y, "tp53_group": gname,
                             "n_lines": n, "rho": r, "p": p, "p_perm": pp, "rho_within_organ": rw,
                             "p_within_organ": pw})
    # the TP53 group itself: is TRIM72 untreated level different in WT vs altered lines?
    a = lt.loc[groups["TP53-WT"], "TRIM72_rel_reliable_plates"].dropna()
    b = lt.loc[groups["TP53-altered"], "TRIM72_rel_reliable_plates"].dropna()
    u = stats.mannwhitneyu(a, b, alternative="two-sided")
    rows.append({"test": "TRIM72 untreated level, TP53-WT vs altered (Mann-Whitney; rho column = AUC P(WT > alt))",
                 "x": "TRIM72_rel_reliable_plates", "y": "tp53_group", "tp53_group": "WT vs altered",
                 "n_lines": len(a) + len(b), "rho": u.statistic / (len(a) * len(b)), "p": u.pvalue,
                 "median_WT": a.median(), "median_altered": b.median()})
    R = pd.DataFrame(rows)
    R["q_bh"] = np.nan
    m = R["test"] == "TRIM72 untreated level vs p53 readout"
    R.loc[m, "q_bh"] = bh(R.loc[m, "p_perm"].to_numpy())
    R.to_csv(os.path.join(tab, "b_baseline_tests.csv"), index=False)
    # per plate: TRIM72 relative level vs within-plate basal p53 activity, by TP53 group
    pr = []
    for p_ in plates:
        for gname, gm in groups.items():
            n, r, p, _ = partial_spearman(rel[GENE][p_][gm.to_numpy()], basal_pl[p_][gm.to_numpy()])
            pr.append({"plate": p_, "trim72_baseline_batch": "high" if p_ in HIGH_TRIM72_PLATES else "low",
                       "unreliable_plate": p_ in E.meta["unreliable_plates"], "tp53_group": gname, "n_lines": n,
                       "rho": r, "p": p, "median_line_TRIM72_cpm": float(cpm[p_].median()),
                       "median_line_TRIM72_counts": float(cnt[p_].median())})
    pr = pd.DataFrame(pr)
    pr.to_csv(os.path.join(tab, "b_baseline_per_plate_correlations.csv"), index=False)
    log(f"  (b) {len(plates)} plates ({len(high)} high / {len(low)} low TRIM72 baseline, reliable), "
        f"{int(lt['TRIM72_expressed'].sum())} lines express TRIM72")
    return R


# ============================================================================= (c) across drug-doses
def mh_odds_ratio(a, b, c, d):
    """Mantel-Haenszel common odds ratio over strata (arrays of 2x2 cells) and the CMH chi-square p (1 df,
    continuity-corrected)."""
    a, b, c, d = (np.asarray(v, float) for v in (a, b, c, d))
    n = a + b + c + d
    ok = n > 1
    a, b, c, d, n = a[ok], b[ok], c[ok], d[ok], n[ok]
    num, den = (a * d / n).sum(), (b * c / n).sum()
    orr = num / den if den > 0 else np.inf
    ea = (a + b) * (a + c) / n
    va = (a + b) * (c + d) * (a + c) * (b + d) / (n * n * (n - 1))
    chi = (abs((a - ea).sum()) - 0.5) ** 2 / va.sum() if va.sum() > 0 else np.nan
    return float(orr), float(stats.chi2.sf(chi, 1)) if np.isfinite(chi) else np.nan


def block_bootstrap_rho(x, y, Z, blocks, n_boot, rng):
    """95% CI of the (partial) Spearman by resampling whole drugs (all doses of a drug together)."""
    ub = pd.unique(blocks)
    pos = {b: np.where(blocks == b)[0] for b in ub}
    out = []
    for _ in range(n_boot):
        pick = rng.choice(ub, size=len(ub), replace=True)
        ii = np.concatenate([pos[b] for b in pick])
        out.append(partial_spearman(x[ii], y[ii], None if Z is None else Z[ii])[1])
    out = np.array([v for v in out if np.isfinite(v)])
    return (float(np.quantile(out, 0.025)), float(np.quantile(out, 0.975))) if len(out) else (np.nan, np.nan)


def analysis_c(E, data, cdir, tab, n_boot):
    log("(c) across drug-doses")
    rng = np.random.default_rng(SEED + 2)
    res_dir = os.path.join(data, "gene_panel", "results")
    al = pd.read_csv(os.path.join(cdir, "drug_effects_all_genes.csv.gz"))
    key = ["drug", "conc"]
    zt = al.pivot_table(index=key, columns="gene", values="z_corrected", aggfunc="first")
    ft = al.pivot_table(index=key, columns="gene", values="fold_change", aggfunc="first")
    tri = al[al["gene"] == GENE].set_index(key)
    sc = pd.read_csv(os.path.join(res_dir, "pathway_scores_by_dose.csv"))
    p53s = sc[sc["score"] == "P53_ACTIVITY"].set_index(key)
    wt = pd.read_csv(os.path.join(res_dir, "p53_wt_vs_altered.csv")).set_index(key)
    ctx = pd.read_csv(os.path.join(res_dir, "drug_context_by_dose.csv")).set_index(key)
    at = pd.read_csv(os.path.join(data, "atlas", "effects", "drugdose.csv")).set_index(key)
    D = pd.DataFrame(index=tri.index)
    D["TRIM72_fold_change"] = tri["fold_change"]
    D["TRIM72_z"] = tri["z_corrected"]
    D["TRIM72_fdr_up"] = tri["fdr_up"]
    D["TRIM72_call"] = tri["call"].fillna("")
    D["P53_ACTIVITY_fold_change"] = p53s["fold_change"].reindex(D.index)
    D["P53_ACTIVITY_z"] = p53s["z"].reindex(D.index)
    D["P53_ACTIVITY_fdr_up"] = p53s["fdr_up"].reindex(D.index)
    D["p53_WT_minus_altered_z"] = wt["z_wt_more"].reindex(D.index)
    D["p53_WT_minus_altered_log2"] = wt["extra_log2_p53_induction_in_WT"].reindex(D.index)
    D["p53_wt_pattern"] = wt["pattern"].reindex(D.index)
    for g in NAMED + [m for m in E.members if m not in NAMED]:
        D[f"{g}_z"] = zt[g].reindex(D.index)
    for g in NAMED:
        D[f"{g}_fold_change"] = ft[g].reindex(D.index)
    mem = [f"{g}_z" for g in E.members]
    D["n_p53_members_z_ge_3"] = (D[mem] >= 3).sum(axis=1)
    D["median_p53_member_z"] = D[mem].median(axis=1)
    D["atlas_n_sig_genes"] = at["n_sig_genes"].reindex(D.index)
    for c in ("cells_log2_vs_plate", "S_PHASE_z", "G2M_PHASE_z", "umi_per_cell_log2_vs_plate", "ISR_z", "NRF2_z",
              "UPR_z", "HEAT_SHOCK_z", "NFKB_z"):
        D[c] = ctx[c].reindex(D.index)
    D["flags"] = tri["flags"]
    D["plates"] = tri["plates"]
    D["unreliable_plate_only"] = at["unreliable_plate_only"].reindex(D.index)
    D["moa_fine"] = at["moa_fine"].reindex(D.index)
    D["targets"] = at["targets"].reindex(D.index)
    D = D.reset_index()
    # the panel's DNA-damage definition (names by prefix, or TOP1/TOP2/TYMS/DHFR/RRM targets)
    dmeta = at.reset_index().drop_duplicates("drug").set_index("drug")[["targets", "moa_fine"]]
    dna = set(P.find_drugs(set(D["drug"]), dmeta, P.DNA_DAMAGE))
    D["dna_damaging"] = D["drug"].isin(dna)
    # categories
    t_up = D["TRIM72_call"].eq("up")
    t_not = D["TRIM72_z"] < 2
    p_up = (D["P53_ACTIVITY_fdr_up"] < 0.10) & (D["P53_ACTIVITY_z"] >= 3)
    p_not = D["P53_ACTIVITY_z"] < 2
    D["category"] = np.select([t_up & p_up, t_up & p_not, p_up & t_not, t_up, p_up],
                              ["TRIM72 up + p53 activated", "TRIM72 up, p53 NOT activated (z < 2)",
                               "p53 activated, TRIM72 NOT up (z < 2)", "TRIM72 up, p53 in between",
                               "p53 activated, TRIM72 in between"], "neither")
    D.to_csv(os.path.join(tab, "c_drugdose_table.csv"), index=False)

    # correlations across drug-doses
    act = ["atlas_n_sig_genes", "cells_log2_vs_plate", "S_PHASE_z", "G2M_PHASE_z"]
    outs = ["P53_ACTIVITY_z", "MDM2_z", "CDKN1A_z", "BBC3_z", "PMAIP1_z", "TP53_z", "p53_WT_minus_altered_z"]
    subsets = {"all drug-doses": np.ones(len(D), bool),
               "not on an unreliable plate only": ~D["unreliable_plate_only"].fillna(False).astype(bool).to_numpy(),
               "active (atlas >= 100 significant genes)": (D["atlas_n_sig_genes"] >= 100).to_numpy(),
               "p53 activators (P53_ACTIVITY z >= 3, FDR < 0.10)": p_up.to_numpy(),
               "TRIM72 raisers (call up)": t_up.to_numpy()}
    rows = []
    x = D["TRIM72_z"].to_numpy()
    blocks = D["drug"].to_numpy()
    for sname, m in subsets.items():
        for out in outs + ["MDM2_z | P53_ACTIVITY_z"]:
            if out == "MDM2_z | P53_ACTIVITY_z":
                y = D["MDM2_z"].to_numpy()
                adjs = {"P53_ACTIVITY_z": D[["P53_ACTIVITY_z"]].to_numpy(),
                        "P53_ACTIVITY_z + activity": D[["P53_ACTIVITY_z"] + act].to_numpy()}
            else:
                y = D[out].to_numpy()
                adjs = {"none": None, "activity (n_sig_genes, cells, S, G2M)": D[act].to_numpy()}
            for adj, Z in adjs.items():
                n, r, p, _ = partial_spearman(x[m], y[m], None if Z is None else Z[m])
                lo, hi = block_bootstrap_rho(x[m], y[m], None if Z is None else Z[m], blocks[m],
                                             n_boot if n >= 20 else 0, rng) if n >= 20 else (np.nan, np.nan)
                rows.append({"subset": sname, "x": "TRIM72_z", "y": out, "adjustment": adj, "n_drugdoses": n,
                             "rho": r, "p": p, "ci95_low_drug_bootstrap": lo, "ci95_high_drug_bootstrap": hi})
    # within single plates (drug-doses with one used plate): Spearman per plate, mean over plates
    one = D["plates"].astype(str).str.count(",").eq(0)
    for out in ("P53_ACTIVITY_z", "MDM2_z"):
        rs = []
        for p_, g in D[one].groupby("plates"):
            if len(g) >= 20:
                rs.append(partial_spearman(g["TRIM72_z"].to_numpy(), g[out].to_numpy())[1])
        rows.append({"subset": "within plates (mean over plates of the per-plate Spearman)", "x": "TRIM72_z",
                     "y": out, "adjustment": "none", "n_drugdoses": int(one.sum()), "rho": float(np.nanmean(rs)),
                     "p": np.nan, "n_plates": len(rs), "n_plates_rho_positive": int(np.sum(np.array(rs) > 0))})
    C = pd.DataFrame(rows)
    C.to_csv(os.path.join(tab, "c_correlations_across_drugdoses.csv"), index=False)

    # enrichment: TRIM72 up vs p53 activated, raw and stratified by drug activity (deciles of n_sig_genes)
    er = []
    a_ = (t_up & p_up).sum()
    b_ = (t_up & ~p_up).sum()
    c_ = (~t_up & p_up).sum()
    d_ = (~t_up & ~p_up).sum()
    orr, pf = stats.fisher_exact([[a_, b_], [c_, d_]])
    er.append({"test": "Fisher exact (all drug-doses)", "TRIM72_up_and_p53_activated": int(a_),
               "TRIM72_up_only": int(b_), "p53_activated_only": int(c_), "neither": int(d_), "odds_ratio": orr,
               "p": pf})
    dec = pd.qcut(D["atlas_n_sig_genes"].rank(method="first"), 10, labels=False)
    A_, B_, C_, D_ = [], [], [], []
    for k in range(10):
        mm = (dec == k).to_numpy()
        A_.append((t_up & p_up)[mm].sum())
        B_.append((t_up & ~p_up)[mm].sum())
        C_.append((~t_up & p_up)[mm].sum())
        D_.append((~t_up & ~p_up)[mm].sum())
    orr2, p2 = mh_odds_ratio(A_, B_, C_, D_)
    er.append({"test": "Mantel-Haenszel, strata = deciles of atlas n_sig_genes", "TRIM72_up_and_p53_activated":
               int(sum(A_)), "TRIM72_up_only": int(sum(B_)), "p53_activated_only": int(sum(C_)),
               "neither": int(sum(D_)), "odds_ratio": orr2, "p": p2})
    pd.DataFrame(er).to_csv(os.path.join(tab, "c_trim72_up_vs_p53_activated_enrichment.csv"), index=False)

    # what the p53 targets do in each category
    cats = ["TRIM72 up + p53 activated", "TRIM72 up, p53 NOT activated (z < 2)", "p53 activated, TRIM72 NOT up (z < 2)",
            "TRIM72 up, p53 in between", "p53 activated, TRIM72 in between", "neither"]
    summ = []
    for ccat in cats:
        g = D[D["category"] == ccat]
        r = {"category": ccat, "n_drugdoses": len(g), "median_TRIM72_z": g["TRIM72_z"].median(),
             "median_P53_ACTIVITY_z": g["P53_ACTIVITY_z"].median(),
             "median_p53_WT_minus_altered_z": g["p53_WT_minus_altered_z"].median(),
             "frac_WT_induction_pattern_fdr10": float(((g["p53_wt_pattern"] == "WT induction")
                                                       & (wt["fdr"].reindex(pd.MultiIndex.from_frame(g[key]))
                                                          .to_numpy() < 0.10)).mean()) if len(g) else np.nan}
        for gname in NAMED:
            r[f"median_{gname}_z"] = g[f"{gname}_z"].median()
        r["median_n_p53_members_z_ge_3"] = g["n_p53_members_z_ge_3"].median()
        r["median_atlas_n_sig_genes"] = g["atlas_n_sig_genes"].median()
        r["frac_dna_damaging"] = g["dna_damaging"].mean() if len(g) else np.nan
        summ.append(r)
    pd.DataFrame(summ).to_csv(os.path.join(tab, "c_category_summary.csv"), index=False)
    lst = D[D["category"] != "neither"].sort_values(["category", "TRIM72_z"], ascending=[True, False])
    keep = ["category", "drug", "conc", "TRIM72_fold_change", "TRIM72_z", "P53_ACTIVITY_fold_change",
            "P53_ACTIVITY_z", "p53_WT_minus_altered_z", "p53_wt_pattern"] + [f"{g}_z" for g in NAMED] + \
        ["n_p53_members_z_ge_3", "median_p53_member_z", "atlas_n_sig_genes", "cells_log2_vs_plate", "S_PHASE_z",
         "G2M_PHASE_z", "ISR_z", "NRF2_z", "UPR_z", "HEAT_SHOCK_z", "dna_damaging", "flags", "plates", "moa_fine"]
    lst[keep].to_csv(os.path.join(tab, "c_categories_drugdoses.csv"), index=False)
    log(f"  (c) {len(D)} drug-doses; categories: " + "; ".join(f"{k} {int((D['category'] == k).sum())}"
                                                           for k in cats))
    return D, C


# ============================================================================= (d) single cells
def poisson_glm(y, X, off, n_iter=30, tol=1e-8):
    """Poisson GLM (log link, offset) by IRLS; returns coefficients, quasi-Poisson covariance (dispersion = Pearson
    chi2 / df, floored at 1) and the dispersion."""
    n, p = X.shape
    b = np.zeros(p)
    b[0] = np.log(max(y.mean(), 1e-8) / np.exp(off).mean())
    for _ in range(n_iter):
        eta = X @ b + off
        mu = np.exp(np.clip(eta, -30, 30))
        z = eta - off + (y - mu) / mu
        XtW = X.T * mu
        try:
            bn = np.linalg.solve(XtW @ X, XtW @ z)
        except np.linalg.LinAlgError:
            return None
        if np.max(np.abs(bn - b)) < tol:
            b = bn
            break
        b = bn
    mu = np.exp(np.clip(X @ b + off, -30, 30))
    phi = max(1.0, float(((y - mu) ** 2 / mu).sum() / max(1, n - p)))
    try:
        cov = phi * np.linalg.inv((X.T * mu) @ X)
    except np.linalg.LinAlgError:
        return None
    return b, cov, phi


def dl_meta(est, se):
    """DerSimonian-Laird random-effects meta-analysis: estimate, SE, z, p, tau2, I2."""
    est, se = np.asarray(est, float), np.asarray(se, float)
    ok = np.isfinite(est) & np.isfinite(se) & (se > 0)
    est, se = est[ok], se[ok]
    k = len(est)
    if k < 2:
        return dict(k=k, estimate=np.nan, se=np.nan, z=np.nan, p=np.nan, tau2=np.nan, I2=np.nan)
    w = 1 / se ** 2
    fe = (w * est).sum() / w.sum()
    Q = (w * (est - fe) ** 2).sum()
    c = w.sum() - (w ** 2).sum() / w.sum()
    tau2 = max(0.0, (Q - (k - 1)) / c) if c > 0 else 0.0
    ws = 1 / (se ** 2 + tau2)
    m = (ws * est).sum() / ws.sum()
    s = np.sqrt(1 / ws.sum())
    I2 = max(0.0, (Q - (k - 1)) / Q) if Q > 0 else 0.0
    return dict(k=k, estimate=float(m), se=float(s), z=float(m / s), p=float(2 * stats.norm.sf(abs(m / s))),
                tau2=float(tau2), I2=float(I2))


def mh_rate_ratio(y, T_, det, strata):
    """Mantel-Haenszel rate ratio of counts y per UMI (T_) in TRIM72-detected vs not, over depth strata."""
    num = den = 0.0
    for s in np.unique(strata):
        m = strata == s
        a, t1 = y[m & det].sum(), T_[m & det].sum()
        b, t0 = y[m & ~det].sum(), T_[m & ~det].sum()
        tt = t1 + t0
        if t1 > 0 and t0 > 0:
            num += a * t0 / tt
            den += b * t1 / tt
    return num / den if den > 0 and num > 0 else np.nan


def analysis_d(E, cdir, tab):
    log("(d) single cells: TRIM72-detected vs not, per line, idarubicin 5 uM and DMSO (plates 6, 14)")
    cells = pd.read_parquet(os.path.join(cdir, "cells_selected.parquet"))
    wellsets = {"idarubicin 5 uM, plate6": [IDA_WELLS["plate6"]], "idarubicin 5 uM, plate14": [IDA_WELLS["plate14"]],
                "idarubicin 5 uM, both wells": list(IDA_WELLS.values()),
                "DMSO, plate6": DMSO_WELLS["plate6"], "DMSO, plate14": DMSO_WELLS["plate14"],
                "DMSO, plates 6+14": DMSO_WELLS["plate6"] + DMSO_WELLS["plate14"]}
    members = E.members
    cells["P53_SCORE"] = cells[members].sum(axis=1)
    bg = [g for g in E.background if g in cells.columns]
    outcomes = ["P53_SCORE"] + NAMED + ["ATF3"] + [m for m in members if m not in NAMED]
    allout = outcomes + [g for g in bg if g not in outcomes]
    expr = {g: (E.L[f"expr_{g}"].astype(bool) if f"expr_{g}" in E.L else pd.Series(True, index=E.lines))
            for g in allout if g != "P53_SCORE"}
    expr["P53_SCORE"] = pd.Series(True, index=E.lines)
    tp = E.L["tp53_group"]
    fits, desc, mh = [], [], []
    for wsname, wells in wellsets.items():
        sub = cells[cells["sample"].isin(wells)]
        for line, c in sub.groupby("cell_line_id"):
            if not bool(E.L.loc[line, f"expr_{GENE}"]):          # NCI-H661: TRIM72 not expressed (ambient only)
                continue
            det = (c[GENE].to_numpy() > 0)
            n, npos = len(c), int(det.sum())
            T_ = c["total_counts"].to_numpy(dtype=float)
            sS = np.log((c["S_PHASE"].to_numpy() + 0.5) / T_)
            sG = np.log((c["G2M_PHASE"].to_numpy() + 0.5) / T_)
            desc.append({"wellset": wsname, "cell_line_id": line, "cell_line": E.L.loc[line, "cell_name"],
                         "tp53_group": tp.get(line), "n_cells": n, "n_TRIM72_detected": npos,
                         "pct_TRIM72_detected": 100 * npos / n if n else np.nan,
                         "median_UMI_detected": float(np.median(T_[det])) if npos else np.nan,
                         "median_UMI_not_detected": float(np.median(T_[~det])) if n - npos else np.nan,
                         "mean_S_score_detected_minus_not": float(sS[det].mean() - sS[~det].mean())
                         if 0 < npos < n else np.nan,
                         "mean_G2M_score_detected_minus_not": float(sG[det].mean() - sG[~det].mean())
                         if 0 < npos < n else np.nan})
            if n < 50 or npos < 5 or n - npos < 5:
                continue
            lt = np.log(T_)
            cols = [np.ones(n), det.astype(float), lt - lt.mean(), sS - sS.mean(), sG - sG.mean()]
            if len(wells) > 1:
                for w_ in wells[1:]:
                    ind = (c["sample"].to_numpy() == w_).astype(float)
                    if 0 < ind.sum() < n:
                        cols.append(ind)
            X = np.column_stack(cols)
            strata = np.asarray(pd.qcut(pd.Series(lt).rank(method="first"), 5, labels=False))
            if len(wells) > 1:
                strata = strata * 10 + pd.factorize(c["sample"])[0]
            for g in allout:
                if not bool(expr[g].get(line, False)):
                    continue
                y = c[g].to_numpy(dtype=float)
                if y.sum() < 20:
                    continue
                fit = poisson_glm(y, X, lt)
                if fit is None:
                    continue
                b, cov, phi = fit
                fits.append({"wellset": wsname, "cell_line_id": line, "tp53_group": tp.get(line), "outcome": g,
                             "is_p53_outcome": g in outcomes, "n_cells": n, "n_TRIM72_detected": npos,
                             "outcome_counts": int(y.sum()), "log_rate_ratio": b[1],
                             "se": float(np.sqrt(cov[1, 1])), "dispersion": phi,
                             "log_rate_ratio_unadjusted": float(np.log(((y[det].sum() + 0.5) / T_[det].sum())
                                                                       / ((y[~det].sum() + 0.5) / T_[~det].sum())))})
                if g in ("P53_SCORE", "CDKN1A", "MDM2", "BBC3", "PMAIP1", "TP53"):
                    mh.append({"wellset": wsname, "cell_line_id": line, "tp53_group": tp.get(line), "outcome": g,
                               "mh_rate_ratio_depth_strata": mh_rate_ratio(y, T_, det, strata)})
    F = pd.DataFrame(fits)
    F.to_csv(os.path.join(tab, "d_single_cell_per_line_fits.csv.gz"), index=False)
    pd.DataFrame(desc).to_csv(os.path.join(tab, "d_single_cell_line_description.csv"), index=False)
    # meta-analysis over lines per wellset x TP53 group x outcome
    rows = []
    for (ws, grp, out), g in F.groupby(["wellset", "tp53_group", "outcome"]):
        m = dl_meta(g["log_rate_ratio"], g["se"])
        rows.append({"wellset": ws, "tp53_group": grp, "outcome": out, "is_p53_outcome": out in outcomes,
                     "n_lines": m["k"], "rate_ratio": float(np.exp(m["estimate"])) if np.isfinite(m["estimate"])
                     else np.nan, "log_rate_ratio": m["estimate"], "se": m["se"], "z": m["z"], "p": m["p"],
                     "tau2": m["tau2"], "I2": m["I2"], "n_lines_positive": int((g["log_rate_ratio"] > 0).sum()),
                     "median_line_log_rate_ratio": float(g["log_rate_ratio"].median()),
                     "median_line_log_rate_ratio_unadjusted": float(g["log_rate_ratio_unadjusted"].median())})
    M = pd.DataFrame(rows)
    # negative controls: where does each p53 outcome fall among the non-p53 (background) panel genes?
    M["control_median_log_rate_ratio"] = np.nan
    M["percentile_among_controls"] = np.nan
    M["log_rate_ratio_minus_control_median"] = np.nan
    for (ws, grp), g in M.groupby(["wellset", "tp53_group"]):
        ctl = g.loc[~g["is_p53_outcome"], "log_rate_ratio"].dropna().to_numpy()
        if len(ctl):
            M.loc[g.index, "control_median_log_rate_ratio"] = np.median(ctl)
            M.loc[g.index, "percentile_among_controls"] = [100 * (ctl < v).mean() if np.isfinite(v) else np.nan
                                                           for v in g["log_rate_ratio"]]
            M.loc[g.index, "log_rate_ratio_minus_control_median"] = g["log_rate_ratio"] - np.median(ctl)
            M.loc[g.index, "n_controls"] = len(ctl)
    M["q_bh_p53_outcomes"] = np.nan
    for _k, g in M[M["is_p53_outcome"]].groupby(["wellset", "tp53_group"]):
        M.loc[g.index, "q_bh_p53_outcomes"] = bh(g["p"].to_numpy())
    M.to_csv(os.path.join(tab, "d_single_cell_meta_all_outcomes.csv"), index=False)
    main = M[M["outcome"].isin(["P53_SCORE"] + NAMED + ["ATF3"])].copy()
    # WT vs altered difference of the meta estimates
    dif = []
    for (ws, out), g in main.groupby(["wellset", "outcome"]):
        g = g.set_index("tp53_group")
        if {"WT", "altered"} <= set(g.index):
            d = g.at["WT", "log_rate_ratio"] - g.at["altered", "log_rate_ratio"]
            se = np.sqrt(g.at["WT", "se"] ** 2 + g.at["altered", "se"] ** 2)
            dif.append({"wellset": ws, "outcome": out, "WT_minus_altered_log_rate_ratio": d, "se": se,
                        "p": float(2 * stats.norm.sf(abs(d / se))) if se > 0 else np.nan})
    main = main.merge(pd.DataFrame(dif), on=["wellset", "outcome"], how="left",
                      suffixes=("", "_WT_minus_altered"))
    main.to_csv(os.path.join(tab, "d_single_cell_meta_main.csv"), index=False)
    # depth-stratified Mantel-Haenszel rate ratios: median over lines and Wilcoxon signed-rank vs 1
    H = pd.DataFrame(mh)
    hs = []
    for (ws, grp, out), g in H.groupby(["wellset", "tp53_group", "outcome"]):
        v = np.log(g["mh_rate_ratio_depth_strata"].dropna().to_numpy())
        v = v[np.isfinite(v)]
        hs.append({"wellset": ws, "tp53_group": grp, "outcome": out, "n_lines": len(v),
                   "median_line_rate_ratio": float(np.exp(np.median(v))) if len(v) else np.nan,
                   "n_lines_above_1": int((v > 0).sum()),
                   "p_wilcoxon": float(stats.wilcoxon(v).pvalue) if len(v) >= 6 else np.nan})
    pd.DataFrame(hs).to_csv(os.path.join(tab, "d_single_cell_mh_depth_strata.csv"), index=False)
    log(f"  (d) {len(F)} per-line fits; {F['cell_line_id'].nunique()} lines")
    return main



# ============================================================================= checks, headline table, main
def checks(E, data, cdir, tab):
    rows = []
    res = os.path.join(data, "gene_panel", "results")
    # 1. TRIM72 idarubicin 5 uM per-line r2 vs the earlier corrected per-line table
    ref_f = os.path.join(REPO, "trim72_idarubicin", "corrected", "TRIM72_idarubicin_5uM_per_line_corrected.csv")
    if os.path.exists(ref_f):
        ref = pd.read_csv(ref_f).set_index("cell_line_id")["log2FC_corrected"].reindex(E.lines)
        ii = [E.si[s] for s in IDA_WELLS.values()]
        with quiet():
            mine = pd.Series(np.nanmean(E.mat(GENE)[ii], axis=0), index=E.lines)
        rows.append({"check": "TRIM72 idarubicin 5 uM per-line r2 vs trim72_idarubicin/corrected (max |diff|)",
                     "value": float((mine - ref).abs().max()), "n": int((mine.notna() & ref.notna()).sum())})
    # 2. p53 responsiveness recomputed from the cache vs the panel's p53_functional_status.csv
    f = pd.read_csv(os.path.join(res, "p53_functional_status.csv")).set_index("cell_line_id")
    rd = pd.read_csv(os.path.join(res, "p53_reference_doses.csv"))
    W = E.W[~E.W["is_dmso"] & E.W["used"]]
    keys = set(zip(rd["drug"], rd["conc"].astype(float)))
    ss = [s for s, d, c in zip(W.index, W["drug"], W["conc"].astype(float)) if (d, c) in keys]
    with quiet():
        resp = pd.Series(np.nanmean(E.p53_score()[[E.si[s] for s in ss]], axis=0), index=E.lines)
    rows.append({"check": "p53 responsiveness from the cache vs p53_functional_status.csv (max |diff|)",
                 "value": float((resp - f["p53_responsiveness_log2"].reindex(E.lines)).abs().max()),
                 "n": len(ss), "note": f"{len(ss)} reference wells"})
    # 3. TRIM72 drug-dose z in the cache vs the panel table
    al = pd.read_csv(os.path.join(cdir, "drug_effects_all_genes.csv.gz"))
    a = al[al["gene"] == GENE].set_index(["drug", "conc"])["z_corrected"]
    b = pd.read_csv(os.path.join(res, "TRIM72_drug_effects_by_dose.csv")).set_index(["drug", "conc"])["z_corrected"]
    rows.append({"check": "TRIM72 drug-dose z: cache vs TRIM72_drug_effects_by_dose.csv (max |diff|)",
                 "value": float((a - b.reindex(a.index)).abs().max()), "n": len(a)})
    # 4. per-cell rows vs the sample map's cell counts
    cells = pd.read_parquet(os.path.join(cdir, "cells_selected.parquet"), columns=["sample"])
    sm = pd.read_csv(os.path.join(data, "gene_panel", "sample_map.csv"), dtype={"sample": str}).set_index("sample")
    cnt = cells["sample"].value_counts()
    rows.append({"check": "cells per well in cells_selected.parquet minus sample_map n_cells (max |diff|)",
                 "value": float((cnt - sm["n_cells"].reindex(cnt.index)).abs().max()), "n": int(cnt.sum()),
                 "note": "; ".join(f"{k} {v}" for k, v in cnt.items())})
    # 5. within-plate basal p53 activity vs the panel's pooled-DMSO basal activity
    bt = pd.read_csv(os.path.join(tab, "b_baseline_per_line.csv"))
    r = stats.spearmanr(bt["basal_p53_within_plate"], bt["basal_p53_activity_log2_panel"], nan_policy="omit")
    rows.append({"check": "basal p53 activity: within-plate (this script) vs panel basal_p53_activity_log2 (Spearman)",
                 "value": float(r.statistic), "n": int(bt["basal_p53_within_plate"].notna().sum())})
    rows.append({"check": "lines TP53-WT / altered", "value": int((E.L["tp53_group"] == "WT").sum()),
                 "n": int((E.L["tp53_group"] == "altered").sum()), "note": "WT in value, altered in n"})
    rows.append({"check": "P53_ACTIVITY members used", "value": len(E.members), "n": len(E.members),
                 "note": ", ".join(E.members)})
    pd.DataFrame(rows).to_csv(os.path.join(tab, "checks.csv"), index=False)
    return pd.DataFrame(rows)


def headline(tab):
    """One table with the numbers the summary cites, each pointing at its source table."""
    out = []

    def add(section, claim, src, df, **cols):
        for _, r in df.iterrows():
            out.append({"section": section, "claim": claim, "source_table": src,
                        **{k: r[v] if v in r else np.nan for k, v in cols.items()},
                        "detail": "; ".join(f"{c}={r[c]}" for c in ("drug", "conc", "scope", "set", "wellset",
                                                                    "tp53_group", "predictor", "outcome", "x", "y",
                                                                    "adjustment", "subset", "test", "feature")
                                            if c in r and pd.notna(r[c]))})
    a = pd.read_csv(os.path.join(tab, "a_line_correlations.csv"))
    m = a[a["drug"].eq(IDA) & np.isclose(a["conc"], 5) & a["scope"].eq("all used wells")
          & a["predictor"].eq("TRIM72_r2") & a["outcome"].isin(["P53_SCORE", "MDM2", "CDKN1A"])]
    add("a", "idarubicin 5 uM: per-line TRIM72 induction vs p53-target induction", "a_line_correlations.csv", m,
        n="n_lines", estimate="rho", p="p_perm", q="q_bh")
    pl = pd.read_csv(os.path.join(tab, "a_pooled_over_drugdoses.csv"))
    m = pl[pl["predictor"].eq("TRIM72_r2") & pl["outcome"].isin(["P53_SCORE", "MDM2", "CDKN1A", "TP53"])
           & pl["set"].isin(["TRIM72 raisers", "p53 reference activators"])]
    add("a", "pooled over drug-doses (mean rho; one line permutation for all)", "a_pooled_over_drugdoses.csv", m,
        n="n_drugdoses", estimate="mean_rho", p="p_line_permutation", q="q_bh_within_set_group_adjustment")
    pw = pd.read_csv(os.path.join(tab, "a_pooled_WT_vs_altered.csv"))
    m = pw[pw["set"].eq("TRIM72 raisers") & pw["outcome"].isin(["P53_SCORE", "MDM2"])]
    add("a", "pooled TRIM72 raisers: WT minus altered (mean Fisher z), TP53-label permutation",
        "a_pooled_WT_vs_altered.csv", m, n="n_drugdoses", estimate="fisher_z_WT_minus_altered",
        p="p_tp53_label_permutation")
    rp = pd.read_csv(os.path.join(tab, "a_replicate_reliability.csv"))
    m = rp[rp["drug"].eq(IDA) & rp["feature"].isin(["TRIM72_r2", "P53_SCORE"])]
    add("a", "replicate reliability (plate 6 vs plate 14 well), per-line Spearman", "a_replicate_reliability.csv", m,
        n="n_lines", estimate="rho_replicate", p="p")
    cw = pd.read_csv(os.path.join(tab, "a_cross_well_correlations.csv"))
    m = cw[cw["drug"].eq(IDA) & cw["outcome"].eq("P53_SCORE")]
    add("a", "cross-well: TRIM72 from one 5 uM well vs P53 score from the other", "a_cross_well_correlations.csv",
        m, n="n_lines", estimate="rho_cross_mean")
    b = pd.read_csv(os.path.join(tab, "b_baseline_tests.csv"))
    m = b[(b["x"].eq("TRIM72_rel_reliable_plates") & b["y"].isin(["basal_p53_within_plate",
                                                                 "p53_responsiveness_log2_panel",
                                                                 "MDM2_rel_reliable_plates",
                                                                 "TP53_rel_reliable_plates"]))
          | b["test"].str.startswith("TRIM72 line ranking")]
    add("b", "untreated TRIM72 (plate-standardised) vs basal p53 activity / responsiveness", "b_baseline_tests.csv",
        m, n="n_lines", estimate="rho", p="p_perm", q="q_bh")
    c = pd.read_csv(os.path.join(tab, "c_correlations_across_drugdoses.csv"))
    m = c[c["subset"].isin(["all drug-doses", "p53 activators (P53_ACTIVITY z >= 3, FDR < 0.10)"])
          & c["y"].isin(["P53_ACTIVITY_z", "MDM2_z", "MDM2_z | P53_ACTIVITY_z", "p53_WT_minus_altered_z",
                         "PMAIP1_z", "CDKN1A_z"])]
    add("c", "across drug-doses: TRIM72 z vs p53 readouts (Spearman)", "c_correlations_across_drugdoses.csv", m,
        n="n_drugdoses", estimate="rho", p="p", ci_low="ci95_low_drug_bootstrap", ci_high="ci95_high_drug_bootstrap")
    e = pd.read_csv(os.path.join(tab, "c_trim72_up_vs_p53_activated_enrichment.csv"))
    add("c", "TRIM72 up vs p53 activated: odds ratio", "c_trim72_up_vs_p53_activated_enrichment.csv", e,
        estimate="odds_ratio", p="p")
    d = pd.read_csv(os.path.join(tab, "d_single_cell_meta_main.csv"))
    m = d[d["outcome"].isin(["P53_SCORE", "MDM2", "CDKN1A", "ATF3", "PMAIP1"])]
    add("d", "single cells: rate ratio of target counts, TRIM72-detected vs not (depth, S, G2M adjusted; "
        "random-effects over lines)", "d_single_cell_meta_main.csv", m, n="n_lines", estimate="rate_ratio", p="p",
        q="q_bh_p53_outcomes", control_percentile="percentile_among_controls",
        wt_minus_altered="WT_minus_altered_log_rate_ratio", p_wt_minus_altered="p_WT_minus_altered")
    H = pd.DataFrame(out)
    H.to_csv(os.path.join(tab, "key_results.csv"), index=False)
    return H


README_TABLES = """Tables of downstream_p53.py (re-created by: python3 downstream_p53.py). Associations only: Tahoe has no MG53
perturbation and measures mRNA; p53 activity = transcription of its target genes. r2 = the method-v3 corrected log2
effect per (well, cell line) (plate x line baseline -> composition shift -> position correction), per line = mean of
the drug-dose's used wells. P53_SCORE = mean r2 of the panel's 21 P53_ACTIVITY members the line expresses (per cell:
their summed counts). TP53 groups: the panel's (17 WT, 33 altered). rho = Spearman; 'partial' = covariate ranks
regressed out of both ranks. p_perm = two-sided permutation p (residual permutation). q_bh = Benjamini-Hochberg.

(a) across lines in the same wells
a_selected_drugdoses.csv          drug-doses tested: TRIM72 raisers (panel call up, z >= 4) and the panel's 10 p53
                                  reference activators; TRIM72 fold change / z, P53_ACTIVITY z, flags.
a_per_line_effects.csv            per drug-dose x line: TRIM72_r2, TRIM72_level (treated log2 CPM), P53_SCORE, CDKN1A,
                                  MDM2, BBC3, PMAIP1, TP53 r2, bg_abs_r2 (mean |r2| of the non-p53 panel genes),
                                  atlas_beta (DD_beta), atlas_A (DD_A, relative abundance; < 0 = depleted),
                                  TRIM72_base (log2 untreated DMSO CPM of TRIM72, plates pooled).
a_line_correlations.csv           every drug-dose x scope (all used wells / one plate's well) x TP53 group x predictor
                                  (TRIM72_r2, TRIM72_level) x outcome x adjustment (none; beta+A = atlas DD_beta and
                                  DD_A; bg|r2|+A = mean |r2| of non-p53 panel genes and DD_A; beta+A+TRIM72base =
                                  beta+A and the untreated TRIM72 level): n_lines, rho, p (t),
                                  p_perm, q_bh (within scope type x predictor x adjustment x group).
a_line_correlations_WT_vs_altered.csv  the same test in WT vs altered lines: Fisher z difference and p.
a_reference_background_genes.csv  TRIM72_r2 vs each p53 outcome next to TRIM72_r2 vs every non-p53 panel gene
                                  (median, 5th / 95th percentile, percentile of the p53 outcome among them).
a_replicate_reliability.csv       2-well drug-doses: per-line agreement of the plate-6 and plate-14 wells (Spearman).
a_cross_well_correlations.csv     2-well drug-doses: TRIM72_r2 from one well vs outcome r2 from the other well (shared
                                  per-profile noise cannot create these), next to the same-well values.
a_pooled_over_drugdoses.csv       mean rho over a set of drug-doses (Fisher z average) with ONE line-label permutation
                                  applied to all drug-doses at once (they share lines and wells); q within set x group x
                                  adjustment.
a_pooled_WT_vs_altered.csv        the pooled TRIM72_r2 correlations, WT minus altered (mean Fisher z difference), p from
                                  permuting the TP53 labels over lines (residuals recomputed in the permuted groups).

(b) untreated (DMSO wells)
b_baseline_per_line.csv           per line: TRIM72_rel_* = log2(observed / expected counts), expected = the plate's
                                  median expressing line's CPM x the profile's UMIs, summed over the plates of the set
                                  (reliable plates; high-baseline plates 1-3, 14; low-baseline plates 4-12), NaN when
                                  expected < 2 counts; basal_p53_within_plate (mean over the expressed P53_ACTIVITY
                                  members of the same standardised level), the panel's basal_p53_activity_log2 and
                                  p53_responsiveness_log2, CDKN1A/MDM2/BBC3/PMAIP1/TP53 standardised levels.
b_baseline_per_plate_line.csv     the same per plate (long).
b_baseline_tests.csv              Spearman (permutation p, within-organ rho / p as tahoe_gene_panel.spearman_within),
                                  q_bh over the TRIM72-vs-p53 tests; the high- vs low-plate ranking check; Mann-Whitney
                                  of the TRIM72 level WT vs altered (rho column = AUC).
b_baseline_per_plate_correlations.csv  per plate and group: TRIM72 vs within-plate basal p53 (the plates share lines:
                                  not independent replicates).

(c) across drug-doses (all 1,132)
c_drugdose_table.csv              per drug-dose: TRIM72 fold / z / FDR / call, P53_ACTIVITY fold / z / FDR, the panel's
                                  WT-minus-altered p53 contrast (z, log2, pattern), z of every p53 target, activity
                                  covariates (atlas n_sig_genes, cells, S / G2M z, ISR / NRF2 / UPR / heat-shock /
                                  NF-kB z), DNA-damaging (the panel's definition), category.
c_correlations_across_drugdoses.csv  Spearman of TRIM72 z with p53 readouts, raw and with activity partialled out, in
                                  subsets; 95% CI by resampling whole drugs (all doses together); 'MDM2_z |
                                  P53_ACTIVITY_z' = MDM2 beyond the p53 score; within-plate means.
c_trim72_up_vs_p53_activated_enrichment.csv  2x2: TRIM72 call up vs P53_ACTIVITY z >= 3 & FDR < 0.10 (Fisher;
                                  Mantel-Haenszel over deciles of drug activity).
c_category_summary.csv / c_categories_drugdoses.csv  drug-doses that raise TRIM72 with / without p53 activation
                                  (P53_ACTIVITY z < 2) and p53 activators without TRIM72 (TRIM72 z < 2): what each p53
                                  target does there.

(d) single cells (idarubicin 5 uM wells smp_2010 / smp_2778; DMSO wells of plates 6 and 14)
d_single_cell_line_description.csv  per well set x line: cells, TRIM72-detected cells (>= 1 UMI), median UMIs of
                                  detected / not detected cells, S / G2M score differences.
d_single_cell_per_line_fits.csv.gz  per well set x line x outcome: quasi-Poisson GLM log rate ratio of the outcome's
                                  counts for TRIM72-detected cells (offset log UMIs; covariates log UMIs, log S-phase
                                  and G2M module fraction, well indicator for pooled wells), SE, dispersion, and the
                                  unadjusted log rate ratio. Lines need >= 50 cells, >= 5 detected and >= 5 not; outcomes
                                  >= 20 counts in the line and expressed by it.
d_single_cell_meta_all_outcomes.csv  DerSimonian-Laird random-effects over lines per well set x TP53 group x outcome
                                  (p53 outcomes and every non-p53 panel gene = negative controls); percentile of each
                                  outcome among the controls; q_bh over the p53 outcomes.
d_single_cell_meta_main.csv       the p53 outcomes (P53_SCORE, CDKN1A, MDM2, BBC3, PMAIP1, TP53, ATF3) with the WT-minus-
                                  altered difference.
d_single_cell_mh_depth_strata.csv  Mantel-Haenszel rate ratio within UMI-depth quintiles per line; median over lines,
                                  Wilcoxon signed-rank p.

checks.csv                        agreement with the panel's tables and the earlier per-line TRIM72 table.
key_results.csv                   the numbers the summary cites, each with its source table.
"""


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--data", default=os.environ.get("MG53_DATA") or os.environ.get("TAHOE_DATA") or os.path.expanduser("~/Tahoe-100M"))
    ap.add_argument("--recompute", action="store_true", help="rebuild the caches")
    ap.add_argument("--perm", type=int, default=5000, help="permutations per test")
    ap.add_argument("--boot", type=int, default=1000, help="drug-level bootstrap resamples")
    a = ap.parse_args()
    t0 = time.time()
    cdir, tab = os.path.join(os.environ.get("MG53_OUT") or HERE, "cache"), os.path.join(os.environ.get("MG53_OUT") or HERE, "tables")
    os.makedirs(cdir, exist_ok=True)
    os.makedirs(tab, exist_ok=True)
    if a.recompute or not all(os.path.exists(os.path.join(cdir, f)) for f in
                              ("effects.npz", "wells.csv", "lines.csv", "meta.json", "drug_effects_all_genes.csv.gz")):
        build_effects_cache(a.data, cdir)
    if a.recompute or not os.path.exists(os.path.join(cdir, "cells_selected.parquet")):
        build_cells_cache(a.data, cdir)
    E = Eff(cdir)
    A = Atlas(a.data)
    analysis_a(E, A, os.path.join(a.data, "gene_panel", "results"), tab, a.perm)
    analysis_b(E, a.data, tab, a.perm)
    analysis_c(E, a.data, cdir, tab, a.boot)
    analysis_d(E, cdir, tab)
    ck = checks(E, a.data, cdir, tab)
    headline(tab)
    with open(os.path.join(tab, "README_tables.txt"), "w", encoding="utf-8") as fh:
        fh.write(README_TABLES)
    print(ck.to_string(index=False))
    try:
        import resource
        peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6
    except Exception:  # noqa: BLE001
        peak = float("nan")
    log(f"tables written to {tab}; peak RSS {peak:.2f} GB; wall {time.time() - t0:.0f} s")


if __name__ == "__main__":
    main()
