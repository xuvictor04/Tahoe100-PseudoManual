---
drug: "L-Eflornithine (monohydrochloride)"
type: "drug"
salt_base: "L-Eflornithine"
targets: "ODC1"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 34
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# L-Eflornithine (monohydrochloride)

*unclear (inhibitor/antagonist) · targets: ODC1 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 1 / 9 / 34; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.32 / -0.04.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:C5 | 1 / 0 | — | +0.36 | +0.6/+0.8/+0.5 | — |
| 0.5 µM | [[Plate 11]]:C5 | 2 / 7 | — | -0.28 | +0.6/+0.6/+0.5 | — |
| 5 µM | [[Plate 12]]:C5 | 20 / 14 | — | -0.25 | +0.9/+0.4/-0.4 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[RYR2]] 1.34× (z +2.9, 2/47 lines)

**0.5 µM** (2 genes, none with an alert): [[CYB561D1]] 1.25× (z +3.6, 3/43 lines), [[SALL4]] 1.28× (z +3.5, 3/25 lines)

**5 µM** (20 genes, none with an alert; 12 shown): [[JADE1]] 1.21× (z +3.7, 11/48 lines), [[SAMD9]] 1.55× (z +3.6, 29/37 lines), [[TRIM14]] 1.30× (z +3.5, 18/47 lines), [[HERC5]] 1.31× (z +3.4, 7/33 lines), [[MX2]] 1.48× (z +3.4, 21/32 lines), [[IFIT1]] 1.53× (z +3.2, 20/44 lines), [[ADAM12]] 1.23× (z +3.2, 3/21 lines), [[USP18]] 1.39× (z +3.2, 12/43 lines), [[STAT1]] 1.24× (z +3.2, 24/48 lines), [[XAF1]] 1.46× (z +3.2, 20/34 lines), [[RSAD2]] 1.51× (z +3.1, 11/34 lines), [[RIGI]] 1.31× (z +3.1, 16/45 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (7 genes, none with an alert): [[MMAA]] 0.707× (z -4.9, 15/43 lines), [[MYO15A]] 0.657× (z -3.8, 9/32 lines), [[CCDC102A]] 0.755× (z -3.2, 10/38 lines), [[CHST10]] 0.741× (z -3.1, 7/28 lines), [[TMEM11-DT]] 0.807× (z -2.9, 7/44 lines), [[ENSG00000285851]] 0.773× (z -2.9, 8/44 lines), [[LINC02086]] 0.797× (z -2.8, 7/23 lines)

**5 µM** (14 genes, none with an alert; 12 shown): [[ENSG00000284697]] 0.648× (z -4.1, 21/47 lines), [[TMEM68]] 0.828× (z -3.6, 10/47 lines), [[LINC02680]] 0.697× (z -3.3, 21/48 lines), [[CLEC4A]] 0.701× (z -3.3, 9/46 lines), [[FBXO31]] 0.814× (z -3.2, 14/48 lines), [[FUT3]] 0.746× (z -3.2, 1/18 lines), [[SPATA5L1]] 0.810× (z -3.2, 7/48 lines), [[KLRD1]] 0.674× (z -3.2, 11/39 lines), [[TMEM185A]] 0.810× (z -3.1, 7/47 lines), [[PPTC7]] 0.816× (z -3.1, 16/48 lines), [[HSF2]] 0.797× (z -3.1, 12/47 lines), [[FBXO42]] 0.817× (z -3.1, 22/48 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | [[Module 168]] (-2.4), [[Module 171]] (-2.1) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | [[SW 1088 (line)]] (1.44), [[SW 900 (line)]] (1.37), [[RKO (line)]] (1.24), [[NCI-H1792 (line)]] (1.23) · weakest: [[AN3 CA (line)]] (0.296), [[NCI-H661 (line)]] (0.351), [[NCI-H2030 (line)]] (0.455) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar.*

- [[Estrone sulfate (potassium) (drug)]] (+0.95, unclear); [[Carbamazepine (drug)]] (+0.84, HDAC inhibitor); [[Apalutamide (drug)]] (+0.83, Androgen receptor antagonist); [[Esmolol (hydrochloride) (drug)]] (+0.80, unclear); [[Larotrectinib (drug)]] (+0.80, Other TK inhibitor); [[Busulfan (drug)]] (+0.79, DNA synthesis/repair inhibitor); [[(R)-Verapamil (hydrochloride) (drug)]] (+0.79, unclear); [[Diphenhydramine (drug)]] (+0.79, unclear)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "L-Eflornithine (monohydrochloride)"
- `tables/drugdoses.parquet` — dd in 582, 583, 584
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
