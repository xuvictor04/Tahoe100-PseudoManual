---
symbol: USP1
type: gene
tier: 2
aliases: [ubiquitin specific peptidase 1]
p53_direction: repressed by p53
program_arm: P down (WT-selective repression)
median_line_cpm: 76.53
mg53_verdict: none
tags: [gene, p53-program, p53-repressed]
generated_by: knowledge/_build/build_vault.py
---

# USP1

> [!summary] In one line
> USP1 is a deubiquitinase that, with its cofactor UAF1, strips monoubiquitin from FANCD2/FANCI and from PCNA, resetting the Fanconi-anaemia and translesion-synthesis arms of DNA damage tolerance.

## What it is

USP1 is a cysteine protease of the USP family, nearly inert until it binds WDR48/UAF1 (see [[WDR48]]). Two substrates define it: monoubiquitinated [[FANCD2]]/FANCI, whose deubiquitination is needed to complete crosslink repair, and monoubiquitinated PCNA, whose deubiquitination ends recruitment of the translesion polymerase eta ([[POLH]]). USP1 is therefore a reset switch, not a repair activator or inhibitor; both excess and absence are deleterious. Its own regulation is largely post-translational: it autocleaves after UV damage, letting PCNA-Ub persist, and APC/C degrades it in G1. Its mRNA peaks in S phase. USP1 inhibitors are in clinical development for BRCA1/2-mutant tumours, where losing its activity is synthetic-lethal.

## Why it appears in this work

USP1 sits in the repression arm of [[p53 program P]]: one of the replication-and-repair genes that fall when p53 is activated, through [[CDKN1A]] and [[The p21-DREAM axis]] rather than a response element of its own. A fall in USP1 belongs to the same signal as a fall in [[CCNE2]] or [[EXO1]], and counts as p53 output only after sign conversion ([[Signing genes by p53 direction]]).

## What is uncertain

USP1 is almost certainly an indirect p53 target: no validated response element is described at the locus, and its downregulation fits loss of E2F-driven transcription and DREAM-mediated repression downstream of p21. A decrease therefore reports cell-cycle exit at least as much as p53 itself, and in a panel where many compounds arrest cells for non-p53 reasons the two are hard to separate. Its activity is also set post-translationally, so the transcript is a weak proxy for how much deubiquitination actually happens.

## References

- Nijman et al., 2005, Molecular Cell — identified USP1 as the deubiquitinase for monoubiquitinated FANCD2.
- Huang et al., 2006, Nature Cell Biology — showed USP1 regulates PCNA monoubiquitination and translesion synthesis, and autocleaves after UV damage.
- Cohn et al., 2007, Molecular Cell — identified UAF1/WDR48 as the cofactor required for USP1 activity.
- Liang et al., 2014, Nature Chemical Biology — ML323, a selective USP1/UAF1 inhibitor, potentiates cisplatin sensitivity.
- Fischer et al., 2016, Nucleic Acids Research — described the p53-p21-DREAM-CDE/CHR route for indirect repression of cell-cycle genes after p53 activation.

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 76.53 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no same-strand neighbour close enough to spill into it |

### What p53 does to it

| | |
|---|---|
| Direction | **repressed by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P down (WT-selective repression) |
| Rank in the program | — of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 0.963× |
| Wild-type minus altered | 0.968× |
| Compounds moving it up in WT lines | 33 of 98 |
| Direction mixed? | no |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00006 |
| As a percentage | -0.00% |
| FDR, exposure-shuffle null | 0.9829 |
| In TP53-wild-type lines / altered lines | 0.00106 / -0.00074 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | 0.349 raw, 0.077 with 3 PCs removed |

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
