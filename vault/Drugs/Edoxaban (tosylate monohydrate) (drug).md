---
drug: "Edoxaban (tosylate monohydrate)"
type: "drug"
salt_base: "Edoxaban"
targets: "F10"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 35
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Edoxaban (tosylate monohydrate)

*unclear (inhibitor/antagonist) · targets: F10 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 0 / 6 / 35; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): -0.03 / 0.17.
> Flags by dose: unreliable plate only / unreliable plate only / unreliable plate only. ⚠ 0.05 µM: unreliable plate only; 0.5 µM: unreliable plate only; 5 µM: unreliable plate only (artifact flags: its changes there are shown with an alert, not left out).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 13]]:H9 | 0 / 0 | — | +0.52 | -0.0/-0.2/-0.4 | ⚠ unreliable plate only |
| 0.5 µM | [[Plate 13]]:G9 | 2 / 4 | — | -0.63 | +0.3/-1.2/+0.3 | ⚠ unreliable plate only |
| 5 µM | [[Plate 13]]:F9 | 8 / 27 | — | +0.30 | +0.9/+0.2/+0.2 | ⚠ unreliable plate only |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (2 genes, 2 with an alert ⚠; the drug-dose carries ⚠ unreliable plate only): [[MAOA]] ⚠ 1.24× (z +2.9, 2/33 lines), [[NNMT]] ⚠ 1.33× (z +2.6, 5/23 lines)

**5 µM** (8 genes, 8 with an alert ⚠; the drug-dose carries ⚠ unreliable plate only): [[CCND3]] ⚠ 1.34× (z +4.0, 17/47 lines), [[NNMT]] ⚠ 1.47× (z +3.5, 10/24 lines), [[DNER]] ⚠ 1.30× (z +3.4, 11/17 lines), [[PID1]] ⚠ 1.25× (z +3.1, 11/26 lines), [[MIR181A2HG]] ⚠ 1.22× (z +2.9, 4/45 lines), [[IRAK3]] ⚠ 1.30× (z +2.9, 6/12 lines), [[SAA1]] ⚠ 1.87× (z +2.8, 9/19 lines), [[TFCP2L1]] ⚠ 1.21× (z +2.8, 7/26 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (4 genes, 4 with an alert ⚠; the drug-dose carries ⚠ unreliable plate only): [[TEF]] ⚠ 0.708× (z -4.7, 15/45 lines), [[PER2]] ⚠ 0.755× (z -3.9, 23/47 lines), [[PER3]] ⚠ 0.832× (z -3.0, 12/44 lines), [[ALS2CL]] ⚠ 0.803× (z -2.9, 2/33 lines)

**5 µM** (27 genes, 27 with an alert ⚠; the drug-dose carries ⚠ unreliable plate only; 12 shown): [[PER2]] ⚠ 0.265× (z -18.4, 48/49 lines), [[PER3]] ⚠ 0.358× (z -16.9, 38/45 lines), [[TEF]] ⚠ 0.331× (z -15.0, 37/47 lines), [[CRY1]] ⚠ 0.327× (z -11.9, 46/49 lines), [[NR6A1]] ⚠ 0.602× (z -10.8, 45/47 lines), [[CRY2]] ⚠ 0.524× (z -8.6, 39/48 lines), [[OSGIN1]] ⚠ 0.571× (z -6.3, 25/45 lines), [[MTHFD1L]] ⚠ 0.790× (z -5.7, 26/46 lines), [[MMRN2]] ⚠ 0.588× (z -5.5, 15/34 lines), [[DBP]] ⚠ 0.498× (z -5.3, 26/45 lines), [[TRAPPC6A]] ⚠ 0.516× (z -5.2, 26/46 lines), [[EIF5A2]] ⚠ 0.726× (z -4.9, 21/44 lines)

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
| 5 µM | — | [[HS-578T (line)]] (1.96), [[H4 (line)]] (1.86), [[hTERT-HPNE (line)]] (1.68), [[RPMI-7951 (line)]] (1.65) · weakest: [[RKO (line)]] (0.181), [[AN3 CA (line)]] (0.393), [[LoVo (line)]] (0.456) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: no trustworthy dose (vector dose flagged: unreliable plate only). Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Phenylephrine (hydrochloride) (drug)]] (+0.65, Adrenoceptor agonist); [[Dexamethasone (drug)]] (+0.62, Glucocorticoid receptor agonist); [[Fostamatinib (disodium hexahydrate) (drug)]] (+0.58, Other TK inhibitor, ⚠ only 3 significant genes; no trustworthy dose (vector dose flagged: unreliable plate only)); [[Econazole (drug)]] (+0.57, unclear); [[Betamethasone dipropionate (drug)]] (+0.54, Glucocorticoid receptor agonist); [[Bexarotene (drug)]] (+0.53, Retinoic receptor agonist); [[Triamcinolone (drug)]] (+0.49, Glucocorticoid receptor agonist); [[Ivabradine (hydrochloride) (drug)]] (+0.48, unclear, ⚠ no trustworthy dose (vector dose flagged: unreliable plate only)); [[Loperamide (hydrochloride) (drug)]] (+0.45, unclear); [[Regorafenib (drug)]] (+0.44, Multi-TK inhibitor)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Edoxaban (tosylate monohydrate)"
- `tables/drugdoses.parquet` — dd in 398, 399, 400
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
