---
symbol: "MOGAT3"
type: "gene"
col: 2753
ensembl_id: "ENSG00000106384"
name: "monoacylglycerol O-acyltransferase 3"
location: "7q22.1"
module: 31
arm: "+"
pooled_cpm: 2.68
n_lines_expressing: 20
n_dd_up: 18
n_dd_down: 1
n_dd_up_clean: 9
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 16
direction_downstream: 43
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# MOGAT3

*monoacylglycerol O-acyltransferase 3* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.02× (z +13.6, q 2e-39, up in 4 of 12 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM: 0.506× (z -4.1, q 0.020, down in 6 of 16 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (KATO III 0.165×, SW1417 0.313×, HT-29 0.244×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (HT-29 0.154×, KATO III 0.187×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (SW480 0.105×; ⚠ cell-cycle shift, would explain all of this change); [[PH-797804 (drug)]] 5 µM in 1 line (SW480 0.0284×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LPAR5]] (+0.68, fdr 8e-06), [[RGL3]] (+0.57, fdr 6e-05), [[PTK6]] (+0.57, fdr 1e-05); moves opposite to [[CAPRIN1]] (-0.54, fdr 3e-05), [[SMARCD1]] (-0.46, fdr 2e-04), [[EIF3F]] (-0.46, fdr 3e-04).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[TPST1]] → it (grade B ⚠); 43 go from it, the strongest it → [[TLDC2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2753.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.02×** | +13.6 | 2e-39 | 4/12 (C32, LoVo, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.39×** | +8.8 | 3e-16 | 2/7 (LS 180, HepG2/C3A) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.34×** | +8.4 | 7e-15 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.39×** | +7.3 | 4e-11 | 5/12 (SW1417, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **2.20×** | +6.6 | 4e-09 | 9/15 (KATO III, LS 180, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.08×** | +6.2 | 5e-08 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.81×** | +4.2 | 0.003 | 1/3 (HepG2/C3A) | top dose only | noisy plate (z scaled) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.57×** | +4.0 | 0.004 | 0/7 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.92×** | +3.9 | 0.006 | 8/14 (SW480, HT-29, …) | top dose only | position effect removed |
| [[Selinexor (drug)]] 0.5 µM |  | **1.92×** | +3.9 | 0.006 | 10/13 (KATO III, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.44×** | +3.8 | 0.008 | 3/7 (SW1417, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.93×** | +3.7 | 0.008 | 1/7 (AsPC-1) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.88×** | +3.7 | 0.008 | 4/10 (SW1417, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.85×** | +3.6 | 0.011 | 8/15 (KATO III, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.76×** | +3.3 | 0.032 | 1/7 (AsPC-1) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.43×** | +3.0 | 0.094 | 6/14 (LS 180, KATO III, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2753.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (KATO III 0.165×, SW1417 0.313×, HT-29 0.244×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (HT-29 0.154×, KATO III 0.187×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (SW480 0.105×; ⚠ cell-cycle shift, would explain all of this change); [[PH-797804 (drug)]] 5 µM in 1 line (SW480 0.0284×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **0.506×** | -4.1 | 0.020 | 6/16 (RPMI-7951, AsPC-1, …) | all doses, flat | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.530× | -3.6 | 0.10 | 4/16 (C32, KATO III, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | 0.606× | -3.1 | 0.40 | 5/15 (SK-MEL-2, LoVo, …) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2753. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 13.2 | 1 | 2 | [[Selinexor (drug)]] 5 µM 5.06× (z +9.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.165× (z -11.0) |
| [[HT-29 (line)]] | alt | 11.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -11.7) |
| [[SW1417 (line)]] | alt | 21.9 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -9.3) |
| [[SW480 (line)]] | alt | 4.95 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.105× (z -10.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0284× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 24.2 | 1 | 0 | [[Selinexor (drug)]] 5 µM 3.49× (z +8.8) | — |
| [[LS 180 (line)]] | wt | 6.26 | 1 | 0 | [[Selinexor (drug)]] 5 µM 7.26× (z +9.3) | — |
| [[A-172 (line)]] | wt | 0.433 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.390 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.459 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.362 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.781 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.316 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.389 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.547 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.394 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.386 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.803 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.803 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.390 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.638 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.366 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.430 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.340 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.962 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.890 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.398 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.854 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.287 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.427 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.631 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.309 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.266 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.451 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.578 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.283 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.396 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.832 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.286 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.808 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.333 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.437 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.973 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.299 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.426 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.439 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2753), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LPAR5]] | +0.68 | +0.58 / +0.67 | both halves | 8e-06 |  |
| [[RGL3]] | +0.57 | +0.39 / +0.57 | both halves | 6e-05 |  |
| [[PTK6]] | +0.57 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[RINL]] | +0.56 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[CBLC]] | +0.56 | +0.34 / +0.57 | both halves | 1e-04 |  |
| [[DOCK6]] | +0.56 | +0.28 / +0.68 | both halves | 3e-04 |  |
| [[NGFR]] | +0.55 | +0.38 / +0.59 | both halves | 6e-05 |  |
| [[NGEF]] | +0.54 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[VAV1]] | +0.54 | +0.52 / +0.42 | both halves | 4e-05 |  |
| [[SLC5A1]] | +0.54 | +0.64 / +0.41 | both halves | 4e-05 |  |
| [[SLC22A18]] | +0.53 | +0.34 / +0.60 | both halves | 1e-04 |  |
| [[AMN]] | +0.53 | +0.38 / +0.54 | both halves | 6e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAPRIN1]] | -0.54 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[SMARCD1]] | -0.46 | -0.32 / -0.46 | both halves | 2e-04 |  |
| [[EIF3F]] | -0.46 | -0.28 / -0.46 | both halves | 3e-04 |  |
| [[LAMP1]] | -0.44 | -0.38 / -0.42 | both halves | 6e-05 |  |
| [[AP2M1]] | -0.43 | -0.37 / -0.39 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 2, C 14. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TPST1]] | B | TPST1 activity lowers MOGAT3's level | lines that do not express TPST1 (5) vs lines expressing it (45) | 6.13× higher at baseline in the lines without TPST1 | 0.027 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CYP46A1, CSRP2, MYO5A |
| [[LYPD3]] | B | LYPD3 activity raises MOGAT3's level | lines that do not express LYPD3 (15) vs lines expressing it (35) | 1.90× lower at baseline in the lines without LYPD3 | 0.073 | ⚠ within organs, on part of the lines; also absent: ENSG00000259345, ENSG00000256982, IGSF9; maybe low, not absent |
| [[CLRN3]] | C | CLRN3 activity raises MOGAT3's level | lines that do not express CLRN3 (40) vs lines expressing it (10) | 4.69× lower at baseline in the lines without CLRN3 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13; co-absent with the target |
| [[TFF3]] | C | TFF3 activity raises MOGAT3's level | lines that do not express TFF3 (38) vs lines expressing it (12) | 3.42× lower at baseline in the lines without TFF3 | 0.003 | ⚠ within organs, on part of the lines; also absent: CEACAM5, MUC17, AGR3; co-absent with the target |
| [[AZGP1]] | C | AZGP1 activity raises MOGAT3's level | lines that do not express AZGP1 (35) vs lines expressing it (15) | 3.72× lower at baseline in the lines without AZGP1 | 0.006 | ⚠ within organs, on part of the lines; also absent: GJB1, PROM1, LYZ; co-absent with the target |
| [[LINC01819]] | C | LINC01819 activity raises MOGAT3's level | lines that do not express LINC01819 (29) vs lines expressing it (21) | 2.82× lower at baseline in the lines without LINC01819 | 0.007 | ⚠ within organs, on part of the lines; also absent: MOGAT3, LGR6, A1CF; maybe low, not absent; co-absent with the target |
| [[LINC03040]] | C | LINC03040 activity raises MOGAT3's level | lines that do not express LINC03040 (31) vs lines expressing it (19) | 2.74× lower at baseline in the lines without LINC03040 | 0.017 | ⚠ within organs, on part of the lines; also absent: SLC44A4, EPS8L3, LCN2; co-absent with the target |
| [[USH1C]] | C | USH1C activity raises MOGAT3's level | lines that do not express USH1C (34) vs lines expressing it (16) | 2.47× lower at baseline in the lines without USH1C | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC13, CLRN3, HHLA2; co-absent with the target |
| [[ADCY4]] | C | ADCY4 activity raises MOGAT3's level | lines that do not express ADCY4 (33) vs lines expressing it (17) | 2.45× lower at baseline in the lines without ADCY4 | 0.036 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, SLC5A1, CLIC5; co-absent with the target |
| [[EPHA1]] | C | EPHA1 activity raises MOGAT3's level | lines that do not express EPHA1 (23) vs lines expressing it (27) | 2.22× lower at baseline in the lines without EPHA1 | 0.048 | ⚠ within organs, on part of the lines; also absent: TNNT2, KDF1, PLEKHG6; maybe low, not absent; co-absent with the target |
| [[SULT2B1]] | C | SULT2B1 activity raises MOGAT3's level | lines that do not express SULT2B1 (28) vs lines expressing it (22) | 1.95× lower at baseline in the lines without SULT2B1 | 0.061 | ⚠ within organs, on part of the lines; also absent: ATP2C2, ST14, SGPP2; maybe low, not absent; co-absent with the target |
| [[CYP3A5]] | C | CYP3A5 activity raises MOGAT3's level | lines that do not express CYP3A5 (32) vs lines expressing it (18) | 2.55× lower at baseline in the lines without CYP3A5 | 0.064 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HHLA2, GCNT3, HNF4A; co-absent with the target |

### Downstream of this gene

*43 arrows, 43 of them with an alert ⚠; grade A 0, B 18, C 25. Shown: the 12 strongest; 31 more arrows (31 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TLDC2]] | B | MOGAT3 activity raises TLDC2's level | lines that do not express MOGAT3 (30) vs lines expressing it (20) | 2.11× lower at baseline in the lines without MOGAT3 | 0.002 | ⚠ within organs, on part of the lines; also absent: VIL1, LINC02964, LINC01819 |
| [[FUT2]] | B | MOGAT3 activity raises FUT2's level | lines that do not express MOGAT3 (30) vs lines expressing it (20) | 2.23× lower at baseline in the lines without MOGAT3 | 0.015 | ⚠ within organs, on part of the lines; also absent: VIL1, LINC02964, LINC01819 |
| [[PTK6]] | B | MOGAT3 activity raises PTK6's level | lines that do not express MOGAT3 (30) vs lines expressing it (20) | 1.74× lower at baseline in the lines without MOGAT3 | 0.019 | ⚠ within organs, on part of the lines; also absent: VIL1, LINC02964, LINC01819 |
| [[BAIAP2L1]] | B | MOGAT3 activity raises BAIAP2L1's level | lines that do not express MOGAT3 (30) vs lines expressing it (20) | 1.69× lower at baseline in the lines without MOGAT3 | 0.021 | ⚠ within organs, on part of the lines; also absent: VIL1, LINC02964, LINC01819 |
| [[ACOT11]] | B | MOGAT3 activity raises ACOT11's level | lines that do not express MOGAT3 (30) vs lines expressing it (20) | 2.23× lower at baseline in the lines without MOGAT3 | 0.030 | ⚠ within organs, on part of the lines; also absent: VIL1, LINC02964, LINC01819 |
| [[LINC01290]] | B | MOGAT3 activity raises LINC01290's level | lines that do not express MOGAT3 (30) vs lines expressing it (20) | 1.62× lower at baseline in the lines without MOGAT3 | 0.039 | ⚠ within organs, on part of the lines; also absent: VIL1, LINC02964, LINC01819 |
| [[FAM83E]] | B | MOGAT3 activity raises FAM83E's level | lines that do not express MOGAT3 (30) vs lines expressing it (20) | 2.51× lower at baseline in the lines without MOGAT3 | 0.049 | ⚠ within organs, on part of the lines; also absent: VIL1, LINC02964, LINC01819 |
| [[HAP1]] | B | MOGAT3 activity raises HAP1's level | lines that do not express MOGAT3 (30) vs lines expressing it (20) | 1.30× lower at baseline in the lines without MOGAT3 | 0.056 | ⚠ within organs, on part of the lines; also absent: VIL1, LINC02964, LINC01819 |
| [[EPHB3]] | B | MOGAT3 activity raises EPHB3's level | lines that do not express MOGAT3 (30) vs lines expressing it (20) | 2.50× lower at baseline in the lines without MOGAT3 | 0.061 | ⚠ within organs, on part of the lines; also absent: VIL1, LINC02964, LINC01819 |
| [[SLC22A18]] | B | MOGAT3 activity raises SLC22A18's level | lines that do not express MOGAT3 (30) vs lines expressing it (20) | 1.74× lower at baseline in the lines without MOGAT3 | 0.073 | ⚠ within organs, on part of the lines; also absent: VIL1, LINC02964, LINC01819 |
| [[LYPD3]] | B | MOGAT3 activity raises LYPD3's level | lines that do not express MOGAT3 (30) vs lines expressing it (20) | 1.34× lower at baseline in the lines without MOGAT3 | 0.079 | ⚠ within organs, on part of the lines; also absent: VIL1, LINC02964, LINC01819 |
| cells under [[Infigratinib (drug)]] 0.5 µM | B | MOGAT3 activity raises the cells' numbers under Infigratinib 0.5 µM (protects the cells) | lines that do not express MOGAT3 (30) vs lines expressing it (18) | the lines without MOGAT3: 0.87× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: VIL1, LINC02964, LINC01819 |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.507). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.1, 57.1); signed map (-2.3, 39.6). **Vector** length 35.5, 8.57% of its response variance represented; |z| ≥ 3 in 374 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +3.4 | +6.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +3.0 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +2.6 | +3.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | +2.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.4 | +8.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.7 | +3.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +3.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.2 | +2.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.1 | +0.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -2.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.5 | -0.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -0.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -3.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.0 | -0.4 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.9 | -2.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -1.4 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -0.8 | -2.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -0.8 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | monoacylglycerol O-acyltransferase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:101,195,007-101,201,038 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DC7, MGAT3, DGAT2L2 |
| Gene groups (HGNC) | Diacylglycerol O-acyltransferase 2 family |
| Reactome | 3 pathways, smallest: Triglyceride biosynthesis; Triglyceride metabolism; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86VF5](https://www.uniprot.org/uniprotkb/Q86VF5) (2-acylglycerol O-acyltransferase 3):

> Catalyzes the formation of diacylglycerol from 2-monoacylglycerol and fatty acyl-CoA. Also able to catalyze the terminal step in triacylglycerol synthesis by using diacylglycerol and fatty acyl-CoA as substrates. Has a preference toward palmitoyl-CoA and oleoyl-CoA. May be involved in absorption of dietary fat in the small intestine by catalyzing the resynthesis of triacylglycerol in enterocytes. Also able to use 1-monoalkylglycerol (1-MAkG) as an acyl acceptor for the synthesis of …

**Summary**, from NCBI Gene [346606](https://www.ncbi.nlm.nih.gov/gene/346606):

> Acyl-CoA:monoacylglycerol acyltransferase (MOGAT; EC 2.3.1.22) catalyzes the synthesis of diacylglycerol from 2-monoacylglycerol and fatty acyl-CoA (Cheng et al., 2003 [PubMed 12618427]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:23249](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23249) · Entrez [346606](https://www.ncbi.nlm.nih.gov/gene/346606) · UniProt [Q86VF5](https://www.uniprot.org/uniprotkb/Q86VF5) · Ensembl [ENSG00000106384](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106384)

## Data

Gene col 2753: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2753); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2753, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2753]; `tensor/DDL_lfc|DDL_z.npy` [2753]; `embed/gene_vectors.npy` [2753]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2753 or target_col == 2753). Every well: [[MOGAT3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MOGAT3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
