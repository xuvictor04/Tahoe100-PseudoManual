---
drug: "Omeprazole (sodium)"
type: "drug"
salt_base: "Omeprazole"
targets: ""
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 14
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Omeprazole (sodium)

*unclear (inhibitor/antagonist) · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 0 / 1 / 14; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.25 / 0.17.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:B9 | 0 / 0 | — | +0.29 | -0.1/-0.3/+0.1 | — |
| 0.5 µM | [[Plate 11]]:B9 | 1 / 0 | — | +0.59 | +0.7/+0.6/+0.5 | — |
| 5 µM | [[Plate 12]]:B9 | 13 / 1 | — | -0.28 | +0.3/+1.4/+0.6 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (1 gene, none with an alert): [[ENSG00000257062]] 1.25× (z +3.0, 0/19 lines)

**5 µM** (13 genes, none with an alert; 12 shown): [[CYP1B1]] 1.85× (z +4.2, 16/19 lines), [[TIPARP]] 1.31× (z +3.3, 22/47 lines), [[RMDN2-AS1]] 1.57× (z +3.2, 9/30 lines), [[TRIM15]] 1.52× (z +3.2, 1/14 lines), [[BMP2]] 1.28× (z +3.2, 2/26 lines), [[ALDH1A3]] 1.28× (z +3.2, 6/27 lines), [[HCG20]] 1.36× (z +3.2, 5/45 lines), [[ADGRF1]] 1.41× (z +3.1, 1/13 lines), [[STK32B]] 1.24× (z +3.1, 0/24 lines), [[PPP1R14A]] 1.93× (z +3.1, 1/9 lines), [[ATP2C2]] 1.24× (z +3.0, 0/15 lines), [[ENSG00000285822]] 1.31× (z +2.8, 0/9 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**5 µM** (1 gene, none with an alert): [[ENSG00000285043]] 0.729× (z -3.2, 3/46 lines)

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

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 3 next most similar without an alert.*

- [[Ornidazole (drug)]] (+0.69, unclear, ⚠ only 1 significant gene; no trustworthy dose (vector dose flagged: unreliable plate only)); [[CP21R7 (drug)]] (+0.68, GSK3 inhibitor, ⚠ only 1 significant gene); [[Minodronic acid (drug)]] (+0.66, unclear); [[Carbamazepine (drug)]] (+0.65, HDAC inhibitor); [[Altretamine (drug)]] (+0.57, DNA synthesis/repair inhibitor, ⚠ only 1 significant gene); [[Silodosin (drug)]] (+0.56, unclear); [[Azithromycin (hydrate) (drug)]] (+0.56, unclear); [[Decitabine (drug)]] (+0.56, DNA methyltransferase inhibitor); [[Bendamustine (drug)]] (+0.56, DNA synthesis/repair inhibitor); [[Bicalutamide (drug)]] (+0.54, Androgen receptor antagonist); [[Entrectinib (drug)]] (+0.53, Other TK inhibitor)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Omeprazole (sodium)"
- `tables/drugdoses.parquet` — dd in 741, 742, 743
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
