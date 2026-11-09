---
symbol: "HNRNPA2B1"
type: "gene"
col: 4353
ensembl_id: "ENSG00000122566"
name: "heterogeneous nuclear ribonucleoprotein A2/B1"
location: "7p15.2"
module: 3
arm: "-"
pooled_cpm: 671.55
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 12
n_dd_up_clean: 7
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# HNRNPA2B1

*heterogeneous nuclear ribonucleoprotein A2/B1* — 7p15.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (17 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.70× (z +24.2, q 0e+00, up in 46 of 48 measured lines) ⚠ cell-cycle shift, explains ~40% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.12× (z +13.3, q 2e-38, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.641× (z -7.9, q 2e-12, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CHD4]] (+0.69, fdr 7e-06), [[HNRNPU]] (+0.69, fdr 7e-06), [[YWHAE]] (+0.69, fdr 7e-06); moves opposite to [[LCMT1]] (-0.71, fdr 7e-06), [[CCZ1B]] (-0.71, fdr 7e-06), [[COMMD6]] (-0.70, fdr 7e-06).
> It sits in the **-** arm of [[Module 003]] (mRNA 3'-end processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 19 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4353.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **2.70×** | +24.2 | 0e+00 | 46/48 (AsPC-1, C32, …) | rises with dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.85×** | +23.9 | 0e+00 | 49/49 (A549, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.38×** | +20.8 | 0e+00 | 44/44 (A549, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.16×** | +18.8 | 0e+00 | 45/45 (HOP62, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.12×** | +13.3 | 2e-38 | 46/48 (AsPC-1, C32, …) | rises with dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.89×** | +11.3 | 2e-27 | 45/48 (C32, SK-MEL-2, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.85×** | +10.9 | 8e-26 | 47/48 (KATO III, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.88×** | +10.7 | 5e-25 | 44/48 (AsPC-1, A498, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **1.65×** | +8.5 | 1e-15 | 40/47 (COLO 205, SHP-77, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **1.58×** | +8.1 | 4e-14 | 44/48 (KATO III, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.53×** | +7.6 | 2e-12 | 41/48 (CFPAC-1, SNU-423, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.44×** | +6.4 | 7e-09 | 40/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.39×** | +5.8 | 3e-07 | 36/48 (RPMI-7951, SNU-423, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.35×** | +5.1 | 2e-05 | 34/50 (MIA PaCa-2, A-172, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **1.30×** | +4.6 | 1e-04 | 37/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.21×** | +3.4 | 0.016 | 26/48 (HOP62, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | **1.21×** | +3.4 | 0.016 | 27/48 (LoVo, SW 900, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.20×** | +3.1 | 0.038 | 25/48 (A549, H4, …) | top dose only |  |
| [[Crizotinib (hydrochloride) (drug)]] 0.5 µM |  | 1.19× | +3.0 | 0.059 | 17/48 (C32, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4353.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.641×** | -7.9 | 2e-12 | 37/48 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.654×** | -7.6 | 1e-11 | 40/48 (BT-474, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.695×** | -6.5 | 2e-08 | 32/48 (HEC-1-A, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **0.773×** | -4.6 | 7e-04 | 35/48 (C-33 A, LOX-IMVI, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.843× | -4.2 | 0.003 | 24/48 (SW480, NCI-H23, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.791×** | -4.2 | 0.003 | 32/48 (LS 180, SHP-77, …) | two highest doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.648×** | -4.0 | 0.005 | 38/49 (A-427, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.851× | -3.9 | 0.006 | 20/48 (C-33 A, HCT15, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.784×** | -3.9 | 0.006 | 34/50 (NCI-H23, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.818×** | -3.6 | 0.019 | 25/48 (HEC-1-A, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.819×** | -3.6 | 0.019 | 27/49 (NCI-H23, LoVo, …) | all doses, flat | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.819×** | -3.4 | 0.028 | 29/48 (NCI-H23, C-33 A, …) | all doses, flat | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.826×** | -3.4 | 0.028 | 25/48 (BT-474, SW48, …) | inconsistent across doses | position effect removed |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | 0.872× | -3.3 | 0.035 | 10/48 (J82, RKO, …) | rises with dose | position effect removed |
| [[Amsacrine (drug)]] 5 µM |  | 0.875× | -3.3 | 0.043 | 15/48 (SW48, BT-474, …) | top dose only |  |
| [[Rifaximin (drug)]] 5 µM |  | 0.835× | -3.1 | 0.068 | 20/48 (COLO 205, A549, …) | top dose only | position effect removed |
| [[Roxadustat (drug)]] 5 µM |  | 0.837× | -3.1 | 0.068 | 18/48 (C32, AN3 CA, …) | top dose only | position effect removed |
| [[Bimiralisib (drug)]] 5 µM |  | **0.720×** | -3.1 | 0.068 | 26/50 (NCI-H23, SHP-77, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 0.843× | -3.1 | 0.068 | 21/48 (HS-578T, RPMI-7951, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.54 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4353. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 570 | 15 (13 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.89× (z +24.5) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.47× (z +16.3) | — |
| [[A-172 (line)]] | wt | 616 | 14 (12 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +20.8) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.22× (z +15.9) | — |
| [[SNU-423 (line)]] | alt | 465 | 13 (9 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +25.9) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.58× (z +14.2) | — |
| [[SW480 (line)]] | alt | 921 | 10 (9 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 4.29× (z +19.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.19× (z +10.7) | [[Panobinostat (drug)]] 5 µM 0.497× (z -9.6) |
| [[H4 (line)]] | wt | 902 | 12 (10 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +17.9) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.56× (z +14.4) | — |
| [[PANC-1 (line)]] | alt | 898 | 9 (8 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +19.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.42× (z +13.6) | [[Panobinostat (drug)]] 5 µM 0.472× (z -11.4) |
| [[AsPC-1 (line)]] | alt | 610 | 9 (8 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 6.90× (z +37.0) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.92× (z +19.1) | [[Panobinostat (drug)]] 0.5 µM 0.435× (z -11.6) |
| [[HEC-1-A (line)]] | alt | 909 | 8 (6 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +16.7) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.39× (z +14.2) | [[Panobinostat (drug)]] 0.5 µM 0.483× (z -11.9) |
| [[HOP62 (line)]] | alt | 508 | 11 (9 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.77× (z +25.6) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.69× (z +13.9) | — |
| [[NCI-H1792 (line)]] | alt | 307 | 11 (9 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.93× (z +26.9) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.28× (z +10.2) | — |
| [[HS-578T (line)]] | alt | 498 | 10 (8 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +23.6) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.70× (z +17.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 705 | 10 (8 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.06× (z +23.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.23× (z +14.9) | — |
| [[SK-MEL-2 (line)]] | alt | 770 | 8 (6 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +23.4) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.77× (z +15.0) | [[Panobinostat (drug)]] 0.5 µM 0.528× (z -9.4) |
| [[C32 (line)]] | wt | 381 | 9 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.22× (z +27.4) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.26× (z +17.5) | — |
| [[KATO III (line)]] | alt | 755 | 9 (9 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.37× (z +19.3) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 705 | 8 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +27.1) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.74× (z +14.0) | — |
| [[LOX-IMVI (line)]] | wt | 655 | 8 (7 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.21× (z +20.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.23× (z +11.6) | — |
| [[NCI-H1573 (line)]] | alt | 426 | 8 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +22.6) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.95× (z +14.0) | — |
| [[Panc 03.27 (line)]] | alt | 483 | 8 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +22.0) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.43× (z +13.0) | — |
| [[SW1417 (line)]] | alt | 678 | 8 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +20.3) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.18× (z +14.8) | — |
| [[A498 (line)]] | wt | 771 | 7 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +26.3) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.40× (z +16.9) | — |
| [[A549 (line)]] | wt | 536 | 7 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.68× (z +25.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.18× (z +10.6) | — |
| [[CFPAC-1 (line)]] | alt | 472 | 7 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +19.9) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 1.95× (z +9.1) | — |
| [[HepG2_C3A (line)]] | wt | 428 | 4 (4 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.83× (z +14.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.422× (z -11.7) |
| [[HT-29 (line)]] | alt | 740 | 7 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.09× (z +17.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.84× (z +13.2) | — |
| [[hTERT-HPNE (line)]] | wt | 422 | 7 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +24.7) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.14× (z +14.5) | — |
| [[LS 180 (line)]] | wt | 544 | 7 (7 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.75× (z +20.0) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 735 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +23.0) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.57× (z +15.5) | — |
| [[SW 900 (line)]] | alt | 635 | 7 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +22.1) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.20× (z +11.6) | — |
| [[COLO 205 (line)]] | alt | 416 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +24.4) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.01× (z +8.8) | — |
| [[J82 (line)]] | alt | 650 | 6 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.23× (z +21.1) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 821 | 4 (4 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +16.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.508× (z -10.0) |
| [[SNU-1 (line)]] | wt | 528 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.85× (z +16.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.49× (z +10.9) | — |
| [[AN3 CA (line)]] | alt | 851 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +11.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.60× (z +10.3) | — |
| [[BT-474 (line)]] | alt | 881 | 3 (2 ⚠) | 2 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.46× (z +14.0) | [[Panobinostat (drug)]] 0.5 µM 0.457× (z -12.2) |
| [[Hs 766T (line)]] | wt | 410 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.11× (z +17.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.34× (z +10.4) | — |
| [[NCI-H2030 (line)]] | alt | 777 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +19.9) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.95× (z +9.0) | — |
| [[NCI-H2347 (line)]] | alt | 616 | 5 (5 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +12.4) ⚠ cell-cycle shift, explains ~6% of this change | — |
| [[A-427 (line)]] | wt | 903 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.66× (z +14.0) ⚠ toxic; transcription drop | [[Selinexor (drug)]] 5 µM 0.630× (z -9.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.534× (z -9.1) |
| [[SW48 (line)]] | wt | 831 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.50× (z +13.9) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.454× (z -8.7) ⚠ cell-cycle shift, explains ~62% of this change |
| [[CHP-212 (line)]] | wt | 659 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.33× (z +13.3) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 919 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.72× (z +14.5) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 950 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +14.6) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[RKO (line)]] | wt | 654 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.81× (z +19.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.60× (z +11.7) | — |
| [[SW 1088 (line)]] | alt | 634 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.42× (z +15.1) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.67× (z +11.4) | — |
| [[C-33 A (line)]] | alt | 859 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.84× (z +12.6) ⚠ toxic; transcription drop | — |
| [[SW 1271 (line)]] | alt | 690 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +14.5) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[NCI-H2122 (line)]] | alt | 564 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 613 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 851 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4353), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*29 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHD4]] | +0.69 | +0.62 / +0.66 | both halves | 7e-06 | STRING 481 |
| [[HNRNPU]] | +0.69 | +0.67 / +0.63 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 979 |
| [[YWHAE]] | +0.69 | +0.62 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[ILF3]] | +0.67 | +0.70 / +0.57 | both halves | 1e-05 | STRING 994 |
| [[HNRNPM]] | +0.67 | +0.61 / +0.67 | both halves | 7e-06 | same gene group; pathway: Dengue Virus-Host Interactions; STRING 987 |
| [[HNRNPK]] | +0.67 | +0.65 / +0.61 | both halves | 7e-06 | same gene group; pathway: Dengue Virus-Host Interactions; STRING 983 |
| [[DARS2]] | +0.66 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[SRSF1]] | +0.66 | +0.61 / +0.57 | both halves | 9e-06 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 972 |
| [[HNRNPL]] | +0.65 | +0.60 / +0.57 | both halves | 1e-05 | same gene group; pathway: Dengue Virus-Host Interactions; STRING 999 |
| [[DDX3X]] | +0.65 | +0.55 / +0.59 | both halves | 1e-05 | pathway: Dengue Virus-Host Interactions; STRING 726 |
| [[TASOR]] | +0.64 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[SFPQ]] | +0.63 | +0.55 / +0.64 | both halves | 1e-05 | same gene group; STRING 939 |

## Genes that move opposite

*71 of its nearest partners move opposite, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LCMT1]] | -0.71 | -0.63 / -0.68 | both halves | 7e-06 |  |
| [[CCZ1B]] | -0.71 | -0.68 / -0.63 | both halves | 7e-06 |  |
| [[COMMD6]] | -0.70 | -0.71 / -0.59 | both halves | 7e-06 |  |
| [[LIN7B]] | -0.68 | -0.49 / -0.64 | both halves | 1e-05 |  |
| [[CIAO2B]] | -0.67 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[CAMLG]] | -0.66 | -0.59 / -0.60 | both halves | 7e-06 |  |
| [[RPP21]] | -0.66 | -0.45 / -0.65 | both halves | 3e-05 |  |
| [[PLD3]] | -0.66 | -0.70 / -0.58 | both halves | 7e-06 |  |
| [[CCZ1]] | -0.66 | -0.59 / -0.60 | both halves | 7e-06 |  |
| [[MALSU1]] | -0.66 | -0.57 / -0.59 | both halves | 1e-05 |  |
| [[KLHL7]] | -0.66 | -0.55 / -0.60 | both halves | 1e-05 |  |
| [[ATP5MJ]] | -0.66 | -0.61 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **-** arm (projection on the module's main direction -0.737). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-36.8, -25.0); signed map (15.1, -37.8). **Vector** length 128, 56.7% of its response variance represented; |z| ≥ 3 in 1,692 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.59 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +7.9 | +24.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.4 | +11.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.8 | +18.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.4 | +0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.0 | +0.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +4.9 | +3.4 |
|  | [[Demeclocycline (drug)]] 5 µM |  | +3.9 | -0.4 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -8.4 | -2.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -7.4 | -7.6 |
|  | [[Belinostat (drug)]] 5 µM |  | -6.8 | -6.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | -6.0 | -7.9 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | -4.3 | -3.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -4.2 | -3.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.1 | -1.5 |
|  | [[Amsacrine (drug)]] 5 µM |  | -4.0 | -3.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.6 | -1.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.6 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | heterogeneous nuclear ribonucleoprotein A2/B1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p15.2 — chr7:26,171,151-26,201,529 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HNRNPA2, HNRNPB1; previously HNRPA2B1 |
| Gene groups (HGNC) | RNA binding motif containing; Heterogeneous nuclear ribonucleoproteins |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 14 pathways, smallest: Gene and protein expression by JAK-STAT signaling after Interleukin-12 stimulation; Interleukin-12 signaling; Interleukin-12 family signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P22626](https://www.uniprot.org/uniprotkb/P22626) (Heterogeneous nuclear ribonucleoproteins A2/B1):

> Heterogeneous nuclear ribonucleoprotein (hnRNP) that associates with nascent pre-mRNAs, packaging them into hnRNP particles. The hnRNP particle arrangement on nascent hnRNA is non-random and sequence-dependent and serves to condense and stabilize the transcripts and minimize tangling and knotting. Packaging plays a role in various processes such as transcription, pre-mRNA processing, RNA nuclear export, subcellular location, mRNA translation and stability of mature mRNAs. Forms hnRNP particles …

**Summary**, from NCBI Gene [3181](https://www.ncbi.nlm.nih.gov/gene/3181):

> This gene belongs to the A/B subfamily of ubiquitously expressed heterogeneous nuclear ribonucleoproteins (hnRNPs). The hnRNPs are RNA binding proteins and they complex with heterogeneous nuclear RNA (hnRNA). These proteins are associated with pre-mRNAs in the nucleus and appear to influence pre-mRNA processing and other aspects of mRNA metabolism and transport. While all of the hnRNPs are present in the nucleus, some seem to shuttle between the nucleus and the cytoplasm. The hnRNP proteins …

**Accessions** — [HGNC:5033](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5033) · Entrez [3181](https://www.ncbi.nlm.nih.gov/gene/3181) · UniProt [P22626](https://www.uniprot.org/uniprotkb/P22626) · Ensembl [ENSG00000122566](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122566)

## Data

Gene col 4353: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4353); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4353, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4353]; `tensor/DDL_lfc|DDL_z.npy` [4353]; `embed/gene_vectors.npy` [4353]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4353 or target_col == 4353). Every well: [[HNRNPA2B1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HNRNPA2B1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
