#!/usr/bin/env python3
"""MDM2 against MG53, level by level.

MDM2 is a p53 *regulator*, not a p53 effector: p53 induces it, and the MDM2 protein then ubiquitinates p53
and sends it for degradation. So a relationship between MG53 and MDM2 is not a reading of p53's output - and
in this data it does not behave like one either, which is the point of the table. MDM2 is also the single
best-measured gene in the whole analysis: 185.8 CPM median, detected in all 50 lines, moved up by 96 of 98
reference compounds. MG53 sits at 5.89 CPM with 12.4% zeros. Whatever MDM2 shows is not a detection problem.

The question asked here is deliberately flat-footed: take different levels of MG53 and different levels of
MDM2 and put them side by side. There are four resolutions at which both genes exist in a run's output, and
they do not agree with each other, which is the finding:

  unit 1  baseline across lines          48 lines           each line's untreated level of both genes
  unit 2  drug-dose, lines pooled      1,132 drug-doses     each exposure's effect on both genes
  unit 3  line x drug-dose               861 cells          18 MG53-raising exposures x 50 lines
  unit 4  the genome-wide screen      53,084 cells          reported from c_screen_genes, not recomputed
  unit 5  single cells in one well    up to 47 lines        MG53-detected vs MG53-undetected cells, with
                                                            78-85 control genes as the placebo family

Two different things get called "level" and they behave differently, so both are binned separately:

  LEVEL   how much MG53 mRNA is present      (CPM, or the line's baseline, or TRIM72_level)
  CHANGE  how far MG53 moved under the drug  (log2 fold change: TRIM72_z / TRIM72_r2 / fold change)

Controls carried through every unit, because each is a live alternative explanation of a negative slope:
  activity    atlas_n_sig_genes, cells_log2_vs_plate, S_PHASE_z, G2M_PHASE_z, umi_per_cell_log2_vs_plate
              - a drug that moves the whole transcriptome moves both genes, in whatever direction each has
  p53         P53_ACTIVITY_z - if the relationship runs through p53 it should vanish when p53 output is held
              fixed, and should be absent in lines that have no p53
  genotype    every contrast is also split TP53-WT vs TP53-altered; MDM2's induction needs p53, so a slope
              that is the same size in altered lines is not p53-mediated
  plate       MG53 carries a 3.12 log2 plate-batch gap, the largest of 16,656 genes, so the within-plate
              version of the drug-dose contrast is computed too

Uncertainty: bin means get an ordinary SE, but drug-doses of the same compound are not independent (three
doses each), so every slope and correlation also gets a 2,000-draw bootstrap clustered on compound. The
per-line unit clusters on cell line and removes drug-dose means first.

Usage:
    python3 mdm2_mg53_levels.py --results ~/Tahoe-100M/mg53_p53
"""
import argparse
import hashlib
import os

import numpy as np
import pandas as pd
from scipy import stats as st

GENE, PARTNER = "MDM2", "CDKN1A"           # PARTNER is the contrast gene: a p53 effector, opposite sign
ACTIVITY = ["atlas_n_sig_genes", "cells_log2_vs_plate", "S_PHASE_z", "G2M_PHASE_z",
            "umi_per_cell_log2_vs_plate"]
REL = 0.2894                               # MG53 split-half reliability, for the measured -> true conversion
NDRAW = 2000
SEED = 0


# ----------------------------------------------------------------------------- small statistics helpers
def resid(y, X, mask=None):
    """y with the columns of X (plus an intercept) projected out; NaN rows propagate as NaN.

    `mask` restricts the rows the regression is ESTIMATED on. Pass it whenever the residual will be
    correlated against another residual: fitting x and y on different row sets leaves the two residuals
    orthogonal to the covariates on different subsets, so on their intersection neither is clean. Use
    resid_pair rather than calling this twice.
    """
    y = pd.to_numeric(y, errors="coerce")
    X = X.apply(pd.to_numeric, errors="coerce")
    ok = y.notna() & X.notna().all(axis=1)
    if mask is not None:
        ok = ok & mask.reindex(y.index).fillna(False)
    out = pd.Series(np.nan, index=y.index, dtype=float)
    if ok.sum() <= X.shape[1] + 1:
        return out
    A = np.column_stack([np.ones(int(ok.sum()))] + [X.loc[ok, c].to_numpy(float) for c in X.columns])
    beta, *_ = np.linalg.lstsq(A, y.loc[ok].to_numpy(float), rcond=None)
    out.loc[ok] = y.loc[ok].to_numpy(float) - A @ beta
    return out


def resid_pair(x, y, X):
    """Residualise x and y on X over the SAME rows: the intersection where x, y and every covariate exist."""
    x, y = pd.to_numeric(x, errors="coerce"), pd.to_numeric(y, errors="coerce")
    Xn = X.apply(pd.to_numeric, errors="coerce")
    ok = x.notna() & y.notna() & Xn.notna().all(axis=1)
    return resid(x, X, ok), resid(y, X, ok)


def fit(x, y, cluster=None, label="", seed_tag=""):
    """OLS slope, both correlations, a cluster-robust SE, and a cluster bootstrap when a key is given.

    Three p values come back and they are not interchangeable, which is the point of naming them:
      p            the OLS slope's p, from the iid SE. Quote it only beside b.
      p_cluster    the slope's p from the cluster-robust SE. Prefer it when a cluster key exists.
      p_spearman   Spearman's own p. The ONLY p to quote beside rho.
    """
    d = pd.DataFrame({"x": pd.to_numeric(x, errors="coerce"), "y": pd.to_numeric(y, errors="coerce")})
    if cluster is not None:
        d["g"] = np.asarray(cluster)
    d = d.dropna().reset_index(drop=True)
    n = len(d)
    if n < 10 or d["x"].std() == 0 or d["y"].std() == 0:
        return dict(contrast=label, n=n, b=np.nan, se=np.nan, r=np.nan, rho=np.nan)
    a, b = d["x"].to_numpy(), d["y"].to_numpy()
    coef = np.polyfit(a, b, 1)
    beta = float(coef[0])
    r = float(np.corrcoef(a, b)[0, 1])
    sp = st.spearmanr(a, b)
    res = b - np.polyval(coef, a)
    sxx = float(np.sum((a - a.mean()) ** 2))
    se = float(np.sqrt(np.sum(res ** 2) / (n - 2) / sxx))
    o = dict(contrast=label, n=n, b=beta, se=se, t=beta / se if se else np.nan,
             p=float(2 * st.t.sf(abs(beta / se), n - 2)) if se else np.nan,
             r=r, rho=float(sp.statistic), p_spearman=float(sp.pvalue))
    if cluster is not None and d["g"].nunique() >= 10:          # bootstrap whole compounds, not rows
        ac = a - a.mean()
        meat = sum(float(np.sum(ac[i] * res[i])) ** 2
                   for i in (d.index[d["g"].to_numpy() == k].to_numpy() for k in pd.unique(d["g"])))
        se_cl = float(np.sqrt(meat) / sxx)
        nc = int(d["g"].nunique())
        o.update(n_clusters=nc, se_cluster=se_cl, t_cluster=beta / se_cl if se_cl else np.nan,
                 p_cluster=float(2 * st.t.sf(abs(beta / se_cl), nc - 1)) if se_cl else np.nan)
        # One RNG per contrast, so two contrasts' intervals are not drawn from the identical cluster picks -
        # but seeded through a STABLE hash. Python's hash() is salted per process for str (and for any tuple
        # containing one) unless PYTHONHASHSEED is set, so seeding from it makes the bootstrap irreproducible
        # across runs. An earlier version of this file did exactly that, and the committed intervals could
        # not be regenerated; blake2b is stable across processes and machines.
        key = "|".join(str(x) for x in (SEED, label, seed_tag, n, nc)).encode()
        rng = np.random.default_rng(int.from_bytes(hashlib.blake2b(key, digest_size=4).digest(), "big"))
        keys = d["g"].to_numpy()
        groups = [d.index[keys == k].to_numpy() for k in pd.unique(keys)]
        bs, rs = [], []
        for _ in range(NDRAW):
            pick = rng.integers(0, len(groups), len(groups))
            idx = np.concatenate([groups[i] for i in pick])
            s = d.loc[idx]
            if s["x"].std() == 0 or s["y"].std() == 0:
                continue
            bs.append(np.polyfit(s["x"], s["y"], 1)[0])
            rs.append(np.corrcoef(s["x"], s["y"])[0, 1])
        if bs:
            bs_a = np.asarray(bs)
            pb = float(2 * min(np.mean(bs_a <= 0), np.mean(bs_a >= 0)))
            o.update(b_lo=float(np.percentile(bs, 2.5)), b_hi=float(np.percentile(bs, 97.5)),
                     r_lo=float(np.percentile(rs, 2.5)), r_hi=float(np.percentile(rs, 97.5)),
                     p_boot=pb, n_boot_draws=len(bs),
                     # a percentile-inversion p cannot resolve below 2/draws; say so instead of printing 0
                     p_boot_floor="< %.4f" % (2.0 / len(bs)) if pb == 0 else "")
    return o


