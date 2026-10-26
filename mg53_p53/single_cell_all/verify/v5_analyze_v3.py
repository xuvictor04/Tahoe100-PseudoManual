"""Verifier v5: summarise v3 (own raw-data recompute) against the step's cache, and the confounding variants."""
import sys, json, numpy as np, pandas as pd
from scipy import stats
D, outdir = sys.argv[1:3]
pd.set_option("display.width", 250); pd.set_option("display.max_columns", 40); pd.set_option("display.max_rows", 300)
info = json.load(open(f"{D}/cache/run_info.json"))
OUTS = info["params"]["outcomes"]; PREDS = ["TRIM72"] + info["params"]["placebo"]
g = pd.read_csv(f"{D}/tables/groups.csv.gz"); g["gid"] = np.arange(len(g))
R = pd.read_csv(f"{outdir}/v3_group_fits.csv.gz")
R = R.merge(g[["gid", "tp53_group", "cell_name", "well_class", "sampling_prob", "fitted"]], on="gid", how="left")
R["sep"] = (R.y_det <= 0) | (R.y_tot - R.y_det <= 0) | ~np.isfinite(R.se) | (R.se > 3)
print("own fits flagged as separation / unstable (excluded from sections 2-5):", int(R.sep.sum()), "of", len(R))
F = pd.read_parquet(f"{D}/cache/fits.parquet", columns=["gid", "pred", "outcome", "beta", "se"])
F = F[F.gid.isin(R.gid.unique())]
F["pred"] = np.asarray(PREDS)[F["pred"].to_numpy()]; F["outcome"] = np.asarray(OUTS)[F["outcome"].to_numpy()]

print("== 1. replication of the step's per-group fits (variant 'rep' = same cells, same model, own solver)")
rep = R[R.variant == "rep"].merge(F, on=["gid", "pred", "outcome"], how="outer", suffixes=("_own", "_step"), indicator=True)
print(rep["_merge"].value_counts().to_string())
both = rep[(rep["_merge"] == "both") & np.isfinite(rep.beta_step)]
for lab, h in (("TRIM72 x P53_SCORE", both[(both.pred == "TRIM72") & (both.outcome == "P53_SCORE")]),
               ("TRIM72 x all 8 outcomes", both[both.pred == "TRIM72"]), ("placebo predictors", both[both.pred != "TRIM72"])):
    d = np.abs(h.beta_own - h.beta_step); rs = np.abs(h.se_own - h.se_step) / h.se_step
    print(f"  {lab}: n {len(h)} groups/fits; max |d log RR| {d.max():.2e}; 99th pct {np.quantile(d, .99):.2e}; "
          f"max rel |d SE| {rs.max():.2e}; corr {np.corrcoef(h.beta_own, h.beta_step)[0, 1]:.8f}")
only_own = rep[rep["_merge"] == "left_only"]; only_step = rep[rep["_merge"] == "right_only"]
print(f"  fits only in own: {len(only_own)} (outcomes {only_own.outcome.value_counts().to_dict()}); only in step: {len(only_step)}"
      f" (finite in step: {int(np.isfinite(only_step.beta_step).sum())})")
h = both[(both.pred == "TRIM72") & (both.outcome == "P53_SCORE")]
print(f"  random-subset TRIM72 x P53_SCORE: {h.gid.nunique()} groups ({(h.tp53_group == 'WT').sum()} WT, "
      f"{(h.tp53_group == 'altered').sum()} altered, {h.cell_name.nunique()} lines, {h.well_class.value_counts().to_dict()})")
for tp in ("WT", "altered"):
    x = h[h.tp53_group == tp]
    for lab, b, s in (("own", x.beta_own, x.se_own), ("step", x.beta_step, x.se_step)):
        w = 1 / s ** 2
        print(f"    {tp:8s} {lab}: inverse-variance mean log RR {np.sum(w * b) / np.sum(w):.5f} (se {np.sqrt(1 / np.sum(w)):.5f})")


def line_cluster(dlt, lines):
    m = pd.Series(np.asarray(dlt)).groupby(np.asarray(lines)).mean()
    return m.mean(), m.std(ddof=1) / np.sqrt(len(m)), len(m)


