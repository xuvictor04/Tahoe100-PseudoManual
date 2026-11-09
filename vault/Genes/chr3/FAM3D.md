---
symbol: "FAM3D"
type: "gene"
col: 12633
ensembl_id: "ENSG00000198643"
name: "FAM3 metabolism regulating signaling molecule D"
location: "3p14.2"
module: 73
arm: "+"
pooled_cpm: 3.07
n_lines_expressing: 7
n_dd_up: 15
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 35
direction_downstream: 104
tags: ["gene", "module/073"]
generated_by: "tahoemap"
---

# FAM3D

*FAM3 metabolism regulating signaling molecule D* — 3p14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 7.27× (z +11.3, q 5e-27, up in 1 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.93× (z +5.5, q 5e-06, up in 0 of 4 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 15 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (LoVo 0.0468×, HT-29 0.0214×, LS 180 0.0673×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (LoVo 0.0499×, HT-29 0.0233×, LS 180 0.113×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (HT-29 0.0668×, LoVo 0.194×); [[Harringtonine (drug)]] 5 µM in 2 lines (LoVo 0.109×, HT-29 0.0943×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NPSR1]] (+0.88, fdr 7e-06), [[GPA33]] (+0.87, fdr 7e-06), [[HEPH]] (+0.85, fdr 7e-06).
> It is in [[Module 073]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 35 arrows point to it, the strongest [[BOLA3-DT]] → it (grade B ⚠); 104 go from it, the strongest it → [[SDCBP2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12633.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **7.27×** | +11.3 | 5e-27 | 1/2 (HT-29) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.12×** | +9.7 | 9e-20 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.33×** | +8.0 | 2e-13 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.93×** | +5.5 | 5e-06 | 0/4 | top dose only | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.94×** | +4.6 | 6e-04 | 0/3 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.65×** | +4.2 | 0.003 | 0/5 | top dose only | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.04×** | +4.1 | 0.004 | 0/3 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.97×** | +3.9 | 0.008 | 0/4 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Thymol (drug)]] 0.5 µM |  | **1.86×** | +3.7 | 0.016 | 0/3 | two highest doses | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.85×** | +3.6 | 0.016 | 0/3 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.35×** | +3.6 | 0.016 | 0/3 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.10×** | +3.5 | 0.021 | 0/2 | top dose only | noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.77×** | +3.4 | 0.032 | 1/3 (LoVo) | inconsistent across doses | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.08×** | +3.1 | 0.081 | 1/3 (LoVo) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +3.0 | 0.099 | 0/4 | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12633.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 15 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (LoVo 0.0468×, HT-29 0.0214×, LS 180 0.0673×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (LoVo 0.0499×, HT-29 0.0233×, LS 180 0.113×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (HT-29 0.0668×, LoVo 0.194×); [[Harringtonine (drug)]] 5 µM in 2 lines (LoVo 0.109×, HT-29 0.0943×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | 0.574× | -3.3 | 0.35 | 3/4 (LoVo, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~8% here); position effect removed |
| [[Ciclopirox (drug)]] 0.5 µM |  | 0.584× | -3.2 | 0.35 | 0/4 | inconsistent across doses | position effect removed |
| [[Artesunate (drug)]] 0.5 µM |  | 0.604× | -3.0 | 0.46 | 1/4 (HT-29) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12633. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 53.1 | 0 | 16 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0468× (z -25.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0499× (z -17.4) |
| [[HT-29 (line)]] | alt | 24.2 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0214× (z -20.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0668× (z -14.7) |
| [[LS 180 (line)]] | wt | 13.0 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0673× (z -16.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.113× (z -9.3) |
| [[A-172 (line)]] | wt | 0.362 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.383 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.474 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.327 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.585 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.565 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.527 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.358 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.530 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.579 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.460 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.896 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.505 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.392 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.570 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.352 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.524 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.419 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.421 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.491 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.352 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.749 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.524 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.293 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.366 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.532 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.530 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.557 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.345 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.481 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.369 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.318 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.295 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.479 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.646 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.514 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.359 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.358 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.568 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.630 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.606 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.440 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.414 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.350 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12633), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPSR1]] | +0.88 | +0.83 / +0.87 | both halves | 7e-06 | **novel candidate** |
| [[GPA33]] | +0.87 | +0.88 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[HEPH]] | +0.85 | +0.88 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[CFTR]] | +0.85 | +0.85 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[LGALS4]] | +0.83 | +0.77 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[SLC6A20]] | +0.81 | +0.76 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[PRR15L]] | +0.80 | +0.79 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[MYO7B]] | +0.79 | +0.80 / +0.75 | both halves | 7e-06 |  |
| [[UGT1A1]] | +0.79 | +0.79 / +0.70 | both halves | 7e-06 |  |
| [[TPTEP1-1]] | +0.78 | +0.76 / +0.65 | both halves | 7e-06 |  |
| [[LINC01819]] | +0.77 | +0.74 / +0.80 | both halves | 7e-06 |  |
| [[TPRXL]] | +0.76 | +0.74 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*35 arrows, 35 of them with an alert ⚠; grade A 0, B 1, C 34. Shown: the 12 strongest; 23 more arrows (23 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BOLA3-DT]] | B | BOLA3-DT activity lowers FAM3D's level | lines that do not express BOLA3-DT (10) vs lines expressing it (40) | 2.56× higher at baseline in the lines without BOLA3-DT | 0.076 | ⚠ within organs, on part of the lines; also absent: GIHCG, KATNAL1, LIX1L |
| [[MUC2]] | C | MUC2 activity raises FAM3D's level | lines that do not express MUC2 (42) vs lines expressing it (8) | 3.46× lower at baseline in the lines without MUC2 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000248588, DSG4; co-absent with the target |
| [[REG4]] | C | REG4 activity raises FAM3D's level | lines that do not express REG4 (43) vs lines expressing it (7) | 4.36× lower at baseline in the lines without REG4 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, NPSR1, ENSG00000230975; co-absent with the target |
| [[CFTR]] | C | CFTR activity raises FAM3D's level | lines that do not express CFTR (39) vs lines expressing it (11) | 2.66× lower at baseline in the lines without CFTR | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CTSE, ENSG00000224322, ATP10B; maybe low, not absent; co-absent with the target |
| [[C6orf132]] | C | C6orf132 activity raises FAM3D's level | lines that do not express C6orf132 (27) vs lines expressing it (23) | 1.60× lower at baseline in the lines without C6orf132 | 0.008 | ⚠ within organs, on part of the lines; also absent: PCSK9, RNF223, CDH1; co-absent with the target |
| [[CEACAM5]] | C | CEACAM5 activity raises FAM3D's level | lines that do not express CEACAM5 (39) vs lines expressing it (11) | 2.80× lower at baseline in the lines without CEACAM5 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, ENSG00000267881; co-absent with the target |
| [[CTSE]] | C | CTSE activity raises FAM3D's level | lines that do not express CTSE (42) vs lines expressing it (8) | 3.32× lower at baseline in the lines without CTSE | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000224322, REG4, CFTR; co-absent with the target |
| [[LINC00457]] | C | LINC00457 activity raises FAM3D's level | lines that do not express LINC00457 (29) vs lines expressing it (21) | 1.67× lower at baseline in the lines without LINC00457 | 0.013 | ⚠ within organs, on part of the lines; also absent: LINC01440, LINC01456, NTS; maybe low, not absent; co-absent with the target |
| [[NPSR1]] | C | NPSR1 activity raises FAM3D's level | lines that do not express NPSR1 (42) vs lines expressing it (8) | 3.76× lower at baseline in the lines without NPSR1 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, MUC17, CDH17; co-absent with the target |
| [[TNFRSF14-AS1]] | C | TNFRSF14-AS1 activity raises FAM3D's level | lines that do not express TNFRSF14-AS1 (23) vs lines expressing it (27) | 1.46× lower at baseline in the lines without TNFRSF14-AS1 | 0.032 | ⚠ within organs, on part of the lines; also absent: ACSL5, LINC01819, MAOB; co-absent with the target |
| [[UGT1A1]] | C | UGT1A1 activity raises FAM3D's level | lines that do not express UGT1A1 (36) vs lines expressing it (14) | 2.09× lower at baseline in the lines without UGT1A1 | 0.034 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, NPSR1; co-absent with the target |
| [[CDH17]] | C | CDH17 activity raises FAM3D's level | lines that do not express CDH17 (40) vs lines expressing it (10) | 3.03× lower at baseline in the lines without CDH17 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, MUC13, CLRN3; co-absent with the target |

