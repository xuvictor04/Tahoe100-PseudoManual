---
symbol: MEF2B
type: gene
tier: 1
tags: [gene, muscle-tf]
generated_by: knowledge/_build/build_vault.py
---

# MEF2B

> [!abstract] Knowledge layer: needs a written note — it is well studied and central here
> Nothing is written about this gene yet. Add `knowledge/20-Genes/_knowledge/MEF2B.md` and rebuild; see [[How this vault is built]].

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00807 |
| As a percentage | +0.56% |
| FDR, exposure-shuffle null | 0.0361 |
| In TP53-wild-type lines / altered lines | 0.00713 / 0.00865 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | -0.016 raw, -0.133 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

> [!info] One of TRIM72's native-tissue drivers
> MG53 is a striated-muscle protein and this factor drives it there. In this panel of cancer
> lines it is expressed at trace level (13.77 CPM), which is why the muscle programme is not what moves MG53 here.

## Links

- **Concepts:** [[Transcription factor activity inference]]
- **Findings:** [[Downstream of MG53]], [[Upstream of MG53]]
- **Why this gene is in the vault:** muscle promoter TF (TRIM72's native drivers)
- **Indexes:** [[Genes — Map of Content]]

## Sources

- Program and MG53 columns: `mg53_p53/findings/tables/tableD_p53_target_genes.csv`
- Genome-wide screen: `genome_wide/tables/c_screen_genes.csv.gz`
- Curated effector columns: `mg53_p53/findings/tables/p53_effectors_per_gene.csv`
