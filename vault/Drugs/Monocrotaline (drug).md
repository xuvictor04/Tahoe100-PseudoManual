---
drug: "Monocrotaline"
type: "drug"
salt_base: "Monocrotaline"
targets: "SLC22A1, SLC22A2"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "0.05"
max_sig_genes: 23
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Monocrotaline

*unclear (inhibitor/antagonist) · targets: SLC22A1, SLC22A2 · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 23 / 4 / 3; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): low dose only (noise?).
> Signature similarity between consecutive doses (low–mid / mid–high): -0.00 / -0.07.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:D4 | 22 / 1 | — | -0.50 | -0.1/-0.1/+0.2 | — |
| 0.5 µM | [[Plate 08]]:D4 | 1 / 3 | — | +0.16 | +0.6/+0.6/+0.6 | — |
| 5 µM | [[Plate 09]]:D4 | 1 / 2 | — | -0.12 | +0.7/+0.2/-0.6 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (22 genes, none with an alert; 12 shown): [[DTD2]] 1.28× (z +3.6, 7/42 lines), [[ZBED9]] 1.45× (z +3.5, 1/25 lines), [[LCA5L]] 1.40× (z +3.4, 2/32 lines), [[CPEB1]] 1.34× (z +3.4, 1/19 lines), [[ZNF329]] 1.22× (z +3.4, 5/40 lines), [[TMEM229B]] 1.40× (z +3.3, 1/20 lines), [[WIPF3]] 1.38× (z +3.3, 1/23 lines), [[ELAPOR1]] 1.43× (z +3.2, 2/23 lines), [[NRTN]] 1.47× (z +3.1, 0/22 lines), [[GTPBP3]] 1.25× (z +3.1, 6/42 lines), [[ANGPTL2]] 1.51× (z +3.1, 0/14 lines), [[ENSG00000291063]] 1.44× (z +3.1, 1/28 lines)

**0.5 µM** (1 gene, none with an alert): [[ENSG00000249328]] 1.29× (z +2.9, 3/45 lines)

**5 µM** (1 gene, none with an alert): [[LCA5L]] 1.34× (z +3.1, 5/40 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[HOXB4]] 0.795× (z -2.8, 8/34 lines)

**0.5 µM** (3 genes, none with an alert): [[LRATD1]] 0.672× (z -3.9, 1/16 lines), [[TP73]] 0.774× (z -3.1, 3/32 lines), [[BAP1]] 0.826× (z -3.0, 8/48 lines)

**5 µM** (2 genes, none with an alert): [[FUT11]] 0.778× (z -2.9, 26/48 lines), [[RNF144B]] 0.824× (z -2.8, 4/31 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | [[Module 045]] (-2.0) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[AN3 CA (line)]] (2.02), [[SW 1271 (line)]] (1.90), [[COLO 205 (line)]] (1.81), [[CHP-212 (line)]] (1.71) · weakest: [[A-427 (line)]] (-0.221), [[NCI-H1573 (line)]] (-0.197), [[SW480 (line)]] (-0.171) |
| 0.5 µM | — | — |
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 3 next most similar without an alert.*

- [[Orlistat (drug)]] (+0.69, unclear); [[Canagliflozin (drug)]] (+0.65, Glucose transporter inhibitor); [[Hydroxyurea (drug)]] (+0.64, DNA synthesis/repair inhibitor); [[Oxaprozin (drug)]] (+0.63, Cyclooxygenase inhibitor); [[Topotecan (hydrochloride) (drug)]] (+0.56, DNA synthesis/repair inhibitor, ⚠ vector dose flagged: toxic; cell-cycle shift); [[Imiquimod (hydrochloride) (drug)]] (+0.56, unclear, ⚠ vector dose flagged: toxic); [[Dexmedetomidine (drug)]] (+0.54, Adrenoceptor agonist, ⚠ only 9 significant genes); [[Pyridoxine (drug)]] (+0.54, unclear); [[Canagliflozin (hemihydrate) (drug)]] (+0.52, Glucose transporter inhibitor); [[Bimatoprost (drug)]] (+0.51, unclear); [[Decitabine (drug)]] (+0.51, DNA methyltransferase inhibitor)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Monocrotaline"
- `tables/drugdoses.parquet` — dd in 693, 694, 695
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
