---
symbol: "GLCE"
type: "gene"
col: 6191
ensembl_id: "ENSG00000138604"
name: "glucuronic acid epimerase"
location: "15q23"
module: 88
arm: "-"
pooled_cpm: 51.08
n_lines_expressing: 49
n_dd_up: 13
n_dd_down: 19
n_dd_up_clean: 11
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/088"]
generated_by: "tahoemap"
---

# GLCE

*glucuronic acid epimerase* — 15q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.27× (z +33.4, q 0e+00, up in 46 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.579× (z -12.6, q 1e-33, down in 37 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.397× (z -11.1, q 2e-26, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP8A1]] (+0.57, fdr 2e-05), [[DLG3]] (+0.57, fdr 2e-05), [[CDC42SE2]] (+0.57, fdr 2e-05); moves opposite to [[ANKLE2]] (-0.62, fdr 5e-05), [[GTF2H1]] (-0.60, fdr 2e-05), [[METTL6]] (-0.57, fdr 5e-05).
> It sits in the **-** arm of [[Module 088]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6191.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **4.27×** | +33.4 | 0e+00 | 46/47 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.67×** | +29.9 | 0e+00 | 46/47 (NCI-H2030, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.48×** | +28.7 | 0e+00 | 45/47 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.80×** | +19.1 | 0e+00 | 45/47 (SW480, CFPAC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.11×** | +17.2 | 0e+00 | 43/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +12.3 | 1e-32 | 29/48 (A-172, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.61×** | +11.5 | 6e-29 | 40/48 (PANC-1, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.58×** | +10.6 | 2e-24 | 34/47 (NCI-H2347, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.49×** | +9.2 | 1e-18 | 32/47 (A-172, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.39×** | +7.5 | 4e-12 | 27/48 (CFPAC-1, NCI-H2347, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.40×** | +7.4 | 8e-12 | 27/46 (SW480, RPMI-7951, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.80×** | +7.0 | 9e-11 | 29/47 (CFPAC-1, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.33×** | +6.5 | 3e-09 | 22/47 (SW480, PANC-1, …) | two highest doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | 1.20× | +5.9 | 2e-07 | 18/47 (J82, SNU-423, …) | top dose only | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | 1.20× | +4.0 | 0.002 | 14/48 (A-427, SW480, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.19× | +4.0 | 0.002 | 18/47 (C32, AsPC-1, …) | top dose only |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | 1.14× | +3.0 | 0.082 | 1/47 (LS 180) | two highest doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.14× | +3.0 | 0.082 | 8/47 (SW480, A-172, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6191.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.579×** | -12.6 | 1e-33 | 37/46 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.569×** | -12.0 | 8e-31 | 28/39 (LoVo, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.397×** | -11.1 | 2e-26 | 37/48 (LoVo, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.620×** | -11.0 | 5e-26 | 33/47 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.622×** | -10.9 | 8e-26 | 27/45 (LS 180, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.618×** | -10.7 | 1e-24 | 28/38 (LS 180, HCT15, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.631×** | -10.6 | 2e-24 | 28/47 (SW480, C32, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.668×** | -9.3 | 1e-18 | 29/47 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **0.764×** | -8.8 | 1e-16 | 26/46 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.697×** | -8.3 | 5e-15 | 27/46 (A-427, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.708×** | -8.0 | 9e-14 | 32/47 (LS 180, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.728×** | -7.3 | 1e-11 | 28/47 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.744×** | -6.5 | 3e-09 | 26/47 (KATO III, LS 180, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.755×** | -6.5 | 4e-09 | 21/47 (LS 180, NCI-H460, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.597×** | -6.2 | 2e-08 | 23/47 (RKO, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.759×** | -5.9 | 2e-07 | 21/46 (CHP-212, NCI-H460, …) | all doses, flat | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.831×** | -4.3 | 7e-04 | 19/47 (LS 180, KATO III, …) | two highest doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.870× | -3.2 | 0.035 | 9/46 (C32, LS 180, …) | all doses, flat |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.829×** | -3.1 | 0.052 | 11/47 (LS 180, SW480, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Sulfatinib (drug)]] 5 µM |  | 0.875× | -3.0 | 0.076 | 8/48 (AN3 CA, NCI-H2347, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.883× | -2.9 | 0.096 | 14/47 (LS 180, C32, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6191. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 234 | 0 | 14 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.109× (z -25.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.366× (z -12.1) |
| [[LoVo (line)]] | wt | 70.9 | 4 | 7 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.96× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.181× (z -18.7) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.113× (z -12.5) |
| [[PANC-1 (line)]] | alt | 35.9 | 4 | 7 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.39× (z +15.6) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.261× (z -14.3) |
| [[SW480 (line)]] | alt | 48.6 | 6 | 5 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 3.10× (z +16.5) | [[Auranofin (drug)]] 5 µM 0.380× (z -14.0) |
| [[KATO III (line)]] | alt | 84.5 | 3 | 6 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.75× (z +10.2) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.319× (z -11.6) |
| [[HT-29 (line)]] | alt | 98.5 | 4 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.01× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.259× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.401× (z -9.2) |
| [[SW1417 (line)]] | alt | 98.3 | 5 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.77× (z +12.2) | [[Dinaciclib (drug)]] 0.05 µM 0.275× (z -14.4) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 42.5 | 3 | 4 (3 ⚠) | [[Panobinostat (drug)]] 0.5 µM 5.21× (z +16.8) | [[Dinaciclib (drug)]] 5 µM 0.246× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.204× (z -8.5) |
| [[A-172 (line)]] | wt | 13.4 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 8.83× (z +14.7) | — |
| [[A498 (line)]] | wt | 16.6 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 7.46× (z +16.6) | — |
| [[CFPAC-1 (line)]] | alt | 40.2 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.64× (z +16.0) | — |
| [[COLO 205 (line)]] | alt | 160 | 0 | 5 (1 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.120× (z -10.3) |
| [[HEC-1-A (line)]] | alt | 33.5 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 4.48× (z +14.7) | — |
| [[J82 (line)]] | alt | 27.2 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.87× (z +15.6) | — |
| [[NCI-H460 (line)]] | wt | 145 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.153× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.243× (z -10.6) |
| [[RKO (line)]] | wt | 27.7 | 4 | 1 | [[Panobinostat (drug)]] 0.5 µM 4.27× (z +10.1) | [[PH-797804 (drug)]] 5 µM 0.0892× (z -8.8) |
| [[SK-MEL-2 (line)]] | alt | 49.9 | 1 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.91× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.102× (z -18.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.274× (z -10.4) |
| [[A549 (line)]] | wt | 47.5 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.37× (z +15.2) | — |
| [[C-33 A (line)]] | alt | 51.4 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.37× (z +9.0) | [[Dinaciclib (drug)]] 0.05 µM 0.204× (z -10.9) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 41.0 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.60× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.206× (z -10.9) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 38.7 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.47× (z +14.1) | [[Homoharringtonine (drug)]] 5 µM 0.527× (z -8.5) ⚠ cell-cycle shift, explains ~82% of this change |
| [[NCI-H1573 (line)]] | alt | 20.7 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 5.60× (z +12.8) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.248× (z -10.4) |
| [[NCI-H1792 (line)]] | alt | 42.4 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.64× (z +13.0) | [[Dinaciclib (drug)]] 5 µM 0.344× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 35.9 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.96× (z +13.0) | — |
| [[RPMI-7951 (line)]] | alt | 31.0 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.13× (z +10.5) | [[AZD2858 (drug)]] 5 µM 0.0564× (z -9.6) ⚠ toxic |
| [[A-427 (line)]] | wt | 26.3 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.06× (z +8.9) | [[Homoharringtonine (drug)]] 0.5 µM 0.201× (z -12.7) ⚠ cell-cycle shift, explains ~39% of this change |
| [[AsPC-1 (line)]] | alt | 35.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.33× (z +12.7) | — |
| [[BT-474 (line)]] | alt | 21.7 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 8.29× (z +13.0) | — |
| [[HS-578T (line)]] | alt | 16.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.86× (z +11.4) | — |
| [[hTERT-HPNE (line)]] | wt | 29.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.96× (z +11.1) | — |
| [[LOX-IMVI (line)]] | wt | 27.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.87× (z +13.3) | — |
| [[Panc 03.27 (line)]] | alt | 48.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.78× (z +11.5) | — |
| [[SHP-77 (line)]] | alt | 68.9 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.83× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.328× (z -9.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 25.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.74× (z +11.8) | — |
| [[C32 (line)]] | wt | 73.3 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.300× (z -10.6) |
| [[HCT15 (line)]] | alt | 60.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.124× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Belzutifan (drug)]] 5 µM 0.0924× (z -9.4) |
| [[Hs 766T (line)]] | wt | 14.7 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.62× (z +9.2) | — |
| [[NCI-H23 (line)]] | alt | 24.2 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.34× (z +9.8) | — |
| [[SNU-423 (line)]] | alt | 22.8 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.29× (z +10.8) | — |
| [[SNU-1 (line)]] | wt | 24.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.159× (z -9.0) ⚠ cell-cycle shift, explains ~39% of this change |
| [[SW 1271 (line)]] | alt | 52.9 | 0 | 1 (1 ⚠) | — | [[Allantoin (drug)]] 0.05 µM 0.0885× (z -8.6) ⚠ transcription drop |
| [[AN3 CA (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 35.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 36.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.9 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 60.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 56.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 64.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6191), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*50 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP8A1]] | +0.57 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[DLG3]] | +0.57 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[CDC42SE2]] | +0.57 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[USP3]] | +0.56 | +0.52 / +0.39 | both halves | 6e-05 |  |
| [[NXPH4]] | +0.56 | +0.33 / +0.51 | both halves | 1e-04 |  |
| [[POMGNT2]] | +0.54 | +0.35 / +0.49 | both halves | 1e-04 |  |
| [[UNC5B]] | +0.54 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[FAM102B]] | +0.54 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[SCML2]] | +0.53 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[PPP1R2]] | +0.53 | +0.40 / +0.43 | both halves | 5e-05 |  |
| [[CPOX]] | +0.53 | +0.38 / +0.50 | both halves | 7e-05 |  |
| [[GRB2]] | +0.53 | +0.38 / +0.46 | both halves | 6e-05 |  |

## Genes that move opposite

*50 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKLE2]] | -0.62 | -0.40 / -0.62 | both halves | 5e-05 |  |
| [[GTF2H1]] | -0.60 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[METTL6]] | -0.57 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[C11orf58]] | -0.56 | -0.39 / -0.47 | both halves | 6e-05 |  |
| [[ARRDC3-AS1]] | -0.56 | -0.43 / -0.34 | both halves | 1e-04 |  |
| [[MCPH1]] | -0.55 | -0.36 / -0.54 | both halves | 1e-04 |  |
| [[ZNF764]] | -0.55 | -0.43 / -0.39 | both halves | 5e-05 |  |
| [[TRMT13]] | -0.55 | -0.42 / -0.38 | both halves | 6e-05 |  |
| [[GGPS1]] | -0.55 | -0.47 / -0.38 | both halves | 6e-05 |  |
| [[PCNX4-DT]] | -0.53 | -0.36 / -0.34 | both halves | 1e-04 |  |
| [[C1S]] | -0.53 | -0.50 / -0.36 | both halves | 1e-04 |  |
| [[AKT1S1]] | -0.53 | -0.34 / -0.42 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 088]]; 51 genes; this gene is in the **-** arm (projection on the module's main direction -0.584). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.46).
- **Nodal map** (x, y) = (0.0, 8.7); signed map (-19.7, 19.6). **Vector** length 89.1, 21.8% of its response variance represented; |z| ≥ 3 in 1,423 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.8 | +19.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.7 | +10.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.3 | +17.2 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.9 | +28.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.7 | +29.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.1 | +7.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.0 | +7.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.0 | +11.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.9 | +1.7 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -6.9 | -8.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | -6.2 | -8.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.4 | -10.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.0 | -12.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.6 | -6.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.4 | -0.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.4 | -6.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.9 | +1.4 |

## What is on record

|  |  |
|---|---|
| Name | glucuronic acid epimerase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q23 — chr15:69,160,584-69,272,217 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0836, HSEPI |
| Hallmark sets | GLYCOLYSIS |
| Reactome | 4 pathways, smallest: HS-GAG biosynthesis; Heparan sulfate/heparin (HS-GAG) metabolism; Glycosaminoglycan metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [O94923](https://www.uniprot.org/uniprotkb/O94923) (D-glucuronyl C5-epimerase):

> Converts D-glucuronic acid residues adjacent to N-sulfate sugar residues to L-iduronic acid residues, both in maturing heparan sulfate (HS) and heparin chains. This is important for further modifications that determine the specificity of interactions between these glycosaminoglycans and proteins.

**Summary**, from NCBI Gene [26035](https://www.ncbi.nlm.nih.gov/gene/26035):

> Enables calcium ion binding activity; heparosan-N-sulfate-glucuronate 5-epimerase activity; and protein homodimerization activity. Involved in heparan sulfate proteoglycan biosynthetic process. Predicted to be located in Golgi membrane. Predicted to be active in Golgi apparatus. Implicated in cerebrovascular disease and hypertension. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17855](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17855) · Entrez [26035](https://www.ncbi.nlm.nih.gov/gene/26035) · UniProt [O94923](https://www.uniprot.org/uniprotkb/O94923) · Ensembl [ENSG00000138604](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138604)

## Data

Gene col 6191: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6191); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6191, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6191]; `tensor/DDL_lfc|DDL_z.npy` [6191]; `embed/gene_vectors.npy` [6191]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6191 or target_col == 6191). Every well: [[GLCE — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GLCE.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
