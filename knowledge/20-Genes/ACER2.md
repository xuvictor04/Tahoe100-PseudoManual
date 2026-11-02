---
symbol: ACER2
type: gene
tier: 1
aliases: [alkaline ceramidase 2]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
curated_effector: true
effector_role: metabolism / redox
median_line_cpm: 13.72
mg53_verdict: up with MG53
mg53_effect_on_p53_output: toward MORE p53 output
tags: [curated-effector, gene, mg53-associated, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# ACER2

> [!summary] In one line
> ACER2 is a Golgi alkaline ceramidase that hydrolyses ceramide to sphingosine, and it is one of the most cleanly p53-inducible genes in sphingolipid metabolism.

## What it is

ACER2 (alkaline ceramidase 2) is one of three human alkaline ceramidases. It is a multi-pass membrane enzyme of the Golgi that hydrolyses unsaturated long-chain ceramides and dihydroceramides into a free fatty acid plus sphingosine or dihydrosphingosine; its activity is reported to depend on calcium and to have an alkaline pH optimum. Sphingosine released this way is the substrate for the sphingosine kinases, so ACER2 sits at a control point in the sphingolipid rheostat: it drains the ceramide pool, which signals toward arrest and death, and feeds the sphingosine and sphingosine-1-phosphate pools, which signal toward survival and migration. Which of those two consequences dominates depends on how much flux passes through the step.

Its regulation is what makes it interesting here. ACER2 mRNA rises sharply after DNA damage, and the induction appears to be a direct p53 effect: the dominant promoter lies inside the first intron and carries p53 consensus sites, and mutating the first conserved site abolishes p53-driven reporter activity. Downstream, doxorubicin raises ACER2 and cellular sphingosine together in a dose-dependent way, knockdown blunts both the sphingosine rise and the death response, and forced ACER2 expression drives autophagy and apoptosis in a manner blocked by antioxidants. Clinically, nothing is established: ACER2 is not a drug target and has no accepted diagnostic role.

## Why it appears in this work

ACER2 earns its place as a readout gene rather than as a mediator. Basal expression is low in most lines and the induction is steep and comparatively p53-selective, which is a good combination for a sparse single-cell readout — the opposite situation from [[MG53 (TRIM72)]] (see [[Why MG53 is hard to measure here]]). It is also a useful corrective to a cell-cycle-centric reading of [[p53 program P]]: part of p53's output runs through lipid metabolism, not only through [[The p21-DREAM axis]].

## What is uncertain

The direct-target claim rests on reporter and ChIP work in a small number of lines, and the intronic-promoter architecture has not been widely replicated; the question of whether some of the induction is indirect remains open. More importantly for reading this vault, a transcript increase is a weak proxy for ceramidase flux, which also depends on substrate supply, kinase levels and Golgi context. The cell-fate consequence is dose-dependent in the reported work — strong induction linked to death, modest induction linked to blunted arrest through S1P — and nothing in a 24 h mRNA measurement says which regime a given exposure occupied. Whether ACER2 is an effector of p53-driven death or only a bystander readout of it has been tested by knockdown in very few systems.

## References

- Wang et al., 2017, Scientific Reports — identified ACER2 as a direct p53 target with its major promoter and p53 sites in the first intron, and showed ROS-dependent autophagy and apoptosis on overexpression.
- Xu et al., 2016, Oncotarget — showed doxorubicin raises ACER2 and sphingosine dose-dependently in HCT116, and that ACER2 knockdown blunts both the sphingosine rise and the death response.

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 13.72 CPM |
| Lines where detected | 49 of 50 |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 13 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.114× |
| Wild-type minus altered | 1.179× |
| Compounds moving it up in WT lines | 68 of 98 |
| Direction mixed? | no |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.01357 |
| As a percentage | +0.95% |
| FDR, exposure-shuffle null | 0.0515 |
| In TP53-wild-type lines / altered lines | 0.00590 / 0.01845 |
| Verdict | up with MG53 |
| **Signed into p53-output units** | **toward MORE p53 output** |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

## Links

- **Concepts:** [[The p53 pathway]], [[p53 program P]]
- **Findings:** [[Downstream of MG53]], [[Upstream of MG53]]
- **Why this gene is in the vault:** curated p53 effector; p53 program, induction arm
- **Indexes:** [[Genes — Map of Content]]

## Sources

- Program and MG53 columns: `mg53_p53/findings/tables/tableD_p53_target_genes.csv`
- Genome-wide screen: `genome_wide/tables/c_screen_genes.csv.gz`
- Curated effector columns: `mg53_p53/findings/tables/p53_effectors_per_gene.csv`
