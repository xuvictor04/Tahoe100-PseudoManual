---
drug: "Lapatinib ditosylate"
type: "drug"
salt_base: "Lapatinib ditosylate"
targets: "EGFR, ERBB2"
moa_fine: "EGFR/ERBB inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 9
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Lapatinib ditosylate

*EGFR/ERBB inhibitor (inhibitor/antagonist) · targets: EGFR, ERBB2 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 9 / 9 / 3; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): none.
> Signature similarity between consecutive doses (low–mid / mid–high): -0.51 / -0.28.
> Flags by dose: - / noisy plate (z scaled) / noisy plate (z scaled).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:A11 | 8 / 1 | — | -0.09 | +0.7/+0.6/+0.7 | — |
| 0.5 µM | [[Plate 02]]:A11 | 1 / 8 | — | +0.28 | +0.1/-0.6/-1.0 | noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:A11 | 3 / 0 | — | +1.08 | +1.1/+0.9/+0.2 | noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (8 genes, none with an alert): [[PSENEN]] 1.46× (z +3.4, 12/45 lines), [[ENSG00000286048]] 1.48× (z +3.2, 2/37 lines), [[CDKN2B]] 1.24× (z +3.1, 2/36 lines), [[CFB]] 1.45× (z +3.0, 12/28 lines), [[RAD51C]] 1.27× (z +3.0, 7/46 lines), [[PM20D2]] 1.23× (z +3.0, 3/44 lines), [[HSPB8]] 1.32× (z +2.9, 7/47 lines), [[PWWP3B]] 1.60× (z +2.9, 0/14 lines)

**0.5 µM** (1 gene, none with an alert): [[ESYT2]] 1.31× (z +3.1, 29/48 lines)

**5 µM** (3 genes, none with an alert): [[VDAC2]] 1.48× (z +3.7, 21/48 lines), [[RPL6]] 1.69× (z +3.0, 22/48 lines), [[LDLR]] 1.50× (z +3.0, 16/46 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[IKZF5]] 0.820× (z -2.9, 11/48 lines)

