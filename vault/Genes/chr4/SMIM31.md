---
symbol: "SMIM31"
type: "gene"
col: 14569
ensembl_id: "ENSG00000248771"
name: "small integral membrane protein 31"
location: "4q32.3"
module: 8
arm: "+"
pooled_cpm: 7.65
n_lines_expressing: 16
n_dd_up: 10
n_dd_down: 5
n_dd_up_clean: 1
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 64
direction_downstream: 77
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# SMIM31

*small integral membrane protein 31* — 4q32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.60× (z +10.1, q 5e-21, up in 2 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 1.83× (z +3.3, q 0.073, up in 0 of 12 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.531× (z -5.0, q 2e-04, down in 14 of 14 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CEACAM5]] (+0.72, fdr 7e-06), [[TMEM45B]] (+0.71, fdr 7e-06), [[ITGB6]] (+0.67, fdr 7e-06); moves opposite to [[KATNAL1]] (-0.54, fdr 5e-05), [[ANKRD36]] (-0.48, fdr 3e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 64 arrows point to it, the strongest [[KATNAL1]] → it (grade B ⚠); 77 go from it, the strongest it → [[KATNAL1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 9 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14569.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.60×** | +10.1 | 5e-21 | 2/9 (AsPC-1, SW 900) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.56×** | +9.6 | 3e-19 | 1/8 (SW 900) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.99×** | +7.9 | 4e-13 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.71×** | +4.2 | 0.004 | 2/11 (BT-474, LoVo) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.69×** | +3.9 | 0.009 | 2/11 (LoVo, SW 900) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +3.7 | 0.018 | 2/13 (BT-474, LoVo) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.35×** | +3.3 | 0.070 | 5/13 (LS 180, LoVo, …) | top dose only | composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.83×** | +3.3 | 0.073 | 0/12 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.51×** | +3.2 | 0.075 | 0/10 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~25% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.19×** | +3.2 | 0.075 | 1/8 (SW 900) | rises with dose | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | 1.32× | +3.1 | 0.11 | 0/12 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cabozantinib (S-malate) (drug)]] 0.5 µM |  | 1.48× | +3.0 | 0.11 | 1/14 (KATO III) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14569.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.531×** | -5.0 | 2e-04 | 14/14 (LS 180, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.534×** | -5.0 | 2e-04 | 12/14 (LS 180, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~22% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.584×** | -4.3 | 0.004 | 11/14 (LS 180, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~6% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.607×** | -4.0 | 0.011 | 12/14 (LS 180, LoVo, …) | all doses, flat | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.589×** | -3.9 | 0.012 | 3/14 (NCI-H1573, BT-474, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14569. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 28.3 | 0 | 11 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0218× (z -17.9) |
| [[LS 180 (line)]] | wt | 78.4 | 0 | 10 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0236× (z -28.6) |
| [[HT-29 (line)]] | alt | 29.9 | 0 | 8 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0385× (z -17.2) |
| [[BT-474 (line)]] | alt | 15.2 | 0 | 7 (3 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0423× (z -12.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Neratinib (drug)]] 5 µM 0.0620× (z -11.0) |
| [[LoVo (line)]] | wt | 15.7 | 0 | 6 (3 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0267× (z -21.0) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0617× (z -16.2) |
| [[NCI-H1573 (line)]] | alt | 99.6 | 0 | 5 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0583× (z -17.1) |
| [[SK-MEL-2 (line)]] | alt | 7.58 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0623× (z -9.8) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0655× (z -9.6) |
| [[SW 900 (line)]] | alt | 18.6 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0769× (z -10.9) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0790× (z -10.8) |
| [[A-172 (line)]] | wt | 0.906 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.931 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.42 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.71 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.960 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.937 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.990 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.906 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.988 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.957 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.765 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.22 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.729 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.616 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.793 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 8.82 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.766 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.874 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.851 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.840 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.792 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.895 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.902 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.824 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.03 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.773 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14569), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEACAM5]] | +0.72 | +0.65 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[TMEM45B]] | +0.71 | +0.64 / +0.72 | both halves | 7e-06 |  |
| [[ITGB6]] | +0.67 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[TNFRSF21]] | +0.67 | +0.63 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[SLC28A3]] | +0.66 | +0.65 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[CATSPERB]] | +0.63 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[ADGRF1]] | +0.62 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[CYP3A5]] | +0.61 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[DAPP1]] | +0.61 | +0.67 / +0.43 | both halves | 3e-05 |  |
| [[ARHGAP30]] | +0.58 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[TMPRSS4]] | +0.58 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[FLRT3]] | +0.57 | +0.56 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KATNAL1]] | -0.54 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[ANKRD36]] | -0.48 | -0.44 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*64 arrows, 64 of them with an alert ⚠; grade A 0, B 6, C 58. Shown: the 12 strongest; 52 more arrows (52 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KATNAL1]] | B | KATNAL1 activity lowers SMIM31's level | lines that do not express KATNAL1 (7) vs lines expressing it (43) | 7.55× higher at baseline in the lines without KATNAL1 | 0.002 | ⚠ within organs, on part of the lines; also absent: BOLA3-DT, STARD9, SPAG17 |
| [[HEG1]] | B | HEG1 activity lowers SMIM31's level | lines that do not express HEG1 (11) vs lines expressing it (39) | 3.72× higher at baseline in the lines without HEG1 | 0.023 | ⚠ within organs, on part of the lines; also absent: CCDC88A, STARD9, RECK |
| [[SRMS]] | B | SRMS activity raises SMIM31's level | lines that do not express SRMS (14) vs lines expressing it (36) | 2.19× lower at baseline in the lines without SRMS | 0.039 | ⚠ within organs, on part of the lines; also absent: MX1, OAS2, RSAD2 |
| [[HDAC6]] | B | HDAC6 activity raises SMIM31's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ELF3-AS1]] | B | ELF3-AS1 activity raises SMIM31's level | lines that do not express ELF3-AS1 (15) vs lines expressing it (35) | 2.20× lower at baseline in the lines without ELF3-AS1 | 0.075 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, EFNA1; maybe low, not absent |
| [[LXN]] | B | LXN activity raises SMIM31's level | lines that do not express LXN (19) vs lines expressing it (31) | 2.00× lower at baseline in the lines without LXN | 0.092 | ⚠ within organs, on part of the lines; also absent: GPX3, CYP4F11, SLPI; maybe low, not absent |
| [[FAM3D]] | C | FAM3D activity raises SMIM31's level | lines that do not express FAM3D (43) vs lines expressing it (7) | 11.69× lower at baseline in the lines without FAM3D | 1e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, ENSG00000230975, NPSR1; maybe low, not absent; co-absent with the target |
| [[CEACAM5]] | C | CEACAM5 activity raises SMIM31's level | lines that do not express CEACAM5 (39) vs lines expressing it (11) | 7.14× lower at baseline in the lines without CEACAM5 | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, ENSG00000267881; co-absent with the target |
| [[CDH17]] | C | CDH17 activity raises SMIM31's level | lines that do not express CDH17 (40) vs lines expressing it (10) | 6.20× lower at baseline in the lines without CDH17 | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, MUC13, CLRN3; co-absent with the target |
| [[ADGRF1]] | C | ADGRF1 activity raises SMIM31's level | lines that do not express ADGRF1 (35) vs lines expressing it (15) | 4.24× lower at baseline in the lines without ADGRF1 | 6e-04 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4; co-absent with the target |
| [[TFF1]] | C | TFF1 activity raises SMIM31's level | lines that do not express TFF1 (31) vs lines expressing it (19) | 3.74× lower at baseline in the lines without TFF1 | 0.001 | ⚠ within organs, on part of the lines; also absent: TOX3, CEACAM5, MUC5AC; co-absent with the target |
| [[TOX3]] | C | TOX3 activity raises SMIM31's level | lines that do not express TOX3 (31) vs lines expressing it (19) | 4.16× lower at baseline in the lines without TOX3 | 0.001 | ⚠ within organs, on part of the lines; also absent: GPX2, ENSG00000287426, TMEM45B; co-absent with the target |

