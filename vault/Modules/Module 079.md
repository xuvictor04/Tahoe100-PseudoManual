---
module: 79
type: "module"
n_genes: 57
n_plus: 57
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.3438127338886261
label: "hypoxia"
label_source: "hallmark"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 079

*hypoxia · 57 genes (single-armed) · [[Module 079.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

Label from the validation stage: **hypoxia** (hallmark, q 1e-14; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | hypoxia | hallmark | 16/57 | 23.3 | 1e-14 |
| + | hypoxia | hallmark | 16/57 | 23.3 | 1e-14 |
| all | hypoxia | control | 5/57 | 82.7 | 2e-06 |
| + | hypoxia | control | 5/57 | 82.7 | 2e-06 |
| all | glycolysis | hallmark | 8/57 | 11.6 | 2e-04 |
| + | glycolysis | hallmark | 8/57 | 11.6 | 2e-04 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 78), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Tucidinostat (drug)]] 5 µM (+2.3); [[PF-06260933 (drug)]] 5 µM (+2.1); [[Dimethyl fumarate (drug)]] 5 µM (+2.0); [[Tucidinostat (drug)]] 0.5 µM (+1.9, ⚠ cell-cycle shift); [[Artesunate (drug)]] 5 µM (+1.9, ⚠ cell-cycle shift); [[Fumaric acid (drug)]] 5 µM (+1.6); [[Terfenadine (drug)]] 5 µM (+1.5); [[Pravastatin (sodium) (drug)]] 5 µM (+1.4); [[Ouabain (Octahydrate) (drug)]] 5 µM (+1.3, ⚠ cell-cycle shift); [[Niclosamide (olamine) (drug)]] 0.5 µM (+1.2); [[Silodosin (drug)]] 5 µM (+1.1); [[Ritonavir (drug)]] 0.5 µM (+1.1); [[Cobimetinib (drug)]] 5 µM (+1.1) (17 in all, 4 with an alert ⚠; shown: the 10 strongest and the 3 next strongest without an alert)
- Lower it: [[Dinaciclib (drug)]] 5 µM (-7.7, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (-7.4, ⚠ toxic; transcription drop; cell-cycle shift); [[Homoharringtonine (drug)]] 5 µM (-6.8, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (-5.7, ⚠ toxic; transcription drop; cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-5.7, ⚠ cell-cycle shift); [[Niclosamide (olamine) (drug)]] 5 µM (-5.5, ⚠ toxic; cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-5.0, ⚠ cell-cycle shift); [[Topotecan (hydrochloride) (drug)]] 5 µM (-3.5, ⚠ toxic; cell-cycle shift); [[c-Kit-IN-1 (drug)]] 0.05 µM (-3.1, ⚠ unreliable plate only); [[Ixazomib citrate (drug)]] 5 µM (-2.8, ⚠ cell-cycle shift); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (-2.4); [[Belumosudil (drug)]] 5 µM (-2.4); [[Auranofin (drug)]] 5 µM (-2.3); [[Ixazomib citrate (drug)]] 0.5 µM (-1.8); [[TAK-733 (drug)]] 5 µM (-1.8); [[TAK-901 (drug)]] 0.05 µM (-1.7); [[5-Azacytidine (drug)]] 5 µM (-1.5); [[c-Kit-IN-1 (drug)]] 5 µM (-1.5); [[Retinoic acid (drug)]] 0.05 µM (-1.4); [[Clobetasol propionate (drug)]] 0.05 µM (-1.4) (45 in all, 19 with an alert ⚠; shown: the 10 strongest and the 10 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[C32 (line)]], [[NCI-H2347 (line)]], [[RPMI-7951 (line)]], [[LOX-IMVI (line)]], [[NCI-H1573 (line)]], [[A-172 (line)]], [[NCI-H1792 (line)]], [[CFPAC-1 (line)]]

## Candidate new members

*Members not annotated to the set their arm is enriched for, ranked by mean cos to the annotated members (`validation/novel_members.csv`); ⚠ = a reason to doubt the gene's place (in the vector space only through flagged drug-doses), kept in its rank. 36 candidates, none with an alert; shown: the 15 strongest.*

| # | Gene | Set | Mean cos |
|---|---|---|---|
| 1 | [[MXI1]] | hypoxia | +0.72 |
| 2 | [[HILPDA]] | hypoxia | +0.70 |
| 3 | [[KDM3A]] | glycolysis | +0.70 |
| 4 | [[FAM162A]] | hypoxia | +0.69 |
| 5 | [[SAP30-DT]] | hypoxia | +0.67 |
| 6 | [[RBPJ]] | hypoxia | +0.66 |
| 7 | [[KDM4B]] | hypoxia | +0.65 |
| 8 | [[FAM13A]] | glycolysis | +0.64 |
| 9 | [[NARF]] | hypoxia | +0.64 |
| 10 | [[ANKRD37]] | glycolysis | +0.63 |
| 11 | [[VKORC1]] | hypoxia | +0.63 |
| 12 | [[RNF122]] | hypoxia | +0.59 |
| 13 | [[DDIT4]] | hypoxia | +0.57 |
| 14 | [[WDR54]] | hypoxia | +0.56 |
| 15 | [[RLF]] | hypoxia | +0.56 |

## + arm (57)

| Gene | Projection | Name |
|---|---|---|
| [[HILPDA]] | 0.889 | hypoxia inducible lipid droplet associated |
| [[MXI1]] | 0.875 | MAX interactor 1, dimerization protein |
| [[KDM3A]] | 0.874 | lysine demethylase 3A |
| [[FAM162A]] | 0.866 | family with sequence similarity 162 member A |
| [[ANKRD37]] | 0.857 | ankyrin repeat domain 37 |
| [[SAP30-DT]] | 0.849 | SAP30 divergent transcript |
| [[P4HA1]] | 0.847 | prolyl 4-hydroxylase subunit alpha 1 |
| [[RBPJ]] | 0.823 | recombination signal binding protein for immunoglobulin kappa J region |
| [[FAM13A]] | 0.820 | family with sequence similarity 13 member A |
| [[VKORC1]] | 0.804 | vitamin K epoxide reductase complex subunit 1 |
| [[SAP30]] | 0.770 | Sin3A associated protein 30 |
| [[KDM4B]] | 0.753 | lysine demethylase 4B |
| [[WDR54]] | 0.747 | WD repeat domain 54 |
| [[ADM]] | 0.738 | adrenomedullin |
| [[EFNA3]] | 0.737 | ephrin A3 |
| [[DDIT4]] | 0.729 | DNA damage inducible transcript 4 |
| [[NARF]] | 0.729 | nuclear prelamin A recognition factor |
| [[ALDOC]] | 0.724 | aldolase, fructose-bisphosphate C |
| [[RNF122]] | 0.718 | ring finger protein 122 |
| [[ZNF395]] | 0.707 | zinc finger protein 395 |
| [[ABCB9]] | 0.706 | ATP binding cassette subfamily B member 9 |
| [[FBXO42]] | 0.702 | F-box protein 42 |
| [[RFX2]] | 0.701 | regulatory factor X2 |
| [[RNF24]] | 0.687 | ring finger protein 24 |
| [[RLF]] | 0.687 | RLF zinc finger |
| [[RYBP]] | 0.677 | RING1 and YY1 binding protein |
| [[DEPP1]] | 0.671 | DEPP autophagy regulator 1 |
| [[ARSK]] | 0.661 | arylsulfatase family member K |
| [[ANKZF1]] | 0.661 | ankyrin repeat and zinc finger peptidyl tRNA hydrolase 1 |
| [[MAP3K2]] | 0.660 | mitogen-activated protein kinase kinase kinase 2 |
| [[ZNF292]] | 0.656 | zinc finger protein 292 |
| [[CCSAP]] | 0.654 | centriole, cilia and spindle associated protein |
| [[SLC25A36]] | 0.653 | solute carrier family 25 member 36 |
| [[AVPI1]] | 0.651 | arginine vasopressin induced 1 |
| [[C4orf3]] | 0.651 | allregulin |
| [[PARVA]] | -0.641 | parvin alpha |
| [[BRWD3]] | 0.627 | bromodomain and WD repeat domain containing 3 |
| [[LPIN2]] | 0.623 | lipin 2 |
| [[BNIP3L]] | 0.621 | BCL2 interacting protein 3 like |
| [[RORA]] | 0.606 | RAR related orphan receptor A |
| [[ZMYM2]] | 0.605 | zinc finger MYM-type containing 2 |
| [[ZMAT5]] | 0.605 | zinc finger matrin-type 5 |
| [[THAP8]] | 0.590 | THAP domain containing 8 |
| [[CLEC2B]] | 0.578 | C-type lectin domain family 2 member B |
| [[PPP1R3C]] | 0.552 | protein phosphatase 1 regulatory subunit 3C |
| [[PTCH1]] | 0.536 | patched 1 |
| [[ACOT9]] | -0.534 | acyl-CoA thioesterase 9 |
| [[PLIN2]] | 0.533 | perilipin 2 |
| [[OXR1]] | 0.485 | oxidation resistance 1 |
| [[PTPN21]] | -0.483 | protein tyrosine phosphatase non-receptor type 21 |
| [[LIX1L]] | 0.476 | limb and CNS expressed 1 like |
| [[PPP1R3B]] | 0.470 | protein phosphatase 1 regulatory subunit 3B |
| [[SNAPC1]] | 0.469 | small nuclear RNA activating complex polypeptide 1 |
| [[SDAD1P1]] | 0.464 | SDA1 domain containing 1 pseudogene 1 |
| [[PRKD3]] | 0.463 | protein kinase D3 |
| [[ARL4D]] | 0.432 | ARF like GTPase 4D |
| [[POU3F3]] | 0.405 | POU class 3 homeobox 3 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 79; `graph/modules.parquet` — module == 79; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [78] (drug-dose × line)
