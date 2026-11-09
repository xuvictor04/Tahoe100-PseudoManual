---
module: 30
type: "module"
n_genes: 146
n_plus: 134
n_minus: 12
arms_opposite: true
mean_cos_between_arms: -0.36518365144729614
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 030

*146 genes (134 in the + arm, 12 in the − arm) · [[Module 030.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37). The + arm rises where the − arm falls. Arm = the side of the module's main direction a gene sits on.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of the + arm minus the − arm (`graph/module_pooled_z.npy`, row 29), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it (+ arm up, − arm down): [[Panobinostat (drug)]] 0.5 µM (+11.6, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (+10.9, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (+10.0, ⚠ cell-cycle shift); [[Ixazomib citrate (drug)]] 5 µM (+5.7, ⚠ cell-cycle shift); [[Radotinib (drug)]] 5 µM (+5.4); [[Selinexor (drug)]] 5 µM (+4.8, ⚠ cell-cycle shift); [[Topotecan (hydrochloride) (drug)]] 5 µM (+4.7, ⚠ toxic; cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (+4.3, ⚠ cell-cycle shift); [[Bortezomib (drug)]] 0.05 µM (+4.2, ⚠ cell-cycle shift); [[Belinostat (drug)]] 0.5 µM (+4.0, ⚠ cell-cycle shift); [[Ixazomib citrate (drug)]] 0.5 µM (+3.6); [[Ponatinib (drug)]] 5 µM (+3.4); [[Brivudine (drug)]] 5 µM (+3.3); [[Ipatasertib (drug)]] 0.5 µM (+2.8); [[Flumatinib (mesylate) (drug)]] 5 µM (+2.7); [[Vinblastine (sulfate) (drug)]] 5 µM (+2.4); [[Osimertinib (mesylate) (drug)]] 5 µM (+2.4); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM (+2.4); [[Bortezomib (drug)]] 0.5 µM (+2.3) (116 in all, 25 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)
- Lower it: [[Homoharringtonine (drug)]] 5 µM (-23.4, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-13.1, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-13.0, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (-10.4, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (-7.7, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (-7.3, ⚠ cell-cycle shift); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (-6.3); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (-6.1, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (-6.0, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 0.5 µM (-5.9, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.05 µM (-3.2); [[Auranofin (drug)]] 5 µM (-3.0); [[Filgotinib (drug)]] 5 µM (-3.0); [[TAK-901 (drug)]] 0.05 µM (-2.9); [[Demeclocycline (drug)]] 5 µM (-2.7); [[Esmolol (hydrochloride) (drug)]] 5 µM (-2.6); [[Busulfan (drug)]] 0.05 µM (-2.6); [[BAY1125976 (drug)]] 5 µM (-2.5); [[Diphenhydramine (drug)]] 0.5 µM (-2.4) (121 in all, 25 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[NCI-H460 (line)]], [[HOP62 (line)]], [[PANC-1 (line)]], [[NCI-H2347 (line)]], [[SW480 (line)]], [[MIA PaCa-2 (line)]], [[LOX-IMVI (line)]], [[A-172 (line)]]

## + arm (134)

| Gene | Projection | Name |
|---|---|---|
| [[UNC45A]] | 0.859 | unc-45 myosin chaperone A |
| [[SLC9A6]] | 0.835 | solute carrier family 9 member A6 |
| [[CRYZL1]] | 0.829 | crystallin zeta like 1 |
| [[MYPOP]] | 0.822 | Myb related transcription factor, partner of profilin |
| [[MGST3]] | 0.795 | microsomal glutathione S-transferase 3 |
| [[MKRN2]] | 0.791 | makorin ring finger protein 2 |
| [[TMEM185A]] | 0.789 | transmembrane protein 185A |
| [[NBPF3]] | 0.780 | NBPF member 3 |
| [[STX7]] | 0.779 | syntaxin 7 |
| [[DPY30]] | 0.771 | dpy-30 histone methyltransferase complex regulatory subunit |
| [[NFRKB]] | 0.769 | nuclear factor related to kappaB binding protein |
| [[CCZ1B]] | 0.768 | CCZ1B vacuolar protein trafficking and biogenesis associated |
| [[PLD3]] | 0.765 | phospholipase D family member 3 |
| [[HSDL1]] | 0.762 | hydroxysteroid dehydrogenase like 1 |
| [[SCAI]] | 0.757 | suppressor of cancer cell invasion |
| [[MMS19]] | 0.754 | MMS19 cytosolic iron-sulfur assembly component |
| [[OSBPL7]] | 0.751 | oxysterol binding protein like 7 |
| [[INPP5B]] | 0.748 | inositol polyphosphate-5-phosphatase B |
| [[PRUNE1]] | 0.748 | prune exopolyphosphatase 1 |
| [[CCZ1]] | 0.747 | CCZ1 vacuolar protein trafficking and biogenesis associated |
| [[SNTA1]] | 0.744 | syntrophin alpha 1 |
| [[PHAF1]] | 0.739 | phagophore assembly factor 1 |
| [[ABCD4]] | 0.737 | ATP binding cassette subfamily D member 4 |
| [[MRI1]] | 0.736 | methylthioribose-1-phosphate isomerase 1 |
| [[NTAN1]] | 0.733 | N-terminal asparagine amidase |
| [[PCTP]] | 0.731 | phosphatidylcholine transfer protein |
| [[FLYWCH1]] | 0.730 | FLYWCH-type zinc finger 1 |
| [[ZFP14]] | 0.730 | ZFP14 zinc finger protein |
| [[GET1]] | 0.729 | guided entry of tail-anchored proteins factor 1 |
| [[KLHDC10]] | 0.727 | kelch domain containing 10 |
| [[PSMD9]] | 0.726 | proteasome 26S subunit, non-ATPase 9 |
| [[FLYWCH2]] | 0.722 | FLYWCH family member 2 |
| [[ECI2]] | 0.722 | enoyl-CoA delta isomerase 2 |
| [[ATPAF2]] | 0.721 | ATP synthase mitochondrial F1 complex assembly factor 2 |
| [[SUFU]] | 0.720 | SUFU negative regulator of hedgehog signaling |
| [[NDUFAF7]] | 0.718 | NADH:ubiquinone oxidoreductase complex assembly factor 7 |
| [[PLD2]] | 0.718 | phospholipase D2 |
| [[USP35]] | 0.714 | ubiquitin specific peptidase 35 |
| [[CDK5RAP1]] | 0.712 | CDK5RAP1 mitochondrial tRNA methylthiotransferase |
| [[RNF41]] | 0.709 | ring finger protein 41 |
| [[TSC2]] | 0.705 | TSC complex subunit 2 |
| [[VPS37D]] | 0.702 | VPS37D subunit of ESCRT-I |
| [[E4F1]] | 0.695 | E4F transcription factor 1 |
| [[MFSD9]] | 0.690 | solute carrier family 67 member 2 |
| [[DHRS1]] | 0.687 | dehydrogenase/reductase 1 |
| [[ANKMY2]] | 0.686 | ankyrin repeat and MYND domain containing 2 |
| [[TBCB]] | 0.684 | tubulin folding cofactor B |
| [[SLC15A4]] | 0.683 | solute carrier family 15 member 4 |
| [[SHARPIN]] | 0.683 | SHANK associated RH domain interactor |
| [[CNEP1R1]] | 0.681 | CTD nuclear envelope phosphatase 1 regulatory subunit 1 |
| [[IFT52]] | 0.676 | intraflagellar transport 52 |
| [[RAB18]] | 0.676 | RAB18, member RAS oncogene family |
| [[RNF216P1]] | 0.674 | ring finger protein 216 pseudogene 1 |
| [[XKR8]] | 0.673 | XK related 8 |
| [[ZNF552]] | 0.673 | zinc finger protein 552 |
| [[STAM]] | 0.670 | signal transducing adaptor molecule |
| [[POMGNT2]] | 0.670 | protein O-linked mannose N-acetylglucosaminyltransferase 2 (beta 1,4-) |
| [[MAP4K2]] | 0.669 | mitogen-activated protein kinase kinase kinase kinase 2 |
| [[GTF2H2B]] | 0.668 | general transcription factor IIH subunit 2B (pseudogene) |
| [[FAM104A]] | 0.663 | VCP nuclear cofactor family member 1 |
| [[IQSEC2]] | 0.661 | IQ motif and Sec7 domain ArfGEF 2 |
| [[RECK]] | 0.653 | reversion inducing cysteine rich protein with kazal motifs |
| [[CC2D1A]] | 0.653 | coiled-coil and C2 domain containing 1A |
| [[OTX1]] | 0.652 | orthodenticle homeobox 1 |
| [[BAG4]] | 0.650 | BAG cochaperone 4 |
| [[RHOT1]] | 0.645 | ras homolog family member T1 |
| [[CDADC1]] | 0.643 | cytidine and dCMP deaminase domain containing 1 |
| [[RUFY2]] | 0.634 | RUN and FYVE domain containing 2 |
| [[NMRAL1]] | 0.632 | NmrA like redox sensor 1 |
| [[TBCE]] | 0.630 | tubulin folding cofactor E |
| [[TMUB1]] | 0.630 | transmembrane and ubiquitin like domain containing 1 |
| [[FHIP1B]] | 0.629 | FHF complex subunit HOOK interacting protein 1B |
| [[UNC119]] | 0.623 | unc-119 lipid binding chaperone |
| [[ZNF667-AS1]] | 0.620 | ZNF667 antisense RNA 1 |
| [[PKN1]] | 0.618 | protein kinase N1 |
| [[GIT2]] | 0.618 | GIT ArfGAP 2 |
| [[ADCK2]] | 0.617 | aarF domain containing kinase 2 |
| [[KIAA2013]] | 0.615 | KIAA2013 |
| [[HTT]] | 0.615 | huntingtin |
| [[MAPK3]] | 0.614 | mitogen-activated protein kinase 3 |
| [[MRGBP]] | 0.612 | MRG domain binding protein |
| [[TMEM219]] | 0.607 | transmembrane protein 219 |
| [[NBPF1]] | 0.605 | NBPF member 1 |
| [[GRB2]] | 0.603 | growth factor receptor bound protein 2 |
| [[SNRNP48]] | 0.594 | small nuclear ribonucleoprotein U11/U12 subunit 48 |
| [[ASAP3]] | 0.585 | ArfGAP with SH3 domain, ankyrin repeat and PH domain 3 |
| [[PRKAB2]] | 0.585 | protein kinase AMP-activated non-catalytic subunit beta 2 |
| [[GDPD3]] | 0.584 | glycerophosphodiester phosphodiesterase domain containing 3 |
| [[MIR29B2CHG]] | 0.584 | MIR29B2 and MIR29C host gene |
| [[RWDD1]] | 0.583 | RWD domain containing 1 |
| [[ACSF2]] | 0.579 | acyl-CoA synthetase family member 2 |
| [[OTULIN]] | 0.575 | OTU deubiquitinase with linear linkage specificity |
| [[ABHD8]] | 0.572 | abhydrolase domain containing 8 |
| [[HYKK]] | 0.571 | hydroxylysine kinase |
| [[MRPS5]] | 0.571 | mitochondrial ribosomal protein S5 |
| [[CALCOCO2]] | 0.568 | calcium binding and coiled-coil domain 2 |
| [[SLC22A18]] | 0.565 | solute carrier family 67 member 1 |
| [[CAPN5]] | 0.565 | calpain 5 |
| [[PPT2]] | 0.564 | palmitoyl-protein thioesterase 2 |
| [[TRAF6]] | 0.551 | TNF receptor associated factor 6 |
| [[GALNT11]] | 0.539 | polypeptide N-acetylgalactosaminyltransferase 11 |
| [[PIKFYVE]] | 0.533 | phosphoinositide kinase, FYVE-type zinc finger containing |
| [[WDFY1]] | 0.524 | WD repeat and FYVE domain containing 1 |
| [[PSMF1]] | 0.523 | proteasome inhibitor subunit 1 |
| [[ZNF567-DT]] | 0.522 | ZNF567 divergent transcript |
| [[MBOAT2]] | 0.519 | membrane bound glycerophospholipid O-acyltransferase 2 |
| [[BCAS4]] | 0.518 | breast carcinoma amplified sequence 4 |
| [[ZNF174]] | 0.510 | zinc finger protein 174 |
| [[SLC66A3]] | 0.509 | solute carrier family 66 member 3 |
| [[ZFYVE19]] | 0.509 | zinc finger FYVE-type containing 19 |
| [[DDRGK1]] | 0.497 | DDRGK domain containing 1 |
| [[TTLL7]] | 0.495 | tubulin tyrosine ligase like 7 |
| [[ZNF341]] | 0.483 | zinc finger protein 341 |
| [[FBXL2]] | 0.479 | F-box and leucine rich repeat protein 2 |
| [[VAT1]] | 0.479 | vesicle amine transport 1 |
| [[COQ4]] | 0.478 | coenzyme Q4 |
| [[ERGIC3]] | 0.476 | ERGIC and golgi 3 |
| [[STARD9]] | 0.461 | StAR related lipid transfer domain containing 9 |
| [[GINM1]] | 0.457 | glycosylated integral membrane protein 1 |
| [[LINC03006-1]] | 0.451 | long independently transcribed non-coding RNA 3006 |
| [[NUDT2]] | 0.445 | nudix hydrolase 2 |
| [[DNAJC24]] | 0.442 | DnaJ heat shock protein family (Hsp40) member C24 |
| [[ANKRD54]] | 0.434 | ankyrin repeat domain 54 |
| [[B4GAT1]] | 0.430 | beta-1,4-glucuronyltransferase 1 |
| [[SH3BP5]] | 0.430 | SH3 domain binding protein 5 |
| [[KCTD2]] | 0.404 | potassium channel tetramerization domain containing 2 |
| [[IL17RD]] | 0.395 | interleukin 17 receptor D |
| [[SLC25A20]] | 0.394 | solute carrier family 25 member 20 |
| [[RGPD8]] | 0.384 | RANBP2 like and GRIP domain containing 8 |
| [[TUBGCP2]] | 0.353 | tubulin gamma complex component 2 |
| [[ARL8B]] | 0.348 | ARF like GTPase 8B |
| [[GPX8]] | 0.333 | glutathione peroxidase 8 (putative) |
| [[VCPKMT]] | 0.254 | valosin containing protein lysine methyltransferase |
| [[WASF1]] | 0.150 | WASP family member 1 |

## − arm (12)

| Gene | Projection | Name |
|---|---|---|
| [[ERCC6L2]] | -0.799 | ERCC excision repair 6 like 2 |
| [[MSRA]] | -0.745 | methionine sulfoxide reductase A |
| [[SKIL]] | -0.705 | SKI like proto-oncogene |
| [[KDSR]] | -0.634 | 3-ketodihydrosphingosine reductase |
| [[ALG13]] | -0.629 | ALG13 UDP-N-acetylglucosaminyltransferase subunit |
| [[ASXL2]] | -0.625 | ASXL transcriptional regulator 2 |
| [[RFX3]] | -0.594 | regulatory factor X3 |
| [[CHD4]] | -0.565 | chromodomain helicase DNA binding protein 4 |
| [[NSUN6]] | -0.554 | NOP2/Sun RNA methyltransferase 6 |
| [[IGF2BP3]] | -0.522 | insulin like growth factor 2 mRNA binding protein 3 |
| [[SLC20A2]] | -0.500 | solute carrier family 20 member 2 |
| [[ZCCHC14]] | -0.361 | zinc finger CCHC-type containing 14 |

## Data

- `graph/nodes.parquet` — module == 30; `graph/modules.parquet` — module == 30; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [29] (drug-dose × line)
