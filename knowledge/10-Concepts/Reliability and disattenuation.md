---
type: concept
tags: [concept, method, measurement, reliability, trim72]
status: current
---

# Reliability and disattenuation

> [!summary] In one line
> Dividing a log2 slope by MG53's reliability converts "per doubling of **measured** MG53" into "per
> doubling of **true** MG53" — but the right divisor in this dataset is anywhere from 0.289 to 0.705
> depending on which subset you believe, a **2.4× range in the correction**, so the true-scale number is a
> range and never a point.

## What split-half reliability is here

It is not a generic "how noisy is this gene". It is a specific operation, and knowing which one matters:

1. Within each (well, line), split the **cells** into two halves.
2. Re-run the atlas correction separately on each half.
3. Average each half to the (drug-dose, line) grain and residualise.
4. Correlate the two halves. That raw correlation is `r_halves` = **0.169124**.
5. Project it to the full data with Spearman-Brown, `2r/(1+r)` = **0.289317**.

[`two_way/tables/trim72_reliability.csv`, row 54, `fe = ddxg`.]

Two things follow from step 1. First, **0.289 is already the full-data reliability, not a half-reliability**:
dividing a slope by it once is correct and in the right direction, and dividing by 0.169 would be the
mistake. Second, because the split is over cells *within* a well, it measures **cell-sampling noise only**
and books every well-level artefact — plate chemistry, library depth, [[Readthrough spillover]], the
[[Plate batch effects|plate gap]] — as **signal**. It is therefore the most optimistic reliability the
project contains.

## The published anchors disagree with each other

> [!warning] Five numbers, four specifications, one frequently-quoted "0.289"
> | Value | Where | What it is |
> |---|---|---|
> | **0.289317** | `trim72_reliability.csv` row 54, `fe = ddxg` | split-half, Spearman-Brown, full data |
> | 0.169124 | same table, row 184 `estimate` | the **raw** half-correlation; 0.289 appears only in that row's `detail` string |
> | **0.288981** | `two_way/tables/d1_two_way_models.csv`, `attenuation_lambda_split_half` | the value the pipeline actually divides by |
> | **0.114342** | `trim72_reliability.csv` row 111, `fe = dd` | replicate-**well** reliability |
> | 0.113639 | `two_way/tables/key_results.csv` row 206 | a third specification of the same idea — and the row the project's key facts cite for "0.114" |
>
> All verified directly. The split-half and replicate-well figures are **not the same number and not
> interchangeable**; see [[Corrections and retractions]].

The replicate-well figure carries its own defect: it is a Pearson *r* between two wells whose residual SDs
are **0.519 and 0.825** — a 2.5× difference *by design*, one deep-plate and one shallow-plate well. So
there is no single exchangeable-replicate reliability for MG53. Only the two batch-conditional values have
an estimand, and Spearman-Brown projections that mix batches cannot be computed from one pooled λ.

## The range, and what it is a range over

The run reports the same split-half under several subsets:

| λ | Subset | Correction factor 1/λ |
|---|---|---|
| **0.289** | primary specification (`i_all`) | **3.46×** |
| 0.425 | the 102 replicated drug-doses only — **not** `ii_active_no_plate3_13`, which reads **0.590** on its 58 | 2.35× |
| 0.586 | the 50 p53-activating exposures (`ii_p53`; 0.585 under `ddxg` fixed effects) | 1.71× |
| 0.610 | active exposures (`ii_active`) | 1.64× |
| **0.705** | MG53-moving exposures | **1.42×** |

[`two_way/tables/trim72_reliability.csv`, variant by variant; the menu is the one `MDM2_MG53.md` lists in Table 7.]

The endpoints differ by **2.4×** in the correction. Reliability rises on the active subsets for the obvious
reason — where MG53 actually moves, the signal-to-noise ratio is better — so the choice of subset is a
choice about the population the estimate is meant to generalise to, not a robustness check.

Two further anchors in use, from the per-arm fits of the central result: **0.301** in the TP53-wild-type
lines and **0.283** in the altered lines, against **0.114** for a single well
(quoted in [[The measurement with controls]], which is where they are used).

### A separate, much smaller family of numbers

Estimated instead from the 102 cross-batch **replicate pairs** — where the two measurements come from
different wells — single-profile reliability is **0.078–0.105** (λ = 0.080 against the full-sample
denominator, 0.105 against the pair subset), and **0.042** 10%-trimmed. Those imply corrections of
**9.5× to 12.5×**, or 24× trimmed [`variance/t4_crossbatch_pairs.csv`; `verify_variance_1`].

These are not in conflict with the split-half numbers; they answer a different question. The split-half
asks *what if the same well were resequenced*; the replicate-pair λ asks *what if a fresh well were run*.
Pick the one that matches the claim. Most claims in this project are about a fresh well, which is why the
pipeline's applied 3.46× is the **optimistic floor** of the defensible range rather than its centre.

> [!warning] A claimed agreement that does not hold
> "The counting share of variance (≈0.71) matches 1 − 0.289" was offered as mutual corroboration. It is an
> artefact of comparing unmatched samples: the matched split-half on the same 102 replicated drug-doses is
> **0.425164** [row 108], so the matched comparator is 1 − 0.425 = **0.575**, not 0.711. Logged in
> [[Corrections and retractions]].

