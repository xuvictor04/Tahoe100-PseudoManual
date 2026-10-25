#!/usr/bin/env python3
"""Adversarial verification, part 7: muscle-gene folds under idarubicin 5 uM (F9) and replication of single-plate
TRIM72 increases between plate 6 and plate 14 (same drug-doses, same positions). Read-only."""
import os
import numpy as np
import pandas as pd
EFF = "/home/user/tahoe_data/atlas/effects"
genes = pd.read_csv(os.path.join(EFF, "genes.csv")); dd = pd.read_csv(os.path.join(EFF, "drugdose.csv"))
sym = genes["symbol"].astype(str).to_numpy(); col = {s: i for i, s in enumerate(sym)}
L = np.load(os.path.join(EFF, "DD_lfc.npy"), mmap_mode="r")
i = dd.index[(dd.drug == "Idarubicin (hydrochloride)") & (dd.conc == 5)][0]
print("idarubicin 5 uM:", ", ".join(f"{g} {2 ** float(L[i, col[g]]):.2f}x" for g in ("DYSF", "TTN", "NEB", "MYH3", "PYGM", "TRIM72") if g in col))
w = pd.read_csv(os.path.join(EFF, "wells.csv")); Zw = np.load(os.path.join(EFF, "Z.npy"), mmap_mode="r")
c = col["TRIM72"]; w["Z"] = np.asarray(Zw[:, c], float)
d6 = w[(w.plate == "plate6") & ~w.is_dmso.astype(bool)].set_index(["drug", "conc"])["Z"]
d14 = w[(w.plate == "plate14") & ~w.is_dmso.astype(bool)].set_index(["drug", "conc"])["Z"]
j = pd.concat([d6.rename("z6"), d14.rename("z14")], axis=1, join="inner")
for thr in (3, 2.5):
    h6 = j[j.z6 >= thr]; h14 = j[j.z14 >= thr]
    print(f"plate6 z>={thr}: {len(h6)}; of these z14>=2: {(h6.z14 >= 2).sum()}, z14>=z6/1.85-1 : {(h6.z14 >= h6.z6 / 1.85 - 1).sum()}")
    print(f"plate14 z>={thr}: {len(h14)}; of these z6>=2: {(h14.z6 >= 2).sum()}")
    print(h6.round(2).to_string())

# 16p11.2 neighbours of TRIM72 (chr16 ~31.0-31.5 Mb): folds under the top raisers and partial Spearman with TRIM72 z
from scipy import stats
Z = np.load(os.path.join(EFF, "DD_z.npy"), mmap_mode="r")
tz = np.asarray(Z[:, c], float)
act = np.log1p(dd["n_sig_genes"].astype(float)).to_numpy(); cl = dd["cells_log2_vs_plate"].to_numpy(float)
def rres(y, covs):
    ry = stats.rankdata(y); X = np.column_stack([np.ones(len(ry))] + [stats.rankdata(v) for v in covs])
    b, *_ = np.linalg.lstsq(X, ry, rcond=None); return ry - X @ b
rt = rres(tz, [act, cl])
rows_top = {k: dd.index[(dd.drug == a) & (dd.conc == 5)][0] for k, a in (("ida", "Idarubicin (hydrochloride)"), ("hht", "Homoharringtonine"), ("aur", "Auranofin"))}
NB = ["STX4", "ZNF668", "ZNF646", "VKORC1", "BCKDK", "KAT8", "PRSS8", "FUS", "PYCARD", "PYDC1", "ITGAM", "ITGAX", "COX6A2",
      "ARMC5", "TGFB1I1", "SLC5A2", "RUSF1", "C16orf58", "AHSP", "ZNF843", "SETD1A", "HSD3B7", "ORAI3", "ZNF688", "ZNF785", "ZNF689", "PRR14", "FBRS", "SRCAP", "PHKG2", "RNF40", "ZNF629", "BCL7C", "CTF1", "FBXL19", "ORAI3"]
out = []
for g in dict.fromkeys(NB):
    if g not in col:
        continue
    k = col[g]
    gz = np.asarray(Z[:, k], float)
    ok = np.isfinite(gz)
    r = np.corrcoef(rt[ok] if ok.all() else rres(tz[ok], [act[ok], cl[ok]]), rres(gz[ok], [act[ok], cl[ok]]))[0, 1]
    out.append((g, round(float(genes.loc[k, "median_line_cpm"]), 1), round(r, 3),
                *[round(2 ** float(L[i, k]), 2) for i in rows_top.values()]))
print(pd.DataFrame(out, columns=["gene", "median_line_cpm", "partial_rho_with_TRIM72", "fold_ida5", "fold_hht5", "fold_aur5"]).to_string(index=False))