def bins(d, xcol, ycol, q, unit, xname, yname, extra=None, group=""):
    """Split on quantiles of xcol and summarise ycol in each bin. The headline shape of this file."""
    s = d[[xcol, ycol] + list(extra or [])].dropna(subset=[xcol, ycol]).copy()
    if len(s) < q * 3:
        return pd.DataFrame()
    try:
        s["_bin"] = pd.qcut(s[xcol].rank(method="first"), q, labels=False) + 1
    except ValueError:
        return pd.DataFrame()
    rows = []
    for k, g in s.groupby("_bin"):
        y = g[ycol].to_numpy(float)
        se = float(y.std(ddof=1) / np.sqrt(len(y))) if len(y) > 1 else np.nan
        row = dict(unit=unit, group=group, x=xname, y=yname, n_bins=q, bin=int(k),
                   bin_label="%d of %d" % (k, q), n=len(g),
                   x_lo=float(g[xcol].min()), x_median=float(g[xcol].median()), x_hi=float(g[xcol].max()),
                   y_mean=float(y.mean()), y_median=float(np.median(y)), y_sd=float(y.std(ddof=1)),
                   y_se=se, y_lo=float(y.mean() - 1.96 * se), y_hi=float(y.mean() + 1.96 * se))
        if "log2" in yname:
            # 2**(mean log2) is a GEOMETRIC mean of fold changes, not the mean fold change. Both are given
            # because they differ enough to matter: in the top MG53 decile, 1.017 against 1.035.
            row.update(y_geometric_fold=float(2 ** y.mean()),
                       y_geometric_fold_lo=float(2 ** (y.mean() - 1.96 * se)),
                       y_geometric_fold_hi=float(2 ** (y.mean() + 1.96 * se)))
            lin = 2 ** y
            sel = float(lin.std(ddof=1) / np.sqrt(len(lin))) if len(lin) > 1 else np.nan
            row.update(y_arithmetic_fold=float(lin.mean()),
                       y_arithmetic_fold_lo=float(lin.mean() - 1.96 * sel),
                       y_arithmetic_fold_hi=float(lin.mean() + 1.96 * sel))
        for c in (extra or []):
            row["%s_mean" % c] = float(pd.to_numeric(g[c], errors="coerce").mean())
        rows.append(row)
    t = pd.DataFrame(rows)
    top, bot = t.iloc[-1], t.iloc[0]
    t["y_mean_top_minus_bottom"] = top["y_mean"] - bot["y_mean"]
    t["monotone_spearman"] = float(st.spearmanr(t["bin"], t["y_mean"]).statistic)
    return t


# ----------------------------------------------------------------------------- the four units
def unit_baseline(res, out, models):
    """Unit 1. Untreated level of each gene, one row per cell line. Does a line with more MG53 have more MDM2?"""
    b = pd.read_csv(os.path.join(res, "downstream_p53/tables/b_baseline_per_line.csv"))
    b = b.rename(columns={"TRIM72_rel_reliable_plates": "mg53_base", "MDM2_rel_reliable_plates": "mdm2_base",
                          "CDKN1A_rel_reliable_plates": "cdkn1a_base",
                          "TRIM72_cpm_median_high_plates": "mg53_cpm"})
    t = []
    for grp, s in (("all lines", b), ("TP53-WT", b[b.tp53_group.eq("WT")]),
                   ("TP53-altered", b[b.tp53_group.eq("altered")])):
        t.append(bins(s, "mg53_base", "mdm2_base", 3 if grp != "all lines" else 4,
                      "1. baseline across cell lines", "MG53 baseline level (log2, panel-relative)",
                      "MDM2 baseline level (log2, panel-relative)", ["cdkn1a_base", "mg53_cpm"], grp))
        models.append(dict(unit="1. baseline across cell lines", group=grp, x="MG53 baseline level",
                           y="MDM2 baseline level", adjustment="none",
                           **fit(s["mg53_base"], s["mdm2_base"], label="across lines, untreated")))
    models.append(dict(unit="1. baseline across cell lines", group="all lines", x="MG53 baseline level",
                       y="CDKN1A baseline level", adjustment="none",
                       **fit(b["mg53_base"], b["cdkn1a_base"], label="across lines, untreated (contrast gene)")))
    return pd.concat([x for x in t if len(x)], ignore_index=True)


