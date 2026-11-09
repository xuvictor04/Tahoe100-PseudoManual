---
symbol: "FYTTD1"
type: "gene"
col: 4319
ensembl_id: "ENSG00000122068"
name: "forty-two-three domain containing 1"
location: "3q29"
module: 28
arm: "+"
pooled_cpm: 80.95
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# FYTTD1

*forty-two-three domain containing 1* — 3q29

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.26× (z +15.9, q 0e+00, up in 45 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.92× (z +12.8, q 4e-35, up in 43 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-172 0.509×, A-427 0.592×; ⚠ cell-cycle shift, explains ~50% of this change); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (SW48 0.417×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMARCA5]] (+0.57, fdr 1e-05), [[EXOC5]] (+0.54, fdr 1e-05), [[MRPS10]] (+0.53, fdr 4e-05); moves opposite to [[SFT2D1]] (-0.48, fdr 4e-05), [[DMC1]] (-0.45, fdr 8e-05), [[RFWD3]] (-0.45, fdr 4e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MYO5A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 13 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4319.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.26×** | +15.9 | 0e+00 | 45/49 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.21×** | +14.9 | 0e+00 | 41/44 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.92×** | +12.8 | 4e-35 | 43/48 (MIA PaCa-2, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.42×** | +9.8 | 2e-20 | 33/48 (CFPAC-1, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.62×** | +8.7 | 3e-16 | 36/45 (SNU-423, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.51×** | +8.1 | 4e-14 | 37/48 (PANC-1, CFPAC-1, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.49×** | +7.8 | 6e-13 | 43/48 (HOP62, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.49×** | +7.7 | 7e-13 | 37/48 (LS 180, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.44×** | +7.2 | 5e-11 | 38/48 (MIA PaCa-2, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.42×** | +6.8 | 4e-10 | 35/48 (LOX-IMVI, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.36×** | +5.9 | 1e-07 | 33/48 (LOX-IMVI, HOP62, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **1.35×** | +5.7 | 5e-07 | 29/47 (HOP62, hTERT-HPNE, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.31×** | +5.3 | 5e-06 | 24/48 (LOX-IMVI, LS 180, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~47% of this change | **1.30×** | +5.1 | 1e-05 | 28/48 (SW1417, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.28×** | +4.8 | 6e-05 | 30/48 (PANC-1, CFPAC-1, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.27×** | +4.6 | 1e-04 | 28/48 (MIA PaCa-2, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.27×** | +4.3 | 6e-04 | 26/48 (HOP62, LS 180, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.21×** | +3.8 | 0.005 | 20/48 (CFPAC-1, HOP62, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.14× | +3.7 | 0.006 | 13/49 (CFPAC-1, HOP62, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.05 µM |  | 1.20× | +3.6 | 0.009 | 15/48 (HOP62, LS 180, …) | all doses, stronger at high dose |  |
| [[AZD-7648 (drug)]] 0.5 µM |  | **1.28×** | +3.4 | 0.014 | 17/48 (KATO III, J82, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.19× | +3.4 | 0.014 | 18/47 (HOP62, NCI-H23, …) | inconsistent across doses |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-172 0.509×, A-427 0.592×; ⚠ cell-cycle shift, explains ~50% of this change); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (SW48 0.417×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4319. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 71.7 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.42× (z +15.2) | — |
| [[HOP62 (line)]] | alt | 58.8 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.50× (z +13.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.48× (z +9.9) | — |
| [[PANC-1 (line)]] | alt | 109 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +14.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.29× (z +11.0) | — |
| [[HEC-1-A (line)]] | alt | 94.0 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.07× (z +14.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.92× (z +8.5) | — |
| [[KATO III (line)]] | alt | 92.7 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.97× (z +13.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.04× (z +8.8) | — |
| [[SNU-423 (line)]] | alt | 62.5 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.86× (z +12.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.49× (z +8.5) | — |
| [[SW480 (line)]] | alt | 125 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.13× (z +15.4) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 34.4 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.48× (z +9.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.25× (z +8.5) | — |
| [[SW1417 (line)]] | alt | 88.1 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +10.5) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.12× (z +10.0) | — |
| [[A-172 (line)]] | wt | 113 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.74× (z +10.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.509× (z -10.2) ⚠ cell-cycle shift, explains ~50% of this change |
| [[A-427 (line)]] | wt | 90.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.10× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.592× (z -8.8) ⚠ cell-cycle shift, explains ~50% of this change |
| [[A549 (line)]] | wt | 55.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.16× (z +11.5) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 52.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.17× (z +10.6) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 66.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +15.0) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.71× (z +14.0) | — |
| [[COLO 205 (line)]] | alt | 59.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.92× (z +10.4) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 41.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.14× (z +12.1) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 73.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +11.7) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.21× (z +8.6) | — |
| [[J82 (line)]] | alt | 114 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.85× (z +12.5) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 55.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.29× (z +11.0) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 60.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.51× (z +11.9) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 111 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.08× (z +9.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.07× (z +9.0) | — |
| [[AsPC-1 (line)]] | alt | 48.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +10.1) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[HCT15 (line)]] | alt | 76.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.33× (z +9.7) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 150 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.59× (z +9.6) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 63.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.80× (z +10.9) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 49.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.67× (z +10.7) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 102 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.14× (z +8.6) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 96.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.27× (z +13.8) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 91.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.00× (z +10.6) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 46.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.51× (z +10.3) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 72.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.79× (z +10.2) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 88.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +8.9) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[SW 900 (line)]] | alt | 49.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +8.7) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[SW48 (line)]] | wt | 112 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.417× (z -8.5) |
| [[A498 (line)]] | wt | 63.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 72.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 86.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 58.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 71.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 65.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 58.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 72.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 75.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 72.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 77.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 55.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 100.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4319), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMARCA5]] | +0.57 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[EXOC5]] | +0.54 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[MRPS10]] | +0.53 | +0.56 / +0.42 | both halves | 4e-05 |  |
| [[SH3GLB1]] | +0.50 | +0.39 / +0.49 | both halves | 6e-05 |  |
| [[FAM114A2]] | +0.49 | +0.54 / +0.36 | both halves | 9e-05 |  |
| [[ANXA7]] | +0.48 | +0.52 / +0.42 | both halves | 4e-05 |  |
| [[DCTN2]] | +0.48 | +0.52 / +0.40 | both halves | 5e-05 |  |
| [[RNF2]] | +0.48 | +0.40 / +0.36 | both halves | 9e-05 |  |
| [[MYO5A]] | +0.47 | +0.36 / +0.44 | both halves | 1e-04 |  |
| [[DYNC1LI2]] | +0.47 | +0.38 / +0.45 | both halves | 7e-05 |  |
| [[MTMR6]] | +0.47 | +0.51 / +0.40 | both halves | 5e-05 |  |
| [[SNX18]] | +0.47 | +0.45 / +0.40 | both halves | 4e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SFT2D1]] | -0.48 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[DMC1]] | -0.45 | -0.38 / -0.37 | both halves | 8e-05 |  |
| [[RFWD3]] | -0.45 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[HROB]] | -0.45 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[INTS9]] | -0.44 | -0.36 / -0.41 | both halves | 1e-04 |  |
| [[RAD54L]] | -0.43 | -0.52 / -0.38 | both halves | 7e-05 |  |
| [[EVI2B]] | -0.43 | -0.38 / -0.33 | both halves | 1e-04 |  |
| [[MIRLET7A1HG]] | -0.43 | -0.38 / -0.43 | both halves | 6e-05 |  |
| [[GINS4]] | -0.43 | -0.48 / -0.32 | both halves | 2e-04 |  |
| [[SUZ12P1]] | -0.43 | -0.42 / -0.30 | both halves | 2e-04 |  |
| [[ASF1B]] | -0.42 | -0.44 / -0.33 | both halves | 1e-04 |  |
| [[FBXW9]] | -0.42 | -0.19 / -0.51 | ⚠ one half (not replicated) | 8e-04 |  |
| [[CENPO]] | -0.42 | -0.48 / -0.32 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYO5A]] | B | MYO5A activity raises FYTTD1's level | lines that do not express MYO5A (6) vs lines expressing it (44) | 1.17× lower at baseline in the lines without MYO5A | 0.095 | ⚠ within organs, on part of the lines; also absent: TPST1, CYP46A1, CSRP2 |
| [[SOGA3]] | B | SOGA3 activity raises FYTTD1's level | lines that do not express SOGA3 (21) vs lines expressing it (29) | 1.12× lower at baseline in the lines without SOGA3 | 0.099 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: KIAA0408, ENSG00000255330, RFTN1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.286). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-25.0, -15.9); signed map (-5.1, -35.5). **Vector** length 97.6, 26.2% of its response variance represented; |z| ≥ 3 in 1,049 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +4.2 | +7.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.4 | +2.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.4 | +12.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.3 | +5.9 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | +0.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +4.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.2 | +0.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.2 | +2.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.8 | +2.2 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -8.3 | -0.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -5.4 | -1.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~3% of this change | -5.2 | +3.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.1 | -0.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.0 | -1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.6 | -2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -4.0 | -2.5 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -2.6 | -1.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.6 | -0.3 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.4 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | forty-two-three domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q29 — chr3:197,737,179-197,787,596 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp761B1514, UIF |
| Gene groups (HGNC) | Transcription and export complex 1 subunits |
| Reactome | 5 pathways, smallest: Transport of Mature mRNA derived from an Intron-Containing Transcript; Transport of Mature Transcript to Cytoplasm; mRNA 3'-end processing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96QD9](https://www.uniprot.org/uniprotkb/Q96QD9) (UAP56-interacting factor):

> Required for mRNA export from the nucleus to the cytoplasm. Acts as an adapter that uses the DDX39B/UAP56-NFX1 pathway to ensure efficient mRNA export and delivering to the nuclear pore. Associates with spliced and unspliced mRNAs simultaneously with ALYREF/THOC4.

**Summary**, from NCBI Gene [84248](https://www.ncbi.nlm.nih.gov/gene/84248):

> Enables mRNA binding activity. Involved in mRNA export from nucleus. Located in nuclear speck. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25407](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25407) · Entrez [84248](https://www.ncbi.nlm.nih.gov/gene/84248) · UniProt [Q96QD9](https://www.uniprot.org/uniprotkb/Q96QD9) · Ensembl [ENSG00000122068](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122068)

## Data

Gene col 4319: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4319); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4319, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4319]; `tensor/DDL_lfc|DDL_z.npy` [4319]; `embed/gene_vectors.npy` [4319]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4319 or target_col == 4319). Every well: [[FYTTD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FYTTD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
