#!/usr/bin/env python3
"""
test_analysis.py -- end-to-end test: simulate a dataset with known planted effects, run the
analysis, and assert the planted effects are recovered and the QC flags fire.

Run:
  python3 test_analysis.py            # uses the OLS engine (deterministic, no statsmodels)
  python3 test_analysis.py --engine auto

It calls make_synthetic_ct.py and analyze_mg53_qpcr.py in a temp directory, then checks:
  D1  MG53-OE lowers the p53 score in TP53-WT under the activator (~ -0.7 log2, CI excludes 0)
  D1  MG53-OE does NOT lower it in TP53-null (near 0, not significant)
  D1  the MG53 x TP53 interaction is significant and ~ +0.7 (WT-specific lowering)
  D1  MG53 knockdown RAISES the p53 score in WT under the activator (~ +0.7, opposite sign)
  D2  the planted p53-INDEPENDENT gene (KIF11) shows a significant MG53-OE effect in TP53-null
  QC  the moving reference (PPIA) is flagged unstable
  QC  at least one technical-replicate SD flag fires
  QC  undetermined / censored measurements are reported (not imputed)
  perturbation check: MG53 readout moves up with OE
"""
import argparse
import os
import sys
import tempfile
import subprocess
import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))


def run_cmd(cmd):
    print("+ " + " ".join(cmd))
    r = subprocess.run(cmd, capture_output=True, text=True)
    sys.stdout.write(r.stdout)
    if r.returncode != 0:
        sys.stderr.write(r.stderr)
        raise SystemExit(f"command failed ({r.returncode}): {' '.join(cmd)}")
    return r.stdout


