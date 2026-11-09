---
module: 158
type: "module"
n_genes: 27
n_plus: 27
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.4063347280025482
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 158

*27 genes (single-armed) · [[Module 158.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | Tetrahydrobiopterin (BH4) synthesis, recycling, salvage and regulation | reactome | 2/27 | 112 | 0.048 |
| + | Tetrahydrobiopterin (BH4) synthesis, recycling, salvage and regulation | reactome | 2/27 | 112 | 0.048 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 157), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Homoharringtonine (drug)]] 5 µM (+16.2, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (+9.2, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (+8.0, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (+5.4); [[Dinaciclib (drug)]] 0.05 µM (+5.3, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (+5.0, ⚠ toxic; transcription drop; cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (+4.7, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (+4.5, ⚠ toxic; transcription drop; cell-cycle shift); [[Auranofin (drug)]] 5 µM (+4.0); [[Tucidinostat (drug)]] 0.5 µM (+3.6, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.05 µM (+2.3); [[Harringtonine (drug)]] 0.05 µM (+2.1); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+1.6); [[vincristine (drug)]] 0.5 µM (+1.5); [[Belzutifan (drug)]] 5 µM (+1.5); [[Peretinoin (drug)]] 0.5 µM (+1.3); [[Peretinoin (drug)]] 5 µM (+1.3); [[Ipatasertib (drug)]] 0.5 µM (+1.3) (49 in all, 32 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)
- Lower it: [[Trametinib (drug)]] 5 µM (-4.2, ⚠ cell-cycle shift); [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM (-3.6); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM (-3.5); [[Trametinib (drug)]] 0.5 µM (-3.5); [[Trametinib (drug)]] 0.05 µM (-3.1); [[Binimetinib (drug)]] 0.5 µM (-3.1); [[Binimetinib (drug)]] 5 µM (-2.9); [[Cobimetinib (drug)]] 5 µM (-2.9); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM (-2.8); [[RMC-6236 (drug)]] 5 µM (-2.3); [[Cobimetinib (drug)]] 0.5 µM (-2.3) (34 in all, 4 with an alert ⚠; shown: the 10 strongest and the 1 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[NCI-H460 (line)]], [[HOP62 (line)]], [[AsPC-1 (line)]], [[A-172 (line)]], [[NCI-H1573 (line)]], [[HS-578T (line)]], [[A498 (line)]], [[LOX-IMVI (line)]]

## + arm (27)

| Gene | Projection | Name |
|---|---|---|
| [[LINC00460]] | 0.787 | long independently transcribed non-coding RNA 460 |
| [[PHLDA1]] | 0.786 | pleckstrin homology like domain family A member 1 |
| [[BCAN-AS1]] | 0.781 | BCAN antisense RNA 1 |
| [[FOSL1]] | 0.781 | FOS like 1, AP-1 transcription factor subunit |
| [[CD163L1]] | 0.772 | CD163 molecule like 1 |
| [[BCAN-AS2]] | 0.769 | BCAN antisense RNA 2 |
| [[PRKG2-AS1]] | 0.762 | PRKG2 antisense RNA 1 |
| [[ICAM2]] | 0.759 | intercellular adhesion molecule 2 |
| [[ZNF697]] | 0.750 | zinc finger protein 697 |
| [[CD22]] | 0.740 | CD22 molecule |
| [[BCL10]] | 0.719 | BCL10 immune signaling adaptor |
| [[SFR1]] | 0.705 | SWI5 dependent homologous recombination repair protein 1 |
| [[SLC45A3]] | 0.704 | solute carrier family 45 member 3 |
| [[GOLT1A]] | 0.697 | golgi transport 1A |
| [[ARL14]] | 0.678 | ARF like GTPase 14 |
| [[RABL6]] | -0.643 | RAB, member RAS oncogene family like 6 |
| [[DIAPH2-AS1]] | 0.637 | DIAPH2 antisense RNA 1 |
| [[ZSWIM4]] | 0.635 | zinc finger SWIM-type containing 4 |
| [[ALOXE3]] | 0.624 | arachidonate epidermal lipoxygenase 3 |
| [[GOLGA7B]] | 0.613 | golgin A7 family member B |
| [[NOS3]] | 0.594 | nitric oxide synthase 3 |
| [[ODC1]] | 0.581 | ornithine decarboxylase 1 |
| [[MAGEB2]] | 0.553 | MAGE family member B2 |
| [[PRKG2]] | 0.537 | protein kinase cGMP-dependent 2 |
| [[FBXO41]] | 0.532 | F-box protein 41 |
| [[MAGEA4]] | 0.399 | MAGE family member A4 |
| [[AMN1]] | 0.326 | antagonist of mitotic exit network 1 homolog |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 158; `graph/modules.parquet` — module == 158; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [157] (drug-dose × line)
