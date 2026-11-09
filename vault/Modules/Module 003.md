---
module: 3
type: "module"
n_genes: 246
n_plus: 172
n_minus: 74
arms_opposite: true
mean_cos_between_arms: -0.32266852259635925
label: "mRNA 3'-end processing"
label_source: "reactome"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 003

*mRNA 3'-end processing · 246 genes (172 in the + arm, 74 in the − arm) · [[Module 003.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32). The + arm rises where the − arm falls. Arm = the side of the module's main direction a gene sits on.

Label from the validation stage: **mRNA 3'-end processing** (reactome, q 1e-08; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| - | mRNA 3'-end processing | reactome | 12/74 | 16.2 | 1e-08 |
| - | mRNA Polyadenylation | reactome | 11/74 | 17.6 | 3e-08 |
| - | mRNA Splicing - Major Pathway | reactome | 12/74 | 12.0 | 3e-07 |
| - | mRNA Splicing | reactome | 12/74 | 11.5 | 4e-07 |
| - | Dengue Virus-Host Interactions | reactome | 12/74 | 11.2 | 6e-07 |
| - | Processing of Capped Intron-Containing Pre-mRNA | reactome | 13/74 | 9.10 | 1e-06 |
| - | Dengue Virus Infection | reactome | 13/74 | 8.20 | 4e-06 |
| - | G2/M checkpoint | hallmark | 10/74 | 10.3 | 3e-05 |

## Drugs that move it

