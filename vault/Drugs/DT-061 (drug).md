---
drug: "DT-061"
type: "drug"
salt_base: "DT-061"
targets: ""
moa_fine: "unclear"
moa_broad: "activator/agonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 33
tags: ["drug", "moa/activator_agonist"]
generated_by: "tahoemap"
---

# DT-061

*unclear (activator/agonist) · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 0 / 0 / 33; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.32 / -0.46.
> Flags by dose: - / noisy plate (z scaled) / noisy plate (z scaled).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:G7 | 0 / 0 | — | -0.47 | -0.0/+0.1/-0.5 | — |
| 0.5 µM | [[Plate 02]]:G7 | 0 / 0 | — | +0.49 | -0.8/-1.1/-1.1 | noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:G7 | 14 / 19 | — | -0.50 | +1.5/+0.9/+1.1 | noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**5 µM** (14 genes, none with an alert; 12 shown): [[CYP1B1]] 2.99× (z +3.7, 15/18 lines), [[ABCB8]] 1.46× (z +3.3, 3/41 lines), [[CNP]] 1.59× (z +3.2, 11/45 lines), [[TRAPPC2]] 1.32× (z +3.2, 6/44 lines), [[PFN2]] 1.61× (z +3.2, 16/42 lines), [[PXMP2]] 1.83× (z +3.1, 4/31 lines), [[PLAC8]] 1.75× (z +3.1, 6/20 lines), [[HAUS8]] 1.49× (z +3.0, 2/41 lines), [[NAA40]] 1.42× (z +3.0, 2/42 lines), [[NQO1]] 1.77× (z +2.9, 20/43 lines), [[UGT1A6]] 1.69× (z +2.9, 2/12 lines), [[TRAFD1]] 1.34× (z +2.9, 2/44 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**5 µM** (19 genes, none with an alert; 12 shown): [[ENSG00000288542]] 0.651× (z -3.6, 7/35 lines), [[TEC]] 0.687× (z -3.5, 13/38 lines), [[EFL1]] 0.691× (z -3.5, 18/46 lines), [[LRCH1]] 0.756× (z -3.5, 15/47 lines), [[ACVR1]] 0.666× (z -3.2, 20/47 lines), [[CEP170]] 0.774× (z -3.2, 12/43 lines), [[ZEB1]] 0.727× (z -3.0, 13/38 lines), [[PLEKHM1]] 0.729× (z -3.0, 13/45 lines), [[RASA2]] 0.714× (z -3.0, 16/47 lines), [[BACE2]] 0.756× (z -3.0, 16/38 lines), [[LRRC8C]] 0.666× (z -2.9, 11/38 lines), [[SNX9]] 0.762× (z -2.9, 18/47 lines)

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
| 5 µM | [[C32 (line)]] (-4.2), [[SW480 (line)]] (-3.5), [[CHP-212 (line)]] (-3.2) | [[HOP62 (line)]] (1.38), [[H4 (line)]] (1.37), [[NCI-H1573 (line)]] (1.29), [[SW 1088 (line)]] (1.29) · weakest: [[SNU-1 (line)]] (0.382), [[NCI-H661 (line)]] (0.539), [[SW480 (line)]] (0.562) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[AZD-7648 (drug)]] (+0.73, DNA synthesis/repair inhibitor); [[XRK3F2 (drug)]] (+0.73, unclear); [[LY-2584702 (tosylate salt) (drug)]] (+0.72, MTOR inhibitor, ⚠ vector dose flagged: toxic); [[Capmatinib (drug)]] (+0.71, EGFR/ERBB inhibitor); [[BI-78D3 (drug)]] (+0.69, Other MAPK inhibitor); [[9-ING-41 (drug)]] (+0.67, GSK3 inhibitor); [[Canagliflozin (drug)]] (+0.65, Glucose transporter inhibitor); [[olaparib (drug)]] (+0.58, DNA synthesis/repair inhibitor, ⚠ only 3 significant genes); [[OTS514 (drug)]] (+0.57, Other MAPK inhibitor); [[Alpelisib (drug)]] (+0.55, PI3K/AKT inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[ENSG00000258919]] | 5 µM | B | ENSG00000258919 activity lowers the cells' numbers under DT-061 5 µM (makes them more sensitive) | lines that do not express ENSG00000258919 (23) vs lines expressing it (25) | the lines without ENSG00000258919: 1.19× the cells of the other lines | 0.0995 | ⚠ within organs, on part of the lines; also absent: LINC02320, ENSG00000266088, DIO3OS |
| [[SDC3]] | 5 µM | C | SDC3 activity raises the cells' numbers under DT-061 5 µM (protects the cells) | lines that do not express SDC3 (4) vs lines expressing it (44) | the lines without SDC3: 0.71× the cells of the other lines | 0.026 | ⚠ few lines (4 vs 46); across organs |
| [[SEMA4G]] | 5 µM | C | SEMA4G activity lowers the cells' numbers under DT-061 5 µM (makes them more sensitive) | lines that do not express SEMA4G (6) vs lines expressing it (42) | the lines without SEMA4G: 1.28× the cells of the other lines | 0.087 | ⚠ tissue-confounded; across organs; also absent: SLC2A9, HMGA2; maybe low, not absent |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "DT-061"
- `tables/drugdoses.parquet` — dd in 308, 309, 310
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
