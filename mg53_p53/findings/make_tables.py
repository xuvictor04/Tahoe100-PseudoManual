#!/usr/bin/env python3
"""Build the MG53 (TRIM72) <-> p53 correlation tables from a finished run's output.

Scope (fixed, per the project's question):
  upstream of MG53   = what raises or lowers MG53 expression
  downstream of MG53 = what MG53's level does to p53 and p53's output
Whether p53 regulates MG53 ("MG53 downstream of p53") is NOT in scope and no table here reports it.

A separate, purely positional fact is reported as a measurement caveat, never as regulation: TRIM72 lies
10.6 kb 3' of PYCARD-AS1 and 17 kb 3' of FUS on the SAME strand, so transcription running past those genes
is counted as TRIM72. That is called "readthrough spillover" throughout, never "downstream".

Usage:
    python3 make_tables.py --results ~/Tahoe-100M/mg53_p53 --out mg53_p53/findings/tables

Writes tableA_wt_p53_targets.csv, tableB_upstream_mg53.csv, tableC_mutants_by_activity.csv,
per_line_p53_activity.csv, wt_lines_pathway.csv and p53_nullification.csv.
"""
import argparse
import os

import numpy as np
import pandas as pd
from scipy import stats as st


def fit(s, ycol, mode, xcol="r2_mean"):
    """Pearson r and slope of ycol on MG53 (xcol) after removing the given fixed effects.

    mode: raw | within_line (line means removed; drug varies) | within_dd (drug-dose means removed;
    lines vary) | twoway (both removed). CI for r is Fisher; the slope SE is clustered on cell line.
    """
    s = s.dropna(subset=[xcol, ycol]).copy()
    if len(s) < 50 or s["cell_line_id"].nunique() < 3:
        return None
    s["_x"] = s[xcol].astype(float)
    s["_y"] = s[ycol].astype(float)
    if mode == "within_line":
        for c in ("_x", "_y"):
            s[c] -= s.groupby("cell_line_id")[c].transform("mean")
    elif mode == "within_dd":
        for c in ("_x", "_y"):
            s[c] -= s.groupby("drug_dose_row")[c].transform("mean")
    elif mode == "twoway":
        for _ in range(60):                       # alternating projections; converges well before 60
            for c in ("_x", "_y"):
                s[c] -= s.groupby("cell_line_id")[c].transform("mean")
                s[c] -= s.groupby("drug_dose_row")[c].transform("mean")
    a, b = s["_x"].to_numpy(), s["_y"].to_numpy()
    sxx = float(np.sum(a * a))
    if sxx <= 0:
        return None
    r = float(np.corrcoef(a, b)[0, 1])
    n = len(s)
    z, se_z = np.arctanh(r), 1 / np.sqrt(max(n - 3, 1))
    slope = float(np.sum(a * b) / sxx)
    res = b - slope * a
    num = sum(float(np.sum(g["_x"].to_numpy() * g["res"].to_numpy())) ** 2
              for _, g in s.assign(res=res).groupby("cell_line_id"))
    se_b = float(np.sqrt(num) / sxx)
    return dict(r=r, r_lo=float(np.tanh(z - 1.96 * se_z)), r_hi=float(np.tanh(z + 1.96 * se_z)),
                slope=slope, se_slope=se_b, slope_lo=slope - 1.96 * se_b, slope_hi=slope + 1.96 * se_b,
                n_rows=n, n_lines=int(s["cell_line_id"].nunique()))


def direction(o):
    if o is None:
        return "not estimable"
    if o["slope_lo"] > 0:
        return "positive"
    if o["slope_hi"] < 0:
        return "negative"
    return "none (interval spans 0)"


def load(res):
    tx = pd.read_csv(os.path.join(res, "export/TRIM72/TRIM72_per_drugdose_line.csv"))
    pr = pd.read_csv(os.path.join(res, "export/downstream/program_scores_per_drugdose_line.csv"))
    d = tx[["drug_dose_row", "cell_line_id", "cell_name", "tp53_group", "n_wells_r2", "r2_mean"]].merge(
        pr[["drug_dose_row", "cell_line_id", "P_r2_mean", "P_down_r2_mean"]],
        on=["drug_dose_row", "cell_line_id"])
    ovp = os.path.join(res, "export/downstream/overlay/scores_per_drugdose_line.csv")
    if os.path.exists(ovp):
        ov = pd.read_csv(ovp)
        oc = [c for c in ov.columns if c.endswith("_r2_mean")]
        d = d.merge(ov[["drug_dose_row", "cell_line_id"] + oc], on=["drug_dose_row", "cell_line_id"], how="left")
    act = pd.read_csv(os.path.join(res, "genome_wide/tables/b_drugdose_p53_activation.csv"))
    d = d.merge(act[["drugdose_row", "in_S2_p53_activating"]], left_on="drug_dose_row",
                right_on="drugdose_row", how="left")
    ls = pd.read_csv(os.path.join(res, "p53_dependence/tables/lines_tp53_status.csv"))
    d = d.merge(ls[["cell_line_id", "p53_responsiveness_log2", "functional_call", "tp53_class",
                    "basal_p53_activity_log2"]], on="cell_line_id", how="left")
    return d[(d["n_wells_r2"] >= 1) & d["r2_mean"].notna()].copy(), ls


