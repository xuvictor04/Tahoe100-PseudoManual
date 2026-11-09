---
symbol: "FOSL1"
type: "gene"
col: 10628
ensembl_id: "ENSG00000175592"
name: "FOS like 1, AP-1 transcription factor subunit"
location: "11q13.1"
module: 158
arm: "+"
pooled_cpm: 176.44
n_lines_expressing: 45
n_dd_up: 27
n_dd_down: 49
n_dd_up_clean: 15
n_dd_down_clean: 46
in_vector_space: true
direction_upstream: 31
direction_downstream: 23
tags: ["gene", "module/158"]
generated_by: "tahoemap"
---

# FOSL1

*FOS like 1, AP-1 transcription factor subunit* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.37× (z +20.7, q 0e+00, up in 40 of 43 measured lines) ⚠ cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 20.8× (z +15.7, q 0e+00, up in 44 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 49 drug-doses (3 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 0.217× (z -15.4, q 0e+00, down in 44 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PHLDA1]] (+0.73, fdr 7e-06), [[MYEOV]] (+0.73, fdr 7e-06), [[EGR1]] (+0.72, fdr 7e-06).
> It is in [[Module 158]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 31 arrows point to it, the strongest [[GPR39]] → it (grade B ⚠); 23 go from it, the strongest it → [[NT5E]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 12 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10628.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **4.37×** | +20.7 | 0e+00 | 40/43 (AsPC-1, A549, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **20.8×** | +15.7 | 0e+00 | 44/44 (PANC-1, MIA PaCa-2, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **4.13×** | +13.5 | 2e-39 | 40/43 (A549, NCI-H1573, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **7.54×** | +10.5 | 2e-23 | 36/43 (HEC-1-A, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.77×** | +10.1 | 7e-22 | 38/42 (A549, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.55×** | +8.2 | 2e-14 | 35/43 (A549, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **2.24×** | +8.0 | 9e-14 | 38/43 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **2.22×** | +7.9 | 1e-13 | 37/43 (SW480, KATO III, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **2.05×** | +7.2 | 5e-11 | 37/43 (NCI-H1573, NCI-H460, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.03×** | +6.5 | 4e-09 | 30/40 (HS-578T, MIA PaCa-2, …) | inconsistent across doses | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.82×** | +5.9 | 2e-07 | 33/43 (A549, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.71×** | +5.3 | 5e-06 | 29/43 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.67×** | +5.1 | 2e-05 | 27/43 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.31×** | +4.3 | 6e-04 | 24/34 (HOP62, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **1.47×** | +3.7 | 0.007 | 27/42 (KATO III, HT-29, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.5 µM |  | **1.72×** | +3.6 | 0.011 | 23/43 (HEC-1-A, A-172, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.42×** | +3.5 | 0.015 | 21/43 (KATO III, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.85×** | +3.2 | 0.041 | 25/43 (A549, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **1.39×** | +3.2 | 0.042 | 26/43 (SW480, hTERT-HPNE, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.37×** | +3.1 | 0.050 | 22/43 (KATO III, NCI-H1573, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.81×** | +3.1 | 0.050 | 22/43 (Hs 766T, HEC-1-A, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.55×** | +2.9 | 0.073 | 22/43 (NCI-H2030, A498, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Isocorydine (drug)]] 0.05 µM |  | **1.34×** | +2.9 | 0.073 | 21/43 (SW 900, Panc 03.27, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.23×** | +2.9 | 0.073 | 22/44 (KATO III, HT-29, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 49 in all, 3 with an alert ⚠; shown: the 15 strongest. 49 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10628.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM |  | **0.217×** | -15.4 | 0e+00 | 44/45 (MIA PaCa-2, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.236×** | -13.7 | 5e-40 | 40/42 (AsPC-1, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.256×** | -12.9 | 7e-36 | 43/43 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.354×** | -12.2 | 3e-32 | 42/43 (SW480, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.471×** | -10.4 | 5e-23 | 41/43 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.324×** | -10.3 | 9e-23 | 42/43 (SW480, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.372×** | -10.3 | 9e-23 | 41/44 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.318×** | -10.0 | 1e-21 | 41/44 (NCI-H23, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.389×** | -9.3 | 1e-18 | 39/43 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.400×** | -9.0 | 1e-17 | 37/43 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.474×** | -8.8 | 8e-17 | 39/43 (MIA PaCa-2, NCI-H2347, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.375×** | -8.6 | 6e-16 | 39/42 (MIA PaCa-2, C32, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.419×** | -8.5 | 6e-16 | 40/43 (KATO III, NCI-H23, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.542×** | -8.5 | 8e-16 | 35/44 (PANC-1, SW48, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Bimiralisib (drug)]] 5 µM |  | **0.232×** | -7.5 | 2e-12 | 39/45 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.84 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10628. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 238 | 6 (3 ⚠) | 18 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.19× (z +21.9) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 26.9× (z +14.6) | [[Adagrasib (drug)]] 0.05 µM 0.351× (z -30.3) ⚠ position not correctable · without an alert: [[Trametinib (drug)]] 5 µM 0.116× (z -18.3) |
| [[PANC-1 (line)]] | alt | 344 | 4 (2 ⚠) | 19 | [[TAK-901 (drug)]] 5 µM 20.5× (z +14.6) | [[Panobinostat (drug)]] 5 µM 0.126× (z -19.1) |
| [[C32 (line)]] | wt | 241 | 7 (3 ⚠) | 11 | [[Homoharringtonine (drug)]] 5 µM 4.91× (z +15.6) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 5.39× (z +10.3) | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.156× (z -12.3) |
| [[NCI-H23 (line)]] | alt | 95.1 | 2 (1 ⚠) | 16 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +10.0) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 11.3× (z +8.7) | [[Adagrasib (drug)]] 0.05 µM 0.417× (z -19.9) ⚠ position not correctable · without an alert: [[Trametinib (drug)]] 5 µM 0.0900× (z -16.5) |
| [[HEC-1-A (line)]] | alt | 187 | 3 (1 ⚠) | 14 | [[TAK-901 (drug)]] 5 µM 29.2× (z +14.2) | [[Trametinib (drug)]] 5 µM 0.142× (z -16.2) |
| [[NCI-H1573 (line)]] | alt | 197 | 9 (7 ⚠) | 6 | [[Homoharringtonine (drug)]] 5 µM 7.00× (z +19.3) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 38.1× (z +13.3) | [[Cobimetinib (drug)]] 5 µM 0.134× (z -13.4) |
| [[Panc 03.27 (line)]] | alt | 225 | 6 (3 ⚠) | 9 | [[Homoharringtonine (drug)]] 5 µM 8.40× (z +21.6) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 23.8× (z +11.9) | [[Cobimetinib (drug)]] 5 µM 0.155× (z -12.8) |
| [[A-427 (line)]] | wt | 99.8 | 8 (3 ⚠) | 6 | [[Homoharringtonine (drug)]] 5 µM 4.69× (z +17.8) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 25.1× (z +13.7) | [[Trametinib (drug)]] 5 µM 0.230× (z -11.4) |
| [[AsPC-1 (line)]] | alt | 423 | 7 (6 ⚠) | 7 | [[Homoharringtonine (drug)]] 5 µM 9.22× (z +25.0) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 13.2× (z +10.7) | [[Cobimetinib (drug)]] 5 µM 0.141× (z -14.9) |
| [[NCI-H2347 (line)]] | alt | 151 | 2 (1 ⚠) | 12 | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +11.8) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 12.4× (z +9.0) | [[Trametinib (drug)]] 5 µM 0.139× (z -13.6) |
| [[SW480 (line)]] | alt | 152 | 3 | 11 | [[TAK-901 (drug)]] 5 µM 27.7× (z +12.4) | [[Trametinib (drug)]] 0.5 µM 0.167× (z -15.3) |
| [[A549 (line)]] | wt | 178 | 8 (5 ⚠) | 5 | [[Homoharringtonine (drug)]] 5 µM 9.63× (z +22.8) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 11.7× (z +15.5) | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.178× (z -11.8) |
| [[Hs 766T (line)]] | wt | 255 | 3 (2 ⚠) | 10 | [[Homoharringtonine (drug)]] 5 µM 6.64× (z +18.5) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 54.3× (z +14.4) | [[Trametinib (drug)]] 5 µM 0.160× (z -13.1) |
| [[NCI-H460 (line)]] | wt | 109 | 13 (10 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.00× (z +16.5) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 10.3× (z +12.4) | — |
| [[LoVo (line)]] | wt | 154 | 2 (1 ⚠) | 9 | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +12.2) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 15.9× (z +10.1) | [[Trametinib (drug)]] 5 µM 0.162× (z -13.3) |
| [[LOX-IMVI (line)]] | wt | 213 | 4 (2 ⚠) | 7 | [[TAK-901 (drug)]] 5 µM 19.1× (z +12.8) | [[Trametinib (drug)]] 5 µM 0.231× (z -12.7) |
| [[SK-MEL-2 (line)]] | alt | 90.6 | 3 (1 ⚠) | 8 | [[TAK-901 (drug)]] 5 µM 21.2× (z +11.0) | [[Trametinib (drug)]] 5 µM 0.151× (z -13.2) |
| [[SNU-423 (line)]] | alt | 137 | 7 (5 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 8.98× (z +22.2) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 32.0× (z +12.9) | [[Cobimetinib (drug)]] 5 µM 0.215× (z -10.5) |
| [[SW48 (line)]] | wt | 367 | 1 | 10 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 11.6× (z +9.3) | [[Trametinib (drug)]] 5 µM 0.0907× (z -17.0) |
| [[HOP62 (line)]] | alt | 206 | 3 (1 ⚠) | 7 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 34.7× (z +12.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.301× (z -11.5) |
| [[KATO III (line)]] | alt | 108 | 6 (2 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +11.3) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 4.80× (z +9.7) | [[Ponatinib (drug)]] 5 µM 0.125× (z -12.7) |
| [[HCT15 (line)]] | alt | 113 | 0 | 9 | — | [[Trametinib (drug)]] 5 µM 0.138× (z -13.4) |
| [[HS-578T (line)]] | alt | 175 | 6 (4 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 5.73× (z +17.4) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 40.9× (z +13.7) | [[Trametinib (drug)]] 5 µM 0.248× (z -10.3) |
| [[A498 (line)]] | wt | 92.9 | 4 (2 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 4.83× (z +17.6) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 18.6× (z +12.0) | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.256× (z -10.3) |
| [[NCI-H2030 (line)]] | alt | 86.5 | 7 (5 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.56× (z +16.1) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 52.7× (z +13.7) | [[Adagrasib (drug)]] 0.05 µM 0.614× (z -10.6) ⚠ position not correctable |
| [[LS 180 (line)]] | wt | 193 | 1 | 6 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 12.9× (z +8.8) | [[Ponatinib (drug)]] 5 µM 0.207× (z -10.1) |
| [[RPMI-7951 (line)]] | alt | 201 | 4 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 4.35× (z +13.3) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 32.3× (z +11.6) | [[Trametinib (drug)]] 5 µM 0.201× (z -10.1) |
| [[SW 900 (line)]] | alt | 163 | 5 (3 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 4.87× (z +14.8) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 36.9× (z +12.4) | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.184× (z -10.7) |
| [[hTERT-HPNE (line)]] | wt | 154 | 5 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 5.46× (z +17.6) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 27.9× (z +12.8) | [[Panobinostat (drug)]] 5 µM 0.312× (z -8.5) |
| [[SW1417 (line)]] | alt | 219 | 1 (1 ⚠) | 5 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +11.9) ⚠ cell-cycle shift, explains ~39% of this change | [[Trametinib (drug)]] 5 µM 0.244× (z -10.7) |
| [[J82 (line)]] | alt | 321 | 1 | 4 | [[TAK-901 (drug)]] 5 µM 12.8× (z +11.4) | [[Panobinostat (drug)]] 0.5 µM 0.165× (z -15.5) |
| [[RKO (line)]] | wt | 259 | 2 | 3 | [[TAK-901 (drug)]] 5 µM 8.85× (z +11.5) | [[Panobinostat (drug)]] 0.5 µM 0.323× (z -11.3) |
| [[A-172 (line)]] | wt | 166 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.28× (z +11.6) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 37.6× (z +10.7) | — |
| [[NCI-H1792 (line)]] | alt | 105 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.45× (z +14.9) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 7.33× (z +10.0) | — |
| [[CFPAC-1 (line)]] | alt | 300 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 6.75× (z +16.4) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 26.5× (z +10.4) | [[Trametinib (drug)]] 5 µM 0.240× (z -8.5) |
| [[HT-29 (line)]] | alt | 175 | 0 | 3 | — | [[Ponatinib (drug)]] 5 µM 0.173× (z -9.4) |
| [[COLO 205 (line)]] | alt | 102 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 7.08× (z +11.0) ⚠ cell-cycle shift, explains ~39% of this change | [[Trametinib (drug)]] 5 µM 0.121× (z -8.7) |
| [[H4 (line)]] | wt | 176 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 40.3× (z +12.7) | — |
| [[AN3 CA (line)]] | alt | 47.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.9× (z +10.7) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[HepG2_C3A (line)]] | wt | 84.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.36× (z +11.4) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[SW 1271 (line)]] | alt | 88.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.13× (z +10.4) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[BT-474 (line)]] | alt | 24.5 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 17.2 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 55.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 158 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.1 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 11.4 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 30.0 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 196 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10628), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHLDA1]] | +0.73 | +0.74 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[MYEOV]] | +0.73 | +0.71 / +0.74 | both halves | 7e-06 |  |
| [[EGR1]] | +0.72 | +0.72 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 862 |
| [[SHB]] | +0.72 | +0.72 / +0.72 | both halves | 7e-06 |  |
| [[ERCC1]] | +0.69 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[BCAN-AS2]] | +0.69 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[EHD1]] | +0.68 | +0.73 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[EPHA2]] | +0.68 | +0.67 / +0.68 | both halves | 7e-06 | STRING 505 |
| [[EGR3]] | +0.68 | +0.66 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 702 |
| [[IER2]] | +0.68 | +0.67 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[SPRY4]] | +0.67 | +0.65 / +0.73 | both halves | 7e-06 |  |
| [[LIF]] | +0.67 | +0.71 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*31 arrows, 31 of them with an alert ⚠; grade A 0, B 26, C 5. Shown: the 12 strongest; 19 more arrows (19 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPR39]] | B | GPR39 activity raises FOSL1's level | lines that do not express GPR39 (11) vs lines expressing it (39) | 2.34× lower at baseline in the lines without GPR39 | 0.006 | ⚠ within organs, on part of the lines; also absent: MET, AHR, ABCC3 |
| [[UBASH3B]] | B | UBASH3B activity raises FOSL1's level | lines that do not express UBASH3B (7) vs lines expressing it (43) | 2.21× lower at baseline in the lines without UBASH3B | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000284969, CD59, MAMLD1 |
| [[LINC02454]] | B | LINC02454 activity raises FOSL1's level | lines that do not express LINC02454 (12) vs lines expressing it (38) | 2.06× lower at baseline in the lines without LINC02454 | 0.020 | ⚠ within organs, on part of the lines; also absent: PAPLN, LGALS1, SCHIP1; maybe low, not absent |
| [[CD44]] | B | CD44 activity raises FOSL1's level | lines that do not express CD44 (15) vs lines expressing it (35) | 2.94× lower at baseline in the lines without CD44 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: GBP3, CLEC2B, ADAMTS16 |
| [[KCNN4]] | B | KCNN4 activity raises FOSL1's level | lines that do not express KCNN4 (12) vs lines expressing it (38) | 1.98× lower at baseline in the lines without KCNN4 | 0.030 | ⚠ within organs, on part of the lines; also absent: RP1, GSPT2, GALC |
| [[TOR4A]] | B | TOR4A activity raises FOSL1's level | lines that do not express TOR4A (14) vs lines expressing it (36) | 2.38× lower at baseline in the lines without TOR4A | 0.033 | ⚠ within organs, on part of the lines; also absent: PLEKHA6, CDCP1, C19orf33 |
| [[PLAU]] | B | PLAU activity raises FOSL1's level | lines that do not express PLAU (26) vs lines expressing it (24) | 2.05× lower at baseline in the lines without PLAU | 0.036 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, C3, VGLL3 |
| [[ITGB1-DT]] | B | ITGB1-DT activity raises FOSL1's level | lines that do not express ITGB1-DT (21) vs lines expressing it (29) | 1.92× lower at baseline in the lines without ITGB1-DT | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000282849, LTBP2, ADTRP; maybe low, not absent |
| [[ANTXR2]] | B | ANTXR2 activity raises FOSL1's level | lines that do not express ANTXR2 (10) vs lines expressing it (40) | 2.39× lower at baseline in the lines without ANTXR2 | 0.045 | ⚠ within organs, on part of the lines; also absent: RIN2, LINC01291, ST3GAL1; maybe low, not absent |
| [[NT5E]] | B | NT5E activity raises FOSL1's level | lines that do not express NT5E (14) vs lines expressing it (36) | 2.03× lower at baseline in the lines without NT5E | 0.048 | ⚠ within organs, on part of the lines; also absent: MDFIC, PAPSS2, ENSG00000289526 |
| [[CD82]] | B | CD82 activity raises FOSL1's level | lines that do not express CD82 (11) vs lines expressing it (39) | 2.61× lower at baseline in the lines without CD82 | 0.049 | ⚠ within organs, on part of the lines; also absent: ITGA3, GBP3, CXCL3; maybe low, not absent |
| [[CDCP1]] | B | CDCP1 activity raises FOSL1's level | lines that do not express CDCP1 (16) vs lines expressing it (34) | 2.02× lower at baseline in the lines without CDCP1 | 0.061 | ⚠ within organs, on part of the lines; also absent: PTK6, TNK1, CHMP4C |

### Downstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 21, C 2. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NT5E]] | B | FOSL1 activity raises NT5E's level | lines that do not express FOSL1 (5) vs lines expressing it (45) | 7.14× lower at baseline in the lines without FOSL1 | 0.060 | ⚠ within organs, on part of the lines; also absent: PLS3, ENSG00000281883, NIBAN2; its own permutation p |
| [[ITGA2]] | B | FOSL1 activity raises ITGA2's level | lines that do not express FOSL1 (5) vs lines expressing it (45) | 6.10× lower at baseline in the lines without FOSL1 | 0.060 | ⚠ within organs, on part of the lines; also absent: PLS3, ENSG00000281883, NIBAN2; its own permutation p |
| [[UBASH3B]] | B | FOSL1 activity raises UBASH3B's level | lines that do not express FOSL1 (5) vs lines expressing it (45) | 4.36× lower at baseline in the lines without FOSL1 | 0.060 | ⚠ within organs, on part of the lines; also absent: PLS3, ENSG00000281883, NIBAN2; its own permutation p |
| [[KCNN4]] | B | FOSL1 activity raises KCNN4's level | lines that do not express FOSL1 (5) vs lines expressing it (45) | 3.79× lower at baseline in the lines without FOSL1 | 0.060 | ⚠ within organs, on part of the lines; also absent: PLS3, ENSG00000281883, NIBAN2; its own permutation p |
| [[ITGB5]] | B | FOSL1 activity raises ITGB5's level | lines that do not express FOSL1 (5) vs lines expressing it (45) | 2.62× lower at baseline in the lines without FOSL1 | 0.060 | ⚠ within organs, on part of the lines; also absent: PLS3, ENSG00000281883, NIBAN2; its own permutation p |
| [[TNFRSF10B]] | B | FOSL1 activity raises TNFRSF10B's level | lines that do not express FOSL1 (5) vs lines expressing it (45) | 2.35× lower at baseline in the lines without FOSL1 | 0.060 | ⚠ within organs, on part of the lines; also absent: PLS3, ENSG00000281883, NIBAN2; its own permutation p |
| [[ACTN1]] | B | FOSL1 activity raises ACTN1's level | lines that do not express FOSL1 (5) vs lines expressing it (45) | 2.15× lower at baseline in the lines without FOSL1 | 0.060 | ⚠ within organs, on part of the lines; also absent: PLS3, ENSG00000281883, NIBAN2; its own permutation p |
| [[IER2]] | B | FOSL1 activity raises IER2's level | lines that do not express FOSL1 (5) vs lines expressing it (45) | 1.38× lower at baseline in the lines without FOSL1 | 0.060 | ⚠ within organs, on part of the lines; also absent: PLS3, ENSG00000281883, NIBAN2; its own permutation p |
| [[SYNJ2]] | B | FOSL1 activity raises SYNJ2's level | lines that do not express FOSL1 (5) vs lines expressing it (45) | 3.23× lower at baseline in the lines without FOSL1 | 0.088 | ⚠ within organs, on part of the lines; also absent: PLS3, ENSG00000281883, NIBAN2 |
| [[ANTXR2]] | B | FOSL1 activity raises ANTXR2's level | lines that do not express FOSL1 (5) vs lines expressing it (45) | 4.47× lower at baseline in the lines without FOSL1 | 0.089 | ⚠ within organs, on part of the lines; also absent: PLS3, ENSG00000281883, NIBAN2; its own permutation p |
| [[IER3]] | B | FOSL1 activity raises IER3's level | lines that do not express FOSL1 (5) vs lines expressing it (45) | 4.38× lower at baseline in the lines without FOSL1 | 0.089 | ⚠ within organs, on part of the lines; also absent: PLS3, ENSG00000281883, NIBAN2; its own permutation p |
| [[GPR39]] | B | FOSL1 activity raises GPR39's level | lines that do not express FOSL1 (5) vs lines expressing it (45) | 3.86× lower at baseline in the lines without FOSL1 | 0.089 | ⚠ within organs, on part of the lines; also absent: PLS3, ENSG00000281883, NIBAN2; its own permutation p |

## Where it sits

- **Module**: [[Module 158]]; 27 genes; every member is in the + arm (projection on the module's main direction 0.781). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (39.6, 2.0); signed map (7.3, 40.3). **Vector** length 125, 53.7% of its response variance represented; |z| ≥ 3 in 2,281 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +8.5 | +20.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +6.7 | +10.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.8 | +15.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.7 | +7.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +4.5 | +13.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.0 | +5.9 |
|  | [[Diphenhydramine (drug)]] 0.5 µM |  | +2.5 | +0.5 |
|  | [[Infigratinib (drug)]] 5 µM |  | +2.5 | +1.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.3 | +2.3 |
| fall | [[Trametinib (drug)]] 0.5 µM |  | -10.3 | -12.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -9.2 | -12.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -9.0 | -10.0 |
|  | [[Trametinib (drug)]] 5 µM |  | -9.0 | -15.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | -8.0 | -10.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -7.6 | -13.7 |

## What is on record

|  |  |
|---|---|
| Name | FOS like 1, AP-1 transcription factor subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:65,892,049-65,900,573 (-) |
| Ensembl biotype | protein_coding |
| Also known as | fra-1 |
| Gene groups (HGNC) | Fos transcription factor family |
| Hallmark sets | TNFA_SIGNALING_VIA_NFKB |
| Reactome | 5 pathways, smallest: NGF-stimulated transcription; Nuclear Events (kinase and transcription factor activation); Signaling by NTRK1 (TRKA) |
| Matched by | ensembl_id |

UniProt [P15407](https://www.uniprot.org/uniprotkb/P15407) carries no function annotation.

**Summary**, from NCBI Gene [8061](https://www.ncbi.nlm.nih.gov/gene/8061):

> The Fos gene family consists of 4 members: FOS, FOSB, FOSL1, and FOSL2. These genes encode leucine zipper proteins that can dimerize with proteins of the JUN family, thereby forming the transcription factor complex AP-1. As such, the FOS proteins have been implicated as regulators of cell proliferation, differentiation, and transformation. Several transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2014]

**Accessions** — [HGNC:13718](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13718) · Entrez [8061](https://www.ncbi.nlm.nih.gov/gene/8061) · UniProt [P15407](https://www.uniprot.org/uniprotkb/P15407) · Ensembl [ENSG00000175592](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175592)

## Data

Gene col 10628: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10628); `tables/drug_effects.parquet` (76 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10628, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10628]; `tensor/DDL_lfc|DDL_z.npy` [10628]; `embed/gene_vectors.npy` [10628]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10628 or target_col == 10628). Every well: [[FOSL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FOSL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
