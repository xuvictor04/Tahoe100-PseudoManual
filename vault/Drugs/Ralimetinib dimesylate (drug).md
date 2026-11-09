---
drug: "Ralimetinib dimesylate"
type: "drug"
salt_base: "Ralimetinib dimesylate"
targets: "MAPKAPK2, MAPK14, MAPK11"
moa_fine: "Other MAPK inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "0.05"
max_sig_genes: 265
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Ralimetinib dimesylate

*Other MAPK inhibitor (inhibitor/antagonist) · targets: MAPKAPK2, MAPK14, MAPK11 · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 265 / 6 / 45; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): -0.44 / -0.27.
> Flags by dose: unreliable plate only / low cells (technical?); plate-row cell shift; noisy plate (z scaled) / plate-row cell shift; noisy plate (z scaled). ⚠ 0.05 µM: unreliable plate only (artifact flags: its changes there are shown with an alert, not left out).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 13]]:A3 | 150 / 115 | — | +0.13 | +0.2/-1.2/-2.3 | ⚠ unreliable plate only |
| 0.5 µM | [[Plate 02]]:D2 | 5 / 1 | — | -1.03 | +0.9/+0.3/+1.5 | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:D2 | 41 / 4 | — | +0.52 | +1.3/+0.6/-1.2 | plate-row cell shift; noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (150 genes, 150 with an alert ⚠; the drug-dose carries ⚠ unreliable plate only; 12 shown): [[MAP2K6]] ⚠ 2.07× (z +6.5, 18/26 lines), [[SMARCA2]] ⚠ 1.29× (z +5.3, 29/42 lines), [[QDPR]] ⚠ 1.29× (z +5.0, 13/47 lines), [[SORL1]] ⚠ 1.35× (z +4.8, 16/27 lines), [[SLC25A12]] ⚠ 1.25× (z +4.7, 17/48 lines), [[NRG2]] ⚠ 1.36× (z +4.7, 6/32 lines), [[ADAM22]] ⚠ 1.34× (z +4.7, 17/36 lines), [[TLN2]] ⚠ 1.34× (z +4.6, 15/43 lines), [[DTX4]] ⚠ 1.35× (z +4.4, 6/38 lines), [[MANBA]] ⚠ 1.25× (z +4.4, 27/48 lines), [[TRERF1]] ⚠ 1.26× (z +4.3, 21/42 lines), [[VPS26B]] ⚠ 1.24× (z +4.3, 8/48 lines)

**0.5 µM** (5 genes, none with an alert): [[ALAD]] 1.30× (z +3.1, 1/47 lines), [[ZHX1]] 1.21× (z +3.0, 4/48 lines), [[TAPBPL]] 1.34× (z +2.8, 1/41 lines), [[ENSG00000287172]] 1.84× (z +2.8, 0/3 lines), [[HSPA1A]] 2.00× (z +2.7, 13/35 lines)

