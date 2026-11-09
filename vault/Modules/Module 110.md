---
module: 110
type: "module"
n_genes: 43
n_plus: 43
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.282824844121933
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 110

*43 genes (single-armed) · [[Module 110.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 109), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Daptomycin (drug)]] 5 µM (+2.6, ⚠ unreliable plate only); [[Auranofin (drug)]] 5 µM (+2.2); [[Vinblastine (sulfate) (drug)]] 5 µM (+2.2); [[Peretinoin (drug)]] 5 µM (+2.2); [[Daptomycin (drug)]] 0.5 µM (+2.0, ⚠ unreliable plate only); [[Idarubicin (hydrochloride) (drug)]] 5 µM (+1.9, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (+1.9, ⚠ toxic; transcription drop; cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (+1.9); [[Vinblastine (sulfate) (drug)]] 0.5 µM (+1.9); [[vincristine (drug)]] 0.5 µM (+1.7); [[Peretinoin (drug)]] 0.5 µM (+1.5); [[vincristine (drug)]] 5 µM (+1.5); [[Rapamycin (drug)]] 5 µM (+1.3); [[Pitavastatin (Calcium) (drug)]] 0.5 µM (+1.2) (21 in all, 7 with an alert ⚠; shown: the 10 strongest and the 4 next strongest without an alert)
- Lower it: [[Homoharringtonine (drug)]] 5 µM (-5.7, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (-4.6, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (-4.2, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (-3.7, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-3.6, ⚠ cell-cycle shift); [[Trametinib (drug)]] 5 µM (-3.3, ⚠ cell-cycle shift); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM (-3.1); [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM (-3.1); [[Trametinib (drug)]] 0.5 µM (-3.1); [[Binimetinib (drug)]] 0.5 µM (-2.8); [[Binimetinib (drug)]] 5 µM (-2.6); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM (-2.5); [[Elimusertib hydrochloride (drug)]] 0.05 µM (-2.3); [[Binimetinib (drug)]] 0.05 µM (-2.3); [[Cobimetinib (drug)]] 5 µM (-2.1); [[Trametinib (drug)]] 0.05 µM (-1.8) (40 in all, 15 with an alert ⚠; shown: the 10 strongest and the 6 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[RKO (line)]], [[MIA PaCa-2 (line)]], [[LOX-IMVI (line)]], [[HOP62 (line)]], [[NCI-H23 (line)]], [[PANC-1 (line)]], [[SK-MEL-2 (line)]], [[SW480 (line)]]

## + arm (43)

| Gene | Projection | Name |
|---|---|---|
| [[CORO2B]] | 0.909 | coronin 2B |
| [[PNP]] | 0.802 | purine nucleoside phosphorylase |
| [[ARHGAP22]] | 0.775 | Rho GTPase activating protein 22 |
| [[LRRC8C]] | 0.762 | leucine rich repeat containing 8 VRAC subunit C |
| [[ZEB1]] | 0.747 | zinc finger E-box binding homeobox 1 |
| [[KIAA1549L]] | 0.739 | KIAA1549 like |
| [[SLC4A7]] | 0.739 | solute carrier family 4 member 7 |
| [[FXYD5]] | 0.735 | FXYD domain containing ion transport regulator 5 |
| [[NIPAL1]] | 0.727 | NIPA like domain containing 1 |
| [[KCNC4]] | 0.724 | potassium voltage-gated channel subfamily C member 4 |
| [[NBPF9]] | 0.711 | NBPF member 9 |
| [[ACP7]] | 0.707 | acid phosphatase 7, tartrate resistant (putative) |
| [[NBPF8]] | 0.704 | NBPF member 8 |
| [[C12orf56]] | 0.691 | chromosome 12 open reading frame 56 |
| [[PARVB]] | 0.674 | parvin beta |
| [[ZNF83]] | 0.654 | zinc finger protein 83 |
| [[TUBB6]] | 0.654 | tubulin beta 6 class V |
| [[KBTBD8]] | 0.642 | kelch repeat and BTB domain containing 8 |
| [[LINC01629]] | 0.636 | long independently transcribed non-coding RNA 1629 |
| [[NBPF15]] | 0.635 | NBPF member 15 |
| [[ZNF710]] | 0.628 | zinc finger protein 710 |
| [[GBX1]] | 0.626 | gastrulation brain homeobox 1 |
| [[MBNL2]] | -0.618 | muscleblind like splicing regulator 2 |
| [[WT1-AS]] | 0.615 | WT1 antisense RNA |
| [[CAPN2]] | 0.615 | calpain 2 |
| [[CRYL1]] | 0.598 | crystallin lambda 1 |
| [[WT1]] | 0.590 | WT1 transcription factor |
| [[PLGRKT]] | 0.570 | plasminogen receptor with a C-terminal lysine |
| [[TNFRSF10A]] | 0.565 | TNF receptor superfamily member 10a |
| [[TBILA]] | 0.561 | TGF-beta induced lncRNA |
| [[GSTO1]] | 0.544 | glutathione S-transferase omega 1 |
| [[GMIP]] | 0.526 | GEM interacting protein |
| [[ZNF33A]] | -0.520 | zinc finger protein 33A |
| [[SYT9]] | 0.515 | synaptotagmin 9 |
| [[ENG]] | 0.509 | endoglin |
| [[BEGAIN]] | 0.503 | brain enriched guanylate kinase associated |
| [[KCNQ5]] | 0.502 | potassium voltage-gated channel subfamily Q member 5 |
| [[LINC02509]] | 0.447 | long independently transcribed non-coding RNA 2509 |
| [[SDCCAG8]] | 0.441 | SHH signaling and ciliogenesis regulator SDCCAG8 |
| [[GPR137B]] | 0.333 | G protein-coupled receptor 137B |
| [[LINC01010]] | 0.323 | long independently transcribed non-coding RNA 1010 |
| [[ZBTB7B]] | -0.314 | zinc finger and BTB domain containing 7B |
| [[APPL2]] | 0.279 | adaptor protein, phosphotyrosine interacting with PH domain and leucine zipper 2 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 110; `graph/modules.parquet` — module == 110; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [109] (drug-dose × line)
