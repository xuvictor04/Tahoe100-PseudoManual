---
symbol: "STAT1"
type: "gene"
col: 3671
ensembl_id: "ENSG00000115415"
name: "signal transducer and activator of transcription 1"
location: "2q32.2"
module: 32
arm: "+"
pooled_cpm: 381.03
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 48
n_dd_up_clean: 23
n_dd_down_clean: 39
in_vector_space: true
direction_upstream: 36
direction_downstream: 44
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# STAT1

*signal transducer and activator of transcription 1* — 2q32.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (4 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 1.82× (z +8.8, q 6e-16, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 48 drug-doses (9 with an alert ⚠); the strongest is [[Tofacitinib (drug)]] 5 µM: 0.361× (z -21.2, q 0e+00, down in 38 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OAS3]] (+0.93, fdr 7e-06), [[MX1]] (+0.92, fdr 7e-06), [[RIGI]] (+0.91, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 36 arrows point to it, the strongest [[OAS2]] → it (grade B ⚠); 44 go from it, the strongest it → [[ADAR]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3671.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **1.82×** | +8.8 | 6e-16 | 35/48 (C32, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.48×** | +8.2 | 8e-14 | 29/48 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.69×** | +7.8 | 1e-12 | 31/48 (SW480, HOP62, …) | two highest doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.68×** | +7.4 | 2e-11 | 35/48 (NCI-H460, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~5% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.55×** | +6.5 | 1e-08 | 29/48 (SW480, HOP62, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.49×** | +5.9 | 4e-07 | 32/48 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.44×** | +5.2 | 1e-05 | 35/47 (J82, AsPC-1, …) | rises with dose |  |
| [[Berbamine (drug)]] 0.05 µM |  | **1.31×** | +4.1 | 0.004 | 29/48 (J82, Panc 03.27, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.29×** | +3.8 | 0.008 | 30/47 (AsPC-1, Hs 766T, …) | rises with dose |  |
| [[venetoclax (drug)]] 0.05 µM |  | **1.33×** | +3.8 | 0.008 | 28/49 (J82, Hs 766T, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 5 µM |  | 1.20× | +3.8 | 0.008 | 24/48 (HS-578T, AsPC-1, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.29×** | +3.7 | 0.009 | 26/48 (SW 900, NCI-H1792, …) | inconsistent across doses |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | **1.27×** | +3.6 | 0.014 | 30/48 (NCI-H1792, CHP-212, …) | top dose only |  |
| [[Omeprazole (drug)]] 0.05 µM |  | **1.27×** | +3.5 | 0.017 | 24/48 (A-172, CFPAC-1, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.28×** | +3.5 | 0.017 | 24/48 (AsPC-1, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.20×** | +3.5 | 0.019 | 22/48 (AsPC-1, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Apalutamide (drug)]] 0.5 µM |  | **1.25×** | +3.3 | 0.033 | 22/48 (A498, NCI-H1792, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 52 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 48 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3671.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tofacitinib (drug)]] 5 µM |  | **0.361×** | -21.2 | 0e+00 | 38/49 (RPMI-7951, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.450×** | -16.6 | 0e+00 | 38/49 (RPMI-7951, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.391×** | -13.8 | 4e-41 | 40/48 (BT-474, A-172, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.530×** | -13.2 | 1e-37 | 38/48 (CFPAC-1, SNU-423, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.420×** | -12.7 | 4e-35 | 37/49 (NCI-H1573, BT-474, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.453×** | -11.6 | 3e-29 | 34/49 (A549, RPMI-7951, …) | rises with dose |  |
| [[Ixazomib (drug)]] 5 µM |  | **0.343×** | -8.2 | 1e-14 | 35/48 (RPMI-7951, NCI-H1573, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.577×** | -8.1 | 5e-14 | 30/48 (LoVo, NCI-H23, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.568×** | -8.0 | 8e-14 | 32/47 (LoVo, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.683×** | -7.9 | 2e-13 | 39/49 (NCI-H1573, RKO, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.579×** | -7.7 | 7e-13 | 33/47 (RPMI-7951, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.613×** | -7.2 | 3e-11 | 35/48 (BT-474, SNU-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.615×** | -7.1 | 5e-11 | 33/48 (LoVo, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.613×** | -6.4 | 6e-09 | 33/48 (MIA PaCa-2, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.655×** | -6.2 | 2e-08 | 38/48 (NCI-H1573, NCI-H23, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.675×** | -5.8 | 3e-07 | 34/48 (LoVo, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.675×** | -5.8 | 3e-07 | 29/48 (LoVo, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.691×** | -5.4 | 2e-06 | 26/48 (LoVo, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3671. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 682 | 0 | 21 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -19.3) |
| [[LoVo (line)]] | wt | 580 | 0 | 18 (5 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.250× (z -19.5) |
| [[NCI-H1573 (line)]] | alt | 568 | 1 | 14 (2 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.36× (z +8.7) | [[Tofacitinib (drug)]] 5 µM 0.308× (z -16.9) |
| [[NCI-H23 (line)]] | alt | 661 | 0 | 15 (2 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.348× (z -16.0) |
| [[A-172 (line)]] | wt | 626 | 3 | 11 (4 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.82× (z +10.8) | [[Tofacitinib (drug)]] 5 µM 0.267× (z -19.5) |
| [[BT-474 (line)]] | alt | 473 | 0 | 14 (4 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.228× (z -18.7) |
| [[RPMI-7951 (line)]] | alt | 870 | 1 | 13 (4 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.32× (z +9.4) | [[Tofacitinib (drug)]] 5 µM 0.215× (z -24.2) |
| [[A549 (line)]] | wt | 789 | 0 | 11 (3 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.201× (z -20.8) |
| [[AsPC-1 (line)]] | alt | 352 | 3 | 8 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +13.4) | [[Tofacitinib (drug)]] 5 µM 0.324× (z -15.9) |
| [[HEC-1-A (line)]] | alt | 136 | 11 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +15.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 759 | 2 | 9 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +11.7) | [[Tofacitinib (drug)]] 5 µM 0.176× (z -20.1) |
| [[NCI-H1792 (line)]] | alt | 397 | 0 | 11 (2 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.211× (z -19.2) |
| [[C-33 A (line)]] | alt | 986 | 0 | 10 (3 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.206× (z -19.2) |
| [[CFPAC-1 (line)]] | alt | 562 | 3 | 7 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 3.79× (z +13.3) | [[Tofacitinib (drug)]] 5 µM 0.224× (z -21.9) |
| [[HS-578T (line)]] | alt | 480 | 3 | 7 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.58× (z +13.1) | [[Tofacitinib (drug)]] 5 µM 0.314× (z -16.7) |
| [[NCI-H2347 (line)]] | alt | 485 | 4 | 6 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.78× (z +14.3) | [[Tofacitinib (drug)]] 5 µM 0.308× (z -18.5) |
| [[SHP-77 (line)]] | alt | 466 | 0 | 10 (3 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.322× (z -14.5) |
| [[PANC-1 (line)]] | alt | 247 | 5 (3 ⚠) | 4 | [[Panobinostat (drug)]] 5 µM 2.66× (z +11.6) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.40× (z +10.4) | [[Tofacitinib (drug)]] 5 µM 0.505× (z -11.4) |
| [[SNU-423 (line)]] | alt | 560 | 0 | 9 (2 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.244× (z -18.8) |
| [[J82 (line)]] | alt | 273 | 6 (6 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 5.92× (z +17.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Tofacitinib (drug)]] 5 µM 0.434× (z -11.4) |
| [[NCI-H460 (line)]] | wt | 149 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.87× (z +28.7) | — |
| [[A498 (line)]] | wt | 450 | 0 | 7 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.364× (z -13.1) |
| [[COLO 205 (line)]] | alt | 1,039 | 0 | 7 (2 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.212× (z -17.2) |
| [[HOP62 (line)]] | alt | 98.5 | 7 (5 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.20× (z +15.0) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.52× (z +10.7) | — |
| [[Hs 766T (line)]] | wt | 280 | 2 | 5 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +10.9) | [[Tofacitinib (drug)]] 5 µM 0.336× (z -14.2) |
| [[hTERT-HPNE (line)]] | wt | 136 | 7 (6 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.03× (z +11.6) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.55× (z +11.1) | — |
| [[KATO III (line)]] | alt | 398 | 0 | 7 | — | [[Tofacitinib (drug)]] 5 µM 0.296× (z -16.0) |
| [[SK-MEL-2 (line)]] | alt | 428 | 3 (2 ⚠) | 4 | [[Panobinostat (drug)]] 0.5 µM 2.48× (z +9.5) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.48× (z +9.2) | [[Tofacitinib (drug)]] 5 µM 0.345× (z -15.7) |
| [[SW1417 (line)]] | alt | 535 | 0 | 6 | — | [[Tofacitinib (drug)]] 5 µM 0.379× (z -15.0) |
| [[SW480 (line)]] | alt | 143 | 6 (6 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.77× (z +16.8) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[C32 (line)]] | wt | 222 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.93× (z +15.4) | — |
| [[HT-29 (line)]] | alt | 137 | 5 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.57× (z +14.3) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.70× (z +8.5) | — |
| [[Panc 03.27 (line)]] | alt | 400 | 2 | 3 | [[Harringtonine (drug)]] 5 µM 2.83× (z +9.2) | [[Tofacitinib (drug)]] 5 µM 0.387× (z -12.4) |
| [[SNU-1 (line)]] | wt | 369 | 0 | 5 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.202× (z -11.2) ⚠ toxic · without an alert: [[Ponatinib (drug)]] 5 µM 0.275× (z -9.4) |
| [[H4 (line)]] | wt | 126 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.12× (z +12.2) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.34× (z +9.0) | — |
| [[HepG2_C3A (line)]] | wt | 451 | 0 | 3 | — | [[Tofacitinib (drug)]] 5 µM 0.245× (z -14.4) |
| [[LS 180 (line)]] | wt | 106 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.41× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H2030 (line)]] | alt | 156 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +9.1) | — |
| [[A-427 (line)]] | wt | 227 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.09× (z +8.9) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[CHP-212 (line)]] | wt | 312 | 0 | 2 | — | [[Tofacitinib (drug)]] 5 µM 0.277× (z -11.2) |
| [[SW 900 (line)]] | alt | 265 | 0 | 2 | — | [[Tofacitinib (citrate) (drug)]] 5 µM 0.426× (z -9.2) |
| [[AN3 CA (line)]] | alt | 161 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +9.3) | — |
| [[HCT15 (line)]] | alt | 189 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[LOX-IMVI (line)]] | wt | 290 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 248 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 286 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 231 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 206 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 242 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 146 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3671), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OAS3]] | +0.93 | +0.92 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 959 |
| [[MX1]] | +0.92 | +0.88 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 942 |
| [[RIGI]] | +0.91 | +0.93 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 994 |
| [[OAS2]] | +0.91 | +0.87 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 972 |
| [[CMPK2]] | +0.91 | +0.87 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 599 |
| [[PLSCR1]] | +0.91 | +0.84 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 723 |
| [[IFIT1]] | +0.90 | +0.88 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 945 |
| [[PARP9]] | +0.90 | +0.89 / +0.93 | both halves | 7e-06 | pathway: SARS-CoV-2 Infection; STRING 943 |
| [[OAS1]] | +0.89 | +0.85 / +0.90 | both halves | 7e-06 | pathway: Antimicrobial mechanism of IFN-stimulated genes; STRING 966 |
| [[IFI44]] | +0.89 | +0.84 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 915 |
| [[EIF2AK2]] | +0.88 | +0.83 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 980 |
| [[BATF2]] | +0.88 | +0.83 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 545 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*36 arrows, 36 of them with an alert ⚠; grade A 0, B 25, C 11. Shown: the 12 strongest; 24 more arrows (24 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OAS2]] | B | OAS2 activity raises STAT1's level | lines that do not express OAS2 (14) vs lines expressing it (36) | 2.31× lower at baseline in the lines without OAS2 | 0.001 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1 |
| [[IFI6]] | B | IFI6 activity raises STAT1's level | lines that do not express IFI6 (13) vs lines expressing it (37) | 2.74× lower at baseline in the lines without IFI6 | 0.001 | ⚠ within organs, on part of the lines; also absent: RASGRP3, MX1, IFITM1; maybe low, not absent |
| [[BATF2]] | B | BATF2 activity raises STAT1's level | lines that do not express BATF2 (13) vs lines expressing it (37) | 1.89× lower at baseline in the lines without BATF2 | 0.006 | ⚠ within organs, on part of the lines; also absent: RSAD2; maybe low, not absent |
| [[OAS1]] | B | OAS1 activity raises STAT1's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 2.30× lower at baseline in the lines without OAS1 | 0.006 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[RASGRP3]] | B | RASGRP3 activity raises STAT1's level | lines that do not express RASGRP3 (16) vs lines expressing it (34) | 2.09× lower at baseline in the lines without RASGRP3 | 0.008 | ⚠ within organs, on part of the lines; also absent: IFI6, SLC15A3, GBP4; maybe low, not absent |
| [[PARP9]] | B | PARP9 activity raises STAT1's level | lines that do not express PARP9 (7) vs lines expressing it (43) | 2.44× lower at baseline in the lines without PARP9 | 0.013 | ⚠ within organs, on part of the lines; also absent: PLSCR1, OAS3, SRMS; maybe low, not absent |
| [[CMPK2]] | B | CMPK2 activity raises STAT1's level | lines that do not express CMPK2 (11) vs lines expressing it (39) | 2.19× lower at baseline in the lines without CMPK2 | 0.018 | ⚠ within organs, on part of the lines; also absent: OAS2, NRIR, OAS1 |
| [[IFI6]] | B | IFI6 activity strengthens STAT1's drug response | lines that do not express IFI6 (13) vs lines expressing it (36) | the lines without IFI6 respond 0.33× as strongly (z diff +2.92); strongest at Auranofin 5 µM: 1.08x vs 0.48x (z diff +7.2) | 0.020 | ⚠ within organs, on part of the lines; also absent: RASGRP3, MX1, IFITM1; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[FBXO39]] | B | FBXO39 activity raises STAT1's level | lines that do not express FBXO39 (16) vs lines expressing it (34) | 1.88× lower at baseline in the lines without FBXO39 | 0.020 | ⚠ within organs, on part of the lines; also absent: XAF1, TRIM22, SLC15A3 |
| [[OAS2]] | B | OAS2 activity strengthens STAT1's drug response | lines that do not express OAS2 (14) vs lines expressing it (35) | the lines without OAS2 respond 0.44× as strongly (z diff +2.08); strongest at Auranofin 5 µM: 0.98x vs 0.49x (z diff +6.2) | 0.025 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1; target measured in part of the lines; artifact flags |
| [[PLSCR1]] | B | PLSCR1 activity raises STAT1's level | lines that do not express PLSCR1 (8) vs lines expressing it (42) | 2.39× lower at baseline in the lines without PLSCR1 | 0.028 | ⚠ within organs, on part of the lines; also absent: PARP9, ENSG00000279320, IFI6; maybe low, not absent |
| [[BATF2]] | B | BATF2 activity strengthens STAT1's drug response | lines that do not express BATF2 (13) vs lines expressing it (36) | the lines without BATF2 respond 0.55× as strongly (z diff +1.94); strongest at Auranofin 5 µM: 0.93x vs 0.51x (z diff +5.5) | 0.032 | ⚠ within organs, on part of the lines; also absent: RSAD2; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

*44 arrows, 44 of them with an alert ⚠; grade A 0, B 0, C 44. Shown: the 12 strongest; 32 more arrows (32 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADAR]] | C | STAT1's natural level strengthens ADAR's drug response | STAT1's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.89, reverse +0.69; direction not clear | 3e-07 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[IRF9]] | C | STAT1's natural level strengthens IRF9's drug response | STAT1's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.88, reverse +0.70; direction not clear | 3e-07 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[USP18]] | C | STAT1's natural level strengthens USP18's drug response | STAT1's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.89, reverse +0.54; direction not clear | 2e-06 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[HELZ2]] | C | STAT1's natural level strengthens HELZ2's drug response | STAT1's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.85, reverse +0.74; direction not clear | 6e-06 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PML]] | C | STAT1's natural level strengthens PML's drug response | STAT1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.85, reverse +0.54; direction not clear | 9e-06 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[TDRD7]] | C | STAT1's natural level strengthens TDRD7's drug response | STAT1's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.84, reverse +0.45; direction not clear | 1e-05 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[IFIT5]] | C | STAT1's natural level strengthens IFIT5's drug response | STAT1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.84, reverse +0.69; direction not clear | 2e-05 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PNPT1]] | C | STAT1's natural level strengthens PNPT1's drug response | STAT1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.84, reverse +0.67; direction not clear | 3e-05 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[TRIM25]] | C | STAT1's natural level strengthens TRIM25's drug response | STAT1's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.83, reverse +0.50; direction not clear | 3e-05 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[IFIT1]] | C | STAT1's natural level strengthens IFIT1's drug response | STAT1's natural level across 45 lines (lineage-adjusted; a glimpse) | r +0.84, reverse +0.24; direction not clear | 5e-05 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[TRIM14]] | C | STAT1's natural level strengthens TRIM14's drug response | STAT1's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.83, reverse +0.58; direction not clear | 5e-05 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PARP10]] | C | STAT1's natural level strengthens PARP10's drug response | STAT1's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.82, reverse +0.63; direction not clear | 1e-04 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.905). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (49.0, 53.9); signed map (65.3, 31.8). **Vector** length 174, 69.7% of its response variance represented; |z| ≥ 3 in 2,128 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon alpha response* (hallmark, mean cos +0.77 to 56); *Modulation of host responses by IFN-stimulated genes* (reactome, mean cos +0.80 to 10); *DDX58/IFIH1-mediated induction of interferon-alpha/beta* (reactome, mean cos +0.73 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +13.3 | +8.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +11.0 | +7.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +11.0 | +5.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.3 | +8.2 |
|  | [[Docetaxel (drug)]] 5 µM |  | +5.7 | +3.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.6 | +5.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +4.8 | +3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.5 | +1.0 |
|  | [[venetoclax (drug)]] 0.05 µM |  | +4.2 | +3.8 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -13.6 | -21.2 |
|  | [[Selinexor (drug)]] 5 µM |  | -13.3 | -13.2 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -12.5 | -16.6 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -12.1 | -13.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -11.2 | -7.2 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -10.3 | -12.7 |

## What is on record

|  |  |
|---|---|
| Name | signal transducer and activator of transcription 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q32.2 — chr2:190,908,460-191,020,960 (-) |
| Ensembl biotype | protein_coding |
| Also known as | STAT91, ISGF-3 |
| Gene groups (HGNC) | SH2 domain containing; Signal transducer and activator of transcription family |
| Hallmark sets | IL6_JAK_STAT3_SIGNALING, ALLOGRAFT_REJECTION, INTERFERON_GAMMA_RESPONSE |
| Reactome | 66 pathways, smallest: Interleukin-9 signaling; Differentiation of naive CD4+ T cells to T helper 1 cells (Th1 cells); Interleukin-21 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P42224](https://www.uniprot.org/uniprotkb/P42224) (Signal transducer and activator of transcription 1-alpha/beta):

> Signal transducer and transcription activator that mediates cellular responses to interferons (IFNs), cytokine KITLG/SCF and other cytokines and other growth factors. Following type I IFN (IFN-alpha and IFN-beta) binding to cell surface receptors, signaling via protein kinases leads to activation of Jak kinases (TYK2 and JAK1) and to tyrosine phosphorylation of STAT1 and STAT2. The phosphorylated STATs dimerize and associate with ISGF3G/IRF-9 to form a complex termed ISGF3 transcription factor, …

**Summary**, from NCBI Gene [6772](https://www.ncbi.nlm.nih.gov/gene/6772):

> The protein encoded by this gene is a member of the STAT protein family. In response to cytokines and growth factors, STAT family members are phosphorylated by the receptor associated kinases, and then form homo- or heterodimers that translocate to the cell nucleus where they act as transcription activators. The protein encoded by this gene can be activated by various ligands including interferon-alpha, interferon-gamma, EGF, PDGF and IL6. This protein mediates the expression of a variety of …

**Accessions** — [HGNC:11362](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11362) · Entrez [6772](https://www.ncbi.nlm.nih.gov/gene/6772) · UniProt [P42224](https://www.uniprot.org/uniprotkb/P42224) · Ensembl [ENSG00000115415](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115415)

## Data

Gene col 3671: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3671); `tables/drug_effects.parquet` (83 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3671, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3671]; `tensor/DDL_lfc|DDL_z.npy` [3671]; `embed/gene_vectors.npy` [3671]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3671 or target_col == 3671). Every well: [[STAT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STAT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
