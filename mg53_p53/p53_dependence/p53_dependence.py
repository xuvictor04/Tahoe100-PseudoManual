#!/usr/bin/env python3
"""Is TRIM72 (MG53) induction p53-dependent?  Tahoe-100M, method-v3 corrected effects per (well, cell line).

What it does (all numbers are recomputed from the gene panel's extract; nothing under the data folder is written):
  1. Runs the gene panel's own setup in memory (tahoe_gene_panel.load / step_baseline / step_expression /
     step_prepare, tahoe_mtap_gankyrin.well_context) and T.expression_effects for every panel gene, keeping the
     per (well, line) corrected log2 effect r2, the per-line z (z_line), log2 CPM y and the plate x line baseline.
     Cached in cache/ (rebuilt with --recompute or when missing).
  2. For the strong TRIM72 raisers and the strongest p53 activators (every dose of each drug), compares TP53
     wild-type (WT, 17) with TP53-altered (33) lines IN THE SAME WELLS: difference of medians, bootstrap CI,
     Mann-Whitney, label permutation (also stratified by organ), per plate when a drug-dose has 2 wells; the same for
     the canonical p53 targets CDKN1A, MDM2, BBC3, TP53I3, FDXR and the panel's 21-gene P53_ACTIVITY score
     (positive controls: they show the power of the test).
  3. Uses functional p53 responsiveness (the panel's genotype-blind measure, recomputed leaving out the wells of the
     drug under test) as a continuous covariate, with and without the line's untreated TRIM72 level.
  4. Splits the altered lines into missense vs truncating / splice / deletion (likely null).
  5. Across all 1,132 drug-doses: the WT-minus-altered difference per well (per-plate robust z, Stouffer over the
     used wells) for TRIM72, the controls and the P53 score; p53 activators that do / do not damage DNA.
  6. 'Does TRIM72 behave like a p53 target?': four metrics for every panel gene (p53-score members, other p53
     targets, TRIM72, the rest) and where TRIM72 falls.

    python3 p53_dependence.py [--data DIR (default $MG53_DATA, $TAHOE_DATA or ~/Tahoe-100M)] [--recompute] [--perm 10000]

Outputs (this script's folder, tables/; log2 effects are the method-v3 corrected r2, per line = mean of used wells):
  key_results.csv                         headline rows: strongest TRIM72 raisers + selinexor, TRIM72 next to the
                                          controls, per scope (both wells, each well alone)
  wt_vs_altered_selected_long.csv         every selected drug-dose x scope x gene: medians WT / altered / missense /
                                          truncating, difference of medians, bootstrap CI, Mann-Whitney, permutation
                                          (also within organ), critical |diff| at alpha 0.05, Wilcoxon 'altered > 0',
                                          responsiveness Spearman / partial / OLS, BH FDR within gene
  wt_vs_altered_selected_wide.csv         one row per selected drug-dose: TRIM72 vs CDKN1A, MDM2, P53 score
  per_line_effects_selected.csv           per line r2 and z_line (all genes: mean of used wells; TRIM72: also per well)
  selected_drugdoses.csv                  the drug-doses tested and why (raiser / p53 activator / screen hit)
  lines_tp53_status.csv                   TP53 group / class, functional responsiveness, TRIM72 untreated level
  trim72_levels_by_tp53_group.csv         TRIM72 CPM untreated (plate baseline) and treated per group, per well
  trim72_pooled_fold_change_no_pseudocount.csv  summed-count CPM ratios per group (no pseudocount), permutation
  trim72_inducibility_pooled_sets.csv     per-line inducibility pooled over TRIM72-raising drug-doses
  replicate_wells_per_line_agreement.csv  plate 6 vs plate 14 (and same-plate duplicates): line-to-line agreement
  screen_all_drugdoses_wt_minus_altered.csv  all 1,132 drug-doses: per-well WT-minus-altered, Stouffer z, BH FDR
  screen_summary_by_gene.csv              per gene: screen hits by direction, spread of z, Spearman with P53 score
  p53_activators_dna_damage_vs_not.csv / p53_activators_summary.csv   strong p53 activators, DNA-damaging or not
  target_likeness_by_gene.csv / target_likeness_summary.csv           does TRIM72 behave like a p53 target?
  checks.csv                              agreement with the panel's own tables and the earlier per-line table
Associations only: Tahoe has no MG53 perturbation, so nothing here is causal for MG53 -> p53.
"""
import argparse
import contextlib
import json
import math
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
CONTROLS = ["CDKN1A", "MDM2", "BBC3", "TP53I3", "FDXR"]          # canonical p53 targets (positive controls)
EXTRA = ["ATF3", "PMAIP1", "TP53"]                                # descriptive companions (ATF3 / PMAIP1 co-regulated)
SCORE = "P53_SCORE"                                               # the panel's 21-gene P53_ACTIVITY, per line
OTHER_P53_TARGETS = ["CCNG1", "BTG2", "TIGAR", "TNFRSF10B", "GADD45A", "SESN2", "PMAIP1"]   # left out of the score
TRIM72_RAISERS = ["Idarubicin", "Homoharringtonine", "Auranofin", "Dinaciclib", "Epirubicin", "Doxorubicin",
                  "Topotecan", "Mitoxantrone"]
FAMILY = {"Harringtonine": "harringtonines", "Homoharringtonine": "harringtonines"}   # leave-drug-out families
MIN_GROUP = 5            # a well's WT-minus-altered difference needs >= this many lines of each group
TOP_P53 = 20             # target-likeness: the drug-doses with the strongest WT-selective P53-score induction
SEED = 20261022


@contextlib.contextmanager
def quiet():
    """Silence the 'mean / median of empty slice' warnings of all-NaN rows (they give NaN, as intended)."""
    with warnings.catch_warnings(), np.errstate(invalid="ignore", divide="ignore"):
        warnings.simplefilter("ignore", RuntimeWarning)
        yield


# ============================================================================= setup (read-only)
def read_only_discover(data_dir, out_dir, refresh=False):
    """T.discover without the write: the panel's file index is read, never rebuilt (nothing under the data folder
    is written by this script)."""
    with open(os.path.join(out_dir, "file_index.json"), encoding="utf-8") as fh:
        return json.load(fh)


def panel_setup(data):
    T.discover = read_only_discover
    args = argparse.Namespace(command="analyze", data=data, out=os.path.join(data, "gene_panel"), workers=0,
                              batch_size=20000, limit_files=0, layout=None, min_cells=T.MIN_CELLS, reindex=False,
                              genes="", mtap_null=None, tp53_wt=None, tp53_altered=None, prior="none",
                              unreliable_plates=None, atlas=None)
    S = P.Run(args)
    S.R = tempfile.mkdtemp()           # the panel's side tables of the setup steps land here, then are removed
    P.load(S)
    P.step_baseline(S)
    P.step_expression(S)
    P.step_prepare(S)
    S.ctx = T.well_context(S.wl, S.sm, S.cols, S.M)
    return S