### Downstream of this gene

*104 arrows, 104 of them with an alert ⚠; grade A 0, B 16, C 88. Shown: the 12 strongest; 92 more arrows (92 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SDCBP2]] | B | FAM3D activity raises SDCBP2's level | lines that do not express FAM3D (43) vs lines expressing it (7) | 9.47× lower at baseline in the lines without FAM3D | 4e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, ENSG00000230975, NPSR1; maybe low, not absent |
| [[CYSTM1]] | B | FAM3D activity raises CYSTM1's level | lines that do not express FAM3D (43) vs lines expressing it (7) | 2.50× lower at baseline in the lines without FAM3D | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, ENSG00000230975, NPSR1; maybe low, not absent |
| [[MYH14]] | B | FAM3D activity raises MYH14's level | lines that do not express FAM3D (43) vs lines expressing it (7) | 6.87× lower at baseline in the lines without FAM3D | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, ENSG00000230975, NPSR1; maybe low, not absent |
| [[ARHGEF16]] | B | FAM3D activity raises ARHGEF16's level | lines that do not express FAM3D (43) vs lines expressing it (7) | 3.22× lower at baseline in the lines without FAM3D | 0.029 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, ENSG00000230975, NPSR1; maybe low, not absent |
| [[NOSTRIN]] | B | FAM3D activity raises NOSTRIN's level | lines that do not express FAM3D (43) vs lines expressing it (7) | 3.90× lower at baseline in the lines without FAM3D | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, ENSG00000230975, NPSR1; maybe low, not absent |
| [[BAIAP2L2]] | B | FAM3D activity raises BAIAP2L2's level | lines that do not express FAM3D (43) vs lines expressing it (7) | 2.43× lower at baseline in the lines without FAM3D | 0.037 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, ENSG00000230975, NPSR1; maybe low, not absent |
| [[LINC01290]] | B | FAM3D activity raises LINC01290's level | lines that do not express FAM3D (43) vs lines expressing it (7) | 2.02× lower at baseline in the lines without FAM3D | 0.049 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, ENSG00000230975, NPSR1; maybe low, not absent |
| [[BOLA3-DT]] | B | FAM3D activity lowers BOLA3-DT's level | lines that do not express FAM3D (43) vs lines expressing it (7) | 1.97× higher at baseline in the lines without FAM3D | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, ENSG00000230975, NPSR1; maybe low, not absent |
| [[IL22RA1]] | B | FAM3D activity raises IL22RA1's level | lines that do not express FAM3D (43) vs lines expressing it (7) | 3.44× lower at baseline in the lines without FAM3D | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, ENSG00000230975, NPSR1; maybe low, not absent |
| [[LINC02580]] | B | FAM3D activity raises LINC02580's level | lines that do not express FAM3D (43) vs lines expressing it (7) | 2.01× lower at baseline in the lines without FAM3D | 0.058 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, ENSG00000230975, NPSR1; maybe low, not absent |
| [[MUC12]] | B | FAM3D activity raises MUC12's level | lines that do not express FAM3D (43) vs lines expressing it (7) | 3.24× lower at baseline in the lines without FAM3D | 0.065 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, ENSG00000230975, NPSR1; maybe low, not absent |
| [[EPS8L1]] | B | FAM3D activity raises EPS8L1's level | lines that do not express FAM3D (43) vs lines expressing it (7) | 3.90× lower at baseline in the lines without FAM3D | 0.067 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, ENSG00000230975, NPSR1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 073]]; 66 genes; every member is in the + arm (projection on the module's main direction 0.823). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (20.2, 50.6); signed map (64.9, 7.1). **Vector** length 42.9, 29.7% of its response variance represented; |z| ≥ 3 in 167 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.8 | +8.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.6 | +9.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | +0.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.3 | +11.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.0 | +5.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.9 | +3.6 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +0.6 | +0.3 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +0.6 | +0.2 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | +0.6 | +0.9 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.4 | -2.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.0 | -0.0 |
|  | [[EX229 (drug)]] 5 µM |  | -0.9 | +0.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -0.8 | -1.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.8 | -2.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -0.7 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | FAM3 metabolism regulating signaling molecule D |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p14.2 — chr3:58,633,946-58,666,834 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EF7, OIT1 |
| Matched by | ensembl_id |

UniProt [Q96BQ1](https://www.uniprot.org/uniprotkb/Q96BQ1) carries no function annotation.

**Summary**, from NCBI Gene [131177](https://www.ncbi.nlm.nih.gov/gene/131177):

> Predicted to enable cytokine activity. Involved in negative regulation of insulin secretion. Predicted to be located in extracellular region. Predicted to be active in obsolete extracellular space. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:18665](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18665) · Entrez [131177](https://www.ncbi.nlm.nih.gov/gene/131177) · UniProt [Q96BQ1](https://www.uniprot.org/uniprotkb/Q96BQ1) · Ensembl [ENSG00000198643](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198643)

## Data

Gene col 12633: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12633); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12633, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12633]; `tensor/DDL_lfc|DDL_z.npy` [12633]; `embed/gene_vectors.npy` [12633]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12633 or target_col == 12633). Every well: [[FAM3D — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM3D.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
