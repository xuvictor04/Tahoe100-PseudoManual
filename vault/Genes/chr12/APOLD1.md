---
symbol: "APOLD1"
type: "gene"
col: 10967
ensembl_id: "ENSG00000178878"
name: "apolipoprotein L domain containing 1"
location: "12p13.1"
module: 23
arm: "+"
pooled_cpm: 114.73
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 10
n_dd_up_clean: 16
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# APOLD1

*apolipoprotein L domain containing 1* — 12p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.86× (z +23.3, q 0e+00, up in 40 of 48 measured lines) ⚠ cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 4.80× (z +21.4, q 0e+00, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.573× (z -14.8, q 0e+00, down in 41 of 48 measured lines) ⚠ cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[EX229 (drug)]] 5 µM: 0.724× (z -4.4, q 8e-04, down in 18 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NIFK-AS1]] (+0.69, fdr 1e-05), [[AHI1-DT]] (+0.69, fdr 8e-06), [[C21orf62-AS1]] (+0.67, fdr 7e-06); moves opposite to [[TEX2]] (-0.63, fdr 2e-05), [[GBA2]] (-0.59, fdr 1e-05), [[NAPG]] (-0.58, fdr 3e-05).
> It sits in the **+** arm of [[Module 023]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 15 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10967.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.86×** | +23.3 | 0e+00 | 40/48 (PANC-1, J82, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **4.80×** | +21.4 | 0e+00 | 47/49 (PANC-1, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.62×** | +12.9 | 2e-35 | 34/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.53×** | +10.8 | 4e-25 | 31/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +10.3 | 1e-22 | 27/49 (NCI-H1573, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.06×** | +9.9 | 5e-21 | 35/48 (LoVo, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +9.3 | 2e-18 | 29/48 (Hs 766T, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.36×** | +8.1 | 5e-14 | 29/48 (H4, HS-578T, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.34×** | +7.8 | 4e-13 | 24/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.32×** | +7.4 | 8e-12 | 25/48 (A498, PANC-1, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.70×** | +7.2 | 3e-11 | 31/47 (PANC-1, J82, …) | top dose only | noisy plate (z scaled) |
| [[Sulfatinib (drug)]] 5 µM |  | **1.31×** | +7.0 | 1e-10 | 24/49 (HOP62, KATO III, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.26×** | +6.0 | 6e-08 | 23/48 (HS-578T, HOP62, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.24×** | +5.8 | 3e-07 | 22/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.24×** | +5.6 | 1e-06 | 24/47 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +5.5 | 1e-06 | 25/50 (Hs 766T, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.47×** | +5.2 | 5e-06 | 24/50 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.23×** | +5.2 | 5e-06 | 21/48 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.17× | +5.2 | 7e-06 | 22/48 (MIA PaCa-2, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | 1.18× | +5.0 | 2e-05 | 18/49 (MIA PaCa-2, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.21×** | +4.5 | 2e-04 | 21/49 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10967.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.573×** | -14.8 | 0e+00 | 41/48 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.603×** | -13.4 | 2e-38 | 42/48 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.659×** | -11.1 | 3e-26 | 33/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.657×** | -10.7 | 1e-24 | 32/43 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.805×** | -5.8 | 9e-07 | 27/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~93% of this change | **0.827×** | -4.5 | 8e-04 | 21/48 (SW480, MIA PaCa-2, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.724×** | -4.4 | 8e-04 | 18/48 (MIA PaCa-2, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.750×** | -3.9 | 0.006 | 15/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | 0.870× | -3.7 | 0.013 | 18/48 (PANC-1, SW1417, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | 0.857× | -3.6 | 0.017 | 20/49 (SW480, RPMI-7951, …) | rises with dose | composition shift |
| [[Dexamethasone (drug)]] 5 µM |  | 0.875× | -3.6 | 0.019 | 7/48 (NCI-H1573, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.884× | -3.3 | 0.049 | 11/48 (NCI-H1573, A549, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.788×** | -3.2 | 0.049 | 11/49 (PANC-1, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.790×** | -3.2 | 0.049 | 13/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~77% of this change | 0.880× | -3.2 | 0.049 | 18/48 (HOP62, HEC-1-A, …) | inconsistent across doses |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 0.887× | -3.2 | 0.050 | 6/48 (NCI-H2030, NCI-H2347, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.887× | -3.2 | 0.050 | 6/48 (NCI-H1573, PANC-1, …) | top dose only |  |
| [[Cytarabine (drug)]] 0.05 µM |  | 0.884× | -3.0 | 0.075 | 9/48 (NCI-H1573, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.38 per unit of S-phase module lfc, +0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10967. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 265 | 9 (2 ⚠) | 2 (2 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.78× (z +22.6) ⚠ position not correctable · without an alert: [[Cobimetinib (drug)]] 5 µM 3.23× (z +12.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.403× (z -10.3) ⚠ unreliable plate only |
| [[PANC-1 (line)]] | alt | 96.9 | 6 (3 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +29.3) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 7.91× (z +16.8) | [[Panobinostat (drug)]] 5 µM 0.356× (z -16.4) ⚠ cell-cycle shift, explains ~35% of this change |
| [[LoVo (line)]] | wt | 136 | 7 (4 ⚠) | 2 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 4.39× (z +19.6) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 9.88× (z +16.3) | [[Dinaciclib (drug)]] 5 µM 0.318× (z -15.2) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 38.7 | 8 (6 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.96× (z +14.8) | — |
| [[A498 (line)]] | wt | 91.9 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +22.0) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.71× (z +9.8) | — |
| [[HOP62 (line)]] | alt | 227 | 2 (2 ⚠) | 3 (3 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.54× (z +14.5) ⚠ position not correctable | [[Ixazomib citrate (drug)]] 5 µM 0.382× (z -9.2) ⚠ cell-cycle shift, would explain all of this change |
| [[hTERT-HPNE (line)]] | wt | 283 | 1 (1 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +15.4) ⚠ cell-cycle shift, explains ~36% of this change | [[Panobinostat (drug)]] 5 µM 0.232× (z -12.9) ⚠ cell-cycle shift, explains ~35% of this change |
| [[KATO III (line)]] | alt | 77.9 | 5 (3 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 2.88× (z +11.7) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.62× (z +11.1) | — |
| [[NCI-H1792 (line)]] | alt | 127 | 5 (2 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 2.12× (z +11.5) | — |
| [[SW480 (line)]] | alt | 197 | 1 | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 3.91× (z +9.4) | [[Panobinostat (drug)]] 0.5 µM 0.330× (z -14.9) ⚠ cell-cycle shift, explains ~32% of this change |
| [[J82 (line)]] | alt | 80.9 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.11× (z +25.9) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 7.24× (z +10.3) | — |
| [[LS 180 (line)]] | wt | 90.5 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.68× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.288× (z -14.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 126 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.74× (z +15.4) | — |
| [[NCI-H23 (line)]] | alt | 135 | 4 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 11.2× (z +13.2) | — |
| [[A-427 (line)]] | wt | 83.6 | 3 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 9.62× (z +13.4) | — |
| [[COLO 205 (line)]] | alt | 43.7 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +10.0) | — |
| [[Hs 766T (line)]] | wt | 79.9 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.48× (z +14.3) | — |
| [[NCI-H2030 (line)]] | alt | 93.4 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +15.7) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 11.0× (z +12.2) | — |
| [[NCI-H2347 (line)]] | alt | 102 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +13.6) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.21× (z +9.5) | — |
| [[RPMI-7951 (line)]] | alt | 203 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.296× (z -11.8) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SK-MEL-2 (line)]] | alt | 179 | 0 | 3 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.337× (z -10.0) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SW48 (line)]] | wt | 101 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +15.5) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[A549 (line)]] | wt | 72.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +15.3) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 10.9× (z +11.4) | — |
| [[AsPC-1 (line)]] | alt | 50.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.62× (z +12.2) | — |
| [[BT-474 (line)]] | alt | 107 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +9.9) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.81× (z +8.7) | — |
| [[HCT15 (line)]] | alt | 222 | 0 | 2 (2 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.314× (z -9.1) ⚠ cell-cycle shift, explains ~35% of this change |
| [[HEC-1-A (line)]] | alt | 202 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.332× (z -10.3) ⚠ cell-cycle shift, explains ~32% of this change |
| [[HS-578T (line)]] | alt | 141 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +10.8) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[Panc 03.27 (line)]] | alt | 144 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.32× (z +10.1) | — |
| [[RKO (line)]] | wt | 59.9 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 10.1× (z +11.4) | — |
| [[SNU-1 (line)]] | wt | 65.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +12.0) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 12.8× (z +9.5) | — |
| [[AN3 CA (line)]] | alt | 77.5 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.117× (z -8.8) ⚠ toxic |
| [[C-33 A (line)]] | alt | 140 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +10.1) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[H4 (line)]] | wt | 129 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +10.1) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[HT-29 (line)]] | alt | 56.0 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.74× (z +9.5) | — |
| [[LOX-IMVI (line)]] | wt | 78.1 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.10× (z +9.6) | — |
| [[SW 900 (line)]] | alt | 149 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +13.1) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[SW1417 (line)]] | alt | 83.7 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.480× (z -8.7) ⚠ cell-cycle shift, explains ~32% of this change |
| [[A-172 (line)]] | wt | 66.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 85.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 68.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 135 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 43.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 90.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 77.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 172 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 193 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10967), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NIFK-AS1]] | +0.69 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[AHI1-DT]] | +0.69 | +0.65 / +0.58 | both halves | 8e-06 |  |
| [[C21orf62-AS1]] | +0.67 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[CDKN1B]] | +0.67 | +0.61 / +0.62 | both halves | 7e-06 | ⚠ same locus (3.5 kb, same strand: neighbours can correlate without regulation) |
| [[CFAP43]] | +0.64 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[DICER1-AS1]] | +0.63 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[KLRK1-AS1]] | +0.62 | +0.54 / +0.39 | both halves | 5e-05 |  |
| [[DNAI4]] | +0.61 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[PLS3-AS1]] | +0.60 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[ZBED5-AS1]] | +0.60 | +0.54 / +0.43 | both halves | 3e-05 |  |
| [[PRANCR]] | +0.59 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[CFAP418-AS1]] | +0.59 | +0.58 / +0.44 | both halves | 3e-05 |  |
| [[RSBN1]] | +0.59 | +0.59 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TEX2]] | -0.63 | -0.54 / -0.46 | both halves | 2e-05 |  |
| [[GBA2]] | -0.59 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[NAPG]] | -0.58 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[GNA12]] | -0.56 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[ACOT7]] | -0.56 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[ABCC10]] | -0.55 | -0.50 / -0.42 | both halves | 4e-05 | same gene group |
| [[LYPLA1]] | -0.55 | -0.58 / -0.40 | both halves | 5e-05 |  |
| [[USB1]] | -0.55 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[MPP3]] | -0.54 | -0.59 / -0.43 | both halves | 3e-05 |  |
| [[PPM1F]] | -0.54 | -0.50 / -0.39 | both halves | 6e-05 |  |
| [[ABTB3]] | -0.54 | -0.53 / -0.36 | both halves | 1e-04 |  |
| [[RGS19]] | -0.53 | -0.48 / -0.39 | both halves | 6e-05 | same gene group |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.601). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (4.6, 19.2); signed map (29.8, -8.6). **Vector** length 136, 41.1% of its response variance represented; |z| ≥ 3 in 1,557 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +8.0 | +21.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +6.9 | +8.1 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | +6.3 | +5.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +6.2 | +5.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +9.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +5.8 | +4.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +5.7 | +5.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +5.5 | +3.9 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -8.0 | -13.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -7.7 | -14.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.1 | -5.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -6.7 | -11.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -5.9 | -1.6 |
|  | [[EX229 (drug)]] 5 µM |  | -4.1 | -4.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.3 | -2.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.9 | -3.2 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -2.9 | -3.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.7 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | apolipoprotein L domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.1 — chr12:12,725,917-12,829,975 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ25138, DKFZP434F0318 |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96LR9](https://www.uniprot.org/uniprotkb/Q96LR9) (Apolipoprotein L domain-containing protein 1):

> Is a modulator of endothelial barrier permeability, required for proper organization of endothelial cell-cell junctions and cytoskeleton. It also plays a role in the modulation of secretory autophagy. May affect blood-brain barrier permeability.

**Summary**, from NCBI Gene [81575](https://www.ncbi.nlm.nih.gov/gene/81575):

> APOLD1 is an endothelial cell early response protein that may play a role in regulation of endothelial cell signaling and vascular function (Regard et al., 2004 [PubMed 15102925]).[supplied by OMIM, Dec 2008]

**Accessions** — [HGNC:25268](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25268) · Entrez [81575](https://www.ncbi.nlm.nih.gov/gene/81575) · UniProt [Q96LR9](https://www.uniprot.org/uniprotkb/Q96LR9) · Ensembl [ENSG00000178878](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178878)

## Data

Gene col 10967: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10967); `tables/drug_effects.parquet` (63 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10967, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10967]; `tensor/DDL_lfc|DDL_z.npy` [10967]; `embed/gene_vectors.npy` [10967]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10967 or target_col == 10967). Every well: [[APOLD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/APOLD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
