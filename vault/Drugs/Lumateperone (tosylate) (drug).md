---
drug: "Lumateperone (tosylate)"
type: "drug"
salt_base: "Lumateperone"
targets: "HTR2A, DRD2"
moa_fine: "unclear"
moa_broad: "unclear"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 9
tags: ["drug", "moa/unclear"]
generated_by: "tahoemap"
---

# Lumateperone (tosylate)

*unclear (unclear) · targets: HTR2A, DRD2 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 1 / 9 / 7; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): none.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.10 / 0.37.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:F11 | 1 / 0 | — | +0.30 | +0.3/-0.4/-0.3 | — |
| 0.5 µM | [[Plate 05]]:F11 | 0 / 9 | — | +0.29 | +1.2/+1.3/-0.1 | — |
| 5 µM | [[Plate 14]]:F11 | 4 / 3 | 0.891 | +0.15 | -0.9/-2.0/-2.2 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[USP35]] 1.31× (z +3.1, 2/46 lines)

**5 µM** (4 genes, none with an alert): [[ENSG00000269968]] 1.63× (z +6.1, 35/48 lines), [[ENSG00000273149]] 1.64× (z +5.2, 23/44 lines), [[MED16]] 1.26× (z +3.8, 11/48 lines), [[PCDH7]] 1.20× (z +2.9, 7/31 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (9 genes, none with an alert): [[ANXA8]] 0.448× (z -3.8, 0/9 lines), [[PINCR]] 0.571× (z -3.8, 3/18 lines), [[CPAMD8]] 0.649× (z -3.7, 8/28 lines), [[ZNF790-AS1]] 0.787× (z -3.6, 4/22 lines), [[ENSG00000269968]] 0.701× (z -3.4, 9/48 lines), [[CNGA1]] 0.755× (z -3.2, 5/39 lines), [[SHF]] 0.759× (z -3.2, 2/39 lines), [[TMEM38A]] 0.813× (z -3.2, 8/47 lines), [[DPY19L2P3]] 0.795× (z -3.1, 2/44 lines)

**5 µM** (3 genes, none with an alert): [[HMGB2]] 0.779× (z -3.6, 35/49 lines), [[TARS2]] 0.831× (z -3.1, 13/48 lines), [[ENSG00000284685]] 0.807× (z -2.8, 5/39 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | [[Module 048]] (-2.3), [[Module 041]] (-2.1), [[Module 059]] (-2.0) |

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

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 3 next most similar without an alert.*

- [[Relugolix (drug)]] (+0.88, unclear, ⚠ only 5 significant genes); [[Rutin (trihydrate) (drug)]] (+0.73, unclear); [[Pyridoxine (hydrochloride) (drug)]] (+0.71, unclear); [[Trifluridine (drug)]] (+0.70, DNA synthesis/repair inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Megestrol (drug)]] (+0.67, unclear, ⚠ vector dose flagged: cell-cycle shift); [[Retinoic acid (drug)]] (+0.66, Retinoic receptor agonist); [[Larotrectinib (drug)]] (+0.66, Other TK inhibitor); [[Busulfan (drug)]] (+0.66, DNA synthesis/repair inhibitor); [[Palmatine (chloride) (drug)]] (+0.61, unclear); [[Tucatinib (drug)]] (+0.60, EGFR/ERBB inhibitor); [[MK-8353 (drug)]] (+0.60, Other MAPK inhibitor)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Lumateperone (tosylate)"
- `tables/drugdoses.parquet` — dd in 639, 640, 641
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
