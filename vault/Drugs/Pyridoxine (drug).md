---
drug: "Pyridoxine"
type: "drug"
salt_base: "Pyridoxine"
targets: ""
moa_fine: "unclear"
moa_broad: "unclear"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 140
tags: ["drug", "moa/unclear"]
generated_by: "tahoemap"
---

# Pyridoxine

*unclear (unclear) · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 17 / 140 / 9; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): low dose only (noise?).
> Signature similarity between consecutive doses (low–mid / mid–high): 0.23 / -0.14.
> Flags by dose: - / low cells (technical?) / -.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:B6 | 13 / 4 | — | +0.07 | +0.4/+0.1/+0.7 | — |
| 0.5 µM | [[Plate 05]]:B6 | 139 / 1 | — | -1.08 | -2.2/-1.7/-0.3 | low cells (technical?) |
| 5 µM | [[Plate 14]]:B6 | 2 / 7 | 0.735 | -0.19 | -0.3/-0.0/-1.2 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (13 genes, none with an alert; 12 shown): [[ENSG00000251143]] 1.51× (z +3.7, 6/41 lines), [[FAM184B]] 1.31× (z +3.2, 1/44 lines), [[TMPRSS9]] 1.46× (z +3.2, 5/43 lines), [[HCLS1]] 1.46× (z +3.2, 6/44 lines), [[PRKCG]] 1.76× (z +3.1, 10/40 lines), [[MYOCOS]] 1.48× (z +3.0, 8/44 lines), [[ENSG00000267318]] 1.32× (z +3.0, 5/47 lines), [[SELPLG]] 1.61× (z +2.9, 3/36 lines), [[ENSG00000259536]] 1.31× (z +2.9, 3/43 lines), [[MTFR2]] 1.25× (z +2.9, 2/48 lines), [[FRZB]] 1.41× (z +2.8, 1/42 lines), [[CFAP210]] 1.66× (z +2.8, 10/43 lines)

**0.5 µM** (139 genes, none with an alert; 12 shown): [[HAGLR]] 1.54× (z +4.5, 1/18 lines), [[NCDN]] 1.45× (z +4.4, 11/42 lines), [[ZNF229]] 1.40× (z +4.4, 4/21 lines), [[UCKL1]] 1.43× (z +4.4, 21/45 lines), [[TTC36]] 1.72× (z +4.4, 6/21 lines), [[RNF44]] 1.42× (z +4.3, 25/45 lines), [[ENSG00000291189]] 1.61× (z +4.3, 1/12 lines), [[NSUN5P1]] 1.55× (z +4.3, 6/28 lines), [[PGBD4]] 1.40× (z +4.3, 3/28 lines), [[SMPDL3A]] 1.50× (z +4.2, 9/28 lines), [[ENSG00000288643]] 1.51× (z +4.2, 6/25 lines), [[UBE2D3-AS1]] 1.38× (z +4.1, 9/39 lines)

**5 µM** (2 genes, none with an alert): [[ENSG00000255330]] 1.31× (z +3.2, 2/27 lines), [[PTGIS]] 1.37× (z +3.2, 0/8 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (4 genes, none with an alert): [[ZNF232]] 0.780× (z -3.3, 6/44 lines), [[ATP2A3]] 0.745× (z -3.2, 5/29 lines), [[POMGNT2]] 0.807× (z -3.1, 4/45 lines), [[SPEG]] 0.772× (z -2.9, 7/31 lines)

**0.5 µM** (1 gene, none with an alert): [[ADORA2B]] 0.830× (z -3.0, 10/41 lines)

**5 µM** (7 genes, none with an alert): [[INPP5E]] 0.802× (z -4.2, 11/47 lines), [[ENSG00000262660]] 0.826× (z -3.7, 8/48 lines), [[C19orf25]] 0.828× (z -3.5, 15/48 lines), [[TM7SF2]] 0.788× (z -3.4, 7/45 lines), [[RFNG]] 0.762× (z -3.4, 16/45 lines), [[B4GALNT4]] 0.799× (z -3.3, 8/30 lines), [[DDX54]] 0.822× (z -3.3, 17/48 lines)

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
| 0.05 µM | — | — |
| 0.5 µM | — | [[SW 1271 (line)]] (2.45), [[SW 1088 (line)]] (1.79), [[NCI-H661 (line)]] (1.77), [[SW48 (line)]] (1.48) · weakest: [[NCI-H2347 (line)]] (0.259), [[HOP62 (line)]] (0.349), [[Panc 03.27 (line)]] (0.365) |
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Hydroxyurea (drug)]] (+0.83, DNA synthesis/repair inhibitor); [[LY-2584702 (tosylate salt) (drug)]] (+0.74, MTOR inhibitor, ⚠ vector dose flagged: toxic); [[Nimesulide (drug)]] (+0.72, Cyclooxygenase inhibitor, ⚠ no trustworthy dose (vector dose flagged: toxic; unreliable plate only)); [[XRK3F2 (drug)]] (+0.71, unclear); [[Thymol (drug)]] (+0.70, unclear); [[Canagliflozin (drug)]] (+0.70, Glucose transporter inhibitor); [[Canagliflozin (hemihydrate) (drug)]] (+0.69, Glucose transporter inhibitor); [[9-ING-41 (drug)]] (+0.65, GSK3 inhibitor); [[Drospirenone (drug)]] (+0.61, unclear); [[Ipatasertib (drug)]] (+0.59, PI3K/AKT inhibitor)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Pyridoxine"
- `tables/drugdoses.parquet` — dd in 848, 849, 850
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
