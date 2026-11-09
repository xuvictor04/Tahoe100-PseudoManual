---
drug: "Chlorhexidine (diacetate)"
type: "drug"
salt_base: "Chlorhexidine"
targets: ""
moa_fine: "unclear"
moa_broad: "unclear"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 127
tags: ["drug", "moa/unclear"]
generated_by: "tahoemap"
---

# Chlorhexidine (diacetate)

*unclear (unclear) · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 0 / 5 / 127; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): -0.11 / 0.06.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:A2 | 0 / 0 | — | +0.12 | -0.7/-0.0/+0.2 | — |
| 0.5 µM | [[Plate 05]]:A2 | 3 / 2 | — | +0.49 | -0.2/-0.4/-0.9 | — |
| 5 µM | [[Plate 14]]:A2 | 94 / 33 | 0.842 | +0.34 | -2.0/-0.4/+0.4 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (3 genes, none with an alert): [[SF3B4]] 1.58× (z +3.9, 21/47 lines), [[ENSG00000289474]] 2.09× (z +3.5, 6/8 lines), [[KMT2B]] 1.21× (z +3.1, 12/48 lines)

**5 µM** (94 genes, none with an alert; 12 shown): [[MT1G]] 6.25× (z +11.3, 16/16 lines), [[SLC30A1]] 1.73× (z +11.0, 38/48 lines), [[MT1F]] 3.53× (z +9.4, 24/31 lines), [[MT1E]] 2.81× (z +9.4, 24/26 lines), [[NIBAN1]] 1.52× (z +9.1, 25/38 lines), [[PCK2]] 1.54× (z +8.5, 29/47 lines), [[TRIB3]] 1.56× (z +8.5, 28/46 lines), [[ASNS]] 1.52× (z +7.7, 33/45 lines), [[MT1M]] 4.54× (z +7.6, 15/16 lines), [[YARS1]] 1.28× (z +7.5, 34/49 lines), [[PSAT1]] 1.51× (z +7.5, 28/41 lines), [[CARS1]] 1.30× (z +7.3, 31/49 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (2 genes, none with an alert): [[DTX4]] 0.796× (z -3.4, 6/39 lines), [[LINC01119]] 0.763× (z -2.8, 4/37 lines)

**5 µM** (33 genes, none with an alert; 12 shown): [[MT-CYB]] 0.505× (z -9.6, 42/49 lines), [[MT-CO3]] 0.531× (z -9.3, 42/49 lines), [[MT-CO1]] 0.588× (z -8.8, 43/49 lines), [[MT-ND5]] 0.515× (z -8.8, 44/49 lines), [[MT-CO2]] 0.591× (z -8.1, 42/49 lines), [[MT-ND4]] 0.568× (z -8.0, 44/49 lines), [[MT-ND1]] 0.510× (z -7.6, 46/49 lines), [[MT-ATP6]] 0.560× (z -6.8, 41/49 lines), [[MTND5P11]] 0.533× (z -6.3, 26/42 lines), [[MT-ND2]] 0.584× (z -6.2, 41/49 lines), [[MTCO1P12]] 0.631× (z -5.9, 23/47 lines), [[MTATP6P1]] 0.503× (z -5.8, 41/49 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[Module 133]] (+3.5), [[Module 063]] (+3.4) | [[Module 006]] (-2.4) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | [[NCI-H460 (line)]] (1.93), [[Hs 766T (line)]] (1.90), [[MIA PaCa-2 (line)]] (1.65), [[SNU-1 (line)]] (1.50) · weakest: [[NCI-H2122 (line)]] (0.0449), [[RKO (line)]] (0.364), [[LoVo (line)]] (0.366) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Artesunate (drug)]] (+0.63, JAK/STAT inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Neratinib (maleate) (drug)]] (+0.57, EGFR/ERBB inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Adagrasib (drug)]] (+0.55, RAS inhibitor); [[Belumosudil (mesylate) (drug)]] (+0.51, unclear); [[Dihydroartemisinin (drug)]] (+0.50, unclear); [[Pentamidine (isethionate) (drug)]] (+0.47, unclear); [[Entrectinib (drug)]] (+0.44, Other TK inhibitor); [[Cepharanthine (drug)]] (+0.44, unclear); [[5-Azacytidine (drug)]] (+0.39, DNA methyltransferase inhibitor); [[GSK1059615 (drug)]] (+0.34, PI3K/AKT inhibitor)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Chlorhexidine (diacetate)"
- `tables/drugdoses.parquet` — dd in 257, 258, 259
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
