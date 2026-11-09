---
symbol: "NADSYN1"
type: "gene"
col: 10311
ensembl_id: "ENSG00000172890"
name: "NAD synthetase 1"
location: "11q13.4"
module: 15
arm: "+"
pooled_cpm: 35.26
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 7
n_dd_up_clean: 7
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# NADSYN1

*NAD synthetase 1* — 11q13.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.59× (z +12.8, q 7e-35, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.660× (z -11.5, q 8e-28, down in 31 of 47 measured lines) ⚠ cell-cycle shift, explains ~70% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.672× (z -11.0, q 1e-25, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BCL2L2-PABPN1]] (+0.66, fdr 7e-06), [[BCL2L2]] (+0.63, fdr 1e-05), [[GPALPP1]] (+0.62, fdr 1e-05); moves opposite to [[MT1G]] (-0.60, fdr 4e-05), [[IER2]] (-0.55, fdr 2e-05), [[ARL4A]] (-0.54, fdr 4e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10311.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +12.8 | 7e-35 | 37/48 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +9.1 | 2e-17 | 37/47 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +6.9 | 1e-09 | 29/48 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.38×** | +6.3 | 3e-08 | 31/48 (LoVo, KATO III, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.37×** | +6.0 | 2e-07 | 26/46 (NCI-H460, A-427, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.33×** | +5.6 | 3e-06 | 22/48 (A549, RKO, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.33×** | +5.5 | 4e-06 | 27/47 (HOP62, NCI-H23, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.20× | +5.0 | 4e-05 | 19/48 (A549, A-427, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.17× | +4.4 | 6e-04 | 21/48 (NCI-H460, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.50×** | +4.2 | 0.002 | 10/48 (SW480, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.21×** | +4.0 | 0.003 | 14/48 (NCI-H23, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.15× | +3.9 | 0.006 | 15/48 (NCI-H23, NCI-H1573, …) | all doses, flat |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.14× | +3.8 | 0.007 | 7/48 (LOX-IMVI, NCI-H2030, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.4 | 0.031 | 15/48 (NCI-H1573, NCI-H2030, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~90% of this change | 1.20× | +3.3 | 0.031 | 16/48 (SK-MEL-2, SW48, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.18× | +3.2 | 0.046 | 17/48 (NCI-H460, A-427, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.18× | +3.1 | 0.068 | 7/48 (NCI-H23, LoVo, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.15× | +3.0 | 0.072 | 10/48 (A-427, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.34×** | +3.0 | 0.072 | 6/48 (NCI-H23, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.17× | +3.0 | 0.074 | 11/47 (NCI-H23, HepG2/C3A, …) | all doses, flat |  |
| [[Roxadustat (drug)]] 5 µM |  | 1.17× | +3.0 | 0.076 | 8/47 (HEC-1-A, C32, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10311.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.660×** | -11.5 | 8e-28 | 31/47 (C32, HT-29, …) | rises with dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.672×** | -11.0 | 1e-25 | 40/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.576×** | -10.4 | 6e-23 | 37/48 (SW480, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.645×** | -8.6 | 1e-15 | 32/47 (C32, SW1417, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.675×** | -7.7 | 2e-12 | 34/48 (C32, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.734×** | -6.0 | 1e-07 | 26/48 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | **0.818×** | -3.9 | 0.008 | 17/48 (PANC-1, HEC-1-A, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~64% of this change | 0.846× | -3.1 | 0.12 | 15/47 (SW 1271, NCI-H1792, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10311. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 32.5 | 4 (1 ⚠) | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.71× (z +16.0) | [[Homoharringtonine (drug)]] 5 µM 0.494× (z -11.3) ⚠ cell-cycle shift, explains ~70% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.581× (z -8.7) |
| [[A549 (line)]] | wt | 33.8 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.14× (z +13.4) | — |
| [[RKO (line)]] | wt | 41.9 | 3 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.05× (z +12.6) | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -11.6) ⚠ cell-cycle shift, explains ~70% of this change |
| [[C32 (line)]] | wt | 58.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -14.3) ⚠ cell-cycle shift, explains ~70% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.334× (z -9.4) |
| [[LoVo (line)]] | wt | 33.3 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.85× (z +16.8) | — |
| [[A498 (line)]] | wt | 15.4 | 2 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 5.08× (z +12.7) | — |
| [[LOX-IMVI (line)]] | wt | 22.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.18× (z +12.9) | — |
| [[LS 180 (line)]] | wt | 55.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.73× (z +13.2) | — |
| [[NCI-H23 (line)]] | alt | 50.3 | 1 | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.73× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -12.9) ⚠ cell-cycle shift, explains ~70% of this change |
| [[SW480 (line)]] | alt | 53.1 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.474× (z -9.1) |
| [[A-427 (line)]] | wt | 38.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.479× (z -8.6) ⚠ cell-cycle shift, explains ~70% of this change |
| [[C-33 A (line)]] | alt | 26.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0468× (z -17.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 30.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -11.3) ⚠ cell-cycle shift, explains ~70% of this change |
| [[COLO 205 (line)]] | alt | 29.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.233× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 45.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -8.9) ⚠ cell-cycle shift, explains ~70% of this change |
| [[HT-29 (line)]] | alt | 41.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -14.1) ⚠ cell-cycle shift, explains ~70% of this change |
| [[NCI-H2030 (line)]] | alt | 17.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +9.7) | — |
| [[Panc 03.27 (line)]] | alt | 40.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -11.4) ⚠ cell-cycle shift, explains ~70% of this change |
| [[SNU-1 (line)]] | wt | 36.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 31.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.387× (z -8.7) ⚠ cell-cycle shift, explains ~33% of this change |
| [[SW48 (line)]] | wt | 29.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.75× (z +14.2) | — |
| [[A-172 (line)]] | wt | 52.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 33.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 40.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 35.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10311), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCL2L2-PABPN1]] | +0.66 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[BCL2L2]] | +0.63 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[GPALPP1]] | +0.62 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[GARS1-DT]] | +0.60 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[SAP30L-AS1]] | +0.57 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[FBXO22]] | +0.57 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[EI24]] | +0.57 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[FAM185A]] | +0.56 | +0.30 / +0.54 | both halves | 2e-04 |  |
| [[TMEM68]] | +0.55 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[SLC12A9]] | +0.55 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[REXO2]] | +0.55 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[NBR2]] | +0.55 | +0.53 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MT1G]] | -0.60 | -0.43 / -0.58 | both halves | 4e-05 |  |
| [[IER2]] | -0.55 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[ARL4A]] | -0.54 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[ZNF184]] | -0.53 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[ANKRD44]] | -0.52 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[EXOC6]] | -0.52 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[DHRS2]] | -0.51 | -0.35 / -0.51 | both halves | 1e-04 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[POGZ]] | -0.51 | -0.39 / -0.55 | both halves | 5e-05 |  |
| [[HES1]] | -0.51 | -0.44 / -0.48 | both halves | 3e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[MAP3K14]] | -0.50 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[DUSP2]] | -0.50 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[MGA]] | -0.50 | -0.47 / -0.55 | both halves | 2e-05 | same gene group |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers NADSYN1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TP53]] | C | TP53 activity strengthens NADSYN1's drug response | recorded loss-of-function mutation of TP53 in 31 lines vs 17 not recorded | the TP53-altered lines respond 0.73× as strongly (z diff +1.07); strongest at Doxorubicin (hydrochloride) 5 µM: 1.46x vs 2.87x (z diff +4.1) | 0.312 over the table, 0.012 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.567). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-4.6, 24.6); signed map (2.2, 1.6). **Vector** length 109, 27.1% of its response variance represented; |z| ≥ 3 in 1,008 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.5 | +12.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.4 | +9.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +6.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~90% of this change | +4.2 | +3.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | +3.7 | +6.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.5 | +6.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +5.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.4 | +3.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.1 | +2.0 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.0 | +2.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -9.9 | -11.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -8.1 | -6.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -7.6 | -10.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -6.4 | -8.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | -5.5 | -11.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.8 | -1.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.2 | -1.2 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -2.0 | -2.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | +0.7 |