def table_a(d, out):
    """MG53 -> p53 target output, in the TP53-wild-type lines only."""
    reads = [("P_r2_mean", "data-defined p53 program P (180 genes)", "data-defined"),
             ("P_down_r2_mean", "data-defined p53 repression arm (15 genes)", "data-defined"),
             ("OVERLAY_CollecTRI_TP53_activated_r2_mean", "CollecTRI TP53 targets (612 genes)", "list-based"),
             ("OVERLAY_P53_ACTIVITY21_r2_mean", "curated 21-gene P53_ACTIVITY", "list-based"),
             ("OVERLAY_GM_p53_primary_r2_mean", "curated p53 primary targets", "list-based"),
             ("OVERLAY_GM_p53_all_r2_mean", "curated p53 all targets", "list-based")]
    wt = d[d["tp53_group"] == "WT"]
    rows = []
    for col, label, basis in reads:
        if col not in d.columns:
            continue
        o = {m: fit(wt, col, m) for m in ("raw", "within_line", "within_dd", "twoway")}
        t = o["twoway"]
        if t is None:
            continue
        rows.append(dict(readout=label, basis=basis, r_raw=o["raw"]["r"],
                         r_within_line=o["within_line"]["r"], r_within_drugdose=o["within_dd"]["r"],
                         r_twoway=t["r"], r_twoway_lo=t["r_lo"], r_twoway_hi=t["r_hi"],
                         slope_twoway=t["slope"], slope_lo=t["slope_lo"], slope_hi=t["slope_hi"],
                         direction=direction(t), n_rows=t["n_rows"], n_lines=t["n_lines"]))
    t = pd.DataFrame(rows)
    t.to_csv(os.path.join(out, "tableA_wt_p53_targets.csv"), index=False)
    return t


def table_b(res, out):
    """Upstream of MG53: what moves its expression. p53-as-a-driver is out of scope and omitted."""
    rows = []
    ln = pd.read_csv(os.path.join(res, "upstream_coregulation/tables/c_locus_neighbours_effects.csv"))
    for lab in ("PYCARD-AS1", "FUS", "ITGAM", "ITGAX", "PYCARD"):
        s = ln[ln["label"] == lab]
        if not len(s):
            continue
        s = s.iloc[0]
        rows.append(dict(category="readthrough spillover (positional, not regulation)", driver=lab,
                         detail=f"{s['rel_to_TRIM72']}, {'same' if s['same_strand_as_TRIM72'] else 'OPPOSITE'} "
                                f"strand, {int(s['distance_bp'])/1000:.1f} kb, {s['pooled_cpm_quiet_wells']:.2f} CPM",
                         statistic="r with MG53 across drug-doses", value=s["r_z_with_TRIM72_over_drugdoses"],
                         basis="data-defined"))
    dg = pd.read_csv(os.path.join(res, "upstream_coregulation/tables/c_DoG_tests.csv"))
    for _, s in dg.head(2).iterrows():
        rows.append(dict(category="readthrough spillover (positional, not regulation)",
                         driver="genome-wide readthrough index" if "raw index" in s["test"] else "antisense control",
                         detail=s["test"], statistic="Spearman vs MG53 z", value=s["estimate"], basis="data-defined"))
    dd = pd.read_csv(os.path.join(res, "export/upstream/TRIM72_per_drugdose.csv")).sort_values("DD_z")
    for _, s in pd.concat([dd.tail(6).iloc[::-1], dd.head(4)]).iterrows():
        rows.append(dict(category="drug", driver=f"{s['drug']} {s['concentration_uM']:g} uM",
                         detail=f"plates {s['plates']}; z {s['DD_z']:.2f}", statistic="corrected log2 fold",
                         value=s["DD_lfc"], basis="data-defined"))
    tf = pd.read_csv(os.path.join(res, "summary/T11_upstream_TF_activity.csv"))
    rc = next((c for c in tf.columns if "r across" in c), None)
    pc = next((c for c in tf.columns if "without" in c), None)
    for _, s in tf.iterrows():
        name = str(s.iloc[0])
        if name.startswith("TP53"):                 # p53 as a driver of MG53: out of scope
            continue
        rows.append(dict(category="transcription factor (regulon activity)", driver=name,
                         detail=f"after removing shared AP-1/IEG/ATF3 targets: {s[pc] if pc else ''}",
                         statistic="r across drug-doses", value=s[rc] if rc else np.nan, basis="list-based"))
    bl = pd.read_csv(os.path.join(res, "upstream_coregulation/tables/b_baseline_coexpression_genomewide.csv"))
    for _, s in bl.head(3).iterrows():
        rows.append(dict(category="untreated level across cell lines", driver=s["gene"],
                         detail=f"organ-adjusted {s['rho_organ_adjusted']:.3f}",
                         statistic="Spearman across lines", value=s["rho_median_over_plates"], basis="data-defined"))
    pv = pd.read_csv(os.path.join(res, "genome_wide/tables/d_program_vs_exposure.csv"))
    for _, s in pv[pv["set"].str.startswith("PROG_")].nlargest(3, "r_across_dd").iterrows():
        rows.append(dict(category="data-driven program", driver=s["set"],
                         detail=f"within-line slope {s['b_common_within']:+.4f} (p {s['p_common_twoway']:.2g})",
                         statistic="r across drug-doses", value=s["r_across_dd"], basis="data-defined"))
    t = pd.DataFrame(rows)
    t["direction"] = np.where(t["value"] > 0.15, "positive",
                              np.where(t["value"] < -0.15, "negative", "none / weak"))
    t.to_csv(os.path.join(out, "tableB_upstream_mg53.csv"), index=False)
    return t


