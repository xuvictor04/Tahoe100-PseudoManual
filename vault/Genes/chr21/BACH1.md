---
symbol: "BACH1"
type: "gene"
col: 7967
ensembl_id: "ENSG00000156273"
name: "BACH transcriptional regulator 1"
location: "21q21.3"
module: 151
arm: "+"
pooled_cpm: 364.85
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 28
n_dd_up_clean: 6
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 16
direction_downstream: 0
tags: ["gene", "module/151"]
generated_by: "tahoemap"
---

# BACH1

*BACH transcriptional regulator 1* — 21q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 0.05 µM: 1.55× (z +5.9, q 2e-06, up in 44 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.546× (z -12.7, q 3e-34, down in 41 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CYTOR]] (+0.69, fdr 7e-06), [[NABP1]] (+0.67, fdr 7e-06), [[LINC01204]] (+0.67, fdr 1e-05); moves opposite to [[RCOR3]] (-0.62, fdr 1e-05), [[TADA1]] (-0.62, fdr 7e-06), [[CHPT1]] (-0.60, fdr 8e-06).
> It is in [[Module 151]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[CXCL8]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7967.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 0.05 µM |  | **1.55×** | +5.9 | 2e-06 | 44/47 (HS-578T, HOP62, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.43×** | +5.3 | 4e-05 | 34/48 (A-172, C32, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.28×** | +5.1 | 7e-05 | 28/48 (A-172, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.65×** | +3.9 | 0.016 | 33/48 (NCI-H1792, SW480, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | **1.56×** | +3.4 | 0.073 | 31/48 (LoVo, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.25×** | +3.3 | 0.087 | 24/48 (SNU-1, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.24× | +3.1 | 0.13 | 23/48 (KATO III, LS 180, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | 1.24× | +3.1 | 0.13 | 26/48 (NCI-H2347, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Sapanisertib (drug)]] 5 µM |  | 1.48× | +3.0 | 0.15 | 27/49 (LoVo, SW 900, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 12 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7967.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.546×** | -12.7 | 3e-34 | 41/49 (C32, J82, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.489×** | -10.6 | 9e-24 | 41/49 (SK-MEL-2, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.515×** | -9.5 | 5e-19 | 45/47 (C32, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.516×** | -9.4 | 6e-19 | 34/44 (SK-MEL-2, C32, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.570×** | -8.3 | 8e-15 | 43/48 (NCI-H1792, HEC-1-A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.582×** | -8.0 | 9e-14 | 42/48 (HEC-1-A, C32, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.622×** | -7.1 | 1e-10 | 37/48 (HT-29, C32, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.633×** | -6.3 | 2e-08 | 29/45 (CFPAC-1, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.658×** | -6.2 | 3e-08 | 42/48 (C32, H4, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | **0.758×** | -5.8 | 3e-07 | 38/48 (C32, RKO, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.675×** | -5.6 | 9e-07 | 36/48 (C32, A-172, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.719×** | -4.7 | 1e-04 | 33/50 (C32, H4, …) | top dose only |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.740×** | -4.5 | 3e-04 | 29/48 (H4, HOP62, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.780×** | -4.5 | 3e-04 | 28/48 (C32, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.743×** | -4.4 | 4e-04 | 32/49 (C32, HOP62, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.755×** | -4.0 | 0.002 | 32/49 (H4, HOP62, …) | all doses, stronger at high dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.602×** | -3.9 | 0.003 | 36/48 (C32, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.777×** | -3.8 | 0.005 | 28/49 (C32, NCI-H460, …) | two highest doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.781×** | -3.7 | 0.006 | 33/48 (KATO III, H4, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.781×** | -3.7 | 0.006 | 28/48 (H4, SW 1088, …) | all doses, stronger at high dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.844× | -3.6 | 0.008 | 21/48 (H4, HOP62, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.819×** | -3.4 | 0.015 | 24/49 (C32, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.730×** | -3.3 | 0.019 | 28/48 (A498, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.823×** | -3.3 | 0.020 | 24/48 (C32, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7967. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 823 | 2 | 28 (11 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.28× (z +12.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.291× (z -18.1) |
| [[H4 (line)]] | wt | 685 | 0 | 18 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.342× (z -14.3) |
| [[A-172 (line)]] | wt | 462 | 5 (1 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.96× (z +26.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.453× (z -13.1) |
| [[HOP62 (line)]] | alt | 527 | 0 | 9 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -13.0) |
| [[LOX-IMVI (line)]] | wt | 767 | 0 | 8 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -13.5) |
| [[NCI-H1792 (line)]] | alt | 527 | 1 | 7 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.245× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -13.6) |
| [[SK-MEL-2 (line)]] | alt | 663 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -17.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.479× (z -12.1) |
| [[hTERT-HPNE (line)]] | wt | 519 | 1 | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.20× (z +10.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -12.1) |
| [[RPMI-7951 (line)]] | alt | 593 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.322× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.552× (z -9.2) |
| [[CFPAC-1 (line)]] | alt | 566 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.291× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -10.8) |
| [[NCI-H460 (line)]] | wt | 471 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.486× (z -11.7) |
| [[A498 (line)]] | wt | 335 | 1 (1 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.47× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.366× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.541× (z -8.9) |
| [[J82 (line)]] | alt | 351 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -14.7) |
| [[LoVo (line)]] | wt | 452 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.352× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[NCI-H23 (line)]] | alt | 174 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +12.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.533× (z -9.9) |
| [[NCI-H2347 (line)]] | alt | 184 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +13.4) | — |
| [[RKO (line)]] | wt | 309 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.512× (z -10.9) |
| [[COLO 205 (line)]] | alt | 407 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.284× (z -10.5) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -9.9) |
| [[HEC-1-A (line)]] | alt | 502 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.486× (z -12.7) |
| [[Hs 766T (line)]] | wt | 521 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.323× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HT-29 (line)]] | alt | 371 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.374× (z -13.9) |
| [[LS 180 (line)]] | wt | 194 | 3 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 1.87× (z +10.3) | — |
| [[Panc 03.27 (line)]] | alt | 401 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.375× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.502× (z -9.9) |
| [[SNU-1 (line)]] | wt | 170 | 3 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 2.59× (z +10.0) | — |
| [[AsPC-1 (line)]] | alt | 698 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.353× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HS-578T (line)]] | alt | 468 | 1 | 1 | [[Homoharringtonine (drug)]] 0.5 µM 2.58× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.501× (z -9.2) |
| [[NCI-H2030 (line)]] | alt | 170 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +12.4) | — |
| [[SHP-77 (line)]] | alt | 207 | 1 (1 ⚠) | 1 | [[Daptomycin (drug)]] 5 µM 2.08× (z +8.5) ⚠ unreliable plate only | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.572× (z -9.0) |
| [[SNU-423 (line)]] | alt | 413 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.402× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[A549 (line)]] | wt | 307 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -14.0) |
| [[AN3 CA (line)]] | alt | 189 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.97× (z +11.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 310 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.356× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[NCI-H1573 (line)]] | alt | 542 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.385× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[PANC-1 (line)]] | alt | 111 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.62× (z +8.8) | — |
| [[SW 1088 (line)]] | alt | 652 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.304× (z -9.9) |
| [[SW 1271 (line)]] | alt | 562 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.301× (z -10.4) |
| [[SW 900 (line)]] | alt | 232 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.433× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SW1417 (line)]] | alt | 220 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.437× (z -8.8) ⚠ toxic |
| [[A-427 (line)]] | wt | 117 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 217 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 135 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 203 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 185 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 367 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 176 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 418 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 378 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 167 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 148 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 181 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7967), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYTOR]] | +0.69 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[NABP1]] | +0.67 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[LINC01204]] | +0.67 | +0.57 / +0.68 | both halves | 1e-05 |  |
| [[MIR4435-2HG]] | +0.66 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[SCHIP1]] | +0.65 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[ANAPC1P4]] | +0.65 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[DCBLD2]] | +0.65 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[TNFRSF12A]] | +0.65 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[PHLDA1]] | +0.64 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[TBILA]] | +0.64 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[ZFPM2-AS1]] | +0.64 | +0.49 / +0.65 | both halves | 1e-05 |  |
| [[SVIL]] | +0.64 | +0.70 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RCOR3]] | -0.62 | -0.66 / -0.55 | both halves | 1e-05 |  |
| [[TADA1]] | -0.62 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[CHPT1]] | -0.60 | -0.57 / -0.62 | both halves | 8e-06 |  |
| [[DRAM2]] | -0.59 | -0.61 / -0.54 | both halves | 1e-05 |  |
| [[MLLT10]] | -0.59 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[RABL6]] | -0.58 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[ALG9]] | -0.58 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[PRKRA]] | -0.58 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[TMEM94]] | -0.58 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[TMEM143]] | -0.57 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[FHIP2A]] | -0.57 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[C6orf136]] | -0.57 | -0.51 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 16, C 0. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CXCL8]] | B | CXCL8 activity raises BACH1's level | lines that do not express CXCL8 (20) vs lines expressing it (30) | 1.72× lower at baseline in the lines without CXCL8 | 0.015 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, IL1R1, C15orf48 |
| [[LINP1]] | B | LINP1 activity raises BACH1's level | lines that do not express LINP1 (29) vs lines expressing it (21) | 1.54× lower at baseline in the lines without LINP1 | 0.022 | ⚠ within organs, on part of the lines; also absent: ENSG00000285743, LINC00707, IGFN1 |
| [[NIPAL1]] | B | NIPAL1 activity raises BACH1's level | lines that do not express NIPAL1 (5) vs lines expressing it (45) | 1.78× lower at baseline in the lines without NIPAL1 | 0.030 | ⚠ within organs, on part of the lines; also absent: SLC18B1, AHR, RALGPS2; maybe low, not absent |
| [[LINC02742]] | B | LINC02742 activity raises BACH1's level | lines that do not express LINC02742 (34) vs lines expressing it (16) | 1.76× lower at baseline in the lines without LINC02742 | 0.033 | ⚠ within organs, on part of the lines; also absent: ENSG00000255029, ENSG00000254526, ENSG00000255227 |
| [[MANCR]] | B | MANCR activity raises BACH1's level | lines that do not express MANCR (20) vs lines expressing it (30) | 1.73× lower at baseline in the lines without MANCR | 0.039 | ⚠ within organs, on part of the lines; also absent: NLRP1, EVA1A, RAC2 |
| [[RAI14]] | B | RAI14 activity raises BACH1's level | lines that do not express RAI14 (11) vs lines expressing it (39) | 1.87× lower at baseline in the lines without RAI14 | 0.042 | ⚠ within organs, on part of the lines; also absent: CCDC71L, LINC01828, ENSG00000285744; maybe low, not absent |
| [[FRMPD4]] | B | FRMPD4 activity raises BACH1's level | lines that do not express FRMPD4 (24) vs lines expressing it (26) | 1.77× lower at baseline in the lines without FRMPD4 | 0.046 | ⚠ within organs, on part of the lines; also absent: COL4A1, BICC1, NTF3 |
| [[C12orf75-AS1]] | B | C12orf75-AS1 activity raises BACH1's level | lines that do not express C12orf75-AS1 (22) vs lines expressing it (28) | 1.78× lower at baseline in the lines without C12orf75-AS1 | 0.053 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, FOXC2, GLIPR1 |
| [[TNIP3]] | B | TNIP3 activity raises BACH1's level | lines that do not express TNIP3 (33) vs lines expressing it (17) | 1.70× lower at baseline in the lines without TNIP3 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SERPINB11, TMPRSS15, INHBA |
| [[LINC03004]] | B | LINC03004 activity raises BACH1's level | lines that do not express LINC03004 (22) vs lines expressing it (28) | 1.85× lower at baseline in the lines without LINC03004 | 0.061 | ⚠ within organs, on part of the lines; also absent: MSC-AS1, OR4F15, ADAM12; maybe low, not absent |
| [[PTGS2]] | B | PTGS2 activity raises BACH1's level | lines that do not express PTGS2 (27) vs lines expressing it (23) | 1.64× lower at baseline in the lines without PTGS2 | 0.062 | ⚠ within organs, on part of the lines; also absent: ADAMTS9-AS2, CFH, ITGA4 |
| [[RUNX1]] | B | RUNX1 activity raises BACH1's level | lines that do not express RUNX1 (5) vs lines expressing it (45) | 2.24× lower at baseline in the lines without RUNX1 | 0.067 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: KIFC3, STAMBPL1, TRIB1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 151]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.829). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (40.2, 9.8); signed map (11.0, 41.7). **Vector** length 138, 54.4% of its response variance represented; |z| ≥ 3 in 1,855 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +9.7 | +5.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +9.1 | +1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +8.2 | +2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +8.1 | +2.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.6 | +5.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.1 | +1.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +4.9 | +2.8 |
| fall | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -7.1 | -3.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -6.5 | -6.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -5.8 | -5.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -5.7 | -1.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -5.4 | -3.8 |
|  | [[venetoclax (drug)]] 5 µM |  | -5.3 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | BACH transcriptional regulator 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q21.3 — chr21:29,194,071-29,630,751 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BACH-1, BTBD24 |
| Gene groups (HGNC) | BTB domain containing; BACH transcriptional regulator family |
| Hallmark sets | HEME_METABOLISM |
| Reactome | 10 pathways, smallest: Regulation of HMOX1 expression and activity; Regulation of BACH1 activity; NFE2L2 regulating anti-oxidant/detoxification enzymes |
| Matched by | ensembl_id |

