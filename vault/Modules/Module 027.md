---
module: 27
type: "module"
n_genes: 155
n_plus: 155
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.23795601725578308
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 027

*155 genes (single-armed) · [[Module 027.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 26), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Dinaciclib (drug)]] 5 µM (+9.2, ⚠ toxic; transcription drop; cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (+9.1, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (+8.4, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+6.5, ⚠ toxic; transcription drop; cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (+5.4); [[Homoharringtonine (drug)]] 5 µM (+3.9, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 0.5 µM (+3.3, ⚠ cell-cycle shift); [[Docetaxel (drug)]] 0.05 µM (+2.7, ⚠ transcription drop; cell-cycle shift); [[Selinexor (drug)]] 5 µM (+2.7, ⚠ cell-cycle shift); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+2.2); [[Ponatinib (drug)]] 0.5 µM (+2.2); [[Ipatasertib (drug)]] 0.5 µM (+2.1); [[XRK3F2 (drug)]] 0.5 µM (+2.1); [[Cobimetinib (drug)]] 5 µM (+2.0); [[Ponatinib (drug)]] 5 µM (+1.9); [[Trametinib (drug)]] 0.5 µM (+1.9); [[Entrectinib (drug)]] 5 µM (+1.9); [[Bimiralisib (drug)]] 0.5 µM (+1.7) (76 in all, 23 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)
- Lower it: [[Digitoxin (drug)]] 0.5 µM (-3.5, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (-2.6, ⚠ cell-cycle shift); [[Mebendazole (drug)]] 5 µM (-2.2); [[Digitoxin (drug)]] 0.05 µM (-2.0, ⚠ cell-cycle shift); [[Daptomycin (drug)]] 0.5 µM (-1.6, ⚠ unreliable plate only); [[Artesunate (drug)]] 0.5 µM (-1.6); [[Ouabain (Octahydrate) (drug)]] 0.05 µM (-1.6, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (-1.6, ⚠ cell-cycle shift); [[Daptomycin (drug)]] 5 µM (-1.6, ⚠ unreliable plate only); [[c-Kit-IN-1 (drug)]] 0.05 µM (-1.6, ⚠ unreliable plate only); [[Ixazomib citrate (drug)]] 0.5 µM (-1.6); [[Lucanthone (drug)]] 0.05 µM (-1.6); [[Rutin (trihydrate) (drug)]] 0.05 µM (-1.4); [[5-Azacytidine (drug)]] 5 µM (-1.4); [[(S)-Crizotinib (drug)]] 0.05 µM (-1.4); [[Clopidogrel (drug)]] 0.05 µM (-1.4); [[Pravastatin (sodium) (drug)]] 5 µM (-1.4); [[Diphenhydramine (drug)]] 0.05 µM (-1.4) (50 in all, 12 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[COLO 205 (line)]], [[SNU-1 (line)]], [[NCI-H23 (line)]], [[SW480 (line)]], [[SHP-77 (line)]], [[A-427 (line)]], [[SW48 (line)]], [[SK-MEL-2 (line)]]

## + arm (155)

| Gene | Projection | Name |
|---|---|---|
| [[B3GAT1-DT]] | 0.854 | B3GAT1 divergent transcript |
| [[PKHD1]] | 0.846 | PKHD1 ciliary IPT domain containing fibrocystin/polyductin |
| [[LINC02058]] | 0.841 | long independently transcribed non-coding RNA 2058 |
| [[ST18]] | 0.840 | ST18 C2H2C-type zinc finger transcription factor |
| [[APCDD1]] | 0.840 | APC down-regulated 1 |
| [[SMOC2]] | 0.829 | SPARC related modular calcium binding 2 |
| [[AXIN2]] | 0.811 | axin 2 |
| [[JAKMIP2-AS1]] | 0.805 | JAKMIP2 antisense RNA 1 |
| [[VWA2]] | 0.786 | von Willebrand factor A domain containing 2 |
| [[PROX1-AS1]] | 0.780 | PROX1 antisense RNA 1 |
| [[LINC01622]] | 0.778 | long independently transcribed non-coding RNA 1622 |
| [[CHDH]] | 0.763 | choline dehydrogenase |
| [[LINC02254]] | 0.760 | — |
| [[FGF20]] | 0.759 | fibroblast growth factor 20 |
| [[LINC02253]] | 0.757 | long independently transcribed non-coding RNA 2253 |
| [[IGFL4]] | 0.750 | IGF like family member 4 |
| [[RMST]] | 0.748 | rhabdomyosarcoma 2 associated transcript |
| [[HS3ST5]] | 0.736 | heparan sulfate-glucosamine 3-sulfotransferase 5 |
| [[PROX1]] | 0.733 | prospero homeobox 1 |
| [[RIMBP2]] | 0.724 | RIMS binding protein 2 |
| [[LINC02466]] | 0.721 | long independently transcribed non-coding RNA 2466 |
| [[A1CF]] | 0.719 | APOBEC1 complementation factor |
| [[LINC01980]] | 0.719 | long independently transcribed non-coding RNA 1980 |
| [[PDK4-AS1]] | 0.719 | PDK4 antisense RNA 1 |
| [[NKD1]] | 0.719 | NKD inhibitor of Wnt signaling pathway 1 |
| [[LINC00299]] | 0.719 | long independently transcribed non-coding RNA 299 |
| [[F10]] | 0.718 | coagulation factor X |
| [[LINC01814]] | 0.714 | — |
| [[DIP2C-AS1]] | 0.714 | DIP2C antisense RNA 1 |
| [[PSD2]] | 0.713 | pleckstrin and Sec7 domain containing 2 |
| [[GJB1]] | 0.711 | gap junction protein beta 1 |
| [[SLC30A10]] | 0.711 | solute carrier family 30 member 10 |
| [[LINC01748]] | 0.710 | long independently transcribed non-coding RNA 1748 |
| [[NOTUM]] | 0.707 | notum, palmitoleoyl-protein carboxylesterase |
| [[RHOXF1-AS1]] | 0.706 | RHOXF1 antisense RNA 1 |
| [[BANK1]] | 0.704 | B cell scaffold protein with ankyrin repeats 1 |
| [[FGD3]] | 0.704 | FYVE, RhoGEF and PH domain containing 3 |
| [[LINC01611]] | 0.691 | long independently transcribed non-coding RNA 1611 |
| [[TMEM139]] | 0.688 | transmembrane protein 139 |
| [[LINC01091]] | 0.687 | long independently transcribed non-coding RNA 1091 |
| [[PHYHIPL]] | 0.679 | phytanoyl-CoA 2-hydroxylase interacting protein like |
| [[VIL1]] | 0.679 | villin 1 |
| [[ARHGAP25]] | 0.676 | Rho GTPase activating protein 25 |
| [[MIR4500HG]] | 0.675 | MIR4500 host gene |
| [[LINC00649]] | 0.672 | long independently transcribed non-coding RNA 649 |
| [[FGD5]] | 0.666 | FYVE, RhoGEF and PH domain containing 5 |
| [[LINC02981]] | 0.661 | long independently transcribed non-coding RNA 2981 |
| [[LINC00491]] | 0.660 | long independently transcribed non-coding RNA 491 |
| [[SORL1]] | 0.660 | sortilin related receptor 1 |
| [[NCALD]] | 0.653 | neurocalcin delta |
| [[LINC01876]] | 0.652 | long independently transcribed non-coding RNA 1876 |
| [[NIHCOLE]] | 0.642 | ncRNA involved in NHEJ oncogenic ligation efficiency |
| [[CCR3]] | 0.637 | C-C motif chemokine receptor 3 |
| [[MIR3667HG]] | 0.636 | MIR3667 host gene |
| [[ASB4]] | 0.635 | ankyrin repeat and SOCS box containing 4 |
| [[SHISA9]] | 0.634 | shisa family member 9 |
| [[NMNAT3]] | 0.631 | nicotinamide nucleotide adenylyltransferase 3 |
| [[NDUFA4L2]] | 0.627 | cytochrome c oxidase hypoxia associated subunit FA4L2 |
| [[SLCO6A1]] | 0.627 | solute carrier organic anion transporter family member 6A1 |
| [[MIR4713HG]] | 0.627 | MIR4713 host gene |
| [[SERPINF1]] | 0.626 | serpin family F member 1 |
| [[DACH1]] | 0.625 | dachshund family transcription factor 1 |
| [[CDX2]] | 0.624 | caudal type homeobox 2 |
| [[HUNK]] | 0.619 | hormonally up-regulated Neu-associated kinase |
| [[ILDR1]] | 0.618 | immunoglobulin like domain containing receptor 1 |
| [[DLEU1]] | 0.611 | deleted in lymphocytic leukemia 1 |
| [[GLDN]] | 0.611 | gliomedin |
| [[GPR143]] | 0.604 | G protein-coupled receptor 143 |
| [[LINC03042]] | 0.604 | long independently transcribed non-coding RNA 3042 |
| [[LINC02428]] | 0.594 | long independently transcribed non-coding RNA 2428 |
| [[F5]] | 0.589 | coagulation factor V |
| [[KSR2]] | 0.587 | kinase suppressor of ras 2 |
| [[ZNF703]] | 0.581 | zinc finger protein 703 |
| [[ZNF69]] | 0.580 | zinc finger protein 69 |
| [[LINC02315]] | 0.578 | long independently transcribed non-coding RNA 2315 |
| [[POU3F2]] | 0.577 | POU class 3 homeobox 2 |
| [[PSG1]] | 0.570 | pregnancy specific beta-1-glycoprotein 1 |
| [[DCDC2]] | 0.563 | doublecortin domain containing 2 |
| [[LINC02832]] | 0.554 | long independently transcribed non-coding RNA 2832 |
| [[MAP2K6]] | 0.552 | mitogen-activated protein kinase kinase 6 |
| [[LYPLAL1-AS1]] | 0.549 | LYPLAL1 antisense RNA 1 |
| [[TMEM184A]] | 0.540 | transmembrane protein 184A |
| [[MKX]] | 0.539 | mohawk homeobox |
| [[RGCC]] | 0.534 | regulator of cell cycle |
| [[C11orf52]] | 0.533 | chromosome 11 open reading frame 52 |
| [[TRPV4]] | 0.532 | transient receptor potential cation channel subfamily V member 4 |
| [[GABRG2]] | 0.531 | gamma-aminobutyric acid type A receptor subunit gamma2 |
| [[LINC00923]] | 0.528 | long independently transcribed non-coding RNA 923 |
| [[COLGALT2]] | 0.523 | collagen beta(1-O)galactosyltransferase 2 |
| [[ANO4]] | 0.521 | anoctamin 4 |
| [[LINC02050]] | 0.517 | long independently transcribed non-coding RNA 2050 |
| [[SLC44A5]] | 0.516 | solute carrier family 44 member 5 |
| [[DMTN]] | 0.512 | dematin actin binding protein |
| [[BAMBI]] | 0.508 | BMP and activin membrane bound inhibitor |
| [[LINC02940]] | 0.508 | long independently transcribed non-coding RNA 2940 |
| [[TRPM2-AS]] | 0.507 | TRPM2 antisense RNA |
| [[LARGE2]] | 0.504 | LARGE xylosyl- and glucuronyltransferase 2 |
| [[MAN1A1]] | 0.500 | mannosidase alpha class 1A member 1 |
| [[DNAH6]] | 0.499 | dynein axonemal heavy chain 6 |
| [[FKBP9P1]] | 0.496 | FKBP prolyl isomerase 9 pseudogene 1 |
| [[CPLX2]] | 0.494 | complexin 2 |
| [[MIR2052HG]] | 0.493 | MIR2052 host gene |
| [[FGF19]] | 0.491 | fibroblast growth factor 19 |
| [[FCGRT]] | 0.490 | Fc gamma receptor and transporter |
| [[ROBO2]] | 0.485 | roundabout guidance receptor 2 |
| [[SPINK5]] | 0.482 | serine peptidase inhibitor Kazal type 5 |
| [[ADRA2C]] | 0.482 | adrenoceptor alpha 2C |
| [[YWHAEP7-1]] | 0.480 | — |
| [[KRT5]] | 0.478 | keratin 5 |
| [[LINC00992]] | 0.474 | long independently transcribed non-coding RNA 992 |
| [[STK31]] | 0.464 | serine/threonine kinase 31 |
| [[PWWP3B]] | 0.464 | PWWP domain containing 3B |
| [[SLC25A25-AS1]] | 0.463 | SLC25A25 antisense RNA 1 |
| [[LRRTM4]] | 0.459 | leucine rich repeat transmembrane neuronal 4 |
| [[HNF1A]] | 0.458 | HNF1 homeobox A |
| [[PDE11A]] | 0.458 | phosphodiesterase 11A |
| [[PPM1H]] | 0.457 | protein phosphatase, Mg2+/Mn2+ dependent 1H |
| [[PAQR8]] | 0.453 | progestin and adipoQ receptor family member 8 |
| [[EPHX4]] | 0.452 | epoxide hydrolase 4 |
| [[PASD1]] | -0.452 | PAS domain containing repressor 1 |
| [[NEK5]] | 0.452 | NIMA related kinase 5 |
| [[LINC01551]] | 0.450 | long independently transcribed non-coding RNA 1551 |
| [[SLC25A24P1]] | 0.448 | SLC25A24 pseudogene 1 |
| [[BMP7]] | 0.447 | bone morphogenetic protein 7 |
| [[MYRIP]] | 0.447 | myosin VIIA and Rab interacting protein |
| [[RAB17]] | 0.446 | RAB17, member RAS oncogene family |
| [[IL17RB]] | 0.441 | interleukin 17 receptor B |
| [[DNAH7]] | 0.429 | dynein axonemal heavy chain 7 |
| [[LINC02147]] | 0.420 | long independently transcribed non-coding RNA 2147 |
| [[HEPHL1]] | 0.419 | hephaestin like 1 |
| [[MPP7]] | 0.418 | MAGUK p55 scaffold protein 7 |
| [[LINC02964]] | 0.411 | long independently transcribed non-coding RNA 2964 |
| [[ENPP5]] | 0.406 | ectonucleotide pyrophosphatase/phosphodiesterase family member 5 |
| [[LINC01905]] | 0.405 | long independently transcribed non-coding RNA 1905 |
| [[GNAT3]] | 0.402 | G protein subunit alpha transducin 3 |
| [[CACNA1D]] | 0.401 | calcium voltage-gated channel subunit alpha1 D |
| [[APOB]] | 0.399 | apolipoprotein B |
| [[SCN5A]] | 0.394 | sodium voltage-gated channel alpha subunit 5 |
| [[CFAP298-TCP10L]] | 0.392 | CFAP298-TCP10L readthrough |
| [[SCNN1A]] | 0.389 | sodium channel epithelial 1 subunit alpha |
| [[GPR15]] | 0.347 | G protein-coupled receptor 15 |
| [[SLC24A3]] | 0.341 | solute carrier family 24 member 3 |
| [[P4HTM]] | 0.339 | prolyl 4-hydroxylase, transmembrane |
| [[CDK15]] | 0.331 | cyclin dependent kinase 15 |
| [[GOLGA2P5]] | 0.322 | GOLGA2 pseudogene 5 |
| [[LINC02999]] | 0.317 | long independently transcribed non-coding RNA 2999 |
| [[LNCAROD]] | 0.315 | lncRNA activating regulator of DKK1 |
| [[SERPINI1]] | 0.313 | serpin family I member 1 |
| [[ERBB2]] | 0.306 | erb-b2 receptor tyrosine kinase 2 |
| [[ENPP4]] | 0.279 | ectonucleotide pyrophosphatase/phosphodiesterase 4 |
| [[PEG3]] | 0.277 | paternally expressed 3 |
| [[CAPN14]] | 0.251 | calpain 14 |
| [[LINC01456]] | 0.236 | long independently transcribed non-coding RNA 1456 |
| [[EVPL]] | 0.225 | envoplakin |
| [[CHST9]] | 0.148 | carbohydrate sulfotransferase 9 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 27; `graph/modules.parquet` — module == 27; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [26] (drug-dose × line)
