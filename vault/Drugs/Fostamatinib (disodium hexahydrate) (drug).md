---
drug: "Fostamatinib (disodium hexahydrate)"
type: "drug"
salt_base: "Fostamatinib"
targets: "SYK, FLT3, LYN, LCK"
moa_fine: "Other TK inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 3
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Fostamatinib (disodium hexahydrate)

*Other TK inhibitor (inhibitor/antagonist) · targets: SYK, FLT3, LYN, LCK · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 1 / 0 / 3; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): none.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.16 / 0.23.
> Flags by dose: unreliable plate only / unreliable plate only / unreliable plate only. ⚠ 0.05 µM: unreliable plate only; 0.5 µM: unreliable plate only; 5 µM: unreliable plate only (artifact flags: its changes there are shown with an alert, not left out).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 13]]:H4 | 0 / 1 | — | +0.22 | +0.1/-0.2/-0.4 | ⚠ unreliable plate only |
| 0.5 µM | [[Plate 13]]:G4 | 0 / 0 | — | -0.28 | +0.6/+0.1/+0.4 | ⚠ unreliable plate only |
| 5 µM | [[Plate 13]]:F4 | 1 / 2 | — | -0.16 | -0.4/-0.2/-0.3 | ⚠ unreliable plate only |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**5 µM** (1 gene, 1 with an alert ⚠; the drug-dose carries ⚠ unreliable plate only): [[SLC37A2]] ⚠ 1.38× (z +3.3, 0/34 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, 1 with an alert ⚠; the drug-dose carries ⚠ unreliable plate only): [[TRIP10]] ⚠ 0.825× (z -3.4, 5/48 lines)

**5 µM** (2 genes, 2 with an alert ⚠; the drug-dose carries ⚠ unreliable plate only): [[PFKL]] ⚠ 0.804× (z -3.6, 18/48 lines), [[PCBP1]] ⚠ 0.823× (z -3.0, 16/48 lines)

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
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: only 3 significant genes; no trustworthy dose (vector dose flagged: unreliable plate only). Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 4 next most similar without an alert.*

- [[Ivabradine (hydrochloride) (drug)]] (+0.80, unclear, ⚠ no trustworthy dose (vector dose flagged: unreliable plate only)); [[Plicamycin (drug)]] (+0.71, unclear, ⚠ only 3 significant genes; no trustworthy dose (vector dose flagged: unreliable plate only)); [[Verteporfin (drug)]] (+0.70, unclear); [[Ligustrazine (drug)]] (+0.66, unclear, ⚠ only 2 significant genes); [[Vandetanib (drug)]] (+0.60, Multi-TK inhibitor); [[Cabozantinib (S-malate) (drug)]] (+0.60, Multi-TK inhibitor); [[Cysteamine (hydrochloride) (drug)]] (+0.58, unclear); [[Edoxaban (tosylate monohydrate) (drug)]] (+0.58, unclear, ⚠ no trustworthy dose (vector dose flagged: unreliable plate only)); [[Pasireotide (acetate) (drug)]] (+0.50, unclear); [[Ciclopirox (drug)]] (+0.50, unclear); [[Lidocaine (hydrochloride) (drug)]] (+0.48, unclear); [[Ponatinib (drug)]] (+0.48, Multi-TK inhibitor)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Fostamatinib (disodium hexahydrate)"
- `tables/drugdoses.parquet` — dd in 471, 472, 473
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
