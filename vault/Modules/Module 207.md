---
module: 207
type: "module"
n_genes: 15
n_plus: 8
n_minus: 7
arms_opposite: true
mean_cos_between_arms: -0.3641258180141449
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 207

*15 genes (8 in the + arm, 7 in the − arm) · [[Module 207.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.36). The + arm rises where the − arm falls. Arm = the side of the module's main direction a gene sits on.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of the + arm minus the − arm (`graph/module_pooled_z.npy`, row 206), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it (+ arm up, − arm down): [[Idarubicin (hydrochloride) (drug)]] 5 µM (+22.4, ⚠ cell-cycle shift); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (+6.9, ⚠ cell-cycle shift); [[Epirubicin (hydrochloride) (drug)]] 5 µM (+6.3, ⚠ cell-cycle shift); [[Selinexor (drug)]] 5 µM (+5.7, ⚠ cell-cycle shift); [[Selinexor (drug)]] 0.5 µM (+3.4, ⚠ cell-cycle shift); [[Topotecan (hydrochloride) (drug)]] 5 µM (+3.3, ⚠ toxic; cell-cycle shift); [[Abemaciclib (drug)]] 0.5 µM (+2.6); [[Bortezomib (drug)]] 0.05 µM (+2.4, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 0.5 µM (+2.4, ⚠ cell-cycle shift); [[Pravastatin (sodium) (drug)]] 5 µM (+2.3); [[Cloxacillin (sodium) (drug)]] 0.05 µM (+2.2); [[Fumaric acid (drug)]] 5 µM (+2.2); [[Niclosamide (olamine) (drug)]] 0.5 µM (+2.2); [[Triamcinolone (drug)]] 5 µM (+2.2); [[Entecavir (monohydrate) (drug)]] 0.5 µM (+2.1); [[Terfenadine (drug)]] 5 µM (+2.1); [[Piroxicam (drug)]] 0.05 µM (+2.1); [[Tirabrutinib (drug)]] 5 µM (+2.0) (114 in all, 18 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)
- Lower it: [[Tucidinostat (drug)]] 5 µM (-15.7); [[Tucidinostat (drug)]] 0.5 µM (-11.4, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (-11.0, ⚠ toxic; transcription drop; cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (-10.0, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-9.2, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (-8.5, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (-7.7, ⚠ toxic; transcription drop; cell-cycle shift); [[Belinostat (drug)]] 5 µM (-7.3, ⚠ cell-cycle shift); [[Belumosudil (drug)]] 5 µM (-7.0); [[Panobinostat (drug)]] 5 µM (-6.5, ⚠ cell-cycle shift); [[Auranofin (drug)]] 5 µM (-6.5); [[Brivudine (drug)]] 5 µM (-5.3); [[Temsirolimus (drug)]] 0.05 µM (-4.1); [[Retinoic acid (drug)]] 0.05 µM (-3.8); [[Palmatine (chloride) (drug)]] 0.05 µM (-3.4); [[Busulfan (drug)]] 0.05 µM (-3.3); [[Berbamine (drug)]] 0.05 µM (-3.2); [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM (-3.2) (158 in all, 31 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[SW1417 (line)]], [[HOP62 (line)]], [[CFPAC-1 (line)]], [[HT-29 (line)]], [[SW480 (line)]], [[COLO 205 (line)]], [[KATO III (line)]], [[PANC-1 (line)]]

## + arm (8)

| Gene | Projection | Name |
|---|---|---|
| [[GLE1]] | 0.855 | GLE1 RNA export mediator |
| [[PMS2P4-1]] | 0.837 | — |
| [[VDAC1P8]] | 0.762 | voltage dependent anion channel 1 pseudogene 8 |
| [[COG7]] | 0.740 | component of oligomeric golgi complex 7 |
| [[POMT1]] | 0.660 | protein O-mannosyltransferase 1 |
| [[PDSS2]] | 0.584 | decaprenyl diphosphate synthase subunit 2 |
| [[UQCRC2]] | 0.580 | ubiquinol-cytochrome c reductase core protein 2 |
| [[BLOC1S5-TXNDC5]] | 0.541 | BLOC1S5-TXNDC5 readthrough (NMD candidate) |

## − arm (7)

| Gene | Projection | Name |
|---|---|---|
| [[PCNX2]] | -0.792 | pecanex 2 |
| [[MPDZ]] | -0.689 | multiple PDZ domain crumbs cell polarity complex component |
| [[AIG1]] | -0.682 | androgen induced 1 |
| [[GALNT10]] | -0.647 | polypeptide N-acetylgalactosaminyltransferase 10 |
| [[CBX6]] | -0.629 | chromobox 6 |
| [[NBEA]] | -0.588 | neurobeachin |
| [[TTC28]] | -0.466 | tetratricopeptide repeat domain 28 |

## Data

- `graph/nodes.parquet` — module == 207; `graph/modules.parquet` — module == 207; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [206] (drug-dose × line)
