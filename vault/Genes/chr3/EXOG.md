---
symbol: "EXOG"
type: "gene"
col: 8037
ensembl_id: "ENSG00000157036"
name: "exo/endonuclease G"
location: "3p22.2"
module: 4
arm: "+"
pooled_cpm: 22.03
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 5
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# EXOG

*exo/endonuclease G* — 3p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.79× (z +11.3, q 1e-26, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.769× (z -7.3, q 2e-10, down in 25 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 8 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 4 lines (SW480 0.113×, LOX-IMVI 0.0610×, RKO 0.255×, A-427 0.253×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (A-427 0.146×, SW480 0.310×, RKO 0.221×, HepG2/C3A 0.106×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (RKO 0.453×, HEC-1-A 0.541×, LOX-IMVI 0.472×); [[Baicalin (drug)]] 0.5 µM in 1 line (SW 1271 0.0800×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM168]] (+0.65, fdr 1e-05), [[YLPM1]] (+0.64, fdr 7e-06), [[COA1]] (+0.61, fdr 1e-05); moves opposite to [[FAM117A]] (-0.57, fdr 7e-05), [[PMS2P4-1]] (-0.54, fdr 3e-05), [[LASP1]] (-0.54, fdr 2e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MVB12B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8037.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.79×** | +11.3 | 1e-26 | 38/48 (HOP62, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.70×** | +9.9 | 1e-20 | 35/47 (KATO III, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.62×** | +9.4 | 1e-18 | 34/48 (A-172, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.60×** | +9.0 | 3e-17 | 37/47 (NCI-H2347, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.56×** | +8.6 | 7e-16 | 30/47 (A-172, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +6.6 | 4e-09 | 1/48 (C32) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.51×** | +6.5 | 6e-09 | 26/48 (NCI-H2347, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.42×** | +6.5 | 7e-09 | 19/47 (LoVo, SW480, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +4.7 | 2e-04 | 13/48 (NCI-H2347, NCI-H1573, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.27×** | +4.6 | 2e-04 | 18/47 (RPMI-7951, Panc 03.27, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.25×** | +4.2 | 0.001 | 16/48 (NCI-H23, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.52×** | +4.2 | 0.001 | 7/48 (NCI-H2347, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.23×** | +3.9 | 0.004 | 15/48 (SW480, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.22×** | +3.9 | 0.004 | 11/47 (NCI-H460, NCI-H23, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.21×** | +3.6 | 0.012 | 13/47 (RPMI-7951, NCI-H1573, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.20×** | +3.5 | 0.014 | 10/46 (NCI-H2347, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.18× | +3.2 | 0.046 | 8/48 (C-33 A, NCI-H2347, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.19× | +3.1 | 0.068 | 11/47 (A549, SW48, …) | all doses, flat | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | 1.18× | +3.0 | 0.075 | 6/46 (SW480, Panc 03.27, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8037.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 8 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 4 lines (SW480 0.113×, LOX-IMVI 0.0610×, RKO 0.255×, A-427 0.253×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (A-427 0.146×, SW480 0.310×, RKO 0.221×, HepG2/C3A 0.106×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (RKO 0.453×, HEC-1-A 0.541×, LOX-IMVI 0.472×); [[Baicalin (drug)]] 0.5 µM in 1 line (SW 1271 0.0800×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.769×** | -7.3 | 2e-10 | 25/47 (RKO, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.687×** | -6.8 | 3e-09 | 17/40 (SW480, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.767×** | -5.1 | 6e-05 | 19/44 (A-427, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.782×** | -4.6 | 5e-04 | 13/32 (NCI-H1792, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **0.810×** | -4.1 | 0.004 | 13/47 (SW480, HEC-1-A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8037. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 43.7 | 0 | 4 (3 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.298× (z -12.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.541× (z -9.4) |
| [[A-427 (line)]] | wt | 38.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.146× (z -17.7) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 24.8 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.291× (z -11.8) ⚠ cell-cycle shift, explains ~14% of this change |
| [[RKO (line)]] | wt | 53.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.221× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.453× (z -10.6) |
| [[J82 (line)]] | alt | 13.8 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0444× (z -20.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 17.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.205× (z -10.8) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 25.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0610× (z -20.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.472× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 28.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.19× (z +8.6) ⚠ toxic; transcription drop | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.258× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 41.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.113× (z -26.8) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 57.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.291× (z -10.0) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 19.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.106× (z -10.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 38.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.207× (z -12.7) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 22.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.184× (z -9.0) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 50.2 | 0 | 1 | — | [[Baicalin (drug)]] 0.5 µM 0.0800× (z -8.7) |
| [[SW1417 (line)]] | alt | 35.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.308× (z -10.5) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 40.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.190× (z -9.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.33 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.56 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.14 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.08 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 37.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8037), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM168]] | +0.65 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[YLPM1]] | +0.64 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[COA1]] | +0.61 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[EIF2B3]] | +0.61 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[INTS7]] | +0.61 | +0.49 / +0.65 | both halves | 1e-05 |  |
| [[RAD51D]] | +0.61 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[TSEN2]] | +0.60 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[AGK]] | +0.58 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[SNRPD1]] | +0.58 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[RAD54L2]] | +0.58 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[ACSF3]] | +0.58 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[UQCC2]] | +0.58 | +0.42 / +0.65 | both halves | 4e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM117A]] | -0.57 | -0.37 / -0.49 | both halves | 7e-05 |  |
| [[PMS2P4-1]] | -0.54 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[LASP1]] | -0.54 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[STX5-DT]] | -0.54 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[OSER1-DT]] | -0.53 | -0.31 / -0.49 | both halves | 2e-04 |  |
| [[GNAS]] | -0.53 | -0.39 / -0.61 | both halves | 5e-05 |  |
| [[KIAA1191]] | -0.52 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[ZFC3H1]] | -0.51 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[AAMDC]] | -0.50 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[NDUFV2-AS1]] | -0.50 | -0.18 / -0.50 | ⚠ not reproduced | 9e-04 |  |
| [[CNGB3]] | -0.50 | -0.32 / -0.45 | both halves | 2e-04 |  |
| [[SLC6A8]] | -0.49 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[PIK3C2A]] | -0.49 | -0.45 / -0.53 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MVB12B]] | B | MVB12B activity raises EXOG's level | lines that do not express MVB12B (6) vs lines expressing it (44) | 2.06× lower at baseline in the lines without MVB12B | 0.048 | ⚠ within organs, on part of the lines; co-occurs with SMAD4; also absent: PDE5A, TSEN2, TYMSOS; maybe low, not absent |
| [[AADAT]] | B | AADAT activity raises EXOG's level | lines that do not express AADAT (5) vs lines expressing it (45) | 1.58× lower at baseline in the lines without AADAT | 0.072 | ⚠ within organs, on part of the lines; also absent: GGH, LINC01341, HHAT; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.540). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-18.6, -41.2); signed map (-9.8, -47.3). **Vector** length 81.1, 15.1% of its response variance represented; |z| ≥ 3 in 915 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +5.8 | +9.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.8 | +9.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.7 | +4.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.5 | +6.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | +3.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.0 | +3.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.9 | +3.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.8 | +3.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.3 | -7.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.9 | -1.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | -2.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.3 | -1.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | -0.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -1.9 | -4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.6 | -2.9 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.5 | -1.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.5 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | exo/endonuclease G |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p22.2 — chr3:38,496,127-38,542,161 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ENGL-a, ENGL, ENGL-b; previously ENDOGL1, ENDOGL2 |
| Reactome | 2 pathways, smallest: Strand-asynchronous mitochondrial DNA replication; DNA Replication |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2C4](https://www.uniprot.org/uniprotkb/Q9Y2C4) (Nuclease EXOG, mitochondrial):

> Endo/exonuclease with nicking activity towards supercoiled DNA, a preference for single-stranded DNA and 5'-3' exonuclease activity.

**Summary**, from NCBI Gene [9941](https://www.ncbi.nlm.nih.gov/gene/9941):

> This gene encodes an endo/exonuclease with 5'-3' exonuclease activity. The encoded enzyme catalyzes the hydrolysis of ester linkages at the 5' end of a nucleic acid chain. This enzyme is localized to the mitochondria and may play a role in programmed cell death. Alternatively spliced transcript variants have been described. A pseudogene exists on chromosome 18. [provided by RefSeq, Feb 2009]

**Accessions** — [HGNC:3347](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3347) · Entrez [9941](https://www.ncbi.nlm.nih.gov/gene/9941) · UniProt [Q9Y2C4](https://www.uniprot.org/uniprotkb/Q9Y2C4) · Ensembl [ENSG00000157036](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157036)

## Data

Gene col 8037: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8037); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8037, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8037]; `tensor/DDL_lfc|DDL_z.npy` [8037]; `embed/gene_vectors.npy` [8037]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8037 or target_col == 8037). Every well: [[EXOG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EXOG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
