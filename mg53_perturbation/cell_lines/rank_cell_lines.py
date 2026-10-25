#!/usr/bin/env python3
"""Rank candidate cell lines for an MG53 (TRIM72) perturbation experiment, from Tahoe-100M.

Builds cell_line_candidates.csv: all 50 Tahoe lines with the metrics the MG53 experiment
needs, a group (WT-candidate / altered-comparator), a rank within group, and a 'why' column.

Metrics per line (Tahoe-100M, method v3, mRNA, 24 h, read-only inputs):
  - TP53 annotation + protein change, derived variant class (null/truncating vs missense vs splice)
  - p53 functional responsiveness: p53_responsiveness_log2 = reference-dose p53-target induction
    (p53_functional_status.csv, 10 reference doses), functional_call, basal p53 activity
  - p53 program inducibility by idarubicin 5 uM (per-line P53_SCORE & MDM2 fold) as a second read
  - untreated TRIM72 level, DMSO/quiet wells, WITHIN-PLATE standardised (TRIM72 plate batch)
  - TRIM72 inducibility by idarubicin 5 uM and homoharringtonine 5 uM (both replicated in Tahoe)
  - cell numbers / growth: n_cells_total, and relative abundance under the two drugs (survives?)
  - lineage (organ)

Usage: python3 rank_cell_lines.py [--data DIR]
  DIR defaults to $MG53_DATA, $TAHOE_DATA, or ~/Tahoe-100M. It must contain
  atlas/effects, gene_panel/results. Existing analysis tables are read from the repo
  (mg53_p53/, trim72_idarubicin/) relative to this script if present, else recomputed-paths.
Nothing is written under the data dir; output CSV is written next to this script.
"""
import os, sys, csv, argparse, math
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))  # Tahoe100-PseudoManual


def find_data(cli):
    for c in (cli, os.environ.get("MG53_DATA"), os.environ.get("TAHOE_DATA"),
              os.path.expanduser("~/Tahoe-100M"), "/home/user/tahoe_data"):
        if c and os.path.isdir(os.path.join(c, "atlas", "effects")):
            return c
    sys.exit("Could not find a Tahoe data dir with atlas/effects (use --data).")


