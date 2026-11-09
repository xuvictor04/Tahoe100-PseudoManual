---
symbol: "MARCHF6"
type: "gene"
col: 6999
ensembl_id: "ENSG00000145495"
name: "membrane associated ring-CH-type finger 6"
location: "5p15.2"
module: 45
arm: "+"
pooled_cpm: 325.95
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 17
n_dd_up_clean: 12
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# MARCHF6

*membrane associated ring-CH-type finger 6* — 5p15.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.04× (z +12.1, q 6e-31, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.519× (z -10.7, q 9e-24, down in 41 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.691× (z -8.9, q 2e-16, down in 41 of 49 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNX1]] (+0.70, fdr 1e-05), [[SEC11A]] (+0.64, fdr 3e-05), [[COPS4]] (+0.62, fdr 1e-05); moves opposite to [[NCBP2]] (-0.61, fdr 1e-05), [[TNFRSF12A]] (-0.60, fdr 2e-05), [[UTP3]] (-0.58, fdr 2e-05).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6999.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.04×** | +12.1 | 6e-31 | 48/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.82×** | +10.1 | 1e-21 | 46/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.99×** | +9.7 | 5e-20 | 47/49 (COLO 205, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.71×** | +8.8 | 1e-16 | 47/48 (SW480, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.58×** | +7.7 | 1e-12 | 43/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.49×** | +6.8 | 9e-10 | 41/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.45×** | +6.3 | 3e-08 | 43/48 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +6.1 | 9e-08 | 36/47 (COLO 205, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.35×** | +5.1 | 2e-05 | 30/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.31×** | +4.6 | 3e-04 | 34/48 (PANC-1, KATO III, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.27×** | +3.9 | 0.006 | 32/48 (PANC-1, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.33×** | +3.3 | 0.041 | 32/49 (PANC-1, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Tomivosertib (drug)]] 5 µM |  | **1.44×** | +3.2 | 0.050 | 29/48 (BT-474, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.21×** | +3.2 | 0.050 | 24/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 14 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6999.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.519×** | -10.7 | 9e-24 | 41/44 (NCI-H2347, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.691×** | -8.9 | 2e-16 | 41/49 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.625×** | -8.0 | 3e-13 | 42/49 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.729×** | -5.3 | 1e-05 | 33/48 (HOP62, CFPAC-1, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.730×** | -5.1 | 3e-05 | 39/47 (NCI-H2347, CHP-212, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.818×** | -4.8 | 2e-04 | 26/48 (CFPAC-1, SW480, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.834× | -4.3 | 0.001 | 23/48 (CFPAC-1, PANC-1, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.780×** | -4.2 | 0.002 | 31/48 (HOP62, NCI-H23, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.785×** | -4.1 | 0.002 | 34/48 (PANC-1, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 0.843× | -4.1 | 0.002 | 19/48 (CFPAC-1, NCI-H2347, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.779×** | -3.9 | 0.005 | 26/45 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.801×** | -3.8 | 0.008 | 30/48 (HOP62, CFPAC-1, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.810×** | -3.6 | 0.017 | 25/48 (HT-29, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.813×** | -3.5 | 0.019 | 25/48 (HOP62, SW 900, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.820×** | -3.4 | 0.030 | 27/48 (BT-474, PANC-1, …) | rises with dose |  |
| [[Apalutamide (drug)]] 0.5 µM |  | **0.827×** | -3.2 | 0.043 | 23/48 (NCI-H1573, AsPC-1, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.832×** | -3.1 | 0.057 | 26/48 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[Carbamazepine (drug)]] 5 µM |  | 0.834× | -3.1 | 0.061 | 23/47 (C32, A498, …) | top dose only |  |
| [[Mifepristone (drug)]] 0.5 µM |  | 0.836× | -3.0 | 0.067 | 21/48 (NCI-H1573, NCI-H1792, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 0.841× | -2.9 | 0.083 | 12/48 (NCI-H1573, C32, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6999. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 239 | 11 (4 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.12× (z +19.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.10× (z +19.3) | — |
| [[SW480 (line)]] | alt | 363 | 8 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.17× (z +19.4) | [[Dinaciclib (drug)]] 5 µM 0.524× (z -10.5) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 267 | 7 (2 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.37× (z +13.3) | [[Dinaciclib (drug)]] 5 µM 0.387× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.637× (z -9.9) |
| [[PANC-1 (line)]] | alt | 283 | 8 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.35× (z +20.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.604× (z -12.1) |
| [[LoVo (line)]] | wt | 340 | 7 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.92× (z +16.9) | — |
| [[NCI-H1573 (line)]] | alt | 156 | 7 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.73× (z +18.3) | — |
| [[HOP62 (line)]] | alt | 382 | 0 | 5 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.409× (z -10.6) ⚠ cell-cycle shift, explains ~76% of this change |
| [[SW1417 (line)]] | alt | 347 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.56× (z +13.0) | [[Dinaciclib (drug)]] 5 µM 0.456× (z -10.4) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 395 | 4 | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.12× (z +9.9) | — |
| [[CFPAC-1 (line)]] | alt | 389 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.347× (z -12.5) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 259 | 4 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.60× (z +16.4) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 7.61× (z +14.1) | — |
| [[HEC-1-A (line)]] | alt | 292 | 2 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +10.3) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 3.15× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.504× (z -9.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.644× (z -8.8) |
| [[HT-29 (line)]] | alt | 333 | 3 (1 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 2.36× (z +12.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.34× (z +12.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.645× (z -9.1) |
| [[J82 (line)]] | alt | 373 | 2 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.49× (z +12.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.614× (z -9.3) |
| [[KATO III (line)]] | alt | 184 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.11× (z +15.3) | — |
| [[NCI-H1792 (line)]] | alt | 325 | 2 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.53× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.436× (z -9.6) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 613 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.288× (z -15.4) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 362 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.94× (z +12.3) | — |
| [[HepG2_C3A (line)]] | wt | 224 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.27× (z +9.5) | — |
| [[LOX-IMVI (line)]] | wt | 387 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.384× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.527× (z -9.1) |
| [[SW 900 (line)]] | alt | 404 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.28× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.449× (z -8.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 385 | 1 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 3.92× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.362× (z -13.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 258 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +12.8) ⚠ cell-cycle shift, explains ~24% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.513× (z -11.4) |
| [[AN3 CA (line)]] | alt | 418 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.242× (z -13.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 378 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.380× (z -9.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.560× (z -8.6) |
| [[LS 180 (line)]] | wt | 261 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.83× (z +11.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 330 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 4.40× (z +9.7) | — |
| [[Panc 03.27 (line)]] | alt | 345 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.460× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[RKO (line)]] | wt | 271 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +9.7) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 4.46× (z +9.6) | — |
| [[SW48 (line)]] | wt | 291 | 2 | 0 | [[TAK-901 (drug)]] 0.05 µM 4.00× (z +12.0) | — |
| [[A-172 (line)]] | wt | 268 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.598× (z -8.9) |
| [[A498 (line)]] | wt | 416 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +10.7) ⚠ cell-cycle shift, explains ~24% of this change | — |
| [[C32 (line)]] | wt | 225 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 5.08× (z +8.8) | — |
| [[CHP-212 (line)]] | wt | 400 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.328× (z -9.3) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 312 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.542× (z -9.9) |
| [[Hs 766T (line)]] | wt | 402 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.365× (z -12.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 371 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.97× (z +10.0) | — |
| [[RPMI-7951 (line)]] | alt | 235 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.438× (z -9.5) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 415 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.481× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SNU-1 (line)]] | wt | 240 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.71× (z +9.6) | — |
| [[SW 1088 (line)]] | alt | 429 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.177× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[C-33 A (line)]] | alt | 258 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 328 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 256 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 346 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 360 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 432 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 280 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 335 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6999), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNX1]] | +0.70 | +0.77 / +0.54 | both halves | 1e-05 |  |
| [[SEC11A]] | +0.64 | +0.74 / +0.44 | both halves | 3e-05 |  |
| [[COPS4]] | +0.62 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[H3-3A]] | +0.62 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[FOXJ3]] | +0.62 | +0.73 / +0.52 | both halves | 1e-05 |  |
| [[TFG]] | +0.62 | +0.78 / +0.50 | both halves | 1e-05 | pathway: Asparagine N-linked glycosylation |
| [[ORC4]] | +0.61 | +0.65 / +0.40 | both halves | 5e-05 |  |
| [[ELP2]] | +0.60 | +0.71 / +0.36 | both halves | 9e-05 |  |
| [[TENT2]] | +0.60 | +0.72 / +0.48 | both halves | 2e-05 |  |
| [[KLHDC3]] | +0.60 | +0.70 / +0.42 | both halves | 4e-05 |  |
| [[AUH]] | +0.60 | +0.67 / +0.48 | both halves | 2e-05 |  |
| [[HBS1L]] | +0.59 | +0.63 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCBP2]] | -0.61 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[TNFRSF12A]] | -0.60 | -0.62 / -0.47 | both halves | 2e-05 |  |
| [[UTP3]] | -0.58 | -0.68 / -0.48 | both halves | 2e-05 |  |
| [[LIG4]] | -0.58 | -0.70 / -0.28 | both halves | 3e-04 |  |
| [[ZNF562]] | -0.56 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[MED1]] | -0.56 | -0.68 / -0.41 | both halves | 4e-05 |  |
| [[ZBTB38]] | -0.55 | -0.60 / -0.36 | both halves | 1e-04 |  |
| [[OSTM1]] | -0.55 | -0.66 / -0.33 | both halves | 1e-04 |  |
| [[DNTTIP2]] | -0.55 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[ERCC6L2]] | -0.55 | -0.76 / -0.25 | both halves | 4e-04 |  |
| [[ERCC4]] | -0.54 | -0.72 / -0.43 | both halves | 3e-05 |  |
| [[ZNF468]] | -0.53 | -0.57 / -0.49 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.627). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-3.6, -14.1); signed map (-33.8, -9.8). **Vector** length 78.7, 33.2% of its response variance represented; |z| ≥ 3 in 1,321 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +4.7 | -8.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | -10.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | +4.3 | -3.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +3.7 | +6.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | +3.3 | -3.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.8 | +2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | -0.2 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.2 | -0.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | -2.7 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.8 | +1.0 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -7.4 | -3.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.1 | -3.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.2 | -1.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.2 | -4.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.5 | +7.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.5 | -1.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.0 | -1.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.0 | -1.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.7 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | membrane associated ring-CH-type finger 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p15.2 — chr5:10,353,695-10,440,388 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TEB4, MARCH-VI, RNF176; previously MARCH6 |
| Gene groups (HGNC) | Ring finger proteins; Membrane associated ring-CH-type fingers |
| Hallmark sets | XENOBIOTIC_METABOLISM |
| Reactome | 4 pathways, smallest: ER Quality Control Compartment (ERQC); Calnexin/calreticulin cycle; N-glycan trimming in the ER and Calnexin/Calreticulin cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [O60337](https://www.uniprot.org/uniprotkb/O60337) (E3 ubiquitin-protein ligase MARCHF6):

> Endoplasmic reticulum membrane-associated E3 ubiquitin ligase that plays a critical role in mitigating endoplasmic reticulum stress, the regulation of cholesterol and lipid homeostasis, and ferroptosis. Acts as a pivotal component of both the Ac/N-degron pathway (targeting the N-terminal acetyl group of substrates) and the ER-associated protein degradation-cytosol (ERAD-C) pathway (targeting misfolded substrates). For instance, mediates the degradation of Ac/N-degron-bearing proteins such as …

**Summary**, from NCBI Gene [10299](https://www.ncbi.nlm.nih.gov/gene/10299):

> This gene encodes a member of a family of membrane-associated E3 ubiquitin ligases containing RING-CH-type zinc finger motifs. Ubiquitination of type II deiodinase by the encoded protein is an important regulatory step in thyroid hormone signalling. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Jul 2012]

**Accessions** — [HGNC:30550](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30550) · Entrez [10299](https://www.ncbi.nlm.nih.gov/gene/10299) · UniProt [O60337](https://www.uniprot.org/uniprotkb/O60337) · Ensembl [ENSG00000145495](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145495)

## Data

Gene col 6999: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6999); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6999, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6999]; `tensor/DDL_lfc|DDL_z.npy` [6999]; `embed/gene_vectors.npy` [6999]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6999 or target_col == 6999). Every well: [[MARCHF6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MARCHF6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
