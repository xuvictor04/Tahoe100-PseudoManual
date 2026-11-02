---
symbol: FDXR
type: gene
tier: 1
aliases: [ferredoxin reductase]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
curated_effector: true
effector_role: metabolism / redox
median_line_cpm: 10.46
mg53_verdict: none
tags: [curated-effector, gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# FDXR

> [!summary] In one line
> FDXR encodes mitochondrial NADPH:ferredoxin reductase, the entry point for electrons into the ferredoxin system that supplies steroidogenic cytochromes P450 and iron-sulfur cluster assembly; it is a direct p53 target and the strongest known blood-transcript biomarker of radiation dose.

## What it is

FDXR is a FAD-containing flavoprotein of the mitochondrial inner compartment, also called adrenodoxin reductase or ferredoxin reductase (FR). It accepts a hydride from NADPH and passes single electrons to the small iron-sulfur proteins ferredoxin 1 and ferredoxin 2. Through FDX1 (adrenodoxin) this chain supplies the mitochondrial cytochromes P450 — CYP11A1 for the first committed step of steroidogenesis, CYP11B1/B2, and the vitamin D hydroxylases. Through FDX2 it supplies the core iron-sulfur cluster assembly machinery. That second branch is why FDXR, despite its adrenal-sounding name, is expressed in essentially every cell.

Its place in p53 biology came out of a differential screen for genes induced by p53 after 5-fluorouracil, where it was one of very few hits. Raising FR sensitised cells to 5-FU and suppressing it protected them, and the proposed mechanism was generation of oxidative stress in mitochondria downstream of p53. Later work made the relationship reciprocal rather than one-way: FDXR loss raises iron regulatory protein 2, which in turn represses p53 (and, by destabilising TP73 mRNA, p73), so FDXR and p53 sit in a feedback loop routed through iron homeostasis, and FDXR is required for p53-dependent tumour suppression in that model.

FDXR's most practical claim is as a dosimeter. It is the best stand-alone transcriptional biomarker of ionising radiation exposure in human blood, with a usable dose-response extending to low and partial-body exposures — a direct consequence of its being a steep, reliable p53 target in lymphocytes. Clinically, biallelic loss-of-function FDXR variants cause a mitochondriopathy with optic atrophy and auditory neuropathy, consistent with loss of the ISC branch rather than the steroidogenic one.

## Why it appears in this work

FDXR is a direct, high-fidelity member of [[p53 program P]] with a property no other target in the panel has: it is the gene the radiation biology field already uses to read out dose. That makes it the natural reporter in a dose-resolved screen like the one [[Tahoe-100M]] supports. It also carries an arm of p53's output the other reporters do not — mitochondrial metabolism, redox and iron — distinct from arrest through [[The p21-DREAM axis]] and from the apoptotic effectors.

## What is uncertain

Whether FDXR induction produces ROS, which is the mechanism originally proposed for its contribution to p53-dependent death, is not settled; a reductase feeding iron-sulfur cluster assembly could as easily lower oxidative stress as raise it, and the two readings have not been cleanly separated in one system. The feedback loop onto p53 means FDXR is both a target and a modulator of the pathway, so treating its level as a pure readout is an approximation — defensible for a 24 h mRNA measurement, less so if protein-level or chronic effects are in play. Because part of its expression serves constitutive ISC biogenesis, FDXR carries a real housekeeping floor, which damps its fold-change relative to targets with no basal function; absolute and relative induction will disagree about its rank. Finally, the biodosimetry literature finds that specific FDXR transcript variants carry the signal, and a 3′-biased short-read assay collapses them into one number.

## References

- Hwang et al., 2001, Nature Medicine — identified FDXR as one of few genes induced by p53 after 5-fluorouracil and showed its level modulates p53-dependent apoptosis in colorectal cancer cells.
- Zhang et al., 2017, Genes & Development — showed ferredoxin reductase is critical for p53-dependent tumour suppression via iron regulatory protein 2, establishing an FDXR–p53 feedback loop through iron homeostasis.
- O'Brien et al., 2018, Scientific Reports — demonstrated FDXR as a biomarker of radiation exposure in vivo, with a dose-response at low and partial-body doses.
- Peng et al., 2017, Human Molecular Genetics — reported biallelic FDXR mutations in 17 individuals from 13 unrelated families causing a mitochondriopathy with optic atrophy, with reduced ferredoxin reductase activity in patient fibroblasts rescued by wild-type FDXR.
- Paul et al., 2017, American Journal of Human Genetics — independently found biallelic FDXR variants in four families with auditory neuropathy and optic atrophy, with pathogenicity established by complementation in yeast.

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 10.46 CPM |
| Lines where detected | 49 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 5 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.237× |
| Wild-type minus altered | 1.243× |
| Compounds moving it up in WT lines | 87 of 98 |
| Direction mixed? | no |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00247 |
| As a percentage | +0.17% |
| FDR, exposure-shuffle null | 0.7125 |
| In TP53-wild-type lines / altered lines | -0.01057 / 0.01074 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | 0.203 raw, -0.046 with 3 PCs removed |

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
