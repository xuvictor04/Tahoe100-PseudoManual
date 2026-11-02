---
symbol: EXO1
type: gene
tier: 2
aliases: [exonuclease 1]
p53_direction: repressed by p53
program_arm: P down (WT-selective repression)
median_line_cpm: 17.65
mg53_verdict: none
tags: [gene, p53-program, p53-repressed]
generated_by: knowledge/_build/build_vault.py
---

# EXO1

> [!summary] In one line
> EXO1 is a 5'-to-3' exonuclease that trims DNA ends in mismatch repair, long-range double-strand break resection and telomere processing.

## What it is

EXO1 is a Rad2/XPG-family nuclease, first identified in yeast as an exonuclease binding MSH2. In mismatch repair it degrades the error-containing strand from a nick after MutS and MutL license repair. In break repair it performs long-range resection, extending the 3' tail that RPA and then RAD51 occupy — the step committing a break to recombination; a DNA2-dependent route runs in parallel, both fed by BLM. Resection is actively blocked by [[TP53BP1]] with RIF1 and shieldin, which is how pathway choice is enforced. Expression is cell-cycle periodic under E2F and DREAM control, peaking in S phase; CDK phosphorylation adds another layer. Mouse knockouts are mismatch-repair deficient and tumour prone.

## Why it appears in this work

EXO1 sits in the repression arm of [[p53 program P]] — a proliferation-coupled gene that falls, selectively in TP53-wild-type lines, under compounds that activate p53. That is what [[The p21-DREAM axis]] predicts: p53 reaches this class of gene through p21 and the RB-E2F and DREAM complexes, not by binding its promoter.

## What is uncertain

Direct repression by p53 is doubtful; the p21-relayed account fits better. Being a repressed gene, the sign of any MG53 association must be flipped before it says anything about p53 output ([[Signing genes by p53 direction]]). Transcript level is a weak proxy for resection capacity, and a modest fall at 24 h is as consistent with fewer cells in S phase as with regulation of the gene itself. The circularity warning applies.

## References

- Tishkoff et al., 1997, PNAS — identified yeast EXO1 as an exonuclease that interacts with MSH2 and acts in mismatch repair.
- Wei et al., 2003, Genes & Development — Exo1-deficient mice show mismatch-repair defects and increased cancer susceptibility.
- Mimitou & Symington, 2008, Nature — Sae2, Exo1 and Sgs1 collaborate in processing DNA double-strand break ends.
- Nimonkar et al., 2011, Genes & Development — reconstituted BLM-DNA2 and EXO1-BLM machineries for human DNA end resection.
- Engeland, 2018, Cell Death and Differentiation — review of indirect transcriptional repression through the p53-p21-DREAM route.

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 17.65 CPM |
| Lines where detected | 49 of 50 |
| Readthrough geometry | no same-strand neighbour close enough to spill into it |

### What p53 does to it

| | |
|---|---|
| Direction | **repressed by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P down (WT-selective repression) |
| Rank in the program | — of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 0.936× |
| Wild-type minus altered | 0.918× |
| Compounds moving it up in WT lines | 32 of 98 |
| Direction mixed? | no |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00343 |
| As a percentage | +0.24% |
| FDR, exposure-shuffle null | 0.4678 |
| In TP53-wild-type lines / altered lines | 0.00483 / 0.00264 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | 0.046 raw, -0.077 with 3 PCs removed |

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
