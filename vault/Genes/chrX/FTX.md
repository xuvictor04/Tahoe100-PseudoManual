---
symbol: "FTX"
type: "gene"
col: 13760
ensembl_id: "ENSG00000230590"
name: "FTX transcript, XIST regulator"
location: "Xq13.2"
module: 26
arm: "+"
pooled_cpm: 494.25
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 30
n_dd_up_clean: 4
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# FTX

*FTX transcript, XIST regulator* — Xq13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Auranofin (drug)]] 5 µM: 1.50× (z +5.5, q 2e-05, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (20 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.335× (z -21.1, q 0e+00, down in 46 of 48 measured lines) ⚠ cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.210× (z -11.1, q 8e-27, down in 49 of 49 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPATCH2]] (+0.69, fdr 1e-05), [[FBXL19-AS1]] (+0.69, fdr 7e-06), [[NEK11]] (+0.66, fdr 1e-05); moves opposite to [[SUGT1P4-STRA6LP]] (-0.57, fdr 2e-05), [[ALDH7A1]] (-0.56, fdr 2e-05), [[SDHAF3]] (-0.55, fdr 3e-05).
> It sits in the **+** arm of [[Module 026]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13760.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.50×** | +5.5 | 2e-05 | 32/48 (LoVo, C32, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.32×** | +3.8 | 0.044 | 38/47 (Hs 766T, LOX-IMVI, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.67×** | +3.7 | 0.049 | 34/50 (A-427, LS 180, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.36×** | +3.4 | 0.087 | 34/47 (CFPAC-1, A-427, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 20 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13760.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.335×** | -21.1 | 0e+00 | 46/48 (NCI-H1573, COLO 205, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.327×** | -15.3 | 0e+00 | 48/48 (COLO 205, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.337×** | -14.9 | 0e+00 | 48/48 (SW480, HCT15, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.347×** | -14.4 | 4e-45 | 48/48 (HCT15, MIA PaCa-2, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.342×** | -12.0 | 4e-31 | 48/48 (C32, COLO 205, …) | rises with dose | composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.210×** | -11.1 | 8e-27 | 49/49 (NCI-H23, NCI-H1573, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.475×** | -10.2 | 2e-22 | 45/48 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.242×** | -10.1 | 3e-22 | 45/48 (SK-MEL-2, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change | **0.493×** | -9.6 | 3e-20 | 42/49 (A-427, NCI-H23, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.427×** | -9.5 | 1e-19 | 47/47 (NCI-H1573, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **0.511×** | -9.2 | 3e-18 | 45/48 (PANC-1, BT-474, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **0.491×** | -9.0 | 1e-17 | 42/45 (A-172, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **0.479×** | -8.2 | 8e-15 | 44/47 (MIA PaCa-2, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.549×** | -8.2 | 1e-14 | 43/48 (PANC-1, BT-474, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change | **0.537×** | -7.0 | 1e-10 | 37/44 (A-427, NCI-H1573, …) | all doses, flat | composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.702×** | -4.8 | 4e-05 | 38/48 (MIA PaCa-2, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.572×** | -4.0 | 0.002 | 42/49 (CHP-212, HepG2/C3A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.829×** | -3.6 | 0.007 | 28/48 (CHP-212, RPMI-7951, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.835× | -3.5 | 0.012 | 24/49 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.736×** | -3.4 | 0.013 | 29/48 (H4, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.788×** | -3.2 | 0.025 | 29/48 (C32, BT-474, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.806×** | -2.9 | 0.067 | 27/47 (NCI-H23, CFPAC-1, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 0.861× | -2.9 | 0.074 | 17/48 (CHP-212, SK-MEL-2, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.811×** | -2.8 | 0.079 | 27/48 (CFPAC-1, NCI-H1573, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.46 per unit of S-phase module lfc, -0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13760. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 911 | 0 | 19 (17 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -17.8) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.219× (z -15.0) |
| [[NCI-H460 (line)]] | wt | 794 | 0 | 18 (15 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -27.7) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.210× (z -16.6) |
| [[COLO 205 (line)]] | alt | 706 | 1 | 14 (10 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.01× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -28.5) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.156× (z -12.2) |
| [[MIA PaCa-2 (line)]] | alt | 693 | 0 | 15 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -18.6) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.239× (z -15.8) |
| [[HepG2_C3A (line)]] | wt | 518 | 0 | 14 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -20.9) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.391× (z -9.5) |
| [[BT-474 (line)]] | alt | 530 | 0 | 13 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -18.0) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.189× (z -9.4) |
| [[LoVo (line)]] | wt | 474 | 1 | 12 (10 ⚠) | [[Auranofin (drug)]] 5 µM 2.70× (z +13.3) | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -21.1) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.210× (z -10.9) |
| [[NCI-H1573 (line)]] | alt | 802 | 0 | 13 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -33.5) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.157× (z -13.0) |
| [[A-172 (line)]] | wt | 532 | 0 | 12 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -23.0) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.239× (z -14.2) |
| [[A-427 (line)]] | wt | 380 | 0 | 12 (9 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.230× (z -19.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.384× (z -12.8) |
| [[SNU-423 (line)]] | alt | 496 | 0 | 12 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -24.3) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.170× (z -9.9) |
| [[CHP-212 (line)]] | wt | 854 | 0 | 11 (8 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.212× (z -14.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.106× (z -10.9) |
| [[SW480 (line)]] | alt | 674 | 0 | 11 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.256× (z -16.1) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.204× (z -9.8) |
| [[H4 (line)]] | wt | 538 | 0 | 10 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -20.4) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.301× (z -11.3) |
| [[KATO III (line)]] | alt | 288 | 1 | 9 (9 ⚠) | [[Auranofin (drug)]] 5 µM 1.97× (z +8.8) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.309× (z -15.2) ⚠ cell-cycle shift, explains ~67% of this change |
| [[NCI-H23 (line)]] | alt | 752 | 0 | 10 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -19.2) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.117× (z -13.8) |
| [[SW1417 (line)]] | alt | 638 | 0 | 10 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -17.0) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.329× (z -10.9) |
| [[LS 180 (line)]] | wt | 443 | 0 | 9 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.290× (z -14.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.127× (z -12.1) |
| [[SK-MEL-2 (line)]] | alt | 606 | 0 | 9 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.216× (z -18.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.121× (z -13.0) |
| [[C32 (line)]] | wt | 296 | 1 | 7 (6 ⚠) | [[Auranofin (drug)]] 5 µM 2.60× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -28.1) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.195× (z -16.9) |
| [[HT-29 (line)]] | alt | 433 | 1 | 7 (6 ⚠) | [[Auranofin (drug)]] 5 µM 2.31× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.412× (z -13.8) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.171× (z -10.2) |
| [[J82 (line)]] | alt | 341 | 0 | 8 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -16.1) ⚠ cell-cycle shift, explains ~38% of this change |
| [[Panc 03.27 (line)]] | alt | 330 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -14.6) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.422× (z -9.8) |
| [[RPMI-7951 (line)]] | alt | 563 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -25.1) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.358× (z -10.3) |
| [[A498 (line)]] | wt | 471 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -23.2) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.149× (z -9.1) |
| [[A549 (line)]] | wt | 416 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -19.0) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.245× (z -12.1) |
| [[AsPC-1 (line)]] | alt | 488 | 0 | 7 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.324× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[CFPAC-1 (line)]] | alt | 298 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -20.9) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.348× (z -12.3) |
| [[HCT15 (line)]] | alt | 438 | 0 | 7 (6 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.239× (z -16.1) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.220× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 398 | 0 | 7 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.324× (z -14.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.179× (z -11.6) |
| [[HOP62 (line)]] | alt | 540 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -20.0) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.129× (z -10.5) |
| [[hTERT-HPNE (line)]] | wt | 321 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -21.2) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.140× (z -9.3) |
| [[SW 900 (line)]] | alt | 349 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -19.1) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.183× (z -8.6) |
| [[C-33 A (line)]] | alt | 428 | 0 | 6 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.270× (z -15.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.155× (z -11.2) |
| [[Hs 766T (line)]] | wt | 357 | 0 | 6 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.352× (z -10.4) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H1792 (line)]] | alt | 340 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -23.7) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.197× (z -10.2) |
| [[SNU-1 (line)]] | wt | 438 | 0 | 6 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.245× (z -12.5) ⚠ toxic · without an alert: [[PH-797804 (drug)]] 5 µM 0.207× (z -8.9) |
| [[HS-578T (line)]] | alt | 258 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -16.9) ⚠ cell-cycle shift, explains ~38% of this change |
| [[SW48 (line)]] | wt | 488 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.285× (z -13.4) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[TAK-901 (drug)]] 0.05 µM 0.425× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 355 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -16.4) ⚠ cell-cycle shift, explains ~38% of this change |
| [[RKO (line)]] | wt | 262 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.481× (z -12.4) ⚠ cell-cycle shift, explains ~38% of this change |
| [[AN3 CA (line)]] | alt | 313 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.289× (z -9.6) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H2347 (line)]] | alt | 207 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.535× (z -10.1) ⚠ cell-cycle shift, explains ~38% of this change |
| [[NCI-H2030 (line)]] | alt | 253 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.390× (z -12.3) ⚠ cell-cycle shift, explains ~38% of this change |
| [[SHP-77 (line)]] | alt | 259 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.403× (z -9.5) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SW 1271 (line)]] | alt | 371 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -12.3) ⚠ cell-cycle shift, explains ~38% of this change |
| [[SW 1088 (line)]] | alt | 605 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -12.1) ⚠ cell-cycle shift, explains ~38% of this change |
| [[NCI-H2122 (line)]] | alt | 465 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 504 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 262 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13760), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPATCH2]] | +0.69 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[FBXL19-AS1]] | +0.69 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[NEK11]] | +0.66 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[EXOC4]] | +0.65 | +0.57 / +0.63 | both halves | 9e-06 |  |
| [[SLC38A6]] | +0.65 | +0.68 / +0.52 | both halves | 1e-05 |  |
| [[MRPL45P2]] | +0.65 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[ACYP2]] | +0.65 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[CCDC90B-AS1]] | +0.64 | +0.46 / +0.65 | both halves | 3e-05 |  |
| [[HTATIP2]] | +0.63 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[SLC25A53]] | +0.61 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[COA6]] | +0.61 | +0.66 / +0.41 | both halves | 4e-05 |  |
| [[KANSL1L]] | +0.59 | +0.56 / +0.36 | both halves | 1e-04 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SUGT1P4-STRA6LP]] | -0.57 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[ALDH7A1]] | -0.56 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[SDHAF3]] | -0.55 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[FOXO6]] | -0.55 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[MRPS31P4]] | -0.54 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[STRA6LP]] | -0.54 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[PADI2]] | -0.54 | -0.36 / -0.43 | both halves | 1e-04 |  |
| [[ZNF30]] | -0.54 | -0.31 / -0.49 | both halves | 2e-04 |  |
| [[RAB3A]] | -0.52 | -0.51 / -0.24 | both halves | 4e-04 |  |
| [[STARD5]] | -0.51 | -0.30 / -0.44 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.591). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (9.5, 12.8); signed map (23.9, -4.5). **Vector** length 108, 52.8% of its response variance represented; |z| ≥ 3 in 1,658 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +12.8 | +5.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +9.3 | +1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +9.2 | +0.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +8.9 | -0.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.7 | +2.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.6 | -0.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.9 | +1.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -8.3 | -3.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change | -6.9 | -7.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.6 | -2.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -6.5 | -15.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -6.0 | -14.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.2 | -10.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -4.0 | -4.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -3.0 | -2.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.9 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | FTX transcript, XIST regulator |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | Xq13.2 — chrX:73,940,435-74,293,574 (-) |
| Ensembl biotype | lncRNA |
| Also known as | LINC00182, FLJ33139; previously NCRNA00182, MIR374AHG |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [100302692](https://www.ncbi.nlm.nih.gov/gene/100302692):

> This gene is located upstream of XIST, within the X-inactivation center (XIC). It produces a spliced long non-coding RNA that is thought to positively regulate the expression of XIST, which is essential for the initiation and spread of X-inactivation. [provided by RefSeq, May 2015]

**Accessions** — [HGNC:37190](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:37190) · Entrez [100302692](https://www.ncbi.nlm.nih.gov/gene/100302692) · Ensembl [ENSG00000230590](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000230590)

## Data

Gene col 13760: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13760); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13760, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13760]; `tensor/DDL_lfc|DDL_z.npy` [13760]; `embed/gene_vectors.npy` [13760]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13760 or target_col == 13760). Every well: [[FTX — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FTX.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
