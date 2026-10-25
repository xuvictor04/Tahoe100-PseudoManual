#!/usr/bin/env python3
"""Adversarial check of F5/F6 (across all 1,132 drug-doses: TRIM72 z vs p53 readouts; TRIM72-up vs p53-activated).

Independent inputs: the genome-wide atlas (atlas/effects DD_z / DD_lfc / drugdose.csv; a different pipeline from the
gene panel the analysis used) for TRIM72 and the 21 P53_ACTIVITY members; the analysis's c_drugdose_table only for the
panel's P53_ACTIVITY z / calls and the WT-minus-altered contrast (to reproduce its 2x2 and to split it).

Checks
  1. atlas TRIM72 z vs panel TRIM72 z; atlas P53 score (mean member z) vs panel P53_ACTIVITY z
  2. Spearman TRIM72 z vs P53 score / CDKN1A / MDM2 / PMAIP1 / ATF3 (atlas), drug-bootstrap CI, raw and activity-partial
  3. plate batch: the same split by plate set (high-TRIM72-baseline plates 1-3 alone; low-baseline plates 4-12 alone;
     the 2-well plate-6+14 drug-doses) - does a low-baseline plate hide TRIM72 increases?
  4. the 2x2 of F6 reproduced, then stratified by plate set (MH) and by plate set x activity tercile; what the
     'p53 without TRIM72' and 'TRIM72 without p53' rows look like (plate, wells, TRIM72 fold, power proxy: expected
     TRIM72 counts per well x line profile on that plate)
  5. shared stimulus: among DNA-damaging drug-doses only, TRIM72 z vs P53 z and vs the WT-minus-altered contrast;
     and the per-line WT vs altered TRIM72 induction for the analysis's selected drug-doses (does TRIM72 rise equally
     in TP53-altered lines? then its co-rise with p53 targets needs no p53 -> TRIM72 or TRIM72 -> p53 link)

    python3 verify/v3_drugdose.py   -> verify/out/v3_*.csv
"""
import os
import numpy as np
import pandas as pd
from scipy import stats

DATA = "/home/user/tahoe_data"
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(HERE, "out")
os.makedirs(OUT, exist_ok=True)
rng = np.random.default_rng(5)
P53 = ["CDKN1A", "MDM2", "FDXR", "ZMAT3", "SESN1", "BBC3", "BAX", "TP53I3", "RRM2B", "AEN", "DDB2", "XPC", "PHLDA3",
       "SPATA18", "TRIAP1", "RPS27L", "ACER2", "TP53INP1", "PLK3", "POLH", "EDA2R"]
EXTRA = ["TRIM72", "TP53", "PMAIP1", "ATF3"]
HIGH = {"plate1", "plate2", "plate3", "plate14"}

E = os.path.join(DATA, "atlas", "effects")
dd = pd.read_csv(os.path.join(E, "drugdose.csv"))
ga = pd.read_csv(os.path.join(E, "genes.csv"))
ga = ga[ga.kind == "gene"].drop_duplicates("symbol").set_index("symbol")
Zm = np.load(os.path.join(E, "DD_z.npy"), mmap_mode="r")
Lm = np.load(os.path.join(E, "DD_lfc.npy"), mmap_mode="r")
cols = {g: int(ga.loc[g, "col"]) for g in P53 + EXTRA}
A = pd.DataFrame({g + "_az": np.asarray(Zm[:, c]) for g, c in cols.items()})
for g in ("TRIM72", "MDM2", "CDKN1A"):
    A[g + "_afold"] = 2 ** np.asarray(Lm[:, cols[g]])
A["P53_az"] = A[[g + "_az" for g in P53]].mean(axis=1)
A = pd.concat([dd[["drug", "conc", "plates", "n_wells", "n_sig_genes", "cells_log2_vs_plate", "S_PHASE_z",
                   "G2M_PHASE_z", "flags", "moa_fine"]], A], axis=1)

