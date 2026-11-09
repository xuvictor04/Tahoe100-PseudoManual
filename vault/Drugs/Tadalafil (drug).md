---
drug: "Tadalafil"
type: "drug"
salt_base: "Tadalafil"
targets: "PDE5A"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 49
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Tadalafil

*unclear (inhibitor/antagonist) · targets: PDE5A · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 2 / 2 / 49; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.06 / 0.10.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:B6 | 2 / 0 | — | -0.20 | -0.6/-0.7/-0.0 | — |
| 0.5 µM | [[Plate 08]]:B6 | 0 / 2 | — | +0.59 | +0.1/+0.2/+0.9 | — |
| 5 µM | [[Plate 09]]:B6 | 9 / 40 | — | -0.46 | -1.5/-1.0/-0.7 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (2 genes, none with an alert): [[ENSG00000273345]] 1.41× (z +3.5, 1/43 lines), [[ENSG00000256083]] 1.47× (z +3.0, 2/34 lines)

**5 µM** (9 genes, none with an alert): [[AP4B1]] 1.36× (z +4.1, 9/46 lines), [[C2orf27A]] 1.24× (z +3.6, 6/43 lines), [[NPTN]] 1.22× (z +3.5, 25/48 lines), [[ENSG00000274561]] 1.38× (z +3.4, 4/37 lines), [[MINDY3]] 1.23× (z +3.4, 15/48 lines), [[AFDN]] 1.20× (z +3.3, 23/47 lines), [[UBP1]] 1.21× (z +3.2, 14/48 lines), [[ZNF483]] 1.26× (z +3.0, 8/41 lines), [[AGFG2]] 1.21× (z +2.8, 4/45 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (2 genes, none with an alert): [[INPP5E]] 0.773× (z -3.5, 6/47 lines), [[LINC00482]] 0.699× (z -2.9, 4/34 lines)

**5 µM** (40 genes, none with an alert; 12 shown): [[KLHL36]] 0.791× (z -4.8, 19/47 lines), [[ASGR1]] 0.599× (z -3.8, 10/31 lines), [[WAKMAR2]] 0.691× (z -3.8, 6/37 lines), [[PTPRN]] 0.616× (z -3.8, 1/13 lines), [[MANEAL]] 0.629× (z -3.8, 10/35 lines), [[TP53I13]] 0.667× (z -3.7, 15/41 lines), [[UTY]] 0.797× (z -3.7, 0/17 lines), [[SEPHS2]] 0.688× (z -3.6, 22/47 lines), [[SGPP2]] 0.794× (z -3.6, 0/16 lines), [[MID1IP1]] 0.749× (z -3.5, 16/45 lines), [[TMEM42]] 0.671× (z -3.5, 9/33 lines), [[AKR7A2]] 0.721× (z -3.4, 18/46 lines)

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
| 5 µM | — | [[HEC-1-A (line)]] (1.53), [[NCI-H661 (line)]] (1.52), [[SW48 (line)]] (1.43), [[SK-MEL-2 (line)]] (1.40) · weakest: [[NCI-H1573 (line)]] (0.473), [[CFPAC-1 (line)]] (0.570), [[HepG2_C3A (line)]] (0.574) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 3 next most similar without an alert.*

- [[Glycyrrhizic acid (drug)]] (+0.68, unclear); [[Thymopentin (drug)]] (+0.64, unclear, ⚠ only 2 significant genes); [[Fluvoxamine (drug)]] (+0.64, unclear); [[Asciminib (drug)]] (+0.62, Other TK inhibitor); [[8-Hydroxyquinoline (drug)]] (+0.60, unclear); [[Capivasertib (drug)]] (+0.59, PI3K/AKT inhibitor, ⚠ only 5 significant genes); [[Indacaterol (maleate) (drug)]] (+0.54, Adrenoceptor agonist, ⚠ only 3 significant genes); [[Folic acid (drug)]] (+0.54, unclear); [[Dihydroartemisinin (drug)]] (+0.51, unclear); [[Roxadustat (drug)]] (+0.48, unclear); [[Ivermectin (drug)]] (+0.47, unclear)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Tadalafil"
- `tables/drugdoses.parquet` — dd in 979, 980, 981
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
