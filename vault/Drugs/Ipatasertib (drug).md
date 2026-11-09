---
drug: "Ipatasertib"
type: "drug"
salt_base: "Ipatasertib"
targets: "AKT1, AKT2, AKT3"
moa_fine: "PI3K/AKT inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 2158
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Ipatasertib

*PI3K/AKT inhibitor (inhibitor/antagonist) · targets: AKT1, AKT2, AKT3 · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 62 / 2158 / 157; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.26 / -0.50.
> Flags by dose: - / low cells (technical?); plate-row cell shift; noisy plate (z scaled) / plate-row cell shift; noisy plate (z scaled).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:D6 | 40 / 22 | — | -0.28 | +1.1/+0.8/+0.7 | — |
| 0.5 µM | [[Plate 02]]:D6 | 1,742 / 416 | — | -1.23 | -1.1/-1.5/+0.8 | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:D6 | 72 / 85 | — | +1.39 | +0.4/+0.2/-1.4 | plate-row cell shift; noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (40 genes, none with an alert; 12 shown): [[TRERF1]] 1.30× (z +4.5, 23/42 lines), [[CAMK2G]] 1.21× (z +4.4, 16/48 lines), [[PRR12]] 1.30× (z +4.3, 18/48 lines), [[CYP2S1]] 1.54× (z +4.3, 15/28 lines), [[SRPX]] 1.33× (z +4.2, 8/25 lines), [[EEF2K]] 1.21× (z +4.1, 14/48 lines), [[SORL1]] 1.31× (z +4.0, 7/27 lines), [[EXTL2]] 1.30× (z +3.9, 7/48 lines), [[PORCN]] 1.42× (z +3.8, 6/37 lines), [[PIP4P2]] 1.32× (z +3.8, 15/44 lines), [[ADGRE5]] 1.30× (z +3.8, 13/41 lines), [[SEPTIN6]] 1.25× (z +3.7, 14/47 lines)

**0.5 µM** (1742 genes, none with an alert; 12 shown): [[RILPL1]] 1.51× (z +6.6, 34/46 lines), [[KIF1A]] 2.07× (z +6.6, 0/13 lines), [[SGPP2]] 1.73× (z +6.4, 1/16 lines), [[ENGASE]] 2.09× (z +6.4, 29/40 lines), [[ACAP3]] 1.96× (z +6.2, 29/43 lines), [[IGF2]] 3.26× (z +6.2, 9/16 lines), [[ZNF316]] 2.02× (z +6.2, 37/45 lines), [[RFLNA]] 1.39× (z +6.1, 36/48 lines), [[TAF6L]] 1.74× (z +6.1, 12/35 lines), [[ITGB6]] 1.74× (z +6.1, 0/16 lines), [[KIFC3]] 1.55× (z +6.1, 27/44 lines), [[ZCCHC3]] 2.26× (z +6.1, 30/42 lines)

