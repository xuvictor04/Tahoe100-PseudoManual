"""Compare the deterministic columns of the from-scratch --quick run (caches rebuilt under verify/out_quick) with the
committed tables (permutation-based columns differ by design: fewer permutations)."""
import os
import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
A = os.path.join(os.path.dirname(HERE), "tables")
B = os.path.join(HERE, "out_quick", "tables")
DET = ["n_rows", "b_WT", "b_alt", "diff", "se_diff_drug", "se_diff_line", "se_diff_twoway", "p_diff_twoway",
       "b_common", "p_common_twoway", "attenuation_lambda_split_half"]
keys = ["family", "readout", "variant", "covset", "fe"]
for f in ("d1_two_way_models.csv", "d2_screen_models.csv"):
    x, y = pd.read_csv(os.path.join(A, f)), pd.read_csv(os.path.join(B, f))
    j = x.merge(y, on=keys, suffixes=("_a", "_b"))
    print(f, "rows", len(x), len(y), "matched", len(j))
    for c in DET:
        if c + "_a" in j:
            d = np.abs(j[c + "_a"] - j[c + "_b"]) / np.maximum(np.abs(j[c + "_a"]), 1e-12)
            print(f"   {c}: max rel diff {np.nanmax(d):.2e}")
for f in ("trim72_reliability.csv", "readthrough_correction_fit.csv", "drugdose_sets.csv"):
    x, y = pd.read_csv(os.path.join(A, f)), pd.read_csv(os.path.join(B, f))
    num = x.select_dtypes("number").columns
    print(f, "shape", x.shape, y.shape, "max abs diff numeric", float(np.nanmax(np.abs(x[num].to_numpy(float) - y[num].to_numpy(float)))))
x = pd.read_csv(os.path.join(A, "analysis_cells.csv.gz"))
y = pd.read_csv(os.path.join(B, "analysis_cells.csv.gz"))
num = x.select_dtypes("number").columns
print("analysis_cells shape", x.shape, y.shape, "max abs diff numeric",
      float(np.nanmax(np.abs(x[num].to_numpy(float) - y[num].to_numpy(float)))),
      "NaN pattern equal", bool((x[num].isna().to_numpy() == y[num].isna().to_numpy()).all()))
ck = pd.read_csv(os.path.join(B, "checks.csv"))
print(ck[["check", "value"]].to_string(index=False, max_colwidth=90))
