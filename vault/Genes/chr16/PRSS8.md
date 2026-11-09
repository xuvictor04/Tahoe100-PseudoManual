---
symbol: "PRSS8"
type: "gene"
col: 584
ensembl_id: "ENSG00000052344"
name: "serine protease 8"
location: "16p11.2"
module: 31
arm: "+"
pooled_cpm: 12.58
n_lines_expressing: 17
n_dd_up: 6
n_dd_down: 4
n_dd_up_clean: 1
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 53
direction_downstream: 84
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# PRSS8

*serine protease 8* — 16p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.91× (z +8.3, q 5e-14, up in 0 of 12 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 2.11× (z +3.5, q 0.044, up in 3 of 15 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 0.575× (z -4.3, q 0.010, down in 11 of 15 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CLDN7]] (+0.66, fdr 7e-06), [[RASSF7]] (+0.63, fdr 1e-05), [[FUT3]] (+0.63, fdr 7e-06); moves opposite to [[ZMYND11]] (-0.52, fdr 8e-05), [[ACADM]] (-0.51, fdr 1e-04), [[TRIM44]] (-0.50, fdr 5e-05).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 53 arrows point to it, the strongest [[LMTK3]] → it (grade B ⚠); 84 go from it, the strongest it → [[FAM83E]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 584.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.91×** | +8.3 | 5e-14 | 0/12 | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.07×** | +5.9 | 1e-06 | 0/14 | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.91×** | +4.8 | 2e-04 | 0/12 | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.67×** | +4.1 | 0.005 | 6/15 (Panc 03.27, COLO 205, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~23% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.11×** | +3.5 | 0.044 | 3/15 (Panc 03.27, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.54×** | +3.5 | 0.044 | 2/15 (HT-29, AsPC-1) | top dose only | cell-cycle shift (explains ~17% here); position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 1.47× | +3.1 | 0.16 | 5/15 (NCI-H2347, LS 180, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 584.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.575×** | -4.3 | 0.010 | 11/15 (NCI-H1573, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.621×** | -3.8 | 0.035 | 15/15 (NCI-H1573, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.623×** | -3.5 | 0.075 | 5/15 (NCI-H2347, HT-29, …) | inconsistent across doses | position effect removed |
| [[Allantoin (drug)]] 5 µM |  | **0.738×** | -3.5 | 0.075 | 0/15 | rises with dose | position effect removed |
| [[Encorafenib (drug)]] 5 µM |  | 0.478× | -3.1 | 0.16 | 0/15 | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.659× | -3.1 | 0.16 | 3/15 (CFPAC-1, BT-474, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.683× | -3.1 | 0.16 | 5/15 (AsPC-1, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[BAY1125976 (drug)]] 5 µM |  | 0.487× | -3.0 | 0.16 | 2/15 (HEC-1-A, HepG2/C3A) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | 0.688× | -3.0 | 0.16 | 9/15 (CFPAC-1, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 584. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 43.7 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0351× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.162× (z -10.1) |
| [[CFPAC-1 (line)]] | alt | 132 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0813× (z -24.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.163× (z -12.3) |
| [[HT-29 (line)]] | alt | 39.7 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0558× (z -19.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 29.5 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0840× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.220× (z -9.1) |
| [[HCT15 (line)]] | alt | 43.8 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.162× (z -14.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.194× (z -8.6) |
| [[KATO III (line)]] | alt | 39.8 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0460× (z -19.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 30.6 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0926× (z -19.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0449× (z -17.6) |
| [[NCI-H2347 (line)]] | alt | 41.9 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.186× (z -11.8) |
| [[SW1417 (line)]] | alt | 35.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.185× (z -10.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 22.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.149× (z -11.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 24.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.162× (z -10.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 1.96 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.643 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.66 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.560 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 7.82 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.788 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.612 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.907 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.781 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.730 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.756 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.665 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.877 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.851 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.898 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.911 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.602 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.534 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.599 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.591 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.615 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.528 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.699 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.610 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.692 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.670 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.840 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.749 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.622 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 584), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLDN7]] | +0.66 | +0.70 / +0.59 | both halves | 7e-06 | STRING 586 |
| [[RASSF7]] | +0.63 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[FUT3]] | +0.63 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[S100P]] | +0.63 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[GALNT3]] | +0.62 | +0.60 / +0.57 | both halves | 8e-06 |  |
| [[FAM83A]] | +0.62 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[S100A14]] | +0.62 | +0.70 / +0.41 | both halves | 4e-05 |  |
| [[TTC9]] | +0.61 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[CORO2A]] | +0.60 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[RAB25]] | +0.60 | +0.69 / +0.43 | both halves | 3e-05 | STRING 614 |
| [[TMPRSS4]] | +0.60 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[ELMO3]] | +0.60 | +0.64 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZMYND11]] | -0.52 | -0.41 / -0.37 | both halves | 8e-05 |  |
| [[ACADM]] | -0.51 | -0.44 / -0.35 | both halves | 1e-04 |  |
| [[TRIM44]] | -0.50 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[TSTD2]] | -0.49 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[ZMPSTE24]] | -0.49 | -0.33 / -0.46 | both halves | 1e-04 |  |
| [[RCBTB2]] | -0.49 | -0.44 / -0.30 | both halves | 2e-04 |  |
| [[SDCBP2-AS1]] | -0.48 | -0.40 / -0.39 | both halves | 6e-05 |  |
| [[ME3]] | -0.47 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[MCM3AP]] | -0.47 | -0.29 / -0.37 | both halves | 2e-04 |  |
| [[ATE1]] | -0.47 | -0.36 / -0.39 | both halves | 1e-04 |  |
| [[OXCT1]] | -0.47 | -0.38 / -0.37 | both halves | 7e-05 |  |
| [[TMEM80]] | -0.47 | -0.48 / -0.24 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*53 arrows, 53 of them with an alert ⚠; grade A 0, B 3, C 50. Shown: the 12 strongest; 41 more arrows (41 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LMTK3]] | B | LMTK3 activity raises PRSS8's level | lines that do not express LMTK3 (15) vs lines expressing it (35) | 3.54× lower at baseline in the lines without LMTK3 | 0.033 | ⚠ within organs, on part of the lines; also absent: CRYBG2, CXADR, CCDC120; maybe low, not absent |
| [[SEMA3B]] | B | SEMA3B activity raises PRSS8's level | lines that do not express SEMA3B (19) vs lines expressing it (31) | 2.92× lower at baseline in the lines without SEMA3B | 0.046 | ⚠ within organs, on part of the lines; also absent: SERPINA1, CSF1R, TNNT2; maybe low, not absent |
| [[TMC6]] | B | TMC6 activity raises PRSS8's level | lines that do not express TMC6 (12) vs lines expressing it (38) | 3.52× lower at baseline in the lines without TMC6 | 0.090 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, FGFR4, LSR |
| [[RAB25]] | C | RAB25 activity raises PRSS8's level | lines that do not express RAB25 (33) vs lines expressing it (17) | 13.51× lower at baseline in the lines without RAB25 | 5e-06 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, TMEM30B, PRSS8; co-absent with the target |
| [[TMPRSS4]] | C | TMPRSS4 activity raises PRSS8's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 13.07× lower at baseline in the lines without TMPRSS4 | 6e-06 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B; co-absent with the target |
| [[CDH1]] | C | CDH1 activity raises PRSS8's level | lines that do not express CDH1 (31) vs lines expressing it (19) | 11.51× lower at baseline in the lines without CDH1 | 1e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST14, LAD1, KDF1; co-absent with the target |
| [[S100A14]] | C | S100A14 activity raises PRSS8's level | lines that do not express S100A14 (33) vs lines expressing it (17) | 12.22× lower at baseline in the lines without S100A14 | 2e-05 | ⚠ within organs, on part of the lines; also absent: PRSS8, RAB25, TMPRSS4; co-absent with the target |
| [[ATP2C2]] | C | ATP2C2 activity raises PRSS8's level | lines that do not express ATP2C2 (32) vs lines expressing it (18) | 10.01× lower at baseline in the lines without ATP2C2 | 3e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, GRHL2, ST14; co-absent with the target |
| [[TMEM125]] | C | TMEM125 activity raises PRSS8's level | lines that do not express TMEM125 (33) vs lines expressing it (17) | 11.24× lower at baseline in the lines without TMEM125 | 3e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ATP2C2, ST14; co-absent with the target |
| [[MPZL2]] | C | MPZL2 activity raises PRSS8's level | lines that do not express MPZL2 (29) vs lines expressing it (21) | 9.08× lower at baseline in the lines without MPZL2 | 5e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, IRF6, ST14; co-absent with the target |
| [[FAM83B]] | C | FAM83B activity raises PRSS8's level | lines that do not express FAM83B (30) vs lines expressing it (20) | 8.63× lower at baseline in the lines without FAM83B | 6e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, GRHL2, ST14; co-absent with the target |
| [[ESRP1]] | C | ESRP1 activity raises PRSS8's level | lines that do not express ESRP1 (31) vs lines expressing it (19) | 9.67× lower at baseline in the lines without ESRP1 | 7e-05 | ⚠ within organs, on part of the lines; also absent: ST14, KDF1, CLDN7; co-absent with the target |

### Downstream of this gene

*84 arrows, 84 of them with an alert ⚠; grade A 0, B 34, C 50. Shown: the 12 strongest; 72 more arrows (72 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM83E]] | B | PRSS8 activity raises FAM83E's level | lines that do not express PRSS8 (33) vs lines expressing it (17) | 4.77× lower at baseline in the lines without PRSS8 | 2e-04 | ⚠ within organs, on part of the lines; also absent: RAB25, TMPRSS4, LCN2 |
| [[ELMO3]] | B | PRSS8 activity raises ELMO3's level | lines that do not express PRSS8 (33) vs lines expressing it (17) | 2.65× lower at baseline in the lines without PRSS8 | 7e-04 | ⚠ within organs, on part of the lines; also absent: RAB25, TMPRSS4, LCN2 |
| [[TMC6]] | B | PRSS8 activity raises TMC6's level | lines that do not express PRSS8 (33) vs lines expressing it (17) | 4.60× lower at baseline in the lines without PRSS8 | 0.001 | ⚠ within organs, on part of the lines; also absent: RAB25, TMPRSS4, LCN2 |
| [[PTK2B]] | B | PRSS8 activity raises PTK2B's level | lines that do not express PRSS8 (33) vs lines expressing it (17) | 3.51× lower at baseline in the lines without PRSS8 | 0.001 | ⚠ within organs, on part of the lines; also absent: RAB25, TMPRSS4, LCN2 |
| [[LMTK3]] | B | PRSS8 activity raises LMTK3's level | lines that do not express PRSS8 (33) vs lines expressing it (17) | 3.51× lower at baseline in the lines without PRSS8 | 0.002 | ⚠ within organs, on part of the lines; also absent: RAB25, TMPRSS4, LCN2 |
| [[SEMA3B]] | B | PRSS8 activity raises SEMA3B's level | lines that do not express PRSS8 (33) vs lines expressing it (17) | 4.03× lower at baseline in the lines without PRSS8 | 0.003 | ⚠ within organs, on part of the lines; also absent: RAB25, TMPRSS4, LCN2 |
| [[RASSF7]] | B | PRSS8 activity raises RASSF7's level | lines that do not express PRSS8 (33) vs lines expressing it (17) | 2.64× lower at baseline in the lines without PRSS8 | 0.003 | ⚠ within organs, on part of the lines; also absent: RAB25, TMPRSS4, LCN2 |
| [[RAB11FIP1]] | B | PRSS8 activity raises RAB11FIP1's level | lines that do not express PRSS8 (33) vs lines expressing it (17) | 3.01× lower at baseline in the lines without PRSS8 | 0.004 | ⚠ within organs, on part of the lines; also absent: RAB25, TMPRSS4, LCN2 |
| [[MKNK2]] | B | PRSS8 activity raises MKNK2's level | lines that do not express PRSS8 (33) vs lines expressing it (17) | 1.74× lower at baseline in the lines without PRSS8 | 0.010 | ⚠ within organs, on part of the lines; also absent: RAB25, TMPRSS4, LCN2 |
| [[PHF10]] | B | PRSS8 activity lowers PHF10's level | lines that do not express PRSS8 (33) vs lines expressing it (17) | 1.44× higher at baseline in the lines without PRSS8 | 0.030 | ⚠ within organs, on part of the lines; also absent: RAB25, TMPRSS4, LCN2 |
| [[TSC22D2]] | B | PRSS8 activity raises TSC22D2's level | lines that do not express PRSS8 (33) vs lines expressing it (17) | 1.61× lower at baseline in the lines without PRSS8 | 0.033 | ⚠ within organs, on part of the lines; also absent: RAB25, TMPRSS4, LCN2 |
| [[ACADM]] | B | PRSS8 activity lowers ACADM's level | lines that do not express PRSS8 (33) vs lines expressing it (17) | 1.59× higher at baseline in the lines without PRSS8 | 0.037 | ⚠ within organs, on part of the lines; also absent: RAB25, TMPRSS4, LCN2 |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.563). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (19.4, 59.7); signed map (71.1, 9.4). **Vector** length 64.9, 26.0% of its response variance represented; |z| ≥ 3 in 340 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | +0.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | -0.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | +0.3 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +1.7 | +4.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.5 | +1.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.4 | +2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.4 | +2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.3 | +0.6 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.3 | +2.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.3 | +2.5 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.1 | -3.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.7 | -2.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -1.7 | -4.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.6 | -2.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.3 | -2.6 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.3 | -1.8 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.3 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | serine protease 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p11.2 — chr16:31,131,433-31,135,727 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CAP1 |
| Gene groups (HGNC) | Serine proteases |
| Reactome | 2 pathways, smallest: Formation of the cornified envelope; Keratinization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16651](https://www.uniprot.org/uniprotkb/Q16651) (Prostasin):

> Possesses a trypsin-like cleavage specificity with a preference for poly-basic substrates. Stimulates epithelial sodium channel (ENaC) activity through activating cleavage of the gamma subunits (SCNN1G).

**Summary**, from NCBI Gene [5652](https://www.ncbi.nlm.nih.gov/gene/5652):

> This gene encodes a member of the peptidase S1 or chymotrypsin family of serine proteases. The encoded preproprotein is proteolytically processed to generate light and heavy chains that associate via a disulfide bond to form the heterodimeric enzyme. This enzyme is highly expressed in prostate epithelia and is one of several proteolytic enzymes found in seminal fluid. This protease exhibits trypsin-like substrate specificity, cleaving protein substrates at the carboxyl terminus of lysine or …

**Accessions** — [HGNC:9491](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9491) · Entrez [5652](https://www.ncbi.nlm.nih.gov/gene/5652) · UniProt [Q16651](https://www.uniprot.org/uniprotkb/Q16651) · Ensembl [ENSG00000052344](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000052344)

## Data

Gene col 584: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 584); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 584, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 584]; `tensor/DDL_lfc|DDL_z.npy` [584]; `embed/gene_vectors.npy` [584]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 584 or target_col == 584). Every well: [[PRSS8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRSS8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
