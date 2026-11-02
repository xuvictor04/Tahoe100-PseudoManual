---
type: concept
tags: [concept, measurement, artefact, batch, trim72]
status: current
---

# Plate batch effects

> [!summary] In one line
> MG53 carries the **largest untreated plate-to-plate gap of any gene in the dataset** — 3.124 log2, a 16×
> spread in its plate medians with no drug in them — so any statistic that compares MG53's *absolute level*
> across exposures is mostly comparing plates, and the pipeline's corrected fold change removes the gap's
> mean but not its noise.

## The gap

| | Value | Source |
|---|---|---|
| Untreated plate-batch gap, TRIM72 | **3.124 log2 = 8.7×** | `upstream_coregulation/tables/b_plate_batch_gap_genomewide.csv`, row 0 |
| Its rank among all genes | **1 of 16,656** | same table |
| Range of TRIM72's per-plate medians | **0.86 to 14.05 CPM** (16×) | `mdm2_mg53_cpm_by_plate.csv` |
| Median TRIM72 UMIs, plates 1/2/3/14 | **21** | `verify_variance_1`, recomputed |
| Median TRIM72 UMIs, plates 4–13 | **3** | same |

The 14 plates fall into two batches that differ in sequencing depth, and MG53 — being a trace transcript —
is the gene that suffers most. Plate 2 has a median of 28 UMIs and 1.71% zeros; plate 7 has a median of
**1** UMI and 30.96% zeros. The 16,656-gene universe quoted for the rank is the plate-gap table's own;
the genome-wide screen uses 16,642 tested genes, a near-identical but not identical set.

This is **not** library-size collapse. MG53's CPM is flat against UMIs per cell, ρ = **−0.013**, so the
denominator is not what is moving [`MDM2_MG53.md`, Table 2].

### It is a precision problem, not a bias problem

Depth drives the counting-noise floor, which is most of MG53's variance ([[Why MG53 is hard to measure here]]):

| | Deep plates (1/2/3/14) | Shallow plates (4–13) | Ratio |
|---|---|---|---|
| Count-noise floor | 0.190 log2² | 0.568 log2² | 2.99× |
| Full-sample single-profile residual variance | 0.350 | 0.764 | **2.18×** |
| Single-profile reliability | 0.145–0.188 | 0.066–0.073 | — |

[`verify_variance_1`, recomputed.]

### The artefact and the biology are the same phenomenon

The genome-wide plate gap is **strand-specific**. Among genes at 2–20 CPM, readthrough-exposed genes carry
a plate gap **0.264 log2 larger** than unexposed genes (p 1.6×10⁻⁶⁶), while antisense-exposed and "other"
classes are null (p 0.72 and 0.32) [`upstream_coregulation/tables/b_TRIM72_baseline_tests.csv`]. Deeper
libraries read more of the transcription that fails to terminate at a 5′ neighbour, so the plate gap *is*
[[Readthrough spillover]], measured on a different axis. That is the deepest confound in the project: the
artefact and the candidate mechanism cannot be separated by a depth control, because depth is how the
mechanism becomes visible.

## What the gap does to an across-exposure correlation of absolute levels

Almost every exposure sits on one plate: **1,030 of 1,132 on one, 101 on two**, and only adagrasib 0.05 µM
spans more (13). So across exposures, "which plate" and "which drug-dose" are nearly the same variable, and
a correlation of absolute levels between two genes is a correlation between their plate profiles.

### Worked example — MDM2's CPM against MG53's CPM

Binned by MG53 decile, MDM2 falls monotonically from **328.9 ± 4.4 CPM** in the lowest decile to
**252.1 ± 6.7** in the ninth as MG53 rises 20× [`MDM2_MG53.md`, Table 2]. Read alone it is the largest
result in the whole set: Spearman **−0.614**, p 5×10⁻¹¹⁸. Decomposed, it is the plate:

| Unit | Spearman |
|---|---|
| All 1,132 exposures together | **−0.614** |
| Between plates (the 14 plate medians) | **−0.763** |
| **Within plate, pooled** (plate medians removed) | **+0.074** |
| Mean of the 13 per-plate correlations | **+0.087** (negative on only 2 plates) |

MG53's plate medians run 0.86 → 14.05 CPM; MDM2's run the other way, 343 → 227. Within a plate the
relationship is *weakly positive*. There is no level-to-level relationship between these two genes; there
is a plate.

Two conventions were checked, because the decomposition depends on one. Assigning each exposure to the
first plate named leaves plate 6 holding a single exposure, so its "median" is one number. Dropping plate 6
gives between-plate **−0.791**; counting every plate an exposure actually appears on gives between-plate
**−0.793** and within-plate **+0.031**. The sign of the conclusion is convention-independent; the magnitude
of the within-plate figure is not (+0.074 against +0.031) and is small either way. See [[MDM2 and MG53]].

## What the correction fixes, and what it leaves

The analysed quantity, `r2`, subtracts a per-(plate, line) drug-well median and a composition correction.
By construction that **cancels the gap's mean and leaves its variance**.

