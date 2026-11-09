---
drug: "Radotinib"
type: "drug"
salt_base: "Radotinib"
targets: "ABL1"
moa_fine: "Other TK inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 824
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Radotinib

*Other TK inhibitor (inhibitor/antagonist) · targets: ABL1 · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 1 / 43 / 824; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): -0.05 / 0.51.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:E12 | 0 / 1 | — | +0.25 | -0.6/+0.2/-0.3 | — |
| 0.5 µM | [[Plate 05]]:E12 | 31 / 12 | — | -0.86 | +0.3/+0.5/+0.6 | — |
| 5 µM | [[Plate 14]]:E12 | 360 / 464 | 0.947 | -0.23 | +0.3/+1.4/+0.1 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (31 genes, none with an alert; 12 shown): [[TFB1M]] 1.23× (z +4.6, 13/47 lines), [[CHDH]] 1.44× (z +4.0, 1/21 lines), [[ENSG00000260927]] 1.42× (z +4.0, 9/34 lines), [[METTL3]] 1.22× (z +3.9, 8/46 lines), [[SOGA3]] 1.32× (z +3.9, 6/25 lines), [[ZNF331]] 1.21× (z +3.9, 7/32 lines), [[FAM111A-DT]] 1.44× (z +3.8, 5/27 lines), [[GCSH]] 1.42× (z +3.6, 6/40 lines), [[RN7SKP255]] 4.14× (z +3.5, 30/45 lines), [[CSTF3-DT]] 1.40× (z +3.5, 6/27 lines), [[SLC35F4]] 1.42× (z +3.4, 3/26 lines), [[NLRP2]] 1.32× (z +3.3, 0/14 lines)

**5 µM** (360 genes, none with an alert; 12 shown): [[MAP2K6]] 2.48× (z +11.4, 22/26 lines), [[TM7SF3]] 1.38× (z +10.8, 42/48 lines), [[CAT]] 1.53× (z +9.5, 35/47 lines), [[CAMK2G]] 1.29× (z +9.1, 36/48 lines), [[ATP8B1]] 1.27× (z +8.9, 20/34 lines), [[OSBPL1A]] 1.25× (z +8.4, 28/46 lines), [[PIK3C2B]] 1.40× (z +7.9, 27/45 lines), [[NUAK1]] 1.34× (z +7.8, 24/43 lines), [[PPM1H]] 1.36× (z +7.7, 25/37 lines), [[EHMT2]] 1.41× (z +7.6, 35/48 lines), [[KRT80]] 1.50× (z +7.6, 13/26 lines), [[TRERF1]] 1.33× (z +7.5, 31/42 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[TSPAN33]] 0.716× (z -3.5, 1/35 lines)

**0.5 µM** (12 genes, none with an alert): [[ENSG00000290008]] 0.718× (z -4.6, 14/43 lines), [[ENSG00000256206]] 0.710× (z -3.9, 13/43 lines), [[ADAMTSL4-AS2]] 0.652× (z -3.8, 14/44 lines), [[YJU2]] 0.810× (z -3.7, 12/44 lines), [[EFCAB8]] 0.701× (z -3.4, 9/40 lines), [[CYB5D2]] 0.831× (z -3.3, 8/46 lines), [[ZNF320]] 0.819× (z -3.3, 7/34 lines), [[VWCE]] 0.686× (z -3.1, 12/44 lines), [[ENSG00000259053]] 0.782× (z -2.9, 10/39 lines), [[ENSG00000255202]] 0.637× (z -2.8, 13/36 lines), [[ITPKC]] 0.830× (z -2.8, 13/44 lines), [[LIF]] 0.782× (z -2.8, 7/38 lines)

