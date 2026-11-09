---
drug: "Abiraterone acetate"
type: "drug"
salt_base: "Abiraterone acetate"
targets: "CYP17A1"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.05"
max_sig_genes: 167
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Abiraterone acetate

*unclear (inhibitor/antagonist) · targets: CYP17A1 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 167 / 1 / 2; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): low dose only (noise?).
> Signature similarity between consecutive doses (low–mid / mid–high): 0.17 / 0.05.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:D1 | 159 / 8 | — | +0.42 | +0.3/-1.9/-0.5 | — |
| 0.5 µM | [[Plate 11]]:D1 | 0 / 1 | — | +0.49 | -0.8/-0.6/-1.4 | — |
| 5 µM | [[Plate 12]]:D1 | 0 / 2 | — | -0.05 | -0.2/-0.5/+0.3 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (159 genes, none with an alert; 12 shown): [[PCLO]] 1.54× (z +5.8, 21/34 lines), [[SIPA1L2]] 1.37× (z +4.8, 12/39 lines), [[ENSG00000286540]] 1.51× (z +4.5, 10/25 lines), [[WWOX]] 1.40× (z +4.4, 35/44 lines), [[SLC43A2]] 1.37× (z +4.3, 10/44 lines), [[MX1]] 1.46× (z +4.1, 25/30 lines), [[SLC7A11]] 1.39× (z +4.0, 23/43 lines), [[RSAD2]] 1.69× (z +4.0, 19/35 lines), [[MOCOS]] 1.30× (z +4.0, 10/41 lines), [[NMRAL2P]] 1.54× (z +3.9, 11/29 lines), [[LRP1B]] 1.36× (z +3.9, 12/23 lines), [[KYNU]] 1.36× (z +3.9, 9/20 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (8 genes, none with an alert): [[ENSG00000272980]] 0.751× (z -3.7, 6/45 lines), [[SNAPC3]] 0.823× (z -3.5, 19/49 lines), [[ESYT2]] 0.815× (z -3.2, 26/49 lines), [[TADA1]] 0.806× (z -3.2, 4/47 lines), [[INSIG2]] 0.815× (z -2.9, 21/49 lines), [[EFNA3]] 0.777× (z -2.9, 6/47 lines), [[BORA]] 0.798× (z -2.8, 7/48 lines), [[ENSG00000257759]] 0.829× (z -2.6, 7/48 lines)

**0.5 µM** (1 gene, none with an alert): [[GRHL2]] 0.820× (z -2.9, 0/14 lines)

**5 µM** (2 genes, none with an alert): [[HMGCR]] 0.811× (z -3.0, 15/48 lines), [[MSMO1]] 0.755× (z -3.0, 18/47 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 137]] (+2.8) | [[Module 207]] (-2.9) |
| 0.5 µM | — | — |
| 5 µM | — | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[SW48 (line)]] (1.29), [[A549 (line)]] (1.25), [[CFPAC-1 (line)]] (1.23), [[NCI-H2122 (line)]] (1.23) · weakest: [[NCI-H661 (line)]] (0.553), [[SW 1271 (line)]] (0.591), [[A-427 (line)]] (0.597) |
| 0.5 µM | — | — |
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar.*

- [[Meloxicam (drug)]] (+0.91, Cyclooxygenase inhibitor); [[Benztropine (mesylate) (drug)]] (+0.85, unclear); [[Vitamin K4 (drug)]] (+0.80, unclear); [[Brimonidine (drug)]] (+0.80, Adrenoceptor agonist); [[Bestatin (hydrochloride) (drug)]] (+0.73, unclear); [[Finasteride (drug)]] (+0.72, unclear); [[Esmolol (hydrochloride) (drug)]] (+0.69, unclear); [[Apalutamide (drug)]] (+0.63, Androgen receptor antagonist)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Abiraterone acetate"
- `tables/drugdoses.parquet` — dd in 45, 46, 47
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
