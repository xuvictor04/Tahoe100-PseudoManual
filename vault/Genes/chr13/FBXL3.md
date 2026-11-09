---
symbol: "FBXL3"
type: "gene"
col: 89
ensembl_id: "ENSG00000005812"
name: "F-box and leucine rich repeat protein 3"
location: "13q22.3"
module: 130
arm: "+"
pooled_cpm: 75.13
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 20
n_dd_up_clean: 10
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/130"]
generated_by: "tahoemap"
---

# FBXL3

*F-box and leucine rich repeat protein 3* — 13q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.52× (z +12.9, q 4e-35, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.399× (z -19.1, q 0e+00, down in 40 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.493× (z -15.3, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLEKHF2]] (+0.71, fdr 7e-06), [[TAPT1]] (+0.66, fdr 1e-05), [[C3orf38]] (+0.66, fdr 1e-05); moves opposite to [[DAP3]] (-0.61, fdr 1e-05), [[EP400]] (-0.59, fdr 4e-05), [[GAK]] (-0.58, fdr 1e-04).
> It is in [[Module 130]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 89.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.52×** | +12.9 | 4e-35 | 37/48 (A549, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.56×** | +9.3 | 4e-18 | 36/48 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.50×** | +8.8 | 2e-16 | 34/48 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.12×** | +8.5 | 3e-15 | 39/49 (SW480, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.48×** | +8.4 | 4e-15 | 35/48 (HEC-1-A, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.40×** | +7.3 | 4e-11 | 27/48 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.39×** | +7.1 | 1e-10 | 32/48 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.31×** | +5.8 | 4e-07 | 29/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.60×** | +5.4 | 5e-06 | 33/48 (SW480, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.23×** | +4.6 | 3e-04 | 24/48 (A549, A498, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.21×** | +4.2 | 0.001 | 23/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +4.0 | 0.003 | 17/48 (A-427, A498, …) | rises with dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 14 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 89.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.399×** | -19.1 | 0e+00 | 40/41 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.439×** | -17.8 | 0e+00 | 46/49 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.493×** | -15.3 | 0e+00 | 47/48 (HOP62, SW480, …) | inconsistent across doses | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.478×** | -14.8 | 0e+00 | 38/45 (HEC-1-A, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.509×** | -14.6 | 0e+00 | 44/48 (A-172, HOP62, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.536×** | -13.5 | 1e-39 | 41/48 (A-172, AsPC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.551×** | -12.9 | 3e-36 | 43/48 (A-172, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.590×** | -11.4 | 2e-28 | 38/48 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.684×** | -8.2 | 1e-14 | 34/48 (KATO III, LS 180, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.692×** | -8.0 | 1e-13 | 39/48 (NCI-H2347, AsPC-1, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.936× | -5.2 | 1e-05 | 1/50 (SW 1088) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.644×** | -5.0 | 3e-05 | 28/49 (A-172, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.654×** | -4.8 | 6e-05 | 26/48 (LoVo, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.660×** | -4.7 | 1e-04 | 27/48 (AsPC-1, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.661×** | -4.7 | 1e-04 | 24/48 (RPMI-7951, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.688×** | -4.2 | 8e-04 | 19/48 (SW480, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Thymol (drug)]] 5 µM |  | 0.886× | -3.7 | 0.006 | 8/48 (Panc 03.27, RPMI-7951, …) | top dose only |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.745×** | -3.3 | 0.024 | 15/47 (NCI-H460, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.745×** | -3.3 | 0.024 | 19/48 (NCI-H2347, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Isocorydine (drug)]] 0.5 µM |  | 0.866× | -3.1 | 0.041 | 11/48 (AsPC-1, Hs 766T, …) | inconsistent across doses |  |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | 0.904× | -3.1 | 0.041 | 6/48 (HS-578T, NCI-H1792, …) | top dose only |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 0.868× | -3.1 | 0.045 | 8/48 (SW1417, J82, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.826×** | -3.0 | 0.060 | 11/48 (LoVo, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.38 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 89. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 127 | 5 (1 ⚠) | 8 (6 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.00× (z +12.5) | [[Dinaciclib (drug)]] 0.5 µM 0.230× (z -26.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.513× (z -11.9) |
| [[NCI-H460 (line)]] | wt | 61.5 | 6 (3 ⚠) | 4 (3 ⚠) | [[Digitoxin (drug)]] 5 µM 2.54× (z +11.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.42× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.377× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.456× (z -9.8) |
| [[A549 (line)]] | wt | 57.7 | 3 | 6 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +14.7) | [[Dinaciclib (drug)]] 5 µM 0.347× (z -11.9) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 98.4 | 2 | 7 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +13.1) | [[Dinaciclib (drug)]] 0.05 µM 0.169× (z -21.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.415× (z -11.4) |
| [[HOP62 (line)]] | alt | 73.2 | 1 | 8 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.264× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.285× (z -14.8) |
| [[NCI-H2347 (line)]] | alt | 107 | 0 | 9 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.202× (z -20.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.496× (z -9.6) |
| [[CFPAC-1 (line)]] | alt | 74.5 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.284× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.412× (z -10.3) |
| [[KATO III (line)]] | alt | 82.6 | 3 (1 ⚠) | 5 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.65× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.215× (z -18.9) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 0.5 µM 0.491× (z -9.1) |
| [[LS 180 (line)]] | wt | 79.7 | 3 (1 ⚠) | 5 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.66× (z +10.6) | [[Dinaciclib (drug)]] 0.05 µM 0.317× (z -11.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 80.7 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.179× (z -19.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.05 µM 0.352× (z -12.5) |
| [[Hs 766T (line)]] | wt | 128 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.203× (z -18.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.450× (z -9.6) |
| [[AsPC-1 (line)]] | alt | 99.7 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.227× (z -19.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.506× (z -9.0) |
| [[LoVo (line)]] | wt | 77.5 | 1 | 5 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.16× (z +10.6) | [[Dinaciclib (drug)]] 0.05 µM 0.356× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.499× (z -9.5) |
| [[SNU-423 (line)]] | alt | 73.8 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.245× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.337× (z -11.8) |
| [[A498 (line)]] | wt | 63.4 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +12.3) | [[Panobinostat (drug)]] 0.5 µM 0.347× (z -10.8) ⚠ cell-cycle shift, explains ~31% of this change |
| [[LOX-IMVI (line)]] | wt | 93.4 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.328× (z -12.5) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 113 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.358× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.416× (z -9.7) |
| [[H4 (line)]] | wt | 53.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.241× (z -10.4) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 99.1 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +12.0) | [[Dinaciclib (drug)]] 0.05 µM 0.380× (z -10.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 42.0 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.451× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.475× (z -9.5) |
| [[SW1417 (line)]] | alt | 70.5 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.217× (z -16.0) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 76.7 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.42× (z +8.7) | — |
| [[HT-29 (line)]] | alt | 84.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.342× (z -12.1) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 77.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.249× (z -12.2) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 58.9 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.350× (z -9.9) |
| [[NCI-H23 (line)]] | alt | 46.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.173× (z -16.3) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 78.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +11.2) | — |
| [[SNU-1 (line)]] | wt | 92.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.266× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.342× (z -8.6) |
| [[C32 (line)]] | wt | 51.7 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.353× (z -8.9) |
| [[CHP-212 (line)]] | wt | 66.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.149× (z -8.9) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 106 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.211× (z -13.9) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 114 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.195× (z -15.3) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 54.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.294× (z -9.4) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 77.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.123× (z -21.9) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 66.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0816× (z -10.5) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 71.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.383× (z -8.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 36.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +10.8) | — |
| [[SW48 (line)]] | wt | 93.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.247× (z -11.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 41.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 73.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 49.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 83.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 85.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 92.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 63.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 89), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLEKHF2]] | +0.71 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[TAPT1]] | +0.66 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[C3orf38]] | +0.66 | +0.53 / +0.70 | both halves | 1e-05 |  |
| [[CLK4]] | +0.63 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[PIK3CA]] | +0.62 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[FBXO8]] | +0.62 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[MBIP]] | +0.62 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[RCHY1]] | +0.61 | +0.61 / +0.53 | both halves | 1e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[PIGP]] | +0.60 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[PAPOLG]] | +0.60 | +0.41 / +0.63 | both halves | 4e-05 |  |
| [[TERF2IP]] | +0.59 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[RAB9A]] | +0.59 | +0.49 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DAP3]] | -0.61 | -0.63 / -0.56 | both halves | 1e-05 |  |
| [[EP400]] | -0.59 | -0.42 / -0.60 | both halves | 4e-05 |  |
| [[GAK]] | -0.58 | -0.36 / -0.59 | both halves | 1e-04 |  |
| [[LRP8]] | -0.57 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[PPM1F]] | -0.57 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[LIMK1]] | -0.57 | -0.46 / -0.52 | both halves | 2e-05 |  |
| [[RTEL1]] | -0.56 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[ERCC2]] | -0.56 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[ASPH]] | -0.56 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[ETF1]] | -0.55 | -0.31 / -0.65 | both halves | 2e-04 |  |
| [[FUBP3]] | -0.55 | -0.28 / -0.64 | both halves | 3e-04 |  |
| [[EIPR1]] | -0.55 | -0.56 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 130]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.721). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (2.3, -26.3); signed map (24.9, -16.2). **Vector** length 115, 36.0% of its response variance represented; |z| ≥ 3 in 1,210 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.9 | +4.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.4 | +8.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.3 | +9.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +6.7 | +2.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.6 | +12.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.5 | +4.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.7 | +2.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.3 | +1.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.0 | +1.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -9.0 | -15.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -8.9 | -8.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~13% of this change | -5.6 | -3.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | -5.3 | -3.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -5.2 | -8.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.9 | -3.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.6 | -4.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.4 | -2.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.4 | -4.7 |

## What is on record

|  |  |
|---|---|
| Name | F-box and leucine rich repeat protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q22.3 — chr13:76,992,598-77,027,195 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FBL3, FBL3A; previously FBXL3A |
| Gene groups (HGNC) | F-box and leucine rich repeat proteins |
| Reactome | 11 pathways, smallest: AMP and AMPK regulate the circadian clock; Association of TriC/CCT with target proteins during biosynthesis; Regulation of the circadian clock |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UKT7](https://www.uniprot.org/uniprotkb/Q9UKT7) (F-box/LRR-repeat protein 3):

> Substrate-recognition component of the SCF(FBXL3) E3 ubiquitin ligase complex involved in circadian rhythm function. Plays a key role in the maintenance of both the speed and the robustness of the circadian clock oscillation. The SCF(FBXL3) complex mainly acts in the nucleus and mediates ubiquitination and subsequent degradation of CRY1 and CRY2. Activity of the SCF(FBXL3) complex is counteracted by the SCF(FBXL21) complex.

**Summary**, from NCBI Gene [26224](https://www.ncbi.nlm.nih.gov/gene/26224):

> This gene encodes a member of the F-box protein family which is characterized by an approximately 40 amino acid motif, the F-box. The F-box proteins constitute one of the four subunits of ubiquitin protein ligase complex called SCFs (SKP1-cullin-F-box), which function in phosphorylation-dependent ubiquitination. The F-box proteins are divided into 3 classes: Fbws containing WD-40 domains, Fbls containing leucine-rich repeats, and Fbxs containing either different protein-protein interaction …

**Accessions** — [HGNC:13599](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13599) · Entrez [26224](https://www.ncbi.nlm.nih.gov/gene/26224) · UniProt [Q9UKT7](https://www.uniprot.org/uniprotkb/Q9UKT7) · Ensembl [ENSG00000005812](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000005812)

## Data

Gene col 89: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 89); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 89, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 89]; `tensor/DDL_lfc|DDL_z.npy` [89]; `embed/gene_vectors.npy` [89]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 89 or target_col == 89). Every well: [[FBXL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBXL3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
