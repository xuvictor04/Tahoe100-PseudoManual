---
module: 12
type: "module"
n_genes: 215
n_plus: 195
n_minus: 20
arms_opposite: true
mean_cos_between_arms: -0.2848765552043915
label: "mRNA Splicing - Major Pathway"
label_source: "reactome"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 012

*mRNA Splicing - Major Pathway · 215 genes (195 in the + arm, 20 in the − arm) · [[Module 012.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28). The + arm rises where the − arm falls. Arm = the side of the module's main direction a gene sits on.

Label from the validation stage: **mRNA Splicing - Major Pathway** (reactome, q 1e-06; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| + | mRNA Splicing - Major Pathway | reactome | 17/195 | 6.44 | 1e-06 |
| + | mRNA Splicing | reactome | 17/195 | 6.20 | 2e-06 |
| all | mRNA Splicing - Major Pathway | reactome | 17/215 | 5.84 | 4e-06 |
| + | Processing of Capped Intron-Containing Pre-mRNA | reactome | 19/195 | 5.05 | 6e-06 |
| all | mRNA Splicing | reactome | 17/215 | 5.62 | 8e-06 |
| + | Metabolism of RNA | reactome | 30/195 | 3.18 | 1e-05 |
| all | Processing of Capped Intron-Containing Pre-mRNA | reactome | 19/215 | 4.58 | 3e-05 |
| all | Metabolism of RNA | reactome | 30/215 | 2.89 | 1e-04 |

## Drugs that move it

*Mean pooled z of the + arm minus the − arm (`graph/module_pooled_z.npy`, row 11), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it (+ arm up, − arm down): [[Homoharringtonine (drug)]] 5 µM (+10.0, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (+9.6, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (+7.8, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (+6.3, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.05 µM (+4.8); [[Selinexor (drug)]] 5 µM (+2.7, ⚠ cell-cycle shift); [[Docetaxel (Trihydrate) (drug)]] 0.5 µM (+2.5); [[Selinexor (drug)]] 0.5 µM (+2.4, ⚠ cell-cycle shift); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM (+2.3); [[Harringtonine (drug)]] 0.05 µM (+2.2); [[GSK1059615 (drug)]] 0.5 µM (+2.1); [[Bimiralisib (drug)]] 0.5 µM (+2.0); [[Ipatasertib (drug)]] 0.5 µM (+1.9); [[Methylprednisolone succinate (drug)]] 0.5 µM (+1.8); [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM (+1.8); [[Binimetinib (drug)]] 0.05 µM (+1.7) (90 in all, 20 with an alert ⚠; shown: the 10 strongest and the 6 next strongest without an alert)
- Lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM (-11.0, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (-9.2, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (-9.0, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (-6.7, ⚠ toxic; transcription drop; cell-cycle shift); [[Digitoxin (drug)]] 0.5 µM (-6.6, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (-5.5, ⚠ cell-cycle shift); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (-5.4, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (-4.9, ⚠ cell-cycle shift); [[Epirubicin (hydrochloride) (drug)]] 5 µM (-4.8, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (-4.2, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (-3.7); [[Brivudine (drug)]] 5 µM (-2.5); [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM (-2.2); [[PH-797804 (drug)]] 0.05 µM (-2.0); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (-2.0); [[Auranofin (drug)]] 5 µM (-1.7); [[Fusidic acid (drug)]] 5 µM (-1.7); [[Pyridoxine (hydrochloride) (drug)]] 5 µM (-1.7); [[Fenofibrate (drug)]] 0.05 µM (-1.7); [[Berberine (chloride hydrate) (drug)]] 5 µM (-1.7) (86 in all, 23 with an alert ⚠; shown: the 10 strongest and the 10 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[KATO III (line)]], [[PANC-1 (line)]], [[SW480 (line)]], [[LS 180 (line)]], [[RKO (line)]], [[A-172 (line)]], [[NCI-H460 (line)]], [[HEC-1-A (line)]]

## Candidate new members

*Members not annotated to the set their arm is enriched for, ranked by mean cos to the annotated members (`validation/novel_members.csv`); ⚠ = a reason to doubt the gene's place (in the vector space only through flagged drug-doses), kept in its rank. 14 candidates, none with an alert.*

| # | Gene | Set | Mean cos |
|---|---|---|---|
| 1 | [[CCDC174]] | mRNA Splicing - Major Pathway | +0.62 |
| 2 | [[SLC4A1AP]] | mRNA Splicing - Major Pathway | +0.56 |
| 3 | [[ZC3H13]] | mRNA Splicing - Major Pathway | +0.54 |
| 4 | [[SEC62]] | mRNA Splicing - Major Pathway | +0.54 |
| 5 | [[FRG1]] | mRNA Splicing - Major Pathway | +0.53 |
| 6 | [[PHAX]] | mRNA Splicing - Major Pathway | +0.53 |
| 7 | [[MRPS18C]] | mRNA Splicing - Major Pathway | +0.52 |
| 8 | [[COIL]] | mRNA Splicing - Major Pathway | +0.52 |
| 9 | [[NFKBIL1]] | mRNA Splicing - Major Pathway | +0.51 |
| 10 | [[SNHG11]] | mRNA Splicing - Major Pathway | +0.51 |
| 11 | [[ASB8]] | mRNA Splicing - Major Pathway | +0.50 |
| 12 | [[C18orf21]] | mRNA Splicing - Major Pathway | +0.50 |
| 13 | [[MED19]] | mRNA Splicing - Major Pathway | +0.50 |
| 14 | [[CCDC43]] | mRNA Splicing - Major Pathway | +0.50 |

*⚠ 2 of its 215 genes are in the vector space only through drug-doses that carry an alert (`embed/genes.parquet` evidence_flagged_only): their place here may reflect what those drug-doses did to the cells. They are marked in the tables of this note.*

## + arm (195)

| Gene | Projection | Name | Alert |
|---|---|---|---|
| [[CCDC174]] | 0.894 | coiled-coil domain containing 174 |  |
| [[RBMX2]] | 0.876 | RNA binding motif protein X-linked 2 |  |
| [[RP9]] | 0.864 | RP9 pre-mRNA splicing factor |  |
| [[PHAX]] | 0.861 | phosphorylated adaptor for RNA export |  |
| [[C18orf21]] | 0.855 | ribonuclease MRP subunit p24 |  |
| [[SNHG11]] | 0.853 | small nucleolar RNA host gene 11 |  |
| [[ASB8]] | 0.821 | ankyrin repeat and SOCS box containing 8 |  |
| [[NFKBIL1]] | 0.819 | NFKB inhibitor like 1 |  |
| [[COIL]] | 0.808 | coilin |  |
| [[MRPS31]] | 0.797 | mitochondrial ribosomal protein S31 |  |
| [[EBAG9]] | 0.795 | estrogen receptor binding site associated antigen 9 |  |
| [[PEX12]] | 0.794 | peroxisomal biogenesis factor 12 |  |
| [[SEC62]] | 0.791 | SEC62 preprotein translocation factor |  |
| [[SNW1]] | 0.790 | SNW domain containing 1 |  |
| [[CINP]] | 0.789 | cyclin dependent kinase 2 interacting protein |  |
| [[PIGBOS1]] | 0.784 | PIGB opposite strand 1 |  |
| [[MED19]] | 0.774 | mediator complex subunit 19 |  |
| [[STK16]] | 0.771 | serine/threonine kinase 16 |  |
| [[FRG1]] | 0.770 | FSHD region gene 1 |  |
| [[MRPS18C]] | 0.769 | mitochondrial ribosomal protein S18C |  |
| [[PPIG]] | 0.765 | peptidylprolyl isomerase G |  |
| [[FRA10AC1]] | 0.763 | FRA10A associated CGG repeat 1 |  |
| [[ZNF579]] | 0.762 | zinc finger protein 579 |  |
| [[NRBF2]] | 0.762 | nuclear receptor binding factor 2 |  |
| [[RIOK2]] | 0.761 | RIO kinase 2 |  |
| [[KBTBD7]] | 0.758 | kelch repeat and BTB domain containing 7 |  |
| [[RNF113A]] | 0.748 | ring finger protein 113A |  |
| [[DNAL4]] | 0.747 | dynein axonemal light chain 4 |  |
| [[VIRMA]] | 0.745 | vir like m6A methyltransferase associated |  |
| [[LEO1]] | 0.743 | LEO1 component of Paf1/RNA polymerase II complex |  |
| [[ZNF205]] | 0.742 | zinc finger protein 205 |  |
| [[NEMF]] | 0.742 | nuclear export mediator factor |  |
| [[MPHOSPH10]] | 0.740 | M-phase phosphoprotein 10 |  |
| [[ASNSD1]] | 0.739 | asparagine synthetase domain containing 1 |  |
| [[MMADHC]] | 0.733 | metabolism of cobalamin associated D |  |
| [[CCDC43]] | 0.731 | coiled-coil domain containing 43 |  |
| [[GORAB]] | 0.729 | golgin, RAB6 interacting |  |
| [[SNAPIN]] | 0.728 | SNAP associated protein |  |
| [[TCEAL8]] | 0.726 | transcription elongation factor A like 8 |  |
| [[TARS2]] | 0.725 | threonyl-tRNA synthetase 2, mitochondrial |  |
| [[SLC4A1AP]] | 0.724 | solute carrier family 4 member 1 adaptor protein |  |
| [[ZC3H13]] | 0.723 | zinc finger CCCH-type containing 13 |  |
| [[NAA30]] | 0.721 | N-alpha-acetyltransferase 30, NatC catalytic subunit |  |
| [[ZCCHC9]] | 0.720 | zinc finger CCHC-type containing 9 |  |
| [[SNRPB2]] | 0.720 | small nuclear ribonucleoprotein polypeptide B2 |  |
| [[AMZ2P1-1]] | 0.716 | — |  |
| [[PPP4R2]] | 0.714 | protein phosphatase 4 regulatory subunit 2 |  |
| [[R3HCC1]] | 0.711 | R3H domain and coiled-coil containing 1 |  |
| [[DCTN6]] | 0.711 | dynactin subunit 6 |  |
| [[SPOP]] | 0.708 | speckle type BTB/POZ protein |  |
| [[TMEM42]] | 0.706 | transmembrane protein 42 |  |
| [[MRPL21]] | 0.703 | mitochondrial ribosomal protein L21 |  |
| [[NOL7]] | 0.700 | nucleolar protein 7 | ⚠ only flagged evidence |
| [[MRPS33]] | 0.694 | mitochondrial ribosomal protein S33 |  |
| [[DPF2]] | 0.691 | double PHD fingers 2 |  |
| [[NSUN5]] | 0.689 | NOP2/Sun RNA methyltransferase 5 |  |
| [[PUS3]] | 0.688 | pseudouridine synthase 3 |  |
| [[GFER]] | 0.687 | growth factor, augmenter of liver regeneration |  |
| [[SURF2]] | 0.685 | surfeit 2 |  |
| [[NDUFA8]] | 0.683 | NADH:ubiquinone oxidoreductase subunit A8 |  |
| [[C2orf74]] | 0.681 | DPM1 ER membrane anchor 1 |  |
| [[BNIP1]] | 0.680 | BCL2 interacting protein 1 |  |
| [[HEIH]] | 0.678 | hepatocellular carcinoma up-regulated EZH2-associated long non-coding RNA |  |
| [[TMEM216]] | 0.677 | transmembrane protein 216 |  |
| [[ELOF1]] | 0.677 | elongation factor 1 |  |
| [[PI4KB]] | 0.671 | phosphatidylinositol 4-kinase beta |  |
| [[MFAP1]] | 0.669 | microfibril associated protein 1 |  |
| [[MTRES1]] | 0.664 | mitochondrial transcription rescue factor 1 |  |
| [[KBTBD6]] | 0.662 | kelch repeat and BTB domain containing 6 |  |
| [[PRPF6]] | 0.661 | pre-mRNA processing factor 6 |  |
| [[DCP1A]] | 0.659 | decapping mRNA 1A |  |
| [[COMMD3]] | 0.659 | COMM domain containing 3 |  |
| [[SUCLG1]] | 0.652 | succinate-CoA ligase GDP/ADP-forming subunit alpha |  |
| [[ZC3H15]] | 0.650 | zinc finger CCCH-type containing 15 |  |
| [[TMEM265]] | 0.650 | transmembrane protein 265 |  |
| [[CREB3]] | 0.649 | cAMP responsive element binding protein 3 |  |
| [[MRPL57]] | 0.649 | mitochondrial ribosomal protein L57 |  |
| [[MPHOSPH8]] | 0.648 | M-phase phosphoprotein 8 |  |
| [[LINC00888-1]] | 0.646 | — |  |
| [[SRSF11]] | 0.645 | serine and arginine rich splicing factor 11 | ⚠ only flagged evidence |
| [[SNRNP27]] | 0.641 | small nuclear ribonucleoprotein U4/U6.U5 subunit 27 |  |
| [[BCAS2]] | 0.640 | BCAS2 pre-mRNA processing factor |  |
| [[DECR2]] | 0.638 | 2,4-dienoyl-CoA reductase 2 |  |
| [[HAX1]] | 0.637 | HCLS1 associated protein X-1 |  |
| [[NDUFB9]] | 0.637 | NADH:ubiquinone oxidoreductase subunit B9 |  |
| [[MRPL10]] | 0.636 | mitochondrial ribosomal protein L10 |  |
| [[CEP290]] | 0.628 | centrosomal protein 290 |  |
| [[EMC9]] | 0.625 | ER membrane protein complex subunit 9 |  |
| [[BRF2]] | 0.621 | BRF2 general transcription factor IIIB subunit |  |
| [[NFU1]] | 0.615 | NFU1 iron-sulfur cluster scaffold |  |
| [[TCEANC]] | 0.613 | transcription elongation factor A N-terminal and central domain containing |  |
| [[DHX36]] | 0.608 | DEAH-box helicase 36 |  |
| [[DRG1]] | 0.599 | developmentally regulated GTP binding protein 1 |  |
| [[DHX29]] | 0.596 | DExH-box helicase 29 |  |
| [[IWS1]] | 0.595 | interacts with SUPT6H, CTD assembly factor 1 |  |
| [[CIDECP1]] | 0.593 | CIDEC pseudogene 1 |  |
| [[PRDM4]] | 0.591 | PR/SET domain 4 |  |
| [[ZNF622]] | 0.590 | zinc finger protein 622 |  |
| [[BDP1]] | 0.583 | BDP1 general transcription factor IIIB subunit |  |
| [[DNAJB2]] | 0.582 | DnaJ heat shock protein family (Hsp40) member B2 |  |
| [[THAP3]] | 0.581 | THAP domain containing 3 |  |
| [[ZNF555]] | 0.579 | zinc finger protein 555 |  |
| [[PNPLA4]] | 0.579 | patatin like domain 4, phospholipase and triacylglycerol lipase |  |
| [[GTF2H5]] | 0.578 | general transcription factor IIH subunit 5 |  |
| [[MYG1]] | 0.578 | MYG1 exonuclease |  |
| [[DNAJC2]] | 0.577 | DnaJ heat shock protein family (Hsp40) member C2 |  |
| [[CDC5L]] | 0.577 | cell division cycle 5 like |  |
| [[SUGT1P3-1]] | 0.576 | — |  |
| [[YIF1A]] | 0.575 | Yip1 interacting factor homolog A, membrane trafficking protein |  |
| [[RSRC2]] | 0.571 | arginine and serine rich coiled-coil 2 |  |
| [[RNF166]] | 0.571 | ring finger protein 166 |  |
| [[PSMB1]] | 0.571 | proteasome 20S subunit beta 1 |  |
| [[GPATCH1]] | 0.571 | G-patch domain containing 1 |  |
| [[PRRC2C]] | 0.564 | proline rich coiled-coil 2C |  |
| [[FAM32A]] | 0.556 | family with sequence similarity 32 member A |  |
| [[CCDC51]] | 0.554 | coiled-coil domain containing 51 |  |
| [[PPP1R12A]] | 0.553 | protein phosphatase 1 regulatory subunit 12A |  |
| [[CHD9]] | 0.552 | chromodomain helicase DNA binding protein 9 |  |
| [[SAP18]] | 0.551 | Sin3A associated protein 18 |  |
| [[METTL25B]] | 0.551 | methyltransferase like 25B |  |
| [[NDUFV3]] | 0.549 | NADH:ubiquinone oxidoreductase subunit V3 |  |
| [[POLK]] | 0.548 | DNA polymerase kappa |  |
| [[OSCP1]] | 0.539 | organic solute carrier partner 1 |  |
| [[ZSWIM9]] | 0.538 | zinc finger SWIM-type containing 9 |  |
| [[HDDC3]] | 0.537 | HD domain containing 3 |  |
| [[ALG2]] | 0.536 | ALG2 alpha-1,3/1,6-mannosyltransferase |  |
| [[TCEAL9]] | 0.536 | transcription elongation factor A like 9 |  |
| [[KIF3B]] | 0.531 | kinesin family member 3B |  |
| [[PDLIM2]] | 0.523 | PDZ and LIM domain 2 |  |
| [[TSR3]] | 0.520 | TSR3 ribosome maturation factor |  |
| [[ATG4D]] | 0.519 | autophagy related 4D cysteine peptidase |  |
| [[FNBP4]] | 0.515 | formin binding protein 4 |  |
| [[CBY1]] | 0.513 | chibby 1, beta catenin antagonist |  |
| [[TBL2]] | 0.512 | transducin beta like 2 |  |
| [[MSRB2]] | 0.508 | methionine sulfoxide reductase B2 |  |
| [[ZNF213]] | 0.507 | zinc finger protein 213 |  |
| [[USP8]] | 0.505 | ubiquitin specific peptidase 8 |  |
| [[CDPF1]] | 0.501 | cysteine rich DPF motif domain containing 1 |  |
| [[ZSCAN16]] | 0.490 | zinc finger and SCAN domain containing 16 |  |
| [[NVL]] | 0.489 | nuclear VCP like |  |
| [[POLM]] | 0.484 | DNA polymerase mu |  |
| [[CUEDC2]] | 0.483 | CUE domain containing 2 |  |
| [[FAHD2B]] | 0.481 | fumarylacetoacetate hydrolase domain containing 2B |  |
| [[AP3S2]] | 0.481 | adaptor related protein complex 3 subunit sigma 2 |  |
| [[MORN2]] | 0.479 | MORN repeat containing 2 |  |
| [[SPRYD7]] | 0.477 | SPRY domain containing 7 |  |
| [[CRB3]] | 0.477 | crumbs cell polarity complex component 3 |  |
| [[CAVIN3]] | 0.462 | caveolae associated protein 3 |  |
| [[CIRBP]] | 0.461 | cold inducible RNA binding protein |  |
| [[VPS28]] | 0.457 | VPS28 subunit of ESCRT-I |  |
| [[ZNF737]] | 0.457 | zinc finger protein 737 |  |
| [[CMAS]] | 0.454 | cytidine monophosphate N-acetylneuraminic acid synthetase |  |
| [[WBP2NL]] | 0.454 | WBP2 N-terminal like |  |
| [[AARSD1]] | 0.453 | alanyl-tRNA synthetase domain containing 1 |  |
| [[CZIB]] | 0.452 | CXXC motif containing zinc binding protein |  |
| [[GEMIN8]] | 0.449 | gem nuclear organelle associated protein 8 |  |
| [[GPS2]] | 0.448 | G protein pathway suppressor 2 |  |
| [[NUDCD2]] | 0.448 | NudC domain containing 2 |  |
| [[RNASEL]] | 0.439 | ribonuclease L |  |
| [[ZBTB48]] | 0.437 | zinc finger and BTB domain containing 48 |  |
| [[NAT1]] | 0.434 | N-acetyltransferase 1 |  |
| [[MLST8]] | 0.433 | MTOR associated protein MLST8 |  |
| [[PPP1R3D]] | 0.431 | protein phosphatase 1 regulatory subunit 3D |  |
| [[XRCC1]] | 0.430 | X-ray repair cross complementing 1 |  |
| [[AGTRAP]] | 0.429 | angiotensin II receptor associated protein |  |
| [[FAM241B]] | 0.427 | family with sequence similarity 241 member B |  |
| [[GFUS]] | 0.425 | GDP-L-fucose synthase |  |
| [[UBC]] | 0.421 | ubiquitin C |  |
| [[COA8]] | 0.420 | cytochrome c oxidase assembly factor 8 |  |
| [[RBM4B]] | 0.413 | RNA binding motif protein 4B |  |
| [[RAD23A]] | 0.405 | RAD23 nucleotide excision repair protein A |  |
| [[CLBA1]] | 0.403 | clathrin binding box of aftiphilin containing 1 |  |
| [[RBM25]] | 0.402 | RNA binding motif protein 25 |  |
| [[POLR3A]] | 0.401 | RNA polymerase III subunit A |  |
| [[COX19]] | 0.400 | cytochrome c oxidase assembly factor COX19 |  |
| [[ALG12]] | 0.400 | ALG12 alpha-1,6-mannosyltransferase |  |
| [[U2AF1L4]] | 0.398 | U2 small nuclear RNA auxiliary factor 1 like 4 |  |
| [[LENG9]] | 0.397 | leukocyte receptor cluster member 9 |  |
| [[ARFIP1]] | 0.380 | ARF interacting protein 1 |  |
| [[GON7]] | 0.376 | GON7 subunit of KEOPS complex |  |
| [[ZNF32]] | 0.363 | zinc finger protein 32 |  |
| [[TRIP4]] | 0.362 | thyroid hormone receptor interactor 4 |  |
| [[EIF4A2]] | 0.357 | eukaryotic translation initiation factor 4A2 |  |
| [[UBR1]] | 0.348 | ubiquitin protein ligase E3 component n-recognin 1 |  |
| [[KLHL35]] | 0.339 | kelch like family member 35 |  |
| [[CCDC144BP]] | 0.335 | coiled-coil domain containing 144B, pseudogene |  |
| [[AP1G1]] | 0.332 | adaptor related protein complex 1 subunit gamma 1 |  |
| [[ROCK1]] | 0.331 | Rho associated coiled-coil containing protein kinase 1 |  |
| [[CPT1B]] | 0.331 | carnitine palmitoyltransferase 1B |  |
| [[HNRNPH1]] | 0.299 | heterogeneous nuclear ribonucleoprotein H1 |  |
| [[ZNF77]] | 0.293 | zinc finger protein 77 |  |
| [[OXSM]] | 0.284 | 3-oxoacyl-ACP synthase, mitochondrial |  |
| [[NFS1]] | 0.277 | NFS1 cysteine desulfurase |  |
| [[THOC2]] | 0.260 | THO complex subunit 2 |  |
| [[PPP1R7]] | 0.251 | protein phosphatase 1 regulatory subunit 7 |  |

## − arm (20)

| Gene | Projection | Name | Alert |
|---|---|---|---|
| [[SMG1P3]] | -0.646 | SMG1 pseudogene 3 |  |
| [[BCAP31]] | -0.625 | B cell receptor associated protein 31 |  |
| [[PTDSS1]] | -0.615 | phosphatidylserine synthase 1 |  |
| [[EIF4EBP2]] | -0.608 | eukaryotic translation initiation factor 4E binding protein 2 |  |
| [[MAPK9]] | -0.595 | mitogen-activated protein kinase 9 |  |
| [[FAM81A]] | -0.587 | family with sequence similarity 81 member A |  |
| [[ACLY]] | -0.537 | ATP citrate lyase |  |
| [[MAN2C1]] | -0.531 | mannosidase alpha class 2C member 1 |  |
| [[CTSC]] | -0.519 | cathepsin C |  |
| [[TSPAN3]] | -0.501 | tetraspanin 3 |  |
| [[TUFM]] | -0.465 | Tu translation elongation factor, mitochondrial |  |
| [[MARCKSL1]] | -0.460 | MARCKS like 1 |  |
| [[NAXE]] | -0.453 | NAD(P)HX epimerase |  |
| [[DNAJB6]] | -0.453 | DnaJ heat shock protein family (Hsp40) member B6 |  |
| [[MED14]] | -0.429 | mediator complex subunit 14 |  |
| [[PROCR]] | -0.416 | protein C receptor |  |
| [[ABI2]] | -0.404 | abl interactor 2 |  |
| [[CRNDE]] | -0.366 | colorectal neoplasia differentially expressed |  |
| [[GOLM2]] | -0.363 | golgi membrane protein 2 |  |
| [[IVNS1ABP]] | -0.329 | influenza virus NS1A binding protein |  |

## Data

- `graph/nodes.parquet` — module == 12; `graph/modules.parquet` — module == 12; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [11] (drug-dose × line)
