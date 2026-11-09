---
drug: "Baicalin"
type: "drug"
salt_base: "Baicalin"
targets: ""
moa_fine: "unclear"
moa_broad: "activator/agonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 12
tags: ["drug", "moa/activator_agonist"]
generated_by: "tahoemap"
---

# Baicalin

*unclear (activator/agonist) · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 3 / 5 / 12; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.23 / 0.10.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:G3 | 2 / 1 | — | +0.19 | -0.7/-0.0/+0.2 | — |
| 0.5 µM | [[Plate 05]]:G3 | 2 / 3 | — | +0.07 | +0.3/+0.6/+0.8 | — |
| 5 µM | [[Plate 14]]:G3 | 5 / 7 | 0.874 | +0.39 | -0.9/-0.7/-0.9 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (2 genes, none with an alert): [[RING1]] 1.27× (z +4.1, 11/48 lines), [[CFAP210]] 1.69× (z +2.9, 9/45 lines)

**0.5 µM** (2 genes, none with an alert): [[RING1]] 1.36× (z +5.3, 25/48 lines), [[ZNF875]] 1.32× (z +4.2, 24/46 lines)

**5 µM** (5 genes, none with an alert): [[SLCO5A1]] 1.34× (z +6.1, 16/42 lines), [[ZBED6]] 1.45× (z +3.2, 12/48 lines), [[EBF2]] 1.29× (z +3.1, 2/27 lines), [[SMG1P3]] 1.28× (z +3.1, 5/47 lines), [[SUSD4]] 1.28× (z +3.0, 2/33 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[ENSG00000288670]] 0.777× (z -3.1, 6/45 lines)

**0.5 µM** (3 genes, none with an alert): [[RPSA]] 0.705× (z -4.6, 22/48 lines), [[THSD7B]] 0.671× (z -4.1, 9/39 lines), [[PPP1R3F]] 0.753× (z -3.3, 6/44 lines)

**5 µM** (7 genes, none with an alert): [[RPSA]] 0.810× (z -3.9, 23/48 lines), [[C6orf47]] 0.780× (z -3.9, 8/48 lines), [[CHCHD4]] 0.773× (z -3.6, 11/48 lines), [[SEPHS2]] 0.787× (z -3.4, 18/48 lines), [[ZNF22]] 0.833× (z -3.4, 9/43 lines), [[DNAJC4]] 0.749× (z -3.4, 17/48 lines), [[SLC22A17]] 0.786× (z -3.0, 3/27 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[Module 179]] (+2.3), [[Module 077]] (+2.0) | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 6 next most similar without an alert.*

- [[NVP-BHG712 (drug)]] (+0.57, unclear); [[Gallic acid (drug)]] (+0.49, Cyclooxygenase inhibitor); [[AT7519 (drug)]] (+0.49, CDK inhibitor, ⚠ only 6 significant genes); [[Capivasertib (drug)]] (+0.49, PI3K/AKT inhibitor, ⚠ only 5 significant genes); [[Thymopentin (drug)]] (+0.45, unclear, ⚠ only 2 significant genes); [[Triclosan (drug)]] (+0.43, unclear, ⚠ only 2 significant genes); [[Acetazolamide (drug)]] (+0.42, unclear, ⚠ only 3 significant genes); [[Belinostat (drug)]] (+0.40, HDAC inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Sulfisoxazole (drug)]] (+0.39, unclear); [[Goserelin (acetate) (drug)]] (+0.39, unclear); [[Fluvoxamine (drug)]] (+0.38, unclear); [[Hexylresorcinol (drug)]] (+0.38, unclear); [[Tadalafil (drug)]] (+0.37, unclear); [[Berberine (chloride hydrate) (drug)]] (+0.36, unclear)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Baicalin"
- `tables/drugdoses.parquet` — dd in 138, 139, 140
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
