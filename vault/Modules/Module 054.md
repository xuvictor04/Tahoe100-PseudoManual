---
module: 54
type: "module"
n_genes: 88
n_plus: 56
n_minus: 32
arms_opposite: true
mean_cos_between_arms: -0.32213449478149414
label: "Mitochondrial ribosome-associated quality control"
label_source: "reactome"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 054

*Mitochondrial ribosome-associated quality control · 88 genes (56 in the + arm, 32 in the − arm) · [[Module 054.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32). The + arm rises where the − arm falls. Arm = the side of the module's main direction a gene sits on.

Label from the validation stage: **Mitochondrial ribosome-associated quality control** (reactome, q 4e-08; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| + | Mitochondrial ribosome-associated quality control | reactome | 9/56 | 27.2 | 4e-08 |
| + | Mitochondrial translation | reactome | 9/56 | 24.5 | 1e-07 |
| all | Mitochondrial translation | reactome | 10/88 | 17.3 | 3e-07 |
| + | Mitochondrial translation elongation | reactome | 8/56 | 24.8 | 9e-07 |
| + | Mitochondrial translation initiation | reactome | 8/56 | 24.8 | 9e-07 |
| + | Mitochondrial translation termination | reactome | 8/56 | 24.5 | 1e-06 |
| all | Mitochondrial translation termination | reactome | 9/88 | 17.5 | 2e-06 |
| all | Mitochondrial ribosome-associated quality control | reactome | 9/88 | 17.3 | 2e-06 |

## Drugs that move it

*Mean pooled z of the + arm minus the − arm (`graph/module_pooled_z.npy`, row 53), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it (+ arm up, − arm down): [[Panobinostat (drug)]] 0.5 µM (+8.2, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (+8.0, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (+7.9, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (+4.1, ⚠ cell-cycle shift); [[Belinostat (drug)]] 0.5 µM (+3.5, ⚠ cell-cycle shift); [[Topotecan (hydrochloride) (drug)]] 5 µM (+3.4, ⚠ toxic; cell-cycle shift); [[Ipatasertib (drug)]] 0.5 µM (+2.9); [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM (+2.8); [[Sunitinib (drug)]] 5 µM (+2.8, ⚠ toxic); [[Imiquimod (hydrochloride) (drug)]] 5 µM (+2.6, ⚠ toxic); [[Docetaxel (Trihydrate) (drug)]] 0.5 µM (+2.4); [[Azithromycin (hydrate) (drug)]] 5 µM (+2.4); [[Arbutin (drug)]] 5 µM (+2.4); [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM (+2.2); [[Bendamustine (drug)]] 5 µM (+2.2); [[Decitabine (drug)]] 0.5 µM (+2.1); [[Sapanisertib (drug)]] 0.5 µM (+2.1); [[Darolutamide (drug)]] 5 µM (+2.0) (120 in all, 22 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)
- Lower it: [[Homoharringtonine (drug)]] 5 µM (-15.2, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (-13.7, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (-13.7, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (-11.9, ⚠ toxic; transcription drop; cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-7.4, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-6.3, ⚠ cell-cycle shift); [[Auranofin (drug)]] 5 µM (-5.8); [[Idarubicin (hydrochloride) (drug)]] 5 µM (-5.8, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (-3.8, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (-3.1, ⚠ cell-cycle shift); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (-2.6); [[PH-797804 (drug)]] 0.05 µM (-2.4); [[Lucanthone (drug)]] 0.05 µM (-2.4); [[Diphenhydramine (drug)]] 0.05 µM (-2.4); [[Homoharringtonine (drug)]] 0.05 µM (-2.2); [[BAY1125976 (drug)]] 5 µM (-2.0); [[Benproperine (phosphate) (drug)]] 0.05 µM (-2.0); [[Fenofibrate (drug)]] 0.05 µM (-2.0); [[Tirabrutinib (drug)]] 0.05 µM (-2.0) (138 in all, 28 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[SW480 (line)]], [[NCI-H460 (line)]], [[HOP62 (line)]], [[PANC-1 (line)]], [[NCI-H1573 (line)]], [[HS-578T (line)]], [[LoVo (line)]], [[A498 (line)]]

## Candidate new members

*Members not annotated to the set their arm is enriched for, ranked by mean cos to the annotated members (`validation/novel_members.csv`); ⚠ = a reason to doubt the gene's place (in the vector space only through flagged drug-doses), kept in its rank. 15 candidates, 3 with an alert ⚠.*

| # | Gene | Set | Mean cos | Alert |
|---|---|---|---|---|
| 1 | [[POP7]] | Mitochondrial ribosome-associated quality control | +0.70 |  |
| 2 | [[PET117]] | Mitochondrial translation elongation | +0.64 |  |
| 3 | [[C15orf61]] ⚠ | Mitochondrial ribosome-associated quality control | +0.62 | ⚠ in the vector space only through drug-doses that carry an alert |
| 4 | [[LSM2]] | Mitochondrial ribosome-associated quality control | +0.62 |  |
| 5 | [[SF3B5]] ⚠ | Mitochondrial ribosome-associated quality control | +0.61 | ⚠ in the vector space only through drug-doses that carry an alert |
| 6 | [[TIMM13]] | Mitochondrial translation elongation | +0.61 |  |
| 7 | [[EMC6]] | Mitochondrial translation elongation | +0.59 |  |
| 8 | [[SAC3D1]] | Mitochondrial ribosome-associated quality control | +0.58 |  |
| 9 | [[SDHAF1]] | Mitochondrial ribosome-associated quality control | +0.57 |  |
| 10 | [[NR2F6]] | Mitochondrial ribosome-associated quality control | +0.56 |  |
| 11 | [[MALSU1]] | Mitochondrial translation elongation | +0.55 |  |
| 12 | [[SNU13]] | Mitochondrial ribosome-associated quality control | +0.55 |  |
| 13 | [[RPL22L1]] ⚠ | Mitochondrial translation elongation | +0.54 | ⚠ in the vector space only through drug-doses that carry an alert |
| 14 | [[TOMM5]] | Mitochondrial translation elongation | +0.53 |  |
| 15 | [[CCDC107]] | Mitochondrial ribosome-associated quality control | +0.53 |  |

*⚠ 4 of its 88 genes are in the vector space only through drug-doses that carry an alert (`embed/genes.parquet` evidence_flagged_only): their place here may reflect what those drug-doses did to the cells. They are marked in the tables of this note.*

## + arm (56)

| Gene | Projection | Name | Alert |
|---|---|---|---|
| [[POP7]] | 0.888 | POP7 ribonuclease P/MRP subunit |  |
| [[LSM2]] | 0.862 | LSM2 homolog, U6 small nuclear RNA and mRNA degradation associated |  |
| [[C15orf61]] | 0.848 | chromosome 15 open reading frame 61 | ⚠ only flagged evidence |
| [[MALSU1]] | 0.844 | mitochondrial assembly of ribosomal large subunit 1 |  |
| [[CHCHD1]] | 0.832 | coiled-coil-helix-coiled-coil-helix domain containing 1 |  |
| [[MRPL34]] | 0.818 | mitochondrial ribosomal protein L34 |  |
| [[SF3B5]] | 0.791 | splicing factor 3b subunit 5 | ⚠ only flagged evidence |
| [[SDHAF1]] | 0.786 | succinate dehydrogenase complex assembly factor 1 |  |
| [[PET117]] | 0.767 | PET117 cytochrome c oxidase chaperone |  |
| [[MRPS34]] | 0.752 | mitochondrial ribosomal protein S34 |  |
| [[SAC3D1]] | 0.751 | SAC3 domain containing 1 |  |
| [[NR2F6]] | 0.751 | nuclear receptor subfamily 2 group F member 6 |  |
| [[CCDC107]] | 0.748 | coiled-coil domain containing 107 |  |
| [[MRPS26]] | 0.718 | mitochondrial ribosomal protein S26 |  |
| [[EMC6]] | 0.710 | ER membrane protein complex subunit 6 |  |
| [[SNU13]] | 0.709 | small nuclear ribonucleoprotein 13 |  |
| [[RPL22L1]] | 0.702 | ribosomal protein L22 like 1 | ⚠ only flagged evidence |
| [[MRPS12]] | 0.690 | mitochondrial ribosomal protein S12 |  |
| [[MRPL14]] | 0.686 | mitochondrial ribosomal protein L14 |  |
| [[USP42]] | 0.682 | ubiquitin specific peptidase 42 |  |
| [[TOMM5]] | 0.680 | translocase of outer mitochondrial membrane 5 |  |
| [[NSFP1]] | 0.678 | N-ethylmaleimide-sensitive factor pseudogene 1 |  |
| [[IMP3]] | 0.650 | IMP U3 small nucleolar ribonucleoprotein 3 |  |
| [[TIMM13]] | 0.646 | translocase of inner mitochondrial membrane 13 |  |
| [[GTF2H2]] | 0.642 | general transcription factor IIH subunit 2 |  |
| [[TUBD1]] | 0.638 | tubulin delta 1 |  |
| [[RNF149]] | 0.632 | ring finger protein 149 |  |
| [[AURKAIP1]] | 0.631 | aurora kinase A interacting protein 1 |  |
| [[MRPS21]] | 0.630 | mitochondrial ribosomal protein S21 |  |
| [[HEBP1]] | 0.618 | heme binding protein 1 |  |
| [[SMIM3]] | 0.585 | small integral membrane protein 3 |  |
| [[NOP10]] | 0.583 | NOP10 ribonucleoprotein | ⚠ only flagged evidence |
| [[PPP1R12B]] | 0.576 | protein phosphatase 1 regulatory subunit 12B |  |
| [[CLPP]] | 0.569 | caseinolytic mitochondrial matrix peptidase proteolytic subunit |  |
| [[SLIRP]] | 0.563 | SRA stem-loop interacting RNA binding protein |  |
| [[TMEM170A]] | 0.559 | transmembrane protein 170A |  |
| [[MNX1]] | 0.544 | motor neuron and pancreas homeobox 1 |  |
| [[STK38]] | 0.544 | serine/threonine kinase 38 |  |
| [[DCUN1D5]] | 0.542 | defective in cullin neddylation 1 domain containing 5 |  |
| [[ACAD10]] | 0.542 | acyl-CoA dehydrogenase family member 10 |  |
| [[RTL8A]] | 0.540 | retrotransposon Gag like 8A |  |
| [[NXT1]] | 0.539 | nuclear transport factor 2 like export factor 1 |  |
| [[CAPN7]] | 0.517 | calpain 7 |  |
| [[MTM1]] | 0.498 | myotubularin 1 |  |
| [[TOMM22]] | 0.481 | translocase of outer mitochondrial membrane 22 |  |
| [[TIMM10]] | 0.458 | translocase of inner mitochondrial membrane 10 |  |
| [[DISP1]] | 0.451 | dispatched RND transporter family member 1 |  |
| [[TUT4]] | 0.424 | terminal uridylyl transferase 4 |  |
| [[GRAMD1A]] | 0.391 | GRAM domain containing 1A |  |
| [[TBC1D7]] | 0.383 | TBC1 domain family member 7 |  |
| [[TMCC1]] | 0.371 | transmembrane and coiled-coil domain family 1 |  |
| [[NUDT11]] | 0.367 | nudix hydrolase 11 |  |
| [[GUSBP1-1]] | 0.320 | — |  |
| [[HECTD4]] | 0.306 | HECT domain E3 ubiquitin protein ligase 4 |  |
| [[SLMAP]] | 0.303 | sarcolemma associated protein |  |
| [[CEP89]] | 0.244 | centrosomal protein 89 |  |

## − arm (32)

| Gene | Projection | Name | Alert |
|---|---|---|---|
| [[ZNF655]] | -0.756 | zinc finger protein 655 |  |
| [[CCDC200]] | -0.752 | coiled-coil domain containing 200 |  |
| [[CROCC]] | -0.730 | ciliary rootlet coiled-coil, rootletin |  |
| [[PIEZO1]] | -0.723 | piezo type mechanosensitive ion channel component 1 (Er blood group) |  |
| [[NID1]] | -0.694 | nidogen 1 |  |
| [[SCRN1]] | -0.690 | secernin 1 |  |
| [[SEPTIN11]] | -0.678 | septin 11 |  |
| [[UBE2A]] | -0.678 | ubiquitin conjugating enzyme E2 A |  |
| [[FLII]] | -0.651 | FLII actin remodeling protein |  |
| [[MYOSLID]] | -0.646 | myocardin-induced smooth muscle lncRNA, inducer of differentiation |  |
| [[KRT8P12]] | -0.646 | keratin 8 pseudogene 12 |  |
| [[THOC6]] | -0.646 | THO complex subunit 6 |  |
| [[SEPTIN8]] | -0.636 | septin 8 |  |
| [[CYB5D1]] | -0.620 | cytochrome b5 domain containing 1 |  |
| [[CLASP1-AS1]] | -0.595 | CLASP1 antisense RNA 1 |  |
| [[STK26]] | -0.587 | serine/threonine kinase 26 |  |
| [[HAPSTR1]] | -0.580 | HUWE1 associated protein modifying stress responses |  |
| [[YES1]] | -0.568 | YES proto-oncogene 1, Src family tyrosine kinase |  |
| [[RLIM]] | -0.565 | ring finger protein, LIM domain interacting |  |
| [[MTRF1L]] | -0.551 | mitochondrial translation release factor 1 like |  |
| [[PITRM1]] | -0.526 | pitrilysin metallopeptidase 1 |  |
| [[TMEM43]] | -0.507 | transmembrane protein 43 |  |
| [[SBDS]] | -0.501 | SBDS ribosome maturation factor |  |
| [[PHF10]] | -0.501 | PHD finger protein 10 |  |
| [[AHNAK]] | -0.485 | AHNAK nucleoprotein |  |
| [[DSP]] | -0.475 | desmoplakin |  |
| [[PAK2]] | -0.442 | p21 (RAC1) activated kinase 2 |  |
| [[IQCG]] | -0.421 | dynein regulatory complex subunit 9 |  |
| [[PFKP]] | -0.407 | phosphofructokinase, platelet |  |
| [[ELF4]] | -0.392 | E74 like ETS transcription factor 4 |  |
| [[VPS4A]] | -0.317 | vacuolar protein sorting 4 homolog A |  |
| [[SAMD10]] | -0.205 | sterile alpha motif domain containing 10 |  |

## Data

- `graph/nodes.parquet` — module == 54; `graph/modules.parquet` — module == 54; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [53] (drug-dose × line)
