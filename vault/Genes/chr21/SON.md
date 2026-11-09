---
symbol: "SON"
type: "gene"
col: 8220
ensembl_id: "ENSG00000159140"
name: "SON DNA and RNA binding protein"
location: "21q22.11"
module: 95
arm: "+"
pooled_cpm: 299.1
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 6
n_dd_up_clean: 16
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/095"]
generated_by: "tahoemap"
---

# SON

*SON DNA and RNA binding protein* — 21q22.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.84× (z +30.4, q 0e+00, up in 48 of 48 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.73× (z +22.1, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.696× (z -8.0, q 8e-13, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RBBP6]] (+0.80, fdr 7e-06), [[MED1]] (+0.78, fdr 7e-06), [[ZNF24]] (+0.75, fdr 7e-06); moves opposite to [[GCSH]] (-0.70, fdr 7e-06), [[STX7]] (-0.68, fdr 1e-05), [[FAR1]] (-0.67, fdr 1e-05).
> It sits in the **+** arm of [[Module 095]] (Chromatin organization).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8220.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.84×** | +30.4 | 0e+00 | 48/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.73×** | +22.1 | 0e+00 | 48/48 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.73×** | +22.1 | 0e+00 | 48/48 (NCI-H460, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.69×** | +20.9 | 0e+00 | 48/48 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.15×** | +16.9 | 0e+00 | 48/48 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.06×** | +15.9 | 0e+00 | 48/48 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.87×** | +13.7 | 5e-41 | 48/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.22×** | +13.4 | 3e-39 | 49/49 (LoVo, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.79×** | +12.8 | 7e-36 | 48/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.62×** | +10.6 | 1e-24 | 44/48 (C32, LoVo, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.51×** | +9.0 | 1e-17 | 40/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.12×** | +8.7 | 2e-16 | 45/48 (LS 180, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +6.6 | 2e-09 | 29/49 (AsPC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +6.0 | 1e-07 | 32/48 (SW1417, NCI-H2347, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.29×** | +5.6 | 6e-07 | 37/48 (HT-29, HEC-1-A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.29×** | +5.5 | 1e-06 | 34/48 (NCI-H2347, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.27×** | +4.8 | 4e-05 | 33/47 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8220.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.696×** | -8.0 | 8e-13 | 44/48 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.733×** | -6.8 | 2e-09 | 39/48 (NCI-H1573, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.756×** | -6.2 | 1e-07 | 36/48 (NCI-H1573, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.757×** | -6.1 | 1e-07 | 34/48 (NCI-H1573, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.807×** | -4.7 | 2e-04 | 28/48 (KATO III, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.664×** | -4.7 | 2e-04 | 43/49 (PANC-1, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.857× | -4.4 | 8e-04 | 12/48 (LOX-IMVI, MIA PaCa-2, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.840× | -3.9 | 0.008 | 23/48 (hTERT-HPNE, NCI-H2030, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.851× | -3.6 | 0.021 | 21/48 (NCI-H2030, NCI-H23, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 0.854× | -3.5 | 0.027 | 18/49 (LOX-IMVI, A498, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8220. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 201 | 16 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.19× (z +30.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 5.00× (z +25.8) | — |
| [[LOX-IMVI (line)]] | wt | 350 | 12 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +28.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.45× (z +20.5) | [[Panobinostat (drug)]] 5 µM 0.537× (z -10.3) |
| [[HOP62 (line)]] | alt | 319 | 13 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +27.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.37× (z +20.6) | — |
| [[HEC-1-A (line)]] | alt | 375 | 10 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +17.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.50× (z +16.3) | [[Panobinostat (drug)]] 5 µM 0.558× (z -10.4) |
| [[NCI-H1573 (line)]] | alt | 469 | 9 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +26.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.59× (z +20.0) | [[Panobinostat (drug)]] 5 µM 0.435× (z -13.0) |
| [[PANC-1 (line)]] | alt | 249 | 10 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +30.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.49× (z +22.1) | [[Belinostat (drug)]] 5 µM 0.547× (z -10.6) |
| [[SW480 (line)]] | alt | 346 | 12 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.57× (z +20.4) | — |
| [[HS-578T (line)]] | alt | 282 | 11 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +25.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.46× (z +22.7) | — |
| [[LoVo (line)]] | wt | 310 | 11 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +22.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.77× (z +21.1) | — |
| [[LS 180 (line)]] | wt | 282 | 11 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.51× (z +24.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 428 | 11 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.90× (z +18.2) | — |
| [[RKO (line)]] | wt | 396 | 11 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +15.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.76× (z +15.6) | — |
| [[SNU-1 (line)]] | wt | 313 | 11 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +21.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.34× (z +18.6) | — |
| [[SW1417 (line)]] | alt | 329 | 11 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +20.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.47× (z +16.1) | — |
| [[A-172 (line)]] | wt | 391 | 10 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +21.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.88× (z +16.9) | — |
| [[hTERT-HPNE (line)]] | wt | 313 | 10 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +22.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.66× (z +19.7) | — |
| [[NCI-H1792 (line)]] | alt | 202 | 10 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +22.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.66× (z +20.8) | — |
| [[H4 (line)]] | wt | 360 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +21.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.39× (z +17.1) | — |
| [[HT-29 (line)]] | alt | 236 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +19.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.33× (z +13.0) | — |
| [[NCI-H2347 (line)]] | alt | 246 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +25.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.27× (z +20.2) | — |
| [[SW 900 (line)]] | alt | 310 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +16.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.21× (z +16.5) | — |
| [[SW48 (line)]] | wt | 262 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +16.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.74× (z +15.7) | — |
| [[AsPC-1 (line)]] | alt | 227 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +21.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.09× (z +18.6) | — |
| [[C32 (line)]] | wt | 256 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +23.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.84× (z +19.2) | — |
| [[CFPAC-1 (line)]] | alt | 285 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +23.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.86× (z +16.6) | — |
| [[A549 (line)]] | wt | 208 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +26.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.71× (z +19.1) | — |
| [[BT-474 (line)]] | alt | 236 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +15.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.71× (z +13.7) | — |
| [[COLO 205 (line)]] | alt | 325 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.37× (z +27.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 5.38× (z +23.4) | — |
| [[HCT15 (line)]] | alt | 499 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +16.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.75× (z +13.9) | — |
| [[HepG2_C3A (line)]] | wt | 273 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +18.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.52× (z +12.7) | — |
| [[Hs 766T (line)]] | wt | 220 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +18.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.82× (z +14.2) | — |
| [[KATO III (line)]] | alt | 215 | 7 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.32× (z +18.4) | — |
| [[RPMI-7951 (line)]] | alt | 292 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +20.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.50× (z +16.4) | — |
| [[SHP-77 (line)]] | alt | 216 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +11.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.10× (z +11.0) | — |
| [[SK-MEL-2 (line)]] | alt | 272 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +29.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.67× (z +19.3) | — |
| [[SNU-423 (line)]] | alt | 221 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +23.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.13× (z +15.2) | — |
| [[A-427 (line)]] | wt | 290 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +13.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.30× (z +13.2) | [[Dinaciclib (drug)]] 5 µM 0.458× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 411 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +27.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.28× (z +21.0) | — |
| [[NCI-H2030 (line)]] | alt | 309 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +26.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.11× (z +17.9) | — |
| [[Panc 03.27 (line)]] | alt | 308 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +16.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.11× (z +11.6) | — |
| [[AN3 CA (line)]] | alt | 319 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +11.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.61× (z +10.2) | — |
| [[J82 (line)]] | alt | 248 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +15.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 1.98× (z +10.4) | — |
| [[NCI-H23 (line)]] | alt | 318 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +20.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.48× (z +13.0) | — |
| [[CHP-212 (line)]] | wt | 353 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.78× (z +11.0) | — |
| [[C-33 A (line)]] | alt | 302 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +10.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.09× (z +10.0) | — |
| [[NCI-H2122 (line)]] | alt | 314 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 291 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 290 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 354 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 297 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8220), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBBP6]] | +0.80 | +0.78 / +0.69 | both halves | 7e-06 | STRING 872 |
| [[MED1]] | +0.78 | +0.82 / +0.63 | both halves | 7e-06 | STRING 455 |
| [[ZNF24]] | +0.75 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[BPTF]] | +0.73 | +0.77 / +0.69 | both halves | 7e-06 | STRING 403 |
| [[TRIP11]] | +0.73 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[TAF7]] | +0.72 | +0.76 / +0.51 | both halves | 1e-05 |  |
| [[CREBBP]] | +0.70 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[MZF1-AS1]] | +0.70 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[ERCC6L2]] | +0.69 | +0.69 / +0.51 | both halves | 1e-05 |  |
| [[ASH1L]] | +0.69 | +0.63 / +0.56 | both halves | 1e-05 | same gene group; STRING 444 |
| [[CDK12]] | +0.69 | +0.74 / +0.52 | both halves | 1e-05 |  |
| [[CCDC90B-AS1]] | +0.69 | +0.67 / +0.37 | both halves | 8e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GCSH]] | -0.70 | -0.68 / -0.60 | both halves | 7e-06 |  |
| [[STX7]] | -0.68 | -0.62 / -0.49 | both halves | 1e-05 |  |
| [[FAR1]] | -0.67 | -0.66 / -0.56 | both halves | 1e-05 |  |
| [[SERAC1]] | -0.67 | -0.60 / -0.51 | both halves | 1e-05 |  |
| [[HACE1]] | -0.66 | -0.67 / -0.43 | both halves | 3e-05 |  |
| [[LTA4H]] | -0.65 | -0.60 / -0.57 | both halves | 1e-05 |  |
| [[HSPB11]] | -0.65 | -0.64 / -0.47 | both halves | 2e-05 |  |
| [[ABHD12]] | -0.65 | -0.67 / -0.50 | both halves | 1e-05 |  |
| [[GPD1L]] | -0.64 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[WASF3]] | -0.63 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[ELP1]] | -0.63 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[CTC1]] | -0.63 | -0.75 / -0.59 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises SON's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 095]] — Chromatin organization; 48 genes; this gene is in the **+** arm (projection on the module's main direction 0.718). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.36).
- **Nodal map** (x, y) = (-22.3, 11.1); signed map (13.6, -29.2). **Vector** length 130, 54.2% of its response variance represented; |z| ≥ 3 in 1,385 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Chromatin organization* (reactome, mean cos +0.53 to 7); *Activation of HOX genes during differentiation* (reactome, mean cos +0.56 to 4); *Activation of anterior HOX genes in hindbrain development during early embryogenesis* (reactome, mean cos +0.56 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +8.3 | +6.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.0 | +22.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +7.8 | +15.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +7.6 | +9.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.5 | +6.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.8 | +10.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +4.9 | +4.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +4.5 | +2.5 |
| fall | [[Belinostat (drug)]] 5 µM |  | -8.4 | -8.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -6.3 | -4.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.8 | -6.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.7 | -6.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -5.1 | -6.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -4.7 | -4.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.2 | -0.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -3.3 | -0.5 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -3.2 | -1.3 |
|  | [[NVP-BHG712 (drug)]] 0.05 µM |  | -3.1 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | SON DNA and RNA binding protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.11 — chr21:33,543,038-33,577,481 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DBP-5, NREBP, KIAA1019, BASS1, FLJ21099, FLJ33914; previously C21orf50 |
| Gene groups (HGNC) | G-patch domain containing; Minor histocompatibility antigens; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [P18583](https://www.uniprot.org/uniprotkb/P18583) (Protein SON):

> RNA-binding protein that acts as a mRNA splicing cofactor by promoting efficient splicing of transcripts that possess weak splice sites. Specifically promotes splicing of many cell-cycle and DNA-repair transcripts that possess weak splice sites, such as TUBG1, KATNB1, TUBGCP2, AURKB, PCNT, AKT1, RAD23A, and FANCG. Probably acts by facilitating the interaction between Serine/arginine-rich proteins such as SRSF2 and the RNA polymerase II. Also binds to DNA; binds to the consensus DNA sequence: …

**Summary**, from NCBI Gene [6651](https://www.ncbi.nlm.nih.gov/gene/6651):

> This gene encodes a protein that contains multiple simple repeats. The encoded protein binds RNA and promotes pre-mRNA splicing, particularly of transcripts with poor splice sites. The protein also recognizes a specific DNA sequence found in the human hepatitis B virus (HBV) and represses HBV core promoter activity. There is a pseudogene for this gene on chromosome 1. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2013]

**Accessions** — [HGNC:11183](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11183) · Entrez [6651](https://www.ncbi.nlm.nih.gov/gene/6651) · UniProt [P18583](https://www.uniprot.org/uniprotkb/P18583) · Ensembl [ENSG00000159140](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159140)

## Data

Gene col 8220: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8220); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8220, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8220]; `tensor/DDL_lfc|DDL_z.npy` [8220]; `embed/gene_vectors.npy` [8220]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8220 or target_col == 8220). Every well: [[SON — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SON.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
