---
symbol: NFIL3
type: gene
tier: 2
tags: [gene, transcription-factor]
generated_by: knowledge/_build/build_vault.py
---

# NFIL3

> [!summary] In one line
> NFIL3 encodes E4BP4, a bZIP transcription factor that represses D-box promoter elements by competing with the PAR-family activators for the same sites.

## What it is

NFIL3 belongs to the proline- and acidic-amino-acid-rich (PAR) branch of the bZIP family but lacks the PAR activation domain its relatives carry, so it binds the shared D-box consensus and represses rather than activates. Its abundance oscillates in antiphase to DBP, HLF and TEF, and that competition is part of the circadian oscillator, with PER1 and PER2 among the repressed targets. It was isolated twice under different names — as E4BP4, a repressor of the adenovirus E4 promoter, and as an interleukin-3-regulated factor in haematopoietic survival. Its best-established requirement is developmental: Nfil3-deficient mice lack mature natural killer cells, and the factor acts early in the innate lymphoid lineage.

## Why it appears in this work

NFIL3 is one of the factors scored in the regulon-based activity step. For a reader of this study the question is whether an inferred factor could account for MG53's movement; a D-box repressor would do so by a route separate from p53, and showing it would need a D-box in the TRIM72 promoter, which has not been reported. See [[Transcription factor activity inference]].

## What is uncertain

Its regulon here is small, and its targets were curated largely from circadian and mouse lymphoid systems rather than epithelial tumour cells, so coherent movement need not report NFIL3. Because it represses, the direction of its inferred activity depends on sign conventions applied inconsistently to repressors. And unsynchronised proliferating cultures have scrambled circadian phase, removing the context in which D-box coherence is interpretable.

## References

- Cowell et al., 1992, Molecular and Cellular Biology — identified E4BP4 as a bZIP transcriptional repressor.
- Mitsui et al., 2001, Genes & Development — showed E4BP4 and the PAR activators act antagonistically at D-boxes in the circadian oscillator.
- Gascoyne et al., 2009, Nature Immunology — E4BP4 is essential for natural killer cell development.
- Kamizono et al., 2009, Journal of Experimental Medicine — Nfil3/E4bp4 is required for NK cell development and maturation in vivo.

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00603 |
| As a percentage | -0.42% |
| FDR, exposure-shuffle null | 0.1089 |
| In TP53-wild-type lines / altered lines | -0.00360 / -0.00751 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | -0.026 raw, -0.182 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

### As a transcription factor, against MG53

| | |
|---|---|
| Regulon size used | 21 targets |
| Activity vs MG53 across exposures (r) | -0.319 (q 2.07e-19) |
| With 3 principal components removed | -0.289 (q 6.59e-16) |
| Within line, across exposures (r) | -0.030 (q 0.013) |
| Percentile against all genes | 1.1 |

## Links

- **Concepts:** [[Transcription factor activity inference]]
- **Findings:** [[Downstream of MG53]], [[Upstream of MG53]]
- **Why this gene is in the vault:** transcription factor, negative rank
- **Indexes:** [[Genes — Map of Content]]

## Sources

- Program and MG53 columns: `mg53_p53/findings/tables/tableD_p53_target_genes.csv`
- Genome-wide screen: `genome_wide/tables/c_screen_genes.csv.gz`
- Curated effector columns: `mg53_p53/findings/tables/p53_effectors_per_gene.csv`
- Transcription-factor activity: `upstream_tf/tables/a1a2_tf_summary.csv`
