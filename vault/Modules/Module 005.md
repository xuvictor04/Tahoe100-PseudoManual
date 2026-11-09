---
module: 5
type: "module"
n_genes: 244
n_plus: 206
n_minus: 38
arms_opposite: true
mean_cos_between_arms: -0.2894759774208069
label: "MYC targets v2"
label_source: "hallmark"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 005

*MYC targets v2 · 244 genes (206 in the + arm, 38 in the − arm) · [[Module 005.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29). The + arm rises where the − arm falls. Arm = the side of the module's main direction a gene sits on.

Label from the validation stage: **MYC targets v2** (hallmark, q 1e-09; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| + | MYC targets v2 | hallmark | 13/206 | 16.4 | 1e-09 |
| + | rRNA processing | reactome | 20/206 | 7.17 | 7e-09 |
| all | MYC targets v2 | hallmark | 13/244 | 13.8 | 8e-09 |
| + | rRNA processing in the nucleus and cytosol | reactome | 19/206 | 7.44 | 1e-08 |
| all | rRNA processing | reactome | 20/244 | 6.06 | 1e-07 |
| all | rRNA processing in the nucleus and cytosol | reactome | 19/244 | 6.28 | 2e-07 |
| + | rRNA modification in the nucleus and cytosol | reactome | 11/206 | 13.9 | 3e-07 |
| + | Metabolism of RNA | reactome | 33/206 | 3.31 | 1e-06 |

## Drugs that move it

*Mean pooled z of the + arm minus the − arm (`graph/module_pooled_z.npy`, row 4), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it (+ arm up, − arm down): [[c-Kit-IN-1 (drug)]] 0.05 µM (+9.9, ⚠ unreliable plate only); [[Idarubicin (hydrochloride) (drug)]] 5 µM (+6.9, ⚠ cell-cycle shift); [[Topotecan (hydrochloride) (drug)]] 5 µM (+6.6, ⚠ toxic; cell-cycle shift); [[Auranofin (drug)]] 5 µM (+5.8); [[c-Kit-IN-1 (drug)]] 5 µM (+4.9); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+4.8); [[Ixazomib citrate (drug)]] 5 µM (+4.7, ⚠ cell-cycle shift); [[Topotecan (hydrochloride) (drug)]] 0.5 µM (+4.3, ⚠ cell-cycle shift); [[TAK-733 (drug)]] 5 µM (+4.1); [[EX229 (drug)]] 5 µM (+4.1); [[Belumosudil (drug)]] 5 µM (+4.0); [[TAK-901 (drug)]] 0.05 µM (+3.6); [[PH-797804 (drug)]] 5 µM (+3.6); [[Abemaciclib (drug)]] 5 µM (+3.4); [[5-Azacytidine (drug)]] 5 µM (+2.7) (108 in all, 27 with an alert ⚠; shown: the 10 strongest and the 5 next strongest without an alert)
- Lower it: [[Tucidinostat (drug)]] 5 µM (-5.9); [[Homoharringtonine (drug)]] 5 µM (-5.4, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (-5.1, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (-5.1, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (-4.9, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 0.5 µM (-4.5, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (-3.5, ⚠ cell-cycle shift); [[Trametinib (drug)]] 5 µM (-3.4, ⚠ cell-cycle shift); [[Trametinib (drug)]] 0.5 µM (-3.3); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM (-3.3); [[Cobimetinib (drug)]] 5 µM (-3.1); [[Brivudine (drug)]] 5 µM (-3.1); [[Binimetinib (drug)]] 5 µM (-3.0); [[Binimetinib (drug)]] 0.5 µM (-3.0); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM (-2.7); [[Pitavastatin (Calcium) (drug)]] 0.5 µM (-2.4); [[Radotinib (drug)]] 5 µM (-2.2) (87 in all, 19 with an alert ⚠; shown: the 10 strongest and the 7 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[NCI-H460 (line)]], [[PANC-1 (line)]], [[SW480 (line)]], [[RKO (line)]], [[SW1417 (line)]], [[MIA PaCa-2 (line)]], [[CFPAC-1 (line)]], [[NCI-H1792 (line)]]

## Candidate new members

*Members not annotated to the set their arm is enriched for, ranked by mean cos to the annotated members (`validation/novel_members.csv`); ⚠ = a reason to doubt the gene's place (in the vector space only through flagged drug-doses), kept in its rank. 78 candidates, none with an alert; shown: the 15 strongest.*

| # | Gene | Set | Mean cos |
|---|---|---|---|
| 1 | [[WDR4]] | MYC targets v2 | +0.75 |
| 2 | [[TWNK]] | MYC targets v2 | +0.71 |
| 3 | [[NOP16]] | ribosome biogenesis | +0.70 |
| 4 | [[PNO1]] | MYC targets v2 | +0.68 |
| 5 | [[MRTO4]] | rRNA modification in the nucleus and cytosol | +0.68 |
| 6 | [[DHX37]] | MYC targets v2 | +0.68 |
| 7 | [[URB2]] | MYC targets v2 | +0.67 |
| 8 | [[PUS1]] | rRNA modification in the nucleus and cytosol | +0.67 |
| 9 | [[DDX31]] | MYC targets v2 | +0.66 |
| 10 | [[GTPBP4]] | MYC targets v2 | +0.66 |
| 11 | [[DHX33]] | MYC targets v2 | +0.65 |
| 12 | [[TSR1]] | MYC targets v2 | +0.65 |
| 13 | [[NIP7]] | rRNA modification in the nucleus and cytosol | +0.64 |
| 14 | [[GEMIN4]] | MYC targets v2 | +0.64 |
| 15 | [[GRWD1]] | ribosome biogenesis | +0.63 |

## + arm (206)

| Gene | Projection | Name |
|---|---|---|
| [[WDR4]] | 0.933 | WDR4 tRNA N7-guanosine methyltransferase non-catalytic subunit |
| [[PUS1]] | 0.901 | pseudouridine synthase 1 |
| [[TWNK]] | 0.850 | twinkle mtDNA helicase |
| [[ALG8]] | 0.842 | ALG8 alpha-1,3-glucosyltransferase |
| [[MRTO4]] | 0.841 | MRT4 homolog, ribosome maturation factor |
| [[DHX37]] | 0.834 | DEAH-box helicase 37 |
| [[NOP16]] | 0.831 | NOP16 nucleolar protein |
| [[NOP2]] | 0.827 | NOP2 nucleolar protein |
| [[PRMT3]] | 0.821 | protein arginine methyltransferase 3 |
| [[GTPBP4]] | 0.814 | GTP binding protein 4 |
| [[TSR1]] | 0.812 | TSR1 ribosome maturation factor |
| [[GRWD1]] | 0.809 | glutamate rich WD repeat containing 1 |
| [[GNL3L]] | 0.799 | G protein nucleolar 3 like |
| [[ARMC6]] | 0.799 | armadillo repeat containing 6 |
| [[DHX33]] | 0.792 | DEAH-box helicase 33 |
| [[PNO1]] | 0.788 | partner of NOB1 homolog |
| [[DDX31]] | 0.786 | DEAD-box helicase 31 |
| [[NIP7]] | 0.781 | nucleolar pre-rRNA processing protein NIP7 |
| [[NOM1]] | 0.780 | nucleolar protein with MIF4G domain 1 |
| [[PUM3]] | 0.777 | pumilio RNA binding family member 3 |
| [[TRMT1]] | 0.776 | tRNA methyltransferase 1 |
| [[URB2]] | 0.774 | URB2 ribosome biogenesis homolog |
| [[TRNT1]] | 0.771 | tRNA nucleotidyl transferase 1 |
| [[ABCF2]] | 0.770 | ATP binding cassette subfamily F member 2 |
| [[ATR]] | 0.766 | ATR checkpoint kinase |
| [[MRM1]] | 0.763 | mitochondrial rRNA methyltransferase 1 |
| [[UTP4]] | 0.763 | UTP4 small subunit processome component |
| [[SLFNL1-AS1]] | 0.761 | SLFNL1 antisense RNA 1 |
| [[DDX21]] | 0.760 | DExD-box helicase 21 |
| [[CTPS1]] | 0.758 | CTP synthase 1 |
| [[TIMM23B-AGAP6]] | 0.756 | TIMM23B-AGAP6 readthrough (NMD candidate) |
| [[ZNF202]] | 0.749 | zinc finger protein 202 |
| [[TBRG4]] | 0.747 | FASTK mitochondrial RNA regulator 4 |
| [[PINX1]] | 0.738 | PIN2 (TERF1) interacting telomerase inhibitor 1 |
| [[PPRC1]] | 0.737 | PPARG related coactivator 1 |
| [[PIGW]] | 0.736 | phosphatidylinositol glycan anchor biosynthesis class W |
| [[SDAD1]] | 0.734 | SDA1 domain containing 1 |
| [[EMG1]] | 0.732 | EMG1 N1-specific pseudouridine methyltransferase |
| [[E2F3]] | 0.728 | E2F transcription factor 3 |
| [[BEND3]] | 0.726 | BEN domain containing 3 |
| [[METTL8]] | 0.723 | methyltransferase 8, tRNA N3-cytidine |
| [[NOL9]] | 0.722 | nucleolar protein 9 |
| [[PDCD11]] | 0.716 | programmed cell death 11 |
| [[KLHDC4]] | 0.710 | kelch domain containing 4 |
| [[LYAR]] | 0.704 | Ly1 antibody reactive |
| [[MAPKAPK5]] | 0.703 | MAPK activated protein kinase 5 |
| [[PPAN]] | 0.699 | peter pan homolog |
| [[HNRNPAB]] | 0.690 | heterogeneous nuclear ribonucleoprotein A/B |
| [[MBD3]] | 0.687 | methyl-CpG binding domain protein 3 |
| [[NDUFAF2]] | 0.684 | NADH:ubiquinone oxidoreductase complex assembly factor 2 |
| [[LYRM4]] | 0.683 | LYR motif containing 4 |
| [[C1orf109]] | 0.682 | AFG2 interacting ribosome maturation factor |
| [[TRMT6]] | 0.682 | tRNA methyltransferase 6 non-catalytic subunit |
| [[RBM19]] | 0.681 | RNA binding motif protein 19 |
| [[NOLC1]] | 0.679 | nucleolar and coiled-body phosphoprotein 1 |
| [[PRDM15]] | 0.678 | PR/SET domain 15 |
| [[SPOPL-DT]] | 0.675 | SPOPL divergent transcript |
| [[SP2-AS1]] | 0.670 | SP2 antisense RNA 1 |
| [[NADK]] | 0.670 | NAD kinase |
| [[P2RY11]] | 0.669 | purinergic receptor P2Y11 |
| [[DHX34]] | 0.669 | DExH-box helicase 34 |
| [[NOP56]] | 0.666 | NOP56 ribonucleoprotein |
| [[PTPRG]] | 0.664 | protein tyrosine phosphatase receptor type G |
| [[DCTD]] | 0.663 | dCMP deaminase |
| [[RPTOR]] | 0.662 | regulatory associated protein of MTOR complex 1 |
| [[AGAP6]] | 0.660 | ArfGAP with GTPase domain, ankyrin repeat and PH domain 6 |
| [[GEMIN4]] | 0.659 | gem nuclear organelle associated protein 4 |
| [[TRIM65]] | 0.655 | tripartite motif containing 65 |
| [[ZNF142]] | 0.654 | zinc finger protein 142 |
| [[TASOR2]] | 0.654 | transcription activation suppressor family member 2 |
| [[PA2G4]] | 0.649 | proliferation-associated 2G4 |
| [[CHCHD4]] | 0.647 | coiled-coil-helix-coiled-coil-helix domain containing 4 |
| [[DUS2]] | 0.644 | dihydrouridine synthase 2 |
| [[CCNJ]] | 0.644 | cyclin J |
| [[ENOX2]] | 0.642 | ecto-NOX disulfide-thiol exchanger 2 |
| [[ZNF276]] | 0.640 | zinc finger protein 276 |
| [[MCM3AP]] | 0.639 | minichromosome maintenance complex component 3 associated protein |
| [[ASMTL-AS1]] | 0.638 | ASMTL antisense RNA 1 |
| [[DIMT1]] | 0.638 | DIM1 rRNA methyltransferase and ribosome maturation factor |
| [[ZNF124]] | 0.635 | zinc finger protein 124 |
| [[P2RX5]] | 0.635 | purinergic receptor P2X 5 |
| [[XXYLT1]] | 0.634 | xyloside xylosyltransferase 1 |
| [[TLCD3A]] | 0.633 | TLC domain containing 3A |
| [[MTHFD1L]] | 0.632 | methylenetetrahydrofolate dehydrogenase (NADP+ dependent) 1 like |
| [[RNASEH1]] | 0.632 | ribonuclease H1 |
| [[DDX51]] | 0.626 | DEAD-box helicase 51 |
| [[GBX2-AS1]] | 0.622 | GBX2 and ASB18 antisense RNA 1 |
| [[METTL2B]] | 0.620 | methyltransferase 2B, tRNA N3-cytidine |
| [[LRRK1]] | 0.620 | leucine rich repeat kinase 1 |
| [[UBIAD1]] | 0.620 | UbiA prenyltransferase domain containing 1 |
| [[KCNJ14]] | 0.619 | potassium inwardly rectifying channel subfamily J member 14 |
| [[BRD9]] | 0.615 | bromodomain containing 9 |
| [[PRRC2B]] | 0.615 | proline rich coiled-coil 2B |
| [[DDX56]] | 0.615 | DEAD-box helicase 56 |
| [[RRP1]] | 0.613 | ribosomal RNA processing 1 |
| [[DOCK1]] | 0.609 | dedicator of cytokinesis 1 |
| [[TRMT12]] | 0.606 | tRNA wybutosine-synthesizing protein 2 |
| [[C1orf159]] | 0.606 | chromosome 1 open reading frame 159 |
| [[WDR27]] | 0.604 | WD repeat domain 27 |
| [[PEX26]] | 0.603 | peroxisomal biogenesis factor 26 |
| [[SCLY]] | 0.602 | selenocysteine lyase |
| [[TEAD4]] | 0.601 | TEA domain transcription factor 4 |
| [[POLR1G]] | 0.599 | RNA polymerase I subunit G |
| [[ADAT1]] | 0.595 | adenosine deaminase tRNA specific 1 |
| [[EIF3J]] | 0.595 | eukaryotic translation initiation factor 3 subunit J |
| [[MORC2]] | 0.594 | MORC family CW-type zinc finger 2 |
| [[FAR2]] | 0.590 | fatty acyl-CoA reductase 2 |
| [[NAT10]] | 0.588 | N-acetyltransferase 10 |
| [[L3HYPDH]] | 0.585 | trans-L-3-hydroxyproline dehydratase |
| [[KMT2D]] | 0.582 | lysine methyltransferase 2D |
| [[ENTR1]] | 0.580 | endosome associated trafficking regulator 1 |
| [[THAP4]] | 0.575 | THAP domain containing 4 |
| [[RRP7A]] | 0.573 | ribosomal RNA processing 7 homolog A |
| [[MECR]] | 0.572 | mitochondrial trans-2-enoyl-CoA reductase |
| [[NCL]] | 0.571 | nucleolin multifunctional protein |
| [[PRR7-AS1]] | 0.570 | PRR7 antisense RNA 1 |
| [[POLR1C]] | 0.567 | RNA polymerase I and III subunit C |
| [[EXOSC7]] | 0.566 | exosome component 7 |
| [[PALD1]] | 0.565 | phosphatase domain containing paladin 1 |
| [[NACC1]] | 0.564 | nucleus accumbens associated 1 |
| [[SENP3]] | 0.563 | SUMO specific peptidase 3 |
| [[FAM86DP-1]] | 0.562 | — |
| [[RRP7BP-1]] | 0.562 | — |
| [[SETD6]] | 0.560 | SET domain containing 6, protein lysine methyltransferase |
| [[SLC9B2]] | 0.558 | solute carrier family 9 member B2 |
| [[LRP8]] | 0.556 | LDL receptor related protein 8 |
| [[SLC25A19]] | 0.556 | solute carrier family 25 member 19 |
| [[PINX1-1]] | 0.555 | — |
| [[ALDH1B1]] | 0.555 | aldehyde dehydrogenase 1 family member B1 |
| [[NAF1]] | 0.554 | nuclear assembly factor 1 ribonucleoprotein |
| [[LINC02728]] | 0.553 | long independently transcribed non-coding RNA 2728 |
| [[ZNF562]] | 0.553 | zinc finger protein 562 |
| [[ANKRD40]] | 0.552 | ankyrin repeat domain 40 |
| [[MFSD14CP-1]] | 0.551 | — |
| [[MAD1L1]] | 0.547 | mitotic arrest deficient 1 like 1 |
| [[MAPKAP1]] | 0.546 | MAPK associated protein 1 |
| [[TMEM138]] | 0.541 | transmembrane protein 138 |
| [[TOR1A]] | 0.541 | torsin family 1 member A |
| [[HDAC4]] | 0.535 | histone deacetylase 4 |
| [[TRABD2B]] | 0.533 | TraB domain containing 2B |
| [[PWP2]] | 0.528 | PWP2 small subunit processome component |
| [[ZNG1C]] | 0.526 | Zn regulated GTPase metalloprotein activator 1C |
| [[PKP4]] | 0.524 | plakophilin 4 |
| [[SPOUT1]] | 0.523 | SPOUT domain containing methyltransferase 1 |
| [[ZNRF3]] | 0.522 | zinc and ring finger 3 |
| [[ACTR3B]] | 0.521 | actin related protein 3B |
| [[LRRC69]] | 0.520 | leucine rich repeat containing 69 |
| [[ZNF787]] | 0.518 | zinc finger protein 787 |
| [[CPSF3]] | 0.518 | cleavage and polyadenylation specific factor 3 |
| [[SHLD2]] | 0.517 | shieldin complex subunit 2 |
| [[NR2C2AP]] | 0.512 | nuclear receptor 2C2 associated protein |
| [[PRR5L]] | 0.510 | proline rich 5 like |
| [[GPR135]] | 0.510 | G protein-coupled receptor 135 |
| [[MIR17HG]] | 0.509 | miR-17-92a-1 cluster host gene |
| [[CUL4A]] | 0.503 | cullin 4A |
| [[ECHDC1]] | 0.502 | ethylmalonyl-CoA decarboxylase 1 |
| [[TOR3A]] | 0.500 | torsin family 3 member A |
| [[ZNG1E]] | 0.495 | Zn regulated GTPase metalloprotein activator 1E |
| [[ZNG1F]] | 0.491 | Zn regulated GTPase metalloprotein activator 1F |
| [[NPIPB11]] | 0.491 | nuclear pore complex interacting protein family member B11 |
| [[PRPF40B]] | 0.481 | pre-mRNA processing factor 40B |
| [[KTN1-AS1]] | 0.474 | KTN1 antisense RNA 1 |
| [[SIPA1L1]] | 0.472 | signal induced proliferation associated 1 like 1 |
| [[SMG1P6]] | 0.472 | SMG1 pseudogene 6 |
| [[NDST1]] | 0.472 | N-deacetylase and N-sulfotransferase 1 |
| [[EHBP1]] | 0.466 | EH domain binding protein 1 |
| [[COMT]] | 0.460 | catechol-O-methyltransferase |
| [[TPK1]] | 0.460 | thiamin pyrophosphokinase 1 |
| [[TXLNGY]] | 0.459 | taxilin gamma Y-linked (pseudogene) |
| [[CDK5R1]] | 0.456 | cyclin dependent kinase 5 regulatory subunit 1 |
| [[RIN3]] | 0.456 | Ras and Rab interactor 3 |
| [[LMF1]] | 0.451 | lipase maturation factor 1 |
| [[AMER1]] | 0.449 | APC membrane recruitment protein 1 |
| [[VAC14]] | 0.449 | VAC14 component of PIKFYVE complex |
| [[PARG]] | 0.445 | poly(ADP-ribose) glycohydrolase |
| [[LINC00106]] | 0.441 | long independently transcribed non-coding RNA 106 |
| [[SYMPK]] | 0.437 | symplekin scaffold protein |
| [[POLR1E]] | 0.437 | RNA polymerase I subunit E |
| [[TRAPPC12]] | 0.437 | trafficking protein particle complex subunit 12 |
| [[NUTM2A-AS1]] | 0.435 | NUTM2A antisense RNA 1 |
| [[NUTM2B-AS1]] | 0.435 | NUTM2B antisense RNA 1 |
| [[ADORA2B]] | 0.432 | adenosine A2b receptor |
| [[BCL2]] | 0.431 | BCL2 apoptosis regulator |
| [[ZNF696]] | 0.427 | zinc finger protein 696 |
| [[TIMM21]] | 0.425 | translocase of inner mitochondrial membrane 21 |
| [[KAT8]] | 0.421 | lysine acetyltransferase 8 |
| [[OGFOD1]] | 0.418 | 2-oxoglutarate and iron dependent oxygenase domain containing 1 |
| [[TMX2]] | 0.415 | thioredoxin related transmembrane protein 2 |
| [[MEX3A]] | 0.410 | mex-3 RNA binding family member A |
| [[SNX19]] | 0.407 | sorting nexin 19 |
| [[ZBTB47]] | 0.393 | zinc finger and BTB domain containing 47 |
| [[LIMD1]] | 0.387 | LIM domain containing 1 |
| [[AGAP4]] | 0.381 | ArfGAP with GTPase domain, ankyrin repeat and PH domain 4 |
| [[SIRPA]] | 0.378 | signal regulatory protein alpha |
| [[NPIPB12]] | 0.361 | nuclear pore complex interacting protein family member B12 |
| [[CDC42BPA]] | 0.359 | CDC42 binding protein kinase alpha |
| [[GSAP]] | 0.355 | gamma-secretase activating protein |
| [[SRBD1]] | 0.354 | S1 RNA binding domain 1 |
| [[RAI1]] | 0.344 | retinoic acid induced 1 |
| [[TXLNG]] | 0.315 | taxilin gamma |
| [[BOK]] | 0.306 | BCL2 family apoptosis regulator BOK |
| [[RTKN]] | 0.302 | rhotekin |
| [[PNN]] | 0.294 | pinin, desmosome associated protein |
| [[ATP9B]] | 0.292 | ATPase phospholipid transporting 9B |
| [[INO80E]] | 0.264 | INO80 complex subunit E |
| [[PPCDC]] | 0.146 | phosphopantothenoylcysteine decarboxylase |

## − arm (38)

| Gene | Projection | Name |
|---|---|---|
| [[PJA2]] | -0.695 | praja ring finger ubiquitin ligase 2 |
| [[MPC2]] | -0.657 | mitochondrial pyruvate carrier 2 |
| [[PPDPF]] | -0.630 | pancreatic progenitor cell differentiation and proliferation factor |
| [[SKAP2]] | -0.616 | src kinase associated phosphoprotein 2 |
| [[DDAH2]] | -0.594 | DDAH family member 2, ADMA-independent |
| [[OAZ1]] | -0.594 | ornithine decarboxylase antizyme 1 |
| [[ABI1]] | -0.593 | abl interactor 1 |
| [[MEF2A]] | -0.590 | myocyte enhancer factor 2A |
| [[SECISBP2L]] | -0.580 | SECIS binding protein 2 like |
| [[VWA5A]] | -0.576 | von Willebrand factor A domain containing 5A |
| [[PGM2L1]] | -0.575 | phosphoglucomutase 2 like 1 |
| [[ADD3]] | -0.571 | adducin 3 |
| [[GRHL1]] | -0.555 | grainyhead like transcription factor 1 |
| [[RAB11A]] | -0.552 | RAB11A, member RAS oncogene family |
| [[FAM8A1]] | -0.549 | family with sequence similarity 8 member A1 |
| [[MTMR11]] | -0.549 | myotubularin related protein 11 |
| [[SPAG9]] | -0.548 | sperm associated antigen 9 |
| [[KMT2C]] | -0.546 | lysine methyltransferase 2C |
| [[HADHB]] | -0.542 | hydroxyacyl-CoA dehydrogenase trifunctional multienzyme complex subunit beta |
| [[MOSPD2]] | -0.534 | motile sperm domain containing 2 |
| [[SVIP]] | -0.521 | small VCP interacting protein |
| [[ILK]] | -0.514 | integrin linked kinase |
| [[GSN]] | -0.509 | gelsolin |
| [[CRIP2]] | -0.488 | cysteine rich protein 2 |
| [[KIDINS220]] | -0.484 | kinase D interacting substrate 220 |
| [[NBEAL1]] | -0.469 | neurobeachin like 1 |
| [[SH3GLB1]] | -0.456 | SH3 domain containing GRB2 like, endophilin B1 |
| [[RNF11]] | -0.455 | ring finger protein 11 |
| [[EXOC1]] | -0.441 | exocyst complex component 1 |
| [[HCFC2]] | -0.417 | host cell factor C2 |
| [[CDKL5]] | -0.405 | cyclin dependent kinase like 5 |
| [[IMPA1]] | -0.395 | inositol monophosphatase 1 |
| [[ACADSB]] | -0.381 | acyl-CoA dehydrogenase short/branched chain |
| [[CTBS]] | -0.373 | chitobiase |
| [[KAT2B]] | -0.367 | lysine acetyltransferase 2B |
| [[MYO6]] | -0.302 | myosin VI |
| [[PDCD6IP]] | -0.255 | programmed cell death 6 interacting protein |
| [[RFESD]] | -0.232 | Rieske Fe-S domain containing |

## Data

- `graph/nodes.parquet` — module == 5; `graph/modules.parquet` — module == 5; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [4] (drug-dose × line)