def read_csv(path):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def f(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return float("nan")


def variant_class(changes):
    """Classify TP53 protein change string into a coarse functional class."""
    if not changes or not changes.strip():
        return "WT"
    s = changes
    low = s.lower()
    has_fs = "fs" in low
    has_stop = "*" in s
    has_del = ("del" in low and "fs" not in low) or s.strip().upper() == "DEL"
    has_splice = "splice" in low or (">" in s)  # e.g. 375+5G>T
    # synonymous only (e.g. 'Thr125Thr; p.T125T')
    import re
    aa = re.findall(r"p\.([A-Z])\d+([A-Z])", s)
    syn3 = re.findall(r"p\.([A-Za-z]{3})(\d+)([A-Za-z]{3})", s)
    only_syn = False
    if aa and all(a == b for a, b in aa) and not has_fs and not has_stop:
        only_syn = True
    if "125t" in low and "thr125thr" in low:
        only_syn = True
    if has_fs or has_stop or has_del:
        return "null/truncating"
    if has_splice:
        return "splice"
    if only_syn:
        return "silent(synonymous)"
    return "missense"


def zscore(vals):
    a = np.array(vals, dtype=float)
    m = np.nanmean(a)
    sd = np.nanstd(a)
    if not np.isfinite(sd) or sd == 0:
        return np.zeros_like(a)
    z = (a - m) / sd
    z[~np.isfinite(z)] = 0.0
    return z


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", default=None)
    ap.add_argument("--repo", default=REPO)
    ap.add_argument("--out", default=os.path.join(HERE, "cell_line_candidates.csv"))
    args = ap.parse_args()
    data = find_data(args.data)
    repo = args.repo
    gp = os.path.join(data, "gene_panel", "results")
    eff = os.path.join(data, "atlas", "effects")

    # ---- 1. p53 functional status (annotation, responsiveness, basal, call) ----
    pf = {r["cell_line_id"]: r for r in read_csv(os.path.join(gp, "p53_functional_status.csv"))}

    # ---- 2. atlas line order + cell counts + organ + driver changes ----
    lines = read_csv(os.path.join(eff, "lines.csv"))
    line_order = [r["cell_line_id"] for r in lines]
    line_idx = {cid: i for i, cid in enumerate(line_order)}
    ncells = {r["cell_line_id"]: f(r["n_cells_total"]) for r in lines}
    organ = {r["cell_line_id"]: r["Organ"] for r in lines}
    cname = {r["cell_line_id"]: r["cell_name"] for r in lines}

    # ---- 3. drug-dose index for relative abundance (survives drug?) ----
    dd = read_csv(os.path.join(eff, "drugdose.csv"))
    def dd_row(drug_sub, conc):
        for i, r in enumerate(dd):
            if drug_sub.lower() in r["drug"].lower() and abs(f(r["conc"]) - conc) < 1e-6:
                return i
        return None
    i_ida5 = dd_row("idarubicin", 5.0)
    i_hht5 = dd_row("homoharringtonine", 5.0)
    DD_A = np.load(os.path.join(eff, "DD_A.npy"), mmap_mode="r")  # drugdoses x lines, log2 rel abundance
    relabund_ida5 = {cid: float(DD_A[i_ida5, line_idx[cid]]) for cid in line_order}
    relabund_hht5 = {cid: float(DD_A[i_hht5, line_idx[cid]]) for cid in line_order}

    # ---- 4. within-plate standardised untreated TRIM72 (from coregulation baseline) ----
    trim_base_path = os.path.join(repo, "mg53_p53", "upstream_coregulation", "tables",
                                  "b_TRIM72_baseline_per_line.csv")
    trim_base = {r["cell_line_id"]: r for r in read_csv(trim_base_path)}

    # raw DMSO CPM of TRIM72 and MDM2 from expression_by_line.csv
    expr = read_csv(os.path.join(gp, "expression_by_line.csv"))
    trim_cpm_dmso = {r["cell_line_id"]: f(r["cpm_dmso"]) for r in expr if r["gene"] == "TRIM72"}

    # ---- 5. per-line effects for idarubicin 5 / homoharringtonine 5 (TRIM72, P53_SCORE, MDM2) ----
    ple_path = os.path.join(repo, "mg53_p53", "p53_dependence", "tables",
                            "per_line_effects_selected.csv")
    # key: (drug_sub, gene) -> {cid: (fold, z)}
    want = {
        ("idarubicin", "TRIM72"): {}, ("idarubicin", "P53_SCORE"): {}, ("idarubicin", "MDM2"): {},
        ("homoharringtonine", "TRIM72"): {}, ("homoharringtonine", "P53_SCORE"): {}, ("homoharringtonine", "MDM2"): {},
    }
    with open(ple_path, newline="") as fh:
        r = csv.DictReader(fh)
        for row in r:
            if row["scope"] != "mean of used wells":
                continue
            if row["conc"] not in ("5", "5.0"):
                continue
            d = row["drug"].lower()
            dsub = "idarubicin" if "idarubicin" in d else ("homoharringtonine" if "homoharringtonine" in d else None)
            if dsub is None:
                continue
            g = row["gene"]
            key = (dsub, g)
            if key in want:
                want[key][row["cell_line_id"]] = (f(row["fold_change"]), f(row["z_line"]))

    def getfz(dsub, gene, cid):
        return want[(dsub, gene)].get(cid, (float("nan"), float("nan")))

    # ---- assemble rows ----
    recs = []
    for cid in line_order:
        p = pf.get(cid, {})
        anno = p.get("tp53_annotation", "")
        changes = p.get("tp53_changes", "") or ""
        is_wt = anno.strip().lower().startswith("wild type")
        vclass = "WT" if is_wt else variant_class(changes)
        tb = trim_base.get(cid, {})
        ti_f, ti_z = getfz("idarubicin", "TRIM72", cid)
        th_f, th_z = getfz("homoharringtonine", "TRIM72", cid)
        p53_ida_f = getfz("idarubicin", "P53_SCORE", cid)[0]
        mdm2_ida_f = getfz("idarubicin", "MDM2", cid)[0]
        p53_hht_f = getfz("homoharringtonine", "P53_SCORE", cid)[0]
        recs.append({
            "cell_line_id": cid,
            "cell_name": cname.get(cid, p.get("cell_name", "")),
            "organ": organ.get(cid, p.get("organ", "")),
            "tp53_annotation": "WT" if is_wt else "altered",
            "tp53_changes": changes,
            "tp53_variant_class": vclass,
            "p53_functional_call": p.get("functional_call", ""),
            "p53_responsiveness_log2": f(p.get("p53_responsiveness_log2")),
            "p53_responsiveness_se": f(p.get("p53_responsiveness_se")),
            "responsiveness_rank": f(p.get("responsiveness_rank")),
            "basal_p53_activity_log2": f(p.get("basal_p53_activity_log2")),
            "discordant_note": p.get("discordant", ""),
            "p53score_fold_ida5": p53_ida_f,
            "mdm2_fold_ida5": mdm2_ida_f,
            "p53score_fold_hht5": p53_hht_f,
            "trim72_cpm_dmso_raw": trim_cpm_dmso.get(cid, float("nan")),
            "trim72_log2cpm_vs_plate_mean": f(tb.get("TRIM72_log2cpm_vs_plate_mean")),
            "trim72_cpm_median_over_plates": f(tb.get("TRIM72_cpm_median_over_plates")),
            "trim72_mean_rank_within_plate": f(tb.get("TRIM72_mean_rank_within_plate")),
            "trim72_fold_ida5": ti_f,
            "trim72_z_ida5": ti_z,
            "trim72_fold_hht5": th_f,
            "trim72_z_hht5": th_z,
            "n_cells_total": ncells.get(cid, float("nan")),
            "relabund_log2_ida5": relabund_ida5.get(cid, float("nan")),
            "relabund_log2_hht5": relabund_hht5.get(cid, float("nan")),
        })

    # ---- WT composite score ----
    wt = [r for r in recs if r["tp53_annotation"] == "WT"]
    # functional tier: responsive=0, uncertain=1, unresponsive/discordant=2
    def ftier(r):
        c = (r["p53_functional_call"] or "").lower()
        if r["discordant_note"]:
            return 2
        if c.startswith("responsive"):
            return 0
        if c.startswith("uncertain"):
            return 1
        return 2
    for r in wt:
        r["_ftier"] = ftier(r)
    # standardized components over WT lines
    resp_z = zscore([r["p53_responsiveness_log2"] for r in wt])
    p53f_z = zscore([r["p53score_fold_ida5"] for r in wt])
    mdm2_z = zscore([r["mdm2_fold_ida5"] for r in wt])
    base_z = zscore([r["trim72_log2cpm_vs_plate_mean"] for r in wt])
    tind_z = zscore([math.log2(r["trim72_fold_ida5"]) if r["trim72_fold_ida5"] > 0 else float("nan") for r in wt])
    thnd_z = zscore([math.log2(r["trim72_fold_hht5"]) if r["trim72_fold_hht5"] > 0 else float("nan") for r in wt])
    cell_z = zscore([math.log2(r["n_cells_total"]) if r["n_cells_total"] > 0 else float("nan") for r in wt])
    for k, r in enumerate(wt):
        r["wt_score"] = round(float(
            0.40 * resp_z[k] + 0.15 * p53f_z[k] + 0.10 * mdm2_z[k]
            + 0.10 * base_z[k] + 0.10 * tind_z[k] + 0.05 * thnd_z[k] + 0.10 * cell_z[k]), 4)
    wt.sort(key=lambda r: (r["_ftier"], -r["wt_score"]))
    for i, r in enumerate(wt, 1):
        r["rank_in_group"] = i

    # ---- altered comparator score ----
    alt = [r for r in recs if r["tp53_annotation"] == "altered"]
    top_wt_organs = [r["organ"] for r in wt[:3]]  # lineages of top WT picks
    def ctier(r):
        v = r["tp53_variant_class"]
        if v == "null/truncating":
            return 0
        if v == "splice":
            return 1
        if v == "silent(synonymous)":
            return 3
        return 2  # missense
    for r in alt:
        r["_ctier"] = ctier(r)
        r["_organ_match"] = 1 if r["organ"] in top_wt_organs else 0
    # lower responsiveness = better (confirms LOF); higher cells = better
    resp_a = np.array([r["p53_responsiveness_log2"] for r in alt], dtype=float)
    cell_a = zscore([math.log2(r["n_cells_total"]) if r["n_cells_total"] > 0 else float("nan") for r in alt])
    resp_a_z = zscore(resp_a)
    for k, r in enumerate(alt):
        r["alt_score"] = round(float(-0.6 * resp_a_z[k] + 0.4 * cell_a[k]), 4)
    # sort: variant tier, organ match (desc), alt_score (desc)
    alt.sort(key=lambda r: (r["_ctier"], -r["_organ_match"], -r["alt_score"]))
    for i, r in enumerate(alt, 1):
        r["rank_in_group"] = i

    # ---- why column ----
    for r in wt:
        bits = [f"TP53-WT; p53 {r['p53_functional_call'].split(' (')[0]}",
                f"responsiveness {r['p53_responsiveness_log2']:.2f} log2 (rank {int(r['responsiveness_rank']) if r['responsiveness_rank']==r['responsiveness_rank'] else '?'})",
                f"ida5 p53score {r['p53score_fold_ida5']:.1f}x / MDM2 {r['mdm2_fold_ida5']:.1f}x",
                f"TRIM72 within-plate {r['trim72_log2cpm_vs_plate_mean']:+.2f} log2, ida5 {r['trim72_fold_ida5']:.0f}x"]
        if r["discordant_note"]:
            bits.append(f"NOTE: {r['discordant_note']}")
        r["why"] = "; ".join(bits)
    for r in alt:
        bits = [f"TP53-altered ({r['tp53_variant_class']}: {r['tp53_changes']})",
                f"p53 {r['p53_functional_call'].split(' (')[0]} (responsiveness {r['p53_responsiveness_log2']:.2f})",
                f"lineage {r['organ']}" + (" [matches top WT]" if r["_organ_match"] else "")]
        r["why"] = "; ".join(bits)

    # ---- write combined CSV (WT first by rank, then altered by rank) ----
    cols = ["group", "rank_in_group", "cell_line_id", "cell_name", "organ",
            "tp53_annotation", "tp53_variant_class", "tp53_changes",
            "p53_functional_call", "p53_responsiveness_log2", "p53_responsiveness_se",
            "responsiveness_rank", "basal_p53_activity_log2",
            "p53score_fold_ida5", "mdm2_fold_ida5", "p53score_fold_hht5",
            "trim72_cpm_dmso_raw", "trim72_log2cpm_vs_plate_mean",
            "trim72_cpm_median_over_plates", "trim72_mean_rank_within_plate",
            "trim72_fold_ida5", "trim72_z_ida5", "trim72_fold_hht5", "trim72_z_hht5",
            "n_cells_total", "relabund_log2_ida5", "relabund_log2_hht5",
            "wt_score", "alt_score", "discordant_note", "why"]
    out_rows = []
    for r in wt:
        r["group"] = "WT-candidate"
        out_rows.append(r)
    for r in alt:
        r["group"] = "altered-comparator"
        out_rows.append(r)
    with open(args.out, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        for r in out_rows:
            def fmt(v):
                if isinstance(v, float):
                    if v != v:
                        return ""
                    return f"{v:.4g}"
                return v
            w.writerow({c: fmt(r.get(c, "")) for c in cols})
    print(f"wrote {args.out} ({len(out_rows)} lines: {len(wt)} WT, {len(alt)} altered)")

    # ---- console summary ----
    print("\nTop 8 WT candidates:")
    for r in wt[:8]:
        print(f"  {r['rank_in_group']:>2}. {r['cell_name']:<12} {r['organ']:<14} "
              f"call={r['p53_functional_call'].split(' (')[0]:<12} resp={r['p53_responsiveness_log2']:.2f} "
              f"p53score_ida5={r['p53score_fold_ida5']:.1f}x score={r['wt_score']:+.3f}")
    print("\nTop 8 altered comparators:")
    for r in alt[:8]:
        print(f"  {r['rank_in_group']:>2}. {r['cell_name']:<12} {r['organ']:<14} "
              f"class={r['tp53_variant_class']:<16} resp={r['p53_responsiveness_log2']:.2f} "
              f"organ_match={r['_organ_match']} score={r['alt_score']:+.3f}")


if __name__ == "__main__":
    main()
