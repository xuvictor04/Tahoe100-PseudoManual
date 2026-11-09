---
symbol: "SYT5"
type: "gene"
col: 5011
ensembl_id: "ENSG00000129990"
name: "synaptotagmin 5"
location: "19q13.42"
module: 53
arm: "+"
pooled_cpm: 2.17
n_lines_expressing: 40
n_dd_up: 16
n_dd_down: 3
n_dd_up_clean: 10
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 3
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# SYT5

*synaptotagmin 5* — 19q13.42

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.07× (z +8.3, q 5e-14, up in 15 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.497× (z -5.7, q 7e-06, down in 19 of 33 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 0.05 µM in 1 line (NCI-H23 0.0520×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (NCI-H23 0.0728×); [[Homoharringtonine (drug)]] 5 µM in 1 line (HT-29 0.187×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CPNE9]] (+0.73, fdr 7e-06), [[MAPK8IP1]] (+0.66, fdr 1e-05), [[PTPRH]] (+0.65, fdr 1e-05, ⚠ read-through risk), [[LSMEM2]] (+0.63, fdr 1e-05); moves opposite to [[QRSL1]] (-0.55, fdr 2e-05), [[DHX35]] (-0.54, fdr 2e-05), [[ASH2L]] (-0.54, fdr 3e-05).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAGEA4-AS1]] → it (grade B ⚠); 3 go from it, the strongest it → [[PTPRH]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5011.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.07×** | +8.3 | 5e-14 | 15/23 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.34×** | +6.6 | 1e-08 | 1/2 (PANC-1) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.14×** | +5.7 | 2e-06 | 0/2 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.01×** | +5.7 | 2e-06 | 15/34 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.00×** | +5.6 | 2e-06 | 1/7 (SHP-77) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +5.6 | 2e-06 | 8/23 (LoVo, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.85×** | +5.0 | 5e-05 | 12/32 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.58×** | +3.4 | 0.044 | 1/13 (NCI-H1573) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.50×** | +3.3 | 0.064 | 4/21 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.75×** | +3.2 | 0.064 | 0/16 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | **1.49×** | +3.2 | 0.064 | 2/17 (PANC-1, LOX-IMVI) | inconsistent across doses | position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.10×** | +3.1 | 0.075 | 1/4 (HT-29) | top dose only | noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | **1.47×** | +3.1 | 0.075 | 4/34 (HT-29, HepG2/C3A, …) | top dose only | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.47×** | +3.1 | 0.076 | 10/32 (SHP-77, A-172, …) | top dose only | position effect removed |
| [[Fingolimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +3.0 | 0.093 | 1/31 (A-172) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5011.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 0.05 µM in 1 line (NCI-H23 0.0520×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (NCI-H23 0.0728×); [[Homoharringtonine (drug)]] 5 µM in 1 line (HT-29 0.187×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.497×** | -5.7 | 7e-06 | 19/33 (A-427, HT-29, …) | all doses, flat | cell-cycle shift (explains ~9% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.592×** | -4.3 | 0.005 | 11/34 (HT-29, PANC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.624×** | -3.8 | 0.023 | 8/28 (NCI-H23, SW480, …) | all doses, flat | cell-cycle shift (explains ~9% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.661× | -3.4 | 0.11 | 8/29 (NCI-H23, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Radotinib (drug)]] 5 µM |  | 0.757× | -3.2 | 0.14 | 11/33 (NCI-H460, SW480, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.679× | -3.2 | 0.15 | 12/34 (HT-29, KATO III, …) | all doses, flat | cell-cycle shift (explains ~21% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.665× | -3.1 | 0.17 | 7/34 (SK-MEL-2, C-33 A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5011. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 8.99 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 7.72 | 0 | 2 | — | [[Digitoxin (drug)]] 0.05 µM 0.0520× (z -11.2) |
| [[A-172 (line)]] | wt | 3.74 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.851 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.98 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.821 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.531 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.423 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.349 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.516 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 5.31 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.866 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.08 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.801 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.364 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.935 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.453 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.859 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.374 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.285 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.56 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.368 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.313 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.641 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5011), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPNE9]] | +0.73 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[MAPK8IP1]] | +0.66 | +0.70 / +0.53 | both halves | 1e-05 |  |
| [[PTPRH]] | +0.65 | +0.52 / +0.63 | both halves | 1e-05 | ⚠ **readthrough risk**: this gene lies 1.0 kb 3′ of PTPRH on the same strand (can correlate by spillover, not regulation) |
| [[LSMEM2]] | +0.63 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[RAP1GAP]] | +0.62 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[MYO7A]] | +0.61 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[ELAVL3]] | +0.60 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[HCN2]] | +0.60 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[PRX]] | +0.59 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[SMIM41]] | +0.59 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[LHX4]] | +0.59 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[MIR9-1HG]] | +0.59 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[LINC02901]] | +0.58 | +0.59 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[QRSL1]] | -0.55 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[DHX35]] | -0.54 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[ASH2L]] | -0.54 | -0.60 / -0.43 | both halves | 3e-05 |  |
| [[DTD2]] | -0.54 | -0.54 / -0.46 | both halves | 2e-05 |  |
| [[CSE1L]] | -0.53 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[NAE1]] | -0.52 | -0.50 / -0.49 | both halves | 2e-05 |  |
| [[TRMT61B]] | -0.51 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[TMEM209]] | -0.51 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[CHPT1]] | -0.50 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[TADA2A]] | -0.50 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[PAXBP1]] | -0.50 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[HACD3]] | -0.49 | -0.53 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAGEA4-AS1]] | B | MAGEA4-AS1 activity raises SYT5's level | lines that do not express MAGEA4-AS1 (41) vs lines expressing it (9) | 1.61× lower at baseline in the lines without MAGEA4-AS1 | 0.035 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: CGA, CALCA, GCG |
| [[SH2D4B]] | C | SH2D4B activity lowers SYT5's level | lines that do not express SH2D4B (3) vs lines expressing it (47) | 2.22× higher at baseline in the lines without SH2D4B | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ENSG00000249951, ARHGAP15, B4GALT1; maybe low, not absent; its own permutation p |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTPRH]] | B | SYT5 activity raises PTPRH's level | lines that do not express SYT5 (10) vs lines expressing it (40) | 3.40× lower at baseline in the lines without SYT5 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with EP300, RNF43, ACVR2A; also absent: B4GALNT1, LARP6; maybe low, not absent |
| [[TLCD2]] | B | SYT5 activity raises TLCD2's level | lines that do not express SYT5 (10) vs lines expressing it (40) | 1.46× lower at baseline in the lines without SYT5 | 0.086 | ⚠ within organs, on part of the lines; co-occurs with EP300, RNF43, ACVR2A; also absent: B4GALNT1, LARP6; maybe low, not absent |
| [[EGR2]] | B | SYT5 activity raises EGR2's level | lines that do not express SYT5 (10) vs lines expressing it (40) | 1.19× lower at baseline in the lines without SYT5 | 0.095 | ⚠ within organs, on part of the lines; co-occurs with EP300, RNF43, ACVR2A; also absent: B4GALNT1, LARP6; maybe low, not absent |

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.604). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (43.0, -17.0); signed map (-2.5, 24.0). **Vector** length 49.0, 7.36% of its response variance represented; |z| ≥ 3 in 900 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +3.7 | +8.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.9 | +5.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.6 | +6.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.3 | +5.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.2 | +5.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +3.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.7 | +0.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.4 | +2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.3 | +2.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +3.2 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.9 | -5.7 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.7 | -3.1 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.6 | -3.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.6 | -3.4 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.1 | -1.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.1 | -3.2 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.1 | -2.4 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.0 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | synaptotagmin 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.42 — chr19:55,171,196-55,180,289 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Synaptotagmins |
| Reactome | 2 pathways, smallest: Regulation of insulin secretion; Integration of energy metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [O00445](https://www.uniprot.org/uniprotkb/O00445) (Synaptotagmin-5):

> May be involved in Ca(2+)-dependent exocytosis of secretory vesicles through Ca(2+) and phospholipid binding to the C2 domain or may serve as Ca(2+) sensors in the process of vesicular trafficking and exocytosis. Regulates the Ca(2+)-dependent secretion of norepinephrine in PC12 cells. Required for export from the endocytic recycling compartment to the cell surface (By similarity).

**Summary**, from NCBI Gene [6861](https://www.ncbi.nlm.nih.gov/gene/6861):

> Synaptotagmins, such as SYT5, are a family of type III membrane proteins characterized by cytoplasmic repeats related to protein kinase C (see MIM 176960) regulatory (C2) domains, which are thought to bind calcium. Synaptotagmins may act both as negative regulators of vesicle fusion, allowing fusion in the presence of calcium, and as calcium receptors or sensor molecules (summary by Hudson and Birnbaum, 1995 [PubMed 7597049]).[supplied by OMIM, Feb 2011]

**Accessions** — [HGNC:11513](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11513) · Entrez [6861](https://www.ncbi.nlm.nih.gov/gene/6861) · UniProt [O00445](https://www.uniprot.org/uniprotkb/O00445) · Ensembl [ENSG00000129990](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129990)

## Data

Gene col 5011: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5011); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5011, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5011]; `tensor/DDL_lfc|DDL_z.npy` [5011]; `embed/gene_vectors.npy` [5011]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5011 or target_col == 5011). Every well: [[SYT5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SYT5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