def build_cache(data, cdir):
    t0 = time.time()
    S = panel_setup(data)
    order, todo = P.effect_genes(S)
    genes = [g for g in todo if g not in P.MODULES]
    samples = S.sm["sample"].astype(str).tolist()
    lines = list(S.base.index)
    focus = [GENE] + CONTROLS + EXTRA
    R2 = np.full((len(genes), len(samples), len(lines)), np.nan, dtype=np.float32)
    ZL = np.full_like(R2, np.nan)
    focus_y, focus_base, focus_cnt, res_all = {}, {}, {}, []
    for k, g in enumerate(genes):
        res, W, d, cal = T.expression_effects(S.wl, S.sm, g, P.gene_exclusions(S, g), S.ctx, S.drugs, method=S.M)
        R2[k] = d.pivot(index="sample", columns="cell_line_id", values="r2").reindex(index=samples, columns=lines)
        ZL[k] = d.pivot(index="sample", columns="cell_line_id", values="z_line").reindex(index=samples, columns=lines)
        if g in focus:
            focus_y[g] = d.pivot(index="sample", columns="cell_line_id", values="y").reindex(index=samples,
                                                                                            columns=lines)
            focus_base[g] = (d.assign(b=d["y"] - d["r1"]).pivot(index="sample", columns="cell_line_id", values="b")
                             .reindex(index=samples, columns=lines))
            focus_cnt[g] = d.pivot(index="sample", columns="cell_line_id", values=g).reindex(index=samples,
                                                                                            columns=lines)
            if g == GENE:                  # library size per (well, line) profile: the same for every gene
                focus_cnt["total_counts"] = d.pivot(index="sample", columns="cell_line_id",
                                                    values="total_counts").reindex(index=samples, columns=lines)
        keep = ["drug", "conc", "call", "fold_change", "log2FC_corrected", "z_corrected", "fdr_up", "fdr_down",
                "n_lines", "n_lines_up", "n_lines_down", "flags", "plates", "wells"]
        res_all.append(res[[c for c in keep if c in res]].assign(gene=g))
        if k % 20 == 0:
            print(f"  {k + 1}/{len(genes)} genes ({time.time() - t0:.0f} s)", flush=True)
    os.makedirs(cdir, exist_ok=True)
    np.savez_compressed(os.path.join(cdir, "r2_zline.npz"), R2=R2, ZL=ZL, genes=np.array(genes),
                        samples=np.array(samples), lines=np.array(lines))
    for name, dct in (("y", focus_y), ("plate_baseline_y", focus_base), ("counts", focus_cnt)):
        parts = []
        for g, m in dct.items():
            arr = m.to_numpy(dtype=float)
            ii, jj = np.where(np.isfinite(arr))
            parts.append(pd.DataFrame({"gene": g, "sample": np.asarray(samples)[ii],
                                       "cell_line_id": np.asarray(lines)[jj], "v": arr[ii, jj]}))
        pd.concat(parts, ignore_index=True).to_parquet(os.path.join(cdir, f"focus_{name}.parquet"), index=False)
    pd.concat(res_all, ignore_index=True).to_csv(os.path.join(cdir, "drug_effects_all_genes.csv.gz"), index=False)
    # wells: used (the drug-dose's wells on reliable plates, as the method) and reference (drug wells, reliable)
    W = T.wells_of(S.sm).reindex(samples)
    Wd = W.loc[~W["is_dmso"]].copy()
    Wd["dose"] = T.dose_key(Wd)
    W["dose"] = Wd["dose"].reindex(W.index)
    W["used"] = T.used_wells(Wd).reindex(W.index).fillna(False).astype(bool)
    W["reference"] = T.reference_wells(W)
    W["n_cells"] = S.sm.set_index("sample")["n_cells"].reindex(W.index)
    W.rename_axis("sample").reset_index().to_csv(os.path.join(cdir, "wells.csv"), index=False)
    # lines: TP53 annotation, organ, expressed flags and untreated levels of the focus genes
    L = pd.DataFrame({"cell_name": S.name, "organ": S.base["Organ"], "tp53_status": S.base["tp53_status"],
                      "tp53_group": S.base["tp53_group"], "tp53_changes": S.base["tp53_changes"]})
    L = pd.concat([L] + [pd.DataFrame({f"expr_{g}": S.E[g].reindex(L.index) if g in S.E else False,
                                       f"cpm_dmso_{g}": S.Cd[g].reindex(L.index) if g in S.Cd else np.nan})
                         for g in genes], axis=1)
    L.index.name = "cell_line_id"
    L.to_csv(os.path.join(cdir, "lines.csv"))
    S.drugs.reset_index().to_csv(os.path.join(cdir, "drugs.csv"), index=False)
    dna = P.find_drugs(set(S.sm.loc[~S.sm["is_dmso"], "drug"]), S.drugs, P.DNA_DAMAGE)
    meta = {"genes": genes, "p53_score_members": [g for g in P.P53_ACTIVITY
                                                 if g in genes and S.status.get(g) == "testable"],
            "dna_damage_drugs": dna, "status": {g: S.status.get(g) for g in genes},
            "expressed_threshold_cpm_TRIM72": float(S.thr[GENE]), "unreliable_plates": list(S.unreliable),
            "plate_factor_note": S.plate_scale_note, "composition": S.comp_note, "min_cells": T.MIN_CELLS,
            "built_seconds": round(time.time() - t0, 1)}
    with open(os.path.join(cdir, "meta.json"), "w", encoding="utf-8") as fh:
        json.dump(meta, fh, indent=1)
    import shutil
    shutil.rmtree(S.R, ignore_errors=True)
    print(f"cache built in {time.time() - t0:.0f} s", flush=True)


# ============================================================================= cache access
class Data:
    def __init__(self, cdir, data):
        z = np.load(os.path.join(cdir, "r2_zline.npz"), allow_pickle=False)
        self.genes = [str(x) for x in z["genes"]]
        self.samples = [str(x) for x in z["samples"]]
        self.lines = [str(x) for x in z["lines"]]
        self.R2, self.ZL = z["R2"].astype(float), z["ZL"].astype(float)
        self.gi = {g: i for i, g in enumerate(self.genes)}
        self.W = pd.read_csv(os.path.join(cdir, "wells.csv"), dtype={"sample": str, "plate": str}).set_index("sample")
        self.L = pd.read_csv(os.path.join(cdir, "lines.csv")).set_index("cell_line_id").reindex(self.lines).copy()
        self.meta = json.load(open(os.path.join(cdir, "meta.json"), encoding="utf-8"))
        self.res = pd.read_csv(os.path.join(cdir, "drug_effects_all_genes.csv.gz"))
        self.drugs = pd.read_csv(os.path.join(cdir, "drugs.csv")).set_index("drug")
        self.focus = {n: pd.read_parquet(os.path.join(cdir, f"focus_{n}.parquet"))
                      for n in ("y", "plate_baseline_y", "counts")}
        self.members = list(self.meta["p53_score_members"])
        # the panel's P53_ACTIVITY per (well, line): nan-mean of the expressed members' r2 (tahoe_gene_panel.p53_matrix)
        stack = self.R2[[self.gi[g] for g in self.members]]
        with quiet():
            self.P53 = np.nanmean(stack, axis=0)
        self.stack_members = stack
        res_dir = os.path.join(data, "gene_panel", "results")
        self.func = pd.read_csv(os.path.join(res_dir, "p53_functional_status.csv")).set_index("cell_line_id")
        self.ref_doses = pd.read_csv(os.path.join(res_dir, "p53_reference_doses.csv"))
        self.p53wt = pd.read_csv(os.path.join(res_dir, "p53_wt_vs_altered.csv"))
        sc = pd.read_csv(os.path.join(res_dir, "pathway_scores_by_dose.csv"))
        self.p53score = sc[sc["score"] == "P53_ACTIVITY"].copy()
        self.panel_trim72 = pd.read_csv(os.path.join(res_dir, "TRIM72_drug_effects_by_dose.csv"))

    def mat(self, g):
        """(samples x lines) r2 of a gene, or of the P53 score (SCORE), or the score without one member."""
        if g == SCORE:
            return self.P53
        if g.startswith(SCORE + "-"):
            drop = g.split("-", 1)[1]
            keep = [i for i, m in enumerate(self.members) if m != drop]
            with quiet():
                return np.nanmean(self.stack_members[keep], axis=0)
        return self.R2[self.gi[g]]

    def zl(self, g):
        return None if g.startswith(SCORE) else self.ZL[self.gi[g]]


# ============================================================================= line classes
def tp53_class(group, changes):
    if group == "WT":
        return "WT"
    ch = str(changes or "")
    trunc = any(k in ch for k in ("fs", "*", "Splice", "DEL", "+")) or "T125T" in ch
    return "altered: truncating / splice / deletion" if trunc else "altered: missense only"


# ============================================================================= statistics
def diff_medians(v, lab):
    a, b = v[lab == 1], v[lab == 0]
    return float(np.median(a) - np.median(b))


def perm_medians(v, lab, B, rng, strata=None):
    """Two-sided permutation p of the difference of medians (WT - altered); labels shuffled over lines (within
    strata when given). Also the 95th percentile of |null difference|: the critical |difference| at alpha 0.05, i.e.
    the smallest observed difference that this test calls significant (a difference must be larger still to be
    found with high power)."""
    obs = diff_medians(v, lab)
    n1 = int(lab.sum())
    if strata is None:
        idx = np.argsort(rng.random((B, len(v))), axis=1)          # a random relabelling per row
    else:
        Lb = np.tile(lab, (B, 1))
        for s in np.unique(strata):
            ii = np.where(strata == s)[0]
            if len(ii) > 1:
                Lb[:, ii] = rng.permuted(Lb[:, ii], axis=1)
        idx = np.argsort(-Lb, axis=1, kind="stable")                # the n1 'WT' positions first
    Vs = v[idx]
    null = np.median(Vs[:, :n1], axis=1) - np.median(Vs[:, n1:], axis=1)
    p = (1 + np.sum(np.abs(null) >= abs(obs) - 1e-12)) / (1 + len(null))
    return float(p), float(np.quantile(np.abs(null), 0.95))


def boot_ci(v, lab, B, rng):
    a, b = v[lab == 1], v[lab == 0]
    ia = rng.integers(0, len(a), (B, len(a)))
    ib = rng.integers(0, len(b), (B, len(b)))
    d = np.median(a[ia], axis=1) - np.median(b[ib], axis=1)
    return float(np.quantile(d, 0.025)), float(np.quantile(d, 0.975))


def partial_spearman(x, y, z):
    """Spearman of x and y with z (rank) projected out of both; p from t with n - 3 df."""
    ok = np.isfinite(x) & np.isfinite(y) & np.isfinite(z)
    n = int(ok.sum())
    if n < 6:
        return np.nan, np.nan, n
    rx, ry, rz = (stats.rankdata(a[ok]) for a in (x, y, z))
    Z = np.column_stack([np.ones(n), rz])
    ex = rx - Z @ np.linalg.lstsq(Z, rx, rcond=None)[0]
    ey = ry - Z @ np.linalg.lstsq(Z, ry, rcond=None)[0]
    r = float(np.corrcoef(ex, ey)[0, 1])
    t = r * math.sqrt((n - 3) / max(1e-12, 1 - r * r))
    return r, float(2 * stats.t.sf(abs(t), n - 3)), n