## The arithmetic, and a worked example

Classical disattenuation is `b_true = b_obs / λ`, and because both axes here are log2, the units survive
the division: a slope in "log2 of the outcome per doubling of measured MG53" becomes "log2 of the outcome
per doubling of true MG53". The interval divides with the point estimate.

[[MDM2]]'s screen slope is the cleanest illustration — **−0.0048 log2, i.e. −0.35% of MDM2 per doubling of
measured MG53** [95% CI −0.61% to −0.08%, line-clustered]:

| λ used | Per doubling of **true** MG53 | 95% interval |
|---|---|---|
| 0.289 (primary) | **−1.19%** | −2.11% to −0.26% |
| 0.425 (the 102 replicated drug-doses) | −0.81% | — |
| 0.610 (active exposures) | **−0.57%** | −1.01% to −0.12% |
| 0.705 (MG53-moving exposures) | −0.49% | — |

[`MDM2_MG53.md`, Table 7.] The reportable statement is **"somewhere around −0.5% to −1.2% per doubling of
true MG53"**. An earlier version of that table gave −1.19% alone — the subset that maximises the
correction. Recorded in [[Corrections and retractions]].

The same arithmetic sets the study's own detection bounds. For a per-gene genotype difference the 80%-power
bound is |diff| ≥ 0.029 log2 = **+2.0% per doubling of measured MG53**, which at λ = 0.289 is **+7.1% per
doubling of true MG53** — and that is **1.43× the median program gene's entire wild-type-minus-altered
genotype effect** (0.070 log2). MG53 would have to move a p53 target by more than TP53 genotype itself does
for this screen to have seen it [`c_screen_genes.csv.gz`, `se_diff`/`se_common`/`df`].

## When not to divide at all

The correction assumes **classical** measurement error: error independent of the true score, and
independent of the outcome's error. The second condition fails by construction wherever MG53 and the
outcome are counted from the same cells, in the same well, against the same total-UMI denominator — which
is every same-well statistic in this project. The implied error correlation from the cross-batch pairs is
**0.045**, direction supported and magnitude unidentified
([[Why MG53 is hard to measure here]], point 2).

> [!important] Do not report "per doubling of true MG53" by dividing a same-well slope by λ.
> That quantity has no estimand: the division amplifies the shared artefact along with the signal. The
> internally consistent artefact-free slope needs no λ, because it is built from `cov(x_wellA, y_wellB)`:
> **+0.0074 to +0.0079 program-log2 per doubling of true MG53 [−0.018, +0.026]**
> [`variance/t6_shared_error.csv`]. Every "true-MG53" restatement elsewhere in the material should be read
> as illustrative.

Two further ways a reliability estimate goes wrong here:

- **The ceiling argument does not apply.** `r_obs ≤ √(λ_x λ_z)` holds only for independent errors. For
  readthrough partners it fails more deeply than that: transcription running past FUS is *literally counted
  as* TRIM72 mRNA, so those measurements share **signal**, not merely error, and no attenuation ceiling
  constrains their correlation. The claim that MG53's observed partner correlations (max 0.863) exceed what
  its reliability permits is **withdrawn**.
- **Centring must be per well.** Residualising on the pooled drug-dose fixed effect before pairing forces
  the two wells anti-correlated and yields a *negative* σ²_DL. This is the detail a replicator most needs
  and the analysis omitted it [`verify_variance_1`].

## How to report it

1. **Measured scale first.** The slope and interval on measured MG53 are what the data produced; they need
   no assumption.
2. **True scale as a range**, naming both λ endpoints and the subset each belongs to — e.g. "−0.5% to
   −1.2% per doubling of true MG53 (λ 0.705 to 0.289)".
3. **Never a single disattenuated point estimate**, and never the λ that happens to maximise the effect.
4. **State the error-independence assumption** and whether it holds for that statistic. If exposure and
   outcome share a well, say that the correction is illustrative and quote the artefact-free estimate
   instead.

## Links

- [[Why MG53 is hard to measure here]] — where the low reliability comes from
- [[Plate batch effects]] — why one pooled λ cannot cover both batches
- [[The measurement with controls]] — the central result, reported on both scales
- [[MDM2 and MG53]] — the worked example in full
- [[Corrections and retractions]] — the anchor disagreement, the withdrawn ceiling argument, the −1.19%
- [[Two-way fixed effects]], [[Nulls and calibration]], [[How the numbers are decided]]
- [[MG53 (TRIM72)]], [[TRIM72]], [[MDM2]]

## Sources

- `/tmp/claude-0/-home-user-Tahoe100-PseudoManual/6ff0eb71-456e-5d8b-af99-308c7803f336/tasks/w2dbqis5h.output`
  — *Upstream of MG53*, findings F5 and F6 and §§2.3, 2.6, 5.2.
- `mg53_p53/findings/MDM2_MG53.md` — Table 7 and the subset table at line 454.
- `mg53_p53/findings/MG53_p53_TABLES.md` — "The true-MG53 scale is a range, not a point" and the per-gene
  detectable-effect bound.
- `two_way/tables/trim72_reliability.csv`, `d1_two_way_models.csv`, `key_results.csv`;
  `variance/t4_crossbatch_pairs.csv`, `t6_shared_error.csv`.
