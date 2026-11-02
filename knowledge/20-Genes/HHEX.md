---
symbol: HHEX
type: gene
tier: 2
tags: [gene, transcription-factor]
generated_by: knowledge/_build/build_vault.py
---

# HHEX

> [!summary] In one line
> HHEX encodes a homeodomain transcriptional repressor, also called PRH, required for liver, thyroid, forebrain and vascular development and for definitive haematopoiesis.

## What it is

HHEX was cloned from haematopoietic cells and has three parts: a long proline-, glycine- and alanine-rich N-terminal domain, a central homeodomain, and an acidic tail. It represses by two routes worth keeping separate. The N-terminal domain recruits Groucho/TLE co-repressors — see [[TLE4]] — giving promoter-level repression; separately, the same region binds eIF4E and blocks nuclear export of specific mRNAs, a post-transcriptional mechanism involving no DNA binding. Loss of Hhex in mouse is embryonic-lethal with defective forebrain, liver, thyroid, vasculogenesis and definitive haematopoiesis, and the gene stays expressed in adult thyroid, liver, lung and blood. The locus is also an early replicated type 2 diabetes association signal, reported as an IDE–[[KIF11]]–HHEX linkage block whose causal gene was never pinned down.

## Why it appears in this work

HHEX enters through [[Transcription factor activity inference]], not p53 biology: its inferred regulon activity is among the strongest negative associations with measured MG53. Read at face value that would place a repressor upstream of TRIM72. Nothing here licenses a causal reading, and HHEX is close to the worst case for the method.

## What is uncertain

Activity inference assumes a factor's targets move with it; for a repressor that inverts the sign, and for one that also acts on mRNA export the inferred activity mixes two mechanisms into one number. "Repressor" is itself shorthand — PRH activates some targets as well — so there is no one sign to invert. The regulon used here is small, and HHEX's own expression is restricted enough that many of these lines likely carry little of it — inference from a thin, possibly inactive regulon is weak evidence either way. Which HHEX targets are direct is itself open outside a few developmental loci.

## References

- Crompton et al., 1992, Nucleic Acids Research — identified Hex/HHEX as a homeobox gene expressed in haematopoietic cells.
- Martinez Barbera et al., 2000, Development — Hex is required in definitive endoderm for normal forebrain, liver and thyroid formation.
- Soufi and Jayaraman, 2008, Biochemical Journal — review of PRH/HHEX as an oligomeric transcription factor and multifunctional regulator of cell fate, covering the Groucho/TLE and eIF4E interactions and the dual repression/activation behaviour.
- Sladek et al., 2007, Nature — genome-wide association study implicating the HHEX region in type 2 diabetes.

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.01647 |
| As a percentage | +1.15% |
| FDR, exposure-shuffle null | 0.2515 |
| In TP53-wild-type lines / altered lines | 0.02823 / 0.01086 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.302 raw, -0.106 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

### As a transcription factor, against MG53

| | |
|---|---|
| Regulon size used | 20 targets |
| Activity vs MG53 across exposures (r) | -0.224 (q 1.14e-11) |
| With 3 principal components removed | -0.183 (q 5.43e-08) |
| Within line, across exposures (r) | -0.028 (q 0.030) |
| Percentile against all genes | 3.9 |

## Links

- **Concepts:** [[Transcription factor activity inference]]
- **Findings:** [[Downstream of MG53]], [[Upstream of MG53]]
- **Why this gene is in the vault:** transcription factor, negative rank
- **Indexes:** [[Genes — Map of Content]]

## Sources

- Program and MG53 columns: `mg53_p53/findings/tables/tableD_p53_target_genes.csv`
- Genome-wide screen: `genome_wide/tables/c_screen_genes.csv.gz`
- Curated effector columns: `mg53_p53/findings/tables/p53_effectors_per_gene.csv`
- Transcription-factor activity: `upstream_tf/tables/a1a2_tf_summary.csv`