def ols(y, X, names):
    """OLS with intercept: coefficient, SE and two-sided p of each named column."""
    ok = np.isfinite(y) & np.all(np.isfinite(X), axis=1)
    y, X = y[ok], X[ok]
    n, k = len(y), X.shape[1] + 1
    if n <= k + 2:
        return {f"{nm}_{s}": np.nan for nm in names for s in ("coef", "se", "p")}
    A = np.column_stack([np.ones(n), X])
    beta, *_ = np.linalg.lstsq(A, y, rcond=None)
    resid = y - A @ beta
    s2 = float(resid @ resid) / (n - k)
    cov = s2 * np.linalg.pinv(A.T @ A)
    out = {}
    for j, nm in enumerate(names, start=1):
        se = math.sqrt(max(cov[j, j], 0))
        out[f"{nm}_coef"], out[f"{nm}_se"] = float(beta[j]), se
        out[f"{nm}_p"] = float(2 * stats.t.sf(abs(beta[j] / se), n - k)) if se > 0 else np.nan
    out["ols_n"] = n
    return out


def robust_cs(v):
    v = v[np.isfinite(v)]
    if len(v) < 5:
        return np.nan, np.nan
    c = float(np.median(v))
    s = 1.4826 * float(np.median(np.abs(v - c)))
    return c, (s if s > 0 else float(np.std(v)) or np.nan)


# ============================================================================= drug-dose selection
def select_drugdoses(D, screen):
    """Every dose of: the named TRIM72 raisers; the p53 activators (the panel's reference doses, all-line P53 score
    z >= 5 with FDR < 0.10, or 'WT induction' with z_wt_more >= 5 and FDR < 0.10); and the drugs with a TRIM72
    WT-minus-altered difference at FDR < 0.10 in the screen of all drug-doses (so each screen hit gets the per-line
    tests too)."""
    dd = D.W.loc[~D.W["is_dmso"].astype(bool), ["drug", "conc"]].drop_duplicates()
    names = sorted(dd["drug"].unique())
    raisers = {d for d in names if any(d.startswith(p) for p in TRIM72_RAISERS)}
    hits = set(screen.loc[screen["TRIM72_fdr"] < 0.10, "drug"])
    act = set(D.ref_doses["drug"])
    sc = D.p53score
    act |= set(sc.loc[(sc["z"] >= 5) & (sc["fdr_up"] < 0.10), "drug"])
    w = D.p53wt
    act |= set(w.loc[(w["pattern"] == "WT induction") & (w["fdr"] < 0.10) & (w["z_wt_more"] >= 5), "drug"])
    pick = dd[dd["drug"].isin(raisers | act | hits)].copy()
    pick["role"] = ["TRIM72 raiser + p53 activator" if d in raisers and d in act else
                    "TRIM72 raiser" if d in raisers else "p53 activator" if d in act else
                    "TRIM72 WT-vs-altered screen hit" for d in pick["drug"]]
    pick["screen_hit"] = pick["drug"].isin(hits)
    dna = set(D.meta["dna_damage_drugs"])
    pick["dna_damaging"] = pick["drug"].isin(dna)
    return pick.sort_values(["role", "drug", "conc"]).reset_index(drop=True)


def family(drug):
    b = T.salt_base(drug)
    return FAMILY.get(b, b)


# ============================================================================= responsiveness (leave drug out)
def responsiveness(D, leave_out_family=None):
    """The panel's p53 responsiveness: per line, the mean P53 score over the used wells of the reference drug-doses
    (p53_reference_doses.csv); optionally without the wells of one drug family (so a drug's own wells never enter
    the covariate it is tested against)."""
    keys = set(zip(D.ref_doses["drug"], D.ref_doses["conc"].astype(float)))
    W = D.W
    sel = [i for i, (s, d, c, u) in enumerate(zip(W.index, W["drug"], W["conc"].astype(float), W["used"]))
           if (d, c) in keys and u and not W["is_dmso"].iloc[i]
           and (leave_out_family is None or family(d) != leave_out_family)]
    M = D.P53[sel]
    with quiet():
        return pd.Series(np.nanmean(M, axis=0), index=D.lines), len(sel)


# ============================================================================= per drug-dose WT vs altered
def per_line_values(D, g, wells):
    """Per line: the mean over the given wells of r2 (and z_line), as the method's per_line table."""
    idx = [D.W.index.get_loc(s) for s in wells]
    M = D.mat(g)[idx]
    with quiet():
        r2 = np.nanmean(M, axis=0)
        z = D.zl(g)
        zl = np.nanmean(z[idx], axis=0) if z is not None else np.full(len(D.lines), np.nan)
    return r2, zl


def compare(v, lab, cls, organ, B, rng):
    ok = np.isfinite(v)
    v, lab, cls, organ = v[ok], lab[ok], cls[ok], organ[ok]
    n1, n0 = int((lab == 1).sum()), int((lab == 0).sum())
    out = {"n_wt": n1, "n_altered": n0}
    if n1 < 3 or n0 < 3:
        return out
    out["median_all_log2"] = float(np.median(v))
    out["median_wt_log2"] = float(np.median(v[lab == 1]))
    out["median_altered_log2"] = float(np.median(v[lab == 0]))
    out["diff_wt_minus_altered_log2"] = diff_medians(v, lab)
    out["ci95_low"], out["ci95_high"] = boot_ci(v, lab, B, rng)
    u = stats.mannwhitneyu(v[lab == 1], v[lab == 0], alternative="two-sided")
    out["auc_wt_gt_altered"] = float(u.statistic / (n1 * n0))
    out["p_mannwhitney"] = float(u.pvalue)
    out["p_perm"], out["critical_abs_diff_p05"] = perm_medians(v, lab, B, rng)
    out["p_perm_within_organ"], _ = perm_medians(v, lab, B, rng, strata=organ)
    alt = v[lab == 0]
    out["p_altered_lines_above_0"] = float(stats.wilcoxon(alt, alternative="greater").pvalue) \
        if np.any(alt != 0) else np.nan
    for name, key in (("missense", "altered: missense only"), ("truncating", "altered: truncating / splice / deletion")):
        vv = v[cls == key]
        out[f"n_{name}"] = len(vv)
        out[f"median_{name}_log2"] = float(np.median(vv)) if len(vv) else np.nan
        out[f"p_{name}_vs_wt"] = float(stats.mannwhitneyu(v[lab == 1], vv, alternative="two-sided").pvalue) \
            if len(vv) >= 3 else np.nan
    return out


def wt_vs_altered_selected(D, pick, genes, B, rng):
    lab = (D.L["tp53_group"] == "WT").astype(int).to_numpy()
    cls = D.L["tp53_class"].to_numpy()
    organ = D.L["organ"].fillna("").astype(str).to_numpy()
    resp_full, _ = responsiveness(D)
    # the line's untreated level (log2 DMSO CPM; for the score: its basal p53 activity), a covariate: lines with a
    # low untreated level can show larger fold changes
    base = {g: np.log2(D.L[f"cpm_dmso_{g}"].astype(float).to_numpy() + 0.1) if f"cpm_dmso_{g}" in D.L
            else D.func["basal_p53_activity_log2"].reindex(D.lines).to_numpy(dtype=float) for g in genes}
    rows, longrows = [], []
    Wd = D.W.loc[~D.W["is_dmso"].astype(bool)]
    for _, pr in pick.iterrows():
        ww = Wd[(Wd["drug"] == pr["drug"]) & np.isclose(Wd["conc"].astype(float), float(pr["conc"]))]
        used = list(ww.index[ww["used"].astype(bool)])
        scopes = [("mean of used wells", used)]
        if len(used) > 1:
            scopes += [(f"{ww.at[s, 'plate']} {ww.at[s, 'well']} only", [s]) for s in used]
        resp_ldo, n_ref = responsiveness(D, family(pr["drug"]))
        for scope, wells in scopes:
            for g in genes:
                v, zl = per_line_values(D, g, wells)
                r = {"drug": pr["drug"], "conc": pr["conc"], "role": pr["role"], "dna_damaging": pr["dna_damaging"],
                     "scope": scope, "plates": ",".join(sorted({str(D.W.at[s, 'plate']) for s in wells})),
                     "gene": g}
                r.update(compare(v, lab, cls, organ, B, rng))
                # functional p53 status (responsiveness, leave-drug-out) as a continuous covariate
                ok = np.isfinite(v) & np.isfinite(resp_ldo.to_numpy())
                if ok.sum() >= 6:
                    rho, p = stats.spearmanr(v[ok], resp_ldo.to_numpy()[ok])
                    r["spearman_vs_responsiveness_ldo"], r["p_spearman_responsiveness"] = float(rho), float(p)
                    pr_, pp_, _n = partial_spearman(v, resp_ldo.to_numpy(), base[g])
                    r["partial_spearman_given_baseline"], r["p_partial"] = pr_, pp_
                    o = ols(v, np.column_stack([resp_ldo.to_numpy(), base[g]]), ["responsiveness", "baseline"])
                    r["slope_per_log2_responsiveness"], r["p_slope_responsiveness"] = \
                        o.get("responsiveness_coef"), o.get("responsiveness_p")
                    o2 = ols(v, np.column_stack([lab.astype(float), base[g]]), ["wt", "baseline"])
                    r["wt_minus_altered_adjusted_for_baseline"], r["p_adjusted"] = o2.get("wt_coef"), o2.get("wt_p")
                    r["baseline_slope"] = o2.get("baseline_coef")
                if g != SCORE:     # across lines, the same wells: does the gene follow the line's p53 response?
                    sv, _ = per_line_values(D, SCORE, wells)
                    ok2 = np.isfinite(v) & np.isfinite(sv)
                    if ok2.sum() >= 6:
                        rho2, p2 = stats.spearmanr(v[ok2], sv[ok2])
                        r["spearman_vs_p53score_same_wells"], r["p_spearman_p53score"] = float(rho2), float(p2)
                r["n_reference_wells_ldo"] = n_ref
                up = (zl > T.Z_LINE) & (v > T.LFC_MIN)
                r["frac_wt_lines_up"] = float(np.mean(up[(lab == 1) & np.isfinite(v)])) if g != SCORE else np.nan
                r["frac_altered_lines_up"] = float(np.mean(up[(lab == 0) & np.isfinite(v)])) if g != SCORE else np.nan
                rows.append(r)
                if scope == "mean of used wells" or g == GENE:
                    for j, c in enumerate(D.lines):
                        if np.isfinite(v[j]):
                            longrows.append({"drug": pr["drug"], "conc": pr["conc"], "scope": scope, "gene": g,
                                             "cell_line_id": c, "cell_name": D.L.at[c, "cell_name"],
                                             "organ": D.L.at[c, "organ"], "tp53_group": D.L.at[c, "tp53_group"],
                                             "tp53_class": D.L.at[c, "tp53_class"],
                                             "responsiveness_panel": resp_full.iloc[j],
                                             "responsiveness_leave_drug_out": resp_ldo.iloc[j],
                                             "log2FC_corrected": v[j], "fold_change": 2 ** v[j],
                                             "z_line": zl[j]})
    res = pd.DataFrame(rows)
    # BH within gene over the a-priori drug-doses (the 'mean of used wells' rows), for both tests
    res["fdr_perm"] = np.nan
    res["fdr_mannwhitney"] = np.nan
    # (the drugs added only as screen hits are left out: they were picked for their TRIM72 difference, so their
    # multiple testing is the screen's FDR over all drug-doses)
    for g in genes:
        m = (res["gene"] == g) & (res["scope"] == "mean of used wells") & \
            (res["role"] != "TRIM72 WT-vs-altered screen hit")
        res.loc[m, "fdr_perm"] = T.bh(res.loc[m, "p_perm"].to_numpy())
        res.loc[m, "fdr_mannwhitney"] = T.bh(res.loc[m, "p_mannwhitney"].to_numpy())
    return res, pd.DataFrame(longrows)


