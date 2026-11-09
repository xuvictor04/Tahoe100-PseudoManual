---
drug: "Darinaparsin"
type: "drug"
salt_base: "Darinaparsin"
targets: ""
moa_fine: "unclear"
moa_broad: "unclear"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 793
tags: ["drug", "moa/unclear"]
generated_by: "tahoemap"
---

# Darinaparsin

*unclear (unclear) · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 2 / 7 / 793; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.32 / 0.53.
> Flags by dose: - / - / cell-cycle shift. ⚠ 5 µM: cell-cycle shift (artifact flags: its changes there are shown with an alert, not left out).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:D8 | 0 / 2 | — | -0.30 | -0.0/-0.1/-0.0 | — |
| 0.5 µM | [[Plate 05]]:D8 | 7 / 0 | — | +0.17 | +0.9/+0.6/-0.1 | — |
| 5 µM | [[Plate 14]]:D8 | 646 / 147 | 0.930 | -0.33 | +5.7/+6.7/+2.5 | ⚠ cell-cycle shift |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (7 genes, none with an alert): [[EPHA1]] 1.45× (z +4.0, 0/21 lines), [[WT1]] 1.34× (z +3.1, 2/18 lines), [[ENSG00000236255]] 1.27× (z +3.1, 11/47 lines), [[PEX6]] 1.24× (z +3.0, 1/45 lines), [[GRM7]] 1.32× (z +2.9, 1/41 lines), [[LTB4R]] 1.26× (z +2.9, 3/46 lines), [[DPY19L2P2]] 1.29× (z +2.8, 1/41 lines)

**5 µM** (646 genes, 496 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 24 shown): [[KNL1]] ⚠ 1.42× (z +8.2, 40/47 lines; cell-cycle shift, explains ~72% of this change), [[KIF4A]] ⚠ 1.38× (z +7.7, 37/47 lines; cell-cycle shift, explains ~77% of this change), [[TACC3]] ⚠ 1.35× (z +7.5, 34/48 lines; cell-cycle shift, explains ~82% of this change), [[HMMR]] ⚠ 1.63× (z +7.3, 43/48 lines; cell-cycle shift, explains ~65% of this change), [[KIF18B]] ⚠ 1.51× (z +7.3, 39/46 lines; cell-cycle shift, explains ~71% of this change), [[DEPDC1]] ⚠ 1.54× (z +7.2, 40/46 lines; cell-cycle shift, explains ~68% of this change), [[CENPF]] ⚠ 1.51× (z +7.2, 42/46 lines; cell-cycle shift, explains ~76% of this change), [[AURKA]] ⚠ 1.46× (z +7.2, 37/48 lines; cell-cycle shift, explains ~65% of this change), [[ASPM]] ⚠ 1.44× (z +7.1, 38/47 lines; cell-cycle shift, explains ~58% of this change), [[KNSTRN]] ⚠ 1.36× (z +7.0, 28/48 lines; cell-cycle shift, explains ~55% of this change), [[MKI67]] ⚠ 1.57× (z +7.0, 44/48 lines; cell-cycle shift, explains ~73% of this change), [[BIRC5]] ⚠ 1.65× (z +6.9, 42/47 lines; cell-cycle shift, explains ~69% of this change), [[PTGR1]] 1.29× (z +6.5, 28/40 lines; cell-cycle shift (explains ~0% here)), [[C5]] 1.47× (z +5.3, 15/44 lines; cell-cycle shift (explains ~8% here)), [[PIR]] 1.25× (z +5.0, 17/38 lines; cell-cycle shift (explains ~0% here)), [[SPATA17]] 1.48× (z +5.0, 21/44 lines; cell-cycle shift (explains ~0% here)), [[NNMT]] 1.47× (z +4.9, 14/24 lines; cell-cycle shift (explains ~0% here)), [[RPL34-DT]] 1.40× (z +4.8, 18/44 lines; cell-cycle shift (explains ~0% here)), [[ENSG00000255094]] 1.47× (z +4.7, 14/42 lines; cell-cycle shift (explains ~14% here)), [[NMRAL2P]] 1.41× (z +4.7, 16/30 lines; cell-cycle shift (explains ~0% here)), [[CCDC40]] 1.35× (z +4.7, 18/47 lines; cell-cycle shift (explains ~0% here)), [[ENSG00000229983]] 1.49× (z +4.6, 12/40 lines; cell-cycle shift (explains ~9% here)), [[HTATIP2]] 1.30× (z +4.5, 19/41 lines; cell-cycle shift (explains ~7% here)), [[SLC27A2]] 1.32× (z +4.4, 13/27 lines; cell-cycle shift (explains ~16% here))

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (2 genes, none with an alert): [[WT1-AS]] 0.641× (z -3.6, 2/11 lines), [[PPT2]] 0.819× (z -3.0, 6/46 lines)

