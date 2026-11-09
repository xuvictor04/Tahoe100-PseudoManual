---
drug: "L-Thyroxine (sodium salt pentahydrate)"
type: "drug"
salt_base: "L-Thyroxine"
targets: ""
moa_fine: "unclear"
moa_broad: "unclear"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.05"
max_sig_genes: 67
tags: ["drug", "moa/unclear"]
generated_by: "tahoemap"
---

# L-Thyroxine (sodium salt pentahydrate)

*unclear (unclear) · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 67 / 25 / 22; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.27 / 0.45.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:B11 | 7 / 60 | — | -0.24 | +0.9/+2.4/+1.2 | — |
| 0.5 µM | [[Plate 05]]:B11 | 19 / 6 | — | -0.63 | +0.9/+1.9/+0.1 | — |
| 5 µM | [[Plate 06]]:B11 | 18 / 4 | — | +0.44 | +1.1/+3.0/+1.5 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (7 genes, none with an alert): [[KLF9]] 1.40× (z +5.7, 22/43 lines), [[HIF1A]] 1.25× (z +4.4, 27/48 lines), [[TNC]] 1.37× (z +3.6, 11/25 lines), [[TENT5A]] 1.21× (z +3.3, 9/37 lines), [[KLF10]] 1.23× (z +3.2, 16/48 lines), [[CDCA8]] 1.25× (z +3.1, 13/47 lines), [[TNFRSF9]] 1.32× (z +2.8, 5/26 lines)

**0.5 µM** (19 genes, none with an alert; 12 shown): [[KLF9]] 1.45× (z +6.3, 26/43 lines), [[SCNN1A]] 1.40× (z +4.8, 13/21 lines), [[HCG25]] 1.52× (z +4.2, 6/31 lines), [[CPM]] 1.30× (z +3.5, 12/45 lines), [[PAX2]] 1.36× (z +3.5, 0/14 lines), [[DBP]] 1.58× (z +3.4, 12/41 lines), [[TMEM145]] 1.43× (z +3.3, 1/23 lines), [[ENSG00000288271]] 1.34× (z +3.2, 6/41 lines), [[ENSG00000280571]] 1.35× (z +3.2, 5/39 lines), [[PLAAT1]] 1.31× (z +3.2, 3/24 lines), [[TNFRSF9]] 1.37× (z +3.1, 5/24 lines), [[LINC00460]] 1.60× (z +3.1, 1/12 lines)

**5 µM** (18 genes, none with an alert; 12 shown): [[KLF9]] 1.55× (z +7.3, 29/43 lines), [[ALDH1A3]] 1.56× (z +5.8, 16/28 lines), [[SCNN1A]] 1.41× (z +4.8, 12/21 lines), [[DBP]] 1.74× (z +4.2, 15/45 lines), [[LINC00540]] 1.38× (z +4.1, 2/15 lines), [[UGT1A6]] 1.43× (z +3.8, 6/13 lines), [[EREG]] 1.29× (z +3.4, 10/22 lines), [[HCG25]] 1.39× (z +3.3, 4/44 lines), [[TIPARP]] 1.31× (z +3.3, 22/47 lines), [[TNC]] 1.34× (z +3.3, 6/25 lines), [[CYP1B1]] 1.62× (z +3.3, 14/19 lines), [[KLF10]] 1.24× (z +3.3, 15/48 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (60 genes, none with an alert; 12 shown): [[TTC23L]] 0.677× (z -4.4, 6/39 lines), [[METTL6]] 0.817× (z -4.2, 9/48 lines), [[ANKRD20A5P]] 0.761× (z -4.2, 5/31 lines), [[ENSG00000286239]] 0.681× (z -4.1, 11/44 lines), [[ENSG00000272438]] 0.626× (z -4.0, 8/37 lines), [[ENSG00000286753]] 0.686× (z -3.9, 9/44 lines), [[TCAIM]] 0.791× (z -3.9, 18/48 lines), [[ZNF69]] 0.707× (z -3.8, 7/32 lines), [[ZNF397]] 0.805× (z -3.7, 10/48 lines), [[FZD7]] 0.739× (z -3.7, 10/44 lines), [[HAL]] 0.683× (z -3.7, 4/39 lines), [[ENSG00000247121]] 0.736× (z -3.7, 6/45 lines)

**0.5 µM** (6 genes, none with an alert): [[FZD7]] 0.730× (z -3.9, 14/42 lines), [[OTUD1]] 0.779× (z -3.6, 13/41 lines), [[PRSS16]] 0.722× (z -3.3, 7/26 lines), [[BPHL]] 0.788× (z -3.1, 9/46 lines), [[SEPTIN5]] 0.718× (z -3.1, 9/27 lines), [[FAIM]] 0.796× (z -3.0, 11/43 lines)

**5 µM** (4 genes, none with an alert): [[APH1B]] 0.799× (z -3.4, 6/42 lines), [[RBKS]] 0.787× (z -3.1, 6/42 lines), [[ARHGEF4]] 0.820× (z -3.1, 4/33 lines), [[UBE2Q2P13]] 0.751× (z -3.0, 2/24 lines)

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
| 0.05 µM | — | [[AN3 CA (line)]] (1.54), [[Panc 03.27 (line)]] (1.49), [[SW 900 (line)]] (1.41), [[MIA PaCa-2 (line)]] (1.38) · weakest: [[NCI-H23 (line)]] (0.608), [[A-427 (line)]] (0.641), [[A-172 (line)]] (0.667) |
| 0.5 µM | — | [[COLO 205 (line)]] (1.49), [[SW1417 (line)]] (1.40), [[BT-474 (line)]] (1.34), [[SW48 (line)]] (1.34) · weakest: [[HS-578T (line)]] (0.219), [[C32 (line)]] (0.221), [[NCI-H2030 (line)]] (0.326) |
| 5 µM | — | [[LS 180 (line)]] (1.75), [[HT-29 (line)]] (1.59), [[COLO 205 (line)]] (1.59), [[AsPC-1 (line)]] (1.52) · weakest: [[NCI-H661 (line)]] (0.470), [[NCI-H23 (line)]] (0.541), [[PANC-1 (line)]] (0.664) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 4 next most similar without an alert.*

- [[Salicylic acid (drug)]] (+0.71, Cyclooxygenase inhibitor, ⚠ only 3 significant genes); [[Asciminib (drug)]] (+0.71, Other TK inhibitor); [[Indacaterol (maleate) (drug)]] (+0.70, Adrenoceptor agonist, ⚠ only 3 significant genes); [[Dimethyl fumarate (drug)]] (+0.68, unclear); [[Acetazolamide (drug)]] (+0.68, unclear, ⚠ only 3 significant genes); [[LB-100 (drug)]] (+0.62, unclear, ⚠ only 5 significant genes); [[Pimitespib (drug)]] (+0.62, unclear); [[Pravastatin (sodium) (drug)]] (+0.60, unclear); [[Gallic acid (drug)]] (+0.59, Cyclooxygenase inhibitor); [[Lopinavir (drug)]] (+0.57, unclear); [[Mozavaptan (drug)]] (+0.54, unclear); [[Brivudine (drug)]] (+0.54, unclear)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "L-Thyroxine (sodium salt pentahydrate)"
- `tables/drugdoses.parquet` — dd in 585, 586, 587
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
