#!/usr/bin/env python3
"""Adversarial verification, part 6: TRIM72 vs P53_ACTIVITY (the panel's pathway score, used as given data) across
drug-doses and among active drug-doses; top-20 P53_ACTIVITY drug-doses and how many raise TRIM72; genome-wide partial
Spearman partners of TRIM72 (own vectorised code) and their expression level; muscle genes in the atlas. Read-only."""
import os
import numpy as np
import pandas as pd
from scipy import stats

EFF = "/home/user/tahoe_data/atlas/effects"
GR = "/home/user/tahoe_data/gene_panel/results"
pd.set_option("display.width", 250)
genes = pd.read_csv(os.path.join(EFF, "genes.csv"))
dd = pd.read_csv(os.path.join(EFF, "drugdose.csv"))
sym = genes["symbol"].astype(str).to_numpy()
c = int(np.flatnonzero(sym == "TRIM72")[0])
Z = np.load(os.path.join(EFF, "DD_z.npy"), mmap_mode="r")
L = np.load(os.path.join(EFF, "DD_lfc.npy"), mmap_mode="r")
QU = np.load(os.path.join(EFF, "DD_qup.npy"), mmap_mode="r")
dd["z"] = np.asarray(Z[:, c], float)
dd["lfc"] = np.asarray(L[:, c], float)
dd["sig_up"] = (np.asarray(QU[:, c], float) < 0.1) & (dd.lfc >= np.log2(1.2))
act = np.log1p(dd["n_sig_genes"].astype(float)).to_numpy()
cl = dd["cells_log2_vs_plate"].to_numpy(float)

ps = pd.read_csv(os.path.join(GR, "pathway_scores_by_dose.csv"), usecols=["score", "drug", "conc", "z"])
p53 = ps[ps.score == "P53_ACTIVITY"].rename(columns={"z": "P53_z"})
dd["conc_r"] = dd["conc"].round(4)
p53["conc_r"] = p53["conc"].round(4)
dd = dd.merge(p53[["drug", "conc_r", "P53_z"]], on=["drug", "conc_r"], how="left")
print("P53 merged:", dd.P53_z.notna().sum())


def rres(y, covs):
    ry = stats.rankdata(y)
    X = np.column_stack([np.ones(len(ry))] + [stats.rankdata(v) for v in covs])
    b, *_ = np.linalg.lstsq(X, ry, rcond=None)
    return ry - X @ b


r = np.corrcoef(rres(dd.z, [act, cl]), rres(dd.P53_z, [act, cl]))[0, 1]
print(f"partial Spearman TRIM72 z vs P53_ACTIVITY z (activity, cell loss), all {len(dd)}: {r:+.3f}")
a = (dd["n_sig_genes"] >= 500).to_numpy()
r = np.corrcoef(rres(dd.z[a], [act[a]]), rres(dd.P53_z[a], [act[a]]))[0, 1]
print(f"  active only (n {a.sum()}): {r:+.3f}")
top = dd.sort_values("P53_z", ascending=False).head(20)
print(f"top 20 P53_ACTIVITY drug-doses: {int(top.sig_up.sum())} raise TRIM72")
print(top[["drug", "conc", "P53_z", "z", "sig_up"]].round(2).to_string())
act_dd = dd[a]
print(f"active drug-doses with P53_z>=4: {(act_dd.P53_z >= 4).sum()}, raisers among them {int(act_dd[act_dd.P53_z >= 4].sig_up.sum())}")

# genome-wide partners (partial Spearman, activity + cell loss), genes expressed in >= 25 lines
ranked = np.flatnonzero((genes["kind"] == "gene").to_numpy() & (genes["n_lines_expressing"] >= 25).to_numpy())
X = np.column_stack([np.ones(len(dd)), stats.rankdata(act), stats.rankdata(cl)])
P = X @ np.linalg.pinv(X)
ty = rres(dd.z.to_numpy(), [act, cl])
rs = np.full(len(ranked), np.nan)
B = 2000
for s in range(0, len(ranked), B):
    cols = ranked[s:s + B]
    M = np.asarray(Z[:, cols], float)
    M = np.where(np.isfinite(M), M, 0.0)
    R = stats.rankdata(M, axis=0)
    R = R - P @ R
    num = (R * ty[:, None]).sum(0)
    den = np.sqrt((R ** 2).sum(0) * (ty ** 2).sum())
    rs[s:s + B] = num / den
res = pd.DataFrame({"gene": sym[ranked], "partial": rs, "median_line_cpm": genes["median_line_cpm"].to_numpy()[ranked]})
res = res[res.gene != "TRIM72"].sort_values("partial", ascending=False)
print("\ntop 15 genome-wide partners:")
print(res.head(15).round(3).to_string(index=False))
t100 = res.head(100)
print(f"top-100 partners median line CPM {t100.median_line_cpm.median():.1f} vs all ranked {res.median_line_cpm.median():.1f}")
hi = res[res.median_line_cpm >= 10]
print("top partners among genes >= 10 CPM:", hi.head(5)[["gene", "partial"]].round(3).values.tolist())
for g in ("PYGM", "MEF2A", "MEF2C", "MEF2D", "DYSF", "TTN", "NEB", "MYH3", "FNDC7", "PYCARD"):
    v = res[res.gene == g]
    print(f"  {g}: {v.partial.round(3).tolist()} (rank {int(np.flatnonzero(res.gene.to_numpy() == g)[0]) + 1 if len(v) else 'NA'})")
for g in ("MYOD1", "MYOG", "MYF5", "MYF6", "DES", "CKM", "CAV3", "CHRNA1", "TRIM63", "MSTN", "PYCARD"):
    h = genes[genes.symbol == g]
    print(f"  atlas column {g}: {'absent' if h.empty else h[['median_line_cpm', 'pooled_cpm', 'n_lines_expressing']].round(2).values.tolist()}")

# where do the IEG genes rank among genome-wide partners?
res = res.reset_index(drop=True)
for g in ("FOSB", "FOS", "JUN", "HEXIM1", "ATF3", "PMAIP1", "EGR1"):
    k = np.flatnonzero(res.gene.to_numpy() == g)
    if len(k):
        hi_rank = int(np.flatnonzero(hi.gene.to_numpy() == g)[0]) + 1 if g in set(hi.gene) else None
        print(f"  {g}: partial {res.partial.iloc[k[0]]:.3f}, rank {k[0] + 1} of {len(res)} (among >=10 CPM: {hi_rank} of {len(hi)})")
print(f"genes with partial >= 0.50: {(res.partial >= 0.5).sum()}; >= 0.47: {(res.partial >= 0.47).sum()}")
