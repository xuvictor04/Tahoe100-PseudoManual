---
module: 175
type: "module"
n_genes: 23
n_plus: 23
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.35303857922554016
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 175

*23 genes (single-armed) · [[Module 175.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 174), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Ponatinib (drug)]] 5 µM (+2.6); [[Trametinib (drug)]] 5 µM (+1.9, ⚠ cell-cycle shift); [[Ponatinib (drug)]] 0.5 µM (+1.7); [[Cabozantinib (S-malate) (drug)]] 5 µM (+1.7); [[Anethole trithione (drug)]] 5 µM (+1.6, ⚠ cell-cycle shift); [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM (+1.5); [[Ralimetinib dimesylate (drug)]] 0.05 µM (+1.5, ⚠ unreliable plate only); [[Radotinib (drug)]] 5 µM (+1.3); [[Clobetasol propionate (drug)]] 0.5 µM (+1.3); [[Trametinib (drug)]] 0.05 µM (+1.3); [[Verteporfin (drug)]] 5 µM (+1.3); [[Cobimetinib (drug)]] 5 µM (+1.2); [[Afatinib (drug)]] 5 µM (+1.1) (19 in all, 3 with an alert ⚠; shown: the 10 strongest and the 3 next strongest without an alert)
- Lower it: [[Homoharringtonine (drug)]] 5 µM (-12.0, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-7.8, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (-7.7, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 5 µM (-7.0, ⚠ toxic; transcription drop; cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-6.7, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (-5.2, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 0.5 µM (-5.2, ⚠ cell-cycle shift); [[Auranofin (drug)]] 5 µM (-5.1); [[Niclosamide (olamine) (drug)]] 5 µM (-4.1, ⚠ toxic; cell-cycle shift); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (-4.0); [[Ixazomib citrate (drug)]] 0.5 µM (-3.2); [[PH-797804 (drug)]] 5 µM (-2.3); [[9-ING-41 (drug)]] 0.5 µM (-1.5); [[Peretinoin (drug)]] 0.5 µM (-1.4); [[Mebendazole (drug)]] 5 µM (-1.4); [[Peretinoin (drug)]] 5 µM (-1.2); [[Homoharringtonine (drug)]] 0.05 µM (-1.2); [[Peretinoin (drug)]] 0.05 µM (-1.2) (38 in all, 24 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[PANC-1 (line)]], [[NCI-H460 (line)]], [[HOP62 (line)]], [[A-172 (line)]], [[SW480 (line)]], [[MIA PaCa-2 (line)]], [[LOX-IMVI (line)]], [[HS-578T (line)]]

## + arm (23)

| Gene | Projection | Name |
|---|---|---|
| [[ABCB10]] | 0.834 | ATP binding cassette subfamily B member 10 |
| [[PRMT7]] | 0.777 | protein arginine methyltransferase 7 |
| [[ALG6]] | 0.775 | ALG6 alpha-1,3-glucosyltransferase |
| [[GK5]] | 0.754 | glycerol kinase 5 |
| [[DDHD2]] | 0.753 | DDHD domain containing 2 |
| [[WHAMMP1]] | 0.723 | WHAMM pseudogene 1 |
| [[PCCB]] | 0.701 | propionyl-CoA carboxylase subunit beta |
| [[ZNF25]] | 0.696 | zinc finger protein 25 |
| [[RWDD4]] | 0.677 | RWD domain containing 4 |
| [[ADNP2]] | -0.676 | ADNP homeobox 2 |
| [[ANKRD36B]] | 0.673 | ankyrin repeat domain 36B |
| [[BIVM]] | 0.669 | basic, immunoglobulin-like variable motif containing |
| [[ATPAF1]] | 0.669 | ATP synthase mitochondrial F1 complex assembly factor 1 |
| [[ZNF449]] | 0.637 | zinc finger protein 449 |
| [[ATXN1]] | -0.606 | ataxin 1 |
| [[PGAP2]] | 0.582 | post-GPI attachment to proteins 2 |
| [[KATNAL1]] | 0.560 | katanin catalytic subunit A1 like 1 |
| [[ZNF333]] | 0.543 | zinc finger protein 333 |
| [[ANKRD36]] | 0.529 | ankyrin repeat domain 36 |
| [[C3orf33]] | 0.502 | mitochondrial inner membrane subdomain organizer 1 |
| [[TMEM143]] | 0.477 | transmembrane protein 143 |
| [[ANKRD36C]] | 0.144 | ankyrin repeat domain 36C |
| [[FAM161A]] | 0.111 | FAM161 centrosomal protein A |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 175; `graph/modules.parquet` — module == 175; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [174] (drug-dose × line)
