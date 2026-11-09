---
symbol: "CSNK1A1"
type: "gene"
col: 3492
ensembl_id: "ENSG00000113712"
name: "casein kinase 1 alpha 1"
location: "5q32"
module: 65
arm: "-"
pooled_cpm: 494.56
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 3
n_dd_up_clean: 6
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# CSNK1A1

*casein kinase 1 alpha 1* — 5q32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.04× (z +27.6, q 0e+00, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.730× (z -11.5, q 8e-28, down in 41 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 0.836× (z -6.8, q 1e-09, down in 22 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (A498 0.630×, A549 0.689×, PANC-1 0.747×; ⚠ cell-cycle shift, explains ~56% of this change); [[Belinostat (drug)]] 5 µM in 3 lines (PANC-1 0.613×, CFPAC-1 0.615×, SW 900 0.562×; ⚠ cell-cycle shift, explains ~0% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 0.478×, NCI-H2347 0.654×; ⚠ toxic); [[Belumosudil (drug)]] 5 µM in 1 line (NCI-H23 0.636×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SYAP1]] (+0.65, fdr 7e-06), [[SUPT6H]] (+0.61, fdr 7e-06), [[ZSWIM6]] (+0.60, fdr 9e-06); moves opposite to [[ABCB10]] (-0.57, fdr 2e-05), [[ILKAP]] (-0.55, fdr 1e-05), [[NBPF1]] (-0.54, fdr 2e-05).
> It sits in the **-** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3492.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.04×** | +27.6 | 0e+00 | 48/49 (LoVo, MIA PaCa-2, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.97×** | +21.6 | 0e+00 | 46/48 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.48×** | +14.9 | 0e+00 | 41/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.27×** | +12.8 | 2e-35 | 29/48 (AsPC-1, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.38×** | +11.7 | 8e-30 | 33/48 (HS-578T, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.28×** | +9.4 | 4e-19 | 36/48 (SW480, LoVo, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.27×** | +9.1 | 5e-18 | 30/48 (SW480, LoVo, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.25×** | +8.3 | 8e-15 | 29/48 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.23×** | +7.9 | 3e-13 | 28/48 (HT-29, COLO 205, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.22×** | +7.5 | 4e-12 | 26/48 (HT-29, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 1.20× | +6.7 | 9e-10 | 22/48 (HS-578T, C32, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | 1.17× | +6.0 | 8e-08 | 20/48 (LoVo, SW480, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +5.5 | 2e-06 | 18/48 (A-172, HT-29, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | 1.14× | +5.1 | 1e-05 | 19/48 (HS-578T, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.27×** | +4.7 | 8e-05 | 29/48 (HOP62, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | 1.14× | +3.6 | 0.009 | 12/49 (A-172, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.14× | +3.6 | 0.010 | 13/47 (NCI-H2347, HEC-1-A, …) | all doses, stronger at high dose | low cells (technical?); noisy plate (z scaled) |
| [[Artesunate (drug)]] 0.5 µM |  | 1.09× | +3.4 | 0.017 | 1/48 (A-427) | rises with dose |  |
| [[Fumaric acid (drug)]] 5 µM |  | 1.09× | +3.1 | 0.044 | 0/49 | top dose only | plate-row cell shift |
| [[Naproxen (drug)]] 5 µM |  | 1.09× | +3.1 | 0.055 | 4/48 (RPMI-7951, AsPC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 13 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3492.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (A498 0.630×, A549 0.689×, PANC-1 0.747×; ⚠ cell-cycle shift, explains ~56% of this change); [[Belinostat (drug)]] 5 µM in 3 lines (PANC-1 0.613×, CFPAC-1 0.615×, SW 900 0.562×; ⚠ cell-cycle shift, explains ~0% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 0.478×, NCI-H2347 0.654×; ⚠ toxic); [[Belumosudil (drug)]] 5 µM in 1 line (NCI-H23 0.636×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.730×** | -11.5 | 8e-28 | 41/47 (RKO, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | 0.868× | -7.6 | 9e-12 | 17/48 (SNU-423, hTERT-HPNE, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.831×** | -7.0 | 4e-10 | 25/48 (MIA PaCa-2, NCI-H2347, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.836× | -6.8 | 1e-09 | 22/48 (NCI-H23, CFPAC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.853× | -6.1 | 2e-07 | 21/48 (PANC-1, NCI-H23, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.853× | -5.8 | 6e-07 | 20/44 (NCI-H1573, LoVo, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.860× | -5.7 | 8e-07 | 22/48 (PANC-1, CFPAC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.863× | -5.6 | 2e-06 | 17/48 (SW 900, COLO 205, …) | all doses, flat |  |
| [[Radotinib (drug)]] 5 µM |  | 0.905× | -5.3 | 6e-06 | 3/48 (RKO, AsPC-1, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.866× | -5.3 | 8e-06 | 14/48 (NCI-H23, NCI-H460, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.883× | -4.7 | 1e-04 | 13/48 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.924× | -4.2 | 0.001 | 1/48 (AN3 CA) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.817×** | -4.0 | 0.003 | 24/49 (CFPAC-1, SW 900, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.900× | -4.0 | 0.003 | 5/48 (CFPAC-1, NCI-H23, …) | rises with dose |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 0.905× | -3.8 | 0.006 | 4/48 (RKO, COLO 205, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | 0.872× | -3.7 | 0.008 | 15/47 (J82, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | 0.938× | -3.5 | 0.019 | 0/48 | top dose only |  |
| [[Afatinib (drug)]] 5 µM |  | 0.903× | -3.4 | 0.025 | 4/49 (SNU-423, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.916× | -3.3 | 0.025 | 4/49 (SK-MEL-2, RKO, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 5 µM |  | 0.942× | -3.2 | 0.036 | 2/48 (HT-29, BT-474) | inconsistent across doses |  |
| [[venetoclax (drug)]] 0.05 µM |  | 0.915× | -3.2 | 0.038 | 5/49 (A-427, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.917× | -3.2 | 0.038 | 6/48 (RKO, HepG2/C3A, …) | all doses, flat |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.944× | -3.1 | 0.046 | 1/48 (AN3 CA) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3492. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 427 | 7 (2 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 9.09× (z +21.5) | [[Belinostat (drug)]] 5 µM 0.614× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 524 | 8 (4 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.79× (z +25.7) | — |
| [[RKO (line)]] | wt | 458 | 6 (3 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.16× (z +17.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.478× (z -12.8) ⚠ toxic |
| [[SW48 (line)]] | wt | 498 | 7 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.68× (z +16.1) | — |
| [[AsPC-1 (line)]] | alt | 536 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +24.4) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.01× (z +17.9) | — |
| [[BT-474 (line)]] | alt | 479 | 6 (1 ⚠) | 0 | [[PH-797804 (drug)]] 5 µM 4.50× (z +14.2) | — |
| [[HEC-1-A (line)]] | alt | 511 | 6 (3 ⚠) | 0 | [[PH-797804 (drug)]] 5 µM 4.81× (z +21.2) | — |
| [[HOP62 (line)]] | alt | 537 | 5 (2 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.05× (z +16.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.632× (z -10.1) ⚠ toxic |
| [[HS-578T (line)]] | alt | 480 | 6 (3 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 4.54× (z +17.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 637 | 5 (2 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 8.81× (z +24.1) | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.606× (z -10.6) ⚠ cell-cycle shift, explains ~20% of this change |
| [[NCI-H23 (line)]] | alt | 605 | 1 | 5 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 4.52× (z +15.4) | [[Dinaciclib (drug)]] 0.5 µM 0.538× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Belumosudil (drug)]] 5 µM 0.636× (z -8.6) |
| [[SNU-1 (line)]] | wt | 349 | 6 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 8.12× (z +16.2) | — |
| [[SW480 (line)]] | alt | 461 | 6 (3 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.09× (z +23.1) | — |
| [[C32 (line)]] | wt | 439 | 3 (3 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.54× (z +10.8) ⚠ cell-cycle shift, explains ~50% of this change | [[Belinostat (drug)]] 5 µM 0.576× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 562 | 3 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.48× (z +14.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.596× (z -9.0) ⚠ toxic |
| [[HT-29 (line)]] | alt | 501 | 5 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 3.59× (z +15.6) | — |
| [[LS 180 (line)]] | wt | 494 | 4 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.43× (z +14.8) | [[Dinaciclib (drug)]] 5 µM 0.609× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 711 | 4 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.01× (z +14.7) | [[Dinaciclib (drug)]] 5 µM 0.443× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 472 | 5 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.40× (z +19.9) | — |
| [[SW 900 (line)]] | alt | 420 | 3 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.40× (z +11.2) | [[Belinostat (drug)]] 5 µM 0.562× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 702 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.78× (z +13.4) | [[Dinaciclib (drug)]] 0.5 µM 0.550× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 438 | 4 (1 ⚠) | 0 | [[PH-797804 (drug)]] 5 µM 3.55× (z +13.0) | — |
| [[Panc 03.27 (line)]] | alt | 487 | 4 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 4.54× (z +16.8) | — |
| [[PANC-1 (line)]] | alt | 663 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.40× (z +16.3) | [[Panobinostat (drug)]] 5 µM 0.606× (z -12.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 547 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.54× (z +15.0) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 2.91× (z +13.8) | — |
| [[A549 (line)]] | wt | 406 | 3 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.75× (z +19.8) | — |
| [[CFPAC-1 (line)]] | alt | 520 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 2.95× (z +13.4) | [[Belinostat (drug)]] 5 µM 0.615× (z -11.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 362 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 3.40× (z +13.1) | — |
| [[NCI-H1792 (line)]] | alt | 381 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 4.09× (z +13.6) | — |
| [[NCI-H2030 (line)]] | alt | 525 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 3.74× (z +13.1) | — |
| [[A-172 (line)]] | wt | 460 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 4.15× (z +17.7) | — |
| [[A498 (line)]] | wt | 486 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 2.46× (z +10.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.630× (z -14.2) ⚠ cell-cycle shift, explains ~56% of this change |
| [[C-33 A (line)]] | alt | 336 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 4.06× (z +12.2) | — |
| [[LOX-IMVI (line)]] | wt | 467 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 5.55× (z +21.0) | — |
| [[NCI-H2347 (line)]] | alt | 526 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 1.96× (z +9.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.654× (z -11.1) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 398 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 4.04× (z +14.6) | — |
| [[SK-MEL-2 (line)]] | alt | 458 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 4.50× (z +17.2) | — |
| [[SNU-423 (line)]] | alt | 382 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 2.72× (z +9.5) | — |
| [[AN3 CA (line)]] | alt | 532 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.66× (z +9.3) | — |
| [[H4 (line)]] | wt | 456 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.15× (z +12.6) | — |
| [[HepG2_C3A (line)]] | wt | 399 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 2.56× (z +8.8) | — |
| [[Hs 766T (line)]] | wt | 494 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.53× (z +17.4) | — |
| [[J82 (line)]] | alt | 313 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 2.26× (z +9.2) | — |
| [[SHP-77 (line)]] | alt | 295 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.90× (z +12.0) | — |
| [[CHP-212 (line)]] | wt | 507 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 571 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 483 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 458 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 547 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 550 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3492), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*48 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SYAP1]] | +0.65 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[SUPT6H]] | +0.61 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[ZSWIM6]] | +0.60 | +0.59 / +0.57 | both halves | 9e-06 |  |
| [[TUT7]] | +0.58 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[KDM5A]] | +0.56 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[USP8]] | +0.54 | +0.56 / +0.46 | both halves | 3e-05 | pathway: Signaling by WNT |
| [[SETX]] | +0.52 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[SON]] | +0.52 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[USP16]] | +0.52 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[KLHL4]] | +0.51 | +0.52 / +0.43 | both halves | 3e-05 |  |
| [[AP1G1]] | +0.51 | +0.57 / +0.46 | both halves | 2e-05 |  |
| [[WDR26]] | +0.51 | +0.51 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*52 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABCB10]] | -0.57 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[ILKAP]] | -0.55 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[NBPF1]] | -0.54 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[FIP1L1]] | -0.53 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[MTX2]] | -0.53 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[RFXAP]] | -0.53 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[SEC61A2]] | -0.53 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[TADA1]] | -0.53 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[GCSH]] | -0.53 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[NAPB]] | -0.52 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[RWDD4]] | -0.52 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[CAMKK2]] | -0.51 | -0.48 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **-** arm (projection on the module's main direction -0.429). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-21.3, 12.4); signed map (2.7, 25.7). **Vector** length 114, 37.8% of its response variance represented; |z| ≥ 3 in 1,603 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +6.5 | +27.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.0 | +6.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +0.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.3 | +21.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | -1.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +2.9 | +3.4 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.9 | -11.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | -5.7 | -7.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -5.4 | +0.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | -4.9 | -3.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | -4.6 | -7.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.8 | -1.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.5 | -5.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.5 | -6.8 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -3.3 | -4.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.1 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | casein kinase 1 alpha 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q32 — chr5:149,492,982-149,551,471 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CK1, CK1a, CK1alpha, CKIa, CKIalpha |
| Gene groups (HGNC) | Casein kinase 1 family |
| Reactome | 36 pathways, smallest: APC truncation mutants have impaired AXIN binding; AXIN missense mutants destabilize the destruction complex; Signaling by AMER1 mutants |
| Matched by | ensembl_id |

**Function**, from UniProt [P48729](https://www.uniprot.org/uniprotkb/P48729) (Casein kinase I isoform alpha):

> Casein kinases are operationally defined by their preferential utilization of acidic proteins such as caseins as substrates. Phosphorylates a large number of proteins. Participates in Wnt signaling. Phosphorylates CTNNB1 at 'Ser-45'. May phosphorylate PER1 and PER2 (By similarity). May play a role in segregating chromosomes during mitosis. May play a role in keratin cytoskeleton disassembly and thereby, it may regulate epithelial cell migration. Acts as a positive regulator of mTORC1 and mTORC2 …

**Summary**, from NCBI Gene [1452](https://www.ncbi.nlm.nih.gov/gene/1452):

> Enables protein serine/threonine kinase activity. Involved in several processes, including intermediate filament cytoskeleton organization; positive regulation of proteasomal ubiquitin-dependent protein catabolic process; and regulation of signal transduction. Located in cytoskeleton; cytosol; and nucleus. Part of beta-catenin destruction complex. Biomarker of Alzheimer's disease and inclusion body myositis. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:2451](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2451) · Entrez [1452](https://www.ncbi.nlm.nih.gov/gene/1452) · UniProt [P48729](https://www.uniprot.org/uniprotkb/P48729) · Ensembl [ENSG00000113712](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113712)

## Data

Gene col 3492: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3492); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3492, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3492]; `tensor/DDL_lfc|DDL_z.npy` [3492]; `embed/gene_vectors.npy` [3492]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3492 or target_col == 3492). Every well: [[CSNK1A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CSNK1A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
