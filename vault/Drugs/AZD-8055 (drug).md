---
drug: "AZD-8055"
type: "drug"
salt_base: "AZD-8055"
targets: "MTOR"
moa_fine: "MTOR inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 156
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# AZD-8055

*MTOR inhibitor (inhibitor/antagonist) · targets: MTOR · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 27 / 115 / 156; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.33 / 0.64.
> Flags by dose: - / noisy plate (z scaled) / noisy plate (z scaled).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:B11 | 17 / 10 | — | +0.42 | -1.0/-0.1/-0.3 | — |
| 0.5 µM | [[Plate 02]]:B11 | 46 / 69 | — | +0.25 | -3.0/-1.2/-1.7 | noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:B11 | 104 / 52 | — | +0.70 | -1.5/-1.2/-1.9 | noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (17 genes, none with an alert; 12 shown): [[CFB]] 1.64× (z +4.0, 16/28 lines), [[SOX6]] 1.34× (z +3.7, 7/26 lines), [[GBP2]] 1.37× (z +3.4, 10/35 lines), [[KRT80]] 1.31× (z +3.3, 6/26 lines), [[PDIK1L]] 1.23× (z +3.2, 3/48 lines), [[TGFB2]] 1.23× (z +3.1, 9/33 lines), [[SEMA6A]] 1.25× (z +3.1, 2/28 lines), [[USP38-DT]] 1.42× (z +3.1, 4/44 lines), [[ARID5B]] 1.23× (z +3.1, 15/42 lines), [[ENSG00000132832]] 1.49× (z +3.1, 1/29 lines), [[FBN1]] 1.21× (z +2.9, 4/20 lines), [[NEBL]] 1.22× (z +2.8, 11/31 lines)

**0.5 µM** (46 genes, none with an alert; 12 shown): [[BACH2]] 1.35× (z +4.0, 11/41 lines), [[RPGR]] 1.31× (z +3.9, 14/48 lines), [[WDR19]] 1.38× (z +3.8, 18/48 lines), [[LYST]] 1.27× (z +3.7, 13/47 lines), [[USP2-AS1]] 1.40× (z +3.6, 9/47 lines), [[UTP25]] 1.24× (z +3.5, 3/48 lines), [[SOD2]] 1.50× (z +3.5, 21/45 lines), [[MAP3K5]] 1.27× (z +3.5, 16/45 lines), [[INSR]] 1.30× (z +3.4, 16/45 lines), [[GAB2]] 1.28× (z +3.3, 10/46 lines), [[TBC1D15]] 1.25× (z +3.3, 16/48 lines), [[ATP6V1C1]] 1.22× (z +3.3, 7/48 lines)

