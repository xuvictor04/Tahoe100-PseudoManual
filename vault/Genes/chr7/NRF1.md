---
symbol: "NRF1"
type: "gene"
col: 2761
ensembl_id: "ENSG00000106459"
name: "nuclear respiratory factor 1"
location: "7q32.2"
module: 18
arm: "+"
pooled_cpm: 95.01
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 11
n_dd_up_clean: 10
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# NRF1

*nuclear respiratory factor 1* — 7q32.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.28× (z +15.7, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.342× (z -20.5, q 0e+00, down in 48 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.633× (z -8.7, q 3e-16, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNRF2P2]] (+0.67, fdr 7e-06), [[C2orf69]] (+0.66, fdr 1e-05), [[CRTC3]] (+0.61, fdr 1e-05); moves opposite to [[SF3B1]] (-0.53, fdr 1e-05), [[INTS3]] (-0.52, fdr 3e-05), [[RAB3GAP2]] (-0.52, fdr 3e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2761.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.28×** | +15.7 | 0e+00 | 48/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.07×** | +13.9 | 2e-41 | 43/48 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.95×** | +12.7 | 7e-35 | 45/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.83×** | +11.5 | 2e-28 | 44/48 (LoVo, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.47×** | +7.4 | 2e-11 | 38/48 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +6.3 | 2e-08 | 27/49 (MIA PaCa-2, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.32×** | +5.4 | 7e-06 | 34/48 (Hs 766T, PANC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.32×** | +5.3 | 1e-05 | 33/47 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.30×** | +5.0 | 5e-05 | 29/48 (LS 180, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.23×** | +4.0 | 0.004 | 24/48 (H4, LoVo, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.48×** | +3.9 | 0.005 | 26/48 (NCI-H1573, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.15× | +3.7 | 0.008 | 15/49 (CFPAC-1, A-172, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.21×** | +3.6 | 0.012 | 22/48 (CFPAC-1, H4, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.22×** | +3.6 | 0.013 | 22/47 (SW480, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.20× | +3.4 | 0.025 | 22/48 (LS 180, SW480, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | 1.20× | +3.3 | 0.035 | 17/47 (CFPAC-1, LS 180, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.36×** | +3.1 | 0.071 | 21/49 (SW480, COLO 205, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2761.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.342×** | -20.5 | 0e+00 | 48/49 (SK-MEL-2, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.355×** | -19.1 | 0e+00 | 40/44 (C-33 A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.542×** | -10.8 | 7e-25 | 39/45 (C-33 A, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.633×** | -8.7 | 3e-16 | 39/48 (C32, BT-474, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.652×** | -7.9 | 4e-13 | 36/50 (HEC-1-A, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.682×** | -7.3 | 2e-11 | 36/48 (HepG2/C3A, SHP-77, …) | two highest doses | cell-cycle shift (explains ~18% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.737×** | -5.8 | 4e-07 | 29/48 (C32, SW48, …) | two highest doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.749×** | -5.3 | 7e-06 | 30/48 (SW48, SW 1271, …) | two highest doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.694×** | -5.0 | 4e-05 | 36/48 (HS-578T, SW48, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.778×** | -4.8 | 9e-05 | 27/48 (C32, HS-578T, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.843× | -3.3 | 0.056 | 15/49 (SW 1088, AsPC-1, …) | inconsistent across doses |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.727×** | -3.2 | 0.065 | 21/47 (SW480, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | 0.855× | -3.0 | 0.11 | 20/48 (SHP-77, LOX-IMVI, …) | two highest doses |  |
| [[Cytarabine (drug)]] 0.05 µM |  | 0.844× | -3.0 | 0.11 | 17/48 (HEC-1-A, PANC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2761. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 116 | 7 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.42× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.248× (z -17.7) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 96.7 | 4 (1 ⚠) | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.88× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.339× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.435× (z -9.0) |
| [[SNU-423 (line)]] | alt | 76.0 | 4 (1 ⚠) | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.65× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.231× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -9.0) |
| [[J82 (line)]] | alt | 109 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.275× (z -16.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.594× (z -9.5) |
| [[LoVo (line)]] | wt | 96.5 | 5 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.51× (z +19.0) | [[Dinaciclib (drug)]] 5 µM 0.357× (z -12.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 85.3 | 4 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.35× (z +15.9) | [[Dinaciclib (drug)]] 5 µM 0.135× (z -20.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 78.7 | 5 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.01× (z +12.8) | [[Dinaciclib (drug)]] 0.5 µM 0.332× (z -10.2) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 80.1 | 5 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.89× (z +14.1) | [[Dinaciclib (drug)]] 5 µM 0.435× (z -12.7) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 76.2 | 5 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.84× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.192× (z -11.2) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 85.8 | 4 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.07× (z +12.7) | [[Dinaciclib (drug)]] 5 µM 0.265× (z -14.4) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 89.7 | 4 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.17× (z +15.5) | [[Dinaciclib (drug)]] 0.5 µM 0.191× (z -17.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 85.5 | 5 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.33× (z +17.5) | [[Dinaciclib (drug)]] 5 µM 0.184× (z -23.8) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 85.4 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.338× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.414× (z -10.9) |
| [[SW1417 (line)]] | alt | 131 | 3 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.18× (z +14.4) | [[Dinaciclib (drug)]] 0.5 µM 0.382× (z -12.1) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 91.2 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.66× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.193× (z -18.9) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 166 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0721× (z -24.8) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 51.6 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.62× (z +12.8) | — |
| [[HEC-1-A (line)]] | alt | 113 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.255× (z -16.7) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.393× (z -10.9) |
| [[HT-29 (line)]] | alt | 95.2 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.83× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.225× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.360× (z -11.8) |
| [[NCI-H2030 (line)]] | alt | 98.0 | 1 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +10.5) ⚠ cell-cycle shift, explains ~17% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.226× (z -16.9) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -10.8) |
| [[A-172 (line)]] | wt | 73.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.298× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.540× (z -9.2) |
| [[BT-474 (line)]] | alt | 115 | 2 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.54× (z +10.3) | [[Auranofin (drug)]] 5 µM 0.338× (z -12.1) |
| [[HepG2_C3A (line)]] | wt | 101 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.145× (z -16.9) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 56.0 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.17× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.287× (z -9.9) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 96.8 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.31× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.359× (z -11.6) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 125 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.266× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.253× (z -10.9) |
| [[A549 (line)]] | wt | 98.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.255× (z -15.0) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 167 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0715× (z -16.5) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 113 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.310× (z -12.8) |
| [[LOX-IMVI (line)]] | wt | 137 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.211× (z -13.4) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 81.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.261× (z -14.2) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 148 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.346× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.436× (z -9.1) |
| [[SHP-77 (line)]] | alt | 89.6 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.72× (z +11.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.40× (z +9.7) | — |
| [[SK-MEL-2 (line)]] | alt | 104 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.107× (z -21.7) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 115 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.138× (z -17.3) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 83.4 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.77× (z +9.4) | — |
| [[A-427 (line)]] | wt | 96.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.291× (z -14.4) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 99.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.301× (z -11.4) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 59.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.400× (z -8.6) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 84.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.109× (z -11.5) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 89.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.241× (z -12.1) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 89.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.30× (z +15.7) | — |
| [[NCI-H23 (line)]] | alt | 110 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +13.2) | — |
| [[RPMI-7951 (line)]] | alt | 66.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.204× (z -12.3) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 113 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.149× (z -9.0) ⚠ cell-cycle shift, explains ~19% of this change |
| [[Hs 766T (line)]] | wt | 62.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 92.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 95.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 79.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 83.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2761), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNRF2P2]] | +0.67 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[C2orf69]] | +0.66 | +0.54 / +0.63 | both halves | 1e-05 | **novel candidate** |
| [[CRTC3]] | +0.61 | +0.66 / +0.52 | both halves | 1e-05 | pathway: Mitochondrial biogenesis |
| [[TAF4]] | +0.59 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[KANK1]] | +0.55 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[PTPMT1]] | +0.55 | +0.53 / +0.43 | both halves | 3e-05 |  |
| [[NR2C2]] | +0.53 | +0.40 / +0.57 | both halves | 4e-05 |  |
| [[MEMO1]] | +0.53 | +0.57 / +0.43 | both halves | 4e-05 |  |
| [[PRDM15]] | +0.53 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[ARHGEF11]] | +0.52 | +0.46 / +0.47 | both halves | 2e-05 |  |
| [[CMTM4]] | +0.52 | +0.59 / +0.42 | both halves | 4e-05 |  |
| [[MCM9]] | +0.51 | +0.43 / +0.51 | both halves | 3e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SF3B1]] | -0.53 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[INTS3]] | -0.52 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[RAB3GAP2]] | -0.52 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[MAGED2]] | -0.51 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[TOX4]] | -0.50 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[CREB3]] | -0.49 | -0.53 / -0.37 | both halves | 7e-05 |  |
| [[GRIPAP1]] | -0.48 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[CLCN3]] | -0.47 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[RLIM]] | -0.47 | -0.39 / -0.45 | both halves | 5e-05 |  |
| [[SLC25A46]] | -0.46 | -0.49 / -0.39 | both halves | 6e-05 |  |
| [[BROX]] | -0.46 | -0.52 / -0.37 | both halves | 9e-05 |  |
| [[VAMP7]] | -0.45 | -0.29 / -0.43 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.425). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-47.1, -40.9); signed map (7.7, -4.7). **Vector** length 109, 35.2% of its response variance represented; |z| ≥ 3 in 1,294 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +9.0 | +3.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.0 | +6.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +4.6 | +11.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.4 | +4.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.9 | +1.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.6 | +3.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.4 | +3.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.3 | +2.8 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +3.3 | +2.7 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.4 | -8.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -6.1 | -2.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.3 | +3.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.6 | +0.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | -2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.3 | +3.9 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | -2.7 | -2.5 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -2.5 | -3.0 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -2.5 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | nuclear respiratory factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q32.2 — chr7:129,611,720-129,757,082 (+) |
| Ensembl biotype | protein_coding |
| Also known as | EWG, ALPHA-PAL |
| Reactome | 9 pathways, smallest: Mitochondrial unfolded protein response (UPRmt); Transcriptional activation of mitochondrial biogenesis; Mitochondrial biogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16656](https://www.uniprot.org/uniprotkb/Q16656) (Nuclear respiratory factor 1):

> Transcription factor that activates the expression of the EIF2S1 (EIF2-alpha) gene. Links the transcriptional modulation of key metabolic genes to cellular growth and development. Implicated in the control of nuclear genes required for respiration, heme biosynthesis, and mitochondrial DNA transcription and replication.

**Summary**, from NCBI Gene [4899](https://www.ncbi.nlm.nih.gov/gene/4899):

> This gene encodes a protein that homodimerizes and functions as a transcription factor which activates the expression of some key metabolic genes regulating cellular growth and nuclear genes required for respiration, heme biosynthesis, and mitochondrial DNA transcription and replication. The protein has also been associated with the regulation of neurite outgrowth. Alternative splicing results in multiple transcript variants. Confusion has occurred in bibliographic databases due to the shared …

**Accessions** — [HGNC:7996](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7996) · Entrez [4899](https://www.ncbi.nlm.nih.gov/gene/4899) · UniProt [Q16656](https://www.uniprot.org/uniprotkb/Q16656) · Ensembl [ENSG00000106459](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106459)

## Data

Gene col 2761: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2761); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2761, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2761]; `tensor/DDL_lfc|DDL_z.npy` [2761]; `embed/gene_vectors.npy` [2761]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2761 or target_col == 2761). Every well: [[NRF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NRF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
