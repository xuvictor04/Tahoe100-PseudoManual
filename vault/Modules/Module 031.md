---
module: 31
type: "module"
n_genes: 141
n_plus: 141
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.2232540249824524
label: "Formation of the cornified envelope"
label_source: "reactome"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 031

*Formation of the cornified envelope · 141 genes (single-armed) · [[Module 031.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

Label from the validation stage: **Formation of the cornified envelope** (reactome, q 8e-08; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | Formation of the cornified envelope | reactome | 9/141 | 24.7 | 8e-08 |
| all | Keratinization | reactome | 9/141 | 24.7 | 8e-08 |
| + | Keratinization | reactome | 9/141 | 24.7 | 8e-08 |
| + | Formation of the cornified envelope | reactome | 9/141 | 24.7 | 8e-08 |
| + | RHO GTPase cycle | reactome | 15/141 | 3.78 | 0.005 |
| all | RHO GTPase cycle | reactome | 15/141 | 3.78 | 0.005 |
| all | Tight junction interactions | reactome | 4/141 | 22.5 | 0.011 |
| + | Tight junction interactions | reactome | 4/141 | 22.5 | 0.011 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 30), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Tucidinostat (drug)]] 5 µM (+3.6); [[Dinaciclib (drug)]] 0.5 µM (+3.2, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (+3.2, ⚠ toxic; transcription drop; cell-cycle shift); [[Tucidinostat (drug)]] 0.5 µM (+2.5, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+2.4, ⚠ toxic; transcription drop; cell-cycle shift); [[Ipatasertib (drug)]] 0.5 µM (+1.9); [[Pitavastatin (Calcium) (drug)]] 0.5 µM (+1.8); [[Pitavastatin (Calcium) (drug)]] 5 µM (+1.5, ⚠ cell-cycle shift); [[LY-2584702 (tosylate salt) (drug)]] 5 µM (+1.4, ⚠ toxic); [[PF-06260933 (drug)]] 5 µM (+1.4); [[9-ING-41 (drug)]] 0.5 µM (+1.2); [[vincristine (drug)]] 0.5 µM (+1.2); [[Thymol (drug)]] 0.5 µM (+1.1); [[Entrectinib (drug)]] 5 µM (+1.1); [[Infigratinib (drug)]] 0.05 µM (+1.0); [[Celecoxib (drug)]] 0.5 µM (+1.0) (20 in all, 8 with an alert ⚠; shown: the 10 strongest and the 6 next strongest without an alert)
- Lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM (-4.0, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-3.5, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (-3.2, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (-3.1, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 0.5 µM (-3.1, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 5 µM (-3.0, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-2.9, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (-2.8, ⚠ cell-cycle shift); [[c-Kit-IN-1 (drug)]] 0.05 µM (-2.5, ⚠ unreliable plate only); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (-2.2, ⚠ cell-cycle shift); [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM (-2.2); [[PH-797804 (drug)]] 5 µM (-1.8); [[TAK-733 (drug)]] 5 µM (-1.7); [[Abemaciclib (drug)]] 5 µM (-1.3); [[Anethole trithione (drug)]] 0.5 µM (-1.2); [[Trametinib (drug)]] 0.05 µM (-1.2); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM (-1.2); [[Binimetinib (drug)]] 0.5 µM (-1.1); [[c-Kit-IN-1 (drug)]] 5 µM (-1.1); [[Erlotinib (drug)]] 0.05 µM (-1.1) (39 in all, 23 with an alert ⚠; shown: the 10 strongest and the 10 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[LoVo (line)]], [[LS 180 (line)]], [[SW480 (line)]], [[CFPAC-1 (line)]], [[KATO III (line)]], [[COLO 205 (line)]], [[NCI-H1573 (line)]], [[HT-29 (line)]]

## Candidate new members

*Members not annotated to the set their arm is enriched for, ranked by mean cos to the annotated members (`validation/novel_members.csv`); ⚠ = a reason to doubt the gene's place (in the vector space only through flagged drug-doses), kept in its rank. 1 candidates, none with an alert.*

| # | Gene | Set | Mean cos |
|---|---|---|---|
| 1 | [[SEMA3B]] | Formation of the cornified envelope | +0.51 |

## + arm (141)

| Gene | Projection | Name |
|---|---|---|
| [[CRYBG2]] | 0.888 | crystallin beta-gamma domain containing 2 |
| [[TMPRSS4]] | 0.878 | transmembrane serine protease 4 |
| [[B3GNT3]] | 0.848 | UDP-GlcNAc:betaGal beta-1,3-N-acetylglucosaminyltransferase 3 |
| [[TMC6]] | 0.842 | transmembrane channel like 6 |
| [[EPS8L1]] | 0.826 | EPS8 signaling adaptor L1 |
| [[HS3ST1]] | 0.822 | heparan sulfate-glucosamine 3-sulfotransferase 1 |
| [[C1orf116]] | 0.815 | chromosome 1 open reading frame 116 |
| [[JUP]] | 0.791 | junction plakoglobin |
| [[RDH13]] | 0.784 | retinol dehydrogenase 13 |
| [[SEMA3B]] | 0.783 | semaphorin 3B |
| [[KIAA0040]] | 0.768 | KIAA0040 |
| [[FA2H]] | 0.767 | fatty acid 2-hydroxylase |
| [[ITGB4]] | 0.759 | integrin subunit beta 4 |
| [[PADI1]] | 0.750 | peptidyl arginine deiminase 1 |
| [[MST1R]] | 0.747 | macrophage stimulating 1 receptor |
| [[PTK6]] | 0.744 | protein tyrosine kinase 6 |
| [[PCDH1]] | 0.740 | protocadherin 1 |
| [[CDH1]] | 0.738 | cadherin 1 |
| [[SDR16C5]] | 0.737 | short chain dehydrogenase/reductase family 16C member 5 |
| [[CLDN4]] | 0.733 | claudin 4 |
| [[SULT2B1]] | 0.730 | sulfotransferase family 2B member 1 |
| [[ARHGAP27]] | 0.726 | Rho GTPase activating protein 27 |
| [[LIPH]] | 0.726 | lipase H |
| [[TTC9]] | 0.723 | tetratricopeptide repeat domain 9 |
| [[GPR35]] | 0.722 | G protein-coupled receptor 35 |
| [[FAM83E]] | 0.720 | scaffolding CK1 anchoring protein E |
| [[CEACAM1]] | 0.719 | CEA cell adhesion molecule 1 |
| [[LEMD1]] | 0.711 | LEM domain containing 1 |
| [[SDCBP2]] | 0.705 | syndecan binding protein 2 |
| [[ARHGEF16]] | 0.701 | Rho guanine nucleotide exchange factor 16 |
| [[ONECUT3]] | 0.689 | one cut homeobox 3 |
| [[ARHGEF34P]] | 0.685 | Rho guanine nucleotide exchange factor 34, pseudogene |
| [[CAPN8]] | 0.682 | calpain 8 |
| [[LCK]] | 0.675 | LCK proto-oncogene, Src family tyrosine kinase |
| [[TJP2]] | 0.675 | tight junction protein 2 |
| [[P2RY2]] | 0.666 | purinergic receptor P2Y2 |
| [[BLACAT1]] | 0.664 | BLACAT1 overlapping LEMD1 locus |
| [[TNS4]] | 0.658 | tensin 4 |
| [[TLDC2]] | 0.658 | TBC/LysM-associated domain containing 2 |
| [[KRT19]] | 0.656 | keratin 19 |
| [[EPHA1]] | 0.655 | EPH receptor A1 |
| [[CBLC]] | 0.652 | Cbl proto-oncogene C |
| [[ANO1]] | 0.647 | anoctamin 1 |
| [[ALS2CL]] | 0.647 | ALS2 C-terminal like |
| [[B4GALNT3]] | 0.643 | beta-1,4-N-acetyl-galactosaminyltransferase 3 |
| [[IQANK1]] | 0.640 | IQ motif and ankyrin repeat containing 1 |
| [[ARHGEF5]] | 0.639 | Rho guanine nucleotide exchange factor 5 |
| [[GPRC5A]] | 0.637 | G protein-coupled receptor class C group 5 member A |
| [[ABHD11]] | 0.633 | abhydrolase domain containing 11 |
| [[MISP]] | 0.627 | mitotic spindle positioning |
| [[PTK2B]] | 0.627 | protein tyrosine kinase 2 beta |
| [[AMN]] | 0.627 | amnion associated transmembrane protein |
| [[IGSF9]] | 0.621 | immunoglobulin superfamily member 9 |
| [[ACOT11]] | 0.620 | acyl-CoA thioesterase 11 |
| [[CLDN7]] | 0.614 | claudin 7 |
| [[UNC5A]] | 0.614 | unc-5 netrin receptor A |
| [[EZR]] | 0.613 | ezrin |
| [[MYO5B]] | 0.604 | myosin VB |
| [[LASTR]] | 0.603 | lncRNA associated with SART3 regulation of splicing |
| [[UNC13D]] | 0.603 | unc-13 homolog D |
| [[CORO2A]] | 0.592 | coronin 2A |
| [[EFNB1]] | 0.590 | ephrin B1 |
| [[PDE9A]] | 0.589 | phosphodiesterase 9A |
| [[IL1RN]] | 0.588 | interleukin 1 receptor antagonist |
| [[MYRF]] | 0.584 | myelin regulatory factor |
| [[TICAM1]] | 0.582 | TIR domain containing adaptor molecule 1 |
| [[KCNK1]] | 0.575 | potassium two pore domain channel subfamily K member 1 |
| [[FAM83B]] | 0.574 | scaffolding CK1 anchoring protein B |
| [[MYO1D]] | 0.573 | myosin ID |
| [[ANXA11]] | 0.572 | annexin A11 |
| [[CAPG]] | 0.568 | capping actin protein, gelsolin like |
| [[ELMO3]] | 0.567 | engulfment and cell motility 3 |
| [[KRT18]] | 0.566 | keratin 18 |
| [[EPB41L1]] | 0.565 | erythrocyte membrane protein band 4.1 like 1 |
| [[PRSS8]] | 0.563 | serine protease 8 |
| [[BICDL2]] | 0.559 | BICD family like cargo adaptor 2 |
| [[GALNT3]] | 0.559 | polypeptide N-acetylgalactosaminyltransferase 3 |
| [[PLCD3]] | 0.549 | phospholipase C delta 3 |
| [[OXSR1]] | 0.547 | oxidative stress responsive kinase 1 |
| [[ARHGEF3]] | 0.541 | Rho guanine nucleotide exchange factor 3 |
| [[LMO7]] | 0.536 | LIM domain 7 |
| [[ITPKC]] | 0.533 | inositol-trisphosphate 3-kinase C |
| [[ADAP1]] | 0.533 | ArfGAP with dual PH domains 1 |
| [[KRT8]] | 0.533 | keratin 8 |
| [[ZNF860]] | 0.529 | zinc finger protein 860 |
| [[TRIP10]] | 0.528 | thyroid hormone receptor interactor 10 |
| [[PSD4]] | 0.523 | pleckstrin and Sec7 domain containing 4 |
| [[PPARG]] | 0.523 | peroxisome proliferator activated receptor gamma |
| [[VSIR]] | 0.522 | V-set immunoregulatory receptor |
| [[PROSER2]] | 0.520 | proline and serine rich 2 |
| [[PKP3]] | 0.519 | plakophilin 3 |
| [[KIAA1522]] | 0.518 | NHS like 3 |
| [[UBE2H]] | 0.517 | ubiquitin conjugating enzyme E2 H |
| [[KLF5]] | 0.512 | KLF transcription factor 5 |
| [[MOGAT3]] | 0.507 | monoacylglycerol O-acyltransferase 3 |
| [[DEF6]] | 0.505 | DEF6 guanine nucleotide exchange factor |
| [[PSORS1C1]] | 0.502 | psoriasis susceptibility 1 candidate 1 |
| [[PARD6B]] | 0.500 | par-6 family cell polarity regulator beta |
| [[ABCC3]] | 0.500 | ATP binding cassette subfamily C member 3 |
| [[MYORG]] | 0.488 | myogenesis regulating glycosidase |
| [[DTX2]] | 0.487 | deltex E3 ubiquitin ligase 2 |
| [[ATP2C2]] | 0.487 | ATPase secretory pathway Ca2+ transporting 2 |
| [[UBXN11]] | 0.479 | UBX domain protein 11 |
| [[TSC22D2]] | 0.479 | TSC22 domain family member 2 |
| [[B3GNT2]] | 0.475 | UDP-GlcNAc:betaGal beta-1,3-N-acetylglucosaminyltransferase 2 |
| [[CD55]] | 0.468 | CD55 molecule (Cromer blood group) |
| [[FBLIM1]] | 0.462 | filamin binding LIM protein 1 |
| [[FAM83A]] | 0.457 | scaffolding CK1 anchoring protein A |
| [[NET1]] | 0.454 | neuroepithelial cell transforming 1 |
| [[S100A14]] | 0.454 | S100 calcium binding protein A14 |
| [[KLF3]] | 0.451 | KLF transcription factor 3 |
| [[KRT16]] | 0.447 | keratin 16 |
| [[PIM1]] | 0.444 | Pim-1 proto-oncogene, serine/threonine kinase |
| [[NOXA1]] | 0.441 | NADPH oxidase activator 1 |
| [[ZBED2]] | 0.439 | zinc finger BED-type containing 2 |
| [[IFNLR1]] | 0.438 | interferon lambda receptor 1 |
| [[KPNA7]] | 0.438 | karyopherin subunit alpha 7 |
| [[SYNE3]] | 0.429 | spectrin repeat containing nuclear envelope family member 3 |
| [[EPS8L2]] | 0.425 | EPS8 signaling adaptor L2 |
| [[IRF6]] | 0.424 | interferon regulatory factor 6 |
| [[S100P]] | 0.422 | S100 calcium binding protein P |
| [[STK24]] | 0.420 | serine/threonine kinase 24 |
| [[RPH3AL]] | 0.419 | rabphilin 3A like (without C2 domains) |
| [[CCDC120]] | 0.413 | coiled-coil domain containing 120 |
| [[ST3GAL3]] | -0.413 | ST3 beta-galactoside alpha-2,3-sialyltransferase 3 |
| [[ITPK1]] | 0.407 | inositol-tetrakisphosphate 1-kinase |
| [[SLC16A5]] | 0.401 | solute carrier family 16 member 5 |
| [[TMBIM1]] | 0.401 | transmembrane BAX inhibitor motif containing 1 |
| [[MYO18A]] | 0.401 | myosin XVIIIA |
| [[USP53]] | 0.380 | ubiquitin specific peptidase 53 |
| [[PATJ]] | 0.380 | PATJ crumbs cell polarity complex component |
| [[DZIP1L]] | -0.379 | DAZ interacting zinc finger protein 1 like |
| [[DSC2]] | 0.367 | desmocollin 2 |
| [[KRT14]] | 0.362 | keratin 14 |
| [[PRXL2B]] | 0.356 | peroxiredoxin like 2B |
| [[LPAR2]] | 0.332 | lysophosphatidic acid receptor 2 |
| [[ESRP2]] | 0.322 | epithelial splicing regulatory protein 2 |
| [[COQ8B]] | 0.307 | coenzyme Q8B |
| [[MAP7]] | 0.285 | microtubule associated protein 7 |
| [[XIST]] | 0.268 | X inactive specific transcript |
| [[LINC01169]] | 0.243 | long independently transcribed non-coding RNA 1169 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 31; `graph/modules.parquet` — module == 31; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [30] (drug-dose × line)
