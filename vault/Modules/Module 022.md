---
module: 22
type: "module"
n_genes: 185
n_plus: 185
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.26331672072410583
label: "G2/M checkpoint"
label_source: "hallmark"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 022

*G2/M checkpoint · 185 genes (single-armed) · [[Module 022.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

Label from the validation stage: **G2/M checkpoint** (hallmark, q 9e-65; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | G2/M checkpoint | hallmark | 60/185 | 24.7 | 9e-65 |
| + | G2/M checkpoint | hallmark | 60/185 | 24.7 | 9e-65 |
| + | Cell Cycle, Mitotic | reactome | 75/185 | 12.7 | 1e-59 |
| all | Cell Cycle, Mitotic | reactome | 75/185 | 12.7 | 1e-59 |
| all | Cell Cycle | reactome | 79/185 | 10.6 | 7e-57 |
| + | Cell Cycle | reactome | 79/185 | 10.6 | 7e-57 |
| + | M Phase | reactome | 61/185 | 14.8 | 5e-51 |
| all | M Phase | reactome | 61/185 | 14.8 | 5e-51 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 21), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Homoharringtonine (drug)]] 5 µM (+8.7, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (+4.5, ⚠ cell-cycle shift); [[Docetaxel (drug)]] 0.05 µM (+4.5, ⚠ transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (+4.4, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (+4.1, ⚠ toxic; transcription drop; cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (+4.0, ⚠ cell-cycle shift); [[Darinaparsin (drug)]] 5 µM (+3.7, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 5 µM (+3.4, ⚠ toxic; transcription drop; cell-cycle shift); [[NG25 (drug)]] 5 µM (+3.0, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 0.05 µM (+2.9, ⚠ cell-cycle shift); [[Docetaxel (drug)]] 5 µM (+2.1); [[Vinblastine (sulfate) (drug)]] 0.05 µM (+1.9); [[Mebendazole (drug)]] 0.5 µM (+1.9); [[Mebendazole (drug)]] 5 µM (+1.8); [[Retinoic acid (drug)]] 0.05 µM (+1.7); [[Peretinoin (drug)]] 0.05 µM (+1.7); [[Peretinoin (drug)]] 0.5 µM (+1.6); [[Berbamine (drug)]] 0.05 µM (+1.4); [[HI-TOPK-032 (drug)]] 5 µM (+1.3); [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM (+1.3) (47 in all, 29 with an alert ⚠; shown: the 10 strongest and the 10 next strongest without an alert)
- Lower it: [[Selinexor (drug)]] 5 µM (-6.1, ⚠ cell-cycle shift); [[Selinexor (drug)]] 0.5 µM (-5.6, ⚠ cell-cycle shift); [[Bortezomib (drug)]] 0.05 µM (-4.7, ⚠ cell-cycle shift); [[Ixazomib citrate (drug)]] 5 µM (-3.9, ⚠ cell-cycle shift); [[Selinexor (drug)]] 0.05 µM (-3.4, ⚠ cell-cycle shift); [[Auranofin (drug)]] 5 µM (-3.0); [[Bortezomib (drug)]] 5 µM (-2.8, ⚠ toxic; cell-cycle shift); [[Cytarabine (drug)]] 5 µM (-2.8, ⚠ cell-cycle shift); [[c-Kit-IN-1 (drug)]] 0.05 µM (-2.5, ⚠ unreliable plate only); [[Amsacrine (drug)]] 5 µM (-2.5); [[Neratinib (maleate) (drug)]] 5 µM (-2.4); [[Lactate (calcium) (drug)]] 0.5 µM (-2.0); [[EX229 (drug)]] 5 µM (-2.0); [[Cytarabine (hydrochloride) (drug)]] 0.05 µM (-1.8); [[Ixazomib citrate (drug)]] 0.5 µM (-1.7); [[Rapamycin (drug)]] 5 µM (-1.7); [[Bortezomib (drug)]] 0.5 µM (-1.7); [[Temsirolimus (drug)]] 5 µM (-1.6) (59 in all, 25 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[PANC-1 (line)]], [[A-172 (line)]], [[LOX-IMVI (line)]], [[Panc 03.27 (line)]], [[A498 (line)]], [[SW1417 (line)]], [[LS 180 (line)]], [[LoVo (line)]]

## Candidate new members

*Members not annotated to the set their arm is enriched for, ranked by mean cos to the annotated members (`validation/novel_members.csv`); ⚠ = a reason to doubt the gene's place (in the vector space only through flagged drug-doses), kept in its rank. 149 candidates, none with an alert; shown: the 15 strongest.*

| # | Gene | Set | Mean cos |
|---|---|---|---|
| 1 | [[KIF18A]] | DREAM G2/M down | +0.85 |
| 2 | [[CDCA8]] | DREAM G2/M down | +0.85 |
| 3 | [[MKI67]] | DREAM G2/M down | +0.85 |
| 4 | [[NDC80]] | DREAM G2/M down | +0.85 |
| 5 | [[CKAP2]] | DREAM G2/M down | +0.84 |
| 6 | [[ARHGAP11A]] | DREAM G2/M down | +0.84 |
| 7 | [[TROAP]] | DREAM G2/M down | +0.84 |
| 8 | [[RACGAP1]] | DREAM G2/M down | +0.83 |
| 9 | [[GTSE1]] | DREAM G2/M down | +0.83 |
| 10 | [[ASPM]] | DREAM G2/M down | +0.83 |
| 11 | [[TACC3]] | DREAM G2/M down | +0.82 |
| 12 | [[CDK1]] | DREAM G2/M down | +0.82 |
| 13 | [[DEPDC1]] | DREAM G2/M down | +0.82 |
| 14 | [[KNL1]] | DREAM G2/M down | +0.82 |
| 15 | [[KIF14]] | DREAM G2/M down | +0.82 |

## + arm (185)

| Gene | Projection | Name |
|---|---|---|
| [[TPX2]] | 0.969 | TPX2 microtubule nucleation factor |
| [[DLGAP5]] | 0.965 | DLG associated protein 5 |
| [[BIRC5]] | 0.962 | baculoviral IAP repeat containing 5 |
| [[TOP2A]] | 0.960 | DNA topoisomerase II alpha |
| [[MKI67]] | 0.959 | marker of proliferation Ki-67 |
| [[KIF23]] | 0.958 | kinesin family member 23 |
| [[NDC80]] | 0.956 | NDC80 kinetochore complex component |
| [[KIF4A]] | 0.955 | kinesin family member 4A |
| [[BUB1]] | 0.953 | BUB1 mitotic checkpoint serine/threonine kinase |
| [[KIF11]] | 0.946 | kinesin family member 11 |
| [[CCNA2]] | 0.946 | cyclin A2 |
| [[KIF2C]] | 0.944 | kinesin family member 2C |
| [[KIF18A]] | 0.943 | kinesin family member 18A |
| [[CDCA8]] | 0.942 | cell division cycle associated 8 |
| [[RACGAP1]] | 0.941 | Rac GTPase activating protein 1 |
| [[KNL1]] | 0.941 | kinetochore scaffold 1 |
| [[NCAPG]] | 0.939 | non-SMC condensin I complex subunit G |
| [[ARHGAP11A]] | 0.938 | Rho GTPase activating protein 11A |
| [[CDK1]] | 0.936 | cyclin dependent kinase 1 |
| [[PRC1]] | 0.928 | protein regulator of cytokinesis 1 |
| [[BUB1B]] | 0.927 | BUB1 mitotic checkpoint serine/threonine kinase B |
| [[GTSE1]] | 0.926 | G2 and S-phase expressed 1 |
| [[CENPF]] | 0.925 | centromere protein F |
| [[CCNB2]] | 0.925 | cyclin B2 |
| [[TACC3]] | 0.921 | transforming acidic coiled-coil containing protein 3 |
| [[CKAP2L]] | 0.918 | cytoskeleton associated protein 2L |
| [[CCNB1]] | 0.918 | cyclin B1 |
| [[NCAPD2]] | 0.917 | non-SMC condensin I complex subunit D2 |
| [[TROAP]] | 0.914 | trophinin associated protein |
| [[DEPDC1B]] | 0.914 | DEP domain containing 1B |
| [[KIF14]] | 0.913 | kinesin family member 14 |
| [[CKAP2]] | 0.911 | cytoskeleton associated protein 2 |
| [[NUSAP1]] | 0.907 | nucleolar and spindle associated protein 1 |
| [[NCAPH]] | 0.907 | non-SMC condensin I complex subunit H |
| [[NEK2]] | 0.906 | NIMA related kinase 2 |
| [[KIF15]] | 0.906 | kinesin family member 15 |
| [[INCENP]] | 0.905 | inner centromere protein |
| [[CENPE]] | 0.904 | centromere protein E |
| [[SGO1]] | 0.901 | shugoshin 1 |
| [[ASPM]] | 0.901 | assembly factor for spindle microtubules |
| [[UBE2C]] | 0.900 | ubiquitin conjugating enzyme E2 C |
| [[CDKN3]] | 0.897 | cyclin dependent kinase inhibitor 3 |
| [[CEP55]] | 0.896 | centrosomal protein 55 |
| [[PRR11]] | 0.894 | proline rich 11 |
| [[KIF20A]] | 0.893 | kinesin family member 20A |
| [[DEPDC1]] | 0.882 | DEP domain containing 1 |
| [[ANLN]] | 0.882 | anillin, actin binding protein |
| [[HJURP]] | 0.880 | Holliday junction recognition protein |
| [[SGO2]] | 0.874 | shugoshin 2 |
| [[SMC4]] | 0.873 | structural maintenance of chromosomes 4 |
| [[KNSTRN]] | 0.860 | kinetochore localized astrin (SPAG5) binding protein |
| [[AURKA]] | 0.858 | aurora kinase A |
| [[CKAP5]] | 0.854 | cytoskeleton associated protein 5 |
| [[PLK1]] | 0.853 | polo like kinase 1 |
| [[CDCA2]] | 0.849 | cell division cycle associated 2 |
| [[CCNF]] | 0.843 | cyclin F |
| [[FAM72D]] | 0.842 | RUMY family member 4 |
| [[PAK6]] | 0.841 | p21 (RAC1) activated kinase 6 |
| [[PIF1]] | 0.840 | PIF1 5'-to-3' DNA helicase |
| [[FAM83D]] | 0.836 | scaffolding CK1 anchoring protein D |
| [[PTTG1]] | 0.834 | PTTG1 regulator of sister chromatid separation, securin |
| [[SHCBP1]] | 0.827 | SHC binding and spindle associated 1 |
| [[CDC20]] | 0.826 | cell division cycle 20 |
| [[MAD2L1]] | 0.824 | mitotic arrest deficient 2 like 1 |
| [[KPNA2]] | 0.822 | karyopherin subunit alpha 2 |
| [[PSRC1]] | 0.821 | proline and serine rich coiled-coil 1 |
| [[FAM72B]] | 0.820 | RUMY family member 2 |
| [[SCLT1]] | 0.816 | sodium channel and clathrin linker 1 |
| [[GAS2L3]] | 0.816 | growth arrest specific 2 like 3 |
| [[G2E3]] | 0.807 | G2/M-phase specific E3 ubiquitin protein ligase |
| [[KIF20B]] | 0.804 | kinesin family member 20B |
| [[ECT2]] | 0.803 | epithelial cell transforming 2 |
| [[SKA3]] | 0.802 | spindle and kinetochore associated complex subunit 3 |
| [[ARHGEF39]] | 0.798 | Rho guanine nucleotide exchange factor 39 |
| [[PLK4]] | 0.797 | polo like kinase 4 |
| [[PIMREG]] | 0.791 | PICALM interacting mitotic regulator |
| [[ERCC6L]] | 0.788 | ERCC excision repair 6 like DNA helicase |
| [[CDC25C]] | 0.780 | cell division cycle 25C |
| [[HMMR]] | 0.779 | hyaluronan mediated motility receptor |
| [[LMNB1]] | 0.779 | lamin B1 |
| [[FBXO5]] | 0.774 | F-box protein 5 |
| [[GPSM2]] | 0.773 | G protein signaling modulator 2 |
| [[FOXM1]] | 0.773 | forkhead box M1 |
| [[CNTRL]] | 0.768 | centriolin |
| [[SKA1]] | 0.765 | spindle and kinetochore associated complex subunit 1 |
| [[STMN1]] | 0.762 | stathmin 1 |
| [[BUB3]] | 0.760 | BUB3 mitotic checkpoint protein |
| [[DIAPH3]] | 0.757 | diaphanous related formin 3 |
| [[CENPA]] | 0.756 | centromere protein A |
| [[FAM72A]] | 0.750 | regulator of UNG2 and MKLN1 interacting yippee protein 1 |
| [[TMPO]] | 0.746 | thymopoietin |
| [[DBF4]] | 0.736 | DBF4-CDC7 kinase regulatory subunit |
| [[H2AZ2]] | 0.730 | H2A.Z variant histone 2 |
| [[LINC01572]] | 0.724 | long independently transcribed non-coding RNA 1572 |
| [[CIP2A]] | 0.724 | cellular inhibitor of PP2A |
| [[KMT5A]] | 0.710 | lysine methyltransferase 5A |
| [[SAPCD2]] | 0.705 | suppressor APC domain containing 2 |
| [[SKA2]] | 0.703 | spindle and kinetochore associated complex subunit 2 |
| [[SPDL1]] | 0.700 | spindle apparatus coiled-coil protein 1 |
| [[MZT1]] | 0.698 | mitotic spindle organizing protein 1 |
| [[BORA]] | 0.696 | BORA aurora kinase A activator |
| [[HMGB3]] | 0.693 | high mobility group box 3 |
| [[HCCS-DT]] | 0.693 | HCCS divergent transcript |
| [[HMGB2]] | 0.681 | high mobility group box 2 |
| [[NDE1]] | 0.676 | nudE neurodevelopment protein 1 |
| [[HASPIN]] | 0.676 | histone H3 associated protein kinase |
| [[HP1BP3]] | 0.666 | heterochromatin protein 1 binding protein 3 |
| [[SMC2]] | 0.648 | structural maintenance of chromosomes 2 |
| [[MDC1]] | 0.639 | mediator of DNA damage checkpoint 1 |
| [[RNF26]] | 0.636 | ring finger protein 26 |
| [[UBE2S]] | 0.634 | ubiquitin conjugating enzyme E2 S |
| [[ARL6IP1]] | 0.634 | ARL6 interacting reticulophagy regulator 1 |
| [[HELLPAR]] | 0.633 | HELLP associated long non-coding RNA |
| [[RAD21]] | 0.632 | RAD21 cohesin complex component |
| [[ACBD7]] | 0.631 | acyl-CoA binding domain containing 7 |
| [[H2AX]] | 0.627 | H2A.X variant histone |
| [[SUV39H1]] | 0.626 | SUV39H1 histone lysine methyltransferase |
| [[ARHGAP19]] | 0.624 | Rho GTPase activating protein 19 |
| [[C18orf54]] | 0.616 | chromosome 18 open reading frame 54 |
| [[CCP110]] | 0.605 | centriolar coiled-coil protein 110 |
| [[DEK]] | 0.591 | DEK proto-oncogene |
| [[HYLS1]] | 0.588 | HYLS1 centriolar and ciliogenesis associated |
| [[WEE1]] | 0.586 | WEE1 G2 checkpoint kinase |
| [[SCG5]] | 0.577 | secretogranin V |
| [[HMGB1]] | 0.573 | high mobility group box 1 |
| [[NUCKS1]] | 0.569 | nuclear casein kinase and cyclin dependent kinase substrate 1 |
| [[PSIP1]] | 0.565 | PC4 and SRSF1 interacting protein 1 |
| [[LBR]] | 0.565 | lamin B receptor |
| [[CKS2]] | 0.564 | CDC28 protein kinase regulatory subunit 2 |
| [[KIAA0586]] | 0.564 | KIAA0586 |
| [[CDC25B]] | 0.563 | cell division cycle 25B |
| [[LMNB2]] | 0.560 | lamin B2 |
| [[CCDC18]] | 0.559 | coiled-coil domain containing 18 |
| [[ANP32E]] | 0.556 | acidic nuclear phosphoprotein 32 family member E |
| [[C2orf69]] | 0.554 | chromosome 2 open reading frame 69 |
| [[PHF19]] | 0.554 | PHD finger protein 19 |
| [[NUMA1]] | 0.549 | nuclear mitotic apparatus protein 1 |
| [[PHF7]] | 0.546 | PHD finger protein 7 |
| [[NEMP1]] | 0.545 | nuclear envelope integral membrane protein 1 |
| [[MYBL1]] | 0.539 | MYB proto-oncogene like 1 |
| [[MXD3]] | 0.538 | MAX dimerization protein 3 |
| [[SPA17]] | 0.535 | sperm autoantigenic protein 17 |
| [[WDPCP]] | 0.534 | WD repeat containing planar cell polarity effector |
| [[SLX4]] | 0.529 | SLX4 structure-specific endonuclease subunit |
| [[YEATS4]] | 0.513 | YEATS domain containing 4 |
| [[CEP70]] | 0.511 | centrosomal protein 70 |
| [[CEP295]] | 0.510 | centrosomal protein 295 |
| [[PPP2R5D]] | 0.507 | protein phosphatase 2 regulatory subunit B'delta |
| [[STARD8]] | 0.507 | StAR related lipid transfer domain containing 8 |
| [[NUP37]] | 0.505 | nucleoporin 37 |
| [[ZMYM1]] | 0.502 | zinc finger MYM-type containing 1 |
| [[MIS18A]] | 0.493 | MIS18 kinetochore protein A |
| [[HSD17B11]] | 0.490 | hydroxysteroid 17-beta dehydrogenase 11 |
| [[VANGL1]] | 0.489 | VANGL planar cell polarity protein 1 |
| [[SMCHD1]] | 0.488 | structural maintenance of chromosomes flexible hinge domain containing 1 |
| [[BRD8]] | 0.487 | bromodomain containing 8 |
| [[CDKN2C]] | 0.487 | cyclin dependent kinase inhibitor 2C |
| [[PCNT]] | 0.481 | pericentrin |
| [[DCP2]] | 0.478 | decapping mRNA 2 |
| [[LSM5]] | 0.477 | LSM5 homolog, U6 small nuclear RNA and mRNA degradation associated |
| [[FAM110A]] | 0.466 | family with sequence similarity 110 member A |
| [[LINC01515]] | 0.458 | long independently transcribed non-coding RNA 1515 |
| [[CEP135]] | 0.455 | centrosomal protein 135 |
| [[NUP98]] | 0.453 | nucleoporin 98 and 96 precursor |
| [[UBALD2]] | 0.451 | UBA like domain containing 2 |
| [[SUN2]] | 0.450 | Sad1 and UNC84 domain containing 2 |
| [[MYEF2]] | 0.441 | myelin expression factor 2 |
| [[SS18]] | 0.439 | SS18 subunit of BAF chromatin remodeling complex |
| [[RPL39L]] | 0.438 | ribosomal protein L39 like |
| [[HNRNPUL2]] | 0.428 | heterogeneous nuclear ribonucleoprotein U like 2 |
| [[REEP4]] | 0.427 | receptor accessory protein 4 |
| [[SOGA1]] | 0.425 | microtubule crosslinking factor 2 |
| [[CCDC85C]] | 0.424 | coiled-coil domain containing 85C |
| [[TRAF2]] | 0.419 | TNF receptor associated factor 2 |
| [[SMC3]] | 0.419 | structural maintenance of chromosomes 3 |
| [[RANGAP1]] | 0.418 | Ran GTPase activating protein 1 |
| [[YPEL1]] | 0.415 | yippee like 1 |
| [[SIN3A]] | 0.399 | SIN3 transcription regulator family member A |
| [[PCM1]] | 0.395 | pericentriolar material 1 |
| [[PAX6]] | 0.387 | paired box 6 |
| [[DCAF7]] | 0.385 | DDB1 and CUL4 associated factor 7 |
| [[OVAAL]] | -0.371 | ovarian adenocarcinoma amplified long non-coding RNA |
| [[CCDC88A]] | 0.366 | coiled-coil and HOOK domain protein 88A |
| [[CDC27]] | 0.351 | cell division cycle 27 |
| [[ANKRD20A7P]] | 0.279 | ankyrin repeat domain 20 family member A7, pseudogene |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 22; `graph/modules.parquet` — module == 22; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [21] (drug-dose × line)
