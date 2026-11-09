---
symbol: "RAB7A"
type: "gene"
col: 1131
ensembl_id: "ENSG00000075785"
name: "RAB7A, member RAS oncogene family"
location: "3q21.3"
module: 53
arm: "+"
pooled_cpm: 497.4
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 11
n_dd_up_clean: 22
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# RAB7A

*RAB7A, member RAS oncogene family* — 3q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.63× (z +18.1, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 0.717× (z -6.2, q 3e-07, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP6V1D]] (+0.67, fdr 7e-06), [[SLC9A1]] (+0.65, fdr 1e-05), [[CLTA]] (+0.62, fdr 5e-05); moves opposite to [[KCTD3]] (-0.61, fdr 7e-06), [[FIP1L1]] (-0.60, fdr 1e-05), [[NDUFAF5]] (-0.56, fdr 1e-05).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF165]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1131.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.63×** | +18.1 | 0e+00 | 48/48 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.96×** | +17.8 | 0e+00 | 40/48 (Hs 766T, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.25×** | +15.1 | 0e+00 | 48/48 (NCI-H460, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.81×** | +13.1 | 7e-37 | 49/49 (Hs 766T, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.05×** | +12.7 | 1e-34 | 47/48 (NCI-H460, SNU-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.96×** | +12.6 | 2e-34 | 47/48 (SW480, SNU-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.96×** | +11.8 | 2e-30 | 46/48 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.84×** | +10.2 | 1e-22 | 46/48 (HEC-1-A, hTERT-HPNE, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.70×** | +9.9 | 3e-21 | 47/48 (KATO III, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.50×** | +7.1 | 5e-11 | 44/48 (KATO III, HT-29, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +6.5 | 5e-09 | 29/49 (LS 180, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.41×** | +6.2 | 2e-08 | 34/48 (AsPC-1, COLO 205, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.51×** | +5.5 | 2e-06 | 42/49 (HEC-1-A, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.38×** | +5.4 | 2e-06 | 36/48 (HEC-1-A, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.34×** | +5.2 | 7e-06 | 32/47 (NCI-H460, SHP-77, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.32×** | +5.2 | 9e-06 | 33/48 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **1.25×** | +4.2 | 9e-04 | 31/48 (NCI-H2030, AN3 CA, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1131.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **0.717×** | -6.2 | 3e-07 | 38/48 (CFPAC-1, NCI-H23, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.763×** | -5.0 | 1e-04 | 34/48 (HT-29, CFPAC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.761×** | -4.9 | 2e-04 | 29/44 (LS 180, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.770×** | -4.9 | 2e-04 | 26/49 (BT-474, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.769×** | -4.7 | 3e-04 | 38/48 (NCI-H23, AsPC-1, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.788×** | -4.1 | 0.004 | 28/48 (NCI-H23, AsPC-1, …) | all doses, flat |  |
| [[Larotrectinib (drug)]] 5 µM |  | 0.862× | -3.9 | 0.008 | 12/48 (LOX-IMVI, Hs 766T, …) | top dose only | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.810×** | -3.8 | 0.012 | 27/47 (NCI-H23, AsPC-1, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.842× | -3.7 | 0.012 | 18/48 (NCI-H23, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.824×** | -3.6 | 0.017 | 28/48 (LoVo, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.832×** | -3.6 | 0.017 | 21/50 (NCI-H23, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.870× | -3.6 | 0.017 | 10/48 (NCI-H23, AsPC-1, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.844× | -3.6 | 0.017 | 25/48 (NCI-H23, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.880× | -3.4 | 0.030 | 15/48 (NCI-H23, AsPC-1, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.831×** | -3.2 | 0.046 | 24/48 (NCI-H23, CFPAC-1, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.880× | -3.1 | 0.053 | 14/49 (NCI-H23, AsPC-1, …) | all doses, flat |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.830×** | -3.1 | 0.053 | 22/48 (NCI-H23, AsPC-1, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.848× | -3.1 | 0.066 | 21/49 (NCI-H23, AsPC-1, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1131. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 339 | 15 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.54× (z +24.3) | — |
| [[SW480 (line)]] | alt | 379 | 13 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.15× (z +19.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.15× (z +19.5) | — |
| [[KATO III (line)]] | alt | 656 | 12 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.36× (z +23.6) | — |
| [[HT-29 (line)]] | alt | 640 | 10 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.04× (z +17.4) | — |
| [[LS 180 (line)]] | wt | 334 | 9 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 3.14× (z +17.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.10× (z +16.8) | [[Dinaciclib (drug)]] 5 µM 0.525× (z -9.3) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 471 | 10 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.91× (z +22.9) | — |
| [[SNU-1 (line)]] | wt | 424 | 10 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.52× (z +22.1) | — |
| [[Hs 766T (line)]] | wt | 338 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.81× (z +27.9) | — |
| [[hTERT-HPNE (line)]] | wt | 461 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +24.0) | — |
| [[NCI-H23 (line)]] | alt | 686 | 6 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +16.2) | [[Trametinib (drug)]] 5 µM 0.532× (z -9.5) ⚠ cell-cycle shift, explains ~13% of this change · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.501× (z -9.5) |
| [[HS-578T (line)]] | alt | 477 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +17.7) | — |
| [[NCI-H1573 (line)]] | alt | 595 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +17.5) | — |
| [[SW 900 (line)]] | alt | 407 | 8 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.35× (z +16.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.31× (z +16.4) | — |
| [[AsPC-1 (line)]] | alt | 540 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +26.6) | — |
| [[HOP62 (line)]] | alt | 431 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +17.4) | — |
| [[LOX-IMVI (line)]] | wt | 457 | 7 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.18× (z +14.6) | — |
| [[H4 (line)]] | wt | 510 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.33× (z +12.4) | — |
| [[HEC-1-A (line)]] | alt | 483 | 6 | 0 | [[PH-797804 (drug)]] 5 µM 4.33× (z +14.1) | — |
| [[HepG2_C3A (line)]] | wt | 347 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.15× (z +20.1) | — |
| [[J82 (line)]] | alt | 521 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +16.1) | — |
| [[LoVo (line)]] | wt | 488 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +14.3) | — |
| [[NCI-H1792 (line)]] | alt | 363 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +14.7) | — |
| [[NCI-H2347 (line)]] | alt | 603 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +18.2) | — |
| [[Panc 03.27 (line)]] | alt | 607 | 6 | 0 | [[Auranofin (drug)]] 5 µM 2.36× (z +14.1) | — |
| [[SW1417 (line)]] | alt | 596 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.18× (z +18.6) | — |
| [[A-172 (line)]] | wt | 424 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +18.3) | — |
| [[A498 (line)]] | wt | 380 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +16.5) | — |
| [[BT-474 (line)]] | alt | 703 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.80× (z +14.5) | — |
| [[SHP-77 (line)]] | alt | 280 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.68× (z +13.4) | — |
| [[SNU-423 (line)]] | alt | 627 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +16.7) | — |
| [[SW48 (line)]] | wt | 426 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.03× (z +13.0) | — |
| [[C32 (line)]] | wt | 469 | 4 | 0 | [[Auranofin (drug)]] 5 µM 2.55× (z +10.0) | — |
| [[COLO 205 (line)]] | alt | 631 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +17.3) | — |
| [[NCI-H2030 (line)]] | alt | 409 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +14.0) | — |
| [[RPMI-7951 (line)]] | alt | 701 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +11.9) | — |
| [[SK-MEL-2 (line)]] | alt | 654 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +21.8) | — |
| [[A-427 (line)]] | wt | 736 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.01× (z +9.9) | — |
| [[CFPAC-1 (line)]] | alt | 606 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +13.9) | — |
| [[CHP-212 (line)]] | wt | 421 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.41× (z +9.1) | — |
| [[RKO (line)]] | wt | 658 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.23× (z +10.1) | — |
| [[AN3 CA (line)]] | alt | 510 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.90× (z +14.7) | — |
| [[C-33 A (line)]] | alt | 295 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.04× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[HCT15 (line)]] | alt | 539 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.55× (z +10.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 859 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +15.0) | — |
| [[A549 (line)]] | wt | 324 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 514 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 494 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 385 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 375 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 442 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1131), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP6V1D]] | +0.67 | +0.61 / +0.70 | both halves | 7e-06 |  |
| [[SLC9A1]] | +0.65 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[CLTA]] | +0.62 | +0.39 / +0.60 | both halves | 5e-05 | pathway: MHC class II antigen presentation |
| [[BIN3]] | +0.62 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[LRRC23]] | +0.62 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[SAP30BP]] | +0.60 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[GPATCH2L]] | +0.60 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[AXDND1]] | +0.59 | +0.30 / +0.58 | both halves | 2e-04 |  |
| [[NABP1]] | +0.58 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[RABGEF1]] | +0.58 | +0.55 / +0.52 | both halves | 1e-05 | pathway: RAB GEFs exchange GTP for GDP on RABs; STRING 420 |
| [[TTLL3]] | +0.58 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[MIR9-1HG]] | +0.57 | +0.40 / +0.52 | both halves | 5e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCTD3]] | -0.61 | -0.58 / -0.59 | both halves | 7e-06 | pathway: CDC42 GTPase cycle |
| [[FIP1L1]] | -0.60 | -0.52 / -0.64 | both halves | 1e-05 |  |
| [[NDUFAF5]] | -0.56 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[PROSER1]] | -0.55 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[MDM1]] | -0.53 | -0.38 / -0.59 | both halves | 6e-05 |  |
| [[AIFM1]] | -0.52 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[CASC3]] | -0.52 | -0.34 / -0.56 | both halves | 1e-04 |  |
| [[YEATS4]] | -0.51 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[TADA2A]] | -0.51 | -0.43 / -0.58 | both halves | 3e-05 |  |
| [[CAND1]] | -0.51 | -0.40 / -0.54 | both halves | 5e-05 |  |
| [[NSL1]] | -0.51 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[FOXJ2]] | -0.51 | -0.49 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF165]] | B | ZNF165 activity raises RAB7A's level | lines that do not express ZNF165 (19) vs lines expressing it (31) | 1.28× lower at baseline in the lines without ZNF165 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ENSG00000224621, ESRP2, CNKSR1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.542). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (30.1, -25.1); signed map (7.6, 15.8). **Vector** length 109, 48.6% of its response variance represented; |z| ≥ 3 in 1,598 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +10.6 | +12.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.1 | +6.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +5.9 | +2.7 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift | +5.1 | +2.6 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +4.6 | +3.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.9 | +0.4 |
|  | [[Entrectinib (drug)]] 5 µM |  | +3.7 | +0.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.6 | +2.0 |
|  | [[Belzutifan (drug)]] 5 µM |  | +3.4 | +0.6 |
| fall | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -5.1 | +1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.8 | -4.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.4 | +1.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.9 | -6.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.7 | +6.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.5 | -1.0 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -2.8 | -3.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.8 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | RAB7A, member RAS oncogene family |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q21.3 — chr3:128,693,669-128,825,942 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously RAB7, CMT2B |
| Gene groups (HGNC) | RAB, member RAS oncogene GTPases |
| Reactome | 31 pathways, smallest: Prevention of phagosomal-lysosomal fusion; Suppression of phagosomal maturation; Response of Mtb to phagocytosis |
| Matched by | ensembl_id |

