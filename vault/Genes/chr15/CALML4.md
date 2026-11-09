---
symbol: "CALML4"
type: "gene"
col: 4941
ensembl_id: "ENSG00000129007"
name: "calmodulin like 4"
location: "15q23"
module: 44
arm: "+"
pooled_cpm: 14.39
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 2
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 18
direction_downstream: 0
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# CALML4

*calmodulin like 4* — 15q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.01× (z +13.7, q 6e-40, up in 25 of 34 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Selinexor (drug)]] 0.05 µM: 1.57× (z +8.9, q 9e-17, up in 23 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 0.528× (z -6.6, q 3e-08, down in 22 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (HT-29 0.273×, LS 180 0.357×, LoVo 0.454×; ⚠ cell-cycle shift, explains ~91% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (HT-29 0.217×, LS 180 0.307×, MIA PaCa-2 0.194×; ⚠ cell-cycle shift, explains ~41% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (HT-29 0.162×, LS 180 0.342×); [[Canagliflozin (drug)]] 0.05 µM in 1 line (COLO 205 0.146×); [[Roxadustat (drug)]] 0.05 µM in 1 line (BT-474 0.110×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CLN6]] (+0.69, fdr 7e-06, ⚠ same locus), [[ST6GALNAC1]] (+0.60, fdr 1e-05), [[GPA33]] (+0.59, fdr 1e-05), [[PPP1R1B]] (+0.58, fdr 1e-05); moves opposite to [[TMEM45A]] (-0.50, fdr 8e-05), [[WASHC3]] (-0.49, fdr 3e-05), [[GOLGA8N]] (-0.49, fdr 1e-04).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 18 arrows point to it, the strongest [[MUC13]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4941.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **2.01×** | +13.7 | 6e-40 | 25/34 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.92×** | +12.3 | 3e-32 | 13/22 (KATO III, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.66×** | +9.9 | 8e-21 | 26/47 (SW480, NCI-H460, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM |  | **1.57×** | +8.9 | 9e-17 | 23/48 (PANC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.62×** | +8.8 | 2e-16 | 16/27 (KATO III, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.47×** | +7.5 | 4e-12 | 22/47 (PANC-1, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.35×** | +5.9 | 3e-07 | 14/47 (A549, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.24×** | +5.6 | 2e-06 | 17/46 (H4, J82, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **1.63×** | +5.0 | 3e-05 | 8/44 (MIA PaCa-2, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.29×** | +4.9 | 5e-05 | 8/47 (HEC-1-A, PANC-1, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.56×** | +4.6 | 2e-04 | 6/44 (NCI-H460, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.25×** | +4.4 | 5e-04 | 10/44 (Hs 766T, SW48, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.17× | +4.1 | 0.002 | 7/48 (SHP-77, MIA PaCa-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.22×** | +4.0 | 0.003 | 13/47 (NCI-H1573, NCI-H1792, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.32×** | +3.9 | 0.003 | 1/48 (NCI-H460) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.46×** | +3.8 | 0.004 | 5/44 (NCI-H460, RPMI-7951, …) | all doses, flat | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.26×** | +3.2 | 0.041 | 2/46 (NCI-H460, NCI-H1792) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | 1.19× | +3.2 | 0.043 | 4/47 (RKO, SW480, …) | all doses, flat |  |
| [[EX229 (drug)]] 0.5 µM |  | **1.25×** | +3.1 | 0.043 | 2/47 (NCI-H460, NCI-H1792) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | 1.17× | +2.9 | 0.085 | 10/42 (NCI-H23, J82, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.16× | +2.8 | 0.099 | 2/47 (BT-474, HOP62) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4941.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (HT-29 0.273×, LS 180 0.357×, LoVo 0.454×; ⚠ cell-cycle shift, explains ~91% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (HT-29 0.217×, LS 180 0.307×, MIA PaCa-2 0.194×; ⚠ cell-cycle shift, explains ~41% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (HT-29 0.162×, LS 180 0.342×); [[Canagliflozin (drug)]] 0.05 µM in 1 line (COLO 205 0.146×); [[Roxadustat (drug)]] 0.05 µM in 1 line (BT-474 0.110×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.528×** | -6.6 | 3e-08 | 22/47 (LoVo, LS 180, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.555×** | -6.1 | 4e-07 | 18/43 (KATO III, LoVo, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Terfenadine (drug)]] 5 µM |  | 0.869× | -3.6 | 0.069 | 3/48 (RKO, A-427, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 0.852× | -3.2 | 0.20 | 15/43 (HT-29, LS 180, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.5 µM |  | 0.856× | -3.1 | 0.22 | 2/48 (SNU-1, SW48) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4941. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 78.5 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -19.8) |
| [[LS 180 (line)]] | wt | 43.5 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -11.1) |
| [[LoVo (line)]] | wt | 21.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.185× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[BT-474 (line)]] | alt | 9.16 | 0 | 1 | — | [[Roxadustat (drug)]] 0.05 µM 0.110× (z -8.6) |
| [[COLO 205 (line)]] | alt | 21.0 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.146× (z -9.6) |
| [[H4 (line)]] | wt | 8.55 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.78× (z +9.4) | — |
| [[J82 (line)]] | alt | 16.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +9.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 10.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.194× (z -8.8) ⚠ cell-cycle shift, explains ~41% of this change |
| [[NCI-H1573 (line)]] | alt | 10.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.47× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[NCI-H2030 (line)]] | alt | 8.81 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0812× (z -13.1) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 15.7 | 0 | 1 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.213× (z -9.6) ⚠ toxic |
| [[A-172 (line)]] | wt | 7.77 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.42 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.99 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.02 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.91 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.72 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.69 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.61 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.82 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.83 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.86 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.72 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.43 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 13.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4941), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLN6]] | +0.69 | +0.65 / +0.74 | both halves | 7e-06 | STRING 733; ⚠ same locus (0.9 kb, same strand: neighbours can correlate without regulation) |
| [[ST6GALNAC1]] | +0.60 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[GPA33]] | +0.59 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[PPP1R1B]] | +0.58 | +0.57 / +0.54 | both halves | 1e-05 | STRING 418 |
| [[CENPV]] | +0.57 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[CTSE]] | +0.56 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[UGT1A1]] | +0.55 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[FAM3D]] | +0.55 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[MUC5B]] | +0.55 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[SYK]] | +0.55 | +0.57 / +0.45 | both halves | 3e-05 | STRING 411 |
| [[ZNRF3]] | +0.54 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[DENND2D]] | +0.54 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[PRR15L]] | +0.53 | +0.56 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM45A]] | -0.50 | -0.57 / -0.37 | both halves | 8e-05 |  |
| [[WASHC3]] | -0.49 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[GOLGA8N]] | -0.49 | -0.52 / -0.32 | both halves | 1e-04 |  |
| [[SERINC1]] | -0.47 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[C2orf74-DT]] | -0.46 | -0.39 / -0.40 | both halves | 5e-05 |  |
| [[ZMAT5]] | -0.44 | -0.46 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 18, C 0. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MUC13]] | B | MUC13 activity raises CALML4's level | lines that do not express MUC13 (40) vs lines expressing it (10) | 2.28× lower at baseline in the lines without MUC13 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, NPSR1, CDH17 |
| [[LGALS4]] | B | LGALS4 activity raises CALML4's level | lines that do not express LGALS4 (39) vs lines expressing it (11) | 2.25× lower at baseline in the lines without LGALS4 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13; maybe low, not absent |
| [[CDH17]] | B | CDH17 activity raises CALML4's level | lines that do not express CDH17 (40) vs lines expressing it (10) | 2.21× lower at baseline in the lines without CDH17 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, MUC13, CLRN3 |
| [[REG4]] | B | REG4 activity raises CALML4's level | lines that do not express REG4 (43) vs lines expressing it (7) | 2.36× lower at baseline in the lines without REG4 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, NPSR1, ENSG00000230975 |
| [[NPSR1]] | B | NPSR1 activity raises CALML4's level | lines that do not express NPSR1 (42) vs lines expressing it (8) | 2.35× lower at baseline in the lines without NPSR1 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, MUC17, CDH17 |
| [[GCNT3]] | B | GCNT3 activity raises CALML4's level | lines that do not express GCNT3 (38) vs lines expressing it (12) | 1.86× lower at baseline in the lines without GCNT3 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, LYZ, MUC13 |
| [[NPSR1]] | B | NPSR1 activity weakens CALML4's drug response | lines that do not express NPSR1 (42) vs lines expressing it (6) | the lines without NPSR1 respond 1.64× as strongly (z diff -0.97); strongest at Homoharringtonine 5 µM: 1.41x vs 0.39x (z diff -9.1) | 0.026 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, MUC17, CDH17; target measured in part of the lines; both ways; artifact flags |
| [[REG4]] | B | REG4 activity weakens CALML4's drug response | lines that do not express REG4 (43) vs lines expressing it (5) | the lines without REG4 respond 1.57× as strongly (z diff -0.95); strongest at Homoharringtonine 5 µM: 1.38x vs 0.36x (z diff -9.6) | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, NPSR1, ENSG00000230975; target measured in part of the lines; both ways; artifact flags |
| [[MECOM]] | B | MECOM activity weakens CALML4's drug response | lines that do not express MECOM (18) vs lines expressing it (30) | the lines without MECOM respond 1.26× as strongly (z diff -0.50); strongest at Homoharringtonine 5 µM: 1.54x vs 1.03x (z diff -2.5) | 0.034 | ⚠ within organs, on part of the lines; also absent: STYK1, IKZF2, TSTD1; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[MYO7B]] | B | MYO7B activity raises CALML4's level | lines that do not express MYO7B (36) vs lines expressing it (14) | 1.67× lower at baseline in the lines without MYO7B | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CLRN3, LINC01559, PHGR1 |
| [[ARHGEF16]] | B | ARHGEF16 activity raises CALML4's level | lines that do not express ARHGEF16 (14) vs lines expressing it (36) | 1.61× lower at baseline in the lines without ARHGEF16 | 0.056 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A-DT, KRT18, NRARP |
| [[LINC01559]] | B | LINC01559 activity raises CALML4's level | lines that do not express LINC01559 (38) vs lines expressing it (12) | 1.96× lower at baseline in the lines without LINC01559 | 0.061 | ⚠ within organs, on part of the lines; also absent: CLRN3, NPSR1, CDH17 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.560). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.5, 50.7); signed map (64.6, 6.0). **Vector** length 78.1, 13.5% of its response variance represented; |z| ≥ 3 in 895 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +4.7 | +12.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | +4.4 | +13.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +4.3 | +8.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.9 | +2.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.6 | +9.9 |
|  | [[EX229 (drug)]] 5 µM |  | +2.4 | +3.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.2 | +4.6 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.2 | +2.2 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.7 | +3.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.7 | +7.5 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -2.7 | -6.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.5 | -6.1 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -2.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.7 | -0.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.5 | -2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.4 | -2.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.3 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | calmodulin like 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q23 — chr15:68,190,705-68,206,079 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC4809, NY-BR-20 |
| Gene groups (HGNC) | EF-hand domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96GE6](https://www.uniprot.org/uniprotkb/Q96GE6) (Calmodulin-like protein 4):

> As part of the intermicrovillar adhesion complex/IMAC plays a role in epithelial brush border differentiation, controlling microvilli organization and length. Acts as a light chain for MYO7B and is required for efficient targeting of the IMAC to the tips of border brush microvilli.

**Summary**, from NCBI Gene [91860](https://www.ncbi.nlm.nih.gov/gene/91860):

> Enables myosin head/neck binding activity. Involved in brush border assembly. Located in microvillus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:18445](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18445) · Entrez [91860](https://www.ncbi.nlm.nih.gov/gene/91860) · UniProt [Q96GE6](https://www.uniprot.org/uniprotkb/Q96GE6) · Ensembl [ENSG00000129007](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129007)

## Data

Gene col 4941: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4941); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4941, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4941]; `tensor/DDL_lfc|DDL_z.npy` [4941]; `embed/gene_vectors.npy` [4941]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4941 or target_col == 4941). Every well: [[CALML4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CALML4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
