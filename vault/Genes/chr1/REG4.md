---
symbol: "REG4"
type: "gene"
col: 5520
ensembl_id: "ENSG00000134193"
name: "regenerating family member 4"
location: "1p12"
module: 73
arm: "+"
pooled_cpm: 3.38
n_lines_expressing: 7
n_dd_up: 15
n_dd_down: 3
n_dd_up_clean: 4
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 37
direction_downstream: 61
tags: ["gene", "module/073"]
generated_by: "tahoemap"
---

# REG4

*regenerating family member 4* — 1p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 11.9× (z +11.9, q 6e-30, up in 2 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.30× (z +5.7, q 2e-06, up in 1 of 4 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Erlotinib (drug)]] 0.05 µM: 0.414× (z -3.9, q 0.031, down in 0 of 5 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CTSE]] (+0.86, fdr 7e-06), [[PHGR1]] (+0.82, fdr 7e-06), [[GPA33]] (+0.75, fdr 7e-06).
> It is in [[Module 073]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 37 arrows point to it, the strongest [[LINC02582]] → it (grade C ⚠); 61 go from it, the strongest it → [[CALML4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 11 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5520.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **11.9×** | +11.9 | 6e-30 | 2/2 (LoVo, LS 180) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **9.86×** | +10.6 | 1e-23 | 2/2 (LoVo, LS 180) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **7.54×** | +9.0 | 6e-17 | 2/2 (LoVo, LS 180) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.71×** | +6.3 | 5e-08 | 3/3 (HT-29, LoVo, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.30×** | +5.7 | 2e-06 | 1/4 (KATO III) | top dose only | cell-cycle shift (explains ~2% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.10×** | +5.2 | 2e-05 | 0/2 | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.75×** | +4.9 | 1e-04 | 1/3 (KATO III) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~22% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **2.40×** | +4.2 | 0.002 | 0/5 | top dose only |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.88×** | +4.1 | 0.002 | 0/2 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **5.01×** | +4.0 | 0.003 | 0/1 | top dose only | noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.09×** | +3.5 | 0.021 | 0/3 | top dose only |  |
| [[Trifluridine (drug)]] 5 µM |  | **1.66×** | +3.4 | 0.029 | 2/5 (LS 180, LoVo) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.09×** | +3.4 | 0.030 | 0/5 | top dose only | cell-cycle shift (explains ~23% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.00×** | +3.2 | 0.055 | 0/5 | top dose only | cell-cycle shift (explains ~6% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.93×** | +3.2 | 0.060 | 0/3 | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5520.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Erlotinib (drug)]] 0.05 µM |  | **0.414×** | -3.9 | 0.031 | 0/5 | inconsistent across doses |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.419×** | -3.9 | 0.031 | 0/5 | inconsistent across doses |  |
| [[Pravastatin (sodium) (drug)]] 0.5 µM |  | **0.482×** | -3.5 | 0.085 | 0/5 | two highest doses |  |
| [[Benproperine (phosphate) (drug)]] 0.05 µM |  | 0.494× | -3.1 | 0.24 | 2/5 (LoVo, LS 180) | inconsistent across doses | position effect removed |
| [[OTS514 (drug)]] 0.05 µM | ⚠ transcription drop | 0.514× | -3.0 | 0.25 | 0/5 | inconsistent across doses | position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | 0.643× | -3.0 | 0.25 | 2/5 (LS 180, LoVo) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5520. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 64.4 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0972× (z -13.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.0584× (z -11.3) |
| [[LS 180 (line)]] | wt | 34.8 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0204× (z -23.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.00707× (z -21.1) |
| [[A-172 (line)]] | wt | 0.313 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.272 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.237 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.253 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.555 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.353 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.330 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.294 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.370 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.368 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.307 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.296 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.343 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.343 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.338 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.315 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.651 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.274 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.420 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.255 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.363 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.219 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.499 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.245 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.282 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.288 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.357 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.273 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.311 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.265 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.238 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.300 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.278 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.220 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.289 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.318 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.309 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.603 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.315 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.336 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.300 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.374 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.273 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5520), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTSE]] | +0.86 | +0.86 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[PHGR1]] | +0.82 | +0.74 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[GPA33]] | +0.75 | +0.69 / +0.70 | both halves | 7e-06 |  |
| [[MUC2]] | +0.72 | +0.69 / +0.74 | both halves | 7e-06 | STRING 608 |
| [[TPTEP1-1]] | +0.72 | +0.74 / +0.58 | both halves | 7e-06 |  |
| [[FAM3D]] | +0.72 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[PPP1R1B]] | +0.71 | +0.61 / +0.75 | both halves | 7e-06 |  |
| [[MUC6]] | +0.65 | +0.70 / +0.48 | both halves | 2e-05 | **novel candidate** |
| [[SPON1]] | +0.65 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[TFF2]] | +0.64 | +0.64 / +0.59 | both halves | 7e-06 | STRING 643 |
| [[CFTR]] | +0.64 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[DSG4]] | +0.63 | +0.72 / +0.36 | both halves | 9e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*37 arrows, 37 of them with an alert ⚠; grade A 0, B 0, C 37. Shown: the 12 strongest; 25 more arrows (25 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02582]] | C | LINC02582 activity raises REG4's level | lines that do not express LINC02582 (41) vs lines expressing it (9) | 3.36× lower at baseline in the lines without LINC02582 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, ENSG00000250920, ENSG00000230975; co-absent with the target |
| [[TPTEP1-1]] | C | TPTEP1-1 activity raises REG4's level | lines that do not express TPTEP1-1 (41) vs lines expressing it (9) | 3.00× lower at baseline in the lines without TPTEP1-1 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000283633, GCG, ENSG00000230975; co-absent with the target |
| [[MUC2]] | C | MUC2 activity raises REG4's level | lines that do not express MUC2 (42) vs lines expressing it (8) | 3.40× lower at baseline in the lines without MUC2 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000248588, DSG4; co-absent with the target |
| [[NPSR1]] | C | NPSR1 activity raises REG4's level | lines that do not express NPSR1 (42) vs lines expressing it (8) | 4.20× lower at baseline in the lines without NPSR1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, MUC17, CDH17; co-absent with the target |
| [[IL33]] | C | IL33 activity raises REG4's level | lines that do not express IL33 (35) vs lines expressing it (15) | 1.89× lower at baseline in the lines without IL33 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01133, MUC2, LINC01411; co-absent with the target |
| [[MMP28]] | C | MMP28 activity raises REG4's level | lines that do not express MMP28 (27) vs lines expressing it (23) | 1.62× lower at baseline in the lines without MMP28 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000285743, LINC02582, LINP1; maybe low, not absent; co-absent with the target |
| [[PLA2G2A]] | C | PLA2G2A activity raises REG4's level | lines that do not express PLA2G2A (41) vs lines expressing it (9) | 3.13× lower at baseline in the lines without PLA2G2A | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000248588, CALB1; co-absent with the target |
| [[ERG]] | C | ERG activity raises REG4's level | lines that do not express ERG (30) vs lines expressing it (20) | 1.49× lower at baseline in the lines without ERG | 0.013 | ⚠ within organs, on part of the lines; also absent: FUT9, ZIC1, MDGA2; maybe low, not absent; co-absent with the target |
| [[UGT1A1]] | C | UGT1A1 activity raises REG4's level | lines that do not express UGT1A1 (36) vs lines expressing it (14) | 2.33× lower at baseline in the lines without UGT1A1 | 0.018 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, NPSR1; co-absent with the target |
| [[CEACAM5]] | C | CEACAM5 activity raises REG4's level | lines that do not express CEACAM5 (39) vs lines expressing it (11) | 2.86× lower at baseline in the lines without CEACAM5 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, ENSG00000267881; co-absent with the target |
| [[CFTR]] | C | CFTR activity raises REG4's level | lines that do not express CFTR (39) vs lines expressing it (11) | 2.66× lower at baseline in the lines without CFTR | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CTSE, ENSG00000224322, ATP10B; maybe low, not absent; co-absent with the target |
| [[DSG4]] | C | DSG4 activity raises REG4's level | lines that do not express DSG4 (45) vs lines expressing it (5) | 6.04× lower at baseline in the lines without DSG4 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, GPR15, ENSG00000237031; co-absent with the target |