print("\n== 2. variants vs all cells (paired per group; mean shift with line-clustered SE), TRIM72 predictor")
A = R[(R.variant == "all") & ~R.sep].set_index(["gid", "pred", "outcome"])
rows = []
for var in ("rep", "nocc", "flex", "trim95", "dose"):
    V = R[(R.variant == var) & ~R.sep].set_index(["gid", "pred", "outcome"])
    j = V.join(A[["beta", "se"]], rsuffix="_all", how="inner").reset_index()
    j = j[np.isfinite(j.beta) & np.isfinite(j.beta_all)]
    for o in ["P53_SCORE", "MDM2", "CDKN1A", "XPC", "DDB2", "ATF3", "TP53", "PMAIP1"]:
        r = {}
        for tp in ("WT", "altered"):
            x = j[(j.pred == "TRIM72") & (j.outcome == o) & (j.tp53_group == tp)]
            if len(x) < 5:
                continue
            m, s, nl = line_cluster(x.beta - x.beta_all, x.cell_name)
            r[tp] = (m, s)
            rows.append(dict(variant=var, outcome=o, tp=tp, n_groups=len(x), n_lines=nl, mean_all=x.beta_all.mean(),
                             mean_variant=x.beta.mean(), shift=m, shift_se=s))
        if len(r) == 2:
            rows.append(dict(variant=var, outcome=o, tp="WT minus altered", shift=r["WT"][0] - r["altered"][0],
                             shift_se=np.hypot(r["WT"][1], r["altered"][1])))
V2 = pd.DataFrame(rows)
print(V2.round(4).to_string(index=False))

print("\n== 3. generic 'any low gene detected' effect: placebo predictors under each model (mean log RR over groups)")
rows = []
for var in ("rep", "all", "nocc", "flex"):
    for o in ("P53_SCORE", "ATF3"):
        for tp in ("WT", "altered"):
            x = R[(R.variant == var) & (R.outcome == o) & (R.tp53_group == tp) & np.isfinite(R.beta) & ~R.sep]
            pl = x[x.pred != "TRIM72"].groupby("pred").beta.mean()
            t = x[x.pred == "TRIM72"].beta.mean()
            rows.append(dict(variant=var, outcome=o, tp=tp, TRIM72_mean=t, placebo_median_of_means=pl.median(),
                             placebo_min=pl.min(), placebo_max=pl.max(), TRIM72_pct=100 * np.mean(pl < t)))
print(pd.DataFrame(rows).round(4).to_string(index=False))

print("\n== 4. dose: 1 UMI vs >= 2 UMI (both vs 0), random-effects (DL) over groups")


def dl(b, v):
    b, v = np.asarray(b, float), np.asarray(v, float); w = 1 / v; k = len(b)
    fe = np.sum(w * b) / np.sum(w); Q = np.sum(w * (b - fe) ** 2); c = np.sum(w) - np.sum(w ** 2) / np.sum(w)
    t2 = max(0.0, (Q - (k - 1)) / c); ws = 1 / (v + t2)
    return np.sum(ws * b) / np.sum(ws), np.sqrt(1 / np.sum(ws)), k


Dd = R[(R.variant == "dose") & (R.pred == "TRIM72") & ~R.sep]
for o in ["P53_SCORE", "ATF3", "TP53", "XPC", "DDB2", "MDM2"]:
    for tp in ("WT", "altered"):
        x = Dd[(Dd.outcome == o) & (Dd.tp53_group == tp)]
        x1 = x[np.isfinite(x.beta) & (x.se > 0) & (x.se < 5)]
        x2 = x[np.isfinite(x.beta2) & (x.se2 > 0) & (x.se2 < 5) & (x.n_det2 >= 3)]
        a = dl(x1.beta, x1.se ** 2); b = dl(x2.beta2, x2.se2 ** 2)
        print(f"  {o:9s} {tp:8s} 1 UMI: {a[0]:+.4f} (se {a[1]:.4f}, {a[2]} groups)   >=2 UMI: {b[0]:+.4f} (se {b[1]:.4f}, {b[2]} groups)")

