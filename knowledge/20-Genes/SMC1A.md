---
symbol: SMC1A
type: gene
tier: 2
aliases: [SMC1, SMC1L1]
p53_direction: repressed by p53
program_arm: P down (WT-selective repression)
median_line_cpm: 126.07
mg53_verdict: up with MG53
mg53_effect_on_p53_output: toward LESS p53 output
tags: [gene, mg53-associated, p53-program, p53-repressed]
generated_by: knowledge/_build/build_vault.py
---

# SMC1A

> [!summary] In one line
> SMC1A is an ATPase subunit of the cohesin ring that holds sister chromatids together, and is also a direct ATM substrate in the DNA-damage response.

## What it is

SMC1A heterodimerises with SMC3 through long coiled-coil arms joined at a hinge; RAD21 and a STAG subunit close the ring entrapping sister chromatids from replication until anaphase, and the same complex organises chromatin loops with CTCF. Beyond cohesion, SMC1A is phosphorylated by [[ATM]] on two C-terminal serines after ionising radiation, a step required for the S-phase checkpoint: cohesin is part of the damage response, not only the scaffold. The gene is X-linked: missense variants give a Cornelia de Lange phenotype, truncating variants a distinct epileptic encephalopathy. Cohesin subunits are recurrently mutated in myeloid malignancy and bladder cancer.

## Why it appears in this work

SMC1A was selected into the repressed arm of [[p53 program P]]: it falls where p53 output rises. Its value is as a reminder that a data-derived p53 programme contains genes p53 switches off, not only genes it induces. See [[Signing genes by p53 direction]].

## What is uncertain

SMC1A is not a canonical direct p53 target. No p53 repressive element at this gene is established, and indirect repression through [[The p21-DREAM axis]] explains cohesin and mitotic genes at least as well, the route that also moves [[SGO1]] and [[KIF11]]. Being essential and well expressed in every line, its dynamic range is narrow: a small coordinated fall is what cell-cycle exit alone produces. The direct-versus-indirect question is open.

## References

- Kim et al., 2002, Genes & Development — ATM-dependent and ATM-independent phosphorylation of SMC1 in response to DNA damage.
- Musio et al., 2006, Nature Genetics — SMC1A mutations cause X-linked Cornelia de Lange syndrome.
- Nasmyth & Haering, 2009, Annual Review of Genetics — review of cohesin ring architecture and its roles.

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 126.07 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **repressed by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P down (WT-selective repression) |
| Rank in the program | — of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 0.957× |
| Wild-type minus altered | 0.971× |
| Compounds moving it up in WT lines | 30 of 98 |
| Direction mixed? | no |
| Program membership stability | partial (2-3 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00535 |
| As a percentage | +0.37% |
| FDR, exposure-shuffle null | 0.0064 |
| In TP53-wild-type lines / altered lines | 0.00547 / 0.00529 |
| Verdict | up with MG53 |
| **Signed into p53-output units** | **toward LESS p53 output** |
| Co-regulation with MG53 across exposures (r) | 0.352 raw, 0.097 with 3 PCs removed |

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
