---
symbol: "ZBTB20"
type: "gene"
col: 11208
ensembl_id: "ENSG00000181722"
name: "zinc finger and BTB domain containing 20"
location: "3q13.31"
module: 74
arm: "+"
pooled_cpm: 550.82
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 49
n_dd_up_clean: 16
n_dd_down_clean: 28
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/074"]
generated_by: "tahoemap"
---

# ZBTB20

*zinc finger and BTB domain containing 20* — 3q13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (3 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.52× (z +6.7, q 1e-08, up in 38 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 49 drug-doses (21 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.526× (z -14.9, q 0e+00, down in 46 of 49 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KMT2A]] (+0.67, fdr 1e-05), [[BCAS3]] (+0.65, fdr 7e-06), [[ANKRD12]] (+0.63, fdr 1e-05); moves opposite to [[KHDC1]] (-0.56, fdr 8e-05), [[PLEKHH1]] (-0.55, fdr 4e-05), [[NSUN2]] (-0.52, fdr 3e-05).
> It is in [[Module 074]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MTOR]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11208.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.52×** | +6.7 | 1e-08 | 38/47 (SK-MEL-2, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.88×** | +5.3 | 3e-05 | 40/50 (HEC-1-A, SK-MEL-2, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.41×** | +5.2 | 3e-05 | 38/50 (SK-MEL-2, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.36×** | +5.1 | 5e-05 | 38/47 (SK-MEL-2, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.34×** | +4.6 | 4e-04 | 33/48 (SK-MEL-2, LoVo, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.27×** | +4.5 | 6e-04 | 33/48 (SK-MEL-2, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.31×** | +4.3 | 0.001 | 34/47 (NCI-H460, NCI-H23, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.23×** | +4.3 | 0.001 | 31/48 (SK-MEL-2, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.29×** | +4.2 | 0.002 | 31/49 (SK-MEL-2, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[RMC-6236 (drug)]] 5 µM |  | **1.57×** | +3.8 | 0.008 | 35/48 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.26×** | +3.8 | 0.008 | 36/47 (RKO, HEC-1-A, …) | rises with dose | low cells (technical?) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.51×** | +3.5 | 0.021 | 29/49 (HEC-1-A, BT-474, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.26×** | +3.5 | 0.021 | 30/48 (SK-MEL-2, LoVo, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.20×** | +3.4 | 0.024 | 27/48 (HEC-1-A, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | 1.15× | +3.2 | 0.050 | 15/48 (KATO III, C-33 A, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 5 µM |  | **1.46×** | +3.2 | 0.050 | 26/48 (HEC-1-A, NCI-H23, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.23×** | +3.1 | 0.060 | 22/48 (HEC-1-A, SK-MEL-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 58 in all, 24 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 49 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 21 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11208.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.526×** | -14.9 | 0e+00 | 46/49 (CHP-212, SHP-77, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.389×** | -14.9 | 0e+00 | 47/47 (NCI-H1573, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.428×** | -13.9 | 7e-42 | 42/48 (NCI-H23, NCI-H1573, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.444×** | -13.4 | 1e-38 | 46/48 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.482×** | -12.0 | 4e-31 | 42/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.253×** | -11.6 | 6e-29 | 47/49 (NCI-H23, C32, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | **0.508×** | -11.1 | 7e-27 | 40/49 (NCI-H23, A-427, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.514×** | -10.9 | 5e-26 | 40/48 (PANC-1, HCT15, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | **0.522×** | -10.3 | 5e-23 | 36/44 (NCI-H23, SHP-77, …) | all doses, flat | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **0.539×** | -9.8 | 8e-21 | 41/47 (NCI-H1792, A-427, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.526×** | -9.8 | 8e-21 | 38/45 (C32, NCI-H1792, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.563×** | -9.4 | 2e-19 | 43/48 (PANC-1, BT-474, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.673×** | -9.2 | 2e-18 | 31/48 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.372×** | -8.3 | 4e-15 | 38/48 (A-427, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.379×** | -8.2 | 1e-14 | 44/48 (NCI-H23, SNU-1, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.505×** | -8.0 | 4e-14 | 48/48 (NCI-H23, SNU-1, …) | rises with dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.615×** | -8.0 | 5e-14 | 42/48 (KATO III, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.633×** | -7.5 | 2e-12 | 41/48 (NCI-H23, COLO 205, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.412×** | -7.5 | 3e-12 | 43/48 (NCI-H23, KATO III, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.448×** | -6.8 | 4e-10 | 39/48 (NCI-H23, NCI-H1573, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.667×** | -6.7 | 7e-10 | 36/48 (PANC-1, HT-29, …) | rises with dose |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.661×** | -6.1 | 3e-08 | 45/48 (SNU-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.514×** | -5.6 | 5e-07 | 36/48 (NCI-H23, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.535×** | -5.3 | 3e-06 | 36/48 (NCI-H23, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.644×** | -5.2 | 5e-06 | 43/48 (NCI-H23, COLO 205, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.52 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11208. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 622 | 0 | 29 (15 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -28.0) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.185× (z -23.6) |
| [[NCI-H1573 (line)]] | alt | 593 | 0 | 24 (13 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.149× (z -23.3) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.228× (z -18.8) |
| [[KATO III (line)]] | alt | 321 | 4 (3 ⚠) | 15 (5 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.86× (z +9.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.132× (z -22.6) ⚠ unreliable plate only · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.245× (z -15.6) |
| [[LOX-IMVI (line)]] | wt | 370 | 0 | 19 (9 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.192× (z -19.4) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.270× (z -15.4) |
| [[SNU-1 (line)]] | wt | 478 | 0 | 19 (9 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.134× (z -22.4) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 0.05 µM 0.289× (z -12.4) |
| [[A-427 (line)]] | wt | 808 | 0 | 17 (10 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.147× (z -24.2) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0921× (z -16.0) |
| [[COLO 205 (line)]] | alt | 1,138 | 0 | 14 (7 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.262× (z -19.8) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.436× (z -12.8) |
| [[HT-29 (line)]] | alt | 876 | 1 (1 ⚠) | 13 (8 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +12.1) ⚠ cell-cycle shift, explains ~48% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.177× (z -22.5) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.364× (z -13.6) |
| [[PANC-1 (line)]] | alt | 300 | 0 | 14 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -24.6) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.251× (z -14.3) |
| [[C32 (line)]] | wt | 929 | 0 | 13 (9 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.238× (z -17.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.395× (z -17.3) |
| [[NCI-H460 (line)]] | wt | 283 | 0 | 13 (12 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.253× (z -15.7) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.497× (z -11.2) |
| [[SW480 (line)]] | alt | 744 | 0 | 13 (11 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.395× (z -17.4) |
| [[BT-474 (line)]] | alt | 425 | 0 | 12 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -16.7) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[TAK-901 (drug)]] 0.05 µM 0.329× (z -9.6) |
| [[MIA PaCa-2 (line)]] | alt | 160 | 0 | 12 (5 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.135× (z -20.0) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.180× (z -17.1) |
| [[CHP-212 (line)]] | wt | 1,029 | 0 | 11 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.273× (z -19.5) |
| [[H4 (line)]] | wt | 764 | 0 | 11 (10 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.274× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.218× (z -9.2) |
| [[HCT15 (line)]] | alt | 294 | 0 | 11 (7 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.141× (z -17.5) ⚠ unreliable plate only · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.212× (z -13.9) |
| [[NCI-H1792 (line)]] | alt | 601 | 0 | 11 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.285× (z -16.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -16.3) |
| [[SHP-77 (line)]] | alt | 564 | 2 (1 ⚠) | 9 (6 ⚠) | [[Daptomycin (drug)]] 5 µM 1.79× (z +9.0) ⚠ unreliable plate only · without an alert: [[Peretinoin (drug)]] 5 µM 1.80× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -21.2) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.414× (z -19.2) |
| [[AN3 CA (line)]] | alt | 638 | 0 | 10 (7 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.244× (z -13.4) |
| [[RPMI-7951 (line)]] | alt | 824 | 0 | 10 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.294× (z -13.4) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 0.141× (z -11.4) |
| [[SW 900 (line)]] | alt | 533 | 0 | 10 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -16.0) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.155× (z -11.0) |
| [[A-172 (line)]] | wt | 868 | 2 (1 ⚠) | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +12.5) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.03× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.289× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.554× (z -11.3) |
| [[HEC-1-A (line)]] | alt | 878 | 1 | 6 (3 ⚠) | [[Cobimetinib (drug)]] 5 µM 1.94× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.432× (z -16.8) |
| [[Hs 766T (line)]] | wt | 146 | 0 | 7 (5 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.196× (z -13.5) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.282× (z -10.5) |
| [[LoVo (line)]] | wt | 165 | 2 (1 ⚠) | 5 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.00× (z +10.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.138× (z -20.8) ⚠ unreliable plate only · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.359× (z -10.7) |
| [[J82 (line)]] | alt | 603 | 0 | 6 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.352× (z -12.4) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.513× (z -11.6) |
| [[LS 180 (line)]] | wt | 507 | 0 | 6 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.246× (z -16.4) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.419× (z -14.4) |
| [[SK-MEL-2 (line)]] | alt | 663 | 2 | 4 (2 ⚠) | [[Cobimetinib (drug)]] 5 µM 2.21× (z +9.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.409× (z -10.6) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.555× (z -9.9) |
| [[hTERT-HPNE (line)]] | wt | 526 | 0 | 5 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.315× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[RKO (line)]] | wt | 445 | 1 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 1.99× (z +9.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.230× (z -18.9) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.570× (z -10.7) |
| [[SW1417 (line)]] | alt | 542 | 0 | 5 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.289× (z -11.7) ⚠ unreliable plate only · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.311× (z -11.0) |
| [[SW48 (line)]] | wt | 282 | 0 | 5 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.125× (z -16.2) ⚠ unreliable plate only · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.228× (z -11.6) |
| [[C-33 A (line)]] | alt | 369 | 0 | 4 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.223× (z -14.8) ⚠ unreliable plate only · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.314× (z -11.4) |
| [[HS-578T (line)]] | alt | 1,189 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.453× (z -11.2) |
| [[CFPAC-1 (line)]] | alt | 426 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.496× (z -10.2) |
| [[HepG2_C3A (line)]] | wt | 794 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.187× (z -18.3) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.407× (z -14.4) |
| [[Panc 03.27 (line)]] | alt | 676 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.480× (z -11.3) |
| [[SW 1271 (line)]] | alt | 658 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.177× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[NCI-H2030 (line)]] | alt | 467 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.515× (z -9.2) |
| [[SNU-423 (line)]] | alt | 543 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.507× (z -11.6) |
| [[A498 (line)]] | wt | 634 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -14.7) |
| [[A549 (line)]] | wt | 719 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.291× (z -14.8) |
| [[HOP62 (line)]] | alt | 610 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.436× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[SW 1088 (line)]] | alt | 642 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.237× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[AsPC-1 (line)]] | alt | 415 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 503 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 356 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 582 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 198 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11208), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KMT2A]] | +0.67 | +0.56 / +0.67 | both halves | 1e-05 | STRING 407 |
| [[BCAS3]] | +0.65 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[ANKRD12]] | +0.63 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[RSF1]] | +0.62 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[RB1CC1]] | +0.62 | +0.45 / +0.66 | both halves | 3e-05 |  |
| [[NIPBL]] | +0.61 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[ATXN1]] | +0.59 | +0.36 / +0.63 | both halves | 9e-05 |  |
| [[C1QTNF3-AMACR]] | +0.58 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[SMDT1]] | +0.58 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[NBEA]] | +0.58 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[WDR48]] | +0.58 | +0.31 / +0.59 | both halves | 2e-04 |  |
| [[PNRC1]] | +0.58 | +0.51 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KHDC1]] | -0.56 | -0.37 / -0.50 | both halves | 8e-05 |  |
| [[PLEKHH1]] | -0.55 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[NSUN2]] | -0.52 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[RNPS1]] | -0.52 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[PDSS1]] | -0.50 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[GMIP]] | -0.50 | -0.36 / -0.44 | both halves | 1e-04 |  |
| [[ATG16L1]] | -0.49 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[MALL]] | -0.49 | -0.53 / -0.39 | both halves | 5e-05 | same gene group |
| [[SFXN2]] | -0.49 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[RABEPK]] | -0.48 | -0.40 / -0.45 | both halves | 4e-05 |  |
| [[CAPN15]] | -0.48 | -0.46 / -0.40 | both halves | 4e-05 | same gene group |
| [[SLC25A15]] | -0.48 | -0.41 / -0.48 | both halves | 4e-05 | same gene group |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTOR]] | B | MTOR activity lowers ZBTB20's level | compounds that target MTOR: 4 of 8 raise it (AZD-8055, Bimiralisib, GSK1059615, Temsirolimus) | 50% of the class's compounds vs 3.4% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds |
| [[MAP2K1]] | B | MAP2K1 activity lowers ZBTB20's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.4% of all compounds | 0.067 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 074]]; 63 genes; every member is in the + arm (projection on the module's main direction 0.691). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-5.5, -45.5); signed map (-7.9, 12.2). **Vector** length 103, 44.5% of its response variance represented; |z| ≥ 3 in 2,469 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | +8.6 | -5.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | +5.9 | -2.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +5.8 | -12.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.8 | -5.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.6 | +4.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.2 | +6.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.9 | +2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.8 | +4.6 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +3.8 | +5.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -10.9 | -13.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -9.5 | -14.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -8.7 | -8.0 |
|  | [[EX229 (drug)]] 5 µM |  | -7.4 | -7.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -6.9 | -6.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -6.4 | -8.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -6.2 | -5.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -6.2 | -8.2 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger and BTB domain containing 20 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q13.31 — chr3:114,314,500-115,147,292 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ODA-8S, DKFZp566F123, DPZF; previously ZNF288 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; BTB domain containing; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HC78](https://www.uniprot.org/uniprotkb/Q9HC78) (Zinc finger and BTB domain-containing protein 20):

> May be a transcription factor that may be involved in hematopoiesis, oncogenesis, and immune responses. Plays a role in postnatal myogenesis, may be involved in the regulation of satellite cells self-renewal (By similarity).

**Summary**, from NCBI Gene [26137](https://www.ncbi.nlm.nih.gov/gene/26137):

> This gene, which was initially designated as dendritic cell-derived BTB/POZ zinc finger (DPZF), belongs to a family of transcription factors with an N-terminal BTB/POZ domain and a C-terminal DNA-bindng zinc finger domain. The BTB/POZ domain is a hydrophobic region of approximately 120 aa which mediates association with other BTB/POZ domain-containing proteins. This gene acts as a transcriptional repressor and plays a role in many processes including neurogenesis, glucose homeostasis, and …

**Accessions** — [HGNC:13503](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13503) · Entrez [26137](https://www.ncbi.nlm.nih.gov/gene/26137) · UniProt [Q9HC78](https://www.uniprot.org/uniprotkb/Q9HC78) · Ensembl [ENSG00000181722](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000181722)

## Data

Gene col 11208: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11208); `tables/drug_effects.parquet` (82 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11208, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11208]; `tensor/DDL_lfc|DDL_z.npy` [11208]; `embed/gene_vectors.npy` [11208]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11208 or target_col == 11208). Every well: [[ZBTB20 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZBTB20.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
