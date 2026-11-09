---
module: 88
type: "module"
n_genes: 51
n_plus: 36
n_minus: 15
arms_opposite: true
mean_cos_between_arms: -0.4562649726867676
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 088

*51 genes (36 in the + arm, 15 in the − arm) · [[Module 088.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.46). The + arm rises where the − arm falls. Arm = the side of the module's main direction a gene sits on.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of the + arm minus the − arm (`graph/module_pooled_z.npy`, row 87), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it (+ arm up, − arm down): [[Homoharringtonine (drug)]] 5 µM (+21.4, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (+16.8, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (+12.3, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (+9.1, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.05 µM (+6.6); [[Dinaciclib (drug)]] 0.5 µM (+4.7, ⚠ toxic; transcription drop; cell-cycle shift); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+4.6); [[Dinaciclib (drug)]] 0.05 µM (+4.4, ⚠ toxic; transcription drop; cell-cycle shift); [[Auranofin (drug)]] 5 µM (+3.5); [[TAK-901 (drug)]] 5 µM (+3.3, ⚠ cell-cycle shift); [[Belumosudil (drug)]] 5 µM (+3.2); [[5-Azacytidine (drug)]] 5 µM (+2.9); [[Harringtonine (drug)]] 0.05 µM (+2.7); [[TAK-901 (drug)]] 0.05 µM (+2.7); [[Clobetasol propionate (drug)]] 0.05 µM (+2.5); [[Filgotinib (drug)]] 5 µM (+2.5); [[Binimetinib (drug)]] 0.05 µM (+2.5) (125 in all, 22 with an alert ⚠; shown: the 10 strongest and the 7 next strongest without an alert)
- Lower it: [[Panobinostat (drug)]] 5 µM (-20.3, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (-20.0, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (-19.5, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (-11.4, ⚠ cell-cycle shift); [[Belinostat (drug)]] 0.5 µM (-9.9, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (-8.8); [[Brivudine (drug)]] 5 µM (-7.3); [[Tucidinostat (drug)]] 0.5 µM (-4.8, ⚠ cell-cycle shift); [[Bortezomib (drug)]] 5 µM (-3.5, ⚠ toxic; cell-cycle shift); [[Ixazomib citrate (drug)]] 5 µM (-3.5, ⚠ cell-cycle shift); [[HI-TOPK-032 (drug)]] 5 µM (-3.3); [[Niclosamide (olamine) (drug)]] 0.5 µM (-2.7); [[PF-06260933 (drug)]] 5 µM (-2.6); [[Dimethyl fumarate (drug)]] 5 µM (-2.4); [[Radotinib (drug)]] 5 µM (-2.2); [[Belinostat (drug)]] 0.05 µM (-2.1); [[Ixazomib citrate (drug)]] 0.5 µM (-2.0); [[Bortezomib (drug)]] 0.5 µM (-2.0) (85 in all, 19 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[PANC-1 (line)]], [[SW480 (line)]], [[NCI-H23 (line)]], [[NCI-H460 (line)]], [[LoVo (line)]], [[NCI-H1573 (line)]], [[HOP62 (line)]], [[LOX-IMVI (line)]]

## + arm (36)

| Gene | Projection | Name |
|---|---|---|
| [[ST7L]] | 0.917 | suppression of tumorigenicity 7 like |
| [[RAB30-DT]] | 0.888 | RAB30 divergent transcript |
| [[WARS2-AS1]] | 0.875 | WARS2 antisense RNA 1 |
| [[CLHC1]] | 0.850 | clathrin heavy chain linker domain containing 1 |
| [[GABPB2]] | 0.842 | GA binding protein transcription factor subunit beta 2 |
| [[ZC3H4]] | 0.839 | zinc finger CCCH-type containing 4 |
| [[FKRP]] | 0.818 | fukutin related protein |
| [[LZIC]] | 0.814 | leucine zipper and CTNNBIP1 domain containing |
| [[NEPRO-AS1]] | 0.805 | NEPRO antisense RNA 1 |
| [[TASOR]] | 0.804 | transcription activation suppressor |
| [[MCPH1]] | 0.802 | microcephalin 1 |
| [[GTF2H1]] | 0.801 | general transcription factor IIH subunit 1 |
| [[TRMT13]] | 0.786 | tRNA methyltransferase 13 |
| [[FIZ1]] | 0.778 | FLT3 interacting zinc finger 1 |
| [[RGS5]] | 0.773 | regulator of G protein signaling 5 |
| [[ARMCX4]] | 0.766 | armadillo repeat containing X-linked 4 |
| [[SDCBP2-AS1]] | 0.765 | SDCBP2 antisense RNA 1 |
| [[USP40]] | 0.756 | ubiquitin specific peptidase 40 |
| [[NEK9]] | 0.754 | NIMA related kinase 9 |
| [[TXNRD2]] | 0.754 | thioredoxin reductase 2 |
| [[ZC3H7B]] | 0.741 | zinc finger CCCH-type containing 7B |
| [[VPS35L]] | 0.732 | VPS35 endosomal protein sorting factor like |
| [[HCG11]] | 0.730 | HLA complex group 11 |
| [[WDR33]] | 0.728 | WD repeat domain 33 |
| [[CARD8]] | 0.719 | caspase recruitment domain family member 8 |
| [[R3HDM2]] | 0.719 | R3H domain containing 2 |
| [[ITPRIPL2]] | 0.703 | ITPRIP like 2 |
| [[BCL2L13]] | 0.700 | BCL2 like 13 |
| [[EXOSC6]] | 0.687 | exosome component 6 |
| [[AFG3L1P]] | 0.680 | AFG3 like matrix AAA peptidase subunit 1, pseudogene |
| [[THOC7]] | 0.677 | THO complex subunit 7 |
| [[UPF3A]] | 0.577 | UPF3A regulator of nonsense mediated mRNA decay |
| [[SLC36A4]] | 0.502 | solute carrier family 36 member 4 |
| [[CREB1]] | 0.501 | cAMP responsive element binding protein 1 |
| [[MTMR1]] | 0.488 | myotubularin related protein 1 |
| [[TBX15]] | 0.477 | T-box transcription factor 15 |

## − arm (15)

| Gene | Projection | Name |
|---|---|---|
| [[IGSF8]] | -0.819 | immunoglobulin superfamily member 8 |
| [[EFNA4]] | -0.750 | ephrin A4 |
| [[AZIN2]] | -0.689 | antizyme inhibitor 2 |
| [[INPP5F]] | -0.686 | inositol polyphosphate-5-phosphatase F |
| [[ANKRD9]] | -0.681 | ankyrin repeat domain 9 |
| [[OSTF1]] | -0.670 | osteoclast stimulating factor 1 |
| [[KATNB1]] | -0.639 | katanin regulatory subunit B1 |
| [[PI4KAP2]] | -0.637 | phosphatidylinositol 4-kinase alpha pseudogene 2 |
| [[LPCAT2]] | -0.628 | lysophosphatidylcholine acyltransferase 2 |
| [[CPOX]] | -0.622 | coproporphyrinogen oxidase |
| [[GLCE]] | -0.584 | glucuronic acid epimerase |
| [[NAA80]] | -0.557 | N-alpha-acetyltransferase 80, NatH catalytic subunit |
| [[PI4KAP1]] | -0.554 | phosphatidylinositol 4-kinase alpha pseudogene 1 |
| [[SLC2A13]] | -0.552 | solute carrier family 2 member 13 |
| [[PMP22]] | -0.550 | peripheral myelin protein 22 |

## Data

- `graph/nodes.parquet` — module == 88; `graph/modules.parquet` — module == 88; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [87] (drug-dose × line)
