---
drug: "Resveratrol"
type: "drug"
salt_base: "Resveratrol"
targets: "SIRT1"
moa_fine: "unclear"
moa_broad: "unclear"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 18
tags: ["drug", "moa/unclear"]
generated_by: "tahoemap"
---

# Resveratrol

*unclear (unclear) · targets: SIRT1 · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 5 / 6 / 18; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.23 / 0.30.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:D2 | 4 / 1 | — | -0.55 | -0.9/-1.1/-0.6 | — |
| 0.5 µM | [[Plate 05]]:D2 | 3 / 3 | — | -0.07 | +0.2/-0.8/-0.6 | — |
| 5 µM | [[Plate 14]]:D2 | 9 / 9 | 0.624 | +0.02 | -0.2/-0.7/-0.1 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (4 genes, none with an alert): [[ENSG00000287562]] 1.57× (z +4.4, 11/40 lines), [[ELAVL3]] 1.38× (z +3.2, 0/38 lines), [[ARHGAP20]] 1.44× (z +3.1, 0/12 lines), [[MGAM2]] 1.43× (z +3.1, 2/15 lines)

**0.5 µM** (3 genes, none with an alert): [[NCDN]] 1.33× (z +3.4, 5/44 lines), [[KMT2B]] 1.23× (z +3.4, 15/49 lines), [[KDM6B]] 1.29× (z +3.3, 25/49 lines)

**5 µM** (9 genes, none with an alert): [[CYP1B1]] 1.48× (z +3.8, 19/20 lines), [[ENSG00000228434]] 1.23× (z +3.6, 4/48 lines), [[ENSG00000260729]] 1.24× (z +3.5, 23/47 lines), [[ANKHD1-EIF4EBP3]] 1.23× (z +3.4, 11/48 lines), [[SMIM19]] 1.24× (z +3.3, 13/48 lines), [[SLC25A20]] 1.20× (z +3.2, 3/46 lines), [[PINX1-1]] 1.25× (z +3.0, 1/43 lines), [[RMDN2-AS1]] 1.34× (z +3.0, 6/31 lines), [[BMF]] 1.25× (z +2.7, 1/42 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[PIF1]] 0.809× (z -2.6, 8/45 lines)

**0.5 µM** (3 genes, none with an alert): [[ENSG00000285696]] 0.739× (z -3.8, 11/43 lines), [[CFAP97]] 0.779× (z -3.8, 23/48 lines), [[LINC01881]] 0.810× (z -2.8, 10/48 lines)

**5 µM** (9 genes, none with an alert): [[ENSG00000289084]] 0.826× (z -3.7, 8/44 lines), [[NDNF]] 0.772× (z -3.6, 3/22 lines), [[SRMS]] 0.670× (z -3.6, 6/31 lines), [[B3GALT5]] 0.811× (z -3.4, 9/21 lines), [[DPY19L2P1]] 0.824× (z -3.3, 8/22 lines), [[TUBB3]] 0.819× (z -3.3, 4/47 lines), [[FAM3B]] 0.776× (z -3.2, 3/32 lines), [[IGSF9]] 0.746× (z -3.2, 4/30 lines), [[CHAC1]] 0.764× (z -3.2, 9/37 lines)

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

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar.*

- [[MK-3903 (drug)]] (+0.78, unclear); [[ULK-101 (drug)]] (+0.71, unclear); [[Rapamycin (drug)]] (+0.69, MTOR inhibitor); [[AZD1390 (drug)]] (+0.64, unclear); [[Temsirolimus (drug)]] (+0.64, MTOR inhibitor); [[AZD-8055 (drug)]] (+0.57, MTOR inhibitor); [[18β-Glycyrrhetinic acid (drug)]] (+0.56, unclear); [[Sodium Salicylate (drug)]] (+0.56, Cyclooxygenase inhibitor)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Resveratrol"
- `tables/drugdoses.parquet` — dd in 884, 885, 886
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
