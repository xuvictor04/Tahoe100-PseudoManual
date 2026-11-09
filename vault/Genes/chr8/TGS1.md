---
symbol: "TGS1"
type: "gene"
col: 6038
ensembl_id: "ENSG00000137574"
name: "trimethylguanosine synthase 1"
location: "8q12.1"
module: 7
arm: "+"
pooled_cpm: 58.33
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 3
n_dd_up_clean: 17
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# TGS1

*trimethylguanosine synthase 1* — 8q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.78× (z +20.0, q 0e+00, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.587× (z -12.6, q 2e-33, down in 33 of 43 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (LoVo 0.163×, PANC-1 0.410×, C-33 A 0.216×, NCI-H2030 0.360×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (A-427 0.359×, CHP-212 0.0725×, SW480 0.508×, PANC-1 0.526×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (SNU-423 0.220×, RKO 0.425×, KATO III 0.371×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MIEF1]] (+0.63, fdr 7e-06), [[RRN3]] (+0.60, fdr 1e-05), [[DDX55]] (+0.58, fdr 2e-05); moves opposite to [[CD99]] (-0.53, fdr 1e-05), [[TMSB4X]] (-0.50, fdr 3e-05), [[C12orf75]] (-0.46, fdr 3e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 14 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6038.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.78×** | +20.0 | 0e+00 | 42/48 (NCI-H1792, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.89×** | +15.6 | 0e+00 | 45/48 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.88×** | +13.6 | 1e-39 | 45/49 (A498, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.57×** | +11.0 | 4e-26 | 40/48 (SW480, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.24×** | +10.3 | 5e-23 | 36/48 (LS 180, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.51×** | +10.2 | 2e-22 | 31/48 (LoVo, A498, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.51×** | +10.1 | 4e-22 | 38/48 (PANC-1, A498, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.52×** | +9.9 | 2e-21 | 34/48 (MIA PaCa-2, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.50×** | +9.9 | 2e-21 | 40/48 (SW480, NCI-H1792, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.48×** | +9.7 | 3e-20 | 38/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.30×** | +9.0 | 1e-17 | 31/48 (A549, SNU-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.44×** | +8.9 | 2e-17 | 41/48 (LoVo, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.39×** | +8.1 | 2e-14 | 33/48 (COLO 205, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.33×** | +6.6 | 2e-09 | 28/48 (HOP62, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~23% of this change | **1.31×** | +6.3 | 1e-08 | 29/47 (SW480, NCI-H1573, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **1.47×** | +5.0 | 2e-05 | 21/48 (PANC-1, A498, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.46×** | +4.8 | 3e-05 | 22/48 (PANC-1, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.20×** | +4.5 | 1e-04 | 23/48 (HOP62, LoVo, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.38×** | +4.1 | 8e-04 | 18/48 (A498, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.38×** | +4.1 | 9e-04 | 19/48 (AsPC-1, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 5 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6038.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (LoVo 0.163×, PANC-1 0.410×, C-33 A 0.216×, NCI-H2030 0.360×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (A-427 0.359×, CHP-212 0.0725×, SW480 0.508×, PANC-1 0.526×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (SNU-423 0.220×, RKO 0.425×, KATO III 0.371×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.587×** | -12.6 | 2e-33 | 33/43 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.619×** | -11.8 | 2e-29 | 35/49 (A-427, CHP-212, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.619×** | -10.9 | 3e-25 | 31/45 (SNU-423, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.939× | -5.0 | 8e-05 | 0/49 | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 0.870× | -3.4 | 0.070 | 13/48 (LS 180, H4, …) | inconsistent across doses |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | 0.836× | -3.1 | 0.16 | 12/48 (CHP-212, SW 1271, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6038. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 65.0 | 4 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.37× (z +14.4) | [[Dinaciclib (drug)]] 5 µM 0.410× (z -14.4) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 89.7 | 4 (2 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.30× (z +13.1) | [[Dinaciclib (drug)]] 0.5 µM 0.489× (z -10.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 61.6 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +12.5) | [[Dinaciclib (drug)]] 0.5 µM 0.508× (z -10.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 66.5 | 2 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 3.12× (z +16.4) | [[Dinaciclib (drug)]] 5 µM 0.163× (z -25.2) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 78.5 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.32× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.325× (z -11.0) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 78.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +13.4) | — |
| [[NCI-H2030 (line)]] | alt | 69.5 | 1 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.02× (z +8.6) ⚠ cell-cycle shift, explains ~22% of this change | [[Dinaciclib (drug)]] 5 µM 0.360× (z -12.2) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 51.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +13.8) | — |
| [[COLO 205 (line)]] | alt | 64.9 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 8.53× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.390× (z -8.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 47.2 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.409× (z -9.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 103 | 2 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.26× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.415× (z -9.9) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 48.6 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.316× (z -10.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 53.5 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.40× (z +8.9) | — |
| [[C32 (line)]] | wt | 62.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +11.9) | — |
| [[CFPAC-1 (line)]] | alt | 37.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +14.5) | — |
| [[H4 (line)]] | wt | 51.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.261× (z -9.2) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 47.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +9.7) | — |
| [[KATO III (line)]] | alt | 75.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.371× (z -10.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 27.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +10.6) | — |
| [[NCI-H1792 (line)]] | alt | 36.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +15.6) | — |
| [[NCI-H2347 (line)]] | alt | 49.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.340× (z -11.9) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 41.6 | 2 (2 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.27× (z +8.7) ⚠ toxic; cell-cycle shift, explains ~45% of this change | — |
| [[RKO (line)]] | wt | 131 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +10.8) | [[Dinaciclib (drug)]] 0.05 µM 0.425× (z -10.8) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 53.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.354× (z -9.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 68.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.359× (z -12.4) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 40.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +8.5) | — |
| [[C-33 A (line)]] | alt | 58.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.216× (z -13.8) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 54.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0725× (z -12.3) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 49.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +9.6) | — |
| [[Hs 766T (line)]] | wt | 35.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +11.0) | — |
| [[HS-578T (line)]] | alt | 52.8 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.41× (z +8.6) | — |
| [[hTERT-HPNE (line)]] | wt | 37.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +9.0) | — |
| [[NCI-H23 (line)]] | alt | 74.1 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.25× (z +9.0) | — |
| [[SHP-77 (line)]] | alt | 88.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.388× (z -10.1) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 51.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +11.3) | — |
| [[SNU-423 (line)]] | alt | 39.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.220× (z -12.8) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 44.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +11.3) | — |
| [[A-172 (line)]] | wt | 36.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 62.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 61.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 39.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 50.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 55.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 65.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 55.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 70.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 59.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 60.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6038), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIEF1]] | +0.63 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[RRN3]] | +0.60 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[DDX55]] | +0.58 | +0.47 / +0.66 | both halves | 2e-05 |  |
| [[NOL8]] | +0.58 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[GRPEL2]] | +0.56 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[REXO4]] | +0.55 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[CEBPZ]] | +0.55 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[CCDC43]] | +0.55 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[SMARCAD1]] | +0.55 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[SART3]] | +0.55 | +0.56 / +0.46 | both halves | 2e-05 | STRING 513 |
| [[DHX36]] | +0.54 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[MRPL46]] | +0.54 | +0.54 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CD99]] | -0.53 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[TMSB4X]] | -0.50 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[C12orf75]] | -0.46 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[PRKACA]] | -0.46 | -0.40 / -0.41 | both halves | 4e-05 | pathway: Organelle biogenesis and maintenance |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.451). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-40.8, 0.6); signed map (-2.6, -22.2). **Vector** length 78.9, 18.0% of its response variance represented; |z| ≥ 3 in 1,193 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +6.0 | +9.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.7 | +10.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~45% of this change | +4.6 | +4.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +4.1 | +5.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +10.2 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.1 | +5.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.0 | +4.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.9 | +2.6 |
|  | [[EX229 (drug)]] 5 µM |  | +2.7 | +4.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -0.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.9 | -12.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -2.8 | -10.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -2.7 | -11.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -2.5 | +5.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.8 | -2.2 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.7 | -1.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.6 | -0.6 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.5 | -1.2 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.4 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | trimethylguanosine synthase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q12.1 — chr8:55,773,446-55,826,445 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PIMT; previously NCOA6IP |
| Gene groups (HGNC) | 7BS DNA/RNA methyltransferases; DNA/RNA methyltransferases |
| Reactome | 23 pathways, smallest: BMAL1:CLOCK,NPAS2 activates circadian expression; RORA,B,C and NR1D1 (REV-ERBA) regulate gene expression; Expression of BMAL (ARNTL), CLOCK, and NPAS2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96RS0](https://www.uniprot.org/uniprotkb/Q96RS0) (Trimethylguanosine synthase):

> Catalyzes the 2 serial methylation steps for the conversion of the 7-monomethylguanosine (m(7)G) caps of snRNAs and snoRNAs to a 2,2,7-trimethylguanosine (m(2,2,7)G) cap structure. The enzyme is specific for guanine, and N7 methylation must precede N2 methylation. Hypermethylation of the m7G cap of U snRNAs leads to their concentration in nuclear foci, their colocalization with coilin and the formation of canonical Cajal bodies (CBs). Plays a role in transcriptional regulation.

**Summary**, from NCBI Gene [96764](https://www.ncbi.nlm.nih.gov/gene/96764):

> Enables RNA cap trimethylguanosine synthase activity. Involved in 7-methylguanosine cap hypermethylation. Located in cytosol and nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17843](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17843) · Entrez [96764](https://www.ncbi.nlm.nih.gov/gene/96764) · UniProt [Q96RS0](https://www.uniprot.org/uniprotkb/Q96RS0) · Ensembl [ENSG00000137574](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137574)

## Data

Gene col 6038: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6038); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6038, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6038]; `tensor/DDL_lfc|DDL_z.npy` [6038]; `embed/gene_vectors.npy` [6038]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6038 or target_col == 6038). Every well: [[TGS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TGS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
