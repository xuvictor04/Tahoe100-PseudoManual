---
module: 38
type: "module"
n_genes: 122
n_plus: 122
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.2823379933834076
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 038

*122 genes (single-armed) · [[Module 038.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 37), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM (+10.8, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 5 µM (+5.3, ⚠ cell-cycle shift); [[Auranofin (drug)]] 5 µM (+4.4); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (+3.6, ⚠ cell-cycle shift); [[Epirubicin (hydrochloride) (drug)]] 5 µM (+2.8, ⚠ cell-cycle shift); [[Topotecan (hydrochloride) (drug)]] 5 µM (+2.7, ⚠ toxic; cell-cycle shift); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+2.4); [[Filgotinib (drug)]] 5 µM (+2.4); [[Homoharringtonine (drug)]] 0.5 µM (+2.2, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (+2.1, ⚠ cell-cycle shift); [[PF-06260933 (drug)]] 5 µM (+1.6); [[TAK-901 (drug)]] 0.05 µM (+1.6); [[Lactate (calcium) (drug)]] 5 µM (+1.5); [[Vilanterol (drug)]] 5 µM (+1.3); [[TAK-733 (drug)]] 0.05 µM (+1.3); [[5-Azacytidine (drug)]] 5 µM (+1.2); [[Pyridoxine (drug)]] 0.05 µM (+1.2) (31 in all, 13 with an alert ⚠; shown: the 10 strongest and the 7 next strongest without an alert)
- Lower it: [[Digitoxin (drug)]] 5 µM (-3.7, ⚠ toxic; transcription drop; cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (-3.4, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 0.5 µM (-3.2, ⚠ cell-cycle shift); [[Niclosamide (olamine) (drug)]] 5 µM (-2.6, ⚠ toxic; cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (-2.6, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (-2.5, ⚠ cell-cycle shift); [[NG25 (drug)]] 5 µM (-2.5, ⚠ cell-cycle shift); [[HI-TOPK-032 (drug)]] 0.05 µM (-2.2); [[Belumosudil (drug)]] 5 µM (-1.9); [[Radotinib (drug)]] 5 µM (-1.9); [[Pralsetinib (drug)]] 5 µM (-1.9); [[Dimethyl fumarate (drug)]] 5 µM (-1.8); [[Bexarotene (drug)]] 5 µM (-1.6); [[Pyridoxine (hydrochloride) (drug)]] 5 µM (-1.5); [[Infigratinib (drug)]] 0.05 µM (-1.3); [[Dexamethasone (drug)]] 5 µM (-1.3); [[Homoharringtonine (drug)]] 0.05 µM (-1.2) (37 in all, 11 with an alert ⚠; shown: the 10 strongest and the 7 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[NCI-H460 (line)]], [[SW480 (line)]], [[PANC-1 (line)]], [[HOP62 (line)]], [[NCI-H1573 (line)]], [[NCI-H23 (line)]], [[LoVo (line)]], [[HT-29 (line)]]

## + arm (122)

| Gene | Projection | Name |
|---|---|---|
| [[PILRA]] | 0.887 | paired immunoglobin like type 2 receptor alpha |
| [[ARL9]] | 0.885 | ARF like GTPase 9 |
| [[VWCE]] | 0.883 | von Willebrand factor C and EGF domains |
| [[ISY1-RAB43]] | 0.881 | ISY1-RAB43 readthrough |
| [[PYGM]] | 0.877 | glycogen phosphorylase, muscle associated |
| [[FNDC7]] | 0.877 | fibronectin type III domain containing 7 |
| [[IDI2-AS1]] | 0.857 | IDI2 antisense RNA 1 |
| [[TRIM72]] | 0.856 | tripartite motif containing 72 |
| [[SLC9A5]] | 0.843 | solute carrier family 9 member A5 |
| [[ORAI2]] | 0.834 | ORAI calcium release-activated calcium modulator 2 |
| [[RFPL3S]] | 0.833 | RFPL3 antisense |
| [[LINC00672]] | 0.822 | LASP1 neighbor |
| [[ADCY10P1]] | 0.821 | ADCY10 pseudogene 1 |
| [[PHYHD1]] | 0.814 | phytanoyl-CoA dioxygenase domain containing 1 |
| [[LINC01588]] | 0.812 | long independently transcribed non-coding RNA 1588 |
| [[SYCE2]] | 0.810 | synaptonemal complex central element protein 2 |
| [[AVIL]] | 0.807 | advillin |
| [[TINCR]] | 0.805 | TINCR ubiquitin domain containing |
| [[LRRC23]] | 0.804 | leucine rich repeat containing 23 |
| [[PPIEL-1]] | 0.804 | — |
| [[COL20A1]] | 0.800 | collagen type XX alpha 1 chain |
| [[PPIEL]] | 0.800 | peptidylprolyl isomerase E like (pseudogene) |
| [[ATP2A1]] | 0.799 | ATPase sarcoplasmic/endoplasmic reticulum Ca2+ transporting 1 |
| [[PYY]] | 0.786 | peptide YY |
| [[THUMPD3-AS1]] | 0.778 | THUMPD3 antisense RNA 1 |
| [[TTLL3]] | 0.773 | tubulin tyrosine ligase like 3 |
| [[FAM209A]] | 0.766 | family with sequence similarity 209 member A |
| [[SLC23A3]] | 0.757 | solute carrier family 23 member 3 |
| [[ZNF432]] | 0.754 | zinc finger protein 432 |
| [[ASIC4]] | 0.741 | acid sensing ion channel subunit family member 4 |
| [[ADORA1]] | 0.735 | adenosine A1 receptor |
| [[ROPN1L]] | 0.732 | rhophilin associated tail protein 1 like |
| [[LDHC]] | 0.731 | lactate dehydrogenase C |
| [[CHRNE]] | 0.719 | cholinergic receptor nicotinic epsilon subunit |
| [[SPRED3]] | 0.713 | sprouty related EVH1 domain containing 3 |
| [[INTS6]] | 0.712 | integrator complex subunit 6 |
| [[SLC22A20P]] | 0.711 | solute carrier family 22 member 20, pseudogene |
| [[C17orf100]] | 0.710 | chromosome 17 open reading frame 100 |
| [[SMBD1P]] | 0.708 | somatomedin B domain containing 1, pseudogene |
| [[SYCE1L]] | 0.706 | synaptonemal complex central element protein 1 like |
| [[TRPV1]] | 0.704 | transient receptor potential cation channel subfamily V member 1 |
| [[CFAP251]] | 0.703 | cilia and flagella associated protein 251 |
| [[C5AR1]] | 0.697 | complement C5a receptor 1 |
| [[SRRM5]] | 0.694 | serine/arginine repetitive matrix 5 |
| [[POU2F2]] | 0.694 | POU class 2 homeobox 2 |
| [[FGF18]] | 0.692 | fibroblast growth factor 18 |
| [[ADAMTSL4-AS2]] | 0.687 | ADAMTSL4 antisense RNA 2 |
| [[HYAL1]] | 0.683 | hyaluronidase 1 |
| [[LINC02245]] | 0.678 | long independently transcribed non-coding RNA 2245 |
| [[ITGA2B]] | 0.678 | integrin subunit alpha 2b |
| [[TFAP2E]] | 0.674 | transcription factor AP-2 epsilon |
| [[WNT2B]] | 0.673 | Wnt family member 2B |
| [[SPACDR]] | 0.670 | sperm acrosome developmental regulator |
| [[APRG1]] | 0.668 | APRG1 tumor suppressor candidate |
| [[UBE2CP5]] | 0.668 | ubiquitin conjugating enzyme E2 C pseudogene 5 |
| [[LNP1]] | 0.661 | leukemia NUP98 fusion partner 1 |
| [[PLCD4]] | 0.660 | phospholipase C delta 4 |
| [[LINC02804]] | 0.653 | — |
| [[C9]] | 0.652 | complement C9 |
| [[QRICH2]] | 0.642 | glutamine rich 2 |
| [[MON1B]] | 0.641 | MON1 vesicular trafficking associated B |
| [[EOGT]] | 0.634 | EGF domain specific O-linked N-acetylglucosamine transferase |
| [[CCDC168]] | 0.632 | leucine rich repeat transmembrane protein 3 |
| [[PTPN6]] | 0.631 | protein tyrosine phosphatase non-receptor type 6 |
| [[WTIP]] | 0.629 | WT1 interacting protein |
| [[WNK4]] | 0.625 | WNK lysine deficient protein kinase 4 |
| [[USE1]] | 0.624 | unconventional SNARE in the ER 1 |
| [[POLG2]] | 0.619 | DNA polymerase gamma 2, accessory subunit |
| [[TTLL13]] | 0.619 | tubulin tyrosine ligase like 13 |
| [[SIDT2]] | 0.617 | SID1 transmembrane family member 2 |
| [[IKZF4]] | 0.617 | IKAROS family zinc finger 4 |
| [[TRIM39]] | 0.617 | tripartite motif containing 39 |
| [[NHEJ1]] | 0.613 | non-homologous end joining factor 1 |
| [[LRP2BP-AS1]] | 0.613 | — |
| [[FES]] | 0.612 | FES proto-oncogene, tyrosine kinase |
| [[MUC20-OT1]] | 0.612 | MUC20 overlapping transcript |
| [[MIR22HG]] | 0.609 | MIR22 host gene |
| [[GAL3ST1]] | 0.606 | galactose-3-O-sulfotransferase 1 |
| [[LRIF1]] | 0.605 | ligand dependent nuclear receptor interacting factor 1 |
| [[NUFIP2]] | 0.604 | nuclear FMR1 interacting protein 2 |
| [[DMPK]] | 0.594 | DM1 protein kinase |
| [[CCDC97]] | 0.593 | coiled-coil domain containing 97 |
| [[C6orf62]] | 0.592 | chromosome 6 open reading frame 62 |
| [[NEU3]] | 0.591 | neuraminidase 3 |
| [[LINC01291]] | 0.575 | long independently transcribed non-coding RNA 1291 |
| [[CDKL1]] | 0.569 | cyclin dependent kinase like 1 |
| [[EEF1AKMT1]] | 0.569 | EEF1A lysine methyltransferase 1 |
| [[CEACAM19]] | 0.568 | CEA cell adhesion molecule 19 |
| [[USP36]] | 0.567 | ubiquitin specific peptidase 36 |
| [[WDR5B-DT]] | 0.564 | WDR5B divergent transcript |
| [[CDK13]] | 0.557 | cyclin dependent kinase 13 |
| [[PRRT3-AS1]] | 0.556 | PRRT3 antisense RNA 1 |
| [[STRADA]] | 0.556 | STE20 related adaptor alpha |
| [[FBXO10]] | 0.552 | F-box protein 10 |
| [[UBE2F-SCLY]] | 0.550 | UBE2F-SCLY readthrough (NMD candidate) |
| [[SPAG7]] | 0.545 | sperm associated antigen 7 |
| [[ASB3]] | 0.544 | ankyrin repeat and SOCS box containing 3 |
| [[AGO3]] | 0.541 | argonaute RISC catalytic component 3 |
| [[ING5]] | 0.538 | inhibitor of growth family member 5 |
| [[RRP12]] | 0.538 | ribosomal RNA processing 12 homolog |
| [[MLIP]] | 0.537 | muscular LMNA interacting protein |
| [[SAP30BP]] | 0.529 | SAP30 binding protein |
| [[ERFL]] | 0.528 | ETS repressor factor like |
| [[ST6GALNAC6-1]] | 0.516 | — |
| [[PNPLA7]] | 0.509 | patatin like domain 7, lysophospholipase |
| [[MSS51]] | 0.505 | MSS51 mitochondrial translational activator |
| [[NIM1K]] | 0.496 | NIM1 serine/threonine protein kinase |
| [[CENPBD2P]] | 0.491 | CENPB DNA-binding domains containing 2, pseudogene |
| [[RSKR]] | 0.489 | ribosomal protein S6 kinase related |
| [[PRPSAP1]] | 0.485 | phosphoribosyl pyrophosphate synthetase associated protein 1 |
| [[MICU2]] | -0.481 | mitochondrial calcium uptake 2 |
| [[MAP3K11]] | 0.466 | mitogen-activated protein kinase kinase kinase 11 |
| [[CCDC138]] | 0.464 | coiled-coil domain containing 138 |
| [[PHKG2]] | 0.430 | phosphorylase kinase catalytic subunit gamma 2 |
| [[FAHD2CP]] | -0.418 | fumarylacetoacetate hydrolase domain containing 2C, pseudogene |
| [[TECPR2]] | 0.405 | tectonin beta-propeller repeat containing 2 |
| [[CEMIP2]] | 0.399 | cell migration inducing hyaluronidase 2 |
| [[THSD1]] | 0.399 | thrombospondin type 1 domain containing 1 |
| [[ZNF584]] | 0.343 | zinc finger protein 584 |
| [[UGDH]] | 0.322 | UDP-glucose 6-dehydrogenase |
| [[CAMSAP1-DT]] | 0.295 | CAMSAP1 divergent transcript |
| [[DNAJC6]] | 0.282 | DnaJ heat shock protein family (Hsp40) member C6 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 38; `graph/modules.parquet` — module == 38; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [37] (drug-dose × line)
