---
drug: "Mebendazole"
type: "drug"
salt_base: "Mebendazole"
targets: "TUBA1A, TUBA1B, TUBA1C, TUBB, TUBB1, TUBB2A, TUBB3, TUBB4A, TUBB4B, TUBB6"
moa_fine: "Microtubule inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 1202
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Mebendazole

*Microtubule inhibitor (inhibitor/antagonist) · targets: TUBA1A, TUBA1B, TUBA1C, TUBB, TUBB1, TUBB2A, TUBB3, TUBB4A, TUBB4B, TUBB6 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 4 / 65 / 1202; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.17 / 0.21.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:E11 | 3 / 1 | — | +0.16 | -0.5/+0.1/-0.1 | — |
| 0.5 µM | [[Plate 08]]:E11 | 62 / 3 | — | -0.24 | +0.5/+2.4/+1.1 | — |
| 5 µM | [[Plate 09]]:E11 | 259 / 943 | — | +1.22 | +2.5/+3.4/+2.9 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (3 genes, none with an alert): [[ENSG00000100101]] 1.28× (z +3.6, 13/47 lines), [[RPL18A]] 1.59× (z +3.5, 17/46 lines), [[GBA2]] 1.24× (z +3.5, 4/47 lines)

**0.5 µM** (62 genes, none with an alert; 12 shown): [[PLK1]] 1.43× (z +4.7, 15/47 lines), [[BRD8]] 1.21× (z +4.4, 18/48 lines), [[KNSTRN]] 1.30× (z +4.2, 12/47 lines), [[KIF18B]] 1.39× (z +4.1, 20/46 lines), [[ENSG00000248774]] 1.58× (z +4.1, 8/43 lines), [[ENSG00000258101]] 1.43× (z +4.0, 9/41 lines), [[ARHGAP11A]] 1.28× (z +4.0, 22/47 lines), [[TROAP]] 1.31× (z +4.0, 6/47 lines), [[TACC3]] 1.25× (z +3.9, 16/48 lines), [[ELAVL2]] 1.36× (z +3.8, 1/14 lines), [[AURKA]] 1.32× (z +3.8, 16/48 lines), [[KIF5C]] 1.27× (z +3.8, 12/48 lines)

**5 µM** (259 genes, none with an alert; 12 shown): [[CAPN2]] 1.27× (z +5.5, 27/48 lines), [[CREB5]] 1.37× (z +5.3, 18/33 lines), [[KIF1C]] 1.32× (z +5.2, 24/48 lines), [[HSPH1]] 1.67× (z +5.1, 39/48 lines), [[TOMM34]] 1.37× (z +5.0, 23/48 lines), [[IPO7]] 1.30× (z +4.9, 34/48 lines), [[RECQL]] 1.24× (z +4.9, 23/47 lines), [[CCNB1]] 1.49× (z +4.8, 27/47 lines), [[RPS10-NUDT3]] 1.82× (z +4.7, 19/46 lines), [[TPM4]] 1.35× (z +4.7, 40/48 lines), [[BZW1]] 1.43× (z +4.7, 44/48 lines), [[CMTM1]] 1.47× (z +4.6, 18/46 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[ENSG00000253106]] 0.639× (z -3.9, 15/39 lines)

**0.5 µM** (3 genes, none with an alert): [[IL1RAP]] 0.827× (z -3.1, 16/40 lines), [[NR4A3]] 0.743× (z -3.0, 14/41 lines), [[PLD1]] 0.827× (z -2.7, 14/41 lines)

