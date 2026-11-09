---
symbol: "SPON1"
type: "gene"
col: 15391
ensembl_id: "ENSG00000262655"
name: "spondin 1"
location: "11p15.2"
module: 73
arm: "+"
pooled_cpm: 24.26
n_lines_expressing: 11
n_dd_up: 10
n_dd_down: 2
n_dd_up_clean: 5
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 40
direction_downstream: 47
tags: ["gene", "module/073"]
generated_by: "tahoemap"
---

# SPON1

*spondin 1* — 11p15.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.44× (z +12.0, q 2e-30, up in 6 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.18× (z +10.7, q 4e-24, up in 2 of 9 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.568× (z -5.5, q 2e-05, down in 9 of 9 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 3 lines (LoVo 0.0274×, LS 180 0.118×, SW48 0.0240×; ⚠ cell-cycle shift, explains ~7% of this change); [[Belinostat (drug)]] 5 µM in 3 lines (LoVo 0.0520×, LS 180 0.139×, SW48 0.0378×); [[Panobinostat (drug)]] 0.5 µM in 2 lines (LoVo 0.0462×, LS 180 0.146×); [[Ixazomib citrate (drug)]] 0.5 µM in 2 lines (LS 180 0.144×, LoVo 0.249×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC6A20]] (+0.81, fdr 7e-06), [[DSG4]] (+0.76, fdr 7e-06), [[CALB1]] (+0.74, fdr 7e-06).
> It is in [[Module 073]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 40 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 47 go from it, the strongest it → [[JPH1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15391.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.44×** | +12.0 | 2e-30 | 6/9 (AsPC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.18×** | +10.7 | 4e-24 | 2/9 (C32, SW480) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.91×** | +10.0 | 4e-21 | 4/7 (HEC-1-A, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.67×** | +8.8 | 1e-16 | 2/8 (HEC-1-A, Panc 03.27) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +5.1 | 5e-05 | 1/9 (HEC-1-A) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.40×** | +4.6 | 3e-04 | 1/9 (C32) | rises with dose | composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.20×** | +4.0 | 0.005 | 2/3 (HEC-1-A, AsPC-1) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +3.7 | 0.017 | 1/9 (SW480) | rises with dose |  |
| [[Ixazomib (drug)]] 0.05 µM |  | **1.43×** | +3.3 | 0.058 | 0/9 | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +3.2 | 0.073 | 0/9 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Temsirolimus (drug)]] 5 µM |  | 1.25× | +3.0 | 0.12 | 3/9 (SW480, LS 180, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15391.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 3 lines (LoVo 0.0274×, LS 180 0.118×, SW48 0.0240×; ⚠ cell-cycle shift, explains ~7% of this change); [[Belinostat (drug)]] 5 µM in 3 lines (LoVo 0.0520×, LS 180 0.139×, SW48 0.0378×); [[Panobinostat (drug)]] 0.5 µM in 2 lines (LoVo 0.0462×, LS 180 0.146×); [[Ixazomib citrate (drug)]] 0.5 µM in 2 lines (LS 180 0.144×, LoVo 0.249×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.568×** | -5.5 | 2e-05 | 9/9 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.610×** | -4.4 | 0.003 | 5/9 (LoVo, SW480, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | 0.713× | -3.3 | 0.20 | 9/9 (LoVo, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15391. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 350 | 0 | 10 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0274× (z -22.6) ⚠ cell-cycle shift, explains ~7% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0462× (z -19.3) |
| [[LS 180 (line)]] | wt | 243 | 0 | 9 (5 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0852× (z -15.7) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.139× (z -12.6) |
| [[SW48 (line)]] | wt | 62.9 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0240× (z -11.4) ⚠ cell-cycle shift, explains ~7% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0378× (z -10.0) |
| [[Hs 766T (line)]] | wt | 33.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -11.1) ⚠ cell-cycle shift, explains ~48% of this change |
| [[A-172 (line)]] | wt | 2.88 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.32 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.39 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.54 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.45 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.73 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.92 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 6.55 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.96 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.88 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.65 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.90 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.31 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.35 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.74 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.47 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.45 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.47 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.66 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.57 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.25 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.97 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.45 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.48 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.99 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.36 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.61 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 4.32 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.88 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.28 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.79 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.50 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.11 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.35 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.86 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.19 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.72 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 3.19 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.85 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 5.30 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 7.28 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15391), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC6A20]] | +0.81 | +0.79 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[DSG4]] | +0.76 | +0.70 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[CALB1]] | +0.74 | +0.74 / +0.67 | both halves | 7e-06 |  |
| [[CTSE]] | +0.72 | +0.64 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[LINC02474]] | +0.71 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[HEPH]] | +0.71 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[LINC02582]] | +0.70 | +0.69 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[NPSR1]] | +0.68 | +0.58 / +0.68 | both halves | 8e-06 |  |
| [[GPA33]] | +0.67 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[FAM3D]] | +0.67 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[TPTEP1-1]] | +0.66 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[IGFL2]] | +0.66 | +0.76 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*40 arrows, 40 of them with an alert ⚠; grade A 0, B 1, C 39. Shown: the 12 strongest; 28 more arrows (28 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SPON1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[LINC02582]] | C | LINC02582 activity raises SPON1's level | lines that do not express LINC02582 (41) vs lines expressing it (9) | 6.85× lower at baseline in the lines without LINC02582 | 7e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, ENSG00000250920, ENSG00000230975; co-absent with the target |
| [[DSG4]] | C | DSG4 activity raises SPON1's level | lines that do not express DSG4 (45) vs lines expressing it (5) | 14.52× lower at baseline in the lines without DSG4 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, GPR15, ENSG00000237031; co-absent with the target |
| [[FGFBP1]] | C | FGFBP1 activity raises SPON1's level | lines that do not express FGFBP1 (36) vs lines expressing it (14) | 4.99× lower at baseline in the lines without FGFBP1 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: COL17A1, KLK10, SERPINB5; co-absent with the target |
| [[EDAR]] | C | EDAR activity raises SPON1's level | lines that do not express EDAR (36) vs lines expressing it (14) | 4.80× lower at baseline in the lines without EDAR | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: EPS8L3, KLK10, DSG3; co-absent with the target |
| [[MMP28]] | C | MMP28 activity raises SPON1's level | lines that do not express MMP28 (27) vs lines expressing it (23) | 2.05× lower at baseline in the lines without MMP28 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000285743, LINC02582, LINP1; maybe low, not absent; co-absent with the target |
| [[LGR6]] | C | LGR6 activity raises SPON1's level | lines that do not express LGR6 (35) vs lines expressing it (15) | 3.92× lower at baseline in the lines without LGR6 | 0.009 | ⚠ within organs, on part of the lines; also absent: SLC6A20, LINC01559, VWA2; co-absent with the target |
| [[REG4]] | C | REG4 activity raises SPON1's level | lines that do not express REG4 (43) vs lines expressing it (7) | 5.96× lower at baseline in the lines without REG4 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, NPSR1, ENSG00000230975; co-absent with the target |
| [[LINC01819]] | C | LINC01819 activity raises SPON1's level | lines that do not express LINC01819 (29) vs lines expressing it (21) | 3.27× lower at baseline in the lines without LINC01819 | 0.014 | ⚠ within organs, on part of the lines; also absent: MOGAT3, LGR6, A1CF; maybe low, not absent; co-absent with the target |
| [[MUC2]] | C | MUC2 activity raises SPON1's level | lines that do not express MUC2 (42) vs lines expressing it (8) | 5.22× lower at baseline in the lines without MUC2 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000248588, DSG4; co-absent with the target |
| [[XACT]] | C | XACT activity raises SPON1's level | lines that do not express XACT (30) vs lines expressing it (20) | 1.75× lower at baseline in the lines without XACT | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000248515, ENSG00000267284, LINC02438; co-absent with the target |
| [[UGT1A1]] | C | UGT1A1 activity raises SPON1's level | lines that do not express UGT1A1 (36) vs lines expressing it (14) | 2.93× lower at baseline in the lines without UGT1A1 | 0.017 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, NPSR1; co-absent with the target |

