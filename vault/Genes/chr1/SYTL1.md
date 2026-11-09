---
symbol: "SYTL1"
type: "gene"
col: 6654
ensembl_id: "ENSG00000142765"
name: "synaptotagmin like 1"
location: "1p36.11"
module: 8
arm: "+"
pooled_cpm: 5.19
n_lines_expressing: 35
n_dd_up: 18
n_dd_down: 9
n_dd_up_clean: 10
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 18
direction_downstream: 17
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# SYTL1

*synaptotagmin like 1* — 1p36.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.49× (z +9.1, q 5e-17, up in 4 of 16 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 1.87× (z +4.5, q 0.001, up in 8 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.513× (z -6.7, q 1e-08, down in 20 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TCEA3]] (+0.65, fdr 7e-06), [[ERICH2]] (+0.63, fdr 1e-05), [[ADM2]] (+0.61, fdr 1e-05); moves opposite to [[PBX3]] (-0.46, fdr 1e-04), [[DOCK1]] (-0.45, fdr 5e-05), [[NUDCD1]] (-0.44, fdr 3e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 18 arrows point to it, the strongest [[ATP2C2]] → it (grade B ⚠); 17 go from it, the strongest it → [[MKNK2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6654.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.49×** | +9.1 | 5e-17 | 4/16 (HEC-1-A, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.21×** | +7.6 | 9e-12 | 2/10 (NCI-H2347, HEC-1-A) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.85×** | +5.7 | 3e-06 | 1/13 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.87×** | +4.5 | 0.001 | 8/22 (SW480, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +4.4 | 0.001 | 3/23 (LoVo, BT-474, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.52×** | +4.2 | 0.003 | 17/30 (SW480, HCT15, …) | all doses, stronger at high dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.05×** | +3.7 | 0.015 | 0/6 | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.44×** | +3.7 | 0.018 | 7/28 (SW480, HCT15, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | **1.28×** | +3.4 | 0.033 | 5/29 (SW480, KATO III, …) | rises with dose |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.94×** | +3.4 | 0.033 | 2/10 (KATO III, NCI-H1573) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.41×** | +3.4 | 0.033 | 6/18 (NCI-H2347, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.39×** | +3.3 | 0.049 | 5/23 (HOP62, NCI-H1573, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.38×** | +3.2 | 0.067 | 4/27 (MIA PaCa-2, KATO III, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[PH-797804 (drug)]] 0.5 µM |  | **1.55×** | +3.1 | 0.070 | 6/26 (SHP-77, CFPAC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +3.1 | 0.073 | 2/18 (SW48, LS 180) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.25×** | +3.1 | 0.073 | 5/31 (SW480, SHP-77, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.36×** | +3.0 | 0.081 | 6/27 (SW480, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~15% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6654.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.513×** | -6.7 | 1e-08 | 20/28 (SW480, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.561×** | -5.8 | 2e-06 | 15/25 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.611×** | -5.0 | 1e-04 | 17/32 (SW1417, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.621×** | -4.6 | 6e-04 | 13/27 (HCT15, PANC-1, …) | rises with dose | composition shift; position effect removed |
| [[Selinexor (drug)]] 0.5 µM |  | **0.688×** | -3.8 | 0.019 | 9/27 (SW480, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.702×** | -3.6 | 0.035 | 6/29 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.711×** | -3.4 | 0.047 | 11/29 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Malotilate (drug)]] 0.5 µM |  | **0.716×** | -3.4 | 0.053 | 6/27 (NCI-H23, HT-29, …) | two highest doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.727×** | -3.2 | 0.084 | 12/26 (PANC-1, SW480, …) | all doses, stronger at high dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6654. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 9.38 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0636× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.187× (z -9.5) |
| [[HT-29 (line)]] | alt | 9.45 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.118× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[COLO 205 (line)]] | alt | 8.65 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.113× (z -11.4) |
| [[HCT15 (line)]] | alt | 26.8 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0470× (z -13.0) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 13.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.249× (z -8.6) |
| [[KATO III (line)]] | alt | 8.24 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0903× (z -9.8) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 5.39 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0881× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 2.60 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0436× (z -12.7) ⚠ cell-cycle shift, explains ~24% of this change |
| [[SW1417 (line)]] | alt | 2.74 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0474× (z -9.1) |
| [[SW48 (line)]] | wt | 30.1 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.143× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 1.23 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 3.53 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.903 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.888 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.31 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.69 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.23 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.38 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 34.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.948 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.42 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.908 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.33 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.08 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.53 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6654), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCEA3]] | +0.65 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[ERICH2]] | +0.63 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[ADM2]] | +0.61 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[TMEM125]] | +0.61 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[ESRP1]] | +0.59 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[GARS1]] | +0.56 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[ADCY4]] | +0.56 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[EPS8L2]] | +0.56 | +0.59 / +0.46 | both halves | 3e-05 | STRING 437 |
| [[CLGN]] | +0.55 | +0.40 / +0.51 | both halves | 5e-05 |  |
| [[ASS1]] | +0.54 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[HID1]] | +0.54 | +0.46 / +0.56 | both halves | 2e-05 |  |
| [[ULBP1]] | +0.54 | +0.42 / +0.49 | both halves | 4e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PBX3]] | -0.46 | -0.35 / -0.41 | both halves | 1e-04 |  |
| [[DOCK1]] | -0.45 | -0.39 / -0.45 | both halves | 5e-05 |  |
| [[NUDCD1]] | -0.44 | -0.43 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 16, C 2. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATP2C2]] | B | ATP2C2 activity raises SYTL1's level | lines that do not express ATP2C2 (32) vs lines expressing it (18) | 3.19× lower at baseline in the lines without ATP2C2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, GRHL2, ST14 |
| [[TMEM125]] | B | TMEM125 activity raises SYTL1's level | lines that do not express TMEM125 (33) vs lines expressing it (17) | 3.36× lower at baseline in the lines without TMEM125 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ATP2C2, ST14 |
| [[FUT3]] | B | FUT3 activity raises SYTL1's level | lines that do not express FUT3 (29) vs lines expressing it (21) | 2.49× lower at baseline in the lines without FUT3 | 0.002 | ⚠ within organs, on part of the lines; also absent: ATP2C2, TMEM125, ENSG00000243004 |
| [[ESRP1]] | B | ESRP1 activity raises SYTL1's level | lines that do not express ESRP1 (31) vs lines expressing it (19) | 3.13× lower at baseline in the lines without ESRP1 | 0.004 | ⚠ within organs, on part of the lines; also absent: ST14, KDF1, CLDN7 |
| [[RORC]] | B | RORC activity raises SYTL1's level | lines that do not express RORC (30) vs lines expressing it (20) | 2.52× lower at baseline in the lines without RORC | 0.005 | ⚠ within organs, on part of the lines; also absent: LRG1, LINC03040, ATP2C2 |
| [[CDC42BPG]] | B | CDC42BPG activity raises SYTL1's level | lines that do not express CDC42BPG (19) vs lines expressing it (31) | 2.47× lower at baseline in the lines without CDC42BPG | 0.015 | ⚠ within organs, on part of the lines; also absent: SPINT2, ENSG00000267748, PLEKHG6; maybe low, not absent |
| [[ADGRG1]] | B | ADGRG1 activity raises SYTL1's level | lines that do not express ADGRG1 (12) vs lines expressing it (38) | 2.00× lower at baseline in the lines without ADGRG1 | 0.023 | ⚠ within organs, on part of the lines; also absent: LGALS3, PDGFB, ENSG00000249526 |
| [[EPS8L2]] | B | EPS8L2 activity raises SYTL1's level | lines that do not express EPS8L2 (19) vs lines expressing it (31) | 2.38× lower at baseline in the lines without EPS8L2 | 0.024 | ⚠ within organs, on part of the lines; also absent: KRT80, ITGB4, C19orf33; maybe low, not absent |
| [[ARHGEF16]] | B | ARHGEF16 activity raises SYTL1's level | lines that do not express ARHGEF16 (14) vs lines expressing it (36) | 2.37× lower at baseline in the lines without ARHGEF16 | 0.059 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A-DT, KRT18, NRARP |
| [[TMC4]] | B | TMC4 activity raises SYTL1's level | lines that do not express TMC4 (26) vs lines expressing it (24) | 2.37× lower at baseline in the lines without TMC4 | 0.062 | ⚠ within organs, on part of the lines; also absent: CBLC, TNNT2, CRB3; maybe low, not absent |
| [[LINC03040]] | B | LINC03040 activity raises SYTL1's level | lines that do not express LINC03040 (31) vs lines expressing it (19) | 2.45× lower at baseline in the lines without LINC03040 | 0.068 | ⚠ within organs, on part of the lines; also absent: SLC44A4, EPS8L3, LCN2 |
| [[IL17RE]] | B | IL17RE activity raises SYTL1's level | lines that do not express IL17RE (10) vs lines expressing it (40) | 2.13× lower at baseline in the lines without IL17RE | 0.083 | ⚠ within organs, on part of the lines; also absent: MCF2L; maybe low, not absent |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 15, C 2. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MKNK2]] | B | SYTL1 activity raises MKNK2's level | lines that do not express SYTL1 (15) vs lines expressing it (35) | 1.54× lower at baseline in the lines without SYTL1 | 0.006 | ⚠ within organs, on part of the lines; also absent: ATAD3C, PLEKHG6, SORL1; maybe low, not absent |
| [[ZFAND1]] | B | SYTL1 activity raises ZFAND1's level | lines that do not express SYTL1 (15) vs lines expressing it (35) | 1.56× lower at baseline in the lines without SYTL1 | 0.023 | ⚠ within organs, on part of the lines; also absent: ATAD3C, PLEKHG6, SORL1; maybe low, not absent |
| [[CDC42BPG]] | B | SYTL1 activity raises CDC42BPG's level | lines that do not express SYTL1 (15) vs lines expressing it (35) | 2.93× lower at baseline in the lines without SYTL1 | 0.025 | ⚠ within organs, on part of the lines; also absent: ATAD3C, PLEKHG6, SORL1; maybe low, not absent |
| [[ESRP1]] | B | SYTL1 activity raises ESRP1's level | lines that do not express SYTL1 (15) vs lines expressing it (35) | 6.10× lower at baseline in the lines without SYTL1 | 0.043 | ⚠ within organs, on part of the lines; also absent: ATAD3C, PLEKHG6, SORL1; maybe low, not absent |
| [[TMC4]] | B | SYTL1 activity raises TMC4's level | lines that do not express SYTL1 (15) vs lines expressing it (35) | 3.23× lower at baseline in the lines without SYTL1 | 0.048 | ⚠ within organs, on part of the lines; also absent: ATAD3C, PLEKHG6, SORL1; maybe low, not absent |
| [[TMEM184A]] | B | SYTL1 activity raises TMEM184A's level | lines that do not express SYTL1 (15) vs lines expressing it (35) | 2.07× lower at baseline in the lines without SYTL1 | 0.052 | ⚠ within organs, on part of the lines; also absent: ATAD3C, PLEKHG6, SORL1; maybe low, not absent |
| [[ARHGEF16]] | B | SYTL1 activity raises ARHGEF16's level | lines that do not express SYTL1 (15) vs lines expressing it (35) | 2.54× lower at baseline in the lines without SYTL1 | 0.052 | ⚠ within organs, on part of the lines; also absent: ATAD3C, PLEKHG6, SORL1; maybe low, not absent |
| [[RAP1GAP]] | B | SYTL1 activity raises RAP1GAP's level | lines that do not express SYTL1 (15) vs lines expressing it (35) | 1.73× lower at baseline in the lines without SYTL1 | 0.057 | ⚠ within organs, on part of the lines; also absent: ATAD3C, PLEKHG6, SORL1; maybe low, not absent |
| [[MLXIPL]] | B | SYTL1 activity raises MLXIPL's level | lines that do not express SYTL1 (15) vs lines expressing it (35) | 2.64× lower at baseline in the lines without SYTL1 | 0.059 | ⚠ within organs, on part of the lines; also absent: ATAD3C, PLEKHG6, SORL1; maybe low, not absent |
| [[GOLGA4]] | B | SYTL1 activity lowers GOLGA4's level | lines that do not express SYTL1 (15) vs lines expressing it (35) | 1.24× higher at baseline in the lines without SYTL1 | 0.069 | ⚠ within organs, on part of the lines; also absent: ATAD3C, PLEKHG6, SORL1; maybe low, not absent |
| [[HID1]] | B | SYTL1 activity raises HID1's level | lines that do not express SYTL1 (15) vs lines expressing it (35) | 2.68× lower at baseline in the lines without SYTL1 | 0.079 | ⚠ within organs, on part of the lines; also absent: ATAD3C, PLEKHG6, SORL1; maybe low, not absent |
| [[DEF6]] | B | SYTL1 activity raises DEF6's level | lines that do not express SYTL1 (15) vs lines expressing it (35) | 2.07× lower at baseline in the lines without SYTL1 | 0.082 | ⚠ within organs, on part of the lines; also absent: ATAD3C, PLEKHG6, SORL1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.375). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-15.3, 49.4); signed map (-11.0, 23.3). **Vector** length 56.4, 11.7% of its response variance represented; |z| ≥ 3 in 609 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +7.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.9 | +9.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +5.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.1 | +4.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +2.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +4.5 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.2 | +3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +1.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.0 | -6.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.9 | -5.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | -1.8 | -3.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.6 | -3.6 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.5 | -2.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.4 | -1.7 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.3 | -1.7 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.3 | -2.3 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.3 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | synaptotagmin like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.11 — chr1:27,342,020-27,353,937 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SLP1, JFC1, FLJ14996, exophilin-7 |
| Gene groups (HGNC) | Synaptotagmin like tandem C2 proteins |
| Reactome | 4 pathways, smallest: TBC/RABGAPs; Rab regulation of trafficking; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IYJ3](https://www.uniprot.org/uniprotkb/Q8IYJ3) (Synaptotagmin-like protein 1):

> May play a role in vesicle trafficking (By similarity). Binds phosphatidylinositol 3,4,5-trisphosphate. Acts as a RAB27A effector protein and may play a role in cytotoxic granule exocytosis in lymphocytes (By similarity).

**Summary**, from NCBI Gene [84958](https://www.ncbi.nlm.nih.gov/gene/84958):

> Predicted to enable neurexin family protein binding activity. Involved in exocytosis. Located in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:15584](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15584) · Entrez [84958](https://www.ncbi.nlm.nih.gov/gene/84958) · UniProt [Q8IYJ3](https://www.uniprot.org/uniprotkb/Q8IYJ3) · Ensembl [ENSG00000142765](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142765)

## Data

Gene col 6654: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6654); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6654, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6654]; `tensor/DDL_lfc|DDL_z.npy` [6654]; `embed/gene_vectors.npy` [6654]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6654 or target_col == 6654). Every well: [[SYTL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SYTL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
