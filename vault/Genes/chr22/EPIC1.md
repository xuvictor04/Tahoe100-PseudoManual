---
symbol: "EPIC1"
type: "gene"
col: 13391
ensembl_id: "ENSG00000224271"
name: "epigenetically induced MYC interacting lncRNA 1"
location: "22q13.31"
module: 105
arm: "+"
pooled_cpm: 757.09
n_lines_expressing: 27
n_dd_up: 1
n_dd_down: 43
n_dd_up_clean: 1
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 7
direction_downstream: 14
tags: ["gene", "module/105"]
generated_by: "tahoemap"
---

# EPIC1

*epigenetically induced MYC interacting lncRNA 1* — 22q13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Lactate (calcium) (drug)]] 0.5 µM: 1.24× (z +3.9, q 0.060, up in 16 of 25 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Auranofin (drug)]] 5 µM in 1 line (SHP-77 2.26×).
> Pooled over the cell lines (median), lowered significantly by 43 drug-doses (20 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.181× (z -42.6, q 0e+00, down in 25 of 25 measured lines).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TPT1-AS1]] (+0.49, fdr 3e-05), [[GBE1]] (+0.48, fdr 4e-05), [[AGAP1]] (+0.47, fdr 4e-05); moves opposite to [[NEIL1]] (-0.51, fdr 3e-05), [[YWHAEP7-1]] (-0.50, fdr 8e-05), [[AGAP13P]] (-0.44, fdr 1e-04).
> It is in [[Module 105]], a single-armed module (Late Phase of HIV Life Cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[ZC3H12B]] → it (grade B ⚠); 14 go from it, the strongest it → [[GOLGA6L9]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13391.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Auranofin (drug)]] 5 µM in 1 line (SHP-77 2.26×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **1.24×** | +3.9 | 0.060 | 16/25 (A-172, RPMI-7951, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 48 in all, 23 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 43 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13391.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.181×** | -42.6 | 0e+00 | 25/25 (SNU-423, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.176×** | -27.5 | 0e+00 | 25/25 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.230×** | -25.9 | 0e+00 | 25/26 (SK-MEL-2, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.267×** | -23.3 | 0e+00 | 25/25 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.421×** | -21.5 | 0e+00 | 25/26 (NCI-H1792, BT-474, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.264×** | -21.1 | 0e+00 | 24/24 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.284×** | -19.9 | 0e+00 | 25/25 (HepG2/C3A, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.294×** | -19.9 | 0e+00 | 23/24 (C-33 A, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.297×** | -19.2 | 0e+00 | 25/25 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.373×** | -17.4 | 0e+00 | 25/25 (PANC-1, BT-474, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.186×** | -15.5 | 0e+00 | 26/26 (NCI-H1573, LS 180, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.420×** | -15.3 | 0e+00 | 25/25 (PANC-1, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.450×** | -14.1 | 3e-43 | 23/25 (HEC-1-A, A-427, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.590×** | -13.1 | 1e-37 | 23/25 (SK-MEL-2, SNU-423, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.487×** | -12.7 | 3e-35 | 25/25 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.261×** | -12.3 | 2e-33 | 22/25 (LS 180, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.594×** | -9.2 | 1e-18 | 22/25 (RPMI-7951, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.653×** | -7.5 | 1e-12 | 20/25 (RPMI-7951, SK-MEL-2, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.784×** | -6.0 | 3e-08 | 19/25 (A-172, BT-474, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.755×** | -4.9 | 2e-05 | 19/25 (PANC-1, A-427, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.761×** | -4.5 | 1e-04 | 19/25 (SNU-423, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.620×** | -4.4 | 2e-04 | 21/26 (NCI-H1573, NCI-H1792, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.44 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13391. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 1,379 | 0 | 23 (15 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -35.4) |
| [[C-33 A (line)]] | alt | 2,436 | 0 | 23 (14 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0802× (z -30.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.202× (z -27.5) |
| [[PANC-1 (line)]] | alt | 615 | 0 | 23 (14 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -43.9) |
| [[HEC-1-A (line)]] | alt | 2,214 | 0 | 22 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -36.0) |
| [[LOX-IMVI (line)]] | wt | 740 | 0 | 22 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -31.7) |
| [[NCI-H1792 (line)]] | alt | 1,359 | 0 | 22 (13 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0660× (z -47.8) |
| [[NCI-H23 (line)]] | alt | 1,646 | 0 | 20 (14 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -33.6) |
| [[HepG2_C3A (line)]] | wt | 730 | 0 | 19 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -29.9) |
| [[NCI-H1573 (line)]] | alt | 4,334 | 0 | 19 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0815× (z -41.3) |
| [[SK-MEL-2 (line)]] | alt | 973 | 0 | 19 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -40.5) |
| [[SNU-423 (line)]] | alt | 1,274 | 0 | 19 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0527× (z -48.1) |
| [[H4 (line)]] | wt | 2,776 | 0 | 17 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -30.3) |
| [[RPMI-7951 (line)]] | alt | 2,167 | 0 | 17 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -35.3) |
| [[SNU-1 (line)]] | wt | 3,320 | 0 | 17 (7 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0959× (z -23.6) |
| [[KATO III (line)]] | alt | 1,530 | 0 | 16 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -31.6) |
| [[AN3 CA (line)]] | alt | 1,104 | 0 | 14 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -27.3) |
| [[LS 180 (line)]] | wt | 2,160 | 0 | 14 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.144× (z -23.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.177× (z -18.8) |
| [[A-172 (line)]] | wt | 697 | 0 | 13 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0805× (z -46.5) |
| [[HT-29 (line)]] | alt | 458 | 0 | 13 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -30.5) |
| [[HS-578T (line)]] | alt | 3,042 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0752× (z -32.1) |
| [[LoVo (line)]] | wt | 355 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -31.2) |
| [[A-427 (line)]] | wt | 590 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -33.4) |
| [[SHP-77 (line)]] | alt | 2,004 | 1 | 10 (5 ⚠) | [[Auranofin (drug)]] 5 µM 2.26× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.136× (z -26.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.503× (z -14.0) |
| [[SW 1271 (line)]] | alt | 879 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -14.4) |
| [[A498 (line)]] | wt | 51.7 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 52.5 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 94.5 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 177 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 59.7 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 89.1 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 76.8 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 148 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 72.1 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 61.3 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 137 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 74.4 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 51.1 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 58.9 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 629 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 53.0 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 63.2 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 888 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 251 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 54.3 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 74.5 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 143 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 81.2 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 75.6 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 81.6 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 59.5 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13391), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 8 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPT1-AS1]] | +0.49 | +0.46 / +0.49 | both halves | 3e-05 |  |
| [[GBE1]] | +0.48 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[AGAP1]] | +0.47 | +0.43 / +0.49 | both halves | 4e-05 |  |
| [[LINC02649]] | +0.46 | +0.38 / +0.45 | both halves | 6e-05 |  |
| [[LINC01203]] | +0.45 | +0.33 / +0.38 | both halves | 1e-04 |  |
| [[EFCAB3P1]] | +0.45 | +0.41 / +0.48 | both halves | 4e-05 |  |
| [[LINC02616]] | +0.45 | +0.44 / +0.44 | both halves | 3e-05 |  |
| [[C1QTNF7-AS1]] | +0.44 | +0.18 / +0.54 | ⚠ one half (not replicated) | 9e-04 |  |
| [[KCNQ1OT1]] | +0.43 | +0.34 / +0.41 | both halves | 1e-04 | same gene group |
| [[BNIP3L]] | +0.43 | +0.47 / +0.33 | both halves | 1e-04 |  |
| [[FUT11]] | +0.43 | +0.45 / +0.42 | both halves | 4e-05 |  |
| [[LINC03009-1]] | +0.42 | +0.39 / +0.40 | both halves | 6e-05 |  |
| [[TMEM14B]] | +0.42 | +0.24 / +0.44 | both halves | 5e-04 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NEIL1]] | -0.51 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[YWHAEP7-1]] | -0.50 | -0.48 / -0.37 | both halves | 8e-05 |  |
| [[AGAP13P]] | -0.44 | -0.36 / -0.34 | both halves | 1e-04 |  |
| [[PGAP4]] | -0.43 | -0.41 / -0.24 | both halves | 4e-04 |  |
| [[KCTD3]] | -0.40 | -0.39 / -0.40 | both halves | 5e-05 |  |
| [[BMS1P1-1]] | -0.39 | -0.23 / -0.37 | both halves | 5e-04 |  |
| [[GUCY1B2]] | -0.39 | -0.41 / -0.29 | both halves | 2e-04 |  |
| [[GPR87]] | -0.39 | -0.27 / -0.35 | both halves | 3e-04 |  |
| [[ALDH3B1]] | -0.38 | -0.50 / -0.24 | both halves | 5e-04 |  |
| [[LINC01508]] | -0.37 | -0.31 / -0.36 | both halves | 2e-04 |  |
| [[ITGB8]] | -0.37 | -0.42 / -0.33 | both halves | 1e-04 |  |
| [[IL22RA1]] | -0.37 | -0.27 / -0.35 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 3, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZC3H12B]] | B | ZC3H12B activity raises EPIC1's level | lines that do not express ZC3H12B (21) vs lines expressing it (29) | 2.84× lower at baseline in the lines without ZC3H12B | 0.042 | ⚠ within organs, on part of the lines; also absent: RUNX3, TMEM132D, LINC01876 |
| [[TOP2A]] | B | TOP2A activity raises EPIC1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.8% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[GABRA3]] | B | GABRA3 activity raises EPIC1's level | lines that do not express GABRA3 (26) vs lines expressing it (24) | 2.92× lower at baseline in the lines without GABRA3 | 0.081 | ⚠ within organs, on part of the lines; also absent: MAGEA3-DT, MKRN3, LRRTM4 |
| [[MAGEA3-DT]] | C | MAGEA3-DT activity raises EPIC1's level | lines that do not express MAGEA3-DT (29) vs lines expressing it (21) | 4.42× lower at baseline in the lines without MAGEA3-DT | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRA3, LINC00648, LINC00470; co-absent with the target |
| [[LINC02575]] | C | LINC02575 activity raises EPIC1's level | lines that do not express LINC02575 (32) vs lines expressing it (18) | 3.05× lower at baseline in the lines without LINC02575 | 0.014 | ⚠ within organs, on part of the lines; also absent: ENSG00000289309, LINC01205, MSRB3-AS1; co-absent with the target |
| [[ASNSP1]] | C | ASNSP1 activity raises EPIC1's level | lines that do not express ASNSP1 (35) vs lines expressing it (15) | 3.29× lower at baseline in the lines without ASNSP1 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZNF208, GCG, GPR15; co-absent with the target |
| [[LINC02616]] | C | LINC02616 activity raises EPIC1's level | lines that do not express LINC02616 (37) vs lines expressing it (13) | 4.85× lower at baseline in the lines without LINC02616 | 0.082 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ADGRG7, ENSG00000287474, FCRLA; co-absent with the target |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 10, C 4. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GOLGA6L9]] | B | EPIC1 activity raises GOLGA6L9's level | lines that do not express EPIC1 (23) vs lines expressing it (27) | 1.40× lower at baseline in the lines without EPIC1 | 0.003 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ENSG00000243620, POTEE, FAR2P1 |
| [[ITGB8]] | B | EPIC1 activity weakens ITGB8's drug response | lines that do not express EPIC1 (16) vs lines expressing it (15) | the lines without EPIC1 respond 1.32× as strongly (z diff -1.41); strongest at Auranofin 5 µM: 0.29x vs 0.66x (z diff -5.1) | 0.014 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ENSG00000243620, POTEE, FAR2P1; target measured in part of the lines; artifact flags |
| [[UBE2Q2P2-1]] | B | EPIC1 activity raises UBE2Q2P2-1's level | lines that do not express EPIC1 (23) vs lines expressing it (27) | 1.32× lower at baseline in the lines without EPIC1 | 0.019 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ENSG00000243620, POTEE, FAR2P1 |
| [[GABRA3]] | B | EPIC1 activity raises GABRA3's level | lines that do not express EPIC1 (23) vs lines expressing it (27) | 2.92× lower at baseline in the lines without EPIC1 | 0.023 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ENSG00000243620, POTEE, FAR2P1 |
| [[UBE2Q2P2]] | B | EPIC1 activity raises UBE2Q2P2's level | lines that do not express EPIC1 (23) vs lines expressing it (27) | 1.38× lower at baseline in the lines without EPIC1 | 0.024 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ENSG00000243620, POTEE, FAR2P1 |
| [[ZC3H12B]] | B | EPIC1 activity raises ZC3H12B's level | lines that do not express EPIC1 (23) vs lines expressing it (27) | 2.96× lower at baseline in the lines without EPIC1 | 0.044 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ENSG00000243620, POTEE, FAR2P1 |
| [[BCKDHB]] | B | EPIC1 activity raises BCKDHB's level | lines that do not express EPIC1 (23) vs lines expressing it (27) | 1.48× lower at baseline in the lines without EPIC1 | 0.054 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ENSG00000243620, POTEE, FAR2P1 |
| [[MFSD4B]] | B | EPIC1 activity raises MFSD4B's level | lines that do not express EPIC1 (23) vs lines expressing it (27) | 1.54× lower at baseline in the lines without EPIC1 | 0.067 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ENSG00000243620, POTEE, FAR2P1 |
| [[GBE1]] | B | EPIC1 activity lowers GBE1's level | lines that do not express EPIC1 (23) vs lines expressing it (27) | 1.28× higher at baseline in the lines without EPIC1 | 0.071 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ENSG00000243620, POTEE, FAR2P1 |
| [[KIAA1328]] | B | EPIC1 activity raises KIAA1328's level | lines that do not express EPIC1 (23) vs lines expressing it (27) | 1.42× lower at baseline in the lines without EPIC1 | 0.076 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ENSG00000243620, POTEE, FAR2P1 |
| [[MAGEA3-DT]] | C | EPIC1 activity raises MAGEA3-DT's level | lines that do not express EPIC1 (23) vs lines expressing it (27) | 4.40× lower at baseline in the lines without EPIC1 | 0.005 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ENSG00000243620, POTEE, FAR2P1; co-absent with the target |
| [[LINC02575]] | C | EPIC1 activity raises LINC02575's level | lines that do not express EPIC1 (23) vs lines expressing it (27) | 2.57× lower at baseline in the lines without EPIC1 | 0.023 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ENSG00000243620, POTEE, FAR2P1; co-absent with the target |

## Where it sits

- **Module**: [[Module 105]] — Late Phase of HIV Life Cycle; 44 genes; every member is in the + arm (projection on the module's main direction 0.355). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (19.8, -18.1); signed map (-38.2, 29.2). **Vector** length 107, 34.8% of its response variance represented; |z| ≥ 3 in 1,055 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.1 | +0.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +3.3 | -15.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.7 | +1.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +2.6 | -10.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.5 | -27.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.0 | +2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.9 | -7.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +1.6 | +2.3 |
| fall | [[Selinexor (drug)]] 5 µM |  | -5.6 | -13.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | -4.8 | -21.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -4.8 | -12.7 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -1.4 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -3.1 | -3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.2 | -6.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | -12.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.1 | -1.9 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -1.9 | -0.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.8 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | epigenetically induced MYC interacting lncRNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 22q13.31 — chr22:47,630,827-48,023,004 (+) |
| Ensembl biotype | lncRNA |
| Also known as | Lnc-EPIC1 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:27672](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27672) · Entrez [284930](https://www.ncbi.nlm.nih.gov/gene/284930) · Ensembl [ENSG00000224271](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000224271)

## Data

Gene col 13391: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13391); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13391, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13391]; `tensor/DDL_lfc|DDL_z.npy` [13391]; `embed/gene_vectors.npy` [13391]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13391 or target_col == 13391). Every well: [[EPIC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EPIC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
