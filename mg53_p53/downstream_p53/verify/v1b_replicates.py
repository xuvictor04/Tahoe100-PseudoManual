#!/usr/bin/env python3
"""F1 'not blind' check: is the plate-6 vs plate-14 reproducibility of per-line TRIM72 induction under idarubicin 5 uM
just the reproducible UNTREATED TRIM72 level (fold change = treated - baseline)? Partial Spearman of the two wells'
TRIM72 r2 with the line's untreated level partialled out, and the same for the treated level and P53_SCORE.
Also TRIM72 treated level vs P53_SCORE (the analysis computed it but did not report it).
Reads cache/effects.npz (method-v3 r2 and log2 CPM y per well x line) and cache/lines.csv.

    python3 verify/v1b_replicates.py -> verify/out/v1b_replicates.csv
"""
import os
import numpy as np
import pandas as pd
from scipy import stats

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(HERE, "out")
P53 = ["CDKN1A", "MDM2", "FDXR", "ZMAT3", "SESN1", "BBC3", "BAX", "TP53I3", "RRM2B", "AEN", "DDB2", "XPC", "PHLDA3",
       "SPATA18", "TRIAP1", "RPS27L", "ACER2", "TP53INP1", "PLK3", "POLH", "EDA2R"]
z = np.load(os.path.join(ROOT, "cache", "effects.npz"))
genes = [str(g) for g in z["genes"]]
samples = [str(s) for s in z["samples"]]
lines = [str(l) for l in z["lines"]]
gi = {g: i for i, g in enumerate(genes)}
si = {s: i for i, s in enumerate(samples)}
R2, Y = z["R2"].astype(float), z["Y"].astype(float)
L = pd.read_csv(os.path.join(ROOT, "cache", "lines.csv")).set_index("cell_line_id").reindex(lines)
base = np.log2(L["cpm_dmso_TRIM72"].to_numpy(float) + 0.1)
w6, w14 = si["smp_2010"], si["smp_2778"]
with np.errstate(all="ignore"):
    import warnings
    warnings.simplefilter("ignore")
    p53_6 = np.nanmean(R2[[gi[g] for g in P53], w6, :], axis=0)
    p53_14 = np.nanmean(R2[[gi[g] for g in P53], w14, :], axis=0)


def pspear(x, y, Z=None):
    ok = np.isfinite(x) & np.isfinite(y)
    if Z is not None:
        ok &= np.isfinite(Z)
    a, b = stats.rankdata(x[ok]), stats.rankdata(y[ok])
    if Z is not None:
        X = np.column_stack([np.ones(ok.sum()), stats.rankdata(Z[ok])])
        a = a - X @ np.linalg.lstsq(X, a, rcond=None)[0]
        b = b - X @ np.linalg.lstsq(X, b, rcond=None)[0]
    r = np.corrcoef(a, b)[0, 1]
    n = ok.sum()
    t = r * np.sqrt((n - 3) / (1 - r * r))
    return int(n), float(r), float(2 * stats.t.sf(abs(t), n - 3))


rows = []
for grp in ("WT", "altered"):
    m = (L.tp53_group == grp).to_numpy()
    feats = {"TRIM72_r2": (R2[gi["TRIM72"], w6], R2[gi["TRIM72"], w14]),
             "TRIM72_treated_log2cpm": (Y[gi["TRIM72"], w6], Y[gi["TRIM72"], w14]),
             "P53_SCORE": (p53_6, p53_14)}
    for f, (a, b) in feats.items():
        for adj in ("none", "untreated TRIM72"):
            n, r, p = pspear(a[m], b[m], base[m] if adj != "none" else None)
            rows.append(dict(test="replicate plate6 vs plate14", group=grp, feature=f, adjust=adj, n=n, rho=r, p=p))
    # TRIM72 r2 vs untreated level, within each well
    for wn, w in (("plate6", w6), ("plate14", w14)):
        n, r, p = pspear(R2[gi["TRIM72"], w][m], base[m])
        rows.append(dict(test=f"TRIM72_r2 vs untreated level ({wn})", group=grp, feature="TRIM72_r2", adjust="none",
                         n=n, rho=r, p=p))
pd.DataFrame(rows).to_csv(os.path.join(OUT, "v1b_replicates.csv"), index=False)
print(pd.DataFrame(rows).round(3).to_string())
