---
symbol: TP53BP1
type: gene
tier: 1
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# TP53BP1

> [!summary] In one line
> TP53BP1 encodes 53BP1, a chromatin adaptor that reads the histone marks around a double-strand break and steers repair toward end-joining — named for a p53 interaction that is still the least settled thing about it.

## What it is

53BP1 is a large, mostly scaffold-like protein with no catalytic activity. It was isolated in a two-hybrid screen as a protein binding wild-type but not mutant p53, through tandem C-terminal BRCT domains that contact the p53 core domain — hence the name. Its principal characterised job, however, is in double-strand break repair. Nucleosomes flanking a break carry constitutive H4K20me2 and, after RNF168 acts, H2A Lys15 ubiquitylation; 53BP1 reads both simultaneously, with its tandem Tudor domain on the methyl mark and a short ubiquitylation-dependent recruitment motif on the ubiquitin, which is why it concentrates into the microscopically visible foci that define a damaged nucleus. ATM then phosphorylates its N-terminal SQ/TQ cluster, creating a platform for RIF1 and the shieldin complex, which blocks CtIP, MRE11 and EXO1 from resecting the break ends. The consequence is pathway choice: 53BP1 protects ends for non-homologous end joining and suppresses homologous recombination. That logic is the basis of one of the cleanest genetic interactions in the field — loss of 53BP1 restores recombination and viability to BRCA1-deficient cells and is a recognised route to PARP-inhibitor resistance. Mouse knockouts show DNA-damage-response defects, impaired class switch recombination and tumour susceptibility, and 53BP1 behaves as a haploinsufficient tumour suppressor cooperating with p53. The p53 connection has been revisited more recently: 53BP1 does promote p53-dependent transcription and cell-fate decisions, through a mechanism separable from its repair function.

## Why it appears in this work

53BP1 sits upstream of p53, not downstream of it. It is part of the apparatus that converts a genotoxic drug into an ATM-dependent signal strong enough to stabilise p53, so it helps set how much p53 output a compound produces — but it is not itself a p53 transcriptional target, and it is not a member of [[p53 program P]]. That distinction is the main reason to read this note: a gene symbol beginning "TP53" in a p53-themed vault invites the assumption that its induction reports p53 activity, and here it does not. See [[The p53 pathway]].

## What is uncertain

The interaction the gene is named for is the weakest-supported part of its biology. Whether BRCT-mediated p53 binding contributes meaningfully to p53 activity in cells, as opposed to being a detectable affinity, has never been settled; the more recent evidence for a 53BP1 contribution to p53-dependent transcription points to a different, oligomerisation- and chromatin-dependent mechanism, and rests on a limited number of systems. Separately, 53BP1 mRNA is a poor proxy for 53BP1 function: recruitment depends on H4K20me2 density, RNF168 activity, ATM phosphorylation and competition with BRCA1-associated factors, none of which move with the transcript. Its effect on repair outcome is also strongly context-dependent — pro-survival in some settings, actively deleterious in BRCA1-mutant cells.

## References

- Iwabuchi et al., 1994, PNAS — identified two proteins binding wild-type but not mutant p53, one of which became 53BP1.
- Schultz et al., 2000, Journal of Cell Biology — placed 53BP1 as an early participant in the cellular response to double-strand breaks.
- Botuyan et al., 2006, Cell — structural basis for methylation-state-specific recognition of H4K20me2 by the 53BP1 Tudor domain.
- Bunting et al., 2010, Cell — 53BP1 inhibits homologous recombination in Brca1-deficient cells by blocking end resection.
- Fradet-Turcotte et al., 2013, Nature — 53BP1 is a reader of the damage-induced H2A Lys15 ubiquitin mark.
- Cuella-Martin et al., 2016, Molecular Cell — separated 53BP1's DNA-repair and p53-dependent cell-fate functions mechanistically.

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00275 |
| As a percentage | -0.19% |
| FDR, exposure-shuffle null | 0.0996 |
| In TP53-wild-type lines / altered lines | -0.00120 / -0.00369 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | -0.110 raw, -0.045 with 3 PCs removed |

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
