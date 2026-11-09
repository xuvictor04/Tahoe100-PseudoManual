---
module: 87
type: "module"
n_genes: 51
n_plus: 51
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 087

*51 genes (single-armed) · [[Module 087.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 86), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM (+12.6, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (+10.0, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (+9.6, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+7.5, ⚠ toxic; transcription drop; cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (+5.3); [[Epirubicin (hydrochloride) (drug)]] 5 µM (+3.4, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 5 µM (+3.3, ⚠ cell-cycle shift); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (+3.2, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 0.5 µM (+3.1, ⚠ cell-cycle shift); [[Docetaxel (drug)]] 0.05 µM (+3.0, ⚠ transcription drop; cell-cycle shift); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+2.9); [[Auranofin (drug)]] 5 µM (+2.9); [[Ipatasertib (drug)]] 0.5 µM (+2.5); [[XRK3F2 (drug)]] 0.5 µM (+1.8); [[Thymol (drug)]] 0.5 µM (+1.7); [[Carbamazepine (drug)]] 5 µM (+1.6); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM (+1.5); [[9-ING-41 (drug)]] 0.5 µM (+1.5); [[Glycyrrhizic acid (drug)]] 0.05 µM (+1.5) (69 in all, 25 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)
- Lower it: [[Digitoxin (drug)]] 0.5 µM (-2.1, ⚠ cell-cycle shift); [[Artesunate (drug)]] 0.5 µM (-2.0); [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM (-1.9); [[Lucanthone (drug)]] 0.05 µM (-1.9); [[Rutin (trihydrate) (drug)]] 0.05 µM (-1.7); [[Adagrasib (drug)]] 0.05 µM (-1.6, ⚠ position not correctable); [[Harringtonine (drug)]] 0.5 µM (-1.6, ⚠ cell-cycle shift); [[Fenofibrate (drug)]] 0.05 µM (-1.6); [[Diphenhydramine (drug)]] 0.05 µM (-1.6); [[(S)-Crizotinib (drug)]] 0.05 µM (-1.5); [[Asciminib (drug)]] 0.05 µM (-1.5); [[Tirabrutinib (drug)]] 0.05 µM (-1.4); [[Mebendazole (drug)]] 5 µM (-1.4) (51 in all, 7 with an alert ⚠; shown: the 10 strongest and the 3 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[NCI-H23 (line)]], [[C32 (line)]], [[SNU-1 (line)]], [[RKO (line)]], [[SK-MEL-2 (line)]], [[LoVo (line)]], [[A-427 (line)]], [[AN3 CA (line)]]

## + arm (51)

| Gene | Projection | Name |
|---|---|---|
| [[SOX10]] | 0.885 | SRY-box transcription factor 10 |
| [[C10orf90]] | 0.877 | chromosome 10 open reading frame 90 |
| [[LEF1-AS1]] | 0.874 | LEF1 antisense RNA 1 |
| [[A2M]] | 0.854 | alpha-2-macroglobulin |
| [[SAMMSON]] | 0.850 | survival associated mitochondrial melanoma specific oncogenic non-coding RNA |
| [[MIR3681HG]] | 0.840 | MIR3681 host gene |
| [[COL19A1]] | 0.838 | collagen type XIX alpha 1 chain |
| [[LEF1]] | 0.807 | lymphoid enhancer binding factor 1 |
| [[LHFPL3-AS1]] | 0.787 | LHFPL3 antisense RNA 1 |
| [[PI15]] | 0.778 | peptidase inhibitor 15 |
| [[CTTNBP2]] | 0.759 | cortactin binding protein 2 |
| [[RMEL3]] | 0.750 | enriched in melanoma 3 |
| [[RHOJ]] | 0.749 | ras homolog family member J |
| [[FCRLA]] | 0.749 | Fc receptor like A |
| [[TYR]] | 0.737 | tyrosinase |
| [[MDGA2]] | 0.732 | MAM domain containing glycosylphosphatidylinositol anchor 2 |
| [[TRPM8]] | 0.726 | transient receptor potential cation channel subfamily M member 8 |
| [[LINC02566]] | 0.722 | long independently transcribed non-coding RNA 2566 |
| [[LINC02941]] | 0.720 | long independently transcribed non-coding RNA 2941 |
| [[AEBP1]] | 0.719 | AE binding protein 1 |
| [[GAS7]] | 0.708 | growth arrest specific 7 |
| [[FKBP9P1-1]] | 0.705 | — |
| [[CD96]] | 0.703 | CD96 molecule |
| [[LOXL3]] | 0.695 | lysyl oxidase like 3 |
| [[EFR3B]] | 0.683 | EFR3 homolog B |
| [[LINC01205]] | 0.677 | long independently transcribed non-coding RNA 1205 |
| [[LINC02226]] | 0.674 | long independently transcribed non-coding RNA 2226 |
| [[NLGN4X]] | 0.665 | neuroligin 4 X-linked |
| [[PTPRZ1]] | 0.662 | protein tyrosine phosphatase receptor type Z1 |
| [[EDNRB]] | 0.657 | endothelin receptor type B |
| [[TF]] | 0.655 | transferrin |
| [[ARNT2]] | 0.652 | aryl hydrocarbon receptor nuclear translocator 2 |
| [[ARNT2-DT]] | 0.651 | ARNT2 divergent transcript |
| [[STAG3]] | 0.650 | STAG3 cohesin complex component |
| [[NYAP2]] | 0.637 | neuronal tyrosine-phosphorylated phosphoinositide-3-kinase adaptor 2 |
| [[TDRD9]] | 0.616 | tudor domain containing 9 |
| [[LOXL4]] | 0.614 | lysyl oxidase like 4 |
| [[FZD1]] | 0.609 | frizzled class receptor 1 |
| [[LINC01812]] | 0.604 | long independently transcribed non-coding RNA 1812 |
| [[PLEKHS1]] | 0.602 | pleckstrin homology domain containing S1 |
| [[SHROOM4]] | 0.597 | shroom family member 4 |
| [[OPRD1]] | 0.565 | opioid receptor delta 1 |
| [[GLDC]] | 0.561 | glycine decarboxylase |
| [[PANTR1]] | 0.559 | POU3F3 adjacent non-coding transcript 1 |
| [[NRG3]] | 0.557 | neuregulin 3 |
| [[NTRK2]] | 0.547 | neurotrophic receptor tyrosine kinase 2 |
| [[LINC02343]] | 0.541 | long independently transcribed non-coding RNA 2343 |
| [[TNC]] | 0.504 | tenascin C |
| [[APOD]] | 0.499 | apolipoprotein D |
| [[MSRB3-AS1]] | 0.437 | MSRB3 antisense RNA 1 |
| [[TMEM229B]] | 0.382 | transmembrane protein 229B |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 87; `graph/modules.parquet` — module == 87; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [86] (drug-dose × line)
