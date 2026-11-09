---
name: reading-tahoe-data
description: What every number in a Tahoe-100M gene-map dossier means and how far it can be trusted - baselines, pooled versus single-line values, z, q, fdr, evidence halves, mutual rank, specificity, artifact flags, modules and arms, drug and line sections, probable-direction arrows with their grades, signs and alerts, and the limits of the design. Use it whenever a dossier or a tahoe_lookup result is being interpreted.
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

Artifact flags make a drug-dose (or one gene's value) unclean; the gene's change may be the artifact. Nothing is left
out for a flag: a flagged item keeps its ranked place and is marked ⚠ followed by the reason in plain words, and
counts say how many items carry an alert. A list capped at N shows the N strongest, plus any of the N strongest
without an alert that would fall below them, so flagged items never push clean ones out of view.

| flag | what happened | how to read the genes |
|---|---|---|
| `toxic` | the line's cells fell to under half the plate's (beyond their plate row), with no recovery at a higher dose | dying and stressed cells dominate: stress, ISR, p53, apoptosis genes rise and proliferation genes fall whatever the target |
| `transcription drop` | genes or UMIs per cell fell: global shutdown (e.g. CDK7/CDK9 or RNA polymerase inhibition) | short-lived mRNAs (MYC, immediate-early genes, histones) fall first; after the composition correction stable mRNAs appear to rise; do not read single genes |
| `cell-cycle shift` | the S-phase or G2/M programme moved | cycle genes follow the share of cells in S and G2/M; a CDK4/6 inhibitor lowers E2F targets by arresting cells, not by regulating each gene. Judged gene by gene: the alert says how much of this gene's change the shift would explain ("cell-cycle shift, explains ~40%", from the gene's own slopes on the S-phase and G2/M programmes); where it explains little (less than half even with the slopes doubled, and what is left is still >= 1.2x) the gene's value reads `cell-cycle shift (explains ~N% here)`, is no artifact flag and is clean |
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

Only genes with a real response are in the space (enough contexts at |z| >= 3, and a significant pooled drug-dose
or a strong single-line response in two lines). A gene in the space only through significant drug-doses that carry
an artifact flag is marked ⚠: its vector, partners and module may reflect the artifact. A gene outside the space
has no partners, module or arm; that says only that no drug moved it detectably.

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
- The best dose has the most significant genes. The best trustworthy dose is the active dose with no artifact flag;
  its full gene lists come first. The drug's vector (nearest drugs) uses the embedding's dose, which may carry a
  toxic, transcription-drop or cell-cycle flag: the dossier names it and gives that dose's full lists too, marked
  FLAGGED (a flag can be the drug's own effect, such as an antimitotic's cell-cycle shift: say which). When no dose
  is trustworthy the dossier says so and lists the flags: read every gene list as possibly the artifact. Read a
  dose's flags before reading its genes.
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

## Probable direction (arrows)

A gene dossier ends with "Probable direction": arrows SOURCE → TARGET from the direction stage, in three tables -
upstream (what probably acts on the gene), downstream (the genes it probably acts on) and the cells under drug-doses
(how it probably acts on the cells' growth there: their numbers relative to the other lines in the same wells). A
`pair` look-up gives the arrows between two genes either way. The source is what a test conditions on; the target is
what differs with it. The arrow points one way because the source's state is set before the experiment (a mutation
cannot be a consequence of the target), not because regulation was shown.

