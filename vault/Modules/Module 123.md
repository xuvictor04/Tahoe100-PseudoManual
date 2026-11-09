---
module: 123
type: "module"
n_genes: 40
n_plus: 40
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: "TNF-alpha signaling via NF-kB"
label_source: "hallmark"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 123

*TNF-alpha signaling via NF-kB · 40 genes (single-armed) · [[Module 123.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

Label from the validation stage: **TNF-alpha signaling via NF-kB** (hallmark, q 1e-06; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | TNF-alpha signaling via NF-kB | hallmark | 9/40 | 18.0 | 1e-06 |
| + | TNF-alpha signaling via NF-kB | hallmark | 9/40 | 18.0 | 1e-06 |
| all | Signaling by Hippo | reactome | 3/40 | 56.5 | 0.009 |
| + | Signaling by Hippo | reactome | 3/40 | 56.5 | 0.009 |
| all | apoptosis | hallmark | 5/40 | 13.3 | 0.015 |
| + | apoptosis | hallmark | 5/40 | 13.3 | 0.015 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 122), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Homoharringtonine (drug)]] 5 µM (+16.9, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (+9.7, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (+8.6, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (+5.7, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (+5.7); [[Ouabain (Octahydrate) (drug)]] 5 µM (+4.1, ⚠ cell-cycle shift); [[TAK-901 (drug)]] 5 µM (+3.9, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 0.5 µM (+3.7, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 5 µM (+3.2, ⚠ toxic; transcription drop; cell-cycle shift); [[Homoharringtonine (drug)]] 0.05 µM (+3.0); [[Binimetinib (drug)]] 5 µM (+2.8); [[Trametinib (drug)]] 0.5 µM (+2.7); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM (+2.2); [[Binimetinib (drug)]] 0.5 µM (+2.1); [[Peretinoin (drug)]] 5 µM (+2.0); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM (+2.0); [[XRK3F2 (drug)]] 0.5 µM (+1.9); [[Peretinoin (drug)]] 0.5 µM (+1.8) (53 in all, 19 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)
- Lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM (-3.6, ⚠ cell-cycle shift); [[Bortezomib (drug)]] 0.05 µM (-2.8, ⚠ cell-cycle shift); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (-2.6, ⚠ cell-cycle shift); [[Ixazomib citrate (drug)]] 5 µM (-2.5, ⚠ cell-cycle shift); [[Epirubicin (hydrochloride) (drug)]] 5 µM (-2.1, ⚠ cell-cycle shift); [[Ixazomib citrate (drug)]] 0.5 µM (-1.7); [[GSK1059615 (drug)]] 5 µM (-1.6); [[Dabrafenib (drug)]] 5 µM (-1.4); [[Bortezomib (drug)]] 5 µM (-1.3, ⚠ toxic; cell-cycle shift); [[Cabozantinib (S-malate) (drug)]] 5 µM (-1.2); [[BAY1125976 (drug)]] 5 µM (-1.1); [[Fenofibrate (drug)]] 0.05 µM (-1.0); [[Gallic acid (drug)]] 0.05 µM (-1.0); [[ERK5-IN-2 (drug)]] 5 µM (-1.0) (15 in all, 7 with an alert ⚠; shown: the 10 strongest and the 4 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[NCI-H460 (line)]], [[A-172 (line)]], [[PANC-1 (line)]], [[HS-578T (line)]], [[A498 (line)]], [[HOP62 (line)]], [[J82 (line)]], [[C32 (line)]]

## Candidate new members

*Members not annotated to the set their arm is enriched for, ranked by mean cos to the annotated members (`validation/novel_members.csv`); ⚠ = a reason to doubt the gene's place (in the vector space only through flagged drug-doses), kept in its rank. 7 candidates, none with an alert.*

| # | Gene | Set | Mean cos |
|---|---|---|---|
| 1 | [[EDN1]] | Signaling by Hippo | +0.64 |
| 2 | [[AJUBA]] | Signaling by Hippo | +0.61 |
| 3 | [[TGIF2]] | Signaling by Hippo | +0.58 |
| 4 | [[FOSL2]] | Signaling by Hippo | +0.54 |
| 5 | [[ARL4A]] | TNF-alpha signaling via NF-kB | +0.52 |
| 6 | [[KRT80]] | Signaling by Hippo | +0.51 |
| 7 | [[NEDD9]] | TNF-alpha signaling via NF-kB | +0.50 |

## + arm (40)

| Gene | Projection | Name |
|---|---|---|
| [[RHOB]] | 0.786 | ras homolog family member B |
| [[KLF4]] | 0.762 | KLF transcription factor 4 |
| [[FOSL2]] | 0.747 | FOS like 2, AP-1 transcription factor subunit |
| [[ARL4A]] | 0.730 | ARF like GTPase 4A |
| [[RHOU]] | 0.728 | ras homolog family member U |
| [[JUND]] | 0.720 | JunD proto-oncogene, AP-1 transcription factor subunit |
| [[KLF2]] | 0.704 | KLF transcription factor 2 |
| [[DUSP8]] | 0.689 | dual specificity phosphatase 8 |
| [[KRTAP5-AS1]] | 0.673 | KRTAP5-1/KRTAP5-2 antisense RNA 1 |
| [[ZFP36L2]] | 0.671 | ZFP36 like 2 zinc finger CCCH-type |
| [[LMNA]] | 0.665 | lamin A/C |
| [[ARID5B]] | 0.660 | AT-rich interaction domain 5B |
| [[TXNIP]] | 0.659 | thioredoxin interacting protein |
| [[EDN1]] | 0.652 | endothelin 1 |
| [[IL18]] | 0.643 | interleukin 18 |
| [[ETS2]] | 0.643 | ETS proto-oncogene 2, transcription factor |
| [[AMOTL2]] | 0.640 | angiomotin like 2 |
| [[NEDD9]] | 0.629 | neural precursor cell expressed, developmentally down-regulated 9 |
| [[PTGER4]] | 0.618 | prostaglandin E receptor 4 |
| [[TUBB2B]] | 0.608 | tubulin beta 2B class IIb |
| [[TUBB2A]] | 0.598 | tubulin beta 2A class IIa |
| [[CKB]] | 0.598 | creatine kinase B |
| [[AJUBA]] | 0.596 | ajuba LIM protein |
| [[LATS2]] | 0.585 | large tumor suppressor kinase 2 |
| [[KRT80]] | 0.583 | keratin 80 |
| [[IRF2BP2]] | 0.572 | interferon regulatory factor 2 binding protein 2 |
| [[CITED2]] | 0.572 | Cbp/p300 interacting transactivator with ED-rich tail 2 |
| [[SERTAD2]] | 0.571 | SERTA domain containing 2 |
| [[RNF223]] | 0.527 | ring finger protein 223 |
| [[MT1G]] | 0.518 | metallothionein 1G |
| [[TGIF2]] | 0.518 | TGFB induced factor homeobox 2 |
| [[WWC1]] | 0.484 | WW and C2 domain containing 1 |
| [[OSR2]] | 0.442 | odd-skipped related transciption factor 2 |
| [[SYDE2]] | 0.434 | synapse defective Rho GTPase homolog 2 |
| [[YWHAH]] | 0.425 | tyrosine 3-monooxygenase/tryptophan 5-monooxygenase activation protein eta |
| [[FAM50A]] | 0.417 | family with sequence similarity 50 member A |
| [[KRT17]] | 0.401 | keratin 17 |
| [[FNIP2]] | 0.389 | folliculin interacting protein 2 |
| [[SHC2]] | 0.353 | SHC adaptor protein 2 |
| [[SH3RF2]] | 0.262 | SH3 domain containing ring finger 2 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 123; `graph/modules.parquet` — module == 123; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [122] (drug-dose × line)
