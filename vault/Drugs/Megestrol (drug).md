---
drug: "Megestrol"
type: "drug"
salt_base: "Megestrol"
targets: ""
moa_fine: "unclear"
moa_broad: "unclear"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.05"
max_sig_genes: 574
tags: ["drug", "moa/unclear"]
generated_by: "tahoemap"
---

# Megestrol

*unclear (unclear) · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 574 / 18 / 32; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.20 / 0.40.
> Flags by dose: cell-cycle shift / - / -. ⚠ 0.05 µM: cell-cycle shift (artifact flags: its changes there are shown with an alert, not left out).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:B9 | 262 / 312 | — | +0.06 | +5.0/+4.5/+2.0 | ⚠ cell-cycle shift |
| 0.5 µM | [[Plate 05]]:B9 | 13 / 5 | — | -0.31 | +0.0/+0.4/+0.4 | — |
| 5 µM | [[Plate 14]]:B9 | 9 / 23 | 0.850 | +0.06 | +0.1/+0.4/-0.3 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (262 genes, 216 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 24 shown): [[DIAPH3]] ⚠ 1.27× (z +5.2, 25/45 lines; cell-cycle shift, explains ~78% of this change), [[KNL1]] ⚠ 1.34× (z +5.0, 26/47 lines; cell-cycle shift, explains ~86% of this change), [[KIF4A]] ⚠ 1.31× (z +4.8, 22/47 lines; cell-cycle shift, explains ~84% of this change), [[WDR76]] ⚠ 1.38× (z +4.7, 12/46 lines; cell-cycle shift, explains ~82% of this change), [[SGO1]] ⚠ 1.44× (z +4.7, 23/47 lines; cell-cycle shift, explains ~67% of this change), [[FBXO5]] ⚠ 1.44× (z +4.7, 21/47 lines; cell-cycle shift, explains ~76% of this change), [[NCAPH]] ⚠ 1.35× (z +4.7, 21/47 lines; cell-cycle shift, explains ~95% of this change), [[TMX3]] ⚠ 1.22× (z +4.6, 19/48 lines; cell-cycle shift, explains ~12% of this change), [[NCAPG]] ⚠ 1.35× (z +4.6, 25/47 lines; cell-cycle shift, explains ~91% of this change), [[SCLT1]] ⚠ 1.26× (z +4.6, 25/48 lines; cell-cycle shift, explains ~42% of this change), [[ERCC6L]] ⚠ 1.40× (z +4.5, 15/47 lines; cell-cycle shift, explains ~77% of this change), [[FAM111B]] ⚠ 1.68× (z +4.5, 19/38 lines; cell-cycle shift, explains ~86% of this change), [[MAP1B]] 1.24× (z +4.2, 17/32 lines; cell-cycle shift (explains ~0% here)), [[WWC3]] 1.28× (z +3.9, 16/44 lines; cell-cycle shift (explains ~6% here)), [[ENSG00000288828]] 1.63× (z +3.8, 5/15 lines; cell-cycle shift (explains ~0% here)), [[MID1]] 1.26× (z +3.7, 17/42 lines; cell-cycle shift (explains ~10% here)), [[F2R]] 1.40× (z +3.7, 12/36 lines; cell-cycle shift (explains ~7% here)), [[GDAP1]] 1.38× (z +3.6, 3/42 lines; cell-cycle shift (explains ~0% here)), [[ZRANB3]] 1.28× (z +3.6, 18/48 lines; cell-cycle shift (explains ~2% here)), [[CEP41]] 1.40× (z +3.6, 9/44 lines; cell-cycle shift (explains ~19% here)), [[TRMT5]] 1.30× (z +3.5, 9/48 lines; cell-cycle shift (explains ~12% here)), [[ENSG00000250899]] 1.50× (z +3.5, 1/38 lines; cell-cycle shift (explains ~10% here)), [[LINC00342]] 1.32× (z +3.5, 19/48 lines; cell-cycle shift (explains ~0% here)), [[NT5E]] 1.33× (z +3.5, 20/34 lines; cell-cycle shift (explains ~8% here))

**0.5 µM** (13 genes, none with an alert; 12 shown): [[ENSG00000238273]] 1.33× (z +3.7, 5/43 lines), [[FAM230C]] 1.29× (z +3.4, 1/17 lines), [[ENSG00000289418]] 1.89× (z +3.4, 3/9 lines), [[PLAC1]] 1.39× (z +3.4, 3/39 lines), [[ENSG00000288573]] 1.43× (z +3.4, 2/37 lines), [[ENSG00000280241]] 1.48× (z +3.2, 3/13 lines), [[FENDRR]] 1.57× (z +3.2, 0/8 lines), [[CCND3]] 1.26× (z +3.1, 13/47 lines), [[TBXAS1]] 1.27× (z +3.0, 5/37 lines), [[ENSG00000285845]] 1.34× (z +2.9, 1/17 lines), [[IRAK3]] 1.30× (z +2.9, 2/12 lines), [[HAVCR1]] 1.44× (z +2.8, 1/9 lines)

