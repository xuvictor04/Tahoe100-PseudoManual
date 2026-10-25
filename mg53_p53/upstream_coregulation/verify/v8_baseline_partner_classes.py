#!/usr/bin/env python3
"""F6 check: TRIM72's untreated partners (within-plate Spearman over lines, quiet wells, median over 13 plates; v3)
by neighbour geometry (v6 pairs, Ensembl 110), restricted to atlas genes. Compares the top-100 positive partners with
all atlas genes and with atlas genes of 1-20 CPM. Also: does the ranking survive partialling out a line-level
background of near-silent genes (v3 column rho_partial_given_silent_background)?

    python3 mg53_p53/upstream_coregulation/verify/v8_baseline_partner_classes.py   (needs v3 and v6 outputs)
"""
import os

import numpy as np
import pandas as pd
from scipy.stats import fisher_exact

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
FXD = "/home/user/tahoe_data/atlas/effects"


def main():
    genes = pd.read_csv(os.path.join(FXD, "genes.csv"))
    G = genes[genes["kind"] == "gene"].reset_index(drop=True)
    B = pd.read_csv(os.path.join(OUT, "v3_baseline_genomewide_quiet.csv"))
    PT = pd.read_csv(os.path.join(OUT, "v6_neighbour_pairs.csv"))
    conf = {}
    for c, h in PT.groupby("config"):
        conf[c] = set(G["token"].iloc[h["low"].to_numpy()].astype(int))
    A = B[B["token"].isin(G["token"])].copy()
    lvl = dict(zip(G["token"].astype(int), G["median_line_cpm"]))
    A["median_line_cpm"] = A["token"].map(lvl)
    rows = []
    for stat in ("rho_within_plate_median", "rho_partial_given_silent_background"):
        top = A.nlargest(100, stat)
        rest = A[~A["token"].isin(top["token"])]
        rest_lvl = rest[(rest["median_line_cpm"] >= 1) & (rest["median_line_cpm"] <= 20)]
        for c, s in conf.items():
            k = int(top["token"].isin(s).sum())
            m = int(rest_lvl["token"].isin(s).sum())
            OR, p = fisher_exact([[k, 100 - k], [m, len(rest_lvl) - m]])
            rows.append({"ranking": stat, "geometry": c, "top100_n": k,
                         "pct_rest_1to20cpm": 100 * m / len(rest_lvl), "pct_all_atlas": 100 * A["token"].isin(s).mean(),
                         "fisher_OR_vs_rest_1to20cpm": OR, "fisher_p": p})
    R = pd.DataFrame(rows)
    R.to_csv(os.path.join(OUT, "v8_baseline_partner_geometry.csv"), index=False, float_format="%.4g")
    pd.set_option("display.width", 220)
    print(R.round(4).to_string())
    print("top 20 atlas-gene baseline partners:", ", ".join(A.nlargest(20, "rho_within_plate_median")["gene"].astype(str)))


if __name__ == "__main__":
    main()
