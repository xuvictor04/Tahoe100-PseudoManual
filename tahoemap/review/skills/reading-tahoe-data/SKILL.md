---
name: reading-tahoe-data
description: What every number in a Tahoe-100M gene-map dossier means and how far it can be trusted - baselines, pooled versus single-line values, z, q, fdr, evidence halves, mutual rank, specificity, artifact flags, modules and arms, drug and line sections, and the limits of the design. Use it whenever a dossier or a tahoe_lookup result is being interpreted.
---

# Reading the Tahoe-100M data

## The experiment

Tahoe-100M profiled about 100 million single cells: 50 cancer cell lines grown together in every well (each cell is
assigned to its line by genotype), 379 drugs at three doses (mostly 0.05, 0.5 and 5 uM), 24 hours of exposure, 14
plates of 96 wells, single-cell RNA counts. The gene map sums each line's cells per well (a pseudo-bulk profile per
well and line) and works from those profiles.

It measures steady-state mRNA after 24 h, nothing else: not protein, phosphorylation, localisation, activity or
splicing. A gene whose protein is regulated (stabilised, cleaved, phosphorylated) shows nothing here unless its
mRNA also changes. Genes named SYNTH0001 and so on, and Ensembl-style ids beginning ENSG9, belong to the synthetic
test data: no literature exists for them.

## Every fold change is against the typical drugged well, not DMSO

The baseline of a fold change is the same cell line's median over the plate's drug wells. Two DMSO wells per plate
are too few to be a baseline, and most drugs leave most genes alone, so the median drugged well is close to
untreated. Two consequences:

- A fold of 1.0x means "like a typical drugged well". For a gene that many drugs on a plate move (a generic stress
  gene), the baseline moves too and fold changes shrink.
- Effects are also corrected for library composition (median-of-ratios), so they are relative to the median gene.
  When a drug shuts transcription down globally, stable mRNAs then appear to rise; the `transcription drop` flag marks
  such drug-doses.

The well-position effect (a drug sits at the same position on every plate) is estimated from the other drugs at that
position and removed.

## Pooled values: the median over the measured lines

The "raised by / lowered by" tables are pooled: per well, the median over the lines that measure the gene; per
drug-dose, the mean over its wells (fold) and a Stouffer sum (z). A pooled call therefore means that more than half
of the measured lines moved. A response confined to a few lines, for example a p53 response in the TP53-wild-type
lines only, or a lineage-restricted one, can be invisible in the pooled table and strong in the single-line table.

- fold = 2^lfc; z = robust z against the spread of the plate's drug wells, divided by the plate factor on noisy
  plates (caveat `noisy plate (z scaled)`).
- q = Benjamini-Hochberg within the gene over all ~1,100 drug-doses. Significant = q < 0.10 and fold >= 1.2x (or <=
  1/1.2x). One significant drug-dose at q ~ 0.08 is weak evidence; the same drug at two or three doses rising with
  dose, or several drugs of one class, is strong.
