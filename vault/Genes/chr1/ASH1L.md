---
symbol: "ASH1L"
type: "gene"
col: 3804
ensembl_id: "ENSG00000116539"
name: "ASH1 like histone lysine methyltransferase"
location: "1q22"
module: 23
arm: "+"
pooled_cpm: 498.83
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 14
n_dd_up_clean: 12
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# ASH1L

*ASH1 like histone lysine methyltransferase* — 1q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.00× (z +57.8, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.581× (z -20.2, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANKHD1-EIF4EBP3]] (+0.76, fdr 7e-06), [[CREBBP]] (+0.74, fdr 7e-06), [[MED13]] (+0.74, fdr 7e-06); moves opposite to [[RIMS3]] (-0.68, fdr 1e-05), [[ATP13A2]] (-0.66, fdr 2e-05), [[MOCS1]] (-0.65, fdr 2e-05).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3804.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.00×** | +57.8 | 0e+00 | 48/48 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.70×** | +36.9 | 0e+00 | 48/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.25×** | +29.0 | 0e+00 | 47/48 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.12×** | +28.0 | 0e+00 | 48/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.00×** | +25.9 | 0e+00 | 48/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.82×** | +22.2 | 0e+00 | 48/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.79×** | +21.7 | 0e+00 | 44/48 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.97×** | +21.2 | 0e+00 | 48/49 (SW480, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.87×** | +12.2 | 3e-32 | 45/48 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.39×** | +12.1 | 8e-32 | 31/48 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.25×** | +8.3 | 5e-15 | 31/48 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.23×** | +7.6 | 2e-12 | 26/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +7.3 | 1e-11 | 21/49 (AsPC-1, Hs 766T, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.26×** | +4.4 | 4e-04 | 27/48 (CFPAC-1, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.13× | +4.2 | 9e-04 | 19/47 (A498, NCI-H460, …) | top dose only |  |
| [[Irinotecan (hydrochloride) (drug)]] 0.05 µM |  | 1.10× | +3.1 | 0.059 | 0/48 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3804.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.581×** | -20.2 | 0e+00 | 47/48 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.597×** | -19.2 | 0e+00 | 47/48 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.647×** | -16.3 | 0e+00 | 47/48 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.662×** | -15.1 | 0e+00 | 45/49 (A498, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.688×** | -13.4 | 5e-39 | 38/44 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.720×** | -12.2 | 2e-32 | 44/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~21% of this change | **0.731×** | -11.3 | 1e-27 | 41/47 (SW1417, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.812×** | -11.0 | 3e-26 | 32/48 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.728×** | -11.0 | 4e-26 | 34/45 (NCI-H2030, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.799×** | -8.3 | 9e-15 | 32/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.813×** | -7.7 | 5e-13 | 27/48 (HCT15, KATO III, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.813×** | -7.7 | 6e-13 | 26/49 (SW480, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.706×** | -6.8 | 5e-10 | 39/49 (A498, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 0.843× | -6.4 | 6e-09 | 23/48 (SW 900, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.766×** | -5.2 | 8e-06 | 32/49 (PANC-1, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 0.883× | -4.5 | 3e-04 | 7/48 (NCI-H1573, NCI-H460, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | 0.884× | -3.3 | 0.031 | 12/48 (HEC-1-A, Panc 03.27, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Infigratinib (drug)]] 0.05 µM |  | 0.918× | -3.0 | 0.069 | 2/48 (HCT15, SW 1271) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 0.947× | -2.9 | 0.096 | 0/48 | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3804. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 724 | 9 (1 ⚠) | 8 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +31.6) | [[Panobinostat (drug)]] 5 µM 0.514× (z -14.7) |
| [[LOX-IMVI (line)]] | wt | 462 | 9 (1 ⚠) | 7 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +21.8) | [[Panobinostat (drug)]] 5 µM 0.482× (z -14.2) |
| [[NCI-H460 (line)]] | wt | 834 | 12 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +44.0) | [[Dinaciclib (drug)]] 5 µM 0.452× (z -20.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.578× (z -14.7) |
| [[HT-29 (line)]] | alt | 485 | 8 (1 ⚠) | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +32.9) | [[Panobinostat (drug)]] 0.5 µM 0.500× (z -15.4) |
| [[NCI-H1573 (line)]] | alt | 616 | 10 (2 ⚠) | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +33.7) | [[Panobinostat (drug)]] 5 µM 0.467× (z -14.9) |
| [[RPMI-7951 (line)]] | alt | 470 | 10 (1 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +33.9) | [[Panobinostat (drug)]] 5 µM 0.510× (z -14.0) |
| [[A498 (line)]] | wt | 484 | 8 (1 ⚠) | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.70× (z +54.0) | [[Panobinostat (drug)]] 5 µM 0.483× (z -18.0) |
| [[CHP-212 (line)]] | wt | 758 | 8 (1 ⚠) | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +18.6) | [[Dinaciclib (drug)]] 5 µM 0.310× (z -17.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.526× (z -9.7) |
| [[KATO III (line)]] | alt | 394 | 8 (1 ⚠) | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +26.2) | [[Panobinostat (drug)]] 0.5 µM 0.506× (z -15.4) |
| [[NCI-H2030 (line)]] | alt | 678 | 8 (1 ⚠) | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.93× (z +43.7) | [[Dinaciclib (drug)]] 0.05 µM 0.513× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.569× (z -12.8) |
| [[Panc 03.27 (line)]] | alt | 442 | 9 (2 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +32.0) | [[Panobinostat (drug)]] 5 µM 0.602× (z -11.3) |
| [[PANC-1 (line)]] | alt | 498 | 10 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.69× (z +65.7) | [[Panobinostat (drug)]] 0.5 µM 0.539× (z -18.6) |
| [[SNU-423 (line)]] | alt | 391 | 7 (1 ⚠) | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +41.3) | [[Dinaciclib (drug)]] 5 µM 0.549× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.602× (z -11.3) |
| [[A-172 (line)]] | wt | 537 | 8 (1 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +47.0) | [[Panobinostat (drug)]] 5 µM 0.529× (z -16.2) |
| [[A549 (line)]] | wt | 430 | 9 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.20× (z +53.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.627× (z -17.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.541× (z -16.0) |
| [[CFPAC-1 (line)]] | alt | 490 | 6 (1 ⚠) | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +32.0) | [[Panobinostat (drug)]] 5 µM 0.492× (z -16.2) |
| [[COLO 205 (line)]] | alt | 638 | 9 (2 ⚠) | 4 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.91× (z +32.0) | [[Panobinostat (drug)]] 0.5 µM 0.472× (z -15.2) |
| [[HCT15 (line)]] | alt | 619 | 6 (1 ⚠) | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +22.4) | [[Dinaciclib (drug)]] 0.5 µM 0.439× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.475× (z -15.1) |
| [[HEC-1-A (line)]] | alt | 466 | 9 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.00× (z +51.6) | [[Panobinostat (drug)]] 5 µM 0.519× (z -17.2) |
| [[HOP62 (line)]] | alt | 555 | 8 (1 ⚠) | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +32.8) | [[Panobinostat (drug)]] 5 µM 0.481× (z -14.9) |
| [[RKO (line)]] | wt | 414 | 10 (2 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +25.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.605× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~21% of this change |
| [[SW1417 (line)]] | alt | 400 | 9 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +29.6) | [[Panobinostat (drug)]] 0.5 µM 0.518× (z -14.5) |
| [[SW480 (line)]] | alt | 427 | 10 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +31.6) | [[Panobinostat (drug)]] 0.05 µM 0.634× (z -12.8) |
| [[AsPC-1 (line)]] | alt | 446 | 10 (3 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +33.7) | [[Panobinostat (drug)]] 5 µM 0.625× (z -9.9) |
| [[LS 180 (line)]] | wt | 370 | 9 (1 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.99× (z +22.7) | [[Panobinostat (drug)]] 0.5 µM 0.529× (z -13.2) |
| [[NCI-H1792 (line)]] | alt | 478 | 9 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +33.8) | [[Panobinostat (drug)]] 5 µM 0.542× (z -13.4) |
| [[Hs 766T (line)]] | wt | 467 | 8 (2 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +33.2) | [[Dinaciclib (drug)]] 5 µM 0.549× (z -12.0) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 991 | 8 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +39.8) | [[Dinaciclib (drug)]] 5 µM 0.411× (z -19.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.663× (z -9.5) |
| [[NCI-H2347 (line)]] | alt | 400 | 9 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +41.7) | [[Panobinostat (drug)]] 5 µM 0.600× (z -10.6) |
| [[BT-474 (line)]] | alt | 333 | 7 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +20.5) | [[Panobinostat (drug)]] 0.5 µM 0.513× (z -12.9) |
| [[C32 (line)]] | wt | 375 | 6 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +18.1) | [[Panobinostat (drug)]] 0.5 µM 0.542× (z -11.4) |
| [[H4 (line)]] | wt | 381 | 9 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.23× (z +34.4) | [[Panobinostat (drug)]] 0.5 µM 0.582× (z -9.2) |
| [[hTERT-HPNE (line)]] | wt | 413 | 9 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +28.2) | [[Belinostat (drug)]] 5 µM 0.632× (z -8.6) |
| [[LoVo (line)]] | wt | 355 | 9 (2 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.87× (z +33.2) | [[Panobinostat (drug)]] 0.5 µM 0.662× (z -10.1) |
| [[SK-MEL-2 (line)]] | alt | 473 | 6 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +34.4) | [[Panobinostat (drug)]] 5 µM 0.574× (z -11.9) |
| [[A-427 (line)]] | wt | 472 | 8 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +23.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.666× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 305 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.21× (z +43.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 563 | 6 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +37.2) | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.547× (z -14.3) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SNU-1 (line)]] | wt | 470 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +32.3) | — |
| [[HepG2_C3A (line)]] | wt | 327 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +26.0) | — |
| [[J82 (line)]] | alt | 418 | 6 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +39.5) | [[Panobinostat (drug)]] 0.5 µM 0.612× (z -12.1) |
| [[SHP-77 (line)]] | alt | 673 | 6 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.47× (z +21.4) | [[Dinaciclib (drug)]] 5 µM 0.512× (z -15.3) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 516 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +15.8) | — |
| [[SW48 (line)]] | wt | 371 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +28.4) | — |
| [[AN3 CA (line)]] | alt | 447 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +15.6) | [[Selinexor (drug)]] 5 µM 0.570× (z -10.4) ⚠ cell-cycle shift, explains ~15% of this change |
| [[SW 1271 (line)]] | alt | 437 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +11.9) | — |
| [[NCI-H661 (line)]] | alt | 396 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.380× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~21% of this change |
| [[SW 1088 (line)]] | alt | 370 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +12.6) | — |
| [[NCI-H2122 (line)]] | alt | 592 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 513 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3804), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKHD1-EIF4EBP3]] | +0.76 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[CREBBP]] | +0.74 | +0.66 / +0.62 | both halves | 7e-06 | same gene group; pathway: Chromatin modifying enzymes; STRING 478 |
| [[MED13]] | +0.74 | +0.65 / +0.62 | both halves | 7e-06 | STRING 464 |
| [[BPTF]] | +0.74 | +0.69 / +0.74 | both halves | 7e-06 | same gene group; STRING 688 |
| [[GTF2IRD2B]] | +0.73 | +0.69 / +0.53 | both halves | 1e-05 |  |
| [[NIFK-AS1]] | +0.73 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[AEBP2]] | +0.72 | +0.65 / +0.59 | both halves | 7e-06 | pathway: Chromatin modifying enzymes |
| [[DNAI4]] | +0.71 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[MZF1-AS1]] | +0.70 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[SON]] | +0.69 | +0.63 / +0.56 | both halves | 1e-05 | same gene group; STRING 444 |
| [[RSF1]] | +0.69 | +0.63 / +0.66 | both halves | 7e-06 | same gene group; STRING 487 |
| [[CCDC90B-AS1]] | +0.69 | +0.60 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RIMS3]] | -0.68 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[ATP13A2]] | -0.66 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[MOCS1]] | -0.65 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[SEMA4F]] | -0.65 | -0.40 / -0.57 | both halves | 5e-05 |  |
| [[STARD3NL]] | -0.64 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[APMAP]] | -0.64 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[MBOAT2]] | -0.64 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[ANXA6]] | -0.63 | -0.63 / -0.43 | both halves | 3e-05 |  |
| [[POMGNT2]] | -0.63 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[FBXW2]] | -0.63 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[USP35]] | -0.63 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[RNF216P1]] | -0.62 | -0.55 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises ASH1L's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises ASH1L's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.685). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (2.8, 10.2); signed map (21.4, -9.5). **Vector** length 131, 52.1% of its response variance represented; |z| ≥ 3 in 1,771 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +12.1 | +7.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +10.7 | +4.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +8.3 | +2.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.8 | +29.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.6 | +57.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +7.1 | +2.7 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +5.3 | +1.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.2 | +1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.4 | +1.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.2 | +1.2 |
| fall | [[Belinostat (drug)]] 5 µM |  | -8.3 | -16.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -8.2 | -11.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -7.8 | -19.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | -6.7 | -20.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -6.6 | -12.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -4.9 | -6.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -4.3 | -2.3 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -4.3 | -1.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.1 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | ASH1 like histone lysine methyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q22 — chr1:155,335,268-155,563,162 (-) |
| Ensembl biotype | protein_coding |
| Also known as | huASH1, ASH1, ASH1L1, KMT2H |
| Gene groups (HGNC) | PHD finger proteins; Histone lysine methyltransferases; Bromodomain containing; SET domain containing; MicroRNA protein coding host genes |
| Reactome | 3 pathways, smallest: PKMTs methylate histone lysines; Chromatin modifying enzymes; Chromatin organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NR48](https://www.uniprot.org/uniprotkb/Q9NR48) (Histone-lysine N-methyltransferase ASH1L):

> Histone methyltransferase specifically trimethylating 'Lys-36' of histone H3 forming H3K36me3. Also monomethylates 'Lys-9' of histone H3 (H3K9me1) in vitro (By similarity). The physiological significance of the H3K9me1 activity is unclear (By similarity).

**Summary**, from NCBI Gene [55870](https://www.ncbi.nlm.nih.gov/gene/55870):

> This gene encodes a member of the trithorax group of transcriptional activators. The protein contains four AT hooks, a SET domain, a PHD-finger motif, and a bromodomain. It is localized to many small speckles in the nucleus, and also to cell-cell tight junctions. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:19088](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19088) · Entrez [55870](https://www.ncbi.nlm.nih.gov/gene/55870) · UniProt [Q9NR48](https://www.uniprot.org/uniprotkb/Q9NR48) · Ensembl [ENSG00000116539](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116539)

## Data

Gene col 3804: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3804); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3804, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3804]; `tensor/DDL_lfc|DDL_z.npy` [3804]; `embed/gene_vectors.npy` [3804]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3804 or target_col == 3804). Every well: [[ASH1L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ASH1L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