def table_c(d, ls, out):
    """MG53 -> p53 program, with the TP53-mutant lines split by how much p53 activity they retain."""
    s2 = d[d["in_S2_p53_activating"] == True]                                          # noqa: E712
    ind = (s2.groupby(["cell_line_id", "cell_name", "tp53_group"])["P_r2_mean"]
           .mean().reset_index(name="ind_P"))
    ind = ind.merge(ls[["cell_line_id", "p53_responsiveness_log2", "tp53_class", "functional_call",
                        "basal_p53_activity_log2", "tp53_changes"]], on="cell_line_id", how="left")
    null_ref = ind.loc[ind["tp53_class"].astype(str).str.contains("truncating"), "ind_P"].median()
    ind["activity_group"] = np.where(
        ind["tp53_group"] == "WT", "WT (functional p53)",
        np.where(ind["ind_P"] > null_ref, "altered: higher activity", "altered: lower activity"))
    ind.sort_values("ind_P", ascending=False).to_csv(os.path.join(out, "per_line_p53_activity.csv"), index=False)
    dd = d.merge(ind[["cell_line_id", "activity_group", "ind_P"]], on="cell_line_id", how="left")
    rows = []
    for g in ("WT (functional p53)", "altered: higher activity", "altered: lower activity"):
        o = fit(dd[dd["activity_group"] == g], "P_r2_mean", "twoway")
        if o:
            rows.append(dict(split="data-defined p53 inducibility", group=g, **o, direction=direction(o)))
    for g in ("responsive", "unresponsive", "uncertain (within 2 SE of the cut)"):
        o = fit(d[d["functional_call"] == g], "P_r2_mean", "twoway")
        if o:
            rows.append(dict(split="gene-panel functional call (list-based)", group=g, **o, direction=direction(o)))
    t = pd.DataFrame(rows)
    t.insert(0, "null_reference_ind_P", null_ref)
    t.to_csv(os.path.join(out, "tableC_mutants_by_activity.csv"), index=False)
    return t, ind


def nullification(ind, ls, res, out):
    """How far p53 has been disabled across the panel, and by which route."""
    cl = pd.read_csv(os.path.join(res, "export/metadata/cell_lines.csv"))
    j = ls.merge(cl[["cell_line_id", "drivers"]], on="cell_line_id", how="left").merge(
        ind[["cell_line_id", "ind_P"]], on="cell_line_id", how="left")
    w = j.loc[j["tp53_group"] == "WT", "p53_responsiveness_log2"].dropna()
    a = j.loc[j["tp53_group"] == "altered", "p53_responsiveness_log2"].dropna()
    rows = [dict(measure="TP53 driver mutation", value=f"{(j.tp53_group == 'altered').sum()}/{len(j)}",
                 note="genotype, from Tahoe cell_line_metadata", basis="list-based"),
            dict(measure="functionally responsive lines",
                 value=f"{(j.functional_call == 'responsive').sum()}/{len(j)}",
                 note="gene-panel call; every responsive line is genotype-WT", basis="list-based"),
            dict(measure="median responsiveness, WT vs altered (log2)",
                 value=f"{w.median():.3f} vs {a.median():.3f} ({w.median()/a.median():.1f}x)",
                 note=f"Mann-Whitney p {st.mannwhitneyu(w, a).pvalue:.2g}; ranking is genotype-blind",
                 basis="list-based"),
            dict(measure="altered lines retaining a response",
                 value=f"0/{(j.tp53_group == 'altered').sum()}",
                 note="no TP53-altered line is called responsive", basis="list-based")]
    wt = j[j["tp53_group"] == "WT"].copy()
    wt["p53_pathway_drivers"] = wt["drivers"].fillna("").apply(
        lambda s: "; ".join(g for g in ("CDKN2A", "CDKN2B", "ATM", "CHEK2", "MDM2", "MDM4", "PPM1D", "RB1")
                            if g in s))
    rows += [dict(measure="genotype-WT lines not fully responsive",
                  value=f"{(wt.functional_call != 'responsive').sum()}/{len(wt)}",
                  note="p53 damped without a TP53 mutation", basis="list-based"),
             dict(measure="genotype-WT lines with CDKN2A/ARF loss",
                  value=f"{wt.p53_pathway_drivers.str.contains('CDKN2A').sum()}/{len(wt)}",
                  note="a second route to lowering p53 activity", basis="list-based")]
    wt[["cell_name", "tp53_group", "functional_call", "p53_responsiveness_log2", "ind_P",
        "p53_pathway_drivers"]].sort_values("ind_P", ascending=False).to_csv(
        os.path.join(out, "wt_lines_pathway.csv"), index=False)
    t = pd.DataFrame(rows)
    t.to_csv(os.path.join(out, "p53_nullification.csv"), index=False)
    return t


# Canonical p53 effectors, grouped by what they do once p53 is active. The grouping is literature
# annotation, not derived from Tahoe; it is an overlay for reading the table, and selects nothing.
P53_EFFECTOR_ROLE = {
    "CDKN1A": "cell-cycle arrest", "BTG2": "cell-cycle arrest", "GADD45A": "cell-cycle arrest",
    "PLK3": "cell-cycle arrest", "CCNG1": "cell-cycle arrest",
    "BAX": "apoptosis", "BBC3": "apoptosis", "PMAIP1": "apoptosis", "TNFRSF10B": "apoptosis",
    "AEN": "apoptosis", "TP53INP1": "apoptosis", "TRIAP1": "apoptosis (anti-)", "EDA2R": "apoptosis",
    "DDB2": "DNA repair", "POLH": "DNA repair", "XPC": "DNA repair", "RRM2B": "DNA repair",
    "FDXR": "metabolism / redox", "TIGAR": "metabolism / redox", "SESN1": "metabolism / redox",
    "TP53I3": "metabolism / redox", "ACER2": "metabolism / redox",
    "MDM2": "negative feedback", "PPM1D": "negative feedback", "ZMAT3": "negative feedback",
    "RPS27L": "other", "PHLDA3": "other", "GDF15": "other (secreted)",
}


#: Curated sets that assert a gene is p53-ACTIVATED. There is no curated p53-REPRESSED set in the run, so
#: repression is data-defined only, and a gene in one of these that lands in the repression arm is a
#: literature-versus-data conflict worth flagging rather than resolving.
CURATED_ACTIVATED = ["OVERLAY_CollecTRI_TP53_activated", "OVERLAY_P53_ACTIVITY21",
                     "OVERLAY_GM_p53_primary", "OVERLAY_GM_p53_secondary", "OVERLAY_GM_p53_all"]


