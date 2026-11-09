---
symbol: "FCHSD2"
type: "gene"
col: 6018
ensembl_id: "ENSG00000137478"
name: "FCH and double SH3 domains 2"
location: "11q13.4"
module: 14
arm: "+"
pooled_cpm: 176.42
n_lines_expressing: 49
n_dd_up: 5
n_dd_down: 21
n_dd_up_clean: 5
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# FCHSD2

*FCH and double SH3 domains 2* — 11q13.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 1.66× (z +13.7, q 1e-39, up in 34 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.472× (z -20.2, q 0e+00, down in 40 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.494× (z -19.7, q 0e+00, down in 45 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NEO1]] (+0.62, fdr 1e-05), [[SSH2]] (+0.62, fdr 1e-05), [[NUAK1]] (+0.61, fdr 1e-05); moves opposite to [[TPD52L2]] (-0.56, fdr 3e-05), [[SZT2]] (-0.56, fdr 1e-05), [[TMED5]] (-0.55, fdr 1e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6018.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **1.66×** | +13.7 | 1e-39 | 34/47 (PANC-1, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.39×** | +13.1 | 7e-37 | 33/47 (PANC-1, A549, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.63×** | +6.3 | 5e-08 | 28/48 (PANC-1, A549, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.24×** | +5.8 | 1e-06 | 25/46 (NCI-H2347, AsPC-1, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.13× | +5.0 | 8e-05 | 11/47 (AsPC-1, HOP62, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.18× | +4.8 | 2e-04 | 16/47 (A549, C32, …) | all doses, stronger at high dose |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.16× | +4.3 | 0.001 | 11/47 (AsPC-1, CFPAC-1, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.16× | +4.3 | 0.001 | 17/47 (C32, LoVo, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.16× | +3.8 | 0.010 | 16/47 (NCI-H2347, SW 900, …) | all doses, flat |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.15× | +3.7 | 0.011 | 13/48 (SHP-77, C-33 A, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.09× | +3.5 | 0.024 | 9/47 (NCI-H2347, SW 900, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 1.14× | +3.3 | 0.045 | 16/49 (NCI-H2347, SW 900, …) | all doses, flat | noisy plate (z scaled) |
| [[Bentamapimod (drug)]] 0.05 µM |  | 1.13× | +3.2 | 0.055 | 9/46 (NCI-H460, AsPC-1, …) | inconsistent across doses |  |
| [[Bentamapimod (drug)]] 5 µM |  | **1.27×** | +3.1 | 0.073 | 9/47 (A549, PANC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 17 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6018.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.472×** | -20.2 | 0e+00 | 40/43 (LS 180, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.494×** | -19.7 | 0e+00 | 45/47 (SNU-423, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.521×** | -18.2 | 0e+00 | 45/48 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.599×** | -13.1 | 5e-37 | 36/44 (NCI-H2347, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.646×** | -12.2 | 3e-32 | 40/47 (NCI-H23, Hs 766T, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.659×** | -11.6 | 3e-29 | 34/47 (NCI-H23, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.651×** | -11.5 | 1e-28 | 30/46 (RKO, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.708×** | -9.6 | 4e-20 | 33/47 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.735×** | -8.6 | 5e-16 | 31/47 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **0.805×** | -8.5 | 8e-16 | 27/48 (HEC-1-A, LOX-IMVI, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.750×** | -8.0 | 5e-14 | 36/47 (PANC-1, NCI-H2030, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.783×** | -6.8 | 5e-10 | 28/47 (HEC-1-A, NCI-H23, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.789×** | -6.6 | 2e-09 | 33/48 (Panc 03.27, NCI-H2347, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.791×** | -6.5 | 2e-09 | 29/47 (Panc 03.27, AsPC-1, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.850× | -6.4 | 6e-09 | 20/47 (HEC-1-A, SW1417, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.778×** | -6.3 | 9e-09 | 26/47 (Panc 03.27, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.676×** | -5.1 | 1e-05 | 26/47 (Hs 766T, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.791×** | -4.5 | 2e-04 | 26/47 (Panc 03.27, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.712×** | -4.4 | 3e-04 | 21/47 (HT-29, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.856× | -4.3 | 5e-04 | 17/46 (BT-474, MIA PaCa-2, …) | all doses, flat |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 0.870× | -3.8 | 0.003 | 17/47 (NCI-H23, NCI-H1573, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.743×** | -3.8 | 0.003 | 18/47 (MIA PaCa-2, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | 0.870× | -3.7 | 0.005 | 13/47 (HOP62, MIA PaCa-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6018. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 225 | 2 | 12 (8 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +17.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.441× (z -19.7) ⚠ cell-cycle shift, explains ~8% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.479× (z -12.5) |
| [[PANC-1 (line)]] | alt | 287 | 3 | 10 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +22.4) | [[Dinaciclib (drug)]] 0.5 µM 0.334× (z -20.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.495× (z -13.0) |
| [[NCI-H23 (line)]] | alt | 277 | 0 | 10 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.153× (z -26.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.379× (z -13.9) |
| [[Panc 03.27 (line)]] | alt | 296 | 1 | 9 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.190× (z -19.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.280× (z -15.7) |
| [[LOX-IMVI (line)]] | wt | 295 | 0 | 9 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.324× (z -17.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.461× (z -11.7) |
| [[SNU-423 (line)]] | alt | 195 | 1 | 8 (4 ⚠) | [[Harringtonine (drug)]] 5 µM 1.82× (z +9.1) | [[Auranofin (drug)]] 5 µM 0.306× (z -18.6) |
| [[A549 (line)]] | wt | 184 | 4 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +19.0) | [[Panobinostat (drug)]] 5 µM 0.544× (z -10.0) |
| [[Hs 766T (line)]] | wt | 230 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.388× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.420× (z -11.6) |
| [[NCI-H2347 (line)]] | alt | 195 | 3 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +13.7) | [[Dinaciclib (drug)]] 0.05 µM 0.266× (z -17.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.458× (z -11.0) |
| [[J82 (line)]] | alt | 213 | 1 | 6 (6 ⚠) | [[Harringtonine (drug)]] 5 µM 2.16× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.306× (z -15.1) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 137 | 2 (2 ⚠) | 5 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.64× (z +9.6) ⚠ cell-cycle shift, explains ~8% of this change | [[Dinaciclib (drug)]] 5 µM 0.136× (z -26.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.411× (z -12.2) |
| [[NCI-H1573 (line)]] | alt | 160 | 0 | 7 (5 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.284× (z -16.2) ⚠ cell-cycle shift, explains ~14% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.431× (z -10.8) |
| [[NCI-H2030 (line)]] | alt | 203 | 1 | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.56× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.531× (z -12.7) ⚠ cell-cycle shift, explains ~8% of this change |
| [[RKO (line)]] | wt | 288 | 0 | 5 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.225× (z -20.9) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.382× (z -14.0) |
| [[A-172 (line)]] | wt | 225 | 1 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.05× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.245× (z -16.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.399× (z -11.0) |
| [[BT-474 (line)]] | alt | 264 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.379× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.394× (z -10.6) |
| [[HS-578T (line)]] | alt | 194 | 2 (1 ⚠) | 2 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 4.42× (z +15.7) | [[Dinaciclib (drug)]] 5 µM 0.388× (z -10.1) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 295 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.275× (z -17.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.399× (z -12.2) |
| [[SW1417 (line)]] | alt | 135 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +10.6) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.581× (z -11.4) |
| [[A-427 (line)]] | wt | 253 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.426× (z -12.3) |
| [[AN3 CA (line)]] | alt | 336 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.202× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.281× (z -12.0) |
| [[AsPC-1 (line)]] | alt | 106 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.420× (z -10.9) |
| [[C-33 A (line)]] | alt | 244 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.245× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.418× (z -11.4) |
| [[HOP62 (line)]] | alt | 99.9 | 1 | 2 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 2.09× (z +9.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.626× (z -8.7) ⚠ cell-cycle shift, explains ~8% of this change |
| [[HT-29 (line)]] | alt | 130 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.393× (z -13.4) |
| [[LoVo (line)]] | wt | 99.7 | 1 (1 ⚠) | 2 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 1.93× (z +9.4) ⚠ cell-cycle shift, explains ~37% of this change | [[Auranofin (drug)]] 5 µM 0.402× (z -13.7) |
| [[MIA PaCa-2 (line)]] | alt | 161 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.369× (z -11.6) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.384× (z -11.6) |
| [[NCI-H1792 (line)]] | alt | 133 | 1 | 2 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.30× (z +10.6) | [[Homoharringtonine (drug)]] 5 µM 0.625× (z -8.9) |
| [[RPMI-7951 (line)]] | alt | 113 | 2 | 1 | [[Harringtonine (drug)]] 5 µM 3.79× (z +13.4) | [[Auranofin (drug)]] 5 µM 0.390× (z -9.9) |
| [[SNU-1 (line)]] | wt | 223 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.393× (z -11.7) |
| [[SW 900 (line)]] | alt | 167 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.325× (z -13.8) |
| [[NCI-H460 (line)]] | wt | 97.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +11.5) | [[Dinaciclib (drug)]] 0.05 µM 0.539× (z -8.5) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 206 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.365× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.470× (z -8.5) |
| [[SW480 (line)]] | alt | 142 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.356× (z -16.8) |
| [[A498 (line)]] | wt | 118 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +8.7) | — |
| [[CFPAC-1 (line)]] | alt | 104 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +11.6) | — |
| [[CHP-212 (line)]] | wt | 197 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.238× (z -9.8) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 82.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.374× (z -9.6) ⚠ cell-cycle shift, explains ~9% of this change |
| [[H4 (line)]] | wt | 149 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.355× (z -11.5) |
| [[HCT15 (line)]] | alt | 162 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.328× (z -13.0) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 257 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.363× (z -10.5) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 142 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 3.35× (z +10.8) | — |
| [[NCI-H596 (line)]] | alt | 174 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 5 µM 0.247× (z -14.1) |
| [[C32 (line)]] | wt | 141 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.0 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 163 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 68.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 94.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 205 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6018), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NEO1]] | +0.62 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[SSH2]] | +0.62 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[NUAK1]] | +0.61 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[NUAK2]] | +0.59 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[ANKRD33B]] | +0.58 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[CD70]] | +0.57 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[TGIF2]] | +0.57 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[CDC14A]] | +0.56 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[UVRAG]] | +0.56 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[IKBKE]] | +0.56 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[PLCL2]] | +0.55 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[DENND2B]] | +0.55 | +0.51 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPD52L2]] | -0.56 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[SZT2]] | -0.56 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[TMED5]] | -0.55 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[RER1]] | -0.52 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[WDR55]] | -0.51 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[SIN3B]] | -0.51 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[MBD1]] | -0.51 | -0.40 / -0.56 | both halves | 5e-05 |  |
| [[SLC30A6]] | -0.50 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[CHFR]] | -0.50 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[PCYT1A]] | -0.48 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[ZNF587]] | -0.47 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[SPTLC1]] | -0.47 | -0.52 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.563). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.1, 6.1); signed map (43.9, 1.1). **Vector** length 123, 39.3% of its response variance represented; |z| ≥ 3 in 1,530 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +11.5 | +13.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.2 | +13.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +6.1 | +5.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.0 | +6.3 |
|  | [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +0.5 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +3.0 | +2.9 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | +2.8 | +2.7 |
|  | [[Bentamapimod (drug)]] 5 µM |  | +2.8 | +3.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.7 | +5.8 |
| fall | [[Auranofin (drug)]] 5 µM |  | -10.5 | -19.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -5.6 | -6.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -5.6 | -9.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.6 | -2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.2 | -8.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -5.1 | -1.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.9 | -1.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.7 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | FCH and double SH3 domains 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.4 — chr11:72,836,745-73,142,318 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0769; previously SH3MD3 |
| Gene groups (HGNC) | F-BAR domain containing; SH3 domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [O94868](https://www.uniprot.org/uniprotkb/O94868) (F-BAR and double SH3 domains protein 2):

> Adapter protein that plays a role in endocytosis via clathrin-coated pits. Contributes to the internalization of cell surface receptors, such as integrin ITGB1 and transferrin receptor. Promotes endocytosis of EGFR in cancer cells, and thereby contributes to the down-regulation of EGFR signaling. Recruited to clathrin-coated pits during a mid-to-late stage of assembly, where it is required for normal progress from U-shaped intermediate stage pits to terminal, omega-shaped pits. Binds to …

**Summary**, from NCBI Gene [9873](https://www.ncbi.nlm.nih.gov/gene/9873):

> Enables phosphatidylinositol-3,4,5-trisphosphate binding activity and phosphatidylinositol-3,4-bisphosphate binding activity. Involved in clathrin-dependent endocytosis and positive regulation of Arp2/3 complex-mediated actin nucleation. Located in clathrin-coated pit and plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29114](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29114) · Entrez [9873](https://www.ncbi.nlm.nih.gov/gene/9873) · UniProt [O94868](https://www.uniprot.org/uniprotkb/O94868) · Ensembl [ENSG00000137478](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137478)

## Data

Gene col 6018: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6018); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6018, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6018]; `tensor/DDL_lfc|DDL_z.npy` [6018]; `embed/gene_vectors.npy` [6018]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6018 or target_col == 6018). Every well: [[FCHSD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FCHSD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
