---
symbol: "RABEP1"
type: "gene"
col: 393
ensembl_id: "ENSG00000029725"
name: "rabaptin, RAB GTPase binding effector protein 1"
location: "17p13.2"
module: 172
arm: "+"
pooled_cpm: 104.65
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 0
n_dd_up_clean: 21
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/172"]
generated_by: "tahoemap"
---

# RABEP1

*rabaptin, RAB GTPase binding effector protein 1* — 17p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.39× (z +37.1, q 0e+00, up in 47 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SNU-1 0.317×, HEC-1-A 0.551×, HT-29 0.525×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change); [[Adagrasib (drug)]] 0.05 µM in 1 line (NCI-H23 0.697×; ⚠ position not correctable); [[Lonafarnib (drug)]] 5 µM in 1 line (BT-474 0.115×; ⚠ toxic); [[Auranofin (drug)]] 5 µM in 1 line (HEC-1-A 0.629×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TBCA]] (+0.58, fdr 1e-05), [[ZNF609]] (+0.57, fdr 1e-05), [[GPATCH8]] (+0.57, fdr 1e-05); moves opposite to [[KHDC4]] (-0.54, fdr 1e-05), [[EEF1AKMT3]] (-0.53, fdr 1e-05), [[SLC35A2]] (-0.52, fdr 3e-05).
> It is in [[Module 172]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 49 in all, 18 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 393.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.39×** | +37.1 | 0e+00 | 47/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.52×** | +27.8 | 0e+00 | 48/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.48×** | +27.3 | 0e+00 | 48/48 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.25×** | +24.3 | 0e+00 | 47/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.12×** | +21.6 | 0e+00 | 47/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.86×** | +18.7 | 0e+00 | 45/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.78×** | +16.4 | 0e+00 | 42/48 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.82×** | +16.1 | 0e+00 | 43/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.67×** | +15.4 | 0e+00 | 42/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.60×** | +14.1 | 2e-43 | 45/48 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.51×** | +12.4 | 1e-33 | 40/48 (PANC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.51×** | +12.3 | 3e-33 | 35/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.50×** | +12.3 | 7e-33 | 40/48 (BT-474, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.42×** | +10.5 | 3e-24 | 39/48 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.27×** | +10.3 | 3e-23 | 27/49 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.31×** | +8.2 | 8e-15 | 35/48 (BT-474, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.66×** | +7.9 | 6e-14 | 43/49 (PANC-1, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 393.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SNU-1 0.317×, HEC-1-A 0.551×, HT-29 0.525×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change); [[Adagrasib (drug)]] 0.05 µM in 1 line (NCI-H23 0.697×; ⚠ position not correctable); [[Lonafarnib (drug)]] 5 µM in 1 line (BT-474 0.115×; ⚠ toxic); [[Auranofin (drug)]] 5 µM in 1 line (HEC-1-A 0.629×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.932× | -6.9 | 2e-09 | 1/50 (NCI-H23) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.917× | -3.7 | 0.067 | 2/48 (Hs 766T, SW 1271) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 393. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 129 | 17 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.79× (z +41.4) | — |
| [[PANC-1 (line)]] | alt | 78.1 | 14 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +33.2) | — |
| [[HS-578T (line)]] | alt | 87.4 | 11 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +17.3) | — |
| [[NCI-H1792 (line)]] | alt | 107 | 11 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.25× (z +15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.15× (z +15.3) | — |
| [[A498 (line)]] | wt | 107 | 10 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.86× (z +17.2) | — |
| [[COLO 205 (line)]] | alt | 83.2 | 10 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.93× (z +21.5) | — |
| [[H4 (line)]] | wt | 46.9 | 10 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +11.3) | — |
| [[NCI-H23 (line)]] | alt | 127 | 10 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +22.5) | — |
| [[SW480 (line)]] | alt | 182 | 10 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.75× (z +21.2) | — |
| [[A-172 (line)]] | wt | 135 | 9 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +23.4) | — |
| [[A549 (line)]] | wt | 122 | 9 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +21.0) | — |
| [[BT-474 (line)]] | alt | 109 | 8 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.84× (z +11.9) | [[Lonafarnib (drug)]] 5 µM 0.115× (z -12.9) ⚠ toxic |
| [[J82 (line)]] | alt | 115 | 9 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +22.3) | — |
| [[LS 180 (line)]] | wt | 77.4 | 9 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +18.2) | — |
| [[AsPC-1 (line)]] | alt | 69.2 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +19.8) | — |
| [[HEC-1-A (line)]] | alt | 133 | 6 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +17.9) | [[Dinaciclib (drug)]] 0.5 µM 0.551× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.629× (z -8.8) |
| [[HOP62 (line)]] | alt | 84.4 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +20.1) | — |
| [[Hs 766T (line)]] | wt | 75.8 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.42× (z +25.3) | — |
| [[KATO III (line)]] | alt | 128 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +24.5) | — |
| [[HCT15 (line)]] | alt | 114 | 7 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.24× (z +12.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 176 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +23.7) | — |
| [[NCI-H1573 (line)]] | alt | 38.9 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.76× (z +19.7) | — |
| [[NCI-H2030 (line)]] | alt | 73.0 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.84× (z +22.4) | — |
| [[SW 900 (line)]] | alt | 91.4 | 7 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.51× (z +18.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.17× (z +12.3) | — |
| [[A-427 (line)]] | wt | 116 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 2.46× (z +12.1) | — |
| [[C32 (line)]] | wt | 102 | 6 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.55× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.31× (z +10.3) | — |
| [[HT-29 (line)]] | alt | 90.5 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +18.5) | [[Dinaciclib (drug)]] 0.5 µM 0.525× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[hTERT-HPNE (line)]] | wt | 91.0 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +12.5) | — |
| [[SNU-423 (line)]] | alt | 125 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +21.2) | — |
| [[LoVo (line)]] | wt | 99.4 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 2.88× (z +17.1) | — |
| [[LOX-IMVI (line)]] | wt | 74.0 | 5 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.41× (z +14.4) | — |
| [[NCI-H2347 (line)]] | alt | 61.0 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +17.2) | — |
| [[RPMI-7951 (line)]] | alt | 82.8 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +12.0) | — |
| [[SW48 (line)]] | wt | 138 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +11.4) | [[Dinaciclib (drug)]] 0.05 µM 0.425× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change |
| [[C-33 A (line)]] | alt | 127 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.69× (z +10.4) | — |
| [[CFPAC-1 (line)]] | alt | 50.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +17.3) | — |
| [[HepG2_C3A (line)]] | wt | 90.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +12.2) | — |
| [[Panc 03.27 (line)]] | alt | 86.3 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.41× (z +12.3) | — |
| [[SHP-77 (line)]] | alt | 140 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.97× (z +14.0) | — |
| [[SW1417 (line)]] | alt | 81.3 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.43× (z +12.1) | — |
| [[RKO (line)]] | wt | 187 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +12.1) | — |
| [[SNU-1 (line)]] | wt | 160 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.317× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[SK-MEL-2 (line)]] | alt | 42.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +10.6) | — |
| [[AN3 CA (line)]] | alt | 167 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 137 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 81.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 128 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 393), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBCA]] | +0.58 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[ZNF609]] | +0.57 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[GPATCH8]] | +0.57 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[ALS2]] | +0.55 | +0.68 / +0.49 | both halves | 1e-05 | pathway: Rab regulation of trafficking; STRING 502 |
| [[SLC38A7]] | +0.54 | +0.72 / +0.37 | both halves | 7e-05 |  |
| [[DTNBP1]] | +0.54 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[PPP6R2]] | +0.53 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[CLEC16A]] | +0.53 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[ITSN2]] | +0.53 | +0.53 / +0.47 | both halves | 2e-05 | STRING 594 |
| [[JPX]] | +0.52 | +0.66 / +0.44 | both halves | 3e-05 |  |
| [[GUSBP11]] | +0.50 | +0.58 / +0.44 | both halves | 3e-05 |  |
| [[EIF3J]] | +0.50 | +0.60 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KHDC4]] | -0.54 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[EEF1AKMT3]] | -0.53 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[SLC35A2]] | -0.52 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[VAMP1]] | -0.52 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[KLHL15]] | -0.51 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[ATP5F1B]] | -0.51 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[LINC01232]] | -0.51 | -0.28 / -0.61 | both halves | 3e-04 |  |
| [[TMEM39A]] | -0.50 | -0.61 / -0.44 | both halves | 3e-05 |  |
| [[SUCO]] | -0.50 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[DERL1]] | -0.50 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[CHST7]] | -0.49 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[APAF1]] | -0.49 | -0.62 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 172]]; 24 genes; every member is in the + arm (projection on the module's main direction 0.642). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-30.8, -13.3); signed map (-1.6, -9.9). **Vector** length 92.0, 27.1% of its response variance represented; |z| ≥ 3 in 1,367 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +6.7 | +15.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +6.6 | +16.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.6 | +14.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +5.1 | +12.3 |
|  | [[Rapamycin (drug)]] 5 µM |  | +5.1 | +4.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.4 | +7.0 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | +3.7 | +3.1 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +3.6 | +4.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.4 | +0.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | +0.8 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -3.8 | -6.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | -3.5 | -0.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | -3.2 | +10.3 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | -2.1 | -0.4 |
|  | [[Asciminib (drug)]] 0.05 µM |  | -1.9 | -1.9 |
|  | [[ERK5-IN-2 (drug)]] 0.05 µM |  | -1.8 | -0.6 |
|  | [[Allopurinol (drug)]] 0.05 µM |  | -1.7 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | rabaptin, RAB GTPase binding effector protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.2 — chr17:5,282,265-5,386,340 (+) |
| Ensembl biotype | protein_coding |
| Also known as | neurocrescin, RAB5EP, RABPT5, rabaptin-5 |
| Hallmark sets | ESTROGEN_RESPONSE_LATE |
| Reactome | 4 pathways, smallest: TBC/RABGAPs; Rab regulation of trafficking; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15276](https://www.uniprot.org/uniprotkb/Q15276) (Rab GTPase-binding effector protein 1):

> Rab effector protein acting as linker between gamma-adaptin, RAB4A and RAB5A. Involved in endocytic membrane fusion and membrane trafficking of recycling endosomes. Involved in KCNH1 channels trafficking to and from the cell membrane. Forms a complex with RABGEF1 that stimulates RABGEF1-mediated nucleotide exchange on RAB5A. Mediates the traffic of PKD1:PKD2 complex from the endoplasmic reticulum through the Golgi to the cilium (By similarity).

**Summary**, from NCBI Gene [9135](https://www.ncbi.nlm.nih.gov/gene/9135):

> Enables protein domain specific binding activity and protein homodimerization activity. Involved in vesicle-mediated transport. Located in cytosol; endocytic vesicle; and endosome. Part of protein-containing complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17677](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17677) · Entrez [9135](https://www.ncbi.nlm.nih.gov/gene/9135) · UniProt [Q15276](https://www.uniprot.org/uniprotkb/Q15276) · Ensembl [ENSG00000029725](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000029725)

## Data

Gene col 393: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 393); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 393, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 393]; `tensor/DDL_lfc|DDL_z.npy` [393]; `embed/gene_vectors.npy` [393]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 393 or target_col == 393). Every well: [[RABEP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RABEP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
