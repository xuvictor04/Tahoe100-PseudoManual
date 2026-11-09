---
symbol: "PHGR1"
type: "gene"
col: 13884
ensembl_id: "ENSG00000233041"
name: "proline, histidine and glycine rich 1"
location: "15q15.1"
module: 44
arm: "+"
pooled_cpm: 2.85
n_lines_expressing: 7
n_dd_up: 14
n_dd_down: 0
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 34
direction_downstream: 49
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# PHGR1

*proline, histidine and glycine rich 1* — 15q15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 13.3× (z +10.5, q 3e-23, up in 3 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.64× (z +7.4, q 2e-11, up in 1 of 5 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (LS 180 0.134×); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (COLO 205 0.0531×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[REG4]] (+0.82, fdr 7e-06), [[PPP1R1B]] (+0.77, fdr 7e-06), [[LYZ]] (+0.73, fdr 7e-06); moves opposite to [[CTSL]] (-0.43, fdr 2e-04).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 34 arrows point to it, the strongest [[LYZ]] → it (grade C ⚠); 49 go from it, the strongest it → [[RSPH1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 12 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13884.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **13.3×** | +10.5 | 3e-23 | 3/3 (LS 180, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **12.1×** | +9.5 | 6e-19 | 2/2 (LS 180, SW1417) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **7.35×** | +7.5 | 1e-11 | 3/3 (HT-29, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.64×** | +7.4 | 2e-11 | 1/5 (LoVo) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.80×** | +5.4 | 7e-06 | 4/4 (COLO 205, HT-29, …) | top dose only | cell-cycle shift (explains ~19% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **2.43×** | +5.1 | 4e-05 | 2/5 (LoVo, SW1417) | top dose only | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **3.15×** | +4.7 | 3e-04 | 2/5 (SW1417, LS 180) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~24% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **7.72×** | +4.4 | 1e-03 | 0/1 | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.09×** | +4.3 | 0.001 | 2/4 (SW1417, HT-29) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.67×** | +3.7 | 0.011 | 3/5 (LS 180, HT-29, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **4.50×** | +3.5 | 0.023 | 0/4 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.25×** | +3.3 | 0.049 | 1/5 (HT-29) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.76×** | +3.2 | 0.054 | 0/5 | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **2.21×** | +3.2 | 0.055 | 1/5 (SW1417) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13884.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (LS 180 0.134×); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (COLO 205 0.0531×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Erlotinib (drug)]] 0.05 µM |  | 0.375× | -3.7 | 0.10 | 1/5 (LoVo) | inconsistent across doses | position effect removed |
| [[Artesunate (drug)]] 0.5 µM |  | 0.474× | -3.1 | 0.55 | 1/5 (COLO 205) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.58 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13884. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 16.8 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0531× (z -8.5) |
| [[LS 180 (line)]] | wt | 78.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.134× (z -10.6) |
| [[A-172 (line)]] | wt | 0.252 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.201 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.188 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.181 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.517 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.336 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.227 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.240 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.220 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.311 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.307 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.267 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.221 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.273 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.252 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.282 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.212 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.233 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.294 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.197 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.442 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.24 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.370 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.242 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.328 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.185 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.199 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.225 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.272 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.274 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.271 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.219 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.208 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.237 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.218 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.207 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.214 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.253 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.274 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.523 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.239 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.258 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.287 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.282 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13884), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[REG4]] | +0.82 | +0.74 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[PPP1R1B]] | +0.77 | +0.62 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[LYZ]] | +0.73 | +0.59 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[GPA33]] | +0.71 | +0.66 / +0.74 | both halves | 7e-06 |  |
| [[MYB]] | +0.68 | +0.57 / +0.70 | both halves | 1e-05 | **novel candidate** |
| [[TSPAN8]] | +0.68 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[CTSE]] | +0.68 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[CFTR]] | +0.68 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[PLA2G2A]] | +0.67 | +0.58 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[ST6GALNAC1]] | +0.67 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[EPCAM]] | +0.65 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[TFF3]] | +0.64 | +0.48 / +0.73 | both halves | 2e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTSL]] | -0.43 | -0.36 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*34 arrows, 34 of them with an alert ⚠; grade A 0, B 0, C 34. Shown: the 12 strongest; 22 more arrows (22 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LYZ]] | C | LYZ activity raises PHGR1's level | lines that do not express LYZ (40) vs lines expressing it (10) | 3.90× lower at baseline in the lines without LYZ | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCNT3, TRIM31, MUC17; co-absent with the target |
| [[MUC13]] | C | MUC13 activity raises PHGR1's level | lines that do not express MUC13 (40) vs lines expressing it (10) | 4.13× lower at baseline in the lines without MUC13 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, NPSR1, CDH17; co-absent with the target |
| [[CDH17]] | C | CDH17 activity raises PHGR1's level | lines that do not express CDH17 (40) vs lines expressing it (10) | 4.20× lower at baseline in the lines without CDH17 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, MUC13, CLRN3; co-absent with the target |
| [[LGALS4]] | C | LGALS4 activity raises PHGR1's level | lines that do not express LGALS4 (39) vs lines expressing it (11) | 3.65× lower at baseline in the lines without LGALS4 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13; maybe low, not absent; co-absent with the target |
| [[CLRN3]] | C | CLRN3 activity raises PHGR1's level | lines that do not express CLRN3 (40) vs lines expressing it (10) | 4.18× lower at baseline in the lines without CLRN3 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13; co-absent with the target |
| [[GPA33]] | C | GPA33 activity raises PHGR1's level | lines that do not express GPA33 (41) vs lines expressing it (9) | 4.78× lower at baseline in the lines without GPA33 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, NPSR1, CDH17; co-absent with the target |
| [[TFF2]] | C | TFF2 activity raises PHGR1's level | lines that do not express TFF2 (39) vs lines expressing it (11) | 3.03× lower at baseline in the lines without TFF2 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG3, ENSG00000250920, TRIM31; co-absent with the target |
| [[PIGR]] | C | PIGR activity raises PHGR1's level | lines that do not express PIGR (45) vs lines expressing it (5) | 3.10× lower at baseline in the lines without PIGR | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, TM4SF4, APOB; co-absent with the target |
| [[PPP1R1B]] | C | PPP1R1B activity raises PHGR1's level | lines that do not express PPP1R1B (37) vs lines expressing it (13) | 2.97× lower at baseline in the lines without PPP1R1B | 0.027 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CEACAM5, NPSR1, CDH17; co-absent with the target |
| [[MUC6]] | C | MUC6 activity raises PHGR1's level | lines that do not express MUC6 (45) vs lines expressing it (5) | 3.02× lower at baseline in the lines without MUC6 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, ENSG00000230975, APOB; co-absent with the target |
| [[GJB1]] | C | GJB1 activity raises PHGR1's level | lines that do not express GJB1 (38) vs lines expressing it (12) | 3.06× lower at baseline in the lines without GJB1 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53, CDKN2A; also absent: AZGP1, LYZ, ATP10B; co-absent with the target |
| [[LINC01559]] | C | LINC01559 activity raises PHGR1's level | lines that do not express LINC01559 (38) vs lines expressing it (12) | 3.35× lower at baseline in the lines without LINC01559 | 0.040 | ⚠ within organs, on part of the lines; also absent: CLRN3, NPSR1, CDH17; co-absent with the target |

