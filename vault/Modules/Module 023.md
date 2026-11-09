---
module: 23
type: "module"
n_genes: 179
n_plus: 144
n_minus: 35
arms_opposite: true
mean_cos_between_arms: -0.3404281437397003
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 023

*179 genes (144 in the + arm, 35 in the − arm) · [[Module 023.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34). The + arm rises where the − arm falls. Arm = the side of the module's main direction a gene sits on.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of the + arm minus the − arm (`graph/module_pooled_z.npy`, row 22), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it (+ arm up, − arm down): [[Idarubicin (hydrochloride) (drug)]] 5 µM (+21.5, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 5 µM (+17.5, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (+10.6, ⚠ cell-cycle shift); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (+8.4, ⚠ cell-cycle shift); [[Topotecan (hydrochloride) (drug)]] 5 µM (+7.7, ⚠ toxic; cell-cycle shift); [[Auranofin (drug)]] 5 µM (+6.5); [[Epirubicin (hydrochloride) (drug)]] 5 µM (+6.4, ⚠ cell-cycle shift); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+6.1); [[Harringtonine (drug)]] 5 µM (+6.0, ⚠ cell-cycle shift); [[Selinexor (drug)]] 5 µM (+4.9, ⚠ cell-cycle shift); [[Ponatinib (drug)]] 5 µM (+3.7); [[Homoharringtonine (drug)]] 0.05 µM (+3.6); [[Trametinib (drug)]] 0.5 µM (+2.7); [[Binimetinib (drug)]] 0.05 µM (+2.7); [[Ponatinib (drug)]] 0.5 µM (+2.6); [[Cobimetinib (drug)]] 0.5 µM (+2.4); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM (+2.3); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM (+2.3) (80 in all, 26 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)
- Lower it: [[Panobinostat (drug)]] 5 µM (-14.8, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (-14.4, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (-13.8, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (-9.1, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (-7.2); [[Belinostat (drug)]] 0.5 µM (-6.9, ⚠ cell-cycle shift); [[Brivudine (drug)]] 5 µM (-5.4); [[c-Kit-IN-1 (drug)]] 0.05 µM (-4.9, ⚠ unreliable plate only); [[Niclosamide (olamine) (drug)]] 5 µM (-4.3, ⚠ toxic; cell-cycle shift); [[Ixazomib citrate (drug)]] 5 µM (-4.2, ⚠ cell-cycle shift); [[Ixazomib citrate (drug)]] 0.5 µM (-2.9); [[Abemaciclib (drug)]] 0.5 µM (-1.6); [[Berberine (chloride hydrate) (drug)]] 5 µM (-1.6); [[Pyridoxine (hydrochloride) (drug)]] 5 µM (-1.5); [[Abemaciclib (drug)]] 5 µM (-1.5); [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM (-1.5); [[Dimethyl fumarate (drug)]] 5 µM (-1.5); [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM (-1.4) (54 in all, 17 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[SW480 (line)]], [[PANC-1 (line)]], [[LoVo (line)]], [[NCI-H460 (line)]], [[NCI-H2030 (line)]], [[HOP62 (line)]], [[LOX-IMVI (line)]], [[NCI-H1573 (line)]]

## + arm (144)

| Gene | Projection | Name |
|---|---|---|
| [[ATE1OSP]] | 0.922 | ATE1 opposite strand, pseudogene |
| [[OXA1L-DT]] | 0.920 | OXA1L divergent transcript |
| [[MFF-DT]] | 0.893 | MFF divergent transcript |
| [[PPP1R12A-AS2]] | 0.891 | PPP1R12A antisense RNA 2 |
| [[THAP2]] | 0.883 | THAP domain containing 2 |
| [[CHD1-DT]] | 0.876 | CHD1 divergent transcript |
| [[SEPTIN7-DT]] | 0.856 | SEPTIN7 divergent transcript |
| [[MAILR]] | 0.854 | macrophage interferon regulatory lncRNA |
| [[DNAI4]] | 0.854 | dynein axonemal intermediate chain 4 |
| [[LINC01004]] | 0.851 | — |
| [[CASS4]] | 0.850 | Cas scaffold protein family member 4 |
| [[CDKL3]] | 0.849 | cyclin dependent kinase like 3 |
| [[ANKRD17-DT]] | 0.847 | ANKRD17 divergent transcript |
| [[ERCC6L2-AS1]] | 0.843 | ERCC6L2 antisense RNA 1 |
| [[PRANCR]] | 0.842 | progenitor renewal associated non-coding RNA |
| [[N4BP2L1]] | 0.838 | NEDD4 binding protein 2 like 1 |
| [[RFX3-DT]] | 0.835 | RFX3 divergent transcript |
| [[METTL6]] | 0.834 | methyltransferase 6, tRNA N3-cytidine |
| [[GTF2IRD2]] | 0.832 | GTF2I repeat domain containing 2 |
| [[TAS2R4]] | 0.831 | taste 2 receptor member 4 |
| [[TBCE-1]] | 0.830 | — |
| [[AHI1-DT]] | 0.828 | AHI1 divergent transcript |
| [[HEXIM2-AS1]] | 0.822 | HEXIM2 antisense RNA 1 |
| [[PPP1R3F]] | 0.816 | protein phosphatase 1 regulatory subunit 3F |
| [[LRRC37A3]] | 0.815 | leucine rich repeat containing 37 member A3 |
| [[ITFG2-AS1]] | 0.811 | ITFG2 antisense RNA 1 |
| [[KMT2E-AS1]] | 0.793 | KMT2E antisense RNA 1 |
| [[GALNT7-DT]] | 0.791 | GALNT7 divergent transcript |
| [[GTF2IRD2B]] | 0.790 | GTF2I repeat domain containing 2B |
| [[ANKHD1-DT]] | 0.788 | ANKHD1 divergent transcript |
| [[C3orf38]] | 0.785 | chromosome 3 open reading frame 38 |
| [[TTC32]] | 0.770 | tetratricopeptide repeat domain 32 |
| [[EIF3J-DT]] | 0.769 | EIF3J divergent transcript |
| [[EPM2A-DT]] | 0.766 | EPM2A divergent transcript |
| [[MAIP1]] | 0.763 | matrix AAA peptidase interacting protein 1 |
| [[NSMCE1-DT]] | 0.763 | NSMCE1 divergent transcript |
| [[CCDC59]] | 0.762 | coiled-coil domain containing 59 |
| [[ENTPD3-AS1]] | 0.761 | ENTPD3, EIF1B and MYRIP antisense RNA 1 |
| [[KRBOX5]] | 0.757 | KRAB domain containing 5 |
| [[ATF5]] | 0.752 | activating transcription factor 5 |
| [[ZNF425]] | 0.749 | zinc finger protein 425 |
| [[PPP5D1P-1]] | 0.745 | — |
| [[KANSL1L]] | 0.742 | KAT8 regulatory NSL complex subunit 1 like |
| [[KLRK1-AS1]] | 0.735 | KLRK1 antisense RNA 1 |
| [[MSTO1]] | 0.732 | misato mitochondrial distribution and morphology regulator 1 |
| [[MR1]] | 0.729 | major histocompatibility complex, class I-related |
| [[UGDH-AS1]] | 0.728 | UGDH antisense RNA 1 |
| [[CYB5D2]] | 0.727 | cytochrome b5 domain containing 2 |
| [[HAVCR2]] | 0.725 | hepatitis A virus cellular receptor 2 |
| [[C1S]] | 0.724 | complement C1s |
| [[ZNF785]] | 0.722 | zinc finger protein 785 |
| [[C12orf60]] | 0.717 | chromosome 12 open reading frame 60 |
| [[MKRN3]] | 0.716 | makorin ring finger protein 3 |
| [[ZNF846]] | 0.710 | zinc finger protein 846 |
| [[AMY2B]] | 0.710 | amylase alpha 2B |
| [[CFAP43]] | 0.704 | cilia and flagella associated protein 43 |
| [[ARMCX5-GPRASP2]] | 0.702 | ARMCX5-GPRASP2 readthrough |
| [[RBM48]] | 0.699 | RNA binding motif protein 48 |
| [[C19orf18]] | 0.697 | chromosome 19 open reading frame 18 |
| [[CCDC122]] | 0.696 | coiled-coil domain containing 122 |
| [[ANKHD1-EIF4EBP3]] | 0.695 | ANKHD1-EIF4EBP3 readthrough |
| [[SPTY2D1OS]] | 0.695 | mitochondrial sheath formation associated |
| [[ZCWPW2]] | 0.694 | zinc finger CW-type and PWWP domain containing 2 |
| [[YARS2]] | 0.691 | tyrosyl-tRNA synthetase 2 |
| [[SLC13A3]] | 0.688 | solute carrier family 13 member 3 |
| [[ASH1L]] | 0.685 | ASH1 like histone lysine methyltransferase |
| [[RRAGC-DT]] | 0.681 | RRAGC divergent transcript |
| [[NMNAT1]] | 0.681 | nicotinamide nucleotide adenylyltransferase 1 |
| [[ZNF91]] | 0.681 | zinc finger protein 91 |
| [[TP53]] | 0.677 | tumor protein p53 |
| [[PCF11]] | 0.676 | PCF11 cleavage and polyadenylation factor subunit |
| [[ERMAP]] | 0.675 | erythroblast membrane associated protein (Scianna blood group) |
| [[DNAJC27-AS1]] | 0.673 | DNAJC27 antisense RNA 1 |
| [[C1orf43]] | 0.668 | lipid transport auxiliary protein 1 |
| [[GIPC2]] | 0.668 | GIPC PDZ domain containing family member 2 |
| [[UFC1]] | 0.665 | ubiquitin-fold modifier conjugating enzyme 1 |
| [[ZSCAN16-AS1]] | 0.658 | ZSCAN16 antisense RNA 1 |
| [[HOMEZ]] | 0.654 | homeobox and leucine zipper encoding |
| [[MED13]] | 0.653 | mediator complex subunit 13 |
| [[GPRASP1]] | 0.648 | G protein-coupled receptor associated sorting protein 1 |
| [[SBF2-AS1]] | 0.647 | SBF2 antisense RNA 1 |
| [[CAB39L]] | 0.645 | calcium binding protein 39 like |
| [[HOXA-AS2]] | 0.639 | HOXA cluster antisense RNA 2 |
| [[BICRAL]] | 0.639 | BICRA like chromatin remodeling complex associated protein |
| [[NDUFA6-DT]] | 0.637 | NDUFA6 divergent transcript |
| [[MTUS1-DT]] | 0.634 | MTUS1 divergent transcript |
| [[HPS1]] | 0.632 | HPS1 biogenesis of lysosomal organelles complex 3 subunit 1 |
| [[ZNF253]] | 0.630 | zinc finger protein 253 |
| [[AGBL3]] | 0.621 | AGBL carboxypeptidase 3 |
| [[HSD17B14]] | 0.621 | hydroxysteroid 17-beta dehydrogenase 14 |
| [[YAE1]] | 0.620 | YAE1 maturation factor of ABCE1 |
| [[DMXL1-DT]] | 0.614 | DMXL1 divergent transcript |
| [[BORCS7]] | 0.612 | BLOC-1 related complex subunit 7 |
| [[CD72]] | 0.610 | CD72 molecule |
| [[TMEM80]] | 0.609 | transmembrane protein 80 |
| [[ZNF345]] | 0.608 | zinc finger protein 345 |
| [[SLC9B1]] | 0.607 | solute carrier family 9 member B1 |
| [[TMEM91]] | 0.604 | transmembrane protein 91 |
| [[APOLD1]] | 0.601 | apolipoprotein L domain containing 1 |
| [[ICA1L]] | 0.600 | islet cell autoantigen 1 like |
| [[PSMD6-AS2]] | 0.592 | PSMD6 antisense RNA 2 |
| [[KIF27]] | 0.591 | kinesin family member 27 |
| [[NR1H3]] | 0.587 | nuclear receptor subfamily 1 group H member 3 |
| [[ZNF665]] | 0.585 | zinc finger protein 665 |
| [[SCYL3]] | 0.577 | SCY1 like pseudokinase 3 |
| [[ZDHHC1]] | 0.574 | zDHHC palmitoyltransferase 1 |
| [[GPRASP3]] | 0.573 | G protein-coupled receptor associated sorting protein family member 3 |
| [[ST20-MTHFS]] | 0.571 | ST20-MTHFS readthrough |
| [[SUPT7L]] | 0.569 | SPT7 like, STAGA complex subunit gamma |
| [[MTRF1]] | 0.567 | mitochondrial translation release factor 1 |
| [[MCPH1-AS1]] | 0.562 | MCPH1 antisense RNA 1 |
| [[COPB2-DT]] | 0.555 | COPB2 divergent transcript |
| [[DAZAP2]] | 0.553 | DAZ associated protein 2 |
| [[RBM3]] | 0.544 | RNA binding motif protein 3 |
| [[KCNRG]] | 0.543 | potassium channel regulator |
| [[C21orf62-AS1]] | 0.540 | EPCIP antisense RNA 1 |
| [[SMIM4]] | 0.540 | ubiquinol-cytochrome c reductase complex assembly factor 5 |
| [[VAMP5]] | 0.539 | vesicle associated membrane protein 5 |
| [[ZNF207]] | 0.524 | zinc finger protein 207 |
| [[IBA57]] | 0.523 | iron-sulfur cluster assembly factor IBA57 |
| [[SLC35B3]] | 0.518 | solute carrier family 35 member B3 |
| [[RBM39]] | 0.516 | RNA binding motif protein 39 |
| [[SSBP1]] | 0.513 | single stranded DNA binding protein 1 |
| [[HLA-V-1]] | 0.511 | — |
| [[PUS10]] | 0.504 | pseudouridine synthase 10 |
| [[TRPC1]] | 0.500 | transient receptor potential cation channel subfamily C member 1 |
| [[ZDBF2]] | 0.492 | zinc finger DBF-type containing 2 |
| [[PLAGL1]] | 0.489 | PLAG1 like zinc finger 1 |
| [[AMZ2]] | 0.488 | archaelysin family metallopeptidase 2 |
| [[LINC02482]] | 0.486 | long independently transcribed non-coding RNA 2482 |
| [[ZNF626]] | 0.478 | zinc finger protein 626 |
| [[ZNF630]] | 0.473 | zinc finger protein 630 |
| [[LAMTOR3]] | 0.452 | late endosomal/lysosomal adaptor, MAPK and MTOR activator 3 |
| [[KIAA0753]] | 0.451 | KIAA0753 |
| [[LINC02609]] | 0.444 | long independently transcribed non-coding RNA 2609 |
| [[SPATA24]] | 0.437 | spermatogenesis associated 24 |
| [[RECQL5]] | 0.434 | RecQ like helicase 5 |
| [[PARP11]] | 0.419 | poly(ADP-ribose) polymerase family member 11 |
| [[RNF32-DT]] | 0.394 | RNF32 divergent transcript |
| [[CA3]] | 0.377 | carbonic anhydrase 3 |
| [[ATF7IP2]] | 0.365 | activating transcription factor 7 interacting protein 2 |
| [[UBE2D3]] | 0.304 | ubiquitin conjugating enzyme E2 D3 |
| [[TESMIN]] | 0.299 | testis expressed metallothionein like protein |
| [[CLCN2]] | 0.137 | chloride voltage-gated channel 2 |

## − arm (35)

| Gene | Projection | Name |
|---|---|---|
| [[SMYD3]] | -0.690 | SET and MYND domain containing 3 |
| [[ARHGAP8]] | -0.677 | Rho GTPase activating protein 8 |
| [[APMAP]] | -0.670 | adipocyte plasma membrane associated protein |
| [[EDA]] | -0.662 | ectodysplasin A |
| [[NHP2]] | -0.645 | NHP2 ribonucleoprotein |
| [[DGKD]] | -0.635 | diacylglycerol kinase delta |
| [[SIPA1]] | -0.627 | signal-induced proliferation-associated 1 |
| [[ENDOD1]] | -0.619 | endonuclease domain containing 1 |
| [[PLXND1]] | -0.615 | plexin D1 |
| [[RGS19]] | -0.603 | regulator of G protein signaling 19 |
| [[EML4]] | -0.597 | EMAP like 4 |
| [[HYAL2]] | -0.591 | hyaluronidase 2 |
| [[RNFT2]] | -0.581 | ring finger protein, transmembrane 2 |
| [[MATCAP1]] | -0.576 | microtubule associated tyrosine carboxypeptidase 1 |
| [[TRAK1]] | -0.575 | trafficking kinesin protein 1 |
| [[GMDS]] | -0.574 | GDP-mannose 4,6-dehydratase |
| [[CBR1]] | -0.564 | carbonyl reductase 1 |
| [[SLC29A1]] | -0.562 | solute carrier family 29 member 1 (Augustine blood group) |
| [[SPATA13]] | -0.557 | spermatogenesis associated 13 |
| [[CYRIB]] | -0.535 | CYFIP related Rac1 interactor B |
| [[LRBA]] | -0.530 | LPS responsive beige-like anchor protein |
| [[XPR1]] | -0.514 | xenotropic and polytropic retrovirus receptor 1 |
| [[PPM1G]] | -0.498 | protein phosphatase, Mg2+/Mn2+ dependent 1G |
| [[CARMIL1]] | -0.492 | capping protein regulator and myosin 1 linker 1 |
| [[PTPN3]] | -0.492 | protein tyrosine phosphatase non-receptor type 3 |
| [[CERS6]] | -0.491 | ceramide synthase 6 |
| [[PRRG1]] | -0.481 | proline rich and Gla domain 1 |
| [[SOAT1]] | -0.453 | sterol O-acyltransferase 1 |
| [[ARMC9]] | -0.448 | armadillo repeat containing 9 |
| [[BAK1]] | -0.448 | BCL2 antagonist/killer 1 |
| [[ARHGAP32]] | -0.437 | Rho GTPase activating protein 32 |
| [[GTDC1]] | -0.419 | queuosine-tRNA mannosyltransferase |
| [[NLRP2]] | -0.419 | NLR family pyrin domain containing 2 |
| [[PRKCI]] | -0.373 | protein kinase C iota |
| [[PPP2R2A]] | -0.243 | protein phosphatase 2 regulatory subunit Balpha |

## Data

- `graph/nodes.parquet` — module == 23; `graph/modules.parquet` — module == 23; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [22] (drug-dose × line)
