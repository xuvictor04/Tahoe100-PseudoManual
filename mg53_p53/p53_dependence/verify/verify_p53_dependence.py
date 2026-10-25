#!/usr/bin/env python3
"""Adversarial verification of the p53-dependence findings for TRIM72 (independent code).

Independent per-line effect: simple DMSO-baseline log2 ratio from the raw gene-panel counts
(well_line.parquet): log2((c_treated + 0.5) / T_treated) - log2((c_dmso + 0.5) / T_dmso), where the DMSO
baseline is the pooled counts of the same line in the plate's 2 DMSO wells. No composition, position or
plate-factor correction. Profiles with < 30 cells are dropped; a line must express the gene (pooled DMSO
CPM over all plates >= 1).

Writes tables under verify/tables/. Read-only on /home/user/tahoe_data.
Usage: python3 verify_p53_dependence.py
"""
import os
import sys
import numpy as np
import pandas as pd
from scipy import stats

DATA = "/home/user/tahoe_data"
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "tables")
os.makedirs(OUT, exist_ok=True)
RNG = np.random.default_rng(7)
B = 10000
MIN_CELLS = 30
P53_ACTIVITY = ["CDKN1A", "MDM2", "FDXR", "ZMAT3", "SESN1", "BBC3", "BAX", "TP53I3", "RRM2B", "AEN", "DDB2",
                "XPC", "PHLDA3", "SPATA18", "TRIAP1", "RPS27L", "ACER2", "TP53INP1", "PLK3", "POLH", "EDA2R"]
GENES = ["TRIM72", "MDM2", "CDKN1A", "TP53I3", "FDXR", "BBC3"]
DRUGDOSES = [("Idarubicin (hydrochloride)", 5.0), ("Idarubicin (hydrochloride)", 0.5),
             ("Selinexor", 5.0), ("Homoharringtonine", 5.0), ("Epirubicin (hydrochloride)", 5.0),
             ("Doxorubicin (hydrochloride)", 5.0), ("Auranofin", 5.0), ("Dinaciclib", 5.0)]

# ---------------------------------------------------------------- load
sm = pd.read_csv(f"{DATA}/gene_panel/sample_map.csv")
cols = ["sample", "cell_line_id", "n_cells", "total_counts", "MTAP"] + sorted(set(GENES + P53_ACTIVITY))
wl = pd.read_parquet(f"{DATA}/gene_panel/well_line.parquet", columns=cols)
wl = wl.groupby(["sample", "cell_line_id"], as_index=False).sum()           # sum duplicate rows if any
wl = wl.merge(sm[["sample", "plate", "well", "drug", "conc", "is_dmso"]], on="sample", how="left")
assert wl.plate.notna().all()

base = pd.read_csv(f"{DATA}/gene_panel/results/baseline_by_cell_line.csv")
func = pd.read_csv(f"{DATA}/gene_panel/results/p53_functional_status.csv")
lines = base[["cell_line_id", "cell_name", "Organ", "tp53_group", "tp53_changes", "MTAP_null"]].merge(
    func[["cell_line_id", "p53_responsiveness_log2", "functional_call", "discordant"]], on="cell_line_id", how="left")
lines = lines.set_index("cell_line_id")

# expression: pooled DMSO CPM over all plates
dm = wl[wl.is_dmso.astype(bool)]
dpool = dm.groupby("cell_line_id")[cols[3:]].sum()
cpm_dmso_all = dpool[cols[4:]].div(dpool.total_counts, axis=0) * 1e6
expressed = cpm_dmso_all >= 1.0

# DMSO baseline per (plate, line)
dpl = dm.groupby(["plate", "cell_line_id"])[cols[3:]].sum()


