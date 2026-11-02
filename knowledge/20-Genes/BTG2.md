---
symbol: BTG2
type: gene
tier: 1
aliases: [PC3, TIS21]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
curated_effector: true
effector_role: cell-cycle arrest
median_line_cpm: 8.51
mg53_verdict: up with MG53
mg53_effect_on_p53_output: toward MORE p53 output
tags: [curated-effector, gene, mg53-associated, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# BTG2

> [!summary] In one line
> BTG2 is an antiproliferative immediate-early gene and direct p53 target that works by accelerating mRNA deadenylation rather than by inhibiting a kinase.

## What it is

BTG2 (also PC3, TIS21) belongs to the BTG/Tob antiproliferative family. It has no enzymatic activity of its own; it is an adapter built around the conserved BTG domain (boxes A and B). Its best-established molecular function is bridging the poly(A)-binding protein PABPC1 to CNOT7/CNOT8 (Caf1a/Caf1b), the catalytic deadenylase subunits of the CCR4–NOT complex. Through that bridge BTG2 acts as a general activator of mRNA deadenylation, and the PABPC1 interaction is required for its antiproliferative effect — so BTG2 restrains proliferation post-transcriptionally, which makes it mechanistically unlike the CDK-inhibitor arm of the p53 response.

Its transcriptional behaviour is the other half of the story. BTG2 was first catalogued as an immediate-early gene (TIS21 for TPA-inducible sequence 21) induced by growth factors, serum and phorbol esters, and separately as a p53-dependent DNA-damage-response gene with a p53 response element in its promoter. Functionally, the clearest downstream account is that BTG2 limits cyclin D1 expression and so holds RB hypophosphorylated, enforcing G1 arrest. A systematic screen for the effectors that actually carry p53's antiproliferative output identified BTG2 as a major one in Ras-transduced mouse and human fibroblasts: knocking it down cooperated with oncogenic Ras to transform cells that still had transcriptionally active p53. Later work reported that BTG2 binds H-Ras and lowers its GTP loading, giving a second, more direct route to the same effect. BTG2 expression is reported reduced in a sizeable fraction of kidney and breast carcinomas, and the gene also has roles in neurogenesis and in maintaining quiescence.

## Why it appears in this work

BTG2 is a curated p53 arrest effector whose induction is a high-confidence read on the transcriptional output of [[The p53 pathway]], and it is well enough expressed across the panel to be measured reliably. It earns a second kind of attention here because it is simultaneously a classic immediate-early gene: whatever happens to it under a drug exposure is a mixture of p53 engagement and generic stress and growth-factor signalling. That makes it a useful internal check on whether an induction assigned to [[p53 program P]] is really p53-specific or part of a broader response, and it is one of the program genes where the measured association with MG53 level is on the positive side.

## What is uncertain

The p53-dependence of BTG2 induction is solid for DNA damage in specific systems, but the gene's immediate-early character means an induction at 24 h cannot be attributed to p53 from the induction alone. The deadenylation mechanism is well supported biochemically; which mRNAs it actually controls in a cell is largely unmapped, and cyclin D1 repression — the usual stated link to arrest — rests heavily on overexpression experiments. BTG2's standing as a tumour suppressor comes from expression-loss correlations and mouse fibroblast genetics rather than recurrent somatic mutation; the gene is rarely mutated in human tumours. The Ras-GTP-loading claim has been reported in a small number of systems and should be treated as provisional.

## References

- Rouault et al., 1996, Nature Genetics — cloned human BTG2 and showed its expression is p53-dependent in the DNA-damage response.
- Boiko et al., 2006, Genes & Development — identified BTG2 as a major downstream effector of p53-dependent arrest of Ras-transformed fibroblasts, acting via cyclin D1/E1 and RB.
- Mauxion, Faux & Séraphin, 2008, The EMBO Journal — showed BTG2 is a general activator of mRNA deadenylation.
- Winkler, 2010, Journal of Cellular Physiology — review of the BTG/Tob antiproliferative protein family and its CCR4–NOT link.
- Fischer, 2017, Oncogene — census of p53 target genes, placing BTG2 among the well-supported direct targets.

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 8.51 CPM |
| Lines where detected | 45 of 50 |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 45 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.155× |
| Wild-type minus altered | 1.198× |
| Compounds moving it up in WT lines | 74 of 98 |
| Direction mixed? | no |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.01531 |
| As a percentage | +1.07% |
| FDR, exposure-shuffle null | 0.0546 |
| In TP53-wild-type lines / altered lines | 0.00030 / 0.02636 |
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
