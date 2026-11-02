---
symbol: SGO1
type: gene
tier: 2
aliases: [shugoshin 1]
p53_direction: repressed by p53
program_arm: P down (WT-selective repression)
median_line_cpm: 25.07
mg53_verdict: none
tags: [gene, p53-program, p53-repressed]
generated_by: knowledge/_build/build_vault.py
---

# SGO1

> [!summary] In one line
> SGO1 encodes shugoshin 1, the mitotic protein that shields centromeric cohesin from premature removal so sister chromatids stay paired until anaphase.

## What it is

Shugoshin is recruited to centromeres by the Bub1-phosphorylated H2A-T120 mark and by contacts near CENP-A, and brings the phosphatase PP2A-B56 to the right place. PP2A dephosphorylates sororin and the cohesin subunit SA2, blocking the Wapl- and separase-driven cohesin release that strips cohesin from chromosome arms in prophase; Cdk1 phosphorylation of Sgo1 in mitosis switches on its direct cohesin binding, making the protection mitosis-specific. Loss produces premature sister-chromatid separation, missegregation and aneuploidy, and Sgo1 also participates in kinetochore tension sensing. Clinically, a homozygous founder variant causes CAID syndrome — chronic atrial and intestinal dysrhythmia — a cohesinopathy of sinus-node and gut pacemaker tissue, with accelerated cycling and increased senescence in patient fibroblasts.

## Why it appears in this work

SGO1 is a data-defined member of the repressed arm of [[p53 program P]]: it declines in TP53-wild-type lines under p53-activating compounds. That is the expected behaviour of a mitotic gene when p53 arrests cells — [[CDKN1A]] induction, CDK inhibition, and E2F/DREAM-mediated shutdown of the mitotic module. See [[The p21-DREAM axis]].

## What is uncertain

Whether "p53 target" means anything direct here. I know of no evidence for p53 occupancy at the SGO1 promoter, and the whole mitotic module — [[KIF11]], [[HJURP]], [[CENPN]] and this gene together — moves as a block, the signature of indirect repression through the cell cycle rather than gene-specific regulation. Its program membership is also only partially stable across cross-fitting folds, so it sits nearer the selection threshold than the strongly repressed cell-cycle genes. Treating its decline as evidence about p53's direct output would be over-reading ([[Signing genes by p53 direction]]).

## References

- Kitajima et al., 2006, Nature — showed that shugoshin collaborates with PP2A to protect centromeric cohesin.
- Liu, Rankin & Yu, 2013, Nature Cell Biology — Cdk-mediated mitotic phosphorylation of Sgo1 activates its direct cohesin binding.
- Chetaille et al., 2014, Nature Genetics — a homozygous SGO1 founder mutation causes CAID syndrome, a cohesinopathy of heart and gut rhythm.

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 25.07 CPM |
| Lines where detected | 49 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **repressed by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P down (WT-selective repression) |
| Rank in the program | — of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 0.896× |
| Wild-type minus altered | 0.945× |
| Compounds moving it up in WT lines | 20 of 98 |
| Direction mixed? | no |
| Program membership stability | partial (2-3 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00213 |
| As a percentage | +0.15% |
| FDR, exposure-shuffle null | 0.5251 |
| In TP53-wild-type lines / altered lines | -0.00236 / 0.00466 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | 0.247 raw, 0.056 with 3 PCs removed |

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
