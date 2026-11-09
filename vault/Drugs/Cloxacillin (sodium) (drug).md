---
drug: "Cloxacillin (sodium)"
type: "drug"
salt_base: "Cloxacillin"
targets: ""
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.05"
max_sig_genes: 19
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Cloxacillin (sodium)

*unclear (inhibitor/antagonist) · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 19 / 5 / 0; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): low dose only (noise?).
> Signature similarity between consecutive doses (low–mid / mid–high): 0.33 / 0.28.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:G11 | 9 / 10 | — | +0.30 | -0.3/+0.2/+0.3 | — |
| 0.5 µM | [[Plate 05]]:G11 | 0 / 5 | — | +0.54 | +0.7/+1.1/+0.2 | — |
| 5 µM | [[Plate 14]]:G11 | 0 / 0 | 0.667 | +0.28 | -1.0/-0.4/-0.3 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (9 genes, none with an alert): [[BZW2]] 1.26× (z +3.2, 22/46 lines), [[DNAJB4]] 1.24× (z +3.2, 3/46 lines), [[TMED2]] 1.21× (z +3.1, 22/48 lines), [[OAT]] 1.26× (z +3.1, 9/46 lines), [[IFRD1]] 1.30× (z +3.0, 28/48 lines), [[DNAJC3]] 1.23× (z +3.0, 21/47 lines), [[SLC16A1]] 1.22× (z +2.9, 14/45 lines), [[ZNF844]] 1.31× (z +2.9, 4/24 lines), [[KHDRBS3]] 1.21× (z +2.7, 3/37 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (10 genes, none with an alert): [[ZNF876P]] 0.717× (z -3.3, 4/30 lines), [[IL31RA]] 0.756× (z -3.2, 1/20 lines), [[ZP3]] 0.749× (z -3.2, 2/36 lines), [[DGCR5]] 0.818× (z -3.2, 4/39 lines), [[CNTNAP3B]] 0.747× (z -3.1, 1/25 lines), [[SOCS3-DT]] 0.647× (z -3.1, 4/40 lines), [[LINC02885]] 0.745× (z -3.1, 3/30 lines), [[LINC02086]] 0.785× (z -3.0, 0/24 lines), [[HEXD]] 0.801× (z -2.9, 6/48 lines), [[LINC01091]] 0.771× (z -2.8, 1/31 lines)

**0.5 µM** (5 genes, none with an alert): [[ENSG00000291185]] 0.640× (z -4.4, 4/28 lines), [[GPR141]] 0.569× (z -4.1, 0/9 lines), [[FAM167A]] 0.663× (z -4.0, 3/30 lines), [[PRRT3]] 0.704× (z -3.9, 8/44 lines), [[SYT13]] 0.666× (z -3.8, 1/15 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 207]] (+2.2), [[Module 041]] (+2.0) | — |
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

- [[Piroxicam (drug)]] (+0.78, Cyclooxygenase inhibitor); [[Ranolazine (drug)]] (+0.78, unclear); [[Allopurinol (drug)]] (+0.76, unclear); [[Clopidogrel (drug)]] (+0.75, unclear); [[Sacubitril_Valsartan (drug)]] (+0.75, unclear, ⚠ only 1 significant gene); [[Pravastatin (sodium) (drug)]] (+0.68, unclear); [[Malotilate (drug)]] (+0.67, unclear); [[Salicylic acid (drug)]] (+0.67, Cyclooxygenase inhibitor, ⚠ only 3 significant genes); [[Goserelin (acetate) (drug)]] (+0.66, unclear); [[Hesperidin (drug)]] (+0.66, unclear)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Cloxacillin (sodium)"
- `tables/drugdoses.parquet` — dd in 287, 288, 289
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
