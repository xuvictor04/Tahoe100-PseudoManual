---
symbol: "PPP6R2"
type: "gene"
col: 1900
ensembl_id: "ENSG00000100239"
name: "protein phosphatase 6 regulatory subunit 2"
location: "22q13.33"
module: 172
arm: "+"
pooled_cpm: 100.02
n_lines_expressing: 49
n_dd_up: 11
n_dd_down: 8
n_dd_up_clean: 8
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/172"]
generated_by: "tahoemap"
---

# PPP6R2

*protein phosphatase 6 regulatory subunit 2* — 22q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.76× (z +20.6, q 0e+00, up in 44 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.470× (z -27.4, q 0e+00, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF609]] (+0.68, fdr 7e-06), [[UBE2W]] (+0.64, fdr 7e-06), [[GUSBP11]] (+0.64, fdr 1e-05); moves opposite to [[CRYZ]] (-0.56, fdr 2e-05), [[IVNS1ABP]] (-0.55, fdr 1e-05), [[VAMP1]] (-0.53, fdr 4e-05).
> It is in [[Module 172]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1900.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.76×** | +20.6 | 0e+00 | 44/47 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.00×** | +17.7 | 0e+00 | 46/47 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.65×** | +12.8 | 2e-35 | 44/47 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.51×** | +10.6 | 3e-24 | 42/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.85×** | +8.3 | 1e-14 | 33/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.37×** | +8.0 | 8e-14 | 35/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.37×** | +7.8 | 6e-13 | 33/47 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.33×** | +6.0 | 1e-07 | 27/47 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.23×** | +5.2 | 1e-05 | 22/47 (H4, MIA PaCa-2, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.41×** | +4.6 | 2e-04 | 25/47 (HEC-1-A, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.22×** | +4.1 | 0.002 | 19/48 (A498, NCI-H460, …) | two highest doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.16× | +3.8 | 0.007 | 13/47 (PANC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.14× | +3.4 | 0.032 | 14/47 (CFPAC-1, Hs 766T, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.13× | +3.1 | 0.076 | 10/47 (H4, NCI-H23, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1900.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.470×** | -27.4 | 0e+00 | 45/48 (C-33 A, SW1417, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.604×** | -12.9 | 1e-35 | 38/48 (NCI-H1573, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.659×** | -10.3 | 2e-22 | 37/42 (NCI-H1573, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.786×** | -8.7 | 3e-16 | 31/47 (MIA PaCa-2, Hs 766T, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.706×** | -8.3 | 2e-14 | 31/44 (SW48, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.742×** | -7.4 | 2e-11 | 30/49 (C32, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | 0.843× | -4.4 | 1e-03 | 23/47 (RPMI-7951, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 0.842× | -4.2 | 0.002 | 21/47 (C32, MIA PaCa-2, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.840× | -3.7 | 0.014 | 15/47 (COLO 205, SW 900, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.911× | -3.4 | 0.042 | 8/47 (SNU-423, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.880× | -3.3 | 0.054 | 10/47 (LoVo, KATO III, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.786×** | -3.2 | 0.058 | 16/46 (C32, COLO 205, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.860× | -3.2 | 0.058 | 16/48 (MIA PaCa-2, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 0.887× | -3.1 | 0.080 | 15/47 (C32, SHP-77, …) | top dose only |  |
| [[NVP-BHG712 (drug)]] 0.5 µM |  | **0.825×** | -3.1 | 0.080 | 6/47 (PANC-1, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1900. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 161 | 0 | 8 (4 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.323× (z -14.2) |
| [[SW480 (line)]] | alt | 104 | 6 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.73× (z +16.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.393× (z -21.7) |
| [[KATO III (line)]] | alt | 103 | 4 (1 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.81× (z +14.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -19.3) |
| [[NCI-H1792 (line)]] | alt | 90.0 | 3 | 4 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.69× (z +12.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -15.0) |
| [[HOP62 (line)]] | alt | 106 | 4 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +14.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.414× (z -17.9) |
| [[LoVo (line)]] | wt | 129 | 4 (1 ⚠) | 2 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.38× (z +13.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.25× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.488× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.649× (z -9.1) |
| [[MIA PaCa-2 (line)]] | alt | 96.2 | 2 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +14.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -16.2) |
| [[NCI-H1573 (line)]] | alt | 190 | 2 (1 ⚠) | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.05× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.126× (z -30.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.638× (z -9.7) |
| [[NCI-H23 (line)]] | alt | 124 | 3 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +13.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -14.2) |
| [[PANC-1 (line)]] | alt | 93.0 | 5 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +23.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.418× (z -19.6) |
| [[RKO (line)]] | wt | 141 | 2 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -14.8) |
| [[HT-29 (line)]] | alt | 86.6 | 2 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +17.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.305× (z -20.2) |
| [[BT-474 (line)]] | alt | 129 | 3 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.56× (z +11.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.558× (z -10.2) |
| [[C-33 A (line)]] | alt | 164 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.176× (z -30.0) |
| [[COLO 205 (line)]] | alt | 107 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +16.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.534× (z -9.6) |
| [[H4 (line)]] | wt | 69.5 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.15× (z +9.3) ⚠ cell-cycle shift, explains ~13% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 3.14× (z +9.2) | — |
| [[Hs 766T (line)]] | wt | 112 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +16.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.464× (z -13.8) |
| [[NCI-H460 (line)]] | wt | 103 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.56× (z +10.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.548× (z -13.6) |
| [[SHP-77 (line)]] | alt | 140 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.54× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -16.9) |
| [[SNU-1 (line)]] | wt | 132 | 1 | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.43× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.130× (z -19.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -10.5) |
| [[AsPC-1 (line)]] | alt | 84.7 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +16.8) | [[Dinaciclib (drug)]] 5 µM 0.401× (z -9.0) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 64.9 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +13.8) | — |
| [[HS-578T (line)]] | alt | 116 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +19.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -16.5) |
| [[SNU-423 (line)]] | alt | 91.3 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +11.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.456× (z -13.7) |
| [[SW1417 (line)]] | alt | 93.9 | 1 | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.00× (z +9.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.314× (z -23.2) |
| [[SW48 (line)]] | wt | 151 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.217× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -12.8) |
| [[A-172 (line)]] | wt | 68.8 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.564× (z -10.4) |
| [[A-427 (line)]] | wt | 84.8 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +11.4) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.386× (z -11.9) |
| [[AN3 CA (line)]] | alt | 126 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.218× (z -15.2) |
| [[HCT15 (line)]] | alt | 113 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +9.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.377× (z -13.8) |
| [[HEC-1-A (line)]] | alt | 99.4 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.440× (z -17.2) |
| [[hTERT-HPNE (line)]] | wt | 92.7 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.419× (z -9.1) ⚠ cell-cycle shift, explains ~7% of this change |
| [[J82 (line)]] | alt | 81.4 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -14.1) |
| [[LS 180 (line)]] | wt | 113 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +10.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.522× (z -10.9) |
| [[NCI-H2030 (line)]] | alt | 129 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +19.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.377× (z -20.6) |
| [[NCI-H2347 (line)]] | alt | 77.3 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +16.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.580× (z -10.6) |
| [[Panc 03.27 (line)]] | alt | 78.6 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -14.2) |
| [[RPMI-7951 (line)]] | alt | 82.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.205× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.382× (z -14.2) |
| [[SW 900 (line)]] | alt | 80.0 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +12.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -12.8) |
| [[A498 (line)]] | wt | 75.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.518× (z -8.9) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 84.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.490× (z -9.3) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 109 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -10.1) |
| [[HepG2_C3A (line)]] | wt | 84.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.8 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 57.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 113 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1900), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF609]] | +0.68 | +0.70 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[UBE2W]] | +0.64 | +0.70 / +0.58 | both halves | 7e-06 |  |
| [[GUSBP11]] | +0.64 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[UBE2J2]] | +0.64 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[GMEB2]] | +0.64 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[IP6K1]] | +0.63 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[FAM193A]] | +0.63 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[OPA3]] | +0.61 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[GPATCH8]] | +0.59 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[SRSF4]] | +0.59 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[NCOA6]] | +0.58 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[PIAS4]] | +0.58 | +0.59 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRYZ]] | -0.56 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[IVNS1ABP]] | -0.55 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[VAMP1]] | -0.53 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[OAT]] | -0.52 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[SLC39A6]] | -0.52 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[PGRMC1]] | -0.51 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[CPNE3]] | -0.49 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[GNAI3]] | -0.48 | -0.43 / -0.59 | both halves | 3e-05 |  |
| [[SAR1A]] | -0.48 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[TPP2]] | -0.48 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[GLUD1]] | -0.47 | -0.40 / -0.44 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 172]]; 24 genes; every member is in the + arm (projection on the module's main direction 0.715). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-47.0, 12.3); signed map (-2.4, -10.8). **Vector** length 114, 33.7% of its response variance represented; |z| ≥ 3 in 1,072 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +6.2 | +12.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.0 | +10.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.7 | +20.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.4 | +2.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +5.0 | +17.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.2 | +2.6 |
|  | [[Amsacrine (drug)]] 5 µM |  | +3.8 | +2.3 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +3.5 | +1.6 |
|  | [[Rapamycin (drug)]] 5 µM |  | +3.0 | +1.3 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +3.0 | +2.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.8 | -27.4 |
|  | [[Selinexor (drug)]] 5 µM |  | -6.5 | -8.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.2 | -7.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.8 | -2.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.4 | -3.7 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -3.0 | -2.6 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | -2.4 | -2.4 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | -2.3 | -2.8 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -2.3 | -0.9 |
|  | [[Lonafarnib (drug)]] 0.5 µM |  | -2.3 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase 6 regulatory subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.33 — chr22:50,343,304-50,445,090 (+) |
| Ensembl biotype | protein_coding |
| Also known as | dJ579N16.1, SAP190; previously KIAA0685, SAPS2 |
| Gene groups (HGNC) | Protein phosphatase 6 regulatory subunits; Armadillo like helical domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [O75170](https://www.uniprot.org/uniprotkb/O75170) (Serine/threonine-protein phosphatase 6 regulatory subunit 2):

> Regulatory subunit of protein phosphatase 6 (PP6). May function as a scaffolding PP6 subunit. Involved in the PP6-mediated dephosphorylation of NFKBIE opposing its degradation in response to TNF.

**Summary**, from NCBI Gene [9701](https://www.ncbi.nlm.nih.gov/gene/9701):

> The protein encoded by this gene is a regulatory protein for the protein phosphatase-6 catalytic subunit. Together, these proteins act as a significant T-loop phosphatase for Aurora A, an essential mitotic kinase. Loss of function of either the regulatory or catalytic subunit of protein phosphatase-6 interferes with spindle formation and chromosome alignment. [provided by RefSeq, May 2017]

**Accessions** — [HGNC:19253](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19253) · Entrez [9701](https://www.ncbi.nlm.nih.gov/gene/9701) · UniProt [O75170](https://www.uniprot.org/uniprotkb/O75170) · Ensembl [ENSG00000100239](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100239)

## Data

Gene col 1900: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1900); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1900, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1900]; `tensor/DDL_lfc|DDL_z.npy` [1900]; `embed/gene_vectors.npy` [1900]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1900 or target_col == 1900). Every well: [[PPP6R2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP6R2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
