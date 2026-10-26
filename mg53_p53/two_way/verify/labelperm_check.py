"""Own TP53-label permutation (ddxg, full, ii_active, P53_SCORE): permute group labels over lines, refit everything."""
import numpy as np, pandas as pd, indep as I
a = I.load()
act = a["in_ii_active"].to_numpy()
sub = a[act].copy()
o = I.model(sub, "P53_SCORE", covset="full", fe="ddxg")[0]
# lines analysed (with full covariates): 17 WT + 30 altered
ok = np.isfinite(sub[["TRIM72_r2", "P53_SCORE"] + I.COVS["full"]]).all(axis=1)
lines = sub.loc[ok, ["cell_line_id", "wt"]].drop_duplicates()
L, W = lines["cell_line_id"].to_numpy(), lines["wt"].to_numpy()
rng = np.random.default_rng(11)
B = 1000
tn, dn = [], []
for b in range(B):
    perm = dict(zip(L, rng.permutation(W)))
    s2 = sub.copy()
    s2["wt"] = s2["cell_line_id"].map(perm).fillna(False).astype(bool)
    r = I.model(s2, "P53_SCORE", covset="full", fe="ddxg")[0]
    tn.append(r["t_line"]); dn.append(r["diff"])
tn, dn = np.array(tn), np.array(dn)
print("obs diff %.4f t_line %.3f" % (o["diff"], o["t_line"]))
print("label-perm p (studentised) %.4f; unstudentised %.4f; null SD of diff %.4f; MDE 2.8 x SD %.4f" % (
    (1 + (np.abs(tn) >= abs(o["t_line"])).sum()) / (B + 1), (1 + (np.abs(dn) >= abs(o["diff"])).sum()) / (B + 1),
    dn.std(), 2.8 * dn.std()))
print("null t_line SD %.3f, mean %.3f; null diff mean %.4f" % (tn.std(), tn.mean(), dn.mean()))
