---
module: 16
type: "module"
n_genes: 206
n_plus: 181
n_minus: 25
arms_opposite: true
mean_cos_between_arms: -0.29030436277389526
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 016

*206 genes (181 in the + arm, 25 in the − arm) · [[Module 016.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29). The + arm rises where the − arm falls. Arm = the side of the module's main direction a gene sits on.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of the + arm minus the − arm (`graph/module_pooled_z.npy`, row 15), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it (+ arm up, − arm down): [[Homoharringtonine (drug)]] 5 µM (+15.7, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (+12.2, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (+11.9, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (+9.1, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.05 µM (+6.1); [[TAK-901 (drug)]] 5 µM (+5.9, ⚠ cell-cycle shift); [[Selinexor (drug)]] 5 µM (+5.2, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 0.05 µM (+3.9); [[Docetaxel (drug)]] 0.05 µM (+3.9, ⚠ transcription drop; cell-cycle shift); [[Topotecan (hydrochloride) (drug)]] 5 µM (+3.8, ⚠ toxic; cell-cycle shift); [[PH-797804 (drug)]] 5 µM (+3.1); [[Filgotinib (drug)]] 5 µM (+2.9); [[Retinoic acid (drug)]] 0.05 µM (+2.8); [[Busulfan (drug)]] 0.05 µM (+2.6); [[Belumosudil (drug)]] 5 µM (+2.6); [[TAK-901 (drug)]] 0.05 µM (+2.3); [[Omeprazole (drug)]] 0.05 µM (+2.1); [[Berbamine (drug)]] 0.05 µM (+2.1) (99 in all, 21 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)
- Lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM (-11.6, ⚠ cell-cycle shift); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (-7.6, ⚠ cell-cycle shift); [[Epirubicin (hydrochloride) (drug)]] 5 µM (-6.8, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (-6.4, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (-6.0, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (-5.0, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 5 µM (-4.3, ⚠ toxic; transcription drop; cell-cycle shift); [[Ixazomib citrate (drug)]] 5 µM (-3.7, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (-3.7, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 0.5 µM (-3.5, ⚠ cell-cycle shift); [[HI-TOPK-032 (drug)]] 5 µM (-2.9); [[Bortezomib (drug)]] 0.5 µM (-2.7); [[Ixazomib citrate (drug)]] 0.5 µM (-2.4); [[Niclosamide (olamine) (drug)]] 0.5 µM (-2.2); [[Brivudine (drug)]] 5 µM (-2.2); [[Tomivosertib (drug)]] 5 µM (-2.1); [[Verteporfin (drug)]] 5 µM (-1.9); [[Vinblastine (sulfate) (drug)]] 5 µM (-1.9); [[PF-06260933 (drug)]] 5 µM (-1.8); [[Abemaciclib (drug)]] 0.5 µM (-1.6) (74 in all, 20 with an alert ⚠; shown: the 10 strongest and the 10 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[A-172 (line)]], [[NCI-H460 (line)]], [[HS-578T (line)]], [[RKO (line)]], [[HEC-1-A (line)]], [[LOX-IMVI (line)]], [[HOP62 (line)]], [[SW480 (line)]]

## + arm (181)

| Gene | Projection | Name |
|---|---|---|
| [[ZNF268]] | 0.878 | zinc finger protein 268 |
| [[CSTF2T]] | 0.872 | cleavage stimulation factor subunit 2 tau variant |
| [[ZNF260]] | 0.865 | zinc finger protein 260 |
| [[RTL6]] | 0.859 | retrotransposon Gag like 6 |
| [[ZNF780A]] | 0.857 | zinc finger protein 780A |
| [[ZNF776]] | 0.849 | zinc finger protein 776 |
| [[ZNF620]] | 0.846 | zinc finger protein 620 |
| [[PABIR1]] | 0.830 | PP2A Aalpha (PPP2R1A) and B55A (PPP2R2A) interacting phosphatase regulator 1 |
| [[ZNF480]] | 0.828 | zinc finger protein 480 |
| [[ZNF155]] | 0.825 | zinc finger protein 155 |
| [[ZNF502]] | 0.812 | zinc finger protein 502 |
| [[SLC35A4]] | 0.808 | solute carrier family 35 member A4 |
| [[ZNF510]] | 0.803 | zinc finger protein 510 |
| [[ZNF317]] | 0.797 | zinc finger protein 317 |
| [[ZKSCAN2]] | 0.789 | zinc finger with KRAB and SCAN domains 2 |
| [[ZSCAN12]] | 0.789 | zinc finger and SCAN domain containing 12 |
| [[ZNF606]] | 0.786 | zinc finger protein 606 |
| [[KLHL9]] | 0.779 | kelch like family member 9 |
| [[ZBED9]] | 0.777 | SCAN domain containing 3 |
| [[C7orf25]] | 0.775 | chromosome 7 open reading frame 25 |
| [[ZNF772]] | 0.772 | zinc finger protein 772 |
| [[LIG4]] | 0.767 | DNA ligase 4 |
| [[ZNF518B]] | 0.766 | zinc finger protein 518B |
| [[VPS72]] | 0.766 | vacuolar protein sorting 72 homolog |
| [[DCLRE1A]] | 0.759 | DNA cross-link repair 1A |
| [[MRPS18A]] | 0.758 | mitochondrial ribosomal protein S18A |
| [[VEZF1]] | 0.758 | vascular endothelial zinc finger 1 |
| [[HNRNPH2]] | 0.750 | heterogeneous nuclear ribonucleoprotein H2 |
| [[CHTOP]] | 0.748 | chromatin target of PRMT1 |
| [[ZMYM4]] | 0.747 | zinc finger MYM-type containing 4 |
| [[UBQLN2]] | 0.743 | ubiquilin 2 |
| [[BBS10]] | 0.737 | Bardet-Biedl syndrome 10 |
| [[DDX20]] | 0.736 | DEAD-box helicase 20 |
| [[ZNF140]] | 0.734 | zinc finger protein 140 |
| [[ZNF252P-1]] | 0.729 | — |
| [[MRPL47]] | 0.729 | mitochondrial ribosomal protein L47 |
| [[GDAP1]] | 0.724 | ganglioside induced differentiation associated protein 1 |
| [[LYRM2]] | 0.723 | LYR motif containing 2 |
| [[ZNF211]] | 0.718 | zinc finger protein 211 |
| [[ZNF594]] | 0.714 | zinc finger protein 594 |
| [[ZSCAN26]] | 0.714 | zinc finger and SCAN domain containing 26 |
| [[TMEM185B]] | 0.713 | transmembrane protein 185B |
| [[ZNF134]] | 0.711 | zinc finger protein 134 |
| [[IRF2BP1]] | 0.707 | interferon regulatory factor 2 binding protein 1 |
| [[ZNF221]] | 0.703 | zinc finger protein 221 |
| [[FNBP1P1]] | 0.701 | formin binding protein 1 pseudogene 1 |
| [[DEDD]] | 0.700 | death effector domain containing |
| [[ASF1A]] | 0.700 | anti-silencing function 1A histone chaperone |
| [[PUF60]] | 0.700 | poly(U) binding splicing factor 60 |
| [[ADO]] | 0.696 | 2-aminoethanethiol dioxygenase |
| [[SAYSD1]] | 0.695 | SAYSVFN motif domain containing 1 |
| [[GOPC]] | 0.693 | golgi associated PDZ and coiled-coil motif containing |
| [[ZNF839]] | 0.691 | zinc finger protein 839 |
| [[KAT5]] | 0.688 | lysine acetyltransferase 5 |
| [[ZFP41]] | 0.687 | ZFP41 zinc finger protein |
| [[REPIN1]] | 0.687 | replication initiator 1 |
| [[TIGD2]] | 0.684 | tigger transposable element derived 2 |
| [[RANBP6]] | 0.681 | RAN binding protein 6 |
| [[ZNF613]] | 0.681 | zinc finger protein 613 |
| [[C22orf46]] | 0.675 | chromosome 22 open reading frame 46, pseudogene |
| [[ZNF554]] | 0.669 | zinc finger protein 554 |
| [[PYM1]] | 0.669 | PYM1 exon junction complex associated factor |
| [[MIS12]] | 0.669 | MIS12 kinetochore complex component |
| [[ZNF512B]] | 0.667 | zinc finger protein 512B |
| [[PRRC2A]] | 0.666 | proline rich coiled-coil 2A |
| [[MSANTD4]] | 0.664 | Myb/SANT DNA binding domain containing 4 with coiled-coils |
| [[CHAMP1]] | 0.656 | chromosome alignment maintaining phosphoprotein 1 |
| [[ZSCAN20]] | 0.650 | zinc finger and SCAN domain containing 20 |
| [[SRRD]] | 0.650 | SRR1 domain containing |
| [[ZNF681]] | 0.649 | zinc finger protein 681 |
| [[ZNF180]] | 0.649 | zinc finger protein 180 |
| [[EIF2B5]] | 0.646 | eukaryotic translation initiation factor 2B subunit epsilon |
| [[ANKEF1]] | 0.646 | ankyrin repeat and EF-hand domain containing 1 |
| [[ZNF528]] | 0.645 | zinc finger protein 528 |
| [[SENP1]] | 0.643 | SUMO specific peptidase 1 |
| [[ZKSCAN3]] | 0.640 | zinc finger with KRAB and SCAN domains 3 |
| [[SRCAP]] | 0.640 | Snf2 related CREBBP activator protein |
| [[CEP41]] | 0.638 | centrosomal protein 41 |
| [[C9orf64]] | 0.637 | Q-nucleotide N-glycosylase 1 |
| [[ZNF548]] | 0.635 | zinc finger protein 548 |
| [[ZNF24]] | 0.635 | zinc finger protein 24 |
| [[ZNF829]] | 0.631 | zinc finger protein 829 |
| [[CCDC102A]] | 0.630 | coiled-coil domain containing 102A |
| [[ANAPC13]] | 0.627 | anaphase promoting complex subunit 13 |
| [[DNAJC14]] | 0.626 | DnaJ heat shock protein family (Hsp40) member C14 |
| [[ZNF678]] | 0.625 | zinc finger protein 678 |
| [[ZFHX2]] | 0.623 | zinc finger homeobox 2 |
| [[ZNF793]] | 0.606 | zinc finger protein 793 |
| [[LGALSL]] | 0.605 | galectin like |
| [[ZBED8]] | 0.604 | zinc finger BED-type containing 8 |
| [[FANCF]] | 0.602 | FA complementation group F |
| [[TRIM68]] | 0.597 | tripartite motif containing 68 |
| [[TTC30A]] | 0.595 | intraflagellar transport 70A |
| [[MANBAL]] | 0.593 | mannosidase beta like |
| [[ZNF607]] | 0.591 | zinc finger protein 607 |
| [[ZNF615]] | 0.590 | zinc finger protein 615 |
| [[B3GALT9]] | 0.588 | beta-1,3-galactosyltransferase 9 |
| [[ZNF22]] | 0.588 | zinc finger protein 22 |
| [[GSS]] | 0.587 | glutathione synthetase |
| [[ZSCAN22]] | 0.585 | zinc finger and SCAN domain containing 22 |
| [[ZFP37]] | 0.582 | ZFP37 zinc finger protein |
| [[ZNF570]] | 0.582 | zinc finger protein 570 |
| [[PURB]] | 0.581 | purine rich element binding protein B |
| [[PLAGL2]] | 0.573 | PLAG1 like zinc finger 2 |
| [[NHLRC2]] | 0.570 | NHL repeat containing 2 |
| [[ZSCAN9]] | 0.568 | zinc finger and SCAN domain containing 9 |
| [[TSPYL5]] | 0.566 | TSPY like 5 |
| [[ZNF136]] | 0.565 | zinc finger protein 136 |
| [[MRPL35]] | 0.558 | mitochondrial ribosomal protein L35 |
| [[THUMPD2]] | 0.558 | THUMP domain 2 tRNA and snRNA guanosine methyltransferase |
| [[PAFAH2]] | 0.554 | platelet activating factor acetylhydrolase 2 |
| [[KLF11]] | 0.554 | KLF transcription factor 11 |
| [[ZNF284]] | 0.552 | zinc finger protein 284 |
| [[XKR6]] | 0.550 | XK related 6 |
| [[ZNF225]] | 0.549 | zinc finger protein 225 |
| [[ZNF81]] | 0.547 | zinc finger protein 81 |
| [[ZNF334]] | 0.544 | zinc finger protein 334 |
| [[ZBTB17]] | 0.542 | zinc finger and BTB domain containing 17 |
| [[ZBTB4]] | 0.541 | zinc finger and BTB domain containing 4 |
| [[NUP62]] | 0.533 | nucleoporin 62 |
| [[NRIP1]] | 0.533 | nuclear receptor interacting protein 1 |
| [[ZNF625]] | 0.531 | zinc finger protein 625 |
| [[C2orf74-DT]] | 0.529 | C2orf74 antisense RNA 1 |
| [[AFF4]] | 0.526 | ALF transcription elongation factor 4 |
| [[ZNF880]] | 0.526 | zinc finger protein 880 |
| [[ZNF484]] | 0.525 | zinc finger protein 484 |
| [[ZNF624]] | 0.523 | zinc finger protein 624 |
| [[TTPAL]] | 0.522 | alpha tocopherol transfer protein like |
| [[DNAH14]] | 0.518 | dynein axonemal heavy chain 14 |
| [[ZFP1]] | 0.516 | ZFP1 zinc finger protein |
| [[C6orf120]] | 0.516 | chromosome 6 open reading frame 120 |
| [[HERPUD2-AS1]] | 0.515 | HERPUD2 antisense RNA 1 |
| [[ZBTB9]] | 0.510 | zinc finger and BTB domain containing 9 |
| [[ATXN7L3B]] | 0.505 | ataxin 7 like 3B |
| [[PPP1R9A]] | 0.504 | protein phosphatase 1 regulatory subunit 9A |
| [[IL4I1]] | 0.503 | interleukin 4 induced 1 |
| [[ZNF780B]] | 0.494 | zinc finger protein 780B |
| [[ZC3H10]] | 0.489 | zinc finger CCCH-type containing 10 |
| [[THNSL1]] | 0.487 | threonine synthase like 1 |
| [[DUSP19]] | 0.487 | dual specificity phosphatase 19 |
| [[DPY19L2P2-1]] | 0.487 | — |
| [[ZNF585B]] | 0.484 | zinc finger protein 585B |
| [[EID1]] | 0.482 | EP300 interacting inhibitor of differentiation 1 |
| [[WDR82]] | 0.482 | WD repeat domain 82 |
| [[CENPS]] | 0.479 | centromere protein S |
| [[STK33]] | 0.477 | serine/threonine kinase 33 |
| [[RNF180]] | 0.476 | ring finger protein 180 |
| [[SLC31A2]] | 0.462 | solute carrier family 31 member 2 |
| [[WDCP]] | 0.461 | WD repeat and coiled coil containing |
| [[ZNF229]] | 0.452 | zinc finger protein 229 |
| [[THRAP3]] | 0.451 | thyroid hormone receptor associated protein 3 |
| [[ZNF354C]] | 0.448 | zinc finger protein 354C |
| [[ZNF287]] | 0.446 | zinc finger protein 287 |
| [[C15orf39]] | 0.445 | PRMT2 interacting protein |
| [[CEP19]] | 0.442 | centrosomal protein 19 |
| [[ZSCAN23]] | 0.441 | zinc finger and SCAN domain containing 23 |
| [[KIAA0408]] | 0.434 | KIAA0408 |
| [[FAHD1]] | 0.430 | FAH domain containing oxaloacetate decarboxylase 1 |
| [[MRPL28]] | 0.425 | mitochondrial ribosomal protein L28 |
| [[RANBP2]] | 0.421 | RAN binding protein 2 |
| [[CPSF7]] | 0.417 | cleavage and polyadenylation specific factor 7 |
| [[ZSCAN18]] | 0.411 | zinc finger and SCAN domain containing 18 |
| [[DST]] | 0.411 | dystonin |
| [[C2orf68]] | 0.400 | chromosome 2 open reading frame 68 |
| [[HHEX]] | 0.396 | hematopoietically expressed homeobox |
| [[RRAGA]] | 0.393 | Ras related GTP binding A |
| [[MAGEA1]] | 0.387 | MAGE family member A1 |
| [[OSGEPL1]] | 0.377 | O-sialoglycoprotein endopeptidase like 1 |
| [[NUDT6]] | 0.365 | nudix hydrolase 6 |
| [[PIGM]] | 0.363 | phosphatidylinositol glycan anchor biosynthesis class M |
| [[CHMP7]] | 0.343 | charged multivesicular body protein 7 |
| [[LHFPL4]] | 0.319 | LHFPL tetraspan subfamily member 4 |
| [[MICU3]] | 0.314 | mitochondrial calcium uptake 3 |
| [[ZNF677]] | 0.311 | zinc finger protein 677 |
| [[ZBTB14]] | 0.309 | zinc finger and BTB domain containing 14 |
| [[GALNT4]] | 0.295 | polypeptide N-acetylgalactosaminyltransferase 4 |
| [[ZNF280B]] | 0.292 | zinc finger protein 280B |
| [[LINC00205]] | 0.238 | long independently transcribed non-coding RNA 205 |
| [[CCNYL2-1]] | 0.228 | — |
| [[JRKL]] | 0.211 | JRK like |
| [[CANT1]] | 0.167 | calcium activated nucleotidase 1 |

## − arm (25)

| Gene | Projection | Name |
|---|---|---|
| [[GNRH1]] | -0.701 | gonadotropin releasing hormone 1 |
| [[MFN1]] | -0.671 | mitofusin 1 |
| [[PIGN]] | -0.664 | phosphatidylinositol glycan anchor biosynthesis class N |
| [[SMG1P5]] | -0.649 | SMG1 pseudogene 5 |
| [[SRD5A1]] | -0.624 | steroid 5 alpha-reductase 1 |
| [[SETD3]] | -0.611 | SET domain containing 3, actin N3(tau)-histidine methyltransferase |
| [[DCUN1D2]] | -0.599 | defective in cullin neddylation 1 domain containing 2 |
| [[TAF5]] | -0.583 | TATA-box binding protein associated factor 5 |
| [[PDXK]] | -0.569 | pyridoxal kinase |
| [[MTFR1]] | -0.567 | mitochondrial fission regulator 1 |
| [[SRGAP2D]] | -0.557 | SLIT-ROBO Rho GTPase activating protein 2D (pseudogene) |
| [[SCARB1]] | -0.547 | scavenger receptor class B member 1 |
| [[SFI1]] | -0.541 | SFI1 centrin binding protein |
| [[MALT1]] | -0.523 | MALT1 paracaspase |
| [[BUD23]] | -0.486 | BUD23 rRNA methyltransferase and ribosome maturation factor |
| [[CD99]] | -0.458 | CD99 molecule (Xg blood group) |
| [[DGKE]] | -0.431 | diacylglycerol kinase epsilon |
| [[METTL21A]] | -0.422 | methyltransferase 21A, HSPA lysine |
| [[HPRT1]] | -0.407 | hypoxanthine phosphoribosyltransferase 1 |
| [[HS2ST1]] | -0.405 | heparan sulfate 2-O-sulfotransferase 1 |
| [[TALAM1]] | -0.378 | TALAM1 transcript, MALAT1 antisense RNA |
| [[NEAT1]] | -0.341 | nuclear paraspeckle assembly transcript 1 |
| [[STAG3L4-1]] | -0.324 | — |
| [[MALAT1]] | -0.257 | metastasis associated lung adenocarcinoma transcript 1 |
| [[ARL15]] | -0.248 | ARF like GTPase 15 |

## Data

- `graph/nodes.parquet` — module == 16; `graph/modules.parquet` — module == 16; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [15] (drug-dose × line)
