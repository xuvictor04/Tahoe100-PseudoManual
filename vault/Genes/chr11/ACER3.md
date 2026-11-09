---
symbol: "ACER3"
type: "gene"
col: 1210
ensembl_id: "ENSG00000078124"
name: "alkaline ceramidase 3"
location: "11q13.5"
module: 151
arm: "+"
pooled_cpm: 111.53
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 19
n_dd_up_clean: 6
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/151"]
generated_by: "tahoemap"
---

# ACER3

*alkaline ceramidase 3* — 11q13.5

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.60× (z +10.5, q 6e-23, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.631× (z -9.9, q 3e-20, down in 25 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 0.755× (z -6.3, q 7e-08, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBASH3B]] (+0.61, fdr 7e-06), [[AMOTL1]] (+0.59, fdr 1e-05), [[ITGB5]] (+0.56, fdr 1e-05); moves opposite to [[COPS5]] (-0.57, fdr 2e-05), [[OSER1]] (-0.57, fdr 1e-05), [[MED6]] (-0.53, fdr 2e-05).
> It is in [[Module 151]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[NR2E3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1210.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.60×** | +10.5 | 6e-23 | 40/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.42×** | +7.9 | 9e-13 | 33/48 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.40×** | +7.6 | 7e-12 | 32/48 (BT-474, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.37×** | +6.8 | 2e-09 | 29/48 (NCI-H2347, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **1.30×** | +5.8 | 9e-07 | 25/48 (BT-474, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.29×** | +5.7 | 1e-06 | 26/48 (A498, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.20× | +5.7 | 1e-06 | 23/48 (HT-29, A498, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.29×** | +5.6 | 1e-06 | 28/48 (RKO, LoVo, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **1.26×** | +5.1 | 2e-05 | 27/48 (A498, HT-29, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.24×** | +4.5 | 4e-04 | 21/47 (SW480, C32, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +4.0 | 0.003 | 22/48 (NCI-H2347, SW480, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~95% of this change | 1.19× | +3.9 | 0.004 | 22/48 (A498, NCI-H2347, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | 1.19× | +3.9 | 0.004 | 21/48 (PANC-1, SW 900, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.2 | 0.055 | 22/49 (HT-29, A498, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.32×** | +3.2 | 0.055 | 11/48 (SW480, C32, …) | top dose only | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.15× | +3.1 | 0.061 | 14/48 (HS-578T, SW480, …) | top dose only |  |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM |  | 1.15× | +3.0 | 0.075 | 14/48 (HEC-1-A, AN3 CA, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1210.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.631×** | -9.9 | 3e-20 | 25/44 (A-427, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.750×** | -6.4 | 4e-08 | 28/49 (RKO, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.755×** | -6.3 | 7e-08 | 29/48 (Hs 766T, A-172, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.756×** | -6.2 | 7e-08 | 28/48 (A-427, J82, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.779×** | -6.0 | 2e-07 | 26/50 (Hs 766T, C32, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.766×** | -5.9 | 2e-07 | 27/48 (HEC-1-A, LOX-IMVI, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **0.592×** | -5.9 | 2e-07 | 31/47 (Hs 766T, AsPC-1, …) | top dose only | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.809×** | -5.5 | 3e-06 | 24/48 (Hs 766T, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.624×** | -5.3 | 6e-06 | 27/49 (LOX-IMVI, LS 180, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.847× | -5.2 | 9e-06 | 22/49 (J82, Panc 03.27, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.793×** | -5.0 | 3e-05 | 27/48 (NCI-H460, C32, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.807×** | -4.8 | 8e-05 | 25/49 (C32, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | 0.865× | -4.6 | 2e-04 | 20/48 (C32, RPMI-7951, …) | top dose only |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.832×** | -4.5 | 3e-04 | 20/49 (C32, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.810×** | -4.3 | 6e-04 | 21/45 (A-427, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.768×** | -4.2 | 9e-04 | 23/47 (SW48, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.856× | -4.0 | 0.002 | 19/48 (C32, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.782×** | -3.9 | 0.003 | 20/48 (Panc 03.27, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.847× | -3.7 | 0.006 | 19/48 (KATO III, HOP62, …) | rises with dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | 0.843× | -3.6 | 0.009 | 18/48 (Hs 766T, C32, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.890× | -3.6 | 0.010 | 17/49 (Hs 766T, C32, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1210. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 181 | 0 | 17 (5 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.380× (z -12.4) |
| [[NCI-H460 (line)]] | wt | 149 | 0 | 13 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.359× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Trametinib (drug)]] 0.5 µM 0.443× (z -11.0) |
| [[Hs 766T (line)]] | wt | 171 | 0 | 9 (1 ⚠) | — | [[Cobimetinib (drug)]] 5 µM 0.220× (z -12.6) |
| [[A498 (line)]] | wt | 46.8 | 6 (5 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +13.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.62× (z +8.8) | — |
| [[LOX-IMVI (line)]] | wt | 148 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -22.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.384× (z -9.6) |
| [[NCI-H2347 (line)]] | alt | 62.4 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +20.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.84× (z +12.8) | — |
| [[A-172 (line)]] | wt | 182 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -14.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 104 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.05× (z +13.3) | — |
| [[J82 (line)]] | alt | 208 | 0 | 5 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.487× (z -13.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 97.3 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +15.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.59× (z +15.6) | — |
| [[SHP-77 (line)]] | alt | 92.8 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.09× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.266× (z -13.8) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 167 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +13.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.75× (z +13.0) | [[Dinaciclib (drug)]] 0.5 µM 0.422× (z -11.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 132 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.214× (z -21.8) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 75.8 | 3 (2 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 2.16× (z +11.4) | — |
| [[Panc 03.27 (line)]] | alt | 178 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.284× (z -14.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 114 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.58× (z +9.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 1.81× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.607× (z -10.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 80.9 | 0 | 3 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.349× (z -9.5) ⚠ cell-cycle shift, explains ~99% of this change · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.400× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 133 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.513× (z -9.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.531× (z -9.0) |
| [[KATO III (line)]] | alt | 94.5 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.27× (z +14.5) | — |
| [[LS 180 (line)]] | wt | 105 | 2 (2 ⚠) | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 3.15× (z +13.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SNU-1 (line)]] | wt | 92.0 | 1 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.59× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.177× (z -16.0) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 151 | 0 | 1 (1 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.396× (z -9.5) ⚠ cell-cycle shift, explains ~17% of this change |
| [[CFPAC-1 (line)]] | alt | 140 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.525× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 31.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.43× (z +9.2) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 52.4 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.08× (z +10.5) | — |
| [[LoVo (line)]] | wt | 100 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.26× (z +10.8) | — |
| [[NCI-H2030 (line)]] | alt | 135 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.490× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 213 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.451× (z -9.7) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 121 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0885× (z -32.5) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 218 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.168× (z -8.8) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 50.7 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.81× (z +8.7) | — |
| [[A549 (line)]] | wt | 162 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 128 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 113 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 50.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 52.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 67.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 67.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 47.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 87.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 76.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 73.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 86.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 98.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 63.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 96.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 84.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1210), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBASH3B]] | +0.61 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[AMOTL1]] | +0.59 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[ITGB5]] | +0.56 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[NT5E]] | +0.56 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[SRPK1]] | +0.56 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[CALM1]] | +0.55 | +0.57 / +0.46 | both halves | 3e-05 |  |
| [[S100A16]] | +0.55 | +0.53 / +0.43 | both halves | 3e-05 |  |
| [[EIF5A2]] | +0.55 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[GALNT18]] | +0.55 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[COL13A1]] | +0.55 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[SH3BGRL3]] | +0.54 | +0.55 / +0.44 | both halves | 3e-05 |  |
| [[DOCK4]] | +0.54 | +0.50 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COPS5]] | -0.57 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[OSER1]] | -0.57 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[MED6]] | -0.53 | -0.52 / -0.46 | both halves | 2e-05 |  |
| [[CDKN1B]] | -0.51 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[COPS2]] | -0.51 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[MBNL2]] | -0.49 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[CIR1]] | -0.48 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[CLIP3]] | -0.48 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[ADAM20]] | -0.48 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[ABHD4]] | -0.48 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[FBXO8]] | -0.47 | -0.55 / -0.34 | both halves | 1e-04 |  |
| [[ADAM20P1]] | -0.47 | -0.45 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR2E3]] | B | NR2E3 activity raises ACER3's level | lines that do not express NR2E3 (23) vs lines expressing it (27) | 1.51× lower at baseline in the lines without NR2E3 | 0.007 | ⚠ within organs, on part of the lines; also absent: THSD4, SLC35F3, MPV17L |
| [[THSD4]] | B | THSD4 activity raises ACER3's level | lines that do not express THSD4 (18) vs lines expressing it (32) | 1.44× lower at baseline in the lines without THSD4 | 0.034 | ⚠ within organs, on part of the lines; also absent: NR2E3, EDN1, CLDN1 |
| [[PIK3CA]] | B | PIK3CA activity raises ACER3's level | compounds that target PIK3CA: 3 of 4 lower it (Alpelisib, Bimiralisib, GSK1059615) | 75% of the class's compounds vs 3.9% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[SDC3]] | C | SDC3 activity raises ACER3's level | lines that do not express SDC3 (4) vs lines expressing it (46) | 2.07× lower at baseline in the lines without SDC3 | 0.054 | ⚠ few lines (4 vs 46); across organs |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 151]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.553). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (47.2, 7.2); signed map (5.6, 48.3). **Vector** length 135, 41.5% of its response variance represented; |z| ≥ 3 in 1,610 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +5.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.3 | +5.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.1 | +1.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | +3.8 | +5.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.4 | +3.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.6 | +3.1 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +2.5 | +2.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.4 | +3.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.4 | +0.8 |
| fall | [[NG25 (drug)]] 5 µM |  | -6.6 | -5.9 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | -6.5 | -6.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | -6.5 | -5.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.9 | -5.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -5.4 | -4.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.3 | -0.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -5.1 | -6.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -5.0 | -5.0 |

## What is on record

|  |  |
|---|---|
| Name | alkaline ceramidase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.5 — chr11:76,860,859-77,026,797 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11238, APHC; previously PHCA |
| Gene groups (HGNC) | Alkaline ceramidases |
| Reactome | 3 pathways, smallest: Sphingolipid catabolism; Sphingolipid metabolism; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NUN7](https://www.uniprot.org/uniprotkb/Q9NUN7) (Alkaline ceramidase 3):

> Endoplasmic reticulum and Golgi ceramidase that catalyzes the hydrolysis of unsaturated long-chain C18:1-, C20:1- and C20:4-ceramides, dihydroceramides and phytoceramides into sphingoid bases like sphingosine and free fatty acids at alkaline pH. Ceramides, sphingosine, and its phosphorylated form sphingosine-1-phosphate are bioactive lipids that mediate cellular signaling pathways regulating several biological processes including cell proliferation, apoptosis and differentiation. Controls the …

**Summary**, from NCBI Gene [55331](https://www.ncbi.nlm.nih.gov/gene/55331):

> Enables N-acylsphingosine amidohydrolase activity; calcium ion binding activity; and zinc ion binding activity. Involved in several processes, including myelination; positive regulation of cell population proliferation; and sphingolipid metabolic process. Located in Golgi membrane and endoplasmic reticulum membrane. Biomarker of hepatocellular carcinoma and metabolic dysfunction-associated steatohepatitis. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16066](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16066) · Entrez [55331](https://www.ncbi.nlm.nih.gov/gene/55331) · UniProt [Q9NUN7](https://www.uniprot.org/uniprotkb/Q9NUN7) · Ensembl [ENSG00000078124](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000078124)

## Data

Gene col 1210: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1210); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1210, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1210]; `tensor/DDL_lfc|DDL_z.npy` [1210]; `embed/gene_vectors.npy` [1210]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1210 or target_col == 1210). Every well: [[ACER3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACER3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
