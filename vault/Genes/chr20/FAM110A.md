---
symbol: "FAM110A"
type: "gene"
col: 4690
ensembl_id: "ENSG00000125898"
name: "family with sequence similarity 110 member A"
location: "20p13"
module: 22
arm: "+"
pooled_cpm: 8.13
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 17
n_dd_up_clean: 1
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# FAM110A

*family with sequence similarity 110 member A* — 20p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.50× (z +17.3, q 0e+00, up in 34 of 40 measured lines) ⚠ cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.06× (z +13.7, q 4e-40, up in 34 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (PANC-1 7.10×, CFPAC-1 4.67×, A549 4.13×, NCI-H2347 2.99×; ⚠ cell-cycle shift, explains ~35% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (SW480 2.77×, NCI-H460 4.62×, A498 4.19×); [[Harringtonine (drug)]] 5 µM in 1 line (PANC-1 5.26×; ⚠ cell-cycle shift, explains ~36% of this change).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.630× (z -6.2, q 3e-07, down in 23 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM72A]] (+0.67, fdr 7e-06), [[STARD8]] (+0.62, fdr 8e-06), [[HJURP]] (+0.62, fdr 8e-06); moves opposite to [[LARP4]] (-0.57, fdr 1e-05), [[GSR]] (-0.57, fdr 1e-05), [[AKR1C1]] (-0.54, fdr 2e-05).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TPBG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4690.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (PANC-1 7.10×, CFPAC-1 4.67×, A549 4.13×, NCI-H2347 2.99×; ⚠ cell-cycle shift, explains ~35% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (SW480 2.77×, NCI-H460 4.62×, A498 4.19×); [[Harringtonine (drug)]] 5 µM in 1 line (PANC-1 5.26×; ⚠ cell-cycle shift, explains ~36% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **2.50×** | +17.3 | 0e+00 | 34/40 (PANC-1, CFPAC-1, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.06×** | +13.7 | 4e-40 | 34/43 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **2.06×** | +9.3 | 3e-18 | 30/46 (PANC-1, A549, …) | top dose only | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~39% of this change | **1.69×** | +7.0 | 3e-10 | 19/35 (CFPAC-1, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.33×** | +3.8 | 0.020 | 13/40 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.31×** | +3.6 | 0.028 | 10/45 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.28× | +3.2 | 0.10 | 8/34 (CFPAC-1, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.40× | +3.2 | 0.10 | 6/37 (NCI-H460, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bentamapimod (drug)]] 0.05 µM |  | 1.27× | +3.1 | 0.14 | 3/46 (NCI-H23, COLO 205, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4690.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.630×** | -6.2 | 3e-07 | 23/46 (HOP62, HT-29, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.635×** | -6.1 | 3e-07 | 21/47 (HEC-1-A, HS-578T, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.654×** | -5.7 | 2e-06 | 19/30 (Hs 766T, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.666×** | -5.3 | 2e-05 | 18/44 (NCI-H2347, HS-578T, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **0.764×** | -5.1 | 3e-05 | 16/47 (NCI-H1573, NCI-H23, …) | rises with dose | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.688×** | -5.0 | 5e-05 | 15/44 (HOP62, HCT15, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.746×** | -4.1 | 0.004 | 11/48 (A-172, RKO, …) | all doses, flat | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.734×** | -3.9 | 0.006 | 17/44 (HEC-1-A, HOP62, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.753×** | -3.8 | 0.008 | 11/46 (A-172, SK-MEL-2, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.819×** | -3.7 | 0.010 | 13/46 (MIA PaCa-2, HOP62, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.754×** | -3.7 | 0.013 | 15/44 (J82, HOP62, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.767×** | -3.4 | 0.028 | 9/14 (A-172, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~42% of this change | **0.617×** | -3.4 | 0.030 | 11/29 (HOP62, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.774×** | -3.3 | 0.036 | 13/45 (HOP62, PANC-1, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.786×** | -3.3 | 0.043 | 8/47 (HOP62, A-172, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.773×** | -3.2 | 0.047 | 9/47 (PANC-1, NCI-H460, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.49 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4690. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 6.51 | 0 | 2 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.126× (z -9.3) ⚠ cell-cycle shift, explains ~34% of this change |
| [[HOP62 (line)]] | alt | 26.1 | 0 | 2 (2 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0473× (z -11.2) ⚠ toxic; cell-cycle shift, explains ~42% of this change |
| [[PANC-1 (line)]] | alt | 8.10 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.10× (z +17.0) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[SW480 (line)]] | alt | 8.42 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.77× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.258× (z -9.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 17.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.208× (z -9.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 5.41 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.19× (z +9.2) | — |
| [[A549 (line)]] | wt | 11.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +10.0) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[CFPAC-1 (line)]] | alt | 7.64 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +10.4) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[H4 (line)]] | wt | 14.4 | 0 | 1 | — | [[Triamcinolone (drug)]] 0.5 µM 0.0553× (z -10.7) |
| [[Hs 766T (line)]] | wt | 12.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0579× (z -13.2) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 9.63 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +9.5) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H460 (line)]] | wt | 3.50 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.62× (z +9.5) | — |
| [[SNU-423 (line)]] | alt | 6.68 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0762× (z -10.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 3.91 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.14 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.44 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.56 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.44 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.14 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.00 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.54 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.46 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.83 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.38 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.36 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.92 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.10 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.71 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.02 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.48 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.09 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4690), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM72A]] | +0.67 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[STARD8]] | +0.62 | +0.58 / +0.59 | both halves | 8e-06 |  |
| [[HJURP]] | +0.62 | +0.58 / +0.64 | both halves | 8e-06 |  |
| [[FAM72D]] | +0.61 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[ESPL1]] | +0.60 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[CDC25C]] | +0.59 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[NBPF14]] | +0.59 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[TRIOBP]] | +0.57 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[FAM72B]] | +0.56 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[NDE1]] | +0.56 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[SGO2]] | +0.56 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[STARD10]] | +0.56 | +0.53 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LARP4]] | -0.57 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[GSR]] | -0.57 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[AKR1C1]] | -0.54 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[VPS50]] | -0.52 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[NAA50]] | -0.51 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[MGST1]] | -0.51 | -0.42 / -0.59 | both halves | 4e-05 |  |
| [[OPA1]] | -0.51 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[TTC14]] | -0.50 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[AP3M1]] | -0.50 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[USP14]] | -0.50 | -0.40 / -0.60 | both halves | 5e-05 |  |
| [[PSMB2]] | -0.49 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[CDC123]] | -0.49 | -0.52 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TPBG]] | B | TPBG activity raises FAM110A's level | lines that do not express TPBG (10) vs lines expressing it (40) | 1.69× lower at baseline in the lines without TPBG | 0.037 | ⚠ within organs, on part of the lines |
| [[RAC2]] | B | RAC2 activity raises FAM110A's level | lines that do not express RAC2 (19) vs lines expressing it (31) | 1.58× lower at baseline in the lines without RAC2 | 0.039 | ⚠ within organs, on part of the lines; also absent: BHLHE41, ADTRP, MANCR |
| [[PINLYP]] | B | PINLYP activity raises FAM110A's level | lines that do not express PINLYP (17) vs lines expressing it (33) | 1.30× lower at baseline in the lines without PINLYP | 0.058 | ⚠ within organs, on part of the lines; also absent: C9, BMPER, CALD1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.466). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-37.4, -59.7); signed map (-53.4, -42.2). **Vector** length 90.4, 18.5% of its response variance represented; |z| ≥ 3 in 913 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +8.1 | +17.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.4 | +13.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +4.7 | +9.3 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~39% of this change | +3.9 | +7.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | +2.7 | +3.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +3.2 |
|  | [[Mebendazole (drug)]] 0.5 µM |  | +1.7 | +1.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.4 | +0.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.4 | +2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.3 | +1.5 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -4.2 | -6.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.9 | -6.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~55% of this change | -3.5 | -3.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.3 | -5.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.7 | -3.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.6 | -5.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.4 | -2.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.4 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 110 member A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p13 — chr20:833,715-857,463 (+) |
| Ensembl biotype | protein_coding |
| Also known as | bA371L19.3; previously C20orf55 |
| Matched by | ensembl_id |

UniProt [Q9BQ89](https://www.uniprot.org/uniprotkb/Q9BQ89) carries no function annotation.

**Summary**, from NCBI Gene [83541](https://www.ncbi.nlm.nih.gov/gene/83541):

> Involved in mitotic spindle organization. Located in cytosol; microtubule cytoskeleton; and nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16188](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16188) · Entrez [83541](https://www.ncbi.nlm.nih.gov/gene/83541) · UniProt [Q9BQ89](https://www.uniprot.org/uniprotkb/Q9BQ89) · Ensembl [ENSG00000125898](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125898)

## Data

Gene col 4690: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4690); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4690, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4690]; `tensor/DDL_lfc|DDL_z.npy` [4690]; `embed/gene_vectors.npy` [4690]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4690 or target_col == 4690). Every well: [[FAM110A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM110A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