def trim72_levels(D, pick):
    """Untreated (plate baseline) and treated TRIM72 CPM per TP53 group in the same wells: the induced level, which
    does not depend on the plate's baseline (the TRIM72 plate batch inflates fold changes on plates 4-13)."""
    y = D.focus["y"]
    y = y[y["gene"] == GENE].pivot(index="sample", columns="cell_line_id", values="v")
    b = D.focus["plate_baseline_y"]
    b = b[b["gene"] == GENE].pivot(index="sample", columns="cell_line_id", values="v")
    c = D.focus["counts"]
    c = c[c["gene"] == GENE].pivot(index="sample", columns="cell_line_id", values="v")
    grp = D.L["tp53_group"]
    Wd = D.W.loc[~D.W["is_dmso"].astype(bool)]
    rows = []
    for _, pr in pick.iterrows():
        ww = Wd[(Wd["drug"] == pr["drug"]) & np.isclose(Wd["conc"].astype(float), float(pr["conc"]))]
        for s in ww.index[ww["used"].astype(bool)]:
            r = {"drug": pr["drug"], "conc": pr["conc"], "plate": ww.at[s, "plate"], "well": ww.at[s, "well"]}
            for gname in ("WT", "altered"):
                cols = [x for x in grp.index[grp == gname] if x in y.columns]
                yy, bb = y.reindex(index=[s], columns=cols).iloc[0], b.reindex(index=[s], columns=cols).iloc[0]
                ok = yy.notna() & bb.notna()
                r[f"n_{gname}"] = int(ok.sum())
                r[f"median_cpm_plate_baseline_{gname}"] = float(np.median(2 ** bb[ok])) if ok.any() else np.nan
                r[f"median_cpm_treated_{gname}"] = float(np.median(2 ** yy[ok])) if ok.any() else np.nan
                r[f"median_counts_treated_{gname}"] = float(np.median(c.reindex(index=[s], columns=cols).iloc[0]
                                                                      [ok])) if ok.any() else np.nan
            ya = y.reindex(index=[s]).iloc[0]
            lab = grp.reindex(ya.index)
            ok = ya.notna() & lab.isin(["WT", "altered"])
            if ok.sum() > 6:
                u = stats.mannwhitneyu(ya[ok & (lab == "WT")], ya[ok & (lab == "altered")], alternative="two-sided")
                r["p_treated_level_wt_vs_altered"] = float(u.pvalue)
            rows.append(r)
    return pd.DataFrame(rows)


# ============================================================================= all drug-doses: per-well difference
def well_delta(D, g):
    M = D.mat(g)
    wt = (D.L["tp53_group"] == "WT").to_numpy()
    alt = (D.L["tp53_group"] == "altered").to_numpy()
    with quiet():
        a = np.nanmedian(M[:, wt], axis=1)
        b = np.nanmedian(M[:, alt], axis=1)
        alla = np.nanmedian(M, axis=1)
    n1, n0 = np.isfinite(M[:, wt]).sum(1), np.isfinite(M[:, alt]).sum(1)
    d = a - b
    d[(n1 < MIN_GROUP) | (n0 < MIN_GROUP)] = np.nan
    # per-plate robust z over the plate's drug wells (each plate on its own scale: TRIM72 magnitudes differ by plate)
    z = np.full(len(d), np.nan)
    drug = ~D.W["is_dmso"].astype(bool).to_numpy()
    for p_ in D.W["plate"].unique():
        m = (D.W["plate"] == p_).to_numpy()
        c, s = robust_cs(d[m & drug])
        if np.isfinite(s) and s > 0:
            z[m] = (d[m] - c) / s
    return pd.DataFrame({"delta": d, "z": z, "wt_median": a, "altered_median": b, "all_median": alla},
                        index=D.W.index)


def per_drugdose(D, wd):
    W = D.W.join(wd)
    W = W[~W["is_dmso"].astype(bool) & W["used"].astype(bool)].copy()
    g = W.groupby(["drug", "dose"])
    out = g[["delta", "wt_median", "altered_median", "all_median"]].mean()
    out["z"] = g["z"].sum() / np.sqrt(g["z"].count())
    out["conc"] = g["conc"].first()
    out["plates"] = g["plate"].agg(lambda s: ",".join(sorted(set(map(str, s)))))
    out["n_wells"] = g.size()
    out = out.reset_index().drop(columns=["dose"])
    out["p_two_sided"] = 2 * T.norm_sf(np.abs(out["z"].to_numpy()))
    out["fdr"] = T.bh(out["p_two_sided"].to_numpy())
    return out


def screen_all(D, genes):
    tabs = {}
    for g in genes:
        t = per_drugdose(D, well_delta(D, g))
        tabs[g] = t
    keys = tabs[genes[0]][["drug", "conc"]]
    out = keys.copy()
    for g, t in tabs.items():
        t = t.set_index(["drug", "conc"])
        for c, nm in (("delta", "wt_minus_altered_log2"), ("z", "wt_minus_altered_z"), ("fdr", "fdr"),
                      ("wt_median", "wt_median_log2"), ("altered_median", "altered_median_log2")):
            out[f"{g}_{nm}"] = t[c].reindex(pd.MultiIndex.from_frame(keys)).to_numpy()
    r = D.res[D.res["gene"] == GENE].set_index(["drug", "conc"])
    for c in ("fold_change", "z_corrected", "fdr_up", "flags", "plates"):
        out[f"TRIM72_all_lines_{c}"] = r[c].reindex(pd.MultiIndex.from_frame(keys)).to_numpy()
    sc = D.p53score.set_index(["drug", "conc"])
    out["P53_ACTIVITY_all_lines_z"] = sc["z"].reindex(pd.MultiIndex.from_frame(keys)).to_numpy()
    pw = D.p53wt.set_index(["drug", "conc"])
    out["panel_p53_z_wt_more"] = pw["z_wt_more"].reindex(pd.MultiIndex.from_frame(keys)).to_numpy()
    out["panel_p53_pattern"] = pw["pattern"].reindex(pd.MultiIndex.from_frame(keys)).to_numpy()
    out["dna_damaging"] = out["drug"].isin(set(D.meta["dna_damage_drugs"]))
    out = out.join(D.drugs[[c for c in ("moa_fine", "targets") if c in D.drugs]], on="drug")
    return out, tabs


