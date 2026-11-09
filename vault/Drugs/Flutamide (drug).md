---
drug: "Flutamide"
type: "drug"
salt_base: "Flutamide"
targets: "AR"
moa_fine: "Androgen receptor antagonist"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 19
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Flutamide

*Androgen receptor antagonist (inhibitor/antagonist) · targets: AR · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 3 / 19 / 18; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): -0.11 / 0.53.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:C8 | 2 / 1 | — | +0.23 | -0.2/-0.1/-0.2 | — |
| 0.5 µM | [[Plate 11]]:C8 | 13 / 6 | — | -0.24 | +1.1/+1.5/+1.0 | — |
| 5 µM | [[Plate 12]]:C8 | 12 / 6 | — | -0.35 | +1.0/+1.6/+1.0 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (2 genes, none with an alert): [[KIF5C]] 1.24× (z +3.3, 6/48 lines), [[CLASP1-AS1]] 1.61× (z +3.1, 10/45 lines)

**0.5 µM** (13 genes, none with an alert; 12 shown): [[SYN2]] 1.44× (z +3.8, 3/21 lines), [[CX3CL1]] 1.54× (z +3.4, 0/19 lines), [[DCC]] 1.41× (z +3.4, 4/37 lines), [[MORF4L1P1]] 1.40× (z +3.4, 14/44 lines), [[STAG3]] 1.30× (z +3.2, 3/24 lines), [[HAND2-AS1]] 1.48× (z +3.2, 1/20 lines), [[GRIA4]] 1.44× (z +3.1, 0/30 lines), [[LINC02934]] 1.40× (z +3.1, 4/40 lines), [[COPZ2]] 1.40× (z +3.1, 0/32 lines), [[XRCC3]] 1.26× (z +3.0, 4/42 lines), [[ENSG00000253642]] 1.40× (z +3.0, 1/7 lines), [[HUNK]] 1.22× (z +3.0, 1/26 lines)

**5 µM** (12 genes, none with an alert): [[BAALC]] 1.54× (z +3.7, 0/13 lines), [[P3H2]] 1.24× (z +3.7, 3/20 lines), [[LPAR3]] 1.45× (z +3.6, 1/25 lines), [[GJA1]] 1.28× (z +3.3, 5/22 lines), [[WT1]] 1.35× (z +3.2, 2/18 lines), [[ENSG00000263272]] 1.49× (z +3.2, 10/44 lines), [[TYMS]] 1.33× (z +3.0, 16/46 lines), [[PTHLH]] 1.35× (z +3.0, 5/26 lines), [[ENSG00000259827]] 1.71× (z +2.9, 5/38 lines), [[FOXC2]] 1.54× (z +2.8, 5/14 lines), [[HTATIP2]] 1.26× (z +2.8, 5/40 lines), [[H1-10]] 1.27× (z +2.8, 12/48 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[MAP2K6]] 0.719× (z -3.0, 0/26 lines)

**0.5 µM** (6 genes, none with an alert): [[USO1]] 0.832× (z -4.2, 21/48 lines), [[DANT1]] 0.649× (z -3.8, 10/25 lines), [[LRRC37A2]] 0.813× (z -3.4, 11/46 lines), [[ZNF699]] 0.830× (z -3.3, 10/48 lines), [[ENSG00000283352]] 0.780× (z -3.1, 5/46 lines), [[ENSG00000290890]] 0.833× (z -2.7, 13/48 lines)

**5 µM** (6 genes, none with an alert): [[MCF2]] 0.704× (z -3.3, 8/42 lines), [[BMAL1]] 0.821× (z -3.3, 6/46 lines), [[ZFYVE1]] 0.831× (z -3.2, 6/48 lines), [[LINC00862]] 0.778× (z -3.1, 16/47 lines), [[TRIM3]] 0.781× (z -3.1, 8/47 lines), [[IKZF5]] 0.821× (z -3.0, 13/48 lines)

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
| 5 µM | [[HEC-1-A (line)]] (-3.1) | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] (+0.79, Glucose transporter inhibitor); [[Dorzolamide (hydrochloride) (drug)]] (+0.79, unclear); [[Elagolix sodium (drug)]] (+0.72, unclear); [[Bimatoprost (drug)]] (+0.65, unclear); [[Imiquimod (hydrochloride) (drug)]] (+0.64, unclear, ⚠ vector dose flagged: toxic); [[Oxaprozin (drug)]] (+0.62, Cyclooxygenase inhibitor); [[Darolutamide (drug)]] (+0.61, Androgen receptor antagonist, ⚠ only 5 significant genes); [[Drospirenone (drug)]] (+0.60, unclear); [[Canagliflozin (hemihydrate) (drug)]] (+0.60, Glucose transporter inhibitor); [[Celecoxib (drug)]] (+0.60, Cyclooxygenase inhibitor)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Flutamide"
- `tables/drugdoses.parquet` — dd in 459, 460, 461
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
