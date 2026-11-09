---
drug: "Pentagastrin"
type: "drug"
salt_base: "Pentagastrin"
targets: "CCKBR"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 9
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Pentagastrin

*unclear (inhibitor/antagonist) · targets: CCKBR · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 2 / 6 / 9; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): none.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.30 / 0.24.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:F10 | 0 / 2 | — | -0.48 | -1.4/-0.9/-0.3 | — |
| 0.5 µM | [[Plate 05]]:F10 | 5 / 1 | — | -0.42 | -1.0/-0.7/-0.6 | — |
| 5 µM | [[Plate 14]]:F10 | 1 / 8 | 0.810 | +0.49 | -0.9/-0.2/-1.2 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (5 genes, none with an alert): [[FAM86DP]] 1.38× (z +3.6, 3/39 lines), [[ENSG00000288725]] 1.40× (z +3.2, 3/37 lines), [[KBTBD3]] 1.35× (z +3.2, 3/44 lines), [[ENSG00000230647]] 1.32× (z +3.1, 2/22 lines), [[CTTN-DT]] 1.22× (z +2.9, 5/45 lines)

**5 µM** (1 gene, none with an alert): [[ENSG00000266953]] 1.36× (z +3.4, 8/47 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (2 genes, none with an alert): [[AOX1]] 0.707× (z -3.9, 5/28 lines), [[RMI2]] 0.790× (z -3.2, 7/44 lines)

**0.5 µM** (1 gene, none with an alert): [[CCDC144CP]] 0.767× (z -3.4, 8/39 lines)

**5 µM** (8 genes, none with an alert): [[BAX]] 0.828× (z -3.9, 7/48 lines), [[NCL]] 0.797× (z -3.8, 40/48 lines), [[RPL39L]] 0.820× (z -3.3, 4/32 lines), [[IRF2BPL]] 0.816× (z -3.3, 15/47 lines), [[TMEM106C]] 0.816× (z -3.2, 14/47 lines), [[E2F1]] 0.785× (z -3.2, 1/45 lines), [[SBK1]] 0.818× (z -3.2, 3/31 lines), [[POLR3GL]] 0.777× (z -3.0, 16/48 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[Module 179]] (+2.1) | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: only 9 significant genes. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Paclitaxel (drug)]] (+0.70, Microtubule inhibitor, ⚠ only 3 significant genes); [[Fenofibrate (drug)]] (+0.69, unclear); [[Lucanthone (drug)]] (+0.68, unclear); [[Volasertib (drug)]] (+0.67, unclear); [[Balsalazide (sodium hydrate) (drug)]] (+0.65, JAK/STAT inhibitor, ⚠ only 9 significant genes); [[Ivermectin (drug)]] (+0.64, unclear); [[ERK5-IN-2 (drug)]] (+0.63, Other MAPK inhibitor); [[Folic acid (drug)]] (+0.61, unclear); [[Rutin (trihydrate) (drug)]] (+0.60, unclear); [[Tucatinib (drug)]] (+0.60, EGFR/ERBB inhibitor)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Pentagastrin"
- `tables/drugdoses.parquet` — dd in 788, 789, 790
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
