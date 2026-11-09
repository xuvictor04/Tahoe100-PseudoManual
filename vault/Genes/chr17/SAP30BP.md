---
symbol: "SAP30BP"
type: "gene"
col: 8435
ensembl_id: "ENSG00000161526"
name: "SAP30 binding protein"
location: "17q25.1"
module: 38
arm: "+"
pooled_cpm: 96.33
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 19
n_dd_up_clean: 13
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# SAP30BP

*SAP30 binding protein* — 17q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.15× (z +13.6, q 2e-39, up in 46 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.472× (z -13.2, q 7e-37, down in 39 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 0.671× (z -7.3, q 4e-11, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[USE1]] (+0.73, fdr 7e-06), [[ZKSCAN5]] (+0.70, fdr 7e-06), [[BIN3]] (+0.69, fdr 7e-06); moves opposite to [[KDM1A]] (-0.62, fdr 1e-05), [[TMEM123]] (-0.60, fdr 2e-05), [[HSF2]] (-0.58, fdr 1e-05).
> It is in [[Module 038]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8435.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.15×** | +13.6 | 2e-39 | 46/49 (SW480, COLO 205, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.84×** | +10.0 | 6e-21 | 42/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.37×** | +8.2 | 3e-14 | 34/48 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.54×** | +7.9 | 3e-13 | 40/48 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.39×** | +6.0 | 2e-07 | 39/48 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.38×** | +5.7 | 1e-06 | 30/48 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.36×** | +5.6 | 1e-06 | 32/48 (SW480, HT-29, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.29×** | +4.7 | 2e-04 | 29/48 (NCI-H460, AsPC-1, …) | rises with dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.30×** | +4.5 | 4e-04 | 30/48 (SW480, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.25×** | +4.1 | 0.002 | 26/48 (HT-29, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.23×** | +3.8 | 0.007 | 24/48 (SNU-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.22×** | +3.6 | 0.014 | 23/48 (NCI-H460, SNU-1, …) | two highest doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.019 | 20/48 (SW480, SW 900, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.30×** | +3.4 | 0.028 | 22/49 (SW480, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.20×** | +3.4 | 0.029 | 20/48 (NCI-H460, SNU-1, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.40×** | +3.2 | 0.041 | 17/48 (HOP62, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM |  | 1.18× | +3.0 | 0.077 | 14/48 (NCI-H23, Hs 766T, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.25×** | +3.0 | 0.096 | 17/48 (HCT15, HT-29, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8435.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.472×** | -13.2 | 7e-37 | 39/44 (AsPC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.503×** | -12.5 | 1e-33 | 42/49 (HOP62, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.600×** | -8.6 | 1e-15 | 36/45 (J82, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.671×** | -7.3 | 4e-11 | 37/48 (LoVo, J82, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.781×** | -6.4 | 2e-08 | 36/48 (hTERT-HPNE, A-172, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.731×** | -5.7 | 1e-06 | 36/48 (J82, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.816×** | -5.1 | 3e-05 | 25/48 (A-427, PANC-1, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.766×** | -4.9 | 9e-05 | 25/49 (NCI-H2347, SW48, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.764×** | -4.7 | 2e-04 | 32/47 (SK-MEL-2, LoVo, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.619×** | -4.6 | 3e-04 | 32/49 (AsPC-1, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.771×** | -4.4 | 6e-04 | 29/48 (LoVo, NCI-H1573, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.787×** | -4.4 | 6e-04 | 30/48 (AsPC-1, A-427, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.831×** | -4.0 | 0.003 | 23/48 (LoVo, HepG2/C3A, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.808×** | -3.9 | 0.004 | 26/49 (LoVo, SW480, …) | all doses, flat |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.869× | -3.6 | 0.011 | 11/48 (Hs 766T, NCI-H1792, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.821×** | -3.6 | 0.011 | 26/48 (A549, LoVo, …) | rises with dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.813×** | -3.6 | 0.012 | 22/48 (SK-MEL-2, SW480, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.845× | -3.6 | 0.012 | 19/48 (SK-MEL-2, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.829×** | -3.3 | 0.024 | 21/48 (LoVo, NCI-H1573, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8435. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 73.9 | 9 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +12.3) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.63× (z +10.6) | — |
| [[SW480 (line)]] | alt | 98.7 | 5 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.32× (z +14.6) | [[Dinaciclib (drug)]] 0.5 µM 0.523× (z -9.0) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 102 | 3 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +10.7) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.89× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.342× (z -12.4) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 136 | 2 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +14.5) ⚠ cell-cycle shift, explains ~22% of this change | [[Dinaciclib (drug)]] 5 µM 0.229× (z -18.9) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 88.5 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.82× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.486× (z -10.0) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 91.6 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.87× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.464× (z -10.2) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 107 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +10.7) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.37× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.376× (z -10.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 142 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.325× (z -11.3) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 111 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.69× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.305× (z -14.5) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 107 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.289× (z -15.3) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 90.7 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.58× (z +10.6) | [[Dinaciclib (drug)]] 0.5 µM 0.452× (z -10.6) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 93.4 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.37× (z +11.6) | [[Dinaciclib (drug)]] 0.5 µM 0.390× (z -10.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 83.2 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +10.5) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.64× (z +8.9) | [[Dinaciclib (drug)]] 0.05 µM 0.370× (z -9.0) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 68.9 | 2 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 13.2× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.210× (z -10.7) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 65.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.194× (z -12.9) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 98.7 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 16.6× (z +12.4) | — |
| [[HT-29 (line)]] | alt | 64.5 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.19× (z +9.1) | — |
| [[KATO III (line)]] | alt | 108 | 1 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 3.93× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.360× (z -12.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 97.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +9.2) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.62× (z +8.8) | — |
| [[NCI-H1792 (line)]] | alt | 103 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.336× (z -9.3) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 108 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.21× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.426× (z -10.5) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 91.6 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.83× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.283× (z -13.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 108 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.85× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.328× (z -12.4) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 102 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.396× (z -10.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 108 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.294× (z -13.7) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 121 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.440× (z -9.6) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 73.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.211× (z -11.9) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 76.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.393× (z -10.4) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 115 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.144× (z -8.7) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 84.9 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.46× (z +8.6) ⚠ cell-cycle shift, explains ~24% of this change | — |
| [[LS 180 (line)]] | wt | 72.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.57× (z +8.9) | — |
| [[NCI-H661 (line)]] | alt | 64.4 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.110× (z -9.1) |
| [[RPMI-7951 (line)]] | alt | 82.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.366× (z -8.8) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 81.9 | 0 | 1 | — | [[Drospirenone (drug)]] 0.5 µM 0.0754× (z -9.1) |
| [[SW1417 (line)]] | alt | 93.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.378× (z -11.0) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 84.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +8.9) ⚠ cell-cycle shift, explains ~22% of this change | — |
| [[A-172 (line)]] | wt | 95.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 83.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 64.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 147 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 82.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 70.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 79.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 99.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 99.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 90.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 76.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 105 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8435), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USE1]] | +0.73 | +0.69 / +0.70 | both halves | 7e-06 |  |
| [[ZKSCAN5]] | +0.70 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[BIN3]] | +0.69 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[BLZF1]] | +0.68 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[GPATCH2L]] | +0.67 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[KCTD5]] | +0.63 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[ZNF432]] | +0.63 | +0.63 / +0.57 | both halves | 8e-06 |  |
| [[TRIM39]] | +0.61 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[RECQL5]] | +0.61 | +0.60 / +0.63 | both halves | 7e-06 | ⚠ same locus (0.1 kb: neighbours can correlate without regulation) |
| [[FAM32A]] | +0.61 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[RAB7A]] | +0.60 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[MTF1]] | +0.60 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[ZNF324]] | +0.59 | +0.53 / +0.54 | both halves | 1e-05 | pathway: Epigenetic regulation of gene expression |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KDM1A]] | -0.62 | -0.53 / -0.66 | both halves | 1e-05 |  |
| [[TMEM123]] | -0.60 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[HSF2]] | -0.58 | -0.57 / -0.63 | both halves | 1e-05 |  |
| [[TMEM64]] | -0.57 | -0.62 / -0.55 | both halves | 1e-05 |  |
| [[CISD2]] | -0.57 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[TNPO1]] | -0.54 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[HDAC2]] | -0.54 | -0.47 / -0.51 | both halves | 2e-05 | pathway: Epigenetic regulation of gene expression; STRING 520 |
| [[HACD2]] | -0.53 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[NCKAP1]] | -0.53 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[NDUFV2]] | -0.53 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[RAD23B]] | -0.53 | -0.33 / -0.55 | both halves | 1e-04 |  |
| [[DRAM2]] | -0.52 | -0.52 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.529). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (17.7, -25.5); signed map (8.0, 15.9). **Vector** length 120, 40.7% of its response variance represented; |z| ≥ 3 in 1,290 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.6 | +5.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | +0.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.0 | +13.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.4 | +3.5 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.8 | +3.0 |
|  | [[Mifepristone (drug)]] 0.5 µM |  | +2.6 | +1.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +3.4 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -7.2 | -3.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.7 | -6.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -5.6 | -7.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | -5.4 | +3.6 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -5.4 | -1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.8 | -4.4 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -4.5 | -3.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.0 | -4.7 |

## What is on record

|  |  |
|---|---|
| Name | SAP30 binding protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.1 — chr17:75,667,251-75,708,062 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HCNGP, HTRG, HTRP |
| Reactome | 3 pathways, smallest: NoRC negatively regulates rRNA expression; Negative epigenetic regulation of rRNA expression; Epigenetic regulation of gene expression |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UHR5](https://www.uniprot.org/uniprotkb/Q9UHR5) (SAP30-binding protein):

> Plays a role in transcriptional repression by promoting histone deacetylase activity, leading to deacetylation of histone H3. Acts as a regulator of pre-mRNA splicing by facilitating assembly of the cyclin-L-CDK11 cyclin-dependent protein kinase complex, thereby promoting phosphorylation of SF3B1. May be involved in the regulation of beta-2-microglobulin genes (By similarity).; (Microbial infection) Involved in transcriptional repression of HHV-1 genes TK and gC.

**Summary**, from NCBI Gene [29115](https://www.ncbi.nlm.nih.gov/gene/29115):

> Enables cyclin-dependent protein serine/threonine kinase regulator activity. Involved in regulation of mRNA splicing, via spliceosome. Located in nucleoplasm. Is active in nuclear speck. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30785](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30785) · Entrez [29115](https://www.ncbi.nlm.nih.gov/gene/29115) · UniProt [Q9UHR5](https://www.uniprot.org/uniprotkb/Q9UHR5) · Ensembl [ENSG00000161526](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000161526)

## Data

Gene col 8435: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8435); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8435, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8435]; `tensor/DDL_lfc|DDL_z.npy` [8435]; `embed/gene_vectors.npy` [8435]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8435 or target_col == 8435). Every well: [[SAP30BP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SAP30BP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
