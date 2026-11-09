---
symbol: "ATG3"
type: "gene"
col: 6938
ensembl_id: "ENSG00000144848"
name: "autophagy related 3"
location: "3q13.2"
module: 17
arm: "+"
pooled_cpm: 61.34
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 3
n_dd_up_clean: 5
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# ATG3

*autophagy related 3* — 3q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.96× (z +23.9, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.926× (z -4.3, q 0.012, down in 2 of 49 measured lines) ⚠ position not correctable. The strongest without an alert is [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM: 0.772× (z -3.9, q 0.027, down in 25 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Trametinib (drug)]] 5 µM in 1 line (NCI-H596 0.438×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MIER1]] (+0.68, fdr 7e-06), [[PATL1]] (+0.59, fdr 1e-05), [[SNX2]] (+0.58, fdr 1e-05); moves opposite to [[CRK]] (-0.57, fdr 1e-05), [[METTL2B]] (-0.55, fdr 1e-05), [[DAP3]] (-0.54, fdr 1e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 14 with an alert ⚠; shown: the 15 strongest. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6938.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.96×** | +23.9 | 0e+00 | 48/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **3.01×** | +17.2 | 0e+00 | 47/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.37×** | +13.4 | 8e-39 | 44/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.10×** | +11.5 | 1e-28 | 43/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.07×** | +10.9 | 9e-26 | 44/47 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **3.81×** | +10.9 | 1e-25 | 44/49 (NCI-H1573, NCI-H23, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.86×** | +9.3 | 1e-18 | 41/48 (NCI-H460, NCI-H1573, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.80×** | +9.1 | 4e-18 | 43/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.91×** | +8.7 | 2e-16 | 38/48 (SW1417, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.75×** | +8.7 | 2e-16 | 41/48 (SW480, A-172, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.64×** | +7.7 | 7e-13 | 40/48 (SW480, HT-29, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.60×** | +7.3 | 1e-11 | 36/48 (A-172, HT-29, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.57×** | +7.1 | 7e-11 | 36/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~50% of this change | **1.47×** | +6.0 | 9e-08 | 36/48 (KATO III, PANC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.37×** | +4.9 | 4e-05 | 29/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6938.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Trametinib (drug)]] 5 µM in 1 line (NCI-H596 0.438×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.926× | -4.3 | 0.012 | 2/49 (SW 1088, SW 1271) | inconsistent across doses |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | **0.772×** | -3.9 | 0.027 | 25/49 (HT-29, LS 180, …) | top dose only | plate-row cell shift |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | **0.776×** | -3.8 | 0.027 | 22/48 (SW 1088, NCI-H1573, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.795×** | -3.4 | 0.081 | 14/47 (HepG2/C3A, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.810× | -3.3 | 0.10 | 17/48 (HT-29, LoVo, …) | inconsistent across doses |  |
| [[Tirabrutinib (drug)]] 0.5 µM |  | 0.811× | -3.3 | 0.10 | 13/48 (SW1417, LOX-IMVI, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.820× | -3.1 | 0.15 | 16/48 (SW 1271, LS 180, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.822× | -3.1 | 0.15 | 11/48 (hTERT-HPNE, NCI-H2347, …) | inconsistent across doses |  |
| [[Bestatin (hydrochloride) (drug)]] 0.5 µM |  | 0.824× | -3.0 | 0.15 | 14/48 (SNU-423, CFPAC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6938. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 36.3 | 13 (8 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.49× (z +26.7) | — |
| [[NCI-H1573 (line)]] | alt | 50.1 | 8 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.45× (z +23.8) | — |
| [[PANC-1 (line)]] | alt | 70.0 | 8 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.49× (z +21.2) | — |
| [[SW480 (line)]] | alt | 51.3 | 8 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +15.1) | — |
| [[COLO 205 (line)]] | alt | 55.8 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.93× (z +18.9) | — |
| [[SW1417 (line)]] | alt | 90.6 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +16.7) | — |
| [[J82 (line)]] | alt | 85.6 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +19.0) | — |
| [[KATO III (line)]] | alt | 60.5 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.46× (z +17.6) | — |
| [[LoVo (line)]] | wt | 64.1 | 4 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.76× (z +12.1) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.39× (z +11.6) | — |
| [[NCI-H23 (line)]] | alt | 64.7 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +15.6) | — |
| [[HOP62 (line)]] | alt | 35.8 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.19× (z +15.3) | — |
| [[LOX-IMVI (line)]] | wt | 68.7 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.34× (z +12.1) | — |
| [[LS 180 (line)]] | wt | 51.4 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.01× (z +12.8) | — |
| [[NCI-H1792 (line)]] | alt | 49.5 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +12.8) | — |
| [[SNU-423 (line)]] | alt | 58.5 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.08× (z +17.6) | — |
| [[SW 900 (line)]] | alt | 61.2 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +11.8) | — |
| [[A-172 (line)]] | wt | 47.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +18.2) | — |
| [[AsPC-1 (line)]] | alt | 44.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +14.9) | — |
| [[BT-474 (line)]] | alt | 42.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +10.0) | — |
| [[C32 (line)]] | wt | 49.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.55× (z +14.3) | — |
| [[HepG2_C3A (line)]] | wt | 34.6 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.75× (z +10.4) | — |
| [[HT-29 (line)]] | alt | 71.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +16.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 55.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.88× (z +14.8) | — |
| [[RPMI-7951 (line)]] | alt | 70.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.04× (z +14.8) | — |
| [[SK-MEL-2 (line)]] | alt | 57.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.91× (z +19.5) | — |
| [[A-427 (line)]] | wt | 103 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +9.0) | — |
| [[A498 (line)]] | wt | 99.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +12.0) | — |
| [[A549 (line)]] | wt | 41.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.90× (z +18.0) | — |
| [[CFPAC-1 (line)]] | alt | 59.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +13.3) | — |
| [[H4 (line)]] | wt | 46.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.26× (z +12.0) | — |
| [[HEC-1-A (line)]] | alt | 60.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +14.2) | — |
| [[Hs 766T (line)]] | wt | 45.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +15.9) | — |
| [[HS-578T (line)]] | alt | 94.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +10.9) | — |
| [[hTERT-HPNE (line)]] | wt | 46.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.16× (z +12.8) | — |
| [[NCI-H2347 (line)]] | alt | 106 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +13.1) | — |
| [[NCI-H596 (line)]] | alt | 61.5 | 0 | 1 (1 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.438× (z -9.1) ⚠ cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 61.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +10.5) | — |
| [[RKO (line)]] | wt | 44.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +14.6) | — |
| [[SHP-77 (line)]] | alt | 64.6 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.86× (z +8.5) | — |
| [[AN3 CA (line)]] | alt | 93.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 42.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 63.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 53.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 75.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 59.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 67.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 46.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6938), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIER1]] | +0.68 | +0.73 / +0.63 | both halves | 7e-06 |  |
| [[PATL1]] | +0.59 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[SNX2]] | +0.58 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[METTL14]] | +0.57 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[RCHY1]] | +0.55 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[MRPL22]] | +0.54 | +0.42 / +0.59 | both halves | 4e-05 |  |
| [[FIP1L1]] | +0.54 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[TPR]] | +0.54 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[NECAP1]] | +0.53 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[MLLT10]] | +0.53 | +0.35 / +0.59 | both halves | 1e-04 |  |
| [[MAP3K2]] | +0.53 | +0.37 / +0.54 | both halves | 8e-05 |  |
| [[EHMT2]] | +0.52 | +0.48 / +0.53 | both halves | 2e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRK]] | -0.57 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[METTL2B]] | -0.55 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[DAP3]] | -0.54 | -0.65 / -0.50 | both halves | 1e-05 |  |
| [[NIPAL1]] | -0.53 | -0.38 / -0.55 | both halves | 6e-05 |  |
| [[IDI2-AS1]] | -0.53 | -0.37 / -0.55 | both halves | 8e-05 |  |
| [[CPNE2]] | -0.52 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[ZNF562]] | -0.51 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[RRP7BP-1]] | -0.51 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[LINC01588]] | -0.51 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[KCNJ14]] | -0.51 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[CDKL1]] | -0.50 | -0.34 / -0.59 | both halves | 1e-04 |  |
| [[SLC9A1]] | -0.50 | -0.45 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.475). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (16.7, -8.7); signed map (-22.9, -9.9). **Vector** length 79.5, 21.8% of its response variance represented; |z| ≥ 3 in 966 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +3.6 | +10.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~50% of this change | +3.3 | +6.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.2 | +0.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +2.9 | +3.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.8 | +23.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.6 | -0.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.6 | -0.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.4 | +1.0 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.3 | +0.5 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -5.7 | -0.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -5.7 | +1.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.4 | -3.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.1 | +2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.3 | +1.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.4 | +1.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.9 | -2.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.9 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | autophagy related 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q13.2 — chr3:112,532,510-112,562,046 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PC3-96, FLJ22125, MGC15201, DKFZp564M1178; previously APG3L |
| Gene groups (HGNC) | Autophagy related; Autophagy related E2 enzymes |
| Reactome | 2 pathways, smallest: Macroautophagy; Autophagy |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NT62](https://www.uniprot.org/uniprotkb/Q9NT62) (Ubiquitin-like-conjugating enzyme ATG3):

> E2 conjugating enzyme that catalyzes the covalent conjugation of the C-terminal Gly of ATG8-like proteins (GABARAP, GABARAPL1, GABARAPL2 or MAP1LC3A) to the amino group of phosphatidylethanolamine (PE)-containing lipids in the membrane resulting in membrane-bound ATG8-like proteins which is one of the key steps in the development of autophagic isolation membranes during autophagosome formation. Cycles back and forth between binding to ATG7 for loading with the ATG8-like proteins and binding to …

**Summary**, from NCBI Gene [64422](https://www.ncbi.nlm.nih.gov/gene/64422):

> This gene encodes a ubiquitin-like-conjugating enzyme and is a component of ubiquitination-like systems involved in autophagy, the process of degradation, turnover and recycling of cytoplasmic constituents in eukaryotic cells. This protein is known to play a role in regulation of autophagy during cell death. A pseudogene of this gene is located on chromosome 20. Alternative splicing results in multiple transcript variants encoding different isoforms. [provided by RefSeq, Jul 2013]

**Accessions** — [HGNC:20962](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20962) · Entrez [64422](https://www.ncbi.nlm.nih.gov/gene/64422) · UniProt [Q9NT62](https://www.uniprot.org/uniprotkb/Q9NT62) · Ensembl [ENSG00000144848](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144848)

## Data

Gene col 6938: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6938); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6938, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6938]; `tensor/DDL_lfc|DDL_z.npy` [6938]; `embed/gene_vectors.npy` [6938]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6938 or target_col == 6938). Every well: [[ATG3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATG3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
