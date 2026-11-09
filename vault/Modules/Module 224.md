---
module: 224
type: "module"
n_genes: 9
n_plus: 9
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: "hypoxia"
label_source: "hallmark"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 224

*hypoxia · 9 genes (single-armed) · [[Module 224.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

Label from the validation stage: **hypoxia** (hallmark, q 0.048; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | hypoxia | hallmark | 3/9 | 27.6 | 0.048 |
| + | hypoxia | hallmark | 3/9 | 27.6 | 0.048 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 223), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Homoharringtonine (drug)]] 5 µM (+12.5, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (+8.3, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (+8.1); [[Harringtonine (drug)]] 5 µM (+7.3, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (+6.4, ⚠ cell-cycle shift); [[TAK-901 (drug)]] 5 µM (+6.0, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (+5.8, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (+5.5, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (+4.9, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (+4.3, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.05 µM (+3.3); [[Peretinoin (drug)]] 5 µM (+3.0); [[PH-797804 (drug)]] 5 µM (+2.9); [[Binimetinib (drug)]] 5 µM (+2.2); [[Harringtonine (drug)]] 0.05 µM (+2.2); [[Brivudine (drug)]] 5 µM (+2.0); [[Vinblastine (sulfate) (drug)]] 0.5 µM (+1.9); [[Peretinoin (drug)]] 0.5 µM (+1.9); [[Vinblastine (sulfate) (drug)]] 5 µM (+1.8) (58 in all, 23 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)
- Lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM (-5.4, ⚠ cell-cycle shift); [[Dexamethasone (drug)]] 5 µM (-3.1); [[Clobetasol propionate (drug)]] 0.05 µM (-3.1); [[Triamcinolone (drug)]] 5 µM (-3.0); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (-2.9, ⚠ cell-cycle shift); [[Clobetasol propionate (drug)]] 0.5 µM (-2.9); [[Budesonide (drug)]] 5 µM (-2.7); [[Triamcinolone (drug)]] 0.5 µM (-2.5); [[Betamethasone dipropionate (drug)]] 0.5 µM (-2.4); [[Clobetasol propionate (drug)]] 5 µM (-2.4); [[Dexamethasone (drug)]] 0.5 µM (-2.4); [[GSK1059615 (drug)]] 5 µM (-2.3) (46 in all, 11 with an alert ⚠; shown: the 10 strongest and the 2 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[MIA PaCa-2 (line)]], [[A-427 (line)]], [[SW1417 (line)]], [[NCI-H460 (line)]], [[A549 (line)]], [[A-172 (line)]], [[Panc 03.27 (line)]], [[HEC-1-A (line)]]

## + arm (9)

| Gene | Projection | Name |
|---|---|---|
| [[SYTL2]] | 0.827 | synaptotagmin like 2 |
| [[LIMA1]] | 0.821 | LIM domain and actin binding 1 |
| [[PLK2]] | 0.772 | polo like kinase 2 |
| [[EXT1]] | 0.752 | exostosin glycosyltransferase 1 |
| [[DUSP14]] | 0.739 | dual specificity phosphatase 14 |
| [[CPA4]] | 0.682 | carboxypeptidase A4 |
| [[NOCT]] | 0.673 | nocturnin |
| [[FHL2]] | 0.670 | four and a half LIM domains 2 |
| [[CAVIN1]] | 0.582 | caveolae associated protein 1 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 224; `graph/modules.parquet` — module == 224; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [223] (drug-dose × line)
