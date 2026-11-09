---
module: 81
type: "module"
n_genes: 55
n_plus: 55
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.2855745255947113
label: "KRAS signaling up"
label_source: "hallmark"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 081

*KRAS signaling up · 55 genes (single-armed) · [[Module 081.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

Label from the validation stage: **KRAS signaling up** (hallmark, q 0.001; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | KRAS signaling up | hallmark | 7/55 | 11.6 | 0.001 |
| + | KRAS signaling up | hallmark | 7/55 | 11.6 | 0.001 |
| all | epithelial mesenchymal transition | hallmark | 6/55 | 8.99 | 0.021 |
| + | epithelial mesenchymal transition | hallmark | 6/55 | 8.99 | 0.021 |
| all | Uptake and actions of bacterial toxins | reactome | 3/55 | 35.8 | 0.029 |
| + | Uptake and actions of bacterial toxins | reactome | 3/55 | 35.8 | 0.029 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 80), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Tucidinostat (drug)]] 5 µM (+4.8); [[Tucidinostat (drug)]] 0.5 µM (+3.2, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (+1.7, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (+1.5, ⚠ toxic; transcription drop; cell-cycle shift); [[PF-06260933 (drug)]] 5 µM (+1.4); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+1.4); [[Daptomycin (drug)]] 5 µM (+1.4, ⚠ unreliable plate only); [[Vilanterol (drug)]] 0.5 µM (+1.4); [[Panobinostat (drug)]] 0.05 µM (+1.3, ⚠ cell-cycle shift); [[9-ING-41 (drug)]] 0.5 µM (+1.3); [[Peretinoin (drug)]] 5 µM (+1.2); [[Pitavastatin (Calcium) (drug)]] 0.5 µM (+1.1); [[Vilanterol (drug)]] 5 µM (+1.0) (15 in all, 7 with an alert ⚠; shown: the 10 strongest and the 3 next strongest without an alert)
- Lower it: [[Trametinib (drug)]] 5 µM (-4.0, ⚠ cell-cycle shift); [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM (-3.7); [[Ponatinib (drug)]] 5 µM (-3.4); [[Trametinib (drug)]] 0.5 µM (-3.4); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM (-3.3); [[Trametinib (drug)]] 0.05 µM (-3.1); [[Cobimetinib (drug)]] 5 µM (-3.1); [[Binimetinib (drug)]] 0.5 µM (-3.1); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM (-2.9); [[Clobetasol propionate (drug)]] 5 µM (-2.8); [[Triamcinolone (drug)]] 0.5 µM (-2.8) (60 in all, 9 with an alert ⚠; shown: the 10 strongest and the 1 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[BT-474 (line)]], [[NCI-H23 (line)]], [[RKO (line)]], [[NCI-H1573 (line)]], [[NCI-H460 (line)]], [[AsPC-1 (line)]], [[Hs 766T (line)]], [[SK-MEL-2 (line)]]

## Candidate new members

*Members not annotated to the set their arm is enriched for, ranked by mean cos to the annotated members (`validation/novel_members.csv`); ⚠ = a reason to doubt the gene's place (in the vector space only through flagged drug-doses), kept in its rank. 12 candidates, none with an alert.*

| # | Gene | Set | Mean cos |
|---|---|---|---|
| 1 | [[ANTXR2]] | KRAS signaling up | +0.64 |
| 2 | [[PTHLH]] | KRAS signaling up | +0.59 |
| 3 | [[MMP1]] | KRAS signaling up | +0.57 |
| 4 | [[PRDM8]] | KRAS signaling up | +0.57 |
| 5 | [[AADAC]] | KRAS signaling up | +0.56 |
| 6 | [[AADACP1]] | KRAS signaling up | +0.56 |
| 7 | [[PKIA]] | KRAS signaling up | +0.55 |
| 8 | [[STC1]] | KRAS signaling up | +0.53 |
| 9 | [[FAM107B]] | KRAS signaling up | +0.52 |
| 10 | [[BCL2A1]] | KRAS signaling up | +0.52 |
| 11 | [[TFPI2]] | KRAS signaling up | +0.51 |
| 12 | [[NGRN]] | KRAS signaling up | +0.51 |

## + arm (55)

| Gene | Projection | Name |
|---|---|---|
| [[ITGA2]] | 0.837 | integrin subunit alpha 2 |
| [[MMP1]] | 0.828 | matrix metallopeptidase 1 |
| [[ANTXR2]] | 0.821 | ANTXR cell adhesion molecule 2 |
| [[STC1]] | 0.812 | stanniocalcin 1 |
| [[PKIA]] | 0.807 | cAMP-dependent protein kinase inhibitor alpha |
| [[HBEGF]] | 0.806 | heparin binding EGF like growth factor |
| [[TMEM158]] | 0.800 | transmembrane protein 158 |
| [[BCL2A1]] | 0.785 | BCL2 related protein A1 |
| [[FAM107B]] | 0.773 | family with sequence similarity 107 member B |
| [[AADACP1]] | 0.772 | arylacetamide deacetylase pseudogene 1 |
| [[TIMP1]] | 0.745 | TIMP metallopeptidase inhibitor 1 |
| [[PTHLH]] | 0.734 | parathyroid hormone like hormone |
| [[AADAC]] | 0.732 | arylacetamide deacetylase |
| [[TFPI2]] | 0.723 | tissue factor pathway inhibitor 2 |
| [[IL1B]] | 0.720 | interleukin 1 beta |
| [[DPF3]] | 0.714 | double PHD fingers 3 |
| [[C3orf52]] | 0.711 | chromosome 3 open reading frame 52 |
| [[SHB]] | 0.709 | SH2 domain containing adaptor protein B |
| [[TM4SF1]] | 0.708 | transmembrane 4 L six family member 1 |
| [[PRDM8]] | 0.707 | PR/SET domain 8 |
| [[MARCHF3]] | 0.694 | membrane associated ring-CH-type finger 3 |
| [[NRIP3]] | 0.688 | nuclear receptor interacting protein 3 |
| [[SLC25A51]] | 0.687 | solute carrier family 25 member 51 |
| [[MAST4]] | 0.680 | microtubule associated serine/threonine kinase family member 4 |
| [[SMTN]] | 0.660 | smoothelin |
| [[SH2D2A]] | 0.648 | SH2 domain containing 2A |
| [[CALM1]] | 0.641 | calmodulin 1 |
| [[TMEM132A]] | 0.640 | transmembrane protein 132A |
| [[ANXA10]] | 0.630 | annexin A10 |
| [[IL33]] | 0.629 | interleukin 33 |
| [[TPBG]] | 0.627 | trophoblast glycoprotein |
| [[NGRN]] | 0.622 | neugrin, neurite outgrowth associated |
| [[STK17A]] | 0.621 | serine/threonine kinase 17a |
| [[CCNYL1]] | 0.620 | cyclin Y like 1 |
| [[SLC46A3]] | 0.620 | solute carrier family 46 member 3 |
| [[SPSB1]] | 0.603 | splA/ryanodine receptor domain and SOCS box containing 1 |
| [[GRB10]] | 0.573 | growth factor receptor bound protein 10 |
| [[ERN1]] | 0.573 | endoplasmic reticulum to nucleus signaling 1 |
| [[SEMA3A]] | 0.566 | semaphorin 3A |
| [[ACVR1]] | 0.561 | activin A receptor type 1 |
| [[CA2]] | 0.555 | carbonic anhydrase 2 |
| [[GCKR]] | 0.554 | glucokinase regulator |
| [[IL13RA2]] | 0.543 | interleukin 13 receptor subunit alpha 2 |
| [[RAI14]] | 0.537 | retinoic acid induced 14 |
| [[ALDH3B1]] | -0.512 | aldehyde dehydrogenase 3 family member B1 |
| [[FST]] | 0.506 | follistatin |
| [[CREG2]] | 0.495 | cellular repressor of E1A stimulated genes 2 |
| [[CD68]] | 0.489 | CD68 molecule |
| [[CTSL]] | 0.487 | cathepsin L |
| [[CPA6]] | 0.471 | carboxypeptidase A6 |
| [[SERPINE2]] | 0.462 | serpin family E member 2 |
| [[MIRLET7BHG]] | -0.449 | MIRLET7B and MIRLET7A3 host gene |
| [[MYOF]] | -0.432 | myoferlin |
| [[ATP2B1]] | 0.369 | ATPase plasma membrane Ca2+ transporting 1 |
| [[SLC22A23]] | 0.336 | solute carrier family 22 member 23 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 81; `graph/modules.parquet` — module == 81; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [80] (drug-dose × line)
