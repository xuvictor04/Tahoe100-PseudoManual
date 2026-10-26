"""dd estimate = precision-weighted mix of the ddxg (within-group) estimate and a between-group estimate (WT-mean minus
altered-mean gaps per drug-dose). Exact decomposition with projections, no covariates."""
import numpy as np, pandas as pd, indep as I
a = I.load()
for vname, m in (("ii_active", a["in_ii_active"].to_numpy()), ("ii_trim72", a["in_ii_trim72"].to_numpy()), ("ii_p53", a["in_ii_p53"].to_numpy()), ("i_all", np.ones(len(a), bool))):
    df = a[m]
    df = I.drop_singletons(df[np.isfinite(df[["TRIM72_r2", "P53_SCORE"]]).all(axis=1)])
    wt = df["wt"].to_numpy()
    X = df["TRIM72_r2"].to_numpy(float); Y = df["P53_SCORE"].to_numpy(float)
    V = np.column_stack([X * wt, X * ~wt, Y])
    g2 = df["cell_line_id"].to_numpy()
    Rdd = I.demean2(V, df["drugdose_row"].to_numpy(), g2)
    Rx = I.demean2(V, df["drugdose_row"].to_numpy() * 2 + wt, g2)
    Bc = Rdd - Rx                                   # between-group (dd x WT dummy) component
    Wm, Bm = Rx[:, :2], Bc[:, :2]
    bw = np.linalg.solve(Wm.T @ Wm, Wm.T @ Rx[:, 2])
    bb = np.linalg.lstsq(Bm, Bc[:, 2], rcond=None)[0]
    bd = np.linalg.solve(Rdd[:, :2].T @ Rdd[:, :2], Rdd[:, :2].T @ Rdd[:, 2])
    share = np.trace(Bm.T @ Bm) / np.trace(Rdd[:, :2].T @ Rdd[:, :2])
    print(f"{vname}: dd diff {bd[0]-bd[1]:+.4f} (b_WT {bd[0]:+.4f}, b_alt {bd[1]:+.4f}); within (ddxg) diff {bw[0]-bw[1]:+.4f}; "
          f"between-group diff {bb[0]-bb[1]:+.4f} (b_WT {bb[0]:+.4f}, b_alt {bb[1]:+.4f}); between share of regressor SS {share:.3f}")