**5 µM** (147 genes, 108 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 22 shown): [[SLC41A2]] ⚠ 0.798× (z -6.1, 29/46 lines; cell-cycle shift, explains ~35% of this change), [[MBOAT2]] ⚠ 0.815× (z -5.8, 22/45 lines; cell-cycle shift, explains ~28% of this change), [[DENND3]] 0.735× (z -5.6, 28/41 lines; cell-cycle shift (explains ~20% here)), [[FGD6]] 0.815× (z -5.5, 21/36 lines; cell-cycle shift (explains ~0% here)), [[PTPRJ]] ⚠ 0.803× (z -5.4, 33/46 lines; cell-cycle shift, explains ~24% of this change), [[MYO5B]] ⚠ 0.829× (z -5.3, 13/22 lines; cell-cycle shift, explains ~5% of this change), [[ABCA5]] ⚠ 0.797× (z -5.3, 31/44 lines; cell-cycle shift, explains ~32% of this change), [[ZFAND3]] ⚠ 0.822× (z -5.3, 28/48 lines; cell-cycle shift, explains ~26% of this change), [[PTPRH]] ⚠ 0.781× (z -5.2, 24/42 lines; cell-cycle shift, explains ~50% of this change), [[ABI1]] ⚠ 0.828× (z -5.2, 24/48 lines; cell-cycle shift, explains ~10% of this change), [[CBLB]] ⚠ 0.804× (z -5.2, 31/47 lines; cell-cycle shift, explains ~61% of this change), [[LINC00598]] ⚠ 0.801× (z -5.1, 26/43 lines; cell-cycle shift, explains ~23% of this change), [[TICAM1]] 0.790× (z -4.9, 23/48 lines; cell-cycle shift (explains ~10% here)), [[RAB30]] 0.819× (z -4.8, 17/48 lines; cell-cycle shift (explains ~0% here)), [[RHBDF1]] 0.741× (z -4.5, 18/47 lines; cell-cycle shift (explains ~11% here)), [[CAMTA1]] 0.822× (z -4.5, 25/48 lines; cell-cycle shift (explains ~0% here)), [[SPRED2]] 0.818× (z -4.4, 28/48 lines; cell-cycle shift (explains ~0% here)), [[GP6-AS1]] 0.768× (z -4.4, 23/35 lines; cell-cycle shift (explains ~11% here)), [[IRF6]] 0.812× (z -4.3, 8/17 lines; cell-cycle shift (explains ~0% here)), [[ITPKC]] 0.820× (z -4.2, 18/46 lines; cell-cycle shift (explains ~0% here)), [[GOLGA7B]] 0.779× (z -4.1, 8/33 lines; cell-cycle shift (explains ~6% here)), [[ABTB2]] 0.821× (z -4.1, 21/41 lines; cell-cycle shift (explains ~0% here))

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[Module 022]] (+3.7), [[Module 006]] (+3.6), [[Module 060]] (+3.5) | [[Module 179]] (-3.7), [[Module 226]] (-3.0), [[Module 234]] (-2.8) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | [[CFPAC-1 (line)]] (1.17), [[NCI-H1792 (line)]] (1.13), [[HOP62 (line)]] (1.13), [[HS-578T (line)]] (1.10) · weakest: [[LOX-IMVI (line)]] (0.642), [[BT-474 (line)]] (0.679), [[NCI-H661 (line)]] (0.691) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: vector dose flagged: cell-cycle shift. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Megestrol (drug)]] (+0.58, unclear, ⚠ vector dose flagged: cell-cycle shift); [[Diammonium Glycyrrhizinate (drug)]] (+0.52, unclear); [[Brimonidine (drug)]] (+0.51, Adrenoceptor agonist); [[Gallic acid (hydrate) (drug)]] (+0.50, Cyclooxygenase inhibitor); [[Berbamine (drug)]] (+0.49, unclear); [[Glasdegib (drug)]] (+0.48, Sonic inhibitor, ⚠ only 4 significant genes; no trustworthy dose (vector dose flagged: unreliable plate only)); [[Retinoic acid (drug)]] (+0.47, Retinoic receptor agonist); [[Finasteride (drug)]] (+0.47, unclear); [[Palmatine (chloride) (drug)]] (+0.47, unclear); [[Demeclocycline (drug)]] (+0.45, unclear)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Darinaparsin"
- `tables/drugdoses.parquet` — dd in 329, 330, 331
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
