---
module: 73
type: "module"
n_genes: 66
n_plus: 66
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 073

*66 genes (single-armed) · [[Module 073.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 72), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Dinaciclib (drug)]] 0.5 µM (+9.8, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (+9.5, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+7.1, ⚠ toxic; transcription drop; cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (+6.0, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (+4.1); [[Homoharringtonine (drug)]] 5 µM (+3.6, ⚠ cell-cycle shift); [[Docetaxel (drug)]] 0.05 µM (+2.9, ⚠ transcription drop; cell-cycle shift); [[Lonafarnib (drug)]] 5 µM (+2.8, ⚠ toxic); [[Topotecan (hydrochloride) (drug)]] 5 µM (+2.8, ⚠ toxic; cell-cycle shift); [[Tucidinostat (drug)]] 0.5 µM (+2.5, ⚠ cell-cycle shift); [[Ipatasertib (drug)]] 0.5 µM (+2.2); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+2.1); [[Auranofin (drug)]] 5 µM (+1.9); [[Docetaxel (Trihydrate) (drug)]] 0.5 µM (+1.8); [[XRK3F2 (drug)]] 0.5 µM (+1.8); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM (+1.6); [[vincristine (drug)]] 0.5 µM (+1.5); [[9-ING-41 (drug)]] 0.5 µM (+1.4); [[Methylprednisolone succinate (drug)]] 0.5 µM (+1.3) (63 in all, 25 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)
- Lower it: [[Belinostat (drug)]] 5 µM (-2.8, ⚠ cell-cycle shift); [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM (-2.7); [[Panobinostat (drug)]] 0.5 µM (-2.2, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (-2.2, ⚠ cell-cycle shift); [[Erlotinib (drug)]] 0.05 µM (-1.9); [[Lucanthone (drug)]] 0.05 µM (-1.9); [[Artesunate (drug)]] 0.5 µM (-1.8); [[Anethole trithione (drug)]] 0.5 µM (-1.8); [[Fenofibrate (drug)]] 0.05 µM (-1.7); [[Rutin (trihydrate) (drug)]] 0.05 µM (-1.7); [[Encorafenib (drug)]] 5 µM (-1.6); [[Diphenhydramine (drug)]] 0.05 µM (-1.6); [[Brivudine (drug)]] 5 µM (-1.6) (53 in all, 9 with an alert ⚠; shown: the 10 strongest and the 3 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[LoVo (line)]], [[LS 180 (line)]], [[RKO (line)]], [[SNU-1 (line)]], [[KATO III (line)]], [[COLO 205 (line)]], [[SK-MEL-2 (line)]], [[HT-29 (line)]]

## + arm (66)

| Gene | Projection | Name |
|---|---|---|
| [[CALB1]] | 0.886 | calbindin 1 |
| [[NPSR1]] | 0.884 | neuropeptide S receptor 1 |
| [[SLC6A20]] | 0.873 | solute carrier family 6 member 20 |
| [[HEPH]] | 0.853 | hephaestin |
| [[DSG4]] | 0.853 | desmoglein 4 |
| [[TPTEP1-1]] | 0.846 | — |
| [[KLK10]] | 0.838 | kallikrein related peptidase 10 |
| [[LINC02582]] | 0.833 | long independently transcribed non-coding RNA 2582 |
| [[FAM3D]] | 0.823 | FAM3 metabolism regulating signaling molecule D |
| [[CTSE]] | 0.820 | cathepsin E |
| [[LINC02474]] | 0.814 | long independently transcribed non-coding RNA 2474 |
| [[SPON1]] | 0.813 | spondin 1 |
| [[MUC17]] | 0.801 | mucin 17, cell surface associated |
| [[NOSTRIN]] | 0.797 | nitric oxide synthase trafficking |
| [[C4BPB]] | 0.788 | complement component 4 binding protein beta |
| [[ACSL5]] | 0.768 | acyl-CoA synthetase long chain family member 5 |
| [[TFF2]] | 0.768 | trefoil factor 2 |
| [[DSG3]] | 0.766 | desmoglein 3 |
| [[SERPINB5]] | 0.756 | serpin family B member 5 |
| [[IGFL2]] | 0.748 | IGF like family member 2 |
| [[COL17A1]] | 0.748 | collagen type XVII alpha 1 chain |
| [[CEACAM6]] | 0.736 | CEA cell adhesion molecule 6 |
| [[MUC2]] | 0.734 | mucin 2, oligomeric mucus/gel-forming |
| [[CYP3A5]] | 0.730 | cytochrome P450 family 3 subfamily A member 5 |
| [[KLK11]] | 0.711 | kallikrein related peptidase 11 |
| [[TMEM30B]] | 0.700 | cell division cycle 50 P4-ATPase accessory subunit B |
| [[REG4]] | 0.696 | regenerating family member 4 |
| [[SEPTIN9-DT]] | 0.695 | SEPTIN9 divergent transcript |
| [[HTR1D]] | 0.688 | 5-hydroxytryptamine receptor 1D |
| [[INPP1]] | 0.678 | inositol polyphosphate-1-phosphatase |
| [[SLC22A3]] | 0.675 | solute carrier family 22 member 3 |
| [[CFAP46]] | 0.670 | cilia and flagella associated protein 46 |
| [[EHF]] | 0.667 | ETS homologous factor |
| [[FGFBP1]] | 0.660 | fibroblast growth factor binding protein 1 |
| [[MMP28]] | 0.653 | matrix metallopeptidase 28 |
| [[SULF2]] | 0.652 | sulfatase 2 |
| [[LAD1]] | 0.650 | ladinin 1 |
| [[SLCO1B3]] | 0.623 | solute carrier organic anion transporter family member 1B3 |
| [[IL2RG]] | 0.614 | interleukin 2 receptor subunit gamma |
| [[TRABD2A]] | 0.611 | TraB domain containing 2A |
| [[FUT4]] | 0.610 | fucosyltransferase 4 |
| [[PKP1]] | 0.607 | plakophilin 1 |
| [[IL1R2]] | 0.607 | interleukin 1 receptor type 2 |
| [[TFF1]] | 0.603 | trefoil factor 1 |
| [[CD200]] | 0.588 | CD200 molecule |
| [[SLCO1B3-SLCO1B7]] | 0.586 | SLCO1B3-SLCO1B7 readthrough |
| [[TLN2]] | 0.580 | talin 2 |
| [[BAIAP2L2]] | 0.580 | BAR/IMD domain containing adaptor protein 2 like 2 |
| [[XYLT1]] | 0.579 | xylosyltransferase 1 |
| [[LINC00589]] | 0.570 | long independently transcribed non-coding RNA 589 |
| [[LINC00457]] | 0.562 | long independently transcribed non-coding RNA 457 |
| [[PIWIL4]] | 0.556 | piwi like RNA-mediated gene silencing 4 |
| [[ERG]] | 0.556 | ETS transcription factor ERG |
| [[MYO16-AS1]] | 0.546 | MYO16 antisense RNA 1 |
| [[XACT]] | 0.544 | X active specific transcript |
| [[GALNT5]] | 0.542 | polypeptide N-acetylgalactosaminyltransferase 5 |
| [[ARHGAP6]] | 0.536 | Rho GTPase activating protein 6 |
| [[PRSS22]] | 0.531 | serine protease 22 |
| [[PITPNM3]] | 0.523 | PITPNM family member 3 |
| [[ZNF736P9Y]] | 0.515 | zinc finger protein 736 pseudogene 9, Y-linked |
| [[SLC9A2]] | 0.466 | solute carrier family 9 member A2 |
| [[LINC02595]] | 0.465 | — |
| [[RBP1]] | 0.385 | retinol binding protein 1 |
| [[ADIRF]] | 0.383 | adipogenesis regulatory factor |
| [[DMKN]] | 0.311 | dermokine |
| [[KRTCAP3]] | 0.305 | keratinocyte associated protein 3 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 73; `graph/modules.parquet` — module == 73; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [72] (drug-dose × line)