**5 µM** (464 genes, none with an alert; 12 shown): [[CPEB4]] 0.787× (z -9.0, 34/47 lines), [[VMP1]] 0.757× (z -8.5, 41/48 lines), [[SEPTIN10]] 0.777× (z -8.4, 32/48 lines), [[TUT7]] 0.791× (z -8.0, 31/48 lines), [[SLC4A7]] 0.762× (z -8.0, 33/45 lines), [[PTGS2]] 0.619× (z -8.0, 18/21 lines), [[SPRY4]] 0.668× (z -7.3, 33/48 lines), [[PRDM1]] 0.712× (z -7.2, 20/33 lines), [[CD55]] 0.761× (z -7.1, 26/32 lines), [[CEMIP]] 0.619× (z -7.1, 24/29 lines), [[TFPI]] 0.719× (z -7.0, 27/34 lines), [[HOMER1]] 0.745× (z -7.0, 34/47 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[Module 045]] (+6.5), [[Module 146]] (+6.1), [[Module 182]] (+5.8) | [[Module 160]] (-3.3), [[Module 219]] (-3.1), [[Module 083]] (-3.0) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | [[SW 1271 (line)]] (1.60), [[CHP-212 (line)]] (1.53), [[Hs 766T (line)]] (1.47), [[NCI-H661 (line)]] (1.45) · weakest: [[HT-29 (line)]] (0.368), [[NCI-H1573 (line)]] (0.383), [[LoVo (line)]] (0.395) |
| 5 µM | [[SNU-1 (line)]] (-3.5), [[SK-MEL-2 (line)]] (-3.4) | [[AsPC-1 (line)]] (1.70), [[C32 (line)]] (1.63), [[RKO (line)]] (1.57), [[CHP-212 (line)]] (1.42) · weakest: [[SW48 (line)]] (0.407), [[NCI-H661 (line)]] (0.455), [[C-33 A (line)]] (0.649) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[Flumatinib (mesylate) (drug)]] (+0.84, Other TK inhibitor); [[Regorafenib (drug)]] (+0.83, Multi-TK inhibitor); [[Ponatinib (drug)]] (+0.72, Multi-TK inhibitor); [[Cabozantinib (S-malate) (drug)]] (+0.71, Multi-TK inhibitor); [[Afatinib (drug)]] (+0.63, EGFR/ERBB inhibitor); [[Bentamapimod (drug)]] (+0.59, Other MAPK inhibitor); [[Vandetanib (drug)]] (+0.55, Multi-TK inhibitor); [[NG25 (drug)]] (+0.52, Other MAPK inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Ralimetinib dimesylate (drug)]] (+0.46, Other MAPK inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 12 arrows, 12 of them with an alert ⚠; grade A 0, B 0, C 12.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[ENSG00000267174]] | 5 µM | C | ENSG00000267174 activity raises the cells' numbers under Radotinib 5 µM (protects the cells) | lines that do not express ENSG00000267174 (3) vs lines expressing it (45) | the lines without ENSG00000267174: 0.78× the cells of the other lines | 0.008 | ⚠ few lines (3 vs 47); across organs; also absent: FSCN2, ENSG00000229848, ZFP36; maybe low, not absent |
| [[ENSG00000291174]] | 5 µM | C | ENSG00000291174 activity raises the cells' numbers under Radotinib 5 µM (protects the cells) | lines that do not express ENSG00000291174 (3) vs lines expressing it (45) | the lines without ENSG00000291174: 0.80× the cells of the other lines | 0.012 | ⚠ few lines (3 vs 47); across organs; also absent: ZFP36, IQCN, NEK3 |
| [[TNFRSF25]] | 5 µM | C | TNFRSF25 activity raises the cells' numbers under Radotinib 5 µM (protects the cells) | lines that do not express TNFRSF25 (4) vs lines expressing it (44) | the lines without TNFRSF25: 0.81× the cells of the other lines | 0.014 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: PLEKHG5, ENSG00000284716 |
| [[IQCN]] | 5 µM | C | IQCN activity raises the cells' numbers under Radotinib 5 µM (protects the cells) | lines that do not express IQCN (3) vs lines expressing it (43) | the lines without IQCN: 0.79× the cells of the other lines | 0.021 | ⚠ few lines (3 vs 45); across organs; also absent: ENSG00000257894, CDC42EP1, PDE4C; maybe low, not absent |
| [[ENSG00000284716]] | 5 µM | C | ENSG00000284716 activity raises the cells' numbers under Radotinib 5 µM (protects the cells) | lines that do not express ENSG00000284716 (5) vs lines expressing it (43) | the lines without ENSG00000284716: 0.84× the cells of the other lines | 0.025 | ⚠ tissue-confounded; across organs; also absent: FTH1, TMEM184A, ZFP36; maybe low, not absent |
| [[FTH1]] | 5 µM | C | FTH1 activity raises the cells' numbers under Radotinib 5 µM (protects the cells) | lines that do not express FTH1 (4) vs lines expressing it (44) | the lines without FTH1: 0.83× the cells of the other lines | 0.031 | ⚠ few lines (4 vs 46); across organs; also absent: ENSG00000284716, ZFP36, DDR1; maybe low, not absent |
| [[NEK3]] | 5 µM | C | NEK3 activity raises the cells' numbers under Radotinib 5 µM (protects the cells) | lines that do not express NEK3 (3) vs lines expressing it (45) | the lines without NEK3: 0.81× the cells of the other lines | 0.041 | ⚠ few lines (3 vs 47); across organs; also absent: ZFP36, IQCN, SLC22A20P |
| [[MAPK11]] | 5 µM | C | MAPK11 activity raises the cells' numbers under Radotinib 5 µM (protects the cells) | lines that do not express MAPK11 (3) vs lines expressing it (45) | the lines without MAPK11: 0.82× the cells of the other lines | 0.046 | ⚠ few lines (3 vs 47); across organs; also absent: ADCY7, DBN1, LAMC1; maybe low, not absent |
| [[ENSG00000287264]] | 5 µM | C | ENSG00000287264 activity raises the cells' numbers under Radotinib 5 µM (protects the cells) | lines that do not express ENSG00000287264 (3) vs lines expressing it (45) | the lines without ENSG00000287264: 0.84× the cells of the other lines | 0.059 | ⚠ few lines (3 vs 47); across organs; also absent: PLEKHG5, MYH16, PER3; maybe low, not absent |
| [[DBNDD1]] | 5 µM | C | DBNDD1 activity raises the cells' numbers under Radotinib 5 µM (protects the cells) | lines that do not express DBNDD1 (3) vs lines expressing it (45) | the lines without DBNDD1: 0.83× the cells of the other lines | 0.075 | ⚠ few lines (3 vs 47); across organs; also absent: ARHGEF37, RHBDF2, EIF4E3 |
| [[ZFP36]] | 5 µM | C | ZFP36 activity raises the cells' numbers under Radotinib 5 µM (protects the cells) | lines that do not express ZFP36 (3) vs lines expressing it (45) | the lines without ZFP36: 0.82× the cells of the other lines | 0.084 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: FTH1, CDC42EP1, ENSG00000284716 |
| [[IGF2BP2]] | 5 µM | C | IGF2BP2 activity raises the cells' numbers under Radotinib 5 µM (protects the cells) | lines that do not express IGF2BP2 (3) vs lines expressing it (45) | the lines without IGF2BP2: 0.84× the cells of the other lines | 0.099 | ⚠ few lines (3 vs 47); across organs; also absent: PLS3, SLC25A43, SGK2 |

