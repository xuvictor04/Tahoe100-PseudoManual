---
module: 165
type: "module"
n_genes: 26
n_plus: 26
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 165

*26 genes (single-armed) · [[Module 165.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 164), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM (+22.4, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 5 µM (+15.0, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (+13.3, ⚠ toxic; transcription drop; cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (+12.5); [[Dinaciclib (drug)]] 0.5 µM (+12.4, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+9.9, ⚠ toxic; transcription drop; cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 0.5 µM (+8.5, ⚠ cell-cycle shift); [[Auranofin (drug)]] 5 µM (+8.1); [[Panobinostat (drug)]] 5 µM (+7.3, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 0.5 µM (+6.9, ⚠ cell-cycle shift); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+6.6); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM (+2.0); [[Ipatasertib (drug)]] 0.5 µM (+1.9); [[Amsacrine (drug)]] 5 µM (+1.8); [[Verteporfin (drug)]] 5 µM (+1.7); [[Decitabine (drug)]] 0.5 µM (+1.6); [[Docetaxel (Trihydrate) (drug)]] 0.5 µM (+1.6); [[Methylprednisolone succinate (drug)]] 0.5 µM (+1.6) (65 in all, 31 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)
- Lower it: [[Adagrasib (drug)]] 0.05 µM (-2.7, ⚠ position not correctable); [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM (-1.9); [[Lucanthone (drug)]] 0.05 µM (-1.6); [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM (-1.6); [[Trametinib (drug)]] 5 µM (-1.5, ⚠ cell-cycle shift); [[Radotinib (drug)]] 5 µM (-1.5); [[Anethole trithione (drug)]] 0.5 µM (-1.5); [[Erlotinib (drug)]] 0.05 µM (-1.5); [[Fenofibrate (drug)]] 0.05 µM (-1.4); [[Pyridoxine (hydrochloride) (drug)]] 5 µM (-1.4); [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM (-1.3); [[Ipatasertib (drug)]] 5 µM (-1.3) (28 in all, 4 with an alert ⚠; shown: the 10 strongest and the 2 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[SW480 (line)]], [[HEC-1-A (line)]], [[NCI-H460 (line)]], [[A-427 (line)]], [[LoVo (line)]], [[RKO (line)]], [[A498 (line)]], [[HOP62 (line)]]

## + arm (26)

| Gene | Projection | Name |
|---|---|---|
| [[DLGAP2]] | 0.903 | DLG associated protein 2 |
| [[ATP8A2]] | 0.872 | ATPase phospholipid transporting 8A2 |
| [[MTUS2]] | 0.865 | microtubule associated scaffold protein 2 |
| [[RELN]] | 0.850 | reelin |
| [[SLC8A1-AS1]] | 0.844 | SLC8A1 antisense RNA 1 |
| [[RYR3]] | 0.831 | ryanodine receptor 3 |
| [[CCDC26]] | 0.824 | CCDC26 long non-coding RNA |
| [[OPCML]] | 0.807 | opioid binding protein/cell adhesion molecule like |
| [[COL23A1]] | 0.797 | collagen type XXIII alpha 1 chain |
| [[RETREG1-AS1]] | 0.782 | RETREG1 antisense RNA 1 |
| [[PLD5]] | 0.745 | phospholipase D family member 5 |
| [[CACNA1A]] | 0.738 | calcium voltage-gated channel subunit alpha1 A |
| [[ASIC2]] | 0.729 | acid sensing ion channel subunit 2 |
| [[DELEC1]] | 0.709 | deleted in esophageal cancer 1 |
| [[PLXNA4]] | 0.702 | plexin A4 |
| [[AP3B2]] | 0.697 | adaptor related protein complex 3 subunit beta 2 |
| [[ZPLD1]] | 0.686 | zona pellucida like domain containing 1 |
| [[DIRC3-AS1]] | 0.671 | testicular germ cell expressed HSF2 interacting lncRNA |
| [[RERGL]] | 0.669 | RERG like |
| [[NOS1]] | 0.658 | nitric oxide synthase 1 |
| [[TMEM132B]] | 0.657 | transmembrane protein 132B |
| [[DISP3]] | 0.653 | dispatched RND transporter family member 3 |
| [[DNMBP-AS1]] | 0.650 | DNMBP antisense RNA 1 |
| [[SLC7A11-AS1]] | 0.606 | SLC7A11 antisense RNA 1 |
| [[SMPD3]] | 0.558 | sphingomyelin phosphodiesterase 3 |
| [[NPTX2]] | 0.499 | neuronal pentraxin 2 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 165; `graph/modules.parquet` — module == 165; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [164] (drug-dose × line)
