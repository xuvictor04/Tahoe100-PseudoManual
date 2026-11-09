---
drug: "8-Hydroxyquinoline"
type: "drug"
salt_base: "8-Hydroxyquinoline"
targets: ""
moa_fine: "unclear"
moa_broad: "unclear"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 17
tags: ["drug", "moa/unclear"]
generated_by: "tahoemap"
---

# 8-Hydroxyquinoline

*unclear (unclear) · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 1 / 17 / 6; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): low dose only (noise?).
> Signature similarity between consecutive doses (low–mid / mid–high): 0.16 / 0.35.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:A1 | 0 / 1 | — | -0.11 | -0.5/+0.4/-0.2 | — |
| 0.5 µM | [[Plate 05]]:A1 | 11 / 6 | — | +0.24 | +1.4/+1.0/-0.0 | — |
| 5 µM | [[Plate 14]]:A1 | 1 / 5 | 0.635 | +0.15 | +1.4/+1.4/+0.2 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (11 genes, none with an alert): [[HNRNPA3]] 1.28× (z +4.7, 39/48 lines), [[PHF2]] 1.22× (z +4.3, 12/48 lines), [[ANP32A]] 1.25× (z +4.2, 32/48 lines), [[LMNB2]] 1.31× (z +3.8, 16/48 lines), [[IPO4]] 1.41× (z +3.8, 15/47 lines), [[CIZ1]] 1.20× (z +3.6, 15/48 lines), [[SART1]] 1.26× (z +3.6, 20/48 lines), [[PPP1R9B]] 1.31× (z +3.5, 14/47 lines), [[TAOK2]] 1.29× (z +3.2, 10/48 lines), [[PUF60]] 1.26× (z +3.0, 10/48 lines), [[PASK]] 1.28× (z +2.9, 4/44 lines)

**5 µM** (1 gene, none with an alert): [[H1-4]] 1.40× (z +3.3, 26/48 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[ZBTB45]] 0.754× (z -3.2, 4/43 lines)

**0.5 µM** (6 genes, none with an alert): [[ENSG00000270019]] 0.642× (z -3.9, 11/39 lines), [[ZNF625]] 0.776× (z -3.7, 5/29 lines), [[LINC02363]] 0.656× (z -3.7, 6/37 lines), [[ISY1-RAB43]] 0.706× (z -3.6, 8/44 lines), [[CTBS]] 0.785× (z -3.3, 13/47 lines), [[LINC02985]] 0.753× (z -2.9, 5/32 lines)

**5 µM** (5 genes, none with an alert): [[TCAF2]] 0.815× (z -3.8, 10/44 lines), [[SLC15A2]] 0.756× (z -3.4, 11/46 lines), [[SPATA24]] 0.807× (z -3.3, 5/46 lines), [[CHAC1]] 0.768× (z -3.2, 10/38 lines), [[PHC2-AS1]] 0.821× (z -3.0, 5/42 lines)

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
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Tadalafil (drug)]] (+0.60, unclear); [[Folic acid (drug)]] (+0.59, unclear); [[Indacaterol (maleate) (drug)]] (+0.57, Adrenoceptor agonist, ⚠ only 3 significant genes); [[Fluvoxamine (drug)]] (+0.57, unclear); [[Asciminib (drug)]] (+0.55, Other TK inhibitor); [[Bentamapimod (drug)]] (+0.53, Other MAPK inhibitor); [[Pentoxifylline (drug)]] (+0.52, unclear); [[Clonidine (hydrochloride) (drug)]] (+0.51, Adrenoceptor agonist, ⚠ only 4 significant genes); [[Pyridoxine (hydrochloride) (drug)]] (+0.46, unclear); [[Budesonide (drug)]] (+0.46, Glucocorticoid receptor agonist)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "8-Hydroxyquinoline"
- `tables/drugdoses.parquet` — dd in 18, 19, 20
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