**Function**, from UniProt [P51149](https://www.uniprot.org/uniprotkb/P51149) (Ras-related protein Rab-7a):

> The small GTPases Rab are key regulators of intracellular membrane trafficking, from the formation of transport vesicles to their fusion with membranes. Rabs cycle between an inactive GDP-bound form and an active GTP-bound form that is able to recruit to membranes different sets of downstream effectors directly responsible for vesicle formation, movement, tethering and fusion. In its active state, RAB7A binds to a variety of effector proteins playing a key role in the regulation of …

**Summary**, from NCBI Gene [7879](https://www.ncbi.nlm.nih.gov/gene/7879):

> RAB family members are small, RAS-related GTP-binding proteins that are important regulators of vesicular transport. Each RAB protein targets multiple proteins that act in exocytic / endocytic pathways. This gene encodes a RAB family member that regulates vesicle traffic in the late endosomes and also from late endosomes to lysosomes. This encoded protein is also involved in the cellular vacuolation of the VacA cytotoxin of Helicobacter pylori. Mutations at highly conserved amino acid residues …

**Accessions** — [HGNC:9788](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9788) · Entrez [7879](https://www.ncbi.nlm.nih.gov/gene/7879) · UniProt [P51149](https://www.uniprot.org/uniprotkb/P51149) · Ensembl [ENSG00000075785](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000075785)

## Data

Gene col 1131: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1131); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1131, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1131]; `tensor/DDL_lfc|DDL_z.npy` [1131]; `embed/gene_vectors.npy` [1131]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1131 or target_col == 1131). Every well: [[RAB7A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAB7A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
