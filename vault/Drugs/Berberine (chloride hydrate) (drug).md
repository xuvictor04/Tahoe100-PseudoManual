---
drug: "Berberine (chloride hydrate)"
type: "drug"
salt_base: "Berberine"
targets: ""
moa_fine: "unclear"
moa_broad: "unclear"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 24
tags: ["drug", "moa/unclear"]
generated_by: "tahoemap"
---

# Berberine (chloride hydrate)

*unclear (unclear) · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 1 / 8 / 24; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.41 / 0.08.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:G4 | 0 / 1 | — | -0.08 | +0.8/+0.4/+0.4 | — |
| 0.5 µM | [[Plate 05]]:G4 | 1 / 7 | — | +0.00 | +0.8/+0.4/+0.7 | — |
| 5 µM | [[Plate 14]]:G4 | 4 / 20 | 0.788 | +0.56 | +0.9/+0.7/-0.5 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (1 gene, none with an alert): [[EDC4]] 1.25× (z +3.1, 8/48 lines)

**5 µM** (4 genes, none with an alert): [[MT-CO2]] 1.57× (z +7.1, 43/48 lines), [[MT-TL1]] 1.97× (z +6.2, 31/48 lines), [[MT-ATP6]] 1.31× (z +3.1, 28/48 lines), [[ENSG00000275216]] 1.23× (z +3.1, 6/28 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[RBM44]] 0.759× (z -3.0, 6/44 lines)

**0.5 µM** (7 genes, none with an alert): [[ENSG00000250264]] 0.714× (z -3.4, 3/31 lines), [[MAN1C1]] 0.749× (z -3.3, 7/32 lines), [[TUBG2]] 0.822× (z -3.1, 8/47 lines), [[SMPDL3A]] 0.741× (z -3.1, 6/37 lines), [[ENSG00000258593]] 0.698× (z -3.0, 5/29 lines), [[PRIMPOL]] 0.828× (z -2.9, 7/48 lines), [[TSBP1-AS1]] 0.804× (z -2.9, 2/36 lines)

**5 µM** (20 genes, none with an alert; 12 shown): [[ENSG00000249174]] 0.670× (z -4.4, 0/9 lines), [[MT-RNR1]] 0.618× (z -4.0, 41/48 lines), [[EID2B]] 0.732× (z -3.8, 7/34 lines), [[PLCH2]] 0.716× (z -3.6, 3/22 lines), [[ALG2]] 0.825× (z -3.6, 17/48 lines), [[ENSG00000234156]] 0.782× (z -3.6, 3/23 lines), [[ADCY4]] 0.676× (z -3.6, 5/15 lines), [[C9orf40]] 0.779× (z -3.5, 8/47 lines), [[HOXA-AS2]] 0.772× (z -3.5, 6/43 lines), [[P3H2-AS1]] 0.714× (z -3.5, 1/16 lines), [[CPT2]] 0.793× (z -3.4, 14/48 lines), [[MTND5P11]] 0.718× (z -3.3, 10/45 lines)

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
| 0.5 µM | — | — |
| 5 µM | — | [[Panc 03.27 (line)]] (1.56), [[MIA PaCa-2 (line)]] (1.45), [[COLO 205 (line)]] (1.45), [[SW 1088 (line)]] (1.42) · weakest: [[A498 (line)]] (0.548), [[C-33 A (line)]] (0.570), [[NCI-H2030 (line)]] (0.729) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 3 next most similar without an alert.*

- [[Balsalazide (sodium hydrate) (drug)]] (+0.70, JAK/STAT inhibitor, ⚠ only 9 significant genes); [[Pyridoxine (hydrochloride) (drug)]] (+0.67, unclear); [[Rutin (trihydrate) (drug)]] (+0.67, unclear); [[Tucatinib (drug)]] (+0.66, EGFR/ERBB inhibitor); [[MK-8353 (drug)]] (+0.64, Other MAPK inhibitor); [[Methyl aminolevulinate (hydrochloride) (drug)]] (+0.61, unclear, ⚠ only 3 significant genes); [[Fusidic acid (drug)]] (+0.60, unclear); [[Verapamil (drug)]] (+0.59, unclear, ⚠ only 5 significant genes); [[Clopidogrel (drug)]] (+0.58, unclear); [[Lucanthone (drug)]] (+0.58, unclear); [[Folic acid (drug)]] (+0.57, unclear)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Berberine (chloride hydrate)"
- `tables/drugdoses.parquet` — dd in 173, 174, 175
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
