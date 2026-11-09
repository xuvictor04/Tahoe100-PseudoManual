---
drug: "Bimatoprost"
type: "drug"
salt_base: "Bimatoprost"
targets: ""
moa_fine: "unclear"
moa_broad: "unclear"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 54
tags: ["drug", "moa/unclear"]
generated_by: "tahoemap"
---

# Bimatoprost

*unclear (unclear) · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 0 / 54 / 4; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): low dose only (noise?).
> Signature similarity between consecutive doses (low–mid / mid–high): 0.18 / 0.13.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:F6 | 0 / 0 | — | -0.01 | +0.0/-0.2/-0.4 | — |
| 0.5 µM | [[Plate 05]]:F6 | 54 / 0 | — | -0.46 | -0.3/-0.6/-0.1 | — |
| 5 µM | [[Plate 14]]:F6 | 4 / 0 | 0.576 | -0.17 | +1.0/+0.1/-0.4 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (54 genes, none with an alert; 12 shown): [[KIF5C]] 1.42× (z +5.6, 23/48 lines), [[FSIP1]] 1.34× (z +4.4, 8/46 lines), [[RNF212]] 1.44× (z +4.1, 1/11 lines), [[GRHL2]] 1.31× (z +4.1, 0/15 lines), [[CAPN14]] 1.57× (z +4.0, 2/17 lines), [[THBS2]] 1.47× (z +3.9, 0/11 lines), [[PI4KAP2]] 1.33× (z +3.9, 5/43 lines), [[ENSG00000259805]] 1.30× (z +3.8, 5/45 lines), [[EFEMP1]] 1.36× (z +3.8, 1/16 lines), [[ANKRD42-DT]] 1.21× (z +3.7, 11/47 lines), [[ENSG00000287069]] 1.42× (z +3.7, 0/7 lines), [[CSMD1]] 1.31× (z +3.7, 5/41 lines)

**5 µM** (4 genes, none with an alert): [[FKBP5]] 1.67× (z +8.9, 27/42 lines), [[CCND3]] 1.25× (z +4.3, 22/47 lines), [[NNMT]] 1.27× (z +3.0, 8/24 lines), [[MAOA]] 1.20× (z +2.7, 6/35 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

No gene is significantly lowered at any dose.

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
| 0.5 µM | — | [[SW 1088 (line)]] (1.39), [[RKO (line)]] (1.36), [[AsPC-1 (line)]] (1.32), [[SW48 (line)]] (1.31) · weakest: [[HEC-1-A (line)]] (0.306), [[SW 900 (line)]] (0.418), [[SNU-423 (line)]] (0.445) |
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Methylprednisolone succinate (drug)]] (+0.82, Glucocorticoid receptor agonist); [[Nimesulide (drug)]] (+0.79, Cyclooxygenase inhibitor, ⚠ no trustworthy dose (vector dose flagged: toxic; unreliable plate only)); [[Celecoxib (drug)]] (+0.79, Cyclooxygenase inhibitor); [[Bergenin (drug)]] (+0.78, unclear); [[Ipatasertib (drug)]] (+0.76, PI3K/AKT inhibitor); [[Canagliflozin (hemihydrate) (drug)]] (+0.76, Glucose transporter inhibitor); [[Darolutamide (drug)]] (+0.76, Androgen receptor antagonist, ⚠ only 5 significant genes); [[Oxaprozin (drug)]] (+0.75, Cyclooxygenase inhibitor); [[Decitabine (drug)]] (+0.75, DNA methyltransferase inhibitor); [[Docetaxel (Trihydrate) (drug)]] (+0.74, Microtubule inhibitor)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Bimatoprost"
- `tables/drugdoses.parquet` — dd in 194, 195, 196
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