**5 µM** (72 genes, none with an alert; 12 shown): [[MAP2K6]] 3.85× (z +6.3, 19/25 lines), [[TRERF1]] 1.75× (z +5.3, 27/42 lines), [[EEF2K]] 1.53× (z +5.1, 19/48 lines), [[NFIA]] 1.64× (z +5.0, 24/37 lines), [[PIP4P2]] 1.64× (z +4.4, 14/44 lines), [[PAPSS1]] 1.35× (z +4.2, 11/48 lines), [[NRG2]] 1.67× (z +4.1, 8/33 lines), [[RAVER2]] 1.47× (z +4.0, 11/46 lines), [[CAMK2G]] 1.35× (z +4.0, 8/48 lines), [[STAMBPL1]] 1.80× (z +3.9, 17/42 lines), [[TM7SF3]] 1.37× (z +3.9, 13/48 lines), [[MIDEAS]] 1.65× (z +3.9, 33/48 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (22 genes, none with an alert; 12 shown): [[DUSP16]] 0.816× (z -4.3, 21/46 lines), [[STEAP1B]] 0.725× (z -4.1, 17/47 lines), [[ENSG00000285080]] 0.613× (z -4.0, 20/46 lines), [[SLC7A9]] 0.601× (z -4.0, 15/37 lines), [[ENSG00000237550]] 0.596× (z -3.9, 21/43 lines), [[PFKFB2]] 0.801× (z -3.6, 11/46 lines), [[H2BC11]] 0.673× (z -3.6, 9/43 lines), [[HDX]] 0.753× (z -3.5, 15/32 lines), [[ZNF140]] 0.802× (z -3.5, 16/43 lines), [[ZNF613]] 0.709× (z -3.5, 11/36 lines), [[FAM81A]] 0.823× (z -3.3, 11/48 lines), [[VPS35L]] 0.830× (z -3.3, 6/39 lines)

**0.5 µM** (416 genes, none with an alert; 12 shown): [[ZBTB41]] 0.657× (z -6.5, 39/48 lines), [[RIF1]] 0.712× (z -6.5, 42/48 lines), [[ZHX1]] 0.669× (z -6.3, 26/46 lines), [[TWF1]] 0.519× (z -6.1, 42/48 lines), [[TMTC3]] 0.706× (z -6.0, 28/48 lines), [[STAG2]] 0.736× (z -5.9, 36/48 lines), [[TMEM106B]] 0.643× (z -5.8, 35/48 lines), [[TMX1]] 0.628× (z -5.8, 33/48 lines), [[ZNF8]] 0.619× (z -5.8, 16/46 lines), [[RO60]] 0.796× (z -5.8, 29/48 lines), [[DSP]] 0.643× (z -5.7, 26/31 lines), [[BIRC3]] 0.626× (z -5.7, 32/43 lines)

**5 µM** (85 genes, none with an alert; 12 shown): [[PTGS2]] 0.449× (z -5.0, 10/21 lines), [[ZNFX1]] 0.608× (z -4.8, 33/48 lines), [[DUSP16]] 0.687× (z -4.3, 16/46 lines), [[IFIH1]] 0.550× (z -4.2, 26/45 lines), [[SGPP2]] 0.614× (z -4.2, 1/16 lines), [[DNAH17]] 0.559× (z -3.9, 10/33 lines), [[SLC28A3]] 0.406× (z -3.9, 3/14 lines), [[ENSG00000230647]] 0.513× (z -3.8, 6/23 lines), [[CXCL1]] 0.368× (z -3.8, 19/31 lines), [[INHBA]] 0.434× (z -3.8, 11/16 lines), [[CXCL2]] 0.365× (z -3.7, 14/34 lines), [[CXCL8]] 0.368× (z -3.7, 21/28 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 045]] (+2.2) | — |
| 0.5 µM | [[Module 002]] (+4.2), [[Module 003]] (+3.8), [[Module 059]] (+3.6) | [[Module 029]] (-4.7), [[Module 025]] (-4.6), [[Module 194]] (-3.6) |
| 5 µM | — | [[Module 048]] (-2.0) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[A549 (line)]] (1.49), [[COLO 205 (line)]] (1.47), [[NCI-H661 (line)]] (1.42), [[HepG2_C3A (line)]] (1.40) · weakest: [[SW 1271 (line)]] (0.497), [[HEC-1-A (line)]] (0.612), [[SNU-1 (line)]] (0.643) |
| 0.5 µM | [[HCT15 (line)]] (-8.3), [[COLO 205 (line)]] (-6.2), [[RPMI-7951 (line)]] (-5.9), [[hTERT-HPNE (line)]] (-5.9), [[SW480 (line)]] (-5.4) | [[SW 1271 (line)]] (1.64), [[SW 1088 (line)]] (1.63), [[SNU-1 (line)]] (1.47), [[AN3 CA (line)]] (1.40) · weakest: [[NCI-H2347 (line)]] (0.667), [[SW1417 (line)]] (0.676), [[NCI-H1573 (line)]] (0.680) |
| 5 µM | [[J82 (line)]] (-3.1) | [[A549 (line)]] (1.39), [[CHP-212 (line)]] (1.35), [[SW 900 (line)]] (1.34), [[SNU-1 (line)]] (1.34) · weakest: [[NCI-H460 (line)]] (0.670), [[SHP-77 (line)]] (0.694), [[A-427 (line)]] (0.717) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Celecoxib (drug)]] (+0.89, Cyclooxygenase inhibitor); [[Thymol (drug)]] (+0.89, unclear); [[Methylprednisolone succinate (drug)]] (+0.87, Glucocorticoid receptor agonist); [[Nimesulide (drug)]] (+0.84, Cyclooxygenase inhibitor, ⚠ no trustworthy dose (vector dose flagged: toxic; unreliable plate only)); [[Darolutamide (drug)]] (+0.81, Androgen receptor antagonist, ⚠ only 5 significant genes); [[Bimatoprost (drug)]] (+0.76, unclear); [[Erythromycin (drug)]] (+0.76, unclear); [[9-ING-41 (drug)]] (+0.76, GSK3 inhibitor); [[Hydroxyurea (drug)]] (+0.75, DNA synthesis/repair inhibitor); [[Bergenin (drug)]] (+0.74, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[HS3ST3B1]] | 0.5 µM | B | HS3ST3B1 activity lowers the cells' numbers under Ipatasertib 0.5 µM (makes them more sensitive) | lines that do not express HS3ST3B1 (18) vs lines expressing it (30) | the lines without HS3ST3B1: 1.30× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: ENSG00000230647, SRPX, APCDD1L-DT |
| [[ADGRV1]] | 0.5 µM | B | ADGRV1 activity lowers the cells' numbers under Ipatasertib 0.5 µM (makes them more sensitive) | lines that do not express ADGRV1 (16) vs lines expressing it (32) | the lines without ADGRV1: 1.43× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: FRY, PPFIA2, EPHA3; maybe low, not absent |
| [[ABCC2]] | 5 µM | B | ABCC2 activity raises the cells' numbers under Ipatasertib 5 µM (protects the cells) | lines that do not express ABCC2 (22) vs lines expressing it (26) | the lines without ABCC2: 0.89× the cells of the other lines | 0.096 | ⚠ within organs, on part of the lines; also absent: ENSG00000230647, NR0B1, DNAJC12; maybe low, not absent |
| [[CRYZL2P]] | 0.5 µM | B | CRYZL2P activity raises the cells' numbers under Ipatasertib 0.5 µM (protects the cells) | lines that do not express CRYZL2P (14) vs lines expressing it (34) | the lines without CRYZL2P: 0.66× the cells of the other lines | 0.0995 | ⚠ within organs, on part of the lines; also absent: SEC16B |
| [[ENO2]] | 5 µM | C | ENO2 activity raises the cells' numbers under Ipatasertib 5 µM (protects the cells) | lines that do not express ENO2 (3) vs lines expressing it (45) | the lines without ENO2: 0.69× the cells of the other lines | 0.028 | ⚠ few lines (3 vs 47); across organs; also absent: NMB |
| [[UBOX5-AS1]] | 0.5 µM | C | UBOX5-AS1's natural level lowers the cells' numbers under Ipatasertib 0.5 µM (makes them more sensitive) | UBOX5-AS1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.68 | 0.285 over the table, 0.083 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

