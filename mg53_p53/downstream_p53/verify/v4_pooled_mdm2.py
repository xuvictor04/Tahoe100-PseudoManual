#!/usr/bin/env python3
"""Adversarial check of F2/F3: pooled over the 13 TRIM72 raisers, TRIM72 induction vs MDM2 / P53_SCORE / TP53 in
TP53-WT lines. Reads the per (well, line) method-v3 r2 of the analysis's cache (cache/effects.npz; its idarubicin
values were re-derived from raw counts in v1, Pearson 0.9999) and the atlas DD_beta / DD_A.

Checks: (1) recompute the pooled mean rho with a joint line permutation; (2) the same statistic for TRIM72 vs EVERY
other panel gene: is MDM2 unusual?; (3) leave-one-drug-out (all doses of a drug together); (4) one dose per drug;
(5) BH over all 288 pooled tests the analysis ran (its own p values).

    python3 verify/v4_pooled_mdm2.py  -> verify/out/v4_*.csv
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
rng = np.random.default_rng(3)
P53 = ["CDKN1A", "MDM2", "FDXR", "ZMAT3", "SESN1", "BBC3", "BAX", "TP53I3", "RRM2B", "AEN", "DDB2", "XPC", "PHLDA3",
       "SPATA18", "TRIAP1", "RPS27L", "ACER2", "TP53INP1", "PLK3", "POLH", "EDA2R"]

z = np.load(os.path.join(ROOT, "cache", "effects.npz"))
genes = [str(g) for g in z["genes"]]
samples = [str(s) for s in z["samples"]]
lines = [str(l) for l in z["lines"]]
R2 = z["R2"].astype(float)
gi = {g: i for i, g in enumerate(genes)}
si = {s: i for i, s in enumerate(samples)}
W = pd.read_csv(os.path.join(ROOT, "cache", "wells.csv"), dtype={"sample": str}).set_index("sample")
L = pd.read_csv(os.path.join(ROOT, "cache", "lines.csv")).set_index("cell_line_id").reindex(lines)
wt = (L.tp53_group == "WT").to_numpy()
alt = (L.tp53_group == "altered").to_numpy()
sel = pd.read_csv(os.path.join(ROOT, "tables", "a_selected_drugdoses.csv"))
rais = sel[sel.role.str.startswith("TRIM72 raiser")][["drug", "conc"]].values.tolist()
dd = pd.read_csv(os.path.join(DATA, "atlas", "effects", "drugdose.csv"))
alines = pd.read_csv(os.path.join(DATA, "atlas", "effects", "lines.csv")).cell_line_id.astype(str).tolist()
DDb = np.load(os.path.join(DATA, "atlas", "effects", "DD_beta.npy"), mmap_mode="r")
DDA = np.load(os.path.join(DATA, "atlas", "effects", "DD_A.npy"), mmap_mode="r")


def per_line(drug, conc):
    w = W[(W.drug == drug) & np.isclose(W.conc.astype(float), conc) & ~W.is_dmso & W.used]
    ii = [si[s] for s in w.index]
    with np.errstate(all="ignore"):
        import warnings
        warnings.simplefilter("ignore")
        M = np.nanmean(R2[:, ii, :], axis=1)              # genes x lines
        p53 = np.nanmean(M[[gi[g] for g in P53]], axis=0)
    r = int(dd.index[(dd.drug == drug) & np.isclose(dd.conc, conc)][0])
    b = pd.Series(np.asarray(DDb[r]), index=alines).reindex(lines).to_numpy()
    A = pd.Series(np.asarray(DDA[r]), index=alines).reindex(lines).to_numpy()
    return M, p53, np.column_stack([b, A])


def resid_ranks(x, y, Z, m):
    ok = m & np.isfinite(x) & np.isfinite(y)
    if Z is not None:
        ok &= np.isfinite(Z).all(1)
    rx, ry = np.full(len(x), np.nan), np.full(len(x), np.nan)
    if ok.sum() < 8:
        return rx, ry
    a, b = stats.rankdata(x[ok]), stats.rankdata(y[ok])
    if Z is not None:
        X = np.column_stack([np.ones(ok.sum())] + [stats.rankdata(Z[ok, j]) for j in range(Z.shape[1])])
        a = a - X @ np.linalg.lstsq(X, a, rcond=None)[0]
        b = b - X @ np.linalg.lstsq(X, b, rcond=None)[0]
    rx[ok], ry[ok] = a, b
    return rx, ry


def fz(rx, ry, perms):
    Xp = rx[perms]
    m = np.isfinite(Xp) & np.isfinite(ry)[None, :]
    n = m.sum(1)
    with np.errstate(all="ignore"):
        X0, Y0 = np.where(m, Xp, 0), np.where(m, ry[None, :], 0)
        mx, my = X0.sum(1) / n, Y0.sum(1) / n
        dx, dy = np.where(m, Xp - mx[:, None], 0), np.where(m, ry[None, :] - my[:, None], 0)
        r = (dx * dy).sum(1) / np.sqrt((dx * dx).sum(1) * (dy * dy).sum(1))
    return np.arctanh(np.clip(r, -0.999999, 0.999999))


tabs = {(d, c): per_line(d, c) for d, c in rais}
outs = ["P53_SCORE"] + [g for g in genes if g != "TRIM72"]
rows = []
for gname, gm in (("WT", wt), ("altered", alt)):
    idx = np.where(gm)[0]
    perms = np.stack([np.arange(len(idx))] + [rng.permutation(len(idx)) for _ in range(2000)])
    for adj in ("none", "beta+A"):
        for o in outs:
            Zs, per = [], []
            for (d, c), (M, p53, Z) in tabs.items():
                x = M[gi["TRIM72"]]
                y = p53 if o == "P53_SCORE" else M[gi[o]]
                rx, ry = resid_ranks(x, y, Z if adj == "beta+A" else None, gm)
                if np.isfinite(rx).sum() < 8:
                    continue
                zz = fz(rx[idx], ry[idx], perms)
                Zs.append(zz)
                per.append((d, c, float(np.tanh(zz[0]))))
            if len(Zs) < 5:
                continue
            Zs = np.stack(Zs)
            with np.errstate(all="ignore"):
                mz = np.nanmean(Zs, axis=0)
            obs, null = mz[0], mz[1:]
            # leave-one-drug-out
            drugs = sorted(set(d for d, c, _ in per))
            lodo = []
            for dr in drugs:
                keep = [i for i, (d, c, _) in enumerate(per) if d != dr]
                lodo.append(float(np.tanh(np.nanmean(Zs[keep, 0]))))
            # one dose per drug: the strongest TRIM72 dose (first listed per drug in a_selected, sorted by z)
            seen, one = set(), []
            for i, (d, c, _) in enumerate(per):
                if d not in seen:
                    seen.add(d)
                    one.append(i)
            m1 = np.nanmean(Zs[one], axis=0)
            rows.append(dict(group=gname, adjust=adj, outcome=o, is_p53=o in P53 + ["P53_SCORE", "TP53"],
                             n_dd=len(per), mean_rho=float(np.tanh(obs)),
                             p_perm=float((1 + (np.abs(null) >= abs(obs) - 1e-12).sum()) / (len(null) + 1)),
                             n_neg=int((Zs[:, 0] < 0).sum()), lodo_min=min(lodo), lodo_max=max(lodo),
                             lodo_drug_at_max=drugs[int(np.argmax(lodo))],
                             one_dose_per_drug_n=len(one), one_dose_per_drug_rho=float(np.tanh(m1[0])),
                             one_dose_per_drug_p=float((1 + (np.abs(m1[1:]) >= abs(m1[0]) - 1e-12).sum())
                                                       / (len(m1) - 1 + 1))))
            if o in ("MDM2", "P53_SCORE", "TP53"):
                pd.DataFrame(per, columns=["drug", "conc", "rho"]).assign(group=gname, adjust=adj, outcome=o).to_csv(
                    os.path.join(OUT, f"v4_per_drugdose_{o}_{gname}_{adj.replace('+', '')}.csv"), index=False)
R = pd.DataFrame(rows)
# percentile of each outcome among the non-p53 panel genes (same group / adjustment)
notbg = set(P53 + ["P53_SCORE", "TP53", "PMAIP1", "GADD45A", "SESN2", "TNFRSF10B", "CCNG1", "BTG2", "TIGAR", "ATF3"])
R["pct_among_background"] = np.nan
R["bg_n_p_lt_05"] = np.nan
for (g, a), h in R.groupby(["group", "adjust"]):
    bg = h[~h.outcome.isin(notbg)]
    R.loc[h.index, "pct_among_background"] = [100 * (bg.mean_rho < v).mean() for v in h.mean_rho]
    R.loc[h.index, "bg_n_p_lt_05"] = int((bg.p_perm < 0.05).sum())
    R.loc[h.index, "bg_n"] = len(bg)
    R.loc[h.index, "q_bh_all_genes"] = stats.false_discovery_control(h.p_perm.to_numpy())
R.to_csv(os.path.join(OUT, "v4_pooled_all_genes.csv"), index=False)

# BH over all 288 pooled tests of the analysis
pl = pd.read_csv(os.path.join(ROOT, "tables", "a_pooled_over_drugdoses.csv"))
pl["q_bh_all_288"] = stats.false_discovery_control(pl.p_line_permutation.to_numpy())
pl.to_csv(os.path.join(OUT, "v4_analysis_pooled_q_all288.csv"), index=False)

pd.set_option("display.width", 250)
pd.set_option("display.max_columns", 30)
k = R[R.outcome.isin(["P53_SCORE", "MDM2", "TP53", "CDKN1A"])]
print(k.round(3).to_string())
for (g, a), h in R.groupby(["group", "adjust"]):
    bg = h[~h.outcome.isin(notbg)]
    print(g, a, "background genes:", len(bg), "median", round(bg.mean_rho.median(), 3), "p5/p95",
          np.round(bg.mean_rho.quantile([.05, .95]).to_numpy(), 3), "n p<0.05:", int((bg.p_perm < 0.05).sum()),
          "most negative:", bg.sort_values("mean_rho").head(5)[["outcome", "mean_rho"]].round(3).values.tolist())
print(pl[(pl.set == "TRIM72 raisers") & (pl.predictor == "TRIM72_r2") & pl.outcome.isin(["MDM2", "TP53"]) &
         (pl.tp53_group == "TP53-WT")][["adjustment", "outcome", "mean_rho", "p_line_permutation", "q_bh_all_288"]]
      .round(3).to_string())
print("analysis pooled tests with q_bh_all_288 < 0.1:", int((pl.q_bh_all_288 < 0.1).sum()))
print(pl.sort_values("p_line_permutation").head(8)[["set", "tp53_group", "adjustment", "predictor", "outcome",
                                                     "mean_rho", "p_line_permutation", "q_bh_all_288"]].round(4)
      .to_string())
