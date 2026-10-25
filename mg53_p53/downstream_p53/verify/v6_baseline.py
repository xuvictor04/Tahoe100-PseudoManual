#!/usr/bin/env python3
"""F4 independent: untreated TRIM72 level vs basal p53 activity / responsiveness, own within-plate standardisation.

Per plate (13 reliable plates; plate 13 left out): sum each line's counts over the plate's DMSO wells; log2 CPM
(pseudocount 0.5 count); subtract the plate's median over lines (a line-relative level, removing the plate batch);
average over plates (only plates where the line has >= 2 expected TRIM72 counts). Basal p53 = mean of the 21 targets'
relative levels (targets the line expresses). Spearman with permutation p in WT and altered lines; the panel's
basal_p53_activity_log2 and p53_responsiveness_log2 as alternative outcomes; leave-one-plate-out range.

    python3 verify/v6_baseline.py -> verify/out/v6_*.csv
"""
import os
import numpy as np
import pandas as pd
from scipy import stats

DATA = "/home/user/tahoe_data"
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
rng = np.random.default_rng(23)
P53 = ["CDKN1A", "MDM2", "FDXR", "ZMAT3", "SESN1", "BBC3", "BAX", "TP53I3", "RRM2B", "AEN", "DDB2", "XPC", "PHLDA3",
       "SPATA18", "TRIAP1", "RPS27L", "ACER2", "TP53INP1", "PLK3", "POLH", "EDA2R"]
GENES = ["TRIM72", "TP53"] + P53
sm = pd.read_csv(os.path.join(DATA, "gene_panel", "sample_map.csv"), dtype={"sample": str})
wl = pd.read_parquet(os.path.join(DATA, "gene_panel", "well_line.parquet"),
                     columns=["sample", "cell_line_id", "total_counts"] + GENES)
wl = wl.groupby(["sample", "cell_line_id"], as_index=False).sum().merge(sm[["sample", "plate", "is_dmso"]], on="sample")
wl = wl[wl.is_dmso & (wl.plate != "plate13")]
agg = wl.groupby(["plate", "cell_line_id"])[GENES + ["total_counts"]].sum().reset_index()
E = os.path.join(DATA, "atlas", "effects")
lines = pd.read_csv(os.path.join(E, "lines.csv"))
lid = lines.cell_line_id.astype(str).tolist()
ga = pd.read_csv(os.path.join(E, "genes.csv"))
ga = ga[ga.kind == "gene"].drop_duplicates("symbol").set_index("symbol")
expr = np.load(os.path.join(E, "expr_mask.npy"), mmap_mode="r")
EXPR = pd.DataFrame({g: np.asarray(expr[:, int(ga.loc[g, "col"])]).astype(bool) for g in GENES}, index=lid)
fs = pd.read_csv(os.path.join(DATA, "gene_panel", "results", "p53_functional_status.csv")).set_index("cell_line_id")
tp = pd.read_csv(os.path.join(DATA, "gene_panel", "results", "baseline_by_cell_line.csv")).set_index(
    "cell_line_id")["tp53_group"]

per_plate = []
for plate, a in agg.groupby("plate"):
    a = a.set_index("cell_line_id")
    rel = {}
    for g in GENES:
        cpm = 1e6 * a[g] / a.total_counts
        expd = a.total_counts * cpm[EXPR[g].reindex(a.index).fillna(False)].median() / 1e6
        lv = np.log2((a[g] + 0.5) / a.total_counts * 1e6)
        r = lv - lv[EXPR[g].reindex(a.index).fillna(False)].median()
        r[~EXPR[g].reindex(a.index).fillna(False)] = np.nan
        if g == "TRIM72":
            r[expd < 2] = np.nan
        rel[g] = r
    R = pd.DataFrame(rel)
    R["basal_p53"] = R[P53].mean(axis=1)
    R["plate"] = plate
    per_plate.append(R.reset_index())
PP = pd.concat(per_plate)
PP.to_csv(os.path.join(OUT, "v6_per_plate_line.csv"), index=False)


def summarise(df):
    S = df.groupby("cell_line_id")[["TRIM72", "TP53", "MDM2", "CDKN1A", "basal_p53"]].mean()
    S["basal_p53_panel"] = fs["basal_p53_activity_log2"].reindex(S.index)
    S["p53_responsiveness_panel"] = fs["p53_responsiveness_log2"].reindex(S.index)
    S["tp53"] = tp.reindex(S.index)
    return S


def sp(x, y, nperm=4000):
    ok = np.isfinite(x) & np.isfinite(y)
    x, y = stats.rankdata(x[ok]), stats.rankdata(y[ok])
    r = np.corrcoef(x, y)[0, 1]
    null = np.array([np.corrcoef(x[rng.permutation(len(x))], y)[0, 1] for _ in range(nperm)])
    return int(ok.sum()), float(r), float((1 + (np.abs(null) >= abs(r) - 1e-12).sum()) / (nperm + 1))


S = summarise(PP)
S.to_csv(os.path.join(OUT, "v6_per_line.csv"))
rows = []
for grp in ("WT", "altered"):
    g = S[S.tp53 == grp]
    for y in ("basal_p53", "basal_p53_panel", "p53_responsiveness_panel", "MDM2", "CDKN1A", "TP53"):
        n, r, p = sp(g.TRIM72.to_numpy(), g[y].to_numpy())
        lopo = []
        for pl_ in PP.plate.unique():
            gg = summarise(PP[PP.plate != pl_])
            gg = gg[gg.tp53 == grp]
            ok = gg.TRIM72.notna() & gg[y].notna()
            lopo.append(stats.spearmanr(gg.TRIM72[ok], gg[y][ok])[0])
        rows.append(dict(group=grp, y=y, n=n, rho=r, p_perm=p, leave_one_plate_out_min=min(lopo),
                         leave_one_plate_out_max=max(lopo)))
R = pd.DataFrame(rows)
R["q_bh"] = stats.false_discovery_control(R.p_perm)
R.to_csv(os.path.join(OUT, "v6_baseline_tests.csv"), index=False)
an = pd.read_csv(os.path.join(os.path.dirname(HERE), "tables", "b_baseline_per_line.csv")).set_index("cell_line_id")
col = [c for c in an.columns if c.startswith("TRIM72_rel") and "reliable" in c][0]
ok = S.TRIM72.notna() & an[col].reindex(S.index).notna()
print("agreement with analysis", col, "spearman", round(stats.spearmanr(S.TRIM72[ok], an[col].reindex(S.index)[ok])[0], 3),
      "n", int(ok.sum()))
pd.set_option("display.width", 200)
print(R.round(3).to_string())
