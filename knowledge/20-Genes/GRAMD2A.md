---
symbol: GRAMD2A
type: gene
tier: 2
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# GRAMD2A

> [!summary] In one line
> GRAMD2A encodes a tail-anchored ER protein reported to tether the endoplasmic reticulum to PI(4,5)P2-rich patches of the plasma membrane, and nearly all of what is known about it comes from one study.

## What it is

GRAMD2A, formerly GRAMD2, sits at 15q23. Its product is anchored in the ER membrane and presents a cytosolic GRAM domain that binds PI(4,5)P2, and that preference confines it to a subset of ER-plasma-membrane contact sites distinct from those held by the GRAMD1/Aster sterol transporters, alongside the extended synaptotagmins E-Syt2 and E-Syt3. The same work proposed it pre-marks the sites where STIM1 accumulates during store-operated calcium entry, making it an organiser of contact-site identity rather than a transporter. Its kinship to the yeast Lam/Ltc sterol-transfer proteins is domain homology only; no transfer activity has been shown, there is no animal knockout, and expression is low and uneven.

## Why it appears in this work

GRAMD2A is here only because the genome-wide screen ranked it as tracking measured MG53. The coincidence deserves naming — [[MG53 (TRIM72)]] acts at the injured plasma membrane and this organises plasma-membrane contact sites — but naming it is as far as this design reaches. At 15q23 it is far from TRIM72, so [[Readthrough spillover]] cannot account for it.

## What is uncertain

This is effectively a one-paper gene, and that paper's most interesting claim is its least settled: reviewers noted roughly half of STIM1 puncta formed at sites GRAMD2A did not mark. Antibody staining in the Human Protein Atlas puts the protein in nucleoli and nuclear speckles, irreconcilable with a tail-anchored ER tether; one localisation is wrong, most likely the antibody's. Nothing links the gene to p53, and at the level seen here ambient RNA stays live; see [[Why MG53 is hard to measure here]].

## References

- Besprozvannaya et al., 2018, eLife — showed GRAMD2a marks a PI(4,5)P2-dependent subset of ER-PM contact sites distinct from GRAMD1a's, and proposed a role in STIM1 recruitment.

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.10794 |
| As a percentage | +7.77% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.11489 / 0.10373 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.723 raw, 0.520 with 3 PCs removed |

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
