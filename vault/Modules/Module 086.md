---
module: 86
type: "module"
n_genes: 51
n_plus: 51
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: "cholesterol synthesis"
label_source: "control"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 086

*cholesterol synthesis · 51 genes (single-armed) · [[Module 086.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

Label from the validation stage: **cholesterol synthesis** (control, q 7e-52; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | cholesterol synthesis | control | 22/51 | 283 | 7e-52 |
| + | cholesterol synthesis | control | 22/51 | 283 | 7e-52 |
| + | Cholesterol biosynthesis | reactome | 20/51 | 227 | 1e-42 |
| all | Cholesterol biosynthesis | reactome | 20/51 | 227 | 1e-42 |
| all | cholesterol homeostasis | hallmark | 24/51 | 103 | 2e-40 |
| + | cholesterol homeostasis | hallmark | 24/51 | 103 | 2e-40 |
| + | Metabolism of steroids | reactome | 25/51 | 59.6 | 1e-35 |
| all | Metabolism of steroids | reactome | 25/51 | 59.6 | 1e-35 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 85), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Cepharanthine (drug)]] 5 µM (+11.4); [[Berbamine (drug)]] 5 µM (+10.8); [[Panobinostat (drug)]] 5 µM (+5.6, ⚠ cell-cycle shift); [[Entrectinib (drug)]] 5 µM (+4.9); [[Panobinostat (drug)]] 0.5 µM (+4.8, ⚠ cell-cycle shift); [[Niclosamide (olamine) (drug)]] 5 µM (+4.6, ⚠ toxic; cell-cycle shift); [[Belinostat (drug)]] 5 µM (+4.5, ⚠ cell-cycle shift); [[Almonertinib (mesylate) (drug)]] 5 µM (+4.2); [[Posaconazole (drug)]] 5 µM (+4.1); [[Berbamine (dihydrochloride) (drug)]] 5 µM (+4.0); [[Adagrasib (drug)]] 5 µM (+3.9); [[(S)-Crizotinib (drug)]] 5 µM (+3.8); [[Osimertinib (mesylate) (drug)]] 5 µM (+3.2); [[Terfenadine (drug)]] 5 µM (+3.2) (65 in all, 19 with an alert ⚠; shown: the 10 strongest and the 4 next strongest without an alert)
- Lower it: [[Homoharringtonine (drug)]] 0.05 µM (-3.4); [[Harringtonine (drug)]] 0.5 µM (-3.4, ⚠ cell-cycle shift); [[5-Azacytidine (drug)]] 5 µM (-3.1); [[Homoharringtonine (drug)]] 0.5 µM (-2.6, ⚠ cell-cycle shift); [[Quinestrol (drug)]] 5 µM (-2.5); [[Belumosudil (drug)]] 5 µM (-2.3); [[Harringtonine (drug)]] 0.05 µM (-2.3); [[Harringtonine (drug)]] 5 µM (-2.1, ⚠ cell-cycle shift); [[Temsirolimus (drug)]] 0.05 µM (-2.1); [[Asciminib (drug)]] 5 µM (-1.8); [[Temsirolimus (drug)]] 0.5 µM (-1.5); [[Ponatinib (drug)]] 0.5 µM (-1.5); [[Rapamycin (drug)]] 0.5 µM (-1.4) (42 in all, 12 with an alert ⚠; shown: the 10 strongest and the 3 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[HOP62 (line)]], [[A549 (line)]], [[LoVo (line)]], [[C-33 A (line)]], [[A498 (line)]], [[SNU-423 (line)]], [[HEC-1-A (line)]], [[NCI-H23 (line)]]

## Candidate new members

*Members not annotated to the set their arm is enriched for, ranked by mean cos to the annotated members (`validation/novel_members.csv`); ⚠ = a reason to doubt the gene's place (in the vector space only through flagged drug-doses), kept in its rank. 42 candidates, none with an alert; shown: the 15 strongest.*

| # | Gene | Set | Mean cos |
|---|---|---|---|
| 1 | [[HMGCR]] | Cholesterol biosynthesis via desmosterol (Bloch pathway) | +0.76 |
| 2 | [[MSMO1]] | Lanosterol biosynthesis | +0.75 |
| 3 | [[DHCR7]] | Lanosterol biosynthesis | +0.74 |
| 4 | [[SREBF2]] | Lanosterol biosynthesis | +0.72 |
| 5 | [[FDFT1]] | Zymostenol biosynthesis via lathosterol (Kandutsch-Russell pathway) | +0.72 |
| 6 | [[ACSS2]] | Activation of gene expression by SREBF (SREBP) | +0.71 |
| 7 | [[FDPS]] | Cholesterol biosynthesis via desmosterol (Bloch pathway) | +0.71 |
| 8 | [[EBP]] | Lanosterol biosynthesis | +0.71 |
| 9 | [[SCD]] | Lanosterol biosynthesis | +0.70 |
| 10 | [[IDI1]] | Cholesterol biosynthesis via desmosterol (Bloch pathway) | +0.69 |
| 11 | [[INSIG1]] | Lanosterol biosynthesis | +0.69 |
| 12 | [[CYP51A1]] | Lanosterol biosynthesis | +0.68 |
| 13 | [[MVD]] | Zymostenol biosynthesis via lathosterol (Kandutsch-Russell pathway) | +0.67 |
| 14 | [[ERG28]] | Cholesterol biosynthesis | +0.67 |
| 15 | [[HMGCS1]] | Cholesterol biosynthesis via desmosterol (Bloch pathway) | +0.67 |

