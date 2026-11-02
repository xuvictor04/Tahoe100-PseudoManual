---
symbol: TGIF1
type: gene
tier: 2
tags: [gene, transcription-factor]
generated_by: knowledge/_build/build_vault.py
---

# TGIF1

> [!abstract] Knowledge layer: needs a short written note
> Nothing is written about this gene yet. Add `knowledge/20-Genes/_knowledge/TGIF1.md` and rebuild; see [[How this vault is built]].

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00274 |
| As a percentage | -0.19% |
| FDR, exposure-shuffle null | 0.5616 |
| In TP53-wild-type lines / altered lines | 0.00339 / -0.00646 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | -0.268 raw, -0.009 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

### As a transcription factor, against MG53

| | |
|---|---|
| Regulon size used | 7 targets |
| Activity vs MG53 across exposures (r) | -0.252 (q 4.47e-13) |
| With 3 principal components removed | -0.174 (q 4.90e-07) |
| Within line, across exposures (r) | -0.029 (q 0.042) |
| Percentile against all genes | 8.2 |

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
