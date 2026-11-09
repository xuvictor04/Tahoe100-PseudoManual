---
module: 4
type: "module"
n_genes: 245
n_plus: 183
n_minus: 62
arms_opposite: true
mean_cos_between_arms: -0.29841214418411255
label: "MYC targets v1"
label_source: "hallmark"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 004

*MYC targets v1 · 245 genes (183 in the + arm, 62 in the − arm) · [[Module 004.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30). The + arm rises where the − arm falls. Arm = the side of the module's main direction a gene sits on.

Label from the validation stage: **MYC targets v1** (hallmark, q 6e-11; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| + | MYC targets v1 | hallmark | 21/183 | 8.65 | 6e-11 |
| all | MYC targets v1 | hallmark | 21/245 | 6.46 | 2e-08 |
| + | Metabolism of RNA | reactome | 31/183 | 3.50 | 8e-07 |
| + | Dengue Virus Infection | reactome | 17/183 | 4.34 | 3e-04 |
| + | tRNA Aminoacylation | reactome | 7/183 | 14.4 | 3e-04 |
| + | tRNA processing in the nucleus | reactome | 8/183 | 11.4 | 3e-04 |
| + | Translation | reactome | 17/183 | 4.30 | 3e-04 |
| + | tRNA processing | reactome | 10/183 | 7.49 | 5e-04 |

## Drugs that move it

*Mean pooled z of the + arm minus the − arm (`graph/module_pooled_z.npy`, row 3), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it (+ arm up, − arm down): [[Dinaciclib (drug)]] 0.5 µM (+11.2, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (+10.7, ⚠ toxic; transcription drop; cell-cycle shift); [[c-Kit-IN-1 (drug)]] 0.05 µM (+8.6, ⚠ unreliable plate only); [[Dinaciclib (drug)]] 0.05 µM (+8.4, ⚠ toxic; transcription drop; cell-cycle shift); [[Belumosudil (drug)]] 5 µM (+5.4); [[Ixazomib citrate (drug)]] 5 µM (+5.1, ⚠ cell-cycle shift); [[Ixazomib citrate (drug)]] 0.5 µM (+4.7); [[PH-797804 (drug)]] 5 µM (+4.6); [[TAK-901 (drug)]] 5 µM (+4.5, ⚠ cell-cycle shift); [[c-Kit-IN-1 (drug)]] 5 µM (+4.0); [[TAK-733 (drug)]] 5 µM (+3.6); [[EX229 (drug)]] 5 µM (+3.5); [[TAK-901 (drug)]] 0.05 µM (+3.3); [[Homoharringtonine (drug)]] 0.05 µM (+2.8); [[Abemaciclib (drug)]] 5 µM (+2.6); [[Retinoic acid (drug)]] 0.05 µM (+2.6) (114 in all, 21 with an alert ⚠; shown: the 10 strongest and the 6 next strongest without an alert)
- Lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM (-15.6, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 5 µM (-13.7, ⚠ cell-cycle shift); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (-4.9, ⚠ cell-cycle shift); [[Epirubicin (hydrochloride) (drug)]] 5 µM (-4.0, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (-3.3, ⚠ cell-cycle shift); [[Artesunate (drug)]] 5 µM (-3.2, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-3.2, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 5 µM (-3.1, ⚠ toxic; transcription drop; cell-cycle shift); [[HI-TOPK-032 (drug)]] 5 µM (-2.2); [[Terfenadine (drug)]] 5 µM (-2.2); [[Entrectinib (drug)]] 5 µM (-2.1); [[PF-06260933 (drug)]] 5 µM (-2.0); [[Niclosamide (olamine) (drug)]] 0.5 µM (-2.0); [[Docetaxel (Trihydrate) (drug)]] 0.5 µM (-1.9); [[Ipatasertib (drug)]] 0.5 µM (-1.9); [[Retinoic acid (drug)]] 5 µM (-1.8); [[Tucidinostat (drug)]] 5 µM (-1.8); [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM (-1.7) (87 in all, 20 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[NCI-H460 (line)]], [[SW480 (line)]], [[PANC-1 (line)]], [[MIA PaCa-2 (line)]], [[HOP62 (line)]], [[NCI-H1573 (line)]], [[LoVo (line)]], [[CFPAC-1 (line)]]

## Candidate new members

*Members not annotated to the set their arm is enriched for, ranked by mean cos to the annotated members (`validation/novel_members.csv`); ⚠ = a reason to doubt the gene's place (in the vector space only through flagged drug-doses), kept in its rank. 70 candidates, none with an alert; shown: the 15 strongest.*

| # | Gene | Set | Mean cos |
|---|---|---|---|
| 1 | [[PTPN11]] | Folding of actin by CCT/TriC | +0.64 |
| 2 | [[MRPS27]] | tRNA processing in the nucleus | +0.63 |
| 3 | [[GLO1]] | Folding of actin by CCT/TriC | +0.63 |
| 4 | [[PRKDC]] | Folding of actin by CCT/TriC | +0.63 |
| 5 | [[RUVBL1]] | Folding of actin by CCT/TriC | +0.62 |
| 6 | [[TMX3]] | Folding of actin by CCT/TriC | +0.62 |
| 7 | [[C1QBP]] | Folding of actin by CCT/TriC | +0.62 |
| 8 | [[NUDC]] | Folding of actin by CCT/TriC | +0.62 |
| 9 | [[DLAT]] | Folding of actin by CCT/TriC | +0.60 |
| 10 | [[EIF2S1]] | Folding of actin by CCT/TriC | +0.60 |
| 11 | [[NUP155]] | Folding of actin by CCT/TriC | +0.60 |
| 12 | [[LRPPRC]] | Folding of actin by CCT/TriC | +0.60 |
| 13 | [[ATIC]] | MYC targets v1 | +0.59 |
| 14 | [[GOT2]] | Folding of actin by CCT/TriC | +0.59 |
| 15 | [[NAA25]] | tRNA processing | +0.58 |

## + arm (183)

| Gene | Projection | Name |
|---|---|---|
| [[MRPS27]] | 0.868 | mitochondrial ribosomal protein S27 |
| [[POLR1A]] | 0.861 | RNA polymerase I subunit A |
| [[NAA15]] | 0.860 | N-alpha-acetyltransferase 15, NatA auxiliary subunit |
| [[TMEM33]] | 0.857 | transmembrane protein 33 |
| [[CCT2]] | 0.852 | chaperonin containing TCP1 subunit 2 |
| [[ATIC]] | 0.850 | 5-aminoimidazole-4-carboxamide ribonucleotide formyltransferase/IMP cyclohydrolase |
| [[EFTUD2]] | 0.833 | elongation factor Tu GTP binding domain containing 2 |
| [[FARSB]] | 0.825 | phenylalanyl-tRNA synthetase subunit beta |
| [[NUP155]] | 0.821 | nucleoporin 155 |
| [[CCT5]] | 0.819 | chaperonin containing TCP1 subunit 5 |
| [[WDR77]] | 0.812 | WD repeat domain 77 |
| [[MYBBP1A]] | 0.805 | MYB binding protein 1a |
| [[ELAC2]] | 0.804 | elaC ribonuclease Z 2 |
| [[AGPS]] | 0.804 | alkylglycerone phosphate synthase |
| [[RUVBL1]] | 0.803 | RuvB like AAA ATPase 1 |
| [[NAA25]] | 0.802 | N-alpha-acetyltransferase 25, NatB auxiliary subunit |
| [[PFAS]] | 0.791 | phosphoribosylformylglycinamidine synthase |
| [[PRKDC]] | 0.788 | protein kinase, DNA-activated, catalytic subunit |
| [[LAS1L]] | 0.784 | LAS1 like ribosome biogenesis factor |
| [[MRPL3]] | 0.782 | mitochondrial ribosomal protein L3 |
| [[TSEN2]] | 0.776 | tRNA splicing endonuclease subunit 2 |
| [[C1QBP]] | 0.775 | complement C1q binding protein |
| [[COA1]] | 0.774 | cytochrome c oxidase assembly factor 1 |
| [[DPH6]] | 0.773 | diphthamine biosynthesis 6 |
| [[VWA8]] | 0.769 | von Willebrand factor A domain containing 8 |
| [[EIPR1]] | 0.764 | EARP complex and GARP complex interacting protein 1 |
| [[DIS3L2]] | 0.756 | DIS3 like 3'-5' exoribonuclease 2 |
| [[MRPL42]] | 0.754 | mitochondrial ribosomal protein L42 |
| [[GOT2]] | 0.751 | glutamic-oxaloacetic transaminase 2 |
| [[PGAM5]] | 0.749 | PGAM family member 5, mitochondrial serine/threonine protein phosphatase |
| [[GFM1]] | 0.747 | G elongation factor mitochondrial 1 |
| [[PRPF19]] | 0.746 | pre-mRNA processing factor 19 |
| [[PRPS1]] | 0.745 | phosphoribosyl pyrophosphate synthetase 1 |
| [[CHCHD3]] | 0.745 | coiled-coil-helix-coiled-coil-helix domain containing 3 |
| [[CLPB]] | 0.742 | ClpB family mitochondrial disaggregase |
| [[TMX3]] | 0.738 | thioredoxin related transmembrane protein 3 |
| [[RPE]] | 0.737 | ribulose-5-phosphate-3-epimerase |
| [[EIF2S1]] | 0.735 | eukaryotic translation initiation factor 2 subunit alpha |
| [[FAM98B]] | 0.734 | tRNA splicing ligase complex subunit 3B |
| [[RAD51D]] | 0.730 | RAD51 paralog D |
| [[XRN2]] | 0.721 | 5'-3' exoribonuclease 2 |
| [[MTAP]] | 0.719 | methylthioadenosine phosphorylase |
| [[LSG1]] | 0.718 | large 60S subunit nuclear export GTPase 1 |
| [[NUDC]] | 0.717 | nuclear distribution C, dynein complex regulator |
| [[DLAT]] | 0.716 | dihydrolipoamide S-acetyltransferase |
| [[BOP1]] | 0.715 | BOP1 ribosomal biogenesis factor |
| [[XRCC5]] | 0.711 | X-ray repair cross complementing 5 |
| [[SLC35B4]] | 0.709 | solute carrier family 35 member B4 |
| [[NME1]] | 0.705 | NME/NM23 nucleoside diphosphate kinase 1 |
| [[G3BP1]] | 0.702 | G3BP stress granule assembly factor 1 |
| [[SARS2]] | 0.702 | seryl-tRNA synthetase 2, mitochondrial |
| [[DCAF1]] | 0.702 | DDB1 and CUL4 associated factor 1 |
| [[DHX9]] | 0.697 | DExH-box helicase 9 |
| [[PPP5C]] | 0.697 | protein phosphatase 5 catalytic subunit |
| [[PTPN11]] | 0.691 | protein tyrosine phosphatase non-receptor type 11 |
| [[SPTBN2]] | 0.690 | spectrin beta, non-erythrocytic 2 |
| [[RABGGTB]] | 0.687 | Rab geranylgeranyltransferase subunit beta |
| [[DROSHA]] | 0.686 | drosha ribonuclease III |
| [[CSTF2]] | 0.686 | cleavage stimulation factor subunit 2 |
| [[EIF4G1]] | 0.680 | eukaryotic translation initiation factor 4 gamma 1 |
| [[EBNA1BP2]] | 0.679 | EBNA1 binding protein 2 |
| [[SNRPD1]] | 0.678 | small nuclear ribonucleoprotein D1 polypeptide |
| [[FIRRE]] | 0.676 | firre intergenic repeating RNA element |
| [[COX10]] | 0.675 | cytochrome c oxidase assembly factor heme A:farnesyltransferase COX10 |
| [[LRPPRC]] | 0.671 | leucine rich pentatricopeptide repeat containing |
| [[USP14]] | 0.671 | ubiquitin specific peptidase 14 |
| [[CDIN1]] | 0.671 | CDAN1 interacting nuclease 1 |
| [[NOC2L]] | 0.670 | NOC2 like nucleolar associated transcriptional repressor |
| [[BCCIP]] | 0.667 | BRCA2 and CDKN1A interacting protein |
| [[CMSS1]] | 0.661 | cms1 ribosomal small subunit homolog |
| [[CCT7]] | 0.659 | chaperonin containing TCP1 subunit 7 |
| [[MACROH2A1]] | 0.653 | macroH2A.1 histone |
| [[STX18-AS1]] | 0.645 | STX18 antisense RNA 1 |
| [[HNRNPR]] | 0.645 | heterogeneous nuclear ribonucleoprotein R |
| [[ALKBH8]] | 0.641 | alkB homolog 8, tRNA methyltransferase |
| [[RAB4A-AS1]] | 0.637 | RAB4A antisense RNA 1 |
| [[INTS7]] | 0.636 | integrator complex subunit 7 |
| [[LARP4]] | 0.636 | La ribonucleoprotein 4 |
| [[MINDY4]] | 0.635 | MINDY lysine 48 deubiquitinase 4 |
| [[NAA50]] | 0.632 | N-alpha-acetyltransferase 50, NatE catalytic subunit |
| [[NUDT5]] | 0.626 | nudix hydrolase 5 |
| [[POP1]] | 0.625 | POP1 ribonuclease P/MRP subunit |
| [[SLC19A1]] | 0.624 | solute carrier family 19 member 1 |
| [[DFFA]] | 0.624 | DNA fragmentation factor subunit alpha |
| [[MEST]] | 0.623 | mesoderm specific transcript |
| [[LCLAT1]] | 0.616 | lysocardiolipin acyltransferase 1 |
| [[SUPT16H]] | 0.616 | SPT16 homolog, facilitates chromatin remodeling subunit |
| [[GTF2F2]] | 0.614 | general transcription factor IIF subunit 2 |
| [[IPO7]] | 0.612 | importin 7 |
| [[COG8]] | 0.611 | component of oligomeric golgi complex 8 |
| [[TANGO6]] | 0.606 | transport and golgi organization 6 homolog |
| [[RPRD1A]] | 0.606 | regulation of nuclear pre-mRNA domain containing 1A |
| [[MRPL24]] | 0.605 | mitochondrial ribosomal protein L24 |
| [[VARS1]] | 0.605 | valyl-tRNA synthetase 1 |
| [[SERBP1]] | 0.605 | SERPINE1 mRNA binding protein 1 |
| [[DNAAF5]] | 0.604 | dynein axonemal assembly factor 5 |
| [[MAPKAPK3]] | 0.602 | MAPK activated protein kinase 3 |
| [[MIPOL1]] | 0.601 | mirror-image polydactyly 1 |
| [[HARS1]] | 0.599 | histidyl-tRNA synthetase 1 |
| [[NIT2]] | 0.597 | nitrilase family member 2 |
| [[MRPL19]] | 0.595 | mitochondrial ribosomal protein L19 |
| [[UTP11]] | 0.590 | UTP11 small subunit processome component |
| [[SACS]] | 0.588 | sacsin molecular chaperone |
| [[ZP3]] | 0.587 | zona pellucida glycoprotein 3 |
| [[HLCS]] | 0.587 | holocarboxylase synthetase |
| [[IPO4]] | 0.587 | importin 4 |
| [[RTEL1]] | 0.586 | regulator of telomere elongation helicase 1 |
| [[CLYBL]] | 0.585 | citramalyl-CoA lyase |
| [[GLO1]] | 0.581 | glyoxalase I |
| [[ERH]] | 0.581 | ERH mRNA splicing and mitosis factor |
| [[AATF]] | 0.576 | apoptosis antagonizing transcription factor |
| [[LARS2]] | 0.575 | leucyl-tRNA synthetase 2, mitochondrial |
| [[KAT2A]] | 0.571 | lysine acetyltransferase 2A |
| [[NCBP1]] | 0.569 | nuclear cap binding protein subunit 1 |
| [[SPIDR]] | 0.564 | scaffold protein involved in DNA repair |
| [[ENTPD1-AS1]] | 0.557 | ENTPD1 antisense RNA 1 |
| [[UQCC2]] | 0.554 | ubiquinol-cytochrome c reductase complex assembly factor 2 |
| [[DPP3]] | 0.553 | dipeptidyl peptidase 3 |
| [[CRACR2A]] | 0.552 | calcium release activated channel regulator 2A |
| [[FAF1]] | 0.552 | Fas associated factor 1 |
| [[ERCC8]] | 0.551 | ERCC excision repair 8, CSA ubiquitin ligase complex subunit |
| [[IDE]] | 0.546 | insulin degrading enzyme |
| [[NUDCD1]] | 0.543 | NudC domain containing 1 |
| [[C7orf50]] | 0.542 | cholesin |
| [[EXOG]] | 0.540 | exo/endonuclease G |
| [[GSPT1]] | 0.533 | G1 to S phase transition 1 |
| [[NUP42]] | 0.526 | nucleoporin 42 |
| [[PITPNB]] | 0.522 | phosphatidylinositol transfer protein beta |
| [[HSPBP1]] | 0.511 | HSPA (Hsp70) binding protein 1 |
| [[TRMT11]] | 0.509 | tRNA methyltransferase 11 |
| [[ELP6]] | 0.508 | elongator acetyltransferase complex subunit 6 |
| [[PVT1]] | 0.507 | Pvt1 oncogene |
| [[MTHFD2L]] | 0.506 | methylenetetrahydrofolate dehydrogenase (NADP+ dependent) 2 like |
| [[CCT8]] | 0.503 | chaperonin containing TCP1 subunit 8 |
| [[NCLN]] | 0.501 | nicalin |
| [[DNM1L]] | 0.497 | dynamin 1L |
| [[BICD1]] | 0.496 | BICD cargo adaptor 1 |
| [[KLHL2]] | 0.494 | kelch like family member 2 |
| [[ZNF37BP]] | 0.486 | zinc finger protein 37B, pseudogene |
| [[KARS1]] | 0.486 | lysyl-tRNA synthetase 1 |
| [[SNRPE]] | 0.483 | small nuclear ribonucleoprotein polypeptide E |
| [[EIF4G3]] | 0.471 | eukaryotic translation initiation factor 4 gamma 3 |
| [[EIF4E]] | 0.470 | eukaryotic translation initiation factor 4E |
| [[SLC48A1]] | 0.466 | solute carrier family 48 member 1 |
| [[RBM17]] | 0.466 | RNA binding motif protein 17 |
| [[TUSC3]] | 0.460 | tumor suppressor candidate 3 |
| [[SMARCA4]] | 0.458 | SWI/SNF related BAF chromatin remodeling complex subunit ATPase 4 |
| [[FABP5]] | 0.457 | fatty acid binding protein 5 |
| [[CNOT6]] | 0.453 | CCR4-NOT transcription complex subunit 6 |
| [[PSTK]] | 0.450 | phosphoseryl-tRNA kinase |
| [[ENTPD6]] | 0.446 | ectonucleoside triphosphate diphosphohydrolase 6 |
| [[MAP3K4]] | 0.436 | mitogen-activated protein kinase kinase kinase 4 |
| [[LINC01357]] | 0.431 | — |
| [[PPA2]] | 0.430 | inorganic pyrophosphatase 2 |
| [[IQCH]] | 0.429 | IQ motif containing H |
| [[SLC12A8]] | 0.429 | solute carrier family 12 member 8 |
| [[SPIN3]] | 0.425 | spindlin family member 3 |
| [[MGMT]] | 0.424 | O-6-methylguanine-DNA methyltransferase |
| [[KBTBD11]] | 0.415 | kelch repeat and BTB domain containing 11 |
| [[AGMAT]] | 0.412 | agmatinase (putative) |
| [[LINC02666]] | 0.409 | long independently transcribed non-coding RNA 2666 |
| [[DTWD2]] | 0.406 | DTW motif tRNA-uridine aminocarboxypropyltransferase 2 |
| [[TOMM40L]] | 0.405 | translocase of outer mitochondrial membrane 40 like |
| [[RAN]] | 0.400 | RAN, member RAS oncogene family |
| [[KPNA1]] | 0.398 | karyopherin subunit alpha 1 |
| [[ZNF346]] | 0.389 | zinc finger protein 346 |
| [[RTN4IP1]] | 0.388 | reticulon 4 interacting protein 1 |
| [[TMEM168]] | 0.388 | transmembrane protein 168 |
| [[MTARC1]] | 0.385 | mitochondrial amidoxime reducing component 1 |
| [[STXBP4]] | 0.384 | syntaxin binding protein 4 |
| [[CDK4]] | 0.382 | cyclin dependent kinase 4 |
| [[KHDC1-AS1]] | 0.381 | KHDC1 antisense RNA 1 |
| [[MSH3]] | 0.380 | mutS homolog 3 |
| [[SMARCC1]] | 0.375 | SWI/SNF related BAF chromatin remodeling complex subunit C1 |
| [[CCDC57]] | 0.367 | coiled-coil domain containing 57 |
| [[LRP5]] | 0.364 | LDL receptor related protein 5 |
| [[ZNF37A]] | 0.360 | zinc finger protein 37A |
| [[PRMT1]] | 0.344 | protein arginine methyltransferase 1 |
| [[SNRPF]] | 0.326 | small nuclear ribonucleoprotein polypeptide F |
| [[SLC38A5]] | 0.273 | solute carrier family 38 member 5 |
| [[PFDN6]] | 0.250 | prefoldin subunit 6 |
| [[ZNF589]] | 0.213 | zinc finger protein 589 |
| [[DNPH1]] | 0.206 | 2'-deoxynucleoside 5'-phosphate N-hydrolase 1 |

## − arm (62)

| Gene | Projection | Name |
|---|---|---|
| [[RSRP1]] | -0.809 | arginine and serine rich protein 1 |
| [[AAMDC]] | -0.801 | adipogenesis associated Mth938 domain containing |
| [[TESK2]] | -0.738 | testis associated actin remodelling kinase 2 |
| [[ZFYVE1]] | -0.726 | zinc finger FYVE-type containing 1 |
| [[SIRT2]] | -0.716 | sirtuin 2 |
| [[FAM117A]] | -0.702 | family with sequence similarity 117 member A |
| [[SELENOK]] | -0.698 | selenoprotein K |
| [[KDM5B]] | -0.682 | lysine demethylase 5B |
| [[HMGCL]] | -0.679 | 3-hydroxy-3-methylglutaryl-CoA lyase |
| [[STARD10]] | -0.676 | StAR related lipid transfer domain containing 10 |
| [[TSC22D4]] | -0.672 | TSC22 domain family member 4 |
| [[SHOC2]] | -0.671 | SHOC2 leucine rich repeat scaffold protein |
| [[TMEM106A]] | -0.670 | transmembrane protein 106A |
| [[TTC21A]] | -0.658 | tetratricopeptide repeat domain 21A |
| [[TRNAU1AP]] | -0.654 | tRNA selenocysteine 1 associated protein 1 |
| [[CCS]] | -0.651 | copper chaperone for superoxide dismutase |
| [[ACAP1]] | -0.633 | ArfGAP with coiled-coil, ankyrin repeat and PH domains 1 |
| [[ERO1B]] | -0.628 | endoplasmic reticulum oxidoreductase 1 beta |
| [[HOTAIRM1]] | -0.612 | HOXA transcript antisense RNA, myeloid-specific 1 |
| [[GPRC5C]] | -0.603 | G protein-coupled receptor class C group 5 member C |
| [[FNBP1]] | -0.600 | formin binding protein 1 |
| [[ZNF490]] | -0.595 | zinc finger protein 490 |
| [[MTHFR]] | -0.592 | methylenetetrahydrofolate reductase |
| [[ING1]] | -0.587 | inhibitor of growth family member 1 |
| [[KATNA1]] | -0.577 | katanin catalytic subunit A1 |
| [[CATSPERG]] | -0.550 | catsper channel auxiliary subunit gamma |
| [[INTS6L]] | -0.549 | integrator complex subunit 6 like |
| [[CD63]] | -0.542 | CD63 molecule |
| [[STX12]] | -0.535 | syntaxin 12 |
| [[LASP1]] | -0.525 | LIM and SH3 protein 1 |
| [[GLIS2]] | -0.516 | GLIS family zinc finger 2 |
| [[GAD1]] | -0.506 | glutamate decarboxylase 1 |
| [[IER5L]] | -0.496 | immediate early response 5 like |
| [[OVOL1]] | -0.473 | ovo like transcriptional repressor 1 |
| [[CRY2]] | -0.471 | cryptochrome circadian regulator 2 |
| [[MAP1LC3B]] | -0.462 | microtubule associated protein 1 light chain 3 beta |
| [[CEP95]] | -0.461 | centrosomal protein 95 |
| [[GCAT]] | -0.461 | glycine C-acetyltransferase |
| [[CBR3-AS1]] | -0.459 | CBR3 antisense RNA 1 |
| [[CDC42EP4]] | -0.457 | CDC42 effector protein 4 |
| [[C16orf46]] | -0.454 | chromosome 16 open reading frame 46 |
| [[ZBTB18]] | -0.444 | zinc finger and BTB domain containing 18 |
| [[RAB2B]] | -0.442 | RAB2B, member RAS oncogene family |
| [[HES4]] | -0.436 | hes family bHLH transcription factor 4 |
| [[ARL17B]] | -0.430 | ARF like GTPase 17B |
| [[VAMP4]] | -0.423 | vesicle associated membrane protein 4 |
| [[BBIP1]] | -0.421 | BBSome interacting protein 1 |
| [[TRIM24]] | -0.402 | tripartite motif containing 24 |
| [[ACOX1]] | -0.390 | acyl-CoA oxidase 1 |
| [[MAP4K3-DT]] | -0.389 | MAP4K3 divergent transcript |
| [[DENND4A]] | -0.382 | DENN domain containing 4A |
| [[CAMK2N1]] | -0.374 | calcium/calmodulin dependent protein kinase II inhibitor 1 |
| [[HNRNPLL]] | -0.374 | heterogeneous nuclear ribonucleoprotein L like |
| [[GATA2]] | -0.367 | GATA binding protein 2 |
| [[TBPL1]] | -0.362 | TATA-box binding protein like 1 |
| [[SLC41A1]] | -0.356 | solute carrier family 41 member 1 |
| [[WASL]] | -0.332 | WASP like actin nucleation promoting factor |
| [[TPM2]] | -0.294 | tropomyosin 2 |
| [[STK17B]] | -0.290 | serine/threonine kinase 17b |
| [[SLC35F5]] | -0.275 | solute carrier family 35 member F5 |
| [[FKBP15]] | -0.245 | FKBP prolyl isomerase family member 15 |
| [[MAN2B1]] | -0.234 | mannosidase alpha class 2B member 1 |

## Data

- `graph/nodes.parquet` — module == 4; `graph/modules.parquet` — module == 4; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [3] (drug-dose × line)
