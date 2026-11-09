---
symbol: "GOLGB1"
type: "gene"
col: 10360
ensembl_id: "ENSG00000173230"
name: "golgin B1"
location: "3q13.33"
module: 74
arm: "+"
pooled_cpm: 471.63
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 21
n_dd_up_clean: 9
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/074"]
generated_by: "tahoemap"
---

# GOLGB1

*golgin B1* — 3q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.45× (z +28.1, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (8 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.626× (z -10.4, q 1e-22, down in 42 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[venetoclax (drug)]] 5 µM: 0.645× (z -5.1, q 3e-05, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CREB3]] (+0.76, fdr 7e-06), [[AKAP9]] (+0.75, fdr 7e-06), [[BOD1L1]] (+0.75, fdr 7e-06); moves opposite to [[ADAT2]] (-0.67, fdr 7e-06), [[LAPTM4B]] (-0.66, fdr 7e-06), [[UCK2]] (-0.63, fdr 7e-06).
> It is in [[Module 074]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10360.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.45×** | +28.1 | 0e+00 | 48/48 (PANC-1, C32, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.06×** | +15.5 | 0e+00 | 47/48 (PANC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.99×** | +15.4 | 0e+00 | 45/48 (C32, RKO, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.43×** | +7.9 | 3e-13 | 34/48 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.37×** | +7.1 | 2e-10 | 34/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.41×** | +4.0 | 0.005 | 34/49 (HepG2/C3A, Panc 03.27, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.20×** | +3.9 | 0.008 | 23/48 (A-427, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.39×** | +3.8 | 0.010 | 31/48 (A-427, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.4 | 0.036 | 22/48 (A-427, SW1417, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.16× | +3.4 | 0.036 | 17/48 (KATO III, HEC-1-A, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.33×** | +3.3 | 0.046 | 24/49 (A-427, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.31×** | +3.2 | 0.075 | 26/47 (SK-MEL-2, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.30×** | +3.1 | 0.087 | 19/45 (SW1417, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.0 | 0.10 | 19/48 (A-427, SK-MEL-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10360.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.626×** | -10.4 | 1e-22 | 42/48 (H4, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.630×** | -9.9 | 1e-20 | 44/47 (COLO 205, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.665×** | -9.1 | 2e-17 | 41/48 (HT-29, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.719×** | -6.8 | 2e-09 | 28/45 (H4, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.762×** | -6.0 | 2e-07 | 30/49 (COLO 205, H4, …) | all doses, flat | composition shift |
| [[venetoclax (drug)]] 5 µM |  | **0.645×** | -5.1 | 3e-05 | 43/48 (CFPAC-1, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.851× | -5.0 | 4e-05 | 22/48 (BT-474, NCI-H1573, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.802×** | -4.9 | 6e-05 | 27/48 (H4, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.808×** | -4.7 | 1e-04 | 31/48 (KATO III, COLO 205, …) | rises with dose |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.812×** | -4.6 | 2e-04 | 33/48 (NCI-H460, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.817×** | -4.5 | 4e-04 | 25/48 (H4, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.682×** | -4.4 | 4e-04 | 31/48 (AsPC-1, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.683×** | -4.4 | 4e-04 | 37/48 (CFPAC-1, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.820×** | -4.4 | 4e-04 | 23/48 (H4, COLO 205, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[EX229 (drug)]] 5 µM |  | **0.686×** | -4.4 | 4e-04 | 33/48 (MIA PaCa-2, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.833×** | -4.1 | 0.002 | 23/49 (BT-474, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.809×** | -3.4 | 0.021 | 29/48 (HT-29, HepG2/C3A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.815×** | -3.2 | 0.030 | 25/48 (PANC-1, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.816×** | -3.2 | 0.030 | 28/48 (NCI-H23, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | 0.869× | -3.1 | 0.044 | 16/48 (AN3 CA, C32, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.767×** | -3.1 | 0.046 | 25/48 (MIA PaCa-2, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10360. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 851 | 2 | 11 (8 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.22× (z +12.1) | [[Digitoxin (drug)]] 5 µM 0.345× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.415× (z -13.3) |
| [[NCI-H460 (line)]] | wt | 276 | 7 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +23.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.487× (z -12.1) ⚠ unreliable plate only · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.579× (z -9.2) |
| [[NCI-H1573 (line)]] | alt | 585 | 4 | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +22.0) | [[Digitoxin (drug)]] 5 µM 0.393× (z -12.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 400 | 7 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +30.5) | [[Digitoxin (drug)]] 5 µM 0.554× (z -10.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 402 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +16.2) | — |
| [[HT-29 (line)]] | alt | 670 | 4 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +21.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.454× (z -12.9) ⚠ unreliable plate only |
| [[SK-MEL-2 (line)]] | alt | 612 | 5 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +19.3) | [[Dinaciclib (drug)]] 0.05 µM 0.493× (z -10.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 511 | 6 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +21.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.534× (z -9.9) ⚠ toxic |
| [[A549 (line)]] | wt | 488 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +20.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.570× (z -12.1) ⚠ cell-cycle shift, explains ~53% of this change |
| [[CFPAC-1 (line)]] | alt | 631 | 1 | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +17.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.475× (z -13.0) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 287 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +21.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.561× (z -8.6) ⚠ unreliable plate only |
| [[MIA PaCa-2 (line)]] | alt | 394 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +18.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.446× (z -12.6) ⚠ unreliable plate only |
| [[RKO (line)]] | wt | 348 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +21.2) | [[Dinaciclib (drug)]] 0.5 µM 0.469× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[C32 (line)]] | wt | 364 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.83× (z +29.9) | — |
| [[COLO 205 (line)]] | alt | 889 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +18.4) | [[Dinaciclib (drug)]] 0.5 µM 0.220× (z -19.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[HEC-1-A (line)]] | alt | 469 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +23.3) | — |
| [[HS-578T (line)]] | alt | 702 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +12.8) | [[Digitoxin (drug)]] 5 µM 0.506× (z -11.0) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 535 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +22.8) | [[Digitoxin (drug)]] 5 µM 0.594× (z -9.0) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 305 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +20.6) | [[Digitoxin (drug)]] 5 µM 0.409× (z -13.0) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 283 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +19.6) | — |
| [[SW480 (line)]] | alt | 422 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +22.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.459× (z -13.3) ⚠ toxic |
| [[A-172 (line)]] | wt | 471 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +20.3) | [[Digitoxin (drug)]] 5 µM 0.523× (z -11.7) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 728 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.59× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.475× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[HOP62 (line)]] | alt | 519 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +23.3) | [[Dinaciclib (drug)]] 0.05 µM 0.473× (z -10.6) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 525 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +24.8) | [[Dinaciclib (drug)]] 0.05 µM 0.445× (z -11.5) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 612 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +11.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.392× (z -12.4) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 430 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +18.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.509× (z -9.2) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 808 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +18.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.514× (z -11.2) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 511 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +14.0) | [[Digitoxin (drug)]] 5 µM 0.444× (z -12.2) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 496 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +24.0) | — |
| [[C-33 A (line)]] | alt | 220 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +12.7) | — |
| [[HepG2_C3A (line)]] | wt | 315 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +13.2) | — |
| [[LS 180 (line)]] | wt | 482 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +20.9) | — |
| [[SNU-1 (line)]] | wt | 325 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +18.0) | — |
| [[SNU-423 (line)]] | alt | 521 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +17.4) | [[Digitoxin (drug)]] 5 µM 0.513× (z -11.4) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 486 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +14.9) | — |
| [[CHP-212 (line)]] | wt | 342 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +9.8) | [[Dinaciclib (drug)]] 0.05 µM 0.330× (z -10.8) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 410 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.435× (z -11.1) ⚠ toxic |
| [[LoVo (line)]] | wt | 568 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +23.5) | — |
| [[NCI-H2030 (line)]] | alt | 284 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +12.2) | — |
| [[NCI-H23 (line)]] | alt | 563 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +19.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.505× (z -10.2) ⚠ unreliable plate only |
| [[SHP-77 (line)]] | alt | 309 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +11.6) | [[Digitoxin (drug)]] 5 µM 0.544× (z -9.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 289 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +17.0) | — |
| [[AsPC-1 (line)]] | alt | 474 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 2.35× (z +10.5) | — |
| [[SW 1271 (line)]] | alt | 530 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +12.1) | — |
| [[SW 900 (line)]] | alt | 427 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +12.2) | — |
| [[NCI-H2122 (line)]] | alt | 430 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 435 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 241 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 514 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10360), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CREB3]] | +0.76 | +0.76 / +0.73 | both halves | 7e-06 |  |
| [[AKAP9]] | +0.75 | +0.73 / +0.76 | both halves | 7e-06 | STRING 515 |
| [[BOD1L1]] | +0.75 | +0.69 / +0.82 | both halves | 7e-06 |  |
| [[IK]] | +0.72 | +0.74 / +0.69 | both halves | 7e-06 |  |
| [[USP8]] | +0.68 | +0.78 / +0.59 | both halves | 7e-06 |  |
| [[TRIP11]] | +0.64 | +0.71 / +0.71 | both halves | 7e-06 | same gene group; pathway: FLT3 signaling in disease; STRING 857 |
| [[LYSMD3]] | +0.64 | +0.73 / +0.54 | both halves | 1e-05 |  |
| [[KDM5A]] | +0.64 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[TMF1]] | +0.64 | +0.57 / +0.62 | both halves | 1e-05 | same gene group; STRING 584 |
| [[SLU7]] | +0.63 | +0.75 / +0.62 | both halves | 7e-06 |  |
| [[CCDC186]] | +0.63 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[YIPF3]] | +0.63 | +0.65 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAT2]] | -0.67 | -0.72 / -0.63 | both halves | 7e-06 |  |
| [[LAPTM4B]] | -0.66 | -0.66 / -0.58 | both halves | 7e-06 |  |
| [[UCK2]] | -0.63 | -0.69 / -0.60 | both halves | 7e-06 |  |
| [[NBL1]] | -0.62 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[C1orf216]] | -0.61 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[UBE2G2]] | -0.60 | -0.62 / -0.58 | both halves | 7e-06 |  |
| [[NDC1]] | -0.60 | -0.63 / -0.60 | both halves | 7e-06 |  |
| [[CPSF4]] | -0.60 | -0.68 / -0.58 | both halves | 7e-06 |  |
| [[EEF1E1]] | -0.60 | -0.61 / -0.59 | both halves | 7e-06 |  |
| [[TUBGCP4]] | -0.60 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[CMTM4]] | -0.60 | -0.64 / -0.53 | both halves | 1e-05 |  |
| [[SLC41A3]] | -0.59 | -0.62 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 074]]; 63 genes; every member is in the + arm (projection on the module's main direction 0.695). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-4.6, -47.9); signed map (-10.6, -4.6). **Vector** length 169, 64.8% of its response variance represented; |z| ≥ 3 in 1,345 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +11.4 | +15.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +11.0 | +15.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +9.9 | +28.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +9.4 | +7.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.1 | +2.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +4.0 | +4.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +3.9 | +1.6 |
|  | [[Gemfibrozil (drug)]] 5 µM |  | +3.2 | +1.9 |
|  | [[Adagrasib (drug)]] 5 µM |  | +3.2 | +2.4 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -11.6 | -9.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -10.9 | -9.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -8.9 | -10.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -7.2 | -4.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -6.9 | -4.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.8 | -5.0 |
|  | [[venetoclax (drug)]] 5 µM |  | -6.6 | -5.1 |
|  | [[EX229 (drug)]] 5 µM |  | -6.3 | -4.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -5.8 | -4.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.4 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | golgin B1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q13.33 — chr3:121,663,199-121,749,966 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GCP, GCP372, giantin, GOLIM1 |
| Gene groups (HGNC) | Golgins |
| Reactome | 11 pathways, smallest: Signaling by FLT3 fusion proteins; FLT3 signaling in disease; Golgi Associated Vesicle Biogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14789](https://www.uniprot.org/uniprotkb/Q14789) (Golgin subfamily B member 1):

> May participate in forming intercisternal cross-bridges of the Golgi complex.

**Summary**, from NCBI Gene [2804](https://www.ncbi.nlm.nih.gov/gene/2804):

> Enables RNA binding activity. Involved in protein localization to pericentriolar material. Located in Golgi apparatus and endoplasmic reticulum-Golgi intermediate compartment. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:4429](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4429) · Entrez [2804](https://www.ncbi.nlm.nih.gov/gene/2804) · UniProt [Q14789](https://www.uniprot.org/uniprotkb/Q14789) · Ensembl [ENSG00000173230](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173230)

## Data

Gene col 10360: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10360); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10360, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10360]; `tensor/DDL_lfc|DDL_z.npy` [10360]; `embed/gene_vectors.npy` [10360]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10360 or target_col == 10360). Every well: [[GOLGB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GOLGB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
