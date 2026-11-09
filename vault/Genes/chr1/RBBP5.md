---
symbol: "RBBP5"
type: "gene"
col: 3884
ensembl_id: "ENSG00000117222"
name: "RB binding protein 5, histone lysine methyltransferase complex subunit"
location: "1q32.1"
module: 41
arm: "+"
pooled_cpm: 59.91
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 3
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# RBBP5

*RB binding protein 5, histone lysine methyltransferase complex subunit* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.12× (z +21.6, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.546× (z -11.1, q 9e-26, down in 33 of 42 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (Panc 03.27 0.0727×, LS 180 0.0661×, NCI-H460 0.184×, NCI-H2347 0.330×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 5 lines (NCI-H23 0.106×, NCI-H2347 0.261×, NCI-H1573 0.319×, HT-29 0.313×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H1573 0.203×, NCI-H2347 0.370×, NCI-H460 0.417×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SUGP1]] (+0.75, fdr 7e-06), [[MTF1]] (+0.65, fdr 1e-05), [[INTS4]] (+0.64, fdr 1e-05); moves opposite to [[SLC39A10]] (-0.56, fdr 3e-04), [[GNG12]] (-0.55, fdr 2e-05), [[UBQLN4]] (-0.54, fdr 1e-04).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3884.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.12×** | +21.6 | 0e+00 | 48/48 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.86×** | +19.9 | 0e+00 | 48/48 (SK-MEL-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.08×** | +19.6 | 0e+00 | 46/48 (SK-MEL-2, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.42×** | +16.8 | 0e+00 | 46/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.54×** | +12.5 | 8e-34 | 47/49 (SW480, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.78×** | +10.9 | 8e-26 | 42/48 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.77×** | +10.8 | 2e-25 | 38/48 (C32, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.16× | +9.7 | 2e-20 | 4/49 (Hs 766T, SNU-1, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.59×** | +8.8 | 1e-16 | 42/48 (COLO 205, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.42×** | +8.7 | 1e-16 | 37/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.55×** | +7.9 | 1e-13 | 38/48 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.38×** | +6.1 | 5e-08 | 33/48 (LoVo, BT-474, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.35×** | +5.7 | 5e-07 | 31/47 (SW480, LoVo, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.38×** | +5.7 | 5e-07 | 36/48 (COLO 205, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.32×** | +5.2 | 9e-06 | 29/48 (COLO 205, HOP62, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.31×** | +5.1 | 1e-05 | 28/48 (LoVo, SW480, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.17× | +4.1 | 0.001 | 19/48 (SK-MEL-2, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3884.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (Panc 03.27 0.0727×, LS 180 0.0661×, NCI-H460 0.184×, NCI-H2347 0.330×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 5 lines (NCI-H23 0.106×, NCI-H2347 0.261×, NCI-H1573 0.319×, HT-29 0.313×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H1573 0.203×, NCI-H2347 0.370×, NCI-H460 0.417×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.546×** | -11.1 | 9e-26 | 33/42 (Panc 03.27, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.545×** | -10.7 | 3e-24 | 38/45 (NCI-H23, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.644×** | -8.0 | 2e-13 | 35/49 (NCI-H1573, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Carbamazepine (drug)]] 5 µM |  | 0.840× | -3.4 | 0.11 | 11/47 (SW1417, SW 900, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.844× | -3.3 | 0.13 | 15/49 (LOX-IMVI, HEC-1-A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3884. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 76.3 | 7 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +14.7) | [[Dinaciclib (drug)]] 5 µM 0.184× (z -20.3) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 62.2 | 8 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.38× (z +16.8) | — |
| [[AsPC-1 (line)]] | alt | 56.0 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +13.1) | [[Dinaciclib (drug)]] 0.5 µM 0.305× (z -9.7) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 143 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.79× (z +17.3) | [[Dinaciclib (drug)]] 0.05 µM 0.312× (z -9.9) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 53.2 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +13.0) | [[Dinaciclib (drug)]] 0.5 µM 0.404× (z -9.0) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 84.5 | 3 | 3 (3 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.80× (z +12.6) | [[Dinaciclib (drug)]] 0.05 µM 0.261× (z -15.2) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 62.7 | 4 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.11× (z +10.6) | [[Dinaciclib (drug)]] 0.5 µM 0.494× (z -9.5) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 50.1 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +14.3) | [[Dinaciclib (drug)]] 5 µM 0.351× (z -9.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 48.6 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.79× (z +14.3) | [[Dinaciclib (drug)]] 0.5 µM 0.428× (z -8.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 53.3 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 4.63× (z +16.1) | — |
| [[LS 180 (line)]] | wt | 49.6 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.10× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.0661× (z -21.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 57.5 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +14.0) | — |
| [[NCI-H1573 (line)]] | alt | 63.3 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.203× (z -16.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 63.5 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.47× (z +14.6) | — |
| [[CFPAC-1 (line)]] | alt | 59.3 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +14.1) | [[Dinaciclib (drug)]] 0.5 µM 0.413× (z -8.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 48.3 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.61× (z +12.3) | — |
| [[Hs 766T (line)]] | wt | 47.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +13.2) | — |
| [[HS-578T (line)]] | alt | 42.2 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.72× (z +11.4) | — |
| [[J82 (line)]] | alt | 58.8 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.84× (z +10.3) | — |
| [[NCI-H23 (line)]] | alt | 55.1 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.13× (z +11.8) | [[Dinaciclib (drug)]] 0.05 µM 0.106× (z -21.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 58.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.84× (z +17.9) | — |
| [[A-172 (line)]] | wt | 45.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.84× (z +15.3) | — |
| [[COLO 205 (line)]] | alt | 69.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +12.0) | — |
| [[H4 (line)]] | wt | 41.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.52× (z +9.6) | — |
| [[HT-29 (line)]] | alt | 56.8 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.313× (z -10.4) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 40.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +10.1) | — |
| [[NCI-H1792 (line)]] | alt | 48.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +16.7) | — |
| [[NCI-H2030 (line)]] | alt | 53.8 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.55× (z +9.6) | [[Dinaciclib (drug)]] 0.05 µM 0.362× (z -9.7) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 63.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.01× (z +9.8) | — |
| [[RPMI-7951 (line)]] | alt | 51.5 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.69× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.276× (z -10.2) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 65.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.81× (z +10.5) | — |
| [[SNU-423 (line)]] | alt | 45.4 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.35× (z +11.3) | — |
| [[SW 900 (line)]] | alt | 95.3 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +13.0) | [[Dinaciclib (drug)]] 5 µM 0.349× (z -9.2) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 80.3 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.31× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.339× (z -11.1) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 62.8 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.22× (z +8.5) | [[Dinaciclib (drug)]] 0.05 µM 0.287× (z -8.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 62.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.374× (z -9.3) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 32.3 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.88× (z +10.1) | — |
| [[Panc 03.27 (line)]] | alt | 66.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.0727× (z -23.1) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 57.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.216× (z -11.7) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 53.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.47× (z +9.6) | — |
| [[HepG2_C3A (line)]] | wt | 42.7 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.34× (z +8.8) | — |
| [[SNU-1 (line)]] | wt | 50.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.42× (z +8.5) | — |
| [[AN3 CA (line)]] | alt | 63.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 75.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 53.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 62.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 62.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 83.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 61.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3884), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 5 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SUGP1]] | +0.75 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[MTF1]] | +0.65 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[INTS4]] | +0.64 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[MRPL10]] | +0.64 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[ACBD3]] | +0.64 | +0.46 / +0.45 | both halves | 3e-05 |  |
| [[RPP21]] | +0.63 | +0.43 / +0.48 | both halves | 3e-05 |  |
| [[MRPL55]] | +0.62 | +0.32 / +0.49 | both halves | 2e-04 |  |
| [[SSR2]] | +0.61 | +0.41 / +0.39 | both halves | 6e-05 |  |
| [[CCDC127]] | +0.60 | +0.42 / +0.42 | both halves | 4e-05 |  |
| [[NOSIP]] | +0.60 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[HERPUD1]] | +0.59 | +0.37 / +0.44 | both halves | 7e-05 |  |
| [[KLHL20]] | +0.59 | +0.59 / +0.53 | both halves | 1e-05 | pathway: Neddylation |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC39A10]] | -0.56 | -0.28 / -0.47 | both halves | 3e-04 |  |
| [[GNG12]] | -0.55 | -0.50 / -0.47 | both halves | 2e-05 | pathway: Signaling by WNT |
| [[UBQLN4]] | -0.54 | -0.38 / -0.33 | both halves | 1e-04 |  |
| [[SEPTIN11]] | -0.52 | -0.36 / -0.32 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.559). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-41.7, -9.4); signed map (-16.1, -4.7). **Vector** length 63.3, 14.3% of its response variance represented; |z| ≥ 3 in 1,148 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +3.8 | +19.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.3 | +21.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~56% of this change | +2.7 | +3.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.1 | +2.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +1.9 | +16.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +0.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +4.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.6 | +2.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.5 | -0.9 |
|  | [[Vilanterol (drug)]] 5 µM |  | +1.4 | +1.2 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.8 | -10.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.8 | +0.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.3 | +6.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.1 | -8.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.0 | -11.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.1 | -0.5 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.1 | -0.5 |
|  | [[Cepharanthine (drug)]] 5 µM |  | -1.1 | -0.3 |
|  | [[Adenine (drug)]] 5 µM |  | -1.0 | -1.7 |
|  | [[Rapamycin (drug)]] 5 µM |  | -0.9 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | RB binding protein 5, histone lysine methyltransferase complex subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:205,086,142-205,122,015 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RBQ3, SWD1 |
| Gene groups (HGNC) | WD repeat domain containing; WRAD complex |
| Reactome | 31 pathways, smallest: Loss of Function of KMT2D in Kabuki Syndrome; Loss of Function of KMT2D in MLL4 Complex Formation in Kabuki Syndrome; Disorders of Developmental Biology |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15291](https://www.uniprot.org/uniprotkb/Q15291) (Retinoblastoma-binding protein 5):

> In embryonic stem (ES) cells, plays a crucial role in the differentiation potential, particularly along the neural lineage, regulating gene induction and H3 'Lys-4' methylation at key developmental loci, including that mediated by retinoic acid (By similarity). Does not affect ES cell self-renewal (By similarity). Component or associated component of some histone methyltransferase complexes which regulates transcription through recruitment of those complexes to gene promoters. As part of the …

**Summary**, from NCBI Gene [5929](https://www.ncbi.nlm.nih.gov/gene/5929):

> This gene encodes a ubiquitously expressed nuclear protein which belongs to a highly conserved subfamily of WD-repeat proteins. The encoded protein binds directly to retinoblastoma protein, which regulates cell proliferation. It interacts preferentially with the underphosphorylated retinoblastoma protein via the E1A-binding pocket B. Three alternatively spliced transcript variants that encode different protein isoforms have been described for this gene. [provided by RefSeq, Jul 2010]

**Accessions** — [HGNC:9888](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9888) · Entrez [5929](https://www.ncbi.nlm.nih.gov/gene/5929) · UniProt [Q15291](https://www.uniprot.org/uniprotkb/Q15291) · Ensembl [ENSG00000117222](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117222)

## Data

Gene col 3884: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3884); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3884, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3884]; `tensor/DDL_lfc|DDL_z.npy` [3884]; `embed/gene_vectors.npy` [3884]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3884 or target_col == 3884). Every well: [[RBBP5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RBBP5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
