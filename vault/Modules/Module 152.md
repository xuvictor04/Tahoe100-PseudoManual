---
module: 152
type: "module"
n_genes: 29
n_plus: 29
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: "Retinoid metabolism and transport"
label_source: "reactome"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 152

*Retinoid metabolism and transport · 29 genes (single-armed) · [[Module 152.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

Label from the validation stage: **Retinoid metabolism and transport** (reactome, q 0.011; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | Retinoid metabolism and transport | reactome | 3/29 | 52.0 | 0.011 |
| + | Retinoid metabolism and transport | reactome | 3/29 | 52.0 | 0.011 |
| all | Metabolism of fat-soluble vitamins | reactome | 3/29 | 45.9 | 0.015 |
| + | Metabolism of fat-soluble vitamins | reactome | 3/29 | 45.9 | 0.015 |
| all | Sensory Perception | reactome | 4/29 | 15.3 | 0.045 |
| + | Sensory Perception | reactome | 4/29 | 15.3 | 0.045 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 151), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Tucidinostat (drug)]] 5 µM (+11.6); [[Idarubicin (hydrochloride) (drug)]] 5 µM (+7.4, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 0.5 µM (+6.9, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (+4.8, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (+4.5, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (+4.0, ⚠ toxic; transcription drop; cell-cycle shift); [[Panobinostat (drug)]] 5 µM (+3.8, ⚠ cell-cycle shift); [[Cobimetinib (drug)]] 5 µM (+3.6); [[Panobinostat (drug)]] 0.5 µM (+3.1, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (+2.8, ⚠ cell-cycle shift); [[Ponatinib (drug)]] 0.5 µM (+2.5); [[Brivudine (drug)]] 5 µM (+2.4); [[Cobimetinib (drug)]] 0.5 µM (+2.3); [[Trametinib (drug)]] 0.5 µM (+2.2); [[Binimetinib (drug)]] 5 µM (+1.8); [[Binimetinib (drug)]] 0.5 µM (+1.7); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM (+1.7); [[Verteporfin (drug)]] 5 µM (+1.7) (49 in all, 14 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)
- Lower it: [[Digitoxin (drug)]] 0.5 µM (-5.0, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (-4.7, ⚠ cell-cycle shift); [[Ixazomib citrate (drug)]] 5 µM (-4.1, ⚠ cell-cycle shift); [[Ixazomib citrate (drug)]] 0.5 µM (-4.0); [[Homoharringtonine (drug)]] 0.5 µM (-4.0, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-3.3, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 0.05 µM (-3.2, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 5 µM (-3.0, ⚠ toxic; transcription drop; cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (-2.9, ⚠ cell-cycle shift); [[Vinblastine (sulfate) (drug)]] 5 µM (-2.9); [[Vinblastine (sulfate) (drug)]] 0.5 µM (-2.9); [[Mebendazole (drug)]] 5 µM (-2.6); [[5-Azacytidine (drug)]] 5 µM (-2.6); [[Peretinoin (drug)]] 5 µM (-2.4); [[Peretinoin (drug)]] 0.5 µM (-2.1); [[Neratinib (maleate) (drug)]] 5 µM (-1.9); [[Homoharringtonine (drug)]] 0.05 µM (-1.8); [[crizotinib (drug)]] 5 µM (-1.6) (58 in all, 20 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[C32 (line)]], [[PANC-1 (line)]], [[NCI-H460 (line)]], [[NCI-H23 (line)]], [[SNU-1 (line)]], [[NCI-H1792 (line)]], [[SK-MEL-2 (line)]], [[LOX-IMVI (line)]]

## + arm (29)

| Gene | Projection | Name |
|---|---|---|
| [[EPHA3]] | 0.853 | EPH receptor A3 |
| [[PTPRD]] | 0.769 | protein tyrosine phosphatase receptor type D |
| [[ARHGAP28]] | 0.765 | Rho GTPase activating protein 28 |
| [[LRRC7]] | 0.752 | leucine rich repeat containing 7 |
| [[RARB]] | 0.741 | retinoic acid receptor beta |
| [[NREP]] | 0.739 | neuronal regeneration related protein |
| [[LRP2]] | 0.739 | LDL receptor related protein 2 |
| [[TMEM178B]] | 0.710 | transmembrane protein 178B |
| [[LRAT]] | 0.700 | lecithin retinol acyltransferase |
| [[SFMBT2]] | 0.700 | Scm like with four mbt domains 2 |
| [[KCTD16]] | 0.699 | potassium channel tetramerization domain containing 16 |
| [[EYA1]] | 0.687 | EYA transcriptional coactivator and phosphatase 1 |
| [[ZMAT4]] | 0.686 | zinc finger matrin-type 4 |
| [[LINGO2]] | 0.675 | leucine rich repeat and Ig domain containing 2 |
| [[MEF2C]] | 0.667 | myocyte enhancer factor 2C |
| [[SNAP25]] | 0.666 | synaptosome associated protein 25 |
| [[GPC6]] | 0.631 | glypican 6 |
| [[SLFN11]] | 0.631 | schlafen family member 11 |
| [[LINC01583]] | 0.622 | long independently transcribed non-coding RNA 1583 |
| [[MEIS1]] | 0.609 | Meis homeobox 1 |
| [[TRIM9]] | 0.582 | tripartite motif containing 9 |
| [[CFI]] | 0.568 | complement factor I |
| [[ARHGAP20]] | 0.497 | Rho GTPase activating protein 20 |
| [[PLA2G4A]] | 0.494 | phospholipase A2 group IVA |
| [[RNF165]] | 0.426 | arkadia (RNF111) C-terminal like ring finger ubiquitin ligase 2C |
| [[GAL]] | 0.405 | galanin and GMAP prepropeptide |
| [[ANOS1]] | 0.399 | anosmin 1 |
| [[NR2F1]] | 0.286 | nuclear receptor subfamily 2 group F member 1 |
| [[RNF217]] | 0.196 | ring finger protein 217 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 152; `graph/modules.parquet` — module == 152; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [151] (drug-dose × line)
