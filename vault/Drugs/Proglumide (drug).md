---
drug: "Proglumide"
type: "drug"
salt_base: "Proglumide"
targets: "CCKBR, CCKAR"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "0.05"
max_sig_genes: 14
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Proglumide

*unclear (inhibitor/antagonist) · targets: CCKBR, CCKAR · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 14 / 0 / 0; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): low dose only (noise?).
> Signature similarity between consecutive doses (low–mid / mid–high): 0.07 / 0.30.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:D11 | 12 / 2 | — | -0.55 | -0.4/-0.5/-1.7 | — |
| 0.5 µM | [[Plate 11]]:D11 | 0 / 0 | — | -0.02 | +0.3/-0.2/-0.2 | — |
| 5 µM | [[Plate 12]]:D11 | 0 / 0 | — | -0.16 | +0.4/+0.1/-0.2 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (12 genes, none with an alert): [[ST8SIA6-AS1]] 1.55× (z +3.7, 0/8 lines), [[UBE2Q2P13]] 1.39× (z +3.4, 1/20 lines), [[ENSG00000285000]] 1.30× (z +3.2, 7/43 lines), [[ZBED9]] 1.37× (z +3.2, 0/32 lines), [[ENSG00000285835]] 1.30× (z +3.1, 0/25 lines), [[ENSG00000287721]] 1.55× (z +3.1, 3/39 lines), [[BMP8B]] 1.37× (z +3.1, 3/33 lines), [[ENSG00000224635]] 1.44× (z +3.1, 5/39 lines), [[ENSG00000287862]] 1.42× (z +3.0, 1/10 lines), [[KCNK13]] 1.32× (z +3.0, 1/26 lines), [[TMEM45A]] 1.26× (z +2.9, 7/35 lines), [[DNAH12]] 1.34× (z +2.7, 1/43 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (2 genes, none with an alert): [[LINC00938]] 0.766× (z -3.4, 8/47 lines), [[PPTC7]] 0.808× (z -3.2, 16/48 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | [[Module 182]] (-2.1), [[Module 168]] (-2.1) |
| 0.5 µM | — | — |
| 5 µM | — | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | [[HEC-1-A (line)]] (-3.4) | — |
| 0.5 µM | — | — |
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[Mifepristone (drug)]] (+0.82, unclear); [[Estrone sulfate (potassium) (drug)]] (+0.80, unclear); [[Apalutamide (drug)]] (+0.78, Androgen receptor antagonist); [[Tirabrutinib (drug)]] (+0.70, Other TK inhibitor); [[L-Eflornithine (monohydrochloride) (drug)]] (+0.70, unclear); [[Glasdegib (drug)]] (+0.69, Sonic inhibitor, ⚠ only 4 significant genes; no trustworthy dose (vector dose flagged: unreliable plate only)); [[Esmolol (hydrochloride) (drug)]] (+0.66, unclear); [[Carbamazepine (drug)]] (+0.65, HDAC inhibitor); [[Diphenhydramine (drug)]] (+0.62, unclear)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Proglumide"
- `tables/drugdoses.parquet` — dd in 845, 846, 847
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