- "lines moved / measured": lines with per-line z >= 2 and >= 1.2x among the lines that measure the gene. This is a
  description of where the pooled effect shows, not a per-line test: a line with no effect also passes now and then
  (the dossier gives the run's chance rates, typically under 1% upwards and a few % downwards).
- Dose pattern: "rises with dose", "two highest doses" and "all doses" are consistent responses; "single dose" or
  "top dose only" at 5 uM can be cytotoxicity; "inconsistent across doses" makes a single-dose call fragile. Each dose
  sits on its own plates, so dose is confounded with plate.
- Most drug-doses have a single well (about 1,024 of 1,132 on the full data). Their significance rests on the spread
  of the other wells, not on replicates; "replicate r" exists only with two or more wells.

## Single-line values

Per-line fold = that line's change against its own baseline; per-line z likewise. The single-line tables use a cut
calibrated on the run (never below 4; the dossier states it) so that about 0.05 chance calls are expected per gene
and line. A large per-line fold with a pooled fold near 1x is a response specific to that line or a few lines.

Lines that do not express a gene (below a quarter of the median line, or reading only the well's ambient RNA, or
with too few counts) are "not measured": they have no per-line value. "Not measured" is not "not induced", and the
re-expression of a gene a line has silenced cannot be detected.

## Flags

Artifact flags make a drug-dose (or one gene's value) unclean; the gene's change may be the artifact:

| flag | what happened | how to read the genes |
|---|---|---|
| `toxic` | the line's cells fell to under half the plate's (beyond their plate row), with no recovery at a higher dose | dying and stressed cells dominate: stress, ISR, p53, apoptosis genes rise and proliferation genes fall whatever the target |
| `transcription drop` | genes or UMIs per cell fell: global shutdown (e.g. CDK7/CDK9 or RNA polymerase inhibition) | short-lived mRNAs (MYC, immediate-early genes, histones) fall first; after the composition correction stable mRNAs appear to rise; do not read single genes |
| `cell-cycle shift` | the S-phase or G2/M programme moved | cycle genes follow the share of cells in S and G2/M; a CDK4/6 inhibitor lowers E2F targets by arresting cells, not by regulating each gene |
| `unreliable plate only` | only wells on the unreliable plate | not reproducible; ignore unless confirmed elsewhere |
| `position not correctable` | too few other drugs at the well position | a position artifact cannot be excluded |
| `position correction uncertain` | (per gene) too few clean donors at the position | the same, for that gene |
| `wells disagree` | two or more wells whose profiles do not correlate | one well may be wrong |

Soft caveats do not make a value unclean but deserve a mention when a conclusion rests on that drug-dose: `low cells
(technical?)`, `plate-row cell shift`, `composition shift`, `noisy plate (z scaled)`, `position effect removed`.
A gene the dossier says "tracks the S-phase / G2/M programme" moves with any drug that changes proliferation.
Noise-class RNAs (snoRNA, mitochondrial, ribosomal-protein pseudogenes, replication-dependent histones) need care.

## The vector space and the data partners

Each gene's response pattern across tens of thousands of (active drug-dose, cell line) contexts is denoised by an
SVD (64 dimensions on the full data). The cosine between two genes is the correlation of their denoised response
patterns. Random pairs have cos ~ 0; |cos| 0.3 is moderate, >= 0.5 strong, >= 0.7 very strong. Positive: the two
move together. Negative: one rises where the other falls, often the induced and the repressed arm of one response
(p53 targets against the G2/M genes p53 represses through p21 and DREAM), or two programmes the same drugs push in
opposite directions. Neither sign is a regulatory arrow: no gene was knocked out or overexpressed.

Only genes with a real response are in the space (enough contexts at |z| >= 3, and a significant clean pooled
drug-dose or a strong single-line response in two lines). A gene outside the space has no partners, module or arm;
that says only that no drug moved it detectably.

Partner columns:
- **evidence**: `both halves` = the compounds were split into two random halves (by a hash of the compound name, salt
  forms together) and the pair has the same sign in the full space and in both halves, |cos| >= 0.2 in each, at
  fdr <= 0.10: replicated across independent perturbations. `one half` = |cos| >= 0.5 in one half only: driven by
  the compounds of one half, often a single compound; a hypothesis, not a finding. `not reproduced` = neither.
- **fdr**: sign-concordance false discovery rate, read at the pair's weaker half cosine.
- **mutual rank**: the larger of the two genes' ranks for each other (1 = each is the other's strongest partner;
  ">100" = not reciprocal).
- **specificity**: how exceptional the pair is for both genes (the smaller of the two robust z scores of the pair
  within each gene's partner list). Broad programmes (proliferation, stress, interferon) make hundreds of replicable
  pairs; low mutual rank with specificity >= 3-4 marks a particular relation, high cos with specificity ~2 marks
  membership of the same large programme.
- **genomic**: `same locus` (<= 50 kb) and `READTHROUGH RISK` (same strand, <= 20 kb, the 5' gene >= 8x more
  expressed). Such pairs can co-vary through readthrough transcription, shared regulatory elements or reads assigned
  to the neighbour; they are not evidence of a functional link and are never called novel.
- **known**: STRING combined score (>= 400 recorded; >= 700 high confidence; the evidence channel is not given: it
  can be physical binding, co-expression, text mining or database transfer), a shared Reactome set (<= 300 genes) or
  Hallmark set, a shared HGNC gene group (often paralogs). "Known" is not "known to be co-regulated at the mRNA
  level".
- **NOVEL CANDIDATE**: mutually among each other's 10 strongest partners, specificity >= 4, both halves at fdr <=
  0.05, |cos| >= 0.5, no STRING link, shared pathway or gene group, not the same locus, both genes annotated. Novel
  means only "absent from these databases"; many are documented targets of one transcription factor.

**Known but absent**: partners with STRING >= 700 or a shared Hallmark / Reactome set of <= 100 genes that are not
among the gene's 100 data partners, with their cosine and the rank of |cos| among all genes in the space (rank just
above 100 = nearly a partner; cos ~ 0 = unrelated in these data), or why no cosine exists (not in the space, not
measured).

## Modules and arms

Modules are communities of the graph that links each gene to its strongest replicated partners. A module's label
comes from gene-set enrichment (Hallmark, Reactome, the curated control sets) or, when nothing is enriched, from its
top genes. Very large sets ("Metabolism", "Signal transduction") make weak labels: read the list of enriched sets.
A module has a + and a - arm only when its two sides anti-correlate under the same drugs; otherwise all members are +.
"Guilt by association" lines say that the gene sits in a module enriched for a set it is not annotated to.

## Drug sections

- Targets and mechanism come from Tahoe's drug metadata and can be incomplete ("unclear") or wrong. Salt forms are
  separate drugs.
- Doses: compare with the drug's known potency and exposure. A nanomolar inhibitor active only at 5 uM is probably
  acting off target or through toxicity; a 0.05 uM response of a potent drug is on target.
- The best dose has the most significant genes; the best trustworthy dose (no untrusted flag) defines the drug's
  vector. Read its flags before reading its genes.
- The targets' own mRNA: inhibiting a protein rarely changes its mRNA; feedback can raise it (statins raise HMGCR
  through SREBP2, proteasome inhibitors raise proteasome genes through NFE2L1, HSP90 inhibitors raise HSP70 genes).
