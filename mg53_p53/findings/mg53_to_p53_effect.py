#!/usr/bin/env python3
"""Measure the change in p53 activity per change in MG53, with a p53-knockout-like control arm.

The question: for a doubling of MG53 (TRIM72) mRNA, how much does p53 activity change, and is that change
specific to cells that have working p53?

Design. Lines are split into arms by how much p53 activity they actually retain, so that the arms with no
p53 serve as a negative control. Tahoe has no engineered p53 knockout, but it has the next best thing: 10
lines whose only TP53 allele is truncated, splice-disrupted or deleted outright (KATO III is a whole-gene
deletion). Those cannot mount a p53 response, so any MG53 -> p53-activity slope measured in them is being
produced by something other than p53, and it is the right thing to subtract.

    A  functional p53      the lines the genotype-blind panel calls responsive (all are TP53 wild-type)
    B  WT, not responsive  TP53 wild-type by sequence but functionally damped
    B2 mutant, some activity
    C  low-activity mutant retains <= 15% of the wild-type-minus-null gap  (pseudo-control)
    D  p53-null CONTROL    truncating / splice / whole-gene deletion, core null reference  (knockout-like)

Model, per arm, matching the pipeline's fixed-effect structure: both cell-line and drug-dose means are
removed from the outcome and the exposure (iterated two-way demeaning), then one slope is fitted. So the
estimate uses only residual co-variation: for a given line under a given drug, does p53 activity deviate
from expectation in the same direction MG53 does? Standard errors are clustered on cell line.

    outcome   P_r2_mean   the data-defined p53 program score for that line x drug-dose (log2)
    exposure  r2_mean     MG53's corrected log2 fold change for the same cell

The headline is reported both as log2 of the program per doubling of MG53 and as a percentage change in p53
activity, with the knockout-controlled contrast A - D.

NOT computable from a run's output alone: per-arm placebo-gene pseudo-controls (a matched gene put in MG53's
place within each arm) need per-line values for arbitrary genes, which only `export/all_genes` on the full
data provides. The pipeline's own `c_placebos.csv` has 200 placebo exposures at the wild-type / altered split
only, and is printed for context.

Usage:
    python3 mg53_to_p53_effect.py --results ~/Tahoe-100M/mg53_p53
"""
import argparse
import os

import numpy as np
import pandas as pd

ARMS = ["A. functional p53 (responsive)", "B. WT, not fully responsive", "B2. mutant, some activity",
        "C. low-activity mutant (pseudo-control)", "D. p53-null CONTROL (trunc/splice/del)"]


def two_way_slope(s, x, y, cluster="cell_line_id", unit="drug_dose_row"):
    """One slope after removing both cluster and unit means from x and y, with a cluster-robust SE."""
    s = s.dropna(subset=[x, y]).copy()
    if s[cluster].nunique() < 3:
        return None
    s["_x"], s["_y"] = s[x].astype(float), s[y].astype(float)
    for _ in range(60):                                   # alternating projections; converges well before 60
        for c in ("_x", "_y"):
            s[c] -= s.groupby(cluster)[c].transform("mean")
            s[c] -= s.groupby(unit)[c].transform("mean")
    a, b = s["_x"].to_numpy(), s["_y"].to_numpy()
    sxx = float(np.sum(a * a))
    if sxx <= 0:
        return None
    beta = float(np.sum(a * b) / sxx)
    s["_r"] = b - beta * a
    num = sum(float(np.sum(g["_x"].to_numpy() * g["_r"].to_numpy())) ** 2 for _, g in s.groupby(cluster))
    se = float(np.sqrt(num) / sxx)
    return dict(b=beta, se=se, lo=beta - 1.96 * se, hi=beta + 1.96 * se,
                n_rows=len(s), n_lines=int(s[cluster].nunique()),
                pct=100 * (2 ** beta - 1), pct_lo=100 * (2 ** (beta - 1.96 * se) - 1),
                pct_hi=100 * (2 ** (beta + 1.96 * se) - 1),
                # smallest slope this arm could detect at 80% power, as a percentage
                mde_pct=100 * (2 ** (2.802 * se) - 1))


