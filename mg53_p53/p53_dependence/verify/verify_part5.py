#!/usr/bin/env python3
"""Part 5 of the adversarial verification (independent code, raw gene-panel counts, read-only on tahoe_data).

Checks:
  A. TRIM72 inducibility pooled over the analysis's 18 TRIM72-raising drug-doses (F6), recomputed with the simple
     DMSO-baseline log2 ratio: WT minus altered, baseline-adjusted (OLS on log2 DMSO CPM), Spearman with p53
     responsiveness, split into p53-activating (10) and non-activating (8) raisers; per-drug-dose sign test.
  B. Sign of the analysis's own screen TRIM72 WT-minus-altered z among its TRIM72 raisers (F4 'looks like noise').
  C. Low-expressed p53 targets as power-matched positive controls (F1/F5): DMSO CPM vs target-likeness, and their
     idarubicin WT-minus-altered differences and within-group SD next to TRIM72's.
  D. Within-organ permutation of the idarubicin 5 uM TRIM72 contrast with the DMSO-ratio values (F1).
  E. Fine-grid power (80% minimal detectable WT excess) with the analysis's own per-line values (F1).
Usage: python3 verify_part5.py
"""
import os
import numpy as np
import pandas as pd
from scipy import stats

DATA = "/home/user/tahoe_data"
HERE = os.path.dirname(os.path.abspath(__file__))
ANA = os.path.join(os.path.dirname(HERE), "tables")
OUT = os.path.join(HERE, "tables")
os.makedirs(OUT, exist_ok=True)
pd.set_option("display.width", 250); pd.set_option("display.max_columns", 40); pd.set_option("display.max_rows", 200)
RNG = np.random.default_rng(11)
B = 10000
MIN_CELLS = 30
P53 = ["CDKN1A", "MDM2", "FDXR", "ZMAT3", "SESN1", "BBC3", "BAX", "TP53I3", "RRM2B", "AEN", "DDB2", "XPC", "PHLDA3",
       "SPATA18", "TRIAP1", "RPS27L", "ACER2", "TP53INP1", "PLK3", "POLH", "EDA2R"]
GEN = ["TRIM72"] + P53

smap = pd.read_csv(f"{DATA}/gene_panel/sample_map.csv")
wl = pd.read_parquet(f"{DATA}/gene_panel/well_line.parquet", columns=["sample", "cell_line_id", "n_cells", "total_counts"] + GEN)
wl = wl.groupby(["sample", "cell_line_id"], as_index=False).sum().merge(
    smap[["sample", "plate", "drug", "conc", "is_dmso"]], on="sample")
base = pd.read_csv(f"{DATA}/gene_panel/results/baseline_by_cell_line.csv").set_index("cell_line_id")
func = pd.read_csv(f"{DATA}/gene_panel/results/p53_functional_status.csv").set_index("cell_line_id")
dm = wl[wl.is_dmso.astype(bool)]
pool = dm.groupby("cell_line_id")[GEN + ["total_counts"]].sum()
cpm_all = pool[GEN].div(pool.total_counts, axis=0) * 1e6
expr = cpm_all >= 1
dpl = dm.groupby(["plate", "cell_line_id"])[GEN + ["total_counts"]].sum()


def ratio(sample, g):
    t = wl[(wl["sample"] == sample) & (wl.n_cells >= MIN_CELLS)].set_index("cell_line_id")
    d = dpl.loc[t.plate.iloc[0]].reindex(t.index)
    v = np.log2((t[g] + 0.5) / t.total_counts) - np.log2((d[g] + 0.5) / d.total_counts)
    v[~expr.reindex(t.index)[g].fillna(False).values] = np.nan
    return v


def drugdose_lines(drug, conc, g):
    ss = smap[(smap.drug == drug) & np.isclose(smap.conc, conc)]["sample"]
    return pd.concat([ratio(s, g) for s in ss], axis=1).mean(axis=1)


def perm_diff(v, lab, B=B, within=None):
    v = np.asarray(v, float); lab = np.asarray(lab, bool)
    d = np.median(v[lab]) - np.median(v[~lab])
    cnt = 0
    for _ in range(B):
        if within is None:
            p = RNG.permutation(lab)
        else:
            p = lab.copy()
            for grp in np.unique(within):
                m = within == grp
                p[m] = RNG.permutation(lab[m])
        cnt += abs(np.median(v[p]) - np.median(v[~p])) >= abs(d) - 1e-12
    return d, (cnt + 1) / (B + 1)


def ols_wt(y, wt, x):
    X = np.column_stack([np.ones(len(y)), wt.astype(float), x])
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    r = y - X @ beta
    s2 = r @ r / (len(y) - 3)
    se = np.sqrt(s2 * np.linalg.inv(X.T @ X)[1, 1])
    return beta[1], 2 * stats.t.sf(abs(beta[1] / se), len(y) - 3)


def partial_spearman(a, b, c):
    ra, rb, rc = (stats.rankdata(z) for z in (a, b, c))
    res = lambda y: y - np.polyval(np.polyfit(rc, y, 1), rc)
    return stats.pearsonr(res(ra), res(rb))


