---
symbol: "MUC6"
type: "gene"
col: 11596
ensembl_id: "ENSG00000184956"
name: "mucin 6, oligomeric mucus/gel-forming (gene/pseudogene)"
location: "11p15.5"
module: 44
arm: "+"
pooled_cpm: 16.47
n_lines_expressing: 5
n_dd_up: 11
n_dd_down: 0
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 16
direction_downstream: 43
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# MUC6

*mucin 6, oligomeric mucus/gel-forming (gene/pseudogene)* — 11p15.5

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 8.96× (z +11.5, q 1e-27, up in 2 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.56× (z +9.4, q 1e-18, up in 1 of 3 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (LS 180 0.134×; ⚠ cell-cycle shift, explains ~57% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (LS 180 0.0631×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[REG4]] (+0.65, fdr 2e-05), [[PHGR1]] (+0.60, fdr 1e-05), [[YBX2]] (+0.58, fdr 1e-05); moves opposite to [[N4BP1]] (-0.42, fdr 4e-04).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[AHSG]] → it (grade C ⚠); 43 go from it, the strongest it → [[ENPP3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11596.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **8.96×** | +11.5 | 1e-27 | 2/2 (LS 180, BT-474) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **7.09×** | +9.8 | 2e-20 | 2/2 (BT-474, LS 180) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.56×** | +9.4 | 1e-18 | 1/3 (BT-474) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.16×** | +6.9 | 1e-09 | 2/2 (LS 180, BT-474) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **5.08×** | +4.4 | 0.001 | 1/2 (BT-474) | top dose only | noisy plate (z scaled); position effect removed |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **2.81×** | +4.3 | 0.001 | 0/3 | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **2.23×** | +4.2 | 0.002 | 1/3 (LS 180) | inconsistent across doses | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.21×** | +4.1 | 0.003 | 1/3 (BT-474) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~23% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.64×** | +3.6 | 0.017 | 0/3 | top dose only | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.90×** | +3.4 | 0.045 | 0/3 | top dose only | cell-cycle shift (explains ~24% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.54×** | +3.2 | 0.075 | 0/3 | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11596.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (LS 180 0.134×; ⚠ cell-cycle shift, explains ~57% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (LS 180 0.0631×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Futibatinib (drug)]] 0.05 µM |  | 0.481× | -3.6 | 0.17 | 0/3 | inconsistent across doses | position effect removed |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | 0.664× | -3.0 | 0.48 | 2/3 (SHP-77, LS 180) | inconsistent across doses | position effect removed |
| [[Ivabradine (hydrochloride) (drug)]] 5 µM | ⚠ unreliable plate only | 0.563× | -3.0 | 0.48 | 0/3 | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11596. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 547 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -10.0) ⚠ cell-cycle shift, explains ~57% of this change |
| [[A-172 (line)]] | wt | 1.30 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.935 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.961 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.67 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 156 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.977 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.58 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.25 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.59 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.75 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.56 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.984 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.903 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.959 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.33 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.73 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.58 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.18 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11596), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[REG4]] | +0.65 | +0.70 / +0.48 | both halves | 2e-05 | **novel candidate** |
| [[PHGR1]] | +0.60 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[YBX2]] | +0.58 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[GPA33]] | +0.57 | +0.60 / +0.46 | both halves | 3e-05 |  |
| [[PIGR]] | +0.55 | +0.58 / +0.33 | both halves | 1e-04 |  |
| [[CTSE]] | +0.54 | +0.63 / +0.33 | both halves | 1e-04 |  |
| [[TFF3]] | +0.54 | +0.44 / +0.57 | both halves | 3e-05 | STRING 695 |
| [[PLA2G2A]] | +0.53 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[MYB]] | +0.52 | +0.37 / +0.49 | both halves | 8e-05 |  |
| [[FGFR4]] | +0.51 | +0.47 / +0.46 | both halves | 3e-05 |  |
| [[FAM3D]] | +0.51 | +0.57 / +0.36 | both halves | 9e-05 |  |
| [[ST6GALNAC1]] | +0.51 | +0.53 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[N4BP1]] | -0.42 | -0.46 / -0.26 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 0, C 16. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AHSG]] | C | AHSG activity raises MUC6's level | lines that do not express AHSG (45) vs lines expressing it (5) | 2.14× lower at baseline in the lines without AHSG | 0.003 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53, KRAS; also absent: APOA2, APOB, CALCA; co-absent with the target |
| [[PLA2G2A]] | C | PLA2G2A activity raises MUC6's level | lines that do not express PLA2G2A (41) vs lines expressing it (9) | 4.59× lower at baseline in the lines without PLA2G2A | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000248588, CALB1; co-absent with the target |
| [[TFF3]] | C | TFF3 activity raises MUC6's level | lines that do not express TFF3 (38) vs lines expressing it (12) | 3.59× lower at baseline in the lines without TFF3 | 0.034 | ⚠ within organs, on part of the lines; also absent: CEACAM5, MUC17, AGR3; co-absent with the target |
| [[MUC17]] | C | MUC17 activity raises MUC6's level | lines that do not express MUC17 (44) vs lines expressing it (6) | 4.45× lower at baseline in the lines without MUC17 | 0.035 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, FGFR2, NPSR1; co-absent with the target |
| [[REG4]] | C | REG4 activity raises MUC6's level | lines that do not express REG4 (43) vs lines expressing it (7) | 3.81× lower at baseline in the lines without REG4 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, NPSR1, ENSG00000230975; co-absent with the target |
| [[ERG]] | C | ERG activity raises MUC6's level | lines that do not express ERG (30) vs lines expressing it (20) | 2.22× lower at baseline in the lines without ERG | 0.056 | ⚠ within organs, on part of the lines; also absent: FUT9, ZIC1, MDGA2; maybe low, not absent; co-absent with the target |
| [[TCN1]] | C | TCN1 activity raises MUC6's level | lines that do not express TCN1 (37) vs lines expressing it (13) | 2.76× lower at baseline in the lines without TCN1 | 0.062 | ⚠ within organs, on part of the lines; also absent: AGR3, MUC5AC, MUC5B; co-absent with the target |
| [[SMOC2]] | C | SMOC2 activity raises MUC6's level | lines that do not express SMOC2 (33) vs lines expressing it (17) | 2.60× lower at baseline in the lines without SMOC2 | 0.066 | ⚠ within organs, on part of the lines; also absent: LINC01456, TFF3, MIR3667HG; maybe low, not absent; co-absent with the target |
| [[AGR3]] | C | AGR3 activity raises MUC6's level | lines that do not express AGR3 (42) vs lines expressing it (8) | 5.38× lower at baseline in the lines without AGR3 | 0.070 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGFR2, GABRP, MUC17; co-absent with the target |
| [[TPTEP1-1]] | C | TPTEP1-1 activity raises MUC6's level | lines that do not express TPTEP1-1 (41) vs lines expressing it (9) | 2.62× lower at baseline in the lines without TPTEP1-1 | 0.074 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000283633, GCG, ENSG00000230975; co-absent with the target |
| [[PIGR]] | C | PIGR activity raises MUC6's level | lines that do not express PIGR (45) vs lines expressing it (5) | 6.04× lower at baseline in the lines without PIGR | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, TM4SF4, APOB; co-absent with the target; its own permutation p |
| [[CADPS]] | C | CADPS activity raises MUC6's level | lines that do not express CADPS (39) vs lines expressing it (11) | 2.25× lower at baseline in the lines without CADPS | 0.090 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX10, LINC01425, TYR; co-absent with the target |

