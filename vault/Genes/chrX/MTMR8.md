---
symbol: "MTMR8"
type: "gene"
col: 2207
ensembl_id: "ENSG00000102043"
name: "myotubularin related protein 8"
location: "Xq11.2"
module: 146
arm: "+"
pooled_cpm: 5.3
n_lines_expressing: 30
n_dd_up: 19
n_dd_down: 9
n_dd_up_clean: 13
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/146"]
generated_by: "tahoemap"
---

# MTMR8

*myotubularin related protein 8* — Xq11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.05 µM: 2.23× (z +9.5, q 1e-18, up in 19 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (7 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.518× (z -7.9, q 2e-12, down in 15 of 28 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.761× (z -4.6, q 6e-04, down in 10 of 26 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Epirubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A-427 0.0993×, HEC-1-A 0.271×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (SW48 0.0824×, NCI-H1573 0.167×; ⚠ cell-cycle shift, explains ~59% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H460 0.126×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change); [[Pravastatin (sodium) (drug)]] 0.05 µM in 1 line (SNU-1 0.0552×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SOAT1]] (+0.62, fdr 1e-05), [[SYTL4]] (+0.61, fdr 1e-05), [[CHST10]] (+0.57, fdr 1e-05); moves opposite to [[LINC00310]] (-0.51, fdr 6e-05), [[LINC01135]] (-0.50, fdr 1e-04), [[UBE3B]] (-0.50, fdr 2e-04).
> It sits in the **+** arm of [[Module 146]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAP2K6]] → it (grade C ⚠); 1 goes from it, the strongest it → [[MAP2K6]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2207.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.05 µM |  | **2.23×** | +9.5 | 1e-18 | 19/28 (PANC-1, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.91×** | +7.8 | 1e-12 | 17/27 (PANC-1, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.76×** | +6.9 | 1e-09 | 15/28 (NCI-H2347, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.66×** | +6.1 | 1e-07 | 13/28 (PANC-1, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.40×** | +5.8 | 6e-07 | 16/28 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.58×** | +5.5 | 3e-06 | 12/27 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.49×** | +4.8 | 1e-04 | 10/28 (Panc 03.27, NCI-H2347, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.12×** | +4.7 | 1e-04 | 8/28 (A-427, NCI-H2347, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.47×** | +4.7 | 2e-04 | 12/28 (NCI-H2347, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **1.46×** | +4.4 | 6e-04 | 6/24 (COLO 205, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.44×** | +4.4 | 6e-04 | 5/18 (HOP62, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +4.2 | 1e-03 | 6/24 (HT-29, J82, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.44×** | +4.2 | 1e-03 | 3/6 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.40×** | +4.0 | 0.002 | 5/28 (SW480, LS 180, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.23×** | +3.5 | 0.017 | 7/28 (SNU-1, NCI-H460, …) | rises with dose | low cells (technical?) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.28×** | +3.0 | 0.077 | 5/27 (SW480, CHP-212, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.28×** | +3.0 | 0.086 | 3/28 (LS 180, CFPAC-1, …) | rises with dose |  |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | **1.28×** | +2.9 | 0.098 | 2/28 (COLO 205, SW 1271) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 7 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2207.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Epirubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A-427 0.0993×, HEC-1-A 0.271×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (SW48 0.0824×, NCI-H1573 0.167×; ⚠ cell-cycle shift, explains ~59% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H460 0.126×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change); [[Pravastatin (sodium) (drug)]] 0.05 µM in 1 line (SNU-1 0.0552×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.518×** | -7.9 | 2e-12 | 15/28 (LS 180, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~95% of this change | **0.675×** | -6.6 | 1e-08 | 15/28 (A549, PANC-1, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.616×** | -5.8 | 1e-06 | 14/26 (NCI-H460, LS 180, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.761×** | -4.6 | 6e-04 | 10/26 (NCI-H460, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.718×** | -4.0 | 0.009 | 12/27 (SW48, NCI-H1573, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.718×** | -3.9 | 0.010 | 10/28 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.732×** | -3.7 | 0.017 | 12/27 (HEC-1-A, C-33 A, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.752×** | -3.4 | 0.048 | 7/28 (PANC-1, A-427, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.758×** | -3.3 | 0.060 | 10/28 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.55 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2207. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 28.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.242× (z -10.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 18.8 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0993× (z -15.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 3.25 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -8.6) ⚠ cell-cycle shift, explains ~95% of this change |
| [[LS 180 (line)]] | wt | 14.1 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.195× (z -8.9) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H1573 (line)]] | alt | 8.41 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.167× (z -8.5) ⚠ cell-cycle shift, explains ~59% of this change |
| [[NCI-H460 (line)]] | wt | 5.49 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.126× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[SNU-1 (line)]] | wt | 13.7 | 0 | 1 | — | [[Pravastatin (sodium) (drug)]] 0.05 µM 0.0552× (z -9.5) |
| [[SW48 (line)]] | wt | 12.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0824× (z -9.8) ⚠ cell-cycle shift, explains ~59% of this change |
| [[A-172 (line)]] | wt | 0.879 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.550 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.716 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.771 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.643 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.74 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.10 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 9.04 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.780 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.737 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.949 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.919 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.736 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.824 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.914 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.827 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.655 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.568 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.56 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.677 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 7.08 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.858 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.78 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2207), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SOAT1]] | +0.62 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[SYTL4]] | +0.61 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[CHST10]] | +0.57 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[SMPDL3B]] | +0.57 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[SLC27A2]] | +0.56 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[KLHL2]] | +0.56 | +0.41 / +0.60 | both halves | 4e-05 |  |
| [[GNPTAB]] | +0.56 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[SCN8A]] | +0.56 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[SLC5A4-AS1]] | +0.56 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[RAVER2]] | +0.53 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[NXPE3]] | +0.53 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[RABGGTB]] | +0.53 | +0.27 / +0.67 | both halves | 3e-04 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00310]] | -0.51 | -0.41 / -0.39 | both halves | 6e-05 |  |
| [[LINC01135]] | -0.50 | -0.34 / -0.46 | both halves | 1e-04 |  |
| [[UBE3B]] | -0.50 | -0.32 / -0.60 | both halves | 2e-04 |  |
| [[LINC01500]] | -0.50 | -0.33 / -0.36 | both halves | 1e-04 |  |
| [[HMGCL]] | -0.49 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[MTR]] | -0.49 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[FANK1]] | -0.48 | -0.22 / -0.58 | both halves | 6e-04 |  |
| [[NMNAT1]] | -0.48 | -0.37 / -0.45 | both halves | 8e-05 |  |
| [[ZKSCAN1]] | -0.48 | -0.35 / -0.35 | both halves | 1e-04 |  |
| [[BOLA1]] | -0.48 | -0.22 / -0.46 | both halves | 6e-04 |  |
| [[MCPH1-AS1]] | -0.47 | -0.33 / -0.37 | both halves | 1e-04 |  |
| [[SERPINB6]] | -0.47 | -0.41 / -0.49 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K6]] | C | MAP2K6 activity raises MTMR8's level | lines that do not express MAP2K6 (21) vs lines expressing it (29) | 2.69× lower at baseline in the lines without MAP2K6 | 0.012 | ⚠ within organs, on part of the lines; also absent: AGMO, MTMR8, ENSG00000286133; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K6]] | C | MTMR8 activity raises MAP2K6's level | lines that do not express MTMR8 (20) vs lines expressing it (30) | 2.82× lower at baseline in the lines without MTMR8 | 0.005 | ⚠ within organs, on part of the lines; also absent: MAP2K6, CXADR, BARX1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 146]]; 31 genes; this gene is in the **+** arm (projection on the module's main direction 0.410). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-2.3, 37.1); signed map (-2.3, 16.1). **Vector** length 37.5, 5.21% of its response variance represented; |z| ≥ 3 in 657 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.0 | +4.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +5.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.7 | +5.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.6 | +4.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +2.2 | +4.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.2 | +3.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.2 | +2.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.1 | -0.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.1 | +4.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~95% of this change | -2.3 | -6.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | -1.7 | -4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.4 | -3.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -1.3 | -4.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -1.1 | +4.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.9 | -0.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -0.8 | +1.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.5 | -0.4 |
|  | [[Lonafarnib (drug)]] 0.5 µM |  | -0.5 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | myotubularin related protein 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq11.2 — chrX:64,268,081-64,395,452 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20126 |
| Gene groups (HGNC) | Myotubularins; Phosphoinositide phosphatases |
| Reactome | 4 pathways, smallest: Synthesis of PIPs at the plasma membrane; PI Metabolism; Phospholipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96EF0](https://www.uniprot.org/uniprotkb/Q96EF0) (Phosphatidylinositol-3,5-bisphosphate 3-phosphatase MTMR8):

> Lipid phosphatase that specifically dephosphorylates the D-3 position of phosphatidylinositol 3-phosphate and phosphatidylinositol 3,5-bisphosphate, generating phosphatidylinositol and phosphatidylinositol 5-phosphate. In complex with MTMR9, negatively regulates autophagy.

**Summary**, from NCBI Gene [55613](https://www.ncbi.nlm.nih.gov/gene/55613):

> This gene encodes a member of the myotubularin-related family and is part of the MTMR6 subgroup. Family members are dual-specificity phosphatases and the encoded protein contains a phosphoinositide-binding domain (PID) and a SET-interacting domain (SID). Defects in other family members have been found in myotubular myopathic diseases. [provided by RefSeq, Mar 2010]

**Accessions** — [HGNC:16825](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16825) · Entrez [55613](https://www.ncbi.nlm.nih.gov/gene/55613) · UniProt [Q96EF0](https://www.uniprot.org/uniprotkb/Q96EF0) · Ensembl [ENSG00000102043](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102043)

## Data

Gene col 2207: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2207); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2207, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2207]; `tensor/DDL_lfc|DDL_z.npy` [2207]; `embed/gene_vectors.npy` [2207]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2207 or target_col == 2207). Every well: [[MTMR8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTMR8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
