---
drug: "ML264"
type: "drug"
salt_base: "ML264"
targets: "KLF5"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "0.05"
max_sig_genes: 5
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# ML264

*unclear (inhibitor/antagonist) · targets: KLF5 · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 5 / 0 / 0; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): none.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.09 / -0.26.
> Flags by dose: - / noisy plate (z scaled) / plate-row cell shift; noisy plate (z scaled).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:C2 | 1 / 4 | — | -0.21 | +0.3/+0.1/+0.4 | — |
| 0.5 µM | [[Plate 02]]:C2 | 0 / 0 | — | +0.28 | +1.2/+1.3/+1.0 | noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:C2 | 0 / 0 | — | +0.77 | +0.6/+0.2/-0.8 | plate-row cell shift; noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[CFAP210]] 1.86× (z +3.2, 7/44 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (4 genes, none with an alert): [[ENSG00000289106]] 0.695× (z -3.9, 6/42 lines), [[DDX59]] 0.829× (z -3.6, 9/48 lines), [[NOXA1]] 0.738× (z -3.4, 4/37 lines), [[SLC66A3]] 0.819× (z -3.0, 3/46 lines)

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
| 5 µM | [[BT-474 (line)]] (-3.3) | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: only 5 significant genes. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] (+0.70, unclear); [[Lapatinib ditosylate (drug)]] (+0.60, EGFR/ERBB inhibitor, ⚠ only 9 significant genes); [[Cloxacillin (sodium) (drug)]] (+0.59, unclear); [[Tazarotene (drug)]] (+0.58, Retinoic receptor agonist); [[Aspirin (drug)]] (+0.57, Cyclooxygenase inhibitor, ⚠ only 3 significant genes); [[Allopurinol (drug)]] (+0.53, unclear); [[Malotilate (drug)]] (+0.52, unclear); [[Hesperidin (drug)]] (+0.52, unclear); [[Pentoxifylline (drug)]] (+0.51, unclear); [[Volasertib (drug)]] (+0.50, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[MTMR7]] | 5 µM | B | MTMR7 activity raises the cells' numbers under ML264 5 µM (protects the cells) | lines that do not express MTMR7 (16) vs lines expressing it (32) | the lines without MTMR7: 0.78× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; also absent: GAP43, NRXN1, LOXL3; maybe low, not absent |
| [[ENSG00000255723]], [[HSD17B11]] | 5 µM | C | ENSG00000255723, HSD17B11 activity raises the cells' numbers under ML264 5 µM (protects the cells) | lines that do not express ENSG00000255723, HSD17B11 (3) vs lines expressing them (45) | the lines without ENSG00000255723, HSD17B11: 0.71× the cells of the other lines | 0.082 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; co-occurs with ERBB2; co-absent genes |
| [[SDC3]] | 5 µM | C | SDC3 activity lowers the cells' numbers under ML264 5 µM (makes them more sensitive) | lines that do not express SDC3 (4) vs lines expressing it (44) | the lines without SDC3: 1.38× the cells of the other lines | 0.089 | ⚠ few lines (4 vs 46); across organs |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "ML264"
- `tables/drugdoses.parquet` — dd in 648, 649, 650
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