**Function**, from UniProt [O14867](https://www.uniprot.org/uniprotkb/O14867) (Transcription regulator protein BACH1):

> Transcriptional regulator that acts as a repressor or activator, depending on the context. Binds to NF-E2 DNA binding sites. Plays important roles in coordinating transcription activation and repression by MAFK (By similarity). Together with MAF, represses the transcription of genes under the control of the NFE2L2 oxidative stress pathway.

**Summary**, from NCBI Gene [571](https://www.ncbi.nlm.nih.gov/gene/571):

> This gene encodes a transcription factor that belongs to the cap'n'collar type of basic region leucine zipper factor family (CNC-bZip). The encoded protein contains broad complex, tramtrack, bric-a-brac/poxvirus and zinc finger (BTB/POZ) domains, which is atypical of CNC-bZip family members. These BTB/POZ domains facilitate protein-protein interactions and formation of homo- and/or hetero-oligomers. When this encoded protein forms a heterodimer with MafK, it functions as a repressor of Maf …

**Accessions** — [HGNC:935](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:935) · Entrez [571](https://www.ncbi.nlm.nih.gov/gene/571) · UniProt [O14867](https://www.uniprot.org/uniprotkb/O14867) · Ensembl [ENSG00000156273](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156273)

## Data

Gene col 7967: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7967); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7967, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7967]; `tensor/DDL_lfc|DDL_z.npy` [7967]; `embed/gene_vectors.npy` [7967]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7967 or target_col == 7967). Every well: [[BACH1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BACH1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
