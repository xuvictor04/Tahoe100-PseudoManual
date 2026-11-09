---
module: 133
type: "module"
n_genes: 36
n_plus: 36
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 133

*36 genes (single-armed) · [[Module 133.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 132), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Auranofin (drug)]] 5 µM (+7.1); [[Idarubicin (hydrochloride) (drug)]] 5 µM (+6.6, ⚠ cell-cycle shift); [[Artesunate (drug)]] 5 µM (+6.0, ⚠ cell-cycle shift); [[Neratinib (maleate) (drug)]] 0.5 µM (+5.4, ⚠ cell-cycle shift); [[5-Azacytidine (drug)]] 5 µM (+5.3); [[Ponatinib (drug)]] 5 µM (+5.2); [[c-Kit-IN-1 (drug)]] 0.05 µM (+4.9, ⚠ unreliable plate only); [[Neratinib (maleate) (drug)]] 5 µM (+4.7); [[Neratinib (drug)]] 5 µM (+3.7); [[Dinaciclib (drug)]] 0.5 µM (+3.7, ⚠ toxic; transcription drop; cell-cycle shift); [[Artesunate (drug)]] 0.5 µM (+3.7); [[Dihydroartemisinin (drug)]] 5 µM (+3.5); [[Chlorhexidine (diacetate) (drug)]] 5 µM (+3.5); [[venetoclax (drug)]] 5 µM (+2.8); [[Dihydroartemisinin (drug)]] 0.5 µM (+2.6) (71 in all, 19 with an alert ⚠; shown: the 10 strongest and the 5 next strongest without an alert)
- Lower it: [[Panobinostat (drug)]] 5 µM (-6.9, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (-6.4, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (-6.3, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-3.3, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (-3.1, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (-3.0, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 0.05 µM (-2.8); [[Digitoxin (drug)]] 0.5 µM (-2.8, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 5 µM (-2.6, ⚠ toxic; transcription drop; cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (-2.6, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.05 µM (-1.9); [[PH-797804 (drug)]] 5 µM (-1.5); [[Diammonium Glycyrrhizinate (drug)]] 5 µM (-1.3); [[Brivudine (drug)]] 5 µM (-1.2); [[Methotrexate (drug)]] 5 µM (-1.2); [[HI-TOPK-032 (drug)]] 5 µM (-1.1); [[Pyridoxine (hydrochloride) (drug)]] 5 µM (-1.1); [[BAY1125976 (drug)]] 5 µM (-1.1); [[8-Hydroxyquinoline (drug)]] 5 µM (-1.1) (27 in all, 15 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[LoVo (line)]], [[SW480 (line)]], [[NCI-H460 (line)]], [[HT-29 (line)]], [[KATO III (line)]], [[PANC-1 (line)]], [[LS 180 (line)]], [[MIA PaCa-2 (line)]]

## + arm (36)

| Gene | Projection | Name |
|---|---|---|
| [[PCK2]] | 0.881 | phosphoenolpyruvate carboxykinase 2, mitochondrial |
| [[SLC6A9]] | 0.868 | solute carrier family 6 member 9 |
| [[CEBPG]] | 0.864 | CCAAT enhancer binding protein gamma |
| [[DMGDH]] | 0.860 | dimethylglycine dehydrogenase |
| [[YARS1]] | 0.859 | tyrosyl-tRNA synthetase 1 |
| [[NBR2]] | 0.830 | neighbor of BRCA1 lncRNA 2 |
| [[MOCOS]] | 0.809 | molybdenum cofactor sulfurase |
| [[NIBAN1]] | 0.793 | niban apoptosis regulator 1 |
| [[TMEM268]] | 0.789 | transmembrane protein 268 |
| [[VLDLR-AS1]] | 0.787 | VLDLR antisense RNA 1 |
| [[SLC3A2]] | 0.784 | solute carrier family 3 member 2 |
| [[MIA2]] | 0.728 | MIA SH3 domain ER export factor 2 |
| [[BLTP3A]] | 0.715 | bridge-like lipid transfer protein family member 3A |
| [[HOXB9]] | 0.695 | homeobox B9 |
| [[NRSN2-AS1]] | 0.694 | NRSN2 antisense RNA 1 |
| [[ZBED3]] | 0.684 | zinc finger BED-type containing 3 |
| [[LURAP1L-AS1]] | 0.671 | LURAP1L antisense RNA 1 |
| [[LMO4]] | 0.665 | LIM domain only 4 |
| [[LURAP1L]] | 0.662 | leucine rich adaptor protein 1 like |
| [[FAM27C]] | 0.659 | family with sequence similarity 27 member C |
| [[KCTD15]] | 0.652 | potassium channel tetramerization domain containing 15 |
| [[WARS1]] | 0.631 | tryptophanyl-tRNA synthetase 1 |
| [[COP1-DT]] | 0.627 | COP1 divergent transcript |
| [[TIMM44]] | 0.622 | translocase of inner mitochondrial membrane 44 |
| [[MAPK6]] | 0.605 | mitogen-activated protein kinase 6 |
| [[SLC38A1]] | 0.604 | solute carrier family 38 member 1 |
| [[MTO1]] | 0.604 | mitochondrial tRNA translation optimization 1 |
| [[GHITM]] | 0.590 | growth hormone inducible transmembrane protein |
| [[NFE2L1]] | 0.588 | NFE2 like bZIP transcription factor 1 |
| [[TTTY14]] | 0.588 | testis expressed transcript, Y-linked 14 |
| [[PRDM16]] | 0.573 | PR/SET domain 16 |
| [[TLCD2]] | 0.536 | TLC domain containing 2 |
| [[MID1IP1]] | 0.509 | MID1 interacting protein 1 |
| [[ANKFN1]] | 0.487 | ankyrin repeat and fibronectin type III domain containing 1 |
| [[CLIP4]] | 0.458 | CAP-Gly domain containing linker protein family member 4 |
| [[MFAP3L]] | 0.447 | microfibril associated protein 3 like |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 133; `graph/modules.parquet` — module == 133; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [132] (drug-dose × line)
