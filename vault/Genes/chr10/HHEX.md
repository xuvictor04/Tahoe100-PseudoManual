---
symbol: "HHEX"
type: "gene"
col: 7661
ensembl_id: "ENSG00000152804"
name: "hematopoietically expressed homeobox"
location: "10q23.33"
module: 16
arm: "+"
pooled_cpm: 2.3
n_lines_expressing: 32
n_dd_up: 15
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 6
tags: ["gene", "module/016", "written"]
generated_by: "tahoemap"
---

# HHEX

*hematopoietically expressed homeobox* — 10q23.33

> [!note] Written for the earlier MG53/p53 study
> The written section below was written for an earlier study on the same data (MG53/TRIM72 and p53). Where it mentions a score, a rank, a regulon, an association or "this batch", it refers to that study's analysis (transcription-factor activity inferred from target sets, and MG53 as the exposure), which tahoemap does not compute. This run's own numbers are in the generated sections below.

> [!summary] In one line
> HHEX encodes a homeodomain transcriptional repressor, also called PRH, required for liver, thyroid, forebrain and vascular development and for definitive haematopoiesis.

## What it is

HHEX was cloned from haematopoietic cells and has three parts: a long proline-, glycine- and alanine-rich N-terminal domain, a central homeodomain, and an acidic tail. It represses by two routes worth keeping separate. The N-terminal domain recruits Groucho/TLE co-repressors — see [[TLE4]] — giving promoter-level repression; separately, the same region binds eIF4E and blocks nuclear export of specific mRNAs, a post-transcriptional mechanism involving no DNA binding. Loss of Hhex in mouse is embryonic-lethal with defective forebrain, liver, thyroid, vasculogenesis and definitive haematopoiesis, and the gene stays expressed in adult thyroid, liver, lung and blood. The locus is also an early replicated type 2 diabetes association signal, reported as an IDE–[[KIF11]]–HHEX linkage block whose causal gene was never pinned down.

## What is uncertain

Activity inference assumes a factor's targets move with it; for a repressor that inverts the sign, and for one that also acts on mRNA export the inferred activity mixes two mechanisms into one number. "Repressor" is itself shorthand — PRH activates some targets as well — so there is no one sign to invert. Its curated target set is small, and HHEX's own expression is restricted enough that many of these lines likely carry little of it — inference from a thin, possibly inactive regulon is weak evidence either way. Which HHEX targets are direct is itself open outside a few developmental loci.

## References