*Mean pooled z of the + arm minus the − arm (`graph/module_pooled_z.npy`, row 2), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it (+ arm up, − arm down): [[Panobinostat (drug)]] 0.5 µM (+10.8, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (+10.4, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (+10.2, ⚠ cell-cycle shift); [[Belinostat (drug)]] 0.5 µM (+5.1, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (+5.0, ⚠ cell-cycle shift); [[Ipatasertib (drug)]] 0.5 µM (+3.8); [[Brivudine (drug)]] 5 µM (+2.7); [[Docetaxel (Trihydrate) (drug)]] 0.5 µM (+2.4); [[Sunitinib (drug)]] 5 µM (+2.4, ⚠ toxic); [[Bortezomib (drug)]] 0.05 µM (+2.3, ⚠ cell-cycle shift); [[Methylprednisolone succinate (drug)]] 0.5 µM (+2.3); [[Celecoxib (drug)]] 0.5 µM (+2.2); [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM (+2.2); [[Thymol (drug)]] 0.5 µM (+2.1); [[BAY1125976 (drug)]] 0.5 µM (+2.1); [[Sapanisertib (drug)]] 0.5 µM (+2.0); [[Tofacitinib (citrate) (drug)]] 5 µM (+1.9) (101 in all, 16 with an alert ⚠; shown: the 10 strongest and the 7 next strongest without an alert)
- Lower it: [[Homoharringtonine (drug)]] 5 µM (-15.4, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (-13.9, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (-13.5, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (-11.8, ⚠ toxic; transcription drop; cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-9.7, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-8.6, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (-6.0, ⚠ cell-cycle shift); [[TAK-901 (drug)]] 5 µM (-5.9, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (-5.1, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 0.5 µM (-4.7, ⚠ cell-cycle shift); [[PH-797804 (drug)]] 5 µM (-4.3); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (-3.8); [[Homoharringtonine (drug)]] 0.05 µM (-2.7); [[Belumosudil (drug)]] 5 µM (-2.6); [[TAK-901 (drug)]] 0.05 µM (-2.6); [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM (-2.4); [[Filgotinib (drug)]] 5 µM (-2.3); [[Clobetasol propionate (drug)]] 5 µM (-2.1); [[Benproperine (phosphate) (drug)]] 0.05 µM (-2.1); [[Erlotinib (drug)]] 0.05 µM (-2.1) (118 in all, 28 with an alert ⚠; shown: the 10 strongest and the 10 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[PANC-1 (line)]], [[SW480 (line)]], [[HOP62 (line)]], [[A-172 (line)]], [[A549 (line)]], [[A498 (line)]], [[NCI-H460 (line)]], [[LoVo (line)]]

## Candidate new members

*Members not annotated to the set their arm is enriched for, ranked by mean cos to the annotated members (`validation/novel_members.csv`); ⚠ = a reason to doubt the gene's place (in the vector space only through flagged drug-doses), kept in its rank. 22 candidates, none with an alert; shown: the 15 strongest.*

| # | Gene | Set | Mean cos |
|---|---|---|---|
| 1 | [[YWHAE]] | Dengue Virus-Host Interactions | +0.67 |
| 2 | [[HNRNPM]] | MYC targets v1 | +0.65 |
| 3 | [[EWSR1]] | mRNA Splicing - Major Pathway | +0.63 |
| 4 | [[SFPQ]] | mRNA Splicing - Major Pathway | +0.62 |
| 5 | [[BCLAF1]] | mRNA Polyadenylation | +0.61 |
| 6 | [[HNRNPK]] | MYC targets v1 | +0.60 |
| 7 | [[DDX3X]] | mRNA Polyadenylation | +0.60 |
| 8 | [[HNRNPL]] | MYC targets v1 | +0.59 |
| 9 | [[HNRNPA2B1]] | G2/M checkpoint | +0.59 |
| 10 | [[ILF3]] | Dengue Virus-Host Interactions | +0.59 |
| 11 | [[CBX5]] | Dengue Virus-Host Interactions | +0.58 |
| 12 | [[HNRNPH3]] | mRNA Polyadenylation | +0.58 |
| 13 | [[EIF4G2]] | Dengue Virus-Host Interactions | +0.54 |
| 14 | [[TUG1]] | Dengue Virus-Host Interactions | +0.54 |
| 15 | [[SRSF3]] | G2/M checkpoint | +0.54 |

## + arm (172)

| Gene | Projection | Name |
|---|---|---|
| [[MPG]] | 0.868 | N-methylpurine DNA glycosylase |
| [[COMMD6]] | 0.839 | COMM domain containing 6 |
| [[LIN7B]] | 0.819 | lin-7 cell polarity scaffold B |
| [[LCMT1]] | 0.818 | leucine carboxyl methyltransferase 1 |
| [[CIAO2B]] | 0.816 | cytosolic iron-sulfur assembly component 2B |
| [[RAB40C]] | 0.815 | RAB40C, member RAS oncogene family |
| [[MRPL55]] | 0.809 | mitochondrial ribosomal protein L55 |
| [[SDHAP2]] | 0.802 | SDHA pseudogene 2 |
| [[CARD19]] | 0.799 | caspase recruitment domain family member 19 |
| [[ATG4B]] | 0.798 | autophagy related 4B cysteine peptidase |
| [[ARID3A]] | 0.795 | AT-rich interaction domain 3A |
| [[CBFA2T2]] | 0.780 | CBFA2/RUNX1 partner transcriptional co-repressor 2 |
| [[CDC34]] | 0.779 | cell division cycle 34, ubiquitin conjugating enzyme |
| [[KLHL7]] | 0.778 | kelch like family member 7 |
| [[TRIM62]] | 0.773 | tripartite motif containing 62 |
| [[MPST]] | 0.770 | mercaptopyruvate sulfurtransferase |
| [[A1BG]] | 0.766 | alpha-1-B glycoprotein |
| [[RALGDS]] | 0.766 | ral guanine nucleotide dissociation stimulator |
| [[BAHD1]] | 0.765 | bromo adjacent homology domain containing 1 |
| [[GUK1]] | 0.762 | guanylate kinase 1 |
| [[PMM1]] | 0.758 | phosphomannomutase 1 |
| [[ALKBH7]] | 0.756 | alkB homolog 7, RNA demethylase |
| [[SH3GL1]] | 0.755 | SH3 domain containing GRB2 like 1, endophilin A2 |
| [[B3GAT3]] | 0.746 | beta-1,3-glucuronyltransferase 3 |
| [[STK32C]] | 0.745 | serine/threonine kinase 32C |
| [[NUDT22]] | 0.740 | nudix hydrolase 22 |
| [[TRPT1]] | 0.738 | tRNA phosphotransferase 1 |
| [[MACO1]] | 0.729 | macoilin 1 |
| [[CDKN2D]] | 0.723 | cyclin dependent kinase inhibitor 2D |
| [[MKNK2]] | 0.720 | MAPK interacting serine/threonine kinase 2 |
| [[RNF181]] | 0.718 | ring finger protein 181 |
| [[RASSF7]] | 0.713 | Ras association domain family member 7 |
| [[MARK4]] | 0.707 | microtubule affinity regulating kinase 4 |
| [[AFMID]] | 0.705 | arylformamidase |
| [[HEATR5B]] | 0.703 | HEAT repeat containing 5B |
| [[SIVA1]] | 0.702 | SIVA1 apoptosis inducing factor |
| [[MIGA2]] | 0.697 | mitoguardin 2 |
| [[IL17RA]] | 0.695 | interleukin 17 receptor A |
| [[MAP3K9]] | 0.695 | mitogen-activated protein kinase kinase kinase 9 |
| [[RALA]] | 0.693 | RAS like proto-oncogene A |
| [[SNAPC2]] | 0.691 | small nuclear RNA activating complex polypeptide 2 |
| [[FAM193B]] | 0.690 | family with sequence similarity 193 member B |
| [[GPR157]] | 0.685 | G protein-coupled receptor 157 |
| [[XYLT2]] | 0.684 | xylosyltransferase 2 |
| [[DUSP18]] | 0.684 | dual specificity phosphatase 18 |
| [[PGPEP1]] | 0.677 | pyroglutamyl-peptidase I |
| [[ZNRD2]] | 0.676 | zinc ribbon domain containing 2 |
| [[BLVRB]] | 0.672 | biliverdin reductase B |
| [[SLC25A29]] | 0.672 | solute carrier family 25 member 29 |
| [[COX14]] | 0.670 | cytochrome c oxidase assembly factor COX14 |
| [[VRK3]] | 0.669 | VRK serine/threonine kinase 3 |
| [[CCNQ]] | 0.666 | cyclin Q |
| [[TUSC2]] | 0.665 | tumor suppressor 2, mitochondrial calcium regulator |
| [[SMYD4]] | 0.664 | SET and MYND domain containing 4 |
| [[UBTD1]] | 0.663 | ubiquitin domain containing 1 |
| [[RNF114]] | 0.663 | ring finger protein 114 |
| [[RANBP10]] | 0.661 | RAN binding protein 10 |
| [[METTL26]] | 0.660 | methyltransferase like 26 |
| [[SIRT7]] | 0.659 | sirtuin 7 |
| [[WIPF2]] | 0.658 | WAS/WASL interacting protein family member 2 |
| [[SEZ6L2]] | 0.658 | seizure related 6 homolog like 2 |
| [[TRAPPC4]] | 0.656 | trafficking protein particle complex subunit 4 |
| [[TRIM11]] | 0.654 | tripartite motif containing 11 |
| [[ZNF823]] | 0.651 | zinc finger protein 823 |
| [[MEX3D]] | 0.646 | mex-3 RNA binding family member D |
| [[RABGEF1P1]] | 0.643 | RABGEF1 pseudogene 1 |
| [[ZXDC]] | 0.640 | ZXD family zinc finger C |
| [[EML2]] | 0.639 | EMAP like 2 |
| [[ARL8A]] | 0.633 | ARF like GTPase 8A |
| [[GNB2]] | 0.631 | G protein subunit beta 2 |
| [[PKD1]] | 0.629 | polycystin 1, transient receptor potential channel interacting |
| [[CSNK1G2]] | 0.626 | casein kinase 1 gamma 2 |
| [[MPND]] | 0.622 | MPN domain containing |
| [[PKD1P6]] | 0.622 | polycystin 1, transient receptor potential channel interacting pseudogene 6 |
| [[GLTP]] | 0.621 | glycolipid transfer protein |
| [[CNNM4]] | 0.621 | cyclin and CBS domain divalent metal cation transport mediator 4 |
| [[ANKRD13D]] | 0.621 | ankyrin repeat domain 13D |
| [[C1orf174]] | 0.617 | chromosome 1 open reading frame 174 |
| [[CAMKK1]] | 0.615 | calcium/calmodulin dependent protein kinase kinase 1 |
| [[CCDC167]] | 0.615 | coiled-coil domain containing 167 |
| [[UBE2R2]] | 0.613 | ubiquitin conjugating enzyme E2 R2 |
| [[DENND6B]] | 0.609 | DENN domain containing 6B |
| [[UBE2D2]] | 0.609 | ubiquitin conjugating enzyme E2 D2 |
| [[DEXI]] | 0.609 | Dexi homolog |
| [[GLRX5]] | 0.608 | glutaredoxin 5 |
| [[CDAN1]] | 0.607 | codanin 1 |
| [[DOCK6]] | 0.605 | dedicator of cytokinesis 6 |
| [[A1BG-AS1]] | 0.600 | A1BG antisense RNA 1 |
| [[PTOV1]] | 0.597 | PTOV1 extended AT-hook containing adaptor protein |
| [[CCDC85B]] | 0.594 | coiled-coil domain containing 85B |
| [[VPS37C]] | 0.594 | VPS37C subunit of ESCRT-I |
| [[SELENOO]] | 0.591 | selenoprotein O |
| [[PIN1]] | 0.588 | peptidylprolyl cis/trans isomerase, NIMA-interacting 1 |
| [[CNIH4]] | 0.583 | cornichon family member 4 |
| [[POLB]] | 0.576 | DNA polymerase beta |
| [[PTDSS2]] | 0.576 | phosphatidylserine synthase 2 |
| [[NUBP2]] | 0.575 | NUBP iron-sulfur cluster assembly factor 2, cytosolic |
| [[TRADD]] | 0.570 | TNFRSF1A associated via death domain |
| [[PIP5K1C]] | 0.569 | phosphatidylinositol-4-phosphate 5-kinase type 1 gamma |
| [[CSTB]] | 0.564 | cystatin B |
| [[TRAPPC1]] | 0.564 | trafficking protein particle complex subunit 1 |
| [[FZR1]] | 0.561 | fizzy and cell division cycle 20 related 1 |
| [[FAAP20]] | 0.560 | FA core complex associated protein 20 |
| [[PHLDB3]] | 0.559 | pleckstrin homology like domain family B member 3 |
| [[TMEM38A]] | 0.558 | transmembrane protein 38A |
| [[EXOSC1]] | 0.557 | exosome component 1 |
| [[KLHL26]] | 0.554 | kelch like family member 26 |
| [[CLASRP]] | 0.553 | CLK4 associating serine/arginine rich protein |
| [[POLD4]] | 0.550 | DNA polymerase delta 4, accessory subunit |
| [[WDR44]] | 0.534 | WD repeat domain 44 |
| [[LLGL2]] | 0.522 | LLGL scribble cell polarity complex component 2 |
| [[GID4]] | 0.522 | GID complex subunit 4 homolog |
| [[MORC3]] | 0.520 | MORC family CW-type zinc finger 3 |
| [[PPP1R21]] | 0.519 | protein phosphatase 1 regulatory subunit 21 |
| [[CHRNB1]] | 0.519 | cholinergic receptor nicotinic beta 1 subunit |
| [[ACTR6]] | 0.516 | actin related protein 6 |
| [[FXR2]] | 0.516 | FMR1 autosomal homolog 2 |
| [[SCYL1]] | 0.512 | SCY1 like pseudokinase 1 |
| [[MEA1]] | 0.512 | male-enhanced antigen 1 |
| [[TSEN34]] | 0.509 | tRNA splicing endonuclease subunit 34 |
| [[POLR2F]] | 0.508 | RNA polymerase II, I and III subunit F |
| [[PDP2]] | 0.508 | pyruvate dehydrogenase phosphatase catalytic subunit 2 |
| [[RABIF]] | 0.507 | RAB interacting factor |
| [[MAPK8IP3]] | 0.505 | mitogen-activated protein kinase 8 interacting protein 3 |
| [[NELFB]] | 0.504 | negative elongation factor complex member B |
| [[CASTOR3P]] | 0.503 | CASTOR family member 3, pseudogene |
| [[PLEKHF1]] | 0.498 | pleckstrin homology and FYVE domain containing 1 |
| [[MCRIP1]] | 0.498 | MAPK regulated corepressor interacting protein 1 |
| [[HEBP2]] | 0.494 | heme binding protein 2 |
| [[MRPL17]] | 0.492 | mitochondrial ribosomal protein L17 |
| [[FOXK2]] | 0.487 | forkhead box K2 |
| [[HAUS3]] | 0.487 | HAUS augmin like complex subunit 3 |
| [[CAMSAP3]] | 0.486 | calmodulin regulated spectrin associated protein family member 3 |
| [[ULBP2]] | 0.485 | UL16 binding protein 2 |
| [[RTL10]] | 0.480 | retrotransposon Gag like 10 |
| [[TENT4B]] | 0.477 | terminal nucleotidyltransferase 4B |
| [[PRADC1]] | 0.475 | protease associated domain containing 1 |
| [[PPP1R13B]] | 0.468 | protein phosphatase 1 regulatory subunit 13B |
| [[DSTYK]] | 0.464 | dual serine/threonine and tyrosine protein kinase |
| [[TMEM120A]] | 0.461 | transmembrane protein 120A |
| [[RGL3]] | 0.452 | ral guanine nucleotide dissociation stimulator like 3 |
| [[AGAP3]] | 0.450 | ArfGAP with GTPase domain, ankyrin repeat and PH domain 3 |
| [[DHPS]] | 0.440 | deoxyhypusine synthase |
| [[TXNDC17]] | 0.438 | thioredoxin domain containing 17 |
| [[CCDC82]] | 0.438 | coiled-coil domain containing 82 |
| [[PPP1R16A]] | 0.435 | protein phosphatase 1 regulatory subunit 16A |
| [[C8orf82]] | 0.432 | chromosome 8 open reading frame 82 |
| [[KATNBL1]] | 0.424 | katanin regulatory subunit B1 like 1 |
| [[CRTC1]] | 0.422 | CREB regulated transcription coactivator 1 |
| [[DHRS7]] | 0.421 | dehydrogenase/reductase 7 |
| [[ZC2HC1A]] | 0.419 | zinc finger C2HC-type containing 1A |
| [[SLC52A2]] | 0.412 | solute carrier family 52 member 2 |
| [[RP9P]] | 0.409 | RP9 pseudogene |
| [[GPN3]] | 0.407 | GPN-loop GTPase 3 |
| [[RASSF1]] | 0.402 | Ras association domain family member 1 |
| [[SMG6]] | 0.393 | SMG6 nonsense mediated mRNA decay factor |
| [[JPT1]] | 0.390 | Jupiter microtubule associated homolog 1 |
| [[TSPO]] | 0.385 | translocator protein |
| [[CLPTM1]] | 0.379 | CLPTM1 regulator of GABA type A receptor forward trafficking |
| [[R3HCC1L]] | 0.371 | R3H domain and coiled-coil containing 1 like |
| [[CETN2]] | 0.371 | centrin 2 |
| [[SAMD8]] | 0.363 | sterile alpha motif domain containing 8 |
| [[CLEC11A]] | 0.352 | C-type lectin domain containing 11A |
| [[YTHDF1]] | 0.347 | YTH N6-methyladenosine RNA binding protein F1 |
| [[SETD5]] | 0.330 | SET domain containing 5 |
| [[PPP3R1]] | 0.324 | protein phosphatase 3 regulatory subunit B, alpha |
| [[CCDC93]] | 0.300 | CCC complex scaffolding subunit CCDC93 |
| [[TAF4]] | 0.298 | TATA-box binding protein associated factor 4 |
| [[RXRA]] | 0.292 | retinoid X receptor alpha |
| [[SOX12]] | 0.289 | SRY-box transcription factor 12 |
| [[PDZD11]] | 0.283 | PDZ domain containing 11 |
| [[CUL3]] | 0.0662 | cullin 3 |

## − arm (74)

| Gene | Projection | Name |
|---|---|---|
| [[HNRNPK]] | -0.825 | heterogeneous nuclear ribonucleoprotein K |
| [[YWHAE]] | -0.799 | tyrosine 3-monooxygenase/tryptophan 5-monooxygenase activation protein epsilon |
| [[EWSR1]] | -0.794 | EWS RNA binding protein 1 |
| [[EIF4G2]] | -0.790 | eukaryotic translation initiation factor 4 gamma 2 |
| [[SRSF1]] | -0.764 | serine and arginine rich splicing factor 1 |
| [[DDX3X]] | -0.755 | DEAD-box helicase 3 X-linked |
| [[HNRNPU]] | -0.749 | heterogeneous nuclear ribonucleoprotein U |
| [[HNRNPL]] | -0.745 | heterogeneous nuclear ribonucleoprotein L |
| [[TUG1]] | -0.737 | taurine up-regulated 1 |
| [[HNRNPA2B1]] | -0.737 | heterogeneous nuclear ribonucleoprotein A2/B1 |
| [[BCLAF1]] | -0.728 | BCL2 associated transcription factor 1 |
| [[SLC39A10]] | -0.718 | solute carrier family 39 member 10 |
| [[ILF3]] | -0.709 | interleukin enhancer binding factor 3 |
| [[SFPQ]] | -0.708 | splicing factor proline and glutamine rich |
| [[IL6ST]] | -0.707 | interleukin 6 cytokine family signal transducer |
| [[ACADM]] | -0.706 | acyl-CoA dehydrogenase medium chain |
| [[TRIP12]] | -0.701 | thyroid hormone receptor interactor 12 |
| [[HNRNPM]] | -0.699 | heterogeneous nuclear ribonucleoprotein M |
| [[ZNF300]] | -0.695 | zinc finger protein 300 |
| [[NCR3LG1]] | -0.677 | natural killer cell cytotoxicity receptor 3 ligand 1 |
| [[HNRNPH3]] | -0.671 | heterogeneous nuclear ribonucleoprotein H3 |
| [[CHRAC1]] | -0.669 | chromatin accessibility complex subunit 1 |
| [[OXCT1]] | -0.666 | 3-oxoacid CoA-transferase 1 |
| [[CBX5]] | -0.666 | chromobox 5 |
| [[PRKAR1A]] | -0.662 | protein kinase cAMP-dependent type I regulatory subunit alpha |
| [[DPY19L1P2]] | -0.652 | DPY19L1 pseudogene 2 |
| [[GALC]] | -0.650 | galactosylceramidase |
| [[SRSF10]] | -0.646 | serine and arginine rich splicing factor 10 |
| [[PSME3]] | -0.646 | proteasome activator subunit 3 |
| [[SRSF3]] | -0.643 | serine and arginine rich splicing factor 3 |
| [[SSU72]] | -0.638 | SSU72 homolog, RNA polymerase II CTD phosphatase |
| [[CPNE1]] | -0.632 | copine 1 |
| [[PPP2CA]] | -0.632 | protein phosphatase 2 catalytic subunit alpha |
| [[NCOA4]] | -0.630 | nuclear receptor coactivator 4 |
| [[RBM12]] | -0.624 | RNA binding motif protein 12 |
| [[HMGN1]] | -0.623 | high mobility group nucleosome binding domain 1 |
| [[NXT2]] | -0.615 | nuclear transport factor 2 like export factor 2 |
| [[HNRNPD]] | -0.614 | heterogeneous nuclear ribonucleoprotein D |
| [[ELK4]] | -0.611 | ETS transcription factor ELK4 |
| [[LEPROT]] | -0.604 | leptin receptor overlapping transcript |
| [[ARHGEF9]] | -0.593 | Cdc42 guanine nucleotide exchange factor 9 |
| [[SUCLA2]] | -0.577 | succinate-CoA ligase ADP-forming subunit beta |
| [[HNRNPC]] | -0.565 | heterogeneous nuclear ribonucleoprotein C |
| [[SYNCRIP]] | -0.551 | synaptotagmin binding cytoplasmic RNA interacting protein |
| [[USP7]] | -0.551 | ubiquitin specific peptidase 7 |
| [[SOCS4]] | -0.546 | suppressor of cytokine signaling 4 |
| [[HNRNPUL1]] | -0.543 | heterogeneous nuclear ribonucleoprotein U like 1 |
| [[UTRN]] | -0.516 | utrophin |
| [[TMX4]] | -0.513 | thioredoxin related transmembrane protein 4 |
| [[KIF5B]] | -0.511 | kinesin family member 5B |
| [[MATR3]] | -0.508 | matrin 3 |
| [[SLC35A5]] | -0.507 | solute carrier family 35 member A5 |
| [[STAG2]] | -0.502 | STAG2 cohesin complex component |
| [[TOP2B]] | -0.488 | DNA topoisomerase II beta |
| [[PTBP1]] | -0.479 | polypyrimidine tract binding protein 1 |
| [[CYP4A22-AS1]] | -0.471 | CYP4A22 antisense RNA 1 |
| [[TRDMT1]] | -0.466 | tRNA aspartic acid methyltransferase 1 |
| [[WLS]] | -0.464 | Wnt ligand secretion mediator |
| [[ACAA2]] | -0.459 | acetyl-CoA acyltransferase 2 |
| [[PRNP]] | -0.452 | prion protein (Kanno blood group) |
| [[DDX39A]] | -0.450 | DExD-box helicase 39A |
| [[SF1]] | -0.436 | splicing factor 1 |
| [[WNK1]] | -0.418 | WNK lysine deficient protein kinase 1 |
| [[IFT80]] | -0.413 | intraflagellar transport 80 |
| [[AP1S3]] | -0.412 | adaptor related protein complex 1 subunit sigma 3 |
| [[TAX1BP3]] | -0.400 | Tax1 binding protein 3 |
| [[FLOT2]] | -0.396 | flotillin 2 |
| [[RNF207]] | -0.392 | ring finger protein 207 |
| [[B3GLCT]] | -0.385 | beta 3-glucosyltransferase |
| [[SUB1]] | -0.378 | SUB1 regulator of transcription |
| [[PARP4]] | -0.360 | poly(ADP-ribose) polymerase family member 4 |
| [[SUGT1P3]] | -0.350 | SUGT1 pseudogene 3 |
| [[RSC1A1]] | -0.323 | — |
| [[C1QTNF3]] | -0.247 | C1q and TNF related 3 |

## Data

- `graph/nodes.parquet` — module == 3; `graph/modules.parquet` — module == 3; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [2] (drug-dose × line)
