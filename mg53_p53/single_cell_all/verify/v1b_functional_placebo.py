"""Verifier: TP53 functional status (gene panel responsive vs unresponsive; responsiveness as a continuous moderator)
instead of genotype, for TRIM72 and each of the 16 placebo predictors (cached per-group fits, own two-stage DL)."""
import sys, json, numpy as np, pandas as pd
from scipy import stats
D, data, outdir = sys.argv[1:4]
rng = np.random.default_rng(11)
info = json.load(open(f"{D}/cache/run_info.json"))
outs = info["params"]["outcomes"]; preds = ["TRIM72"] + info["params"]["placebo"]
g = pd.read_csv(f"{D}/tables/groups.csv.gz")
F = pd.read_parquet(f"{D}/cache/fits.parquet", columns=["pred", "outcome", "beta", "se", "gid"])
F = F[F["gid"].isin(np.where(g["fitted"].fillna(False).astype(bool))[0])]
F = F[np.isfinite(F["beta"]) & np.isfinite(F["se"]) & (F["se"] > 0)]
F["cell_line_id"] = g["cell_line_id"].to_numpy()[F["gid"].to_numpy()]
F["tp53_group"] = g["tp53_group"].to_numpy()[F["gid"].to_numpy()]
F["well_class"] = g["well_class"].to_numpy()[F["gid"].to_numpy()]
st = pd.read_csv(f"{data}/gene_panel/results/p53_functional_status.csv")[["cell_line_id", "functional_call", "p53_responsiveness_log2"]]

def dl(b, v):
    w = 1 / v; k = len(b); fe = np.sum(w * b) / np.sum(w); Q = np.sum(w * (b - fe) ** 2)
    c = np.sum(w) - np.sum(w ** 2) / np.sum(w); t2 = max(0.0, (Q - (k - 1)) / c) if (k > 1 and c > 0) else 0.0
    ws = 1 / (v + t2); return np.sum(ws * b) / np.sum(ws), np.sqrt(1 / np.sum(ws)), t2

def lines(h):
    r = []
    for cid, x in h.groupby("cell_line_id"):
        e, s, _ = dl(x.beta.to_numpy(float), x.se.to_numpy(float) ** 2); r.append((cid, x.tp53_group.iloc[0], e, s))
    return pd.DataFrame(r, columns=["cell_line_id", "tp", "est", "se"]).merge(st, on="cell_line_id", how="left")

def stats_of(L, nperm=0):
    out = {}
    for lab, a_, b_ in (("genotype", L.tp == "WT", L.tp == "altered"),
                        ("functional", L.functional_call == "responsive", L.functional_call == "unresponsive")):
        e1, s1, _ = dl(L.est[a_].to_numpy(), L.se[a_].to_numpy() ** 2); e0, s0, _ = dl(L.est[b_].to_numpy(), L.se[b_].to_numpy() ** 2)
        out[lab] = e1 - e0
    ok = L.p53_responsiveness_log2.notna()
    _, _, t2 = dl(L.est[ok].to_numpy(), L.se[ok].to_numpy() ** 2)
    X = np.column_stack([np.ones(ok.sum()), L.p53_responsiveness_log2[ok]]); W = 1 / (L.se[ok].to_numpy() ** 2 + t2)
    XtW = X.T * W; bta = np.linalg.solve(XtW @ X, XtW @ L.est[ok].to_numpy()); out["slope"] = bta[1]
    out["slope_se"] = np.sqrt(np.linalg.inv(XtW @ X)[1, 1])
    return out

rows = []
for oname in ["P53_SCORE", "P53_PRIMARY5", "MDM2", "CDKN1A", "XPC", "DDB2", "ATF3", "TP53"]:
    oi = outs.index(oname)
    for cl in ["all wells", "DMSO", "other drugs"]:
        for pi, pn in enumerate(preds):
            h = F[(F.pred == pi) & (F.outcome == oi)]
            if cl != "all wells": h = h[h.well_class == cl]
            if h.empty: continue
            L = lines(h)
            s = stats_of(L)
            rows.append(dict(outcome=oname, cls=cl, predictor=pn, n_lines=len(L), **s))
R = pd.DataFrame(rows)
R.to_csv(f"{outdir}/functional_status_contrasts.csv", index=False)
summ = []
for (o, cl), h in R.groupby(["outcome", "cls"], sort=False):
    t = h[h.predictor == "TRIM72"].iloc[0]; p = h[h.predictor != "TRIM72"]
    d = dict(outcome=o, cls=cl)
    for k in ("genotype", "functional", "slope"):
        v = p[k].to_numpy(); med = np.median(v)
        d[f"TRIM72_{k}"] = t[k]; d[f"plac_med_{k}"] = med
        d[f"pct_{k}"] = 100 * np.mean(v < t[k]); d[f"emp_p_{k}"] = (1 + np.sum(np.abs(v - med) >= abs(t[k] - med))) / (len(v) + 1)
    d["slope_z_TRIM72"] = t["slope"] / t["slope_se"]
    summ.append(d)
S = pd.DataFrame(summ)
pd.set_option("display.width", 250); pd.set_option("display.max_columns", 30)
print(S.round(4).to_string(index=False))
# permutation p of the functional contrast for TRIM72 x P53_SCORE all wells (labels over the 38 classified lines)
L = lines(F[(F.pred == 0) & (F.outcome == outs.index("P53_SCORE"))])
Lf = L[L.functional_call.isin(["responsive", "unresponsive"])].reset_index(drop=True)
obs = stats_of(Lf)["functional"]; lab = (Lf.functional_call == "responsive").to_numpy(); ex = 0; n = 5000
for _ in range(n):
    p = rng.permutation(lab)
    e1 = dl(Lf.est[p].to_numpy(), Lf.se[p].to_numpy() ** 2)[0]; e0 = dl(Lf.est[~p].to_numpy(), Lf.se[~p].to_numpy() ** 2)[0]
    ex += abs(e1 - e0) >= abs(obs) - 1e-12
print("TRIM72 x P53_SCORE, all wells, responsive minus unresponsive: %.4f, permutation p %.4f" % (obs, (1 + ex) / (n + 1)))
print(Lf.sort_values("p53_responsiveness_log2", ascending=False)[["cell_line_id", "tp", "functional_call", "p53_responsiveness_log2", "est", "se"]].round(4).to_string(index=False))
