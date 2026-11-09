---
module: 69
type: "module"
n_genes: 71
n_plus: 71
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.33010679483413696
label: "FOXO-mediated transcription"
label_source: "reactome"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 069

*FOXO-mediated transcription · 71 genes (single-armed) · [[Module 069.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

Label from the validation stage: **FOXO-mediated transcription** (reactome, q 0.048; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | FOXO-mediated transcription | reactome | 4/71 | 15.2 | 0.048 |
| + | FOXO-mediated transcription | reactome | 4/71 | 15.2 | 0.048 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 68), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Homoharringtonine (drug)]] 5 µM (+7.5, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (+5.6, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (+5.1, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 5 µM (+3.0, ⚠ toxic; transcription drop; cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (+2.6, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (+2.4, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 0.5 µM (+2.3, ⚠ cell-cycle shift); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (+2.2, ⚠ cell-cycle shift); [[GSK1059615 (drug)]] 5 µM (+1.9); [[Homoharringtonine (drug)]] 0.5 µM (+1.9, ⚠ cell-cycle shift); [[Bimiralisib (drug)]] 5 µM (+1.9); [[PH-797804 (drug)]] 5 µM (+1.9); [[Terfenadine (drug)]] 5 µM (+1.5); [[Sapanisertib (drug)]] 5 µM (+1.5); [[Temsirolimus (drug)]] 0.5 µM (+1.4); [[AZD-8055 (drug)]] 0.5 µM (+1.4); [[Temsirolimus (drug)]] 5 µM (+1.3); [[ULK-101 (drug)]] 0.05 µM (+1.3); [[crizotinib (drug)]] 5 µM (+1.2) (42 in all, 21 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)
- Lower it: [[c-Kit-IN-1 (drug)]] 0.05 µM (-13.7, ⚠ unreliable plate only); [[TAK-733 (drug)]] 5 µM (-7.1); [[EX229 (drug)]] 5 µM (-6.5); [[Abemaciclib (drug)]] 5 µM (-6.4); [[c-Kit-IN-1 (drug)]] 5 µM (-6.2); [[venetoclax (drug)]] 5 µM (-5.5); [[Dinaciclib (drug)]] 5 µM (-5.3, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (-5.1, ⚠ toxic; transcription drop; cell-cycle shift); [[Abemaciclib (drug)]] 0.5 µM (-4.0); [[EX229 (drug)]] 0.5 µM (-3.4); [[EX229 (drug)]] 0.05 µM (-3.3); [[Belzutifan (drug)]] 5 µM (-3.2); [[Sapanisertib (drug)]] 0.5 µM (-2.9) (48 in all, 11 with an alert ⚠; shown: the 10 strongest and the 3 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[SW1417 (line)]], [[NCI-H460 (line)]], [[MIA PaCa-2 (line)]], [[LoVo (line)]], [[NCI-H2347 (line)]], [[AsPC-1 (line)]], [[SW480 (line)]], [[HEC-1-A (line)]]

## + arm (71)

| Gene | Projection | Name |
|---|---|---|
| [[CREBRF]] | 0.904 | CREB3 regulatory factor |
| [[KLHL24]] | 0.901 | kelch like family member 24 |
| [[HBP1]] | 0.877 | HMG-box transcription factor 1 |
| [[UBXN7]] | 0.853 | UBX domain protein 7 |
| [[TCP11L2]] | 0.839 | t-complex 11 like 2 |
| [[ATOSA]] | 0.807 | atos homolog A |
| [[PIK3CA]] | 0.807 | phosphatidylinositol-4,5-bisphosphate 3-kinase catalytic subunit alpha |
| [[JMY]] | 0.797 | junction mediating and regulatory protein, p53 cofactor |
| [[RB1CC1]] | 0.790 | RB1 inducible coiled-coil 1 |
| [[SERINC1]] | 0.781 | serine incorporator 1 |
| [[YPEL5]] | 0.777 | yippee like 5 |
| [[TMEM59]] | 0.768 | transmembrane protein 59 |
| [[ELF2]] | 0.766 | E74 like ETS transcription factor 2 |
| [[TXNDC16]] | 0.751 | thioredoxin domain containing 16 |
| [[MKRN1]] | 0.747 | makorin ring finger protein 1 |
| [[CTDSP2]] | 0.739 | CTD small phosphatase 2 |
| [[WBP1]] | 0.738 | WW domain binding protein 1 |
| [[ARID4A]] | 0.736 | AT-rich interaction domain 4A |
| [[OSER1-DT]] | 0.735 | OSER1 divergent transcript |
| [[UBN2]] | 0.725 | ubinuclein 2 |
| [[SMIM14]] | 0.722 | small integral membrane protein 14 |
| [[CCNG2]] | 0.717 | cyclin G2 |
| [[PCMTD1]] | 0.714 | protein-L-isoaspartate (D-aspartate) O-methyltransferase domain containing 1 |
| [[CERT1]] | 0.713 | ceramide transporter 1 |
| [[YTHDC1]] | 0.710 | YTH N6-methyladenosine RNA binding protein C1 |
| [[PIK3IP1]] | 0.709 | phosphoinositide-3-kinase interacting protein 1 |
| [[KDM6A]] | 0.701 | lysine demethylase 6A |
| [[TBC1D15]] | 0.698 | TBC1 domain family member 15 |
| [[OGA]] | 0.693 | O-GlcNAcase |
| [[CYLD]] | 0.692 | CYLD lysine 63 deubiquitinase |
| [[FBXO32]] | 0.688 | F-box protein 32 |
| [[PDCD4]] | 0.682 | programmed cell death 4 |
| [[ZBTB10]] | 0.675 | zinc finger and BTB domain containing 10 |
| [[NEK7]] | 0.663 | NIMA related kinase 7 |
| [[OSER1]] | 0.663 | oxidative stress responsive serine rich 1 |
| [[CEP44]] | 0.647 | centrosomal protein 44 |
| [[CLK1]] | 0.642 | CDC like kinase 1 |
| [[RICTOR]] | 0.632 | RPTOR independent companion of MTOR complex 2 |
| [[HECA]] | 0.626 | HECA ribonucleoprotein granule regulator |
| [[ANAPC1P2]] | 0.625 | ANAPC1 pseudogene 2 |
| [[MTURN]] | 0.619 | maturin, neural progenitor differentiation regulator homolog |
| [[INSR]] | 0.612 | insulin receptor |
| [[RNGTT]] | -0.612 | RNA guanylyltransferase and 5'-phosphatase |
| [[TNKS2]] | 0.602 | tankyrase 2 |
| [[CPEB3]] | 0.601 | cytoplasmic polyadenylation element binding protein 3 |
| [[NR1D2]] | 0.584 | nuclear receptor subfamily 1 group D member 2 |
| [[RNF103]] | 0.578 | ring finger protein 103 |
| [[CHD2]] | 0.570 | chromodomain helicase DNA binding protein 2 |
| [[OTUD1]] | 0.565 | OTU deubiquitinase 1 |
| [[PAIP2]] | 0.565 | poly(A) binding protein interacting protein 2 |
| [[PABIR3]] | 0.560 | PABIR family member 3 |
| [[FRAT2]] | 0.558 | FRAT regulator of Wnt signaling pathway 2 |
| [[REPS2]] | 0.552 | RALBP1 associated Eps domain containing 2 |
| [[TAX1BP1]] | 0.548 | Tax1 binding protein 1 |
| [[RNF5]] | 0.537 | ring finger protein 5 |
| [[SIRT1]] | 0.530 | sirtuin 1 |
| [[SERINC3]] | 0.519 | serine incorporator 3 |
| [[RHEBL1]] | 0.514 | RHEB like 1 |
| [[ENY2]] | 0.508 | ENY2 transcription and export complex 2 subunit |
| [[CENPC]] | 0.508 | centromere protein C |
| [[DHRS3]] | 0.504 | dehydrogenase/reductase 3 |
| [[NATD1]] | 0.499 | N-acetyltransferase domain containing 1 |
| [[ACVR2B]] | 0.476 | activin A receptor type 2B |
| [[PNPLA2]] | 0.469 | patatin like domain 2, triacylglycerol lipase |
| [[TOM1L2]] | 0.461 | target of myb1 like 2 membrane trafficking protein |
| [[HMGXB3]] | -0.455 | HMG-box containing 3 |
| [[INO80B]] | 0.420 | INO80 complex subunit B |
| [[RPS6KB1]] | 0.401 | ribosomal protein S6 kinase B1 |
| [[PDCL]] | 0.378 | phosducin like |
| [[SMAD4]] | 0.375 | SMAD family member 4 |
| [[IFT27]] | 0.285 | intraflagellar transport 27 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 69; `graph/modules.parquet` — module == 69; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [68] (drug-dose × line)
