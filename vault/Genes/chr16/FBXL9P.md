---
symbol: "FBXL9P"
type: "gene"
col: 4587
ensembl_id: "ENSG00000125122"
name: "F-box and leucine rich repeat protein 9, pseudogene"
location: "16q22.1"
module: 89
arm: "+"
pooled_cpm: 7.05
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 18
n_dd_up_clean: 1
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/089"]
generated_by: "tahoemap"
---

# FBXL9P

*F-box and leucine rich repeat protein 9, pseudogene* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Clobetasol propionate (drug)]] 0.05 µM: 1.53× (z +3.9, q 0.049, up in 15 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (9 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.265× (z -12.1, q 4e-31, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF594]] (+0.59, fdr 4e-05), [[ZNF302]] (+0.58, fdr 2e-05), [[ZNF181]] (+0.58, fdr 3e-05); moves opposite to [[PRPS2]] (-0.53, fdr 1e-05), [[PRKAR2B]] (-0.53, fdr 7e-05), [[RAPGEF5]] (-0.52, fdr 3e-05).
> It is in [[Module 089]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[RAPGEF5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4587.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.53×** | +3.9 | 0.049 | 15/45 (HT-29, HS-578T, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.49× | +3.5 | 0.11 | 13/45 (SW480, C-33 A, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.29× | +3.4 | 0.11 | 11/47 (PANC-1, BT-474, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | 1.29× | +3.4 | 0.11 | 15/42 (NCI-H2030, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.30× | +3.3 | 0.12 | 13/48 (SW480, NCI-H460, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.27× | +3.1 | 0.18 | 8/47 (NCI-H2030, LS 180, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.39× | +3.1 | 0.18 | 11/45 (HS-578T, Hs 766T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 9 with an alert ⚠. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4587.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.265×** | -12.1 | 4e-31 | 44/48 (PANC-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.329×** | -9.8 | 4e-20 | 30/36 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.380×** | -8.9 | 2e-16 | 35/46 (PANC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.391×** | -8.6 | 1e-15 | 27/40 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.442×** | -7.5 | 1e-11 | 30/45 (HOP62, PANC-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.470×** | -6.6 | 3e-09 | 26/46 (MIA PaCa-2, NCI-H460, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.534×** | -5.7 | 8e-07 | 27/47 (RPMI-7951, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.540×** | -5.6 | 1e-06 | 27/48 (C-33 A, NCI-H460, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.562×** | -5.3 | 9e-06 | 25/46 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.395×** | -4.4 | 5e-04 | 18/46 (PANC-1, NCI-H23, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.396×** | -4.4 | 5e-04 | 25/41 (HOP62, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change | **0.633×** | -4.2 | 0.001 | 17/27 (PANC-1, A-172, …) | inconsistent across doses | composition shift; position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.450×** | -3.8 | 0.006 | 15/45 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.676×** | -3.6 | 0.015 | 17/46 (MIA PaCa-2, A549, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.703×** | -3.2 | 0.050 | 18/45 (HS-578T, Panc 03.27, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.615×** | -3.2 | 0.055 | 8/47 (NCI-H460, SNU-1, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.714×** | -3.1 | 0.072 | 10/48 (A-427, SW1417, …) | rises with dose | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.794×** | -3.0 | 0.095 | 15/47 (SNU-1, CFPAC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.53 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4587. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 9.93 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0600× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.124× (z -10.7) |
| [[PANC-1 (line)]] | alt | 7.47 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.103× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.131× (z -11.5) |
| [[MIA PaCa-2 (line)]] | alt | 10.6 | 0 | 4 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0486× (z -13.3) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.108× (z -10.2) |
| [[HOP62 (line)]] | alt | 10.9 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0835× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[RPMI-7951 (line)]] | alt | 12.5 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0709× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[A-172 (line)]] | wt | 9.91 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.141× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change |
| [[BT-474 (line)]] | alt | 5.20 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.0579× (z -9.3) |
| [[hTERT-HPNE (line)]] | wt | 6.86 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.0564× (z -9.2) |
| [[SW480 (line)]] | alt | 7.72 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0850× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.144× (z -10.1) |
| [[A549 (line)]] | wt | 7.58 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0592× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[C-33 A (line)]] | alt | 7.52 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 0.0421× (z -10.1) ⚠ cell-cycle shift, explains ~30% of this change |
| [[C32 (line)]] | wt | 9.53 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0710× (z -10.7) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 9.00 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0349× (z -12.1) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 13.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.109× (z -9.3) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 6.50 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0812× (z -8.7) |
| [[SNU-423 (line)]] | alt | 8.17 | 0 | 1 | — | [[Hesperidin (drug)]] 5 µM 0.0762× (z -9.3) |
| [[SW 900 (line)]] | alt | 6.03 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0344× (z -10.7) |
| [[A-427 (line)]] | wt | 8.02 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.21 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.93 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.37 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.44 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.32 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.85 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.73 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.50 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4587), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF594]] | +0.59 | +0.70 / +0.42 | both halves | 4e-05 |  |
| [[ZNF302]] | +0.58 | +0.65 / +0.47 | both halves | 2e-05 |  |
| [[ZNF181]] | +0.58 | +0.68 / +0.43 | both halves | 3e-05 |  |
| [[TMEM9B-AS1]] | +0.58 | +0.62 / +0.41 | both halves | 4e-05 |  |
| [[POLL]] | +0.57 | +0.43 / +0.66 | both halves | 3e-05 |  |
| [[ATE1OSP]] | +0.57 | +0.63 / +0.60 | both halves | 7e-06 | same gene group |
| [[ANKRD49]] | +0.56 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[YJU2B]] | +0.56 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[ZNF585B]] | +0.56 | +0.59 / +0.42 | both halves | 4e-05 |  |
| [[LINC02256]] | +0.56 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[ACTG1P17]] | +0.55 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[NPIPB2]] | +0.55 | +0.59 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRPS2]] | -0.53 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[PRKAR2B]] | -0.53 | -0.38 / -0.43 | both halves | 7e-05 |  |
| [[RAPGEF5]] | -0.52 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[PPAT]] | -0.52 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[UGT8]] | -0.52 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[TBC1D4]] | -0.51 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[MGAT4A]] | -0.51 | -0.55 / -0.40 | both halves | 5e-05 |  |
| [[STT3B]] | -0.51 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[MGAT5]] | -0.50 | -0.58 / -0.39 | both halves | 5e-05 |  |
| [[CPOX]] | -0.49 | -0.62 / -0.28 | both halves | 3e-04 |  |
| [[VPS13A]] | -0.48 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[CDCA7L]] | -0.48 | -0.39 / -0.47 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RAPGEF5]] | B | RAPGEF5 activity lowers FBXL9P's level | lines that do not express RAPGEF5 (17) vs lines expressing it (33) | 1.51× higher at baseline in the lines without RAPGEF5 | 0.039 | ⚠ within organs, on part of the lines; also absent: HSH2D, HOOK1, SAMD12; maybe low, not absent |
| [[ZNF594]] | B | ZNF594 activity raises FBXL9P's level | lines that do not express ZNF594 (6) vs lines expressing it (44) | 1.70× lower at baseline in the lines without ZNF594 | 0.090 | ⚠ within organs, on part of the lines; co-occurs with NF1; also absent: ZNF594-DT, MIR3659HG, SYNGR1 |
| [[DET1]] | C | DET1's natural level strengthens FBXL9P's drug response | DET1's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.64, reverse +0.14; direction not clear | 0.073 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 089]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.539). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-41.2, 8.8); signed map (-1.7, -14.4). **Vector** length 57.5, 8.66% of its response variance represented; |z| ≥ 3 in 1,030 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | +2.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.5 | +2.4 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.4 | +2.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.3 | +1.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.3 | -0.2 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.2 | +1.6 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +1.1 | +1.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.0 | -2.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.7 | -9.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change | -2.7 | -4.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.7 | +0.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | +0.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | -0.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.7 | -3.8 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.4 | -2.5 |
|  | [[Fluvoxamine (maleate) (drug)]] 0.5 µM |  | -1.2 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | F-box and leucine rich repeat protein 9, pseudogene |
| Locus type | pseudogene |
| Location | 16q22.1 — chr16:67,207,605-67,226,998 (-) |
| Ensembl biotype | transcribed_unitary_pseudogene |
| Also known as | FBL9; previously FBXL9, LRRC29 |
| Gene groups (HGNC) | F-box and leucine rich repeat proteins; Unitary pseudogenes |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [26231](https://www.ncbi.nlm.nih.gov/gene/26231):

> This gene encodes a member of the F-box protein family which is characterized by an approximately 40 amino acid motif, the F-box. The F-box proteins constitute one of the four subunits of ubiquitin protein ligase complex called SCFs (SKP1-cullin-F-box), which function in phosphorylation-dependent ubiquitination. The F-box proteins are divided into 3 classes: Fbws containing WD-40 domains, Fbls containing leucine-rich repeats, and Fbxs containing either different protein-protein interaction …

**Accessions** — [HGNC:13605](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13605) · Entrez [26231](https://www.ncbi.nlm.nih.gov/gene/26231) · Ensembl [ENSG00000125122](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125122)

## Data

Gene col 4587: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4587); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4587, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4587]; `tensor/DDL_lfc|DDL_z.npy` [4587]; `embed/gene_vectors.npy` [4587]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4587 or target_col == 4587). Every well: [[FBXL9P — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBXL9P.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
