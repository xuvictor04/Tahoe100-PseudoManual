---
drug: "Decitabine"
type: "drug"
salt_base: "Decitabine"
targets: "DNMT1, DNMT3A, DNMT3B"
moa_fine: "DNA methyltransferase inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 138
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Decitabine

*DNA methyltransferase inhibitor (inhibitor/antagonist) · targets: DNMT1, DNMT3A, DNMT3B · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 23 / 138 / 28; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.42 / -0.34.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:E6 | 9 / 14 | — | -0.27 | -0.3/-0.1/+1.0 | — |
| 0.5 µM | [[Plate 08]]:E6 | 132 / 6 | — | -0.66 | +0.3/+0.4/+1.0 | — |
| 5 µM | [[Plate 09]]:E6 | 14 / 14 | — | +0.18 | +0.4/+0.4/-0.7 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (9 genes, none with an alert): [[CYP2U1-AS1]] 1.47× (z +4.2, 10/40 lines), [[ATP8A2]] 1.36× (z +3.6, 2/35 lines), [[CNBD2]] 1.35× (z +3.2, 3/35 lines), [[AMZ2P1-1]] 1.40× (z +3.1, 5/34 lines), [[ACYP1]] 1.25× (z +3.1, 9/43 lines), [[ISG20]] 1.27× (z +3.0, 8/43 lines), [[ENSG00000286652]] 1.43× (z +2.9, 4/22 lines), [[RBFOX1]] 1.24× (z +2.9, 6/37 lines), [[MCOLN3]] 1.26× (z +2.8, 1/26 lines)

**0.5 µM** (132 genes, none with an alert; 12 shown): [[ARHGAP20]] 1.68× (z +4.4, 0/11 lines), [[ENSG00000285822]] 1.51× (z +4.3, 0/9 lines), [[ENSG00000285471]] 1.53× (z +4.2, 3/15 lines), [[RETREG1-AS1]] 1.54× (z +4.1, 2/35 lines), [[PRSS51]] 1.69× (z +4.0, 0/10 lines), [[ENSG00000256615]] 1.62× (z +4.0, 1/9 lines), [[ENSG00000253642]] 1.54× (z +3.9, 0/7 lines), [[ANKRD20A4P]] 1.49× (z +3.9, 1/19 lines), [[COL23A1]] 1.36× (z +3.9, 4/40 lines), [[CSTF3-DT]] 1.45× (z +3.9, 4/35 lines), [[EPHA6]] 1.29× (z +3.8, 0/19 lines), [[LINC00923]] 1.41× (z +3.8, 1/15 lines)

