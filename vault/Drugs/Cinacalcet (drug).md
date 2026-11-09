---
drug: "Cinacalcet"
type: "drug"
salt_base: "Cinacalcet"
targets: "CASR"
moa_fine: "unclear"
moa_broad: "activator/agonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 8
tags: ["drug", "moa/activator_agonist"]
generated_by: "tahoemap"
---

# Cinacalcet

*unclear (activator/agonist) · targets: CASR · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 0 / 4 / 8; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): none.
> Signature similarity between consecutive doses (low–mid / mid–high): -0.00 / -0.01.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:G3 | 0 / 0 | — | -0.53 | -0.7/-0.0/-0.1 | — |
| 0.5 µM | [[Plate 11]]:G3 | 3 / 1 | — | -0.30 | +0.6/+1.2/+0.7 | — |
| 5 µM | [[Plate 12]]:G3 | 8 / 0 | — | +0.50 | -0.6/-1.0/-0.6 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (3 genes, none with an alert): [[RING1]] 1.28× (z +4.2, 15/48 lines), [[SSX1]] 1.97× (z +3.0, 0/5 lines), [[TAP1]] 1.22× (z +3.0, 8/48 lines)

**5 µM** (8 genes, none with an alert): [[ENSG00000285650]] 1.46× (z +3.5, 1/46 lines), [[LINC01191]] 1.35× (z +3.1, 10/46 lines), [[SLCO5A1]] 1.24× (z +3.1, 5/42 lines), [[ZDHHC11]] 1.37× (z +3.1, 5/43 lines), [[ADAM32]] 1.25× (z +3.1, 5/46 lines), [[FAM151B]] 1.26× (z +2.9, 2/48 lines), [[MPP4]] 1.47× (z +2.9, 3/44 lines), [[ENSG00000229321]] 1.30× (z +2.7, 1/48 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (1 gene, none with an alert): [[PHC2-AS1]] 0.756× (z -3.0, 11/37 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | [[Module 045]] (-2.3) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: only 8 significant genes. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 3 next most similar without an alert.*

- [[Ivermectin (drug)]] (+0.67, unclear); [[Demeclocycline (drug)]] (+0.67, unclear); [[Rimonabant (drug)]] (+0.66, unclear, ⚠ only 7 significant genes); [[(S)-Crizotinib (drug)]] (+0.62, unclear); [[Esmolol (hydrochloride) (drug)]] (+0.59, unclear); [[Phenytoin (sodium) (drug)]] (+0.58, unclear, ⚠ only 7 significant genes); [[Cilostazol (drug)]] (+0.57, unclear); [[Balsalazide (sodium hydrate) (drug)]] (+0.56, JAK/STAT inhibitor, ⚠ only 9 significant genes); [[Dabrafenib (drug)]] (+0.55, RAF inhibitor); [[Finasteride (drug)]] (+0.54, unclear); [[Omeprazole (drug)]] (+0.53, unclear)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Cinacalcet"
- `tables/drugdoses.parquet` — dd in 266, 267, 268
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
