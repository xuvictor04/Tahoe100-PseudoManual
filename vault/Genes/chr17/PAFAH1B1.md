---
symbol: "PAFAH1B1"
type: "gene"
col: 138
ensembl_id: "ENSG00000007168"
name: "platelet activating factor acetylhydrolase 1b regulatory subunit 1"
location: "17p13.3"
module: 74
arm: "+"
pooled_cpm: 279.86
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 13
n_dd_up_clean: 7
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/074"]
generated_by: "tahoemap"
---

# PAFAH1B1

*platelet activating factor acetylhydrolase 1b regulatory subunit 1* — 17p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.67× (z +15.7, q 0e+00, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.695× (z -15.7, q 0e+00, down in 38 of 49 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNX6]] (+0.61, fdr 1e-05), [[FAM193A]] (+0.58, fdr 1e-05), [[ANKRD12]] (+0.58, fdr 2e-05); moves opposite to [[BEND3]] (-0.53, fdr 3e-05), [[SLC43A1]] (-0.50, fdr 3e-05), [[NOLC1]] (-0.50, fdr 8e-05).
> It is in [[Module 074]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 138.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.67×** | +15.7 | 0e+00 | 42/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.15×** | +12.2 | 6e-32 | 43/49 (SW480, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.44×** | +11.1 | 2e-26 | 38/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.44×** | +11.0 | 4e-26 | 39/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.26×** | +10.0 | 1e-21 | 33/48 (PANC-1, NCI-H460, …) | top dose only | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.80×** | +9.4 | 5e-19 | 39/48 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.31×** | +8.3 | 7e-15 | 35/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.26×** | +7.2 | 6e-11 | 31/48 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.20× | +5.4 | 3e-06 | 23/48 (KATO III, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +4.6 | 2e-04 | 19/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +4.4 | 6e-04 | 20/48 (A498, PANC-1, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.5 µM |  | 1.12× | +3.5 | 0.024 | 6/48 (SHP-77, A-427, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | 1.16× | +3.3 | 0.041 | 13/49 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.12× | +3.2 | 0.053 | 15/47 (LoVo, COLO 205, …) | rises with dose |  |
| [[Tomivosertib (drug)]] 5 µM |  | **1.21×** | +3.0 | 0.088 | 15/48 (NCI-H1573, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 15 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 138.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.695×** | -15.7 | 0e+00 | 38/49 (A549, A-172, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.673×** | -12.1 | 5e-31 | 35/49 (C32, RKO, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.689×** | -10.5 | 1e-23 | 35/45 (A549, C32, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.721×** | -9.6 | 1e-19 | 30/44 (A549, C32, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.732×** | -9.5 | 2e-19 | 35/48 (LOX-IMVI, A498, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.740×** | -9.2 | 3e-18 | 41/48 (LOX-IMVI, A498, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.749×** | -8.8 | 1e-16 | 41/48 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.924× | -8.6 | 5e-16 | 0/50 | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.756×** | -8.5 | 8e-16 | 31/48 (LOX-IMVI, A549, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.751×** | -8.4 | 3e-15 | 40/47 (MIA PaCa-2, A-172, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 0.834× | -7.9 | 2e-13 | 24/48 (SK-MEL-2, NCI-H2347, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.783×** | -7.5 | 4e-12 | 31/48 (C32, LOX-IMVI, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.848× | -7.1 | 5e-11 | 18/48 (A-172, HEC-1-A, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.807×** | -6.5 | 3e-09 | 26/48 (HOP62, MIA PaCa-2, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.813×** | -6.3 | 1e-08 | 27/48 (HOP62, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.05 µM |  | 0.888× | -3.6 | 0.008 | 3/48 (AN3 CA, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.893× | -3.4 | 0.015 | 7/48 (NCI-H460, NCI-H1573, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.818×** | -3.2 | 0.032 | 15/49 (A498, LOX-IMVI, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 0.898× | -3.2 | 0.037 | 12/48 (RKO, SNU-1, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.902× | -3.1 | 0.037 | 3/48 (NCI-H1573, NCI-H1792, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.905× | -3.0 | 0.051 | 10/48 (AN3 CA, CFPAC-1, …) | rises with dose |  |
| [[Aliskiren (drug)]] 0.5 µM |  | 0.911× | -2.8 | 0.096 | 0/49 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 138. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 301 | 1 | 10 (8 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.62× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.559× (z -15.5) |
| [[SW480 (line)]] | alt | 362 | 8 (2 ⚠) | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.69× (z +16.8) | [[Dinaciclib (drug)]] 0.5 µM 0.558× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[NCI-H460 (line)]] | wt | 262 | 6 (3 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +18.8) ⚠ cell-cycle shift, explains ~18% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.10× (z +13.5) | [[Dinaciclib (drug)]] 0.05 µM 0.416× (z -14.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 225 | 9 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.64× (z +24.8) | — |
| [[A549 (line)]] | wt | 398 | 1 (1 ⚠) | 7 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.53× (z +12.1) ⚠ cell-cycle shift, explains ~18% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -31.8) |
| [[C32 (line)]] | wt | 458 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.223× (z -17.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.430× (z -15.1) |
| [[KATO III (line)]] | alt | 315 | 8 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.35× (z +17.1) | — |
| [[NCI-H1573 (line)]] | alt | 221 | 6 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.92× (z +15.2) | [[Dinaciclib (drug)]] 5 µM 0.459× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[A-172 (line)]] | wt | 360 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.394× (z -22.9) |
| [[HepG2_C3A (line)]] | wt | 217 | 5 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.21× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.427× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[LoVo (line)]] | wt | 244 | 7 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.90× (z +21.2) | — |
| [[SNU-1 (line)]] | wt | 329 | 5 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.28× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.414× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.653× (z -8.9) |
| [[LS 180 (line)]] | wt | 265 | 5 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.15× (z +16.1) | [[Dinaciclib (drug)]] 0.05 µM 0.515× (z -8.6) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 242 | 5 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +14.2) ⚠ cell-cycle shift, explains ~18% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.23× (z +12.2) | [[Dinaciclib (drug)]] 0.5 µM 0.391× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[COLO 205 (line)]] | alt | 256 | 5 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.67× (z +14.0) | — |
| [[HEC-1-A (line)]] | alt | 299 | 3 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.05× (z +13.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.526× (z -20.7) |
| [[HT-29 (line)]] | alt | 244 | 3 (1 ⚠) | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.17× (z +12.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.606× (z -14.0) |
| [[MIA PaCa-2 (line)]] | alt | 379 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.383× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.547× (z -10.6) |
| [[NCI-H1792 (line)]] | alt | 294 | 2 | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.97× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.368× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.531× (z -14.8) |
| [[NCI-H2030 (line)]] | alt | 292 | 2 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 2.96× (z +10.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.608× (z -13.1) |
| [[C-33 A (line)]] | alt | 329 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.515× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.636× (z -9.6) |
| [[HOP62 (line)]] | alt | 281 | 1 | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.71× (z +9.3) | [[Auranofin (drug)]] 5 µM 0.543× (z -10.7) |
| [[SW48 (line)]] | wt | 268 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +12.8) ⚠ cell-cycle shift, explains ~18% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.27× (z +12.3) | — |
| [[A498 (line)]] | wt | 273 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 1.58× (z +10.0) ⚠ cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.574× (z -17.3) |
| [[AsPC-1 (line)]] | alt | 295 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.55× (z +10.3) ⚠ cell-cycle shift, explains ~18% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.491× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[HCT15 (line)]] | alt | 308 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.39× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.525× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SNU-423 (line)]] | alt | 269 | 0 | 3 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.490× (z -12.2) ⚠ cell-cycle shift, explains ~65% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.628× (z -11.7) |
| [[SW1417 (line)]] | alt | 214 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.02× (z +12.3) | — |
| [[BT-474 (line)]] | alt | 214 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.552× (z -12.9) |
| [[CFPAC-1 (line)]] | alt | 210 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.588× (z -13.0) |
| [[hTERT-HPNE (line)]] | wt | 264 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.346× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.542× (z -12.1) |
| [[NCI-H23 (line)]] | alt | 390 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 2.37× (z +9.4) | — |
| [[NCI-H2347 (line)]] | alt | 177 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.583× (z -12.6) |
| [[RPMI-7951 (line)]] | alt | 273 | 0 | 2 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.283× (z -10.0) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.637× (z -9.7) |
| [[SK-MEL-2 (line)]] | alt | 156 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.596× (z -11.0) ⚠ cell-cycle shift, explains ~6% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.659× (z -8.8) |
| [[AN3 CA (line)]] | alt | 287 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.593× (z -8.5) |
| [[CHP-212 (line)]] | wt | 314 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.533× (z -9.4) |
| [[Hs 766T (line)]] | wt | 226 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.77× (z +8.9) | — |
| [[J82 (line)]] | alt | 272 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.605× (z -9.1) ⚠ toxic; cell-cycle shift, explains ~29% of this change |
| [[SHP-77 (line)]] | alt | 287 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.70× (z +8.6) | — |
| [[SW 900 (line)]] | alt | 423 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.64× (z +8.5) | — |
| [[A-427 (line)]] | wt | 283 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 182 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 261 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 349 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 284 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 338 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 211 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 298 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 349 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 138), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNX6]] | +0.61 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[FAM193A]] | +0.58 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[ANKRD12]] | +0.58 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[KMT2C]] | +0.57 | +0.48 / +0.66 | both halves | 2e-05 |  |
| [[PPP6R2]] | +0.55 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[HCFC2]] | +0.53 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[RBM5]] | +0.52 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[MRTFA]] | +0.52 | +0.53 / +0.47 | both halves | 2e-05 | pathway: RHO GTPase Effectors |
| [[KLHL4]] | +0.52 | +0.34 / +0.48 | both halves | 1e-04 |  |
| [[UBAP1]] | +0.51 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[MICU2]] | +0.51 | +0.58 / +0.44 | both halves | 3e-05 |  |
| [[SMDT1]] | +0.51 | +0.20 / +0.52 | ⚠ one half (not replicated) | 8e-04 |  |
| [[PRMT2]] | +0.50 | +0.60 / +0.29 | both halves | 2e-04 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BEND3]] | -0.53 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[SLC43A1]] | -0.50 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[NOLC1]] | -0.50 | -0.55 / -0.37 | both halves | 8e-05 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[IVNS1ABP]] | -0.49 | -0.48 / -0.39 | both halves | 5e-05 |  |
| [[AMER1]] | -0.49 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[DPAGT1]] | -0.48 | -0.44 / -0.34 | both halves | 1e-04 |  |
| [[RASSF3]] | -0.48 | -0.42 / -0.32 | both halves | 2e-04 |  |
| [[CRACR2A]] | -0.47 | -0.39 / -0.42 | both halves | 6e-05 |  |
| [[ADAT2]] | -0.47 | -0.40 / -0.43 | both halves | 4e-05 |  |
| [[EBNA1BP2]] | -0.47 | -0.48 / -0.39 | both halves | 6e-05 |  |
| [[CYP27B1]] | -0.47 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[DHX33]] | -0.46 | -0.47 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 074]]; 63 genes; every member is in the + arm (projection on the module's main direction 0.428). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-6.4, -44.2); signed map (-5.9, 10.2). **Vector** length 96.9, 33.4% of its response variance represented; |z| ≥ 3 in 1,397 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +5.3 | -12.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +4.6 | -9.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | +4.2 | +10.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.2 | +0.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +4.2 | -7.5 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +4.1 | +0.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | -1.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.8 | +1.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.7 | +1.2 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | -5.9 | -7.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.5 | -8.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.1 | -1.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.6 | -3.6 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.9 | +2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.8 | -6.5 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -2.7 | -1.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.3 | -2.2 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -2.2 | -0.2 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -2.1 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | platelet activating factor acetylhydrolase 1b regulatory subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.3 — chr17:2,593,183-2,685,615 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LIS1, PAFAH, NudF; previously MDCR, MDS |
| Gene groups (HGNC) | WD repeat domain containing |
| Hallmark sets | G2M_CHECKPOINT, MITOTIC_SPINDLE |
| Reactome | 35 pathways, smallest: COPI-independent Golgi-to-ER retrograde traffic; Loss of Nlp from mitotic centrosomes; Loss of proteins required for interphase microtubule organization from the centrosome |
| Matched by | ensembl_id |

**Function**, from UniProt [P43034](https://www.uniprot.org/uniprotkb/P43034) (Platelet-activating factor acetylhydrolase IB subunit beta):

> Regulatory subunit (beta subunit) of the cytosolic type I platelet-activating factor (PAF) acetylhydrolase (PAF-AH (I)), an enzyme that catalyzes the hydrolyze of the acetyl group at the sn-2 position of PAF and its analogs and participates in PAF inactivation. Regulates the PAF-AH (I) activity in a catalytic dimer composition-dependent manner (By similarity). Required for proper activation of Rho GTPases and actin polymerization at the leading edge of locomoting cerebellar neurons and …

**Summary**, from NCBI Gene [5048](https://www.ncbi.nlm.nih.gov/gene/5048):

> This locus was identified as encoding a gene that when mutated or lost caused the lissencephaly associated with Miller-Dieker lissencephaly syndrome. This gene encodes the non-catalytic alpha subunit of the intracellular Ib isoform of platelet-activating factor acteylhydrolase, a heterotrimeric enzyme that specifically catalyzes the removal of the acetyl group at the SN-2 position of platelet-activating factor (identified as 1-O-alkyl-2-acetyl-sn-glyceryl-3-phosphorylcholine). Two other …

**Accessions** — [HGNC:8574](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8574) · Entrez [5048](https://www.ncbi.nlm.nih.gov/gene/5048) · UniProt [P43034](https://www.uniprot.org/uniprotkb/P43034) · Ensembl [ENSG00000007168](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000007168)

## Data

Gene col 138: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 138); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 138, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 138]; `tensor/DDL_lfc|DDL_z.npy` [138]; `embed/gene_vectors.npy` [138]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 138 or target_col == 138). Every well: [[PAFAH1B1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PAFAH1B1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
