---
drug: "Rapamycin"
type: "drug"
salt_base: "Rapamycin"
targets: "MTOR, FKBP1A"
moa_fine: "MTOR inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 209
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Rapamycin

*MTOR inhibitor (inhibitor/antagonist) · targets: MTOR, FKBP1A · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 45 / 209 / 190; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.62 / 0.72.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:D3 | 20 / 25 | — | -0.16 | -3.6/-2.2/-1.2 | — |
| 0.5 µM | [[Plate 05]]:D3 | 125 / 84 | — | -0.41 | -3.6/-2.7/-1.6 | — |
| 5 µM | [[Plate 14]]:D3 | 102 / 88 | 0.849 | -0.02 | -5.1/-2.9/-1.7 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (20 genes, none with an alert; 12 shown): [[OTUD1]] 1.33× (z +4.1, 3/43 lines), [[KLHL24]] 1.29× (z +4.1, 29/49 lines), [[HSPBAP1]] 1.27× (z +3.7, 11/47 lines), [[CREBRF]] 1.26× (z +3.6, 24/49 lines), [[FBXL2]] 1.20× (z +3.6, 15/42 lines), [[SLC49A4]] 1.21× (z +3.5, 9/49 lines), [[SPINK1]] 1.76× (z +3.3, 6/17 lines), [[RRAGC-DT]] 1.31× (z +3.3, 15/48 lines), [[CTNS]] 1.21× (z +3.2, 5/47 lines), [[TM4SF19]] 1.26× (z +3.1, 8/28 lines), [[NPC1]] 1.21× (z +3.1, 17/48 lines), [[KIAA0319]] 1.21× (z +3.0, 6/30 lines)

**0.5 µM** (125 genes, none with an alert; 12 shown): [[PMEPA1]] 1.41× (z +5.9, 31/42 lines), [[SKIL]] 1.32× (z +4.8, 30/46 lines), [[AHNAK2]] 1.47× (z +4.6, 29/36 lines), [[GATA2-AS1]] 1.39× (z +4.6, 10/38 lines), [[PACS2]] 1.26× (z +4.5, 19/48 lines), [[SYT14]] 1.40× (z +4.4, 5/19 lines), [[BACH2]] 1.27× (z +4.4, 9/41 lines), [[AGO4]] 1.26× (z +4.4, 23/48 lines), [[ING4]] 1.26× (z +4.3, 13/46 lines), [[ZDHHC2]] 1.21× (z +4.3, 10/37 lines), [[SLC49A4]] 1.27× (z +4.3, 20/47 lines), [[HSPBAP1]] 1.31× (z +4.2, 11/47 lines)

