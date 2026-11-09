---
drug: "Dapagliflozin"
type: "drug"
salt_base: "Dapagliflozin"
targets: "SLC5A2"
moa_fine: "Glucose transporter inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.05"
max_sig_genes: 18
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Dapagliflozin

*Glucose transporter inhibitor (inhibitor/antagonist) · targets: SLC5A2 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 18 / 0 / 2; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): low dose only (noise?).
> Signature similarity between consecutive doses (low–mid / mid–high): 0.33 / 0.57.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:H7 | 12 / 6 | — | +0.43 | -0.8/-1.4/-1.3 | — |
| 0.5 µM | [[Plate 11]]:H7 | 0 / 0 | — | +0.89 | +0.2/-0.2/-0.2 | — |
| 5 µM | [[Plate 12]]:H7 | 2 / 0 | — | +0.49 | -0.1/-0.4/-0.0 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (12 genes, none with an alert): [[PRIM2]] 1.25× (z +3.4, 24/48 lines), [[CFAP161]] 1.51× (z +3.3, 18/42 lines), [[CORIN]] 1.35× (z +3.2, 5/42 lines), [[SCFD2]] 1.23× (z +3.1, 12/48 lines), [[MIPOL1]] 1.20× (z +3.1, 10/40 lines), [[MOB3B]] 1.26× (z +3.0, 1/38 lines), [[MCF2]] 1.38× (z +3.0, 2/43 lines), [[THADA]] 1.27× (z +3.0, 23/47 lines), [[PCNX4-DT]] 1.44× (z +3.0, 2/46 lines), [[VWA8]] 1.24× (z +2.9, 17/48 lines), [[ADAM32]] 1.24× (z +2.9, 10/46 lines), [[ACYP2]] 1.26× (z +2.8, 13/48 lines)

**5 µM** (2 genes, none with an alert): [[ENSG00000286125]] 1.57× (z +3.7, 7/47 lines), [[H4C8]] 1.33× (z +3.0, 1/47 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (6 genes, none with an alert): [[FTH1]] 0.739× (z -3.1, 32/44 lines), [[IRF2BP2]] 0.819× (z -3.0, 20/47 lines), [[PDGFB]] 0.748× (z -3.0, 10/32 lines), [[HLA-E]] 0.818× (z -2.9, 18/47 lines), [[INSIG1]] 0.754× (z -2.8, 15/47 lines), [[PTGS2]] 0.803× (z -2.6, 2/21 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 137]] (+2.5), [[Module 230]] (+2.1) | [[Module 059]] (-2.2) |
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

- [[Vismodegib (drug)]] (+0.75, Sonic inhibitor, ⚠ only 5 significant genes); [[Finasteride (drug)]] (+0.74, unclear); [[Brimonidine (drug)]] (+0.69, Adrenoceptor agonist); [[Cilostazol (drug)]] (+0.68, unclear); [[Bisoprolol (hemifumarate) (drug)]] (+0.67, Adrenoceptor agonist); [[Adenosine (drug)]] (+0.65, unclear, ⚠ only 9 significant genes); [[Acetohexamide (drug)]] (+0.62, unclear); [[Dabrafenib (drug)]] (+0.58, RAF inhibitor); [[Demeclocycline (drug)]] (+0.57, unclear); [[MK-8353 (drug)]] (+0.57, Other MAPK inhibitor)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Dapagliflozin"
- `tables/drugdoses.parquet` — dd in 320, 321, 322
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