### Downstream of this gene

*61 arrows, 61 of them with an alert ⚠; grade A 0, B 4, C 57. Shown: the 12 strongest; 49 more arrows (49 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CALML4]] | B | REG4 activity raises CALML4's level | lines that do not express REG4 (43) vs lines expressing it (7) | 2.36× lower at baseline in the lines without REG4 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, NPSR1, ENSG00000230975 |
| [[SEPTIN9-DT]] | B | REG4 activity raises SEPTIN9-DT's level | lines that do not express REG4 (43) vs lines expressing it (7) | 2.80× lower at baseline in the lines without REG4 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, NPSR1, ENSG00000230975 |
| [[CALML4]] | B | REG4 activity weakens CALML4's drug response | lines that do not express REG4 (43) vs lines expressing it (5) | the lines without REG4 respond 1.57× as strongly (z diff -0.95); strongest at Homoharringtonine 5 µM: 1.38x vs 0.36x (z diff -9.6) | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, NPSR1, ENSG00000230975; target measured in part of the lines; both ways; artifact flags |
| [[SEMA4G]] | B | REG4 activity raises SEMA4G's level | lines that do not express REG4 (43) vs lines expressing it (7) | 2.07× lower at baseline in the lines without REG4 | 0.090 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, NPSR1, ENSG00000230975 |
| [[MUC17]] | C | REG4 activity raises MUC17's level | lines that do not express REG4 (43) vs lines expressing it (7) | 16.52× lower at baseline in the lines without REG4 | 4e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, NPSR1, ENSG00000230975; co-absent with the target |
| [[HEPH]] | C | REG4 activity raises HEPH's level | lines that do not express REG4 (43) vs lines expressing it (7) | 10.01× lower at baseline in the lines without REG4 | 7e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, NPSR1, ENSG00000230975; co-absent with the target |
| [[NPSR1]] | C | REG4 activity raises NPSR1's level | lines that do not express REG4 (43) vs lines expressing it (7) | 22.07× lower at baseline in the lines without REG4 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, NPSR1, ENSG00000230975; co-absent with the target |
| [[SLC6A20]] | C | REG4 activity raises SLC6A20's level | lines that do not express REG4 (43) vs lines expressing it (7) | 11.64× lower at baseline in the lines without REG4 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, NPSR1, ENSG00000230975; co-absent with the target |
| [[CEACAM5]] | C | REG4 activity raises CEACAM5's level | lines that do not express REG4 (43) vs lines expressing it (7) | 21.87× lower at baseline in the lines without REG4 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, NPSR1, ENSG00000230975; co-absent with the target |
| [[CFTR]] | C | REG4 activity raises CFTR's level | lines that do not express REG4 (43) vs lines expressing it (7) | 8.36× lower at baseline in the lines without REG4 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, NPSR1, ENSG00000230975; co-absent with the target |
| [[TSPAN8]] | C | REG4 activity raises TSPAN8's level | lines that do not express REG4 (43) vs lines expressing it (7) | 12.94× lower at baseline in the lines without REG4 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, NPSR1, ENSG00000230975; co-absent with the target |
| [[LGALS4]] | C | REG4 activity raises LGALS4's level | lines that do not express REG4 (43) vs lines expressing it (7) | 11.60× lower at baseline in the lines without REG4 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, NPSR1, ENSG00000230975; co-absent with the target |

