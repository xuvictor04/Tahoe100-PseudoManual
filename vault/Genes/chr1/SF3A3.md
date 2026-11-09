---
symbol: "SF3A3"
type: "gene"
col: 11402
ensembl_id: "ENSG00000183431"
name: "splicing factor 3a subunit 3"
location: "1p34.3"
module: 1
arm: "+"
pooled_cpm: 58.39
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 2
n_dd_up_clean: 13
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# SF3A3

*splicing factor 3a subunit 3* — 1p34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.96× (z +15.2, q 0e+00, up in 43 of 48 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 2.49× (z +10.8, q 4e-25, up in 40 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.827× (z -5.8, q 3e-06, down in 25 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (AsPC-1 0.450×; ⚠ cell-cycle shift, explains ~0% of this change); [[Pimozide (drug)]] 0.05 µM in 1 line (CHP-212 0.1000×); [[Temsirolimus (drug)]] 0.5 µM in 1 line (CHP-212 0.104×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BMS1]] (+0.79, fdr 7e-06), [[PES1]] (+0.72, fdr 7e-06), [[DLAT]] (+0.71, fdr 7e-06); moves opposite to [[ZNF706]] (-0.60, fdr 2e-05), [[PEAK1]] (-0.57, fdr 2e-05), [[GABARAPL2]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 17 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11402.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **1.96×** | +15.2 | 0e+00 | 43/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.85×** | +13.4 | 2e-38 | 36/42 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.71×** | +11.3 | 4e-27 | 35/44 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.49×** | +10.8 | 4e-25 | 40/49 (A498, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.61×** | +10.8 | 6e-25 | 43/48 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.56×** | +10.1 | 8e-22 | 40/48 (NCI-H1792, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.34×** | +9.1 | 5e-18 | 31/48 (NCI-H1792, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.10×** | +8.8 | 9e-17 | 33/48 (LS 180, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.47×** | +8.8 | 9e-17 | 33/48 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.49×** | +8.6 | 3e-16 | 37/48 (NCI-H1792, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.40×** | +7.6 | 2e-12 | 37/48 (SW480, LOX-IMVI, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.39×** | +7.4 | 8e-12 | 32/48 (COLO 205, LOX-IMVI, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.35×** | +6.9 | 3e-10 | 32/48 (COLO 205, LoVo, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.34×** | +6.7 | 1e-09 | 30/48 (COLO 205, PANC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.33×** | +6.5 | 3e-09 | 30/48 (HOP62, A-427, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.27×** | +5.4 | 3e-06 | 25/48 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.16× | +4.6 | 1e-04 | 18/48 (HOP62, NCI-H460, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.24×** | +4.6 | 1e-04 | 22/47 (MIA PaCa-2, LoVo, …) | all doses, stronger at high dose | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.39×** | +3.9 | 0.002 | 14/48 (NCI-H460, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.35×** | +3.5 | 0.009 | 11/48 (J82, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.34×** | +3.5 | 0.012 | 10/48 (NCI-H460, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.05 µM |  | 1.17× | +3.3 | 0.021 | 11/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.30×** | +3.1 | 0.037 | 11/48 (NCI-H460, SW480, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11402.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (AsPC-1 0.450×; ⚠ cell-cycle shift, explains ~0% of this change); [[Pimozide (drug)]] 0.05 µM in 1 line (CHP-212 0.1000×); [[Temsirolimus (drug)]] 0.5 µM in 1 line (CHP-212 0.104×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.827×** | -5.8 | 3e-06 | 25/48 (A498, HS-578T, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.785×** | -5.5 | 1e-05 | 27/48 (SHP-77, Hs 766T, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.876× | -4.2 | 0.005 | 13/48 (C-33 A, SHP-77, …) | all doses, flat |  |
| [[Cepharanthine (drug)]] 5 µM |  | 0.881× | -4.0 | 0.010 | 8/48 (J82, SHP-77, …) | top dose only | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.863× | -3.4 | 0.087 | 14/47 (SK-MEL-2, A-427, …) | rises with dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 0.860× | -3.3 | 0.088 | 21/47 (SW480, KATO III, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11402. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 39.2 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.25× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.03× (z +9.9) | — |
| [[LOX-IMVI (line)]] | wt | 58.1 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.20× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.30× (z +8.8) | — |
| [[PANC-1 (line)]] | alt | 68.0 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.53× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 1.97× (z +8.9) | — |
| [[SW480 (line)]] | alt | 76.4 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.02× (z +15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 1.82× (z +8.6) | — |
| [[A-172 (line)]] | wt | 37.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.47× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[A498 (line)]] | wt | 95.3 | 3 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 4.13× (z +10.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 70.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.67× (z +16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[SNU-423 (line)]] | alt | 52.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.29× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[CHP-212 (line)]] | wt | 32.3 | 0 | 2 | — | [[Pimozide (drug)]] 0.05 µM 0.1000× (z -9.4) |
| [[HEC-1-A (line)]] | alt | 61.0 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +10.4) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[Hs 766T (line)]] | wt | 60.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.18× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[KATO III (line)]] | alt | 49.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.16× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[LS 180 (line)]] | wt | 39.1 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 7.63× (z +10.2) | — |
| [[NCI-H23 (line)]] | alt | 102 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.94× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[NCI-H460 (line)]] | wt | 39.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[AsPC-1 (line)]] | alt | 41.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.450× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 47.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +8.7) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[HepG2_C3A (line)]] | wt | 61.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +9.3) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[HT-29 (line)]] | alt | 39.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.08× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[LoVo (line)]] | wt | 40.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +8.9) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[NCI-H1573 (line)]] | alt | 32.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.86× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[Panc 03.27 (line)]] | alt | 72.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.14× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[A-427 (line)]] | wt | 57.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 41.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 86.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 71.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 50.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 63.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 81.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 78.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 53.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 92.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 68.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 75.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 77.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 64.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 82.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 55.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 76.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 47.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 59.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11402), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BMS1]] | +0.79 | +0.81 / +0.78 | both halves | 7e-06 | STRING 407 |
| [[PES1]] | +0.72 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[DLAT]] | +0.71 | +0.74 / +0.66 | both halves | 7e-06 |  |
| [[DDX1]] | +0.70 | +0.72 / +0.64 | both halves | 7e-06 |  |
| [[GTF2H3]] | +0.69 | +0.61 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_DNA_REPAIR |
| [[SMARCAD1]] | +0.68 | +0.73 / +0.63 | both halves | 7e-06 |  |
| [[LAS1L]] | +0.67 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[LSG1]] | +0.66 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[MAK16]] | +0.66 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[RBM28]] | +0.65 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[UCHL5]] | +0.64 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[PRMT5]] | +0.64 | +0.67 / +0.57 | both halves | 1e-05 | STRING 843 |

