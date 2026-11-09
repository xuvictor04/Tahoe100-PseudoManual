---
module: 226
type: "module"
n_genes: 9
n_plus: 9
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.5257039070129395
label: "NOTCH2 Activation and Transmission of Signal to the Nucleus"
label_source: "reactome"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 226

*NOTCH2 Activation and Transmission of Signal to the Nucleus · 9 genes (single-armed) · [[Module 226.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.53; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

Label from the validation stage: **NOTCH2 Activation and Transmission of Signal to the Nucleus** (reactome, q 6e-07; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | NOTCH2 Activation and Transmission of Signal to the Nucleus | reactome | 4/9 | 279 | 6e-07 |
| + | NOTCH2 Activation and Transmission of Signal to the Nucleus | reactome | 4/9 | 279 | 6e-07 |
| + | Signaling by NOTCH2 | reactome | 4/9 | 209 | 2e-06 |
| all | Signaling by NOTCH2 | reactome | 4/9 | 209 | 2e-06 |
| + | Pre-NOTCH Transcription and Translation | reactome | 4/9 | 168 | 4e-06 |
| all | Pre-NOTCH Transcription and Translation | reactome | 4/9 | 168 | 4e-06 |
| all | Pre-NOTCH Expression and Processing | reactome | 4/9 | 120 | 2e-05 |
| + | Pre-NOTCH Expression and Processing | reactome | 4/9 | 120 | 2e-05 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 225), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Homoharringtonine (drug)]] 5 µM (+19.4, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (+10.1, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (+6.3, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (+5.5, ⚠ cell-cycle shift); [[TAK-901 (drug)]] 5 µM (+4.8, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 5 µM (+4.3, ⚠ toxic; transcription drop; cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (+3.9, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 0.5 µM (+3.6, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (+2.9); [[Tucidinostat (drug)]] 0.5 µM (+2.7, ⚠ cell-cycle shift); [[GSK1059615 (drug)]] 5 µM (+2.7); [[PH-797804 (drug)]] 5 µM (+2.3); [[Niclosamide (olamine) (drug)]] 0.5 µM (+1.7); [[Glycyrrhizic acid (drug)]] 0.5 µM (+1.6); [[Dihydroartemisinin (drug)]] 5 µM (+1.5); [[Lidocaine (hydrochloride) (drug)]] 0.5 µM (+1.4); [[Pentagastrin (drug)]] 5 µM (+1.4); [[Temsirolimus (drug)]] 0.5 µM (+1.4); [[Pravastatin (sodium) (drug)]] 5 µM (+1.4) (65 in all, 28 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)
- Lower it: [[Dinaciclib (drug)]] 0.5 µM (-8.9, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (-6.2, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (-5.3, ⚠ toxic; transcription drop; cell-cycle shift); [[Topotecan (hydrochloride) (drug)]] 5 µM (-4.6, ⚠ toxic; cell-cycle shift); [[Auranofin (drug)]] 5 µM (-3.1); [[Darinaparsin (drug)]] 5 µM (-3.0, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (-2.7, ⚠ cell-cycle shift); [[Topotecan (hydrochloride) (drug)]] 0.5 µM (-2.6, ⚠ cell-cycle shift); [[Thymol (drug)]] 5 µM (-2.1); [[Clobetasol propionate (drug)]] 0.05 µM (-2.0); [[Berbamine (drug)]] 0.05 µM (-1.7); [[Amsacrine (drug)]] 5 µM (-1.7); [[Riluzole hydrochloride (drug)]] 5 µM (-1.6); [[Betamethasone dipropionate (drug)]] 5 µM (-1.5); [[Arbutin (drug)]] 5 µM (-1.5); [[Palmatine (chloride) (drug)]] 0.05 µM (-1.4); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (-1.4) (57 in all, 15 with an alert ⚠; shown: the 10 strongest and the 7 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[PANC-1 (line)]], [[HEC-1-A (line)]], [[SNU-1 (line)]], [[NCI-H460 (line)]], [[RKO (line)]], [[A498 (line)]], [[A-427 (line)]], [[LoVo (line)]]

## Candidate new members

*Members not annotated to the set their arm is enriched for, ranked by mean cos to the annotated members (`validation/novel_members.csv`); ⚠ = a reason to doubt the gene's place (in the vector space only through flagged drug-doses), kept in its rank. 4 candidates, none with an alert.*

| # | Gene | Set | Mean cos |
|---|---|---|---|
| 1 | [[NBPF26]] | NOTCH2 Activation and Transmission of Signal to the Nucleus | +0.67 |
| 2 | [[NBPF10]] | NOTCH2 Activation and Transmission of Signal to the Nucleus | +0.64 |
| 3 | [[NBPF14]] | NOTCH2 Activation and Transmission of Signal to the Nucleus | +0.61 |
| 4 | [[NBPF19]] | NOTCH2 Activation and Transmission of Signal to the Nucleus | +0.59 |

## + arm (9)

| Gene | Projection | Name |
|---|---|---|
| [[NBPF10]] | 0.920 | NBPF member 10 |
| [[NBPF14]] | 0.887 | NBPF member 14 |
| [[NOTCH2NLA]] | 0.885 | notch 2 N-terminal like A |
| [[NBPF19]] | 0.878 | NBPF member 19 |
| [[NOTCH2NLB]] | 0.854 | notch 2 N-terminal like B |
| [[NBPF26]] | 0.844 | NBPF member 26 |
| [[NOTCH2NLC]] | 0.735 | notch 2 N-terminal like C |
| [[ADPGK]] | -0.698 | ADP dependent glucokinase |
| [[NOTCH2]] | 0.684 | notch receptor 2 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 226; `graph/modules.parquet` — module == 226; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [225] (drug-dose × line)
