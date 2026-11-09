---
symbol: "KC6"
type: "gene"
col: 15541
ensembl_id: "ENSG00000267313"
name: ""
location: ""
module: 108
arm: "+"
pooled_cpm: 5.8
n_lines_expressing: 18
n_dd_up: 11
n_dd_down: 8
n_dd_up_clean: 4
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 10
direction_downstream: 26
tags: ["gene", "module/108"]
generated_by: "tahoemap"
---

# KC6

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.19× (z +10.6, q 2e-23, up in 1 of 15 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.481× (z -7.0, q 2e-09, down in 11 of 15 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF521]] (+0.78, fdr 7e-06), [[LINC02377]] (+0.77, fdr 7e-06), [[LINC02109]] (+0.73, fdr 7e-06); moves opposite to [[MYO5C]] (-0.49, fdr 2e-04), [[PATJ]] (-0.48, fdr 3e-05).
> It is in [[Module 108]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 26 go from it, the strongest it → [[LDB2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15541.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.19×** | +10.6 | 2e-23 | 1/15 (hTERT-HPNE) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.15×** | +10.5 | 2e-23 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.71×** | +9.5 | 4e-19 | 1/10 (Hs 766T) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.15×** | +6.7 | 2e-09 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Entrectinib (drug)]] 5 µM |  | **1.48×** | +3.8 | 0.020 | 1/15 (J82) | top dose only |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.67×** | +3.5 | 0.039 | 0/10 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.44×** | +3.5 | 0.039 | 2/15 (A-427, LOX-IMVI) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Saquinavir (drug)]] 5 µM |  | **1.28×** | +3.4 | 0.055 | 2/13 (H4, HS-578T) | inconsistent across doses | position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.94×** | +3.3 | 0.059 | 0/9 | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.41×** | +3.3 | 0.060 | 0/13 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.41×** | +3.2 | 0.060 | 0/12 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Saquinavir (drug)]] 0.05 µM |  | 1.38× | +3.0 | 0.11 | 3/13 (C32, A-427, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15541.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.481×** | -7.0 | 2e-09 | 11/15 (H4, CHP-212, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.499×** | -6.6 | 9e-09 | 12/14 (HS-578T, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.594×** | -5.0 | 1e-04 | 8/15 (RPMI-7951, C32, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.606×** | -4.8 | 2e-04 | 10/15 (H4, CHP-212, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.641×** | -4.1 | 0.005 | 7/15 (J82, C32, …) | two highest doses | cell-cycle shift (explains ~3% here); composition shift |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | **0.640×** | -3.9 | 0.008 | 1/15 (SW 1271) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.693×** | -3.5 | 0.037 | 12/15 (H4, CHP-212, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.706×** | -3.3 | 0.063 | 6/15 (H4, SW 1271, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15541. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 91.7 | 0 | 9 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0537× (z -18.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.142× (z -17.9) |
| [[RPMI-7951 (line)]] | alt | 29.0 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0900× (z -16.8) ⚠ cell-cycle shift, explains <1% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.105× (z -15.7) |
| [[CHP-212 (line)]] | wt | 218 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0543× (z -17.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.190× (z -14.0) |
| [[HS-578T (line)]] | alt | 45.4 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.206× (z -16.1) |
| [[NCI-H1792 (line)]] | alt | 25.2 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0513× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.162× (z -9.6) |
| [[C32 (line)]] | wt | 20.2 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0836× (z -14.9) ⚠ cell-cycle shift, explains <1% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0491× (z -12.8) |
| [[J82 (line)]] | alt | 4.37 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0465× (z -10.0) |
| [[SHP-77 (line)]] | alt | 8.83 | 0 | 1 | — | [[DT-061 (drug)]] 0.05 µM 0.0634× (z -9.4) |
| [[SK-MEL-2 (line)]] | alt | 12.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0986× (z -9.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 5.44 | 0 | 1 | — | [[Vilanterol (drug)]] 0.05 µM 0.0806× (z -8.9) |
| [[A-172 (line)]] | wt | 0.744 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.653 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.632 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.695 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.635 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.610 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.686 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.797 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.690 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.733 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.752 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.75 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.822 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.765 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.622 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.639 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.608 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.570 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.732 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.556 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.929 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.722 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.781 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.854 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.670 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.835 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.821 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15541), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF521]] | +0.78 | +0.78 / +0.77 | both halves | 7e-06 |  |
| [[LINC02377]] | +0.77 | +0.67 / +0.77 | both halves | 7e-06 |  |
| [[LINC02109]] | +0.73 | +0.69 / +0.58 | both halves | 7e-06 |  |
| [[LINC01242]] | +0.70 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[APBB1IP]] | +0.65 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[MSC-AS1]] | +0.65 | +0.57 / +0.64 | both halves | 9e-06 |  |
| [[MAGEA3-DT]] | +0.65 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[LINC01446]] | +0.64 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[PRRX1]] | +0.64 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[LINC00879]] | +0.64 | +0.49 / +0.67 | both halves | 1e-05 |  |
| [[MDGA2]] | +0.63 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[RARB]] | +0.63 | +0.50 / +0.66 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYO5C]] | -0.49 | -0.53 / -0.31 | both halves | 2e-04 |  |
| [[PATJ]] | -0.48 | -0.48 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 1, C 9.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises KC6's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CCNYL2]] | C | CCNYL2 activity raises KC6's level | lines that do not express CCNYL2 (29) vs lines expressing it (21) | 4.83× lower at baseline in the lines without CCNYL2 | 0.007 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with KRAS; also absent: LINC00839, KC6, MSR1; co-absent with the target |
| [[CDH8]] | C | CDH8 activity raises KC6's level | lines that do not express CDH8 (28) vs lines expressing it (22) | 3.68× lower at baseline in the lines without CDH8 | 0.027 | ⚠ within organs, on part of the lines; also absent: ZIC1, IGFBP5, PCDH18; maybe low, not absent; co-absent with the target |
| [[FRG1FP]] | C | FRG1FP activity raises KC6's level | lines that do not express FRG1FP (22) vs lines expressing it (28) | 3.61× lower at baseline in the lines without FRG1FP | 0.034 | ⚠ within organs, on part of the lines; also absent: FRG1GP, LINC01446, ENSG00000248973; maybe low, not absent; co-absent with the target |
| [[FAM230C]] | C | FAM230C activity raises KC6's level | lines that do not express FAM230C (28) vs lines expressing it (22) | 3.34× lower at baseline in the lines without FAM230C | 0.038 | ⚠ within organs, on part of the lines; also absent: ENSG00000277693, LINC01446, LINC01266; co-absent with the target |
| [[ZNF208]] | C | ZNF208 activity raises KC6's level | lines that do not express ZNF208 (41) vs lines expressing it (9) | 4.91× lower at baseline in the lines without ZNF208 | 0.052 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000234426, LINC01029, ENSG00000287598; co-absent with the target |
| [[MME]] | C | MME activity raises KC6's level | lines that do not express MME (30) vs lines expressing it (20) | 4.54× lower at baseline in the lines without MME | 0.060 | ⚠ within organs, on part of the lines; also absent: APCDD1L, PHACTR1, GYPC; co-absent with the target |
| [[HTR1F]] | C | HTR1F activity raises KC6's level | lines that do not express HTR1F (34) vs lines expressing it (16) | 4.67× lower at baseline in the lines without HTR1F | 0.083 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MGP, TIMP3, AEBP1; maybe low, not absent; co-absent with the target |
| [[FRG1JP]] | C | FRG1JP activity raises KC6's level | lines that do not express FRG1JP (23) vs lines expressing it (27) | 3.50× lower at baseline in the lines without FRG1JP | 0.086 | ⚠ within organs, on part of the lines; also absent: LSAMP, TRPV2, MSC; maybe low, not absent; co-absent with the target |
| [[MIR646HG]] | C | MIR646HG activity raises KC6's level | lines that do not express MIR646HG (34) vs lines expressing it (16) | 3.05× lower at baseline in the lines without MIR646HG | 0.091 | ⚠ within organs, on part of the lines; also absent: ENSG00000253642, ADGRG7, ENSG00000287211; co-absent with the target |

