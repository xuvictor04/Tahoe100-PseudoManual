---
type: concept
tags: [concept, measurement, trim72, reliability, power]
status: current
---

# Why MG53 is hard to measure here

> [!summary] In one line
> MG53 is a trace transcript in this dataset — median 5 UMIs per profile — so two thirds of the variance in
> its measured fold change is the Poisson noise of counting those UMIs, and 90% of the design's drug-doses
> have one well with which to average it down. Everything that uses MG53 as the *exposure* inherits that.

## The four facts

| | Value | Source |
|---|---|---|
| Median level across the 50 lines | **5.89 CPM** (per-line range 0.93–23.6) | `export/downstream/` per-line levels, quoted in `MDM2_MG53.md` Table at line 29 |
| Profiles with zero TRIM72 counts | **12.42%** of the 62,611 usable profiles from expressing lines | recomputed, `verify_raisers_0` |
| Median TRIM72 UMIs per profile | **5** | `verify_variance_1`, recomputed |
| Split-half reliability, primary spec | **0.289** — but 0.425 to 0.705 on active subsets | `two_way/tables/trim72_reliability.csv` |

> [!warning] The zero fraction depends on its denominator, and the headline figure uses the narrowest one
> 12.42% over the 62,611 usable profiles from *expressing* lines; **13.69%** over all 63,921 usable
> profiles; **16.56%** over all 66,449. The project's 12.4% is reproducible only with its own denominator
> [recomputed, `verify_raisers_0`]. Quoting it without the denominator understates the problem by four
> percentage points. Logged in [[Corrections and retractions]].

The pooled-CPM column of the plate-gap table reads **5.33 CPM** for TRIM72 rather than 5.89
[`upstream_coregulation/tables/b_plate_batch_gap_genomewide.csv`, row 0, `pooled_cpm`]. These are two
different quantities — a pooled CPM over all profiles against a median of per-line levels — not a
discrepancy.

## Two thirds of the fold-change variance is counting noise

A Poisson simulation keyed only to each profile's sequencing depth, pushed through the pipeline's exact
`log2(1e6·(k+0.5)/T)` transform (reproduced to 2×10⁻³), reproduces most of the observed variance:

| Estimator | Counting share of variance |
|---|---|
| Deep plates (1/2/3/14) | 0.54 |
| Shallow plates (4–13) | 0.74 |
| Strata regression | 0.67 |
| Regression through the origin | 0.88 |
| **Central estimate / defensible range** | **0.67–0.71 / 0.54–0.88** |

[`variance/t3_count_noise_strata.csv`; range widened by `verify_variance_0` and `verify_variance_1`.]

The strata regression is `observed_var = 0.213 + 0.949 × Poisson_floor` with slope SE 0.055. Read that
honestly: Poisson is **not rejected at ±15% resolution**, which is not the same as Poisson being
established. No extra over-dispersion term is needed, but none is excluded either.
*(Corrected: the original analysis claimed ±10% resolution.)*

The share is a function of depth, not a constant: **0.91** where the median is 1 UMI, **0.19** at 75 UMIs.
That is why the deep/shallow split in [[Plate batch effects]] is also a precision split.

## The design gives almost nothing to average over

| Replication | Drug-doses |
|---|---|
| One used well | **1,024 of 1,132 (90.46%)** |
| Two wells | 107 (101 of them cross-plate) |
| Fourteen wells | 1 (adagrasib 0.05 µM) |
| Drug-dose × plate cells holding ≥ 2 wells | **7** *(corrected from 6 in `verify_variance_1`)* |

[`variance/t1_replication_per_dd.csv`.]

So the counting noise cannot be averaged down, and the well-level and plate-level terms cannot be separated
except on those 7 cells — where the bootstrap interval on within-plate well noise (σ²_W = 0.0869,
CI 0.017–0.194, against 0.1390 cross-plate) overlaps the cross-plate value and the p53 program *inverts*
sign [`verify_variance_1/v8_withinplate.py`]. The question "is MG53's reliability nearer 0.08 or 0.29" has
no answer in this design.

