---
type: concept
tags: [concept, artefact, trim72, measurement]
status: current
---

# Readthrough spillover

> [!summary] In one line
> Transcription that fails to terminate at one gene runs into the next one on the same strand and is counted
> as that gene's mRNA — which for MG53 is the leading explanation of what "raises" it.

## The mechanism

RNA polymerase II does not stop cleanly at every annotated 3′ end. When termination fails, the polymerase
continues into whatever lies 3′ on the same strand, and a short-read assay assigns the resulting reads to the
gene they land in. The effect scales with the *donor's* expression, not the recipient's, so a gene sitting a
few kilobases 3′ of a highly expressed neighbour can register large apparent changes that are not its own
transcription at all.

Readthrough is itself regulated: it increases under stress, heat shock, osmotic shock, viral infection and
various transcription and translation inhibitors. Which matters here, because the drugs that most "raise"
MG53 in this dataset are exactly that sort of compound.

**Naming rule for this project.** This phenomenon is called **readthrough spillover**. Chromosomal position
is written "3′ of" or "5′ of". The word "downstream" is reserved for regulatory consequence and never used
for position — a distinction that matters because confusing the two is how a measurement artefact gets
written up as a pathway.

## Why MG53 is unusually exposed

See [[The TRIM72 locus]] for the geometry. In short: TRIM72 lies 17.05 kb 3′ of [[FUS]] on the same strand,
and FUS runs at roughly **47× TRIM72's level**. The pipeline flags genes in this position `sense_exposed` —
within 20 kb 3′ of an expressed same-strand gene at ≥ 8× their own expression — and TRIM72 is one of them.

## How far it has actually been established

This is where to be careful. The evidence splits into a part that is solid and a part that is not.

**Solid — the phenomenon is real and strand-aware.** In the wells where MG53 rises most, the plus-strand
genes on the readthrough path rise together (median excess **+0.856 log2**, 14 of 15 wells, one-sided
Wilcoxon p 9×10⁻⁵, shuffle unit = well), while **[[PYCARD]]** — co-positional with PYCARD-AS1 to the base
pair but on the *minus* strand — **falls** (median −0.495 log2, negative in 14 of 15, p 0.0013). Two genes at
identical coordinates moving in opposite directions rules out a mapping smear and establishes that the
quantification respects strand.

**Not solid — the magnitude.** A flux model calibrated three independent ways on the plate-batch contrast
(κ = 5.36 to 8.00 CPM delivered to TRIM72 per CPM delivered to PYCARD-AS1) **over-predicts** the observed
rise by about 59% at the median, and per-well attributable fractions run from −140% to +742%. So: order-of-
magnitude consistent, and quantitatively unaccounted for.

The honest statement is therefore "readthrough spillover is the leading account of MG53's apparent
induction, and the arithmetic does not close" — not "MG53's induction is readthrough".

## What is done about it

- A **readthrough-corrected covariate set**, `gw_rt`, is carried through the genome-wide screen. Any result
  that survives it is not spillover, and this is stated wherever such a result is quoted. [[MDM2]]'s slope,
  for instance, is −0.00500 under the primary set and −0.00501 under `gw_rt` — unchanged.
- Genes are annotated with a `dog_class` (`sense_exposed` / `unexposed` / `other`) and an
  `in_TRIM72_locus_200kb` flag, both surfaced in every gene note's generated block.
- Placebo comparisons can be restricted to `unexposed` genes, which are structurally incapable of spillover.
  Doing so does not rescue MG53's raiser list: restricted to the 419 level-matched unexposed genes, the
  median number of "raisers" per gene *rises* to 20 and MG53's 21 sits at the 53rd percentile.

## Links

- [[The TRIM72 locus]] · [[MG53 (TRIM72)]] · [[Plate batch effects]]
- [[Upstream of MG53]] — the findings this dominates
- [[Placebo genes and reference families]] — the unexposed-gene comparison
- Gene notes: [[TRIM72]], [[FUS]], [[PYCARD]], [[PYCARD-AS1]]

## Sources

- `upstream_coregulation/tables/b_plate_batch_gap_genomewide.csv` — `DoG_class`, the 5′ same-strand
  neighbour, pooled CPM.
- `upstream_coregulation/tables/c_locus_obs_over_exp_raiser_wells.csv` — the per-well strand contrast.
- `upstream_coregulation/tables/c_DoG_gene_exposure_classes.csv` — the exposure class of every gene.
- `genome_wide/tables/c_screen_genes.csv.gz` — `b_common_gw_rt`, the readthrough-corrected slope.
