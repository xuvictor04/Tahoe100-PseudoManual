---
drug: "Vitamin K4"
type: "drug"
salt_base: "Vitamin K4"
targets: ""
moa_fine: "unclear"
moa_broad: "unclear"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "0.05"
max_sig_genes: 210
tags: ["drug", "moa/unclear"]
generated_by: "tahoemap"
---

# Vitamin K4

*unclear (unclear) · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 210 / 0 / 3; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): low dose only (noise?).
> Signature similarity between consecutive doses (low–mid / mid–high): 0.32 / 0.24.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:C1 | 203 / 7 | — | +0.11 | +0.2/-0.9/-0.2 | — |
| 0.5 µM | [[Plate 11]]:C1 | 0 / 0 | — | -0.12 | +0.3/-0.1/-0.2 | — |
| 5 µM | [[Plate 12]]:C1 | 3 / 0 | — | -0.04 | +0.1/-0.1/+0.2 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (203 genes, none with an alert; 12 shown): [[CACNA1D]] 1.38× (z +5.0, 5/24 lines), [[ERC2]] 1.48× (z +4.7, 6/25 lines), [[PCLO]] 1.41× (z +4.6, 16/34 lines), [[GALNT13]] 1.32× (z +4.4, 0/18 lines), [[CDH11]] 1.44× (z +4.3, 0/13 lines), [[ACVR1C]] 1.40× (z +4.3, 7/42 lines), [[UNC5D]] 1.64× (z +4.1, 1/11 lines), [[SPATA6L]] 1.35× (z +4.1, 7/32 lines), [[BARX2]] 1.31× (z +4.1, 0/19 lines), [[GABPB1-AS1]] 1.30× (z +3.9, 19/47 lines), [[C19orf44]] 1.32× (z +3.9, 1/46 lines), [[LINC02086]] 1.36× (z +3.9, 6/24 lines)

**5 µM** (3 genes, none with an alert): [[CYP1B1]] 1.67× (z +3.5, 10/19 lines), [[TEX11]] 1.41× (z +2.9, 0/39 lines), [[RMDN2-AS1]] 1.47× (z +2.8, 2/30 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (7 genes, none with an alert): [[CCNK]] 0.830× (z -3.4, 19/49 lines), [[ZNF385A]] 0.771× (z -3.4, 6/40 lines), [[NT5DC3]] 0.784× (z -3.3, 21/49 lines), [[MED26]] 0.743× (z -3.2, 21/49 lines), [[ZNF143]] 0.821× (z -3.1, 11/49 lines), [[INSIG2]] 0.819× (z -2.9, 20/49 lines), [[UBA6]] 0.829× (z -2.7, 18/49 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | [[Module 207]] (-2.2) |
| 0.5 µM | — | — |
| 5 µM | — | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[hTERT-HPNE (line)]] (1.20), [[NCI-H2030 (line)]] (1.13), [[NCI-H1792 (line)]] (1.08), [[NCI-H460 (line)]] (1.07) · weakest: [[HEC-1-A (line)]] (0.529), [[SHP-77 (line)]] (0.546), [[SK-MEL-2 (line)]] (0.603) |
| 0.5 µM | — | — |
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[Benztropine (mesylate) (drug)]] (+0.92, unclear); [[Meloxicam (drug)]] (+0.88, Cyclooxygenase inhibitor); [[Bestatin (hydrochloride) (drug)]] (+0.80, unclear); [[Abiraterone acetate (drug)]] (+0.80, unclear); [[Drospirenone (drug)]] (+0.73, unclear); [[Oxaprozin (drug)]] (+0.71, Cyclooxygenase inhibitor); [[Ataluren (drug)]] (+0.68, unclear, ⚠ only 7 significant genes); [[Isocorydine (drug)]] (+0.67, unclear); [[Brimonidine (drug)]] (+0.63, Adrenoceptor agonist)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Vitamin K4"
- `tables/drugdoses.parquet` — dd in 1093, 1094, 1095
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
