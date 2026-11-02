---
symbol: POGLUT3
type: gene
tier: 2
aliases: [KDELC2]
p53_direction: repressed by p53
program_arm: P down (WT-selective repression)
median_line_cpm: 18.98
mg53_verdict: none
tags: [gene, p53-program, p53-repressed]
generated_by: knowledge/_build/build_vault.py
---

# POGLUT3

> [!summary] In one line
> POGLUT3, formerly KDELC2, is an ER protein O-glucosyltransferase that modifies a specific serine in correctly folded EGF repeats of Notch receptors and some matrix proteins.

## What it is

Despite its KDEL motif this is a glucosyltransferase, not part of KDEL-receptor retrieval. With its paralogue POGLUT2 (KDELC1) it adds glucose to a serine between the third and fourth conserved cysteines of an EGF repeat, a position distinct from the sites POGLUT1 uses. Only properly folded repeats are accepted. Losing the site, together with nearby O-fucose sites, reduces NOTCH1 surface presentation and ligand responsiveness, so the modification reads as a folding and trafficking checkpoint rather than a signalling switch. Later work extended the substrates beyond Notch to fibrillins and LTBP1. Past that the record is thin: no human disease is firmly attributed to it, and nothing is established about its transcriptional regulation.

## Why it appears in this work

POGLUT3 is here as a data-defined member of the repressed arm of [[p53 program P]] — it declines in TP53-wild-type lines under compounds that activate p53. Nothing in its known biology predicts that: it is not a cell-cycle gene and has no reported p53 connection.

## What is uncertain

Its program membership is the weak kind, holding in only some cross-fitting folds, so it may be a borderline gene that cleared a threshold rather than a real part of the response. No mechanism connects a Notch glycosyltransferase to p53, and with nothing known about its promoter there is no indirect route to check either; the transcriptional slowdown of arresting cells would give the same direction. See [[Signing genes by p53 direction]].

## References

- Takeuchi et al., 2018, PNAS — identified KDELC1 and KDELC2 as protein O-glucosyltransferases POGLUT2 and POGLUT3, modifying an EGF-repeat site distinct from POGLUT1's.

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 18.98 CPM |
| Lines where detected | 45 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **repressed by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P down (WT-selective repression) |
| Rank in the program | — of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 0.919× |
| Wild-type minus altered | 0.953× |
| Compounds moving it up in WT lines | 23 of 98 |
| Direction mixed? | no |
| Program membership stability | partial (2-3 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00068 |
| As a percentage | +0.05% |
| FDR, exposure-shuffle null | 0.8974 |
| In TP53-wild-type lines / altered lines | 0.00085 / 0.00058 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | -0.001 raw, 0.161 with 3 PCs removed |

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
