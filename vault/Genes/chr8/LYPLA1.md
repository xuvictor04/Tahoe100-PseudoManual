---
symbol: "LYPLA1"
type: "gene"
col: 4243
ensembl_id: "ENSG00000120992"
name: "lysophospholipase 1"
location: "8q11.23"
module: 35
arm: "-"
pooled_cpm: 113.98
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 12
n_dd_up_clean: 5
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# LYPLA1

*lysophospholipase 1* — 8q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.54× (z +16.0, q 0e+00, up in 47 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.33× (z +5.9, q 5e-07, up in 30 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.469× (z -22.2, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP13A2]] (+0.69, fdr 1e-05), [[PACC1]] (+0.66, fdr 2e-05), [[ANKS6]] (+0.66, fdr 2e-05); moves opposite to [[TET2]] (-0.66, fdr 1e-05), [[KBTBD4]] (-0.64, fdr 1e-05), [[CDKN1B]] (-0.62, fdr 1e-05).
> It sits in the **-** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[IRAG2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 7 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4243.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.54×** | +16.0 | 0e+00 | 47/49 (LOX-IMVI, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.02×** | +13.9 | 1e-41 | 42/44 (HS-578T, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.80×** | +11.3 | 4e-27 | 39/45 (HEC-1-A, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +7.3 | 4e-11 | 35/47 (LoVo, Hs 766T, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.33×** | +5.9 | 5e-07 | 30/48 (AsPC-1, MIA PaCa-2, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.17× | +4.4 | 9e-04 | 20/49 (SK-MEL-2, CFPAC-1, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.23×** | +4.2 | 0.002 | 22/48 (AsPC-1, CFPAC-1, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.20×** | +3.7 | 0.018 | 21/47 (AsPC-1, H4, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~44% of this change | 1.18× | +3.5 | 0.032 | 20/48 (RPMI-7951, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.18× | +3.4 | 0.032 | 21/47 (PANC-1, CFPAC-1, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.36×** | +3.4 | 0.032 | 21/48 (PANC-1, HOP62, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[vincristine (drug)]] 5 µM |  | **1.36×** | +3.3 | 0.047 | 20/46 (PANC-1, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.16× | +3.1 | 0.088 | 18/48 (CFPAC-1, PANC-1, …) | rises with dose |  |
| [[Ixazomib (drug)]] 0.05 µM |  | 1.17× | +3.0 | 0.090 | 11/47 (HepG2/C3A, SNU-1, …) | inconsistent across doses | position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | 1.17× | +3.0 | 0.090 | 15/48 (AsPC-1, CFPAC-1, …) | top dose only |  |
| [[Canagliflozin (drug)]] 0.05 µM |  | 1.17× | +3.0 | 0.098 | 12/47 (HS-578T, HT-29, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4243.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.469×** | -22.2 | 0e+00 | 47/48 (J82, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.721×** | -9.6 | 2e-19 | 35/49 (AsPC-1, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.644×** | -9.1 | 1e-17 | 34/48 (NCI-H2347, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.697×** | -7.2 | 8e-11 | 34/48 (J82, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.518×** | -7.1 | 1e-10 | 39/49 (RKO, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.562×** | -6.2 | 4e-08 | 32/48 (HOP62, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.772×** | -5.4 | 5e-06 | 30/50 (AsPC-1, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.811×** | -4.2 | 0.002 | 26/47 (AsPC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.875× | -3.9 | 0.005 | 15/48 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.703×** | -3.8 | 0.008 | 23/50 (AsPC-1, NCI-H23, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | 0.842× | -3.8 | 0.008 | 18/49 (AsPC-1, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.882× | -3.6 | 0.013 | 13/48 (AsPC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.857× | -3.5 | 0.017 | 17/48 (AsPC-1, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | 0.840× | -3.4 | 0.024 | 17/48 (AsPC-1, CFPAC-1, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.822×** | -3.4 | 0.025 | 17/47 (AsPC-1, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.848× | -3.4 | 0.025 | 20/48 (AsPC-1, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4243. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 170 | 1 | 7 (1 ⚠) | [[Auranofin (drug)]] 5 µM 1.98× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -22.9) |
| [[RKO (line)]] | wt | 167 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -21.8) |
| [[C32 (line)]] | wt | 85.7 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 3.37× (z +11.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.436× (z -11.2) |
| [[HOP62 (line)]] | alt | 90.4 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.72× (z +12.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -20.3) |
| [[NCI-H23 (line)]] | alt | 144 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 2.22× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -15.9) |
| [[PANC-1 (line)]] | alt | 167 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.27× (z +10.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.487× (z -15.8) |
| [[A-172 (line)]] | wt | 60.6 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.04× (z +11.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.430× (z -13.0) |
| [[A498 (line)]] | wt | 185 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.10× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -17.2) |
| [[HEC-1-A (line)]] | alt | 113 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.05 µM 2.31× (z +11.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.590× (z -10.7) |
| [[HS-578T (line)]] | alt | 67.8 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.42× (z +12.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -17.8) |
| [[LoVo (line)]] | wt | 90.9 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.38× (z +9.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.419× (z -16.0) |
| [[LOX-IMVI (line)]] | wt | 139 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.95× (z +12.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -19.9) |
| [[NCI-H1792 (line)]] | alt | 67.5 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.48× (z +11.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.459× (z -10.5) |
| [[NCI-H460 (line)]] | wt | 75.4 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.78× (z +12.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -19.8) |
| [[SNU-423 (line)]] | alt | 62.5 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.93× (z +12.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -10.9) |
| [[SW480 (line)]] | alt | 112 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.54× (z +11.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.510× (z -13.5) |
| [[A549 (line)]] | wt | 128 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.82× (z +10.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.519× (z -10.9) |
| [[MIA PaCa-2 (line)]] | alt | 143 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.42× (z +9.9) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.479× (z -11.9) |
| [[NCI-H1573 (line)]] | alt | 50.9 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.31× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -16.1) |
| [[CFPAC-1 (line)]] | alt | 93.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.18× (z +9.4) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 85.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.59× (z +9.6) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 84.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.20× (z +10.2) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 103 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.01× (z +10.9) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 119 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -26.8) |
| [[NCI-H2030 (line)]] | alt | 219 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -18.3) |
| [[NCI-H2347 (line)]] | alt | 145 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.401× (z -17.6) |
| [[Panc 03.27 (line)]] | alt | 131 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.72× (z +9.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.504× (z -10.9) |
| [[RPMI-7951 (line)]] | alt | 55.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.46× (z +9.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -13.6) |
| [[SW48 (line)]] | wt | 120 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.444× (z -11.3) |
| [[A-427 (line)]] | wt | 142 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.516× (z -13.2) |
| [[BT-474 (line)]] | alt | 99.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.536× (z -9.9) |
| [[C-33 A (line)]] | alt | 114 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.47× (z +9.0) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 58.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.80× (z +10.4) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 120 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.462× (z -11.1) |
| [[hTERT-HPNE (line)]] | wt | 56.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -11.7) |
| [[KATO III (line)]] | alt | 120 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.509× (z -11.3) |
| [[SK-MEL-2 (line)]] | alt | 88.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -15.9) |
| [[AN3 CA (line)]] | alt | 89.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 78.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 58.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 110 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 227 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 130 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 96.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 87.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 77.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4243), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*48 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP13A2]] | +0.69 | +0.66 / +0.51 | both halves | 1e-05 |  |
| [[PACC1]] | +0.66 | +0.67 / +0.47 | both halves | 2e-05 |  |
| [[ANKS6]] | +0.66 | +0.67 / +0.48 | both halves | 2e-05 |  |
| [[METAP1]] | +0.63 | +0.70 / +0.42 | both halves | 4e-05 |  |
| [[TEX2]] | +0.62 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[INPP4A]] | +0.62 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[MCOLN2]] | +0.62 | +0.55 / +0.46 | both halves | 2e-05 |  |
| [[EEF1E1]] | +0.62 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[PPM1F]] | +0.61 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[EPS15]] | +0.61 | +0.68 / +0.46 | both halves | 2e-05 |  |
| [[PALS2]] | +0.61 | +0.72 / +0.44 | both halves | 3e-05 |  |
| [[CRLF3]] | +0.60 | +0.63 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*52 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TET2]] | -0.66 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[KBTBD4]] | -0.64 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[CDKN1B]] | -0.62 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[C11orf71]] | -0.62 | -0.57 / -0.42 | both halves | 4e-05 |  |
| [[AEBP2]] | -0.61 | -0.65 / -0.37 | both halves | 8e-05 |  |
| [[TAPBPL]] | -0.61 | -0.62 / -0.41 | both halves | 4e-05 |  |
| [[BTN2A1]] | -0.60 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[ZNF764]] | -0.59 | -0.61 / -0.42 | both halves | 4e-05 |  |
| [[PAF1]] | -0.59 | -0.63 / -0.48 | both halves | 2e-05 |  |
| [[KMO]] | -0.59 | -0.60 / -0.40 | both halves | 5e-05 |  |
| [[RBM23]] | -0.59 | -0.62 / -0.43 | both halves | 3e-05 |  |
| [[CREBZF]] | -0.59 | -0.63 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IRAG2]] | B | IRAG2 activity lowers LYPLA1's level | lines that do not express IRAG2 (39) vs lines expressing it (11) | 1.40× higher at baseline in the lines without IRAG2 | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CARMN, GDNF, LINC01411 |
| [[JAM2]] | B | JAM2 activity lowers LYPLA1's level | lines that do not express JAM2 (28) vs lines expressing it (22) | 1.34× higher at baseline in the lines without JAM2 | 0.055 | ⚠ within organs, on part of the lines; also absent: ITGA4, RORB, IL7R |
| [[ABCA3]] | B | ABCA3 activity raises LYPLA1's level | lines that do not express ABCA3 (9) vs lines expressing it (41) | 1.42× lower at baseline in the lines without ABCA3 | 0.091 | ⚠ within organs, on part of the lines; also absent: SLC37A1, CCDC88C, GRTP1; maybe low, not absent |
| [[TENT5A]] | B | TENT5A activity lowers LYPLA1's level | lines that do not express TENT5A (11) vs lines expressing it (39) | 1.36× higher at baseline in the lines without TENT5A | 0.095 | ⚠ within organs, on part of the lines; also absent: GBP2, CXCL2, IFI44; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **-** arm (projection on the module's main direction -0.504). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (13.1, 3.9); signed map (-42.5, -8.5). **Vector** length 118, 37.8% of its response variance represented; |z| ≥ 3 in 1,045 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.8 | +2.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +5.0 | +4.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.5 | +0.4 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +4.2 | +3.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | +1.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.0 | +0.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.8 | +4.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.6 | +0.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.6 | +3.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -10.0 | -9.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -8.5 | -22.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.7 | -7.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.9 | -7.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.9 | -3.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | -4.4 | -3.8 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -4.2 | -3.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.1 | -4.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -4.1 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | lysophospholipase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q11.23 — chr8:54,046,367-54,102,017 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LPL1, APT-1, APT1 |
| Gene groups (HGNC) | Depalmitoylases; Thioester hydrolases |
| Reactome | 6 pathways, smallest: eNOS activation; Metabolism of nitric oxide: NOS3 activation and regulation; RAS processing |
| Matched by | ensembl_id |

**Function**, from UniProt [O75608](https://www.uniprot.org/uniprotkb/O75608) (Acyl-protein thioesterase 1):

> Acts as an acyl-protein thioesterase. Hydrolyzes fatty acids from S-acylated cysteine residues in proteins such as trimeric G alpha proteins or HRAS. Acts as a palmitoyl thioesterase that catalyzes depalmitoylation of proteins, such as ADRB2, KCNMA1 and SQSTM1. Acts as a negative regulator of autophagy by mediating palmitoylation of SQSTM1, decreasing affinity between SQSTM1 and ATG8 proteins and recruitment of ubiquitinated cargo proteins to autophagosomes. Acts as a lysophospholipase and …

**Summary**, from NCBI Gene [10434](https://www.ncbi.nlm.nih.gov/gene/10434):

> This gene encodes a member of the alpha/beta hydrolase superfamily. The encoded protein functions as a homodimer, exhibiting both depalmitoylating as well as lysophospholipase activity, and may be involved in Ras localization and signaling. Alternate splicing results in multiple transcript variants. Pseudogenes of this gene have been defined on chromosomes 4, 6, and 7. [provided by RefSeq, Jul 2013]

**Accessions** — [HGNC:6737](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6737) · Entrez [10434](https://www.ncbi.nlm.nih.gov/gene/10434) · UniProt [O75608](https://www.uniprot.org/uniprotkb/O75608) · Ensembl [ENSG00000120992](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120992)

## Data

Gene col 4243: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4243); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4243, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4243]; `tensor/DDL_lfc|DDL_z.npy` [4243]; `embed/gene_vectors.npy` [4243]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4243 or target_col == 4243). Every well: [[LYPLA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LYPLA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
