---
drug: "Azithromycin (hydrate)"
type: "drug"
salt_base: "Azithromycin"
targets: ""
moa_fine: "unclear"
moa_broad: "unclear"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 32
tags: ["drug", "moa/unclear"]
generated_by: "tahoemap"
---

# Azithromycin (hydrate)

*unclear (unclear) · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 0 / 8 / 32; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.35 / 0.37.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:D11 | 0 / 0 | — | -0.14 | +0.2/+0.3/+0.2 | — |
| 0.5 µM | [[Plate 05]]:D11 | 1 / 7 | — | -0.39 | -0.2/+0.3/-0.0 | — |
| 5 µM | [[Plate 14]]:D11 | 19 / 13 | 0.891 | -0.25 | +1.0/+1.8/+1.1 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (1 gene, none with an alert): [[MAK]] 1.27× (z +3.0, 7/46 lines)

**5 µM** (19 genes, none with an alert; 12 shown): [[HOXA10]] 1.32× (z +3.9, 13/26 lines), [[DEXI]] 1.24× (z +3.5, 16/48 lines), [[RAB24]] 1.28× (z +3.5, 13/48 lines), [[COA3]] 1.45× (z +3.4, 14/46 lines), [[KNOP1]] 1.25× (z +3.2, 21/48 lines), [[PITPNA-AS1]] 1.38× (z +3.2, 11/43 lines), [[TMEM160]] 1.49× (z +3.2, 19/46 lines), [[BSPRY]] 1.24× (z +3.2, 3/19 lines), [[MAP3K9-DT]] 1.31× (z +3.1, 3/30 lines), [[PABPN1]] 1.29× (z +3.1, 41/49 lines), [[UBL5]] 1.40× (z +3.1, 35/48 lines), [[FBXO27]] 1.27× (z +3.1, 5/20 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (7 genes, none with an alert): [[STK19]] 0.734× (z -4.8, 18/47 lines), [[CFAP46]] 0.633× (z -3.6, 9/18 lines), [[LINC00857]] 0.707× (z -3.5, 7/27 lines), [[ENSG00000173867]] 0.794× (z -3.2, 8/44 lines), [[SYT9-AS1]] 0.717× (z -3.0, 2/33 lines), [[C14orf93]] 0.784× (z -3.0, 10/45 lines), [[ZNF287]] 0.728× (z -2.9, 5/31 lines)

**5 µM** (13 genes, none with an alert; 12 shown): [[CA5BP1-1]] 0.706× (z -4.5, 13/44 lines), [[ENSG00000269069]] 0.679× (z -4.0, 12/37 lines), [[ENSG00000281383]] 0.528× (z -3.9, 34/46 lines), [[ZNF484]] 0.793× (z -3.9, 26/48 lines), [[USP19]] 0.810× (z -3.8, 19/47 lines), [[NRBP2]] 0.795× (z -3.7, 17/45 lines), [[ZNF607]] 0.753× (z -3.6, 12/39 lines), [[ZNF596]] 0.818× (z -3.6, 8/44 lines), [[ZKSCAN8]] 0.803× (z -3.5, 22/46 lines), [[ZNF17]] 0.785× (z -3.5, 15/46 lines), [[EEF1A1]] 0.807× (z -3.4, 35/49 lines), [[ZNF845]] 0.832× (z -3.2, 12/43 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[Module 048]] (+2.9), [[Module 054]] (+2.4), [[Module 024]] (+2.2) | [[Module 020]] (-2.3) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | [[H4 (line)]] (1.52), [[COLO 205 (line)]] (1.37), [[HCT15 (line)]] (1.29), [[NCI-H23 (line)]] (1.24) · weakest: [[NCI-H2122 (line)]] (0.218), [[NCI-H460 (line)]] (0.577), [[A549 (line)]] (0.647) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Sivelestat (sodium tetrahydrate) (drug)]] (+0.77, unclear); [[Tranilast (drug)]] (+0.74, unclear, ⚠ only 6 significant genes); [[Decitabine (drug)]] (+0.73, DNA methyltransferase inhibitor); [[Bendamustine (drug)]] (+0.70, DNA synthesis/repair inhibitor); [[Darolutamide (drug)]] (+0.70, Androgen receptor antagonist, ⚠ only 5 significant genes); [[Methylprednisolone succinate (drug)]] (+0.66, Glucocorticoid receptor agonist); [[Celecoxib (drug)]] (+0.66, Cyclooxygenase inhibitor); [[18β-Glycyrrhetinic acid (drug)]] (+0.64, unclear); [[Sodium Salicylate (drug)]] (+0.63, Cyclooxygenase inhibitor); [[Vilanterol (drug)]] (+0.61, Adrenoceptor agonist)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Azithromycin (hydrate)"
- `tables/drugdoses.parquet` — dd in 126, 127, 128
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
