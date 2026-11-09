---
module: 76
type: "module"
n_genes: 59
n_plus: 59
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.3066386878490448
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 076

*59 genes (single-armed) · [[Module 076.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 75), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Panobinostat (drug)]] 5 µM (+4.7, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (+4.5, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (+4.0, ⚠ cell-cycle shift); [[Belinostat (drug)]] 0.5 µM (+2.0, ⚠ cell-cycle shift); [[Selinexor (drug)]] 5 µM (+1.8, ⚠ cell-cycle shift); [[GSK1059615 (drug)]] 0.5 µM (+1.8); [[Panobinostat (drug)]] 0.05 µM (+1.8, ⚠ cell-cycle shift); [[GSK1059615 (drug)]] 5 µM (+1.7); [[NG25 (drug)]] 5 µM (+1.5, ⚠ cell-cycle shift); [[Bimiralisib (drug)]] 5 µM (+1.4); [[Brivudine (drug)]] 5 µM (+1.3); [[Ponatinib (drug)]] 5 µM (+1.3); [[Temsirolimus (drug)]] 5 µM (+1.1); [[XRK3F2 (drug)]] 0.5 µM (+1.1); [[AZD-8055 (drug)]] 5 µM (+1.1); [[AZD-8055 (drug)]] 0.5 µM (+1.1); [[Temsirolimus (drug)]] 0.5 µM (+1.1) (26 in all, 10 with an alert ⚠; shown: the 10 strongest and the 7 next strongest without an alert)
- Lower it: [[c-Kit-IN-1 (drug)]] 0.05 µM (-12.7, ⚠ unreliable plate only); [[Homoharringtonine (drug)]] 5 µM (-8.1, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-6.9, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-6.8, ⚠ cell-cycle shift); [[TAK-733 (drug)]] 5 µM (-6.0); [[Harringtonine (drug)]] 0.5 µM (-5.7, ⚠ cell-cycle shift); [[Abemaciclib (drug)]] 5 µM (-5.5); [[c-Kit-IN-1 (drug)]] 5 µM (-5.4); [[EX229 (drug)]] 5 µM (-5.3); [[venetoclax (drug)]] 5 µM (-5.0); [[Abemaciclib (drug)]] 0.5 µM (-4.2); [[EX229 (drug)]] 0.05 µM (-3.7); [[Homoharringtonine (drug)]] 0.05 µM (-3.3); [[EX229 (drug)]] 0.5 µM (-3.0); [[Sapanisertib (drug)]] 0.5 µM (-2.4) (45 in all, 20 with an alert ⚠; shown: the 10 strongest and the 5 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[PANC-1 (line)]], [[SW480 (line)]], [[AsPC-1 (line)]], [[MIA PaCa-2 (line)]], [[CFPAC-1 (line)]], [[HEC-1-A (line)]], [[HOP62 (line)]], [[HT-29 (line)]]

## + arm (59)

| Gene | Projection | Name |
|---|---|---|
| [[CCDC28A]] | 0.877 | coiled-coil domain containing 28A |
| [[SPSB3]] | 0.847 | splA/ryanodine receptor domain and SOCS box containing 3 |
| [[WIPI2]] | 0.822 | WD repeat domain, phosphoinositide interacting 2 |
| [[KLHDC3]] | 0.818 | kelch domain containing 3 |
| [[CRIPT]] | 0.810 | CXXC repeat containing interactor of PDZ3 domain |
| [[ADIPOR1]] | 0.801 | adiponectin receptor 1 |
| [[YPEL3]] | 0.779 | yippee like 3 |
| [[CALCOCO1]] | 0.779 | calcium binding and coiled-coil domain 1 |
| [[MOSPD3]] | 0.774 | motile sperm domain containing 3 |
| [[MARF1]] | 0.757 | meiosis regulator and mRNA stability factor 1 |
| [[AUH]] | 0.755 | AU RNA binding methylglutaconyl-CoA hydratase |
| [[RALBP1]] | 0.749 | ralA binding protein 1 |
| [[LINC01881]] | 0.737 | long independently transcribed non-coding RNA 1881 |
| [[LMBR1L]] | 0.730 | limb development membrane protein 1 like |
| [[WASF2]] | 0.729 | WASP family member 2 |
| [[HINFP]] | 0.729 | histone H4 transcription factor |
| [[COQ8A]] | 0.729 | coenzyme Q8A |
| [[RETREG2]] | 0.727 | reticulophagy regulator family member 2 |
| [[UBXN6]] | 0.725 | UBX domain protein 6 |
| [[FBXO25]] | 0.720 | F-box protein 25 |
| [[YPEL2]] | 0.719 | yippee like 2 |
| [[MARCHF8]] | 0.714 | membrane associated ring-CH-type finger 8 |
| [[HACL1]] | 0.712 | 2-hydroxyacyl-CoA lyase 1 |
| [[SARAF]] | 0.706 | store-operated calcium entry associated regulatory factor |
| [[ABTB1]] | 0.700 | ankyrin repeat and BTB domain containing 1 |
| [[SEMA6C]] | 0.679 | semaphorin 6C |
| [[MTMR14]] | 0.675 | myotubularin related protein 14 |
| [[ATF6B]] | 0.673 | activating transcription factor 6 beta |
| [[ATG14]] | 0.672 | autophagy related 14 |
| [[INPP5K]] | 0.672 | inositol polyphosphate-5-phosphatase K |
| [[PBXIP1]] | 0.672 | PBX homeobox interacting protein 1 |
| [[CBX7]] | 0.670 | chromobox 7 |
| [[MBTPS1]] | 0.667 | membrane bound transcription factor peptidase, site 1 |
| [[TFDP2]] | 0.642 | transcription factor Dp-2 |
| [[TPRG1L]] | 0.638 | tumor protein p63 regulated 1 like |
| [[KIZ]] | 0.635 | kizuna centrosomal protein |
| [[NIPAL3]] | 0.631 | NIPA like domain containing 3 |
| [[PLEKHM3]] | 0.621 | pleckstrin homology domain containing M3 |
| [[FOXO4]] | 0.613 | forkhead box O4 |
| [[FKBP8]] | 0.608 | FKBP prolyl isomerase 8 |
| [[DCAF11]] | 0.603 | DDB1 and CUL4 associated factor 11 |
| [[SCAMP1]] | 0.600 | secretory carrier membrane protein 1 |
| [[MED25]] | 0.593 | mediator complex subunit 25 |
| [[RPS6KA5]] | 0.586 | ribosomal protein S6 kinase A5 |
| [[PIH1D1]] | 0.578 | PIH1 domain containing 1 |
| [[AAMP]] | 0.577 | angio associated migratory cell protein |
| [[PIK3C3]] | 0.556 | phosphatidylinositol 3-kinase catalytic subunit type 3 |
| [[C9orf78]] | 0.534 | chromosome 9 open reading frame 78 |
| [[KIF21A]] | -0.486 | kinesin family member 21A |
| [[BTBD8]] | 0.486 | BTB domain containing 8 |
| [[BBS9]] | 0.483 | Bardet-Biedl syndrome 9 |
| [[PCMTD2]] | 0.478 | protein-L-isoaspartate (D-aspartate) O-methyltransferase domain containing 2 |
| [[EPG5]] | 0.473 | ectopic P-granules 5 autophagy tethering factor |
| [[GMPR2]] | 0.468 | guanosine monophosphate reductase 2 |
| [[TNKS]] | 0.468 | tankyrase |
| [[PTTG1IP]] | 0.449 | PTTG1 interacting protein |
| [[ELK1]] | 0.389 | ETS transcription factor ELK1 |
| [[CNOT2]] | 0.365 | CCR4-NOT transcription complex subunit 2 |
| [[ARFGEF1]] | 0.277 | ARF guanine nucleotide exchange factor 1 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 76; `graph/modules.parquet` — module == 76; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [75] (drug-dose × line)
