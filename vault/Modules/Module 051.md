---
module: 51
type: "module"
n_genes: 89
n_plus: 80
n_minus: 9
arms_opposite: true
mean_cos_between_arms: -0.3086563050746918
label: "Chromatin modifying enzymes"
label_source: "reactome"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 051

*Chromatin modifying enzymes · 89 genes (80 in the + arm, 9 in the − arm) · [[Module 051.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31). The + arm rises where the − arm falls. Arm = the side of the module's main direction a gene sits on.

Label from the validation stage: **Chromatin modifying enzymes** (reactome, q 0.037; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| + | Chromatin modifying enzymes | reactome | 7/80 | 6.50 | 0.037 |
| + | mRNA Splicing - Major Pathway | reactome | 7/80 | 6.47 | 0.038 |
| + | mRNA Splicing | reactome | 7/80 | 6.22 | 0.046 |

## Drugs that move it

*Mean pooled z of the + arm minus the − arm (`graph/module_pooled_z.npy`, row 50), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it (+ arm up, − arm down): [[Homoharringtonine (drug)]] 5 µM (+23.6, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (+16.2, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (+13.8, ⚠ cell-cycle shift); [[TAK-901 (drug)]] 5 µM (+10.1, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (+8.1, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (+7.2, ⚠ cell-cycle shift); [[PH-797804 (drug)]] 5 µM (+6.9); [[Digitoxin (drug)]] 5 µM (+5.0, ⚠ toxic; transcription drop; cell-cycle shift); [[Homoharringtonine (drug)]] 0.05 µM (+4.5); [[Ixazomib citrate (drug)]] 5 µM (+4.3, ⚠ cell-cycle shift); [[Ixazomib citrate (drug)]] 0.5 µM (+3.1); [[TAK-901 (drug)]] 0.05 µM (+3.0); [[EX229 (drug)]] 5 µM (+2.2); [[Harringtonine (drug)]] 0.05 µM (+2.1); [[Belumosudil (drug)]] 5 µM (+2.0); [[Gallic acid (hydrate) (drug)]] 0.05 µM (+1.8); [[Trametinib (drug)]] 0.5 µM (+1.7); [[Filgotinib (drug)]] 5 µM (+1.7) (66 in all, 25 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)
- Lower it: [[Panobinostat (drug)]] 5 µM (-17.6, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (-16.9, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (-16.5, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (-15.2, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (-10.0, ⚠ cell-cycle shift); [[Belinostat (drug)]] 0.5 µM (-9.6, ⚠ cell-cycle shift); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (-8.2, ⚠ cell-cycle shift); [[Epirubicin (hydrochloride) (drug)]] 5 µM (-6.9, ⚠ cell-cycle shift); [[Brivudine (drug)]] 5 µM (-5.8); [[Auranofin (drug)]] 5 µM (-5.4); [[Tucidinostat (drug)]] 5 µM (-5.2); [[Belinostat (drug)]] 0.05 µM (-2.8); [[Neratinib (drug)]] 5 µM (-1.9); [[Lopinavir (drug)]] 5 µM (-1.6); [[Neratinib (maleate) (drug)]] 5 µM (-1.6); [[Bosentan (hydrate) (drug)]] 5 µM (-1.5); [[Celecoxib (drug)]] 0.05 µM (-1.5); [[HI-TOPK-032 (drug)]] 0.05 µM (-1.5) (53 in all, 21 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[SW480 (line)]], [[PANC-1 (line)]], [[NCI-H460 (line)]], [[HEC-1-A (line)]], [[LOX-IMVI (line)]], [[A549 (line)]], [[A498 (line)]], [[HOP62 (line)]]

## + arm (80)

| Gene | Projection | Name |
|---|---|---|
| [[EPC1]] | 0.877 | enhancer of polycomb 1 |
| [[SCAF8]] | 0.853 | SR-related CTD associated factor 8 |
| [[ZNF644]] | 0.846 | zinc finger protein 644 |
| [[EPC2]] | 0.828 | enhancer of polycomb 2 |
| [[NFYC]] | 0.817 | nuclear transcription factor Y subunit gamma |
| [[RBM23]] | 0.808 | RNA binding motif protein 23 |
| [[SENP6]] | 0.797 | SUMO specific peptidase 6 |
| [[LARP7]] | 0.794 | La ribonucleoprotein 7, transcriptional regulator |
| [[WARS2]] | 0.791 | tryptophanyl tRNA synthetase 2, mitochondrial |
| [[YJU2]] | 0.781 | YJU2 splicing factor homolog |
| [[BRAF]] | 0.774 | B-Raf proto-oncogene, serine/threonine kinase |
| [[ING3]] | 0.773 | inhibitor of growth family member 3 |
| [[INO80]] | 0.764 | INO80 complex ATPase subunit |
| [[SREK1]] | 0.753 | splicing regulatory glutamic acid and lysine rich protein 1 |
| [[BPTF]] | 0.753 | bromodomain PHD finger transcription factor |
| [[SRSF4]] | 0.745 | serine and arginine rich splicing factor 4 |
| [[THG1L]] | 0.735 | tRNA-histidine guanylyltransferase 1 like |
| [[COQ7]] | 0.727 | coenzyme Q7, hydroxylase |
| [[ADNP]] | 0.707 | activity dependent neuroprotector homeobox |
| [[ATRX]] | 0.706 | ATRX chromatin remodeler |
| [[ZNF280D]] | 0.705 | zinc finger protein 280D |
| [[KMT5B]] | 0.705 | lysine methyltransferase 5B |
| [[USP16]] | 0.701 | ubiquitin specific peptidase 16 |
| [[ACIN1]] | 0.692 | apoptotic chromatin condensation inducer 1 |
| [[GPATCH8]] | 0.689 | G-patch domain containing 8 |
| [[POGZ]] | 0.688 | pogo transposable element derived with ZNF domain |
| [[RBM5]] | 0.681 | RNA binding motif protein 5 |
| [[TRMO]] | 0.677 | tRNA methyltransferase O |
| [[CC2D2A]] | 0.666 | coiled-coil and C2 domain containing 2A |
| [[SMARCB1]] | 0.663 | SWI/SNF related BAF chromatin remodeling complex subunit B1 |
| [[SETD2]] | 0.663 | SET domain containing 2, histone lysine methyltransferase |
| [[UBE3A]] | 0.662 | ubiquitin protein ligase E3A |
| [[ELF1]] | 0.657 | E74 like ETS transcription factor 1 |
| [[TLK1]] | 0.656 | tousled like kinase 1 |
| [[LIPT1]] | 0.649 | lipoyltransferase 1 |
| [[ABCB7]] | 0.646 | ATP binding cassette subfamily B member 7 |
| [[TOR1AIP1]] | 0.644 | torsin 1A interacting protein 1 |
| [[STAG1]] | 0.644 | STAG1 cohesin complex component |
| [[HELQ]] | 0.643 | helicase, POLQ like |
| [[PBRM1]] | 0.636 | polybromo 1 |
| [[LANCL2]] | 0.635 | LanC like glutathione S-transferase 2 |
| [[NCOA5]] | 0.629 | nuclear receptor coactivator 5 |
| [[ZNF414]] | 0.629 | zinc finger protein 414 |
| [[DHFR2]] | 0.623 | dihydrofolate reductase 2 |
| [[OTUD6B-AS1]] | 0.621 | OTUD6B antisense RNA 1 |
| [[NSUN3]] | 0.618 | NOP2/Sun RNA methyltransferase 3 |
| [[ZNF428]] | 0.613 | zinc finger protein 428 |
| [[SLC24A1]] | 0.603 | solute carrier family 24 member 1 |
| [[ASXL1]] | 0.602 | ASXL transcriptional regulator 1 |
| [[RBM10]] | 0.600 | RNA binding motif protein 10 |
| [[NUBP1]] | 0.583 | NUBP iron-sulfur cluster assembly factor 1, cytosolic |
| [[ZNF713]] | 0.582 | zinc finger protein 713 |
| [[CHIC1]] | 0.580 | cysteine rich hydrophobic domain 1 |
| [[ATF1]] | 0.577 | activating transcription factor 1 |
| [[ARMC5]] | 0.564 | armadillo repeat containing 5 |
| [[PTBP2]] | 0.559 | polypyrimidine tract binding protein 2 |
| [[SLTM]] | 0.552 | SAFB like transcription modulator |
| [[DNAJC8]] | 0.551 | DnaJ heat shock protein family (Hsp40) member C8 |
| [[BAZ1B]] | 0.548 | bromodomain adjacent to zinc finger domain 1B |
| [[TMEM18]] | 0.536 | transmembrane protein 18 |
| [[MECP2]] | 0.507 | methyl-CpG binding protein 2 |
| [[TEN1]] | 0.492 | TEN1 subunit of CST complex |
| [[TTC12]] | 0.489 | tetratricopeptide repeat domain 12 |
| [[SMARCA5]] | 0.483 | SNF2 related chromatin remodeling ATPase 5 |
| [[COQ2]] | 0.470 | coenzyme Q2, polyprenyltransferase |
| [[ARMH4]] | 0.457 | armadillo like helical domain containing 4 |
| [[CYB5RL]] | 0.455 | cytochrome b5 reductase 5 (putative) |
| [[SNX12]] | 0.455 | sorting nexin 12 |
| [[FOXRED2]] | 0.455 | FAD dependent oxidoreductase domain containing 2 |
| [[PUM2]] | 0.454 | pumilio RNA binding family member 2 |
| [[MTMR3]] | 0.445 | myotubularin related protein 3 |
| [[PRPF40A]] | 0.412 | pre-mRNA processing factor 40A |
| [[C5orf24]] | 0.411 | chromosome 5 open reading frame 24 |
| [[NFAT5]] | 0.393 | nuclear factor of activated T cells 5 |
| [[SLC2A11]] | 0.384 | solute carrier family 2 member 11 |
| [[HNRNPA0]] | 0.379 | heterogeneous nuclear ribonucleoprotein A0 |
| [[NCOR1]] | 0.315 | nuclear receptor corepressor 1 |
| [[FBXW9]] | 0.216 | F-box and WD repeat domain containing 9 |
| [[NRDC]] | 0.209 | nardilysin convertase |
| [[DGAT2]] | 0.119 | diacylglycerol O-acyltransferase 2 |

## − arm (9)

| Gene | Projection | Name |
|---|---|---|
| [[PIGF]] | -0.718 | phosphatidylinositol glycan anchor biosynthesis class F |
| [[MXRA7]] | -0.636 | matrix remodeling associated 7 |
| [[ENTPD4]] | -0.624 | ectonucleoside triphosphate diphosphohydrolase 4 |
| [[TOR1B]] | -0.562 | torsin family 1 member B |
| [[TMEM87B]] | -0.499 | transmembrane protein 87B |
| [[SPATA33]] | -0.485 | spermatogenesis associated 33 |
| [[NMRK1]] | -0.436 | nicotinamide riboside kinase 1 |
| [[CAMTA1]] | -0.390 | calmodulin binding transcription activator 1 |
| [[LSM11]] | -0.381 | LSM11, U7 small nuclear RNA associated |

## Data

- `graph/nodes.parquet` — module == 51; `graph/modules.parquet` — module == 51; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [50] (drug-dose × line)