- Modules it moves: module score = mean pooled z of the + arm minus the - arm.
- Lines it depletes: the line's cell count relative to the other lines in the same wells at 24 h (relative abundance
  z <= -3). It measures selective loss; a drug that kills every line equally depletes none.
- Response strength (DD_beta): how strongly each line shows the drug's consensus response (1 = typical, 0 = none).
- Nearest drugs: cosine of the drug vectors, i.e. similar transcriptional effect, not shared targets.

## Cell-line sections

- Organ, drivers and protein changes come from Tahoe's cell-line metadata and can be incomplete; TP53 status is
  derived from that drivers list.
- Genes specifically high or low at baseline (the line against the median of the other lines) reflect lineage,
  copy number (amplicons put neighbouring genes high together; deletions such as 9p21 CDKN2A / CDKN2B / MTAP make them
  absent), mutation-driven programmes (KEAP1 or NFE2L2 mutation raises NRF2 targets) and silencing. "Measured here:
  no" means below the ambient-RNA floor, consistent with deletion or silencing.
- Drivers' own mRNA: deletions and nonsense changes usually lower it; missense changes usually do not.
- Programmes it responds to more or less: per component of the vector space, the line's response slope (1 = typical
  line, 0 = no response), with the component's top genes and drug-doses; a TP53-mutant line is expected to respond
  weakly to the p53 programme.

## What these data cannot say

Co-variation across drug responses is not mechanism; reserve "upstream", "downstream" and "regulates" for what a
paper shows. One time point (24 h): transient early responses may be over and secondary effects included. Cancer
cell lines in culture, without tissue context, immune cells or hypoxia. mRNA only. Dose confounded with plate. Most
drug-doses in one well.
