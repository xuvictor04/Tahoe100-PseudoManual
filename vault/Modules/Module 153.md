---
module: 153
type: "module"
n_genes: 29
n_plus: 29
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.23185060918331146
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 153

*29 genes (single-armed) · [[Module 153.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 152), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Dinaciclib (drug)]] 5 µM (+4.0, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+3.6, ⚠ toxic; transcription drop; cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (+3.6, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (+3.1, ⚠ toxic; transcription drop; cell-cycle shift); [[TAK-901 (drug)]] 5 µM (+3.0, ⚠ cell-cycle shift); [[PH-797804 (drug)]] 5 µM (+2.7); [[Homoharringtonine (drug)]] 5 µM (+2.6, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 0.5 µM (+2.3, ⚠ cell-cycle shift); [[Docetaxel (drug)]] 0.05 µM (+2.1, ⚠ transcription drop; cell-cycle shift); [[Adagrasib (drug)]] 0.05 µM (+1.9, ⚠ position not correctable); [[Folic acid (drug)]] 5 µM (+1.7); [[Bosentan (hydrate) (drug)]] 5 µM (+1.6); [[Budesonide (drug)]] 5 µM (+1.4); [[Dihydroartemisinin (drug)]] 5 µM (+1.4); [[TAK-901 (drug)]] 0.05 µM (+1.4); [[Vismodegib (drug)]] 5 µM (+1.3); [[Pentoxifylline (drug)]] 0.5 µM (+1.3); [[Pyridoxine (hydrochloride) (drug)]] 5 µM (+1.3); [[Adenine (drug)]] 0.05 µM (+1.2) (41 in all, 23 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)
- Lower it: [[Belinostat (drug)]] 5 µM (-4.4, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (-3.7, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (-3.4, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (-3.2, ⚠ cell-cycle shift); [[Belinostat (drug)]] 0.5 µM (-3.2, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (-2.6, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (-2.2); [[Brivudine (drug)]] 5 µM (-2.0); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (-1.8, ⚠ cell-cycle shift); [[Bosentan (hydrate) (drug)]] 0.5 µM (-1.5); [[Loperamide (hydrochloride) (drug)]] 5 µM (-1.4); [[Azithromycin (hydrate) (drug)]] 5 µM (-1.4); [[Gallic acid (hydrate) (drug)]] 0.05 µM (-1.4); [[Adagrasib (drug)]] 5 µM (-1.3); [[Doxycycline (monohydrate) (drug)]] 0.5 µM (-1.2); [[Bisoprolol (hemifumarate) (drug)]] 5 µM (-1.2); [[AT7519 (drug)]] 0.05 µM (-1.1) (32 in all, 11 with an alert ⚠; shown: the 10 strongest and the 7 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[PANC-1 (line)]], [[NCI-H460 (line)]], [[A-427 (line)]], [[SNU-1 (line)]], [[NCI-H23 (line)]], [[NCI-H1573 (line)]], [[SW1417 (line)]], [[A-172 (line)]]

*⚠ 1 of its 29 genes are in the vector space only through drug-doses that carry an alert (`embed/genes.parquet` evidence_flagged_only): their place here may reflect what those drug-doses did to the cells. They are marked in the tables of this note.*

## + arm (29)

| Gene | Projection | Name | Alert |
|---|---|---|---|
| [[ATP13A1]] | 0.899 | ATPase 13A1 |  |
| [[SF3B4]] | 0.821 | splicing factor 3b subunit 4 |  |
| [[WASH8P]] | 0.811 | WAS protein family homolog 8, pseudogene | ⚠ only flagged evidence |
| [[ZBED6]] | 0.783 | zinc finger BED-type containing 6 |  |
| [[MTX1]] | 0.780 | metaxin 1 |  |
| [[STRN4]] | 0.769 | striatin 4 |  |
| [[SF3A1]] | 0.764 | splicing factor 3a subunit 1 |  |
| [[RAB1B]] | 0.760 | RAB1B, member RAS oncogene family |  |
| [[ANAPC2]] | 0.742 | anaphase promoting complex subunit 2 |  |
| [[RAB11B]] | 0.728 | RAB11B, member RAS oncogene family |  |
| [[POMK]] | 0.722 | protein O-mannose kinase |  |
| [[BAG6]] | 0.720 | BAG cochaperone 6 |  |
| [[PPP2R1A]] | 0.714 | protein phosphatase 2 scaffold subunit Aalpha |  |
| [[USP22]] | 0.690 | ubiquitin specific peptidase 22 |  |
| [[RANBP3]] | 0.690 | RAN binding protein 3 |  |
| [[WASH9P]] | 0.689 | WAS protein family homolog 9, pseudogene |  |
| [[PCIF1]] | 0.681 | phosphorylated CTD interacting factor 1 |  |
| [[EXOSC10]] | 0.664 | exosome component 10 |  |
| [[ZBTB22]] | 0.655 | zinc finger and BTB domain containing 22 |  |
| [[ARAF]] | 0.652 | A-Raf proto-oncogene, serine/threonine kinase |  |
| [[SMARCD1]] | 0.614 | SWI/SNF related BAF chromatin remodeling complex subunit D1 |  |
| [[TARBP2]] | 0.583 | TARBP2 subunit of RISC loading complex |  |
| [[USP21]] | 0.581 | ubiquitin specific peptidase 21 |  |
| [[BMS1P2]] | 0.565 | BMS1 pseudogene 2 |  |
| [[THBS3]] | 0.562 | thrombospondin 3 |  |
| [[KLHL11]] | 0.507 | kelch like family member 11 |  |
| [[JMJD7]] | 0.421 | jumonji domain containing 7 |  |
| [[SAT1]] | -0.375 | spermidine/spermine N1-acetyltransferase 1 |  |
| [[DTX2P1]] | 0.367 | DTX2 pseudogene 1 |  |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 153; `graph/modules.parquet` — module == 153; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [152] (drug-dose × line)
