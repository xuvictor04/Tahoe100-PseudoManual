---
module: 13
type: "module"
n_genes: 213
n_plus: 213
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.19666273891925812
label: "epithelial mesenchymal transition"
label_source: "hallmark"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 013

*epithelial mesenchymal transition · 213 genes (single-armed) · [[Module 013.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

Label from the validation stage: **epithelial mesenchymal transition** (hallmark, q 8e-19; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | epithelial mesenchymal transition | hallmark | 29/213 | 11.2 | 8e-19 |
| + | epithelial mesenchymal transition | hallmark | 29/213 | 11.2 | 8e-19 |
| + | Extracellular matrix organization | reactome | 22/213 | 6.43 | 6e-09 |
| all | Extracellular matrix organization | reactome | 22/213 | 6.43 | 6e-09 |
| all | Collagen formation | reactome | 12/213 | 10.8 | 9e-07 |
| + | Collagen formation | reactome | 12/213 | 10.8 | 9e-07 |
| + | Assembly of collagen fibrils and other multimeric structures | reactome | 10/213 | 14.2 | 1e-06 |
| all | Assembly of collagen fibrils and other multimeric structures | reactome | 10/213 | 14.2 | 1e-06 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 12), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Dinaciclib (drug)]] 5 µM (+6.9, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (+6.4, ⚠ toxic; transcription drop; cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (+4.6, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (+4.6); [[Dinaciclib (drug)]] 0.05 µM (+4.4, ⚠ toxic; transcription drop; cell-cycle shift); [[Tucidinostat (drug)]] 0.5 µM (+3.1, ⚠ cell-cycle shift); [[Ipatasertib (drug)]] 0.5 µM (+1.6); [[LY-2584702 (tosylate salt) (drug)]] 5 µM (+1.4, ⚠ toxic); [[Filgotinib (drug)]] 5 µM (+1.4); [[Carbamazepine (drug)]] 5 µM (+1.3); [[Estrone sulfate (potassium) (drug)]] 5 µM (+1.3); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM (+1.2); [[Auranofin (drug)]] 5 µM (+1.1); [[Pimozide (drug)]] 0.05 µM (+1.1); [[Apalutamide (drug)]] 0.5 µM (+1.1); [[Vitamin K4 (drug)]] 0.05 µM (+1.1) (23 in all, 9 with an alert ⚠; shown: the 10 strongest and the 6 next strongest without an alert)
- Lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM (-3.7, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 0.5 µM (-3.7, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (-3.3, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-3.2, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-2.7, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (-2.7, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (-2.6, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (-2.6, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (-2.3, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 0.05 µM (-2.2, ⚠ cell-cycle shift); [[Dexamethasone (drug)]] 0.5 µM (-2.0); [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM (-2.0); [[Clobetasol propionate (drug)]] 5 µM (-1.9); [[Ixazomib citrate (drug)]] 0.5 µM (-1.8); [[Triamcinolone (drug)]] 5 µM (-1.7); [[Triamcinolone (drug)]] 0.5 µM (-1.6); [[Dexamethasone (drug)]] 5 µM (-1.6); [[Budesonide (drug)]] 5 µM (-1.6); [[PH-797804 (drug)]] 5 µM (-1.5); [[Dexamethasone (drug)]] 0.05 µM (-1.4) (44 in all, 18 with an alert ⚠; shown: the 10 strongest and the 10 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[NCI-H1792 (line)]], [[HOP62 (line)]], [[hTERT-HPNE (line)]], [[NCI-H23 (line)]], [[LOX-IMVI (line)]], [[H4 (line)]], [[RKO (line)]], [[J82 (line)]]

## Candidate new members

*Members not annotated to the set their arm is enriched for, ranked by mean cos to the annotated members (`validation/novel_members.csv`); ⚠ = a reason to doubt the gene's place (in the vector space only through flagged drug-doses), kept in its rank. 40 candidates, none with an alert; shown: the 15 strongest.*

| # | Gene | Set | Mean cos |
|---|---|---|---|
| 1 | [[THBS2]] | Collagen biosynthesis and modifying enzymes | +0.60 |
| 2 | [[ITGA11]] | Collagen biosynthesis and modifying enzymes | +0.59 |
| 3 | [[RFX8]] | NCAM1 interactions | +0.59 |
| 4 | [[PDGFRB]] | Collagen biosynthesis and modifying enzymes | +0.58 |
| 5 | [[SARDH]] | Signaling by PDGF | +0.58 |
| 6 | [[CARMN]] | Signaling by PDGF | +0.58 |
| 7 | [[APCDD1L]] | Assembly of collagen fibrils and other multimeric structures | +0.58 |
| 8 | [[SCUBE3]] | NCAM1 interactions | +0.57 |
| 9 | [[INSYN2B]] | Defective B3GALTL causes PpS | +0.57 |
| 10 | [[TMEM200A]] | Defective B3GALTL causes PpS | +0.56 |
| 11 | [[DKK3]] | Collagen degradation | +0.56 |
| 12 | [[COL5A1]] | Defective B3GALTL causes PpS | +0.56 |
| 13 | [[CSPG4]] | Collagen degradation | +0.56 |
| 14 | [[LINC01411]] | Defective B3GALTL causes PpS | +0.55 |
| 15 | [[SYNDIG1]] | Collagen biosynthesis and modifying enzymes | +0.55 |

## + arm (213)

| Gene | Projection | Name |
|---|---|---|
| [[APCDD1L]] | 0.907 | APC down-regulated 1 like |
| [[INSYN2B]] | 0.839 | inhibitory synaptic factor family member 2B |
| [[NAV1]] | 0.830 | neuron navigator 1 |
| [[SYNDIG1]] | 0.817 | synapse differentiation inducing 1 |
| [[ITGA11]] | 0.808 | integrin subunit alpha 11 |
| [[SPOCD1]] | 0.798 | SPOC domain containing 1 |
| [[APCDD1L-DT]] | 0.793 | APCDD1L divergent transcript |
| [[LINC01411]] | 0.788 | long independently transcribed non-coding RNA 1411 |
| [[COL5A1]] | 0.785 | collagen type V alpha 1 chain |
| [[SAMD3]] | 0.770 | sterile alpha motif domain containing 3 |
| [[VSTM4]] | 0.766 | V-set and transmembrane domain containing 4 |
| [[TMEM200A]] | 0.751 | transmembrane protein 200A |
| [[EDNRA]] | 0.747 | endothelin receptor type A |
| [[GPR68]] | 0.746 | G protein-coupled receptor 68 |
| [[THBS2]] | 0.739 | thrombospondin 2 |
| [[FRMD4A]] | 0.738 | FERM domain containing 4A |
| [[GDNF-AS1]] | 0.735 | GDNF antisense RNA 1 |
| [[RFX8]] | 0.731 | regulatory factor X8 |
| [[LINC01615]] | 0.729 | long independently transcribed non-coding RNA 1615 |
| [[SEMA5A]] | 0.722 | semaphorin 5A |
| [[TSHZ3]] | 0.721 | teashirt zinc finger homeobox 3 |
| [[COL6A3]] | 0.717 | collagen type VI alpha 3 chain |
| [[DENND2A]] | 0.717 | DENN domain containing 2A |
| [[COL15A1]] | 0.717 | collagen type XV alpha 1 chain |
| [[SETBP1]] | 0.716 | SET binding protein 1 |
| [[COL6A2]] | 0.707 | collagen type VI alpha 2 chain |
| [[ADAMTS12]] | 0.707 | ADAM metallopeptidase with thrombospondin type 1 motif 12 |
| [[MEG3]] | 0.704 | maternally expressed 3 |
| [[LOXL2]] | 0.703 | lysyl oxidase like 2 |
| [[NMNAT2]] | 0.702 | nicotinamide nucleotide adenylyltransferase 2 |
| [[ADAMTS6]] | 0.701 | ADAM metallopeptidase with thrombospondin type 1 motif 6 |
| [[SPOCK1]] | 0.700 | SPARC (osteonectin), cwcv and kazal like domains proteoglycan 1 |
| [[PLEKHG4B]] | 0.700 | pleckstrin homology and RhoGEF domain containing G4B |
| [[GDNF]] | 0.696 | glial cell derived neurotrophic factor |
| [[CSF1R]] | 0.693 | colony stimulating factor 1 receptor |
| [[ANGPTL2]] | 0.693 | angiopoietin like 2 |
| [[MEG8]] | 0.691 | maternally expressed 8, small nucleolar RNA host gene |
| [[PDGFRB]] | 0.691 | platelet derived growth factor receptor beta |
| [[KCNK3]] | 0.688 | potassium two pore domain channel subfamily K member 3 |
| [[SLC8A1]] | 0.687 | solute carrier family 8 member A1 |
| [[AK5]] | 0.680 | adenylate kinase 5 |
| [[CSPG4]] | 0.677 | chondroitin sulfate proteoglycan 4 |
| [[ADAM12]] | 0.676 | ADAM metallopeptidase domain 12 |
| [[ADAMTS14]] | 0.674 | ADAM metallopeptidase with thrombospondin type 1 motif 14 |
| [[CSMD2]] | 0.671 | CUB and Sushi multiple domains 2 |
| [[EVC2]] | 0.670 | EvC ciliary complex subunit 2 |
| [[CARMN]] | 0.670 | cardiac mesoderm enhancer-associated non-coding RNA |
| [[VEGFC]] | 0.669 | vascular endothelial growth factor C |
| [[LAMA4]] | 0.661 | laminin subunit alpha 4 |
| [[DKK3]] | 0.658 | dickkopf Wnt signaling pathway inhibitor 3 |
| [[PRRX1]] | 0.658 | paired related homeobox 1 |
| [[FAM167A]] | 0.656 | family with sequence similarity 167 member A |
| [[NTNG2]] | 0.655 | netrin G2 |
| [[AFF3]] | 0.654 | ALF transcription elongation factor 3 |
| [[BAALC]] | 0.651 | BAALC binder of MAP3K1 and KLF4 |
| [[COL7A1]] | 0.651 | collagen type VII alpha 1 chain |
| [[SHANK1]] | 0.650 | SH3 and multiple ankyrin repeat domains 1 |
| [[CTHRC1]] | 0.648 | collagen triple helix repeat containing 1 |
| [[SCUBE3]] | 0.648 | signal peptide, CUB domain and EGF like domain containing 3 |
| [[HTR1F]] | 0.646 | 5-hydroxytryptamine receptor 1F |
| [[MIR493HG]] | 0.642 | MIR493 cluster host gene |
| [[PRSS23]] | 0.639 | serine protease 23 |
| [[OR9Q1]] | 0.633 | olfactory receptor family 9 subfamily Q member 1 |
| [[GLIS3]] | 0.632 | GLIS family zinc finger 3 |
| [[SARDH]] | 0.631 | sarcosine dehydrogenase |
| [[GPR173]] | 0.629 | G protein-coupled receptor 173 |
| [[FAM20C]] | 0.623 | FAM20C golgi associated secretory pathway kinase |
| [[PGF]] | 0.622 | placental growth factor |
| [[TSHZ3-AS1]] | 0.621 | TSHZ3 antisense RNA 1 |
| [[MYO10]] | 0.619 | myosin X |
| [[GLYATL2]] | 0.619 | glycine-N-acyltransferase like 2 |
| [[LINC02813]] | 0.618 | long independently transcribed non-coding RNA 2813 |
| [[SORCS2]] | 0.618 | sortilin related VPS10 domain containing receptor 2 |
| [[RFTN1]] | 0.616 | raftlin, lipid raft linker 1 |
| [[VEPH1]] | 0.616 | ventricular zone expressed PH domain containing 1 |
| [[KCNMA1]] | 0.616 | potassium calcium-activated channel subfamily M alpha 1 |
| [[GRIN2A]] | 0.613 | glutamate ionotropic receptor NMDA type subunit 2A |
| [[DOCK2]] | 0.611 | dedicator of cytokinesis 2 |
| [[ADAMTS16]] | 0.608 | ADAM metallopeptidase with thrombospondin type 1 motif 16 |
| [[CDH13]] | 0.607 | cadherin 13 |
| [[COL5A3]] | 0.604 | collagen type V alpha 3 chain |
| [[HS3ST3A1]] | 0.603 | heparan sulfate-glucosamine 3-sulfotransferase 3A1 |
| [[LINC00702]] | 0.603 | long independently transcribed non-coding RNA 702 |
| [[EVC]] | 0.599 | EvC ciliary complex subunit 1 |
| [[DIRAS3]] | 0.593 | DIRAS family GTPase 3 |
| [[EVA1A]] | 0.592 | eva-1 homolog A, regulator of programmed cell death |
| [[APBB1IP]] | 0.592 | amyloid beta precursor protein binding family B member 1 interacting protein |
| [[MANCR]] | 0.591 | mitotically associated long non coding RNA |
| [[NDNF]] | 0.591 | neuron derived neurotrophic factor |
| [[LINC01705]] | 0.591 | long independently transcribed non-coding RNA 1705 |
| [[LINC01119]] | 0.590 | long independently transcribed non-coding RNA 1119 |
| [[COL6A1]] | 0.586 | collagen type VI alpha 1 chain |
| [[WNT5B]] | 0.586 | Wnt family member 5B |
| [[FBLN7]] | 0.584 | fibulin 7 |
| [[AIM2]] | 0.583 | absent in melanoma 2 |
| [[GFPT2]] | 0.582 | glutamine--fructose-6-phosphate transaminase 2 |
| [[KIRREL3]] | 0.581 | kirre like nephrin family adhesion molecule 3 |
| [[ZNF385D]] | 0.580 | zinc finger protein 385D |
| [[ARMCX2]] | 0.576 | armadillo repeat containing X-linked 2 |
| [[NLRP3]] | 0.575 | NLR family pyrin domain containing 3 |
| [[SIGLEC15]] | 0.574 | sialic acid binding Ig like lectin 15 |
| [[NALF1]] | 0.572 | NALCN channel auxiliary factor 1 |
| [[TENM4]] | 0.570 | teneurin transmembrane protein 4 |
| [[GREM1]] | 0.568 | gremlin 1, DAN family BMP antagonist |
| [[FGF5]] | 0.566 | fibroblast growth factor 5 |
| [[NLRP1]] | 0.561 | NLR family pyrin domain containing 1 |
| [[PTGFR]] | 0.559 | prostaglandin F receptor |
| [[BCL11B]] | 0.559 | BCL11 transcription factor B |
| [[BNC1]] | 0.556 | basonuclin zinc finger protein 1 |
| [[TWIST2]] | 0.551 | twist family bHLH transcription factor 2 |
| [[TNS1]] | 0.550 | tensin 1 |
| [[MMP14]] | 0.547 | matrix metallopeptidase 14 |
| [[ABI3BP]] | 0.547 | ABI family member 3 binding protein |
| [[ARHGEF6]] | 0.546 | Rac/Cdc42 guanine nucleotide exchange factor 6 |
| [[PAPPA]] | 0.544 | pappalysin 1 |
| [[IGFBP3]] | 0.544 | insulin like growth factor binding protein 3 |
| [[CFAP20DC]] | 0.538 | CFAP20 domain containing |
| [[ITGB3]] | 0.537 | integrin subunit beta 3 |
| [[WNT5A]] | 0.537 | Wnt family member 5A |
| [[PRICKLE2]] | 0.537 | prickle planar cell polarity protein 2 |
| [[IL11]] | 0.536 | interleukin 11 |
| [[EML1]] | 0.535 | EMAP like 1 |
| [[KLF7]] | 0.534 | KLF transcription factor 7 |
| [[STK32B]] | 0.533 | serine/threonine kinase 32B |
| [[SYTL3]] | 0.531 | synaptotagmin like 3 |
| [[IQCA1]] | 0.526 | dynein regulatory complex subunit 11 |
| [[PHLDB1]] | 0.524 | pleckstrin homology like domain family B member 1 |
| [[RUNX3]] | 0.523 | RUNX family transcription factor 3 |
| [[PDE4DIPP2]] | 0.521 | PDE4DIP pseudogene 2 |
| [[SDC2]] | 0.519 | syndecan 2 |
| [[ITPR1]] | 0.519 | inositol 1,4,5-trisphosphate receptor type 1 |
| [[ADAMTS18]] | 0.517 | ADAM metallopeptidase with thrombospondin type 1 motif 18 |
| [[ZNF175]] | 0.513 | zinc finger protein 175 |
| [[LINC01435]] | 0.510 | long independently transcribed non-coding RNA 1435 |
| [[CYP26B1]] | 0.509 | cytochrome P450 family 26 subfamily B member 1 |
| [[SFRP1]] | 0.509 | secreted frizzled related protein 1 |
| [[BOC]] | 0.507 | BOC cell adhesion associated, oncogene regulated |
| [[PCDHGA2]] | 0.500 | protocadherin gamma subfamily A, 2 |
| [[ABCA1]] | 0.499 | ATP binding cassette subfamily A member 1 |
| [[LRFN5]] | 0.494 | leucine rich repeat and fibronectin type III domain containing 5 |
| [[IGFBP7]] | 0.494 | insulin like growth factor binding protein 7 |
| [[VCAN]] | 0.493 | versican |
| [[HHIP]] | 0.492 | hedgehog interacting protein |
| [[TMEM132D]] | 0.490 | transmembrane protein 132D |
| [[PDLIM4]] | 0.489 | PDZ and LIM domain 4 |
| [[STRA6]] | 0.485 | signaling receptor and transporter of retinol STRA6 |
| [[ARL10]] | 0.485 | ARF like GTPase 10 |
| [[CNRIP1]] | 0.483 | cannabinoid receptor interacting protein 1 |
| [[NTNG1]] | 0.481 | netrin G1 |
| [[NTF3]] | 0.480 | neurotrophin 3 |
| [[MIR3936HG]] | -0.479 | MIR3936 host gene |
| [[NTM]] | 0.478 | neurotrimin |
| [[ZNF667]] | 0.477 | zinc finger protein 667 |
| [[ADAMTS2]] | 0.474 | ADAM metallopeptidase with thrombospondin type 1 motif 2 |
| [[MME]] | 0.474 | membrane metalloendopeptidase |
| [[MXRA5]] | 0.474 | matrix remodeling associated 5 |
| [[CYGB]] | 0.469 | cytoglobin |
| [[TEK]] | 0.467 | TEK receptor tyrosine kinase |
| [[PRR16]] | 0.463 | proline rich 16 |
| [[CA12]] | 0.463 | carbonic anhydrase 12 |
| [[GSDME]] | 0.462 | gasdermin E |
| [[PTPRN]] | 0.462 | protein tyrosine phosphatase receptor type N |
| [[CLDN14-AS1]] | 0.459 | — |
| [[LAYN]] | 0.455 | layilin |
| [[WIPF1]] | 0.451 | WAS/WASL interacting protein family member 1 |
| [[MDGA1]] | 0.449 | MAM domain containing glycosylphosphatidylinositol anchor 1 |
| [[SIPA1L3]] | 0.446 | signal induced proliferation associated 1 like 3 |
| [[SLIT3]] | 0.445 | slit guidance ligand 3 |
| [[PRKY]] | 0.442 | protein kinase Y-linked (pseudogene) |
| [[HAS2]] | 0.440 | hyaluronan synthase 2 |
| [[FLI1]] | 0.438 | Fli-1 proto-oncogene, ETS transcription factor |
| [[CPQ]] | 0.435 | carboxypeptidase Q |
| [[EFCAB13]] | 0.432 | EF-hand calcium binding domain 13 |
| [[ADAMTS9-AS2]] | 0.428 | ADAMTS9 antisense RNA 2 |
| [[ZNF439]] | 0.427 | zinc finger protein 439 |
| [[ZNF471]] | 0.427 | zinc finger protein 471 |
| [[C14orf132]] | 0.424 | chromosome 14 open reading frame 132 |
| [[UBE2Q2P13]] | 0.422 | UBE2Q2 pseudogene 13 |
| [[B3GNT9]] | 0.420 | UDP-GlcNAc:betaGal beta-1,3-N-acetylglucosaminyltransferase 9 |
| [[STAC]] | 0.419 | SH3 and cysteine rich domain |
| [[DAB2]] | 0.419 | DAB adaptor protein 2 |
| [[FMNL3]] | 0.408 | formin like 3 |
| [[CCDC33]] | 0.403 | coiled-coil domain containing 33 |
| [[RNF152]] | 0.397 | ring finger protein 152 |
| [[CYP27C1]] | 0.395 | cytochrome P450 family 27 subfamily C member 1 |
| [[LRIG1]] | 0.391 | leucine rich repeats and immunoglobulin like domains 1 |
| [[ANO6]] | 0.388 | anoctamin 6 |
| [[PKD1L1-AS1]] | 0.386 | PKD1L1 antisense RNA 1 |
| [[IL1RAPL1]] | 0.385 | interleukin 1 receptor accessory protein like 1 |
| [[LOX]] | 0.379 | lysyl oxidase |
| [[LOXL1]] | 0.375 | lysyl oxidase like 1 |
| [[FMNL1-DT]] | 0.374 | FMNL1 divergent transcript |
| [[CERCAM]] | 0.368 | cerebral endothelial cell adhesion molecule |
| [[IGFBP6]] | 0.351 | insulin like growth factor binding protein 6 |
| [[TGFB1I1]] | 0.342 | transforming growth factor beta 1 induced transcript 1 |
| [[SUCNR1]] | 0.338 | succinate receptor 1 |
| [[AGTR1]] | 0.334 | angiotensin II receptor type 1 |
| [[MSRB3]] | 0.330 | methionine sulfoxide reductase B3 |
| [[GLIS1]] | 0.329 | GLIS family zinc finger 1 |
| [[IGDCC4]] | 0.327 | immunoglobulin superfamily DCC subclass member 4 |
| [[CNPY4]] | 0.327 | canopy FGF signaling regulator 4 |
| [[DSCAM]] | 0.326 | DS cell adhesion molecule |
| [[OSMR]] | 0.296 | oncostatin M receptor |
| [[C2CD2]] | 0.293 | C2 calcium dependent domain containing 2 |
| [[S1PR2]] | 0.277 | sphingosine-1-phosphate receptor 2 |
| [[PCBP3]] | 0.264 | poly(rC) binding protein 3 |
| [[WFDC10B]] | 0.256 | WAP four-disulfide core domain 10B |
| [[SLC22A5]] | -0.242 | solute carrier family 22 member 5 |
| [[GYPC]] | 0.219 | glycophorin C (Gerbich blood group) |
| [[FMNL1]] | 0.198 | formin like 1 |
| [[LINC00698]] | 0.197 | long independently transcribed non-coding RNA 698 |
| [[P2RX7]] | 0.170 | purinergic receptor P2X 7 |
| [[WFDC3]] | 0.145 | WAP four-disulfide core domain 3 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 13; `graph/modules.parquet` — module == 13; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [12] (drug-dose × line)
