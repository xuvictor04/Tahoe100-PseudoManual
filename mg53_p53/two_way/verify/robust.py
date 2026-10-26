"""Adversarial robustness checks of the two_way headline (ii_active, P53_SCORE), own code (indep.py)."""
import os
import sys
import time
import numpy as np
import pandas as pd
from scipy import stats

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import indep as I  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
rng = np.random.default_rng(7)
a = I.load()
act = a["in_ii_active"].to_numpy()
what = sys.argv[1] if len(sys.argv) > 1 else "all"
out = {}


def log(*x):
    print(time.strftime("%H:%M:%S"), *x, flush=True)


# ---------------------------------------------------------------- (a) leave-one-line-out, (b) leave-one-drug-out
if what in ("all", "loo"):
    rows = []
    for fe in ("ddxg", "dd"):
        for cs in ("full", "none"):
            base = I.model(a, "P53_SCORE", covset=cs, fe=fe, mask=act)[0]
            lines = a.loc[act, ["cell_line_id", "cell_line", "tp53_group"]].drop_duplicates()
            for _, L in lines.iterrows():
                o = I.model(a, "P53_SCORE", covset=cs, fe=fe, mask=act & (a["cell_line_id"] != L.cell_line_id).to_numpy())[0]
                rows.append({"kind": "leave_one_line_out", "fe": fe, "covset": cs, "dropped": L.cell_line,
                             "dropped_group": L.tp53_group, "diff_all": base["diff"]} | o)
            for dr in a.loc[act, "drug"].unique():
                o = I.model(a, "P53_SCORE", covset=cs, fe=fe, mask=act & (a["drug"] != dr).to_numpy())[0]
                rows.append({"kind": "leave_one_drug_out", "fe": fe, "covset": cs, "dropped": dr,
                             "diff_all": base["diff"]} | o)
            log("loo", fe, cs)
    R = pd.DataFrame(rows)
    R.to_csv(os.path.join(HERE, "robust_loo.csv"), index=False)
    for (k, fe, cs), g in R.groupby(["kind", "fe", "covset"]):
        i = g["p_line"].idxmax()
        print(k, fe, cs, "diff range %.4f..%.4f; max p_twoway %.4f; max p_line %.4f (drop %s); max p_cons %.4f" % (
            g["diff"].min(), g["diff"].max(), g["p_twoway"].max(), g["p_line"].max(), g.loc[i, "dropped"],
            g["p_conservative"].max()))
        print("   n with p_line > 0.05:", int((g["p_line"] > 0.05).sum()), "of", len(g),
              "; p_cons > 0.05:", int((g["p_conservative"] > 0.05).sum()))

# ---------------------------------------------------------------- (c) covariates: drop one, add one
if what in ("all", "cov"):
    rows = []
    full = I.COVS["full"]
    sets = {"full": full, "none": []}
    for c in full:
        sets[f"full minus {c}"] = [x for x in full if x != c]
        sets[f"only {c}"] = [c]
    sets["full + FUS + PYCARD-AS1 (readthrough as covariates)"] = full + ["FUS_r2", "PYCARD-AS1_r2"]
    sets["full + trim72_base_x_dd + p53resp_x_dd"] = full + ["trim72_base_x_dd", "p53resp_x_dd"]
    for fe in ("ddxg", "dd"):
        for vname, m in (("ii_active", act), ("i_all", None)):
            for nm, cs in sets.items():
                I.COVS["_tmp"] = cs
                o = I.model(a, "P53_SCORE", covset="_tmp", fe=fe, mask=m)[0]
                rows.append({"fe": fe, "variant": vname, "covariates": nm} | o)
            log("cov", fe, vname)
    # readthrough variant as in two_way (X = TRIM72_rt) next to it
    for fe in ("ddxg", "dd"):
        for vname, m in (("ii_active", act), ("i_all", None)):
            o = I.model(a, "P53_SCORE", x="TRIM72_rt", covset="full", fe=fe, mask=m)[0]
            rows.append({"fe": fe, "variant": vname, "covariates": "full, X = TRIM72_rt (two_way's variant iii)"} | o)
    R = pd.DataFrame(rows)
    R.to_csv(os.path.join(HERE, "robust_covariates.csv"), index=False)
    print(R[["fe", "variant", "covariates", "n", "diff", "p_twoway", "p_line", "p_conservative"]].to_string())

