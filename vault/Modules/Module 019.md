---
module: 19
type: "module"
n_genes: 196
n_plus: 196
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.16810032725334167
label: "Neuronal System"
label_source: "reactome"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 019

*Neuronal System · 196 genes (single-armed) · [[Module 019.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

Label from the validation stage: **Neuronal System** (reactome, q 2e-05; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | Neuronal System | reactome | 18/196 | 4.91 | 2e-05 |
| + | Neuronal System | reactome | 18/196 | 4.91 | 2e-05 |
| + | Collagen biosynthesis and modifying enzymes | reactome | 7/196 | 9.13 | 0.005 |
| all | Collagen biosynthesis and modifying enzymes | reactome | 7/196 | 9.13 | 0.005 |
| all | Anchoring fibril formation | reactome | 4/196 | 20.5 | 0.014 |
| + | Anchoring fibril formation | reactome | 4/196 | 20.5 | 0.014 |
| + | Inwardly rectifying K+ channels | reactome | 4/196 | 18.1 | 0.023 |
| all | Inwardly rectifying K+ channels | reactome | 4/196 | 18.1 | 0.023 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 18), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Dinaciclib (drug)]] 0.5 µM (+9.4, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (+9.0, ⚠ toxic; transcription drop; cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (+8.7, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+6.8, ⚠ toxic; transcription drop; cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (+6.4); [[Tucidinostat (drug)]] 0.5 µM (+3.9, ⚠ cell-cycle shift); [[Epirubicin (hydrochloride) (drug)]] 5 µM (+2.7, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 5 µM (+2.5, ⚠ cell-cycle shift); [[Docetaxel (drug)]] 0.05 µM (+2.3, ⚠ transcription drop; cell-cycle shift); [[Lonafarnib (drug)]] 5 µM (+2.2, ⚠ toxic); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+2.2); [[Ipatasertib (drug)]] 0.5 µM (+2.1); [[Auranofin (drug)]] 5 µM (+2.0); [[XRK3F2 (drug)]] 0.5 µM (+1.8); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM (+1.6); [[Docetaxel (Trihydrate) (drug)]] 0.5 µM (+1.5); [[Vitamin K4 (drug)]] 0.05 µM (+1.5); [[GSK1059615 (drug)]] 0.5 µM (+1.5); [[Methylprednisolone succinate (drug)]] 0.5 µM (+1.4) (63 in all, 22 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)
- Lower it: [[Digitoxin (drug)]] 0.5 µM (-2.8, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 0.05 µM (-2.2, ⚠ cell-cycle shift); [[c-Kit-IN-1 (drug)]] 0.05 µM (-1.9, ⚠ unreliable plate only); [[Dexamethasone (drug)]] 0.5 µM (-1.8); [[Lucanthone (drug)]] 0.05 µM (-1.8); [[Harringtonine (drug)]] 0.5 µM (-1.8, ⚠ cell-cycle shift); [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM (-1.7); [[Fenofibrate (drug)]] 0.05 µM (-1.7); [[Mebendazole (drug)]] 5 µM (-1.7); [[Erlotinib (drug)]] 0.05 µM (-1.6); [[Diphenhydramine (drug)]] 0.05 µM (-1.5); [[Artesunate (drug)]] 0.5 µM (-1.5); [[Rutin (trihydrate) (drug)]] 0.05 µM (-1.5); [[(S)-Crizotinib (drug)]] 0.05 µM (-1.4) (61 in all, 11 with an alert ⚠; shown: the 10 strongest and the 4 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[SNU-1 (line)]], [[NCI-H460 (line)]], [[C-33 A (line)]], [[NCI-H23 (line)]], [[A-427 (line)]], [[AN3 CA (line)]], [[SHP-77 (line)]], [[CHP-212 (line)]]

## Candidate new members

*Members not annotated to the set their arm is enriched for, ranked by mean cos to the annotated members (`validation/novel_members.csv`); ⚠ = a reason to doubt the gene's place (in the vector space only through flagged drug-doses), kept in its rank. 13 candidates, none with an alert.*

| # | Gene | Set | Mean cos |
|---|---|---|---|
| 1 | [[LINC01035]] | Neuronal System | +0.55 |
| 2 | [[COL4A6]] | Neuronal System | +0.54 |
| 3 | [[CDH7]] | Neuronal System | +0.53 |
| 4 | [[NCKAP5-AS2]] | Neuronal System | +0.53 |
| 5 | [[ADGRD1]] | Neuronal System | +0.52 |
| 6 | [[GREM2]] | Neuronal System | +0.52 |
| 7 | [[LINC03000]] | Neuronal System | +0.51 |
| 8 | [[CTNND2]] | Neuronal System | +0.51 |
| 9 | [[GLP2R]] | Neuronal System | +0.51 |
| 10 | [[CDH11]] | Neuronal System | +0.51 |
| 11 | [[PDE1C]] | Neuronal System | +0.51 |
| 12 | [[DPP10]] | Neuronal System | +0.51 |
| 13 | [[SLITRK4]] | Collagen biosynthesis and modifying enzymes | +0.50 |

*⚠ 1 of its 196 genes are in the vector space only through drug-doses that carry an alert (`embed/genes.parquet` evidence_flagged_only): their place here may reflect what those drug-doses did to the cells. They are marked in the tables of this note.*

## + arm (196)

| Gene | Projection | Name | Alert |
|---|---|---|---|
| [[LINC01035]] | 0.888 | long independently transcribed non-coding RNA 1035 |  |
| [[COL4A6]] | 0.876 | collagen type IV alpha 6 chain |  |
| [[GLP2R]] | 0.872 | glucagon like peptide 2 receptor |  |
| [[LINC03000]] | 0.865 | long independently transcribed non-coding RNA 3000 |  |
| [[NCKAP5-AS2]] | 0.852 | NCKAP5 antisense RNA 2 |  |
| [[GREM2]] | 0.850 | gremlin 2, DAN family BMP antagonist |  |
| [[KCNK2]] | 0.849 | potassium two pore domain channel subfamily K member 2 |  |
| [[ADGRD1]] | 0.838 | adhesion G protein-coupled receptor D1 |  |
| [[CDH7]] | 0.833 | cadherin 7 |  |
| [[DPP10]] | 0.833 | dipeptidyl peptidase like 10 |  |
| [[CTNND2]] | 0.832 | catenin delta 2 |  |
| [[PAX7]] | 0.828 | paired box 7 |  |
| [[CHL1]] | 0.810 | cell adhesion molecule L1 like |  |
| [[PDE1A]] | 0.810 | phosphodiesterase 1A |  |
| [[SCARA5]] | 0.807 | scavenger receptor class A member 5 |  |
| [[CDH11]] | 0.805 | cadherin 11 |  |
| [[SERPINB11]] | 0.805 | serpin family B member 11 |  |
| [[PDE7B]] | 0.800 | phosphodiesterase 7B |  |
| [[SPDYE10]] | 0.787 | speedy/RINGO cell cycle regulator family member E10 |  |
| [[LIN7A]] | 0.785 | lin-7 cell polarity scaffold A |  |
| [[SLITRK4]] | 0.783 | SLIT and NTRK like family member 4 |  |
| [[TBXT]] | 0.764 | T-box transcription factor T | ⚠ only flagged evidence |
| [[GTF2I-AS1]] | 0.755 | GTF2I antisense RNA 1 |  |
| [[CNTN1]] | 0.748 | contactin 1 |  |
| [[EPB41L3]] | 0.746 | erythrocyte membrane protein band 4.1 like 3 |  |
| [[PDE1C]] | 0.733 | phosphodiesterase 1C |  |
| [[TENM1]] | 0.726 | teneurin transmembrane protein 1 |  |
| [[FENDRR]] | 0.725 | FOXF1 adjacent non-coding developmental regulatory RNA |  |
| [[RHOH]] | 0.725 | ras homolog family member H |  |
| [[RIMS1]] | 0.723 | regulating synaptic membrane exocytosis 1 |  |
| [[GASK1B]] | 0.721 | golgi associated kinase 1B |  |
| [[DOK6]] | 0.713 | docking protein 6 |  |
| [[RAB3C]] | 0.713 | RAB3C, member RAS oncogene family |  |
| [[RTN1]] | 0.713 | reticulon 1 |  |
| [[KCNMB2]] | 0.712 | potassium calcium-activated channel subfamily M regulatory beta subunit 2 |  |
| [[DDIT4L]] | 0.704 | DNA damage inducible transcript 4 like |  |
| [[LAMB4]] | 0.700 | laminin subunit beta 4 |  |
| [[IQCM]] | 0.698 | IQ motif containing M |  |
| [[SLC15A5]] | 0.696 | solute carrier family 15 member 5 |  |
| [[EPGN]] | 0.695 | epithelial mitogen |  |
| [[PAK3]] | 0.695 | p21 (RAC1) activated kinase 3 |  |
| [[LINC00461]] | 0.691 | MIR9-2 host gene |  |
| [[PCDH15]] | 0.691 | protocadherin related 15 |  |
| [[KCNJ6]] | 0.691 | potassium inwardly rectifying channel subfamily J member 6 |  |
| [[SCUBE1]] | 0.691 | signal peptide, CUB domain and EGF like domain containing 1 |  |
| [[P3H2-AS1]] | 0.689 | P3H2 antisense RNA 1 |  |
| [[PALMD]] | 0.682 | palmdelphin |  |
| [[LSAMP]] | 0.681 | limbic system associated membrane protein |  |
| [[COL4A5]] | 0.680 | collagen type IV alpha 5 chain |  |
| [[GPRIN3]] | 0.680 | GPRIN family member 3 |  |
| [[SEMA3D]] | 0.676 | semaphorin 3D |  |
| [[AMDHD1]] | 0.673 | amidohydrolase domain containing 1 |  |
| [[PLAC4]] | 0.673 | placenta associated 4 |  |
| [[SMOC1]] | 0.666 | SPARC related modular calcium binding 1 |  |
| [[PDE4B]] | 0.663 | phosphodiesterase 4B |  |
| [[NCKAP5]] | 0.661 | NCK associated protein 5 |  |
| [[LINC01257]] | 0.660 | long independently transcribed non-coding RNA 1257 |  |
| [[ANO3]] | 0.659 | anoctamin 3 |  |
| [[CDH19]] | 0.658 | cadherin 19 |  |
| [[PRICKLE1]] | 0.655 | prickle planar cell polarity protein 1 |  |
| [[UNC5D]] | 0.654 | unc-5 netrin receptor D |  |
| [[LINC01967]] | 0.652 | long independently transcribed non-coding RNA 1967 |  |
| [[CASC15]] | 0.652 | cancer susceptibility 15 |  |
| [[NKAIN2]] | 0.651 | sodium/potassium transporting ATPase interacting 2 |  |
| [[LINC00824]] | 0.650 | long independently transcribed non-coding RNA 824 |  |
| [[LINC02994]] | 0.642 | long independently transcribed non-coding RNA 2994 |  |
| [[LRRC63]] | 0.642 | leucine rich repeat containing 63 |  |
| [[ST8SIA4]] | 0.639 | ST8 alpha-N-acetyl-neuraminide alpha-2,8-sialyltransferase 4 |  |
| [[NRCAM]] | 0.637 | neuronal cell adhesion molecule |  |
| [[EYA2]] | 0.636 | EYA transcriptional coactivator and phosphatase 2 |  |
| [[LINC01508]] | 0.635 | long independently transcribed non-coding RNA 1508 |  |
| [[GASK1B-AS1]] | 0.634 | GASK1B antisense RNA 1 |  |
| [[SLITRK5]] | 0.631 | SLIT and NTRK like family member 5 |  |
| [[HORMAD1]] | 0.626 | HORMA domain containing 1 |  |
| [[TCF4]] | 0.625 | transcription factor 4 |  |
| [[MEIOB]] | 0.619 | meiosis specific with OB-fold |  |
| [[BMPER]] | 0.617 | BMP binding endothelial regulator |  |
| [[C5orf46]] | 0.613 | chromosome 5 open reading frame 46 |  |
| [[ESM1]] | 0.609 | endothelial cell specific molecule 1 |  |
| [[TRPA1]] | 0.606 | transient receptor potential cation channel subfamily A member 1 |  |
| [[CNKSR2]] | 0.601 | connector enhancer of kinase suppressor of Ras 2 |  |
| [[CPS1]] | 0.600 | carbamoyl-phosphate synthase 1 |  |
| [[STEAP1B-AS1]] | 0.599 | STEAP1B antisense RNA 1 |  |
| [[CPED1]] | 0.598 | cadherin like and PC-esterase domain containing 1 |  |
| [[P3H2]] | 0.598 | prolyl 3-hydroxylase 2 |  |
| [[PDE3A]] | 0.597 | phosphodiesterase 3A |  |
| [[TNFRSF11B]] | 0.596 | TNF receptor superfamily member 11b |  |
| [[CACNA2D3]] | 0.595 | calcium voltage-gated channel auxiliary subunit alpha2delta 3 |  |
| [[SNCA]] | 0.593 | synuclein alpha |  |
| [[GABBR2]] | 0.591 | gamma-aminobutyric acid type B receptor subunit 2 |  |
| [[LINC02864]] | 0.590 | long independently transcribed non-coding RNA 2864 |  |
| [[BCHE]] | 0.590 | butyrylcholinesterase |  |
| [[LGSN]] | 0.589 | lengsin, lens protein with glutamine synthetase domain |  |
| [[IGSF1]] | 0.588 | immunoglobulin superfamily member 1 |  |
| [[SLC16A4]] | 0.583 | solute carrier family 16 member 4 |  |
| [[SERPIND1]] | 0.582 | serpin family D member 1 |  |
| [[SOX6]] | 0.581 | SRY-box transcription factor 6 |  |
| [[HERC2P3-1]] | 0.577 | — |  |
| [[ACSS3]] | 0.577 | acyl-CoA synthetase short chain family member 3 |  |
| [[LINC02742]] | 0.575 | long independently transcribed non-coding RNA 2742 |  |
| [[LINC02945]] | 0.572 | long independently transcribed non-coding RNA 2945 |  |
| [[GSG1L2]] | 0.571 | GSG1 like 2 |  |
| [[WDR72]] | 0.571 | WD repeat domain 72 |  |
| [[F2RL2]] | 0.568 | coagulation factor II thrombin receptor like 2 |  |
| [[NXPH1]] | 0.566 | neurexophilin 1 |  |
| [[NOVA1]] | 0.565 | NOVA alternative splicing regulator 1 |  |
| [[PART1]] | 0.562 | prostate androgen-regulated transcript 1 |  |
| [[BASP1-AS1]] | 0.561 | BASP1 antisense RNA 1 |  |
| [[CLDN16]] | 0.556 | claudin 16 |  |
| [[BDNF]] | 0.555 | brain derived neurotrophic factor |  |
| [[NLGN4Y]] | 0.555 | neuroligin 4 Y-linked |  |
| [[CLDN10-AS1]] | 0.554 | CLDN10 antisense RNA 1 |  |
| [[PAPPA2]] | 0.554 | pappalysin 2 |  |
| [[ABCC9]] | 0.552 | ATP binding cassette subfamily C member 9 |  |
| [[KCNE4]] | 0.552 | potassium voltage-gated channel subfamily E regulatory subunit 4 |  |
| [[ENPEP]] | 0.549 | glutamyl aminopeptidase |  |
| [[GRAMD1B]] | 0.547 | GRAM domain containing 1B |  |
| [[PDE10A]] | 0.544 | phosphodiesterase 10A |  |
| [[COL8A1]] | 0.544 | collagen type VIII alpha 1 chain |  |
| [[NRG1]] | 0.541 | neuregulin 1 |  |
| [[TM4SF18]] | 0.538 | transmembrane 4 L six family member 18 |  |
| [[SLCO1C1]] | 0.538 | solute carrier organic anion transporter family member 1C1 |  |
| [[GTF2IP7]] | 0.535 | general transcription factor IIi pseudogene 7 |  |
| [[QPCT]] | 0.534 | glutaminyl-peptide cyclotransferase |  |
| [[NEXMIF]] | 0.534 | neurite extension and migration factor |  |
| [[STEAP1B]] | 0.531 | STEAP family member 1B |  |
| [[ELOVL2]] | 0.531 | ELOVL fatty acid elongase 2 |  |
| [[P4HA3]] | 0.530 | prolyl 4-hydroxylase subunit alpha 3 |  |
| [[SPINK13]] | 0.528 | serine peptidase inhibitor Kazal type 13 |  |
| [[LMNTD1]] | 0.526 | lamin tail domain containing 1 |  |
| [[RSPO3]] | 0.525 | R-spondin 3 |  |
| [[MARCOL]] | 0.524 | MARCO like |  |
| [[ALDH1A1]] | 0.516 | aldehyde dehydrogenase 1 family member A1 |  |
| [[CAVIN2-AS1]] | 0.516 | CAVIN2 and TMEFF2 antisense RNA 1 |  |
| [[GDA]] | 0.516 | guanine deaminase |  |
| [[CRLF2]] | 0.515 | cytokine receptor like factor 2 |  |
| [[RADIL]] | 0.513 | Rap associating with DIL domain |  |
| [[MN1]] | 0.511 | MN1 proto-oncogene, transcriptional regulator |  |
| [[NRXN3]] | 0.511 | neurexin 3 |  |
| [[MAPK4]] | 0.510 | mitogen-activated protein kinase 4 |  |
| [[SGIP1]] | 0.507 | SH3GL interacting endocytic adaptor 1 |  |
| [[CACNG6]] | 0.507 | calcium voltage-gated channel auxiliary subunit gamma 6 |  |
| [[NEFL]] | 0.506 | neurofilament light chain |  |
| [[LYPLAL1-DT]] | 0.501 | LYPLAL1 divergent transcript |  |
| [[SERPINB2]] | 0.498 | serpin family B member 2 |  |
| [[LINC02269]] | 0.497 | long independently transcribed non-coding RNA 2269 |  |
| [[NRG4]] | 0.484 | neuregulin 4 |  |
| [[RMDN2-AS1]] | 0.484 | RMDN2 antisense RNA 1 |  |
| [[MIR9-3HG]] | 0.483 | MIR9-3 host gene |  |
| [[GLRB]] | 0.482 | glycine receptor beta |  |
| [[ODAD2]] | 0.480 | outer dynein arm docking complex subunit 2 |  |
| [[GNG11]] | 0.472 | G protein subunit gamma 11 |  |
| [[SALL4]] | 0.470 | spalt like transcription factor 4 |  |
| [[GYG2]] | 0.469 | glycogenin 2 |  |
| [[LINC01139]] | 0.469 | long independently transcribed non-coding RNA 1139 |  |
| [[BARX1]] | 0.469 | BARX homeobox 1 |  |
| [[FRMPD4]] | 0.467 | FERM and PDZ domain containing 4 |  |
| [[NEFM]] | 0.465 | neurofilament medium chain |  |
| [[COL4A3]] | 0.464 | collagen type IV alpha 3 chain |  |
| [[GJA1]] | 0.462 | gap junction protein alpha 1 |  |
| [[SLC19A3]] | 0.460 | solute carrier family 19 member 3 |  |
| [[SIRLNT]] | 0.460 | SIRT1 regulating lncRNA tumor promoter |  |
| [[TARID]] | 0.458 | TCF21 antisense RNA inducing promoter demethylation |  |
| [[COL4A4]] | 0.457 | collagen type IV alpha 4 chain |  |
| [[SPP1]] | 0.454 | secreted phosphoprotein 1 |  |
| [[GALNT16]] | 0.451 | polypeptide N-acetylgalactosaminyltransferase 16 |  |
| [[PDE4D]] | 0.450 | phosphodiesterase 4D |  |
| [[CYP1B1]] | 0.446 | cytochrome P450 family 1 subfamily B member 1 |  |
| [[TTTY10]] | 0.442 | testis expressed transcript, Y-linked 10 |  |
| [[SLC4A11]] | 0.436 | solute carrier family 4 member 11 |  |
| [[LINC01684]] | 0.435 | long independently transcribed non-coding RNA 1684 |  |
| [[TBX2]] | 0.430 | T-box transcription factor 2 |  |
| [[EDARADD]] | 0.420 | EDAR associated via death domain |  |
| [[PTPN20]] | 0.419 | protein tyrosine phosphatase non-receptor type 20 |  |
| [[ELMO1]] | 0.415 | engulfment and cell motility 1 |  |
| [[SOX7]] | 0.414 | SRY-box transcription factor 7 |  |
| [[SPANXA2-OT1]] | 0.414 | SPANXA2 overlapping transcript 1 |  |
| [[EDIL3]] | 0.413 | EGF like and discoidin domains 3 |  |
| [[ANO5]] | 0.412 | anoctamin 5 |  |
| [[EBF2]] | 0.403 | EBF transcription factor 2 |  |
| [[TNFRSF19]] | 0.400 | TNF receptor superfamily member 19 |  |
| [[CHSY3]] | 0.395 | chondroitin sulfate synthase 3 |  |
| [[TMEM170B]] | 0.381 | transmembrane protein 170B |  |
| [[GABRE]] | 0.380 | gamma-aminobutyric acid type A receptor subunit epsilon |  |
| [[LINC03046]] | 0.371 | long independently transcribed non-coding RNA 3046 |  |
| [[PRSS23-AS1]] | 0.358 | PRSS23 antisense RNA 1 |  |
| [[KIAA0319]] | 0.357 | KIAA0319 |  |
| [[RDH10]] | 0.347 | retinol dehydrogenase 10 |  |
| [[RAB27B]] | 0.334 | RAB27B, member RAS oncogene family |  |
| [[SLC2A10]] | -0.292 | solute carrier family 2 member 10 |  |
| [[LINC00482]] | 0.280 | long independently transcribed non-coding RNA 482 |  |
| [[HGF]] | 0.278 | hepatocyte growth factor |  |
| [[UPK1B]] | 0.277 | uroplakin 1B |  |
| [[LIMK2]] | 0.260 | LIM domain kinase 2 |  |
| [[CYP24A1]] | 0.252 | cytochrome P450 family 24 subfamily A member 1 |  |
| [[ADGRF5]] | 0.218 | adhesion G protein-coupled receptor F5 |  |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 19; `graph/modules.parquet` — module == 19; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [18] (drug-dose × line)
