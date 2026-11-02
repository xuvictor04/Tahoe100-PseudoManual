---
symbol: RAD54B
type: gene
tier: 2
aliases: [RAD54B]
p53_direction: repressed by p53
program_arm: P down (WT-selective repression)
median_line_cpm: 52.76
mg53_verdict: none
tags: [direction-mixed, gene, p53-program, p53-repressed]
generated_by: knowledge/_build/build_vault.py
---

# RAD54B

> [!summary] In one line
> RAD54B is a SWI2/SNF2-family DNA translocase that works in homologous recombination and has separately been reported as a scaffold promoting MDM2–MDMX-dependent p53 degradation.

## What it is

The paralogue of RAD54L: an ATP-driven double-stranded DNA translocase that binds RAD51 and remodels nucleosomes and branched recombination intermediates. The paralogues are not simply redundant — mouse Rad54b loss alone has little effect on recombination efficiency, and genetic analysis gives them non-overlapping roles despite similar biochemistry. Mutations were found in primary colon cancers and lymphomas, and RAD54B-deficient cells are synthetic-lethal with loss of FEN1. The p53 link is a separate line of work: RAD54B was reported to act as an adapter promoting MDM2–MDMX heterodimer formation and ubiquitin-dependent p53 turnover, rising early after damage and falling once a checkpoint is established.

## Why it appears in this work

RAD54B is a data-defined member of the repressed arm of [[p53 program P]]: it falls in TP53-wild-type lines under p53-activating compounds. That is the direction the scaffold model predicts, since lowering a cofactor for p53 degradation would reinforce p53's own output — see [[MDM2]] and [[MDM4]]. It is also a proliferation gene, and [[The p21-DREAM axis]] predicts the same direction for an unrelated reason.

## What is uncertain

Those two explanations are not separable from this data. Most recombination and cell-cycle genes fall when cells arrest, so the repression is fully expected from [[CDKN1A]]-driven E2F and DREAM shutdown alone, with no feedback interpretation required. The MDM2–MDMX scaffold claim rests on essentially one primary study and has not been broadly replicated; treat it as a lead, not a premise. The study's direction call here is also flagged as internally mixed across compounds, so the sign is less clean than a summary row suggests.

## References

- Hiramoto et al., 1999, Oncogene — found mutations in RAD54B in primary cancers.
- Wesoly et al., 2006, Molecular and Cellular Biology — showed the differential, non-overlapping contributions of the mammalian Rad54 paralogues to recombination, repair and meiosis.
- McManus et al., 2009, PNAS — FEN1 silencing is synthetic-lethal in RAD54B-deficient colorectal cancer cells.
- Yasuhara et al., 2014, Nature Communications — reported Rad54B as a scaffold for MDM2–MDMX-mediated p53 degradation.

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 52.76 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **repressed by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P down (WT-selective repression) |
| Rank in the program | — of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 0.965× |
| Wild-type minus altered | 0.951× |
| Compounds moving it up in WT lines | 41 of 98 |
| Direction mixed? | **yes** — it goes each way across compounds, so its direction is not a fact about the gene |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00042 |
| As a percentage | +0.03% |
| FDR, exposure-shuffle null | 0.9347 |
| In TP53-wild-type lines / altered lines | 0.00528 / -0.00253 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | -0.266 raw, -0.103 with 3 PCs removed |

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