def lfc_table(sample):
    """Per line log2 ratio vs plate DMSO for every gene of `cols`, plus the 21-gene P53 score."""
    t = wl[(wl["sample"] == sample) & (wl.n_cells >= MIN_CELLS)].set_index("cell_line_id")
    plate = sm.loc[sm["sample"] == sample, "plate"].iloc[0]
    d = dpl.loc[plate].reindex(t.index)
    out = pd.DataFrame(index=t.index)
    for g in cols[4:]:
        lt = np.log2((t[g] + 0.5) / t.total_counts)
        ld = np.log2((d[g] + 0.5) / d.total_counts)
        v = lt - ld
        v[~expressed.reindex(t.index)[g].fillna(False).values] = np.nan
        out[g] = v
        out[g + "_cpm_treated"] = 1e6 * t[g] / t.total_counts
        out[g + "_cpm_dmso"] = 1e6 * d[g] / d.total_counts
        out[g + "_counts"] = t[g]
    out["P53_SCORE"] = out[P53_ACTIVITY].mean(axis=1, skipna=True)
    out["n_cells"] = t.n_cells
    return out


# ---------------------------------------------------------------- statistics
def hl(a, b):
    return np.median(np.subtract.outer(a, b))


def compare(v, lab, B=B, rng=RNG):
    """v: values; lab: True = group 1 (WT). Returns dict of effect sizes and tests."""
    v = np.asarray(v, float); lab = np.asarray(lab, bool)
    ok = np.isfinite(v); v = v[ok]; lab = lab[ok]
    a, b = v[lab], v[~lab]
    d = np.median(a) - np.median(b)
    perm = np.empty(B)
    for i in range(B):
        p = rng.permutation(lab)
        perm[i] = np.median(v[p]) - np.median(v[~p])
    p_perm = (1 + np.sum(np.abs(perm) >= abs(d) - 1e-12)) / (B + 1)
    boot = np.empty(B)
    for i in range(B):
        boot[i] = np.median(rng.choice(a, len(a))) - np.median(rng.choice(b, len(b)))
    mw = stats.mannwhitneyu(a, b, alternative="two-sided")
    return dict(n1=len(a), n0=len(b), med1=np.median(a), med0=np.median(b), fc1=2 ** np.median(a),
                fc0=2 ** np.median(b), diff_medians=d, hodges_lehmann=hl(a, b),
                ci_low=np.percentile(boot, 2.5), ci_high=np.percentile(boot, 97.5), p_perm=p_perm,
                p_mw=mw.pvalue, auc=mw.statistic / (len(a) * len(b)),
                crit_abs_diff_p05=np.percentile(np.abs(perm), 95))


def loo(v, lab, names):
    """Leave-one-line-out range of the difference of medians, and the most influential line."""
    v = np.asarray(v, float); lab = np.asarray(lab, bool); names = np.asarray(names)
    ok = np.isfinite(v); v, lab, names = v[ok], lab[ok], names[ok]
    res = []
    for i in range(len(v)):
        m = np.ones(len(v), bool); m[i] = False
        res.append(np.median(v[m][lab[m]]) - np.median(v[m][~lab[m]]))
    res = np.array(res)
    full = np.median(v[lab]) - np.median(v[~lab])
    i = np.argmax(np.abs(res - full))
    return res.min(), res.max(), names[i]


def drop_k_extremes(v, lab, k=3):
    """Drop the k most extreme lines (by value) of each group's tail that favours the observed sign, recompute."""
    v = np.asarray(v, float); lab = np.asarray(lab, bool)
    ok = np.isfinite(v); v, lab = v[ok], lab[ok]
    a, b = np.sort(v[lab]), np.sort(v[~lab])
    # both directions: remove top-k WT and bottom-k altered (favours null if diff > 0), and the reverse
    d1 = np.median(a[:-k]) - np.median(b[k:])
    d2 = np.median(a[k:]) - np.median(b[:-k])
    return d1, d2


