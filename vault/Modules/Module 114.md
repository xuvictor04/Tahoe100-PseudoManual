---
module: 114
type: "module"
n_genes: 42
n_plus: 42
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.37972408533096313
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 114

*42 genes (single-armed) · [[Module 114.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 113), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Homoharringtonine (drug)]] 5 µM (+4.8, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (+4.6, ⚠ cell-cycle shift); [[Topotecan (hydrochloride) (drug)]] 5 µM (+4.4, ⚠ toxic; cell-cycle shift); [[Auranofin (drug)]] 5 µM (+2.6); [[Idarubicin (hydrochloride) (drug)]] 5 µM (+2.4, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (+2.0, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.05 µM (+2.0); [[Selinexor (drug)]] 5 µM (+2.0, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (+1.8, ⚠ cell-cycle shift); [[Bortezomib (drug)]] 0.05 µM (+1.8, ⚠ cell-cycle shift); [[Clobetasol propionate (drug)]] 0.5 µM (+1.7); [[Ipatasertib (drug)]] 0.5 µM (+1.7); [[Cabozantinib (S-malate) (drug)]] 0.05 µM (+1.5); [[Docetaxel (Trihydrate) (drug)]] 0.5 µM (+1.4); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+1.4); [[ULK-101 (drug)]] 0.05 µM (+1.3); [[Ponatinib (drug)]] 0.5 µM (+1.3); [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM (+1.3) (32 in all, 14 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)
- Lower it: [[Niclosamide (olamine) (drug)]] 5 µM (-4.9, ⚠ toxic; cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (-4.6, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (-3.8, ⚠ toxic; transcription drop; cell-cycle shift); [[Belinostat (drug)]] 5 µM (-3.8, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (-3.6, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (-3.2, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (-2.8, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (-2.5, ⚠ toxic; transcription drop; cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (-2.4); [[Belinostat (drug)]] 0.5 µM (-1.9, ⚠ cell-cycle shift); [[Brivudine (drug)]] 5 µM (-1.8); [[Clopidogrel (drug)]] 0.05 µM (-1.3); [[Cyclosporin A (drug)]] 0.05 µM (-1.3); [[Mebendazole (drug)]] 5 µM (-1.1); [[Terfenadine (drug)]] 0.5 µM (-1.1); [[Gefitinib (drug)]] 5 µM (-1.1) (19 in all, 12 with an alert ⚠; shown: the 10 strongest and the 6 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[NCI-H23 (line)]], [[PANC-1 (line)]], [[SK-MEL-2 (line)]], [[NCI-H460 (line)]], [[NCI-H1573 (line)]], [[SW480 (line)]], [[A-427 (line)]], [[KATO III (line)]]

## + arm (42)

| Gene | Projection | Name |
|---|---|---|
| [[ZNF721]] | 0.882 | zinc finger protein 721 |
| [[ALKBH1]] | 0.873 | alkB homolog 1, histone H2A dioxygenase |
| [[MTG2]] | 0.851 | mitochondrial ribosome associated GTPase 2 |
| [[ZC3HC1]] | 0.833 | zinc finger C3HC-type containing 1 |
| [[ZCCHC10]] | 0.800 | zinc finger CCHC-type containing 10 |
| [[FBXO28]] | 0.792 | F-box protein 28 |
| [[DOHH]] | 0.792 | deoxyhypusine hydroxylase |
| [[GPN2]] | 0.778 | GPN-loop GTPase 2 |
| [[ZBTB8OS]] | 0.772 | tRNA splicing ligase complex subunit 1 |
| [[SETDB1]] | 0.767 | SET domain bifurcated histone lysine methyltransferase 1 |
| [[GMEB2]] | 0.765 | glucocorticoid modulatory element binding protein 2 |
| [[ZNF506]] | 0.758 | zinc finger protein 506 |
| [[BMS1P4-1]] | 0.743 | — |
| [[ZNF271P]] | 0.715 | zinc finger protein 271, pseudogene |
| [[ZNF586]] | 0.712 | zinc finger protein 586 |
| [[RPAP1]] | 0.710 | RNA polymerase II associated protein 1 |
| [[MTHFS]] | 0.709 | methenyltetrahydrofolate synthetase |
| [[GOSR1]] | 0.708 | golgi SNAP receptor complex member 1 |
| [[ZNF35]] | 0.697 | zinc finger protein 35 |
| [[LAMB2P1]] | 0.688 | laminin subunit beta 2 pseudogene 1 |
| [[TMEM222]] | 0.686 | transmembrane protein 222 |
| [[SNRNP35]] | 0.680 | small nuclear ribonucleoprotein U11/U12 subunit 35 |
| [[C10orf88]] | 0.668 | chromosome 10 open reading frame 88 |
| [[ZKSCAN2-DT]] | 0.664 | ZKSCAN2 divergent transcript |
| [[ZNF653]] | 0.650 | zinc finger protein 653 |
| [[BMS1P4]] | 0.648 | BMS1 pseudogene 4 |
| [[DCAF10]] | 0.637 | DDB1 and CUL4 associated factor 10 |
| [[GGA3]] | 0.623 | golgi associated, gamma adaptin ear containing, ARF binding protein 3 |
| [[ZSCAN32]] | 0.622 | zinc finger and SCAN domain containing 32 |
| [[TRIM13]] | 0.616 | tripartite motif containing 13 |
| [[LSM1]] | 0.608 | LSM1 homolog, mRNA degradation associated |
| [[PIGC]] | 0.597 | phosphatidylinositol glycan anchor biosynthesis class C |
| [[HSCB]] | 0.585 | HscB mitochondrial iron-sulfur cluster cochaperone |
| [[ITFG2]] | 0.583 | integrin alpha FG-GAP repeat containing 2 |
| [[YBEY]] | 0.582 | ybeY metalloendoribonuclease |
| [[DIAPH1]] | -0.580 | diaphanous related formin 1 |
| [[KRIT1]] | 0.561 | KRIT1 ankyrin repeat containing |
| [[GOLIM4]] | -0.556 | golgi integral membrane protein 4 |
| [[COMMD1]] | 0.553 | copper metabolism domain containing 1 |
| [[SLC7A6OS]] | 0.546 | solute carrier family 7 member 6 opposite strand |
| [[B9D1]] | 0.518 | B9 domain containing 1 |
| [[ZNF580]] | 0.464 | zinc finger protein 580 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 114; `graph/modules.parquet` — module == 114; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [113] (drug-dose × line)
