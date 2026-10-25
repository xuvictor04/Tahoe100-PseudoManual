#!/usr/bin/env python3
"""F5 background: is TRIM72's across-drug-dose correlation with the p53 score (and with the WT-minus-altered contrast,
PMAIP1, ATF3, CDKN1A) unusual among all genes, or what any gene of similar expression shows?

Atlas DD_z (1,132 drug-doses x 16,643 genes). For every gene expressed in >= 25 lines: Spearman of its z with
P53 score (mean atlas z of the 21 P53_ACTIVITY members), with the panel's WT-minus-altered p53 contrast, and with the
general activity of the drug-dose (atlas n_sig_genes). Percentile of TRIM72 among all genes and among genes with a
similar median line CPM (2-8 CPM) and among genes with a similar plate batch pattern is not possible from DD_z alone, so
the low-baseline-plate drug-doses are also analysed separately.

    python3 verify/v3b_genome_background.py -> verify/out/v3b_*.csv
"""
import os
import numpy as np
import pandas as pd
from scipy import stats

DATA = "/home/user/tahoe_data"
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
E = os.path.join(DATA, "atlas", "effects")
P53 = ["CDKN1A", "MDM2", "FDXR", "ZMAT3", "SESN1", "BBC3", "BAX", "TP53I3", "RRM2B", "AEN", "DDB2", "XPC", "PHLDA3",
       "SPATA18", "TRIAP1", "RPS27L", "ACER2", "TP53INP1", "PLK3", "POLH", "EDA2R"]

M = pd.read_csv(os.path.join(OUT, "v3_drugdose_inputs.csv"))       # written by v3_drugdose.py (same row order)
dd = pd.read_csv(os.path.join(E, "drugdose.csv"))
assert (dd.drug.values == M.drug.values).all() and np.allclose(dd.conc.values, M.conc.values)
ga = pd.read_csv(os.path.join(E, "genes.csv"))
G = ga[(ga.kind == "gene") & (ga.n_lines_expressing >= 25)].drop_duplicates("symbol")
Z = np.asarray(np.load(os.path.join(E, "DD_z.npy"), mmap_mode="r")[:, G.col.to_numpy()], dtype=np.float64)
Z = np.nan_to_num(Z)


def rank_cols(X):
    return np.apply_along_axis(stats.rankdata, 0, X)


def spearman_vec(X, y, rows):
    Rx = rank_cols(X[rows])
    ry = stats.rankdata(y[rows])
    Rx = Rx - Rx.mean(0)
    ry = ry - ry.mean()
    return (Rx * ry[:, None]).sum(0) / np.sqrt((Rx ** 2).sum(0) * (ry ** 2).sum())


ys = {"P53_az": M.P53_az.to_numpy(), "p53_WT_minus_altered_z": M.p53_WT_minus_altered_z.to_numpy(),
      "activity_n_sig_genes": M.n_sig_genes.to_numpy().astype(float)}
subsets = {"all": np.ones(len(M), bool),
           "low-baseline plates 4-12": (M.plate_set == "low-baseline plate (4-12)").to_numpy(),
           "high-baseline plates 1-3": (M.plate_set == "high-baseline plate (1-3)").to_numpy(),
           "plates 6+14": (M.plate_set == "plates 6+14 (2 wells)").to_numpy()}
sym = G.symbol.to_numpy()
cpm = G.median_line_cpm.to_numpy()
notp53 = ~np.isin(sym, P53 + ["TP53"])
matched = notp53 & (cpm >= 2) & (cpm <= 8)
it = int(np.where(sym == "TRIM72")[0][0])
rows, per_gene = [], {}
for sname, m in subsets.items():
    for yname, y in ys.items():
        r = spearman_vec(Z, y, m)
        per_gene[(sname, yname)] = r
        for bg_name, bg in (("all expressed non-p53 genes", notp53), ("expression-matched (2-8 CPM)", matched)):
            v = r[bg & (np.arange(len(r)) != it)]
            rows.append(dict(subset=sname, n_drugdoses=int(m.sum()), y=yname, background=bg_name, n_genes=len(v),
                             rho_TRIM72=r[it], bg_median=np.median(v), bg_p05=np.quantile(v, .05),
                             bg_p95=np.quantile(v, .95), pct_TRIM72=100 * (v < r[it]).mean()))
B = pd.DataFrame(rows)
B.to_csv(os.path.join(OUT, "v3b_background.csv"), index=False)
# TRIM72's rho with the p53 score after its rho with general activity: residual of the across-gene regression
# (genes that track activity also track p53 activators)
res = []
for sname in subsets:
    a = per_gene[(sname, "activity_n_sig_genes")]
    p = per_gene[(sname, "P53_az")]
    ok = notp53
    b = np.polyfit(a[ok], p[ok], 1)
    resid = p - np.polyval(b, a)
    res.append(dict(subset=sname, slope=b[0], intercept=b[1], TRIM72_rho_activity=a[it], TRIM72_rho_P53=p[it],
                    TRIM72_expected_from_activity=np.polyval(b, a[it]), TRIM72_resid=resid[it],
                    pct_resid_TRIM72=100 * (resid[ok] < resid[it]).mean(),
                    pct_resid_TRIM72_matched=100 * (resid[matched] < resid[it]).mean()))
pd.DataFrame(res).to_csv(os.path.join(OUT, "v3b_background_vs_activity.csv"), index=False)
pd.set_option("display.width", 250)
print(B.round(3).to_string())
print(pd.DataFrame(res).round(3).to_string())
