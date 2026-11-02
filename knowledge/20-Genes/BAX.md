---
symbol: BAX
type: gene
tier: 1
aliases: [bcl-2-associated X]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
curated_effector: true
effector_role: apoptosis
median_line_cpm: 10.52
mg53_verdict: none
tags: [curated-effector, direction-mixed, gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# BAX

> [!summary] In one line
> BAX is the pore-forming BCL-2-family effector that permeabilises the outer mitochondrial membrane, and it was the first component of the apoptotic machinery identified as a direct p53 transcriptional target.

## What it is

BAX is a multidomain pro-apoptotic member of the BCL-2 family. In healthy cells most of it is a soluble cytosolic monomer, cycling on and off mitochondria and being retrotranslocated back to the cytosol by anti-apoptotic relatives. On activation it undergoes a large conformational change, inserts into the outer mitochondrial membrane and oligomerises, with BAK, into macropores. That permeabilisation releases cytochrome c and SMAC, which assemble the APAF1 apoptosome and activate caspase-9 and then caspase-3. It is the commitment step of the intrinsic pathway: cells lacking both BAX and BAK are broadly resistant to mitochondrial apoptosis regardless of upstream signalling.

BAX is controlled at two levels. Transcriptionally, p53 binds its promoter and raises its expression, the finding that first put a p53 target inside the death machinery itself. Post-translationally — and this is where the decision is actually made — its activity depends on the balance between BH3-only activators such as BID, BIM and PUMA and the anti-apoptotic proteins BCL-2, BCL-xL and MCL-1 that sequester both activators and BAX. That stoichiometry is what BH3-mimetic drugs such as venetoclax exploit; they kill through BAX and BAK rather than around them. Frameshift mutations in the BAX coding repeat are recurrent in microsatellite-unstable colorectal cancer.

## Why it appears in this work

BAX marks the apoptotic arm of p53's output. Its induction is the transcript-level signal that p53 reached the death machinery rather than stopping at arrest through [[The p21-DREAM axis]]. It is also the clearest example in this gene set of why mRNA is a lossy readout of apoptotic commitment: whether BAX kills is set by protein stoichiometry at the mitochondrion, and BAX protein is abundant and comparatively long-lived on the timescale of the 24 h window used in [[Tahoe-100M]]. A modest transcript move here can mean much less, or much more, than the same move in a gene with near-zero baseline such as [[BBC3]].

## What is uncertain

How much of a p53 transcriptional target BAX really is remains contested. The promoter work was done in a small number of systems, and across cell types BAX induction after p53 activation is usually modest and inconsistent, with PUMA and NOXA responding far more strongly; in several lineages BAX mRNA barely moves while apoptosis proceeds. So for this vault the direct-versus-indirect question is less interesting than the magnitude question: BAX is a genuine target whose transcriptional arm is probably not where its p53 dependence mostly lives. Mechanistically, whether PUMA and BID activate BAX directly or only by displacing it from anti-apoptotic partners is still argued, with evidence for both. The transcription-independent mechanism in which cytoplasmic p53 activates BAX directly is accepted by some groups and disputed by others. And Bax-null mice have a mild phenotype, which says BAK covers for it in most tissues.

## References

- Oltvai, Milliman and Korsmeyer, 1993, Cell — identified BAX as a BCL-2-interacting protein that promotes apoptosis.
- Miyashita and Reed, 1995, Cell — showed p53 is a direct transcriptional activator of the human BAX promoter.
- Wei et al., 2001, Science — showed BAX and BAK are jointly required for mitochondrial apoptosis.
- Chipuk et al., 2004, Science — reported direct activation of BAX by cytoplasmic p53, independent of transcription.
- Knudson et al., 1995, Science — characterised Bax-deficient mice, showing a limited phenotype consistent with redundancy.

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 10.52 CPM |
| Lines where detected | 50 of 50 |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 47 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.060× |
| Wild-type minus altered | 1.104× |
| Compounds moving it up in WT lines | 53 of 98 |
| Direction mixed? | **yes** — it goes each way across compounds, so its direction is not a fact about the gene |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00018 |
| As a percentage | -0.01% |
| FDR, exposure-shuffle null | 0.9720 |
| In TP53-wild-type lines / altered lines | -0.00692 / 0.00390 |
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
