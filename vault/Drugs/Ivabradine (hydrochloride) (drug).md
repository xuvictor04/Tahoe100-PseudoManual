---
drug: "Ivabradine (hydrochloride)"
type: "drug"
salt_base: "Ivabradine"
targets: "HCN4"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 21
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Ivabradine (hydrochloride)

*unclear (inhibitor/antagonist) · targets: HCN4 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 0 / 8 / 21; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): -0.06 / 0.06.
> Flags by dose: unreliable plate only / transcription drop; unreliable plate only / unreliable plate only. ⚠ 0.05 µM: unreliable plate only; 0.5 µM: transcription drop; unreliable plate only; 5 µM: unreliable plate only (artifact flags: its changes there are shown with an alert, not left out).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 13]]:H5 | 0 / 0 | — | -0.22 | -0.3/-0.8/-0.8 | ⚠ unreliable plate only |
| 0.5 µM | [[Plate 13]]:G5 | 5 / 3 | — | -0.80 | +0.2/-0.5/+0.8 | ⚠ transcription drop; unreliable plate only |
| 5 µM | [[Plate 13]]:F5 | 0 / 21 | — | -0.01 | -0.8/-0.9/-0.1 | ⚠ unreliable plate only |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (5 genes, 5 with an alert ⚠; the drug-dose carries ⚠ transcription drop; unreliable plate only): [[TTC39A]] ⚠ 1.30× (z +3.6, 4/41 lines), [[NSMCE1-DT]] ⚠ 1.41× (z +3.3, 0/33 lines), [[TRPV4]] ⚠ 1.42× (z +3.1, 0/18 lines), [[THAP2]] ⚠ 1.22× (z +3.1, 1/44 lines), [[P3H2-AS1]] ⚠ 1.52× (z +3.0, 1/14 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (3 genes, 3 with an alert ⚠; the drug-dose carries ⚠ transcription drop; unreliable plate only): [[ADD3-AS1]] ⚠ 0.719× (z -3.1, 3/33 lines), [[ZNF692]] ⚠ 0.830× (z -3.0, 13/47 lines), [[BMS1P23]] ⚠ 0.748× (z -3.0, 9/37 lines)

**5 µM** (21 genes, 21 with an alert ⚠; the drug-dose carries ⚠ unreliable plate only; 12 shown): [[NFKB2]] ⚠ 0.781× (z -3.9, 30/48 lines), [[AXIN2]] ⚠ 0.782× (z -3.7, 0/16 lines), [[HAS3]] ⚠ 0.642× (z -3.7, 2/28 lines), [[ENSG00000285043]] ⚠ 0.677× (z -3.7, 8/43 lines), [[BCAR3-AS1]] ⚠ 0.717× (z -3.6, 10/42 lines), [[NCKIPSD]] ⚠ 0.799× (z -3.5, 17/48 lines), [[ADD2]] ⚠ 0.792× (z -3.5, 0/17 lines), [[MNT]] ⚠ 0.795× (z -3.5, 18/48 lines), [[FBRS]] ⚠ 0.808× (z -3.5, 14/48 lines), [[BCAR1]] ⚠ 0.824× (z -3.4, 12/48 lines), [[NID2]] ⚠ 0.717× (z -3.4, 0/15 lines), [[TAF6]] ⚠ 0.832× (z -3.4, 3/48 lines)

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
| 5 µM | — | [[SNU-1 (line)]] (1.99), [[SW1417 (line)]] (1.83), [[SW 900 (line)]] (1.59), [[RKO (line)]] (1.57) · weakest: [[CFPAC-1 (line)]] (0.356), [[KATO III (line)]] (0.639), [[SW 1271 (line)]] (0.690) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: no trustworthy dose (vector dose flagged: unreliable plate only). Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Fostamatinib (disodium hexahydrate) (drug)]] (+0.80, Other TK inhibitor, ⚠ only 3 significant genes; no trustworthy dose (vector dose flagged: unreliable plate only)); [[Loperamide (hydrochloride) (drug)]] (+0.65, unclear); [[Futibatinib (drug)]] (+0.63, Other TK inhibitor); [[Entecavir (monohydrate) (drug)]] (+0.60, unclear); [[Vandetanib (drug)]] (+0.59, Multi-TK inhibitor); [[Ciclopirox (drug)]] (+0.58, unclear); [[Ligustrazine (drug)]] (+0.57, unclear, ⚠ only 2 significant genes); [[Menadione (drug)]] (+0.54, unclear); [[Bisoprolol (hemifumarate) (drug)]] (+0.53, Adrenoceptor agonist); [[Sulfisoxazole (drug)]] (+0.52, unclear)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Ivabradine (hydrochloride)"
- `tables/drugdoses.parquet` — dd in 570, 571, 572
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
