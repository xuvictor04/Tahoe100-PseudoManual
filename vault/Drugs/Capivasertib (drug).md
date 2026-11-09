---
drug: "Capivasertib"
type: "drug"
salt_base: "Capivasertib"
targets: "AKT1, AKT2, AKT3, RPS6KB1, PRKACA, ROCK2, ROCK1"
moa_fine: "PI3K/AKT inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 5
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Capivasertib

*PI3K/AKT inhibitor (inhibitor/antagonist) · targets: AKT1, AKT2, AKT3, RPS6KB1, PRKACA, ROCK2, ROCK1 · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 0 / 5 / 3; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): none.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.10 / -0.46.
> Flags by dose: - / noisy plate (z scaled) / noisy plate (z scaled).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:A6 | 0 / 0 | — | +0.06 | -0.0/+0.1/+0.3 | — |
| 0.5 µM | [[Plate 02]]:A6 | 3 / 2 | — | +0.40 | -1.0/-1.1/-1.4 | noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:A6 | 1 / 2 | — | -0.39 | +1.2/+1.1/+0.9 | noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (3 genes, none with an alert): [[ACVR2A]] 1.22× (z +2.9, 4/48 lines), [[NPTN]] 1.25× (z +2.9, 13/48 lines), [[PELI1]] 1.26× (z +2.8, 0/44 lines)

**5 µM** (1 gene, none with an alert): [[TEX30]] 1.52× (z +2.9, 1/37 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (2 genes, none with an alert): [[LINC01605]] 0.684× (z -3.0, 0/21 lines), [[ENSG00000289161]] 0.619× (z -2.9, 3/39 lines)

**5 µM** (2 genes, none with an alert): [[GUSBP18]] 0.663× (z -3.6, 18/45 lines), [[ENSG00000271204]] 0.714× (z -2.9, 15/41 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | [[Module 179]] (+2.7) | — |
| 5 µM | — | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[SW 1271 (line)]] (-3.2) | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: only 5 significant genes. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[NVP-BHG712 (drug)]] (+0.83, unclear); [[Goserelin (acetate) (drug)]] (+0.78, unclear); [[Tomivosertib (drug)]] (+0.72, Protein synthesis inhibitor); [[Gallic acid (drug)]] (+0.70, Cyclooxygenase inhibitor); [[Asciminib (drug)]] (+0.69, Other TK inhibitor); [[Acetazolamide (drug)]] (+0.67, unclear, ⚠ only 3 significant genes); [[Indacaterol (maleate) (drug)]] (+0.66, Adrenoceptor agonist, ⚠ only 3 significant genes); [[Captopril (drug)]] (+0.63, unclear); [[Hexylresorcinol (drug)]] (+0.62, unclear); [[Pravastatin (sodium) (drug)]] (+0.61, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[ZBED9]] | 5 µM | B | ZBED9 activity raises the cells' numbers under Capivasertib 5 µM (protects the cells) | lines that do not express ZBED9 (14) vs lines expressing it (34) | the lines without ZBED9: 0.91× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: TDRP, ZNF583, POPDC3 |
| [[OSBPL10]] | 5 µM | B | OSBPL10 activity raises the cells' numbers under Capivasertib 5 µM (protects the cells) | lines that do not express OSBPL10 (5) vs lines expressing it (43) | the lines without OSBPL10: 0.78× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: MORC4, USP53, CTNNA3; maybe low, not absent |
| [[GXYLT2]] | 5 µM | B | GXYLT2 activity lowers the cells' numbers under Capivasertib 5 µM (makes them more sensitive) | lines that do not express GXYLT2 (11) vs lines expressing it (37) | the lines without GXYLT2: 1.19× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: TMEM145, SLC17A7, FAM171B |
| [[CCSER1]] | 5 µM | B | CCSER1 activity raises the cells' numbers under Capivasertib 5 µM (protects the cells) | lines that do not express CCSER1 (20) vs lines expressing it (28) | the lines without CCSER1: 0.85× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: TSTD1, UGT8, HOOK1 |

### Its targets: what acting on them probably does

*Drug-target arrows of the compound classes it belongs to (compounds sharing a listed target and mechanism; one molecule counts once, under all its names): the target → a gene whose level those compounds move. A row that names several targets is one test: the compounds share them all, and any of them could be the cause. 5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Its target | Gene it moves | This drug | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|---|
| [[AKT1]], [[AKT2]], [[AKT3]] | [[MMGT1]] | does not move it that way (the class's other compounds do) | B | AKT1, AKT2, AKT3 activity raises MMGT1's level | compounds that target AKT1, AKT2, AKT3: 2 of 3 lower it (BAY1125976, Ipatasertib) | 67% of the class's compounds vs 0.6% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; shared targets |
| [[AKT1]], [[AKT2]], [[AKT3]] | [[GTF3C4]] | does not move it that way (the class's other compounds do) | B | AKT1, AKT2, AKT3 activity raises GTF3C4's level | compounds that target AKT1, AKT2, AKT3: 2 of 3 lower it (BAY1125976, Ipatasertib) | 67% of the class's compounds vs 0.8% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets |
| [[AKT1]], [[AKT2]], [[AKT3]] | [[HSPA13]] | does not move it that way (the class's other compounds do) | B | AKT1, AKT2, AKT3 activity raises HSPA13's level | compounds that target AKT1, AKT2, AKT3: 2 of 3 lower it (BAY1125976, Ipatasertib) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets |
| [[AKT1]], [[AKT2]], [[AKT3]] | [[TWF1]] | does not move it that way (the class's other compounds do) | B | AKT1, AKT2, AKT3 activity raises TWF1's level | compounds that target AKT1, AKT2, AKT3: 2 of 3 lower it (BAY1125976, Ipatasertib) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets |
| [[AKT1]], [[AKT2]], [[AKT3]] | [[ZHX1]] | does not move it that way (the class's other compounds do) | B | AKT1, AKT2, AKT3 activity raises ZHX1's level | compounds that target AKT1, AKT2, AKT3: 2 of 3 lower it (BAY1125976, Ipatasertib) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets |

## Data

- `tables/drugs.parquet` — drug == "Capivasertib"
- `tables/drugdoses.parquet` — dd in 236, 237, 238
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
