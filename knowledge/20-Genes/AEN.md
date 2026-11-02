---
symbol: AEN
type: gene
tier: 1
aliases: [ISG20L1]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
curated_effector: true
effector_role: apoptosis
median_line_cpm: 16.97
mg53_verdict: up with MG53
mg53_effect_on_p53_output: toward MORE p53 output
tags: [curated-effector, gene, mg53-associated, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# AEN

> [!summary] In one line
> AEN, also called ISG20L1, is a p53-inducible nuclear exonuclease that degrades nucleic acid during apoptosis and is needed for efficient DNA fragmentation downstream of p53.

## What it is

AEN (apoptosis-enhancing nuclease) is a small exonuclease of the ISG20/exonuclease-I family, encoded at 15q26.1 and also known as ISG20L1. It carries the conserved exonuclease motifs of that family and has reported activity against single- and double-stranded DNA as well as RNA. In unstressed cells the protein is concentrated in the nucleolus; on induction of apoptosis it redistributes into the nucleoplasm, which is where its substrate is. Mutating the catalytic motifs abolishes both the nuclease activity and the ability to enhance cell death, so the two properties are coupled rather than coincidental.

AEN is a direct transcriptional target of p53 and one of the more reliably recovered members of p53 response signatures across transcriptome studies. Its induction is not p53-exclusive: transcription is driven by all three p53-family members, so p63 and p73 can also raise it. Functionally it has been placed in two adjacent processes. In the first, it is required for efficient internucleosomal DNA fragmentation during p53-dependent apoptosis — loss of AEN reduces fragmentation without necessarily abolishing upstream death signalling, which fits a role as an executioner rather than an initiator. In the second, it modulates genotoxic-stress-induced autophagy, with knockdown reducing autophagic vacuoles and LC3-II after damage. There is no established clinical or therapeutic angle on AEN.

## Why it appears in this work

AEN is a readout gene for the apoptotic end of [[p53 program P]], and a well-behaved one: it is induced robustly, it is not strongly expressed at baseline, and its literature as a direct target is unusually clean for a gene this obscure in the broader apoptosis field. Reading it alongside [[BBC3]] and [[BAX]] distinguishes p53 output that has reached the nuclear demolition machinery from output that stopped at arrest via [[The p21-DREAM axis]]. It is also a warning case for how this study assigns direction, since p63/p73 can drive it: see [[Signing genes by p53 direction]].

## What is uncertain

Whether the nuclease activity is the function that matters in cells, or whether AEN also acts as a scaffold, has not been separated cleanly — the catalytic-mutant experiments show the activity is required for the death-enhancing phenotype, not that nothing else is going on. The autophagy role comes essentially from one laboratory and has not been broadly replicated. The in vivo requirement is weakly established: AEN is dispensable for most of p53's phenotypic output in the systems where it has been examined, which is consistent with a downstream amplifier rather than a decision point. And because p53-family members share its promoter, induction in a pooled, mixed-genotype screen is not by itself evidence that p53 specifically was active.

## References

- Kawase et al., 2008, Oncogene — identified AEN as a direct p53 target gene encoding a nuclear exonuclease required for efficient DNA fragmentation in p53-dependent apoptosis.
- Eby et al., 2010, Molecular Cancer — showed ISG20L1/AEN is transcriptionally controlled by all three p53-family members and that its loss reduces genotoxic-stress-induced autophagy.

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 16.97 CPM |
| Lines where detected | 49 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 33 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.167× |
| Wild-type minus altered | 1.135× |
| Compounds moving it up in WT lines | 77 of 98 |
| Direction mixed? | no |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00899 |
| As a percentage | +0.62% |
| FDR, exposure-shuffle null | 0.0388 |
| In TP53-wild-type lines / altered lines | 0.00135 / 0.01382 |
| Verdict | up with MG53 |
| **Signed into p53-output units** | **toward MORE p53 output** |
| Co-regulation with MG53 across exposures (r) | 0.466 raw, 0.101 with 3 PCs removed |

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
