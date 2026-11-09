---
drug: "Olanzapine"
type: "drug"
salt_base: "Olanzapine"
targets: "HTR2A, HTR2C, DRD2, DRD4, ADRA1A, ADRA1B, ADRA1D, HTR6, CHRM1, CHRM2, CHRM3, CHRM4, CHRM5"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 5
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Olanzapine

*unclear (inhibitor/antagonist) · targets: HTR2A, HTR2C, DRD2, DRD4, ADRA1A, ADRA1B, ADRA1D, HTR6, CHRM1, CHRM2, CHRM3, CHRM4, CHRM5 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 0 / 2 / 5; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): none.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.34 / 0.31.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:F8 | 0 / 0 | — | +0.30 | +0.9/+0.6/+0.1 | — |
| 0.5 µM | [[Plate 05]]:F8 | 1 / 1 | — | +0.39 | +1.6/+0.9/-0.1 | — |
| 5 µM | [[Plate 14]]:F8 | 4 / 1 | 0.838 | -0.16 | +2.3/+0.8/-0.0 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (1 gene, none with an alert): [[ADAM15]] 1.30× (z +3.6, 9/47 lines)

**5 µM** (4 genes, none with an alert): [[CDC45]] 1.20× (z +3.3, 4/45 lines), [[TMEM109]] 1.21× (z +3.1, 5/46 lines), [[NNMT]] 1.24× (z +2.8, 5/24 lines), [[FAM111B]] 1.25× (z +2.7, 3/38 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (1 gene, none with an alert): [[DPY19L2P3]] 0.806× (z -3.0, 6/43 lines)

**5 µM** (1 gene, none with an alert): [[PIK3IP1]] 0.821× (z -2.9, 7/39 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[Module 006]] (+2.2) | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: only 5 significant genes. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[Diphenhydramine (drug)]] (+0.81, unclear); [[Palmatine (chloride) (drug)]] (+0.80, unclear); [[Busulfan (drug)]] (+0.80, DNA synthesis/repair inhibitor); [[(R)-Verapamil (hydrochloride) (drug)]] (+0.78, unclear); [[Megestrol (drug)]] (+0.78, unclear, ⚠ vector dose flagged: cell-cycle shift); [[Brimonidine (drug)]] (+0.75, Adrenoceptor agonist); [[Acetohexamide (drug)]] (+0.75, unclear); [[Finasteride (drug)]] (+0.75, unclear); [[Diammonium Glycyrrhizinate (drug)]] (+0.74, unclear)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Olanzapine"
- `tables/drugdoses.parquet` — dd in 732, 733, 734
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