def approx(a, b, tol):
    return abs(a - b) <= tol


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--engine", default="ols", choices=["auto", "ols", "mixedlm"])
    ap.add_argument("--keep", action="store_true", help="keep temp dir")
    args = ap.parse_args()

    tmp = tempfile.mkdtemp(prefix="mg53_qpcr_test_")
    ct_csv = os.path.join(tmp, "synthetic_ct.csv")
    outdir = os.path.join(tmp, "results")

    # 1) simulate
    run_cmd([sys.executable, os.path.join(HERE, "make_synthetic_ct.py"), "--out", ct_csv])

    # 2) analyse
    run_cmd([sys.executable, os.path.join(HERE, "analyze_mg53_qpcr.py"),
             "--input", ct_csv, "--outdir", outdir, "--engine", args.engine])

    # import the planted truth
    sys.path.insert(0, HERE)
    import make_synthetic_ct as syn

    checks = []

    def check(name, ok, detail=""):
        checks.append((name, bool(ok), detail))
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f" -- {detail}" if detail else ""))

    # ---------- load outputs ----------
    contrasts = pd.read_csv(os.path.join(outdir, "contrasts_all.csv"))
    d1 = pd.read_csv(os.path.join(outdir, "d1_primary.csv"))
    screen = pd.read_csv(os.path.join(outdir, "screen.csv"))
    qc_ref = pd.read_csv(os.path.join(outdir, "qc_reference_stability.csv"))
    qc_tech = pd.read_csv(os.path.join(outdir, "qc_techreps.csv"))
    qc_cens = pd.read_csv(os.path.join(outdir, "qc_censoring.csv"))
    qc_pert = pd.read_csv(os.path.join(outdir, "qc_perturbation_check.csv"))
    per_sample = pd.read_csv(os.path.join(outdir, "per_sample_dct.csv"))
    assert os.path.isfile(os.path.join(outdir, "REPORT.md")), "REPORT.md missing"

    def get(df, **kw):
        m = pd.Series(True, index=df.index)
        for k, v in kw.items():
            m &= (df[k] == v)
        return df[m]

    ACT = "p53_activator"

    # ---------- D1: p53 score, MG53-OE in WT under activator ----------
    r = get(d1, response="p53_score", contrast="MG53_in_WT", mg53="overexpression",
            treatment=ACT, time_h=24)
    check("D1 p53_score contrast exists (OE, WT, activator, 24h)", len(r) == 1,
          f"rows={len(r)}")
    if len(r) == 1:
        est = float(r["log2fc"].iloc[0]); lo = float(r["ci_low"].iloc[0]); hi = float(r["ci_high"].iloc[0])
        check("D1 MG53-OE LOWERS p53 score in WT (~ -0.7 log2)",
              approx(est, -syn.PLANTED_D1, 0.35) and est < 0,
              f"log2fc={est:+.2f} (planted {-syn.PLANTED_D1:+.2f})")
        check("D1 WT effect CI excludes 0 (significant)", hi < 0,
              f"95% CI [{lo:.2f}, {hi:.2f}]")

    # MG53-OE in null: ~0, not significant
    rn = get(d1, response="p53_score", contrast="MG53_in_null", mg53="overexpression",
             treatment=ACT, time_h=24)
    if len(rn) == 1:
        est = float(rn["log2fc"].iloc[0]); lo = float(rn["ci_low"].iloc[0]); hi = float(rn["ci_high"].iloc[0])
        check("D1 MG53-OE does NOT lower p53 score in null (~0, CI spans 0)",
              approx(est, 0.0, 0.35) and (lo < 0 < hi),
              f"log2fc={est:+.2f}, 95% CI [{lo:.2f}, {hi:.2f}]")

    # interaction significant, ~ +0.7 (null - WT)
    ri = get(d1, response="p53_score", contrast="MG53_x_TP53_interaction",
             mg53="overexpression", treatment=ACT, time_h=24)
    if len(ri) == 1:
        est = float(ri["log2fc"].iloc[0]); lo = float(ri["ci_low"].iloc[0]); hi = float(ri["ci_high"].iloc[0])
        check("D1 MG53 x TP53 interaction significant and ~ +0.7 (WT-specific lowering)",
              approx(est, syn.PLANTED_D1, 0.4) and (lo > 0),
              f"interaction log2fc={est:+.2f}, 95% CI [{lo:.2f}, {hi:.2f}]")

    # knockdown opposite sign in WT under activator
    rk = get(d1, response="p53_score", contrast="MG53_in_WT", mg53="knockdown",
             treatment=ACT, time_h=24)
    if len(rk) == 1:
        est = float(rk["log2fc"].iloc[0]); lo = float(rk["ci_low"].iloc[0])
        check("D1 MG53-KD RAISES p53 score in WT (~ +0.7, opposite of OE)",
              approx(est, syn.PLANTED_D1, 0.4) and (lo > 0),
              f"log2fc={est:+.2f}")

    # vehicle: no MG53-OE effect in WT (effect is activator-specific)
    rv = get(d1, response="p53_score", contrast="MG53_in_WT", mg53="overexpression",
             treatment="vehicle", time_h=24)
    if len(rv) == 1:
        est = float(rv["log2fc"].iloc[0]); lo = float(rv["ci_low"].iloc[0]); hi = float(rv["ci_high"].iloc[0])
        check("D1 MG53-OE has ~no effect on p53 score in WT under vehicle",
              approx(est, 0.0, 0.35) and (lo < 0 < hi),
              f"log2fc={est:+.2f}, 95% CI [{lo:.2f}, {hi:.2f}]")

    # ---------- D2: planted p53-INDEPENDENT gene KIF11 ----------
    rk2 = get(screen, response="KIF11", contrast="MG53_in_null", mg53="overexpression",
              time_h=24)
    # choose any treatment row that is significant in null
    check("D2 KIF11 has MG53_in_null contrasts", len(rk2) >= 1, f"rows={len(rk2)}")
    if len(rk2) >= 1:
        sig = rk2[(rk2["p"] < 0.05) & (rk2["log2fc"] < -0.3)]
        est = float(rk2["log2fc"].median())
        check("D2 KIF11 is p53-INDEPENDENT (significant MG53-OE effect in TP53-null)",
              len(sig) >= 1 and approx(est, -syn.PLANTED_INDEP, 0.4),
              f"median log2fc(null)={est:+.2f} (planted {-syn.PLANTED_INDEP:+.2f}), sig rows={len(sig)}")
        check("D2 KIF11 flagged p53_independent_signal",
              bool(rk2["p53_independent_signal"].any()))

    # KIF11 also present in WT (should be, since p53-independent)
    rk3 = get(screen, response="KIF11", contrast="MG53_in_WT", mg53="overexpression", time_h=24)
    if len(rk3) >= 1:
        est = float(rk3["log2fc"].median())
        check("D2 KIF11 also down in WT (p53-independent, both genotypes)",
              approx(est, -syn.PLANTED_INDEP, 0.45) and est < 0, f"median log2fc(WT)={est:+.2f}")

    # ---------- QC: moving reference ----------
    ppia = get(qc_ref, reference="PPIA")  # the planted moving reference
    check("QC moving reference row exists (PPIA)", len(ppia) == 1)
    if len(ppia) == 1:
        check("QC PPIA flagged unstable (moving reference detected)",
              bool(ppia["flag_unstable"].iloc[0]),
              f"dCt_SD_across_conditions={ppia['dCt_SD_across_conditions'].iloc[0]}, M={ppia['geNorm_M'].iloc[0]}")
    # stable references should NOT be flagged
    stable_ok = True
    for ref in ("GAPDH", "ACTB"):
        row = get(qc_ref, reference=ref)
        if len(row) == 1 and bool(row["flag_unstable"].iloc[0]):
            stable_ok = False
    check("QC stable references (GAPDH, ACTB) not flagged", stable_ok)

    # ---------- QC: technical-replicate SD flag ----------
    check("QC at least one technical-replicate SD flag fires",
          int(qc_tech["flag_sd_gt_thresh"].sum()) >= 1,
          f"n_flagged={int(qc_tech['flag_sd_gt_thresh'].sum())}")
    # the specific planted noisy triplet (A549 / MDM2) is flagged
    noisy = qc_tech[(qc_tech["cell_line"] == "A549") & (qc_tech["gene"] == "MDM2")
                    & (qc_tech["treatment"] == "vehicle") & (qc_tech["mg53"] == "control")
                    & (qc_tech["bio_rep"] == 1) & (qc_tech["time_h"] == 24)]
    check("QC the planted noisy triplet (A549/MDM2) is flagged",
          len(noisy) == 1 and bool(noisy["flag_sd_gt_thresh"].iloc[0]),
          f"ct_sd={float(noisy['ct_sd'].iloc[0]):.2f}" if len(noisy) == 1 else "row missing")

    # ---------- QC: censoring reported, never imputed ----------
    total_censored = int(qc_cens["n_censored"].sum())
    check("QC undetermined/censored measurements are reported (>0)", total_censored > 0,
          f"n_censored={total_censored}")
    # low-abundance assay TP53I3 should have censored reads
    t3 = qc_cens[qc_cens["gene"] == "TP53I3"]
    check("QC low-abundance assay TP53I3 has censored reads", t3["n_censored"].sum() > 0)
    # per_sample dCt must have NaN (not imputed) where target was censored for all reps
    check("per_sample dCt keeps NaN where censored (no silent imputation)",
          per_sample["pseudo_dct"].isna().any())

    # ---------- perturbation check ----------
    oe = qc_pert[(qc_pert["mg53"] == "overexpression") & (qc_pert["gene"] == "TRIM72_total")]
    check("perturbation check: MG53-OE raises TRIM72_total readout",
          len(oe) >= 1 and bool((oe["consistent"]).all()),
          f"median log2fc range {oe['median_log2fc'].min():+.2f}..{oe['median_log2fc'].max():+.2f}")

    # ---------- summary ----------
    n_pass = sum(1 for _, ok, _ in checks if ok)
    n = len(checks)
    print(f"\n=== {n_pass}/{n} checks passed ===")
    if not args.keep:
        import shutil
        shutil.rmtree(tmp, ignore_errors=True)
    else:
        print(f"temp dir kept at {tmp}")
    if n_pass != n:
        failed = [name for name, ok, _ in checks if not ok]
        raise SystemExit("FAILED checks: " + "; ".join(failed))
    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    main()
