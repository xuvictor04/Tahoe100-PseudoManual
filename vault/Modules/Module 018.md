---
module: 18
type: "module"
n_genes: 197
n_plus: 190
n_minus: 7
arms_opposite: true
mean_cos_between_arms: -0.22468434274196625
label: "Nucleotide biosynthesis"
label_source: "reactome"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 018

*Nucleotide biosynthesis · 197 genes (190 in the + arm, 7 in the − arm) · [[Module 018.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22). The + arm rises where the − arm falls. Arm = the side of the module's main direction a gene sits on.

Label from the validation stage: **Nucleotide biosynthesis** (reactome, q 0.010; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| + | Nucleotide biosynthesis | reactome | 4/190 | 22.7 | 0.010 |
| all | Nucleotide biosynthesis | reactome | 4/197 | 21.9 | 0.011 |

## Drugs that move it

*Mean pooled z of the + arm minus the − arm (`graph/module_pooled_z.npy`, row 17), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it (+ arm up, − arm down): [[c-Kit-IN-1 (drug)]] 0.05 µM (+7.8, ⚠ unreliable plate only); [[Belumosudil (drug)]] 5 µM (+3.5); [[c-Kit-IN-1 (drug)]] 5 µM (+3.4); [[venetoclax (drug)]] 5 µM (+3.2); [[Dinaciclib (drug)]] 5 µM (+3.1, ⚠ toxic; transcription drop; cell-cycle shift); [[Niclosamide (olamine) (drug)]] 5 µM (+2.6, ⚠ toxic; cell-cycle shift); [[EX229 (drug)]] 5 µM (+2.4); [[Clobetasol propionate (drug)]] 5 µM (+2.4); [[Topotecan (hydrochloride) (drug)]] 0.5 µM (+2.2, ⚠ cell-cycle shift); [[Dexamethasone (drug)]] 5 µM (+2.1); [[Clobetasol propionate (drug)]] 0.05 µM (+1.9); [[Budesonide (drug)]] 5 µM (+1.9); [[TAK-733 (drug)]] 5 µM (+1.9); [[Abemaciclib (drug)]] 0.5 µM (+1.8) (81 in all, 11 with an alert ⚠; shown: the 10 strongest and the 4 next strongest without an alert)
- Lower it: [[Homoharringtonine (drug)]] 5 µM (-23.6, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (-12.0, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (-11.7, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-11.4, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (-11.1, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-9.9, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (-8.7, ⚠ cell-cycle shift); [[Auranofin (drug)]] 5 µM (-5.9); [[TAK-901 (drug)]] 5 µM (-5.1, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (-4.1, ⚠ cell-cycle shift); [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM (-2.9); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (-2.6); [[XRK3F2 (drug)]] 0.5 µM (-2.5); [[GSK1059615 (drug)]] 0.5 µM (-2.5); [[PF-06260933 (drug)]] 5 µM (-2.3); [[Entrectinib (drug)]] 5 µM (-2.1); [[Bimiralisib (drug)]] 0.5 µM (-2.1); [[9-ING-41 (drug)]] 0.5 µM (-2.0); [[Vilanterol (drug)]] 5 µM (-1.8) (67 in all, 21 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[PANC-1 (line)]], [[NCI-H460 (line)]], [[MIA PaCa-2 (line)]], [[SW480 (line)]], [[RKO (line)]], [[LoVo (line)]], [[NCI-H1573 (line)]], [[A549 (line)]]

## Candidate new members

*Members not annotated to the set their arm is enriched for, ranked by mean cos to the annotated members (`validation/novel_members.csv`); ⚠ = a reason to doubt the gene's place (in the vector space only through flagged drug-doses), kept in its rank. 36 candidates, none with an alert; shown: the 15 strongest.*

| # | Gene | Set | Mean cos |
|---|---|---|---|
| 1 | [[MDN1]] | Nucleotide biosynthesis | +0.66 |
| 2 | [[DKC1]] | Nucleotide biosynthesis | +0.66 |
| 3 | [[SEH1L]] | Nucleotide biosynthesis | +0.65 |
| 4 | [[TRAP1]] | Nucleotide biosynthesis | +0.64 |
| 5 | [[URB1]] | Nucleotide biosynthesis | +0.64 |
| 6 | [[ADAT2]] | Nucleotide biosynthesis | +0.61 |
| 7 | [[HEATR1]] | Nucleotide biosynthesis | +0.61 |
| 8 | [[EEF1E1]] | Nucleotide biosynthesis | +0.61 |
| 9 | [[XYLB]] | Nucleotide biosynthesis | +0.60 |
| 10 | [[QSOX2]] | Nucleotide biosynthesis | +0.58 |
| 11 | [[TUBGCP4]] | Nucleotide biosynthesis | +0.58 |
| 12 | [[CARNMT1]] | Nucleotide biosynthesis | +0.58 |
| 13 | [[TCOF1]] | Nucleotide biosynthesis | +0.57 |
| 14 | [[PMS1]] | Nucleotide biosynthesis | +0.57 |
| 15 | [[LETM1]] | Nucleotide biosynthesis | +0.56 |

## + arm (190)

| Gene | Projection | Name |
|---|---|---|
| [[ADCY3]] | 0.847 | adenylate cyclase 3 |
| [[UCK2]] | 0.836 | uridine-cytidine kinase 2 |
| [[MDN1]] | 0.829 | midasin AAA ATPase 1 |
| [[ADAT2]] | 0.820 | adenosine deaminase tRNA specific 2 |
| [[LETM1]] | 0.805 | leucine zipper and EF-hand containing transmembrane protein 1 |
| [[TMTC4]] | 0.805 | transmembrane O-mannosyltransferase targeting cadherins 4 |
| [[DKC1]] | 0.803 | dyskerin pseudouridine synthase 1 |
| [[PUS7]] | 0.794 | pseudouridine synthase 7 |
| [[CAD]] | 0.790 | carbamoyl-phosphate synthetase 2, aspartate transcarbamylase, and dihydroorotase |
| [[EEF1E1]] | 0.784 | eukaryotic translation elongation factor 1 epsilon 1 |
| [[GART]] | 0.781 | phosphoribosylglycinamide formyltransferase, phosphoribosylglycinamide synthetase, phosphoribosylaminoimidazole synthetase |
| [[TCOF1]] | 0.778 | treacle ribosome biogenesis factor 1 |
| [[XPO5]] | 0.773 | exportin 5 |
| [[DTD2]] | 0.772 | D-aminoacyl-tRNA deacylase 2 |
| [[SFXN4]] | 0.764 | sideroflexin 4 |
| [[TUBGCP4]] | 0.755 | tubulin gamma complex component 4 |
| [[UBE2G2]] | 0.747 | ubiquitin conjugating enzyme E2 G2 |
| [[SLC25A15]] | 0.746 | solute carrier family 25 member 15 |
| [[SEH1L]] | 0.745 | SEH1 like nucleoporin |
| [[DDX54]] | 0.744 | DEAD-box helicase 54 |
| [[MACROD1]] | 0.741 | mono-ADP ribosylhydrolase 1 |
| [[ABCC4]] | 0.740 | ATP binding cassette subfamily C member 4 (PEL blood group) |
| [[NUDT3]] | 0.735 | nudix hydrolase 3 |
| [[XYLB]] | 0.727 | xylulokinase |
| [[PMS1]] | 0.725 | PMS1 homolog 1, mismatch repair system component |
| [[HEATR1]] | 0.725 | HEAT repeat containing 1 |
| [[PEMT]] | 0.722 | phosphatidylethanolamine N-methyltransferase |
| [[URB1]] | 0.720 | URB1 ribosome biogenesis factor |
| [[CMTM4]] | 0.717 | CKLF like MARVEL transmembrane domain containing 4 |
| [[PALS2]] | 0.717 | protein associated with LIN7 2, MAGUK p55 family member |
| [[POLR3E]] | 0.714 | RNA polymerase III subunit E |
| [[SORD]] | 0.713 | sorbitol dehydrogenase |
| [[NAE1]] | 0.704 | NEDD8 activating enzyme E1 subunit 1 |
| [[LDLRAD3]] | 0.702 | low density lipoprotein receptor class A domain containing 3 |
| [[EBPL]] | 0.701 | EBP like |
| [[MRPS25]] | 0.701 | mitochondrial ribosomal protein S25 |
| [[PPARGC1B]] | 0.701 | PPARG coactivator 1 beta |
| [[POLR3G]] | 0.696 | RNA polymerase III subunit G |
| [[CARNMT1]] | 0.694 | carnosine N-methyltransferase 1 |
| [[ANAPC1]] | 0.681 | anaphase promoting complex subunit 1 |
| [[WDR12]] | 0.680 | WD repeat domain 12 |
| [[UBE3C]] | 0.668 | ubiquitin protein ligase E3C |
| [[NLN]] | 0.668 | neurolysin |
| [[HEATR3]] | 0.665 | HEAT repeat containing 3 |
| [[CCDC88C]] | 0.660 | coiled-coil and HOOK domain protein 88C |
| [[FAM20B]] | 0.659 | FAM20B glycosaminoglycan xylosylkinase |
| [[RAP1GDS1]] | 0.653 | Rap1 GTPase-GDP dissociation stimulator 1 |
| [[NSMAF]] | 0.649 | neutral sphingomyelinase activation associated factor |
| [[MCM3AP-AS1]] | 0.649 | MCM3AP antisense RNA 1 |
| [[METTL3]] | 0.648 | methyltransferase 3, N6-adenosine-methyltransferase complex catalytic subunit |
| [[PDS5A]] | 0.642 | PDS5 cohesin associated factor A |
| [[CAMKMT]] | 0.640 | calmodulin-lysine N-methyltransferase |
| [[GARNL3]] | 0.635 | GTPase activating Rap/RanGAP domain like 3 |
| [[NT5M]] | 0.634 | 5',3'-nucleotidase, mitochondrial |
| [[USP46]] | 0.633 | ubiquitin specific peptidase 46 |
| [[TRAP1]] | 0.629 | TNF receptor associated protein 1 |
| [[RPUSD4]] | 0.628 | RNA pseudouridine synthase D4 |
| [[GALNT14]] | 0.626 | polypeptide N-acetylgalactosaminyltransferase 14 |
| [[CPNE7]] | 0.625 | copine 7 |
| [[ANKRD13B]] | 0.625 | ankyrin repeat domain 13B |
| [[WNK2]] | 0.622 | WNK lysine deficient protein kinase 2 |
| [[PHKA1]] | 0.620 | phosphorylase kinase regulatory subunit alpha 1 |
| [[LARP1]] | 0.615 | La ribonucleoprotein 1, translational regulator |
| [[ME2]] | 0.615 | malic enzyme 2 |
| [[USP31]] | 0.615 | ubiquitin specific peptidase 31 |
| [[RNASEH2B]] | 0.613 | ribonuclease H2 subunit B |
| [[CENPV]] | 0.612 | centromere protein V |
| [[LRRC8D]] | 0.612 | leucine rich repeat containing 8 VRAC subunit D |
| [[MVB12B]] | 0.608 | multivesicular body subunit 12B |
| [[CHD7]] | 0.606 | chromodomain helicase DNA binding protein 7 |
| [[ZNF749]] | 0.604 | zinc finger protein 749 |
| [[AHCY]] | 0.602 | adenosylhomocysteinase |
| [[ACACA]] | 0.600 | acetyl-CoA carboxylase alpha |
| [[MTERF3]] | 0.600 | mitochondrial transcription termination factor 3 |
| [[ZFYVE9]] | 0.599 | zinc finger FYVE-type containing 9 |
| [[RFT1]] | 0.595 | RFT1 glycolipid translocator homolog |
| [[QSOX2]] | 0.595 | quiescin sulfhydryl oxidase 2 |
| [[KPNA3]] | 0.593 | karyopherin subunit alpha 3 |
| [[POFUT1]] | 0.591 | protein O-fucosyltransferase 1 |
| [[KANK1]] | 0.588 | KN motif and ankyrin repeat domains 1 |
| [[HS6ST2]] | 0.588 | heparan sulfate 6-O-sulfotransferase 2 |
| [[IRAK1]] | 0.586 | interleukin 1 receptor associated kinase 1 |
| [[FAM136A]] | 0.582 | TIM double twin CX3C motif chaperone |
| [[ZC3HAV1L]] | 0.577 | ZC3HAV1 like |
| [[USP45]] | 0.574 | ubiquitin specific peptidase 45 |
| [[TARBP1]] | 0.573 | tRNA guanosine 2 -O-methyltransferase TARBP1 |
| [[TTC13]] | 0.570 | tetratricopeptide repeat domain 13 |
| [[TBC1D4]] | 0.570 | TBC1 domain family member 4 |
| [[GATD1]] | 0.567 | glutamine amidotransferase class 1 domain containing 1 |
| [[AGPAT3]] | 0.566 | 1-acylglycerol-3-phosphate O-acyltransferase 3 |
| [[SMAGP]] | 0.566 | small cell adhesion glycoprotein |
| [[PAM16]] | 0.564 | presequence translocase associated motor 16 |
| [[SPECC1L]] | 0.561 | sperm antigen with calponin homology and coiled-coil domains 1 like |
| [[PRKX]] | 0.561 | protein kinase cAMP-dependent X-linked catalytic subunit |
| [[MTA1]] | 0.560 | metastasis associated 1 |
| [[CMTM8]] | 0.559 | CKLF like MARVEL transmembrane domain containing 8 |
| [[CAMKK2]] | 0.557 | calcium/calmodulin dependent protein kinase kinase 2 |
| [[NCS1]] | 0.556 | neuronal calcium sensor 1 |
| [[CMTM7]] | 0.550 | CKLF like MARVEL transmembrane domain containing 7 |
| [[DAZAP1]] | 0.549 | DAZ associated protein 1 |
| [[CHID1]] | 0.546 | chitinase domain containing 1 |
| [[NPRL3]] | 0.546 | NPR3 like, GATOR1 complex subunit |
| [[FAM120A]] | 0.545 | family with sequence similarity 120 member A |
| [[TOP1MT]] | 0.541 | DNA topoisomerase I mitochondrial |
| [[CLN6]] | 0.540 | CLN6 transmembrane ER protein |
| [[TBC1D30]] | 0.540 | TBC1 domain family member 30 |
| [[FBXL4]] | 0.537 | F-box and leucine rich repeat protein 4 |
| [[CAPN15]] | 0.534 | calpain 15 |
| [[UIMC1]] | 0.534 | ubiquitin interaction motif containing 1 |
| [[TRAF5]] | 0.532 | TNF receptor associated factor 5 |
| [[MTG1]] | 0.531 | mitochondrial ribosome associated GTPase 1 |
| [[ADSL]] | 0.530 | adenylosuccinate lyase |
| [[PDE3B]] | 0.530 | phosphodiesterase 3B |
| [[TCF20]] | 0.529 | transcription factor 20 |
| [[APIP]] | 0.529 | APAF1 interacting protein |
| [[R3HDM1]] | 0.528 | R3H domain containing 1 |
| [[PPAT]] | 0.527 | phosphoribosyl pyrophosphate amidotransferase |
| [[PRELID3A]] | 0.522 | PRELI domain containing 3A |
| [[RILPL1]] | 0.522 | Rab interacting lysosomal protein like 1 |
| [[PTPDC1]] | 0.517 | protein tyrosine phosphatase domain containing 1 |
| [[B3GALNT1]] | 0.517 | beta-1,3-N-acetylgalactosaminyltransferase 1 (Globoside blood group) |
| [[SNX24]] | 0.517 | sorting nexin 24 |
| [[SLC35G1]] | 0.516 | solute carrier family 35 member G1 |
| [[ANP32B]] | 0.514 | acidic nuclear phosphoprotein 32 family member B |
| [[USP2-AS1]] | 0.513 | USP2 antisense RNA 1 |
| [[HDDC2]] | 0.511 | HD domain containing 2 |
| [[SMIM13]] | 0.510 | small integral membrane protein 13 |
| [[GLMN]] | 0.509 | glomulin |
| [[ECPAS]] | 0.507 | Ecm29 proteasome adaptor and scaffold |
| [[RNF125]] | 0.499 | ring finger protein 125 |
| [[OGFOD3]] | 0.496 | 2-oxoglutarate and iron dependent oxygenase domain containing 3 |
| [[CNDP2]] | 0.491 | carnosine dipeptidase 2 |
| [[CLASP2]] | 0.487 | cytoplasmic linker associated protein 2 |
| [[PCOLCE2]] | 0.483 | procollagen C-endopeptidase enhancer 2 |
| [[CTDSPL]] | 0.483 | CTD small phosphatase like |
| [[KIAA1549]] | 0.478 | KIAA1549 |
| [[FAM135A]] | 0.476 | family with sequence similarity 135 member A |
| [[ST6GAL1]] | 0.476 | ST6 beta-galactoside alpha-2,6-sialyltransferase 1 |
| [[TYRO3]] | 0.475 | TYRO3 protein tyrosine kinase |
| [[DTNB]] | 0.475 | dystrobrevin beta |
| [[FAM86DP]] | 0.473 | family with sequence similarity 86 member D, pseudogene |
| [[SLC29A2]] | 0.473 | solute carrier family 29 member 2 |
| [[PAXBP1]] | 0.472 | PAX3 and PAX7 binding protein 1 |
| [[ARHGEF11]] | 0.470 | Rho guanine nucleotide exchange factor 11 |
| [[SFMBT1]] | 0.469 | Scm like with four mbt domains 1 |
| [[GPR63]] | 0.467 | G protein-coupled receptor 63 |
| [[UBE2K]] | 0.461 | ubiquitin conjugating enzyme E2 K |
| [[GLRX3]] | 0.461 | glutaredoxin 3 |
| [[NETO2]] | 0.458 | neuropilin and tolloid like 2 |
| [[ZNRF2P2]] | 0.456 | zinc and ring finger 2 pseudogene 2 |
| [[CDHR3]] | 0.456 | cadherin related family member 3 |
| [[KLHL23]] | 0.454 | kelch like family member 23 |
| [[ARHGAP4]] | 0.447 | Rho GTPase activating protein 4 |
| [[RUSC2]] | 0.438 | RUN and SH3 domain containing 2 |
| [[FAM89A]] | 0.433 | family with sequence similarity 89 member A |
| [[RHBDD1]] | 0.430 | rhomboid domain containing 1 |
| [[MPP3]] | 0.427 | MAGUK p55 scaffold protein 3 |
| [[ALDH5A1]] | 0.426 | aldehyde dehydrogenase 5 family member A1 |
| [[MIPEP]] | 0.425 | mitochondrial intermediate peptidase |
| [[NRF1]] | 0.425 | nuclear respiratory factor 1 |
| [[CBFB]] | 0.422 | core-binding factor subunit beta |
| [[COX10-DT]] | 0.421 | COX10 divergent transcript |
| [[TMEM231]] | 0.417 | transmembrane protein 231 |
| [[PKD2]] | 0.416 | polycystin 2, transient receptor potential cation channel |
| [[PYGO1]] | 0.413 | pygopus family PHD finger 1 |
| [[GTPBP6]] | 0.407 | GTP binding protein 6 |
| [[ARMC10]] | 0.386 | armadillo repeat containing 10 |
| [[DPY19L1P1]] | 0.386 | DPY19L1 pseudogene 1 |
| [[KIF2A]] | 0.385 | kinesin family member 2A |
| [[MOB1B]] | 0.382 | MOB kinase activator 1B |
| [[PTPN4]] | 0.380 | protein tyrosine phosphatase non-receptor type 4 |
| [[SET]] | 0.379 | SET nuclear proto-oncogene |
| [[AKAP7]] | 0.378 | A-kinase anchoring protein 7 |
| [[PABPC4]] | 0.374 | poly(A) binding protein cytoplasmic 4 |
| [[CRTC3]] | 0.374 | CREB regulated transcription coactivator 3 |
| [[MFHAS1]] | 0.368 | multifunctional ROCO family signaling regulator 1 |
| [[MRTFB]] | 0.366 | myocardin related transcription factor B |
| [[TIGD1]] | 0.366 | tigger transposable element derived 1 |
| [[ZNRF2P1]] | 0.355 | zinc and ring finger 2 pseudogene 1 |
| [[MACROH2A2]] | 0.344 | macroH2A.2 histone |
| [[DENR]] | 0.343 | density regulated re-initiation and release factor |
| [[L3MBTL3]] | 0.336 | L3MBTL histone methyl-lysine binding protein 3 |
| [[PCNX1]] | 0.324 | pecanex 1 |
| [[FBXO17]] | 0.300 | F-box protein 17 |
| [[ZNF618]] | 0.299 | zinc finger protein 618 |
| [[LINC00839]] | 0.298 | long independently transcribed non-coding RNA 839 |
| [[GNAQ]] | 0.288 | G protein subunit alpha q |
| [[AHCYL2]] | 0.281 | adenosylhomocysteinase like 2 |
| [[CLCN5]] | 0.279 | Cl-/H+ antiporter 5 |
| [[RAB28]] | 0.207 | RAB28, member RAS oncogene family |

## − arm (7)

| Gene | Projection | Name |
|---|---|---|
| [[TOX4]] | -0.644 | TOX high mobility group box family member 4 |
| [[PDPK1]] | -0.484 | 3-phosphoinositide dependent protein kinase 1 |
| [[DYNLRB1]] | -0.426 | dynein light chain roadblock-type 1 |
| [[CFAP20]] | -0.378 | cilia and flagella associated protein 20 |
| [[ATG12]] | -0.353 | autophagy related 12 |
| [[MFSD11]] | -0.331 | major facilitator superfamily domain containing 11 |
| [[GLCCI1]] | -0.268 | glucocorticoid induced 1 |

## Data

- `graph/nodes.parquet` — module == 18; `graph/modules.parquet` — module == 18; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [17] (drug-dose × line)
