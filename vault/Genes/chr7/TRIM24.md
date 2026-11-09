---
symbol: "TRIM24"
type: "gene"
col: 4375
ensembl_id: "ENSG00000122779"
name: "tripartite motif containing 24"
location: "7q33-q34"
module: 4
arm: "-"
pooled_cpm: 101.67
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 7
n_dd_up_clean: 10
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# TRIM24

*tripartite motif containing 24* — 7q33-q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.19× (z +35.2, q 0e+00, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.526× (z -20.4, q 0e+00, down in 40 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.781× (z -7.9, q 5e-13, down in 26 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FOXA2]] (+0.57, fdr 1e-05), [[SHOC2]] (+0.55, fdr 2e-05), [[NBPF14]] (+0.54, fdr 2e-05); moves opposite to [[ZFP69]] (-0.49, fdr 1e-04), [[BCCIP]] (-0.49, fdr 4e-05), [[CWC27]] (-0.49, fdr 2e-05).
> It sits in the **-** arm of [[Module 004]] (MYC targets v1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4375.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.19×** | +35.2 | 0e+00 | 41/48 (C32, LoVo, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.54×** | +13.1 | 8e-37 | 38/48 (NCI-H460, C32, …) | top dose only | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.52×** | +12.4 | 8e-33 | 34/48 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.34×** | +9.2 | 3e-18 | 28/48 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.33×** | +8.9 | 5e-17 | 31/48 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +8.8 | 8e-17 | 31/48 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.30×** | +8.2 | 2e-14 | 25/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.27×** | +7.5 | 6e-12 | 27/48 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.44×** | +6.0 | 9e-08 | 28/48 (KATO III, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 1.14× | +6.0 | 1e-07 | 20/49 (NCI-H460, LoVo, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.21×** | +5.9 | 2e-07 | 21/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 1.13× | +5.3 | 6e-06 | 16/48 (RPMI-7951, SW1417, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 1.18× | +5.1 | 2e-05 | 19/50 (NCI-H460, LoVo, …) | inconsistent across doses |  |
| [[Cepharanthine (drug)]] 5 µM |  | 1.12× | +4.9 | 3e-05 | 6/48 (CFPAC-1, A549, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.16× | +4.7 | 1e-04 | 15/49 (HEC-1-A, RKO, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.26×** | +3.8 | 0.005 | 14/49 (NCI-H460, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.22×** | +3.2 | 0.032 | 8/49 (COLO 205, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.10× | +3.1 | 0.053 | 11/47 (SW480, NCI-H2030, …) | rises with dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4375.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.526×** | -20.4 | 0e+00 | 40/49 (A498, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.575×** | -16.3 | 0e+00 | 35/45 (A-172, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.658×** | -12.8 | 3e-35 | 32/43 (A498, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.781×** | -7.9 | 5e-13 | 26/48 (A-427, SW480, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 0.878× | -5.9 | 5e-07 | 16/48 (H4, A-427, …) | rises with dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.837× | -5.7 | 1e-06 | 20/48 (HOP62, LS 180, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.840× | -5.1 | 2e-05 | 21/47 (HOP62, COLO 205, …) | inconsistent across doses | low cells (technical?) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 0.853× | -5.1 | 3e-05 | 22/48 (KATO III, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.770×** | -4.4 | 8e-04 | 16/38 (HS-578T, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.963× | -4.2 | 0.001 | 1/50 (SW 1088) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.839× | -4.0 | 0.003 | 14/48 (SW 1271, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.810×** | -3.5 | 0.021 | 17/49 (CFPAC-1, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 5 µM |  | **0.816×** | -3.4 | 0.031 | 12/46 (SW 900, LS 180, …) | rises with dose | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | 0.867× | -3.2 | 0.048 | 16/48 (SNU-423, SW480, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.898× | -3.2 | 0.051 | 12/48 (SW 1271, MIA PaCa-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4375. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 60.4 | 13 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +29.8) | — |
| [[LoVo (line)]] | wt | 70.6 | 10 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +30.0) | — |
| [[C32 (line)]] | wt | 188 | 6 (2 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.00× (z +34.7) | [[Dinaciclib (drug)]] 0.5 µM 0.336× (z -14.9) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 275 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -16.7) |
| [[PANC-1 (line)]] | alt | 80.4 | 4 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +20.3) | [[Dinaciclib (drug)]] 5 µM 0.388× (z -16.1) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 238 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.236× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.429× (z -9.2) |
| [[SW480 (line)]] | alt | 141 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +20.8) | [[Dinaciclib (drug)]] 0.5 µM 0.390× (z -17.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 222 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +23.4) | [[Dinaciclib (drug)]] 0.5 µM 0.165× (z -26.9) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 98.0 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +14.8) | [[Dinaciclib (drug)]] 0.05 µM 0.371× (z -11.5) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 69.7 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 7.78× (z +25.2) | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.376× (z -8.6) |
| [[KATO III (line)]] | alt | 140 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +13.3) | [[Dinaciclib (drug)]] 0.5 µM 0.353× (z -14.8) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 52.4 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +16.8) | [[Dinaciclib (drug)]] 0.05 µM 0.418× (z -9.1) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 100 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +16.7) | — |
| [[SW 900 (line)]] | alt | 118 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.340× (z -11.3) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 222 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +16.2) | [[Dinaciclib (drug)]] 0.5 µM 0.226× (z -24.5) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 83.4 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.478× (z -9.7) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 56.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.159× (z -14.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 208 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.247× (z -17.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 58.7 | 2 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +12.3) ⚠ cell-cycle shift, explains ~13% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.65× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.433× (z -8.9) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 65.3 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +13.6) ⚠ cell-cycle shift, explains ~13% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.57× (z +13.0) | — |
| [[RPMI-7951 (line)]] | alt | 88.5 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +12.5) | [[Dinaciclib (drug)]] 0.05 µM 0.320× (z -11.9) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 85.4 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +12.4) | — |
| [[A-172 (line)]] | wt | 85.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.252× (z -17.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 57.5 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +13.2) | [[Auranofin (drug)]] 5 µM 0.373× (z -11.0) |
| [[BT-474 (line)]] | alt | 104 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +12.9) | — |
| [[CFPAC-1 (line)]] | alt | 73.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +14.7) | [[Dinaciclib (drug)]] 5 µM 0.470× (z -9.3) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 218 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -11.2) |
| [[COLO 205 (line)]] | alt | 101 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.269× (z -12.3) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 101 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.288× (z -11.0) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 86.0 | 0 | 2 (2 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0663× (z -12.2) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 79.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +18.2) | — |
| [[HOP62 (line)]] | alt | 69.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +17.8) | [[Dinaciclib (drug)]] 0.05 µM 0.361× (z -13.1) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 70.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +19.4) | — |
| [[NCI-H2030 (line)]] | alt | 57.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +14.6) | — |
| [[NCI-H2347 (line)]] | alt | 65.7 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.66× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.483× (z -8.6) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 208 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.372× (z -15.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 75.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.453× (z -9.1) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 190 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.188× (z -14.7) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 74.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.435× (z -8.5) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 59.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +11.3) | — |
| [[HT-29 (line)]] | alt | 95.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +13.7) | — |
| [[J82 (line)]] | alt | 80.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +17.1) | — |
| [[NCI-H1573 (line)]] | alt | 32.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +13.7) | — |
| [[Panc 03.27 (line)]] | alt | 64.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +19.0) | — |
| [[SK-MEL-2 (line)]] | alt | 125 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.206× (z -20.1) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 109 | 0 | 1 | — | [[Fluvoxamine (drug)]] 5 µM 0.0946× (z -9.1) |
| [[NCI-H2122 (line)]] | alt | 93.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 96.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 75.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4375), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*47 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FOXA2]] | +0.57 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[SHOC2]] | +0.55 | +0.48 / +0.57 | both halves | 2e-05 | pathway: Oncogenic MAPK signaling |
| [[NBPF14]] | +0.54 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[NBPF10]] | +0.53 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[ZNF503]] | +0.52 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[NBPF19]] | +0.51 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[TNRC6C]] | +0.49 | +0.38 / +0.62 | both halves | 6e-05 |  |
| [[TESK2]] | +0.48 | +0.50 / +0.43 | both halves | 3e-05 |  |
| [[STK17B]] | +0.48 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[PPP1R13B]] | +0.47 | +0.35 / +0.58 | both halves | 1e-04 |  |
| [[TMEM60]] | +0.46 | +0.44 / +0.45 | both halves | 3e-05 |  |
| [[IRX5]] | +0.46 | +0.47 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*53 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFP69]] | -0.49 | -0.48 / -0.35 | both halves | 1e-04 |  |
| [[BCCIP]] | -0.49 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[CWC27]] | -0.49 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[ZNF512]] | -0.48 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[COPS7B]] | -0.47 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[RAD23B]] | -0.46 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[ZNF875]] | -0.46 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[TTC14]] | -0.45 | -0.43 / -0.36 | both halves | 1e-04 |  |
| [[ZNF891]] | -0.45 | -0.36 / -0.41 | both halves | 1e-04 |  |
| [[WASH9P]] | -0.45 | -0.39 / -0.44 | both halves | 5e-05 |  |
| [[PSMB7]] | -0.45 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[SUMO1]] | -0.44 | -0.36 / -0.44 | both halves | 9e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **-** arm (projection on the module's main direction -0.402). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (10.0, -46.1); signed map (-5.5, 9.1). **Vector** length 101, 25.4% of its response variance represented; |z| ≥ 3 in 1,216 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.7 | +35.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.4 | +13.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | +4.8 | +5.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +4.6 | +6.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +8.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.2 | +4.7 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.7 | +0.5 |
|  | [[Adagrasib (drug)]] 5 µM |  | +2.1 | +0.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +5.3 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.7 | -16.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.2 | -7.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | -5.1 | -5.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.1 | -12.8 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -4.1 | -4.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.6 | -1.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.3 | -5.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.7 | -0.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.2 | -5.1 |

## What is on record

|  |  |
|---|---|
| Name | tripartite motif containing 24 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q33-q34 — chr7:138,460,259-138,589,996 (+) |
| Ensembl biotype | protein_coding |
| Also known as | hTIF1, Tif1a, RNF82, TIF1A; previously TIF1 |
| Gene groups (HGNC) | Ring finger proteins; Tripartite motif family; PHD finger proteins; Bromodomain containing; RING finger E3 ubiquitin protein ligases |
| Reactome | 7 pathways, smallest: Signaling by cytosolic FGFR1 fusion mutants; FGFR1 mutant receptor activation; Signaling by FGFR1 in disease |
| Matched by | ensembl_id |

**Function**, from UniProt [O15164](https://www.uniprot.org/uniprotkb/O15164) (Transcription intermediary factor 1-alpha):

> Transcriptional coactivator that interacts with numerous nuclear receptors and coactivators and modulates the transcription of target genes. Interacts with chromatin depending on histone H3 modifications, having the highest affinity for histone H3 that is both unmodified at 'Lys-4' (H3K4me0) and acetylated at 'Lys-23' (H3K23ac). Has E3 protein-ubiquitin ligase activity. During the DNA damage response, participates in an autoregulatory feedback loop with TP53. Early in response to DNA damage, …

**Summary**, from NCBI Gene [8805](https://www.ncbi.nlm.nih.gov/gene/8805):

> The protein encoded by this gene mediates transcriptional control by interaction with the activation function 2 (AF2) region of several nuclear receptors, including the estrogen, retinoic acid, and vitamin D3 receptors. The protein localizes to nuclear bodies and is thought to associate with chromatin and heterochromatin-associated factors. The protein is a member of the tripartite motif (TRIM) family. The TRIM motif includes three zinc-binding domains - a RING, a B-box type 1 and a B-box type …

**Accessions** — [HGNC:11812](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11812) · Entrez [8805](https://www.ncbi.nlm.nih.gov/gene/8805) · UniProt [O15164](https://www.uniprot.org/uniprotkb/O15164) · Ensembl [ENSG00000122779](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122779)

## Data

Gene col 4375: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4375); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4375, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4375]; `tensor/DDL_lfc|DDL_z.npy` [4375]; `embed/gene_vectors.npy` [4375]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4375 or target_col == 4375). Every well: [[TRIM24 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRIM24.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
