#!/usr/bin/env python3
"""Summary tables of the MG53 (TRIM72) / p53 analysis: one compact table per question, as CSV and as markdown.

Reads the tables the four workstream scripts wrote (upstream_perturbations/, upstream_coregulation/, p53_dependence/,
downstream_p53/ under --in) plus the gene panel's pathway scores (<data>/gene_panel/results), and writes
<in>/summary/*.csv and <in>/SUMMARY.md. Nothing is recomputed here: every number comes from those tables.

    python3 summary_tables.py --in <folder with the workstream outputs> [--data <Tahoe-100M folder>]
"""
import argparse
import os
import re

import numpy as np
import pandas as pd

IDA = "Idarubicin (hydrochloride)"


def fx(log2=None, fold=None):
    v = fold if fold is not None else (2.0 ** log2 if log2 is not None and np.isfinite(log2) else np.nan)
    return "–" if not np.isfinite(v) else (f"{v:.1f}×" if v >= 0.95 else f"{v:.2f}×")


def num(v, d=2):
    return "–" if v is None or not np.isfinite(v) else f"{v:.{d}f}"


def pval(v):
    if v is None or not np.isfinite(v):
        return "–"
    if v == 0:
        return "<1e-15"
    return f"{v:.0e}" if v < 1e-3 else f"{v:.3f}" if v < 0.1 else f"{v:.2f}"


def short(drug):
    return re.sub(r"\s*\((hydrochloride|dihydrochloride|calcium|Octahydrate)\)", "", str(drug))


