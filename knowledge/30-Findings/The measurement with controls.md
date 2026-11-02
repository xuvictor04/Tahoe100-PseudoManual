---
type: finding
tags: [finding, measurement, controls, effect-size, power]
status: current
---

# The measurement with controls

The study's central number: **how much the p53 program moves per doubling of measured MG53 mRNA, in cell
lines that have working p53, measured against an arm of lines that cannot make p53 at all.**

The answer is zero to within a few tenths of a percent, and — more informative than the estimate — the
knockout-like control arm carries *as much* residual association as the functional arm, so no slope of this
size in this design can be read as a p53 effect.

> [!warning] This note's intervals are wider than the committed README's, on purpose
> `mg53_p53/findings/README.md` and `mg53_p53/findings/tables/mg53_to_p53_effect.csv` quote CR0
> cluster-robust SEs on cell line with a 1.96 multiplier. The reanalysis in the authoritative write-up uses
> a **two-way (drug, line) CR1 cluster-robust SE on a *t* with min(drugs, lines) − 1 = 10 df**, and a
> **whole-line exposure permutation** null in place of the within-drug-dose shuffle. Those intervals are
> 12–58% wider, and **where the committed text says an interval excludes zero and this note says it does
> not, this note is right.** Three such reversals are listed below under
> [[#Three intervals that no longer exclude zero]]. See [[Corrections and retractions]].

## The design

[[Tahoe-100M]] contains no engineered p53 knockout and no MG53 perturbation, so the effect has to be
identified from line-to-line variation *inside* a drug-dose, and the control has to come from genotype.
Both cell-line and drug-dose means are removed from outcome and exposure before one slope is fitted per arm
([[Two-way fixed effects]]), so only residual co-variation is used: for a given line under a given
drug-dose, does p53 output deviate from expectation in the direction MG53 does?

- **Outcome** — `P_r2_mean`, the data-defined [[p53 program P]] score (180 genes here) for that
  line × drug-dose, in log2. See [[Program P derivation]].
- **Exposure** — `r2_mean`, [[TRIM72]]'s corrected log2 fold change for the same cell.

| Arm | Definition | Lines | Rows (all drug-doses) |
|---|---|---|---|
| A functional p53 | the genotype-blind panel calls them responsive; all TP53 wild-type | 11 | 12,448 |
| B WT, not fully responsive | TP53 wild-type by sequence, functionally damped | 6 | 6,784 |
| B2 mutant, some activity | one line (J82) — too few clusters to fit, excluded | 1 | — |
| C low-activity mutant | retains ≤ 0.15 of the wild-type-minus-null gap (pseudo-control) | 21 of 22 | 21,652 |
| **D p53-null CONTROL** | **truncating / splice-disrupted / whole-gene deletion** | **10** | **11,315** |

Arm assignment comes from `mg53_p53/findings/tables/per_line_p53_state.csv`
(`functional_call`, `ind_P_mean_frac_of_WT_gap`) — see [[Per-line p53 function]] — and arm D from
`mg53_p53/findings/tables/null_reference_lines.csv`, `role = "null reference (core)"`.

### Why arm D is knockout-like

The ten core null-reference lines — AsPC-1, COLO 205, SNU-423, KATO III, HOP62, NCI-H1792, Panc 03.27,
RPMI-7951, SW1417, SW 900 — have **no intact TP53 allele to transcribe**; KATO III is a whole-gene deletion,
the rest are frameshifts, nonsense codons or disrupted splice sites. They cannot mount a p53 response, so
any MG53 → p53-activity slope measured in them is produced by something that is not p53. That is what a
knockout arm buys: it turns an uninterpretable association into a subtractable one. See
[[p53 nullification in cancer cell lines]].

Arm D is also the **only outcome-independent arm**. A, B and C are cut on thresholds applied to a line-level
summary of the very program score that is the outcome — a circularity the design does not escape
([[Cross-fitting and circularity]]) — while D is defined by genotype alone.

Three further truncating-class lines are deliberately **held out** of the core arm, each because some
full-length p53 could survive: AN3 CA (`p.S90fs` plus missense `p.R213Q` and `p.G389W`), HCT15 (splice site
plus the DNA-contact hotspot `p.S241F`), and NCI-H2347 (`p.T125T`, synonymous at the exon-4 donor and
splice-affecting) [`null_reference_lines.csv`, `role = "truncating class, flagged mixed"` and the
`why flagged` rows].

### The control is demonstrably competent

A negative control is only worth as much as its ability to show a difference. Taking a p53-activating
drug-dose minus the rest, per line:

| Read-out | Arm A (functional) | Arm D (p53-null) | Ratio |
|---|---|---|---|
| data-defined program P | **+0.17043 log2 = +12.54%**, all 11 lines between +0.1033 and +0.2030 | +0.01878 = +1.31% | ~10× |
| curated 21-gene p53 panel | **+0.31691 = +24.57%** | +0.00307 = +0.21% | ~100× |

[authoritative write-up, `w2_positive_control.csv` rows 0–4, recomputed]

So the arms differ by roughly **10× (program) to 100× (panel) in p53 competence**, and a p53-mediated MG53
effect of any appreciable size would have appeared as an A-versus-D difference. None does. The caveat on
reading this as power: it assumes a doubling of MG53 ought to move p53 output on a scale comparable to a
drug-induced p53 response. That is a scale assumption, not a power calculation.

**Arm B is a second, within-genotype control.** It is TP53 wild-type by sequence exactly as arm A is, yet its
slope has the opposite sign (−0.00131 against +0.00137 over all drug-doses), which bounds how much of any
A-versus-D gap is p53 competence rather than arm-level noise.

## The headline

> [!important] In the 11 functional-p53 lines, a doubling of **measured** MG53 moves program P by
> **+0.00137 log2 = +0.095% of p53 activity, 95% CI −0.161% to +0.352%**, across all 1,132 drug-doses
> (12,448 line × drug-dose rows). Whole-line permutation p = 0.387; two-way clustered p = 0.427.

Per doubling of **true** MG53 — dividing by the TP53-wild-type exposure reliability 0.301
([[Reliability and disattenuation]]) — the same estimate reads **+0.317% (−0.533% to +1.174%)**.

Nothing in that interval is distinguishable from zero under any inference method tried, including a
restricted wild cluster bootstrap on the 11 lines: p = 0.394, CI −0.00243 to +0.00517 log2
[`w1_arm_slopes.csv` row 0, `p_wcb`/`lo_wcb`/`hi_wcb`, recomputed].

### The permutation null behind the interval

Two nulls disagree, and the difference matters more than the p-values do ([[Nulls and calibration]]).

| Null | How it is built | Behaviour |
|---|---|---|
| within-drug-dose exposure shuffle, 2,000 draws | raw MG53 permuted across lines inside a drug-dose | **too tight** — null SD 0.47× the quoted SE in arm A, 0.19× in C, 0.80× in D |
| **whole-line exposure permutation, 1,000 draws** | each line's entire MG53 trajectory reassigned to another line of the same arm | **calibrated** — null SD 0.94× (A), 0.54× (C), 0.90× (D); mean within 5e-5 of zero |

The shuffle destroys the line-level structure the line fixed effect would otherwise absorb, so the permuted
exposure carries more residual variance than the real one and the null comes out narrow. The whole-line
permutation keeps each trajectory intact and reproduces the clustered SE. **Read the line permutation; treat
the shuffle p with suspicion.** An analytic p alone is not evidence here in any case: the pipeline's own
calibration shows observed λ 4.44 against matched-placebo medians 5.52 and 4.69
[`genome_wide/tables/c_calibration.csv`] — see [[FDR calibration and the inflated null]].

## Main table — program P, all 1,132 drug-doses / 379 drugs

Slope = log2 of the outcome per doubling of measured MG53. CI = two-way (drug, line) CR1 cluster on *t*,
10 df. MDE80 = smallest detectable change at 80% power with the few-cluster multiplier
*t*(.975,df) + *t*(.80,df) = 3.11.

| Arm | Lines | Slope | 95% CI | Change in p53 activity | Shuffle p | Line-perm p | MDE80 |
|---|---|---|---|---|---|---|---|
| A functional p53 | 11 | +0.00137 | −0.00232, +0.00506 | +0.095% (−0.161, +0.352) | 0.080 | 0.387 | +0.357% |
| B WT, damped | 6 | −0.00131 | −0.00500, +0.00239 | −0.091% (−0.346, +0.165) | 0.280 | 0.459 | +0.348% |
| C low-activity mutant | 21 | +0.00438 | −0.00032, +0.00908 | +0.304% (−0.022, +0.632) | 0.0005 | 0.0010 | +0.461% |
| **D p53-null CONTROL** | 10 | +0.00065 | −0.00061, +0.00190 | +0.045% (−0.042, +0.132) | 0.138 | 0.189 | +0.121% |
| **A − D (knockout-controlled)** | 21 | **+0.00073** | **−0.00280, +0.00425** | **+0.050% (−0.194, +0.295)** | 0.426 | 0.665 | **+0.346%** |

## Main table — program P, p53-activating drug-doses only (142 drug-doses / 98 drugs)

| Arm | Lines | Slope | 95% CI | Change in p53 activity | Shuffle p | Line-perm p | MDE80 |
|---|---|---|---|---|---|---|---|
| A functional p53 | 11 | −0.00178 | −0.01242, +0.00886 | −0.123% (−0.857, +0.616) | 0.646 | 0.752 | +1.034% |
| C low-activity mutant | 21 | +0.00619 | −0.00131, +0.01370 | +0.430% (−0.091, +0.954) | 0.0005 | 0.030 | +0.738% |
| **D p53-null CONTROL** | 10 | +0.00324 | −0.00149, +0.00796 | +0.225% (−0.103, +0.553) | 0.059 | 0.055 | +0.456% |
| **A − D** | 21 | **−0.00502** | **−0.01471, +0.00467** | **−0.347% (−1.014, +0.324)** | 0.234 | 0.392 | **+0.953%** |

This is the scope where p53 is actually being driven, and it is where the control misbehaves most plainly:
**arm D's slope exceeds arm A's, and the contrast flips sign.** Row-by-row figures come from
`mg53_p53/findings/tables/mg53_to_p53_effect.csv` (point estimates, `n_rows`, `n_lines`) with the intervals
and the permutation columns from the reanalysis.

Note also what is *not* carried here: in the third scope, the 23 drug-doses where MG53 itself moves
(|exposure z| ≥ 3), A − D = −0.0327 (CI −0.0608 to −0.0045, two-way p 0.025) on 252 arm-A rows — the only
nominally significant knockout-controlled contrast, and negative. Per-drug leave-one-out keeps it between
−0.0306 and −0.0380 across the scope's 20 drugs, and the arm's median cell count there is *higher* than its
overall median, so neither one drug nor cytotoxicity explains it. The grounds for calling it suggestive
rather than a finding are multiplicity and a 23-drug-dose, 11-line base.

## The knockout-controlled contrast A − D

This is the only p53-attributable quantity the design produces.

- **All drug-doses: +0.00073 log2 = +0.050% of p53 activity per doubling of measured MG53 (95% CI −0.194%
  to +0.295%)**, two-way p 0.672, whole-line permutation p 0.665, within-drug-dose shuffle p 0.426, wild
  cluster bootstrap on the 21 lines p 0.666 with CI −0.00300 to +0.00445. MDE80 +0.346% (+0.329% with the
  normal multiplier).
- **p53-activating drug-doses: −0.00502 = −0.347% (−1.014% to +0.324%)**, two-way p 0.293, line-permutation
  p 0.392. MDE80 +0.953%.
- Per doubling of **true** MG53, disattenuated **arm by arm** (b_A/0.301 − b_D/0.283, because reliability is
  group-specific): **+0.00228 log2 = +0.158%**, detection limit +1.155%. A single shared divisor gives
  +0.174%, which is 10% too large.

The contrast is fitted **jointly**, with (drug-dose × arm) fixed-effect cells and arm-specific slopes, so its
covariance is correct under drug clustering. Adding two SEs in quadrature — as the first pass did — is valid
only under cell-line clustering, where the arms share no line and the covariance is exactly zero
[`mg53_to_p53_effect.csv` rows 4 and 31; `w1_contrast.csv`, recomputed].

### Did the control behave as a control should? No.

A clean negative control would sit near zero while the functional arm did not. Instead:

- Over all drug-doses the control carries about as much residual association as the functional arm. On the
  comparable scale — **partial correlation**, which removes arm D's program score having only 0.0286 of
  residual spread against arm A's 0.0516 — arm D is **+0.0189 against arm A's +0.0214, i.e. 88% of it.** The
  raw slope ratio of 47% is a scale artifact, not a measure of relative signal.
- In the p53-activating scope the control (+0.00324) **exceeds** the arm it is meant to control for
  (−0.00178), and the contrast flips sign.
- Arm C — lines with essentially no p53 — carries the largest slope in the whole design (+0.00438).

Every one of those orderings is a comparison of point estimates whose contrast interval spans zero, so none
is a demonstrated inequality. Together they say the measured association is **not p53-mediated**.

## What the design could have detected

| Quantity | Value | As a fraction of the drug-induced p53 response |
|---|---|---|
| MDE80, arm A, measured MG53, few-cluster multiplier | **+0.357%** per doubling | 3.0% of the +0.1704 log2 (+12.5%) arm A shows to a p53-activating drug-dose |
| MDE80, arm A, normal multiplier on the same CR1 SE | +0.322% | 2.7% |
| MDE80, arm A, per doubling of **true** MG53 (÷ 0.301) | +1.194% | **10.0%** |
| MDE80, A − D contrast | +0.346% (true-MG53: +1.155%) | 2.9% (9.7%) |

Fractions are taken in log2 against arm A's **+0.17043 log2** response to a p53-activating drug-dose;
the arm-A rows are the write-up's own (3.0% / 10.0%), the A − D rows are that same division carried out
here.

The committed `mde_pct` column reads +0.290% for arm A because it applies 2.802 to the narrower CR0 SE; the
figure to quote is +0.357%. Either way the claim the study is entitled to make is a **bound**: effects larger
than roughly a third of a percent of p53 activity per doubling of measured MG53 are excluded, which is a few
per cent of what a p53-activating drug does to the same cells. That is the number behind the vault's headline
in [[What this study found]].

## Three intervals that no longer exclude zero

| Where | Committed README / CSV | Reanalysis (correct) |
|---|---|---|
| arm C, all drug-doses | +0.304% (+0.022, +0.587) | +0.304% (**−0.022**, +0.632) |
| arm C, p53-activating | +0.430% (+0.048, +0.814) | +0.430% (**−0.091**, +0.954) |
| arm D, p53-activating | +0.225% (+0.007, +0.443) | +0.225% (**−0.103**, +0.553) |

Arm C is nonetheless a **real residual association**, and the reason to call it non-p53 is mechanism, not
inference: under the calibrated whole-line permutation it is p 0.0010, Holm 0.008 over the pre-specified
family of 10, and the wild cluster bootstrap gives p 0.038 with an interval excluding zero. It is only the
two-way clustered *t* (p 0.066) that does not reach significance — and under that inference **nothing** in
the family survives multiplicity (min Holm 0.662, min BH 0.503). The pre-specified family is 10 tests:
program P × four arms plus the contrast × two scopes.

## Why the control arm has a slope at all

Summarised here, developed in [[Downstream of MG53]] and [[Why MG53 is hard to measure here]]:

1. **MG53 tracks generic response amplitude and its own 3′ neighbourhood, not p53** — and does so just as
   strongly where p53 is absent. Standardised by each outcome's residual spread, MG53's residual association
   in arm A is 5.75× larger with a 5-gene stress/ISR set than with program P and 4.12× larger with the FUS
   readthrough score; in arm D the same ratios are 5.98× and 3.56×, and a three-gene housekeeping score
   beats program P by 2.95×. [[TRIM72]] sits 3′ of [[FUS]] and [[PYCARD-AS1]] on the same strand, so part of
   the measured exposure is [[Readthrough spillover]] — and FUS is the only atlas member of that overlay
   set, so its share is a floor. See [[The TRIM72 locus]].
2. **The association lives inside a single well — the winning explanation.** On the 108 drug-doses with two
   usable wells (4,974 paired cells), a single-well exposure on both sides gives arm C same-well +0.00683
   (CI +0.00018, +0.01348) against **cross-well −0.00213 (−0.00581, +0.00154)**; arm D same-well +0.00386
   (−0.00063, +0.00835) against **cross-well −0.00133 (−0.00477, +0.00212)**; arm A +0.01719 against
   −0.01226. Independent measurement error attenuates both estimators identically, so the gap isolates error
   **correlated between exposure and outcome inside one profile**, and every cross-well estimate is at or
   below zero. No fixed effect can remove it: a well fixed effect is a per-well, not a per-(line × well),
   projection, which is why moving from drug-dose to well fixed effects only halves the slopes (arm A
   +0.00349 → +0.00142, arm D +0.00109 → +0.00066, 57,726 rows) instead of eliminating them.
3. **Breaking the shared normalisation collapses the point estimate.** Pairing the `r2` exposure with a
   differently normalised outcome moves arm A from +0.00137 to +0.00026 (`u_drugmedian` outcome) to −0.00031
   (`u_dmso` outcome), and A − D from +0.00073 to +0.00012 to −0.00053. **The sign of the headline is not
   robust to that change.** Arm C rises instead (+0.00549, +0.00607), so for arm C the shared *correction* is
   not the channel even though the shared *well* is.
4. **A positive slope of this size in TP53-altered lines is what any matched gene gives.** 97.5% of 200
   expression- and response-matched placebo exposures have a positive altered-line slope, placebo mean
   +0.00227 against MG53's +0.00223 — see [[Placebo genes and reference families]]. Those fits are on the
   TP53 *genotype* split (17 WT against 30 altered), so they bound whether MG53 is special at genotype level
   and say nothing directly about A − D.

Two claims that have been offered and are **not** endorsed: that residual composition noise is ruled out
(controlling for `composition_shift_mean` removes about a quarter of arm A's slope, so it is a real if
partial channel), and that arm C's slope dissolves under better inference (it does not, as above).

## What this cannot establish

- **Association, not perturbation.** There is no MG53 perturbation in Tahoe-100M. Every number here is
  residual co-variation across cell lines within a drug-dose, 24 h after treatment. Direction of effect is
  not identified.
- **mRNA, not protein.** The exposure is a transcript count for a gene whose product acts largely
  post-translationally; there is no protein measurement in the data. See [[MG53 (TRIM72)]].
- **The effective sample is small where it counts.** 49 of 50 lines enter (NCI-H661 has `expressed = False`
  in all 1,132 drug-doses); 11 and 10 lines in the two arms of the contrast; a 6-to-21-cluster inference
  problem throughout. 48,249 of 53,331 usable (drug-dose, line) cells rest on a single well (90.5%), with a
  median of 5 UMIs for TRIM72 [`export/TRIM72/TRIM72_per_drugdose_line.csv`, `n_wells_r2`,
  `umi_count_sum`].
- **Disattenuation is a bound on precision, not a correction of the estimate.** Full-data split-half
  reliability is 0.289 (0.301 in wild-type lines, 0.283 in altered, 0.114 for a single well). The classical
  1/reliability correction needs exposure and outcome errors to be independent — and the cross-well test
  above shows the association is same-well only, which is precisely the case where that fails. Read "per
  doubling of true MG53" as a statement about how loose the bound is.
- **Scope-matched reliability for the p53-activating set does not exist.** 0.585 belongs to the 50
  drug-doses with curated P53_ACTIVITY z ≥ 3 and 0.706 to the 23 MG53-moving ones; neither is the
  142-drug-dose `in_S2_p53_activating` set. The true-MG53 scaling of the p53-activating estimates is
  therefore **unverified**.
- **Arm membership is outcome-dependent for A, B and C.** The clean fix — define arms on one half of the
  drug-doses, estimate on the other — was not run.
- **Two sub-claims could not be reproduced** and are marked unverified: a 7× asymmetry in per-arm
  single-well exposure reliability (A 0.117 / C 0.052 / D 0.016), where the paired-well recomputation gives
  a uniformly low 0.134 / 0.106 / 0.091 against the repo's pooled 0.114; and the claim that arm D's
  p53-activating slope lives in the drug-doses without a replicate well, where splitting on `n_wells_r2`
  gives +0.00323 single-well against +0.00361 replicated.

## What would settle it

1. **Per-arm matched placebo exposures** — a matched gene put in MG53's place *inside each arm*. This needs
   per-line values for arbitrary genes, which a completed run's output does not carry: only TRIM72 has them.
   On the full data it is one call to the existing `set_tables` over the 200 symbols of `c_placebos.csv`,
   about 790 MB and ~1 min, with no new pass over Tahoe-100M.
2. **A split-half version of the cross-well test** — MG53 from one half of a well's cells, program P from
   the other. The full-power form of the one decisive mechanism test, which here rests on 108 replicated
   drug-doses.
3. **A program P purged of stress/ISR overlap**, since MG53's standardised association with the stress set
   is ~6× its association with the program in *both* arms.
4. **Split-half reliability on exactly the 142 `in_S2_p53_activating` drug-doses.**
5. **A readthrough-specific placebo exposure** — per-line PYCARD-AS1 alongside FUS, to separate
   [[Readthrough spillover]] from MG53's own transcript.
6. **What the data cannot supply at all**: an engineered TP53 knockout or a Nutlin-3a arm would separate
   "cannot make p53 output" from "did not here", and an MG53 perturbation would turn this measurement from
   an association into an effect.

## Links

- **Concepts:** [[p53 program P]], [[Two-way fixed effects]], [[Reliability and disattenuation]],
  [[Readthrough spillover]], [[Cross-fitting and circularity]]
- **Methods:** [[Nulls and calibration]], [[Program P derivation]], [[Per-line p53 function]],
  [[How the numbers are decided]], [[Placebo genes and reference families]]
- **Findings:** [[What this study found]], [[Downstream of MG53]], [[Why MG53 is hard to measure here]],
  [[p53 nullification in cancer cell lines]], [[Corrections and retractions]]
- **Indexes:** [[Home]], [[Tables — what the study produced]]

## Sources

- Arm slopes, intervals, `n_rows`/`n_lines`, MDE: `mg53_p53/findings/tables/mg53_to_p53_effect.csv`
  (11 rows: 5 arms × 2 scopes, less arm B in the p53-activating scope)
- Arm D membership and the three held-out lines: `mg53_p53/findings/tables/null_reference_lines.csv`
- Arm A/B/C membership: `mg53_p53/findings/tables/per_line_p53_state.csv`
- Design and model: `mg53_p53/findings/mg53_to_p53_effect.py`; prose
  `mg53_p53/findings/README.md`, section "The measurement: change in p53 activity per change in MG53, with a
  knockout-like control" — whose intervals are superseded as noted above
- Conservative intervals, whole-line permutation, wild cluster bootstrap, positive control, cross-well and
  cross-normalisation tests, multiplicity: the reanalysis write-up "The measurement: p53 activity change per
  MG53 change, with controls" (`w5_main_table.csv`, `w4_lineperm_unbalanced.csv`, `w1_arm_slopes.csv`,
  `w1_contrast.csv`, `w2_positive_control.csv`, `w2_outcome_controls.csv`, `w2_cross_normalisation.csv`,
  `w2_placebos.csv`, `w3_same_vs_cross_well.csv`, `w3_well_level.csv`, `w3_replicated_split.csv`,
  `w5_multiplicity.csv`)
- Reliability: `two_way/tables/trim72_reliability.csv`, `two_way/tables/key_results.csv`
- Null calibration and placebos: `genome_wide/tables/c_calibration.csv`,
  `genome_wide/tables/c_placebos.csv`, `genome_wide/tables/c_program_models.csv`
- Exposure depth and well structure: `export/TRIM72/TRIM72_per_drugdose_line.csv`
