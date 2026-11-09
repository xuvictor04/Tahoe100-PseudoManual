---
module: 44
type: "module"
n_genes: 102
n_plus: 102
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.2855507731437683
label: "Defective GALNT12 causes CRCS1"
label_source: "reactome"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 044

*Defective GALNT12 causes CRCS1 · 102 genes (single-armed) · [[Module 044.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

Label from the validation stage: **Defective GALNT12 causes CRCS1** (reactome, q 1e-05; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | Defective GALNT12 causes CRCS1 | reactome | 5/102 | 56.8 | 1e-05 |
| all | Defective GALNT3 causes HFTC | reactome | 5/102 | 56.8 | 1e-05 |
| + | Defective GALNT3 causes HFTC | reactome | 5/102 | 56.8 | 1e-05 |
| + | Defective GALNT12 causes CRCS1 | reactome | 5/102 | 56.8 | 1e-05 |
| all | Defective C1GALT1C1 causes TNPS | reactome | 5/102 | 52.8 | 2e-05 |
| + | Defective C1GALT1C1 causes TNPS | reactome | 5/102 | 52.8 | 2e-05 |
| + | Dectin-2 family | reactome | 5/102 | 43.5 | 5e-05 |
| all | Dectin-2 family | reactome | 5/102 | 43.5 | 5e-05 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 43), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Dinaciclib (drug)]] 5 µM (+9.1, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (+8.8, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+6.2, ⚠ toxic; transcription drop; cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (+6.2, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (+5.2); [[Tucidinostat (drug)]] 0.5 µM (+3.5, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 5 µM (+2.8, ⚠ cell-cycle shift); [[Docetaxel (drug)]] 0.05 µM (+2.8, ⚠ transcription drop; cell-cycle shift); [[XRK3F2 (drug)]] 0.5 µM (+2.2); [[Trametinib (drug)]] 0.5 µM (+2.1); [[Ipatasertib (drug)]] 0.5 µM (+2.0); [[Binimetinib (drug)]] 5 µM (+1.9); [[Cobimetinib (drug)]] 5 µM (+1.9); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM (+1.8); [[Entrectinib (drug)]] 5 µM (+1.8); [[Ponatinib (drug)]] 0.5 µM (+1.8); [[Bimiralisib (drug)]] 0.5 µM (+1.7) (67 in all, 24 with an alert ⚠; shown: the 10 strongest and the 7 next strongest without an alert)
- Lower it: [[Digitoxin (drug)]] 0.5 µM (-3.0, ⚠ cell-cycle shift); [[c-Kit-IN-1 (drug)]] 0.05 µM (-2.0, ⚠ unreliable plate only); [[BAY1125976 (drug)]] 5 µM (-1.9); [[Ouabain (Octahydrate) (drug)]] 5 µM (-1.8, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (-1.7, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-1.7, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 0.05 µM (-1.6, ⚠ cell-cycle shift); [[Dabrafenib (drug)]] 5 µM (-1.6); [[5-Azacytidine (drug)]] 5 µM (-1.6); [[Mebendazole (drug)]] 5 µM (-1.6); [[Sapanisertib (drug)]] 5 µM (-1.5); [[Fenofibrate (drug)]] 0.05 µM (-1.5); [[Erlotinib (drug)]] 0.05 µM (-1.5); [[Lucanthone (drug)]] 0.05 µM (-1.4); [[Artesunate (drug)]] 0.5 µM (-1.4); [[Dexamethasone (drug)]] 0.5 µM (-1.4) (44 in all, 10 with an alert ⚠; shown: the 10 strongest and the 6 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[COLO 205 (line)]], [[LoVo (line)]], [[HT-29 (line)]], [[LS 180 (line)]], [[NCI-H23 (line)]], [[KATO III (line)]], [[HOP62 (line)]], [[Hs 766T (line)]]

## Candidate new members

*Members not annotated to the set their arm is enriched for, ranked by mean cos to the annotated members (`validation/novel_members.csv`); ⚠ = a reason to doubt the gene's place (in the vector space only through flagged drug-doses), kept in its rank. 58 candidates, none with an alert; shown: the 15 strongest.*

| # | Gene | Set | Mean cos |
|---|---|---|---|
| 1 | [[PRR15-DT]] | Glucuronidation | +0.70 |
| 2 | [[MGAM2]] | Glucuronidation | +0.69 |
| 3 | [[GNA14]] | Glucuronidation | +0.68 |
| 4 | [[MUC13]] | Glucuronidation | +0.67 |
| 5 | [[MUC5B]] | Glucuronidation | +0.66 |
| 6 | [[PRR15L]] | Defective GALNT12 causes CRCS1 | +0.66 |
| 7 | [[MECOM]] | Glucuronidation | +0.65 |
| 8 | [[CFTR]] | Defective GALNT12 causes CRCS1 | +0.64 |
| 9 | [[GPA33]] | Defective GALNT12 causes CRCS1 | +0.64 |
| 10 | [[PTPRB]] | Glucuronidation | +0.64 |
| 11 | [[ST6GALNAC1]] | Defective GALNT12 causes CRCS1 | +0.64 |
| 12 | [[LGALS4]] | Defective GALNT12 causes CRCS1 | +0.63 |
| 13 | [[PLEKHG6]] | Defective GALNT12 causes CRCS1 | +0.63 |
| 14 | [[FXYD3]] | Defective GALNT12 causes CRCS1 | +0.63 |
| 15 | [[UGT1A1]] | Defective GALNT12 causes CRCS1 | +0.63 |

## + arm (102)

| Gene | Projection | Name |
|---|---|---|
| [[PRR15L]] | 0.882 | proline rich 15 like |
| [[UGT1A1]] | 0.881 | UDP glucuronosyltransferase family 1 member A1 |
| [[TSPAN8]] | 0.864 | tetraspanin 8 |
| [[PRR15]] | 0.863 | proline rich 15 |
| [[LGALS4]] | 0.858 | galectin 4 |
| [[ST6GALNAC1]] | 0.854 | ST6 N-acetylgalactosaminide alpha-2,6-sialyltransferase 1 |
| [[PLEKHG6]] | 0.840 | pleckstrin homology and RhoGEF domain containing G6 |
| [[FXYD3]] | 0.837 | FXYD domain containing ion transport regulator 3 |
| [[GPA33]] | 0.829 | glycoprotein A33 |
| [[CFTR]] | 0.825 | CF transmembrane conductance regulator |
| [[PPP1R1B]] | 0.820 | protein phosphatase 1 regulatory inhibitor subunit 1B |
| [[MUC3A]] | 0.819 | mucin 3A, cell surface associated |
| [[MUC13]] | 0.819 | mucin 13, cell surface associated |
| [[UGT1A6]] | 0.811 | UDP glucuronosyltransferase family 1 member A6 |
| [[CLDN3]] | 0.810 | claudin 3 |
| [[LINC02331]] | 0.809 | long independently transcribed non-coding RNA 2331 |
| [[MUC5B]] | 0.801 | mucin 5B, oligomeric mucus/gel-forming |
| [[TJP3]] | 0.800 | tight junction protein 3 |
| [[SLC40A1]] | 0.798 | solute carrier family 40 member 1 |
| [[AGR3]] | 0.795 | anterior gradient 3, protein disulphide isomerase family member |
| [[ATP10B]] | 0.793 | ATPase phospholipid transporting 10B (putative) |
| [[CDH17]] | 0.792 | cadherin 17 |
| [[CYP4F12]] | 0.790 | cytochrome P450 family 4 subfamily F member 12 |
| [[UGT1A9]] | 0.768 | UDP glucuronosyltransferase family 1 member A9 |
| [[HNF1A-AS1]] | 0.768 | HNF1A antisense RNA 1 |
| [[NPNT]] | 0.756 | nephronectin |
| [[TM4SF4]] | 0.750 | transmembrane 4 L six family member 4 |
| [[FGFR2]] | 0.740 | fibroblast growth factor receptor 2 |
| [[MGAM2]] | 0.736 | maltase-glucoamylase 2 (putative) |
| [[UGT1A8]] | 0.730 | UDP glucuronosyltransferase family 1 member A8 |
| [[MANSC1]] | 0.728 | MANSC domain containing 1 |
| [[PROM2]] | 0.723 | prominin 2 |
| [[ILDR2]] | 0.719 | immunoglobulin like domain containing receptor 2 |
| [[PRR15-DT]] | 0.719 | PRR15 divergent transcript |
| [[PCK1]] | 0.719 | phosphoenolpyruvate carboxykinase 1 |
| [[TSPAN1]] | 0.716 | tetraspanin 1 |
| [[LYZ]] | 0.714 | lysozyme |
| [[VIPR1]] | 0.707 | vasoactive intestinal peptide receptor 1 |
| [[PIGR]] | 0.704 | polymeric immunoglobulin receptor |
| [[MUC12]] | 0.692 | mucin 12, cell surface associated |
| [[RSPH1]] | 0.684 | radial spoke head component 1 |
| [[ATP8B1]] | 0.684 | ATPase phospholipid transporting 8B1 |
| [[PLAAT3]] | 0.683 | phospholipase A and acyltransferase 3 |
| [[CKMT1B]] | 0.682 | creatine kinase, mitochondrial 1B |
| [[CRACDL]] | 0.673 | CRACD like |
| [[CKMT1A]] | 0.668 | creatine kinase, mitochondrial 1A |
| [[PLA2G2A]] | 0.666 | phospholipase A2 group IIA |
| [[LINC01133]] | 0.650 | long independently transcribed non-coding RNA 1133 |
| [[LRP4]] | 0.649 | LDL receptor related protein 4 |
| [[PLAC8]] | 0.647 | placenta associated 8 |
| [[PIK3C2B]] | 0.641 | phosphatidylinositol-4-phosphate 3-kinase catalytic subunit type 2 beta |
| [[MYB]] | 0.641 | MYB proto-oncogene, transcription factor |
| [[BCL2L14]] | 0.639 | BCL2 like 14 |
| [[SH3BGRL2]] | 0.631 | SH3 domain binding glutamate rich protein like 2 |
| [[RAB25]] | 0.629 | RAB25, member RAS oncogene family |
| [[GNA14]] | 0.627 | G protein subunit alpha 14 |
| [[MECOM]] | 0.625 | MDS1 and EVI1 complex locus |
| [[KRT20]] | 0.620 | keratin 20 |
| [[PHGR1]] | 0.617 | proline, histidine and glycine rich 1 |
| [[PKDCC]] | 0.610 | protein kinase domain containing, cytoplasmic |
| [[ALDH3A1]] | 0.606 | aldehyde dehydrogenase 3 family member A1 |
| [[RAB15]] | 0.593 | RAB15, member RAS oncogene family |
| [[AOAH]] | 0.589 | acyloxyacyl hydrolase |
| [[LDLRAD4]] | 0.578 | low density lipoprotein receptor class A domain containing 4 |
| [[KLK7]] | 0.567 | kallikrein related peptidase 7 |
| [[CGN]] | 0.567 | cingulin |
| [[CALML4]] | 0.560 | calmodulin like 4 |
| [[PPFIBP2]] | 0.560 | PPFIB scaffold protein 2 |
| [[PTPRB]] | 0.558 | protein tyrosine phosphatase receptor type B |
| [[SLC12A2]] | 0.551 | solute carrier family 12 member 2 |
| [[CDC42EP5]] | 0.546 | CDC42 effector protein 5 |
| [[SMPDL3B]] | 0.543 | sphingomyelin phosphodiesterase acid like 3B |
| [[GALM]] | 0.533 | galactose mutarotase |
| [[MSLN]] | 0.532 | mesothelin |
| [[DTX4]] | 0.518 | deltex E3 ubiquitin ligase 4 |
| [[KCNQ1]] | 0.516 | potassium voltage-gated channel subfamily Q member 1 |
| [[ADD3-AS1]] | 0.503 | ADD3 antisense RNA 1 |
| [[LINC02967]] | 0.493 | long independently transcribed non-coding RNA 2967 |
| [[EPCAM]] | 0.490 | epithelial cell adhesion molecule |
| [[APOH]] | 0.487 | apolipoprotein H |
| [[USP54]] | 0.486 | ubiquitin specific peptidase 54 |
| [[AZGP1]] | 0.483 | alpha-2-glycoprotein 1, zinc-binding |
| [[YBX2]] | 0.478 | Y-box binding protein 2 |
| [[MUC6]] | 0.478 | mucin 6, oligomeric mucus/gel-forming (gene/pseudogene) |
| [[CREB3L1]] | 0.470 | cAMP responsive element binding protein 3 like 1 |
| [[NCMAP]] | 0.462 | non-compact myelin associated protein |
| [[MAP3K20]] | -0.461 | mitogen-activated protein kinase kinase kinase 20 |
| [[NR3C2]] | 0.442 | nuclear receptor subfamily 3 group C member 2 |
| [[PRKCH-AS1]] | 0.437 | PRKCH antisense RNA 1 |
| [[FGFR4]] | 0.436 | fibroblast growth factor receptor 4 |
| [[AMOT]] | 0.430 | angiomotin |
| [[TCEA3]] | 0.426 | transcription elongation factor A3 |
| [[SOD3]] | 0.424 | superoxide dismutase 3 |
| [[MAPRE2]] | 0.409 | microtubule associated protein RP/EB family member 2 |
| [[CD2AP]] | 0.402 | CD2 associated protein |
| [[SPINT2]] | 0.392 | serine peptidase inhibitor, Kunitz type 2 |
| [[TMEM54]] | 0.392 | transmembrane protein 54 |
| [[AKR1B10]] | 0.389 | aldo-keto reductase family 1 member B10 |
| [[ENTPD2]] | 0.374 | ectonucleoside triphosphate diphosphohydrolase 2 |
| [[TUFT1]] | 0.363 | tuftelin 1 |
| [[COL9A3]] | 0.338 | collagen type IX alpha 3 chain |
| [[AP1M2]] | 0.301 | adaptor related protein complex 1 subunit mu 2 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 44; `graph/modules.parquet` — module == 44; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [43] (drug-dose × line)
