"""(1) dd-model confounding mechanism: between-group (WT-mean minus altered-mean) TRIM72 vs P53 gaps per drug-dose.
(2) inter-gene residual correlation among p53 targets (VIF for the member-vs-background Mann-Whitney)."""
import numpy as np, pandas as pd, indep as I
from scipy import stats
a = I.load()
act = a["in_ii_active"].to_numpy()
df = a[act].copy()
df = df[np.isfinite(df[["TRIM72_r2", "P53_SCORE"]]).all(axis=1)]
# line effects from the full panel (all drug-doses) as line means, then per drug-dose WT - altered gaps
for v in ("TRIM72_r2", "P53_SCORE"):
    lm = a.groupby("cell_line_id")[v].mean()
    df[v + "_adj"] = df[v] - df["cell_line_id"].map(lm)
g = df.groupby(["drugdose_row", "wt"])[["TRIM72_r2_adj", "P53_SCORE_adj"]].mean().unstack("wt")
gap = pd.DataFrame({"dX": g[("TRIM72_r2_adj", True)] - g[("TRIM72_r2_adj", False)],
                    "dY": g[("P53_SCORE_adj", True)] - g[("P53_SCORE_adj", False)]})
ds = pd.read_csv("../tables/drugdose_sets.csv")
gap["p53z"] = ds.loc[gap.index, "P53_ACTIVITY_z"].to_numpy()
gap["trimz"] = ds.loc[gap.index, "TRIM72_z"].to_numpy()
print("active drug-doses:", len(gap))
print("corr(dX, dY) = %.3f; slope dY on dX = %.3f" % (gap.dX.corr(gap.dY), np.polyfit(gap.dX, gap.dY, 1)[0]))
print("corr(dY, P53_ACTIVITY z) = %.3f; corr(dX, P53_ACTIVITY z) = %.3f" % (gap.dY.corr(gap.p53z), gap.dX.corr(gap.p53z)))
print("mean dY %.3f (WT-only p53 response), mean dX %.3f" % (gap.dY.mean(), gap.dX.mean()))
# (2) residual correlation among the 7 member genes present in analysis_cells (ddxg, full, active)
mem = ["MDM2", "CDKN1A", "FDXR", "ZMAT3", "DDB2", "TP53I3", "BBC3"]
sub = a[act]
cols = mem + ["TRIM72_r2"] + I.COVS["full"]
sub = I.drop_singletons(sub[np.isfinite(sub[cols]).all(axis=1)])
wt = sub["wt"].to_numpy()
g1 = sub["drugdose_row"].to_numpy() * 2 + wt
g2 = sub["cell_line_id"].to_numpy()
C = sub[I.COVS["full"]].to_numpy(float)
N = np.column_stack([C * wt[:, None], C * (~wt)[:, None], sub["TRIM72_r2"].to_numpy() * wt, sub["TRIM72_r2"].to_numpy() * ~wt])
V = I.demean2(np.column_stack([N, sub[mem].to_numpy(float)]), g1, g2)
Q = np.linalg.svd(V[:, :N.shape[1]], full_matrices=False)[0]
E = V[:, N.shape[1]:] - Q @ (Q.T @ V[:, N.shape[1]:])
x = V[:, N.shape[1] - 2] + V[:, N.shape[1] - 1]
Rm = np.corrcoef(E.T)
iu = np.triu_indices(len(mem), 1)
# correlation of the (x-weighted) per-line scores, which drive the t-statistics
lid = pd.factorize(g2)[0]
S = np.zeros((lid.max() + 1, len(mem)))
np.add.at(S, lid, E * x[:, None])
Rs = np.corrcoef(S.T)
rho_e, rho_s = Rm[iu].mean(), Rs[iu].mean()
print("7 members, active ddxg full: mean pairwise residual corr %.3f; mean pairwise line-score corr %.3f" % (rho_e, rho_s))
for rho in (rho_e, rho_s):
    vif = 1 + 20 * rho
    z = (-1.22031 - 0.239439) / (1.22003 / np.sqrt(21))
    print("rho %.3f -> VIF(21) %.2f; z independent %.2f (p %.1e) -> z/sqrt(VIF) %.2f (p %.3g)" % (
        rho, vif, z, 2 * stats.norm.sf(abs(z)), z / np.sqrt(vif), 2 * stats.norm.sf(abs(z / np.sqrt(vif)))))
