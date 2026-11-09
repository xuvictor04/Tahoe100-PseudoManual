---
symbol: "SART3"
type: "gene"
col: 1134
ensembl_id: "ENSG00000075856"
name: "spliceosome associated factor 3, U4/U6 recycling protein"
location: "12q23.3"
module: 7
arm: "+"
pooled_cpm: 65.76
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 6
n_dd_up_clean: 18
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# SART3

*spliceosome associated factor 3, U4/U6 recycling protein* — 12q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.29× (z +26.2, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.493× (z -15.8, q 0e+00, down in 45 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.777× (z -8.0, q 2e-13, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC4A1AP]] (+0.73, fdr 7e-06), [[SNW1]] (+0.73, fdr 7e-06), [[C1orf131]] (+0.71, fdr 7e-06); moves opposite to [[C12orf75]] (-0.63, fdr 1e-05), [[DIAPH1]] (-0.60, fdr 2e-05), [[TWSG1]] (-0.60, fdr 2e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1134.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.29×** | +26.2 | 0e+00 | 46/48 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **6.44×** | +21.8 | 0e+00 | 48/49 (SW480, LoVo, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **4.65×** | +17.9 | 0e+00 | 46/48 (SW480, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.97×** | +15.1 | 0e+00 | 45/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.01×** | +15.0 | 0e+00 | 46/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.88×** | +14.1 | 5e-43 | 45/48 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.78×** | +12.9 | 3e-36 | 43/48 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.79×** | +12.2 | 1e-32 | 45/48 (PANC-1, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.61×** | +10.7 | 9e-25 | 43/48 (PANC-1, HT-29, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.58×** | +10.2 | 2e-22 | 41/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.47×** | +8.7 | 3e-16 | 38/48 (NCI-H1573, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.43×** | +8.0 | 5e-14 | 37/48 (NCI-H1573, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.41×** | +7.7 | 5e-13 | 33/48 (NCI-H1573, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.39×** | +7.3 | 9e-12 | 30/48 (LoVo, SW480, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.82×** | +7.0 | 1e-10 | 21/36 (NCI-H1573, SW480, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.35×** | +6.7 | 6e-10 | 33/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.37×** | +5.0 | 1e-05 | 27/49 (PANC-1, HOP62, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1134.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.493×** | -15.8 | 0e+00 | 45/49 (RKO, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.497×** | -15.0 | 0e+00 | 42/44 (LS 180, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.645×** | -9.1 | 2e-17 | 31/45 (C32, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.777×** | -8.0 | 2e-13 | 32/48 (SW1417, SW480, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.803×** | -4.9 | 1e-04 | 27/49 (C32, SW480, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.815×** | -4.6 | 4e-04 | 21/48 (RKO, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.836× | -4.0 | 0.005 | 19/48 (A498, SW1417, …) | all doses, flat | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.859× | -3.3 | 0.076 | 16/48 (RKO, LOX-IMVI, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.871× | -3.1 | 0.12 | 13/48 (A498, SW1417, …) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1134. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 66.0 | 9 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.77× (z +26.0) | [[Dinaciclib (drug)]] 5 µM 0.266× (z -17.8) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 63.9 | 9 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +19.8) | [[Dinaciclib (drug)]] 5 µM 0.101× (z -24.9) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 63.1 | 9 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +20.2) | [[Dinaciclib (drug)]] 0.5 µM 0.346× (z -13.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 50.1 | 7 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +13.1) | [[Dinaciclib (drug)]] 0.5 µM 0.419× (z -9.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 70.7 | 9 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 9.51× (z +15.3) | — |
| [[SW480 (line)]] | alt | 71.3 | 7 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 9.37× (z +17.8) | [[Dinaciclib (drug)]] 5 µM 0.451× (z -11.8) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 66.8 | 4 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +13.3) | [[Dinaciclib (drug)]] 0.5 µM 0.332× (z -15.4) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 65.9 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +23.2) | [[Dinaciclib (drug)]] 5 µM 0.397× (z -12.5) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 59.8 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.64× (z +23.0) | [[Dinaciclib (drug)]] 5 µM 0.408× (z -9.1) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 56.9 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.383× (z -9.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 75.4 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +17.2) | — |
| [[NCI-H2030 (line)]] | alt | 65.7 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +13.5) | [[Dinaciclib (drug)]] 0.5 µM 0.379× (z -10.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 63.3 | 4 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.17× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.251× (z -15.1) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 72.1 | 3 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 8.85× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.0398× (z -27.3) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 73.1 | 4 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.49× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.463× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 58.3 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +17.0) | [[Dinaciclib (drug)]] 5 µM 0.277× (z -11.7) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 86.9 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +14.0) | [[Dinaciclib (drug)]] 0.5 µM 0.114× (z -24.7) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 85.6 | 4 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.99× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.449× (z -10.4) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 85.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +19.4) | — |
| [[HS-578T (line)]] | alt | 43.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.29× (z +19.6) | — |
| [[J82 (line)]] | alt | 65.1 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +14.7) | [[Dinaciclib (drug)]] 5 µM 0.427× (z -9.9) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 67.0 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.84× (z +10.6) | [[Dinaciclib (drug)]] 0.5 µM 0.377× (z -10.4) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 47.1 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +11.8) | [[Dinaciclib (drug)]] 0.5 µM 0.0993× (z -20.3) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 74.3 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 8.37× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.184× (z -13.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 44.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +16.1) | — |
| [[A-427 (line)]] | wt | 75.5 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.41× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.328× (z -13.0) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 55.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +10.4) | — |
| [[C32 (line)]] | wt | 60.2 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.221× (z -11.3) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 53.6 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +13.4) | [[Dinaciclib (drug)]] 0.5 µM 0.424× (z -10.0) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 70.7 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 9.68× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.111× (z -20.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 105 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +14.0) | — |
| [[RPMI-7951 (line)]] | alt | 63.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +14.3) | — |
| [[SW48 (line)]] | wt | 75.8 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 4.17× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.301× (z -9.4) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 65.8 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.51× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.182× (z -14.2) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 43.7 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 8.67× (z +10.6) | — |
| [[hTERT-HPNE (line)]] | wt | 48.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +15.0) | [[Dinaciclib (drug)]] 5 µM 0.242× (z -10.6) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 49.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +10.8) | — |
| [[SNU-423 (line)]] | alt | 56.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +15.3) | [[Dinaciclib (drug)]] 5 µM 0.392× (z -8.6) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 83.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.105× (z -14.2) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 72.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.123× (z -11.6) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 61.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +11.1) | — |
| [[HepG2_C3A (line)]] | wt | 74.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +9.9) | — |
| [[NCI-H661 (line)]] | alt | 82.0 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.121× (z -9.9) |
| [[SHP-77 (line)]] | alt | 80.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.392× (z -9.6) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 81.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 66.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 66.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 58.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 79.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 81.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1134), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC4A1AP]] | +0.73 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[SNW1]] | +0.73 | +0.67 / +0.67 | both halves | 7e-06 | STRING 400 |
| [[C1orf131]] | +0.71 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[TACO1]] | +0.71 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[KEAP1]] | +0.70 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[CCDC174]] | +0.69 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[ZNF830]] | +0.69 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[PHAX]] | +0.69 | +0.67 / +0.65 | both halves | 7e-06 | STRING 409 |
| [[MRM3]] | +0.69 | +0.50 / +0.68 | both halves | 1e-05 |  |
| [[PAAF1]] | +0.69 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[WAPL]] | +0.68 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[ABRAXAS2]] | +0.68 | +0.63 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C12orf75]] | -0.63 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[DIAPH1]] | -0.60 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[TWSG1]] | -0.60 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[MAPK1]] | -0.58 | -0.59 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises SART3's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[PRKACA]] | C | PRKACA's natural level weakens SART3's drug response | PRKACA's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.72, reverse -0.28; direction not clear | 0.005 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[SESTD1]] | C | SESTD1 activity lowers SART3's level | lines that do not express SESTD1 (4) vs lines expressing it (46) | 1.31× higher at baseline in the lines without SESTD1 | 0.078 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SCML1, LHFPL2, TBXAS1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.713). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-38.5, 8.4); signed map (-5.2, -18.5). **Vector** length 87.7, 24.5% of its response variance represented; |z| ≥ 3 in 1,324 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.7 | +14.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.5 | +3.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.3 | +12.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.2 | +26.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.9 | +15.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.8 | +3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.6 | +7.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.5 | +6.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.5 | +10.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.6 | -0.7 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -5.4 | +7.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.9 | +12.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.3 | -4.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.2 | +8.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.1 | -8.0 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -2.4 | -1.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.4 | -2.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.0 | -0.7 |
|  | [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | -1.8 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | spliceosome associated factor 3, U4/U6 recycling protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q23.3 — chr12:108,522,214-108,561,400 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0156, RP11-13G14, TIP110, p110 |
| Gene groups (HGNC) | RNA binding motif containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15020](https://www.uniprot.org/uniprotkb/Q15020) (Spliceosome associated factor 3, U4/U6 recycling protein):

> U6 snRNP-binding protein that functions as a recycling factor of the splicing machinery. Promotes the initial reassembly of U4 and U6 snRNPs following their ejection from the spliceosome during its maturation. Also binds U6atac snRNPs and may function as a recycling factor for U4atac/U6atac spliceosomal snRNP, an initial step in the assembly of U12-type spliceosomal complex. The U12-type spliceosomal complex plays a role in the splicing of introns with non-canonical splice sites. May also …

**Summary**, from NCBI Gene [9733](https://www.ncbi.nlm.nih.gov/gene/9733):

> The protein encoded by this gene is an RNA-binding nuclear protein that is a tumor-rejection antigen. This antigen possesses tumor epitopes capable of inducing HLA-A24-restricted and tumor-specific cytotoxic T lymphocytes in cancer patients and may be useful for specific immunotherapy. This gene product is found to be an important cellular factor for HIV-1 gene expression and viral replication. It also associates transiently with U6 and U4/U6 snRNPs during the recycling phase of the spliceosome …

**Accessions** — [HGNC:16860](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16860) · Entrez [9733](https://www.ncbi.nlm.nih.gov/gene/9733) · UniProt [Q15020](https://www.uniprot.org/uniprotkb/Q15020) · Ensembl [ENSG00000075856](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000075856)

## Data

Gene col 1134: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1134); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1134, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1134]; `tensor/DDL_lfc|DDL_z.npy` [1134]; `embed/gene_vectors.npy` [1134]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1134 or target_col == 1134). Every well: [[SART3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SART3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
