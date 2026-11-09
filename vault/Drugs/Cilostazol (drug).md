---
drug: "Cilostazol"
type: "drug"
salt_base: "Cilostazol"
targets: "PDE3A"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 17
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Cilostazol

*unclear (inhibitor/antagonist) · targets: PDE3A · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 7 / 0 / 17; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.35 / -0.06.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:E2 | 2 / 5 | — | +0.02 | +0.6/+0.4/+1.4 | — |
| 0.5 µM | [[Plate 08]]:E2 | 0 / 0 | — | +0.36 | +0.2/+0.9/+0.5 | — |
| 5 µM | [[Plate 09]]:E2 | 1 / 16 | — | +0.36 | -0.2/-0.1/+0.0 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (2 genes, none with an alert): [[PNRC2]] 1.21× (z +3.4, 10/47 lines), [[PRELID3B]] 1.22× (z +3.2, 16/47 lines)

**5 µM** (1 gene, none with an alert): [[PID1]] 1.24× (z +2.9, 9/26 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (5 genes, none with an alert): [[RECQL5]] 0.828× (z -3.3, 8/47 lines), [[ZNF214]] 0.690× (z -3.3, 8/33 lines), [[ZNF274]] 0.802× (z -3.2, 12/46 lines), [[MLXIPL]] 0.783× (z -3.1, 2/32 lines), [[ENSG00000230479]] 0.817× (z -2.8, 8/35 lines)

**5 µM** (16 genes, none with an alert; 12 shown): [[SELENOF]] 0.827× (z -4.9, 22/48 lines), [[DHRS3]] 0.741× (z -4.7, 24/35 lines), [[EFNA3]] 0.670× (z -4.5, 17/47 lines), [[ATN1]] 0.798× (z -3.9, 22/48 lines), [[APOBEC3C]] 0.742× (z -3.5, 10/43 lines), [[ENSG00000289293]] 0.675× (z -3.4, 0/47 lines), [[LANCL3]] 0.708× (z -3.4, 2/26 lines), [[OPTN]] 0.828× (z -3.4, 18/46 lines), [[PIAS3]] 0.811× (z -3.3, 6/47 lines), [[VEGFA]] 0.800× (z -3.2, 22/46 lines), [[TMEM263]] 0.829× (z -3.1, 17/48 lines), [[NDNF]] 0.721× (z -3.1, 2/21 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 182]] (+2.1) | — |
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

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 4 next most similar without an alert.*

- [[Dapagliflozin (drug)]] (+0.68, Glucose transporter inhibitor); [[Finasteride (drug)]] (+0.66, unclear); [[Olanzapine (drug)]] (+0.58, unclear, ⚠ only 5 significant genes); [[Oxaliplatin (drug)]] (+0.57, DNA synthesis/repair inhibitor, ⚠ only 7 significant genes); [[Cinacalcet (drug)]] (+0.57, unclear, ⚠ only 8 significant genes); [[Vismodegib (drug)]] (+0.55, Sonic inhibitor, ⚠ only 5 significant genes); [[Dabrafenib (drug)]] (+0.54, RAF inhibitor); [[Demeclocycline (drug)]] (+0.54, unclear); [[Palmatine (chloride) (drug)]] (+0.52, unclear); [[Acetohexamide (drug)]] (+0.50, unclear); [[(R)-Verapamil (hydrochloride) (drug)]] (+0.48, unclear); [[Gallic acid (hydrate) (drug)]] (+0.48, Cyclooxygenase inhibitor)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Cilostazol"
- `tables/drugdoses.parquet` — dd in 263, 264, 265
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