# ============================================================================= p53 activators, DNA damage or not
def activators_table(screen):
    s = screen.copy()
    strong = (s["P53_ACTIVITY_all_lines_z"] >= 5) | ((s["panel_p53_z_wt_more"] >= 5) &
                                                     (s["panel_p53_pattern"] == "WT induction"))
    t = s[strong].copy()
    t["class"] = np.where(t["dna_damaging"], "DNA-damaging (panel DNA_DAMAGE list)", "not DNA-damaging")
    t["TRIM72_up"] = (t["TRIM72_all_lines_z_corrected"] >= 3) & (t["TRIM72_all_lines_fold_change"] >= 1.2)
    cols = ["drug", "conc", "class", "moa_fine", "targets", "P53_ACTIVITY_all_lines_z", "panel_p53_z_wt_more",
            "P53_SCORE_wt_minus_altered_log2", "P53_SCORE_wt_minus_altered_z", "TRIM72_all_lines_fold_change",
            "TRIM72_all_lines_z_corrected", "TRIM72_up", "TRIM72_wt_minus_altered_log2", "TRIM72_wt_minus_altered_z",
            "TRIM72_fdr", "CDKN1A_wt_minus_altered_log2", "CDKN1A_wt_minus_altered_z", "TRIM72_all_lines_flags",
            "TRIM72_all_lines_plates"]
    t = t[cols].sort_values("P53_ACTIVITY_all_lines_z", ascending=False)
    # summaries over all drug-doses
    rows = []
    ok = s["TRIM72_all_lines_z_corrected"].notna() & s["P53_ACTIVITY_all_lines_z"].notna()
    rho, p = stats.spearmanr(s.loc[ok, "TRIM72_all_lines_z_corrected"], s.loc[ok, "P53_ACTIVITY_all_lines_z"])
    rows.append({"comparison": "all drug-doses: Spearman TRIM72 z vs P53_ACTIVITY z (all lines)", "n": int(ok.sum()),
                 "statistic": float(rho), "p": float(p)})
    ok2 = s["TRIM72_all_lines_z_corrected"].notna() & s["P53_SCORE_wt_minus_altered_z"].notna()
    rho, p = stats.spearmanr(s.loc[ok2, "TRIM72_all_lines_z_corrected"], s.loc[ok2, "P53_SCORE_wt_minus_altered_z"])
    rows.append({"comparison": "all drug-doses: Spearman TRIM72 z vs P53 score WT-minus-altered z", "n": int(ok2.sum()),
                 "statistic": float(rho), "p": float(p)})
    ok3 = s["TRIM72_wt_minus_altered_z"].notna() & s["P53_SCORE_wt_minus_altered_z"].notna()
    rho, p = stats.spearmanr(s.loc[ok3, "TRIM72_wt_minus_altered_z"], s.loc[ok3, "P53_SCORE_wt_minus_altered_z"])
    rows.append({"comparison": "all drug-doses: Spearman TRIM72 WT-minus-altered z vs P53 score WT-minus-altered z",
                 "n": int(ok3.sum()), "statistic": float(rho), "p": float(p)})
    up = (s["TRIM72_all_lines_z_corrected"] >= 3) & (s["TRIM72_all_lines_fold_change"] >= 1.2)
    a, b = int((strong & up).sum()), int((strong & ~up).sum())
    c, d = int((~strong & up).sum()), int((~strong & ~up).sum())
    orr, p = stats.fisher_exact([[a, b], [c, d]])
    rows.append({"comparison": "all drug-doses: TRIM72 up (z>=3, >=1.2x) among strong p53 activators vs the rest "
                               "(Fisher; statistic = odds ratio)", "n": a + b + c + d, "statistic": float(orr),
                 "p": float(p), "detail": f"activators {a}/{a + b} up; others {c}/{c + d} up"})
    # among the strong activators only: does TRIM72 rise more where the p53 response is stronger / more WT-selective?
    for xa, ya in (("TRIM72_all_lines_z_corrected", "P53_ACTIVITY_all_lines_z"),
                   ("TRIM72_all_lines_z_corrected", "P53_SCORE_wt_minus_altered_z"),
                   ("TRIM72_wt_minus_altered_z", "P53_SCORE_wt_minus_altered_z")):
        ok4 = t[xa].notna() & t[ya].notna()
        rho, p = stats.spearmanr(t.loc[ok4, xa], t.loc[ok4, ya])
        rows.append({"comparison": f"strong p53 activators only: Spearman {xa} vs {ya}", "n": int(ok4.sum()),
                     "statistic": float(rho), "p": float(p)})
    for cl in ("DNA-damaging (panel DNA_DAMAGE list)", "not DNA-damaging"):
        x = t[t["class"] == cl]
        rows.append({"comparison": f"strong p53 activators, {cl}: TRIM72 up", "n": len(x),
                     "statistic": float(x["TRIM72_up"].mean()) if len(x) else np.nan, "p": np.nan,
                     "detail": f"{int(x['TRIM72_up'].sum())} of {len(x)} up; "
                               + "; ".join(f"{d} {c:g}: TRIM72 {f:.2f}x z {z:.1f}" for d, c, f, z in
                                           x[["drug", "conc", "TRIM72_all_lines_fold_change",
                                              "TRIM72_all_lines_z_corrected"]].values)})
    return t, pd.DataFrame(rows)


# ============================================================================= target-likeness across genes
def gene_group(g, members):
    if g == GENE:
        return "TRIM72"
    if g in members:
        return "P53_ACTIVITY member"
    if g in OTHER_P53_TARGETS:
        return "p53 target outside the score"
    if g == "TP53":
        return "TP53 itself"
    return "other panel gene"


def target_likeness(D, tabs_score):
    """Four metrics per gene: (1) Spearman over drug-doses of its WT-minus-altered z with the P53 score's (the score
    without the gene for members); (2) its mean WT-minus-altered z over the TOP_P53 drug-doses with the strongest
    WT-selective P53-score induction; (3) across lines, Spearman of its r2 with the P53 score's in the reference
    wells (Fisher-z mean over wells); (4) untreated level WT vs altered (log2 DMSO CPM, difference of medians over the
    expressing lines)."""
    members = D.members
    lab = D.L["tp53_group"].to_numpy()
    keys = set(zip(D.ref_doses["drug"], D.ref_doses["conc"].astype(float)))
    ref_idx = [i for i, (d, c, u, dm) in enumerate(zip(D.W["drug"], D.W["conc"].astype(float), D.W["used"],
                                                       D.W["is_dmso"])) if (d, c) in keys and u and not dm]
    score_cache = {}
    rows = []
    for g in D.genes:
        sname = f"{SCORE}-{g}" if g in members else SCORE
        if sname not in score_cache:
            score_cache[sname] = per_drugdose(D, well_delta(D, sname)).set_index(["drug", "conc"])
        sc = score_cache[sname]
        tg = per_drugdose(D, well_delta(D, g)).set_index(["drug", "conc"])
        j = sc[["z"]].join(tg[["z", "delta"]], rsuffix="_g").dropna()
        r = {"gene": g, "group": gene_group(g, members), "status": D.meta["status"].get(g, ""),
             "n_lines_expressing": int(D.L[f"expr_{g}"].astype(bool).sum())}
        if len(j) > 20:
            rho, _ = stats.spearmanr(j["z"], j["z_g"])
            r["m1_spearman_delta_z_vs_p53score_delta_z"] = float(rho)
            top = j.sort_values("z", ascending=False).head(TOP_P53)
            r["m2_mean_delta_z_top_p53_drugdoses"] = float(top["z_g"].mean())
            r["m2_mean_delta_log2_top_p53_drugdoses"] = float(top["delta"].mean())
        M, Sm = D.mat(g)[ref_idx], D.mat(sname)[ref_idx]
        zs = []
        for i in range(len(ref_idx)):
            ok = np.isfinite(M[i]) & np.isfinite(Sm[i])
            if ok.sum() >= 10:
                rr = stats.spearmanr(M[i][ok], Sm[i][ok])[0]
                if np.isfinite(rr):
                    zs.append(np.arctanh(np.clip(rr, -0.999, 0.999)))
        r["m3_across_line_spearman_with_p53score_reference_wells"] = float(np.tanh(np.mean(zs))) if zs else np.nan
        e = D.L[f"expr_{g}"].astype(bool).to_numpy()
        lv = np.log2(D.L[f"cpm_dmso_{g}"].astype(float).to_numpy() + 0.1)
        a, b = lv[e & (lab == "WT")], lv[e & (lab == "altered")]
        if len(a) >= 3 and len(b) >= 3:
            r["m4_basal_wt_minus_altered_log2"] = float(np.median(a) - np.median(b))
            r["m4_p_mannwhitney"] = float(stats.mannwhitneyu(a, b, alternative="two-sided").pvalue)
        rows.append(r)
    t = pd.DataFrame(rows)
    summ = []
    for m in ["m1_spearman_delta_z_vs_p53score_delta_z", "m2_mean_delta_z_top_p53_drugdoses",
              "m3_across_line_spearman_with_p53score_reference_wells", "m4_basal_wt_minus_altered_log2"]:
        mem = t.loc[t["group"] == "P53_ACTIVITY member", m].dropna()
        oth = t.loc[t["group"] == "other panel gene", m].dropna()
        tv = float(t.loc[t["gene"] == GENE, m].iloc[0])
        u = stats.mannwhitneyu(mem, oth, alternative="two-sided")
        summ.append({"metric": m, "TRIM72": tv, "members_median": float(mem.median()),
                     "members_min": float(mem.min()), "other_genes_median": float(oth.median()),
                     "other_genes_iqr": f"{oth.quantile(0.25):.3f} to {oth.quantile(0.75):.3f}",
                     "auc_members_vs_other": float(u.statistic / (len(mem) * len(oth))), "p_members_vs_other":
                     float(u.pvalue), "n_members": len(mem), "n_other": len(oth),
                     "TRIM72_percentile_among_other_genes": float(100 * (oth < tv).mean()),
                     "TRIM72_percentile_among_members": float(100 * (mem < tv).mean()),
                     "TRIM72_rank_all_genes_desc": int((t[m] > tv).sum() + 1), "n_genes": int(t[m].notna().sum())})
    return t.sort_values("m1_spearman_delta_z_vs_p53score_delta_z", ascending=False), pd.DataFrame(summ)


