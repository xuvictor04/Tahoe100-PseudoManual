---
drug: "Dimethyl fumarate"
type: "drug"
salt_base: "Dimethyl fumarate"
targets: "NFE2L2"
moa_fine: "unclear"
moa_broad: "activator/agonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 300
tags: ["drug", "moa/activator_agonist"]
generated_by: "tahoemap"
---

# Dimethyl fumarate

*unclear (activator/agonist) · targets: NFE2L2 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 4 / 0 / 300; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.15 / -0.06.
> Flags by dose: - / - / plate-row cell shift.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:A6 | 2 / 2 | — | -0.08 | -0.6/+0.1/+0.2 | — |
| 0.5 µM | [[Plate 08]]:A6 | 0 / 0 | — | +0.71 | -0.6/-0.0/-1.2 | — |
| 5 µM | [[Plate 09]]:A6 | 138 / 162 | — | +0.94 | +0.1/+0.7/+0.9 | plate-row cell shift |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (2 genes, none with an alert): [[GXYLT2]] 1.25× (z +3.0, 1/36 lines), [[DPY19L2P2]] 1.33× (z +2.9, 4/38 lines)

**5 µM** (138 genes, none with an alert; 12 shown): [[RYBP]] 1.55× (z +6.0, 46/49 lines), [[TJP2]] 1.22× (z +5.5, 14/39 lines), [[NPEPPS]] 1.33× (z +5.4, 39/49 lines), [[SLC2A1]] 1.43× (z +5.3, 31/45 lines), [[CNOT8]] 1.36× (z +4.9, 36/49 lines), [[NAMPT]] 1.37× (z +4.8, 38/49 lines), [[PLEKHA2]] 1.31× (z +4.8, 30/44 lines), [[PFKFB4]] 1.46× (z +4.7, 41/49 lines), [[UBE2Q2]] 1.22× (z +4.7, 22/49 lines), [[CHD1L]] 1.31× (z +4.6, 28/49 lines), [[TFB1M]] 1.24× (z +4.6, 14/47 lines), [[USP3]] 1.50× (z +4.4, 37/49 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (2 genes, none with an alert): [[NOTCH2NLA]] 0.736× (z -3.8, 12/42 lines), [[KLRA1P]] 0.736× (z -3.0, 10/41 lines)

**5 µM** (162 genes, none with an alert; 12 shown): [[LINC02804]] 0.583× (z -5.0, 14/44 lines), [[ENSG00000287562]] 0.583× (z -4.7, 13/45 lines), [[PSMD6-AS2]] 0.738× (z -4.4, 18/47 lines), [[C9orf24]] 0.629× (z -4.4, 21/40 lines), [[BPTF]] 0.811× (z -4.3, 27/49 lines), [[ENSG00000265408]] 0.616× (z -4.3, 15/43 lines), [[DTNBP1]] 0.788× (z -4.3, 23/48 lines), [[CEACAM19]] 0.734× (z -4.1, 10/45 lines), [[ZCWPW2]] 0.753× (z -4.1, 11/48 lines), [[NSRP1]] 0.805× (z -4.1, 30/49 lines), [[FAM3B]] 0.632× (z -4.0, 5/34 lines), [[TNFSF13B]] 0.747× (z -4.0, 13/45 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[Module 164]] (+2.3), [[Module 065]] (+2.2), [[Module 045]] (+2.2) | [[Module 088]] (-2.4), [[Module 005]] (-2.1), [[Module 194]] (-2.1) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | [[SW48 (line)]] (1.37), [[SW 900 (line)]] (1.29), [[HS-578T (line)]] (1.29), [[A-172 (line)]] (1.28) · weakest: [[NCI-H2122 (line)]] (0.284), [[SHP-77 (line)]] (0.594), [[A-427 (line)]] (0.728) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Pravastatin (sodium) (drug)]] (+0.78, unclear); [[Fumaric acid (drug)]] (+0.77, unclear); [[Pimitespib (drug)]] (+0.71, unclear); [[L-Thyroxine (sodium salt pentahydrate) (drug)]] (+0.68, unclear); [[Allopurinol (drug)]] (+0.67, unclear); [[Indacaterol (maleate) (drug)]] (+0.67, Adrenoceptor agonist, ⚠ only 3 significant genes); [[Salicylic acid (drug)]] (+0.66, Cyclooxygenase inhibitor, ⚠ only 3 significant genes); [[Piroxicam (drug)]] (+0.66, Cyclooxygenase inhibitor); [[Mozavaptan (drug)]] (+0.62, unclear); [[Bexarotene (drug)]] (+0.62, Retinoic receptor agonist)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Dimethyl fumarate"
- `tables/drugdoses.parquet` — dd in 359, 360, 361
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
