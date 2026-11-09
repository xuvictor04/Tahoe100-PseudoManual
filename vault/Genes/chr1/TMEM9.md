---
symbol: "TMEM9"
type: "gene"
col: 3848
ensembl_id: "ENSG00000116857"
name: "transmembrane protein 9"
location: "1q32.1"
module: 45
arm: "+"
pooled_cpm: 20.41
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 15
n_dd_up_clean: 2
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# TMEM9

*transmembrane protein 9* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.32× (z +11.0, q 2e-25, up in 35 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.30× (z +4.9, q 1e-04, up in 19 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (A498 3.14×, NCI-H1573 6.26×, HEC-1-A 3.11×; ⚠ toxic; transcription drop); [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 1.53×; ⚠ position not correctable); [[Dinaciclib (drug)]] 5 µM in 1 line (A498 2.86×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.333× (z -20.4, q 0e+00, down in 45 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SCPEP1]] (+0.74, fdr 7e-06), [[ARL6]] (+0.67, fdr 3e-05), [[RAB3A]] (+0.67, fdr 1e-05); moves opposite to [[DGKH]] (-0.67, fdr 1e-05), [[CFAP161]] (-0.65, fdr 7e-06), [[GNG12-AS1]] (-0.64, fdr 2e-05).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PPP1R3C]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3848.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (A498 3.14×, NCI-H1573 6.26×, HEC-1-A 3.11×; ⚠ toxic; transcription drop); [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 1.53×; ⚠ position not correctable); [[Dinaciclib (drug)]] 5 µM in 1 line (A498 2.86×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.32×** | +11.0 | 2e-25 | 35/41 (A498, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.96×** | +8.4 | 8e-15 | 22/31 (A498, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.16× | +6.6 | 9e-09 | 11/48 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **1.30×** | +4.9 | 1e-04 | 19/48 (LoVo, SK-MEL-2, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.36×** | +4.1 | 0.006 | 21/46 (A-427, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~12% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.32×** | +3.3 | 0.082 | 15/36 (HEC-1-A, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.28×** | +3.2 | 0.094 | 10/47 (RPMI-7951, NCI-H460, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 1.19× | +3.2 | 0.094 | 12/48 (RKO, C32, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.28× | +3.0 | 0.14 | 10/47 (A-172, SW480, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3848.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.333×** | -20.4 | 0e+00 | 45/47 (SW 900, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.317×** | -15.0 | 0e+00 | 40/45 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.476×** | -9.7 | 5e-20 | 41/48 (SW 900, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.648×** | -8.1 | 1e-13 | 34/47 (SK-MEL-2, RKO, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.549×** | -7.9 | 4e-13 | 34/46 (SW48, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.544×** | -7.7 | 2e-12 | 38/48 (NCI-H2347, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.585×** | -7.0 | 2e-10 | 37/47 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.586×** | -7.0 | 2e-10 | 33/46 (SW 900, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.685×** | -5.0 | 4e-05 | 23/46 (SW 900, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.675×** | -4.9 | 4e-05 | 25/44 (A-427, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.691×** | -4.7 | 2e-04 | 24/46 (SW 900, C32, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.510×** | -4.6 | 2e-04 | 23/48 (SW 900, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.516×** | -4.5 | 3e-04 | 22/45 (HOP62, NCI-H2347, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.783×** | -3.2 | 0.054 | 11/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Sapanisertib (drug)]] 5 µM |  | **0.632×** | -3.1 | 0.063 | 8/48 (Hs 766T, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3848. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 28.0 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0483× (z -29.1) |
| [[A498 (line)]] | wt | 39.1 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.14× (z +10.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -11.4) |
| [[C32 (line)]] | wt | 48.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -15.3) |
| [[Hs 766T (line)]] | wt | 18.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -11.1) |
| [[MIA PaCa-2 (line)]] | alt | 17.5 | 1 (1 ⚠) | 2 | [[Adagrasib (drug)]] 0.05 µM 1.53× (z +9.0) ⚠ position not correctable | [[Homoharringtonine (drug)]] 0.5 µM 0.121× (z -13.5) |
| [[NCI-H2347 (line)]] | alt | 32.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -16.3) |
| [[NCI-H460 (line)]] | wt | 34.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -21.2) |
| [[RKO (line)]] | wt | 14.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0651× (z -14.7) |
| [[A-172 (line)]] | wt | 41.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -12.9) |
| [[A549 (line)]] | wt | 19.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -11.6) |
| [[H4 (line)]] | wt | 16.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -10.2) |
| [[HEC-1-A (line)]] | alt | 25.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.11× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.414× (z -10.0) |
| [[HOP62 (line)]] | alt | 20.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -15.1) |
| [[LoVo (line)]] | wt | 10.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -9.9) |
| [[NCI-H1573 (line)]] | alt | 16.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.26× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -9.1) |
| [[NCI-H2030 (line)]] | alt | 12.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -10.8) |
| [[PANC-1 (line)]] | alt | 12.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -11.3) |
| [[RPMI-7951 (line)]] | alt | 26.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -12.7) |
| [[SK-MEL-2 (line)]] | alt | 22.8 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.124× (z -19.0) |
| [[CFPAC-1 (line)]] | alt | 18.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -14.3) |
| [[HS-578T (line)]] | alt | 18.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -10.4) |
| [[HT-29 (line)]] | alt | 22.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -13.9) |
| [[J82 (line)]] | alt | 24.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -15.8) |
| [[LOX-IMVI (line)]] | wt | 11.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.181× (z -8.7) |
| [[NCI-H1792 (line)]] | alt | 15.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.279× (z -9.8) |
| [[NCI-H23 (line)]] | alt | 10.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -9.3) |
| [[SHP-77 (line)]] | alt | 23.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -8.6) |
| [[SNU-423 (line)]] | alt | 22.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -10.7) |
| [[SW480 (line)]] | alt | 13.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -11.5) |
| [[A-427 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 64.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.25 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3848), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCPEP1]] | +0.74 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[ARL6]] | +0.67 | +0.68 / +0.45 | both halves | 3e-05 |  |
| [[RAB3A]] | +0.67 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[SNAPC3]] | +0.67 | +0.71 / +0.54 | both halves | 1e-05 |  |
| [[CDON]] | +0.67 | +0.75 / +0.40 | both halves | 5e-05 |  |
| [[USP30]] | +0.66 | +0.70 / +0.52 | both halves | 1e-05 |  |
| [[BCL9]] | +0.66 | +0.70 / +0.55 | both halves | 1e-05 |  |
| [[VDAC3]] | +0.66 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[STARD3NL]] | +0.65 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[ALAD]] | +0.65 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[PDK3]] | +0.65 | +0.74 / +0.45 | both halves | 3e-05 |  |
| [[CAT]] | +0.65 | +0.65 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DGKH]] | -0.67 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[CFAP161]] | -0.65 | -0.68 / -0.61 | both halves | 7e-06 |  |
| [[GNG12-AS1]] | -0.64 | -0.62 / -0.47 | both halves | 2e-05 |  |
| [[TLNRD1]] | -0.63 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[ST7L]] | -0.61 | -0.69 / -0.36 | both halves | 9e-05 |  |
| [[MSRA]] | -0.61 | -0.63 / -0.43 | both halves | 3e-05 |  |
| [[WARS2-AS1]] | -0.61 | -0.64 / -0.37 | both halves | 8e-05 |  |
| [[MYH3]] | -0.60 | -0.69 / -0.43 | both halves | 3e-05 |  |
| [[ITPRIPL2]] | -0.60 | -0.61 / -0.38 | both halves | 6e-05 |  |
| [[KDSR]] | -0.59 | -0.57 / -0.40 | both halves | 5e-05 |  |
| [[ANKMY1]] | -0.59 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[SATB2]] | -0.58 | -0.49 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PPP1R3C]] | B | PPP1R3C activity raises TMEM9's level | lines that do not express PPP1R3C (22) vs lines expressing it (28) | 1.39× lower at baseline in the lines without PPP1R3C | 0.030 | ⚠ within organs, on part of the lines; also absent: CDH2, SSTR2, IDO1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.693). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (0.0, -8.4); signed map (-31.2, -7.1). **Vector** length 77.1, 15.9% of its response variance represented; |z| ≥ 3 in 891 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +5.6 | +4.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.8 | +3.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | -0.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | -0.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | -1.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.1 | +3.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.0 | +0.6 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +1.9 | +0.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +2.5 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +1.7 | +2.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.8 | -20.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.3 | -8.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.6 | -15.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.4 | -4.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.2 | -4.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.3 | -0.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.8 | -0.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.7 | -2.2 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | -1.6 | -1.6 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -1.6 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:201,134,772-201,171,574 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TMEM9A |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P0T7](https://www.uniprot.org/uniprotkb/Q9P0T7) (Proton-transporting V-type ATPase complex assembly regulator TMEM9):

