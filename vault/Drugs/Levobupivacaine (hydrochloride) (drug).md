---
drug: "Levobupivacaine (hydrochloride)"
type: "drug"
salt_base: "Levobupivacaine"
targets: "SCN5A"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 9
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Levobupivacaine (hydrochloride)

*unclear (inhibitor/antagonist) · targets: SCN5A · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 1 / 2 / 9; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): none.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.27 / 0.38.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:F1 | 0 / 1 | — | +0.40 | -0.0/+0.3/-1.1 | — |
| 0.5 µM | [[Plate 08]]:F1 | 1 / 1 | — | -0.01 | +0.1/+0.3/+0.1 | — |
| 5 µM | [[Plate 09]]:F1 | 8 / 1 | — | +0.02 | -0.4/-0.3/-0.6 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (1 gene, none with an alert): [[CCDC40]] 1.33× (z +3.2, 11/46 lines)

**5 µM** (8 genes, none with an alert): [[CCDC40]] 1.49× (z +4.2, 17/46 lines), [[EVA1C]] 1.38× (z +4.0, 11/33 lines), [[ZNF577]] 1.34× (z +3.7, 9/36 lines), [[PLEKHS1]] 1.54× (z +3.3, 1/23 lines), [[ENSG00000289694]] 1.32× (z +3.2, 6/44 lines), [[CADM4]] 1.27× (z +3.1, 3/41 lines), [[ARMC2]] 1.20× (z +2.9, 4/46 lines), [[ENSG00000250917]] 1.25× (z +2.8, 8/47 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[LINC01033]] 0.642× (z -3.9, 7/41 lines)

**0.5 µM** (1 gene, none with an alert): [[ENSG00000230021]] 0.798× (z -3.0, 11/48 lines)

**5 µM** (1 gene, none with an alert): [[TBP]] 0.817× (z -4.4, 11/47 lines)

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
| 5 µM | [[HEC-1-A (line)]] (-3.2) | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: only 9 significant genes. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar.*

- [[Lactate (calcium) (drug)]] (+0.58, unclear); [[Filgotinib (drug)]] (+0.49, JAK/STAT inhibitor); [[Rosiglitazone (drug)]] (+0.47, unclear); [[Sodium Salicylate (drug)]] (+0.46, Cyclooxygenase inhibitor); [[Isocorydine (drug)]] (+0.45, unclear); [[Bimatoprost (drug)]] (+0.43, unclear); [[Mifepristone (drug)]] (+0.43, unclear); [[Atazanavir (sulfate) (drug)]] (+0.43, unclear)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Levobupivacaine (hydrochloride)"
- `tables/drugdoses.parquet` — dd in 615, 616, 617
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
