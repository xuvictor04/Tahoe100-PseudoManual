---
drug: "Estrone sulfate (potassium)"
type: "drug"
salt_base: "Estrone sulfate"
targets: ""
moa_fine: "unclear"
moa_broad: "unclear"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 108
tags: ["drug", "moa/unclear"]
generated_by: "tahoemap"
---

# Estrone sulfate (potassium)

*unclear (unclear) · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 5 / 16 / 108; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.12 / 0.34.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:C4 | 5 / 0 | — | -0.01 | -0.4/+0.3/+0.7 | — |
| 0.5 µM | [[Plate 11]]:C4 | 15 / 1 | — | -0.45 | -0.5/+0.1/+0.0 | — |
| 5 µM | [[Plate 12]]:C4 | 60 / 48 | — | +0.02 | +0.4/+0.7/-0.6 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (5 genes, none with an alert): [[PLBD2]] 1.24× (z +4.1, 14/48 lines), [[CNTN6]] 1.42× (z +3.0, 0/8 lines), [[ENSG00000232754]] 1.29× (z +3.0, 1/43 lines), [[LINC03046]] 1.35× (z +2.9, 0/10 lines), [[KCNAB1]] 1.27× (z +2.7, 2/44 lines)

**0.5 µM** (15 genes, none with an alert; 12 shown): [[ENSG00000228613]] 1.46× (z +3.5, 2/23 lines), [[SDR16C5]] 1.44× (z +3.5, 1/20 lines), [[RAMP1]] 1.36× (z +3.4, 1/27 lines), [[BMP5]] 1.48× (z +3.3, 2/10 lines), [[ENSG00000229642]] 1.48× (z +3.2, 1/11 lines), [[ABCC9]] 1.42× (z +3.2, 2/15 lines), [[ADGRF5]] 1.63× (z +3.2, 0/6 lines), [[LINC01917]] 1.53× (z +3.1, 1/13 lines), [[HYAL3]] 1.37× (z +3.1, 8/34 lines), [[POTEE]] 1.63× (z +3.0, 0/11 lines), [[AGTR1]] 1.51× (z +3.0, 1/9 lines), [[DSC3]] 1.30× (z +2.8, 2/16 lines)

**5 µM** (60 genes, none with an alert; 12 shown): [[MX2]] 1.62× (z +4.2, 27/32 lines), [[PCOLCE2]] 1.28× (z +4.0, 3/31 lines), [[ENSG00000159239]] 1.36× (z +3.9, 0/45 lines), [[RIGI]] 1.40× (z +3.9, 31/45 lines), [[STING1]] 1.46× (z +3.8, 10/30 lines), [[PTPRD]] 1.33× (z +3.8, 8/23 lines), [[SAMD9]] 1.58× (z +3.8, 30/37 lines), [[SP110]] 1.38× (z +3.8, 27/43 lines), [[COL27A1]] 1.21× (z +3.8, 12/36 lines), [[DHRS2]] 1.72× (z +3.8, 4/34 lines), [[CALCRL]] 1.47× (z +3.7, 3/28 lines), [[TMEM45A]] 1.35× (z +3.7, 16/35 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (1 gene, none with an alert): [[DUSP7]] 0.777× (z -3.3, 8/41 lines)

**5 µM** (48 genes, none with an alert; 12 shown): [[RBM14]] 0.736× (z -4.1, 28/48 lines), [[PPP1R15B]] 0.725× (z -4.1, 32/48 lines), [[LRRFIP2]] 0.812× (z -4.1, 26/48 lines), [[EFCAB12]] 0.611× (z -3.8, 10/43 lines), [[SERAC1]] 0.805× (z -3.8, 9/47 lines), [[IQUB]] 0.692× (z -3.8, 10/44 lines), [[PPTC7]] 0.780× (z -3.7, 22/48 lines), [[SUPV3L1]] 0.760× (z -3.7, 24/48 lines), [[WDR49]] 0.667× (z -3.7, 16/44 lines), [[OTUD6B]] 0.782× (z -3.7, 17/48 lines), [[FAM168B]] 0.807× (z -3.7, 26/48 lines), [[ENSG00000284697]] 0.678× (z -3.7, 16/48 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | [[Module 182]] (-3.1), [[Module 171]] (-2.7), [[Module 168]] (-2.2) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | [[CHP-212 (line)]] (1.53), [[NCI-H1792 (line)]] (1.35), [[SNU-423 (line)]] (1.32), [[COLO 205 (line)]] (1.25) · weakest: [[BT-474 (line)]] (0.560), [[NCI-H661 (line)]] (0.566), [[HCT15 (line)]] (0.675) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar.*

- [[L-Eflornithine (monohydrochloride) (drug)]] (+0.95, unclear); [[Apalutamide (drug)]] (+0.88, Androgen receptor antagonist); [[Carbamazepine (drug)]] (+0.87, HDAC inhibitor); [[Esmolol (hydrochloride) (drug)]] (+0.83, unclear); [[Mifepristone (drug)]] (+0.83, unclear); [[Proglumide (drug)]] (+0.80, unclear); [[Tirabrutinib (drug)]] (+0.80, Other TK inhibitor); [[(R)-Verapamil (hydrochloride) (drug)]] (+0.77, unclear)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Estrone sulfate (potassium)"
- `tables/drugdoses.parquet` — dd in 432, 433, 434
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