print("\n== 5. groups dropped after the subsample (refit with all cells) vs fitted groups, TRIM72 x P53_SCORE")
x = R[(R.variant == "all") & (R.pred == "TRIM72") & (R.outcome == "P53_SCORE") & np.isfinite(R.beta) & ~R.sep]
for lab, h in (("dropped", x[~x.fitted.fillna(False).astype(bool)]), ("fitted", x[x.fitted.fillna(False).astype(bool)])):
    for tp in ("WT", "altered"):
        y = h[h.tp53_group == tp]
        if len(y) >= 3:
            m, s, k = dl(y.beta, y.se ** 2)
            print(f"  {lab:8s} {tp:8s} n {len(y)}: DL mean {m:+.4f} (se {s:.4f}); median n_det {y.n_det.median():.0f}")

print("\n== 6. TRIM72 UMI distribution in detected cells and depth of detected vs undetected (random groups, all cells)")
C = pd.read_parquet(f"{outdir}/v3_cells.parquet", columns=["gid", "total_counts", "n_genes", "TRIM72", "S_PHASE", "G2M_PHASE", "is_h661"])
c = C[C.gid >= 0].merge(g[["gid", "tp53_group", "fitted"]], on="gid")
c = c[c.fitted.fillna(False).astype(bool)]
d = c[c.TRIM72 > 0]
print(f"  detected cells {len(d):,}: 1 UMI {100 * np.mean(d.TRIM72 == 1):.1f}%, 2 {100 * np.mean(d.TRIM72 == 2):.1f}%, >=3 {100 * np.mean(d.TRIM72 >= 3):.1f}%")
c["logT"] = np.log(c.total_counts); c["lt_c"] = c["logT"] - c.groupby("gid")["logT"].transform("mean")
c["ng_c"] = np.log(c.n_genes) - c.groupby("gid").n_genes.transform(lambda v: np.log(v).mean())
c["top5"] = c.total_counts > c.groupby("gid").total_counts.transform(lambda v: np.quantile(v, 0.95))
c["g2m"] = np.log((c.G2M_PHASE + 0.5) / c.total_counts); c["g2m_c"] = c.g2m - c.groupby("gid").g2m.transform("mean")
c["s"] = np.log((c.S_PHASE + 0.5) / c.total_counts); c["s_c"] = c.s - c.groupby("gid").s.transform("mean")
for tp in ("WT", "altered"):
    h = c[c.tp53_group == tp]; det = h.TRIM72 > 0
    print(f"  {tp}: detected vs undetected, within-group mean log total UMI diff {h.lt_c[det].mean() - h.lt_c[~det].mean():+.3f}; "
          f"log n_genes {h.ng_c[det].mean() - h.ng_c[~det].mean():+.3f}; in top 5% UMI {100 * h.top5[det].mean():.1f}% vs "
          f"{100 * h.top5[~det].mean():.1f}%; log S frac {h.s_c[det].mean() - h.s_c[~det].mean():+.3f}; log G2M frac "
          f"{h.g2m_c[det].mean() - h.g2m_c[~det].mean():+.3f}")
hh = C[C.is_h661]
print(f"  NCI-H661: {len(hh):,} cells, {int((hh.TRIM72 > 0).sum())} detected ({100 * np.mean(hh.TRIM72 > 0):.2f}%), 1 UMI among them "
      f"{100 * np.mean(hh.TRIM72[hh.TRIM72 > 0] == 1):.1f}%")

print("\n== 7. NCI-H661 (TRIM72 not expressed): well-fixed-effect Poisson, 'gene detected' vs not")
H = pd.read_csv(f"{outdir}/v3_h661_fe.csv")
for cells, h in H.groupby("cells", sort=False):
    t = h[h.pred == "TRIM72"].set_index("outcome")
    p = h[h.pred != "TRIM72"]
    s = p.groupby("outcome").log_rr.agg(["median", "min", "max", "size"])
    out = t[["n_det", "pct_det", "pct_det_1umi", "log_rr", "se", "rr"]].join(s.add_prefix("placebo_"))
    out["TRIM72_pct_among_placebos"] = [100 * np.mean(p[p.outcome == o].log_rr < t.loc[o, "log_rr"]) for o in out.index]
    print(f"  -- {cells}"); print(out.round(4).to_string())