**5 µM** (41 genes, none with an alert; 12 shown): [[MAP2K6]] 3.35× (z +5.6, 17/24 lines), [[CREB5]] 1.70× (z +4.9, 19/33 lines), [[EEF2K]] 1.48× (z +4.8, 15/48 lines), [[TRERF1]] 1.62× (z +4.6, 26/42 lines), [[CAMK2G]] 1.38× (z +4.3, 14/48 lines), [[SMARCA2]] 1.44× (z +4.0, 20/42 lines), [[FAM102B]] 1.49× (z +3.8, 8/46 lines), [[ACACB]] 1.75× (z +3.8, 9/47 lines), [[NFIA]] 1.44× (z +3.7, 17/37 lines), [[MMS22L]] 1.55× (z +3.7, 10/48 lines), [[NRG2]] 1.57× (z +3.6, 7/33 lines), [[TM7SF3]] 1.34× (z +3.6, 4/48 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (115 genes, 115 with an alert ⚠; the drug-dose carries ⚠ unreliable plate only; 12 shown): [[UBE2J2]] ⚠ 0.775× (z -5.6, 25/48 lines), [[PTGS2]] ⚠ 0.675× (z -4.6, 10/21 lines), [[ZFP36L1]] ⚠ 0.682× (z -4.5, 40/46 lines), [[IL11]] ⚠ 0.573× (z -4.3, 12/21 lines), [[ENSG00000276900]] ⚠ 0.582× (z -4.3, 18/39 lines), [[IER3]] ⚠ 0.551× (z -4.3, 41/43 lines), [[RNASEK]] ⚠ 0.617× (z -4.1, 41/48 lines), [[CXCL8]] ⚠ 0.633× (z -4.0, 20/28 lines), [[STC1]] ⚠ 0.652× (z -4.0, 20/24 lines), [[GNG5]] ⚠ 0.731× (z -3.9, 29/48 lines), [[TUBA1C]] ⚠ 0.732× (z -3.8, 32/48 lines), [[IFITM1]] ⚠ 0.532× (z -3.8, 25/29 lines)

**0.5 µM** (1 gene, none with an alert): [[FHIP1B]] 0.719× (z -3.1, 16/47 lines)

**5 µM** (4 genes, none with an alert): [[PRDM1]] 0.615× (z -3.7, 8/33 lines), [[MIR22HG]] 0.533× (z -3.6, 15/47 lines), [[ZSWIM8]] 0.664× (z -3.2, 7/48 lines), [[TP53INP2]] 0.641× (z -3.0, 8/45 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 146]] (+3.0), [[Module 171]] (+2.8), [[Module 025]] (+2.3) | [[Module 048]] (-3.5), [[Module 160]] (-2.4) |
| 0.5 µM | — | — |
| 5 µM | [[Module 006]] (+2.4) | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[NCI-H1573 (line)]] (1.30), [[SW 900 (line)]] (1.24), [[NCI-H1792 (line)]] (1.23), [[CFPAC-1 (line)]] (1.17) · weakest: [[NCI-H661 (line)]] (0.683), [[SHP-77 (line)]] (0.780), [[NCI-H2347 (line)]] (0.802) |
| 0.5 µM | — | — |
| 5 µM | [[J82 (line)]] (-3.2) | [[NCI-H1792 (line)]] (1.47), [[SW 900 (line)]] (1.39), [[A549 (line)]] (1.32), [[SNU-1 (line)]] (1.32) · weakest: [[NCI-H2347 (line)]] (0.232), [[HEC-1-A (line)]] (0.431), [[SW48 (line)]] (0.445) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[Bentamapimod (drug)]] (+0.73, Other MAPK inhibitor); [[MK-8353 (drug)]] (+0.69, Other MAPK inhibitor); [[Tucatinib (drug)]] (+0.57, EGFR/ERBB inhibitor); [[Flumatinib (mesylate) (drug)]] (+0.56, Other TK inhibitor); [[Berberine (chloride hydrate) (drug)]] (+0.49, unclear); [[Temuterkib (drug)]] (+0.49, Other MAPK inhibitor, ⚠ only 3 significant genes); [[Regorafenib (drug)]] (+0.48, Multi-TK inhibitor); [[Pyridoxine (hydrochloride) (drug)]] (+0.47, unclear); [[Rutin (trihydrate) (drug)]] (+0.46, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 12 arrows, 12 of them with an alert ⚠; grade A 0, B 9, C 3.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[AHR]] | 5 µM | B | AHR activity raises the cells' numbers under Ralimetinib dimesylate 5 µM (protects the cells) | lines that do not express AHR (7) vs lines expressing it (41) | the lines without AHR: 0.82× the cells of the other lines | 0.036 | ⚠ within organs, on part of the lines; also absent: ENSG00000283321, VDR, GPR39 |
| [[NIPAL1]] | 5 µM | B | NIPAL1 activity raises the cells' numbers under Ralimetinib dimesylate 5 µM (protects the cells) | lines that do not express NIPAL1 (5) vs lines expressing it (43) | the lines without NIPAL1: 0.78× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: SLC18B1, AHR, RALGPS2; maybe low, not absent |
| [[KLRK1-AS1]] | 5 µM | B | KLRK1-AS1 activity raises the cells' numbers under Ralimetinib dimesylate 5 µM (protects the cells) | lines that do not express KLRK1-AS1 (11) vs lines expressing it (37) | the lines without KLRK1-AS1: 0.85× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: BACH2; maybe low, not absent |
| [[AQP3]] | 5 µM | B | AQP3 activity raises the cells' numbers under Ralimetinib dimesylate 5 µM (protects the cells) | lines that do not express AQP3 (19) vs lines expressing it (29) | the lines without AQP3: 0.85× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; also absent: ABCC3, ELF3, CD24; maybe low, not absent |
| [[SLC2A9]] | 5 µM | B | SLC2A9 activity raises the cells' numbers under Ralimetinib dimesylate 5 µM (protects the cells) | lines that do not express SLC2A9 (6) vs lines expressing it (42) | the lines without SLC2A9: 0.78× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; also absent: VDR, SEMA4G, TBC1D8B; maybe low, not absent |
| [[ENSG00000284686]] | 5 µM | B | ENSG00000284686 activity raises the cells' numbers under Ralimetinib dimesylate 5 µM (protects the cells) | lines that do not express ENSG00000284686 (8) vs lines expressing it (40) | the lines without ENSG00000284686: 0.83× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: ENSG00000258989, PLPP3, PRKCH; maybe low, not absent |
| [[TREM1]] | 5 µM | B | TREM1 activity raises the cells' numbers under Ralimetinib dimesylate 5 µM (protects the cells) | lines that do not express TREM1 (25) vs lines expressing it (23) | the lines without TREM1: 0.87× the cells of the other lines | 0.094 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, DTNA, MAF |
| [[RASGEF1B]] | 5 µM | B | RASGEF1B activity raises the cells' numbers under Ralimetinib dimesylate 5 µM (protects the cells) | lines that do not express RASGEF1B (10) vs lines expressing it (38) | the lines without RASGEF1B: 0.82× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: FBXW10B; maybe low, not absent |
| [[PPP1R1C]] | 5 µM | B | PPP1R1C activity raises the cells' numbers under Ralimetinib dimesylate 5 µM (protects the cells) | lines that do not express PPP1R1C (13) vs lines expressing it (35) | the lines without PPP1R1C: 0.82× the cells of the other lines | 0.099 | ⚠ within organs, on part of the lines; also absent: ENSG00000261227, LINC01239, ADGRL4; maybe low, not absent |
| [[SEMA4G]] | 5 µM | C | SEMA4G activity raises the cells' numbers under Ralimetinib dimesylate 5 µM (protects the cells) | lines that do not express SEMA4G (6) vs lines expressing it (42) | the lines without SEMA4G: 0.77× the cells of the other lines | 0.041 | ⚠ tissue-confounded; across organs; also absent: SLC2A9, HMGA2; maybe low, not absent |
| [[ENSG00000288755]] | 5 µM | C | ENSG00000288755 activity raises the cells' numbers under Ralimetinib dimesylate 5 µM (protects the cells) | lines that do not express ENSG00000288755 (3) vs lines expressing it (45) | the lines without ENSG00000288755: 0.70× the cells of the other lines | 0.043 | ⚠ few lines (3 vs 47); across organs; also absent: SLC25A45; maybe low, not absent |
| [[SLC25A45]] | 5 µM | C | SLC25A45 activity raises the cells' numbers under Ralimetinib dimesylate 5 µM (protects the cells) | lines that do not express SLC25A45 (3) vs lines expressing it (45) | the lines without SLC25A45: 0.73× the cells of the other lines | 0.082 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; co-occurs with WNK2; also absent: CASP8, SP100, PRRG1; maybe low, not absent |

