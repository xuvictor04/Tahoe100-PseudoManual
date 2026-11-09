---
module: 28
type: "module"
n_genes: 154
n_plus: 140
n_minus: 14
arms_opposite: true
mean_cos_between_arms: -0.26631876826286316
label: "Intraflagellar transport"
label_source: "reactome"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 028

*Intraflagellar transport · 154 genes (140 in the + arm, 14 in the − arm) · [[Module 028.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27). The + arm rises where the − arm falls. Arm = the side of the module's main direction a gene sits on.

Label from the validation stage: **Intraflagellar transport** (reactome, q 0.028; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| + | Intraflagellar transport | reactome | 5/140 | 11.5 | 0.028 |
| all | Intraflagellar transport | reactome | 5/154 | 10.4 | 0.041 |

## Drugs that move it

*Mean pooled z of the + arm minus the − arm (`graph/module_pooled_z.npy`, row 27), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it (+ arm up, − arm down): [[Homoharringtonine (drug)]] 5 µM (+18.0, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (+13.4, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (+12.9, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (+8.6, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.05 µM (+5.7); [[TAK-901 (drug)]] 5 µM (+3.8, ⚠ cell-cycle shift); [[Selinexor (drug)]] 5 µM (+3.4, ⚠ cell-cycle shift); [[Ponatinib (drug)]] 5 µM (+3.2); [[Trametinib (drug)]] 5 µM (+2.9, ⚠ cell-cycle shift); [[Binimetinib (drug)]] 0.5 µM (+2.6); [[Cobimetinib (drug)]] 5 µM (+2.6); [[Harringtonine (drug)]] 0.05 µM (+2.4); [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM (+2.2); [[Binimetinib (drug)]] 5 µM (+2.1); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM (+2.1); [[Cobimetinib (drug)]] 0.5 µM (+2.0); [[Trametinib (drug)]] 0.05 µM (+2.0) (44 in all, 14 with an alert ⚠; shown: the 10 strongest and the 7 next strongest without an alert)
- Lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM (-8.2, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (-7.2, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 5 µM (-7.0, ⚠ toxic; transcription drop; cell-cycle shift); [[Digitoxin (drug)]] 0.5 µM (-6.2, ⚠ cell-cycle shift); [[Auranofin (drug)]] 5 µM (-6.1); [[Belinostat (drug)]] 5 µM (-5.7, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (-5.5, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (-5.4, ⚠ cell-cycle shift); [[Ixazomib citrate (drug)]] 5 µM (-4.8, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (-4.8, ⚠ cell-cycle shift); [[Ixazomib citrate (drug)]] 0.5 µM (-2.3); [[PF-06260933 (drug)]] 5 µM (-2.0); [[Tucidinostat (drug)]] 5 µM (-1.8); [[Bortezomib (drug)]] 0.5 µM (-1.7); [[Vilanterol (drug)]] 0.5 µM (-1.7); [[Thymol (drug)]] 0.5 µM (-1.6); [[Peretinoin (drug)]] 0.5 µM (-1.5); [[Bergenin (drug)]] 0.5 µM (-1.5); [[Vilanterol (drug)]] 5 µM (-1.5) (52 in all, 28 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[SW480 (line)]], [[PANC-1 (line)]], [[A-172 (line)]], [[A-427 (line)]], [[KATO III (line)]], [[A549 (line)]], [[RKO (line)]], [[NCI-H460 (line)]]

*⚠ 1 of its 154 genes are in the vector space only through drug-doses that carry an alert (`embed/genes.parquet` evidence_flagged_only): their place here may reflect what those drug-doses did to the cells. They are marked in the tables of this note.*

## + arm (140)

| Gene | Projection | Name | Alert |
|---|---|---|---|
| [[CCDC25]] | 0.864 | coiled-coil domain containing 25 |  |
| [[RAD52]] | 0.836 | RAD52 DNA repair protein |  |
| [[SMARCE1]] | 0.830 | SWI/SNF related BAF chromatin remodeling complex subunit E1 |  |
| [[CLK4]] | 0.810 | CDC like kinase 4 |  |
| [[COQ5]] | 0.805 | coenzyme Q5, methyltransferase |  |
| [[NDUFA5]] | 0.800 | NADH:ubiquinone oxidoreductase subunit A5 |  |
| [[AASDHPPT]] | 0.795 | aminoadipate-semialdehyde dehydrogenase-phosphopantetheinyl transferase |  |
| [[IFT74]] | 0.784 | intraflagellar transport 74 |  |
| [[SLC25A46]] | 0.781 | solute carrier family 25 member 46 |  |
| [[CHURC1]] | 0.780 | churchill domain containing 1 |  |
| [[COPS5]] | 0.774 | COP9 signalosome subunit 5 |  |
| [[AIMP1]] | 0.772 | aminoacyl tRNA synthetase complex interacting multifunctional protein 1 |  |
| [[FUNDC1]] | 0.769 | FUN14 domain containing 1 |  |
| [[TRMT10B]] | 0.766 | tRNA methyltransferase 10B |  |
| [[SEPSECS]] | 0.766 | Sep (O-phosphoserine) tRNA:Sec (selenocysteine) tRNA synthase |  |
| [[DARS1]] | 0.761 | aspartyl-tRNA synthetase 1 |  |
| [[RAD50]] | 0.760 | RAD50 double strand break repair protein |  |
| [[SUPT20H]] | 0.758 | SPT20 homolog, SAGA complex component |  |
| [[GIN1]] | 0.744 | gypsy retrotransposon integrase 1 |  |
| [[POLI]] | 0.744 | DNA polymerase iota |  |
| [[PEX1]] | 0.743 | peroxisomal biogenesis factor 1 |  |
| [[TMEM128]] | 0.741 | transmembrane protein 128 |  |
| [[MKS1]] | 0.733 | MKS transition zone complex subunit 1 |  |
| [[DZIP3]] | 0.732 | DAZ interacting zinc finger protein 3 |  |
| [[FAM114A2]] | 0.731 | family with sequence similarity 114 member A2 |  |
| [[RNF214]] | 0.716 | ring finger protein 214 |  |
| [[KCTD18]] | 0.711 | potassium channel tetramerization domain containing 18 |  |
| [[DBT]] | 0.710 | dihydrolipoamide branched chain transacylase E2 |  |
| [[TRMT1L]] | 0.709 | tRNA methyltransferase 1L |  |
| [[TYW5]] | 0.708 | tRNA-yW synthesizing protein 5 |  |
| [[COG4]] | 0.704 | component of oligomeric golgi complex 4 |  |
| [[TRUB1]] | 0.699 | TruB pseudouridine synthase family member 1 |  |
| [[PHC3]] | 0.690 | polyhomeotic homolog 3 |  |
| [[ZC3H7A]] | 0.682 | zinc finger CCCH-type containing 7A |  |
| [[PMPCB]] | 0.679 | peptidase, mitochondrial processing subunit beta |  |
| [[DDX1]] | 0.676 | DEAD-box helicase 1 |  |
| [[ZC3H6]] | 0.672 | zinc finger CCCH-type containing 6 |  |
| [[CLUAP1]] | 0.669 | intraflagellar transport 38 |  |
| [[ANKRD26]] | 0.669 | ankyrin repeat domain 26 |  |
| [[SCRN3]] | 0.668 | secernin 3 |  |
| [[CEP63]] | 0.667 | centrosomal protein 63 |  |
| [[CILK1]] | 0.667 | ciliogenesis associated kinase 1 |  |
| [[NSMCE1]] | 0.666 | NSE1 component of SMC5/6 complex |  |
| [[TRIP11]] | 0.658 | thyroid hormone receptor interactor 11 |  |
| [[CCDC113]] | 0.657 | cilia and flagella associated protein 263 |  |
| [[ZSCAN21]] | 0.654 | zinc finger and SCAN domain containing 21 |  |
| [[IFT46]] | 0.650 | intraflagellar transport 46 |  |
| [[STAMBP]] | 0.647 | STAM binding protein |  |
| [[NFYB]] | 0.646 | nuclear transcription factor Y subunit beta |  |
| [[COQ6]] | 0.645 | coenzyme Q6, monooxygenase |  |
| [[COQ9]] | 0.642 | coenzyme Q9 |  |
| [[EXOSC8]] | 0.637 | exosome component 8 |  |
| [[NBN]] | 0.633 | nibrin |  |
| [[CCDC90B]] | 0.632 | coiled-coil domain containing 90B |  |
| [[AGL]] | 0.631 | amylo-alpha-1,6-glucosidase and 4-alpha-glucanotransferase |  |
| [[WASHC3]] | 0.631 | WASH complex subunit 3 |  |
| [[FAM204A]] | 0.628 | family with sequence similarity 204 member A |  |
| [[ANAPC16]] | 0.625 | anaphase promoting complex subunit 16 |  |
| [[CFL2]] | 0.621 | cofilin 2 |  |
| [[CETN3]] | 0.621 | centrin 3 |  |
| [[NUDT12]] | 0.620 | nudix hydrolase 12 |  |
| [[TAB2]] | 0.620 | TGF-beta activated kinase 1 (MAP3K7) binding protein 2 |  |
| [[ATP5PB]] | 0.619 | ATP synthase peripheral stalk-membrane subunit b |  |
| [[ELAC1]] | 0.617 | elaC ribonuclease Z 1 |  |
| [[TMEM260]] | 0.617 | transmembrane protein 260 |  |
| [[LSM14A]] | 0.616 | LSM14A mRNA processing body assembly factor |  |
| [[ZDHHC4]] | 0.611 | zDHHC palmitoyltransferase 4 |  |
| [[FCF1]] | 0.610 | FCF1 rRNA-processing protein |  |
| [[LINC01473]] | 0.609 | long independently transcribed non-coding RNA 1473 |  |
| [[RPAP2]] | 0.608 | RNA polymerase II associated protein 2 |  |
| [[SPG11]] | 0.608 | SPG11 vesicle trafficking associated, spatacsin |  |
| [[GOLGA1]] | 0.604 | golgin A1 |  |
| [[SPEF2]] | 0.601 | sperm flagellar and cilia associated 2 |  |
| [[AMACR]] | 0.600 | alpha-methylacyl-CoA racemase |  |
| [[ERMARD]] | 0.599 | ER membrane associated RNA degradation |  |
| [[CEP350]] | 0.598 | centrosomal protein 350 |  |
| [[CLCN3]] | 0.598 | Cl-/H+ antiporter 3 |  |
| [[AMZ2P1]] | 0.596 | AMZ2 pseudogene 1 |  |
| [[SF3B1]] | 0.592 | splicing factor 3b subunit 1 |  |
| [[INTS12]] | 0.591 | integrator complex subunit 12 |  |
| [[NEDD4]] | 0.572 | NEDD4 E3 ubiquitin protein ligase |  |
| [[ARMCX5]] | 0.569 | armadillo repeat containing X-linked 5 |  |
| [[BMI1]] | 0.563 | BMI1 proto-oncogene, polycomb ring finger |  |
| [[MDM4]] | 0.558 | MDM4 regulator of p53 |  |
| [[SCAF11]] | 0.554 | SR-related CTD associated factor 11 |  |
| [[PDIK1L]] | 0.553 | PDLIM1 interacting kinase 1 like |  |
| [[AZI2]] | 0.551 | 5-azacytidine induced 2 |  |
| [[ZNF711]] | 0.550 | ZFX family zinc finger ZNF711 |  |
| [[DCUN1D1]] | 0.549 | defective in cullin neddylation 1 domain containing 1 |  |
| [[LRRC37A2]] | 0.546 | leucine rich repeat containing 37 member A2 |  |
| [[PAIP1]] | 0.545 | poly(A) binding protein interacting protein 1 |  |
| [[ZNF227]] | 0.541 | zinc finger protein 227 |  |
| [[GTF3A]] | 0.540 | general transcription factor IIIA | ⚠ only flagged evidence |
| [[CHM]] | 0.536 | CHM Rab escort protein |  |
| [[ZNG1A]] | 0.536 | Zn regulated GTPase metalloprotein activator 1A |  |
| [[OSGEP]] | 0.534 | O-sialoglycoprotein endopeptidase |  |
| [[TAB3]] | 0.533 | TGF-beta activated kinase 1 (MAP3K7) binding protein 3 |  |
| [[TBCEL]] | 0.530 | tubulin folding cofactor E like |  |
| [[TTC8]] | 0.530 | tetratricopeptide repeat domain 8 |  |
| [[NDUFB5]] | 0.529 | NADH:ubiquinone oxidoreductase subunit B5 |  |
| [[TBCK]] | 0.526 | TBC1 domain containing kinase |  |
| [[MRPS10]] | 0.525 | mitochondrial ribosomal protein S10 |  |
| [[MTMR6]] | 0.524 | myotubularin related protein 6 |  |
| [[GLOD4]] | 0.521 | glyoxalase domain containing 4 |  |
| [[ACAD11]] | 0.520 | acyl-CoA dehydrogenase family member 11 |  |
| [[C2CD5]] | 0.519 | C2 calcium dependent domain containing 5 |  |
| [[BDH2]] | 0.513 | 3-hydroxybutyrate dehydrogenase 2 |  |
| [[ZNF638]] | 0.509 | zinc finger protein 638 |  |
| [[RUFY1]] | 0.504 | RUN and FYVE domain containing 1 |  |
| [[SYNE1]] | 0.504 | spectrin repeat containing nuclear envelope protein 1 |  |
| [[LMLN]] | 0.501 | leishmanolysin like peptidase |  |
| [[IFT81]] | 0.501 | intraflagellar transport 81 |  |
| [[TAF15]] | 0.495 | TATA-box binding protein associated factor 15 |  |
| [[MDM1]] | 0.488 | stabilizer of axonemal microtubules 6 |  |
| [[MAP9]] | 0.485 | microtubule associated protein 9 |  |
| [[TEX9]] | 0.481 | testis expressed 9 |  |
| [[RAB3GAP2]] | 0.475 | RAB3 GTPase activating non-catalytic protein subunit 2 |  |
| [[DMXL2]] | 0.457 | Dmx like 2 |  |
| [[CEP120]] | 0.449 | centrosomal protein 120 |  |
| [[ATG10]] | 0.446 | autophagy related 10 |  |
| [[AGAP9]] | 0.445 | ArfGAP with GTPase domain, ankyrin repeat and PH domain 9 |  |
| [[REST]] | 0.431 | RE1 silencing transcription factor |  |
| [[PKN2]] | 0.427 | protein kinase N2 |  |
| [[MBLAC2]] | 0.425 | metallo-beta-lactamase domain containing 2 |  |
| [[FAM149B1]] | 0.419 | family with sequence similarity 149 member B1 |  |
| [[RMDN1]] | 0.417 | regulator of microtubule dynamics 1 |  |
| [[MPV17]] | 0.411 | mitochondrial inner membrane protein MPV17 |  |
| [[CYP2U1]] | 0.408 | cytochrome P450 family 2 subfamily U member 1 |  |
| [[GIGYF2]] | 0.405 | GRB10 interacting GYF protein 2 |  |
| [[LYRM9]] | 0.400 | LYR motif containing 9 |  |
| [[PCID2]] | 0.393 | PCI domain containing 2 |  |
| [[ZNG1B]] | 0.390 | Zn regulated GTPase metalloprotein activator 1B |  |
| [[ZSWIM7]] | 0.368 | zinc finger SWIM-type containing 7 |  |
| [[MTCH2]] | 0.346 | mitochondrial carrier 2 |  |
| [[FYTTD1]] | 0.286 | forty-two-three domain containing 1 |  |
| [[UBLCP1]] | 0.282 | ubiquitin like domain containing CTD phosphatase 1 |  |
| [[AGAP13P]] | 0.261 | ArfGAP with GTPase domain, ankyrin repeat and PH domain 13, pseudogene |  |
| [[UBE2V2]] | 0.259 | ubiquitin conjugating enzyme E2 V2 |  |
| [[BMS1P1-1]] | 0.209 | — |  |
| [[AGPAT5]] | 0.207 | 1-acylglycerol-3-phosphate O-acyltransferase 5 |  |

## − arm (14)

| Gene | Projection | Name | Alert |
|---|---|---|---|
| [[LMBR1]] | -0.604 | limb development membrane protein 1 |  |
| [[FARP2]] | -0.578 | FERM, ARH/RhoGEF and pleckstrin domain protein 2 |  |
| [[TPTEP2-CSNK1E]] | -0.553 | TPTEP2-CSNK1E readthrough |  |
| [[C1orf216]] | -0.528 | chromosome 1 open reading frame 216 |  |
| [[CD9]] | -0.520 | CD9 molecule |  |
| [[RBM14-RBM4]] | -0.515 | RBM14-RBM4 readthrough |  |
| [[NFATC2IP]] | -0.514 | nuclear factor of activated T cells 2 interacting protein |  |
| [[SDC1]] | -0.508 | syndecan 1 |  |
| [[LIPE-AS1]] | -0.432 | LIPE antisense RNA 1 |  |
| [[NBL1]] | -0.424 | NBL1, DAN family BMP antagonist |  |
| [[ESRRA]] | -0.415 | estrogen related receptor alpha |  |
| [[RFLNB]] | -0.365 | refilin B |  |
| [[BAIAP2-DT]] | -0.290 | BAIAP2 divergent transcript |  |
| [[ECI1]] | -0.273 | enoyl-CoA delta isomerase 1 |  |

## Data

- `graph/nodes.parquet` — module == 28; `graph/modules.parquet` — module == 28; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [27] (drug-dose × line)
