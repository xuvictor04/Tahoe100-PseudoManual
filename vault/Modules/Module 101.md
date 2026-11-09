---
module: 101
type: "module"
n_genes: 46
n_plus: 46
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 101

*46 genes (single-armed) · [[Module 101.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 100), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Homoharringtonine (drug)]] 5 µM (+7.2, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (+4.9, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (+4.0, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (+3.6, ⚠ cell-cycle shift); [[Auranofin (drug)]] 5 µM (+3.2); [[Dinaciclib (drug)]] 0.5 µM (+3.2, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+2.9, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (+2.7, ⚠ toxic; transcription drop; cell-cycle shift); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+2.6); [[Harringtonine (drug)]] 0.5 µM (+2.3, ⚠ cell-cycle shift); [[Pitavastatin (Calcium) (drug)]] 0.5 µM (+2.0); [[PF-06260933 (drug)]] 5 µM (+1.8); [[Tucidinostat (drug)]] 5 µM (+1.6); [[Homoharringtonine (drug)]] 0.05 µM (+1.6); [[Peretinoin (drug)]] 5 µM (+1.5); [[5-Azacytidine (drug)]] 5 µM (+1.3); [[Peretinoin (drug)]] 0.5 µM (+1.2); [[Vinblastine (sulfate) (drug)]] 5 µM (+1.2) (31 in all, 16 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)
- Lower it: [[Ponatinib (drug)]] 5 µM (-3.1); [[NG25 (drug)]] 5 µM (-3.1, ⚠ cell-cycle shift); [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM (-2.7); [[Trametinib (drug)]] 5 µM (-2.6, ⚠ cell-cycle shift); [[Trametinib (drug)]] 0.5 µM (-2.6); [[Binimetinib (drug)]] 0.5 µM (-2.5); [[Belinostat (drug)]] 5 µM (-2.4, ⚠ cell-cycle shift); [[Cobimetinib (drug)]] 5 µM (-2.4); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM (-2.4); [[Panobinostat (drug)]] 0.5 µM (-2.2, ⚠ cell-cycle shift); [[Elimusertib hydrochloride (drug)]] 0.05 µM (-2.2); [[Radotinib (drug)]] 5 µM (-2.2); [[Trametinib (drug)]] 0.05 µM (-2.2); [[Binimetinib (drug)]] 5 µM (-2.1) (41 in all, 10 with an alert ⚠; shown: the 10 strongest and the 4 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[NCI-H460 (line)]], [[HOP62 (line)]], [[MIA PaCa-2 (line)]], [[A498 (line)]], [[AsPC-1 (line)]], [[NCI-H1573 (line)]], [[SW 900 (line)]], [[PANC-1 (line)]]

## + arm (46)

| Gene | Projection | Name |
|---|---|---|
| [[NOP14-AS1]] | 0.851 | NOP14 antisense RNA 1 |
| [[STK10]] | 0.788 | serine/threonine kinase 10 |
| [[C11orf91]] | 0.758 | chromosome 11 open reading frame 91 |
| [[PHLDA2]] | 0.757 | pleckstrin homology like domain family A member 2 |
| [[CLCF1]] | 0.745 | cardiotrophin like cytokine factor 1 |
| [[SERPINB8]] | 0.730 | serpin family B member 8 |
| [[ITGA2-AS1]] | 0.720 | ITGA2 antisense RNA 1 |
| [[LUCAT1]] | 0.718 | lung cancer associated transcript 1 |
| [[FAM83G]] | 0.714 | scaffolding CK1 anchoring protein G |
| [[GPATCH2L]] | 0.712 | G-patch domain containing 2 like |
| [[PPP1R14B-AS1]] | 0.709 | PPP1R14B antisense RNA 1 |
| [[ABR]] | 0.704 | ABR activator of RhoGEF and GTPase |
| [[S100A11]] | 0.703 | S100 calcium binding protein A11 |
| [[HOMER1]] | 0.693 | homer scaffold protein 1 |
| [[HCG20]] | 0.684 | HLA complex group 20 |
| [[SOWAHC]] | 0.681 | sosondowah ankyrin repeat domain family member C |
| [[KDM7A-DT]] | 0.663 | KDM7A divergent transcript |
| [[WNT9A]] | 0.646 | Wnt family member 9A |
| [[FAM131B-AS2]] | 0.644 | FAM131B antisense RNA 2 |
| [[CACNG8]] | 0.643 | calcium voltage-gated channel auxiliary subunit gamma 8 |
| [[LAMB3]] | 0.638 | laminin subunit beta 3 |
| [[JOSD1]] | 0.632 | Josephin domain containing 1 |
| [[TRPV3]] | 0.612 | transient receptor potential cation channel subfamily V member 3 |
| [[CYFIP1]] | 0.610 | cytoplasmic FMR1 interacting protein 1 |
| [[GNG4]] | 0.603 | G protein subunit gamma 4 |
| [[TEP1]] | 0.598 | telomerase associated protein 1 |
| [[RAP1B]] | 0.597 | RAP1B, member of RAS oncogene family |
| [[ERRFI1-DT]] | 0.587 | ERRFI1 divergent transcript |
| [[RAPH1]] | 0.581 | Ras association (RalGDS/AF-6) and pleckstrin homology domains 1 |
| [[ATP13A3-DT]] | 0.575 | ATP13A3 divergent transcript |
| [[ADGRL1-AS1]] | 0.570 | ADGRL1 antisense RNA 1 |
| [[S100A2]] | 0.548 | S100 calcium binding protein A2 |
| [[KLHL21]] | 0.542 | kelch like family member 21 |
| [[PPP1R18]] | 0.520 | protein phosphatase 1 regulatory subunit 18 |
| [[ATP2C2-AS1]] | 0.513 | ATP2C2 antisense RNA 1 |
| [[PPP4R1L]] | 0.498 | protein phosphatase 4 regulatory subunit 1 like (pseudogene) |
| [[MYO1C]] | 0.492 | myosin IC |
| [[SLC12A4]] | 0.491 | solute carrier family 12 member 4 |
| [[OSMR-DT]] | 0.484 | OSMR divergent transcript |
| [[SERPINB9]] | 0.463 | serpin family B member 9 |
| [[S100A6]] | 0.462 | S100 calcium binding protein A6 |
| [[IL1RL1]] | 0.454 | interleukin 33 receptor |
| [[CLTB]] | 0.441 | clathrin light chain B |
| [[SEPTIN9]] | 0.435 | septin 9 |
| [[ARHGAP23]] | 0.396 | Rho GTPase activating protein 23 |
| [[BTBD10]] | 0.390 | BTB domain containing 10 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 101; `graph/modules.parquet` — module == 101; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [100] (drug-dose × line)
