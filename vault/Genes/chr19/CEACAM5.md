---
symbol: "CEACAM5"
type: "gene"
col: 2594
ensembl_id: "ENSG00000105388"
name: "CEA cell adhesion molecule 5"
location: "19q13.2"
module: 8
arm: "+"
pooled_cpm: 82.55
n_lines_expressing: 11
n_dd_up: 7
n_dd_down: 6
n_dd_up_clean: 2
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 97
direction_downstream: 115
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# CEACAM5

*CEA cell adhesion molecule 5* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.10× (z +12.9, q 2e-35, up in 8 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Thymol (drug)]] 5 µM: 1.37× (z +3.5, q 0.045, up in 7 of 9 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H1573 5.29×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.543× (z -6.9, q 4e-09, down in 9 of 9 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CEACAM6]] (+0.89, fdr 7e-06, ⚠ same locus), [[TSPAN1]] (+0.81, fdr 7e-06), [[MUC2]] (+0.77, fdr 7e-06), [[TMEM45B]] (+0.76, fdr 7e-06).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 97 arrows point to it, the strongest [[AQP3]] → it (grade B ⚠); 115 go from it, the strongest it → [[ABHD17C]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2594.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H1573 5.29×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.10×** | +12.9 | 2e-35 | 8/10 (NCI-H1573, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.31×** | +9.1 | 2e-17 | 4/7 (NCI-H1573, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.08×** | +8.3 | 3e-14 | 1/8 (NCI-H1573) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.83×** | +4.8 | 2e-04 | 1/9 (AsPC-1) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.65×** | +4.0 | 0.008 | 0/9 | top dose only | cell-cycle shift (explains ~11% here) |
| [[Thymol (drug)]] 5 µM |  | **1.37×** | +3.5 | 0.045 | 7/9 (KATO III, LS 180, …) | top dose only | position effect removed |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.59×** | +3.4 | 0.060 | 2/9 (AsPC-1, COLO 205) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.32× | +3.1 | 0.14 | 2/9 (LS 180, LoVo) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2594.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.543×** | -6.9 | 4e-09 | 9/9 (KATO III, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.448×** | -6.4 | 5e-08 | 8/9 (LS 180, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.489×** | -5.5 | 8e-06 | 9/9 (KATO III, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.572×** | -4.4 | 0.001 | 9/9 (LoVo, KATO III, …) | top dose only | cell-cycle shift (explains ~16% here); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.733×** | -3.5 | 0.051 | 5/9 (NCI-H1573, COLO 205, …) | top dose only | low cells (technical?); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.634×** | -3.4 | 0.074 | 3/9 (BT-474, LS 180, …) | inconsistent across doses | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.664× | -3.2 | 0.11 | 4/9 (LoVo, COLO 205, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 0.05 µM |  | 0.657× | -3.2 | 0.11 | 0/9 | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.756× | -3.1 | 0.12 | 1/9 (BT-474) | inconsistent across doses | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 0.682× | -3.1 | 0.12 | 9/9 (LoVo, KATO III, …) | all doses, flat |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.683× | -3.0 | 0.12 | 0/9 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, +0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2594. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 326 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0387× (z -24.6) |
| [[NCI-H1573 (line)]] | alt | 475 | 1 (1 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.29× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.0427× (z -23.0) |
| [[AsPC-1 (line)]] | alt | 189 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.0382× (z -20.8) |
| [[KATO III (line)]] | alt | 1,681 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0146× (z -34.8) |
| [[HT-29 (line)]] | alt | 31.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0793× (z -15.3) |
| [[LS 180 (line)]] | wt | 391 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0143× (z -32.7) |
| [[BT-474 (line)]] | alt | 38.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0963× (z -12.4) |
| [[SHP-77 (line)]] | alt | 24.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -12.0) |
| [[COLO 205 (line)]] | alt | 50.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0938× (z -10.9) |
| [[A-172 (line)]] | wt | 6.39 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 5.83 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 4.93 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 5.35 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 11.7 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 6.49 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 6.06 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 13.7 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 7.08 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.80 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 6.30 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 7.47 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 7.12 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 6.31 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 6.56 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 5.68 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.09 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 5.45 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 7.07 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.55 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 4.98 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 6.07 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 267 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.82 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 13.2 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 5.67 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 59.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.11 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 5.43 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 4.71 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 6.37 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.57 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.50 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.67 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 9.28 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 11.8 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 7.03 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 6.75 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 18.1 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 17.3 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 5.58 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2594), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEACAM6]] | +0.89 | +0.89 / +0.88 | both halves | 7e-06 | same gene group; pathway: Cell surface interactions at the vascular wall; STRING 710; ⚠ same locus (20.5 kb, same strand: neighbours can correlate without regulation) |
| [[TSPAN1]] | +0.81 | +0.80 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[MUC2]] | +0.77 | +0.75 / +0.66 | both halves | 7e-06 | STRING 611 |
| [[TMEM45B]] | +0.76 | +0.80 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[CATSPERB]] | +0.74 | +0.74 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[TMPRSS4]] | +0.73 | +0.72 / +0.69 | both halves | 7e-06 |  |
| [[ITGB6]] | +0.73 | +0.72 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[SMIM31]] | +0.72 | +0.65 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[TMEM30B]] | +0.71 | +0.69 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[CAPN8]] | +0.71 | +0.76 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[SLC28A3]] | +0.70 | +0.73 / +0.64 | both halves | 7e-06 |  |
| [[MUC5B]] | +0.70 | +0.71 / +0.54 | both halves | 1e-05 |  |
| [[PPP1R1B]] | +0.69 | +0.76 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*97 arrows, 97 of them with an alert ⚠; grade A 0, B 3, C 94. Shown: the 12 strongest; 85 more arrows (85 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AQP3]] | B | AQP3 activity raises CEACAM5's level | lines that do not express AQP3 (19) vs lines expressing it (31) | 3.06× lower at baseline in the lines without AQP3 | 0.085 | ⚠ within organs, on part of the lines; also absent: ABCC3, ELF3, CD24; maybe low, not absent |
| [[FBXO17]] | B | FBXO17 activity lowers CEACAM5's level | lines that do not express FBXO17 (18) vs lines expressing it (32) | 4.19× higher at baseline in the lines without FBXO17 | 0.092 | ⚠ within organs, on part of the lines; also absent: ENSG00000269547, MRC2, MIR130AHG |
| [[EPS8L1]] | B | EPS8L1 activity raises CEACAM5's level | lines that do not express EPS8L1 (14) vs lines expressing it (36) | 2.57× lower at baseline in the lines without EPS8L1 | 0.097 | ⚠ within organs, on part of the lines; also absent: KIAA0040, IL1RN, MBNL3; maybe low, not absent |
| [[CDH17]] | C | CDH17 activity raises CEACAM5's level | lines that do not express CDH17 (40) vs lines expressing it (10) | 18.79× lower at baseline in the lines without CDH17 | 5e-05 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, MUC13, CLRN3; co-absent with the target |
| [[LINC00589]] | C | LINC00589 activity raises CEACAM5's level | lines that do not express LINC00589 (28) vs lines expressing it (22) | 4.66× lower at baseline in the lines without LINC00589 | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00520, ENSG00000267881, TSPAN8; co-absent with the target |
| [[NPSR1]] | C | NPSR1 activity raises CEACAM5's level | lines that do not express NPSR1 (42) vs lines expressing it (8) | 19.02× lower at baseline in the lines without NPSR1 | 4e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, MUC17, CDH17; co-absent with the target |
| [[FAM3D]] | C | FAM3D activity raises CEACAM5's level | lines that do not express FAM3D (43) vs lines expressing it (7) | 14.26× lower at baseline in the lines without FAM3D | 4e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, ENSG00000230975, NPSR1; maybe low, not absent; co-absent with the target |
| [[TMPRSS2]] | C | TMPRSS2 activity raises CEACAM5's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 8.63× lower at baseline in the lines without TMPRSS2 | 6e-04 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6; co-absent with the target |
| [[CEACAM6]] | C | CEACAM6 activity raises CEACAM5's level | lines that do not express CEACAM6 (37) vs lines expressing it (13) | 10.27× lower at baseline in the lines without CEACAM6 | 7e-04 | ⚠ within organs, on part of the lines; also absent: DAPP1, TMPRSS2, CDH17; co-absent with the target |
| [[ADGRF1]] | C | ADGRF1 activity raises CEACAM5's level | lines that do not express ADGRF1 (35) vs lines expressing it (15) | 7.58× lower at baseline in the lines without ADGRF1 | 8e-04 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4; co-absent with the target |
| [[TMPRSS4]] | C | TMPRSS4 activity raises CEACAM5's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 7.32× lower at baseline in the lines without TMPRSS4 | 0.001 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B; co-absent with the target |
| [[REG4]] | C | REG4 activity raises CEACAM5's level | lines that do not express REG4 (43) vs lines expressing it (7) | 21.87× lower at baseline in the lines without REG4 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, NPSR1, ENSG00000230975; co-absent with the target |