## Genes that move opposite

*14 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF706]] | -0.60 | -0.46 / -0.61 | both halves | 2e-05 |  |
| [[PEAK1]] | -0.57 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[GABARAPL2]] | -0.57 | -0.54 / -0.61 | both halves | 1e-05 |  |
| [[HIGD2A]] | -0.56 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[NPC2]] | -0.55 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[MIF]] | -0.54 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[CSKMT]] | -0.54 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[COX7B]] | -0.54 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[HINT1]] | -0.54 | -0.41 / -0.63 | both halves | 4e-05 |  |
| [[SLC25A5]] | -0.53 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[RPL37A]] ⚠ | -0.53 | -0.48 / -0.59 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[EIF1B]] | -0.53 | -0.42 / -0.50 | both halves | 4e-05 | pathway: HALLMARK_DNA_REPAIR |
| [[MIEN1]] | -0.52 | -0.49 / -0.58 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.570). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-21.1, -39.3); signed map (-3.4, -42.0). **Vector** length 101, 26.3% of its response variance represented; |z| ≥ 3 in 1,099 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.6 | +10.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.6 | +8.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.8 | +10.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.4 | +10.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.8 | +5.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +7.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.2 | +1.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.1 | +4.6 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -7.7 | -2.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.9 | -2.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.7 | -3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.2 | -5.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.2 | -0.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.2 | -2.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.1 | -2.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.1 | -0.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.8 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | splicing factor 3a subunit 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.3 — chr1:37,956,975-37,990,075 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SF3a60, SAP61, PRP9, PRPF9 |
| Gene groups (HGNC) | U2 small nuclear ribonucleoprotein; SF3a complex |
| Hallmark sets | DNA_REPAIR |
| Reactome | 13 pathways, smallest: CHD1 and CHD2 subfamily; CHD chromatin remodelers; mRNA Polyadenylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12874](https://www.uniprot.org/uniprotkb/Q12874) (Splicing factor 3A subunit 3):

> Component of the 17S U2 SnRNP complex of the spliceosome, a large ribonucleoprotein complex that removes introns from transcribed pre-mRNAs. The 17S U2 SnRNP complex (1) directly participates in early spliceosome assembly and (2) mediates recognition of the intron branch site during pre-mRNA splicing by promoting the selection of the pre-mRNA branch-site adenosine, the nucleophile for the first step of splicing. Within the 17S U2 SnRNP complex, SF3A3 is part of the SF3A subcomplex that …

**Summary**, from NCBI Gene [10946](https://www.ncbi.nlm.nih.gov/gene/10946):

> This gene encodes subunit 3 of the splicing factor 3a protein complex. The splicing factor 3a heterotrimer includes subunits 1, 2 and 3 and is necessary for the in vitro conversion of 15S U2 snRNP into an active 17S particle that performs pre-mRNA splicing. Subunit 3 interacts with subunit 1 through its amino-terminus while the zinc finger domain of subunit 3 plays a role in its binding to the 15S U2 snRNP. This gene has a pseudogene on chromosome 20. Alternative splicing results in multiple …

**Accessions** — [HGNC:10767](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10767) · Entrez [10946](https://www.ncbi.nlm.nih.gov/gene/10946) · UniProt [Q12874](https://www.uniprot.org/uniprotkb/Q12874) · Ensembl [ENSG00000183431](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183431)

## Data

Gene col 11402: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11402); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11402, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11402]; `tensor/DDL_lfc|DDL_z.npy` [11402]; `embed/gene_vectors.npy` [11402]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11402 or target_col == 11402). Every well: [[SF3A3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SF3A3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
