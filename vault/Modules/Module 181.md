---
module: 181
type: "module"
n_genes: 22
n_plus: 22
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 181

*22 genes (single-armed) · [[Module 181.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 180), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Homoharringtonine (drug)]] 5 µM (+18.8, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (+9.5, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (+8.1, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (+6.6, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (+4.6, ⚠ toxic; transcription drop; cell-cycle shift); [[Auranofin (drug)]] 5 µM (+4.6); [[Dinaciclib (drug)]] 0.05 µM (+4.2, ⚠ toxic; transcription drop; cell-cycle shift); [[Tucidinostat (drug)]] 0.5 µM (+2.4, ⚠ cell-cycle shift); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (+2.4, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (+2.4, ⚠ toxic; transcription drop; cell-cycle shift); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+2.3); [[Filgotinib (drug)]] 5 µM (+2.0); [[Tucidinostat (drug)]] 5 µM (+2.0); [[PF-06260933 (drug)]] 5 µM (+1.9); [[Thymol (drug)]] 0.5 µM (+1.5); [[Cobimetinib (drug)]] 5 µM (+1.5); [[TAK-901 (drug)]] 0.05 µM (+1.4); [[Cepharanthine (drug)]] 5 µM (+1.4); [[Ipatasertib (drug)]] 0.5 µM (+1.4) (40 in all, 18 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)
- Lower it: [[Panobinostat (drug)]] 0.5 µM (-4.0, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (-3.9, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (-3.4, ⚠ cell-cycle shift); [[NG25 (drug)]] 5 µM (-2.6, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 0.5 µM (-1.6, ⚠ cell-cycle shift); [[Berbamine (drug)]] 0.05 µM (-1.5); [[Brivudine (drug)]] 5 µM (-1.5); [[Belumosudil (drug)]] 5 µM (-1.4); [[Betamethasone dipropionate (drug)]] 5 µM (-1.4); [[Dexamethasone (drug)]] 0.5 µM (-1.4); [[Radotinib (drug)]] 5 µM (-1.3); [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM (-1.3); [[Dexamethasone (drug)]] 5 µM (-1.3); [[Pralsetinib (drug)]] 5 µM (-1.3); [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM (-1.3) (27 in all, 7 with an alert ⚠; shown: the 10 strongest and the 5 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[A-172 (line)]], [[PANC-1 (line)]], [[SK-MEL-2 (line)]], [[NCI-H460 (line)]], [[NCI-H1573 (line)]], [[RPMI-7951 (line)]], [[HS-578T (line)]], [[HOP62 (line)]]

## + arm (22)

| Gene | Projection | Name |
|---|---|---|
| [[IL34]] | 0.872 | interleukin 34 |
| [[NLGN3]] | 0.865 | neuroligin 3 |
| [[COL11A2]] | 0.861 | collagen type XI alpha 2 chain |
| [[TGIF2-RAB5IF]] | 0.808 | TGIF2-RAB5IF readthrough |
| [[MSANTD3-TMEFF1]] | 0.794 | MSANTD3-TMEFF1 readthrough |
| [[NPHS1]] | 0.770 | NPHS1 adhesion molecule, nephrin |
| [[CCDC17]] | 0.739 | coiled-coil domain containing 17 |
| [[PIK3IP1-DT]] | 0.736 | PIK3IP1 divergent transcript |
| [[NFATC1]] | 0.729 | nuclear factor of activated T cells 1 |
| [[AGER]] | 0.725 | advanced glycosylation end-product specific receptor |
| [[KCNN1]] | 0.717 | potassium calcium-activated channel subfamily N member 1 |
| [[SCARF1]] | 0.713 | scavenger receptor class F member 1 |
| [[YJEFN3]] | 0.696 | YjeF N-terminal domain containing 3 |
| [[NPR2]] | 0.696 | natriuretic peptide receptor 2 |
| [[MC1R]] | 0.685 | melanocortin 1 receptor |
| [[MATN1-AS1]] | 0.662 | MATN1 antisense RNA 1 |
| [[PAQR6]] | 0.639 | progestin and adipoQ receptor family member 6 |
| [[ARL14EPL]] | 0.635 | ARF like GTPase 14 effector protein like |
| [[KCNQ4]] | 0.628 | potassium voltage-gated channel subfamily Q member 4 |
| [[TMEFF1]] | 0.588 | transmembrane protein with EGF like and two follistatin like domains 1 |
| [[CYP27B1]] | 0.546 | cytochrome P450 family 27 subfamily B member 1 |
| [[AMPD3]] | 0.486 | adenosine monophosphate deaminase 3 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 181; `graph/modules.parquet` — module == 181; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [180] (drug-dose × line)
