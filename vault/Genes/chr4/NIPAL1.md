---
symbol: "NIPAL1"
type: "gene"
col: 8663
ensembl_id: "ENSG00000163293"
name: "NIPA like domain containing 1"
location: "4p12"
module: 110
arm: "+"
pooled_cpm: 16.62
n_lines_expressing: 45
n_dd_up: 17
n_dd_down: 18
n_dd_up_clean: 10
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 9
direction_downstream: 14
tags: ["gene", "module/110"]
generated_by: "tahoemap"
---

# NIPAL1

*NIPA like domain containing 1* — 4p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.97× (z +14.1, q 1e-42, up in 37 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.854× (z -7.9, q 1e-12, down in 14 of 43 measured lines) ⚠ position not correctable. The strongest without an alert is [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM: 0.644× (z -6.5, q 2e-08, down in 21 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01204]] (+0.73, fdr 7e-06), [[KBTBD8]] (+0.71, fdr 7e-06), [[HBEGF]] (+0.69, fdr 7e-06); moves opposite to [[TNRC6A]] (-0.63, fdr 7e-06), [[ERP29]] (-0.61, fdr 1e-05), [[PLEKHH3]] (-0.60, fdr 1e-05).
> It is in [[Module 110]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[C6orf141]] → it (grade B ⚠); 14 go from it, the strongest it → [[MAZ]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8663.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.97×** | +14.1 | 1e-42 | 37/41 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.92×** | +9.2 | 9e-18 | 26/38 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.80×** | +8.7 | 6e-16 | 29/42 (NCI-H2347, HEC-1-A, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.73×** | +8.0 | 1e-13 | 27/41 (CFPAC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.55×** | +6.4 | 1e-08 | 29/42 (NCI-H460, KATO III, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.50×** | +5.9 | 3e-07 | 21/41 (NCI-H2347, SW 900, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.48×** | +5.7 | 7e-07 | 22/41 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.39×** | +4.9 | 8e-05 | 17/42 (NCI-H1573, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.40×** | +4.8 | 1e-04 | 16/41 (A498, SW480, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.39×** | +4.7 | 1e-04 | 14/42 (CFPAC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.33×** | +4.2 | 0.001 | 14/42 (NCI-H1573, SW 900, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.34×** | +4.1 | 0.002 | 14/41 (NCI-H1573, A498, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.29×** | +3.8 | 0.007 | 12/41 (SW 900, NCI-H460, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.27×** | +3.6 | 0.015 | 13/42 (NCI-H460, C32, …) | all doses, flat |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.58×** | +3.5 | 0.016 | 10/40 (HOP62, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.16× | +3.0 | 0.077 | 15/43 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.16× | +3.0 | 0.085 | 13/42 (NCI-H460, A-427, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.22×** | +3.0 | 0.092 | 10/42 (Panc 03.27, CFPAC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8663.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.854× | -7.9 | 1e-12 | 14/43 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.644×** | -6.5 | 2e-08 | 21/42 (NCI-H2347, SK-MEL-2, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.667×** | -5.8 | 1e-06 | 24/41 (H4, HOP62, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM |  | **0.706×** | -5.7 | 2e-06 | 24/42 (C32, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.686×** | -5.6 | 3e-06 | 24/42 (HOP62, KATO III, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.05 µM |  | **0.691×** | -5.1 | 4e-05 | 20/40 (HS-578T, MIA PaCa-2, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.745×** | -5.0 | 5e-05 | 18/42 (C32, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.528×** | -4.9 | 6e-05 | 18/41 (RKO, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.703×** | -4.8 | 9e-05 | 16/42 (HOP62, C32, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.766×** | -4.7 | 2e-04 | 21/42 (SW48, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.738×** | -4.5 | 3e-04 | 15/41 (C32, SK-MEL-2, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.773×** | -4.4 | 5e-04 | 17/43 (HOP62, C32, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.752×** | -4.2 | 0.001 | 15/42 (hTERT-HPNE, KATO III, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.764×** | -3.8 | 0.005 | 20/40 (MIA PaCa-2, CFPAC-1, …) | all doses, flat |  |
| [[Radotinib (drug)]] 5 µM |  | 0.842× | -3.6 | 0.011 | 15/42 (C32, RKO, …) | top dose only |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.851× | -3.4 | 0.022 | 11/42 (SW 900, Hs 766T, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8663. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 25.5 | 1 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +9.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Adagrasib (drug)]] 0.05 µM 0.626× (z -12.2) ⚠ position not correctable · without an alert: [[Ponatinib (drug)]] 5 µM 0.304× (z -8.5) |
| [[C32 (line)]] | wt | 12.4 | 0 | 3 | — | [[Canagliflozin (drug)]] 0.05 µM 0.0993× (z -9.9) |
| [[A498 (line)]] | wt | 9.67 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.74× (z +10.9) | — |
| [[CFPAC-1 (line)]] | alt | 32.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +11.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.96× (z +8.8) | — |
| [[HEC-1-A (line)]] | alt | 22.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.30× (z +13.9) | [[Niclosamide (olamine) (drug)]] 5 µM 0.295× (z -9.6) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 14.0 | 0 | 2 (2 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.550× (z -10.5) ⚠ position not correctable |
| [[SK-MEL-2 (line)]] | alt | 21.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.216× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 16.4 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.68× (z +15.7) | — |
| [[A549 (line)]] | wt | 6.18 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.24× (z +9.0) | — |
| [[AsPC-1 (line)]] | alt | 47.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0658× (z -21.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[hTERT-HPNE (line)]] | wt | 8.25 | 0 | 1 | — | [[Ferulic acid (drug)]] 5 µM 0.0800× (z -8.5) |
| [[LoVo (line)]] | wt | 34.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.303× (z -10.3) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 32.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.22× (z +13.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 12.2 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.404× (z -13.9) ⚠ position not correctable |
| [[NCI-H1573 (line)]] | alt | 15.5 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.37× (z +8.6) | — |
| [[NCI-H1792 (line)]] | alt | 19.1 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.658× (z -8.5) ⚠ position not correctable |
| [[NCI-H2030 (line)]] | alt | 5.70 | 0 | 1 | — | [[Clofarabine (drug)]] 0.05 µM 0.0858× (z -9.0) |
| [[NCI-H2347 (line)]] | alt | 16.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.44× (z +8.8) | — |
| [[NCI-H460 (line)]] | wt | 7.42 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.94× (z +12.5) | — |
| [[SW48 (line)]] | wt | 41.9 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.142× (z -11.5) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 3.16 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 7.27 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.71 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.61 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.36 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 39.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.67 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.75 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.76 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8663), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01204]] | +0.73 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[KBTBD8]] | +0.71 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[HBEGF]] | +0.69 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[PNP]] | +0.66 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[CORO2B]] | +0.65 | +0.58 / +0.68 | both halves | 7e-06 |  |
| [[STK10]] | +0.64 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[RPSAP52]] | +0.63 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[SERPINB8]] | +0.63 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[HOMER1]] | +0.62 | +0.64 / +0.57 | both halves | 8e-06 |  |
| [[TBILA]] | +0.61 | +0.60 / +0.57 | both halves | 9e-06 |  |
| [[GPATCH2L]] | +0.61 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[TOMM34]] | +0.61 | +0.66 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNRC6A]] | -0.63 | -0.62 / -0.63 | both halves | 7e-06 |  |
| [[ERP29]] | -0.61 | -0.51 / -0.62 | both halves | 1e-05 |  |
| [[PLEKHH3]] | -0.60 | -0.62 / -0.52 | both halves | 1e-05 |  |
| [[EHMT2]] | -0.60 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[RCOR3]] | -0.59 | -0.65 / -0.56 | both halves | 1e-05 |  |
| [[PPP1R12B]] | -0.58 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[AUH]] | -0.57 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[PXK]] | -0.57 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[TNRC6B]] | -0.57 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[MLLT10]] | -0.56 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[ARNT]] | -0.56 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[MED25]] | -0.56 | -0.60 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C6orf141]] | B | C6orf141 activity raises NIPAL1's level | lines that do not express C6orf141 (21) vs lines expressing it (29) | 1.95× lower at baseline in the lines without C6orf141 | 0.006 | ⚠ within organs, on part of the lines; also absent: ADAM8, ENSG00000251584, SAMD12-AS1 |
| [[MAST4]] | B | MAST4 activity raises NIPAL1's level | lines that do not express MAST4 (11) vs lines expressing it (39) | 2.48× lower at baseline in the lines without MAST4 | 0.022 | ⚠ within organs, on part of the lines; also absent: TSPAN12, AHR, TLE4; maybe low, not absent |
| [[ADTRP]] | B | ADTRP activity raises NIPAL1's level | lines that do not express ADTRP (25) vs lines expressing it (25) | 1.36× lower at baseline in the lines without ADTRP | 0.023 | ⚠ within organs, on part of the lines; also absent: LINC02725, ROBO4, AIM2 |
| [[P2RY1]] | B | P2RY1 activity raises NIPAL1's level | lines that do not express P2RY1 (21) vs lines expressing it (29) | 1.48× lower at baseline in the lines without P2RY1 | 0.040 | ⚠ within organs, on part of the lines; also absent: RGS2, FGF14, BASP1-AS1 |
| [[FAR2]] | B | FAR2 activity raises NIPAL1's level | lines that do not express FAR2 (19) vs lines expressing it (31) | 1.67× lower at baseline in the lines without FAR2 | 0.042 | ⚠ within organs, on part of the lines; also absent: CCN3, MIR155HG, LINC02605; maybe low, not absent |
| [[NRIP3]] | B | NRIP3 activity lowers NIPAL1's level | lines that do not express NRIP3 (15) vs lines expressing it (35) | 1.94× higher at baseline in the lines without NRIP3 | 0.052 | ⚠ within organs, on part of the lines; also absent: SDK2, DTX3, MCTP1 |
| [[MAP2K1]] | B | MAP2K1 activity raises NIPAL1's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.1% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |
| [[PHLDA2]] | B | PHLDA2 activity raises NIPAL1's level | lines that do not express PHLDA2 (7) vs lines expressing it (43) | 2.71× lower at baseline in the lines without PHLDA2 | 0.072 | ⚠ within organs, on part of the lines; also absent: MET, TGFBR2, SDC4; maybe low, not absent |
| [[RABGEF1P3]] | B | RABGEF1P3 activity raises NIPAL1's level | lines that do not express RABGEF1P3 (5) vs lines expressing it (45) | 2.67× lower at baseline in the lines without RABGEF1P3 | 0.099 | ⚠ within organs, on part of the lines; also absent: SLC2A1, PHLDA2, SHB; maybe low, not absent |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 13, C 1. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAZ]] | B | NIPAL1 activity lowers MAZ's level | lines that do not express NIPAL1 (5) vs lines expressing it (45) | 1.55× higher at baseline in the lines without NIPAL1 | 0.003 | ⚠ within organs, on part of the lines; also absent: SLC18B1, AHR, RALGPS2; maybe low, not absent |
| [[HSF2]] | B | NIPAL1 activity lowers HSF2's level | lines that do not express NIPAL1 (5) vs lines expressing it (45) | 2.00× higher at baseline in the lines without NIPAL1 | 0.009 | ⚠ within organs, on part of the lines; also absent: SLC18B1, AHR, RALGPS2; maybe low, not absent |
| [[BACH1]] | B | NIPAL1 activity raises BACH1's level | lines that do not express NIPAL1 (5) vs lines expressing it (45) | 1.78× lower at baseline in the lines without NIPAL1 | 0.030 | ⚠ within organs, on part of the lines; also absent: SLC18B1, AHR, RALGPS2; maybe low, not absent |
| [[SERPINB8]] | B | NIPAL1 activity raises SERPINB8's level | lines that do not express NIPAL1 (5) vs lines expressing it (45) | 1.73× lower at baseline in the lines without NIPAL1 | 0.059 | ⚠ within organs, on part of the lines; also absent: SLC18B1, AHR, RALGPS2; maybe low, not absent |
| [[BLZF2P]] | B | NIPAL1 activity raises BLZF2P's level | lines that do not express NIPAL1 (5) vs lines expressing it (45) | 1.77× lower at baseline in the lines without NIPAL1 | 0.063 | ⚠ within organs, on part of the lines; also absent: SLC18B1, AHR, RALGPS2; maybe low, not absent |
| [[MAST4]] | B | NIPAL1 activity raises MAST4's level | lines that do not express NIPAL1 (5) vs lines expressing it (45) | 4.75× lower at baseline in the lines without NIPAL1 | 0.070 | ⚠ within organs, on part of the lines; also absent: SLC18B1, AHR, RALGPS2; maybe low, not absent |
| cells under [[Ralimetinib dimesylate (drug)]] 5 µM | B | NIPAL1 activity raises the cells' numbers under Ralimetinib dimesylate 5 µM (protects the cells) | lines that do not express NIPAL1 (5) vs lines expressing it (43) | the lines without NIPAL1: 0.78× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: SLC18B1, AHR, RALGPS2; maybe low, not absent |
| cells under [[Isocorydine (drug)]] 5 µM | B | NIPAL1 activity raises the cells' numbers under Isocorydine 5 µM (protects the cells) | lines that do not express NIPAL1 (5) vs lines expressing it (43) | the lines without NIPAL1: 0.91× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: SLC18B1, AHR, RALGPS2; maybe low, not absent |
| cells under [[MK-3903 (drug)]] 0.05 µM | B | NIPAL1 activity raises the cells' numbers under MK-3903 0.05 µM (protects the cells) | lines that do not express NIPAL1 (5) vs lines expressing it (43) | the lines without NIPAL1: 0.85× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; also absent: SLC18B1, AHR, RALGPS2; maybe low, not absent |
| [[C3orf52]] | B | NIPAL1 activity raises C3orf52's level | lines that do not express NIPAL1 (5) vs lines expressing it (45) | 2.49× lower at baseline in the lines without NIPAL1 | 0.079 | ⚠ within organs, on part of the lines; also absent: SLC18B1, AHR, RALGPS2; maybe low, not absent |
| cells under [[Lapatinib ditosylate (drug)]] 0.5 µM | B | NIPAL1 activity raises the cells' numbers under Lapatinib ditosylate 0.5 µM (protects the cells) | lines that do not express NIPAL1 (5) vs lines expressing it (43) | the lines without NIPAL1: 0.77× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; also absent: SLC18B1, AHR, RALGPS2; maybe low, not absent |
| cells under [[c-Kit-IN-1 (drug)]] 0.5 µM | B | NIPAL1 activity raises the cells' numbers under c-Kit-IN-1 0.5 µM (protects the cells) | lines that do not express NIPAL1 (5) vs lines expressing it (43) | the lines without NIPAL1: 0.79× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; also absent: SLC18B1, AHR, RALGPS2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 110]]; 43 genes; every member is in the + arm (projection on the module's main direction 0.727). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.1, 1.2); signed map (4.4, 46.1). **Vector** length 110, 26.6% of its response variance represented; |z| ≥ 3 in 1,041 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.3 | +14.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.7 | +9.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +5.6 | +6.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.3 | +3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.0 | +5.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.8 | +3.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.6 | +4.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +3.0 |
| fall | [[Trametinib (drug)]] 5 µM |  | -4.4 | -5.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.3 | -6.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.0 | -4.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.8 | -4.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.8 | -5.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.7 | -5.8 |

## What is on record

|  |  |
|---|---|
| Name | NIPA like domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p12 — chr4:47,914,142-48,040,173 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp686A06115, SLC57A3, NIPA3; previously NPAL1 |
| Gene groups (HGNC) | Solute carrier family 57, NIPA-like magnesium transporters |
| Reactome | 2 pathways, smallest: Miscellaneous transport and binding events; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6NVV3](https://www.uniprot.org/uniprotkb/Q6NVV3) (Magnesium transporter NIPA3):

> Acts as a Mg(2+) transporter. Can also transport other divalent cations such as Fe(2+), Sr(2+), Ba(2+), Mn(2+), Cu(2+) and Co(2+) but to a much less extent than Mg(2+) (By similarity).

**Summary**, from NCBI Gene [152519](https://www.ncbi.nlm.nih.gov/gene/152519):

> Predicted to enable magnesium ion transmembrane transporter activity. Predicted to be involved in magnesium ion transport. Predicted to be located in Golgi apparatus. Predicted to be active in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:27194](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27194) · Entrez [152519](https://www.ncbi.nlm.nih.gov/gene/152519) · UniProt [Q6NVV3](https://www.uniprot.org/uniprotkb/Q6NVV3) · Ensembl [ENSG00000163293](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163293)

## Data

Gene col 8663: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8663); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8663, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8663]; `tensor/DDL_lfc|DDL_z.npy` [8663]; `embed/gene_vectors.npy` [8663]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8663 or target_col == 8663). Every well: [[NIPAL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NIPAL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
