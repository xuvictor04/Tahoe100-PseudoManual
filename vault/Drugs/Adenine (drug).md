---
drug: "Adenine"
type: "drug"
salt_base: "Adenine"
targets: ""
moa_fine: "unclear"
moa_broad: "unclear"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 14
tags: ["drug", "moa/unclear"]
generated_by: "tahoemap"
---

# Adenine

*unclear (unclear) · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 0 / 1 / 14; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.05 / 0.10.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:H4 | 0 / 0 | — | +0.31 | -0.9/-0.7/-0.7 | — |
| 0.5 µM | [[Plate 05]]:H4 | 0 / 1 | — | +0.12 | -0.2/-0.3/+0.4 | — |
| 5 µM | [[Plate 14]]:H4 | 10 / 4 | 0.731 | +0.09 | +0.2/+0.3/-0.4 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**5 µM** (10 genes, none with an alert): [[PCLO]] 1.34× (z +6.6, 26/33 lines), [[RNF150]] 1.29× (z +4.8, 17/32 lines), [[GNG2]] 1.26× (z +4.7, 14/26 lines), [[SLC44A2]] 1.21× (z +4.3, 15/44 lines), [[ZNF441]] 1.22× (z +3.9, 7/41 lines), [[SLC16A9]] 1.21× (z +3.9, 5/29 lines), [[RYR2]] 1.25× (z +3.1, 5/48 lines), [[SH3TC1]] 1.20× (z +2.9, 4/38 lines), [[STK32A]] 1.21× (z +2.8, 3/25 lines), [[SNAI2]] 1.25× (z +2.8, 7/25 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (1 gene, none with an alert): [[TMPRSS5]] 0.765× (z -3.0, 7/44 lines)

**5 µM** (4 genes, none with an alert): [[SSU72]] 0.820× (z -5.3, 21/48 lines), [[FUT3]] 0.753× (z -4.4, 1/18 lines), [[ENSG00000262633]] 0.809× (z -3.4, 6/48 lines), [[GPC5]] 0.754× (z -3.4, 7/40 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[Module 025]] (+2.0) | [[Module 041]] (-2.1) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 3 next most similar without an alert.*

- [[Pyridoxine (hydrochloride) (drug)]] (+0.78, unclear); [[Folic acid (drug)]] (+0.75, unclear); [[Temuterkib (drug)]] (+0.69, Other MAPK inhibitor, ⚠ only 3 significant genes); [[Trifluridine (drug)]] (+0.65, DNA synthesis/repair inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Ferulic acid (drug)]] (+0.58, Other TK inhibitor); [[Clonidine (hydrochloride) (drug)]] (+0.58, Adrenoceptor agonist, ⚠ only 4 significant genes); [[Retinoic acid (drug)]] (+0.58, Retinoic receptor agonist); [[MK-8353 (drug)]] (+0.57, Other MAPK inhibitor); [[Pemetrexed (drug)]] (+0.56, DNA synthesis/repair inhibitor); [[Lopinavir (drug)]] (+0.55, unclear); [[Busulfan (drug)]] (+0.53, DNA synthesis/repair inhibitor)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Adenine"
- `tables/drugdoses.parquet` — dd in 57, 58, 59
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
