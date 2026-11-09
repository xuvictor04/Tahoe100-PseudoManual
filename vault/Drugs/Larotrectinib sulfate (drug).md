---
drug: "Larotrectinib sulfate"
type: "drug"
salt_base: "Larotrectinib sulfate"
targets: "NTRK1, NTRK2, NTRK3"
moa_fine: "Other TK inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 94
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Larotrectinib sulfate

*Other TK inhibitor (inhibitor/antagonist) · targets: NTRK1, NTRK2, NTRK3 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 60 / 94 / 21; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.37 / 0.54.
> Flags by dose: unreliable plate only / unreliable plate only / unreliable plate only. ⚠ 0.05 µM: unreliable plate only; 0.5 µM: unreliable plate only; 5 µM: unreliable plate only (artifact flags: its changes there are shown with an alert, not left out).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 13]]:H8 | 23 / 37 | — | -0.20 | -2.5/-3.8/-0.4 | ⚠ unreliable plate only |
| 0.5 µM | [[Plate 13]]:G8 | 74 / 20 | — | -0.48 | -2.9/-1.8/-1.6 | ⚠ unreliable plate only |
| 5 µM | [[Plate 13]]:F8 | 15 / 6 | — | +0.19 | -1.7/-1.3/-1.7 | ⚠ unreliable plate only |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (23 genes, 23 with an alert ⚠; the drug-dose carries ⚠ unreliable plate only; 12 shown): [[ACOT7]] ⚠ 1.27× (z +5.2, 18/46 lines; unreliable plate only; position correction uncertain), [[KLHL24]] ⚠ 1.32× (z +4.5, 36/48 lines), [[CREBRF]] ⚠ 1.29× (z +4.0, 27/48 lines), [[FBXO32]] ⚠ 1.30× (z +3.9, 16/34 lines), [[WASHC2C]] ⚠ 1.22× (z +3.9, 3/47 lines), [[ENSG00000237596]] ⚠ 1.39× (z +3.7, 10/33 lines), [[ING4]] ⚠ 1.22× (z +3.7, 11/48 lines), [[ROR2]] ⚠ 1.23× (z +3.6, 3/22 lines), [[HDAC9]] ⚠ 1.20× (z +3.5, 14/39 lines), [[HSPBAP1]] ⚠ 1.24× (z +3.4, 6/47 lines), [[DPY19L2P3]] ⚠ 1.27× (z +3.3, 2/45 lines), [[WDR81]] ⚠ 1.29× (z +3.3, 3/47 lines)

**0.5 µM** (74 genes, 74 with an alert ⚠; the drug-dose carries ⚠ unreliable plate only; 12 shown): [[SKIL]] ⚠ 1.33× (z +4.9, 29/46 lines), [[KIF26B]] ⚠ 1.32× (z +4.5, 10/37 lines), [[EPHB2]] ⚠ 1.24× (z +4.5, 17/41 lines), [[PMEPA1]] ⚠ 1.29× (z +4.3, 23/42 lines), [[ARHGEF28]] ⚠ 1.30× (z +4.2, 22/42 lines), [[FHOD3]] ⚠ 1.31× (z +4.2, 16/34 lines), [[VAC14]] ⚠ 1.25× (z +4.1, 22/48 lines), [[SYT14]] ⚠ 1.36× (z +4.1, 9/19 lines), [[DNAH14]] ⚠ 1.32× (z +4.0, 21/38 lines), [[RAB27B]] ⚠ 1.30× (z +3.9, 18/33 lines), [[CCDC91]] ⚠ 1.23× (z +3.9, 28/46 lines), [[HSPBAP1]] ⚠ 1.28× (z +3.9, 7/47 lines)