## What is on record

|  |  |
|---|---|
| Name | NAD synthetase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.4 — chr11:71,453,109-71,524,107 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10631 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Ligases |
| Hallmark sets | ESTROGEN_RESPONSE_EARLY |
| Reactome | 3 pathways, smallest: Nicotinate metabolism; Metabolism of water-soluble vitamins and cofactors; Metabolism of vitamins and cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6IA69](https://www.uniprot.org/uniprotkb/Q6IA69) (Glutamine-dependent NAD(+) synthetase):

> Catalyzes the final step of the nicotinamide adenine dinucleotide (NAD) de novo synthesis pathway, the ATP-dependent amidation of deamido-NAD using L-glutamine as a nitrogen source.

**Summary**, from NCBI Gene [55191](https://www.ncbi.nlm.nih.gov/gene/55191):

> Nicotinamide adenine dinucleotide (NAD) is a coenzyme in metabolic redox reactions, a precursor for several cell signaling molecules, and a substrate for protein posttranslational modifications. NAD synthetase (EC 6.3.5.1) catalyzes the final step in the biosynthesis of NAD from nicotinic acid adenine dinucleotide (NaAD).[supplied by OMIM, Apr 2004]

**Accessions** — [HGNC:29832](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29832) · Entrez [55191](https://www.ncbi.nlm.nih.gov/gene/55191) · UniProt [Q6IA69](https://www.uniprot.org/uniprotkb/Q6IA69) · Ensembl [ENSG00000172890](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172890)

## Data

Gene col 10311: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10311); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10311, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10311]; `tensor/DDL_lfc|DDL_z.npy` [10311]; `embed/gene_vectors.npy` [10311]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10311 or target_col == 10311). Every well: [[NADSYN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NADSYN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
