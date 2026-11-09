---
drug: "Regorafenib"
type: "drug"
salt_base: "Regorafenib"
targets: "BRAF, FLT1, FLT4, KDR, KIT, PDGFRB, RAF1, RET, TEK"
moa_fine: "Multi-TK inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 61
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Regorafenib

*Multi-TK inhibitor (inhibitor/antagonist) · targets: BRAF, FLT1, FLT4, KDR, KIT, PDGFRB, RAF1, RET, TEK · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 3 / 0 / 61; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): -0.07 / -0.06.
> Flags by dose: - / noisy plate (z scaled) / noisy plate (z scaled).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:B7 | 3 / 0 | — | -0.37 | -0.2/+0.0/-0.2 | — |
| 0.5 µM | [[Plate 02]]:B7 | 0 / 0 | — | +0.58 | -0.6/-0.7/-1.0 | noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:B7 | 43 / 18 | — | +0.22 | +0.8/+0.8/-0.4 | noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (3 genes, none with an alert): [[DMWD]] 1.26× (z +3.5, 5/48 lines), [[EPHA2]] 1.23× (z +3.1, 10/37 lines), [[BMP6]] 1.24× (z +2.7, 2/25 lines)

**5 µM** (43 genes, none with an alert; 12 shown): [[MAP2K6]] 3.54× (z +5.9, 12/24 lines), [[TRERF1]] 1.51× (z +3.9, 20/42 lines), [[DIXDC1]] 1.45× (z +3.9, 8/48 lines), [[TARBP1]] 1.47× (z +3.9, 14/48 lines), [[NFIA]] 1.47× (z +3.9, 17/37 lines), [[TM7SF3]] 1.37× (z +3.9, 9/48 lines), [[ALDH7A1]] 1.35× (z +3.6, 6/46 lines), [[CAMK2G]] 1.31× (z +3.6, 13/48 lines), [[ACSS1]] 1.56× (z +3.6, 0/35 lines), [[ERAP2]] 1.46× (z +3.5, 5/41 lines), [[MEF2C]] 1.50× (z +3.5, 8/34 lines), [[NSL1]] 1.33× (z +3.2, 5/48 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**5 µM** (18 genes, none with an alert; 12 shown): [[GXYLT1]] 0.781× (z -3.6, 9/48 lines), [[DIAPH1]] 0.799× (z -3.5, 17/48 lines), [[PRDM1]] 0.631× (z -3.5, 8/32 lines), [[SHPK]] 0.715× (z -3.2, 6/46 lines), [[ACSL4]] 0.799× (z -3.1, 10/47 lines), [[VMP1]] 0.769× (z -3.0, 19/48 lines), [[NPC1]] 0.704× (z -2.9, 17/47 lines), [[PPARD]] 0.711× (z -2.9, 16/46 lines), [[EHD4]] 0.774× (z -2.8, 13/48 lines), [[LINC02454]] 0.564× (z -2.8, 7/27 lines), [[B3GNT5]] 0.723× (z -2.8, 6/41 lines), [[LIF]] 0.624× (z -2.8, 7/38 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[Module 146]] (+2.5), [[Module 045]] (+2.3) | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | [[NCI-H23 (line)]] (1.59), [[AsPC-1 (line)]] (1.57), [[SK-MEL-2 (line)]] (1.37), [[LOX-IMVI (line)]] (1.37) · weakest: [[SW48 (line)]] (0.193), [[C-33 A (line)]] (0.283), [[NCI-H661 (line)]] (0.339) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[Radotinib (drug)]] (+0.83, Other TK inhibitor); [[Flumatinib (mesylate) (drug)]] (+0.74, Other TK inhibitor); [[Ponatinib (drug)]] (+0.73, Multi-TK inhibitor); [[Cabozantinib (S-malate) (drug)]] (+0.72, Multi-TK inhibitor); [[Afatinib (drug)]] (+0.66, EGFR/ERBB inhibitor); [[NG25 (drug)]] (+0.60, Other MAPK inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Bentamapimod (drug)]] (+0.59, Other MAPK inhibitor); [[Elimusertib hydrochloride (drug)]] (+0.55, unclear); [[Vandetanib (drug)]] (+0.52, Multi-TK inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

None: no gene was found to set how the cells fare under it.

### Its targets: what acting on them probably does

*Drug-target arrows of the compound classes it belongs to (compounds sharing a listed target and mechanism; one molecule counts once, under all its names): the target → a gene whose level those compounds move. A row that names several targets is one test: the compounds share them all, and any of them could be the cause. 5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Its target | Gene it moves | This drug | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|---|
| KIT | [[PKD1P6]] | does not move it that way (the class's other compounds do) | B | KIT activity lowers PKD1P6's level | compounds that target KIT: 3 of 4 raise it (Pexidartinib, Ponatinib, c-Kit-IN-1) | 75% of the class's compounds vs 1.7% of all compounds | 0.025 | ⚠ off-target possible; 3 compounds; artifact flags |
| KDR | [[PPARD]] | moves it that way too | B | KDR activity raises PPARD's level | compounds that target KDR: 5 of 8 lower it (Cabozantinib, Ponatinib, Regorafenib, Sulfatinib, Sunitinib) | 62% of the class's compounds vs 6.2% of all compounds | 0.036 | ⚠ off-target possible; 5 compounds; artifact flags |
| KDR | [[DNAJB6]] | does not move it that way (the class's other compounds do) | B | KDR activity raises DNAJB6's level | compounds that target KDR: 3 of 8 lower it (Cabozantinib, Ponatinib, c-Kit-IN-1) | 38% of the class's compounds vs 1.7% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| KDR | [[DUSP10]] | does not move it that way (the class's other compounds do) | B | KDR activity raises DUSP10's level | compounds that target KDR: 4 of 8 lower it (Cabozantinib, Ponatinib, Sunitinib, c-Kit-IN-1) | 50% of the class's compounds vs 4.5% of all compounds | 0.077 | ⚠ off-target possible; 4 compounds; artifact flags |
| KDR | [[PGLS-DT]] | does not move it that way (the class's other compounds do) | B | KDR activity lowers PGLS-DT's level | compounds that target KDR: 4 of 8 raise it (Cabozantinib, Ponatinib, Sunitinib, c-Kit-IN-1) | 50% of the class's compounds vs 4.5% of all compounds | 0.077 | ⚠ off-target possible; 4 compounds; artifact flags |

## Data

- `tables/drugs.parquet` — drug == "Regorafenib"
- `tables/drugdoses.parquet` — dd in 878, 879, 880
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
