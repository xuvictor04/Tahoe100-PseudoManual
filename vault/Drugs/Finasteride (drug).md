---
drug: "Finasteride"
type: "drug"
salt_base: "Finasteride"
targets: "SRD5A2"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 21
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Finasteride

*unclear (inhibitor/antagonist) · targets: SRD5A2 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 3 / 0 / 21; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.18 / 0.46.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:D5 | 2 / 1 | — | -0.32 | -1.1/-0.8/-0.1 | — |
| 0.5 µM | [[Plate 08]]:D5 | 0 / 0 | — | -0.29 | -0.3/-0.6/+0.2 | — |
| 5 µM | [[Plate 09]]:D5 | 20 / 1 | — | -0.06 | -0.0/-0.3/-0.9 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (2 genes, none with an alert): [[LINC02646]] 1.49× (z +2.9, 12/43 lines), [[TOR3A]] 1.24× (z +2.8, 3/45 lines)

**5 µM** (20 genes, none with an alert; 12 shown): [[GSAP]] 1.28× (z +3.5, 13/42 lines), [[CLYBL]] 1.28× (z +3.4, 12/45 lines), [[ENSG00000266302]] 1.32× (z +3.4, 0/16 lines), [[GLDN]] 1.47× (z +3.4, 3/22 lines), [[ENSG00000287925]] 1.61× (z +3.3, 3/36 lines), [[TPK1]] 1.27× (z +3.3, 12/44 lines), [[EEF1AKMT1]] 1.25× (z +3.2, 7/46 lines), [[MIPOL1]] 1.22× (z +3.2, 13/40 lines), [[ZNF876P]] 1.39× (z +3.1, 2/29 lines), [[ZNF382]] 1.32× (z +3.0, 4/27 lines), [[OR51B5]] 1.25× (z +3.0, 7/30 lines), [[ENSG00000243176]] 1.38× (z +3.0, 3/45 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[ENSG00000225032]] 0.666× (z -3.6, 12/37 lines)

**5 µM** (1 gene, none with an alert): [[FTH1]] 0.675× (z -3.9, 42/44 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | [[Module 045]] (-2.1) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | [[Hs 766T (line)]] (1.29), [[RPMI-7951 (line)]] (1.22), [[HOP62 (line)]] (1.20), [[SW48 (line)]] (1.18) · weakest: [[NCI-H1573 (line)]] (0.185), [[RKO (line)]] (0.260), [[A-172 (line)]] (0.276) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[Brimonidine (drug)]] (+0.86, Adrenoceptor agonist); [[Esmolol (hydrochloride) (drug)]] (+0.81, unclear); [[Demeclocycline (drug)]] (+0.77, unclear); [[Acetohexamide (drug)]] (+0.75, unclear); [[Busulfan (drug)]] (+0.75, DNA synthesis/repair inhibitor); [[Olanzapine (drug)]] (+0.75, unclear, ⚠ only 5 significant genes); [[Dapagliflozin (drug)]] (+0.74, Glucose transporter inhibitor); [[Diphenhydramine (drug)]] (+0.72, unclear); [[Abiraterone acetate (drug)]] (+0.72, unclear)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Finasteride"
- `tables/drugdoses.parquet` — dd in 450, 451, 452
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
