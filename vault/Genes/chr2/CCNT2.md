---
symbol: "CCNT2"
type: "gene"
col: 1342
ensembl_id: "ENSG00000082258"
name: "cyclin T2"
location: "2q21.3"
module: 10
arm: "+"
pooled_cpm: 105.54
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 11
n_dd_up_clean: 20
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# CCNT2

*cyclin T2* — 2q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.62× (z +21.0, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.399× (z -13.7, q 9e-40, down in 37 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.510× (z -10.4, q 4e-23, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[THBS4]] (+0.74, fdr 2e-05), [[PLEKHF2]] (+0.71, fdr 1e-05), [[RAB21]] (+0.68, fdr 2e-05); moves opposite to [[ADARB1]] (-0.61, fdr 3e-05), [[NPHP4]] (-0.59, fdr 9e-05), [[SRGAP2]] (-0.59, fdr 3e-05).
> It sits in the **+** arm of [[Module 010]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1342.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.62×** | +21.0 | 0e+00 | 48/48 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.86×** | +16.2 | 0e+00 | 48/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **6.59×** | +15.2 | 0e+00 | 48/49 (SW480, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **6.11×** | +14.6 | 0e+00 | 47/48 (SW480, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.47×** | +14.0 | 3e-42 | 45/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.33×** | +13.1 | 4e-37 | 47/48 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.04×** | +11.0 | 3e-26 | 46/48 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.90×** | +9.9 | 3e-21 | 44/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.83×** | +9.3 | 8e-19 | 39/48 (NCI-H23, C32, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.77×** | +8.5 | 1e-15 | 44/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.49×** | +6.1 | 5e-08 | 39/48 (PANC-1, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.95×** | +5.4 | 3e-06 | 31/38 (NCI-H1573, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.38×** | +5.0 | 3e-05 | 33/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.34×** | +4.5 | 3e-04 | 29/48 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.33×** | +4.5 | 3e-04 | 31/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.33×** | +4.4 | 3e-04 | 31/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.31×** | +4.2 | 9e-04 | 30/48 (PANC-1, NCI-H23, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1342.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.399×** | -13.7 | 9e-40 | 37/44 (SHP-77, SNU-1, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.500×** | -10.7 | 3e-24 | 46/49 (SNU-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.510×** | -10.4 | 4e-23 | 47/48 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.542×** | -9.5 | 4e-19 | 46/48 (CFPAC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.614×** | -7.5 | 6e-12 | 42/48 (SW480, A549, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.660×** | -6.4 | 1e-08 | 42/48 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.761×** | -6.0 | 2e-07 | 36/48 (HepG2/C3A, SW480, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.831×** | -4.1 | 0.004 | 24/49 (A549, HT-29, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 0.856× | -3.4 | 0.040 | 18/48 (NCI-H2347, PANC-1, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.808×** | -3.3 | 0.056 | 27/48 (SW 1271, AsPC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Filgotinib (drug)]] 0.05 µM |  | **0.814×** | -3.2 | 0.076 | 21/48 (NCI-H1573, SW48, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.752×** | -3.1 | 0.078 | 24/48 (SW 1271, SW 900, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1342. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 102 | 15 (2 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 8.72× (z +25.2) | [[Panobinostat (drug)]] 5 µM 0.480× (z -8.6) |
| [[HOP62 (line)]] | alt | 99.0 | 8 (1 ⚠) | 4 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.53× (z +13.7) | [[Dinaciclib (drug)]] 5 µM 0.374× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.404× (z -9.9) |
| [[SW480 (line)]] | alt | 115 | 8 (1 ⚠) | 4 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.48× (z +17.0) | [[Panobinostat (drug)]] 5 µM 0.404× (z -12.3) |
| [[PANC-1 (line)]] | alt | 96.7 | 9 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.66× (z +20.9) | [[Dinaciclib (drug)]] 5 µM 0.449× (z -9.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.493× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 83.7 | 9 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.89× (z +17.3) | [[Dinaciclib (drug)]] 5 µM 0.310× (z -10.2) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 159 | 8 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +15.2) | [[Dinaciclib (drug)]] 5 µM 0.224× (z -13.8) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 110 | 3 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +17.4) | [[Dinaciclib (drug)]] 5 µM 0.325× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.412× (z -9.8) |
| [[BT-474 (line)]] | alt | 115 | 9 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.22× (z +15.1) | — |
| [[AsPC-1 (line)]] | alt | 158 | 4 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +14.0) | [[Dinaciclib (drug)]] 5 µM 0.248× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.360× (z -9.7) |
| [[LoVo (line)]] | wt | 79.5 | 8 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 11.2× (z +15.7) | — |
| [[NCI-H2030 (line)]] | alt | 131 | 6 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.213× (z -11.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 117 | 7 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +16.8) | [[Dinaciclib (drug)]] 5 µM 0.293× (z -13.6) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 75.8 | 5 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +16.0) | [[Dinaciclib (drug)]] 5 µM 0.302× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.402× (z -9.1) |
| [[KATO III (line)]] | alt | 50.6 | 7 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.18× (z +18.7) | — |
| [[LOX-IMVI (line)]] | wt | 116 | 6 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +14.8) | [[Dinaciclib (drug)]] 5 µM 0.359× (z -10.0) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 80.4 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +15.0) | — |
| [[A498 (line)]] | wt | 113 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +19.8) | [[Dinaciclib (drug)]] 5 µM 0.324× (z -11.9) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 106 | 6 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.22× (z +11.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.12× (z +11.2) | — |
| [[HEC-1-A (line)]] | alt | 150 | 4 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 9.21× (z +10.6) | [[Dinaciclib (drug)]] 0.5 µM 0.280× (z -11.7) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 104 | 4 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +14.7) | [[Panobinostat (drug)]] 5 µM 0.425× (z -9.2) |
| [[J82 (line)]] | alt | 99.0 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +18.4) | — |
| [[NCI-H2347 (line)]] | alt | 105 | 2 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +13.6) | [[Dinaciclib (drug)]] 0.5 µM 0.238× (z -16.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.487× (z -8.5) |
| [[RKO (line)]] | wt | 87.9 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.293× (z -11.5) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 154 | 5 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.22× (z +11.5) | [[Panobinostat (drug)]] 0.5 µM 0.420× (z -8.6) |
| [[A-172 (line)]] | wt | 103 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +19.9) | [[Dinaciclib (drug)]] 5 µM 0.381× (z -10.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 99.0 | 4 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 6.99× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.219× (z -14.9) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 146 | 1 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +14.9) | [[Dinaciclib (drug)]] 0.5 µM 0.302× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.365× (z -10.5) |
| [[COLO 205 (line)]] | alt | 113 | 4 | 1 | [[TAK-901 (drug)]] 5 µM 11.3× (z +13.3) | [[Panobinostat (drug)]] 0.5 µM 0.384× (z -10.0) |
| [[HepG2_C3A (line)]] | wt | 127 | 3 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.37× (z +10.8) | [[Panobinostat (drug)]] 5 µM 0.282× (z -11.4) |
| [[LS 180 (line)]] | wt | 97.9 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.27× (z +15.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 103 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +13.8) | — |
| [[Panc 03.27 (line)]] | alt | 105 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +12.6) | [[Panobinostat (drug)]] 5 µM 0.442× (z -8.7) |
| [[RPMI-7951 (line)]] | alt | 127 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +13.4) | — |
| [[SK-MEL-2 (line)]] | alt | 59.1 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.23× (z +18.4) | — |
| [[SNU-1 (line)]] | wt | 124 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +12.6) | [[Dinaciclib (drug)]] 0.5 µM 0.0610× (z -22.0) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 101 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +14.9) | — |
| [[SNU-423 (line)]] | alt | 84.3 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +14.8) | [[Dinaciclib (drug)]] 5 µM 0.369× (z -9.3) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 87.6 | 4 | 0 | [[TAK-901 (drug)]] 0.05 µM 7.12× (z +13.6) | — |
| [[C-33 A (line)]] | alt | 88.5 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.82× (z +9.1) | — |
| [[HCT15 (line)]] | alt | 101 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +12.4) | — |
| [[hTERT-HPNE (line)]] | wt | 77.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +12.3) | — |
| [[HS-578T (line)]] | alt | 89.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +10.4) | — |
| [[SHP-77 (line)]] | alt | 64.8 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.72× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.115× (z -19.2) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 115 | 0 | 2 (1 ⚠) | — | [[Ixazomib (drug)]] 0.05 µM 0.0452× (z -14.0) |
| [[CHP-212 (line)]] | wt | 128 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.181× (z -9.3) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 110 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 119 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1342), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 9 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THBS4]] | +0.74 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[PLEKHF2]] | +0.71 | +0.71 / +0.49 | both halves | 1e-05 |  |
| [[RAB21]] | +0.68 | +0.73 / +0.47 | both halves | 2e-05 |  |
| [[BDNF-AS]] | +0.67 | +0.43 / +0.40 | both halves | 5e-05 |  |
| [[KRBA2]] | +0.67 | +0.38 / +0.47 | both halves | 7e-05 |  |
| [[AHI1-DT]] | +0.67 | +0.42 / +0.42 | both halves | 4e-05 |  |
| [[DPH6-DT]] | +0.66 | +0.40 / +0.37 | both halves | 8e-05 |  |
| [[OXA1L-DT]] | +0.66 | +0.41 / +0.36 | both halves | 1e-04 |  |
| [[ZNF407-AS1]] | +0.66 | +0.44 / +0.41 | both halves | 4e-05 |  |
| [[MAILR]] | +0.66 | +0.36 / +0.29 | both halves | 2e-04 |  |
| [[EHHADH]] | +0.65 | +0.65 / +0.42 | both halves | 4e-05 |  |
| [[C3orf38]] | +0.64 | +0.52 / +0.32 | both halves | 2e-04 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADARB1]] | -0.61 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[NPHP4]] | -0.59 | -0.42 / -0.36 | both halves | 9e-05 |  |
| [[SRGAP2]] | -0.59 | -0.57 / -0.46 | both halves | 3e-05 |  |
| [[TMEM184B]] | -0.59 | -0.38 / -0.50 | both halves | 6e-05 |  |
| [[KIAA1958]] | -0.58 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[GNAI2]] | -0.58 | -0.34 / -0.27 | both halves | 3e-04 |  |
| [[SRGAP2C]] | -0.57 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[EHD4]] | -0.57 | -0.43 / -0.32 | both halves | 2e-04 |  |
| [[RELL1]] | -0.57 | -0.50 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.712). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (0.0, 18.0); signed map (27.9, -15.3). **Vector** length 74.8, 26.7% of its response variance represented; |z| ≥ 3 in 1,397 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.2 | +9.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +6.9 | +2.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +6.0 | +0.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.9 | +0.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.4 | +13.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.4 | -2.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.0 | +4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +0.3 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.7 | -0.3 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -4.6 | -9.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.5 | -7.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.2 | -10.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.6 | +11.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.1 | -6.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.5 | -1.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.3 | +0.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.0 | +1.5 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.9 | +1.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.9 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | cyclin T2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q21.3 — chr2:134,918,235-134,959,342 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Cyclins; P-TEFb complex subunits |
| Reactome | 22 pathways, smallest: HIV elongation arrest and recovery; Pausing and recovery of HIV elongation; SMAD2/SMAD3:SMAD4 heterotrimer regulates transcription |
| Matched by | ensembl_id |

