---
drug: "Goserelin (acetate)"
type: "drug"
salt_base: "Goserelin"
targets: "GNRHR"
moa_fine: "unclear"
moa_broad: "activator/agonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 10
tags: ["drug", "moa/activator_agonist"]
generated_by: "tahoemap"
---

# Goserelin (acetate)

*unclear (activator/agonist) · targets: GNRHR · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 0 / 4 / 10; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.46 / 0.36.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:G8 | 0 / 0 | — | +0.55 | -0.7/+0.1/-0.9 | — |
| 0.5 µM | [[Plate 05]]:G8 | 2 / 2 | — | +0.52 | +0.9/+1.8/+0.1 | — |
| 5 µM | [[Plate 14]]:G8 | 2 / 8 | 0.837 | +0.24 | -2.1/-0.9/-1.4 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (2 genes, none with an alert): [[EIF2AK1]] 1.34× (z +4.6, 39/49 lines), [[WBP11]] 1.25× (z +3.4, 28/49 lines)

**5 µM** (2 genes, none with an alert): [[ENSG00000269967]] 1.27× (z +3.0, 2/48 lines), [[RPS10-NUDT3]] 1.30× (z +3.0, 6/47 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (2 genes, none with an alert): [[LINC00698]] 0.439× (z -4.2, 3/10 lines), [[ZNF860]] 0.743× (z -3.2, 3/31 lines)

**5 µM** (8 genes, none with an alert): [[ENSG00000260289]] 0.727× (z -4.0, 6/11 lines), [[TPRXL]] 0.727× (z -4.0, 3/14 lines), [[TFAP4]] 0.831× (z -3.4, 4/48 lines), [[CNPY4]] 0.799× (z -3.2, 5/47 lines), [[CCN1]] 0.819× (z -3.2, 12/41 lines), [[HENMT1]] 0.810× (z -3.1, 4/31 lines), [[CARD6]] 0.800× (z -3.1, 4/31 lines), [[LIMD2]] 0.776× (z -3.0, 5/41 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[Module 179]] (+3.1) | [[Module 060]] (-2.1) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[Capivasertib (drug)]] (+0.78, PI3K/AKT inhibitor, ⚠ only 5 significant genes); [[Tomivosertib (drug)]] (+0.73, Protein synthesis inhibitor); [[Ranolazine (drug)]] (+0.71, unclear); [[Gallic acid (drug)]] (+0.70, Cyclooxygenase inhibitor); [[Pravastatin (sodium) (drug)]] (+0.69, unclear); [[Hexylresorcinol (drug)]] (+0.68, unclear); [[Cloxacillin (sodium) (drug)]] (+0.66, unclear); [[Asciminib (drug)]] (+0.63, Other TK inhibitor); [[NVP-BHG712 (drug)]] (+0.62, unclear)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Goserelin (acetate)"
- `tables/drugdoses.parquet` — dd in 513, 514, 515
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
