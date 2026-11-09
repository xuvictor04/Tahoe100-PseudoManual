---
module: 209
type: "module"
n_genes: 13
n_plus: 13
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 209

*13 genes (single-armed) · [[Module 209.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 208), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Panobinostat (drug)]] 5 µM (+12.5, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (+11.5, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (+9.6, ⚠ cell-cycle shift); [[Topotecan (hydrochloride) (drug)]] 5 µM (+4.8, ⚠ toxic; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (+4.4, ⚠ toxic; transcription drop; cell-cycle shift); [[Homoharringtonine (drug)]] 5 µM (+4.0, ⚠ cell-cycle shift); [[Ponatinib (drug)]] 5 µM (+2.9); [[Selinexor (drug)]] 5 µM (+2.8, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (+2.8, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+2.8, ⚠ toxic; transcription drop; cell-cycle shift); [[Brivudine (drug)]] 5 µM (+2.7); [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM (+2.0); [[Ponatinib (drug)]] 0.5 µM (+1.8); [[Trametinib (drug)]] 0.05 µM (+1.8); [[Amsacrine (drug)]] 5 µM (+1.8); [[Cabozantinib (S-malate) (drug)]] 5 µM (+1.7); [[Homoharringtonine (drug)]] 0.05 µM (+1.6); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM (+1.4); [[Binimetinib (drug)]] 0.05 µM (+1.4) (38 in all, 21 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)
- Lower it: [[Niclosamide (olamine) (drug)]] 5 µM (-3.8, ⚠ toxic; cell-cycle shift); [[c-Kit-IN-1 (drug)]] 0.05 µM (-2.0, ⚠ unreliable plate only); [[Ixazomib citrate (drug)]] 5 µM (-1.7, ⚠ cell-cycle shift); [[Ixazomib citrate (drug)]] 0.5 µM (-1.6); [[PH-797804 (drug)]] 5 µM (-1.6); [[PF-06260933 (drug)]] 5 µM (-1.6); [[Peretinoin (drug)]] 5 µM (-1.5); [[Abemaciclib (drug)]] 5 µM (-1.5); [[Gefitinib (drug)]] 5 µM (-1.4); [[Cyclosporin A (drug)]] 0.05 µM (-1.4); [[Auranofin (drug)]] 5 µM (-1.3); [[Mebendazole (drug)]] 5 µM (-1.3); [[Clopidogrel (drug)]] 0.05 µM (-1.2) (28 in all, 9 with an alert ⚠; shown: the 10 strongest and the 3 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[SW480 (line)]], [[A498 (line)]], [[LS 180 (line)]], [[PANC-1 (line)]], [[HEC-1-A (line)]], [[NCI-H460 (line)]], [[LoVo (line)]], [[KATO III (line)]]

## + arm (13)

| Gene | Projection | Name |
|---|---|---|
| [[TBC1D13]] | 0.823 | TBC1 domain family member 13 |
| [[VPS16]] | 0.774 | VPS16 core subunit of CORVET and HOPS complexes |
| [[STEEP1]] | 0.749 | STING1 ER exit protein 1 |
| [[NISCH]] | 0.729 | nischarin |
| [[CROCCP2]] | 0.721 | CROCC pseudogene 2 |
| [[TMEM175]] | 0.713 | transmembrane protein 175 |
| [[PXMP4]] | 0.704 | peroxisomal membrane protein 4 |
| [[C6orf89]] | 0.696 | chromosome 6 open reading frame 89 |
| [[ZNF594-DT]] | 0.674 | ZNF594 divergent transcript |
| [[COMMD9]] | 0.511 | COMM domain containing 9 |
| [[BSN]] | 0.321 | bassoon presynaptic cytomatrix protein |
| [[PPP3CB]] | 0.181 | protein phosphatase 3 catalytic subunit beta |
| [[PHF20L1]] | 0.0797 | PHD finger protein 20 like 1 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 209; `graph/modules.parquet` — module == 209; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [208] (drug-dose × line)
