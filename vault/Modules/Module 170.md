---
module: 170
type: "module"
n_genes: 24
n_plus: 18
n_minus: 6
arms_opposite: true
mean_cos_between_arms: -0.39593279361724854
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 170

*24 genes (18 in the + arm, 6 in the − arm) · [[Module 170.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40). The + arm rises where the − arm falls. Arm = the side of the module's main direction a gene sits on.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| - | Synthesis of very long-chain fatty acyl-CoAs | reactome | 2/6 | 279 | 0.009 |
| - | Fatty acyl-CoA biosynthesis | reactome | 2/6 | 179 | 0.020 |

## Drugs that move it

*Mean pooled z of the + arm minus the − arm (`graph/module_pooled_z.npy`, row 169), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it (+ arm up, − arm down): [[Homoharringtonine (drug)]] 5 µM (+9.0, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (+7.7, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (+5.4, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.05 µM (+4.8); [[Harringtonine (drug)]] 0.5 µM (+4.5, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 0.5 µM (+3.9, ⚠ cell-cycle shift); [[TAK-901 (drug)]] 5 µM (+3.6, ⚠ cell-cycle shift); [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM (+3.5, ⚠ cell-cycle shift); [[5-Azacytidine (drug)]] 5 µM (+2.9); [[Trametinib (drug)]] 5 µM (+2.9, ⚠ cell-cycle shift); [[Pexidartinib (hydrochloride) (drug)]] 5 µM (+2.9); [[Neratinib (maleate) (drug)]] 5 µM (+2.8); [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM (+2.7); [[Pitavastatin (Calcium) (drug)]] 0.5 µM (+2.7); [[Lactate (calcium) (drug)]] 0.5 µM (+2.7); [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM (+2.6); [[Harringtonine (drug)]] 0.05 µM (+2.6); [[Vortioxetine (drug)]] 0.5 µM (+2.6) (137 in all, 26 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)
- Lower it: [[Dinaciclib (drug)]] 0.5 µM (-16.2, ⚠ toxic; transcription drop; cell-cycle shift); [[Niclosamide (olamine) (drug)]] 5 µM (-14.2, ⚠ toxic; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (-14.0, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (-12.9, ⚠ toxic; transcription drop; cell-cycle shift); [[Auranofin (drug)]] 5 µM (-10.1); [[Digitoxin (drug)]] 5 µM (-8.7, ⚠ toxic; transcription drop; cell-cycle shift); [[Ixazomib citrate (drug)]] 0.5 µM (-8.4); [[Ixazomib citrate (drug)]] 5 µM (-8.0, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (-7.4, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (-7.0, ⚠ cell-cycle shift); [[Abemaciclib (drug)]] 5 µM (-3.3); [[Brivudine (drug)]] 5 µM (-3.1); [[Bortezomib (drug)]] 0.5 µM (-2.9); [[Arbutin (drug)]] 5 µM (-2.7); [[Tucidinostat (drug)]] 5 µM (-2.6); [[Berbamine (drug)]] 5 µM (-2.6); [[Mebendazole (drug)]] 5 µM (-2.6); [[Retinoic acid (drug)]] 0.05 µM (-2.4) (155 in all, 37 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[NCI-H460 (line)]], [[C32 (line)]], [[PANC-1 (line)]], [[SW480 (line)]], [[NCI-H1792 (line)]], [[HOP62 (line)]], [[NCI-H1573 (line)]], [[A-172 (line)]]

## + arm (18)

| Gene | Projection | Name |
|---|---|---|
| [[TJAP1]] | 0.860 | tight junction associated protein 1 |
| [[NDUFAF1]] | 0.809 | NADH:ubiquinone oxidoreductase complex assembly factor 1 |
| [[HARBI1]] | 0.753 | harbinger transposase derived 1 |
| [[TSG101]] | 0.743 | tumor susceptibility 101 |
| [[ZSWIM3]] | 0.713 | zinc finger SWIM-type containing 3 |
| [[CYP20A1]] | 0.698 | cytochrome P450 family 20 subfamily A member 1 |
| [[TUT1]] | 0.694 | terminal uridylyl transferase 1, U6 snRNA-specific |
| [[CCDC22]] | 0.688 | CCC complex scaffolding subunit CCDC22 |
| [[CHMP4A]] | 0.676 | charged multivesicular body protein 4A |
| [[ZNF7]] | 0.674 | zinc finger protein 7 |
| [[KLHL12]] | 0.672 | kelch like family member 12 |
| [[RNF111]] | 0.664 | ring finger protein 111 |
| [[ZNF264]] | 0.659 | zinc finger protein 264 |
| [[PRPSAP2]] | 0.578 | phosphoribosyl pyrophosphate synthetase associated protein 2 |
| [[DET1]] | 0.567 | DET1 partner of COP1 E3 ubiquitin ligase |
| [[ITCH]] | 0.541 | itchy E3 ubiquitin protein ligase |
| [[ZNF76]] | 0.457 | zinc finger protein 76 |
| [[WDR89]] | 0.322 | WD repeat domain 89 |

## − arm (6)

| Gene | Projection | Name |
|---|---|---|
| [[TMEM97]] | -0.721 | transmembrane protein 97 |
| [[LDHB]] | -0.719 | lactate dehydrogenase B |
| [[PLPP2]] | -0.687 | phospholipid phosphatase 2 |
| [[ELOVL5]] | -0.686 | ELOVL fatty acid elongase 5 |
| [[HACD3]] | -0.655 | 3-hydroxyacyl-CoA dehydratase 3 |
| [[SCML1]] | -0.505 | Scm polycomb group protein like 1 |

## Data

- `graph/nodes.parquet` — module == 170; `graph/modules.parquet` — module == 170; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [169] (drug-dose × line)