C = pd.read_csv(os.path.join(ROOT, "tables", "c_drugdose_table.csv"))
M = A.merge(C[["drug", "conc", "TRIM72_z", "TRIM72_fold_change", "TRIM72_call", "P53_ACTIVITY_z",
               "P53_ACTIVITY_fdr_up", "p53_WT_minus_altered_z", "dna_damaging", "category"]],
            on=["drug", "conc"], how="left", validate="1:1")
assert len(M) == 1132 and M.TRIM72_z.notna().all()


def plate_set(p):
    s = set(p.split(","))
    if s == {"plate6", "plate14"}:
        return "plates 6+14 (2 wells)"
    if len(s) > 1:
        return "other multi-plate"
    if s <= HIGH:
        return "high-baseline plate (1-3)"
    if s == {"plate13"}:
        return "plate 13 (unreliable)"
    return "low-baseline plate (4-12)"


M["plate_set"] = M.plates.map(plate_set)

# TRIM72 expected counts per well x line profile on each plate (power proxy): median line CPM of DMSO x median UMIs
wl = pd.read_parquet(os.path.join(DATA, "gene_panel", "well_line.parquet"),
                     columns=["sample", "cell_line_id", "TRIM72", "total_counts"])
sm = pd.read_csv(os.path.join(DATA, "gene_panel", "sample_map.csv"), dtype={"sample": str})
wl = wl.groupby(["sample", "cell_line_id"], as_index=False).sum().merge(sm[["sample", "plate", "is_dmso"]], on="sample")
pw = wl.groupby("plate").apply(lambda g: pd.Series(dict(
    median_profile_TRIM72_counts=g.TRIM72.median(),
    median_line_cpm_dmso=g[g.is_dmso].groupby("cell_line_id").apply(
        lambda h: 1e6 * h.TRIM72.sum() / h.total_counts.sum()).median())), include_groups=False)
pw.to_csv(os.path.join(OUT, "v3_plate_TRIM72_counts.csv"))
M["median_profile_TRIM72_counts"] = M.plates.map(
    lambda p: float(np.mean([pw.loc[x, "median_profile_TRIM72_counts"] for x in p.split(",")])))
M.to_csv(os.path.join(OUT, "v3_drugdose_inputs.csv"), index=False)

# ---------------------------------------------------------------- 1. agreement atlas vs panel
agree = []
for a, b in (("TRIM72_az", "TRIM72_z"), ("P53_az", "P53_ACTIVITY_z")):
    agree.append(dict(atlas=a, panel=b, spearman=stats.spearmanr(M[a], M[b])[0], pearson=np.corrcoef(M[a], M[b])[0, 1]))
pd.DataFrame(agree).to_csv(os.path.join(OUT, "v3_atlas_vs_panel.csv"), index=False)


# ---------------------------------------------------------------- 2./3. correlations
def partial_rho(x, y, Z=None):
    rx, ry = stats.rankdata(x), stats.rankdata(y)
    if Z is not None:
        X = np.column_stack([np.ones(len(x))] + [stats.rankdata(Z[:, j]) for j in range(Z.shape[1])])
        rx = rx - X @ np.linalg.lstsq(X, rx, rcond=None)[0]
        ry = ry - X @ np.linalg.lstsq(X, ry, rcond=None)[0]
    return float(np.corrcoef(rx, ry)[0, 1])


def drug_boot(df, x, y, zc, B=1000):
    drugs = df.drug.unique()
    g = {d: np.where(df.drug.to_numpy() == d)[0] for d in drugs}
    out = []
    for _ in range(B):
        ii = np.concatenate([g[d] for d in rng.choice(drugs, len(drugs), replace=True)])
        s = df.iloc[ii]
        out.append(partial_rho(s[x].to_numpy(), s[y].to_numpy(), None if zc is None else s[zc].to_numpy()))
    return np.quantile(out, [0.025, 0.975])


