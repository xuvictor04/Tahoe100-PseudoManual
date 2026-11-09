---
drug: "Everolimus"
type: "drug"
salt_base: "Everolimus"
targets: "MTOR, FKBP1A"
moa_fine: "MTOR inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 22
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Everolimus

*MTOR inhibitor (inhibitor/antagonist) · targets: MTOR, FKBP1A · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 4 / 0 / 22; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.04 / 0.26.
> Flags by dose: - / noisy plate (z scaled) / noisy plate (z scaled).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:A3, [[Plate 01]]:E9 | 4 / 0 | 0.487 | -0.29 | +0.3/+0.7/+0.6 | — |
| 0.5 µM | [[Plate 02]]:A3, [[Plate 02]]:E9 | 0 / 0 | 0.305 | -0.47 | -0.5/-0.2/-0.5 | noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:A3, [[Plate 03]]:E9 | 1 / 21 | 0.398 | +0.30 | +0.4/-0.5/-0.4 | noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (4 genes, none with an alert): [[TXLNGY]] 1.21× (z +3.3, 0/18 lines), [[NT5M]] 1.20× (z +3.3, 4/39 lines), [[ACKR3]] 1.35× (z +3.0, 0/16 lines), [[SLC44A4]] 1.28× (z +2.9, 0/11 lines)

