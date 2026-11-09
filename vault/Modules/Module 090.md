---
module: 90
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

# Module 090

*51 genes (single-armed) · [[Module 090.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 89), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM (+18.5, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (+11.2, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (+10.6, ⚠ toxic; transcription drop; cell-cycle shift); [[Homoharringtonine (drug)]] 5 µM (+10.1, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+8.9, ⚠ toxic; transcription drop; cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (+7.8); [[Idarubicin (hydrochloride) (drug)]] 0.5 µM (+6.3, ⚠ cell-cycle shift); [[Auranofin (drug)]] 5 µM (+5.1); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+4.9); [[Tucidinostat (drug)]] 0.5 µM (+4.8, ⚠ cell-cycle shift); [[Cobimetinib (drug)]] 5 µM (+2.1); [[Ipatasertib (drug)]] 0.5 µM (+2.0); [[XRK3F2 (drug)]] 0.5 µM (+1.9); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM (+1.9); [[Docetaxel (Trihydrate) (drug)]] 0.5 µM (+1.8); [[Ponatinib (drug)]] 0.5 µM (+1.8); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM (+1.6) (83 in all, 31 with an alert ⚠; shown: the 10 strongest and the 7 next strongest without an alert)
- Lower it: [[Adagrasib (drug)]] 0.05 µM (-2.1, ⚠ position not correctable); [[Lucanthone (drug)]] 0.05 µM (-1.8); [[Artesunate (drug)]] 0.5 µM (-1.6); [[Digitoxin (drug)]] 0.5 µM (-1.5, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 0.05 µM (-1.5, ⚠ cell-cycle shift); [[Dexamethasone (drug)]] 0.5 µM (-1.4); [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM (-1.4); [[Fenofibrate (drug)]] 0.05 µM (-1.4); [[Diphenhydramine (drug)]] 0.05 µM (-1.4); [[Clopidogrel (drug)]] 0.05 µM (-1.3); [[Goserelin (acetate) (drug)]] 5 µM (-1.3); [[Erlotinib (drug)]] 0.05 µM (-1.3); [[Rutin (trihydrate) (drug)]] 0.05 µM (-1.3) (35 in all, 4 with an alert ⚠; shown: the 10 strongest and the 3 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[A-427 (line)]], [[CHP-212 (line)]], [[C32 (line)]], [[LS 180 (line)]], [[A-172 (line)]], [[PANC-1 (line)]], [[HEC-1-A (line)]], [[NCI-H460 (line)]]

## + arm (51)

| Gene | Projection | Name |
|---|---|---|
| [[CLVS1]] | 0.905 | clavesin 1 |
| [[CNBD1]] | 0.891 | cyclic nucleotide binding domain containing 1 |
| [[LINC02208]] | 0.884 | long independently transcribed non-coding RNA 2208 |
| [[PTPRT]] | 0.884 | protein tyrosine phosphatase receptor type T |
| [[CNTNAP5]] | 0.883 | contactin associated protein family member 5 |
| [[LINC00861]] | 0.864 | long independently transcribed non-coding RNA 861 |
| [[GRM7]] | 0.862 | glutamate metabotropic receptor 7 |
| [[MYT1L]] | 0.862 | myelin transcription factor 1 like |
| [[CNTNAP4]] | 0.829 | contactin associated protein family member 4 |
| [[GLRA3]] | 0.829 | glycine receptor alpha 3 |
| [[VENTXP1]] | 0.824 | VENT homeobox pseudogene 1 |
| [[LINC00578]] | 0.802 | long independently transcribed non-coding RNA 578 |
| [[LINC01414]] | 0.796 | long independently transcribed non-coding RNA 1414 |
| [[G2E3-AS1]] | 0.791 | G2E3 antisense RNA 1 |
| [[LINC02306]] | 0.785 | long independently transcribed non-coding RNA 2306 |
| [[SEMA6D]] | 0.783 | semaphorin 6D |
| [[COL21A1]] | 0.782 | collagen type XXI alpha 1 chain |
| [[LINC00298]] | 0.782 | — |
| [[XIRP2]] | 0.771 | xin actin binding repeat containing 2 |
| [[PWRN1]] | 0.763 | Prader-Willi region non-protein coding RNA 1 |
| [[KIF6]] | 0.762 | kinesin family member 6 |
| [[LINC00871]] | 0.760 | long independently transcribed non-coding RNA 871 |
| [[MIR325HG]] | 0.756 | MIR325 host gene |
| [[ENTPD1]] | 0.755 | ectonucleoside triphosphate diphosphohydrolase 1 |
| [[LINC01483]] | 0.741 | long independently transcribed non-coding RNA 1483 |
| [[CHRM5]] | 0.730 | cholinergic receptor muscarinic 5 |
| [[IL1RAPL2]] | 0.716 | interleukin 1 receptor accessory protein like 2 |
| [[ELAPOR1]] | 0.710 | endosome-lysosome associated apoptosis and autophagy regulator 1 |
| [[LRRN3]] | 0.705 | leucine rich repeat neuronal 3 |
| [[CNTNAP2]] | 0.704 | contactin associated protein 2 |
| [[TSPEAR]] | 0.702 | thrombospondin type laminin G domain and EAR repeats |
| [[LINC02223]] | 0.689 | long independently transcribed non-coding RNA 2223 |
| [[PECAM1]] | 0.687 | platelet and endothelial cell adhesion molecule 1 |
| [[SLC35F4]] | 0.680 | solute carrier family 35 member F4 |
| [[DNAH2]] | 0.670 | dynein axonemal heavy chain 2 |
| [[ADAMTS19]] | 0.658 | ADAM metallopeptidase with thrombospondin type 1 motif 19 |
| [[TMC1]] | 0.640 | transmembrane channel like 1 |
| [[SLC7A7]] | 0.638 | solute carrier family 7 member 7 |
| [[CASC20]] | 0.608 | cancer susceptibility 20 |
| [[PSD]] | 0.608 | pleckstrin and Sec7 domain containing |
| [[MIAT]] | 0.592 | myocardial infarction associated transcript |
| [[LHFPL5]] | 0.591 | LHFPL tetraspan subfamily member 5 |
| [[ATP6V0A4]] | 0.582 | ATPase H+ transporting V0 subunit a4 |
| [[SLC9A9]] | 0.574 | solute carrier family 9 member A9 |
| [[HAND2-AS1]] | 0.551 | HAND2 antisense RNA 1 |
| [[ENPP3]] | 0.529 | ectonucleotide pyrophosphatase/phosphodiesterase 3 |
| [[HTR2C]] | 0.525 | 5-hydroxytryptamine receptor 2C |
| [[LIPC]] | 0.518 | lipase C, hepatic type |
| [[ATL1]] | 0.487 | atlastin GTPase 1 |
| [[SLC7A8]] | 0.474 | solute carrier family 7 member 8 |
| [[LINC01605]] | 0.403 | long independently transcribed non-coding RNA 1605 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 90; `graph/modules.parquet` — module == 90; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [89] (drug-dose × line)
