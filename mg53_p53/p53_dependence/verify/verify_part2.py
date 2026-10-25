#!/usr/bin/env python3
"""Part 2 of the adversarial verification (run after verify_p53_dependence.py).

Uses (a) the analysis's own per-line corrected effects (tables/per_line_effects_selected.csv) and (b) raw panel
counts, to check: power with the analysis's values, leave-lines-out, functional regrouping, a plate-specific
baseline-adjusted (ANCOVA) WT effect, an ambient-RNA-corrected treated level, and whether the replicate agreement
of per-line TRIM72 fold changes survives removing the shared baseline.
Usage: python3 verify_part2.py
"""
import os
import numpy as np
import pandas as pd
from scipy import stats

DATA = "/home/user/tahoe_data"
HERE = os.path.dirname(os.path.abspath(__file__))
TAB = os.path.join(os.path.dirname(HERE), "tables")
OUT = os.path.join(HERE, "tables")
os.makedirs(OUT, exist_ok=True)
rng = np.random.default_rng(11)
pd.set_option("display.width", 250); pd.set_option("display.max_columns", 40)

pl = pd.read_csv(f"{TAB}/per_line_effects_selected.csv")
func = pd.read_csv(f"{DATA}/gene_panel/results/p53_functional_status.csv").set_index("cell_line_id")
base = pd.read_csv(f"{DATA}/gene_panel/results/baseline_by_cell_line.csv").set_index("cell_line_id")


def mw_power(v, lab, deltas, nsim=2000):
    res = np.concatenate([v[lab] - np.median(v[lab]), v[~lab] - np.median(v[~lab])])
    n1, n0 = lab.sum(), (~lab).sum()
    out = []
    for d in deltas:
        hits = 0
        for _ in range(nsim):
            if stats.mannwhitneyu(rng.choice(res, n1) + d, rng.choice(res, n0)).pvalue < 0.05:
                hits += 1
        out.append(hits / nsim)
    return out


def ols_wt(y, wt, b):
    """OLS y ~ 1 + wt + b: WT coefficient, its SE, t-test p and the baseline slope."""
    A = np.column_stack([np.ones(len(y)), wt, b])
    beta, *_ = np.linalg.lstsq(A, y, rcond=None)
    r = y - A @ beta
    s2 = r @ r / (len(y) - 3)
    cov = s2 * np.linalg.inv(A.T @ A)
    se = np.sqrt(cov[1, 1])
    return beta[1], se, 2 * stats.t.sf(abs(beta[1] / se), len(y) - 3), beta[2]


def perm_p(v, lab, B=10000):
    d = np.median(v[lab]) - np.median(v[~lab])
    null = np.empty(B)
    for i in range(B):
        p = rng.permutation(lab)
        null[i] = np.median(v[p]) - np.median(v[~p])
    return d, (1 + np.sum(np.abs(null) >= abs(d) - 1e-12)) / (B + 1)


# ------------------------------------------------------------ 1. power with the analysis's own per-line values
deltas = [0.25, 0.5, 0.65, 0.75, 1.0, 1.25, 1.5]
rows = []
ida = pl[(pl.drug == "Idarubicin (hydrochloride)") & np.isclose(pl.conc, 5.0)]
for scope in ida.scope.unique():
    for g in ["TRIM72", "P53_SCORE", "MDM2", "CDKN1A", "BBC3", "FDXR", "TP53I3"]:
        x = ida[(ida.scope == scope) & (ida.gene == g)].dropna(subset=["log2FC_corrected"])
        if len(x) < 20:
            continue
        v = x.log2FC_corrected.to_numpy(); lab = (x.tp53_group == "WT").to_numpy()
        sd = np.std(np.concatenate([v[lab] - np.median(v[lab]), v[~lab] - np.median(v[~lab])]))
        pw = mw_power(v, lab, deltas, nsim=1000)
        r = dict(scope=scope, gene=g, n_wt=int(lab.sum()), n_alt=int((~lab).sum()), within_group_sd=sd,
                 diff=np.median(v[lab]) - np.median(v[~lab]))
        r.update({f"power_{d}": p for d, p in zip(deltas, pw)})
        rows.append(r)
pw = pd.DataFrame(rows)
pw.to_csv(f"{OUT}/power_analysis_values_idarubicin5.csv", index=False)
print("=== Power (MW alpha 0.05) using the analysis's corrected per-line values, idarubicin 5 uM ===")
print(pw.round(2).to_string(index=False))

