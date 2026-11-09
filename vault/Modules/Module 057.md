---
module: 57
type: "module"
n_genes: 86
n_plus: 66
n_minus: 20
arms_opposite: true
mean_cos_between_arms: -0.29501211643218994
label: "Peroxisomal protein import"
label_source: "reactome"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 057

*Peroxisomal protein import · 86 genes (66 in the + arm, 20 in the − arm) · [[Module 057.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30). The + arm rises where the − arm falls. Arm = the side of the module's main direction a gene sits on.

Label from the validation stage: **Peroxisomal protein import** (reactome, q 0.036; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| + | Peroxisomal protein import | reactome | 4/66 | 16.6 | 0.036 |

## Drugs that move it

*Mean pooled z of the + arm minus the − arm (`graph/module_pooled_z.npy`, row 56), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it (+ arm up, − arm down): [[Panobinostat (drug)]] 5 µM (+11.4, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (+11.0, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (+9.7, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (+9.5, ⚠ toxic; transcription drop; cell-cycle shift); [[Belinostat (drug)]] 5 µM (+9.3, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+7.2, ⚠ toxic; transcription drop; cell-cycle shift); [[NG25 (drug)]] 5 µM (+6.1, ⚠ cell-cycle shift); [[Selinexor (drug)]] 5 µM (+5.9, ⚠ cell-cycle shift); [[Radotinib (drug)]] 5 µM (+4.3); [[TAK-901 (drug)]] 5 µM (+4.0, ⚠ cell-cycle shift); [[Ponatinib (drug)]] 5 µM (+3.8); [[PH-797804 (drug)]] 5 µM (+3.1); [[Brivudine (drug)]] 5 µM (+3.0); [[Ixazomib citrate (drug)]] 0.5 µM (+2.8); [[Flumatinib (mesylate) (drug)]] 5 µM (+2.6); [[Tofacitinib (drug)]] 0.5 µM (+1.9); [[Cabozantinib (S-malate) (drug)]] 5 µM (+1.9); [[Ponatinib (drug)]] 0.05 µM (+1.9); [[Budesonide (drug)]] 0.05 µM (+1.8) (72 in all, 20 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)
- Lower it: [[Homoharringtonine (drug)]] 5 µM (-22.7, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-14.4, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-12.7, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (-12.1, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (-8.6, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (-7.6, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (-7.4, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 5 µM (-7.3, ⚠ toxic; transcription drop; cell-cycle shift); [[Digitoxin (drug)]] 0.5 µM (-6.7, ⚠ cell-cycle shift); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (-5.5); [[Homoharringtonine (drug)]] 0.05 µM (-3.4); [[5-Azacytidine (drug)]] 5 µM (-3.3); [[PF-06260933 (drug)]] 5 µM (-2.3); [[Rapamycin (drug)]] 5 µM (-2.0); [[Pitavastatin (Calcium) (drug)]] 0.5 µM (-1.8); [[Temsirolimus (drug)]] 0.05 µM (-1.8); [[Lactate (calcium) (drug)]] 0.5 µM (-1.8); [[Abiraterone acetate (drug)]] 0.05 µM (-1.7); [[Benztropine (mesylate) (drug)]] 0.05 µM (-1.6) (76 in all, 24 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[NCI-H460 (line)]], [[PANC-1 (line)]], [[HOP62 (line)]], [[LoVo (line)]], [[NCI-H1573 (line)]], [[J82 (line)]], [[A498 (line)]], [[MIA PaCa-2 (line)]]

## + arm (66)

| Gene | Projection | Name |
|---|---|---|
| [[NDRG3]] | 0.863 | NDRG family member 3 |
| [[SKP2]] | 0.841 | S-phase kinase associated protein 2 |
| [[ATP5F1C]] | 0.830 | ATP synthase F1 subunit gamma |
| [[NUDT21]] | 0.807 | nudix hydrolase 21 |
| [[PAPSS1]] | 0.804 | 3'-phosphoadenosine 5'-phosphosulfate synthase 1 |
| [[SDHB]] | 0.799 | succinate dehydrogenase complex iron sulfur subunit B |
| [[PLA2G12A]] | 0.789 | phospholipase A2 group XIIA |
| [[ELP1]] | 0.780 | elongator acetyltransferase complex subunit 1 |
| [[RPA1]] | 0.777 | replication protein A1 |
| [[UBAC1]] | 0.771 | UBA domain containing 1 |
| [[LONP2]] | 0.766 | lon peptidase 2, peroxisomal |
| [[RAB4A]] | 0.745 | RAB4A, member RAS oncogene family |
| [[CBX1]] | 0.727 | chromobox 1 |
| [[CROT]] | 0.727 | carnitine O-octanoyltransferase |
| [[STARD3NL]] | 0.725 | STARD3 N-terminal like |
| [[RPP30]] | 0.724 | ribonuclease P/MRP subunit p30 |
| [[PIK3R2]] | 0.713 | phosphoinositide-3-kinase regulatory subunit 2 |
| [[ANAPC5]] | 0.713 | anaphase promoting complex subunit 5 |
| [[VAMP7]] | 0.711 | vesicle associated membrane protein 7 |
| [[SLC35A3]] | 0.697 | solute carrier family 35 member A3 |
| [[GNPDA2]] | 0.696 | glucosamine-6-phosphate deaminase 2 |
| [[HBS1L]] | 0.694 | HBS1 like translational GTPase |
| [[PECR]] | 0.684 | peroxisomal trans-2-enoyl-CoA reductase |
| [[HLTF]] | 0.682 | helicase like transcription factor |
| [[HSD17B4]] | 0.679 | hydroxysteroid 17-beta dehydrogenase 4 |
| [[CYB5R4]] | 0.678 | cytochrome b5 reductase 4 |
| [[CNIH1]] | 0.666 | cornichon family member 1 |
| [[USP48]] | 0.663 | ubiquitin specific peptidase 48 |
| [[IARS2]] | 0.656 | isoleucyl-tRNA synthetase 2, mitochondrial |
| [[PHKB]] | 0.652 | phosphorylase kinase regulatory subunit beta |
| [[TBC1D2B]] | 0.645 | TBC1 domain family member 2B |
| [[GUSBP1]] | 0.645 | GUSB pseudogene 1 |
| [[MIGA1]] | 0.635 | mitoguardin 1 |
| [[VPS26B]] | 0.632 | VPS26 retromer complex component B |
| [[RBL2]] | 0.623 | RB transcriptional corepressor like 2 |
| [[BLTP1]] | 0.619 | bridge-like lipid transfer protein family member 1 |
| [[TMEM245]] | 0.606 | transmembrane protein 245 |
| [[ZDHHC20]] | 0.600 | zDHHC palmitoyltransferase 20 |
| [[EEF1AKMT2]] | 0.586 | EEF1A lysine methyltransferase 2 |
| [[ALDH7A1]] | 0.584 | aldehyde dehydrogenase 7 family member A1 |
| [[NXPE3]] | 0.582 | neurexophilin and PC-esterase domain family member 3 |
| [[DDX42]] | 0.568 | DEAD-box helicase 42 |
| [[NAP1L4]] | 0.558 | nucleosome assembly protein 1 like 4 |
| [[EIF2AK1]] | 0.554 | eukaryotic translation initiation factor 2 alpha kinase 1 |
| [[BLMH]] | 0.547 | bleomycin hydrolase |
| [[TMEM161B]] | 0.543 | transmembrane protein 161B |
| [[CNOT7]] | 0.541 | CCR4-NOT transcription complex subunit 7 |
| [[ABRAXAS1]] | 0.526 | abraxas 1, BRCA1 A complex subunit |
| [[TTC14]] | 0.519 | tetratricopeptide repeat domain 14 |
| [[ZNF512]] | 0.517 | zinc finger protein 512 |
| [[NDUFV1]] | 0.503 | NADH:ubiquinone oxidoreductase core subunit V1 |
| [[APPL1]] | 0.497 | adaptor protein, phosphotyrosine interacting with PH domain and leucine zipper 1 |
| [[KCNK15-AS1]] | 0.495 | KCNK15 and WISP2 antisense RNA 1 |
| [[SNRPC]] | 0.475 | small nuclear ribonucleoprotein polypeptide C |
| [[GCOM1]] | 0.451 | GCOM1, MYZAP-POLR2M combined locus |
| [[PHC1]] | 0.448 | polyhomeotic homolog 1 |
| [[VPS35]] | 0.439 | VPS35 retromer complex component |
| [[MOCS2]] | 0.439 | molybdenum cofactor synthesis 2 |
| [[MAPRE3]] | 0.436 | microtubule associated protein RP/EB family member 3 |
| [[MRPL48]] | 0.433 | mitochondrial ribosomal protein L48 |
| [[FN3K]] | 0.410 | fructosamine 3 kinase |
| [[OSBPL1A]] | 0.397 | oxysterol binding protein like 1A |
| [[DNM1]] | 0.394 | dynamin 1 |
| [[ZNF891]] | 0.375 | zinc finger protein 891 |
| [[MRPL13]] | 0.348 | mitochondrial ribosomal protein L13 |
| [[LRP12]] | 0.290 | LDL receptor related protein 12 |

## − arm (20)

| Gene | Projection | Name |
|---|---|---|
| [[BAZ1A]] | -0.730 | bromodomain adjacent to zinc finger domain 1A |
| [[HIVEP1]] | -0.722 | HIVEP zinc finger 1 |
| [[ERF]] | -0.678 | ETS2 repressor factor |
| [[SATB2]] | -0.671 | SATB homeobox 2 |
| [[TSC22D1]] | -0.629 | TSC22 domain family member 1 |
| [[XIAP]] | -0.615 | X-linked inhibitor of apoptosis |
| [[EPOP]] | -0.583 | elongin BC and polycomb repressive complex 2 associated protein |
| [[NFE2L2]] | -0.548 | NFE2 like bZIP transcription factor 2 |
| [[PHLPP2]] | -0.544 | PH domain and leucine rich repeat protein phosphatase 2 |
| [[RIPK1]] | -0.538 | receptor interacting serine/threonine kinase 1 |
| [[LINC00963]] | -0.510 | long independently transcribed non-coding RNA 963 |
| [[CREM]] | -0.498 | cAMP responsive element modulator |
| [[ZDHHC14]] | -0.490 | zDHHC palmitoyltransferase 14 |
| [[ZFYVE16]] | -0.478 | zinc finger FYVE-type containing 16 |
| [[PWWP2A]] | -0.460 | PWWP domain containing 2A |
| [[ALS2]] | -0.415 | alsin Rho guanine nucleotide exchange factor ALS2 |
| [[GABBR1]] | -0.384 | gamma-aminobutyric acid type B receptor subunit 1 |
| [[CDC42SE1]] | -0.347 | CDC42 small effector 1 |
| [[SLF2]] | -0.293 | SMC5/6 complex localization factor 2 |
| [[VHL]] | -0.130 | von Hippel-Lindau tumor suppressor |

## Data

- `graph/nodes.parquet` — module == 57; `graph/modules.parquet` — module == 57; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [56] (drug-dose × line)
