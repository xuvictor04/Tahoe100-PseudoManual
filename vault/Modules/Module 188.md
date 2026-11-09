---
module: 188
type: "module"
n_genes: 18
n_plus: 18
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.4467933177947998
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 188

*18 genes (single-armed) · [[Module 188.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.45; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 187), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Belinostat (drug)]] 5 µM (+4.2, ⚠ cell-cycle shift); [[Niclosamide (olamine) (drug)]] 5 µM (+4.0, ⚠ toxic; cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (+3.3); [[Selinexor (drug)]] 5 µM (+3.2, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (+3.1, ⚠ toxic; transcription drop; cell-cycle shift); [[Panobinostat (drug)]] 5 µM (+3.1, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (+2.9, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+2.9, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (+2.8, ⚠ toxic; transcription drop; cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (+2.8, ⚠ cell-cycle shift); [[Brivudine (drug)]] 5 µM (+2.5); [[Vinblastine (sulfate) (drug)]] 5 µM (+2.2); [[Neratinib (maleate) (drug)]] 5 µM (+2.0); [[Radotinib (drug)]] 5 µM (+1.9); [[Neratinib (drug)]] 5 µM (+1.9); [[PH-797804 (drug)]] 5 µM (+1.8); [[Ponatinib (drug)]] 5 µM (+1.6); [[Flumatinib (mesylate) (drug)]] 5 µM (+1.6); [[Belumosudil (drug)]] 5 µM (+1.5) (48 in all, 24 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)
- Lower it: [[Homoharringtonine (drug)]] 5 µM (-3.7, ⚠ cell-cycle shift); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (-2.1); [[Idarubicin (hydrochloride) (drug)]] 5 µM (-1.6, ⚠ cell-cycle shift); [[(S)-Crizotinib (drug)]] 0.5 µM (-1.6); [[Estrone sulfate (potassium) (drug)]] 5 µM (-1.4); [[Filgotinib (drug)]] 5 µM (-1.4); [[Esmolol (hydrochloride) (drug)]] 5 µM (-1.4); [[Lactate (calcium) (drug)]] 0.5 µM (-1.4); [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM (-1.4); [[Diphenhydramine (drug)]] 0.5 µM (-1.4); [[Filgotinib (drug)]] 0.05 µM (-1.4); [[Demeclocycline (drug)]] 5 µM (-1.4) (24 in all, 4 with an alert ⚠; shown: the 10 strongest and the 2 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[LoVo (line)]], [[NCI-H460 (line)]], [[PANC-1 (line)]], [[NCI-H1573 (line)]], [[SK-MEL-2 (line)]], [[NCI-H23 (line)]], [[NCI-H2030 (line)]], [[LOX-IMVI (line)]]

*⚠ 1 of its 18 genes are in the vector space only through drug-doses that carry an alert (`embed/genes.parquet` evidence_flagged_only): their place here may reflect what those drug-doses did to the cells. They are marked in the tables of this note.*

## + arm (18)

| Gene | Projection | Name | Alert |
|---|---|---|---|
| [[FAR1]] | 0.865 | fatty acyl-CoA reductase 1 |  |
| [[GPD1L]] | 0.799 | glycerol-3-phosphate dehydrogenase 1 like |  |
| [[GCSH]] | 0.790 | glycine cleavage system protein H |  |
| [[METAP1]] | 0.765 | methionyl aminopeptidase 1 |  |
| [[RBBP6]] | -0.764 | RB binding protein 6, ubiquitin ligase |  |
| [[OTUD6B]] | 0.758 | OTU deubiquitinase 6B |  |
| [[NDFIP1]] | 0.757 | Nedd4 family interacting protein 1 |  |
| [[GNPTAB]] | 0.757 | N-acetylglucosamine-1-phosphate transferase subunits alpha and beta |  |
| [[RFXAP]] | 0.756 | regulatory factor X associated protein |  |
| [[MBD2]] | 0.743 | methyl-CpG binding domain protein 2 |  |
| [[MCUR1]] | 0.723 | mitochondrial calcium uniporter regulator 1 | ⚠ only flagged evidence |
| [[AKTIP]] | 0.709 | AKT interacting protein |  |
| [[RNF2]] | 0.677 | ring finger protein 2 |  |
| [[GRB14]] | 0.648 | growth factor receptor bound protein 14 |  |
| [[OLA1]] | 0.624 | Obg like ATPase 1 |  |
| [[SYS1]] | -0.563 | SYS1 golgi trafficking protein |  |
| [[CSNK1G3]] | 0.555 | casein kinase 1 gamma 3 |  |
| [[RCAN3]] | 0.523 | regulator of calcineurin 3 |  |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 188; `graph/modules.parquet` — module == 188; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [187] (drug-dose × line)
