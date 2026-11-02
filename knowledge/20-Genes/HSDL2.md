---
symbol: HSDL2
type: gene
tier: 3
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 67.53
mg53_verdict: none
tags: [direction-mixed, gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# HSDL2

> [!abstract] Knowledge layer: no written note; the tables below are what this vault knows about it
> Nothing is written about this gene yet. Add `knowledge/20-Genes/_knowledge/HSDL2.md` and rebuild; see [[How this vault is built]].

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 67.53 CPM |
| Lines where detected | 50 of 50 |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 94 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.012× |
| Wild-type minus altered | 1.036× |
| Compounds moving it up in WT lines | 51 of 98 |
| Direction mixed? | **yes** — it goes each way across compounds, so its direction is not a fact about the gene |
| Program membership stability | partial (2-3 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00371 |
| As a percentage | -0.26% |
| FDR, exposure-shuffle null | 0.1049 |
| In TP53-wild-type lines / altered lines | -0.00279 / -0.00426 |
| Verdict | none |
| **Signed into p53-output units** | **none** |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

## Links

- **Concepts:** [[The p53 pathway]], [[p53 program P]]
- **Findings:** [[Downstream of MG53]], [[Upstream of MG53]]
- **Why this gene is in the vault:** p53 program, induction arm
- **Indexes:** [[Genes — Map of Content]]

## Sources

- Program and MG53 columns: `mg53_p53/findings/tables/tableD_p53_target_genes.csv`
- Genome-wide screen: `genome_wide/tables/c_screen_genes.csv.gz`
- Curated effector columns: `mg53_p53/findings/tables/p53_effectors_per_gene.csv`