## What one well is worth

Over 89 non-raiser cross-batch pairs the two independent wells agree at Spearman **+0.358**
(drug-dose-label permutation, 5,000 draws, p 0.0004), with 95% limits of agreement **−0.779 to +0.824 log2**
and an implied per-well SD of **0.289 log2** [`raisers/t4_pair_agreement.csv`].

> [!warning] One well's 95% error is **1.48×**, not 1.74×
> The 1.74× figure in the earlier analysis is the *repeatability coefficient*, which bounds the gap between
> two wells, not the error of one [corrected in `verify_raisers_0`]. See [[Corrections and retractions]].

There is also a hard multiplicity floor. An exact within-plate rank *p* for a single well has a floor of
1/94 = 0.01064, while BH over 1,132 drug-doses needs *p* ≤ 8.8×10⁻⁵ for the top rank — so the smallest
attainable *q* is **12.0**: no single-well drug-dose can reach FDR 0.10 at any effect size under that
exchangeability unit. That is a property of the chosen null rather than of the design; pooling the
within-plate null over all 14 plates (1,252 drug wells) gets resolution near 8.0×10⁻⁴, within an order of
magnitude of what BH needs. Either way, every single-well call in this study rests on normal theory for *Z*.

## Reliability by unit, and the resulting bounds

| Unit | Reliability | 80%-power MDE |
|---|---|---|
| One profile (well × line) | **0.078–0.105** (0.055 trimmed) | 3.58× fold |
| One profile, deep plates 1/2/3/14 | 0.145–0.188 | — |
| One profile, shallow plates 4–13 | 0.066–0.073 | — |
| Mean of 2 wells, one per batch | 0.189 | — |
| One well, drug-dose main effect | **0.280** screen-wide (0.61 among replicate-bearing drug-doses) | 2.19× fold |
| Per-line untreated level, within the 14-plate set | 0.977 | 1.67× fold |
| Per-line untreated level, generalising across batch | **0.896** | **3.32× fold** |
| p53 program P, one profile | **0.425** | — |

[`variance/t1`–`t4`; `verify_variance_1`. The split-half anchors are a separate object —
see [[Reliability and disattenuation]].]

The last row is the one to keep in mind. Program P is roughly **twice as well determined per well as MG53**,
because averaging 180 genes divides the independent counting noise without dividing the signal
(program total variance 0.006684 log2², well main effect 47.5%, residual 49.85%, against MG53's total
0.8785 with 73.34% residual [`variance/t2_variance_shares.csv`]). In any asymmetric reading of an
MG53 ↔ p53 relationship, **MG53 is the limiting instrument for variance** — though not for bias, because
both channels are counted from the same libraries.

## What this does to a test that uses MG53 as the exposure

1. **The slope is attenuated toward zero**, by a factor that depends on which reliability you believe —
   3.46× as the pipeline applies it, 9–12× on the single-profile λ this reanalysis supports, 24× on the
   trimmed value. The arithmetic and the honest way to report it are in
   [[Reliability and disattenuation]].
2. **The attenuation correction is the lesser problem, and in the same-well case it is the wrong
   correction.** `b_true = b_obs/λ` needs exposure error independent of outcome error, and that fails by
   construction: MG53 and every program-P gene are counted from the same cells, in the same well, against
   the same total-UMI denominator. The cross-batch estimate of the shared-error channel is 0.00134–0.00142
   [95% CI −0.00015 to +0.00378] with an implied error correlation of 0.045 — direction supported,
   magnitude unidentified. Split by batch it is **−0.00044 on the deep plates and +0.00311 on the shallow
   ones**, so the whole signal is one batch and the deep-plate estimate has the wrong sign for the proposed
   mechanism [`verify_variance_0/v3_cb.py`]. The widely quoted "77% of the observed association is shared
   error" is a ratio of two near-zero quantities with a recomputed bootstrap SD of 54 and CI
   [−0.236, +1.420]; **it is withdrawn as a point estimate** ([[Corrections and retractions]]).
   The artefact-free route needs no λ at all — see [[The measurement with controls]].
