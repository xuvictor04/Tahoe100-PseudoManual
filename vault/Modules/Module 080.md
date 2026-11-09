---
module: 80
type: "module"
n_genes: 57
n_plus: 57
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.36472180485725403
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 080

*57 genes (single-armed) · [[Module 080.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 79), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM (+17.6, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 5 µM (+13.5, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (+6.6, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (+6.5, ⚠ toxic; transcription drop; cell-cycle shift); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (+6.4, ⚠ cell-cycle shift); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+6.3); [[Dinaciclib (drug)]] 0.05 µM (+5.9, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (+5.9, ⚠ toxic; transcription drop; cell-cycle shift); [[Harringtonine (drug)]] 5 µM (+5.6, ⚠ cell-cycle shift); [[Epirubicin (hydrochloride) (drug)]] 5 µM (+5.6, ⚠ cell-cycle shift); [[Auranofin (drug)]] 5 µM (+3.6); [[Tucidinostat (drug)]] 5 µM (+2.1); [[Filgotinib (drug)]] 5 µM (+2.1); [[Homoharringtonine (drug)]] 0.05 µM (+1.8); [[Amsacrine (drug)]] 5 µM (+1.5); [[Belzutifan (drug)]] 5 µM (+1.5); [[Harringtonine (drug)]] 0.05 µM (+1.4); [[Ponatinib (drug)]] 0.5 µM (+1.2); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM (+1.2) (49 in all, 21 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)
- Lower it: [[Belinostat (drug)]] 5 µM (-3.8, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 0.5 µM (-3.3, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (-3.3, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (-3.1, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (-3.1, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 5 µM (-2.4, ⚠ toxic; transcription drop; cell-cycle shift); [[Ixazomib citrate (drug)]] 5 µM (-2.2, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (-2.1, ⚠ cell-cycle shift); [[c-Kit-IN-1 (drug)]] 0.05 µM (-1.9, ⚠ unreliable plate only); [[Ixazomib citrate (drug)]] 0.5 µM (-1.8); [[Niclosamide (olamine) (drug)]] 0.5 µM (-1.8); [[PH-797804 (drug)]] 5 µM (-1.6); [[Dexamethasone (drug)]] 0.5 µM (-1.5); [[Dimethyl fumarate (drug)]] 5 µM (-1.4); [[Abemaciclib (drug)]] 0.5 µM (-1.4); [[Dexamethasone (drug)]] 5 µM (-1.3); [[Brivudine (drug)]] 5 µM (-1.2); [[Pravastatin (sodium) (drug)]] 5 µM (-1.2); [[Tomivosertib (drug)]] 5 µM (-1.2) (32 in all, 14 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[A-172 (line)]], [[HOP62 (line)]], [[NCI-H460 (line)]], [[HS-578T (line)]], [[A498 (line)]], [[C-33 A (line)]], [[LoVo (line)]], [[NCI-H2347 (line)]]

## + arm (57)

| Gene | Projection | Name |
|---|---|---|
| [[ZNF341-AS1]] | 0.896 | ZNF341 antisense RNA 1 |
| [[LPXN]] | 0.870 | leupaxin |
| [[NEK8]] | 0.860 | NIMA related kinase 8 |
| [[WAKMAR2]] | 0.854 | wound and keratinocyte migration associated lncRNA 2 |
| [[MZF1-AS1]] | 0.848 | MZF1 antisense RNA 1 |
| [[ENO3]] | 0.824 | enolase 3 |
| [[LETM2]] | 0.808 | leucine zipper and EF-hand containing transmembrane protein 2 |
| [[ANGPT2]] | 0.799 | angiopoietin 2 |
| [[NANOS3]] | 0.798 | nanos C2HC-type zinc finger 3 |
| [[HIVEP2-DT]] | 0.791 | HIVEP2 divergent transcript |
| [[BCL10-AS1]] | 0.788 | BCL10 antisense RNA 1 |
| [[GPR137]] | 0.784 | G protein-coupled receptor 137 |
| [[MMRN2]] | 0.783 | multimerin 2 |
| [[CDK6-AS1]] | 0.778 | CDK6 antisense RNA 1 |
| [[PIGV]] | 0.762 | phosphatidylinositol glycan anchor biosynthesis class V |
| [[BOLA1]] | 0.758 | bolA family member 1 |
| [[SSPN]] | 0.753 | sarcospan |
| [[LINC01829]] | 0.735 | long independently transcribed non-coding RNA 1829 |
| [[DENND5B-AS1]] | 0.733 | DENND5B antisense RNA 1 |
| [[LINC02068]] | 0.733 | long independently transcribed non-coding RNA 2068 |
| [[CFLAR-AS1]] | 0.731 | CFLAR antisense RNA 1 |
| [[SPHK1]] | 0.727 | sphingosine kinase 1 |
| [[GCNT4]] | 0.725 | glucosaminyl (N-acetyl) transferase 4 |
| [[SIX5]] | 0.710 | SIX homeobox 5 |
| [[LINC00705]] | 0.707 | long independently transcribed non-coding RNA 705 |
| [[PPP1R1C]] | 0.703 | protein phosphatase 1 regulatory inhibitor subunit 1C |
| [[DPY19L2P2]] | 0.699 | DPY19L2 pseudogene 2 |
| [[CABYR]] | 0.696 | calcium binding tyrosine phosphorylation regulated |
| [[ZHX2]] | 0.692 | zinc fingers and homeoboxes 2 |
| [[C2orf92]] | 0.689 | chromosome 2 open reading frame 92 |
| [[BHLHE40-AS1]] | 0.670 | BHLHE40 antisense RNA 1 |
| [[IPO9-AS1]] | 0.667 | IPO9 antisense RNA 1 |
| [[GASAL1]] | 0.662 | growth arrest associated lncRNA 1 |
| [[SERPINB9P1]] | 0.662 | serpin family B member 9 pseudogene 1 |
| [[FBXO48]] | 0.657 | F-box protein 48 |
| [[PLEKHA8P1]] | 0.641 | pleckstrin homology domain containing A8 pseudogene 1 |
| [[CUBN]] | 0.640 | cubilin |
| [[LPAR6]] | 0.637 | lysophosphatidic acid receptor 6 |
| [[ZNF641]] | 0.637 | zinc finger protein 641 |
| [[FRMD6-AS2]] | 0.628 | FRMD6 antisense RNA 2 |
| [[SPATA6]] | -0.618 | spermatogenesis associated 6 |
| [[BFSP1]] | 0.617 | beaded filament structural protein 1 |
| [[LINC01186]] | 0.600 | long independently transcribed non-coding RNA 1186 |
| [[DNASE1]] | 0.599 | deoxyribonuclease 1 |
| [[IRF3]] | 0.587 | interferon regulatory factor 3 |
| [[RASSF8-AS1]] | 0.581 | RASSF8 antisense RNA 1 |
| [[ALDH1A2]] | 0.578 | aldehyde dehydrogenase 1 family member A2 |
| [[TMEM242]] | -0.560 | transmembrane protein 242 |
| [[COL27A1]] | 0.556 | collagen type XXVII alpha 1 chain |
| [[ANK1]] | 0.548 | ankyrin 1 |
| [[OXTR]] | 0.541 | oxytocin receptor |
| [[LHPP]] | -0.537 | phospholysine phosphohistidine inorganic pyrophosphate phosphatase |
| [[JAM2]] | 0.528 | junctional adhesion molecule 2 |
| [[MOB3C]] | 0.509 | MOB kinase activator 3C |
| [[LRRC28]] | -0.500 | leucine rich repeat containing 28 |
| [[LINC00857]] | 0.481 | long independently transcribed non-coding RNA 857 |
| [[SLC27A3]] | 0.360 | solute carrier family 27 member 3 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 80; `graph/modules.parquet` — module == 80; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [79] (drug-dose × line)
