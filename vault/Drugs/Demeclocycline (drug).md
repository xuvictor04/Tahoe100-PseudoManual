---
drug: "Demeclocycline"
type: "drug"
salt_base: "Demeclocycline"
targets: ""
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 136
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Demeclocycline

*unclear (inhibitor/antagonist) · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 3 / 2 / 136; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.17 / 0.46.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:E7 | 3 / 0 | — | -0.08 | -0.1/-0.5/-0.5 | — |
| 0.5 µM | [[Plate 05]]:E7 | 1 / 1 | — | +0.39 | -0.4/-0.4/-1.8 | — |
| 5 µM | [[Plate 14]]:E7 | 124 / 12 | 0.865 | -0.34 | +1.1/+0.6/-1.2 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (3 genes, none with an alert): [[LINC00654]] 1.48× (z +3.1, 3/41 lines), [[CDKL2]] 1.39× (z +3.0, 2/39 lines), [[ENSG00000288587]] 1.31× (z +2.9, 2/42 lines)

**0.5 µM** (1 gene, none with an alert): [[SLCO5A1]] 1.23× (z +3.0, 5/41 lines)

**5 µM** (124 genes, none with an alert; 12 shown): [[GARIN1A]] 1.55× (z +4.5, 29/47 lines), [[ENSG00000226149]] 1.40× (z +4.4, 16/36 lines), [[NEMP2]] 1.25× (z +4.4, 17/40 lines), [[SORBS2]] 1.23× (z +4.4, 16/31 lines), [[ENSG00000263257]] 1.46× (z +4.4, 10/43 lines), [[SIAH2-AS1]] 1.42× (z +4.4, 6/42 lines), [[PRKG1-AS1]] 1.36× (z +4.2, 4/30 lines), [[LINC01829]] 1.29× (z +4.2, 13/44 lines), [[ELFN2]] 1.31× (z +4.1, 11/28 lines), [[IMPG2]] 1.42× (z +4.1, 13/43 lines), [[ENSG00000273118]] 1.40× (z +4.1, 16/36 lines), [[CAPN3]] 1.49× (z +4.0, 11/43 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (1 gene, none with an alert): [[LRRC34]] 0.668× (z -4.2, 3/23 lines)

**5 µM** (12 genes, none with an alert): [[CCDC126]] 0.824× (z -5.2, 23/48 lines), [[GADD45A]] 0.697× (z -4.1, 35/47 lines), [[ENSG00000262831]] 0.718× (z -4.0, 9/43 lines), [[SMNDC1]] 0.825× (z -3.9, 24/48 lines), [[RCHY1]] 0.824× (z -3.9, 22/48 lines), [[TFPI2]] 0.727× (z -3.7, 15/26 lines), [[ALKBH5]] 0.831× (z -3.7, 20/48 lines), [[ARL4D]] 0.805× (z -3.6, 8/42 lines), [[APBA3]] 0.833× (z -3.4, 9/47 lines), [[EAF2]] 0.800× (z -3.4, 10/47 lines), [[TRIM36]] 0.828× (z -3.2, 17/46 lines), [[SPATA2L]] 0.828× (z -3.2, 5/47 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[Module 006]] (+2.7), [[Module 194]] (+2.6), [[Module 088]] (+2.3) | [[Module 030]] (-2.7), [[Module 043]] (-2.7), [[Module 045]] (-2.5) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[SW1417 (line)]] (-3.6) | [[BT-474 (line)]] (1.18), [[A-172 (line)]] (1.18), [[H4 (line)]] (1.16), [[SW 900 (line)]] (1.15) · weakest: [[AN3 CA (line)]] (0.409), [[CHP-212 (line)]] (0.444), [[HCT15 (line)]] (0.483) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[Esmolol (hydrochloride) (drug)]] (+0.82, unclear); [[(R)-Verapamil (hydrochloride) (drug)]] (+0.78, unclear); [[Omeprazole (drug)]] (+0.77, unclear); [[Finasteride (drug)]] (+0.77, unclear); [[Busulfan (drug)]] (+0.75, DNA synthesis/repair inhibitor); [[Megestrol (drug)]] (+0.74, unclear, ⚠ vector dose flagged: cell-cycle shift); [[Brimonidine (drug)]] (+0.73, Adrenoceptor agonist); [[Palmatine (chloride) (drug)]] (+0.73, unclear); [[Diphenhydramine (drug)]] (+0.72, unclear)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Demeclocycline"
- `tables/drugdoses.parquet` — dd in 341, 342, 343
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