def unit_drugdose(res, out, models):
    """Unit 2. One row per drug-dose, lines pooled. Both LEVEL and CHANGE, raw / activity-adjusted /
    p53-adjusted / within-plate, each also split by TP53 group where the column exists."""
    d = pd.read_csv(os.path.join(res, "downstream_p53/tables/c_drugdose_table.csv"))
    tx = pd.read_csv(os.path.join(res, "export/TRIM72/TRIM72_per_drugdose.csv"))
    gz = os.path.join(res, "export/downstream/genes_per_drugdose.csv.gz")
    mg = pd.read_csv(gz, usecols=["gene", "drug_dose_row", "drug", "concentration_uM", "cpm_pooled",
                                  "r2_median_lines_mean", "plates"])
    mg = mg[mg.gene.isin([GENE, PARTNER])]
    wide = mg.pivot_table(index=["drug", "concentration_uM"], columns="gene",
                          values=["cpm_pooled", "r2_median_lines_mean"])
    wide.columns = ["%s_%s" % (a, b) for a, b in wide.columns]      # value_gene, e.g. cpm_pooled_MDM2
    wide = wide.reset_index().rename(columns={"concentration_uM": "conc"})
    tx = tx.rename(columns={"concentration_uM": "conc", "cpm_pooled": "MG53_cpm",
                            "r2_median_lines_mean": "MG53_r2"})
    d = d.merge(wide, on=["drug", "conc"], how="left").merge(
        tx[["drug", "conc", "MG53_cpm", "MG53_r2", "plates"]].rename(columns={"plates": "plates_tx"}),
        on=["drug", "conc"], how="left")
    d["mg53_log2fc"] = np.log2(pd.to_numeric(d["TRIM72_fold_change"], errors="coerce"))
    d["mdm2_log2fc"] = np.log2(pd.to_numeric(d["MDM2_fold_change"], errors="coerce"))
    d["cdkn1a_log2fc"] = np.log2(pd.to_numeric(d["CDKN1A_fold_change"], errors="coerce"))
    d["plate1"] = d["plates"].astype(str).str.split(",").str[0]
    # residual versions: strip transcriptome-wide activity, then p53 output, then plate
    d["mg53_z_act"], d["mdm2_z_act"] = resid_pair(d["TRIM72_z"], d["MDM2_z"], d[ACTIVITY])
    d["mg53_z_p53"], d["mdm2_z_p53"] = resid_pair(d["TRIM72_z"], d["MDM2_z"], d[["P53_ACTIVITY_z"]])
    d["mg53_z_both"], d["mdm2_z_both"] = resid_pair(d["TRIM72_z"], d["MDM2_z"],
                                                    d[ACTIVITY + ["P53_ACTIVITY_z"]])
    for c in ("TRIM72_z", "MDM2_z"):
        d[c + "_wp"] = d[c] - d.groupby("plate1")[c].transform("mean")
    U = "2. drug-dose, lines pooled"
    t = [
        bins(d, "MG53_cpm", "cpm_pooled_%s" % GENE, 10, U, "MG53 level (CPM, pooled over lines)",
             "MDM2 level (CPM, pooled over lines)", ["cpm_pooled_%s" % PARTNER, "MDM2_z"], "all"),
        bins(d, "TRIM72_z", "MDM2_z", 10, U, "MG53 change (z)", "MDM2 change (z)",
             ["mdm2_log2fc", "cdkn1a_log2fc", "P53_ACTIVITY_z", "atlas_n_sig_genes"], "all"),
        bins(d, "mg53_log2fc", "mdm2_log2fc", 10, U, "MG53 change (log2 fold change)",
             "MDM2 change (log2 fold change)", ["cdkn1a_log2fc", "MDM2_z"], "all"),
        bins(d, "mg53_z_act", "mdm2_z_act", 10, U, "MG53 change (z, activity-adjusted)",
             "MDM2 change (z, activity-adjusted)", [], "all"),
        bins(d, "mg53_z_both", "mdm2_z_both", 10, U, "MG53 change (z, activity + p53-adjusted)",
             "MDM2 change (z, activity + p53-adjusted)", [], "all"),
        bins(d, "TRIM72_z_wp", "MDM2_z_wp", 10, U, "MG53 change (z, within plate)",
             "MDM2 change (z, within plate)", [], "all"),
        bins(d, "MDM2_z", "TRIM72_z", 10, U, "MDM2 change (z)", "MG53 change (z)", [], "reverse direction"),
    ]
    for dose, s in d.groupby("conc"):
        t.append(bins(s, "TRIM72_z", "MDM2_z", 5, U, "MG53 change (z)", "MDM2 change (z)",
                      ["mdm2_log2fc"], "%g uM only" % dose))
    for nm, s in (("p53-activating only", d[pd.to_numeric(d["P53_ACTIVITY_z"], errors="coerce") >= 3]),
                  ("not p53-activating", d[pd.to_numeric(d["P53_ACTIVITY_z"], errors="coerce") < 3]),
                  ("DNA-damaging only", d[d["dna_damaging"] == True]),                       # noqa: E712
                  ("reliable plates only", d[d["unreliable_plate_only"] != True])):          # noqa: E712
        t.append(bins(s, "TRIM72_z", "MDM2_z", 5, U, "MG53 change (z)", "MDM2 change (z)",
                      ["mdm2_log2fc"], nm))
    pairs = [("TRIM72_z", "MDM2_z", "none", "all"), ("mg53_z_act", "mdm2_z_act", "activity", "all"),
             ("mg53_z_p53", "mdm2_z_p53", "P53_ACTIVITY_z", "all"),
             ("mg53_z_both", "mdm2_z_both", "activity + P53_ACTIVITY_z", "all"),
             ("TRIM72_z_wp", "MDM2_z_wp", "plate mean removed", "all"),
             ("MG53_cpm", "cpm_pooled_%s" % GENE, "none (levels, not change)", "all"),
             ("mg53_log2fc", "mdm2_log2fc", "none (log2 fold change)", "all"),
             ("TRIM72_z", "CDKN1A_z", "none", "contrast gene CDKN1A")]
    for x, y, adj, grp in pairs:
        models.append(dict(unit=U, group=grp, x=x, y=y, adjustment=adj,
                           **fit(d[x], d[y], d["drug"], "drug-dose level, %s" % adj)))
    for nm, s in (("p53-activating only", d[pd.to_numeric(d["P53_ACTIVITY_z"], errors="coerce") >= 3]),
                  ("not p53-activating", d[pd.to_numeric(d["P53_ACTIVITY_z"], errors="coerce") < 3])):
        models.append(dict(unit=U, group=nm, x="TRIM72_z", y="MDM2_z", adjustment="none",
                           **fit(s["TRIM72_z"], s["MDM2_z"], s["drug"], "drug-dose level, %s" % nm)))
    return d, pd.concat([x for x in t if len(x)], ignore_index=True)


def unit_perline(res, out, models):
    """Unit 3. One row per cell line x MG53-raising drug-dose. The only unit where both genes are resolved
    per line, so the only place the TP53-WT / altered split is a real split of the same contrast."""
    e = pd.read_csv(os.path.join(res, "downstream_p53/tables/a_per_line_effects.csv"))
    e["dd"] = e["drug"].astype(str) + " @ " + e["conc"].astype(str)
    for c in ("TRIM72_r2", "TRIM72_level", GENE, PARTNER, "P53_SCORE"):
        e[c] = pd.to_numeric(e[c], errors="coerce")
    # within drug-dose: remove each exposure's mean, so lines are compared only against lines on the same drug
    for c in ("TRIM72_r2", "TRIM72_level", GENE, PARTNER):
        e[c + "_wdd"] = e[c] - e.groupby("dd")[c].transform("mean")
    e["mg53_amp"], e["mdm2_amp"] = resid_pair(e["TRIM72_r2"], e[GENE],
                                              e[["bg_abs_r2", "atlas_beta", "atlas_A"]])
    e["mg53_p53"], e["mdm2_p53"] = resid_pair(e["TRIM72_r2"], e[GENE], e[["P53_SCORE"]])
    U = "3. cell line x drug-dose (18 MG53-raising exposures)"
    t, extra = [], [PARTNER, "P53_SCORE", "TRIM72_level"]
    for grp, s in (("all lines", e), ("TP53-WT", e[e.tp53_group.eq("WT")]),
                   ("TP53-altered", e[e.tp53_group.eq("altered")])):
        t += [bins(s, "TRIM72_r2", GENE, 5, U, "MG53 change (log2, r2)", "MDM2 change (log2)", extra, grp),
              bins(s, "TRIM72_r2_wdd", GENE + "_wdd", 5, U, "MG53 change (log2, within drug-dose)",
                   "MDM2 change (log2, within drug-dose)", [PARTNER + "_wdd"], grp),
              bins(s, "TRIM72_level", GENE, 5, U, "MG53 level (log2 CPM after treatment)",
                   "MDM2 change (log2)", extra, grp)]
        for x, y, adj in (("TRIM72_r2", GENE, "none"),
                          ("TRIM72_r2_wdd", GENE + "_wdd", "drug-dose mean removed"),
                          ("mg53_amp", "mdm2_amp", "bg|r2| + atlas beta + atlas A"),
                          ("mg53_p53", "mdm2_p53", "P53_SCORE"),
                          ("TRIM72_level", GENE, "none (level, not change)"),
                          ("TRIM72_r2", PARTNER, "none (contrast gene CDKN1A)")):
            models.append(dict(unit=U, group=grp, x=x, y=y, adjustment=adj,
                               **fit(s[x], s[y], s["cell_line_id"], "per line, %s" % adj)))
    return e, pd.concat([x for x in t if len(x)], ignore_index=True)


