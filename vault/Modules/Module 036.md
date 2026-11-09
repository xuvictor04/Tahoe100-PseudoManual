---
module: 36
type: "module"
n_genes: 135
n_plus: 128
n_minus: 7
arms_opposite: true
mean_cos_between_arms: -0.23120972514152527
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 036

*135 genes (128 in the + arm, 7 in the − arm) · [[Module 036.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23). The + arm rises where the − arm falls. Arm = the side of the module's main direction a gene sits on.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of the + arm minus the − arm (`graph/module_pooled_z.npy`, row 35), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it (+ arm up, − arm down): [[Panobinostat (drug)]] 0.5 µM (+6.6, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (+5.9, ⚠ cell-cycle shift); [[Ixazomib citrate (drug)]] 5 µM (+5.6, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (+5.4, ⚠ cell-cycle shift); [[c-Kit-IN-1 (drug)]] 0.05 µM (+5.3, ⚠ unreliable plate only); [[Bortezomib (drug)]] 0.05 µM (+5.0, ⚠ cell-cycle shift); [[PH-797804 (drug)]] 5 µM (+4.5); [[TAK-901 (drug)]] 5 µM (+4.0, ⚠ cell-cycle shift); [[Belinostat (drug)]] 0.5 µM (+3.9, ⚠ cell-cycle shift); [[Ixazomib citrate (drug)]] 0.5 µM (+3.6); [[Auranofin (drug)]] 5 µM (+3.1); [[Belumosudil (drug)]] 5 µM (+3.0); [[TAK-901 (drug)]] 0.05 µM (+2.5); [[EX229 (drug)]] 5 µM (+2.1); [[c-Kit-IN-1 (drug)]] 5 µM (+2.1); [[TAK-733 (drug)]] 5 µM (+1.9); [[Budesonide (drug)]] 5 µM (+1.9); [[Bortezomib (drug)]] 0.5 µM (+1.8) (57 in all, 22 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)
- Lower it: [[Homoharringtonine (drug)]] 5 µM (-14.4, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-8.1, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (-6.9, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (-5.7); [[Tucidinostat (drug)]] 0.5 µM (-5.6, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-5.4, ⚠ cell-cycle shift); [[Selinexor (drug)]] 5 µM (-5.2, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (-4.7, ⚠ toxic; transcription drop; cell-cycle shift); [[Selinexor (drug)]] 0.5 µM (-3.7, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (-3.5, ⚠ toxic; transcription drop; cell-cycle shift); [[Tucidinostat (drug)]] 0.05 µM (-2.7); [[Cobimetinib (drug)]] 5 µM (-2.6); [[Binimetinib (drug)]] 5 µM (-2.4); [[Binimetinib (drug)]] 0.5 µM (-2.2); [[Entrectinib (drug)]] 5 µM (-2.1); [[Trametinib (drug)]] 0.5 µM (-1.9); [[Osimertinib (mesylate) (drug)]] 5 µM (-1.9); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM (-1.8); [[Radotinib (drug)]] 5 µM (-1.6) (62 in all, 19 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[HOP62 (line)]], [[A498 (line)]], [[A-172 (line)]], [[HS-578T (line)]], [[J82 (line)]], [[PANC-1 (line)]], [[SW480 (line)]], [[AsPC-1 (line)]]

## + arm (128)

| Gene | Projection | Name |
|---|---|---|
| [[HERC2P9]] | 0.851 | HERC2 pseudogene 9 |
| [[HIRA]] | 0.825 | histone cell cycle regulator |
| [[CHCHD6]] | 0.806 | coiled-coil-helix-coiled-coil-helix domain containing 6 |
| [[HERC2P2]] | 0.797 | HERC2 pseudogene 2 |
| [[ZNF496]] | 0.786 | zinc finger protein 496 |
| [[TRAPPC10]] | 0.777 | trafficking protein particle complex subunit 10 |
| [[HERC2]] | 0.773 | HECT and RLD domain containing E3 ubiquitin protein ligase 2 |
| [[HERC2P3]] | 0.765 | HERC2 pseudogene 3 |
| [[EXOC2]] | 0.754 | exocyst complex component 2 |
| [[HSF1]] | 0.750 | heat shock transcription factor 1 |
| [[TOMM40]] | 0.740 | translocase of outer mitochondrial membrane 40 |
| [[TYW1]] | 0.740 | tRNA-yW synthesizing protein 1 homolog |
| [[VKORC1L1]] | 0.718 | vitamin K epoxide reductase complex subunit 1L1 |
| [[ERI3]] | 0.711 | ERI1 exoribonuclease family member 3 |
| [[RNF216]] | 0.711 | ring finger protein 216 |
| [[ZNF767P-1]] | 0.705 | — |
| [[NUP93]] | 0.698 | nucleoporin 93 |
| [[ATAD3A]] | 0.694 | ATPase family AAA domain containing 3A |
| [[EHMT1]] | 0.689 | euchromatic histone lysine methyltransferase 1 |
| [[SPATA5]] | 0.682 | AAA ATPase AFG2A |
| [[NLK]] | 0.677 | nemo like kinase |
| [[XPO4]] | 0.674 | exportin 4 |
| [[SIMC1]] | 0.673 | SUMO interacting motifs containing 1 |
| [[EP400]] | 0.667 | E1A binding protein p400 |
| [[ATAD3B]] | 0.667 | ATPase family AAA domain containing 3B |
| [[EMC8]] | 0.662 | ER membrane protein complex subunit 8 |
| [[NIPA2]] | 0.653 | NIPA magnesium transporter 2 |
| [[ZDHHC5]] | 0.653 | zDHHC palmitoyltransferase 5 |
| [[TIMM23B]] | 0.652 | translocase of inner mitochondrial membrane 23 homolog B |
| [[MTOR]] | 0.650 | mechanistic target of rapamycin kinase |
| [[TREX2]] | 0.649 | three prime repair exonuclease 2 |
| [[PCGF6]] | 0.648 | polycomb group ring finger 6 |
| [[POMT2]] | 0.642 | protein O-mannosyltransferase 2 |
| [[VPS13D]] | 0.642 | vacuolar protein sorting 13 homolog D |
| [[B4GALT2]] | 0.639 | beta-1,4-galactosyltransferase 2 |
| [[KNOP1]] | 0.634 | lysine rich nucleolar protein 1 |
| [[CHUK]] | 0.631 | component of inhibitor of nuclear factor kappa B kinase complex |
| [[DAP3]] | 0.629 | death associated protein 3 |
| [[FBXW11]] | 0.629 | F-box and WD repeat domain containing 11 |
| [[GTF3C2]] | 0.627 | general transcription factor IIIC subunit 2 |
| [[ZBED4]] | 0.625 | zinc finger BED-type containing 4 |
| [[XPO7]] | 0.623 | exportin 7 |
| [[WRN]] | 0.616 | WRN RecQ like helicase |
| [[ERCC3]] | 0.611 | ERCC excision repair 3, TFIIH core complex helicase subunit |
| [[PARGP1]] | 0.608 | PARG pseudogene 1 |
| [[SETD1A]] | 0.608 | SET domain containing 1A, histone lysine methyltransferase |
| [[ZNF551]] | 0.607 | zinc finger protein 551 |
| [[MCM9]] | 0.607 | minichromosome maintenance 9 homologous recombination repair factor |
| [[NDUFS6]] | 0.606 | NADH:ubiquinone oxidoreductase subunit S6 |
| [[TRRAP]] | 0.606 | transformation/transcription domain associated protein |
| [[ARIH2]] | 0.606 | ariadne RBR E3 ubiquitin protein ligase 2 |
| [[SRM]] | 0.605 | spermidine synthase |
| [[PARN]] | 0.604 | poly(A)-specific ribonuclease |
| [[SMG5]] | 0.598 | SMG5 nonsense mediated mRNA decay factor |
| [[RAB5IF]] | 0.598 | RAB5 interacting factor |
| [[UPF1]] | 0.588 | UPF1 RNA helicase and ATPase |
| [[ZNF544]] | 0.585 | zinc finger protein 544 |
| [[THOC5]] | 0.585 | THO complex subunit 5 |
| [[ZNF875]] | 0.580 | zinc finger protein 875 |
| [[COP1]] | 0.576 | COP1 E3 ubiquitin ligase |
| [[ANKS6]] | 0.576 | ankyrin repeat and sterile alpha motif domain containing 6 |
| [[SNRPD3]] | 0.571 | small nuclear ribonucleoprotein D3 polypeptide |
| [[AAGAB]] | 0.568 | alpha and gamma adaptin binding protein |
| [[HERC2P9-1]] | 0.565 | — |
| [[MEF2B]] | 0.564 | myocyte enhancer factor 2B |
| [[NPLOC4]] | 0.562 | NPL4 homolog, ubiquitin recognition factor |
| [[PIK3R4]] | 0.561 | phosphoinositide-3-kinase regulatory subunit 4 |
| [[PSMD1]] | 0.556 | proteasome 26S subunit, non-ATPase 1 |
| [[SLC35C1]] | 0.556 | solute carrier family 35 member C1 |
| [[PYCR3]] | 0.553 | pyrroline-5-carboxylate reductase 3 |
| [[UBAC2]] | 0.550 | UBA domain containing 2 |
| [[FBXL18]] | 0.550 | F-box and leucine rich repeat protein 18 |
| [[AREL1]] | 0.549 | apoptosis resistant E3 ubiquitin protein ligase 1 |
| [[PGP]] | 0.542 | phosphoglycolate phosphatase |
| [[RANBP17]] | 0.540 | RAN binding protein 17 |
| [[ARPC5L]] | 0.539 | actin related protein 2/3 complex subunit 5 like |
| [[DFFB]] | 0.538 | DNA fragmentation factor subunit beta |
| [[NEIL2]] | 0.538 | nei like DNA glycosylase 2 |
| [[NCK2]] | 0.533 | NCK adaptor protein 2 |
| [[IL9RP3]] | 0.530 | IL9R pseudogene 3 |
| [[TRAF3IP1]] | 0.520 | intraflagellar transport 54 |
| [[KLHL18]] | 0.517 | kelch like family member 18 |
| [[KIAA0232]] | 0.517 | KIAA0232 |
| [[BICRA]] | 0.516 | BRD4 interacting chromatin remodeling complex associated protein |
| [[SLC27A5]] | 0.510 | solute carrier family 27 member 5 |
| [[ZNF169]] | 0.506 | zinc finger protein 169 |
| [[MED9]] | 0.505 | mediator complex subunit 9 |
| [[SPHK2]] | 0.500 | sphingosine kinase 2 |
| [[GTF3C3]] | 0.494 | general transcription factor IIIC subunit 3 |
| [[UBE2L3]] | 0.493 | ubiquitin conjugating enzyme E2 L3 |
| [[DNAJC16]] | 0.492 | DnaJ heat shock protein family (Hsp40) member C16 |
| [[EXT2]] | 0.491 | exostosin glycosyltransferase 2 |
| [[PTPMT1]] | 0.489 | protein tyrosine phosphatase mitochondrial 1 |
| [[PCSK7]] | 0.484 | proprotein convertase subtilisin/kexin type 7 |
| [[MED27]] | 0.475 | mediator complex subunit 27 |
| [[DTNBP1]] | 0.473 | dystrobrevin binding protein 1 |
| [[E2F6]] | 0.467 | E2F transcription factor 6 |
| [[BAG5]] | 0.464 | BAG cochaperone 5 |
| [[DDX46]] | 0.464 | DEAD-box helicase 46 |
| [[DNAJC17]] | 0.462 | DnaJ heat shock protein family (Hsp40) member C17 |
| [[RAB35]] | 0.459 | RAB35, member RAS oncogene family |
| [[RALGAPB]] | 0.457 | Ral GTPase activating protein non-catalytic subunit beta |
| [[CHERP]] | 0.453 | calcium homeostasis endoplasmic reticulum protein |
| [[JRK]] | 0.451 | Jrk helix-turn-helix protein |
| [[TTC7B]] | 0.448 | tetratricopeptide repeat domain 7B |
| [[TAF6L]] | 0.441 | TATA-box binding protein associated factor 6 like |
| [[TRAPPC9]] | 0.441 | trafficking protein particle complex subunit 9 |
| [[SLC25A10]] | 0.434 | solute carrier family 25 member 10 |
| [[SMIM7]] | 0.431 | small integral membrane protein 7 |
| [[SLC7A6]] | 0.424 | solute carrier family 7 member 6 |
| [[ENTPD5]] | 0.418 | ectonucleoside triphosphate diphosphohydrolase 5 |
| [[ZNF324B]] | 0.399 | zinc finger protein 324B |
| [[ABCA3]] | 0.392 | ATP binding cassette subfamily A member 3 |
| [[ATP6V0A2]] | 0.386 | ATPase H+ transporting V0 subunit a2 |
| [[ZNF473]] | 0.376 | zinc finger protein 473 |
| [[C16orf95]] | 0.361 | chromosome 16 open reading frame 95 |
| [[VPS45]] | 0.340 | vacuolar protein sorting 45 homolog |
| [[ALG14]] | 0.339 | ALG14 UDP-N-acetylglucosaminyltransferase subunit |
| [[SH3BP4]] | 0.330 | SH3 domain binding protein 4 |
| [[CCDC66]] | 0.323 | coiled-coil domain containing 66 |
| [[ARAP3]] | 0.318 | ArfGAP with RhoGAP domain, ankyrin repeat and PH domain 3 |
| [[NEK4]] | 0.314 | NIMA related kinase 4 |
| [[VPS9D1]] | 0.248 | VPS9 domain containing 1 |
| [[PRR12]] | 0.244 | proline rich 12 |
| [[NAGLU]] | 0.239 | N-acetyl-alpha-glucosaminidase |
| [[ZFAT]] | 0.199 | zinc finger and AT-hook domain containing |
| [[C22orf39]] | 0.147 | chromosome 22 open reading frame 39 |
| [[AVL9]] | 0.145 | AVL9 cell migration associated |

## − arm (7)

| Gene | Projection | Name |
|---|---|---|
| [[SDCBP]] | -0.689 | syndecan binding protein |
| [[ZNF821]] | -0.529 | zinc finger protein 821 |
| [[SETDB2]] | -0.462 | SET domain bifurcated histone lysine methyltransferase 2 |
| [[MATCAP2]] | -0.456 | microtubule associated tyrosine carboxypeptidase 2 |
| [[P2RX4]] | -0.398 | purinergic receptor P2X 4 |
| [[S100A10]] | -0.294 | S100 calcium binding protein A10 |
| [[KLHL3]] | -0.191 | kelch like family member 3 |

## Data

- `graph/nodes.parquet` — module == 36; `graph/modules.parquet` — module == 36; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [35] (drug-dose × line)
