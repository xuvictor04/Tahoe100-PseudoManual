---
module: 220
type: "module"
n_genes: 11
n_plus: 11
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: "Respiratory electron transport"
label_source: "reactome"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 220

*Respiratory electron transport · 11 genes (single-armed) · [[Module 220.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

Label from the validation stage: **Respiratory electron transport** (reactome, q 0.001; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | Respiratory electron transport | reactome | 4/11 | 38.9 | 0.001 |
| + | Respiratory electron transport | reactome | 4/11 | 38.9 | 0.001 |
| all | Complex I biogenesis | reactome | 3/11 | 66.3 | 0.005 |
| + | Complex I biogenesis | reactome | 3/11 | 66.3 | 0.005 |
| all | Aerobic respiration and respiratory electron transport | reactome | 4/11 | 23.7 | 0.008 |
| + | Aerobic respiration and respiratory electron transport | reactome | 4/11 | 23.7 | 0.008 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 219), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[TAK-901 (drug)]] 5 µM (+5.6, ⚠ cell-cycle shift); [[Selinexor (drug)]] 5 µM (+4.5, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (+3.3, ⚠ toxic; transcription drop; cell-cycle shift); [[Digitoxin (drug)]] 5 µM (+3.2, ⚠ toxic; transcription drop; cell-cycle shift); [[NG25 (drug)]] 5 µM (+3.2, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (+2.9, ⚠ cell-cycle shift); [[PH-797804 (drug)]] 5 µM (+2.9); [[Dinaciclib (drug)]] 5 µM (+2.6, ⚠ toxic; transcription drop; cell-cycle shift); [[Docetaxel (drug)]] 0.05 µM (+2.4, ⚠ transcription drop; cell-cycle shift); [[Selinexor (drug)]] 0.5 µM (+2.3, ⚠ cell-cycle shift); [[XRK3F2 (drug)]] 0.5 µM (+2.0); [[Ponatinib (drug)]] 5 µM (+1.9); [[GSK1059615 (drug)]] 0.5 µM (+1.8); [[Radotinib (drug)]] 5 µM (+1.8); [[Harringtonine (drug)]] 0.05 µM (+1.7); [[9-ING-41 (drug)]] 0.5 µM (+1.7); [[Pralsetinib (drug)]] 5 µM (+1.6); [[AZD-7648 (drug)]] 5 µM (+1.6); [[Osimertinib (mesylate) (drug)]] 5 µM (+1.6) (69 in all, 21 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)
- Lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM (-6.5, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 5 µM (-3.3, ⚠ cell-cycle shift); [[Auranofin (drug)]] 5 µM (-2.8); [[Epirubicin (hydrochloride) (drug)]] 5 µM (-2.1, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (-2.0, ⚠ cell-cycle shift); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (-1.9, ⚠ cell-cycle shift); [[BAY1125976 (drug)]] 5 µM (-1.9); [[c-Kit-IN-1 (drug)]] 0.05 µM (-1.8, ⚠ unreliable plate only); [[Sapanisertib (drug)]] 5 µM (-1.7); [[Lucanthone (drug)]] 0.05 µM (-1.6); [[9-ING-41 (drug)]] 5 µM (-1.5); [[XRK3F2 (drug)]] 5 µM (-1.5); [[Dabrafenib (drug)]] 5 µM (-1.5); [[5-Azacytidine (drug)]] 5 µM (-1.5); [[Encorafenib (drug)]] 5 µM (-1.4); [[Diphenhydramine (drug)]] 0.05 µM (-1.4) (53 in all, 13 with an alert ⚠; shown: the 10 strongest and the 6 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[LoVo (line)]], [[SW480 (line)]], [[NCI-H460 (line)]], [[LS 180 (line)]], [[NCI-H1792 (line)]], [[NCI-H1573 (line)]], [[KATO III (line)]], [[PANC-1 (line)]]

## Candidate new members

*Members not annotated to the set their arm is enriched for, ranked by mean cos to the annotated members (`validation/novel_members.csv`); ⚠ = a reason to doubt the gene's place (in the vector space only through flagged drug-doses), kept in its rank. 3 candidates, none with an alert.*

| # | Gene | Set | Mean cos |
|---|---|---|---|
| 1 | [[MRPL22]] | Complex I biogenesis | +0.62 |
| 2 | [[PEX2]] | Respiratory electron transport | +0.60 |
| 3 | [[MRPS14]] | Respiratory electron transport | +0.58 |

## + arm (11)

| Gene | Projection | Name |
|---|---|---|
| [[MRPL22]] | 0.871 | mitochondrial ribosomal protein L22 |
| [[NDUFS4]] | 0.853 | NADH:ubiquinone oxidoreductase subunit S4 |
| [[PEX2]] | 0.813 | peroxisomal biogenesis factor 2 |
| [[MRPS14]] | 0.731 | mitochondrial ribosomal protein S14 |
| [[CWC15]] | 0.725 | CWC15 spliceosome associated protein |
| [[NDUFA9]] | 0.720 | NADH:ubiquinone oxidoreductase subunit A9 |
| [[NDUFB6]] | 0.693 | NADH:ubiquinone oxidoreductase subunit B6 |
| [[COA5]] | 0.647 | cytochrome c oxidase assembly factor 5 |
| [[SPIN2B]] | 0.631 | spindlin family member 2B |
| [[NTPCR]] | 0.614 | nucleoside-triphosphatase, cancer-related |
| [[SARNP]] | 0.602 | SAP domain containing ribonucleoprotein |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 220; `graph/modules.parquet` — module == 220; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [219] (drug-dose × line)
