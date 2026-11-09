---
module: 37
type: "module"
n_genes: 123
n_plus: 123
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.34035804867744446
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 037

*123 genes (single-armed) · [[Module 037.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 36), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM (+11.8, ⚠ cell-cycle shift); [[Auranofin (drug)]] 5 µM (+6.9); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (+6.5, ⚠ cell-cycle shift); [[Epirubicin (hydrochloride) (drug)]] 5 µM (+5.1, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (+3.3, ⚠ cell-cycle shift); [[GSK1059615 (drug)]] 5 µM (+3.2); [[Tucidinostat (drug)]] 5 µM (+3.1); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+3.0); [[Homoharringtonine (drug)]] 5 µM (+2.5, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 0.5 µM (+2.4, ⚠ cell-cycle shift); [[Ponatinib (drug)]] 5 µM (+1.8); [[Cobimetinib (drug)]] 5 µM (+1.8); [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM (+1.5); [[Cepharanthine (drug)]] 5 µM (+1.5); [[Bimiralisib (drug)]] 0.05 µM (+1.4); [[Lactate (calcium) (drug)]] 0.5 µM (+1.4) (35 in all, 15 with an alert ⚠; shown: the 10 strongest and the 6 next strongest without an alert)
- Lower it: [[Harringtonine (drug)]] 5 µM (-3.4, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (-2.7, ⚠ cell-cycle shift); [[Belumosudil (drug)]] 5 µM (-1.9); [[NG25 (drug)]] 5 µM (-1.9, ⚠ cell-cycle shift); [[Retinoic acid (drug)]] 0.05 µM (-1.9); [[c-Kit-IN-1 (drug)]] 0.05 µM (-1.8, ⚠ unreliable plate only); [[Berbamine (drug)]] 0.05 µM (-1.7); [[Pyridoxine (hydrochloride) (drug)]] 5 µM (-1.7); [[TAK-901 (drug)]] 5 µM (-1.7, ⚠ cell-cycle shift); [[Pralsetinib (drug)]] 5 µM (-1.7); [[Dimethyl fumarate (drug)]] 5 µM (-1.6); [[Infigratinib (drug)]] 0.05 µM (-1.6); [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM (-1.5); [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM (-1.3); [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM (-1.3) (37 in all, 16 with an alert ⚠; shown: the 10 strongest and the 5 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[SW480 (line)]], [[A498 (line)]], [[NCI-H460 (line)]], [[HOP62 (line)]], [[SW 900 (line)]], [[Panc 03.27 (line)]], [[MIA PaCa-2 (line)]], [[HS-578T (line)]]

## + arm (123)

| Gene | Projection | Name |
|---|---|---|
| [[WDR49]] | 0.906 | WD repeat domain 49 |
| [[SNX31]] | 0.888 | sorting nexin 31 |
| [[TMEM269]] | 0.851 | transmembrane protein 269 |
| [[LINC02680]] | 0.846 | long independently transcribed non-coding RNA 2680 |
| [[LINC02936]] | 0.834 | long independently transcribed non-coding RNA 2936 |
| [[PIWIL2]] | 0.830 | piwi like RNA-mediated gene silencing 2 |
| [[TMEM225B]] | 0.827 | transmembrane protein 225B |
| [[C9orf153]] | 0.819 | chromosome 9 open reading frame 153 |
| [[LINC00640]] | 0.817 | long independently transcribed non-coding RNA 640 |
| [[CCDC62]] | 0.813 | coiled-coil domain containing 62 |
| [[ADCY10]] | 0.811 | adenylate cyclase 10 |
| [[CFAP53]] | 0.809 | cilia and flagella associated protein 53 |
| [[PHKG1]] | 0.801 | phosphorylase kinase catalytic subunit gamma 1 |
| [[CORIN]] | 0.799 | corin, serine peptidase |
| [[LINC01482]] | 0.798 | long independently transcribed non-coding RNA 1482 |
| [[TICAM2]] | 0.797 | TIR domain containing adaptor molecule 2 |
| [[TEX29]] | 0.796 | testis expressed 29 |
| [[DRC1]] | 0.792 | dynein regulatory complex subunit 1 |
| [[EFCAB12]] | 0.783 | EF-hand calcium binding domain 12 |
| [[DCAF4L1]] | 0.777 | DDB1 and CUL4 associated factor 4 like 1 |
| [[KLRD1]] | 0.772 | killer cell lectin like receptor D1 |
| [[MIA]] | 0.768 | MIA SH3 domain containing |
| [[CD200R1]] | 0.766 | CD200 receptor 1 |
| [[PLD5P1]] | 0.765 | PLD5 pseudogene 1 |
| [[RRH]] | 0.757 | retinal pigment epithelium-derived rhodopsin homolog |
| [[TNXB]] | 0.757 | tenascin XB |
| [[ADAM20P1]] | 0.754 | ADAM metallopeptidase domain 20 pseudogene 1 |
| [[FRZB]] | 0.748 | frizzled related protein |
| [[FLJ46284]] | 0.743 | — |
| [[LINC00862]] | 0.739 | long independently transcribed non-coding RNA 862 |
| [[ADAM20]] | 0.738 | ADAM metallopeptidase domain 20 |
| [[ECT2L]] | 0.738 | epithelial cell transforming 2 like |
| [[CD247]] | 0.736 | CD247 molecule |
| [[LVRN]] | 0.735 | laeverin |
| [[SPX]] | 0.732 | spexin hormone |
| [[CMYA5]] | 0.731 | cardiomyopathy associated 5 |
| [[BNIPL]] | 0.731 | BCL2 interacting protein like |
| [[DNHD1]] | 0.728 | dynein heavy chain domain 1 |
| [[PXDNL]] | 0.722 | peroxidasin like |
| [[MAP7D2]] | 0.720 | MAP7 domain containing 2 |
| [[TNFSF13B]] | 0.711 | TNF superfamily member 13b |
| [[NPHP3-ACAD11]] | 0.707 | NPHP3-ACAD11 readthrough (NMD candidate) |
| [[RSPH9]] | 0.707 | radial spoke head component 9 |
| [[NOXRED1]] | 0.705 | NADP dependent oxidoreductase domain containing 1 |
| [[LINC00159]] | 0.705 | long independently transcribed non-coding RNA 159 |
| [[CDC20-DT]] | 0.704 | CDC20 divergent transcript |
| [[KLRA1P]] | 0.698 | killer cell lectin like receptor A1, pseudogene |
| [[TSNAX-DISC1]] | 0.697 | TSNAX-DISC1 readthrough (NMD candidate) |
| [[LSMEM1]] | 0.693 | leucine rich single-pass membrane protein 1 |
| [[ZNF547]] | 0.681 | zinc finger protein 547 |
| [[PPP1R32]] | 0.679 | stabilizer of axonemal microtubules 4 |
| [[MCF2]] | 0.679 | MCF.2 cell line derived transforming sequence |
| [[ZNF814]] | 0.668 | zinc finger protein 814 |
| [[L3MBTL1]] | 0.666 | L3MBTL histone methyl-lysine binding protein 1 |
| [[BET1]] | 0.663 | Bet1 golgi vesicular membrane trafficking protein |
| [[TBX19]] | 0.661 | T-box transcription factor 19 |
| [[GRK7]] | 0.656 | G protein-coupled receptor kinase 7 |
| [[CCDC13]] | 0.654 | coiled-coil domain containing 13 |
| [[METTL21EP-1]] | 0.646 | — |
| [[LEPR]] | 0.646 | leptin receptor |
| [[ZNNT1]] | 0.643 | ZNF706 neighboring transcript 1 |
| [[LINC00310]] | 0.639 | long independently transcribed non-coding RNA 310 |
| [[GUCA1B]] | 0.635 | guanylate cyclase activator 1B |
| [[GPC5]] | 0.634 | glypican 5 |
| [[PLAC1]] | 0.633 | placenta associated 1 |
| [[GET1-SH3BGR]] | 0.630 | GET1-SH3BGR readthrough |
| [[AS3MT]] | 0.630 | arsenite methyltransferase |
| [[MMP24OS]] | 0.628 | MMP24 opposite strand |
| [[CLEC4A]] | 0.621 | C-type lectin domain family 4 member A |
| [[TTC28-AS1]] | 0.619 | TTC28 antisense RNA 1 |
| [[HERC4]] | 0.613 | HECT and RLD domain containing E3 ubiquitin protein ligase 4 |
| [[UBAP1L]] | 0.610 | ubiquitin associated protein 1 like |
| [[PLSCR2]] | 0.605 | phospholipid scramblase 2 |
| [[BRD7]] | -0.597 | bromodomain containing 7 |
| [[TMEM161B-DT]] | 0.596 | TMEM161B divergent transcript |
| [[IQCJ]] | 0.592 | IQ motif containing J |
| [[ZNF248]] | 0.586 | zinc finger protein 248 |
| [[ZNF473CR]] | 0.585 | ZNF473 cis regulating lncRNA |
| [[TPT1-AS1]] | 0.584 | TPT1 antisense RNA 1 |
| [[LINC01422]] | 0.577 | long independently transcribed non-coding RNA 1422 |
| [[FAM229A]] | 0.574 | family with sequence similarity 229 member A |
| [[BCO2]] | 0.564 | beta-carotene oxygenase 2 |
| [[CHURC1-FNTB]] | 0.563 | CHURC1-FNTB readthrough |
| [[SCIRT]] | 0.562 | stem cell inhibitory RNA transcript |
| [[SNED1-AS1]] | 0.557 | SNED1 antisense RNA 1 |
| [[TMCO3]] | 0.552 | solute carrier family 9 member D1 |
| [[SH3BGR]] | 0.550 | SH3 domain binding glutamate rich protein |
| [[AGAP5]] | 0.542 | ArfGAP with GTPase domain, ankyrin repeat and PH domain 5 |
| [[DYNLT2B]] | 0.542 | dynein light chain Tctex-type 2B |
| [[TNNI3K]] | 0.541 | TNNI3 interacting kinase |
| [[GRK3]] | 0.540 | G protein-coupled receptor kinase 3 |
| [[KAZN]] | 0.540 | kazrin, periplakin interacting protein |
| [[SMG1P7]] | 0.539 | SMG1 pseudogene 7 |
| [[RPL34-DT]] | 0.530 | RPL34 divergent transcript |
| [[INTS4P1]] | 0.524 | integrator complex subunit 4 pseudogene 1 |
| [[RAB4B]] | 0.523 | RAB4B, member RAS oncogene family |
| [[RASA4B]] | 0.516 | RAS p21 protein activator 4B |
| [[LINC01950]] | 0.512 | long independently transcribed non-coding RNA 1950 |
| [[LINC02036]] | 0.512 | — |
| [[LSP1P5-1]] | 0.508 | — |
| [[ACVR1C]] | 0.507 | activin A receptor type 1C |
| [[AOC2]] | 0.505 | amine oxidase copper containing 2 |
| [[PPP2R2D]] | 0.504 | protein phosphatase 2 regulatory subunit Bdelta |
| [[RBM44]] | 0.504 | RNA binding motif protein 44 |
| [[DNAI7]] | 0.503 | dynein axonemal intermediate chain 7 |
| [[DAGLA]] | -0.503 | diacylglycerol lipase alpha |
| [[EXD3]] | 0.490 | exonuclease 3'-5' domain containing 3 |
| [[IQUB]] | 0.488 | IQ motif and ubiquitin domain containing |
| [[LINC01118]] | 0.484 | long independently transcribed non-coding RNA 1118 |
| [[CCDC146]] | 0.477 | coiled-coil domain containing 146 |
| [[USP49]] | 0.473 | ubiquitin specific peptidase 49 |
| [[CYP27A1]] | 0.473 | cytochrome P450 family 27 subfamily A member 1 |
| [[LINC02885]] | 0.464 | long independently transcribed non-coding RNA 2885 |
| [[OVGP1]] | 0.457 | oviductal glycoprotein 1 |
| [[CRYGS]] | 0.449 | crystallin gamma S |
| [[DISC1]] | 0.441 | DISC1 scaffold protein |
| [[LINC00595]] | 0.421 | long independently transcribed non-coding RNA 595 |
| [[DEAF1]] | 0.418 | DEAF1 transcription factor |
| [[CTSK]] | 0.396 | cathepsin K |
| [[TMEM178A]] | 0.365 | transmembrane protein 178A |
| [[LINC01234]] | 0.349 | long independently transcribed non-coding RNA 1234 |
| [[LINC02112]] | 0.324 | long independently transcribed non-coding RNA 2112 |
| [[LINC02656]] | 0.318 | long independently transcribed non-coding RNA 2656 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 37; `graph/modules.parquet` — module == 37; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [36] (drug-dose × line)
