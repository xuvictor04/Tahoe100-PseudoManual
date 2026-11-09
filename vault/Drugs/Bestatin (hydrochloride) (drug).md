---
drug: "Bestatin (hydrochloride)"
type: "drug"
salt_base: "Bestatin"
targets: ""
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "0.05"
max_sig_genes: 119
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Bestatin (hydrochloride)

*unclear (inhibitor/antagonist) · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 119 / 12 / 1; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): low dose only (noise?).
> Signature similarity between consecutive doses (low–mid / mid–high): 0.49 / 0.21.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:A1 | 106 / 13 | — | -0.39 | -0.7/-2.5/-0.6 | — |
| 0.5 µM | [[Plate 11]]:A1 | 6 / 6 | — | +0.54 | -0.5/-0.8/-1.5 | — |
| 5 µM | [[Plate 12]]:A1 | 0 / 1 | — | +0.09 | +0.3/-0.9/+0.7 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (106 genes, none with an alert; 12 shown): [[PCLO]] 1.42× (z +4.7, 16/33 lines), [[DYNLL2]] 1.28× (z +4.7, 21/47 lines), [[LINC02267]] 1.78× (z +4.2, 0/2 lines), [[RHBDF2]] 1.26× (z +4.1, 15/43 lines), [[NLRC5]] 1.35× (z +4.0, 12/42 lines), [[TNIP3]] 1.52× (z +4.0, 2/13 lines), [[GLDN]] 1.54× (z +3.9, 5/22 lines), [[LHX4]] 1.49× (z +3.7, 3/33 lines), [[KNDC1]] 1.44× (z +3.7, 9/38 lines), [[SLC27A2]] 1.39× (z +3.7, 4/27 lines), [[ZNF747]] 1.55× (z +3.7, 5/35 lines), [[DGAT2]] 1.35× (z +3.6, 1/34 lines)

**0.5 µM** (6 genes, none with an alert): [[APH1B]] 1.24× (z +3.2, 8/42 lines), [[ENSG00000256625]] 1.40× (z +3.2, 3/41 lines), [[DGLUCY]] 1.21× (z +3.1, 11/46 lines), [[KDM4D]] 1.38× (z +3.1, 0/44 lines), [[SLC35F6]] 1.34× (z +3.0, 6/47 lines), [[SRGAP3]] 1.23× (z +2.9, 6/46 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (13 genes, none with an alert; 12 shown): [[NCAPH]] 0.786× (z -3.7, 12/46 lines), [[GAS2L3]] 0.820× (z -3.5, 7/48 lines), [[FAM83D]] 0.785× (z -3.5, 8/47 lines), [[KIF14]] 0.822× (z -3.3, 13/47 lines), [[KIF18A]] 0.797× (z -3.2, 14/47 lines), [[NUF2]] 0.795× (z -3.2, 13/47 lines), [[CCNF]] 0.830× (z -3.0, 10/47 lines), [[ECT2]] 0.786× (z -3.0, 21/47 lines), [[PIF1]] 0.788× (z -3.0, 6/45 lines), [[TTK]] 0.787× (z -2.9, 12/47 lines), [[BUB1]] 0.794× (z -2.9, 14/47 lines), [[UBA6]] 0.824× (z -2.8, 24/48 lines)

**0.5 µM** (6 genes, none with an alert): [[HBS1L]] 0.807× (z -4.1, 26/48 lines), [[KPNA1]] 0.809× (z -3.8, 19/48 lines), [[SNRPG]] 0.792× (z -3.6, 7/48 lines), [[SBDSP1-1]] 0.681× (z -3.6, 11/44 lines), [[EIF4E]] 0.809× (z -3.3, 20/48 lines), [[PSMD14]] 0.820× (z -2.9, 20/48 lines)

**5 µM** (1 gene, none with an alert): [[ZNF185]] 0.802× (z -3.2, 4/33 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | [[Module 207]] (-2.4) |
| 0.5 µM | — | — |
| 5 µM | — | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[SW 1271 (line)]] (1.60), [[hTERT-HPNE (line)]] (1.06), [[SW 900 (line)]] (1.04), [[SNU-423 (line)]] (1.04) · weakest: [[NCI-H2347 (line)]] (0.365), [[AN3 CA (line)]] (0.428), [[NCI-H460 (line)]] (0.506) |
| 0.5 µM | — | — |
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[Meloxicam (drug)]] (+0.84, Cyclooxygenase inhibitor); [[Vitamin K4 (drug)]] (+0.80, unclear); [[Oxaprozin (drug)]] (+0.80, Cyclooxygenase inhibitor); [[Benztropine (mesylate) (drug)]] (+0.76, unclear); [[Abiraterone acetate (drug)]] (+0.73, unclear); [[Drospirenone (drug)]] (+0.71, unclear); [[Canagliflozin (hemihydrate) (drug)]] (+0.67, Glucose transporter inhibitor); [[Nimesulide (drug)]] (+0.65, Cyclooxygenase inhibitor, ⚠ no trustworthy dose (vector dose flagged: toxic; unreliable plate only)); [[Isocorydine (drug)]] (+0.61, unclear)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Bestatin (hydrochloride)"
- `tables/drugdoses.parquet` — dd in 182, 183, 184
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
