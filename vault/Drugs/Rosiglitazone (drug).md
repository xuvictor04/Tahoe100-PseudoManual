---
drug: "Rosiglitazone"
type: "drug"
salt_base: "Rosiglitazone"
targets: "PPARG, TRPC5, TRPM3"
moa_fine: "unclear"
moa_broad: "unclear"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 43
tags: ["drug", "moa/unclear"]
generated_by: "tahoemap"
---

# Rosiglitazone

*unclear (unclear) · targets: PPARG, TRPC5, TRPM3 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 1 / 4 / 43; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.35 / 0.27.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:F2 | 1 / 0 | — | +0.46 | +0.9/+0.8/+0.2 | — |
| 0.5 µM | [[Plate 08]]:F2 | 4 / 0 | — | +0.02 | +0.4/+0.6/+0.6 | — |
| 5 µM | [[Plate 09]]:F2 | 39 / 4 | — | -0.42 | +0.7/+1.0/+1.3 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[ACSL5]] 1.24× (z +3.1, 7/23 lines)

**0.5 µM** (4 genes, none with an alert): [[PDK4]] 1.42× (z +3.2, 11/23 lines), [[ACSL5]] 1.21× (z +3.1, 7/24 lines), [[STON2]] 1.22× (z +3.0, 8/28 lines), [[PLIN2]] 1.41× (z +3.0, 16/31 lines)

**5 µM** (39 genes, none with an alert; 12 shown): [[PDK4]] 2.15× (z +6.7, 18/23 lines), [[CPT1A]] 1.42× (z +6.4, 30/46 lines), [[PLIN2]] 2.03× (z +5.9, 27/31 lines), [[LPCAT3]] 1.34× (z +5.3, 20/47 lines), [[ACSL5]] 1.39× (z +5.1, 9/23 lines), [[CASC11]] 1.42× (z +4.0, 2/32 lines), [[ACAA2]] 1.36× (z +3.9, 22/46 lines), [[ABCC3]] 1.33× (z +3.8, 16/31 lines), [[GDE1]] 1.26× (z +3.6, 17/47 lines), [[STON2]] 1.28× (z +3.5, 9/28 lines), [[PLPP2]] 1.35× (z +3.5, 8/38 lines), [[LINC00960]] 1.28× (z +3.5, 1/23 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**5 µM** (4 genes, none with an alert): [[GLRB]] 0.774× (z -3.3, 4/27 lines), [[FAM117A]] 0.814× (z -3.2, 9/44 lines), [[TNFRSF14]] 0.720× (z -3.1, 9/31 lines), [[ABCA5]] 0.830× (z -3.0, 13/43 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | [[Module 179]] (-2.1) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | [[Hs 766T (line)]] (1.45), [[NCI-H661 (line)]] (1.41), [[AsPC-1 (line)]] (1.34), [[COLO 205 (line)]] (1.31) · weakest: [[HEC-1-A (line)]] (-0.147), [[AN3 CA (line)]] (0.179), [[RKO (line)]] (0.269) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[Pioglitazone (drug)]] (+0.67, unclear); [[Mifepristone (drug)]] (+0.65, unclear); [[Isocorydine (drug)]] (+0.63, unclear); [[Simotinib (drug)]] (+0.61, EGFR/ERBB inhibitor, ⚠ vector dose flagged: toxic); [[Apalutamide (drug)]] (+0.60, Androgen receptor antagonist); [[Vitamin K4 (drug)]] (+0.59, unclear); [[Carbamazepine (drug)]] (+0.59, HDAC inhibitor); [[Gallic acid (hydrate) (drug)]] (+0.59, Cyclooxygenase inhibitor); [[L-Eflornithine (monohydrochloride) (drug)]] (+0.58, unclear)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Rosiglitazone"
- `tables/drugdoses.parquet` — dd in 911, 912, 913
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
