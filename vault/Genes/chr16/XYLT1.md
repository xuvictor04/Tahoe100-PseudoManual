---
symbol: "XYLT1"
type: "gene"
col: 2371
ensembl_id: "ENSG00000103489"
name: "xylosyltransferase 1"
location: "16p12.3"
module: 73
arm: "+"
pooled_cpm: 47.43
n_lines_expressing: 25
n_dd_up: 17
n_dd_down: 5
n_dd_up_clean: 12
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 17
direction_downstream: 24
tags: ["gene", "module/073"]
generated_by: "tahoemap"
---

# XYLT1

*xylosyltransferase 1* — 16p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.26× (z +22.0, q 0e+00, up in 16 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.762× (z -4.8, q 8e-04, down in 4 of 23 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CYP3A5]] (+0.62, fdr 1e-05), [[SLC5A1]] (+0.59, fdr 1e-05), [[NUDT4]] (+0.58, fdr 1e-05); moves opposite to [[SYDE1]] (-0.46, fdr 1e-04), [[SMAD9]] (-0.43, fdr 4e-05).
> It is in [[Module 073]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 17 arrows point to it, the strongest [[CYP3A5]] → it (grade B ⚠); 24 go from it, the strongest it → [[NOSTRIN]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2371.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.26×** | +22.0 | 0e+00 | 16/23 (C32, BT-474, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.88×** | +17.0 | 0e+00 | 15/22 (C32, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.06×** | +13.3 | 7e-38 | 2/17 (J82, BT-474) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.87×** | +11.9 | 2e-30 | 5/22 (J82, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.75×** | +10.6 | 3e-24 | 12/23 (C32, BT-474, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.34×** | +5.6 | 2e-06 | 6/23 (C32, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.33×** | +5.4 | 6e-06 | 10/23 (C32, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.32×** | +5.1 | 3e-05 | 6/20 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.40×** | +4.6 | 3e-04 | 0/23 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **1.28×** | +4.6 | 3e-04 | 1/23 (C-33 A) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **1.24×** | +4.1 | 0.002 | 7/23 (C32, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.24×** | +4.0 | 0.003 | 6/23 (C32, SHP-77, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.47×** | +3.8 | 0.006 | 10/23 (COLO 205, LS 180, …) | top dose only | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.22×** | +3.8 | 0.007 | 12/22 (H4, SW48, …) | two highest doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~5% of this change | **1.20×** | +3.5 | 0.017 | 10/22 (C32, HS-578T, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.26×** | +3.1 | 0.057 | 2/23 (SK-MEL-2, NCI-H1573) | rises with dose | noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 1.18× | +3.1 | 0.057 | 2/23 (J82, A549) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | 1.18× | +3.1 | 0.058 | 2/23 (C32, BT-474) | inconsistent across doses |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | 1.17× | +2.9 | 0.087 | 1/23 (BT-474) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2371.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.762×** | -4.8 | 8e-04 | 4/23 (SW48, AsPC-1, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.641×** | -4.5 | 0.002 | 11/24 (KATO III, LS 180, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.660×** | -4.2 | 0.004 | 9/22 (LS 180, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.805×** | -4.2 | 0.004 | 9/23 (KATO III, SW1417, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.860× | -4.1 | 0.004 | 8/23 (SW48, J82, …) | top dose only | low cells (technical?) |
| [[TAK-733 (drug)]] 5 µM |  | **0.694×** | -3.7 | 0.024 | 7/23 (NCI-H1573, SW48, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 5 µM |  | 0.850× | -3.1 | 0.14 | 5/23 (NCI-H460, AsPC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.855× | -3.0 | 0.19 | 9/23 (LoVo, KATO III, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2371. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 200 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.196× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.311× (z -10.7) |
| [[COLO 205 (line)]] | alt | 124 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.239× (z -15.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.250× (z -10.3) |
| [[LoVo (line)]] | wt | 95.9 | 1 | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +10.8) | [[Dinaciclib (drug)]] 0.05 µM 0.382× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 207 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.285× (z -11.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.355× (z -9.5) |
| [[C32 (line)]] | wt | 18.1 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 14.5× (z +19.4) | — |
| [[LS 180 (line)]] | wt | 98.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.219× (z -13.0) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 252 | 1 | 2 (2 ⚠) | [[Trametinib (drug)]] 0.05 µM 2.10× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.252× (z -11.8) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 188 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.374× (z -12.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 21.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.79× (z +12.4) | — |
| [[HS-578T (line)]] | alt | 129 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +14.5) | — |
| [[NCI-H1573 (line)]] | alt | 39.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +11.4) | — |
| [[NCI-H596 (line)]] | alt | 67.8 | 0 | 1 | — | [[Citalopram (hydrobromide) (drug)]] 0.05 µM 0.123× (z -9.0) |
| [[SW1417 (line)]] | alt | 152 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.278× (z -17.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 5.03 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 11.6 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 4.81 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.46 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 9.31 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 152 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.26 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 5.40 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 5.76 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 5.15 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 10.2 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.04 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 57.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.46 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 7.08 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 6.58 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.06 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 4.24 n.m. | — | — | — | — |
| [[NCI-H661 (line)]] | alt | 8.15 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 4.66 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 6.27 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 6.06 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 77.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.91 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 6.92 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 68.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.53 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 8.04 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 7.98 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2371), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYP3A5]] | +0.62 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[SLC5A1]] | +0.59 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[NUDT4]] | +0.58 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[AUTS2]] | +0.58 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[PRSS3]] | +0.57 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[TPRXL]] | +0.56 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[MYO7B]] | +0.55 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[PRSS22]] | +0.55 | +0.41 / +0.41 | both halves | 4e-05 |  |
| [[DSG3]] | +0.55 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[LAMB3]] | +0.55 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[KCNH8]] | +0.54 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[LINC00589]] | +0.54 | +0.51 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SYDE1]] | -0.46 | -0.56 / -0.34 | both halves | 1e-04 |  |
| [[SMAD9]] | -0.43 | -0.45 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 1, C 16. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CYP3A5]] | B | CYP3A5 activity raises XYLT1's level | lines that do not express CYP3A5 (32) vs lines expressing it (18) | 2.04× lower at baseline in the lines without CYP3A5 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HHLA2, GCNT3, HNF4A |
| [[DSG3]] | C | DSG3 activity raises XYLT1's level | lines that do not express DSG3 (41) vs lines expressing it (9) | 5.66× lower at baseline in the lines without DSG3 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TFF2, TRIM31, NPSR1; co-absent with the target |
| [[ZBTB7C]] | C | ZBTB7C activity raises XYLT1's level | lines that do not express ZBTB7C (25) vs lines expressing it (25) | 3.91× lower at baseline in the lines without ZBTB7C | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000290808, FSTL4, PPARGC1A; co-absent with the target |
| [[INPP5D]] | C | INPP5D activity raises XYLT1's level | lines that do not express INPP5D (34) vs lines expressing it (16) | 3.08× lower at baseline in the lines without INPP5D | 0.020 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A, TP53; also absent: CLRN3, LINC02964, LGR5; co-absent with the target |
| [[LINC00589]] | C | LINC00589 activity raises XYLT1's level | lines that do not express LINC00589 (28) vs lines expressing it (22) | 3.28× lower at baseline in the lines without LINC00589 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00520, ENSG00000267881, TSPAN8; co-absent with the target |
| [[KLK10]] | C | KLK10 activity raises XYLT1's level | lines that do not express KLK10 (34) vs lines expressing it (16) | 2.64× lower at baseline in the lines without KLK10 | 0.032 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, HS3ST1, IRF6; co-absent with the target |
| [[GCNT3]] | C | GCNT3 activity raises XYLT1's level | lines that do not express GCNT3 (38) vs lines expressing it (12) | 3.04× lower at baseline in the lines without GCNT3 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, LYZ, MUC13; co-absent with the target |
| [[PKP1]] | C | PKP1 activity raises XYLT1's level | lines that do not express PKP1 (33) vs lines expressing it (17) | 2.52× lower at baseline in the lines without PKP1 | 0.048 | ⚠ within organs, on part of the lines; also absent: SERPINB5, TFF2, CLIC5; co-absent with the target |
| [[LINC01133]] | C | LINC01133 activity raises XYLT1's level | lines that do not express LINC01133 (34) vs lines expressing it (16) | 3.80× lower at baseline in the lines without LINC01133 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HEPH, IL33, UGT1A1; co-absent with the target |
| [[NPSR1]] | C | NPSR1 activity raises XYLT1's level | lines that do not express NPSR1 (42) vs lines expressing it (8) | 4.76× lower at baseline in the lines without NPSR1 | 0.054 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, MUC17, CDH17; co-absent with the target |
| [[TFF2]] | C | TFF2 activity raises XYLT1's level | lines that do not express TFF2 (39) vs lines expressing it (11) | 3.03× lower at baseline in the lines without TFF2 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG3, ENSG00000250920, TRIM31; co-absent with the target |
| [[HNF4A]] | C | HNF4A activity raises XYLT1's level | lines that do not express HNF4A (34) vs lines expressing it (16) | 2.57× lower at baseline in the lines without HNF4A | 0.064 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: EPS8L3, GCNT3, LINC02964; co-absent with the target |

### Downstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 10, C 14. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NOSTRIN]] | B | XYLT1 activity raises NOSTRIN's level | lines that do not express XYLT1 (25) vs lines expressing it (25) | 2.06× lower at baseline in the lines without XYLT1 | 0.018 | ⚠ within organs, on part of the lines; also absent: LINC02055, CADPS, MGC32805 |
| [[FA2H]] | B | XYLT1 activity raises FA2H's level | lines that do not express XYLT1 (25) vs lines expressing it (25) | 1.89× lower at baseline in the lines without XYLT1 | 0.033 | ⚠ within organs, on part of the lines; also absent: LINC02055, CADPS, MGC32805 |
| [[CEP250]] | B | XYLT1 activity lowers CEP250's level | lines that do not express XYLT1 (25) vs lines expressing it (25) | 1.21× higher at baseline in the lines without XYLT1 | 0.039 | ⚠ within organs, on part of the lines; also absent: LINC02055, CADPS, MGC32805 |
| [[MAP7]] | B | XYLT1 activity raises MAP7's level | lines that do not express XYLT1 (25) vs lines expressing it (25) | 1.97× lower at baseline in the lines without XYLT1 | 0.050 | ⚠ within organs, on part of the lines; also absent: LINC02055, CADPS, MGC32805 |
| [[NCALD]] | B | XYLT1 activity raises NCALD's level | lines that do not express XYLT1 (25) vs lines expressing it (25) | 2.36× lower at baseline in the lines without XYLT1 | 0.052 | ⚠ within organs, on part of the lines; also absent: LINC02055, CADPS, MGC32805 |
| [[SDCBP2]] | B | XYLT1 activity raises SDCBP2's level | lines that do not express XYLT1 (25) vs lines expressing it (25) | 2.10× lower at baseline in the lines without XYLT1 | 0.055 | ⚠ within organs, on part of the lines; also absent: LINC02055, CADPS, MGC32805 |
| [[IL2RG]] | B | XYLT1 activity raises IL2RG's level | lines that do not express XYLT1 (25) vs lines expressing it (25) | 1.30× lower at baseline in the lines without XYLT1 | 0.059 | ⚠ within organs, on part of the lines; also absent: LINC02055, CADPS, MGC32805 |
| [[TFF1]] | B | XYLT1 activity raises TFF1's level | lines that do not express XYLT1 (25) vs lines expressing it (25) | 1.71× lower at baseline in the lines without XYLT1 | 0.071 | ⚠ within organs, on part of the lines; also absent: LINC02055, CADPS, MGC32805 |
| [[NRXN3]] | B | XYLT1 activity raises NRXN3's level | lines that do not express XYLT1 (25) vs lines expressing it (25) | 2.96× lower at baseline in the lines without XYLT1 | 0.092 | ⚠ within organs, on part of the lines; also absent: LINC02055, CADPS, MGC32805 |
| [[SULT2B1]] | B | XYLT1 activity raises SULT2B1's level | lines that do not express XYLT1 (25) vs lines expressing it (25) | 1.82× lower at baseline in the lines without XYLT1 | 0.0997 | ⚠ within organs, on part of the lines; also absent: LINC02055, CADPS, MGC32805 |
| [[HNF4A]] | C | XYLT1 activity raises HNF4A's level | lines that do not express XYLT1 (25) vs lines expressing it (25) | 2.17× lower at baseline in the lines without XYLT1 | 0.007 | ⚠ within organs, on part of the lines; also absent: LINC02055, CADPS, MGC32805; co-absent with the target |
| [[DSG3]] | C | XYLT1 activity raises DSG3's level | lines that do not express XYLT1 (25) vs lines expressing it (25) | 2.12× lower at baseline in the lines without XYLT1 | 0.010 | ⚠ within organs, on part of the lines; also absent: LINC02055, CADPS, MGC32805; co-absent with the target |

## Where it sits

- **Module**: [[Module 073]]; 66 genes; every member is in the + arm (projection on the module's main direction 0.579). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (16.7, 52.7); signed map (67.3, 12.4). **Vector** length 75.2, 20.0% of its response variance represented; |z| ≥ 3 in 685 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.3 | +11.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.6 | +13.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.5 | +22.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +6.1 | +2.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.5 | +10.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +3.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +0.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +4.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.1 | +3.1 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -2.5 | -0.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.3 | -4.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.2 | -4.8 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.9 | -3.1 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.8 | -2.3 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.8 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | xylosyltransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p12.3 — chr16:17,101,769-17,470,960 (-) |
| Ensembl biotype | protein_coding |
| Also known as | XT-I, PXYLT1 |
| Gene groups (HGNC) | Glucosaminyl (N-acetyl) transferases/xylosyltransferases |
| Reactome | 3 pathways, smallest: Glycosaminoglycan-protein linkage region biosynthesis; Glycosaminoglycan metabolism; Metabolism of carbohydrates and carbohydrate derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86Y38](https://www.uniprot.org/uniprotkb/Q86Y38) (Xylosyltransferase 1):

> Catalyzes the first step in the biosynthesis of chondroitin sulfate and dermatan sulfate proteoglycans, such as DCN. Transfers D-xylose from UDP-D-xylose to specific serine residues of the core protein. Required for normal embryonic and postnatal skeleton development, especially of the long bones. Required for normal maturation of chondrocytes during bone development, and normal onset of ossification (By similarity).

**Summary**, from NCBI Gene [64131](https://www.ncbi.nlm.nih.gov/gene/64131):

> This locus encodes a xylosyltransferase enzyme. The encoded protein catalyzes transfer of UDP-xylose to serine residues of an acceptor protein substrate. This transfer reaction is necessary for biosynthesis of glycosaminoglycan chains. Mutations in this gene have been associated with increased severity of pseudoxanthoma elasticum.[provided by RefSeq, Nov 2009]

**Accessions** — [HGNC:15516](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15516) · Entrez [64131](https://www.ncbi.nlm.nih.gov/gene/64131) · UniProt [Q86Y38](https://www.uniprot.org/uniprotkb/Q86Y38) · Ensembl [ENSG00000103489](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103489)

## Data

Gene col 2371: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2371); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2371, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2371]; `tensor/DDL_lfc|DDL_z.npy` [2371]; `embed/gene_vectors.npy` [2371]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2371 or target_col == 2371). Every well: [[XYLT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/XYLT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