def md(df):
    cols = list(df.columns)
    out = ["| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]
    out += ["| " + " | ".join(str(v) for v in row) + " |" for row in df.itertuples(index=False)]
    return "\n".join(out)


def t1_drugdoses(ws, data):
    """Drug-doses that significantly raise or lower TRIM72, with replication and p53 activation."""
    r = pd.read_csv(os.path.join(ws, "upstream_perturbations", "tables", "a_TRIM72_drugdose_ranking.csv"))
    s = r[(r["sig_up"] == True) | (r["sig_down"] == True)].copy()  # noqa: E712
    p53 = None
    ps = os.path.join(data, "gene_panel", "results", "pathway_scores_by_dose.csv") if data else ""
    if ps and os.path.exists(ps):
        p = pd.read_csv(ps)
        p53 = p[p["score"] == "P53_ACTIVITY"].set_index(["drug", "conc"])["z"]

    def replication(row):
        by = [float(m) for m in re.findall(r":\s*([0-9.]+)x", str(row["pooled_fold_no_pseudocount_by_well"]))]
        up = row["sig_up"] == True  # noqa: E712
        if len(by) < 2:
            return "single well"
        ok = [b >= 1.5 if up else b <= 1 / 1.5 for b in by]
        return f"replicated ({len(by)} wells)" if all(ok) else f"not replicated ({sum(ok)}/{len(by)} wells)"

    rows = []
    for _, x in s.sort_values("z", ascending=False).iterrows():
        rows.append({
            "Drug": short(x["drug"]), "Dose (µM)": f"{x['conc']:g}",
            "TRIM72 fold (corrected)": fx(fold=x["fold_change"]), "z": num(x["z"], 1),
            "q": pval(x["q_up"] if x["sig_up"] == True else x["q_down"]),  # noqa: E712
            "Fold without pseudocount": fx(fold=x["pooled_fold_no_pseudocount"]),
            "Wells": replication(x), "Plates": ", ".join(sorted(re.findall(r"\d+", str(x["plates"])), key=int)),
            "p53 activity z": num(p53.get((x["drug"], x["conc"]), np.nan), 1) if p53 is not None else "–",
            "Genes changed": f"{int(x['n_sig_genes']):,}" if np.isfinite(x["n_sig_genes"]) else "–",
            "Flags": "" if pd.isna(x["flags"]) else str(x["flags"]),
        })
    return pd.DataFrame(rows)


def t2_classes(ws):
    """Drug classes among TRIM72 raisers and lowerers, matched for global activity (compound level)."""
    c = pd.read_csv(os.path.join(ws, "upstream_perturbations", "tables", "b_TRIM72_class_enrichment_compound_level.csv"))
    up = c[(c["system"] == "curated") & (c["n_raisers"] > 0)].sort_values("p_raisers_stratified").head(8)
    dn = c[c["mean_z_min_resid"] < 0].sort_values("p_mean_z_min_down_stratified").head(4)
    rows = []
    for tag, t in (("raises", up), ("lowers", dn)):
        for _, x in t.iterrows():
            rows.append({
                "Direction": tag, "Class": x["class"], "Grouping": x["system"], "Compounds": int(x["n_compounds"]),
                "Movers (observed / expected)": (f"{int(x['n_raisers'])} / {x['expected_raisers_activity_matched']:.1f}"
                                                 if tag == "raises" else f"{int(x['n_lowerers_nominal'])} / "
                                                 f"{x['expected_lowerers_nominal_activity_matched']:.1f}"),
                "p (activity-matched; lowers: mean z)": pval(x["p_raisers_stratified"] if tag == "raises"
                                             else x["p_mean_z_min_down_stratified"]),
                "q": pval(x["q_raisers_stratified"] if tag == "raises" else x["q_mean_z_min_down_stratified"]),
                "Members that move TRIM72": (x["raisers_names"] if tag == "raises" else x["lowerers_nominal_names"])
                if isinstance(x["raisers_names" if tag == "raises" else "lowerers_nominal_names"], str) else "",
            })
    return pd.DataFrame(rows)


def t3_programs(ws):
    """Programs and genes that move with TRIM72 across all drug-doses (partial Spearman, activity and cell loss out)."""
    d = pd.read_csv(os.path.join(ws, "upstream_perturbations", "tables", "d_TRIM72_vs_programs_correlations.csv"))
    d = d.sort_values("partial_spearman_activity_cellloss", ascending=False)
    return pd.DataFrame({
        "Program / gene": d["program"],
        "rho, all drug-doses (activity, cell loss out)": d["partial_spearman_activity_cellloss"].map(lambda v: num(v)),
        "q": d["q_partial_activity_cellloss"].map(pval),
        "rho, active drug-doses only": d["partial_spearman_active_only_activity"].map(lambda v: num(v)),
        "n drug-doses": d["n"].astype(int),
    })


def t4_locus(ws):
    """The chr16p11.2 neighbourhood of TRIM72: strand, position and response to the strongest TRIM72 raisers."""
    t = pd.read_csv(os.path.join(ws, "upstream_coregulation", "tables", "c_locus_neighbours_effects.csv"))
    t = t[t["Idarubicin_5_log2FC"].notna() | t["label"].isin(["TRIM72", "PYDC1"])].sort_values("start")
    return pd.DataFrame({
        "Gene": t["label"], "Strand": t["strand"].map(lambda s: "+" if s in (1, "1", "+") else "−"),
        "Position vs TRIM72": t["rel_to_TRIM72"], "Distance (kb)": (t["distance_bp"] / 1000).map(lambda v: num(v, 1)),
        "Median line CPM": t["median_line_cpm"].map(lambda v: num(v, 1)),
        "Idarubicin 5 µM": t["Idarubicin_5_log2FC"].map(lambda v: fx(log2=v)),
        "Homoharringtonine 5 µM": t["Homoharringtonine_5_log2FC"].map(lambda v: fx(log2=v)),
        "Dinaciclib 5 µM": t["Dinaciclib_5_log2FC"].map(lambda v: fx(log2=v)),
        "r with TRIM72 across drug-doses": t["r_z_with_TRIM72_over_drugdoses"].map(lambda v: num(v)),
    })


def t5_p53_dependence(ws):
    """TRIM72 induction in TP53 wild-type vs altered lines in the same wells, with p53 targets as positive controls."""
    k = pd.read_csv(os.path.join(ws, "p53_dependence", "tables", "key_results.csv"))
    k = k[k["scope"] == "mean of used wells"]
    rows = []
    for (drug, conc), g in k.groupby(["drug", "conc"], sort=False):
        g = g.set_index("gene")
        if "TRIM72" not in g.index:
            continue
        t = g.loc["TRIM72"]
        row = {"Drug": short(drug), "Dose (µM)": f"{conc:g}",
               "TRIM72 WT lines": fx(fold=t["fc_wt"]), "TRIM72 altered lines": fx(fold=t["fc_altered"]),
               "TRIM72 WT − altered (log2)": num(t["diff_wt_minus_altered_log2"]),
               "95% CI": f"{num(t['ci95_low'])} to {num(t['ci95_high'])}", "p": pval(t["p_perm"]),
               "Altered lines up": f"{t['frac_altered_lines_up']:.0%}" if np.isfinite(t["frac_altered_lines_up"]) else "–"}
        for gene in ("MDM2", "P53_SCORE"):
            row[f"{gene.replace('_SCORE', ' score')} WT − altered (log2), p"] = \
                f"{num(g.loc[gene, 'diff_wt_minus_altered_log2'])}, {pval(g.loc[gene, 'p_perm'])}" if gene in g.index else "–"
        rows.append(row)
    return pd.DataFrame(rows)


def t6_per_line(ws):
    """Idarubicin 5 µM per cell line: TRIM72 next to p53 targets and stress genes (corrected fold, mean of 2 wells)."""
    p = pd.read_csv(os.path.join(ws, "p53_dependence", "tables", "per_line_effects_selected.csv"))
    p = p[(p["drug"] == IDA) & np.isclose(p["conc"], 5.0) & (p["scope"] == "mean of used wells")]
    w = p.pivot_table(index=["cell_name", "organ", "tp53_group"], columns="gene", values="log2FC_corrected").reset_index()
    genes = [g for g in ("TRIM72", "P53_SCORE", "MDM2", "CDKN1A", "BBC3", "TP53I3", "TP53", "ATF3", "PMAIP1") if g in w]
    w = w.assign(_wt=(w["tp53_group"] == "WT")).sort_values(["_wt", "TRIM72"], ascending=[False, False])
    out = pd.DataFrame({"Cell line": w["cell_name"], "Tissue": w["organ"], "TP53 status": w["tp53_group"]})
    for g in genes:
        out[{"P53_SCORE": "p53 score (21 targets)", "TP53": "TP53 mRNA"}.get(g, g)] = w[g].map(lambda v: fx(log2=v))
    return out


def t7_downstream(ws):
    """Does TRIM72 go with more or less p53 output? Every test, its estimate and what it can exclude."""
    D = os.path.join(ws, "downstream_p53", "tables")
    a = pd.read_csv(os.path.join(D, "a_line_correlations.csv"))
    po = pd.read_csv(os.path.join(D, "a_pooled_over_drugdoses.csv"))
    b = pd.read_csv(os.path.join(D, "b_baseline_tests.csv"))
    c = pd.read_csv(os.path.join(D, "c_correlations_across_drugdoses.csv"))
    d = pd.read_csv(os.path.join(D, "d_single_cell_meta_main.csv"))
    rows = []

    def add(test, group, est, p, n):
        rows.append({"Test": test, "Lines / cells": group, "Estimate": est, "p": pval(p), "n": n})

    for grp in ("TP53-WT", "TP53-altered"):
        for adj, lab in (("none", "unadjusted"), ("beta+A", "drug response and cell loss out")):
            x = a[(a["drug"] == IDA) & np.isclose(a["conc"], 5.0) & (a["scope"] == "all used wells")
                  & (a["predictor"] == "TRIM72_r2") & (a["outcome"] == "P53_SCORE") & (a["tp53_group"] == grp)
                  & (a["adjustment"] == adj)]
            if len(x):
                x = x.iloc[0]
                add(f"Idarubicin 5 µM, per line: TRIM72 induction vs p53-score induction ({lab})", grp,
                    f"rho {num(x['rho'])}", x["p_perm"], f"{int(x['n_lines'])} lines")
    for grp in ("TP53-WT", "TP53-altered"):
        for outc in ("P53_SCORE", "MDM2"):
            x = po[(po["set"] == "TRIM72 raisers") & (po["tp53_group"] == grp) & (po["outcome"] == outc)
                   & (po["adjustment"] == "beta+A") & (po["predictor"] == "TRIM72_r2")]
            if len(x):
                x = x.iloc[0]
                add(f"{int(x['n_drugdoses'])} TRIM72 raisers pooled, per line: TRIM72 vs {outc.replace('_SCORE', ' score')}"
                    " (drug response and cell loss out)", grp, f"mean rho {num(x['mean_rho'])}",
                    x["p_line_permutation"], f"{int(x['n_drugdoses'])} drug-doses")
    for grp in ("TP53-WT", "TP53-altered"):
        for y, lab in (("basal_p53_within_plate", "basal p53 activity"), ("p53_responsiveness_log2_panel", "p53 responsiveness"),
                       ("TP53_rel_reliable_plates", "TP53 mRNA")):
            x = b[(b["x"] == "TRIM72_rel_reliable_plates") & (b["y"] == y) & (b["tp53_group"] == grp)]
            if len(x):
                x = x.iloc[0]
                add(f"Untreated, per line (within plates): TRIM72 level vs {lab}", grp, f"rho {num(x['rho'])}",
                    x["p_perm"], f"{int(x['n_lines'])} lines")
    for y in ("P53_ACTIVITY_z", "MDM2_z", "p53_WT_minus_altered_z", "PMAIP1_z"):
        x = c[(c["subset"] == "all drug-doses") & (c["x"] == "TRIM72_z") & (c["y"] == y)
              & (c["adjustment"] == "activity (n_sig_genes, cells, S, G2M)")]
        if len(x):
            x = x.iloc[0]
            add(f"Across all drug-doses: TRIM72 z vs {y.replace('_z', ' z')} (activity out)", "all lines pooled",
                f"rho {num(x['rho'])} (CI {num(x['ci95_low_drug_bootstrap'])} to {num(x['ci95_high_drug_bootstrap'])})",
                x["p"], f"{int(x['n_drugdoses'])} drug-doses")
    for grp in ("TP53-WT", "TP53-altered"):
        for outc in ("P53_SCORE", "MDM2", "ATF3", "PMAIP1"):
            x = d[(d["wellset"] == "idarubicin 5 uM, both wells") & (d["tp53_group"] == grp.replace("TP53-", ""))
                  & (d["outcome"] == outc)]
            if len(x):
                x = x.iloc[0]
                add(f"Single cells, idarubicin 5 µM: {outc.replace('_SCORE', ' score')} counts in TRIM72-detected vs "
                    "undetected cells (depth, cycle out)", grp, f"rate ratio {num(x['rate_ratio'], 3)}", x["p"],
                    f"{int(x['n_lines'])} lines")
    return pd.DataFrame(rows)


def t8_answers():
    """The short answers (written from the verified findings; see README.md for the evidence and caveats)."""
    return pd.DataFrame([
        ("Is TRIM72 a p53 target gene?", "No", "Not in the p53-target census or near TP53 ChIP peaks; behaves like a non-target "
         "on 4 metrics in Tahoe (T5)", "strong"),
        ("Does TRIM72 induction need p53?", "No", "Rises in 31/31 TP53-altered lines under idarubicin 5 µM; selinexor activates "
         "p53 without raising TRIM72 (T5)", "strong"),
        ("Could a small p53 contribution exist?", "Not excluded", "WT lines lean +0.16 to +0.45 log2 across raisers, also for drugs "
         "that do not activate p53 (T5)", "moderate"),
        ("What raises TRIM72 mRNA?", "Strong stress drugs", "Anthracyclines/TOP2 poisons, harringtonines, auranofin, CDK9 and "
         "HDAC inhibitors; robust and replicated: idarubicin and homoharringtonine 5 µM (T1, T2)", "moderate"),
        ("What moves with it?", "AP-1 / immediate-early, ATF3, PMAIP1", "Co-responders across drugs and in single cells, not shown "
         "regulators; muscle TFs (MyoD/MEF2, the known promoter TFs) are silent in these lines (T3)", "moderate"),
        ("Is it TRIM72's own promoter?", "Unresolved", "Part of TRIM72's reads look like readthrough from FUS (17-22 kb upstream, "
         "same strand); clean for homoharringtonine, not significant for idarubicin after level matching (T4)", "moderate"),
        ("Does more TRIM72 go with less p53 output?", "No detectable association", "Per line, across drugs, untreated and in "
         "single cells; only strong associations are excluded (17 WT lines) (T6, T7)", "null, limited power"),
        ("Does MG53 act on p53 protein?", "Not testable here", "Literature: MG53 binds p53 and drives its degradation "
         "(cardiomyocytes 2024, trophoblasts 2021); Tahoe has mRNA only and no MG53 perturbation", "literature only"),
    ], columns=["Question", "Answer", "Basis", "Strength"])


TABLES = [
    ("T8_answers", "Short answers", t8_answers, False),
    ("T1_drugdoses_moving_TRIM72", "T1. Drug-doses that significantly change TRIM72 mRNA (q < 0.1, >= 1.2x)", t1_drugdoses, True),
    ("T2_drug_classes", "T2. Drug classes, matched for global activity (compound level)", t2_classes, False),
    ("T3_programs_moving_with_TRIM72", "T3. What moves with TRIM72 across all drug-doses", t3_programs, False),
    ("T4_TRIM72_locus", "T4. The TRIM72 neighbourhood (chr16p11.2): readthrough check", t4_locus, False),
    ("T5_p53_dependence", "T5. TRIM72 induction in TP53 wild-type vs altered lines (same wells)", t5_p53_dependence, False),
    ("T6_idarubicin_per_line_TRIM72_and_p53", "T6. Idarubicin 5 µM per cell line: TRIM72 next to p53 targets", t6_per_line, False),
    ("T7_TRIM72_vs_p53_output_tests", "T7. Does TRIM72 go with more or less p53 output?", t7_downstream, False),
]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--in", dest="inp", default=os.path.dirname(os.path.abspath(__file__)),
                    help="folder holding upstream_perturbations/, upstream_coregulation/, p53_dependence/, downstream_p53/")
    ap.add_argument("--data", default=os.environ.get("MG53_DATA") or os.environ.get("TAHOE_DATA")
                    or os.path.expanduser("~/Tahoe-100M"), help="Tahoe-100M folder (for the panel's p53 activity z)")
    a = ap.parse_args()
    out = os.path.join(a.inp, "summary")
    os.makedirs(out, exist_ok=True)
    parts = ["# MG53 (TRIM72) and p53 in Tahoe-100M: summary tables",
             "", "Generated by summary_tables.py from the workstream tables. mRNA, 24 h, 50 cancer cell lines; every "
             "MG53-p53 relation here is an association (Tahoe has no MG53 perturbation). Fold changes are corrected "
             "(method v3) unless labelled otherwise. TRIM72's untreated level is ~10x lower on plates 4-13 than on "
             "plates 1-3 and 14, which inflates folds on the low plates: compare z or replicated wells.", ""]
    for name, title, fn, needs_data in TABLES:
        try:
            df = fn(a.inp, a.data) if needs_data else (fn() if name == "T8_answers" else fn(a.inp))
        except FileNotFoundError as e:
            parts += [f"## {title}", "", f"(not available: {os.path.basename(str(e.filename))} missing; run that step)", ""]
            continue
        df.to_csv(os.path.join(out, name + ".csv"), index=False)
        parts += [f"## {title}", "", (fn.__doc__ or "").strip(), "", md(df), ""]
        print(f"{name}: {len(df)} rows")
    with open(os.path.join(a.inp, "SUMMARY.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(parts) + "\n")
    print("wrote", os.path.join(a.inp, "SUMMARY.md"), "and", out)


if __name__ == "__main__":
    main()
