---
module: 159
type: "module"
n_genes: 27
n_plus: 27
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.42501068115234375
label: "High laminar flow shear stress activates signaling by PIEZO1 and PECAM1:CDH5:KDR in endothelial cells"
label_source: "reactome"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 159

*High laminar flow shear stress activates signaling by PIEZO1 and PECAM1:CDH5:KDR in endothelial cells · 27 genes (single-armed) · [[Module 159.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.43; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

Label from the validation stage: **High laminar flow shear stress activates signaling by PIEZO1 and PECAM1:CDH5:KDR in endothelial cells** (reactome, q 0.045; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | Cellular responses to stimuli | reactome | 10/27 | 7.20 | 3e-04 |
| + | Cellular responses to stimuli | reactome | 10/27 | 7.20 | 3e-04 |
| all | High laminar flow shear stress activates signaling by PIEZO1 and PECAM1:CDH5:KDR in endothelial cells | reactome | 3/27 | 30.5 | 0.045 |
| + | High laminar flow shear stress activates signaling by PIEZO1 and PECAM1:CDH5:KDR in endothelial cells | reactome | 3/27 | 30.5 | 0.045 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 158), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Panobinostat (drug)]] 5 µM (+11.0, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (+9.7, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (+9.4, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (+6.1, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (+5.7); [[Brivudine (drug)]] 5 µM (+4.4); [[Bortezomib (drug)]] 0.05 µM (+3.9, ⚠ cell-cycle shift); [[Ixazomib citrate (drug)]] 5 µM (+3.8, ⚠ cell-cycle shift); [[Belinostat (drug)]] 0.5 µM (+3.6, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 0.5 µM (+3.3, ⚠ cell-cycle shift); [[Ixazomib citrate (drug)]] 0.5 µM (+2.4); [[HI-TOPK-032 (drug)]] 5 µM (+1.6); [[Neratinib (maleate) (drug)]] 5 µM (+1.5); [[Bortezomib (drug)]] 0.5 µM (+1.4); [[Ponatinib (drug)]] 5 µM (+1.3); [[Pitavastatin (Calcium) (drug)]] 0.5 µM (+1.2); [[Brivudine (drug)]] 0.5 µM (+1.1) (22 in all, 13 with an alert ⚠; shown: the 10 strongest and the 7 next strongest without an alert)
- Lower it: [[Homoharringtonine (drug)]] 5 µM (-7.4, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-6.1, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-5.9, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (-4.3, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (-4.0, ⚠ cell-cycle shift); [[TAK-901 (drug)]] 5 µM (-3.9, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (-3.5, ⚠ toxic; transcription drop; cell-cycle shift); [[Auranofin (drug)]] 5 µM (-3.4); [[Ouabain (Octahydrate) (drug)]] 5 µM (-3.3, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (-3.1, ⚠ toxic; transcription drop; cell-cycle shift); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (-2.2); [[Homoharringtonine (drug)]] 0.05 µM (-1.9); [[PH-797804 (drug)]] 5 µM (-1.6); [[Sulfatinib (drug)]] 5 µM (-1.6); [[Belzutifan (drug)]] 5 µM (-1.3); [[Thymol (drug)]] 5 µM (-1.2); [[Harringtonine (drug)]] 0.05 µM (-1.2); [[Abemaciclib (drug)]] 5 µM (-1.2); [[TAK-733 (drug)]] 5 µM (-1.1) (32 in all, 21 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[PANC-1 (line)]], [[A-172 (line)]], [[NCI-H460 (line)]], [[LOX-IMVI (line)]], [[HOP62 (line)]], [[J82 (line)]], [[NCI-H1573 (line)]], [[HS-578T (line)]]

## + arm (27)

| Gene | Projection | Name |
|---|---|---|
| [[PACC1]] | 0.861 | proton activated chloride channel 1 |
| [[SERAC1]] | 0.838 | serine active site containing 1 |
| [[CRLF3]] | 0.829 | cytokine receptor like factor 3 |
| [[BLVRA]] | 0.798 | biliverdin reductase A |
| [[RALGPS1]] | 0.793 | Ral GEF with PH domain and SH3 binding motif 1 |
| [[INPP4A]] | 0.784 | inositol polyphosphate-4-phosphatase type I A |
| [[CAMK2G]] | 0.765 | calcium/calmodulin dependent protein kinase II gamma |
| [[SLC23A2]] | 0.756 | solute carrier family 23 member 2 |
| [[EPS15]] | 0.738 | epidermal growth factor receptor pathway substrate 15 |
| [[USP11]] | -0.726 | ubiquitin specific peptidase 11 |
| [[PRR5]] | 0.714 | proline rich 5 |
| [[UNC13B]] | 0.712 | unc-13 homolog B |
| [[STIMATE]] | 0.704 | STIM activating enhancer |
| [[SEMA4F]] | 0.702 | ssemaphorin 4F |
| [[UBE2Q2P2-1]] | 0.698 | — |
| [[EIF4E3]] | 0.696 | eukaryotic translation initiation factor 4E family member 3 |
| [[HDAC11]] | 0.664 | histone deacetylase 11 |
| [[RBKS]] | -0.650 | ribokinase |
| [[PIK3CB]] | 0.638 | phosphatidylinositol-4,5-bisphosphate 3-kinase catalytic subunit beta |
| [[EXTL3]] | 0.623 | exostosin like glycosyltransferase 3 |
| [[WFS1]] | 0.610 | wolframin ER transmembrane glycoprotein |
| [[YME1L1]] | -0.608 | YME1 like 1 ATPase |
| [[NIPA1]] | 0.571 | NIPA magnesium transporter 1 |
| [[MAPK8]] | 0.561 | mitogen-activated protein kinase 8 |
| [[SLC45A4]] | 0.501 | solute carrier family 45 member 4 |
| [[ADCY9]] | 0.478 | adenylate cyclase 9 |
| [[HSPA12A]] | 0.432 | heat shock protein family A (Hsp70) member 12A |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 159; `graph/modules.parquet` — module == 159; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [158] (drug-dose × line)
