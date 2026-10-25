#!/usr/bin/env python3
"""Adversarial verification, part 1: TRIM72 ranking re-derived straight from the atlas .npy/.csv files
(no use of the analysis tables). Read-only on /home/user/tahoe_data. Prints results; writes small CSVs to verify/out/."""
import os
import numpy as np
import pandas as pd
from scipy import stats

EFF = "/home/user/tahoe_data/atlas/effects"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
os.makedirs(OUT, exist_ok=True)
pd.set_option("display.width", 250)
pd.set_option("display.max_columns", 40)
pd.set_option("display.max_colwidth", 60)

genes = pd.read_csv(os.path.join(EFF, "genes.csv"))
dd = pd.read_csv(os.path.join(EFF, "drugdose.csv"))
wells = pd.read_csv(os.path.join(EFF, "wells.csv"))
c = int(genes.loc[genes["symbol"] == "TRIM72", "col"].iloc[0])
print("TRIM72 col", c, genes.loc[c, ["median_line_cpm", "n_lines_expressing", "pooled_cpm"]].to_dict())

L = np.load(os.path.join(EFF, "DD_lfc.npy"), mmap_mode="r")
Zm = np.load(os.path.join(EFF, "DD_z.npy"), mmap_mode="r")
QU = np.load(os.path.join(EFF, "DD_qup.npy"), mmap_mode="r")
QD = np.load(os.path.join(EFF, "DD_qdn.npy"), mmap_mode="r")
t = dd[["drug", "conc", "plates", "wells", "n_wells", "n_sig_genes", "cells_log2_vs_plate", "cells_log2_best_well",
        "flags", "moa_fine", "targets", "composition_shift_log2", "umi_per_cell_log2_vs_plate"]].copy()
t["lfc"] = np.asarray(L[:, c], float)
t["fold"] = 2 ** t["lfc"]
t["z"] = np.asarray(Zm[:, c], float)
t["qup"] = np.asarray(QU[:, c], float)
t["qdn"] = np.asarray(QD[:, c], float)
LFC_MIN = np.log2(1.2)
t["sig_up"] = (t.qup < 0.1) & (t.lfc >= LFC_MIN)
t["sig_dn"] = (t.qdn < 0.1) & (t.lfc <= -LFC_MIN)

# independent q-value check: one-sided normal p from z, BH over the 1132 drug-doses
def bh(p):
    p = np.asarray(p, float); n = len(p); o = np.argsort(p)
    r = p[o] * n / np.arange(1, n + 1); r = np.minimum.accumulate(r[::-1])[::-1]
    q = np.empty(n); q[o] = np.minimum(r, 1); return q
t["q_up_mine"] = bh(stats.norm.sf(t["z"]))
t["q_dn_mine"] = bh(stats.norm.cdf(t["z"]))
print("q_up atlas vs mine: spearman", stats.spearmanr(t.qup, t.q_up_mine).statistic,
      " max|diff| among q<0.2:", np.nanmax(np.abs(t.qup - t.q_up_mine)[t.qup < 0.2]))

def salt_base(s):
    s = str(s)
    return s.split(" (")[0].strip().lower()
t["compound"] = [salt_base(d) for d in t["drug"]]
up = t[t.sig_up].sort_values("z", ascending=False)
print(f"\nsig_up: {len(up)} drug-doses, {up.compound.nunique()} compounds; sig_down: {int(t.sig_dn.sum())}")
print(up[["drug", "conc", "fold", "z", "qup", "plates", "n_sig_genes", "cells_log2_vs_plate", "flags"]].to_string())
print("\nsig_down:")
print(t[t.sig_dn][["drug", "conc", "fold", "z", "qdn", "plates", "n_sig_genes"]].to_string())
print("\nnominal z <= -2:", int((t.z <= -2).sum()), " z >= 2:", int((t.z >= 2).sum()),
      " expected each side under N(0,1):", round(len(t) * stats.norm.cdf(-2), 1))
# z distribution symmetry: robust centre / scale
print("z median", t.z.median().round(3), "MAD-sd", (1.4826 * np.median(np.abs(t.z - t.z.median()))).round(3))
for thr in (2, 2.5, 3):
    print(f"  |z|>={thr}: up {(t.z >= thr).sum()}  down {(t.z <= -thr).sum()}")

# alternative raiser definitions: robustness of the set
print("\nraisers with q<0.05:", int(((t.qup < 0.05) & (t.lfc >= LFC_MIN)).sum()),
      " z>=3:", int((t.z >= 3).sum()), " z>=4:", int((t.z >= 4).sum()))
t.to_csv(os.path.join(OUT, "v1_trim72_drugdose.csv"), index=False)

# plate group of each drug-dose (high-baseline plates 1,2,3,14)
HIGH = {"plate1", "plate2", "plate3", "plate14"}
def grp(pl):
    s = set(str(pl).split(";")) if ";" in str(pl) else set(str(pl).replace(" ", "").split(","))
    h = {p in HIGH for p in s}
    return "high" if h == {True} else "low" if h == {False} else "mixed"
t["pgroup"] = [grp(p) for p in t["plates"]]
print("\nplates column examples:", t["plates"].head(3).tolist())
print(pd.crosstab(t["pgroup"], t["sig_up"]))
print(pd.crosstab(t["pgroup"], t["z"] <= -2))
# by plate of single-well drug-doses
one = t[t.n_wells == 1].copy()
one["plate"] = one["plates"].astype(str)
tab = one.groupby("plate").agg(n=("z", "size"), n_up_sig=("sig_up", "sum"), n_z_ge3=("z", lambda s: int((s >= 3).sum())),
                               n_z_le_m2=("z", lambda s: int((s <= -2).sum())), sd_z=("z", "std"),
                               mad_lfc=("lfc", lambda s: 1.4826 * np.median(np.abs(s - s.median()))))
print(tab.loc[sorted(tab.index, key=lambda s: int(s.replace("plate", "")) if s.startswith("plate") and s[5:].isdigit() else 99)])
