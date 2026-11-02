---
symbol: BRCA2
type: gene
tier: 2
aliases: [FANCD1]
p53_direction: repressed by p53
program_arm: P down (WT-selective repression)
median_line_cpm: 47.76
mg53_verdict: none
tags: [gene, p53-program, p53-repressed]
generated_by: knowledge/_build/build_vault.py
---

# BRCA2

> [!summary] In one line
> BRCA2 is the mediator that loads RAD51 onto resected DNA ends for homologous recombination, and one of the two classical hereditary breast and ovarian cancer genes.

## What it is

BRCA2 is a very large protein whose BRC repeats and DNA-binding domain deliver RAD51 to single-stranded DNA and displace RPA, the nucleation step of homologous recombination. The same activity stabilises RAD51 on stalled forks, a function separable from repair of frank breaks. Monoallelic germline loss confers raised risk of breast, ovarian, pancreatic and prostate cancer; biallelic hypomorphic loss causes the FANCD1 subtype of Fanconi anaemia. Loss of BRCA2 is the canonical setting for PARP-inhibitor synthetic lethality and platinum sensitivity; restored recombination is a recognised resistance route.

## Why it appears in this work

BRCA2 is in the repression arm of [[p53 program P]]: its level falls modestly, and selectively in TP53-wild-type lines, under compounds that activate p53. That is what [[The p21-DREAM axis]] predicts for a proliferation-coupled gene: p53 reaches such genes indirectly, through p21 and the RB-E2F and DREAM complexes. Its presence supports reading that arm as a cell-cycle-exit footprint.

## What is uncertain

Whether p53 represses BRCA2 at all in the direct sense is doubtful; the better-supported view is that p53 is an activator whose apparent repression of cell-cycle genes is relayed through p21. The direction label below is also a selection outcome, so it describes the gene rather than demonstrating specificity. And transcript level is a weak proxy for recombination proficiency: a modest fall in BRCA2 mRNA at 24 h is not evidence of induced "BRCAness".

## References

- Wooster et al., 1995, Nature — identification of the BRCA2 gene.
- Moynahan et al., 2001, Molecular Cell — BRCA2 is required for homology-directed repair of double-strand breaks.
- Howlett et al., 2002, Science — biallelic BRCA2 mutations cause Fanconi anaemia, defining FANCD1.
- Jensen et al., 2010, Nature — purified human BRCA2 promotes RAD51-mediated recombination.
- Farmer et al., 2005, Nature — PARP inhibition is selectively lethal in BRCA-deficient cells.
- Engeland, 2018, Cell Death and Differentiation — review of indirect transcriptional repression through the p53-p21-DREAM route.

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 47.76 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **repressed by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P down (WT-selective repression) |
| Rank in the program | — of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 0.929× |
| Wild-type minus altered | 0.950× |
| Compounds moving it up in WT lines | 20 of 98 |
| Direction mixed? | no |
| Program membership stability | partial (2-3 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00244 |
| As a percentage | +0.17% |
| FDR, exposure-shuffle null | 0.5596 |
| In TP53-wild-type lines / altered lines | -0.00061 / 0.00429 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | 0.097 raw, 0.191 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

## Links

- **Concepts:** [[The p53 pathway]], [[p53 program P]], [[The p21-DREAM axis]]
- **Findings:** [[Downstream of MG53]], [[Upstream of MG53]]
- **Why this gene is in the vault:** p53 program, repression arm
- **Indexes:** [[Genes — Map of Content]]

## Sources

- Program and MG53 columns: `mg53_p53/findings/tables/tableD_p53_target_genes.csv`
- Genome-wide screen: `genome_wide/tables/c_screen_genes.csv.gz`
- Curated effector columns: `mg53_p53/findings/tables/p53_effectors_per_gene.csv`
