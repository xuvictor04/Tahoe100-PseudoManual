#!/usr/bin/env python3
"""Part 3 of the adversarial verification: an independent 'screen-lite' over all drug wells (DMSO-baseline log2
ratios from raw panel counts, no corrections) for F4/F5, and a direct test of F7's 'tracks cytotoxicity' claim.
Usage: python3 verify_part3.py
"""
import os
import numpy as np
import pandas as pd
from scipy import stats

DATA = "/home/user/tahoe_data"
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "tables")
os.makedirs(OUT, exist_ok=True)
pd.set_option("display.width", 250); pd.set_option("display.max_columns", 40)
P53 = ["CDKN1A", "MDM2", "FDXR", "ZMAT3", "SESN1", "BBC3", "BAX", "TP53I3", "RRM2B", "AEN", "DDB2", "XPC", "PHLDA3",
       "SPATA18", "TRIAP1", "RPS27L", "ACER2", "TP53INP1", "PLK3", "POLH", "EDA2R"]
GEN = ["TRIM72"] + P53
smap = pd.read_csv(f"{DATA}/gene_panel/sample_map.csv")
wl = pd.read_parquet(f"{DATA}/gene_panel/well_line.parquet", columns=["sample", "cell_line_id", "n_cells", "total_counts"] + GEN)
wl = wl.groupby(["sample", "cell_line_id"], as_index=False).sum().merge(smap[["sample", "plate", "drug", "conc", "is_dmso"]], on="sample")
base = pd.read_csv(f"{DATA}/gene_panel/results/baseline_by_cell_line.csv").set_index("cell_line_id")
lines = sorted(wl.cell_line_id.unique())
wt = base.reindex(lines).tp53_group.eq("WT").to_numpy()

dm = wl[wl.is_dmso.astype(bool)]
cpm_all = dm.groupby("cell_line_id")[GEN + ["total_counts"]].sum()
expr = (cpm_all[GEN].div(cpm_all.total_counts, axis=0) * 1e6 >= 1).reindex(lines)
dpl = dm.groupby(["plate", "cell_line_id"])[GEN + ["total_counts"]].sum()

rows = []
for s, w in wl[~wl.is_dmso.astype(bool) & (wl.plate != "plate13")].groupby("sample"):
    plate = w.plate.iloc[0]
    w = w[w.n_cells >= 30].set_index("cell_line_id").reindex(lines)
    d = dpl.loc[plate].reindex(lines)
    L = {}
    for g in GEN:
        v = np.log2((w[g] + 0.5) / w.total_counts) - np.log2((d[g] + 0.5) / d.total_counts)
        v[~expr[g].fillna(False).to_numpy()] = np.nan
        L[g] = v.to_numpy()
    M = np.vstack([L[g] for g in P53])
    score = np.nanmean(M, axis=0)
    r = dict(sample=s, plate=plate, drug=w.drug.dropna().iloc[0] if w.drug.notna().any() else None,
             conc=w.conc.dropna().iloc[0] if w.conc.notna().any() else None)
    for nm, v in [("TRIM72", L["TRIM72"]), ("P53_SCORE", score), ("MDM2", L["MDM2"]), ("CDKN1A", L["CDKN1A"]),
                  ("SPATA18", L["SPATA18"]), ("EDA2R", L["EDA2R"]), ("TP53I3", L["TP53I3"])]:
        a, b = v[wt & np.isfinite(v)], v[~wt & np.isfinite(v)]
        r[f"{nm}_all"] = np.nanmedian(v) if np.isfinite(v).sum() >= 10 else np.nan
        r[f"{nm}_d"] = (np.median(a) - np.median(b)) if (len(a) >= 5 and len(b) >= 5) else np.nan
    # P53 score leaving the gene out (for members)
    for g in ["MDM2", "CDKN1A", "SPATA18", "EDA2R", "TP53I3"]:
        sc = np.nanmean(np.vstack([L[x] for x in P53 if x != g]), axis=0)
        a, b = sc[wt & np.isfinite(sc)], sc[~wt & np.isfinite(sc)]
        r[f"P53_SCORE_wo_{g}_d"] = np.median(a) - np.median(b)
    rows.append(r)