# ============================================================================= checks without the pseudocount
def focus_matrix(D, name, gene):
    f = D.focus[name]
    return f[f["gene"] == gene].pivot(index="sample", columns="cell_line_id", values="v") \
        .reindex(index=D.W.index, columns=D.lines)


def pooled_fold_change(D, pick, B, rng):
    """TRIM72 without pseudocount or composition shift: per TP53 group, summed TRIM72 counts / summed library size
    in the treated well, over the same lines' sums in the plate's other drug wells (not the same drug). log2 ratio
    WT / altered, label permutation over lines. A check on the corrected (log, pseudocount 0.5) effects for a gene
    with ~5 counts per profile, where a well that lost reads can read 'up' from the pseudocount alone."""
    C, Tt = focus_matrix(D, "counts", GENE), focus_matrix(D, "counts", "total_counts")
    grp = D.L["tp53_group"].to_numpy()
    Wd = D.W.loc[~D.W["is_dmso"].astype(bool)]
    rows = []
    for _, pr in pick.iterrows():
        ww = Wd[(Wd["drug"] == pr["drug"]) & np.isclose(Wd["conc"].astype(float), float(pr["conc"]))]
        for s in ww.index[ww["used"].astype(bool)]:
            pl = ww.at[s, "plate"]
            others = Wd.index[(Wd["plate"] == pl) & (Wd["drug"] != pr["drug"])]
            bc, bt = C.loc[others].sum(axis=0, min_count=1), Tt.loc[others].sum(axis=0, min_count=1)
            tc, tt = C.loc[s], Tt.loc[s]
            ok = (np.isfinite(tc) & np.isfinite(tt) & (bt > 0) & np.isin(grp, ["WT", "altered"])).to_numpy()
            lab = (grp[ok] == "WT").astype(float)
            arr = np.vstack([tc.to_numpy()[ok], tt.to_numpy()[ok], bc.to_numpy()[ok], bt.to_numpy()[ok]])

            def fc(Lm):
                s1 = Lm @ arr.T                 # (k x 4): sums over the lines of the group
                return (s1[:, 0] / s1[:, 1]) / (s1[:, 2] / s1[:, 3])
            Lw, La = lab[None, :], 1 - lab[None, :]
            with quiet():
                fw, fa = float(fc(Lw)[0]), float(fc(La)[0])
                obs = math.log2(fw / fa) if fw > 0 and fa > 0 else np.nan
                Lp = np.argsort(rng.random((B, len(lab))), axis=1)
                Lb = lab[Lp]
                null = np.log2(fc(Lb) / fc(1 - Lb))
            null = null[np.isfinite(null)]
            r = {"drug": pr["drug"], "conc": pr["conc"], "plate": pl, "well": ww.at[s, "well"],
                 "n_wt": int(lab.sum()), "n_altered": int((1 - lab).sum()),
                 "trim72_counts_treated_wt": float((arr[0] * lab).sum()),
                 "trim72_counts_treated_altered": float((arr[0] * (1 - lab)).sum()),
                 "cpm_treated_wt": 1e6 * float((arr[0] * lab).sum() / (arr[1] * lab).sum()),
                 "cpm_treated_altered": 1e6 * float((arr[0] * (1 - lab)).sum() / (arr[1] * (1 - lab)).sum()),
                 "cpm_plate_other_drugs_wt": 1e6 * float((arr[2] * lab).sum() / (arr[3] * lab).sum()),
                 "cpm_plate_other_drugs_altered": 1e6 * float((arr[2] * (1 - lab)).sum() / (arr[3] * (1 - lab)).sum()),
                 "fold_change_wt": fw, "fold_change_altered": fa, "log2_ratio_wt_over_altered": obs,
                 "p_perm": float((1 + np.sum(np.abs(null) >= abs(obs) - 1e-12)) / (1 + len(null)))
                 if np.isfinite(obs) else np.nan,
                 "library_size_vs_plate_log2": float(np.log2((arr[1].sum() / ok.sum()) /
                                                             (arr[3].sum() / max(1, len(others)) / ok.sum())))}
            rows.append(r)
    return pd.DataFrame(rows)


# ============================================================================= pooled over TRIM72-raising drug-doses
def inducibility_sets(D, B, rng):
    """Per line, the mean TRIM72 effect over a set of TRIM72-raising drug-doses (each drug-dose: mean of its used
    wells) - one 'inducibility' value per line - compared between TP53 groups, between functional groups and
    against responsiveness (computed without the wells of the set's drugs). Sets: every TRIM72 raiser (z >= 3,
    >= 1.2x, FDR < 0.10, position correctable), those that also raise the P53 score (all-line z >= 3) and those that
    do not. The same for the P53 score, MDM2 and CDKN1A (controls) and ATF3."""
    r = D.res[D.res["gene"] == GENE].copy()
    r = r[(r["z_corrected"] >= 3) & (r["fold_change"] >= 1.2) & (r["fdr_up"] < 0.10)
          & ~r["flags"].fillna("").str.contains("position not correctable")]
    r = r.merge(D.p53score[["drug", "conc", "z"]].rename(columns={"z": "p53z"}), on=["drug", "conc"], how="left")
    sets = {"all TRIM72 raisers": r, "TRIM72 raisers with P53 score z >= 3": r[r["p53z"] >= 3],
            "TRIM72 raisers with P53 score z < 3": r[r["p53z"] < 3]}
    lab_g = (D.L["tp53_group"] == "WT").astype(int).to_numpy()
    fc_ = D.func["functional_call"].reindex(D.lines).fillna("").to_numpy()
    lab_f = np.where(fc_ == "responsive", 1, np.where(fc_ == "unresponsive", 0, -1))
    cls = D.L["tp53_class"].to_numpy()
    organ = D.L["organ"].fillna("").astype(str).to_numpy()
    Wd = D.W.loc[~D.W["is_dmso"].astype(bool)]
    rows = []
    for sname, t in sets.items():
        fams = {family(d) for d in t["drug"]}
        resp, nref = responsiveness_excluding(D, fams)
        for g in [GENE, SCORE, "MDM2", "CDKN1A", "ATF3"]:
            V, Z = [], []
            for d, c in zip(t["drug"], t["conc"]):
                ww = Wd[(Wd["drug"] == d) & np.isclose(Wd["conc"].astype(float), float(c))]
                v, zl = per_line_values(D, g, list(ww.index[ww["used"].astype(bool)]))
                V.append(v)
                Z.append(zl)
            with quiet():
                V, Z = np.nanmean(np.vstack(V), axis=0), np.nanmean(np.vstack(Z), axis=0)
            for vt, vals in (("mean log2FC_corrected", V), ("mean z_line", Z)):
                if g == SCORE and vt == "mean z_line":
                    continue
                row = {"set": sname, "n_drugdoses": len(t), "drugdoses": "; ".join(f"{d} {c:g}" for d, c in
                                                                                 zip(t["drug"], t["conc"])),
                       "gene": g, "value": vt, "grouping": "TP53 genotype (WT vs altered)"}
                row.update(compare(vals, lab_g, cls, organ, B, rng))
                ok = np.isfinite(vals) & np.isfinite(resp.to_numpy())
                rho, p = stats.spearmanr(vals[ok], resp.to_numpy()[ok])
                row["spearman_vs_responsiveness"], row["p_spearman"] = float(rho), float(p)
                bl = np.log2(D.L[f"cpm_dmso_{g}"].astype(float).to_numpy() + 0.1) if f"cpm_dmso_{g}" in D.L \
                    else D.func["basal_p53_activity_log2"].reindex(D.lines).to_numpy(dtype=float)
                row["partial_spearman_given_baseline"], row["p_partial"], _ = partial_spearman(vals, resp.to_numpy(),
                                                                                              bl)
                o2 = ols(vals, np.column_stack([lab_g.astype(float), bl]), ["wt", "baseline"])
                row["wt_minus_altered_adjusted_for_baseline"], row["p_adjusted"] = o2.get("wt_coef"), o2.get("wt_p")
                row["responsiveness_reference_wells"] = nref
                rows.append(row)
                # functional grouping (responsive vs unresponsive; 'uncertain' lines left out)
                m = lab_f >= 0
                row2 = {k: row[k] for k in ("set", "n_drugdoses", "drugdoses", "gene", "value")}
                row2["grouping"] = ("functional p53, responsive vs unresponsive ('uncertain' left out; the *_wt "
                                    "columns hold the responsive lines, the *_altered columns the unresponsive)")
                cmp2 = compare(vals[m], lab_f[m], cls[m], organ[m], B, rng)
                row2.update({k: v for k, v in cmp2.items() if not k.startswith(
                    ("n_missense", "n_truncating", "median_missense", "median_truncating", "p_missense",
                     "p_truncating"))})
                rows.append(row2)
    return pd.DataFrame(rows)


def responsiveness_excluding(D, families):
    keys = set(zip(D.ref_doses["drug"], D.ref_doses["conc"].astype(float)))
    W = D.W
    sel = [i for i, (d, c, u, dm) in enumerate(zip(W["drug"], W["conc"].astype(float), W["used"], W["is_dmso"]))
           if (d, c) in keys and u and not dm and family(d) not in families]
    with quiet():
        return pd.Series(np.nanmean(D.P53[sel], axis=0), index=D.lines), len(sel)


