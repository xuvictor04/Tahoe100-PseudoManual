---
module: 164
type: "module"
n_genes: 26
n_plus: 26
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.3657732307910919
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 164

*26 genes (single-armed) · [[Module 164.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.37; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 163), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[TAK-901 (drug)]] 5 µM (+4.7, ⚠ cell-cycle shift); [[PH-797804 (drug)]] 5 µM (+2.7); [[Dimethyl fumarate (drug)]] 5 µM (+2.3); [[Fumaric acid (drug)]] 5 µM (+2.1); [[Radotinib (drug)]] 5 µM (+2.1); [[PF-06260933 (drug)]] 5 µM (+2.0); [[Roxadustat (drug)]] 5 µM (+1.7); [[Pravastatin (sodium) (drug)]] 5 µM (+1.7); [[Tomivosertib (drug)]] 5 µM (+1.6); [[Verteporfin (drug)]] 5 µM (+1.5); [[Abemaciclib (drug)]] 0.5 µM (+1.5) (35 in all, 5 with an alert ⚠; shown: the 10 strongest and the 1 next strongest without an alert)
- Lower it: [[Homoharringtonine (drug)]] 5 µM (-12.5, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-8.3, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (-8.0, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (-7.9, ⚠ toxic; transcription drop; cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-7.4, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (-7.0, ⚠ toxic; transcription drop; cell-cycle shift); [[Niclosamide (olamine) (drug)]] 5 µM (-6.5, ⚠ toxic; cell-cycle shift); [[Topotecan (hydrochloride) (drug)]] 5 µM (-4.0, ⚠ toxic; cell-cycle shift); [[Belumosudil (drug)]] 5 µM (-3.7); [[Selinexor (drug)]] 5 µM (-3.5, ⚠ cell-cycle shift); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (-2.7); [[Auranofin (drug)]] 5 µM (-2.6); [[5-Azacytidine (drug)]] 5 µM (-2.4); [[Temsirolimus (drug)]] 0.05 µM (-2.2); [[Retinoic acid (drug)]] 0.05 µM (-2.2); [[Rapamycin (drug)]] 5 µM (-2.0); [[Busulfan (drug)]] 0.05 µM (-1.7); [[Clobetasol propionate (drug)]] 0.05 µM (-1.7); [[Palmatine (chloride) (drug)]] 0.05 µM (-1.7) (66 in all, 21 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[C32 (line)]], [[A-172 (line)]], [[NCI-H460 (line)]], [[LOX-IMVI (line)]], [[NCI-H1792 (line)]], [[SK-MEL-2 (line)]], [[CFPAC-1 (line)]], [[NCI-H1573 (line)]]

## + arm (26)

| Gene | Projection | Name |
|---|---|---|
| [[PEX3]] | 0.877 | peroxisomal biogenesis factor 3 |
| [[WDR45B]] | 0.857 | WD repeat domain 45B |
| [[SNAPC3]] | 0.848 | small nuclear RNA activating complex polypeptide 3 |
| [[UBE2O]] | 0.836 | ubiquitin conjugating enzyme E2 O |
| [[USP37]] | 0.836 | ubiquitin specific peptidase 37 |
| [[HERC3]] | 0.827 | HECT and RLD domain containing E3 ubiquitin protein ligase 3 |
| [[CNOT8]] | 0.812 | CCR4-NOT transcription complex subunit 8 |
| [[SMAP2]] | 0.810 | small ArfGAP2 |
| [[PLEKHA2]] | 0.802 | pleckstrin homology domain containing A2 |
| [[YEATS2]] | 0.801 | YEATS domain containing 2 |
| [[HDHD5]] | 0.774 | haloacid dehalogenase like hydrolase domain containing 5 |
| [[RAB20]] | 0.766 | RAB20, member RAS oncogene family |
| [[TRMU]] | 0.737 | tRNA mitochondrial 2-thiouridylase |
| [[GGA2]] | 0.736 | golgi associated, gamma adaptin ear containing, ARF binding protein 2 |
| [[GPR155]] | 0.731 | G protein-coupled receptor 155 |
| [[LNPK]] | 0.727 | lunapark, ER junction formation factor |
| [[HELZ]] | 0.720 | helicase with zinc finger |
| [[XPNPEP1]] | 0.716 | X-prolyl aminopeptidase 1 |
| [[USP28]] | 0.688 | ubiquitin specific peptidase 28 |
| [[RNASET2]] | 0.682 | ribonuclease T2 |
| [[PMS2CL]] | 0.680 | PMS2 C-terminal like (pseudogene) |
| [[PGRMC2]] | 0.585 | progesterone receptor membrane component 2 |
| [[MYH10]] | 0.566 | myosin heavy chain 10 |
| [[TJP1]] | -0.529 | tight junction protein 1 |
| [[ZNF331]] | 0.488 | zinc finger protein 331 |
| [[VAPB]] | 0.428 | VAMP associated protein B and C |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 164; `graph/modules.parquet` — module == 164; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [163] (drug-dose × line)