- Crompton et al., 1992, Nucleic Acids Research — identified Hex/HHEX as a homeobox gene expressed in haematopoietic cells.
- Martinez Barbera et al., 2000, Development — Hex is required in definitive endoderm for normal forebrain, liver and thyroid formation.
- Soufi and Jayaraman, 2008, Biochemical Journal — review of PRH/HHEX as an oligomeric transcription factor and multifunctional regulator of cell fate, covering the Groucho/TLE and eIF4E interactions and the dual repression/activation behaviour.
- Sladek et al., 2007, Nature — genome-wide association study implicating the HHEX region in type 2 diabetes.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.76× (z +7.5, q 5e-11, up in 12 of 19 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.06× (z +6.8, q 3e-09, up in 10 of 19 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (J82 0.151×; ⚠ cell-cycle shift, explains ~14% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TIFA]] (+0.51, fdr 4e-05), [[ISOC1]] (+0.51, fdr 1e-05), [[DLX1]] (+0.50, fdr 3e-05); moves opposite to [[SPG7]] (-0.47, fdr 6e-05), [[SARM1]] (-0.47, fdr 6e-04), [[AP2A1]] (-0.46, fdr 3e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 6 go from it, the strongest it → [[NAP1L4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 9 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7661.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.76×** | +7.5 | 5e-11 | 12/19 (CFPAC-1, HOP62, …) | rises with dose | composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.25×** | +7.3 | 9e-11 | 8/11 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.06×** | +6.8 | 3e-09 | 10/19 (CFPAC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **2.08×** | +6.6 | 7e-09 | 11/25 (CFPAC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.94×** | +6.0 | 3e-07 | 0/4 | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.79×** | +5.3 | 1e-05 | 6/15 (HOP62, PANC-1, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.72×** | +5.1 | 2e-05 | 5/9 (SW480, NCI-H460, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~24% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.72×** | +5.1 | 2e-05 | 8/28 (A549, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.35×** | +4.0 | 0.004 | 7/28 (A549, NCI-H2347, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **1.50×** | +3.8 | 0.008 | 5/19 (SK-MEL-2, CFPAC-1, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.47×** | +3.6 | 0.017 | 3/27 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | **1.45×** | +3.5 | 0.021 | 0/15 | rises with dose | composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.02×** | +3.4 | 0.025 | 0/7 | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.29×** | +3.4 | 0.030 | 5/21 (A549, PANC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.033 | 10/27 (SW480, MIA PaCa-2, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7661.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (J82 0.151×; ⚠ cell-cycle shift, explains ~14% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Orlistat (drug)]] 5 µM |  | 0.692× | -3.3 | 0.55 | 4/26 (NCI-H23, SNU-423, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7661. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 9.29 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.5× (z +16.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 7.89× (z +9.2) | — |
| [[HOP62 (line)]] | alt | 2.86 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.47× (z +9.7) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[J82 (line)]] | alt | 3.37 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.151× (z -8.6) ⚠ cell-cycle shift, explains ~14% of this change |
| [[A-172 (line)]] | wt | 0.180 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 3.06 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.49 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.09 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.365 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.148 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.256 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.185 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.816 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.397 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.202 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.231 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.177 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.440 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.639 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.172 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.729 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.231 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.607 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.500 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.90 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.178 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.546 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.167 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.15 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.435 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.739 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.197 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.17 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7661), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIFA]] | +0.51 | +0.41 / +0.58 | both halves | 4e-05 |  |
| [[ISOC1]] | +0.51 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[DLX1]] | +0.50 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[SIX1]] | +0.50 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[IKZF3]] | +0.50 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[ZNF816]] | +0.50 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[SERTAD4]] | +0.50 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[CDC42EP3]] | +0.49 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[DCLRE1A]] | +0.49 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[ZNF711]] | +0.49 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[TIGD2]] | +0.48 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[ENC1]] | +0.48 | +0.52 / +0.40 | both halves | 4e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPG7]] | -0.47 | -0.38 / -0.49 | both halves | 6e-05 |  |
| [[SARM1]] | -0.47 | -0.22 / -0.58 | both halves | 6e-04 |  |
| [[AP2A1]] | -0.46 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[GNPTG]] | -0.46 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[CD81]] | -0.46 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[LINC02614]] | -0.46 | -0.27 / -0.54 | both halves | 3e-04 |  |
| [[CA5B]] | -0.45 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[SLC35F5]] | -0.44 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[RAB5C]] | -0.44 | -0.37 / -0.52 | both halves | 8e-05 |  |
| [[CYB5R3]] | -0.44 | -0.38 / -0.45 | both halves | 6e-05 |  |
| [[SLC25A16]] | -0.44 | -0.31 / -0.43 | both halves | 2e-04 |  |
| [[MROH1]] | -0.44 | -0.28 / -0.55 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NAP1L4]] | B | HHEX activity raises NAP1L4's level | lines that do not express HHEX (18) vs lines expressing it (32) | 1.13× lower at baseline in the lines without HHEX | 0.023 | ⚠ within organs, on part of the lines; also absent: HEYL, MT1A, NUP62CL |
| [[KCTD12]] | B | HHEX activity lowers KCTD12's level | lines that do not express HHEX (18) vs lines expressing it (32) | 1.07× higher at baseline in the lines without HHEX | 0.033 | ⚠ within organs, on part of the lines; also absent: HEYL, MT1A, NUP62CL |
| [[RHOA]] | B | HHEX activity raises RHOA's level | lines that do not express HHEX (18) vs lines expressing it (32) | 1.15× lower at baseline in the lines without HHEX | 0.060 | ⚠ within organs, on part of the lines; also absent: HEYL, MT1A, NUP62CL |
| [[ZNF280B]] | B | HHEX activity raises ZNF280B's level | lines that do not express HHEX (18) vs lines expressing it (32) | 1.48× lower at baseline in the lines without HHEX | 0.067 | ⚠ within organs, on part of the lines; also absent: HEYL, MT1A, NUP62CL |
| [[CYB5R3]] | B | HHEX activity strengthens CYB5R3's drug response | lines that do not express HHEX (18) vs lines expressing it (31) | the lines without HHEX respond 0.94× as strongly (z diff +0.19); strongest at Homoharringtonine 5 µM: 0.66x vs 0.46x (z diff +3.3) | 0.069 | ⚠ within organs, on part of the lines; also absent: HEYL, MT1A, NUP62CL; target measured in part of the lines; both ways; artifact flags |
| [[CD81]] | B | HHEX activity lowers CD81's level | lines that do not express HHEX (18) vs lines expressing it (32) | 1.07× higher at baseline in the lines without HHEX | 0.075 | ⚠ within organs, on part of the lines; also absent: HEYL, MT1A, NUP62CL |

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.396). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (22.0, -10.3); signed map (17.4, -11.2). **Vector** length 31.6, 4.18% of its response variance represented; |z| ≥ 3 in 596 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +2.3 | +7.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.0 | +6.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.0 | +6.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +1.6 | +7.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.5 | +3.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +0.7 | -0.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +0.6 | +1.0 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | +0.5 | +2.6 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +0.5 | +1.5 |
| fall | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.1 | -1.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -0.9 | -2.1 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -0.9 | -2.0 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -0.7 | -1.2 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -0.7 | -0.8 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | -0.6 | -1.8 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -0.6 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | hematopoietically expressed homeobox |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q23.33 — chr10:92,689,955-92,695,647 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HEX, HOX11L-PEN; previously PRHX |
| Gene groups (HGNC) | NKL subclass homeoboxes and pseudogenes |
| Hallmark sets | REACTIVE_OXYGEN_SPECIES_PATHWAY |
| Reactome | 2 pathways, smallest: POU5F1 (OCT4), SOX2, NANOG repress genes related to differentiation; Transcriptional regulation of pluripotent stem cells |
| Matched by | ensembl_id |

