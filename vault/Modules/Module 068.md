---
module: 68
type: "module"
n_genes: 73
n_plus: 68
n_minus: 5
arms_opposite: true
mean_cos_between_arms: -0.43357962369918823
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 068

*73 genes (68 in the + arm, 5 in the − arm) · [[Module 068.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43). The + arm rises where the − arm falls. Arm = the side of the module's main direction a gene sits on.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of the + arm minus the − arm (`graph/module_pooled_z.npy`, row 67), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it (+ arm up, − arm down): [[Homoharringtonine (drug)]] 5 µM (+35.4, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (+22.9, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (+22.8, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (+15.4, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (+14.4, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.05 µM (+9.3); [[Dinaciclib (drug)]] 0.5 µM (+8.8, ⚠ toxic; transcription drop; cell-cycle shift); [[Digitoxin (drug)]] 5 µM (+8.3, ⚠ toxic; transcription drop; cell-cycle shift); [[Topotecan (hydrochloride) (drug)]] 5 µM (+7.9, ⚠ toxic; cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+7.9, ⚠ toxic; transcription drop; cell-cycle shift); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+7.4); [[Auranofin (drug)]] 5 µM (+4.3); [[Harringtonine (drug)]] 0.05 µM (+4.3); [[Amsacrine (drug)]] 5 µM (+3.9); [[Trametinib (drug)]] 0.5 µM (+2.6); [[Peretinoin (drug)]] 0.5 µM (+2.6); [[Belumosudil (drug)]] 5 µM (+2.4); [[Docetaxel (drug)]] 5 µM (+2.3); [[Tucidinostat (drug)]] 5 µM (+2.1) (102 in all, 38 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)
- Lower it: [[Panobinostat (drug)]] 5 µM (-16.0, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (-15.2, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (-14.8, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (-7.1, ⚠ cell-cycle shift); [[Belinostat (drug)]] 0.5 µM (-6.6, ⚠ cell-cycle shift); [[Brivudine (drug)]] 5 µM (-4.6); [[Bortezomib (drug)]] 0.05 µM (-3.0, ⚠ cell-cycle shift); [[Budesonide (drug)]] 5 µM (-2.9); [[Triamcinolone (drug)]] 0.5 µM (-2.5); [[Dexamethasone (drug)]] 0.5 µM (-2.3); [[Clobetasol propionate (drug)]] 5 µM (-2.0); [[Clobetasol propionate (drug)]] 0.5 µM (-1.9); [[Quinestrol (drug)]] 5 µM (-1.9); [[Dexamethasone (drug)]] 0.05 µM (-1.7); [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM (-1.6); [[Triamcinolone (drug)]] 0.05 µM (-1.6) (70 in all, 12 with an alert ⚠; shown: the 10 strongest and the 6 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[PANC-1 (line)]], [[A-172 (line)]], [[LoVo (line)]], [[A498 (line)]], [[NCI-H460 (line)]], [[HOP62 (line)]], [[NCI-H1573 (line)]], [[SW480 (line)]]

## + arm (68)

| Gene | Projection | Name |
|---|---|---|
| [[PATL2]] | 0.902 | PAT1 homolog 2 |
| [[RIPK2-DT]] | 0.849 | palmitic acid regulated anti-inflammatory lncRNA |
| [[ZNF764]] | 0.821 | zinc finger protein 764 |
| [[LGALSL-DT]] | 0.820 | LGALSL divergent transcript |
| [[HHLA3]] | 0.817 | ANKRD13C divergent transcript |
| [[WAC-AS1]] | 0.817 | WAC antisense RNA 1 |
| [[TAPBPL]] | 0.816 | TAP binding protein like |
| [[PLA2G4C]] | 0.802 | phospholipase A2 group IVC |
| [[APLF]] | 0.797 | aprataxin and PNKP like factor |
| [[SLC9A8]] | 0.783 | solute carrier family 9 member A8 |
| [[FAM200B]] | 0.778 | zinc finger BED-type containing 11 |
| [[LACTB2]] | 0.777 | lactamase beta 2 |
| [[TRIP6]] | 0.756 | thyroid hormone receptor interactor 6 |
| [[LACC1]] | 0.755 | laccase domain multifunctional purine nucleosidase 1 |
| [[TCEAL4]] | 0.752 | transcription elongation factor A like 4 |
| [[LINC00944]] | 0.749 | long independently transcribed non-coding RNA 944 |
| [[PAXIP1-AS2]] | 0.742 | PAXIP1 antisense RNA 2 |
| [[COL28A1]] | 0.742 | collagen type XXVIII alpha 1 chain |
| [[ZNF462]] | 0.737 | zinc finger protein 462 |
| [[TMEM35B]] | 0.733 | transmembrane protein 35B |
| [[RC3H2]] | 0.720 | ring finger and CCCH-type domains 2 |
| [[RWDD2B]] | 0.714 | RWD domain containing 2B |
| [[LATS1]] | 0.710 | large tumor suppressor kinase 1 |
| [[ZFY]] | 0.709 | zinc finger protein Y-linked |
| [[NNT-AS1]] | 0.708 | NNT antisense RNA 1 |
| [[CPEB2]] | 0.706 | cytoplasmic polyadenylation element binding protein 2 |
| [[SOCS2-AS1]] | 0.705 | SOCS2 antisense RNA 1 |
| [[GYG1]] | 0.701 | glycogenin 1 |
| [[SOCS2]] | 0.698 | suppressor of cytokine signaling 2 |
| [[EIF4EBP3]] | 0.682 | eukaryotic translation initiation factor 4E binding protein 3 |
| [[DUSP16]] | 0.682 | dual specificity phosphatase 16 |
| [[TTC6]] | 0.671 | tetratricopeptide repeat domain 6 |
| [[PLD6]] | 0.669 | phospholipase D family member 6 |
| [[IFNAR1]] | 0.660 | interferon alpha and beta receptor subunit 1 |
| [[RNF103-CHMP3]] | 0.658 | RNF103-CHMP3 readthrough |
| [[MARVELD2]] | 0.654 | MARVEL domain containing 2 |
| [[ZBTB21]] | 0.648 | zinc finger and BTB domain containing 21 |
| [[ANKRD20A5P]] | 0.647 | ankyrin repeat domain 20 family member A5, pseudogene |
| [[ZNF702P]] | 0.644 | zinc finger protein 702, pseudogene |
| [[SPAG1]] | 0.632 | sperm associated antigen 1 |
| [[SLC16A9]] | 0.628 | solute carrier family 16 member 9 |
| [[CAMK2D]] | 0.628 | calcium/calmodulin dependent protein kinase II delta |
| [[TBC1D22B]] | 0.621 | TBC1 domain family member 22B |
| [[HHAT]] | 0.607 | hedgehog acyltransferase |
| [[GULP1]] | 0.606 | GULP PTB domain containing engulfment adaptor 1 |
| [[ETFRF1]] | 0.605 | electron transfer flavoprotein regulatory factor 1 |
| [[C21orf91]] | 0.603 | chromosome 21 open reading frame 91 |
| [[DHRS12]] | 0.602 | dehydrogenase/reductase 12 |
| [[STXBP3]] | 0.601 | syntaxin binding protein 3 |
| [[DLX2]] | 0.597 | distal-less homeobox 2 |
| [[NEXN]] | 0.582 | nexilin F-actin binding protein |
| [[TFAP2A]] | 0.564 | transcription factor AP-2 alpha |
| [[H2AJ]] | 0.555 | H2A.J histone |
| [[LINC00265]] | 0.549 | long independently transcribed non-coding RNA 265 |
| [[SPPL2A]] | 0.542 | signal peptide peptidase like 2A |
| [[GATA3]] | 0.538 | GATA binding protein 3 |
| [[HOXA7]] | 0.535 | homeobox A7 |
| [[CDKN2B-AS1]] | 0.534 | CDKN2B and CDKN2A antisense cis and trans regulatory RNA 1 |
| [[UST]] | 0.533 | uronyl 2-sulfotransferase |
| [[FOXA1]] | 0.531 | forkhead box A1 |
| [[PMAIP1]] | 0.529 | phorbol-12-myristate-13-acetate-induced protein 1 |
| [[STAT6]] | 0.525 | signal transducer and activator of transcription 6 |
| [[TRAPPC6B]] | 0.509 | trafficking protein particle complex subunit 6B |
| [[CLEC2D]] | 0.483 | C-type lectin domain family 2 member D |
| [[STX3]] | 0.433 | syntaxin 3 |
| [[TLCD4-RWDD3]] | 0.412 | TLCD4-RWDD3 readthrough |
| [[CCDC159]] | 0.383 | coiled-coil domain containing 159 |
| [[LRRC37A4P]] | 0.364 | leucine rich repeat containing 37 member A4, pseudogene |

## − arm (5)

| Gene | Projection | Name |
|---|---|---|
| [[ST6GALNAC4]] | -0.754 | ST6 N-acetylgalactosaminide alpha-2,6-sialyltransferase 4 |
| [[PHKA2]] | -0.737 | phosphorylase kinase regulatory subunit alpha 2 |
| [[YIPF1]] | -0.661 | Yip1 domain family member 1 |
| [[GNB1L]] | -0.658 | G protein subunit beta 1 like |
| [[TTLL5]] | -0.551 | tubulin tyrosine ligase like 5 |

## Data

- `graph/nodes.parquet` — module == 68; `graph/modules.parquet` — module == 68; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [67] (drug-dose × line)
