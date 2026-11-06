---
type: concept
tags: [concept, method, measurement, reliability]
status: current
---

# Reliability and disattenuation

> [!summary] In one line
> Dividing a slope by a variable's reliability converts "per unit of the **measured** variable" into "per unit of
> the **true** variable" — but for a low-level gene in this data the right divisor depends on which subset and
> which kind of replicate you believe (0.29 to 0.71 for MG53 in the earlier study, a 2.4× range), so the
> true-scale number is a range and never a point.

## What split-half reliability is here

It is not a generic "how noisy is this gene". It is a specific operation, and knowing which one matters. In the
earlier MG53/p53 study, for MG53 ([[TRIM72]]):

1. Within each (well, line), split the **cells** into two halves.
2. Re-run the atlas correction separately on each half.
3. Average each half to the (drug-dose, line) grain and residualise.
4. Correlate the two halves. That raw correlation was `r_halves` = **0.169124**.
5. Project it to the full data with Spearman-Brown, `2r/(1+r)` = **0.289317**.

Two things follow from step 1. First, **the Spearman-Brown value is already the full-data reliability**:
dividing a slope by it once is correct, and dividing by the raw half-correlation would be the mistake. Second,
because the split is over cells *within* a well, it measures **cell-sampling noise only** and books every
well-level artefact — plate chemistry, library depth, [[Readthrough spillover]], the plate gap
([[Plate batch effects]]) — as **signal**. It is therefore the most optimistic reliability available.

## Different specifications give different numbers

| Value | What it is |
|---|---|
| **0.289** | split-half, Spearman-Brown, full data |
| 0.169 | the **raw** half-correlation |
| **0.114** | replicate-**well** reliability |

The split-half and replicate-well figures are **not the same number and not interchangeable**. The replicate-well
figure carried its own defect: a Pearson *r* between two wells whose residual SDs were **0.519 and 0.825** — one
deep-plate and one shallow-plate well. So there was no single exchangeable-replicate reliability; only
batch-conditional values have an estimand.

## The range, and what it is a range over

The same split-half under different subsets:

| λ | Subset | Correction factor 1/λ |
|---|---|---|
| **0.289** | all exposures | **3.46×** |
| 0.425 | the 102 replicated drug-doses only | 2.35× |
| 0.586 | the 50 p53-activating exposures | 1.71× |
| 0.610 | active exposures | 1.64× |
| **0.705** | exposures that move the gene | **1.42×** |

Reliability rises on the active subsets for the obvious reason — where the gene actually moves, the
signal-to-noise ratio is better — so the choice of subset is a choice about the population the estimate is meant
to generalise to, not a robustness check.

Estimated instead from cross-batch **replicate pairs** — two different wells — single-profile reliability was
**0.078–0.105** (0.042 10%-trimmed), implying corrections of 9.5× to 12.5×. These answer a different question: the
split-half asks *what if the same well were resequenced*; the replicate-pair λ asks *what if a fresh well were
run*. Most claims are about a fresh well.

## The arithmetic

Classical disattenuation is `b_true = b_obs / λ`; on log2 axes the units survive the division. The interval divides
with the point estimate. In the earlier study, [[MDM2]]'s slope on measured MG53 was −0.35% per doubling
[95% CI −0.61% to −0.08%]; divided by λ it became −1.19% (λ 0.289) to −0.49% (λ 0.705) per doubling of true MG53 —
reportable as "somewhere around −0.5% to −1.2%", never as the single value that maximises the correction.

## When not to divide at all

The correction assumes **classical** measurement error: error independent of the true score, and independent of the
outcome's error. The second condition fails by construction wherever two genes are counted from the same cells, in
the same well, against the same total-UMI denominator.

> [!important] Do not disattenuate a same-well correlation by dividing by λ.
> The division amplifies the shared artefact along with the signal. An artefact-free estimate pairs the two
> variables across *different* wells (`cov(x_wellA, y_wellB)`), and needs no λ.

Two further ways a reliability estimate goes wrong:

- **The ceiling argument does not apply to shared signal.** `r_obs ≤ √(λ_x λ_z)` holds only for independent
  errors. For readthrough partners, transcription running past the 5′ gene is *literally counted as* the 3′ gene's
  mRNA, so they share signal, not merely error, and no attenuation ceiling constrains their correlation.
- **Centring must be per well.** Residualising on a pooled drug-dose effect before pairing wells forces the two
  wells anti-correlated.

## What this means for the vault's numbers

- The **z** of a drug effect already carries its noise: a low-level gene has a wide reference spread and so small z
  for the same fold change. Fold changes of low-level genes (look at `pooled_cpm` and `n_lines_expressing` in the
  frontmatter) are noisier than their z suggests only when the z reference itself is mis-specified.
- **Gene–gene cosines** are computed on denoised vectors, so they are not attenuated the way raw correlations are;
  their reliability is checked directly by recomputing them in two halves of the compounds (`cos_half1`,
  `cos_half2`, `evidence`).

## How to report it

1. **Measured scale first.** The slope and interval on the measured variable are what the data produced.
2. **True scale as a range**, naming both λ endpoints and the subset each belongs to.
3. **Never a single disattenuated point estimate**, and never the λ that happens to maximise the effect.
4. **State the error-independence assumption** and whether it holds for that statistic.

## Sources

- The earlier MG53/p53 study: `two_way/tables/trim72_reliability.csv`, `d1_two_way_models.csv`,
  `key_results.csv`; `variance/t4_crossbatch_pairs.csv`, `t6_shared_error.csv`;
  `mg53_p53/findings/MDM2_MG53.md` (Table 7).
