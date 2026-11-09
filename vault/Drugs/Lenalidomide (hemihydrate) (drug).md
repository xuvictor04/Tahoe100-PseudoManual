---
drug: "Lenalidomide (hemihydrate)"
type: "drug"
salt_base: "Lenalidomide"
targets: "CRBN, IKZF1, IKZF3"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 44
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Lenalidomide (hemihydrate)

*unclear (inhibitor/antagonist) · targets: CRBN, IKZF1, IKZF3 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 12 / 44 / 9; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): low dose only (noise?).
> Signature similarity between consecutive doses (low–mid / mid–high): 0.18 / 0.40.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:D10 | 9 / 3 | — | -0.46 | -0.4/-1.3/-0.2 | — |
| 0.5 µM | [[Plate 05]]:D10 | 21 / 23 | — | -0.51 | -0.2/-0.5/+1.0 | — |
| 5 µM | [[Plate 14]]:D10 | 6 / 3 | 0.800 | -0.22 | +0.2/-0.1/+0.9 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (9 genes, none with an alert): [[VPS33B]] 1.25× (z +3.7, 5/46 lines), [[ENSG00000249174]] 1.59× (z +3.5, 0/8 lines), [[MILR1]] 1.43× (z +3.4, 2/25 lines), [[ENSG00000242396]] 1.41× (z +3.2, 1/28 lines), [[RHCE]] 1.38× (z +3.2, 6/41 lines), [[RBM24]] 1.47× (z +3.1, 0/19 lines), [[ENSG00000233491]] 1.42× (z +3.0, 0/11 lines), [[LINC00457]] 1.42× (z +2.9, 3/11 lines), [[ENSG00000267698]] 1.22× (z +2.8, 7/45 lines)

**0.5 µM** (21 genes, none with an alert; 12 shown): [[ULK3]] 1.40× (z +4.4, 9/43 lines), [[C2orf76]] 1.22× (z +3.8, 6/46 lines), [[ATRIP]] 1.25× (z +3.7, 4/44 lines), [[TPPP]] 1.37× (z +3.6, 8/39 lines), [[ZNF639]] 1.21× (z +3.6, 13/47 lines), [[RTL10]] 1.27× (z +3.5, 9/46 lines), [[GORASP1]] 1.26× (z +3.4, 9/45 lines), [[BRPF1]] 1.28× (z +3.3, 5/47 lines), [[TRIM65]] 1.26× (z +3.3, 12/45 lines), [[DHRS1]] 1.33× (z +3.3, 9/42 lines), [[CHPF2]] 1.34× (z +3.3, 16/44 lines), [[DHODH]] 1.30× (z +3.3, 7/38 lines)

**5 µM** (6 genes, none with an alert): [[ENSG00000287351]] 1.27× (z +3.5, 7/44 lines), [[ENSG00000197670]] 1.23× (z +3.2, 4/45 lines), [[MED18]] 1.20× (z +3.1, 6/45 lines), [[CNGB3]] 1.21× (z +3.1, 6/46 lines), [[ITIH5]] 1.26× (z +3.0, 1/11 lines), [[YRDC]] 1.20× (z +2.9, 8/46 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (3 genes, none with an alert): [[C19orf38]] 0.679× (z -3.2, 7/42 lines), [[FOSB]] 0.508× (z -3.0, 33/48 lines), [[NR4A3]] 0.761× (z -2.7, 9/42 lines)

**0.5 µM** (23 genes, none with an alert; 12 shown): [[POLR2J3-1]] 0.606× (z -5.3, 22/39 lines), [[ENSG00000291228]] 0.668× (z -5.1, 23/45 lines), [[PRR3]] 0.718× (z -5.0, 17/46 lines), [[GTF2IP4]] 0.651× (z -5.0, 14/36 lines), [[BEST1]] 0.643× (z -4.3, 19/44 lines), [[ANO7]] 0.727× (z -3.7, 10/33 lines), [[LSP1P4]] 0.755× (z -3.6, 8/36 lines), [[TPM3]] 0.807× (z -3.5, 29/48 lines), [[KREMEN1]] 0.827× (z -3.4, 16/44 lines), [[FSCN2]] 0.542× (z -3.3, 19/37 lines), [[HAPLN3]] 0.763× (z -3.3, 14/36 lines), [[GPAM]] 0.807× (z -3.3, 12/46 lines)

**5 µM** (3 genes, none with an alert): [[ENSG00000253671]] 0.695× (z -3.5, 11/29 lines), [[HAL]] 0.776× (z -3.5, 8/38 lines), [[PCDHA6]] 0.805× (z -3.1, 6/30 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[Module 048]] (+2.1), [[Module 043]] (+2.1) | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | [[Panc 03.27 (line)]] (1.47), [[NCI-H2030 (line)]] (1.40), [[BT-474 (line)]] (1.32), [[CFPAC-1 (line)]] (1.31) · weakest: [[CHP-212 (line)]] (-0.0583), [[H4 (line)]] (0.296), [[HOP62 (line)]] (0.320) |
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Canagliflozin (drug)]] (+0.70, Glucose transporter inhibitor); [[9-ING-41 (drug)]] (+0.69, GSK3 inhibitor); [[Thymol (drug)]] (+0.66, unclear); [[LY-2584702 (tosylate salt) (drug)]] (+0.63, MTOR inhibitor, ⚠ vector dose flagged: toxic); [[BI-78D3 (drug)]] (+0.63, Other MAPK inhibitor); [[XRK3F2 (drug)]] (+0.62, unclear); [[Hydroxyurea (drug)]] (+0.62, DNA synthesis/repair inhibitor); [[Eplerenone (drug)]] (+0.61, unclear, ⚠ only 4 significant genes); [[Medroxyprogesterone acetate (drug)]] (+0.57, unclear); [[OTS514 (drug)]] (+0.57, Other MAPK inhibitor)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Lenalidomide (hemihydrate)"
- `tables/drugdoses.parquet` — dd in 612, 613, 614
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
