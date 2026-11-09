---
symbol: "STX12"
type: "gene"
col: 3949
ensembl_id: "ENSG00000117758"
name: "syntaxin 12"
location: "1p35.3"
module: 4
arm: "-"
pooled_cpm: 67.38
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 11
n_dd_up_clean: 10
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# STX12

*syntaxin 12* — 1p35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.61× (z +16.7, q 0e+00, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.641× (z -11.0, q 1e-25, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDR44]] (+0.62, fdr 1e-05), [[ABHD18]] (+0.61, fdr 1e-05), [[EIF1B]] (+0.60, fdr 1e-05); moves opposite to [[COG8]] (-0.61, fdr 1e-05), [[NUP155]] (-0.57, fdr 1e-05), [[PFKM]] (-0.57, fdr 3e-05).
> It sits in the **-** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[NUP210]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3949.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.61×** | +16.7 | 0e+00 | 38/48 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.80×** | +14.6 | 0e+00 | 42/48 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.70×** | +13.1 | 4e-37 | 39/48 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.60×** | +11.7 | 2e-29 | 40/48 (HEC-1-A, LoVo, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.46×** | +9.4 | 9e-19 | 30/48 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +9.3 | 1e-18 | 40/48 (NCI-H460, C32, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +8.9 | 3e-17 | 35/50 (NCI-H460, LS 180, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.24×** | +7.6 | 2e-12 | 29/49 (LoVo, NCI-H460, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.29×** | +6.3 | 2e-08 | 26/48 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.27×** | +5.9 | 2e-07 | 24/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.26×** | +5.8 | 4e-07 | 25/48 (hTERT-HPNE, NCI-H1792, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.26×** | +5.5 | 2e-06 | 26/48 (LoVo, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.24×** | +5.1 | 1e-05 | 25/47 (NCI-H460, A-427, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.27×** | +5.1 | 2e-05 | 23/48 (H4, LS 180, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.22×** | +5.0 | 2e-05 | 21/48 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.11× | +3.7 | 0.007 | 11/49 (H4, HepG2/C3A, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.15× | +3.5 | 0.013 | 12/48 (COLO 205, CFPAC-1, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.17× | +3.5 | 0.015 | 14/49 (NCI-H460, A-172, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 1.12× | +3.3 | 0.028 | 10/48 (NCI-H460, SNU-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.10× | +3.0 | 0.062 | 5/48 (COLO 205, HS-578T, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3949.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.641×** | -11.0 | 1e-25 | 35/48 (HT-29, HOP62, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.471×** | -9.8 | 4e-20 | 36/49 (HS-578T, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.694×** | -8.4 | 1e-14 | 28/45 (RKO, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.584×** | -7.0 | 4e-10 | 28/48 (HS-578T, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.802×** | -5.3 | 2e-05 | 24/48 (PANC-1, NCI-H1792, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.811×** | -5.2 | 2e-05 | 25/49 (HS-578T, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.808×** | -5.1 | 3e-05 | 22/43 (C-33 A, A549, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | **0.828×** | -4.7 | 2e-04 | 24/47 (hTERT-HPNE, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.747×** | -3.8 | 0.010 | 17/47 (SNU-1, SHP-77, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.764×** | -3.5 | 0.027 | 13/48 (Hs 766T, RKO, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.875× | -3.3 | 0.047 | 12/48 (RKO, HT-29, …) | inconsistent across doses |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | 0.878× | -3.2 | 0.060 | 10/49 (CFPAC-1, NCI-H1792, …) | two highest doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.782×** | -3.2 | 0.060 | 14/36 (HS-578T, HT-29, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3949. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 68.9 | 11 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +21.0) | — |
| [[NCI-H460 (line)]] | wt | 53.0 | 7 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +16.8) | [[Dinaciclib (drug)]] 0.05 µM 0.351× (z -13.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 72.6 | 6 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +13.3) ⚠ cell-cycle shift, explains ~12% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.08× (z +12.4) | — |
| [[PANC-1 (line)]] | alt | 70.7 | 3 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.59× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.504× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.349× (z -8.8) |
| [[SW480 (line)]] | alt | 65.0 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +20.5) | — |
| [[C32 (line)]] | wt | 64.6 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +11.4) | — |
| [[HEC-1-A (line)]] | alt | 57.4 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.55× (z +12.0) | — |
| [[AN3 CA (line)]] | alt | 71.3 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.137× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.166× (z -10.4) |
| [[C-33 A (line)]] | alt | 92.6 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.72× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.159× (z -18.1) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 121 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.485× (z -9.1) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.260× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 50.7 | 2 | 1 | [[Homoharringtonine (drug)]] 0.5 µM 3.23× (z +12.4) | [[Auranofin (drug)]] 5 µM 0.400× (z -9.7) |
| [[A-427 (line)]] | wt | 48.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.203× (z -14.4) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 70.5 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +12.1) | [[Auranofin (drug)]] 5 µM 0.402× (z -10.9) |
| [[HT-29 (line)]] | alt | 89.1 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 1.93× (z +8.5) | [[Auranofin (drug)]] 5 µM 0.426× (z -11.1) |
| [[Panc 03.27 (line)]] | alt | 54.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.365× (z -9.5) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 59.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +10.4) | [[Dinaciclib (drug)]] 0.05 µM 0.249× (z -12.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 45.3 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.63× (z +10.2) | — |
| [[A549 (line)]] | wt | 56.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.232× (z -14.9) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 42.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +11.2) | — |
| [[CFPAC-1 (line)]] | alt | 44.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +10.3) | — |
| [[COLO 205 (line)]] | alt | 78.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +10.0) | — |
| [[H4 (line)]] | wt | 79.7 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.121× (z -8.7) |
| [[HCT15 (line)]] | alt | 89.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +9.1) | — |
| [[Hs 766T (line)]] | wt | 101 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.409× (z -10.1) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 84.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +8.7) | — |
| [[J82 (line)]] | alt | 56.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +10.4) | — |
| [[LOX-IMVI (line)]] | wt | 78.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.370× (z -9.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 79.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.363× (z -9.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 72.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.344× (z -10.5) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 68.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +11.5) | — |
| [[RKO (line)]] | wt | 115 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.105× (z -25.4) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 116 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.390× (z -8.7) |
| [[SHP-77 (line)]] | alt | 59.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.419× (z -8.7) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 51.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +9.9) | — |
| [[SNU-423 (line)]] | alt | 81.5 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.392× (z -9.7) |
| [[A-172 (line)]] | wt | 47.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 61.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 75.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 40.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 59.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 68.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 65.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 69.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 60.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 72.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 55.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 53.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 58.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 53.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3949), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR44]] | +0.62 | +0.49 / +0.65 | both halves | 1e-05 |  |
| [[ABHD18]] | +0.61 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[EIF1B]] | +0.60 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[CCS]] | +0.60 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[ITCH]] | +0.59 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[CDC37L1]] | +0.59 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[LRCH3]] | +0.59 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[SELENOK]] | +0.58 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[COX17]] | +0.57 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[SCAMP2]] | +0.56 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[TMEM50A]] | +0.56 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[INAFM1]] | +0.56 | +0.54 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COG8]] | -0.61 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[NUP155]] | -0.57 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[PFKM]] | -0.57 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[HNRNPF]] | -0.56 | -0.61 / -0.52 | both halves | 1e-05 |  |
| [[RAB4A-AS1]] | -0.56 | -0.40 / -0.56 | both halves | 5e-05 |  |
| [[ATIC]] | -0.55 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[MAT2A]] | -0.55 | -0.46 / -0.60 | both halves | 3e-05 |  |
| [[PRKDC]] | -0.54 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[PFAS]] | -0.54 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[ADAM22]] | -0.54 | -0.50 / -0.34 | both halves | 1e-04 |  |
| [[LRP5]] | -0.52 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[G3BP1]] | -0.52 | -0.48 / -0.54 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NUP210]] | B | NUP210 activity lowers STX12's level | lines that do not express NUP210 (13) vs lines expressing it (37) | 1.36× higher at baseline in the lines without NUP210 | 0.021 | ⚠ within organs, on part of the lines; also absent: PRR36, NEBL, FAM169A |
| [[TOP2A]] | B | TOP2A activity lowers STX12's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **-** arm (projection on the module's main direction -0.535). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-27.9, -31.5); signed map (-15.3, 4.6). **Vector** length 110, 29.3% of its response variance represented; |z| ≥ 3 in 1,067 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +8.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +9.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +5.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.8 | +16.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +3.8 | +5.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.6 | +3.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.8 | +2.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.6 | +3.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.5 | +2.8 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.2 | +2.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -8.7 | -11.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | -8.3 | -9.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -7.7 | -7.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.4 | -8.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.4 | -3.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.3 | -5.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.9 | -0.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.8 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | syntaxin 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p35.3 — chr1:27,773,219-27,824,443 (+) |
| Ensembl biotype | protein_coding |
| Also known as | STX13, STX14 |
| Gene groups (HGNC) | Syntaxins |
| Hallmark sets | PROTEIN_SECRETION |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86Y82](https://www.uniprot.org/uniprotkb/Q86Y82) (Syntaxin-12):

> SNARE promoting fusion of transport vesicles with target membranes. Together with SNARE STX6, promotes movement of vesicles from endosomes to the cell membrane, and may therefore function in the endocytic recycling pathway. Through complex formation with GRIP1, GRIA2 and NSG1 controls the intracellular fate of AMPAR and the endosomal sorting of the GRIA2 subunit toward recycling and membrane targeting.

**Summary**, from NCBI Gene [23673](https://www.ncbi.nlm.nih.gov/gene/23673):

> Predicted to enable SNAP receptor activity and SNARE binding activity. Involved in autophagosome assembly; cholesterol efflux; and protein stabilization. Located in several cellular components, including BLOC-1 complex; phagocytic vesicle; and phagophore assembly site. Part of SNARE complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:11430](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11430) · Entrez [23673](https://www.ncbi.nlm.nih.gov/gene/23673) · UniProt [Q86Y82](https://www.uniprot.org/uniprotkb/Q86Y82) · Ensembl [ENSG00000117758](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117758)

## Data

Gene col 3949: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3949); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3949, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3949]; `tensor/DDL_lfc|DDL_z.npy` [3949]; `embed/gene_vectors.npy` [3949]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3949 or target_col == 3949). Every well: [[STX12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STX12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
