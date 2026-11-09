---
symbol: "DNTTIP2"
type: "gene"
col: 859
ensembl_id: "ENSG00000067334"
name: "deoxynucleotidyltransferase terminal interacting protein 2"
location: "1p22.1"
module: 7
arm: "+"
pooled_cpm: 82.91
n_lines_expressing: 50
n_dd_up: 39
n_dd_down: 0
n_dd_up_clean: 21
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# DNTTIP2

*deoxynucleotidyltransferase terminal interacting protein 2* — 1p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 39 drug-doses (18 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 3.35× (z +16.3, q 0e+00, up in 48 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 2 lines (MIA PaCa-2 0.624×, NCI-H2030 0.769×; ⚠ position not correctable); [[Dinaciclib (drug)]] 5 µM in 1 line (AsPC-1 0.270×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SW48 0.267×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMD7]] (+0.83, fdr 7e-06), [[CCDC137]] (+0.76, fdr 7e-06), [[MRM3]] (+0.75, fdr 7e-06); moves opposite to [[H3-3A]] (-0.69, fdr 7e-06), [[SUMF2]] (-0.68, fdr 7e-06), [[TWSG1]] (-0.67, fdr 7e-06).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 19 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 39 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 859.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.35×** | +16.3 | 0e+00 | 48/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **3.30×** | +16.1 | 0e+00 | 48/48 (KATO III, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **3.30×** | +16.1 | 0e+00 | 48/48 (LoVo, HT-29, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **2.38×** | +15.8 | 0e+00 | 48/48 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.98×** | +14.7 | 0e+00 | 48/48 (HT-29, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.96×** | +14.0 | 1e-42 | 48/48 (NCI-H1792, A498, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.94×** | +13.3 | 1e-38 | 48/48 (HT-29, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.59×** | +12.8 | 9e-36 | 48/48 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.03×** | +9.5 | 1e-19 | 46/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **3.77×** | +9.3 | 6e-19 | 46/49 (Hs 766T, MIA PaCa-2, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.90×** | +7.5 | 3e-12 | 44/45 (Panc 03.27, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.70×** | +7.1 | 5e-11 | 43/48 (NCI-H1792, HT-29, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.62×** | +6.5 | 4e-09 | 40/48 (SW 900, PANC-1, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.63×** | +6.3 | 1e-08 | 38/47 (C-33 A, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.54×** | +5.8 | 2e-07 | 35/48 (SW 900, PANC-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.35×** | +5.3 | 3e-06 | 39/48 (PANC-1, Hs 766T, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.45×** | +4.8 | 5e-05 | 37/47 (MIA PaCa-2, HT-29, …) | all doses, stronger at high dose | position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.97×** | +4.7 | 7e-05 | 38/49 (CFPAC-1, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.96×** | +4.7 | 7e-05 | 41/48 (HT-29, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.87×** | +4.4 | 3e-04 | 33/48 (NCI-H1573, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.36×** | +4.1 | 8e-04 | 30/47 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.77×** | +4.0 | 0.001 | 35/48 (CFPAC-1, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 859.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 2 lines (MIA PaCa-2 0.624×, NCI-H2030 0.769×; ⚠ position not correctable); [[Dinaciclib (drug)]] 5 µM in 1 line (AsPC-1 0.270×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SW48 0.267×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.913× | -3.8 | 0.070 | 7/50 (MIA PaCa-2, NCI-H2030, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.835× | -3.3 | 0.27 | 18/48 (A498, KATO III, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, +0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 859. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 59.1 | 11 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +17.2) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.93× (z +16.1) | — |
| [[NCI-H460 (line)]] | wt | 67.4 | 10 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.97× (z +12.6) | — |
| [[C32 (line)]] | wt | 57.5 | 9 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 8.05× (z +16.8) | — |
| [[HEC-1-A (line)]] | alt | 76.8 | 9 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.26× (z +13.8) | — |
| [[HOP62 (line)]] | alt | 42.9 | 9 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.97× (z +14.2) | — |
| [[Hs 766T (line)]] | wt | 85.6 | 9 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.69× (z +14.2) | — |
| [[LOX-IMVI (line)]] | wt | 58.5 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +14.6) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.28× (z +14.0) | — |
| [[LS 180 (line)]] | wt | 79.0 | 9 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.30× (z +13.3) | — |
| [[NCI-H2347 (line)]] | alt | 59.7 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +13.7) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.81× (z +13.5) | — |
| [[A-172 (line)]] | wt | 68.2 | 8 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.89× (z +12.5) | — |
| [[A498 (line)]] | wt | 140 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +12.6) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.70× (z +12.1) | — |
| [[HS-578T (line)]] | alt | 81.2 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +15.4) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.52× (z +12.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 230 | 7 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.99× (z +14.5) | [[Adagrasib (drug)]] 0.05 µM 0.624× (z -16.8) ⚠ position not correctable |
| [[NCI-H1573 (line)]] | alt | 105 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.24× (z +16.7) | — |
| [[NCI-H2030 (line)]] | alt | 105 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.26× (z +14.8) | — |
| [[SW 900 (line)]] | alt | 85.3 | 8 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.76× (z +11.9) | — |
| [[SW480 (line)]] | alt | 81.9 | 8 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.34× (z +14.8) | — |
| [[A549 (line)]] | wt | 57.6 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +15.2) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.20× (z +13.3) | — |
| [[CFPAC-1 (line)]] | alt | 69.0 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +15.3) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.49× (z +14.8) | — |
| [[HT-29 (line)]] | alt | 83.5 | 7 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 6.87× (z +18.8) | — |
| [[hTERT-HPNE (line)]] | wt | 62.5 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.77× (z +11.4) | — |
| [[KATO III (line)]] | alt | 66.1 | 7 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.42× (z +14.7) | — |
| [[NCI-H1792 (line)]] | alt | 48.3 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +15.7) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.49× (z +13.4) | — |
| [[SNU-423 (line)]] | alt | 72.5 | 7 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.52× (z +13.0) | — |
| [[J82 (line)]] | alt | 113 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +13.0) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.08× (z +12.0) | — |
| [[Panc 03.27 (line)]] | alt | 82.9 | 6 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.01× (z +13.0) | — |
| [[RPMI-7951 (line)]] | alt | 93.1 | 6 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.83× (z +11.6) | — |
| [[SW1417 (line)]] | alt | 69.6 | 6 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.82× (z +10.6) | — |
| [[AsPC-1 (line)]] | alt | 94.0 | 4 (2 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.41× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.270× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 67.7 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.71× (z +11.9) | — |
| [[LoVo (line)]] | wt | 96.7 | 5 | 0 | [[Auranofin (drug)]] 5 µM 7.96× (z +20.5) | — |
| [[SK-MEL-2 (line)]] | alt | 105 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.12× (z +10.1) | — |
| [[NCI-H23 (line)]] | alt | 120 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.63× (z +12.2) | — |
| [[A-427 (line)]] | wt | 50.3 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.37× (z +9.9) | — |
| [[COLO 205 (line)]] | alt | 45.6 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 7.30× (z +13.1) | — |
| [[HCT15 (line)]] | alt | 102 | 3 | 0 | [[Auranofin (drug)]] 5 µM 4.21× (z +10.4) | — |
| [[RKO (line)]] | wt | 123 | 3 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 2.96× (z +8.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.76× (z +8.6) | — |
| [[BT-474 (line)]] | alt | 54.1 | 2 | 0 | [[Auranofin (drug)]] 5 µM 4.05× (z +10.2) | — |
| [[SHP-77 (line)]] | alt | 72.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +10.5) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.36× (z +9.9) | — |
| [[SNU-1 (line)]] | wt | 75.2 | 2 | 0 | [[Auranofin (drug)]] 5 µM 4.02× (z +9.6) | — |
| [[C-33 A (line)]] | alt | 75.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.47× (z +9.4) | — |
| [[H4 (line)]] | wt | 69.9 | 1 | 0 | [[Bortezomib (drug)]] 0.05 µM 3.97× (z +8.8) | — |
| [[SW48 (line)]] | wt | 102 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.267× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change |
| [[AN3 CA (line)]] | alt | 88.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 42.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 62.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 68.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 73.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 70.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 73.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 859), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMD7]] | +0.83 | +0.86 / +0.79 | both halves | 7e-06 |  |
| [[CCDC137]] | +0.76 | +0.77 / +0.71 | both halves | 7e-06 |  |
| [[MRM3]] | +0.75 | +0.69 / +0.76 | both halves | 7e-06 |  |
| [[TRMT10C]] | +0.74 | +0.78 / +0.69 | both halves | 7e-06 |  |
| [[REXO4]] | +0.74 | +0.80 / +0.75 | both halves | 7e-06 | STRING 731 |
| [[NSRP1]] | +0.74 | +0.75 / +0.70 | both halves | 7e-06 |  |
| [[FAM32A]] | +0.73 | +0.79 / +0.64 | both halves | 7e-06 |  |
| [[WAPL]] | +0.72 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[C12orf43]] | +0.72 | +0.64 / +0.73 | both halves | 7e-06 |  |
| [[FADD]] | +0.72 | +0.77 / +0.67 | both halves | 7e-06 |  |
| [[UTP3]] | +0.70 | +0.74 / +0.64 | both halves | 7e-06 | STRING 998 |
| [[ZNF562]] | +0.70 | +0.71 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[H3-3A]] | -0.69 | -0.69 / -0.68 | both halves | 7e-06 |  |
| [[SUMF2]] | -0.68 | -0.62 / -0.68 | both halves | 7e-06 |  |
| [[TWSG1]] | -0.67 | -0.64 / -0.65 | both halves | 7e-06 |  |
| [[RCN2]] | -0.64 | -0.63 / -0.58 | both halves | 7e-06 |  |
| [[SLC25A40]] | -0.64 | -0.62 / -0.59 | both halves | 7e-06 |  |
| [[LIX1L]] | -0.63 | -0.65 / -0.52 | both halves | 1e-05 |  |
| [[PRKACA]] | -0.62 | -0.48 / -0.66 | both halves | 2e-05 |  |
| [[CLSTN1]] | -0.61 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[NPTN]] | -0.61 | -0.70 / -0.56 | both halves | 1e-05 |  |
| [[TLE5]] | -0.60 | -0.62 / -0.48 | both halves | 2e-05 |  |
| [[ATP6AP2]] | -0.59 | -0.59 / -0.62 | both halves | 7e-06 |  |
| [[SLC25A23]] | -0.59 | -0.55 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.710). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-41.3, 1.8); signed map (-3.6, -23.5). **Vector** length 108, 41.1% of its response variance represented; |z| ≥ 3 in 1,329 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +9.6 | +13.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +9.2 | +16.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +8.5 | +14.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +8.5 | +16.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.3 | +16.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +7.2 | +9.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +4.7 | +3.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.0 | +3.4 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change | -3.6 | +4.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | -3.5 | +6.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.4 | +0.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -3.3 | -0.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.7 | +2.7 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -2.3 | -2.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.3 | -0.7 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | -2.2 | -0.7 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.2 | -0.8 |
|  | [[Clonidine (hydrochloride) (drug)]] 5 µM |  | -1.9 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | deoxynucleotidyltransferase terminal interacting protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p22.1 — chr1:93,866,284-93,879,918 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HSU15552, ERBP, TdIF2 |
| Hallmark sets | P53_PATHWAY |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5QJE6](https://www.uniprot.org/uniprotkb/Q5QJE6) (Deoxynucleotidyltransferase terminal-interacting protein 2):

> Regulates the transcriptional activity of DNTT and ESR1. May function as a chromatin remodeling protein. Part of the small subunit (SSU) processome, first precursor of the small eukaryotic ribosomal subunit. During the assembly of the SSU processome in the nucleolus, many ribosome biogenesis factors, an RNA chaperone and ribosomal proteins associate with the nascent pre-rRNA and work in concert to generate RNA folding, modifications, rearrangements and cleavage as well as targeted degradation …

**Summary**, from NCBI Gene [30836](https://www.ncbi.nlm.nih.gov/gene/30836):

> This gene is thought to be involved in chromatin remodeling and gene transcription. The encoded nuclear protein binds to and enhances the transcriptional activity of the estrogen receptor alpha, and also interacts with terminal deoxynucleotidyltransferase. The expression profile of this gene is a potential biomarker for chronic obstructive pulmonary disease. [provided by RefSeq, Dec 2010]

**Accessions** — [HGNC:24013](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24013) · Entrez [30836](https://www.ncbi.nlm.nih.gov/gene/30836) · UniProt [Q5QJE6](https://www.uniprot.org/uniprotkb/Q5QJE6) · Ensembl [ENSG00000067334](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000067334)

## Data

Gene col 859: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 859); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 859, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 859]; `tensor/DDL_lfc|DDL_z.npy` [859]; `embed/gene_vectors.npy` [859]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 859 or target_col == 859). Every well: [[DNTTIP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNTTIP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
