---
drug: "Elagolix sodium"
type: "drug"
salt_base: "Elagolix sodium"
targets: "GNRHR"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 21
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Elagolix sodium

*unclear (inhibitor/antagonist) · targets: GNRHR · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 1 / 21 / 4; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): low dose only (noise?).
> Signature similarity between consecutive doses (low–mid / mid–high): 0.22 / 0.29.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:D1 | 1 / 0 | — | -0.05 | -0.3/-0.3/+0.4 | — |
| 0.5 µM | [[Plate 05]]:D1 | 14 / 7 | — | -0.35 | +0.1/+0.5/+0.2 | — |
| 5 µM | [[Plate 14]]:D1 | 2 / 2 | 0.751 | -0.25 | +0.1/+1.2/+1.1 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[CCNYL2]] 1.28× (z +3.1, 0/16 lines)

**0.5 µM** (14 genes, none with an alert; 12 shown): [[KDM5D]] 1.39× (z +4.6, 1/18 lines), [[ENSG00000267284]] 1.38× (z +4.2, 1/15 lines), [[LRRN3]] 1.42× (z +3.4, 2/33 lines), [[FGF5]] 1.37× (z +3.3, 0/18 lines), [[STAG3]] 1.30× (z +3.3, 3/24 lines), [[COX7B2]] 1.58× (z +3.2, 0/5 lines), [[ENSG00000260167]] 1.40× (z +3.1, 3/26 lines), [[IRX2]] 1.70× (z +3.1, 0/16 lines), [[ENSG00000197670]] 1.33× (z +3.1, 6/44 lines), [[LINC01320]] 1.35× (z +3.1, 1/7 lines), [[PLXNC1]] 1.29× (z +3.0, 4/34 lines), [[NSMCE1-DT]] 1.37× (z +3.0, 5/31 lines)

**5 µM** (2 genes, none with an alert): [[ZNF382]] 1.22× (z +3.2, 0/29 lines), [[RNF166]] 1.26× (z +3.1, 4/47 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (7 genes, none with an alert): [[ZNF699]] 0.791× (z -4.2, 15/48 lines), [[BAG3]] 0.800× (z -3.9, 19/48 lines), [[ZNF764]] 0.758× (z -3.7, 6/44 lines), [[TMEM230]] 0.822× (z -3.7, 18/48 lines), [[DDX56]] 0.791× (z -3.6, 13/47 lines), [[TMEM138]] 0.811× (z -3.3, 9/45 lines), [[ENSG00000290890]] 0.806× (z -3.3, 13/47 lines)

**5 µM** (2 genes, none with an alert): [[ENSG00000249328]] 0.785× (z -4.0, 6/45 lines), [[SLC35C1]] 0.790× (z -3.4, 11/44 lines)

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
| 0.5 µM | — | [[C32 (line)]] (1.77), [[Panc 03.27 (line)]] (1.67), [[NCI-H661 (line)]] (1.55), [[AsPC-1 (line)]] (1.42) · weakest: [[NCI-H23 (line)]] (-0.187), [[SHP-77 (line)]] (-0.0805), [[CFPAC-1 (line)]] (0.106) |
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 3 next most similar without an alert.*

- [[Flutamide (drug)]] (+0.72, Androgen receptor antagonist); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] (+0.72, Glucose transporter inhibitor); [[Dorzolamide (hydrochloride) (drug)]] (+0.68, unclear); [[Verteporfin (drug)]] (+0.60, unclear); [[Clofarabine (drug)]] (+0.60, DNA synthesis/repair inhibitor, ⚠ only 8 significant genes); [[Allantoin (drug)]] (+0.56, unclear); [[Tolmetin (drug)]] (+0.53, Cyclooxygenase inhibitor, ⚠ only 4 significant genes); [[Imiquimod (hydrochloride) (drug)]] (+0.51, unclear, ⚠ vector dose flagged: toxic); [[Bicalutamide (drug)]] (+0.48, Androgen receptor antagonist); [[Vitamin K4 (drug)]] (+0.47, unclear); [[Drospirenone (drug)]] (+0.47, unclear)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Elagolix sodium"
- `tables/drugdoses.parquet` — dd in 401, 402, 403
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
