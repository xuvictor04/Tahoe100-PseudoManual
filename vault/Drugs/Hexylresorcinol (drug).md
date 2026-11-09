---
drug: "Hexylresorcinol"
type: "drug"
salt_base: "Hexylresorcinol"
targets: ""
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 15
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Hexylresorcinol

*unclear (inhibitor/antagonist) · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 0 / 10 / 15; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.08 / 0.23.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:G2 | 0 / 0 | — | +0.21 | -0.4/-0.6/-1.0 | — |
| 0.5 µM | [[Plate 05]]:G2 | 1 / 9 | — | +0.23 | +1.6/+1.9/+0.3 | — |
| 5 µM | [[Plate 14]]:G2 | 6 / 9 | 0.857 | +0.46 | -0.6/-0.7/-0.6 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (1 gene, none with an alert): [[DDIAS]] 1.24× (z +2.7, 3/46 lines)

**5 µM** (6 genes, none with an alert): [[ALOXE3]] 1.31× (z +3.7, 2/40 lines), [[DUSP8]] 1.31× (z +3.6, 15/44 lines), [[CD83]] 1.31× (z +3.2, 12/44 lines), [[N4BP3]] 1.21× (z +3.1, 8/42 lines), [[ENSG00000236453]] 1.24× (z +2.9, 2/26 lines), [[TNFRSF9]] 1.21× (z +2.7, 4/27 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (9 genes, none with an alert): [[SLC41A3]] 0.805× (z -4.3, 8/46 lines), [[ST6GALNAC6]] 0.792× (z -4.1, 12/48 lines), [[DPH1]] 0.774× (z -3.9, 8/48 lines), [[DMWD]] 0.800× (z -3.6, 9/48 lines), [[MTARC2]] 0.807× (z -3.3, 11/39 lines), [[ENSG00000284773]] 0.695× (z -3.3, 5/42 lines), [[TOR4A]] 0.794× (z -3.1, 2/33 lines), [[SHROOM1]] 0.753× (z -3.1, 4/42 lines), [[GAA]] 0.813× (z -3.1, 3/46 lines)

**5 µM** (9 genes, none with an alert): [[LINC01504]] 0.749× (z -4.7, 19/48 lines), [[FKBP7]] 0.762× (z -3.5, 12/40 lines), [[CASC11]] 0.813× (z -3.5, 3/34 lines), [[RHOBTB2]] 0.810× (z -3.3, 5/47 lines), [[C10orf95-AS1]] 0.780× (z -3.3, 5/42 lines), [[ST6GALNAC3]] 0.822× (z -3.3, 5/30 lines), [[CCND2]] 0.827× (z -3.2, 10/11 lines), [[DHCR7]] 0.809× (z -3.2, 10/45 lines), [[MYO16-AS1]] 0.815× (z -2.8, 4/25 lines)

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

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Goserelin (acetate) (drug)]] (+0.68, unclear); [[Pravastatin (sodium) (drug)]] (+0.63, unclear); [[Capivasertib (drug)]] (+0.62, PI3K/AKT inhibitor, ⚠ only 5 significant genes); [[Asciminib (drug)]] (+0.58, Other TK inhibitor); [[Ranolazine (drug)]] (+0.57, unclear); [[Cloxacillin (sodium) (drug)]] (+0.54, unclear); [[Dihydroartemisinin (drug)]] (+0.53, unclear); [[Salicylic acid (drug)]] (+0.52, Cyclooxygenase inhibitor, ⚠ only 3 significant genes); [[Tomivosertib (drug)]] (+0.52, Protein synthesis inhibitor); [[Fluvoxamine (drug)]] (+0.52, unclear)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Hexylresorcinol"
- `tables/drugdoses.parquet` — dd in 525, 526, 527
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