### Its targets: what acting on them probably does

*Drug-target arrows of the compound classes it belongs to (compounds sharing a listed target and mechanism; one molecule counts once, under all its names): the target → a gene whose level those compounds move. A row that names several targets is one test: the compounds share them all, and any of them could be the cause. 5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Its target | Gene it moves | This drug | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|---|
| [[MAPK14]] | [[ESRRA]] | moves it that way too | B | MAPK14 activity raises ESRRA's level | compounds that target MAPK14: 2 of 2 lower it (PH-797804, Ralimetinib dimesylate) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[MAPK14]] | [[DLGAP1]] | moves it that way too | B | MAPK14 activity raises DLGAP1's level | compounds that target MAPK14: 2 of 2 lower it (PH-797804, Ralimetinib dimesylate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[MAPK14]] | [[TSFM]] | moves it that way too | B | MAPK14 activity lowers TSFM's level | compounds that target MAPK14: 2 of 2 raise it (PH-797804, Ralimetinib dimesylate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[MAPK14]] | [[NFATC2IP]] | moves it that way too | B | MAPK14 activity raises NFATC2IP's level | compounds that target MAPK14: 2 of 2 lower it (PH-797804, Ralimetinib dimesylate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[MAPK14]] | [[TSEN34]] | moves it that way too | B | MAPK14 activity raises TSEN34's level | compounds that target MAPK14: 2 of 2 lower it (PH-797804, Ralimetinib dimesylate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

## Data

- `tables/drugs.parquet` — drug == "Ralimetinib dimesylate"
- `tables/drugdoses.parquet` — dd in 866, 867, 868
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
