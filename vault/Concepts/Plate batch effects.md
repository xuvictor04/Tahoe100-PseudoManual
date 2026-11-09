---
type: "concept"
tags: ["concept", "measurement", "artefact", "batch"]
status: "current"
source: "tahoemap/vault_seed/notes/Plate batch effects.md"
generated_by: "tahoemap"
---

# Plate batch effects

> [!summary] In one line
> Untreated levels differ between Tahoe's plates by up to 3.1 log2 for a single gene, and nearly every drug-dose
> sits on one plate — so any statistic that compares a gene's *absolute level* across exposures is mostly comparing
> plates, and the per-plate baseline removes the gap's mean but not its noise.

## The gap

Each gene's untreated level differs from plate to plate, and for some genes by a lot. The earlier MG53/p53 study
measured the gap genome-wide; its extreme case was [[TRIM72]] (MG53):

| | Value | Source |
|---|---|---|
| Untreated plate-batch gap, TRIM72 | **3.124 log2 = 8.7×** | `upstream_coregulation/tables/b_plate_batch_gap_genomewide.csv`, row 0 |
| Its rank among all genes | **1 of 16,656** | same table |
| Range of TRIM72's per-plate medians | **0.86 to 14.05 CPM** (16×) | `mdm2_mg53_cpm_by_plate.csv` |
| Median TRIM72 UMIs, plates 1/2/3/14 | **21** | `verify_variance_1` |
| Median TRIM72 UMIs, plates 4–13 | **3** | same |

The 14 plates fall into two batches that differ in sequencing depth (plates 1/2/3/14 deep, 4–13 shallow), and
trace transcripts suffer most: for TRIM72, plate 2 had a median of 28 UMIs and 1.71% zeros, plate 7 a median of
**1** UMI and 30.96% zeros. That was **not** library-size collapse — TRIM72's CPM was flat against UMIs per cell
(ρ = −0.013) — so the denominator is not what moves.

### It is a precision problem, not a bias problem

Depth drives the counting-noise floor, which is most of a trace gene's variance. For TRIM72:

| | Deep plates (1/2/3/14) | Shallow plates (4–13) | Ratio |
|---|---|---|---|
| Count-noise floor | 0.190 log2² | 0.568 log2² | 2.99× |
| Full-sample single-profile residual variance | 0.350 | 0.764 | **2.18×** |
| Single-profile reliability | 0.145–0.188 | 0.066–0.073 | — |

### The artefact and the biology can be the same phenomenon

The genome-wide plate gap is **strand-specific**. Among genes at 2–20 CPM, readthrough-exposed genes carried a
plate gap **0.264 log2 larger** than unexposed genes (p 1.6×10⁻⁶⁶), while antisense-exposed and "other" classes
were null (p 0.72 and 0.32). Deeper libraries read more of the transcription that fails to terminate at a 5′
neighbour, so for exposed genes the plate gap *is* [[Readthrough spillover]], measured on a different axis: depth
is how that mechanism becomes visible, so a depth control cannot separate them.

## What the gap does to an across-exposure correlation of absolute levels

Almost every exposure sits on one plate: **1,030 of 1,132 on one, 101 on two**, and only adagrasib 0.05 µM spans
more (13). So across exposures, "which plate" and "which drug-dose" are nearly the same variable, and a
correlation of absolute levels between two genes is a correlation between their plate profiles.

### Worked example — two genes' CPM against each other

In the earlier study, [[MDM2]]'s CPM binned by TRIM72 decile fell monotonically from **328.9 ± 4.4 CPM** to
**252.1 ± 6.7** as TRIM72 rose 20×: Spearman **−0.614**, p 5×10⁻¹¹⁸, the largest number in that study.
Decomposed, it was the plate:

| Unit | Spearman |
|---|---|
| All 1,132 exposures together | **−0.614** |
| Between plates (the 14 plate medians) | **−0.763** |
| **Within plate, pooled** (plate medians removed) | **+0.074** |
| Mean of the 13 per-plate correlations | **+0.087** (negative on only 2 plates) |

