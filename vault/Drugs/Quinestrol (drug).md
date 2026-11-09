---
drug: "Quinestrol"
type: "drug"
salt_base: "Quinestrol"
targets: ""
moa_fine: "unclear"
moa_broad: "unclear"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 30
tags: ["drug", "moa/unclear"]
generated_by: "tahoemap"
---

# Quinestrol

*unclear (unclear) · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 0 / 3 / 30; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.50 / 0.34.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:C2 | 0 / 0 | — | +0.65 | -0.3/-0.2/-0.6 | — |
| 0.5 µM | [[Plate 05]]:C2 | 0 / 3 | — | +0.70 | +0.3/+0.1/-0.4 | — |
| 5 µM | [[Plate 14]]:C2 | 2 / 28 | 0.846 | +0.35 | +0.7/+0.4/-0.4 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**5 µM** (2 genes, none with an alert): [[CCND3]] 1.28× (z +4.7, 24/47 lines), [[SNED1-AS1]] 1.23× (z +3.6, 4/45 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (3 genes, none with an alert): [[ENSG00000256966]] 0.698× (z -3.7, 12/44 lines), [[RPL23AP82]] 0.573× (z -3.6, 12/40 lines), [[ELAVL2]] 0.763× (z -3.3, 1/14 lines)

**5 µM** (28 genes, none with an alert; 12 shown): [[MSMO1]] 0.694× (z -5.6, 33/48 lines), [[INSIG1]] 0.698× (z -5.1, 34/48 lines), [[IDI1]] 0.768× (z -5.0, 26/49 lines), [[SCD]] 0.785× (z -4.9, 33/49 lines), [[FDFT1]] 0.788× (z -4.7, 28/48 lines), [[TFPI2]] 0.672× (z -4.7, 21/27 lines), [[HMGCR]] 0.802× (z -4.5, 26/49 lines), [[SQLE]] 0.760× (z -4.4, 27/48 lines), [[CYP51A1]] 0.824× (z -4.3, 25/48 lines), [[TMPRSS3]] 0.717× (z -4.3, 4/19 lines), [[ACAT2]] 0.832× (z -4.0, 16/48 lines), [[IGFN1]] 0.715× (z -4.0, 4/12 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | [[Module 086]] (-2.5) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | [[KATO III (line)]] (1.96), [[C32 (line)]] (1.85), [[NCI-H1792 (line)]] (1.56), [[CFPAC-1 (line)]] (1.56) · weakest: [[NCI-H2122 (line)]] (0.192), [[MIA PaCa-2 (line)]] (0.537), [[SHP-77 (line)]] (0.625) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Dexamethasone (drug)]] (+0.66, Glucocorticoid receptor agonist); [[Phenylephrine (hydrochloride) (drug)]] (+0.63, Adrenoceptor agonist); [[Econazole (drug)]] (+0.62, unclear); [[Budesonide (drug)]] (+0.53, Glucocorticoid receptor agonist); [[Verapamil (drug)]] (+0.48, unclear, ⚠ only 5 significant genes); [[Betamethasone dipropionate (drug)]] (+0.47, Glucocorticoid receptor agonist); [[Citalopram (hydrobromide) (drug)]] (+0.45, unclear); [[LB-100 (drug)]] (+0.45, unclear, ⚠ only 5 significant genes); [[Tirabrutinib (hydrochloride) (drug)]] (+0.43, Other TK inhibitor); [[Rutin (trihydrate) (drug)]] (+0.43, unclear)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Quinestrol"
- `tables/drugdoses.parquet` — dd in 854, 855, 856
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
