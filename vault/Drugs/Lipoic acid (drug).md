---
drug: "Lipoic acid"
type: "drug"
salt_base: "Lipoic acid"
targets: ""
moa_fine: "unclear"
moa_broad: "unclear"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 6
tags: ["drug", "moa/unclear"]
generated_by: "tahoemap"
---

# Lipoic acid

*unclear (unclear) · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 0 / 0 / 6; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): none.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.11 / 0.16.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:H6 | 0 / 0 | — | +0.32 | +0.2/-0.0/+0.5 | — |
| 0.5 µM | [[Plate 05]]:H6 | 0 / 0 | — | +0.59 | +0.1/+0.3/+0.1 | — |
| 5 µM | [[Plate 14]]:H6 | 6 / 0 | 0.672 | +0.19 | -0.5/-0.8/+0.6 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**5 µM** (6 genes, none with an alert): [[PDIA4]] 1.30× (z +4.4, 33/48 lines), [[FICD]] 1.33× (z +3.6, 7/48 lines), [[HYOU1]] 1.29× (z +3.5, 21/47 lines), [[HSPA5]] 1.38× (z +3.4, 30/48 lines), [[HSP90B1]] 1.22× (z +3.3, 24/48 lines), [[ENSG00000259543]] 1.25× (z +3.2, 4/45 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

No gene is significantly lowered at any dose.

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

⚠ This drug's own vector: only 6 significant genes. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 4 next most similar without an alert.*

- [[Salicylic acid (drug)]] (+0.69, Cyclooxygenase inhibitor, ⚠ only 3 significant genes); [[Pasireotide (acetate) (drug)]] (+0.62, unclear); [[Eplerenone (drug)]] (+0.60, unclear, ⚠ only 4 significant genes); [[Goserelin (acetate) (drug)]] (+0.55, unclear); [[Gallic acid (drug)]] (+0.54, Cyclooxygenase inhibitor); [[Indacaterol (maleate) (drug)]] (+0.49, Adrenoceptor agonist, ⚠ only 3 significant genes); [[Vortioxetine (drug)]] (+0.48, unclear, ⚠ vector dose flagged: toxic); [[Cloxacillin (sodium) (drug)]] (+0.46, unclear); [[Pravastatin (sodium) (drug)]] (+0.44, unclear); [[Belumosudil (mesylate) (drug)]] (+0.44, unclear); [[Hexylresorcinol (drug)]] (+0.44, unclear); [[Menadione (drug)]] (+0.43, unclear)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Lipoic acid"
- `tables/drugdoses.parquet` — dd in 624, 625, 626
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