**5 µM** (102 genes, none with an alert; 12 shown): [[PMEPA1]] 1.41× (z +8.2, 35/42 lines), [[INSR]] 1.22× (z +5.3, 28/45 lines), [[SKIL]] 1.24× (z +5.3, 27/46 lines), [[BEND7]] 1.24× (z +5.2, 14/36 lines), [[HSPBAP1]] 1.27× (z +5.2, 19/48 lines), [[RAB31]] 1.25× (z +5.1, 18/32 lines), [[VAC14]] 1.22× (z +5.1, 22/48 lines), [[EBF4]] 1.31× (z +5.1, 15/36 lines), [[PACS2]] 1.21× (z +5.1, 21/48 lines), [[RRAGC-DT]] 1.33× (z +5.0, 29/48 lines), [[KLHL24]] 1.26× (z +5.0, 31/48 lines), [[FHOD3]] 1.25× (z +4.9, 18/34 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (25 genes, none with an alert; 12 shown): [[PSAT1]] 0.687× (z -4.8, 19/40 lines), [[MARS1]] 0.789× (z -4.1, 23/49 lines), [[MYBL2]] 0.690× (z -4.0, 17/44 lines), [[SKA1]] 0.783× (z -3.7, 10/45 lines), [[MCM8]] 0.804× (z -3.6, 16/48 lines), [[HELLS]] 0.812× (z -3.3, 21/49 lines), [[APLN]] 0.646× (z -3.3, 6/29 lines), [[RRM2]] 0.762× (z -3.2, 19/46 lines), [[MCM3]] 0.765× (z -3.2, 15/45 lines), [[FANCI]] 0.827× (z -3.2, 16/49 lines), [[CENPM]] 0.725× (z -3.1, 5/42 lines), [[ACAT2]] 0.815× (z -3.1, 10/48 lines)

**0.5 µM** (84 genes, none with an alert; 12 shown): [[ASNS]] 0.661× (z -5.4, 30/44 lines), [[PSAT1]] 0.663× (z -5.3, 26/39 lines), [[MARS1]] 0.762× (z -4.7, 24/48 lines), [[PHGDH]] 0.688× (z -4.5, 22/43 lines), [[ERCC6L]] 0.717× (z -4.4, 16/44 lines), [[BPNT1]] 0.779× (z -4.4, 16/46 lines), [[YARS1]] 0.816× (z -4.4, 24/48 lines), [[FKBP14]] 0.770× (z -4.3, 20/48 lines), [[CARS1]] 0.816× (z -4.2, 22/48 lines), [[RAD54B]] 0.810× (z -4.1, 16/48 lines), [[FANCB]] 0.814× (z -4.1, 14/48 lines), [[XPOT]] 0.822× (z -4.1, 24/48 lines)

**5 µM** (88 genes, none with an alert; 12 shown): [[HELLS]] 0.783× (z -5.5, 28/48 lines), [[MAGOHB]] 0.811× (z -5.4, 21/48 lines), [[PSAT1]] 0.745× (z -5.4, 22/40 lines), [[MYBL2]] 0.706× (z -5.3, 24/44 lines), [[MPDU1]] 0.765× (z -5.3, 26/47 lines), [[SLC1A5]] 0.818× (z -5.2, 21/47 lines), [[ASNS]] 0.754× (z -5.2, 28/44 lines), [[TENT5A]] 0.811× (z -5.2, 23/37 lines), [[SMAP2]] 0.819× (z -5.0, 26/48 lines), [[DNAJB11]] 0.776× (z -5.0, 33/48 lines), [[SHCBP1]] 0.795× (z -4.8, 27/47 lines), [[CDC6]] 0.783× (z -4.8, 22/48 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | [[Module 006]] (-2.2) |
| 0.5 µM | — | [[Module 006]] (-2.1), [[Module 065]] (-2.0) |
| 5 µM | [[Module 193]] (+2.6), [[Module 230]] (+2.5), [[Module 222]] (+2.3) | [[Module 065]] (-2.7), [[Module 148]] (-2.7), [[Module 006]] (-2.5) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[SW 1088 (line)]] (1.63), [[RPMI-7951 (line)]] (1.59), [[Hs 766T (line)]] (1.58), [[H4 (line)]] (1.57) · weakest: [[NCI-H2347 (line)]] (0.219), [[SHP-77 (line)]] (0.293), [[A-427 (line)]] (0.463) |
| 0.5 µM | — | [[SW 1088 (line)]] (1.65), [[Hs 766T (line)]] (1.17), [[H4 (line)]] (1.15), [[SW 1271 (line)]] (1.14) · weakest: [[A-427 (line)]] (0.611), [[NCI-H1792 (line)]] (0.625), [[SW1417 (line)]] (0.640) |
| 5 µM | — | [[SW 1088 (line)]] (1.62), [[RPMI-7951 (line)]] (1.40), [[H4 (line)]] (1.33), [[NCI-H460 (line)]] (1.26) · weakest: [[CHP-212 (line)]] (0.442), [[SW 1271 (line)]] (0.495), [[HepG2_C3A (line)]] (0.624) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[Temsirolimus (drug)]] (+0.88, MTOR inhibitor); [[Larotrectinib sulfate (drug)]] (+0.76, Other TK inhibitor, ⚠ no trustworthy dose (vector dose flagged: unreliable plate only)); [[AZD1390 (drug)]] (+0.74, unclear); [[MK-3903 (drug)]] (+0.72, unclear); [[Resveratrol (drug)]] (+0.69, unclear); [[ULK-101 (drug)]] (+0.66, unclear); [[AZD-8055 (drug)]] (+0.63, MTOR inhibitor); [[DTP3 (drug)]] (+0.59, unclear); [[Lactate (calcium) (drug)]] (+0.58, unclear)

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

- `tables/drugs.parquet` — drug == "Rapamycin"
- `tables/drugdoses.parquet` — dd in 875, 876, 877
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
