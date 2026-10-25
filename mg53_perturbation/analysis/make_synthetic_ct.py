#!/usr/bin/env python3
"""
make_synthetic_ct.py -- simulate a realistic MG53 (TRIM72) perturbation qPCR dataset with
KNOWN planted effects, so analyze_mg53_qpcr.py can be tested against ground truth.

Planted ground truth (all sizes in log2 / cycles; qPCR: higher Ct = less RNA):
  - DESIGN: TP53-WT lines {A549, RKO, NCI-H460} and TP53-null lines {MIA PaCa-2, PANC-1,
    SW480}; mg53 in {control, overexpression, knockdown}; treatment in
    {vehicle, p53_activator, idarubicin}; one time point 24 h (plus a quieter 6 h);
    bio_rep 1-3; tech_rep 1-3.
  - D1 (primary): MG53 overexpression LOWERS p53 targets by PLANTED_D1 = 0.7 log2 in TP53-WT
    under the p53 activator ONLY (not in vehicle, not in TP53-null). Knockdown RAISES them by
    0.7 log2 in the same cell. => log2fc(MG53_in_WT, activator) ~ -0.7, log2fc(MG53_in_null)
    ~ 0, interaction (null-WT) ~ +0.7.
  - D2 screen: KIF11 is p53-INDEPENDENT: MG53-OE lowers it by PLANTED_INDEP = 0.6 log2 in BOTH
    TP53-WT and TP53-null, in every treatment. (SLC7A11 is planted p53-dependent & opposite:
    rises with MG53-OE in WT only, a secondary check.)
  - A MOVING REFERENCE: PPIA shifts +PLANTED_REF_SHIFT = 1.5 cycles (expression down) under
    idarubicin in all lines -> must trip the reference-stability flag. GAPDH, ACTB stable.
  - UNDETERMINED Cts: low-abundance assays (TP53I3, CHAC1, FUS-TRIM72 intergenic) drop out in
    a fraction of samples; plus a handful of forced undetermined reads.
  - A NOISY technical triplet: one (sample, gene) gets tech-rep SD > 0.3 cycles to trip the
    technical-replicate QC flag.

Output: a tidy CSV with columns
  sample, cell_line, tp53, mg53, treatment, time_h, bio_rep, tech_rep, gene, ct, mg53_check

Only numpy / pandas are used. Deterministic given --seed.
"""
import argparse
import numpy as np
import pandas as pd

PLANTED_D1 = 0.7          # log2, MG53-OE lowers p53 targets in WT under activator
PLANTED_INDEP = 0.6       # log2, KIF11 lowered by MG53-OE regardless of TP53 (p53-independent)
PLANTED_SLC = 0.6         # log2, SLC7A11 raised by MG53-OE in WT only (p53-repressed target)
PLANTED_REF_SHIFT = 1.5   # cycles, PPIA moves under idarubicin (unstable reference)
PLANTED_ACT_INDUCTION = 2.0  # log2, p53 targets induced by activator/idarubicin in WT

WT_LINES = ["A549", "RKO", "NCI-H460"]
NULL_LINES = ["MIA PaCa-2", "PANC-1", "SW480"]
MG53_LEVELS = ["control", "overexpression", "knockdown"]
TREATMENTS = ["vehicle", "p53_activator", "idarubicin"]
TIMES = [6, 24]
BIO_REPS = [1, 2, 3]
TECH_REPS = [1, 2, 3]

REFERENCES = ["GAPDH", "ACTB", "PPIA"]
# p53 positive targets (rise on p53 activation; fall if MG53 lowers p53)
P53_TARGETS = ["MDM2", "CDKN1A", "FDXR", "ZMAT3", "DDB2", "TP53I3",
               "BBC3", "RRM2B", "SESN1", "GDF15"]
# screen / other
SCREEN = ["NFKBIA", "TNFAIP3", "KIF11", "CCND1", "SLC7A11", "GPX4", "BAX", "MCL1"]
MG53_READOUT = ["TRIM72_total", "TRIM72_endogenous"]
STRESS = ["ATF3", "FOS"]