def unit_screen(res, models):
    """Unit 4. The genome-wide screen's own slope of MDM2 on MG53: per line x drug-dose, line and
    drug-dose fixed effects, 53,084 cells. Reported, not recomputed - per-gene per-line values are not in
    the export. Every covariate set is carried so the sign can be checked for robustness."""
    g_all = pd.read_csv(os.path.join(res, "genome_wide/tables/c_screen_genes.csv.gz"), low_memory=False)
    g = g_all[g_all.symbol.isin([GENE, PARTNER])].set_index("symbol")
    rows = []
    sets = [("gw (primary)", "b_common", "p_common"), ("gw_all", "b_common_gw_all", "p_common_gw_all"),
            ("gw_pc", "b_common_gw_pc", "p_common_gw_pc"),
            ("curated_cycle", "b_common_curated_cycle", "p_common_curated_cycle"),
            ("none", "b_common_none", "p_common_none"),
            ("gw_rt (readthrough-corrected)", "b_common_gw_rt", "p_common_gw_rt")]
    for sym in (GENE, PARTNER):
        if sym not in g.index:
            continue
        r = g.loc[sym]
        for nm, bc, pc in sets:
            b = float(r[bc])
            rows.append(dict(gene=sym, arm="common slope, all 47 lines", covariate_set=nm, b=b,
                             pct_per_doubling_measured=100 * (2 ** b - 1),
                             pct_per_doubling_true=100 * (2 ** (b / REL) - 1), p=float(r[pc]),
                             se=float(r["se_common"]) if nm == "gw (primary)" else np.nan,
                             se_drug_clustered=float(r["se_common_drug"]) if nm == "gw (primary)" else np.nan,
                             q_bh=float(r["q_common"]) if nm == "gw (primary)" else np.nan,
                             q_exposure_shuffle=float(r["q_xperm_common"]) if nm == "gw (primary)" else np.nan))
        for arm, bk, sek, tk, pk in (("TP53-WT lines only (17)", "b_WT", "se_WT", "t_WT", "p_WT"),
                                     ("TP53-altered lines only (30)", "b_alt", "se_alt", "t_alt", "p_alt"),
                                     ("WT minus altered", "diff", "se_diff", "t_diff", "p_diff")):
            b = float(r[bk])
            rows.append(dict(gene=sym, arm=arm, covariate_set="gw (primary)", b=b,
                             pct_per_doubling_measured=100 * (2 ** b - 1),
                             pct_per_doubling_true=100 * (2 ** (b / REL) - 1),
                             se=float(r[sek]), t=float(r[tk]), p=float(r[pk]),
                             q_bh=float(r["q_diff"]) if bk == "diff" else np.nan,
                             q_label_permutation=float(r["q_label_diff"]) if bk == "diff" else np.nan))
        n_tested = int((g_all["tested"] == True).sum())                                  # noqa: E712
        tcrit = float(st.t.isf(0.1 / n_tested / 2, float(r["df"])))
        # The run supplies TWO standard errors and they disagree about how marginal this gene is, so both
        # thresholds are given rather than the one that suits the argument.
        for lab, sek in (("line-clustered se_common", "se_common"),
                         ("drug-clustered se_common_drug", "se_common_drug")):
            se = float(r[sek])
            rows.append(dict(gene=sym, arm="lone-discovery threshold at q < 0.1 (%s)" % lab,
                             covariate_set="gw (primary)", b=tcrit * se, t=tcrit, se=se,
                             p=float(2 * st.t.sf(abs(float(r["b_common"]) / se), float(r["df"]))),
                             note="|b| this large would be needed to clear q < 0.1 with no other gene among"
                                  " the %d tested; the slope is %.2fx under it. BH draws its power from the"
                                  " mass of genome-wide signal, which the run's own calibration finds 4.44x"
                                  " inflated" % (n_tested, tcrit * se / abs(float(r["b_common"])))))
        # The disattenuation is not a point value: the run reports split-half reliability for MG53 under
        # several subsets, and MG53_p53_TABLES.md already flags that the ii_active variant (0.610) halves
        # the correction. Giving one number would pick the subset that maximises it.
        for rel, which in ((0.272, "i_all variant, lowest"), (REL, "i_all, FE + full - the primary"),
                           (0.425, "ii_active_no_plate3_13"), (0.610, "ii_active"), (0.705, "ii_trim72")):
            b = float(r["b_common"])
            rows.append(dict(gene=sym, arm="per doubling of TRUE MG53 at reliability %.3f (%s)" % (rel, which),
                             covariate_set="gw (primary)", b=b / rel,
                             pct_per_doubling_true=100 * (2 ** (b / rel) - 1),
                             note="classical errors-in-variables correction; 0.289 is already the"
                                  " Spearman-Brown full-data reliability, not a half-reliability"))
    t = pd.DataFrame(rows)
    models.append(dict(unit="4. genome-wide screen (reported)", group="all 47 lines", x="MG53 log2 (r2)",
                       y="MDM2 log2 (r2)", adjustment="line + drug-dose fixed effects, gw covariates",
                       contrast="within line, across drugs", n=int(g.loc[GENE, "n_rows"]),
                       b=float(g.loc[GENE, "b_common"]), se=float(g.loc[GENE, "se_common"]),
                       t=float(g.loc[GENE, "t_common"]), p=float(g.loc[GENE, "p_common"])))
    return t


