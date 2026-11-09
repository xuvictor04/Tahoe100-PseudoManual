---
symbol: "VARS1"
type: "gene"
col: 12868
ensembl_id: "ENSG00000204394"
name: "valyl-tRNA synthetase 1"
location: "6p21.33"
module: 4
arm: "+"
pooled_cpm: 25.51
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 5
n_dd_up_clean: 15
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# VARS1

*valyl-tRNA synthetase 1* — 6p21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.32× (z +16.3, q 0e+00, up in 45 of 45 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.84× (z +6.7, q 1e-09, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Bimiralisib (drug)]] 0.05 µM: 0.686× (z -4.0, q 0.034, down in 20 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IPO4]] (+0.83, fdr 7e-06), [[NUP188]] (+0.78, fdr 7e-06), [[ATP13A1]] (+0.75, fdr 7e-06); moves opposite to [[DCTN6-DT]] (-0.71, fdr 7e-06), [[BSDC1]] (-0.69, fdr 7e-06), [[EAPP]] (-0.66, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 14 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12868.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **4.32×** | +16.3 | 0e+00 | 45/45 (HOP62, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **3.93×** | +14.6 | 0e+00 | 34/36 (HOP62, A498, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **3.15×** | +11.8 | 9e-30 | 38/42 (HOP62, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.84×** | +9.5 | 3e-19 | 38/48 (PANC-1, CFPAC-1, …) | rises with dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.20×** | +8.7 | 3e-16 | 45/47 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.96×** | +7.2 | 8e-11 | 34/48 (PANC-1, HOP62, …) | rises with dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.84×** | +6.7 | 1e-09 | 32/48 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.72×** | +6.0 | 2e-07 | 32/48 (PANC-1, NCI-H1573, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~42% of this change | **1.75×** | +5.9 | 2e-07 | 35/46 (LoVo, C32, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **2.36×** | +5.0 | 4e-05 | 30/46 (A498, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **2.31×** | +4.8 | 6e-05 | 30/46 (NCI-H460, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +4.8 | 7e-05 | 4/48 (KATO III, HCT15, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **2.25×** | +4.7 | 1e-04 | 29/46 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **2.22×** | +4.6 | 2e-04 | 28/46 (PANC-1, NCI-H460, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **2.17×** | +4.5 | 3e-04 | 32/47 (MIA PaCa-2, NCI-H460, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[EX229 (drug)]] 0.05 µM |  | **1.45×** | +3.9 | 0.003 | 20/48 (Hs 766T, A498, …) | all doses, stronger at high dose | position effect removed |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.60×** | +3.7 | 0.006 | 19/48 (NCI-H1792, NCI-H2030, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.41×** | +3.6 | 0.008 | 22/47 (LoVo, NCI-H1792, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.38×** | +3.6 | 0.009 | 20/46 (SK-MEL-2, MIA PaCa-2, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **1.85×** | +3.6 | 0.009 | 19/45 (NCI-H460, Hs 766T, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.22×** | +3.1 | 0.041 | 15/48 (MIA PaCa-2, C32, …) | rises with dose |  |
| [[Talc (drug)]] 0.5 µM |  | **1.32×** | +3.1 | 0.045 | 7/47 (NCI-H2030, SHP-77, …) | inconsistent across doses | position effect removed |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.46×** | +3.0 | 0.054 | 18/48 (NCI-H2030, NCI-H23, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Pralsetinib (drug)]] 5 µM |  | **1.67×** | +3.0 | 0.056 | 14/46 (PANC-1, Panc 03.27, …) | top dose only | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12868.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bimiralisib (drug)]] 0.05 µM |  | **0.686×** | -4.0 | 0.034 | 20/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Ciclopirox (drug)]] 5 µM |  | **0.789×** | -3.8 | 0.040 | 21/48 (SW480, SHP-77, …) | inconsistent across doses |  |
| [[Bergenin (drug)]] 5 µM |  | **0.795×** | -3.7 | 0.040 | 20/48 (SHP-77, LS 180, …) | top dose only | position effect removed |
| [[Bimiralisib (drug)]] 5 µM |  | **0.538×** | -3.6 | 0.040 | 18/48 (A-427, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.720×** | -3.4 | 0.087 | 18/48 (SK-MEL-2, LoVo, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | 0.585× | -3.1 | 0.15 | 16/48 (LS 180, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 0.755× | -3.1 | 0.18 | 17/46 (LOX-IMVI, SW1417, …) | rises with dose | position effect removed |
| [[Meloxicam (drug)]] 0.5 µM |  | 0.767× | -3.0 | 0.19 | 16/47 (SNU-423, NCI-H2347, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, +0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12868. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 44.4 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.02× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.81× (z +9.2) | — |
| [[A549 (line)]] | wt | 11.6 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.31× (z +9.8) ⚠ cell-cycle shift, explains ~57% of this change | — |
| [[HOP62 (line)]] | alt | 16.6 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.61× (z +13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[A498 (line)]] | wt | 36.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.89× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[LoVo (line)]] | wt | 22.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.79× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[LOX-IMVI (line)]] | wt | 30.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.87× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[SNU-423 (line)]] | alt | 15.2 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.19× (z +10.8) ⚠ cell-cycle shift, explains ~57% of this change | — |
| [[A-172 (line)]] | wt | 20.2 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +10.3) ⚠ cell-cycle shift, explains ~57% of this change | — |
| [[CFPAC-1 (line)]] | alt | 18.0 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.62× (z +11.9) ⚠ cell-cycle shift, explains ~57% of this change | — |
| [[HEC-1-A (line)]] | alt | 18.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.32× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[HS-578T (line)]] | alt | 23.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.17× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H1792 (line)]] | alt | 11.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.91× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H460 (line)]] | wt | 19.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.35× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SW480 (line)]] | alt | 23.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.64× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[A-427 (line)]] | wt | 28.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.05× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[C32 (line)]] | wt | 16.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.37× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[HCT15 (line)]] | alt | 38.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.19× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[Hs 766T (line)]] | wt | 14.3 | 0 | 1 (1 ⚠) | — | [[Tucidinostat (drug)]] 0.5 µM 0.0514× (z -14.6) ⚠ cell-cycle shift, would explain all of this change |
| [[HT-29 (line)]] | alt | 23.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.11× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[KATO III (line)]] | alt | 23.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.17× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[LS 180 (line)]] | wt | 17.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.71× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 29.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.72× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H1573 (line)]] | alt | 8.61 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.84× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H23 (line)]] | alt | 45.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.62× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[Panc 03.27 (line)]] | alt | 19.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.97× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 26.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.12× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SW 900 (line)]] | alt | 16.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +8.6) ⚠ cell-cycle shift, explains ~57% of this change | — |
| [[SW48 (line)]] | wt | 38.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.57× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[AN3 CA (line)]] | alt | 75.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.20 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 33.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 32.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 50.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 34.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12868), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IPO4]] | +0.83 | +0.80 / +0.80 | both halves | 7e-06 | STRING 459 |
| [[NUP188]] | +0.78 | +0.72 / +0.78 | both halves | 7e-06 |  |
| [[ATP13A1]] | +0.75 | +0.77 / +0.71 | both halves | 7e-06 |  |
| [[PFAS]] | +0.75 | +0.73 / +0.74 | both halves | 7e-06 |  |
| [[EIF4G1]] | +0.75 | +0.74 / +0.72 | both halves | 7e-06 |  |
| [[FARSB]] | +0.72 | +0.68 / +0.76 | both halves | 7e-06 | pathway: Cytosolic tRNA aminoacylation; STRING 776 |
| [[WDR77]] | +0.72 | +0.67 / +0.75 | both halves | 7e-06 |  |
| [[BOP1]] | +0.71 | +0.73 / +0.75 | both halves | 7e-06 | STRING 537 |
| [[PSME3]] | +0.70 | +0.70 / +0.73 | both halves | 7e-06 |  |
| [[ATIC]] | +0.69 | +0.68 / +0.69 | both halves | 7e-06 | STRING 496 |
| [[MTHFD1]] | +0.67 | +0.58 / +0.75 | both halves | 8e-06 |  |
| [[PNPO]] | +0.66 | +0.70 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCTN6-DT]] | -0.71 | -0.63 / -0.70 | both halves | 7e-06 |  |
| [[BSDC1]] | -0.69 | -0.63 / -0.70 | both halves | 7e-06 |  |
| [[EAPP]] | -0.66 | -0.49 / -0.73 | both halves | 1e-05 |  |
| [[RNF181]] | -0.64 | -0.52 / -0.65 | both halves | 1e-05 |  |
| [[GABARAPL2]] | -0.64 | -0.50 / -0.69 | both halves | 1e-05 |  |
| [[ATXN3]] | -0.64 | -0.60 / -0.65 | both halves | 7e-06 |  |
| [[UBE2B]] | -0.64 | -0.51 / -0.75 | both halves | 1e-05 |  |
| [[SYF2]] | -0.63 | -0.39 / -0.73 | both halves | 6e-05 |  |
| [[FTL]] | -0.63 | -0.55 / -0.66 | both halves | 1e-05 |  |
| [[FAM182B]] | -0.63 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[CAMLG]] | -0.63 | -0.60 / -0.66 | both halves | 7e-06 |  |
| [[FBXL20]] | -0.62 | -0.61 / -0.59 | both halves | 7e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.605). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-19.0, -33.3); signed map (-6.7, -44.6). **Vector** length 101, 28.4% of its response variance represented; |z| ≥ 3 in 964 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +8.0 | +8.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +7.9 | +14.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +7.1 | +11.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +7.1 | +16.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | +5.8 | +9.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | +4.1 | +4.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.0 | +4.7 |
|  | [[EX229 (drug)]] 5 µM |  | +3.8 | +5.0 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.5 | +3.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.5 | +3.6 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.7 | -1.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | +0.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.5 | +0.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -2.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.3 | -0.8 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -2.2 | -1.9 |
|  | [[Adagrasib (drug)]] 5 µM |  | -1.9 | -2.1 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | -1.9 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | valyl-tRNA synthetase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.33 — chr6:31,777,518-31,795,752 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously VARS2, VARS |
| Gene groups (HGNC) | Aminoacyl tRNA synthetases, Class I |
| Reactome | 3 pathways, smallest: Cytosolic tRNA aminoacylation; tRNA Aminoacylation; Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [P26640](https://www.uniprot.org/uniprotkb/P26640) (Valine--tRNA ligase):

> Catalyzes the attachment of valine to tRNA(Val).

**Summary**, from NCBI Gene [7407](https://www.ncbi.nlm.nih.gov/gene/7407):

> Aminoacyl-tRNA synthetases catalyze the aminoacylation of tRNA by their cognate amino acid. Because of their central role in linking amino acids with nucleotide triplets contained in tRNAs, aminoacyl-tRNA synthetases are thought to be among the first proteins that appeared in evolution. The protein encoded by this gene belongs to class-I aminoacyl-tRNA synthetase family and is located in the class III region of the major histocompatibility complex. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:12651](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12651) · Entrez [7407](https://www.ncbi.nlm.nih.gov/gene/7407) · UniProt [P26640](https://www.uniprot.org/uniprotkb/P26640) · Ensembl [ENSG00000204394](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204394)

## Data

Gene col 12868: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12868); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12868, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12868]; `tensor/DDL_lfc|DDL_z.npy` [12868]; `embed/gene_vectors.npy` [12868]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12868 or target_col == 12868). Every well: [[VARS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VARS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
