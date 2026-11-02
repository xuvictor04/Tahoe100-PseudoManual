---
symbol: HJURP
type: gene
tier: 2
aliases: [FAKTS]
p53_direction: repressed by p53
program_arm: P down (WT-selective repression)
median_line_cpm: 51.18
mg53_verdict: none
tags: [gene, p53-program, p53-repressed]
generated_by: knowledge/_build/build_vault.py
---

# HJURP

> [!summary] In one line
> HJURP is the dedicated chaperone that holds newly made CENP-A and deposits it at centromeres, so it is the gene that decides where new centromeric chromatin is built.

## What it is

HJURP was picked up twice over — once as a protein binding a Holliday-junction-like structure, once as a transcript over-expressed in lung tumours, the source of the alias URLC9. Its real job emerged from CENP-A proteomics: HJURP binds the CENP-A/H4 dimer through a conserved N-terminal domain, keeps it soluble, and loads it into centromeric chromatin in a narrow window at mitotic exit and early G1. Without it, new CENP-A is not deposited, the existing pool is diluted by replication, and kinetochores fail — placing HJURP upstream of the CENP-A reader [[CENPN]] in one assembly pathway. Beyond that the literature is largely correlative: high HJURP associates with poor outcome in several tumour series, a weak basis for functional claims.

## Why it appears in this work

HJURP was selected into the repression arm of [[p53 program P]], falling selectively in TP53-wild-type lines under p53 activators. For a replication-coupled chromatin factor the expected route is indirect, through p21 and DREAM rather than p53 at the promoter; see [[The p21-DREAM axis]]. Its presence reinforces reading that arm as cells leaving the cycle.

## What is uncertain

Nothing establishes HJURP as a p53 target in any direct sense, and its program membership here is unstable across folds, so hold it more loosely than the arm's core members. There is also a timing problem: HJURP acts in a short window at mitotic exit, so a 24 h transcript measurement in an arresting population reports cell-cycle distribution rather than centromere assembly. The prognosis literature is expression-correlation, not evidence that HJURP drives those phenotypes.

## References

- Foltz et al., 2009, Cell — showed HJURP mediates centromere-specific assembly of CENP-A nucleosomes.
- Dunleavy et al., 2009, Cell — identified HJURP as a cell-cycle-dependent CENP-A deposition and maintenance factor.
- Shuaib et al., 2010, PNAS — mapped the conserved N-terminal domain through which HJURP binds CENP-A.
- Engeland, 2018, Cell Death and Differentiation — review of p53-p21-DREAM-mediated repression of cell-cycle genes.

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 51.18 CPM |
| Lines where detected | 49 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **repressed by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P down (WT-selective repression) |
| Rank in the program | — of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 0.872× |
| Wild-type minus altered | 0.927× |
| Compounds moving it up in WT lines | 26 of 98 |
| Direction mixed? | no |
| Program membership stability | unstable (0-1 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00325 |
| As a percentage | -0.22% |
| FDR, exposure-shuffle null | 0.4626 |
| In TP53-wild-type lines / altered lines | 0.00068 / -0.00546 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | -0.004 raw, 0.174 with 3 PCs removed |

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
