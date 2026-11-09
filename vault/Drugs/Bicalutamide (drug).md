---
drug: "Bicalutamide"
type: "drug"
salt_base: "Bicalutamide"
targets: "AR"
moa_fine: "Androgen receptor antagonist"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 30
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Bicalutamide

*Androgen receptor antagonist (inhibitor/antagonist) · targets: AR · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 3 / 30 / 1; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): low dose only (noise?).
> Signature similarity between consecutive doses (low–mid / mid–high): 0.23 / 0.17.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:A8 | 2 / 1 | — | +0.41 | -0.7/-0.4/-1.5 | — |
| 0.5 µM | [[Plate 11]]:A8 | 29 / 1 | — | -0.33 | -0.6/+0.1/-0.2 | — |
| 5 µM | [[Plate 12]]:A8 | 1 / 0 | — | +0.66 | -0.4/-0.5/-1.3 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (2 genes, none with an alert): [[RYR2]] 1.34× (z +2.9, 2/48 lines), [[MOCS3]] 1.32× (z +2.8, 1/46 lines)

**0.5 µM** (29 genes, none with an alert; 12 shown): [[LENG9]] 1.55× (z +3.5, 3/40 lines), [[CYRIA]] 1.34× (z +3.5, 1/22 lines), [[MAP3K12]] 1.28× (z +3.4, 11/47 lines), [[BCHE]] 1.34× (z +3.4, 0/13 lines), [[LINC01435]] 1.49× (z +3.3, 0/9 lines), [[TPTE2P6]] 1.20× (z +3.3, 2/46 lines), [[LINC02566]] 1.91× (z +3.2, 0/2 lines), [[ENSG00000255886]] 1.35× (z +3.2, 0/43 lines), [[EAF1-AS1]] 1.45× (z +3.2, 2/43 lines), [[ENSG00000279501]] 1.41× (z +3.2, 2/44 lines), [[NCAM1]] 1.33× (z +3.2, 0/14 lines), [[PRXL2B]] 1.31× (z +3.1, 3/43 lines)

**5 µM** (1 gene, none with an alert): [[ENSG00000237356]] 1.27× (z +3.0, 1/42 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[WDR43]] 0.827× (z -3.1, 23/48 lines)

**0.5 µM** (1 gene, none with an alert): [[DHRS11]] 0.765× (z -3.4, 10/43 lines)

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
| 0.5 µM | — | [[A549 (line)]] (1.33), [[SHP-77 (line)]] (1.30), [[C32 (line)]] (1.27), [[NCI-H1792 (line)]] (1.24) · weakest: [[hTERT-HPNE (line)]] (0.240), [[LoVo (line)]] (0.299), [[SW 900 (line)]] (0.307) |
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Bendamustine (drug)]] (+0.87, DNA synthesis/repair inhibitor); [[Decitabine (drug)]] (+0.78, DNA methyltransferase inhibitor); [[Canagliflozin (hemihydrate) (drug)]] (+0.73, Glucose transporter inhibitor); [[Sivelestat (sodium tetrahydrate) (drug)]] (+0.73, unclear); [[Methylprednisolone succinate (drug)]] (+0.73, Glucocorticoid receptor agonist); [[Docetaxel (Trihydrate) (drug)]] (+0.71, Microtubule inhibitor); [[Darolutamide (drug)]] (+0.71, Androgen receptor antagonist, ⚠ only 5 significant genes); [[Imiquimod (hydrochloride) (drug)]] (+0.71, unclear, ⚠ vector dose flagged: toxic); [[Drospirenone (drug)]] (+0.70, unclear); [[Celecoxib (drug)]] (+0.68, Cyclooxygenase inhibitor)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Bicalutamide"
- `tables/drugdoses.parquet` — dd in 191, 192, 193
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
