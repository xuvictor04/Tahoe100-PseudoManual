---
symbol: "COTL1"
type: "gene"
col: 2331
ensembl_id: "ENSG00000103187"
name: "coactosin like F-actin binding protein 1"
location: "16q24.1"
module: 78
arm: "+"
pooled_cpm: 97.84
n_lines_expressing: 45
n_dd_up: 39
n_dd_down: 14
n_dd_up_clean: 15
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 3
direction_downstream: 4
tags: ["gene", "module/078"]
generated_by: "tahoemap"
---

# COTL1

*coactosin like F-actin binding protein 1* — 16q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 39 drug-doses (24 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.50× (z +19.3, q 0e+00, up in 37 of 43 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.17× (z +11.5, q 8e-29, up in 34 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 0.645× (z -6.1, q 4e-07, down in 28 of 45 measured lines) ⚠ cell-cycle shift, explains ~42% of this change. The strongest without an alert is [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM: 0.657× (z -6.1, q 4e-07, down in 31 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACTN1]] (+0.72, fdr 7e-06), [[CSRP1]] (+0.68, fdr 1e-05), [[CORO1C]] (+0.63, fdr 2e-05); moves opposite to [[COA6]] (-0.60, fdr 3e-05), [[SNX13]] (-0.56, fdr 8e-05), [[PEX11A]] (-0.56, fdr 2e-05).
> It is in [[Module 078]], a single-armed module (apical junction).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 4 go from it, the strongest it → [[TLK2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 24 with an alert ⚠; shown: the 15 strongest and the 13 next strongest without an alert. 39 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 24 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2331.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.50×** | +19.3 | 0e+00 | 37/43 (A498, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **3.57×** | +18.9 | 0e+00 | 42/43 (HOP62, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **3.56×** | +18.9 | 0e+00 | 43/44 (SW480, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **3.37×** | +17.4 | 0e+00 | 34/36 (SW480, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **3.14×** | +17.1 | 0e+00 | 43/43 (HOP62, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **2.99×** | +16.3 | 0e+00 | 42/43 (HOP62, LOX-IMVI, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **2.68×** | +13.6 | 4e-40 | 38/39 (NCI-H1792, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.17×** | +11.5 | 8e-29 | 34/43 (C32, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.97×** | +9.7 | 2e-20 | 30/43 (A498, A-172, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.68×** | +7.7 | 9e-13 | 33/43 (LOX-IMVI, A-172, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.40×** | +7.0 | 1e-10 | 24/43 (A-172, NCI-H2347, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change | **1.59×** | +6.8 | 4e-10 | 28/43 (NCI-H460, SW480, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.55×** | +6.2 | 2e-08 | 30/45 (SNU-423, MIA PaCa-2, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +5.6 | 8e-07 | 25/43 (LOX-IMVI, SK-MEL-2, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.44×** | +5.5 | 2e-06 | 28/42 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.42×** | +5.2 | 8e-06 | 30/43 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.41×** | +5.1 | 1e-05 | 31/42 (NCI-H23, COLO 205, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.39×** | +4.9 | 2e-05 | 24/43 (C32, MIA PaCa-2, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.25×** | +4.7 | 8e-05 | 22/44 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.36×** | +4.4 | 2e-04 | 28/42 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.34×** | +4.2 | 5e-04 | 22/43 (A549, NCI-H23, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.68×** | +4.0 | 0.001 | 22/44 (A549, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.29×** | +3.8 | 0.003 | 21/43 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.61×** | +3.7 | 0.004 | 25/43 (RPMI-7951, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.39×** | +3.5 | 0.008 | 21/43 (NCI-H23, PANC-1, …) | rises with dose | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[vincristine (drug)]] 5 µM |  | **1.51×** | +3.2 | 0.021 | 14/41 (NCI-H23, NCI-H1573, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Flumatinib (mesylate) (drug)]] 0.5 µM |  | **1.21×** | +2.7 | 0.089 | 13/43 (NCI-H2030, A549, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **1.20×** | +2.7 | 0.095 | 13/43 (MIA PaCa-2, NCI-H1573, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2331.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.645×** | -6.1 | 4e-07 | 28/45 (SK-MEL-2, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.657×** | -6.1 | 4e-07 | 31/43 (HOP62, J82, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.676×** | -5.7 | 3e-06 | 29/42 (HOP62, LoVo, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.755×** | -5.0 | 6e-05 | 25/43 (HOP62, Hs 766T, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.718×** | -5.0 | 7e-05 | 28/42 (NCI-H2030, SK-MEL-2, …) | rises with dose | low cells (technical?) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.705×** | -4.9 | 9e-05 | 32/43 (HEC-1-A, LoVo, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.714×** | -4.9 | 9e-05 | 27/42 (HOP62, PANC-1, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.818×** | -4.2 | 0.002 | 23/43 (NCI-H23, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.771×** | -3.9 | 0.006 | 20/44 (HOP62, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.618×** | -3.8 | 0.009 | 21/45 (NCI-H23, HEC-1-A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.790×** | -3.6 | 0.019 | 17/44 (NCI-H23, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[RMC-6236 (drug)]] 5 µM |  | **0.649×** | -3.4 | 0.033 | 18/43 (NCI-H23, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.804×** | -3.3 | 0.043 | 21/42 (SK-MEL-2, RKO, …) | rises with dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.800×** | -3.2 | 0.058 | 14/43 (NCI-H23, SK-MEL-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.65 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2331. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 122 | 8 (7 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +17.7) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.50× (z +10.1) | [[Cobimetinib (drug)]] 5 µM 0.424× (z -9.1) |
| [[A-172 (line)]] | wt | 94.6 | 10 (9 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.60× (z +19.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.95× (z +14.2) | — |
| [[A498 (line)]] | wt | 284 | 9 (8 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +25.5) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.86× (z +14.8) | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.546× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 144 | 10 (8 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.41× (z +18.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.02× (z +15.4) | — |
| [[NCI-H1792 (line)]] | alt | 88.9 | 10 (9 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.73× (z +15.9) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.92× (z +8.8) | — |
| [[SNU-423 (line)]] | alt | 107 | 10 (10 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.82× (z +13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[J82 (line)]] | alt | 156 | 7 (7 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +14.6) ⚠ cell-cycle shift, explains ~31% of this change | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.493× (z -8.5) |
| [[NCI-H2030 (line)]] | alt | 191 | 8 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +11.7) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.54× (z +10.3) | — |
| [[SW 900 (line)]] | alt | 69.6 | 8 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +13.9) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.07× (z +11.3) | — |
| [[C32 (line)]] | wt | 95.8 | 7 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.24× (z +21.5) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 8.75× (z +16.7) | — |
| [[LOX-IMVI (line)]] | wt | 45.4 | 7 (7 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.09× (z +14.2) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[NCI-H23 (line)]] | alt | 61.9 | 6 (5 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 6.87× (z +14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.55× (z +9.8) | [[Trametinib (drug)]] 5 µM 0.317× (z -8.9) ⚠ cell-cycle shift, explains ~42% of this change |
| [[NCI-H460 (line)]] | wt | 24.5 | 7 (7 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 7.61× (z +13.5) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[RPMI-7951 (line)]] | alt | 70.6 | 7 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.31× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.40× (z +9.5) | — |
| [[A549 (line)]] | wt | 124 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.70× (z +17.2) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.06× (z +11.3) | — |
| [[CFPAC-1 (line)]] | alt | 121 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.29× (z +20.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.14× (z +9.8) | — |
| [[HS-578T (line)]] | alt | 127 | 6 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +12.9) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H1573 (line)]] | alt | 25.7 | 6 (5 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 7.94× (z +13.8) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.41× (z +9.9) | — |
| [[Panc 03.27 (line)]] | alt | 78.4 | 6 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +15.6) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 56.4 | 5 (5 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 5.29× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | [[Trametinib (drug)]] 5 µM 0.377× (z -9.0) ⚠ cell-cycle shift, explains ~42% of this change |
| [[SW1417 (line)]] | alt | 120 | 6 (6 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.20× (z +12.6) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[SW480 (line)]] | alt | 58.2 | 6 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.96× (z +17.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[H4 (line)]] | wt | 154 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.24× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[Hs 766T (line)]] | wt | 101 | 5 (5 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.66× (z +10.7) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 75.3 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.94× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[KATO III (line)]] | alt | 200 | 5 (5 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.25× (z +12.2) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[LS 180 (line)]] | wt | 37.6 | 5 (5 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.33× (z +12.1) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[AsPC-1 (line)]] | alt | 112 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.71× (z +23.2) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.93× (z +10.1) | — |
| [[PANC-1 (line)]] | alt | 158 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.28× (z +13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.17× (z +9.0) | — |
| [[RKO (line)]] | wt | 112 | 4 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.38× (z +13.1) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[HCT15 (line)]] | alt | 34.4 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 7.38× (z +10.8) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[LoVo (line)]] | wt | 33.6 | 2 (2 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 4.17× (z +10.5) ⚠ cell-cycle shift, explains ~36% of this change | [[Cobimetinib (drug)]] 5 µM 0.298× (z -8.5) |
| [[NCI-H2347 (line)]] | alt | 75.9 | 3 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.32× (z +9.9) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[HEC-1-A (line)]] | alt | 134 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +10.9) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.07× (z +8.7) | — |
| [[HepG2_C3A (line)]] | wt | 66.7 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.87× (z +8.8) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[C-33 A (line)]] | alt | 37.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.83× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[SW48 (line)]] | wt | 71.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.08× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[A-427 (line)]] | wt | 23.2 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 219 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.9 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 17.5 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 94.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 19.7 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 55.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 61.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 252 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.2 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 31.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 157 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 79.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2331), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACTN1]] | +0.72 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[CSRP1]] | +0.68 | +0.73 / +0.57 | both halves | 1e-05 |  |
| [[CORO1C]] | +0.63 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[MYH9]] | +0.61 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[TPM4]] | +0.60 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[EPB41L2]] | +0.59 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[MIR222HG]] | +0.59 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[MICAL2]] | +0.59 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[ITGA6]] | +0.58 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[VCL]] | +0.58 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[EGR3]] | +0.58 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[EGR1]] | +0.57 | +0.58 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COA6]] | -0.60 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[SNX13]] | -0.56 | -0.62 / -0.37 | both halves | 8e-05 |  |
| [[PEX11A]] | -0.56 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[ELMOD3]] | -0.56 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[YBEY]] | -0.56 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[ZNF148]] | -0.55 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[KEAP1]] | -0.54 | -0.39 / -0.53 | both halves | 6e-05 |  |
| [[ATG14]] | -0.53 | -0.64 / -0.48 | both halves | 2e-05 |  |
| [[LINC02256]] | -0.52 | -0.37 / -0.48 | both halves | 8e-05 |  |
| [[RWDD3]] | -0.52 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[RNPC3]] | -0.52 | -0.52 / -0.38 | both halves | 7e-05 |  |
| [[NCOA6]] | -0.52 | -0.52 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises COTL1's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.0% of all compounds | 0.029 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[FBXO6]] | B | FBXO6 activity raises COTL1's level | lines that do not express FBXO6 (7) vs lines expressing it (43) | 1.35× lower at baseline in the lines without FBXO6 | 0.060 | ⚠ within organs, on part of the lines; also absent: KDM7A-DT; maybe low, not absent; its own permutation p |
| [[MAP2K2]] | B | MAP2K2 activity raises COTL1's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TLK2]] | B | COTL1 activity raises TLK2's level | lines that do not express COTL1 (5) vs lines expressing it (45) | 1.09× lower at baseline in the lines without COTL1 | 0.050 | ⚠ within organs, on part of the lines; also absent: TIMP1, HOXA-AS2, ELK3; maybe low, not absent |
| [[SHB]] | B | COTL1 activity raises SHB's level | lines that do not express COTL1 (5) vs lines expressing it (45) | 1.75× lower at baseline in the lines without COTL1 | 0.063 | ⚠ within organs, on part of the lines; also absent: TIMP1, HOXA-AS2, ELK3; maybe low, not absent |
| [[COL13A1]] | B | COTL1 activity raises COL13A1's level | lines that do not express COTL1 (5) vs lines expressing it (45) | 2.47× lower at baseline in the lines without COTL1 | 0.078 | ⚠ within organs, on part of the lines; also absent: TIMP1, HOXA-AS2, ELK3; maybe low, not absent |
| [[CAPN2]] | B | COTL1 activity raises CAPN2's level | lines that do not express COTL1 (5) vs lines expressing it (45) | 1.91× lower at baseline in the lines without COTL1 | 0.089 | ⚠ within organs, on part of the lines; also absent: TIMP1, HOXA-AS2, ELK3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 078]] — apical junction; 58 genes; every member is in the + arm (projection on the module's main direction 0.681). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-16.8, 25.5); signed map (-7.2, 35.2). **Vector** length 98.1, 31.1% of its response variance represented; |z| ≥ 3 in 1,496 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.8 | +5.6 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +4.1 | +3.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | +3.9 | +7.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +3.8 | +16.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.6 | +2.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.2 | +4.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.8 | +4.7 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.7 | +5.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.6 | +4.0 |
| fall | [[Trametinib (drug)]] 0.5 µM |  | -4.2 | -5.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.1 | -0.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.1 | -6.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.9 | -5.7 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -3.8 | -6.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.7 | -3.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.6 | +0.5 |

## What is on record

|  |  |
|---|---|
| Name | coactosin like F-actin binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q24.1 — chr16:84,565,596-84,618,078 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CLP |
| Gene groups (HGNC) | Coactosin like F-actin binding protein family |
| Reactome | 2 pathways, smallest: Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14019](https://www.uniprot.org/uniprotkb/Q14019) (Coactosin-like protein):

> Binds to F-actin in a calcium-independent manner. Has no direct effect on actin depolymerization. Acts as a chaperone for ALOX5 (5LO), influencing both its stability and activity in leukotrienes synthesis.

**Summary**, from NCBI Gene [23406](https://www.ncbi.nlm.nih.gov/gene/23406):

> This gene encodes one of the numerous actin-binding proteins which regulate the actin cytoskeleton. This protein binds F-actin, and also interacts with 5-lipoxygenase, which is the first committed enzyme in leukotriene biosynthesis. Although this gene has been reported to map to chromosome 17 in the Smith-Magenis syndrome region, the best alignments for this gene are to chromosome 16. The Smith-Magenis syndrome region is the site of two related pseudogenes. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:18304](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18304) · Entrez [23406](https://www.ncbi.nlm.nih.gov/gene/23406) · UniProt [Q14019](https://www.uniprot.org/uniprotkb/Q14019) · Ensembl [ENSG00000103187](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103187)

## Data

Gene col 2331: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2331); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2331, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2331]; `tensor/DDL_lfc|DDL_z.npy` [2331]; `embed/gene_vectors.npy` [2331]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2331 or target_col == 2331). Every well: [[COTL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COTL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
