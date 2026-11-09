---
drug: "Carbidopa (monohydrate)"
type: "drug"
salt_base: "Carbidopa"
targets: "AHR"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.05"
max_sig_genes: 306
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Carbidopa (monohydrate)

*unclear (inhibitor/antagonist) · targets: AHR · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 306 / 7 / 5; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): low dose only (noise?).
> Signature similarity between consecutive doses (low–mid / mid–high): -0.01 / 0.14.
> Flags by dose: unreliable plate only; position not correctable / unreliable plate only / unreliable plate only. ⚠ 0.05 µM: unreliable plate only; position not correctable; 0.5 µM: unreliable plate only; 5 µM: unreliable plate only (artifact flags: its changes there are shown with an alert, not left out).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 13]]:H11 | 63 / 243 | — | +0.65 | -0.5/-0.6/-0.8 | ⚠ unreliable plate only; position not correctable |
| 0.5 µM | [[Plate 13]]:G11 | 5 / 2 | — | -0.22 | +0.3/+0.3/+0.9 | ⚠ unreliable plate only |
| 5 µM | [[Plate 13]]:F11 | 5 / 0 | — | +0.24 | -0.9/-0.7/-0.2 | ⚠ unreliable plate only |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (63 genes, 63 with an alert ⚠; the drug-dose carries ⚠ unreliable plate only; position not correctable; 12 shown): [[MTND2P28]] ⚠ 6.09× (z +12.7, 46/46 lines), [[PLBD2]] ⚠ 1.51× (z +8.0, 37/48 lines), [[ENSG00000278996]] ⚠ 3.27× (z +7.2, 41/48 lines), [[ENSG00000285043]] ⚠ 1.91× (z +6.5, 18/47 lines), [[APH1A]] ⚠ 1.51× (z +5.7, 37/48 lines), [[MT-ND1]] ⚠ 2.01× (z +5.6, 47/49 lines), [[TOR4A]] ⚠ 1.49× (z +5.4, 12/34 lines), [[7SK]] ⚠ 4.51× (z +5.1, 48/49 lines), [[KLF9]] ⚠ 1.35× (z +5.0, 22/43 lines), [[ATN1]] ⚠ 1.32× (z +4.9, 34/49 lines), [[TAPBP]] ⚠ 1.33× (z +4.8, 40/49 lines), [[INTS11]] ⚠ 1.32× (z +4.8, 21/48 lines)

**0.5 µM** (5 genes, 5 with an alert ⚠; the drug-dose carries ⚠ unreliable plate only): [[KLF9]] ⚠ 1.51× (z +6.9, 29/43 lines), [[PHKA1]] ⚠ 1.21× (z +4.4, 14/40 lines), [[TNFRSF9]] ⚠ 1.41× (z +3.4, 3/26 lines), [[ALDH1A3]] ⚠ 1.26× (z +3.0, 7/27 lines), [[TP53INP2]] ⚠ 1.24× (z +2.9, 6/46 lines)

**5 µM** (5 genes, 5 with an alert ⚠; the drug-dose carries ⚠ unreliable plate only): [[KLF9]] ⚠ 1.44× (z +6.1, 29/43 lines), [[ALDH1A3]] ⚠ 1.31× (z +3.5, 14/27 lines), [[SCNN1A]] ⚠ 1.28× (z +3.4, 11/22 lines), [[CPM]] ⚠ 1.27× (z +3.3, 9/46 lines), [[CYP1B1]] ⚠ 1.50× (z +2.8, 11/20 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (243 genes, 243 with an alert ⚠; the drug-dose carries ⚠ unreliable plate only; position not correctable; 12 shown): [[ENSG00000283765]] ⚠ 0.331× (z -9.8, 36/46 lines), [[TNKS1BP1]] ⚠ 0.563× (z -7.3, 44/48 lines), [[INO80B]] ⚠ 0.595× (z -7.1, 38/47 lines), [[ENSG00000289293]] ⚠ 0.465× (z -7.0, 30/47 lines), [[PET100]] ⚠ 0.470× (z -6.9, 30/47 lines), [[ENSG00000217801]] ⚠ 0.463× (z -6.6, 30/43 lines), [[BCAP31]] ⚠ 0.623× (z -6.6, 41/48 lines), [[CDK5RAP3]] ⚠ 0.612× (z -6.5, 42/48 lines), [[ASMTL-AS1]] ⚠ 0.464× (z -6.5, 39/48 lines), [[ENSG00000288993]] ⚠ 0.461× (z -6.5, 20/38 lines), [[RPL41]] ⚠ 0.513× (z -6.4, 44/48 lines), [[DDX23]] ⚠ 0.722× (z -6.4, 39/48 lines)

**0.5 µM** (2 genes, 2 with an alert ⚠; the drug-dose carries ⚠ unreliable plate only): [[LPCAT4]] ⚠ 0.825× (z -3.0, 6/47 lines), [[SYNE3]] ⚠ 0.824× (z -2.8, 3/36 lines)

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
| 0.05 µM | — | [[NCI-H661 (line)]] (1.24), [[hTERT-HPNE (line)]] (1.17), [[SNU-1 (line)]] (1.15), [[HepG2_C3A (line)]] (1.13) · weakest: [[NCI-H2122 (line)]] (0.318), [[SW 1271 (line)]] (0.871), [[BT-474 (line)]] (0.926) |
| 0.5 µM | — | — |
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: no trustworthy dose (vector dose flagged: unreliable plate only; position not correctable). Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 5 next most similar without an alert.*

- [[Ribociclib (drug)]] (+0.75, CDK inhibitor, ⚠ no trustworthy dose (vector dose flagged: unreliable plate only; position not correctable)); [[Futibatinib (drug)]] (+0.66, Other TK inhibitor); [[Relugolix (drug)]] (+0.55, unclear, ⚠ only 5 significant genes); [[Ivabradine (hydrochloride) (drug)]] (+0.52, unclear, ⚠ no trustworthy dose (vector dose flagged: unreliable plate only)); [[Loperamide (hydrochloride) (drug)]] (+0.51, unclear); [[Voriconazole (drug)]] (+0.50, unclear, ⚠ only 6 significant genes); [[Sinomenine (drug)]] (+0.47, unclear); [[Altretamine (drug)]] (+0.44, DNA synthesis/repair inhibitor, ⚠ only 1 significant gene); [[Doxycycline (monohydrate) (drug)]] (+0.41, unclear); [[Menadione (drug)]] (+0.38, unclear); [[Arbutin (drug)]] (+0.37, unclear); [[Anethole trithione (drug)]] (+0.35, unclear); [[Rutin (trihydrate) (drug)]] (+0.33, unclear)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Carbidopa (monohydrate)"
- `tables/drugdoses.parquet` — dd in 248, 249, 250
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
