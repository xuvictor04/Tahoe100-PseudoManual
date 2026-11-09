---
symbol: "SORCS2"
type: "gene"
col: 11601
ensembl_id: "ENSG00000184985"
name: "sortilin related VPS10 domain containing receptor 2"
location: "4p16.1"
module: 13
arm: "+"
pooled_cpm: 20.0
n_lines_expressing: 28
n_dd_up: 24
n_dd_down: 3
n_dd_up_clean: 10
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 9
direction_downstream: 3
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# SORCS2

*sortilin related VPS10 domain containing receptor 2* — 4p16.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.84× (z +12.5, q 6e-33, up in 3 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.68× (z +12.3, q 5e-32, up in 14 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.752× (z -5.0, q 3e-04, down in 15 of 26 measured lines) ⚠ cell-cycle shift, explains ~43% of this change. The strongest without an alert is [[TAK-733 (drug)]] 0.05 µM: 0.668× (z -4.1, q 0.012, down in 1 of 26 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Trametinib (drug)]] 5 µM in 2 lines (LOX-IMVI 0.106×, SK-MEL-2 0.114×; ⚠ cell-cycle shift, explains ~33% of this change); [[Selinexor (drug)]] 5 µM in 2 lines (HS-578T 0.277×, SW480 0.376×; ⚠ cell-cycle shift, explains ~43% of this change); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM in 2 lines (SK-MEL-2 0.0695×, LOX-IMVI 0.171×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A498 0.396×); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.166×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DOCK2]] (+0.65, fdr 7e-06), [[COL15A1]] (+0.60, fdr 4e-05), [[NMNAT2]] (+0.59, fdr 3e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[FKBP9P1-1]] → it (grade B ⚠); 3 go from it, the strongest it → [[CARD11]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11601.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.84×** | +12.5 | 6e-33 | 3/10 (HS-578T, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.68×** | +12.3 | 5e-32 | 14/25 (MIA PaCa-2, PANC-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.71×** | +11.5 | 3e-28 | 4/13 (RPMI-7951, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.87×** | +11.0 | 7e-26 | 9/24 (BT-474, A549, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.80×** | +10.4 | 4e-23 | 15/26 (SW480, A-427, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **4.57×** | +9.9 | 4e-21 | 12/17 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **2.17×** | +9.6 | 5e-20 | 7/17 (NCI-H2030, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.67×** | +9.0 | 1e-17 | 8/25 (NCI-H2030, PANC-1, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.86×** | +7.7 | 9e-13 | 5/24 (PANC-1, HepG2/C3A, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.73×** | +6.8 | 7e-10 | 5/26 (PANC-1, NCI-H1573, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.71×** | +6.7 | 1e-09 | 9/26 (PANC-1, J82, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.56×** | +5.5 | 1e-06 | 10/25 (NCI-H2030, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.55×** | +5.4 | 3e-06 | 12/26 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.19×** | +5.1 | 1e-05 | 6/16 (A549, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.52×** | +4.9 | 4e-05 | 6/26 (PANC-1, J82, …) | all doses, stronger at high dose |  |
| [[Busulfan (drug)]] 5 µM |  | **1.30×** | +4.6 | 2e-04 | 3/26 (MIA PaCa-2, SK-MEL-2, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.82×** | +3.9 | 0.003 | 6/21 (A-172, BT-474, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.33×** | +3.6 | 0.011 | 4/26 (A-172, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +3.0 | 0.066 | 3/26 (A549, HepG2/C3A, …) | top dose only |  |
| [[LJI308 (drug)]] 0.05 µM |  | **1.34×** | +3.0 | 0.069 | 1/24 (PANC-1) | inconsistent across doses | noisy plate (z scaled) |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM |  | **1.26×** | +2.9 | 0.087 | 1/23 (BT-474) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11601.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Trametinib (drug)]] 5 µM in 2 lines (LOX-IMVI 0.106×, SK-MEL-2 0.114×; ⚠ cell-cycle shift, explains ~33% of this change); [[Selinexor (drug)]] 5 µM in 2 lines (HS-578T 0.277×, SW480 0.376×; ⚠ cell-cycle shift, explains ~43% of this change); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM in 2 lines (SK-MEL-2 0.0695×, LOX-IMVI 0.171×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A498 0.396×); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.166×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.752×** | -5.0 | 3e-04 | 15/26 (HS-578T, SW480, …) | top dose only | low cells (technical?) |
| [[TAK-733 (drug)]] 0.05 µM |  | **0.668×** | -4.1 | 0.012 | 1/26 (MIA PaCa-2) | inconsistent across doses | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.743×** | -3.7 | 0.038 | 5/24 (SW480, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11601. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 98.9 | 0 | 3 (1 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.106× (z -12.3) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.166× (z -9.5) |
| [[SK-MEL-2 (line)]] | alt | 24.2 | 0 | 3 (2 ⚠) | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0695× (z -9.9) |
| [[A498 (line)]] | wt | 175 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.396× (z -10.3) |
| [[PANC-1 (line)]] | alt | 9.54 | 2 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 6.77× (z +10.9) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[SW480 (line)]] | alt | 21.2 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.166× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 34.5 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 5.63× (z +10.0) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[A549 (line)]] | wt | 19.9 | 1 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 8.96× (z +11.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HS-578T (line)]] | alt | 24.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.277× (z -10.6) ⚠ cell-cycle shift, explains ~43% of this change |
| [[J82 (line)]] | alt | 9.31 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.129× (z -8.8) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 6.56 | 1 | 0 | [[Auranofin (drug)]] 5 µM 11.0× (z +9.1) | — |
| [[A-427 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.20 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.95 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.39 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.66 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.14 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.39 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.91 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.50 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 5.40 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 86.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.64 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.25 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.86 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.02 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 4.45 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.01 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.39 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.60 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.35 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.50 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.30 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.91 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.61 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.47 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 4.54 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.08 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11601), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DOCK2]] | +0.65 | +0.58 / +0.61 | both halves | 7e-06 | same gene group |
| [[COL15A1]] | +0.60 | +0.41 / +0.63 | both halves | 4e-05 |  |
| [[NMNAT2]] | +0.59 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[FRMD4A]] | +0.58 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[EVA1A]] | +0.58 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[INSYN2B]] | +0.58 | +0.37 / +0.55 | both halves | 9e-05 |  |
| [[CAMK4]] | +0.57 | +0.46 / +0.55 | both halves | 2e-05 |  |
| [[STK32B]] | +0.56 | +0.38 / +0.57 | both halves | 6e-05 |  |
| [[NAV1]] | +0.56 | +0.44 / +0.48 | both halves | 3e-05 | same gene group |
| [[APCDD1L]] | +0.56 | +0.42 / +0.61 | both halves | 4e-05 |  |
| [[ADAMTS12]] | +0.56 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[CSMD2]] | +0.56 | +0.40 / +0.57 | both halves | 4e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 7, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FKBP9P1-1]] | B | FKBP9P1-1 activity raises SORCS2's level | lines that do not express FKBP9P1-1 (30) vs lines expressing it (20) | 1.88× lower at baseline in the lines without FKBP9P1-1 | 0.035 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000231317, ENSG00000253642, ENSG00000287622; maybe low, not absent |
| [[CDH13]] | B | CDH13 activity raises SORCS2's level | lines that do not express CDH13 (35) vs lines expressing it (15) | 2.32× lower at baseline in the lines without CDH13 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMP2, APCDD1L, ENSG00000222032 |
| [[COL6A2]] | B | COL6A2 activity raises SORCS2's level | lines that do not express COL6A2 (28) vs lines expressing it (22) | 2.32× lower at baseline in the lines without COL6A2 | 0.050 | ⚠ within organs, on part of the lines; also absent: COL6A1, DKK3, ADAMTS2 |
| [[ADAMTS12]] | B | ADAMTS12 activity raises SORCS2's level | lines that do not express ADAMTS12 (33) vs lines expressing it (17) | 2.79× lower at baseline in the lines without ADAMTS12 | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC01411, APBB1IP, VCAM1 |
| [[SLC8A1]] | B | SLC8A1 activity raises SORCS2's level | lines that do not express SLC8A1 (26) vs lines expressing it (24) | 2.50× lower at baseline in the lines without SLC8A1 | 0.085 | ⚠ within organs, on part of the lines; also absent: DPY19L2, MAGI2, MAGI2-AS3 |
| [[SARDH]] | B | SARDH activity raises SORCS2's level | lines that do not express SARDH (21) vs lines expressing it (29) | 1.63× lower at baseline in the lines without SARDH | 0.089 | ⚠ within organs, on part of the lines; also absent: PKD1L1-AS1, ZNF90, ENSG00000222032; maybe low, not absent |
| [[FAM167A]] | B | FAM167A activity raises SORCS2's level | lines that do not express FAM167A (17) vs lines expressing it (33) | 2.40× lower at baseline in the lines without FAM167A | 0.091 | ⚠ within organs, on part of the lines; also absent: ENSG00000255330, PREX1, SOGA3; maybe low, not absent |
| [[MGAT5B]] | C | MGAT5B activity raises SORCS2's level | lines that do not express MGAT5B (15) vs lines expressing it (35) | 2.77× lower at baseline in the lines without MGAT5B | 0.017 | ⚠ within organs, on part of the lines; also absent: SDK2, PYGO1, EVL; co-absent with the target |
| [[NTM]] | C | NTM activity raises SORCS2's level | lines that do not express NTM (33) vs lines expressing it (17) | 2.48× lower at baseline in the lines without NTM | 0.099 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000222032, CDH13, THY1; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CARD11]] | B | SORCS2 activity lowers CARD11's level | lines that do not express SORCS2 (22) vs lines expressing it (28) | 1.71× higher at baseline in the lines without SORCS2 | 0.068 | ⚠ within organs, on part of the lines; also absent: ELFN1, CECR2, NTRK3; maybe low, not absent |
| [[IQSEC1]] | B | SORCS2 activity raises IQSEC1's level | lines that do not express SORCS2 (22) vs lines expressing it (28) | 1.89× lower at baseline in the lines without SORCS2 | 0.073 | ⚠ within organs, on part of the lines; also absent: ELFN1, CECR2, NTRK3; maybe low, not absent |
| [[MGAT5B]] | C | SORCS2 activity raises MGAT5B's level | lines that do not express SORCS2 (22) vs lines expressing it (28) | 3.31× lower at baseline in the lines without SORCS2 | 0.023 | ⚠ within organs, on part of the lines; also absent: ELFN1, CECR2, NTRK3; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.618). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (50.1, 15.9); signed map (21.5, 46.3). **Vector** length 54.9, 11.4% of its response variance represented; |z| ≥ 3 in 627 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.5 | +12.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | +5.0 | +9.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +10.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.2 | +11.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +11.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +12.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +3.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +1.3 |
|  | [[Glycyrrhizic acid (drug)]] 0.05 µM |  | +1.2 | -0.1 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -2.1 | -5.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.9 | -2.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.8 | -2.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -1.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | +0.7 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.6 | -2.3 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.6 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | sortilin related VPS10 domain containing receptor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p16.1 — chr4:7,192,538-7,742,827 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1329 |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96PQ0](https://www.uniprot.org/uniprotkb/Q96PQ0) (VPS10 domain-containing receptor SorCS2):

> The heterodimer formed by NGFR and SORCS2 functions as receptor for the precursor forms of NGF (proNGF) and BDNF (proBDNF). ProNGF and proBDNF binding both promote axon growth cone collapse (in vitro). Plays a role in the regulation of dendritic spine density in hippocampus neurons (By similarity). Required for normal neurite branching and extension in response to BDNF. Plays a role in BDNF-dependent hippocampal synaptic plasticity. Together with NGFR and NTRK2, is required both for …

**Summary**, from NCBI Gene [57537](https://www.ncbi.nlm.nih.gov/gene/57537):

> This gene encodes one family member of vacuolar protein sorting 10 (VPS10) domain-containing receptor proteins. The VPS10 domain name comes from the yeast carboxypeptidase Y sorting receptor Vps10 protein. Members of this gene family are large with many exons but the CDS lengths are usually less than 3700 nt. Very large introns typically separate the exons encoding the VPS10 domain; the remaining exons are separated by much smaller-sized introns. These genes are strongly expressed in the …

**Accessions** — [HGNC:16698](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16698) · Entrez [57537](https://www.ncbi.nlm.nih.gov/gene/57537) · UniProt [Q96PQ0](https://www.uniprot.org/uniprotkb/Q96PQ0) · Ensembl [ENSG00000184985](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184985)

## Data

Gene col 11601: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11601); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11601, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11601]; `tensor/DDL_lfc|DDL_z.npy` [11601]; `embed/gene_vectors.npy` [11601]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11601 or target_col == 11601). Every well: [[SORCS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SORCS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