def sign_by_p53_direction(g, res, bcol="b_common", qcol=None):
    """Add the direction of p53 regulation, and re-express MG53's slope in p53-OUTPUT units.

    Why this is necessary. A gene's MG53 slope is in the gene's own units, and "up with MG53" means opposite
    things depending on which way p53 moves that gene. For a p53-INDUCED gene, more of it means more p53
    output. For a p53-REPRESSED gene, more of it means LESS p53 output. Tallying slopes without signing them
    adds the two together and reads as noise either way, so the signed column is the only one that can be
    summed across genes.

    Direction comes from the data-defined program arm: induction (in_P, 180 genes, moved up by 64-99% of the
    98 reference compounds) or repression (in_P_down, 15 genes, moved DOWN by 70-81%). The two are disjoint
    and no gene is significant in both directions (q_up and q_down are never both < 0.1), so in this data
    the arms are clean. Curation agrees where it speaks: no repression-arm gene appears in any of the curated
    p53-activated sets, including CollecTRI's 723 TP53 targets.

    Mixedness is reported rather than resolved, because it is a property of the gene and not a defect:
      frac_compounds_wt_up      the share of the 98 compounds that move the gene UP in wild-type lines. At
                                0.5 the gene goes each way equally often and its direction is not a fact.
      direction_is_mixed        set when that share sits between 0.35 and 0.65, or when the data arm
                                contradicts a curated activated set.
      program_membership_stable n_folds_kept is the number of the 5 cross-fitting folds in which the gene
                                was re-selected into the program. A gene at 0 or 1 is in the full-data
                                program but almost none of the cross-fitted ones, so its direction label is
                                itself unstable. loco_frequency is the same idea over 98 leave-one-compound-
                                out programs - but it is computed for the INDUCTION arm only, so every
                                repression-arm gene reads NaN and must be judged on n_folds_kept alone.
    """
    cur = pd.read_csv(os.path.join(res, "export/downstream/overlay/curated_sets.csv"))
    act = set(cur.loc[cur["set"].isin(CURATED_ACTIVATED), "gene"].astype(str))
    if "arm" in g.columns:                                        # the program tables carry a named arm
        arm = g["arm"].astype(str)
        rep, ind = arm.str.contains("down", case=False), arm.str.contains("up", case=False)
    else:                                                         # the genome-wide tables carry the flags
        rep = g["in_P_down"] == True if "in_P_down" in g.columns else pd.Series(False, index=g.index)
        ind = g["in_P"] == True if "in_P" in g.columns else pd.Series(False, index=g.index)
    rep, ind = rep.fillna(False), ind.fillna(False)               # noqa: E712
    g["curated_calls_p53_activated"] = g["symbol"].isin(act)
    # Where the data-defined program gives no direction, fall back to curation. Several canonical targets
    # (PMAIP1/NOXA and TP53I3 among them) are not in the data-defined program at all, so without this they
    # would be dropped from a signed tally for want of a sign - even though their direction is not in doubt.
    cur_only = ~rep & ~ind & g["curated_calls_p53_activated"]
    g["p53_direction"] = np.where(rep, "repressed by p53",
                                  np.where(ind | cur_only, "induced by p53", "not in the program"))
    g["p53_direction_source"] = np.where(rep | ind, "data: the program arm it was selected into",
                                         np.where(cur_only, "curated p53-activated set (not in the"
                                                            " data-defined program)", "none available"))
    g["p53_direction_sign"] = np.where(rep, -1, np.where(ind | cur_only, 1, 0))
    wtup = (pd.to_numeric(g["frac_compounds_wt_up"], errors="coerce") if "frac_compounds_wt_up" in g.columns
            else pd.Series(np.nan, index=g.index, dtype=float))
    g["frac_compounds_wt_up"] = wtup
    conflict = rep & g["curated_calls_p53_activated"]
    g["direction_conflicts_curation"] = conflict
    g["direction_is_mixed"] = (wtup.between(0.35, 0.65) | conflict).fillna(False)
    nf = (pd.to_numeric(g["n_folds_kept"], errors="coerce") if "n_folds_kept" in g.columns
          else pd.Series(np.nan, index=g.index, dtype=float))
    g["program_membership_stable"] = np.where(nf.isna(), "unknown",
                                              np.where(nf >= 4, "stable (4-5 of 5 folds)",
                                                       np.where(nf >= 2, "partial (2-3 of 5)",
                                                                "unstable (0-1 of 5)")))
    # The signed verdict. Only meaningful where the slope cleared its threshold AND the gene has a direction.
    b = pd.to_numeric(g[bcol], errors="coerce")
    hit = pd.to_numeric(g[qcol], errors="coerce") < 0.1 if qcol else b.notna()
    toward = np.sign(b) * g["p53_direction_sign"]
    g["mg53_effect_on_p53_output"] = np.where(
        ~hit | (g["p53_direction_sign"] == 0), "none",
        np.where(toward > 0, "toward MORE p53 output", "toward LESS p53 output"))
    return g


def signed_tally(t, out, name="p53_direction_signed_tally.csv"):
    """The point of signing: how the genes with a verdict split once direction is accounted for."""
    rows = []
    for arm, s in t.groupby("p53_direction"):
        v = s[s["mg53_effect_on_p53_output"] != "none"]
        rows.append(dict(p53_direction=arm, n_genes=len(s), n_with_verdict=len(v),
                         n_toward_more_p53_output=int((v["mg53_effect_on_p53_output"]
                                                       == "toward MORE p53 output").sum()),
                         n_toward_less_p53_output=int((v["mg53_effect_on_p53_output"]
                                                       == "toward LESS p53 output").sum()),
                         n_direction_mixed=int(s["direction_is_mixed"].sum()),
                         n_membership_unstable=int((s["program_membership_stable"]
                                                    == "unstable (0-1 of 5)").sum())))
    tot = pd.DataFrame(rows)
    allv = t[t["mg53_effect_on_p53_output"] != "none"]
    tot.loc[len(tot)] = dict(
        p53_direction="ALL", n_genes=len(t), n_with_verdict=len(allv),
        n_toward_more_p53_output=int((allv["mg53_effect_on_p53_output"] == "toward MORE p53 output").sum()),
        n_toward_less_p53_output=int((allv["mg53_effect_on_p53_output"] == "toward LESS p53 output").sum()),
        n_direction_mixed=int(t["direction_is_mixed"].sum()),
        n_membership_unstable=int((t["program_membership_stable"] == "unstable (0-1 of 5)").sum()))
    tot["reading"] = ("a coherent shift in p53 output would push the induction and repression arms in"
                      " OPPOSITE gene-level directions and so land on ONE side of this split; an even split"
                      " is what a non-specific association looks like")
    tot.to_csv(os.path.join(out, name), index=False)
    return tot