act = ["n_sig_genes", "cells_log2_vs_plate", "S_PHASE_z", "G2M_PHASE_z"]
subsets = {"all": np.ones(len(M), bool)}
for ps in M.plate_set.unique():
    subsets["plate set: " + ps] = (M.plate_set == ps).to_numpy()
subsets["DNA-damaging (panel definition)"] = M.dna_damaging.fillna(False).astype(bool).to_numpy()
subsets["DNA-damaging and P53 z>=3"] = subsets["DNA-damaging (panel definition)"] & (M.P53_ACTIVITY_z >= 3).to_numpy()
rows = []
for sname, m in subsets.items():
    d = M[m].reset_index(drop=True)
    if len(d) < 10:
        continue
    for x in ("TRIM72_az", "TRIM72_z"):
        for y in ("P53_az", "P53_ACTIVITY_z", "CDKN1A_az", "MDM2_az", "PMAIP1_az", "ATF3_az", "TP53_az",
                  "p53_WT_minus_altered_z"):
            if x == "TRIM72_z" and y.endswith("_az") and y != "P53_az":
                continue
            for adj in ("none", "activity"):
                zc = None if adj == "none" else act
                r = partial_rho(d[x].to_numpy(), d[y].to_numpy(), None if zc is None else d[zc].to_numpy())
                lo, hi = drug_boot(d, x, y, zc, 500) if sname == "all" or "plate" in sname or "DNA" in sname \
                    else (np.nan, np.nan)
                rows.append(dict(subset=sname, n=len(d), x=x, y=y, adjust=adj, rho=r, ci_lo=lo, ci_hi=hi))
R = pd.DataFrame(rows)
R.to_csv(os.path.join(OUT, "v3_correlations.csv"), index=False)

# ---------------------------------------------------------------- 4. 2x2
M["T_up"] = M.TRIM72_call.eq("up")
M["P_act"] = (M.P53_ACTIVITY_z >= 3) & (M.P53_ACTIVITY_fdr_up < 0.10)


def tab(d):
    a = int((d.T_up & d.P_act).sum())
    b = int((d.T_up & ~d.P_act).sum())
    c = int((~d.T_up & d.P_act).sum())
    e = int((~d.T_up & ~d.P_act).sum())
    return a, b, c, e


t2 = []
a, b, c, e = tab(M)
t2.append(dict(stratum="all", both=a, T_only=b, P_only=c, neither=e, OR=stats.contingency.odds_ratio([[a, b], [c, e]]
                                                                                                       ).statistic,
               p=stats.fisher_exact([[a, b], [c, e]])[1]))
for ps, d in M.groupby("plate_set"):
    a, b, c, e = tab(d)
    t2.append(dict(stratum=ps, both=a, T_only=b, P_only=c, neither=e,
                   frac_P_act_with_T_up=a / (a + c) if a + c else np.nan,
                   frac_T_up_with_P_act=a / (a + b) if a + b else np.nan,
                   pct_drugdoses_T_up=100 * (a + b) / len(d), pct_drugdoses_P_act=100 * (a + c) / len(d)))
# MH over plate set x activity tercile
M["act3"] = pd.qcut(M.n_sig_genes.rank(method="first"), 3, labels=False)
num = den = 0.0
for _, d in M.groupby(["plate_set", "act3"]):
    a, b, c, e = tab(d)
    n = a + b + c + e
    num += a * e / n
    den += b * c / n
t2.append(dict(stratum="MH over plate set x activity tercile", OR=num / den if den else np.nan))
T2 = pd.DataFrame(t2)
T2.to_csv(os.path.join(OUT, "v3_2x2_by_plate_set.csv"), index=False)

# the off-diagonal rows
po = M[~M.T_up & M.P_act].copy()
to = M[M.T_up & ~M.P_act].copy()
keep = ["drug", "conc", "plates", "plate_set", "n_wells", "flags", "TRIM72_fold_change", "TRIM72_z", "TRIM72_az",
        "TRIM72_afold", "median_profile_TRIM72_counts", "P53_ACTIVITY_z", "P53_az", "p53_WT_minus_altered_z",
        "MDM2_az", "category"]
