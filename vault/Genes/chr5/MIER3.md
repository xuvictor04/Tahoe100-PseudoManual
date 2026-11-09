---
symbol: "MIER3"
type: "gene"
col: 7903
ensembl_id: "ENSG00000155545"
name: "MIER family member 3"
location: "5q11.2"
module: 11
arm: "+"
pooled_cpm: 39.54
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 7
n_dd_up_clean: 17
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# MIER3

*MIER family member 3* — 5q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.19× (z +20.1, q 0e+00, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.393× (z -16.4, q 0e+00, down in 32 of 40 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.531× (z -11.6, q 1e-28, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF689]] (+0.79, fdr 1e-05), [[ZNF747]] (+0.72, fdr 7e-05), [[ZNF24]] (+0.71, fdr 1e-05); moves opposite to [[GNAI2]] (-0.65, fdr 3e-04), [[SLC27A1]] (-0.64, fdr 1e-04), [[WDR59]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7903.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.19×** | +20.1 | 0e+00 | 43/48 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.08×** | +13.3 | 4e-38 | 41/48 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.00×** | +12.6 | 2e-34 | 45/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.03×** | +12.4 | 3e-33 | 44/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.94×** | +10.3 | 1e-22 | 35/49 (SW480, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.62×** | +8.7 | 2e-16 | 40/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.58×** | +8.3 | 9e-15 | 35/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.28×** | +7.8 | 3e-13 | 35/48 (SW480, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.53×** | +7.8 | 4e-13 | 37/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.49×** | +7.3 | 2e-11 | 31/48 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +6.7 | 1e-09 | 27/47 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.36×** | +5.3 | 5e-06 | 26/48 (SNU-423, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.72×** | +5.2 | 1e-05 | 25/42 (A-427, SW480, …) | all doses, flat | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.22×** | +5.1 | 1e-05 | 22/48 (HEC-1-A, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.32×** | +5.1 | 1e-05 | 29/48 (CFPAC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.29×** | +4.7 | 1e-04 | 22/47 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.24×** | +3.9 | 0.003 | 16/47 (H4, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7903.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.393×** | -16.4 | 0e+00 | 32/40 (Panc 03.27, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.447×** | -14.7 | 0e+00 | 43/48 (A498, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.531×** | -11.6 | 1e-28 | 43/48 (SW1417, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.539×** | -11.3 | 2e-27 | 39/48 (SW1417, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.635×** | -8.3 | 1e-14 | 37/48 (SW1417, A498, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.612×** | -8.3 | 1e-14 | 30/45 (A-427, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.928× | -4.6 | 3e-04 | 1/49 (NCI-H1792) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.868× | -3.7 | 0.018 | 16/48 (KATO III, SW1417, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.758×** | -3.6 | 0.019 | 18/47 (AN3 CA, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~10% of this change | 0.840× | -3.2 | 0.077 | 15/48 (SW1417, A498, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7903. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 42.8 | 6 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.363× (z -12.4) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 40.5 | 6 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +13.0) | [[Dinaciclib (drug)]] 5 µM 0.249× (z -16.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 40.0 | 1 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.249× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.355× (z -11.3) |
| [[PANC-1 (line)]] | alt | 34.5 | 5 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +17.4) | [[Dinaciclib (drug)]] 0.5 µM 0.322× (z -13.3) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 51.9 | 2 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +13.2) | [[Dinaciclib (drug)]] 0.05 µM 0.298× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.408× (z -9.7) |
| [[CFPAC-1 (line)]] | alt | 29.1 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +13.0) | [[Dinaciclib (drug)]] 0.5 µM 0.363× (z -8.8) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 44.6 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +11.1) | [[Panobinostat (drug)]] 5 µM 0.216× (z -14.4) |
| [[A549 (line)]] | wt | 39.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +15.2) | — |
| [[HepG2_C3A (line)]] | wt | 29.4 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.0936× (z -14.4) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 32.4 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.146× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.381× (z -8.7) |
| [[KATO III (line)]] | alt | 46.3 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +9.2) | [[Panobinostat (drug)]] 0.5 µM 0.301× (z -10.8) |
| [[LoVo (line)]] | wt | 91.5 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.96× (z +8.5) | [[Panobinostat (drug)]] 5 µM 0.340× (z -9.9) |
| [[NCI-H2030 (line)]] | alt | 35.2 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.348× (z -8.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 63.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.139× (z -19.2) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 89.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.126× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.379× (z -8.6) |
| [[J82 (line)]] | alt | 33.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.228× (z -14.0) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 40.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.281× (z -11.0) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 33.6 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.66× (z +10.9) | — |
| [[NCI-H1573 (line)]] | alt | 25.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +11.8) | [[Dinaciclib (drug)]] 0.05 µM 0.255× (z -10.2) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 32.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.251× (z -12.3) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 50.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.102× (z -20.3) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 49.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +12.9) | [[Dinaciclib (drug)]] 0.5 µM 0.192× (z -14.5) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 53.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.157× (z -11.8) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 32.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.264× (z -10.7) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 45.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +11.2) | — |
| [[BT-474 (line)]] | alt | 49.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +9.7) | — |
| [[COLO 205 (line)]] | alt | 35.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +10.3) | — |
| [[HCT15 (line)]] | alt | 49.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +10.3) | — |
| [[Hs 766T (line)]] | wt | 24.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.117× (z -13.9) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 29.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.277× (z -8.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 47.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +8.5) | — |
| [[NCI-H1792 (line)]] | alt | 24.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0807× (z -17.8) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 33.0 | 0 | 1 | — | [[Malotilate (drug)]] 0.05 µM 0.0662× (z -8.6) |
| [[SW 900 (line)]] | alt | 51.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.329× (z -8.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 39.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 46.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 54.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 66.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 44.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7903), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF689]] | +0.79 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[ZNF747]] | +0.72 | +0.65 / +0.38 | both halves | 7e-05 |  |
| [[ZNF24]] | +0.71 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[MARVELD2]] | +0.70 | +0.63 / +0.44 | both halves | 3e-05 |  |
| [[ZSCAN29]] | +0.69 | +0.66 / +0.41 | both halves | 4e-05 |  |
| [[RPP38]] | +0.69 | +0.62 / +0.46 | both halves | 2e-05 |  |
| [[ZNF649]] | +0.69 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[ATXN7]] | +0.68 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[AP5M1]] | +0.67 | +0.63 / +0.20 | ⚠ one half (not replicated) | 8e-04 |  |
| [[ZNF629]] | +0.67 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[PEF1]] | +0.66 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[DCUN1D1]] | +0.66 | +0.76 / +0.40 | both halves | 4e-05 |  |
| [[ZBTB33]] | +0.66 | +0.59 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAI2]] | -0.65 | -0.42 / -0.29 | both halves | 3e-04 |  |
| [[SLC27A1]] | -0.64 | -0.43 / -0.34 | both halves | 1e-04 |  |
| [[WDR59]] | -0.63 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[COG5]] | -0.63 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[TMEM120B]] | -0.63 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[PCMT1]] | -0.62 | -0.43 / -0.33 | both halves | 1e-04 |  |
| [[QSOX1]] | -0.62 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[P4HB]] | -0.61 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[FCHO1]] | -0.61 | -0.48 / -0.15 | ⚠ not reproduced | 0.001 |  |
| [[F11R]] | -0.60 | -0.47 / -0.38 | both halves | 7e-05 |  |
| [[HSP90B1]] | -0.60 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[SNX1]] | -0.59 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[PDIA4]] | -0.59 | -0.52 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises MIER3's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[FAXC]] | B | FAXC activity raises MIER3's level | lines that do not express FAXC (11) vs lines expressing it (39) | 1.17× lower at baseline in the lines without FAXC | 0.060 | ⚠ within organs, on part of the lines; also absent: NTN1, CYP46A1, CSRP2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.629). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-8.8, 8.5); signed map (13.8, -21.4). **Vector** length 83.9, 20.1% of its response variance represented; |z| ≥ 3 in 1,220 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.2 | +4.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +5.8 | +4.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.7 | +8.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.6 | +13.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +5.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.7 | +7.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.5 | +3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | +1.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.7 | +3.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.0 | +2.5 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -6.8 | -11.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -6.1 | -11.3 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.9 | -8.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.0 | -2.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~10% of this change | -1.8 | -3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.7 | -0.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.4 | -3.6 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.4 | +0.6 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.4 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | MIER family member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q11.2 — chr5:56,919,602-56,971,675 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ35954, DKFZp686L09111, DKFZp781I1119 |
| Gene groups (HGNC) | Myb/SANT domain containing; MIER complex subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z3K6](https://www.uniprot.org/uniprotkb/Q7Z3K6) (Mesoderm induction early response protein 3):

> Transcriptional repressor.

**Summary**, from NCBI Gene [166968](https://www.ncbi.nlm.nih.gov/gene/166968):

> Predicted to enable histone deacetylase binding activity and transcription corepressor activity. Predicted to be involved in negative regulation of transcription by RNA polymerase II. Located in nucleoplasm. Part of protein-containing complex. Implicated in breast cancer and lung adenocarcinoma. Biomarker of breast cancer; invasive ductal carcinoma; and lung non-small cell carcinoma. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26678](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26678) · Entrez [166968](https://www.ncbi.nlm.nih.gov/gene/166968) · UniProt [Q7Z3K6](https://www.uniprot.org/uniprotkb/Q7Z3K6) · Ensembl [ENSG00000155545](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155545)

## Data

Gene col 7903: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7903); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7903, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7903]; `tensor/DDL_lfc|DDL_z.npy` [7903]; `embed/gene_vectors.npy` [7903]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7903 or target_col == 7903). Every well: [[MIER3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MIER3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
