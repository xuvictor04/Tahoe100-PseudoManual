---
symbol: KIF11
type: gene
tier: 2
aliases: [EG5]
p53_direction: repressed by p53
program_arm: P down (WT-selective repression)
median_line_cpm: 75.2
mg53_verdict: none
tags: [direction-mixed, gene, p53-program, p53-repressed]
generated_by: knowledge/_build/build_vault.py
---

# KIF11

> [!summary] In one line
> KIF11 encodes Eg5, the kinesin-5 motor that cross-links antiparallel microtubules and pushes the two halves of the mitotic spindle apart.

## What it is

Eg5 is a homotetramer with motor domains at both ends, so it slides antiparallel microtubules past one another, generating the outward force that separates duplicated centrosomes into a bipolar spindle. Cdk1 phosphorylation of the tail switches on its spindle association at mitotic entry. Inhibit it and cells enter mitosis but collapse into a monopolar spindle — the phenotype that identified monastrol in one of the first small-molecule phenotypic screens, and the basis of the kinesin-spindle-protein inhibitor class, whose single-agent activity in solid tumours disappointed. Its transcript is tightly proliferation-coupled and sits in the canonical E2F/DREAM-regulated cell-cycle cluster. Germline heterozygous loss-of-function mutations cause microcephaly, variably with lymphoedema and chorioretinal dysplasia.

## Why it appears in this work

KIF11 was selected into the repression arm of [[p53 program P]], declining selectively in TP53-wild-type lines under p53 activators. For a core mitotic gene the expected route is indirect, through p21 and the DREAM complex rather than p53 at the promoter; see [[The p21-DREAM axis]]. Its membership supports reading that arm as a proliferation-arrest signature.

## What is uncertain

KIF11 is not a direct p53 target, and its direction here is flagged as mixed — it moves both ways across compounds — so no single direction is a fact about the gene. Some of that scatter is expected: many compounds in a panel this size perturb the cycle directly, and a transcript this tightly proliferation-coupled reports where cells sit in the cycle as much as what p53 is doing. If any exposure is itself an antimitotic, the arrest it produces would move KIF11 for reasons unrelated to p53.

## References

- Blangy et al., 1995, Cell — showed Cdk1 phosphorylation of Eg5 controls its spindle association and that Eg5 is required for bipolar spindle formation.
- Mayer et al., 1999, Science — identified monastrol as an Eg5 inhibitor in a phenotype-based screen.
- Ostergaard et al., 2012, American Journal of Human Genetics — KIF11 mutations cause microcephaly with lymphoedema and chorioretinopathy.
- Engeland, 2018, Cell Death and Differentiation — review of p53-p21-DREAM-mediated repression of cell-cycle and mitosis genes.

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 75.20 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no same-strand neighbour close enough to spill into it |

### What p53 does to it

| | |
|---|---|
| Direction | **repressed by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P down (WT-selective repression) |
| Rank in the program | — of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 0.951× |
| Wild-type minus altered | 0.942× |
| Compounds moving it up in WT lines | 36 of 98 |
| Direction mixed? | **yes** — it goes each way across compounds, so its direction is not a fact about the gene |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00041 |
| As a percentage | -0.03% |
| FDR, exposure-shuffle null | 0.9200 |
| In TP53-wild-type lines / altered lines | 0.00174 / -0.00172 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | 0.114 raw, 0.034 with 3 PCs removed |

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