The residual shares of plate and line in `r2` are tiny — plate | batch 0.18%, line 0.16%, plate × line
0.77% [`variance/t2_variance_shares.csv`] — and it is a mistake to read that as "batch and line effects
are small here". They are leakage from using a median rather than a mean. In the *untreated* data the same
terms are **48.5–53.1%** (plate) and **34.3–38.6%** (line) of the variance in per-(plate, line) log2 CPM
[`verify_variance_1/v10_plate_line_untreated.csv`]. The effects are enormous; they have been removed from
the mean.

Three consequences that survive the correction:

1. **The gap costs precision everywhere**, through the 2.18× residual-variance penalty above. Every MDE in
   this project is a batch-mix average.
2. **The effect is ratio-scale, so a uniform fold-change threshold is not a uniform bar.** A 1.2× floor is
   0.26–0.28 added CPM on a low-baseline plate (median drug-well baseline 1.39 CPM) but **2.37 added CPM**
   on a high-baseline plate (11.87 CPM) — **8.5× stricter**. Consistently, the 250 of 1,132 drug-doses
   (22.1%) whose used wells lie only on plates 1–3 carry **1 of the 21 committed raisers against 4.64
   expected** (Fisher one-sided OR 0.17, p 0.0356; raiser-label permutation p 0.0368). The committed
   ranking is nonetheless already essentially a within-plate ranking —
   Spearman(`DD_z`, within-plate z) = **0.9846**
   [`upstream_perturbations/tables/a_TRIM72_plate_batch_checks.csv`, row 2].
3. **A naive added-CPM ranking must not be used.** Plate 3's drug wells pool to 12.38 CPM against 19.00 CPM
   in its DMSO wells, so a compound that merely *fails to suppress* MG53 scores a large absolute gain.
   Per-plate median added CPM against DMSO is −8.3 (plate 3) and −3.7 (plate 14) against −0.1 to −1.0 on
   the low-baseline plates. Relatedly, Tahoe's own DESeq2 log2 fold change for TRIM72 is negative on **13
   of 14 plates** — plate 9 being the exception, and plate 9 carries five single-well raisers.

## The sign flips, and how far

Two cross-plate replications of the same exposure show how far a plate can carry a result on its own.

**Fold changes.** Plate 6 against plate 14 agree at Pearson **0.775** overall, falling to **0.321** once the
two strongest raisers are removed *(corrected: the earlier brief gave 0.75 and 0.28 —
`verify_raisers_0`)*. Over 89 non-raiser cross-batch pairs the agreement is Spearman +0.358 with 95% limits
of agreement −0.779 to +0.824 log2.

**Single cells.** The sharpest case is in [[MDM2 and MG53]], Table 6: idarubicin 5 µM, the same dose, the
same wild-type lines, split by whether MG53 was detected in the cell.

| Plate | MDM2 rate ratio | p | percentile among controls |
|---|---|---|---|
| **14** | **1.150** | **3×10⁻⁶** | 84th of 79 control genes |
| **6** | 0.941 | 0.20 | 15th of 78 |
| pooled | 1.043 | 0.18 | 65th of 80 |

One plate says MDM2 is 15% higher in MG53-positive cells at p = 3×10⁻⁶; the other says 6% lower. Either
would have looked publishable alone. That is the clearest available statement of what an MG53 measurement
in this data is worth at single-cell resolution, and it is why no claim in this project rests on one well
set.

## Rules that follow

- **Never correlate absolute MG53 levels across exposures** without removing plate first, and report the
  between- and within-plate parts separately. A pooled number is uninterpretable.
- **Report which plates an estimate rests on.** "Plates 1/2/3/14" and "plates 4–13" are different
  measurement regimes, not a nuisance label.
- **A fold-change threshold is plate-conditional.** Convert it to added CPM on each plate's own baseline
  before believing a ranking.
- **Cross-plate replication is the test that matters**, and almost nothing has it: only 107 drug-doses have
  two wells, 101 of them cross-plate.

## Links

- [[Why MG53 is hard to measure here]] — the counting noise the depth split drives
- [[Readthrough spillover]], [[The TRIM72 locus]] — why the plate gap is strand-specific
- [[MDM2 and MG53]] — the worked example in full, with its decile table and single-cell rows
- [[Reliability and disattenuation]] — why there is no single exchangeable-replicate reliability for MG53
- [[Two-way fixed effects]] — the nuisance-removal logic applied to drug-dose and line
- [[Upstream of MG53]], [[Corrections and retractions]], [[Tahoe-100M]]

## Sources

- `/tmp/claude-0/-home-user-Tahoe100-PseudoManual/6ff0eb71-456e-5d8b-af99-308c7803f336/tasks/w2dbqis5h.output`
  — *Upstream of MG53*, finding F4 and §§2.1, 2.4, 4.4.
- `mg53_p53/findings/MDM2_MG53.md` — Table 2 (the plate decomposition) and Table 6 (single cells).
- `upstream_coregulation/tables/b_plate_batch_gap_genomewide.csv`,
  `b_TRIM72_baseline_tests.csv`;
  `upstream_perturbations/tables/a_TRIM72_plate_batch_checks.csv`;
  `mg53_p53/findings/tables/mdm2_mg53_cpm_by_plate.csv`;
  `variance/t2_variance_shares.csv`; `verify_variance_1/v10_plate_line_untreated.csv`.
