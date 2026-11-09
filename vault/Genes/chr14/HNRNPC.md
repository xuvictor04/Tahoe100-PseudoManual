---
symbol: "HNRNPC"
type: "gene"
col: 1693
ensembl_id: "ENSG00000092199"
name: "heterogeneous nuclear ribonucleoprotein C"
location: "14q11.2"
module: 3
arm: "-"
pooled_cpm: 634.59
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 7
n_dd_up_clean: 9
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# HNRNPC

*heterogeneous nuclear ribonucleoprotein C* — 14q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.88× (z +30.8, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Ponatinib (drug)]] 5 µM: 0.756× (z -5.8, q 4e-06, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SFPQ]] (+0.63, fdr 5e-05), [[YWHAE]] (+0.62, fdr 1e-05), [[LINC00641]] (+0.60, fdr 6e-05, ⚠ read-through risk), [[ETF1]] (+0.58, fdr 7e-06); moves opposite to [[ARL8A]] (-0.65, fdr 3e-05), [[BAHD1]] (-0.58, fdr 1e-04), [[RP9P]] (-0.58, fdr 1e-05).
> It sits in the **-** arm of [[Module 003]] (mRNA 3'-end processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1693.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.88×** | +30.8 | 0e+00 | 46/48 (HS-578T, J82, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **5.42×** | +17.3 | 0e+00 | 49/49 (HS-578T, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **2.00×** | +13.8 | 8e-41 | 46/48 (HS-578T, J82, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.93×** | +13.5 | 2e-39 | 48/48 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **3.73×** | +13.5 | 3e-39 | 48/48 (HEC-1-A, LS 180, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.64×** | +10.2 | 1e-22 | 37/49 (NCI-H460, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.61×** | +9.8 | 1e-20 | 41/48 (HS-578T, A-172, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.58×** | +9.4 | 4e-19 | 44/48 (NCI-H460, SW480, …) | two highest doses | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.60×** | +8.9 | 3e-17 | 35/45 (A-172, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.53×** | +8.8 | 6e-17 | 45/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.53×** | +8.7 | 1e-16 | 41/48 (NCI-H460, LS 180, …) | two highest doses | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.38×** | +6.4 | 7e-09 | 29/44 (A549, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~19% of this change | **1.34×** | +5.8 | 4e-07 | 34/47 (COLO 205, A-172, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.25×** | +4.6 | 1e-04 | 31/48 (NCI-H460, SNU-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.23×** | +4.2 | 9e-04 | 28/48 (SNU-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.19× | +3.6 | 0.011 | 21/48 (HT-29, PANC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.12× | +3.3 | 0.025 | 11/48 (A-172, NCI-H661, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1693.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **0.756×** | -5.8 | 4e-06 | 37/48 (J82, PANC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.767×** | -5.5 | 1e-05 | 38/48 (SW48, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.727×** | -4.7 | 5e-04 | 42/47 (SW1417, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.812×** | -4.3 | 0.002 | 31/48 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.873× | -4.0 | 0.008 | 22/49 (A549, CHP-212, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 0.883× | -3.6 | 0.028 | 8/48 (A-427, RKO, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.786×** | -3.6 | 0.031 | 35/48 (SW 900, SW1417, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | 0.891× | -3.4 | 0.056 | 11/48 (LS 180, RKO, …) | top dose only | low cells (technical?) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.801×** | -3.3 | 0.070 | 33/48 (LoVo, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.808×** | -3.1 | 0.094 | 30/48 (HCT15, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1693. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 596 | 15 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +29.1) | — |
| [[A-172 (line)]] | wt | 287 | 11 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.22× (z +30.7) | — |
| [[HS-578T (line)]] | alt | 356 | 11 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +33.1) | — |
| [[PANC-1 (line)]] | alt | 570 | 11 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +23.9) | — |
| [[SW480 (line)]] | alt | 630 | 10 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.22× (z +15.5) | — |
| [[A549 (line)]] | wt | 659 | 8 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +23.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.571× (z -12.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 576 | 9 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.36× (z +30.3) | — |
| [[LOX-IMVI (line)]] | wt | 555 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +24.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 679 | 9 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +19.9) | — |
| [[SNU-1 (line)]] | wt | 533 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +22.6) | — |
| [[A498 (line)]] | wt | 555 | 8 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +25.6) | — |
| [[BT-474 (line)]] | alt | 1,092 | 7 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +23.8) | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.426× (z -13.8) ⚠ cell-cycle shift, explains ~13% of this change |
| [[LoVo (line)]] | wt | 669 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +23.8) | — |
| [[LS 180 (line)]] | wt | 576 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +18.5) | — |
| [[NCI-H1573 (line)]] | alt | 689 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +21.2) | — |
| [[AsPC-1 (line)]] | alt | 460 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.04× (z +29.2) | — |
| [[COLO 205 (line)]] | alt | 694 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +22.9) | — |
| [[H4 (line)]] | wt | 563 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +21.7) | — |
| [[HEC-1-A (line)]] | alt | 688 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +21.4) | — |
| [[RKO (line)]] | wt | 789 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +14.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.665× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 579 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +23.8) | — |
| [[SW1417 (line)]] | alt | 515 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +16.8) | — |
| [[SW48 (line)]] | wt | 691 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +14.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.645× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 540 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.27× (z +31.1) | — |
| [[KATO III (line)]] | alt | 468 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.03× (z +16.3) | — |
| [[NCI-H23 (line)]] | alt | 781 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +16.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.632× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 503 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +24.2) | — |
| [[SK-MEL-2 (line)]] | alt | 457 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +30.2) | — |
| [[Hs 766T (line)]] | wt | 406 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.69× (z +26.2) | — |
| [[HT-29 (line)]] | alt | 513 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +19.6) | — |
| [[J82 (line)]] | alt | 591 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +32.7) | — |
| [[NCI-H1792 (line)]] | alt | 713 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.20× (z +23.5) | — |
| [[NCI-H2347 (line)]] | alt | 926 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +17.4) | — |
| [[Panc 03.27 (line)]] | alt | 796 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +22.8) | — |
| [[A-427 (line)]] | wt | 560 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.08× (z +12.6) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 3.30× (z +10.1) | — |
| [[C32 (line)]] | wt | 467 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +21.8) | — |
| [[HCT15 (line)]] | alt | 830 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +17.0) | — |
| [[NCI-H2030 (line)]] | alt | 1,116 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +14.5) | — |
| [[SNU-423 (line)]] | alt | 634 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +26.4) | — |
| [[C-33 A (line)]] | alt | 697 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 3.22× (z +9.5) | — |
| [[CFPAC-1 (line)]] | alt | 1,145 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +22.0) | — |
| [[CHP-212 (line)]] | wt | 713 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.543× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 469 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +12.6) | — |
| [[AN3 CA (line)]] | alt | 577 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +15.6) | — |
| [[SHP-77 (line)]] | alt | 540 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.69× (z +8.5) | — |
| [[SW 1088 (line)]] | alt | 554 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +13.2) | — |
| [[SW 1271 (line)]] | alt | 568 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.12× (z +16.8) | — |
| [[NCI-H2122 (line)]] | alt | 669 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 609 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 576 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1693), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*38 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SFPQ]] | +0.63 | +0.40 / +0.68 | both halves | 5e-05 | same gene group; STRING 926 |
| [[YWHAE]] | +0.62 | +0.51 / +0.64 | both halves | 1e-05 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 702 |
| [[LINC00641]] | +0.60 | +0.38 / +0.68 | both halves | 6e-05 | ⚠ **readthrough risk**: LINC00641 lies 2.2 kb 3′ of this gene on the same strand (can correlate by spillover, not regulation) |
| [[ETF1]] | +0.58 | +0.61 / +0.58 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[EWSR1]] | +0.58 | +0.37 / +0.68 | both halves | 8e-05 | same gene group; STRING 836 |
| [[SRSF3]] | +0.57 | +0.50 / +0.60 | both halves | 1e-05 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 981 |
| [[DDX3X]] | +0.57 | +0.50 / +0.64 | both halves | 1e-05 | pathway: Dengue Virus-Host Interactions; STRING 785 |
| [[BCLAF1]] | +0.55 | +0.56 / +0.62 | both halves | 1e-05 | STRING 643 |
| [[PBRM1]] | +0.55 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[SMU1]] | +0.54 | +0.55 / +0.53 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 587 |
| [[SF1]] | +0.54 | +0.28 / +0.65 | both halves | 3e-04 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 560 |
| [[HUWE1]] | +0.54 | +0.36 / +0.61 | both halves | 9e-05 |  |
| [[CDC42]] | +0.53 | +0.28 / +0.59 | both halves | 3e-04 |  |

