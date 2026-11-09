---
drug: "Temuterkib"
type: "drug"
salt_base: "Temuterkib"
targets: ""
moa_fine: "Other MAPK inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "0.05"
max_sig_genes: 3
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Temuterkib

*Other MAPK inhibitor (inhibitor/antagonist) · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 3 / 1 / 0; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): none.
> Signature similarity between consecutive doses (low–mid / mid–high): -0.19 / -0.31.
> Flags by dose: - / noisy plate (z scaled) / plate-row cell shift; noisy plate (z scaled).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:C1 | 2 / 1 | — | -0.03 | +1.8/+0.0/+0.4 | — |
| 0.5 µM | [[Plate 02]]:C1 | 1 / 0 | — | -0.57 | +0.7/+1.1/+1.2 | noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:C1 | 0 / 0 | — | +0.69 | +0.6/+0.2/-0.7 | plate-row cell shift; noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (2 genes, none with an alert): [[PXN-AS1]] 1.67× (z +5.2, 8/44 lines), [[UBR7]] 1.22× (z +3.4, 4/48 lines)

**0.5 µM** (1 gene, none with an alert): [[SLCO1B3]] 1.30× (z +3.3, 0/20 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[VEGFA]] 0.808× (z -3.0, 16/46 lines)

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
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: only 3 significant genes. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 3 next most similar without an alert.*

- [[Oxaliplatin (drug)]] (+0.77, DNA synthesis/repair inhibitor, ⚠ only 7 significant genes); [[Pyridoxine (hydrochloride) (drug)]] (+0.70, unclear); [[Adenine (drug)]] (+0.69, unclear); [[Folic acid (drug)]] (+0.69, unclear); [[MK-8353 (drug)]] (+0.68, Other MAPK inhibitor); [[Trifluridine (drug)]] (+0.66, DNA synthesis/repair inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Balsalazide (sodium hydrate) (drug)]] (+0.64, JAK/STAT inhibitor, ⚠ only 9 significant genes); [[Retinoic acid (drug)]] (+0.60, Retinoic receptor agonist); [[Busulfan (drug)]] (+0.59, DNA synthesis/repair inhibitor); [[Berbamine (drug)]] (+0.58, unclear); [[Pemetrexed (drug)]] (+0.57, DNA synthesis/repair inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[ADIRF]] | 5 µM | B | ADIRF activity lowers the cells' numbers under Temuterkib 5 µM (makes them more sensitive) | lines that do not express ADIRF (31) vs lines expressing it (17) | the lines without ADIRF: 1.14× the cells of the other lines | 0.0995 | ⚠ within organs, on part of the lines; also absent: CEACAM6, FGFBP1, KRT6A |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Temuterkib"
- `tables/drugdoses.parquet` — dd in 991, 992, 993
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
