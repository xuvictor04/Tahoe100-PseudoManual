---
drug: "Meloxicam"
type: "drug"
salt_base: "Meloxicam"
targets: "PTGS1, PTGS2"
moa_fine: "Cyclooxygenase inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.05"
max_sig_genes: 57
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Meloxicam

*Cyclooxygenase inhibitor (inhibitor/antagonist) · targets: PTGS1, PTGS2 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 57 / 4 / 2; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): low dose only (noise?).
> Signature similarity between consecutive doses (low–mid / mid–high): 0.39 / 0.14.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:E1 | 56 / 1 | — | -0.01 | -0.9/-1.7/-1.1 | — |
| 0.5 µM | [[Plate 11]]:E1 | 0 / 4 | — | -0.17 | -1.8/-0.9/-1.8 | — |
| 5 µM | [[Plate 12]]:E1 | 0 / 2 | — | -0.49 | -0.5/-1.0/-0.9 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (56 genes, none with an alert; 12 shown): [[PCLO]] 1.39× (z +4.4, 16/33 lines), [[ENSG00000227681]] 1.27× (z +3.7, 1/31 lines), [[TM9SF5P]] 1.41× (z +3.6, 13/45 lines), [[CCDC171]] 1.42× (z +3.4, 15/45 lines), [[CACNA1D]] 1.25× (z +3.4, 2/24 lines), [[PRKG1]] 1.26× (z +3.3, 3/25 lines), [[GABPB1-AS1]] 1.25× (z +3.3, 15/46 lines), [[SLC38A10]] 1.21× (z +3.3, 10/48 lines), [[GABPB2]] 1.27× (z +3.3, 8/47 lines), [[GRAMD1B]] 1.32× (z +3.3, 3/17 lines), [[KCNMB2-AS1]] 1.41× (z +3.3, 8/33 lines), [[SEMA3D]] 1.29× (z +3.2, 0/15 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[RNF139-DT]] 0.757× (z -3.1, 4/44 lines)

**0.5 µM** (4 genes, none with an alert): [[IDH3A]] 0.808× (z -4.1, 16/47 lines), [[PDE12]] 0.803× (z -3.5, 11/47 lines), [[PSMC6]] 0.827× (z -3.0, 19/48 lines), [[URB2]] 0.805× (z -2.9, 9/46 lines)

**5 µM** (2 genes, none with an alert): [[IRF2BP2]] 0.820× (z -3.0, 18/47 lines), [[THEMIS2]] 0.784× (z -2.7, 1/27 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | [[Module 207]] (-2.0) |
| 0.5 µM | — | — |
| 5 µM | — | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[SW 1271 (line)]] (1.53), [[NCI-H2030 (line)]] (1.32), [[H4 (line)]] (1.31), [[NCI-H1573 (line)]] (1.22) · weakest: [[RKO (line)]] (0.374), [[LS 180 (line)]] (0.435), [[NCI-H23 (line)]] (0.476) |
| 0.5 µM | — | — |
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar.*

- [[Abiraterone acetate (drug)]] (+0.91, unclear); [[Vitamin K4 (drug)]] (+0.88, unclear); [[Benztropine (mesylate) (drug)]] (+0.84, unclear); [[Bestatin (hydrochloride) (drug)]] (+0.84, unclear); [[Brimonidine (drug)]] (+0.74, Adrenoceptor agonist); [[Drospirenone (drug)]] (+0.69, unclear); [[Finasteride (drug)]] (+0.67, unclear); [[Mitoxantrone (dihydrochloride) (drug)]] (+0.63, DNA synthesis/repair inhibitor)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Meloxicam"
- `tables/drugdoses.parquet` — dd in 666, 667, 668
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
