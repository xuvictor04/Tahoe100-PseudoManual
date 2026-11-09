---
module: 82
type: "module"
n_genes: 55
n_plus: 55
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.2807154357433319
label: "Muscle contraction"
label_source: "reactome"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 082

*Muscle contraction · 55 genes (single-armed) · [[Module 082.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

Label from the validation stage: **Muscle contraction** (reactome, q 0.004; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | Muscle contraction | reactome | 6/55 | 12.7 | 0.004 |
| + | Muscle contraction | reactome | 6/55 | 12.7 | 0.004 |
| + | Cardiac conduction | reactome | 5/55 | 16.5 | 0.006 |
| all | Cardiac conduction | reactome | 5/55 | 16.5 | 0.006 |
| + | Kinesins | reactome | 4/55 | 22.8 | 0.012 |
| all | Kinesins | reactome | 4/55 | 22.8 | 0.012 |
| all | Phase 0 - rapid depolarisation | reactome | 3/55 | 35.8 | 0.029 |
| + | Phase 0 - rapid depolarisation | reactome | 3/55 | 35.8 | 0.029 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 81), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Tucidinostat (drug)]] 5 µM (+12.7); [[Panobinostat (drug)]] 5 µM (+10.0, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (+9.3, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 0.5 µM (+8.2, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (+8.0, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (+8.0, ⚠ toxic; transcription drop; cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (+7.5, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (+7.4, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (+6.9, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+4.8, ⚠ toxic; transcription drop; cell-cycle shift); [[Brivudine (drug)]] 5 µM (+4.1); [[Tucidinostat (drug)]] 0.05 µM (+2.3); [[Brivudine (drug)]] 0.5 µM (+1.8); [[Auranofin (drug)]] 5 µM (+1.7); [[XRK3F2 (drug)]] 0.5 µM (+1.5); [[Ponatinib (drug)]] 0.5 µM (+1.5); [[Ponatinib (drug)]] 5 µM (+1.5); [[Ipatasertib (drug)]] 0.5 µM (+1.4); [[Saquinavir (drug)]] 5 µM (+1.1) (38 in all, 22 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)
- Lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM (-4.7, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 0.5 µM (-4.6, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (-3.4, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (-3.2, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-3.2, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 0.05 µM (-2.6, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 0.05 µM (-2.5, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-2.3, ⚠ cell-cycle shift); [[TAK-901 (drug)]] 5 µM (-2.1, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 5 µM (-2.0, ⚠ toxic; transcription drop; cell-cycle shift); [[PH-797804 (drug)]] 5 µM (-1.7); [[Homoharringtonine (drug)]] 0.05 µM (-1.3); [[Clopidogrel (drug)]] 0.05 µM (-1.2); [[Gefitinib (drug)]] 5 µM (-1.2); [[Malotilate (drug)]] 5 µM (-1.1); [[(S)-Crizotinib (drug)]] 0.05 µM (-1.1); [[Malotilate (drug)]] 0.5 µM (-1.1); [[Sapanisertib (drug)]] 5 µM (-1.0); [[ERK5-IN-2 (drug)]] 5 µM (-1.0) (19 in all, 10 with an alert ⚠)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[NCI-H460 (line)]], [[PANC-1 (line)]], [[NCI-H23 (line)]], [[SW480 (line)]], [[LS 180 (line)]], [[NCI-H1573 (line)]], [[J82 (line)]], [[SK-MEL-2 (line)]]

## Candidate new members

*Members not annotated to the set their arm is enriched for, ranked by mean cos to the annotated members (`validation/novel_members.csv`); ⚠ = a reason to doubt the gene's place (in the vector space only through flagged drug-doses), kept in its rank. 1 candidates, none with an alert.*

| # | Gene | Set | Mean cos |
|---|---|---|---|
| 1 | [[DPYSL5]] | Cardiac conduction | +0.51 |

## + arm (55)

| Gene | Projection | Name |
|---|---|---|
| [[JAKMIP1]] | 0.834 | janus kinase and microtubule interacting protein 1 |
| [[MAP6]] | 0.786 | microtubule associated protein 6 |
| [[NOVA2]] | 0.781 | NOVA alternative splicing regulator 2 |
| [[LPAR3]] | 0.781 | lysophosphatidic acid receptor 3 |
| [[LMX1B]] | 0.764 | LIM homeobox transcription factor 1 beta |
| [[DPYSL5]] | 0.754 | dihydropyrimidinase like 5 |
| [[GNAO1]] | 0.752 | G protein subunit alpha o1 |
| [[RIMS3]] | 0.752 | regulating synaptic membrane exocytosis 3 |
| [[RET]] | 0.734 | ret proto-oncogene |
| [[CACNG7]] | 0.725 | calcium voltage-gated channel auxiliary subunit gamma 7 |
| [[KIF5C]] | 0.721 | kinesin family member 5C |
| [[FAM124A]] | 0.709 | family with sequence similarity 124 member A |
| [[GPRIN1]] | 0.704 | G protein regulated inducer of neurite outgrowth 1 |
| [[ADCY1]] | 0.690 | adenylate cyclase 1 |
| [[SYT11]] | 0.690 | synaptotagmin 11 |
| [[LHX6]] | 0.689 | LIM homeobox 6 |
| [[PTPRS]] | 0.688 | protein tyrosine phosphatase receptor type S |
| [[RASSF2]] | 0.687 | Ras association domain family member 2 |
| [[ESYT3]] | 0.684 | extended synaptotagmin 3 |
| [[KIF26A]] | 0.683 | kinesin family member 26A |
| [[KCNK13]] | 0.682 | potassium two pore domain channel subfamily K member 13 |
| [[STOX2]] | 0.677 | storkhead box 2 |
| [[SLC6A17]] | 0.677 | solute carrier family 6 member 17 |
| [[FSD1]] | 0.676 | fibronectin type III and SPRY domain containing 1 |
| [[TMEM108]] | 0.675 | transmembrane protein 108 |
| [[VASH1]] | 0.644 | vasohibin 1 |
| [[CRMP1]] | 0.635 | collapsin response mediator protein 1 |
| [[DNMT3B]] | 0.634 | DNA methyltransferase 3 beta |
| [[ADD2]] | 0.634 | adducin 2 |
| [[NFASC]] | 0.629 | neurofascin |
| [[KIF3C]] | 0.629 | kinesin family member 3C |
| [[BMP8B]] | 0.623 | bone morphogenetic protein 8b |
| [[TEX15]] | 0.617 | testis expressed 15, meiosis and synapsis associated |
| [[HEYL]] | 0.607 | hes related family bHLH transcription factor with YRPW motif like |
| [[ETNK2]] | 0.602 | ethanolamine kinase 2 |
| [[TMEM150C]] | 0.580 | transmembrane protein 150C |
| [[KCNS3]] | 0.578 | potassium voltage-gated channel modifier subfamily S member 3 |
| [[KIF5A]] | 0.570 | kinesin family member 5A |
| [[GPC3]] | 0.563 | glypican 3 |
| [[SLC66A1L]] | 0.555 | solute carrier family 66 member 1 like, pseudogene |
| [[ST6GALNAC3]] | 0.553 | ST6 N-acetylgalactosaminide alpha-2,6-sialyltransferase 3 |
| [[OCA2]] | 0.546 | OCA2 melanosomal transmembrane protein |
| [[GUCY1B1]] | 0.544 | guanylate cyclase 1 soluble subunit beta 1 |
| [[SCN8A]] | 0.541 | sodium voltage-gated channel alpha subunit 8 |
| [[SLC22A17]] | 0.537 | solute carrier family 22 member 17 |
| [[SOGA3]] | 0.534 | MTCL family member 3 |
| [[PAX9]] | 0.507 | paired box 9 |
| [[FXYD6]] | 0.502 | FXYD domain containing ion transport regulator 6 |
| [[PDHX]] | -0.471 | pyruvate dehydrogenase complex component X |
| [[CACNG4]] | 0.449 | calcium voltage-gated channel auxiliary subunit gamma 4 |
| [[WDR17]] | 0.407 | WD repeat domain 17 |
| [[JAZF1]] | 0.395 | JAZF zinc finger 1 |
| [[BVES]] | 0.370 | popeye domain cAMP effector 1 |
| [[DZIP1]] | 0.312 | DAZ interacting zinc finger protein 1 |
| [[LOXL1-AS1]] | 0.305 | LOXL1 antisense RNA 1 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 82; `graph/modules.parquet` — module == 82; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [81] (drug-dose × line)
