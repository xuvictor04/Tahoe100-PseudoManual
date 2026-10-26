"""Is the ii_active pattern specific to active drug-doses, or the same slope with less noise? ddxg, full covariates."""
import numpy as np, pandas as pd, indep as I
a = I.load()
act = a["in_ii_active"].to_numpy()
o_in = I.model(a, "P53_SCORE", covset="full", fe="ddxg", mask=~act)[0]
o_ac = I.model(a, "P53_SCORE", covset="full", fe="ddxg", mask=act)[0]
print("inactive (%d dd): diff %+.4f se_line %.4f se2 %.4f p2 %.3f" % (o_in["n_dd"], o_in["diff"], o_in["se_line"], o_in["se_twoway"], o_in["p_twoway"]))
print("active (%d dd): diff %+.4f se_line %.4f se2 %.4f p2 %.3f" % (o_ac["n_dd"], o_ac["diff"], o_ac["se_line"], o_ac["se_twoway"], o_ac["p_twoway"]))
# interaction: one model with TRIM72 x group x active (FE ddxg; covariates x group x active)
df = a[np.isfinite(a[["TRIM72_r2", "P53_SCORE"] + I.COVS["full"]]).all(axis=1)].copy()
df = I.drop_singletons(df)
wt = df["wt"].to_numpy(); ac = df["in_ii_active"].to_numpy()
X = df["TRIM72_r2"].to_numpy(float); C = df[I.COVS["full"]].to_numpy(float)
cols = []
for g in (wt & ac, ~wt & ac, wt & ~ac, ~wt & ~ac):
    cols.append(X * g)
for g in (wt & ac, ~wt & ac, wt & ~ac, ~wt & ~ac):
    cols += [C[:, j] * g for j in range(C.shape[1])]
M = np.column_stack(cols + [df["P53_SCORE"].to_numpy(float)])
g1 = df["drugdose_row"].to_numpy() * 2 + wt
D = I.demean2(M, g1, df["cell_line_id"].to_numpy())
R, y = D[:, :-1], D[:, -1]
bread = np.linalg.pinv(R.T @ R); b = bread @ R.T @ y; e = y - R @ b
n, p = len(y), R.shape[1] + len(np.unique(g1)) + df["cell_line_id"].nunique() - 1
c = np.zeros(R.shape[1]); c[[0, 1, 2, 3]] = [1, -1, -1, 1]
out = {}
for nm, grp in (("drug", df["drug_id"].to_numpy()), ("line", df["cell_line_id"].to_numpy()), ("inter", df["drug_id"].astype(str).to_numpy() + df["cell_line_id"].to_numpy())):
    V, G = I.cr1(R, e, grp, bread, n, p); out[nm] = (c @ V @ c, G)
v2 = out["drug"][0] + out["line"][0] - out["inter"][0]
se = np.sqrt(max(v2, out["drug"][0], out["line"][0]))
from scipy import stats
dd = c @ b
print("difference-in-diff (active minus inactive): %+.4f, conservative SE %.4f, p %.3f; line-SE p %.3f" % (dd, se, 2 * stats.t.sf(abs(dd / se), 46), 2 * stats.t.sf(abs(dd / np.sqrt(out['line'][0])), 46)))
# the active-set diff inside the joint model (line FE estimated from all 1,132 drug-doses)
from scipy import stats as st
for nm_, cc in (("active diff, joint model (line FE from all drug-doses)", [1, -1, 0, 0]), ("inactive diff, joint model", [0, 0, 1, -1])):
    c = np.zeros(R.shape[1]); c[[0, 1, 2, 3]] = cc
    vv = {}
    for nm, grp in (("drug", df["drug_id"].to_numpy()), ("line", df["cell_line_id"].to_numpy()), ("inter", df["drug_id"].astype(str).to_numpy() + df["cell_line_id"].to_numpy())):
        V, G = I.cr1(R, e, grp, bread, n, p); vv[nm] = c @ V @ c
    v2 = vv["drug"] + vv["line"] - vv["inter"]
    se2 = np.sqrt(v2) if v2 > 0 else np.sqrt(max(vv["drug"], vv["line"]))
    sec = max(se2, np.sqrt(vv["drug"]), np.sqrt(vv["line"]))
    est = c @ b
    print("%s: %+.4f; two-way p %.3f; line p %.3f; conservative p %.3f" % (nm_, est, 2 * st.t.sf(abs(est / se2), 46),
          2 * st.t.sf(abs(est / np.sqrt(vv['line'])), 46), 2 * st.t.sf(abs(est / sec), 46)))
