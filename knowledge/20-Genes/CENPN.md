---
symbol: CENPN
type: gene
tier: 2
aliases: [CENP-N]
p53_direction: repressed by p53
program_arm: P down (WT-selective repression)
median_line_cpm: 31.5
mg53_verdict: none
tags: [gene, p53-program, p53-repressed]
generated_by: knowledge/_build/build_vault.py
---

# CENPN

> [!summary] In one line
> CENPN encodes CENP-N, the subunit of the constitutive centromere-associated network that reads the CENP-A nucleosome directly and so marks where a kinetochore is built.

## What it is

CENP-N was found in the complex that co-purifies with CENP-A chromatin, and is the component that recognises it specifically, contacting the CENP-A nucleosome through the histone's exposed RG loop. Structural work has since resolved that interface and shown how CENP-N bridges to CENP-L and sits alongside CENP-C in the inner kinetochore. Depleting it impairs kinetochore assembly and new CENP-A deposition, so cells lose chromosome segregation fidelity. Expression is proliferation-coupled rather than tissue-specific. Outside that structural role its literature is mostly correlative: raised expression in various tumours with survival associations, a weak basis for functional claims.

## Why it appears in this work

CENPN was selected into the repression arm of [[p53 program P]], declining modestly and selectively in TP53-wild-type lines under p53-activating compounds. For a mitosis gene of this kind the expected route is indirect, through p21 and the DREAM complex rather than p53 at the promoter; see [[The p21-DREAM axis]]. Its membership mainly reinforces reading that arm as a proliferation-arrest signature rather than a dedicated repression programme.

## What is uncertain

Nothing establishes CENPN as a p53 target in any direct sense, and its program membership here is only partially stable across folds, so it should be held more loosely than the core members of the arm. CENP-N's biology is executed at the protein level, so a fall in its transcript reports cells leaving the cycle, not a change in centromere function.

## References

- Foltz et al., 2006, Nature Cell Biology — defined the human CENP-A nucleosome-associated complex, including CENP-N.
- Carroll et al., 2009, Nature Cell Biology — showed CENP-N binds CENP-A nucleosomes directly and is required for centromere assembly.
- Chittori et al., 2018, Science — structural basis of centromeric nucleosome recognition by CENP-N.
- Engeland, 2018, Cell Death and Differentiation — review of p53-p21-DREAM-mediated repression of cell-cycle and mitosis genes.

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 31.50 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **repressed by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P down (WT-selective repression) |
| Rank in the program | — of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 0.946× |
| Wild-type minus altered | 0.943× |
| Compounds moving it up in WT lines | 28 of 98 |
| Direction mixed? | no |
| Program membership stability | partial (2-3 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00349 |
| As a percentage | +0.24% |
| FDR, exposure-shuffle null | 0.3130 |
| In TP53-wild-type lines / altered lines | 0.00345 / 0.00351 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | 0.339 raw, 0.108 with 3 PCs removed |

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
