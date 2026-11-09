---
symbol: "DNM1L"
type: "gene"
col: 1506
ensembl_id: "ENSG00000087470"
name: "dynamin 1L"
location: "12p11.21"
module: 4
arm: "+"
pooled_cpm: 125.06
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 4
n_dd_up_clean: 6
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# DNM1L

*dynamin 1L* — 12p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (16 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.50× (z +14.5, q 1e-44, up in 32 of 48 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.62× (z +12.3, q 4e-32, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Ponatinib (drug)]] 5 µM: 0.787× (z -6.1, q 6e-07, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GALNT1]] (+0.59, fdr 1e-05), [[ACOT7]] (+0.59, fdr 1e-05), [[DLAT]] (+0.56, fdr 1e-05); moves opposite to [[BET1]] (-0.59, fdr 1e-05), [[HCG27]] (-0.59, fdr 2e-05), [[NR1H3]] (-0.57, fdr 2e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MIR3659HG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 18 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1506.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.50×** | +14.5 | 1e-44 | 32/48 (A498, Panc 03.27, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.62×** | +12.3 | 4e-32 | 43/48 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.57×** | +11.4 | 5e-28 | 44/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.56×** | +10.8 | 4e-25 | 37/48 (A498, Panc 03.27, …) | rises with dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.50×** | +9.7 | 4e-20 | 43/48 (PANC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.37×** | +8.0 | 1e-13 | 32/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **1.36×** | +7.4 | 1e-11 | 36/47 (LoVo, NCI-H460, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.31×** | +6.9 | 3e-10 | 30/48 (PANC-1, A498, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.31×** | +6.9 | 3e-10 | 31/48 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change | **1.31×** | +6.9 | 4e-10 | 27/49 (COLO 205, NCI-H23, …) | two highest doses | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.28×** | +6.3 | 1e-08 | 29/48 (PANC-1, HT-29, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.67×** | +6.3 | 2e-08 | 29/49 (NCI-H1573, HepG2/C3A, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.67×** | +6.2 | 2e-08 | 31/48 (C32, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | **1.25×** | +5.7 | 6e-07 | 26/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.35×** | +5.4 | 3e-06 | 34/49 (PANC-1, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Diphenhydramine (drug)]] 5 µM |  | 1.16× | +3.7 | 0.005 | 11/48 (HS-578T, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | 1.16× | +3.6 | 0.007 | 13/49 (H4, NCI-H460, …) | top dose only |  |
| [[Hexylresorcinol (drug)]] 0.5 µM |  | 1.14× | +3.3 | 0.020 | 3/49 (SK-MEL-2, NCI-H1573, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | 1.19× | +3.2 | 0.029 | 15/48 (SW1417, NCI-H2030, …) | two highest doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | 1.13× | +3.0 | 0.055 | 13/48 (A498, LOX-IMVI, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | 1.13× | +3.0 | 0.057 | 12/48 (MIA PaCa-2, SW 900, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1506.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **0.787×** | -6.1 | 6e-07 | 30/48 (J82, NCI-H23, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.882× | -4.5 | 0.002 | 17/49 (J82, A549, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.885× | -4.3 | 0.004 | 13/49 (SK-MEL-2, SW480, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.867× | -4.0 | 0.007 | 15/48 (LoVo, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.855× | -4.0 | 0.007 | 11/48 (KATO III, A-172, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | 0.850× | -4.0 | 0.007 | 20/50 (LoVo, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.899× | -3.8 | 0.010 | 16/48 (hTERT-HPNE, HOP62, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 0.862× | -3.8 | 0.011 | 17/48 (SW 900, AsPC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.814×** | -3.7 | 0.012 | 17/48 (SW 900, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.907× | -3.5 | 0.029 | 8/48 (NCI-H2347, SK-MEL-2, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.902× | -3.4 | 0.038 | 8/48 (SK-MEL-2, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.833×** | -3.3 | 0.038 | 17/48 (LS 180, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 0.878× | -3.3 | 0.038 | 12/48 (KATO III, HepG2/C3A, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.871× | -3.2 | 0.047 | 14/48 (LoVo, SK-MEL-2, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.886× | -3.1 | 0.078 | 10/49 (LoVo, HepG2/C3A, …) | all doses, flat |  |
| [[Cabozantinib (S-malate) (drug)]] 0.5 µM |  | 0.889× | -3.0 | 0.090 | 9/48 (HOP62, CHP-212, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.885× | -3.0 | 0.090 | 14/48 (AsPC-1, SW480, …) | all doses, flat |  |
| [[Resveratrol (drug)]] 0.5 µM |  | 0.890× | -3.0 | 0.090 | 6/49 (LOX-IMVI, Hs 766T, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.784×** | -3.0 | 0.090 | 18/50 (AsPC-1, NCI-H1573, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1506. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 93.4 | 8 (5 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.97× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.69× (z +9.5) | — |
| [[NCI-H460 (line)]] | wt | 111 | 6 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 2.06× (z +12.1) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 1.69× (z +8.8) | — |
| [[PANC-1 (line)]] | alt | 123 | 5 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 1.93× (z +12.1) | — |
| [[LS 180 (line)]] | wt | 98.8 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +10.2) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.06× (z +8.6) | — |
| [[NCI-H23 (line)]] | alt | 169 | 2 (2 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.06× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change | [[Homoharringtonine (drug)]] 5 µM 0.605× (z -11.1) ⚠ cell-cycle shift, explains ~30% of this change |
| [[SW480 (line)]] | alt | 169 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.61× (z +12.8) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 1.67× (z +9.6) | — |
| [[A-427 (line)]] | wt | 176 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.83× (z +9.6) | [[Dinaciclib (drug)]] 0.05 µM 0.461× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 96.8 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +21.6) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[LoVo (line)]] | wt | 161 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +13.2) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[Panc 03.27 (line)]] | alt | 119 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +17.5) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[C-33 A (line)]] | alt | 129 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.66× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.05 µM 0.482× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 90.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +14.0) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.17× (z +8.7) | — |
| [[COLO 205 (line)]] | alt | 47.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.51× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change | — |
| [[HOP62 (line)]] | alt | 209 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +14.3) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 1.87× (z +8.8) | — |
| [[HT-29 (line)]] | alt | 72.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +12.5) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.54× (z +8.8) | — |
| [[KATO III (line)]] | alt | 93.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +9.7) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.24× (z +8.9) | — |
| [[SW1417 (line)]] | alt | 127 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +13.5) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[A549 (line)]] | wt | 137 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +10.1) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[AsPC-1 (line)]] | alt | 143 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +15.1) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[CFPAC-1 (line)]] | alt | 43.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +11.3) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[HEC-1-A (line)]] | alt | 101 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +10.4) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 96.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +12.0) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[J82 (line)]] | alt | 150 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.504× (z -16.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 127 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 1.99× (z +9.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 201 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.01× (z +9.3) | — |
| [[NCI-H1792 (line)]] | alt | 83.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +14.9) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H2347 (line)]] | alt | 78.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.62× (z +8.7) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[SNU-1 (line)]] | wt | 130 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.338× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 108 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.14× (z +8.8) ⚠ toxic; cell-cycle shift, explains ~36% of this change | — |
| [[SW 900 (line)]] | alt | 305 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +9.4) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[A-172 (line)]] | wt | 88.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 143 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 128 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 96.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 95.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 185 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 75.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 175 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 65.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 182 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 99.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 84.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 168 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 148 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1506), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*52 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GALNT1]] | +0.59 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[ACOT7]] | +0.59 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[DLAT]] | +0.56 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[CCT2]] | +0.55 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[RAP1GDS1]] | +0.55 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[HERC2]] | +0.55 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[USP14]] | +0.54 | +0.50 / +0.52 | both halves | 1e-05 | STRING 485 |
| [[IMMT]] | +0.52 | +0.46 / +0.52 | both halves | 3e-05 | STRING 798 |
| [[NIN]] | +0.52 | +0.43 / +0.49 | both halves | 4e-05 |  |
| [[FARP1]] | +0.52 | +0.43 / +0.55 | both halves | 4e-05 |  |
| [[PRPS1]] | +0.51 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[GALNT10]] | +0.51 | +0.34 / +0.53 | both halves | 1e-04 |  |