# ---------------------------------------------------------------- (d) placebo: random splits inside one TP53 group
if what in ("all", "placebo"):
    rows = []
    for vname, m, B in (("ii_active", act, 400), ("i_all", None, 60)):
        for grp, nA in (("altered", 15), ("WT", 9)):
            sub = a if m is None else a[m]
            sub = sub[sub["tp53_group"] == grp].copy()
            L = sub["cell_line_id"].unique()
            for b in range(B):
                pick = set(rng.choice(L, nA, replace=False))
                sub["wt"] = sub["cell_line_id"].isin(pick)
                for y in ("P53_SCORE",):
                    o = I.model(sub, y, covset="full", fe="ddxg")[0]
                    rows.append({"variant": vname, "group_split": grp, "rep": b, "readout": y} | o)
            log("placebo", vname, grp)
    R = pd.DataFrame(rows)
    R.to_csv(os.path.join(HERE, "robust_placebo.csv"), index=False)
    for (v, g), x in R.groupby(["variant", "group_split"]):
        print(v, g, len(x), "SD t_twoway %.2f, SD t_line %.2f; reject 5%%: twoway %.3f line %.3f cons %.3f drug %.3f"
              % (x.t_twoway.std(), x.t_line.std(), (x.p_twoway < .05).mean(), (x.p_line < .05).mean(),
                 (x.p_conservative < .05).mean(), (x.p_drug < .05).mean()))

# ---------------------------------------------------------------- (e) wild cluster restricted bootstrap by line
if what in ("all", "wcb"):
    res = []
    for vname, m in (("ii_active", act), ("i_all", None)):
        for cs in ("full", "none"):
            o, df, R, yt, e = I.model(a, "P53_SCORE", covset=cs, fe="ddxg", mask=m)
            covs = I.COVS[cs]
            wt = df["wt"].to_numpy()
            n = len(df)
            C = df[covs].to_numpy(float) if covs else np.zeros((n, 0))
            g1 = df["drugdose_row"].to_numpy() * 2 + wt
            g2 = df["cell_line_id"].to_numpy()
            Cn = np.column_stack([C[:, j] * wt for j in range(C.shape[1])] + [C[:, j] * ~wt for j in range(C.shape[1])]) \
                if covs else np.zeros((n, 0))
            Cd = I.demean2(Cn, g1, g2) if covs else Cn
            Qc = np.linalg.svd(Cd, full_matrices=False)[0] if covs else np.zeros((n, 0))
            x1, x2 = R[:, 0], R[:, 1]
            # restricted fit (b_WT = b_alt) on the partialled data
            xs = x1 + x2
            bc = xs @ yt / (xs @ xs)
            er = yt - bc * xs
            lid = pd.factorize(g2)[0]
            G = lid.max() + 1
            Bn = 999
            W = rng.choice([-1.0, 1.0], size=(G, Bn))
            Ys = bc * xs[:, None] + er[:, None] * W[lid]
            Ys = I.demean2(Ys, g1, g2, tol=1e-12)
            if Qc.shape[1]:
                Ys = Ys - Qc @ (Qc.T @ Ys)
            RR = R[:, :2]
            bread = np.linalg.inv(RR.T @ RR)
            Bt = bread @ RR.T @ Ys
            E = Ys - RR @ Bt
            S = np.zeros((G, 2, Bn))
            for k in range(2):
                np.add.at(S[:, k, :], lid, RR[:, [k]] * E)
            c = np.array([1.0, -1.0])
            w = bread @ c
            sc = np.einsum("k,gkb->gb", w, S)
            p_all = 2 + 2 * len(covs) + len(np.unique(g1)) + G - 1
            cf = G / (G - 1) * (n - 1) / (n - p_all)
            se = np.sqrt(cf * (sc ** 2).sum(0))
            tb = (Bt[0] - Bt[1]) / se
            p = (1 + (np.abs(tb) >= abs(o["t_line"])).sum()) / (Bn + 1)
            res.append({"variant": vname, "covset": cs, "diff": o["diff"], "t_line": o["t_line"],
                        "p_line_t46": o["p_line"], "p_wild_cluster_line_bootstrap": p, "B": Bn})
            log("wcb", vname, cs, res[-1])
    pd.DataFrame(res).to_csv(os.path.join(HERE, "robust_wcb.csv"), index=False)
