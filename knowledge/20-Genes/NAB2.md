---
symbol: NAB2
type: gene
tier: 2
tags: [gene, transcription-factor]
generated_by: knowledge/_build/build_vault.py
---

# NAB2

> [!summary] In one line
> NAB2 encodes a transcriptional corepressor with no DNA-binding domain of its own, acting through EGR-family factors to shut down their output.

## What it is

NAB2 — NGFI-A-binding protein 2, also known as EGR1-binding protein 2 or MADER — was isolated as a repressor of NGFI-A (EGR1) and Krox20 (EGR2). Its first conserved domain binds the R1 region of NGFI-A, and repression is carried out at least partly by recruiting the CHD4 subunit of the NuRD remodelling and deacetylase complex. The circuit is a feedback loop: EGR factors bind sites in the NAB2 promoter and induce it, so NAB2 accumulates after the immediate-early burst and terminates it. The gene sits at 12q13.3, where a recurrent NAB2-STAT6 fusion defines solitary fibrous tumour.

## Why it appears in this work

NAB2 is scored as a factor in the regulon-based activity step. The thing to hold onto is that it has no targets of its own: its regulon is borrowed from EGR, so "NAB2 activity" is an immediate-early readout with an inverted sign. See [[Transcription factor activity inference]].

## What is uncertain

Its regulon in this collection holds only a handful of targets, which puts the score close to a single-gene measurement; and because NAB2 represses, whether coherent movement in those targets means high or low activity depends on sign conventions the collections apply inconsistently to repressors. Immediate-early signalling is also moved by the stress and translation-inhibiting compounds that drive [[Readthrough spillover]]. One practical trap: the yeast protein Nab2 is an unrelated poly(A)-RNA-binding protein, and much of what a literature search returns under this name concerns that.

## References

- Svaren et al., 1996, Molecular and Cellular Biology — identified NAB2 as a corepressor of NGFI-A and Krox20 induced by proliferative and differentiative stimuli.
- Robinson et al., 2013, Nature Genetics — identified recurrent NAB2-STAT6 fusions in solitary fibrous tumour.
- Chmielecki et al., 2013, Nature Genetics — independently found the recurrent NAB2-STAT6 fusion in solitary fibrous tumours.

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00297 |
| As a percentage | -0.21% |
| FDR, exposure-shuffle null | 0.6468 |
| In TP53-wild-type lines / altered lines | -0.00355 / -0.00260 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | -0.194 raw, 0.019 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

### As a transcription factor, against MG53

| | |
|---|---|
| Regulon size used | 6 targets |
| Activity vs MG53 across exposures (r) | -0.377 (q 8.88e-28) |
| With 3 principal components removed | -0.365 (q 5.93e-27) |
| Within line, across exposures (r) | -0.066 (q 0.004) |
| Percentile against all genes | 0.6 |

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
