---
drug: "Asciminib"
type: "drug"
salt_base: "Asciminib"
targets: "ABL1"
moa_fine: "Other TK inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.05"
max_sig_genes: 92
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Asciminib

*Other TK inhibitor (inhibitor/antagonist) · targets: ABL1 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 92 / 5 / 7; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): low dose only (noise?).
> Signature similarity between consecutive doses (low–mid / mid–high): 0.52 / 0.15.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:D2 | 10 / 82 | — | -0.24 | -0.1/+0.9/+0.7 | — |
| 0.5 µM | [[Plate 11]]:D2 | 0 / 5 | — | +0.62 | -0.4/+0.8/-0.9 | — |
| 5 µM | [[Plate 12]]:D2 | 0 / 7 | — | -0.43 | -0.1/+0.6/+0.4 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (10 genes, none with an alert): [[RWDD4]] 1.28× (z +3.4, 3/47 lines), [[KMT2B]] 1.23× (z +3.4, 16/48 lines), [[SCML2]] 1.23× (z +3.3, 12/40 lines), [[FBRS]] 1.22× (z +3.1, 14/48 lines), [[ZUP1]] 1.22× (z +2.9, 9/47 lines), [[CCNT2]] 1.21× (z +2.9, 17/48 lines), [[KDM6B]] 1.25× (z +2.9, 16/48 lines), [[ARHGAP20]] 1.40× (z +2.8, 0/12 lines), [[HSF2]] 1.23× (z +2.8, 3/47 lines), [[OTUD6B]] 1.21× (z +2.7, 7/47 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (82 genes, none with an alert; 12 shown): [[ANGPT1]] 0.734× (z -3.9, 1/23 lines), [[DEPTOR]] 0.714× (z -3.9, 8/39 lines), [[DPY19L2P2]] 0.709× (z -3.8, 11/45 lines), [[ENSG00000285534]] 0.707× (z -3.8, 4/16 lines), [[CD226]] 0.615× (z -3.8, 15/39 lines), [[HGF]] 0.646× (z -3.7, 3/9 lines), [[ENSG00000286739]] 0.713× (z -3.7, 6/41 lines), [[TTTY14]] 0.729× (z -3.6, 4/21 lines), [[CD96]] 0.719× (z -3.6, 9/33 lines), [[LY75]] 0.792× (z -3.6, 3/18 lines), [[ENSG00000258081]] 0.753× (z -3.6, 2/17 lines), [[LINC01482]] 0.715× (z -3.5, 6/40 lines)

**0.5 µM** (5 genes, none with an alert): [[RHOXF1-AS1]] 0.626× (z -3.9, 8/37 lines), [[F2RL2]] 0.518× (z -3.8, 3/15 lines), [[VSIG1]] 0.562× (z -3.7, 2/14 lines), [[HAGLR]] 0.715× (z -3.5, 6/28 lines), [[BEAN1]] 0.787× (z -3.0, 5/38 lines)

**5 µM** (7 genes, none with an alert): [[IDI1]] 0.735× (z -4.1, 26/48 lines), [[MMAB]] 0.742× (z -4.0, 11/47 lines), [[MSMO1]] 0.730× (z -3.4, 22/47 lines), [[CYP51A1]] 0.807× (z -3.4, 23/47 lines), [[GIPC1]] 0.801× (z -3.3, 17/47 lines), [[HMGCS1]] 0.773× (z -3.2, 21/47 lines), [[DHCR24]] 0.801× (z -2.9, 14/44 lines)

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
| 0.05 µM | — | [[AN3 CA (line)]] (1.89), [[CHP-212 (line)]] (1.70), [[NCI-H1792 (line)]] (1.41), [[SW48 (line)]] (1.40) · weakest: [[SW 1088 (line)]] (-0.152), [[SHP-77 (line)]] (0.577), [[NCI-H23 (line)]] (0.698) |
| 0.5 µM | — | — |
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 4 next most similar without an alert.*

- [[Acetazolamide (drug)]] (+0.73, unclear, ⚠ only 3 significant genes); [[L-Thyroxine (sodium salt pentahydrate) (drug)]] (+0.71, unclear); [[Fluvoxamine (drug)]] (+0.70, unclear); [[Capivasertib (drug)]] (+0.69, PI3K/AKT inhibitor, ⚠ only 5 significant genes); [[Indacaterol (maleate) (drug)]] (+0.68, Adrenoceptor agonist, ⚠ only 3 significant genes); [[Delamanid (drug)]] (+0.68, unclear, ⚠ only 6 significant genes); [[Gallic acid (drug)]] (+0.65, Cyclooxygenase inhibitor); [[Goserelin (acetate) (drug)]] (+0.63, unclear); [[Piroxicam (drug)]] (+0.62, Cyclooxygenase inhibitor); [[Tadalafil (drug)]] (+0.62, unclear); [[Lucanthone (drug)]] (+0.61, unclear); [[Lopinavir (drug)]] (+0.59, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

None: no gene was found to set how the cells fare under it.

### Its targets: what acting on them probably does

*Drug-target arrows of the compound classes it belongs to (compounds sharing a listed target and mechanism; one molecule counts once, under all its names): the target → a gene whose level those compounds move. A row that names several targets is one test: the compounds share them all, and any of them could be the cause. 54 arrows, 54 of them with an alert ⚠; grade A 0, B 54, C 0. Shown: the 15 strongest; 39 more arrows (39 of them with an alert ⚠) not shown.*

| Its target | Gene it moves | This drug | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|---|
| [[ABL1]] | [[ANKMY2]] | does not move it that way (the class's other compounds do) | B | ABL1 activity lowers ANKMY2's level | compounds that target ABL1: 4 of 6 raise it (Flumatinib, NG25, Ponatinib, Radotinib) | 67% of the class's compounds vs 2.8% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ABL1]] | [[CDKN2B]] | does not move it that way (the class's other compounds do) | B | ABL1 activity raises CDKN2B's level | compounds that target ABL1: 3 of 6 lower it (NG25, Ponatinib, Radotinib) | 50% of the class's compounds vs 1.1% of all compounds | 0.025 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ABL1]] | [[GSG1L]] | does not move it that way (the class's other compounds do) | B | ABL1 activity raises GSG1L's level | compounds that target ABL1: 3 of 6 lower it (NG25, Ponatinib, Radotinib) | 50% of the class's compounds vs 1.1% of all compounds | 0.025 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ABL1]] | [[TMEM185A]] | does not move it that way (the class's other compounds do) | B | ABL1 activity lowers TMEM185A's level | compounds that target ABL1: 4 of 6 raise it (Flumatinib, NG25, Ponatinib, Radotinib) | 67% of the class's compounds vs 3.4% of all compounds | 0.025 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ABL1]] | [[NUAK1]] | does not move it that way (the class's other compounds do) | B | ABL1 activity lowers NUAK1's level | compounds that target ABL1: 4 of 6 raise it (Flumatinib, NG25, Ponatinib, Radotinib) | 67% of the class's compounds vs 3.6% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ABL1]] | [[CAMK2G]] | does not move it that way (the class's other compounds do) | B | ABL1 activity lowers CAMK2G's level | compounds that target ABL1: 4 of 6 raise it (Flumatinib, NG25, Ponatinib, Radotinib) | 67% of the class's compounds vs 3.9% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ABL1]] | [[CDKN1A]] | does not move it that way (the class's other compounds do) | B | ABL1 activity raises CDKN1A's level | compounds that target ABL1: 3 of 6 lower it (NG25, Ponatinib, Radotinib) | 50% of the class's compounds vs 1.4% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ABL1]] | [[ENSG00000225218]] | does not move it that way (the class's other compounds do) | B | ABL1 activity raises ENSG00000225218's level | compounds that target ABL1: 3 of 6 lower it (NG25, Ponatinib, Radotinib) | 50% of the class's compounds vs 1.4% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ABL1]] | [[ENSG00000290241]] | does not move it that way (the class's other compounds do) | B | ABL1 activity raises ENSG00000290241's level | compounds that target ABL1: 3 of 6 lower it (NG25, Ponatinib, Radotinib) | 50% of the class's compounds vs 1.4% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ABL1]] | [[HEATR6]] | does not move it that way (the class's other compounds do) | B | ABL1 activity lowers HEATR6's level | compounds that target ABL1: 3 of 6 raise it (Flumatinib, Ponatinib, Radotinib) | 50% of the class's compounds vs 1.4% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds |
| [[ABL1]] | [[PRKAB2]] | does not move it that way (the class's other compounds do) | B | ABL1 activity lowers PRKAB2's level | compounds that target ABL1: 3 of 6 raise it (NG25, Ponatinib, Radotinib) | 50% of the class's compounds vs 1.4% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ABL1]] | [[SLC8A2]] | does not move it that way (the class's other compounds do) | B | ABL1 activity raises SLC8A2's level | compounds that target ABL1: 3 of 6 lower it (NG25, Ponatinib, Radotinib) | 50% of the class's compounds vs 1.4% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ABL1]] | [[ALDH7A1]] | does not move it that way (the class's other compounds do) | B | ABL1 activity lowers ALDH7A1's level | compounds that target ABL1: 4 of 6 raise it (Flumatinib, NG25, Ponatinib, Radotinib) | 67% of the class's compounds vs 4.2% of all compounds | 0.037 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ABL1]] | [[ARL6]] | does not move it that way (the class's other compounds do) | B | ABL1 activity lowers ARL6's level | compounds that target ABL1: 4 of 6 raise it (Flumatinib, NG25, Ponatinib, Radotinib) | 67% of the class's compounds vs 4.2% of all compounds | 0.037 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ABL1]] | [[PIP4P2]] | does not move it that way (the class's other compounds do) | B | ABL1 activity lowers PIP4P2's level | compounds that target ABL1: 4 of 6 raise it (Flumatinib, NG25, Ponatinib, Radotinib) | 67% of the class's compounds vs 4.2% of all compounds | 0.037 | ⚠ off-target possible; 4 compounds; artifact flags |

## Data

- `tables/drugs.parquet` — drug == "Asciminib"
- `tables/drugdoses.parquet` — dd in 111, 112, 113
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
