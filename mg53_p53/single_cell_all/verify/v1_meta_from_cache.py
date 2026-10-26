"""Verifier: recompute the two-stage DerSimonian-Laird meta and the WT-minus-altered contrast from the cached per-group
fits with independent code; robustness of the line-level contrast (unweighted, rank, leave-one-line-out, functional p53
status, ambient-heavy lines out)."""
import sys, json, numpy as np, pandas as pd
from scipy import stats
D = sys.argv[1]; data = sys.argv[2]; outdir = sys.argv[3]
rng = np.random.default_rng(7)
info = json.load(open(f"{D}/cache/run_info.json"))
outs = info["params"]["outcomes"]; preds = ["TRIM72"] + info["params"]["placebo"]
g = pd.read_csv(f"{D}/tables/groups.csv.gz")
F = pd.read_parquet(f"{D}/cache/fits.parquet", columns=["pred", "outcome", "beta", "se", "gid"])
F = F[F["gid"].isin(np.where(g["fitted"].fillna(False).astype(bool))[0])]
F = F[np.isfinite(F["beta"]) & np.isfinite(F["se"]) & (F["se"] > 0)]
for c in ("well_class", "cell_line_id", "tp53_group", "sample", "cell_name", "plate"):
    F[c] = g[c].to_numpy()[F["gid"].to_numpy()]

def dl(b, s):
    b = np.asarray(b, float); v = np.asarray(s, float) ** 2
    w = 1 / v; k = len(b)
    if k == 0: return np.nan, np.nan, 0.0, 0.0
    fe = np.sum(w * b) / np.sum(w); Q = np.sum(w * (b - fe) ** 2)
    c = np.sum(w) - np.sum(w ** 2) / np.sum(w)
    t2 = max(0.0, (Q - (k - 1)) / c) if (k > 1 and c > 0) else 0.0
    ws = 1 / (v + t2)
    I2 = max(0.0, (Q - (k - 1)) / Q) if Q > 0 else 0.0
    return np.sum(ws * b) / np.sum(ws), np.sqrt(1 / np.sum(ws)), t2, I2

def lines_table(h):
    rows = []
    for (cid, tp), x in h.groupby(["cell_line_id", "tp53_group"]):
        e, s, t2, _ = dl(x["beta"], x["se"])
        rows.append(dict(cell_line_id=cid, cell_name=x["cell_name"].iloc[0], tp=tp, est=e, se=s, n_wells=len(x)))
    return pd.DataFrame(rows)

def contrast(L):
    w = L[L.tp == "WT"]; a = L[L.tp == "altered"]
    ew, sw, _, I2w = dl(w.est, w.se); ea, sa, _, I2a = dl(a.est, a.se)
    return ew, sw, ea, sa, ew - ea, np.hypot(sw, sa), I2w, I2a

def perm_p(L, n=20000):
    obs = contrast(L)[4]
    lab = (L.tp == "WT").to_numpy(); ex = 0
    for _ in range(n):
        p = rng.permutation(lab)
        e1 = dl(L.est[p], L.se[p])[0]; e0 = dl(L.est[~p], L.se[~p])[0]
        ex += abs(e1 - e0) >= abs(obs) - 1e-12
    return (1 + ex) / (n + 1)

rep = []
classes = ["DMSO", "TRIM72 raisers", "p53 activators", "other drugs", "all wells"]
for oname in ["P53_SCORE", "P53_PRIMARY5", "MDM2", "CDKN1A", "XPC", "DDB2", "ZMAT3", "ATF3", "TP53", "PMAIP1"]:
    oi = outs.index(oname)
    for cl in classes:
        h = F[(F.pred == 0) & (F.outcome == oi)]
        if cl != "all wells": h = h[h.well_class == cl]
        L = lines_table(h)
        ew, sw, ea, sa, d, sd, I2w, I2a = contrast(L)
        pp = perm_p(L, 4000) if (oname in ("P53_SCORE", "XPC", "DDB2") and cl == "all wells") or (oname == "P53_SCORE") else np.nan
        rep.append(dict(outcome=oname, cls=cl, n_WT=int((L.tp == "WT").sum()), n_alt=int((L.tp == "altered").sum()), logrr_WT=ew, se_WT=sw,
                        logrr_alt=ea, se_alt=sa, diff=d, se_diff=sd, I2_WT=I2w, I2_alt=I2a, p_perm_own=pp))