**Function**, from UniProt [Q03014](https://www.uniprot.org/uniprotkb/Q03014) (Hematopoietically-expressed homeobox protein HHEX):

> Recognizes the DNA sequence 5'-ATTAA-3' (By similarity). Transcriptional repressor (By similarity). Activator of WNT-mediated transcription in conjunction with CTNNB1. Establishes anterior identity at two levels; acts early to enhance canonical WNT-signaling by repressing expression of TLE4, and acts later to inhibit NODAL-signaling by directly targeting NODAL (By similarity). Inhibits EIF4E-mediated mRNA nuclear export. May play a role in hematopoietic differentiation.

**Summary**, from NCBI Gene [3087](https://www.ncbi.nlm.nih.gov/gene/3087):

> This gene encodes a member of the homeobox family of transcription factors, many of which are involved in developmental processes. Expression in specific hematopoietic lineages suggests that this protein may play a role in hematopoietic differentiation. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:4901](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4901) · Entrez [3087](https://www.ncbi.nlm.nih.gov/gene/3087) · UniProt [Q03014](https://www.uniprot.org/uniprotkb/Q03014) · Ensembl [ENSG00000152804](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152804)

## Data

Gene col 7661: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7661); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7661, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7661]; `tensor/DDL_lfc|DDL_z.npy` [7661]; `embed/gene_vectors.npy` [7661]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7661 or target_col == 7661). Every well: [[HHEX — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/HHEX.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
