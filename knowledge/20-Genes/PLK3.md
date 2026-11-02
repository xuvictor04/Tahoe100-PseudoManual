---
symbol: PLK3
type: gene
tier: 1
aliases: [PRK, FNK]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
curated_effector: true
effector_role: cell-cycle arrest
median_line_cpm: 16.9
mg53_verdict: none
tags: [curated-effector, gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# PLK3

> [!summary] In one line
> PLK3 encodes a stress-activated polo-like kinase, switched on by DNA damage and oxidative stress, that has been implicated in phosphorylating p53 at serine 20.

## What it is

PLK3 (also PRK, FNK, CNK) belongs to the polo-like kinase family — an N-terminal kinase domain plus a C-terminal polo-box domain for substrate docking and localisation. Family membership is misleading if read as family resemblance. PLK1 is a mitotic kinase, overexpressed in tumours and a drug target; PLK3 behaves instead as a stress-response kinase whose transcript is an immediate-early gene and whose activity is induced rather than cell-cycle-scheduled.

The best-developed part of its biology is the damage response. PLK3 activity rises rapidly after DNA damage in an ATM-dependent manner, and PLK3 phosphorylates p53 on serine 20 in vitro — the site whose modification interferes with [[MDM2]] binding and so stabilises the protein. Hydrogen peroxide produces a comparable activation, and in cells a kinase-dead PLK3 reduces serine 20 phosphorylation after either insult, though the published effect is partial in both cases. PLK3 has also been reported to phosphorylate CHK2 ([[CHEK2]]) and CDC25C and to act on HIF-1α under hypoxia, but no single function has been pinned down as its principal one.

PLK3 is usually labelled a tumour suppressor. The basis is expression rather than mutation — the transcript is reported down-regulated in several carcinomas, lung and head and neck among them. The mouse genetics are split rather than merely weak: one study reports tumours in various organs in aged Plk3-null animals, tied to deregulated HIF-1α, while another finds no significant increase in spontaneous tumour incidence across genotypes.

## Why it appears in this work

PLK3 sits in the induction arm of [[p53 program P]] as a curated effector with an arrest role, and its interest here is that it is a candidate *feedback* component rather than a terminal output. If PLK3 is induced as part of the p53 response and also phosphorylates p53 at a stabilising site, its induction reports engagement of a loop, not merely a downstream consequence — a different kind of signal from p21's. Its presence says the stress-kinase layer moved with the canonical arrest and apoptosis arms, as one expects if [[The p53 pathway]] is genuinely active.

## What is uncertain

The serine 20 claim deserves its hedges. It rests on in vitro kinase work plus dominant-negative and knockdown experiments; CHK2 is the better-established serine 20 kinase, and how much PLK3 contributes in any particular cell type is unresolved; the two are not mutually exclusive. Whether PLK3 is a *direct* p53 target is a separate, weaker question: it is damage-inducible, but a validated p53 response element is not part of the standard account, so membership in a p53-associated induction arm may reflect a general stress induction running parallel to p53 rather than through it. The tumour-suppressor designation rests largely on reduced expression in tumour series, and the mouse data do not settle it either way. Most pointedly here, a report has PLK3 phosphorylating serine 20 of gain-of-function mutant p53 and supporting its transactivation — if that holds, PLK3's effect is conditional on p53 genotype, and this panel contains both wild-type and altered lines (see [[p53 nullification in cancer cell lines]]).

## References

- Xie et al., 2001, Journal of Biological Chemistry — Plk3 links DNA damage to arrest and apoptosis partly via p53, with ATM-dependent activation and serine 20 as a target site.
- Xie et al., 2001, Journal of Biological Chemistry — reactive-oxygen-species-induced phosphorylation of p53 on serine 20 is mediated in part by Plk3.
- Bahassi El et al., 2002, Oncogene — Plk3 as a multifunctional kinase in stress-response pathways, interacting with the damage checkpoint machinery.
- Myer et al., 2011, Mutation Research — Plk3-null mice stabilise Cdc25A after DNA damage, but show no significant increase in tumour incidence between genotypes.

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 16.90 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 22 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.091× |
| Wild-type minus altered | 1.119× |
| Compounds moving it up in WT lines | 70 of 98 |
| Direction mixed? | no |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00763 |
| As a percentage | +0.53% |
| FDR, exposure-shuffle null | 0.2280 |
| In TP53-wild-type lines / altered lines | 0.00356 / 0.01010 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | 0.459 raw, 0.273 with 3 PCs removed |

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
