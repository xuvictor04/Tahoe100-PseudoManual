---
symbol: "NIT2"
type: "gene"
col: 3516
ensembl_id: "ENSG00000114021"
name: "nitrilase family member 2"
location: "3q12.2"
module: 4
arm: "+"
pooled_cpm: 18.55
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 14
n_dd_up_clean: 8
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# NIT2

*nitrilase family member 2* — 3q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.41× (z +16.4, q 0e+00, up in 31 of 40 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.73× (z +10.2, q 3e-22, up in 37 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.554× (z -15.5, q 0e+00, down in 34 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMA1]] (+0.65, fdr 1e-05), [[GPN1]] (+0.65, fdr 7e-06), [[TMX3]] (+0.65, fdr 7e-06); moves opposite to [[PURA]] (-0.60, fdr 1e-05), [[INAFM1]] (-0.60, fdr 1e-05), [[CDKN2D]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[GDPD4]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[ERK5-IN-2 (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3516.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.41×** | +16.4 | 0e+00 | 31/40 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.48×** | +16.3 | 0e+00 | 28/29 (LoVo, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.10×** | +12.8 | 3e-35 | 32/36 (A549, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.73×** | +10.2 | 3e-22 | 37/47 (HOP62, COLO 205, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.56×** | +8.3 | 2e-14 | 28/47 (COLO 205, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.54×** | +7.6 | 2e-12 | 30/48 (NCI-H23, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.20×** | +4.8 | 1e-04 | 19/48 (Hs 766T, HS-578T, …) | top dose only | low cells (technical?) |
| [[Belumosudil (drug)]] 5 µM |  | **1.27×** | +4.3 | 0.001 | 15/47 (NCI-H23, NCI-H1792, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.27×** | +4.1 | 0.002 | 17/45 (SK-MEL-2, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.25×** | +4.1 | 0.002 | 14/44 (BT-474, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.21×** | +3.5 | 0.022 | 11/47 (NCI-H1573, HS-578T, …) | two highest doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.30×** | +3.5 | 0.026 | 14/44 (PANC-1, A-172, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | 1.20× | +3.4 | 0.033 | 7/48 (RPMI-7951, J82, …) | rises with dose |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.40×** | +3.3 | 0.038 | 9/44 (Hs 766T, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 1.19× | +3.3 | 0.038 | 7/45 (SHP-77, NCI-H23, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 1 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3516.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.554×** | -15.5 | 0e+00 | 34/47 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.620×** | -8.9 | 1e-16 | 28/46 (LoVo, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.630×** | -8.6 | 1e-15 | 31/48 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.697×** | -6.7 | 2e-09 | 24/47 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.698×** | -6.7 | 2e-09 | 26/47 (A-427, A-172, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.707×** | -6.5 | 1e-08 | 27/48 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.709×** | -6.2 | 6e-08 | 22/47 (H4, A-172, …) | top dose only | cell-cycle shift (explains ~13% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.727×** | -5.9 | 2e-07 | 20/47 (SK-MEL-2, A-172, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.729×** | -5.9 | 2e-07 | 19/47 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.757×** | -5.2 | 1e-05 | 22/47 (MIA PaCa-2, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.628×** | -4.5 | 3e-04 | 13/48 (RKO, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.808×** | -4.0 | 0.004 | 20/48 (HEC-1-A, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.688×** | -3.6 | 0.012 | 8/48 (SNU-1, J82, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.716×** | -3.3 | 0.047 | 12/44 (Hs 766T, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Lidocaine (hydrochloride) (drug)]] 0.5 µM |  | 0.844× | -3.2 | 0.060 | 10/45 (HT-29, Panc 03.27, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3516. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 20.3 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.95× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -9.1) |
| [[LoVo (line)]] | wt | 15.1 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.82× (z +10.4) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.111× (z -17.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 25.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.288× (z -10.7) |
| [[A-427 (line)]] | wt | 54.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.202× (z -16.1) |
| [[HepG2_C3A (line)]] | wt | 11.3 | 0 | 2 | — | [[Talc (drug)]] 0.5 µM 0.0655× (z -10.6) |
| [[NCI-H460 (line)]] | wt | 15.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.45× (z +10.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.463× (z -9.4) |
| [[PANC-1 (line)]] | alt | 30.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.20× (z +12.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -12.3) |
| [[RKO (line)]] | wt | 24.9 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.291× (z -11.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.380× (z -9.2) |
| [[SW480 (line)]] | alt | 15.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.82× (z +8.8) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 21.8 | 0 | 1 | — | [[LY-2584702 (tosylate salt) (drug)]] 0.05 µM 0.0716× (z -8.7) |
| [[H4 (line)]] | wt | 18.6 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.117× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 24.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.448× (z -10.7) |
| [[HT-29 (line)]] | alt | 14.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.82× (z +9.3) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 27.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -11.9) |
| [[KATO III (line)]] | alt | 20.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.48× (z +10.7) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 12.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.154× (z -10.9) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 22.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -16.0) |
| [[NCI-H1573 (line)]] | alt | 13.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.12× (z +9.7) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 26.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -10.4) |
| [[Panc 03.27 (line)]] | alt | 17.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -11.3) |
| [[RPMI-7951 (line)]] | alt | 15.7 | 0 | 1 | — | [[Elagolix sodium (drug)]] 0.5 µM 0.117× (z -11.4) |
| [[SW 900 (line)]] | alt | 9.68 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.130× (z -9.1) |
| [[A498 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.40 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.60 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 27.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3516), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMA1]] | +0.65 | +0.73 / +0.54 | both halves | 1e-05 |  |
| [[GPN1]] | +0.65 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[TMX3]] | +0.65 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[FECH]] | +0.64 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[UBQLN1]] | +0.63 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[CLPB]] | +0.63 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[CCT3]] | +0.63 | +0.73 / +0.53 | both halves | 1e-05 |  |
| [[DPP3]] | +0.63 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[CCT7]] | +0.63 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[ELAC2]] | +0.62 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[B3GALNT1]] | +0.62 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[PSMB2]] | +0.62 | +0.68 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PURA]] | -0.60 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[INAFM1]] | -0.60 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[CDKN2D]] | -0.58 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[S100A1]] | -0.56 | -0.30 / -0.52 | both halves | 2e-04 |  |
| [[ING2]] | -0.56 | -0.42 / -0.60 | both halves | 4e-05 |  |
| [[ARID4A]] | -0.55 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[GPX4]] | -0.54 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[MINDY2]] | -0.53 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[PLAG1]] | -0.53 | -0.60 / -0.36 | both halves | 9e-05 |  |
| [[MIDN]] | -0.53 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[TNRC6C]] | -0.53 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[ZBTB7A]] | -0.53 | -0.46 / -0.54 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GDPD4]] | B | GDPD4 activity lowers NIT2's level | lines that do not express GDPD4 (32) vs lines expressing it (18) | 1.30× higher at baseline in the lines without GDPD4 | 0.085 | ⚠ within organs, on part of the lines; also absent: STEAP4, ENSG00000275016, DDX43; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[ERK5-IN-2 (drug)]] 0.5 µM | C | NIT2's natural level lowers the cells' numbers under ERK5-IN-2 0.5 µM (makes them more sensitive) | NIT2's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.57 | 0.510 over the table, 0.093 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.597). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-24.0, -31.0); signed map (-13.1, -43.9). **Vector** length 80.6, 15.3% of its response variance represented; |z| ≥ 3 in 962 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Folding of actin by CCT/TriC* (reactome, mean cos +0.56 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +7.4 | +8.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +7.0 | +7.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.8 | +10.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.7 | +16.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.5 | +16.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.8 | +1.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.7 | +0.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.0 | +1.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.8 | +1.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -3.6 | -15.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.9 | -8.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.1 | -6.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.1 | -5.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -1.7 | -6.2 |
|  | [[Azithromycin (hydrate) (drug)]] 5 µM |  | -1.3 | -0.1 |
|  | [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | -1.2 | -1.8 |
|  | [[HI-TOPK-032 (drug)]] 0.5 µM |  | -1.2 | -1.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.2 | -1.3 |
|  | [[EX229 (drug)]] 0.5 µM |  | -1.2 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | nitrilase family member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q12.2 — chr3:100,334,739-100,361,635 (+) |
| Ensembl biotype | protein_coding |
| Reactome | 2 pathways, smallest: Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NQR4](https://www.uniprot.org/uniprotkb/Q9NQR4) (Omega-amidase NIT2):

> Has omega-amidase activity. The role of omega-amidase is to remove potentially toxic intermediates by converting 2-oxoglutaramate and 2-oxosuccinamate to biologically useful 2-oxoglutarate and oxaloacetate, respectively.

**Summary**, from NCBI Gene [56954](https://www.ncbi.nlm.nih.gov/gene/56954):

> Enables omega-amidase activity. Involved in L-glutamine metabolic process; asparagine metabolic process; and oxaloacetate metabolic process. Located in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29878](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29878) · Entrez [56954](https://www.ncbi.nlm.nih.gov/gene/56954) · UniProt [Q9NQR4](https://www.uniprot.org/uniprotkb/Q9NQR4) · Ensembl [ENSG00000114021](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114021)

## Data

Gene col 3516: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3516); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3516, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3516]; `tensor/DDL_lfc|DDL_z.npy` [3516]; `embed/gene_vectors.npy` [3516]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3516 or target_col == 3516). Every well: [[NIT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NIT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