**5 µM** (104 genes, none with an alert; 12 shown): [[FOXN3]] 1.49× (z +4.9, 23/47 lines), [[JAK1]] 1.33× (z +4.1, 23/49 lines), [[SYNE2]] 1.59× (z +4.0, 28/48 lines), [[BCAS3]] 1.52× (z +4.0, 35/49 lines), [[ZC2HC1A]] 1.44× (z +4.0, 13/47 lines), [[INSR]] 1.48× (z +3.8, 22/46 lines), [[ENSG00000287042]] 1.89× (z +3.8, 18/45 lines), [[ATP9A]] 1.51× (z +3.8, 16/45 lines), [[FOXP1]] 1.59× (z +3.7, 29/45 lines), [[DHRSX]] 1.33× (z +3.6, 14/48 lines), [[MFSD6]] 1.41× (z +3.6, 8/46 lines), [[TFDP2]] 1.25× (z +3.6, 12/49 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (10 genes, none with an alert): [[ETV5]] 0.791× (z -3.8, 17/48 lines), [[CDC42BPG]] 0.734× (z -3.5, 7/27 lines), [[WT1]] 0.715× (z -3.4, 1/17 lines), [[SPRY4]] 0.764× (z -3.3, 13/48 lines), [[FOSL1]] 0.716× (z -3.1, 22/43 lines), [[B4GALT6]] 0.829× (z -3.1, 5/39 lines), [[EPHA2]] 0.814× (z -3.0, 11/37 lines), [[SPRED2]] 0.809× (z -3.0, 24/48 lines), [[RFC4]] 0.829× (z -2.9, 4/48 lines), [[LIF]] 0.781× (z -2.7, 8/38 lines)

**0.5 µM** (69 genes, none with an alert; 12 shown): [[CDC45]] 0.590× (z -4.9, 13/45 lines), [[MARS1]] 0.672× (z -4.9, 31/48 lines), [[CLSPN]] 0.477× (z -4.8, 29/44 lines), [[PSAT1]] 0.611× (z -4.5, 14/40 lines), [[DNMT1]] 0.691× (z -4.3, 24/48 lines), [[UHRF1]] 0.532× (z -4.3, 15/46 lines), [[WDR76]] 0.668× (z -4.2, 9/46 lines), [[E2F2]] 0.505× (z -4.2, 6/33 lines), [[ADGRL1]] 0.764× (z -4.1, 6/42 lines), [[CDC7]] 0.659× (z -4.1, 13/46 lines), [[WDHD1]] 0.753× (z -4.0, 17/48 lines), [[MYBL2]] 0.593× (z -4.0, 20/44 lines)

**5 µM** (52 genes, none with an alert; 12 shown): [[MARS1]] 0.559× (z -5.2, 36/49 lines), [[GPT2]] 0.548× (z -5.0, 24/46 lines), [[SRA1]] 0.552× (z -4.2, 26/48 lines), [[PSAT1]] 0.536× (z -3.8, 21/40 lines), [[CARS1]] 0.703× (z -3.8, 18/49 lines), [[C11orf24]] 0.606× (z -3.8, 11/47 lines), [[ASNS]] 0.576× (z -3.7, 19/45 lines), [[TSPAN13]] 0.672× (z -3.6, 11/36 lines), [[MTHFD2]] 0.625× (z -3.6, 23/49 lines), [[AK2]] 0.710× (z -3.5, 18/49 lines), [[TIGAR]] 0.641× (z -3.5, 7/47 lines), [[XPOT]] 0.727× (z -3.4, 13/49 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | [[Module 006]] (-2.2) |
| 5 µM | [[Module 230]] (+2.1) | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[AsPC-1 (line)]] (1.69), [[A549 (line)]] (1.56), [[MIA PaCa-2 (line)]] (1.55), [[Hs 766T (line)]] (1.47) · weakest: [[AN3 CA (line)]] (-0.0266), [[NCI-H661 (line)]] (0.124), [[RKO (line)]] (0.164) |
| 0.5 µM | — | [[Hs 766T (line)]] (1.99), [[H4 (line)]] (1.78), [[MIA PaCa-2 (line)]] (1.63), [[SW 1088 (line)]] (1.44) · weakest: [[SW1417 (line)]] (0.268), [[NCI-H661 (line)]] (0.434), [[CHP-212 (line)]] (0.462) |
| 5 µM | [[Panc 03.27 (line)]] (-4.2), [[LoVo (line)]] (-3.7), [[COLO 205 (line)]] (-3.0) | [[AsPC-1 (line)]] (1.49), [[Hs 766T (line)]] (1.31), [[HCT15 (line)]] (1.30), [[HEC-1-A (line)]] (1.30) · weakest: [[COLO 205 (line)]] (0.448), [[C32 (line)]] (0.611), [[SW1417 (line)]] (0.613) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[Bimiralisib (drug)]] (+0.79, PI3K/AKT inhibitor); [[IQ 1 (drug)]] (+0.76, unclear); [[MK-3903 (drug)]] (+0.73, unclear); [[Rapamycin (drug)]] (+0.63, MTOR inhibitor); [[Alpelisib (drug)]] (+0.61, PI3K/AKT inhibitor); [[Larotrectinib sulfate (drug)]] (+0.60, Other TK inhibitor, ⚠ no trustworthy dose (vector dose flagged: unreliable plate only)); [[Temsirolimus (drug)]] (+0.58, MTOR inhibitor); [[Resveratrol (drug)]] (+0.57, unclear); [[BI-3406 (drug)]] (+0.52, RAS inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[OTULINL]] | 5 µM | B | OTULINL activity raises the cells' numbers under AZD-8055 5 µM (protects the cells) | lines that do not express OTULINL (7) vs lines expressing it (41) | the lines without OTULINL: 0.76× the cells of the other lines | 0.082 | ⚠ within organs, on part of the lines; also absent: PLP2, LRFN4, C12orf75; maybe low, not absent |
| [[HMGA2]] | 5 µM | B | HMGA2 activity raises the cells' numbers under AZD-8055 5 µM (protects the cells) | lines that do not express HMGA2 (9) vs lines expressing it (39) | the lines without HMGA2: 0.88× the cells of the other lines | 0.094 | ⚠ within organs, on part of the lines; also absent: SEMA4G, LINC02454 |
| [[FIGN]] | 5 µM | C | FIGN activity raises the cells' numbers under AZD-8055 5 µM (protects the cells) | lines that do not express FIGN (16) vs lines expressing it (32) | the lines without FIGN: 0.82× the cells of the other lines | 0.082 | ⚠ tissue-confounded; across organs; also absent: SPART-AS1, CCDC169, SPART |
| [[SPART-AS1]] | 5 µM | C | SPART-AS1 activity raises the cells' numbers under AZD-8055 5 µM (protects the cells) | lines that do not express SPART-AS1 (16) vs lines expressing it (32) | the lines without SPART-AS1: 0.83× the cells of the other lines | 0.094 | ⚠ tissue-confounded; across organs; also absent: CCDC169, FIGN, SPART |

### Its targets: what acting on them probably does

