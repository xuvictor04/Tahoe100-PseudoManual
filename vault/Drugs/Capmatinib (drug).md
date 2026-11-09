---
drug: "Capmatinib"
type: "drug"
salt_base: "Capmatinib"
targets: "MET"
moa_fine: "EGFR/ERBB inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 135
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Capmatinib

*EGFR/ERBB inhibitor (inhibitor/antagonist) · targets: MET · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 0 / 11 / 135; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): -0.22 / -0.17.
> Flags by dose: - / noisy plate (z scaled) / noisy plate (z scaled).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:B5 | 0 / 0 | — | -0.13 | +0.5/+1.4/+0.3 | — |
| 0.5 µM | [[Plate 02]]:B5 | 1 / 10 | — | +0.32 | -1.0/-1.2/-1.3 | noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:B5 | 65 / 70 | — | -0.47 | -0.9/-0.1/-0.0 | noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (1 gene, none with an alert): [[RAB30]] 1.28× (z +3.0, 6/49 lines)

**5 µM** (65 genes, none with an alert; 12 shown): [[OLFML2A]] 2.18× (z +4.4, 3/23 lines), [[CFB]] 2.63× (z +3.9, 15/25 lines), [[TOB1]] 1.59× (z +3.8, 18/48 lines), [[GBP1]] 2.20× (z +3.8, 17/31 lines), [[GBP2]] 1.98× (z +3.8, 10/35 lines), [[PLAAT4]] 2.52× (z +3.6, 7/18 lines), [[IFIH1]] 1.65× (z +3.5, 20/45 lines), [[MPP7]] 1.46× (z +3.5, 1/26 lines), [[MUC1]] 2.53× (z +3.5, 9/22 lines), [[DMD]] 1.44× (z +3.5, 3/25 lines), [[DUSP16]] 1.35× (z +3.4, 7/46 lines), [[PGM2L1]] 1.33× (z +3.4, 5/43 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (10 genes, none with an alert): [[CD59]] 0.759× (z -3.5, 19/42 lines), [[GJB3]] 0.625× (z -3.0, 2/17 lines), [[NTSR1]] 0.694× (z -2.8, 6/23 lines), [[CDCP1]] 0.795× (z -2.7, 13/33 lines), [[PLEK2]] 0.711× (z -2.7, 6/31 lines), [[ELK3]] 0.796× (z -2.7, 12/45 lines), [[TM4SF1]] 0.738× (z -2.7, 12/37 lines), [[NT5E]] 0.734× (z -2.7, 13/35 lines), [[CD44]] 0.829× (z -2.6, 5/34 lines), [[ITGA2]] 0.765× (z -2.5, 12/38 lines)

**5 µM** (70 genes, none with an alert; 12 shown): [[ZFPM2-AS1]] 0.500× (z -5.7, 22/32 lines), [[SPRY4-AS1]] 0.353× (z -5.6, 31/44 lines), [[MYEOV]] 0.448× (z -4.8, 18/28 lines), [[NT5E]] 0.403× (z -4.7, 23/34 lines), [[HMGA2]] 0.480× (z -4.5, 23/39 lines), [[PHLDA1]] 0.446× (z -4.3, 32/43 lines), [[THSD4]] 0.524× (z -4.3, 21/30 lines), [[B4GALT6]] 0.590× (z -4.2, 16/35 lines), [[ITGB5]] 0.540× (z -4.2, 28/46 lines), [[ITGA2]] 0.469× (z -3.9, 29/37 lines), [[SNX9]] 0.704× (z -3.8, 25/48 lines), [[SLC4A7]] 0.625× (z -3.8, 18/45 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[Module 059]] (+2.1) | [[Module 174]] (-2.1) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[COLO 205 (line)]] (-4.3), [[CHP-212 (line)]] (-3.7) | [[AsPC-1 (line)]] (1.43), [[NCI-H23 (line)]] (1.30), [[MIA PaCa-2 (line)]] (1.28), [[LOX-IMVI (line)]] (1.27) · weakest: [[SNU-423 (line)]] (0.574), [[SHP-77 (line)]] (0.633), [[AN3 CA (line)]] (0.659) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar.*

- [[Binimetinib (drug)]] (+0.87, MEK inhibitor); [[AZD-7648 (drug)]] (+0.86, DNA synthesis/repair inhibitor); [[Elimusertib hydrochloride (drug)]] (+0.83, unclear); [[Trametinib (DMSO_TF solvate) (drug)]] (+0.82, MEK inhibitor); [[Cobimetinib (drug)]] (+0.80, MEK inhibitor); [[Alpelisib (drug)]] (+0.79, PI3K/AKT inhibitor); [[DT-061 (drug)]] (+0.71, unclear); [[XRK3F2 (drug)]] (+0.67, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[PDE3B]] | 5 µM | B | PDE3B activity lowers the cells' numbers under Capmatinib 5 µM (makes them more sensitive) | lines that do not express PDE3B (20) vs lines expressing it (28) | the lines without PDE3B: 1.26× the cells of the other lines | 0.073 | ⚠ within organs, on part of the lines; also absent: ENSG00000250049, MIR4458HG, ASB4 |
| [[MTMR7]] | 5 µM | B | MTMR7 activity lowers the cells' numbers under Capmatinib 5 µM (makes them more sensitive) | lines that do not express MTMR7 (16) vs lines expressing it (32) | the lines without MTMR7: 1.23× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; also absent: GAP43, NRXN1, LOXL3; maybe low, not absent |
| [[SDC3]] | 5 µM | C | SDC3 activity raises the cells' numbers under Capmatinib 5 µM (protects the cells) | lines that do not express SDC3 (4) vs lines expressing it (44) | the lines without SDC3: 0.62× the cells of the other lines | 0.004 | ⚠ few lines (4 vs 46); across organs |
| [[RRM2]] | 5 µM | C | RRM2 activity raises the cells' numbers under Capmatinib 5 µM (protects the cells) | lines that do not express RRM2 (3) vs lines expressing it (45) | the lines without RRM2: 0.67× the cells of the other lines | 0.093 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: CLSPN, E2F8, TCF19; maybe low, not absent |

### Its targets: what acting on them probably does

*Drug-target arrows of the compound classes it belongs to (compounds sharing a listed target and mechanism; one molecule counts once, under all its names): the target → a gene whose level those compounds move. A row that names several targets is one test: the compounds share them all, and any of them could be the cause. 1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Its target | Gene it moves | This drug | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|---|
| [[MET]] | [[TNFAIP1]] | does not move it that way (the class's other compounds do) | B | MET activity raises TNFAIP1's level | compounds that target MET: 3 of 4 lower it (Cabozantinib, Crizotinib / crizotinib, c-Kit-IN-1) | 75% of the class's compounds vs 3.4% of all compounds | 0.067 | ⚠ off-target possible; 3 compounds; artifact flags |

## Data

- `tables/drugs.parquet` — drug == "Capmatinib"
- `tables/drugdoses.parquet` — dd in 239, 240, 241
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