## Genes that move opposite

*62 of its nearest partners move opposite, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARL8A]] | -0.65 | -0.45 / -0.70 | both halves | 3e-05 |  |
| [[BAHD1]] | -0.58 | -0.35 / -0.62 | both halves | 1e-04 |  |
| [[RP9P]] | -0.58 | -0.52 / -0.62 | both halves | 1e-05 |  |
| [[CDAN1]] | -0.57 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[C8orf76]] | -0.57 | -0.33 / -0.65 | both halves | 1e-04 |  |
| [[SAP30L]] | -0.56 | -0.38 / -0.63 | both halves | 6e-05 |  |
| [[TRAPPC4]] | -0.56 | -0.34 / -0.63 | both halves | 1e-04 |  |
| [[COMMD5]] | -0.55 | -0.31 / -0.62 | both halves | 2e-04 |  |
| [[SLC35D2]] | -0.54 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[IL17RA]] | -0.54 | -0.30 / -0.64 | both halves | 2e-04 |  |
| [[CDC34]] | -0.54 | -0.40 / -0.65 | both halves | 5e-05 |  |
| [[RAB11FIP5]] | -0.54 | -0.37 / -0.59 | both halves | 7e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **-** arm (projection on the module's main direction -0.565). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-37.5, -23.9); signed map (15.9, -39.2). **Vector** length 117, 47.9% of its response variance represented; |z| ≥ 3 in 1,316 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.6 | +10.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +7.1 | +6.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.4 | +8.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +3.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | +1.2 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | +3.0 | +2.0 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | +2.8 | +0.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.4 | -0.7 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +2.3 | +1.7 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -9.1 | -5.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -7.3 | -4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -7.2 | -1.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | -5.3 | -1.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -5.1 | -1.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -4.4 | -4.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -4.4 | -2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.3 | +0.3 |
|  | [[vincristine (drug)]] 0.5 µM |  | -4.3 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | heterogeneous nuclear ribonucleoprotein C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q11.2 — chr14:21,209,136-21,269,494 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously HNRPC |
| Gene groups (HGNC) | RNA binding motif containing; Spliceosomal C complex; Spliceosomal P complex; Heterogeneous nuclear ribonucleoproteins |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 18 pathways, smallest: RHOBTB1 GTPase cycle; RHOBTB2 GTPase cycle; RHOBTB GTPase Cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [P07910](https://www.uniprot.org/uniprotkb/P07910) (Heterogeneous nuclear ribonucleoproteins C1/C2):

> Binds pre-mRNA and nucleates the assembly of 40S hnRNP particles. Interacts with poly-U tracts in the 3'-UTR or 5'-UTR of mRNA and modulates the stability and the level of translation of bound mRNA molecules. Single HNRNPC tetramers bind 230-240 nucleotides. Trimers of HNRNPC tetramers bind 700 nucleotides. May play a role in the early steps of spliceosome assembly and pre-mRNA splicing. N6-methyladenosine (m6A) has been shown to alter the local structure in mRNAs and long non-coding RNAs …

**Summary**, from NCBI Gene [3183](https://www.ncbi.nlm.nih.gov/gene/3183):

> This gene belongs to the subfamily of ubiquitously expressed heterogeneous nuclear ribonucleoproteins (hnRNPs). The hnRNPs are RNA binding proteins and they complex with heterogeneous nuclear RNA (hnRNA). These proteins are associated with pre-mRNAs in the nucleus and appear to influence pre-mRNA processing and other aspects of mRNA metabolism and transport. While all of the hnRNPs are present in the nucleus, some seem to shuttle between the nucleus and the cytoplasm. The hnRNP proteins have …

**Accessions** — [HGNC:5035](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5035) · Entrez [3183](https://www.ncbi.nlm.nih.gov/gene/3183) · UniProt [P07910](https://www.uniprot.org/uniprotkb/P07910) · Ensembl [ENSG00000092199](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000092199)

## Data

Gene col 1693: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1693); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1693, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1693]; `tensor/DDL_lfc|DDL_z.npy` [1693]; `embed/gene_vectors.npy` [1693]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1693 or target_col == 1693). Every well: [[HNRNPC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HNRNPC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
