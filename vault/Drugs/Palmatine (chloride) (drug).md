---
drug: "Palmatine (chloride)"
type: "drug"
salt_base: "Palmatine"
targets: "IDO1, WNV NS2B-NS3"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "0.05"
max_sig_genes: 203
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Palmatine (chloride)

*unclear (inhibitor/antagonist) · targets: IDO1, WNV NS2B-NS3 · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 203 / 90 / 16; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.24 / 0.40.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:A10 | 46 / 157 | — | +0.52 | +3.5/+1.8/+1.1 | — |
| 0.5 µM | [[Plate 05]]:A10 | 79 / 11 | — | -0.82 | +0.1/+0.3/+0.7 | — |
| 5 µM | [[Plate 14]]:A10 | 13 / 3 | 0.810 | -0.04 | -0.3/+0.6/+0.7 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (46 genes, none with an alert; 12 shown): [[EVA1A-AS]] 1.84× (z +4.1, 12/25 lines), [[ALPK2]] 1.42× (z +4.0, 6/17 lines), [[CYTOR]] 1.35× (z +4.0, 30/47 lines), [[FAM111B]] 1.55× (z +3.8, 15/38 lines), [[F2R]] 1.41× (z +3.8, 11/36 lines), [[ENSG00000285016]] 1.39× (z +3.7, 26/48 lines), [[VMA21]] 1.24× (z +3.6, 15/48 lines), [[ESCO2]] 1.41× (z +3.5, 8/47 lines), [[FAM111A]] 1.30× (z +3.5, 15/45 lines), [[CD96]] 1.38× (z +3.5, 6/35 lines), [[NIP7]] 1.31× (z +3.4, 6/48 lines), [[CENPH]] 1.28× (z +3.4, 14/48 lines)

**0.5 µM** (79 genes, none with an alert; 12 shown): [[ENSG00000263847]] 1.62× (z +4.1, 8/27 lines), [[ENSG00000270055]] 1.53× (z +4.0, 3/19 lines), [[WNK3]] 1.28× (z +3.9, 1/16 lines), [[WTIP]] 1.27× (z +3.9, 10/40 lines), [[FBLN2]] 1.54× (z +3.8, 2/12 lines), [[SV2A]] 1.40× (z +3.7, 4/26 lines), [[DTYMK]] 1.43× (z +3.7, 20/47 lines), [[ENSG00000291078]] 1.45× (z +3.6, 6/33 lines), [[XYLT2]] 1.21× (z +3.6, 10/48 lines), [[ENSG00000144785]] 1.25× (z +3.6, 13/47 lines), [[ENSG00000254929]] 1.25× (z +3.5, 6/44 lines), [[NT5DC2]] 1.35× (z +3.5, 10/42 lines)

**5 µM** (13 genes, none with an alert; 12 shown): [[MT-CO2]] 1.47× (z +5.9, 31/48 lines), [[MTCO1P12]] 1.47× (z +5.0, 17/47 lines), [[MT-ATP6]] 1.46× (z +4.4, 34/48 lines), [[MT-ND6]] 1.34× (z +4.2, 26/48 lines), [[MT-TL1]] 1.59× (z +4.2, 24/45 lines), [[MT-CO1]] 1.27× (z +4.0, 29/48 lines), [[MT-ND3]] 1.54× (z +3.9, 31/48 lines), [[MT-ND2]] 1.38× (z +3.7, 30/48 lines), [[COLEC11]] 1.39× (z +3.4, 8/45 lines), [[ATP6V0A4]] 1.29× (z +3.2, 0/39 lines), [[SV2A]] 1.22× (z +3.2, 3/30 lines), [[LAMC3]] 1.23× (z +3.1, 5/22 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (157 genes, none with an alert; 12 shown): [[JMY]] 0.699× (z -5.8, 33/48 lines), [[CBLB]] 0.734× (z -5.2, 28/48 lines), [[SLC15A2]] 0.586× (z -5.1, 21/46 lines), [[DNAJC25]] 0.642× (z -5.0, 39/49 lines), [[CNNM2]] 0.725× (z -5.0, 35/49 lines), [[GOLPH3L]] 0.761× (z -4.8, 28/48 lines), [[FBXO42]] 0.740× (z -4.6, 33/49 lines), [[SRP54-AS1]] 0.675× (z -4.5, 36/48 lines), [[FYN]] 0.823× (z -4.3, 12/41 lines), [[MINDY2]] 0.795× (z -4.2, 28/49 lines), [[KLHL24]] 0.769× (z -4.2, 30/49 lines), [[HLA-V-1]] 0.694× (z -4.2, 6/26 lines)

**0.5 µM** (11 genes, none with an alert): [[APMAP]] 0.786× (z -5.1, 23/48 lines), [[ZNF615]] 0.750× (z -4.7, 15/38 lines), [[TAP1]] 0.738× (z -4.5, 28/48 lines), [[THAP9]] 0.758× (z -4.1, 15/44 lines), [[TRIB1]] 0.761× (z -3.9, 19/42 lines), [[EMD]] 0.732× (z -3.8, 22/47 lines), [[TAF9]] 0.789× (z -3.5, 16/47 lines), [[ZNF304]] 0.742× (z -3.5, 9/33 lines), [[PEX11B]] 0.818× (z -3.3, 12/45 lines), [[MORF4L1P1]] 0.723× (z -3.3, 16/42 lines), [[ARPC5]] 0.815× (z -3.1, 21/48 lines)

**5 µM** (3 genes, none with an alert): [[CCNYL2]] 0.830× (z -3.3, 1/16 lines), [[ADCK5]] 0.800× (z -3.3, 5/44 lines), [[ENSG00000291068]] 0.813× (z -3.2, 9/47 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 004]] (+2.5), [[Module 016]] (+2.0) | [[Module 207]] (-3.4), [[Module 041]] (-2.8), [[Module 179]] (-2.7) |
| 0.5 µM | — | — |
| 5 µM | — | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[LS 180 (line)]] (1.51), [[SW 1088 (line)]] (1.40), [[HOP62 (line)]] (1.33), [[NCI-H1573 (line)]] (1.32) · weakest: [[NCI-H2347 (line)]] (0.485), [[BT-474 (line)]] (0.488), [[NCI-H2122 (line)]] (0.493) |
| 0.5 µM | — | [[Hs 766T (line)]] (1.69), [[HCT15 (line)]] (1.50), [[COLO 205 (line)]] (1.42), [[hTERT-HPNE (line)]] (1.42) · weakest: [[NCI-H2347 (line)]] (0.392), [[HEC-1-A (line)]] (0.409), [[CFPAC-1 (line)]] (0.417) |
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[Megestrol (drug)]] (+0.95, unclear, ⚠ vector dose flagged: cell-cycle shift); [[Retinoic acid (drug)]] (+0.94, Retinoic receptor agonist); [[Busulfan (drug)]] (+0.94, DNA synthesis/repair inhibitor); [[Larotrectinib (drug)]] (+0.93, Other TK inhibitor); [[(R)-Verapamil (hydrochloride) (drug)]] (+0.91, unclear); [[Berbamine (drug)]] (+0.90, unclear); [[Diammonium Glycyrrhizinate (drug)]] (+0.82, unclear); [[Gallic acid (hydrate) (drug)]] (+0.81, Cyclooxygenase inhibitor); [[Esmolol (hydrochloride) (drug)]] (+0.80, unclear)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Palmatine (chloride)"
- `tables/drugdoses.parquet` — dd in 771, 772, 773
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
