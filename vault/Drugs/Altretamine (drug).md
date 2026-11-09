---
drug: "Altretamine"
type: "drug"
salt_base: "Altretamine"
targets: ""
moa_fine: "DNA synthesis/repair inhibitor"
moa_broad: "unclear"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 1
tags: ["drug", "moa/unclear"]
generated_by: "tahoemap"
---

# Altretamine

*DNA synthesis/repair inhibitor (unclear) · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 1 / 1 / 1; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): none.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.52 / -0.55.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:F12 | 0 / 1 | — | -0.14 | -1.1/-0.6/-1.1 | — |
| 0.5 µM | [[Plate 08]]:F12 | 0 / 1 | — | -0.09 | -1.0/-1.2/-1.5 | — |
| 5 µM | [[Plate 09]]:F12 | 0 / 1 | — | +0.08 | +0.3/+1.0/+1.0 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

No gene is significantly raised at any dose.

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[CNNM3]] 0.792× (z -3.7, 8/46 lines)

**0.5 µM** (1 gene, none with an alert): [[DNTTIP1]] 0.830× (z -3.0, 11/48 lines)

**5 µM** (1 gene, none with an alert): [[DGCR5]] 0.780× (z -3.8, 4/38 lines)

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

⚠ This drug's own vector: only 1 significant gene. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 3 next most similar without an alert.*

- [[Silodosin (drug)]] (+0.80, unclear); [[Arbutin (drug)]] (+0.73, unclear); [[Sivelestat (sodium tetrahydrate) (drug)]] (+0.69, unclear); [[Tetracycline (hydrochloride) (drug)]] (+0.66, unclear, ⚠ only 6 significant genes); [[Ligustrazine (drug)]] (+0.65, unclear, ⚠ only 2 significant genes); [[Azithromycin (hydrate) (drug)]] (+0.62, unclear); [[Fluvoxamine (maleate) (drug)]] (+0.62, unclear); [[CP21R7 (drug)]] (+0.61, GSK3 inhibitor, ⚠ only 1 significant gene); [[Quinidine (15% dihydroquinidine) (drug)]] (+0.59, unclear); [[Fumaric acid (drug)]] (+0.58, unclear); [[Terfenadine (drug)]] (+0.57, unclear)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Altretamine"
- `tables/drugdoses.parquet` — dd in 84, 85, 86
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
