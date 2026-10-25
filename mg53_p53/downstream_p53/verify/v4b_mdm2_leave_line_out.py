#!/usr/bin/env python3
"""F3: does one TP53-WT line drive the pooled TRIM72_r2 vs MDM2 association over the 13 TRIM72 raisers?
Leave-one-line-out of the mean Spearman (Fisher z average), unadjusted and with DD_beta + DD_A partialled out; and the
same with the treated TRIM72 level (log2 CPM, cache Y) as predictor instead of the fold change.

    python3 verify/v4b_mdm2_leave_line_out.py -> verify/out/v4b_mdm2_leave_line_out.csv
"""
import os
import warnings
import numpy as np
import pandas as pd
from scipy import stats

warnings.simplefilter("ignore")
DATA = "/home/user/tahoe_data"
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(HERE, "out")
z = np.load(os.path.join(ROOT, "cache", "effects.npz"))
genes = [str(g) for g in z["genes"]]
samples = [str(s) for s in z["samples"]]
lines = [str(l) for l in z["lines"]]
R2, Y = z["R2"].astype(float), z["Y"].astype(float)
gi = {g: i for i, g in enumerate(genes)}
si = {s: i for i, s in enumerate(samples)}
W = pd.read_csv(os.path.join(ROOT, "cache", "wells.csv"), dtype={"sample": str}).set_index("sample")
L = pd.read_csv(os.path.join(ROOT, "cache", "lines.csv")).set_index("cell_line_id").reindex(lines)
nm = pd.read_csv(os.path.join(DATA, "atlas", "effects", "lines.csv")).set_index("cell_line_id").cell_name
wt = np.where((L.tp53_group == "WT").to_numpy())[0]
sel = pd.read_csv(os.path.join(ROOT, "tables", "a_selected_drugdoses.csv"))
rais = sel[sel.role.str.startswith("TRIM72 raiser")][["drug", "conc"]].values.tolist()
dd = pd.read_csv(os.path.join(DATA, "atlas", "effects", "drugdose.csv"))
alines = pd.read_csv(os.path.join(DATA, "atlas", "effects", "lines.csv")).cell_line_id.astype(str).tolist()
DDb = np.load(os.path.join(DATA, "atlas", "effects", "DD_beta.npy"), mmap_mode="r")
DDA = np.load(os.path.join(DATA, "atlas", "effects", "DD_A.npy"), mmap_mode="r")

tabs = []
for d, c in rais:
    w = W[(W.drug == d) & np.isclose(W.conc.astype(float), c) & ~W.is_dmso & W.used]
    ii = [si[s] for s in w.index]
    r = int(dd.index[(dd.drug == d) & np.isclose(dd.conc, c)][0])
    Z = np.column_stack([pd.Series(np.asarray(DDb[r]), index=alines).reindex(lines).to_numpy(),
                         pd.Series(np.asarray(DDA[r]), index=alines).reindex(lines).to_numpy()])
    tabs.append(dict(r2=np.nanmean(R2[gi["TRIM72"]][ii], axis=0), lev=np.nanmean(Y[gi["TRIM72"]][ii], axis=0),
                     mdm2=np.nanmean(R2[gi["MDM2"]][ii], axis=0), Z=Z))


def prho(x, y, Z):
    ok = np.isfinite(x) & np.isfinite(y)
    if Z is not None:
        ok &= np.isfinite(Z).all(1)
    if ok.sum() < 8:
        return np.nan
    a, b = stats.rankdata(x[ok]), stats.rankdata(y[ok])
    if Z is not None:
        X = np.column_stack([np.ones(ok.sum())] + [stats.rankdata(Z[ok, j]) for j in range(Z.shape[1])])
        a = a - X @ np.linalg.lstsq(X, a, rcond=None)[0]
        b = b - X @ np.linalg.lstsq(X, b, rcond=None)[0]
    return np.corrcoef(a, b)[0, 1]


rows = []
for pred in ("r2", "lev"):
    for adj in ("none", "beta+A"):
        def pooled(idx):
            zs = [np.arctanh(prho(t[pred][idx], t["mdm2"][idx], None if adj == "none" else t["Z"][idx])) for t in tabs]
            return float(np.tanh(np.nanmean(zs)))
        full = pooled(wt)
        rows.append(dict(predictor=pred, adjust=adj, left_out="none", mean_rho=full))
        for j in wt:
            rows.append(dict(predictor=pred, adjust=adj, left_out=nm.get(lines[j], lines[j]),
                             mean_rho=pooled(wt[wt != j])))
R = pd.DataFrame(rows)
R.to_csv(os.path.join(OUT, "v4b_mdm2_leave_line_out.csv"), index=False)
print(R.groupby(["predictor", "adjust"]).mean_rho.agg(["first", "min", "max"]).round(3))
print(R[(R.predictor == "r2") & (R.adjust == "none")].sort_values("mean_rho").round(3).to_string())