def power_curve(v, lab, deltas, nsim=2000, rng=RNG):
    """Power of a two-sided Mann-Whitney test (alpha 0.05) to detect a WT shift delta, resampling the
    pooled within-group residuals (each group centred at its median) with the observed group sizes."""
    v = np.asarray(v, float); lab = np.asarray(lab, bool)
    ok = np.isfinite(v); v, lab = v[ok], lab[ok]
    res = np.concatenate([v[lab] - np.median(v[lab]), v[~lab] - np.median(v[~lab])])
    n1, n0 = lab.sum(), (~lab).sum()
    out = []
    for dlt in deltas:
        hits = 0
        for _ in range(nsim):
            a = rng.choice(res, n1) + dlt
            b = rng.choice(res, n0)
            if stats.mannwhitneyu(a, b, alternative="two-sided").pvalue < 0.05:
                hits += 1
        out.append(hits / nsim)
    return np.array(out)


# ---------------------------------------------------------------- per-line effects
tabs = {}
for drug, conc in DRUGDOSES:
    smp = sm[(sm.drug == drug) & (np.isclose(sm.conc, conc))]
    smp = smp[smp.plate != "plate13"]
    per = []
    for _, r in smp.iterrows():
        t = lfc_table(r["sample"])
        t["scope"] = f"{r.plate} {r.well}"
        tabs[(drug, conc, r.plate)] = t
        per.append(t)
    if len(per) > 1:
        g = [c for c in per[0].columns if c not in ("scope",)]
        num = [c for c in g if not c.endswith(("_cpm_treated", "_cpm_dmso", "_counts")) and c != "n_cells"]
        m = pd.concat([p[num] for p in per], axis=1, keys=range(len(per)))
        mean = pd.DataFrame({c: m.xs(c, axis=1, level=1).mean(axis=1, skipna=True) for c in num})
        tabs[(drug, conc, "mean")] = mean

# ---------------------------------------------------------------- group comparisons
grp_defs = {
    "annotation WT vs altered": lambda L: L.tp53_group.map({"WT": True, "altered": False}),
    "functional responsive vs unresponsive (uncertain dropped)": lambda L: L.functional_call.map(
        {"responsive": True, "unresponsive": False}),
    "annotation, discordant + uncertain dropped": lambda L: L.tp53_group.map({"WT": True, "altered": False}).where(
        ~L.functional_call.str.startswith("uncertain").fillna(False) & L.discordant.isna()),
    "annotation, truncating/splice/deletion altered only": lambda L: L.tp53_group.map({"WT": True, "altered": False}).where(
        (L.tp53_group == "WT") | L.tp53_changes.fillna("").str.contains("fs|\\*|Splice|splice|DEL|\\+|T125T", regex=True)),
}

rows = []
per_line_rows = []
for (drug, conc, scope), t in tabs.items():
    L = lines.reindex(t.index)
    for gname, gf in grp_defs.items():
        lab = gf(L)
        for g in GENES + ["P53_SCORE"]:
            v = t[g]
            ok = lab.notna() & v.notna()
            if ok.sum() < 10:
                continue
            r = compare(v[ok].values, lab[ok].astype(bool).values)
            lo, hi, who = loo(v[ok].values, lab[ok].astype(bool).values, L.cell_name[ok].values)
            dk1, dk2 = drop_k_extremes(v[ok].values, lab[ok].astype(bool).values, 3)
            r.update(drug=drug, conc=conc, scope=scope, grouping=gname, gene=g, loo_min=lo, loo_max=hi,
                     most_influential_line=who, diff_drop3_top_wt_bottom_alt=dk1, diff_drop3_bottom_wt_top_alt=dk2)
            rows.append(r)
    for g in GENES + ["P53_SCORE"]:
        for cl, val in t[g].items():
            per_line_rows.append(dict(drug=drug, conc=conc, scope=scope, gene=g, cell_line_id=cl,
                                      cell_name=lines.cell_name.get(cl), tp53_group=lines.tp53_group.get(cl),
                                      functional_call=lines.functional_call.get(cl), log2_vs_dmso=val))
