---
module: 93
type: "module"
n_genes: 49
n_plus: 49
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: "TNF-alpha signaling via NF-kB"
label_source: "hallmark"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 093

*TNF-alpha signaling via NF-kB · 49 genes (single-armed) · [[Module 093.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

Label from the validation stage: **TNF-alpha signaling via NF-kB** (hallmark, q 0.013; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | TNF-alpha signaling via NF-kB | hallmark | 6/49 | 9.82 | 0.013 |
| + | TNF-alpha signaling via NF-kB | hallmark | 6/49 | 9.82 | 0.013 |
| all | UV response up | hallmark | 5/49 | 10.5 | 0.040 |
| + | UV response up | hallmark | 5/49 | 10.5 | 0.040 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 92), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Homoharringtonine (drug)]] 5 µM (+16.6, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (+12.7, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (+10.1, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (+7.8, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (+7.6, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (+7.1, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (+6.8, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (+5.2, ⚠ cell-cycle shift); [[Epirubicin (hydrochloride) (drug)]] 5 µM (+4.8, ⚠ cell-cycle shift); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (+4.8, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (+4.7); [[Auranofin (drug)]] 5 µM (+4.6); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+3.6); [[HI-TOPK-032 (drug)]] 5 µM (+2.5); [[Ixazomib citrate (drug)]] 0.5 µM (+2.4); [[Bortezomib (drug)]] 0.5 µM (+2.1); [[PF-06260933 (drug)]] 5 µM (+2.1); [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM (+1.7); [[Clopidogrel (drug)]] 0.05 µM (+1.6); [[Artemether (drug)]] 0.05 µM (+1.6) (83 in all, 30 with an alert ⚠; shown: the 10 strongest and the 10 next strongest without an alert)
- Lower it: [[Ponatinib (drug)]] 5 µM (-2.3); [[Clobetasol propionate (drug)]] 0.5 µM (-1.8); [[Cabozantinib (S-malate) (drug)]] 5 µM (-1.8); [[Loperamide (hydrochloride) (drug)]] 0.5 µM (-1.8); [[Phenylephrine (hydrochloride) (drug)]] 0.5 µM (-1.7); [[Vortioxetine (drug)]] 0.5 µM (-1.7); [[Carbamazepine (drug)]] 0.5 µM (-1.7); [[Cabozantinib (S-malate) (drug)]] 0.05 µM (-1.6); [[Ponatinib (drug)]] 0.5 µM (-1.6); [[Sunitinib (drug)]] 5 µM (-1.5, ⚠ toxic); [[Lonafarnib (drug)]] 0.05 µM (-1.5) (51 in all, 2 with an alert ⚠; shown: the 10 strongest and the 1 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[NCI-H460 (line)]], [[SW480 (line)]], [[AsPC-1 (line)]], [[HOP62 (line)]], [[LoVo (line)]], [[PANC-1 (line)]], [[LOX-IMVI (line)]], [[SW1417 (line)]]

## + arm (49)

| Gene | Projection | Name |
|---|---|---|
| [[FAM222A]] | 0.843 | family with sequence similarity 222 member A |
| [[FAM53C]] | 0.843 | family with sequence similarity 53 member C |
| [[GTF2B]] | 0.777 | general transcription factor IIB |
| [[SLC9A1]] | 0.774 | solute carrier family 9 member A1 |
| [[TENT5C]] | 0.772 | terminal nucleotidyltransferase 5C |
| [[IFRD1]] | 0.762 | interferon related developmental regulator 1 |
| [[KLHL15]] | 0.749 | kelch like family member 15 |
| [[HEXIM1]] | 0.749 | HEXIM P-TEFb complex subunit 1 |
| [[POR]] | 0.747 | cytochrome p450 oxidoreductase |
| [[LGMN]] | 0.747 | legumain |
| [[TEX14]] | 0.732 | testis expressed 14, intercellular bridge forming factor |
| [[WDR47]] | 0.732 | WD repeat domain 47 |
| [[LINC00910]] | 0.723 | long independently transcribed non-coding RNA 910 |
| [[HAP1]] | 0.715 | huntingtin associated protein 1 |
| [[POLR2A]] | 0.707 | RNA polymerase II subunit A |
| [[IQCN]] | 0.702 | IQ motif containing N |
| [[GCH1]] | 0.691 | GTP cyclohydrolase 1 |
| [[SNAI1]] | 0.690 | snail family transcriptional repressor 1 |
| [[TLE4]] | 0.685 | TLE family member 4, transcriptional corepressor |
| [[DALRD3]] | 0.682 | DALR anticodon binding domain containing 3 |
| [[PIK3R3]] | 0.660 | phosphoinositide-3-kinase regulatory subunit 3 |
| [[CHCHD7]] | 0.658 | coiled-coil-helix-coiled-coil-helix domain containing 7 |
| [[BRD2]] | 0.653 | bromodomain containing 2 |
| [[ARIH1]] | 0.650 | ariadne RBR E3 ubiquitin protein ligase 1 |
| [[SPSB2]] | 0.646 | splA/ryanodine receptor domain and SOCS box containing 2 |
| [[HSPA2]] | 0.645 | heat shock protein family A (Hsp70) member 2 |
| [[TUBB3]] | 0.634 | tubulin beta 3 class III |
| [[ATF3]] | 0.619 | activating transcription factor 3 |
| [[BZW2]] | 0.594 | basic leucine zipper and W2 domains 2 |
| [[TNFSF9]] | 0.594 | TNF superfamily member 9 |
| [[TOB2]] | 0.592 | transducer of ERBB2, 2 |
| [[NXF1]] | 0.592 | nuclear RNA export factor 1 |
| [[UBE2D1]] | 0.582 | ubiquitin conjugating enzyme E2 D1 |
| [[ABHD5]] | 0.574 | abhydrolase domain containing 5, lysophosphatidic acid acyltransferase |
| [[GSTM3]] | 0.570 | glutathione S-transferase mu 3 |
| [[SKP1]] | 0.554 | S-phase kinase associated protein 1 |
| [[SLC16A1]] | 0.535 | solute carrier family 16 member 1 |
| [[RND3]] | 0.531 | Rho family GTPase 3 |
| [[HS6ST1]] | 0.506 | heparan sulfate 6-O-sulfotransferase 1 |
| [[ABHD17B]] | 0.497 | abhydrolase domain containing 17B, depalmitoylase |
| [[BPGM]] | 0.495 | bisphosphoglycerate mutase |
| [[JUN]] | 0.492 | Jun proto-oncogene, AP-1 transcription factor subunit |
| [[FUS]] | 0.482 | FUS DNA/RNA binding protein |
| [[SRSF7]] | 0.473 | serine and arginine rich splicing factor 7 |
| [[PPP1R15A]] | 0.451 | protein phosphatase 1 regulatory subunit 15A |
| [[BTD]] | 0.449 | biotinidase |
| [[CRISPLD2]] | 0.433 | cysteine rich secretory protein LCCL domain containing 2 |
| [[UBAP2]] | 0.429 | ubiquitin associated protein 2 |
| [[SQSTM1]] | 0.336 | sequestosome 1 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 93; `graph/modules.parquet` — module == 93; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [92] (drug-dose × line)