# ---------------------------------------------------------------- A. pooled raisers (F6)
ps = pd.read_csv(f"{ANA}/trim72_inducibility_pooled_sets.csv")
sets = {}
for s in ps["set"].unique():
    dd = ps.loc[ps["set"] == s, "drugdoses"].iloc[0].split("; ")
    sets[s] = [(x.rsplit(" ", 1)[0], float(x.rsplit(" ", 1)[1])) for x in dd]
per_dd = {}
for dd in sets["all TRIM72 raisers"]:
    per_dd[dd] = drugdose_lines(dd[0], dd[1], "TRIM72")
M = pd.DataFrame(per_dd)
lines_ok = M.index[M.notna().sum(axis=1) >= 0.8 * M.shape[1]]
rowsA = []
for sname, dds in sets.items():
    v = M[dds].reindex(lines_ok).mean(axis=1, skipna=True)
    v = v[np.isfinite(v)]
    wt = base.reindex(v.index).tp53_group.eq("WT").to_numpy()
    bl = np.log2(cpm_all.reindex(v.index).TRIM72.to_numpy())
    resp = func.reindex(v.index).p53_responsiveness_log2.to_numpy()
    d, p = perm_diff(v.to_numpy(), wt)
    adj, p_adj = ols_wt(v.to_numpy(), wt, bl)
    rho, p_rho = stats.spearmanr(v, resp)
    prho, p_prho = partial_spearman(v.to_numpy(), resp, bl)
    # per drug-dose sign of WT-minus-altered (unadjusted median diff and baseline-adjusted OLS)
    signs, signs_adj = [], []
    for dd in dds:
        x = M[dd].dropna()
        w = base.reindex(x.index).tp53_group.eq("WT").to_numpy()
        signs.append(np.median(x[w]) - np.median(x[~w]))
        signs_adj.append(ols_wt(x.to_numpy(), w, np.log2(cpm_all.reindex(x.index).TRIM72.to_numpy()))[0])
    signs, signs_adj = np.array(signs), np.array(signs_adj)
    rowsA.append(dict(set=sname, n_drugdoses=len(dds), n_wt=int(wt.sum()), n_alt=int((~wt).sum()),
                      median_wt=np.median(v[wt]), median_alt=np.median(v[~wt]), diff=d, p_perm=p,
                      adj_diff=adj, p_adj_ols=p_adj, rho_resp=rho, p_rho=p_rho, partial_rho=prho, p_partial=p_prho,
                      n_dd_diff_pos=int((signs > 0).sum()), p_sign=stats.binomtest(int((signs > 0).sum()), len(signs)).pvalue,
                      n_dd_adj_pos=int((signs_adj > 0).sum()),
                      p_sign_adj=stats.binomtest(int((signs_adj > 0).sum()), len(signs_adj)).pvalue))
A = pd.DataFrame(rowsA)
print("=== A. TRIM72 inducibility pooled over the analysis's raiser sets (DMSO-ratio values) ===")
print(A.round(3).to_string(index=False))
A.to_csv(f"{OUT}/f6_pooled_raisers_dmso_ratio.csv", index=False)

# ---------------------------------------------------------------- B. analysis screen sign among raisers (F4)
sc = pd.read_csv(f"{ANA}/screen_all_drugdoses_wt_minus_altered.csv")
r = (sc.TRIM72_all_lines_z_corrected >= 3) & (sc.TRIM72_all_lines_fold_change >= 1.2) & (sc.TRIM72_all_lines_fdr_up < 0.10)
rowsB = []
for lab, m in [("TRIM72 raisers (z>=3, >=1.2x, FDR<0.10)", r),
               ("raisers with P53_ACTIVITY z >= 3", r & (sc.P53_ACTIVITY_all_lines_z >= 3)),
               ("raisers with P53_ACTIVITY z < 3", r & (sc.P53_ACTIVITY_all_lines_z < 3)),
               ("all other drug-doses", ~r)]:
    z = sc.loc[m, "TRIM72_wt_minus_altered_z"].dropna()
    rowsB.append(dict(set=lab, n=len(z), n_pos=int((z > 0).sum()), mean_z=z.mean(), median_z=z.median(),
                      p_wilcoxon=stats.wilcoxon(z).pvalue if len(z) > 5 else np.nan,
                      p_sign=stats.binomtest(int((z > 0).sum()), len(z)).pvalue))
Bt = pd.DataFrame(rowsB)
print("\n=== B. Analysis screen: TRIM72 WT-minus-altered z among TRIM72 raisers vs other drug-doses ===")
print(Bt.round(4).to_string(index=False))
print(sc.loc[r, ["drug", "conc", "TRIM72_all_lines_fold_change", "TRIM72_wt_minus_altered_z", "P53_ACTIVITY_all_lines_z",
                 "P53_SCORE_wt_minus_altered_z"]].sort_values("TRIM72_wt_minus_altered_z").round(2).to_string(index=False))
Bt.to_csv(f"{OUT}/f4_screen_sign_among_raisers.csv", index=False)

