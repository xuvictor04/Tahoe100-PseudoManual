---
module: 196
type: "module"
n_genes: 17
n_plus: 17
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 196

*17 genes (single-armed) · [[Module 196.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 195), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Dinaciclib (drug)]] 5 µM (+10.3, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (+8.0, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+6.8, ⚠ toxic; transcription drop; cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (+6.6, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (+6.0); [[Tucidinostat (drug)]] 0.5 µM (+3.7, ⚠ cell-cycle shift); [[Topotecan (hydrochloride) (drug)]] 5 µM (+3.1, ⚠ toxic; cell-cycle shift); [[AZD2858 (drug)]] 0.5 µM (+3.0, ⚠ toxic); [[Docetaxel (drug)]] 0.05 µM (+2.8, ⚠ transcription drop; cell-cycle shift); [[Niclosamide (olamine) (drug)]] 5 µM (+2.6, ⚠ toxic; cell-cycle shift); [[XRK3F2 (drug)]] 0.5 µM (+2.0); [[Ipatasertib (drug)]] 0.5 µM (+1.9); [[Bendamustine (drug)]] 5 µM (+1.8); [[Oxaprozin (drug)]] 0.5 µM (+1.8); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM (+1.7); [[Saquinavir (drug)]] 5 µM (+1.6); [[Pimozide (drug)]] 0.05 µM (+1.6); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+1.5); [[BAY1125976 (drug)]] 0.5 µM (+1.4) (72 in all, 22 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)
- Lower it: [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM (-2.7); [[Trametinib (drug)]] 5 µM (-2.6, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 0.5 µM (-2.5, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (-2.5, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (-2.4, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-1.9, ⚠ cell-cycle shift); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM (-1.8); [[Binimetinib (drug)]] 0.5 µM (-1.7); [[RMC-6236 (drug)]] 5 µM (-1.7); [[Clopidogrel (drug)]] 0.05 µM (-1.5); [[XRK3F2 (drug)]] 5 µM (-1.4); [[Neratinib (maleate) (drug)]] 5 µM (-1.4); [[Pravastatin (sodium) (drug)]] 5 µM (-1.4); [[Clopidogrel (drug)]] 0.5 µM (-1.4); [[Malotilate (drug)]] 5 µM (-1.4) (43 in all, 7 with an alert ⚠; shown: the 10 strongest and the 5 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[SHP-77 (line)]], [[SNU-1 (line)]], [[MIA PaCa-2 (line)]], [[BT-474 (line)]], [[Hs 766T (line)]], [[PANC-1 (line)]], [[SW480 (line)]], [[NCI-H460 (line)]]

## + arm (17)

| Gene | Projection | Name |
|---|---|---|
| [[IL19]] | 0.724 | interleukin 19 |
| [[MILR1]] | 0.723 | mast cell immunoglobulin like receptor 1 |
| [[LAPTM5]] | 0.683 | lysosomal protein transmembrane 5 |
| [[ANKRD20A1]] | 0.676 | ankyrin repeat domain 20 family member A1 |
| [[TMEM163]] | 0.667 | transmembrane protein 163 |
| [[CNTNAP3B]] | 0.664 | contactin associated protein family member 3B |
| [[CNTNAP3P2]] | 0.652 | CNTNAP3 pseudogene 2 |
| [[CNTNAP3]] | 0.630 | contactin associated protein family member 3 |
| [[CNTNAP3C]] | 0.628 | contactin associated protein family member 3C |
| [[CACNA2D4]] | 0.625 | calcium voltage-gated channel auxiliary subunit alpha2delta 4 |
| [[CCDC152]] | 0.615 | coiled-coil domain containing 152 |
| [[MIR4280HG]] | 0.561 | MIR4280 host gene |
| [[ANKRD29]] | 0.551 | ankyrin repeat domain 29 |
| [[RUBCNL]] | 0.541 | rubicon like autophagy enhancer |
| [[ANKRD20A4P]] | 0.532 | ankyrin repeat domain 20 family member A4, pseudogene |
| [[ADAMTS15]] | 0.469 | ADAM metallopeptidase with thrombospondin type 1 motif 15 |
| [[GPSM3]] | 0.467 | G protein signaling modulator 3 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 196; `graph/modules.parquet` — module == 196; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [195] (drug-dose × line)
