---
module: 10
type: "module"
n_genes: 217
n_plus: 205
n_minus: 12
arms_opposite: true
mean_cos_between_arms: -0.3231571912765503
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 010

*217 genes (205 in the + arm, 12 in the − arm) · [[Module 010.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32). The + arm rises where the − arm falls. Arm = the side of the module's main direction a gene sits on.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of the + arm minus the − arm (`graph/module_pooled_z.npy`, row 9), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it (+ arm up, − arm down): [[Homoharringtonine (drug)]] 5 µM (+15.6, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (+13.5, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+11.0, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (+10.3, ⚠ toxic; transcription drop; cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (+9.9, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (+9.7, ⚠ toxic; transcription drop; cell-cycle shift); [[Harringtonine (drug)]] 5 µM (+9.0, ⚠ cell-cycle shift); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+6.9); [[Harringtonine (drug)]] 0.5 µM (+6.5, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.05 µM (+5.8); [[Belumosudil (drug)]] 5 µM (+5.3); [[Auranofin (drug)]] 5 µM (+4.8); [[Filgotinib (drug)]] 5 µM (+3.8); [[Harringtonine (drug)]] 0.05 µM (+3.5); [[Trametinib (drug)]] 0.5 µM (+3.0); [[Temsirolimus (drug)]] 0.05 µM (+2.8); [[Cobimetinib (drug)]] 0.5 µM (+2.8); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM (+2.7) (150 in all, 35 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)
- Lower it: [[Belinostat (drug)]] 5 µM (-14.6, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (-13.6, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (-13.3, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (-8.0, ⚠ cell-cycle shift); [[Belinostat (drug)]] 0.5 µM (-7.4, ⚠ cell-cycle shift); [[Brivudine (drug)]] 5 µM (-5.8); [[c-Kit-IN-1 (drug)]] 0.05 µM (-4.8, ⚠ unreliable plate only); [[Digitoxin (drug)]] 0.5 µM (-4.8, ⚠ cell-cycle shift); [[Ixazomib citrate (drug)]] 5 µM (-4.5, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (-4.4, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (-4.2); [[Abemaciclib (drug)]] 0.5 µM (-3.6); [[HI-TOPK-032 (drug)]] 5 µM (-2.8); [[Niclosamide (olamine) (drug)]] 0.5 µM (-2.7); [[Abemaciclib (drug)]] 5 µM (-2.6); [[Sapanisertib (drug)]] 0.5 µM (-2.4); [[Belinostat (drug)]] 0.05 µM (-2.3); [[Brivudine (drug)]] 0.5 µM (-2.2); [[Tomivosertib (drug)]] 5 µM (-2.2) (117 in all, 22 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[LoVo (line)]], [[NCI-H460 (line)]], [[SW480 (line)]], [[PANC-1 (line)]], [[NCI-H2347 (line)]], [[HEC-1-A (line)]], [[RKO (line)]], [[SW1417 (line)]]

## + arm (205)

| Gene | Projection | Name |
|---|---|---|
| [[PCNX4-DT]] | 0.897 | PCNX4 divergent transcript |
| [[TMEM202-AS1]] | 0.885 | TMEM202 antisense RNA 1 |
| [[LINC00240]] | 0.858 | long independently transcribed non-coding RNA 240 |
| [[DPH6-DT]] | 0.857 | DPH6 divergent transcript |
| [[MAD2L1-DT]] | 0.853 | MAD2L1 divergent transcript |
| [[PDCL3P4]] | 0.851 | PDCL3 pseudogene 4 |
| [[ANKRD31]] | 0.843 | ankyrin repeat domain 31 |
| [[F8]] | 0.842 | coagulation factor VIII |
| [[LEKR1]] | 0.836 | leucine, glutamate and lysine rich 1 |
| [[USP38-DT]] | 0.827 | USP38 divergent transcript |
| [[BDNF-AS]] | 0.814 | BDNF antisense RNA |
| [[EIF1B-AS1]] | 0.814 | — |
| [[FAM227B]] | 0.806 | family with sequence similarity 227 member B |
| [[ZNF747]] | 0.803 | zinc finger protein 747 |
| [[KRBA2]] | 0.802 | KRAB domain containing 2 |
| [[PPP3CB-AS1]] | 0.800 | PPP3CB antisense RNA 1 |
| [[IQCH-AS1]] | 0.800 | IQCH antisense RNA 1 |
| [[KRCC1]] | 0.799 | lysine rich coiled-coil 1 |
| [[TAFA2]] | 0.798 | TAFA chemokine like family member 2 |
| [[PLBD1-AS1]] | 0.798 | PLBD1 antisense RNA 1 |
| [[FRG1-DT]] | 0.798 | FRG1 divergent transcript |
| [[RAP2C-AS1]] | 0.798 | RAP2C antisense RNA 1 |
| [[TMEM9B-AS1]] | 0.797 | TMEM9B antisense RNA 1 |
| [[FBXO38-DT]] | 0.792 | FBXO38 divergent transcript |
| [[IDNK]] | 0.791 | IDNK gluconokinase |
| [[RNF32]] | 0.788 | ring finger protein 32 |
| [[SUCLG2-DT]] | 0.787 | SUCLG2 divergent transcript |
| [[RBM26-AS1]] | 0.785 | RBM26 antisense RNA 1 |
| [[GUCY2C-AS1]] | 0.784 | GUCY2C antisense RNA 1 |
| [[CTBP1-DT]] | 0.782 | CTBP1 divergent transcript |
| [[UFL1-AS1]] | 0.779 | UFL1 antisense RNA 1 |
| [[ARRDC3-AS1]] | 0.774 | ARRDC3 antisense RNA 1 |
| [[ZNF407-AS1]] | 0.770 | ZNF407 antisense RNA 1 |
| [[ZBED5-AS1]] | 0.769 | ZBED5 antisense RNA 1 |
| [[LINC00667]] | 0.767 | long independently transcribed non-coding RNA 667 |
| [[AK9]] | 0.762 | adenylate kinase 9 |
| [[TRAM2-AS1]] | 0.761 | TRAM2 antisense RNA 1 |
| [[AGA-DT]] | 0.759 | AGA divergent transcript |
| [[ZRANB2-DT]] | 0.758 | ZRANB2 divergent transcript |
| [[TIGD6]] | 0.758 | tigger transposable element derived 6 |
| [[BCDIN3D]] | 0.758 | BCDIN3 domain containing RNA methyltransferase |
| [[LINC02340]] | 0.756 | — |
| [[THBS4]] | 0.754 | thrombospondin 4 |
| [[CAPN3]] | 0.751 | calpain 3 |
| [[STPG2]] | 0.751 | sperm tail PG-rich repeat containing 2 |
| [[ACAD9-DT]] | 0.749 | ACAD9 divergent transcript |
| [[TMEM232]] | 0.746 | transmembrane protein 232 |
| [[GAS2]] | 0.734 | growth arrest specific 2 |
| [[LRRIQ3]] | 0.734 | leucine rich repeats and IQ motif containing 3 |
| [[MYL5]] | 0.731 | myosin light chain 5 |
| [[LINC00886]] | 0.730 | long independently transcribed non-coding RNA 886 |
| [[PGBD4]] | 0.722 | piggyBac transposable element derived 4 |
| [[KATNAL2]] | 0.718 | katanin catalytic subunit A1 like 2 |
| [[TSGA10]] | 0.714 | testis specific 10 |
| [[CCNT2]] | 0.712 | cyclin T2 |
| [[LINC00174]] | 0.712 | long independently transcribed non-coding RNA 174 |
| [[EFCAB6]] | 0.707 | EF-hand calcium binding domain 6 |
| [[ZMAT1]] | 0.706 | zinc finger matrin-type 1 |
| [[CYP1B1-AS1]] | 0.702 | CYP1B1 antisense RNA 1 |
| [[THNSL2]] | 0.700 | threonine synthase like 2 |
| [[TAPT1-AS1]] | 0.696 | TAPT1 antisense RNA 1 |
| [[ZNF610]] | 0.694 | zinc finger protein 610 |
| [[ZSCAN30]] | 0.694 | zinc finger and SCAN domain containing 30 |
| [[CARF]] | 0.690 | calcium responsive transcription factor |
| [[KLHDC1]] | 0.686 | kelch domain containing 1 |
| [[LINC01376]] | 0.684 | long independently transcribed non-coding RNA 1376 |
| [[ATP1A1-AS1]] | 0.682 | ATP1A1 antisense RNA 1 |
| [[GUCY1B2]] | 0.675 | guanylate cyclase 1 soluble subunit beta 2 (pseudogene) |
| [[SMIM19]] | 0.672 | small integral membrane protein 19 |
| [[FLG-AS1]] | 0.672 | cervical cancer associated DHX9 suppressive transcript |
| [[CRB1]] | 0.668 | crumbs cell polarity complex component 1 |
| [[FBXO4]] | 0.664 | F-box protein 4 |
| [[FAM66C]] | 0.664 | family with sequence similarity 66 member C |
| [[ZNF429]] | 0.661 | zinc finger protein 429 |
| [[C5]] | 0.660 | complement C5 |
| [[AJUBA-DT]] | 0.653 | AJUBA divergent transcript |
| [[ARHGEF37]] | 0.649 | Rho guanine nucleotide exchange factor 37 |
| [[PPEF1]] | 0.649 | protein phosphatase with EF-hand domain 1 |
| [[PDIA3P1]] | 0.644 | protein disulfide isomerase family A member 3 pseudogene 1 |
| [[LINC02615]] | 0.643 | long independently transcribed non-coding RNA 2615 |
| [[FAM174A-DT]] | 0.642 | FAM174A divergent transcript |
| [[LINC01725]] | 0.642 | long independently transcribed non-coding RNA 1725 |
| [[NEMP2-DT]] | 0.639 | NEMP2 divergent transcript |
| [[KCNMB2-AS1]] | 0.639 | KCNMB2 antisense RNA 1 |
| [[NPAS3]] | 0.639 | neuronal PAS domain protein 3 |
| [[CYP4V2]] | 0.639 | cytochrome P450 family 4 subfamily V member 2 |
| [[LINC01569]] | 0.638 | long independently transcribed non-coding RNA 1569 |
| [[CLIC2]] | 0.633 | CLIC family member 2 |
| [[FAM120AOS]] | 0.629 | family with sequence similarity 120 member A opposite strand |
| [[FTCDNL1]] | 0.627 | formiminotransferase cyclodeaminase N-terminal like |
| [[MIR1915HG]] | 0.627 | MIR1915 host gene |
| [[CHKB-DT]] | 0.625 | CHKB divergent transcript |
| [[LINC02542]] | 0.625 | long independently transcribed non-coding RNA 2542 |
| [[KCNMB3]] | 0.622 | potassium calcium-activated channel subfamily M regulatory beta subunit 3 |
| [[TPRG1]] | 0.622 | tumor protein p63 regulated 1 |
| [[SCGB2B2]] | 0.618 | secretoglobin family 2B member 2 |
| [[TMEM44-AS1]] | 0.618 | TMEM44 antisense RNA 1 |
| [[ANKRD20A21P]] | 0.615 | ankyrin repeat domain 20 family member A21, pseudogene |
| [[SLC38A4-AS1]] | 0.615 | SLC38A4 antisense RNA 1 |
| [[TYSND1]] | 0.613 | trypsin like peroxisomal matrix peptidase 1 |
| [[CFLAR]] | 0.612 | CASP8 and FADD like apoptosis regulator |
| [[LINC00412]] | 0.612 | long independently transcribed non-coding RNA 412 |
| [[ZNF818P]] | 0.607 | zinc finger protein 818, pseudogene |
| [[RP1]] | 0.600 | RP1 axonemal microtubule associated |
| [[LINC03015]] | 0.596 | long independently transcribed non-coding RNA 3015 |
| [[SRP14-DT]] | 0.596 | SRP14 divergent transcript |
| [[LINC00663]] | 0.587 | long independently transcribed non-coding RNA 663 |
| [[CUTALP]] | 0.583 | cutA divalent cation tolerance like, pseudogene |
| [[FMO4]] | 0.581 | flavin containing dimethylaniline monoxygenase 4 |
| [[ARSD]] | 0.576 | arylsulfatase D |
| [[LINC02175]] | 0.576 | long independently transcribed non-coding RNA 2175 |
| [[PKD2L2-DT]] | 0.574 | PKD2L2 divergent transcript |
| [[LINC02026]] | 0.574 | long independently transcribed non-coding RNA 2026 |
| [[ZNF717]] | 0.566 | zinc finger protein 717 |
| [[RNLS]] | 0.566 | renalase, FAD dependent amine oxidase |
| [[OTUD4]] | 0.565 | OTU deubiquitinase 4 |
| [[ZNF19]] | 0.563 | zinc finger protein 19 |
| [[WDR5B]] | 0.562 | WD repeat domain 5B |
| [[HECTD2]] | 0.562 | HECT domain E3 ubiquitin protein ligase 2 |
| [[ABCA6]] | 0.562 | ATP binding cassette subfamily A member 6 |
| [[LNC-LBCS]] | 0.561 | lncRNA bladder and prostate cancer suppressor, hnRNPK interacting |
| [[ZIC1]] | 0.557 | Zic family zinc finger 1 |
| [[ADAL]] | 0.555 | N6-Methyl-AMP deaminase |
| [[MRAS]] | 0.553 | muscle RAS oncogene homolog |
| [[LRIG3-DT]] | 0.551 | LRIG3 divergent transcript |
| [[JHY]] | 0.549 | junctional cadherin complex regulator |
| [[KIAA0825]] | 0.549 | KIAA0825 |
| [[ANKRD18CP]] | 0.549 | ankyrin repeat domain 18C, pseudogene |
| [[LRRC17]] | 0.547 | leucine rich repeat containing 17 |
| [[ANKS1B]] | 0.544 | ankyrin repeat and sterile alpha motif domain containing 1B |
| [[AK8]] | 0.536 | adenylate kinase 8 |
| [[CNN3-DT]] | 0.535 | CNN3 divergent transcript |
| [[RNASEH1-DT]] | 0.535 | RNASEH1 divergent transcript |
| [[AGBL2]] | 0.533 | AGBL carboxypeptidase 2 |
| [[CNTLN]] | 0.533 | centlein |
| [[ID2-AS1]] | 0.528 | ID2 antisense RNA 1 |
| [[OMA1]] | 0.526 | OMA1 zinc metallopeptidase |
| [[LINC00466]] | 0.523 | long independently transcribed non-coding RNA 466 |
| [[PRECSIT]] | 0.523 | p53 regulated carcinoma associated Stat3 activating long intergenic non-protein coding transcript |
| [[LINC01088]] | 0.522 | long independently transcribed non-coding RNA 1088 |
| [[LINC02966]] | 0.518 | long independently transcribed non-coding RNA 2966 |
| [[MAPK8IP2]] | 0.516 | mitogen-activated protein kinase 8 interacting protein 2 |
| [[ZFP2]] | 0.514 | ZFP2 zinc finger protein |
| [[NECTIN3-AS1]] | 0.509 | NECTIN3 antisense RNA 1 |
| [[STOX1]] | 0.508 | storkhead box 1 |
| [[BEND6]] | 0.503 | BEN domain containing 6 |
| [[PRR3]] | 0.503 | proline rich 3 |
| [[SPAG16]] | 0.502 | sperm associated antigen 16 |
| [[TSPYL4]] | 0.502 | TSPY like 4 |
| [[SYT9-AS1]] | 0.501 | SYT9 antisense RNA 1 |
| [[RIMS2]] | 0.494 | regulating synaptic membrane exocytosis 2 |
| [[BBOX1-AS1]] | 0.491 | BBOX1 antisense RNA 1 |
| [[NAALADL2]] | 0.490 | N-acetylated alpha-linked acidic dipeptidase like 2 |
| [[LRRC51]] | 0.489 | leucine rich repeat containing 51 |
| [[MMP25-AS1]] | 0.488 | MMP25 antisense RNA 1 |
| [[KDM4D]] | 0.486 | lysine demethylase 4D |
| [[ABCA17P]] | 0.482 | ATP binding cassette subfamily A member 17, pseudogene |
| [[ADAMTS13]] | 0.479 | ADAM metallopeptidase with thrombospondin type 1 motif 13 |
| [[TMEM69]] | 0.476 | transmembrane protein 69 |
| [[LINC01013]] | 0.474 | long independently transcribed non-coding RNA 1013 |
| [[ATP6V1E2]] | 0.473 | ATPase H+ transporting V1 subunit E2 |
| [[LRRK2]] | 0.471 | leucine rich repeat kinase 2 |
| [[SIRT5]] | 0.471 | sirtuin 5 |
| [[FZD4-DT]] | 0.459 | FZD4 divergent transcript |
| [[GANC]] | 0.458 | glucosidase alpha, neutral C |
| [[CCT6P3]] | 0.456 | chaperonin containing TCP1 family member 6A3, pseudogene |
| [[DHRS4L2]] | 0.456 | dehydrogenase/reductase 4 like 2 |
| [[SUMF1]] | 0.450 | sulfatase modifying factor 1 |
| [[CCDC191]] | 0.447 | coiled-coil domain containing 191 |
| [[HENMT1]] | 0.446 | HEN methyltransferase 1 |
| [[TIPIN]] | 0.445 | TIMELESS interacting protein |
| [[GPLD1]] | 0.434 | glycosylphosphatidylinositol specific phospholipase D1 |
| [[TMCC1-DT]] | 0.425 | TMCC1 divergent transcript |
| [[SPATA17]] | 0.424 | spermatogenesis associated 17 |
| [[LMO7-AS1]] | 0.415 | LMO7 antisense RNA 1 |
| [[GMDS-DT]] | 0.413 | GMDS divergent transcript |
| [[ATXN1-AS1]] | 0.398 | ATXN1 antisense RNA 1 |
| [[ANKRD20A11P]] | 0.398 | ankyrin repeat domain 20 family member A11, pseudogene |
| [[ERICH6-AS1]] | 0.393 | ERICH6 antisense RNA 1 |
| [[ITGB2]] | 0.392 | integrin subunit beta 2 |
| [[CASC2]] | 0.388 | cancer susceptibility 2 |
| [[ATP6AP1L]] | 0.386 | ATPase H+ transporting accessory protein 1 like (pseudogene) |
| [[FAXC]] | 0.382 | failed axon connections homolog, metaxin like GST domain containing |
| [[WDR31]] | 0.378 | WD repeat domain 31 |
| [[SYCP2]] | 0.374 | synaptonemal complex protein 2 |
| [[C11orf65]] | 0.367 | chromosome 11 open reading frame 65 |
| [[DANT1]] | 0.359 | DXZ4 associated non-coding transcript 1, proximal |
| [[B4GAT1-DT]] | 0.355 | B4GAT1 divergent transcript |
| [[RDM1P5]] | 0.352 | RDM1 pseudogene 5 |
| [[SAMD11]] | 0.340 | sterile alpha motif domain containing 11 |
| [[CHST14]] | 0.332 | carbohydrate sulfotransferase 14 |
| [[MIR130AHG]] | 0.331 | MIR130A host gene |
| [[CCDC171]] | 0.313 | coiled-coil domain containing 171 |
| [[GCAWKR]] | 0.311 | gastric cancer associated WDR5 and KAT2A binding lncRNA |
| [[FBXO15]] | 0.306 | F-box protein 15 |
| [[DLGAP1-AS1]] | 0.277 | DLGAP1 antisense RNA 1 |
| [[KLHL14]] | 0.274 | kelch like family member 14 |
| [[DCDC1]] | 0.270 | doublecortin domain containing 1 |
| [[SSPOP]] | 0.251 | SCO-spondin, pseudogene |
| [[CCDC7]] | 0.236 | coiled-coil domain containing 7 |
| [[HOXC4]] | 0.215 | homeobox C4 |
| [[D2HGDH]] | 0.201 | D-2-hydroxyglutarate dehydrogenase |
| [[TMEM139-AS1]] | 0.192 | TMEM139 antisense RNA 1 |
| [[PRKN]] | 0.179 | parkin RBR E3 ubiquitin protein ligase |
| [[FLJ12825]] | 0.154 | — |

## − arm (12)

| Gene | Projection | Name |
|---|---|---|
| [[L2HGDH]] | -0.694 | L-2-hydroxyglutarate dehydrogenase |
| [[FAM118A]] | -0.691 | SIR2 antiphage like 2 |
| [[CCDC134]] | -0.636 | coiled-coil domain containing 134 |
| [[KLHL8]] | -0.622 | kelch like family member 8 |
| [[CLTCL1]] | -0.608 | clathrin heavy chain like 1 |
| [[AP1S1]] | -0.598 | adaptor related protein complex 1 subunit sigma 1 |
| [[KYAT1]] | -0.595 | kynurenine aminotransferase 1 |
| [[NR2C1]] | -0.588 | nuclear receptor subfamily 2 group C member 1 |
| [[ABHD6]] | -0.572 | abhydrolase domain containing 6, acylglycerol lipase |
| [[TPMT]] | -0.490 | thiopurine S-methyltransferase |
| [[FLVCR1]] | -0.455 | FLVCR choline and heme transporter 1 |
| [[EVL]] | -0.381 | Enah/Vasp-like |

## Data

- `graph/nodes.parquet` — module == 10; `graph/modules.parquet` — module == 10; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [9] (drug-dose × line)