*Drug-target arrows of the compound classes it belongs to (compounds sharing a listed target and mechanism; one molecule counts once, under all its names): the target → a gene whose level those compounds move. A row that names several targets is one test: the compounds share them all, and any of them could be the cause. 93 arrows, 93 of them with an alert ⚠; grade A 0, B 93, C 0. Shown: the 15 strongest; 78 more arrows (78 of them with an alert ⚠) not shown.*

| Its target | Gene it moves | This drug | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|---|
| [[MTOR]] | [[INSR]] | moves it that way too | B | MTOR activity lowers INSR's level | compounds that target MTOR: 6 of 8 raise it (AZD-8055, Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 75% of the class's compounds vs 3.4% of all compounds | 0.004 | ⚠ off-target possible; 6 compounds; artifact flags |
| [[MTOR]] | [[FKBP14]] | moves it that way too | B | MTOR activity raises FKBP14's level | compounds that target MTOR: 6 of 8 lower it (AZD-8055, Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 75% of the class's compounds vs 4.2% of all compounds | 0.005 | ⚠ off-target possible; 6 compounds; artifact flags |
| [[MTOR]] | [[WASHC2C]] | moves it that way too | B | MTOR activity lowers WASHC2C's level | compounds that target MTOR: 6 of 8 raise it (AZD-8055, Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 75% of the class's compounds vs 5.0% of all compounds | 0.005 | ⚠ off-target possible; 6 compounds; artifact flags |
| [[MTOR]] | [[TSPAN13]] | moves it that way too | B | MTOR activity raises TSPAN13's level | compounds that target MTOR: 5 of 8 lower it (AZD-8055, Bimiralisib, Rapamycin, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 2.8% of all compounds | 0.006 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[MTOR]] | [[MCM8]] | moves it that way too | B | MTOR activity raises MCM8's level | compounds that target MTOR: 6 of 8 lower it (AZD-8055, Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 75% of the class's compounds vs 5.6% of all compounds | 0.007 | ⚠ off-target possible; 6 compounds; artifact flags |
| [[MTOR]] | [[WDR19]] | moves it that way too | B | MTOR activity lowers WDR19's level | compounds that target MTOR: 6 of 8 raise it (AZD-8055, Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 75% of the class's compounds vs 5.6% of all compounds | 0.007 | ⚠ off-target possible; 6 compounds; artifact flags |
| [[MTOR]] | [[CENPN]] | moves it that way too | B | MTOR activity raises CENPN's level | compounds that target MTOR: 5 of 8 lower it (AZD-8055, Bimiralisib, Rapamycin, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 3.1% of all compounds | 0.007 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[MTOR]] | [[DTL]] | moves it that way too | B | MTOR activity raises DTL's level | compounds that target MTOR: 6 of 8 lower it (AZD-8055, Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 75% of the class's compounds vs 6.2% of all compounds | 0.008 | ⚠ off-target possible; 6 compounds; artifact flags |
| [[MTOR]] | [[WDR62]] | moves it that way too | B | MTOR activity raises WDR62's level | compounds that target MTOR: 6 of 8 lower it (AZD-8055, Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 75% of the class's compounds vs 6.2% of all compounds | 0.008 | ⚠ off-target possible; 6 compounds; artifact flags |
| [[MTOR]] | [[MARS1]] | moves it that way too | B | MTOR activity raises MARS1's level | compounds that target MTOR: 5 of 8 lower it (AZD-8055, Bimiralisib, Rapamycin, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 3.4% of all compounds | 0.008 | ⚠ off-target possible; 5 compounds |
| [[MTOR]] | [[SMAP2]] | does not move it that way (the class's other compounds do) | B | MTOR activity raises SMAP2's level | compounds that target MTOR: 5 of 8 lower it (Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 3.4% of all compounds | 0.008 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[MTOR]] | [[ERICH1]] | moves it that way too | B | MTOR activity lowers ERICH1's level | compounds that target MTOR: 5 of 8 raise it (AZD-8055, Bimiralisib, Rapamycin, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 3.6% of all compounds | 0.010 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[MTOR]] | [[FBXO32]] | moves it that way too | B | MTOR activity lowers FBXO32's level | compounds that target MTOR: 6 of 8 raise it (AZD-8055, Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 75% of the class's compounds vs 7.3% of all compounds | 0.013 | ⚠ off-target possible; 6 compounds |
| [[MTOR]] | [[PDIA3]] | does not move it that way (the class's other compounds do) | B | MTOR activity raises PDIA3's level | compounds that target MTOR: 5 of 8 lower it (Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 3.9% of all compounds | 0.013 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[MTOR]] | [[YPEL1]] | does not move it that way (the class's other compounds do) | B | MTOR activity lowers YPEL1's level | compounds that target MTOR: 5 of 8 raise it (Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 3.9% of all compounds | 0.013 | ⚠ off-target possible; 5 compounds; artifact flags |

## Data

- `tables/drugs.parquet` — drug == "AZD-8055"
- `tables/drugdoses.parquet` — dd in 33, 34, 35
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