po[keep].sort_values("P53_ACTIVITY_z", ascending=False).to_csv(os.path.join(OUT, "v3_p53_without_TRIM72.csv"),
                                                               index=False)
to[keep].sort_values("TRIM72_z", ascending=False).to_csv(os.path.join(OUT, "v3_TRIM72_without_p53.csv"), index=False)
summ = []
for nm, d in (("p53 activated, TRIM72 not up", po), ("TRIM72 up, p53 not activated", to),
              ("both", M[M.T_up & M.P_act])):
    summ.append(dict(group=nm, n=len(d), **{f"n_{k}": int((d.plate_set == k).sum()) for k in M.plate_set.unique()},
                     n_one_well=int((d.n_wells == 1).sum()),
                     n_TRIM72_fold_gt_1_5=int((d.TRIM72_fold_change > 1.5).sum()),
                     n_TRIM72_fold_lt_1=int((d.TRIM72_fold_change < 1).sum()),
                     n_TRIM72_z_lt_2=int((d.TRIM72_z < 2).sum()),
                     n_TRIM72_z_lt_0=int((d.TRIM72_z < 0).sum()),
                     n_P53_z_lt_2=int((d.P53_ACTIVITY_z < 2).sum()),
                     median_TRIM72_fold=d.TRIM72_fold_change.median(),
                     median_profile_TRIM72_counts=d.median_profile_TRIM72_counts.median()))
pd.DataFrame(summ).to_csv(os.path.join(OUT, "v3_offdiagonal_summary.csv"), index=False)

# ---------------------------------------------------------------- 5. shared stimulus: TRIM72 induction WT vs altered
pl = pd.read_csv(os.path.join(ROOT, "tables", "a_per_line_effects.csv"))
sh = []
for (dr, cc), g in pl.groupby(["drug", "conc"]):
    a_ = g[g.tp53_group == "WT"].TRIM72_r2.dropna()
    b_ = g[g.tp53_group == "altered"].TRIM72_r2.dropna()
    p_ = g[g.tp53_group == "WT"].P53_SCORE.dropna()
    q_ = g[g.tp53_group == "altered"].P53_SCORE.dropna()
    u = stats.mannwhitneyu(a_, b_)
    u2 = stats.mannwhitneyu(p_, q_)
    sh.append(dict(drug=dr, conc=cc, n_WT=len(a_), n_alt=len(b_), TRIM72_r2_median_WT=a_.median(),
                   TRIM72_r2_median_alt=b_.median(), AUC_TRIM72_WT_gt_alt=u.statistic / len(a_) / len(b_),
                   p_TRIM72=u.pvalue, P53_median_WT=p_.median(), P53_median_alt=q_.median(),
                   AUC_P53_WT_gt_alt=u2.statistic / len(p_) / len(q_), p_P53=u2.pvalue))
SH = pd.DataFrame(sh)
SH["q_TRIM72"] = stats.false_discovery_control(SH.p_TRIM72)
SH.to_csv(os.path.join(OUT, "v3_trim72_induction_WT_vs_altered.csv"), index=False)

pd.set_option("display.width", 250)
pd.set_option("display.max_columns", 30)
pd.set_option("display.max_rows", 300)
print(pd.DataFrame(agree).round(3).to_string())
print(pw.round(2).to_string())
print(R[R.subset == "all"].round(3).to_string())
print(R[(R.subset != "all") & R.y.isin(["P53_az", "P53_ACTIVITY_z", "p53_WT_minus_altered_z", "PMAIP1_az"])]
      .round(3).to_string())
print(T2.round(3).to_string())
print(pd.DataFrame(summ).round(2).T.to_string())
print(po[keep].sort_values("P53_ACTIVITY_z", ascending=False).round(2).to_string())
print(to[keep].round(2).to_string())
print(SH.round(3).to_string())
