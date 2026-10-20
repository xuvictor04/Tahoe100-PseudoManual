#!/usr/bin/env python3
"""TRIM72 x idarubicin, per cell line, with the method-v3 corrections of tahoe_gene_panel.py.

Runs the panel's own setup (load, baseline, expressed rule, position passes and plate factors with the atlas's
composition shift and plate factors) and T.expression_effects for TRIM72, then writes the per-line values that
expression_effects computes internally (r2 = plate x line baseline -> composition shift -> position correction),
per well and averaged over the used wells, as the method's own per_line table does.

    python3 trim72_ida_per_line.py --data DIR --outdir DIR
"""
import argparse, os, sys

import numpy as np
import pandas as pd

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))   # the repo root
sys.path.insert(0, REPO)
import tahoe_gene_panel as P          # noqa: E402
import tahoe_mtap_gankyrin as T       # noqa: E402

GENE, DRUG_PAT = os.environ.get("GENE", "TRIM72"), os.environ.get("DRUG_PAT", "Idarubicin")


def run(args, outdir):
    S = P.Run(args)
    S.R = os.path.join(outdir, "panel_tables")        # the panel's side tables go here, not into gene_panel/results
    P.load(S)
    P.step_baseline(S)
    P.step_expression(S)
    P.step_prepare(S)
    S.ctx = T.well_context(S.wl, S.sm, S.cols, S.M)
    excl = P.gene_exclusions(S, GENE)
    res, W, d, cal = T.expression_effects(S.wl, S.sm, GENE, excl, S.ctx, S.drugs, method=S.M)
    drug = next(x for x in res["drug"].unique() if DRUG_PAT.lower() in str(x).lower())

    # drug-dose rows (the panel's TRIM72_by_dose view) for idarubicin, every dose
    dd = res[res["drug"] == drug].sort_values("conc")
    dd.to_csv(os.path.join(outdir, "TRIM72_idarubicin_by_dose_corrected.csv"), index=False)

    # per well x line at 5 uM, the used wells only (unreliable plates only when nothing else), as the method
    Wd = W.loc[~W["is_dmso"]].copy()
    Wd["dose"] = T.dose_key(Wd)
    Wd["_used"] = T.used_wells(Wd)
    w5 = Wd[(Wd["drug"] == drug) & np.isclose(Wd["conc"].astype(float), 5.0)]
    used = w5.index[w5["_used"]]
    x = d[d["sample"].isin(w5.index)].copy()
    x["used"] = x["sample"].isin(used)
    x["plate"] = x["sample"].map(W["plate"])
    x["well"] = x["sample"].map(W["well"])
    x["position_effect_removed"] = x["sample"].map(W["slot_effect"])
    x["composition_shift_log2"] = x["r1"] - x["r1c"]
    name = S.name
    x["cell_line"] = x["cell_line_id"].map(name)
    per_well = x[["cell_line", "cell_line_id", "plate", "well", "used", "n_cells", GENE, "total_counts", "y",
                  "r1", "composition_shift_log2", "position_effect_removed", "r2", "z_line", "lfc_dmso"]] \
        .sort_values(["cell_line", "plate"])
    per_well.to_csv(os.path.join(outdir, "TRIM72_idarubicin_5uM_per_well_line.csv"), index=False)

    u = x[x["used"]]
    g = u.groupby("cell_line_id")
    pl = g[["r2", "z_line"]].mean()                       # the method's per_line: mean over the used wells
    pl["n_wells"] = g.size()
    for p_ in sorted(u["plate"].unique(), key=lambda s: (len(s), s)):
        pl[f"log2FC_{p_}"] = u[u["plate"] == p_].set_index("cell_line_id")["r2"]
    pl["log2FC_vs_DMSO_uncorrected"] = g["lfc_dmso"].mean()
    pl["up"] = (pl["z_line"] > T.Z_LINE) & (pl["r2"] > T.LFC_MIN)
    pl["down"] = (pl["z_line"] < -T.Z_LINE) & (pl["r2"] < -T.LFC_MIN)
    pl["fold_change"] = 2.0 ** pl["r2"]
    exl = pd.DataFrame({"cell_line": name, "organ": S.base["Organ"], "cpm_dmso": S.Cd[GENE],
                        "cpm_all_wells": S.C[GENE], "expressed": S.E[GENE]})
    out = exl.join(pl, how="left").rename(columns={"r2": "log2FC_corrected", "z_line": "z_line"})
    out = out.sort_values(["expressed", "log2FC_corrected"], ascending=[False, False])
    out.index.name = "cell_line_id"
    out.to_csv(os.path.join(outdir, "TRIM72_idarubicin_5uM_per_line_corrected.csv"))
    with open(os.path.join(outdir, "run_notes.txt"), "w") as fh:
        fh.write(f"drug: {drug}\nexpressed threshold (CPM): {float(S.thr[GENE]):.3f}\n"
                 f"median line CPM: {float(S.med[GENE]):.3f}; ambient CPM: {float(S.ambient[GENE]):.3f} "
                 f"(af {S.af:.3f}: {S.af_source})\nstatus: {S.status.get(GENE)}\n"
                 f"plate factors: {S.plate_scale_note}\nexcluded lines: {len(excl)}\n"
                 f"5 uM wells: {list(w5.index)}; used: {list(used)}\ncalibration: {cal}\n")
    print(open(os.path.join(outdir, "run_notes.txt")).read())
    print(dd[[c for c in ("drug", "conc", "call", "fold_change", "log2FC_corrected", "z_corrected", "fdr_up",
                          "n_lines", "n_lines_up", "flags", "log2FC_vs_DMSO_uncorrected", "position_effect_removed",
                          "composition_shift_log2", "plates") if c in dd]].to_string(index=False))
    print(out.to_string())


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", required=True)
    ap.add_argument("--outdir", required=True)
    a, rest = ap.parse_known_args()                    # anything else goes to the panel (e.g. --min-cells)
    os.makedirs(a.outdir, exist_ok=True)
    # the panel's own argument defaults: let its parser build them, then run our steps instead of 'analyze'
    P.cmd_analyze = lambda args: run(args, a.outdir)
    P.cmd_bundle = lambda args: None
    P.next_steps = lambda args: "done"
    sys.argv = ["tahoe_gene_panel.py", "analyze", "--data", a.data] + rest
    P.main()