**5 µM** (943 genes, none with an alert; 12 shown): [[TENT5A]] 0.659× (z -7.0, 28/37 lines), [[HOXA3]] 0.695× (z -6.7, 21/39 lines), [[ENSG00000285755]] 0.479× (z -6.7, 14/37 lines), [[SNTB1]] 0.650× (z -6.4, 21/29 lines), [[HOXB3]] 0.712× (z -6.1, 20/39 lines), [[LINC01876]] 0.636× (z -5.9, 19/24 lines), [[PDE4D]] 0.675× (z -5.9, 25/35 lines), [[MEIS2]] 0.733× (z -5.9, 35/44 lines), [[DACH1]] 0.563× (z -5.8, 12/18 lines), [[THBS3-AS1]] 0.493× (z -5.7, 17/41 lines), [[FRK]] 0.668× (z -5.7, 16/26 lines), [[TRIM2]] 0.765× (z -5.6, 19/33 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[Module 060]] (+2.6) | [[Module 223]] (-3.0), [[Module 200]] (-3.0), [[Module 152]] (-2.6) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | [[C32 (line)]] (-3.2) | [[HT-29 (line)]] (1.55), [[H4 (line)]] (1.54), [[SW 1088 (line)]] (1.46), [[SW 900 (line)]] (1.43) · weakest: [[BT-474 (line)]] (0.237), [[SW1417 (line)]] (0.299), [[SHP-77 (line)]] (0.423) |
| 5 µM | [[RKO (line)]] (-4.1), [[A-427 (line)]] (-3.9), [[LOX-IMVI (line)]] (-3.9), [[SK-MEL-2 (line)]] (-3.8), [[C-33 A (line)]] (-3.8) | [[MIA PaCa-2 (line)]] (1.65), [[SW 1088 (line)]] (1.53), [[H4 (line)]] (1.46), [[A549 (line)]] (1.41) · weakest: [[AN3 CA (line)]] (0.527), [[COLO 205 (line)]] (0.607), [[SHP-77 (line)]] (0.671) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Peretinoin (drug)]] (+0.57, Retinoic receptor agonist); [[Daptomycin (drug)]] (+0.56, unclear, ⚠ no trustworthy dose (vector dose flagged: unreliable plate only)); [[Rucaparib (phosphate) (drug)]] (+0.53, DNA synthesis/repair inhibitor, ⚠ only 5 significant genes); [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] (+0.51, unclear); [[Ranolazine (drug)]] (+0.50, unclear); [[BAY1125976 (drug)]] (+0.48, PI3K/AKT inhibitor); [[Dabrafenib (drug)]] (+0.48, RAF inhibitor); [[Futibatinib (drug)]] (+0.46, Other TK inhibitor); [[Lucanthone (drug)]] (+0.46, unclear); [[Tucatinib (drug)]] (+0.45, EGFR/ERBB inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 29 arrows, 29 of them with an alert ⚠; grade A 0, B 20, C 9. Shown: the 15 strongest; 14 more arrows (14 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[ALDH3B1]] | 5 µM | B | ALDH3B1 activity raises the cells' numbers under Mebendazole 5 µM (protects the cells) | lines that do not express ALDH3B1 (9) vs lines expressing it (39) | the lines without ALDH3B1: 0.61× the cells of the other lines | 0.036 | ⚠ within organs, on part of the lines; also absent: NIBAN2, IER3, FOSL1; maybe low, not absent |
| [[IL15]] | 5 µM | B | IL15 activity raises the cells' numbers under Mebendazole 5 µM (protects the cells) | lines that do not express IL15 (10) vs lines expressing it (38) | the lines without IL15: 0.63× the cells of the other lines | 0.046 | ⚠ within organs, on part of the lines; also absent: TGFBR2, ITGA3, PSORS1C1; maybe low, not absent |
| [[BMPER]] | 0.5 µM | B | BMPER activity lowers the cells' numbers under Mebendazole 0.5 µM (makes them more sensitive) | lines that do not express BMPER (21) vs lines expressing it (27) | the lines without BMPER: 1.12× the cells of the other lines | 0.046 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000253471, IL7R |
| [[SPOCK1]] | 5 µM | B | SPOCK1 activity raises the cells' numbers under Mebendazole 5 µM (protects the cells) | lines that do not express SPOCK1 (29) vs lines expressing it (19) | the lines without SPOCK1: 0.69× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41 |
| [[ADAM12]] | 5 µM | B | ADAM12 activity raises the cells' numbers under Mebendazole 5 µM (protects the cells) | lines that do not express ADAM12 (27) vs lines expressing it (21) | the lines without ADAM12: 0.69× the cells of the other lines | 0.056 | ⚠ within organs, on part of the lines; also absent: ZEB2, MSC-AS1, CNRIP1 |
| [[TGFBR2]] | 5 µM | B | TGFBR2 activity raises the cells' numbers under Mebendazole 5 µM (protects the cells) | lines that do not express TGFBR2 (7) vs lines expressing it (41) | the lines without TGFBR2: 0.58× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: VDR, TRIB1, MET |
| [[ENSG00000230647]] | 5 µM | B | ENSG00000230647 activity raises the cells' numbers under Mebendazole 5 µM (protects the cells) | lines that do not express ENSG00000230647 (24) vs lines expressing it (24) | the lines without ENSG00000230647: 0.70× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: ADAM12, ENSG00000253891, SPOCK1 |
| [[ENSG00000251537]] | 5 µM | B | ENSG00000251537 activity raises the cells' numbers under Mebendazole 5 µM (protects the cells) | lines that do not express ENSG00000251537 (9) vs lines expressing it (39) | the lines without ENSG00000251537: 0.73× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: FBXW10B, PCED1B, NHS; maybe low, not absent |
| [[KCNMA1]] | 5 µM | B | KCNMA1 activity raises the cells' numbers under Mebendazole 5 µM (protects the cells) | lines that do not express KCNMA1 (26) vs lines expressing it (22) | the lines without KCNMA1: 0.68× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |
| [[SIRLNT]] | 5 µM | B | SIRLNT activity raises the cells' numbers under Mebendazole 5 µM (protects the cells) | lines that do not express SIRLNT (32) vs lines expressing it (16) | the lines without SIRLNT: 0.66× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SRGN, LINC01411, KCNMA1 |
| [[IGSF9]] | 5 µM | B | IGSF9 activity raises the cells' numbers under Mebendazole 5 µM (protects the cells) | lines that do not express IGSF9 (16) vs lines expressing it (32) | the lines without IGSF9: 0.79× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; also absent: DUSP4, CREG2, LYPD3 |
| [[RSPO3]] | 5 µM | B | RSPO3 activity raises the cells' numbers under Mebendazole 5 µM (protects the cells) | lines that do not express RSPO3 (39) vs lines expressing it (9) | the lines without RSPO3: 0.70× the cells of the other lines | 0.086 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, TBXT, GSG1L2 |
| [[ENSG00000259200]] | 5 µM | B | ENSG00000259200 activity raises the cells' numbers under Mebendazole 5 µM (protects the cells) | lines that do not express ENSG00000259200 (18) vs lines expressing it (30) | the lines without ENSG00000259200: 0.74× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: ENSG00000203635, CSGALNACT1, ENSG00000232692; maybe low, not absent |
| [[SPOCK1]] | 0.5 µM | B | SPOCK1 activity lowers the cells' numbers under Mebendazole 0.5 µM (makes them more sensitive) | lines that do not express SPOCK1 (29) vs lines expressing it (19) | the lines without SPOCK1: 1.05× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41 |
| [[LINC02057]] | 5 µM | B | LINC02057 activity raises the cells' numbers under Mebendazole 5 µM (protects the cells) | lines that do not express LINC02057 (25) vs lines expressing it (23) | the lines without LINC02057: 0.71× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: CSF3, PTHLH, IL6 |

### Its targets: what acting on them probably does

*Drug-target arrows of the compound classes it belongs to (compounds sharing a listed target and mechanism; one molecule counts once, under all its names): the target → a gene whose level those compounds move. A row that names several targets is one test: the compounds share them all, and any of them could be the cause. 4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Its target | Gene it moves | This drug | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|---|
| TUBB1, [[TUBB2A]], [[TUBB3]], TUBB4A, [[TUBB4B]] | [[SGSH]] | moves it that way too | B | TUBB1, TUBB2A, TUBB3, TUBB4A, TUBB4B activity raises SGSH's level | compounds that target TUBB1, TUBB2A, TUBB3, TUBB4A, TUBB4B: 2 of 2 lower it (Docetaxel, Mebendazole) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; shared targets |
| TUBB1, [[TUBB2A]], [[TUBB3]], TUBB4A, [[TUBB4B]] | [[MZT1]] | moves it that way too | B | TUBB1, TUBB2A, TUBB3, TUBB4A, TUBB4B activity lowers MZT1's level | compounds that target TUBB1, TUBB2A, TUBB3, TUBB4A, TUBB4B: 2 of 2 raise it (Docetaxel, Mebendazole) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| TUBB1, [[TUBB2A]], [[TUBB3]], TUBB4A, [[TUBB4B]] | [[ENSG00000287352]] | moves it that way too | B | TUBB1, TUBB2A, TUBB3, TUBB4A, TUBB4B activity lowers ENSG00000287352's level | compounds that target TUBB1, TUBB2A, TUBB3, TUBB4A, TUBB4B: 2 of 2 raise it (Docetaxel, Mebendazole) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| TUBB1, [[TUBB2A]], [[TUBB3]], TUBB4A, [[TUBB4B]] | [[RAB28]] | moves it that way too | B | TUBB1, TUBB2A, TUBB3, TUBB4A, TUBB4B activity raises RAB28's level | compounds that target TUBB1, TUBB2A, TUBB3, TUBB4A, TUBB4B: 2 of 2 lower it (Docetaxel, Mebendazole) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

## Data

- `tables/drugs.parquet` — drug == "Mebendazole"
- `tables/drugdoses.parquet` — dd in 657, 658, 659
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