def load(res, state_dir):
    tx = pd.read_csv(os.path.join(res, "export/TRIM72/TRIM72_per_drugdose_line.csv"))
    pr = pd.read_csv(os.path.join(res, "export/downstream/program_scores_per_drugdose_line.csv"))
    act = pd.read_csv(os.path.join(res, "genome_wide/tables/b_drugdose_p53_activation.csv"))
    st = pd.read_csv(os.path.join(state_dir, "per_line_p53_state.csv"))
    nr = pd.read_csv(os.path.join(state_dir, "null_reference_lines.csv"))
    core = set(nr.loc[nr["role"].astype(str).str.startswith("null reference (core)"), "cell_line_id"])
    d = tx[["drug_dose_row", "cell_line_id", "cell_name", "tp53_group", "n_wells_r2", "r2_mean"]].merge(
        pr[["drug_dose_row", "cell_line_id", "P_r2_mean"]], on=["drug_dose_row", "cell_line_id"])
    d = d.merge(act[["drugdose_row", "in_S2_p53_activating"]], left_on="drug_dose_row",
                right_on="drugdose_row", how="left")
    d = d.merge(st[["cell_line_id", "functional_call", "ind_P_mean_frac_of_WT_gap"]],
                on="cell_line_id", how="left")
    d = d[(d["n_wells_r2"] >= 1) & d["r2_mean"].notna() & d["P_r2_mean"].notna()].copy()
    d["arm"] = np.where(d["functional_call"] == "responsive", ARMS[0],
                np.where(d["cell_line_id"].isin(core), ARMS[4],
                np.where(d["tp53_group"] == "WT", ARMS[1],
                np.where(d["ind_P_mean_frac_of_WT_gap"] <= 0.15, ARMS[3], ARMS[2]))))
    return d


def run(d, out):
    rows = []
    for scope, sub in (("all drug-doses", d),
                       ("p53-activating drug-doses", d[d["in_S2_p53_activating"] == True])):   # noqa: E712
        fits = {}
        for arm in ARMS:
            o = two_way_slope(sub[sub["arm"] == arm], "r2_mean", "P_r2_mean")
            if o:
                fits[arm] = o
                rows.append(dict(scope=scope, arm=arm, **o))
        a, c = fits.get(ARMS[0]), fits.get(ARMS[4])
        if a and c:                                        # the knockout-controlled contrast
            diff = a["b"] - c["b"]
            se = float(np.hypot(a["se"], c["se"]))
            rows.append(dict(scope=scope, arm="CONTRAST: functional minus p53-null", b=diff, se=se,
                             lo=diff - 1.96 * se, hi=diff + 1.96 * se,
                             n_rows=a["n_rows"] + c["n_rows"], n_lines=a["n_lines"] + c["n_lines"],
                             pct=100 * (2 ** diff - 1), pct_lo=100 * (2 ** (diff - 1.96 * se) - 1),
                             pct_hi=100 * (2 ** (diff + 1.96 * se) - 1),
                             mde_pct=100 * (2 ** (2.802 * se) - 1)))
    t = pd.DataFrame(rows)
    t.to_csv(os.path.join(out, "mg53_to_p53_effect.csv"), index=False)
    return t


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    here = os.path.dirname(os.path.abspath(__file__))
    ap.add_argument("--results", default=os.environ.get("MG53_RESULTS") or os.path.expanduser("~/Tahoe-100M/mg53_p53"))
    ap.add_argument("--out", default=os.path.join(here, "tables"))
    ap.add_argument("--state-dir", default=os.path.join(here, "tables"),
                    help="where per_line_p53_state.csv and null_reference_lines.csv live")
    a = ap.parse_args()
    res, out = (os.path.abspath(os.path.expanduser(p)) for p in (a.results, a.out))
    os.makedirs(out, exist_ok=True)
    t = run(load(res, os.path.abspath(os.path.expanduser(a.state_dir))), out)
    for scope, s in t.groupby("scope", sort=False):
        print(f"\n===== {scope}")
        print(f"{'arm':42s} {'lines':>5} {'slope (log2 P / doubling MG53)':>32} {'change in p53 activity':>26} {'MDE80':>8}")
        for _, r in s.iterrows():
            print(f"{r['arm']:42s} {int(r['n_lines']):5d}   {r['b']:+.5f} ({r['lo']:+.5f},{r['hi']:+.5f})"
                  f"   {r['pct']:+.3f}% ({r['pct_lo']:+.3f},{r['pct_hi']:+.3f})  {r['mde_pct']:+.2f}%")
    print("\nMDE80 = the smallest change this arm could have detected at 80% power.")
    print("Arm D cannot mount a p53 response, so any slope there is not p53-mediated and is the control.")
    print(f"\nwrote {os.path.join(out, 'mg53_to_p53_effect.csv')}")


if __name__ == "__main__":
    main()
