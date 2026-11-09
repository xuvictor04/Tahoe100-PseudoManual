---
drug: "Atazanavir (sulfate)"
type: "drug"
salt_base: "Atazanavir"
targets: "CYP3A4"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 13
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Atazanavir (sulfate)

*unclear (inhibitor/antagonist) · targets: CYP3A4 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 1 / 13 / 2; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): low dose only (noise?).
> Signature similarity between consecutive doses (low–mid / mid–high): 0.08 / 0.29.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:E5 | 0 / 1 | — | +0.32 | -0.7/-0.1/+0.1 | — |
| 0.5 µM | [[Plate 11]]:E5 | 7 / 6 | — | -0.27 | +0.9/+0.5/+1.5 | — |
| 5 µM | [[Plate 12]]:E5 | 1 / 1 | — | -0.10 | +0.3/+0.7/+1.0 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (7 genes, none with an alert): [[SOCS2]] 1.33× (z +3.3, 3/34 lines), [[LMF2]] 1.26× (z +3.2, 6/42 lines), [[ZNF689]] 1.34× (z +3.1, 4/43 lines), [[NEGR1]] 1.22× (z +3.1, 0/24 lines), [[CENPM]] 1.37× (z +3.0, 4/39 lines), [[GPAA1]] 1.24× (z +2.9, 8/43 lines), [[GATM]] 1.33× (z +2.8, 1/32 lines)

**5 µM** (1 gene, none with an alert): [[ENSG00000282943]] 1.30× (z +2.8, 2/22 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[FITM2]] 0.820× (z -3.1, 6/47 lines)

**0.5 µM** (6 genes, none with an alert): [[TMPRSS5]] 0.690× (z -4.2, 13/40 lines), [[ERFL]] 0.679× (z -3.6, 9/33 lines), [[ENSG00000259868]] 0.735× (z -3.5, 7/35 lines), [[ZSCAN20]] 0.734× (z -3.3, 16/45 lines), [[LSP1P4]] 0.788× (z -3.1, 10/38 lines), [[ENSG00000259539]] 0.775× (z -2.9, 12/41 lines)

**5 µM** (1 gene, none with an alert): [[IL11RA]] 0.705× (z -3.4, 5/44 lines)

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
| 0.5 µM | [[C-33 A (line)]] (-3.3) | — |
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 3 next most similar without an alert.*

- [[Palmatine (chloride) (drug)]] (+0.61, unclear); [[Retinoic acid (drug)]] (+0.57, Retinoic receptor agonist); [[Ribociclib (drug)]] (+0.57, CDK inhibitor, ⚠ no trustworthy dose (vector dose flagged: unreliable plate only; position not correctable)); [[Rosiglitazone (drug)]] (+0.57, unclear); [[Canagliflozin (drug)]] (+0.55, Glucose transporter inhibitor); [[Megestrol (drug)]] (+0.53, unclear, ⚠ vector dose flagged: cell-cycle shift); [[Larotrectinib (drug)]] (+0.53, Other TK inhibitor); [[Olanzapine (drug)]] (+0.52, unclear, ⚠ only 5 significant genes); [[Omeprazole (drug)]] (+0.51, unclear); [[Valdecoxib (drug)]] (+0.50, Cyclooxygenase inhibitor); [[Demeclocycline (drug)]] (+0.50, unclear)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Atazanavir (sulfate)"
- `tables/drugdoses.parquet` — dd in 120, 121, 122
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
