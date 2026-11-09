---
symbol: "PIGX"
type: "gene"
col: 8826
ensembl_id: "ENSG00000163964"
name: "phosphatidylinositol glycan anchor biosynthesis class X"
location: "3q29"
module: 6
arm: "+"
pooled_cpm: 22.22
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 8
n_dd_up_clean: 2
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# PIGX

*phosphatidylinositol glycan anchor biosynthesis class X* — 3q29

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.51× (z +15.1, q 0e+00, up in 41 of 41 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.15× (z +13.1, q 1e-36, up in 43 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (PANC-1 4.64×, NCI-H1573 7.11×, HOP62 5.15×, HS-578T 5.15×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 6 lines (HS-578T 3.08×, SW480 2.13×, NCI-H2347 2.75×, HEC-1-A 2.62×, …); [[Dinaciclib (drug)]] 5 µM in 1 line (PANC-1 3.82×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[PH-797804 (drug)]] 5 µM: 0.413× (z -5.6, q 8e-06, down in 27 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BIVM]] (+0.61, fdr 2e-05), [[ACTL6A]] (+0.58, fdr 2e-05), [[PRPS2]] (+0.57, fdr 3e-05); moves opposite to [[PSMD3]] (-0.59, fdr 3e-05), [[ZNF761]] (-0.58, fdr 3e-05), [[EXOC8]] (-0.57, fdr 4e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[NRG2]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[ERK5-IN-2 (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 11 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8826.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (PANC-1 4.64×, NCI-H1573 7.11×, HOP62 5.15×, HS-578T 5.15×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 6 lines (HS-578T 3.08×, SW480 2.13×, NCI-H2347 2.75×, HEC-1-A 2.62×, …); [[Dinaciclib (drug)]] 5 µM in 1 line (PANC-1 3.82×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **3.51×** | +15.1 | 0e+00 | 41/41 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.15×** | +13.1 | 1e-36 | 43/47 (HS-578T, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **3.06×** | +13.0 | 4e-36 | 28/31 (PANC-1, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **2.46×** | +10.0 | 2e-21 | 32/36 (PANC-1, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.80×** | +6.8 | 9e-10 | 36/47 (HS-578T, HOP62, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.76×** | +6.5 | 6e-09 | 36/48 (HS-578T, SK-MEL-2, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.63×** | +5.7 | 1e-06 | 27/43 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.55×** | +5.3 | 1e-05 | 29/48 (A498, KATO III, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~98% of this change | **1.43×** | +4.3 | 0.001 | 25/48 (KATO III, A-172, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.34×** | +3.5 | 0.027 | 17/47 (Panc 03.27, NCI-H1573, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~58% of this change | **1.33×** | +3.5 | 0.028 | 21/45 (HOP62, Hs 766T, …) | inconsistent across doses | low cells (technical?) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.30×** | +3.2 | 0.066 | 12/48 (Panc 03.27, NCI-H2347, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | 1.20× | +3.1 | 0.100 | 11/48 (PANC-1, NCI-H1573, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8826.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **0.413×** | -5.6 | 8e-06 | 27/46 (SW480, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.615×** | -5.5 | 8e-06 | 28/48 (SHP-77, PANC-1, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.736×** | -5.2 | 3e-05 | 27/47 (NCI-H23, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.552×** | -3.7 | 0.025 | 17/48 (SW480, KATO III, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.742×** | -3.6 | 0.036 | 21/47 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.733×** | -3.5 | 0.038 | 19/47 (SW480, SW1417, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.749×** | -3.5 | 0.040 | 20/47 (A-427, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.590×** | -3.3 | 0.063 | 20/46 (NCI-H23, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.773× | -3.1 | 0.12 | 19/48 (SW48, PANC-1, …) | rises with dose |  |
| [[ERK5-IN-2 (drug)]] 5 µM |  | 0.613× | -3.1 | 0.12 | 8/48 (SW480, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.48 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8826. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 40.7 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.64× (z +14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | [[Bortezomib (drug)]] 0.05 µM 0.365× (z -8.7) ⚠ cell-cycle shift, explains ~32% of this change |
| [[A-427 (line)]] | wt | 29.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.106× (z -15.5) |
| [[SW480 (line)]] | alt | 32.8 | 2 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +10.4) | [[PH-797804 (drug)]] 5 µM 0.132× (z -10.2) |
| [[HS-578T (line)]] | alt | 21.9 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.15× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.08× (z +10.5) | — |
| [[SK-MEL-2 (line)]] | alt | 24.3 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.02× (z +9.5) | — |
| [[SNU-1 (line)]] | wt | 43.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.183× (z -10.1) |
| [[A498 (line)]] | wt | 23.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.17× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[A549 (line)]] | wt | 13.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.79× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[HEC-1-A (line)]] | alt | 23.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.62× (z +10.0) | — |
| [[HOP62 (line)]] | alt | 20.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.15× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[Hs 766T (line)]] | wt | 18.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.89× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[J82 (line)]] | alt | 32.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +8.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 55.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.51× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H1573 (line)]] | alt | 16.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.11× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H1792 (line)]] | alt | 11.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.96× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H23 (line)]] | alt | 19.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -16.1) |
| [[NCI-H2347 (line)]] | alt | 16.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +10.0) | — |
| [[NCI-H460 (line)]] | wt | 17.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.71× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SHP-77 (line)]] | alt | 10.1 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0587× (z -11.8) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SNU-423 (line)]] | alt | 17.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.40× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[A-172 (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8826), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BIVM]] | +0.61 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[ACTL6A]] | +0.58 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[PRPS2]] | +0.57 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[PCLAF]] | +0.56 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[RMI1]] | +0.56 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[DUT]] | +0.55 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[EZH2]] | +0.55 | +0.41 / +0.57 | both halves | 4e-05 |  |
| [[PTPN18]] | +0.55 | +0.57 / +0.41 | both halves | 4e-05 |  |
| [[GMPS]] | +0.55 | +0.44 / +0.45 | both halves | 3e-05 |  |
| [[RAD51AP1]] | +0.55 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[THSD4-AS1]] | +0.55 | +0.59 / +0.43 | both halves | 3e-05 |  |
| [[TYMS]] | +0.55 | +0.60 / +0.36 | both halves | 1e-04 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMD3]] | -0.59 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[ZNF761]] | -0.58 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[EXOC8]] | -0.57 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[KCTD21]] | -0.55 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[BRF2]] | -0.55 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[ZNF229]] | -0.54 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[PSMB1]] | -0.54 | -0.66 / -0.35 | both halves | 1e-04 |  |
| [[ZNF579]] | -0.54 | -0.46 / -0.39 | both halves | 6e-05 |  |
| [[CLDN15]] | -0.54 | -0.34 / -0.59 | both halves | 1e-04 |  |
| [[SCUBE2]] | -0.53 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[TRAPPC2B]] | -0.52 | -0.60 / -0.23 | both halves | 5e-04 |  |
| [[DCTN6]] | -0.52 | -0.48 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NRG2]] | B | NRG2 activity raises PIGX's level | lines that do not express NRG2 (15) vs lines expressing it (35) | 1.19× lower at baseline in the lines without NRG2 | 0.060 | ⚠ within organs, on part of the lines; also absent: SHOX2, NOVA2, PHF21B |
| [[TOP2A]] | B | TOP2A activity lowers PIGX's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises PIGX's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TP53]] | C | TP53 activity weakens PIGX's drug response | recorded loss-of-function mutation of TP53 in 31 lines vs 17 not recorded | the TP53-altered lines respond 1.24× as strongly (z diff -0.90); strongest at Topotecan (hydrochloride) 5 µM: 1.70x vs 1.10x (z diff -2.4) | 0.234 over the table, 0.008 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[ERK5-IN-2 (drug)]] 0.5 µM | C | PIGX's natural level lowers the cells' numbers under ERK5-IN-2 0.5 µM (makes them more sensitive) | PIGX's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.64 | 0.390 over the table, 0.040 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.487). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-41.9, -4.4); signed map (-32.4, -44.7). **Vector** length 61.3, 11.5% of its response variance represented; |z| ≥ 3 in 811 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +13.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +4.0 | +6.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +3.2 | +6.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | +1.8 | +15.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.7 | -2.6 |
|  | [[Bentamapimod (drug)]] 5 µM |  | +1.2 | +0.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.2 | +1.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.1 | +1.0 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +1.0 | +0.2 |
|  | [[Ralimetinib dimesylate (drug)]] 5 µM |  | +1.0 | +0.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -4.2 | -5.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | -4.0 | -5.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.9 | -0.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.5 | -3.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.0 | -3.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.8 | -3.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.7 | -3.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.6 | -5.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.3 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | phosphatidylinositol glycan anchor biosynthesis class X |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q29 — chr3:196,639,775-196,736,007 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20522, PIG-X |
| Gene groups (HGNC) | Phosphatidylinositol glycan anchor biosynthesis |
| Reactome | 2 pathways, smallest: Synthesis of glycosylphosphatidylinositol (GPI); Post-translational modification: synthesis of GPI-anchored proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TBF5](https://www.uniprot.org/uniprotkb/Q8TBF5) (GPI alpha-1,4-mannosyltransferase I, stabilizing subunit):

> Stabilizing subunit of the glycosylphosphatidylinositol-mannosyltransferase I complex which catalyzes the transfer of the first mannose, via an alpha-1,4 bond from a dolichol-phosphate-mannose (Dol-P-Man) to the glucosaminyl acyl phosphatidylinositol (GlcN-(acyl)PI) intermediate to generate alpha-D-Man-(1->4)-alpha-D-GlcN-(1->6)-(1-radyl,2-acyl-sn-glycero-3-phospho)-2-acyl-inositol and participates in the sixth step of the glycosylphosphatidylinositol-anchor biosynthesis. Probably acts by …

**Summary**, from NCBI Gene [54965](https://www.ncbi.nlm.nih.gov/gene/54965):

> This gene encodes a type I transmembrane protein in the endoplasmic reticulum (ER). The protein is an essential component of glycosylphosphatidylinositol-mannosyltransferase I, which transfers the first of the four mannoses in the GPI-anchor precursors during GPI-anchor biosynthesis. Studies in rat indicate that the protein is translated from a non-AUG translation initiation site. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Oct 2009]

**Accessions** — [HGNC:26046](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26046) · Entrez [54965](https://www.ncbi.nlm.nih.gov/gene/54965) · UniProt [Q8TBF5](https://www.uniprot.org/uniprotkb/Q8TBF5) · Ensembl [ENSG00000163964](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163964)

## Data

Gene col 8826: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8826); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8826, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8826]; `tensor/DDL_lfc|DDL_z.npy` [8826]; `embed/gene_vectors.npy` [8826]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8826 or target_col == 8826). Every well: [[PIGX — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PIGX.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
