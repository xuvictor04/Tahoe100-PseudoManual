---
symbol: "NELL2"
type: "gene"
col: 11558
ensembl_id: "ENSG00000184613"
name: "neural EGFL like 2"
location: "12q12"
module: 9
arm: "+"
pooled_cpm: 10.41
n_lines_expressing: 22
n_dd_up: 29
n_dd_down: 0
n_dd_up_clean: 21
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 23
direction_downstream: 16
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# NELL2

*neural EGFL like 2* — 12q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (8 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 3.46× (z +23.8, q 0e+00, up in 18 of 20 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 3 lines (SK-MEL-2 0.154×, C-33 A 0.266×, SHP-77 0.300×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SK-MEL-2 0.117×, C-33 A 0.270×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (C-33 A 0.116×; ⚠ toxic; transcription drop); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (C-33 A 0.240×); [[5-Azacytidine (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0709×); [[Homoharringtonine (drug)]] 5 µM in 1 line (LOX-IMVI 0.413×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RBM20]] (+0.65, fdr 7e-06), [[CSMD3]] (+0.64, fdr 1e-05), [[KCNH7]] (+0.64, fdr 7e-06); moves opposite to [[BMS1P4-1]] (-0.51, fdr 9e-05), [[NMNAT1]] (-0.50, fdr 1e-04), [[GUCA1B]] (-0.47, fdr 1e-04).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 23 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 16 go from it, the strongest it → [[ADGRL2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11558.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **3.46×** | +23.8 | 0e+00 | 18/20 (LoVo, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.17×** | +22.2 | 0e+00 | 7/16 (LoVo, J82, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.07×** | +15.3 | 0e+00 | 16/18 (LoVo, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.78×** | +13.9 | 1e-41 | 15/20 (NCI-H23, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.66×** | +13.3 | 2e-38 | 5/14 (J82, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.63×** | +13.2 | 2e-37 | 18/20 (NCI-H23, LoVo, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.64×** | +12.7 | 4e-35 | 5/9 (J82, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.34×** | +11.4 | 3e-28 | 12/19 (NCI-H23, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.92×** | +8.9 | 4e-17 | 11/19 (NCI-H23, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +7.6 | 2e-12 | 3/16 (LoVo, J82, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.47×** | +7.4 | 6e-12 | 1/17 (C32) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.69×** | +7.1 | 6e-11 | 5/19 (LoVo, J82, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.67×** | +6.5 | 4e-09 | 3/11 (J82, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.39×** | +6.4 | 7e-09 | 7/20 (J82, LoVo, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +5.7 | 6e-07 | 3/17 (LoVo, C32, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.15×** | +5.4 | 2e-06 | 8/18 (NCI-H23, NCI-H2030, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.47×** | +5.2 | 8e-06 | 7/18 (NCI-H23, J82, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +3.9 | 0.003 | 1/20 (SW1417) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11558.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 3 lines (SK-MEL-2 0.154×, C-33 A 0.266×, SHP-77 0.300×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SK-MEL-2 0.117×, C-33 A 0.270×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (C-33 A 0.116×; ⚠ toxic; transcription drop); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (C-33 A 0.240×); [[5-Azacytidine (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0709×); [[Homoharringtonine (drug)]] 5 µM in 1 line (LOX-IMVI 0.413×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | 0.774× | -3.4 | 0.34 | 10/19 (SK-MEL-2, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.797× | -3.1 | 0.51 | 5/20 (SW480, C32, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11558. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 3.52 | 5 | 0 | [[Tucidinostat (drug)]] 5 µM 16.7× (z +11.8) | — |
| [[C-33 A (line)]] | alt | 96.3 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.116× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Glycyrrhizic acid (drug)]] 0.05 µM 0.240× (z -9.4) |
| [[LoVo (line)]] | wt | 3.87 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 12.5× (z +13.9) | — |
| [[NCI-H2030 (line)]] | alt | 3.95 | 3 | 1 | [[Tucidinostat (drug)]] 5 µM 7.80× (z +10.0) | [[5-Azacytidine (drug)]] 0.5 µM 0.0709× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 46.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.117× (z -12.6) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 63.4 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.205× (z -13.0) ⚠ transcription drop |
| [[C32 (line)]] | wt | 7.88 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 5.91× (z +9.1) | — |
| [[CFPAC-1 (line)]] | alt | 4.43 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0572× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 11.5 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.32× (z +8.5) | — |
| [[LOX-IMVI (line)]] | wt | 34.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -8.9) |
| [[SHP-77 (line)]] | alt | 44.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.300× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[A-172 (line)]] | wt | 1.52 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.93 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.96 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.92 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.49 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 8.20 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.57 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.55 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.06 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.47 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.92 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.47 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.48 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.28 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.89 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.74 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.49 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.24 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.58 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.43 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.34 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.92 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11558), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBM20]] | +0.65 | +0.62 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[CSMD3]] | +0.64 | +0.54 / +0.58 | both halves | 1e-05 | **novel candidate** |
| [[KCNH7]] | +0.64 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[ASXL3]] | +0.63 | +0.46 / +0.62 | both halves | 3e-05 |  |
| [[TMEM108]] | +0.62 | +0.55 / +0.68 | both halves | 1e-05 |  |
| [[AKAP6]] | +0.60 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[SLAIN1]] | +0.60 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[GRIA2]] | +0.60 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[GABRG2]] | +0.59 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[GABRA2]] | +0.58 | +0.60 / +0.46 | both halves | 2e-05 |  |
| [[ENTREP2]] | +0.58 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[SUSD4]] | +0.57 | +0.48 / +0.60 | both halves | 2e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BMS1P4-1]] | -0.51 | -0.37 / -0.37 | both halves | 9e-05 |  |
| [[NMNAT1]] | -0.50 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[GUCA1B]] | -0.47 | -0.33 / -0.39 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 2, C 21. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers NELL2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MIR2052HG]] | B | MIR2052HG activity raises NELL2's level | lines that do not express MIR2052HG (27) vs lines expressing it (23) | 2.35× lower at baseline in the lines without MIR2052HG | 0.081 | ⚠ within organs, on part of the lines; also absent: PI15, ENSG00000251598, ENSG00000287352; maybe low, not absent |
| [[CSMD3]] | C | CSMD3 activity raises NELL2's level | lines that do not express CSMD3 (36) vs lines expressing it (14) | 3.27× lower at baseline in the lines without CSMD3 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, LINC01205, ENSG00000243486; co-absent with the target |
| [[BMP5]] | C | BMP5 activity raises NELL2's level | lines that do not express BMP5 (38) vs lines expressing it (12) | 3.89× lower at baseline in the lines without BMP5 | 0.007 | ⚠ within organs, on part of the lines; also absent: LINC01035, CPLX2, SCG3; co-absent with the target |
| [[ANO4]] | C | ANO4 activity raises NELL2's level | lines that do not express ANO4 (30) vs lines expressing it (20) | 3.91× lower at baseline in the lines without ANO4 | 0.007 | ⚠ within organs, on part of the lines; also absent: LINC01194, INA, ZNF667-AS1; maybe low, not absent; co-absent with the target |
| [[LINC02050]] | C | LINC02050 activity raises NELL2's level | lines that do not express LINC02050 (37) vs lines expressing it (13) | 2.90× lower at baseline in the lines without LINC02050 | 0.009 | ⚠ within organs, on part of the lines; also absent: ENSG00000286329, ENSG00000242828, PASD1; co-absent with the target |
| [[SLC25A24P1]] | C | SLC25A24P1 activity raises NELL2's level | lines that do not express SLC25A24P1 (40) vs lines expressing it (10) | 4.69× lower at baseline in the lines without SLC25A24P1 | 0.011 | ⚠ within organs, on part of the lines; also absent: LINC01425, ENSG00000275016, MAGEB2; co-absent with the target |
| [[RUNX1T1]] | C | RUNX1T1 activity raises NELL2's level | lines that do not express RUNX1T1 (38) vs lines expressing it (12) | 2.19× lower at baseline in the lines without RUNX1T1 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, ENSG00000232252, SYT4; co-absent with the target |
| [[POU3F2]] | C | POU3F2 activity raises NELL2's level | lines that do not express POU3F2 (32) vs lines expressing it (18) | 2.34× lower at baseline in the lines without POU3F2 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MSR1, AMPH, SPARC; co-absent with the target |
| [[LINC02315]] | C | LINC02315 activity raises NELL2's level | lines that do not express LINC02315 (31) vs lines expressing it (19) | 3.39× lower at baseline in the lines without LINC02315 | 0.022 | ⚠ within organs, on part of the lines; also absent: GABRG2, COX7B2, SLC25A24P1; co-absent with the target |
| [[GABRG2]] | C | GABRG2 activity raises NELL2's level | lines that do not express GABRG2 (36) vs lines expressing it (14) | 2.77× lower at baseline in the lines without GABRG2 | 0.024 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, PCSK1, BAGE2; maybe low, not absent; co-absent with the target |
| [[KCNH7]] | C | KCNH7 activity raises NELL2's level | lines that do not express KCNH7 (35) vs lines expressing it (15) | 3.37× lower at baseline in the lines without KCNH7 | 0.025 | ⚠ within organs, on part of the lines; also absent: FUT9, ENSG00000289309, PI15; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 7, C 9. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADGRL2]] | B | NELL2 activity raises ADGRL2's level | lines that do not express NELL2 (28) vs lines expressing it (22) | 2.68× lower at baseline in the lines without NELL2 | 0.025 | ⚠ within organs, on part of the lines; also absent: SOX2, FREM2, PTH2R; maybe low, not absent |
| [[AGBL4]] | B | NELL2 activity raises AGBL4's level | lines that do not express NELL2 (28) vs lines expressing it (22) | 2.21× lower at baseline in the lines without NELL2 | 0.040 | ⚠ within organs, on part of the lines; also absent: SOX2, FREM2, PTH2R; maybe low, not absent |
| [[MIR2052HG]] | B | NELL2 activity raises MIR2052HG's level | lines that do not express NELL2 (28) vs lines expressing it (22) | 2.39× lower at baseline in the lines without NELL2 | 0.056 | ⚠ within organs, on part of the lines; also absent: SOX2, FREM2, PTH2R; maybe low, not absent |
| [[ENTREP2]] | B | NELL2 activity raises ENTREP2's level | lines that do not express NELL2 (28) vs lines expressing it (22) | 2.20× lower at baseline in the lines without NELL2 | 0.062 | ⚠ within organs, on part of the lines; also absent: SOX2, FREM2, PTH2R; maybe low, not absent |
| [[ADAMTS19]] | B | NELL2 activity raises ADAMTS19's level | lines that do not express NELL2 (28) vs lines expressing it (22) | 1.69× lower at baseline in the lines without NELL2 | 0.064 | ⚠ within organs, on part of the lines; also absent: SOX2, FREM2, PTH2R; maybe low, not absent |
| [[ELAPOR2]] | B | NELL2 activity raises ELAPOR2's level | lines that do not express NELL2 (28) vs lines expressing it (22) | 2.94× lower at baseline in the lines without NELL2 | 0.074 | ⚠ within organs, on part of the lines; also absent: SOX2, FREM2, PTH2R; maybe low, not absent |
| [[IGFL4]] | B | NELL2 activity raises IGFL4's level | lines that do not express NELL2 (28) vs lines expressing it (22) | 1.44× lower at baseline in the lines without NELL2 | 0.093 | ⚠ within organs, on part of the lines; also absent: SOX2, FREM2, PTH2R; maybe low, not absent |
| [[BMP5]] | C | NELL2 activity raises BMP5's level | lines that do not express NELL2 (28) vs lines expressing it (22) | 3.01× lower at baseline in the lines without NELL2 | 0.009 | ⚠ within organs, on part of the lines; also absent: SOX2, FREM2, PTH2R; maybe low, not absent; co-absent with the target |
| [[RIMBP2]] | C | NELL2 activity raises RIMBP2's level | lines that do not express NELL2 (28) vs lines expressing it (22) | 2.65× lower at baseline in the lines without NELL2 | 0.012 | ⚠ within organs, on part of the lines; also absent: SOX2, FREM2, PTH2R; maybe low, not absent; co-absent with the target |
| [[CTNNA2]] | C | NELL2 activity raises CTNNA2's level | lines that do not express NELL2 (28) vs lines expressing it (22) | 3.40× lower at baseline in the lines without NELL2 | 0.031 | ⚠ within organs, on part of the lines; also absent: SOX2, FREM2, PTH2R; maybe low, not absent; co-absent with the target |
| [[HS3ST5]] | C | NELL2 activity raises HS3ST5's level | lines that do not express NELL2 (28) vs lines expressing it (22) | 2.04× lower at baseline in the lines without NELL2 | 0.065 | ⚠ within organs, on part of the lines; also absent: SOX2, FREM2, PTH2R; maybe low, not absent; co-absent with the target |
| [[GABRG2]] | C | NELL2 activity raises GABRG2's level | lines that do not express NELL2 (28) vs lines expressing it (22) | 2.10× lower at baseline in the lines without NELL2 | 0.076 | ⚠ within organs, on part of the lines; also absent: SOX2, FREM2, PTH2R; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.604). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (36.3, 35.4); signed map (42.9, 36.4). **Vector** length 45.3, 9.59% of its response variance represented; |z| ≥ 3 in 498 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.5 | +23.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.1 | +13.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.8 | +12.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.3 | +15.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +6.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.7 | +2.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.5 | +5.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +3.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.3 | +1.8 |
| fall | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.6 | -2.3 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.4 | -2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -0.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.2 | -1.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -0.6 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | -1.1 | -1.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.0 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | neural EGFL like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q12 — chr12:44,508,275-44,921,848 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NRP2 |
| Reactome | 4 pathways, smallest: Regulation of commissural axon pathfinding by SLIT and ROBO; Signaling by ROBO receptors; Axon guidance |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99435](https://www.uniprot.org/uniprotkb/Q99435) (Protein kinase C-binding protein NELL2):

> Plays multiple roles in neural tissues, regulates neuronal proliferation, survival, differentiation, polarization, as well as axon guidance and synaptic functions. Plays an important role in axon development during neuronal differentiation through the MAPK intracellular signaling pathway (By similarity). Via binding to its receptor ROBO3, plays a role in axon guidance, functioning as a repulsive axon guidance cue that contributes to commissural axon guidance to the midline. Required for neuron …

**Summary**, from NCBI Gene [4753](https://www.ncbi.nlm.nih.gov/gene/4753):

> The protein encoded by this gene is a glycoprotein containing several von Willebrand factor C domains and epidermal growth factor (EGF)-like domains. The encoded protein acts as a homotrimer and is found in the cytoplasm. Several variants encoding a few different isoforms exist, and at least one isoform appears to be a secreted protein. Studies in mouse suggest that this protein plays a role in neural cell growth and differentiation as well as in oncogenesis. [provided by RefSeq, Feb 2009]

**Accessions** — [HGNC:7751](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7751) · Entrez [4753](https://www.ncbi.nlm.nih.gov/gene/4753) · UniProt [Q99435](https://www.uniprot.org/uniprotkb/Q99435) · Ensembl [ENSG00000184613](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184613)

## Data

Gene col 11558: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11558); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11558, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11558]; `tensor/DDL_lfc|DDL_z.npy` [11558]; `embed/gene_vectors.npy` [11558]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11558 or target_col == 11558). Every well: [[NELL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NELL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