W = pd.DataFrame(rows)
W = W[W.drug.notna()]
# robust z within plate
for c in [c for c in W.columns if c.endswith("_d") or c.endswith("_all")]:
    g = W.groupby("plate")[c]
    med = g.transform("median"); mad = g.transform(lambda x: 1.4826 * np.nanmedian(np.abs(x - np.nanmedian(x))))
    W[c + "_z"] = (W[c] - med) / mad
zc = [c for c in W.columns if c.endswith("_z")]
DD = W.groupby(["drug", "conc"]).agg({**{c: (lambda x: np.nansum(x) / np.sqrt(np.isfinite(x).sum()) if np.isfinite(x).any() else np.nan) for c in zc},
                                       "sample": "count"}).reset_index().rename(columns={"sample": "n_wells"})
DD.to_csv(f"{OUT}/screen_lite_dmso_ratio_by_drugdose.csv", index=False)

out = []
def sp(a, b, label, mask=None):
    m = DD[a].notna() & DD[b].notna()
    if mask is not None:
        m &= mask
    rho, p = stats.spearmanr(DD.loc[m, a], DD.loc[m, b])
    out.append(dict(test=label, n=int(m.sum()), rho=rho, p=p))

sp("TRIM72_d_z", "P53_SCORE_d_z", "all drug-doses: TRIM72 WT-minus-altered z vs P53 score WT-minus-altered z")
for g in ["MDM2", "CDKN1A", "TP53I3", "SPATA18", "EDA2R"]:
    sp(f"{g}_d_z", f"P53_SCORE_wo_{g}_d_z", f"all drug-doses: {g} WT-minus-altered z vs P53 score (without {g}) WT-minus-altered z")
raisers = DD.TRIM72_all_z >= 3
sp("TRIM72_d_z", "P53_SCORE_d_z", "TRIM72-raising drug-doses (all-line TRIM72 robust z >= 3)", raisers)
sp("TRIM72_all_z", "P53_SCORE_all_z", "all drug-doses: TRIM72 all-line z vs P53 score all-line z")
act = (DD.P53_SCORE_all_z >= 5) | (DD.P53_SCORE_d_z >= 5)
sp("TRIM72_d_z", "P53_SCORE_d_z", "strong p53 activators (all-line or WT-selective P53 z >= 5)", act)
res = pd.DataFrame(out)
# sign / magnitude summaries
top = DD.dropna(subset=["P53_SCORE_d_z"]).nlargest(20, "P53_SCORE_d_z")
summ = dict(
    n_drugdoses=len(DD), n_trim72_raisers=int(raisers.sum()), n_strong_activators=int(act.sum()),
    sd_TRIM72_d_z=np.nanstd(DD.TRIM72_d_z), sd_P53_d_z=np.nanstd(DD.P53_SCORE_d_z), sd_SPATA18_d_z=np.nanstd(DD.SPATA18_d_z),
    sd_EDA2R_d_z=np.nanstd(DD.EDA2R_d_z),
    TRIM72_d_z_gt3=int((DD.TRIM72_d_z > 3).sum()), TRIM72_d_z_lt_minus3=int((DD.TRIM72_d_z < -3).sum()),
    top20_p53_selective_mean_TRIM72_d_z=top.TRIM72_d_z.mean(), top20_TRIM72_d_z_positive=int((top.TRIM72_d_z > 0).sum()),
    top20_mean_SPATA18_d_z=top.SPATA18_d_z.mean(), top20_mean_EDA2R_d_z=top.EDA2R_d_z.mean(),
    top20_mean_MDM2_d_z=top.MDM2_d_z.mean(),
    raisers_mean_TRIM72_d_z=DD.loc[raisers, "TRIM72_d_z"].mean(), raisers_TRIM72_d_z_positive=int((DD.loc[raisers, "TRIM72_d_z"] > 0).sum()),
    raisers_TRIM72_d_z_wilcoxon_p=stats.wilcoxon(DD.loc[raisers, "TRIM72_d_z"].dropna()).pvalue,
)
print("=== Screen-lite (independent; DMSO-baseline ratios, plate robust z, Stouffer) ===")
print(res.round(4).to_string(index=False))
for k, v in summ.items():
    print(f"{k}: {v}")
