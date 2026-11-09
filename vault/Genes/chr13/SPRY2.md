---
symbol: "SPRY2"
type: "gene"
col: 5826
ensembl_id: "ENSG00000136158"
name: "sprouty RTK signaling antagonist 2"
location: "13q31.1"
module: 92
arm: "+"
pooled_cpm: 19.6
n_lines_expressing: 48
n_dd_up: 15
n_dd_down: 42
n_dd_up_clean: 5
n_dd_down_clean: 34
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/092"]
generated_by: "tahoemap"
---

# SPRY2

*sprouty RTK signaling antagonist 2* — 13q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (10 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 1.81× (z +9.0, q 2e-16, up in 27 of 46 measured lines) ⚠ cell-cycle shift, explains ~40% of this change. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 3.21× (z +7.3, q 4e-11, up in 31 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 42 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.309× (z -18.2, q 0e+00, down in 42 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPRY4]] (+0.79, fdr 7e-06), [[SPRED1]] (+0.76, fdr 7e-06), [[PHLDA1]] (+0.74, fdr 7e-06); moves opposite to [[NPEPPS]] (-0.60, fdr 1e-05), [[KIF13A]] (-0.54, fdr 2e-05), [[STK38]] (-0.53, fdr 3e-05).
> It is in [[Module 092]], a single-armed module (MAPK output).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 10 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5826.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.81×** | +9.0 | 2e-16 | 27/46 (NCI-H460, C32, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.74×** | +8.7 | 9e-16 | 32/45 (NCI-H460, HOP62, …) | two highest doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **3.21×** | +7.3 | 4e-11 | 31/44 (SNU-1, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.36×** | +6.9 | 6e-10 | 22/46 (NCI-H460, C32, …) | two highest doses | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.98×** | +6.9 | 6e-10 | 25/46 (C32, SK-MEL-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.46×** | +6.0 | 2e-07 | 24/46 (SNU-1, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~23% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.46×** | +5.9 | 3e-07 | 21/46 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.45×** | +5.4 | 6e-06 | 15/35 (SK-MEL-2, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.32×** | +4.4 | 8e-04 | 21/45 (SNU-1, NCI-H2030, …) | all doses, flat |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.83×** | +3.8 | 0.008 | 9/27 (NCI-H2030, SNU-1, …) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.28×** | +3.7 | 0.010 | 14/43 (NCI-H460, SNU-423, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~87% of this change | **1.25×** | +3.5 | 0.022 | 15/44 (RPMI-7951, HCT15, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **1.23×** | +3.3 | 0.041 | 19/44 (J82, Hs 766T, …) | all doses, flat | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.22×** | +3.2 | 0.058 | 10/45 (NCI-H460, SNU-423, …) | all doses, flat | position effect removed |
| [[Naproxen (drug)]] 5 µM |  | **1.22×** | +3.1 | 0.071 | 5/44 (AsPC-1, MIA PaCa-2, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 42 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5826.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.309×** | -18.2 | 0e+00 | 42/46 (MIA PaCa-2, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.311×** | -18.0 | 0e+00 | 41/46 (LS 180, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.349×** | -15.7 | 0e+00 | 42/46 (C32, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.386×** | -14.7 | 0e+00 | 38/45 (LS 180, SW 900, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.466×** | -14.5 | 1e-45 | 41/46 (MIA PaCa-2, C32, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.415×** | -13.1 | 5e-37 | 40/45 (C32, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.465×** | -11.8 | 3e-30 | 38/46 (MIA PaCa-2, NCI-H23, …) | all doses, flat | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.467×** | -11.3 | 8e-28 | 34/45 (MIA PaCa-2, HS-578T, …) | all doses, flat | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.806×** | -11.1 | 1e-26 | 30/46 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.481×** | -10.7 | 6e-25 | 40/46 (C32, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.482×** | -10.4 | 1e-23 | 37/46 (MIA PaCa-2, C32, …) | all doses, flat | position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.598×** | -9.6 | 3e-20 | 29/46 (MIA PaCa-2, C32, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.638×** | -9.6 | 3e-20 | 36/46 (C32, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.553×** | -9.1 | 3e-18 | 31/45 (C32, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.662×** | -8.9 | 1e-17 | 24/45 (MIA PaCa-2, C32, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.591×** | -7.8 | 2e-13 | 26/44 (MIA PaCa-2, A-172, …) | rises with dose | cell-cycle shift (explains ~18% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, +0.50 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5826. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 37.1 | 4 (3 ⚠) | 14 | [[Harringtonine (drug)]] 0.5 µM 7.05× (z +11.7) | [[Cobimetinib (drug)]] 5 µM 0.0154× (z -23.9) |
| [[MIA PaCa-2 (line)]] | alt | 77.4 | 0 | 18 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.391× (z -27.6) ⚠ position not correctable · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.115× (z -26.0) |
| [[NCI-H460 (line)]] | wt | 19.6 | 5 (3 ⚠) | 12 | [[Harringtonine (drug)]] 0.5 µM 8.18× (z +16.3) | [[Trametinib (drug)]] 5 µM 0.226× (z -11.5) |
| [[SK-MEL-2 (line)]] | alt | 16.4 | 1 (1 ⚠) | 9 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 9.95× (z +11.0) ⚠ toxic; transcription drop | [[Trametinib (drug)]] 0.5 µM 0.146× (z -12.8) |
| [[SNU-1 (line)]] | wt | 146 | 1 | 9 (2 ⚠) | [[Harringtonine (drug)]] 0.5 µM 3.04× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.120× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.223× (z -11.8) |
| [[HOP62 (line)]] | alt | 27.4 | 1 (1 ⚠) | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 4.69× (z +10.7) ⚠ cell-cycle shift, explains ~32% of this change | [[Adagrasib (drug)]] 0.05 µM 0.411× (z -21.6) ⚠ position not correctable · without an alert: [[Panobinostat (drug)]] 5 µM 0.160× (z -12.6) |
| [[SW480 (line)]] | alt | 27.8 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.213× (z -12.5) |
| [[AN3 CA (line)]] | alt | 96.9 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.141× (z -10.1) |
| [[AsPC-1 (line)]] | alt | 25.2 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.161× (z -10.0) |
| [[LS 180 (line)]] | wt | 32.6 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.153× (z -14.3) |
| [[NCI-H23 (line)]] | alt | 12.5 | 0 | 3 (1 ⚠) | — | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.0818× (z -11.8) |
| [[CHP-212 (line)]] | wt | 61.4 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.112× (z -10.0) |
| [[COLO 205 (line)]] | alt | 17.5 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.08× (z +9.7) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[HEC-1-A (line)]] | alt | 15.8 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.193× (z -10.6) |
| [[J82 (line)]] | alt | 12.7 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +9.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[LOX-IMVI (line)]] | wt | 25.2 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.156× (z -10.4) |
| [[PANC-1 (line)]] | alt | 14.7 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.223× (z -9.8) |
| [[A-172 (line)]] | wt | 9.25 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.119× (z -10.5) |
| [[A549 (line)]] | wt | 8.27 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.35× (z +8.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[H4 (line)]] | wt | 16.5 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0288× (z -14.1) |
| [[HS-578T (line)]] | alt | 13.2 | 0 | 1 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0745× (z -11.2) |
| [[KATO III (line)]] | alt | 15.7 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.242× (z -8.6) |
| [[LoVo (line)]] | wt | 18.6 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.260× (z -9.1) |
| [[NCI-H1573 (line)]] | alt | 17.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 13.4 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.600× (z -8.9) ⚠ position not correctable |
| [[NCI-H2030 (line)]] | alt | 13.5 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.542× (z -11.6) ⚠ position not correctable |
| [[RPMI-7951 (line)]] | alt | 16.4 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.124× (z -10.4) |
| [[SW 900 (line)]] | alt | 27.9 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.136× (z -11.4) |
| [[SW1417 (line)]] | alt | 7.88 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0720× (z -11.4) |
| [[SW48 (line)]] | wt | 16.8 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.108× (z -8.9) |
| [[A-427 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.89 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.02 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.40 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.75 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.15 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.73 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5826), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPRY4]] | +0.79 | +0.76 / +0.81 | both halves | 7e-06 | same gene group; STRING 625 |
| [[SPRED1]] | +0.76 | +0.76 / +0.73 | both halves | 7e-06 | pathway: Signaling by FGFR; STRING 554 |
| [[PHLDA1]] | +0.74 | +0.72 / +0.74 | both halves | 7e-06 | STRING 691 |
| [[DUSP6]] | +0.71 | +0.75 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_KRAS_SIGNALING_UP; STRING 829 |
| [[SPRY4-AS1]] | +0.69 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[MCL1]] | +0.68 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[EGR3]] | +0.68 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[LINC02454]] | +0.68 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[HMGA2]] | +0.67 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[DUSP4]] | +0.67 | +0.67 / +0.67 | both halves | 7e-06 | STRING 567 |
| [[FJX1]] | +0.67 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[EGR1]] | +0.66 | +0.69 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPEPPS]] | -0.60 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[KIF13A]] | -0.54 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[STK38]] | -0.53 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[WWP1]] | -0.52 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[ADD1]] | -0.51 | -0.53 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 092]] — MAPK output; 49 genes; every member is in the + arm (projection on the module's main direction 0.807). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (43.9, 7.1); signed map (9.4, 47.2). **Vector** length 107, 27.4% of its response variance represented; |z| ≥ 3 in 1,404 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Pre-NOTCH Expression and Processing* (reactome, mean cos +0.50 to 5); *MAPK family signaling cascades* (reactome, mean cos +0.63 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +6.5 | +8.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +6.2 | +9.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.6 | +6.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.2 | +5.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.7 | +6.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.0 | +2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | -1.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | -1.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | +7.3 |
|  | [[Belzutifan (drug)]] 5 µM |  | +2.3 | +2.7 |
| fall | [[Trametinib (drug)]] 5 µM |  | -8.2 | -15.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -7.3 | -14.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -7.2 | -10.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -7.0 | -11.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -6.7 | -13.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -6.6 | -11.3 |

## What is on record

|  |  |
|---|---|
| Name | sprouty RTK signaling antagonist 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q31.1 — chr13:80,335,976-80,341,126 (-) |
| Ensembl biotype | protein_coding |
| Also known as | hSPRY2 |
| Gene groups (HGNC) | Sprouty RTK signaling antagonist family |
| Hallmark sets | KRAS_SIGNALING_UP |
| Reactome | 13 pathways, smallest: Spry regulation of FGF signaling; Negative regulation of FGFR1 signaling; Negative regulation of FGFR2 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [O43597](https://www.uniprot.org/uniprotkb/O43597) (Protein sprouty homolog 2):

> Antagonist of fibroblast growth factor (FGF) pathways via inhibition of FGF-mediated phosphorylation of ERK1/2 (By similarity). Thereby acts as an antagonist of FGF-induced retinal lens fiber differentiation, may inhibit limb bud outgrowth and may negatively modulate respiratory organogenesis (By similarity). Inhibits TGFB-induced epithelial-to-mesenchymal transition in retinal lens epithelial cells (By similarity). Inhibits CBL/C-CBL-mediated EGFR ubiquitination.

**Summary**, from NCBI Gene [10253](https://www.ncbi.nlm.nih.gov/gene/10253):

> This gene encodes a protein belonging to the sprouty family. The encoded protein contains a carboxyl-terminal cysteine-rich domain essential for the inhibitory activity on receptor tyrosine kinase signaling proteins and is required for growth factor stimulated translocation of the protein to membrane ruffles. In primary dermal endothelial cells this gene is transiently upregulated in response to fibroblast growth factor two. This protein is indirectly involved in the non-cell autonomous …

**Accessions** — [HGNC:11270](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11270) · Entrez [10253](https://www.ncbi.nlm.nih.gov/gene/10253) · UniProt [O43597](https://www.uniprot.org/uniprotkb/O43597) · Ensembl [ENSG00000136158](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136158)

## Data

Gene col 5826: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5826); `tables/drug_effects.parquet` (60 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5826, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5826]; `tensor/DDL_lfc|DDL_z.npy` [5826]; `embed/gene_vectors.npy` [5826]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5826 or target_col == 5826). Every well: [[SPRY2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPRY2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
