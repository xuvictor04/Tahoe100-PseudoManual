---
symbol: AZU1
type: gene
tier: 2
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# AZU1

> [!summary] In one line
> AZU1 encodes azurocidin (CAP37, heparin-binding protein), an antibacterial and chemotactic protein stored in the azurophil granules of neutrophils.

## What it is

Azurocidin is made in promyelocytes and stored in primary granules for release on activation. It folds like an elastase-family serine protease but lacks the catalytic serine and histidine, so it is not an enzyme. It binds heparin and lipopolysaccharide, kills Gram-negative bacteria, attracts monocytes, and increases endothelial permeability — the property behind its use as a sepsis marker. Expression is essentially restricted to bone marrow; the gene lies at 19p13.3 among other azurophil-granule protease genes. No function is established outside the neutrophil lineage, and no link to p53 or to membrane repair is reported.

## Why it appears in this work

AZU1 is not a curated pathway member. It is here because the genome-wide screen ranked it as tracking measured [[MG53 (TRIM72)]] across exposures — a hit with no prior reason to be one. It is not at the TRIM72 locus, so [[Readthrough spillover]] does not apply.

## What is uncertain

Essentially everything that matters here. The transcript sits close to the detection floor, and a promyelocyte-restricted gene reading as weakly present across a pooled cancer-line panel is as easily explained by ambient RNA, or by reads shared with its near-identical neighbours at 19p13.3, as by real expression. Nothing predicts an MG53 relationship, and nothing in this design separates one from a correlation driven by a few lines or by the covariates behind [[Why MG53 is hard to measure here]]. Treat it as a lead for a targeted assay, not a finding.

## References

- Pereira et al., 1990, Journal of Clinical Investigation — characterised CAP37 as a neutrophil-derived chemotactic factor with monocyte specificity.
- Gautam et al., 2001, Nature Medicine — showed heparin-binding protein released from neutrophils causes endothelial hyperpermeability.

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.11227 |
| As a percentage | +8.09% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.12103 / 0.10695 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.673 raw, 0.606 with 3 PCs removed |

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
