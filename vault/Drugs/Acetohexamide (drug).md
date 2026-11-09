---
drug: "Acetohexamide"
type: "drug"
salt_base: "Acetohexamide"
targets: ""
moa_fine: "unclear"
moa_broad: "activator/agonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 13
tags: ["drug", "moa/activator_agonist"]
generated_by: "tahoemap"
---

# Acetohexamide

*unclear (activator/agonist) · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 3 / 9 / 13; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): -0.13 / 0.14.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:B7 | 0 / 3 | — | -0.13 | +0.4/+0.2/+0.7 | — |
| 0.5 µM | [[Plate 05]]:B7 | 9 / 0 | — | -0.25 | -0.3/-0.2/+0.0 | — |
| 5 µM | [[Plate 14]]:B7 | 9 / 4 | 0.726 | -0.32 | +1.0/+0.9/+0.1 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (9 genes, none with an alert): [[FUNDC2]] 1.47× (z +4.9, 23/46 lines), [[PPIA]] 1.27× (z +3.9, 23/48 lines), [[RUNDC3A-AS1]] 1.38× (z +3.7, 3/33 lines), [[SMPD3]] 1.45× (z +3.6, 3/25 lines), [[FBN2]] 1.24× (z +3.2, 0/15 lines), [[SAMD14]] 1.39× (z +3.1, 2/30 lines), [[ENSG00000285743]] 1.36× (z +3.0, 0/18 lines), [[ENSG00000289100]] 1.31× (z +2.8, 0/39 lines), [[ENSG00000234261]] 1.28× (z +2.8, 0/19 lines)

**5 µM** (9 genes, none with an alert): [[LINC00707]] 1.23× (z +3.6, 1/22 lines), [[KIRREL3]] 1.24× (z +3.6, 2/12 lines), [[SSUH2]] 1.26× (z +3.1, 3/42 lines), [[ENSG00000266578]] 1.30× (z +3.1, 2/19 lines), [[ENSG00000289384]] 1.27× (z +3.0, 3/27 lines), [[TBILA]] 1.33× (z +3.0, 3/39 lines), [[LINC02057]] 1.23× (z +2.9, 3/23 lines), [[ENSG00000285743]] 1.24× (z +2.9, 1/18 lines), [[RDUR]] 1.22× (z +2.9, 0/18 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (3 genes, none with an alert): [[DOCK8]] 0.758× (z -3.4, 1/28 lines), [[DARS1-AS1]] 0.752× (z -3.2, 16/47 lines), [[CCDC40]] 0.775× (z -2.8, 6/46 lines)

**5 µM** (4 genes, none with an alert): [[PPIA]] 0.779× (z -5.7, 35/48 lines), [[H1-0]] 0.790× (z -4.1, 33/43 lines), [[CAPN5]] 0.827× (z -3.7, 12/44 lines), [[ZSCAN2]] 0.832× (z -3.4, 12/45 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | [[Module 041]] (-2.1) |

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

- [[Brimonidine (drug)]] (+0.76, Adrenoceptor agonist); [[Norepinephrine (hydrochloride) (drug)]] (+0.76, Adrenoceptor agonist); [[Finasteride (drug)]] (+0.75, unclear); [[Olanzapine (drug)]] (+0.75, unclear, ⚠ only 5 significant genes); [[Demeclocycline (drug)]] (+0.66, unclear); [[Procainamide (hydrochloride) (drug)]] (+0.64, DNA methyltransferase inhibitor, ⚠ only 7 significant genes); [[Dapagliflozin (drug)]] (+0.62, Glucose transporter inhibitor); [[Busulfan (drug)]] (+0.61, DNA synthesis/repair inhibitor); [[Gallic acid (hydrate) (drug)]] (+0.58, Cyclooxygenase inhibitor); [[(R)-Verapamil (hydrochloride) (drug)]] (+0.58, unclear)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Acetohexamide"
- `tables/drugdoses.parquet` — dd in 51, 52, 53
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
