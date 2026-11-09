---
symbol: "VPS26C"
type: "gene"
col: 8080
ensembl_id: "ENSG00000157538"
name: "VPS26 endosomal protein sorting factor C"
location: "21q22.13"
module: 105
arm: "+"
pooled_cpm: 56.16
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 4
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/105"]
generated_by: "tahoemap"
---

# VPS26C

*VPS26 endosomal protein sorting factor C* — 21q22.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.62× (z +10.4, q 2e-22, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.617× (z -10.4, q 1e-22, down in 33 of 48 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (SW480 0.347×, C-33 A 0.210×, C32 0.263×, A-172 0.344×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (A-427 0.155×, A-172 0.245×, SW1417 0.370×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (H4 0.244×, KATO III 0.331×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AVL9]] (+0.57, fdr 3e-05), [[DHRS13]] (+0.56, fdr 2e-05), [[KXD1]] (+0.53, fdr 3e-05); moves opposite to [[VCP]] (-0.58, fdr 1e-05), [[LINC02803]] (-0.49, fdr 4e-05), [[HSP90AA1]] (-0.48, fdr 2e-05).
> It is in [[Module 105]], a single-armed module (Late Phase of HIV Life Cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SLC17A7]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8080.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.62×** | +10.4 | 2e-22 | 38/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.59×** | +10.0 | 3e-21 | 33/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.55×** | +9.4 | 6e-19 | 36/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.52×** | +9.1 | 2e-17 | 36/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.06×** | +8.2 | 3e-14 | 34/49 (NCI-H23, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.23×** | +4.5 | 7e-04 | 20/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.39×** | +3.7 | 0.015 | 20/48 (LS 180, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.13× | +3.7 | 0.015 | 4/48 (NCI-H2030, A-172, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 1.12× | +3.6 | 0.020 | 8/48 (J82, LOX-IMVI, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 1.17× | +3.3 | 0.049 | 11/48 (PANC-1, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8080.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (SW480 0.347×, C-33 A 0.210×, C32 0.263×, A-172 0.344×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (A-427 0.155×, A-172 0.245×, SW1417 0.370×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (H4 0.244×, KATO III 0.331×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.617×** | -10.4 | 1e-22 | 33/48 (H4, KATO III, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.676×** | -8.1 | 1e-13 | 28/42 (SW480, C-33 A, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.673×** | -7.9 | 5e-13 | 28/45 (A-427, A-172, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.670×** | -4.5 | 9e-04 | 23/45 (Hs 766T, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.896× | -3.3 | 0.093 | 10/48 (H4, HS-578T, …) | top dose only |  |
| [[Carbamazepine (drug)]] 5 µM |  | 0.858× | -3.3 | 0.093 | 11/47 (C-33 A, A-172, …) | top dose only |  |
| [[Berbamine (drug)]] 0.05 µM |  | 0.862× | -3.2 | 0.11 | 16/48 (A498, A-172, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 0.904× | -3.1 | 0.14 | 8/48 (HS-578T, NCI-H460, …) | top dose only |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | 0.868× | -3.0 | 0.14 | 10/49 (NCI-H1573, C-33 A, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 5 µM |  | 0.905× | -3.0 | 0.14 | 10/48 (PANC-1, Panc 03.27, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8080. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 42.5 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +14.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 3.54× (z +13.2) | — |
| [[A-172 (line)]] | wt | 98.6 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.245× (z -13.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 63.5 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.71× (z +14.8) | — |
| [[C32 (line)]] | wt | 52.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.263× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[MIA PaCa-2 (line)]] | alt | 84.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.352× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[RKO (line)]] | wt | 69.8 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.74× (z +9.2) | — |
| [[A-427 (line)]] | wt | 53.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.155× (z -17.4) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 54.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.210× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[H4 (line)]] | wt | 68.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.244× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[Hs 766T (line)]] | wt | 51.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +11.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HS-578T (line)]] | alt | 71.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.450× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[J82 (line)]] | alt | 48.1 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.49× (z +9.7) | — |
| [[KATO III (line)]] | alt | 32.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.331× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[LOX-IMVI (line)]] | wt | 80.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.390× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[NCI-H23 (line)]] | alt | 50.8 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.80× (z +8.9) | — |
| [[SNU-423 (line)]] | alt | 54.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.379× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[SW1417 (line)]] | alt | 59.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.370× (z -10.6) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 60.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.347× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[A498 (line)]] | wt | 64.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 45.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 57.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 54.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 70.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 79.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 41.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 53.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 53.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 37.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 49.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 78.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 55.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 54.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 61.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 71.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 62.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 61.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 58.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 65.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 42.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8080), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AVL9]] | +0.57 | +0.67 / +0.45 | both halves | 3e-05 |  |
| [[DHRS13]] | +0.56 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[KXD1]] | +0.53 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[SEC31B]] | +0.51 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[ZBTB25]] | +0.51 | +0.43 / +0.57 | both halves | 4e-05 |  |
| [[SAP30-DT]] | +0.50 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[HINFP]] | +0.50 | +0.63 / +0.36 | both halves | 1e-04 |  |
| [[MTCH2]] | +0.49 | +0.47 / +0.42 | both halves | 4e-05 |  |
| [[BRI3]] | +0.49 | +0.58 / +0.36 | both halves | 9e-05 |  |
| [[ARSK]] | +0.49 | +0.46 / +0.45 | both halves | 3e-05 |  |
| [[LSM14B]] | +0.48 | +0.50 / +0.40 | both halves | 5e-05 |  |
| [[TOLLIP]] | +0.48 | +0.43 / +0.47 | both halves | 3e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VCP]] | -0.58 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[LINC02803]] | -0.49 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[HSP90AA1]] | -0.48 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[MSANTD1]] | -0.46 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[PSMD11]] | -0.46 | -0.56 / -0.35 | both halves | 1e-04 |  |
| [[RBPMS]] | -0.45 | -0.34 / -0.55 | both halves | 1e-04 |  |
| [[LINC02133]] | -0.45 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[CCT6A]] | -0.43 | -0.46 / -0.39 | both halves | 5e-05 |  |
| [[MPP4]] | -0.43 | -0.55 / -0.33 | both halves | 1e-04 |  |
| [[PSMD1]] | -0.43 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[ITPR2-AS1]] | -0.43 | -0.53 / -0.35 | both halves | 1e-04 |  |
| [[OIT3]] | -0.43 | -0.47 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC17A7]] | B | SLC17A7 activity raises VPS26C's level | lines that do not express SLC17A7 (9) vs lines expressing it (41) | 1.34× lower at baseline in the lines without SLC17A7 | 0.060 | ⚠ within organs, on part of the lines; also absent: GXYLT2, ITGA10, NT5M; maybe low, not absent |
| [[PIP4P2]] | C | PIP4P2 activity raises VPS26C's level | lines that do not express PIP4P2 (4) vs lines expressing it (46) | 1.46× lower at baseline in the lines without PIP4P2 | 0.075 | ⚠ few lines (4 vs 46); across organs; also absent: THEM4, MRPS30-DT; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 105]] — Late Phase of HIV Life Cycle; 44 genes; every member is in the + arm (projection on the module's main direction 0.397). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-28.8, -8.4); signed map (-39.1, 21.8). **Vector** length 91.3, 20.7% of its response variance represented; |z| ≥ 3 in 868 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +10.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.3 | +1.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +4.1 | +9.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +3.9 | +10.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +2.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.1 | +3.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.1 | +1.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +1.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.1 | -1.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | -2.4 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -3.6 | -4.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.4 | -2.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.7 | -0.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.3 | -1.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.1 | +0.5 |
|  | [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | -1.7 | -3.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.6 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | VPS26 endosomal protein sorting factor C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.13 — chr21:37,223,420-37,267,919 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DCRA; previously DSCR3 |
| Gene groups (HGNC) | Retriever complex |
| Matched by | ensembl_id |

**Function**, from UniProt [O14972](https://www.uniprot.org/uniprotkb/O14972) (Vacuolar protein sorting-associated protein 26C):

> Component of the commander complex that is essential for endosomal recycling of transmembrane cargos; the commander complex is composed of the CCC subcomplex and the retriever subcomplex. Component of the retriever complex, which is a heterotrimeric complex related to retromer cargo-selective complex (CSC) and essential for retromer-independent retrieval and recycling of numerous cargos such as integrin alpha-5/beta-1 (ITGA5:ITGB1). The recruitment of the retriever complex to the endosomal …

**Summary**, from NCBI Gene [10311](https://www.ncbi.nlm.nih.gov/gene/10311):

> The region of chromosome 21 between genes CBR and ERG (CBR-ERG region), which spans 2.5 Mb on 21q22.2, has been defined by analysis of patients with partial trisomy 21. It contributes significantly to the pathogenesis of many characteristics of Down syndrome, including morphological features, hypotonia, and cognitive disability. The DSCR3 (Down syndrome critical region gene 3) gene is found in this region and is predictated to contain eight exons. DSCR3 is expressed in most tissues examined. …

**Accessions** — [HGNC:3044](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3044) · Entrez [10311](https://www.ncbi.nlm.nih.gov/gene/10311) · UniProt [O14972](https://www.uniprot.org/uniprotkb/O14972) · Ensembl [ENSG00000157538](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157538)

## Data

Gene col 8080: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8080); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8080, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8080]; `tensor/DDL_lfc|DDL_z.npy` [8080]; `embed/gene_vectors.npy` [8080]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8080 or target_col == 8080). Every well: [[VPS26C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VPS26C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