### Downstream of this gene

*47 arrows, 47 of them with an alert ⚠; grade A 0, B 10, C 37. Shown: the 12 strongest; 35 more arrows (35 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[JPH1]] | B | SPON1 activity raises JPH1's level | lines that do not express SPON1 (39) vs lines expressing it (11) | 2.53× lower at baseline in the lines without SPON1 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALB1, DSG4, KRT6A |
| [[INPP1]] | B | SPON1 activity raises INPP1's level | lines that do not express SPON1 (39) vs lines expressing it (11) | 2.82× lower at baseline in the lines without SPON1 | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALB1, DSG4, KRT6A |
| [[ZNG1E]] | B | SPON1 activity raises ZNG1E's level | lines that do not express SPON1 (39) vs lines expressing it (11) | 1.30× lower at baseline in the lines without SPON1 | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALB1, DSG4, KRT6A |
| [[IGSF9]] | B | SPON1 activity raises IGSF9's level | lines that do not express SPON1 (39) vs lines expressing it (11) | 1.94× lower at baseline in the lines without SPON1 | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALB1, DSG4, KRT6A |
| [[LINC02595]] | B | SPON1 activity strengthens LINC02595's drug response | lines that do not express SPON1 (30) vs lines expressing it (8) | the lines without SPON1 respond 0.51× as strongly (z diff +2.30); strongest at Panobinostat 5 µM: 0.42x vs 0.17x (z diff +5.2) | 0.076 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALB1, DSG4, KRT6A; target measured in part of the lines; artifact flags |
| [[PITPNM3]] | B | SPON1 activity raises PITPNM3's level | lines that do not express SPON1 (39) vs lines expressing it (11) | 1.70× lower at baseline in the lines without SPON1 | 0.088 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALB1, DSG4, KRT6A |
| [[SH2D4A]] | B | SPON1 activity raises SH2D4A's level | lines that do not express SPON1 (39) vs lines expressing it (11) | 2.26× lower at baseline in the lines without SPON1 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALB1, DSG4, KRT6A |
| [[TRABD2A]] | B | SPON1 activity raises TRABD2A's level | lines that do not express SPON1 (39) vs lines expressing it (11) | 1.83× lower at baseline in the lines without SPON1 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALB1, DSG4, KRT6A |
| [[BAG1]] | B | SPON1 activity raises BAG1's level | lines that do not express SPON1 (39) vs lines expressing it (11) | 1.71× lower at baseline in the lines without SPON1 | 0.090 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALB1, DSG4, KRT6A |
| [[B4GALNT3]] | B | SPON1 activity raises B4GALNT3's level | lines that do not express SPON1 (39) vs lines expressing it (11) | 2.90× lower at baseline in the lines without SPON1 | 0.091 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALB1, DSG4, KRT6A |
| [[CALB1]] | C | SPON1 activity raises CALB1's level | lines that do not express SPON1 (39) vs lines expressing it (11) | 6.26× lower at baseline in the lines without SPON1 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALB1, DSG4, KRT6A; co-absent with the target |
| [[KIAA0040]] | C | SPON1 activity raises KIAA0040's level | lines that do not express SPON1 (39) vs lines expressing it (11) | 6.06× lower at baseline in the lines without SPON1 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALB1, DSG4, KRT6A; co-absent with the target |

