---
symbol: "SMIM10"
type: "gene"
col: 11574
ensembl_id: "ENSG00000184785"
name: "small integral membrane protein 10"
location: "Xq26.3"
module: 45
arm: "+"
pooled_cpm: 2.72
n_lines_expressing: 26
n_dd_up: 6
n_dd_down: 9
n_dd_up_clean: 2
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 15
direction_downstream: 20
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# SMIM10

*small integral membrane protein 10* — Xq26.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.52× (z +11.5, q 5e-28, up in 15 of 15 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.68× (z +4.9, q 1e-04, up in 12 of 23 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (PANC-1 5.63×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.472× (z -7.2, q 3e-10, down in 15 of 19 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FKBP7]] (+0.62, fdr 1e-05), [[HMGN3]] (+0.59, fdr 2e-05), [[FAM104B]] (+0.58, fdr 2e-05); moves opposite to [[ZNF778]] (-0.48, fdr 1e-04), [[POC1B]] (-0.47, fdr 5e-05), [[CSRNP2]] (-0.46, fdr 1e-04).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[ZNF608]] → it (grade B ⚠); 20 go from it, the strongest it → [[ZNF608]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11574.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (PANC-1 5.63×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.52×** | +11.5 | 5e-28 | 15/15 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.50×** | +9.8 | 4e-20 | 6/7 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.56×** | +5.9 | 8e-07 | 8/8 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.68×** | +4.9 | 1e-04 | 12/23 (CFPAC-1, PANC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.96×** | +4.5 | 6e-04 | 10/20 (J82, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.69×** | +3.4 | 0.063 | 5/12 (SK-MEL-2, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | 1.59× | +3.1 | 0.14 | 4/9 (LS 180, PANC-1, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11574.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.472×** | -7.2 | 3e-10 | 15/19 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.487×** | -4.9 | 3e-04 | 13/22 (CFPAC-1, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.482×** | -4.7 | 5e-04 | 13/20 (PANC-1, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.672×** | -3.8 | 0.018 | 13/20 (SW480, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.598×** | -3.5 | 0.052 | 10/21 (SW480, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.602×** | -3.5 | 0.052 | 10/20 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.383×** | -3.4 | 0.053 | 11/22 (SK-MEL-2, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.610×** | -3.4 | 0.054 | 10/22 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Hydroxyurea (drug)]] 5 µM |  | **0.617×** | -3.2 | 0.097 | 6/22 (HOP62, NCI-H460, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11574. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 8.66 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 5.63× (z +8.8) ⚠ toxic; transcription drop | [[Bortezomib (drug)]] 0.05 µM 0.161× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 2.54 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0799× (z -12.4) |
| [[SW480 (line)]] | alt | 5.46 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -9.8) |
| [[LS 180 (line)]] | wt | 3.75 | 0 | 1 | — | [[Valdecoxib (drug)]] 0.05 µM 0.0603× (z -8.8) |
| [[A-172 (line)]] | wt | 0.383 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.212 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 6.74 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.230 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.447 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.280 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.245 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.273 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.12 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.71 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.241 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.68 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.269 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.254 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.419 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.297 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.267 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.10 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.227 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.237 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.313 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.223 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.254 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.229 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.234 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.936 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.263 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.66 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.257 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.304 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.274 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11574), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FKBP7]] | +0.62 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[HMGN3]] | +0.59 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[FAM104B]] | +0.58 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[TMEM14A]] | +0.55 | +0.39 / +0.49 | both halves | 5e-05 |  |
| [[ZNF883]] | +0.54 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[RASSF4]] | +0.54 | +0.51 / +0.38 | both halves | 6e-05 |  |
| [[TNRC6A]] | +0.54 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[NAT14]] | +0.53 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[ANGPT1]] | +0.53 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[DYNC2H1]] | +0.53 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[OLFML2A]] | +0.52 | +0.54 / +0.42 | both halves | 4e-05 |  |
| [[TET1]] | +0.52 | +0.58 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF778]] | -0.48 | -0.33 / -0.38 | both halves | 1e-04 |  |
| [[POC1B]] | -0.47 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[CSRNP2]] | -0.46 | -0.35 / -0.37 | both halves | 1e-04 |  |
| [[ZNF710]] | -0.46 | -0.32 / -0.40 | both halves | 2e-04 |  |
| [[TRPV1]] | -0.44 | -0.21 / -0.42 | both halves | 7e-04 |  |
| [[LINC01829]] | -0.43 | -0.31 / -0.40 | both halves | 2e-04 |  |
| [[KBTBD8]] | -0.43 | -0.45 / -0.24 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 9, C 6. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF608]] | B | ZNF608 activity raises SMIM10's level | lines that do not express ZNF608 (12) vs lines expressing it (38) | 2.01× lower at baseline in the lines without ZNF608 | 0.002 | ⚠ within organs, on part of the lines; also absent: LINC01170, GDF15 |
| [[TET1]] | B | TET1 activity raises SMIM10's level | lines that do not express TET1 (12) vs lines expressing it (38) | 2.06× lower at baseline in the lines without TET1 | 0.021 | ⚠ within organs, on part of the lines; also absent: PLEKHO1, MCAM, KCNK13; maybe low, not absent |
| [[STK33]] | B | STK33 activity raises SMIM10's level | lines that do not express STK33 (18) vs lines expressing it (32) | 1.57× lower at baseline in the lines without STK33 | 0.033 | ⚠ within organs, on part of the lines; also absent: SDK1, PGBD5, NID1; maybe low, not absent |
| [[RHOBTB3]] | B | RHOBTB3 activity raises SMIM10's level | lines that do not express RHOBTB3 (10) vs lines expressing it (40) | 2.43× lower at baseline in the lines without RHOBTB3 | 0.039 | ⚠ within organs, on part of the lines; also absent: FYN, POGLUT3; maybe low, not absent |
| [[WDR17]] | B | WDR17 activity raises SMIM10's level | lines that do not express WDR17 (16) vs lines expressing it (34) | 2.09× lower at baseline in the lines without WDR17 | 0.059 | ⚠ within organs, on part of the lines; also absent: WIPF1, AFAP1L1, SGCE |
| [[GAMT]] | B | GAMT activity raises SMIM10's level | lines that do not express GAMT (11) vs lines expressing it (39) | 1.53× lower at baseline in the lines without GAMT | 0.093 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: HDGFL3, HLTF, EHD3 |
| [[RASSF4]] | B | RASSF4 activity raises SMIM10's level | lines that do not express RASSF4 (11) vs lines expressing it (39) | 1.79× lower at baseline in the lines without RASSF4 | 0.093 | ⚠ within organs, on part of the lines; also absent: CTSS, SLC15A3, MX2; maybe low, not absent |
| [[MEF2C]] | B | MEF2C activity raises SMIM10's level | lines that do not express MEF2C (14) vs lines expressing it (36) | 1.80× lower at baseline in the lines without MEF2C | 0.094 | ⚠ within organs, on part of the lines; also absent: MEF2C-AS1, RGS2, MYOSLID |
| [[PSMB5]] | B | PSMB5 activity raises SMIM10's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CFI]] | C | CFI activity raises SMIM10's level | lines that do not express CFI (31) vs lines expressing it (19) | 2.27× lower at baseline in the lines without CFI | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000285330, ENSG00000239268, RUNX1T1; co-absent with the target |
| [[CTSF]] | C | CTSF activity raises SMIM10's level | lines that do not express CTSF (16) vs lines expressing it (34) | 2.25× lower at baseline in the lines without CTSF | 0.015 | ⚠ within organs, on part of the lines; also absent: BVES-AS1, LINC01725, BVES; co-absent with the target |
| [[LINC01583]] | C | LINC01583 activity raises SMIM10's level | lines that do not express LINC01583 (28) vs lines expressing it (22) | 2.14× lower at baseline in the lines without LINC01583 | 0.016 | ⚠ within organs, on part of the lines; also absent: INSYN2B, ADAM12, ZEB2; co-absent with the target |

### Downstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 15, C 5. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF608]] | B | SMIM10 activity raises ZNF608's level | lines that do not express SMIM10 (24) vs lines expressing it (26) | 1.93× lower at baseline in the lines without SMIM10 | 0.001 | ⚠ within organs, on part of the lines; also absent: SNAI2, MCAM, ZNF365 |
| [[RASSF4]] | B | SMIM10 activity raises RASSF4's level | lines that do not express SMIM10 (24) vs lines expressing it (26) | 1.99× lower at baseline in the lines without SMIM10 | 0.003 | ⚠ within organs, on part of the lines; also absent: SNAI2, MCAM, ZNF365 |
| [[TET1]] | B | SMIM10 activity raises TET1's level | lines that do not express SMIM10 (24) vs lines expressing it (26) | 2.22× lower at baseline in the lines without SMIM10 | 0.007 | ⚠ within organs, on part of the lines; also absent: SNAI2, MCAM, ZNF365 |
| [[STK33]] | B | SMIM10 activity raises STK33's level | lines that do not express SMIM10 (24) vs lines expressing it (26) | 1.92× lower at baseline in the lines without SMIM10 | 0.014 | ⚠ within organs, on part of the lines; also absent: SNAI2, MCAM, ZNF365 |
| [[SPTLC3]] | B | SMIM10 activity raises SPTLC3's level | lines that do not express SMIM10 (24) vs lines expressing it (26) | 1.76× lower at baseline in the lines without SMIM10 | 0.031 | ⚠ within organs, on part of the lines; also absent: SNAI2, MCAM, ZNF365 |
| [[FKBP7]] | B | SMIM10 activity raises FKBP7's level | lines that do not express SMIM10 (24) vs lines expressing it (26) | 1.82× lower at baseline in the lines without SMIM10 | 0.031 | ⚠ within organs, on part of the lines; also absent: SNAI2, MCAM, ZNF365 |
| [[RHOBTB3]] | B | SMIM10 activity raises RHOBTB3's level | lines that do not express SMIM10 (24) vs lines expressing it (26) | 2.43× lower at baseline in the lines without SMIM10 | 0.034 | ⚠ within organs, on part of the lines; also absent: SNAI2, MCAM, ZNF365 |
| [[CD302]] | B | SMIM10 activity raises CD302's level | lines that do not express SMIM10 (24) vs lines expressing it (26) | 1.80× lower at baseline in the lines without SMIM10 | 0.056 | ⚠ within organs, on part of the lines; also absent: SNAI2, MCAM, ZNF365 |
| [[MIR181A1HG]] | B | SMIM10 activity raises MIR181A1HG's level | lines that do not express SMIM10 (24) vs lines expressing it (26) | 2.23× lower at baseline in the lines without SMIM10 | 0.056 | ⚠ within organs, on part of the lines; also absent: SNAI2, MCAM, ZNF365 |
| [[ZC4H2]] | B | SMIM10 activity raises ZC4H2's level | lines that do not express SMIM10 (24) vs lines expressing it (26) | 1.93× lower at baseline in the lines without SMIM10 | 0.062 | ⚠ within organs, on part of the lines; also absent: SNAI2, MCAM, ZNF365 |
| [[MEF2C]] | B | SMIM10 activity raises MEF2C's level | lines that do not express SMIM10 (24) vs lines expressing it (26) | 3.06× lower at baseline in the lines without SMIM10 | 0.071 | ⚠ within organs, on part of the lines; also absent: SNAI2, MCAM, ZNF365 |
| [[EID1]] | B | SMIM10 activity raises EID1's level | lines that do not express SMIM10 (24) vs lines expressing it (26) | 1.56× lower at baseline in the lines without SMIM10 | 0.079 | ⚠ within organs, on part of the lines; also absent: SNAI2, MCAM, ZNF365 |

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.513). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (9.9, 5.3); signed map (-22.9, -3.8). **Vector** length 39.4, 8.23% of its response variance represented; |z| ≥ 3 in 397 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +4.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.5 | +11.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +9.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.6 | +5.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.5 | +4.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.3 | +2.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.2 | +2.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.2 | +2.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.0 | +1.0 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.6 | -3.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -1.5 | -4.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -1.4 | -3.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -1.3 | -7.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.3 | -2.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.2 | -2.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.1 | -3.4 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.9 | -1.8 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.9 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | small integral membrane protein 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq26.3 — chrX:134,990,991-134,992,473 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously CXorf69 |
| Matched by | ensembl_id |

UniProt [Q96HG1](https://www.uniprot.org/uniprotkb/Q96HG1) carries no function annotation.

**Summary**, from NCBI Gene [644538](https://www.ncbi.nlm.nih.gov/gene/644538):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:41913](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:41913) · Entrez [644538](https://www.ncbi.nlm.nih.gov/gene/644538) · UniProt [Q96HG1](https://www.uniprot.org/uniprotkb/Q96HG1) · Ensembl [ENSG00000184785](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184785)

## Data

Gene col 11574: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11574); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11574, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11574]; `tensor/DDL_lfc|DDL_z.npy` [11574]; `embed/gene_vectors.npy` [11574]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11574 or target_col == 11574). Every well: [[SMIM10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMIM10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
