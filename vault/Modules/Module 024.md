---
module: 24
type: "module"
n_genes: 179
n_plus: 168
n_minus: 11
arms_opposite: true
mean_cos_between_arms: -0.28817200660705566
label: "Aerobic respiration and respiratory electron transport"
label_source: "reactome"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 024

*Aerobic respiration and respiratory electron transport · 179 genes (168 in the + arm, 11 in the − arm) · [[Module 024.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29). The + arm rises where the − arm falls. Arm = the side of the module's main direction a gene sits on.

Label from the validation stage: **Aerobic respiration and respiratory electron transport** (reactome, q 4e-04; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | Aerobic respiration and respiratory electron transport | reactome | 14/179 | 5.10 | 4e-04 |
| + | Aerobic respiration and respiratory electron transport | reactome | 12/168 | 4.66 | 0.005 |
| all | Respiratory electron transport | reactome | 9/179 | 5.38 | 0.019 |
| + | Complex I biogenesis | reactome | 6/168 | 8.68 | 0.025 |
| all | Complex I biogenesis | reactome | 6/179 | 8.15 | 0.034 |
| all | oxidative phosphorylation | hallmark | 10/179 | 4.21 | 0.049 |

## Drugs that move it

*Mean pooled z of the + arm minus the − arm (`graph/module_pooled_z.npy`, row 23), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it (+ arm up, − arm down): [[Ipatasertib (drug)]] 0.5 µM (+3.6); [[Topotecan (hydrochloride) (drug)]] 5 µM (+3.1, ⚠ toxic; cell-cycle shift); [[Sunitinib (drug)]] 5 µM (+3.0, ⚠ toxic); [[Panobinostat (drug)]] 5 µM (+2.9, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (+2.7, ⚠ cell-cycle shift); [[Bimiralisib (drug)]] 0.5 µM (+2.6); [[BAY1125976 (drug)]] 0.5 µM (+2.5); [[GSK1059615 (drug)]] 0.5 µM (+2.5); [[Docetaxel (Trihydrate) (drug)]] 0.5 µM (+2.5); [[Celecoxib (drug)]] 0.5 µM (+2.5); [[Radotinib (drug)]] 5 µM (+2.4); [[9-ING-41 (drug)]] 0.5 µM (+2.4); [[Methylprednisolone succinate (drug)]] 0.5 µM (+2.3); [[Azithromycin (hydrate) (drug)]] 5 µM (+2.2) (127 in all, 22 with an alert ⚠; shown: the 10 strongest and the 4 next strongest without an alert)
- Lower it: [[Dinaciclib (drug)]] 0.5 µM (-11.4, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (-11.4, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (-9.2, ⚠ toxic; transcription drop; cell-cycle shift); [[TAK-901 (drug)]] 5 µM (-5.0, ⚠ cell-cycle shift); [[PH-797804 (drug)]] 5 µM (-3.6); [[Digitoxin (drug)]] 0.5 µM (-3.2, ⚠ cell-cycle shift); [[c-Kit-IN-1 (drug)]] 0.05 µM (-2.9, ⚠ unreliable plate only); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (-2.8); [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM (-2.7); [[Homoharringtonine (drug)]] 0.5 µM (-2.7, ⚠ cell-cycle shift); [[Lucanthone (drug)]] 0.05 µM (-2.6); [[Auranofin (drug)]] 5 µM (-2.5); [[Fenofibrate (drug)]] 0.05 µM (-2.5); [[Diphenhydramine (drug)]] 0.05 µM (-2.4); [[TAK-901 (drug)]] 0.05 µM (-2.4); [[Benproperine (phosphate) (drug)]] 0.05 µM (-2.4); [[Rutin (trihydrate) (drug)]] 0.05 µM (-2.3) (152 in all, 30 with an alert ⚠; shown: the 10 strongest and the 7 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[A549 (line)]], [[SW480 (line)]], [[KATO III (line)]], [[SNU-1 (line)]], [[NCI-H23 (line)]], [[A-172 (line)]], [[A498 (line)]], [[MIA PaCa-2 (line)]]

## Candidate new members

*Members not annotated to the set their arm is enriched for, ranked by mean cos to the annotated members (`validation/novel_members.csv`); ⚠ = a reason to doubt the gene's place (in the vector space only through flagged drug-doses), kept in its rank. 18 candidates, 5 with an alert ⚠.*

| # | Gene | Set | Mean cos | Alert |
|---|---|---|---|---|
| 1 | [[SMIM26]] ⚠ | Aerobic respiration and respiratory electron transport | +0.60 | ⚠ in the vector space only through drug-doses that carry an alert |
| 2 | [[IFI27L2]] | Aerobic respiration and respiratory electron transport | +0.57 |  |
| 3 | [[LAMTOR5]] | Aerobic respiration and respiratory electron transport | +0.57 |  |
| 4 | [[CHCHD5]] | Aerobic respiration and respiratory electron transport | +0.56 |  |
| 5 | [[POLR2J]] ⚠ | Aerobic respiration and respiratory electron transport | +0.56 | ⚠ in the vector space only through drug-doses that carry an alert |
| 6 | [[TRAPPC5]] | Aerobic respiration and respiratory electron transport | +0.54 |  |
| 7 | [[KRT10]] ⚠ | Aerobic respiration and respiratory electron transport | +0.54 | ⚠ in the vector space only through drug-doses that carry an alert |
| 8 | [[RPL36AL]] ⚠ | Aerobic respiration and respiratory electron transport | +0.53 | ⚠ in the vector space only through drug-doses that carry an alert |
| 9 | [[WDR83OS]] ⚠ | Aerobic respiration and respiratory electron transport | +0.53 | ⚠ in the vector space only through drug-doses that carry an alert |
| 10 | [[KRTCAP2]] | Aerobic respiration and respiratory electron transport | +0.53 |  |
| 11 | [[POLR2I]] | Aerobic respiration and respiratory electron transport | +0.53 |  |
| 12 | [[GADD45GIP1]] | Aerobic respiration and respiratory electron transport | +0.52 |  |
| 13 | [[LAGE3]] | Aerobic respiration and respiratory electron transport | +0.52 |  |
| 14 | [[MIEN1]] | Aerobic respiration and respiratory electron transport | +0.52 |  |
| 15 | [[SNHG9]] | Aerobic respiration and respiratory electron transport | +0.51 |  |
| 16 | [[RPP21]] | Aerobic respiration and respiratory electron transport | +0.51 |  |
| 17 | [[TRIM52-AS1]] | Aerobic respiration and respiratory electron transport | +0.50 |  |
| 18 | [[TMEM258]] | Aerobic respiration and respiratory electron transport | +0.50 |  |

*⚠ 13 of its 179 genes are in the vector space only through drug-doses that carry an alert (`embed/genes.parquet` evidence_flagged_only): their place here may reflect what those drug-doses did to the cells. They are marked in the tables of this note.*

## + arm (168)

| Gene | Projection | Name | Alert |
|---|---|---|---|
| [[SMIM26]] | 0.900 | small integral membrane protein 26 | ⚠ only flagged evidence |
| [[LAMTOR5]] | 0.868 | late endosomal/lysosomal adaptor, MAPK and MTOR activator 5 |  |
| [[DCTN6-DT]] | 0.859 | DCTN6 divergent transcript |  |
| [[SNHG9]] | 0.855 | small nucleolar RNA host gene 9 |  |
| [[IFI27L2]] | 0.836 | interferon alpha inducible protein 27 like 2 |  |
| [[CHCHD5]] | 0.829 | coiled-coil-helix-coiled-coil-helix domain containing 5 |  |
| [[SNHG19]] | 0.827 | small nucleolar RNA host gene 19 |  |
| [[RPL36AL]] | 0.823 | ribosomal protein L36a like | ⚠ only flagged evidence |
| [[TRIM52-AS1]] | 0.815 | TRIM52 antisense RNA 1 |  |
| [[KRT10]] | 0.811 | keratin 10 | ⚠ only flagged evidence |
| [[MINCR]] | 0.808 | MYC-induced long non-coding RNA |  |
| [[TMEM258]] | 0.806 | transmembrane protein 258 |  |
| [[MIEN1]] | 0.805 | migration and invasion enhancer 1 |  |
| [[WDR83OS]] | 0.800 | WD repeat domain 83 opposite strand | ⚠ only flagged evidence |
| [[LAGE3]] | 0.780 | L antigen family member 3 |  |
| [[RPP21]] | 0.778 | ribonuclease P subunit p21 |  |
| [[NDUFB4]] | 0.770 | NADH:ubiquinone oxidoreductase subunit B4 |  |
| [[POLR2J]] | 0.768 | RNA polymerase II subunit J | ⚠ only flagged evidence |
| [[DPM3]] | 0.765 | dolichyl-phosphate mannosyltransferase subunit 3, regulatory |  |
| [[MTIF3]] | 0.763 | mitochondrial translational initiation factor 3 |  |
| [[C19orf81]] | 0.763 | chromosome 19 open reading frame 81 |  |
| [[MRPS36]] | 0.759 | alpha-ketoglutarate dehydrogenase subunit 4 | ⚠ only flagged evidence |
| [[POLR2I]] | 0.754 | RNA polymerase II subunit I |  |
| [[APOC1]] | 0.752 | apolipoprotein C1 |  |
| [[SNHG7]] | 0.749 | small nucleolar RNA host gene 7 |  |
| [[LAMTOR4]] | 0.748 | late endosomal/lysosomal adaptor, MAPK and MTOR activator 4 |  |
| [[SMIM27]] | 0.744 | transition zone microprotein 1 |  |
| [[TRAPPC5]] | 0.742 | trafficking protein particle complex subunit 5 |  |
| [[PCGF1]] | 0.741 | polycomb group ring finger 1 | ⚠ only flagged evidence |
| [[MRPL43]] | 0.739 | mitochondrial ribosomal protein L43 |  |
| [[PITPNA-AS1]] | 0.739 | PITPNA antisense RNA 1 |  |
| [[RPAIN]] | 0.738 | RPA interacting protein |  |
| [[UQCC3]] | 0.736 | ubiquinol-cytochrome c reductase complex assembly factor 3 |  |
| [[MRPL23]] | 0.734 | mitochondrial ribosomal protein L23 |  |
| [[SELENOH]] | 0.730 | selenoprotein H |  |
| [[TRIM7-AS2]] | 0.729 | TRIM7 antisense RNA 2 |  |
| [[RANGRF]] | 0.725 | RAN guanine nucleotide release factor |  |
| [[ZFAND2B]] | 0.725 | zinc finger AN1-type containing 2B |  |
| [[NSUN5P2-1]] | 0.722 | — | ⚠ only flagged evidence |
| [[KRTCAP2]] | 0.714 | keratinocyte associated protein 2 |  |
| [[GABARAPL2]] | 0.714 | GABA type A receptor associated protein like 2 |  |
| [[MIR4458HG]] | 0.714 | MIR4458 host gene |  |
| [[DNLZ]] | 0.713 | DNL-type zinc finger |  |
| [[NSUN5P1-1]] | 0.710 | — |  |
| [[ZFAND2A-DT]] | 0.708 | ZFAND2A divergent transcript |  |
| [[C1orf122]] | 0.707 | chromosome 1 open reading frame 122 |  |
| [[VEGFB]] | 0.705 | vascular endothelial growth factor B |  |
| [[NDUFA7]] | 0.696 | NADH:ubiquinone oxidoreductase subunit A7 |  |
| [[MHENCR]] | 0.695 | melanoma highly expressed competing endogenous lncRNA for miR-425 and miR-489 |  |
| [[JOSD2]] | 0.683 | Josephin domain containing 2 |  |
| [[ZNHIT3]] | 0.682 | zinc finger HIT-type containing 3 |  |
| [[FBXL15]] | 0.682 | F-box and leucine rich repeat protein 15 |  |
| [[CSKMT]] | 0.677 | citrate synthase lysine methyltransferase |  |
| [[ENKD1]] | 0.676 | enkurin domain containing 1 |  |
| [[C1orf35]] | 0.673 | chromosome 1 open reading frame 35 |  |
| [[MTLN]] | 0.668 | mitoregulin | ⚠ only flagged evidence |
| [[POLR2H]] | 0.667 | RNA polymerase II, I and III subunit H |  |
| [[AKAP1-DT]] | 0.664 | AKAP1 divergent transcript |  |
| [[C17orf49]] | 0.663 | BPTF associated chromatin complex component 1 | ⚠ only flagged evidence |
| [[DNAJC4]] | 0.662 | DnaJ heat shock protein family (Hsp40) member C4 |  |
| [[RFNG]] | 0.661 | RFNG O-fucosylpeptide 3-beta-N-acetylglucosaminyltransferase |  |
| [[CLN8-AS1]] | 0.661 | CLN8 antisense RNA 1 |  |
| [[MED10]] | 0.660 | mediator complex subunit 10 |  |
| [[OCEL1]] | 0.659 | occludin/ELL domain containing 1 |  |
| [[FBXW5]] | 0.657 | F-box and WD repeat domain containing 5 |  |
| [[SELENOM]] | 0.656 | selenoprotein M |  |
| [[DCXR]] | 0.652 | dicarbonyl and L-xylulose reductase |  |
| [[ZNF232-AS1]] | 0.648 | ZNF232 antisense RNA 1 |  |
| [[BRI3]] | 0.647 | brain protein I3 |  |
| [[ATP6V1F]] | 0.645 | ATPase H+ transporting V1 subunit F |  |
| [[C11orf1]] | 0.645 | cilia and flagella associated protein 68 |  |
| [[LSM10]] | 0.641 | LSM10, U7 small nuclear RNA associated |  |
| [[TMEM126A]] | 0.641 | transmembrane protein 126A |  |
| [[NAT14]] | 0.640 | N-acetyltransferase 14 (putative) |  |
| [[MAP2K7]] | 0.640 | mitogen-activated protein kinase kinase 7 |  |
| [[PTRHD1]] | 0.639 | peptidyl-tRNA hydrolase domain containing 1 | ⚠ only flagged evidence |
| [[MRPL54]] | 0.638 | mitochondrial ribosomal protein L54 |  |
| [[CUTA]] | 0.638 | cutA divalent cation tolerance homolog |  |
| [[GADD45GIP1]] | 0.628 | GADD45G interacting protein 1 |  |
| [[RCE1]] | 0.613 | Ras converting CAAX endopeptidase 1 |  |
| [[UXT]] | 0.611 | ubiquitously expressed prefoldin like chaperone |  |
| [[TMEM134]] | 0.609 | transmembrane protein 134 |  |
| [[SCAMP3]] | 0.609 | secretory carrier membrane protein 3 |  |
| [[NDUFC1]] | 0.607 | NADH:ubiquinone oxidoreductase subunit C1 |  |
| [[CCDC127]] | 0.607 | coiled-coil domain containing 127 |  |
| [[RAB24]] | 0.607 | RAB24, member RAS oncogene family |  |
| [[SSNA1]] | 0.604 | SS nuclear autoantigen 1 |  |
| [[ATP5PO]] | 0.603 | ATP synthase peripheral stalk subunit OSCP | ⚠ only flagged evidence |
| [[TMEM205]] | 0.601 | transmembrane protein 205 |  |
| [[TRAPPC6A]] | 0.592 | trafficking protein particle complex subunit 6A |  |
| [[TM2D3]] | 0.589 | TM2 domain containing 3 |  |
| [[ATP6V0B]] | 0.588 | ATPase H+ transporting V0 subunit b |  |
| [[TBC1D22A-DT]] | 0.584 | TBC1D22A divergent RNA CLOCK regulator 1 |  |
| [[EMC2]] | 0.582 | ER membrane protein complex subunit 2 |  |
| [[HCFC1R1]] | 0.580 | host cell factor C1 regulator 1 |  |
| [[PIAS1]] | 0.576 | protein inhibitor of activated STAT 1 |  |
| [[HRAS]] | 0.575 | HRas proto-oncogene, GTPase |  |
| [[NAA38]] | 0.575 | N-alpha-acetyltransferase 38, NatC auxiliary subunit |  |
| [[SLC25A4]] | 0.574 | solute carrier family 25 member 4 |  |
| [[PGLS]] | 0.573 | 6-phosphogluconolactonase |  |
| [[NMB]] | 0.573 | neuromedin B |  |
| [[SCAMP2]] | 0.571 | secretory carrier membrane protein 2 |  |
| [[ZNF524]] | 0.571 | zinc finger protein 524 |  |
| [[RNF7]] | 0.570 | ring finger protein 7 |  |
| [[RFXANK]] | 0.570 | regulatory factor X associated ankyrin containing protein |  |
| [[SVBP]] | 0.570 | small vasohibin binding protein |  |
| [[NUDT16L1]] | 0.564 | nudix hydrolase 16 like 1 |  |
| [[FLVCR1-DT]] | 0.563 | FLVCR1 divergent transcript |  |
| [[SP2-DT]] | 0.556 | — |  |
| [[ZNF358]] | 0.556 | zinc finger protein 358 |  |
| [[PIGH]] | 0.552 | phosphatidylinositol glycan anchor biosynthesis class H |  |
| [[FMC1]] | 0.552 | formation of mitochondrial complex V assembly factor 1 |  |
| [[NPC2]] | 0.550 | NPC intracellular cholesterol transporter 2 |  |
| [[POLR2J4]] | 0.549 | SPDYE1 and UBE2D4 antisense RNA 1 |  |
| [[CSAG1]] | 0.543 | chondrosarcoma associated gene 1 |  |
| [[FBXO21]] | 0.539 | F-box protein 21 |  |
| [[JTB]] | 0.531 | jumping translocation breakpoint |  |
| [[ILF3-DT]] | 0.525 | ILF3 divergent transcript |  |
| [[ATP6V0E1]] | 0.525 | ATPase H+ transporting V0 subunit e1 |  |
| [[NDUFB10]] | 0.521 | NADH:ubiquinone oxidoreductase subunit B10 |  |
| [[DLL3]] | 0.519 | delta like canonical Notch ligand 3 |  |
| [[ISCA2]] | 0.510 | iron-sulfur cluster assembly 2 |  |
| [[TIMM17B]] | 0.501 | translocase of inner mitochondrial membrane 17B | ⚠ only flagged evidence |
| [[MIR193BHG]] | 0.501 | MIR193b-365a host gene |  |
| [[DCTN3]] | 0.500 | dynactin subunit 3 |  |
| [[FAM222B]] | 0.500 | family with sequence similarity 222 member B |  |
| [[BTBD7]] | 0.498 | BTB domain containing 7 |  |
| [[ARL6IP4]] | 0.495 | ARF like GTPase 6 interacting protein 4 |  |
| [[LDAF1]] | 0.491 | lipid droplet assembly factor 1 |  |
| [[CYB561D1]] | 0.491 | cytochrome b561 family member D1 |  |
| [[BTBD6]] | 0.488 | BTB domain containing 6 |  |
| [[NUDT8]] | 0.486 | nudix hydrolase 8 |  |
| [[ZNF565]] | 0.483 | zinc finger protein 565 |  |
| [[FGFR1OP2]] | 0.480 | FGFR1 oncogene partner 2 |  |
| [[PSMA7]] | 0.479 | proteasome 20S subunit alpha 7 |  |
| [[PDCD5]] | 0.476 | programmed cell death 5 |  |
| [[VAMP8]] | 0.472 | vesicle associated membrane protein 8 |  |
| [[ACADS]] | 0.472 | acyl-CoA dehydrogenase short chain |  |
| [[AMBRA1]] | 0.469 | autophagy and beclin 1 regulator 1 |  |
| [[TST]] | 0.468 | thiosulfate sulfurtransferase |  |
| [[TNFRSF10A-DT]] | 0.467 | TNFRSF10A divergent transcript |  |
| [[HES6]] | 0.462 | hes family bHLH transcription factor 6 |  |
| [[MICU1]] | 0.461 | mitochondrial calcium uptake 1 |  |
| [[FIS1]] | 0.456 | fission, mitochondrial 1 |  |
| [[CLDN12]] | 0.452 | claudin 12 |  |
| [[NDUFA6]] | 0.445 | NADH:ubiquinone oxidoreductase subunit A6 |  |
| [[LINC00847]] | 0.440 | long independently transcribed non-coding RNA 847 |  |
| [[RAB33B-AS1]] | 0.437 | RAB33B antisense RNA 1 |  |
| [[COPRS]] | 0.436 | coordinator of PRMT5 and differentiation stimulator |  |
| [[RNASEK]] | 0.422 | ribonuclease K |  |
| [[LONRF1]] | 0.421 | LON peptidase N-terminal domain and ring finger 1 |  |
| [[UMAD1]] | 0.421 | UBAP1-MVB12-associated (UMA) domain containing 1 |  |
| [[DBNDD2]] | 0.420 | dysbindin domain containing 2 |  |
| [[ACVR2A]] | 0.408 | activin A receptor type 2A |  |
| [[PPP3CC]] | 0.407 | protein phosphatase 3 catalytic subunit gamma |  |
| [[PSMG3]] | 0.397 | proteasome assembly chaperone 3 |  |
| [[SMIM30]] | 0.373 | small integral membrane protein 30 |  |
| [[ABHD14A]] | 0.349 | abhydrolase domain containing 14A |  |
| [[NOA1]] | 0.347 | nitric oxide associated 1 |  |
| [[OCIAD2]] | 0.340 | OCIA domain containing 2 |  |
| [[HABP4]] | 0.336 | hyaluronan binding protein 4 |  |
| [[NMT2]] | 0.325 | N-myristoyltransferase 2 |  |
| [[MAP2K4]] | 0.289 | mitogen-activated protein kinase kinase 4 |  |
| [[POLR2J3-1]] | 0.284 | — |  |
| [[MIR181A1HG]] | 0.282 | MIR181A1 host gene |  |
| [[RNPEPL1]] | 0.277 | arginyl aminopeptidase like 1 |  |
| [[SYNGR2]] | 0.232 | synaptogyrin 2 |  |
| [[CNPPD1]] | 0.221 | cyclin Pas1/PHO80 domain containing 1 |  |

## − arm (11)

| Gene | Projection | Name | Alert |
|---|---|---|---|
| [[MAPRE1]] | -0.761 | microtubule associated protein RP/EB family member 1 |  |
| [[DARS2]] | -0.719 | aspartyl-tRNA synthetase 2, mitochondrial |  |
| [[SLC25A24]] | -0.646 | solute carrier family 25 member 24 |  |
| [[JPT2]] | -0.608 | Jupiter microtubule associated homolog 2 |  |
| [[COPS3]] | -0.522 | COP9 signalosome subunit 3 |  |
| [[SLC35F6]] | -0.512 | solute carrier family 35 member F6 |  |
| [[ACTR2]] | -0.494 | actin related protein 2 |  |
| [[ADGRG6]] | -0.494 | adhesion G protein-coupled receptor G6 |  |
| [[HIGD1A]] | -0.415 | HIG1 hypoxia inducible domain family member 1A |  |
| [[BMS1P23]] | -0.303 | BMS1 pseudogene 23 |  |
| [[ETFA]] | -0.0111 | electron transfer flavoprotein subunit alpha |  |

## Data

- `graph/nodes.parquet` — module == 24; `graph/modules.parquet` — module == 24; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [23] (drug-dose × line)
