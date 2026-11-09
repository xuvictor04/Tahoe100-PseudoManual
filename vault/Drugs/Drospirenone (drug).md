---
drug: "Drospirenone"
type: "drug"
salt_base: "Drospirenone"
targets: ""
moa_fine: "unclear"
moa_broad: "unclear"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 83
tags: ["drug", "moa/unclear"]
generated_by: "tahoemap"
---

# Drospirenone

*unclear (unclear) · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 6 / 83 / 8; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): low dose only (noise?).
> Signature similarity between consecutive doses (low–mid / mid–high): 0.27 / 0.03.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:A9 | 5 / 1 | — | -0.07 | +0.1/-0.9/+0.3 | — |
| 0.5 µM | [[Plate 11]]:A9 | 80 / 3 | — | -0.50 | -0.3/-0.4/+0.5 | — |
| 5 µM | [[Plate 12]]:A9 | 4 / 4 | — | +0.65 | -0.5/-1.0/-1.6 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (5 genes, none with an alert): [[GCNT1]] 1.24× (z +3.9, 12/43 lines), [[ENSG00000255339]] 1.27× (z +3.1, 0/45 lines), [[TEF]] 1.24× (z +3.0, 2/45 lines), [[MX1]] 1.30× (z +2.8, 13/29 lines), [[RDUR]] 1.32× (z +2.8, 1/18 lines)

**0.5 µM** (80 genes, none with an alert; 12 shown): [[ARGLU1]] 1.30× (z +4.8, 34/48 lines), [[NONO]] 1.22× (z +4.3, 22/48 lines), [[ENSG00000250137]] 1.59× (z +4.2, 2/16 lines), [[SVEP1]] 1.43× (z +4.0, 6/28 lines), [[CPNE1]] 1.20× (z +3.9, 23/48 lines), [[PWRN1]] 1.60× (z +3.8, 5/27 lines), [[STK11]] 1.20× (z +3.8, 9/45 lines), [[RNF17]] 1.78× (z +3.7, 0/3 lines), [[NRK]] 1.89× (z +3.7, 1/5 lines), [[ENSG00000291138]] 1.67× (z +3.7, 1/17 lines), [[LINC00648]] 1.58× (z +3.7, 1/10 lines), [[ITGA8]] 1.67× (z +3.7, 1/9 lines)

**5 µM** (4 genes, none with an alert): [[DHCR7]] 1.44× (z +3.7, 9/44 lines), [[ACSS2]] 1.25× (z +3.6, 17/47 lines), [[SCD]] 1.25× (z +3.1, 22/48 lines), [[SNAI3-AS1]] 1.34× (z +3.0, 2/46 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[SLC16A4-AS1]] 0.652× (z -3.6, 9/43 lines)

**0.5 µM** (3 genes, none with an alert): [[ENSG00000291259]] 0.688× (z -3.8, 13/44 lines), [[HAPLN3]] 0.753× (z -3.5, 13/36 lines), [[ARID5A]] 0.786× (z -3.1, 12/45 lines)

**5 µM** (4 genes, none with an alert): [[OSTC]] 0.762× (z -4.2, 32/48 lines), [[HDGFL2]] 0.752× (z -4.0, 15/48 lines), [[GRHL2]] 0.778× (z -3.7, 0/14 lines), [[ESRP1]] 0.807× (z -2.8, 0/17 lines)

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
| 0.5 µM | — | [[NCI-H661 (line)]] (1.82), [[AN3 CA (line)]] (1.65), [[HepG2_C3A (line)]] (1.48), [[SW 1088 (line)]] (1.39) · weakest: [[A498 (line)]] (0.332), [[Panc 03.27 (line)]] (0.374), [[H4 (line)]] (0.439) |
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Canagliflozin (hemihydrate) (drug)]] (+0.77, Glucose transporter inhibitor); [[Vemurafenib (drug)]] (+0.76, RAF inhibitor, ⚠ only 1 significant gene); [[Oxaprozin (drug)]] (+0.73, Cyclooxygenase inhibitor); [[Vitamin K4 (drug)]] (+0.73, unclear); [[Simotinib (drug)]] (+0.72, EGFR/ERBB inhibitor, ⚠ vector dose flagged: toxic); [[Bestatin (hydrochloride) (drug)]] (+0.71, unclear); [[Bimatoprost (drug)]] (+0.71, unclear); [[Bicalutamide (drug)]] (+0.70, Androgen receptor antagonist); [[Meloxicam (drug)]] (+0.69, Cyclooxygenase inhibitor); [[Isocorydine (drug)]] (+0.68, unclear)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Drospirenone"
- `tables/drugdoses.parquet` — dd in 383, 384, 385
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
