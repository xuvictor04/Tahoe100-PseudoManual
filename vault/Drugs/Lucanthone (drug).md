---
drug: "Lucanthone"
type: "drug"
salt_base: "Lucanthone"
targets: ""
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "0.05"
max_sig_genes: 82
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Lucanthone

*unclear (inhibitor/antagonist) · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 82 / 1 / 13; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.26 / 0.26.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:C1 | 2 / 80 | — | +1.22 | -0.6/-0.5/-1.7 | — |
| 0.5 µM | [[Plate 08]]:C1 | 1 / 0 | — | -0.14 | -0.9/-0.1/+0.0 | — |
| 5 µM | [[Plate 09]]:C1 | 10 / 3 | — | +0.51 | -0.7/-0.3/-0.3 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (2 genes, none with an alert): [[LIN7C]] 1.30× (z +3.0, 16/48 lines), [[GNS]] 1.22× (z +2.9, 14/48 lines)

**0.5 µM** (1 gene, none with an alert): [[RPL4]] 1.25× (z +3.0, 31/48 lines)

**5 µM** (10 genes, none with an alert): [[AHRR]] 1.27× (z +3.7, 18/45 lines), [[DMPK]] 1.23× (z +3.7, 11/48 lines), [[CYP1B1-AS1]] 1.54× (z +3.7, 8/33 lines), [[SLC22A20P]] 1.43× (z +3.4, 5/43 lines), [[RMDN2-AS1]] 1.61× (z +3.3, 13/30 lines), [[SCD]] 1.27× (z +3.2, 24/49 lines), [[GARIN1A]] 1.58× (z +3.2, 12/48 lines), [[TPRA1]] 1.22× (z +3.0, 7/48 lines), [[C3orf20]] 1.43× (z +3.0, 7/46 lines), [[ALDH1A3]] 1.27× (z +2.9, 5/27 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (80 genes, none with an alert; 12 shown): [[ZNF667-AS1]] 0.548× (z -4.8, 0/14 lines), [[HNF4A]] 0.692× (z -4.5, 0/14 lines), [[LINC02335]] 0.539× (z -4.3, 1/7 lines), [[PXN-AS1]] 0.661× (z -4.2, 10/47 lines), [[UTY]] 0.776× (z -4.0, 0/17 lines), [[EYA2]] 0.724× (z -3.9, 0/14 lines), [[SKAP1]] 0.747× (z -3.9, 0/14 lines), [[RGPD2]] 0.591× (z -3.9, 0/11 lines), [[ENSG00000203434]] 0.382× (z -3.8, 0/7 lines), [[ANKRD20A9P]] 0.570× (z -3.8, 1/8 lines), [[MT1M]] 0.326× (z -3.8, 3/17 lines), [[PDGFD]] 0.601× (z -3.7, 0/24 lines)

**5 µM** (3 genes, none with an alert): [[DIXDC1]] 0.754× (z -5.5, 19/48 lines), [[HERC3]] 0.688× (z -4.2, 33/47 lines), [[GNG2]] 0.794× (z -3.2, 4/26 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 025]] (+2.5), [[Module 029]] (+2.2), [[Module 020]] (+2.1) | [[Module 024]] (-2.6), [[Module 054]] (-2.4), [[Module 177]] (-2.4) |
| 0.5 µM | — | — |
| 5 µM | — | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[AN3 CA (line)]] (1.92), [[SW 1088 (line)]] (1.89), [[NCI-H661 (line)]] (1.88), [[SW 1271 (line)]] (1.73) · weakest: [[KATO III (line)]] (0.666), [[SW480 (line)]] (0.680), [[NCI-H2347 (line)]] (0.718) |
| 0.5 µM | — | — |
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Fenofibrate (drug)]] (+0.90, unclear); [[Rutin (trihydrate) (drug)]] (+0.90, unclear); [[Tucatinib (drug)]] (+0.87, EGFR/ERBB inhibitor); [[Benproperine (phosphate) (drug)]] (+0.87, unclear); [[Erlotinib (drug)]] (+0.86, EGFR/ERBB inhibitor); [[Anethole trithione (drug)]] (+0.77, unclear); [[Paclitaxel (drug)]] (+0.77, Microtubule inhibitor, ⚠ only 3 significant genes); [[Methyl aminolevulinate (hydrochloride) (drug)]] (+0.74, unclear, ⚠ only 3 significant genes); [[MK-8353 (drug)]] (+0.71, Other MAPK inhibitor); [[Encorafenib (drug)]] (+0.68, RAF inhibitor)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Lucanthone"
- `tables/drugdoses.parquet` — dd in 636, 637, 638
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
