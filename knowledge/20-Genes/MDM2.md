---
symbol: MDM2
type: gene
tier: 1
aliases: [HDM2]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
curated_effector: true
effector_role: negative feedback
median_line_cpm: 185.8
mg53_verdict: down with MG53
mg53_effect_on_p53_output: toward LESS p53 output
tags: [curated-effector, gene, mg53-associated, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# MDM2

> [!abstract] Knowledge layer: needs a written note — it is well studied and central here
> Nothing is written about this gene yet. Add `knowledge/20-Genes/_knowledge/MDM2.md` and rebuild; see [[How this vault is built]].

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 185.80 CPM |
| Lines where detected | 50 of 50 |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 3 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.255× |
| Wild-type minus altered | 1.195× |
| Compounds moving it up in WT lines | 95 of 98 |
| Direction mixed? | no |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00500 |
| As a percentage | -0.35% |
| FDR, exposure-shuffle null | 0.0313 |
| In TP53-wild-type lines / altered lines | -0.00539 / -0.00476 |
| Verdict | down with MG53 |
| **Signed into p53-output units** | **toward LESS p53 output** |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

## Links

- **Concepts:** [[The p53 pathway]], [[p53 program P]]
- **Findings:** [[Downstream of MG53]], [[Upstream of MG53]]
- **Its own write-up:** [[MDM2 and MG53]]
- **Why this gene is in the vault:** curated p53 effector; p53 program, induction arm
- **Indexes:** [[Genes — Map of Content]]

## Sources

- Program and MG53 columns: `mg53_p53/findings/tables/tableD_p53_target_genes.csv`
- Genome-wide screen: `genome_wide/tables/c_screen_genes.csv.gz`
- Curated effector columns: `mg53_p53/findings/tables/p53_effectors_per_gene.csv`
