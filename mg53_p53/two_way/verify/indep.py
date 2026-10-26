"""Independent re-derivation of two_way's D1 estimates from tables/analysis_cells.csv.gz.

Own code path: alternating-projection (iterated group demeaning) two-way FE, explicit OLS on the demeaned
regressors, own CR1 cluster SEs (drug, line, two-way). No code from two_way.py is imported.
"""
import os
import sys
import numpy as np
import pandas as pd
from scipy import stats

HERE = os.path.dirname(os.path.abspath(__file__))
TAB = os.path.join(os.path.dirname(HERE), "tables")
COVS = {"full": ["beta", "A", "S", "G2M", "bg_abs_r2"], "none": [],
        "full_base": ["beta", "A", "S", "G2M", "bg_abs_r2", "trim72_base_x_dd"],
        "full_p53resp": ["beta", "A", "S", "G2M", "bg_abs_r2", "p53resp_x_dd"]}


def load():
    a = pd.read_csv(os.path.join(TAB, "analysis_cells.csv.gz"))
    a["wt"] = a["tp53_group"].eq("WT")
    a["drug_id"] = pd.factorize(a["drug"])[0]
    return a


def demean2(V, g1, g2, tol=1e-13, maxit=5000):
    """Iterated demeaning of the columns of V by two grouping vectors (alternating projections)."""
    V = V.copy()
    i1 = pd.factorize(g1)[0]
    i2 = pd.factorize(g2)[0]
    c1 = np.bincount(i1).astype(float)
    c2 = np.bincount(i2).astype(float)
    for it in range(maxit):
        old = V.copy()
        for idx, c in ((i1, c1), (i2, c2)):
            S = np.zeros((len(c), V.shape[1]))
            np.add.at(S, idx, V)
            V -= (S / c[:, None])[idx]
        if np.max(np.abs(V - old)) < tol:
            break
    return V


def drop_singletons(df):
    for _ in range(20):
        nd = df.groupby("drugdose_row")["wt"].transform("size")
        nl = df.groupby("cell_line_id")["wt"].transform("size")
        bad = (nd < 2) | (nl < 2)
        if not bad.any():
            break
        df = df[~bad]
    return df


def cr1(Xt, e, groups, bread, n, p):
    gid = pd.factorize(groups)[0]
    G = gid.max() + 1
    S = np.zeros((G, Xt.shape[1]))
    np.add.at(S, gid, Xt * e[:, None])
    c = G / (G - 1) * (n - 1) / (n - p)
    return c * bread @ (S.T @ S) @ bread, G


def model(a, y, x="TRIM72_r2", covset="full", fe="ddxg", mask=None, extra_covs=()):
    covs = COVS[covset] + list(extra_covs)
    df = a if mask is None else a[mask]
    df = df[np.isfinite(df[[x, y] + covs]).all(axis=1)]
    df = drop_singletons(df)
    n = len(df)
    wt = df["wt"].to_numpy()
    X = df[x].to_numpy(float)
    C = df[covs].to_numpy(float) if covs else np.zeros((n, 0))
    regs = np.column_stack([X * wt, X * ~wt] + [C[:, j] * wt for j in range(C.shape[1])]
                           + [C[:, j] * ~wt for j in range(C.shape[1])])
    yv = df[y].to_numpy(float)
    g1 = df["drugdose_row"].to_numpy() * 2 + (wt if fe == "ddxg" else 0)
    g2 = df["cell_line_id"].to_numpy()
    D = demean2(np.column_stack([regs, yv]), g1, g2)
    R, yt = D[:, :-1], D[:, -1]
    bread = np.linalg.pinv(R.T @ R)
    b = bread @ R.T @ yt
    e = yt - R @ b
    nfe = len(np.unique(g1)) + len(np.unique(g2)) - 1
    p = R.shape[1] + nfe
    Vd, Gd = cr1(R, e, df["drug_id"].to_numpy(), bread, n, p)
    Vl, Gl = cr1(R, e, g2, bread, n, p)
    Vi, _ = cr1(R, e, df["drug_id"].astype(str).to_numpy() + "|" + g2, bread, n, p)
    c = np.zeros(R.shape[1])
    c[0], c[1] = 1, -1
    dif = b[0] - b[1]
    vd, vl, vi = c @ Vd @ c, c @ Vl @ c, c @ Vi @ c
    v2 = vd + vl - vi
    se2 = np.sqrt(v2) if v2 > 0 else np.sqrt(max(vd, vl))
    df_ = min(Gd, Gl) - 1
    out = {"n": n, "n_dd": df["drugdose_row"].nunique(), "n_WT_lines": df.loc[df.wt, "cell_line_id"].nunique(),
           "n_alt_lines": df.loc[~df.wt, "cell_line_id"].nunique(), "b_WT": b[0], "b_alt": b[1], "diff": dif,
           "se_drug": np.sqrt(vd), "se_line": np.sqrt(vl), "se_twoway": se2, "se_max_oneway": np.sqrt(max(vd, vl)),
           "p_twoway": 2 * stats.t.sf(abs(dif / se2), df_), "p_line": 2 * stats.t.sf(abs(dif / np.sqrt(vl)), Gl - 1),
           "p_drug": 2 * stats.t.sf(abs(dif / np.sqrt(vd)), Gd - 1),
           "p_conservative": 2 * stats.t.sf(abs(dif / max(se2, np.sqrt(vd), np.sqrt(vl))), df_),
           "t_line": dif / np.sqrt(vl), "t_twoway": dif / se2, "G_drug": Gd, "G_line": Gl}
    return out, df, R, yt, e


if __name__ == "__main__":
    a = load()
    rows = []
    act = a["in_ii_active"].to_numpy()
    for fe in ("dd", "ddxg"):
        for vname, m in (("i_all", None), ("ii_active", act)):
            for cs in ("full", "none", "full_base", "full_p53resp"):
                for y in ("P53_SCORE", "MDM2", "CDKN1A", "ZMAT3", "FDXR"):
                    o = model(a, y, covset=cs, fe=fe, mask=m)[0]
                    rows.append({"fe": fe, "variant": vname, "covset": cs, "readout": y} | o)
                    print(fe, vname, cs, y, {k: round(v, 5) if isinstance(v, float) else v for k, v in o.items()},
                          flush=True)
    pd.DataFrame(rows).to_csv(os.path.join(HERE, "indep_main.csv"), index=False)