3. **Reproducible line-specific signal is scarce and concentrated.** σ²_DL = 0.0508 log2²
   [cluster bootstrap over the 102 replicated drug-doses, 95% CI 0.0179–0.1015], but one compound
   (homoharringtonine 5 µM) supplies **38.7%** of it, the top five supply 63.6%, 37.3% of the 102
   drug-doses have a *negative* replicate covariance, and the 10%-trimmed value is 0.0265
   [`verify_variance_1/q4_per_dd_cov.csv`]. The reliability underpinning every power calculation here is
   therefore not a property of a typical drug-dose.
4. **For the median drug-dose there is no line-specific MG53 response at all.** The best-replicated exposure
   in the dataset — adagrasib 0.05 µM, 14 wells, 47–49 lines — has a **negative** between-line variance
   component (−0.0022) against within-line across-well variance 0.704, so reliability is ≤ 0 at one well
   *and* at fourteen, and the MDE with all 14 wells is 0.628 log2 = 1.55× fold. Program P on the identical
   wells reaches 0.099 per well and 0.606 with all 14 [`verify_variance_0/v18_anchor.py`].
5. **At single-cell resolution, "MG53-detected" partly means "more deeply sequenced cell."** With ~5 UMIs
   MG53 is detected in a minority of cells, so the UMI offset, the UMI covariate and the depth-stratified
   variant are load-bearing — and they do move the answer (for DMSO plate 14 wild-type lines, the per-line
   median is −0.210 adjusted against −0.122 unadjusted) [`MDM2_MG53.md`, Table 6].

## What this is not

It is not a claim that MG53 is unmeasurable. The one MG53 question this design answers well is **which cell
line expresses more of it untreated**: reliability 0.977 within the 14-plate set, 0.896 generalising across
batch, SE 0.19 log2 and 0.44 log2 respectively. That is the unit on which the locus result
(PYCARD-AS1 ρ +0.820, CI 0.690–0.899) lives — see [[The TRIM72 locus]] and [[Readthrough spillover]].

Nor is it the reason the study's central answer is null. The bound in [[What this study found]] — effects
above roughly 0.4–0.6% of p53 output per doubling of measured MG53 excluded — is a *bound*, computed with
this noise in it. Poor measurement widens an interval; it does not create a null.
And no line here carries a TRIM72 alteration: all 50 are wild-type MG53 and differ only in level, so
nothing in this dataset contrasts functional with non-functional MG53.

## Links

- [[Plate batch effects]] — the depth split that sets most of the noise, and the gap the correction leaves
- [[Reliability and disattenuation]] — the split-half anchors and the arithmetic of the correction
- [[Readthrough spillover]], [[The TRIM72 locus]] — why part of the measured signal is not MG53's transcript
- [[Two-way fixed effects]] — the estimator this noise feeds
- [[The measurement with controls]], [[What this study found]] — the bound that comes out the other end
- [[MG53 (TRIM72)]], [[TRIM72]], [[Tahoe-100M]]

## Sources

- `/tmp/claude-0/-home-user-Tahoe100-PseudoManual/6ff0eb71-456e-5d8b-af99-308c7803f336/tasks/w2dbqis5h.output`
  — *Upstream of MG53: regulation, perturbations, and what this dataset can support*, §2.1–2.7 and findings
  F4, F5, F6.
- `mg53_p53/findings/MDM2_MG53.md` — Table 6 (single cells) and the measurement summary at line 617.
- `mg53_p53/findings/MG53_p53_TABLES.md` — "Caveats that apply to all three tables".
- `variance/t1_replication_per_dd.csv`, `t2_variance_shares.csv`, `t3_count_noise_strata.csv`,
  `t4_crossbatch_pairs.csv`; `raisers/t4_pair_agreement.csv`; `two_way/tables/trim72_reliability.csv`.