# ------------------------------------------------------------ 2. leave-lines-out and regrouping (analysis's values)
print("\n=== Idarubicin 5 uM TRIM72 (analysis values): regroupings and leave-lines-out ===")
rg = []
for scope in ida.scope.unique():
    x = ida[(ida.scope == scope) & (ida.gene == "TRIM72")].dropna(subset=["log2FC_corrected"]).set_index("cell_line_id")
    x = x.join(func[["functional_call", "discordant", "p53_responsiveness_log2"]])
    groupings = {
        "annotation": x.tp53_group.map({"WT": True, "altered": False}),
        "functional (responsive vs unresponsive)": x.functional_call.map({"responsive": True, "unresponsive": False}),
        "annotation minus Hs 766T and uncertain": x.tp53_group.map({"WT": True, "altered": False}).where(
            x.discordant.isna() & ~x.functional_call.str.startswith("uncertain")),
        "WT vs truncating/splice/deletion": x.tp53_group.map({"WT": True, "altered": False}).where(
            (x.tp53_group == "WT") | (x.tp53_class == "altered: truncating / splice / deletion")),
        "WT vs missense": x.tp53_group.map({"WT": True, "altered": False}).where(
            (x.tp53_group == "WT") | (x.tp53_class == "altered: missense only")),
        "responsiveness top 17 vs bottom 31 (rank)": None,
    }
    for gname, lab in groupings.items():
        if lab is None:
            rk = x.p53_responsiveness_log2.rank(ascending=False)
            lab = (rk <= 17).where(x.p53_responsiveness_log2.notna())
        ok = lab.notna()
        v = x.log2FC_corrected[ok].to_numpy(); L = lab[ok].astype(bool).to_numpy()
        d, p = perm_p(v, L)
        # leave-one-out and drop 3 extremes
        loo = [np.median(np.delete(v, i)[np.delete(L, i)]) - np.median(np.delete(v, i)[~np.delete(L, i)]) for i in range(len(v))]
        a, b = np.sort(v[L]), np.sort(v[~L])
        rg.append(dict(scope=scope, grouping=gname, n1=int(L.sum()), n0=int((~L).sum()), fc1=2 ** np.median(v[L]),
                       fc0=2 ** np.median(v[~L]), diff=d, p_perm=p, loo_min=min(loo), loo_max=max(loo),
                       drop3_top_wt_bottom_alt=np.median(a[:-3]) - np.median(b[3:]),
                       drop3_bottom_wt_top_alt=np.median(a[3:]) - np.median(b[:-3])))
rg = pd.DataFrame(rg)
rg.to_csv(f"{OUT}/regrouping_idarubicin5_analysis_values.csv", index=False)
print(rg.round(3).to_string(index=False))

# ------------------------------------------------------------ 3. raw counts: plate-specific baseline, ambient, ANCOVA
smap = pd.read_csv(f"{DATA}/gene_panel/sample_map.csv")
cols = ["sample", "cell_line_id", "n_cells", "total_counts", "MTAP", "TRIM72"]
wl = pd.read_parquet(f"{DATA}/gene_panel/well_line.parquet", columns=cols)
wl = wl.groupby(["sample", "cell_line_id"], as_index=False).sum().merge(
    smap[["sample", "plate", "well", "drug", "conc", "is_dmso"]], on="sample")
null_lines = set(base.index[base.MTAP_null.astype(bool)])


def ambient_frac(w):
    pooled = w.MTAP.sum() / w.total_counts.sum()
    nl = w[w.cell_line_id.isin(null_lines)]
    return (nl.MTAP.sum() / nl.total_counts.sum()) / pooled


def line_levels(sample_ids, min_cells=30):
    """Per line: observed TRIM72 CPM pooled over the given wells and an ambient-corrected ('intrinsic') CPM:
    (cpm_line - a * cpm_pooled_well) / (1 - a), a = MTAP-null-line ambient fraction of each well."""
    out = []
    for s in sample_ids:
        w = wl[wl["sample"] == s]
        a = ambient_frac(w)
        pooled = 1e6 * w.TRIM72.sum() / w.total_counts.sum()
        ww = w[w.n_cells >= min_cells].copy()
        ww["cpm"] = 1e6 * ww.TRIM72 / ww.total_counts
        ww["cpm_intrinsic"] = ((ww.cpm - a * pooled) / (1 - a)).clip(lower=0)
        ww["ambient_frac"] = a
        ww["pooled_cpm"] = pooled
        out.append(ww)
    return pd.concat(out)


