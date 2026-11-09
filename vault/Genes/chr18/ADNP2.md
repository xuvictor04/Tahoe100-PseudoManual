---
symbol: "ADNP2"
type: "gene"
col: 2150
ensembl_id: "ENSG00000101544"
name: "ADNP homeobox 2"
location: "18q23"
module: 175
arm: "+"
pooled_cpm: 58.96
n_lines_expressing: 50
n_dd_up: 31
n_dd_down: 6
n_dd_up_clean: 25
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/175"]
generated_by: "tahoemap"
---

# ADNP2

*ADNP homeobox 2* — 18q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.70× (z +48.2, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.536× (z -16.2, q 0e+00, down in 40 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Epirubicin (hydrochloride) (drug)]] 5 µM: 0.827× (z -4.8, q 3e-04, down in 21 of 50 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF669]] (+0.64, fdr 1e-05), [[TAF7]] (+0.62, fdr 7e-06), [[ABL2]] (+0.60, fdr 1e-05); moves opposite to [[SETD3]] (-0.66, fdr 7e-06), [[ANAPC5]] (-0.63, fdr 1e-05), [[ABCB10]] (-0.61, fdr 1e-05).
> It is in [[Module 175]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PYDC2-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2150.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.70×** | +48.2 | 0e+00 | 48/48 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.69×** | +32.7 | 0e+00 | 47/48 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **3.13×** | +29.7 | 0e+00 | 48/48 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.67×** | +25.6 | 0e+00 | 47/47 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[TAK-901 (drug)]] 5 µM |  | **5.36×** | +22.1 | 0e+00 | 47/49 (NCI-H460, SW480, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.29×** | +21.6 | 0e+00 | 44/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.15×** | +19.9 | 0e+00 | 46/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.33×** | +19.2 | 0e+00 | 43/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.91×** | +16.8 | 0e+00 | 46/48 (HT-29, PANC-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.80×** | +15.3 | 0e+00 | 32/48 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.48×** | +11.9 | 5e-31 | 32/48 (HEC-1-A, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +11.1 | 5e-27 | 37/47 (NCI-H460, SW48, …) | top dose only | cell-cycle shift (explains ~14% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.52×** | +10.9 | 5e-26 | 36/48 (HT-29, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.49×** | +10.3 | 2e-23 | 36/48 (HT-29, KATO III, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.38×** | +8.3 | 3e-15 | 37/48 (HT-29, A498, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +7.3 | 7e-12 | 24/48 (NCI-H460, SW1417, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.31×** | +7.0 | 7e-11 | 30/48 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.30×** | +6.8 | 4e-10 | 27/48 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2150.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.536×** | -16.2 | 0e+00 | 40/48 (A-427, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.573×** | -14.0 | 6e-42 | 30/44 (NCI-H23, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.793×** | -5.6 | 4e-06 | 22/45 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.827×** | -4.8 | 3e-04 | 21/50 (HEC-1-A, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.834× | -4.6 | 6e-04 | 18/48 (SW480, SNU-423, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.897× | -4.0 | 0.005 | 6/48 (A-427, NCI-H2030, …) | rises with dose |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.738×** | -4.0 | 0.005 | 15/48 (HCT15, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.859× | -4.0 | 0.005 | 18/48 (H4, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.900× | -3.9 | 0.007 | 7/48 (SNU-1, MIA PaCa-2, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.869× | -3.7 | 0.014 | 8/49 (C32, HepG2/C3A, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 0.906× | -3.6 | 0.014 | 9/48 (AsPC-1, LOX-IMVI, …) | top dose only |  |
| [[Alpelisib (drug)]] 5 µM |  | **0.759×** | -3.6 | 0.014 | 16/47 (RPMI-7951, A549, …) | top dose only | noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | 0.912× | -3.4 | 0.027 | 7/48 (NCI-H1792, HOP62, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.885× | -3.2 | 0.058 | 10/48 (AN3 CA, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Erlotinib (drug)]] 5 µM |  | 0.887× | -3.0 | 0.096 | 12/47 (SW48, A549, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2150. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 55.3 | 15 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.87× (z +40.8) | — |
| [[LOX-IMVI (line)]] | wt | 60.5 | 10 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.08× (z +29.8) | [[Dinaciclib (drug)]] 0.5 µM 0.367× (z -11.8) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 68.1 | 10 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.41× (z +30.4) | [[Dinaciclib (drug)]] 5 µM 0.330× (z -12.4) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 61.2 | 9 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +19.7) | [[Dinaciclib (drug)]] 0.5 µM 0.488× (z -8.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 59.4 | 8 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.02× (z +34.4) | [[Dinaciclib (drug)]] 0.5 µM 0.454× (z -8.8) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 92.9 | 10 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.84× (z +16.6) | — |
| [[C32 (line)]] | wt | 55.8 | 8 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +18.1) | [[Dinaciclib (drug)]] 5 µM 0.294× (z -11.1) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 72.7 | 7 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.54× (z +22.6) | [[Dinaciclib (drug)]] 5 µM 0.286× (z -11.2) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 67.6 | 8 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.81× (z +37.9) | [[Dinaciclib (drug)]] 5 µM 0.481× (z -8.7) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 72.2 | 8 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.49× (z +18.2) | [[Dinaciclib (drug)]] 0.5 µM 0.317× (z -14.0) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 104 | 8 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +18.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.443× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 92.9 | 7 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.39× (z +13.7) | [[Dinaciclib (drug)]] 5 µM 0.175× (z -15.7) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 42.2 | 7 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.59× (z +20.4) | [[Dinaciclib (drug)]] 5 µM 0.217× (z -13.9) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 80.5 | 7 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +25.7) | [[Dinaciclib (drug)]] 0.5 µM 0.410× (z -13.3) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 81.9 | 7 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +18.3) | [[Dinaciclib (drug)]] 5 µM 0.286× (z -13.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 34.1 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.51× (z +22.4) | — |
| [[SW480 (line)]] | alt | 51.6 | 7 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.24× (z +17.2) | [[Dinaciclib (drug)]] 5 µM 0.487× (z -10.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 66.4 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +19.4) | [[Dinaciclib (drug)]] 0.5 µM 0.0972× (z -22.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 58.6 | 5 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.20× (z +29.7) | [[Dinaciclib (drug)]] 5 µM 0.358× (z -12.6) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 74.4 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.57× (z +24.1) | — |
| [[H4 (line)]] | wt | 93.0 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +14.5) | — |
| [[HepG2_C3A (line)]] | wt | 84.8 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +15.9) | — |
| [[NCI-H23 (line)]] | alt | 76.3 | 4 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.96× (z +21.2) | [[Dinaciclib (drug)]] 5 µM 0.217× (z -15.9) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 80.5 | 5 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.93× (z +14.7) | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0848× (z -13.5) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 48.5 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.30× (z +17.7) | [[Dinaciclib (drug)]] 0.5 µM 0.217× (z -11.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 33.8 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.82× (z +22.6) | — |
| [[Hs 766T (line)]] | wt | 51.9 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.24× (z +21.5) | [[Dinaciclib (drug)]] 0.5 µM 0.364× (z -9.3) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 56.0 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +17.9) | — |
| [[NCI-H1792 (line)]] | alt | 65.2 | 6 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 6.02× (z +17.8) | — |
| [[NCI-H2030 (line)]] | alt | 41.8 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.58× (z +28.5) | — |
| [[NCI-H2347 (line)]] | alt | 33.4 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.67× (z +26.8) | — |
| [[SK-MEL-2 (line)]] | alt | 83.5 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +21.2) | [[Dinaciclib (drug)]] 0.5 µM 0.456× (z -9.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 70.4 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +16.4) | [[Dinaciclib (drug)]] 0.5 µM 0.416× (z -9.5) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 52.6 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +14.6) | — |
| [[SW1417 (line)]] | alt | 54.8 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +17.2) | — |
| [[A-172 (line)]] | wt | 50.6 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.27× (z +26.5) | [[Dinaciclib (drug)]] 5 µM 0.377× (z -9.7) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 46.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.24× (z +19.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 47.1 | 3 | 0 | [[Harringtonine (drug)]] 5 µM 6.60× (z +15.1) | — |
| [[RPMI-7951 (line)]] | alt | 58.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.88× (z +16.0) | — |
| [[CFPAC-1 (line)]] | alt | 37.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +17.5) | — |
| [[Panc 03.27 (line)]] | alt | 32.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +13.8) | — |
| [[CHP-212 (line)]] | wt | 80.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +10.4) | — |
| [[HCT15 (line)]] | alt | 45.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.97× (z +8.8) | — |
| [[AN3 CA (line)]] | alt | 86.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 75.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 57.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 59.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 80.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 44.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2150), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*51 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF669]] | +0.64 | +0.52 / +0.66 | both halves | 1e-05 | same gene group |
| [[TAF7]] | +0.62 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[ABL2]] | +0.60 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[ZNF274]] | +0.60 | +0.49 / +0.61 | both halves | 1e-05 | same gene group |
| [[ADNP]] | +0.59 | +0.50 / +0.56 | both halves | 1e-05 | same gene group; pathway: ATP-dependent chromatin remodelers; STRING 480 |
| [[ZNF155]] | +0.58 | +0.42 / +0.68 | both halves | 4e-05 | same gene group |
| [[CWC22]] | +0.57 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[JAGN1]] | +0.56 | +0.40 / +0.60 | both halves | 5e-05 |  |
| [[ATF7IP]] | +0.56 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[ZNF513]] | +0.55 | +0.51 / +0.51 | both halves | 1e-05 | same gene group |
| [[PPIF]] | +0.55 | +0.46 / +0.57 | both halves | 2e-05 |  |
| [[ZBTB4]] | +0.55 | +0.51 / +0.56 | both halves | 1e-05 | same gene group |

## Genes that move opposite

*49 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SETD3]] | -0.66 | -0.61 / -0.67 | both halves | 7e-06 |  |
| [[ANAPC5]] | -0.63 | -0.52 / -0.67 | both halves | 1e-05 |  |
| [[ABCB10]] | -0.61 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[RWDD4]] | -0.61 | -0.64 / -0.53 | both halves | 1e-05 |  |
| [[GK5]] | -0.60 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[DDHD2]] | -0.59 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[TMEM50B]] | -0.58 | -0.47 / -0.67 | both halves | 2e-05 |  |
| [[WHAMMP1]] | -0.58 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[NOMO2]] | -0.57 | -0.45 / -0.59 | both halves | 3e-05 |  |
| [[ATPAF1]] | -0.56 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[INTS8]] | -0.56 | -0.38 / -0.59 | both halves | 7e-05 |  |
| [[NDUFV1]] | -0.56 | -0.45 / -0.60 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PYDC2-AS1]] | B | PYDC2-AS1 activity raises ADNP2's level | lines that do not express PYDC2-AS1 (26) vs lines expressing it (24) | 1.31× lower at baseline in the lines without PYDC2-AS1 | 0.025 | ⚠ within organs, on part of the lines; also absent: BCHE, CPED1, CCNYL2 |
| [[ZNF513]] | B | ZNF513 activity raises ADNP2's level | lines that do not express ZNF513 (5) vs lines expressing it (45) | 1.43× lower at baseline in the lines without ZNF513 | 0.096 | ⚠ within organs, on part of the lines; also absent: SPATA13; maybe low, not absent |
| [[ID3]] | B | ID3 activity raises ADNP2's level | lines that do not express ID3 (10) vs lines expressing it (40) | 1.19× lower at baseline in the lines without ID3 | 0.0995 | ⚠ within organs, on part of the lines; also absent: SAMD11, TTC28, ITPR1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 175]]; 23 genes; every member is in the + arm (projection on the module's main direction -0.676). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-29.6, 13.1); signed map (5.2, -27.9). **Vector** length 93.9, 25.9% of its response variance represented; |z| ≥ 3 in 1,236 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +10.5 | +16.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.2 | +7.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.8 | +3.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.8 | +2.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.2 | +32.7 |
|  | [[Carbamazepine (drug)]] 5 µM |  | +3.1 | -0.7 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +3.1 | +1.2 |
|  | [[Belzutifan (drug)]] 5 µM |  | +3.0 | +2.0 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -2.9 | -4.8 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -2.8 | -2.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.5 | -4.6 |
|  | [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -0.6 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -2.4 | -0.7 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -2.4 | -1.7 |
|  | [[Tomivosertib (drug)]] 5 µM |  | -2.3 | +1.0 |
|  | [[Capivasertib (drug)]] 0.5 µM |  | -2.0 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | ADNP homeobox 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q23 — chr18:80,109,262-80,147,523 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0863; previously ZNF508 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; ZF class homeoboxes and pseudogenes |
| Reactome | 5 pathways, smallest: ChAHP complex assembly; CHD3, CHD4, CHD5 subfamily; CHD chromatin remodelers |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6IQ32](https://www.uniprot.org/uniprotkb/Q6IQ32) (Activity-dependent neuroprotector homeobox protein 2):

> May be involved in transcriptional regulation. May play a role in neuronal function; perhaps involved in protection of brain tissues from oxidative stress. May be involved in erythroid differentiation (By similarity).

**Summary**, from NCBI Gene [22850](https://www.ncbi.nlm.nih.gov/gene/22850):

> Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific. Predicted to be involved in nervous system development and regulation of gene expression. Predicted to be located in chromatin. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23803](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23803) · Entrez [22850](https://www.ncbi.nlm.nih.gov/gene/22850) · UniProt [Q6IQ32](https://www.uniprot.org/uniprotkb/Q6IQ32) · Ensembl [ENSG00000101544](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101544)

## Data

Gene col 2150: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2150); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2150, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2150]; `tensor/DDL_lfc|DDL_z.npy` [2150]; `embed/gene_vectors.npy` [2150]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2150 or target_col == 2150). Every well: [[ADNP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADNP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
