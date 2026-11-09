---
drug: "Temsirolimus"
type: "drug"
salt_base: "Temsirolimus"
targets: "MTOR"
moa_fine: "MTOR inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 429
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Temsirolimus

*MTOR inhibitor (inhibitor/antagonist) · targets: MTOR · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 352 / 429 / 68; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.45 / 0.57.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:B8 | 144 / 208 | — | +0.27 | -1.0/-0.4/-0.7 | — |
| 0.5 µM | [[Plate 05]]:B8 | 308 / 121 | — | -0.98 | -3.7/-2.1/-1.2 | — |
| 5 µM | [[Plate 14]]:B8 | 33 / 35 | 0.877 | +0.03 | -4.1/-3.2/-1.3 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (144 genes, none with an alert; 12 shown): [[ABRAXAS1]] 1.33× (z +4.7, 9/48 lines), [[PMEPA1]] 1.31× (z +4.6, 25/43 lines), [[WASHC2A]] 1.24× (z +4.6, 11/48 lines), [[INSR]] 1.28× (z +4.6, 27/46 lines), [[LINC00342]] 1.43× (z +4.5, 32/49 lines), [[GUSBP11]] 1.34× (z +4.5, 26/48 lines), [[KLHL5]] 1.27× (z +4.5, 19/42 lines), [[EPHB2]] 1.23× (z +4.4, 14/41 lines), [[WASHC2C]] 1.25× (z +4.3, 12/47 lines), [[DPH6]] 1.44× (z +4.2, 25/48 lines), [[VPS35L]] 1.25× (z +4.1, 10/39 lines), [[HSPBAP1]] 1.30× (z +4.1, 13/47 lines)

**0.5 µM** (308 genes, none with an alert; 12 shown): [[ATXN7L3-AS1]] 1.63× (z +5.4, 5/27 lines), [[CLCN7]] 1.47× (z +5.1, 26/45 lines), [[KLHL24]] 1.37× (z +5.1, 28/48 lines), [[ING4]] 1.31× (z +5.1, 15/46 lines), [[PMEPA1]] 1.34× (z +4.9, 25/42 lines), [[GTF2IP4]] 1.51× (z +4.9, 8/33 lines), [[HSPBAP1]] 1.36× (z +4.8, 15/44 lines), [[ENSG00000260710]] 1.80× (z +4.8, 3/12 lines), [[SLC25A53]] 1.21× (z +4.7, 13/46 lines), [[WASH2P-1]] 1.67× (z +4.7, 9/34 lines), [[WASHC2A]] 1.25× (z +4.7, 18/46 lines), [[INO80B]] 1.40× (z +4.7, 21/44 lines)

