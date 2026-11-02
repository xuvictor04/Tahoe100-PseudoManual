---
symbol: FNDC7
type: gene
tier: 2
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# FNDC7

> [!summary] In one line
> FNDC7 encodes a predicted secreted protein built from fibronectin type III repeats, and essentially nothing about its function is established.

## What it is

What is known is sequence and little else. The open reading frame predicts a signal peptide and a string of fibronectin type III domains — a module shared with fibronectin itself and many cell-surface proteins, and the only basis for any family assignment. Expression is low wherever surveyed, most consistently in testis. Everything functional is annotation, not observation: "secreted" and "extracellular region" come from domain content, not experiment. There is no published knockout, no identified ligand or receptor, no characterised partner, no replicated disease association. No connection has been reported between FNDC7 and p53, membrane repair, or [[MG53 (TRIM72)]].

## Why it appears in this work

FNDC7 is here only because the genome-wide screen ranked it as tracking measured MG53. It is not a curated p53 effector, not a transcription factor, and not near the TRIM72 locus, so [[Readthrough spillover]] does not account for it.

## What is uncertain

Everything. The transcript is near the detection floor, and a testis-biased gene reading as weakly present across a pooled cancer-line panel is as easily explained by ambient RNA or by reads shared with other FN3-domain paralogues as by real expression. With no established function there is no prediction to test and no mechanism against which a correlation could be judged. Nothing here separates an MG53 association from one driven by a few lines or by the covariates in [[Why MG53 is hard to measure here]]. This note records a screen rank, not biology.

## References

No primary literature I can cite with confidence.

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.14084 |
| As a percentage | +10.25% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.13293 / 0.14564 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.863 raw, 0.761 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

## Links

- **Concepts:** [[The p53 pathway]]
- **Findings:** [[Downstream of MG53]], [[Upstream of MG53]]
- **Why this gene is in the vault:** tracks MG53 genome-wide
- **Indexes:** [[Genes — Map of Content]]

## Sources

- Program and MG53 columns: `mg53_p53/findings/tables/tableD_p53_target_genes.csv`
- Genome-wide screen: `genome_wide/tables/c_screen_genes.csv.gz`
- Curated effector columns: `mg53_p53/findings/tables/p53_effectors_per_gene.csv`
