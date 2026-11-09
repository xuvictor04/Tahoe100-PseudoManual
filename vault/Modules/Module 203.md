---
module: 203
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

# Module 203

*15 genes (single-armed) · [[Module 203.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 202), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Topotecan (hydrochloride) (drug)]] 5 µM (+5.2, ⚠ toxic; cell-cycle shift); [[Selinexor (drug)]] 5 µM (+4.9, ⚠ cell-cycle shift); [[Topotecan (hydrochloride) (drug)]] 0.5 µM (+3.1, ⚠ cell-cycle shift); [[Ixazomib citrate (drug)]] 5 µM (+2.8, ⚠ cell-cycle shift); [[Bortezomib (drug)]] 0.05 µM (+2.8, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (+2.7, ⚠ cell-cycle shift); [[Selinexor (drug)]] 0.5 µM (+2.4, ⚠ cell-cycle shift); [[Selinexor (drug)]] 0.05 µM (+2.1, ⚠ cell-cycle shift); [[Ixazomib citrate (drug)]] 0.5 µM (+2.1); [[5-Azacytidine (drug)]] 5 µM (+2.0); [[Peretinoin (drug)]] 5 µM (+1.7); [[Cabozantinib (S-malate) (drug)]] 0.05 µM (+1.6); [[Osimertinib (mesylate) (drug)]] 5 µM (+1.6); [[Rapamycin (drug)]] 5 µM (+1.6); [[Auranofin (drug)]] 5 µM (+1.5); [[Belzutifan (drug)]] 5 µM (+1.5); [[Vitamin K4 (drug)]] 0.05 µM (+1.5); [[Ipatasertib (drug)]] 0.5 µM (+1.5) (51 in all, 15 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)
- Lower it: [[Dinaciclib (drug)]] 0.5 µM (-5.4, ⚠ toxic; transcription drop; cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (-4.7, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (-4.6, ⚠ toxic; transcription drop; cell-cycle shift); [[Niclosamide (olamine) (drug)]] 5 µM (-4.3, ⚠ toxic; cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (-4.1, ⚠ toxic; transcription drop; cell-cycle shift); [[Digitoxin (drug)]] 0.5 µM (-3.7, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 5 µM (-3.5, ⚠ toxic; transcription drop; cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 0.05 µM (-2.3, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (-2.3, ⚠ cell-cycle shift); [[TAK-901 (drug)]] 5 µM (-2.2, ⚠ cell-cycle shift); [[Gefitinib (drug)]] 5 µM (-1.5); [[Clopidogrel (drug)]] 0.05 µM (-1.4); [[Anethole trithione (drug)]] 0.5 µM (-1.4); [[ERK5-IN-2 (drug)]] 0.05 µM (-1.4); [[Dimethyl fumarate (drug)]] 5 µM (-1.2); [[PH-797804 (drug)]] 5 µM (-1.2); [[Flumatinib (mesylate) (drug)]] 0.5 µM (-1.2); [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM (-1.2); [[Dihydroartemisinin (drug)]] 5 µM (-1.1); [[Pyridoxine (hydrochloride) (drug)]] 5 µM (-1.1) (30 in all, 16 with an alert ⚠; shown: the 10 strongest and the 10 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[PANC-1 (line)]], [[MIA PaCa-2 (line)]], [[NCI-H23 (line)]], [[A-172 (line)]], [[NCI-H460 (line)]], [[SNU-423 (line)]], [[SW480 (line)]], [[SHP-77 (line)]]

## + arm (15)

| Gene | Projection | Name |
|---|---|---|
| [[ZNF600]] | 0.876 | zinc finger protein 600 |
| [[ZNF611]] | 0.850 | zinc finger protein 611 |
| [[ZNF430]] | 0.757 | zinc finger protein 430 |
| [[ZNF431]] | 0.748 | zinc finger protein 431 |
| [[ZNF765]] | 0.745 | zinc finger protein 765 |
| [[ZNF28]] | 0.729 | zinc finger protein 28 |
| [[ZNF761]] | 0.694 | zinc finger protein 761 |
| [[PAQR7]] | 0.649 | progestin and adipoQ receptor family member 7 |
| [[UBE2Q2P1-1]] | 0.644 | — |
| [[SREK1IP1]] | 0.637 | SREK1 interacting protein 1 |
| [[FAAP24]] | 0.610 | FA core complex associated protein 24 |
| [[PLEKHO1]] | 0.577 | pleckstrin homology domain containing O1 |
| [[ZNF337]] | 0.568 | zinc finger protein 337 |
| [[LRFN4]] | 0.546 | leucine rich repeat and fibronectin type III domain containing 4 |
| [[NINL]] | 0.529 | ninein like |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 203; `graph/modules.parquet` — module == 203; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [202] (drug-dose × line)
