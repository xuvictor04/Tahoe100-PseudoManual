---
symbol: "KPNA2"
type: "gene"
col: 11290
ensembl_id: "ENSG00000182481"
name: "karyopherin subunit alpha 2"
location: "17q24.2"
module: 22
arm: "+"
pooled_cpm: 59.18
n_lines_expressing: 50
n_dd_up: 33
n_dd_down: 7
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# KPNA2

*karyopherin subunit alpha 2* — 17q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (22 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.59× (z +16.5, q 0e+00, up in 43 of 48 measured lines) ⚠ cell-cycle shift, explains ~67% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 8.42× (z +13.7, q 3e-40, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Selinexor (drug)]] 0.5 µM: 0.431× (z -10.4, q 2e-22, down in 43 of 48 measured lines) ⚠ cell-cycle shift, explains ~61% of this change. The strongest without an alert is [[Cytarabine (drug)]] 0.05 µM: 0.732× (z -3.6, q 0.032, down in 26 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 7 lines (A-427 0.287×, A498 0.330×, LS 180 0.225×, H4 0.193×, …; ⚠ cell-cycle shift, explains ~89% of this change); [[Selinexor (drug)]] 0.5 µM in 6 lines (A498 0.277×, A-427 0.289×, LoVo 0.315×, HT-29 0.262×, …; ⚠ cell-cycle shift, explains ~61% of this change); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (SW 1271 0.0649×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCNB1]] (+0.84, fdr 7e-06), [[KIF20A]] (+0.84, fdr 7e-06), [[BUB1]] (+0.84, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[PIMREG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 23 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 22 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11290.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **2.59×** | +16.5 | 0e+00 | 43/48 (A498, Panc 03.27, …) | rises with dose | composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **8.42×** | +13.7 | 3e-40 | 48/48 (PANC-1, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.19×** | +13.6 | 1e-39 | 42/48 (KATO III, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **2.84×** | +12.8 | 1e-35 | 47/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **2.54×** | +11.0 | 3e-26 | 42/48 (PANC-1, A498, …) | rises with dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **4.60×** | +9.8 | 1e-20 | 43/48 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **2.17×** | +9.5 | 1e-19 | 44/47 (KATO III, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **2.11×** | +9.2 | 4e-18 | 46/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.91×** | +7.9 | 1e-13 | 42/47 (KATO III, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~48% of this change | **1.90×** | +7.6 | 2e-12 | 37/47 (NCI-H460, COLO 205, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.70×** | +6.5 | 4e-09 | 33/48 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | **1.67×** | +5.8 | 2e-07 | 27/45 (PANC-1, HT-29, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.56×** | +5.5 | 2e-06 | 27/46 (PANC-1, SNU-423, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.56×** | +5.4 | 3e-06 | 28/47 (NCI-H460, H4, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.54×** | +5.3 | 4e-06 | 29/48 (HS-578T, PANC-1, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.53×** | +5.2 | 6e-06 | 29/48 (LS 180, SK-MEL-2, …) | two highest doses | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.35×** | +5.2 | 6e-06 | 25/48 (Hs 766T, HEC-1-A, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.39×** | +4.0 | 0.001 | 24/47 (NCI-H460, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.34×** | +3.6 | 0.007 | 21/47 (SHP-77, NCI-H460, …) | all doses, flat |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.35×** | +3.5 | 0.010 | 19/48 (HT-29, SK-MEL-2, …) | top dose only |  |
| [[LJI308 (drug)]] 0.05 µM |  | **1.34×** | +3.4 | 0.015 | 19/48 (SK-MEL-2, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **1.29×** | +3.0 | 0.052 | 15/47 (HT-29, LoVo, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.27×** | +3.0 | 0.052 | 11/47 (NCI-H23, NCI-H460, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.18× | +2.8 | 0.072 | 15/48 (CFPAC-1, HT-29, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11290.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 7 lines (A-427 0.287×, A498 0.330×, LS 180 0.225×, H4 0.193×, …; ⚠ cell-cycle shift, explains ~89% of this change); [[Selinexor (drug)]] 0.5 µM in 6 lines (A498 0.277×, A-427 0.289×, LoVo 0.315×, HT-29 0.262×, …; ⚠ cell-cycle shift, explains ~61% of this change); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (SW 1271 0.0649×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.431×** | -10.4 | 2e-22 | 43/48 (A498, A-427, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **0.613×** | -8.6 | 3e-15 | 35/48 (A-427, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.581×** | -6.7 | 4e-09 | 38/48 (HT-29, HOP62, …) | all doses, stronger at high dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.737×** | -3.8 | 0.021 | 21/47 (C32, A549, …) | inconsistent across doses |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.732×** | -3.7 | 0.022 | 24/48 (C32, NCI-H1573, …) | all doses, flat |  |
| [[Cytarabine (drug)]] 0.05 µM |  | **0.732×** | -3.6 | 0.032 | 26/48 (A-427, NCI-H2347, …) | all doses, flat |  |
| [[Rapamycin (drug)]] 5 µM |  | **0.826×** | -3.4 | 0.059 | 24/48 (HCT15, HT-29, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 0.776× | -3.1 | 0.11 | 16/48 (SNU-1, SK-MEL-2, …) | inconsistent across doses | position effect removed |
| [[18β-Glycyrrhetinic acid (drug)]] 5 µM |  | 0.839× | -3.1 | 0.11 | 20/48 (H4, NCI-H1792, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.832× | -3.1 | 0.11 | 13/48 (Hs 766T, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.784× | -3.0 | 0.13 | 15/47 (A498, SW48, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.84 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11290. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 36.9 | 11 (9 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.24× (z +14.3) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 12.7× (z +11.5) | — |
| [[NCI-H460 (line)]] | wt | 52.6 | 8 (7 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.30× (z +12.9) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +8.9) | — |
| [[KATO III (line)]] | alt | 32.6 | 7 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 9.09× (z +14.2) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.64× (z +14.0) | — |
| [[LoVo (line)]] | wt | 39.6 | 5 (3 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +11.8) ⚠ cell-cycle shift, explains ~67% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +9.9) | [[Selinexor (drug)]] 0.5 µM 0.315× (z -9.6) ⚠ cell-cycle shift, explains ~61% of this change |
| [[HOP62 (line)]] | alt | 73.3 | 3 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +13.6) ⚠ cell-cycle shift, explains ~67% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 11.6× (z +9.5) | [[Selinexor (drug)]] 5 µM 0.393× (z -9.9) ⚠ cell-cycle shift, explains ~89% of this change |
| [[A498 (line)]] | wt | 61.3 | 2 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +16.3) ⚠ cell-cycle shift, explains ~67% of this change | [[Selinexor (drug)]] 5 µM 0.330× (z -14.2) ⚠ cell-cycle shift, explains ~89% of this change |
| [[HEC-1-A (line)]] | alt | 68.6 | 4 (1 ⚠) | 0 | [[PH-797804 (drug)]] 5 µM 13.6× (z +11.8) | — |
| [[HT-29 (line)]] | alt | 65.9 | 3 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 21.0× (z +11.1) | [[Selinexor (drug)]] 0.5 µM 0.262× (z -9.4) ⚠ cell-cycle shift, explains ~61% of this change |
| [[A-427 (line)]] | wt | 143 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.87× (z +8.7) | [[Selinexor (drug)]] 5 µM 0.287× (z -14.2) ⚠ cell-cycle shift, explains ~89% of this change |
| [[A549 (line)]] | wt | 74.6 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.52× (z +14.7) ⚠ cell-cycle shift, explains ~67% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.35× (z +11.7) | — |
| [[AsPC-1 (line)]] | alt | 17.8 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.80× (z +12.5) ⚠ cell-cycle shift, explains ~67% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.07× (z +9.0) | — |
| [[hTERT-HPNE (line)]] | wt | 44.9 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.35× (z +12.9) ⚠ cell-cycle shift, explains ~67% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.39× (z +9.3) | — |
| [[NCI-H23 (line)]] | alt | 89.1 | 3 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 10.8× (z +9.5) | — |
| [[SW1417 (line)]] | alt | 71.0 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +11.7) ⚠ cell-cycle shift, explains ~67% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +9.2) | — |
| [[SW480 (line)]] | alt | 82.0 | 2 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 8.12× (z +9.3) | [[Selinexor (drug)]] 0.5 µM 0.337× (z -9.4) ⚠ cell-cycle shift, explains ~61% of this change |
| [[A-172 (line)]] | wt | 48.7 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 14.1× (z +9.6) | [[Selinexor (drug)]] 5 µM 0.408× (z -8.8) ⚠ cell-cycle shift, explains ~89% of this change |
| [[C32 (line)]] | wt | 48.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +11.8) ⚠ cell-cycle shift, explains ~67% of this change | [[Selinexor (drug)]] 0.5 µM 0.220× (z -9.3) ⚠ cell-cycle shift, explains ~61% of this change |
| [[CFPAC-1 (line)]] | alt | 33.9 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.92× (z +12.5) | — |
| [[HS-578T (line)]] | alt | 44.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.16× (z +12.9) ⚠ cell-cycle shift, explains ~67% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 15.2× (z +9.1) | — |
| [[J82 (line)]] | alt | 68.8 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.67× (z +10.5) | — |
| [[LOX-IMVI (line)]] | wt | 58.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +9.9) ⚠ cell-cycle shift, explains ~67% of this change | [[Selinexor (drug)]] 5 µM 0.367× (z -8.7) ⚠ cell-cycle shift, explains ~89% of this change |
| [[LS 180 (line)]] | wt | 35.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.95× (z +11.0) ⚠ cell-cycle shift, explains ~48% of this change | [[Selinexor (drug)]] 5 µM 0.225× (z -13.1) ⚠ cell-cycle shift, explains ~89% of this change |
| [[NCI-H1573 (line)]] | alt | 24.6 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 19.1× (z +8.7) | — |
| [[NCI-H1792 (line)]] | alt | 28.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.58× (z +15.8) ⚠ cell-cycle shift, explains ~67% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.15× (z +11.4) | — |
| [[NCI-H2030 (line)]] | alt | 83.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +10.8) ⚠ cell-cycle shift, explains ~67% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 10.1× (z +9.3) | — |
| [[Panc 03.27 (line)]] | alt | 48.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.62× (z +16.1) ⚠ cell-cycle shift, explains ~67% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.68× (z +12.2) | — |
| [[RKO (line)]] | wt | 64.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +10.6) ⚠ cell-cycle shift, explains ~67% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 14.7× (z +10.6) | — |
| [[SNU-423 (line)]] | alt | 41.5 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.59× (z +11.6) | — |
| [[SW 900 (line)]] | alt | 55.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +9.5) ⚠ cell-cycle shift, explains ~67% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 12.3× (z +8.8) | — |
| [[COLO 205 (line)]] | alt | 15.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.11× (z +8.9) ⚠ cell-cycle shift, explains ~67% of this change | — |
| [[H4 (line)]] | wt | 62.7 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.193× (z -10.2) ⚠ cell-cycle shift, explains ~89% of this change |
| [[HepG2_C3A (line)]] | wt | 44.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.54× (z +11.1) | — |
| [[Hs 766T (line)]] | wt | 22.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.52× (z +9.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 80.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.66× (z +10.6) | — |
| [[NCI-H2347 (line)]] | alt | 72.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +10.7) ⚠ cell-cycle shift, explains ~67% of this change | — |
| [[SNU-1 (line)]] | wt | 80.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.175× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW 1271 (line)]] | alt | 76.2 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0649× (z -9.2) |
| [[AN3 CA (line)]] | alt | 129 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 58.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 90.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 121 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 58.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 84.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 93.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 64.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11290), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCNB1]] | +0.84 | +0.82 / +0.86 | both halves | 7e-06 | STRING 840 |
| [[KIF20A]] | +0.84 | +0.83 / +0.86 | both halves | 7e-06 | STRING 660 |
| [[BUB1]] | +0.84 | +0.83 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 644 |
| [[CCNA2]] | +0.82 | +0.84 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 587 |
| [[TACC3]] | +0.82 | +0.77 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 473 |
| [[TROAP]] | +0.82 | +0.78 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[KIF23]] | +0.82 | +0.82 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 778 |
| [[FAM83D]] | +0.81 | +0.82 / +0.81 | both halves | 7e-06 |  |
| [[TPX2]] | +0.81 | +0.81 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 867 |
| [[BIRC5]] | +0.81 | +0.78 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 818 |
| [[KNSTRN]] | +0.81 | +0.79 / +0.79 | both halves | 7e-06 |  |
| [[ARHGAP11A]] | +0.80 | +0.82 / +0.82 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIMREG]] | B | PIMREG activity raises KPNA2's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 2.10× lower at baseline in the lines without PIMREG | 0.011 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[FAM72B]] | B | FAM72B activity raises KPNA2's level | lines that do not express FAM72B (6) vs lines expressing it (44) | 1.72× lower at baseline in the lines without FAM72B | 0.089 | ⚠ within organs, on part of the lines; also absent: LINC02798, SRGAP2C, ZNF512B; its own permutation p |
| [[PBK]] | C | PBK activity raises KPNA2's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.47× lower at baseline in the lines without PBK | 0.016 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises KPNA2's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.11× lower at baseline in the lines without AURKB | 0.023 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[CDC20]] | C | CDC20 activity raises KPNA2's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 2.10× lower at baseline in the lines without CDC20 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.822). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-38.0, -58.1); signed map (-52.1, -43.4). **Vector** length 111, 41.1% of its response variance represented; |z| ≥ 3 in 1,339 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DREAM G2/M down* (control, mean cos +0.76 to 28); *Mitotic Prometaphase* (reactome, mean cos +0.61 to 48); *Mitotic Metaphase and Anaphase* (reactome, mean cos +0.64 to 41).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.6 | +13.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +5.6 | +5.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | +5.1 | +4.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +4.9 | +5.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | +4.7 | +5.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.8 | +9.8 |
|  | [[Docetaxel (drug)]] 5 µM |  | +2.7 | +1.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +0.6 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.4 | +1.5 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.1 | +2.7 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | -8.8 | -8.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | -8.5 | -10.4 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~54% of this change | -4.8 | -6.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.1 | +1.8 |
|  | [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | -4.0 | -3.7 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -2.9 | -3.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.8 | -1.8 |
|  | [[Amsacrine (drug)]] 5 µM |  | -2.8 | -2.2 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | -2.7 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | karyopherin subunit alpha 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q24.2 — chr17:68,035,636-68,047,364 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SRP1alpha, IPOA1, QIP2, PTAC58; previously RCH1 |
| Gene groups (HGNC) | Armadillo repeat containing; Importins |
| Hallmark sets | G2M_CHECKPOINT, E2F_TARGETS, MYC_TARGETS_V1 |
| Reactome | 44 pathways, smallest: Sensing of DNA Double Strand Breaks; CREB1 phosphorylation through the activation of CaMKII/CaMKK/CaMKIV cascasde; CaMK IV-mediated phosphorylation of CREB |
| Matched by | ensembl_id |

**Function**, from UniProt [P52292](https://www.uniprot.org/uniprotkb/P52292) (Importin subunit alpha-1):

> Functions in nuclear protein import as an adapter protein for nuclear receptor KPNB1. Binds specifically and directly to substrates containing either a simple or bipartite NLS motif. Docking of the importin/substrate complex to the nuclear pore complex (NPC) is mediated by KPNB1 through binding to nucleoporin FxFG repeats and the complex is subsequently translocated through the pore by an energy requiring, Ran-dependent mechanism. At the nucleoplasmic side of the NPC, Ran binds to importin-beta …

**Summary**, from NCBI Gene [3838](https://www.ncbi.nlm.nih.gov/gene/3838):

> The import of proteins into the nucleus is a process that involves at least 2 steps. The first is an energy-independent docking of the protein to the nuclear envelope and the second is an energy-dependent translocation through the nuclear pore complex. Imported proteins require a nuclear localization sequence (NLS) which generally consists of a short region of basic amino acids or 2 such regions spaced about 10 amino acids apart. Proteins involved in the first step of nuclear import have been …

**Accessions** — [HGNC:6395](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6395) · Entrez [3838](https://www.ncbi.nlm.nih.gov/gene/3838) · UniProt [P52292](https://www.uniprot.org/uniprotkb/P52292) · Ensembl [ENSG00000182481](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182481)

## Data

Gene col 11290: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11290); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11290, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11290]; `tensor/DDL_lfc|DDL_z.npy` [11290]; `embed/gene_vectors.npy` [11290]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11290 or target_col == 11290). Every well: [[KPNA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KPNA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
