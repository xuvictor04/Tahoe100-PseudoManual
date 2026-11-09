---
module: 215
type: "module"
n_genes: 13
n_plus: 13
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.41425374150276184
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 215

*13 genes (single-armed) · [[Module 215.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 214), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Dinaciclib (drug)]] 5 µM (+9.2, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (+8.8, ⚠ toxic; transcription drop; cell-cycle shift); [[Panobinostat (drug)]] 5 µM (+6.6, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+6.3, ⚠ toxic; transcription drop; cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (+6.0, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (+5.6, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (+5.0, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 5 µM (+4.9, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (+4.3, ⚠ cell-cycle shift); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (+3.9, ⚠ cell-cycle shift); [[Auranofin (drug)]] 5 µM (+3.5); [[Ixazomib citrate (drug)]] 0.5 µM (+2.8); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+2.7); [[Homoharringtonine (drug)]] 0.05 µM (+2.3); [[Belumosudil (drug)]] 5 µM (+1.6); [[Brivudine (drug)]] 5 µM (+1.4); [[TAK-733 (drug)]] 5 µM (+1.3); [[Harringtonine (drug)]] 0.05 µM (+1.3); [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM (+1.1) (36 in all, 27 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)
- Lower it: [[Digitoxin (drug)]] 5 µM (-3.6, ⚠ toxic; transcription drop; cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (-2.4, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (-2.3, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 0.5 µM (-2.2, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 0.5 µM (-1.3, ⚠ cell-cycle shift); [[Ipatasertib (drug)]] 0.5 µM (-1.1); [[Pimozide (drug)]] 0.5 µM (-1.1, ⚠ transcription drop); [[Tucidinostat (drug)]] 0.05 µM (-1.0) (8 in all, 6 with an alert ⚠)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[NCI-H1573 (line)]], [[PANC-1 (line)]], [[SW480 (line)]], [[A549 (line)]], [[SNU-423 (line)]], [[A498 (line)]], [[NCI-H2347 (line)]], [[NCI-H1792 (line)]]

## + arm (13)

| Gene | Projection | Name |
|---|---|---|
| [[PDAP1]] | 0.866 | PDGFA associated protein 1 |
| [[PSMC3]] | 0.822 | proteasome 26S subunit, ATPase 3 |
| [[C17orf80]] | 0.809 | mitochondrial nucleoid associated protein 1 |
| [[PUS7L]] | 0.792 | pseudouridine synthase 7 like |
| [[ZNF460]] | 0.786 | zinc finger protein 460 |
| [[HSPB8]] | 0.762 | heat shock protein family B (small) member 8 |
| [[RBM38]] | -0.711 | RNA binding motif protein 38 |
| [[C1QL1]] | -0.668 | complement C1q like 1 |
| [[UCHL5]] | 0.635 | ubiquitin C-terminal hydrolase L5 |
| [[LMBRD2]] | 0.588 | LMBR1 domain containing 2 |
| [[EXOC7]] | 0.560 | exocyst complex component 7 |
| [[USP38]] | 0.559 | ubiquitin specific peptidase 38 |
| [[TYW1B]] | -0.535 | tRNA-yW synthesizing protein 1 homolog B |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 215; `graph/modules.parquet` — module == 215; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [214] (drug-dose × line)