**5 µM** (14 genes, none with an alert; 12 shown): [[CCNT2-AS1]] 1.41× (z +4.7, 11/44 lines), [[SLC39A10]] 1.23× (z +3.8, 18/47 lines), [[ZNF616]] 1.24× (z +3.4, 9/46 lines), [[VIM-AS1]] 1.26× (z +3.3, 2/38 lines), [[ZNF184]] 1.25× (z +3.1, 6/47 lines), [[NAMPTP1]] 1.40× (z +3.1, 5/42 lines), [[ENSG00000228793]] 1.35× (z +3.1, 2/39 lines), [[STON2]] 1.24× (z +3.1, 4/28 lines), [[WNK2]] 1.22× (z +3.0, 3/31 lines), [[GRIP1]] 1.21× (z +2.9, 9/34 lines), [[TRPV3]] 1.41× (z +2.9, 1/29 lines), [[POT1-AS1]] 1.32× (z +2.8, 4/43 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (14 genes, none with an alert; 12 shown): [[MORF4L1P1]] 0.623× (z -4.5, 17/41 lines), [[DPY19L2P3]] 0.724× (z -4.1, 11/40 lines), [[MALAT1]] 0.782× (z -4.1, 42/47 lines), [[DUXAP9]] 0.733× (z -3.7, 18/38 lines), [[ENSG00000278384]] 0.719× (z -3.6, 11/26 lines), [[EBLN2]] 0.721× (z -3.5, 7/39 lines), [[LSP1P4]] 0.747× (z -3.5, 11/35 lines), [[ENSG00000267127]] 0.731× (z -3.4, 13/42 lines), [[SPHK2]] 0.823× (z -3.4, 8/43 lines), [[ENSG00000203546]] 0.742× (z -3.2, 11/36 lines), [[CLCN2]] 0.801× (z -3.2, 10/43 lines), [[SLITRK6]] 0.705× (z -2.9, 4/16 lines)

**0.5 µM** (6 genes, none with an alert): [[MOB2]] 0.800× (z -4.1, 13/47 lines), [[LINC00674]] 0.706× (z -3.8, 8/43 lines), [[TMEM178B]] 0.829× (z -3.6, 10/26 lines), [[CDKN2AIP]] 0.812× (z -3.5, 6/46 lines), [[PIGO]] 0.807× (z -3.1, 7/42 lines), [[PAN2]] 0.799× (z -3.0, 10/47 lines)

**5 µM** (14 genes, none with an alert; 12 shown): [[MAGOH]] 0.759× (z -4.8, 26/47 lines), [[ENSG00000261267]] 0.635× (z -4.4, 5/39 lines), [[MT-ND4L]] 0.533× (z -4.2, 44/47 lines), [[LRRC34]] 0.675× (z -4.0, 5/20 lines), [[PART1]] 0.563× (z -3.6, 3/18 lines), [[LINC00674]] 0.715× (z -3.5, 4/44 lines), [[ENSG00000249803]] 0.631× (z -3.5, 3/11 lines), [[LINC00648]] 0.637× (z -3.4, 5/11 lines), [[ABHD12B]] 0.721× (z -3.4, 10/39 lines), [[XBP1]] 0.814× (z -3.3, 14/47 lines), [[ENSG00000230532]] 0.787× (z -3.1, 10/45 lines), [[RNF187]] 0.796× (z -3.0, 9/47 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | [[Module 054]] (+2.1) | — |
| 5 µM | — | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[SNU-1 (line)]] (1.68), [[SW 900 (line)]] (1.57), [[NCI-H2347 (line)]] (1.46), [[NCI-H661 (line)]] (1.43) · weakest: [[COLO 205 (line)]] (-0.215), [[NCI-H2030 (line)]] (0.321), [[PANC-1 (line)]] (0.323) |
| 0.5 µM | — | [[SW 1088 (line)]] (2.46), [[AN3 CA (line)]] (2.15), [[SW 1271 (line)]] (1.83), [[CHP-212 (line)]] (1.72) · weakest: [[CFPAC-1 (line)]] (0.320), [[NCI-H2347 (line)]] (0.365), [[Hs 766T (line)]] (0.384) |
| 5 µM | — | [[HOP62 (line)]] (1.59), [[C32 (line)]] (1.52), [[PANC-1 (line)]] (1.41), [[A549 (line)]] (1.40) · weakest: [[C-33 A (line)]] (0.419), [[COLO 205 (line)]] (0.435), [[HT-29 (line)]] (0.523) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Bendamustine (drug)]] (+0.84, DNA synthesis/repair inhibitor); [[Sivelestat (sodium tetrahydrate) (drug)]] (+0.83, unclear); [[Darolutamide (drug)]] (+0.81, Androgen receptor antagonist, ⚠ only 5 significant genes); [[Docetaxel (Trihydrate) (drug)]] (+0.80, Microtubule inhibitor); [[Tranilast (drug)]] (+0.78, unclear, ⚠ only 6 significant genes); [[Bicalutamide (drug)]] (+0.78, Androgen receptor antagonist); [[Methylprednisolone succinate (drug)]] (+0.76, Glucocorticoid receptor agonist); [[Bimatoprost (drug)]] (+0.75, unclear); [[Azithromycin (hydrate) (drug)]] (+0.73, unclear); [[Celecoxib (drug)]] (+0.69, Cyclooxygenase inhibitor)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Decitabine"
- `tables/drugdoses.parquet` — dd in 335, 336, 337
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
