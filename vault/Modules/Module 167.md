---
module: 167
type: "module"
n_genes: 25
n_plus: 25
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 167

*25 genes (single-armed) · [[Module 167.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 166), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Tucidinostat (drug)]] 5 µM (+5.8); [[Dinaciclib (drug)]] 0.5 µM (+3.9, ⚠ toxic; transcription drop; cell-cycle shift); [[Tucidinostat (drug)]] 0.5 µM (+3.9, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (+3.5, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+2.8, ⚠ toxic; transcription drop; cell-cycle shift); [[Binimetinib (drug)]] 5 µM (+2.4); [[Trametinib (drug)]] 0.5 µM (+2.3); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM (+2.2); [[Cobimetinib (drug)]] 5 µM (+2.0); [[Binimetinib (drug)]] 0.5 µM (+1.8); [[Binimetinib (drug)]] 0.05 µM (+1.8); [[XRK3F2 (drug)]] 0.5 µM (+1.7); [[GSK1059615 (drug)]] 0.5 µM (+1.7); [[Bimiralisib (drug)]] 0.5 µM (+1.6) (39 in all, 8 with an alert ⚠; shown: the 10 strongest and the 4 next strongest without an alert)
- Lower it: [[Ixazomib citrate (drug)]] 5 µM (-3.9, ⚠ cell-cycle shift); [[c-Kit-IN-1 (drug)]] 0.05 µM (-3.5, ⚠ unreliable plate only); [[Bortezomib (drug)]] 0.05 µM (-3.2, ⚠ cell-cycle shift); [[Ixazomib citrate (drug)]] 0.5 µM (-3.2); [[Auranofin (drug)]] 5 µM (-2.5); [[Belinostat (drug)]] 5 µM (-2.4, ⚠ cell-cycle shift); [[Abemaciclib (drug)]] 5 µM (-2.2); [[Mebendazole (drug)]] 5 µM (-2.2); [[Vinblastine (sulfate) (drug)]] 5 µM (-2.0); [[Digitoxin (drug)]] 0.5 µM (-2.0, ⚠ cell-cycle shift); [[TAK-733 (drug)]] 5 µM (-1.9); [[Tofacitinib (drug)]] 0.5 µM (-1.9); [[c-Kit-IN-1 (drug)]] 5 µM (-1.9); [[5-Azacytidine (drug)]] 5 µM (-1.9); [[Vinblastine (sulfate) (drug)]] 0.5 µM (-1.7) (44 in all, 14 with an alert ⚠; shown: the 10 strongest and the 5 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[BT-474 (line)]], [[C32 (line)]], [[Panc 03.27 (line)]], [[SW 900 (line)]], [[NCI-H1792 (line)]], [[A498 (line)]], [[NCI-H1573 (line)]], [[CFPAC-1 (line)]]

## + arm (25)

| Gene | Projection | Name |
|---|---|---|
| [[LINC02015]] | 0.849 | long independently transcribed non-coding RNA 2015 |
| [[CD38]] | 0.806 | CD38 molecule |
| [[CP]] | 0.788 | ceruloplasmin |
| [[TCIM]] | 0.748 | transcriptional and immune response regulator |
| [[KYNU]] | 0.747 | kynureninase |
| [[BICC1]] | 0.719 | BicC family RNA binding protein 1 |
| [[CSGALNACT1]] | 0.711 | chondroitin sulfate N-acetylgalactosaminyltransferase 1 |
| [[PLD1]] | 0.709 | phospholipase D1 |
| [[PTGES]] | 0.695 | prostaglandin E synthase |
| [[RHCG]] | 0.673 | Rh family C glycoprotein |
| [[C1R]] | 0.667 | complement C1r |
| [[DPYD]] | 0.660 | dihydropyrimidine dehydrogenase |
| [[SLC16A7]] | 0.627 | solute carrier family 16 member 7 |
| [[ODF3B]] | 0.621 | ciliary microtubule associated protein 1B |
| [[TNIP3]] | 0.594 | TNFAIP3 interacting protein 3 |
| [[GPR37]] | 0.580 | G protein-coupled receptor 37 |
| [[HTRA3]] | 0.552 | HtrA serine peptidase 3 |
| [[LIFR]] | 0.531 | LIF receptor subunit alpha |
| [[ATP10A]] | 0.501 | ATPase phospholipid transporting 10A (putative) |
| [[UGCG]] | 0.495 | UDP-glucose ceramide glucosyltransferase |
| [[THEMIS2]] | 0.478 | thymocyte selection associated family member 2 |
| [[RUNX2]] | 0.469 | RUNX family transcription factor 2 |
| [[LINC01348]] | 0.467 | long independently transcribed non-coding RNA 1348 |
| [[SIPA1L2]] | 0.419 | signal induced proliferation associated 1 like 2 |
| [[SNX6]] | 0.373 | sorting nexin 6 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 167; `graph/modules.parquet` — module == 167; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [166] (drug-dose × line)
