#!/usr/bin/env python3
"""Adversarial check of F7/F8 (single cells: TRIM72-detected vs not, p53-target counts).

Own code, own data read (gene_panel/cells/*.parquet, filtered to the idarubicin 5 uM wells and the plate-6/14 DMSO
wells). Per line and well set:
  - is TRIM72 detection more than Poisson sampling given depth? (expected detected cells and Pearson dispersion under
    a depth-only Poisson model with one rate per line x well)
  - depth / genes / S / G2M of detected vs not
  - rate ratio of outcome counts per UMI, detected vs not, five ways: crude; Mantel-Haenszel in 20 depth bins (x well);
    MH in depth-quintile x S-tertile x G2M-tertile (x well) strata; Poisson GLM (own IRLS, quasi-Poisson SE) with
    offset log UMI + log UMI + (log UMI)^2 + S + G2M fractions (+ well); the same GLM plus log(genes/UMI)
  - permutation null of the depth-bin MH estimate: detection shuffled within depth bins (x well)
  - outcomes: P53_SUM (summed counts of 21 targets, as the analysis), P53_EQ (equal-weight mean of the 21 per-gene
    GLM log RRs), MDM2, CDKN1A, ATF3, PMAIP1, AMBIENT (summed counts of panel genes the line does NOT express: pure
    ambient / cross-line signal), all other panel genes as controls.
  - random-effects (DerSimonian-Laird) meta over lines by TP53 group; sign counts.

    python3 verify/v2_single_cell.py   -> verify/out/v2_*.csv
"""
import glob
import os
import numpy as np
import pandas as pd
import pyarrow.parquet as pq
from scipy import stats

DATA = "/home/user/tahoe_data"
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
os.makedirs(OUT, exist_ok=True)
IDA = {"plate6": "smp_2010", "plate14": "smp_2778"}
DMSO = {"plate6": ["smp_2069", "smp_2070"], "plate14": ["smp_2837", "smp_2838"]}
P53 = ["CDKN1A", "MDM2", "FDXR", "ZMAT3", "SESN1", "BBC3", "BAX", "TP53I3", "RRM2B", "AEN", "DDB2", "XPC", "PHLDA3",
       "SPATA18", "TRIAP1", "RPS27L", "ACER2", "TP53INP1", "PLK3", "POLH", "EDA2R"]
rng = np.random.default_rng(11)

# ------------------------------------------------------------------ read cells
want = [IDA["plate6"], IDA["plate14"]] + DMSO["plate6"] + DMSO["plate14"]
cache = os.path.join(OUT, "v2_cells.parquet")
if os.path.exists(cache):
    cells = pd.read_parquet(cache)
else:
    parts = []
    for f in sorted(glob.glob(os.path.join(DATA, "gene_panel", "cells", "*.parquet"))):
        pf = pq.ParquetFile(f)
        md = pf.metadata
        names = pf.schema_arrow.names
        ip, is_ = names.index("plate"), names.index("sample")
        hit = False
        for r in range(md.num_row_groups):
            st_p = md.row_group(r).column(ip).statistics
            st_s = md.row_group(r).column(is_).statistics
            if st_p is None or st_s is None or not st_p.has_min_max:
                hit = True
                break
            if st_p.min == st_p.max and st_p.min not in ("plate6", "plate14"):
                continue
            if any(st_s.min <= s <= st_s.max for s in want):
                hit = True
                break
        if not hit:
            continue
        t = pq.read_table(f, filters=[("sample", "in", want)])
        if t.num_rows:
            parts.append(t.to_pandas())
    cells = pd.concat(parts, ignore_index=True)
    cells.to_parquet(cache, index=False)
sm = pd.read_csv(os.path.join(DATA, "gene_panel", "sample_map.csv"), dtype={"sample": str}).set_index("sample")
cnt = cells["sample"].value_counts()
print("cells per well (mine vs sample_map):", {k: (int(v), int(sm.loc[k, "n_cells"])) for k, v in cnt.items()})

panel = [c for c in cells.columns if c not in ("barcode", "sample", "plate", "drug", "cell_line_id", "n_genes",
                                                "total_counts", "PROTEASOME", "S_PHASE", "G2M_PHASE")]
