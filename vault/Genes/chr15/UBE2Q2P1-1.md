---
symbol: "UBE2Q2P1-1"
type: "gene"
col: 16545
ensembl_id: "ENSG00000291027"
name: ""
location: ""
module: 203
arm: "+"
pooled_cpm: 3.19
n_lines_expressing: 48
n_dd_up: 2
n_dd_down: 13
n_dd_up_clean: 0
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/203"]
generated_by: "tahoemap"
---

# UBE2Q2P1-1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.03× (z +6.1, q 6e-07, up in 0 of 7 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.381× (z -12.2, q 2e-31, down in 27 of 33 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.540× (z -5.5, q 3e-06, down in 17 of 31 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (CFPAC-1 0.0552×, A549 0.121×, PANC-1 0.153×, A-172 0.112×, …; ⚠ cell-cycle shift, explains ~32% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (NCI-H460 0.0221×, A498 0.0502×; ⚠ cell-cycle shift, explains ~32% of this change); [[Panobinostat (drug)]] 0.5 µM in 2 lines (HS-578T 0.0394×, HepG2/C3A 0.0475×; ⚠ cell-cycle shift, explains ~31% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (PANC-1 0.146×, LOX-IMVI 0.0827×); [[Idoxuridine (drug)]] 0.05 µM in 1 line (HS-578T 0.0378×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBE2Q2P1]] (+0.72, fdr 7e-06, ⚠ same locus), [[ZNF600]] (+0.60, fdr 4e-05), [[ARL8A]] (+0.59, fdr 7e-06), [[PLEKHM2]] (+0.55, fdr 3e-05); moves opposite to [[ARL5B]] (-0.51, fdr 3e-05), [[PRELID2]] (-0.48, fdr 6e-05), [[ECT2]] (-0.47, fdr 5e-05).
> It is in [[Module 203]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[UBE2Q2P13]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16545.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.03×** | +6.1 | 6e-07 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **1.34×** | +3.7 | 0.053 | 6/43 (CFPAC-1, LoVo, …) | rises with dose | low cells (technical?) |
| [[Rapamycin (drug)]] 5 µM |  | 1.28× | +3.2 | 0.28 | 9/42 (PANC-1, LOX-IMVI, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 11 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 16545.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (CFPAC-1 0.0552×, A549 0.121×, PANC-1 0.153×, A-172 0.112×, …; ⚠ cell-cycle shift, explains ~32% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (NCI-H460 0.0221×, A498 0.0502×; ⚠ cell-cycle shift, explains ~32% of this change); [[Panobinostat (drug)]] 0.5 µM in 2 lines (HS-578T 0.0394×, HepG2/C3A 0.0475×; ⚠ cell-cycle shift, explains ~31% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (PANC-1 0.146×, LOX-IMVI 0.0827×); [[Idoxuridine (drug)]] 0.05 µM in 1 line (HS-578T 0.0378×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.381×** | -12.2 | 2e-31 | 27/33 (CFPAC-1, A549, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.397×** | -8.3 | 4e-14 | 32/44 (SNU-423, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.403×** | -8.1 | 9e-14 | 31/42 (HS-578T, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.403×** | -7.8 | 9e-13 | 26/38 (NCI-H460, A498, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.420×** | -7.8 | 1e-12 | 25/42 (A-172, A549, …) | top dose only | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.817×** | -6.3 | 3e-08 | 32/45 (HCT15, A-172, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.526×** | -5.7 | 8e-07 | 20/43 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.540×** | -5.5 | 3e-06 | 17/31 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.670×** | -3.6 | 0.022 | 9/41 (BT-474, PANC-1, …) | all doses, flat | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.672×** | -3.5 | 0.022 | 14/42 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~59% of this change | **0.665×** | -3.5 | 0.025 | 11/21 (NCI-H1792, hTERT-HPNE, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.687×** | -3.3 | 0.039 | 11/43 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.695×** | -3.1 | 0.082 | 4/43 (NCI-H460, BT-474, …) | top dose only | plate-row cell shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.44 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16545. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 3.74 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -11.0) ⚠ cell-cycle shift, explains ~32% of this change |
| [[HS-578T (line)]] | alt | 3.54 | 0 | 3 (2 ⚠) | — | [[Idoxuridine (drug)]] 0.05 µM 0.0378× (z -10.4) |
| [[LOX-IMVI (line)]] | wt | 4.72 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0827× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 2.45 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0221× (z -14.5) ⚠ cell-cycle shift, explains ~32% of this change |
| [[PANC-1 (line)]] | alt | 3.16 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -12.6) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.146× (z -9.1) |
| [[A498 (line)]] | wt | 2.41 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0502× (z -10.3) ⚠ cell-cycle shift, explains ~32% of this change |
| [[A549 (line)]] | wt | 7.57 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -12.6) ⚠ cell-cycle shift, explains ~32% of this change |
| [[CFPAC-1 (line)]] | alt | 5.01 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0552× (z -15.8) ⚠ cell-cycle shift, explains ~32% of this change |
| [[HepG2_C3A (line)]] | wt | 5.98 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0475× (z -9.2) ⚠ cell-cycle shift, explains ~31% of this change |
| [[MIA PaCa-2 (line)]] | alt | 3.82 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0495× (z -9.6) ⚠ unreliable plate only |
| [[NCI-H1792 (line)]] | alt | 7.45 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.131× (z -11.9) ⚠ cell-cycle shift, explains ~44% of this change |
| [[RPMI-7951 (line)]] | alt | 4.48 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0859× (z -9.8) ⚠ cell-cycle shift, explains ~32% of this change |
| [[A-427 (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.06 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.73 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.917 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.987 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.97 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.08 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.566 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.41 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.74 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.273 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.29 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.55 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16545), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2Q2P1]] | +0.72 | +0.72 / +0.71 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[ZNF600]] | +0.60 | +0.41 / +0.63 | both halves | 4e-05 |  |
| [[ARL8A]] | +0.59 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[PLEKHM2]] | +0.55 | +0.45 / +0.62 | both halves | 3e-05 |  |
| [[SREK1IP1]] | +0.54 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[JOSD2]] | +0.54 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[ADAP2]] | +0.54 | +0.32 / +0.59 | both halves | 1e-04 |  |
| [[SNX21]] | +0.54 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[GPR161]] | +0.53 | +0.40 / +0.57 | both halves | 4e-05 |  |
| [[ZNF611]] | +0.52 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[FBXL2]] | +0.52 | +0.48 / +0.66 | both halves | 2e-05 |  |
| [[SLC26A11]] | +0.50 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[RUFY2]] | +0.49 | +0.46 / +0.50 | both halves | 2e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARL5B]] | -0.51 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[PRELID2]] | -0.48 | -0.38 / -0.45 | both halves | 6e-05 |  |
| [[ECT2]] | -0.47 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[PTBP1]] | -0.45 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[BUB1]] | -0.44 | -0.36 / -0.48 | both halves | 1e-04 |  |
| [[BAHCC1]] | -0.44 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[ARHGEF39]] | -0.44 | -0.46 / -0.40 | both halves | 5e-05 |  |
| [[MYBL1]] | -0.44 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[CBX5]] | -0.44 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[MAD2L1]] | -0.44 | -0.32 / -0.49 | both halves | 2e-04 |  |
| [[SSR1]] | -0.44 | -0.39 / -0.41 | both halves | 5e-05 |  |
| [[FH]] | -0.43 | -0.37 / -0.46 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UBE2Q2P13]] | B | UBE2Q2P13 activity raises UBE2Q2P1-1's level | lines that do not express UBE2Q2P13 (23) vs lines expressing it (27) | 1.45× lower at baseline in the lines without UBE2Q2P13 | 0.068 | ⚠ within organs, on part of the lines; also absent: ZFP82, CACNA2D1, BASP1-AS1 |
| [[TBKBP1]] | B | TBKBP1 activity raises UBE2Q2P1-1's level | lines that do not express TBKBP1 (5) vs lines expressing it (45) | 2.35× lower at baseline in the lines without TBKBP1 | 0.089 | ⚠ within organs, on part of the lines; also absent: CSRP2, PHC1, DNAJC18; its own permutation p |
| [[ZNF600]] | B | ZNF600 activity lowers UBE2Q2P1-1's level | lines that do not express ZNF600 (9) vs lines expressing it (41) | 1.40× higher at baseline in the lines without ZNF600 | 0.089 | ⚠ within organs, on part of the lines; also absent: ZNF320, ZNF28, ZNF468 |
| [[RUSC2]] | C | RUSC2 activity raises UBE2Q2P1-1's level | lines that do not express RUSC2 (4) vs lines expressing it (46) | 1.83× lower at baseline in the lines without RUSC2 | 0.067 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: ATP8B3, SOAT1, SPAG17; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 203]]; 15 genes; every member is in the + arm (projection on the module's main direction 0.644). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-51.6, -3.4); signed map (-7.9, -14.0). **Vector** length 50.4, 6.69% of its response variance represented; |z| ≥ 3 in 910 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +1.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | +2.6 | +3.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.5 | +1.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.2 | +1.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.0 | +2.0 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.8 | +3.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | +1.2 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +1.3 | +2.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -2.7 | -12.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -2.5 | -7.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -1.5 | -8.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.4 | -5.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -2.4 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -1.1 | -2.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.0 | -2.6 |
|  | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | -0.9 | -1.2 |
|  | [[Gefitinib (drug)]] 5 µM |  | -0.9 | +0.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -0.9 | -1.9 |

## What is on record

> [!warning] No registry record
> UBE2Q2P1-1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 16545: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16545); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16545, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16545]; `tensor/DDL_lfc|DDL_z.npy` [16545]; `embed/gene_vectors.npy` [16545]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16545 or target_col == 16545). Every well: [[UBE2Q2P1-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBE2Q2P1-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
