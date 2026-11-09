---
drug: "LJI308"
type: "drug"
salt_base: "LJI308"
targets: "RPS6KA1, RPS6KA3, RPS6KA2"
moa_fine: "Other MAPK inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "0.05"
max_sig_genes: 35
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# LJI308

*Other MAPK inhibitor (inhibitor/antagonist) · targets: RPS6KA1, RPS6KA3, RPS6KA2 · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 35 / 2 / 4; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): low dose only (noise?).
> Signature similarity between consecutive doses (low–mid / mid–high): 0.50 / -0.13.
> Flags by dose: - / low cells (technical?); plate-row cell shift; noisy plate (z scaled) / noisy plate (z scaled).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:E4 | 16 / 19 | — | -0.10 | +1.6/+1.5/+2.2 | — |
| 0.5 µM | [[Plate 02]]:E4 | 1 / 1 | — | -1.12 | +0.4/+0.8/+1.1 | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:E4 | 3 / 1 | — | -0.31 | -0.9/-0.5/-0.1 | noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (16 genes, none with an alert; 12 shown): [[NDUFA9]] 1.25× (z +4.7, 21/48 lines), [[NFYB]] 1.28× (z +3.7, 13/48 lines), [[PIK3R2]] 1.26× (z +3.4, 5/47 lines), [[KPNA2]] 1.34× (z +3.4, 19/48 lines), [[NNMT]] 1.47× (z +3.3, 9/24 lines), [[PCOLCE]] 1.38× (z +3.2, 5/37 lines), [[LMF2]] 1.28× (z +3.1, 2/43 lines), [[PIGS]] 1.22× (z +3.1, 6/48 lines), [[TAF9]] 1.24× (z +3.0, 10/48 lines), [[CX3CL1]] 1.48× (z +3.0, 3/17 lines), [[SORCS2]] 1.34× (z +3.0, 1/24 lines), [[TAP1]] 1.24× (z +2.9, 11/48 lines)

**0.5 µM** (1 gene, none with an alert): [[RPUSD2]] 1.71× (z +3.5, 2/28 lines)

**5 µM** (3 genes, none with an alert): [[WARS1]] 1.45× (z +3.1, 6/47 lines), [[NIBAN1]] 1.38× (z +2.8, 10/37 lines), [[MARS1]] 1.36× (z +2.7, 14/48 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (19 genes, none with an alert; 12 shown): [[HTR7]] 0.675× (z -3.7, 6/24 lines), [[KCNN4]] 0.763× (z -3.5, 15/34 lines), [[MFSD14CP]] 0.753× (z -3.4, 9/48 lines), [[ENSG00000269476]] 0.638× (z -3.4, 13/38 lines), [[ZFYVE28]] 0.827× (z -3.3, 15/44 lines), [[ENSG00000290399]] 0.750× (z -3.3, 3/34 lines), [[ZNF274]] 0.807× (z -3.2, 12/47 lines), [[SLC1A1]] 0.819× (z -3.1, 8/37 lines), [[LRRC8C]] 0.813× (z -3.1, 12/40 lines), [[ABTB3]] 0.828× (z -3.1, 7/25 lines), [[RPSAP52]] 0.747× (z -3.1, 10/25 lines), [[PRR5-ARHGAP8]] 0.755× (z -3.1, 5/37 lines)

**0.5 µM** (1 gene, none with an alert): [[TMEM120B]] 0.823× (z -2.9, 6/48 lines)

**5 µM** (1 gene, none with an alert): [[TRAP1]] 0.831× (z -2.7, 0/48 lines)

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
| 0.05 µM | — | [[SNU-423 (line)]] (1.95), [[H4 (line)]] (1.67), [[RPMI-7951 (line)]] (1.66), [[J82 (line)]] (1.65) · weakest: [[AN3 CA (line)]] (0.285), [[HT-29 (line)]] (0.479), [[NCI-H1573 (line)]] (0.507) |
| 0.5 µM | — | — |
| 5 µM | [[H4 (line)]] (-3.6) | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar.*

- [[AZD-7648 (drug)]] (+0.71, DNA synthesis/repair inhibitor); [[Elimusertib hydrochloride (drug)]] (+0.64, unclear); [[Sonidegib (drug)]] (+0.60, Sonic inhibitor); [[Perindopril (erbumine) (drug)]] (+0.58, unclear); [[Trametinib (DMSO_TF solvate) (drug)]] (+0.58, MEK inhibitor); [[Capmatinib (drug)]] (+0.56, EGFR/ERBB inhibitor); [[Binimetinib (drug)]] (+0.55, MEK inhibitor); [[DT-061 (drug)]] (+0.55, unclear)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "LJI308"
- `tables/drugdoses.parquet` — dd in 591, 592, 593
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
