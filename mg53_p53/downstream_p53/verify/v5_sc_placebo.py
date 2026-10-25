#!/usr/bin/env python3
"""F7/F8 adversarial: is anything about the TRIM72-detected cells specific to TRIM72?

1. Placebo predictors: the same per-line quasi-Poisson GLM as v2 (offset log UMI; log UMI, (log UMI)^2, log S and G2M
   module fractions, well), but with 'cell has >= 1 UMI of gene X' for every other panel gene X whose detection rate in
   the well set is within 1/3x-3x of TRIM72's (p53 targets, TP53, ATF3, PMAIP1 excluded as predictors). If detection of
   an arbitrary low-abundance transcript also goes with more ATF3 / PMAIP1 (or with p53 targets), the TRIM72 result
   is a generic cell-state / capture effect. Outcomes: P53_SUM (21 targets summed), ATF3, PMAIP1, MDM2, CDKN1A.
2. Information content of 'TRIM72 detected': per line, the negative-binomial overdispersion of TRIM72 counts given
   depth (moment estimator alpha = sum((y-mu)^2 - y) / sum(mu^2), mu = depth x line rate per well); under a gamma model
   the implied ratio of the true TRIM72 rate in detected vs undetected cells; and what the P53_SUM CI implies per
   doubling of true TRIM72 (elasticity bound).

Reads verify/out/v2_cells.parquet (written by v2_single_cell.py from gene_panel/cells).
    python3 verify/v5_sc_placebo.py -> verify/out/v5_*.csv
"""
import os
import numpy as np
import pandas as pd
from scipy import stats

DATA = "/home/user/tahoe_data"
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
P53 = ["CDKN1A", "MDM2", "FDXR", "ZMAT3", "SESN1", "BBC3", "BAX", "TP53I3", "RRM2B", "AEN", "DDB2", "XPC", "PHLDA3",
       "SPATA18", "TRIAP1", "RPS27L", "ACER2", "TP53INP1", "PLK3", "POLH", "EDA2R"]
STRESS = {"DDIT3", "ASNS", "TRIB3", "CHAC1", "PSAT1", "PHGDH", "PSPH", "SLC3A2", "SLC7A5", "SLC7A11", "CEBPB", "VEGFA",
          "HSPA1A", "HSPA1B", "DNAJB1", "HSPH1", "HSPA6", "BAG3", "HSPA5", "HERPUD1", "DNAJB9", "SDF2L1", "SEL1L", "PDIA4",
          "XBP1", "NFKBIA", "TNFAIP3", "RELB", "NFKB2", "BIRC3", "CXCL8", "ICAM1", "IER3", "PTGS2", "GADD45A", "SESN2",
          "TNFRSF10B", "CCNG1", "BTG2", "TIGAR", "HMOX1", "NQO1", "GCLM", "GCLC", "TXNRD1", "SRXN1", "OSGIN1", "AKR1C1",
          "AKR1C2", "AKR1B10", "ME1", "G6PD", "PIR", "ABCC3", "NFE2L2", "IL1B", "IFIT1", "IFIT3", "MX1", "OAS1", "IFI6",
          "IFI44L", "STAT1", "IRF7", "IFITM1", "ISG15"}
OUTCOMES = ["P53_SUM", "ATF3", "PMAIP1", "MDM2", "CDKN1A"]
rng = np.random.default_rng(13)

cells = pd.read_parquet(os.path.join(OUT, "v2_cells.parquet"))
panel = [c for c in cells.columns if c not in ("barcode", "sample", "plate", "drug", "cell_line_id", "n_genes",
                                                "total_counts", "PROTEASOME", "S_PHASE", "G2M_PHASE")]
lines = pd.read_csv(os.path.join(DATA, "atlas", "effects", "lines.csv"))
lid = lines.cell_line_id.astype(str).tolist()
ga = pd.read_csv(os.path.join(DATA, "atlas", "effects", "genes.csv"))
ga = ga[ga.kind == "gene"].drop_duplicates("symbol").set_index("symbol")
expr = np.load(os.path.join(DATA, "atlas", "effects", "expr_mask.npy"), mmap_mode="r")
EXPR = pd.DataFrame({g: np.asarray(expr[:, int(ga.loc[g, "col"])]).astype(bool) for g in panel if g in ga.index},
                    index=lid)
_pl = pd.read_csv(os.path.join(os.path.dirname(HERE), "cache", "lines.csv")).set_index("cell_line_id").reindex(lid)
for g in panel:
    if g not in EXPR.columns:
        EXPR[g] = _pl["expr_" + g].astype(bool).to_numpy()
tp = pd.read_csv(os.path.join(DATA, "gene_panel", "results", "baseline_by_cell_line.csv")).set_index(
    "cell_line_id")["tp53_group"]


