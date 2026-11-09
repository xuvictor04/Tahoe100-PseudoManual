---
drug: "Bergenin"
type: "drug"
salt_base: "Bergenin"
targets: ""
moa_fine: "unclear"
moa_broad: "unclear"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 31
tags: ["drug", "moa/unclear"]
generated_by: "tahoemap"
---

# Bergenin

*unclear (unclear) · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 0 / 31 / 4; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): low dose only (noise?).
> Signature similarity between consecutive doses (low–mid / mid–high): 0.17 / 0.30.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:F4 | 0 / 0 | — | +0.29 | -0.6/-0.4/-0.2 | — |
| 0.5 µM | [[Plate 05]]:F4 | 6 / 25 | — | -0.31 | -0.5/-1.0/-0.4 | — |
| 5 µM | [[Plate 14]]:F4 | 2 / 2 | 0.641 | +0.18 | -1.2/-1.0/-0.9 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (6 genes, none with an alert): [[COL16A1]] 1.47× (z +3.7, 5/27 lines), [[ENSG00000228434]] 1.32× (z +3.4, 9/43 lines), [[ENSG00000240499]] 1.42× (z +3.2, 2/33 lines), [[RPL6]] 1.35× (z +3.2, 24/48 lines), [[CDK10]] 1.24× (z +3.2, 8/46 lines), [[ENSG00000273784]] 1.32× (z +3.0, 5/38 lines)

**5 µM** (2 genes, none with an alert): [[KCNK13]] 1.23× (z +3.2, 2/31 lines), [[SUSD4]] 1.27× (z +2.9, 1/30 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (25 genes, none with an alert; 12 shown): [[PCBP1]] 0.726× (z -5.0, 40/48 lines), [[PFKM]] 0.741× (z -4.4, 12/45 lines), [[DPAGT1]] 0.756× (z -4.3, 10/44 lines), [[SLC39A6]] 0.810× (z -4.1, 22/48 lines), [[RBM18]] 0.824× (z -4.0, 15/48 lines), [[HUS1]] 0.820× (z -3.8, 15/48 lines), [[ENPP4]] 0.796× (z -3.7, 7/30 lines), [[MLX]] 0.796× (z -3.7, 14/46 lines), [[CFL2]] 0.795× (z -3.6, 13/42 lines), [[FAM8A1]] 0.810× (z -3.5, 17/47 lines), [[TMEM123]] 0.830× (z -3.5, 23/48 lines), [[ZNF184]] 0.772× (z -3.5, 12/46 lines)

**5 µM** (2 genes, none with an alert): [[VARS1]] 0.795× (z -3.7, 20/48 lines), [[G6PD]] 0.829× (z -3.5, 14/48 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | [[Module 160]] (+2.6) | [[Module 025]] (-2.3) |
| 5 µM | — | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | [[NCI-H1792 (line)]] (1.60), [[hTERT-HPNE (line)]] (1.58), [[H4 (line)]] (1.57), [[CHP-212 (line)]] (1.56) · weakest: [[AN3 CA (line)]] (0.370), [[SW1417 (line)]] (0.423), [[LOX-IMVI (line)]] (0.488) |
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Bimatoprost (drug)]] (+0.78, unclear); [[Celecoxib (drug)]] (+0.78, Cyclooxygenase inhibitor); [[Ipatasertib (drug)]] (+0.74, PI3K/AKT inhibitor); [[Methylprednisolone succinate (drug)]] (+0.73, Glucocorticoid receptor agonist); [[Thymol (drug)]] (+0.67, unclear); [[Dexmedetomidine (drug)]] (+0.62, Adrenoceptor agonist, ⚠ only 9 significant genes); [[Darolutamide (drug)]] (+0.61, Androgen receptor antagonist, ⚠ only 5 significant genes); [[Decitabine (drug)]] (+0.61, DNA methyltransferase inhibitor); [[Docetaxel (Trihydrate) (drug)]] (+0.59, Microtubule inhibitor); [[ULK-101 (drug)]] (+0.59, unclear)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Bergenin"
- `tables/drugdoses.parquet` — dd in 176, 177, 178
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
