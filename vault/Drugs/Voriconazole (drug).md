---
drug: "Voriconazole"
type: "drug"
salt_base: "Voriconazole"
targets: ""
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 6
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Voriconazole

*unclear (inhibitor/antagonist) · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 3 / 2 / 6; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): none.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.06 / 0.52.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:D7 | 2 / 1 | — | -0.12 | +0.4/+0.8/-0.5 | — |
| 0.5 µM | [[Plate 11]]:D7 | 1 / 1 | — | +0.45 | +0.6/+1.0/-0.3 | — |
| 5 µM | [[Plate 12]]:D7 | 0 / 6 | — | -0.08 | +0.8/+1.8/+0.0 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (2 genes, none with an alert): [[MT-RNR1]] 1.85× (z +3.5, 48/48 lines), [[DBN1]] 1.34× (z +3.5, 16/45 lines)

**0.5 µM** (1 gene, none with an alert): [[TUBB3]] 1.30× (z +3.0, 2/46 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[OSER1-DT]] 0.777× (z -3.2, 5/45 lines)

**0.5 µM** (1 gene, none with an alert): [[BAP1]] 0.823× (z -3.0, 5/48 lines)

**5 µM** (6 genes, none with an alert): [[MBD6]] 0.750× (z -4.0, 17/47 lines), [[MT-ND4L]] 0.591× (z -3.6, 38/48 lines), [[MTND2P28]] 0.619× (z -3.4, 10/46 lines), [[TNKS1BP1]] 0.786× (z -3.1, 17/48 lines), [[KDM6B]] 0.793× (z -3.0, 20/48 lines), [[MT-ND5]] 0.726× (z -3.0, 41/48 lines)

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

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 6 next most similar without an alert.*

- [[Relugolix (drug)]] (+0.71, unclear, ⚠ only 5 significant genes); [[CP21R7 (drug)]] (+0.61, GSK3 inhibitor, ⚠ only 1 significant gene); [[Pimitespib (drug)]] (+0.59, unclear); [[Altretamine (drug)]] (+0.57, DNA synthesis/repair inhibitor, ⚠ only 1 significant gene); [[Ornidazole (drug)]] (+0.56, unclear, ⚠ only 1 significant gene; no trustworthy dose (vector dose flagged: unreliable plate only)); [[Lumateperone (tosylate) (drug)]] (+0.55, unclear, ⚠ only 9 significant genes); [[Sinomenine (drug)]] (+0.53, unclear); [[Carbidopa (monohydrate) (drug)]] (+0.50, unclear, ⚠ no trustworthy dose (vector dose flagged: unreliable plate only; position not correctable)); [[Furosemide (drug)]] (+0.48, unclear); [[Methotrexate (drug)]] (+0.48, DNA synthesis/repair inhibitor); [[Omeprazole (sodium) (drug)]] (+0.46, unclear); [[Doxycycline (monohydrate) (drug)]] (+0.45, unclear); [[Ralimetinib dimesylate (drug)]] (+0.45, Other MAPK inhibitor); [[Rutin (trihydrate) (drug)]] (+0.41, unclear)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Voriconazole"
- `tables/drugdoses.parquet` — dd in 1099, 1100, 1101
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
