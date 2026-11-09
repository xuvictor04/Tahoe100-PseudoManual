---
module: 72
type: "module"
n_genes: 69
n_plus: 69
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.2334848791360855
label: "Degradation of DVL"
label_source: "reactome"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 072

*Degradation of DVL · 69 genes (single-armed) · [[Module 072.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

Label from the validation stage: **Degradation of DVL** (reactome, q 1e-15; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | Degradation of DVL | reactome | 12/69 | 61.0 | 1e-15 |
| + | Degradation of DVL | reactome | 12/69 | 61.0 | 1e-15 |
| + | proteasome | control | 11/69 | 77.5 | 2e-15 |
| all | proteasome | control | 11/69 | 77.5 | 2e-15 |
| all | NIK-->noncanonical NF-kB signaling | reactome | 12/69 | 57.0 | 3e-15 |
| + | NIK-->noncanonical NF-kB signaling | reactome | 12/69 | 57.0 | 3e-15 |
| + | Dectin-1 mediated noncanonical NF-kB signaling | reactome | 12/69 | 55.8 | 4e-15 |
| all | Dectin-1 mediated noncanonical NF-kB signaling | reactome | 12/69 | 55.8 | 4e-15 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 71), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Ixazomib citrate (drug)]] 5 µM (+12.7, ⚠ cell-cycle shift); [[Bortezomib (drug)]] 0.05 µM (+12.0, ⚠ cell-cycle shift); [[Ixazomib citrate (drug)]] 0.5 µM (+11.9); [[Auranofin (drug)]] 5 µM (+6.7); [[Idarubicin (hydrochloride) (drug)]] 5 µM (+4.9, ⚠ cell-cycle shift); [[Bortezomib (drug)]] 0.5 µM (+4.9); [[Bortezomib (drug)]] 5 µM (+4.9, ⚠ toxic; cell-cycle shift); [[Panobinostat (drug)]] 5 µM (+4.7, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (+4.3, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (+4.2, ⚠ cell-cycle shift); [[Ixazomib citrate (drug)]] 0.05 µM (+1.4); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+1.3); [[Infigratinib (drug)]] 5 µM (+1.2) (23 in all, 17 with an alert ⚠; shown: the 10 strongest and the 3 next strongest without an alert)
- Lower it: [[Homoharringtonine (drug)]] 5 µM (-3.0, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-1.7, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-1.5, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (-1.1, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.05 µM (-1.0) (5 in all, 4 with an alert ⚠)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[SW480 (line)]], [[PANC-1 (line)]], [[HOP62 (line)]], [[HEC-1-A (line)]], [[LoVo (line)]], [[HT-29 (line)]], [[KATO III (line)]], [[NCI-H460 (line)]]

## Candidate new members

*Members not annotated to the set their arm is enriched for, ranked by mean cos to the annotated members (`validation/novel_members.csv`); ⚠ = a reason to doubt the gene's place (in the vector space only through flagged drug-doses), kept in its rank. 16 candidates, none with an alert; shown: the 15 strongest.*

| # | Gene | Set | Mean cos |
|---|---|---|---|
| 1 | [[PSMC6]] | Antigen processing: Ub, ATP-independent proteasomal degradation | +0.62 |
| 2 | [[BABAM1]] | proteasome | +0.61 |
| 3 | [[PSMB4]] | MYC targets v1 | +0.61 |
| 4 | [[PSMD13]] | MYC targets v1 | +0.59 |
| 5 | [[PSMA3]] | MYC targets v1 | +0.59 |
| 6 | [[MRPL18]] | proteasome | +0.57 |
| 7 | [[TXNL1]] | proteasome | +0.55 |
| 8 | [[ANKRD39]] | proteasome | +0.55 |
| 9 | [[PLAA]] | proteasome | +0.55 |
| 10 | [[TMEM161A]] | proteasome | +0.54 |
| 11 | [[TALDO1]] | Antigen processing: Ub, ATP-independent proteasomal degradation | +0.53 |
| 12 | [[CASP6]] | Antigen processing: Ub, ATP-independent proteasomal degradation | +0.52 |
| 13 | [[SLC10A7]] | proteasome | +0.52 |
| 14 | [[ANKRD23]] | Deubiquitination | +0.51 |
| 15 | [[MRPS15]] | proteasome | +0.51 |

## + arm (69)

| Gene | Projection | Name |
|---|---|---|
| [[ANKRD39]] | 0.867 | ankyrin repeat domain 39 |
| [[BABAM1]] | 0.856 | BRISC and BRCA1 A complex member 1 |
| [[PSMB4]] | 0.831 | proteasome 20S subunit beta 4 |
| [[PSMB3]] | 0.810 | proteasome 20S subunit beta 3 |
| [[TMEM161A]] | 0.796 | transmembrane protein 161A |
| [[PSMD13]] | 0.793 | proteasome 26S subunit, non-ATPase 13 |
| [[MRPL18]] | 0.787 | mitochondrial ribosomal protein L18 |
| [[ANKRD23]] | 0.767 | ankyrin repeat domain 23 |
| [[UFD1]] | 0.753 | ubiquitin recognition factor in ER associated degradation 1 |
| [[ZFAND2A]] | 0.748 | zinc finger AN1-type containing 2A |
| [[TANGO2]] | 0.739 | transport and golgi organization 2 homolog |
| [[PSMB2]] | 0.732 | proteasome 20S subunit beta 2 |
| [[PLAA]] | 0.722 | phospholipase A2 activating protein |
| [[PSMA1]] | 0.716 | proteasome 20S subunit alpha 1 |
| [[SNX29]] | 0.714 | sorting nexin 29 |
| [[PCYT1A]] | 0.711 | phosphate cytidylyltransferase 1A, choline |
| [[MED31]] | 0.703 | mediator complex subunit 31 |
| [[PSMA2]] | 0.698 | proteasome 20S subunit alpha 2 |
| [[PSMC4]] | 0.681 | proteasome 26S subunit, ATPase 4 |
| [[EPS15L1]] | 0.676 | epidermal growth factor receptor pathway substrate 15 like 1 |
| [[CCDC32]] | 0.675 | coiled-coil domain containing 32 |
| [[UBE4B]] | 0.663 | ubiquitination factor E4B |
| [[TALDO1]] | 0.662 | transaldolase 1 |
| [[PSMC6]] | 0.661 | proteasome 26S subunit, ATPase 6 |
| [[TXNL1]] | 0.651 | thioredoxin like 1 |
| [[ALKBH6]] | 0.641 | alkB homolog 6, nucleotide demethylase |
| [[MRPS15]] | 0.639 | mitochondrial ribosomal protein S15 |
| [[DYNC1I1]] | 0.638 | dynein cytoplasmic 1 intermediate chain 1 |
| [[FAM219A]] | 0.635 | family with sequence similarity 219 member A |
| [[PSMA6]] | 0.633 | proteasome 20S subunit alpha 6 |
| [[SLC10A7]] | 0.631 | solute carrier family 10 member 7 |
| [[DGKG]] | 0.625 | diacylglycerol kinase gamma |
| [[ZNF771]] | 0.621 | zinc finger protein 771 |
| [[VIPAS39]] | 0.619 | VPS33B interacting protein, apical-basolateral polarity regulator, spe-39 homolog |
| [[CASP6]] | 0.615 | caspase 6 |
| [[MBOAT7]] | 0.614 | membrane bound acylglycerophosphatidylinositol O-acyltransferase MBOAT7 |
| [[PSMD8]] | 0.613 | proteasome 26S subunit, non-ATPase 8 |
| [[RAD9A]] | 0.603 | RAD9 checkpoint clamp component A |
| [[EMC4]] | 0.593 | ER membrane protein complex subunit 4 |
| [[ALDH2]] | 0.586 | aldehyde dehydrogenase 2 family member |
| [[AAK1]] | 0.585 | AP2 associated kinase 1 |
| [[PSMA3]] | 0.579 | proteasome 20S subunit alpha 3 |
| [[HECW1]] | 0.569 | HECT, C2 and WW domain containing E3 ubiquitin protein ligase 1 |
| [[ABCB8]] | 0.564 | ATP binding cassette subfamily B member 8 |
| [[ATG4A]] | 0.564 | autophagy related 4A cysteine peptidase |
| [[SPINDOC]] | 0.559 | spindlin interactor and repressor of chromatin binding |
| [[DMAC2]] | 0.557 | distal membrane arm assembly component 2 |
| [[NQO2]] | 0.548 | N-ribosyldihydronicotinamide:quinone dehydrogenase 2 |
| [[UBE2M]] | 0.547 | ubiquitin conjugating enzyme E2 M |
| [[SANBR]] | 0.543 | SANT and BTB domain regulator of CSR |
| [[MRPL37]] | 0.539 | mitochondrial ribosomal protein L37 |
| [[KLHL25]] | 0.534 | kelch like family member 25 |
| [[TBK1]] | 0.524 | TANK binding kinase 1 |
| [[POMP]] | 0.509 | proteasome maturation protein |
| [[PRR13]] | 0.499 | proline rich 13 |
| [[ABHD3]] | 0.497 | abhydrolase domain containing 3, phospholipase |
| [[AP4B1]] | 0.495 | adaptor related protein complex 4 subunit beta 1 |
| [[MICB]] | 0.485 | MHC class I polypeptide-related sequence B |
| [[EPDR1]] | 0.480 | ependymin related 1 |
| [[KCNAB2]] | 0.477 | potassium voltage-gated channel subfamily A regulatory beta subunit 2 |
| [[UBR3]] | 0.475 | ubiquitin protein ligase E3 component n-recognin 3 |
| [[PLOD3]] | 0.460 | procollagen-lysine,2-oxoglutarate 5-dioxygenase 3 |
| [[CEP126]] | 0.456 | centrosomal protein 126 |
| [[SSX1]] | 0.445 | SSX family member 1 |
| [[LHFPL2]] | 0.441 | LHFPL tetraspan subfamily member 2 |
| [[ACTR1A]] | 0.435 | actin related protein 1A |
| [[DEPDC7]] | -0.396 | DEP domain containing 7 |
| [[TMEM116]] | 0.387 | transmembrane protein 116 |
| [[SNX13]] | 0.375 | sorting nexin 13 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 72; `graph/modules.parquet` — module == 72; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [71] (drug-dose × line)
