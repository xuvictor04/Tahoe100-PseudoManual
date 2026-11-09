---
module: 124
type: "module"
n_genes: 39
n_plus: 33
n_minus: 6
arms_opposite: true
mean_cos_between_arms: -0.3960808217525482
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 124

*39 genes (33 in the + arm, 6 in the − arm) · [[Module 124.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40). The + arm rises where the − arm falls. Arm = the side of the module's main direction a gene sits on.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of the + arm minus the − arm (`graph/module_pooled_z.npy`, row 123), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it (+ arm up, − arm down): [[Idarubicin (hydrochloride) (drug)]] 5 µM (+15.4, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (+9.5, ⚠ cell-cycle shift); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (+8.3, ⚠ cell-cycle shift); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+7.1); [[Ouabain (Octahydrate) (drug)]] 5 µM (+6.3, ⚠ cell-cycle shift); [[Topotecan (hydrochloride) (drug)]] 5 µM (+6.2, ⚠ toxic; cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (+6.0, ⚠ cell-cycle shift); [[Epirubicin (hydrochloride) (drug)]] 5 µM (+5.7, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 0.5 µM (+5.6, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 5 µM (+5.4, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.05 µM (+5.2); [[Auranofin (drug)]] 5 µM (+4.3); [[Belumosudil (drug)]] 5 µM (+3.9); [[Clobetasol propionate (drug)]] 0.05 µM (+3.4); [[5-Azacytidine (drug)]] 5 µM (+3.2); [[Temsirolimus (drug)]] 0.05 µM (+2.8); [[c-Kit-IN-1 (drug)]] 5 µM (+2.4); [[TAK-901 (drug)]] 0.05 µM (+2.4); [[Brimonidine (drug)]] 5 µM (+2.3) (130 in all, 34 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)
- Lower it: [[Panobinostat (drug)]] 0.5 µM (-15.8, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (-15.0, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (-13.7, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (-8.2, ⚠ cell-cycle shift); [[Belinostat (drug)]] 0.5 µM (-6.3, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (-5.5); [[Brivudine (drug)]] 5 µM (-5.2); [[TAK-901 (drug)]] 5 µM (-3.0, ⚠ cell-cycle shift); [[Docetaxel (drug)]] 0.05 µM (-2.9, ⚠ transcription drop; cell-cycle shift); [[Radotinib (drug)]] 5 µM (-2.5); [[Niclosamide (olamine) (drug)]] 0.5 µM (-2.2); [[HI-TOPK-032 (drug)]] 5 µM (-2.1); [[Cloxacillin (sodium) (drug)]] 0.05 µM (-1.8); [[Ipatasertib (drug)]] 0.05 µM (-1.8); [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM (-1.8); [[Terfenadine (drug)]] 0.5 µM (-1.7); [[Allopurinol (drug)]] 0.05 µM (-1.7) (106 in all, 17 with an alert ⚠; shown: the 10 strongest and the 7 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[SW480 (line)]], [[MIA PaCa-2 (line)]], [[PANC-1 (line)]], [[NCI-H460 (line)]], [[Panc 03.27 (line)]], [[LoVo (line)]], [[KATO III (line)]], [[Hs 766T (line)]]

## + arm (33)

| Gene | Projection | Name |
|---|---|---|
| [[GABPB1-AS1]] | 0.842 | GABPB1 antisense RNA 1 |
| [[AVEN]] | 0.839 | apoptosis and caspase activation inhibitor |
| [[ITPA]] | 0.835 | inosine triphosphatase |
| [[DPH5-DT]] | 0.834 | DPH5 divergent transcript |
| [[EPM2A]] | 0.829 | EPM2A glucan phosphatase, laforin |
| [[RXYLT1]] | 0.824 | ribitol xylosyltransferase 1 |
| [[CRPPA]] | 0.804 | CDP-L-ribitol pyrophosphorylase A |
| [[ADCK1]] | 0.800 | aarF domain containing kinase 1 |
| [[ZNF337-AS1]] | 0.790 | ZNF337 antisense RNA 1 |
| [[GABPB1]] | 0.764 | GA binding protein transcription factor subunit beta 1 |
| [[PRDM5]] | 0.762 | PR/SET domain 5 |
| [[POU6F1]] | 0.759 | POU class 6 homeobox 1 |
| [[SLC16A1-AS1]] | 0.743 | SLC16A1 antisense RNA 1 |
| [[MSANTD2]] | 0.739 | Myb/SANT DNA binding domain containing 2 |
| [[ANKRD18A]] | 0.739 | ankyrin repeat domain 18A |
| [[ARSB]] | 0.735 | arylsulfatase B |
| [[MYLK-AS1]] | 0.718 | MYLK antisense RNA 1 |
| [[PCBD2]] | 0.704 | pterin-4 alpha-carbinolamine dehydratase 2 |
| [[TMEM117]] | 0.691 | transmembrane protein 117 |
| [[HACD1]] | 0.684 | 3-hydroxyacyl-CoA dehydratase 1 |
| [[HSPBAP1]] | 0.673 | HSPB1 associated protein 1 |
| [[PYCR2]] | 0.667 | pyrroline-5-carboxylate reductase 2 |
| [[FAM86HP]] | 0.658 | family with sequence similarity 86 member H, pseudogene |
| [[HDGFL3]] | 0.641 | HDGF like 3 |
| [[TMEM192]] | 0.612 | transmembrane protein 192 |
| [[ENOSF1]] | 0.605 | enolase superfamily member 1 |
| [[SUSD1]] | 0.565 | sushi domain containing 1 |
| [[GATC]] | 0.562 | glutamyl-tRNA amidotransferase subunit C |
| [[RUFY3]] | 0.533 | RUN and FYVE domain containing 3 |
| [[TRIM66]] | 0.493 | tripartite motif containing 66 |
| [[MARK1]] | 0.476 | microtubule affinity regulating kinase 1 |
| [[MCOLN3]] | 0.470 | mucolipin TRP cation channel 3 |
| [[GNPDA1]] | 0.342 | glucosamine-6-phosphate deaminase 1 |

## − arm (6)

| Gene | Projection | Name |
|---|---|---|
| [[RAB3A]] | -0.865 | RAB3A, member RAS oncogene family |
| [[HPS3]] | -0.610 | HPS3 biogenesis of lysosomal organelles complex 2 subunit 1 |
| [[TWF2]] | -0.610 | twinfilin actin binding protein 2 |
| [[GDE1]] | -0.593 | glycerophosphodiester phosphodiesterase 1 |
| [[DMBX1]] | -0.511 | diencephalon/mesencephalon homeobox 1 |
| [[ZNF516]] | -0.442 | zinc finger protein 516 |

## Data

- `graph/nodes.parquet` — module == 124; `graph/modules.parquet` — module == 124; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [123] (drug-dose × line)