**5 µM** (1 gene, none with an alert): [[RABEPK]] 1.27× (z +2.8, 3/48 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**5 µM** (21 genes, none with an alert; 12 shown): [[CCDC28A]] 0.666× (z -5.2, 22/48 lines), [[PDCD4]] 0.745× (z -4.7, 29/50 lines), [[TFDP2]] 0.817× (z -4.6, 20/50 lines), [[FBXO25]] 0.778× (z -4.0, 8/44 lines), [[KLHL24]] 0.707× (z -3.9, 28/50 lines), [[TCP11L2]] 0.671× (z -3.6, 19/49 lines), [[FBXO32]] 0.716× (z -3.6, 11/36 lines), [[JMY]] 0.743× (z -3.5, 16/49 lines), [[YPEL2]] 0.768× (z -3.3, 6/45 lines), [[HSD17B7]] 0.725× (z -3.3, 7/47 lines), [[GABARAPL1]] 0.742× (z -3.2, 11/45 lines), [[WIPI2]] 0.819× (z -3.2, 17/49 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | [[NCI-H23 (line)]] (1.98), [[MIA PaCa-2 (line)]] (1.81), [[NCI-H661 (line)]] (1.75), [[AsPC-1 (line)]] (1.63) · weakest: [[NCI-H596 (line)]] (0.0183), [[A-172 (line)]] (0.516), [[A498 (line)]] (0.537) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[c-Kit-IN-1 (drug)]] (+0.64, Multi-TK inhibitor); [[Sapanisertib (drug)]] (+0.62, MTOR inhibitor); [[EX229 (drug)]] (+0.61, unclear); [[TAK-733 (drug)]] (+0.55, MEK inhibitor); [[Abemaciclib (drug)]] (+0.54, CDK inhibitor); [[venetoclax (drug)]] (+0.46, unclear); [[Ataluren (drug)]] (+0.45, unclear, ⚠ only 7 significant genes); [[NVP-BHG712 (drug)]] (+0.42, unclear); [[Ropivacaine (hydrochloride monohydrate) (drug)]] (+0.41, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 10 arrows, 10 of them with an alert ⚠; grade A 0, B 3, C 7.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[NCALD]] | 5 µM | B | NCALD activity lowers the cells' numbers under Everolimus 5 µM (makes them more sensitive) | lines that do not express NCALD (18) vs lines expressing it (30) | the lines without NCALD: 1.08× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: MOGAT3, EPHA1, HNF1A; maybe low, not absent |
| [[SLC2A9]] | 5 µM | B | SLC2A9 activity lowers the cells' numbers under Everolimus 5 µM (makes them more sensitive) | lines that do not express SLC2A9 (6) vs lines expressing it (42) | the lines without SLC2A9: 1.14× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: VDR, SEMA4G, TBC1D8B; maybe low, not absent |
| [[STON2]] | 5 µM | B | STON2 activity lowers the cells' numbers under Everolimus 5 µM (makes them more sensitive) | lines that do not express STON2 (19) vs lines expressing it (29) | the lines without STON2: 1.14× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: FRK, RASSF6, AQP3 |
| [[STX1A]] | 5 µM | C | STX1A activity lowers the cells' numbers under Everolimus 5 µM (makes them more sensitive) | lines that do not express STX1A (3) vs lines expressing it (45) | the lines without STX1A: 1.37× the cells of the other lines | 0.004 | ⚠ few lines (3 vs 47); across organs; also absent: RABGEF1P3, SKAP2, PYGB; maybe low, not absent |
| [[TBILA]] | 5 µM | C | TBILA activity lowers the cells' numbers under Everolimus 5 µM (makes them more sensitive) | lines that do not express TBILA (5) vs lines expressing it (43) | the lines without TBILA: 1.28× the cells of the other lines | 0.008 | ⚠ tissue-confounded; across organs; also absent: C3orf52, ISG20, PSMB8 |
| [[PYGB]] | 5 µM | C | PYGB activity lowers the cells' numbers under Everolimus 5 µM (makes them more sensitive) | lines that do not express PYGB (3) vs lines expressing it (45) | the lines without PYGB: 1.32× the cells of the other lines | 0.016 | ⚠ few lines (3 vs 47); across organs; also absent: PBX4, STX1A, UGDH; maybe low, not absent |
| [[ENSG00000255031]] | 5 µM | C | ENSG00000255031 activity lowers the cells' numbers under Everolimus 5 µM (makes them more sensitive) | lines that do not express ENSG00000255031 (3) vs lines expressing it (45) | the lines without ENSG00000255031: 1.32× the cells of the other lines | 0.029 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: GLMP, TCIRG1, MT1X; maybe low, not absent |
| [[LRRC56]] | 5 µM | C | LRRC56 activity lowers the cells' numbers under Everolimus 5 µM (makes them more sensitive) | lines that do not express LRRC56 (3) vs lines expressing it (45) | the lines without LRRC56: 1.33× the cells of the other lines | 0.046 | ⚠ few lines (3 vs 47); across organs; also absent: NMRAL1, LMNTD2, ENSG00000205890; maybe low, not absent |
| [[SGMS2]] | 5 µM | C | SGMS2 activity lowers the cells' numbers under Everolimus 5 µM (makes them more sensitive) | lines that do not express SGMS2 (5) vs lines expressing it (43) | the lines without SGMS2: 1.20× the cells of the other lines | 0.083 | ⚠ tissue-confounded; across organs; also absent: IL15RA, RPH3AL; maybe low, not absent |
| [[PLPP1]] | 5 µM | C | PLPP1's natural level raises the cells' numbers under Everolimus 5 µM (protects the cells) | PLPP1's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.70 | 0.268 over the table, 0.049 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

### Its targets: what acting on them probably does

*Drug-target arrows of the compound classes it belongs to (compounds sharing a listed target and mechanism; one molecule counts once, under all its names): the target → a gene whose level those compounds move. A row that names several targets is one test: the compounds share them all, and any of them could be the cause. 93 arrows, 93 of them with an alert ⚠; grade A 0, B 93, C 0. Shown: the 15 strongest; 78 more arrows (78 of them with an alert ⚠) not shown.*

| Its target | Gene it moves | This drug | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|---|
| [[MTOR]] | [[INSR]] | does not move it that way (the class's other compounds do) | B | MTOR activity lowers INSR's level | compounds that target MTOR: 6 of 8 raise it (AZD-8055, Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 75% of the class's compounds vs 3.4% of all compounds | 0.004 | ⚠ off-target possible; 6 compounds; artifact flags |
| [[MTOR]] | [[FKBP14]] | does not move it that way (the class's other compounds do) | B | MTOR activity raises FKBP14's level | compounds that target MTOR: 6 of 8 lower it (AZD-8055, Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 75% of the class's compounds vs 4.2% of all compounds | 0.005 | ⚠ off-target possible; 6 compounds; artifact flags |
| [[MTOR]] | [[WASHC2C]] | does not move it that way (the class's other compounds do) | B | MTOR activity lowers WASHC2C's level | compounds that target MTOR: 6 of 8 raise it (AZD-8055, Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 75% of the class's compounds vs 5.0% of all compounds | 0.005 | ⚠ off-target possible; 6 compounds; artifact flags |
| [[MTOR]] | [[TSPAN13]] | does not move it that way (the class's other compounds do) | B | MTOR activity raises TSPAN13's level | compounds that target MTOR: 5 of 8 lower it (AZD-8055, Bimiralisib, Rapamycin, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 2.8% of all compounds | 0.006 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[MTOR]] | [[MCM8]] | does not move it that way (the class's other compounds do) | B | MTOR activity raises MCM8's level | compounds that target MTOR: 6 of 8 lower it (AZD-8055, Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 75% of the class's compounds vs 5.6% of all compounds | 0.007 | ⚠ off-target possible; 6 compounds; artifact flags |
| [[MTOR]] | [[WDR19]] | does not move it that way (the class's other compounds do) | B | MTOR activity lowers WDR19's level | compounds that target MTOR: 6 of 8 raise it (AZD-8055, Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 75% of the class's compounds vs 5.6% of all compounds | 0.007 | ⚠ off-target possible; 6 compounds; artifact flags |
| [[MTOR]] | [[CENPN]] | does not move it that way (the class's other compounds do) | B | MTOR activity raises CENPN's level | compounds that target MTOR: 5 of 8 lower it (AZD-8055, Bimiralisib, Rapamycin, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 3.1% of all compounds | 0.007 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[MTOR]] | [[DTL]] | does not move it that way (the class's other compounds do) | B | MTOR activity raises DTL's level | compounds that target MTOR: 6 of 8 lower it (AZD-8055, Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 75% of the class's compounds vs 6.2% of all compounds | 0.008 | ⚠ off-target possible; 6 compounds; artifact flags |
| [[MTOR]] | [[WDR62]] | does not move it that way (the class's other compounds do) | B | MTOR activity raises WDR62's level | compounds that target MTOR: 6 of 8 lower it (AZD-8055, Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 75% of the class's compounds vs 6.2% of all compounds | 0.008 | ⚠ off-target possible; 6 compounds; artifact flags |
| [[MTOR]] | [[MARS1]] | does not move it that way (the class's other compounds do) | B | MTOR activity raises MARS1's level | compounds that target MTOR: 5 of 8 lower it (AZD-8055, Bimiralisib, Rapamycin, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 3.4% of all compounds | 0.008 | ⚠ off-target possible; 5 compounds |
| [[MTOR]] | [[SMAP2]] | does not move it that way (the class's other compounds do) | B | MTOR activity raises SMAP2's level | compounds that target MTOR: 5 of 8 lower it (Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 3.4% of all compounds | 0.008 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[MTOR]] | [[ERICH1]] | does not move it that way (the class's other compounds do) | B | MTOR activity lowers ERICH1's level | compounds that target MTOR: 5 of 8 raise it (AZD-8055, Bimiralisib, Rapamycin, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 3.6% of all compounds | 0.010 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[MTOR]] | [[FBXO32]] | does not move it that way (the class's other compounds do) | B | MTOR activity lowers FBXO32's level | compounds that target MTOR: 6 of 8 raise it (AZD-8055, Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 75% of the class's compounds vs 7.3% of all compounds | 0.013 | ⚠ off-target possible; 6 compounds |
| [[MTOR]] | [[PDIA3]] | does not move it that way (the class's other compounds do) | B | MTOR activity raises PDIA3's level | compounds that target MTOR: 5 of 8 lower it (Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 3.9% of all compounds | 0.013 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[MTOR]] | [[YPEL1]] | does not move it that way (the class's other compounds do) | B | MTOR activity lowers YPEL1's level | compounds that target MTOR: 5 of 8 raise it (Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 3.9% of all compounds | 0.013 | ⚠ off-target possible; 5 compounds; artifact flags |

## Data

- `tables/drugs.parquet` — drug == "Everolimus"
- `tables/drugdoses.parquet` — dd in 435, 436, 437
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
