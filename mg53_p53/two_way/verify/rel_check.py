"""Split-half reliability of residual TRIM72 (own code) and readthrough fit (own code)."""
import numpy as np, pandas as pd, indep as I
a = I.load()
act = a["in_ii_active"].to_numpy()
for vname, m in (("i_all", np.ones(len(a), bool)), ("ii_active", act), ("ii_trim72", a["in_ii_trim72"].to_numpy())):
    for fe in ("dd", "ddxg"):
        df = a[m]
        cols = ["TRIM72_r2", "TRIM72_r2_halfA", "TRIM72_r2_halfB"] + I.COVS["full"]
        df = I.drop_singletons(df[np.isfinite(df[cols]).all(axis=1)])
        wt = df["wt"].to_numpy()
        g1 = df["drugdose_row"].to_numpy() * 2 + (wt if fe == "ddxg" else 0)
        g2 = df["cell_line_id"].to_numpy()
        C = df[I.COVS["full"]].to_numpy(float)
        N = np.column_stack([C * wt[:, None], C * (~wt)[:, None]])
        V = I.demean2(np.column_stack([N, df[["TRIM72_r2_halfA", "TRIM72_r2_halfB", "TRIM72_r2"]].to_numpy(float)]), g1, g2)
        Q = np.linalg.svd(V[:, :N.shape[1]], full_matrices=False)[0]
        Rr = V[:, N.shape[1]:] - Q @ (Q.T @ V[:, N.shape[1]:])
        out = []
        for gn, mm in (("all", np.ones(len(df), bool)), ("WT", wt), ("alt", ~wt)):
            r = np.corrcoef(Rr[mm, 0], Rr[mm, 1])[0, 1]
            rf = np.corrcoef(Rr[mm, 2], Rr[mm, 0])[0, 1]
            out.append(f"{gn}: r_halves {r:.3f} SB {2*r/(1+r):.3f} (corr full vs halfA {rf:.3f})")
        print(vname, fe, len(df), "; ".join(out))
# readthrough fit (dd + line FE, all lines one group)
df = a[np.isfinite(a[["TRIM72_r2", "FUS_r2", "PYCARD-AS1_r2"]]).all(axis=1)]
df = I.drop_singletons(df)
V = I.demean2(df[["TRIM72_r2", "FUS_r2", "PYCARD-AS1_r2"]].to_numpy(float), df["drugdose_row"].to_numpy(), df["cell_line_id"].to_numpy())
b, *_ = np.linalg.lstsq(V[:, 1:], V[:, 0], rcond=None)
e = V[:, 0] - V[:, 1:] @ b
print("readthrough slopes", b, "within R2", 1 - e @ e / (V[:, 0] @ V[:, 0]), "n", len(df))
rt = df["TRIM72_r2"] - b[0] * df["FUS_r2"] - b[1] * df["PYCARD-AS1_r2"]
print("max |rt - TRIM72_rt (table, 4 s.f.)|", np.nanmax(np.abs(rt - df["TRIM72_rt"])), "median rel", np.nanmedian(np.abs(rt - df["TRIM72_rt"]) / np.abs(df["TRIM72_rt"])))
