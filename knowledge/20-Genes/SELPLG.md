---
symbol: SELPLG
type: gene
tier: 2
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# SELPLG

> [!summary] In one line
> SELPLG encodes PSGL-1 (CD162), the leukocyte sialomucin that is the principal ligand for P-selectin and lets circulating leukocytes tether and roll on activated endothelium.

## What it is

PSGL-1 is a disulfide-linked homodimeric mucin whose function depends almost entirely on post-translational decoration: high-affinity P-selectin binding needs core-2 O-glycans carrying sialyl-Lewis-x, built by the fucosyltransferase FUT7, together with sulfated tyrosines near the N-terminus. It is expressed on most leukocyte lineages, also binds E- and L-selectin, and PSGL-1-deficient mice show defective P-selectin-dependent neutrophil rolling and recruitment. Beyond adhesion it signals inward, contributing to mechanotransduction and integrin activation, and it has a second identity in immune regulation: VISTA was identified as an acidic-pH-selective ligand for PSGL-1, making the pair a candidate checkpoint operating specifically in the acidic tumour microenvironment.

## Why it appears in this work

SELPLG is among the genes whose expression tracks measured [[MG53 (TRIM72)]] across the panel. It plays no part in p53 signalling, is not in the data-defined [[p53 program P]], and was on no curated list — a haematopoietic gene detected at very low level in these cancer lines, present purely as an empirical co-variation.

## What is uncertain

Nearly all of it. SELPLG carries the readthrough-geometry flag: it sits within 20 kb 3′ of a much higher-expressed same-strand gene, so a share of the reads credited to SELPLG may be transcriptional readthrough rather than its own output ([[Readthrough spillover]]). Because measured MG53 is vulnerable to exactly this ([[Why MG53 is hard to measure here]]), a correlation between the two is as easily a shared artefact of how both are quantified as it is biology. No mechanism connects selectin-mediated adhesion to MG53, and this should not be read as a biological pairing without an orthogonal, locus-aware assay.

## References

- Sako et al., 1993, Cell — expression-cloned PSGL-1 as a functional glycoprotein ligand for P-selectin.
- Pouyani & Seed, 1995, Cell — showed that PSGL-1 recognition by P-selectin requires N-terminal tyrosine sulfation alongside its O-glycan.
- Yang et al., 1999, Journal of Experimental Medicine — PSGL-1-null mice are defective in P-selectin-mediated neutrophil rolling and migration.
- Johnston et al., 2019, Nature — identified VISTA as an acidic-pH-selective ligand for PSGL-1 that suppresses T cells.

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.08782 |
| As a percentage | +6.28% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.09336 / 0.08422 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.773 raw, 0.628 with 3 PCs removed |

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
