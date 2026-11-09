---
drug: "Flumatinib (mesylate)"
type: "drug"
salt_base: "Flumatinib"
targets: "ABL1"
moa_fine: "Other TK inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 225
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Flumatinib (mesylate)

*Other TK inhibitor (inhibitor/antagonist) · targets: ABL1 · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 5 / 33 / 225; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.23 / 0.54.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:B8 | 2 / 3 | — | +0.08 | +0.9/+0.6/+0.4 | — |
| 0.5 µM | [[Plate 08]]:B8 | 2 / 31 | — | +0.47 | +1.5/+1.0/+1.9 | — |
| 5 µM | [[Plate 09]]:B8 | 102 / 123 | — | +0.13 | +1.9/+0.9/+0.8 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (2 genes, none with an alert): [[OCA2]] 1.38× (z +2.9, 0/21 lines), [[ATAD3A]] 1.24× (z +2.9, 2/45 lines)

**0.5 µM** (2 genes, none with an alert): [[COTL1]] 1.21× (z +2.7, 13/43 lines), [[RPS10-NUDT3]] 1.39× (z +2.7, 1/47 lines)

**5 µM** (102 genes, none with an alert; 12 shown): [[MAP2K6]] 2.06× (z +6.2, 17/25 lines), [[CAMK2G]] 1.25× (z +5.5, 21/48 lines), [[TM7SF3]] 1.26× (z +5.3, 23/47 lines), [[TMEM131L]] 1.34× (z +5.2, 24/45 lines), [[NUAK1]] 1.32× (z +5.1, 13/42 lines), [[RAB30]] 1.36× (z +5.0, 23/48 lines), [[DIXDC1]] 1.28× (z +4.8, 18/48 lines), [[SLC25A12]] 1.25× (z +4.7, 21/48 lines), [[PECR]] 1.26× (z +4.6, 10/46 lines), [[ALDH7A1]] 1.23× (z +4.6, 20/46 lines), [[IDH1]] 1.40× (z +4.6, 25/47 lines), [[EEF2K]] 1.22× (z +4.5, 15/48 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (3 genes, none with an alert): [[IGIP]] 0.737× (z -3.4, 12/46 lines), [[SLC66A3]] 0.817× (z -3.0, 7/45 lines), [[SLC2A10]] 0.769× (z -2.7, 6/27 lines)

**0.5 µM** (31 genes, none with an alert; 12 shown): [[ENSG00000255158]] 0.673× (z -3.8, 6/44 lines), [[BATF2]] 0.636× (z -3.6, 8/33 lines), [[POC1B-AS1]] 0.732× (z -3.5, 16/47 lines), [[TBX15]] 0.679× (z -3.5, 9/38 lines), [[ARHGEF6]] 0.772× (z -3.4, 6/26 lines), [[SERPINB9P1]] 0.724× (z -3.3, 6/29 lines), [[SLC35G2]] 0.811× (z -3.3, 13/36 lines), [[SULT1C2]] 0.683× (z -3.2, 2/17 lines), [[GSAP]] 0.802× (z -3.2, 11/42 lines), [[PLEKHO1]] 0.796× (z -3.2, 3/34 lines), [[TRIM22]] 0.735× (z -3.1, 9/30 lines), [[CALCOCO1]] 0.785× (z -3.0, 15/48 lines)

**5 µM** (123 genes, none with an alert; 12 shown): [[DHRSX]] 0.807× (z -5.0, 24/47 lines), [[ST3GAL1]] 0.764× (z -4.9, 19/37 lines), [[ITGA2]] 0.701× (z -4.5, 26/37 lines), [[MARCHF3]] 0.765× (z -4.4, 20/43 lines), [[TSG101]] 0.818× (z -4.4, 20/48 lines), [[PTGS2]] 0.681× (z -4.4, 11/21 lines), [[AKAP12]] 0.664× (z -4.3, 25/30 lines), [[CEMIP]] 0.649× (z -4.3, 17/29 lines), [[ENSG00000259753]] 0.619× (z -4.3, 10/22 lines), [[LUCAT1]] 0.744× (z -4.3, 26/40 lines), [[PRDM1]] 0.743× (z -4.3, 9/32 lines), [[ZHX2]] 0.781× (z -4.2, 23/41 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | [[Module 182]] (+2.0) | [[Module 170]] (-2.2) |
| 5 µM | [[Module 182]] (+3.4), [[Module 146]] (+3.2), [[Module 030]] (+2.7) | [[Module 160]] (-2.1) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | [[CHP-212 (line)]] (1.81), [[A549 (line)]] (1.73), [[C32 (line)]] (1.70), [[SNU-423 (line)]] (1.65) · weakest: [[HT-29 (line)]] (0.101), [[LS 180 (line)]] (0.439), [[LoVo (line)]] (0.466) |
| 5 µM | — | [[SW 1271 (line)]] (1.52), [[SK-MEL-2 (line)]] (1.49), [[hTERT-HPNE (line)]] (1.32), [[SW 900 (line)]] (1.32) · weakest: [[NCI-H661 (line)]] (0.587), [[SW48 (line)]] (0.662), [[HCT15 (line)]] (0.671) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar.*

- [[Radotinib (drug)]] (+0.84, Other TK inhibitor); [[Regorafenib (drug)]] (+0.74, Multi-TK inhibitor); [[Ponatinib (drug)]] (+0.67, Multi-TK inhibitor); [[Cabozantinib (S-malate) (drug)]] (+0.63, Multi-TK inhibitor); [[Bentamapimod (drug)]] (+0.62, Other MAPK inhibitor); [[Afatinib (drug)]] (+0.60, EGFR/ERBB inhibitor); [[Ralimetinib dimesylate (drug)]] (+0.56, Other MAPK inhibitor); [[Vandetanib (drug)]] (+0.51, Multi-TK inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 36 arrows, 36 of them with an alert ⚠; grade A 0, B 11, C 25. Shown: the 15 strongest; 21 more arrows (21 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[ALDH3B1]] | 0.5 µM | B | ALDH3B1 activity raises the cells' numbers under Flumatinib (mesylate) 0.5 µM (protects the cells) | lines that do not express ALDH3B1 (9) vs lines expressing it (39) | the lines without ALDH3B1: 0.81× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; also absent: NIBAN2, IER3, FOSL1; maybe low, not absent |
| [[ENSG00000230647]] | 0.5 µM | B | ENSG00000230647 activity raises the cells' numbers under Flumatinib (mesylate) 0.5 µM (protects the cells) | lines that do not express ENSG00000230647 (24) vs lines expressing it (24) | the lines without ENSG00000230647: 0.89× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; also absent: ADAM12, ENSG00000253891, SPOCK1 |
| [[FUT9]] | 0.5 µM | B | FUT9 activity lowers the cells' numbers under Flumatinib (mesylate) 0.5 µM (makes them more sensitive) | lines that do not express FUT9 (40) vs lines expressing it (8) | the lines without FUT9: 1.16× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, KCNH7, GCG |
| [[KCNMA1]] | 0.5 µM | B | KCNMA1 activity raises the cells' numbers under Flumatinib (mesylate) 0.5 µM (protects the cells) | lines that do not express KCNMA1 (26) vs lines expressing it (22) | the lines without KCNMA1: 0.85× the cells of the other lines | 0.078 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |
| [[HRH1]] | 0.5 µM | B | HRH1 activity raises the cells' numbers under Flumatinib (mesylate) 0.5 µM (protects the cells) | lines that do not express HRH1 (10) vs lines expressing it (38) | the lines without HRH1: 0.77× the cells of the other lines | 0.087 | ⚠ within organs, on part of the lines; also absent: PHLDA2, PLAUR, LRRK1; maybe low, not absent |
| [[CKMT1B]] | 0.5 µM | B | CKMT1B activity lowers the cells' numbers under Flumatinib (mesylate) 0.5 µM (makes them more sensitive) | lines that do not express CKMT1B (28) vs lines expressing it (20) | the lines without CKMT1B: 1.10× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: CKMT1A, SYK, PPP1R1B |
| [[ENSG00000259200]] | 0.5 µM | B | ENSG00000259200 activity raises the cells' numbers under Flumatinib (mesylate) 0.5 µM (protects the cells) | lines that do not express ENSG00000259200 (18) vs lines expressing it (30) | the lines without ENSG00000259200: 0.88× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: ENSG00000203635, CSGALNACT1, ENSG00000232692; maybe low, not absent |
| [[ENSG00000242828]] | 0.5 µM | B | ENSG00000242828 activity lowers the cells' numbers under Flumatinib (mesylate) 0.5 µM (makes them more sensitive) | lines that do not express ENSG00000242828 (35) vs lines expressing it (13) | the lines without ENSG00000242828: 1.15× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: LINC02050, ENSG00000286329, ENSG00000289605; maybe low, not absent |
| [[GABRG2]] | 0.5 µM | B | GABRG2 activity lowers the cells' numbers under Flumatinib (mesylate) 0.5 µM (makes them more sensitive) | lines that do not express GABRG2 (36) vs lines expressing it (12) | the lines without GABRG2: 1.16× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, PCSK1, BAGE2; maybe low, not absent |
| [[SRGN]] | 0.5 µM | B | SRGN activity raises the cells' numbers under Flumatinib (mesylate) 0.5 µM (protects the cells) | lines that do not express SRGN (30) vs lines expressing it (18) | the lines without SRGN: 0.83× the cells of the other lines | 0.096 | ⚠ within organs, on part of the lines; also absent: SIRLNT, SPOCK1, KIRREL3 |
| [[SPOCK1]] | 0.5 µM | B | SPOCK1 activity raises the cells' numbers under Flumatinib (mesylate) 0.5 µM (protects the cells) | lines that do not express SPOCK1 (29) vs lines expressing it (19) | the lines without SPOCK1: 0.86× the cells of the other lines | 0.096 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41 |
| [[PHF11]] | 0.5 µM | C | PHF11 activity raises the cells' numbers under Flumatinib (mesylate) 0.5 µM (protects the cells) | lines that do not express PHF11 (3) vs lines expressing it (45) | the lines without PHF11: 0.72× the cells of the other lines | 0.008 | ⚠ few lines (3 vs 47); across organs; also absent: NABP1, ANXA2, SDC4 |
| [[PSMB8]] | 0.5 µM | C | PSMB8 activity raises the cells' numbers under Flumatinib (mesylate) 0.5 µM (protects the cells) | lines that do not express PSMB8 (4) vs lines expressing it (44) | the lines without PSMB8: 0.76× the cells of the other lines | 0.015 | ⚠ few lines (4 vs 46); across organs; co-occurs with WNK2; also absent: TBILA, GCA, C3orf52 |
| [[TBILA]] | 0.5 µM | C | TBILA activity raises the cells' numbers under Flumatinib (mesylate) 0.5 µM (protects the cells) | lines that do not express TBILA (5) vs lines expressing it (43) | the lines without TBILA: 0.77× the cells of the other lines | 0.025 | ⚠ tissue-confounded; across organs; also absent: C3orf52, ISG20, PSMB8 |
| [[SETD7]] | 0.5 µM | C | SETD7 activity raises the cells' numbers under Flumatinib (mesylate) 0.5 µM (protects the cells) | lines that do not express SETD7 (3) vs lines expressing it (45) | the lines without SETD7: 0.75× the cells of the other lines | 0.034 | ⚠ few lines (3 vs 47); across organs; also absent: MAP3K5, SNHG15; maybe low, not absent |

### Its targets: what acting on them probably does

*Drug-target arrows of the compound classes it belongs to (compounds sharing a listed target and mechanism; one molecule counts once, under all its names): the target → a gene whose level those compounds move. A row that names several targets is one test: the compounds share them all, and any of them could be the cause. 54 arrows, 54 of them with an alert ⚠; grade A 0, B 54, C 0. Shown: the 15 strongest; 39 more arrows (39 of them with an alert ⚠) not shown.*

| Its target | Gene it moves | This drug | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|---|
| [[ABL1]] | [[ANKMY2]] | moves it that way too | B | ABL1 activity lowers ANKMY2's level | compounds that target ABL1: 4 of 6 raise it (Flumatinib, NG25, Ponatinib, Radotinib) | 67% of the class's compounds vs 2.8% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ABL1]] | [[CDKN2B]] | does not move it that way (the class's other compounds do) | B | ABL1 activity raises CDKN2B's level | compounds that target ABL1: 3 of 6 lower it (NG25, Ponatinib, Radotinib) | 50% of the class's compounds vs 1.1% of all compounds | 0.025 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ABL1]] | [[GSG1L]] | does not move it that way (the class's other compounds do) | B | ABL1 activity raises GSG1L's level | compounds that target ABL1: 3 of 6 lower it (NG25, Ponatinib, Radotinib) | 50% of the class's compounds vs 1.1% of all compounds | 0.025 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ABL1]] | [[TMEM185A]] | moves it that way too | B | ABL1 activity lowers TMEM185A's level | compounds that target ABL1: 4 of 6 raise it (Flumatinib, NG25, Ponatinib, Radotinib) | 67% of the class's compounds vs 3.4% of all compounds | 0.025 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ABL1]] | [[NUAK1]] | moves it that way too | B | ABL1 activity lowers NUAK1's level | compounds that target ABL1: 4 of 6 raise it (Flumatinib, NG25, Ponatinib, Radotinib) | 67% of the class's compounds vs 3.6% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ABL1]] | [[CAMK2G]] | moves it that way too | B | ABL1 activity lowers CAMK2G's level | compounds that target ABL1: 4 of 6 raise it (Flumatinib, NG25, Ponatinib, Radotinib) | 67% of the class's compounds vs 3.9% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ABL1]] | [[CDKN1A]] | does not move it that way (the class's other compounds do) | B | ABL1 activity raises CDKN1A's level | compounds that target ABL1: 3 of 6 lower it (NG25, Ponatinib, Radotinib) | 50% of the class's compounds vs 1.4% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ABL1]] | [[ENSG00000225218]] | does not move it that way (the class's other compounds do) | B | ABL1 activity raises ENSG00000225218's level | compounds that target ABL1: 3 of 6 lower it (NG25, Ponatinib, Radotinib) | 50% of the class's compounds vs 1.4% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ABL1]] | [[ENSG00000290241]] | does not move it that way (the class's other compounds do) | B | ABL1 activity raises ENSG00000290241's level | compounds that target ABL1: 3 of 6 lower it (NG25, Ponatinib, Radotinib) | 50% of the class's compounds vs 1.4% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ABL1]] | [[HEATR6]] | moves it that way too | B | ABL1 activity lowers HEATR6's level | compounds that target ABL1: 3 of 6 raise it (Flumatinib, Ponatinib, Radotinib) | 50% of the class's compounds vs 1.4% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds |
| [[ABL1]] | [[PRKAB2]] | does not move it that way (the class's other compounds do) | B | ABL1 activity lowers PRKAB2's level | compounds that target ABL1: 3 of 6 raise it (NG25, Ponatinib, Radotinib) | 50% of the class's compounds vs 1.4% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ABL1]] | [[SLC8A2]] | does not move it that way (the class's other compounds do) | B | ABL1 activity raises SLC8A2's level | compounds that target ABL1: 3 of 6 lower it (NG25, Ponatinib, Radotinib) | 50% of the class's compounds vs 1.4% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ABL1]] | [[ALDH7A1]] | moves it that way too | B | ABL1 activity lowers ALDH7A1's level | compounds that target ABL1: 4 of 6 raise it (Flumatinib, NG25, Ponatinib, Radotinib) | 67% of the class's compounds vs 4.2% of all compounds | 0.037 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ABL1]] | [[ARL6]] | moves it that way too | B | ABL1 activity lowers ARL6's level | compounds that target ABL1: 4 of 6 raise it (Flumatinib, NG25, Ponatinib, Radotinib) | 67% of the class's compounds vs 4.2% of all compounds | 0.037 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ABL1]] | [[PIP4P2]] | moves it that way too | B | ABL1 activity lowers PIP4P2's level | compounds that target ABL1: 4 of 6 raise it (Flumatinib, NG25, Ponatinib, Radotinib) | 67% of the class's compounds vs 4.2% of all compounds | 0.037 | ⚠ off-target possible; 4 compounds; artifact flags |

## Data

- `tables/drugs.parquet` — drug == "Flumatinib (mesylate)"
- `tables/drugdoses.parquet` — dd in 456, 457, 458
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
