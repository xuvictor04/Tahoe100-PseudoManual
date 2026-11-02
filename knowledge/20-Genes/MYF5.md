---
symbol: MYF5
type: gene
tier: 1
tags: [gene, muscle-tf, transcription-factor]
generated_by: knowledge/_build/build_vault.py
---

# MYF5

> [!abstract] Knowledge layer: needs a written note — it is well studied and central here
> Nothing is written about this gene yet. Add `knowledge/20-Genes/_knowledge/MYF5.md` and rebuild; see [[How this vault is built]].

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### As a transcription factor, against MG53

| | |
|---|---|
| Regulon size used | 14 targets |
| Activity vs MG53 across exposures (r) | -0.020 (q 0.618) |
| With 3 principal components removed | 0.048 (q 0.184) |
| Within line, across exposures (r) | -0.026 (q 0.045) |
| Percentile against all genes | 45.6 |

> [!info] One of TRIM72's native-tissue drivers
> MG53 is a striated-muscle protein and this factor drives it there. In this panel of cancer
> lines it is absent from the expressed gene list (— CPM), which is why the muscle programme is not what moves MG53 here.

## Links

- **Concepts:** [[Transcription factor activity inference]]
- **Findings:** [[Downstream of MG53]], [[Upstream of MG53]]
- **Why this gene is in the vault:** muscle promoter TF (TRIM72's native drivers)
- **Indexes:** [[Genes — Map of Content]]

## Sources

- Program and MG53 columns: `mg53_p53/findings/tables/tableD_p53_target_genes.csv`
- Genome-wide screen: `genome_wide/tables/c_screen_genes.csv.gz`
- Curated effector columns: `mg53_p53/findings/tables/p53_effectors_per_gene.csv`
- Transcription-factor activity: `upstream_tf/tables/a1a2_tf_summary.csv`
