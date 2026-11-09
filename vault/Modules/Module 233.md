---
module: 233
type: "module"
n_genes: 6
n_plus: 6
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.3518480360507965
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 233

*6 genes (single-armed) · [[Module 233.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 232), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Homoharringtonine (drug)]] 5 µM (+8.8, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (+8.6, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 5 µM (+6.7, ⚠ toxic; transcription drop; cell-cycle shift); [[Digitoxin (drug)]] 0.5 µM (+5.3, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (+5.1, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (+5.1, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (+4.3, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (+4.2, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (+3.6, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (+3.6, ⚠ cell-cycle shift); [[Vinblastine (sulfate) (drug)]] 5 µM (+2.8); [[PF-06260933 (drug)]] 5 µM (+2.4); [[Tomivosertib (drug)]] 5 µM (+2.2); [[Niclosamide (olamine) (drug)]] 0.5 µM (+1.9); [[Vinblastine (sulfate) (drug)]] 0.5 µM (+1.9); [[Artesunate (drug)]] 0.5 µM (+1.7); [[Brivudine (drug)]] 5 µM (+1.7); [[HI-TOPK-032 (drug)]] 5 µM (+1.6); [[Neratinib (maleate) (drug)]] 5 µM (+1.6); [[Dimethyl fumarate (drug)]] 5 µM (+1.5) (61 in all, 27 with an alert ⚠; shown: the 10 strongest and the 10 next strongest without an alert)
- Lower it: [[Auranofin (drug)]] 5 µM (-2.4); [[Darinaparsin (drug)]] 5 µM (-2.1, ⚠ cell-cycle shift); [[Filgotinib (drug)]] 5 µM (-2.0); [[Larotrectinib (drug)]] 5 µM (-1.9); [[Diphenhydramine (drug)]] 0.5 µM (-1.9); [[Ponatinib (drug)]] 0.5 µM (-1.9); [[Docetaxel (drug)]] 0.05 µM (-1.8, ⚠ transcription drop; cell-cycle shift); [[Belzutifan (drug)]] 5 µM (-1.7); [[Esmolol (hydrochloride) (drug)]] 5 µM (-1.6); [[Temsirolimus (drug)]] 0.05 µM (-1.6); [[Ponatinib (drug)]] 5 µM (-1.6); [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM (-1.5) (60 in all, 7 with an alert ⚠; shown: the 10 strongest and the 2 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[KATO III (line)]], [[PANC-1 (line)]], [[SW1417 (line)]], [[SW480 (line)]], [[NCI-H1792 (line)]], [[HepG2_C3A (line)]], [[BT-474 (line)]], [[NCI-H2347 (line)]]

## + arm (6)

| Gene | Projection | Name |
|---|---|---|
| [[TRIM36]] | 0.862 | tripartite motif containing 36 |
| [[ATP11B]] | 0.785 | ATPase phospholipid transporting 11B (putative) |
| [[TGFBR1]] | 0.762 | transforming growth factor beta receptor 1 |
| [[KCTD9]] | 0.694 | potassium channel tetramerization domain containing 9 |
| [[ERGIC2]] | -0.644 | ERGIC and golgi 2 |
| [[FAM241A]] | 0.481 | family with sequence similarity 241 member A |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 233; `graph/modules.parquet` — module == 233; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [232] (drug-dose × line)
