---
drug: "Esmolol (hydrochloride)"
type: "drug"
salt_base: "Esmolol"
targets: "ADRB1"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 120
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Esmolol (hydrochloride)

*unclear (inhibitor/antagonist) · targets: ADRB1 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 1 / 10 / 120; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.37 / 0.01.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:A6 | 1 / 0 | — | +0.76 | -0.4/-0.3/-0.1 | — |
| 0.5 µM | [[Plate 11]]:A6 | 7 / 3 | — | -0.27 | -0.0/-0.1/+0.9 | — |
| 5 µM | [[Plate 12]]:A6 | 84 / 36 | — | +0.65 | +0.2/-0.4/-1.8 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[RYR2]] 1.39× (z +3.3, 10/48 lines)

**0.5 µM** (7 genes, none with an alert): [[ENSG00000258653]] 1.37× (z +3.9, 7/43 lines), [[LSM6]] 1.27× (z +3.5, 13/47 lines), [[LINC00705]] 1.34× (z +3.4, 1/29 lines), [[LINC02603]] 1.36× (z +3.3, 2/41 lines), [[RNF212]] 1.29× (z +2.9, 1/12 lines), [[TSPOAP1]] 1.47× (z +2.9, 1/20 lines), [[ENSG00000243024]] 1.31× (z +2.8, 1/40 lines)

**5 µM** (84 genes, none with an alert; 12 shown): [[NRG1]] 1.29× (z +4.0, 15/29 lines), [[TMEM45A]] 1.38× (z +4.0, 20/35 lines), [[IRS1]] 1.35× (z +3.8, 15/42 lines), [[AFG1L]] 1.32× (z +3.8, 18/47 lines), [[RIGI]] 1.39× (z +3.8, 31/45 lines), [[PLCB1]] 1.27× (z +3.7, 15/29 lines), [[ENSG00000249738]] 1.36× (z +3.7, 14/29 lines), [[LTBP1]] 1.22× (z +3.7, 9/33 lines), [[PCDH7]] 1.40× (z +3.7, 18/30 lines), [[TNC]] 1.38× (z +3.7, 13/25 lines), [[SYTL2]] 1.33× (z +3.7, 11/41 lines), [[ENSG00000239498]] 1.43× (z +3.7, 7/27 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (3 genes, none with an alert): [[GUSBP18]] 0.788× (z -4.0, 18/47 lines), [[NOTCH2NLA]] 0.776× (z -3.4, 10/42 lines), [[WASH2P-1]] 0.700× (z -3.3, 13/41 lines)

**5 µM** (36 genes, none with an alert; 12 shown): [[NDUFV2]] 0.805× (z -4.3, 24/48 lines), [[ZUP1]] 0.758× (z -4.2, 17/48 lines), [[RHEBL1]] 0.582× (z -3.9, 14/46 lines), [[CDC37L1]] 0.803× (z -3.8, 16/48 lines), [[TGDS]] 0.778× (z -3.7, 13/48 lines), [[PSMC6]] 0.795× (z -3.7, 24/48 lines), [[C16orf87]] 0.745× (z -3.6, 18/48 lines), [[MAX]] 0.806× (z -3.6, 24/48 lines), [[TUBE1]] 0.690× (z -3.6, 20/48 lines), [[SASS6]] 0.797× (z -3.6, 14/48 lines), [[JMY]] 0.801× (z -3.6, 21/47 lines), [[MTF2]] 0.814× (z -3.5, 24/48 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[Module 200]] (+2.3), [[Module 088]] (+2.1), [[Module 010]] (+2.0) | [[Module 207]] (-2.8), [[Module 168]] (-2.7), [[Module 182]] (-2.6) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | [[NCI-H1792 (line)]] (1.39), [[CHP-212 (line)]] (1.35), [[MIA PaCa-2 (line)]] (1.29), [[A549 (line)]] (1.25) · weakest: [[AN3 CA (line)]] (0.312), [[BT-474 (line)]] (0.366), [[NCI-H661 (line)]] (0.398) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar.*

- [[Diphenhydramine (drug)]] (+0.91, unclear); [[Apalutamide (drug)]] (+0.90, Androgen receptor antagonist); [[Tirabrutinib (drug)]] (+0.89, Other TK inhibitor); [[(R)-Verapamil (hydrochloride) (drug)]] (+0.87, unclear); [[Busulfan (drug)]] (+0.86, DNA synthesis/repair inhibitor); [[Omeprazole (drug)]] (+0.84, unclear); [[Brimonidine (drug)]] (+0.83, Adrenoceptor agonist); [[Estrone sulfate (potassium) (drug)]] (+0.83, unclear)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Esmolol (hydrochloride)"
- `tables/drugdoses.parquet` — dd in 429, 430, 431
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