### Downstream of this gene

*43 arrows, 43 of them with an alert ⚠; grade A 0, B 3, C 40. Shown: the 12 strongest; 31 more arrows (31 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ENPP3]] | B | MUC6 activity raises ENPP3's level | lines that do not express MUC6 (45) vs lines expressing it (5) | 1.74× lower at baseline in the lines without MUC6 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, ENSG00000230975, APOB |
| [[BCAR3-AS1]] | B | MUC6 activity raises BCAR3-AS1's level | lines that do not express MUC6 (45) vs lines expressing it (5) | 1.95× lower at baseline in the lines without MUC6 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, ENSG00000230975, APOB |
| [[PLXNB1]] | B | MUC6 activity raises PLXNB1's level | lines that do not express MUC6 (45) vs lines expressing it (5) | 1.72× lower at baseline in the lines without MUC6 | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, ENSG00000230975, APOB |
| [[TFF3]] | C | MUC6 activity raises TFF3's level | lines that do not express MUC6 (45) vs lines expressing it (5) | 15.61× lower at baseline in the lines without MUC6 | 7e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, ENSG00000230975, APOB; co-absent with the target |
| [[MUC17]] | C | MUC6 activity raises MUC17's level | lines that do not express MUC6 (45) vs lines expressing it (5) | 3.61× lower at baseline in the lines without MUC6 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, ENSG00000230975, APOB; co-absent with the target |
| [[PCK1]] | C | MUC6 activity raises PCK1's level | lines that do not express MUC6 (45) vs lines expressing it (5) | 5.02× lower at baseline in the lines without MUC6 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, ENSG00000230975, APOB; co-absent with the target |
| [[LINC01814]] | C | MUC6 activity raises LINC01814's level | lines that do not express MUC6 (45) vs lines expressing it (5) | 4.34× lower at baseline in the lines without MUC6 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, ENSG00000230975, APOB; co-absent with the target |
| [[MYB]] | C | MUC6 activity raises MYB's level | lines that do not express MUC6 (45) vs lines expressing it (5) | 3.90× lower at baseline in the lines without MUC6 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, ENSG00000230975, APOB; co-absent with the target |
| [[ST6GALNAC1]] | C | MUC6 activity raises ST6GALNAC1's level | lines that do not express MUC6 (45) vs lines expressing it (5) | 2.08× lower at baseline in the lines without MUC6 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, ENSG00000230975, APOB; co-absent with the target |
| [[GPA33]] | C | MUC6 activity raises GPA33's level | lines that do not express MUC6 (45) vs lines expressing it (5) | 3.18× lower at baseline in the lines without MUC6 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, ENSG00000230975, APOB; co-absent with the target |
| [[TFF2]] | C | MUC6 activity raises TFF2's level | lines that do not express MUC6 (45) vs lines expressing it (5) | 1.47× lower at baseline in the lines without MUC6 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, ENSG00000230975, APOB; co-absent with the target |
| [[SMOC2]] | C | MUC6 activity raises SMOC2's level | lines that do not express MUC6 (45) vs lines expressing it (5) | 4.94× lower at baseline in the lines without MUC6 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, ENSG00000230975, APOB; co-absent with the target |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.478). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.6, 49.8); signed map (65.7, 5.7). **Vector** length 10.8, 4.53% of its response variance represented; |z| ≥ 3 in 35 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.3 | +9.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.2 | +11.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.1 | +9.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.0 | +6.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +0.7 | +4.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.5 | +2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.5 | +1.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.4 | +1.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +0.3 | -0.5 |
|  | [[Thymol (drug)]] 0.5 µM |  | +0.3 | +1.8 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -0.4 | -0.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.4 | -0.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.4 | -1.9 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.3 | -0.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.3 | -2.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -0.3 | -0.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.3 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | mucin 6, oligomeric mucus/gel-forming (gene/pseudogene) |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.5 — chr11:1,012,823-1,036,718 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MUC-6 |
| Gene groups (HGNC) | Mucins |
| Reactome | 12 pathways, smallest: Defective GALNT12 causes CRCS1; Defective GALNT3 causes HFTC; Defective C1GALT1C1 causes TNPS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6W4X9](https://www.uniprot.org/uniprotkb/Q6W4X9) (Mucin-6):

> May provide a mechanism for modulation of the composition of the protective mucus layer related to acid secretion or the presence of bacteria and noxious agents in the lumen. Plays an important role in the cytoprotection of epithelial surfaces and are used as tumor markers in a variety of cancers. May play a role in epithelial organogenesis.

**Summary**, from NCBI Gene [4588](https://www.ncbi.nlm.nih.gov/gene/4588):

> This gene encodes a member of the mucin protein family. Mucins are high molecular weight glycoproteins produced by many epithelial tissues. The protein encoded by this gene is secreted and forms an insoluble mucous barrier that protects the gut lumen. [provided by RefSeq, Dec 2016]

**Accessions** — [HGNC:7517](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7517) · Entrez [4588](https://www.ncbi.nlm.nih.gov/gene/4588) · UniProt [Q6W4X9](https://www.uniprot.org/uniprotkb/Q6W4X9) · Ensembl [ENSG00000184956](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184956)

## Data

Gene col 11596: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11596); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11596, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11596]; `tensor/DDL_lfc|DDL_z.npy` [11596]; `embed/gene_vectors.npy` [11596]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11596 or target_col == 11596). Every well: [[MUC6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MUC6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
