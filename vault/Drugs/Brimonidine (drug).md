---
drug: "Brimonidine"
type: "drug"
salt_base: "Brimonidine"
targets: "ADRA2A, ADRA2B, ADRA2C"
moa_fine: "Adrenoceptor agonist"
moa_broad: "activator/agonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 94
tags: ["drug", "moa/activator_agonist"]
generated_by: "tahoemap"
---

# Brimonidine

*Adrenoceptor agonist (activator/agonist) · targets: ADRA2A, ADRA2B, ADRA2C · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 0 / 17 / 94; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.15 / 0.16.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:A4 | 0 / 0 | — | +0.49 | -0.0/-0.1/-0.4 | — |
| 0.5 µM | [[Plate 11]]:A4 | 12 / 5 | — | -0.45 | +0.6/+0.5/+0.9 | — |
| 5 µM | [[Plate 12]]:A4 | 85 / 9 | — | +0.67 | +1.4/-0.4/-1.2 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (12 genes, none with an alert): [[BTBD16]] 1.46× (z +3.8, 3/31 lines), [[ENSG00000255292]] 1.33× (z +3.8, 11/44 lines), [[ENSG00000267699]] 1.43× (z +3.6, 4/36 lines), [[COP1-DT]] 1.41× (z +3.4, 3/29 lines), [[ENSG00000272688]] 1.40× (z +3.4, 1/24 lines), [[GALNT9]] 1.51× (z +3.3, 1/20 lines), [[GASK1B-AS1]] 1.60× (z +3.2, 3/11 lines), [[POP1]] 1.23× (z +3.2, 2/45 lines), [[CCNJ]] 1.22× (z +3.2, 6/45 lines), [[PPP1R3B-DT]] 1.31× (z +3.1, 2/36 lines), [[CFAP58]] 1.33× (z +3.0, 1/28 lines), [[STK32A]] 1.33× (z +3.0, 1/23 lines)

**5 µM** (85 genes, none with an alert; 12 shown): [[ZRANB3]] 1.32× (z +4.0, 26/48 lines), [[ZNF337]] 1.25× (z +3.9, 20/48 lines), [[DNAH11]] 1.31× (z +3.9, 9/25 lines), [[FAM111B]] 1.54× (z +3.7, 12/38 lines), [[KIF26B]] 1.26× (z +3.7, 10/38 lines), [[ENSG00000285733]] 1.64× (z +3.6, 2/42 lines), [[PCDH7]] 1.38× (z +3.6, 13/30 lines), [[NPIPB14P]] 1.27× (z +3.6, 10/48 lines), [[THADA]] 1.33× (z +3.6, 29/47 lines), [[BICD1]] 1.27× (z +3.5, 24/47 lines), [[ZDHHC14]] 1.35× (z +3.5, 17/45 lines), [[CA3]] 1.38× (z +3.5, 11/37 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (5 genes, none with an alert): [[ENSG00000283765]] 0.670× (z -3.5, 16/40 lines), [[SEC14L2]] 0.819× (z -3.4, 9/47 lines), [[POLR2J3-1]] 0.738× (z -3.2, 19/43 lines), [[SLC25A27]] 0.825× (z -2.8, 11/39 lines), [[TNS1]] 0.813× (z -2.8, 6/25 lines)

**5 µM** (9 genes, none with an alert): [[YOD1]] 0.773× (z -3.8, 16/47 lines), [[TOM1]] 0.802× (z -3.6, 10/48 lines), [[MAX]] 0.811× (z -3.5, 22/48 lines), [[CRY2]] 0.768× (z -3.5, 12/48 lines), [[GNPTG]] 0.820× (z -3.4, 7/48 lines), [[NR1D1]] 0.710× (z -3.1, 19/46 lines), [[PER1]] 0.687× (z -3.0, 27/47 lines), [[WDR45B]] 0.776× (z -2.9, 28/48 lines), [[TMEM185A]] 0.824× (z -2.8, 3/48 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[Module 137]] (+2.4), [[Module 088]] (+2.3), [[Module 124]] (+2.3) | [[Module 207]] (-2.5), [[Module 168]] (-2.4), [[Module 041]] (-2.3) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | [[CHP-212 (line)]] (1.31), [[MIA PaCa-2 (line)]] (1.28), [[A498 (line)]] (1.25), [[NCI-H1792 (line)]] (1.21) · weakest: [[NCI-H661 (line)]] (0.270), [[SHP-77 (line)]] (0.544), [[SW 1088 (line)]] (0.587) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[Finasteride (drug)]] (+0.86, unclear); [[Esmolol (hydrochloride) (drug)]] (+0.83, unclear); [[Abiraterone acetate (drug)]] (+0.80, unclear); [[Acetohexamide (drug)]] (+0.76, unclear); [[Olanzapine (drug)]] (+0.75, unclear, ⚠ only 5 significant genes); [[Busulfan (drug)]] (+0.74, DNA synthesis/repair inhibitor); [[Meloxicam (drug)]] (+0.74, Cyclooxygenase inhibitor); [[Demeclocycline (drug)]] (+0.73, unclear); [[Diphenhydramine (drug)]] (+0.72, unclear)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Brimonidine"
- `tables/drugdoses.parquet` — dd in 212, 213, 214
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
