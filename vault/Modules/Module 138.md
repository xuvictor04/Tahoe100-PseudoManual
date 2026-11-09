---
module: 138
type: "module"
n_genes: 34
n_plus: 34
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.27066439390182495
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 138

*34 genes (single-armed) · [[Module 138.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 137), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Homoharringtonine (drug)]] 5 µM (+7.7, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (+5.2, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (+4.6, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (+4.1, ⚠ toxic; transcription drop; cell-cycle shift); [[Digitoxin (drug)]] 5 µM (+3.9, ⚠ toxic; transcription drop; cell-cycle shift); [[Docetaxel (drug)]] 0.05 µM (+3.5, ⚠ transcription drop; cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (+3.2, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+3.2, ⚠ toxic; transcription drop; cell-cycle shift); [[Harringtonine (drug)]] 5 µM (+3.1, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (+2.4, ⚠ cell-cycle shift); [[Ipatasertib (drug)]] 0.5 µM (+2.0); [[XRK3F2 (drug)]] 0.5 µM (+1.8); [[Gallic acid (hydrate) (drug)]] 0.5 µM (+1.6); [[9-ING-41 (drug)]] 0.5 µM (+1.6); [[Bimiralisib (drug)]] 0.5 µM (+1.4); [[Thymol (drug)]] 0.5 µM (+1.4); [[Pyridoxine (drug)]] 0.5 µM (+1.2); [[Vinblastine (sulfate) (drug)]] 0.5 µM (+1.2); [[Pentoxifylline (drug)]] 0.5 µM (+1.2); [[crizotinib (drug)]] 5 µM (+1.2) (38 in all, 18 with an alert ⚠; shown: the 10 strongest and the 10 next strongest without an alert)
- Lower it: [[Ribociclib (drug)]] 0.05 µM (-2.1, ⚠ unreliable plate only; position not correctable); [[Tucidinostat (drug)]] 5 µM (-1.8); [[Doxycycline (monohydrate) (drug)]] 0.5 µM (-1.7); [[Bosentan (hydrate) (drug)]] 0.5 µM (-1.7); [[Verteporfin (drug)]] 5 µM (-1.6); [[Artesunate (drug)]] 0.5 µM (-1.5); [[Loperamide (hydrochloride) (drug)]] 5 µM (-1.4); [[Loperamide (hydrochloride) (drug)]] 0.5 µM (-1.4); [[Tucidinostat (drug)]] 0.5 µM (-1.4, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (-1.4, ⚠ cell-cycle shift); [[Almonertinib (hydrochloride) (drug)]] 0.05 µM (-1.3); [[Afatinib (drug)]] 0.5 µM (-1.3); [[Arbutin (drug)]] 5 µM (-1.2) (29 in all, 5 with an alert ⚠; shown: the 10 strongest and the 3 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[PANC-1 (line)]], [[KATO III (line)]], [[NCI-H460 (line)]], [[LS 180 (line)]], [[HOP62 (line)]], [[SW480 (line)]], [[NCI-H1792 (line)]], [[CFPAC-1 (line)]]

## + arm (34)

| Gene | Projection | Name |
|---|---|---|
| [[CRTC2]] | 0.815 | CREB regulated transcription coactivator 2 |
| [[TEPSIN]] | 0.798 | TEPSIN adaptor related protein complex 4 accessory protein |
| [[USP19]] | 0.779 | ubiquitin specific peptidase 19 |
| [[DMWD]] | 0.770 | DM1 locus, WD repeat containing |
| [[CACTIN]] | 0.748 | cactin, spliceosome C complex subunit |
| [[ZFTRAF1]] | 0.746 | zinc finger TRAF-type and ring finger containing 1 |
| [[GIGYF1]] | 0.725 | GRB10 interacting GYF protein 1 |
| [[PPP1R37]] | 0.718 | protein phosphatase 1 regulatory subunit 37 |
| [[TAOK2]] | 0.694 | TAO kinase 2 |
| [[ISYNA1]] | 0.654 | inositol-3-phosphate synthase 1 |
| [[CLCN7]] | 0.654 | Cl-/H+ antiporter 7 |
| [[LRCH4]] | 0.652 | leucine rich repeats and calponin homology domain containing 4 |
| [[RHBDF1]] | 0.644 | rhomboid 5 homolog 1 |
| [[MLLT6]] | 0.626 | MLLT6, PHD finger containing |
| [[AGRN]] | 0.625 | agrin |
| [[RIPOR1]] | 0.624 | RHO family interacting cell polarization regulator 1 |
| [[RXRB]] | 0.607 | retinoid X receptor beta |
| [[RNF44]] | 0.606 | ring finger protein 44 |
| [[SLC4A2]] | 0.604 | solute carrier family 4 member 2 |
| [[SRF]] | 0.602 | serum response factor |
| [[MGAT4B]] | 0.601 | alpha-1,3-mannosyl-glycoprotein 4-beta-N-acetylglucosaminyltransferase B |
| [[CLPTM1L]] | 0.575 | CLPTM1 like |
| [[DEF8]] | 0.575 | differentially expressed in FDCP 8 homolog |
| [[FOXP4]] | 0.571 | forkhead box P4 |
| [[TRIM28]] | 0.562 | tripartite motif containing 28 |
| [[MTSS2]] | 0.556 | MTSS I-BAR domain containing 2 |
| [[PANK4]] | 0.538 | pantothenate kinase 4 (inactive) |
| [[TBKBP1]] | 0.496 | TBK1 binding protein 1 |
| [[RAVER1]] | 0.493 | ribonucleoprotein, PTB binding 1 |
| [[SGSH]] | 0.490 | N-sulfoglucosamine sulfohydrolase |
| [[PET100]] | 0.477 | PET100 cytochrome c oxidase chaperone |
| [[TRIM41]] | 0.475 | tripartite motif containing 41 |
| [[BOLA3]] | -0.471 | bolA family member 3 |
| [[DUSP3]] | 0.365 | dual specificity phosphatase 3 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 138; `graph/modules.parquet` — module == 138; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [137] (drug-dose × line)
