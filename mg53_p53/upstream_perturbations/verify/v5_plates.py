#!/usr/bin/env python3
"""Adversarial verification, part 5: plate-baseline batch claims (F2) from the atlas per-well matrices (W2, Z), the
z-vs-activity correlations (F3), and whether TRIM72's co-variation partners survive technical well covariates (F6/F9).
Read-only."""
import os
import numpy as np
import pandas as pd
from scipy import stats

EFF = "/home/user/tahoe_data/atlas/effects"
pd.set_option("display.width", 250)
pd.set_option("display.max_columns", 40)
genes = pd.read_csv(os.path.join(EFF, "genes.csv"))
wells = pd.read_csv(os.path.join(EFF, "wells.csv"))
dd = pd.read_csv(os.path.join(EFF, "drugdose.csv"))
sym = genes["symbol"].astype(str).to_numpy()
col = {s: i for i, s in enumerate(sym)}
c = col["TRIM72"]
W2 = np.load(os.path.join(EFF, "W2.npy"), mmap_mode="r")
Zw = np.load(os.path.join(EFF, "Z.npy"), mmap_mode="r")
wells["W2"] = np.asarray(W2[:, c], float)
wells["Z"] = np.asarray(Zw[:, c], float)
drug = ~wells["is_dmso"].astype(bool)
rel = ~wells["unreliable_plate"].astype(str).str.lower().eq("true")
HIGH = {"plate1", "plate2", "plate3", "plate14"}


def mad(x):
    x = np.asarray(x, float); x = x[np.isfinite(x)]
    return 1.4826 * np.median(np.abs(x - np.median(x)))


pm = wells[drug & rel].groupby("plate").agg(mad_W2=("W2", mad), mad_Z=("Z", mad), n=("W2", "size"),
                                              sd_W2=("W2", "std"), p99_W2=("W2", lambda s: np.percentile(s, 99)))
pm["high"] = pm.index.isin(HIGH)
print(pm.sort_values("high"))
lo, hi = pm[~pm.high].mad_W2, pm[pm.high].mad_W2
print(f"median MAD W2: low {lo.median():.3f} (n {len(lo)}) vs high {hi.median():.3f} (n {len(hi)}); MW p {stats.mannwhitneyu(lo, hi).pvalue:.2f}")
print(f"  without plate 3: high median {pm[pm.high & (pm.index != 'plate3')].mad_W2.median():.3f}")

# same drug-dose on plate 6 and plate 14
d6 = wells[drug & (wells.plate == "plate6")].set_index(["drug", "conc"])
d14 = wells[drug & (wells.plate == "plate14")].set_index(["drug", "conc"])
j = d6[["W2", "Z", "well"]].join(d14[["W2", "Z", "well"]], lsuffix="_6", rsuffix="_14", how="inner")
print(f"\nplate6/14 pairs: {len(j)}; same well position in {int((j.well_6 == j.well_14).sum())}")
for dname in ("Idarubicin (hydrochloride)", "Homoharringtonine", "Mitoxantrone (dihydrochloride)"):
    r = j.loc[(dname, 5.0)]
    print(f"  {dname}: plate6 {2 ** r.W2_6:.2f}x (z {r.Z_6:.1f}) vs plate14 {2 ** r.W2_14:.2f}x (z {r.Z_14:.1f}); log2 ratio {r.W2_6 / r.W2_14:.2f}, z ratio {r.Z_6 / r.Z_14:.2f}")
ts = stats.theilslopes(j.W2_6, j.W2_14)
print(f"  Theil-Sen slope plate6 on plate14 (all pairs): {ts.slope:.2f} ({ts.low_slope:.2f}-{ts.high_slope:.2f}); spearman {stats.spearmanr(j.W2_6, j.W2_14).statistic:.2f}")
big = j[(j.Z_6 >= 3) | (j.Z_14 >= 3)]
print("  pairs with z>=3 on either plate:")
print(big[["W2_6", "W2_14", "Z_6", "Z_14"]].round(2).to_string())

