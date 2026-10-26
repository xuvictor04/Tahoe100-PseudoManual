"""Verifier v4 (from the step's cache and tables, own code): Hartung-Knapp CIs for the stage-2 means and the WT-minus-
altered contrast; per-doubling bounds under other overdispersion assumptions; functional p53 status with placebo
calibration; counts behind F6; line characteristics of WT vs altered (is the contrast confounded?)."""
import sys, json, numpy as np, pandas as pd
from scipy import stats
D, data, outdir = sys.argv[1:4]
pd.set_option("display.width", 250); pd.set_option("display.max_columns", 40); pd.set_option("display.max_rows", 300)
info = json.load(open(f"{D}/cache/run_info.json"))
outs = info["params"]["outcomes"]; preds = ["TRIM72"] + info["params"]["placebo"]
g = pd.read_csv(f"{D}/tables/groups.csv.gz")
F = pd.read_parquet(f"{D}/cache/fits.parquet", columns=["pred", "outcome", "beta", "se", "gid"])
fit = g["fitted"].fillna(False).astype(bool).to_numpy()
F = F[fit[F["gid"].to_numpy()] & np.isfinite(F["beta"]) & np.isfinite(F["se"]) & (F["se"] > 0)]
for c in ("well_class", "cell_line_id", "tp53_group", "cell_name"):
    F[c] = g[c].to_numpy()[F["gid"].to_numpy()]
st = pd.read_csv(f"{data}/gene_panel/results/p53_functional_status.csv")


def dl(b, v):
    b = np.asarray(b, float); v = np.asarray(v, float); w = 1 / v; k = len(b)
    fe = np.sum(w * b) / np.sum(w); Q = np.sum(w * (b - fe) ** 2); c = np.sum(w) - np.sum(w ** 2) / np.sum(w)
    t2 = max(0.0, (Q - (k - 1)) / c) if k > 1 else 0.0
    ws = 1 / (v + t2); m = np.sum(ws * b) / np.sum(ws)
    se = np.sqrt(1 / np.sum(ws))
    q_hk = np.sum(ws * (b - m) ** 2) / (k - 1)                 # Hartung-Knapp(-Sidik-Jonkman) scale
    se_hk = np.sqrt(q_hk / np.sum(ws))
    return m, se, se_hk, k, t2


def lines_of(pi, oi, cls="all wells"):
    h = F[(F.pred == pi) & (F.outcome == oi)]
    if cls != "all wells":
        h = h[h.well_class == cls]
    r = []
    for cid, x in h.groupby("cell_line_id"):
        m, s, _, k, _ = dl(x.beta, x.se ** 2)
        r.append((cid, x.tp53_group.iloc[0], x.cell_name.iloc[0], m, s, k))
    return pd.DataFrame(r, columns=["cell_line_id", "tp", "cell_name", "est", "se", "n_wells"])


print("== 1. DL vs Hartung-Knapp (t, k-1 df) for the stage-2 means and the contrast, TRIM72, all wells")
rows = []
for o in ["P53_SCORE", "P53_PRIMARY5", "MDM2", "XPC", "DDB2", "ATF3"]:
    for cls in ["all wells", "DMSO", "other drugs"]:
        L = lines_of(0, outs.index(o), cls)
        r = {}
        for tp in ("WT", "altered"):
            x = L[L.tp == tp]
            r[tp] = dl(x.est, x.se ** 2)
        (mw, sw, hw, kw, _), (ma, sa, ha, ka, _) = r["WT"], r["altered"]
        d = mw - ma
        se_dl = np.hypot(sw, sa); se_hk = np.hypot(hw, ha)
        dfw = (hw ** 2 + ha ** 2) ** 2 / (hw ** 4 / (kw - 1) + ha ** 4 / (ka - 1))     # Welch-Satterthwaite
        tq = stats.t.ppf(0.975, dfw)
        rows.append(dict(outcome=o, cls=cls, diff=d, ci_dl=f"{d - 1.96 * se_dl:.4f} to {d + 1.96 * se_dl:.4f}",
                         se_dl=se_dl, se_hk=se_hk, df=dfw, ci_hk=f"{d - tq * se_hk:.4f} to {d + tq * se_hk:.4f}",
                         p_hk=2 * stats.t.sf(abs(d) / se_hk, dfw), se_WT_dl=sw, se_WT_hk=hw, se_alt_dl=sa, se_alt_hk=ha))
HK = pd.DataFrame(rows)
print(HK.round(4).to_string(index=False))

print("\n== 2. per-doubling CI of the P53_SCORE WT-minus-altered contrast under other overdispersion assumptions")
cs = pd.read_csv(f"{D}/tables/class_summary.csv")
gg = g[g["fitted"].fillna(False).astype(bool)]