**0.5 µM** (8 genes, none with an alert): [[ZNF804A]] 0.658× (z -3.6, 1/17 lines), [[ZNF677]] 0.408× (z -3.6, 0/9 lines), [[MACC1]] 0.649× (z -3.4, 0/16 lines), [[USP9Y]] 0.768× (z -3.1, 0/18 lines), [[SNCA]] 0.749× (z -3.0, 0/19 lines), [[ENSG00000267284]] 0.720× (z -3.0, 0/16 lines), [[GALNT13]] 0.764× (z -3.0, 0/17 lines), [[LINC02864]] 0.715× (z -3.0, 0/12 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | [[Module 179]] (-2.0) |
| 0.5 µM | — | — |
| 5 µM | — | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | [[NCI-H661 (line)]] (-3.6) | — |
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: only 9 significant genes. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 3 next most similar without an alert.*

- [[Tucatinib (drug)]] (+0.81, EGFR/ERBB inhibitor); [[Lucanthone (drug)]] (+0.65, unclear); [[Methyl aminolevulinate (hydrochloride) (drug)]] (+0.62, unclear, ⚠ only 3 significant genes); [[palbociclib (drug)]] (+0.61, CDK inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Ranolazine (drug)]] (+0.60, unclear); [[ML264 (drug)]] (+0.60, unclear, ⚠ only 5 significant genes); [[Clopidogrel (drug)]] (+0.59, unclear); [[Erlotinib (drug)]] (+0.58, EGFR/ERBB inhibitor); [[Benproperine (phosphate) (drug)]] (+0.58, unclear); [[Fenofibrate (drug)]] (+0.57, unclear); [[Anethole trithione (drug)]] (+0.57, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 44 arrows, 44 of them with an alert ⚠; grade A 0, B 17, C 27. Shown: the 15 strongest; 29 more arrows (29 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[AHR]] | 0.5 µM | B | AHR activity raises the cells' numbers under Lapatinib ditosylate 0.5 µM (protects the cells) | lines that do not express AHR (7) vs lines expressing it (41) | the lines without AHR: 0.77× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000283321, VDR, GPR39 |
| [[IMPA1P1]] | 0.5 µM | B | IMPA1P1 activity raises the cells' numbers under Lapatinib ditosylate 0.5 µM (protects the cells) | lines that do not express IMPA1P1 (6) vs lines expressing it (42) | the lines without IMPA1P1: 0.83× the cells of the other lines | 0.038 | ⚠ within organs, on part of the lines; also absent: ENSG00000229195; maybe low, not absent |
| [[KHDRBS3]] | 0.5 µM | B | KHDRBS3 activity raises the cells' numbers under Lapatinib ditosylate 0.5 µM (protects the cells) | lines that do not express KHDRBS3 (11) vs lines expressing it (37) | the lines without KHDRBS3: 0.86× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; also absent: AHR, STC2 |
| [[GPR39]] | 0.5 µM | B | GPR39 activity raises the cells' numbers under Lapatinib ditosylate 0.5 µM (protects the cells) | lines that do not express GPR39 (11) vs lines expressing it (37) | the lines without GPR39: 0.84× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: MET, AHR, ABCC3 |
| [[SLC2A9]] | 0.5 µM | B | SLC2A9 activity raises the cells' numbers under Lapatinib ditosylate 0.5 µM (protects the cells) | lines that do not express SLC2A9 (6) vs lines expressing it (42) | the lines without SLC2A9: 0.80× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: VDR, SEMA4G, TBC1D8B; maybe low, not absent |
| [[PRKCA]] | 0.5 µM | B | PRKCA activity raises the cells' numbers under Lapatinib ditosylate 0.5 µM (protects the cells) | lines that do not express PRKCA (5) vs lines expressing it (43) | the lines without PRKCA: 0.79× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: TMEM51, ITGA2-AS1; maybe low, not absent |
| [[ENSG00000251537]] | 0.5 µM | B | ENSG00000251537 activity raises the cells' numbers under Lapatinib ditosylate 0.5 µM (protects the cells) | lines that do not express ENSG00000251537 (9) vs lines expressing it (39) | the lines without ENSG00000251537: 0.87× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: FBXW10B, PCED1B, NHS; maybe low, not absent |
| [[ALDH3B1]] | 0.5 µM | B | ALDH3B1 activity raises the cells' numbers under Lapatinib ditosylate 0.5 µM (protects the cells) | lines that do not express ALDH3B1 (9) vs lines expressing it (39) | the lines without ALDH3B1: 0.82× the cells of the other lines | 0.078 | ⚠ within organs, on part of the lines; also absent: NIBAN2, IER3, FOSL1; maybe low, not absent |
| [[ZNF544]] | 0.5 µM | B | ZNF544 activity raises the cells' numbers under Lapatinib ditosylate 0.5 µM (protects the cells) | lines that do not express ZNF544 (6) vs lines expressing it (42) | the lines without ZNF544: 0.88× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: LPIN3 |
| [[GPRC5D-AS1]] | 0.5 µM | B | GPRC5D-AS1 activity raises the cells' numbers under Lapatinib ditosylate 0.5 µM (protects the cells) | lines that do not express GPRC5D-AS1 (5) vs lines expressing it (43) | the lines without GPRC5D-AS1: 0.75× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: S100A6, LGALS3BP, NMI; maybe low, not absent |
| [[ENSG00000283321]] | 0.5 µM | B | ENSG00000283321 activity raises the cells' numbers under Lapatinib ditosylate 0.5 µM (protects the cells) | lines that do not express ENSG00000283321 (7) vs lines expressing it (41) | the lines without ENSG00000283321: 0.82× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: AHR, PSMB8, CXCL2 |
| [[ENSG00000258919]] | 0.5 µM | B | ENSG00000258919 activity raises the cells' numbers under Lapatinib ditosylate 0.5 µM (protects the cells) | lines that do not express ENSG00000258919 (23) vs lines expressing it (25) | the lines without ENSG00000258919: 0.83× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: LINC02320, ENSG00000266088, DIO3OS |
| [[ITGA2]] | 0.5 µM | B | ITGA2 activity raises the cells' numbers under Lapatinib ditosylate 0.5 µM (protects the cells) | lines that do not express ITGA2 (11) vs lines expressing it (37) | the lines without ITGA2: 0.86× the cells of the other lines | 0.082 | ⚠ within organs, on part of the lines; also absent: GPR39, ATXN1-AS1, MET |
| [[NIPAL1]] | 0.5 µM | B | NIPAL1 activity raises the cells' numbers under Lapatinib ditosylate 0.5 µM (protects the cells) | lines that do not express NIPAL1 (5) vs lines expressing it (43) | the lines without NIPAL1: 0.77× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; also absent: SLC18B1, AHR, RALGPS2; maybe low, not absent |
| [[ARL14EPL]] | 0.5 µM | B | ARL14EPL activity raises the cells' numbers under Lapatinib ditosylate 0.5 µM (protects the cells) | lines that do not express ARL14EPL (11) vs lines expressing it (37) | the lines without ARL14EPL: 0.85× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: MAMLD1, ENSG00000243797, ENSG00000253496; maybe low, not absent |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Lapatinib ditosylate"
- `tables/drugdoses.parquet` — dd in 603, 604, 605
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
