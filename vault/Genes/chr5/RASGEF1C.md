---
symbol: "RASGEF1C"
type: "gene"
col: 7063
ensembl_id: "ENSG00000146090"
name: "RasGEF domain family member 1C"
location: "5q35.3"
module: 102
arm: "+"
pooled_cpm: 6.59
n_lines_expressing: 36
n_dd_up: 27
n_dd_down: 8
n_dd_up_clean: 20
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 28
direction_downstream: 15
tags: ["gene", "module/102"]
generated_by: "tahoemap"
---

# RASGEF1C

*RasGEF domain family member 1C* — 5q35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (7 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.84× (z +20.5, q 0e+00, up in 31 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.639× (z -6.2, q 3e-07, down in 20 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SYN2]] (+0.67, fdr 7e-06), [[KCNQ2]] (+0.63, fdr 1e-05), [[BRSK2]] (+0.63, fdr 1e-05); moves opposite to [[GALK2]] (-0.51, fdr 4e-05), [[TRMT1L]] (-0.49, fdr 5e-05), [[ANKRD42]] (-0.48, fdr 3e-05).
> It is in [[Module 102]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 28 arrows point to it, the strongest [[MSI1]] → it (grade B ⚠); 15 go from it, the strongest it → [[SNX10]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7063.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.84×** | +20.5 | 0e+00 | 31/33 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **3.10×** | +15.7 | 0e+00 | 21/33 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.72×** | +13.9 | 1e-41 | 17/32 (NCI-H460, NCI-H2347, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.53×** | +12.9 | 6e-36 | 21/33 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.39×** | +12.1 | 1e-31 | 24/31 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.31×** | +10.5 | 5e-24 | 10/22 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.09×** | +10.2 | 1e-22 | 15/33 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.92×** | +9.1 | 1e-17 | 16/33 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.87×** | +7.9 | 2e-13 | 3/10 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +6.5 | 4e-09 | 9/30 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.58×** | +6.4 | 9e-09 | 17/33 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.56×** | +6.2 | 3e-08 | 5/22 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.03×** | +5.1 | 1e-05 | 6/17 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.25×** | +4.4 | 4e-04 | 5/32 (NCI-H460, C32, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.39×** | +4.2 | 1e-03 | 7/26 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.75×** | +4.1 | 0.001 | 3/26 (C32, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.33×** | +3.9 | 0.002 | 5/30 (NCI-H460, NCI-H1792, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.47×** | +3.8 | 0.004 | 5/30 (NCI-H460, NCI-H1573, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.31×** | +3.7 | 0.006 | 3/33 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7063.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.639×** | -6.2 | 3e-07 | 20/33 (LoVo, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~17% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.442×** | -5.9 | 8e-07 | 16/31 (A-427, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.792×** | -4.6 | 8e-04 | 13/33 (C32, SK-MEL-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.557×** | -4.3 | 0.003 | 11/27 (SK-MEL-2, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.752×** | -4.0 | 0.009 | 12/32 (A-427, C32, …) | two highest doses | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.762×** | -3.4 | 0.052 | 17/29 (SK-MEL-2, SNU-1, …) | two highest doses | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change | **0.782×** | -3.4 | 0.052 | 16/30 (LoVo, SNU-1, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.790×** | -3.3 | 0.075 | 5/32 (NCI-H2030, C32, …) | top dose only |  |
| [[Clopidogrel (drug)]] 0.05 µM |  | 0.797× | -3.2 | 0.10 | 4/33 (NCI-H1792, A498, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | 0.787× | -3.0 | 0.14 | 13/25 (LoVo, C32, …) | top dose only | cell-cycle shift (explains ~11% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7063. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 32.7 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -15.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.134× (z -15.2) |
| [[C32 (line)]] | wt | 26.7 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0770× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.284× (z -9.6) |
| [[SK-MEL-2 (line)]] | alt | 28.2 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -12.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[c-Kit-IN-1 (drug)]] 5 µM 0.0392× (z -10.2) |
| [[LoVo (line)]] | wt | 18.6 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.170× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.268× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 10.8 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.138× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change · without an alert: [[Elimusertib hydrochloride (drug)]] 0.05 µM 0.156× (z -8.8) |
| [[SNU-1 (line)]] | wt | 17.2 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.104× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change |
| [[A-172 (line)]] | wt | 3.54 | 0 | 1 (1 ⚠) | — | [[Pentoxifylline (drug)]] 0.05 µM 0.0759× (z -8.5) ⚠ transcription drop |
| [[C-33 A (line)]] | alt | 33.9 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0307× (z -10.5) |
| [[HEC-1-A (line)]] | alt | 11.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.32× (z +8.7) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 2.96 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.506× (z -8.6) ⚠ position not correctable |
| [[PANC-1 (line)]] | alt | 3.94 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.61× (z +8.8) | — |
| [[A498 (line)]] | wt | 2.76 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.53 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.56 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.27 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.987 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.39 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.916 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.999 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.829 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.40 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 4.41 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7063), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SYN2]] | +0.67 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[KCNQ2]] | +0.63 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[BRSK2]] | +0.63 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[DGCR5]] | +0.62 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[CAMK2B]] | +0.62 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[NKAIN1]] | +0.62 | +0.54 / +0.69 | both halves | 1e-05 |  |
| [[CACNA1H]] | +0.62 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[SHANK3]] | +0.61 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[KIF26A]] | +0.61 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[ST6GAL1]] | +0.60 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[GRID1]] | +0.60 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[JAKMIP1]] | +0.59 | +0.48 / +0.67 | both halves | 2e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GALK2]] | -0.51 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[TRMT1L]] | -0.49 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[ANKRD42]] | -0.48 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[TBCK]] | -0.48 | -0.37 / -0.49 | both halves | 9e-05 |  |
| [[COPS5]] | -0.47 | -0.37 / -0.50 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*28 arrows, 28 of them with an alert ⚠; grade A 0, B 20, C 8. Shown: the 12 strongest; 16 more arrows (16 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MSI1]] | B | MSI1 activity raises RASGEF1C's level | lines that do not express MSI1 (26) vs lines expressing it (24) | 2.18× lower at baseline in the lines without MSI1 | 0.002 | ⚠ within organs, on part of the lines; also absent: KCNQ2, KIF1A, LMX1B |
| [[MED12L]] | B | MED12L activity raises RASGEF1C's level | lines that do not express MED12L (18) vs lines expressing it (32) | 2.20× lower at baseline in the lines without MED12L | 0.013 | ⚠ within organs, on part of the lines; also absent: SYNGR1, NPTX1, AP3B2 |
| [[PDZD4]] | B | PDZD4 activity raises RASGEF1C's level | lines that do not express PDZD4 (22) vs lines expressing it (28) | 2.18× lower at baseline in the lines without PDZD4 | 0.013 | ⚠ within organs, on part of the lines; also absent: CECR2, CPEB1, COLEC12 |
| [[CHD5]] | B | CHD5 activity raises RASGEF1C's level | lines that do not express CHD5 (30) vs lines expressing it (20) | 1.88× lower at baseline in the lines without CHD5 | 0.018 | ⚠ within organs, on part of the lines; also absent: DPYSL5, RET, KIF1A; maybe low, not absent |
| [[RET]] | B | RET activity raises RASGEF1C's level | lines that do not express RET (28) vs lines expressing it (22) | 1.94× lower at baseline in the lines without RET | 0.019 | ⚠ within organs, on part of the lines; also absent: CHD5, KIF1A, NPTX1 |
| [[LHX2]] | B | LHX2 activity raises RASGEF1C's level | lines that do not express LHX2 (26) vs lines expressing it (24) | 2.51× lower at baseline in the lines without LHX2 | 0.020 | ⚠ within organs, on part of the lines; also absent: CECR2, COL4A4, GHR |
| [[SNX10]] | B | SNX10 activity raises RASGEF1C's level | lines that do not express SNX10 (11) vs lines expressing it (39) | 2.43× lower at baseline in the lines without SNX10 | 0.020 | ⚠ within organs, on part of the lines; also absent: AP3B2, LRRC4B, CCDC144CP |
| [[ST6GAL1]] | B | ST6GAL1 activity raises RASGEF1C's level | lines that do not express ST6GAL1 (14) vs lines expressing it (36) | 1.98× lower at baseline in the lines without ST6GAL1 | 0.025 | ⚠ within organs, on part of the lines; also absent: B4GALNT4, MYT1, ENSG00000290588; maybe low, not absent |
| [[ZNF536]] | B | ZNF536 activity raises RASGEF1C's level | lines that do not express ZNF536 (24) vs lines expressing it (26) | 2.14× lower at baseline in the lines without ZNF536 | 0.025 | ⚠ within organs, on part of the lines; also absent: PDZD4, NPTX1, RET; maybe low, not absent |
| [[MSRB3-AS1]] | B | MSRB3-AS1 activity weakens RASGEF1C's drug response | lines that do not express MSRB3-AS1 (28) vs lines expressing it (5) | (z diff -2.29); strongest at Idarubicin (hydrochloride) 5 µM: 1.14x vs 0.46x (z diff -5.5) | 0.029 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GCG, LINC01205, COX7B2; target measured in part of the lines; artifact flags |
| [[ADCY1]] | B | ADCY1 activity raises RASGEF1C's level | lines that do not express ADCY1 (24) vs lines expressing it (26) | 2.54× lower at baseline in the lines without ADCY1 | 0.038 | ⚠ within organs, on part of the lines; also absent: LHX2, GAS7, GHR |
| [[SEMA6B]] | B | SEMA6B activity raises RASGEF1C's level | lines that do not express SEMA6B (14) vs lines expressing it (36) | 2.29× lower at baseline in the lines without SEMA6B | 0.043 | ⚠ within organs, on part of the lines; also absent: FAM78B, BOLA3-DT, SLC4A3; maybe low, not absent |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 10, C 5. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SNX10]] | B | RASGEF1C activity raises SNX10's level | lines that do not express RASGEF1C (14) vs lines expressing it (36) | 2.96× lower at baseline in the lines without RASGEF1C | 0.012 | ⚠ within organs, on part of the lines; also absent: FAM124A, RAB6B, STOX2; maybe low, not absent |
| [[C2orf72]] | B | RASGEF1C activity raises C2orf72's level | lines that do not express RASGEF1C (14) vs lines expressing it (36) | 1.77× lower at baseline in the lines without RASGEF1C | 0.015 | ⚠ within organs, on part of the lines; also absent: FAM124A, RAB6B, STOX2; maybe low, not absent |
| [[MSI1]] | B | RASGEF1C activity raises MSI1's level | lines that do not express RASGEF1C (14) vs lines expressing it (36) | 2.13× lower at baseline in the lines without RASGEF1C | 0.023 | ⚠ within organs, on part of the lines; also absent: FAM124A, RAB6B, STOX2; maybe low, not absent |
| [[GBX1]] | B | RASGEF1C activity raises GBX1's level | lines that do not express RASGEF1C (14) vs lines expressing it (36) | 2.03× lower at baseline in the lines without RASGEF1C | 0.041 | ⚠ within organs, on part of the lines; also absent: FAM124A, RAB6B, STOX2; maybe low, not absent |
| [[ULK2]] | B | RASGEF1C activity raises ULK2's level | lines that do not express RASGEF1C (14) vs lines expressing it (36) | 3.14× lower at baseline in the lines without RASGEF1C | 0.055 | ⚠ within organs, on part of the lines; also absent: FAM124A, RAB6B, STOX2; maybe low, not absent |
| [[RHBDL3]] | B | RASGEF1C activity raises RHBDL3's level | lines that do not express RASGEF1C (14) vs lines expressing it (36) | 2.02× lower at baseline in the lines without RASGEF1C | 0.071 | ⚠ within organs, on part of the lines; also absent: FAM124A, RAB6B, STOX2; maybe low, not absent |
| [[ST6GAL1]] | B | RASGEF1C activity raises ST6GAL1's level | lines that do not express RASGEF1C (14) vs lines expressing it (36) | 2.52× lower at baseline in the lines without RASGEF1C | 0.081 | ⚠ within organs, on part of the lines; also absent: FAM124A, RAB6B, STOX2; maybe low, not absent |
| [[KIF26A]] | B | RASGEF1C activity raises KIF26A's level | lines that do not express RASGEF1C (14) vs lines expressing it (36) | 1.72× lower at baseline in the lines without RASGEF1C | 0.089 | ⚠ within organs, on part of the lines; also absent: FAM124A, RAB6B, STOX2; maybe low, not absent |
| [[OLFM2]] | B | RASGEF1C activity raises OLFM2's level | lines that do not express RASGEF1C (14) vs lines expressing it (36) | 3.18× lower at baseline in the lines without RASGEF1C | 0.089 | ⚠ within organs, on part of the lines; also absent: FAM124A, RAB6B, STOX2; maybe low, not absent |
| [[WIPF3]] | B | RASGEF1C activity raises WIPF3's level | lines that do not express RASGEF1C (14) vs lines expressing it (36) | 1.46× lower at baseline in the lines without RASGEF1C | 0.099 | ⚠ within organs, on part of the lines; also absent: FAM124A, RAB6B, STOX2; maybe low, not absent |
| [[STOX2]] | C | RASGEF1C activity raises STOX2's level | lines that do not express RASGEF1C (14) vs lines expressing it (36) | 4.50× lower at baseline in the lines without RASGEF1C | 0.003 | ⚠ within organs, on part of the lines; also absent: FAM124A, RAB6B, STOX2; maybe low, not absent; co-absent with the target |
| [[TCF7L1]] | C | RASGEF1C activity raises TCF7L1's level | lines that do not express RASGEF1C (14) vs lines expressing it (36) | 3.81× lower at baseline in the lines without RASGEF1C | 0.027 | ⚠ within organs, on part of the lines; also absent: FAM124A, RAB6B, STOX2; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 102]] — Neuronal System; 45 genes; every member is in the + arm (projection on the module's main direction 0.741). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (6.6, 38.6); signed map (27.1, 25.7). **Vector** length 75.9, 15.9% of its response variance represented; |z| ≥ 3 in 906 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.4 | +20.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.0 | +12.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.9 | +7.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.5 | +6.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.1 | +13.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.7 | +3.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.7 | +4.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.5 | +3.7 |
| fall | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -2.4 | -4.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -1.1 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.9 | -2.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.8 | -0.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | -1.8 | -5.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.7 | -3.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.5 | -2.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.4 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | RasGEF domain family member 1C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.3 — chr5:180,100,795-180,209,211 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ35841 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N431](https://www.uniprot.org/uniprotkb/Q8N431) (Ras-GEF domain-containing family member 1C):

> Guanine nucleotide exchange factor (GEF).

**Summary**, from NCBI Gene [255426](https://www.ncbi.nlm.nih.gov/gene/255426):

> Predicted to enable guanyl-nucleotide exchange factor activity. Predicted to be involved in Ras protein signal transduction. Predicted to be active in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:27400](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27400) · Entrez [255426](https://www.ncbi.nlm.nih.gov/gene/255426) · UniProt [Q8N431](https://www.uniprot.org/uniprotkb/Q8N431) · Ensembl [ENSG00000146090](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146090)

## Data

Gene col 7063: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7063); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7063, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7063]; `tensor/DDL_lfc|DDL_z.npy` [7063]; `embed/gene_vectors.npy` [7063]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7063 or target_col == 7063). Every well: [[RASGEF1C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RASGEF1C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