### Its targets: what acting on them probably does

*Drug-target arrows of the compound classes it belongs to (compounds sharing a listed target and mechanism; one molecule counts once, under all its names): the target → a gene whose level those compounds move. A row that names several targets is one test: the compounds share them all, and any of them could be the cause. 5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Its target | Gene it moves | This drug | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|---|
| [[AKT1]], [[AKT2]], [[AKT3]] | [[MMGT1]] | moves it that way too | B | AKT1, AKT2, AKT3 activity raises MMGT1's level | compounds that target AKT1, AKT2, AKT3: 2 of 3 lower it (BAY1125976, Ipatasertib) | 67% of the class's compounds vs 0.6% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; shared targets |
| [[AKT1]], [[AKT2]], [[AKT3]] | [[GTF3C4]] | moves it that way too | B | AKT1, AKT2, AKT3 activity raises GTF3C4's level | compounds that target AKT1, AKT2, AKT3: 2 of 3 lower it (BAY1125976, Ipatasertib) | 67% of the class's compounds vs 0.8% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets |
| [[AKT1]], [[AKT2]], [[AKT3]] | [[HSPA13]] | moves it that way too | B | AKT1, AKT2, AKT3 activity raises HSPA13's level | compounds that target AKT1, AKT2, AKT3: 2 of 3 lower it (BAY1125976, Ipatasertib) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets |
| [[AKT1]], [[AKT2]], [[AKT3]] | [[TWF1]] | moves it that way too | B | AKT1, AKT2, AKT3 activity raises TWF1's level | compounds that target AKT1, AKT2, AKT3: 2 of 3 lower it (BAY1125976, Ipatasertib) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets |
| [[AKT1]], [[AKT2]], [[AKT3]] | [[ZHX1]] | moves it that way too | B | AKT1, AKT2, AKT3 activity raises ZHX1's level | compounds that target AKT1, AKT2, AKT3: 2 of 3 lower it (BAY1125976, Ipatasertib) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets |

## Data

- `tables/drugs.parquet` — drug == "Ipatasertib"
- `tables/drugdoses.parquet` — dd in 558, 559, 560
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
