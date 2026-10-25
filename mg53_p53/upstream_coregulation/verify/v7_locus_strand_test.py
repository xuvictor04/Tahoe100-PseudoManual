#!/usr/bin/env python3
"""F1 check: in the idarubicin / homoharringtonine 5 uM wells, are the (+)-strand genes downstream of FUS's end raised
more than the (-)-strand genes downstream and than the genes upstream, once each gene's rise is compared with genes of
its own level in the same well (level-matched percentile of log2 O/E, from v3)? Window: genes within 250 kb of
TRIM72 (Ensembl 110), expected >= 5 counts, TRIM72 itself excluded. Mann-Whitney (small n: read as descriptive).

    python3 mg53_p53/upstream_coregulation/verify/v7_locus_strand_test.py      (needs out/v3_locus_OE_in_wells.csv)
"""
import os

import numpy as np
import pandas as pd
from scipy.stats import mannwhitneyu

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")


def main():
    L = pd.read_csv(os.path.join(OUT, "v3_locus_OE_in_wells.csv"))
    L = L[(L["expected"] >= 5) & (L["gene"] != "TRIM72") & L["pct_vs_level_within2x"].notna()]
    rows = []
    for w, h in L.groupby("well"):
        dn = h["downstream_of_FUS_end_E110"].astype(bool)
        pdn = h[dn & (h["strand"] == 1)]
        mdn = h[dn & (h["strand"] == -1)]
        up = h[~dn]
        for lab, other in (("minus_downstream", mdn), ("upstream_any_strand", up), ("all_other_locus_genes",
                                                                                      h[~(dn & (h["strand"] == 1))])):
            rows.append({"well": w, "comparison": f"plus_downstream vs {lab}",
                         "n_plus_downstream": len(pdn), "n_other": len(other),
                         "median_pct_plus_downstream": pdn["pct_vs_level_within2x"].median(),
                         "median_pct_other": other["pct_vs_level_within2x"].median(),
                         "median_log2OE_plus_downstream": pdn["log2_OE"].median(),
                         "median_log2OE_other": other["log2_OE"].median(),
                         "MWU_p_one_sided": mannwhitneyu(pdn["pct_vs_level_within2x"], other["pct_vs_level_within2x"],
                                                         alternative="greater").pvalue,
                         "plus_downstream": "; ".join(f"{g} {p:.0f}" for g, p in zip(pdn["gene"], pdn["pct_vs_level_within2x"])),
                         "other": "; ".join(f"{g} {p:.0f}" for g, p in zip(other["gene"], other["pct_vs_level_within2x"]))})
    R = pd.DataFrame(rows)
    R.to_csv(os.path.join(OUT, "v7_locus_strand_test.csv"), index=False, float_format="%.4g")
    pd.set_option("display.width", 250)
    pd.set_option("display.max_colwidth", 200)
    print(R.drop(columns=["plus_downstream", "other"]).round(3).to_string())
    print(R[["well", "plus_downstream"]].drop_duplicates().to_string())
    print(R.loc[R["comparison"].str.contains("minus_downstream"), ["well", "other"]].to_string())


if __name__ == "__main__":
    main()
