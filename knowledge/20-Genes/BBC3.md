---
symbol: BBC3
type: gene
tier: 1
aliases: [PUMA]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
curated_effector: true
effector_role: apoptosis
median_line_cpm: 17.41
mg53_verdict: none
tags: [curated-effector, gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# BBC3

> [!summary] In one line
> BBC3 encodes PUMA, the BH3-only protein that is p53's most direct and most quantitatively important route to apoptosis.

## What it is

BBC3 (BCL-2 binding component 3) encodes PUMA, a small BH3-only member of the BCL-2 family. It is close to undetectable in unstressed cells and is induced strongly and rapidly by p53 through p53 response elements in its promoter. The protein localises to mitochondria and binds every anti-apoptotic BCL-2 family member with high affinity, which frees sequestered activators such as BIM and BID and leaves BAX and BAK unrestrained — so PUMA does not form pores itself, it removes the restraint on the proteins that do. Within the p53 response it is the component whose loss subtracts the most apoptosis: in mouse genetics, Puma deficiency accounts for the bulk of p53-dependent death after DNA damage in lymphoid cells, and combined loss of Puma and Noxa reproduces much of what p53 loss does in that setting.

PUMA is not only a p53 gene. Transcription is also driven by FOXO3A, by E2F1, by glucocorticoid receptor signalling and by growth-factor or cytokine withdrawal, giving it a substantial p53-independent induction repertoire. Clinically, basal and inducible PUMA levels contribute to chemotherapy and glucocorticoid sensitivity and to how cells respond to BH3-mimetic drugs, though PUMA itself is not a drug target.

## Why it appears in this work

PUMA is the cleanest transcript-level evidence that p53's output reached the apoptotic arm rather than stopping at arrest through [[The p21-DREAM axis]]. Its near-zero baseline gives it a large dynamic range within [[p53 program P]], which is an advantage for detecting induction and a liability for estimating it precisely in sparse single-cell data. Read next to [[CDKN1A]], it gives the arrest-versus-death split of a p53 response; read next to [[BAX]], it shows the difference between a gene whose p53 dependence lives in its transcription and one whose p53 dependence mostly does not.

## What is uncertain

Two things qualify PUMA as a readout here. First, its non-p53 inducers are real and several of them — growth-factor withdrawal, glucocorticoid signalling, FOXO3A activation — are exactly what a 24 h drug exposure can produce, so induction in a pooled, mixed-genotype panel is not by itself proof of p53 activity. That matters wherever the logic of [[p53 nullification in cancer cell lines]] is used to sign a gene by genotype. Second, apoptosis is self-censoring in single-cell data: dying cells lose mRNA and are preferentially lost at dissociation and quality filtering, so the cells carrying the strongest PUMA signal are the ones least likely to be counted. The bias runs toward understating the apoptotic arm and is hard to correct.

Mechanistically, whether PUMA is a direct activator of BAX or only a derepressor of anti-apoptotic proteins is still unresolved, with PUMA sitting awkwardly between the two models. And its necessity is lineage-dependent: the strong genetic evidence comes largely from lymphoid cells, while epithelial lines often tolerate PUMA loss with less effect on p53-driven death.

## References

- Nakano and Vousden, 2001, Molecular Cell — identified PUMA as a BH3-only gene induced by p53.
- Yu et al., 2001, Molecular Cell — identified PUMA as a p53-induced gene that triggers rapid apoptosis in colorectal cancer cells.
- Villunger et al., 2003, Science — showed Puma and Noxa mediate much of p53-dependent and drug-induced apoptosis in mouse cells.
- Jeffers et al., 2003, Cancer Cell — showed Puma is an essential mediator of both p53-dependent and p53-independent apoptotic pathways.

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 17.41 CPM |
| Lines where detected | 50 of 50 |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 4 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.136× |
| Wild-type minus altered | 1.137× |
| Compounds moving it up in WT lines | 75 of 98 |
| Direction mixed? | no |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00173 |
| As a percentage | +0.12% |
| FDR, exposure-shuffle null | 0.7087 |
| In TP53-wild-type lines / altered lines | -0.00291 / 0.00454 |
| Verdict | none |
| **Signed into p53-output units** | **none** |

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
