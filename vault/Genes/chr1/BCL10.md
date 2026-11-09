---
symbol: "BCL10"
type: "gene"
col: 6660
ensembl_id: "ENSG00000142867"
name: "BCL10 immune signaling adaptor"
location: "1p22.3"
module: 158
arm: "+"
pooled_cpm: 57.61
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 16
n_dd_up_clean: 11
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/158"]
generated_by: "tahoemap"
---

# BCL10

*BCL10 immune signaling adaptor* — 1p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.21× (z +20.9, q 0e+00, up in 42 of 47 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.65× (z +18.2, q 0e+00, up in 46 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 0.558× (z -10.4, q 1e-22, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDKN2AIP]] (+0.67, fdr 7e-06), [[CD163L1]] (+0.66, fdr 7e-06), [[IER2]] (+0.66, fdr 7e-06); moves opposite to [[NDC1]] (-0.65, fdr 7e-06), [[WHAMMP1]] (-0.64, fdr 1e-05), [[ATL2]] (-0.62, fdr 1e-05).
> It is in [[Module 158]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6660.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.21×** | +20.9 | 0e+00 | 42/47 (MIA PaCa-2, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.65×** | +18.2 | 0e+00 | 46/47 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.25×** | +14.6 | 0e+00 | 45/48 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.01×** | +13.0 | 1e-36 | 43/48 (NCI-H460, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.98×** | +10.7 | 2e-24 | 39/49 (MIA PaCa-2, NCI-H460, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.65×** | +9.3 | 9e-19 | 37/48 (A-172, MIA PaCa-2, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.45×** | +6.4 | 1e-08 | 23/40 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.40×** | +6.3 | 2e-08 | 31/48 (NCI-H460, SW48, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.35×** | +5.1 | 2e-05 | 28/47 (NCI-H460, RKO, …) | all doses, stronger at high dose | low cells (technical?) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.61×** | +4.6 | 2e-04 | 24/48 (NCI-H460, SW48, …) | rises with dose | noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.6 | 2e-04 | 20/48 (KATO III, Hs 766T, …) | rises with dose |  |
| [[Artesunate (drug)]] 0.5 µM |  | **1.24×** | +4.0 | 0.002 | 16/48 (Hs 766T, KATO III, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.29×** | +3.5 | 0.024 | 12/48 (LoVo, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.40×** | +3.3 | 0.045 | 18/47 (LOX-IMVI, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 1.19× | +3.2 | 0.058 | 5/48 (NCI-H1573, AsPC-1, …) | top dose only | plate-row cell shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6660.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.558×** | -10.4 | 1e-22 | 41/48 (RPMI-7951, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.686×** | -9.8 | 2e-20 | 32/47 (RKO, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.660×** | -7.4 | 3e-11 | 34/49 (RKO, Hs 766T, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.771×** | -6.6 | 8e-09 | 29/48 (NCI-H23, PANC-1, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.694×** | -6.5 | 9e-09 | 27/36 (HT-29, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.919× | -5.7 | 1e-06 | 6/49 (MIA PaCa-2, NCI-H2030, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.760×** | -5.1 | 3e-05 | 22/48 (RKO, AsPC-1, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.828×** | -4.9 | 6e-05 | 25/48 (Hs 766T, SW1417, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.759×** | -4.9 | 6e-05 | 22/47 (Hs 766T, PANC-1, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.769×** | -4.8 | 7e-05 | 24/47 (PANC-1, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.769×** | -4.7 | 2e-04 | 26/49 (Hs 766T, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.828×** | -4.5 | 3e-04 | 22/48 (C32, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.777×** | -4.3 | 8e-04 | 20/48 (PANC-1, Hs 766T, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.855× | -3.9 | 0.005 | 15/48 (MIA PaCa-2, Hs 766T, …) | all doses, flat |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.749×** | -3.8 | 0.005 | 20/46 (NCI-H661, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | 0.834× | -3.6 | 0.011 | 18/48 (MIA PaCa-2, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Afatinib (drug)]] 5 µM |  | **0.801×** | -3.5 | 0.013 | 19/49 (PANC-1, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.867× | -3.5 | 0.014 | 17/48 (NCI-H2347, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6660. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 34.2 | 7 (5 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 4.62× (z +10.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.96× (z +9.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 94.5 | 6 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.89× (z +18.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.73× (z +15.0) | [[Adagrasib (drug)]] 0.05 µM 0.585× (z -17.9) ⚠ position not correctable |
| [[NCI-H460 (line)]] | wt | 32.9 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +15.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.72× (z +14.0) | — |
| [[Hs 766T (line)]] | wt | 194 | 2 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +13.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.63× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.420× (z -13.0) |
| [[A549 (line)]] | wt | 37.1 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +15.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.85× (z +12.2) | — |
| [[HOP62 (line)]] | alt | 29.4 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.12× (z +16.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.82× (z +12.5) | — |
| [[HS-578T (line)]] | alt | 48.3 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +17.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.01× (z +13.6) | — |
| [[LOX-IMVI (line)]] | wt | 42.6 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +13.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.46× (z +11.3) | — |
| [[LS 180 (line)]] | wt | 72.2 | 2 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +13.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.77× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.425× (z -10.5) |
| [[RKO (line)]] | wt | 149 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.57× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.162× (z -23.0) |
| [[SW 900 (line)]] | alt | 41.6 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +13.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.80× (z +11.5) | — |
| [[A-172 (line)]] | wt | 27.9 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +13.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.37× (z +11.3) | — |
| [[A498 (line)]] | wt | 54.2 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +12.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.79× (z +11.4) | — |
| [[AsPC-1 (line)]] | alt | 147 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +15.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.59× (z +9.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -11.1) |
| [[CFPAC-1 (line)]] | alt | 94.3 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +15.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.25× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.393× (z -14.3) |
| [[HEC-1-A (line)]] | alt | 43.1 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.333× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.504× (z -9.8) |
| [[HT-29 (line)]] | alt | 66.6 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +9.5) ⚠ cell-cycle shift, explains ~29% of this change | [[Dinaciclib (drug)]] 5 µM 0.173× (z -17.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.498× (z -10.2) |
| [[hTERT-HPNE (line)]] | wt | 36.5 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +9.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.60× (z +9.0) | — |
| [[LoVo (line)]] | wt | 59.3 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +13.0) ⚠ cell-cycle shift, explains ~29% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.502× (z -10.9) |
| [[PANC-1 (line)]] | alt | 112 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +12.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.79× (z +10.4) | — |
| [[RPMI-7951 (line)]] | alt | 47.0 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +14.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.39× (z +11.7) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.216× (z -11.6) |
| [[SK-MEL-2 (line)]] | alt | 31.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.33× (z +15.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 5.40× (z +11.8) | — |
| [[SNU-423 (line)]] | alt | 40.9 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.94× (z +16.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.02× (z +8.8) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -8.7) |
| [[SW480 (line)]] | alt | 28.2 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +11.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.44× (z +8.7) | — |
| [[C32 (line)]] | wt | 33.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +15.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.26× (z +11.1) | — |
| [[Panc 03.27 (line)]] | alt | 75.3 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.384× (z -8.8) |
| [[SNU-1 (line)]] | wt | 27.6 | 2 | 0 | [[Harringtonine (drug)]] 0.5 µM 5.85× (z +8.7) | — |
| [[SW1417 (line)]] | alt | 60.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +11.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.26× (z +8.5) | — |
| [[COLO 205 (line)]] | alt | 45.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -10.5) |
| [[H4 (line)]] | wt | 36.0 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.205× (z -9.4) |
| [[J82 (line)]] | alt | 45.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +9.5) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[KATO III (line)]] | alt | 42.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.251× (z -11.8) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 94.4 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.377× (z -9.2) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 38.9 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 3.27× (z +9.2) | — |
| [[NCI-H2030 (line)]] | alt | 40.7 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.08× (z +9.0) | — |
| [[NCI-H2347 (line)]] | alt | 57.0 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.33× (z +8.6) | — |
| [[A-427 (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 55.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 35.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 45.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6660), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDKN2AIP]] | +0.67 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[CD163L1]] | +0.66 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[IER2]] | +0.66 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[DNTTIP1]] | +0.63 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[SFR1]] | +0.62 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[GALE]] | +0.61 | +0.66 / +0.51 | both halves | 1e-05 |  |
| [[ZNF674]] | +0.61 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[TUT7]] | +0.61 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[ZNF669]] | +0.60 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[EGR1]] | +0.59 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[CTTNBP2NL]] | +0.59 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[BTG1]] | +0.59 | +0.59 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDC1]] | -0.65 | -0.63 / -0.66 | both halves | 7e-06 |  |
| [[WHAMMP1]] | -0.64 | -0.62 / -0.54 | both halves | 1e-05 |  |
| [[ATL2]] | -0.62 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[PAXBP1]] | -0.59 | -0.60 / -0.51 | both halves | 1e-05 |  |
| [[SNRPA1]] | -0.59 | -0.55 / -0.61 | both halves | 1e-05 |  |
| [[ABCB10]] | -0.59 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[SEC61A2]] | -0.58 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[GTF2I]] | -0.57 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[KDM1A]] | -0.57 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[MFSD14B]] | -0.57 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[RBBP4]] | -0.56 | -0.61 / -0.45 | both halves | 3e-05 |  |
| [[BMPR1A]] | -0.56 | -0.52 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises BCL10's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MAP2K1]] | B | MAP2K1 activity raises BCL10's level | compounds that target MAP2K1: 3 of 4 lower it (Cobimetinib, TAK-733, Trametinib) | 75% of the class's compounds vs 3.4% of all compounds | 0.067 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 158]]; 27 genes; every member is in the + arm (projection on the module's main direction 0.719). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (34.1, 3.0); signed map (6.7, 24.3). **Vector** length 129, 39.0% of its response variance represented; |z| ≥ 3 in 1,240 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +10.9 | +18.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +9.3 | +14.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +9.2 | +13.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +8.5 | +20.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.2 | +9.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.8 | +6.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +4.2 | +5.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.7 | +4.6 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | +2.5 | +2.0 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -7.6 | -10.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.8 | -7.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.4 | -5.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.7 | -1.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.4 | -9.8 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.4 | -3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.4 | -4.3 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -3.3 | -6.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.3 | -3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.1 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | BCL10 immune signaling adaptor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p22.3 — chr1:85,265,776-85,276,632 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CARMEN, CIPER, mE10, c-E10, CLAP |
| Gene groups (HGNC) | Caspase recruitment domain containing; CBM complex |
| Hallmark sets | PEROXISOME, ALLOGRAFT_REJECTION, APOPTOSIS |
| Reactome | 13 pathways, smallest: E3 ubiquitin ligases ubiquitinate target proteins; Activation of NF-kappaB in B cells; FCERI mediated NF-kB activation |
| Matched by | ensembl_id |

**Function**, from UniProt [O95999](https://www.uniprot.org/uniprotkb/O95999) (B-cell lymphoma/leukemia 10):

> Plays a key role in both adaptive and innate immune signaling by bridging CARD domain-containing proteins to immune activation. Acts by channeling adaptive and innate immune signaling downstream of CARD domain-containing proteins CARD9, CARD11 and CARD14 to activate NF-kappa-B and MAP kinase p38 (MAPK11, MAPK12, MAPK13 and/or MAPK14) pathways which stimulate expression of genes encoding pro-inflammatory cytokines and chemokines. Recruited by activated CARD domain-containing proteins: …

**Summary**, from NCBI Gene [8915](https://www.ncbi.nlm.nih.gov/gene/8915):

> This gene was identified by its translocation in a case of mucosa-associated lymphoid tissue (MALT) lymphoma. The protein encoded by this gene contains a caspase recruitment domain (CARD), and has been shown to induce apoptosis and to activate NF-kappaB. This protein is reported to interact with other CARD domain containing proteins including CARD9, 10, 11 and 14, which are thought to function as upstream regulators in NF-kappaB signaling. This protein is found to form a complex with MALT1, a …

**Accessions** — [HGNC:989](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:989) · Entrez [8915](https://www.ncbi.nlm.nih.gov/gene/8915) · UniProt [O95999](https://www.uniprot.org/uniprotkb/O95999) · Ensembl [ENSG00000142867](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142867)

## Data

Gene col 6660: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6660); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6660, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6660]; `tensor/DDL_lfc|DDL_z.npy` [6660]; `embed/gene_vectors.npy` [6660]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6660 or target_col == 6660). Every well: [[BCL10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BCL10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
