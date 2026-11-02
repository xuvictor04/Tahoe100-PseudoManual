---
symbol: TEF
type: gene
tier: 2
tags: [gene, transcription-factor]
generated_by: knowledge/_build/build_vault.py
---

# TEF

> [!abstract] Knowledge layer: needs a short written note
> Nothing is written about this gene yet. Add `knowledge/20-Genes/_knowledge/TEF.md` and rebuild; see [[How this vault is built]].

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.01401 |
| As a percentage | +0.98% |
| FDR, exposure-shuffle null | 0.0427 |
| In TP53-wild-type lines / altered lines | 0.02115 / 0.00967 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.191 raw, -0.039 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

### As a transcription factor, against MG53

| | |
|---|---|
| Regulon size used | 12 targets |
| Activity vs MG53 across exposures (r) | 0.285 (q 1.12e-16) |
| With 3 principal components removed | 0.232 (q 1.05e-11) |
| Within line, across exposures (r) | 0.020 (q 0.059) |
| Percentile against all genes | 99.7 |

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