# ---------------------------------------------------------------- C. low-expressed p53 targets as controls
tl = pd.read_csv(f"{ANA}/target_likeness_by_gene.csv").set_index("gene")
rowsC = []
for g in GEN:
    row = dict(gene=g, median_dmso_cpm=float(cpm_all[g].median()), n_lines_expr=int(expr[g].sum()),
               m1=tl.loc[g, "m1_spearman_delta_z_vs_p53score_delta_z"] if g in tl.index else np.nan,
               m2=tl.loc[g, "m2_mean_delta_z_top_p53_drugdoses"] if g in tl.index else np.nan)
    for drug, conc in [("Idarubicin (hydrochloride)", 5.0), ("Idarubicin (hydrochloride)", 0.5)]:
        x = drugdose_lines(drug, conc, g).dropna()
        w = base.reindex(x.index).tp53_group.eq("WT").to_numpy()
        sd = np.sqrt((np.var(x[w], ddof=1) * (w.sum() - 1) + np.var(x[~w], ddof=1) * ((~w).sum() - 1)) / (len(x) - 2))
        d, p = perm_diff(x.to_numpy(), w, B=2000)
        tag = "ida5" if conc == 5 else "ida05"
        row.update({f"{tag}_diff": d, f"{tag}_p": p, f"{tag}_sd": sd, f"{tag}_d_over_sd": d / sd,
                    f"{tag}_median_all": float(np.median(x))})
    rowsC.append(row)
C = pd.DataFrame(rowsC).sort_values("median_dmso_cpm")
print("\n=== C. p53 targets ordered by expression, next to TRIM72 (DMSO-ratio values; idarubicin 5 and 0.5 uM) ===")
print(C.round(3).to_string(index=False))
mem = C[C.gene != "TRIM72"]
print("Spearman over the 21 members, log CPM vs m1:", stats.spearmanr(np.log2(mem.median_dmso_cpm), mem.m1))
print("Spearman over the 21 members, log CPM vs ida5 d/sd:", stats.spearmanr(np.log2(mem.median_dmso_cpm), mem.ida5_d_over_sd))
C.to_csv(f"{OUT}/low_expressed_p53_targets_controls.csv", index=False)

# ---------------------------------------------------------------- D. within-organ permutation, idarubicin 5 uM
x = drugdose_lines("Idarubicin (hydrochloride)", 5.0, "TRIM72").dropna()
w = base.reindex(x.index).tp53_group.eq("WT").to_numpy()
org = base.reindex(x.index).Organ.fillna("NA").to_numpy()
d, p_all = perm_diff(x.to_numpy(), w)
_, p_org = perm_diff(x.to_numpy(), w, within=org)
mixed = [o for o in np.unique(org) if 0 < w[org == o].sum() < (org == o).sum()]
mm = np.isin(org, mixed)
d_mixed, p_mixed = perm_diff(x.to_numpy()[mm], w[mm], within=org[mm])
print("\n=== D. Idarubicin 5 uM TRIM72 (DMSO ratio, mean of the 2 wells): within-organ permutation ===")
print(dict(n=len(x), diff=round(d, 3), p_perm=round(p_all, 4), p_within_organ=round(p_org, 4),
           organs_with_both_groups=mixed, n_lines_in_mixed_organs=int(mm.sum()), n_wt_in_mixed=int(w[mm].sum()),
           diff_mixed_organs=round(d_mixed, 3), p_within_organ_mixed=round(p_mixed, 4)))

# ---------------------------------------------------------------- E. fine power grid with analysis per-line values
pl = pd.read_csv(f"{ANA}/per_line_effects_selected.csv")
q = pl[(pl.drug == "Idarubicin (hydrochloride)") & np.isclose(pl.conc, 5) & (pl.scope == "mean of used wells")]
rowsE = []
for g in ["TRIM72", "P53_SCORE", "MDM2"]:
    y = q[q.gene == g].dropna(subset=["log2FC_corrected"])
    v = y.log2FC_corrected.to_numpy(); lab = (y.tp53_group == "WT").to_numpy()
    res = np.concatenate([v[lab] - np.median(v[lab]), v[~lab] - np.median(v[~lab])])
    for dlt in [0.5, 0.67, 0.8, 0.9, 1.0, 1.1, 1.2]:
        hits = sum(stats.mannwhitneyu(RNG.choice(res, lab.sum()) + dlt, RNG.choice(res, (~lab).sum())).pvalue < 0.05
                   for _ in range(2000))
        rowsE.append(dict(gene=g, delta_log2=dlt, power=hits / 2000, n_wt=int(lab.sum()), n_alt=int((~lab).sum()),
                          pooled_sd=float(np.std(res, ddof=2))))
E = pd.DataFrame(rowsE).pivot_table(index=["gene", "n_wt", "n_alt", "pooled_sd"], columns="delta_log2", values="power")
print("\n=== E. Power (two-sided Mann-Whitney, alpha 0.05), analysis per-line values, idarubicin 5 uM mean of wells ===")
print(E.round(3).to_string())
E.to_csv(f"{OUT}/power_fine_grid_idarubicin5.csv")