lines = pd.read_csv(os.path.join(DATA, "atlas", "effects", "lines.csv"))
lid = lines.cell_line_id.astype(str).tolist()
name = lines.set_index("cell_line_id").cell_name
ga = pd.read_csv(os.path.join(DATA, "atlas", "effects", "genes.csv"))
ga = ga[ga.kind == "gene"].drop_duplicates("symbol").set_index("symbol")
expr = np.load(os.path.join(DATA, "atlas", "effects", "expr_mask.npy"), mmap_mode="r")
EXPR = pd.DataFrame({g: np.asarray(expr[:, int(ga.loc[g, "col"])]).astype(bool) for g in panel if g in ga.index},
                    index=lid)
# 5 panel genes are not in the atlas gene list (PYCARD, CASP1, CASP5, SRXN1, HSPA6): the panel's expressed flag
_pl = pd.read_csv(os.path.join(os.path.dirname(HERE), "cache", "lines.csv")).set_index("cell_line_id").reindex(lid)
for g in panel:
    if g not in EXPR.columns:
        EXPR[g] = _pl["expr_" + g].astype(bool).to_numpy()
tp = pd.read_csv(os.path.join(DATA, "gene_panel", "results", "baseline_by_cell_line.csv")).set_index(
    "cell_line_id")["tp53_group"]

# share of the summed P53 counts per member (does one gene dominate the summed score?)
ida = cells[cells["sample"].isin(IDA.values())]
share = (ida[P53].sum() / ida[P53].sum().sum()).sort_values(ascending=False)
share.rename("share_of_summed_P53_counts").to_csv(os.path.join(OUT, "v2_p53sum_member_share.csv"))


def glm(y, X, off, n_iter=50):
    b = np.zeros(X.shape[1])
    b[0] = np.log(max(y.sum(), 0.5) / np.exp(off).sum())
    for _ in range(n_iter):
        eta = X @ b + off
        mu = np.exp(np.clip(eta, -30, 30))
        z = eta - off + (y - mu) / mu
        W = mu
        try:
            bn = np.linalg.solve((X.T * W) @ X, (X.T * W) @ z)
        except np.linalg.LinAlgError:
            return np.nan, np.nan
        if np.max(np.abs(bn - b)) < 1e-9:
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


def mh(y, T, det, strata):
    sc, ns = np.unique(strata, return_inverse=True)[1], len(np.unique(strata))
    a = np.bincount(sc[det], y[det], ns)
    t1 = np.bincount(sc[det], T[det], ns)
    b = np.bincount(sc[~det], y[~det], ns)
    t0 = np.bincount(sc[~det], T[~det], ns)
    ok = (t1 > 0) & (t0 > 0)
    num = (a[ok] * t0[ok] / (t1[ok] + t0[ok])).sum()
    den = (b[ok] * t1[ok] / (t1[ok] + t0[ok])).sum()
    return np.log(num / den) if num > 0 and den > 0 else np.nan


def dl(est, se):
    est, se = np.asarray(est, float), np.asarray(se, float)
    ok = np.isfinite(est) & np.isfinite(se) & (se > 0)
    est, se = est[ok], se[ok]
    k = len(est)
    if k < 2:
        return k, np.nan, np.nan, np.nan, np.nan
    w = 1 / se ** 2
    fe = (w * est).sum() / w.sum()
    Q = (w * (est - fe) ** 2).sum()
    c = w.sum() - (w ** 2).sum() / w.sum()
    tau2 = max(0.0, (Q - (k - 1)) / c)
    ws = 1 / (se ** 2 + tau2)
    m = (ws * est).sum() / ws.sum()
    s = np.sqrt(1 / ws.sum())
    return k, m, s, float(2 * stats.norm.sf(abs(m / s))), float(max(0, (Q - (k - 1)) / Q) if Q > 0 else 0)


wellsets = {"ida plate6": [IDA["plate6"]], "ida plate14": [IDA["plate14"]], "ida both": list(IDA.values()),
            "DMSO 6+14": DMSO["plate6"] + DMSO["plate14"]}
