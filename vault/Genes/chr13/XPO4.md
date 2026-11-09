---
symbol: "XPO4"
type: "gene"
col: 5395
ensembl_id: "ENSG00000132953"
name: "exportin 4"
location: "13q12.11"
module: 36
arm: "+"
pooled_cpm: 92.06
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 10
n_dd_up_clean: 9
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# XPO4

*exportin 4* — 13q12.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.53× (z +8.8, q 5e-16, up in 42 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 2.21× (z +8.0, q 2e-13, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.639× (z -8.7, q 3e-15, down in 34 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.782× (z -7.3, q 6e-11, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MDN1]] (+0.71, fdr 7e-06), [[WDR4]] (+0.70, fdr 1e-05), [[URB2]] (+0.70, fdr 7e-06); moves opposite to [[MXD1]] (-0.62, fdr 2e-05), [[SDCBP]] (-0.60, fdr 8e-06), [[BTG1]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5395.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.53×** | +8.8 | 5e-16 | 42/48 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.21×** | +8.0 | 2e-13 | 40/48 (SW480, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.46×** | +7.9 | 4e-13 | 34/48 (SHP-77, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.40×** | +6.9 | 5e-10 | 34/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.39×** | +6.9 | 6e-10 | 33/48 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.89×** | +6.5 | 9e-09 | 37/49 (SW480, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.36×** | +6.4 | 1e-08 | 30/48 (SHP-77, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.32×** | +5.7 | 8e-07 | 25/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.26×** | +4.7 | 2e-04 | 26/48 (LS 180, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.22×** | +3.9 | 0.005 | 21/48 (PANC-1, NCI-H460, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **1.40×** | +3.4 | 0.032 | 17/48 (NCI-H460, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.4 | 0.032 | 20/47 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.18× | +3.3 | 0.039 | 18/47 (NCI-H460, MIA PaCa-2, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.37×** | +3.2 | 0.064 | 16/48 (NCI-H460, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5395.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.639×** | -8.7 | 3e-15 | 34/45 (RKO, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.688×** | -7.5 | 1e-11 | 30/44 (C-33 A, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.782×** | -7.3 | 6e-11 | 34/48 (SW480, HOP62, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.720×** | -6.9 | 8e-10 | 31/49 (HCT15, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.819×** | -5.9 | 3e-07 | 22/49 (hTERT-HPNE, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.770×** | -5.5 | 4e-06 | 27/48 (SW1417, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~22% of this change | **0.791×** | -4.9 | 7e-05 | 27/48 (HOP62, LoVo, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.805×** | -4.6 | 4e-04 | 27/48 (SW1417, HOP62, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.808×** | -4.3 | 0.001 | 24/50 (HOP62, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.740×** | -4.1 | 0.003 | 28/47 (J82, H4, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | 0.837× | -3.7 | 0.009 | 23/48 (KATO III, LoVo, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 0.839× | -3.7 | 0.010 | 17/49 (SHP-77, SW480, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.848× | -3.3 | 0.037 | 17/47 (HOP62, HS-578T, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.861× | -3.2 | 0.066 | 18/48 (SW1417, A498, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5395. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 136 | 6 (1 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 1.94× (z +11.4) | — |
| [[HOP62 (line)]] | alt | 77.8 | 0 | 4 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.462× (z -10.6) |
| [[A498 (line)]] | wt | 99.8 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.351× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.593× (z -10.3) |
| [[C-33 A (line)]] | alt | 138 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0914× (z -25.7) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 98.5 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.09× (z +9.0) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.458× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.591× (z -9.7) |
| [[PANC-1 (line)]] | alt | 80.9 | 3 (2 ⚠) | 0 | [[Bortezomib (drug)]] 0.05 µM 2.13× (z +10.3) ⚠ cell-cycle shift, explains ~20% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 1.89× (z +9.2) | — |
| [[RKO (line)]] | wt | 156 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.240× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -8.8) |
| [[HCT15 (line)]] | alt | 92.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.263× (z -12.7) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 162 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.513× (z -9.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 108 | 1 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 3.80× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.591× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 64.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.292× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.586× (z -9.7) |
| [[NCI-H460 (line)]] | wt | 85.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.30× (z +11.7) ⚠ unreliable plate only | [[Dinaciclib (drug)]] 5 µM 0.478× (z -10.1) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 126 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.373× (z -11.4) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 120 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.61× (z +12.3) | — |
| [[SW48 (line)]] | wt | 137 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 3.12× (z +10.1) | [[Dinaciclib (drug)]] 0.05 µM 0.250× (z -12.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 82.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.25× (z +9.1) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 72.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +8.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[AsPC-1 (line)]] | alt | 56.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.516× (z -9.4) |
| [[C32 (line)]] | wt | 91.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.428× (z -8.5) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 162 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.37× (z +9.0) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 101 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.466× (z -8.7) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 108 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.03× (z +8.5) ⚠ unreliable plate only | — |
| [[hTERT-HPNE (line)]] | wt | 71.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.430× (z -10.6) |
| [[KATO III (line)]] | alt | 94.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.403× (z -9.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 94.1 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.67× (z +11.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 99.7 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.49× (z +9.5) ⚠ unreliable plate only | — |
| [[NCI-H1573 (line)]] | alt | 54.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.413× (z -9.6) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 68.2 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.199× (z -15.3) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SW 1271 (line)]] | alt | 93.0 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.0780× (z -12.2) |
| [[SW1417 (line)]] | alt | 101 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.468× (z -10.0) |
| [[A-172 (line)]] | wt | 62.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 125 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 66.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 92.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 61.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 65.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 61.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 76.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 91.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 168 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 64.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 140 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 65.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 92.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 75.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5395), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MDN1]] | +0.71 | +0.71 / +0.72 | both halves | 7e-06 |  |
| [[WDR4]] | +0.70 | +0.57 / +0.73 | both halves | 1e-05 |  |
| [[URB2]] | +0.70 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[MRPL3]] | +0.69 | +0.65 / +0.72 | both halves | 7e-06 |  |
| [[SRM]] | +0.69 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[DHX33]] | +0.69 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[DDX31]] | +0.68 | +0.52 / +0.71 | both halves | 1e-05 |  |
| [[POLR1A]] | +0.68 | +0.53 / +0.75 | both halves | 1e-05 |  |
| [[NOL9]] | +0.68 | +0.45 / +0.74 | both halves | 3e-05 |  |
| [[NOL10]] | +0.67 | +0.68 / +0.73 | both halves | 7e-06 |  |
| [[TOMM40]] | +0.67 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[CAD]] | +0.66 | +0.62 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MXD1]] | -0.62 | -0.47 / -0.63 | both halves | 2e-05 |  |
| [[SDCBP]] | -0.60 | -0.66 / -0.58 | both halves | 8e-06 |  |
| [[BTG1]] | -0.56 | -0.49 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises XPO4's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.674). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-13.2, -36.6); signed map (-4.3, -49.3). **Vector** length 89.9, 23.2% of its response variance represented; |z| ≥ 3 in 964 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.2 | +8.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.7 | +2.5 |
|  | [[EX229 (drug)]] 5 µM |  | +3.6 | +3.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.4 | +3.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.2 | +2.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.1 | +8.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.6 | +0.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.5 | -7.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~1% of this change | -4.3 | -3.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.2 | -1.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.0 | -5.9 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.5 | -3.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.3 | -1.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.9 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | exportin 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q12.11 — chr13:20,777,329-20,903,048 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13046, KIAA1721 |
| Gene groups (HGNC) | Exportins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9C0E2](https://www.uniprot.org/uniprotkb/Q9C0E2) (Exportin-4):

> Mediates the nuclear export of proteins (cargos), such as EIF5A, SMAD3 and isoform M2 of PKM (PKM2). In the nucleus binds cooperatively to its cargo and to the GTPase Ran in its active GTP-bound form. Docking of this trimeric complex to the nuclear pore complex (NPC) is mediated through binding to nucleoporins. Upon transit of a nuclear export complex into the cytoplasm, disassembling of the complex and hydrolysis of Ran-GTP to Ran-GDP (induced by RANBP1 and RANGAP1, respectively) cause release …

**Summary**, from NCBI Gene [64328](https://www.ncbi.nlm.nih.gov/gene/64328):

> XPO4 belongs to a large family of karyopherins (see MIM 602738) that mediate the transport of proteins and other cargo between the nuclear and cytoplasmic compartments (Lipowsky et al., 2000 [PubMed 10944119]).[supplied by OMIM, Mar 2009]

**Accessions** — [HGNC:17796](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17796) · Entrez [64328](https://www.ncbi.nlm.nih.gov/gene/64328) · UniProt [Q9C0E2](https://www.uniprot.org/uniprotkb/Q9C0E2) · Ensembl [ENSG00000132953](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132953)

## Data

Gene col 5395: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5395); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5395, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5395]; `tensor/DDL_lfc|DDL_z.npy` [5395]; `embed/gene_vectors.npy` [5395]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5395 or target_col == 5395). Every well: [[XPO4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/XPO4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
