---
symbol: "SSH2"
type: "gene"
col: 6501
ensembl_id: "ENSG00000141298"
name: "slingshot protein phosphatase 2"
location: "17q11.2"
module: 14
arm: "+"
pooled_cpm: 250.74
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 16
n_dd_up_clean: 10
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# SSH2

*slingshot protein phosphatase 2* — 17q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.67× (z +19.4, q 0e+00, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.441× (z -20.9, q 0e+00, down in 42 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.520× (z -17.3, q 0e+00, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FCHSD2]] (+0.62, fdr 1e-05), [[MICOS10]] (+0.56, fdr 1e-05), [[IKBKE]] (+0.54, fdr 2e-05); moves opposite to [[TPD52L2]] (-0.62, fdr 7e-06), [[SZT2]] (-0.57, fdr 1e-05), [[LIG3]] (-0.55, fdr 1e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6501.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.67×** | +19.4 | 0e+00 | 36/48 (A549, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.58×** | +11.7 | 5e-29 | 38/48 (A549, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.66×** | +7.1 | 3e-10 | 31/49 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +6.3 | 4e-08 | 24/48 (J82, BT-474, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.24×** | +5.8 | 1e-06 | 24/48 (SNU-1, A549, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.24×** | +5.6 | 2e-06 | 29/47 (C32, A549, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.42×** | +4.9 | 8e-05 | 27/49 (LoVo, HOP62, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.20×** | +4.9 | 8e-05 | 24/49 (BT-474, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains <1% of this change | 1.20× | +4.8 | 9e-05 | 23/48 (HOP62, J82, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.16× | +4.0 | 0.003 | 16/48 (A549, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 1.16× | +4.0 | 0.003 | 21/48 (RKO, C-33 A, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 1.16× | +3.9 | 0.005 | 15/49 (C32, MIA PaCa-2, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.16× | +3.8 | 0.008 | 14/47 (SW48, C32, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.13× | +3.7 | 0.010 | 11/49 (C32, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.15× | +3.6 | 0.010 | 15/47 (C32, NCI-H23, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.15× | +3.6 | 0.013 | 12/48 (C32, MIA PaCa-2, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.10× | +3.4 | 0.022 | 6/48 (C32, MIA PaCa-2, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 15 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6501.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.441×** | -20.9 | 0e+00 | 42/44 (HCT15, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.461×** | -20.6 | 0e+00 | 45/49 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.520×** | -17.3 | 0e+00 | 43/48 (HEC-1-A, MIA PaCa-2, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.507×** | -16.7 | 0e+00 | 38/45 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.673×** | -10.5 | 1e-23 | 42/48 (HT-29, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.778×** | -9.4 | 5e-19 | 27/49 (A498, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.768×** | -6.7 | 2e-09 | 25/47 (LOX-IMVI, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.779×** | -6.6 | 2e-09 | 24/48 (LOX-IMVI, MIA PaCa-2, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.783×** | -6.5 | 6e-09 | 31/48 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.803×** | -5.8 | 4e-07 | 30/48 (H4, KATO III, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.726×** | -4.4 | 4e-04 | 26/48 (NCI-H1792, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.888× | -4.4 | 4e-04 | 11/49 (CHP-212, A549, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.730×** | -4.4 | 6e-04 | 27/48 (NCI-H1792, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~5% of this change | 0.846× | -4.2 | 9e-04 | 23/47 (LOX-IMVI, COLO 205, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.850× | -4.1 | 0.001 | 20/50 (HEC-1-A, LOX-IMVI, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.856× | -4.1 | 0.001 | 18/47 (C32, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.868× | -3.7 | 0.006 | 17/48 (CFPAC-1, A498, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.877× | -3.5 | 0.014 | 12/48 (NCI-H460, SW1417, …) | rises with dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 0.882× | -3.3 | 0.023 | 13/48 (LOX-IMVI, RKO, …) | two highest doses |  |
| [[Infigratinib (drug)]] 5 µM |  | **0.791×** | -3.2 | 0.028 | 12/48 (SNU-1, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.881× | -3.1 | 0.043 | 16/47 (NCI-H460, SNU-1, …) | inconsistent across doses | low cells (technical?) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.801×** | -3.1 | 0.044 | 19/49 (A498, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 0.921× | -3.1 | 0.044 | 2/49 (KATO III, SW 1271) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6501. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 376 | 9 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +17.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.374× (z -25.8) |
| [[LOX-IMVI (line)]] | wt | 459 | 0 | 14 (11 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.333× (z -21.9) |
| [[HEC-1-A (line)]] | alt | 653 | 3 (1 ⚠) | 7 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +22.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -24.0) |
| [[SW480 (line)]] | alt | 332 | 4 (2 ⚠) | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.54× (z +13.0) | [[Dinaciclib (drug)]] 0.5 µM 0.323× (z -24.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.525× (z -13.8) |
| [[A-172 (line)]] | wt | 266 | 3 (1 ⚠) | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +20.1) | [[Dinaciclib (drug)]] 0.5 µM 0.236× (z -22.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.476× (z -16.7) |
| [[COLO 205 (line)]] | alt | 587 | 0 | 9 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.186× (z -21.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.446× (z -14.4) |
| [[MIA PaCa-2 (line)]] | alt | 252 | 4 (1 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +18.6) | [[Auranofin (drug)]] 5 µM 0.310× (z -16.2) |
| [[C32 (line)]] | wt | 230 | 7 (1 ⚠) | 1 | [[Cobimetinib (drug)]] 5 µM 2.89× (z +11.8) | [[Auranofin (drug)]] 5 µM 0.480× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 247 | 3 (1 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +13.8) | [[Dinaciclib (drug)]] 0.5 µM 0.415× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.05 µM 0.565× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 213 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -21.3) |
| [[PANC-1 (line)]] | alt | 220 | 3 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +13.6) | [[Dinaciclib (drug)]] 0.5 µM 0.431× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.573× (z -9.5) |
| [[A-427 (line)]] | wt | 253 | 2 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +17.3) | [[Dinaciclib (drug)]] 0.05 µM 0.281× (z -18.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.567× (z -9.1) |
| [[A549 (line)]] | wt | 253 | 4 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +26.4) | [[Dinaciclib (drug)]] 0.5 µM 0.437× (z -13.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 246 | 1 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +15.4) | [[Dinaciclib (drug)]] 5 µM 0.296× (z -18.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.428× (z -13.4) |
| [[NCI-H1792 (line)]] | alt | 338 | 1 | 5 (4 ⚠) | [[Harringtonine (drug)]] 5 µM 1.97× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.342× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.470× (z -17.5) |
| [[Panc 03.27 (line)]] | alt | 289 | 2 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +16.7) | [[Dinaciclib (drug)]] 0.5 µM 0.441× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.450× (z -12.8) |
| [[HS-578T (line)]] | alt | 164 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.396× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.566× (z -10.9) |
| [[KATO III (line)]] | alt | 329 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.363× (z -15.6) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 227 | 4 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +20.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.503× (z -9.1) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 184 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -10.6) |
| [[CHP-212 (line)]] | wt | 359 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0890× (z -21.5) ⚠ toxic; transcription drop · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 0.472× (z -9.8) |
| [[J82 (line)]] | alt | 194 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +19.3) | [[Dinaciclib (drug)]] 5 µM 0.420× (z -13.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 294 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.284× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.521× (z -9.6) |
| [[SNU-1 (line)]] | wt | 214 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.378× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.05 µM 0.453× (z -8.8) |
| [[SNU-423 (line)]] | alt | 152 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +19.7) | [[Dinaciclib (drug)]] 5 µM 0.454× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.546× (z -8.8) |
| [[SW 900 (line)]] | alt | 180 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +11.2) | [[Auranofin (drug)]] 5 µM 0.418× (z -12.4) |
| [[SW1417 (line)]] | alt | 209 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.336× (z -17.1) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 165 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +9.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.455× (z -10.0) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.590× (z -9.5) |
| [[Hs 766T (line)]] | wt | 165 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.196× (z -20.2) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 216 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.392× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.429× (z -9.6) |
| [[LoVo (line)]] | wt | 158 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.82× (z +14.0) | — |
| [[NCI-H23 (line)]] | alt | 321 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.325× (z -12.9) |
| [[SHP-77 (line)]] | alt | 200 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.364× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.407× (z -14.1) |
| [[SW48 (line)]] | wt | 205 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +11.6) | [[Dinaciclib (drug)]] 0.05 µM 0.375× (z -10.4) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 233 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.290× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.500× (z -8.6) |
| [[H4 (line)]] | wt | 151 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +9.9) | [[Auranofin (drug)]] 5 µM 0.371× (z -10.4) |
| [[HepG2_C3A (line)]] | wt | 107 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +13.0) | [[Dinaciclib (drug)]] 0.05 µM 0.319× (z -9.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 151 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.36× (z +25.9) | — |
| [[NCI-H2347 (line)]] | alt | 170 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +16.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.535× (z -10.3) |
| [[SK-MEL-2 (line)]] | alt | 148 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +10.5) | [[Auranofin (drug)]] 5 µM 0.252× (z -14.5) |
| [[SW 1271 (line)]] | alt | 252 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.168× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.274× (z -8.7) |
| [[AN3 CA (line)]] | alt | 251 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.336× (z -9.9) |
| [[HCT15 (line)]] | alt | 283 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.135× (z -24.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 86.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +8.8) | — |
| [[RPMI-7951 (line)]] | alt | 148 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +11.5) | — |
| [[BT-474 (line)]] | alt | 207 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 295 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 245 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 203 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 147 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6501), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FCHSD2]] | +0.62 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[MICOS10]] | +0.56 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[IKBKE]] | +0.54 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[USP54]] | +0.54 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[POGZ]] | +0.53 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[S100A4]] | +0.53 | +0.39 / +0.47 | both halves | 6e-05 |  |
| [[ARRB1]] | +0.52 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[CCDC148]] | +0.51 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[PALS1]] | +0.51 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[MAP3K1]] | +0.51 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[BLOC1S1]] | +0.50 | +0.42 / +0.41 | both halves | 4e-05 |  |
| [[ZNF608]] | +0.50 | +0.50 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPD52L2]] | -0.62 | -0.58 / -0.61 | both halves | 7e-06 |  |
| [[SZT2]] | -0.57 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[LIG3]] | -0.55 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[CRYGS]] | -0.52 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[TIMM10B]] | -0.51 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[SMG1P6]] | -0.50 | -0.38 / -0.50 | both halves | 6e-05 |  |
| [[TMED5]] | -0.50 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[GTPBP2]] | -0.50 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[PABPC1L]] | -0.50 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[PIGG]] | -0.49 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[RFT1]] | -0.49 | -0.54 / -0.39 | both halves | 6e-05 |  |
| [[ZNF749]] | -0.49 | -0.44 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.419). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (10.3, -26.1); signed map (44.4, 1.0). **Vector** length 129, 42.9% of its response variance represented; |z| ≥ 3 in 1,740 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +12.1 | +11.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +9.4 | +19.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.5 | +7.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +6.1 | +3.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.2 | +5.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +6.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +2.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.9 | +4.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.8 | +3.9 |
| fall | [[Auranofin (drug)]] 5 µM |  | -9.5 | -17.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -7.5 | -5.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.7 | -16.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.0 | -9.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | -4.7 | -10.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.5 | -4.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.9 | -3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.7 | -6.6 |

## What is on record

|  |  |
|---|---|
| Name | slingshot protein phosphatase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q11.2 — chr17:29,625,938-29,930,276 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1725 |
| Gene groups (HGNC) | Slingshot protein phosphatases |
| Hallmark sets | MITOTIC_SPINDLE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q76I76](https://www.uniprot.org/uniprotkb/Q76I76) (Protein phosphatase Slingshot homolog 2):

> Protein phosphatase which regulates actin filament dynamics. Dephosphorylates and activates the actin binding/depolymerizing factor cofilin, which subsequently binds to actin filaments and stimulates their disassembly. Inhibitory phosphorylation of cofilin is mediated by LIMK1, which may also be dephosphorylated and inactivated by this protein. Required for spermatogenesis (By similarity). Involved in acrosome biogenesis, probably by regulating cofilin-mediated actin cytoskeleton remodeling …

**Summary**, from NCBI Gene [85464](https://www.ncbi.nlm.nih.gov/gene/85464):

> This gene encodes a protein tyrosine phosphatase that plays a key role in the regulation of actin filaments. The encoded protein dephosphorylates and activates cofilin, which promotes actin filament depolymerization. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Aug 2013]

**Accessions** — [HGNC:30580](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30580) · Entrez [85464](https://www.ncbi.nlm.nih.gov/gene/85464) · UniProt [Q76I76](https://www.uniprot.org/uniprotkb/Q76I76) · Ensembl [ENSG00000141298](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141298)

## Data

Gene col 6501: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6501); `tables/drug_effects.parquet` (63 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6501, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6501]; `tensor/DDL_lfc|DDL_z.npy` [6501]; `embed/gene_vectors.npy` [6501]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6501 or target_col == 6501). Every well: [[SSH2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SSH2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
