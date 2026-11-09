---
drug: "Benztropine (mesylate)"
type: "drug"
salt_base: "Benztropine"
targets: ""
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.05"
max_sig_genes: 208
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Benztropine (mesylate)

*unclear (inhibitor/antagonist) · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 208 / 19 / 0; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): low dose only (noise?).
> Signature similarity between consecutive doses (low–mid / mid–high): 0.51 / 0.20.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:B1 | 196 / 12 | — | +0.03 | -1.0/-2.1/-1.1 | — |
| 0.5 µM | [[Plate 11]]:B1 | 10 / 9 | — | +0.36 | -1.2/-1.7/-1.8 | — |
| 5 µM | [[Plate 12]]:B1 | 0 / 0 | — | -0.07 | -0.8/-0.7/-0.5 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (196 genes, none with an alert; 12 shown): [[PCLO]] 1.44× (z +4.9, 21/33 lines), [[MED12L]] 1.34× (z +4.4, 5/29 lines), [[NLRC5]] 1.38× (z +4.2, 19/43 lines), [[LINC01505]] 1.32× (z +4.2, 17/42 lines), [[CCSER1]] 1.29× (z +4.2, 16/28 lines), [[LINC00992]] 1.66× (z +4.1, 1/15 lines), [[ACVR1C]] 1.37× (z +4.1, 4/42 lines), [[LRP1B]] 1.38× (z +4.1, 11/23 lines), [[STAT4]] 1.41× (z +4.0, 7/37 lines), [[EML5]] 1.33× (z +4.0, 11/29 lines), [[CACNG8]] 1.48× (z +4.0, 19/33 lines), [[ENSG00000242021]] 1.36× (z +3.9, 7/18 lines)

**0.5 µM** (10 genes, none with an alert): [[EML5]] 1.30× (z +3.8, 7/29 lines), [[TMEM117]] 1.36× (z +3.6, 24/45 lines), [[TRMT61B]] 1.24× (z +3.4, 7/48 lines), [[ZNF253]] 1.30× (z +3.1, 2/43 lines), [[ACTR3C]] 1.31× (z +2.9, 7/33 lines), [[FGF2]] 1.22× (z +2.9, 4/32 lines), [[NUP50-DT]] 1.22× (z +2.9, 12/47 lines), [[L3MBTL4]] 1.20× (z +2.9, 9/22 lines), [[ENSG00000286415]] 1.33× (z +2.8, 5/45 lines), [[PRMT3]] 1.23× (z +2.8, 9/46 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (12 genes, none with an alert): [[RAVER1]] 0.815× (z -3.3, 10/48 lines), [[ZNF335]] 0.796× (z -3.3, 16/48 lines), [[ITGA5]] 0.795× (z -3.1, 17/37 lines), [[DDX41]] 0.798× (z -3.1, 11/48 lines), [[SEC13]] 0.831× (z -3.0, 15/48 lines), [[INSIG2]] 0.817× (z -2.9, 22/48 lines), [[ANLN]] 0.812× (z -2.9, 14/46 lines), [[WDR45B]] 0.779× (z -2.9, 30/48 lines), [[NCAPH]] 0.832× (z -2.8, 7/47 lines), [[SLC2A1]] 0.832× (z -2.8, 11/44 lines), [[PRC1]] 0.825× (z -2.8, 15/48 lines), [[EFNA3]] 0.784× (z -2.7, 7/46 lines)

**0.5 µM** (9 genes, none with an alert): [[CD200R1]] 0.595× (z -3.6, 10/42 lines), [[TMEM45B]] 0.734× (z -3.5, 0/16 lines), [[ENSG00000261058]] 0.657× (z -3.4, 10/39 lines), [[GRHL2]] 0.799× (z -3.3, 0/14 lines), [[SERPINB5]] 0.745× (z -3.2, 0/14 lines), [[LINC02864]] 0.788× (z -3.1, 0/12 lines), [[CLDN7]] 0.759× (z -3.1, 0/18 lines), [[ENSG00000236255]] 0.787× (z -3.1, 7/48 lines), [[FLT1]] 0.740× (z -3.0, 0/18 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 137]] (+2.8) | [[Module 207]] (-2.2) |
| 0.5 µM | [[Module 194]] (+2.3), [[Module 137]] (+2.1), [[Module 230]] (+2.0) | [[Module 059]] (-2.3) |
| 5 µM | — | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[SW 1088 (line)]] (1.41), [[LOX-IMVI (line)]] (1.19), [[SNU-423 (line)]] (1.18), [[H4 (line)]] (1.11) · weakest: [[KATO III (line)]] (0.499), [[SW480 (line)]] (0.553), [[LoVo (line)]] (0.573) |
| 0.5 µM | — | — |
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Vitamin K4 (drug)]] (+0.92, unclear); [[Abiraterone acetate (drug)]] (+0.85, unclear); [[Meloxicam (drug)]] (+0.84, Cyclooxygenase inhibitor); [[Bestatin (hydrochloride) (drug)]] (+0.76, unclear); [[Vismodegib (drug)]] (+0.73, Sonic inhibitor, ⚠ only 5 significant genes); [[Ataluren (drug)]] (+0.71, unclear, ⚠ only 7 significant genes); [[Brimonidine (drug)]] (+0.70, Adrenoceptor agonist); [[Oxaprozin (drug)]] (+0.65, Cyclooxygenase inhibitor); [[Finasteride (drug)]] (+0.64, unclear); [[Lidocaine (hydrochloride) (drug)]] (+0.63, unclear)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Benztropine (mesylate)"
- `tables/drugdoses.parquet` — dd in 164, 165, 166
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
