---
symbol: COL20A1
type: gene
tier: 2
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# COL20A1

> [!summary] In one line
> COL20A1 encodes collagen XX, a barely characterised FACIT-family collagen known almost entirely from chick embryonic tissue.

## What it is

Collagen α1(XX) was cloned from chick cornea and assigned to the FACIT subfamily — fibril-associated collagens with interrupted triple helices. Interrupted collagenous stretches sit alongside fibronectin type III repeats and a von Willebrand factor A domain, the layout of a protein that decorates fibrils rather than forming them. In chick it was found in cornea, cartilage and tendon; the human gene lies at 20q13.33, expressed at low level and biased toward brain and testis. After that the record thins fast: no knockout phenotype, no validated partner, no demonstrated activity — the database annotations are inferred from domain content, and no gene-disease association is established.

## Why it appears in this work

COL20A1 is not a curated pathway member. It is here because the genome-wide screen ranked it as tracking measured [[MG53 (TRIM72)]] — an empirical hit with no prior reason to be one. At 20q13.33 it is nowhere near TRIM72, so [[Readthrough spillover]] cannot explain it.

## What is uncertain

Almost everything. The transcript sits low enough that ambient RNA is a live explanation, and the repetitive Gly-X-Y sequence shared across the collagen family is where multi-mapping reads land imprecisely. With no established function there is no mechanism to check a correlation against, and nothing here separates one from a few-line effect or from the covariates in [[Why MG53 is hard to measure here]]. A lead for a targeted assay, not a finding.

## References

- Koch et al., 2001, Journal of Biological Chemistry — cloned α1(XX) collagen from chick cornea and assigned it to the FACIT subfamily.

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.09359 |
| As a percentage | +6.70% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.10733 / 0.08662 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.527 raw, 0.568 with 3 PCs removed |

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
