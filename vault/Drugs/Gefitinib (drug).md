---
drug: "Gefitinib"
type: "drug"
salt_base: "Gefitinib"
targets: "EGFR"
moa_fine: "EGFR/ERBB inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 142
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Gefitinib

*EGFR/ERBB inhibitor (inhibitor/antagonist) · targets: EGFR · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 1 / 0 / 142; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.34 / 0.31.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:H3 | 0 / 1 | — | +0.50 | -0.2/+0.4/+0.6 | — |
| 0.5 µM | [[Plate 11]]:H3 | 0 / 0 | — | +0.41 | -0.7/-0.5/-0.3 | — |
| 5 µM | [[Plate 12]]:H3 | 93 / 49 | — | +0.83 | +0.3/+1.1/+0.6 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**5 µM** (93 genes, none with an alert; 12 shown): [[STPG4]] 1.58× (z +4.9, 23/46 lines), [[ENSG00000286533]] 1.51× (z +4.9, 21/43 lines), [[ADAM32]] 1.40× (z +4.6, 19/46 lines), [[SLC38A2]] 1.25× (z +4.4, 33/48 lines), [[TBX19]] 1.29× (z +4.3, 5/48 lines), [[GRK7]] 1.48× (z +4.3, 7/47 lines), [[CASS4]] 1.81× (z +4.3, 13/46 lines), [[IDI1]] 1.37× (z +4.2, 24/48 lines), [[CXCL2]] 1.68× (z +4.1, 19/34 lines), [[TICAM2]] 1.29× (z +4.1, 16/48 lines), [[LINC02889]] 1.51× (z +4.0, 5/36 lines), [[LSMEM1]] 1.81× (z +4.0, 22/48 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[ZNF667-AS1]] 0.675× (z -3.4, 0/14 lines)

**5 µM** (49 genes, none with an alert; 12 shown): [[ANKRD42-DT]] 0.798× (z -4.3, 8/48 lines), [[ZNF708]] 0.742× (z -4.3, 18/47 lines), [[PARL]] 0.824× (z -4.1, 23/48 lines), [[MCF2L2]] 0.808× (z -4.1, 13/43 lines), [[NMRAL1]] 0.772× (z -4.1, 13/45 lines), [[ZNF16]] 0.757× (z -4.0, 13/48 lines), [[ZNF777]] 0.767× (z -3.9, 8/48 lines), [[TMEM92-AS1]] 0.662× (z -3.8, 8/32 lines), [[IFNLR1]] 0.757× (z -3.8, 8/30 lines), [[ZNF251]] 0.805× (z -3.7, 16/48 lines), [[ARHGAP1]] 0.795× (z -3.7, 14/48 lines), [[ENSG00000285329]] 0.820× (z -3.7, 4/43 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | [[Module 170]] (-2.4), [[Module 030]] (-2.2) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | [[NCI-H460 (line)]] (2.16), [[HOP62 (line)]] (1.75), [[hTERT-HPNE (line)]] (1.56), [[CHP-212 (line)]] (1.56) · weakest: [[SK-MEL-2 (line)]] (0.495), [[SW1417 (line)]] (0.563), [[BT-474 (line)]] (0.594) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 6 next most similar without an alert.*

- [[Methylthiouracil (drug)]] (+0.61, unclear, ⚠ only 9 significant genes); [[Artemether (drug)]] (+0.60, unclear, ⚠ only 7 significant genes); [[Gemfibrozil (drug)]] (+0.54, unclear, ⚠ only 2 significant genes); [[Aliskiren (drug)]] (+0.51, unclear); [[Uridine (drug)]] (+0.45, unclear, ⚠ only 6 significant genes); [[Malotilate (drug)]] (+0.43, unclear); [[Tolcapone (drug)]] (+0.41, unclear, ⚠ only 6 significant genes); [[Rucaparib (phosphate) (drug)]] (+0.41, DNA synthesis/repair inhibitor, ⚠ only 5 significant genes); [[Clopidogrel (drug)]] (+0.39, unclear); [[Fusidic acid (drug)]] (+0.38, unclear); [[Tucatinib (drug)]] (+0.36, EGFR/ERBB inhibitor); [[Anethole trithione (drug)]] (+0.36, unclear); [[Omeprazole (drug)]] (+0.35, unclear); [[ERK5-IN-2 (drug)]] (+0.34, Other MAPK inhibitor)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Gefitinib"
- `tables/drugdoses.parquet` — dd in 498, 499, 500
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
