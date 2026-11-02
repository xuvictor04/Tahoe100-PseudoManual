---
symbol: FANCD2
type: gene
tier: 2
aliases: [Fanconi anaemia D2]
p53_direction: repressed by p53
program_arm: P down (WT-selective repression)
median_line_cpm: 36.95
mg53_verdict: none
tags: [gene, p53-program, p53-repressed]
generated_by: knowledge/_build/build_vault.py
---

# FANCD2

> [!summary] In one line
> FANCD2 is the Fanconi anaemia protein that, once monoubiquitinated and paired with FANCI, clamps onto DNA at stalled replication forks and licenses interstrand crosslink repair.

## What it is

FANCD2 was positionally cloned as the FA-D2 gene, and its central event was identified at the same time: the FA core complex, through its FANCL ligase, attaches a single ubiquitin to FANCD2 at K561 and to its paralogue FANCI. The modified ID2 heterodimer closes around DNA as a clamp, and that species recruits the steps that unhook a crosslink. Ubiquitination depends on ATR-driven replication-stress signalling and is reversed by USP1-UAF1 ([[USP1]]), so the pathway cycles rather than latching. FANCD2 foci are a standard readout of replication stress. It also protects nascent DNA at stalled forks, a function shared with [[BRCA2]]. Biallelic loss causes Fanconi anaemia.

## Why it appears in this work

FANCD2 sits in the repression arm of [[p53 program P]], on the same logic as [[BRCA2]] and [[EXO1]]: not a p53-bound promoter but a proliferation-coupled gene that comes down as cells leave the cycle. [[The p21-DREAM axis]] is the predicted route.

## What is uncertain

Direct repression by p53 is unlikely for this class of gene. Its program membership is also among the less stable here — the stability line in the generated block is worth reading first. More fundamentally, abundance is the wrong variable: proficiency is set by ubiquitination state, not transcript level, so a modest fall in mRNA at 24 h is not evidence that repair was impaired. The sign must be flipped ([[Signing genes by p53 direction]]); the circularity warning applies.

## References

- Timmers et al., 2001, Molecular Cell — positional cloning of FANCD2.
- Garcia-Higuera et al., 2001, Molecular Cell — FANCD2 is monoubiquitinated after damage and colocalises with BRCA1, placing the FA proteins in a common pathway.
- Nijman et al., 2005, Molecular Cell — USP1 deubiquitinates FANCD2 and regulates the FA pathway.
- Smogorzewska et al., 2007, Cell — identified FANCI as a monoubiquitinated FANCD2 paralogue required for repair.
- Schlacher et al., 2012, Cancer Cell — FA proteins protect stalled replication forks, a function distinct from crosslink repair.
- Alcón et al., 2020, Nature Structural & Molecular Biology — cryo-EM showing FANCD2-FANCI as a DNA-stabilised clamp.

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 36.95 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **repressed by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P down (WT-selective repression) |
| Rank in the program | — of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 0.949× |
| Wild-type minus altered | 0.938× |
| Compounds moving it up in WT lines | 30 of 98 |
| Direction mixed? | no |
| Program membership stability | partial (2-3 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00104 |
| As a percentage | -0.07% |
| FDR, exposure-shuffle null | 0.8124 |
| In TP53-wild-type lines / altered lines | -0.00079 / -0.00119 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | 0.213 raw, 0.157 with 3 PCs removed |

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
