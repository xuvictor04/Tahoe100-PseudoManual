---
drug: "Oleic acid"
type: "drug"
salt_base: "Oleic acid"
targets: ""
moa_fine: "unclear"
moa_broad: "activator/agonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 1
tags: ["drug", "moa/activator_agonist"]
generated_by: "tahoemap"
---

# Oleic acid

*unclear (activator/agonist) · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 1 / 1 / 0; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): none.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.24 / 0.02.
> Flags by dose: - / noisy plate (z scaled) / noisy plate (z scaled).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:H7 | 0 / 1 | — | -0.01 | -0.3/+0.5/-0.3 | — |
| 0.5 µM | [[Plate 02]]:H7 | 1 / 0 | — | +0.42 | +0.4/+0.3/-0.4 | noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:H7 | 0 / 0 | — | -0.20 | +0.9/+0.7/+0.7 | noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (1 gene, none with an alert): [[TPRA1]] 1.29× (z +2.9, 5/48 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[PRPF31]] 0.793× (z -3.8, 6/48 lines)

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

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 5 next most similar without an alert.*

- [[Oxaliplatin (drug)]] (+0.53, DNA synthesis/repair inhibitor, ⚠ only 7 significant genes); [[ETC-206 (drug)]] (+0.52, Protein synthesis inhibitor, ⚠ only 0 significant genes); [[Raltitrexed (drug)]] (+0.50, DNA synthesis/repair inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Cilostazol (drug)]] (+0.49, unclear); [[(R)-Verapamil (hydrochloride) (drug)]] (+0.49, unclear); [[Olanzapine (drug)]] (+0.48, unclear, ⚠ only 5 significant genes); [[Filgotinib (drug)]] (+0.48, JAK/STAT inhibitor); [[LY2090314 (drug)]] (+0.47, GSK3 inhibitor, ⚠ only 7 significant genes); [[Diphenhydramine (drug)]] (+0.44, unclear); [[Larotrectinib (drug)]] (+0.44, Other TK inhibitor); [[Demeclocycline (drug)]] (+0.44, unclear); [[Busulfan (drug)]] (+0.42, DNA synthesis/repair inhibitor); [[Gallic acid (hydrate) (drug)]] (+0.41, Cyclooxygenase inhibitor)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Oleic acid"
- `tables/drugdoses.parquet` — dd in 735, 736, 737
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
