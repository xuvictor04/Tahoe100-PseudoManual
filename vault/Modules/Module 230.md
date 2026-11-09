---
module: 230
type: "module"
n_genes: 6
n_plus: 6
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 230

*6 genes (single-armed) · [[Module 230.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 229), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Panobinostat (drug)]] 5 µM (+13.0, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (+11.3, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (+8.8, ⚠ cell-cycle shift); [[Selinexor (drug)]] 5 µM (+4.5, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (+4.1, ⚠ cell-cycle shift); [[Cobimetinib (drug)]] 5 µM (+3.9); [[Belumosudil (drug)]] 5 µM (+3.8); [[Ponatinib (drug)]] 5 µM (+3.7); [[Selinexor (drug)]] 0.5 µM (+3.2, ⚠ cell-cycle shift); [[Ponatinib (drug)]] 0.5 µM (+3.2); [[Trametinib (drug)]] 0.05 µM (+3.1); [[Brivudine (drug)]] 5 µM (+3.0); [[Bimiralisib (drug)]] 5 µM (+3.0); [[Cobimetinib (drug)]] 0.5 µM (+2.7); [[Clobetasol propionate (drug)]] 0.05 µM (+2.7); [[Binimetinib (drug)]] 0.05 µM (+2.6) (128 in all, 20 with an alert ⚠; shown: the 10 strongest and the 6 next strongest without an alert)
- Lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM (-20.6, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (-9.3, ⚠ toxic; transcription drop; cell-cycle shift); [[Digitoxin (drug)]] 5 µM (-9.0, ⚠ toxic; transcription drop; cell-cycle shift); [[Auranofin (drug)]] 5 µM (-8.8); [[Ouabain (Octahydrate) (drug)]] 5 µM (-8.6, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (-8.6, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (-8.5, ⚠ toxic; transcription drop; cell-cycle shift); [[Epirubicin (hydrochloride) (drug)]] 5 µM (-8.0, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 0.5 µM (-7.8, ⚠ cell-cycle shift); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (-7.3, ⚠ cell-cycle shift); [[Peretinoin (drug)]] 0.5 µM (-3.0); [[Vinblastine (sulfate) (drug)]] 5 µM (-2.5); [[PF-06260933 (drug)]] 5 µM (-2.4); [[Vinblastine (sulfate) (drug)]] 0.5 µM (-2.3); [[Vilanterol (drug)]] 5 µM (-2.1); [[Peretinoin (drug)]] 5 µM (-2.1); [[Niclosamide (olamine) (drug)]] 0.5 µM (-2.1); [[Pimitespib (drug)]] 5 µM (-1.9); [[Dimethyl fumarate (drug)]] 5 µM (-1.9) (105 in all, 29 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[LoVo (line)]], [[SW480 (line)]], [[NCI-H460 (line)]], [[PANC-1 (line)]], [[LS 180 (line)]], [[MIA PaCa-2 (line)]], [[SW1417 (line)]], [[HT-29 (line)]]

## + arm (6)

| Gene | Projection | Name |
|---|---|---|
| [[WDR70]] | 0.869 | WD repeat domain 70 |
| [[STX8]] | 0.852 | syntaxin 8 |
| [[WDR7]] | 0.829 | WD repeat domain 7 |
| [[CSTPP1]] | 0.810 | centriolar satellite-associated tubulin polyglutamylase complex regulator 1 |
| [[VPS50]] | 0.781 | VPS50 subunit of EARP/GARPII complex |
| [[VPS8]] | 0.589 | VPS8 subunit of CORVET complex |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 230; `graph/modules.parquet` — module == 230; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [229] (drug-dose × line)
