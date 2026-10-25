#!/usr/bin/env python3
"""Adversarial verification, part 4: specificity of TRIM72 in its raisers (rank among genes), generic low-level-gene
shifts in the raisers, the FOS / IEG / P53 partial correlations, the 'FOS-high -> raiser' table, and plate-layout
structure among the strongest compounds. Own code, straight from the atlas matrices. Read-only."""
import os
import re
import numpy as np
import pandas as pd
from scipy import stats

EFF = "/home/user/tahoe_data/atlas/effects"
pd.set_option("display.width", 250)
pd.set_option("display.max_columns", 40)
pd.set_option("display.max_colwidth", 100)

genes = pd.read_csv(os.path.join(EFF, "genes.csv"))
dd = pd.read_csv(os.path.join(EFF, "drugdose.csv"))
L = np.load(os.path.join(EFF, "DD_lfc.npy"), mmap_mode="r")
Z = np.load(os.path.join(EFF, "DD_z.npy"), mmap_mode="r")
QU = np.load(os.path.join(EFF, "DD_qup.npy"), mmap_mode="r")
sym = genes["symbol"].astype(str).to_numpy()
col = {s: i for i, s in enumerate(sym)}
c = col["TRIM72"]
isg = (genes["kind"] == "gene").to_numpy()
ranked = np.flatnonzero(isg & (genes["n_lines_expressing"] >= 25).to_numpy())
lvl = genes.loc[c, "median_line_cpm"]
lm = np.flatnonzero(isg & (genes["n_lines_expressing"] >= 25).to_numpy() & (genes["median_line_cpm"] >= lvl / 4).to_numpy()
                    & (genes["median_line_cpm"] <= lvl * 4).to_numpy())
print(f"ranked genes {len(ranked)}; level-matched {len(lm)} ({lvl / 4:.2f}-{lvl * 4:.1f} CPM)")
dd["lfc"] = np.asarray(L[:, c], float)
dd["z"] = np.asarray(Z[:, c], float)
dd["qup"] = np.asarray(QU[:, c], float)
dd["sig_up"] = (dd.qup < 0.1) & (dd.lfc >= np.log2(1.2))

print("\n-- specificity of TRIM72 within each raiser")
rows = []
for i in dd.index[dd.sig_up]:
    l = np.asarray(L[i, ranked], float); z = np.asarray(Z[i, ranked], float); q = np.asarray(QU[i, ranked], float)
    ok = np.isfinite(l)
    lt, zt = dd.at[i, "lfc"], dd.at[i, "z"]
    ll = np.asarray(L[i, lm], float)
    rows.append({"drug": dd.at[i, "drug"], "conc": dd.at[i, "conc"], "fold": 2 ** lt, "z": zt,
                 "rank_fold": int((l[ok] > lt).sum()) + 1, "n": int(ok.sum()),
                 "top_pct_fold": 100 * ((l[ok] > lt).sum() + 1) / ok.sum(),
                 "rank_z": int((z[ok] > zt).sum()) + 1,
                 "rank_fold_levelmatched": int((ll[np.isfinite(ll)] > lt).sum()) + 1,
                 "n_up2x_q01": int(((q < 0.1) & (l >= 1)).sum()),
                 "median_lfc_levelmatched": float(np.nanmedian(ll)),
                 "median_lfc_all_ranked": float(np.nanmedian(l)),
                 "n_sig_genes": int(dd.at[i, "n_sig_genes"])})
sp = pd.DataFrame(rows).sort_values("z", ascending=False)
print(sp.round(3).to_string())
strong = sp[sp.z >= 4]
print(f"strong raisers (z>=4): top-% by fold range {strong.top_pct_fold.min():.2f}-{strong.top_pct_fold.max():.2f}")

# narrow responses: rank of TRIM72 among significant genes
for drug, conc in [("Idarubicin (hydrochloride)", 0.05), ("Lactate (calcium)", 5.0), ("Cyclosporin A", 0.05)]:
    i = dd.index[(dd.drug == drug) & (dd.conc == conc)][0]
    q = np.asarray(QU[i, :], float); l = np.asarray(L[i, :], float)
    sigm = isg & (q < 0.1) & (l >= np.log2(1.2))
    order = np.argsort(-np.where(sigm, l, -99))[:8]
    print(f"  {drug} {conc}: {int(sigm.sum())} genes up (q<0.1, >=1.2x); top by fold: " +
          ", ".join(f"{sym[k]} {2 ** l[k]:.2f}x" for k in order))

print("\n-- partial Spearman of TRIM72 z with single-gene z across drug-doses (controls: activity, cell loss)")
act = np.log1p(dd["n_sig_genes"].astype(float).to_numpy())
cl = dd["cells_log2_vs_plate"].to_numpy(float)


def rres(y, covs):
    ry = stats.rankdata(y)
    X = np.column_stack([np.ones(len(ry))] + [stats.rankdata(v) for v in covs])
    b, *_ = np.linalg.lstsq(X, ry, rcond=None)
    return ry - X @ b


