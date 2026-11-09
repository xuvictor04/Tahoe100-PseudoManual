---
symbol: "TRIM28"
type: "gene"
col: 5109
ensembl_id: "ENSG00000130726"
name: "tripartite motif containing 28"
location: "19q13.43"
module: 138
arm: "+"
pooled_cpm: 40.56
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/138"]
generated_by: "tahoemap"
---

# TRIM28

*tripartite motif containing 28* — 19q13.43

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (19 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.82× (z +14.2, q 7e-43, up in 36 of 47 measured lines) ⚠ cell-cycle shift, explains ~43% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.58× (z +7.7, q 7e-13, up in 32 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.321×; ⚠ cell-cycle shift, explains ~39% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRRC2A]] (+0.66, fdr 7e-06), [[RAVER1]] (+0.63, fdr 1e-05), [[PTBP1]] (+0.61, fdr 1e-05); moves opposite to [[COA8]] (-0.57, fdr 8e-05), [[ACTR6]] (-0.52, fdr 7e-05), [[EMC4]] (-0.52, fdr 4e-05).
> It is in [[Module 138]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 22 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5109.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.82×** | +14.2 | 7e-43 | 36/47 (CFPAC-1, A498, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **1.96×** | +11.3 | 4e-27 | 40/45 (SW480, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.90×** | +10.3 | 1e-22 | 38/46 (MIA PaCa-2, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.82×** | +10.1 | 9e-22 | 41/48 (PANC-1, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **1.85×** | +9.9 | 3e-21 | 29/39 (KATO III, A549, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.80×** | +9.9 | 4e-21 | 40/47 (PANC-1, LS 180, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.71×** | +8.7 | 4e-16 | 38/48 (PANC-1, A549, …) | rises with dose | composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~40% of this change | **1.61×** | +8.0 | 1e-13 | 36/46 (SW 900, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **1.63×** | +7.9 | 1e-13 | 33/47 (PANC-1, LoVo, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.58×** | +7.7 | 7e-13 | 32/47 (PANC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.58×** | +7.7 | 7e-13 | 39/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.30×** | +7.3 | 1e-11 | 38/48 (C32, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.70×** | +6.2 | 3e-08 | 30/42 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.44×** | +6.1 | 4e-08 | 30/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.37×** | +5.3 | 4e-06 | 29/48 (NCI-H1792, Hs 766T, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.53×** | +3.7 | 0.005 | 16/48 (MIA PaCa-2, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.34×** | +3.5 | 0.011 | 10/48 (Panc 03.27, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 0.05 µM |  | **1.24×** | +3.4 | 0.019 | 13/48 (LOX-IMVI, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.46×** | +3.3 | 0.019 | 20/48 (C32, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.21×** | +3.2 | 0.030 | 15/48 (LOX-IMVI, RPMI-7951, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5109.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.321×; ⚠ cell-cycle shift, explains ~39% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | 0.798× | -3.6 | 0.16 | 21/47 (A498, RKO, …) | top dose only |  |
| [[Artesunate (drug)]] 0.5 µM |  | 0.828× | -3.2 | 0.46 | 10/48 (RPMI-7951, HEC-1-A, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5109. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 56.4 | 9 (8 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 9.49× (z +23.5) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.12× (z +12.4) | — |
| [[NCI-H460 (line)]] | wt | 32.5 | 7 (7 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 3.61× (z +12.2) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[A549 (line)]] | wt | 46.5 | 5 (5 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 5.84× (z +14.6) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[A498 (line)]] | wt | 67.5 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +16.4) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[CFPAC-1 (line)]] | alt | 29.0 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.02× (z +17.6) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[LoVo (line)]] | wt | 42.0 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +12.6) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[A-172 (line)]] | wt | 44.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.87× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 40.0 | 2 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 6.88× (z +12.5) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[J82 (line)]] | alt | 22.5 | 2 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 5.82× (z +12.9) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[LS 180 (line)]] | wt | 38.6 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.83× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[NCI-H1792 (line)]] | alt | 28.6 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +11.5) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[A-427 (line)]] | wt | 50.8 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.321× (z -11.3) ⚠ cell-cycle shift, explains ~39% of this change |
| [[AsPC-1 (line)]] | alt | 12.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.23× (z +11.5) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[C32 (line)]] | wt | 27.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +9.7) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[COLO 205 (line)]] | alt | 19.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +10.7) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[HEC-1-A (line)]] | alt | 53.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +9.2) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[HOP62 (line)]] | alt | 19.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +13.7) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[Hs 766T (line)]] | wt | 22.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +8.6) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[KATO III (line)]] | alt | 47.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.06× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 39.4 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.41× (z +9.5) ⚠ toxic | — |
| [[NCI-H1573 (line)]] | alt | 19.6 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.97× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[NCI-H2030 (line)]] | alt | 58.8 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.06× (z +8.7) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[Panc 03.27 (line)]] | alt | 35.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +9.8) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[RPMI-7951 (line)]] | alt | 42.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +9.1) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[SW1417 (line)]] | alt | 69.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +9.6) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[SW480 (line)]] | alt | 49.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.59× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[AN3 CA (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 94.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 34.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 42.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 53.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 40.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 43.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 45.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5109), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRRC2A]] | +0.66 | +0.66 / +0.58 | both halves | 7e-06 | same gene group; STRING 485 |
| [[RAVER1]] | +0.63 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[PTBP1]] | +0.61 | +0.68 / +0.50 | both halves | 1e-05 | same gene group |
| [[HNRNPL]] | +0.59 | +0.59 / +0.47 | both halves | 2e-05 | STRING 441 |
| [[SRCAP]] | +0.58 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[USP19]] | +0.57 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[TAOK2]] | +0.56 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[LRCH4]] | +0.55 | +0.46 / +0.65 | both halves | 3e-05 |  |
| [[CHTOP]] | +0.55 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[ISYNA1]] | +0.55 | +0.51 / +0.46 | both halves | 3e-05 |  |
| [[SRSF1]] | +0.55 | +0.61 / +0.41 | both halves | 4e-05 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 436 |
| [[SRSF6]] | +0.54 | +0.53 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COA8]] | -0.57 | -0.37 / -0.60 | both halves | 8e-05 |  |
| [[ACTR6]] | -0.52 | -0.54 / -0.38 | both halves | 7e-05 |  |
| [[EMC4]] | -0.52 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[ZFAND2A]] | -0.50 | -0.38 / -0.49 | both halves | 6e-05 |  |
| [[FTL]] | -0.50 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[PSMA7]] | -0.50 | -0.32 / -0.43 | both halves | 2e-04 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[ARPC3]] | -0.49 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[BLVRB]] | -0.48 | -0.50 / -0.36 | both halves | 9e-05 |  |
| [[TAX1BP1]] | -0.47 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[LINC02935]] | -0.47 | -0.39 / -0.50 | both halves | 5e-05 |  |
| [[DHRS7]] | -0.47 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[PCYT1A]] | -0.47 | -0.46 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 138]]; 34 genes; every member is in the + arm (projection on the module's main direction 0.562). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-40.7, -32.1); signed map (-8.8, -34.6). **Vector** length 75.4, 16.9% of its response variance represented; |z| ≥ 3 in 921 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.0 | +10.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +3.5 | +14.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | +3.5 | +2.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~40% of this change | +3.1 | +8.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +2.7 | -1.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.1 | +0.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.9 | +3.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.9 | +3.2 |
|  | [[crizotinib (drug)]] 5 µM |  | +1.9 | +1.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.7 | +1.0 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -5.2 | -1.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.8 | +0.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.7 | +0.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.7 | -0.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -3.2 | +2.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.2 | +0.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.8 | -3.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.8 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | tripartite motif containing 28 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.43 — chr19:58,544,064-58,550,722 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TIF1B, KAP1, TF1B, RNF96, PPP1R157, KAP-1, TIF1-beta, TIF1beta |
| Gene groups (HGNC) | Ring finger proteins; Tripartite motif family; PHD finger proteins; Protein phosphatase 1 regulatory subunits; Bromodomain containing; MicroRNA protein coding host genes |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 9 pathways, smallest: SUMOylation of transcription cofactors; Regulation of endogenous retroelements by KRAB-ZFP proteins; HCMV Early Events |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13263](https://www.uniprot.org/uniprotkb/Q13263) (Transcription intermediary factor 1-beta):

> E3 SUMO and ubiquitin ligase that plays a pivotal role in embryonic development, genomic imprinting, and maintenance of genomic stability through repression of repetitive and retroviral elements. Also involved in DNA repair, regulation of innate immunity or cellular energy homeostasis. Acts as a scaffold for assembling transcriptional repression complexes containing methyltransferases, histone deacetylases, and chromatin remodelers. Serves as a nuclear corepressor for KRAB domain-containing …

**Summary**, from NCBI Gene [10155](https://www.ncbi.nlm.nih.gov/gene/10155):

> The protein encoded by this gene mediates transcriptional control by interaction with the Kruppel-associated box repression domain found in many transcription factors. The protein localizes to the nucleus and is thought to associate with specific chromatin regions. The protein is a member of the tripartite motif family. This tripartite motif includes three zinc-binding domains, a RING, a B-box type 1 and a B-box type 2, and a coiled-coil region. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:16384](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16384) · Entrez [10155](https://www.ncbi.nlm.nih.gov/gene/10155) · UniProt [Q13263](https://www.uniprot.org/uniprotkb/Q13263) · Ensembl [ENSG00000130726](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130726)

## Data

Gene col 5109: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5109); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5109, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5109]; `tensor/DDL_lfc|DDL_z.npy` [5109]; `embed/gene_vectors.npy` [5109]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5109 or target_col == 5109). Every well: [[TRIM28 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRIM28.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
