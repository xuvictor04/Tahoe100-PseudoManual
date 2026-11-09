---
drug: "Canagliflozin (hemihydrate)"
type: "drug"
salt_base: "Canagliflozin"
targets: "SLC5A2"
moa_fine: "Glucose transporter inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 670
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Canagliflozin (hemihydrate)

*Glucose transporter inhibitor (inhibitor/antagonist) · targets: SLC5A2 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 9 / 670 / 5; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): low dose only (noise?).
> Signature similarity between consecutive doses (low–mid / mid–high): 0.45 / 0.12.
> Flags by dose: - / low cells (technical?) / -.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:A3 | 7 / 2 | — | -0.09 | -0.3/-0.0/+1.0 | — |
| 0.5 µM | [[Plate 11]]:A3 | 642 / 28 | — | -1.15 | -0.0/-0.6/+1.0 | low cells (technical?) |
| 5 µM | [[Plate 12]]:A3 | 5 / 0 | — | +1.06 | -0.1/-0.6/-0.2 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (7 genes, none with an alert): [[SLIT1]] 1.30× (z +3.5, 3/38 lines), [[LINC01203]] 1.61× (z +3.3, 0/9 lines), [[UGT1A8]] 1.51× (z +3.2, 0/14 lines), [[ENSG00000290551]] 1.35× (z +3.2, 1/42 lines), [[ENPEP]] 1.34× (z +3.0, 0/20 lines), [[ENSG00000283982]] 1.34× (z +2.9, 0/17 lines), [[LINC01033]] 1.36× (z +2.9, 0/38 lines)

**0.5 µM** (642 genes, none with an alert; 12 shown): [[SULT4A1]] 2.10× (z +5.7, 2/9 lines), [[CPEB2-DT]] 1.81× (z +5.4, 5/21 lines), [[ENSG00000267581]] 1.56× (z +5.2, 5/24 lines), [[ENSG00000286058]] 1.85× (z +5.2, 4/15 lines), [[CCNYL2]] 1.51× (z +5.2, 5/15 lines), [[ENSG00000286026]] 1.96× (z +5.1, 2/14 lines), [[PTPN20]] 2.04× (z +5.0, 0/12 lines), [[ZNF229]] 1.45× (z +4.9, 3/21 lines), [[ZFHX4-AS1]] 1.81× (z +4.9, 1/6 lines), [[ENSG00000264660]] 2.27× (z +4.8, 2/9 lines), [[ADM2]] 1.69× (z +4.8, 7/24 lines), [[LINC01252]] 1.80× (z +4.7, 10/20 lines)

**5 µM** (5 genes, none with an alert): [[MX1]] 1.39× (z +3.5, 19/31 lines), [[ENSG00000283573]] 1.97× (z +3.2, 14/40 lines), [[NR4A3]] 1.38× (z +3.1, 13/44 lines), [[XAF1]] 1.42× (z +3.0, 12/34 lines), [[TAFA2]] 1.27× (z +2.8, 0/48 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (2 genes, none with an alert): [[CCDC15]] 0.830× (z -3.2, 8/46 lines), [[ANXA2R-OT1]] 0.821× (z -3.2, 6/46 lines)

**0.5 µM** (28 genes, none with an alert; 12 shown): [[MPP1]] 0.689× (z -5.2, 15/36 lines), [[OTULINL]] 0.692× (z -4.8, 9/30 lines), [[B3GNT2]] 0.779× (z -4.5, 17/45 lines), [[SMG1P1]] 0.622× (z -4.4, 22/41 lines), [[NFKBID]] 0.632× (z -4.3, 20/43 lines), [[CYB5D1]] 0.743× (z -4.1, 14/43 lines), [[ERI1]] 0.812× (z -4.0, 19/47 lines), [[ENSG00000289985]] 0.688× (z -3.9, 9/32 lines), [[GPC4]] 0.784× (z -3.8, 6/26 lines), [[ZW10]] 0.829× (z -3.8, 13/46 lines), [[CASP2]] 0.821× (z -3.7, 17/46 lines), [[ACTR5]] 0.733× (z -3.6, 18/44 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | [[Module 012]] (+2.3), [[Module 048]] (+2.2) | — |
| 5 µM | — | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | [[SW 1271 (line)]] (2.24), [[NCI-H661 (line)]] (2.03), [[CHP-212 (line)]] (1.67), [[HepG2_C3A (line)]] (1.44) · weakest: [[SW480 (line)]] (0.405), [[NCI-H460 (line)]] (0.410), [[PANC-1 (line)]] (0.462) |
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Nimesulide (drug)]] (+0.85, Cyclooxygenase inhibitor, ⚠ no trustworthy dose (vector dose flagged: toxic; unreliable plate only)); [[Methylprednisolone succinate (drug)]] (+0.77, Glucocorticoid receptor agonist); [[Drospirenone (drug)]] (+0.77, unclear); [[Oxaprozin (drug)]] (+0.76, Cyclooxygenase inhibitor); [[9-ING-41 (drug)]] (+0.76, GSK3 inhibitor); [[Bimatoprost (drug)]] (+0.76, unclear); [[Bicalutamide (drug)]] (+0.73, Androgen receptor antagonist); [[LY-2584702 (tosylate salt) (drug)]] (+0.73, MTOR inhibitor, ⚠ vector dose flagged: toxic); [[Pimozide (drug)]] (+0.72, unclear); [[Celecoxib (drug)]] (+0.72, Cyclooxygenase inhibitor)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Canagliflozin (hemihydrate)"
- `tables/drugdoses.parquet` — dd in 233, 234, 235
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
