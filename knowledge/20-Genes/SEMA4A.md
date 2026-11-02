---
symbol: SEMA4A
type: gene
tier: 2
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# SEMA4A

> [!summary] In one line
> SEMA4A encodes semaphorin 4A, a transmembrane class IV semaphorin signalling through plexins, neuropilin-1 and Tim-2, with reported roles in T-cell activation, angiogenesis and photoreceptor survival.

## What it is

A sema domain plus an Ig-like domain on a membrane anchor, so Sema4A acts in trans at cell–cell contact; a shed soluble form also circulates. Its best-supported role is immune: expressed on dendritic cells and macrophages, it enhances T-cell priming and Th1-type differentiation, with Tim-2 reported as the T-cell-side receptor. In the vasculature, endothelial Sema4A signalling through plexin-D1 reportedly dampens VEGF-driven angiogenesis. In the eye, SEMA4A variants were reported in retinitis pigmentosa and cone–rod dystrophy, and mouse work ties it to endosomal sorting in retinal pigment epithelium needed for photoreceptor survival. The through-line: a context-dependent ligand whose output depends on which receptor its partner cell presents.

## Why it appears in this work

SEMA4A is among the genes whose expression tracks measured [[MG53 (TRIM72)]] across the panel. It is not in the data-defined [[p53 program P]], has no reported relationship to p53, and appears only as an empirical co-variation with no prior reason to be one.

## What is uncertain

SEMA4A carries the readthrough-geometry flag: it sits within 20 kb 3′ of a much higher-expressed same-strand gene, so some reads credited to it may be that neighbour's ([[Readthrough spillover]]). Measured MG53 has the same weakness ([[Why MG53 is hard to measure here]]), making a shared-artefact explanation at least as plausible as a shared regulator. The biology is unsettled too: the immune work rests on mouse systems and a receptor, Tim-2, whose human counterpart is unclear, and the dominant retinal variant from the original genetics paper has since been reassessed as a common polymorphism, so that gene–disease claim is weaker than database entries imply.

## References

- Kumanogoh et al., 2002, Nature — showed that Sema4A enhances T-cell activation and interacts with Tim-2.
- Abid et al., 2006, Journal of Medical Genetics — first reported SEMA4A variants in retinitis pigmentosa and cone–rod dystrophy; the dominant variant has since been questioned.
- Kumanogoh & Kikutani, 2013, Nature Reviews Immunology — review of semaphorin signalling through plexins and neuropilins in immunity.

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.13252 |
| As a percentage | +9.62% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.15476 / 0.12130 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.770 raw, 0.665 with 3 PCs removed |

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
