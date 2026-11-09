---
symbol: "TASOR"
type: "gene"
col: 8819
ensembl_id: "ENSG00000163946"
name: "transcription activation suppressor"
location: "3p14.3"
module: 88
arm: "+"
pooled_cpm: 80.83
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 11
n_dd_up_clean: 2
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 5
direction_downstream: 1
tags: ["gene", "module/088"]
generated_by: "tahoemap"
---

# TASOR

*transcription activation suppressor* — 3p14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.44× (z +6.1, q 5e-07, up in 33 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (C32 3.37×, NCI-H23 2.03×, NCI-H2347 2.16×, RPMI-7951 2.28×, …); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (C32 4.08×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 2.17×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.358× (z -12.1, q 8e-31, down in 47 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.459× (z -9.2, q 1e-17, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CYREN]] (+0.80, fdr 7e-06), [[ZC3H4]] (+0.80, fdr 7e-06), [[ZFP91]] (+0.75, fdr 7e-06); moves opposite to [[CBFA2T2]] (-0.78, fdr 7e-06), [[SDHAP2]] (-0.73, fdr 7e-06), [[KCTD7]] (-0.73, fdr 7e-06).
> It sits in the **+** arm of [[Module 088]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[FJX1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[SIRT5]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8819.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (C32 3.37×, NCI-H23 2.03×, NCI-H2347 2.16×, RPMI-7951 2.28×, …); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (C32 4.08×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 2.17×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.44×** | +6.1 | 5e-07 | 33/48 (C32, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.58×** | +5.4 | 2e-05 | 38/48 (C32, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | 1.31× | +3.2 | 0.27 | 26/48 (LoVo, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8819.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.358×** | -12.1 | 8e-31 | 47/48 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.459×** | -9.2 | 1e-17 | 44/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.479×** | -8.7 | 9e-16 | 45/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.491×** | -8.4 | 8e-15 | 46/48 (HEC-1-A, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.506×** | -8.0 | 1e-13 | 44/48 (HEC-1-A, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.530×** | -7.5 | 7e-12 | 45/48 (HEC-1-A, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.531×** | -7.5 | 7e-12 | 40/48 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.573×** | -6.3 | 2e-08 | 36/47 (KATO III, PANC-1, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.675×** | -4.6 | 2e-04 | 29/48 (A-427, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.679×** | -4.1 | 0.003 | 29/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.732×** | -3.7 | 0.013 | 25/48 (A-427, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | 0.759× | -3.1 | 0.10 | 21/48 (SNU-1, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | 0.611× | -3.0 | 0.11 | 19/38 (HEC-1-A, SW480, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8819. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 151 | 0 | 7 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.342× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.345× (z -11.8) |
| [[NCI-H23 (line)]] | alt | 131 | 1 | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +9.5) | [[Digitoxin (drug)]] 5 µM 0.177× (z -16.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.239× (z -13.8) |
| [[SNU-1 (line)]] | wt | 84.8 | 0 | 6 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.144× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.211× (z -10.5) |
| [[PANC-1 (line)]] | alt | 109 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.156× (z -19.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.194× (z -17.5) |
| [[SK-MEL-2 (line)]] | alt | 147 | 1 | 4 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +8.5) | [[Panobinostat (drug)]] 5 µM 0.285× (z -11.1) |
| [[HEC-1-A (line)]] | alt | 176 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.337× (z -11.6) |
| [[NCI-H1573 (line)]] | alt | 66.7 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.346× (z -9.8) |
| [[NCI-H460 (line)]] | wt | 77.5 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.206× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.363× (z -9.6) |
| [[SW480 (line)]] | alt | 89.9 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.261× (z -13.7) |
| [[BT-474 (line)]] | alt | 55.8 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.210× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.282× (z -10.0) |
| [[HCT15 (line)]] | alt | 104 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.252× (z -10.2) |
| [[J82 (line)]] | alt | 86.7 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.203× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.274× (z -10.2) |
| [[KATO III (line)]] | alt | 73.3 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.260× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.337× (z -9.6) |
| [[C32 (line)]] | wt | 41.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +11.3) | — |
| [[H4 (line)]] | wt | 81.0 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.243× (z -10.5) |
| [[HT-29 (line)]] | alt | 46.4 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.255× (z -10.9) |
| [[LoVo (line)]] | wt | 57.3 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.382× (z -8.9) |
| [[LOX-IMVI (line)]] | wt | 113 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.274× (z -10.0) |
| [[NCI-H2347 (line)]] | alt | 60.1 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.16× (z +9.0) | — |
| [[RPMI-7951 (line)]] | alt | 105 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +8.8) | [[Digitoxin (drug)]] 5 µM 0.276× (z -9.6) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 50.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.150× (z -13.5) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 61.1 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.326× (z -9.1) |
| [[Hs 766T (line)]] | wt | 51.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.227× (z -10.3) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 53.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +8.5) | — |
| [[LS 180 (line)]] | wt | 51.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.317× (z -8.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 93.1 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.304× (z -9.5) |
| [[NCI-H1792 (line)]] | alt | 67.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.299× (z -9.9) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 75.0 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.101× (z -9.4) |
| [[Panc 03.27 (line)]] | alt | 62.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.225× (z -10.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 119 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 61.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 67.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 82.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 87.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 72.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 41.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 73.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 70.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 68.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 62.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 63.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 91.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 96.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 98.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 65.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 87.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 56.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 48.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8819), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYREN]] | +0.80 | +0.84 / +0.63 | both halves | 7e-06 |  |
| [[ZC3H4]] | +0.80 | +0.84 / +0.63 | both halves | 7e-06 |  |
| [[ZFP91]] | +0.75 | +0.75 / +0.65 | both halves | 7e-06 |  |
| [[CLHC1]] | +0.75 | +0.80 / +0.49 | both halves | 1e-05 |  |
| [[CTBP1-DT]] | +0.75 | +0.81 / +0.48 | both halves | 2e-05 |  |
| [[ST7L]] | +0.75 | +0.74 / +0.63 | both halves | 7e-06 |  |
| [[RIF1]] | +0.73 | +0.70 / +0.74 | both halves | 7e-06 |  |
| [[DNAJC11]] | +0.73 | +0.72 / +0.65 | both halves | 7e-06 |  |
| [[LEKR1]] | +0.72 | +0.75 / +0.48 | both halves | 2e-05 |  |
| [[ZNF747]] | +0.72 | +0.74 / +0.52 | both halves | 1e-05 |  |
| [[USP7]] | +0.72 | +0.53 / +0.68 | both halves | 1e-05 |  |
| [[ZXDB]] | +0.72 | +0.71 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CBFA2T2]] | -0.78 | -0.85 / -0.59 | both halves | 7e-06 |  |
| [[SDHAP2]] | -0.73 | -0.76 / -0.62 | both halves | 7e-06 |  |
| [[KCTD7]] | -0.73 | -0.76 / -0.68 | both halves | 7e-06 |  |
| [[SDHAP1]] | -0.71 | -0.73 / -0.58 | both halves | 7e-06 |  |
| [[GUK1]] | -0.71 | -0.71 / -0.57 | both halves | 9e-06 |  |
| [[STK32C]] | -0.71 | -0.63 / -0.63 | both halves | 7e-06 |  |
| [[HEBP1]] | -0.70 | -0.65 / -0.53 | both halves | 1e-05 |  |
| [[SLC9A6]] | -0.70 | -0.66 / -0.52 | both halves | 1e-05 |  |
| [[NENF]] | -0.70 | -0.72 / -0.64 | both halves | 7e-06 |  |
| [[GMCL1]] | -0.70 | -0.71 / -0.51 | both halves | 1e-05 |  |
| [[TRIM62]] | -0.69 | -0.61 / -0.59 | both halves | 7e-06 |  |
| [[MPG]] | -0.69 | -0.69 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FJX1]] | B | FJX1 activity raises TASOR's level | lines that do not express FJX1 (11) vs lines expressing it (39) | 1.49× lower at baseline in the lines without FJX1 | 0.060 | ⚠ within organs, on part of the lines; also absent: DYNC2H1, GIHCG, HDGFL3 |
| [[HDAC6]] | B | HDAC6 activity raises TASOR's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ANKS1B]] | B | ANKS1B activity raises TASOR's level | lines that do not express ANKS1B (18) vs lines expressing it (32) | 1.37× lower at baseline in the lines without ANKS1B | 0.089 | ⚠ within organs, on part of the lines; also absent: LHX2, CECR2, HS6ST3 |
| [[ANKRD18B]] | B | ANKRD18B activity raises TASOR's level | lines that do not express ANKRD18B (23) vs lines expressing it (27) | 1.21× lower at baseline in the lines without ANKRD18B | 0.095 | ⚠ within organs, on part of the lines; also absent: ZNF229, SUSD5, HECW2 |
| [[MCTS1]] | C | MCTS1's natural level strengthens TASOR's drug response | MCTS1's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.64, reverse +0.11; direction not clear | 0.066 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SIRT5]] | C | TASOR's natural level strengthens SIRT5's drug response | TASOR's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.65, reverse +0.52; direction not clear | 0.047 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 088]]; 51 genes; this gene is in the **+** arm (projection on the module's main direction 0.804). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.46).
- **Nodal map** (x, y) = (-4.5, 2.2); signed map (16.6, -26.9). **Vector** length 133, 47.4% of its response variance represented; |z| ≥ 3 in 889 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +10.9 | +6.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +10.0 | +5.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +9.3 | +1.9 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +7.5 | +2.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.9 | +1.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.3 | +2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.0 | +2.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.4 | +2.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.4 | +3.2 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +3.0 | +2.7 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -7.0 | -8.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | -6.5 | -8.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -6.4 | -7.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.1 | -12.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.8 | -1.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.8 | -1.7 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -3.1 | -2.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.7 | -2.1 |
|  | [[Fumaric acid (drug)]] 5 µM |  | -2.5 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | transcription activation suppressor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p14.3 — chr3:56,620,132-56,683,265 (-) |
| Ensembl biotype | protein_coding |
| Also known as | se89-1, RAP140, KIAA1105, TASOR1; previously C3orf63, FAM208A |
| Gene groups (HGNC) | HUSH complex |
| Reactome | 3 pathways, smallest: Regulation of endogenous retroelements by the Human Silencing Hub (HUSH) complex; Regulation of endogenous retroelements; Epigenetic regulation of gene expression |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UK61](https://www.uniprot.org/uniprotkb/Q9UK61) (Protein TASOR):

> Core component of the HUSH complex, a multiprotein complex that specifically mediates epigenetic repression of mobile genetic elements, such as retroviruses and transposable elements. The HUSH complex represses LINE-1 (L1) retrotransposons that are still capable of transposition. Silencing events often occur within introns of transcriptionally active genes, and lead to the down-regulation of host gene expression. The HUSH complex also represses exogenous retroviruses and synthetic transgenes. …

**Summary**, from NCBI Gene [23272](https://www.ncbi.nlm.nih.gov/gene/23272):

> Enables chromatin binding activity and protein-macromolecule adaptor activity. Involved in protein localization to heterochromatin and transposable element silencing by heterochromatin formation. Located in heterochromatin and nucleoplasm. Part of HUSH complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30314](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30314) · Entrez [23272](https://www.ncbi.nlm.nih.gov/gene/23272) · UniProt [Q9UK61](https://www.uniprot.org/uniprotkb/Q9UK61) · Ensembl [ENSG00000163946](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163946)

## Data

Gene col 8819: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8819); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8819, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8819]; `tensor/DDL_lfc|DDL_z.npy` [8819]; `embed/gene_vectors.npy` [8819]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8819 or target_col == 8819). Every well: [[TASOR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TASOR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
