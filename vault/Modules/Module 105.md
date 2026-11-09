---
module: 105
type: "module"
n_genes: 44
n_plus: 44
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.38270872831344604
label: "Late Phase of HIV Life Cycle"
label_source: "reactome"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 105

*Late Phase of HIV Life Cycle · 44 genes (single-armed) · [[Module 105.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

Label from the validation stage: **Late Phase of HIV Life Cycle** (reactome, q 0.017; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | Late Phase of HIV Life Cycle | reactome | 5/44 | 12.8 | 0.017 |
| + | Late Phase of HIV Life Cycle | reactome | 5/44 | 12.8 | 0.017 |
| all | HIV Life Cycle | reactome | 5/44 | 11.8 | 0.024 |
| + | HIV Life Cycle | reactome | 5/44 | 11.8 | 0.024 |
| all | IPs transport between nucleus and cytosol | reactome | 3/44 | 34.3 | 0.033 |
| all | IP6 and IP7 transport between cytosol and nucleus | reactome | 3/44 | 34.3 | 0.033 |
| + | IP3 and IP4 transport between cytosol and nucleus | reactome | 3/44 | 34.3 | 0.033 |
| all | IP3 and IP4 transport between cytosol and nucleus | reactome | 3/44 | 34.3 | 0.033 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 104), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Auranofin (drug)]] 5 µM (+3.0); [[TAK-901 (drug)]] 5 µM (+2.6, ⚠ cell-cycle shift); [[PF-06260933 (drug)]] 5 µM (+2.6); [[c-Kit-IN-1 (drug)]] 0.05 µM (+2.1, ⚠ unreliable plate only); [[Roxadustat (drug)]] 5 µM (+1.7); [[Abemaciclib (drug)]] 0.5 µM (+1.5); [[Abemaciclib (drug)]] 5 µM (+1.4); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (+1.3, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (+1.3, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (+1.3); [[Verteporfin (drug)]] 5 µM (+1.3); [[Tomivosertib (drug)]] 5 µM (+1.2); [[PH-797804 (drug)]] 5 µM (+1.1); [[EX229 (drug)]] 0.05 µM (+1.1) (19 in all, 8 with an alert ⚠; shown: the 10 strongest and the 4 next strongest without an alert)
- Lower it: [[Homoharringtonine (drug)]] 5 µM (-10.1, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-8.0, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (-6.7, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (-6.4, ⚠ toxic; transcription drop; cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-5.8, ⚠ cell-cycle shift); [[Niclosamide (olamine) (drug)]] 5 µM (-5.4, ⚠ toxic; cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (-2.7, ⚠ toxic; transcription drop; cell-cycle shift); [[Belumosudil (drug)]] 5 µM (-2.6); [[Retinoic acid (drug)]] 0.05 µM (-2.3); [[Harringtonine (drug)]] 0.5 µM (-2.0, ⚠ cell-cycle shift); [[Berbamine (drug)]] 0.05 µM (-1.8); [[Temsirolimus (drug)]] 0.05 µM (-1.7); [[Palmatine (chloride) (drug)]] 0.05 µM (-1.5); [[Larotrectinib (drug)]] 0.05 µM (-1.4); [[Clobetasol propionate (drug)]] 0.05 µM (-1.3); [[Trametinib (drug)]] 0.5 µM (-1.3); [[Pralsetinib (drug)]] 5 µM (-1.3); [[Gallic acid (hydrate) (drug)]] 0.05 µM (-1.3) (37 in all, 15 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[C32 (line)]], [[C-33 A (line)]], [[SK-MEL-2 (line)]], [[HEC-1-A (line)]], [[A-172 (line)]], [[SNU-423 (line)]], [[RPMI-7951 (line)]], [[PANC-1 (line)]]

## + arm (44)

| Gene | Projection | Name |
|---|---|---|
| [[POM121]] | 0.883 | POM121 transmembrane nucleoporin |
| [[FAM210A]] | 0.881 | mitochondrial inner membrane structural 1 |
| [[POM121C]] | 0.872 | POM121 transmembrane nucleoporin C |
| [[PRKRIP1]] | 0.829 | PRKR interacting protein 1 |
| [[CRYBB2P1-1]] | 0.816 | — |
| [[AK2]] | 0.793 | adenylate kinase 2 |
| [[RNMT]] | 0.775 | RNA guanine-7 methyltransferase |
| [[LINC03009-1]] | 0.769 | long independently transcribed non-coding RNA 3009 |
| [[DHRS13]] | 0.762 | dehydrogenase/reductase 13 |
| [[MAP2K1]] | 0.754 | mitogen-activated protein kinase kinase 1 |
| [[SFXN1]] | 0.738 | sideroflexin 1 |
| [[EFCAB3P1]] | 0.704 | EFCAB3 pseudogene 1 |
| [[NUP58]] | 0.704 | nucleoporin 58 |
| [[CPLANE1]] | -0.702 | ciliogenesis and planar polarity effector complex subunit 1 |
| [[SEC31B]] | 0.674 | SEC31 homolog B, COPII component |
| [[BTAF1]] | 0.670 | B-TFIID TATA-box binding protein associated factor 1 |
| [[LONP1]] | 0.662 | lon peptidase 1, mitochondrial |
| [[ISCA1]] | 0.658 | iron-sulfur cluster assembly 1 |
| [[SLC2A1-DT]] | 0.653 | SLC2A1 divergent transcript |
| [[ZNF215]] | 0.651 | zinc finger protein 215 |
| [[FNTB]] | 0.641 | farnesyltransferase, CAAX box, subunit beta |
| [[CTDP1]] | 0.641 | CTD phosphatase 1 |
| [[BRK1]] | 0.640 | BRICK1 subunit of SCAR/WAVE actin nucleating complex |
| [[TMEM14B]] | 0.640 | transmembrane protein 14B |
| [[TCAF2]] | 0.638 | TRPM8 channel associated factor 2 |
| [[TNFRSF10D]] | 0.624 | TNF receptor superfamily member 10d |
| [[CRYBB2P1]] | 0.622 | crystallin beta B2 pseudogene 1 |
| [[PPME1]] | 0.595 | protein phosphatase methylesterase 1 |
| [[SYCP2L]] | 0.571 | synaptonemal complex protein 2 like |
| [[ANO7]] | 0.555 | anoctamin 7 |
| [[TMEM41A]] | 0.548 | transmembrane protein 41A |
| [[FASTKD1]] | 0.547 | FASTK mitochondrial RNA regulator 1 |
| [[TACC2]] | -0.543 | transforming acidic coiled-coil containing protein 2 |
| [[LINC00887]] | 0.538 | long independently transcribed non-coding RNA 887 |
| [[GRPEL1]] | 0.520 | GrpE like 1, mitochondrial |
| [[KDM4A-AS1]] | 0.513 | KDM4A antisense RNA 1 |
| [[WRAP53]] | 0.495 | WD repeat containing antisense to TP53 |
| [[LINC02649]] | 0.493 | long independently transcribed non-coding RNA 2649 |
| [[KDM2B-DT]] | 0.493 | KDM2B divergent transcript |
| [[UPRT]] | 0.485 | uracil phosphoribosyltransferase homolog |
| [[SMYD2]] | 0.475 | SET and MYND domain containing 2 |
| [[ZNF143]] | 0.438 | zinc finger protein 143 |
| [[VPS26C]] | 0.397 | VPS26 endosomal protein sorting factor C |
| [[EPIC1]] | 0.355 | epigenetically induced MYC interacting lncRNA 1 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 105; `graph/modules.parquet` — module == 105; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [104] (drug-dose × line)