rows = []
anc_rows = []
for plate in ["plate6", "plate14"]:
    tr = smap[(smap.drug == "Idarubicin (hydrochloride)") & np.isclose(smap.conc, 5.0) & (smap.plate == plate)]["sample"]
    dm = smap[(smap.is_dmso.astype(bool)) & (smap.plate == plate)]["sample"]
    T = line_levels(tr).set_index("cell_line_id")
    D = line_levels(dm, min_cells=1).groupby("cell_line_id").agg(TRIM72=("TRIM72", "sum"), total=("total_counts", "sum"),
                                                                  cpm_intr=("cpm_intrinsic", "mean"))
    D["cpm"] = 1e6 * D.TRIM72 / D.total
    x = T[["cpm", "cpm_intrinsic", "TRIM72", "ambient_frac", "pooled_cpm"]].join(D[["cpm", "cpm_intr"]], rsuffix="_dmso")
    x = x.join(base[["tp53_group", "cell_name"]]).join(func[["functional_call", "p53_responsiveness_log2"]])
    x = x[x.index != "CVCL_1577"]                                           # NCI-H661: not expressed
    x["log2_treated"] = np.log2(x.cpm + 0.5)
    x["log2_treated_intr"] = np.log2(x.cpm_intrinsic + 0.5)
    x["log2_dmso"] = np.log2(x.cpm_dmso + 0.5)
    x["log2_dmso_allplates"] = np.log2(base.reindex(x.index)["TRIM72_cpm_dmso"] + 0.5)
    x["log2fc"] = x.log2_treated - x.log2_dmso
    x["log2fc_intr"] = x.log2_treated_intr - np.log2(x.cpm_intr + 0.5)
    x["wt"] = (x.tp53_group == "WT").astype(float)
    x["plate"] = plate
    rows.append(x)
    lab = x.wt.astype(bool).to_numpy()
    for q in ["log2_treated", "log2_treated_intr", "log2_dmso", "log2fc", "log2fc_intr"]:
        d, p = perm_p(x[q].to_numpy(), lab)
        anc_rows.append(dict(plate=plate, quantity=q, n_wt=int(lab.sum()), n_alt=int((~lab).sum()),
                             median_wt=np.median(x[q][lab]), median_alt=np.median(x[q][~lab]), diff=d, p_perm=p,
                             ambient_frac=x.ambient_frac.iloc[0], pooled_cpm=x.pooled_cpm.iloc[0]))
    # ANCOVA: log2 treated ~ WT + log2 baseline (plate-specific DMSO, and all-plates DMSO)
    for bname in ["log2_dmso", "log2_dmso_allplates"]:
        for yname in ["log2_treated", "log2_treated_intr"]:
            yy = x[yname].to_numpy(); bb = x[bname].to_numpy(); ww = x.wt.to_numpy()
            ok = np.isfinite(yy) & np.isfinite(bb)
            yy, bb, ww = yy[ok], bb[ok], ww[ok]
            coef, se, pt, slope = ols_wt(yy, ww, bb)
            null = np.array([ols_wt(yy, rng.permutation(ww), bb)[0] for _ in range(5000)])
            pperm = (1 + np.sum(np.abs(null) >= abs(coef))) / 5001
            # rank-based: WT effect on the residual ranks of y after baseline (Spearman partial-style)
            anc_rows.append(dict(plate=plate, quantity=f"ANCOVA {yname} ~ WT + {bname}", n_wt=int(ww.sum()),
                                 n_alt=int((1 - ww).sum()), diff=coef, p_perm=pperm, p_t=pt, se=se,
                                 baseline_slope=slope))
anc = pd.DataFrame(anc_rows)
anc.to_csv(f"{OUT}/idarubicin5_levels_ambient_ancova.csv", index=False)
print("\n=== Idarubicin 5 uM: levels, ambient-corrected levels and plate-specific ANCOVA (p_perm = OLS p for ANCOVA rows) ===")
print(anc.round(3).to_string(index=False))

both = pd.concat(rows)
both.to_csv(f"{OUT}/idarubicin5_levels_per_line.csv")

# ------------------------------------------------------------ 4. replicate agreement beyond the shared baseline
p6 = both[both.plate == "plate6"]; p14 = both[both.plate == "plate14"]
common = p6.index.intersection(p14.index)


