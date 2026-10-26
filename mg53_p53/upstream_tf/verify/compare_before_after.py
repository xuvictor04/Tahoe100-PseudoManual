"""Compare every table of upstream_tf before the verifier fixes (git 48669fd, extracted to verify/before/tables) with
the tables of the from-scratch rerun (tables/). Per table: rows / columns added or removed, and per shared numeric
column the number of matched rows that changed (beyond float-format rounding) and the largest change.

    python3 compare_before_after.py [before_tables_dir] [after_tables_dir]
"""
import json
import os
import sys

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
BEF = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "before", "tables")
AFT = sys.argv[2] if len(sys.argv) > 2 else os.path.join(os.path.dirname(HERE), "tables")
KEYS = {"a0_readthrough_fit.csv": ["predictor"], "a0_regulon_sizes.csv": ["source", "tf"],
        "a0_regulons_used.csv.gz": ["source", "tf", "target"], "a0_tf_edges_to_trim72_locus.csv": ["source", "tf", "target"],
        "a1_dd_tf_vs_trim72.csv.gz": ["source", "tf", "trim72_version", "variant"],
        "a1_matched_genes_reference.csv": ["trim72_version", "variant"], "a1_pc_variance.csv": ["pc"],
        "a1_tf_activity_by_drugdose.csv.gz": ["drug", "conc"], "a1a2_tf_summary.csv": ["tf"],
        "a2_within_line_tf_vs_trim72.csv.gz": ["tf", "trim72_version", "covset"],
        "a3_tp53_positive_control.csv": ["test", "tf_activity", "readout"], "a4_muscle_promoter_tfs.csv": ["tf"],
        "b1_line_outcomes.csv": ["cell_line_id"], "b2_line_feature_tests.csv": ["outcome", "family", "feature"],
        "b3_baseline_tf_activity_per_line.csv": ["cell_line_id"], "checks.csv": ["check", "plate"],
        "key_results.csv": ["section", "what"], "a1_regulon_overlap_control.csv": ["tf", "variant"],
        "a1_plate_batch_split.csv": ["source", "tf", "subset"], "a2_noise_ceiling_genes.csv": ["gene", "trim72_version",
                                                                                                "covset"]}


def load(p):
    return pd.read_csv(p, low_memory=False)


def changed(a, b):
    """Changed beyond the rounding of the tables' float formats (%.4g / %.5g / %.6g): relative 2e-4 or absolute
    1e-10; NaN vs number counts as a change."""
    a, b = a.astype(float), b.astype(float)
    both_nan = np.isnan(a) & np.isnan(b)
    one_nan = np.isnan(a) ^ np.isnan(b)
    with np.errstate(invalid="ignore"):
        d = np.abs(a - b) > np.maximum(2e-4 * np.maximum(np.abs(a), np.abs(b)), 1e-10)
    return (d & ~both_nan) | one_nan


def main():
    files = sorted(set(os.listdir(BEF)) | set(os.listdir(AFT)))
    for f in files:
        pb, pa = os.path.join(BEF, f), os.path.join(AFT, f)
        if not os.path.exists(pb):
            print(f"\n## {f}: NEW ({os.path.getsize(pa) / 1e6:.2f} MB)")
            continue
        if not os.path.exists(pa):
            print(f"\n## {f}: REMOVED")
            continue
        if f.endswith(".txt"):
            print(f"\n## {f}: {'identical' if open(pb).read() == open(pa).read() else 'text changed'}")
            continue
        if f.endswith(".json"):
            jb, ja = json.load(open(pb)), json.load(open(pa))
            print(f"\n## {f}: " + "; ".join(f"{k}: {jb.get(k)} -> {ja.get(k)}" for k in sorted(set(jb) | set(ja))
                                            if jb.get(k) != ja.get(k)))
            continue
        B, A_ = load(pb), load(pa)
        key = [k for k in KEYS.get(f, []) if k in B.columns and k in A_.columns]
        print(f"\n## {f}: rows {len(B)} -> {len(A_)}; columns {B.shape[1]} -> {A_.shape[1]}")
        cb, ca = set(B.columns), set(A_.columns)
        if ca - cb:
            print("   columns added: " + ", ".join(sorted(ca - cb)))
        if cb - ca:
            print("   columns removed: " + ", ".join(sorted(cb - ca)))
        if not key:
            continue
        for d_ in (B, A_):
            for k in key:
                d_[k] = d_[k].astype(str)
        B = B.drop_duplicates(key).set_index(key)
        A_ = A_.drop_duplicates(key).set_index(key)
        only_b, only_a = B.index.difference(A_.index), A_.index.difference(B.index)
        if len(only_b):
            print(f"   rows only before: {len(only_b)} (e.g. {list(only_b[:6])})")
        if len(only_a):
            print(f"   rows only after: {len(only_a)} (e.g. {list(only_a[:6])})")
        common = B.index.intersection(A_.index)
        out = []
        for c in sorted(cb & ca):
            if c in key:
                continue
            xb, xa = B.loc[common, c], A_.loc[common, c]
            if pd.api.types.is_numeric_dtype(xb) and pd.api.types.is_numeric_dtype(xa):
                ch = changed(xb.to_numpy(), xa.to_numpy())
                if ch.any():
                    with np.errstate(invalid="ignore"):
                        dmax = np.nanmax(np.abs(xb.to_numpy(float) - xa.to_numpy(float)))
                    out.append(f"{c}: {int(ch.sum())}/{len(common)} changed (max |diff| {dmax:.3g})")
            else:
                ch = (xb.astype(str) != xa.astype(str)).to_numpy()
                if ch.any():
                    out.append(f"{c}: {int(ch.sum())}/{len(common)} text changed")
        print("   " + ("\n   ".join(out) if out else f"all {len(common)} shared rows identical in the shared columns"))


if __name__ == "__main__":
    main()
