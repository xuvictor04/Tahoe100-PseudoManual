---
drug: "Fusidic acid"
type: "drug"
salt_base: "Fusidic acid"
targets: ""
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 10
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Fusidic acid

*unclear (inhibitor/antagonist) · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 1 / 3 / 10; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.34 / 0.29.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:G9 | 1 / 0 | — | +0.60 | -0.5/-0.8/-1.0 | — |
| 0.5 µM | [[Plate 05]]:G9 | 0 / 3 | — | +0.14 | +0.3/+0.1/-0.4 | — |
| 5 µM | [[Plate 14]]:G9 | 3 / 7 | 0.790 | +0.19 | -0.1/-1.8/-1.3 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[SLCO5A1]] 1.40× (z +4.9, 6/43 lines)

**5 µM** (3 genes, none with an alert): [[SLCO5A1]] 1.31× (z +5.6, 17/42 lines), [[ABCA2]] 1.22× (z +3.3, 11/47 lines), [[ENSG00000236498]] 1.24× (z +3.1, 5/45 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (3 genes, none with an alert): [[ENSG00000280561]] 0.751× (z -3.6, 10/44 lines), [[ENSG00000273828]] 0.724× (z -3.5, 9/42 lines), [[DHRS11]] 0.762× (z -3.5, 6/45 lines)

**5 µM** (7 genes, none with an alert): [[ENSG00000269635]] 0.683× (z -4.0, 6/41 lines), [[ENSG00000249803]] 0.698× (z -4.0, 2/13 lines), [[ESPN]] 0.739× (z -4.0, 6/22 lines), [[ELAVL3]] 0.763× (z -3.8, 12/45 lines), [[TRAM2-AS1]] 0.816× (z -3.5, 10/47 lines), [[ENSG00000291258]] 0.735× (z -3.5, 2/22 lines), [[ZNF341-AS1]] 0.761× (z -3.3, 6/37 lines)

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

- [[Clonidine (hydrochloride) (drug)]] (+0.74, Adrenoceptor agonist, ⚠ only 4 significant genes); [[Balsalazide (sodium hydrate) (drug)]] (+0.74, JAK/STAT inhibitor, ⚠ only 9 significant genes); [[Tucatinib (drug)]] (+0.67, EGFR/ERBB inhibitor); [[Lucanthone (drug)]] (+0.65, unclear); [[Fenofibrate (drug)]] (+0.61, unclear); [[Berberine (chloride hydrate) (drug)]] (+0.60, unclear); [[MK-8353 (drug)]] (+0.58, Other MAPK inhibitor); [[Oxaliplatin (drug)]] (+0.58, DNA synthesis/repair inhibitor, ⚠ only 7 significant genes); [[Benproperine (phosphate) (drug)]] (+0.57, unclear); [[Pyridoxine (hydrochloride) (drug)]] (+0.57, unclear); [[Volasertib (drug)]] (+0.56, unclear)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Fusidic acid"
- `tables/drugdoses.parquet` — dd in 483, 484, 485
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