def replicate_agreement(D, pick, genes):
    """Drug-doses with two used wells (plates 6 and 14): Spearman across lines of the two wells' r2 - how well the
    line-to-line differences that a WT-vs-altered test relies on replicate."""
    Wd = D.W.loc[~D.W["is_dmso"].astype(bool)]
    rows = []
    for _, pr in pick.iterrows():
        ww = Wd[(Wd["drug"] == pr["drug"]) & np.isclose(Wd["conc"].astype(float), float(pr["conc"]))]
        used = list(ww.index[ww["used"].astype(bool)])
        if len(used) != 2:
            continue
        for g in genes:
            a, _ = per_line_values(D, g, [used[0]])
            b, _ = per_line_values(D, g, [used[1]])
            ok = np.isfinite(a) & np.isfinite(b)
            rho, p = stats.spearmanr(a[ok], b[ok])
            rows.append({"drug": pr["drug"], "conc": pr["conc"], "wells": f"{ww.at[used[0], 'plate']} / "
                         f"{ww.at[used[1], 'plate']}", "gene": g, "n_lines": int(ok.sum()),
                         "spearman_between_wells": float(rho), "p": float(p),
                         "median_log2_well1": float(np.median(a[ok])), "median_log2_well2": float(np.median(b[ok]))})
    return pd.DataFrame(rows)


# ============================================================================= summaries
def per_line_check(D):
    """Independent check: idarubicin 5 uM per-line TRIM72 (mean of the used wells) against the earlier corrected
    table (trim72_idarubicin/corrected/TRIM72_idarubicin_5uM_per_line_corrected.csv, made by its own script)."""
    f = os.path.join(REPO, "trim72_idarubicin", "corrected", "TRIM72_idarubicin_5uM_per_line_corrected.csv")
    if not os.path.exists(f):
        return {"check": "idarubicin 5 uM per-line TRIM72 vs trim72_idarubicin/corrected (max |diff|)",
                "value": np.nan, "n": 0, "note": "reference table not found"}
    ref = pd.read_csv(f).set_index("cell_line_id")
    Wd = D.W.loc[~D.W["is_dmso"].astype(bool) & D.W["used"].astype(bool)]
    ss = list(Wd.index[(Wd["drug"] == "Idarubicin (hydrochloride)") & np.isclose(Wd["conc"].astype(float), 5.0)])
    r2, zl = per_line_values(D, GENE, ss)
    mine = pd.DataFrame({"r2": r2, "z": zl}, index=D.lines).join(ref[["log2FC_corrected", "z_line"]]).dropna()
    return {"check": "idarubicin 5 uM per-line TRIM72 r2 vs trim72_idarubicin/corrected (max |diff|)",
            "value": float(np.max(np.abs(mine["r2"] - mine["log2FC_corrected"]))), "n": len(mine),
            "note": f"z_line max |diff| {float(np.max(np.abs(mine['z'] - mine['z_line']))):.2e}; wells {ss}"}


def screen_summary(screen, genes):
    """Per gene, over all drug-doses: how many have a WT-minus-altered difference at FDR < 0.10 in each direction,
    the spread of the per-drug-dose z (about 1 when there is no TP53-group structure) and the Spearman of the gene's
    WT-minus-altered z with the P53 score's."""
    rows = []
    for g in genes:
        z, f = screen[f"{g}_wt_minus_altered_z"], screen[f"{g}_fdr"]
        ok = z.notna() & screen[f"{SCORE}_wt_minus_altered_z"].notna()
        rho, p = stats.spearmanr(z[ok], screen.loc[ok, f"{SCORE}_wt_minus_altered_z"]) if g != SCORE else (1.0, 0.0)
        rows.append({"gene": g, "n_drugdoses": int(z.notna().sum()),
                     "n_fdr10_wt_higher": int(((f < 0.10) & (z > 0)).sum()),
                     "n_fdr10_altered_higher": int(((f < 0.10) & (z < 0)).sum()),
                     "sd_of_z": float(np.nanstd(z)), "frac_abs_z_gt_3": float(np.mean(np.abs(z[z.notna()]) > 3)),
                     "spearman_z_with_P53_SCORE_z": float(rho), "p_spearman": float(p)})
    return pd.DataFrame(rows)


KEY_DOSES = [("Idarubicin (hydrochloride)", 5.0), ("Idarubicin (hydrochloride)", 0.5),
             ("Idarubicin (hydrochloride)", 0.05), ("Homoharringtonine", 5.0), ("Homoharringtonine", 0.5),
             ("Auranofin", 5.0), ("Dinaciclib", 5.0), ("Epirubicin (hydrochloride)", 5.0),
             ("Doxorubicin (hydrochloride)", 5.0), ("Topotecan (hydrochloride)", 5.0),
             ("Mitoxantrone (dihydrochloride)", 5.0), ("Selinexor", 5.0), ("Selinexor", 0.5)]


def key_results(cmp_, wide):
    """The headline rows of wt_vs_altered_selected_long.csv: the strongest TRIM72 raisers and selinexor, TRIM72 next
    to the positive controls, every scope (mean of the used wells, and each well alone when there are two)."""
    genes = [GENE] + CONTROLS + [SCORE]
    x = cmp_[cmp_["gene"].isin(genes)].copy()
    keep = np.zeros(len(x), bool)
    for d, c in KEY_DOSES:
        keep |= ((x["drug"] == d) & np.isclose(x["conc"].astype(float), c)).to_numpy()
    x = x[keep].copy()
    x["order"] = [[k for k, (d, c) in enumerate(KEY_DOSES) if d == a and np.isclose(c, b)][0]
                  for a, b in zip(x["drug"], x["conc"].astype(float))]
    x["gorder"] = x["gene"].map({g: i for i, g in enumerate(genes)})
    for nm, col in (("fc_wt", "median_wt_log2"), ("fc_altered", "median_altered_log2"),
                    ("fc_truncating_splice_deletion", "median_truncating_log2"), ("fc_missense", "median_missense_log2")):
        x[nm] = 2.0 ** x[col]
    x["ratio_wt_over_altered"] = 2.0 ** x["diff_wt_minus_altered_log2"]
    w = wide.set_index(["drug", "conc"])
    k = pd.MultiIndex.from_frame(x[["drug", "conc"]])
    x["TRIM72_panel_fold_change_all_lines"] = w["TRIM72_panel_fold_change"].reindex(k).to_numpy()
    x["P53_ACTIVITY_panel_z_all_lines"] = w["P53_ACTIVITY_panel_z"].reindex(k).to_numpy()
    cols = ["drug", "conc", "scope", "plates", "dna_damaging", "gene", "TRIM72_panel_fold_change_all_lines",
            "P53_ACTIVITY_panel_z_all_lines", "n_wt", "n_altered", "fc_wt", "fc_altered",
            "fc_truncating_splice_deletion", "fc_missense", "diff_wt_minus_altered_log2", "ratio_wt_over_altered",
            "ci95_low", "ci95_high", "p_perm", "p_mannwhitney", "fdr_perm", "p_perm_within_organ",
            "critical_abs_diff_p05", "p_altered_lines_above_0", "frac_wt_lines_up", "frac_altered_lines_up",
            "spearman_vs_responsiveness_ldo", "p_spearman_responsiveness", "partial_spearman_given_baseline",
            "p_partial", "wt_minus_altered_adjusted_for_baseline", "p_adjusted", "spearman_vs_p53score_same_wells",
            "p_spearman_p53score"]
    x["sorder"] = (x["scope"] != "mean of used wells").astype(int)
    return x.sort_values(["order", "sorder", "scope", "gorder"])[cols].reset_index(drop=True)


