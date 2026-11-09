---
symbol: "TAB3"
type: "gene"
col: 8091
ensembl_id: "ENSG00000157625"
name: "TGF-beta activated kinase 1 (MAP3K7) binding protein 3"
location: "Xp21.2"
module: 28
arm: "+"
pooled_cpm: 63.48
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 3
n_dd_up_clean: 9
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# TAB3

*TGF-beta activated kinase 1 (MAP3K7) binding protein 3* — Xp21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.15× (z +24.6, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.669× (z -9.2, q 3e-17, down in 37 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 3 lines (MIA PaCa-2 0.441×, SW480 0.543×, A-172 0.510×); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (H4 0.317×, BT-474 0.459×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (BT-474 0.246×; ⚠ toxic; cell-cycle shift, would explain all of this change); [[Canagliflozin (hemihydrate) (drug)]] 5 µM in 1 line (NCI-H596 0.155×); [[Methylthiouracil (drug)]] 0.05 µM in 1 line (NCI-H596 0.156×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC90B]] (+0.69, fdr 7e-06), [[CLN5]] (+0.66, fdr 7e-06), [[TRAPPC6B]] (+0.64, fdr 1e-05); moves opposite to [[SNRPA]] (-0.59, fdr 1e-05), [[TMEM97]] (-0.58, fdr 1e-05), [[PRIM2]] (-0.54, fdr 2e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠; shown: the 15 strongest. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8091.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.15×** | +24.6 | 0e+00 | 47/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.96×** | +14.7 | 0e+00 | 45/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.97×** | +12.9 | 6e-36 | 42/49 (A498, A-172, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.49×** | +9.1 | 1e-17 | 34/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.29×** | +8.2 | 4e-14 | 30/48 (A498, A-427, …) | all doses, flat | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.40×** | +7.6 | 2e-12 | 34/48 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.89×** | +7.6 | 3e-12 | 35/48 (A-172, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.37×** | +7.2 | 4e-11 | 38/49 (LOX-IMVI, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.32×** | +6.3 | 2e-08 | 32/48 (A-427, LOX-IMVI, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.30×** | +6.0 | 1e-07 | 24/48 (LoVo, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.25×** | +5.0 | 2e-05 | 25/48 (SW1417, LOX-IMVI, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.19× | +4.0 | 0.003 | 20/48 (LoVo, HOP62, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.18× | +3.7 | 0.010 | 17/48 (NCI-H460, A-427, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.5 | 0.019 | 19/48 (NCI-H460, A498, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | 1.16× | +3.3 | 0.031 | 12/49 (A549, A-172, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8091.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 3 lines (MIA PaCa-2 0.441×, SW480 0.543×, A-172 0.510×); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (H4 0.317×, BT-474 0.459×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (BT-474 0.246×; ⚠ toxic; cell-cycle shift, would explain all of this change); [[Canagliflozin (hemihydrate) (drug)]] 5 µM in 1 line (NCI-H596 0.155×); [[Methylthiouracil (drug)]] 0.05 µM in 1 line (NCI-H596 0.156×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.669×** | -9.2 | 3e-17 | 37/48 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.824×** | -4.2 | 0.008 | 20/49 (HCT15, NCI-H1573, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 0.882× | -4.0 | 0.010 | 12/48 (CFPAC-1, PANC-1, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.895× | -3.6 | 0.054 | 8/48 (Hs 766T, HCT15, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.753×** | -3.4 | 0.067 | 16/48 (MIA PaCa-2, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.863× | -3.4 | 0.067 | 10/48 (CFPAC-1, A498, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.863× | -3.3 | 0.067 | 11/48 (NCI-H460, LS 180, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.961× | -3.2 | 0.089 | 2/49 (SW 1088, NCI-H2122) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | 0.871× | -3.2 | 0.10 | 12/48 (CFPAC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | 0.773× | -3.1 | 0.12 | 10/48 (BT-474, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8091. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 72.0 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +21.2) | — |
| [[BT-474 (line)]] | alt | 163 | 2 | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +9.9) | [[Niclosamide (olamine) (drug)]] 5 µM 0.246× (z -14.6) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 32.1 | 6 (4 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 17.6× (z +14.8) | — |
| [[LoVo (line)]] | wt | 47.7 | 6 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.51× (z +14.4) | — |
| [[LS 180 (line)]] | wt | 63.3 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +17.1) | — |
| [[SW480 (line)]] | alt | 77.1 | 5 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +18.7) | [[Auranofin (drug)]] 5 µM 0.543× (z -9.2) |
| [[A-427 (line)]] | wt | 58.7 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +16.1) | — |
| [[A-172 (line)]] | wt | 113 | 3 (1 ⚠) | 1 | [[PH-797804 (drug)]] 5 µM 6.90× (z +12.8) | [[Auranofin (drug)]] 5 µM 0.510× (z -8.6) |
| [[PANC-1 (line)]] | alt | 30.8 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +21.3) | — |
| [[A549 (line)]] | wt | 87.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +11.7) | — |
| [[AsPC-1 (line)]] | alt | 62.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +9.6) | — |
| [[COLO 205 (line)]] | alt | 52.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +14.5) | — |
| [[HOP62 (line)]] | alt | 39.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +12.6) | — |
| [[HS-578T (line)]] | alt | 51.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +12.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 86.8 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 4.12× (z +8.8) | [[Auranofin (drug)]] 5 µM 0.441× (z -9.8) |
| [[NCI-H2030 (line)]] | alt | 45.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +16.7) | — |
| [[NCI-H596 (line)]] | alt | 64.6 | 0 | 2 | — | [[Canagliflozin (hemihydrate) (drug)]] 5 µM 0.155× (z -12.1) |
| [[RKO (line)]] | wt | 54.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +10.7) | — |
| [[RPMI-7951 (line)]] | alt | 76.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +11.4) | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0986× (z -12.4) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 105 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +12.1) | — |
| [[C-33 A (line)]] | alt | 37.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +10.1) | — |
| [[CFPAC-1 (line)]] | alt | 76.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +12.9) | — |
| [[CHP-212 (line)]] | wt | 58.9 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.131× (z -9.6) |
| [[H4 (line)]] | wt | 58.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.317× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 53.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +12.9) | — |
| [[Hs 766T (line)]] | wt | 81.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +10.6) | — |
| [[HT-29 (line)]] | alt | 33.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.24× (z +18.0) | — |
| [[J82 (line)]] | alt | 50.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +12.6) | — |
| [[KATO III (line)]] | alt | 76.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +13.3) | — |
| [[NCI-H1573 (line)]] | alt | 83.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +12.8) | — |
| [[NCI-H1792 (line)]] | alt | 54.9 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 2.99× (z +9.4) | — |
| [[NCI-H23 (line)]] | alt | 42.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +8.6) | — |
| [[NCI-H2347 (line)]] | alt | 71.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +15.7) | — |
| [[Panc 03.27 (line)]] | alt | 90.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +10.9) | — |
| [[SK-MEL-2 (line)]] | alt | 58.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +10.4) | — |
| [[SNU-1 (line)]] | wt | 40.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +9.8) | — |
| [[SW 900 (line)]] | alt | 40.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +9.0) | — |
| [[SW1417 (line)]] | alt | 123 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +13.0) | — |
| [[SW48 (line)]] | wt | 43.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +9.8) | — |
| [[AN3 CA (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 56.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 60.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 75.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 54.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 70.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 67.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 73.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 48.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8091), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC90B]] | +0.69 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[CLN5]] | +0.66 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[TRAPPC6B]] | +0.64 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[AMZ2]] | +0.63 | +0.57 / +0.58 | both halves | 8e-06 |  |
| [[CREBL2]] | +0.61 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[RRM2B]] | +0.60 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[ETFRF1]] | +0.59 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[TRIM8]] | +0.59 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[CHMP4B]] | +0.58 | +0.50 / +0.56 | both halves | 1e-05 | pathway: SARS-CoV-2 Infection |
| [[TNKS2]] | +0.58 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[IFT46]] | +0.58 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[ZSCAN21]] | +0.57 | +0.53 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNRPA]] | -0.59 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[TMEM97]] | -0.58 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[PRIM2]] | -0.54 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[TUFM]] | -0.53 | -0.55 / -0.43 | both halves | 3e-05 | pathway: SARS-CoV-2 Infection |
| [[RRP7BP-1]] | -0.52 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[FARP2]] | -0.52 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[FANCA]] | -0.52 | -0.62 / -0.41 | both halves | 4e-05 |  |
| [[FANCC]] | -0.52 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[PPCDC]] | -0.52 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[RNF216]] | -0.51 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[SPATA5]] | -0.51 | -0.60 / -0.35 | both halves | 1e-04 |  |
| [[KPNB1]] | -0.50 | -0.46 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.533). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-20.8, 21.3); signed map (18.6, -17.5). **Vector** length 99.9, 24.5% of its response variance represented; |z| ≥ 3 in 1,055 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | +7.7 | +8.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.2 | +14.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.8 | +24.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | +5.9 | +6.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.8 | +12.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.3 | +7.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.9 | +3.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.5 | +5.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.1 | +1.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +2.4 |
| fall | [[Auranofin (drug)]] 5 µM |  | -8.1 | -9.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.7 | -2.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.9 | -0.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | +0.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.1 | -0.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.7 | -3.4 |
|  | [[EX229 (drug)]] 5 µM |  | -2.7 | -2.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.5 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | TGF-beta activated kinase 1 (MAP3K7) binding protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp21.2 — chrX:30,827,442-30,975,084 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously MAP3K7IP3 |
| Gene groups (HGNC) | Zinc fingers RANBP2-type; CUE domain containing |
| Reactome | 45 pathways, smallest: IRAK2 mediated activation of TAK1 complex; Alpha-protein kinase 1 signaling pathway; TICAM1,TRAF6-dependent induction of TAK1 complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N5C8](https://www.uniprot.org/uniprotkb/Q8N5C8) (TGF-beta-activated kinase 1 and MAP3K7-binding protein 3):

> Adapter required to activate the JNK and NF-kappa-B signaling pathways through the specific recognition of 'Lys-63'-linked polyubiquitin chains by its RanBP2-type zinc finger (NZF). Acts as an adapter linking MAP3K7/TAK1 and TRAF6 to 'Lys-63'-linked polyubiquitin chains. The RanBP2-type zinc finger (NZF) specifically recognizes 'Lys-63'-linked polyubiquitin chains unanchored or anchored to the substrate proteins such as RIPK1/RIP1 and RIPK2: this acts as a scaffold to organize a large signaling …

**Summary**, from NCBI Gene [257397](https://www.ncbi.nlm.nih.gov/gene/257397):

> The product of this gene functions in the NF-kappaB signal transduction pathway. The encoded protein, and the similar and functionally redundant protein MAP3K7IP2/TAB2, forms a ternary complex with the protein kinase MAP3K7/TAK1 and either TRAF2 or TRAF6 in response to stimulation with the pro-inflammatory cytokines TNF or IL-1. Subsequent MAP3K7/TAK1 kinase activity triggers a signaling cascade leading to activation of the NF-kappaB transcription factor. The human genome contains a related …

**Accessions** — [HGNC:30681](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30681) · Entrez [257397](https://www.ncbi.nlm.nih.gov/gene/257397) · UniProt [Q8N5C8](https://www.uniprot.org/uniprotkb/Q8N5C8) · Ensembl [ENSG00000157625](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157625)

## Data

Gene col 8091: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8091); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8091, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8091]; `tensor/DDL_lfc|DDL_z.npy` [8091]; `embed/gene_vectors.npy` [8091]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8091 or target_col == 8091). Every well: [[TAB3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TAB3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