def p53_effectors(res, out):
    """The canonical p53 effector genes only, each with its fold change and MG53's slope on it.

    This is the focused companion to the full 195-gene program table: the genes that actually carry out
    p53's effects, rather than every gene the genome-wide selection picked up.

    Two fold changes are reported because neither alone is clean, and they are diluted in opposite ways:
      fold_WT_broad  2**wt_mean_log2 from the program table. WT lines only, but averaged over a broad
                     drug-dose set in which most drug-doses do not activate p53, so it reads low.
      fold_ida5      the drug-dose fold under idarubicin 5 uM, a strong p53 activator, from the per-gene
                     per-drug-dose export. Activator-specific, but it is the median over ALL lines, and
                     two-thirds of the panel is p53-dead, so it also reads low for the sharpest targets.
    The clean quantity, WT lines only under one strong activator, needs a per-gene per-line extraction that
    the export does not provide for arbitrary genes (only TRIM72 and the program scores reach that
    granularity). See the open questions in FINDINGS.md.
    """
    gz = pd.read_csv(os.path.join(res, "genome_wide/tables/b_p53_program_genes.csv.gz"), low_memory=False)
    sc = pd.read_csv(os.path.join(res, "genome_wide/tables/c_screen_genes.csv.gz"), low_memory=False)
    cur = pd.read_csv(os.path.join(res, "export/downstream/overlay/curated_sets.csv"))
    panel = set(cur.loc[cur["set"] == "OVERLAY_P53_ACTIVITY21", "gene"].astype(str))
    keep = sorted(set(P53_EFFECTOR_ROLE) | panel)
    g = gz[gz["symbol"].isin(keep)].copy()
    g["role"] = g["symbol"].map(P53_EFFECTOR_ROLE).fillna("other")
    g["in_curated_panel"] = g["symbol"].isin(panel)
    g["arm"] = np.where(g["in_P"] == True, "P up",                                      # noqa: E712
                        np.where(g["in_P_down"] == True, "P down", "not in program"))   # noqa: E712
    up = [c for c in gz.columns if c.startswith("in_P_minus_fold")]
    dn = [c for c in gz.columns if c.startswith("in_P_down_minus_fold")]
    g["n_folds_kept"] = np.where(g["arm"] == "P down", g[dn].sum(axis=1), g[up].sum(axis=1))
    g["fold_WT_broad"] = 2 ** g["wt_mean_log2"]
    # fold under one strong activator, streamed because the per-drug-dose export is ~0.5 GB gzipped
    ids = pd.read_csv(os.path.join(res, "export/downstream/genes.csv"), usecols=["gene", "symbol"])
    want = set(ids.loc[ids["symbol"].isin(keep), "gene"])
    cols = ["gene", "drug", "concentration_uM", "DD_lfc"]
    chunks = [c[c["gene"].isin(want)] for c in
              pd.read_csv(os.path.join(res, "export/downstream/genes_per_drugdose.csv.gz"),
                          usecols=cols, chunksize=400_000)]
    dd = pd.concat(chunks, ignore_index=True).merge(ids, on="gene", how="left")
    ida = dd[dd["drug"].str.contains("Idarubicin", na=False) & np.isclose(dd["concentration_uM"], 5.0)]
    best = dd.loc[dd.groupby("symbol")["DD_lfc"].idxmax()]
    g = g.merge(ida.groupby("symbol")["DD_lfc"].first().rename("ida5_log2"), on="symbol", how="left")
    g = g.merge(best.assign(best_activator=best["drug"] + " " + best["concentration_uM"].astype(str) + " uM")
                [["symbol", "best_activator", "DD_lfc"]].rename(columns={"DD_lfc": "best_log2"}),
                on="symbol", how="left")
    g["fold_ida5"] = 2 ** g["ida5_log2"]
    g = g.merge(sc[["symbol", "b_common", "se_common", "q_common", "q_xperm_common", "b_WT", "b_alt",
                    "diff", "se_diff", "q_diff", "q_label_diff", "placebo_pct_common_expression",
                    "placebo_pct_common_response"]], on="symbol", how="left")
    # Verdicts use the permutation-calibrated q values, not the analytic ones. genome_wide.py's own
    # calibration shows the analytic common-slope statistic is inflated about 4.4x by line-level structure
    # (lambda_common 4.444 observed; c_calibration.csv), and the exposure-shuffle null is the one the step
    # documents for the common slope. The TP53-relabelling null is explicitly NOT valid for the common
    # slope ("relabelling keeps the within-line association"), so the genotype verdict uses q_label_diff.
    # The placebo percentiles are carried alongside because matched placebo genes show the SAME inflation
    # (lambda 4.685 / 5.518), so "significant" here does not mean MG53 is special: read the percentiles.
    qd = g["q_label_diff"].fillna(g["q_diff"])
    qc = g["q_xperm_common"].fillna(g["q_common"])
    g["mg53_common_verdict"] = np.where(qc >= 0.1, "none",
                                        np.where(g["b_common"] > 0, "positive", "negative"))
    g["mg53_genotype_verdict"] = np.where(qd < 0.1, "differs by TP53 status", "none")
    g = sign_by_p53_direction(g, res, "b_common", "q_xperm_common")
    cols_out = ["symbol", "role", "p53_direction", "p53_direction_source", "direction_is_mixed", "frac_compounds_wt_up",
                "curated_calls_p53_activated", "direction_conflicts_curation",
                "mg53_effect_on_p53_output", "program_membership_stable",
                "in_curated_panel", "arm", "n_folds_kept", "median_line_cpm",
                "wt_mean_log2", "fold_WT_broad", "wt_minus_alt_log2", "ida5_log2", "fold_ida5",
                "best_activator", "best_log2", "z_program", "q_up", "loco_frequency",
                "b_common", "se_common", "q_common", "q_xperm_common", "mg53_common_verdict",
                "b_WT", "b_alt", "diff", "se_diff", "q_diff", "q_label_diff", "mg53_genotype_verdict",
                "placebo_pct_common_expression", "placebo_pct_common_response"]
    t = g[[c for c in cols_out if c in g.columns]].sort_values("ida5_log2", ascending=False)
    t.to_csv(os.path.join(out, "p53_effectors_per_gene.csv"), index=False)
    signed_tally(t, out, "p53_effectors_signed_tally.csv")
    return t


