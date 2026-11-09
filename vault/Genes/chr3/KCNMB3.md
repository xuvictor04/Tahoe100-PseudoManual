---
symbol: "KCNMB3"
type: "gene"
col: 10054
ensembl_id: "ENSG00000171121"
name: "potassium calcium-activated channel subfamily M regulatory beta subunit 3"
location: "3q26.32"
module: 10
arm: "+"
pooled_cpm: 10.52
n_lines_expressing: 43
n_dd_up: 15
n_dd_down: 8
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# KCNMB3

*potassium calcium-activated channel subfamily M regulatory beta subunit 3* — 3q26.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.78× (z +10.1, q 4e-21, up in 29 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.583× (z -6.7, q 1e-08, down in 24 of 40 measured lines) ⚠ cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 0.559× (z -3.7, q 0.015, down in 13 of 35 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 7 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 3 lines (RPMI-7951 0.0640×, PANC-1 0.238×, HT-29 0.151×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 3 lines (LOX-IMVI 0.0440×, PANC-1 0.282×, MIA PaCa-2 0.266×; ⚠ cell-cycle shift, explains ~39% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (COLO 205 0.210×, SK-MEL-2 0.205×; ⚠ toxic; transcription drop); [[PH-797804 (drug)]] 5 µM in 1 line (MIA PaCa-2 0.0329×); [[Captopril (drug)]] 0.05 µM in 1 line (NCI-H1573 0.0599×); [[Glycyrrhizic acid (drug)]] 5 µM in 1 line (BT-474 0.0723×).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C22orf46]] (+0.69, fdr 7e-06), [[ZSCAN29]] (+0.68, fdr 2e-05), [[FKRP]] (+0.67, fdr 2e-05); moves opposite to [[MLEC]] (-0.68, fdr 7e-06), [[TRAPPC1]] (-0.66, fdr 7e-05), [[NHP2]] (-0.64, fdr 4e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 1 goes from it, the strongest it → [[PPID]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10054.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **1.78×** | +10.1 | 4e-21 | 29/39 (A498, SW480, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.51×** | +7.2 | 1e-10 | 20/39 (MIA PaCa-2, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.70×** | +6.5 | 1e-08 | 18/40 (C32, SK-MEL-2, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.70×** | +6.3 | 5e-08 | 10/18 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +5.6 | 2e-06 | 23/41 (NCI-H1573, HT-29, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.57×** | +5.6 | 2e-06 | 21/38 (MIA PaCa-2, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.49×** | +4.7 | 2e-04 | 18/39 (SHP-77, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.45×** | +4.6 | 3e-04 | 13/38 (SW480, J82, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.43×** | +4.4 | 7e-04 | 15/32 (LoVo, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.40×** | +4.2 | 0.002 | 13/38 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.32×** | +3.4 | 0.033 | 10/40 (SW 900, SHP-77, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.68×** | +3.3 | 0.045 | 8/39 (SK-MEL-2, J82, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.33×** | +3.3 | 0.048 | 9/29 (HS-578T, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.31×** | +3.2 | 0.049 | 12/38 (SK-MEL-2, MIA PaCa-2, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.30×** | +3.2 | 0.056 | 7/40 (HOP62, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 7 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10054.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 7 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 3 lines (RPMI-7951 0.0640×, PANC-1 0.238×, HT-29 0.151×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 3 lines (LOX-IMVI 0.0440×, PANC-1 0.282×, MIA PaCa-2 0.266×; ⚠ cell-cycle shift, explains ~39% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (COLO 205 0.210×, SK-MEL-2 0.205×; ⚠ toxic; transcription drop); [[PH-797804 (drug)]] 5 µM in 1 line (MIA PaCa-2 0.0329×); [[Captopril (drug)]] 0.05 µM in 1 line (NCI-H1573 0.0599×); [[Glycyrrhizic acid (drug)]] 5 µM in 1 line (BT-474 0.0723×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.583×** | -6.7 | 1e-08 | 24/40 (HEC-1-A, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.639×** | -5.6 | 6e-06 | 21/40 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.640×** | -5.5 | 6e-06 | 22/40 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.652×** | -5.3 | 1e-05 | 21/40 (PANC-1, HT-29, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.652×** | -5.3 | 1e-05 | 22/36 (RPMI-7951, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.717×** | -4.1 | 0.003 | 16/40 (COLO 205, HEC-1-A, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.559×** | -3.7 | 0.015 | 13/35 (MIA PaCa-2, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.593×** | -3.4 | 0.056 | 12/39 (A498, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.783× | -3.0 | 0.13 | 11/35 (CFPAC-1, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.783× | -3.0 | 0.13 | 15/38 (SK-MEL-2, RPMI-7951, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10054. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 22.4 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +9.0) | [[PH-797804 (drug)]] 5 µM 0.0329× (z -11.5) |
| [[SK-MEL-2 (line)]] | alt | 25.4 | 0 | 3 (3 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.179× (z -10.7) ⚠ cell-cycle shift, explains ~99% of this change |
| [[COLO 205 (line)]] | alt | 40.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.210× (z -11.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 20.8 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.238× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[BT-474 (line)]] | alt | 8.26 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 5 µM 0.0723× (z -10.0) |
| [[CFPAC-1 (line)]] | alt | 15.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +8.5) | — |
| [[HOP62 (line)]] | alt | 3.56 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0933× (z -8.8) ⚠ cell-cycle shift, explains ~68% of this change |
| [[HT-29 (line)]] | alt | 8.74 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.151× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[LOX-IMVI (line)]] | wt | 4.42 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0440× (z -11.2) ⚠ cell-cycle shift, explains ~39% of this change |
| [[NCI-H1573 (line)]] | alt | 4.67 | 0 | 1 | — | [[Captopril (drug)]] 0.05 µM 0.0599× (z -10.4) |
| [[NCI-H2030 (line)]] | alt | 8.14 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +8.6) | — |
| [[RPMI-7951 (line)]] | alt | 15.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0640× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[A-172 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.43 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.24 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.17 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.81 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.52 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.06 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.53 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.14 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.10 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.66 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.53 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.43 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.09 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.48 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.59 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 9.11 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10054), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C22orf46]] | +0.69 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[ZSCAN29]] | +0.68 | +0.70 / +0.46 | both halves | 2e-05 |  |
| [[FKRP]] | +0.67 | +0.67 / +0.48 | both halves | 2e-05 |  |
| [[ZNF594]] | +0.67 | +0.70 / +0.57 | both halves | 1e-05 |  |
| [[ZBED9]] | +0.66 | +0.71 / +0.56 | both halves | 1e-05 |  |
| [[ZNF391]] | +0.65 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[ZNF528]] | +0.65 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[ZNF606]] | +0.65 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[TYW3]] | +0.64 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[RIPK2-DT]] | +0.64 | +0.64 / +0.47 | both halves | 2e-05 |  |
| [[LINC01725]] | +0.64 | +0.64 / +0.37 | both halves | 8e-05 |  |
| [[ZNF189]] | +0.63 | +0.69 / +0.38 | both halves | 6e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MLEC]] | -0.68 | -0.64 / -0.64 | both halves | 7e-06 |  |
| [[TRAPPC1]] | -0.66 | -0.72 / -0.38 | both halves | 7e-05 |  |
| [[NHP2]] | -0.64 | -0.58 / -0.42 | both halves | 4e-05 |  |
| [[VKORC1]] | -0.62 | -0.63 / -0.47 | both halves | 2e-05 |  |
| [[NOMO1]] | -0.62 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[GMCL1]] | -0.61 | -0.62 / -0.36 | both halves | 9e-05 |  |
| [[KDM4B]] | -0.61 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[TMED4]] | -0.61 | -0.62 / -0.53 | both halves | 1e-05 |  |
| [[GLG1]] | -0.60 | -0.64 / -0.49 | both halves | 2e-05 |  |
| [[ATP6AP2]] | -0.60 | -0.65 / -0.51 | both halves | 1e-05 |  |
| [[AKR7A2]] | -0.60 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[SDHA]] | -0.60 | -0.61 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises KCNMB3's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[DTX3]] | B | DTX3 activity raises KCNMB3's level | lines that do not express DTX3 (14) vs lines expressing it (36) | 1.85× lower at baseline in the lines without DTX3 | 0.085 | ⚠ within organs, on part of the lines; co-occurs with ARID1A, SETD1B; also absent: NRIP3, UPK1A-AS1, SDK2 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PPID]] | B | KCNMB3 activity lowers PPID's level | lines that do not express KCNMB3 (7) vs lines expressing it (43) | 1.41× higher at baseline in the lines without KCNMB3 | 0.034 | ⚠ within organs, on part of the lines; also absent: IQCD, MLF1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.622). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-28.1, 14.3); signed map (12.5, -22.7). **Vector** length 72.7, 14.1% of its response variance represented; |z| ≥ 3 in 762 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +6.6 | +10.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.8 | +7.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.2 | +5.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.1 | +6.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +6.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +5.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +1.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.6 | +3.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | +2.9 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -3.7 | -6.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -3.1 | -3.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -2.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | -2.4 | -4.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -2.0 | -5.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | -1.1 |
|  | [[Sinomenine (drug)]] 0.5 µM |  | -1.4 | -2.3 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.2 | -2.4 |
|  | [[Fumaric acid (drug)]] 5 µM |  | -1.2 | -2.3 |
|  | [[Flumatinib (mesylate) (drug)]] 0.5 µM |  | -1.1 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | potassium calcium-activated channel subfamily M regulatory beta subunit 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q26.32 — chr3:179,236,691-179,267,002 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously KCNMB2, KCNMBL |
| Gene groups (HGNC) | Potassium calcium-activated channel subfamily M regulatory beta subunits |
| Reactome | 7 pathways, smallest: Ca2+ activated K+ channels; cGMP effects; Nitric oxide stimulates guanylate cyclase |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NPA1](https://www.uniprot.org/uniprotkb/Q9NPA1) (Calcium-activated potassium channel subunit beta-3):

> Regulatory subunit of the calcium activated potassium KCNMA1 (maxiK) channel. Modulates the calcium sensitivity and gating kinetics of KCNMA1, thereby contributing to KCNMA1 channel diversity. Alters the functional properties of the current expressed by the KCNMA1 channel. Isoform 2, isoform 3 and isoform 4 partially inactivate the current of KCNBMA. Isoform 4 induces a fast and incomplete inactivation of KCNMA1 channel that is detectable only at large depolarizations. In contrast, isoform 1 …

**Summary**, from NCBI Gene [27094](https://www.ncbi.nlm.nih.gov/gene/27094):

> MaxiK channels are large conductance, voltage and calcium-sensitive potassium channels which are fundamental to the control of smooth muscle tone and neuronal excitability. MaxiK channels can be formed by 2 subunits: the pore-forming alpha subunit and the modulatory beta subunit. The protein encoded by this gene is an auxiliary beta subunit which may partially inactivate or slightly decrease the activation time of MaxiK alpha subunit currents. Alternative splicing results in multiple transcript …

**Accessions** — [HGNC:6287](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6287) · Entrez [27094](https://www.ncbi.nlm.nih.gov/gene/27094) · UniProt [Q9NPA1](https://www.uniprot.org/uniprotkb/Q9NPA1) · Ensembl [ENSG00000171121](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171121)

## Data

Gene col 10054: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10054); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10054, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10054]; `tensor/DDL_lfc|DDL_z.npy` [10054]; `embed/gene_vectors.npy` [10054]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10054 or target_col == 10054). Every well: [[KCNMB3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCNMB3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
