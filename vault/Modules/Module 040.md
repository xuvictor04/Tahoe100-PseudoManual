---
module: 40
type: "module"
n_genes: 111
n_plus: 100
n_minus: 11
arms_opposite: true
mean_cos_between_arms: -0.2579059898853302
label: "Asparagine N-linked glycosylation"
label_source: "reactome"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 040

*Asparagine N-linked glycosylation · 111 genes (100 in the + arm, 11 in the − arm) · [[Module 040.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26). The + arm rises where the − arm falls. Arm = the side of the module's main direction a gene sits on.

Label from the validation stage: **Asparagine N-linked glycosylation** (reactome, q 0.041; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| + | Asparagine N-linked glycosylation | reactome | 9/100 | 4.76 | 0.041 |

## Drugs that move it

*Mean pooled z of the + arm minus the − arm (`graph/module_pooled_z.npy`, row 39), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it (+ arm up, − arm down): [[Panobinostat (drug)]] 5 µM (+13.6, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (+12.6, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (+11.1, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (+6.2, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (+4.1, ⚠ cell-cycle shift); [[Belinostat (drug)]] 0.5 µM (+3.3, ⚠ cell-cycle shift); [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM (+2.4); [[HI-TOPK-032 (drug)]] 5 µM (+2.4); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (+2.2, ⚠ cell-cycle shift); [[Ipatasertib (drug)]] 0.5 µM (+2.2); [[Triamcinolone (drug)]] 5 µM (+2.1); [[Sapanisertib (drug)]] 0.5 µM (+2.1); [[Tofacitinib (citrate) (drug)]] 5 µM (+2.0); [[Brivudine (drug)]] 5 µM (+2.0); [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM (+1.9); [[Fluvoxamine (maleate) (drug)]] 5 µM (+1.7); [[Docetaxel (Trihydrate) (drug)]] 0.5 µM (+1.7) (53 in all, 8 with an alert ⚠; shown: the 10 strongest and the 7 next strongest without an alert)
- Lower it: [[Homoharringtonine (drug)]] 5 µM (-20.6, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-16.8, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-13.6, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (-10.9, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (-10.0, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (-7.9, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (-7.9, ⚠ toxic; transcription drop; cell-cycle shift); [[Digitoxin (drug)]] 5 µM (-7.8, ⚠ toxic; transcription drop; cell-cycle shift); [[Digitoxin (drug)]] 0.5 µM (-7.4, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (-6.7, ⚠ toxic; transcription drop; cell-cycle shift); [[Homoharringtonine (drug)]] 0.05 µM (-6.6); [[Harringtonine (drug)]] 0.05 µM (-3.6); [[Belumosudil (drug)]] 5 µM (-3.0); [[Ixazomib citrate (drug)]] 0.5 µM (-2.7); [[TAK-901 (drug)]] 0.05 µM (-2.7); [[Cobimetinib (drug)]] 5 µM (-2.2); [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM (-2.2); [[Berbamine (drug)]] 0.05 µM (-2.2); [[Busulfan (drug)]] 0.05 µM (-2.2); [[5-Azacytidine (drug)]] 5 µM (-2.1) (95 in all, 26 with an alert ⚠; shown: the 10 strongest and the 10 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[A-172 (line)]], [[PANC-1 (line)]], [[A549 (line)]], [[SW480 (line)]], [[A498 (line)]], [[HS-578T (line)]], [[NCI-H460 (line)]], [[KATO III (line)]]

## + arm (100)

| Gene | Projection | Name |
|---|---|---|
| [[YIPF2]] | 0.867 | Yip1 domain family member 2 |
| [[SDHAP1]] | 0.866 | SDHA pseudogene 1 |
| [[IER3IP1]] | 0.863 | immediate early response 3 interacting protein 1 |
| [[GMCL1]] | 0.848 | germ cell-less 1, spermatogenesis associated |
| [[GPR107]] | 0.846 | G protein-coupled receptor 107 |
| [[ELP2]] | 0.836 | elongator acetyltransferase complex subunit 2 |
| [[MAX]] | 0.831 | MYC associated transcriptional regulator X |
| [[SLC37A3]] | 0.818 | solute carrier family 37 member 3 |
| [[COG5]] | 0.810 | component of oligomeric golgi complex 5 |
| [[QPCTL]] | 0.805 | glutaminyl-peptide cyclotransferase like |
| [[SRP54-AS1]] | 0.800 | SRP54 antisense RNA 1 |
| [[CYB561D2]] | 0.795 | cytochrome b561 family member D2 |
| [[NPRL2]] | 0.795 | NPR2 like, GATOR1 complex subunit |
| [[DPM1]] | 0.793 | dolichyl-phosphate mannosyltransferase subunit 1, catalytic |
| [[RAB6A]] | 0.786 | RAB6A, member RAS oncogene family |
| [[EEF1AKMT4]] | 0.785 | EEF1A lysine methyltransferase 4 |
| [[KDELR1]] | 0.778 | KDEL endoplasmic reticulum protein retention receptor 1 |
| [[MED26]] | 0.772 | mediator complex subunit 26 |
| [[OXNAD1]] | 0.770 | oxidoreductase NAD binding domain containing 1 |
| [[THOC3]] | 0.761 | THO complex subunit 3 |
| [[TULP3]] | 0.755 | TUB like protein 3 |
| [[CRLS1]] | 0.754 | cardiolipin synthase 1 |
| [[SDF2L1]] | 0.745 | stromal cell derived factor 2 like 1 |
| [[HSPB11]] | 0.744 | intraflagellar transport 25 |
| [[MGAT1]] | 0.743 | alpha-1,3-mannosyl-glycoprotein 2-beta-N-acetylglucosaminyltransferase |
| [[SGSM3]] | 0.731 | small G protein signaling modulator 3 |
| [[SOCS7]] | 0.730 | suppressor of cytokine signaling 7 |
| [[SLC35E1]] | 0.728 | solute carrier family 35 member E1 |
| [[TBC1D20]] | 0.727 | TBC1 domain family member 20 |
| [[ISOC2]] | 0.724 | isochorismatase domain containing 2 |
| [[KCTD7]] | 0.721 | potassium channel tetramerization domain containing 7 |
| [[PIK3C2A]] | 0.721 | phosphatidylinositol-4-phosphate 3-kinase catalytic subunit type 2 alpha |
| [[SHQ1]] | 0.720 | SHQ1, H/ACA ribonucleoprotein assembly factor |
| [[CBLB]] | 0.716 | Cbl proto-oncogene B |
| [[IFI27L1]] | 0.713 | interferon alpha inducible protein 27 like 1 |
| [[IFT20]] | 0.713 | intraflagellar transport 20 |
| [[SPICE1]] | 0.708 | spindle and centriole associated protein 1 |
| [[KMT5C]] | 0.705 | lysine methyltransferase 5C |
| [[ARFGAP1]] | 0.695 | ARF GTPase activating protein 1 |
| [[TMEM50B]] | 0.693 | transmembrane protein 50B |
| [[SDHAP1-1]] | 0.692 | — |
| [[ZFPL1]] | 0.689 | zinc finger protein like 1 |
| [[MOGS]] | 0.681 | mannosyl-oligosaccharide glucosidase |
| [[EIF4EBP1]] | 0.680 | eukaryotic translation initiation factor 4E binding protein 1 |
| [[SNHG18]] | 0.675 | small nucleolar RNA host gene 18 |
| [[PPOX]] | 0.673 | protoporphyrinogen oxidase |
| [[APAF1]] | 0.672 | apoptotic peptidase activating factor 1 |
| [[COX7A2L]] | 0.668 | cytochrome c oxidase subunit 7A2 like |
| [[ZNF710-AS1]] | 0.667 | ZNF710 antisense RNA 1 |
| [[ZCCHC7]] | 0.662 | zinc finger CCHC-type containing 7 |
| [[GLT8D1]] | 0.660 | glycosyltransferase 8 domain containing 1 |
| [[GSDMB]] | 0.653 | gasdermin B |
| [[SYVN1]] | 0.652 | synoviolin 1 |
| [[PRKRA]] | 0.649 | protein activator of interferon induced protein kinase EIF2AK2 |
| [[CSNK2A1]] | 0.648 | casein kinase 2 alpha 1 |
| [[ORMDL3]] | 0.647 | ORMDL sphingolipid biosynthesis regulator 3 |
| [[MAPKAPK5-AS1]] | 0.646 | MAPKAPK5 antisense RNA 1 |
| [[PDPR2P]] | 0.627 | pyruvate dehydrogenase phosphatase regulatory subunit 2, pseudogene |
| [[SGK3]] | 0.626 | serum/glucocorticoid regulated kinase family member 3 |
| [[TFB2M]] | 0.625 | transcription factor B2, mitochondrial |
| [[DUXAP10]] | 0.619 | double homeobox A pseudogene 10 |
| [[CDK2AP2]] | 0.609 | cyclin dependent kinase 2 associated protein 2 |
| [[IDH2]] | 0.608 | isocitrate dehydrogenase (NADP(+)) 2 |
| [[C2CD2L]] | 0.606 | C2CD2 like |
| [[INTS10]] | 0.588 | integrator complex subunit 10 |
| [[IL17RC]] | 0.583 | interleukin 17 receptor C |
| [[ETFDH]] | 0.582 | electron transfer flavoprotein dehydrogenase |
| [[SGTB]] | 0.579 | small glutamine rich tetratricopeptide repeat co-chaperone beta |
| [[FBXO34]] | 0.578 | F-box protein 34 |
| [[ELP5]] | 0.578 | elongator acetyltransferase complex subunit 5 |
| [[ANO10]] | 0.575 | anoctamin 10 |
| [[NBAS]] | 0.574 | NBAS subunit of NRZ tethering complex |
| [[APTR]] | 0.569 | Alu-mediated CDKN1A/p21 transcriptional regulator |
| [[DYM]] | 0.568 | dymeclin |
| [[IKBIP]] | 0.567 | IKBKB interacting protein |
| [[RILPL2]] | 0.566 | Rab interacting lysosomal protein like 2 |
| [[SFXN2]] | 0.564 | sideroflexin 2 |
| [[BTRC]] | 0.555 | beta-transducin repeat containing E3 ubiquitin protein ligase |
| [[ICAM3]] | 0.549 | intercellular adhesion molecule 3 |
| [[CHST12]] | 0.540 | carbohydrate sulfotransferase 12 |
| [[IQCB1]] | 0.533 | IQ motif containing B1 |
| [[URI1]] | 0.517 | URI1 prefoldin like chaperone |
| [[HLA-F-AS1]] | 0.515 | HLA-F antisense RNA 1 |
| [[GNAS-AS1]] | 0.510 | GNAS antisense RNA 1 |
| [[ZW10]] | 0.502 | zw10 kinetochore protein |
| [[ANKIB1]] | 0.471 | ankyrin repeat and IBR domain containing 1 |
| [[TOMM70]] | 0.468 | translocase of outer mitochondrial membrane 70 |
| [[CCNB1IP1]] | 0.463 | cyclin B1 interacting protein 1 |
| [[KANSL3]] | 0.459 | KAT8 regulatory NSL complex subunit 3 |
| [[C2orf27A]] | 0.454 | long independently transcribed non-coding RNA 3124 |
| [[FOCAD]] | 0.452 | focadhesin |
| [[HDAC6]] | 0.451 | histone deacetylase 6 |
| [[ORC3]] | 0.447 | origin recognition complex subunit 3 |
| [[CA5BP1]] | 0.446 | carbonic anhydrase 5B pseudogene 1 |
| [[NOP58]] | 0.424 | NOP58 ribonucleoprotein |
| [[BIRC6]] | 0.398 | baculoviral IAP repeat containing 6 |
| [[GNE]] | 0.376 | glucosamine (UDP-N-acetyl)-2-epimerase/N-acetylmannosamine kinase |
| [[NFYA]] | 0.358 | nuclear transcription factor Y subunit alpha |
| [[TBC1D22A]] | 0.322 | TBC1 domain family member 22A |
| [[CEP76]] | 0.262 | centrosomal protein 76 |

## − arm (11)

| Gene | Projection | Name |
|---|---|---|
| [[PNRC2]] | -0.665 | proline rich nuclear receptor coactivator 2 |
| [[CCDC50]] | -0.615 | coiled-coil domain containing 50 |
| [[LPP]] | -0.548 | LIM domain containing preferred translocation partner in lipoma |
| [[CHMP4B]] | -0.423 | charged multivesicular body protein 4B |
| [[CRYBG1]] | -0.419 | crystallin beta-gamma domain containing 1 |
| [[LRRC57]] | -0.410 | leucine rich repeat containing 57 |
| [[ANKRD50]] | -0.373 | ankyrin repeat domain 50 |
| [[ZNF326]] | -0.310 | zinc finger protein 326 |
| [[DENND1B]] | -0.307 | DENN domain containing 1B |
| [[PAWR]] | -0.270 | pro-apoptotic WT1 regulator |
| [[VRK2]] | -0.204 | VRK serine/threonine kinase 2 |

## Data

- `graph/nodes.parquet` — module == 40; `graph/modules.parquet` — module == 40; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [39] (drug-dose × line)
