---
module: 94
type: "module"
n_genes: 49
n_plus: 49
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.37698644399642944
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 094

*49 genes (single-armed) · [[Module 094.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 93), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Homoharringtonine (drug)]] 5 µM (+14.6, ⚠ cell-cycle shift); [[Selinexor (drug)]] 5 µM (+13.7, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (+10.0, ⚠ cell-cycle shift); [[Selinexor (drug)]] 0.5 µM (+9.3, ⚠ cell-cycle shift); [[Selinexor (drug)]] 0.05 µM (+9.3, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (+7.3, ⚠ cell-cycle shift); [[Osimertinib (mesylate) (drug)]] 5 µM (+6.8); [[Idarubicin (hydrochloride) (drug)]] 5 µM (+5.5, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (+5.5, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.05 µM (+3.1); [[Tucidinostat (drug)]] 5 µM (+2.8); [[Ponatinib (drug)]] 5 µM (+1.8); [[Adenine (drug)]] 5 µM (+1.7); [[Osimertinib (mesylate) (drug)]] 0.5 µM (+1.6); [[Harringtonine (drug)]] 0.05 µM (+1.6); [[Cobimetinib (drug)]] 5 µM (+1.5); [[Radotinib (drug)]] 5 µM (+1.4); [[Amsacrine (drug)]] 5 µM (+1.4) (52 in all, 24 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)
- Lower it: [[Digitoxin (drug)]] 0.5 µM (-2.0, ⚠ cell-cycle shift); [[Niclosamide (olamine) (drug)]] 5 µM (-1.8, ⚠ toxic; cell-cycle shift); [[Digitoxin (drug)]] 0.05 µM (-1.6, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 0.05 µM (-1.5, ⚠ cell-cycle shift); [[Peretinoin (drug)]] 5 µM (-1.5); [[Daptomycin (drug)]] 0.5 µM (-1.4, ⚠ unreliable plate only); [[Gefitinib (drug)]] 5 µM (-1.3); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (-1.3, ⚠ cell-cycle shift); [[c-Kit-IN-1 (drug)]] 0.05 µM (-1.2, ⚠ unreliable plate only); [[Dinaciclib (drug)]] 0.5 µM (-1.2, ⚠ toxic; transcription drop; cell-cycle shift); [[Diphenhydramine (drug)]] 0.5 µM (-1.1); [[Thymol (drug)]] 5 µM (-1.0) (13 in all, 9 with an alert ⚠; shown: the 10 strongest and the 2 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[SW480 (line)]], [[SW1417 (line)]], [[PANC-1 (line)]], [[NCI-H2347 (line)]], [[A-172 (line)]], [[HEC-1-A (line)]], [[HT-29 (line)]], [[RKO (line)]]

## + arm (49)

| Gene | Projection | Name |
|---|---|---|
| [[ZNF442]] | 0.896 | zinc finger protein 442 |
| [[ZNF433]] | 0.872 | zinc finger protein 433 |
| [[ZNF44]] | 0.846 | zinc finger protein 44 |
| [[DUSP15]] | 0.844 | dual specificity phosphatase 15 |
| [[ZNF441]] | 0.824 | zinc finger protein 441 |
| [[ZNF627]] | 0.813 | zinc finger protein 627 |
| [[ZNF563]] | 0.807 | zinc finger protein 563 |
| [[SLC43A2]] | 0.800 | solute carrier family 43 member 2 |
| [[CLN5]] | 0.788 | CLN5 lysosomal BMP synthase |
| [[SDSL]] | 0.771 | serine dehydratase like |
| [[TATDN3]] | 0.761 | TatD DNase domain containing 3 |
| [[SLC16A14]] | 0.760 | solute carrier family 16 member 14 |
| [[ZNF682]] | 0.723 | zinc finger protein 682 |
| [[ZNF391]] | 0.712 | zinc finger protein 391 |
| [[BTN2A1]] | 0.709 | butyrophilin subfamily 2 member A1 |
| [[ZNF101]] | 0.707 | zinc finger protein 101 |
| [[NUDT16]] | 0.699 | nudix hydrolase 16 |
| [[PCLO]] | 0.698 | piccolo presynaptic cytomatrix protein |
| [[CHST3]] | 0.681 | carbohydrate sulfotransferase 3 |
| [[NGFR]] | 0.680 | nerve growth factor receptor |
| [[OSGIN2]] | 0.670 | oxidative stress induced growth inhibitor family member 2 |
| [[SCART1]] | -0.669 | scavenger receptor family member expressed on T cells 1 |
| [[SLC44A2]] | 0.669 | solute carrier family 44 member 2 (CTL2 blood group) |
| [[STK32A]] | 0.667 | serine/threonine kinase 32A |
| [[XPO1]] | 0.656 | exportin 1 |
| [[ZNF844]] | 0.653 | zinc finger protein 844 |
| [[BTN2A3P]] | 0.651 | butyrophilin subfamily 2 member A3, pseudogene |
| [[TRPM4]] | 0.629 | transient receptor potential cation channel subfamily M member 4 |
| [[HES7]] | 0.623 | hes family bHLH transcription factor 7 |
| [[ZNF20]] | 0.619 | zinc finger protein 20 |
| [[BTN2A3P-1]] | 0.604 | — |
| [[RNF150]] | 0.600 | ring finger protein 150 |
| [[ZNF700]] | 0.581 | zinc finger protein 700 |
| [[HMGN4]] | 0.569 | high mobility group nucleosomal binding domain 4 |
| [[ZNF440]] | 0.561 | zinc finger protein 440 |
| [[HSPA4L]] | 0.556 | heat shock protein family A (Hsp70) member 4 like |
| [[GNG2]] | 0.556 | G protein subunit gamma 2 |
| [[NADK2]] | 0.555 | NAD kinase 2, mitochondrial |
| [[PRTG]] | 0.549 | protogenin |
| [[ZNF419]] | 0.527 | zinc finger protein 419 |
| [[SLC2A4RG]] | 0.525 | SLC2A4 regulator |
| [[PSME4]] | -0.520 | proteasome activator subunit 4 |
| [[ZNF727]] | 0.515 | zinc finger protein 727 |
| [[ZKSCAN8]] | 0.512 | zinc finger with KRAB and SCAN domains 8 |
| [[RNFT1]] | 0.511 | ring finger protein, transmembrane 1 |
| [[CNKSR1]] | 0.504 | connector enhancer of kinase suppressor of Ras 1 |
| [[TMEM17]] | 0.500 | transmembrane protein 17 |
| [[GPCPD1]] | 0.493 | glycerophosphocholine phosphodiesterase 1 |
| [[TRAF3IP2]] | 0.469 | TRAF3 interacting protein 2 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 94; `graph/modules.parquet` — module == 94; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [93] (drug-dose × line)
