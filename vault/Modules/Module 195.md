---
module: 195
type: "module"
n_genes: 17
n_plus: 17
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 195

*17 genes (single-armed) · [[Module 195.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 194), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Tucidinostat (drug)]] 5 µM (+3.5); [[Panobinostat (drug)]] 0.05 µM (+2.6, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (+2.1, ⚠ cell-cycle shift); [[PF-06260933 (drug)]] 5 µM (+1.6); [[Tucidinostat (drug)]] 0.5 µM (+1.5, ⚠ cell-cycle shift); [[PH-797804 (drug)]] 0.05 µM (+1.5); [[Daptomycin (drug)]] 5 µM (+1.4, ⚠ unreliable plate only); [[Belinostat (drug)]] 0.5 µM (+1.4, ⚠ cell-cycle shift); [[Demeclocycline (drug)]] 5 µM (+1.3); [[Brivudine (drug)]] 5 µM (+1.3); [[Pitavastatin (Calcium) (drug)]] 0.5 µM (+1.3); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM (+1.3); [[Bentamapimod (drug)]] 5 µM (+1.3); [[Thymopentin (drug)]] 5 µM (+1.2); [[BAY1125976 (drug)]] 5 µM (+1.2) (41 in all, 11 with an alert ⚠; shown: the 10 strongest and the 5 next strongest without an alert)
- Lower it: [[Homoharringtonine (drug)]] 0.5 µM (-6.8, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 5 µM (-6.8, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-5.2, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (-4.4, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (-4.1, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 5 µM (-3.7, ⚠ toxic; transcription drop; cell-cycle shift); [[Selinexor (drug)]] 5 µM (-3.6, ⚠ cell-cycle shift); [[TAK-901 (drug)]] 5 µM (-3.5, ⚠ cell-cycle shift); [[Trametinib (drug)]] 0.5 µM (-3.5); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM (-3.4); [[Cobimetinib (drug)]] 5 µM (-3.1); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM (-2.9); [[Binimetinib (drug)]] 0.5 µM (-2.9); [[Binimetinib (drug)]] 5 µM (-2.8); [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM (-2.7); [[Cobimetinib (drug)]] 0.5 µM (-2.7); [[Binimetinib (drug)]] 0.05 µM (-2.5); [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM (-2.4) (73 in all, 29 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[LOX-IMVI (line)]], [[LoVo (line)]], [[NCI-H2030 (line)]], [[MIA PaCa-2 (line)]], [[SNU-1 (line)]], [[NCI-H460 (line)]], [[A-427 (line)]], [[HOP62 (line)]]

## + arm (17)

| Gene | Projection | Name |
|---|---|---|
| [[ACOT7]] | 0.820 | acyl-CoA thioesterase 7 |
| [[VAV2]] | 0.819 | vav guanine nucleotide exchange factor 2 |
| [[IGSF9B]] | 0.779 | immunoglobulin superfamily member 9B |
| [[IQSEC1]] | 0.774 | IQ motif and Sec7 domain ArfGEF 1 |
| [[SLCO4A1]] | 0.754 | solute carrier organic anion transporter family member 4A1 |
| [[ATP11A]] | 0.661 | ATPase phospholipid transporting 11A |
| [[GLI2]] | 0.651 | GLI family zinc finger 2 |
| [[PPP2R2C]] | 0.617 | protein phosphatase 2 regulatory subunit Bgamma |
| [[SH3TC2]] | 0.610 | SH3 domain and tetratricopeptide repeats 2 |
| [[FIBCD1]] | 0.595 | fibrinogen C domain containing 1 |
| [[FHOD1]] | 0.594 | formin homology 2 domain containing 1 |
| [[SH3TC2-DT]] | 0.593 | SH3TC2 divergent transcript |
| [[SKI]] | 0.588 | SKI proto-oncogene |
| [[OSBPL10]] | 0.577 | oxysterol binding protein like 10 |
| [[MTCL1]] | 0.543 | microtubule crosslinking factor 1 |
| [[MGAT5B]] | 0.522 | alpha-1,6-mannosylglycoprotein 6-beta-N-acetylglucosaminyltransferase B |
| [[MICAL3]] | 0.480 | microtubule associated monooxygenase, calponin and LIM domain containing 3 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 195; `graph/modules.parquet` — module == 195; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [194] (drug-dose × line)