res = pd.DataFrame(rows)
first = ["drug", "conc", "scope", "grouping", "gene"]
res = res[first + [c for c in res.columns if c not in first]]
res.to_csv(f"{OUT}/wt_vs_altered_dmso_ratio.csv", index=False)
pd.DataFrame(per_line_rows).to_csv(f"{OUT}/per_line_dmso_ratio.csv", index=False)

pd.set_option("display.width", 250); pd.set_option("display.max_columns", 40); pd.set_option("display.max_rows", 500)
show = ["drug", "conc", "scope", "gene", "n1", "n0", "fc1", "fc0", "diff_medians", "hodges_lehmann", "ci_low",
        "ci_high", "p_perm", "p_mw", "crit_abs_diff_p05", "loo_min", "loo_max", "most_influential_line"]
print("=== annotation WT vs altered (DMSO-baseline log2 ratio) ===")
print(res[res.grouping == "annotation WT vs altered"][show].round(3).to_string(index=False))
for gname in list(grp_defs)[1:]:
    print(f"\n=== {gname}: TRIM72 and P53_SCORE ===")
    print(res[(res.grouping == gname) & res.gene.isin(["TRIM72", "P53_SCORE", "MDM2"])][show].round(3).to_string(index=False))

# ---------------------------------------------------------------- idarubicin 5 uM: line list, levels, ambient
ida = tabs[("Idarubicin (hydrochloride)", 5.0, "mean")]
p6 = tabs[("Idarubicin (hydrochloride)", 5.0, "plate6")]
p14 = tabs[("Idarubicin (hydrochloride)", 5.0, "plate14")]
lst = lines.reindex(ida.index)[["cell_name", "Organ", "tp53_group", "tp53_changes", "functional_call",
                                "p53_responsiveness_log2"]].copy()
lst["TRIM72_log2_mean"] = ida.TRIM72
lst["TRIM72_fc_mean"] = 2 ** ida.TRIM72
lst["TRIM72_fc_plate6"] = 2 ** p6.TRIM72.reindex(ida.index)
lst["TRIM72_fc_plate14"] = 2 ** p14.TRIM72.reindex(ida.index)
lst["TRIM72_cpm_treated_pl6"] = p6.TRIM72_cpm_treated.reindex(ida.index)
lst["TRIM72_cpm_treated_pl14"] = p14.TRIM72_cpm_treated.reindex(ida.index)
lst["TRIM72_cpm_dmso_pl6"] = p6.TRIM72_cpm_dmso.reindex(ida.index)
lst["TRIM72_cpm_dmso_pl14"] = p14.TRIM72_cpm_dmso.reindex(ida.index)
lst["TRIM72_counts_pl6"] = p6.TRIM72_counts.reindex(ida.index)
lst["TRIM72_counts_pl14"] = p14.TRIM72_counts.reindex(ida.index)
lst["P53_SCORE_mean"] = ida.P53_SCORE
lst["MDM2_mean"] = ida.MDM2
lst["TRIM72_cpm_dmso_allplates"] = cpm_dmso_all.TRIM72.reindex(ida.index)
lst = lst.sort_values(["tp53_group", "TRIM72_log2_mean"], ascending=[False, False])
lst.to_csv(f"{OUT}/idarubicin5_per_line.csv")
print("\n=== Idarubicin 5 uM per line ===")
print(lst.round(2).to_string())

