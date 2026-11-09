---
symbol: "ATP2A3"
type: "gene"
col: 1078
ensembl_id: "ENSG00000074370"
name: "ATPase sarcoplasmic/endoplasmic reticulum Ca2+ transporting 3"
location: "17p13.2"
module: 161
arm: "+"
pooled_cpm: 4.01
n_lines_expressing: 34
n_dd_up: 12
n_dd_down: 18
n_dd_up_clean: 8
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 5
direction_downstream: 5
tags: ["gene", "module/161"]
generated_by: "tahoemap"
---

# ATP2A3

*ATPase sarcoplasmic/endoplasmic reticulum Ca2+ transporting 3* — 17p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.57× (z +14.2, q 6e-43, up in 26 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.443× (z -9.1, q 8e-17, down in 22 of 31 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NXPH4]] (+0.63, fdr 5e-05), [[SCUBE1]] (+0.61, fdr 4e-05), [[SHF]] (+0.60, fdr 9e-05); moves opposite to [[TBCK]] (-0.58, fdr 2e-05), [[AFG1L]] (-0.56, fdr 4e-05), [[MCPH1]] (-0.56, fdr 4e-04).
> It is in [[Module 161]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[VIPR2]] → it (grade B ⚠); 5 go from it, the strongest it → [[GYG2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1078.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.57×** | +14.2 | 6e-43 | 26/31 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.40×** | +13.8 | 4e-41 | 24/29 (SW480, LS 180, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.99×** | +12.2 | 5e-32 | 25/31 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.80×** | +11.5 | 2e-28 | 22/31 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.45×** | +9.6 | 6e-20 | 4/6 (BT-474, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.14×** | +8.5 | 2e-15 | 14/26 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.04×** | +7.4 | 1e-11 | 1/9 (BT-474) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.90×** | +7.2 | 6e-11 | 20/31 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.80×** | +6.6 | 3e-09 | 5/16 (SHP-77, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.45×** | +4.2 | 0.002 | 6/23 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.55×** | +3.5 | 0.026 | 1/16 (NCI-H2030) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.52×** | +3.4 | 0.037 | 3/19 (SW480, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1078.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.443×** | -9.1 | 8e-17 | 22/31 (NCI-H460, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.504×** | -7.3 | 6e-11 | 18/29 (NCI-H460, HT-29, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.518×** | -7.3 | 6e-11 | 16/30 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.523×** | -7.2 | 9e-11 | 16/24 (HT-29, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.558×** | -6.5 | 1e-08 | 20/30 (NCI-H2030, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~20% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.615×** | -5.4 | 6e-06 | 17/31 (A498, HT-29, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.662×** | -4.6 | 4e-04 | 10/31 (NCI-H460, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.667×** | -4.5 | 5e-04 | 10/27 (SW480, HT-29, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.668×** | -4.5 | 5e-04 | 16/22 (HT-29, NCI-H460, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.671×** | -4.4 | 5e-04 | 14/28 (HT-29, SW480, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.675×** | -4.4 | 7e-04 | 6/29 (PANC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~24% here) |
| [[EX229 (drug)]] 0.05 µM |  | **0.663×** | -4.3 | 8e-04 | 7/26 (A549, RPMI-7951, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.726×** | -3.5 | 0.017 | 9/28 (NCI-H460, A-172, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.732×** | -3.5 | 0.022 | 7/29 (NCI-H1792, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.554×** | -3.4 | 0.023 | 7/28 (NCI-H1792, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Pyridoxine (drug)]] 0.05 µM |  | **0.745×** | -3.2 | 0.041 | 5/29 (SHP-77, AN3 CA, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.669×** | -3.2 | 0.048 | 5/31 (HT-29, A498, …) | two highest doses | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.591×** | -3.0 | 0.072 | 6/23 (HT-29, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1078. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 22.0 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.190× (z -12.1) ⚠ cell-cycle shift, explains <1% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.139× (z -10.1) |
| [[COLO 205 (line)]] | alt | 12.3 | 0 | 3 (1 ⚠) | — | [[Oxaprozin (drug)]] 0.5 µM 0.0751× (z -10.6) |
| [[A-172 (line)]] | wt | 3.29 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0612× (z -8.9) |
| [[NCI-H460 (line)]] | wt | 5.07 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.130× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.05 µM 0.136× (z -9.1) |
| [[PANC-1 (line)]] | alt | 2.77 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 10.0× (z +9.4) | — |
| [[SW480 (line)]] | alt | 3.36 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 4.41× (z +9.7) | — |
| [[A498 (line)]] | wt | 3.76 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0325× (z -14.0) ⚠ unreliable plate only |
| [[AsPC-1 (line)]] | alt | 5.64 | 0 | 1 | — | [[Penfluridol (drug)]] 5 µM 0.0719× (z -9.1) |
| [[NCI-H1792 (line)]] | alt | 11.9 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.176× (z -10.6) ⚠ cell-cycle shift, explains <1% of this change |
| [[A-427 (line)]] | wt | 9.16 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.77 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.977 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.458 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.970 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.612 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.950 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.812 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.767 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.588 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.752 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.659 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.58 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.720 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.81 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.424 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.502 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.593 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.744 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.739 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1078), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NXPH4]] | +0.63 | +0.39 / +0.55 | both halves | 5e-05 |  |
| [[SCUBE1]] | +0.61 | +0.60 / +0.41 | both halves | 4e-05 |  |
| [[SHF]] | +0.60 | +0.36 / +0.61 | both halves | 9e-05 |  |
| [[SEMA3F]] | +0.60 | +0.37 / +0.55 | both halves | 8e-05 |  |
| [[FCHO1]] | +0.60 | +0.29 / +0.54 | both halves | 2e-04 |  |
| [[RADIL]] | +0.59 | +0.41 / +0.46 | both halves | 4e-05 |  |
| [[LMTK3]] | +0.59 | +0.39 / +0.47 | both halves | 5e-05 |  |
| [[ASAP3]] | +0.58 | +0.35 / +0.62 | both halves | 1e-04 |  |
| [[RIMS3]] | +0.58 | +0.38 / +0.43 | both halves | 7e-05 |  |
| [[BAIAP3]] | +0.58 | +0.45 / +0.44 | both halves | 3e-05 |  |
| [[ANO8]] | +0.58 | +0.45 / +0.43 | both halves | 3e-05 | pathway: Ion channel transport |
| [[CADM4]] | +0.57 | +0.33 / +0.46 | both halves | 1e-04 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBCK]] | -0.58 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[AFG1L]] | -0.56 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[MCPH1]] | -0.56 | -0.26 / -0.43 | both halves | 4e-04 |  |
| [[EXOC4]] | -0.56 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[PRORP]] | -0.55 | -0.37 / -0.41 | both halves | 9e-05 |  |
| [[GTF2H1]] | -0.55 | -0.33 / -0.42 | both halves | 1e-04 |  |
| [[PLS3-AS1]] | -0.54 | -0.30 / -0.34 | both halves | 2e-04 |  |
| [[SLC16A1-AS1]] | -0.54 | -0.43 / -0.25 | both halves | 4e-04 |  |
| [[TRMT5]] | -0.53 | -0.35 / -0.41 | both halves | 1e-04 |  |
| [[UBE3B]] | -0.51 | -0.30 / -0.37 | both halves | 2e-04 |  |
| [[MFF-DT]] | -0.51 | -0.26 / -0.23 | both halves | 5e-04 |  |
| [[YARS2]] | -0.51 | -0.33 / -0.21 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VIPR2]] | B | VIPR2 activity raises ATP2A3's level | lines that do not express VIPR2 (32) vs lines expressing it (18) | 2.40× lower at baseline in the lines without VIPR2 | 0.083 | ⚠ within organs, on part of the lines; also absent: DPP10, KCNH5, ASXL3; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers ATP2A3's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers ATP2A3's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[MEIOB]] | B | MEIOB activity raises ATP2A3's level | lines that do not express MEIOB (28) vs lines expressing it (22) | 1.90× lower at baseline in the lines without MEIOB | 0.085 | ⚠ within organs, on part of the lines; also absent: SHISAL1, DOK6, DPP10; maybe low, not absent |
| [[ABCG1]] | B | ABCG1 activity raises ATP2A3's level | lines that do not express ABCG1 (15) vs lines expressing it (35) | 2.22× lower at baseline in the lines without ABCG1 | 0.098 | ⚠ within organs, on part of the lines; also absent: RSPH1, OLFM1, PDK4 |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GYG2]] | B | ATP2A3 activity raises GYG2's level | lines that do not express ATP2A3 (16) vs lines expressing it (34) | 1.50× lower at baseline in the lines without ATP2A3 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: WBP2NL, BEX4, NSUN7; maybe low, not absent |
| [[JAK3]] | B | ATP2A3 activity raises JAK3's level | lines that do not express ATP2A3 (16) vs lines expressing it (34) | 1.45× lower at baseline in the lines without ATP2A3 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: WBP2NL, BEX4, NSUN7; maybe low, not absent |
| [[TCEA3]] | B | ATP2A3 activity raises TCEA3's level | lines that do not express ATP2A3 (16) vs lines expressing it (34) | 1.99× lower at baseline in the lines without ATP2A3 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: WBP2NL, BEX4, NSUN7; maybe low, not absent |
| [[ZG16B]] | B | ATP2A3 activity raises ZG16B's level | lines that do not express ATP2A3 (16) vs lines expressing it (34) | 1.20× lower at baseline in the lines without ATP2A3 | 0.083 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: WBP2NL, BEX4, NSUN7; maybe low, not absent |
| [[ARAP1]] | B | ATP2A3 activity raises ARAP1's level | lines that do not express ATP2A3 (16) vs lines expressing it (34) | 1.26× lower at baseline in the lines without ATP2A3 | 0.0997 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: WBP2NL, BEX4, NSUN7; maybe low, not absent |

## Where it sits

- **Module**: [[Module 161]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.704). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (10.5, 1.5); signed map (-21.2, 28.8). **Vector** length 50.2, 8.46% of its response variance represented; |z| ≥ 3 in 802 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.2 | +9.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.8 | +13.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.7 | +6.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.0 | +7.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.6 | +8.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +2.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.6 | +2.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +3.4 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +1.4 | +0.2 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -2.7 | -7.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -2.3 | -7.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.2 | -6.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.1 | -5.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -1.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.6 | -2.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -1.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.4 | -2.3 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.3 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | ATPase sarcoplasmic/endoplasmic reticulum Ca2+ transporting 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.2 — chr17:3,923,870-3,964,464 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SERCA3 |
| Gene groups (HGNC) | ATPases Ca2+ transporting |
| Reactome | 13 pathways, smallest: Reduction of cytosolic Ca++ levels; Pre-NOTCH Processing in Golgi; Platelet calcium homeostasis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q93084](https://www.uniprot.org/uniprotkb/Q93084) (Sarcoplasmic/endoplasmic reticulum calcium ATPase 3):

> This magnesium-dependent enzyme catalyzes the hydrolysis of ATP coupled with the transport of calcium. Transports calcium ions from the cytosol into the sarcoplasmic/endoplasmic reticulum lumen. Contributes to calcium sequestration involved in muscular excitation/contraction.

**Summary**, from NCBI Gene [489](https://www.ncbi.nlm.nih.gov/gene/489):

> This gene encodes one of the SERCA Ca(2+)-ATPases, which are intracellular pumps located in the sarcoplasmic or endoplasmic reticula of muscle cells. This enzyme catalyzes the hydrolysis of ATP coupled with the translocation of calcium from the cytosol to the sarcoplasmic reticulum lumen, and is involved in calcium sequestration associated with muscular excitation and contraction. Alternative splicing results in multiple transcript variants encoding different isoforms. [provided by RefSeq, Jul …

**Accessions** — [HGNC:813](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:813) · Entrez [489](https://www.ncbi.nlm.nih.gov/gene/489) · UniProt [Q93084](https://www.uniprot.org/uniprotkb/Q93084) · Ensembl [ENSG00000074370](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000074370)

## Data

Gene col 1078: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1078); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1078, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1078]; `tensor/DDL_lfc|DDL_z.npy` [1078]; `embed/gene_vectors.npy` [1078]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1078 or target_col == 1078). Every well: [[ATP2A3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP2A3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
