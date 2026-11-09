---
module: 46
type: "module"
n_genes: 97
n_plus: 91
n_minus: 6
arms_opposite: true
mean_cos_between_arms: -0.2985101640224457
label: "Chromatin modifying enzymes"
label_source: "reactome"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 046

*Chromatin modifying enzymes · 97 genes (91 in the + arm, 6 in the − arm) · [[Module 046.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30). The + arm rises where the − arm falls. Arm = the side of the module's main direction a gene sits on.

Label from the validation stage: **Chromatin modifying enzymes** (reactome, q 0.013; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| + | Chromatin modifying enzymes | reactome | 8/91 | 6.53 | 0.013 |
| all | Chromatin modifying enzymes | reactome | 8/97 | 6.12 | 0.020 |
| + | Chromatin organization | reactome | 9/91 | 4.99 | 0.030 |
| all | Chromatin organization | reactome | 9/97 | 4.68 | 0.046 |

## Drugs that move it

*Mean pooled z of the + arm minus the − arm (`graph/module_pooled_z.npy`, row 45), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it (+ arm up, − arm down): [[Idarubicin (hydrochloride) (drug)]] 5 µM (+17.4, ⚠ cell-cycle shift); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (+7.2, ⚠ cell-cycle shift); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+5.4); [[Topotecan (hydrochloride) (drug)]] 5 µM (+5.0, ⚠ toxic; cell-cycle shift); [[Epirubicin (hydrochloride) (drug)]] 5 µM (+5.0, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 0.5 µM (+4.8, ⚠ cell-cycle shift); [[Trametinib (drug)]] 5 µM (+3.9, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (+3.8, ⚠ cell-cycle shift); [[Trametinib (drug)]] 0.05 µM (+3.6); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM (+3.3); [[Trametinib (drug)]] 0.5 µM (+3.3); [[Ponatinib (drug)]] 5 µM (+3.0); [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM (+2.8); [[Binimetinib (drug)]] 0.5 µM (+2.8); [[Cobimetinib (drug)]] 5 µM (+2.8); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM (+2.8); [[Binimetinib (drug)]] 5 µM (+2.7) (68 in all, 26 with an alert ⚠; shown: the 10 strongest and the 7 next strongest without an alert)
- Lower it: [[Panobinostat (drug)]] 5 µM (-20.3, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (-19.9, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (-18.5, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (-10.7, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (-9.4); [[Belinostat (drug)]] 0.5 µM (-8.2, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 0.5 µM (-5.9, ⚠ cell-cycle shift); [[Brivudine (drug)]] 5 µM (-5.2); [[Ixazomib citrate (drug)]] 5 µM (-3.7, ⚠ cell-cycle shift); [[Auranofin (drug)]] 5 µM (-3.6); [[Ixazomib citrate (drug)]] 0.5 µM (-3.3); [[HI-TOPK-032 (drug)]] 5 µM (-2.5); [[Abemaciclib (drug)]] 5 µM (-2.0); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM (-1.9); [[Mebendazole (drug)]] 5 µM (-1.9); [[Peretinoin (drug)]] 5 µM (-1.8); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.05 µM (-1.7) (48 in all, 13 with an alert ⚠; shown: the 10 strongest and the 7 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[SW480 (line)]], [[NCI-H460 (line)]], [[PANC-1 (line)]], [[LoVo (line)]], [[HT-29 (line)]], [[J82 (line)]], [[KATO III (line)]], [[HOP62 (line)]]

## + arm (91)

| Gene | Projection | Name |
|---|---|---|
| [[HOXB7]] | 0.821 | homeobox B7 |
| [[TSTD3]] | 0.821 | thiosulfate sulfurtransferase like domain containing 3, pseudogene |
| [[RAF1]] | 0.796 | Raf-1 proto-oncogene, serine/threonine kinase |
| [[SIAH1]] | 0.796 | siah E3 ubiquitin protein ligase 1 |
| [[RNF146]] | 0.790 | ring finger protein 146 |
| [[PNISR-AS1]] | 0.776 | PNISR antisense RNA 1 |
| [[ZNF362]] | 0.770 | zinc finger protein 362 |
| [[ACOT2]] | 0.757 | acyl-CoA thioesterase 2 |
| [[HOXC9]] | 0.736 | homeobox C9 |
| [[ATAD2B]] | 0.735 | ATPase family AAA domain containing 2B |
| [[ANXA2R-AS1]] | 0.729 | ANXA2R antisense RNA 1 |
| [[DDX59]] | 0.729 | DEAD-box helicase 59 |
| [[NCOA2]] | 0.728 | nuclear receptor coactivator 2 |
| [[LINC00938]] | 0.727 | long independently transcribed non-coding RNA 938 |
| [[SETD1B]] | 0.725 | SET domain containing 1B, histone lysine methyltransferase |
| [[TLK2]] | 0.724 | tousled like kinase 2 |
| [[TRAF3IP2-AS1]] | 0.723 | TRAF3IP2 antisense RNA 1 |
| [[C2orf42]] | 0.721 | chromosome 2 open reading frame 42 |
| [[HOTAIR]] | 0.720 | HOX transcript antisense RNA |
| [[HOXC6]] | 0.719 | homeobox C6 |
| [[FBXW4]] | 0.718 | F-box and WD repeat domain containing 4 |
| [[CASD1]] | 0.706 | CAS1 domain sialic acid O acetyltransferase 1 |
| [[HFE]] | 0.703 | homeostatic iron regulator |
| [[WDFY3]] | 0.690 | WD repeat and FYVE domain containing 3 |
| [[ARID1A]] | 0.690 | AT-rich interaction domain 1A |
| [[C14orf93]] | 0.678 | chromosome 14 open reading frame 93 |
| [[DYRK1A]] | 0.675 | dual specificity tyrosine phosphorylation regulated kinase 1A |
| [[ZCCHC8]] | 0.671 | zinc finger CCHC-type containing 8 |
| [[C1QTNF6]] | 0.661 | C1q and TNF related 6 |
| [[C5orf15]] | 0.660 | chromosome 5 open reading frame 15 |
| [[UBXN2A]] | 0.659 | UBX domain protein 2A |
| [[JADE2]] | 0.659 | jade family PHD finger 2 |
| [[BRD1]] | 0.647 | bromodomain containing 1 |
| [[CFAP418]] | 0.642 | cilia and flagella associated protein 418 |
| [[CABLES1]] | 0.640 | Cdk5 and Abl enzyme substrate 1 |
| [[ARHGEF17]] | 0.638 | Rho guanine nucleotide exchange factor 17 |
| [[MED24]] | 0.632 | mediator complex subunit 24 |
| [[ZBTB8A]] | 0.625 | zinc finger and BTB domain containing 8A |
| [[PHF2]] | 0.622 | PHD finger protein 2 |
| [[HOXC8]] | 0.617 | homeobox C8 |
| [[CYB561A3]] | 0.608 | cytochrome b561 family member A3 |
| [[HOXD10]] | 0.603 | homeobox D10 |
| [[MIR181A2HG]] | 0.599 | MIR181A2 host gene |
| [[RPRD1B]] | 0.599 | regulation of nuclear pre-mRNA domain containing 1B |
| [[CHD6]] | 0.597 | chromodomain helicase DNA binding protein 6 |
| [[SLC35E2B]] | 0.594 | solute carrier family 35 member E2B |
| [[GATA2-AS1]] | 0.587 | GATA2 antisense RNA 1 |
| [[FOXJ2]] | 0.587 | forkhead box J2 |
| [[CCAR1]] | 0.586 | cell division cycle and apoptosis regulator 1 |
| [[HOXD3]] | 0.585 | homeobox D3 |
| [[NEIL1]] | 0.582 | nei like DNA glycosylase 1 |
| [[STRIP1]] | 0.570 | striatin interacting protein 1 |
| [[TNPO2]] | 0.568 | transportin 2 |
| [[ZFR]] | 0.565 | zinc finger RNA binding protein |
| [[C10orf95-AS1]] | 0.561 | C10orf95 antisense RNA 1 |
| [[ACCS]] | 0.561 | 1-aminocyclopropane-1-carboxylate synthase homolog (inactive) |
| [[HOXD11]] | 0.549 | homeobox D11 |
| [[RNF135]] | 0.543 | ring finger protein 135 |
| [[SIX4]] | 0.543 | SIX homeobox 4 |
| [[PIP5K1A]] | 0.543 | phosphatidylinositol-4-phosphate 5-kinase type 1 alpha |
| [[NKIRAS1]] | 0.542 | NFKB inhibitor interacting Ras like 1 |
| [[ABRACL]] | 0.535 | ABRA C-terminal like |
| [[SHOX2]] | 0.532 | SHOX homeobox 2 |
| [[VSIG10]] | 0.531 | V-set and immunoglobulin domain containing 10 |
| [[PRDM2]] | 0.528 | PR/SET domain 2 |
| [[GOLGA2P5-1]] | 0.527 | — |
| [[DNMT3A]] | 0.526 | DNA methyltransferase 3 alpha |
| [[LINC02086]] | 0.517 | long independently transcribed non-coding RNA 2086 |
| [[ALDH1A3-AS1]] | 0.514 | ALDH1A3 antisense RNA 1 |
| [[NLRX1]] | 0.512 | NLR family member X1 |
| [[OBSL1]] | 0.509 | obscurin like cytoskeletal adaptor 1 |
| [[PGAP3]] | 0.508 | post-GPI attachment to proteins phospholipase 3 |
| [[COMMD4]] | 0.490 | COMM domain containing 4 |
| [[SIM2]] | 0.476 | SIM bHLH transcription factor 2 |
| [[CTPS2]] | 0.472 | CTP synthase 2 |
| [[PPP1R3E]] | 0.460 | protein phosphatase 1 regulatory subunit 3E |
| [[WHAMMP3]] | 0.457 | WHAMM pseudogene 3 |
| [[STRN3]] | 0.449 | striatin 3 |
| [[LSM6]] | 0.447 | LSM6 homolog, U6 small nuclear RNA and mRNA degradation associated |
| [[UNC119B]] | 0.444 | unc-119 lipid binding chaperone B |
| [[PLXNB3-AS1]] | 0.437 | PLXNB3 antisense RNA 1 |
| [[ECHDC2]] | 0.435 | enoyl-CoA hydratase domain containing 2 |
| [[SGF29]] | 0.423 | SAGA complex associated factor 29 |
| [[PITX1]] | 0.418 | paired like homeodomain 1 |
| [[DLX6-AS1]] | 0.416 | DLX6 antisense RNA 1 |
| [[ZNF775]] | 0.412 | zinc finger protein 775 |
| [[LRRC34]] | 0.408 | leucine rich repeat containing 34 |
| [[PXDC1]] | 0.373 | PX domain containing 1 |
| [[WDR91]] | 0.368 | WD repeat domain 91 |
| [[ITFG1]] | 0.355 | integrin alpha FG-GAP repeat containing 1 |
| [[ITGA9-AS1]] | 0.335 | ITGA9 antisense RNA 1 |

## − arm (6)

| Gene | Projection | Name |
|---|---|---|
| [[ACTG1]] | -0.578 | actin gamma 1 |
| [[NDFIP2]] | -0.570 | Nedd4 family interacting protein 2 |
| [[TNIK]] | -0.550 | TRAF2 and NCK interacting kinase |
| [[CCDC112]] | -0.517 | coiled-coil domain containing 112 |
| [[ACAP2]] | -0.482 | ArfGAP with coiled-coil, ankyrin repeat and PH domains 2 |
| [[CARMIL2]] | -0.433 | capping protein regulator and myosin 1 linker 2 |

## Data

- `graph/nodes.parquet` — module == 46; `graph/modules.parquet` — module == 46; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [45] (drug-dose × line)