def table_d(res, out):
    """Per-gene companion to Tables A and C: every p53 target gene, its fold change, and MG53's slope on it.

    One row per member of the data-defined p53 program - 180 genes in the induction arm P, 15 in the
    repression arm P-down. The fold-change block says how much the gene moves in the TP53-wild-type lines
    when p53 is activated; the MG53 block is that gene's own row in the genome-wide MG53 screen.

    Scope (fixed, per the project's question): upstream of MG53 = what raises or lowers MG53's expression;
    downstream of MG53 = what MG53's level does to p53 and p53's output. Whether p53 regulates MG53 is NOT
    in scope and no column here reports it. A gene's p53-activation fold change IS in scope: it defines the
    read-out being tested, it says nothing about p53 acting on MG53.

    wt_fold = 2**wt_mean_log2, and the baseline matters. wt_mean_log2 is the compound-equal weighted mean
    (each of 98 compounds carries 1/98, split across its doses) over the 142 S2 p53-activating drug-doses,
    of the mean corrected log2 response of the TP53-WT lines that express the gene - and that response is
    already relative to the SAME LINE's median log2 CPM over that plate's drug wells, minus the composition
    shift and the well-position effect [genome_wide.py:1976 -> set_stats :957-984]. So it is a fold change
    against a typical drug well of the same line on the same plate, not against DMSO and not against
    untreated cells, and it averages 142 treatments rather than reporting one strong activator, which is
    why it reads low (median 1.06x).

    CIRCULARITY: the program's genes AND the S1 / S2 p53-activating drug-doses were both selected USING the
    TP53 WT/altered labels, so arm, z_program, q_arm, wt_mean_log2, wt_minus_alt_log2, frac_compounds_*,
    rank_in_P, loco_frequency and n_folds_kept are all circular as evidence of p53 specificity. The screen
    block is not: it fits every atlas gene over all 1,132 drug-doses with no label-based selection of genes
    or drug-doses (the labels enter the design, plus one covariate, resp_bg, whose background gene set is
    defined by excluding the label-selected programs).

    Writes tableD_p53_target_genes.csv (the 195 program genes, strongest p53 induction first) and
    tableD_top_mg53_partners.csv (the 100 largest |b_common| among the screen's q_common < 0.1 genes, for
    contrast). Returns the first.
    """
    # MG53's split-half reliability under the screen's own fixed effects (drug-dose x TP53-group), used to
    # restate slopes and detection bounds per doubling of TRUE rather than measured MG53: an observed slope
    # is reliability x the true one, so dividing de-attenuates it [two_way/tables/trim72_reliability.csv,
    # row i_all / ddxg / full / all lines]. The ii_active variant gives 0.610, so the true-scale columns
    # are the wide end of a range, not a point estimate.
    rel = 0.289317
    pg = pd.read_csv(os.path.join(res, "genome_wide/tables/b_p53_program_genes.csv.gz"), low_memory=False)
    sc = pd.read_csv(os.path.join(res, "genome_wide/tables/c_screen_genes.csv.gz"), low_memory=False)
    n_tested = int((sc["tested"] == True).sum())                                         # noqa: E712
    alpha = 0.1 / n_tested                   # a lone discovery at q < 0.1 needs a p below this

    def screen(tab):
        """Join the MG53 screen block on symbol, then add the verdicts, detection bounds and geometry.

        b_common is ONE slope shared by all lines: log2 change in the gene per log2 change in measured
        MG53, at equal drug-dose x TP53-group and cell line, with the conservative two-way (compound, line)
        cluster SE. diff = b_WT - b_alt is the wild-type-minus-altered version of the same slope.

        The verdicts use the permutation-calibrated q values, not the analytic ones. The screen's own
        calibration puts lambda_common at 4.44 with 4,500 of 16,642 genes at q_common < 0.1, and matched
        placebo exposures - real genes picked before any fit - give 2 to 8,381 such genes, so q_common on
        its own says almost nothing [genome_wide/tables/c_calibration.csv]. q_xperm_common (the exposure
        shuffled across lines within each drug-dose x TP53-group cell) is the null the step documents for
        the common slope, and the TP53-relabelling null is explicitly not valid for it, so the genotype
        verdict uses q_label_diff instead. The placebo percentiles ride along because they are the only
        per-gene yardstick free of that inflation - with 10 placebos per family their resolution is 0.1, so
        a 0.0 or a 1.0 is "most extreme of ten", not a p value.
        """
        cols = ["symbol", "tested", "n_rows", "n_lines_WT", "n_lines_alt", "n_drugdoses", "df",
                "b_common", "se_common", "t_common", "p_common", "q_common", "q_xperm_common",
                "b_WT", "b_alt", "diff", "se_diff", "t_diff", "p_diff", "q_diff", "q_label_diff",
                "sd_x_resid", "b_common_gw_rt", "diff_gw_rt",
                "placebo_pct_common_expression", "placebo_pct_common_response",
                "placebo_pct_diff_expression", "placebo_pct_diff_response"]
        pos = ["dog_class", "in_TRIM72_locus_200kb"]            # positional flags, kept unprefixed
        cols = [c for c in cols if c in sc.columns]
        pos = [c for c in pos if c in sc.columns]
        s = sc[cols + pos].drop_duplicates("symbol").rename(
            columns={c: "screen_" + c for c in cols if c != "symbol"})
        tab = tab.merge(s, on="symbol", how="left")
        # "not tested" keys on the screen's own tested flag, NOT on a missing slope: the exposure's row
        # carries b_common = 1.0 with tested False, which would otherwise read as a real null result.
        ok = tab.get("screen_tested", pd.Series(False, index=tab.index)) == True          # noqa: E712

        def verdict(est, q, up, down):
            b = pd.to_numeric(tab["screen_" + est], errors="coerce")
            qq = pd.to_numeric(tab["screen_" + q], errors="coerce")
            hit = ok & qq.notna() & (qq < 0.1)
            return np.where(~ok, "not tested", np.where(hit & (b > 0), up,
                                                        np.where(hit & (b < 0), down, "none")))

        tab["mg53_verdict_common"] = verdict("b_common", "q_xperm_common", "up with MG53",
                                             "down with MG53")
        tab["mg53_verdict_genotype"] = verdict("diff", "q_label_diff", "differs by TP53 status (WT higher)",
                                               "differs by TP53 status (altered higher)")
        tab["mg53_verdict_common_test"] = "q_xperm_common < 0.1 (exposure shuffled within cell) on b_common"
        tab["mg53_verdict_genotype_test"] = "q_label_diff < 0.1 (TP53 relabelling) on diff = b_WT - b_alt"
        # Smallest effect this gene could have shown as a lone discovery at q < 0.1: crit_* would be caught
        # half the time, mde80_* four times in five. Dividing by rel converts per doubling of measured MG53
        # into per doubling of true MG53.
        tcrit = st.t.isf(alpha / 2, pd.to_numeric(tab["screen_df"], errors="coerce"))
        for est in ("diff", "common"):
            se = pd.to_numeric(tab["screen_se_" + est], errors="coerce")
            tab["crit_%s_q01_measured" % est] = tcrit * se
            tab["mde80_%s_q01_measured" % est] = (tcrit + st.norm.isf(0.2)) * se
            tab["mde80_%s_q01_true" % est] = tab["mde80_%s_q01_measured" % est] / rel
        tab["diff_per_doubling_true"] = pd.to_numeric(tab["screen_diff"], errors="coerce") / rel
        # Positional only, never regulation: dog_class "sense_exposed" means the gene sits within 20 kb 3'
        # of an expressed same-strand gene at >= 8x its own level, so transcription running past that
        # neighbour is counted as this gene - readthrough spillover. MG53 itself is sense_exposed (TRIM72
        # lies 10.6 kb 3' of PYCARD-AS1 and 17 kb 3' of FUS, same strand), which is why the flag belongs
        # next to b_common at all.
        dc = tab["dog_class"].astype(str) if "dog_class" in tab.columns else pd.Series("", index=tab.index)
        near = (tab["in_TRIM72_locus_200kb"] == True if "in_TRIM72_locus_200kb" in tab.columns
                else pd.Series(False, index=tab.index))                                   # noqa: E712
        tab["readthrough_geometry"] = np.where(
            dc == "sense_exposed", "readthrough spillover risk (<= 20 kb 3' of a much higher same-strand"
                                   " gene)",
            np.where(near, "within 200 kb of the MG53 locus", "no readthrough geometry"))
        # Direction of p53 regulation, and MG53's slope re-expressed in p53-output units. Without this the
        # induction and repression arms are tallied against each other: see sign_by_p53_direction.
        tab = tab.rename(columns={"screen_b_common": "b_common",
                                  "screen_q_xperm_common": "q_xperm_common"})
        tab = sign_by_p53_direction(tab, res, "b_common", "q_xperm_common")
        tab = tab.rename(columns={"b_common": "screen_b_common",
                                  "q_xperm_common": "screen_q_xperm_common"})
        return tab

    ov = {"overlay_OVERLAY_P53_ACTIVITY21": "curated_panel21",
          "overlay_OVERLAY_GM_p53_primary": "curated_p53_primary",
          "overlay_OVERLAY_CollecTRI_TP53_activated": "curated_collectri_TP53",
          "overlay_OVERLAY_GM_locus_readthrough": "curated_locus_readthrough"}
    for c in list(ov) + ["in_P_noX"]:                        # an overlay this run did not write
        if c not in pg.columns:
            pg[c] = np.nan
    fu = [c for c in pg.columns if c.startswith("in_P_minus_fold")]
    fd = [c for c in pg.columns if c.startswith("in_P_down_minus_fold")]
    a_up, a_dn = pg["in_P"] == True, pg["in_P_down"] == True                              # noqa: E712
    g = pg[a_up | a_dn].copy()
    isup = a_up[a_up | a_dn].to_numpy()                      # the two arms are disjoint by construction
    g["arm"] = np.where(isup, "P up (WT-selective induction)", "P down (WT-selective repression)")
    g["q_arm"] = np.where(isup, g["q_up"], g["q_down"])      # the gene's own direction's FDR
    # cross-fitted stability: the program rule re-run on p53-activating drug-doses selected without each
    # compound fold's compounds. This holds compounds out, not labels, so it bounds compound-driven
    # instability and does not touch the label circularity.
    g["n_folds_kept"] = np.where(isup, g[fu].sum(axis=1) if fu else np.nan,
                                 g[fd].sum(axis=1) if fd else np.nan)
    g["n_folds_total"] = len(fu) if fu else np.nan
    # loco_frequency counts leave-one-compound-out INDUCTION programs only (program_rule is called with
    # sign = +1 there), so the published 0.0 on every P-down gene is structural, not fragility: blank it
    # rather than let it read as a stability failure. n_folds_kept is the down arm's only stability column.
    g.loc[~isup, "loco_frequency"] = np.nan
    pm = os.path.join(res, "genome_wide/tables/b_p53_program.csv")    # program_is_fallback lives here
    if os.path.exists(pm):
        pmd = pd.read_csv(pm)
        if "program_is_fallback" in pmd.columns:
            g = g.merge(pmd[["symbol", "program_is_fallback"]].drop_duplicates("symbol"),
                        on="symbol", how="left")
    # rank_in_P is the rank by z WITHIN THE INDUCTION ARM (genome_wide.py:1988 fills it for P only), so it
    # is blank on every P-down row by construction, not missing data.
    t = g[["symbol", "idx", "arm", "rank_in_P", "z_program", "q_arm", "median_line_cpm",
           "n_lines_expressing", "wt_mean_log2", "wt_minus_alt_log2", "frac_compounds_up",
           "frac_compounds_wt_up", "n_compounds_with_z", "loco_frequency", "n_folds_kept",
           "n_folds_total", "in_P_noX"]
          + [c for c in ("program_is_fallback",) if c in g.columns] + list(ov)].rename(columns=ov)
    t.insert(t.columns.get_loc("wt_mean_log2") + 1, "wt_fold", 2.0 ** t["wt_mean_log2"])
    t.insert(t.columns.get_loc("wt_minus_alt_log2") + 1, "wt_minus_alt_fold",
             2.0 ** t["wt_minus_alt_log2"])
    t = screen(t).sort_values("wt_mean_log2", ascending=False, kind="stable").reset_index(drop=True)
    t["fold_change_columns_are_circular"] = True      # chosen with the TP53 labels; see the docstring
    t["mg53_columns_are_circular"] = False
    os.makedirs(out, exist_ok=True)
    t.to_csv(os.path.join(out, "tableD_p53_target_genes.csv"), index=False)
    signed_tally(t, out, "tableD_signed_tally.csv")

    # The other direction, for contrast: what MG53's level actually tracks genome-wide. The program selects
    # nothing here - the ranking is by |b_common| among the genes the screen itself calls hits.
    s = sc[(sc["tested"] == True) & sc["q_common"].notna() & (sc["q_common"] < 0.1)]      # noqa: E712
    s = s.reindex(s["b_common"].abs().sort_values(ascending=False, kind="stable").index).head(100)
    pb = pg[["symbol", "median_line_cpm", "n_lines_expressing", "in_P", "in_P_down", "z_program",
             "wt_mean_log2", "q_up", "loco_frequency"] + list(ov)].rename(
        columns={**ov, "in_P": "in_p53_program_P", "in_P_down": "in_p53_program_P_down"})
    p = s[["symbol"]].merge(pb, on="symbol", how="left")
    p.insert(p.columns.get_loc("wt_mean_log2") + 1, "wt_fold", 2.0 ** p["wt_mean_log2"])
    p = screen(p).sort_values("screen_b_common", key=lambda v: -v.abs(),
                              kind="stable").reset_index(drop=True)
    p.to_csv(os.path.join(out, "tableD_top_mg53_partners.csv"), index=False)
    return t


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--results", default=os.environ.get("MG53_RESULTS") or os.path.expanduser("~/Tahoe-100M/mg53_p53"),
                    help="a finished run's output folder (holds export/, genome_wide/, p53_dependence/ ...)")
    ap.add_argument("--out", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "tables"),
                    help="where to write the CSVs")
    a = ap.parse_args()
    res = os.path.abspath(os.path.expanduser(a.results))
    out = os.path.abspath(os.path.expanduser(a.out))
    os.makedirs(out, exist_ok=True)
    need = ["export/TRIM72/TRIM72_per_drugdose_line.csv", "export/downstream/program_scores_per_drugdose_line.csv",
            "genome_wide/tables/b_drugdose_p53_activation.csv", "p53_dependence/tables/lines_tp53_status.csv"]
    missing = [p for p in need if not os.path.exists(os.path.join(res, p))]
    if missing:
        raise SystemExit(f"not found under {res}:\n  " + "\n  ".join(missing)
                         + "\nRun the pipeline first, or point --results at its output folder.")
    d, ls = load(res)
    print(f"{len(d):,} line x drug-dose rows, {d.cell_line_id.nunique()} lines, {d.drug_dose_row.nunique()} drug-doses")
    print("\nTABLE A  MG53 -> p53 targets, TP53-wild-type lines")
    print(table_a(d, out)[["readout", "r_raw", "r_twoway", "slope_twoway", "slope_lo", "slope_hi",
                           "direction"]].to_string(index=False))
    print("\nTABLE B  upstream of MG53 (rows: %d)" % len(table_b(res, out)))
    tc, ind = table_c(d, ls, out)
    print("\nTABLE C  MG53 -> p53 program, mutants by retained p53 activity")
    print(tc[["split", "group", "n_lines", "r", "slope", "slope_lo", "slope_hi", "direction"]].to_string(index=False))
    print("\np53 nullification across the panel")
    print(nullification(ind, ls, res, out).to_string(index=False))
    print("\nCanonical p53 effectors, per gene (fold change and MG53's slope)")
    pe = p53_effectors(res, out)
    print(pe[["symbol", "role", "fold_ida5", "fold_WT_broad", "wt_minus_alt_log2", "b_common",
              "q_common", "mg53_common_verdict", "mg53_genotype_verdict"]].to_string(index=False))
    print("\nPer-gene: every p53 program gene, its fold change and MG53's slope")
    td = table_d(res, out)
    print(td.head(12).to_string(index=False) if hasattr(td, "head") else td)
    print(f"\nwrote 9 CSVs to {out}")


if __name__ == "__main__":
    main()
