---
symbol: MDM2
type: gene
tier: 1
aliases: [HDM2]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
curated_effector: true
effector_role: negative feedback
median_line_cpm: 185.8
mg53_verdict: down with MG53
mg53_effect_on_p53_output: toward LESS p53 output
tags: [curated-effector, gene, mg53-associated, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# MDM2

> [!summary] In one line
> MDM2 is the E3 ubiquitin ligase that binds, silences and destroys p53, and is itself one of p53's most strongly induced target genes — the negative feedback loop at the centre of p53 control.

## What it is

MDM2 is a three-part protein. Its N-terminal hydrophobic cleft grips the p53 transactivation domain through three p53 residues — Phe19, Trp23, Leu26 — which blocks coactivator recruitment and switches p53 off as a transcription factor. A central acidic region makes a second, weaker contact with the p53 core and is required for efficient degradation. The C-terminal RING is the catalytic end: MDM2 is a genuine E3 ubiquitin ligase for p53, polyubiquitinating it for proteasomal destruction and, at lower MDM2 levels, monoubiquitinating it in a way that favours nuclear export. p53 protein is consequently short-lived in unstressed cells not because it is made slowly but because MDM2 is constantly removing it.

The mouse genetics are unambiguous: *Mdm2*-null embryos die very early and deleting *Trp53* rescues them completely, so MDM2's essential job is restraining p53.

Regulation is a loop. p53 binds an internal P2 promoter in MDM2's first intron, so activating p53 raises MDM2 transcription, which then lowers p53 — the topology that produces the pulsatile p53 dynamics seen in single cells. The loop is broken from several directions: ATM-dependent phosphorylation of p53 at Ser15 and of MDM2 itself weakens the interaction after DNA damage; p14ARF sequesters MDM2 in the nucleolus; ribosomal proteins bind the acidic domain under ribosomal stress; and [[MDM4]] heterodimerises with MDM2 through the RING and tunes its activity. Clinically, MDM2 is amplified rather than mutated, classically in sarcomas and generally in tumours that retain wild-type TP53. It is the target of the nutlins and their clinical successors, which occupy the p53-binding cleft and so reactivate p53 only where TP53 is intact.

## Why it appears in this work

MDM2 is the brake p53 builds for itself, and it sits near the top of the induction arm of [[p53 program P]] while being expressed highly enough to measure well in single cells. That makes it one of the most trustworthy mRNA readouts that p53 is transcriptionally engaged, second only to [[CDKN1A]]. Its meaning is doubled, though: induced MDM2 says p53 is active *and* says the response is already attenuating. A 24 h snapshot in [[Tahoe-100M]] samples a loop, not a step — worth holding in mind whenever MDM2 induction is read as a dose of p53 activity.

## What is uncertain

MDM2 mRNA is not MDM2 activity. Phosphorylation, ARF sequestration, ribosomal-protein binding and MDM4 partnership all gate the ligase without changing the transcript, so transcript-level inference about the brake's strength is weak. Total MDM2 mRNA also mixes two pools — constitutive P1 output and p53-driven P2 output — and the usual measurement does not separate them, which matters when comparing wild-type against TP53-altered lines, since residual MDM2 expression there is P1, not residual p53. MDM2 has p53-independent substrates and non-catalytic activities that are real but less well mapped; how much of its oncogenic effect is p53-independent remains open. And because the loop oscillates with a period of a few hours in some systems, equal 24 h averages can arise from different pulse behaviour — a limit of the timepoint, not of the gene.

## References

- Momand et al., 1992, Cell — the mdm-2 product forms a complex with p53 and inhibits p53-mediated transactivation.
- Oliner et al., 1992, Nature — identified amplification of the gene encoding this p53-associated protein in human sarcomas.
- Wu et al., 1993, Genes & Development — described the p53–mdm-2 autoregulatory feedback loop.
- Haupt et al., 1997, Nature, and Kubbutat et al., 1997, Nature — showed that Mdm2 promotes rapid p53 degradation and controls p53 stability.
- Honda et al., 1997, FEBS Letters — identified MDM2 as a ubiquitin ligase E3 for p53.
- Vassilev et al., 2004, Science — in vivo activation of the p53 pathway by small-molecule MDM2 antagonists (the nutlins).

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 185.80 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 3 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.255× |
| Wild-type minus altered | 1.195× |
| Compounds moving it up in WT lines | 95 of 98 |
| Direction mixed? | no |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00500 |
| As a percentage | -0.35% |
| FDR, exposure-shuffle null | 0.0313 |
| In TP53-wild-type lines / altered lines | -0.00539 / -0.00476 |
| Verdict | down with MG53 |
| **Signed into p53-output units** | **toward LESS p53 output** |
| Co-regulation with MG53 across exposures (r) | 0.005 raw, 0.034 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

## Links

- **Concepts:** [[The p53 pathway]], [[p53 program P]]
- **Findings:** [[Downstream of MG53]], [[Upstream of MG53]]
- **Its own write-up:** [[MDM2 and MG53]]
- **Why this gene is in the vault:** curated p53 effector; p53 program, induction arm
- **Indexes:** [[Genes — Map of Content]]

## Sources

- Program and MG53 columns: `mg53_p53/findings/tables/tableD_p53_target_genes.csv`
- Genome-wide screen: `genome_wide/tables/c_screen_genes.csv.gz`
- Curated effector columns: `mg53_p53/findings/tables/p53_effectors_per_gene.csv`
