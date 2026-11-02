---
symbol: SMIM41
type: gene
tier: 2
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# SMIM41

> [!summary] In one line
> SMIM41 encodes a 93-residue predicted single-pass membrane protein, and nothing about its function is established.

## What it is

What exists is annotation. The gene sits on chromosome 12q13.13, has three small exons, and predicts a protein of about 9 kDa with one transmembrane helix near the middle of the sequence. "Membrane" is its only cellular-component term, assigned by automated inference rather than experiment. There is no identified binding partner, no reported knockout phenotype, no pathway membership, and the mouse orthologue is equally uncharacterised. The SMIM prefix is a naming convention for short predicted membrane proteins, not a family with shared biology, so the other SMIM genes say nothing about this one.

## Why it appears in this work

SMIM41 is here because the genome-wide co-expression step ranked it among the transcripts tracking measured MG53 across this panel. It is not a curated p53 effector, not a transcription factor, and not within the window around [[The TRIM72 locus]], so [[Readthrough spillover]] does not account for it.

## What is uncertain

Everything past its coordinates. The transcript is low in every line, and at low counts a co-expression rank is as compatible with shared depth and ambient-RNA structure as with real covariation — the worry set out in [[Why MG53 is hard to measure here]]. With no known function there is nothing to predict and no mechanism against which the correlation could be judged; whether the open reading frame is appreciably translated has not been shown.

## References

No primary literature I can cite with confidence.

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.10572 |
| As a percentage | +7.60% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.11050 / 0.10283 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.595 raw, 0.532 with 3 PCs removed |

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
