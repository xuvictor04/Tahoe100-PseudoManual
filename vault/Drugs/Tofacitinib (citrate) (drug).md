---
drug: "Tofacitinib (citrate)"
type: "drug"
salt_base: "Tofacitinib"
targets: "JAK1, JAK2, JAK3"
moa_fine: "JAK/STAT inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 296
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Tofacitinib (citrate)

*JAK/STAT inhibitor (inhibitor/antagonist) · targets: JAK1, JAK2, JAK3 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 61 / 296 / 197; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.45 / 0.75.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:D5 | 1 / 60 | — | -0.25 | -0.0/+0.2/-0.5 | — |
| 0.5 µM | [[Plate 05]]:D5 | 68 / 228 | — | -0.33 | +0.1/+0.5/-0.5 | — |
| 5 µM | [[Plate 14]]:D5 | 10 / 187 | 0.814 | -0.09 | -0.7/+0.6/-0.6 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[ENSG00000284959]] 1.33× (z +2.8, 1/44 lines)

**0.5 µM** (68 genes, none with an alert; 12 shown): [[DLX6-AS1]] 1.69× (z +4.6, 2/16 lines), [[GNG7]] 1.30× (z +4.3, 6/45 lines), [[KCNMA1]] 1.24× (z +4.1, 10/22 lines), [[CTDSPL]] 1.23× (z +4.0, 17/43 lines), [[TMEM139]] 1.65× (z +3.9, 3/13 lines), [[NT5DC2]] 1.39× (z +3.9, 8/43 lines), [[WNK3]] 1.28× (z +3.7, 0/16 lines), [[CYB561A3]] 1.32× (z +3.7, 5/41 lines), [[ST6GAL2]] 1.64× (z +3.7, 2/9 lines), [[WNT5B]] 1.26× (z +3.7, 5/26 lines), [[MYB]] 1.46× (z +3.7, 3/23 lines), [[SGSM1]] 1.28× (z +3.6, 7/39 lines)

