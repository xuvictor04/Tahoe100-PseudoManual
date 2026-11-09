---
module: 127
type: "module"
n_genes: 37
n_plus: 37
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.26553046703338623
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 127

*37 genes (single-armed) · [[Module 127.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 126), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[TAK-901 (drug)]] 5 µM (+4.0, ⚠ cell-cycle shift); [[PH-797804 (drug)]] 5 µM (+3.4); [[Panobinostat (drug)]] 5 µM (+3.2, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (+3.1, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (+2.7, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (+2.5, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+1.9, ⚠ toxic; transcription drop; cell-cycle shift); [[TAK-901 (drug)]] 0.05 µM (+1.8); [[Docetaxel (drug)]] 0.05 µM (+1.7, ⚠ transcription drop; cell-cycle shift); [[Adagrasib (drug)]] 0.05 µM (+1.7, ⚠ position not correctable); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+1.3); [[Budesonide (drug)]] 5 µM (+1.2); [[PH-797804 (drug)]] 0.05 µM (+1.1); [[Bosentan (hydrate) (drug)]] 5 µM (+1.1); [[Arbutin (drug)]] 0.5 µM (+1.1); [[Cobimetinib (drug)]] 0.5 µM (+1.1); [[Erlotinib (drug)]] 5 µM (+1.1); [[Belumosudil (drug)]] 5 µM (+1.0) (23 in all, 12 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)
- Lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM (-2.6, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 5 µM (-2.2, ⚠ toxic; transcription drop; cell-cycle shift); [[Ribociclib (drug)]] 0.05 µM (-1.9, ⚠ unreliable plate only; position not correctable); [[Tucidinostat (drug)]] 5 µM (-1.8); [[Epirubicin (hydrochloride) (drug)]] 5 µM (-1.5, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-1.5, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (-1.5, ⚠ cell-cycle shift); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (-1.5, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 0.5 µM (-1.5, ⚠ cell-cycle shift); [[Carbidopa (monohydrate) (drug)]] 0.05 µM (-1.5, ⚠ unreliable plate only; position not correctable); [[Bosentan (hydrate) (drug)]] 0.5 µM (-1.2); [[Loperamide (hydrochloride) (drug)]] 5 µM (-1.1); [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM (-1.1); [[Decitabine (drug)]] 0.5 µM (-1.1); [[Peretinoin (drug)]] 5 µM (-1.1) (19 in all, 13 with an alert ⚠; shown: the 10 strongest and the 5 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[SW480 (line)]], [[RKO (line)]], [[SNU-1 (line)]], [[SHP-77 (line)]], [[PANC-1 (line)]], [[LS 180 (line)]], [[COLO 205 (line)]], [[LoVo (line)]]

## + arm (37)

| Gene | Projection | Name |
|---|---|---|
| [[BAP1]] | 0.876 | BRCA1 associated deubiquitinase 1 |
| [[PRPF31]] | 0.857 | pre-mRNA processing factor 31 |
| [[SNRNP200]] | 0.839 | small nuclear ribonucleoprotein U5 subunit 200 |
| [[PCNX3]] | 0.768 | pecanex 3 |
| [[PRPF8]] | 0.762 | pre-mRNA processing factor 8 |
| [[ABCF3]] | 0.757 | ATP binding cassette subfamily F member 3 |
| [[NOP9]] | 0.755 | NOP9 nucleolar protein |
| [[TAF6]] | 0.748 | TATA-box binding protein associated factor 6 |
| [[GTF3C1]] | 0.732 | general transcription factor IIIC subunit 1 |
| [[STK36]] | 0.714 | serine/threonine kinase 36 |
| [[EMC1]] | 0.704 | ER membrane protein complex subunit 1 |
| [[CDK9]] | 0.699 | cyclin dependent kinase 9 |
| [[TOP3B]] | 0.694 | DNA topoisomerase III beta |
| [[CUL9]] | 0.686 | cullin 9 |
| [[RNF40]] | 0.685 | ring finger protein 40 |
| [[DMAP1]] | 0.683 | DNA methyltransferase 1 associated protein 1 |
| [[SCRIB]] | 0.679 | scribble planar cell polarity protein |
| [[CCAR2]] | 0.674 | cell cycle and apoptosis regulator 2 |
| [[SNAP47]] | 0.657 | synaptosome associated protein 47 |
| [[DHX16]] | 0.656 | DEAH-box helicase 16 |
| [[MEN1]] | 0.648 | menin 1 |
| [[MSX1]] | -0.629 | msh homeobox 1 |
| [[EXOC3]] | 0.619 | exocyst complex component 3 |
| [[COPS7A]] | 0.618 | COP9 signalosome subunit 7A |
| [[PIP4K2B]] | 0.601 | phosphatidylinositol-5-phosphate 4-kinase type 2 beta |
| [[HIF1AN]] | 0.601 | hypoxia inducible factor 1 subunit alpha inhibitor |
| [[TTC31]] | 0.593 | tetratricopeptide repeat domain 31 |
| [[GTF2H4]] | 0.591 | general transcription factor IIH subunit 4 |
| [[INTS3]] | 0.547 | integrator complex subunit 3 |
| [[IKBKG]] | 0.530 | inhibitor of nuclear factor kappa B kinase regulatory subunit gamma |
| [[TMTC2]] | -0.462 | transmembrane O-mannosyltransferase targeting cadherins 2 |
| [[STK11IP]] | 0.458 | serine/threonine kinase 11 interacting protein |
| [[PDK2]] | 0.445 | pyruvate dehydrogenase kinase 2 |
| [[MADD]] | 0.433 | MAP kinase activating death domain |
| [[BCL7A]] | -0.431 | BAF chromatin remodeling complex subunit BCL7A |
| [[LZTFL1]] | 0.303 | leucine zipper transcription factor like 1 |
| [[HDAC7]] | -0.222 | histone deacetylase 7 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 127; `graph/modules.parquet` — module == 127; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [126] (drug-dose × line)