def genotype_interaction(e, out):
    """Does the MG53 -> MDM2 slope differ between TP53-wild-type and TP53-altered lines, at the per-line unit?

    This is the test that decides whether the per-line unit supports a p53 route, and it has to be run twice.
    Fitted raw, the wild-type slope is six times the altered one and the interaction is highly significant -
    which looks exactly like p53 dependence. Fitted with each exposure's mean removed, so that lines are
    compared only against other lines given the same drug at the same dose, the interaction disappears.

    The reason is in the uncontrolled bins: across exposures, the ones that raise MG53 most are the ones that
    induce MDM2 least, and wild-type lines have far more MDM2 range to lose (their baseline runs 3.07x above
    the altered lines'). So the raw interaction is an exposure-level pattern magnified by the wild-type
    lines' larger dynamic range, not a per-line relationship. Both fits are reported; the within-exposure one
    is the one that answers the question.

    Model: MDM2 = a + b1*MG53 + b2*WT + b3*(MG53 x WT), cluster-robust on cell line.
    """
    rows = []
    for ycol, yname in ((GENE, "MDM2"), (PARTNER, "CDKN1A")):
        base = e[e["TRIM72_r2"].notna() & e[ycol].notna() & e["tp53_group"].isin(["WT", "altered"])].copy()
        for mode in ("raw", "within exposure"):
            s = base.copy()
            if mode == "within exposure":
                for c in ("TRIM72_r2", ycol):
                    s[c] = s[c] - s.groupby("dd")[c].transform("mean")
            s = s.reset_index(drop=True)
            wt = (s["tp53_group"] == "WT").to_numpy(float)
            x = s["TRIM72_r2"].to_numpy(float)
            X = np.column_stack([np.ones(len(s)), x, wt, x * wt])
            y = s[ycol].to_numpy(float)
            beta, *_ = np.linalg.lstsq(X, y, rcond=None)
            r = y - X @ beta
            XtXi = np.linalg.pinv(X.T @ X)
            meat = np.zeros((4, 4))
            for _, g in s.groupby("cell_line_id"):
                i = g.index.to_numpy()
                u = X[i].T @ r[i]
                meat += np.outer(u, u)
            se = np.sqrt(np.diag(XtXi @ meat @ XtXi))
            t = beta[3] / se[3] if se[3] else np.nan
            rows.append(dict(outcome=yname, fit=mode, n_rows=len(s), n_lines=int(s["cell_line_id"].nunique()),
                             b_altered=beta[1], se_altered=se[1], b_WT=beta[1] + beta[3],
                             interaction_WT_extra=beta[3], se_interaction=se[3], t_interaction=t,
                             p_interaction=float(2 * st.norm.sf(abs(t))) if np.isfinite(t) else np.nan,
                             ratio_WT_over_altered=(beta[1] + beta[3]) / beta[1] if beta[1] else np.nan,
                             answers_the_question=(mode == "within exposure")))
    t = pd.DataFrame(rows)
    t.to_csv(os.path.join(out, "mdm2_mg53_genotype_interaction.csv"), index=False)
    return t


def unit_singlecell(res, out):
    """Unit 5. Single cells inside one cell line and one well: MDM2 in the cells that have MG53 against the
    cells that do not.

    This is the best-controlled comparison in the data and the cleanest reading of "different levels of
    MG53". Cell line, drug, dose, plate and well are all held fixed by construction - the only thing that
    differs between the two groups of cells is whether MG53 was detected in them. The run fits a
    quasi-Poisson GLM per line (offset log UMIs; covariates log UMIs, S-phase and G2M module fractions, and a
    well indicator where two wells are pooled), then pools lines by DerSimonian-Laird random effects.

    Its negative control is the right one too: every non-p53 panel gene is run through the same fit, giving
    78 to 85 control genes per well set, and MDM2 is reported as a percentile among them. A rate ratio only
    means something if it sits outside that control distribution.

    The catch, and it is a real one: MG53 is detected in few cells at ~5 UMIs, so "detected" partly means
    "deeper cell". The UMI offset, the UMI covariate and the depth-stratified Mantel-Haenszel version
    (d_single_cell_mh_depth_strata) are what stand against that, and all three are carried here.
    """
    m = pd.read_csv(os.path.join(res, "downstream_p53/tables/d_single_cell_meta_main.csv"))
    s = pd.read_csv(os.path.join(res, "downstream_p53/tables/d_single_cell_mh_depth_strata.csv"))
    keep = ["wellset", "tp53_group", "outcome", "n_lines", "rate_ratio", "se", "p", "I2", "n_lines_positive",
            "percentile_among_controls", "n_controls", "q_bh_p53_outcomes",
            "median_line_log_rate_ratio_unadjusted", "WT_minus_altered_log_rate_ratio", "p_WT_minus_altered"]
    t = m[m.outcome.isin([GENE, PARTNER, "P53_SCORE"])][keep].copy()
    t = t.merge(s[["wellset", "tp53_group", "outcome", "median_line_rate_ratio", "n_lines_above_1",
                   "p_wilcoxon"]].rename(columns={"median_line_rate_ratio": "mh_depth_rate_ratio",
                                                  "p_wilcoxon": "mh_depth_p"}),
                on=["wellset", "tp53_group", "outcome"], how="left")
    t["pct_change_in_outcome"] = 100 * (t["rate_ratio"] - 1)
    t["control_percentile_verdict"] = np.where(
        t["percentile_among_controls"].between(5, 95), "inside the control-gene distribution",
        "outside the control-gene distribution")
    t = t.sort_values(["outcome", "wellset", "tp53_group"])
    t.to_csv(os.path.join(out, "mdm2_mg53_single_cell.csv"), index=False)
    return t


