---
module: 53
type: "module"
n_genes: 88
n_plus: 88
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 053

*88 genes (single-armed) · [[Module 053.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 52), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM (+15.8, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 5 µM (+14.2, ⚠ cell-cycle shift); [[Auranofin (drug)]] 5 µM (+8.9); [[Dinaciclib (drug)]] 5 µM (+8.4, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (+6.9, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+6.5, ⚠ toxic; transcription drop; cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (+5.7, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (+5.3, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (+4.7); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+4.4); [[Filgotinib (drug)]] 5 µM (+2.5); [[TAK-901 (drug)]] 0.05 µM (+2.3); [[PF-06260933 (drug)]] 5 µM (+1.7); [[Docetaxel (Trihydrate) (drug)]] 0.5 µM (+1.6); [[Lactate (calcium) (drug)]] 5 µM (+1.5); [[Thymol (drug)]] 0.5 µM (+1.4); [[EX229 (drug)]] 5 µM (+1.3) (46 in all, 24 with an alert ⚠; shown: the 10 strongest and the 7 next strongest without an alert)
- Lower it: [[Digitoxin (drug)]] 0.5 µM (-2.4, ⚠ cell-cycle shift); [[NG25 (drug)]] 5 µM (-2.1, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 0.05 µM (-1.7, ⚠ cell-cycle shift); [[Radotinib (drug)]] 5 µM (-1.6); [[HI-TOPK-032 (drug)]] 0.05 µM (-1.5); [[Pyridoxine (hydrochloride) (drug)]] 5 µM (-1.4); [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM (-1.3); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (-1.3, ⚠ cell-cycle shift); [[Dexamethasone (drug)]] 0.5 µM (-1.3); [[LB-100 (drug)]] 0.05 µM (-1.3); [[Balsalazide (sodium hydrate) (drug)]] 0.05 µM (-1.3); [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM (-1.2); [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM (-1.2); [[Lucanthone (drug)]] 0.05 µM (-1.2) (35 in all, 8 with an alert ⚠; shown: the 10 strongest and the 4 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[NCI-H460 (line)]], [[NCI-H23 (line)]], [[LoVo (line)]], [[HS-578T (line)]], [[SW480 (line)]], [[A498 (line)]], [[SK-MEL-2 (line)]], [[C32 (line)]]

## + arm (88)

| Gene | Projection | Name |
|---|---|---|
| [[MIR9-1HG]] | 0.876 | MIR9-1 host gene |
| [[CATSPERD]] | 0.868 | catsper channel auxiliary subunit delta |
| [[CPT1C]] | 0.865 | carnitine palmitoyltransferase 1C |
| [[NUP210L]] | 0.861 | nucleoporin 210 like |
| [[GRIK5]] | 0.854 | glutamate ionotropic receptor kainate type subunit 5 |
| [[CPNE9]] | 0.852 | copine family member 9 |
| [[KIF17]] | 0.851 | kinesin family member 17 |
| [[PPP1R36]] | 0.846 | protein phosphatase 1 regulatory subunit 36 |
| [[GRAMD2A]] | 0.839 | GRAM domain containing 2A |
| [[TMPRSS9]] | 0.838 | transmembrane serine protease 9 |
| [[AXDND1]] | 0.838 | axonemal dynein light chain domain containing 1 |
| [[ELAVL3]] | 0.836 | ELAV like RNA binding protein 3 |
| [[L3MBTL2-AS1]] | 0.834 | L3MBTL2 antisense RNA 1 |
| [[IL12RB2]] | 0.825 | interleukin 12 receptor subunit beta 2 |
| [[SLC8A2]] | 0.823 | solute carrier family 8 member A2 |
| [[EPHA1-AS1]] | 0.819 | EPHA1 antisense RNA 1 |
| [[PEBP4]] | 0.818 | phosphatidylethanolamine binding protein 4 |
| [[CCNP]] | 0.813 | cyclin P |
| [[SLC4A10]] | 0.811 | solute carrier family 4 member 10 |
| [[SEC1P]] | 0.805 | fucosyltransferase 2B, pseudogene |
| [[AZU1]] | 0.802 | azurocidin 1 |
| [[PLA2G12B]] | 0.802 | phospholipase A2 group XIIB |
| [[DNAH10]] | 0.801 | dynein axonemal heavy chain 10 |
| [[MASP2]] | 0.800 | MBL associated serine protease 2 |
| [[LINC00393]] | 0.793 | long independently transcribed non-coding RNA 393 |
| [[C2CD6]] | 0.788 | catsper channel auxiliary subunit tau |
| [[IRAG1-AS1]] | 0.786 | IRAG1 antisense RNA 1 |
| [[SYT16]] | 0.776 | synaptotagmin 16 |
| [[PKD1L1]] | 0.773 | polycystin 1 like 1, transient receptor potential channel interacting |
| [[PRRT3]] | 0.766 | proline rich transmembrane protein 3 |
| [[ASGR1]] | 0.762 | asialoglycoprotein receptor 1 |
| [[ITGA9]] | 0.745 | integrin subunit alpha 9 |
| [[CNBD2]] | 0.735 | cyclic nucleotide binding domain containing 2 |
| [[LINC02955]] | 0.733 | long independently transcribed non-coding RNA 2955 |
| [[HVCN1]] | 0.732 | hydrogen voltage gated channel 1 |
| [[PRX]] | 0.730 | periaxin |
| [[LINC03036]] | 0.724 | long independently transcribed non-coding RNA 3036 |
| [[LINC00880]] | 0.721 | long independently transcribed non-coding RNA 880 |
| [[TG]] | 0.719 | thyroglobulin |
| [[SEMA4A]] | 0.719 | semaphorin 4A |
| [[EFNA2]] | 0.718 | ephrin A2 |
| [[APC2]] | 0.715 | APC regulator of Wnt signaling pathway 2 |
| [[FLRT1]] | 0.712 | fibronectin leucine rich transmembrane protein 1 |
| [[LINC00616]] | 0.705 | long independently transcribed non-coding RNA 616 |
| [[DHDH]] | 0.704 | dihydrodiol dehydrogenase |
| [[LINC02901]] | 0.703 | long independently transcribed non-coding RNA 2901 |
| [[TTC23L]] | 0.698 | tetratricopeptide repeat domain 23 like |
| [[LRRC56]] | 0.691 | leucine rich repeat containing 56 |
| [[GSG1L]] | 0.689 | GSG1 like |
| [[F2]] | 0.679 | coagulation factor II, thrombin |
| [[PDE4C]] | 0.677 | phosphodiesterase 4C |
| [[PRKCG]] | 0.676 | protein kinase C gamma |
| [[SLC26A4]] | 0.669 | solute carrier family 26 member 4 |
| [[MEI1]] | 0.667 | meiotic double-stranded break formation protein 1 |
| [[AMZ1]] | 0.657 | archaelysin family metallopeptidase 1 |
| [[LHX4]] | 0.654 | LIM homeobox 4 |
| [[SAMD14]] | 0.649 | sterile alpha motif domain containing 14 |
| [[KPTN]] | 0.645 | kaptin, actin binding protein |
| [[HCN2]] | 0.641 | hyperpolarization activated cyclic nucleotide gated potassium and sodium channel 2 |
| [[PARD6G-AS1]] | 0.641 | PARD6G antisense RNA 1 |
| [[GGT1]] | 0.638 | gamma-glutamyltransferase 1 |
| [[GP6]] | 0.630 | glycoprotein VI platelet |
| [[STPG4]] | 0.627 | sperm-tail PG-rich repeat containing 4 |
| [[GDF1]] | 0.614 | growth differentiation factor 1 |
| [[CCDC28B]] | 0.610 | coiled-coil domain containing 28B |
| [[RUNDC3A-AS1]] | 0.609 | RUNDC3A antisense RNA 1 |
| [[LAG3]] | 0.609 | lymphocyte activating 3 |
| [[DLG4]] | 0.606 | discs large MAGUK scaffold protein 4 |
| [[SYT5]] | 0.604 | synaptotagmin 5 |
| [[DDR2]] | 0.569 | discoidin domain receptor tyrosine kinase 2 |
| [[PMVK]] | 0.564 | phosphomevalonate kinase |
| [[CDKL2]] | 0.562 | cyclin dependent kinase like 2 |
| [[ARF4-AS1]] | 0.559 | ARF4 antisense RNA 1 |
| [[SLC2A14]] | 0.554 | solute carrier family 2 member 14 |
| [[RAB7A]] | 0.542 | RAB7A, member RAS oncogene family |
| [[DYSF]] | 0.542 | dysferlin |
| [[CAPN12]] | 0.539 | calpain 12 |
| [[MRC2]] | 0.496 | mannose receptor C-type 2 |
| [[SSC5D]] | 0.491 | scavenger receptor cysteine rich family member with 5 domains |
| [[CASKIN1]] | 0.484 | CASK interacting protein 1 |
| [[AOX1]] | 0.484 | aldehyde oxidase 1 |
| [[MYO7A]] | 0.482 | myosin VIIA |
| [[CFAP45]] | 0.480 | cilia and flagella associated protein 45 |
| [[MAPK8IP1]] | 0.472 | mitogen-activated protein kinase 8 interacting protein 1 |
| [[HORMAD2-AS1]] | 0.431 | HORMAD2 and MTMR3 antisense RNA 1 |
| [[KCNMB4]] | 0.397 | potassium calcium-activated channel subfamily M regulatory beta subunit 4 |
| [[LINC02257]] | 0.395 | — |
| [[PYROXD2]] | 0.388 | pyridine nucleotide-disulphide oxidoreductase domain 2 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 53; `graph/modules.parquet` — module == 53; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [52] (drug-dose × line)
