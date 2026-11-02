---
symbol: KIF17
type: gene
tier: 2
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# KIF17

> [!summary] In one line
> KIF17 is a homodimeric kinesin-2 motor that carries cargo outward along microtubules in dendrites and into cilia.

## What it is

KIF17 is the vertebrate counterpart of *C. elegans* OSM-3: a processive, plus-end-directed homodimer, unlike heterotrimeric kinesin-II. Its best-established cargo is neuronal. The KIF17 tail binds the PDZ domain of mLin-10/Mint1, linking the motor to a scaffold carrying NMDA-receptor NR2B subunits, and this is the route by which NR2B-containing vesicles move into dendrites; CaMKII phosphorylation of the same region releases the cargo. A second, largely separate literature places KIF17 in cilia, where it enters the axoneme, associates with IFT-B, and is required for building photoreceptor outer segments. Mouse knockouts are viable, with impaired NR2B transport and memory deficits. Outside neurons and ciliated cells little is described.

## Why it appears in this work

KIF17 is in the vault only because the genome-wide screen ranked it as tracking measured MG53. It is not a curated p53 effector, not a transcription factor, and 1p36 is nowhere near TRIM72, so [[Readthrough spillover]] does not explain it. Note that it shares nothing with the kinesin-5 spindle motor [[KIF11]] beyond distant motor-domain ancestry.

## What is uncertain

Both of KIF17's established settings — dendrites and cilia — are largely absent from pooled cancer lines, so there is no known function here for a correlation to act through. The transcript is low in these lines, putting ambient RNA and mapping ambiguity across the conserved kinesin motor domain in play; see [[Why MG53 is hard to measure here]]. Nothing in the literature connects KIF17 to p53 or to membrane repair, and nothing in this design separates a real association from one driven by a few lines.

## References

- Setou et al., 2000, Science — showed KIF17 transports NR2B-containing vesicles in dendrites via mLin-10/Mint1.
- Insinna et al., 2008, Developmental Biology — showed Kif17 is required for vertebrate photoreceptor outer-segment development.

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.08870 |
| As a percentage | +6.34% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.10145 / 0.08153 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.651 raw, 0.457 with 3 PCs removed |

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
