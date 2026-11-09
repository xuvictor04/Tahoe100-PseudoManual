---
symbol: "ARMH4"
type: "gene"
col: 6359
ensembl_id: "ENSG00000139971"
name: "armadillo like helical domain containing 4"
location: "14q23.1"
module: 51
arm: "+"
pooled_cpm: 129.83
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 10
n_dd_up_clean: 12
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# ARMH4

*armadillo like helical domain containing 4* — 14q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.23× (z +37.7, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 0.695× (z -11.6, q 1e-28, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ENSA]] (+0.62, fdr 1e-05), [[KMT5B]] (+0.56, fdr 4e-05), [[BTD]] (+0.56, fdr 1e-05); moves opposite to [[OTULIN]] (-0.57, fdr 6e-05), [[ZNF343]] (-0.53, fdr 2e-05), [[RTCA]] (-0.51, fdr 4e-05).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6359.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.23×** | +37.7 | 0e+00 | 46/48 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.19×** | +26.0 | 0e+00 | 45/48 (LS 180, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.91×** | +21.4 | 0e+00 | 44/48 (LS 180, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.71×** | +17.9 | 0e+00 | 44/48 (BT-474, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.68×** | +17.3 | 0e+00 | 45/48 (BT-474, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.62×** | +16.1 | 0e+00 | 43/48 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.45×** | +11.9 | 6e-31 | 37/48 (A498, COLO 205, …) | top dose only | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **1.84×** | +10.6 | 3e-24 | 41/49 (SW480, NCI-H2347, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.68×** | +9.0 | 2e-17 | 32/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.28×** | +8.1 | 2e-14 | 29/48 (A-427, HT-29, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~10% of this change | 1.19× | +5.8 | 3e-07 | 21/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.34×** | +5.0 | 2e-05 | 25/48 (LoVo, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.16× | +4.9 | 4e-05 | 16/49 (LoVo, NCI-H460, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.17× | +4.9 | 4e-05 | 20/45 (KATO III, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +4.5 | 3e-04 | 18/48 (LoVo, A498, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.23×** | +3.5 | 0.012 | 13/49 (HEC-1-A, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.11× | +3.3 | 0.021 | 11/48 (NCI-H460, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[BAY1125976 (drug)]] 5 µM |  | **1.20×** | +3.2 | 0.033 | 6/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.07× | +3.1 | 0.045 | 7/48 (HOP62, A-172, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6359.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.695×** | -11.6 | 1e-28 | 36/48 (LOX-IMVI, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.706×** | -11.1 | 3e-26 | 38/50 (NCI-H23, LS 180, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.771×** | -8.6 | 1e-15 | 30/48 (PANC-1, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.796×** | -7.6 | 5e-12 | 28/48 (SW1417, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.817×** | -6.7 | 2e-09 | 28/48 (J82, Panc 03.27, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.948× | -6.2 | 4e-08 | 1/50 (SW 1088) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | 0.844× | -5.6 | 1e-06 | 20/48 (SW480, C32, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | 0.855× | -5.2 | 1e-05 | 18/48 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | 0.847× | -5.0 | 4e-05 | 20/48 (NCI-H2030, NCI-H1573, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **0.762×** | -4.7 | 1e-04 | 20/48 (NCI-H460, J82, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.05 µM |  | 0.871× | -4.6 | 2e-04 | 12/48 (PANC-1, A-427, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.876× | -4.4 | 5e-04 | 10/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.788×** | -4.1 | 0.002 | 20/48 (LOX-IMVI, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.917× | -4.0 | 0.002 | 6/48 (PANC-1, HOP62, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.800×** | -3.9 | 0.004 | 15/48 (C32, A498, …) | top dose only | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.913× | -3.5 | 0.015 | 6/48 (NCI-H1573, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.817×** | -3.5 | 0.015 | 13/48 (HEC-1-A, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.903× | -3.4 | 0.021 | 11/48 (BT-474, SW 1088, …) | inconsistent across doses |  |
| [[Neratinib (drug)]] 5 µM |  | 0.909× | -3.2 | 0.042 | 7/48 (NCI-H460, NCI-H1792, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.833×** | -3.2 | 0.042 | 11/48 (LOX-IMVI, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6359. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 119 | 9 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +21.4) | — |
| [[LS 180 (line)]] | wt | 127 | 7 (1 ⚠) | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.53× (z +27.0) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.482× (z -10.1) |
| [[NCI-H460 (line)]] | wt | 130 | 7 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +27.9) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.621× (z -8.6) |
| [[BT-474 (line)]] | alt | 161 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +23.7) | — |
| [[NCI-H2030 (line)]] | alt | 190 | 6 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +17.9) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.503× (z -9.1) |
| [[PANC-1 (line)]] | alt | 101 | 6 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +19.0) | [[Docetaxel (drug)]] 0.05 µM 0.565× (z -10.1) ⚠ transcription drop |
| [[SW480 (line)]] | alt | 151 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +27.0) | — |
| [[HT-29 (line)]] | alt | 109 | 5 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.48× (z +13.5) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.551× (z -8.5) |
| [[KATO III (line)]] | alt | 107 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.40× (z +17.4) | — |
| [[NCI-H1573 (line)]] | alt | 237 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +14.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.521× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 132 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +16.5) | — |
| [[SNU-1 (line)]] | wt | 167 | 5 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.39× (z +17.2) | [[Dinaciclib (drug)]] 0.5 µM 0.299× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 218 | 5 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +18.8) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.472× (z -9.4) |
| [[COLO 205 (line)]] | alt | 140 | 4 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.40× (z +22.5) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.472× (z -9.7) |
| [[HEC-1-A (line)]] | alt | 151 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +23.5) | — |
| [[HepG2_C3A (line)]] | wt | 109 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.21× (z +12.5) | — |
| [[HOP62 (line)]] | alt | 113 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +16.9) | — |
| [[NCI-H2347 (line)]] | alt | 128 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +16.8) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.530× (z -10.0) |
| [[RKO (line)]] | wt | 201 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.94× (z +15.0) | — |
| [[SW 900 (line)]] | alt | 136 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +16.3) | — |
| [[SW1417 (line)]] | alt | 120 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.62× (z +11.1) | [[Docetaxel (drug)]] 0.05 µM 0.530× (z -10.2) ⚠ transcription drop |
| [[A-427 (line)]] | wt | 100 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +18.8) | — |
| [[A498 (line)]] | wt | 69.1 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.46× (z +30.8) | — |
| [[AsPC-1 (line)]] | alt | 105 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +16.6) | — |
| [[C-33 A (line)]] | alt | 172 | 4 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.81× (z +13.3) | — |
| [[C32 (line)]] | wt | 150 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +21.8) | — |
| [[CFPAC-1 (line)]] | alt | 129 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +13.6) | [[Docetaxel (drug)]] 0.05 µM 0.560× (z -8.7) ⚠ transcription drop |
| [[HCT15 (line)]] | alt | 146 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +16.3) | — |
| [[HS-578T (line)]] | alt | 81.3 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +16.6) | — |
| [[Hs 766T (line)]] | wt | 91.3 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +17.9) | — |
| [[LOX-IMVI (line)]] | wt | 131 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +18.2) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.476× (z -10.9) |
| [[NCI-H23 (line)]] | alt | 214 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +17.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.580× (z -12.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.470× (z -11.6) |
| [[RPMI-7951 (line)]] | alt | 142 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +20.5) | — |
| [[SNU-423 (line)]] | alt | 106 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +17.7) | — |
| [[hTERT-HPNE (line)]] | wt | 103 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +11.8) | — |
| [[J82 (line)]] | alt | 118 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +12.2) | [[Selinexor (drug)]] 5 µM 0.621× (z -9.8) ⚠ cell-cycle shift, explains ~53% of this change |
| [[MIA PaCa-2 (line)]] | alt | 80.7 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +13.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.03× (z +12.6) | — |
| [[A-172 (line)]] | wt | 78.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +15.0) | — |
| [[A549 (line)]] | wt | 126 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +15.0) | — |
| [[CHP-212 (line)]] | wt | 144 | 0 | 1 (1 ⚠) | — | [[Elimusertib hydrochloride (drug)]] 5 µM 0.0654× (z -10.5) ⚠ toxic |
| [[H4 (line)]] | wt | 112 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +10.0) | — |
| [[Panc 03.27 (line)]] | alt | 146 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +12.9) | — |
| [[SK-MEL-2 (line)]] | alt | 99.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +14.2) | — |
| [[SW 1271 (line)]] | alt | 231 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.18× (z +10.1) | — |
| [[AN3 CA (line)]] | alt | 132 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 174 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 98.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 213 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 110 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6359), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ENSA]] | +0.62 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[KMT5B]] | +0.56 | +0.65 / +0.42 | both halves | 4e-05 |  |
| [[BTD]] | +0.56 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[ADNP]] | +0.55 | +0.78 / +0.38 | both halves | 7e-05 |  |
| [[LINC00641]] | +0.54 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[PMF1]] | +0.54 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[IER2]] | +0.54 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[USP16]] | +0.54 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[BRAF]] | +0.53 | +0.72 / +0.37 | both halves | 8e-05 |  |
| [[PBRM1]] | +0.53 | +0.58 / +0.46 | both halves | 3e-05 |  |
| [[TRMT10A]] | +0.52 | +0.52 / +0.42 | both halves | 4e-05 |  |
| [[ING3]] | +0.51 | +0.66 / +0.37 | both halves | 8e-05 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OTULIN]] | -0.57 | -0.60 / -0.38 | both halves | 6e-05 |  |
| [[ZNF343]] | -0.53 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[RTCA]] | -0.51 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[ANO10]] | -0.51 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[MACIR]] | -0.51 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[NAPB]] | -0.51 | -0.60 / -0.28 | both halves | 3e-04 |  |
| [[PACSIN3]] | -0.50 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[SGTB]] | -0.50 | -0.55 / -0.31 | both halves | 2e-04 |  |
| [[ZW10]] | -0.50 | -0.54 / -0.26 | both halves | 4e-04 |  |
| [[RNF8]] | -0.49 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[MKRN2]] | -0.49 | -0.39 / -0.48 | both halves | 6e-05 |  |
| [[MRPS26]] | -0.49 | -0.37 / -0.44 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises ARMH4's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.457). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-24.7, 13.6); signed map (14.9, -1.3). **Vector** length 118, 34.6% of its response variance represented; |z| ≥ 3 in 1,241 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +11.3 | +4.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +11.1 | +4.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +10.5 | +4.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +9.0 | +37.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.7 | +21.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.6 | +8.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +1.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +4.2 | +3.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +4.1 | +4.9 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +3.0 | +2.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.9 | -4.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -7.1 | -8.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -5.9 | -1.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | -5.1 | -5.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.8 | -3.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.4 | -3.9 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.0 | -4.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.9 | -1.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.9 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | armadillo like helical domain containing 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q23.1 — chr14:57,999,735-58,298,139 (-) |
| Ensembl biotype | protein_coding |
| Also known as | UT2; previously C14orf37 |
| Gene groups (HGNC) | Armadillo like helical domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86TY3](https://www.uniprot.org/uniprotkb/Q86TY3) (Armadillo-like helical domain-containing protein 4):

> May modulate immune response and may play a role in inflammation. Down-modulates STAT3 signaling throught direct interaction with IL6ST, resulting in the inhibition of phosphorylation of STAT3 at 'Tyr-705'. May negatively regulates AKT signaling by modulating the activity of mTORC2 complex through RICTOR interaction (By similarity).

**Summary**, from NCBI Gene [145407](https://www.ncbi.nlm.nih.gov/gene/145407):

> Predicted to enable TORC2 complex binding activity. Involved in regulation of inflammatory response. Located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:19846](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19846) · Entrez [145407](https://www.ncbi.nlm.nih.gov/gene/145407) · UniProt [Q86TY3](https://www.uniprot.org/uniprotkb/Q86TY3) · Ensembl [ENSG00000139971](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139971)

## Data

Gene col 6359: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6359); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6359, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6359]; `tensor/DDL_lfc|DDL_z.npy` [6359]; `embed/gene_vectors.npy` [6359]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6359 or target_col == 6359). Every well: [[ARMH4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARMH4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
