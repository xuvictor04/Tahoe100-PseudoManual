---
symbol: "FAM230C"
type: "gene"
col: 15938
ensembl_id: "ENSG00000279516"
name: "family with sequence similarity 230 member C"
location: "13q11"
module: 177
arm: "+"
pooled_cpm: 7.74
n_lines_expressing: 22
n_dd_up: 19
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 7
direction_downstream: 16
tags: ["gene", "module/177"]
generated_by: "tahoemap"
---

# FAM230C

*family with sequence similarity 230 member C* — 13q11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.62× (z +12.4, q 2e-32, up in 0 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[XRK3F2 (drug)]] 0.5 µM: 1.68× (z +4.9, q 9e-05, up in 1 of 13 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (SNU-423 0.0546×, A-172 0.177×, SK-MEL-2 0.212×, HS-578T 0.161×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (A-172 0.168×, RPMI-7951 0.137×, SNU-423 0.203×; ⚠ toxic; transcription drop); [[Docetaxel (drug)]] 0.05 µM in 2 lines (RPMI-7951 0.252×, HS-578T 0.232×; ⚠ transcription drop; cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (84 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 16 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02335]] (+0.76, fdr 1e-05), [[UTY]] (+0.69, fdr 7e-06), [[BAGE2]] (+0.68, fdr 4e-05).
> It is in [[Module 177]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[LINC00470]] → it (grade C ⚠); 16 go from it, the strongest it → [[LINC01807]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15938.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.62×** | +12.4 | 2e-32 | 0/10 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.95×** | +8.9 | 2e-16 | 0/10 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.97×** | +8.3 | 1e-14 | 0/10 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +5.3 | 1e-05 | 2/14 (NCI-H661, NCI-H1792) | top dose only | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.68×** | +4.9 | 9e-05 | 1/13 (NCI-H1792) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.82×** | +4.2 | 0.003 | 2/9 (NCI-H1792, A549) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.24×** | +4.0 | 0.005 | 5/19 (NCI-H1792, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.38×** | +3.9 | 0.006 | 2/16 (SHP-77, RPMI-7951) | inconsistent across doses |  |
| [[Cepharanthine (drug)]] 5 µM |  | **1.21×** | +3.7 | 0.016 | 6/19 (HS-578T, NCI-H1573, …) | top dose only |  |
| [[Megestrol (drug)]] 0.5 µM |  | **1.29×** | +3.4 | 0.036 | 1/17 (SW 1271) | two highest doses |  |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | **1.28×** | +3.3 | 0.052 | 2/15 (HEC-1-A, HS-578T) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.27×** | +3.2 | 0.066 | 0/17 | inconsistent across doses |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.40×** | +3.2 | 0.066 | 0/11 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Menadione (drug)]] 0.05 µM |  | **1.28×** | +3.1 | 0.090 | 0/16 | inconsistent across doses |  |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **1.25×** | +3.0 | 0.094 | 0/19 | inconsistent across doses |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.26×** | +3.0 | 0.094 | 2/17 (NCI-H1573, A549) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.26×** | +3.0 | 0.094 | 1/17 (SHP-77) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15938.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (SNU-423 0.0546×, A-172 0.177×, SK-MEL-2 0.212×, HS-578T 0.161×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (A-172 0.168×, RPMI-7951 0.137×, SNU-423 0.203×; ⚠ toxic; transcription drop); [[Docetaxel (drug)]] 0.05 µM in 2 lines (RPMI-7951 0.252×, HS-578T 0.232×; ⚠ transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 0.779× | -3.3 | 0.28 | 4/19 (A549, SNU-423, …) | top dose only | position effect removed |
| [[Almonertinib (mesylate) (drug)]] 0.5 µM |  | 0.781× | -3.3 | 0.28 | 1/20 (AN3 CA) | inconsistent across doses |  |
| [[OTS514 (drug)]] 0.05 µM | ⚠ transcription drop | 0.778× | -3.2 | 0.29 | 2/16 (SW 1271, SHP-77) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15938. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RPMI-7951 (line)]] | alt | 39.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.137× (z -13.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 55.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.168× (z -15.0) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 21.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.161× (z -11.1) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 18.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0546× (z -17.4) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 57.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.212× (z -11.8) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 69.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.231× (z -9.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.510 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 31.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.666 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.539 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.676 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.543 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.90 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.613 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.77 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.668 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.665 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.588 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.807 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.22 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.543 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.696 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.732 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.652 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.505 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.733 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.488 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.630 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.516 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.674 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.01 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.707 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.636 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15938), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 16 of them with an alert (⚠; 16 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02335]] | +0.76 | +0.50 / +0.86 | both halves | 1e-05 | **novel candidate** |
| [[UTY]] | +0.69 | +0.68 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[BAGE2]] | +0.68 | +0.42 / +0.74 | both halves | 4e-05 |  |
| [[TPTE]] | +0.67 | +0.51 / +0.71 | both halves | 1e-05 | **novel candidate** |
| [[LINC02476]] | +0.65 | +0.41 / +0.77 | both halves | 4e-05 | **novel candidate** |
| [[LINC02055]] | +0.62 | +0.41 / +0.67 | both halves | 4e-05 | **novel candidate** |
| [[LINC02506]] | +0.61 | +0.01 / +0.67 | ⚠ one half (not replicated) | 0.008 |  |
| [[LINC01518]] | +0.60 | +0.18 / +0.77 | ⚠ one half (not replicated) | 9e-04 |  |
| [[KDM5D]] | +0.59 | +0.40 / +0.61 | both halves | 5e-05 |  |
| [[LINC01320]] | +0.59 | +0.30 / +0.62 | both halves | 2e-04 |  |
| [[LINC00470]] | +0.57 | +0.40 / +0.61 | both halves | 5e-05 |  |
| [[NAA11]] | +0.56 | +0.29 / +0.57 | both halves | 2e-04 |  |
| [[MSR1]] | +0.56 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[LINC01446]] | +0.55 | +0.23 / +0.73 | both halves | 5e-04 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 0, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00470]] | C | LINC00470 activity raises FAM230C's level | lines that do not express LINC00470 (38) vs lines expressing it (12) | 4.33× lower at baseline in the lines without LINC00470 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02566, ENSG00000287474, FCRLA; co-absent with the target |
| [[LINC00648]] | C | LINC00648 activity raises FAM230C's level | lines that do not express LINC00648 (35) vs lines expressing it (15) | 4.14× lower at baseline in the lines without LINC00648 | 0.028 | ⚠ within organs, on part of the lines; also absent: LINC00470, ANKRD20A8P, ZIC1; co-absent with the target |
| [[LINC01098]] | C | LINC01098 activity raises FAM230C's level | lines that do not express LINC01098 (36) vs lines expressing it (14) | 3.50× lower at baseline in the lines without LINC01098 | 0.050 | ⚠ within organs, on part of the lines; also absent: LINC02109, GREM1, ENSG00000288098; maybe low, not absent; co-absent with the target |
| [[LINC01446]] | C | LINC01446 activity raises FAM230C's level | lines that do not express LINC01446 (34) vs lines expressing it (16) | 5.00× lower at baseline in the lines without LINC01446 | 0.073 | ⚠ within organs, on part of the lines; also absent: GABRG2, BAGE2, ENSG00000253363; co-absent with the target |
| [[LINC01518]] | C | LINC01518 activity raises FAM230C's level | lines that do not express LINC01518 (36) vs lines expressing it (14) | 3.14× lower at baseline in the lines without LINC01518 | 0.084 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000285822, CCDC144NL-AS1, PHF2P2; co-absent with the target |
| [[LINC02109]] | C | LINC02109 activity raises FAM230C's level | lines that do not express LINC02109 (40) vs lines expressing it (10) | 3.68× lower at baseline in the lines without LINC02109 | 0.095 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000287474, ENSG00000253642, LINC00879; co-absent with the target |
| [[LINC02438]] | C | LINC02438 activity raises FAM230C's level | lines that do not express LINC02438 (36) vs lines expressing it (14) | 4.32× lower at baseline in the lines without LINC02438 | 0.096 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000248515, MSR1, FSTL5; co-absent with the target |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 1, C 15. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01807]] | B | FAM230C activity raises LINC01807's level | lines that do not express FAM230C (28) vs lines expressing it (22) | 2.16× lower at baseline in the lines without FAM230C | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000277693, LINC01446, LINC01266 |
| [[LINC00470]] | C | FAM230C activity raises LINC00470's level | lines that do not express FAM230C (28) vs lines expressing it (22) | 3.74× lower at baseline in the lines without FAM230C | 0.016 | ⚠ within organs, on part of the lines; also absent: ENSG00000277693, LINC01446, LINC01266; co-absent with the target |
| [[CDH12]] | C | FAM230C activity raises CDH12's level | lines that do not express FAM230C (28) vs lines expressing it (22) | 3.36× lower at baseline in the lines without FAM230C | 0.028 | ⚠ within organs, on part of the lines; also absent: ENSG00000277693, LINC01446, LINC01266; co-absent with the target |
| [[LINC01446]] | C | FAM230C activity raises LINC01446's level | lines that do not express FAM230C (28) vs lines expressing it (22) | 4.98× lower at baseline in the lines without FAM230C | 0.032 | ⚠ within organs, on part of the lines; also absent: ENSG00000277693, LINC01446, LINC01266; co-absent with the target |
| [[LINC02438]] | C | FAM230C activity raises LINC02438's level | lines that do not express FAM230C (28) vs lines expressing it (22) | 4.18× lower at baseline in the lines without FAM230C | 0.033 | ⚠ within organs, on part of the lines; also absent: ENSG00000277693, LINC01446, LINC01266; co-absent with the target |
| [[KC6]] | C | FAM230C activity raises KC6's level | lines that do not express FAM230C (28) vs lines expressing it (22) | 3.34× lower at baseline in the lines without FAM230C | 0.038 | ⚠ within organs, on part of the lines; also absent: ENSG00000277693, LINC01446, LINC01266; co-absent with the target |
| [[TPTE]] | C | FAM230C activity raises TPTE's level | lines that do not express FAM230C (28) vs lines expressing it (22) | 4.58× lower at baseline in the lines without FAM230C | 0.040 | ⚠ within organs, on part of the lines; also absent: ENSG00000277693, LINC01446, LINC01266; co-absent with the target |
| [[MAGEA3-DT]] | C | FAM230C activity raises MAGEA3-DT's level | lines that do not express FAM230C (28) vs lines expressing it (22) | 3.35× lower at baseline in the lines without FAM230C | 0.050 | ⚠ within organs, on part of the lines; also absent: ENSG00000277693, LINC01446, LINC01266; co-absent with the target |
| [[BAGE2]] | C | FAM230C activity raises BAGE2's level | lines that do not express FAM230C (28) vs lines expressing it (22) | 3.44× lower at baseline in the lines without FAM230C | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000277693, LINC01446, LINC01266; co-absent with the target |
| [[FRG1FP]] | C | FAM230C activity raises FRG1FP's level | lines that do not express FAM230C (28) vs lines expressing it (22) | 2.38× lower at baseline in the lines without FAM230C | 0.062 | ⚠ within organs, on part of the lines; also absent: ENSG00000277693, LINC01446, LINC01266; co-absent with the target |
| [[LINC02506]] | C | FAM230C activity raises LINC02506's level | lines that do not express FAM230C (28) vs lines expressing it (22) | 4.09× lower at baseline in the lines without FAM230C | 0.063 | ⚠ within organs, on part of the lines; also absent: ENSG00000277693, LINC01446, LINC01266; co-absent with the target |
| [[LINC00648]] | C | FAM230C activity raises LINC00648's level | lines that do not express FAM230C (28) vs lines expressing it (22) | 3.06× lower at baseline in the lines without FAM230C | 0.067 | ⚠ within organs, on part of the lines; also absent: ENSG00000277693, LINC01446, LINC01266; co-absent with the target |

## Where it sits

- **Module**: [[Module 177]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.813). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (43.3, 27.5); signed map (34.9, 37.9). **Vector** length 23.1, 3.24% of its response variance represented; |z| ≥ 3 in 316 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.2 | +8.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.0 | +12.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.7 | +8.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.1 | +2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +0.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.2 | +1.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +4.9 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +0.9 | +2.4 |
| fall | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -1.2 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.9 | -3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.9 | -1.9 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.9 | -1.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.8 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 230 member C |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 13q11 — chr13:18,195,297-18,232,024 (+) |
| Ensembl biotype | lncRNA |
| Also known as | DKFZP434B061; previously NCRNA00281, LINC00281 |
| Gene groups (HGNC) | Family with sequence similarity 230; Long non-coding RNAs with FAM root symbol |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:24482](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24482) · Entrez [26080](https://www.ncbi.nlm.nih.gov/gene/26080) · Ensembl [ENSG00000279516](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000279516)

## Data

Gene col 15938: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15938); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15938, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15938]; `tensor/DDL_lfc|DDL_z.npy` [15938]; `embed/gene_vectors.npy` [15938]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15938 or target_col == 15938). Every well: [[FAM230C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM230C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
