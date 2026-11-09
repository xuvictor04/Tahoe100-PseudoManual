---
symbol: "TPTEP1-1"
type: "gene"
col: 16473
ensembl_id: "ENSG00000290418"
name: ""
location: ""
module: 73
arm: "+"
pooled_cpm: 12.53
n_lines_expressing: 9
n_dd_up: 8
n_dd_down: 2
n_dd_up_clean: 3
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 9
direction_downstream: 45
tags: ["gene", "module/073"]
generated_by: "tahoemap"
---

# TPTEP1-1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.59× (z +12.6, q 2e-33, up in 1 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.50× (z +4.8, q 2e-04, up in 0 of 6 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.571× (z -4.9, q 7e-04, down in 4 of 7 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (LS 180 0.0490×, LoVo 0.117×, KATO III 0.0523×); [[Belinostat (drug)]] 5 µM in 3 lines (LS 180 0.0702×, LoVo 0.110×, KATO III 0.0701×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (LoVo 0.0642×, LS 180 0.0533×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (LoVo 0.134×, LS 180 0.165×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DSG4]] (+0.83, fdr 7e-06), [[NPSR1]] (+0.83, fdr 7e-06), [[CALB1]] (+0.83, fdr 7e-06).
> It is in [[Module 073]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[ERG]] → it (grade C ⚠); 45 go from it, the strongest it → [[TRABD2A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16473.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.59×** | +12.6 | 2e-33 | 1/5 (SNU-423) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.35×** | +10.4 | 1e-22 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.73×** | +8.0 | 3e-13 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +4.8 | 2e-04 | 0/6 | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.62×** | +4.1 | 0.004 | 3/7 (LoVo, SNU-423, …) | top dose only |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.62×** | +4.1 | 0.004 | 0/7 | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.52×** | +3.4 | 0.056 | 1/7 (KATO III) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.46×** | +3.2 | 0.082 | 0/7 | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 16473.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (LS 180 0.0490×, LoVo 0.117×, KATO III 0.0523×); [[Belinostat (drug)]] 5 µM in 3 lines (LS 180 0.0702×, LoVo 0.110×, KATO III 0.0701×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (LoVo 0.0642×, LS 180 0.0533×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (LoVo 0.134×, LS 180 0.165×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.571×** | -4.9 | 7e-04 | 4/7 (LS 180, LoVo, …) | top dose only | cell-cycle shift (explains ~7% here); position effect removed |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.651×** | -3.7 | 0.056 | 0/7 | inconsistent across doses |  |
| [[Erlotinib (drug)]] 0.05 µM |  | 0.651× | -3.4 | 0.11 | 2/7 (A-427, SNU-423) | inconsistent across doses |  |
| [[Benztropine (mesylate) (drug)]] 0.5 µM |  | 0.698× | -3.1 | 0.21 | 0/7 | inconsistent across doses |  |
| [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | 0.707× | -3.0 | 0.21 | 0/7 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16473. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 147 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0533× (z -20.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0490× (z -14.5) |
| [[LoVo (line)]] | wt | 193 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0642× (z -21.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.134× (z -15.4) |
| [[KATO III (line)]] | alt | 8.46 | 0 | 3 | — | [[Flumatinib (mesylate) (drug)]] 5 µM 0.0394× (z -10.4) |
| [[HOP62 (line)]] | alt | 28.4 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.165× (z -10.6) ⚠ transcription drop |
| [[NCI-H661 (line)]] | alt | 57.8 | 0 | 1 | — | [[Vandetanib (drug)]] 0.5 µM 0.0721× (z -9.4) |
| [[A-172 (line)]] | wt | 1.33 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 7.65 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.848 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.995 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.11 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.21 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.30 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.89 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.37 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.997 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.67 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.37 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.53 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.921 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.759 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.93 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.831 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 8.38 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.995 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.986 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.802 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.21 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.931 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.88 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.88 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 7.73 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.47 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.44 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.02 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16473), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DSG4]] | +0.83 | +0.86 / +0.72 | both halves | 7e-06 |  |
| [[NPSR1]] | +0.83 | +0.80 / +0.77 | both halves | 7e-06 |  |
| [[CALB1]] | +0.83 | +0.82 / +0.75 | both halves | 7e-06 |  |
| [[TPRXL]] | +0.81 | +0.80 / +0.78 | both halves | 7e-06 |  |
| [[HEPH]] | +0.80 | +0.81 / +0.68 | both halves | 7e-06 |  |
| [[FAM3D]] | +0.78 | +0.76 / +0.65 | both halves | 7e-06 |  |
| [[LINC02582]] | +0.78 | +0.80 / +0.77 | both halves | 7e-06 |  |
| [[CTSE]] | +0.75 | +0.79 / +0.58 | both halves | 8e-06 |  |
| [[SLC6A20]] | +0.75 | +0.73 / +0.67 | both halves | 7e-06 |  |
| [[GPA33]] | +0.74 | +0.77 / +0.62 | both halves | 7e-06 |  |
| [[LINC02474]] | +0.74 | +0.75 / +0.65 | both halves | 7e-06 |  |
| [[MUC17]] | +0.73 | +0.73 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 0, C 9.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ERG]] | C | ERG activity raises TPTEP1-1's level | lines that do not express ERG (30) vs lines expressing it (20) | 2.64× lower at baseline in the lines without ERG | 0.003 | ⚠ within organs, on part of the lines; also absent: FUT9, ZIC1, MDGA2; maybe low, not absent; co-absent with the target |
| [[MMP28]] | C | MMP28 activity raises TPTEP1-1's level | lines that do not express MMP28 (27) vs lines expressing it (23) | 1.95× lower at baseline in the lines without MMP28 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000285743, LINC02582, LINP1; maybe low, not absent; co-absent with the target |
| [[REG4]] | C | REG4 activity raises TPTEP1-1's level | lines that do not express REG4 (43) vs lines expressing it (7) | 5.82× lower at baseline in the lines without REG4 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, NPSR1, ENSG00000230975; co-absent with the target |
| [[MUC2]] | C | MUC2 activity raises TPTEP1-1's level | lines that do not express MUC2 (42) vs lines expressing it (8) | 3.38× lower at baseline in the lines without MUC2 | 0.053 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000248588, DSG4; co-absent with the target |
| [[CTSE]] | C | CTSE activity raises TPTEP1-1's level | lines that do not express CTSE (42) vs lines expressing it (8) | 3.61× lower at baseline in the lines without CTSE | 0.057 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000224322, REG4, CFTR; co-absent with the target |
| [[NPSR1]] | C | NPSR1 activity raises TPTEP1-1's level | lines that do not express NPSR1 (42) vs lines expressing it (8) | 4.49× lower at baseline in the lines without NPSR1 | 0.059 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, MUC17, CDH17; co-absent with the target |
| [[DSG4]] | C | DSG4 activity raises TPTEP1-1's level | lines that do not express DSG4 (45) vs lines expressing it (5) | 8.39× lower at baseline in the lines without DSG4 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, GPR15, ENSG00000237031; co-absent with the target |
| [[LINC02474]] | C | LINC02474 activity raises TPTEP1-1's level | lines that do not express LINC02474 (40) vs lines expressing it (10) | 3.94× lower at baseline in the lines without LINC02474 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC4, SFTPA2, ENSG00000230975; co-absent with the target |
| [[LINC02582]] | C | LINC02582 activity raises TPTEP1-1's level | lines that do not express LINC02582 (41) vs lines expressing it (9) | 3.40× lower at baseline in the lines without LINC02582 | 0.075 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, ENSG00000250920, ENSG00000230975; co-absent with the target |

### Downstream of this gene

*45 arrows, 45 of them with an alert ⚠; grade A 0, B 8, C 37. Shown: the 12 strongest; 33 more arrows (33 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRABD2A]] | B | TPTEP1-1 activity raises TRABD2A's level | lines that do not express TPTEP1-1 (41) vs lines expressing it (9) | 2.34× lower at baseline in the lines without TPTEP1-1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000283633, GCG, ENSG00000230975 |
| [[TLN2]] | B | TPTEP1-1 activity raises TLN2's level | lines that do not express TPTEP1-1 (41) vs lines expressing it (9) | 2.33× lower at baseline in the lines without TPTEP1-1 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000283633, GCG, ENSG00000230975 |
| [[PITPNM3]] | B | TPTEP1-1 activity raises PITPNM3's level | lines that do not express TPTEP1-1 (41) vs lines expressing it (9) | 1.93× lower at baseline in the lines without TPTEP1-1 | 0.066 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000283633, GCG, ENSG00000230975 |
| [[TLN2]] | B | TPTEP1-1 activity weakens TLN2's drug response | lines that do not express TPTEP1-1 (36) vs lines expressing it (7) | the lines without TPTEP1-1 respond 1.31× as strongly (z diff -1.67); strongest at Idarubicin (hydrochloride) 5 µM: 2.56x vs 1.15x (z diff -5.3) | 0.069 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000283633, GCG, ENSG00000230975; target measured in part of the lines; artifact flags |
| [[CFAP46]] | B | TPTEP1-1 activity raises CFAP46's level | lines that do not express TPTEP1-1 (41) vs lines expressing it (9) | 1.86× lower at baseline in the lines without TPTEP1-1 | 0.073 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000283633, GCG, ENSG00000230975 |
| [[ABHD12B]] | B | TPTEP1-1 activity raises ABHD12B's level | lines that do not express TPTEP1-1 (41) vs lines expressing it (9) | 1.98× lower at baseline in the lines without TPTEP1-1 | 0.098 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000283633, GCG, ENSG00000230975 |
| [[ALS2CL]] | B | TPTEP1-1 activity strengthens ALS2CL's drug response | lines that do not express TPTEP1-1 (29) vs lines expressing it (6) | the lines without TPTEP1-1 respond 0.49× as strongly (z diff +2.00); strongest at Digitoxin 0.5 µM: 0.76x vs 0.32x (z diff +4.9) | 0.099 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000283633, GCG, ENSG00000230975; target measured in part of the lines; artifact flags |
| [[IL1R2]] | B | TPTEP1-1 activity raises IL1R2's level | lines that do not express TPTEP1-1 (41) vs lines expressing it (9) | 2.06× lower at baseline in the lines without TPTEP1-1 | 0.0995 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000283633, GCG, ENSG00000230975 |
| [[REG4]] | C | TPTEP1-1 activity raises REG4's level | lines that do not express TPTEP1-1 (41) vs lines expressing it (9) | 3.00× lower at baseline in the lines without TPTEP1-1 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000283633, GCG, ENSG00000230975; co-absent with the target |
| [[HEPH]] | C | TPTEP1-1 activity raises HEPH's level | lines that do not express TPTEP1-1 (41) vs lines expressing it (9) | 3.75× lower at baseline in the lines without TPTEP1-1 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000283633, GCG, ENSG00000230975; co-absent with the target |
| [[CALB1]] | C | TPTEP1-1 activity raises CALB1's level | lines that do not express TPTEP1-1 (41) vs lines expressing it (9) | 3.51× lower at baseline in the lines without TPTEP1-1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000283633, GCG, ENSG00000230975; co-absent with the target |
| [[MUC2]] | C | TPTEP1-1 activity raises MUC2's level | lines that do not express TPTEP1-1 (41) vs lines expressing it (9) | 2.85× lower at baseline in the lines without TPTEP1-1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000283633, GCG, ENSG00000230975; co-absent with the target |

## Where it sits

- **Module**: [[Module 073]]; 66 genes; every member is in the + arm (projection on the module's main direction 0.846). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (18.9, 50.3); signed map (65.7, 7.9). **Vector** length 35.9, 16.4% of its response variance represented; |z| ≥ 3 in 166 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.6 | +10.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.5 | +12.6 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.4 | +2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.4 | +4.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.3 | +0.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +0.9 | +2.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.7 | +1.8 |
|  | [[Entrectinib (drug)]] 5 µM |  | +0.6 | +1.9 |
| fall | [[GSK1059615 (drug)]] 5 µM |  | -0.8 | -1.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.7 | -1.0 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.7 | -0.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -0.7 | -0.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.7 | -1.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -0.6 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.6 | -3.0 |

## What is on record

> [!warning] No registry record
> TPTEP1-1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 16473: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16473); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16473, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16473]; `tensor/DDL_lfc|DDL_z.npy` [16473]; `embed/gene_vectors.npy` [16473]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16473 or target_col == 16473). Every well: [[TPTEP1-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TPTEP1-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
