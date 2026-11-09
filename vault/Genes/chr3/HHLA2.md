---
symbol: "HHLA2"
type: "gene"
col: 3556
ensembl_id: "ENSG00000114455"
name: "HHLA2 member of B7 family"
location: "3q13.13"
module: 8
arm: "+"
pooled_cpm: 6.21
n_lines_expressing: 12
n_dd_up: 31
n_dd_down: 1
n_dd_up_clean: 23
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 44
direction_downstream: 67
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# HHLA2

*HHLA2 member of B7 family* — 3q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.21× (z +12.7, q 4e-34, up in 2 of 10 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Benproperine (phosphate) (drug)]] 0.05 µM: 0.568× (z -4.0, q 0.030, down in 0 of 10 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 2 lines (HT-29 0.0479×, CFPAC-1 0.0685×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (HT-29 0.129×, LS 180 0.190×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 2 lines (LS 180 0.111×, HT-29 0.133×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADGRF1]] (+0.75, fdr 7e-06), [[ALOX5]] (+0.74, fdr 7e-06), [[RBM47]] (+0.71, fdr 7e-06).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 44 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 67 go from it, the strongest it → [[LINC01504]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3556.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.21×** | +12.7 | 4e-34 | 2/10 (HEC-1-A, A498) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **2.41×** | +9.6 | 4e-19 | 10/10 (A498, KATO III, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.40×** | +9.1 | 3e-17 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.19×** | +8.5 | 3e-15 | 2/10 (AsPC-1, LoVo) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.95×** | +8.3 | 1e-14 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.59×** | +6.8 | 1e-09 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.19×** | +6.0 | 2e-07 | 9/10 (A498, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.80×** | +5.2 | 1e-05 | 9/10 (AsPC-1, HT-29, …) | two highest doses | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.92×** | +4.8 | 9e-05 | 10/10 (HT-29, CFPAC-1, …) | rises with dose |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.21×** | +4.3 | 8e-04 | 0/6 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.78×** | +4.3 | 0.001 | 1/10 (HEC-1-A) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.12×** | +4.1 | 0.002 | 0/9 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.71×** | +4.1 | 0.002 | 5/10 (AsPC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.74×** | +4.1 | 0.002 | 8/10 (CFPAC-1, HT-29, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.66×** | +4.0 | 0.002 | 9/10 (HT-29, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.68×** | +4.0 | 0.003 | 8/10 (HT-29, CFPAC-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.67×** | +3.9 | 0.003 | 2/10 (A498, HEC-1-A) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.53×** | +3.7 | 0.007 | 7/10 (CFPAC-1, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.61×** | +3.7 | 0.007 | 3/10 (LoVo, A498, …) | rises with dose | cell-cycle shift (explains ~10% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3556.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 2 lines (HT-29 0.0479×, CFPAC-1 0.0685×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (HT-29 0.129×, LS 180 0.190×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 2 lines (LS 180 0.111×, HT-29 0.133×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Benproperine (phosphate) (drug)]] 0.05 µM |  | **0.568×** | -4.0 | 0.030 | 0/10 | inconsistent across doses |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | 0.652× | -3.3 | 0.26 | 1/10 (LoVo) | inconsistent across doses | position effect removed |
| [[Orlistat (drug)]] 5 µM |  | 0.658× | -3.1 | 0.35 | 0/10 | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3556. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 78.0 | 0 | 6 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0479× (z -17.9) |
| [[LS 180 (line)]] | wt | 89.0 | 1 | 5 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.55× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.190× (z -15.7) |
| [[CFPAC-1 (line)]] | alt | 27.1 | 0 | 5 (4 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0685× (z -13.4) |
| [[LoVo (line)]] | wt | 6.40 | 2 (1 ⚠) | 1 | [[Harringtonine (drug)]] 5 µM 21.6× (z +12.2) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 4.44× (z +8.8) | [[Dihydroartemisinin (drug)]] 0.5 µM 0.113× (z -9.0) |
| [[A498 (line)]] | wt | 3.21 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 24.8× (z +14.1) | — |
| [[AsPC-1 (line)]] | alt | 27.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.92× (z +14.3) | — |
| [[KATO III (line)]] | alt | 2.91 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 20.7× (z +10.7) | — |
| [[A-172 (line)]] | wt | 0.605 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.602 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.542 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.793 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.618 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.727 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.957 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.633 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.651 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.696 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.668 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.550 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.635 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.810 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.520 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.706 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.537 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.969 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.518 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.594 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.701 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.585 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.721 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.700 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.577 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.588 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.611 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.647 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.693 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.647 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.635 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.790 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.681 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.991 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.538 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3556), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADGRF1]] | +0.75 | +0.69 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[ALOX5]] | +0.74 | +0.65 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[RBM47]] | +0.71 | +0.63 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[ST14]] | +0.70 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[MUC4]] | +0.69 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[TRIM31]] | +0.69 | +0.60 / +0.77 | both halves | 7e-06 |  |
| [[SLC44A4]] | +0.69 | +0.65 / +0.74 | both halves | 7e-06 |  |
| [[SLC34A2]] | +0.67 | +0.60 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[BCAS1]] | +0.67 | +0.57 / +0.71 | both halves | 9e-06 |  |
| [[DAPP1]] | +0.66 | +0.58 / +0.70 | both halves | 8e-06 | **novel candidate** |
| [[CGN]] | +0.66 | +0.55 / +0.70 | both halves | 1e-05 |  |
| [[FRK]] | +0.66 | +0.51 / +0.74 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*44 arrows, 44 of them with an alert ⚠; grade A 0, B 2, C 42. Shown: the 12 strongest; 32 more arrows (32 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers HHLA2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[GBP2]] | B | GBP2 activity raises HHLA2's level | lines that do not express GBP2 (13) vs lines expressing it (37) | 1.78× lower at baseline in the lines without GBP2 | 0.067 | ⚠ within organs, on part of the lines; also absent: GBP1, ITGA3, SH3TC1 |
| [[TM4SF4]] | C | TM4SF4 activity raises HHLA2's level | lines that do not express TM4SF4 (42) vs lines expressing it (8) | 7.28× lower at baseline in the lines without TM4SF4 | 1e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PIGR, MUC17, HHLA2; co-absent with the target |
| [[TRIM31]] | C | TRIM31 activity raises HHLA2's level | lines that do not express TRIM31 (39) vs lines expressing it (11) | 5.81× lower at baseline in the lines without TRIM31 | 8e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC13, GCNT3, NPSR1; co-absent with the target |
| [[ADGRF1]] | C | ADGRF1 activity raises HHLA2's level | lines that do not express ADGRF1 (35) vs lines expressing it (15) | 3.76× lower at baseline in the lines without ADGRF1 | 0.003 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4; co-absent with the target |
| [[DAPP1]] | C | DAPP1 activity raises HHLA2's level | lines that do not express DAPP1 (39) vs lines expressing it (11) | 4.16× lower at baseline in the lines without DAPP1 | 0.003 | ⚠ within organs, on part of the lines; also absent: SLC6A14, CEACAM6, MUC5B; co-absent with the target |
| [[MUC13]] | C | MUC13 activity raises HHLA2's level | lines that do not express MUC13 (40) vs lines expressing it (10) | 4.90× lower at baseline in the lines without MUC13 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, NPSR1, CDH17; co-absent with the target |
| [[CDH17]] | C | CDH17 activity raises HHLA2's level | lines that do not express CDH17 (40) vs lines expressing it (10) | 4.68× lower at baseline in the lines without CDH17 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, MUC13, CLRN3; co-absent with the target |
| [[INAVA]] | C | INAVA activity raises HHLA2's level | lines that do not express INAVA (29) vs lines expressing it (21) | 2.86× lower at baseline in the lines without INAVA | 0.008 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3; co-absent with the target |
| [[PTPRR]] | C | PTPRR activity raises HHLA2's level | lines that do not express PTPRR (32) vs lines expressing it (18) | 2.72× lower at baseline in the lines without PTPRR | 0.008 | ⚠ within organs, on part of the lines; also absent: DHRS9, LINC01133, TFF2; co-absent with the target |
| [[TMPRSS2]] | C | TMPRSS2 activity raises HHLA2's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 3.51× lower at baseline in the lines without TMPRSS2 | 0.011 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6; co-absent with the target |
| [[ALOX5]] | C | ALOX5 activity raises HHLA2's level | lines that do not express ALOX5 (28) vs lines expressing it (22) | 2.64× lower at baseline in the lines without ALOX5 | 0.015 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ADGRF1, RASSF6; co-absent with the target |

### Downstream of this gene

*67 arrows, 67 of them with an alert ⚠; grade A 0, B 19, C 48. Shown: the 12 strongest; 55 more arrows (55 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01504]] | B | HHLA2 activity raises LINC01504's level | lines that do not express HHLA2 (38) vs lines expressing it (12) | 2.31× lower at baseline in the lines without HHLA2 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, TM4SF4, MUC13 |
| [[MYH14]] | B | HHLA2 activity raises MYH14's level | lines that do not express HHLA2 (38) vs lines expressing it (12) | 4.76× lower at baseline in the lines without HHLA2 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, TM4SF4, MUC13 |
| [[ATP1B1]] | B | HHLA2 activity raises ATP1B1's level | lines that do not express HHLA2 (38) vs lines expressing it (12) | 2.97× lower at baseline in the lines without HHLA2 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, TM4SF4, MUC13 |
| [[TUFT1]] | B | HHLA2 activity raises TUFT1's level | lines that do not express HHLA2 (38) vs lines expressing it (12) | 2.40× lower at baseline in the lines without HHLA2 | 0.026 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, TM4SF4, MUC13 |
| [[FZD5]] | B | HHLA2 activity raises FZD5's level | lines that do not express HHLA2 (38) vs lines expressing it (12) | 2.32× lower at baseline in the lines without HHLA2 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, TM4SF4, MUC13 |
| [[LINC01504]] | B | HHLA2 activity strengthens LINC01504's drug response | lines that do not express HHLA2 (38) vs lines expressing it (10) | the lines without HHLA2 respond 0.64× as strongly (z diff +0.59); rises at some drug-doses, falls at others (53% from rises): Hexylresorcinol 5 µM: 0.81x vs 0.57x (z diff +2.5); Digitoxin 0.5 µM: 0.65x vs 0.45x (z diff +2.3); Panobinostat 5 µM: 1.33x vs 2.01x (z diff +2.1) | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, TM4SF4, MUC13; target measured in part of the lines; rises at some drug-doses, falls at others; artifact flags |
| [[ELF3-AS1]] | B | HHLA2 activity raises ELF3-AS1's level | lines that do not express HHLA2 (38) vs lines expressing it (12) | 2.87× lower at baseline in the lines without HHLA2 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, TM4SF4, MUC13 |
| [[TSPAN15]] | B | HHLA2 activity raises TSPAN15's level | lines that do not express HHLA2 (38) vs lines expressing it (12) | 2.88× lower at baseline in the lines without HHLA2 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, TM4SF4, MUC13 |
| [[LNX1]] | B | HHLA2 activity raises LNX1's level | lines that do not express HHLA2 (38) vs lines expressing it (12) | 3.40× lower at baseline in the lines without HHLA2 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, TM4SF4, MUC13 |
| [[CARD14]] | B | HHLA2 activity raises CARD14's level | lines that do not express HHLA2 (38) vs lines expressing it (12) | 1.67× lower at baseline in the lines without HHLA2 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, TM4SF4, MUC13 |
| [[C4orf19]] | B | HHLA2 activity raises C4orf19's level | lines that do not express HHLA2 (38) vs lines expressing it (12) | 2.87× lower at baseline in the lines without HHLA2 | 0.053 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, TM4SF4, MUC13 |
| [[CD2AP]] | B | HHLA2 activity raises CD2AP's level | lines that do not express HHLA2 (38) vs lines expressing it (12) | 1.67× lower at baseline in the lines without HHLA2 | 0.072 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, TM4SF4, MUC13 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.733). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.9, 54.7); signed map (59.3, 3.5). **Vector** length 53.0, 20.2% of its response variance represented; |z| ≥ 3 in 369 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Dectin-2 family* (reactome, mean cos +0.53 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +9.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.1 | +6.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.1 | +6.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.0 | +9.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.9 | +8.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.9 | +4.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.8 | +5.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.7 | +4.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.3 | +4.1 |
| fall | [[Dabrafenib (drug)]] 5 µM |  | -1.3 | -2.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.2 | -0.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.2 | -2.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.1 | -0.4 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.1 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | HHLA2 member of B7 family |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q13.13 — chr3:108,296,529-108,378,285 (+) |
| Ensembl biotype | protein_coding |
| Also known as | B7H7, B7-H5, B7y, B7-H7 |
| Gene groups (HGNC) | V-set domain containing; C1-set domain containing; B7 family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UM44](https://www.uniprot.org/uniprotkb/Q9UM44) (HERV-H LTR-associating protein 2):

> Through interaction with TMIGD2, costimulates T-cells in the context of TCR-mediated activation. Enhances T-cell proliferation and cytokine production via an AKT-dependent signaling cascade.

**Summary**, from NCBI Gene [11148](https://www.ncbi.nlm.nih.gov/gene/11148):

> This gene encodes a protein ligand found on the surface of monocytes. The encoded protein is thought to regulate cell-mediated immunity by binding to a receptor on T lymphocytes and inhibiting the proliferation of these cells. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Sep 2013]

**Accessions** — [HGNC:4905](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4905) · Entrez [11148](https://www.ncbi.nlm.nih.gov/gene/11148) · UniProt [Q9UM44](https://www.uniprot.org/uniprotkb/Q9UM44) · Ensembl [ENSG00000114455](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114455)

## Data

Gene col 3556: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3556); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3556, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3556]; `tensor/DDL_lfc|DDL_z.npy` [3556]; `embed/gene_vectors.npy` [3556]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3556 or target_col == 3556). Every well: [[HHLA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HHLA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