**Function**, from UniProt [O60583](https://www.uniprot.org/uniprotkb/O60583) (Cyclin-T2):

> Regulatory subunit of the cyclin-dependent kinase pair (CDK9/cyclin T) complex, also called positive transcription elongation factor B (P-TEFB), which is proposed to facilitate the transition from abortive to production elongation by phosphorylating the CTD (carboxy-terminal domain) of the large subunit of RNA polymerase II (RNAP II). The activity of this complex is regulated by binding with 7SK snRNA. Plays a role during muscle differentiation; P-TEFB complex interacts with MYOD1; this …

**Summary**, from NCBI Gene [905](https://www.ncbi.nlm.nih.gov/gene/905):

> The protein encoded by this gene belongs to the highly conserved cyclin family, whose members are characterized by a dramatic periodicity in protein abundance through the cell cycle. Cyclins function as regulators of CDK kinases. Different cyclins exhibit distinct expression and degradation patterns which contribute to the temporal coordination of each mitotic event. This cyclin and its kinase partner CDK9 were found to be subunits of the transcription elongation factor p-TEFb. The p-TEFb …

**Accessions** — [HGNC:1600](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1600) · Entrez [905](https://www.ncbi.nlm.nih.gov/gene/905) · UniProt [O60583](https://www.uniprot.org/uniprotkb/O60583) · Ensembl [ENSG00000082258](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000082258)

## Data

Gene col 1342: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1342); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1342, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1342]; `tensor/DDL_lfc|DDL_z.npy` [1342]; `embed/gene_vectors.npy` [1342]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1342 or target_col == 1342). Every well: [[CCNT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCNT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