tz = dd["z"].to_numpy()
rt = rres(tz, [act, cl])
for g in ("FOS", "FOSB", "JUN", "HEXIM1", "ATF3", "PMAIP1", "CDKN1A", "MDM2", "TP53", "PYGM", "MEF2C", "PYCARD", "EGR1", "IER2"):
    if g not in col:
        print("  missing", g); continue
    gz = np.asarray(Z[:, col[g]], float)
    ok = np.isfinite(gz)
    r = np.corrcoef(rt[ok], rres(gz[ok], [act[ok], cl[ok]]))[0, 1] if ok.all() else np.corrcoef(rres(tz[ok], [act[ok], cl[ok]]), rres(gz[ok], [act[ok], cl[ok]]))[0, 1]
    rs = stats.spearmanr(tz, gz, nan_policy="omit").statistic
    print(f"  {g:7s} partial {r:+.3f}   raw {rs:+.3f}")

# leave-out-HHT/dinaciclib/harringtonine sensitivity for FOS partial correlation
comp = dd["drug"].str.split(" \\(").str[0].str.lower()
for drop in ([], ["homoharringtonine", "harringtonine", "dinaciclib"], ["homoharringtonine", "harringtonine", "dinaciclib", "idarubicin"]):
    keep = ~comp.isin(drop).to_numpy()
    gz = np.asarray(Z[:, col["FOS"]], float)
    r = np.corrcoef(rres(tz[keep], [act[keep], cl[keep]]), rres(gz[keep], [act[keep], cl[keep]]))[0, 1]
    print(f"  FOS partial without {drop or 'nothing'}: {r:+.3f} (n {keep.sum()})")
    # among active drug-doses only
    k2 = keep & (dd["n_sig_genes"].to_numpy() >= 500)
    r = np.corrcoef(rres(tz[k2], [act[k2]]), rres(gz[k2], [act[k2]]))[0, 1]
    print(f"      active only (>=500 sig genes, n {k2.sum()}): {r:+.3f}")

print("\n-- FOS-high (z>=4) among active drug-doses (>=500 sig genes): which are they?")
act_dd = dd[dd["n_sig_genes"] >= 500].copy()
act_dd["FOS_z"] = np.asarray(Z[act_dd.index, col["FOS"]], float)
act_dd["HEXIM1_z"] = np.asarray(Z[act_dd.index, col["HEXIM1"]], float)
print(f"active drug-doses: {len(act_dd)}; raisers among them {int(act_dd.sig_up.sum())}")
print(act_dd[act_dd.FOS_z >= 4][["drug", "conc", "FOS_z", "z", "sig_up", "plates"]].to_string())
print("HEXIM1-high:")
print(act_dd[act_dd.HEXIM1_z >= 4][["drug", "conc", "HEXIM1_z", "z", "sig_up", "plates"]].sort_values("HEXIM1_z", ascending=False).to_string())

print("\n-- top activity decile (compounds) by plate layout: raisers and TRIM72 z_max")


def layout(plates):
    ps = {int(p.replace("plate", "")) for p in str(plates).split(",")}
    return "L1-3" if ps & {1, 2, 3} else "L4-6" if ps & {4, 5, 6, 14} else "L7-9" if ps & {7, 8, 9} else "L10-12" if ps & {10, 11, 12} else "L13"


dd["layout"] = [layout(p) for p in dd["plates"]]
dd["compound"] = [re.sub(r"\s*\((?:[^()]|\([^()]*\))*\)\s*$", "", s).strip().lower() for s in dd["drug"]]
g = dd.groupby("compound")
cp = pd.DataFrame({"act": g["n_sig_genes"].max(), "raiser": g["sig_up"].any(), "z_max": g["z"].max(),
                   "layout": g["layout"].agg(lambda s: ",".join(sorted(set(s))))})
thr = cp["act"].rank(method="first").pipe(lambda r: r > len(cp) * 0.9)
top = cp[thr].sort_values("z_max", ascending=False)
top["L1_3"] = top.layout.str.contains("L1-3")
print(top.to_string())
a = int(top[top.L1_3].raiser.sum()); b = int((top.L1_3).sum()); c_ = int(top[~top.L1_3].raiser.sum()); d_ = int((~top.L1_3).sum())
print(f"top decile: L1-3 raisers {a}/{b} vs other layouts {c_}/{d_}; Fisher p {stats.fisher_exact([[a, b - a], [c_, d_ - c_]])[1]:.4f}")
print("median z_max in top decile: L1-3", top[top.L1_3].z_max.median().round(2), " others", top[~top.L1_3].z_max.median().round(2),
      " MW p", round(stats.mannwhitneyu(top[top.L1_3].z_max, top[~top.L1_3].z_max).pvalue, 4))
# all compounds: L1-3 vs others raiser rate, 5 uM drug-doses on plate 3 vs plates 9/12
five = dd[dd.conc == 5]
for p in ("plate3", "plate9", "plate12", "plate14,plate6"):
    s = five[five.plates == p]
    print(f"  5 uM on {p}: n {len(s)}, sig_up {int(s.sig_up.sum())}, z>=3 {int((s.z >= 3).sum())}, "
          f"median n_sig_genes {s.n_sig_genes.median():.0f}, n with >=1767 sig genes {(s.n_sig_genes >= 1767).sum()}")
