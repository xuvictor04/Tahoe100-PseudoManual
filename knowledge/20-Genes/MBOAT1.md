---
symbol: MBOAT1
type: gene
tier: 2
aliases: [OACT1]
p53_direction: repressed by p53
program_arm: P down (WT-selective repression)
median_line_cpm: 21.93
mg53_verdict: down with MG53
mg53_effect_on_p53_output: toward MORE p53 output
tags: [gene, mg53-associated, p53-program, p53-repressed]
generated_by: knowledge/_build/build_vault.py
---

# MBOAT1

> [!summary] In one line
> MBOAT1 encodes an endoplasmic-reticulum lysophospholipid acyltransferase that re-acylates lyso-phosphatidylethanolamine and lyso-phosphatidylserine, setting the fatty-acid composition of membrane phospholipids.

## What it is

MBOAT1 runs the re-acylation half of the Lands cycle: a phospholipase strips the sn-2 acyl chain from a membrane phospholipid, and a membrane-bound O-acyltransferase puts a new one back. Also called LPEAT1 or LPSAT, it is a multipass ER membrane enzyme preferring lyso-phosphatidylethanolamine and lyso-phosphatidylserine as acceptors and oleoyl-CoA as donor, so its activity shifts membranes toward monounsaturated chains. That specificity gave it a second life in redox biology: MBOAT1 and its paralogue MBOAT2 were identified as ferroptosis suppressors acting independently of GPX4 and FSP1, depleting the polyunsaturated phospholipids that lipid peroxidation requires. In the same work MBOAT1 was reported to be driven transcriptionally by the oestrogen receptor.

## Why it appears in this work

It is carried here as a member of the repression arm of [[p53 program P]], which makes the sign of its slope matter more than the size — a positive coefficient on measured MG53 reads as *less* p53 output, not more. That inversion is the argument of [[Signing genes by p53 direction]].

## What is uncertain

Nothing establishes MBOAT1 as a direct p53 target: no response element at the locus has been reported, and a repression arm derived from expression behaviour collects genes that fall simply because growth and lipid synthesis fall under arrest. The ferroptosis role rests substantially on gain-of-function overexpression. And since its level tracks oestrogen-receptor status, a hormone-receptor covariate across these pooled lines could generate an association unrelated to p53.

## References

- Hishikawa et al., 2008, PNAS — defined the MBOAT lysophospholipid acyltransferase family, assigning MBOAT1 lyso-PE/lyso-PS acceptor preference.
- Liang et al., 2023, Cell — MBOAT1 and MBOAT2 suppress ferroptosis independently of GPX4 and FSP1, and are induced by oestrogen and androgen receptor respectively.

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 21.93 CPM |
| Lines where detected | 49 of 50 |
| Readthrough geometry | no same-strand neighbour close enough to spill into it |

### What p53 does to it

| | |
|---|---|
| Direction | **repressed by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P down (WT-selective repression) |
| Rank in the program | — of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 0.935× |
| Wild-type minus altered | 0.961× |
| Compounds moving it up in WT lines | 30 of 98 |
| Direction mixed? | no |
| Program membership stability | unstable (0-1 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.01093 |
| As a percentage | -0.75% |
| FDR, exposure-shuffle null | 0.0218 |
| In TP53-wild-type lines / altered lines | -0.01012 / -0.01139 |
| Verdict | down with MG53 |
| **Signed into p53-output units** | **toward MORE p53 output** |
| Co-regulation with MG53 across exposures (r) | -0.519 raw, -0.097 with 3 PCs removed |

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
