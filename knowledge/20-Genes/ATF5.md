---
symbol: ATF5
type: gene
tier: 2
tags: [gene, transcription-factor]
generated_by: knowledge/_build/build_vault.py
---

# ATF5

> [!abstract] Knowledge layer: needs a short written note
> Nothing is written about this gene yet. Add `knowledge/20-Genes/_knowledge/ATF5.md` and rebuild; see [[How this vault is built]].

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00230 |
| As a percentage | +0.16% |
| FDR, exposure-shuffle null | 0.5765 |
| In TP53-wild-type lines / altered lines | 0.00411 / 0.00120 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.427 raw, 0.175 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

### As a transcription factor, against MG53

| | |
|---|---|
| Regulon size used | 25 targets |
| Activity vs MG53 across exposures (r) | 0.359 (q 3.27e-26) |
| With 3 principal components removed | 0.373 (q 1.03e-28) |
| Within line, across exposures (r) | -0.007 (q 0.831) |
| Percentile against all genes | 99.9 |

## Links

- **Concepts:** [[Transcription factor activity inference]]
- **Findings:** [[Downstream of MG53]], [[Upstream of MG53]]
- **Why this gene is in the vault:** transcription factor, positive rank
- **Indexes:** [[Genes — Map of Content]]

## Sources

- Program and MG53 columns: `mg53_p53/findings/tables/tableD_p53_target_genes.csv`
- Genome-wide screen: `genome_wide/tables/c_screen_genes.csv.gz`
- Curated effector columns: `mg53_p53/findings/tables/p53_effectors_per_gene.csv`
- Transcription-factor activity: `upstream_tf/tables/a1a2_tf_summary.csv`
