---
module: 202
type: "module"
n_genes: 15
n_plus: 15
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 202

*15 genes (single-armed) · [[Module 202.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | POU5F1 (OCT4), SOX2, NANOG activate genes related to proliferation | reactome | 2/15 | 251 | 0.011 |
| + | POU5F1 (OCT4), SOX2, NANOG activate genes related to proliferation | reactome | 2/15 | 251 | 0.011 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 201), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Homoharringtonine (drug)]] 5 µM (+18.3, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (+13.1, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (+10.8, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (+7.7, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (+6.7, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (+6.7, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+6.3, ⚠ toxic; transcription drop; cell-cycle shift); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+6.3); [[Auranofin (drug)]] 5 µM (+5.7); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (+4.2, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.05 µM (+3.4); [[Tucidinostat (drug)]] 5 µM (+2.6); [[Cobimetinib (drug)]] 5 µM (+2.2); [[Vinblastine (sulfate) (drug)]] 0.5 µM (+2.1); [[Peretinoin (drug)]] 5 µM (+2.1); [[Vinblastine (sulfate) (drug)]] 5 µM (+2.0); [[Peretinoin (drug)]] 0.5 µM (+2.0); [[TAK-901 (drug)]] 0.05 µM (+1.6) (61 in all, 26 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)
- Lower it: [[Panobinostat (drug)]] 0.5 µM (-8.7, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (-7.2, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (-7.1, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (-1.9, ⚠ cell-cycle shift); [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM (-1.8); [[Artesunate (drug)]] 5 µM (-1.8, ⚠ cell-cycle shift); [[Betamethasone dipropionate (drug)]] 5 µM (-1.7); [[HI-TOPK-032 (drug)]] 5 µM (-1.7); [[Belinostat (drug)]] 0.5 µM (-1.7, ⚠ cell-cycle shift); [[Dexamethasone (drug)]] 0.5 µM (-1.6); [[Niclosamide (olamine) (drug)]] 0.5 µM (-1.6); [[Glycyrrhizic acid (drug)]] 5 µM (-1.2); [[Budesonide (drug)]] 0.05 µM (-1.2); [[Dexamethasone (drug)]] 5 µM (-1.2); [[Pravastatin (sodium) (drug)]] 5 µM (-1.2); [[Cloxacillin (sodium) (drug)]] 0.05 µM (-1.1) (22 in all, 8 with an alert ⚠; shown: the 10 strongest and the 6 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[COLO 205 (line)]], [[NCI-H460 (line)]], [[MIA PaCa-2 (line)]], [[A549 (line)]], [[A-172 (line)]], [[SNU-1 (line)]], [[A498 (line)]], [[HOP62 (line)]]

## + arm (15)

| Gene | Projection | Name |
|---|---|---|
| [[CACNA2D1]] | 0.845 | calcium voltage-gated channel auxiliary subunit alpha2delta 1 |
| [[ANKRD18B]] | 0.831 | ankyrin repeat domain 18B |
| [[TENM3-AS1]] | 0.826 | TENM3 antisense RNA 1 |
| [[TRHDE]] | 0.802 | thyrotropin releasing hormone degrading enzyme |
| [[RGS20]] | 0.795 | regulator of G protein signaling 20 |
| [[IL7R]] | 0.773 | interleukin 7 receptor |
| [[FGF2]] | 0.763 | fibroblast growth factor 2 |
| [[BMPR1B]] | 0.749 | bone morphogenetic protein receptor type 1B |
| [[PGM5P2-1]] | 0.687 | — |
| [[LINC01116]] | 0.675 | long independently transcribed non-coding RNA 1116 |
| [[NR2F1-AS1]] | 0.674 | NR2F1 regulatory antisense RNA 1 |
| [[SAMD4A]] | 0.604 | sterile alpha motif domain containing 4A |
| [[SALL1]] | 0.591 | spalt like transcription factor 1 |
| [[CAMSAP2]] | 0.574 | calmodulin regulated spectrin associated protein family member 2 |
| [[PGM5P2]] | 0.427 | phosphoglucomutase 5 pseudogene 2 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 202; `graph/modules.parquet` — module == 202; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [201] (drug-dose × line)
