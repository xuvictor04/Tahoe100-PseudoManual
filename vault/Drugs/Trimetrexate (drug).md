---
drug: "Trimetrexate"
type: "drug"
salt_base: "Trimetrexate"
targets: "DHFR"
moa_fine: "DNA synthesis/repair inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 27
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Trimetrexate

*DNA synthesis/repair inhibitor (inhibitor/antagonist) · targets: DHFR · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 16 / 26 / 27; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.31 / 0.12.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:C4 | 9 / 7 | — | -0.21 | +0.4/+0.2/-0.2 | — |
| 0.5 µM | [[Plate 05]]:C4 | 14 / 12 | — | +0.13 | +0.5/-1.0/-0.3 | — |
| 5 µM | [[Plate 14]]:C4 | 4 / 23 | 0.707 | -0.09 | +1.0/-0.9/-1.1 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (9 genes, none with an alert): [[TTC32]] 1.27× (z +3.3, 5/46 lines), [[ADGRF5]] 1.64× (z +3.2, 1/5 lines), [[MYH7B]] 1.37× (z +3.1, 1/35 lines), [[PRLR]] 1.39× (z +3.1, 1/15 lines), [[SAMD14]] 1.38× (z +3.0, 2/33 lines), [[ADORA1]] 1.39× (z +2.9, 0/34 lines), [[DHX58]] 1.26× (z +2.9, 4/40 lines), [[DEPDC7]] 1.23× (z +2.8, 2/32 lines), [[KCNG3]] 1.24× (z +2.7, 0/25 lines)

**0.5 µM** (14 genes, none with an alert; 12 shown): [[CHPF2]] 1.46× (z +4.2, 16/46 lines), [[EDC4]] 1.34× (z +4.1, 16/48 lines), [[CDK5RAP3]] 1.32× (z +3.6, 18/48 lines), [[PLA2G4B]] 1.51× (z +3.6, 7/39 lines), [[TRIM8]] 1.24× (z +3.4, 11/46 lines), [[TRIM65]] 1.27× (z +3.4, 11/47 lines), [[ZNF672]] 1.26× (z +3.3, 2/45 lines), [[CLPTM1L]] 1.28× (z +3.3, 19/48 lines), [[NAGK]] 1.22× (z +3.2, 8/48 lines), [[ENSG00000260257]] 1.37× (z +3.1, 4/41 lines), [[GORASP1]] 1.23× (z +3.1, 7/47 lines), [[RHPN1]] 1.42× (z +3.1, 7/37 lines)

**5 µM** (4 genes, none with an alert): [[MCEE]] 1.20× (z +3.5, 16/48 lines), [[FAM95A]] 1.42× (z +3.4, 0/9 lines), [[ENSG00000270240]] 1.27× (z +3.2, 2/41 lines), [[ENSG00000227722]] 1.22× (z +3.2, 5/44 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (7 genes, none with an alert): [[H2BC12]] 0.516× (z -4.0, 16/42 lines), [[ALG12]] 0.807× (z -3.9, 10/44 lines), [[ENSG00000289293]] 0.653× (z -3.9, 18/45 lines), [[SDHA]] 0.818× (z -3.8, 24/48 lines), [[ANAPC13]] 0.795× (z -3.4, 4/47 lines), [[H2BC8]] 0.533× (z -3.3, 11/29 lines), [[MLX]] 0.828× (z -3.1, 8/48 lines)

**0.5 µM** (12 genes, none with an alert): [[HNRNPA1L3]] 0.661× (z -4.7, 17/44 lines), [[H1-3]] 0.554× (z -3.9, 22/36 lines), [[BMS1P1-1]] 0.768× (z -3.7, 7/43 lines), [[RNF216P1]] 0.745× (z -3.5, 13/45 lines), [[ADGRE3]] 0.723× (z -3.5, 5/34 lines), [[BCAP31]] 0.784× (z -3.4, 20/48 lines), [[H1-4]] 0.615× (z -3.4, 31/48 lines), [[H2BC8]] 0.519× (z -3.4, 10/30 lines), [[RAB23]] 0.819× (z -3.4, 12/45 lines), [[INCENP]] 0.822× (z -2.8, 10/48 lines), [[BUB1]] 0.800× (z -2.8, 17/47 lines), [[PIF1]] 0.807× (z -2.7, 6/45 lines)

**5 µM** (23 genes, none with an alert; 12 shown): [[H2BC21]] 0.634× (z -4.6, 28/47 lines), [[MAPKAPK3]] 0.823× (z -4.5, 12/47 lines), [[PEMT]] 0.828× (z -4.5, 15/47 lines), [[RNF26]] 0.751× (z -4.2, 18/47 lines), [[H2BC18]] 0.668× (z -4.1, 11/42 lines), [[H2BC8]] 0.593× (z -3.8, 17/32 lines), [[ACTB]] 0.771× (z -3.8, 41/49 lines), [[H2BC12]] 0.651× (z -3.7, 22/43 lines), [[TNFRSF12A]] 0.785× (z -3.6, 18/47 lines), [[PLK1]] 0.827× (z -3.5, 13/48 lines), [[RHOC]] 0.805× (z -3.5, 21/46 lines), [[CCDC86]] 0.816× (z -3.4, 12/47 lines)

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
| 0.5 µM | — | [[RKO (line)]] (1.59), [[CHP-212 (line)]] (1.48), [[KATO III (line)]] (1.44), [[LS 180 (line)]] (1.39) · weakest: [[COLO 205 (line)]] (0.295), [[NCI-H1792 (line)]] (0.481), [[A549 (line)]] (0.487) |
| 5 µM | — | [[SNU-1 (line)]] (1.77), [[HepG2_C3A (line)]] (1.70), [[SW48 (line)]] (1.36), [[LoVo (line)]] (1.34) · weakest: [[NCI-H2347 (line)]] (0.430), [[A549 (line)]] (0.561), [[NCI-H661 (line)]] (0.570) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Ciclopirox (drug)]] (+0.72, unclear); [[Sulfisoxazole (drug)]] (+0.56, unclear); [[Tolcapone (drug)]] (+0.53, unclear, ⚠ only 6 significant genes); [[Entecavir (monohydrate) (drug)]] (+0.52, unclear); [[Rifaximin (drug)]] (+0.50, unclear); [[Rucaparib (phosphate) (drug)]] (+0.44, DNA synthesis/repair inhibitor, ⚠ only 5 significant genes); [[18β-Glycyrrhetinic acid (drug)]] (+0.44, unclear); [[Captopril (drug)]] (+0.44, unclear); [[Vilanterol (drug)]] (+0.41, Adrenoceptor agonist); [[Fedratinib (hydrochloride hydrate) (drug)]] (+0.39, JAK/STAT inhibitor)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Trimetrexate"
- `tables/drugdoses.parquet` — dd in 1051, 1052, 1053
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