**5 µM** (15 genes, 15 with an alert ⚠; the drug-dose carries ⚠ unreliable plate only; 12 shown): [[PMEPA1]] ⚠ 1.34× (z +5.0, 25/42 lines), [[VAC14]] ⚠ 1.26× (z +4.3, 19/48 lines), [[FBXL2]] ⚠ 1.21× (z +3.8, 18/41 lines), [[SKIL]] ⚠ 1.24× (z +3.8, 25/46 lines), [[RRAGC-DT]] ⚠ 1.35× (z +3.6, 14/48 lines), [[NAV2]] ⚠ 1.24× (z +3.6, 17/31 lines), [[TM4SF19]] ⚠ 1.31× (z +3.6, 12/28 lines), [[ENSG00000237596]] ⚠ 1.37× (z +3.5, 6/33 lines), [[WDR19]] ⚠ 1.22× (z +3.3, 15/48 lines), [[ARHGEF28]] ⚠ 1.22× (z +3.2, 15/42 lines), [[ENSG00000230479]] ⚠ 1.24× (z +3.2, 12/35 lines), [[PIK3CD]] ⚠ 1.21× (z +3.1, 6/40 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (37 genes, 37 with an alert ⚠; the drug-dose carries ⚠ unreliable plate only; 12 shown): [[MAP7D1]] ⚠ 0.802× (z -3.9, 16/48 lines), [[EXO1]] ⚠ 0.754× (z -3.7, 12/46 lines), [[SPDL1]] ⚠ 0.740× (z -3.6, 20/45 lines), [[TACC3]] ⚠ 0.814× (z -3.6, 13/48 lines), [[KIF18B]] ⚠ 0.752× (z -3.6, 17/46 lines), [[CDC25A]] ⚠ 0.694× (z -3.6, 10/41 lines), [[BUB1]] ⚠ 0.761× (z -3.5, 19/47 lines), [[CEP55]] ⚠ 0.799× (z -3.4, 14/46 lines), [[TFDP1]] ⚠ 0.808× (z -3.4, 15/48 lines), [[NCAPG2]] ⚠ 0.825× (z -3.4, 17/48 lines), [[SKA3]] ⚠ 0.776× (z -3.4, 8/44 lines), [[LMNB2]] ⚠ 0.796× (z -3.3, 15/48 lines)

**0.5 µM** (20 genes, 20 with an alert ⚠; the drug-dose carries ⚠ unreliable plate only; 12 shown): [[HMGCR]] ⚠ 0.746× (z -4.2, 26/48 lines), [[PSAT1]] ⚠ 0.721× (z -4.2, 16/39 lines), [[MARS1]] ⚠ 0.799× (z -3.9, 19/48 lines), [[MSMO1]] ⚠ 0.707× (z -3.7, 23/47 lines), [[HSPA14]] ⚠ 0.817× (z -3.6, 11/47 lines), [[SCD]] ⚠ 0.790× (z -3.4, 25/48 lines), [[PARP2]] ⚠ 0.809× (z -3.4, 11/47 lines), [[EED]] ⚠ 0.818× (z -3.3, 15/48 lines), [[LAG3]] ⚠ 0.649× (z -3.3, 9/37 lines), [[FDFT1]] ⚠ 0.789× (z -3.3, 17/47 lines), [[SASS6]] ⚠ 0.818× (z -3.2, 13/48 lines), [[DDIAS]] ⚠ 0.784× (z -3.2, 9/46 lines)

**5 µM** (6 genes, 6 with an alert ⚠; the drug-dose carries ⚠ unreliable plate only): [[MARS1]] ⚠ 0.806× (z -3.7, 20/48 lines), [[FBXW10B]] ⚠ 0.682× (z -3.1, 7/36 lines), [[SMIM41]] ⚠ 0.626× (z -3.1, 10/45 lines), [[MFSD2A]] ⚠ 0.727× (z -3.0, 9/44 lines), [[GPX8]] ⚠ 0.790× (z -3.0, 9/40 lines), [[ENSG00000230615]] ⚠ 0.794× (z -2.9, 5/23 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | [[Module 006]] (-2.0) |
| 0.5 µM | [[Module 230]] (+2.1) | [[Module 207]] (-2.6), [[Module 179]] (-2.3), [[Module 065]] (-2.2) |
| 5 µM | — | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[NCI-H460 (line)]] (1.37), [[RKO (line)]] (1.34), [[RPMI-7951 (line)]] (1.28), [[HOP62 (line)]] (1.27) · weakest: [[SW 1271 (line)]] (0.462), [[SHP-77 (line)]] (0.489), [[A-427 (line)]] (0.502) |
| 0.5 µM | — | [[SW 1088 (line)]] (1.42), [[RPMI-7951 (line)]] (1.36), [[SW 900 (line)]] (1.23), [[LOX-IMVI (line)]] (1.18) · weakest: [[SHP-77 (line)]] (0.426), [[A-427 (line)]] (0.519), [[COLO 205 (line)]] (0.533) |
| 5 µM | — | [[H4 (line)]] (1.71), [[NCI-H460 (line)]] (1.65), [[hTERT-HPNE (line)]] (1.52), [[HOP62 (line)]] (1.50) · weakest: [[NCI-H661 (line)]] (0.209), [[SW 1271 (line)]] (0.333), [[SW48 (line)]] (0.393) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: no trustworthy dose (vector dose flagged: unreliable plate only). Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar.*

- [[Rapamycin (drug)]] (+0.76, MTOR inhibitor); [[Apalutamide (drug)]] (+0.63, Androgen receptor antagonist); [[Esmolol (hydrochloride) (drug)]] (+0.63, unclear); [[Meloxicam (drug)]] (+0.61, Cyclooxygenase inhibitor); [[AZD-8055 (drug)]] (+0.60, MTOR inhibitor); [[Temsirolimus (drug)]] (+0.59, MTOR inhibitor); [[Mifepristone (drug)]] (+0.58, unclear); [[Abiraterone acetate (drug)]] (+0.58, unclear)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Larotrectinib sulfate"
- `tables/drugdoses.parquet` — dd in 609, 610, 611
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
