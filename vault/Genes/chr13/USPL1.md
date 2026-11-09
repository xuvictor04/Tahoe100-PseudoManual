---
symbol: "USPL1"
type: "gene"
col: 5394
ensembl_id: "ENSG00000132952"
name: "ubiquitin specific peptidase like 1"
location: "13q12.3"
module: 179
arm: "+"
pooled_cpm: 70.75
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 19
n_dd_up_clean: 13
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/179"]
generated_by: "tahoemap"
---

# USPL1

*ubiquitin specific peptidase like 1* — 13q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 13.5× (z +18.2, q 0e+00, up in 49 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.314× (z -15.5, q 0e+00, down in 48 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.674× (z -7.3, q 7e-11, down in 40 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MED23]] (+0.74, fdr 7e-06), [[MED17]] (+0.73, fdr 7e-06), [[NCK1]] (+0.72, fdr 7e-06); moves opposite to [[ERCC6L2]] (-0.62, fdr 1e-05), [[MSRA]] (-0.61, fdr 1e-05), [[NOTCH2NLB]] (-0.61, fdr 7e-06).
> It sits in the **+** arm of [[Module 179]] (RHOA GTPase cycle).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5394.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **13.5×** | +18.2 | 0e+00 | 49/49 (SW480, Hs 766T, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **8.97×** | +15.3 | 0e+00 | 48/48 (SW480, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.53×** | +5.7 | 2e-06 | 32/48 (NCI-H460, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.42×** | +4.7 | 3e-04 | 31/48 (NCI-H460, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.40×** | +4.5 | 8e-04 | 31/48 (NCI-H460, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +4.3 | 0.001 | 24/47 (SHP-77, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.40×** | +4.3 | 0.001 | 29/48 (CFPAC-1, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~18% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.79×** | +4.1 | 0.003 | 23/37 (PANC-1, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.35×** | +3.8 | 0.008 | 23/47 (SW48, LOX-IMVI, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.67×** | +3.6 | 0.017 | 28/49 (HT-29, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[ERK5-IN-2 (drug)]] 5 µM |  | **1.64×** | +3.5 | 0.026 | 24/49 (SW48, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.29×** | +3.4 | 0.027 | 26/48 (CFPAC-1, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tomivosertib (drug)]] 5 µM |  | **1.58×** | +3.2 | 0.057 | 20/48 (PANC-1, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.26×** | +3.1 | 0.080 | 21/48 (C-33 A, A-427, …) | top dose only |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 1.18× | +3.1 | 0.081 | 14/48 (SNU-423, COLO 205, …) | rises with dose | position effect removed |
| [[Anethole trithione (drug)]] 0.5 µM |  | **1.25×** | +3.0 | 0.088 | 16/48 (A498, NCI-H1792, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.25×** | +3.0 | 0.088 | 21/48 (CFPAC-1, SW480, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5394.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.314×** | -15.5 | 0e+00 | 48/49 (A498, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.358×** | -13.2 | 2e-37 | 40/42 (AsPC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.674×** | -7.3 | 7e-11 | 40/49 (LoVo, A498, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.645×** | -5.4 | 9e-06 | 30/45 (HEC-1-A, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.786×** | -4.5 | 8e-04 | 30/48 (HOP62, MIA PaCa-2, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.717×** | -4.4 | 8e-04 | 30/48 (HOP62, SW 1088, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.786×** | -4.4 | 8e-04 | 27/48 (HOP62, RPMI-7951, …) | inconsistent across doses | composition shift |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.750×** | -3.8 | 0.009 | 31/48 (NCI-H2030, Panc 03.27, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.756×** | -3.7 | 0.013 | 24/48 (A-172, Hs 766T, …) | inconsistent across doses |  |
| [[Carbamazepine (drug)]] 5 µM |  | **0.766×** | -3.5 | 0.023 | 29/47 (NCI-H460, PANC-1, …) | top dose only |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.770×** | -3.5 | 0.025 | 28/48 (A-172, SW1417, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.771×** | -3.5 | 0.026 | 27/49 (SK-MEL-2, COLO 205, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.766×** | -3.4 | 0.028 | 28/50 (HOP62, NCI-H2347, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.769×** | -3.2 | 0.050 | 17/47 (CHP-212, RKO, …) | all doses, flat | low cells (technical?) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | **0.786×** | -3.2 | 0.052 | 20/48 (NCI-H1792, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.793×** | -3.1 | 0.070 | 20/48 (Hs 766T, Panc 03.27, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.795×** | -3.0 | 0.078 | 20/49 (SHP-77, SW480, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.801×** | -3.0 | 0.093 | 18/49 (NCI-H2122, NCI-H2030, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5394. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 58.6 | 7 (3 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 15.7× (z +13.8) | — |
| [[RPMI-7951 (line)]] | alt | 84.8 | 2 | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 13.2× (z +11.3) | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -10.9) ⚠ cell-cycle shift, explains ~33% of this change |
| [[SNU-423 (line)]] | alt | 59.1 | 2 | 4 (4 ⚠) | [[PH-797804 (drug)]] 5 µM 8.64× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.419× (z -10.5) ⚠ cell-cycle shift, explains ~33% of this change |
| [[SW1417 (line)]] | alt | 85.9 | 3 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 10.5× (z +11.3) | [[Dinaciclib (drug)]] 0.5 µM 0.288× (z -11.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 57.5 | 3 | 2 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 3.61× (z +11.1) | [[Homoharringtonine (drug)]] 5 µM 0.448× (z -10.3) ⚠ cell-cycle shift, explains ~33% of this change |
| [[A498 (line)]] | wt | 111 | 1 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 6.66× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.119× (z -23.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.533× (z -10.0) |
| [[C-33 A (line)]] | alt | 83.1 | 4 (1 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 5.58× (z +12.4) | [[Dinaciclib (drug)]] 0.5 µM 0.234× (z -10.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 70.9 | 3 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 13.5× (z +11.1) | [[Dinaciclib (drug)]] 0.05 µM 0.117× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HOP62 (line)]] | alt | 59.7 | 2 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 15.1× (z +14.0) | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -12.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.498× (z -9.8) |
| [[HS-578T (line)]] | alt | 59.7 | 2 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 11.3× (z +10.6) | [[Homoharringtonine (drug)]] 0.5 µM 0.229× (z -12.3) ⚠ cell-cycle shift, explains ~12% of this change |
| [[HT-29 (line)]] | alt | 107 | 3 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 21.6× (z +13.5) | [[Dinaciclib (drug)]] 0.5 µM 0.287× (z -10.5) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 63.5 | 2 | 3 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 15.5× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.213× (z -10.9) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 85.7 | 1 | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 7.74× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.177× (z -16.1) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 86.6 | 2 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 16.0× (z +11.9) | [[Dinaciclib (drug)]] 0.05 µM 0.229× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[LoVo (line)]] | wt | 66.5 | 2 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 20.2× (z +14.4) | [[Dinaciclib (drug)]] 0.5 µM 0.244× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.448× (z -10.1) |
| [[NCI-H2347 (line)]] | alt | 55.0 | 2 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 12.2× (z +13.2) | [[Dinaciclib (drug)]] 0.5 µM 0.237× (z -14.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 45.5 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 13.5× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.281× (z -10.1) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 154 | 3 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 59.8× (z +14.7) | [[Dinaciclib (drug)]] 0.5 µM 0.200× (z -11.1) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 86.2 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 29.6× (z +15.2) | [[Dinaciclib (drug)]] 0.5 µM 0.197× (z -14.0) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 68.0 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 21.8× (z +14.8) | [[Dinaciclib (drug)]] 0.5 µM 0.367× (z -9.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 89.8 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 18.2× (z +12.7) | [[Dinaciclib (drug)]] 5 µM 0.224× (z -12.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 76.0 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 15.8× (z +14.8) | [[Dinaciclib (drug)]] 5 µM 0.233× (z -14.4) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 56.7 | 4 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 32.0× (z +14.8) | — |
| [[SW 900 (line)]] | alt | 88.6 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 9.84× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.210× (z -13.7) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 90.8 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 17.4× (z +17.5) | [[Dinaciclib (drug)]] 5 µM 0.419× (z -9.8) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 71.2 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 11.9× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.318× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.518× (z -8.6) |
| [[BT-474 (line)]] | alt | 46.2 | 3 | 0 | [[TAK-901 (drug)]] 0.05 µM 6.73× (z +12.5) | — |
| [[C32 (line)]] | wt | 78.8 | 1 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 22.4× (z +11.0) | [[Homoharringtonine (drug)]] 0.5 µM 0.192× (z -11.1) ⚠ cell-cycle shift, explains ~12% of this change |
| [[CHP-212 (line)]] | wt | 172 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.140× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.335× (z -9.9) |
| [[LS 180 (line)]] | wt | 55.8 | 2 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 28.1× (z +12.0) | [[Dinaciclib (drug)]] 0.5 µM 0.203× (z -11.0) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 67.2 | 2 | 1 | [[TAK-901 (drug)]] 5 µM 16.8× (z +14.1) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.531× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 32.8 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 13.8× (z +12.4) | [[Dinaciclib (drug)]] 0.5 µM 0.384× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 56.6 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 15.4× (z +13.6) | [[Dinaciclib (drug)]] 0.5 µM 0.393× (z -8.9) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 98.3 | 2 (1 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 5.62× (z +12.5) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 11.9× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.0754× (z -18.8) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 88.6 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 25.4× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.128× (z -13.3) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 68.1 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 13.8× (z +16.0) | [[Dinaciclib (drug)]] 0.5 µM 0.125× (z -13.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 84.2 | 2 | 0 | [[TAK-901 (drug)]] 0.05 µM 5.20× (z +9.4) | — |
| [[AsPC-1 (line)]] | alt | 61.6 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 12.3× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.0385× (z -28.2) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 44.9 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 13.2× (z +11.3) | [[Dinaciclib (drug)]] 0.5 µM 0.349× (z -8.8) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 74.6 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 11.9× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.0512× (z -19.0) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 40.7 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 11.6× (z +9.1) | — |
| [[HCT15 (line)]] | alt | 72.3 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 13.6× (z +9.4) | — |
| [[NCI-H1792 (line)]] | alt | 37.1 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 15.9× (z +11.2) | — |
| [[NCI-H661 (line)]] | alt | 107 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.138× (z -8.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 36.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 18.4× (z +10.8) | — |
| [[SW 1088 (line)]] | alt | 109 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0304× (z -12.2) ⚠ cell-cycle shift, explains ~34% of this change |
| [[HepG2_C3A (line)]] | wt | 52.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 86.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 88.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 119 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5394), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MED23]] | +0.74 | +0.77 / +0.75 | both halves | 7e-06 |  |
| [[MED17]] | +0.73 | +0.79 / +0.61 | both halves | 7e-06 |  |
| [[NCK1]] | +0.72 | +0.79 / +0.62 | both halves | 7e-06 |  |
| [[EDRF1]] | +0.71 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[PRRC1]] | +0.70 | +0.76 / +0.63 | both halves | 7e-06 |  |
| [[SDHAP1]] | +0.69 | +0.77 / +0.62 | both halves | 7e-06 |  |
| [[SDHB]] | +0.69 | +0.74 / +0.58 | both halves | 7e-06 |  |
| [[TMEM39A]] | +0.69 | +0.72 / +0.64 | both halves | 7e-06 |  |
| [[ELP2]] | +0.68 | +0.78 / +0.55 | both halves | 1e-05 |  |
| [[UBOX5]] | +0.68 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[TVP23B]] | +0.67 | +0.72 / +0.61 | both halves | 7e-06 |  |
| [[SHQ1]] | +0.67 | +0.79 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERCC6L2]] | -0.62 | -0.74 / -0.54 | both halves | 1e-05 |  |
| [[MSRA]] | -0.61 | -0.64 / -0.54 | both halves | 1e-05 |  |
| [[NOTCH2NLB]] | -0.61 | -0.63 / -0.58 | both halves | 7e-06 |  |
| [[CPSF2]] | -0.59 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[DDX5]] | -0.59 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[PHF19]] | -0.57 | -0.61 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 179]] — RHOA GTPase cycle; 22 genes; this gene is in the **+** arm (projection on the module's main direction 0.690). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-2.2, -15.7); signed map (-35.2, -9.3). **Vector** length 100.0, 32.1% of its response variance represented; |z| ≥ 3 in 1,037 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +6.6 | +0.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.1 | +15.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +6.1 | +1.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.8 | +18.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.0 | +3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | -0.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.8 | -1.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.7 | -0.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -9.0 | -4.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -7.6 | -3.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.9 | -1.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.9 | -4.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.8 | +4.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.8 | -3.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.4 | -0.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.4 | -1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.3 | -4.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.1 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin specific peptidase like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q12.3 — chr13:30,617,693-30,660,770 (+) |
| Ensembl biotype | protein_coding |
| Also known as | bA121O19.1, D13S106E; previously C13orf22 |
| Gene groups (HGNC) | Ubiquitin specific peptidases; Ubiquitin specific peptidase like |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5W0Q7](https://www.uniprot.org/uniprotkb/Q5W0Q7) (SUMO-specific isopeptidase USPL1):

> SUMO-specific isopeptidase involved in protein desumoylation. Specifically binds SUMO proteins with a higher affinity for SUMO2 and SUMO3 which it cleaves more efficiently. Also able to process full-length SUMO proteins to their mature forms. Plays a key role in RNA polymerase-II-mediated snRNA transcription in the Cajal bodies. Is a component of complexes that can bind to U snRNA genes.

**Summary**, from NCBI Gene [10208](https://www.ncbi.nlm.nih.gov/gene/10208):

> Enables SUMO binding activity and deSUMOylase activity. Involved in several processes, including Cajal body organization; protein desumoylation; and snRNA transcription. Located in Cajal body. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20294](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20294) · Entrez [10208](https://www.ncbi.nlm.nih.gov/gene/10208) · UniProt [Q5W0Q7](https://www.uniprot.org/uniprotkb/Q5W0Q7) · Ensembl [ENSG00000132952](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132952)

## Data

Gene col 5394: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5394); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5394, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5394]; `tensor/DDL_lfc|DDL_z.npy` [5394]; `embed/gene_vectors.npy` [5394]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5394 or target_col == 5394). Every well: [[USPL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/USPL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