def implied(a, m):
    p0 = (1 + a * m) ** (-1 / a); e0 = m / (1 + a * m); e1 = (m - p0 * e0) / (1 - p0); return e1 / e0


L = lines_of(0, outs.index("P53_SCORE"))
mw, sw, hw, kw, _ = dl(L[L.tp == "WT"].est, L[L.tp == "WT"].se ** 2)
ma, sa, ha, ka, _ = dl(L[L.tp == "altered"].est, L[L.tp == "altered"].se ** 2)
for lab, fac in (("alpha as estimated", 1.0), ("half of alpha biological", 0.5), ("a quarter biological", 0.25)):
    d2 = {}
    for tp in ("WT", "altered"):
        a = cs[(cs["class"] == "all wells") & (cs.tp53_group == tp)].alpha_TRIM72_pooled.iloc[0] * fac
        m = gg[gg.tp53_group == tp].mean_expected_TRIM72_per_cell.to_numpy()
        d2[tp] = np.median(np.log2(implied(a, m)))
    for selab, (s1, s0) in (("DL", (sw, sa)), ("HK", (hw, ha))):
        e = mw / d2["WT"] - ma / d2["altered"]; s = np.hypot(s1 / d2["WT"], s0 / d2["altered"])
        print(f"  {lab:28s} log2 ratio WT {d2['WT']:.2f} alt {d2['altered']:.2f}; {selab}: per doubling "
              f"{np.exp(e):.4f} ({np.exp(e - 1.96 * s):.4f} to {np.exp(e + 1.96 * s):.4f}); MDE80 {100 * (np.exp(2.8 * s) - 1):.1f}%")
# log-log (power-law) dose-response: E[log lambda | y>=1] - E[log lambda | y=0] = alpha (nats) for y=1 vs 0 (gamma)
for tp in ("WT", "altered"):
    a = cs[(cs["class"] == "all wells") & (cs.tp53_group == tp)].alpha_TRIM72_pooled.iloc[0]
    print(f"  power-law reading, {tp}: E[log2 rate] contrast of a 1-UMI cell vs 0 = alpha / ln 2 = {a / np.log(2):.2f} "
          f"(vs log2 of the mean ratio used: ~2.0-2.2)")

print("\n== 3. functional p53 status (gene panel call) instead of genotype, with the placebo predictors")
rows = []
for o in ["P53_SCORE", "P53_PRIMARY5", "MDM2", "CDKN1A", "XPC", "DDB2", "ATF3", "TP53"]:
    for pi, pn in enumerate(preds):
        L = lines_of(pi, outs.index(o)).merge(st[["cell_line_id", "functional_call", "p53_responsiveness_log2"]],
                                              on="cell_line_id", how="left")
        a = L[L.functional_call == "responsive"]; b = L[L.functional_call == "unresponsive"]
        if len(a) < 3 or len(b) < 3:
            continue
        ra, rb = dl(a.est, a.se ** 2), dl(b.est, b.se ** 2)
        gw = L[L.tp == "WT"]; ga = L[L.tp == "altered"]
        rw, rl = dl(gw.est, gw.se ** 2), dl(ga.est, ga.se ** 2)
        rows.append(dict(outcome=o, predictor=pn, n_resp=len(a), n_unresp=len(b), func_diff=ra[0] - rb[0],
                         func_se=np.hypot(ra[1], rb[1]), geno_diff=rw[0] - rl[0], geno_se=np.hypot(rw[1], rl[1])))
FX = pd.DataFrame(rows)
out = []
for o, h in FX.groupby("outcome", sort=False):
    t = h[h.predictor == "TRIM72"].iloc[0]; p = h[h.predictor != "TRIM72"]
    for k in ("func", "geno"):
        v = p[f"{k}_diff"].to_numpy(); med = np.median(v); sd = np.std(v, ddof=1)
        z = (t[f"{k}_diff"] - med) / np.sqrt(t[f"{k}_se"] ** 2 + sd ** 2)
        out.append(dict(outcome=o, contrast={"func": "responsive - unresponsive", "geno": "WT - altered"}[k],
                        TRIM72=t[f"{k}_diff"], se=t[f"{k}_se"], placebo_median=med, placebo_sd=sd, placebo_max=v.max(),
                        n_placebos=len(v), pct=100 * np.mean(v < t[f"{k}_diff"]), calibrated_z=z,
                        calibrated_p=2 * stats.norm.sf(abs(z))))
