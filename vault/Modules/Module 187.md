---
module: 187
type: "module"
n_genes: 18
n_plus: 18
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 187

*18 genes (single-armed) · [[Module 187.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 186), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM (+5.1, ⚠ cell-cycle shift); [[Bortezomib (drug)]] 0.05 µM (+5.1, ⚠ cell-cycle shift); [[Ixazomib citrate (drug)]] 5 µM (+4.7, ⚠ cell-cycle shift); [[Ixazomib citrate (drug)]] 0.5 µM (+3.9); [[Bortezomib (drug)]] 0.5 µM (+2.1); [[GSK1059615 (drug)]] 5 µM (+2.1); [[Bimiralisib (drug)]] 5 µM (+1.9); [[Trametinib (drug)]] 5 µM (+1.8, ⚠ cell-cycle shift); [[Selinexor (drug)]] 5 µM (+1.7, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 5 µM (+1.7, ⚠ cell-cycle shift); [[Ponatinib (drug)]] 5 µM (+1.7); [[Temsirolimus (drug)]] 5 µM (+1.5); [[ULK-101 (drug)]] 0.05 µM (+1.5); [[Bimiralisib (drug)]] 0.05 µM (+1.5); [[MK-3903 (drug)]] 5 µM (+1.4); [[Cabozantinib (S-malate) (drug)]] 5 µM (+1.4) (48 in all, 13 with an alert ⚠; shown: the 10 strongest and the 6 next strongest without an alert)
- Lower it: [[c-Kit-IN-1 (drug)]] 0.05 µM (-12.2, ⚠ unreliable plate only); [[Dinaciclib (drug)]] 0.5 µM (-8.2, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (-8.2, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (-7.4, ⚠ toxic; transcription drop; cell-cycle shift); [[TAK-733 (drug)]] 5 µM (-6.1); [[Abemaciclib (drug)]] 5 µM (-5.9); [[EX229 (drug)]] 5 µM (-5.7); [[c-Kit-IN-1 (drug)]] 5 µM (-5.5); [[venetoclax (drug)]] 5 µM (-5.3); [[EX229 (drug)]] 0.05 µM (-3.1); [[Abemaciclib (drug)]] 0.5 µM (-3.0); [[EX229 (drug)]] 0.5 µM (-2.8); [[Auranofin (drug)]] 5 µM (-2.5); [[Sapanisertib (drug)]] 0.5 µM (-2.4) (52 in all, 13 with an alert ⚠; shown: the 10 strongest and the 4 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[NCI-H1792 (line)]], [[NCI-H460 (line)]], [[MIA PaCa-2 (line)]], [[A549 (line)]], [[NCI-H2347 (line)]], [[PANC-1 (line)]], [[CFPAC-1 (line)]], [[A498 (line)]]

## + arm (18)

| Gene | Projection | Name |
|---|---|---|
| [[EAPP]] | 0.900 | E2F associated phosphoprotein |
| [[BSDC1]] | 0.829 | BSD domain containing 1 |
| [[ATXN3]] | 0.824 | ataxin 3 |
| [[IKZF5]] | 0.783 | IKAROS family zinc finger 5 |
| [[CDC37L1]] | 0.777 | cell division cycle 37 like 1, HSP90 cochaperone |
| [[EZH1]] | 0.776 | enhancer of zeste 1 polycomb repressive complex 2 subunit |
| [[KLHDC2]] | 0.774 | kelch domain containing 2 |
| [[AGO4]] | 0.713 | argonaute RISC component 4 |
| [[PAPOLG]] | 0.686 | poly(A) polymerase gamma |
| [[RETREG3]] | 0.657 | reticulophagy regulator family member 3 |
| [[BBS4]] | 0.645 | Bardet-Biedl syndrome 4 |
| [[PCAT7]] | 0.632 | prostate cancer associated transcript 7 |
| [[UBR2]] | 0.622 | ubiquitin protein ligase E3 component n-recognin 2 |
| [[GABARAPL1]] | 0.595 | GABA type A receptor associated protein like 1 |
| [[HELB]] | 0.586 | DNA helicase B |
| [[CEP68]] | 0.586 | centrosomal protein 68 |
| [[ATG13]] | 0.516 | autophagy related 13 |
| [[AFF1]] | 0.332 | ALF transcription elongation factor 1 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 187; `graph/modules.parquet` — module == 187; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [186] (drug-dose × line)
