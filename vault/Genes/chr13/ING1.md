---
symbol: "ING1"
type: "gene"
col: 7724
ensembl_id: "ENSG00000153487"
name: "inhibitor of growth family member 1"
location: "13q34"
module: 4
arm: "-"
pooled_cpm: 22.37
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 3
n_dd_up_clean: 9
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# ING1

*inhibitor of growth family member 1* — 13q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.80× (z +25.3, q 0e+00, up in 44 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.683× (z -5.0, q 4e-04, down in 20 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Trametinib (drug)]] 0.05 µM: 0.827× (z -3.6, q 0.071, down in 20 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (NCI-H2347 0.210×, HT-29 0.267×, J82 0.235×, Hs 766T 0.248×; ⚠ toxic; transcription drop); [[AZD2858 (drug)]] 0.5 µM in 1 line (BT-474 0.0801×; ⚠ toxic); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H2347 0.304×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GCAT]] (+0.66, fdr 7e-06), [[FBXO33]] (+0.64, fdr 1e-05), [[CDKN2D]] (+0.62, fdr 1e-05); moves opposite to [[NAA50]] (-0.65, fdr 7e-06), [[LARP4]] (-0.64, fdr 9e-06), [[TMEM33]] (-0.63, fdr 1e-05).
> It sits in the **-** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[EPHB3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠; shown: the 15 strongest. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7724.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.80×** | +25.3 | 0e+00 | 44/47 (NCI-H1573, C32, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.37×** | +11.6 | 2e-28 | 43/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.29×** | +11.1 | 3e-26 | 45/47 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.23×** | +10.7 | 1e-24 | 44/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +10.0 | 2e-21 | 39/47 (AsPC-1, RKO, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.05×** | +9.6 | 7e-20 | 33/47 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.63×** | +6.3 | 3e-08 | 31/48 (COLO 205, C32, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.14×** | +5.3 | 7e-06 | 31/48 (NCI-H460, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | **1.47×** | +5.1 | 2e-05 | 24/46 (SW48, NCI-H460, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.46×** | +5.0 | 3e-05 | 24/48 (SW48, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.38×** | +4.3 | 9e-04 | 24/46 (SNU-423, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.82×** | +4.2 | 0.001 | 21/45 (Hs 766T, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.36×** | +4.1 | 0.002 | 19/46 (A-172, SNU-423, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.35×** | +4.0 | 0.003 | 17/47 (NCI-H460, SW480, …) | rises with dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~63% of this change | **1.33×** | +3.7 | 0.009 | 24/45 (PANC-1, J82, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7724.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (NCI-H2347 0.210×, HT-29 0.267×, J82 0.235×, Hs 766T 0.248×; ⚠ toxic; transcription drop); [[AZD2858 (drug)]] 0.5 µM in 1 line (BT-474 0.0801×; ⚠ toxic); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H2347 0.304×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.683×** | -5.0 | 4e-04 | 20/35 (NCI-H2347, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.740×** | -3.6 | 0.071 | 12/48 (NCI-H23, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.827×** | -3.6 | 0.071 | 20/48 (A-427, SW480, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | 0.786× | -3.3 | 0.13 | 19/41 (NCI-H2347, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.787× | -3.3 | 0.13 | 15/47 (A498, NCI-H2347, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.854× | -3.0 | 0.20 | 17/48 (HT-29, A-427, …) | rises with dose | low cells (technical?) |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.790× | -3.0 | 0.20 | 9/47 (NCI-H2347, SW 900, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7724. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 15.6 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +23.3) | — |
| [[KATO III (line)]] | alt | 27.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +12.8) | — |
| [[SW1417 (line)]] | alt | 23.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +10.1) | — |
| [[SW480 (line)]] | alt | 35.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +16.7) | — |
| [[C32 (line)]] | wt | 29.3 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 18.9× (z +24.6) | — |
| [[COLO 205 (line)]] | alt | 32.9 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 15.8× (z +22.4) | — |
| [[J82 (line)]] | alt | 32.6 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.235× (z -9.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 31.4 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +24.7) | — |
| [[NCI-H2347 (line)]] | alt | 22.8 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.210× (z -11.6) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 26.7 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.57× (z +11.8) | — |
| [[A498 (line)]] | wt | 26.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.33× (z +16.2) | — |
| [[A549 (line)]] | wt | 13.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.84× (z +13.7) | — |
| [[AsPC-1 (line)]] | alt | 15.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.59× (z +16.2) | — |
| [[BT-474 (line)]] | alt | 20.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +9.6) | [[AZD2858 (drug)]] 0.5 µM 0.0801× (z -9.7) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 29.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.06× (z +15.0) | [[Dinaciclib (drug)]] 5 µM 0.248× (z -8.8) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 37.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.267× (z -11.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 21.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.06× (z +20.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 16.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.42× (z +13.6) | — |
| [[Panc 03.27 (line)]] | alt | 32.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +10.4) | — |
| [[PANC-1 (line)]] | alt | 10.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.48× (z +17.5) | — |
| [[A-172 (line)]] | wt | 24.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +10.7) | — |
| [[CFPAC-1 (line)]] | alt | 18.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.79× (z +11.8) | — |
| [[HEC-1-A (line)]] | alt | 24.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +10.4) | — |
| [[HOP62 (line)]] | alt | 20.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.70× (z +15.9) | — |
| [[HS-578T (line)]] | alt | 28.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.81× (z +15.8) | — |
| [[hTERT-HPNE (line)]] | wt | 20.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.48× (z +15.3) | — |
| [[LOX-IMVI (line)]] | wt | 24.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.69× (z +14.8) | — |
| [[LS 180 (line)]] | wt | 18.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.83× (z +14.4) | — |
| [[NCI-H1792 (line)]] | alt | 11.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.4× (z +12.9) | — |
| [[NCI-H23 (line)]] | alt | 18.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.76× (z +13.6) | — |
| [[RKO (line)]] | wt | 17.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.40× (z +8.9) | — |
| [[RPMI-7951 (line)]] | alt | 23.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.97× (z +13.0) | — |
| [[SK-MEL-2 (line)]] | alt | 14.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +10.3) | — |
| [[SNU-423 (line)]] | alt | 18.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.47× (z +19.2) | — |
| [[SW 900 (line)]] | alt | 22.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +10.0) | — |
| [[A-427 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.07 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7724), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GCAT]] | +0.66 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[FBXO33]] | +0.64 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[CDKN2D]] | +0.62 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[CDK2AP2]] | +0.62 | +0.40 / +0.67 | both halves | 5e-05 |  |
| [[BCL2L12]] | +0.61 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[PIM2]] | +0.61 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[DNAAF3]] | +0.61 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[RNASE4]] | +0.60 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[RARA]] | +0.59 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[ANKRD37]] | +0.59 | +0.36 / +0.63 | both halves | 1e-04 |  |
| [[KATNA1]] | +0.59 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[FSCN1]] | +0.59 | +0.61 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAA50]] | -0.65 | -0.63 / -0.59 | both halves | 7e-06 |  |
| [[LARP4]] | -0.64 | -0.57 / -0.58 | both halves | 9e-06 |  |
| [[TMEM33]] | -0.63 | -0.55 / -0.65 | both halves | 1e-05 |  |
| [[ZNF346]] | -0.62 | -0.59 / -0.46 | both halves | 3e-05 |  |
| [[COMT]] | -0.61 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[TMX3]] | -0.60 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[ATXN10]] | -0.60 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[SLC35B4]] | -0.59 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[NAA25]] | -0.59 | -0.57 / -0.64 | both halves | 1e-05 |  |
| [[ARPP19]] | -0.58 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[TANGO6]] | -0.58 | -0.52 / -0.61 | both halves | 1e-05 |  |
| [[PEX26]] | -0.57 | -0.54 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPHB3]] | B | EPHB3 activity raises ING1's level | lines that do not express EPHB3 (15) vs lines expressing it (35) | 1.30× lower at baseline in the lines without EPHB3 | 0.071 | ⚠ within organs, on part of the lines; also absent: SLC7A8, MCF2L, ENPP5; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **-** arm (projection on the module's main direction -0.587). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-22.7, -30.2); signed map (-25.1, 15.7). **Vector** length 85.8, 19.7% of its response variance represented; |z| ≥ 3 in 951 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.0 | +25.3 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.6 | +11.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.3 | +4.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.3 | +11.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.3 | +10.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.3 | +1.6 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.5 | +0.4 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | +1.4 | +1.4 |
|  | [[Cloxacillin (sodium) (drug)]] 0.05 µM |  | +1.3 | +1.8 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -8.0 | -5.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -7.3 | -3.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.7 | -0.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -5.4 | +0.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.9 | -3.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.8 | +1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.3 | +0.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.3 | -2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | +0.2 |
|  | [[EX229 (drug)]] 5 µM |  | -2.5 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | inhibitor of growth family member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q34 — chr13:110,712,736-110,723,339 (+) |
| Ensembl biotype | protein_coding |
| Also known as | p33ING1, p33ING1b, p24ING1c, p33, p47, p47ING1a |
| Gene groups (HGNC) | PHD finger proteins; Inhibitor of growth family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UK53](https://www.uniprot.org/uniprotkb/Q9UK53) (Inhibitor of growth protein 1):

> Cooperates with p53/TP53 in the negative regulatory pathway of cell growth by modulating p53-dependent transcriptional activation. Implicated as a tumor suppressor gene.

**Summary**, from NCBI Gene [3621](https://www.ncbi.nlm.nih.gov/gene/3621):

> This gene encodes a tumor suppressor protein that can induce cell growth arrest and apoptosis. The encoded protein is a nuclear protein that physically interacts with the tumor suppressor protein TP53 and is a component of the p53 signaling pathway. Reduced expression and rearrangement of this gene have been detected in various cancers. Multiple alternatively spliced transcript variants encoding distinct isoforms have been reported. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6062](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6062) · Entrez [3621](https://www.ncbi.nlm.nih.gov/gene/3621) · UniProt [Q9UK53](https://www.uniprot.org/uniprotkb/Q9UK53) · Ensembl [ENSG00000153487](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153487)

## Data

Gene col 7724: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7724); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7724, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7724]; `tensor/DDL_lfc|DDL_z.npy` [7724]; `embed/gene_vectors.npy` [7724]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7724 or target_col == 7724). Every well: [[ING1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ING1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