desc, fits = [], []
for ws, wells in wellsets.items():
    sub = cells[cells["sample"].isin(wells)]
    for line, c in sub.groupby("cell_line_id"):
        T = c["total_counts"].to_numpy(float)
        y72 = c["TRIM72"].to_numpy(float)
        det = y72 > 0
        n, k = len(c), int(det.sum())
        well = pd.factorize(c["sample"])[0]
        # depth-only Poisson model for TRIM72, one rate per well
        mu72 = np.zeros(n)
        for w_ in np.unique(well):
            m = well == w_
            mu72[m] = T[m] * y72[m].sum() / T[m].sum()
        exp_det = float((1 - np.exp(-mu72)).sum())
        disp = float(((y72 - mu72) ** 2 / np.where(mu72 > 0, mu72, np.nan)).sum() / max(1, n - len(np.unique(well))))
        # detection beyond depth: likelihood-ratio-free check, the share of detected cells with >= 2 UMI vs Poisson
        exp_ge2 = float((1 - np.exp(-mu72) - mu72 * np.exp(-mu72)).sum())
        S = np.log((c["S_PHASE"].to_numpy() + 0.5) / T)
        G = np.log((c["G2M_PHASE"].to_numpy() + 0.5) / T)
        cx = np.log(c["n_genes"].to_numpy(float) / T)
        amb_genes = [g for g in panel if g in EXPR.columns and not EXPR.loc[line, g] and g != "TRIM72"]
        amb = c[amb_genes].sum(axis=1).to_numpy(float) if amb_genes else np.zeros(n)
        desc.append(dict(wellset=ws, cell_line_id=line, cell_line=name.get(line), tp53=tp.get(line),
                         TRIM72_expressed=bool(EXPR.loc[line, "TRIM72"]), n_cells=n, n_det=k, pct_det=100 * k / n,
                         expected_det_poisson=exp_det, obs_over_exp_det=k / exp_det if exp_det > 0 else np.nan,
                         n_ge2=int((y72 >= 2).sum()), expected_ge2_poisson=exp_ge2, dispersion_TRIM72=disp,
                         TRIM72_per_10k_UMI=1e4 * y72.sum() / T.sum(),
                         umi_ratio_det_vs_not=float(np.median(T[det]) / np.median(T[~det])) if 0 < k < n else np.nan,
                         genes_per_umi_diff=float(cx[det].mean() - cx[~det].mean()) if 0 < k < n else np.nan,
                         S_diff=float(S[det].mean() - S[~det].mean()) if 0 < k < n else np.nan,
                         G2M_diff=float(G[det].mean() - G[~det].mean()) if 0 < k < n else np.nan,
                         n_ambient_genes=len(amb_genes)))
        if not EXPR.loc[line, "TRIM72"] or n < 50 or k < 5 or n - k < 5:
            continue
        lT = np.log(T)
        lc = lT - lT.mean()
        base_cols = [np.ones(n), det.astype(float), lc, lc ** 2, S - S.mean(), G - G.mean()]
        for w_ in np.unique(well)[1:]:
            base_cols.append((well == w_).astype(float))
        X1 = np.column_stack(base_cols)
        X2 = np.column_stack(base_cols + [cx - cx.mean()])
        qd = np.asarray(pd.qcut(pd.Series(lT).rank(method="first"), 20, labels=False))
        st_depth = qd * 10 + well
        q5 = np.asarray(pd.qcut(pd.Series(lT).rank(method="first"), 5, labels=False))
        s3 = np.asarray(pd.qcut(pd.Series(S).rank(method="first"), 3, labels=False))
        g3 = np.asarray(pd.qcut(pd.Series(G).rank(method="first"), 3, labels=False))
        st_cc = ((q5 * 3 + s3) * 3 + g3) * 10 + well
        perms = []
        if ws != "DMSO 6+14":
            for _ in range(200):
                dp = det.copy()
                for s_ in np.unique(st_depth):
                    m = np.where(st_depth == s_)[0]
                    dp[m] = det[m][rng.permutation(len(m))]
                perms.append(dp)
        outs = {"P53_SUM": c[[g for g in P53]].sum(axis=1).to_numpy(float), "AMBIENT": amb}
        for g in panel:
            if g != "TRIM72":
                outs[g] = c[g].to_numpy(float)
        for oname, y in outs.items():
            if oname not in ("P53_SUM", "AMBIENT") and not EXPR.loc[line, oname]:
                continue
            if y.sum() < 20:
                continue
            b1, s1 = glm(y, X1, lT)
            b2, s2 = glm(y, X2, lT)
            crude = np.log(((y[det].sum() + 0.5) / T[det].sum()) / ((y[~det].sum() + 0.5) / T[~det].sum()))
            r = dict(wellset=ws, cell_line_id=line, tp53=tp.get(line), outcome=oname, n=n, n_det=k,
                     counts=int(y.sum()), crude=crude, mh_depth20=mh(y, T, det, st_depth),
                     mh_depth_cc=mh(y, T, det, st_cc), glm=b1, glm_se=s1, glm_cx=b2, glm_cx_se=s2)
            if oname in ("P53_SUM", "MDM2", "CDKN1A", "ATF3", "PMAIP1", "AMBIENT") and ws != "DMSO 6+14":
                null = np.array([mh(y, T, dp, st_depth) for dp in perms])
                null = null[np.isfinite(null)]
                r["perm_null_sd"] = float(null.std())
                r["perm_p"] = float((1 + (np.abs(null) >= abs(r["mh_depth20"])).sum()) / (len(null) + 1))
            fits.append(r)