**5 µM** (9 genes, none with an alert): [[CCND3]] 1.38× (z +6.2, 25/47 lines), [[NNMT]] 1.48× (z +5.1, 14/24 lines), [[PID1]] 1.20× (z +3.5, 9/27 lines), [[ADPRHL1]] 1.22× (z +3.4, 9/48 lines), [[ENSG00000289418]] 1.54× (z +3.2, 7/10 lines), [[P2RX5]] 1.25× (z +3.0, 1/28 lines), [[LEF1-AS1]] 1.38× (z +3.0, 0/12 lines), [[SAA1]] 1.55× (z +2.8, 10/21 lines), [[SLC7A2]] 1.21× (z +2.8, 7/19 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (312 genes, 184 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 19 shown): [[FBXO42]] 0.677× (z -5.9, 41/48 lines; cell-cycle shift (explains ~17% here)), [[MINDY2]] ⚠ 0.744× (z -5.5, 40/48 lines; cell-cycle shift, explains ~25% of this change), [[LINC00598]] 0.724× (z -5.3, 21/43 lines; cell-cycle shift (explains ~20% here)), [[CNNM2]] 0.709× (z -5.3, 40/48 lines; cell-cycle shift (explains ~13% here)), [[ENSG00000284697]] 0.572× (z -5.3, 31/48 lines; cell-cycle shift (explains ~8% here)), [[CAB39L]] ⚠ 0.778× (z -5.3, 21/48 lines; cell-cycle shift, explains ~35% of this change), [[SRP54-AS1]] 0.635× (z -5.3, 36/48 lines; cell-cycle shift (explains ~11% here)), [[MIR34AHG]] ⚠ 0.654× (z -5.2, 21/33 lines; cell-cycle shift, explains ~39% of this change), [[ENSG00000257759]] ⚠ 0.694× (z -5.1, 30/47 lines; cell-cycle shift, explains ~32% of this change), [[PLAG1]] ⚠ 0.757× (z -5.0, 24/39 lines; cell-cycle shift, explains ~24% of this change), [[CBLB]] ⚠ 0.749× (z -4.8, 33/47 lines; cell-cycle shift, explains ~52% of this change), [[FOXO3]] ⚠ 0.770× (z -4.8, 32/48 lines; cell-cycle shift, explains ~22% of this change), [[DNAJC25]] 0.661× (z -4.7, 36/48 lines; cell-cycle shift (explains ~0% here)), [[ZNF14]] 0.690× (z -4.7, 21/45 lines; cell-cycle shift (explains ~0% here)), [[CRY2]] 0.702× (z -4.7, 27/48 lines; cell-cycle shift (explains ~0% here)), [[DGKE]] 0.767× (z -4.6, 12/36 lines; cell-cycle shift (explains ~0% here)), [[SLC15A2]] 0.623× (z -4.5, 22/46 lines; cell-cycle shift (explains ~22% here)), [[ADAM20]] 0.679× (z -4.5, 28/48 lines; cell-cycle shift (explains ~23% here)), [[RSRP1]] 0.788× (z -4.5, 30/48 lines; cell-cycle shift (explains ~10% here))

**0.5 µM** (5 genes, none with an alert): [[PER2]] 0.755× (z -3.9, 23/48 lines), [[MPP2]] 0.756× (z -3.7, 11/37 lines), [[PER3]] 0.805× (z -3.5, 17/45 lines), [[PPP1R14C]] 0.775× (z -3.5, 5/32 lines), [[GBP2]] 0.826× (z -2.8, 7/35 lines)

**5 µM** (23 genes, none with an alert; 12 shown): [[PER2]] 0.430× (z -16.5, 48/49 lines), [[PER3]] 0.530× (z -14.7, 37/45 lines), [[TEF]] 0.543× (z -11.7, 33/48 lines), [[NR6A1]] 0.700× (z -10.8, 42/47 lines), [[CRY1]] 0.489× (z -10.7, 45/49 lines), [[CRY2]] 0.639× (z -8.1, 41/48 lines), [[OSGIN1]] 0.675× (z -6.3, 25/45 lines), [[DBP]] 0.581× (z -5.8, 28/45 lines), [[MAPK8IP1]] 0.706× (z -5.6, 14/45 lines), [[MMRN2]] 0.694× (z -5.4, 17/35 lines), [[EIF5A2]] 0.820× (z -4.3, 23/45 lines), [[CIART]] 0.672× (z -4.2, 12/24 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 004]] (+3.1), [[Module 006]] (+2.7), [[Module 060]] (+2.7) | [[Module 207]] (-4.0), [[Module 179]] (-3.5), [[Module 041]] (-3.0) |
| 0.5 µM | — | — |
| 5 µM | — | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[SW 1088 (line)]] (1.99), [[HOP62 (line)]] (1.47), [[NCI-H1573 (line)]] (1.47), [[H4 (line)]] (1.34) · weakest: [[AN3 CA (line)]] (0.194), [[BT-474 (line)]] (0.415), [[NCI-H2347 (line)]] (0.487) |
| 0.5 µM | — | — |
| 5 µM | — | [[H4 (line)]] (1.98), [[NCI-H1792 (line)]] (1.58), [[A-172 (line)]] (1.56), [[SW 900 (line)]] (1.55) · weakest: [[NCI-H2122 (line)]] (0.354), [[NCI-H23 (line)]] (0.427), [[SNU-1 (line)]] (0.443) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: vector dose flagged: cell-cycle shift. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar.*

- [[Palmatine (chloride) (drug)]] (+0.95, unclear); [[Busulfan (drug)]] (+0.94, DNA synthesis/repair inhibitor); [[Retinoic acid (drug)]] (+0.94, Retinoic receptor agonist); [[Larotrectinib (drug)]] (+0.91, Other TK inhibitor); [[(R)-Verapamil (hydrochloride) (drug)]] (+0.91, unclear); [[Berbamine (drug)]] (+0.88, unclear); [[Diammonium Glycyrrhizinate (drug)]] (+0.83, unclear); [[Diphenhydramine (drug)]] (+0.81, unclear)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Megestrol"
- `tables/drugdoses.parquet` — dd in 663, 664, 665
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
