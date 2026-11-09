---
module: 96
type: "module"
n_genes: 48
n_plus: 48
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 096

*48 genes (single-armed) · [[Module 096.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 95), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Dinaciclib (drug)]] 5 µM (+7.0, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (+6.7, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+5.4, ⚠ toxic; transcription drop; cell-cycle shift); [[Homoharringtonine (drug)]] 5 µM (+5.2, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (+2.9, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (+2.7, ⚠ cell-cycle shift); [[Docetaxel (drug)]] 0.05 µM (+2.7, ⚠ transcription drop; cell-cycle shift); [[LY-2584702 (tosylate salt) (drug)]] 5 µM (+2.1, ⚠ toxic); [[XRK3F2 (drug)]] 0.5 µM (+2.0); [[Selinexor (drug)]] 5 µM (+1.8, ⚠ cell-cycle shift); [[9-ING-41 (drug)]] 0.5 µM (+1.6); [[Belumosudil (drug)]] 5 µM (+1.5); [[Homoharringtonine (drug)]] 0.05 µM (+1.5); [[Ipatasertib (drug)]] 0.5 µM (+1.4); [[Topotecan (hydrochloride) (drug)]] 0.05 µM (+1.4); [[Bimiralisib (drug)]] 0.5 µM (+1.4); [[venetoclax (drug)]] 0.05 µM (+1.3); [[Thymol (drug)]] 0.5 µM (+1.2); [[GSK1059615 (drug)]] 0.5 µM (+1.2) (28 in all, 14 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)
- Lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM (-3.6, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (-3.0, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (-2.4, ⚠ cell-cycle shift); [[Belinostat (drug)]] 0.5 µM (-2.0, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (-1.8, ⚠ cell-cycle shift); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (-1.8, ⚠ cell-cycle shift); [[Bosentan (hydrate) (drug)]] 0.5 µM (-1.6); [[Ribociclib (drug)]] 0.05 µM (-1.5, ⚠ unreliable plate only; position not correctable); [[Digitoxin (drug)]] 0.5 µM (-1.5, ⚠ cell-cycle shift); [[Verteporfin (drug)]] 5 µM (-1.5); [[Almonertinib (hydrochloride) (drug)]] 0.05 µM (-1.4); [[Brivudine (drug)]] 5 µM (-1.3); [[Doxycycline (monohydrate) (drug)]] 0.5 µM (-1.3); [[Entecavir (monohydrate) (drug)]] 0.5 µM (-1.2); [[Loperamide (hydrochloride) (drug)]] 0.5 µM (-1.2); [[Loperamide (hydrochloride) (drug)]] 5 µM (-1.2); [[Voriconazole (drug)]] 5 µM (-1.2); [[IQ 1 (drug)]] 0.05 µM (-1.1) (28 in all, 15 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[A498 (line)]], [[A-172 (line)]], [[PANC-1 (line)]], [[HEC-1-A (line)]], [[MIA PaCa-2 (line)]], [[NCI-H460 (line)]], [[SW480 (line)]], [[HOP62 (line)]]

*⚠ 1 of its 48 genes are in the vector space only through drug-doses that carry an alert (`embed/genes.parquet` evidence_flagged_only): their place here may reflect what those drug-doses did to the cells. They are marked in the tables of this note.*

## + arm (48)

| Gene | Projection | Name | Alert |
|---|---|---|---|
| [[WIZ]] | 0.844 | WIZ zinc finger |  |
| [[PIGO]] | 0.834 | phosphatidylinositol glycan anchor biosynthesis class O |  |
| [[SRSF6]] | 0.787 | serine and arginine rich splicing factor 6 |  |
| [[CELSR3]] | 0.781 | cadherin EGF LAG seven-pass G-type receptor 3 |  |
| [[NCDN]] | 0.758 | neurochondrin |  |
| [[WDR6]] | 0.733 | WD repeat domain 6 |  |
| [[SRRM2]] | 0.732 | serine/arginine repetitive matrix 2 |  |
| [[CNOT3]] | 0.730 | CCR4-NOT transcription complex subunit 3 |  |
| [[MED16]] | 0.729 | mediator complex subunit 16 |  |
| [[TAF1C]] | 0.728 | TATA-box binding protein associated factor, RNA polymerase I subunit C |  |
| [[ACP2]] | 0.722 | acid phosphatase 2, lysosomal |  |
| [[PLEKHG4]] | 0.714 | pleckstrin homology and RhoGEF domain containing G4 |  |
| [[UBA1]] | 0.710 | ubiquitin like modifier activating enzyme 1 |  |
| [[DXO]] | 0.708 | decapping exoribonuclease |  |
| [[ATXN7L2]] | 0.705 | ataxin 7 like 2 |  |
| [[ARFRP1]] | 0.701 | ARF related protein 1 |  |
| [[MBD6]] | 0.688 | methyl-CpG binding domain protein 6 |  |
| [[SDR39U1]] | 0.686 | short chain dehydrogenase/reductase family 39U member 1 |  |
| [[IDUA]] | 0.675 | alpha-L-iduronidase |  |
| [[OPLAH]] | 0.671 | 5-oxoprolinase, ATP-hydrolysing | ⚠ only flagged evidence |
| [[ZYX]] | 0.654 | zyxin |  |
| [[TFE3]] | 0.652 | transcription factor binding to IGHM enhancer 3 |  |
| [[DTX3]] | 0.644 | deltex E3 ubiquitin ligase 3 |  |
| [[ZNF628]] | 0.638 | zinc finger protein 628 |  |
| [[SPATA20]] | 0.630 | spermatogenesis associated 20 |  |
| [[CIC]] | 0.628 | capicua transcriptional repressor |  |
| [[BCL7B]] | 0.616 | BAF chromatin remodeling complex subunit BCL7B |  |
| [[VARS2]] | 0.584 | valyl-tRNA synthetase 2, mitochondrial |  |
| [[HYI]] | 0.577 | hydroxypyruvate isomerase (putative) |  |
| [[FASTK]] | 0.573 | Fas activated serine/threonine kinase |  |
| [[GLI4]] | 0.570 | GLI family zinc finger 4 |  |
| [[CREBZF]] | 0.553 | CREB/ATF bZIP transcription factor |  |
| [[DYNLL2]] | 0.550 | dynein light chain LC8-type 2 |  |
| [[AP1G2]] | 0.539 | adaptor related protein complex 1 subunit gamma 2 |  |
| [[TKFC]] | 0.538 | triokinase and FMN cyclase |  |
| [[UROS]] | 0.526 | uroporphyrinogen III synthase |  |
| [[RBM4]] | 0.523 | RNA binding motif protein 4 |  |
| [[GRIPAP1]] | 0.517 | GRIP1 associated protein 1 |  |
| [[LINC00641]] | 0.514 | long independently transcribed non-coding RNA 641 |  |
| [[RABGGTA]] | 0.510 | Rab geranylgeranyltransferase subunit alpha |  |
| [[POTEE]] | 0.484 | POTE ankyrin domain family member E |  |
| [[STX4]] | 0.475 | syntaxin 4 |  |
| [[MAP7D1]] | 0.467 | MAP7 domain containing 1 |  |
| [[CCDC9B]] | 0.464 | coiled-coil domain containing 9B |  |
| [[BPHL]] | 0.454 | biphenyl hydrolase like |  |
| [[ARPIN]] | 0.399 | actin related protein 2/3 complex inhibitor |  |
| [[LPIN3]] | 0.379 | lipin 3 |  |
| [[IFITM10]] | 0.306 | interferon induced transmembrane protein 10 |  |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 96; `graph/modules.parquet` — module == 96; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [95] (drug-dose × line)