# ----------------------------------------------------------------------------- controls
def placebo_screen(res, out):
    """Is MDM2 unusual, or does every gene do this?

    TWO REFERENCE FAMILIES, and the difference between them is a trap this function exists to label.

      the 4,642 exported downstream genes    NOT a sample of genes. 4,500 of them are in the export because
                                             the genome-wide screen already called them significant against
                                             MG53 at q < 0.1 (c_calibration.csv: N_q01_common = 4500), and
                                             the other 142 are p53-program members selected with the TP53
                                             labels. MDM2 is itself one of the 4,500. So a percentile here
                                             is a rank WITHIN THE DISCOVERY SET, not among genes at large,
                                             and the family is shifted toward MG53 association by
                                             construction - which is why its median Spearman is +0.25 on
                                             level and +0.05 on change rather than 0.
      the 16,642 tested genes                The run's own co-regulation columns (coreg_r_across_dd_*) cover
                                             every tested gene, selected for nothing. This is the honest
                                             reference family, and it is the one to read first. Its cost is
                                             that it is the run's Pearson r on z across drug-doses rather
                                             than a statistic recomputed here.

    Each family is reported with its selection stated in the `family` column. Within the first, two
    quantities: pooled CPM (LEVEL) and corrected log2 fold change (CHANGE). The LEVEL one needs the plate
    decomposition in level_by_plate() to be read at all.
    """
    gz = os.path.join(res, "export/downstream/genes_per_drugdose.csv.gz")
    mg = pd.read_csv(gz, usecols=["gene", "drug_dose_row", "cpm_pooled", "r2_median_lines_mean"])
    tx = pd.read_csv(os.path.join(res, "export/TRIM72/TRIM72_per_drugdose.csv"),
                     usecols=["drug_dose_row", "cpm_pooled", "r2_median_lines_mean"])
    rows = []
    for col, what in (("cpm_pooled", "LEVEL (pooled CPM)"), ("r2_median_lines_mean", "CHANGE (corrected log2)")):
        piv = mg.pivot(index="gene", columns="drug_dose_row", values=col)
        x = tx.set_index("drug_dose_row")[col].reindex(piv.columns)
        ok = x.notna().to_numpy()
        X = piv.to_numpy(float)[:, ok]
        xv = x.to_numpy(float)[ok]
        # rank once per row; genes with any missing drug-dose are dropped from the distribution
        keep = ~np.isnan(X).any(axis=1)
        Xk = X[keep]
        rr = np.apply_along_axis(st.rankdata, 1, Xk)
        xr = st.rankdata(xv)
        rr = rr - rr.mean(axis=1, keepdims=True)
        xr = xr - xr.mean()
        rho = (rr @ xr) / np.sqrt((rr ** 2).sum(axis=1) * (xr ** 2).sum())
        Xc = Xk - Xk.mean(axis=1, keepdims=True)
        xc = xv - xv.mean()
        r = (Xc @ xc) / np.sqrt((Xc ** 2).sum(axis=1) * (xc ** 2).sum())
        genes = piv.index.to_numpy()[keep]
        s = pd.DataFrame(dict(gene=genes, rho=rho, r=r))
        for sym in (GENE, PARTNER):
            if sym not in set(genes):
                continue
            v = s[s.gene == sym].iloc[0]
            rows.append(dict(gene=sym, quantity=what, n_genes_in_null=len(s), n_drugdoses=int(ok.sum()),
                             family="the exported downstream set: 4,500 of these genes were SELECTED at"
                                    " q < 0.1 against MG53, so this is a rank within the discovery set",
                             rho=float(v["rho"]), r=float(v["r"]),
                             rho_percentile_among_genes=float((s["rho"] < v["rho"]).mean()),
                             r_percentile_among_genes=float((s["r"] < v["r"]).mean()),
                             all_gene_rho_median=float(s["rho"].median()),
                             all_gene_rho_q05=float(s["rho"].quantile(0.05)),
                             all_gene_rho_q95=float(s["rho"].quantile(0.95)),
                             all_gene_frac_rho_negative=float((s["rho"] < 0).mean()),
                             verdict="middle of this family" if 0.05 <= float((s["rho"] < v["rho"]).mean())
                                     <= 0.95 else "in this family's tail"))
        s.assign(quantity=what).to_csv(os.path.join(
            out, "mdm2_mg53_allgene_null_%s.csv" % col), index=False)
    # The unselected family: the run's own co-regulation columns over every tested gene. Read this one first.
    g = pd.read_csv(os.path.join(res, "genome_wide/tables/c_screen_genes.csv.gz"), low_memory=False,
                    usecols=["symbol", "tested", "coreg_r_across_dd_raw", "coreg_r_across_dd_minus_3pc"])
    for col, what in (("coreg_r_across_dd_raw", "co-regulation r across drug-doses, raw"),
                      ("coreg_r_across_dd_minus_3pc", "co-regulation r across drug-doses, 3 PCs removed")):
        s = g[["symbol", col]].dropna()
        for sym in (GENE, PARTNER):
            if sym not in set(s["symbol"]):
                continue
            v = float(s.loc[s.symbol == sym, col].iloc[0])
            rows.append(dict(gene=sym, quantity=what, n_genes_in_null=len(s), r=v,
                             family="every tested gene, selected for nothing - the honest reference family",
                             r_percentile_among_genes=float((s[col] < v).mean()),
                             all_gene_rho_median=float(s[col].median()),
                             all_gene_rho_q05=float(s[col].quantile(0.05)),
                             all_gene_rho_q95=float(s[col].quantile(0.95)),
                             verdict="middle of this family" if 0.05 <= float((s[col] < v).mean()) <= 0.95
                                     else "in this family's tail"))
    t = pd.DataFrame(rows)
    t.to_csv(os.path.join(out, "mdm2_mg53_allgene_null.csv"), index=False)
    return t


def level_by_plate(res, out, models):
    """Split the LEVEL comparison into its between-plate and within-plate parts, because MG53 carries a
    3.12 log2 plate-batch gap - the largest of 16,656 genes - and plates differ in depth and composition.

    All but one drug-dose lives on one or two plates (1,030 on one, 101 on two; Adagrasib at 0.05 uM is on
    13), so a correlation computed across all 1,132 of them is partly
    a correlation across plates. If MG53's plate medians run 16x while MDM2's run the other way, an
    across-plate correlation appears with no regulation in it at all. The within-plate version is the one
    that can mean something.
    """
    tx = pd.read_csv(os.path.join(res, "export/TRIM72/TRIM72_per_drugdose.csv"))
    mg = pd.read_csv(os.path.join(res, "export/downstream/genes_per_drugdose.csv.gz"),
                     usecols=["gene", "drug_dose_row", "cpm_pooled"])
    d = tx[["drug_dose_row", "drug", "cpm_pooled", "plates"]].rename(columns={"cpm_pooled": "mg53_cpm"})
    for sym in (GENE, PARTNER):
        d = d.merge(mg[mg.gene == sym][["drug_dose_row", "cpm_pooled"]].rename(
            columns={"cpm_pooled": "%s_cpm" % sym}), on="drug_dose_row", how="left")
    d["plate1"] = d["plates"].astype(str).str.split(",").str[0]
    rows = []
    for p, s in d.groupby("plate1"):
        rows.append(dict(plate=p, n_drugdoses=len(s), mg53_cpm_median=float(s["mg53_cpm"].median()),
                         mdm2_cpm_median=float(s["%s_cpm" % GENE].median()),
                         cdkn1a_cpm_median=float(s["%s_cpm" % PARTNER].median()),
                         rho_within_plate=float(st.spearmanr(s["mg53_cpm"], s["%s_cpm" % GENE]).statistic)
                         if len(s) > 5 else np.nan))
    t = pd.DataFrame(rows).sort_values("mg53_cpm_median")
    pm = t.dropna(subset=["rho_within_plate"])
    for c in ("mg53_cpm", "%s_cpm" % GENE):
        d[c + "_wp"] = d[c] - d.groupby("plate1")[c].transform("median")
    overall = float(st.spearmanr(d["mg53_cpm"], d["%s_cpm" % GENE]).statistic)
    t["rho_all_drugdoses"] = overall
    t["rho_between_plate_medians"] = float(st.spearmanr(t["mg53_cpm_median"], t["mdm2_cpm_median"]).statistic)
    t["rho_within_plate_pooled"] = float(st.spearmanr(d["mg53_cpm_wp"], d["%s_cpm_wp" % GENE]).statistic)
    t["mean_of_per_plate_rho"] = float(pm["rho_within_plate"].mean())
    t["n_plates_rho_negative"] = int((pm["rho_within_plate"] < 0).sum())
    t["mg53_plate_median_range_fold"] = float(t["mg53_cpm_median"].max() / t["mg53_cpm_median"].min())
    # Robustness to the one-plate-per-exposure convention above. Assigning each exposure to plates[0] leaves
    # plate6 holding a single exposure, so its "median" is one number; these two variants fix that.
    ex = d.assign(plate=d["plates"].astype(str).str.split(",")).explode("plate")
    pe = ex.groupby("plate").agg(mg=("mg53_cpm", "median"), md=("%s_cpm" % GENE, "median"))
    t["rho_between_plate_medians_full_membership"] = float(st.spearmanr(pe["mg"], pe["md"]).statistic)
    for c in ("mg53_cpm", "%s_cpm" % GENE):
        ex[c + "_wp"] = ex[c] - ex.groupby("plate")[c].transform("median")
    t["rho_within_plate_full_membership"] = float(
        st.spearmanr(ex["mg53_cpm_wp"], ex["%s_cpm_wp" % GENE]).statistic)
    drop6 = t[t["n_drugdoses"] > 5]
    t["rho_between_plate_medians_excl_plate6"] = float(
        st.spearmanr(drop6["mg53_cpm_median"], drop6["mdm2_cpm_median"]).statistic)
    t.to_csv(os.path.join(out, "mdm2_mg53_cpm_by_plate.csv"), index=False)
    U = "2. drug-dose, lines pooled"
    models.append(dict(unit=U, group="LEVEL, all drug-doses", x="MG53 CPM", y="MDM2 CPM",
                       adjustment="none", contrast="across plates and within", n=len(d), rho=overall))
    models.append(dict(unit=U, group="LEVEL, within plate", x="MG53 CPM", y="MDM2 CPM",
                       adjustment="plate median removed", contrast="within plate only", n=len(d),
                       rho=float(st.spearmanr(d["mg53_cpm_wp"], d["%s_cpm_wp" % GENE]).statistic)))
    models.append(dict(unit=U, group="LEVEL, between plates", x="MG53 CPM (plate median)",
                       y="MDM2 CPM (plate median)", adjustment="none", contrast="plate medians only",
                       n=len(t), rho=float(st.spearmanr(t["mg53_cpm_median"], t["mdm2_cpm_median"]).statistic)))
    return t