## Genes that move opposite

*48 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BET1]] | -0.59 | -0.54 / -0.58 | both halves | 1e-05 | pathway: HALLMARK_PROTEIN_SECRETION |
| [[HCG27]] | -0.59 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[NR1H3]] | -0.57 | -0.48 / -0.60 | both halves | 2e-05 |  |
| [[ZNNT1]] | -0.57 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[UPP2]] | -0.54 | -0.38 / -0.49 | both halves | 6e-05 |  |
| [[VPS13B-DT]] | -0.54 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[FAM117A]] | -0.53 | -0.46 / -0.40 | both halves | 4e-05 |  |
| [[MITD1]] | -0.53 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[TERF2IP]] | -0.53 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[TNFRSF14]] | -0.53 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[LINC02100]] | -0.53 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[ISCU]] | -0.51 | -0.51 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MIR3659HG]] | B | MIR3659HG activity raises DNM1L's level | lines that do not express MIR3659HG (5) vs lines expressing it (45) | 1.70× lower at baseline in the lines without MIR3659HG | 0.036 | ⚠ within organs, on part of the lines; also absent: USP31, ZNF594, WHRN; maybe low, not absent |
| [[PIK3CB]] | B | PIK3CB activity raises DNM1L's level | compounds that target PIK3CB: 2 of 3 lower it (Bimiralisib, GSK1059615) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets |
| [[AGTPBP1]] | C | AGTPBP1 activity raises DNM1L's level | lines that do not express AGTPBP1 (3) vs lines expressing it (47) | 1.68× lower at baseline in the lines without AGTPBP1 | 0.076 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: USP31, ENSG00000232732; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.497). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (23.5, -26.5); signed map (-18.0, -48.6). **Vector** length 101, 29.4% of its response variance represented; |z| ≥ 3 in 1,300 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +5.3 | +12.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.1 | +11.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change | +4.9 | +6.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +4.6 | +4.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.5 | +9.7 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +3.4 | +3.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.3 | +0.4 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | +2.7 | +1.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.7 | +5.4 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.6 | -0.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.2 | -6.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | -4.0 | +5.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.0 | -4.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | -3.6 | +5.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.7 | -2.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.3 | -4.0 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -2.3 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | dynamin 1L |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p11.21 — chr12:32,679,200-32,745,650 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DRP1, DVLP, HDYNIV, DYMPLE, VPS1 |
| Gene groups (HGNC) | Dynamin superfamily |
| Hallmark sets | PROTEIN_SECRETION, APOPTOSIS |
| Reactome | 3 pathways, smallest: Apoptotic execution phase; Apoptosis; Programmed Cell Death |
| Matched by | ensembl_id |

