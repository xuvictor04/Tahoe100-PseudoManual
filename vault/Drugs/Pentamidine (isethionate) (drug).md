---
drug: "Pentamidine (isethionate)"
type: "drug"
salt_base: "Pentamidine"
targets: "PRLR"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 56
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Pentamidine (isethionate)

*unclear (inhibitor/antagonist) · targets: PRLR · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 2 / 4 / 56; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.25 / 0.29.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:E1 | 2 / 0 | — | -0.25 | -0.5/-0.8/-0.5 | — |
| 0.5 µM | [[Plate 05]]:E1 | 1 / 3 | — | +0.56 | +0.7/+0.0/-0.1 | — |
| 5 µM | [[Plate 14]]:E1 | 21 / 35 | 0.837 | -0.09 | -1.1/-0.7/-0.3 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (2 genes, none with an alert): [[ENSG00000273784]] 1.34× (z +3.2, 1/43 lines), [[ZNF732]] 1.73× (z +2.9, 0/6 lines)

**0.5 µM** (1 gene, none with an alert): [[ENSG00000230021]] 1.30× (z +3.4, 16/48 lines)

**5 µM** (21 genes, none with an alert; 12 shown): [[ENSG00000272800]] 1.28× (z +6.5, 26/48 lines), [[ENSG00000287621]] 1.36× (z +6.0, 27/45 lines), [[ZNF362]] 1.37× (z +4.8, 22/46 lines), [[DCAF15]] 1.22× (z +4.3, 13/48 lines), [[ZNF618]] 1.26× (z +4.3, 14/39 lines), [[PAXIP1-AS2]] 1.25× (z +4.2, 9/46 lines), [[CDC25B]] 1.22× (z +4.0, 16/48 lines), [[MOCOS]] 1.20× (z +3.9, 10/41 lines), [[KCTD15]] 1.22× (z +3.9, 10/39 lines), [[BCL6]] 1.20× (z +3.7, 21/48 lines), [[PTGS2]] 1.24× (z +3.7, 10/21 lines), [[PSAT1]] 1.22× (z +3.6, 16/40 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (3 genes, none with an alert): [[NSUN5P1]] 0.667× (z -4.0, 12/42 lines), [[MTND5P11]] 0.613× (z -3.5, 10/41 lines), [[MT-CO2]] 0.748× (z -3.3, 22/49 lines)

**5 µM** (35 genes, none with an alert; 12 shown): [[MT-CO2]] 0.368× (z -15.6, 46/48 lines), [[MT-CYB]] 0.346× (z -14.8, 44/48 lines), [[MT-CO3]] 0.366× (z -14.7, 45/48 lines), [[MT-ND4]] 0.383× (z -13.5, 45/48 lines), [[MT-ND5]] 0.364× (z -13.4, 47/48 lines), [[MT-CO1]] 0.499× (z -11.6, 45/48 lines), [[MT-ND2]] 0.406× (z -10.4, 44/48 lines), [[MT-ND1]] 0.451× (z -9.0, 45/48 lines), [[MT-ATP6]] 0.466× (z -9.0, 42/48 lines), [[MT-ND3]] 0.374× (z -8.7, 43/48 lines), [[MTCO1P12]] 0.522× (z -8.3, 30/47 lines), [[MT-ND6]] 0.564× (z -8.3, 43/48 lines)

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
| 5 µM | — | [[A549 (line)]] (1.86), [[NCI-H2030 (line)]] (1.81), [[PANC-1 (line)]] (1.79), [[Hs 766T (line)]] (1.78) · weakest: [[RKO (line)]] (0.0268), [[HT-29 (line)]] (0.190), [[LoVo (line)]] (0.194) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Chlorhexidine (diacetate) (drug)]] (+0.47, unclear); [[crizotinib (drug)]] (+0.40, Multi-TK inhibitor); [[Thymol (drug)]] (+0.39, unclear); [[Ritonavir (drug)]] (+0.37, unclear); [[Cepharanthine (drug)]] (+0.33, unclear); [[Dexmedetomidine (drug)]] (+0.33, Adrenoceptor agonist, ⚠ only 9 significant genes); [[Neratinib (maleate) (drug)]] (+0.33, EGFR/ERBB inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Ivermectin (drug)]] (+0.31, unclear); [[5-Azacytidine (drug)]] (+0.31, DNA methyltransferase inhibitor); [[ULK-101 (drug)]] (+0.31, unclear)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Pentamidine (isethionate)"
- `tables/drugdoses.parquet` — dd in 791, 792, 793
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