### Downstream of this gene

*77 arrows, 77 of them with an alert ⚠; grade A 0, B 17, C 60. Shown: the 12 strongest; 65 more arrows (65 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KATNAL1]] | B | SMIM31 activity lowers KATNAL1's level | lines that do not express SMIM31 (34) vs lines expressing it (16) | 3.21× higher at baseline in the lines without SMIM31 | 0.001 | ⚠ within organs, on part of the lines; also absent: CEACAM5, PPP1R1B, ENSG00000267881 |
| [[ANKRD36]] | B | SMIM31 activity weakens ANKRD36's drug response | lines that do not express SMIM31 (34) vs lines expressing it (15) | the lines without SMIM31 respond 1.38× as strongly (z diff -1.88); strongest at Panobinostat 0.5 µM: 0.55x vs 0.83x (z diff -3.3) | 0.006 | ⚠ within organs, on part of the lines; also absent: CEACAM5, PPP1R1B, ENSG00000267881; target measured in part of the lines; artifact flags |
| [[ANKRD36]] | B | SMIM31 activity lowers ANKRD36's level | lines that do not express SMIM31 (34) vs lines expressing it (16) | 1.80× higher at baseline in the lines without SMIM31 | 0.008 | ⚠ within organs, on part of the lines; also absent: CEACAM5, PPP1R1B, ENSG00000267881 |
| [[ELF3-AS1]] | B | SMIM31 activity raises ELF3-AS1's level | lines that do not express SMIM31 (34) vs lines expressing it (16) | 2.97× lower at baseline in the lines without SMIM31 | 0.015 | ⚠ within organs, on part of the lines; also absent: CEACAM5, PPP1R1B, ENSG00000267881 |
| [[FAM83E]] | B | SMIM31 activity raises FAM83E's level | lines that do not express SMIM31 (34) vs lines expressing it (16) | 2.98× lower at baseline in the lines without SMIM31 | 0.018 | ⚠ within organs, on part of the lines; also absent: CEACAM5, PPP1R1B, ENSG00000267881 |
| [[SRMS]] | B | SMIM31 activity raises SRMS's level | lines that do not express SMIM31 (34) vs lines expressing it (16) | 2.14× lower at baseline in the lines without SMIM31 | 0.019 | ⚠ within organs, on part of the lines; also absent: CEACAM5, PPP1R1B, ENSG00000267881 |
| [[STX19]] | B | SMIM31 activity raises STX19's level | lines that do not express SMIM31 (34) vs lines expressing it (16) | 2.16× lower at baseline in the lines without SMIM31 | 0.019 | ⚠ within organs, on part of the lines; also absent: CEACAM5, PPP1R1B, ENSG00000267881 |
| [[EPS8L1]] | B | SMIM31 activity raises EPS8L1's level | lines that do not express SMIM31 (34) vs lines expressing it (16) | 3.08× lower at baseline in the lines without SMIM31 | 0.020 | ⚠ within organs, on part of the lines; also absent: CEACAM5, PPP1R1B, ENSG00000267881 |
| [[RBM47]] | B | SMIM31 activity raises RBM47's level | lines that do not express SMIM31 (34) vs lines expressing it (16) | 4.30× lower at baseline in the lines without SMIM31 | 0.021 | ⚠ within organs, on part of the lines; also absent: CEACAM5, PPP1R1B, ENSG00000267881 |
| [[ATP1B1]] | B | SMIM31 activity raises ATP1B1's level | lines that do not express SMIM31 (34) vs lines expressing it (16) | 2.72× lower at baseline in the lines without SMIM31 | 0.021 | ⚠ within organs, on part of the lines; also absent: CEACAM5, PPP1R1B, ENSG00000267881 |
| [[TNFRSF21]] | B | SMIM31 activity raises TNFRSF21's level | lines that do not express SMIM31 (34) vs lines expressing it (16) | 3.49× lower at baseline in the lines without SMIM31 | 0.039 | ⚠ within organs, on part of the lines; also absent: CEACAM5, PPP1R1B, ENSG00000267881 |
| [[STX19]] | B | SMIM31 activity strengthens STX19's drug response | lines that do not express SMIM31 (20) vs lines expressing it (11) | the lines without SMIM31 respond 1.78× as strongly (z diff -0.35); strongest at Homoharringtonine 5 µM: 1.58x vs 4.38x (z diff +5.6) | 0.052 | ⚠ within organs, on part of the lines; also absent: CEACAM5, PPP1R1B, ENSG00000267881; target measured in part of the lines; both ways; artifact flags |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.557). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.4, 56.2); signed map (59.2, 7.5). **Vector** length 61.2, 20.7% of its response variance represented; |z| ≥ 3 in 446 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.1 | +7.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +9.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.8 | +10.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.7 | +3.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +2.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.7 | +1.8 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.6 | +1.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.4 | +0.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +3.3 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -3.9 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -1.7 | -0.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.6 | -1.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.3 | -1.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.3 | -1.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -1.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.3 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | small integral membrane protein 31 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q32.3 — chr4:164,754,064-164,803,795 (+) |
| Ensembl biotype | protein_coding |
| Also known as | h.EPR; previously LINC01207 |
| Matched by | ensembl_id |

UniProt [A0A1B0GVY4](https://www.uniprot.org/uniprotkb/A0A1B0GVY4) carries no function annotation.

**Summary**, from NCBI Gene [100505989](https://www.ncbi.nlm.nih.gov/gene/100505989):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:49638](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:49638) · Entrez [100505989](https://www.ncbi.nlm.nih.gov/gene/100505989) · UniProt [A0A1B0GVY4](https://www.uniprot.org/uniprotkb/A0A1B0GVY4) · Ensembl [ENSG00000248771](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000248771)

## Data

Gene col 14569: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14569); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14569, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14569]; `tensor/DDL_lfc|DDL_z.npy` [14569]; `embed/gene_vectors.npy` [14569]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14569 or target_col == 14569). Every well: [[SMIM31 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMIM31.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