TRIM72's plate medians ran 0.86 → 14.05 CPM; MDM2's ran the other way, 343 → 227. Within a plate the
relationship was *weakly positive*: there was no level-to-level relationship, there was a plate. (Assigning each
exposure to every plate it appears on instead gives between-plate −0.793 and within-plate +0.031: the sign of the
conclusion does not depend on the convention; the size of the small within-plate figure does.)

## What the correction fixes, and what it leaves

Every fold change in this vault subtracts a per-(plate, line) drug-well median and a composition correction. By
construction that **cancels the gap's mean and leaves its variance**.

The residual shares of plate and line in the corrected values are tiny — plate | batch 0.18%, line 0.16%,
plate × line 0.77% in the earlier study's variance decomposition — and it is a mistake to read that as "batch and
line effects are small here". In the *untreated* data the same terms are **48.5–53.1%** (plate) and **34.3–38.6%**
(line) of the variance in per-(plate, line) log2 CPM. The effects are enormous; they have been removed from the
mean.

Three consequences survive the correction:

1. **The gap costs precision.** Noisier plates give noisier fold changes. The pipeline widens z on noisy plates by
   a *plate factor* (the drug-dose flag `noisy plate (z scaled)`), and a gene's own plate factor is applied too.
2. **The effect is ratio-scale, so a uniform fold-change threshold is not a uniform bar.** A 1.2× floor was 0.26–0.28
   added CPM on a low-baseline plate for TRIM72 but **2.37 added CPM** on a high-baseline plate — 8.5× stricter.
3. **A naive added-CPM ranking against DMSO must not be used.** On a plate whose drug wells pool lower than its
   DMSO wells, a compound that merely *fails to suppress* a gene scores a large absolute gain.

## The sign flips, and how far

The same exposure on two plates can disagree. In the earlier study, plate 6 against plate 14 agreed at Pearson
0.775 overall, falling to 0.321 once the two strongest raisers were removed; in single cells, idarubicin 5 µM gave
an MDM2 rate ratio of **1.150** (p 3×10⁻⁶) between TRIM72-positive and -negative cells on plate 14 and **0.941**
(p 0.20) on plate 6. Either would have looked publishable alone.

## How this vault shows it

- Each gene has a **plates note** (linked from its `## Data` section): its raw CPM and its corrected well effect
  (W2) in every well of every plate, laid out as the plate is. A gene whose raw level jumps between plates while
  its corrected values stay flat is a plate-gap gene.
- Each **Plate NN** note gives the plate's dose, layout, plate factor, DMSO wells, failed wells and whether the
  plate is unreliable (plate 13: its replicate wells do not reproduce; it is used only for drug-doses with no other
  well, flagged `unreliable plate only`).
- Gene–gene relations are computed on the corrected per-line z, never on absolute levels.

## Rules that follow

- **Never correlate absolute levels across exposures** without removing plate first, and report the between- and
  within-plate parts separately. A pooled number is uninterpretable.
- **Report which plates an estimate rests on.** Deep and shallow plates are different measurement regimes.
- **A fold-change threshold is plate-conditional** for low-level genes.
- **Cross-plate replication is the test that matters**, and almost nothing has it: only 107 drug-doses have two
  wells, 101 of them cross-plate.

## Sources

- The earlier MG53/p53 study: `mg53_p53/findings/MDM2_MG53.md` (Table 2, the plate decomposition; Table 6, single
  cells); `upstream_coregulation/tables/b_plate_batch_gap_genomewide.csv`, `b_TRIM72_baseline_tests.csv`;
  `mg53_p53/findings/tables/mdm2_mg53_cpm_by_plate.csv`; `variance/t2_variance_shares.csv`;
  `verify_variance_1/v10_plate_line_untreated.csv`.
- tahoemap: `tables/plates.parquet` (plate factor, unreliable, failed wells), `tensor/well_counts.npy`,
  `atlas/effects/W2.npy`.

---
*Written note, copied from `tahoemap/vault_seed/notes/Plate batch effects.md` by `tahoemap vault`. Edit it there, not here: this copy is replaced on every build.*
