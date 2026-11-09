---
drug: "(R)-Verapamil (hydrochloride)"
type: "drug"
salt_base: "(R)-Verapamil"
targets: "ABCB1"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "0.05"
max_sig_genes: 100
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# (R)-Verapamil (hydrochloride)

*unclear (inhibitor/antagonist) · targets: ABCB1 · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 100 / 9 / 1; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): low dose only (noise?).
> Signature similarity between consecutive doses (low–mid / mid–high): 0.07 / 0.00.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:B5 | 25 / 75 | — | +0.34 | +2.4/+1.9/+0.1 | — |
| 0.5 µM | [[Plate 05]]:B5 | 6 / 3 | — | -0.20 | -1.2/-0.6/-0.1 | — |
| 5 µM | [[Plate 14]]:B5 | 1 / 0 | 0.797 | +0.24 | -1.2/-0.7/-1.1 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (25 genes, none with an alert; 12 shown): [[DCBLD2]] 1.28× (z +3.7, 26/40 lines), [[RRM2]] 1.34× (z +3.5, 26/46 lines), [[NEMP2]] 1.27× (z +3.4, 4/40 lines), [[CYTOR]] 1.29× (z +3.4, 24/47 lines), [[NRG1]] 1.24× (z +3.3, 8/30 lines), [[TSC22D1]] 1.20× (z +3.3, 20/49 lines), [[LINC00205]] 1.35× (z +3.3, 5/47 lines), [[MIR4435-2HG]] 1.20× (z +3.2, 17/46 lines), [[SCARA3]] 1.34× (z +3.2, 6/28 lines), [[ASPM]] 1.25× (z +3.2, 16/48 lines), [[MKI67]] 1.31× (z +3.1, 22/49 lines), [[RASAL2]] 1.21× (z +3.1, 19/48 lines)

**0.5 µM** (6 genes, none with an alert): [[NOTCH2NLA]] 1.31× (z +3.7, 8/42 lines), [[RXRB]] 1.25× (z +3.2, 4/48 lines), [[ENSG00000266578]] 1.44× (z +3.0, 0/17 lines), [[USH1C]] 1.29× (z +3.0, 0/14 lines), [[MOXD1]] 1.27× (z +2.9, 0/20 lines), [[RDUR]] 1.33× (z +2.9, 1/18 lines)

**5 µM** (1 gene, none with an alert): [[ABCG1]] 1.23× (z +3.2, 12/34 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (75 genes, none with an alert; 12 shown): [[DNAJC25]] 0.637× (z -5.1, 38/49 lines), [[JMY]] 0.739× (z -4.9, 35/48 lines), [[ELP2]] 0.721× (z -4.5, 36/49 lines), [[SLC15A2]] 0.644× (z -4.2, 21/46 lines), [[CLEC4A]] 0.647× (z -4.0, 12/47 lines), [[ENSG00000284697]] 0.656× (z -4.0, 20/48 lines), [[MPZL3]] 0.753× (z -3.9, 12/23 lines), [[TBC1D30]] 0.805× (z -3.9, 9/39 lines), [[CNNM2]] 0.783× (z -3.8, 26/49 lines), [[FBXO42]] 0.784× (z -3.7, 26/49 lines), [[MINDY2]] 0.820× (z -3.7, 24/49 lines), [[SRP54-AS1]] 0.728× (z -3.7, 27/48 lines)

**0.5 µM** (3 genes, none with an alert): [[ZNF852]] 0.805× (z -3.5, 10/46 lines), [[CFL2]] 0.811× (z -3.3, 6/42 lines), [[HROB]] 0.832× (z -3.0, 9/45 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | [[Module 207]] (-3.2), [[Module 041]] (-3.0), [[Module 179]] (-2.7) |
| 0.5 µM | — | — |
| 5 µM | — | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | [[HEC-1-A (line)]] (-3.3) | [[SW 1088 (line)]] (1.76), [[LS 180 (line)]] (1.62), [[H4 (line)]] (1.40), [[hTERT-HPNE (line)]] (1.39) · weakest: [[AN3 CA (line)]] (-0.0286), [[BT-474 (line)]] (0.202), [[SNU-1 (line)]] (0.475) |
| 0.5 µM | — | — |
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[Busulfan (drug)]] (+0.94, DNA synthesis/repair inhibitor); [[Larotrectinib (drug)]] (+0.94, Other TK inhibitor); [[Palmatine (chloride) (drug)]] (+0.91, unclear); [[Megestrol (drug)]] (+0.91, unclear, ⚠ vector dose flagged: cell-cycle shift); [[Diphenhydramine (drug)]] (+0.88, unclear); [[Esmolol (hydrochloride) (drug)]] (+0.87, unclear); [[Retinoic acid (drug)]] (+0.86, Retinoic receptor agonist); [[Gallic acid (hydrate) (drug)]] (+0.85, Cyclooxygenase inhibitor); [[Apalutamide (drug)]] (+0.83, Androgen receptor antagonist)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "(R)-Verapamil (hydrochloride)"
- `tables/drugdoses.parquet` — dd in 0, 1, 2
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