**5 µM** (33 genes, none with an alert; 12 shown): [[KLHL24]] 1.25× (z +4.8, 31/49 lines), [[REPS2]] 1.24× (z +4.6, 14/36 lines), [[PKD1L2]] 1.36× (z +4.3, 12/32 lines), [[RRAGC-DT]] 1.28× (z +4.3, 19/48 lines), [[CREBRF]] 1.20× (z +4.1, 25/49 lines), [[RNF103-CHMP3]] 1.31× (z +4.1, 17/44 lines), [[ZNF345]] 1.22× (z +4.1, 8/35 lines), [[LINC02154]] 1.37× (z +3.8, 9/11 lines), [[DYRK1B]] 1.22× (z +3.8, 5/36 lines), [[ENSG00000260729]] 1.26× (z +3.7, 20/46 lines), [[CRYM]] 1.30× (z +3.7, 12/36 lines), [[ENSG00000237596]] 1.26× (z +3.6, 11/35 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (208 genes, none with an alert; 12 shown): [[PSAT1]] 0.631× (z -5.9, 24/40 lines), [[MSMO1]] 0.610× (z -5.3, 34/48 lines), [[HMGCR]] 0.693× (z -5.3, 36/48 lines), [[ASNS]] 0.639× (z -5.1, 29/45 lines), [[NFXL1]] 0.737× (z -4.9, 32/49 lines), [[TUBE1]] 0.607× (z -4.9, 34/48 lines), [[STARD4]] 0.659× (z -4.9, 30/45 lines), [[SEC24D]] 0.692× (z -4.7, 30/49 lines), [[INSIG1]] 0.623× (z -4.7, 35/48 lines), [[HMGCS1]] 0.686× (z -4.7, 36/48 lines), [[GPT2]] 0.747× (z -4.6, 25/46 lines), [[PREPL]] 0.752× (z -4.6, 32/49 lines)

**0.5 µM** (121 genes, none with an alert; 12 shown): [[PHGDH]] 0.585× (z -6.5, 31/42 lines), [[ATAD1]] 0.830× (z -6.2, 22/44 lines), [[PSAT1]] 0.634× (z -5.8, 26/38 lines), [[MARS1]] 0.723× (z -5.6, 33/47 lines), [[ABCB9]] 0.749× (z -5.5, 20/45 lines), [[SELENOF]] 0.826× (z -5.1, 25/48 lines), [[ASNS]] 0.679× (z -5.0, 29/44 lines), [[HELLS]] 0.728× (z -5.0, 28/48 lines), [[RAD51AP1]] 0.694× (z -4.8, 23/44 lines), [[FBXO5]] 0.688× (z -4.8, 22/46 lines), [[UGT8]] 0.791× (z -4.8, 10/26 lines), [[MAD2L1]] 0.679× (z -4.7, 21/46 lines)

**5 µM** (35 genes, none with an alert; 12 shown): [[EME1]] 0.726× (z -5.0, 22/46 lines), [[ATAD3A]] 0.797× (z -4.9, 16/48 lines), [[TEF]] 0.779× (z -4.8, 12/48 lines), [[PEG10]] 0.793× (z -4.6, 17/32 lines), [[SKA1]] 0.814× (z -4.3, 10/46 lines), [[DTL]] 0.807× (z -4.2, 22/48 lines), [[SPC25]] 0.818× (z -4.2, 17/47 lines), [[H1-4]] 0.663× (z -4.1, 39/48 lines), [[MYBL2]] 0.763× (z -4.1, 22/44 lines), [[PRDX3]] 0.800× (z -4.1, 27/48 lines), [[ANLN]] 0.813× (z -4.0, 26/47 lines), [[PSAT1]] 0.801× (z -4.0, 21/40 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 124]] (+2.8), [[Module 010]] (+2.8), [[Module 230]] (+2.4) | [[Module 207]] (-4.1), [[Module 041]] (-3.3), [[Module 179]] (-3.3) |
| 0.5 µM | [[Module 043]] (+2.5), [[Module 010]] (+2.2) | [[Module 006]] (-2.6) |
| 5 µM | [[Module 043]] (+2.3), [[Module 225]] (+2.2) | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[SW 1088 (line)]] (1.25), [[NCI-H1573 (line)]] (1.18), [[NCI-H2122 (line)]] (1.14), [[HEC-1-A (line)]] (1.13) · weakest: [[A-427 (line)]] (0.588), [[SHP-77 (line)]] (0.670), [[BT-474 (line)]] (0.717) |
| 0.5 µM | — | [[SW 1088 (line)]] (2.24), [[H4 (line)]] (1.62), [[SW 1271 (line)]] (1.47), [[Hs 766T (line)]] (1.28) · weakest: [[A-427 (line)]] (0.422), [[NCI-H2347 (line)]] (0.459), [[NCI-H23 (line)]] (0.584) |
| 5 µM | — | [[Hs 766T (line)]] (1.53), [[NCI-H1573 (line)]] (1.53), [[SW 1088 (line)]] (1.39), [[NCI-H460 (line)]] (1.38) · weakest: [[CHP-212 (line)]] (0.184), [[NCI-H2347 (line)]] (0.537), [[NCI-H661 (line)]] (0.583) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar.*

- [[Rapamycin (drug)]] (+0.88, MTOR inhibitor); [[AZD1390 (drug)]] (+0.76, unclear); [[MK-3903 (drug)]] (+0.72, unclear); [[DTP3 (drug)]] (+0.67, unclear); [[ULK-101 (drug)]] (+0.65, unclear); [[Resveratrol (drug)]] (+0.64, unclear); [[Canagliflozin (hemihydrate) (drug)]] (+0.63, Glucose transporter inhibitor); [[Drospirenone (drug)]] (+0.63, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

None: no gene was found to set how the cells fare under it.

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
| [[MTOR]] | [[SMAP2]] | moves it that way too | B | MTOR activity raises SMAP2's level | compounds that target MTOR: 5 of 8 lower it (Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 3.4% of all compounds | 0.008 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[MTOR]] | [[ERICH1]] | moves it that way too | B | MTOR activity lowers ERICH1's level | compounds that target MTOR: 5 of 8 raise it (AZD-8055, Bimiralisib, Rapamycin, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 3.6% of all compounds | 0.010 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[MTOR]] | [[FBXO32]] | moves it that way too | B | MTOR activity lowers FBXO32's level | compounds that target MTOR: 6 of 8 raise it (AZD-8055, Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 75% of the class's compounds vs 7.3% of all compounds | 0.013 | ⚠ off-target possible; 6 compounds |
| [[MTOR]] | [[PDIA3]] | moves it that way too | B | MTOR activity raises PDIA3's level | compounds that target MTOR: 5 of 8 lower it (Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 3.9% of all compounds | 0.013 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[MTOR]] | [[YPEL1]] | moves it that way too | B | MTOR activity lowers YPEL1's level | compounds that target MTOR: 5 of 8 raise it (Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 3.9% of all compounds | 0.013 | ⚠ off-target possible; 5 compounds; artifact flags |

## Data

- `tables/drugs.parquet` — drug == "Temsirolimus"
- `tables/drugdoses.parquet` — dd in 988, 989, 990
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