| evidence | the test | how strong |
|---|---|---|
| `mutation: response / level / cells` | lines with a recorded loss-of-function, gain-of-function or any alteration of the source (Tahoe's cell-line genetics) against lines with no record of it; the target's response to its 10 strongest drug-doses, its baseline level, or the cells' numbers under a drug-dose; labels shuffled within organs (200 times) | the strongest kind; "not recorded" is not proof of wild type |
| `not expressed: response / level / cells` | lines where the source reads only ambient RNA (natural knockouts) against lines expressing it; only the source's related partners are tested | as strong as the lines allow; genes absent from the same lines share one test |
| `drug target: level` | compounds (>= 2 different molecules; one molecule under two names counts once) sharing the source as a listed target and one mechanism move the target's level the same way more often than the target's rate over all compounds | drugs act on proteins and on other targets too |
| `natural level: response / cells` | the source's lineage-adjusted level across the lines correlates with the target's response strength (or the cells' numbers); written whenever the correlation is significant, both ways when both are; "direction clear" only when the reverse is clearly weaker even after allowing for the arrow having been picked because it is strong (else the alert "direction unclear") | a glimpse (grade C): tissue and measurement precision can mimic it |

- **Grade**: A = a recorded mutation, at least 5 lines on each side compared within organs, significant over the
  whole table, no other recorded alteration concentrated on either side, and not resting on a correction; B = worth
  taking seriously, read its alerts; C = a glimpse, a lead to check, not a finding (also a mutation result the tissue
  can explain: tissue-confounded).
- **Sign** (the "probable direction" sentence): what the source's ACTIVITY probably does to the target. A level or the
  cells' numbers: *raises* / *lowers*. A drug response: *strengthens* / *weakens* - how strongly the target responds,
  **in its own direction at each drug-dose**: a higher rise where it rises, a deeper fall where it falls. Judge
  induction or repression from ALL the drug-doses the row lists ("drug-doses carrying the difference"), never from
  the first one alone: if every listed fold is below 1x (e.g. "SOURCE activity strengthens X's drug response" with
  "0.49x vs 0.80x at drug A; 0.55x vs 0.90x at drug B"), X falls further where the source is active, so the source
  represses it there; if every one is above 1x, the source induces it. A row with the alert "rises at some
  drug-doses, falls at others" has the target rising under some drugs and falling under others: its sign is about
  how strongly it responds, not whether the source induces or represses it - judge only who acts on whom, and call
  papers on induction or repression neither support nor contradiction of the sign. Never read "strengthens" as
  "raises the level". For a
  loss-of-function group, "TP53 activity strengthens CDKN1A's drug response" means CDKN1A responds less where TP53 is
  lost; for compounds that inhibit the source, a target they raise is one the source's activity lowers. "Not
  inferred": the mechanism of the alteration is not recorded, so only "the source is upstream of the target" is
  claimed. For the cells, "lowers the cells' numbers (makes them more sensitive)": lines with the source active lose
  more cells.
- **Numbers**: the comparison (lines on each side) and the stage's sentence with the target's fold in the two groups
  of lines at its strongest drug-dose ("1.32x vs 3.00x at 5-Fluorouracil 5 uM"), or r for a natural level (with the
  reverse correlation: "r +0.97; reverse +0.35"). q is Benjamini-Hochberg over every test of the kind; "q 0.24 over
  the table, 0.006 within its group" means significant only within its own group: a lead (the dossier says how many
  such arrows random groups give).
- **Alerts** (⚠, short labels in the tables, each reason in full once below them); none removes an arrow:

| label | what it means | weigh it |
|---|---|---|
| within its group / drug-dose only (a lead) | significant only within its own family of tests | a lead; random groups give some |
| few lines (N vs M) | 3-4 lines on a side | weak |
| tissue-confounded | the two sides' organs differ (e.g. most altered lines are pancreatic) | the tissue may explain it (grade C) |
| across organs / within organs, on part of the lines | how the lines were compared; within organs only lines in organs that hold both sides count | across organs is weaker |
| co-occurs with X | the altered lines are largely those altered in X | X may be the cause |
| X alterations on the other side | the lines compared against are largely those altered in X (e.g. TP53-intact colon lines are the KMT2D-altered MSI lines) | X may be the cause, with the opposite sign; blocks grade A |
| also absent: X, Y | other genes are absent from most of the same lines (co-deleted neighbours, e.g. MTAP with CDKN2A) | any of them could be the cause |
| X not expressed in N of the M altered lines | the source itself is absent from some altered lines (deletion, silencing) | consistent with loss |
| co-absent genes / shared targets | several genes absent from the same lines, or several targets of the same compounds: one test | any of them could be the cause |
| deletion recorded too | the lines lacking the gene carry a recorded deletion of it | genotype support |
| maybe low, not absent | the "absent" lines still read some of the gene | weaker knockout |
| rests on the correction / the reference differs / partly uncorrected / line-wide correction only | how the lines' general drug responsiveness was corrected; "rests on the correction": the difference appears only after it | "rests on" is weak; "line-wide correction only" is usual |
| lower baseline (lost expression?) | the target is lower at baseline in the altered lines | a weaker response may be lower expression |
| both ways | part of the evidence goes the other way | mixed |
| not significant pooled | the target's response shows in part of the lines only | expected for a genotype-dependent response |
| its own permutation p / target measured in part of the lines | few arrangements of the lines, or few lines measured | the p-value is conservative |
| artifact flags | supporting drug-doses carry artifact flags (toxic, transcription drop ...) | read those drug-doses with care |
| tissue can mimic it / precision caveat / direction unclear | the standing caveats of a natural-level arrow; "direction unclear": the reverse correlation is not clearly weaker once it is allowed for that the arrow was written because it is strong (which alone makes it look the stronger) | a glimpse at most; without this alert the direction passed that test |
| off-target possible / N compounds / sign not inferred | the caveats of a drug-target arrow | as the label says |

An arrow is a probable direction from 50 cancer cell lines at 24 h, not proof of direct regulation: A → B → C looks
like A → C, another alteration of the same lines can be the cause, and compensation and feedback are not seen. The
absence of an arrow says nothing: only recorded mutations, genes some lines do not express, drug targets and related
pairs (for levels) are tested.

## What these data cannot say

Co-variation across drug responses is not mechanism, and an arrow of the "Probable direction" tables is a probable
direction from the cell lines, not proof; reserve "regulates" and "a direct target" for what a paper shows. One time point (24 h): transient early responses may be over and secondary effects included. Cancer
cell lines in culture, without tissue context, immune cells or hypoxia. mRNA only. Dose confounded with plate. Most
drug-doses in one well.
