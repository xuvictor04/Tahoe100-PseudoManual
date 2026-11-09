---
module: 29
type: "module"
n_genes: 148
n_plus: 121
n_minus: 27
arms_opposite: true
mean_cos_between_arms: -0.3057727515697479
label: "Neutrophil degranulation"
label_source: "reactome"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 029

*Neutrophil degranulation · 148 genes (121 in the + arm, 27 in the − arm) · [[Module 029.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31). The + arm rises where the − arm falls. Arm = the side of the module's main direction a gene sits on.

Label from the validation stage: **Neutrophil degranulation** (reactome, q 7e-07; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| + | Neutrophil degranulation | reactome | 18/121 | 6.09 | 7e-07 |
| all | Neutrophil degranulation | reactome | 18/148 | 4.98 | 2e-05 |
| + | Innate Immune System | reactome | 20/121 | 3.21 | 0.002 |
| all | Innate Immune System | reactome | 20/148 | 2.62 | 0.028 |

## Drugs that move it

*Mean pooled z of the + arm minus the − arm (`graph/module_pooled_z.npy`, row 28), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it (+ arm up, − arm down): [[Dinaciclib (drug)]] 0.5 µM (+11.0, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (+9.5, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+8.5, ⚠ toxic; transcription drop; cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (+5.6, ⚠ cell-cycle shift); [[Epirubicin (hydrochloride) (drug)]] 5 µM (+3.9, ⚠ cell-cycle shift); [[Selinexor (drug)]] 5 µM (+3.8, ⚠ cell-cycle shift); [[TAK-901 (drug)]] 5 µM (+3.7, ⚠ cell-cycle shift); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (+3.3, ⚠ cell-cycle shift); [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM (+3.3); [[PH-797804 (drug)]] 5 µM (+2.8); [[Anethole trithione (drug)]] 0.5 µM (+2.7); [[Erlotinib (drug)]] 0.05 µM (+2.6); [[Benproperine (phosphate) (drug)]] 0.05 µM (+2.5); [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM (+2.5); [[Fenofibrate (drug)]] 0.05 µM (+2.3); [[Lucanthone (drug)]] 0.05 µM (+2.2); [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM (+2.2); [[Pyridoxine (hydrochloride) (drug)]] 5 µM (+2.2) (109 in all, 21 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)
- Lower it: [[Homoharringtonine (drug)]] 5 µM (-17.7, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-10.7, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-9.5, ⚠ cell-cycle shift); [[Ipatasertib (drug)]] 0.5 µM (-4.7); [[Harringtonine (drug)]] 0.5 µM (-4.0, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.05 µM (-3.2); [[Celecoxib (drug)]] 0.5 µM (-3.1); [[5-Azacytidine (drug)]] 5 µM (-2.7); [[BAY1125976 (drug)]] 0.5 µM (-2.6); [[Sapanisertib (drug)]] 0.5 µM (-2.5); [[Methylprednisolone succinate (drug)]] 0.5 µM (-2.5); [[PH-797804 (drug)]] 0.5 µM (-2.5); [[Thymol (drug)]] 0.5 µM (-2.5); [[Docetaxel (Trihydrate) (drug)]] 0.5 µM (-2.4) (110 in all, 21 with an alert ⚠; shown: the 10 strongest and the 4 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[PANC-1 (line)]], [[NCI-H460 (line)]], [[A-172 (line)]], [[A498 (line)]], [[NCI-H1573 (line)]], [[HOP62 (line)]], [[HEC-1-A (line)]], [[SW480 (line)]]

*⚠ 3 of its 148 genes are in the vector space only through drug-doses that carry an alert (`embed/genes.parquet` evidence_flagged_only): their place here may reflect what those drug-doses did to the cells. They are marked in the tables of this note.*

## + arm (121)

| Gene | Projection | Name | Alert |
|---|---|---|---|
| [[PPT1]] | 0.884 | palmitoyl-protein thioesterase 1 |  |
| [[SCARB2]] | 0.838 | scavenger receptor class B member 2 |  |
| [[CRTAP]] | 0.836 | cartilage associated protein |  |
| [[FKBP9]] | 0.821 | FKBP prolyl isomerase 9 |  |
| [[TMEM123]] | 0.814 | transmembrane protein 123 |  |
| [[TMEM30A]] | 0.808 | cell division cycle 50 P4-ATPase accessory subunit A |  |
| [[PRDX3]] | 0.800 | peroxiredoxin 3 |  |
| [[FUCA2]] | 0.798 | alpha-L-fucosidase 2 |  |
| [[ERMP1]] | 0.795 | endoplasmic reticulum metallopeptidase 1 |  |
| [[TMX1]] | 0.784 | thioredoxin related transmembrane protein 1 |  |
| [[CIPC]] | 0.771 | CLOCK interacting pacemaker |  |
| [[PGRMC1]] | 0.769 | progesterone receptor membrane component 1 |  |
| [[TSPAN6]] | 0.767 | tetraspanin 6 |  |
| [[PGAM1]] | 0.763 | phosphoglycerate mutase 1 |  |
| [[DDOST]] | 0.752 | dolichyl-diphosphooligosaccharide--protein glycosyltransferase non-catalytic subunit |  |
| [[STRADB]] | 0.744 | STE20 related adaptor beta |  |
| [[SH3BGRL]] | 0.735 | SH3 domain binding glutamate rich protein like |  |
| [[ATRAID]] | 0.734 | all-trans retinoic acid induced differentiation factor |  |
| [[LAMP2]] | 0.730 | lysosome associated membrane protein 2 |  |
| [[CMPK1]] | 0.728 | cytidine/uridine monophosphate kinase 1 |  |
| [[PON2]] | 0.726 | paraoxonase 2 |  |
| [[PPP2R1B]] | 0.722 | protein phosphatase 2 scaffold subunit Abeta |  |
| [[STT3B]] | 0.721 | STT3 oligosaccharyltransferase complex catalytic subunit B |  |
| [[SUMO3]] | 0.719 | small ubiquitin like modifier 3 |  |
| [[EMB]] | 0.716 | embigin |  |
| [[ITM2B]] | 0.713 | integral membrane protein 2B |  |
| [[PIGK]] | 0.709 | phosphatidylinositol glycan anchor biosynthesis class K |  |
| [[ATP5F1B]] | 0.705 | ATP synthase F1 subunit beta |  |
| [[PLBD1]] | 0.702 | phospholipase B domain containing 1 |  |
| [[BANF1]] | 0.700 | barrier to autointegration nuclear assembly factor 1 |  |
| [[GNS]] | 0.698 | glucosamine (N-acetyl)-6-sulfatase |  |
| [[SCP2]] | 0.696 | sterol carrier protein 2 |  |
| [[PTGFRN]] | 0.690 | prostaglandin F2 receptor inhibitor |  |
| [[LANCL1]] | 0.676 | LanC like glutathione S-transferase 1 |  |
| [[LAPTM4B]] | 0.668 | lysosomal protein transmembrane 4 beta |  |
| [[FAM210B]] | 0.666 | mitochondrial inner membrane structural 2 |  |
| [[CREG1]] | 0.664 | cellular repressor of E1A stimulated genes 1 |  |
| [[CNOT1]] | 0.659 | CCR4-NOT transcription complex subunit 1 |  |
| [[ATP5F1A]] | 0.659 | ATP synthase F1 subunit alpha |  |
| [[CNN3]] | 0.653 | calponin 3 |  |
| [[CD99L2]] | 0.640 | CD99 molecule like 2 |  |
| [[SUMF2]] | 0.639 | sulfatase modifying factor 2 |  |
| [[IL13RA1]] | 0.628 | interleukin 13 receptor subunit alpha 1 |  |
| [[GOLM1]] | 0.627 | golgi membrane protein 1 |  |
| [[MDH2]] | 0.617 | malate dehydrogenase 2 |  |
| [[ADAM9]] | 0.617 | ADAM metallopeptidase domain 9 |  |
| [[FKBP1A]] | 0.615 | FKBP prolyl isomerase 1A |  |
| [[CUL2]] | 0.614 | cullin 2 |  |
| [[ARF3]] | 0.612 | ARF GTPase 3 |  |
| [[APP]] | 0.610 | amyloid beta precursor protein |  |
| [[GPC4]] | 0.608 | glypican 4 |  |
| [[FSTL1]] | 0.607 | follistatin like 1 |  |
| [[HIPK1]] | 0.604 | homeodomain interacting protein kinase 1 |  |
| [[ZMYM3]] | 0.603 | zinc finger MYM-type containing 3 |  |
| [[GSTK1]] | 0.602 | glutathione S-transferase kappa 1 |  |
| [[PRCP]] | 0.597 | prolylcarboxypeptidase |  |
| [[TMEM19]] | 0.597 | fatty acid amide binding transmembrane protein |  |
| [[SLC39A6]] | 0.596 | solute carrier family 39 member 6 |  |
| [[CDKN2AIPNL]] | 0.596 | XRN2 binding domain containing 1 |  |
| [[M6PR]] | 0.591 | mannose-6-phosphate receptor, cation dependent |  |
| [[MSL3]] | 0.588 | MSL complex subunit 3 |  |
| [[CIAO2A]] | 0.588 | cytosolic iron-sulfur assembly component 2A |  |
| [[ANP32A]] | 0.576 | acidic nuclear phosphoprotein 32 family member A |  |
| [[CD164]] | 0.570 | CD164 molecule |  |
| [[LRP11]] | 0.569 | LDL receptor related protein 11 |  |
| [[MFSD14A]] | 0.564 | solute carrier family 71 member 1 |  |
| [[SELENOF]] | 0.561 | selenoprotein F |  |
| [[ABHD14B]] | 0.554 | abhydrolase domain containing 14B |  |
| [[PPIC]] | 0.553 | peptidylprolyl isomerase C |  |
| [[GTF2I]] | 0.551 | general transcription factor IIi |  |
| [[CUL4B]] | 0.550 | cullin 4B |  |
| [[CDIPT]] | 0.533 | CDP-diacylglycerol--inositol 3-phosphatidyltransferase |  |
| [[PPM1A]] | 0.533 | protein phosphatase, Mg2+/Mn2+ dependent 1A |  |
| [[C1GALT1C1]] | 0.528 | C1GALT1 specific chaperone 1 |  |
| [[SEPHS1]] | 0.523 | selenophosphate synthetase 1 |  |
| [[DERA]] | 0.518 | deoxyribose-phosphate aldolase |  |
| [[PYURF]] | 0.514 | PIGY upstream open reading frame |  |
| [[THAP12]] | 0.514 | THAP domain containing 12 |  |
| [[PCDHB2]] | 0.512 | protocadherin beta 2 |  |
| [[MSI2]] | 0.510 | musashi RNA binding protein 2 |  |
| [[MINDY1]] | 0.504 | MINDY lysine 48 deubiquitinase 1 |  |
| [[AK3]] | 0.498 | adenylate kinase 3 |  |
| [[CYBRD1]] | 0.494 | cytochrome b reductase 1 |  |
| [[NME4]] | 0.490 | NME/NM23 nucleoside diphosphate kinase 4 |  |
| [[ARHGDIB]] | 0.487 | Rho GDP dissociation inhibitor beta |  |
| [[HINT3]] | 0.486 | histidine triad nucleotide binding protein 3 |  |
| [[G6PC3]] | 0.484 | glucose-6-phosphatase catalytic subunit 3 |  |
| [[CTSH]] | 0.482 | cathepsin H |  |
| [[SYPL1]] | 0.482 | synaptophysin like 1 |  |
| [[PGM1]] | 0.479 | phosphoglucomutase 1 |  |
| [[CYB5B]] | 0.478 | cytochrome b5 type B |  |
| [[CISD2]] | 0.472 | CDGSH iron sulfur domain 2 |  |
| [[PARK7]] | 0.472 | Parkinsonism associated deglycase | ⚠ only flagged evidence |
| [[CPVL]] | 0.470 | carboxypeptidase vitellogenic like |  |
| [[RAB14]] | 0.469 | RAB14, member RAS oncogene family |  |
| [[UQCRC1]] | 0.465 | ubiquinol-cytochrome c reductase core protein 1 | ⚠ only flagged evidence |
| [[ZNF410]] | 0.460 | zinc finger protein 410 |  |
| [[PDZD8]] | 0.460 | PDZ domain containing 8 |  |
| [[RAB11FIP2]] | 0.458 | RAB11 family interacting protein 2 |  |
| [[TMEM9B]] | 0.449 | TMEM9 domain family member B |  |
| [[SMAD6]] | 0.449 | SMAD family member 6 |  |
| [[AGA]] | 0.448 | aspartylglucosaminidase |  |
| [[GNG10]] | 0.436 | G protein subunit gamma 10 |  |
| [[ARL2]] | 0.436 | ARF like GTPase 2 |  |
| [[PCGF5]] | 0.429 | polycomb group ring finger 5 |  |
| [[OXA1L]] | 0.429 | OXA1L mitochondrial inner membrane insertase |  |
| [[SETD7]] | 0.425 | SET domain containing 7, histone lysine methyltransferase |  |
| [[SNRPG]] | 0.424 | small nuclear ribonucleoprotein polypeptide G |  |
| [[MRPS30-DT]] | 0.413 | MRPS30 divergent transcript |  |
| [[PRDX6]] | 0.411 | peroxiredoxin 6 |  |
| [[HADHA]] | 0.411 | hydroxyacyl-CoA dehydrogenase trifunctional multienzyme complex subunit alpha |  |
| [[UCP2]] | 0.384 | uncoupling protein 2 |  |
| [[KIAA1191]] | 0.378 | KIAA1191 |  |
| [[JMJD8]] | 0.368 | jumonji domain containing 8 |  |
| [[SP1]] | 0.357 | Sp1 transcription factor |  |
| [[OAZ2]] | 0.356 | ornithine decarboxylase antizyme 2 |  |
| [[ZNF852]] | 0.356 | zinc finger protein 852 |  |
| [[CPNE3]] | 0.335 | copine 3 |  |
| [[HEXB]] | 0.324 | hexosaminidase subunit beta |  |
| [[ANAPC15]] | 0.321 | anaphase promoting complex subunit 15 |  |
| [[RAB27A]] | 0.313 | RAB27A, member RAS oncogene family |  |

## − arm (27)

| Gene | Projection | Name | Alert |
|---|---|---|---|
| [[ATF4]] | -0.743 | activating transcription factor 4 |  |
| [[ZNF316]] | -0.699 | zinc finger protein 316 |  |
| [[WASHC1]] | -0.696 | WASH complex subunit 1 |  |
| [[FBXL6]] | -0.691 | F-box and leucine rich repeat protein 6 |  |
| [[EIF5B]] | -0.668 | eukaryotic translation initiation factor 5B |  |
| [[AK6]] | -0.661 | adenylate kinase 6 |  |
| [[PPP1R35]] | -0.657 | protein phosphatase 1 regulatory subunit 35 | ⚠ only flagged evidence |
| [[NPIPP1]] | -0.653 | nuclear pore complex interacting protein pseudogene 1 |  |
| [[LIME1]] | -0.636 | Lck interacting transmembrane adaptor 1 |  |
| [[LCAT]] | -0.625 | lecithin-cholesterol acyltransferase |  |
| [[PLEKHN1]] | -0.584 | pleckstrin homology domain containing N1 |  |
| [[ARRDC2]] | -0.562 | arrestin domain containing 2 |  |
| [[BCAT2]] | -0.556 | branched chain amino acid transaminase 2 |  |
| [[BCAR1]] | -0.553 | BCAR1 scaffold protein, Cas family member |  |
| [[TBRG1]] | -0.553 | FYRN and FYRC domains INO80 complex interactor 1 |  |
| [[PILRB]] | -0.549 | paired immunoglobin like type 2 receptor beta |  |
| [[CDK3]] | -0.542 | cyclin dependent kinase 3 |  |
| [[ORAI1]] | -0.517 | ORAI calcium release-activated calcium modulator 1 |  |
| [[SEMA4C]] | -0.505 | semaphorin 4C |  |
| [[GADD45A]] | -0.500 | growth arrest and DNA damage inducible alpha |  |
| [[SMG9]] | -0.496 | SMG9 nonsense mediated mRNA decay factor |  |
| [[DHRSX]] | -0.488 | dehydrogenase/reductase X-linked |  |
| [[GCDH]] | -0.487 | glutaryl-CoA dehydrogenase |  |
| [[HOMER3]] | -0.464 | homer scaffold protein 3 |  |
| [[NUDT4]] | -0.450 | nudix hydrolase 4 |  |
| [[MROH6]] | -0.425 | maestro heat like repeat family member 6 |  |
| [[MAPKBP1]] | -0.394 | mitogen-activated protein kinase binding protein 1 |  |

## Data

- `graph/nodes.parquet` — module == 29; `graph/modules.parquet` — module == 29; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [28] (drug-dose × line)