print(pd.DataFrame(out).round(4).to_string(index=False))
FX.to_csv(f"{outdir}/v4_functional_vs_genotype_all_predictors.csv", index=False)
print(st.groupby(["tp53_annotation", "functional_call"]).size().to_string() if "tp53_annotation" in st else "")
L = lines_of(0, outs.index("P53_SCORE")).merge(st[["cell_line_id", "functional_call", "p53_responsiveness_log2"]], on="cell_line_id", how="left")
print(pd.crosstab(L.tp, L.functional_call.fillna("none")))
print("WT lines not 'responsive':", L[(L.tp == "WT") & (L.functional_call != "responsive")][["cell_name", "functional_call", "p53_responsiveness_log2", "est", "se"]].round(3).to_string(index=False))

print("\n== 4. F6 counts: p53 outcomes (29) WT-minus-altered sign and rank among placebos; all wells")
NP = pd.read_csv(f"{D}/tables/placebo_predictor_null.csv")
x = NP[(NP["class"] == "all wells") & (NP.placebos == "all placebos") & (NP.contrast == "WT minus altered")]
p53o = [o for o in x.outcome.unique() if str(x[x.outcome == o].outcome_type.iloc[0]).startswith(("p53", "TP53"))]
xx = x[x.outcome.isin(p53o)]
print(f"p53 outcomes in placebo null: {len(xx)}; positive: {(xx.TRIM72_log_rr > 0).sum()}; above all placebos: "
      f"{(xx.TRIM72_percentile_among_placebos == 100).sum()} -> {sorted(xx[xx.TRIM72_percentile_among_placebos == 100].outcome)}")
T = pd.read_csv(f"{D}/tables/trim72_WT_minus_altered.csv")
t = T[(T["class"] == "all wells") & T.outcome.isin(["XPC", "DDB2", "ZMAT3", "P53_SCORE"])]
print(t[["outcome", "diff", "ci_lo", "ci_hi", "p_perm", "q_bh", "paired_diff", "paired_p_perm"]].round(4).to_string(index=False))
A = pd.read_csv(f"{D}/adjusted_ATF3/tables/trim72_WT_minus_altered.csv")
a = A[(A["class"] == "all wells") & A.outcome.isin(["XPC", "DDB2", "ZMAT3", "P53_SCORE"])]
print("ATF3-adjusted:"); print(a[["outcome", "diff", "p_perm", "q_bh"]].round(4).to_string(index=False))
print("BH family size (p53 + screen, all classes):", int((T.family == "p53 + screen").sum()),
      "; p_perm computed for", int(T.p_perm.notna().sum()), "rows")

print("\n== 5. Are WT and altered lines comparable? line characteristics of the fitted groups")
fitg = g[g["fitted"].fillna(False).astype(bool)]
lc = fitg.groupby(["cell_name", "tp53_group"]).agg(groups=("sample", "size"), cells=("n_cells_used", "sum"),
                                                   det=("n_TRIM72_detected_used", "sum"),
                                                   mbar=("mean_expected_TRIM72_per_cell", "median")).reset_index()
lc["pct_det"] = 100 * lc.det / lc.cells
soup = pd.read_csv(f"{outdir}/ambient_soup_fraction_by_line.csv")[["cell_name", "cpm", "soup_fraction_est"]]
lc = lc.merge(soup, on="cell_name", how="left")
print(lc.groupby("tp53_group")[["groups", "pct_det", "mbar", "cpm", "soup_fraction_est"]].median().round(4))
for c in ("groups", "pct_det", "cpm", "soup_fraction_est"):
    a_, b_ = lc[lc.tp53_group == "WT"][c].dropna(), lc[lc.tp53_group == "altered"][c].dropna()
    print(f"  {c}: Mann-Whitney p {stats.mannwhitneyu(a_, b_).pvalue:.3f}")
# meta-regression: TRIM72 x P53_SCORE line estimate on WT + log TRIM72 CPM (is the contrast robust to expression level?)
L = lines_of(0, outs.index("P53_SCORE")).merge(lc[["cell_name", "cpm", "pct_det"]], on="cell_name", how="left")
ok = L.cpm.notna()
_, _, _, _, t2 = dl(L.est, L.se ** 2)
X = np.column_stack([np.ones(ok.sum()), (L.tp[ok] == "WT").astype(float), np.log(L.cpm[ok])])
W = 1 / (L.se[ok] ** 2 + t2)
XtW = X.T * W.to_numpy(); bta = np.linalg.solve(XtW @ X, XtW @ L.est[ok]); cov = np.linalg.inv(XtW @ X)
print("meta-regression P53_SCORE line log RR ~ WT + log TRIM72 CPM: WT coef %.4f (se %.4f), log CPM coef %.4f (se %.4f)" % (
    bta[1], np.sqrt(cov[1, 1]), bta[2], np.sqrt(cov[2, 2])))

print("\n== 6. which lines drive the 'other drugs' WT heterogeneity (P53_SCORE)")
L = lines_of(0, outs.index("P53_SCORE"), "other drugs").sort_values("est")
print(L[L.tp == "WT"].round(4).to_string(index=False))