# base Ct (DMSO, control, WT): lower Ct = higher abundance. Low-abundance assays near the
# detection limit so some reads come back undetermined.
BASE_CT = {
    "GAPDH": 16.0, "ACTB": 17.0, "PPIA": 20.0,
    "MDM2": 22.0, "CDKN1A": 23.0, "FDXR": 26.0, "ZMAT3": 24.0, "DDB2": 23.5,
    "TP53I3": 31.0, "BBC3": 25.0, "RRM2B": 23.0, "SESN1": 23.0, "GDF15": 24.0,
    "NFKBIA": 22.0, "TNFAIP3": 24.0, "KIF11": 24.0, "CCND1": 22.0,
    "SLC7A11": 23.0, "GPX4": 22.0, "BAX": 25.0, "MCL1": 21.0,
    "TRIM72_total": 30.0, "TRIM72_endogenous": 30.5,
    "ATF3": 22.0, "FOS": 22.0,
}
LOW_ABUNDANCE = {"TP53I3", "CHAC1", "FUS-TRIM72 intergenic"}  # extra dropout


def log2_expr_change(gene, cell_line, tp53, mg53, treatment):
    """Planted log2 expression change (positive = MORE RNA = lower Ct) relative to the
    WT/control/vehicle baseline of that gene. This is the ground truth the analysis must
    recover (after dCt/ddCt normalisation and sign conventions)."""
    d = 0.0
    is_wt = (tp53 == "WT")
    activated = treatment in ("p53_activator", "idarubicin")

    # p53 activation induces p53 targets in WT only
    if gene in P53_TARGETS and is_wt and activated:
        d += PLANTED_ACT_INDUCTION
    # SLC7A11 is p53-REPRESSED: activation lowers it in WT
    if gene == "SLC7A11" and is_wt and activated:
        d -= 1.0

    # D1: MG53 lowers p53 output in WT under activator (OE down, KD up); p53 targets only
    if gene in P53_TARGETS and is_wt and treatment == "p53_activator":
        if mg53 == "overexpression":
            d -= PLANTED_D1
        elif mg53 == "knockdown":
            d += PLANTED_D1
    # SLC7A11: p53-dependent de-repression -> rises with MG53-OE in WT only
    if gene == "SLC7A11" and is_wt:
        if mg53 == "overexpression":
            d += PLANTED_SLC
        elif mg53 == "knockdown":
            d -= PLANTED_SLC

    # D2 p53-INDEPENDENT: KIF11 lowered by MG53-OE in BOTH genotypes, all treatments
    if gene == "KIF11":
        if mg53 == "overexpression":
            d -= PLANTED_INDEP
        elif mg53 == "knockdown":
            d += PLANTED_INDEP

    # MG53 readout: overexpression raises it strongly, knockdown lowers it; stress raises it
    if gene in MG53_READOUT:
        if mg53 == "overexpression":
            d += 3.0
        elif mg53 == "knockdown":
            d -= 2.0
        if treatment == "idarubicin":
            d += 3.6
        if gene == "TRIM72_endogenous" and mg53 == "overexpression":
            d -= 3.0  # a CDS-only OE construct does not raise the endogenous 3'UTR readout

    # stress markers rise under idarubicin (genotype-independent)
    if gene in STRESS and treatment == "idarubicin":
        d += 1.5

    return d


def reference_shift(gene, treatment):
    """Planted reference instability: PPIA moves up (less RNA) under idarubicin."""
    if gene == "PPIA" and treatment == "idarubicin":
        return PLANTED_REF_SHIFT  # cycles added to Ct (expression down)
    return 0.0