## Where it sits

- **Module**: [[Module 073]]; 66 genes; every member is in the + arm (projection on the module's main direction 0.813). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (18.4, 50.1); signed map (66.1, 8.0). **Vector** length 49.6, 22.7% of its response variance represented; |z| ≥ 3 in 262 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.2 | +8.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.1 | +12.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.9 | +10.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.4 | +10.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +2.0 | +5.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +2.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.2 | +2.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.2 | +1.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.1 | +3.7 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +0.8 | +0.5 |
| fall | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -4.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.1 | -1.4 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.0 | -2.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.0 | -3.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.0 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | spondin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.2 — chr11:13,962,723-14,268,133 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0762, f-spondin |
| Hallmark sets | KRAS_SIGNALING_UP |
| Reactome | 6 pathways, smallest: Defective B3GALTL causes PpS; O-glycosylation of TSR domain-containing proteins; Diseases associated with O-glycosylation of proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HCB6](https://www.uniprot.org/uniprotkb/Q9HCB6) (Spondin-1):

> Cell adhesion protein that promotes the attachment of spinal cord and sensory neuron cells and the outgrowth of neurites in vitro. May contribute to the growth and guidance of axons in both the spinal cord and the PNS (By similarity). Major factor for vascular smooth muscle cell.

**Summary**, from NCBI Gene [10418](https://www.ncbi.nlm.nih.gov/gene/10418):

> Predicted to be an extracellular matrix structural constituent. Predicted to be involved in cell adhesion. Predicted to act upstream of or within negative regulation of amyloid-beta formation; positive regulation of amyloid precursor protein catabolic process; and positive regulation of protein processing. Located in extracellular matrix and obsolete extracellular space. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:11252](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11252) · Entrez [10418](https://www.ncbi.nlm.nih.gov/gene/10418) · UniProt [Q9HCB6](https://www.uniprot.org/uniprotkb/Q9HCB6) · Ensembl [ENSG00000262655](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000262655)

## Data

Gene col 15391: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15391); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15391, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15391]; `tensor/DDL_lfc|DDL_z.npy` [15391]; `embed/gene_vectors.npy` [15391]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15391 or target_col == 15391). Every well: [[SPON1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPON1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