**5 µM** (10 genes, none with an alert): [[KCNMA1]] 1.21× (z +5.3, 10/23 lines), [[GPR173]] 1.27× (z +3.8, 5/18 lines), [[SNED1-AS1]] 1.22× (z +3.4, 5/45 lines), [[ENSG00000267748]] 1.25× (z +3.3, 1/25 lines), [[FSTL4]] 1.28× (z +3.1, 2/24 lines), [[ENSG00000272840]] 1.21× (z +3.1, 3/36 lines), [[ENSG00000286369]] 1.21× (z +3.0, 2/43 lines), [[ENSG00000286415]] 1.24× (z +3.0, 4/46 lines), [[NPTX1]] 1.36× (z +3.0, 2/23 lines), [[AKAP12]] 1.20× (z +2.9, 11/31 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (60 genes, none with an alert; 12 shown): [[TRIM22]] 0.588× (z -5.4, 23/30 lines), [[IFIH1]] 0.719× (z -4.4, 25/46 lines), [[SP100]] 0.816× (z -4.2, 23/46 lines), [[IFI44]] 0.712× (z -4.2, 25/37 lines), [[EIF2AK2]] 0.792× (z -4.2, 29/48 lines), [[SLC15A3]] 0.606× (z -4.1, 9/29 lines), [[HERC5]] 0.724× (z -4.0, 15/33 lines), [[IFI44L]] 0.632× (z -4.0, 20/26 lines), [[PNPT1]] 0.773× (z -4.0, 24/48 lines), [[MX1]] 0.684× (z -3.9, 23/30 lines), [[STAT1]] 0.764× (z -3.9, 29/49 lines), [[RSAD2]] 0.592× (z -3.9, 17/35 lines)

**0.5 µM** (228 genes, none with an alert; 12 shown): [[PARP9]] 0.315× (z -14.0, 37/41 lines), [[STAT1]] 0.391× (z -13.8, 40/48 lines), [[MX1]] 0.271× (z -13.8, 27/29 lines), [[IFI44]] 0.329× (z -13.7, 28/36 lines), [[EIF2AK2]] 0.471× (z -13.5, 36/47 lines), [[TRIM22]] 0.266× (z -13.4, 25/30 lines), [[OAS3]] 0.288× (z -13.3, 36/43 lines), [[OAS2]] 0.186× (z -12.5, 30/34 lines), [[MX2]] 0.240× (z -12.4, 29/32 lines), [[SP100]] 0.561× (z -12.1, 32/45 lines), [[ADAR]] 0.608× (z -12.0, 37/48 lines), [[OAS1]] 0.315× (z -11.6, 30/34 lines)

**5 µM** (187 genes, none with an alert; 12 shown): [[MX1]] 0.268× (z -19.6, 28/30 lines), [[PARP9]] 0.341× (z -18.4, 36/42 lines), [[EIF2AK2]] 0.510× (z -17.1, 35/48 lines), [[OAS3]] 0.331× (z -16.7, 37/44 lines), [[STAT1]] 0.450× (z -16.6, 38/49 lines), [[IFI44]] 0.388× (z -16.5, 28/37 lines), [[OAS2]] 0.215× (z -16.2, 30/34 lines), [[PLSCR1]] 0.423× (z -15.9, 35/41 lines), [[IRF9]] 0.547× (z -15.4, 37/49 lines), [[OAS1]] 0.377× (z -13.8, 30/36 lines), [[SP100]] 0.631× (z -13.6, 30/46 lines), [[CMPK2]] 0.297× (z -13.5, 29/37 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | [[Module 032]] (-2.3) |
| 0.5 µM | — | [[Module 032]] (-6.1), [[Module 070]] (-2.7), [[Module 139]] (-2.4) |
| 5 µM | [[Module 043]] (+2.2), [[Module 040]] (+2.0) | [[Module 032]] (-7.0), [[Module 070]] (-2.9), [[Module 139]] (-2.7) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[BT-474 (line)]] (2.44), [[CHP-212 (line)]] (2.02), [[NCI-H23 (line)]] (1.81), [[C-33 A (line)]] (1.67) · weakest: [[NCI-H661 (line)]] (-0.0792), [[NCI-H2122 (line)]] (-0.0586), [[H4 (line)]] (0.0261) |
| 0.5 µM | — | [[BT-474 (line)]] (1.97), [[LoVo (line)]] (1.55), [[MIA PaCa-2 (line)]] (1.49), [[NCI-H1792 (line)]] (1.49) · weakest: [[NCI-H460 (line)]] (0.127), [[HEC-1-A (line)]] (0.168), [[NCI-H2030 (line)]] (0.212) |
| 5 µM | — | [[COLO 205 (line)]] (1.78), [[MIA PaCa-2 (line)]] (1.74), [[BT-474 (line)]] (1.72), [[A549 (line)]] (1.57) · weakest: [[NCI-H2122 (line)]] (0.0212), [[HEC-1-A (line)]] (0.0858), [[NCI-H460 (line)]] (0.138) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[Tofacitinib (drug)]] (+0.82, JAK/STAT inhibitor); [[Fedratinib (hydrochloride hydrate) (drug)]] (+0.53, JAK/STAT inhibitor); [[Ixazomib (drug)]] (+0.52, Proteasome inhibitor); [[Sunitinib (drug)]] (+0.49, Multi-TK inhibitor, ⚠ vector dose flagged: toxic); [[Bergenin (drug)]] (+0.46, unclear); [[Ipatasertib (drug)]] (+0.44, PI3K/AKT inhibitor); [[Methylprednisolone succinate (drug)]] (+0.44, Glucocorticoid receptor agonist); [[Celecoxib (drug)]] (+0.41, Cyclooxygenase inhibitor); [[Bimatoprost (drug)]] (+0.41, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

None: no gene was found to set how the cells fare under it.

### Its targets: what acting on them probably does

*Drug-target arrows of the compound classes it belongs to (compounds sharing a listed target and mechanism; one molecule counts once, under all its names): the target → a gene whose level those compounds move. A row that names several targets is one test: the compounds share them all, and any of them could be the cause. 38 arrows, 38 of them with an alert ⚠; grade A 0, B 38, C 0. Shown: the 15 strongest; 23 more arrows (23 of them with an alert ⚠) not shown.*

| Its target | Gene it moves | This drug | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|---|
| [[JAK2]] | [[TAP2]] | moves it that way too | B | JAK2 activity raises TAP2's level | compounds that target JAK2: 3 of 3 lower it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 2.5% of all compounds | 0.026 | ⚠ off-target possible; 3 compounds |
| [[JAK2]] | [[OGFR]] | moves it that way too | B | JAK2 activity raises OGFR's level | compounds that target JAK2: 3 of 3 lower it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 3.1% of all compounds | 0.032 | ⚠ off-target possible; 3 compounds |
| [[JAK2]] | [[TRIM25]] | moves it that way too | B | JAK2 activity raises TRIM25's level | compounds that target JAK2: 3 of 3 lower it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 3.1% of all compounds | 0.032 | ⚠ off-target possible; 3 compounds |
| [[JAK2]] | [[ADAR]] | moves it that way too | B | JAK2 activity raises ADAR's level | compounds that target JAK2: 3 of 3 lower it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 3.4% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds |
| [[JAK2]] | [[STRIP2]] | moves it that way too | B | JAK2 activity raises STRIP2's level | compounds that target JAK2: 3 of 3 lower it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 3.4% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds |
| [[JAK2]] | [[NAMPT]] | moves it that way too | B | JAK2 activity raises NAMPT's level | compounds that target JAK2: 3 of 3 lower it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 3.6% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |
| [[JAK2]] | [[ZSCAN5A]] | does not move it that way (the class's other compounds do) | B | JAK2 activity lowers ZSCAN5A's level | compounds that target JAK2: 2 of 3 raise it (Fedratinib, Filgotinib) | 67% of the class's compounds vs 0.6% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds |
| [[JAK2]] | [[IL15]] | moves it that way too | B | JAK2 activity raises IL15's level | compounds that target JAK2: 3 of 3 lower it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 3.9% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |
| [[JAK2]] | [[PATL1]] | moves it that way too | B | JAK2 activity raises PATL1's level | compounds that target JAK2: 3 of 3 lower it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 3.9% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |
| [[JAK2]] | [[TRAF3IP2]] | moves it that way too | B | JAK2 activity raises TRAF3IP2's level | compounds that target JAK2: 3 of 3 lower it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 3.9% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |
| [[JAK2]] | [[IL15RA]] | moves it that way too | B | JAK2 activity raises IL15RA's level | compounds that target JAK2: 3 of 3 lower it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 4.2% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds |
| [[JAK2]] | [[PLEKHA4]] | moves it that way too | B | JAK2 activity raises PLEKHA4's level | compounds that target JAK2: 3 of 3 lower it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 4.8% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |
| [[JAK1]], [[JAK3]] | [[CTDSPL]] | moves it that way too | B | JAK1, JAK3 activity lowers CTDSPL's level | compounds that target JAK1, JAK3: 2 of 2 raise it (Filgotinib, Tofacitinib) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; shared targets |
| [[JAK2]] | [[ENSG00000291144]] | moves it that way too | B | JAK2 activity raises ENSG00000291144's level | compounds that target JAK2: 3 of 3 lower it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 5.3% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[JAK2]] | [[BIRC3]] | moves it that way too | B | JAK2 activity raises BIRC3's level | compounds that target JAK2: 3 of 3 lower it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 5.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |

## Data

- `tables/drugs.parquet` — drug == "Tofacitinib (citrate)"
- `tables/drugdoses.parquet` — dd in 1015, 1016, 1017
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