def main():
    ap = argparse.ArgumentParser(description="Simulate MG53 qPCR Ct data with planted effects.")
    ap.add_argument("--out", required=True, help="output CSV path")
    ap.add_argument("--seed", type=int, default=20251025)
    ap.add_argument("--tech-sd", type=float, default=0.08, help="technical replicate Ct SD")
    ap.add_argument("--bio-sd", type=float, default=0.12, help="biological replicate Ct SD")
    args = ap.parse_args()
    rng = np.random.default_rng(args.seed)

    genes = REFERENCES + P53_TARGETS + SCREEN + MG53_READOUT + STRESS
    lines = [(c, "WT") for c in WT_LINES] + [(c, "null") for c in NULL_LINES]
    # small per-line baseline offsets (biology varies between lines)
    line_offset = {c: rng.normal(0, 0.3) for c, _ in lines}

    rows = []
    for cell_line, tp53 in lines:
        for mg53 in MG53_LEVELS:
            for treatment in TREATMENTS:
                for time_h in TIMES:
                    # planted effects only matter at 24 h (6 h is an early, quiet time point)
                    eff_scale = 1.0 if time_h == 24 else 0.15
                    for bio_rep in BIO_REPS:
                        bio_noise = {g: rng.normal(0, args.bio_sd) for g in genes}
                        sample = f"{cell_line}|{tp53}|{mg53}|{treatment}|{time_h}h|r{bio_rep}"
                        for gene in genes:
                            base = BASE_CT[gene] + line_offset[cell_line]
                            dexpr = eff_scale * log2_expr_change(gene, cell_line, tp53, mg53, treatment)
                            ct_center = base - dexpr + reference_shift(gene, treatment) + bio_noise[gene]
                            for tech_rep in TECH_REPS:
                                ct = ct_center + rng.normal(0, args.tech_sd)
                                rows.append([sample, cell_line, tp53, mg53, treatment,
                                             time_h, bio_rep, tech_rep, gene, round(ct, 3)])

    df = pd.DataFrame(rows, columns=["sample", "cell_line", "tp53", "mg53", "treatment",
                                     "time_h", "bio_rep", "tech_rep", "gene", "ct"])

    # ---- undetermined / high-Ct censoring (reported, never imputed) ----
    # low-abundance assays drop out stochastically
    low_mask = df["gene"].isin(LOW_ABUNDANCE)
    drop = low_mask & (rng.random(len(df)) < 0.25)
    df.loc[drop, "ct"] = np.nan
    # a few forced undetermined reads scattered anywhere
    force = rng.choice(df.index, size=12, replace=False)
    df.loc[force, "ct"] = np.nan
    # anything the simulator pushed above 40 is reported as Undetermined too
    df.loc[df["ct"] > 40, "ct"] = np.nan

    # ---- a deliberately noisy technical triplet (trips tech-rep SD flag) ----
    noisy = ((df["cell_line"] == "A549") & (df["tp53"] == "WT") & (df["mg53"] == "control")
             & (df["treatment"] == "vehicle") & (df["time_h"] == 24) & (df["bio_rep"] == 1)
             & (df["gene"] == "MDM2"))
    idx = df.index[noisy]
    if len(idx) >= 3:
        df.loc[idx, "ct"] = df.loc[idx, "ct"].values + np.array([-0.6, 0.0, 0.7])[:len(idx)]

    # ---- optional perturbation check column (echoes the intended MG53 state) ----
    df["mg53_check"] = df["mg53"].map({"control": "ctrl", "overexpression": "OE+",
                                       "knockdown": "KD-"})
    # render Ct: numbers rounded, NaN -> 'Undetermined'
    df["ct"] = df["ct"].map(lambda x: "Undetermined" if (x is None or (isinstance(x, float) and np.isnan(x)))
                            else round(float(x), 3))

    df.to_csv(args.out, index=False)
    n_undet = int((df["ct"] == "Undetermined").sum())
    print(f"[make_synthetic_ct] wrote {len(df)} rows to {args.out} "
          f"({df['gene'].nunique()} genes, {df[['cell_line','mg53','treatment','time_h','bio_rep']].drop_duplicates().shape[0]} samples, "
          f"{n_undet} undetermined)")
    # also return the planted ground truth for the test harness
    return {
        "PLANTED_D1": PLANTED_D1, "PLANTED_INDEP": PLANTED_INDEP, "PLANTED_SLC": PLANTED_SLC,
        "PLANTED_REF_SHIFT": PLANTED_REF_SHIFT, "moving_reference": "PPIA",
        "p53_independent_gene": "KIF11",
    }


if __name__ == "__main__":
    main()
