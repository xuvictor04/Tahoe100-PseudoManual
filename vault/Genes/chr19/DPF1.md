---
symbol: "DPF1"
type: "gene"
col: 235
ensembl_id: "ENSG00000011332"
name: "double PHD fingers 1"
location: "19q13.2"
module: 15
arm: "-"
pooled_cpm: 2.25
n_lines_expressing: 46
n_dd_up: 24
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 8
direction_downstream: 3
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# DPF1

*double PHD fingers 1* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (12 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 11.8× (z +17.8, q 0e+00, up in 41 of 41 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 3.03× (z +11.3, q 2e-27, up in 21 of 27 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Lonafarnib (drug)]] 0.5 µM in 1 line (SW 1271 0.158×).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[XKR7]] (+0.60, fdr 1e-05), [[KCNN4]] (+0.58, fdr 4e-05), [[MAP1S]] (+0.58, fdr 2e-05); moves opposite to [[MKRN5P]] (-0.62, fdr 2e-05), [[CSDE1]] (-0.62, fdr 3e-05), [[SAP30L-AS1]] (-0.58, fdr 3e-05).
> It sits in the **-** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[BCL11B]] → it (grade B ⚠); 3 go from it, the strongest it → [[RBM3]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 235.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **11.8×** | +17.8 | 0e+00 | 41/41 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **10.8×** | +17.2 | 0e+00 | 40/40 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **9.45×** | +16.2 | 0e+00 | 38/39 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.03×** | +11.3 | 2e-27 | 21/27 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **4.23×** | +10.0 | 2e-21 | 33/38 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **3.66×** | +9.4 | 7e-19 | 19/22 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.41×** | +8.8 | 8e-17 | 36/41 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **3.37×** | +8.4 | 2e-15 | 8/10 (SW480, SHP-77, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change | **2.64×** | +6.7 | 1e-09 | 0/3 | all doses, stronger at high dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.53×** | +6.7 | 1e-09 | 17/25 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change | **2.46×** | +6.5 | 4e-09 | 7/13 (PANC-1, A498, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.20×** | +5.7 | 7e-07 | 17/41 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change | **2.18×** | +5.2 | 9e-06 | 2/4 (PANC-1, SHP-77) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.98×** | +4.9 | 4e-05 | 13/33 (HOP62, SW 900, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.92×** | +4.7 | 1e-04 | 14/42 (A498, Hs 766T, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.52×** | +4.2 | 7e-04 | 12/41 (PANC-1, SW480, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.84×** | +3.9 | 0.003 | 6/34 (PANC-1, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.43×** | +3.6 | 0.009 | 5/40 (PANC-1, SHP-77, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.58×** | +3.1 | 0.061 | 4/19 (A549, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.95×** | +2.9 | 0.092 | 0/30 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 235.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Lonafarnib (drug)]] 0.5 µM in 1 line (SW 1271 0.158×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[GSK1059615 (drug)]] 5 µM |  | 0.439× | -3.1 | 0.55 | 9/33 (A-172, SHP-77, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +1.18 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 235. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 2.40 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.2× (z +12.2) | — |
| [[SW480 (line)]] | alt | 3.22 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 11.5× (z +9.6) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[A549 (line)]] | wt | 2.86 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.6× (z +9.1) ⚠ cell-cycle shift, explains ~64% of this change | — |
| [[SW 1271 (line)]] | alt | 2.16 | 0 | 1 | — | [[Lonafarnib (drug)]] 0.5 µM 0.158× (z -15.9) |
| [[A-172 (line)]] | wt | 4.64 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.38 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.01 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.441 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.61 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.386 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.840 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.631 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.469 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.669 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.69 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.384 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.609 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.983 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.72 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.663 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.902 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.48 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 235), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 5 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[XKR7]] | +0.60 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[KCNN4]] | +0.58 | +0.41 / +0.45 | both halves | 4e-05 | STRING 424 |
| [[MAP1S]] | +0.58 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[ST3GAL5]] | +0.57 | +0.35 / +0.57 | both halves | 1e-04 |  |
| [[RAB39A]] | +0.56 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[HIVEP3]] | +0.55 | +0.43 / +0.50 | both halves | 3e-05 | same gene group |
| [[PLAUR]] | +0.55 | +0.45 / +0.28 | both halves | 3e-04 |  |
| [[POLR3K]] | +0.54 | +0.26 / +0.52 | both halves | 4e-04 |  |
| [[SLC9A7]] | +0.53 | +0.38 / +0.38 | both halves | 7e-05 |  |
| [[GALE]] | +0.53 | +0.44 / +0.43 | both halves | 3e-05 |  |
| [[SNRNP25]] | +0.52 | +0.15 / +0.46 | ⚠ not reproduced | 0.001 |  |
| [[RAC2]] | +0.52 | +0.32 / +0.38 | both halves | 2e-04 |  |
| [[RIN1]] | +0.52 | +0.37 / +0.42 | both halves | 9e-05 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MKRN5P]] | -0.62 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[CSDE1]] | -0.62 | -0.43 / -0.65 | both halves | 3e-05 |  |
| [[SAP30L-AS1]] | -0.58 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[SEC24B-AS1]] | -0.58 | -0.38 / -0.42 | both halves | 6e-05 |  |
| [[ZNF460-AS1]] | -0.58 | -0.42 / -0.38 | both halves | 7e-05 |  |
| [[LAMTOR5-AS1]] | -0.56 | -0.34 / -0.38 | both halves | 1e-04 |  |
| [[NUDT13]] | -0.55 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[CLNS1A]] | -0.55 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[DPY19L2P3]] | -0.55 | -0.51 / -0.37 | both halves | 8e-05 |  |
| [[RBM3]] | -0.54 | -0.30 / -0.46 | both halves | 2e-04 |  |
| [[NAF1]] | -0.54 | -0.49 / -0.39 | both halves | 5e-05 |  |
| [[EPM2A]] | -0.54 | -0.33 / -0.29 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BCL11B]] | B | BCL11B activity lowers DPF1's level | lines that do not express BCL11B (18) vs lines expressing it (32) | 1.75× higher at baseline in the lines without BCL11B | 0.006 | ⚠ within organs, on part of the lines; also absent: ENSG00000249111, HLA-V-1, ENSG00000272297; maybe low, not absent |
| [[SIGIRR]] | B | SIGIRR activity lowers DPF1's level | lines that do not express SIGIRR (9) vs lines expressing it (41) | 2.33× higher at baseline in the lines without SIGIRR | 0.013 | ⚠ within organs, on part of the lines; also absent: CLCF1, LTBR, MYOF |
| [[FSD1]] | B | FSD1 activity raises DPF1's level | lines that do not express FSD1 (17) vs lines expressing it (33) | 1.77× lower at baseline in the lines without FSD1 | 0.015 | ⚠ within organs, on part of the lines; also absent: RFLNB, B4GALNT1, NTNG2 |
| [[KLRD1]] | B | KLRD1 activity lowers DPF1's level | lines that do not express KLRD1 (8) vs lines expressing it (42) | 1.46× higher at baseline in the lines without KLRD1 | 0.018 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TMEM92]] | B | TMEM92 activity lowers DPF1's level | lines that do not express TMEM92 (22) vs lines expressing it (28) | 1.59× higher at baseline in the lines without TMEM92 | 0.024 | ⚠ within organs, on part of the lines; also absent: ARL14, LINC01589, TNFSF10 |
| [[RAB39A]] | B | RAB39A activity strengthens DPF1's drug response | lines that do not express RAB39A (16) vs lines expressing it (26) | the lines without RAB39A respond 0.82× as strongly (z diff +0.97); strongest at Homoharringtonine 5 µM: 1.91x vs 4.30x (z diff +3.3) | 0.088 | ⚠ within organs, on part of the lines; also absent: RBM20, NOVA2, SDK2; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[ATP1A3]] | B | ATP1A3 activity raises DPF1's level | lines that do not express ATP1A3 (12) vs lines expressing it (38) | 1.54× lower at baseline in the lines without ATP1A3 | 0.094 | ⚠ within organs, on part of the lines; also absent: KIF26A; maybe low, not absent |
| [[ADRA1B]] | B | ADRA1B activity lowers DPF1's level | lines that do not express ADRA1B (24) vs lines expressing it (26) | 1.21× higher at baseline in the lines without ADRA1B | 0.099 | ⚠ within organs, on part of the lines; also absent: IL31RA, IGFBP3, STAC |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RBM3]] | C | DPF1 activity raises RBM3's level | lines that do not express DPF1 (4) vs lines expressing it (46) | 1.19× lower at baseline in the lines without DPF1 | 0.064 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; co-occurs with CTNNB1; also absent: ASAP3, CCDC102A, TPST1 |
| [[ACYP2]] | C | DPF1 activity raises ACYP2's level | lines that do not express DPF1 (4) vs lines expressing it (46) | 1.37× lower at baseline in the lines without DPF1 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; co-occurs with CTNNB1; also absent: ASAP3, CCDC102A, TPST1; its own permutation p |
| cells under [[Lapatinib ditosylate (drug)]] 0.5 µM | C | DPF1's natural level lowers the cells' numbers under Lapatinib ditosylate 0.5 µM (makes them more sensitive) | DPF1's natural level across 44 lines (lineage-adjusted; a glimpse) | r -0.71 | 0.291 over the table, 0.024 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **-** arm (projection on the module's main direction -0.539). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-1.9, 23.6); signed map (-2.2, 52.6). **Vector** length 55.5, 9.34% of its response variance represented; |z| ≥ 3 in 942 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +4.0 | +10.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +3.5 | +16.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +3.5 | +17.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +3.4 | +17.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.6 | +11.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +4.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.4 | +3.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.3 | +1.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.2 | +4.9 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.0 | -2.4 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -3.0 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.6 | -2.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.6 | -0.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | +1.4 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.5 | -2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.4 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | double PHD fingers 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:38,211,006-38,229,714 (-) |
| Ensembl biotype | protein_coding |
| Also known as | neuro-d4, NEUD4, BAF45b, SMARCG1 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; PHD finger proteins; BAF complex subunits |
| Reactome | 15 pathways, smallest: Formation of the canonical BAF (cBAF) complex; Formation of neuronal progenitor and neuronal BAF (npBAF and nBAF); SWI/SNF chromatin remodelers |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92782](https://www.uniprot.org/uniprotkb/Q92782) (Zinc finger protein neuro-d4):

> May have an important role in developing neurons by participating in regulation of cell survival, possibly as a neurospecific transcription factor. Belongs to the neuron-specific chromatin remodeling complex (nBAF complex). During neural development a switch from a stem/progenitor to a postmitotic chromatin remodeling mechanism occurs as neurons exit the cell cycle and become committed to their adult state. The transition from proliferating neural stem/progenitor cells to postmitotic neurons …

**Summary**, from NCBI Gene [8193](https://www.ncbi.nlm.nih.gov/gene/8193):

> Enables sequence-specific double-stranded DNA binding activity. Predicted to be involved in nervous system development and regulation of DNA-templated transcription. Predicted to be located in chromatin and nucleoplasm. Predicted to be part of nBAF complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20225](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20225) · Entrez [8193](https://www.ncbi.nlm.nih.gov/gene/8193) · UniProt [Q92782](https://www.uniprot.org/uniprotkb/Q92782) · Ensembl [ENSG00000011332](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000011332)

## Data

Gene col 235: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 235); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 235, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 235]; `tensor/DDL_lfc|DDL_z.npy` [235]; `embed/gene_vectors.npy` [235]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 235 or target_col == 235). Every well: [[DPF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DPF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
