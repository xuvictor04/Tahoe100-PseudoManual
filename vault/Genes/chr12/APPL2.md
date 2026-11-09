---
symbol: "APPL2"
type: "gene"
col: 5803
ensembl_id: "ENSG00000136044"
name: "adaptor protein, phosphotyrosine interacting with PH domain and leucine zipper 2"
location: "12q23.3"
module: 110
arm: "+"
pooled_cpm: 79.36
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 25
n_dd_up_clean: 0
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/110"]
generated_by: "tahoemap"
---

# APPL2

*adaptor protein, phosphotyrosine interacting with PH domain and leucine zipper 2* — 12q23.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (HS-578T 2.23×; ⚠ cell-cycle shift, explains ~28% of this change).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.531× (z -17.7, q 0e+00, down in 39 of 48 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.497× (z -13.9, q 3e-41, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CRYL1]] (+0.55, fdr 1e-05), [[RAB3B]] (+0.53, fdr 3e-05), [[RPGR]] (+0.52, fdr 3e-05); moves opposite to [[LZTS2]] (-0.54, fdr 1e-04), [[TRIM69]] (-0.53, fdr 4e-05), [[LINC02100]] (-0.52, fdr 3e-05).
> It is in [[Module 110]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF793]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5803.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (HS-578T 2.23×; ⚠ cell-cycle shift, explains ~28% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Hydroxyfasudil (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.19× | +3.5 | 0.13 | 17/48 (PANC-1, KATO III, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.13× | +3.5 | 0.13 | 7/48 (PANC-1, LOX-IMVI, …) | rises with dose |  |
| [[BAY1125976 (drug)]] 5 µM |  | 1.36× | +3.2 | 0.23 | 12/48 (NCI-H1573, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 15 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5803.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.531×** | -17.7 | 0e+00 | 39/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.497×** | -13.9 | 3e-41 | 40/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.498×** | -11.2 | 5e-27 | 38/48 (NCI-H1573, A549, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.684×** | -10.6 | 3e-24 | 40/49 (AsPC-1, HT-29, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.660×** | -8.2 | 2e-14 | 37/48 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.475×** | -7.7 | 1e-12 | 36/48 (LS 180, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.624×** | -7.6 | 2e-12 | 39/47 (LoVo, NCI-H460, …) | top dose only | cell-cycle shift (explains ~25% here); noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.480×** | -7.6 | 2e-12 | 33/49 (KATO III, LS 180, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.690×** | -7.3 | 1e-11 | 30/48 (LoVo, NCI-H1792, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.726×** | -5.2 | 1e-05 | 24/47 (J82, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.781×** | -4.9 | 5e-05 | 23/48 (NCI-H460, LS 180, …) | rises with dose | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.931× | -4.8 | 9e-05 | 2/50 (MIA PaCa-2, NCI-H2122) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.752×** | -4.6 | 2e-04 | 27/48 (NCI-H23, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.794×** | -4.5 | 2e-04 | 25/48 (KATO III, NCI-H460, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.798×** | -4.5 | 3e-04 | 24/48 (HT-29, LoVo, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **0.664×** | -4.2 | 7e-04 | 27/48 (KATO III, COLO 205, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.813×** | -4.1 | 0.001 | 22/48 (NCI-H2030, HT-29, …) | two highest doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.685×** | -3.9 | 0.003 | 22/48 (KATO III, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.686×** | -3.9 | 0.003 | 24/48 (KATO III, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.707×** | -3.6 | 0.009 | 20/48 (SW1417, J82, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.837× | -3.5 | 0.011 | 17/49 (NCI-H1573, LOX-IMVI, …) | inconsistent across doses |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 0.846× | -3.3 | 0.022 | 19/48 (HT-29, KATO III, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.746×** | -3.0 | 0.049 | 20/48 (NCI-H460, KATO III, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5803. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 81.5 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -22.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.227× (z -18.2) |
| [[J82 (line)]] | alt | 86.4 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.468× (z -11.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.476× (z -11.0) |
| [[LoVo (line)]] | wt | 143 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.327× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.402× (z -12.0) |
| [[LS 180 (line)]] | wt | 97.4 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.484× (z -11.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.323× (z -10.6) |
| [[AsPC-1 (line)]] | alt | 286 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -20.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.335× (z -17.4) |
| [[HEC-1-A (line)]] | alt | 61.5 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.449× (z -14.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.412× (z -11.6) |
| [[PANC-1 (line)]] | alt | 65.0 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -17.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.236× (z -17.1) |
| [[A549 (line)]] | wt | 80.7 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -18.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.177× (z -15.7) |
| [[KATO III (line)]] | alt | 112 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.448× (z -13.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.393× (z -10.8) |
| [[NCI-H1573 (line)]] | alt | 84.1 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -21.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.254× (z -16.7) |
| [[A-427 (line)]] | wt | 78.2 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.414× (z -14.9) ⚠ cell-cycle shift, explains ~28% of this change |
| [[CFPAC-1 (line)]] | alt | 50.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -14.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.293× (z -9.8) |
| [[COLO 205 (line)]] | alt | 78.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -11.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.231× (z -9.8) |
| [[HT-29 (line)]] | alt | 121 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.425× (z -12.2) |
| [[NCI-H1792 (line)]] | alt | 77.4 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.300× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.241× (z -11.2) |
| [[NCI-H23 (line)]] | alt | 101 | 0 | 3 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.271× (z -12.8) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.417× (z -8.6) |
| [[SNU-423 (line)]] | alt | 55.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -15.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.318× (z -9.1) |
| [[HOP62 (line)]] | alt | 86.8 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.617× (z -8.6) |
| [[SW480 (line)]] | alt | 59.6 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.518× (z -9.1) ⚠ cell-cycle shift, explains ~69% of this change |
| [[A-172 (line)]] | wt | 91.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.516× (z -10.8) |
| [[A498 (line)]] | wt | 47.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.548× (z -9.9) ⚠ cell-cycle shift, explains ~28% of this change |
| [[AN3 CA (line)]] | alt | 58.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.207× (z -8.5) |
| [[C32 (line)]] | wt | 45.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -11.3) ⚠ cell-cycle shift, explains ~28% of this change |
| [[Hs 766T (line)]] | wt | 62.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -10.6) ⚠ cell-cycle shift, explains ~28% of this change |
| [[HS-578T (line)]] | alt | 61.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +10.4) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[LOX-IMVI (line)]] | wt | 121 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -14.1) ⚠ cell-cycle shift, explains ~28% of this change |
| [[MIA PaCa-2 (line)]] | alt | 52.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.276× (z -12.1) |
| [[NCI-H2030 (line)]] | alt | 83.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.455× (z -10.7) |
| [[RKO (line)]] | wt | 88.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.359× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 82.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.457× (z -12.6) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SNU-1 (line)]] | wt | 61.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.140× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 47.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.334× (z -9.5) |
| [[BT-474 (line)]] | alt | 68.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 63.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 55.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 49.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 70.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 64.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 96.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 80.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 73.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 78.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 56.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 59.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 71.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 86.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 57.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5803), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*33 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRYL1]] | +0.55 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[RAB3B]] | +0.53 | +0.46 / +0.49 | both halves | 3e-05 |  |
| [[RPGR]] | +0.52 | +0.54 / +0.46 | both halves | 3e-05 |  |
| [[MAPK8]] | +0.51 | +0.46 / +0.42 | both halves | 4e-05 |  |
| [[CDH4]] | +0.49 | +0.32 / +0.50 | both halves | 2e-04 |  |
| [[LYPLA1]] | +0.49 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[SEPTIN10]] | +0.48 | +0.44 / +0.44 | both halves | 3e-05 |  |
| [[GRK6]] | +0.48 | +0.53 / +0.30 | both halves | 2e-04 |  |
| [[USB1]] | +0.48 | +0.39 / +0.40 | both halves | 5e-05 |  |
| [[TBC1D16]] | +0.47 | +0.36 / +0.41 | both halves | 1e-04 |  |
| [[ELK3]] | +0.47 | +0.40 / +0.52 | both halves | 4e-05 |  |
| [[CNST]] | +0.47 | +0.38 / +0.49 | both halves | 6e-05 |  |

## Genes that move opposite

*67 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LZTS2]] | -0.54 | -0.34 / -0.46 | both halves | 1e-04 |  |
| [[TRIM69]] | -0.53 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[LINC02100]] | -0.52 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[JAM2]] | -0.49 | -0.38 / -0.42 | both halves | 7e-05 |  |
| [[MAD2L1BP]] | -0.49 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[WTAP]] | -0.49 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[DHX58]] | -0.49 | -0.48 / -0.40 | both halves | 4e-05 |  |
| [[CCDC30]] | -0.49 | -0.49 / -0.38 | both halves | 6e-05 |  |
| [[LRRIQ3]] | -0.48 | -0.37 / -0.41 | both halves | 8e-05 |  |
| [[ANKRD31]] | -0.48 | -0.55 / -0.26 | both halves | 4e-04 |  |
| [[SAMD11]] | -0.47 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[PRRT2]] | -0.47 | -0.46 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF793]] | B | ZNF793 activity lowers APPL2's level | lines that do not express ZNF793 (22) vs lines expressing it (28) | 1.33× higher at baseline in the lines without ZNF793 | 0.060 | ⚠ within organs, on part of the lines; also absent: PEG10, MAP6, ZNF570 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 110]]; 43 genes; every member is in the + arm (projection on the module's main direction 0.279). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (59.1, 9.1); signed map (3.6, 54.1). **Vector** length 87.4, 21.9% of its response variance represented; |z| ≥ 3 in 1,165 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.5 | -2.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.7 | +1.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.9 | -1.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | +3.5 | -3.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | -2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.5 | -1.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.1 | +1.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.8 | +0.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.8 | -1.1 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.8 | +3.5 |
| fall | [[TAK-733 (drug)]] 5 µM |  | -3.6 | -3.9 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.6 | -4.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.6 | -13.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.6 | -4.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -3.3 | -17.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.2 | -7.7 |
|  | [[EX229 (drug)]] 5 µM |  | -2.8 | -3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.8 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | adaptor protein, phosphotyrosine interacting with PH domain and leucine zipper 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q23.3 — chr12:105,173,297-105,236,203 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10659, DIP13B |
| Gene groups (HGNC) | BAR-PH domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NEU8](https://www.uniprot.org/uniprotkb/Q8NEU8) (DCC-interacting protein 13-beta):

> Multifunctional adapter protein that binds to various membrane receptors, nuclear factors and signaling proteins to regulate many processes, such as cell proliferation, immune response, endosomal trafficking and cell metabolism. Regulates signaling pathway leading to cell proliferation through interaction with RAB5A and subunits of the NuRD/MeCP1 complex. Plays a role in immune response by modulating phagocytosis, inflammatory and innate immune responses. In macrophages, enhances Fc-gamma …

**Summary**, from NCBI Gene [55198](https://www.ncbi.nlm.nih.gov/gene/55198):

> The protein encoded by this gene is one of two effectors of the small GTPase RAB5A/Rab5, which are involved in a signal transduction pathway. Both effectors contain an N-terminal Bin/Amphiphysin/Rvs (BAR) domain, a central pleckstrin homology (PH) domain, and a C-terminal phosphotyrosine binding (PTB) domain, and they bind the Rab5 through the BAR domain. They are associated with endosomal membranes and can be translocated to the nucleus in response to the EGF stimulus. They interact with the …

**Accessions** — [HGNC:18242](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18242) · Entrez [55198](https://www.ncbi.nlm.nih.gov/gene/55198) · UniProt [Q8NEU8](https://www.uniprot.org/uniprotkb/Q8NEU8) · Ensembl [ENSG00000136044](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136044)

## Data

Gene col 5803: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5803); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5803, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5803]; `tensor/DDL_lfc|DDL_z.npy` [5803]; `embed/gene_vectors.npy` [5803]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5803 or target_col == 5803). Every well: [[APPL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/APPL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