# ============================================================================= main
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--data", default=os.environ.get("MG53_DATA") or os.environ.get("TAHOE_DATA") or os.path.expanduser("~/Tahoe-100M"))
    ap.add_argument("--recompute", action="store_true", help="rebuild cache/ from the panel extract")
    ap.add_argument("--perm", type=int, default=10000, help="permutations / bootstrap resamples per test")
    a = ap.parse_args()
    cdir, tdir = os.path.join(os.environ.get("MG53_OUT") or HERE, "cache"), os.path.join(os.environ.get("MG53_OUT") or HERE, "tables")
    os.makedirs(tdir, exist_ok=True)
    if a.recompute or not os.path.exists(os.path.join(cdir, "meta.json")):
        build_cache(a.data, cdir)
    D = Data(cdir, a.data)
    rng = np.random.default_rng(SEED)
    D.L["tp53_class"] = [tp53_class(g, c) for g, c in zip(D.L["tp53_group"], D.L["tp53_changes"])]

    # ---- checks against the panel's own tables
    checks = []
    resp, nref = responsiveness(D)
    f = D.func["p53_responsiveness_log2"].reindex(D.lines)
    checks.append({"check": "p53 responsiveness recomputed vs p53_functional_status.csv (max |diff|)",
                   "value": float(np.nanmax(np.abs(resp.to_numpy() - f.to_numpy()))), "n": int(f.notna().sum()),
                   "note": f"{nref} reference wells"})
    mine = D.res[D.res["gene"] == GENE].set_index(["drug", "conc"])
    pan = D.panel_trim72.set_index(["drug", "conc"])
    j = mine[["fold_change", "z_corrected"]].join(pan[["fold_change", "z_corrected"]], rsuffix="_panel").dropna()
    checks.append({"check": "TRIM72 drug-dose fold change vs TRIM72_drug_effects_by_dose.csv (max |log2 diff|)",
                   "value": float(np.max(np.abs(np.log2(j["fold_change"]) - np.log2(j["fold_change_panel"])))),
                   "n": len(j), "note": "z max |diff| "
                   f"{float(np.max(np.abs(j['z_corrected'] - j['z_corrected_panel']))):.2e}"})
    ida = mine.loc[("Idarubicin (hydrochloride)", 5.0)]
    checks.append({"check": "TRIM72 idarubicin 5 uM fold change / z (README: 12.2x, z 15.9)",
                   "value": float(ida["fold_change"]), "n": 2, "note": f"z {float(ida['z_corrected']):.2f}"})
    wt = D.p53wt.set_index(["drug", "conc"])
    checks.append({"check": "lines: TP53 WT / altered", "value": int((D.L['tp53_group'] == 'WT').sum()),
                   "n": int((D.L['tp53_group'] == 'altered').sum()), "note": "WT count in value, altered in n"})
    checks.append({"check": "P53_ACTIVITY members used", "value": len(D.members), "n": len(D.members),
                   "note": ", ".join(D.members)})
    checks.append(per_line_check(D))

    # ---- lines
    lines = D.L[["cell_name", "organ", "tp53_group", "tp53_class", "tp53_changes"]].copy()
    lines = lines.join(D.func[["p53_responsiveness_log2", "p53_responsiveness_se", "functional_call",
                               "basal_p53_activity_log2", "discordant"]])
    lines["TRIM72_expressed"] = D.L[f"expr_{GENE}"]
    lines["TRIM72_cpm_dmso"] = D.L[f"cpm_dmso_{GENE}"]

    # ---- selected drug-doses: WT vs altered in the same wells
    # ---- every drug-dose: WT-minus-altered per well (TRIM72, controls, score)
    t0 = time.time()
    screen, tabs = screen_all(D, [GENE] + CONTROLS + [SCORE] + ["ATF3", "PMAIP1"])
    print(f"screen of all drug-doses ({time.time() - t0:.0f} s)", flush=True)
    pick = select_drugdoses(D, screen)
    genes = [GENE] + CONTROLS + [SCORE] + EXTRA
    t0 = time.time()
    cmp_, long_ = wt_vs_altered_selected(D, pick, genes, a.perm, rng)
    print(f"selected drug-doses: {len(pick)}; comparisons {len(cmp_)} ({time.time() - t0:.0f} s)", flush=True)
    lev = trim72_levels(D, pick)

    # compact side-by-side view: TRIM72 vs the controls, mean of used wells
    m = cmp_[cmp_["scope"] == "mean of used wells"]
    wide = pick[["drug", "conc", "role", "dna_damaging", "screen_hit"]].copy()
    for g in [GENE, "CDKN1A", "MDM2", SCORE]:
        x = m[m["gene"] == g].set_index(["drug", "conc"])
        k = pd.MultiIndex.from_frame(wide[["drug", "conc"]])
        wide[f"{g}_fc_all_lines"] = 2 ** x["median_all_log2"].reindex(k).to_numpy()
        wide[f"{g}_fc_wt"] = 2 ** x["median_wt_log2"].reindex(k).to_numpy()
        wide[f"{g}_fc_altered"] = 2 ** x["median_altered_log2"].reindex(k).to_numpy()
        wide[f"{g}_diff_log2"] = x["diff_wt_minus_altered_log2"].reindex(k).to_numpy()
        wide[f"{g}_ci95"] = [f"{lo:.2f} to {hi:.2f}" for lo, hi in
                             zip(x["ci95_low"].reindex(k), x["ci95_high"].reindex(k))]
        wide[f"{g}_p_perm"] = x["p_perm"].reindex(k).to_numpy()
        wide[f"{g}_fdr_perm"] = x["fdr_perm"].reindex(k).to_numpy()
        if g == GENE:
            wide[f"{g}_p_within_organ"] = x["p_perm_within_organ"].reindex(k).to_numpy()
            wide[f"{g}_diff_adjusted_for_baseline"] = x["wt_minus_altered_adjusted_for_baseline"].reindex(k).to_numpy()
            wide[f"{g}_spearman_responsiveness"] = x["spearman_vs_responsiveness_ldo"].reindex(k).to_numpy()
            wide[f"{g}_p_spearman_responsiveness"] = x["p_spearman_responsiveness"].reindex(k).to_numpy()
            wide[f"{g}_spearman_p53score_same_wells"] = x["spearman_vs_p53score_same_wells"].reindex(k).to_numpy()
            wide[f"{g}_p_spearman_p53score_same_wells"] = x["p_spearman_p53score"].reindex(k).to_numpy()
            wide[f"{g}_fc_truncating"] = 2 ** x["median_truncating_log2"].reindex(k).to_numpy()
            wide[f"{g}_frac_altered_up"] = x["frac_altered_lines_up"].reindex(k).to_numpy()
            wide[f"{g}_frac_wt_up"] = x["frac_wt_lines_up"].reindex(k).to_numpy()
    tr = D.res[D.res["gene"] == GENE].set_index(["drug", "conc"])
    k = pd.MultiIndex.from_frame(wide[["drug", "conc"]])
    wide.insert(5, "TRIM72_panel_fold_change", tr["fold_change"].reindex(k).to_numpy())
    wide.insert(6, "TRIM72_panel_z", tr["z_corrected"].reindex(k).to_numpy())
    wide.insert(7, "P53_ACTIVITY_panel_z", D.p53score.set_index(["drug", "conc"])["z"].reindex(k).to_numpy())
    # TRIM72 counts per profile in the treated wells (median over lines, mean over the used wells): < 5 means the
    # corrected effect leans on the pseudocount (see trim72_pooled_fold_change_no_pseudocount.csv)
    Cm = focus_matrix(D, "counts", GENE)
    Wd_ = D.W.loc[~D.W["is_dmso"].astype(bool) & D.W["used"].astype(bool)]
    med_counts = []
    for d_, c_ in zip(wide["drug"], wide["conc"]):
        ss = Wd_.index[(Wd_["drug"] == d_) & np.isclose(Wd_["conc"].astype(float), float(c_))]
        med_counts.append(float(np.mean([np.nanmedian(Cm.loc[x]) for x in ss])) if len(ss) else np.nan)
    wide.insert(8, "TRIM72_median_counts_per_profile_treated", med_counts)
    wide = wide.sort_values("TRIM72_panel_z", ascending=False)
    pooled = pooled_fold_change(D, pick, a.perm, rng)
    sets = inducibility_sets(D, a.perm, rng)
    rep = replicate_agreement(D, pick, [GENE, SCORE, "MDM2", "CDKN1A", "TP53I3", "FDXR"])

    acts, acts_summary = activators_table(screen)
    tsig = screen[(screen["TRIM72_fdr"] < 0.10)].sort_values("TRIM72_wt_minus_altered_z")
    checks.append({"check": "TRIM72 WT-minus-altered: drug-doses with FDR < 0.10 (all drug-doses)",
                   "value": len(tsig), "n": int(screen["TRIM72_fdr"].notna().sum()),
                   "note": "; ".join(f"{d} {c:g} (z {z:.1f})" for d, c, z in
                                     tsig[["drug", "conc", "TRIM72_wt_minus_altered_z"]].values[:12])})
    csig = screen[(screen["CDKN1A_fdr"] < 0.10) & (screen["CDKN1A_wt_minus_altered_z"] > 0)]
    checks.append({"check": "CDKN1A WT-minus-altered: drug-doses with FDR < 0.10 and WT higher",
                   "value": len(csig), "n": int(screen["CDKN1A_fdr"].notna().sum()), "note": ""})

    # ---- target-likeness
    t0 = time.time()
    tl, tls = target_likeness(D, tabs)
    print(f"target-likeness for {len(tl)} genes ({time.time() - t0:.0f} s)", flush=True)

    TABLES = {
        "lines_tp53_status.csv": lines.reset_index(),
        "selected_drugdoses.csv": pick,
        "wt_vs_altered_selected_long.csv": cmp_,
        "wt_vs_altered_selected_wide.csv": wide,
        "per_line_effects_selected.csv": long_,
        "trim72_levels_by_tp53_group.csv": lev,
        "screen_all_drugdoses_wt_minus_altered.csv": screen,
        "p53_activators_dna_damage_vs_not.csv": acts,
        "p53_activators_summary.csv": acts_summary,
        "target_likeness_by_gene.csv": tl,
        "target_likeness_summary.csv": tls,
        "trim72_pooled_fold_change_no_pseudocount.csv": pooled,
        "trim72_inducibility_pooled_sets.csv": sets,
        "replicate_wells_per_line_agreement.csv": rep,
        "screen_summary_by_gene.csv": screen_summary(screen, [GENE] + CONTROLS + [SCORE] + ["ATF3", "PMAIP1"]),
        "key_results.csv": key_results(cmp_, wide),
        "checks.csv": pd.DataFrame(checks),
    }
    for name, df in TABLES.items():
        df.to_csv(os.path.join(tdir, name), index=False, float_format="%.6g")
    print(pd.DataFrame(checks).to_string(index=False))
    print(f"tables written to {tdir}")


if __name__ == "__main__":
    main()
