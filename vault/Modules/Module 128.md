---
module: 128
type: "module"
n_genes: 37
n_plus: 37
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 128

*37 genes (single-armed) · [[Module 128.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 127), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Dinaciclib (drug)]] 5 µM (+9.4, ⚠ toxic; transcription drop; cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (+8.3, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (+7.2, ⚠ toxic; transcription drop; cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (+7.1); [[Dinaciclib (drug)]] 0.05 µM (+6.2, ⚠ toxic; transcription drop; cell-cycle shift); [[Tucidinostat (drug)]] 0.5 µM (+5.2, ⚠ cell-cycle shift); [[Ipatasertib (drug)]] 0.5 µM (+2.4); [[Docetaxel (drug)]] 0.05 µM (+2.4, ⚠ transcription drop; cell-cycle shift); [[XRK3F2 (drug)]] 0.5 µM (+2.3); [[AZD2858 (drug)]] 0.5 µM (+2.3, ⚠ toxic); [[Auranofin (drug)]] 5 µM (+2.3); [[Thymol (drug)]] 0.5 µM (+2.0); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM (+1.8); [[Tucidinostat (drug)]] 0.05 µM (+1.6); [[Ponatinib (drug)]] 0.5 µM (+1.6); [[Temsirolimus (drug)]] 0.5 µM (+1.4); [[Celecoxib (drug)]] 0.5 µM (+1.4) (55 in all, 20 with an alert ⚠; shown: the 10 strongest and the 7 next strongest without an alert)
- Lower it: [[Digitoxin (drug)]] 0.5 µM (-5.1, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (-5.0, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-3.5, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (-3.4, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (-3.2, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 0.05 µM (-3.0, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 0.05 µM (-2.6, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-2.4, ⚠ cell-cycle shift); [[c-Kit-IN-1 (drug)]] 0.05 µM (-2.3, ⚠ unreliable plate only); [[TAK-901 (drug)]] 5 µM (-2.0, ⚠ cell-cycle shift); [[Abemaciclib (drug)]] 5 µM (-1.7); [[PH-797804 (drug)]] 5 µM (-1.6); [[Ixazomib citrate (drug)]] 0.5 µM (-1.6); [[Abemaciclib (drug)]] 0.5 µM (-1.6); [[Artesunate (drug)]] 0.5 µM (-1.5); [[Mebendazole (drug)]] 5 µM (-1.5); [[Erlotinib (drug)]] 0.05 µM (-1.5); [[Clopidogrel (drug)]] 0.05 µM (-1.4); [[Fenofibrate (drug)]] 0.05 µM (-1.4); [[Anethole trithione (drug)]] 0.5 µM (-1.4) (36 in all, 12 with an alert ⚠; shown: the 10 strongest and the 10 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[C-33 A (line)]], [[NCI-H23 (line)]], [[AsPC-1 (line)]], [[hTERT-HPNE (line)]], [[RKO (line)]], [[KATO III (line)]], [[MIA PaCa-2 (line)]], [[SNU-1 (line)]]

## + arm (37)

| Gene | Projection | Name |
|---|---|---|
| [[JPH3]] | 0.832 | junctophilin 3 |
| [[LRRC36]] | 0.757 | leucine rich repeat containing 36 |
| [[CYS1]] | 0.746 | cystin 1 |
| [[CACNA1B]] | 0.743 | calcium voltage-gated channel subunit alpha1 B |
| [[ELFN1]] | 0.733 | extracellular leucine rich repeat and fibronectin type III domain containing 1 |
| [[RFPL1S]] | 0.733 | RFPL1 antisense RNA 1 |
| [[RASGEF1A]] | 0.722 | RasGEF domain family member 1A |
| [[PALM]] | 0.710 | paralemmin |
| [[CHD5]] | 0.704 | chromodomain helicase DNA binding protein 5 |
| [[ADGRB1]] | 0.700 | adhesion G protein-coupled receptor B1 |
| [[TBX1]] | 0.690 | T-box transcription factor 1 |
| [[KCNQ2]] | 0.685 | potassium voltage-gated channel subfamily Q member 2 |
| [[MYT1]] | 0.666 | myelin transcription factor 1 |
| [[LINC02643]] | 0.664 | long independently transcribed non-coding RNA 2643 |
| [[LRRC4B]] | 0.657 | leucine rich repeat containing 4B |
| [[PRRX2]] | 0.647 | paired related homeobox 2 |
| [[PAX2]] | 0.644 | paired box 2 |
| [[CECR2]] | 0.642 | CECR2 histone acetyl-lysine reader |
| [[NR5A2]] | 0.613 | nuclear receptor subfamily 5 group A member 2 |
| [[FBXO27]] | 0.605 | F-box protein 27 |
| [[CBFA2T3]] | 0.598 | CBFA2/RUNX1 partner transcriptional co-repressor 3 |
| [[LAMC3]] | 0.575 | laminin subunit gamma 3 |
| [[SLC6A11]] | 0.562 | solute carrier family 6 member 11 |
| [[GCG]] | 0.555 | glucagon |
| [[DLK2]] | 0.545 | delta like non-canonical Notch ligand 2 |
| [[EPHA10]] | 0.544 | EPH receptor A10 |
| [[TCF7L1]] | 0.542 | transcription factor 7 like 1 |
| [[SRCIN1]] | 0.541 | SRC kinase signaling inhibitor 1 |
| [[ARHGEF25]] | 0.530 | Rho guanine nucleotide exchange factor 25 |
| [[ADAMTS10]] | 0.525 | ADAM metallopeptidase with thrombospondin type 1 motif 10 |
| [[RNF212]] | 0.510 | ring finger protein 212 |
| [[BOLA3-DT]] | 0.499 | BOLA3 divergent transcript |
| [[C3orf18]] | 0.496 | chromosome 3 open reading frame 18 |
| [[SEC14L4]] | 0.491 | SEC14 like lipid binding 4 |
| [[RNF220]] | 0.462 | ring finger protein 220 |
| [[SYT17]] | 0.398 | synaptotagmin 17 |
| [[ST6GALNAC2]] | 0.270 | ST6 N-acetylgalactosaminide alpha-2,6-sialyltransferase 2 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 128; `graph/modules.parquet` — module == 128; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [127] (drug-dose × line)
