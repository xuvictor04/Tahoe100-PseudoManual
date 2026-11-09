---
module: 85
type: "module"
n_genes: 52
n_plus: 46
n_minus: 6
arms_opposite: true
mean_cos_between_arms: -0.4331710934638977
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 085

*52 genes (46 in the + arm, 6 in the − arm) · [[Module 085.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43). The + arm rises where the − arm falls. Arm = the side of the module's main direction a gene sits on.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of the + arm minus the − arm (`graph/module_pooled_z.npy`, row 84), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it (+ arm up, − arm down): [[Panobinostat (drug)]] 5 µM (+19.8, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (+18.8, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (+17.2, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (+9.0, ⚠ cell-cycle shift); [[Belinostat (drug)]] 0.5 µM (+6.4, ⚠ cell-cycle shift); [[Brivudine (drug)]] 5 µM (+6.0); [[Tucidinostat (drug)]] 5 µM (+6.0); [[Tucidinostat (drug)]] 0.5 µM (+2.7, ⚠ cell-cycle shift); [[HI-TOPK-032 (drug)]] 5 µM (+2.5); [[Ipatasertib (drug)]] 0.5 µM (+2.2); [[Radotinib (drug)]] 5 µM (+1.6); [[PF-06260933 (drug)]] 5 µM (+1.5); [[Daidzin (drug)]] 5 µM (+1.5); [[Brivudine (drug)]] 0.5 µM (+1.5); [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM (+1.3); [[Niclosamide (olamine) (drug)]] 0.5 µM (+1.3) (35 in all, 7 with an alert ⚠; shown: the 10 strongest and the 6 next strongest without an alert)
- Lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM (-16.8, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-12.8, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 5 µM (-12.0, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (-11.9, ⚠ toxic; transcription drop; cell-cycle shift); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (-10.9, ⚠ cell-cycle shift); [[Epirubicin (hydrochloride) (drug)]] 5 µM (-9.9, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (-9.8, ⚠ toxic; transcription drop; cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-9.5, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (-9.4, ⚠ toxic; transcription drop; cell-cycle shift); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (-9.1); [[Homoharringtonine (drug)]] 0.05 µM (-5.6); [[Auranofin (drug)]] 5 µM (-4.2); [[Belumosudil (drug)]] 5 µM (-2.9); [[Harringtonine (drug)]] 0.05 µM (-2.5); [[Ixazomib citrate (drug)]] 0.5 µM (-2.2); [[5-Azacytidine (drug)]] 5 µM (-2.1); [[Belzutifan (drug)]] 5 µM (-2.1); [[TAK-901 (drug)]] 0.05 µM (-1.8); [[Amsacrine (drug)]] 5 µM (-1.8) (69 in all, 27 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[SW480 (line)]], [[HOP62 (line)]], [[PANC-1 (line)]], [[HS-578T (line)]], [[Panc 03.27 (line)]], [[KATO III (line)]], [[HEC-1-A (line)]], [[A-172 (line)]]

## + arm (46)

| Gene | Projection | Name |
|---|---|---|
| [[SLC27A1]] | 0.897 | solute carrier family 27 member 1 |
| [[MAST3]] | 0.880 | microtubule associated serine/threonine kinase 3 |
| [[YIF1B]] | 0.863 | Yip1 interacting factor homolog B, membrane trafficking protein |
| [[GNAI2]] | 0.833 | G protein subunit alpha i2 |
| [[PEDS1]] | 0.820 | plasmanylethanolamine desaturase 1 |
| [[CABLES2]] | 0.807 | Cdk5 and Abl enzyme substrate 2 |
| [[PCMT1]] | 0.797 | protein-L-isoaspartate (D-aspartate) O-methyltransferase |
| [[FCHO1]] | 0.791 | FCH and mu domain containing endocytic adaptor 1 |
| [[CEP131]] | 0.784 | centrosomal protein 131 |
| [[FBXL16]] | 0.782 | F-box and leucine rich repeat protein 16 |
| [[FAM13B]] | 0.761 | family with sequence similarity 13 member B |
| [[CFD]] | 0.747 | complement factor D |
| [[TNFAIP8L1]] | 0.745 | TNF alpha induced protein 8 like 1 |
| [[RGS14]] | 0.740 | regulator of G protein signaling 14 |
| [[LRRC42]] | 0.734 | leucine rich repeat containing 42 |
| [[TNNI3]] | 0.723 | troponin I3, cardiac type |
| [[TECPR1]] | 0.718 | tectonin beta-propeller repeat containing 1 |
| [[DOK4]] | 0.717 | docking protein 4 |
| [[PLA2G15]] | 0.717 | phospholipase A2 group XV |
| [[RAB40B]] | 0.712 | RAB40B, member RAS oncogene family |
| [[HDGFL2]] | 0.707 | HDGF like 2 |
| [[PAK4]] | 0.698 | p21 (RAC1) activated kinase 4 |
| [[PLPPR2]] | 0.696 | phospholipid phosphatase related 2 |
| [[SH2B2]] | 0.694 | SH2B adaptor protein 2 |
| [[KANK2]] | 0.692 | KN motif and ankyrin repeat domains 2 |
| [[MAD2L2]] | 0.690 | mitotic arrest deficient 2 like 2 |
| [[ZNF511]] | 0.688 | zinc finger protein 511 |
| [[DHTKD1]] | 0.686 | dehydrogenase E1 and transketolase domain containing 1 |
| [[PLCD1]] | 0.684 | phospholipase C delta 1 |
| [[KIAA1328]] | 0.674 | KIAA1328 |
| [[NPHP4]] | 0.672 | nephrocystin 4 |
| [[FANCE]] | 0.646 | FA complementation group E |
| [[GAS2L1]] | 0.645 | growth arrest specific 2 like 1 |
| [[GIPC1]] | 0.641 | GIPC PDZ domain containing family member 1 |
| [[FN3KRP]] | 0.638 | fructosamine 3 kinase related protein |
| [[TMEM63C]] | 0.630 | transmembrane protein 63C |
| [[SEPTIN6]] | 0.629 | septin 6 |
| [[KANTR]] | 0.582 | KANTR integral membrane protein |
| [[GGA1]] | 0.573 | golgi associated, gamma adaptin ear containing, ARF binding protein 1 |
| [[FOXK1]] | 0.553 | forkhead box K1 |
| [[KHDRBS1]] | 0.543 | KH RNA binding domain containing, signal transduction associated 1 |
| [[RASAL1]] | 0.538 | RAS protein activator like 1 |
| [[ARHGEF10]] | 0.528 | Rho guanine nucleotide exchange factor 10 |
| [[DNM2]] | 0.503 | dynamin 2 |
| [[MEGF9]] | 0.461 | multiple EGF like domains 9 |
| [[STAU1]] | 0.430 | staufen double-stranded RNA binding protein 1 |

## − arm (6)

| Gene | Projection | Name |
|---|---|---|
| [[DECR1]] | -0.758 | 2,4-dienoyl-CoA reductase 1 |
| [[KRR1]] | -0.699 | KRR1 small subunit processome component |
| [[RBMX]] | -0.640 | RNA binding motif protein X-linked |
| [[IRAK4]] | -0.621 | interleukin 1 receptor associated kinase 4 |
| [[GNG12-AS1]] | -0.600 | GNG12, DIRAS3 and WLS antisense RNA 1 |
| [[VBP1]] | -0.582 | VHL binding protein 1 |

## Data

- `graph/nodes.parquet` — module == 85; `graph/modules.parquet` — module == 85; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [84] (drug-dose × line)
