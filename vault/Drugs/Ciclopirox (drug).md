---
drug: "Ciclopirox"
type: "drug"
salt_base: "Ciclopirox"
targets: ""
moa_fine: "unclear"
moa_broad: "unclear"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 46
tags: ["drug", "moa/unclear"]
generated_by: "tahoemap"
---

# Ciclopirox

*unclear (unclear) · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 1 / 19 / 46; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.08 / 0.36.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:E5 | 1 / 0 | — | -0.15 | -0.3/-0.2/-0.5 | — |
| 0.5 µM | [[Plate 05]]:E5 | 0 / 19 | — | +0.45 | -0.6/-0.7/-1.9 | — |
| 5 µM | [[Plate 14]]:E5 | 4 / 42 | 0.647 | -0.43 | -1.1/-1.9/-1.4 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[AMZ1]] 1.26× (z +3.7, 4/44 lines)

**5 µM** (4 genes, none with an alert): [[TFRC]] 1.62× (z +7.5, 45/48 lines), [[PLD5]] 1.28× (z +3.5, 1/32 lines), [[TMEM132B]] 1.24× (z +3.4, 7/39 lines), [[ZNF66]] 1.20× (z +3.0, 2/35 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (19 genes, none with an alert; 12 shown): [[C9orf152]] 0.574× (z -4.1, 0/11 lines), [[ENSG00000290514]] 0.479× (z -4.0, 5/15 lines), [[NTRK3]] 0.582× (z -4.0, 0/13 lines), [[ENSG00000231772]] 0.594× (z -3.9, 1/20 lines), [[LINC01440]] 0.592× (z -3.8, 0/4 lines), [[MXRA8]] 0.601× (z -3.7, 0/12 lines), [[MEIOC]] 0.713× (z -3.7, 9/46 lines), [[ENSG00000266573]] 0.576× (z -3.7, 2/7 lines), [[TEX15]] 0.698× (z -3.5, 2/19 lines), [[HMOX1]] 0.699× (z -3.3, 5/38 lines), [[HCP5]] 0.749× (z -3.3, 0/24 lines), [[SPATA24]] 0.740× (z -3.3, 3/41 lines)

**5 µM** (42 genes, none with an alert; 12 shown): [[KNSTRN]] 0.780× (z -5.7, 21/48 lines), [[GCLM]] 0.778× (z -5.1, 29/46 lines), [[NOMO3]] 0.772× (z -4.5, 14/42 lines), [[USP18]] 0.738× (z -4.1, 25/44 lines), [[KATNB1]] 0.806× (z -4.0, 19/45 lines), [[FUCA2]] 0.819× (z -4.0, 20/45 lines), [[SOCS3]] 0.786× (z -3.9, 19/42 lines), [[AGMAT]] 0.705× (z -3.9, 8/20 lines), [[SAMHD1]] 0.804× (z -3.8, 24/45 lines), [[WNT3]] 0.757× (z -3.8, 8/37 lines), [[CMPK2]] 0.707× (z -3.8, 21/37 lines), [[VARS1]] 0.789× (z -3.8, 21/48 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | [[Module 059]] (-2.1) |
| 5 µM | [[Module 170]] (+2.2) | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | [[RKO (line)]] (1.47), [[RPMI-7951 (line)]] (1.41), [[SW 900 (line)]] (1.40), [[C-33 A (line)]] (1.40) · weakest: [[HT-29 (line)]] (0.229), [[HEC-1-A (line)]] (0.520), [[NCI-H2030 (line)]] (0.599) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 3 next most similar without an alert.*

- [[Trimetrexate (drug)]] (+0.72, DNA synthesis/repair inhibitor); [[Sulfisoxazole (drug)]] (+0.59, unclear); [[Ivabradine (hydrochloride) (drug)]] (+0.58, unclear, ⚠ no trustworthy dose (vector dose flagged: unreliable plate only)); [[18β-Glycyrrhetinic acid (drug)]] (+0.57, unclear); [[Plicamycin (drug)]] (+0.52, unclear, ⚠ only 3 significant genes; no trustworthy dose (vector dose flagged: unreliable plate only)); [[Fedratinib (hydrochloride hydrate) (drug)]] (+0.52, JAK/STAT inhibitor); [[Captopril (drug)]] (+0.51, unclear); [[Fostamatinib (disodium hexahydrate) (drug)]] (+0.50, Other TK inhibitor, ⚠ only 3 significant genes; no trustworthy dose (vector dose flagged: unreliable plate only)); [[Entecavir (monohydrate) (drug)]] (+0.50, unclear); [[Pasireotide (acetate) (drug)]] (+0.48, unclear); [[Verteporfin (drug)]] (+0.44, unclear)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Ciclopirox"
- `tables/drugdoses.parquet` — dd in 260, 261, 262
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