def per_exposure_rho(e, out):
    """Within one exposure, across the cell lines: do the lines that raise MG53 most show least MDM2?

    This is the pipeline's own statistic (a_pooled_over_drugdoses): a Spearman per drug-dose over the lines
    in that group, then the mean over drug-doses. It is kept separate from the pooled within-drug-dose fit
    because mean-of-correlations and pooled-residual-slope are different estimators and here they disagree,
    which is itself worth seeing.

    Two nulls, and the difference between them is the whole question:

      per-exposure shuffle    MDM2 permuted independently inside each exposure. Holds the exposure set, the
                              line count and both marginal distributions fixed. But it also destroys the
                              fact that the SAME 17 or 30 lines appear in all 18 exposures, so if a line
                              simply tends to run high in MG53 and low in MDM2 as a standing property, the
                              real statistic keeps that and the null throws it away. The p is then too
                              small, and this is the null the pipeline reports.
      line-label shuffle      ONE permutation of the line labels, applied to every exposure at once. Each
                              line's whole MDM2 profile travels together and is attached to a different
                              line's MG53 profile. Line-level structure survives in the null, so what is
                              tested is the thing actually claimed: that within an exposure, the lines that
                              raise MG53 more are the ones showing less MDM2. With 17 lines the permutation
                              space is large but the effective sample is 17, not 306.
    """
    rng = np.random.default_rng(SEED)
    rows = []
    for grp, s in (("all lines", e), ("TP53-WT", e[e.tp53_group.eq("WT")]),
                   ("TP53-altered", e[e.tp53_group.eq("altered")])):
        for xcol, yc, nm in (("TRIM72_r2", GENE, "MG53 change"), ("TRIM72_level", GENE, "MG53 level"),
                             ("TRIM72_r2", PARTNER, "MG53 change (contrast gene CDKN1A)")):
            per, obs = [], []
            for dd, g in s.groupby("dd"):
                v = g[[xcol, yc, "cell_line_id"]].dropna()
                if len(v) < 6:
                    continue
                per.append(float(st.spearmanr(v[xcol], v[yc]).statistic))
                obs.append(v)
            if len(per) < 3:
                continue
            mean = float(np.mean(per))
            draws = []
            for _ in range(NDRAW):
                vals = [float(st.spearmanr(v[xcol], rng.permutation(v[yc].to_numpy())).statistic)
                        for v in obs]
                draws.append(np.mean(vals))
            draws = np.asarray(draws)
            # line-label shuffle: one relabelling of cell lines, reused across every exposure
            lines = pd.unique(s["cell_line_id"])
            ldraws = []
            for _ in range(NDRAW):
                mp = dict(zip(lines, rng.permutation(lines)))
                vals = []
                for v in obs:
                    y = v.set_index("cell_line_id")[yc]
                    yp = pd.Series([y.get(mp[c], np.nan) for c in v["cell_line_id"]]).to_numpy(float)
                    ok = ~np.isnan(yp)
                    if ok.sum() >= 6:
                        vals.append(float(st.spearmanr(v[xcol].to_numpy()[ok], yp[ok]).statistic))
                if vals:
                    ldraws.append(np.mean(vals))
            ldraws = np.asarray(ldraws)
            rows.append(dict(group=grp, x=nm, y=yc, n_drugdoses=len(per),
                             n_lines_median=int(np.median([len(v) for v in obs])),
                             mean_rho=mean, n_negative=int(sum(p < 0 for p in per)),
                             min_rho=float(min(per)), max_rho=float(max(per)),
                             p_per_exposure_shuffle=float((np.abs(draws) >= abs(mean)).mean()),
                             null_sd_per_exposure=float(draws.std()),
                             p_line_label_shuffle=float((np.abs(ldraws) >= abs(mean)).mean())
                             if len(ldraws) else np.nan,
                             null_sd_line_label=float(ldraws.std()) if len(ldraws) else np.nan,
                             n_permutations=NDRAW))
    t = pd.DataFrame(rows)
    t.to_csv(os.path.join(out, "mdm2_mg53_per_exposure_rho.csv"), index=False)
    return t


# ----------------------------------------------------------------------------- joint table and extremes
def crosstab(d, out):
    """How the two genes' changes co-occur: counts in each MG53 x MDM2 quintile cell, against independence."""
    s = d[["TRIM72_z", "MDM2_z"]].dropna()
    s["xq"] = pd.qcut(s["TRIM72_z"].rank(method="first"), 5, labels=False) + 1
    s["yq"] = pd.qcut(s["MDM2_z"].rank(method="first"), 5, labels=False) + 1
    obs = pd.crosstab(s["xq"], s["yq"])
    chi = st.chi2_contingency(obs.to_numpy())
    rows = []
    for i in obs.index:
        for j in obs.columns:
            exp = obs.loc[i].sum() * obs[j].sum() / obs.to_numpy().sum()
            rows.append(dict(mg53_quintile=int(i), mdm2_quintile=int(j), n=int(obs.loc[i, j]),
                             n_expected_if_independent=round(float(exp), 1),
                             ratio=round(float(obs.loc[i, j] / exp), 3)))
    t = pd.DataFrame(rows)
    t["chi2"] = round(float(chi.statistic), 2)
    t["chi2_p"] = float(chi.pvalue)
    t["n_total"] = int(obs.to_numpy().sum())
    t.to_csv(os.path.join(out, "mdm2_mg53_crosstab.csv"), index=False)
    return t


def extremes(d, out, k=12):
    """Named exposures at both ends of MG53, with MDM2 beside them. Immune to how the bins were drawn."""
    cols = ["drug", "conc", "TRIM72_fold_change", "TRIM72_z", "MDM2_fold_change", "MDM2_z",
            "CDKN1A_fold_change", "P53_ACTIVITY_z", "atlas_n_sig_genes", "cells_log2_vs_plate", "plates",
            "category", "moa_fine", "targets", "flags"]
    s = d[cols].dropna(subset=["TRIM72_z", "MDM2_z"])
    out_rows = []
    # Ranked by fold change, and separately by z, because they disagree about which exposures are extreme
    # and a table sorted by one while displaying the other reads as non-monotone. n_distinct_compounds is
    # carried because the same compound appears at several doses: these are not independent chances.
    for by in ("TRIM72_fold_change", "TRIM72_z"):
        r = s.sort_values(by)
        for end, part in (("MG53 raised most", r.tail(k).iloc[::-1]), ("MG53 lowered most", r.head(k))):
            p = part.assign(end=end, ranked_by=by)
            p["n_distinct_compounds_in_this_block"] = p["drug"].nunique()
            out_rows.append(p)
    t = pd.concat(out_rows, ignore_index=True)
    t.to_csv(os.path.join(out, "mdm2_mg53_extremes.csv"), index=False)
    return t


