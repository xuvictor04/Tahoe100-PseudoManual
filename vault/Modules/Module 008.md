---
module: 8
type: "module"
n_genes: 228
n_plus: 228
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.22885668277740479
label: "Dectin-2 family"
label_source: "reactome"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 008

*Dectin-2 family · 228 genes (single-armed) · [[Module 008.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

Label from the validation stage: **Dectin-2 family** (reactome, q 0.002; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | Dectin-2 family | reactome | 5/228 | 19.4 | 0.002 |
| + | Dectin-2 family | reactome | 5/228 | 19.4 | 0.002 |
| all | O-linked glycosylation of mucins | reactome | 7/228 | 8.73 | 0.007 |
| + | O-linked glycosylation of mucins | reactome | 7/228 | 8.73 | 0.007 |
| all | Defective GALNT3 causes HFTC | reactome | 4/228 | 20.3 | 0.014 |
| + | Defective GALNT3 causes HFTC | reactome | 4/228 | 20.3 | 0.014 |
| + | Defective GALNT12 causes CRCS1 | reactome | 4/228 | 20.3 | 0.014 |
| all | Defective GALNT12 causes CRCS1 | reactome | 4/228 | 20.3 | 0.014 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 7), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Dinaciclib (drug)]] 5 µM (+6.9, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (+6.7, ⚠ toxic; transcription drop; cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (+5.4); [[Idarubicin (hydrochloride) (drug)]] 5 µM (+5.1, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+4.7, ⚠ toxic; transcription drop; cell-cycle shift); [[Tucidinostat (drug)]] 0.5 µM (+3.8, ⚠ cell-cycle shift); [[Trametinib (drug)]] 0.5 µM (+2.5); [[Cobimetinib (drug)]] 5 µM (+2.5); [[Binimetinib (drug)]] 5 µM (+2.2); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM (+2.1); [[Cobimetinib (drug)]] 0.5 µM (+1.8); [[Binimetinib (drug)]] 0.5 µM (+1.8); [[Binimetinib (drug)]] 0.05 µM (+1.8); [[Ipatasertib (drug)]] 0.5 µM (+1.7); [[Elimusertib hydrochloride (drug)]] 0.05 µM (+1.7) (50 in all, 15 with an alert ⚠; shown: the 10 strongest and the 5 next strongest without an alert)
- Lower it: [[Digitoxin (drug)]] 0.5 µM (-3.8, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (-3.6, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (-2.6, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-2.5, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (-2.3, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-2.3, ⚠ cell-cycle shift); [[c-Kit-IN-1 (drug)]] 0.05 µM (-2.3, ⚠ unreliable plate only); [[Harringtonine (drug)]] 0.5 µM (-2.1, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (-2.1, ⚠ cell-cycle shift); [[Mebendazole (drug)]] 5 µM (-2.0); [[PH-797804 (drug)]] 5 µM (-1.7); [[Ixazomib citrate (drug)]] 0.5 µM (-1.5); [[Abemaciclib (drug)]] 5 µM (-1.4); [[Abemaciclib (drug)]] 0.5 µM (-1.3); [[Lucanthone (drug)]] 0.05 µM (-1.3); [[BAY1125976 (drug)]] 5 µM (-1.3); [[Dexamethasone (drug)]] 0.5 µM (-1.2); [[Rutin (trihydrate) (drug)]] 0.05 µM (-1.2); [[Dabrafenib (drug)]] 5 µM (-1.2) (38 in all, 17 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[COLO 205 (line)]], [[LoVo (line)]], [[LS 180 (line)]], [[KATO III (line)]], [[HT-29 (line)]], [[NCI-H23 (line)]], [[RKO (line)]], [[Panc 03.27 (line)]]

## Candidate new members

*Members not annotated to the set their arm is enriched for, ranked by mean cos to the annotated members (`validation/novel_members.csv`); ⚠ = a reason to doubt the gene's place (in the vector space only through flagged drug-doses), kept in its rank. 30 candidates, none with an alert; shown: the 15 strongest.*

| # | Gene | Set | Mean cos |
|---|---|---|---|
| 1 | [[PDZK1IP1]] | Dectin-2 family | +0.63 |
| 2 | [[TRIM31]] | Dectin-2 family | +0.60 |
| 3 | [[MMP7]] | Dectin-2 family | +0.59 |
| 4 | [[SLC44A4]] | O-linked glycosylation of mucins | +0.59 |
| 5 | [[RBM47]] | Dectin-2 family | +0.58 |
| 6 | [[BCL2L15]] | Dectin-2 family | +0.58 |
| 7 | [[SAMD12-AS1]] | Dectin-2 family | +0.57 |
| 8 | [[TMC5]] | Dectin-2 family | +0.56 |
| 9 | [[ST14]] | Dectin-2 family | +0.56 |
| 10 | [[ALOX5]] | Dectin-2 family | +0.56 |
| 11 | [[SLC34A2]] | Dectin-2 family | +0.56 |
| 12 | [[CLIC5]] | O-linked glycosylation of mucins | +0.55 |
| 13 | [[ADGRF1]] | Dectin-2 family | +0.55 |
| 14 | [[TC2N]] | O-linked glycosylation of mucins | +0.55 |
| 15 | [[GABRP]] | O-linked glycosylation of mucins | +0.55 |

## + arm (228)

| Gene | Projection | Name |
|---|---|---|
| [[SLC44A4]] | 0.847 | solute carrier family 44 member 4 |
| [[BCL2L15]] | 0.834 | BCL2 like 15 |
| [[POF1B]] | 0.825 | POF1B actin binding protein |
| [[ST14]] | 0.822 | ST14 transmembrane serine protease matriptase |
| [[TRIM31]] | 0.818 | tripartite motif containing 31 |
| [[MUC4]] | 0.808 | mucin 4, cell surface associated |
| [[ADGRF1]] | 0.806 | adhesion G protein-coupled receptor F1 |
| [[PROM1]] | 0.796 | prominin 1 |
| [[SPATA6L]] | 0.791 | spermatogenesis associated 6 like |
| [[TC2N]] | 0.787 | tandem C2 domains, nuclear |
| [[TOX3]] | 0.786 | TOX high mobility group box family member 3 |
| [[SAMD12-AS1]] | 0.784 | SAMD12 antisense RNA 1 |
| [[BCAS1]] | 0.783 | brain enriched myelin associated protein 1 |
| [[CATSPERB]] | 0.780 | catsper channel auxiliary subunit beta |
| [[ARHGEF38]] | 0.780 | Rho guanine nucleotide exchange factor 38 |
| [[RBM47]] | 0.780 | RNA binding motif protein 47 |
| [[TMC4]] | 0.777 | transmembrane channel like 4 |
| [[ITGB6]] | 0.774 | integrin subunit beta 6 |
| [[TMPRSS3]] | 0.771 | transmembrane serine protease 3 |
| [[CLIC5]] | 0.771 | CLIC family member 5 |
| [[ADCY4]] | 0.764 | adenylate cyclase 4 |
| [[MMP7]] | 0.764 | matrix metallopeptidase 7 |
| [[ALOX5]] | 0.763 | arachidonate 5-lipoxygenase |
| [[TMC5]] | 0.763 | transmembrane channel like 5 |
| [[FRK]] | 0.760 | fyn related Src family tyrosine kinase |
| [[PLCH1]] | 0.758 | phospholipase C eta 1 |
| [[TMPRSS2]] | 0.755 | transmembrane serine protease 2 |
| [[TMEM45B]] | 0.754 | transmembrane protein 45B |
| [[PDZK1IP1]] | 0.753 | PDZK1 interacting protein 1 |
| [[FAAH2]] | 0.752 | fatty acid amide hydrolase 2 |
| [[GCNT3]] | 0.748 | glucosaminyl (N-acetyl) transferase 3, mucin type |
| [[HHLA2]] | 0.733 | HHLA2 member of B7 family |
| [[ERBB3]] | 0.732 | erb-b2 receptor tyrosine kinase 3 |
| [[RNF183]] | 0.726 | ring finger protein 183 |
| [[MUC20]] | 0.724 | mucin 20, cell surface associated |
| [[HSH2D]] | 0.722 | hematopoietic SH2 domain containing |
| [[SIDT1]] | 0.717 | SID1 transmembrane family member 1 |
| [[SLC44A3]] | 0.714 | solute carrier family 44 member 3 |
| [[OCLN]] | 0.712 | occludin |
| [[ELF3-AS1]] | 0.711 | ELF3 antisense RNA 1 |
| [[ARSL]] | 0.710 | arylsulfatase L |
| [[GABRP]] | 0.707 | gamma-aminobutyric acid type A receptor subunit pi |
| [[MUC16]] | 0.706 | mucin 16, cell surface associated |
| [[SAMD12]] | 0.705 | sterile alpha motif domain containing 12 |
| [[SPINT1]] | 0.704 | serine peptidase inhibitor, Kunitz type 1 |
| [[PTPRR]] | 0.701 | protein tyrosine phosphatase receptor type R |
| [[SLC28A3]] | 0.698 | solute carrier family 28 member 3 |
| [[MTUS1]] | 0.695 | microtubule associated scaffold protein 1 |
| [[SYNPR-AS1]] | 0.692 | SYNPR antisense RNA 1 |
| [[C6orf132]] | 0.692 | chromosome 6 open reading frame 132 |
| [[SMIM2-AS1]] | 0.691 | SMIM2 antisense RNA 1 |
| [[RORC]] | 0.690 | RAR related orphan receptor C |
| [[PIP5K1B]] | 0.687 | phosphatidylinositol-4-phosphate 5-kinase type 1 beta |
| [[STEAP4]] | 0.684 | STEAP4 metalloreductase |
| [[PRSS51]] | 0.683 | serine protease 51 |
| [[SLC34A2]] | 0.676 | solute carrier family 34 member 2 |
| [[TMEM125]] | 0.674 | transmembrane protein 125 |
| [[STS]] | 0.674 | steroid sulfatase |
| [[TACSTD2]] | 0.673 | tumor associated calcium signal transducer 2 |
| [[ELF3]] | 0.673 | E74 like ETS transcription factor 3 |
| [[IGFL2-AS1]] | 0.670 | IGFL2 antisense RNA 1 |
| [[RASSF6]] | 0.670 | Ras association domain family member 6 |
| [[SLC44A3-AS1]] | 0.667 | SLC44A3 antisense RNA 1 |
| [[INAVA]] | 0.667 | innate immunity activator |
| [[TTC22]] | 0.667 | tetratricopeptide repeat domain 22 |
| [[MUC1]] | 0.652 | mucin 1, cell surface associated |
| [[MPZL2]] | 0.651 | myelin protein zero like 2 |
| [[PTPN22]] | 0.649 | protein tyrosine phosphatase non-receptor type 22 |
| [[HNF1B]] | 0.645 | HNF1 homeobox B |
| [[HNF4G]] | 0.641 | hepatocyte nuclear factor 4 gamma |
| [[RAMP1]] | 0.640 | receptor activity modifying protein 1 |
| [[C4orf19]] | 0.640 | PDCD10 and GCKIII kinases associated 1 |
| [[SLC15A1]] | 0.639 | solute carrier family 15 member 1 |
| [[CDHR2]] | 0.636 | cadherin related family member 2 |
| [[NSUN7]] | 0.632 | NOP2/Sun RNA methyltransferase family member 7 |
| [[CYP4F3]] | 0.629 | cytochrome P450 family 4 subfamily F member 3 |
| [[DPP4]] | 0.629 | dipeptidyl peptidase 4 |
| [[ST8SIA6]] | 0.627 | ST8 alpha-N-acetyl-neuraminide alpha-2,8-sialyltransferase 6 |
| [[VNN1]] | 0.625 | vanin 1 |
| [[ANK3]] | 0.624 | ankyrin 3 |
| [[MACC1]] | 0.619 | MET transcriptional regulator MACC1 |
| [[RHBDL2]] | 0.617 | rhomboid like 2 |
| [[MYH14]] | 0.616 | myosin heavy chain 14 |
| [[POU5F1B]] | 0.613 | POU class 5 homeobox 1B |
| [[MAL2]] | 0.610 | mal, T cell differentiation protein 2 |
| [[UNC5CL]] | 0.608 | unc-5 family C-terminal like |
| [[FUT3]] | 0.607 | fucosyltransferase 3 (Lewis blood group) |
| [[UCA1]] | 0.603 | urothelial cancer associated 1 |
| [[RNF39]] | 0.599 | ring finger protein 39 |
| [[INPP4B]] | 0.593 | inositol polyphosphate-4-phosphatase type II B |
| [[FXYD2]] | 0.593 | FXYD domain containing ion transport regulator 2 |
| [[CCSER1]] | 0.590 | coiled-coil serine rich protein 1 |
| [[NECTIN4]] | 0.590 | nectin cell adhesion molecule 4 |
| [[ARHGAP30]] | 0.590 | Rho GTPase activating protein 30 |
| [[TMEM51-AS1]] | 0.589 | TMEM51 antisense RNA 1 |
| [[DAPP1]] | 0.587 | dual adaptor of phosphotyrosine and 3-phosphoinositides 1 |
| [[KRT23]] | 0.587 | keratin 23 |
| [[RGS6]] | 0.586 | regulator of G protein signaling 6 |
| [[WFDC2]] | 0.585 | WAP four-disulfide core domain 2 |
| [[SCIN]] | 0.584 | scinderin |
| [[CARD14]] | 0.583 | caspase recruitment domain family member 14 |
| [[CHN2]] | 0.581 | chimerin 2 |
| [[ASS1]] | 0.580 | argininosuccinate synthase 1 |
| [[ABCC6]] | 0.580 | ATP binding cassette subfamily C member 6 |
| [[FMO5]] | 0.579 | flavin containing dimethylaniline monoxygenase 5 |
| [[POU5F1]] | 0.577 | POU class 5 homeobox 1 |
| [[FRMD4B]] | 0.575 | FERM domain containing 4B |
| [[LINC01504]] | 0.573 | long independently transcribed non-coding RNA 1504 |
| [[TNFRSF21]] | 0.572 | TNF receptor superfamily member 21 |
| [[GRHL2]] | 0.570 | grainyhead like transcription factor 2 |
| [[STYK1]] | 0.568 | STY kinase 1 |
| [[ANKRD22]] | 0.567 | ankyrin repeat domain 22 |
| [[KLHL2P1]] | 0.567 | kelch like family member 2 pseudogene 1 |
| [[CD24]] | 0.565 | CD24 molecule |
| [[RAPGEF5]] | 0.565 | Rap guanine nucleotide exchange factor 5 |
| [[SHROOM3]] | 0.564 | shroom family member 3 |
| [[MGC32805]] | 0.563 | SNCAIP antisense RNA 3 |
| [[EPCAM-DT]] | 0.560 | EPCAM divergent transcript |
| [[ESRP1]] | 0.560 | epithelial splicing regulatory protein 1 |
| [[SEC16B]] | 0.560 | SEC16 homolog B, endoplasmic reticulum export factor |
| [[SMIM31]] | 0.557 | small integral membrane protein 31 |
| [[B3GALT5]] | 0.553 | beta-1,3-galactosyltransferase 5 |
| [[XDH]] | 0.552 | xanthine dehydrogenase |
| [[TRIM2]] | 0.545 | tripartite motif containing 2 |
| [[ATP1B1]] | 0.545 | ATPase Na+/K+ transporting subunit beta 1 |
| [[TCN1]] | 0.545 | transcobalamin 1 |
| [[LNX1]] | 0.542 | ligand of numb-protein X 1 |
| [[IKZF2]] | 0.540 | IKAROS family zinc finger 2 |
| [[LY75]] | 0.538 | lymphocyte antigen 75 |
| [[CEACAM5]] | 0.537 | CEA cell adhesion molecule 5 |
| [[EXPH5]] | 0.532 | exophilin 5 |
| [[PLA2R1]] | 0.532 | phospholipase A2 receptor 1 |
| [[RHEX]] | 0.530 | regulator of hemoglobinization and erythroid cell expansion |
| [[IL22RA1]] | 0.529 | interleukin 22 receptor subunit alpha 1 |
| [[ADGRF4]] | 0.527 | adhesion G protein-coupled receptor F4 |
| [[SLC37A1]] | 0.525 | solute carrier family 37 member 1 |
| [[TTC39A]] | 0.524 | tetratricopeptide repeat domain 39A |
| [[LRG1]] | 0.522 | leucine rich alpha-2-glycoprotein 1 |
| [[FCGBP]] | 0.522 | Fc gamma binding protein |
| [[PLSCR4]] | 0.521 | phospholipid scramblase 4 |
| [[DNAAF9]] | -0.521 | dynein axonemal assembly factor 9 |
| [[USP6NL]] | 0.518 | USP6 N-terminal like |
| [[FOXP2]] | 0.518 | forkhead box P2 |
| [[PCAT1]] | 0.517 | prostate cancer associated transcript 1 |
| [[STX19]] | 0.511 | syntaxin 19 |
| [[HLA-DRB1]] | 0.509 | major histocompatibility complex, class II, DR beta 1 |
| [[FZD5]] | 0.508 | frizzled class receptor 5 |
| [[STEAP2-AS1]] | 0.507 | STEAP2 antisense RNA 1 |
| [[DAPK1]] | 0.505 | death associated protein kinase 1 |
| [[KLF8]] | 0.503 | KLF transcription factor 8 |
| [[DLG3]] | 0.499 | discs large MAGUK scaffold protein 3 |
| [[DAPK2]] | 0.496 | death associated protein kinase 2 |
| [[IL17RE]] | 0.494 | interleukin 17 receptor E |
| [[ACTR3C]] | 0.491 | actin related protein 3C |
| [[PLEKHG1]] | 0.486 | pleckstrin homology and RhoGEF domain containing G1 |
| [[HAVCR1]] | 0.484 | hepatitis A virus cellular receptor 1 |
| [[HGD]] | 0.484 | homogentisate 1,2-dioxygenase |
| [[GPRIN2]] | 0.480 | G protein regulated inducer of neurite outgrowth 2 |
| [[PRRG4]] | 0.477 | proline rich and Gla domain 4 |
| [[DNM3]] | 0.476 | dynamin 3 |
| [[ANXA3]] | 0.473 | annexin A3 |
| [[PRRG2]] | 0.470 | proline rich and Gla domain 2 |
| [[ICA1]] | 0.466 | islet cell autoantigen 1 |
| [[PBX1]] | 0.463 | PBX homeobox 1 |
| [[DSCAML1]] | 0.462 | DS cell adhesion molecule like 1 |
| [[BAG1]] | 0.460 | BAG cochaperone 1 |
| [[FAM149A]] | 0.459 | family with sequence similarity 149 member A |
| [[GRHL3]] | 0.459 | grainyhead like transcription factor 3 |
| [[ST6GALNAC5]] | 0.458 | ST6 N-acetylgalactosaminide alpha-2,6-sialyltransferase 5 |
| [[B4GALT5]] | 0.457 | beta-1,4-galactosyltransferase 5 |
| [[PRSS16]] | 0.455 | serine protease 16 |
| [[STEAP2]] | 0.452 | STEAP2 metalloreductase |
| [[FAM228B]] | -0.451 | family with sequence similarity 228 member B |
| [[RBPMS]] | 0.451 | RNA binding protein, mRNA processing factor |
| [[DAB2IP]] | 0.450 | DAB2 interacting protein |
| [[RASGEF1B]] | 0.450 | RasGEF domain family member 1B |
| [[LYN]] | 0.446 | LYN proto-oncogene, Src family tyrosine kinase |
| [[SELENOP]] | 0.443 | selenoprotein P |
| [[PRSS12]] | 0.439 | serine protease 12 |
| [[SLC2A12]] | 0.437 | solute carrier family 2 member 12 |
| [[LCN2]] | 0.436 | lipocalin 2 |
| [[RAB11FIP4]] | 0.435 | RAB11 family interacting protein 4 |
| [[BSPRY]] | 0.433 | B-box and SPRY domain containing |
| [[HNMT]] | 0.430 | histamine N-methyltransferase |
| [[DEPTOR]] | 0.424 | DEP domain containing MTOR interacting protein |
| [[CRYZL2P]] | 0.424 | crystallin zeta like 2, pseudogene |
| [[NT5C2]] | 0.423 | 5'-nucleotidase, cytosolic II |
| [[B3GNT7]] | 0.422 | UDP-GlcNAc:betaGal beta-1,3-N-acetylglucosaminyltransferase 7 |
| [[THRB]] | 0.412 | thyroid hormone receptor beta |
| [[SLC4A4]] | 0.412 | solute carrier family 4 member 4 |
| [[GPR87]] | 0.411 | G protein-coupled receptor 87 |
| [[LXN]] | 0.410 | latexin |
| [[HLA-DRA]] | 0.407 | major histocompatibility complex, class II, DR alpha |
| [[SPTLC3]] | 0.407 | serine palmitoyltransferase long chain base subunit 3 |
| [[SFTPA2]] | 0.404 | surfactant protein A2 |
| [[PON3]] | 0.388 | paraoxonase 3 |
| [[IGFBP1]] | 0.380 | insulin like growth factor binding protein 1 |
| [[GRB7]] | 0.380 | growth factor receptor bound protein 7 |
| [[MYO5C]] | 0.379 | myosin VC |
| [[TIMD4]] | 0.378 | T cell immunoglobulin and mucin domain containing 4 |
| [[SH2D4A]] | 0.377 | SH2 domain containing 4A |
| [[FGL1]] | 0.375 | fibrinogen like 1 |
| [[SYTL1]] | 0.375 | synaptotagmin like 1 |
| [[PCSK5]] | 0.370 | proprotein convertase subtilisin/kexin type 5 |
| [[CD74]] | 0.361 | CD74 molecule |
| [[ITIH2]] | 0.360 | inter-alpha-trypsin inhibitor heavy chain 2 |
| [[CNGA1]] | 0.357 | cyclic nucleotide gated channel subunit alpha 1 |
| [[HDHD3]] | 0.350 | haloacid dehalogenase like hydrolase domain containing 3 |
| [[AGT]] | 0.335 | angiotensinogen |
| [[BARX2]] | 0.332 | BARX homeobox 2 |
| [[DCLK2]] | -0.329 | doublecortin like kinase 2 |
| [[OPHN1]] | 0.308 | oligophrenin 1 |
| [[LYPD5]] | 0.296 | LY6/PLAUR domain containing 5 |
| [[MARVELD3]] | 0.283 | MARVEL domain containing 3 |
| [[MPZL3]] | 0.280 | myelin protein zero like 3 |
| [[FRAS1]] | 0.265 | Fraser extracellular matrix complex subunit 1 |
| [[ALB]] | 0.233 | albumin |
| [[AFP]] | 0.231 | alpha fetoprotein |
| [[AMBP]] | 0.223 | alpha-1-microglobulin/bikunin precursor |
| [[MACROD2]] | 0.211 | mono-ADP ribosylhydrolase 2 |
| [[XKRX]] | 0.201 | XK related X-linked |
| [[ITIH5]] | 0.193 | inter-alpha-trypsin inhibitor heavy chain 5 |
| [[AHSG]] | 0.193 | alpha 2-HS glycoprotein |
| [[APOA1]] | 0.188 | apolipoprotein A1 |
| [[PAX8]] | 0.178 | paired box 8 |
| [[PREX2]] | 0.155 | phosphatidylinositol-3,4,5-trisphosphate dependent Rac exchange factor 2 |
| [[S100A1]] | 0.0558 | S100 calcium binding protein A1 |
| [[APOA2]] | 0.0317 | apolipoprotein A2 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 8; `graph/modules.parquet` — module == 8; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [7] (drug-dose × line)
