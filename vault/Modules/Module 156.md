---
module: 156
type: "module"
n_genes: 28
n_plus: 28
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.33313891291618347
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 156

*28 genes (single-armed) · [[Module 156.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 155), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[TAK-901 (drug)]] 5 µM (+7.7, ⚠ cell-cycle shift); [[PH-797804 (drug)]] 5 µM (+5.8); [[Ouabain (Octahydrate) (drug)]] 5 µM (+4.9, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (+4.1, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 5 µM (+3.2, ⚠ toxic; transcription drop; cell-cycle shift); [[Ixazomib citrate (drug)]] 5 µM (+3.1, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 0.5 µM (+3.1, ⚠ cell-cycle shift); [[Bortezomib (drug)]] 0.05 µM (+3.0, ⚠ cell-cycle shift); [[Topotecan (hydrochloride) (drug)]] 5 µM (+1.8, ⚠ toxic; cell-cycle shift); [[Ixazomib citrate (drug)]] 0.5 µM (+1.7); [[Bortezomib (drug)]] 0.5 µM (+1.5); [[TAK-901 (drug)]] 0.05 µM (+1.3); [[TAK-733 (drug)]] 0.05 µM (+1.2); [[GSK1059615 (drug)]] 5 µM (+1.2); [[EX229 (drug)]] 5 µM (+1.2); [[Abemaciclib (drug)]] 0.5 µM (+1.0); [[Lactate (calcium) (drug)]] 0.5 µM (+1.0) (22 in all, 13 with an alert ⚠; shown: the 10 strongest and the 7 next strongest without an alert)
- Lower it: [[Dinaciclib (drug)]] 5 µM (-6.9, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (-6.9, ⚠ toxic; transcription drop; cell-cycle shift); [[Panobinostat (drug)]] 5 µM (-6.2, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (-5.7, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (-5.6, ⚠ toxic; transcription drop; cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (-5.1); [[Panobinostat (drug)]] 0.5 µM (-5.1, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (-4.7, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 0.5 µM (-3.6, ⚠ cell-cycle shift); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (-3.1, ⚠ cell-cycle shift); [[Brivudine (drug)]] 5 µM (-2.9); [[Ponatinib (drug)]] 5 µM (-1.6); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM (-1.3); [[Terfenadine (drug)]] 0.5 µM (-1.3); [[Radotinib (drug)]] 5 µM (-1.2); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM (-1.2); [[Trametinib (drug)]] 0.5 µM (-1.2); [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM (-1.1); [[Radotinib (drug)]] 0.5 µM (-1.1) (26 in all, 15 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[SW480 (line)]], [[PANC-1 (line)]], [[NCI-H23 (line)]], [[LoVo (line)]], [[NCI-H460 (line)]], [[A-427 (line)]], [[RKO (line)]], [[KATO III (line)]]

## + arm (28)

| Gene | Projection | Name |
|---|---|---|
| [[TFCP2]] | 0.821 | transcription factor CP2 |
| [[METTL16]] | 0.794 | methyltransferase 16, RNA N6-adenosine |
| [[TM9SF4]] | 0.792 | transmembrane 9 superfamily member 4 |
| [[QRICH1]] | 0.792 | glutamine rich 1 |
| [[ECSIT]] | 0.765 | ECSIT signaling integrator |
| [[FAF2]] | 0.735 | Fas associated factor family member 2 |
| [[AKAP8]] | 0.730 | A-kinase anchoring protein 8 |
| [[UBE2J2]] | 0.724 | ubiquitin conjugating enzyme E2 J2 |
| [[RPP14]] | 0.716 | ribonuclease P/MRP subunit p14 |
| [[NSUN4]] | 0.686 | NOP2/Sun RNA methyltransferase 4 |
| [[SDHAF2]] | 0.651 | succinate dehydrogenase complex assembly factor 2 |
| [[LRRC41]] | 0.637 | leucine rich repeat containing 41 |
| [[VPS51]] | 0.635 | VPS51 subunit of GARP complex |
| [[SDHC]] | 0.621 | succinate dehydrogenase complex subunit C |
| [[TMEM87A]] | 0.612 | transmembrane protein 87A |
| [[PTBP3]] | -0.610 | polypyrimidine tract binding protein 3 |
| [[GMEB1]] | 0.595 | glucocorticoid modulatory element binding protein 1 |
| [[TERF2]] | 0.594 | telomeric repeat binding factor 2 |
| [[ZNF263]] | 0.591 | zinc finger protein 263 |
| [[NMT1]] | 0.584 | N-myristoyltransferase 1 |
| [[ORC2]] | 0.575 | origin recognition complex subunit 2 |
| [[CMTM6]] | -0.572 | CKLF like MARVEL transmembrane domain containing 6 |
| [[ZNF41]] | 0.522 | zinc finger protein 41 |
| [[H3-3A]] | -0.518 | H3.3 histone A |
| [[MBTD1]] | 0.512 | mbt domain containing 1 |
| [[ZNF131]] | 0.492 | zinc finger and BTB domain containing 35 |
| [[SRP19]] | 0.414 | signal recognition particle 19 |
| [[DCTN5]] | 0.411 | dynactin subunit 5 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 156; `graph/modules.parquet` — module == 156; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [155] (drug-dose × line)
