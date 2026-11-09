---
symbol: "HOXA11"
type: "gene"
col: 65
ensembl_id: "ENSG00000005073"
name: "homeobox A11"
location: "7p15.2"
module: 201
arm: "+"
pooled_cpm: 4.72
n_lines_expressing: 21
n_dd_up: 11
n_dd_down: 0
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 5
tags: ["gene", "module/201"]
generated_by: "tahoemap"
---

# HOXA11

*homeobox A11* — 7p15.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.72× (z +13.3, q 1e-37, up in 15 of 17 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (HT-29 0.124×, A498 0.166×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (HT-29 0.160×, A498 0.251×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (A498 0.165×, HT-29 0.173×; ⚠ toxic; transcription drop); [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM in 1 line (HOP62 0.0617×); [[Orlistat (drug)]] 0.05 µM in 1 line (SW1417 0.0579×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HOXA10]] (+0.71, fdr 7e-06, ⚠ same locus), [[HOXA9]] (+0.68, fdr 7e-06, ⚠ same locus), [[HOXA5]] (+0.62, fdr 7e-06, ⚠ same locus), [[PURA]] (+0.58, fdr 1e-05), [[RNF113A]] (+0.57, fdr 3e-05), [[ING2]] (+0.52, fdr 9e-05); moves opposite to [[ADAMTSL5]] (-0.57, fdr 3e-05), [[ACTN4]] (-0.53, fdr 2e-04), [[CDC42]] (-0.51, fdr 1e-04).
> It is in [[Module 201]], a single-armed module (Kidney development).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[HOXA3]] → it (grade B ⚠); 5 go from it, the strongest it → [[HOXA3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 8 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 65.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.72×** | +13.3 | 1e-37 | 15/17 (A498, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.28×** | +8.2 | 8e-14 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.68×** | +6.8 | 2e-09 | 12/14 (KATO III, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.09×** | +5.3 | 2e-05 | 1/12 (SW 900) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.68×** | +5.3 | 2e-05 | 2/19 (LS 180, RKO) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.06×** | +4.8 | 2e-04 | 1/11 (LS 180) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.84×** | +4.4 | 0.001 | 7/17 (LS 180, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.78×** | +4.1 | 0.002 | 15/18 (LS 180, LoVo, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.22×** | +3.6 | 0.020 | 1/11 (HOP62) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **1.60×** | +3.4 | 0.039 | 4/15 (SW480, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.57×** | +3.3 | 0.057 | 3/16 (LS 180, SW480, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | 1.55× | +3.0 | 0.12 | 7/17 (LS 180, LoVo, …) | all doses, flat | composition shift |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (HT-29 0.124×, A498 0.166×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (HT-29 0.160×, A498 0.251×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (A498 0.165×, HT-29 0.173×; ⚠ toxic; transcription drop); [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM in 1 line (HOP62 0.0617×); [[Orlistat (drug)]] 0.05 µM in 1 line (SW1417 0.0579×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 65. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 19.9 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.14× (z +13.9) | [[Dinaciclib (drug)]] 0.5 µM 0.166× (z -12.3) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 45.8 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.124× (z -13.7) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 14.3 | 4 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 6.97× (z +10.2) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 6.14× (z +9.9) | — |
| [[NCI-H460 (line)]] | wt | 3.73 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -11.1) ⚠ cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 5.92 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.88× (z +8.8) | [[Orlistat (drug)]] 0.05 µM 0.0579× (z -10.3) |
| [[HOP62 (line)]] | alt | 3.53 | 0 | 1 | — | [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM 0.0617× (z -10.3) |
| [[LoVo (line)]] | wt | 12.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.31× (z +8.5) | — |
| [[SW480 (line)]] | alt | 5.84 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.64× (z +9.4) | — |
| [[A-172 (line)]] | wt | 0.613 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.315 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.309 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.392 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.428 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.506 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.579 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.460 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.575 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.474 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.500 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.454 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.668 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.811 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.848 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.341 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.281 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.271 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.978 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.684 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.781 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.41 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.837 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.266 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.420 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.341 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.913 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.793 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.453 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.77 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 65), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 7 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 5 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HOXA10]] | +0.71 | +0.59 / +0.71 | both halves | 7e-06 | same gene group; STRING 866; ⚠ same locus (0.9 kb, same strand: neighbours can correlate without regulation) |
| [[HOXA9]] | +0.68 | +0.67 / +0.67 | both halves | 7e-06 | same gene group; STRING 633; ⚠ same locus (6.0 kb, same strand: neighbours can correlate without regulation) |
| [[HOXA5]] | +0.62 | +0.58 / +0.60 | both halves | 7e-06 | same gene group; STRING 513; ⚠ same locus (37.5 kb, same strand: neighbours can correlate without regulation) |
| [[HOXA6]] | +0.62 | +0.57 / +0.57 | both halves | 1e-05 | same gene group; pathway: Kidney development; STRING 523; ⚠ same locus (30.6 kb, same strand: neighbours can correlate without regulation) |
| [[PURA]] | +0.58 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[RNF113A]] | +0.57 | +0.46 / +0.63 | both halves | 3e-05 |  |
| [[ING2]] | +0.52 | +0.36 / +0.57 | both halves | 9e-05 |  |
| [[FUT11]] | +0.52 | +0.31 / +0.60 | both halves | 2e-04 |  |
| [[ALG2]] | +0.51 | +0.38 / +0.59 | both halves | 7e-05 |  |
| [[HOXA10-AS]] | +0.51 | +0.46 / +0.47 | both halves | 2e-05 | ⚠ same locus (9.2 kb: neighbours can correlate without regulation) |
| [[TNFRSF10C]] | +0.51 | +0.24 / +0.59 | both halves | 5e-04 |  |
| [[COG1]] | +0.51 | +0.39 / +0.48 | both halves | 5e-05 |  |
| [[RSBN1]] | +0.51 | +0.38 / +0.46 | both halves | 6e-05 |  |
| [[TGDS]] | +0.50 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[TXNL4B]] | +0.49 | +0.33 / +0.48 | both halves | 1e-04 |  |
| [[RUNDC1]] | +0.49 | +0.48 / +0.42 | both halves | 4e-05 |  |
| [[ZIC2]] | +0.49 | +0.39 / +0.52 | both halves | 5e-05 | STRING 472 |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAMTSL5]] | -0.57 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[ACTN4]] | -0.53 | -0.31 / -0.55 | both halves | 2e-04 |  |
| [[CDC42]] | -0.51 | -0.33 / -0.53 | both halves | 1e-04 |  |
| [[GNB1]] | -0.49 | -0.31 / -0.44 | both halves | 2e-04 |  |
| [[PABIR2]] | -0.49 | -0.30 / -0.55 | both halves | 2e-04 |  |
| [[DIAPH1]] | -0.47 | -0.35 / -0.46 | both halves | 1e-04 |  |
| [[YWHAQ]] | -0.47 | -0.29 / -0.55 | both halves | 3e-04 |  |
| [[DNAJB6]] | -0.46 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[ACTR3]] | -0.46 | -0.34 / -0.46 | both halves | 1e-04 |  |
| [[CAPZB]] | -0.46 | -0.33 / -0.45 | both halves | 1e-04 |  |
| [[VILL]] | -0.46 | -0.42 / -0.37 | both halves | 8e-05 |  |
| [[ARHGAP23]] | -0.45 | -0.37 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOXA3]] | B | HOXA3 activity raises HOXA11's level | lines that do not express HOXA3 (9) vs lines expressing it (41) | 2.17× lower at baseline in the lines without HOXA3 | 0.068 | ⚠ within organs, on part of the lines; also absent: HOXA5, HOXA6, LINC01186; maybe low, not absent |
| [[MEF2C-AS1]] | B | MEF2C-AS1 activity raises HOXA11's level | lines that do not express MEF2C-AS1 (16) vs lines expressing it (34) | 1.12× lower at baseline in the lines without MEF2C-AS1 | 0.069 | ⚠ within organs, on part of the lines; also absent: MEF2C, RGS2, ADGRL4 |
| [[HOXA9]] | C | HOXA9 activity raises HOXA11's level | lines that do not express HOXA9 (31) vs lines expressing it (19) | 4.19× lower at baseline in the lines without HOXA9 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HOXA11, IGFL2-AS1, GPA33; co-absent with the target |
| [[HOXA10-AS]] | C | HOXA10-AS activity raises HOXA11's level | lines that do not express HOXA10-AS (21) vs lines expressing it (29) | 3.09× lower at baseline in the lines without HOXA10-AS | 0.013 | ⚠ within organs, on part of the lines; also absent: HOXA9, HOXA11, HOXA10; maybe low, not absent; co-absent with the target |
| [[HOXA10]] | C | HOXA10 activity raises HOXA11's level | lines that do not express HOXA10 (20) vs lines expressing it (30) | 2.84× lower at baseline in the lines without HOXA10 | 0.022 | ⚠ within organs, on part of the lines; also absent: HOXA9, HOXA10-AS, HOXA11; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOXA3]] | B | HOXA11 activity raises HOXA3's level | lines that do not express HOXA11 (29) vs lines expressing it (21) | 2.97× lower at baseline in the lines without HOXA11 | 0.022 | ⚠ within organs, on part of the lines; also absent: HOXA9, IL20RA, PRSS3 |
| [[MYNN]] | B | HOXA11 activity lowers MYNN's level | lines that do not express HOXA11 (29) vs lines expressing it (21) | 1.12× higher at baseline in the lines without HOXA11 | 0.038 | ⚠ within organs, on part of the lines; also absent: HOXA9, IL20RA, PRSS3 |
| [[HOXA10]] | C | HOXA11 activity raises HOXA10's level | lines that do not express HOXA11 (29) vs lines expressing it (21) | 4.23× lower at baseline in the lines without HOXA11 | 0.003 | ⚠ within organs, on part of the lines; also absent: HOXA9, IL20RA, PRSS3; co-absent with the target |
| [[HOXA9]] | C | HOXA11 activity raises HOXA9's level | lines that do not express HOXA11 (29) vs lines expressing it (21) | 5.71× lower at baseline in the lines without HOXA11 | 0.016 | ⚠ within organs, on part of the lines; also absent: HOXA9, IL20RA, PRSS3; co-absent with the target |
| [[HOXA10-AS]] | C | HOXA11 activity raises HOXA10-AS's level | lines that do not express HOXA11 (29) vs lines expressing it (21) | 2.48× lower at baseline in the lines without HOXA11 | 0.016 | ⚠ within organs, on part of the lines; also absent: HOXA9, IL20RA, PRSS3; co-absent with the target |

## Where it sits

- **Module**: [[Module 201]] — Kidney development; 15 genes; every member is in the + arm (projection on the module's main direction 0.601). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-2.3, 27.7); signed map (-5.2, 6.5). **Vector** length 43.2, 9.78% of its response variance represented; |z| ≥ 3 in 356 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +13.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.0 | +4.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.4 | +2.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.3 | +2.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +1.2 | +6.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.0 | +1.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +0.9 | -0.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +0.8 | +2.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +0.8 | +2.6 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -2.0 | +5.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -1.9 | +8.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.6 | -0.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.5 | -1.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -2.6 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -1.1 | -0.9 |
|  | [[Rapamycin (drug)]] 5 µM |  | -0.9 | -1.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.9 | -1.2 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -0.9 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | homeobox A11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p15.2 — chr7:27,181,157-27,185,232 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously HOX1I, HOX1 |
| Gene groups (HGNC) | HOXL subclass homeoboxes |
| Reactome | 2 pathways, smallest: Formation of the ureteric bud; Kidney development |
| Matched by | ensembl_id |

**Function**, from UniProt [P31270](https://www.uniprot.org/uniprotkb/P31270) (Homeobox protein Hox-A11):

> Sequence-specific transcription factor which is part of a developmental regulatory system that provides cells with specific positional identities on the anterior-posterior axis.

**Summary**, from NCBI Gene [3207](https://www.ncbi.nlm.nih.gov/gene/3207):

> In vertebrates, the genes encoding the class of transcription factors called homeobox genes are found in clusters named A, B, C, and D on four separate chromosomes. Expression of these proteins is spatially and temporally regulated during embryonic development. This gene is part of the A cluster on chromosome 7 and encodes a DNA-binding transcription factor which may regulate gene expression, morphogenesis, and differentiation. This gene is involved in the regulation of uterine development and …

**Accessions** — [HGNC:5101](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5101) · Entrez [3207](https://www.ncbi.nlm.nih.gov/gene/3207) · UniProt [P31270](https://www.uniprot.org/uniprotkb/P31270) · Ensembl [ENSG00000005073](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000005073)

## Data

Gene col 65: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 65); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 65, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 65]; `tensor/DDL_lfc|DDL_z.npy` [65]; `embed/gene_vectors.npy` [65]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 65 or target_col == 65). Every well: [[HOXA11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HOXA11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