def glm(y, X, off, n_iter=40):
    b = np.zeros(X.shape[1])
    b[0] = np.log(max(y.sum(), 0.5) / np.exp(off).sum())
    for _ in range(n_iter):
        eta = X @ b + off
        mu = np.exp(np.clip(eta, -30, 30))
        z = eta - off + (y - mu) / mu
        try:
            bn = np.linalg.solve((X.T * mu) @ X, (X.T * mu) @ z)
        except np.linalg.LinAlgError:
            return np.nan, np.nan
        if np.max(np.abs(bn - b)) < 1e-8:
            b = bn
            break
        b = bn
    mu = np.exp(np.clip(X @ b + off, -30, 30))
    phi = max(1.0, float(((y - mu) ** 2 / mu).sum() / max(1, len(y) - X.shape[1])))
    try:
        cov = phi * np.linalg.inv((X.T * mu) @ X)
    except np.linalg.LinAlgError:
        return np.nan, np.nan
    return float(b[1]), float(np.sqrt(cov[1, 1]))


def dl(est, se):
    est, se = np.asarray(est, float), np.asarray(se, float)
    ok = np.isfinite(est) & np.isfinite(se) & (se > 0)
    est, se = est[ok], se[ok]
    k = len(est)
    if k < 3:
        return k, np.nan, np.nan, np.nan
    w = 1 / se ** 2
    fe = (w * est).sum() / w.sum()
    Q = (w * (est - fe) ** 2).sum()
    c = w.sum() - (w ** 2).sum() / w.sum()
    tau2 = max(0.0, (Q - (k - 1)) / c)
    ws = 1 / (se ** 2 + tau2)
    m = (ws * est).sum() / ws.sum()
    s = np.sqrt(1 / ws.sum())
    return k, m, s, float(2 * stats.norm.sf(abs(m / s)))


wellsets = {"ida both": ["smp_2010", "smp_2778"], "DMSO 6+14": ["smp_2069", "smp_2070", "smp_2837", "smp_2838"]}
fits, info = [], []
for ws, wells in wellsets.items():
    sub = cells[cells["sample"].isin(wells)]
    det_rate = (sub[panel] > 0).mean()
    r72 = det_rate["TRIM72"]
    preds = ["TRIM72"] + [g for g in panel if g not in P53 + ["TP53", "ATF3", "PMAIP1", "TRIM72"]
                          and r72 / 3 <= det_rate[g] <= r72 * 3]
    print(ws, "TRIM72 detection", round(r72, 4), "placebo predictors:", len(preds) - 1, preds[1:])
    for line, c in sub.groupby("cell_line_id"):
        if line not in EXPR.index or not EXPR.loc[line, "TRIM72"] or len(c) < 50:
            continue
        T = c["total_counts"].to_numpy(float)
        lT = np.log(T)
        lc = lT - lT.mean()
        S = np.log((c["S_PHASE"].to_numpy() + 0.5) / T)
        G = np.log((c["G2M_PHASE"].to_numpy() + 0.5) / T)
        well = pd.factorize(c["sample"])[0]
        extra = [(well == w_).astype(float) for w_ in np.unique(well)[1:]]
        ys = {"P53_SUM": c[P53].sum(axis=1).to_numpy(float)}
        for o in OUTCOMES[1:]:
            ys[o] = c[o].to_numpy(float)
        # information content of TRIM72 detection (NB moment estimator given depth)
        y72 = c["TRIM72"].to_numpy(float)
        mu = np.zeros(len(c))
        for w_ in np.unique(well):
            m = well == w_
            mu[m] = T[m] * y72[m].sum() / T[m].sum()
        alpha = float(((y72 - mu) ** 2 - y72).sum() / (mu ** 2).sum()) if (mu ** 2).sum() > 0 else np.nan
        a_ = max(alpha, 1e-6)
        mbar = float(mu.mean())
        # gamma(shape 1/a, mean mbar): E[lam | y=0] = mbar / (1 + a mbar); P0 = (1 + a mbar)^(-1/a)
        p0 = (1 + a_ * mbar) ** (-1 / a_)
        e0 = mbar / (1 + a_ * mbar)
        e1 = (mbar - p0 * e0) / (1 - p0)
        info.append(dict(wellset=ws, cell_line_id=line, tp53=tp.get(line), n=len(c), n_det=int((y72 > 0).sum()),
                         mean_TRIM72_per_cell=mbar, alpha_NB=alpha, implied_true_ratio_det_vs_not=e1 / e0))
        for p in preds:
            if not EXPR.loc[line, p]:
                continue
            det = c[p].to_numpy() > 0
            k = int(det.sum())
            if k < 5 or len(c) - k < 5:
                continue
            X = np.column_stack([np.ones(len(c)), det.astype(float), lc, lc ** 2, S - S.mean(), G - G.mean()] + extra)
            for o, y in ys.items():
                if o != "P53_SUM" and not EXPR.loc[line, o]:
                    continue
                if y.sum() < 20:
                    continue
                b, s = glm(y, X, lT)
                fits.append(dict(wellset=ws, cell_line_id=line, tp53=tp.get(line), predictor=p,
                                 placebo_class="TRIM72" if p == "TRIM72" else ("stress program" if p in STRESS
                                                                              else "other"),
                                 outcome=o, n=len(c), n_det=k, logRR=b, se=s))
