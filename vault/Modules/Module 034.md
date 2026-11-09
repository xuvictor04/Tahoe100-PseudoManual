---
module: 34
type: "module"
n_genes: 137
n_plus: 137
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.23988479375839233
label: "Type I hemidesmosome assembly"
label_source: "reactome"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 034

*Type I hemidesmosome assembly · 137 genes (single-armed) · [[Module 034.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

Label from the validation stage: **Type I hemidesmosome assembly** (reactome, q 0.041; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | Signaling by GPCR | reactome | 12/137 | 3.81 | 0.029 |
| + | Signaling by GPCR | reactome | 12/137 | 3.81 | 0.029 |
| all | Type I hemidesmosome assembly | reactome | 3/137 | 30.0 | 0.041 |
| + | Type I hemidesmosome assembly | reactome | 3/137 | 30.0 | 0.041 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 33), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Tucidinostat (drug)]] 5 µM (+4.8); [[Tucidinostat (drug)]] 0.5 µM (+3.0, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (+2.4, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (+1.7, ⚠ toxic; transcription drop; cell-cycle shift); [[Pitavastatin (Calcium) (drug)]] 0.5 µM (+1.7); [[PF-06260933 (drug)]] 5 µM (+1.6); [[Panobinostat (drug)]] 0.05 µM (+1.6, ⚠ cell-cycle shift); [[Daptomycin (drug)]] 5 µM (+1.5, ⚠ unreliable plate only); [[Dinaciclib (drug)]] 0.05 µM (+1.3, ⚠ toxic; transcription drop; cell-cycle shift); [[Daptomycin (drug)]] 0.5 µM (+1.2, ⚠ unreliable plate only); [[Peretinoin (drug)]] 5 µM (+1.2); [[Ipatasertib (drug)]] 0.5 µM (+1.2); [[vincristine (drug)]] 0.5 µM (+1.2); [[vincristine (drug)]] 5 µM (+1.1); [[Vilanterol (drug)]] 0.5 µM (+1.0); [[Vilanterol (drug)]] 0.05 µM (+1.0) (18 in all, 9 with an alert ⚠; shown: the 10 strongest and the 6 next strongest without an alert)
- Lower it: [[Homoharringtonine (drug)]] 5 µM (-3.6, ⚠ cell-cycle shift); [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM (-3.1); [[Trametinib (drug)]] 5 µM (-3.1, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-3.1, ⚠ cell-cycle shift); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM (-2.9); [[Binimetinib (drug)]] 0.5 µM (-2.8); [[Trametinib (drug)]] 0.5 µM (-2.8); [[Ouabain (Octahydrate) (drug)]] 5 µM (-2.7, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-2.5, ⚠ cell-cycle shift); [[Binimetinib (drug)]] 5 µM (-2.4); [[Trametinib (drug)]] 0.05 µM (-2.3); [[Binimetinib (drug)]] 0.05 µM (-2.3); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM (-2.3); [[Cobimetinib (drug)]] 5 µM (-2.1); [[Elimusertib hydrochloride (drug)]] 0.05 µM (-1.9) (47 in all, 15 with an alert ⚠; shown: the 10 strongest and the 5 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[AsPC-1 (line)]], [[SW480 (line)]], [[LoVo (line)]], [[CFPAC-1 (line)]], [[NCI-H1573 (line)]], [[LS 180 (line)]], [[NCI-H460 (line)]], [[Hs 766T (line)]]

## + arm (137)

| Gene | Projection | Name |
|---|---|---|
| [[PLEK2]] | 0.903 | pleckstrin 2 |
| [[LAMC2]] | 0.818 | laminin subunit gamma 2 |
| [[S100A16]] | 0.818 | S100 calcium binding protein A16 |
| [[CDCP1]] | 0.810 | CUB domain containing protein 1 |
| [[WNT7B]] | 0.809 | Wnt family member 7B |
| [[LYPD3]] | 0.790 | LY6/PLAUR domain containing 3 |
| [[TINAGL1]] | 0.788 | tubulointerstitial nephritis antigen like 1 |
| [[PRSS3]] | 0.777 | serine protease 3 |
| [[PLEKHG5]] | 0.767 | pleckstrin homology and RhoGEF domain containing G5 |
| [[PPARD]] | 0.765 | peroxisome proliferator activated receptor delta |
| [[KRT15]] | 0.753 | keratin 15 |
| [[TMC7]] | 0.751 | transmembrane channel like 7 |
| [[ITGA6]] | 0.736 | integrin subunit alpha 6 |
| [[FERMT1]] | 0.734 | FERM domain containing kindlin 1 |
| [[PLEKHM1P1]] | 0.732 | pleckstrin homology and RUN domain containing M1 pseudogene 1 |
| [[PLAUR]] | 0.712 | plasminogen activator, urokinase receptor |
| [[PDE2A]] | 0.711 | phosphodiesterase 2A |
| [[SEMA7A]] | 0.707 | semaphorin 7A (JohnMiltonHagen blood group) |
| [[TGFA]] | 0.704 | transforming growth factor alpha |
| [[KPNA2P3]] | 0.703 | karyopherin subunit alpha 2 pseudogene 3 |
| [[RAPGEF3]] | 0.699 | Rap guanine nucleotide exchange factor 3 |
| [[LAMA3]] | 0.697 | laminin subunit alpha 3 |
| [[GDPGP1]] | 0.695 | GDP-D-glucose phosphorylase 1 |
| [[EPHB6]] | 0.692 | EPH receptor B6 |
| [[TOR4A]] | 0.692 | torsin family 4 member A |
| [[GDPD5]] | 0.688 | glycerophosphodiester phosphodiesterase domain containing 5 |
| [[CALB2]] | 0.681 | calbindin 2 |
| [[PLEKHM1]] | 0.680 | pleckstrin homology and RUN domain containing M1 |
| [[RHOF]] | 0.675 | ras homolog family member F, filopodia associated |
| [[PSD3]] | 0.672 | pleckstrin and Sec7 domain containing 3 |
| [[NGEF]] | 0.671 | neuronal guanine nucleotide exchange factor |
| [[ARHGEF4]] | 0.670 | Rho guanine nucleotide exchange factor 4 |
| [[GJB3]] | 0.670 | gap junction protein beta 3 |
| [[SERPINB1]] | 0.669 | serpin family B member 1 |
| [[TMCC3]] | 0.666 | transmembrane and coiled-coil domain family 3 |
| [[ARHGAP27P1-BPTFP1-KPNA2P3]] | 0.657 | ARHGAP27P1-BPTFP1-KPNA2P3 readthrough, transcribed pseudogene |
| [[DHRS9]] | 0.655 | dehydrogenase/reductase 9 |
| [[TIAM1]] | 0.646 | TIAM Rac1 associated GEF 1 |
| [[NTSR1]] | 0.645 | neurotensin receptor 1 |
| [[ESAM]] | 0.645 | endothelial cell adhesion molecule |
| [[ADAM19]] | 0.641 | ADAM metallopeptidase domain 19 |
| [[WSCD1]] | 0.633 | WSC domain sialate O sulfotransferase 1 |
| [[C6orf141]] | 0.628 | chromosome 6 open reading frame 141 |
| [[ITPRID2]] | 0.628 | ITPR interacting domain containing 2 |
| [[OSBPL3]] | 0.624 | oxysterol binding protein like 3 |
| [[ADAM8]] | 0.624 | ADAM metallopeptidase domain 8 |
| [[OTUB2]] | 0.621 | OTU deubiquitinase, ubiquitin aldehyde binding 2 |
| [[DENND2C]] | 0.620 | DENN domain containing 2C |
| [[ATG16L1]] | 0.619 | autophagy related 16 like 1 |
| [[LINC02725]] | 0.619 | long independently transcribed non-coding RNA 2725 |
| [[HAS3]] | 0.615 | hyaluronan synthase 3 |
| [[WNT7A]] | 0.614 | Wnt family member 7A |
| [[TNFRSF6B]] | 0.613 | TNF receptor superfamily member 6b |
| [[LANCL3]] | 0.610 | LanC like family member 3 |
| [[EIF5A2]] | 0.608 | eukaryotic translation initiation factor 5A2 |
| [[SERINC2]] | 0.605 | serine incorporator 2 |
| [[PRAG1]] | 0.605 | PEAK1 related, kinase-activating pseudokinase 1 |
| [[SLC35E4]] | 0.600 | solute carrier family 35 member E4 |
| [[PJA1]] | 0.598 | praja ring finger ubiquitin ligase 1 |
| [[FAM3C]] | 0.589 | FAM3 metabolism regulating signaling molecule C |
| [[SCAT1]] | 0.589 | S-phase cancer associated transcript 1 |
| [[LINC01589]] | 0.589 | long independently transcribed non-coding RNA 1589 |
| [[PEAR1]] | 0.587 | platelet endothelial aggregation receptor 1 |
| [[PTAFR]] | 0.586 | platelet activating factor receptor |
| [[ZNF185]] | 0.584 | zinc finger protein 185 with LIM domain |
| [[PTPRE]] | 0.583 | protein tyrosine phosphatase receptor type E |
| [[FAM3C2P]] | 0.583 | family with sequence similarity 3 member C2, pseudogene |
| [[FGD6]] | 0.576 | FYVE, RhoGEF and PH domain containing 6 |
| [[CDYL2]] | 0.575 | chromodomain Y like 2 |
| [[CD58]] | 0.574 | CD58 molecule |
| [[VSIG1]] | 0.568 | V-set and immunoglobulin domain containing 1 |
| [[MPRIP]] | 0.565 | myosin phosphatase Rho interacting protein |
| [[ATG9B]] | 0.564 | autophagy related 9B |
| [[TNFRSF25]] | 0.553 | TNF receptor superfamily member 25 |
| [[BEAN1]] | 0.551 | brain expressed associated with NEDD4 1 |
| [[AGPAT4]] | 0.549 | 1-acylglycerol-3-phosphate O-acyltransferase 4 |
| [[NECTIN1]] | 0.548 | nectin cell adhesion molecule 1 |
| [[MALL]] | 0.547 | mal, T cell differentiation protein like |
| [[F3]] | 0.546 | coagulation factor III, tissue factor |
| [[TMEM92]] | 0.545 | transmembrane protein 92 |
| [[SCEL]] | 0.543 | sciellin |
| [[NPC1]] | 0.541 | NPC intracellular cholesterol transporter 1 |
| [[SLC14A1]] | 0.540 | solute carrier family 14 member 1 (Kidd blood group) |
| [[BACE2]] | 0.539 | beta-secretase 2 |
| [[SYT13]] | 0.537 | synaptotagmin 13 |
| [[FAM110C]] | 0.536 | family with sequence similarity 110 member C |
| [[CCDC68]] | 0.534 | coiled-coil domain containing 68 |
| [[PNMA2]] | 0.528 | PNMA family member 2 |
| [[GNA15]] | 0.525 | G protein subunit alpha 15 |
| [[MAOB]] | 0.516 | monoamine oxidase B |
| [[ZNF365]] | 0.514 | zinc finger protein 365 |
| [[THBD]] | 0.512 | thrombomodulin |
| [[LAT]] | 0.512 | linker for activation of T cells |
| [[TNS3]] | -0.511 | tensin 3 |
| [[TMEM154]] | 0.509 | transmembrane protein 154 |
| [[CELSR1]] | 0.503 | cadherin EGF LAG seven-pass G-type receptor 1 |
| [[KISS1]] | 0.501 | KiSS-1 metastasis suppressor |
| [[SIGIRR]] | 0.500 | single Ig and TIR domain containing |
| [[CARD11]] | 0.499 | caspase recruitment domain family member 11 |
| [[LINC01610]] | 0.498 | long independently transcribed non-coding RNA 1610 |
| [[MFNG]] | 0.494 | MFNG O-fucosylpeptide 3-beta-N-acetylglucosaminyltransferase |
| [[CTTNBP2NL]] | 0.492 | CTTNBP2 N-terminal like |
| [[UNC13A]] | 0.480 | unc-13 homolog A |
| [[PI4K2A]] | 0.474 | phosphatidylinositol 4-kinase type 2 alpha |
| [[RAP1GAP2]] | 0.471 | RAP1 GTPase activating protein 2 |
| [[ARAP1]] | 0.467 | ArfGAP with RhoGAP domain, ankyrin repeat and PH domain 1 |
| [[BICDL1]] | 0.465 | BICD family like cargo adaptor 1 |
| [[PRDM1]] | 0.464 | PR/SET domain 1 |
| [[TMEM171]] | 0.462 | transmembrane protein 171 |
| [[COBLL1]] | -0.458 | cordon-bleu WH2 repeat protein like 1 |
| [[PDP1]] | 0.449 | pyruvate dehydrogenase phosphatase catalytic subunit 1 |
| [[KIAA1671]] | 0.441 | KIAA1671 |
| [[RASA1]] | 0.436 | RAS p21 protein activator 1 |
| [[CCK]] | 0.421 | cholecystokinin |
| [[EVA1A-AS]] | 0.416 | EVA1A antisense RNA |
| [[PLCH2]] | 0.416 | phospholipase C eta 2 |
| [[PLEKHH1]] | 0.415 | pleckstrin homology, MyTH4 and FERM domain containing H1 |
| [[CSF2RA]] | 0.414 | colony stimulating factor 2 receptor subunit alpha |
| [[MDFI]] | 0.407 | MyoD family inhibitor |
| [[STRIP2]] | 0.404 | striatin interacting protein 2 |
| [[CALM2]] | 0.403 | calmodulin 2 |
| [[YOD1]] | 0.401 | YOD1 deubiquitinase |
| [[MGST1]] | -0.401 | microsomal glutathione S-transferase 1 |
| [[GFOD1]] | 0.393 | Gfo/Idh/MocA-like oxidoreductase domain containing 1 |
| [[SNRK]] | 0.391 | SNF related kinase |
| [[SFN]] | 0.384 | stratifin |
| [[SORBS2]] | -0.381 | sorbin and SH3 domain containing 2 |
| [[LINP1]] | 0.375 | lncRNA in non-homologous end joining pathway 1 |
| [[CERK]] | 0.374 | ceramide kinase |
| [[FUT8]] | 0.369 | fucosyltransferase 8 |
| [[SLC12A6]] | 0.365 | solute carrier family 12 member 6 |
| [[LINC01322]] | 0.351 | long independently transcribed non-coding RNA 1322 |
| [[FRMD5]] | 0.348 | FERM domain containing 5 |
| [[GSKIP]] | 0.345 | GSK3B interacting protein |
| [[NHS]] | 0.338 | NHS actin remodeling regulator |
| [[MET]] | 0.330 | MET proto-oncogene, receptor tyrosine kinase |
| [[ZBTB43]] | 0.307 | zinc finger and BTB domain containing 43 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 34; `graph/modules.parquet` — module == 34; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [33] (drug-dose × line)
