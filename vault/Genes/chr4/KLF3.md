---
symbol: "KLF3"
type: "gene"
col: 3081
ensembl_id: "ENSG00000109787"
name: "KLF transcription factor 3"
location: "4p14"
module: 31
arm: "+"
pooled_cpm: 108.5
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 30
n_dd_up_clean: 6
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 30
direction_downstream: 0
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# KLF3

*KLF transcription factor 3* — 4p14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (none with an alert); the strongest is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 1.58× (z +9.3, q 1e-17, up in 37 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (15 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.331× (z -22.2, q 0e+00, down in 47 of 48 measured lines) ⚠ cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 0.647× (z -8.7, q 2e-16, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZFP36L2]] (+0.70, fdr 7e-06), [[MISP]] (+0.61, fdr 1e-05), [[RHOU]] (+0.58, fdr 2e-05); moves opposite to [[POM121]] (-0.52, fdr 3e-05), [[MAP2K1]] (-0.52, fdr 2e-05), [[TUBGCP5]] (-0.52, fdr 1e-05).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 30 arrows point to it, the strongest [[CYP3A5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3081.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.58×** | +9.3 | 1e-17 | 37/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.60×** | +9.1 | 3e-17 | 40/47 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.35×** | +4.3 | 0.003 | 20/48 (HEC-1-A, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Alpelisib (drug)]] 5 µM |  | **1.42×** | +3.7 | 0.033 | 21/47 (NCI-H460, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 1.17× | +3.6 | 0.033 | 19/48 (NCI-H460, HOP62, …) | two highest doses | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.28×** | +3.6 | 0.035 | 12/48 (HOP62, NCI-H460, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | 1.18× | +3.4 | 0.051 | 12/48 (KATO III, NCI-H460, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.18× | +3.4 | 0.052 | 19/49 (SK-MEL-2, HepG2/C3A, …) | inconsistent across doses | composition shift |
| [[RMC-6236 (drug)]] 5 µM |  | **1.37×** | +3.3 | 0.067 | 12/48 (NCI-H460, HOP62, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Neratinib (drug)]] 5 µM |  | 1.17× | +3.2 | 0.090 | 17/48 (NCI-H460, C32, …) | top dose only |  |
| [[Ixazomib (drug)]] 5 µM |  | 1.34× | +3.1 | 0.11 | 11/48 (CFPAC-1, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | 1.33× | +3.0 | 0.11 | 12/50 (NCI-H460, A-427, …) | two highest doses | plate-row cell shift; noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | 1.16× | +3.0 | 0.11 | 15/48 (NCI-H460, A-172, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 19 with an alert ⚠; shown: the 15 strongest and the 12 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3081.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.331×** | -22.2 | 0e+00 | 47/48 (SW480, LS 180, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.354×** | -20.8 | 0e+00 | 47/48 (AsPC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.543×** | -17.3 | 0e+00 | 37/49 (HT-29, LoVo, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.451×** | -16.0 | 0e+00 | 46/48 (SW480, LoVo, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.575×** | -11.1 | 1e-26 | 41/48 (COLO 205, KATO III, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.622×** | -9.1 | 6e-18 | 36/48 (SW48, LS 180, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.647×** | -8.7 | 2e-16 | 39/48 (COLO 205, NCI-H1573, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.650×** | -8.3 | 7e-15 | 35/50 (LS 180, HT-29, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.718×** | -6.6 | 2e-09 | 34/48 (BT-474, SW48, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.792×** | -6.6 | 2e-09 | 27/48 (AsPC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.661×** | -6.0 | 9e-08 | 31/48 (LoVo, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.574×** | -5.8 | 3e-07 | 26/45 (LS 180, SW48, …) | all doses, flat | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.750×** | -5.8 | 3e-07 | 27/48 (HT-29, MIA PaCa-2, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.759×** | -5.5 | 1e-06 | 26/48 (SW480, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~85% of this change | **0.757×** | -5.4 | 3e-06 | 25/47 (HepG2/C3A, SNU-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.610×** | -5.2 | 8e-06 | 24/49 (CFPAC-1, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.754×** | -4.0 | 0.002 | 16/48 (NCI-H460, LoVo, …) | two highest doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.762×** | -3.9 | 0.003 | 22/49 (LS 180, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.699×** | -3.7 | 0.005 | 20/48 (HT-29, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.882× | -3.6 | 0.009 | 15/48 (SNU-1, Hs 766T, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.841× | -3.3 | 0.021 | 16/48 (MIA PaCa-2, COLO 205, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.734×** | -3.2 | 0.027 | 16/48 (NCI-H460, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 0.5 µM |  | **0.799×** | -3.2 | 0.030 | 6/49 (SNU-423, C-33 A, …) | rises with dose | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.738×** | -3.2 | 0.030 | 16/49 (HT-29, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | 0.862× | -3.0 | 0.057 | 11/48 (SNU-1, MIA PaCa-2, …) | rises with dose |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.819×** | -2.9 | 0.075 | 9/49 (NCI-H460, HT-29, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Volasertib (drug)]] 0.5 µM |  | **0.819×** | -2.8 | 0.075 | 9/48 (J82, NCI-H2030, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.68 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3081. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 404 | 0 | 15 (11 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.144× (z -22.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.211× (z -18.1) |
| [[NCI-H460 (line)]] | wt | 89.8 | 11 (1 ⚠) | 4 (4 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 4.33× (z +18.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.395× (z -16.8) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SNU-1 (line)]] | wt | 269 | 0 | 15 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -14.3) |
| [[LoVo (line)]] | wt | 355 | 0 | 13 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -22.3) |
| [[COLO 205 (line)]] | alt | 205 | 0 | 12 (10 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.131× (z -18.2) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.240× (z -18.0) |
| [[LS 180 (line)]] | wt | 328 | 0 | 12 (9 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.127× (z -23.4) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.365× (z -16.2) |
| [[AsPC-1 (line)]] | alt | 234 | 0 | 11 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -27.1) |
| [[SW48 (line)]] | wt | 253 | 0 | 10 (9 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0825× (z -19.6) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.415× (z -9.8) |
| [[KATO III (line)]] | alt | 247 | 0 | 9 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.144× (z -21.2) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.421× (z -9.4) |
| [[Hs 766T (line)]] | wt | 182 | 0 | 8 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.149× (z -17.8) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.359× (z -13.6) |
| [[SW480 (line)]] | alt | 91.0 | 2 | 6 (6 ⚠) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.42× (z +11.9) | [[Panobinostat (drug)]] 5 µM 0.136× (z -27.0) ⚠ cell-cycle shift, explains ~37% of this change |
| [[CFPAC-1 (line)]] | alt | 157 | 0 | 7 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.341× (z -18.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.603× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 90.0 | 3 (2 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +18.5) | [[Panobinostat (drug)]] 5 µM 0.366× (z -13.9) ⚠ cell-cycle shift, explains ~37% of this change |
| [[NCI-H1573 (line)]] | alt | 140 | 0 | 7 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.117× (z -21.3) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.324× (z -11.2) |
| [[A-172 (line)]] | wt | 77.0 | 2 | 4 (4 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 2.62× (z +10.4) | [[Panobinostat (drug)]] 0.5 µM 0.307× (z -13.3) ⚠ cell-cycle shift, explains ~34% of this change |
| [[HS-578T (line)]] | alt | 67.0 | 1 | 4 (4 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 2.96× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -12.3) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SW1417 (line)]] | alt | 106 | 0 | 5 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.280× (z -14.0) ⚠ cell-cycle shift, explains ~34% of this change |
| [[A549 (line)]] | wt | 75.0 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.225× (z -15.0) ⚠ cell-cycle shift, explains ~37% of this change |
| [[Panc 03.27 (line)]] | alt | 144 | 0 | 4 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.369× (z -15.0) ⚠ cell-cycle shift, explains ~27% of this change |
| [[A-427 (line)]] | wt | 65.1 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.177× (z -16.9) ⚠ cell-cycle shift, explains ~37% of this change |
| [[BT-474 (line)]] | alt | 87.0 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.230× (z -12.6) ⚠ cell-cycle shift, explains ~34% of this change |
| [[H4 (line)]] | wt | 59.0 | 2 | 1 (1 ⚠) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 4.92× (z +10.8) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.261× (z -8.7) ⚠ cell-cycle shift, explains ~55% of this change |
| [[HepG2_C3A (line)]] | wt | 82.0 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.164× (z -15.4) ⚠ toxic; cell-cycle shift, explains ~85% of this change |
| [[SK-MEL-2 (line)]] | alt | 62.3 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +9.6) | [[Panobinostat (drug)]] 0.5 µM 0.224× (z -14.0) ⚠ cell-cycle shift, explains ~34% of this change |
| [[C-33 A (line)]] | alt | 62.7 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.316× (z -9.5) ⚠ cell-cycle shift, explains ~37% of this change |
| [[HOP62 (line)]] | alt | 40.1 | 1 | 1 (1 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 3.84× (z +10.4) | [[Panobinostat (drug)]] 5 µM 0.247× (z -11.2) ⚠ cell-cycle shift, explains ~37% of this change |
| [[LOX-IMVI (line)]] | wt | 50.6 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.334× (z -9.4) ⚠ cell-cycle shift, explains ~34% of this change |
| [[MIA PaCa-2 (line)]] | alt | 47.4 | 1 | 1 (1 ⚠) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.81× (z +8.6) | [[Panobinostat (drug)]] 5 µM 0.345× (z -8.8) ⚠ cell-cycle shift, explains ~37% of this change |
| [[NCI-H23 (line)]] | alt | 34.7 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.242× (z -10.6) ⚠ cell-cycle shift, explains ~37% of this change |
| [[NCI-H596 (line)]] | alt | 106 | 0 | 2 (1 ⚠) | — | [[Pentoxifylline (drug)]] 0.05 µM 0.113× (z -10.4) ⚠ transcription drop · without an alert: [[Atazanavir (sulfate) (drug)]] 5 µM 0.121× (z -10.0) |
| [[C32 (line)]] | wt | 27.9 | 1 | 0 | [[Pitavastatin (Calcium) (drug)]] 5 µM 4.93× (z +9.4) | — |
| [[J82 (line)]] | alt | 50.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +11.0) | — |
| [[NCI-H1792 (line)]] | alt | 69.9 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.366× (z -12.8) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H2030 (line)]] | alt | 48.8 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.326× (z -9.4) ⚠ cell-cycle shift, explains ~37% of this change |
| [[SNU-423 (line)]] | alt | 80.0 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.340× (z -10.6) ⚠ cell-cycle shift, explains ~37% of this change |
| [[SW 1271 (line)]] | alt | 135 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.249× (z -8.5) ⚠ cell-cycle shift, explains ~27% of this change |
| [[A498 (line)]] | wt | 59.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 69.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 53.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 78.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 65.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 72.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 39.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 55.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 60.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3081), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFP36L2]] | +0.70 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[MISP]] | +0.61 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[RHOU]] | +0.58 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[EZR]] | +0.57 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[PLCD3]] | +0.56 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[RHOB]] | +0.56 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[C4BPB]] | +0.55 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[ELF3-AS1]] | +0.54 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[KLF11]] | +0.54 | +0.39 / +0.56 | both halves | 5e-05 | same gene group |
| [[CYP3A5]] | +0.53 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[PLEKHG6]] | +0.53 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[MYO16-AS1]] | +0.53 | +0.45 / +0.52 | both halves | 3e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POM121]] | -0.52 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[MAP2K1]] | -0.52 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[TUBGCP5]] | -0.52 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[BTAF1]] | -0.51 | -0.49 / -0.37 | both halves | 8e-05 |  |
| [[POM121C]] | -0.50 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[INTS4]] | -0.49 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[ZNF215]] | -0.49 | -0.43 / -0.48 | both halves | 3e-05 | same gene group |
| [[APBA2]] | -0.48 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[KDM2B-DT]] | -0.47 | -0.39 / -0.53 | both halves | 5e-05 |  |
| [[PSMD14]] | -0.47 | -0.45 / -0.40 | both halves | 4e-05 |  |
| [[CRYBB2P1-1]] | -0.46 | -0.41 / -0.39 | both halves | 5e-05 |  |
| [[PRKRIP1]] | -0.46 | -0.43 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*30 arrows, 30 of them with an alert ⚠; grade A 0, B 30, C 0. Shown: the 12 strongest; 18 more arrows (18 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CYP3A5]] | B | CYP3A5 activity raises KLF3's level | lines that do not express CYP3A5 (32) vs lines expressing it (18) | 2.70× lower at baseline in the lines without CYP3A5 | 6e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HHLA2, GCNT3, HNF4A |
| [[TRIM29]] | B | TRIM29 activity raises KLF3's level | lines that do not express TRIM29 (28) vs lines expressing it (22) | 2.28× lower at baseline in the lines without TRIM29 | 0.001 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, TNNT2 |
| [[FOXQ1]] | B | FOXQ1 activity raises KLF3's level | lines that do not express FOXQ1 (30) vs lines expressing it (20) | 2.34× lower at baseline in the lines without FOXQ1 | 0.002 | ⚠ within organs, on part of the lines; also absent: SERPINB5, TTC22, COL17A1 |
| [[ITGB4]] | B | ITGB4 activity raises KLF3's level | lines that do not express ITGB4 (25) vs lines expressing it (25) | 2.16× lower at baseline in the lines without ITGB4 | 0.004 | ⚠ within organs, on part of the lines; also absent: SCNN1A, AREG, GJB3 |
| [[EDN1]] | B | EDN1 activity raises KLF3's level | lines that do not express EDN1 (27) vs lines expressing it (23) | 1.90× lower at baseline in the lines without EDN1 | 0.007 | ⚠ within organs, on part of the lines; also absent: P2RY2, S100A14, CBLC |
| [[MISP]] | B | MISP activity raises KLF3's level | lines that do not express MISP (23) vs lines expressing it (27) | 2.01× lower at baseline in the lines without MISP | 0.009 | ⚠ within organs, on part of the lines; also absent: GRB7, KRT18, MYO5B |
| [[C4BPB]] | B | C4BPB activity raises KLF3's level | lines that do not express C4BPB (37) vs lines expressing it (13) | 2.52× lower at baseline in the lines without C4BPB | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, LINC02964, REG4 |
| [[TJP2]] | B | TJP2 activity raises KLF3's level | lines that do not express TJP2 (10) vs lines expressing it (40) | 1.96× lower at baseline in the lines without TJP2 | 0.012 | ⚠ within organs, on part of the lines; also absent: PYROXD2, NRIP1, ENSG00000235609; maybe low, not absent |
| [[GCNT3]] | B | GCNT3 activity raises KLF3's level | lines that do not express GCNT3 (38) vs lines expressing it (12) | 2.50× lower at baseline in the lines without GCNT3 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, LYZ, MUC13 |
| [[SLC22A3]] | B | SLC22A3 activity raises KLF3's level | lines that do not express SLC22A3 (30) vs lines expressing it (20) | 2.05× lower at baseline in the lines without SLC22A3 | 0.013 | ⚠ within organs, on part of the lines; also absent: TTC22, GCNT3, INAVA |
| [[EPS8L3]] | B | EPS8L3 activity raises KLF3's level | lines that do not express EPS8L3 (35) vs lines expressing it (15) | 2.49× lower at baseline in the lines without EPS8L3 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02964, EDAR, HNF4A |
| [[PIK3CA]] | B | PIK3CA activity lowers KLF3's level | compounds that target PIK3CA: 3 of 4 raise it (Alpelisib, Bimiralisib, GSK1059615) | 75% of the class's compounds vs 1.4% of all compounds | 0.017 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.451). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (10.7, 57.2); signed map (52.3, 9.0). **Vector** length 117, 37.4% of its response variance represented; |z| ≥ 3 in 1,362 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.8 | -6.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +7.7 | +1.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.6 | +1.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.7 | -2.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | +6.7 | +9.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +5.9 | +9.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.0 | +3.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +3.3 | +2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | -0.3 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +3.0 | +3.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -3.6 | -6.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.0 | -5.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | -2.9 | -9.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -2.6 | -11.1 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -2.5 | -2.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.4 | -4.0 |
|  | [[Bentamapimod (drug)]] 5 µM |  | -2.2 | -1.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.2 | -3.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -2.1 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | KLF transcription factor 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p14 — chr4:38,664,197-38,701,517 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BKLF |
| Gene groups (HGNC) | Zinc fingers C2H2-type; KLF transcription factors |
| Hallmark sets | HEME_METABOLISM |
| Matched by | ensembl_id |

**Function**, from UniProt [P57682](https://www.uniprot.org/uniprotkb/P57682) (Krueppel-like factor 3):

> Binds to the CACCC box of erythroid cell-expressed genes. May play a role in hematopoiesis (By similarity).

**Summary**, from NCBI Gene [51274](https://www.ncbi.nlm.nih.gov/gene/51274):

> Enables sequence-specific double-stranded DNA binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16516](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16516) · Entrez [51274](https://www.ncbi.nlm.nih.gov/gene/51274) · UniProt [P57682](https://www.uniprot.org/uniprotkb/P57682) · Ensembl [ENSG00000109787](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109787)

## Data

Gene col 3081: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3081); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3081, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3081]; `tensor/DDL_lfc|DDL_z.npy` [3081]; `embed/gene_vectors.npy` [3081]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3081 or target_col == 3081). Every well: [[KLF3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KLF3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