D = pd.DataFrame(desc)
F = pd.DataFrame(fits)
D.to_csv(os.path.join(OUT, "v2_line_description.csv"), index=False)
F.to_csv(os.path.join(OUT, "v2_per_line_fits.csv.gz"), index=False)

# P53_EQ: per line, equal-weight mean of the members' GLM log RR (SE from the members' SEs, treated as independent:
# optimistic)
eq = []
for (ws, line), g in F[F.outcome.isin(P53)].groupby(["wellset", "cell_line_id"]):
    if len(g) >= 5:
        eq.append(dict(wellset=ws, cell_line_id=line, tp53=g.tp53.iloc[0], outcome="P53_EQ", n=g.n.iloc[0],
                       n_det=g.n_det.iloc[0], glm=g.glm.mean(), glm_se=np.sqrt((g.glm_se ** 2).sum()) / len(g),
                       crude=g.crude.mean(), mh_depth20=g.mh_depth20.mean(), mh_depth_cc=g.mh_depth_cc.mean(),
                       glm_cx=g.glm_cx.mean(), glm_cx_se=np.sqrt((g.glm_cx_se ** 2).sum()) / len(g)))
F2 = pd.concat([F, pd.DataFrame(eq)], ignore_index=True)

rows = []
ctl_names = [g for g in panel if g not in P53 + ["TRIM72", "TP53", "ATF3", "PMAIP1", "GADD45A", "SESN2", "TNFRSF10B",
                                                 "CCNG1", "BTG2", "TIGAR"]]
for (ws, grp), g in F2.groupby(["wellset", "tp53"]):
    ctl = {}
    for o, h in g[g.outcome.isin(ctl_names)].groupby("outcome"):
        ctl[o] = dl(h.glm, h.glm_se)[1]
    ctlv = np.array([v for v in ctl.values() if np.isfinite(v)])
    for o, h in g.groupby("outcome"):
        if o not in ("P53_SUM", "P53_EQ", "MDM2", "CDKN1A", "ATF3", "PMAIP1", "AMBIENT", "TP53", "BAX", "TFRC",
                     "HSPA6", "HSPA1A"):
            continue
        k, m, s, p, I2 = dl(h.glm, h.glm_se)
        k2, m2, s2, p2, _ = dl(h.glm_cx, h.glm_cx_se)
        rows.append(dict(wellset=ws, tp53=grp, outcome=o, n_lines=k, RR_glm=np.exp(m),
                         ci_lo=np.exp(m - 1.96 * s), ci_hi=np.exp(m + 1.96 * s), p_glm=p, I2=I2,
                         RR_glm_plus_complexity=np.exp(m2), p_glm_plus_complexity=p2,
                         median_line_RR_crude=np.exp(np.nanmedian(h.crude)),
                         median_line_RR_mh_depth20=np.exp(np.nanmedian(h.mh_depth20)),
                         median_line_RR_mh_depth_cellcycle=np.exp(np.nanmedian(h.mh_depth_cc)),
                         n_lines_mh_depth20_gt1=int((h.mh_depth20 > 0).sum()),
                         sign_p_mh_depth20=float(stats.binomtest(int((h.mh_depth20 > 0).sum()),
                                                                 int(h.mh_depth20.notna().sum())).pvalue)
                         if h.mh_depth20.notna().sum() else np.nan,
                         n_lines_perm_p_lt_05=int((h.get("perm_p", pd.Series(dtype=float)) < 0.05).sum()),
                         pct_among_controls=float(100 * (ctlv < m).mean()) if len(ctlv) else np.nan,
                         controls_median_RR=float(np.exp(np.median(ctlv))) if len(ctlv) else np.nan,
                         controls_frac_RR_gt1=float((ctlv > 0).mean()) if len(ctlv) else np.nan,
                         n_controls=len(ctlv)))
