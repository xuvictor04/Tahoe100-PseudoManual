---
module: 189
type: "module"
n_genes: 18
n_plus: 18
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.3257055878639221
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 189

*18 genes (single-armed) · [[Module 189.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 188), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Panobinostat (drug)]] 5 µM (+6.2, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 5 µM (+5.8, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (+5.8, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (+4.3, ⚠ cell-cycle shift); [[Pitavastatin (Calcium) (drug)]] 5 µM (+2.7, ⚠ cell-cycle shift); [[Pitavastatin (Calcium) (drug)]] 0.5 µM (+2.7); [[Tucidinostat (drug)]] 5 µM (+2.6); [[Daptomycin (drug)]] 5 µM (+2.1, ⚠ unreliable plate only); [[Panobinostat (drug)]] 0.05 µM (+1.9, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (+1.8, ⚠ cell-cycle shift); [[Ipatasertib (drug)]] 0.5 µM (+1.8); [[Vinblastine (sulfate) (drug)]] 5 µM (+1.6); [[PF-06260933 (drug)]] 5 µM (+1.6); [[9-ING-41 (drug)]] 0.5 µM (+1.4); [[Niclosamide (olamine) (drug)]] 0.5 µM (+1.3); [[Vinblastine (sulfate) (drug)]] 0.5 µM (+1.3); [[Peretinoin (drug)]] 0.5 µM (+1.2); [[Thymol (drug)]] 0.5 µM (+1.2) (36 in all, 16 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)
- Lower it: [[Digitoxin (drug)]] 0.5 µM (-3.0, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (-3.0, ⚠ cell-cycle shift); [[Selinexor (drug)]] 5 µM (-2.9, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (-2.8, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (-2.7, ⚠ cell-cycle shift); [[TAK-901 (drug)]] 5 µM (-2.4, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 5 µM (-2.2, ⚠ toxic; transcription drop; cell-cycle shift); [[Epirubicin (hydrochloride) (drug)]] 5 µM (-1.9, ⚠ cell-cycle shift); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (-1.8, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 0.05 µM (-1.8, ⚠ cell-cycle shift); [[TAK-901 (drug)]] 0.05 µM (-1.7); [[PH-797804 (drug)]] 5 µM (-1.7); [[Clobetasol propionate (drug)]] 0.05 µM (-1.6); [[Budesonide (drug)]] 0.05 µM (-1.6); [[Betamethasone dipropionate (drug)]] 5 µM (-1.5); [[Medroxyprogesterone acetate (drug)]] 5 µM (-1.5); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (-1.5); [[Triamcinolone (drug)]] 0.5 µM (-1.4); [[Medroxyprogesterone acetate (drug)]] 0.05 µM (-1.3); [[Clobetasol propionate (drug)]] 5 µM (-1.3) (43 in all, 17 with an alert ⚠; shown: the 10 strongest and the 10 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[SW480 (line)]], [[PANC-1 (line)]], [[KATO III (line)]], [[LoVo (line)]], [[MIA PaCa-2 (line)]], [[A549 (line)]], [[J82 (line)]], [[HEC-1-A (line)]]

## + arm (18)

| Gene | Projection | Name |
|---|---|---|
| [[DLGAP4]] | 0.865 | DLG associated protein 4 |
| [[ARVCF]] | 0.769 | ARVCF delta catenin family member |
| [[ACAP3]] | 0.744 | ArfGAP with coiled-coil, ankyrin repeat and PH domains 3 |
| [[RELA]] | 0.733 | RELA proto-oncogene, NF-kB subunit |
| [[PORCN]] | 0.727 | porcupine O-acyltransferase |
| [[SLC9A3R2]] | 0.726 | NHERF family PDZ scaffold protein 2 |
| [[PTPRH]] | 0.712 | protein tyrosine phosphatase receptor type H |
| [[RING1]] | 0.710 | ring finger protein 1 |
| [[PDLIM7]] | 0.675 | PDZ and LIM domain 7 |
| [[ARID5A]] | 0.663 | AT-rich interaction domain 5A |
| [[DAPK3]] | 0.633 | death associated protein kinase 3 |
| [[RMC1]] | 0.629 | regulator of MON1-CCZ1 |
| [[MEGF6]] | 0.618 | multiple EGF like domains 6 |
| [[ACTR1B]] | 0.611 | actin related protein 1B |
| [[DNAJB5]] | 0.607 | DnaJ heat shock protein family (Hsp40) member B5 |
| [[CDC42BPG]] | 0.562 | CDC42 binding protein kinase gamma |
| [[ITPKB]] | -0.538 | inositol-trisphosphate 3-kinase B |
| [[RAP1GAP]] | 0.531 | RAP1 GTPase activating protein |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 189; `graph/modules.parquet` — module == 189; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [188] (drug-dose × line)