# TRIM72 z vs activity
L = np.load(os.path.join(EFF, "DD_lfc.npy"), mmap_mode="r")
Z = np.load(os.path.join(EFF, "DD_z.npy"), mmap_mode="r")
dd["z"] = np.asarray(Z[:, c], float)
dd["lfc"] = np.asarray(L[:, c], float)
act = np.log1p(dd["n_sig_genes"].astype(float))
r1 = stats.spearmanr(dd.z, act); r2 = stats.spearmanr(dd.z.abs(), act)
print(f"\nSpearman TRIM72 z vs activity {r1.statistic:.3f} (p {r1.pvalue:.2f}); |z| vs activity {r2.statistic:.3f} (p {r2.pvalue:.1g})")

# fold vs z rank: plate-3-only promotions
dd["rank_fold"] = (-dd.lfc).rank(method="min"); dd["rank_z"] = (-dd.z).rank(method="min")
p3 = dd[(dd.plates == "plate3") & (2 ** dd.lfc >= 2) & (dd.z < 3)]
print("plate-3-only >=2x with z<3:"); print(p3[["drug", "conc", "lfc", "z", "rank_fold", "rank_z"]].assign(fold=lambda d: 2 ** d.lfc).round(2).to_string())

# partner correlations with technical covariates added (UMI/cell, genes/cell, composition shift, cell loss, activity)
cov = [act.to_numpy(), dd["cells_log2_vs_plate"].to_numpy(float), dd["umi_per_cell_log2_vs_plate"].to_numpy(float),
       dd["genes_per_cell_log2_vs_plate"].to_numpy(float), dd["composition_shift_log2"].to_numpy(float)]


def rres(y, covs):
    ry = stats.rankdata(y)
    X = np.column_stack([np.ones(len(ry))] + [stats.rankdata(v) for v in covs])
    b, *_ = np.linalg.lstsq(X, ry, rcond=None)
    return ry - X @ b


ok = np.all([np.isfinite(v) for v in cov], axis=0)
print(f"\npartial Spearman with TRIM72 z, controls activity+cell loss+UMI/cell+genes/cell+composition (n {ok.sum()}):")
rt = rres(dd.z.to_numpy()[ok], [v[ok] for v in cov])
for g in ("FOS", "FOSB", "JUN", "HEXIM1", "ATF3", "PMAIP1", "PYGM", "CDKN1A"):
    gz = np.asarray(Z[:, col[g]], float)[ok]
    print(f"  {g:7s} {np.corrcoef(rt, rres(gz, [v[ok] for v in cov]))[0, 1]:+.3f}")
# TRIM72 z vs each technical covariate
for nm, v in zip(["activity", "cells_log2", "umi_per_cell", "genes_per_cell", "composition_shift"], cov):
    print(f"  spearman TRIM72 z vs {nm}: {stats.spearmanr(dd.z[ok], v[ok]).statistic:+.3f}")
# level-matched control genes: how does a random low-level gene correlate with FOS?  (shared technical covariation?)
lvl = genes.loc[c, "median_line_cpm"]
lm = np.flatnonzero((genes["kind"] == "gene").to_numpy() & (genes["n_lines_expressing"] >= 25).to_numpy()
                    & (genes["median_line_cpm"].between(lvl / 4, lvl * 4)).to_numpy())
rng = np.random.default_rng(1)
pick = rng.choice(lm, 300, replace=False)
fz = rres(np.asarray(Z[:, col["FOS"]], float)[ok], [v[ok] for v in cov])
rr = []
for k in pick:
    gz = np.asarray(Z[:, k], float)[ok]
    if np.isfinite(gz).all():
        rr.append(np.corrcoef(fz, rres(gz, [v[ok] for v in cov]))[0, 1])
rr = np.array(rr)
print(f"  300 random level-matched genes vs FOS (same partial): median {np.median(rr):+.3f}, 95th pct {np.percentile(rr, 95):+.3f}, max {rr.max():+.3f}")