### Downstream of this gene

*49 arrows, 49 of them with an alert ⚠; grade A 0, B 4, C 45. Shown: the 12 strongest; 37 more arrows (37 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RSPH1]] | B | PHGR1 activity raises RSPH1's level | lines that do not express PHGR1 (43) vs lines expressing it (7) | 3.28× lower at baseline in the lines without PHGR1 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FAM3D, GPA33, KRT20 |
| [[CTSH]] | B | PHGR1 activity raises CTSH's level | lines that do not express PHGR1 (43) vs lines expressing it (7) | 2.03× lower at baseline in the lines without PHGR1 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FAM3D, GPA33, KRT20 |
| [[CALML4]] | B | PHGR1 activity raises CALML4's level | lines that do not express PHGR1 (43) vs lines expressing it (7) | 2.25× lower at baseline in the lines without PHGR1 | 0.090 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FAM3D, GPA33, KRT20 |
| [[MANSC1]] | B | PHGR1 activity raises MANSC1's level | lines that do not express PHGR1 (43) vs lines expressing it (7) | 2.83× lower at baseline in the lines without PHGR1 | 0.091 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FAM3D, GPA33, KRT20 |
| [[MUC13]] | C | PHGR1 activity raises MUC13's level | lines that do not express PHGR1 (43) vs lines expressing it (7) | 26.34× lower at baseline in the lines without PHGR1 | 6e-05 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FAM3D, GPA33, KRT20; co-absent with the target |
| [[PRR15L]] | C | PHGR1 activity raises PRR15L's level | lines that do not express PHGR1 (43) vs lines expressing it (7) | 9.18× lower at baseline in the lines without PHGR1 | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FAM3D, GPA33, KRT20; co-absent with the target |
| [[LGALS4]] | C | PHGR1 activity raises LGALS4's level | lines that do not express PHGR1 (43) vs lines expressing it (7) | 10.08× lower at baseline in the lines without PHGR1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FAM3D, GPA33, KRT20; co-absent with the target |
| [[PRR15]] | C | PHGR1 activity raises PRR15's level | lines that do not express PHGR1 (43) vs lines expressing it (7) | 5.82× lower at baseline in the lines without PHGR1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FAM3D, GPA33, KRT20; co-absent with the target |
| [[CDH17]] | C | PHGR1 activity raises CDH17's level | lines that do not express PHGR1 (43) vs lines expressing it (7) | 10.47× lower at baseline in the lines without PHGR1 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FAM3D, GPA33, KRT20; co-absent with the target |
| [[FXYD3]] | C | PHGR1 activity raises FXYD3's level | lines that do not express PHGR1 (43) vs lines expressing it (7) | 7.67× lower at baseline in the lines without PHGR1 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FAM3D, GPA33, KRT20; co-absent with the target |
| [[MUC3A]] | C | PHGR1 activity raises MUC3A's level | lines that do not express PHGR1 (43) vs lines expressing it (7) | 5.60× lower at baseline in the lines without PHGR1 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FAM3D, GPA33, KRT20; co-absent with the target |
| [[TSPAN8]] | C | PHGR1 activity raises TSPAN8's level | lines that do not express PHGR1 (43) vs lines expressing it (7) | 9.97× lower at baseline in the lines without PHGR1 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FAM3D, GPA33, KRT20; co-absent with the target |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.617). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.8, 50.4); signed map (65.4, 5.6). **Vector** length 27.2, 14.4% of its response variance represented; |z| ≥ 3 in 119 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.0 | +9.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.9 | +7.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.7 | +10.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.6 | +7.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +1.6 | +5.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.9 | -0.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | +0.6 | +0.7 |
|  | [[Entrectinib (drug)]] 5 µM |  | +0.6 | +1.2 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +0.6 | +0.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.6 | +2.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -0.9 | -1.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.7 | +0.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.7 | -2.2 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -0.6 | +0.1 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.6 | -1.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -0.6 | +0.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.6 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | proline, histidine and glycine rich 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q15.1 — chr15:40,351,033-40,356,434 (+) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

UniProt [C9JFL3](https://www.uniprot.org/uniprotkb/C9JFL3) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:37226](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:37226) · Entrez [644844](https://www.ncbi.nlm.nih.gov/gene/644844) · UniProt [C9JFL3](https://www.uniprot.org/uniprotkb/C9JFL3) · Ensembl [ENSG00000233041](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000233041)

## Data

Gene col 13884: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13884); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13884, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13884]; `tensor/DDL_lfc|DDL_z.npy` [13884]; `embed/gene_vectors.npy` [13884]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13884 or target_col == 13884). Every well: [[PHGR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PHGR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