### Downstream of this gene

*115 arrows, 115 of them with an alert ⚠; grade A 0, B 25, C 90. Shown: the 12 strongest; 103 more arrows (103 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABHD17C]] | B | CEACAM5 activity raises ABHD17C's level | lines that do not express CEACAM5 (39) vs lines expressing it (11) | 4.35× lower at baseline in the lines without CEACAM5 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, ENSG00000267881 |
| [[CYSTM1]] | B | CEACAM5 activity raises CYSTM1's level | lines that do not express CEACAM5 (39) vs lines expressing it (11) | 2.28× lower at baseline in the lines without CEACAM5 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, ENSG00000267881 |
| [[BAG1]] | B | CEACAM5 activity raises BAG1's level | lines that do not express CEACAM5 (39) vs lines expressing it (11) | 2.01× lower at baseline in the lines without CEACAM5 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, ENSG00000267881 |
| [[SPIRE2]] | B | CEACAM5 activity raises SPIRE2's level | lines that do not express CEACAM5 (39) vs lines expressing it (11) | 2.25× lower at baseline in the lines without CEACAM5 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, ENSG00000267881 |
| [[TNFRSF21]] | B | CEACAM5 activity raises TNFRSF21's level | lines that do not express CEACAM5 (39) vs lines expressing it (11) | 4.18× lower at baseline in the lines without CEACAM5 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, ENSG00000267881 |
| [[SRMS]] | B | CEACAM5 activity raises SRMS's level | lines that do not express CEACAM5 (39) vs lines expressing it (11) | 2.77× lower at baseline in the lines without CEACAM5 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, ENSG00000267881 |
| [[EPS8L1]] | B | CEACAM5 activity raises EPS8L1's level | lines that do not express CEACAM5 (39) vs lines expressing it (11) | 3.78× lower at baseline in the lines without CEACAM5 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, ENSG00000267881 |
| [[LMO7]] | B | CEACAM5 activity raises LMO7's level | lines that do not express CEACAM5 (39) vs lines expressing it (11) | 4.14× lower at baseline in the lines without CEACAM5 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, ENSG00000267881 |
| [[ABHD11]] | B | CEACAM5 activity raises ABHD11's level | lines that do not express CEACAM5 (39) vs lines expressing it (11) | 2.63× lower at baseline in the lines without CEACAM5 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, ENSG00000267881 |
| [[PTPN14]] | B | CEACAM5 activity lowers PTPN14's level | lines that do not express CEACAM5 (39) vs lines expressing it (11) | 1.98× higher at baseline in the lines without CEACAM5 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, ENSG00000267881 |
| [[PROM2]] | B | CEACAM5 activity raises PROM2's level | lines that do not express CEACAM5 (39) vs lines expressing it (11) | 2.89× lower at baseline in the lines without CEACAM5 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, ENSG00000267881 |
| [[FAM83E]] | B | CEACAM5 activity raises FAM83E's level | lines that do not express CEACAM5 (39) vs lines expressing it (11) | 3.51× lower at baseline in the lines without CEACAM5 | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, ENSG00000267881 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.537). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.6, 56.3); signed map (59.9, 7.4). **Vector** length 66.9, 35.9% of its response variance represented; |z| ≥ 3 in 356 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.4 | +9.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.2 | +12.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.1 | +8.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +3.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | +1.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | -0.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.6 | +2.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +2.1 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.3 | +2.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.9 | -3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.5 | -3.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -2.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -1.1 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.3 | -2.9 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.3 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | CEA cell adhesion molecule 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:41,708,585-41,730,433 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CD66e; previously CEA |
| Gene groups (HGNC) | CD molecules; V-set domain containing; I-set domain containing; CEA cell adhesion molecule family |
| Reactome | 3 pathways, smallest: Post-translational modification: synthesis of GPI-anchored proteins; Cell surface interactions at the vascular wall; Hemostasis |
| Matched by | ensembl_id |

