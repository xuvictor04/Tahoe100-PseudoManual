---
drug: "Perindopril (erbumine)"
type: "drug"
salt_base: "Perindopril"
targets: "STAT3, ACE"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 18
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Perindopril (erbumine)

*unclear (inhibitor/antagonist) · targets: STAT3, ACE · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 1 / 0 / 18; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.13 / 0.04.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:H6 | 1 / 0 | — | +0.93 | -0.2/-0.3/-0.3 | — |
| 0.5 µM | [[Plate 11]]:H6 | 0 / 0 | — | +0.80 | -0.7/+0.0/-0.5 | — |
| 5 µM | [[Plate 12]]:H6 | 1 / 17 | — | +0.33 | +0.1/-0.0/-0.2 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[CFAP210]] 1.70× (z +2.9, 15/46 lines)

**5 µM** (1 gene, none with an alert): [[GBP2]] 1.26× (z +3.5, 7/35 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**5 µM** (17 genes, none with an alert; 12 shown): [[CDCP1]] 0.767× (z -4.4, 24/32 lines), [[PLEK2]] 0.726× (z -3.6, 11/31 lines), [[SPRY4]] 0.766× (z -3.4, 17/48 lines), [[PHC2]] 0.812× (z -3.2, 19/48 lines), [[ITGA2]] 0.785× (z -3.2, 20/37 lines), [[CORO2B]] 0.745× (z -3.1, 8/34 lines), [[LINC00659]] 0.668× (z -3.1, 7/20 lines), [[PAQR5]] 0.832× (z -3.0, 7/37 lines), [[LAMC2]] 0.797× (z -3.0, 8/21 lines), [[DUSP6]] 0.720× (z -2.9, 23/44 lines), [[FERMT1]] 0.792× (z -2.8, 11/26 lines), [[NLRP3]] 0.699× (z -2.8, 4/19 lines)

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

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[Elimusertib hydrochloride (drug)]] (+0.77, unclear); [[Trametinib (DMSO_TF solvate) (drug)]] (+0.76, MEK inhibitor); [[Trametinib (drug)]] (+0.73, MEK inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Binimetinib (drug)]] (+0.71, MEK inhibitor); [[Bimiralisib (drug)]] (+0.68, PI3K/AKT inhibitor); [[Cobimetinib (drug)]] (+0.67, MEK inhibitor); [[AZD-7648 (drug)]] (+0.60, DNA synthesis/repair inhibitor); [[Capmatinib (drug)]] (+0.59, EGFR/ERBB inhibitor); [[BI-3406 (drug)]] (+0.59, RAS inhibitor)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Perindopril (erbumine)"
- `tables/drugdoses.parquet` — dd in 800, 801, 802
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