# absolute treated level WT vs altered (no baseline)
print("\n=== Idarubicin 5 uM: treated TRIM72 log2 CPM (absolute level, no baseline) WT vs altered ===")
lev_rows = []
for nm, t in [("plate6", p6), ("plate14", p14)]:
    L = lines.reindex(t.index)
    lab = L.tp53_group.map({"WT": True, "altered": False})
    ok = lab.notna() & expressed.TRIM72.reindex(t.index).fillna(False) & (t.TRIM72_counts.notna())
    v = np.log2(t.TRIM72_cpm_treated[ok] + 1)
    r = compare(v.values, lab[ok].astype(bool).values); r.update(scope=nm, quantity="log2(treated CPM+1)")
    lev_rows.append(r)
    v = np.log2(t.TRIM72_cpm_dmso[ok] + 1)
    r = compare(v.values, lab[ok].astype(bool).values); r.update(scope=nm, quantity="log2(DMSO CPM+1), same plate")
    lev_rows.append(r)
lev = pd.DataFrame(lev_rows)
lev.to_csv(f"{OUT}/idarubicin5_levels_wt_vs_altered.csv", index=False)
print(lev[["scope", "quantity", "n1", "n0", "med1", "med0", "diff_medians", "ci_low", "ci_high", "p_perm", "p_mw"]].round(3).to_string(index=False))

# replicate agreement of the ABSOLUTE treated level vs of the fold change, and dependence of FC on baseline
both = p6.index.intersection(p14.index)
both = [c for c in both if expressed.TRIM72.get(c, False)]
rep = dict(
    n=len(both),
    spearman_fc=stats.spearmanr(p6.TRIM72[both], p14.TRIM72[both], nan_policy="omit")[0],
    spearman_treated_cpm=stats.spearmanr(p6.TRIM72_cpm_treated[both], p14.TRIM72_cpm_treated[both])[0],
    spearman_dmso_cpm=stats.spearmanr(p6.TRIM72_cpm_dmso[both], p14.TRIM72_cpm_dmso[both])[0],
    spearman_fc_vs_dmso_allplates=stats.spearmanr(ida.TRIM72[both], cpm_dmso_all.TRIM72[both])[0],
    cv_treated_cpm_pl6=np.std(np.log2(p6.TRIM72_cpm_treated[both] + 1)),
    sd_log2_dmso_cpm_pl6=np.std(np.log2(p6.TRIM72_cpm_dmso[both] + 1)),
    sd_log2_treated_cpm_pl14=np.std(np.log2(p14.TRIM72_cpm_treated[both] + 1)),
    sd_log2_dmso_cpm_pl14=np.std(np.log2(p14.TRIM72_cpm_dmso[both] + 1)),
)
# slope of log2 treated vs log2 DMSO (all plates baseline): 1 = fold change constant, 0 = level constant
x = np.log2(cpm_dmso_all.TRIM72[both]); y = np.log2(0.5 * (p6.TRIM72_cpm_treated[both] + p14.TRIM72_cpm_treated[both]) + 0.5)
lr = stats.linregress(x, y)
rep.update(slope_log2treated_on_log2dmso=lr.slope, slope_se=lr.stderr, r_treated_vs_dmso=lr.rvalue)
pd.Series(rep).to_csv(f"{OUT}/idarubicin5_replicate_and_baseline.csv")
print("\n=== Idarubicin 5 uM replicate / baseline structure ===")
print(pd.Series(rep).round(3).to_string())

# ambient RNA in the idarubicin wells: MTAP in MTAP-null lines and TRIM72 in the non-expressing line
amb_rows = []
null_lines = lines.index[lines.MTAP_null.astype(bool)]
for smp_id in sm[(sm.drug == "Idarubicin (hydrochloride)") | sm.is_dmso.astype(bool)]["sample"]:
    w = wl[wl["sample"] == smp_id]
    info = sm[sm["sample"] == smp_id].iloc[0]
    pooled_mtap = w.MTAP.sum() / w.total_counts.sum() * 1e6
    nl = w[w.cell_line_id.isin(null_lines)]
    null_mtap = nl.MTAP.sum() / nl.total_counts.sum() * 1e6
    pooled_trim = w.TRIM72.sum() / w.total_counts.sum() * 1e6
    h661 = w[w.cell_line_id == "CVCL_1577"]
    amb_rows.append(dict(sample=smp_id, plate=info.plate, well=info.well, drug=info.drug, conc=info.conc,
                         ambient_frac_MTAP=null_mtap / pooled_mtap, pooled_TRIM72_cpm=pooled_trim,
                         H661_TRIM72_counts=int(h661.TRIM72.sum()), H661_cells=int(h661.n_cells.sum()),
                         H661_TRIM72_cpm=1e6 * h661.TRIM72.sum() / max(h661.total_counts.sum(), 1),
                         ambient_expected_TRIM72_cpm=null_mtap / pooled_mtap * pooled_trim))
