---
module: 178
type: "module"
n_genes: 22
n_plus: 22
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.35879212617874146
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 178

*22 genes (single-armed) · [[Module 178.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 177), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[TAK-901 (drug)]] 5 µM (+3.8, ⚠ cell-cycle shift); [[Selinexor (drug)]] 5 µM (+3.6, ⚠ cell-cycle shift); [[PH-797804 (drug)]] 5 µM (+2.9); [[Bortezomib (drug)]] 0.05 µM (+2.6, ⚠ cell-cycle shift); [[NG25 (drug)]] 5 µM (+2.0, ⚠ cell-cycle shift); [[Selinexor (drug)]] 0.5 µM (+1.9, ⚠ cell-cycle shift); [[Ixazomib citrate (drug)]] 5 µM (+1.8, ⚠ cell-cycle shift); [[Ponatinib (drug)]] 5 µM (+1.6); [[Anethole trithione (drug)]] 5 µM (+1.3, ⚠ cell-cycle shift); [[Radotinib (drug)]] 5 µM (+1.2); [[Verteporfin (drug)]] 5 µM (+1.2); [[Ixazomib citrate (drug)]] 0.5 µM (+1.2); [[Cabozantinib (S-malate) (drug)]] 5 µM (+1.1) (14 in all, 8 with an alert ⚠; shown: the 10 strongest and the 3 next strongest without an alert)
- Lower it: [[Dinaciclib (drug)]] 0.5 µM (-5.3, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (-4.5, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (-3.9, ⚠ toxic; transcription drop; cell-cycle shift); [[Homoharringtonine (drug)]] 5 µM (-3.7, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-3.3, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-2.5, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (-2.3, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (-2.3); [[Idarubicin (hydrochloride) (drug)]] 5 µM (-2.2, ⚠ cell-cycle shift); [[c-Kit-IN-1 (drug)]] 0.05 µM (-2.2, ⚠ unreliable plate only); [[Filgotinib (drug)]] 5 µM (-1.3); [[Peretinoin (drug)]] 5 µM (-1.2); [[Homoharringtonine (drug)]] 0.05 µM (-1.1); [[Mifepristone (drug)]] 0.5 µM (-1.1); [[Auranofin (drug)]] 5 µM (-1.0); [[Larotrectinib (drug)]] 0.05 µM (-1.0); [[Diphenhydramine (drug)]] 0.5 µM (-1.0); [[Palmatine (chloride) (drug)]] 0.05 µM (-1.0) (24 in all, 15 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[RKO (line)]], [[SW480 (line)]], [[A-427 (line)]], [[HS-578T (line)]], [[LoVo (line)]], [[hTERT-HPNE (line)]], [[HOP62 (line)]], [[NCI-H2347 (line)]]

## + arm (22)

| Gene | Projection | Name |
|---|---|---|
| [[ASB7]] | 0.892 | ankyrin repeat and SOCS box containing 7 |
| [[TENT2]] | 0.829 | terminal nucleotidyltransferase 2 |
| [[MED23]] | 0.818 | mediator complex subunit 23 |
| [[C12orf76]] | 0.806 | chromosome 12 open reading frame 76 |
| [[NDUFB7]] | 0.805 | NADH:ubiquinone oxidoreductase subunit B7 |
| [[COX16]] | 0.781 | cytochrome c oxidase assembly factor COX16 |
| [[SPATA7]] | 0.735 | spermatogenesis associated 7 |
| [[ZNF224]] | 0.719 | zinc finger protein 224 |
| [[TTC9C]] | 0.712 | tetratricopeptide repeat domain 9C |
| [[FAM185BP]] | 0.686 | family with sequence similarity 185 member B, pseudogene |
| [[EID2B]] | 0.668 | EP300 interacting inhibitor of differentiation 2B |
| [[HMBOX1]] | 0.631 | homeobox containing 1 |
| [[TMEM94]] | 0.623 | transmembrane protein 94 |
| [[EYA3]] | 0.614 | EYA transcriptional coactivator and phosphatase 3 |
| [[CACUL1]] | 0.606 | CDK2 associated cullin domain 1 |
| [[PSMG2]] | 0.603 | proteasome assembly chaperone 2 |
| [[STX18]] | 0.598 | syntaxin 18 |
| [[NDUFS2]] | 0.594 | NADH:ubiquinone oxidoreductase core subunit S2 |
| [[AKIRIN1]] | -0.580 | akirin 1 |
| [[LIMS1]] | -0.539 | LIM zinc finger domain containing 1 |
| [[PPIL2]] | 0.508 | peptidylprolyl isomerase like 2 |
| [[ARMCX6]] | 0.447 | armadillo repeat containing X-linked 6 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 178; `graph/modules.parquet` — module == 178; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [177] (drug-dose × line)
