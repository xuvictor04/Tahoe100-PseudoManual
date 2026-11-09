---
symbol: "TFCP2L1"
type: "gene"
col: 3623
ensembl_id: "ENSG00000115112"
name: "transcription factor CP2 like 1"
location: "2q14.2"
module: 98
arm: "+"
pooled_cpm: 9.9
n_lines_expressing: 28
n_dd_up: 55
n_dd_down: 2
n_dd_up_clean: 36
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 4
tags: ["gene", "module/098"]
generated_by: "tahoemap"
---

# TFCP2L1

*transcription factor CP2 like 1* — 2q14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 55 drug-doses (19 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.70× (z +26.8, q 0e+00, up in 22 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 0.527× (z -4.9, q 6e-04, down in 15 of 26 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SW1417 0.273×, A-427 0.231×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H2030 0.270×, SW1417 0.374×; ⚠ toxic; cell-cycle shift, explains ~44% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SW1417 0.322×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TLR2]] (+0.63, fdr 7e-06), [[FKBP5]] (+0.61, fdr 7e-06), [[VSTM2L]] (+0.59, fdr 8e-06); moves opposite to [[FANK1]] (-0.44, fdr 3e-05), [[EXOC3]] (-0.44, fdr 5e-05), [[DCDC1]] (-0.43, fdr 3e-04).
> It is in [[Module 098]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 4 go from it, the strongest it → [[PLXNA2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 55 in all, 19 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 55 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3623.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.70×** | +26.8 | 0e+00 | 22/26 (SW480, A549, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ position correction uncertain | **2.76×** | +20.8 | 0e+00 | 19/24 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **3.44×** | +17.9 | 0e+00 | 19/26 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **2.20×** | +16.1 | 0e+00 | 18/26 (LS 180, HT-29, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.61×** | +13.9 | 1e-41 | 19/26 (PANC-1, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.57×** | +13.6 | 2e-40 | 20/26 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.13×** | +10.5 | 7e-24 | 18/25 (SW480, SW 900, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.02×** | +10.1 | 3e-22 | 18/26 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.02×** | +9.7 | 1e-20 | 15/25 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.96×** | +9.3 | 6e-19 | 14/26 (SW480, RKO, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ position correction uncertain | **1.89×** | +9.2 | 2e-18 | 17/24 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM | ⚠ position correction uncertain | **1.78×** | +8.3 | 6e-15 | 9/26 (Panc 03.27, CFPAC-1, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.76×** | +8.1 | 2e-14 | 17/26 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **1.79×** | +8.1 | 3e-14 | 1/9 (SW480) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM | ⚠ position correction uncertain | **1.75×** | +8.1 | 3e-14 | 17/26 (SW 900, SW480, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 0.05 µM |  | **1.72×** | +7.8 | 2e-13 | 9/26 (Panc 03.27, NCI-H2347, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.45×** | +7.6 | 1e-12 | 11/26 (SW480, CFPAC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.68×** | +7.5 | 2e-12 | 13/26 (HT-29, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Budesonide (drug)]] 5 µM |  | **1.64×** | +7.1 | 3e-11 | 9/26 (Panc 03.27, NCI-H2347, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **1.62×** | +7.0 | 8e-11 | 8/26 (Panc 03.27, NCI-H2347, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.65×** | +6.9 | 1e-10 | 10/26 (Panc 03.27, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.60×** | +6.7 | 4e-10 | 10/26 (J82, SW 900, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Dexamethasone (drug)]] 5 µM |  | **1.51×** | +5.9 | 7e-08 | 8/26 (Panc 03.27, NCI-H2347, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.48×** | +5.6 | 4e-07 | 8/26 (Panc 03.27, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.48×** | +5.6 | 4e-07 | 7/25 (NCI-H2347, Panc 03.27, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3623.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SW1417 0.273×, A-427 0.231×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H2030 0.270×, SW1417 0.374×; ⚠ toxic; cell-cycle shift, explains ~44% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SW1417 0.322×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.527×** | -4.9 | 6e-04 | 15/26 (AsPC-1, NCI-H2030, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.593×** | -4.0 | 0.019 | 7/24 (SW480, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Busulfan (drug)]] 5 µM |  | 0.843× | -3.6 | 0.064 | 3/26 (J82, RKO, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.57 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3623. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 41.3 | 19 (4 ⚠) | 0 | [[Phenylephrine (hydrochloride) (drug)]] 5 µM 4.90× (z +12.9) | — |
| [[Panc 03.27 (line)]] | alt | 41.2 | 19 (4 ⚠) | 0 | [[Budesonide (drug)]] 5 µM 7.59× (z +13.8) | — |
| [[CFPAC-1 (line)]] | alt | 7.47 | 13 (4 ⚠) | 0 | [[Budesonide (drug)]] 0.5 µM 14.3× (z +10.3) | — |
| [[SW480 (line)]] | alt | 23.1 | 9 (6 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.90× (z +17.8) | — |
| [[PANC-1 (line)]] | alt | 4.80 | 5 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 8.48× (z +10.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Betamethasone dipropionate (drug)]] 5 µM 6.09× (z +8.5) | — |
| [[SW1417 (line)]] | alt | 72.3 | 1 (1 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +13.4) ⚠ position correction uncertain | [[Dinaciclib (drug)]] 0.5 µM 0.273× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[COLO 205 (line)]] | alt | 7.78 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.3× (z +11.6) ⚠ position correction uncertain · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.25× (z +8.5) | — |
| [[SW 900 (line)]] | alt | 9.61 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.7× (z +11.8) ⚠ position correction uncertain · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.75× (z +8.7) | — |
| [[A-427 (line)]] | wt | 22.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.231× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[A549 (line)]] | wt | 12.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.34× (z +11.6) | — |
| [[HEC-1-A (line)]] | alt | 2.54 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.4× (z +10.2) | — |
| [[HT-29 (line)]] | alt | 3.80 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 7.19× (z +8.6) | — |
| [[KATO III (line)]] | alt | 12.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.67× (z +9.2) | — |
| [[LS 180 (line)]] | wt | 3.15 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 7.41× (z +8.7) | — |
| [[NCI-H2030 (line)]] | alt | 24.2 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.270× (z -9.8) ⚠ toxic; cell-cycle shift, explains ~44% of this change |
| [[RKO (line)]] | wt | 13.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.97× (z +10.1) | — |
| [[A-172 (line)]] | wt | 0.912 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.837 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.16 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.745 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.10 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.920 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.964 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.80 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.756 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.974 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.03 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.48 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.94 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.824 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.841 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.836 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.18 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 19.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3623), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TLR2]] | +0.63 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[FKBP5]] | +0.61 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[VSTM2L]] | +0.59 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[MT1M]] | +0.54 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[MAP3K6]] | +0.53 | +0.41 / +0.42 | both halves | 4e-05 |  |
| [[MAOA]] | +0.52 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[MAFB]] | +0.51 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[ADAMTSL4]] | +0.51 | +0.43 / +0.46 | both halves | 3e-05 |  |
| [[MT1F]] | +0.50 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[PHACTR3]] | +0.50 | +0.35 / +0.60 | both halves | 1e-04 |  |
| [[FGD4]] | +0.50 | +0.42 / +0.52 | both halves | 4e-05 |  |
| [[SH3TC1]] | +0.49 | +0.46 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FANK1]] | -0.44 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[EXOC3]] | -0.44 | -0.39 / -0.42 | both halves | 5e-05 |  |
| [[DCDC1]] | -0.43 | -0.33 / -0.29 | both halves | 3e-04 |  |
| [[DNAH7]] | -0.42 | -0.35 / -0.23 | both halves | 5e-04 |  |
| [[LRP1B]] | -0.42 | -0.33 / -0.40 | both halves | 1e-04 |  |
| [[CDKN2A]] | -0.40 | -0.37 / -0.43 | both halves | 8e-05 |  |
| [[IQCK]] | -0.40 | -0.27 / -0.43 | both halves | 3e-04 |  |
| [[MID1]] | -0.39 | -0.35 / -0.32 | both halves | 1e-04 |  |
| [[C11orf54]] | -0.39 | -0.40 / -0.37 | both halves | 8e-05 |  |
| [[PRXL2A]] | -0.39 | -0.43 / -0.31 | both halves | 2e-04 |  |
| [[BAIAP2-DT]] | -0.38 | -0.42 / -0.38 | both halves | 7e-05 |  |
| [[SPINT2]] | -0.38 | -0.46 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TFCP2L1's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 9.2% of all compounds | 0.017 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[SPINT2]] | C | SPINT2 activity raises TFCP2L1's level | lines that do not express SPINT2 (24) vs lines expressing it (26) | 4.09× lower at baseline in the lines without SPINT2 | 0.026 | ⚠ within organs, on part of the lines; also absent: ENSG00000267748, SLC52A3, ENTPD2; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLXNA2]] | B | TFCP2L1 activity lowers PLXNA2's level | lines that do not express TFCP2L1 (22) vs lines expressing it (28) | 2.06× higher at baseline in the lines without TFCP2L1 | 0.031 | ⚠ within organs, on part of the lines; also absent: ENSG00000267748, OCLN, SPINT2 |
| [[FGD4]] | B | TFCP2L1 activity raises FGD4's level | lines that do not express TFCP2L1 (22) vs lines expressing it (28) | 3.14× lower at baseline in the lines without TFCP2L1 | 0.033 | ⚠ within organs, on part of the lines; also absent: ENSG00000267748, OCLN, SPINT2 |
| [[AFAP1L1]] | B | TFCP2L1 activity lowers AFAP1L1's level | lines that do not express TFCP2L1 (22) vs lines expressing it (28) | 1.77× higher at baseline in the lines without TFCP2L1 | 0.072 | ⚠ within organs, on part of the lines; also absent: ENSG00000267748, OCLN, SPINT2 |
| [[SPINT2]] | C | TFCP2L1 activity raises SPINT2's level | lines that do not express TFCP2L1 (22) vs lines expressing it (28) | 8.96× lower at baseline in the lines without TFCP2L1 | 5e-04 | ⚠ within organs, on part of the lines; also absent: ENSG00000267748, OCLN, SPINT2; co-absent with the target |

## Where it sits

- **Module**: [[Module 098]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.587). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (29.8, 15.1); signed map (17.1, 31.4). **Vector** length 81.1, 19.9% of its response variance represented; |z| ≥ 3 in 828 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +26.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.3 | +8.1 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +3.0 | +7.8 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +3.0 | +5.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +16.1 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.6 | +7.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.6 | +4.3 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -3.3 | -4.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.3 | -4.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.3 | +1.1 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -1.6 | -3.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.5 | -0.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | +0.0 |

## What is on record

|  |  |
|---|---|
| Name | transcription factor CP2 like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q14.2 — chr2:121,216,587-121,285,202 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LBP-9, CRTR1 |
| Gene groups (HGNC) | Transcription factor CP2 family |
| Hallmark sets | BILE_ACID_METABOLISM, KRAS_SIGNALING_DN |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NZI6](https://www.uniprot.org/uniprotkb/Q9NZI6) (Transcription factor CP2-like protein 1):

> Transcription factor that facilitates establishment and maintenance of pluripotency in embryonic stem cells (ESCs). With KLF2, acts as the major effector of self-renewal that mediates induction of pluripotency downstream of LIF/STAT3 and Wnt/beta-catenin signaling (By similarity). Required for normal duct development in the salivary gland and kidney (By similarity). Coordinates the development of the kidney collecting ducts intercalated (IC) and principal (PC) cells, which regulate acid-base …

**Summary**, from NCBI Gene [29842](https://www.ncbi.nlm.nih.gov/gene/29842):

> Enables RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Involved in regulation of transcription by RNA polymerase II. Predicted to be located in chromatin. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17925](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17925) · Entrez [29842](https://www.ncbi.nlm.nih.gov/gene/29842) · UniProt [Q9NZI6](https://www.uniprot.org/uniprotkb/Q9NZI6) · Ensembl [ENSG00000115112](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115112)

## Data

Gene col 3623: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3623); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3623, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3623]; `tensor/DDL_lfc|DDL_z.npy` [3623]; `embed/gene_vectors.npy` [3623]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3623 or target_col == 3623). Every well: [[TFCP2L1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TFCP2L1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
