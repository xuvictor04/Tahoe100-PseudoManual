---
symbol: "PDCD11"
type: "gene"
col: 7323
ensembl_id: "ENSG00000148843"
name: "programmed cell death 11"
location: "10q24.33"
module: 5
arm: "+"
pooled_cpm: 66.39
n_lines_expressing: 50
n_dd_up: 56
n_dd_down: 11
n_dd_up_clean: 33
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# PDCD11

*programmed cell death 11* — 10q24.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 56 drug-doses (23 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.27× (z +22.8, q 0e+00, up in 48 of 48 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 3.07× (z +21.6, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 0.749× (z -5.4, q 4e-05, down in 30 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LYAR]] (+0.86, fdr 7e-06), [[NOP16]] (+0.82, fdr 7e-06), [[WDR3]] (+0.80, fdr 7e-06); moves opposite to [[ATOSA]] (-0.64, fdr 7e-06), [[ITM2B]] (-0.61, fdr 9e-06).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 69 in all, 28 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 56 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 23 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7323.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **3.27×** | +22.8 | 0e+00 | 48/48 (SW480, NCI-H2347, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.07×** | +21.6 | 0e+00 | 48/48 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.48×** | +17.5 | 0e+00 | 47/48 (SW480, A-172, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.15×** | +14.8 | 0e+00 | 47/48 (NCI-H460, A498, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.00×** | +13.3 | 2e-38 | 37/48 (CFPAC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **2.53×** | +9.4 | 7e-19 | 45/48 (NCI-H1573, SW1417, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.47×** | +9.1 | 6e-18 | 37/48 (SW480, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.40×** | +9.0 | 1e-17 | 31/48 (NCI-H1573, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.59×** | +9.0 | 2e-17 | 42/48 (SW480, AN3 CA, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **1.61×** | +8.8 | 6e-17 | 35/47 (NCI-H1792, NCI-H1573, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **1.52×** | +8.1 | 4e-14 | 32/47 (NCI-H1573, SW480, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.49×** | +7.7 | 5e-13 | 31/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **1.51×** | +7.6 | 1e-12 | 31/47 (NCI-H1573, AsPC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.11×** | +7.5 | 2e-12 | 37/49 (NCI-H1573, COLO 205, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **2.08×** | +7.4 | 6e-12 | 40/48 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **2.06×** | +7.3 | 1e-11 | 39/48 (NCI-H460, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.45×** | +7.1 | 4e-11 | 32/48 (NCI-H1573, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **2.00×** | +7.0 | 9e-11 | 41/48 (A498, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.28×** | +6.6 | 9e-10 | 27/49 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.40×** | +6.5 | 3e-09 | 32/48 (SW480, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.50×** | +5.5 | 7e-07 | 31/48 (A498, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.72×** | +5.5 | 9e-07 | 31/48 (PANC-1, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **1.47×** | +5.3 | 2e-06 | 33/48 (NCI-H460, A498, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7323.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **0.749×** | -5.4 | 4e-05 | 30/47 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.793×** | -4.5 | 0.002 | 23/47 (hTERT-HPNE, PANC-1, …) | two highest doses | low cells (technical?) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.852× | -4.3 | 0.003 | 18/48 (LoVo, MIA PaCa-2, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.833×** | -4.2 | 0.004 | 17/48 (LoVo, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.818×** | -4.1 | 0.004 | 18/49 (SW48, A-427, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.831×** | -4.1 | 0.004 | 21/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.810×** | -4.1 | 0.004 | 22/49 (LoVo, MIA PaCa-2, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.812×** | -4.0 | 0.004 | 23/47 (MIA PaCa-2, LoVo, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.808×** | -4.0 | 0.004 | 20/47 (MIA PaCa-2, LoVo, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.833×** | -3.7 | 0.010 | 20/50 (LoVo, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **0.720×** | -3.3 | 0.046 | 11/50 (A-427, AsPC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.833×** | -3.3 | 0.049 | 17/48 (LoVo, MIA PaCa-2, …) | all doses, flat |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.852× | -3.1 | 0.076 | 15/48 (HCT15, BT-474, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.891× | -3.1 | 0.076 | 13/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.46 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7323. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 69.4 | 11 (7 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.03× (z +18.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.81× (z +17.3) | — |
| [[NCI-H1573 (line)]] | alt | 46.4 | 10 (8 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +14.7) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.46× (z +13.9) | — |
| [[NCI-H1792 (line)]] | alt | 38.1 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.66× (z +12.1) | — |
| [[CFPAC-1 (line)]] | alt | 39.6 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.15× (z +14.5) | — |
| [[HT-29 (line)]] | alt | 33.3 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +12.6) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.10× (z +12.5) | — |
| [[NCI-H2347 (line)]] | alt | 49.6 | 6 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.62× (z +13.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.56× (z +13.5) | — |
| [[NCI-H460 (line)]] | wt | 67.6 | 6 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.89× (z +12.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.98× (z +10.3) | — |
| [[SW 900 (line)]] | alt | 32.5 | 6 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.64× (z +11.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 4.87× (z +10.4) | — |
| [[A549 (line)]] | wt | 57.4 | 5 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.78× (z +11.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.96× (z +9.6) | — |
| [[AsPC-1 (line)]] | alt | 45.2 | 5 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 5.42× (z +13.8) | — |
| [[Hs 766T (line)]] | wt | 39.6 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.00× (z +11.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 94.4 | 4 (3 ⚠) | 1 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.16× (z +10.9) ⚠ unreliable plate only · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.65× (z +9.2) | [[Adagrasib (drug)]] 0.05 µM 0.644× (z -14.8) ⚠ position not correctable |
| [[A498 (line)]] | wt | 57.6 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.70× (z +11.2) | — |
| [[LoVo (line)]] | wt | 56.8 | 3 (2 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 3.90× (z +13.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.61× (z +9.2) | [[Cobimetinib (drug)]] 5 µM 0.386× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 104 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.84× (z +11.6) | — |
| [[SNU-423 (line)]] | alt | 47.5 | 4 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.14× (z +12.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.91× (z +11.7) | — |
| [[A-172 (line)]] | wt | 42.0 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.23× (z +13.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.78× (z +12.5) | — |
| [[AN3 CA (line)]] | alt | 142 | 2 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.48× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -14.9) ⚠ cell-cycle shift, explains ~32% of this change |
| [[C32 (line)]] | wt | 35.0 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.37× (z +10.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.74× (z +9.6) | — |
| [[HEC-1-A (line)]] | alt | 57.9 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.16× (z +11.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.58× (z +9.7) | — |
| [[HepG2_C3A (line)]] | wt | 61.3 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 4.84× (z +12.5) | — |
| [[HOP62 (line)]] | alt | 28.8 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.14× (z +12.6) | — |
| [[HS-578T (line)]] | alt | 38.8 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.48× (z +12.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 4.44× (z +12.4) | — |
| [[LS 180 (line)]] | wt | 42.3 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.69× (z +12.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.75× (z +10.6) | — |
| [[Panc 03.27 (line)]] | alt | 48.9 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.47× (z +12.6) | — |
| [[RPMI-7951 (line)]] | alt | 68.6 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.09× (z +10.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.97× (z +9.6) | — |
| [[SHP-77 (line)]] | alt | 132 | 2 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.25× (z +10.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.01× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.361× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 123 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.322× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 24.6 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.40× (z +8.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 5.15× (z +8.6) | — |
| [[HCT15 (line)]] | alt | 56.4 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.92× (z +10.9) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[KATO III (line)]] | alt | 39.4 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.24× (z +10.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.75× (z +8.8) | — |
| [[SK-MEL-2 (line)]] | alt | 98.6 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.64× (z +9.9) | — |
| [[A-427 (line)]] | wt | 114 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.562× (z -10.2) ⚠ cell-cycle shift, explains ~32% of this change |
| [[BT-474 (line)]] | alt | 40.6 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.53× (z +9.6) | — |
| [[J82 (line)]] | alt | 47.8 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.49× (z +9.3) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[LOX-IMVI (line)]] | wt | 74.6 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.94× (z +11.4) | — |
| [[PANC-1 (line)]] | alt | 145 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.32× (z +10.5) ⚠ unreliable plate only | — |
| [[RKO (line)]] | wt | 125 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.515× (z -9.9) ⚠ cell-cycle shift, explains ~50% of this change |
| [[SNU-1 (line)]] | wt | 70.2 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.19× (z +8.9) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[SW1417 (line)]] | alt | 76.9 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.52× (z +10.6) ⚠ unreliable plate only | — |
| [[SW48 (line)]] | wt | 114 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.269× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[CHP-212 (line)]] | wt | 67.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 57.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 47.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 62.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 74.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 44.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7323), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LYAR]] | +0.86 | +0.83 / +0.85 | both halves | 7e-06 | STRING 429 |
| [[NOP16]] | +0.82 | +0.86 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[WDR3]] | +0.80 | +0.75 / +0.81 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 997 |
| [[POLR1B]] | +0.78 | +0.73 / +0.78 | both halves | 7e-06 | STRING 977 |
| [[PUS1]] | +0.77 | +0.79 / +0.81 | both halves | 7e-06 | STRING 469 |
| [[DDX31]] | +0.76 | +0.75 / +0.82 | both halves | 7e-06 | STRING 850 |
| [[WDR4]] | +0.76 | +0.80 / +0.78 | both halves | 7e-06 |  |
| [[DDX21]] | +0.76 | +0.77 / +0.74 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 544 |
| [[PUM3]] | +0.75 | +0.84 / +0.70 | both halves | 7e-06 | same gene group; STRING 956 |
| [[MDN1]] | +0.75 | +0.68 / +0.78 | both halves | 7e-06 | STRING 672 |
| [[NOL10]] | +0.74 | +0.72 / +0.66 | both halves | 7e-06 | STRING 997 |
| [[DKC1]] | +0.74 | +0.71 / +0.74 | both halves | 7e-06 | pathway: rRNA modification in the nucleus and cytosol; STRING 936 |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATOSA]] | -0.64 | -0.59 / -0.62 | both halves | 7e-06 |  |
| [[ITM2B]] | -0.61 | -0.57 / -0.60 | both halves | 9e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises PDCD11's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 1.4% of all compounds | 0.017 | ⚠ off-target possible; 3 compounds |
| [[MAP2K2]] | B | MAP2K2 activity raises PDCD11's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.716). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-13.8, -38.1); signed map (-3.1, -48.1). **Vector** length 109, 37.4% of its response variance represented; |z| ≥ 3 in 1,630 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.63 to 13); *ribosome biogenesis* (control, mean cos +0.58 to 6); *tRNA modification in the nucleus and cytosol* (reactome, mean cos +0.52 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +10.7 | +14.8 |
|  | [[EX229 (drug)]] 5 µM |  | +6.8 | +9.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +6.1 | +7.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +5.4 | +5.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | +4.9 | +7.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +4.7 | +7.0 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -4.3 | +6.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.9 | -4.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.7 | -5.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -3.5 | +9.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.5 | -3.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.4 | -4.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.3 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | programmed cell death 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.33 — chr10:103,396,626-103,446,294 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0185, ALG-4, RRP5, NFBP |
| Gene groups (HGNC) | Minor histocompatibility antigens; SSU processome |
| Reactome | 5 pathways, smallest: rRNA modification in the nucleus and cytosol; Major pathway of rRNA processing in the nucleolus and cytosol; rRNA processing in the nucleus and cytosol |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14690](https://www.uniprot.org/uniprotkb/Q14690) (Protein RRP5 homolog):

> Essential for the generation of mature 18S rRNA, specifically necessary for cleavages at sites A0, 1 and 2 of the 47S precursor. Directly interacts with U3 snoRNA.; Involved in the biogenesis of rRNA.

**Summary**, from NCBI Gene [22984](https://www.ncbi.nlm.nih.gov/gene/22984):

> PDCD11 is a NF-kappa-B (NFKB1; 164011)-binding protein that colocalizes with U3 RNA (MIM 180710) in the nucleolus and is required for rRNA maturation and generation of 18S rRNA (Sweet et al., 2003 [PubMed 14624448]; Sweet et al., 2008 [PubMed 17654514]).[supplied by OMIM, Oct 2008]

**Accessions** — [HGNC:13408](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13408) · Entrez [22984](https://www.ncbi.nlm.nih.gov/gene/22984) · UniProt [Q14690](https://www.uniprot.org/uniprotkb/Q14690) · Ensembl [ENSG00000148843](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148843)

## Data

Gene col 7323: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7323); `tables/drug_effects.parquet` (83 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7323, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7323]; `tensor/DDL_lfc|DDL_z.npy` [7323]; `embed/gene_vectors.npy` [7323]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7323 or target_col == 7323). Every well: [[PDCD11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDCD11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
