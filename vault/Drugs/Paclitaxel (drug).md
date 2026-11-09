---
drug: "Paclitaxel"
type: "drug"
salt_base: "Paclitaxel"
targets: ""
moa_fine: "Microtubule inhibitor"
moa_broad: "unclear"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 3
tags: ["drug", "moa/unclear"]
generated_by: "tahoemap"
---

# Paclitaxel

*Microtubule inhibitor (unclear) · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 0 / 0 / 3; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): none.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.14 / 0.13.
> Flags by dose: - / noisy plate (z scaled) / plate-row cell shift; noisy plate (z scaled).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:C9 | 0 / 0 | — | +0.25 | -1.2/-1.4/-0.9 | — |
| 0.5 µM | [[Plate 02]]:C9 | 0 / 0 | — | +0.79 | -0.4/+0.3/-0.0 | noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:C9 | 1 / 2 | — | +1.73 | +0.3/+0.5/-1.2 | plate-row cell shift; noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**5 µM** (1 gene, none with an alert): [[TUBA1A]] 1.91× (z +3.5, 8/38 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**5 µM** (2 genes, none with an alert): [[ADGRE5]] 0.676× (z -3.0, 9/41 lines), [[CASC19]] 0.666× (z -2.9, 2/20 lines)

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
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[LOX-IMVI (line)]] (-4.6), [[RKO (line)]] (-4.4), [[NCI-H1792 (line)]] (-3.9) | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: only 3 significant genes. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[Fenofibrate (drug)]] (+0.78, unclear); [[Lucanthone (drug)]] (+0.77, unclear); [[Encorafenib (drug)]] (+0.76, RAF inhibitor); [[Benproperine (phosphate) (drug)]] (+0.76, unclear); [[Erlotinib (drug)]] (+0.76, EGFR/ERBB inhibitor); [[Anethole trithione (drug)]] (+0.74, unclear); [[Rutin (trihydrate) (drug)]] (+0.73, unclear); [[Pentagastrin (drug)]] (+0.70, unclear, ⚠ only 9 significant genes); [[Tucatinib (drug)]] (+0.70, EGFR/ERBB inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 4 arrows, 4 of them with an alert ⚠; grade A 0, B 1, C 3.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[SPTBN2]] | 5 µM | B | SPTBN2 activity lowers the cells' numbers under Paclitaxel 5 µM (makes them more sensitive) | lines that do not express SPTBN2 (9) vs lines expressing it (39) | the lines without SPTBN2: 1.31× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; also absent: CCDC88C, HID1, ASS1; maybe low, not absent |
| [[RAB11FIP1]] | 5 µM | C | RAB11FIP1 activity lowers the cells' numbers under Paclitaxel 5 µM (makes them more sensitive) | lines that do not express RAB11FIP1 (3) vs lines expressing it (45) | the lines without RAB11FIP1: 1.55× the cells of the other lines | 0.097 | ⚠ few lines (3 vs 47); across organs; also absent: PTPN3, ZFHX2 |
| [[ENSG00000240571]] | 5 µM | C | ENSG00000240571's natural level raises the cells' numbers under Paclitaxel 5 µM (protects the cells) | ENSG00000240571's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.71 | 0.250 over the table, 0.017 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| [[BCO2]] | 5 µM | C | BCO2's natural level raises the cells' numbers under Paclitaxel 5 µM (protects the cells) | BCO2's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.66 | 0.339 over the table, 0.086 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Paclitaxel"
- `tables/drugdoses.parquet` — dd in 768, 769, 770
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