**Function**, from UniProt [P06731](https://www.uniprot.org/uniprotkb/P06731) (Cell adhesion molecule CEACAM5):

> Cell surface glycoprotein that plays a role in cell adhesion, intracellular signaling and tumor progression. Mediates homophilic and heterophilic cell adhesion with other carcinoembryonic antigen-related cell adhesion molecules, such as CEACAM6. Plays a role as an oncogene by promoting tumor progression; induces resistance to anoikis of colorectal carcinoma cells.; (Microbial infection) Receptor for E.coli Dr adhesins. Binding of E.coli Dr adhesins leads to dissociation of the homodimer.

**Summary**, from NCBI Gene [1048](https://www.ncbi.nlm.nih.gov/gene/1048):

> This gene encodes a cell surface glycoprotein that represents the founding member of the carcinoembryonic antigen (CEA) family of proteins. The encoded protein is used as a clinical biomarker for gastrointestinal cancers and may promote tumor development through its role as a cell adhesion molecule. Additionally, the encoded protein may regulate differentiation, apoptosis, and cell polarity. This gene is present in a CEA family gene cluster on chromosome 19. Alternative splicing results in …

**Accessions** — [HGNC:1817](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1817) · Entrez [1048](https://www.ncbi.nlm.nih.gov/gene/1048) · UniProt [P06731](https://www.uniprot.org/uniprotkb/P06731) · Ensembl [ENSG00000105388](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105388)

## Data

Gene col 2594: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2594); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2594, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2594]; `tensor/DDL_lfc|DDL_z.npy` [2594]; `embed/gene_vectors.npy` [2594]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2594 or target_col == 2594). Every well: [[CEACAM5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CEACAM5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