## Where it sits

- **Module**: [[Module 073]]; 66 genes; every member is in the + arm (projection on the module's main direction 0.696). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (20.6, 50.1); signed map (65.8, 6.5). **Vector** length 25.2, 11.7% of its response variance represented; |z| ≥ 3 in 121 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.6 | +10.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.5 | +11.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.3 | +9.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +0.9 | +5.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +0.9 | +6.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.6 | +0.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.5 | +2.4 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +0.5 | +1.5 |
|  | [[Arbutin (drug)]] 0.05 µM |  | +0.4 | +1.3 |
|  | [[Entrectinib (drug)]] 5 µM |  | +0.4 | +1.7 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -0.8 | -1.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.7 | -0.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -0.7 | -1.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -0.6 | -0.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -0.6 | -0.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.6 | +0.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.6 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | regenerating family member 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p12 — chr1:119,794,017-119,811,580 (-) |
| Ensembl biotype | protein_coding |
| Also known as | REG-IV, RELP, GISP |
| Gene groups (HGNC) | C-type lectin domain containing; Regenerating family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BYZ8](https://www.uniprot.org/uniprotkb/Q9BYZ8) (Regenerating islet-derived protein 4):

> Calcium-independent lectin displaying mannose-binding specificity and able to maintain carbohydrate recognition activity in an acidic environment. May be involved in inflammatory and metaplastic responses of the gastrointestinal epithelium.

**Summary**, from NCBI Gene [83998](https://www.ncbi.nlm.nih.gov/gene/83998):

> Enables heparin binding activity and mannan binding activity. Predicted to act upstream of or within response to bacterium. Located in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:22977](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22977) · Entrez [83998](https://www.ncbi.nlm.nih.gov/gene/83998) · UniProt [Q9BYZ8](https://www.uniprot.org/uniprotkb/Q9BYZ8) · Ensembl [ENSG00000134193](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134193)

## Data

Gene col 5520: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5520); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5520, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5520]; `tensor/DDL_lfc|DDL_z.npy` [5520]; `embed/gene_vectors.npy` [5520]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5520 or target_col == 5520). Every well: [[REG4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/REG4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