R = pd.DataFrame(rep)
pd.set_option("display.width", 250); pd.set_option("display.max_columns", 30)
print("== own two-stage DL recompute from cache/fits.parquet (TRIM72 predictor)")
print(R.round(4).to_string(index=False))
R.to_csv(f"{outdir}/own_meta_from_cache.csv", index=False)
# compare with the table
T = pd.read_csv(f"{D}/tables/trim72_WT_minus_altered.csv")
m = R.merge(T, left_on=["outcome", "cls"], right_on=["outcome", "class"], suffixes=("", "_tab"))
print("max |own diff - table diff|:", np.nanmax(np.abs(m["diff"] - m["diff_tab"])), " max |se|:", np.nanmax(np.abs(m["se_diff"] - m["se_diff_tab"])))

# ---- robustness of the primary contrast at the line level (P53_SCORE, all wells)
oi = outs.index("P53_SCORE")
L = lines_table(F[(F.pred == 0) & (F.outcome == oi)])
st = pd.read_csv(f"{data}/gene_panel/results/p53_functional_status.csv")[["cell_line_id", "functional_call", "p53_responsiveness_log2"]]
L = L.merge(st, on="cell_line_id", how="left")
amb = pd.read_csv(f"{outdir}/ambient_soup_fraction_by_line.csv")[["cell_name", "soup_fraction_est", "cpm"]]
L = L.merge(amb, on="cell_name", how="left")
w = L[L.tp == "WT"].est; a = L[L.tp == "altered"].est
print("\n== P53_SCORE all wells, line level: unweighted mean WT %.4f altered %.4f diff %.4f; Welch p %.3f; Mann-Whitney p %.3f" % (
    w.mean(), a.mean(), w.mean() - a.mean(), stats.ttest_ind(w, a, equal_var=False).pvalue, stats.mannwhitneyu(w, a).pvalue))
loo = []
for i in range(len(L)):
    loo.append(contrast(L.drop(L.index[i]))[4])
print("leave-one-line-out diff range: %.4f to %.4f" % (min(loo), max(loo)))
# functional p53 status instead of genotype
Lf = L[L.functional_call.isin(["responsive", "unresponsive"])].copy()
Lf["tp"] = np.where(Lf.functional_call == "responsive", "WT", "altered")
c = contrast(Lf)
print("functional: responsive (n=%d) minus unresponsive (n=%d): diff %.4f se %.4f, p_perm %.4f" % ((Lf.tp == "WT").sum(), (Lf.tp == "altered").sum(), c[4], c[5], perm_p(Lf, 4000)))
# meta-regression of line estimates on p53 responsiveness (WLS with DL tau2 of all lines)
_, _, t2, _ = dl(L.est, L.se)
ok = np.isfinite(L.p53_responsiveness_log2)
X = np.column_stack([np.ones(ok.sum()), L.p53_responsiveness_log2[ok]]); W = 1 / (L.se[ok] ** 2 + t2)
XtW = X.T * W.to_numpy(); beta = np.linalg.solve(XtW @ X, XtW @ L.est[ok]); cov = np.linalg.inv(XtW @ X)
print("meta-regression slope of TRIM72 log RR (P53_SCORE) per log2 unit of p53 responsiveness: %.4f (se %.4f, p %.3f)" % (beta[1], np.sqrt(cov[1, 1]), 2 * stats.norm.sf(abs(beta[1] / np.sqrt(cov[1, 1])))))
# ambient-heavy lines out (soup fraction estimated with the deleted-gene rho 0.068 instead of H661's 0.208)
L["soup_frac_rho068"] = L.soup_fraction_est * 0.068 / 0.208
for thr in (0.15, 0.10):
    Lk = L[L.soup_frac_rho068 < thr]
    c = contrast(Lk)
    print("lines with soup fraction < %.2f: WT %d, altered %d; diff %.4f se %.4f p_perm %.4f" % (thr, (Lk.tp == "WT").sum(), (Lk.tp == "altered").sum(), c[4], c[5], perm_p(Lk, 4000)))
L.to_csv(f"{outdir}/line_level_P53_SCORE_all_wells.csv", index=False)
# do line-level TRIM72 associations scale with the soup fraction? (ATF3, TP53, P53_SCORE)
for oname in ["P53_SCORE", "ATF3", "TP53", "PMAIP1"]:
    Lo = lines_table(F[(F.pred == 0) & (F.outcome == outs.index(oname))]).merge(amb, on="cell_name", how="left")
    r = stats.spearmanr(Lo.est, Lo.soup_fraction_est, nan_policy="omit")
    print(f"{oname}: Spearman of line TRIM72 log RR with soup fraction: rho {r.correlation:.3f} p {r.pvalue:.3f} (n {Lo.est.notna().sum()})")
