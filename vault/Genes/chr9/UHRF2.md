---
symbol: "UHRF2"
type: "gene"
col: 7226
ensembl_id: "ENSG00000147854"
name: "ubiquitin like with PHD and ring finger domains 2"
location: "9p24.1"
module: 84
arm: "+"
pooled_cpm: 98.62
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 23
n_dd_up_clean: 3
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/084"]
generated_by: "tahoemap"
---

# UHRF2

*ubiquitin like with PHD and ring finger domains 2* — 9p24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.40× (z +10.2, q 2e-21, up in 44 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.333× (z -23.4, q 0e+00, down in 40 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.744× (z -9.2, q 4e-18, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CEP170]] (+0.63, fdr 1e-05), [[PPP2R3B]] (+0.60, fdr 1e-05), [[FOXJ3]] (+0.60, fdr 3e-05); moves opposite to [[FBXW10B]] (-0.58, fdr 2e-05), [[DIO2]] (-0.56, fdr 3e-05), [[ABCC2]] (-0.55, fdr 2e-05).
> It is in [[Module 084]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7226.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.40×** | +10.2 | 2e-21 | 44/49 (SW480, C32, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.13×** | +8.8 | 5e-16 | 38/48 (C32, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.23×** | +4.7 | 5e-04 | 21/48 (LS 180, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.22×** | +4.2 | 0.004 | 24/47 (LoVo, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 14 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7226.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.333×** | -23.4 | 0e+00 | 40/44 (A-172, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.398×** | -20.3 | 0e+00 | 45/49 (A-427, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.544×** | -12.4 | 3e-33 | 34/45 (A-172, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.744×** | -9.2 | 4e-18 | 29/48 (NCI-H23, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.698×** | -7.9 | 3e-13 | 34/48 (A-427, HEC-1-A, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.693×** | -7.8 | 6e-13 | 34/47 (MIA PaCa-2, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.805×** | -6.8 | 1e-09 | 26/49 (MIA PaCa-2, A549, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.776×** | -5.6 | 2e-06 | 30/48 (C32, PANC-1, …) | two highest doses |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.801×** | -5.0 | 4e-05 | 25/49 (A-427, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.791×** | -5.0 | 4e-05 | 27/47 (A-427, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.798×** | -4.7 | 1e-04 | 26/48 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.942× | -4.6 | 2e-04 | 4/50 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.811×** | -4.6 | 2e-04 | 24/48 (MIA PaCa-2, HS-578T, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.865× | -4.3 | 6e-04 | 17/49 (MIA PaCa-2, Hs 766T, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.826×** | -4.2 | 0.001 | 22/48 (C32, PANC-1, …) | two highest doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.825×** | -4.1 | 0.002 | 18/48 (A-172, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.826×** | -4.0 | 0.002 | 24/48 (Hs 766T, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.833×** | -4.0 | 0.002 | 20/47 (MIA PaCa-2, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.880× | -3.8 | 0.004 | 16/48 (MIA PaCa-2, A-427, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.851× | -3.8 | 0.004 | 18/48 (Hs 766T, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.842× | -3.7 | 0.005 | 21/48 (Hs 766T, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Thymol (drug)]] 5 µM |  | 0.887× | -3.7 | 0.005 | 11/48 (KATO III, CHP-212, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.734×** | -3.6 | 0.008 | 17/48 (SW1417, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.739×** | -3.5 | 0.011 | 16/48 (MIA PaCa-2, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7226. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 243 | 0 | 17 (9 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.567× (z -24.7) ⚠ position not correctable · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.467× (z -13.4) |
| [[Hs 766T (line)]] | wt | 194 | 0 | 9 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.319× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.493× (z -10.7) |
| [[A-172 (line)]] | wt | 93.0 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.157× (z -22.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.428× (z -15.0) |
| [[C32 (line)]] | wt | 111 | 2 | 5 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 10.8× (z +13.3) | [[Dinaciclib (drug)]] 5 µM 0.160× (z -18.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.358× (z -11.0) |
| [[SW480 (line)]] | alt | 104 | 2 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.05× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.309× (z -17.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.576× (z -8.6) |
| [[A-427 (line)]] | wt | 105 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0491× (z -35.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.368× (z -11.6) |
| [[CFPAC-1 (line)]] | alt | 91.5 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.405× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.588× (z -9.4) |
| [[HS-578T (line)]] | alt | 108 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.286× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.526× (z -11.2) |
| [[J82 (line)]] | alt | 162 | 1 (1 ⚠) | 4 (3 ⚠) | [[Selinexor (drug)]] 5 µM 1.53× (z +8.6) ⚠ cell-cycle shift, explains ~11% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.231× (z -20.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.537× (z -12.3) |
| [[SNU-423 (line)]] | alt | 106 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.268× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.537× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 101 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.267× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.375× (z -11.3) |
| [[HOP62 (line)]] | alt | 105 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -14.9) |
| [[KATO III (line)]] | alt | 77.1 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.16× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.385× (z -11.3) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 142 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.11× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.319× (z -14.2) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 141 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.211× (z -17.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.423× (z -14.6) |
| [[A498 (line)]] | wt | 124 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.274× (z -14.9) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 164 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.192× (z -18.6) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 130 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.257× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.436× (z -10.8) |
| [[Panc 03.27 (line)]] | alt | 136 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.308× (z -13.6) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 79.7 | 1 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 8.42× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.0901× (z -18.5) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 113 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.284× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.399× (z -9.2) |
| [[LS 180 (line)]] | wt | 112 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.75× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.398× (z -9.9) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 86.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.238× (z -13.8) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 60.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -15.9) |
| [[NCI-H460 (line)]] | wt | 93.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.345× (z -13.3) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 54.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.414× (z -11.8) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 103 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.247× (z -8.6) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 64.2 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.97× (z +8.5) | — |
| [[H4 (line)]] | wt | 75.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.144× (z -14.8) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 87.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.284× (z -11.3) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 62.8 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.389× (z -9.5) |
| [[LoVo (line)]] | wt | 87.1 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 1.86× (z +8.7) ⚠ toxic | — |
| [[NCI-H1792 (line)]] | alt | 53.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -10.8) |
| [[NCI-H2347 (line)]] | alt | 41.8 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.558× (z -8.9) ⚠ cell-cycle shift, explains ~14% of this change |
| [[RPMI-7951 (line)]] | alt | 96.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.341× (z -9.7) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 85.7 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.185× (z -10.4) ⚠ toxic |
| [[SW 900 (line)]] | alt | 94.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.327× (z -10.5) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 76.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.338× (z -11.7) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 54.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 118 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 97.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 96.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 79.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 97.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 103 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 86.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 63.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7226), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEP170]] | +0.63 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[PPP2R3B]] | +0.60 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[FOXJ3]] | +0.60 | +0.69 / +0.45 | both halves | 3e-05 |  |
| [[MMS19]] | +0.57 | +0.65 / +0.42 | both halves | 4e-05 |  |
| [[ETV5]] | +0.56 | +0.61 / +0.39 | both halves | 5e-05 |  |
| [[MTMR12]] | +0.56 | +0.62 / +0.40 | both halves | 5e-05 |  |
| [[CSNK1E]] | +0.55 | +0.66 / +0.38 | both halves | 6e-05 |  |
| [[SNU13]] | +0.55 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[ANKRD13D]] | +0.55 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[CLEC2B]] | +0.55 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[MAP2K1]] | +0.55 | +0.64 / +0.36 | both halves | 1e-04 |  |
| [[POGLUT2]] | +0.54 | +0.60 / +0.36 | both halves | 9e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXW10B]] | -0.58 | -0.58 / -0.46 | both halves | 2e-05 |  |
| [[DIO2]] | -0.56 | -0.63 / -0.44 | both halves | 3e-05 |  |
| [[ABCC2]] | -0.55 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[TENM3]] | -0.54 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[AKT1S1]] | -0.54 | -0.59 / -0.35 | both halves | 1e-04 |  |
| [[SLC9A8]] | -0.53 | -0.64 / -0.34 | both halves | 1e-04 |  |
| [[TENM3-AS1]] | -0.53 | -0.62 / -0.40 | both halves | 5e-05 |  |
| [[TRIM16L]] | -0.52 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[YIPF6]] | -0.52 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[RABL3]] | -0.52 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[FGF2]] | -0.51 | -0.55 / -0.36 | both halves | 9e-05 |  |
| [[CHD3]] | -0.51 | -0.51 / -0.32 | both halves | 2e-04 | same gene group; pathway: SUMO E3 ligases SUMOylate target proteins |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises UHRF2's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 5.0% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds |
| [[TENM3-AS1]] | B | TENM3-AS1 activity raises UHRF2's level | lines that do not express TENM3-AS1 (19) vs lines expressing it (31) | 1.17× lower at baseline in the lines without TENM3-AS1 | 0.081 | ⚠ within organs, on part of the lines; also absent: TENM3, LRCH2, FBXL7; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 084]]; 52 genes; every member is in the + arm (projection on the module's main direction 0.585). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (18.7, -14.6); signed map (-49.8, -16.2). **Vector** length 103, 29.6% of its response variance represented; |z| ≥ 3 in 1,140 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.4 | +2.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +3.5 | -3.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.4 | -1.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.8 | +8.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | -2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +1.1 |
|  | [[vincristine (drug)]] 0.5 µM |  | +2.0 | -0.0 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.9 | +0.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.8 | -1.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -8.5 | -9.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.0 | -7.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.1 | -2.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -5.0 | -5.0 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.6 | -2.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.4 | -3.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | -4.3 | -5.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.2 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin like with PHD and ring finger domains 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p24.1 — chr9:6,413,151-6,507,054 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RNF107, NIRF, URF2, MGC33463, TDRD23 |
| Gene groups (HGNC) | Ring finger proteins; PHD finger proteins; Tudor domain containing; RING finger E3 ubiquitin protein ligases |
| Reactome | 3 pathways, smallest: SUMOylation of transcription cofactors; SUMO E3 ligases SUMOylate target proteins; SUMOylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96PU4](https://www.uniprot.org/uniprotkb/Q96PU4) (E3 ubiquitin-protein ligase UHRF2):

> E3 ubiquitin ligase that plays important roles in DNA methylation, histone modifications, cell cycle and DNA repair. Acts as a specific reader for 5-hydroxymethylcytosine (5hmC) and thereby recruits various substrates to these sites to ubiquitinate them. This activity also allows the maintenance of 5mC levels at specific genomic loci and regulates neuron-related gene expression (By similarity). Participates in cell cycle regulation by ubiquitinating cyclins CCND1 and CCNE1 and thereby inducing …

**Summary**, from NCBI Gene [115426](https://www.ncbi.nlm.nih.gov/gene/115426):

> This gene encodes a nuclear protein which is involved in cell-cycle regulation. The encoded protein is a ubiquitin-ligase capable of ubiquinating PCNP (PEST-containing nuclear protein), and together they may play a role in tumorigenesis. The encoded protein contains an NIRF_N domain, a PHD finger, a set- and ring-associated (SRA) domain, and a RING finger domain and several of these domains have been shown to be essential for the regulation of cell proliferation. This protein may also have a …

**Accessions** — [HGNC:12557](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12557) · Entrez [115426](https://www.ncbi.nlm.nih.gov/gene/115426) · UniProt [Q96PU4](https://www.uniprot.org/uniprotkb/Q96PU4) · Ensembl [ENSG00000147854](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147854)

## Data

Gene col 7226: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7226); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7226, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7226]; `tensor/DDL_lfc|DDL_z.npy` [7226]; `embed/gene_vectors.npy` [7226]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7226 or target_col == 7226). Every well: [[UHRF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UHRF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
