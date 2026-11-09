---
drug: "5-Fluorouracil"
type: "drug"
salt_base: "5-Fluorouracil"
targets: "TYMS"
moa_fine: "DNA synthesis/repair inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 7
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# 5-Fluorouracil

*DNA synthesis/repair inhibitor (inhibitor/antagonist) · targets: TYMS · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 0 / 7 / 5; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): none.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.29 / 0.37.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:G7 | 0 / 0 | — | -0.14 | -0.0/+0.6/+0.0 | — |
| 0.5 µM | [[Plate 11]]:G7 | 1 / 6 | — | +0.10 | +1.6/+1.0/+1.0 | — |
| 5 µM | [[Plate 12]]:G7 | 0 / 5 | — | +0.10 | +1.2/+0.4/+0.6 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (1 gene, none with an alert): [[APOBEC3A]] 1.48× (z +3.5, 8/38 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (6 genes, none with an alert): [[ZNG1E]] 0.802× (z -3.8, 3/46 lines), [[NSUN5P1]] 0.714× (z -3.3, 3/40 lines), [[TPTE2]] 0.784× (z -3.3, 11/46 lines), [[ENSG00000279712]] 0.658× (z -3.2, 9/22 lines), [[MRPS31P5-1]] 0.715× (z -3.2, 8/42 lines), [[TMEM11-DT]] 0.802× (z -3.0, 8/46 lines)

**5 µM** (5 genes, none with an alert): [[TPTE2]] 0.768× (z -3.6, 6/47 lines), [[ENSG00000255031]] 0.735× (z -3.2, 7/42 lines), [[MINAR1]] 0.723× (z -3.1, 4/41 lines), [[ENSG00000285755]] 0.730× (z -3.0, 5/37 lines), [[DLG2]] 0.809× (z -2.8, 14/46 lines)

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

⚠ This drug's own vector: only 7 significant genes. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 4 next most similar without an alert.*

- [[Sinomenine (drug)]] (+0.65, unclear); [[Ranolazine (drug)]] (+0.58, unclear); [[Allopurinol (drug)]] (+0.56, unclear); [[Uridine (drug)]] (+0.54, unclear, ⚠ only 6 significant genes); [[Sacubitril_Valsartan (drug)]] (+0.51, unclear, ⚠ only 1 significant gene); [[Artemether (drug)]] (+0.51, unclear, ⚠ only 7 significant genes); [[Clopidogrel (drug)]] (+0.50, unclear); [[Verapamil (drug)]] (+0.50, unclear, ⚠ only 5 significant genes); [[Quinidine (15% dihydroquinidine) (drug)]] (+0.49, unclear); [[Hesperidin (drug)]] (+0.48, unclear); [[Tazarotene (drug)]] (+0.48, Retinoic receptor agonist); [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] (+0.46, unclear)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "5-Fluorouracil"
- `tables/drugdoses.parquet` — dd in 15, 16, 17
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