## + arm (51)

| Gene | Projection | Name |
|---|---|---|
| [[HMGCR]] | 0.935 | 3-hydroxy-3-methylglutaryl-CoA reductase |
| [[DHCR7]] | 0.924 | 7-dehydrocholesterol reductase |
| [[FDFT1]] | 0.915 | farnesyl-diphosphate farnesyltransferase 1 |
| [[MSMO1]] | 0.905 | methylsterol monooxygenase 1 |
| [[FDPS]] | 0.886 | farnesyl diphosphate synthase |
| [[SCD]] | 0.880 | stearoyl-CoA desaturase |
| [[IDI1]] | 0.880 | isopentenyl-diphosphate delta isomerase 1 |
| [[HMGCS1]] | 0.866 | 3-hydroxy-3-methylglutaryl-CoA synthase 1 |
| [[ACSS2]] | 0.858 | acyl-CoA synthetase short chain family member 2 |
| [[MVD]] | 0.855 | mevalonate diphosphate decarboxylase |
| [[CYP51A1]] | 0.834 | cytochrome P450 family 51 subfamily A member 1 |
| [[SREBF2]] | 0.831 | sterol regulatory element binding transcription factor 2 |
| [[ACAT2]] | 0.820 | acetyl-CoA acetyltransferase 2 |
| [[ERG28]] | 0.809 | ergosterol biosynthesis 28 homolog |
| [[PCSK9]] | 0.805 | proprotein convertase subtilisin/kexin type 9 |
| [[EBP]] | 0.802 | EBP cholestenol delta-isomerase |
| [[STARD4]] | 0.794 | StAR related lipid transfer domain containing 4 |
| [[INSIG1]] | 0.791 | insulin induced gene 1 |
| [[SQLE]] | 0.788 | squalene epoxidase |
| [[SC5D]] | 0.759 | sterol-C5-desaturase |
| [[MMAB]] | 0.738 | metabolism of cobalamin associated B |
| [[FASN]] | 0.731 | fatty acid synthase |
| [[HSD17B7]] | 0.727 | hydroxysteroid 17-beta dehydrogenase 7 |
| [[DHCR24]] | 0.719 | 24-dehydrocholesterol reductase |
| [[MVK]] | 0.717 | mevalonate kinase |
| [[SNAI3-AS1]] | 0.716 | SNAI3 antisense RNA 1 |
| [[LDLR]] | 0.691 | low density lipoprotein receptor |
| [[HSD17B7P2]] | 0.690 | hydroxysteroid 17-beta dehydrogenase 7 pseudogene 2 |
| [[PNPLA3]] | 0.686 | patatin like domain 3, 1-acylglycerol-3-phosphate O-acyltransferase |
| [[LPIN1]] | 0.682 | lipin 1 |
| [[ACSL3]] | 0.681 | acyl-CoA synthetase long chain family member 3 |
| [[NSDHL]] | 0.670 | NAD(P) dependent 3-beta-hydroxysteroid dehydrogenase NSDHL |
| [[ADIPOR2]] | 0.668 | adiponectin receptor 2 |
| [[LSS]] | 0.662 | lanosterol synthase |
| [[PCYT2]] | 0.658 | phosphate cytidylyltransferase 2, ethanolamine |
| [[FADS1]] | 0.652 | fatty acid desaturase 1 |
| [[SREBF1]] | 0.648 | sterol regulatory element binding transcription factor 1 |
| [[FADS2]] | 0.642 | fatty acid desaturase 2 |
| [[DBI]] | 0.633 | diazepam binding inhibitor, acyl-CoA binding protein |
| [[SLC25A1]] | 0.622 | solute carrier family 25 member 1 |
| [[RDH11]] | 0.621 | retinol dehydrogenase 11 |
| [[OLMALINC]] | 0.614 | oligodendrocyte maturation-associated long intergenic non-coding RNA |
| [[LIPG]] | 0.610 | lipase G, endothelial type |
| [[TMEM135]] | 0.543 | transmembrane protein 135 |
| [[PGD]] | 0.523 | phosphogluconate dehydrogenase |
| [[CLCN6]] | 0.515 | Cl-/H+ antiporter 6 |
| [[TKT]] | 0.510 | transketolase |
| [[HSD17B12]] | 0.507 | hydroxysteroid 17-beta dehydrogenase 12 |
| [[GSK3B]] | 0.492 | glycogen synthase kinase 3 beta |
| [[TMEM53]] | 0.481 | transmembrane protein 53 |
| [[LINC02432]] | 0.408 | long independently transcribed non-coding RNA 2432 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 86; `graph/modules.parquet` — module == 86; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [85] (drug-dose × line)