def partial_spearman(x, y, z):
    rx, ry, rz = stats.rankdata(x), stats.rankdata(y), stats.rankdata(z)
    Z = np.column_stack([np.ones(len(rz)), rz])
    ex = rx - Z @ np.linalg.lstsq(Z, rx, rcond=None)[0]
    ey = ry - Z @ np.linalg.lstsq(Z, ry, rcond=None)[0]
    r = np.corrcoef(ex, ey)[0, 1]
    n = len(x); t = r * np.sqrt((n - 3) / (1 - r * r))
    return r, 2 * stats.t.sf(abs(t), n - 3)


an = pl[(pl.drug == "Idarubicin (hydrochloride)") & np.isclose(pl.conc, 5.0) & (pl.gene == "TRIM72")]
a6 = an[an.scope.str.startswith("plate6")].set_index("cell_line_id").log2FC_corrected
a14 = an[an.scope.str.startswith("plate14")].set_index("cell_line_id").log2FC_corrected
cc = a6.index.intersection(a14.index).intersection(common)
bl = np.log2(base.reindex(cc)["TRIM72_cpm_dmso"] + 0.5)
rep = dict(
    n=len(cc),
    analysis_fc_spearman=stats.spearmanr(a6[cc], a14[cc])[0],
    analysis_fc_partial_given_dmso_allplates=partial_spearman(a6[cc].values, a14[cc].values, bl.values),
    analysis_fc6_vs_baseline=stats.spearmanr(a6[cc], bl)[0],
    analysis_fc14_vs_baseline=stats.spearmanr(a14[cc], bl)[0],
    treated_cpm_spearman=stats.spearmanr(p6.loc[cc, "cpm"], p14.loc[cc, "cpm"])[0],
    treated_cpm_partial_given_baseline=partial_spearman(p6.loc[cc, "cpm"].values, p14.loc[cc, "cpm"].values, bl.values),
    intrinsic_treated_partial_given_baseline=partial_spearman(p6.loc[cc, "cpm_intrinsic"].values,
                                                              p14.loc[cc, "cpm_intrinsic"].values, bl.values),
)
print("\n=== Replicate agreement of idarubicin 5 uM per-line TRIM72 between plate 6 and plate 14 ===")
for k, v in rep.items():
    print(f"{k}: {v}")
pd.Series({k: str(v) for k, v in rep.items()}).to_csv(f"{OUT}/replicate_beyond_baseline.csv")

# ------------------------------------------------------------ 5. concordance of my DMSO-ratio values with the analysis's
mine = pd.read_csv(f"{OUT}/per_line_dmso_ratio.csv")
conc_rows = []
for (drug, conc, scope_m), scope_a in [(("Idarubicin (hydrochloride)", 5.0, "mean"), "mean of used wells"),
                                       (("Idarubicin (hydrochloride)", 5.0, "plate6"), "plate6 C12 only"),
                                       (("Idarubicin (hydrochloride)", 5.0, "plate14"), "plate14 C12 only"),
                                       (("Selinexor", 5.0, "mean"), "mean of used wells"),
                                       (("Homoharringtonine", 5.0, "mean"), "mean of used wells"),
                                       (("Epirubicin (hydrochloride)", 5.0, "plate9"), "mean of used wells")]:
    for g in ["TRIM72", "P53_SCORE", "MDM2"]:
        m = mine[(mine.drug == drug) & np.isclose(mine.conc, conc) & (mine.scope == scope_m) & (mine.gene == g)].set_index("cell_line_id").log2_vs_dmso
        a = pl[(pl.drug == drug) & np.isclose(pl.conc, conc) & (pl.scope == scope_a) & (pl.gene == g)].set_index("cell_line_id").log2FC_corrected
        c = m.dropna().index.intersection(a.dropna().index)
        conc_rows.append(dict(drug=drug, conc=conc, scope=scope_m, gene=g, n=len(c),
                              spearman=stats.spearmanr(m[c], a[c])[0], median_mine=m[c].median(), median_analysis=a[c].median()))
cr = pd.DataFrame(conc_rows)
cr.to_csv(f"{OUT}/concordance_dmso_ratio_vs_analysis.csv", index=False)
print("\n=== Concordance of independent DMSO-ratio per-line values with the analysis's corrected values ===")
print(cr.round(3).to_string(index=False))