F = pd.DataFrame(fits)
F.to_csv(os.path.join(OUT, "v5_per_line_fits.csv.gz"), index=False)
I = pd.DataFrame(info)
I.to_csv(os.path.join(OUT, "v5_trim72_detection_information.csv"), index=False)

rows = []
for (ws, grp, p, o), h in F.groupby(["wellset", "tp53", "predictor", "outcome"]):
    k, m, s, pv = dl(h.logRR, h.se)
    rows.append(dict(wellset=ws, tp53=grp, predictor=p, placebo_class=h.placebo_class.iloc[0], outcome=o, n_lines=k,
                     RR=np.exp(m), ci_lo=np.exp(m - 1.96 * s), ci_hi=np.exp(m + 1.96 * s), p=pv))
Mt = pd.DataFrame(rows)
summ = []
for (ws, grp, o), h in Mt.groupby(["wellset", "tp53", "outcome"]):
    t = h[h.predictor == "TRIM72"]
    if t.empty:
        continue
    t = t.iloc[0]
    for cls, pl in (("all placebos", h[h.predictor != "TRIM72"]), ("non-stress placebos", h[h.placebo_class == "other"])):
        pl = pl[pl.n_lines >= 8]
        summ.append(dict(wellset=ws, tp53=grp, outcome=o, placebos=cls, n_placebos=len(pl), RR_TRIM72=t.RR,
                         p_TRIM72=t.p, n_lines_TRIM72=t.n_lines, placebo_median_RR=pl.RR.median(),
                         placebo_min_RR=pl.RR.min(), placebo_max_RR=pl.RR.max(),
                         placebo_frac_RR_gt1=(pl.RR > 1).mean(), placebo_n_p_lt_05_up=int(((pl.p < 0.05) & (pl.RR > 1)).sum()),
                         pct_TRIM72_among_placebos=100 * (pl.RR < t.RR).mean(),
                         top_placebos=", ".join(f"{a} {b:.2f}" for a, b in pl.sort_values("RR", ascending=False)
                                                .head(4)[["predictor", "RR"]].values)))
S_ = pd.DataFrame(summ)
Mt.to_csv(os.path.join(OUT, "v5_meta_by_predictor.csv"), index=False)
S_.to_csv(os.path.join(OUT, "v5_placebo_summary.csv"), index=False)

# elasticity bound: P53_SUM CI per doubling of the implied true TRIM72 rate (median over lines)
v2m = pd.read_csv(os.path.join(OUT, "v2_meta.csv"))
eb = []
for (ws, grp), h in I[I.n_det >= 5].groupby(["wellset", "tp53"]):
    ratio = h.implied_true_ratio_det_vs_not.median()
    r = Mt[(Mt.wellset == ws) & (Mt.tp53 == grp) & (Mt.predictor == "TRIM72") & (Mt.outcome == "P53_SUM")]
    if r.empty:
        continue
    r = r.iloc[0]
    eb.append(dict(wellset=ws, tp53=grp, n_lines=len(h), median_alpha=h.alpha_NB.median(),
                   frac_alpha_gt0=(h.alpha_NB > 0).mean(), median_mean_per_cell=h.mean_TRIM72_per_cell.median(),
                   median_implied_true_ratio=ratio, RR_P53_SUM=r.RR, ci_lo=r.ci_lo, ci_hi=r.ci_hi,
                   per_doubling_lo=np.exp(np.log(r.ci_lo) / np.log2(ratio)) if ratio > 1.01 else np.nan,
                   per_doubling_hi=np.exp(np.log(r.ci_hi) / np.log2(ratio)) if ratio > 1.01 else np.nan))
pd.DataFrame(eb).to_csv(os.path.join(OUT, "v5_elasticity_bound.csv"), index=False)

pd.set_option("display.width", 260)
pd.set_option("display.max_columns", 30)
pd.set_option("display.max_colwidth", 60)
print(S_.round(3).to_string())
print(pd.DataFrame(eb).round(3).to_string())
print(I.groupby(["wellset", "tp53"])[["alpha_NB", "implied_true_ratio_det_vs_not", "mean_TRIM72_per_cell"]]
      .describe().round(3).T.to_string())