### Downstream of this gene

*26 arrows, 26 of them with an alert ⚠; grade A 0, B 6, C 20. Shown: the 12 strongest; 14 more arrows (14 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LDB2]] | B | KC6 activity raises LDB2's level | lines that do not express KC6 (32) vs lines expressing it (18) | 3.48× lower at baseline in the lines without KC6 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: GYPC, CCNYL2, COL19A1 |
| [[TMEM45A]] | B | KC6 activity raises TMEM45A's level | lines that do not express KC6 (32) vs lines expressing it (18) | 4.56× lower at baseline in the lines without KC6 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: GYPC, CCNYL2, COL19A1 |
| [[MIR181A1HG]] | B | KC6 activity raises MIR181A1HG's level | lines that do not express KC6 (32) vs lines expressing it (18) | 2.79× lower at baseline in the lines without KC6 | 0.069 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: GYPC, CCNYL2, COL19A1 |
| [[FAM13C]] | B | KC6 activity raises FAM13C's level | lines that do not express KC6 (32) vs lines expressing it (18) | 2.38× lower at baseline in the lines without KC6 | 0.081 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: GYPC, CCNYL2, COL19A1 |
| [[SLC14A2]] | B | KC6 activity raises SLC14A2's level | lines that do not express KC6 (32) vs lines expressing it (18) | 2.27× lower at baseline in the lines without KC6 | 0.093 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: GYPC, CCNYL2, COL19A1 |
| [[LINC02226]] | B | KC6 activity raises LINC02226's level | lines that do not express KC6 (32) vs lines expressing it (18) | 1.91× lower at baseline in the lines without KC6 | 0.096 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: GYPC, CCNYL2, COL19A1 |
| [[CDH12]] | C | KC6 activity raises CDH12's level | lines that do not express KC6 (32) vs lines expressing it (18) | 3.81× lower at baseline in the lines without KC6 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: GYPC, CCNYL2, COL19A1; co-absent with the target |
| [[MSR1]] | C | KC6 activity raises MSR1's level | lines that do not express KC6 (32) vs lines expressing it (18) | 3.64× lower at baseline in the lines without KC6 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: GYPC, CCNYL2, COL19A1; co-absent with the target |
| [[TIMP3]] | C | KC6 activity raises TIMP3's level | lines that do not express KC6 (32) vs lines expressing it (18) | 10.15× lower at baseline in the lines without KC6 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: GYPC, CCNYL2, COL19A1; co-absent with the target |
| [[MIR646HG]] | C | KC6 activity raises MIR646HG's level | lines that do not express KC6 (32) vs lines expressing it (18) | 3.99× lower at baseline in the lines without KC6 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: GYPC, CCNYL2, COL19A1; co-absent with the target |
| [[AEBP1]] | C | KC6 activity raises AEBP1's level | lines that do not express KC6 (32) vs lines expressing it (18) | 4.00× lower at baseline in the lines without KC6 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: GYPC, CCNYL2, COL19A1; co-absent with the target |
| [[NETO1]] | C | KC6 activity raises NETO1's level | lines that do not express KC6 (32) vs lines expressing it (18) | 2.75× lower at baseline in the lines without KC6 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: GYPC, CCNYL2, COL19A1; co-absent with the target |

## Where it sits

- **Module**: [[Module 108]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.853). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (47.9, 25.6); signed map (32.0, 43.6). **Vector** length 53.3, 17.0% of its response variance represented; |z| ≥ 3 in 390 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.8 | +9.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.4 | +10.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.0 | +6.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +10.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +0.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.6 | +0.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | -2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +2.5 |
| fall | [[Lucanthone (drug)]] 0.05 µM |  | -1.5 | -1.4 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.5 | -2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | -1.5 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.3 | -3.9 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.3 | -1.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.3 | -1.7 |

## What is on record

> [!warning] No registry record
> KC6 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 15541: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15541); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15541, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15541]; `tensor/DDL_lfc|DDL_z.npy` [15541]; `embed/gene_vectors.npy` [15541]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15541 or target_col == 15541). Every well: [[KC6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KC6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
