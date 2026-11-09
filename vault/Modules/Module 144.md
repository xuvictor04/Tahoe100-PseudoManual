---
module: 144
type: "module"
n_genes: 32
n_plus: 32
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.2982034981250763
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 144

*32 genes (single-armed) · [[Module 144.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 143), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM (+4.3, ⚠ cell-cycle shift); [[TAK-901 (drug)]] 5 µM (+2.7, ⚠ cell-cycle shift); [[PF-06260933 (drug)]] 5 µM (+2.4); [[Cobimetinib (drug)]] 5 µM (+1.9); [[Roxadustat (drug)]] 5 µM (+1.7); [[Fumaric acid (drug)]] 5 µM (+1.2); [[Harringtonine (drug)]] 0.05 µM (+1.2); [[Epirubicin (hydrochloride) (drug)]] 5 µM (+1.2, ⚠ cell-cycle shift); [[Artesunate (drug)]] 5 µM (+1.1, ⚠ cell-cycle shift); [[Ponatinib (drug)]] 0.5 µM (+1.1); [[Homoharringtonine (drug)]] 0.05 µM (+1.1); [[Verteporfin (drug)]] 5 µM (+1.0); [[Entrectinib (drug)]] 5 µM (+1.0) (14 in all, 5 with an alert ⚠; shown: the 10 strongest and the 3 next strongest without an alert)
- Lower it: [[Dinaciclib (drug)]] 5 µM (-10.4, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (-10.1, ⚠ toxic; transcription drop; cell-cycle shift); [[Niclosamide (olamine) (drug)]] 5 µM (-8.9, ⚠ toxic; cell-cycle shift); [[Panobinostat (drug)]] 5 µM (-8.4, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 5 µM (-7.8, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (-7.8, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (-6.7, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-6.3, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (-6.1, ⚠ toxic; transcription drop; cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-5.5, ⚠ cell-cycle shift); [[Auranofin (drug)]] 5 µM (-3.7); [[Ixazomib citrate (drug)]] 0.5 µM (-3.1); [[Belumosudil (drug)]] 5 µM (-2.2); [[Tucidinostat (drug)]] 5 µM (-2.0); [[5-Azacytidine (drug)]] 5 µM (-1.8); [[Vinblastine (sulfate) (drug)]] 0.5 µM (-1.7); [[Peretinoin (drug)]] 0.5 µM (-1.6); [[Retinoic acid (drug)]] 0.05 µM (-1.5); [[Brivudine (drug)]] 5 µM (-1.5); [[Peretinoin (drug)]] 5 µM (-1.4) (49 in all, 28 with an alert ⚠; shown: the 10 strongest and the 10 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[C32 (line)]], [[NCI-H1792 (line)]], [[SNU-423 (line)]], [[HCT15 (line)]], [[NCI-H460 (line)]], [[LOX-IMVI (line)]], [[HOP62 (line)]], [[SK-MEL-2 (line)]]

## + arm (32)

| Gene | Projection | Name |
|---|---|---|
| [[IPMK]] | 0.829 | inositol polyphosphate multikinase |
| [[FUT11]] | 0.785 | protein O-fucosyltransferase 4 |
| [[C4orf47]] | 0.784 | cilia and flagella associated protein 96 |
| [[RSBN1]] | 0.769 | round spermatid basic protein 1 |
| [[ZNF654]] | 0.760 | zinc finger protein 654 |
| [[KDM2A]] | 0.732 | lysine demethylase 2A |
| [[EGLN1]] | 0.726 | egl-9 family hypoxia inducible factor 1 |
| [[ZBTB25]] | 0.715 | zinc finger and BTB domain containing 25 |
| [[AKAP10]] | 0.696 | A-kinase anchoring protein 10 |
| [[DIPK2A]] | 0.696 | divergent protein kinase domain 2A |
| [[ZSWIM5]] | 0.683 | zinc finger SWIM-type containing 5 |
| [[AK4]] | 0.670 | adenylate kinase 4 |
| [[WSB1]] | 0.654 | WD repeat and SOCS box containing 1 |
| [[PIAS2]] | 0.649 | protein inhibitor of activated STAT 2 |
| [[GPR146]] | 0.646 | G protein-coupled receptor 146 |
| [[SLC35E3]] | 0.633 | solute carrier family 35 member E3 |
| [[NOL3]] | 0.627 | nucleolar protein 3 |
| [[NOG]] | 0.627 | noggin |
| [[BCKDHA]] | 0.597 | branched chain keto acid dehydrogenase E1 subunit alpha |
| [[NR2F2]] | 0.592 | nuclear receptor subfamily 2 group F member 2 |
| [[NR2F2-AS1]] | 0.592 | NR2F2 antisense RNA 1 |
| [[DHX32]] | 0.580 | DEAH-box helicase 32 (putative) |
| [[CCL28]] | 0.563 | C-C motif chemokine ligand 28 |
| [[SPRY1]] | 0.561 | sprouty RTK signaling antagonist 1 |
| [[KDM4C]] | 0.556 | lysine demethylase 4C |
| [[MAML1]] | 0.552 | mastermind like transcriptional coactivator 1 |
| [[RUNDC1]] | 0.551 | RUN domain containing 1 |
| [[FAM216A]] | 0.539 | family with sequence similarity 216 member A |
| [[EMSY]] | 0.522 | EMSY transcriptional repressor, BRCA2 interacting |
| [[DELE1]] | -0.512 | DAP3 binding cell death enhancer 1 |
| [[PRELID2]] | 0.493 | PRELI domain containing 2 |
| [[TUBGCP5]] | 0.400 | tubulin gamma complex component 5 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 144; `graph/modules.parquet` — module == 144; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [143] (drug-dose × line)