> Transmembrane protein that binds to and facilitates the assembly of lysosomal proton-transporting V-type ATPase (v-ATPase), resulting in enhanced lysosomal acidification and trafficking. By bringing the v-ATPase accessory protein ATP6AP2 and the v-ATPase subunit ATP6V0D1 together, allows v-ATPase complex formation and activation. TMEM9-controlled vesicular acidification induces hyperactivation of Wnt/beta-catenin signaling, involved in development, tissue homeostasis and tissue regeneration, …

**Summary**, from NCBI Gene [252839](https://www.ncbi.nlm.nih.gov/gene/252839):

> Involved in intracellular pH reduction; positive regulation of canonical Wnt signaling pathway; and proton-transporting V-type ATPase complex assembly. Located in lysosomal membrane and multivesicular body membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:18823](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18823) · Entrez [252839](https://www.ncbi.nlm.nih.gov/gene/252839) · UniProt [Q9P0T7](https://www.uniprot.org/uniprotkb/Q9P0T7) · Ensembl [ENSG00000116857](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116857)

## Data

Gene col 3848: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3848); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3848, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3848]; `tensor/DDL_lfc|DDL_z.npy` [3848]; `embed/gene_vectors.npy` [3848]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3848 or target_col == 3848). Every well: [[TMEM9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
