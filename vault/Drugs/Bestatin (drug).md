---
drug: "Bestatin"
type: "drug"
salt_base: "Bestatin"
targets: "ANPEP"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "0.05"
max_sig_genes: 3
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Bestatin

*unclear (inhibitor/antagonist) · targets: ANPEP · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 3 / 1 / 2; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): none.
> Signature similarity between consecutive doses (low–mid / mid–high): -0.11 / 0.19.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:B5 | 2 / 1 | — | -0.27 | -0.3/-0.9/-0.0 | — |
| 0.5 µM | [[Plate 08]]:B5 | 0 / 1 | — | +0.77 | +0.5/+0.7/+1.2 | — |
| 5 µM | [[Plate 09]]:B5 | 0 / 2 | — | +0.17 | +0.8/+0.0/+0.4 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (2 genes, none with an alert): [[NUMBL]] 1.22× (z +3.6, 8/46 lines), [[ANKRD18B]] 1.33× (z +3.1, 4/24 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[PIF1]] 0.792× (z -2.7, 8/45 lines)

**0.5 µM** (1 gene, none with an alert): [[NIM1K]] 0.773× (z -3.5, 2/44 lines)

**5 µM** (2 genes, none with an alert): [[LHX6]] 0.676× (z -3.4, 4/22 lines), [[SHFL]] 0.799× (z -2.8, 6/46 lines)

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

⚠ This drug's own vector: only 3 significant genes. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 3 next most similar without an alert.*

- [[Vismodegib (drug)]] (+0.72, Sonic inhibitor, ⚠ only 5 significant genes); [[Ataluren (drug)]] (+0.65, unclear, ⚠ only 7 significant genes); [[Belzutifan (drug)]] (+0.56, unclear); [[Belumosudil (mesylate) (drug)]] (+0.56, unclear); [[Macitentan (drug)]] (+0.55, unclear, ⚠ only 5 significant genes); [[Benztropine (mesylate) (drug)]] (+0.55, unclear); [[Dapagliflozin (drug)]] (+0.55, Glucose transporter inhibitor); [[Vitamin K4 (drug)]] (+0.52, unclear); [[Ropivacaine (hydrochloride monohydrate) (drug)]] (+0.52, unclear); [[AZD1390 (drug)]] (+0.49, unclear); [[Isocorydine (drug)]] (+0.49, unclear)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Bestatin"
- `tables/drugdoses.parquet` — dd in 179, 180, 181
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
