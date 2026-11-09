---
module: 151
type: "module"
n_genes: 29
n_plus: 29
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 151

*29 genes (single-armed) · [[Module 151.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 150), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Homoharringtonine (drug)]] 5 µM (+5.5, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (+4.5, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (+4.0); [[Daptomycin (drug)]] 5 µM (+3.1, ⚠ unreliable plate only); [[TAK-901 (drug)]] 5 µM (+3.1, ⚠ cell-cycle shift); [[Auranofin (drug)]] 5 µM (+3.0); [[Daptomycin (drug)]] 0.5 µM (+3.0, ⚠ unreliable plate only); [[Harringtonine (drug)]] 5 µM (+3.0, ⚠ cell-cycle shift); [[Peretinoin (drug)]] 5 µM (+2.9); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+2.7); [[TAK-901 (drug)]] 0.05 µM (+2.3); [[Busulfan (drug)]] 0.05 µM (+2.1); [[Homoharringtonine (drug)]] 0.05 µM (+2.0); [[Peretinoin (drug)]] 0.5 µM (+1.9); [[Filgotinib (drug)]] 5 µM (+1.9); [[Diphenhydramine (drug)]] 0.5 µM (+1.8) (63 in all, 19 with an alert ⚠; shown: the 10 strongest and the 6 next strongest without an alert)
- Lower it: [[Trametinib (drug)]] 5 µM (-4.1, ⚠ cell-cycle shift); [[Ponatinib (drug)]] 5 µM (-3.8); [[Panobinostat (drug)]] 0.5 µM (-3.8, ⚠ cell-cycle shift); [[Trametinib (drug)]] 0.5 µM (-3.8); [[Panobinostat (drug)]] 5 µM (-3.8, ⚠ cell-cycle shift); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM (-3.4); [[Binimetinib (drug)]] 0.5 µM (-3.2); [[Binimetinib (drug)]] 5 µM (-3.2); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM (-3.1); [[Idarubicin (hydrochloride) (drug)]] 5 µM (-2.8, ⚠ cell-cycle shift); [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM (-2.4); [[Cobimetinib (drug)]] 5 µM (-2.2); [[Triamcinolone (drug)]] 5 µM (-2.1); [[Elimusertib hydrochloride (drug)]] 0.05 µM (-2.1) (55 in all, 14 with an alert ⚠; shown: the 10 strongest and the 4 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[HEC-1-A (line)]], [[MIA PaCa-2 (line)]], [[SK-MEL-2 (line)]], [[C32 (line)]], [[SW480 (line)]], [[RKO (line)]], [[HOP62 (line)]], [[A-172 (line)]]

## + arm (29)

| Gene | Projection | Name |
|---|---|---|
| [[BACH1]] | 0.829 | BACH transcriptional regulator 1 |
| [[SCHIP1]] | 0.825 | schwannomin interacting protein 1 |
| [[MIR100HG]] | 0.803 | mir-100-let-7a-2-mir-125b-1 cluster host gene |
| [[CYTOR]] | 0.789 | cytoskeleton regulator RNA |
| [[DCBLD2]] | 0.778 | discoidin, CUB and LCCL domain containing 2 |
| [[CD44]] | 0.749 | CD44 molecule (IN blood group) |
| [[IQCJ-SCHIP1]] | 0.749 | IQCJ-SCHIP1 readthrough |
| [[MIR4435-2HG]] | 0.734 | MIR4435-2 host gene |
| [[LINC03004]] | 0.715 | long independently transcribed non-coding RNA 3004 |
| [[UBASH3B]] | 0.708 | ubiquitin associated and SH3 domain containing B |
| [[TNFRSF12A]] | 0.697 | TNF receptor superfamily member 12A |
| [[SVIL]] | 0.688 | supervillin |
| [[AMOTL1]] | 0.685 | angiomotin like 1 |
| [[TEAD1]] | 0.677 | TEA domain transcription factor 1 |
| [[ANAPC1P4]] | 0.675 | ANAPC1 pseudogene 4 |
| [[LINC02930]] | 0.649 | long independently transcribed non-coding RNA 2930 |
| [[C12orf75-AS1]] | 0.614 | C12orf75 antisense RNA 1 |
| [[HRH1]] | 0.602 | histamine receptor H1 |
| [[PLPP4]] | 0.599 | phospholipid phosphatase 4 |
| [[NF2]] | 0.565 | NF2, moesin-ezrin-radixin like (MERLIN) tumor suppressor |
| [[ACER3]] | 0.553 | alkaline ceramidase 3 |
| [[CDC42EP3]] | 0.550 | CDC42 effector protein 3 |
| [[SRPX2]] | 0.547 | sushi repeat containing protein X-linked 2 |
| [[TBX3]] | 0.533 | T-box transcription factor 3 |
| [[CDK14]] | 0.517 | cyclin dependent kinase 14 |
| [[ARSJ]] | 0.498 | arylsulfatase family member J |
| [[TLR4]] | 0.483 | toll like receptor 4 |
| [[RGMB]] | 0.466 | repulsive guidance molecule BMP co-receptor b |
| [[RCAN1]] | 0.383 | regulator of calcineurin 1 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 151; `graph/modules.parquet` — module == 151; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [150] (drug-dose × line)