**Function**, from UniProt [O00429](https://www.uniprot.org/uniprotkb/O00429) (Dynamin-1-like protein):

> Functions in mitochondrial and peroxisomal division. Mediates membrane fission through oligomerization into membrane-associated tubular structures that wrap around the scission site to constrict and sever the mitochondrial membrane through a GTP hydrolysis-dependent mechanism. The specific recruitment at scission sites is mediated by membrane receptors like MFF, MIEF1 and MIEF2 for mitochondrial membranes. While the recruitment by the membrane receptors is GTP-dependent, the following …

**Summary**, from NCBI Gene [10059](https://www.ncbi.nlm.nih.gov/gene/10059):

> This gene encodes a member of the dynamin superfamily of GTPases. The encoded protein mediates mitochondrial and peroxisomal division, and is involved in developmentally regulated apoptosis and programmed necrosis. Dysfunction of this gene is implicated in several neurological disorders, including Alzheimer's disease. Mutations in this gene are associated with the autosomal dominant disorder, encephalopathy, lethal, due to defective mitochondrial and peroxisomal fission (EMPF). Alternative …

**Accessions** — [HGNC:2973](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2973) · Entrez [10059](https://www.ncbi.nlm.nih.gov/gene/10059) · UniProt [O00429](https://www.uniprot.org/uniprotkb/O00429) · Ensembl [ENSG00000087470](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000087470)

## Data

Gene col 1506: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1506); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1506, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1506]; `tensor/DDL_lfc|DDL_z.npy` [1506]; `embed/gene_vectors.npy` [1506]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1506 or target_col == 1506). Every well: [[DNM1L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNM1L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
