---
symbol: MDM4
type: gene
tier: 1
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# MDM4

> [!summary] In one line
> MDM4 — better known in the literature as MDMX or HDMX — is MDM2's paralogue and the second brake on p53: it occludes p53's transactivation domain but, unlike MDM2, is not itself an efficient ubiquitin ligase for p53.

## What it is

MDM4 is built on the same plan as [[MDM2]]: an N-terminal pocket binding the p53 transactivation domain, a central acidic region, and a C-terminal RING. It was found as MDMX, a p53-binding protein with some of MDM2's functional properties.

The asymmetry is at the RING. MDM4's has little demonstrable intrinsic ligase activity toward p53, and instead heterodimerises with MDM2's RING to stimulate MDM2-dependent p53 ubiquitination. MDM4 therefore restrains p53 by two largely non-catalytic routes — blocking the transactivation domain, and setting how well MDM2 works.

Like *Mdm2*-null, *Mdm4*-null embryos die and are rescued by loss of *Trp53*, so MDM4's essential job is also p53 restraint — but the null phenotype differs in timing and tissue bias, read as evidence for non-overlapping control rather than redundancy.

In cancer MDM4 is amplified and overexpressed rather than mutated, concentrated as with MDM2 in tumours that retain wild-type TP53 — retinoblastoma, glioma, and cutaneous melanoma, where it was argued to be a therapeutic target. Splicing is distinctive to this gene: skipping exon 6 yields an unstable short isoform at the expense of full-length protein, and forcing that skipping with antisense oligonucleotides restrains tumour growth — a mechanism with no close MDM2 parallel.

Transcriptionally MDM4 is mostly constitutive, driven from its upstream P1 promoter, but a p53-responsive promoter in the first intron drives a longer isoform, giving MDM4 a weaker version of MDM2's feedback topology.

## Why it appears in this work

MDM4 completes the brake layer: an account of p53 output that names MDM2 and stops there describes half the restraint. Its value here is as a contrast. MDM2 is transcriptionally coupled to p53 through a strong intronic response element and behaves accordingly in [[p53 program P]]; MDM4's coupling is weak and its control is predominantly post-translational — RING partnership, splicing, protein stability. For a study that reads p53 engagement from mRNA, MDM4 is the standing reminder that a regulator can be fully engaged, or fully disengaged, with its transcript barely moving. Whatever the generated block carries here, that asymmetry is why a thin measurement is the expected result.

## What is uncertain

Whether MDM4's RING has any physiologically meaningful ligase activity toward p53 on its own has been argued both ways; the safe statement is that its contribution to p53 turnover runs mainly through MDM2. The division of labour between the paralogues is genuinely unsettled: the differing null phenotypes are compatible with distinct functions and with one function deployed at different times and places, and the literature reads them both ways. MDM4 sits at 1q32, in an arm gained in many epithelial cancers, so an "MDM4 amplification" in copy-number data is often a passenger of 1q gain; attributing a phenotype to MDM4 needs functional experiments, not copy number. The intronic p53-responsive promoter rests on limited work, and how much of total MDM4 mRNA it contributes in an ordinary cell is not established. Finally, a practical caution: most primary papers call this gene MDMX or HDMX, so a literature search on the approved symbol alone misses much of its own literature.

## References

- Shvarts et al., 1996, The EMBO Journal — identified MDMX as a p53-binding protein with some functional properties of MDM2.
- Parant et al., 2001, Nature Genetics — rescue of *Mdm4*-null embryonic lethality by loss of *Trp53*, argued to indicate a pathway not overlapping MDM2's.
- Linares et al., 2003, PNAS — HdmX stimulates Hdm2-mediated ubiquitination and degradation of p53.
- Phillips et al., 2010, Journal of Biological Chemistry — a functional p53-responsive promoter in the first intron drives the longer HDMX-L isoform.
- Gembarska et al., 2012, Nature Medicine — MDM4 as a therapeutic target in cutaneous melanoma.
- Dewaele et al., 2016, Journal of Clinical Investigation — antisense-driven MDM4 exon 6 skipping lowers full-length MDM4 and impairs tumour growth.

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00188 |
| As a percentage | -0.13% |
| FDR, exposure-shuffle null | 0.2411 |
| In TP53-wild-type lines / altered lines | -0.00079 / -0.00255 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | -0.116 raw, -0.032 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

## Links

- **Concepts:** [[The p53 pathway]]
- **Findings:** [[Downstream of MG53]], [[Upstream of MG53]]
- **Why this gene is in the vault:** central to this work
- **Indexes:** [[Genes — Map of Content]]

## Sources

- Program and MG53 columns: `mg53_p53/findings/tables/tableD_p53_target_genes.csv`
- Genome-wide screen: `genome_wide/tables/c_screen_genes.csv.gz`
- Curated effector columns: `mg53_p53/findings/tables/p53_effectors_per_gene.csv`
