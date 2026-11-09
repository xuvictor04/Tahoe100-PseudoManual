---
module: 62
type: "module"
n_genes: 78
n_plus: 78
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.29682108759880066
label: "p53 targets up"
label_source: "control"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 062

*p53 targets up · 78 genes (single-armed) · [[Module 062.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

Label from the validation stage: **p53 targets up** (control, q 7e-47; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | p53 targets up | control | 26/78 | 120 | 7e-47 |
| + | p53 targets up | control | 26/78 | 120 | 7e-47 |
| all | p53 pathway | hallmark | 26/78 | 26.7 | 5e-27 |
| + | p53 pathway | hallmark | 26/78 | 26.7 | 5e-27 |
| + | Transcriptional Regulation by TP53 | reactome | 14/78 | 7.91 | 2e-06 |
| all | Transcriptional Regulation by TP53 | reactome | 14/78 | 7.91 | 2e-06 |
| all | TP53 Regulates Transcription of Cell Death Genes | reactome | 6/78 | 28.3 | 4e-05 |
| + | TP53 Regulates Transcription of Cell Death Genes | reactome | 6/78 | 28.3 | 4e-05 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 61), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM (+10.1, ⚠ cell-cycle shift); [[Topotecan (hydrochloride) (drug)]] 5 µM (+6.0, ⚠ toxic; cell-cycle shift); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (+5.4, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 5 µM (+5.4, ⚠ cell-cycle shift); [[Selinexor (drug)]] 5 µM (+4.9, ⚠ cell-cycle shift); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+4.7); [[Idarubicin (hydrochloride) (drug)]] 0.5 µM (+4.5, ⚠ cell-cycle shift); [[Epirubicin (hydrochloride) (drug)]] 5 µM (+4.5, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+3.7, ⚠ toxic; transcription drop; cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (+3.5, ⚠ cell-cycle shift); [[Amsacrine (drug)]] 5 µM (+3.4); [[Tucidinostat (drug)]] 5 µM (+2.9); [[Homoharringtonine (drug)]] 0.05 µM (+2.3); [[Topotecan (hydrochloride) (drug)]] 0.05 µM (+2.3); [[Ponatinib (drug)]] 5 µM (+1.9); [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM (+1.8); [[Amsacrine (drug)]] 0.5 µM (+1.8); [[Harringtonine (drug)]] 0.05 µM (+1.7); [[Mitoxantrone (dihydrochloride) (drug)]] 0.05 µM (+1.6) (48 in all, 25 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)
- Lower it: [[Ixazomib citrate (drug)]] 0.5 µM (-1.9); [[Ixazomib citrate (drug)]] 5 µM (-1.8, ⚠ cell-cycle shift); [[Auranofin (drug)]] 5 µM (-1.4); [[c-Kit-IN-1 (drug)]] 0.05 µM (-1.3, ⚠ unreliable plate only); [[Digitoxin (drug)]] 0.5 µM (-1.1, ⚠ cell-cycle shift); [[Pyridoxine (hydrochloride) (drug)]] 5 µM (-1.0) (6 in all, 3 with an alert ⚠)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[NCI-H460 (line)]], [[A498 (line)]], [[LoVo (line)]], [[RKO (line)]], [[A549 (line)]], [[LS 180 (line)]], [[HepG2_C3A (line)]], [[LOX-IMVI (line)]]

## Candidate new members

*Members not annotated to the set their arm is enriched for, ranked by mean cos to the annotated members (`validation/novel_members.csv`); ⚠ = a reason to doubt the gene's place (in the vector space only through flagged drug-doses), kept in its rank. 33 candidates, none with an alert; shown: the 15 strongest.*

| # | Gene | Set | Mean cos |
|---|---|---|---|
| 1 | [[MDM2]] | TP53 Regulates Transcription of Cell Death Genes | +0.67 |
| 2 | [[SPATA18]] | TP53 Regulates Transcription of Cell Death Genes | +0.66 |
| 3 | [[ACTA2]] | TP53 Regulates Transcription of Cell Death Genes | +0.65 |
| 4 | [[PINCR]] | p53 targets up | +0.64 |
| 5 | [[FDXR]] | TP53 Regulates Transcription of Cell Death Genes | +0.64 |
| 6 | [[PTCHD4]] | p53 targets up | +0.63 |
| 7 | [[GRIN2C]] | apoptosis | +0.63 |
| 8 | [[RRM2B]] | apoptosis | +0.62 |
| 9 | [[ZMAT3]] | TP53 Regulates Transcription of Cell Death Genes | +0.62 |
| 10 | [[EDA2R]] | TP53 Regulates Transcription of Cell Death Genes | +0.61 |
| 11 | [[PHLDA3]] | TP53 Regulates Transcription of Cell Death Genes | +0.60 |
| 12 | [[PURPL]] | p53 targets up | +0.59 |
| 13 | [[ZNF79]] | TP53 Regulates Transcription of Cell Death Genes | +0.57 |
| 14 | [[PPM1D]] | p53 targets up | +0.57 |
| 15 | [[DDB2]] | TP53 Regulates Transcription of Cell Death Genes | +0.57 |

## + arm (78)

| Gene | Projection | Name |
|---|---|---|
| [[SPATA18]] | 0.889 | spermatogenesis associated 18 |
| [[PINCR]] | 0.888 | p53-induced noncoding RNA |
| [[ACTA2]] | 0.882 | actin alpha 2, smooth muscle |
| [[FDXR]] | 0.867 | ferredoxin reductase |
| [[GRIN2C]] | 0.856 | glutamate ionotropic receptor NMDA type subunit 2C |
| [[ZMAT3]] | 0.848 | zinc finger matrin-type 3 |
| [[PTCHD4]] | 0.839 | patched domain containing 4 |
| [[MDM2]] | 0.834 | MDM2 proto-oncogene |
| [[EDA2R]] | 0.830 | ectodysplasin A2 receptor |
| [[PURPL]] | 0.813 | p53 upregulated regulator of p53 levels |
| [[RRM2B]] | 0.789 | ribonucleotide reductase regulatory TP53 inducible subunit M2B |
| [[FAS]] | 0.783 | Fas cell surface death receptor |
| [[DDB2]] | 0.779 | damage specific DNA binding protein 2 |
| [[BAX]] | 0.776 | BCL2 associated X, apoptosis regulator |
| [[ANKRA2]] | 0.776 | ankyrin repeat family A member 2 |
| [[RPS27L]] | 0.775 | ribosomal protein S27 like |
| [[DNAI3]] | 0.765 | dynein axonemal intermediate chain 3 |
| [[ZNF423]] | 0.763 | zinc finger protein 423 |
| [[PHLDA3]] | 0.761 | pleckstrin homology like domain family A member 3 |
| [[PPM1D]] | 0.754 | protein phosphatase, Mg2+/Mn2+ dependent 1D |
| [[ZNF79]] | 0.752 | zinc finger protein 79 |
| [[ABCA12]] | 0.744 | ATP binding cassette subfamily A member 12 |
| [[TP53INP1]] | 0.744 | tumor protein p53 inducible nuclear protein 1 |
| [[INKA2]] | 0.739 | inka box actin regulator 2 |
| [[DCP1B]] | 0.738 | decapping mRNA 1B |
| [[ADAMTS7]] | 0.732 | ADAM metallopeptidase with thrombospondin type 1 motif 7 |
| [[TP53I3]] | 0.730 | tumor protein p53 inducible protein 3 |
| [[XPC]] | 0.729 | XPC complex subunit, DNA damage recognition and repair factor |
| [[TYMSOS]] | 0.726 | TYMS opposite strand RNA |
| [[MIR34AHG]] | 0.722 | MIR34A host gene |
| [[BTG2]] | 0.705 | BTG anti-proliferation factor 2 |
| [[SESN1]] | 0.701 | sestrin 1 |
| [[PLCL2]] | 0.680 | phospholipase C like 2 |
| [[FBXO22]] | 0.666 | F-box protein 22 |
| [[GPX1]] | 0.659 | glutathione peroxidase 1 |
| [[PIDD1]] | 0.656 | p53-induced death domain protein 1 |
| [[DOCK8]] | 0.655 | dedicator of cytokinesis 8 |
| [[GAS6-AS1]] | 0.655 | GAS6 antisense RNA 1 |
| [[ACER2]] | 0.653 | alkaline ceramidase 2 |
| [[APOBEC3C]] | 0.652 | apolipoprotein B mRNA editing enzyme catalytic subunit 3C |
| [[BLOC1S2]] | 0.646 | biogenesis of lysosomal organelles complex 1 subunit 2 |
| [[PPP4R3A]] | 0.643 | protein phosphatase 4 regulatory subunit 3A |
| [[POLH]] | 0.641 | DNA polymerase eta |
| [[GLS2]] | 0.639 | glutaminase 2 |
| [[CDKN1A]] | 0.638 | cyclin dependent kinase inhibitor 1A |
| [[INSYN2A]] | 0.631 | inhibitory synaptic factor 2A |
| [[NTN1]] | 0.623 | netrin 1 |
| [[TRIAP1]] | 0.620 | TP53 regulated inhibitor of apoptosis 1 |
| [[GDF15]] | 0.620 | growth differentiation factor 15 |
| [[TIGAR]] | 0.619 | TP53 induced glycolysis regulatory phosphatase |
| [[RETSAT]] | 0.613 | retinol saturase |
| [[REV3L]] | 0.608 | REV3 like, DNA directed polymerase zeta catalytic subunit |
| [[MIR3659HG]] | 0.606 | MIR3659 host gene |
| [[CES2]] | 0.600 | carboxylesterase 2 |
| [[LRATD1]] | 0.600 | LRAT domain containing 1 |
| [[CDIP1]] | 0.597 | cell death inducing p53 target 1 |
| [[NBEAP1]] | 0.593 | neurobeachin pseudogene 1 |
| [[AEN]] | 0.592 | apoptosis enhancing nuclease |
| [[DSC3]] | 0.586 | desmocollin 3 |
| [[EI24]] | 0.579 | EI24 autophagy associated transmembrane protein |
| [[PSTPIP2]] | 0.579 | proline-serine-threonine phosphatase interacting protein 2 |
| [[ISCU]] | 0.575 | iron-sulfur cluster assembly enzyme |
| [[NOPCHAP1]] | 0.575 | NOP protein chaperone 1 |
| [[CYFIP2]] | 0.574 | cytoplasmic FMR1 interacting protein 2 |
| [[RAD51C]] | 0.566 | RAD51 paralog C |
| [[TCAIM]] | 0.541 | T cell activation inhibitor, mitochondrial |
| [[BRMS1L]] | 0.523 | BRMS1 like transcriptional repressor |
| [[ADGRA2]] | 0.522 | adhesion G protein-coupled receptor A2 |
| [[DGKA]] | 0.502 | diacylglycerol kinase alpha |
| [[DDX3Y]] | 0.502 | DEAD-box helicase 3 Y-linked |
| [[PANK1]] | 0.482 | pantothenate kinase 1 |
| [[AK1]] | 0.479 | adenylate kinase 1 |
| [[ASCC3]] | 0.478 | activating signal cointegrator 1 complex subunit 3 |
| [[CEP85L]] | 0.464 | centrosomal protein 85L |
| [[LMCD1-AS1]] | -0.456 | LMCD1 antisense RNA 1 |
| [[UGT2B7]] | 0.433 | UDP glucuronosyltransferase family 2 member B7 |
| [[TCP11L1]] | 0.429 | t-complex 11 like 1 |
| [[BMP1]] | 0.360 | bone morphogenetic protein 1 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 62; `graph/modules.parquet` — module == 62; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [61] (drug-dose × line)
