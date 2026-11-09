---
symbol: "KDM3B"
type: "gene"
col: 4216
ensembl_id: "ENSG00000120733"
name: "lysine demethylase 3B"
location: "5q31.2"
module: 95
arm: "+"
pooled_cpm: 135.39
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 14
n_dd_up_clean: 8
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/095"]
generated_by: "tahoemap"
---

# KDM3B

*lysine demethylase 3B* — 5q31.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.68× (z +21.1, q 0e+00, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.452× (z -22.7, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (86 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 14 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BRD1]] (+0.70, fdr 1e-05), [[BAZ2B]] (+0.67, fdr 3e-05), [[INO80D]] (+0.66, fdr 3e-05); moves opposite to [[ST6GALNAC4]] (-0.60, fdr 5e-04), [[PCMT1]] (-0.57, fdr 2e-04), [[RSU1]] (-0.57, fdr 1e-04).
> It sits in the **+** arm of [[Module 095]] (Chromatin organization).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4216.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.68×** | +21.1 | 0e+00 | 43/48 (LOX-IMVI, LoVo, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.40×** | +9.7 | 6e-20 | 34/48 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.30×** | +7.5 | 2e-11 | 28/48 (LoVo, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.78×** | +6.1 | 1e-07 | 34/48 (LS 180, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.21×** | +5.5 | 5e-06 | 24/48 (LoVo, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.20×** | +5.4 | 8e-06 | 23/48 (LoVo, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +4.3 | 0.002 | 19/48 (A-427, A549, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.09× | +3.7 | 0.015 | 18/49 (HS-578T, HOP62, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.21×** | +3.6 | 0.020 | 17/47 (HEC-1-A, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.38×** | +3.4 | 0.037 | 17/49 (LS 180, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.36×** | +3.2 | 0.060 | 12/49 (HEC-1-A, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 13 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4216.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.452×** | -22.7 | 0e+00 | 47/48 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.459×** | -22.3 | 0e+00 | 48/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.507×** | -19.4 | 0e+00 | 48/48 (SW480, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.676×** | -11.2 | 7e-27 | 45/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.698×** | -9.5 | 2e-19 | 36/45 (NCI-H460, AN3 CA, …) | all doses, flat | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.715×** | -9.2 | 3e-18 | 32/50 (NCI-H460, LS 180, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | **0.740×** | -8.6 | 6e-16 | 32/49 (NCI-H460, AN3 CA, …) | all doses, flat | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.808×** | -8.6 | 6e-16 | 34/48 (LOX-IMVI, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | **0.743×** | -8.2 | 2e-14 | 29/44 (NCI-H23, NCI-H460, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.757×** | -8.0 | 1e-13 | 36/48 (HS-578T, NCI-H460, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.765×** | -7.4 | 9e-12 | 32/48 (NCI-H460, NCI-H23, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.777×** | -7.2 | 3e-11 | 32/48 (A-172, SW480, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.604×** | -5.3 | 4e-06 | 34/49 (HOP62, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 0.834× | -5.2 | 9e-06 | 22/48 (SK-MEL-2, SW480, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | 0.836× | -4.9 | 3e-05 | 22/47 (SK-MEL-2, NCI-H1573, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.919× | -3.4 | 0.021 | 7/48 (BT-474, AN3 CA, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.743×** | -3.1 | 0.049 | 15/49 (A498, H4, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4216. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 147 | 2 (1 ⚠) | 9 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +27.2) | [[Panobinostat (drug)]] 5 µM 0.375× (z -19.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.437× (z -16.2) |
| [[A-427 (line)]] | wt | 141 | 1 (1 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 1.89× (z +9.8) ⚠ cell-cycle shift, explains ~61% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.429× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.518× (z -10.1) |
| [[LS 180 (line)]] | wt | 128 | 0 | 6 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.375× (z -16.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.406× (z -14.7) |
| [[SW480 (line)]] | alt | 148 | 2 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +17.5) | [[Panobinostat (drug)]] 5 µM 0.360× (z -18.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.372× (z -18.2) |
| [[A549 (line)]] | wt | 153 | 1 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +12.9) | [[Panobinostat (drug)]] 0.5 µM 0.358× (z -16.6) |
| [[COLO 205 (line)]] | alt | 165 | 1 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +13.6) | [[Dinaciclib (drug)]] 0.5 µM 0.322× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.351× (z -11.4) |
| [[HEC-1-A (line)]] | alt | 251 | 1 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.60× (z +11.2) | [[Panobinostat (drug)]] 5 µM 0.481× (z -12.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.499× (z -11.7) |
| [[HOP62 (line)]] | alt | 110 | 2 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.79× (z +26.3) | [[Panobinostat (drug)]] 0.5 µM 0.392× (z -13.1) |
| [[LoVo (line)]] | wt | 204 | 2 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +28.4) | [[Panobinostat (drug)]] 5 µM 0.380× (z -16.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.415× (z -15.1) |
| [[LOX-IMVI (line)]] | wt | 124 | 1 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.22× (z +29.3) | [[Dinaciclib (drug)]] 0.05 µM 0.392× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.472× (z -10.9) |
| [[NCI-H23 (line)]] | alt | 129 | 1 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +18.3) | [[Dinaciclib (drug)]] 5 µM 0.313× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change |
| [[SK-MEL-2 (line)]] | alt | 168 | 1 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +24.3) | [[Panobinostat (drug)]] 5 µM 0.479× (z -10.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.492× (z -10.0) |
| [[SW1417 (line)]] | alt | 203 | 1 | 4 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.66× (z +8.6) | [[Panobinostat (drug)]] 5 µM 0.402× (z -15.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.405× (z -15.4) |
| [[A498 (line)]] | wt | 101 | 2 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +22.5) | [[Panobinostat (drug)]] 5 µM 0.482× (z -11.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.485× (z -11.7) |
| [[BT-474 (line)]] | alt | 132 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.223× (z -20.5) |
| [[C-33 A (line)]] | alt | 150 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.408× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.448× (z -9.5) |
| [[CFPAC-1 (line)]] | alt | 107 | 1 (1 ⚠) | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.60× (z +9.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.461× (z -10.8) |
| [[HepG2_C3A (line)]] | wt | 151 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +8.7) | [[Belinostat (drug)]] 5 µM 0.325× (z -13.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.340× (z -12.5) |
| [[HS-578T (line)]] | alt | 71.3 | 2 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +17.7) | [[Panobinostat (drug)]] 0.5 µM 0.403× (z -10.2) |
| [[MIA PaCa-2 (line)]] | alt | 170 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.53× (z +9.6) | [[Panobinostat (drug)]] 5 µM 0.342× (z -17.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.390× (z -15.2) |
| [[NCI-H1573 (line)]] | alt | 137 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +19.3) | [[Panobinostat (drug)]] 0.5 µM 0.324× (z -12.5) |
| [[NCI-H2030 (line)]] | alt | 107 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +14.5) | [[Panobinostat (drug)]] 0.5 µM 0.398× (z -10.7) |
| [[Panc 03.27 (line)]] | alt | 152 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.309× (z -16.7) |
| [[PANC-1 (line)]] | alt | 112 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +14.1) | [[Panobinostat (drug)]] 5 µM 0.520× (z -12.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.530× (z -11.8) |
| [[RKO (line)]] | wt | 155 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +10.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.347× (z -12.8) ⚠ toxic; cell-cycle shift, explains ~86% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.473× (z -9.4) |
| [[SNU-1 (line)]] | wt | 145 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +9.3) | [[Dinaciclib (drug)]] 0.05 µM 0.374× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.495× (z -8.8) |
| [[SW 900 (line)]] | alt | 103 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +9.1) | [[Panobinostat (drug)]] 5 µM 0.402× (z -11.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.460× (z -9.9) |
| [[A-172 (line)]] | wt | 120 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.56× (z +9.1) | [[Panobinostat (drug)]] 5 µM 0.474× (z -10.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.549× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 150 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.367× (z -14.7) |
| [[C32 (line)]] | wt | 110 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 6.19× (z +26.9) | [[Panobinostat (drug)]] 0.5 µM 0.388× (z -9.9) |
| [[HT-29 (line)]] | alt | 125 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.434× (z -11.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.483× (z -10.1) |
| [[J82 (line)]] | alt | 110 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +16.6) | [[Panobinostat (drug)]] 5 µM 0.480× (z -10.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.507× (z -10.0) |
| [[KATO III (line)]] | alt | 118 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.451× (z -11.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.456× (z -11.4) |
| [[NCI-H2347 (line)]] | alt | 139 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.369× (z -16.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.383× (z -15.7) |
| [[RPMI-7951 (line)]] | alt | 73.8 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +21.0) | — |
| [[SNU-423 (line)]] | alt | 135 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +12.0) | [[Panobinostat (drug)]] 0.5 µM 0.417× (z -11.4) |
| [[AN3 CA (line)]] | alt | 230 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.242× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change |
| [[H4 (line)]] | wt | 148 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.315× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.433× (z -8.7) |
| [[Hs 766T (line)]] | wt | 101 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +9.5) | — |
| [[SHP-77 (line)]] | alt | 116 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.478× (z -10.0) |
| [[HCT15 (line)]] | alt | 138 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.371× (z -10.4) ⚠ cell-cycle shift, explains ~28% of this change |
| [[hTERT-HPNE (line)]] | wt | 96.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +15.4) | — |
| [[NCI-H1792 (line)]] | alt | 93.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.82× (z +25.0) | — |
| [[SW48 (line)]] | wt | 131 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.406× (z -9.5) |
| [[CHP-212 (line)]] | wt | 143 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 157 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 161 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4216), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 14 of them with an alert (⚠; 14 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BRD1]] | +0.70 | +0.60 / +0.51 | both halves | 1e-05 | pathway: Chromatin modifying enzymes |
| [[BAZ2B]] | +0.67 | +0.59 / +0.46 | both halves | 3e-05 |  |
| [[INO80D]] | +0.66 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[RPRD2]] | +0.66 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[CREBBP]] | +0.66 | +0.44 / +0.54 | both halves | 3e-05 | pathway: Chromatin modifying enzymes; STRING 558 |
| [[GTF2IRD2]] | +0.65 | +0.56 / +0.40 | both halves | 5e-05 |  |
| [[TMEM202-AS1]] | +0.63 | +0.46 / +0.30 | both halves | 2e-04 |  |
| [[AP5S1]] | +0.63 | +0.47 / +0.36 | both halves | 1e-04 |  |
| [[ATE1OSP]] | +0.63 | +0.50 / +0.26 | both halves | 4e-04 |  |
| [[C11orf58]] | +0.63 | +0.54 / +0.34 | both halves | 1e-04 |  |
| [[LINC00869-1]] | +0.63 | +0.45 / +0.36 | both halves | 1e-04 |  |
| [[LINC02307]] | +0.63 | +0.59 / +0.27 | both halves | 3e-04 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST6GALNAC4]] | -0.60 | -0.49 / -0.24 | both halves | 5e-04 |  |
| [[PCMT1]] | -0.57 | -0.41 / -0.31 | both halves | 2e-04 |  |
| [[RSU1]] | -0.57 | -0.54 / -0.35 | both halves | 1e-04 |  |
| [[SDHAF3]] | -0.56 | -0.49 / -0.34 | both halves | 1e-04 |  |
| [[TMEM241]] | -0.56 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[WASF3]] | -0.56 | -0.42 / -0.29 | both halves | 2e-04 |  |
| [[TMEM120B]] | -0.56 | -0.39 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 095]] — Chromatin organization; 48 genes; this gene is in the **+** arm (projection on the module's main direction 0.749). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.36).
- **Nodal map** (x, y) = (2.1, 10.0); signed map (22.0, -17.5). **Vector** length 101, 28.1% of its response variance represented; |z| ≥ 3 in 1,038 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Activation of HOX genes during differentiation* (reactome, mean cos +0.55 to 4); *Activation of anterior HOX genes in hindbrain development during early embryogenesis* (reactome, mean cos +0.55 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +13.0 | +21.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +10.6 | +3.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.3 | +2.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | +5.3 | -8.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.7 | +4.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.2 | +3.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.8 | +2.5 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +2.5 | +2.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.4 | -1.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.3 | +1.9 |
| fall | [[Panobinostat (drug)]] 0.05 µM |  | -5.0 | -11.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -5.0 | -19.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.9 | -8.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | -3.8 | -8.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.8 | -22.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.4 | -5.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.1 | -1.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.0 | -1.1 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.0 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | lysine demethylase 3B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.2 — chr5:138,352,685-138,437,028 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1082, NET22; previously C5orf7, JMJD1B |
| Gene groups (HGNC) | Lysine demethylase 3 family |
| Reactome | 3 pathways, smallest: HDMs demethylate histones; Chromatin modifying enzymes; Chromatin organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7LBC6](https://www.uniprot.org/uniprotkb/Q7LBC6) (Lysine-specific demethylase 3B):

> Histone demethylase that specifically demethylates 'Lys-9' of histone H3, thereby playing a central role in histone code. Demethylation of Lys residue generates formaldehyde and succinate. May have tumor suppressor activity.

**Summary**, from NCBI Gene [51780](https://www.ncbi.nlm.nih.gov/gene/51780):

> Predicted to enable chromatin DNA binding activity; histone H3K9 demethylase activity; and transcription coregulator activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Located in nucleoplasm. Biomarker of acute lymphoblastic leukemia; breast cancer; colorectal cancer; and lung non-small cell carcinoma. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:1337](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1337) · Entrez [51780](https://www.ncbi.nlm.nih.gov/gene/51780) · UniProt [Q7LBC6](https://www.uniprot.org/uniprotkb/Q7LBC6) · Ensembl [ENSG00000120733](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120733)

## Data

Gene col 4216: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4216); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4216, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4216]; `tensor/DDL_lfc|DDL_z.npy` [4216]; `embed/gene_vectors.npy` [4216]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4216 or target_col == 4216). Every well: [[KDM3B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KDM3B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