Mt = pd.DataFrame(rows)
Mt.to_csv(os.path.join(OUT, "v2_meta.csv"), index=False)

# WT minus altered and plate6 vs plate14 differences of the meta estimates (P53_SUM, P53_EQ, MDM2)
dif = []
for o in ("P53_SUM", "P53_EQ", "MDM2", "CDKN1A", "ATF3", "PMAIP1"):
    for ws in wellsets:
        a = Mt[(Mt.wellset == ws) & (Mt.outcome == o)].set_index("tp53")
        if {"WT", "altered"} <= set(a.index):
            la, lb = np.log(a.at["WT", "RR_glm"]), np.log(a.at["altered", "RR_glm"])
            sa = (np.log(a.at["WT", "ci_hi"]) - np.log(a.at["WT", "ci_lo"])) / 3.92
            sb = (np.log(a.at["altered", "ci_hi"]) - np.log(a.at["altered", "ci_lo"])) / 3.92
            d = la - lb
            dif.append(dict(contrast="WT - altered", wellset=ws, outcome=o, log_diff=d,
                            p=float(2 * stats.norm.sf(abs(d / np.hypot(sa, sb))))))
    for grp in ("WT", "altered"):
        a = Mt[(Mt.tp53 == grp) & (Mt.outcome == o)].set_index("wellset")
        if {"ida plate6", "ida plate14"} <= set(a.index):
            la, lb = np.log(a.at["ida plate14", "RR_glm"]), np.log(a.at["ida plate6", "RR_glm"])
            sa = (np.log(a.at["ida plate14", "ci_hi"]) - np.log(a.at["ida plate14", "ci_lo"])) / 3.92
            sb = (np.log(a.at["ida plate6", "ci_hi"]) - np.log(a.at["ida plate6", "ci_lo"])) / 3.92
            d = la - lb
            dif.append(dict(contrast="plate14 - plate6 (" + grp + ")", wellset="ida", outcome=o, log_diff=d,
                            p=float(2 * stats.norm.sf(abs(d / np.hypot(sa, sb))))))
pd.DataFrame(dif).to_csv(os.path.join(OUT, "v2_differences.csv"), index=False)

pd.set_option("display.width", 250)
pd.set_option("display.max_columns", 40)
print(share.round(3).head(8).to_string())
Dx = D[D.TRIM72_expressed]
print(Dx.groupby("wellset")[["pct_det", "obs_over_exp_det", "dispersion_TRIM72", "umi_ratio_det_vs_not",
                             "genes_per_umi_diff", "S_diff", "G2M_diff"]].median().round(3).to_string())
print(D[D.cell_line == "NCI-H661"][["wellset", "n_cells", "n_det", "pct_det", "TRIM72_per_10k_UMI"]].to_string())
print(D.groupby("wellset").apply(lambda g: pd.Series(dict(
    median_pct_det_expressing=g[g.TRIM72_expressed].pct_det.median(),
    median_TRIM72_per10k=g[g.TRIM72_expressed].TRIM72_per_10k_UMI.median()))).round(3).to_string())
print(Mt.round(3).to_string())
print(pd.DataFrame(dif).round(4).to_string())