### Its targets: what acting on them probably does

*Drug-target arrows of the compound classes it belongs to (compounds sharing a listed target and mechanism; one molecule counts once, under all its names): the target → a gene whose level those compounds move. A row that names several targets is one test: the compounds share them all, and any of them could be the cause. 54 arrows, 54 of them with an alert ⚠; grade A 0, B 54, C 0. Shown: the 15 strongest; 39 more arrows (39 of them with an alert ⚠) not shown.*

| Its target | Gene it moves | This drug | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|---|
| [[ABL1]] | [[ANKMY2]] | moves it that way too | B | ABL1 activity lowers ANKMY2's level | compounds that target ABL1: 4 of 6 raise it (Flumatinib, NG25, Ponatinib, Radotinib) | 67% of the class's compounds vs 2.8% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ABL1]] | [[CDKN2B]] | moves it that way too | B | ABL1 activity raises CDKN2B's level | compounds that target ABL1: 3 of 6 lower it (NG25, Ponatinib, Radotinib) | 50% of the class's compounds vs 1.1% of all compounds | 0.025 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ABL1]] | [[GSG1L]] | moves it that way too | B | ABL1 activity raises GSG1L's level | compounds that target ABL1: 3 of 6 lower it (NG25, Ponatinib, Radotinib) | 50% of the class's compounds vs 1.1% of all compounds | 0.025 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ABL1]] | [[TMEM185A]] | moves it that way too | B | ABL1 activity lowers TMEM185A's level | compounds that target ABL1: 4 of 6 raise it (Flumatinib, NG25, Ponatinib, Radotinib) | 67% of the class's compounds vs 3.4% of all compounds | 0.025 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ABL1]] | [[NUAK1]] | moves it that way too | B | ABL1 activity lowers NUAK1's level | compounds that target ABL1: 4 of 6 raise it (Flumatinib, NG25, Ponatinib, Radotinib) | 67% of the class's compounds vs 3.6% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ABL1]] | [[CAMK2G]] | moves it that way too | B | ABL1 activity lowers CAMK2G's level | compounds that target ABL1: 4 of 6 raise it (Flumatinib, NG25, Ponatinib, Radotinib) | 67% of the class's compounds vs 3.9% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ABL1]] | [[CDKN1A]] | moves it that way too | B | ABL1 activity raises CDKN1A's level | compounds that target ABL1: 3 of 6 lower it (NG25, Ponatinib, Radotinib) | 50% of the class's compounds vs 1.4% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ABL1]] | [[ENSG00000225218]] | moves it that way too | B | ABL1 activity raises ENSG00000225218's level | compounds that target ABL1: 3 of 6 lower it (NG25, Ponatinib, Radotinib) | 50% of the class's compounds vs 1.4% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ABL1]] | [[ENSG00000290241]] | moves it that way too | B | ABL1 activity raises ENSG00000290241's level | compounds that target ABL1: 3 of 6 lower it (NG25, Ponatinib, Radotinib) | 50% of the class's compounds vs 1.4% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ABL1]] | [[HEATR6]] | moves it that way too | B | ABL1 activity lowers HEATR6's level | compounds that target ABL1: 3 of 6 raise it (Flumatinib, Ponatinib, Radotinib) | 50% of the class's compounds vs 1.4% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds |
| [[ABL1]] | [[PRKAB2]] | moves it that way too | B | ABL1 activity lowers PRKAB2's level | compounds that target ABL1: 3 of 6 raise it (NG25, Ponatinib, Radotinib) | 50% of the class's compounds vs 1.4% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ABL1]] | [[SLC8A2]] | moves it that way too | B | ABL1 activity raises SLC8A2's level | compounds that target ABL1: 3 of 6 lower it (NG25, Ponatinib, Radotinib) | 50% of the class's compounds vs 1.4% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ABL1]] | [[ALDH7A1]] | moves it that way too | B | ABL1 activity lowers ALDH7A1's level | compounds that target ABL1: 4 of 6 raise it (Flumatinib, NG25, Ponatinib, Radotinib) | 67% of the class's compounds vs 4.2% of all compounds | 0.037 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ABL1]] | [[ARL6]] | moves it that way too | B | ABL1 activity lowers ARL6's level | compounds that target ABL1: 4 of 6 raise it (Flumatinib, NG25, Ponatinib, Radotinib) | 67% of the class's compounds vs 4.2% of all compounds | 0.037 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ABL1]] | [[PIP4P2]] | moves it that way too | B | ABL1 activity lowers PIP4P2's level | compounds that target ABL1: 4 of 6 raise it (Flumatinib, NG25, Ponatinib, Radotinib) | 67% of the class's compounds vs 4.2% of all compounds | 0.037 | ⚠ off-target possible; 4 compounds; artifact flags |

## Data

- `tables/drugs.parquet` — drug == "Radotinib"
- `tables/drugdoses.parquet` — dd in 863, 864, 865
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
