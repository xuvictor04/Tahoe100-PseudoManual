---
module: 1
type: "module"
n_genes: 298
n_plus: 246
n_minus: 52
arms_opposite: true
mean_cos_between_arms: -0.2736620604991913
label: "rRNA processing"
label_source: "reactome"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 001

*rRNA processing · 298 genes (246 in the + arm, 52 in the − arm) · [[Module 001.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27). The + arm rises where the − arm falls. Arm = the side of the module's main direction a gene sits on.

Label from the validation stage: **rRNA processing** (reactome, q 9e-15; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| + | Metabolism of RNA | reactome | 50/246 | 4.20 | 7e-15 |
| + | rRNA processing | reactome | 28/246 | 8.41 | 9e-15 |
| all | rRNA processing | reactome | 29/298 | 7.19 | 1e-13 |
| all | Metabolism of RNA | reactome | 51/298 | 3.54 | 4e-12 |
| + | rRNA processing in the nucleus and cytosol | reactome | 24/246 | 7.87 | 8e-12 |
| + | Major pathway of rRNA processing in the nucleolus and cytosol | reactome | 23/246 | 7.96 | 2e-11 |
| + | rRNA modification in the nucleus and cytosol | reactome | 15/246 | 15.8 | 3e-11 |
| all | rRNA processing in the nucleus and cytosol | reactome | 25/298 | 6.76 | 6e-11 |

## Drugs that move it

*Mean pooled z of the + arm minus the − arm (`graph/module_pooled_z.npy`, row 0), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it (+ arm up, − arm down): [[Homoharringtonine (drug)]] 0.5 µM (+10.6, ⚠ cell-cycle shift); [[c-Kit-IN-1 (drug)]] 0.05 µM (+8.0, ⚠ unreliable plate only); [[Harringtonine (drug)]] 0.5 µM (+7.8, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (+6.5, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.05 µM (+6.3); [[Dinaciclib (drug)]] 0.5 µM (+6.2, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (+6.1, ⚠ toxic; transcription drop; cell-cycle shift); [[Homoharringtonine (drug)]] 5 µM (+5.8, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+5.7, ⚠ toxic; transcription drop; cell-cycle shift); [[Belumosudil (drug)]] 5 µM (+5.4); [[c-Kit-IN-1 (drug)]] 5 µM (+4.2); [[TAK-733 (drug)]] 5 µM (+4.2); [[EX229 (drug)]] 5 µM (+3.9); [[Harringtonine (drug)]] 0.05 µM (+3.1); [[Abemaciclib (drug)]] 5 µM (+3.1); [[PH-797804 (drug)]] 5 µM (+3.1); [[Clobetasol propionate (drug)]] 0.05 µM (+3.0); [[Pralsetinib (drug)]] 5 µM (+2.8) (75 in all, 18 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)
- Lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM (-9.9, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (-6.0, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (-5.7, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (-5.5, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (-4.9); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (-4.7, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (-4.5, ⚠ cell-cycle shift); [[Epirubicin (hydrochloride) (drug)]] 5 µM (-4.0, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 0.5 µM (-3.7, ⚠ cell-cycle shift); [[Brivudine (drug)]] 5 µM (-2.8); [[Pitavastatin (Calcium) (drug)]] 0.5 µM (-2.5); [[PF-06260933 (drug)]] 5 µM (-2.3); [[HI-TOPK-032 (drug)]] 5 µM (-2.2); [[Binimetinib (drug)]] 5 µM (-2.1); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM (-1.9); [[Trametinib (drug)]] 0.5 µM (-1.9); [[Cobimetinib (drug)]] 5 µM (-1.7); [[Entrectinib (drug)]] 5 µM (-1.6) (53 in all, 18 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[NCI-H1792 (line)]], [[NCI-H2347 (line)]], [[AsPC-1 (line)]], [[LOX-IMVI (line)]], [[LoVo (line)]], [[A-172 (line)]], [[CFPAC-1 (line)]], [[HS-578T (line)]]

## Candidate new members

*Members not annotated to the set their arm is enriched for, ranked by mean cos to the annotated members (`validation/novel_members.csv`); ⚠ = a reason to doubt the gene's place (in the vector space only through flagged drug-doses), kept in its rank. 56 candidates, none with an alert; shown: the 15 strongest.*

| # | Gene | Set | Mean cos |
|---|---|---|---|
| 1 | [[MAK16]] | Major pathway of rRNA processing in the nucleolus and cytosol | +0.65 |
| 2 | [[RRS1]] | MYC targets v2 | +0.63 |
| 3 | [[BYSL]] | rRNA modification in the nucleus and cytosol | +0.62 |
| 4 | [[IFRD2]] | MYC targets v2 | +0.61 |
| 5 | [[UTP14A]] | MYC targets v2 | +0.60 |
| 6 | [[PRMT5]] | Major pathway of rRNA processing in the nucleolus and cytosol | +0.59 |
| 7 | [[LTV1]] | rRNA modification in the nucleus and cytosol | +0.59 |
| 8 | [[UTP15]] | MYC targets v2 | +0.59 |
| 9 | [[PAK1IP1]] | Major pathway of rRNA processing in the nucleolus and cytosol | +0.58 |
| 10 | [[DDX10]] | MYC targets v2 | +0.58 |
| 11 | [[NOL11]] | Mitochondrial mRNA modification | +0.58 |
| 12 | [[TRMT61A]] | MYC targets v2 | +0.58 |
| 13 | [[METTL1]] | rRNA modification in the nucleus and cytosol | +0.58 |
| 14 | [[PPIL1]] | Major pathway of rRNA processing in the nucleolus and cytosol | +0.58 |
| 15 | [[RRP15]] | Major pathway of rRNA processing in the nucleolus and cytosol | +0.57 |

*⚠ 3 of its 298 genes are in the vector space only through drug-doses that carry an alert (`embed/genes.parquet` evidence_flagged_only): their place here may reflect what those drug-doses did to the cells. They are marked in the tables of this note.*

## + arm (246)

| Gene | Projection | Name | Alert |
|---|---|---|---|
| [[MAK16]] | 0.887 | MAK16 homolog |  |
| [[UTP15]] | 0.865 | UTP15 small subunit processome component |  |
| [[LTV1]] | 0.864 | LTV1 ribosome biogenesis factor |  |
| [[BYSL]] | 0.853 | bystin like |  |
| [[COA7]] | 0.851 | cytochrome c oxidase assembly factor 7 |  |
| [[GPATCH4]] | 0.850 | G-patch domain containing 4 (gene/pseudogene) |  |
| [[PPIL1]] | 0.844 | peptidylprolyl isomerase like 1 |  |
| [[RRP15]] | 0.834 | ribosomal RNA processing 15 homolog |  |
| [[ABCE1]] | 0.830 | ATP binding cassette subfamily E member 1 |  |
| [[ZNF239]] | 0.828 | zinc finger protein 239 |  |
| [[ZNF507]] | 0.822 | zinc finger protein 507 |  |
| [[RRS1]] | 0.822 | regulator of ribosome synthesis 1 |  |
| [[PAK1IP1]] | 0.815 | PAK1 interacting protein 1 |  |
| [[UTP20]] | 0.812 | UTP20 small subunit processome component |  |
| [[DNAJC11]] | 0.808 | DnaJ heat shock protein family (Hsp40) member C11 |  |
| [[POGK]] | 0.807 | pogo transposable element derived with KRAB domain |  |
| [[MGA]] | 0.806 | MAX dimerization protein MGA |  |
| [[TCERG1]] | 0.800 | transcription elongation regulator 1 |  |
| [[RIOX2]] | 0.797 | ribosomal oxygenase 2 |  |
| [[IFRD2]] | 0.796 | interferon related developmental regulator 2 |  |
| [[NOL11]] | 0.796 | nucleolar protein 11 |  |
| [[NOP14]] | 0.795 | NOP14 nucleolar protein |  |
| [[DDX10]] | 0.781 | DEAD-box helicase 10 |  |
| [[MRRF]] | 0.781 | mitochondrial ribosome recycling factor |  |
| [[SCO1]] | 0.781 | synthesis of cytochrome C oxidase 1 |  |
| [[UTP14A]] | 0.779 | UTP14A small subunit processome component |  |
| [[FKTN]] | 0.775 | fukutin |  |
| [[METAP1D]] | 0.774 | methionyl aminopeptidase type 1D, mitochondrial |  |
| [[MTPAP]] | 0.773 | mitochondrial poly(A) polymerase |  |
| [[DPH5]] | 0.773 | diphthamide biosynthesis 5 |  |
| [[SF3B3]] | 0.770 | splicing factor 3b subunit 3 |  |
| [[ZNF485]] | 0.767 | zinc finger protein 485 |  |
| [[RBM28]] | 0.765 | RNA binding motif protein 28 |  |
| [[MRPL15]] | 0.762 | mitochondrial ribosomal protein L15 |  |
| [[QTRT2]] | 0.755 | queuine tRNA-ribosyltransferase accessory subunit 2 |  |
| [[NOC3L]] | 0.753 | NOC3 like DNA replication regulator |  |
| [[IMP4]] | 0.753 | IMP U3 small nucleolar ribonucleoprotein 4 |  |
| [[EXOSC2]] | 0.751 | exosome component 2 |  |
| [[N6AMT1]] | 0.751 | HemK methyltransferase 2, ETF1 glutamine and histone H4 lysine |  |
| [[UMPS]] | 0.744 | uridine monophosphate synthetase |  |
| [[PRMT5]] | 0.736 | protein arginine methyltransferase 5 |  |
| [[TMA16]] | 0.735 | translation machinery associated 16 homolog |  |
| [[ZNF121]] | 0.733 | zinc finger protein 121 |  |
| [[GUF1]] | 0.724 | GTP binding elongation factor GUF1 |  |
| [[CCDC86]] | 0.721 | coiled-coil domain containing 86 |  |
| [[NDUFAF4]] | 0.719 | NADH:ubiquinone oxidoreductase complex assembly factor 4 |  |
| [[COA4]] | 0.718 | cytochrome c oxidase assembly factor 4 homolog |  |
| [[THADA]] | 0.716 | THADA armadillo repeat containing |  |
| [[BRIX1]] | 0.715 | biogenesis of ribosomes BRX1 |  |
| [[GCFC2]] | 0.714 | GC-rich sequence DNA-binding factor 2 |  |
| [[SMARCAD1]] | 0.710 | SNF2 related chromatin remodeling ATPase with DExD box 1 |  |
| [[LDAH]] | 0.703 | lipid droplet associated hydrolase |  |
| [[ANAPC7]] | 0.701 | anaphase promoting complex subunit 7 |  |
| [[PHF14]] | 0.698 | PHD finger protein 14 |  |
| [[IMPACT]] | 0.697 | impact RWD domain protein |  |
| [[NUDT19]] | 0.696 | nudix hydrolase 19 |  |
| [[AGK]] | 0.696 | acylglycerol kinase |  |
| [[PES1]] | 0.695 | pescadillo ribosomal biogenesis factor 1 |  |
| [[ZNF195]] | 0.694 | zinc finger protein 195 |  |
| [[GTF2H3]] | 0.692 | general transcription factor IIH subunit 3 |  |
| [[YTHDC2]] | 0.691 | YTH N6-methyladenosine RNA binding protein C2 |  |
| [[FASTKD2]] | 0.691 | FASTK mitochondrial RNA regulator 2 |  |
| [[RIF1]] | 0.691 | replication timing regulatory factor 1 |  |
| [[JPX]] | 0.683 | JPX transcript, XIST activator |  |
| [[ICE2]] | 0.682 | interactor of little elongation complex ELL subunit 2 |  |
| [[TRMT61A]] | 0.681 | tRNA methyltransferase 61A |  |
| [[METTL1]] | 0.679 | methyltransferase 1, tRNA methylguanosine |  |
| [[ZNHIT6]] | 0.675 | zinc finger HIT-type containing 6 |  |
| [[SRFBP1]] | 0.670 | serum response factor binding protein 1 |  |
| [[TGFBRAP1]] | 0.669 | transforming growth factor beta receptor associated protein 1 |  |
| [[AIMP2]] | 0.665 | aminoacyl tRNA synthetase complex interacting multifunctional protein 2 |  |
| [[MIOS]] | 0.665 | meiosis regulator for oocyte development |  |
| [[DCAF17]] | 0.664 | DDB1 and CUL4 associated factor 17 |  |
| [[TXNRD3]] | 0.663 | thioredoxin reductase 3 |  |
| [[ZNF354B]] | 0.661 | zinc finger protein 354B |  |
| [[SMYD5]] | 0.661 | SMYD family member 5 |  |
| [[ZZZ3]] | 0.660 | zinc finger ZZ-type containing 3 |  |
| [[DIS3L]] | 0.659 | DIS3 like exosome 3'-5' exoribonuclease |  |
| [[ZNF783]] | 0.659 | zinc finger protein 783 | ⚠ only flagged evidence |
| [[TTC27]] | 0.658 | tetratricopeptide repeat domain 27 |  |
| [[RIOK1]] | 0.656 | RIO kinase 1 |  |
| [[TRIM44]] | 0.652 | TRIM family member 44 |  |
| [[DHX30]] | 0.652 | DExH-box helicase 30 |  |
| [[CEP83]] | 0.648 | centrosomal protein 83 |  |
| [[C12orf29]] | 0.648 | RNA 5'-phosphate and 3'-OH ligase 1 |  |
| [[PDCD2]] | 0.647 | programmed cell death 2 |  |
| [[PTCD2]] | 0.647 | pentatricopeptide repeat domain 2 |  |
| [[YLPM1]] | 0.647 | YLP motif containing 1 |  |
| [[MPHOSPH6]] | 0.640 | M-phase phosphoprotein 6 |  |
| [[COMMD10]] | 0.639 | COMM domain containing 10 |  |
| [[SNHG26]] | 0.635 | small nucleolar RNA host gene 26 |  |
| [[DNAJA3]] | 0.633 | DnaJ heat shock protein family (Hsp40) member A3 |  |
| [[MLH3]] | 0.633 | mutL homolog 3 |  |
| [[DRG2]] | 0.633 | developmentally regulated GTP binding protein 2 |  |
| [[SLX4IP]] | 0.631 | SLX4 interacting protein |  |
| [[DNAAF2]] | 0.631 | dynein axonemal assembly factor 2 |  |
| [[DUS3L]] | 0.629 | dihydrouridine synthase 3 like |  |
| [[ZNF320]] | 0.627 | zinc finger protein 320 |  |
| [[BMS1]] | 0.626 | BMS1 ribosome biogenesis factor |  |
| [[AFG1L]] | 0.626 | AFG1 like ATPase |  |
| [[EIF2B3]] | 0.626 | eukaryotic translation initiation factor 2B subunit gamma |  |
| [[LARS1]] | 0.623 | leucyl-tRNA synthetase 1 |  |
| [[NOL6]] | 0.621 | nucleolar protein 6 |  |
| [[NUBPL]] | 0.621 | NUBP iron-sulfur cluster assembly factor, mitochondrial |  |
| [[POLR1F]] | 0.620 | RNA polymerase I subunit F |  |
| [[ZBTB24]] | 0.620 | zinc finger and BTB domain containing 24 |  |
| [[CLUH]] | 0.620 | CLUH binding protein of NUMT mRNA |  |
| [[TMEM147-AS1]] | 0.619 | TMEM147 antisense RNA 1 |  |
| [[ACSF3]] | 0.618 | acyl-CoA synthetase family member 3 |  |
| [[PSMG1]] | 0.617 | proteasome assembly chaperone 1 |  |
| [[DCPS]] | 0.616 | decapping enzyme, scavenger |  |
| [[WDR18]] | 0.615 | WD repeat domain 18 |  |
| [[GATB]] | 0.614 | glutamyl-tRNA amidotransferase subunit B |  |
| [[MTIF2]] | 0.612 | mitochondrial translational initiation factor 2 |  |
| [[BCS1L]] | 0.609 | BCS1 ubiquinol-cytochrome c reductase complex chaperone |  |
| [[TADA2A]] | 0.609 | transcriptional adaptor 2A |  |
| [[ZFP62]] | 0.605 | ZFP62 zinc finger protein |  |
| [[U2SURP]] | 0.603 | U2 snRNP associated SURP domain containing |  |
| [[TRMT61B]] | 0.603 | tRNA methyltransferase 61B |  |
| [[ZPR1]] | 0.602 | ZPR1 zinc finger |  |
| [[EIF3D]] | 0.601 | eukaryotic translation initiation factor 3 subunit D |  |
| [[SLC35F2]] | 0.600 | solute carrier family 35 member F2 |  |
| [[RSL1D1]] | 0.599 | ribosomal L1 domain containing 1 |  |
| [[TATDN1]] | 0.596 | TatD DNase domain containing 1 |  |
| [[YDJC]] | 0.594 | YdjC chitooligosaccharide deacetylase homolog |  |
| [[HSF2BP]] | 0.593 | heat shock transcription factor 2 binding protein |  |
| [[UTP25]] | 0.592 | UTP25 small subunit processome component |  |
| [[COG2]] | 0.590 | component of oligomeric golgi complex 2 |  |
| [[TIMM9]] | 0.588 | translocase of inner mitochondrial membrane 9 |  |
| [[WDR46]] | 0.587 | WD repeat domain 46 |  |
| [[HGH1]] | 0.587 | HGH1 cochaperone |  |
| [[QTRT1]] | 0.586 | queuine tRNA-ribosyltransferase catalytic subunit 1 |  |
| [[MCCC2]] | 0.582 | methylcrotonyl-CoA carboxylase subunit 2 |  |
| [[FAM83H]] | 0.581 | scaffolding CK1 anchoring protein H |  |
| [[WDR35]] | 0.581 | WD repeat domain 35 |  |
| [[PALB2]] | 0.581 | partner and localizer of BRCA2 |  |
| [[SETD4]] | 0.580 | SET domain containing 4 |  |
| [[EIF6]] | 0.579 | eukaryotic translation initiation factor 6 |  |
| [[WDR75]] | 0.578 | WD repeat domain 75 |  |
| [[TMEM209]] | 0.577 | transmembrane protein 209 |  |
| [[HNRNPF]] | 0.575 | heterogeneous nuclear ribonucleoprotein F |  |
| [[NIFK]] | 0.572 | nucleolar protein interacting with the FHA domain of MKI67 |  |
| [[SF3A3]] | 0.570 | splicing factor 3a subunit 3 |  |
| [[EEFSEC]] | 0.568 | eukaryotic elongation factor, selenocysteine-tRNA specific |  |
| [[MRPS17]] | 0.566 | mitochondrial ribosomal protein S17 |  |
| [[CRADD]] | 0.564 | CARD and death domain containing adaptor protein |  |
| [[MMACHC]] | 0.563 | metabolism of cobalamin associated C |  |
| [[SLC5A6]] | 0.562 | solute carrier family 5 member 6 |  |
| [[C5orf63]] | 0.559 | chromosome 5 open reading frame 63 |  |
| [[PATZ1]] | 0.557 | POZ/BTB and AT hook containing zinc finger 1 |  |
| [[FBXW8]] | 0.556 | F-box and WD repeat domain containing 8 |  |
| [[RAD54L2]] | 0.555 | RAD54 like 2 |  |
| [[FAN1]] | 0.551 | FANCD2 and FANCI associated nuclease 1 |  |
| [[ANGEL1]] | 0.551 | angel homolog 1 |  |
| [[TFAM]] | 0.551 | transcription factor A, mitochondrial |  |
| [[USP24]] | 0.551 | ubiquitin specific peptidase 24 |  |
| [[MYC]] | 0.550 | MYC proto-oncogene, bHLH transcription factor |  |
| [[DPH2]] | 0.550 | diphthamide biosynthesis 2 |  |
| [[METTL2A]] | 0.549 | methyltransferase 2A, tRNA N3-cytidine |  |
| [[DMAC2L]] | 0.549 | distal membrane arm assembly component 2 like |  |
| [[RRP9]] | 0.544 | ribosomal RNA processing 9, U3 small nucleolar RNA binding protein |  |
| [[ZC3H8]] | 0.543 | zinc finger CCCH-type containing 8 |  |
| [[SLC12A2-DT]] | 0.541 | SLC12A2 divergent transcript |  |
| [[AFG3L2]] | 0.539 | AFG3 like matrix AAA peptidase subunit 2 |  |
| [[PIGL]] | 0.538 | phosphatidylinositol glycan anchor biosynthesis class L |  |
| [[RPF2]] | 0.537 | ribosome production factor 2 homolog |  |
| [[FLAD1]] | 0.535 | flavin adenine dinucleotide synthetase 1 |  |
| [[PRORP]] | 0.532 | protein only RNase P catalytic subunit |  |
| [[ASAH2B]] | 0.532 | N-acylsphingosine amidohydrolase 2B |  |
| [[E2F5]] | 0.530 | E2F transcription factor 5 |  |
| [[MRPS7]] | 0.529 | mitochondrial ribosomal protein S7 |  |
| [[IRS1]] | 0.527 | insulin receptor substrate 1 |  |
| [[TCHP]] | 0.526 | trichoplein keratin filament binding |  |
| [[SETMAR]] | 0.523 | SET and mariner transposase domain methyltransferase |  |
| [[SPRYD4]] | 0.521 | SPRY domain containing 4 |  |
| [[PUDP]] | 0.519 | pseudouridine 5'-phosphatase |  |
| [[QSER1]] | 0.516 | glutamine and serine rich 1 |  |
| [[NCBP2]] | 0.514 | nuclear cap binding protein subunit 2 |  |
| [[CFAP97]] | 0.513 | cilia and flagella associated protein 97 |  |
| [[QRSL1]] | 0.511 | glutaminyl-tRNA amidotransferase subunit QRSL1 |  |
| [[CIAO1]] | 0.507 | cytosolic iron-sulfur assembly component 1 |  |
| [[CASC19]] | 0.506 | cancer susceptibility 19 |  |
| [[SCMH1]] | 0.506 | Scm polycomb group protein homolog 1 |  |
| [[PWP1]] | 0.504 | PWP1 homolog, endonuclein |  |
| [[TAF1B]] | 0.503 | TATA-box binding protein associated factor, RNA polymerase I subunit B |  |
| [[RRN3P1]] | 0.503 | RRN3 pseudogene 1 |  |
| [[HUS1]] | 0.501 | HUS1 checkpoint clamp component |  |
| [[PRKAR1B]] | 0.496 | protein kinase cAMP-dependent type I regulatory subunit beta |  |
| [[MTREX]] | 0.496 | Mtr4 exosome RNA helicase |  |
| [[DDX18]] | 0.495 | DEAD-box helicase 18 |  |
| [[ZNF354A]] | 0.493 | zinc finger protein 354A |  |
| [[EIF3A]] | 0.492 | eukaryotic translation initiation factor 3 subunit A |  |
| [[CHMP6]] | 0.490 | charged multivesicular body protein 6 |  |
| [[PEX10]] | 0.489 | peroxisomal biogenesis factor 10 |  |
| [[RBM45]] | 0.486 | RNA binding motif protein 45 |  |
| [[SSB]] | 0.485 | small RNA binding exonuclease protection factor La |  |
| [[ME3]] | 0.483 | malic enzyme 3 |  |
| [[GSTO2]] | 0.483 | glutathione S-transferase omega 2 |  |
| [[PSEN2]] | 0.483 | presenilin 2 |  |
| [[POLR2D]] | 0.481 | RNA polymerase II subunit D |  |
| [[PCSK6]] | 0.479 | proprotein convertase subtilisin/kexin type 6 |  |
| [[TAF1A]] | 0.476 | TATA-box binding protein associated factor, RNA polymerase I subunit A |  |
| [[CFAP298]] | 0.475 | cilia and flagella associated protein 298 |  |
| [[TXLNGY-1]] | 0.475 | — |  |
| [[SNX5]] | 0.468 | sorting nexin 5 |  |
| [[RPUSD3]] | 0.463 | RNA pseudouridine synthase D3 |  |
| [[TFAP4]] | 0.461 | transcription factor AP-4 |  |
| [[NANP]] | 0.461 | N-acetylneuraminic acid phosphatase |  |
| [[TMBIM4]] | 0.460 | transmembrane BAX inhibitor motif containing 4 |  |
| [[ATXN10]] | 0.458 | ataxin 10 |  |
| [[PROSER1]] | 0.457 | proline and serine rich 1 |  |
| [[IKZF3]] | 0.457 | IKAROS family zinc finger 3 |  |
| [[KIF7]] | 0.453 | kinesin family member 7 |  |
| [[ANKRD17]] | 0.452 | ankyrin repeat domain 17 |  |
| [[GAR1]] | 0.451 | GAR1 ribonucleoprotein |  |
| [[TRUB2]] | 0.451 | TruB pseudouridine synthase family member 2 |  |
| [[ATAD1]] | 0.438 | ATPase family AAA domain containing 1 |  |
| [[NOC4L]] | 0.437 | nucleolar complex associated 4 homolog |  |
| [[SDHAP3]] | 0.437 | SDHA pseudogene 3 |  |
| [[FAM120C]] | 0.436 | family with sequence similarity 120 member C |  |
| [[ZNF529]] | 0.430 | zinc finger protein 529 |  |
| [[UBE2D4]] | 0.426 | ubiquitin conjugating enzyme E2 D4 |  |
| [[PTER]] | 0.420 | phosphotriesterase related |  |
| [[B3GNTL1]] | 0.419 | queuosine-tRNA galactosyltransferase |  |
| [[PAXIP1]] | 0.417 | PAX interacting protein 1 |  |
| [[MKKS]] | 0.412 | MKKS centrosomal shuttling protein |  |
| [[DICER1]] | 0.405 | dicer 1, ribonuclease III |  |
| [[GGACT]] | 0.404 | gamma-glutamylamine cyclotransferase |  |
| [[ABHD13]] | 0.403 | abhydrolase domain containing 13 |  |
| [[ZFP69B]] | 0.390 | ZFP69 zinc finger protein B |  |
| [[EXO5]] | 0.383 | exonuclease 5 |  |
| [[SNAPC4]] | 0.381 | small nuclear RNA activating complex polypeptide 4 |  |
| [[TBL3]] | 0.381 | transducin beta like 3 |  |
| [[STEAP1]] | 0.381 | STEAP family member 1 |  |
| [[PDE12]] | 0.380 | phosphodiesterase 12 |  |
| [[ZNF605]] | 0.367 | zinc finger protein 605 |  |
| [[C5orf22]] | 0.349 | chromosome 5 open reading frame 22 |  |
| [[RAPGEF1]] | 0.346 | Rap guanine nucleotide exchange factor 1 |  |
| [[ULK2]] | 0.345 | unc-51 like autophagy activating kinase 2 |  |
| [[PPWD1]] | 0.344 | peptidylprolyl isomerase domain and WD repeat containing 1 |  |
| [[NAPRT]] | 0.326 | nicotinate phosphoribosyltransferase |  |
| [[POLE4]] | 0.300 | DNA polymerase epsilon 4, accessory subunit | ⚠ only flagged evidence |
| [[TRAF3]] | 0.288 | TNF receptor associated factor 3 |  |
| [[FOXP4-AS1]] | 0.287 | FOXP4 antisense RNA 1 |  |
| [[FAM53B]] | 0.235 | family with sequence similarity 53 member B | ⚠ only flagged evidence |
| [[MSL2]] | 0.189 | MSL complex subunit 2 |  |

## − arm (52)

| Gene | Projection | Name | Alert |
|---|---|---|---|
| [[PHF1]] | -0.684 | PHD finger protein 1 |  |
| [[MXD1]] | -0.653 | MAX dimerization protein 1 |  |
| [[GNAS]] | -0.636 | GNAS complex locus |  |
| [[FBXO33]] | -0.620 | F-box protein 33 |  |
| [[PNPLA8]] | -0.616 | patatin like domain 8, phospholipase A2 |  |
| [[RAB5B]] | -0.608 | RAB5B, member RAS oncogene family |  |
| [[ANG]] | -0.606 | angiogenin |  |
| [[SLC17A7]] | -0.595 | solute carrier family 17 member 7 |  |
| [[RNASE4]] | -0.588 | ribonuclease A family member 4 |  |
| [[ARL3]] | -0.583 | ARF like GTPase 3 |  |
| [[CSRP2]] | -0.577 | cysteine and glycine rich protein 2 |  |
| [[PLAG1]] | -0.576 | PLAG1 zinc finger |  |
| [[SELENOW]] | -0.572 | selenoprotein W |  |
| [[MICA]] | -0.555 | MHC class I polypeptide-related sequence A |  |
| [[CYP46A1]] | -0.554 | cytochrome P450 family 46 subfamily A member 1 |  |
| [[NLGN2]] | -0.554 | neuroligin 2 |  |
| [[DCAF6]] | -0.534 | DDB1 and CUL4 associated factor 6 |  |
| [[CASP9]] | -0.521 | caspase 9 |  |
| [[MTCH1]] | -0.520 | mitochondrial carrier 1 |  |
| [[PAIP2B]] | -0.517 | poly(A) binding protein interacting protein 2B |  |
| [[NUMB]] | -0.514 | NUMB endocytic adaptor protein |  |
| [[MEF2D]] | -0.510 | myocyte enhancer factor 2D |  |
| [[PMEL]] | -0.501 | premelanosome protein |  |
| [[CCNI]] | -0.492 | cyclin I |  |
| [[DNAJC1]] | -0.489 | DnaJ heat shock protein family (Hsp40) member C1 |  |
| [[MRPS6]] | -0.486 | mitochondrial ribosomal protein S6 |  |
| [[SYNJ1]] | -0.481 | synaptojanin 1 |  |
| [[CXCR4]] | -0.479 | C-X-C motif chemokine receptor 4 |  |
| [[PLEKHH2]] | -0.477 | pleckstrin homology, MyTH4 and FERM domain containing H2 |  |
| [[RIOK3]] | -0.475 | RIO kinase 3 |  |
| [[HOOK3]] | -0.473 | hook microtubule tethering protein 3 |  |
| [[MAGI3]] | -0.461 | membrane associated guanylate kinase, WW and PDZ domain containing 3 |  |
| [[PDE6D]] | -0.454 | phosphodiesterase 6D |  |
| [[CTSV]] | -0.451 | cathepsin V |  |
| [[CHP1]] | -0.437 | calcineurin like EF-hand protein 1 |  |
| [[SWT1]] | -0.432 | SWT1 RNA endoribonuclease homolog |  |
| [[PDE5A]] | -0.415 | phosphodiesterase 5A |  |
| [[PPP2R3A]] | -0.402 | protein phosphatase 2 regulatory subunit B''alpha |  |
| [[SLC5A3]] | -0.401 | solute carrier family 5 member 3 |  |
| [[RAPGEF2]] | -0.397 | Rap guanine nucleotide exchange factor 2 |  |
| [[SLC6A8]] | -0.392 | solute carrier family 6 member 8 |  |
| [[IQCD]] | -0.391 | dynein regulatory complex subunit 10 |  |
| [[RALGPS2]] | -0.390 | Ral GEF with PH domain and SH3 binding motif 2 |  |
| [[PTMS]] | -0.362 | parathymosin |  |
| [[NRBP1]] | -0.325 | nuclear receptor binding protein 1 |  |
| [[PI4K2B]] | -0.319 | phosphatidylinositol 4-kinase type 2 beta |  |
| [[CASK]] | -0.288 | calcium/calmodulin dependent serine protein kinase |  |
| [[ITSN1]] | -0.264 | intersectin 1 |  |
| [[USP15]] | -0.253 | ubiquitin specific peptidase 15 |  |
| [[CCDC110]] | -0.240 | coiled-coil domain containing 110 |  |
| [[FRYL]] | -0.210 | FRY like transcription coactivator |  |
| [[DLG1]] | -0.186 | discs large MAGUK scaffold protein 1 |  |

## Data

- `graph/nodes.parquet` — module == 1; `graph/modules.parquet` — module == 1; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [0] (drug-dose × line)
