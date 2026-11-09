---
module: 97
type: "module"
n_genes: 48
n_plus: 48
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: "estrogen response early"
label_source: "hallmark"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 097

*estrogen response early · 48 genes (single-armed) · [[Module 097.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

Label from the validation stage: **estrogen response early** (hallmark, q 0.011; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | estrogen response early | hallmark | 6/48 | 10.2 | 0.011 |
| + | estrogen response early | hallmark | 6/48 | 10.2 | 0.011 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 96), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Tucidinostat (drug)]] 5 µM (+7.2); [[Panobinostat (drug)]] 5 µM (+6.2, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (+5.9, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (+5.7, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (+5.2, ⚠ cell-cycle shift); [[Clobetasol propionate (drug)]] 0.5 µM (+4.1); [[Clobetasol propionate (drug)]] 0.05 µM (+4.0); [[Tucidinostat (drug)]] 0.5 µM (+4.0, ⚠ cell-cycle shift); [[Budesonide (drug)]] 0.5 µM (+3.5); [[Budesonide (drug)]] 5 µM (+3.3); [[Dexamethasone (drug)]] 0.5 µM (+3.3); [[Clobetasol propionate (drug)]] 5 µM (+3.3); [[Betamethasone dipropionate (drug)]] 0.05 µM (+3.2); [[Betamethasone dipropionate (drug)]] 0.5 µM (+3.2); [[Brivudine (drug)]] 5 µM (+3.1) (33 in all, 6 with an alert ⚠; shown: the 10 strongest and the 5 next strongest without an alert)
- Lower it: [[Homoharringtonine (drug)]] 5 µM (-6.2, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-6.1, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (-4.5, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-4.2, ⚠ cell-cycle shift); [[Topotecan (hydrochloride) (drug)]] 5 µM (-3.8, ⚠ toxic; cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (-3.5, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.05 µM (-3.2); [[Idarubicin (hydrochloride) (drug)]] 5 µM (-3.1, ⚠ cell-cycle shift); [[c-Kit-IN-1 (drug)]] 0.05 µM (-3.0, ⚠ unreliable plate only); [[Selinexor (drug)]] 5 µM (-2.9, ⚠ cell-cycle shift); [[TAK-733 (drug)]] 5 µM (-2.7); [[Ixazomib citrate (drug)]] 0.5 µM (-2.6); [[Abemaciclib (drug)]] 5 µM (-2.3); [[Auranofin (drug)]] 5 µM (-2.3); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM (-2.1); [[venetoclax (drug)]] 5 µM (-1.9); [[PH-797804 (drug)]] 5 µM (-1.9); [[c-Kit-IN-1 (drug)]] 5 µM (-1.8); [[Trametinib (drug)]] 0.5 µM (-1.8) (58 in all, 29 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[PANC-1 (line)]], [[NCI-H23 (line)]], [[NCI-H460 (line)]], [[KATO III (line)]], [[NCI-H2030 (line)]], [[SW480 (line)]], [[A-427 (line)]], [[LOX-IMVI (line)]]

## + arm (48)

| Gene | Projection | Name |
|---|---|---|
| [[TBC1D8]] | 0.834 | TBC1 domain family member 8 |
| [[ERGIC1]] | 0.822 | endoplasmic reticulum-golgi intermediate compartment 1 |
| [[AKAP13]] | 0.789 | A-kinase anchoring protein 13 |
| [[PACSIN2]] | 0.744 | protein kinase C and casein kinase substrate in neurons 2 |
| [[TOX2]] | 0.724 | TOX high mobility group box family member 2 |
| [[ATP1A1]] | 0.718 | ATPase Na+/K+ transporting subunit alpha 1 |
| [[PKP2]] | 0.691 | plakophilin 2 |
| [[ABLIM3]] | 0.685 | actin binding LIM protein family member 3 |
| [[NCOA3]] | 0.680 | nuclear receptor coactivator 3 |
| [[DENND3]] | 0.673 | DENN domain containing 3 |
| [[PYGB]] | 0.669 | glycogen phosphorylase B |
| [[RHOBTB2]] | 0.667 | Rho related BTB domain containing 2 |
| [[SH3RF3]] | 0.665 | SH3 domain containing ring finger 3 |
| [[TMEM164]] | 0.663 | transmembrane protein 164 |
| [[KIF13B]] | 0.660 | kinesin family member 13B |
| [[FOXO1]] | 0.659 | forkhead box O1 |
| [[SNED1]] | 0.652 | sushi, nidogen and EGF like domains 1 |
| [[PTPN1]] | 0.649 | protein tyrosine phosphatase non-receptor type 1 |
| [[ABLIM2]] | 0.648 | actin binding LIM protein family member 2 |
| [[ZHX3]] | 0.648 | zinc fingers and homeoboxes 3 |
| [[OSBPL5]] | 0.647 | oxysterol binding protein like 5 |
| [[RPGR]] | 0.627 | retinitis pigmentosa GTPase regulator |
| [[SHROOM2]] | 0.622 | shroom family member 2 |
| [[RPS6KA2]] | 0.619 | ribosomal protein S6 kinase A2 |
| [[TGFBR2]] | 0.610 | transforming growth factor beta receptor 2 |
| [[MFGE8]] | 0.606 | milk fat globule EGF and factor V/VIII domain containing |
| [[ABHD2]] | 0.599 | abhydrolase domain containing 2, acylglycerol lipase |
| [[TBC1D16]] | 0.582 | TBC1 domain family member 16 |
| [[FZD4]] | 0.566 | frizzled class receptor 4 |
| [[FRY]] | 0.565 | FRY microtubule binding protein |
| [[PXYLP1]] | 0.565 | 2-phosphoxylose phosphatase 1 |
| [[ADRA1B]] | 0.552 | adrenoceptor alpha 1B |
| [[EVA1C]] | 0.545 | eva-1 homolog C |
| [[HIP1R]] | 0.543 | huntingtin interacting protein 1 related |
| [[LAMB1]] | 0.538 | laminin subunit beta 1 |
| [[AGFG2]] | 0.533 | ArfGAP with FG repeats 2 |
| [[C16orf74]] | 0.522 | calcimembrin |
| [[IGFBP4]] | 0.519 | insulin like growth factor binding protein 4 |
| [[LINC00598]] | 0.512 | long independently transcribed non-coding RNA 598 |
| [[SEC14L2]] | 0.511 | SEC14 like lipid binding 2 |
| [[ITGA5]] | 0.490 | integrin subunit alpha 5 |
| [[SERPINA5]] | 0.482 | serpin family A member 5 |
| [[PPP3CA]] | 0.447 | protein phosphatase 3 catalytic subunit alpha |
| [[KRT6A]] | 0.440 | keratin 6A |
| [[MLKL]] | 0.431 | mixed lineage kinase domain like pseudokinase |
| [[TCF7L2]] | 0.396 | transcription factor 7 like 2 |
| [[TFAP2C]] | 0.194 | transcription factor AP-2 gamma |
| [[PELI2]] | 0.131 | pellino E3 ubiquitin protein ligase family member 2 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 97; `graph/modules.parquet` — module == 97; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [96] (drug-dose × line)