def context(res, d, e):
    """What each gene is, before any comparison: how well measured, how strongly it responds."""
    g = pd.read_csv(os.path.join(res, "export/downstream/genes.csv"))
    g = g.set_index("gene")
    rows = []
    for sym, nm in ((GENE, "MDM2"), (PARTNER, "CDKN1A")):
        r = g.loc[sym] if sym in g.index else None
        rows.append(dict(gene=nm, median_line_cpm=float(r["median_line_cpm"]),
                         n_lines_expressing=int(r["n_lines_expressing"]),
                         in_p53_program=str(r["program"]), rank_in_program=r["program_rank_in_P"],
                         wt_fold_under_p53_activators=2 ** float(r["program_wt_mean_log2"]),
                         wt_minus_altered_fold=2 ** float(r["program_wt_minus_alt_log2"]),
                         drugdose_fold_min=float(d["%s_fold_change" % nm].min()),
                         drugdose_fold_max=float(d["%s_fold_change" % nm].max()),
                         note="p53 regulator (p53 induces it, it degrades p53)" if nm == GENE
                              else "p53 effector (arrest)"))
    rows.append(dict(gene="MG53 (TRIM72)", median_line_cpm=5.89, n_lines_expressing=50,
                     in_p53_program="not a member", rank_in_program=np.nan,
                     drugdose_fold_min=float(d["TRIM72_fold_change"].min()),
                     drugdose_fold_max=float(d["TRIM72_fold_change"].max()),
                     note="the exposure; 12.4%% zero profiles, split-half reliability %.3f" % REL))
    return pd.DataFrame(rows)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    here = os.path.dirname(os.path.abspath(__file__))
    ap.add_argument("--results", default=os.environ.get("MG53_RESULTS")
                    or os.path.expanduser("~/Tahoe-100M/mg53_p53"))
    ap.add_argument("--out", default=os.path.join(here, "tables"))
    a = ap.parse_args()
    res, out = (os.path.abspath(os.path.expanduser(p)) for p in (a.results, a.out))
    os.makedirs(out, exist_ok=True)

    models = []
    b1 = unit_baseline(res, out, models)
    d, b2 = unit_drugdose(res, out, models)
    e, b3 = unit_perline(res, out, models)
    scr = unit_screen(res, models)

    allbins = pd.concat([b1, b2, b3], ignore_index=True)
    allbins.to_csv(os.path.join(out, "mdm2_mg53_bins.csv"), index=False)
    mt = pd.DataFrame(models)
    mt.to_csv(os.path.join(out, "mdm2_mg53_models.csv"), index=False)
    scr.to_csv(os.path.join(out, "mdm2_mg53_screen.csv"), index=False)
    ct = crosstab(d, out)
    extremes(d, out)
    cx = context(res, d, e)
    cx.to_csv(os.path.join(out, "mdm2_mg53_context.csv"), index=False)
    pex = per_exposure_rho(e, out)
    plt = level_by_plate(res, out, models)
    mt = pd.DataFrame(models)                                  # level_by_plate appends to models
    mt.to_csv(os.path.join(out, "mdm2_mg53_models.csv"), index=False)
    sc = unit_singlecell(res, out)
    gi = genotype_interaction(e, out)
    nul = placebo_screen(res, out)

    pd.set_option("display.width", 200)
    print("\n===== what the two genes are")
    print(cx.to_string(index=False))
    print("\n===== headline bins: MG53 change (z) -> MDM2 change, drug-dose level, deciles")
    h = allbins[(allbins.x == "MG53 change (z)") & (allbins.group == "all") & (allbins.n_bins == 10)]
    print(h[["bin_label", "n", "x_median", "y_mean", "y_lo", "y_hi", "mdm2_log2fc_mean",
             "cdkn1a_log2fc_mean"]].to_string(index=False))
    print("\n===== MG53 level (CPM) -> MDM2 level (CPM), same unit")
    h = allbins[allbins.x.str.startswith("MG53 level (CPM")]
    print(h[["bin_label", "n", "x_median", "y_mean", "y_se"]].to_string(index=False))
    print("\n===== per line, within drug-dose")
    h = allbins[(allbins.unit.str.startswith("3.")) & (allbins.x.str.contains("within drug-dose"))]
    print(h[["group", "bin_label", "n", "x_median", "y_mean", "y_lo", "y_hi"]].to_string(index=False))
    print("\n===== slopes and correlations")
    cols = [c for c in ["unit", "group", "x", "y", "adjustment", "n", "n_clusters", "b", "b_lo", "b_hi",
                        "r", "r_lo", "r_hi", "rho", "p", "p_boot"] if c in mt.columns]
    print(mt[cols].to_string(index=False))
    print("\n===== the screen's own slope on MDM2 (reported)")
    print(scr[scr.gene == GENE][["arm", "covariate_set", "b", "pct_per_doubling_measured",
                                 "pct_per_doubling_true", "p"]].to_string(index=False))
    print("\n===== within one exposure, across lines (mean of per-drug-dose Spearman)")
    print(pex.to_string(index=False))
    print("\n===== LEVEL (CPM) split into between-plate and within-plate")
    print(plt[["plate", "n_drugdoses", "mg53_cpm_median", "mdm2_cpm_median",
               "rho_within_plate"]].to_string(index=False))
    print("all drug-doses rho %+.3f | between plate medians %+.3f | within plate pooled %+.3f | "
          "mean per-plate %+.3f, negative on %d plates | MG53 plate medians span %.1fx"
          % (plt["rho_all_drugdoses"].iloc[0], plt["rho_between_plate_medians"].iloc[0],
             plt["rho_within_plate_pooled"].iloc[0], plt["mean_of_per_plate_rho"].iloc[0],
             plt["n_plates_rho_negative"].iloc[0], plt["mg53_plate_median_range_fold"].iloc[0]))
    print("\n===== does the per-line slope differ by TP53 status? raw, then within exposure")
    print(gi[["outcome", "fit", "n_rows", "n_lines", "b_altered", "b_WT", "interaction_WT_extra",
              "se_interaction", "t_interaction", "p_interaction"]].to_string(index=False))
    print("The raw fit confounds WHICH EXPOSURE a line was in with the line itself; the within-exposure fit"
          " is the one that answers the question.")
    print("\n===== single cells: MDM2 in MG53-detected vs MG53-undetected cells of the same line and well")
    print(sc[sc.outcome.isin([GENE, PARTNER])][
        ["outcome", "wellset", "tp53_group", "n_lines", "rate_ratio", "p", "percentile_among_controls",
         "n_controls", "mh_depth_rate_ratio", "mh_depth_p"]].to_string(index=False))
    print("\n===== is MDM2 unusual? MDM2 against MG53 placed in the all-gene distribution")
    print(nul[["gene", "quantity", "n_genes_in_null", "rho", "r", "rho_percentile_among_genes",
               "r_percentile_among_genes", "all_gene_rho_median", "all_gene_rho_q05", "all_gene_rho_q95",
               "verdict"]].to_string(index=False))
    print("\n===== joint quintiles, chi2 p = %.4g" % ct["chi2_p"].iloc[0])
    print(ct.pivot(index="mg53_quintile", columns="mdm2_quintile", values="n").to_string())
    print("\nwrote 13 CSVs to %s" % out)


if __name__ == "__main__":
    main()
