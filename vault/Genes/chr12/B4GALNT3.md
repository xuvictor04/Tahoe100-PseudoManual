---
symbol: "B4GALNT3"
type: "gene"
col: 6256
ensembl_id: "ENSG00000139044"
name: "beta-1,4-N-acetyl-galactosaminyltransferase 3"
location: "12p13.33"
module: 31
arm: "+"
pooled_cpm: 46.15
n_lines_expressing: 34
n_dd_up: 12
n_dd_down: 17
n_dd_up_clean: 8
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 26
direction_downstream: 36
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# B4GALNT3

*beta-1,4-N-acetyl-galactosaminyltransferase 3* — 12p13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.30× (z +13.0, q 1e-35, up in 13 of 24 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.58× (z +10.4, q 5e-23, up in 18 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.498× (z -15.9, q 0e+00, down in 26 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC6A20]] (+0.63, fdr 1e-05), [[TMC6]] (+0.62, fdr 7e-06), [[KIAA0040]] (+0.62, fdr 1e-05); moves opposite to [[AMACR]] (-0.56, fdr 3e-05), [[PUS10]] (-0.49, fdr 1e-04).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 26 arrows point to it, the strongest [[BLACAT1]] → it (grade B ⚠); 36 go from it, the strongest it → [[BLACAT1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6256.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.30×** | +13.0 | 1e-35 | 13/24 (HOP62, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.58×** | +10.4 | 5e-23 | 18/32 (HOP62, SW480, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +7.3 | 7e-11 | 10/32 (HepG2/C3A, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.51×** | +6.7 | 4e-09 | 9/29 (HOP62, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.11×** | +6.3 | 3e-08 | 13/28 (NCI-H23, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.50×** | +6.2 | 7e-08 | 14/32 (HOP62, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.40×** | +5.0 | 4e-05 | 5/27 (HOP62, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.34×** | +4.7 | 2e-04 | 10/31 (HOP62, A-427, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.39×** | +3.8 | 0.009 | 6/29 (SW480, HepG2/C3A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | **1.27×** | +3.6 | 0.016 | 6/29 (A-427, SW480, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.24×** | +3.5 | 0.020 | 6/32 (HOP62, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.35×** | +3.5 | 0.025 | 6/33 (HOP62, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6256.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.498×** | -15.9 | 0e+00 | 26/31 (A-427, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.461×** | -11.7 | 4e-29 | 22/31 (A-427, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.623×** | -7.4 | 3e-11 | 21/30 (A-427, RKO, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.663×** | -6.6 | 4e-09 | 18/30 (SW48, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.667×** | -6.5 | 7e-09 | 20/32 (LoVo, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~22% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.464×** | -6.5 | 8e-09 | 25/33 (LS 180, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.705×** | -5.4 | 4e-06 | 17/31 (SW480, SW 900, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.733×** | -4.6 | 3e-04 | 13/31 (Panc 03.27, SW480, …) | all doses, flat |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.583×** | -4.6 | 3e-04 | 14/29 (LS 180, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.759×** | -4.5 | 5e-04 | 14/31 (LoVo, COLO 205, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.838× | -4.0 | 0.003 | 17/32 (SW48, SW 900, …) | top dose only | low cells (technical?) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **0.790×** | -3.8 | 0.007 | 15/29 (SW480, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.784×** | -3.8 | 0.007 | 12/31 (Panc 03.27, SW48, …) | all doses, flat |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.642×** | -3.7 | 0.007 | 11/30 (Panc 03.27, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.800×** | -3.6 | 0.012 | 16/32 (Panc 03.27, BT-474, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.805×** | -3.5 | 0.016 | 10/31 (CFPAC-1, SW1417, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.823×** | -3.3 | 0.028 | 12/33 (HOP62, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.859× | -3.3 | 0.031 | 12/32 (Panc 03.27, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6256. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 86.1 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -22.6) |
| [[LoVo (line)]] | wt | 287 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -17.3) |
| [[LS 180 (line)]] | wt | 184 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -20.0) |
| [[SW48 (line)]] | wt | 138 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -20.6) |
| [[A-427 (line)]] | wt | 71.1 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0607× (z -29.5) |
| [[HOP62 (line)]] | alt | 22.4 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 12.3× (z +16.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 4.68× (z +10.8) | — |
| [[SK-MEL-2 (line)]] | alt | 88.3 | 1 (1 ⚠) | 4 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.80× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -17.7) |
| [[HEC-1-A (line)]] | alt | 44.4 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -14.5) |
| [[HepG2_C3A (line)]] | wt | 24.5 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.99× (z +9.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.55× (z +8.9) | — |
| [[KATO III (line)]] | alt | 150 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -16.4) |
| [[NCI-H23 (line)]] | alt | 28.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -16.4) |
| [[Panc 03.27 (line)]] | alt | 78.3 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.235× (z -10.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.427× (z -9.2) |
| [[C-33 A (line)]] | alt | 53.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -20.6) |
| [[MIA PaCa-2 (line)]] | alt | 26.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -12.4) |
| [[SW 900 (line)]] | alt | 84.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.64× (z +10.1) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 19.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -10.5) |
| [[C32 (line)]] | wt | 27.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -16.7) |
| [[HCT15 (line)]] | alt | 29.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -9.3) |
| [[HT-29 (line)]] | alt | 162 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 26.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -9.1) |
| [[NCI-H1792 (line)]] | alt | 21.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.101× (z -20.0) |
| [[SW480 (line)]] | alt | 61.5 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.31× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[A498 (line)]] | wt | 7.25 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 10.1 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.2 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 6.84 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.80 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.97 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 6.40 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.78 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 5.86 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 76.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 49.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.33 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.3 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 8.08 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.68 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 9.16 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 6.08 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.78 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 28.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6256), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC6A20]] | +0.63 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[TMC6]] | +0.62 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[KIAA0040]] | +0.62 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[PRSS3]] | +0.61 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[TMPRSS4]] | +0.61 | +0.57 / +0.63 | both halves | 8e-06 |  |
| [[SPON1]] | +0.61 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[BAIAP2L1]] | +0.60 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[RDH13]] | +0.59 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[KLK10]] | +0.59 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[LEMD1]] | +0.58 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[PRR5-ARHGAP8]] | +0.58 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[EPS8L1]] | +0.57 | +0.45 / +0.64 | both halves | 3e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AMACR]] | -0.56 | -0.58 / -0.46 | both halves | 3e-05 |  |
| [[PUS10]] | -0.49 | -0.58 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*26 arrows, 26 of them with an alert ⚠; grade A 0, B 22, C 4. Shown: the 12 strongest; 14 more arrows (14 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BLACAT1]] | B | BLACAT1 activity raises B4GALNT3's level | lines that do not express BLACAT1 (21) vs lines expressing it (29) | 3.00× lower at baseline in the lines without BLACAT1 | 0.012 | ⚠ within organs, on part of the lines; also absent: LEMD1, MPZL3, SULT1C2 |
| [[SLC6A20]] | B | SLC6A20 activity raises B4GALNT3's level | lines that do not express SLC6A20 (38) vs lines expressing it (12) | 4.59× lower at baseline in the lines without SLC6A20 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KLK11, REG4, HEPH |
| [[LINC02474]] | B | LINC02474 activity raises B4GALNT3's level | lines that do not express LINC02474 (40) vs lines expressing it (10) | 3.77× lower at baseline in the lines without LINC02474 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC4, SFTPA2, ENSG00000230975 |
| [[CBLC]] | B | CBLC activity raises B4GALNT3's level | lines that do not express CBLC (31) vs lines expressing it (19) | 3.22× lower at baseline in the lines without CBLC | 0.016 | ⚠ within organs, on part of the lines; also absent: KDF1, CLDN7, PRSS8 |
| [[MUC2]] | B | MUC2 activity raises B4GALNT3's level | lines that do not express MUC2 (42) vs lines expressing it (8) | 3.22× lower at baseline in the lines without MUC2 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000248588, DSG4 |
| [[C6orf132]] | B | C6orf132 activity raises B4GALNT3's level | lines that do not express C6orf132 (27) vs lines expressing it (23) | 2.68× lower at baseline in the lines without C6orf132 | 0.027 | ⚠ within organs, on part of the lines; also absent: PCSK9, RNF223, CDH1 |
| [[TMPRSS4]] | B | TMPRSS4 activity raises B4GALNT3's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 3.39× lower at baseline in the lines without TMPRSS4 | 0.043 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[DSG4]] | B | DSG4 activity raises B4GALNT3's level | lines that do not express DSG4 (45) vs lines expressing it (5) | 5.69× lower at baseline in the lines without DSG4 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, GPR15, ENSG00000237031 |
| [[LAMA3]] | B | LAMA3 activity raises B4GALNT3's level | lines that do not express LAMA3 (22) vs lines expressing it (28) | 2.45× lower at baseline in the lines without LAMA3 | 0.051 | ⚠ within organs, on part of the lines; also absent: P2RY2, ELF3, MYO5B |
| [[SEMA3B]] | B | SEMA3B activity raises B4GALNT3's level | lines that do not express SEMA3B (19) vs lines expressing it (31) | 2.02× lower at baseline in the lines without SEMA3B | 0.053 | ⚠ within organs, on part of the lines; also absent: SERPINA1, CSF1R, TNNT2; maybe low, not absent |
| [[TINAGL1]] | B | TINAGL1 activity raises B4GALNT3's level | lines that do not express TINAGL1 (26) vs lines expressing it (24) | 2.52× lower at baseline in the lines without TINAGL1 | 0.056 | ⚠ within organs, on part of the lines; also absent: IL20RA, MSLN, KRT19 |
| [[MAP2K1]] | B | MAP2K1 activity raises B4GALNT3's level | compounds that target MAP2K1: 3 of 4 lower it (Cobimetinib, TAK-733, Trametinib) | 75% of the class's compounds vs 3.1% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

*36 arrows, 36 of them with an alert ⚠; grade A 0, B 32, C 4. Shown: the 12 strongest; 24 more arrows (24 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BLACAT1]] | B | B4GALNT3 activity raises BLACAT1's level | lines that do not express B4GALNT3 (16) vs lines expressing it (34) | 2.58× lower at baseline in the lines without B4GALNT3 | 0.007 | ⚠ within organs, on part of the lines; also absent: MCF2L, EPHA1, PLEKHG6 |
| [[TMC6]] | B | B4GALNT3 activity raises TMC6's level | lines that do not express B4GALNT3 (16) vs lines expressing it (34) | 3.72× lower at baseline in the lines without B4GALNT3 | 0.010 | ⚠ within organs, on part of the lines; also absent: MCF2L, EPHA1, PLEKHG6 |
| [[SEMA3B]] | B | B4GALNT3 activity raises SEMA3B's level | lines that do not express B4GALNT3 (16) vs lines expressing it (34) | 3.21× lower at baseline in the lines without B4GALNT3 | 0.010 | ⚠ within organs, on part of the lines; also absent: MCF2L, EPHA1, PLEKHG6 |
| [[CBLC]] | B | B4GALNT3 activity raises CBLC's level | lines that do not express B4GALNT3 (16) vs lines expressing it (34) | 3.42× lower at baseline in the lines without B4GALNT3 | 0.012 | ⚠ within organs, on part of the lines; also absent: MCF2L, EPHA1, PLEKHG6 |
| [[ATP11A]] | B | B4GALNT3 activity raises ATP11A's level | lines that do not express B4GALNT3 (16) vs lines expressing it (34) | 2.35× lower at baseline in the lines without B4GALNT3 | 0.012 | ⚠ within organs, on part of the lines; also absent: MCF2L, EPHA1, PLEKHG6 |
| [[C6orf132]] | B | B4GALNT3 activity raises C6orf132's level | lines that do not express B4GALNT3 (16) vs lines expressing it (34) | 3.93× lower at baseline in the lines without B4GALNT3 | 0.021 | ⚠ within organs, on part of the lines; also absent: MCF2L, EPHA1, PLEKHG6 |
| [[SPATA13]] | B | B4GALNT3 activity raises SPATA13's level | lines that do not express B4GALNT3 (16) vs lines expressing it (34) | 2.38× lower at baseline in the lines without B4GALNT3 | 0.021 | ⚠ within organs, on part of the lines; also absent: MCF2L, EPHA1, PLEKHG6 |
| [[DBNDD1]] | B | B4GALNT3 activity strengthens DBNDD1's drug response | lines that do not express B4GALNT3 (14) vs lines expressing it (30) | the lines without B4GALNT3 respond 0.46× as strongly (z diff +1.77); strongest at Homoharringtonine 5 µM: 1.41x vs 0.40x (z diff +7.0) | 0.033 | ⚠ within organs, on part of the lines; also absent: MCF2L, EPHA1, PLEKHG6; target measured in part of the lines; artifact flags |
| [[IQANK1]] | B | B4GALNT3 activity raises IQANK1's level | lines that do not express B4GALNT3 (16) vs lines expressing it (34) | 2.73× lower at baseline in the lines without B4GALNT3 | 0.033 | ⚠ within organs, on part of the lines; also absent: MCF2L, EPHA1, PLEKHG6 |
| [[TMPRSS4]] | B | B4GALNT3 activity raises TMPRSS4's level | lines that do not express B4GALNT3 (16) vs lines expressing it (34) | 4.24× lower at baseline in the lines without B4GALNT3 | 0.038 | ⚠ within organs, on part of the lines; also absent: MCF2L, EPHA1, PLEKHG6 |
| [[B3GNT3]] | B | B4GALNT3 activity raises B3GNT3's level | lines that do not express B4GALNT3 (16) vs lines expressing it (34) | 3.17× lower at baseline in the lines without B4GALNT3 | 0.040 | ⚠ within organs, on part of the lines; also absent: MCF2L, EPHA1, PLEKHG6 |
| [[ARHGAP27]] | B | B4GALNT3 activity raises ARHGAP27's level | lines that do not express B4GALNT3 (16) vs lines expressing it (34) | 1.84× lower at baseline in the lines without B4GALNT3 | 0.043 | ⚠ within organs, on part of the lines; also absent: MCF2L, EPHA1, PLEKHG6 |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.643). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.1, 54.4); signed map (0.4, 38.4). **Vector** length 93.7, 24.6% of its response variance represented; |z| ≥ 3 in 863 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.4 | +10.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.0 | +6.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +7.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.1 | +6.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | +2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +4.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.6 | +3.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +3.8 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.1 | +2.8 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.7 | -4.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.0 | -3.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.9 | -5.4 |
|  | [[Trametinib (drug)]] 5 µM |  | -2.8 | -3.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.7 | -3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.6 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | beta-1,4-N-acetyl-galactosaminyltransferase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.33 — chr12:459,939-563,509 (+) |
| Ensembl biotype | protein_coding |
| Also known as | B4GalNac-T3, FLJ16224, FLJ40362 |
| Gene groups (HGNC) | Beta 4-glycosyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6L9W6](https://www.uniprot.org/uniprotkb/Q6L9W6) (Beta-1,4-N-acetylgalactosaminyltransferase 3):

> Transfers N-acetylgalactosamine (GalNAc) from UDP-GalNAc to N-acetylglucosamine-beta-benzyl with a beta-1,4-linkage to form N,N'-diacetyllactosediamine, GalNAc-beta-1,4-GlcNAc structures in N-linked glycans and probably O-linked glycans. Mediates the N,N'-diacetyllactosediamine formation on gastric mucosa.

**Summary**, from NCBI Gene [283358](https://www.ncbi.nlm.nih.gov/gene/283358):

> B4GALNT3 transfers N-acetylgalactosamine (GalNAc) onto glucosyl residues to form N,N-prime-diacetyllactosediamine (LacdiNAc, or LDN), a unique terminal structure of cell surface N-glycans (Ikehara et al., 2006 [PubMed 16728562]).[supplied by OMIM, Aug 2008]

**Accessions** — [HGNC:24137](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24137) · Entrez [283358](https://www.ncbi.nlm.nih.gov/gene/283358) · UniProt [Q6L9W6](https://www.uniprot.org/uniprotkb/Q6L9W6) · Ensembl [ENSG00000139044](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139044)

## Data

Gene col 6256: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6256); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6256, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6256]; `tensor/DDL_lfc|DDL_z.npy` [6256]; `embed/gene_vectors.npy` [6256]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6256 or target_col == 6256). Every well: [[B4GALNT3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/B4GALNT3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
