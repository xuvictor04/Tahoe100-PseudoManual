---
symbol: LDHC
type: gene
tier: 2
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# LDHC

> [!summary] In one line
> LDHC encodes the C subunit of lactate dehydrogenase, assembling into the germ-cell-restricted LDH-C4 isozyme that supports sperm energy metabolism.

## What it is

The sixth LDH isozyme was found in human testis in the 1960s and called LDH-X before the subunit got its own gene at 11p15. LDH-C4 is a homotetramer of C subunits catalysing the same pyruvate-lactate interconversion as LDH-A and LDH-B but with a distinct kinetic profile, and normally confined to spermatocytes, spermatids and mature sperm. Loss of C-subunit activity in mouse impairs sperm motility, capacitation and fertilisation, and reduced activity is associated with human male infertility. Because the promoter is silent outside the germline but de-represses in tumours, LDHC is grouped with the cancer-testis antigens, and HLA-A2-restricted peptides from it have been proposed as immunotherapy targets. Reports of a role in tumour motility come from few models.

## Why it appears in this work

LDHC is in the vault only because the genome-wide screen ranked it as tracking measured MG53. It is not a curated p53 effector and 11p15 is far from TRIM72, so [[Readthrough spillover]] does not apply. Worth noting: its expression in these lines is an epigenetic accident of cancer-testis de-repression, not a programmed state.

## What is uncertain

The measurement is the weak point. LDHC shares substantial sequence identity with LDHA and LDHB, both abundant in essentially every cancer line, so a low LDHC count is exactly where read misassignment would show up — importing the behaviour of a major glycolytic gene into this feature. Cancer-testis expression is also strongly line-specific, so an apparent association could be carried by the few lines that de-repress the locus at all; see [[Why MG53 is hard to measure here]].

## References

- Wu et al., 2022, Frontiers in Oncology — review of LDH-C4 in germ-cell metabolism, male infertility and its reclassification as a cancer-testis antigen.
- Naik and Decock, 2023, Frontiers in Oncology — commentary on that review, noting the authors' own earlier identification of HLA-A2-restricted LDHC peptides that elicit cytotoxic T-cell responses.

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.11991 |
| As a percentage | +8.67% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.12646 / 0.11593 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.776 raw, 0.622 with 3 PCs removed |

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