print("\nTRIM72 raisers (screen-lite):")
print(DD.loc[raisers, ["drug", "conc", "n_wells", "TRIM72_all_z", "TRIM72_d_z", "P53_SCORE_all_z", "P53_SCORE_d_z"]].sort_values("TRIM72_all_z", ascending=False).round(2).to_string(index=False))
res.to_csv(f"{OUT}/screen_lite_tests.csv", index=False)
pd.Series(summ).to_csv(f"{OUT}/screen_lite_summary.csv")

# ---------------------------------------------------------------- F7: cytotoxicity vs p53 as predictors of TRIM72
T = pd.read_csv(f"{DATA}/gene_panel/results/TRIM72_drug_effects_by_dose.csv")
T = T[T.z_corrected.notna() & T.P53_ACTIVITY_z.notna() & T.cells_log2_vs_plate.notna()]


def partial(x, y, z):
    rx, ry, rz = stats.rankdata(x), stats.rankdata(y), stats.rankdata(z)
    Z = np.column_stack([np.ones(len(rz)), rz])
    ex = rx - Z @ np.linalg.lstsq(Z, rx, rcond=None)[0]
    ey = ry - Z @ np.linalg.lstsq(Z, ry, rcond=None)[0]
    r = np.corrcoef(ex, ey)[0, 1]
    n = len(x); t = r * np.sqrt((n - 3) / (1 - r * r))
    return r, 2 * stats.t.sf(abs(t), n - 3)


cyt = -T.cells_log2_vs_plate          # higher = more cell loss
f7 = []
for lab, x in [("cell loss (-cells_log2_vs_plate)", cyt), ("P53_ACTIVITY_z", T.P53_ACTIVITY_z),
               ("transcription: -umi_per_cell_log2_vs_plate", -T.umi_per_cell_log2_vs_plate)]:
    rho, p = stats.spearmanr(T.z_corrected, x)
    f7.append(dict(test=f"Spearman TRIM72 z vs {lab}", n=len(T), rho=rho, p=p))
r, p = partial(T.z_corrected.values, T.P53_ACTIVITY_z.values, cyt.values)
f7.append(dict(test="partial Spearman TRIM72 z vs P53_ACTIVITY_z given cell loss", n=len(T), rho=r, p=p))
r, p = partial(T.z_corrected.values, cyt.values, T.P53_ACTIVITY_z.values)
f7.append(dict(test="partial Spearman TRIM72 z vs cell loss given P53_ACTIVITY_z", n=len(T), rho=r, p=p))
up = (T.z_corrected >= 3) & (T.fold_change >= 1.2)
toxic = cyt >= 0.5
tab = pd.crosstab(up, toxic)
orr, pf = stats.fisher_exact(tab.values)
f7.append(dict(test=f"Fisher TRIM72 up vs cell loss >= 0.5 log2 (OR); up&toxic={int((up & toxic).sum())}/{int(toxic.sum())}, up&not={int((up & ~toxic).sum())}/{int((~toxic).sum())}", n=len(T), rho=orr, p=pf))
f7 = pd.DataFrame(f7)
f7.to_csv(f"{OUT}/f7_cytotoxicity_vs_p53.csv", index=False)
print("\n=== F7: does TRIM72 induction track cell loss or p53 activation (over drug-doses)? ===")
print(f7.round(4).to_string(index=False))
print("\nTRIM72 raisers: cell loss and P53 z")
print(T.loc[up, ["drug", "conc", "fold_change", "z_corrected", "P53_ACTIVITY_z", "cells_log2_vs_plate", "umi_per_cell_log2_vs_plate", "plates"]].sort_values("z_corrected", ascending=False).round(2).to_string(index=False))
