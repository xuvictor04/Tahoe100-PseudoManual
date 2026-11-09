---
drug: "Vandetanib"
type: "drug"
salt_base: "Vandetanib"
targets: "EGFR, KDR"
moa_fine: "Multi-TK inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 30
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Vandetanib

*Multi-TK inhibitor (inhibitor/antagonist) · targets: EGFR, KDR · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 4 / 9 / 30; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.11 / 0.05.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:E10 | 1 / 3 | — | -0.19 | -0.3/-0.9/-0.1 | — |
| 0.5 µM | [[Plate 11]]:E10 | 9 / 0 | — | -0.40 | -0.2/-0.7/-0.0 | — |
| 5 µM | [[Plate 12]]:E10 | 4 / 26 | — | +0.06 | -1.0/-1.1/-0.5 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[PAX5]] 1.35× (z +2.8, 0/24 lines)

**0.5 µM** (9 genes, none with an alert): [[LINC01776]] 1.48× (z +3.5, 1/18 lines), [[AGFG2]] 1.24× (z +3.3, 3/45 lines), [[SLC25A19]] 1.25× (z +3.1, 5/44 lines), [[FBN2]] 1.23× (z +3.1, 0/15 lines), [[PAMR1]] 1.55× (z +3.1, 0/10 lines), [[PREX1]] 1.20× (z +3.1, 1/27 lines), [[GRIN2C]] 1.46× (z +3.0, 2/28 lines), [[TMCC2]] 1.37× (z +2.9, 0/34 lines), [[CELF6]] 1.42× (z +2.9, 2/40 lines)

**5 µM** (4 genes, none with an alert): [[IDH1]] 1.32× (z +3.9, 15/48 lines), [[SCD]] 1.29× (z +3.6, 27/48 lines), [[SESN3]] 1.21× (z +3.2, 4/28 lines), [[AR]] 1.27× (z +3.0, 1/20 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (3 genes, none with an alert): [[ENSG00000251675]] 0.734× (z -3.7, 10/43 lines), [[ENSG00000259755]] 0.809× (z -2.9, 6/41 lines), [[TMEM74B]] 0.745× (z -2.8, 7/38 lines)

**5 µM** (26 genes, none with an alert; 12 shown): [[ETS1]] 0.804× (z -3.8, 18/37 lines), [[SRGAP1]] 0.827× (z -3.5, 21/46 lines), [[CCN1]] 0.732× (z -3.5, 19/41 lines), [[ENSG00000283511]] 0.614× (z -3.3, 14/36 lines), [[SARDH]] 0.655× (z -3.3, 5/23 lines), [[ENSG00000280128]] 0.722× (z -3.3, 7/46 lines), [[ENSG00000269026]] 0.795× (z -3.3, 7/41 lines), [[AMOTL2]] 0.806× (z -3.3, 15/44 lines), [[CYTOR]] 0.786× (z -3.3, 21/46 lines), [[ARFRP1]] 0.776× (z -3.2, 10/47 lines), [[PMEPA1]] 0.827× (z -3.2, 13/42 lines), [[MIR4435-2HG]] 0.833× (z -3.2, 17/45 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[Module 171]] (+2.2), [[Module 045]] (+2.0) | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | [[H4 (line)]] (1.90), [[KATO III (line)]] (1.74), [[NCI-H1573 (line)]] (1.65), [[LS 180 (line)]] (1.65) · weakest: [[SNU-1 (line)]] (0.112), [[SW 1088 (line)]] (0.121), [[SNU-423 (line)]] (0.340) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Cabozantinib (S-malate) (drug)]] (+0.68, Multi-TK inhibitor); [[Ponatinib (drug)]] (+0.66, Multi-TK inhibitor); [[Terfenadine (drug)]] (+0.61, unclear); [[Fostamatinib (disodium hexahydrate) (drug)]] (+0.60, Other TK inhibitor, ⚠ only 3 significant genes; no trustworthy dose (vector dose flagged: unreliable plate only)); [[Ivabradine (hydrochloride) (drug)]] (+0.59, unclear, ⚠ no trustworthy dose (vector dose flagged: unreliable plate only)); [[Afatinib (drug)]] (+0.58, EGFR/ERBB inhibitor); [[Almonertinib (mesylate) (drug)]] (+0.57, EGFR/ERBB inhibitor); [[Radotinib (drug)]] (+0.55, Other TK inhibitor); [[Elimusertib hydrochloride (drug)]] (+0.52, unclear); [[Regorafenib (drug)]] (+0.52, Multi-TK inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

None: no gene was found to set how the cells fare under it.

### Its targets: what acting on them probably does

*Drug-target arrows of the compound classes it belongs to (compounds sharing a listed target and mechanism; one molecule counts once, under all its names): the target → a gene whose level those compounds move. A row that names several targets is one test: the compounds share them all, and any of them could be the cause. 4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Its target | Gene it moves | This drug | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|---|
| KDR | [[PPARD]] | does not move it that way (the class's other compounds do) | B | KDR activity raises PPARD's level | compounds that target KDR: 5 of 8 lower it (Cabozantinib, Ponatinib, Regorafenib, Sulfatinib, Sunitinib) | 62% of the class's compounds vs 6.2% of all compounds | 0.036 | ⚠ off-target possible; 5 compounds; artifact flags |
| KDR | [[DNAJB6]] | does not move it that way (the class's other compounds do) | B | KDR activity raises DNAJB6's level | compounds that target KDR: 3 of 8 lower it (Cabozantinib, Ponatinib, c-Kit-IN-1) | 38% of the class's compounds vs 1.7% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| KDR | [[DUSP10]] | does not move it that way (the class's other compounds do) | B | KDR activity raises DUSP10's level | compounds that target KDR: 4 of 8 lower it (Cabozantinib, Ponatinib, Sunitinib, c-Kit-IN-1) | 50% of the class's compounds vs 4.5% of all compounds | 0.077 | ⚠ off-target possible; 4 compounds; artifact flags |
| KDR | [[PGLS-DT]] | does not move it that way (the class's other compounds do) | B | KDR activity lowers PGLS-DT's level | compounds that target KDR: 4 of 8 raise it (Cabozantinib, Ponatinib, Sunitinib, c-Kit-IN-1) | 50% of the class's compounds vs 4.5% of all compounds | 0.077 | ⚠ off-target possible; 4 compounds; artifact flags |

## Data

- `tables/drugs.parquet` — drug == "Vandetanib"
- `tables/drugdoses.parquet` — dd in 1072, 1073, 1074
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