amb = pd.DataFrame(amb_rows)
amb = amb[amb.plate.isin(["plate4", "plate5", "plate6", "plate14"])]
amb.to_csv(f"{OUT}/ambient_check_idarubicin.csv", index=False)
print("\n=== Ambient RNA check (idarubicin wells and DMSO wells, plates 4-6, 14) ===")
print(amb.round(3).to_string(index=False))

# ---------------------------------------------------------------- power
deltas = np.array([0.25, 0.5, 0.65, 0.75, 1.0, 1.25, 1.5])
pw_rows = []
for key in [("Idarubicin (hydrochloride)", 5.0, "mean"), ("Idarubicin (hydrochloride)", 5.0, "plate6"),
            ("Idarubicin (hydrochloride)", 5.0, "plate14")]:
    t = tabs[key]
    L = lines.reindex(t.index)
    lab = L.tp53_group.map({"WT": True, "altered": False})
    for g in ["TRIM72", "P53_SCORE", "MDM2"]:
        ok = lab.notna() & t[g].notna()
        pc = power_curve(t[g][ok].values, lab[ok].astype(bool).values, deltas, nsim=1000)
        for dl, p in zip(deltas, pc):
            pw_rows.append(dict(drug=key[0], conc=key[1], scope=key[2], gene=g, delta_log2=dl, power_mw_p05=p,
                                n_wt=int(lab[ok].sum()), n_alt=int((~lab[ok].astype(bool)).sum()),
                                within_group_sd=np.std(np.concatenate([t[g][ok][lab[ok].astype(bool)] - t[g][ok][lab[ok].astype(bool)].median(),
                                                                      t[g][ok][~lab[ok].astype(bool)] - t[g][ok][~lab[ok].astype(bool)].median()]))))
pw = pd.DataFrame(pw_rows)
pw.to_csv(f"{OUT}/power_idarubicin5.csv", index=False)
print("\n=== Power (Mann-Whitney, alpha 0.05) to detect a WT shift, resampled residuals ===")
print(pw.pivot_table(index=["scope", "gene", "within_group_sd"], columns="delta_log2", values="power_mw_p05").round(2).to_string())

# ---------------------------------------------------------------- continuous responsiveness
print("\n=== Spearman of per-line effect with p53 responsiveness (note: responsiveness uses idarubicin wells) ===")
sp_rows = []
for key in [("Idarubicin (hydrochloride)", 5.0, "mean"), ("Selinexor", 5.0, "mean"), ("Homoharringtonine", 5.0, "mean"),
            ("Epirubicin (hydrochloride)", 5.0, "plate9")]:
    t = tabs[key]
    L = lines.reindex(t.index)
    for g in ["TRIM72", "P53_SCORE", "MDM2"]:
        ok = t[g].notna() & L.p53_responsiveness_log2.notna()
        rho, p = stats.spearmanr(t[g][ok], L.p53_responsiveness_log2[ok])
        sp_rows.append(dict(drug=key[0], conc=key[1], scope=key[2], gene=g, n=int(ok.sum()), rho=rho, p=p))
sp = pd.DataFrame(sp_rows)
sp.to_csv(f"{OUT}/spearman_responsiveness.csv", index=False)
print(sp.round(3).to_string(index=False))
print("\ntables written to", OUT)
