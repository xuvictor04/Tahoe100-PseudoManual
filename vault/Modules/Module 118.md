---
module: 118
type: "module"
n_genes: 41
n_plus: 34
n_minus: 7
arms_opposite: true
mean_cos_between_arms: -0.329124391078949
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 118

*41 genes (34 in the + arm, 7 in the − arm) · [[Module 118.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33). The + arm rises where the − arm falls. Arm = the side of the module's main direction a gene sits on.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of the + arm minus the − arm (`graph/module_pooled_z.npy`, row 117), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it (+ arm up, − arm down): [[Idarubicin (hydrochloride) (drug)]] 5 µM (+15.7, ⚠ cell-cycle shift); [[TAK-901 (drug)]] 5 µM (+10.2, ⚠ cell-cycle shift); [[Topotecan (hydrochloride) (drug)]] 5 µM (+8.4, ⚠ toxic; cell-cycle shift); [[Selinexor (drug)]] 5 µM (+7.2, ⚠ cell-cycle shift); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+6.8); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (+6.2, ⚠ cell-cycle shift); [[PH-797804 (drug)]] 5 µM (+6.1); [[Auranofin (drug)]] 5 µM (+4.7); [[Ixazomib citrate (drug)]] 5 µM (+4.3, ⚠ cell-cycle shift); [[Epirubicin (hydrochloride) (drug)]] 5 µM (+4.3, ⚠ cell-cycle shift); [[Ixazomib citrate (drug)]] 0.5 µM (+4.0); [[Ipatasertib (drug)]] 0.5 µM (+2.8); [[GSK1059615 (drug)]] 0.5 µM (+2.5); [[Triamcinolone (drug)]] 5 µM (+2.4); [[Bimiralisib (drug)]] 0.5 µM (+2.3); [[Entrectinib (drug)]] 5 µM (+2.1); [[Medroxyprogesterone acetate (drug)]] 0.5 µM (+2.1) (96 in all, 24 with an alert ⚠; shown: the 10 strongest and the 7 next strongest without an alert)
- Lower it: [[Dinaciclib (drug)]] 0.5 µM (-11.3, ⚠ toxic; transcription drop; cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (-11.1); [[Dinaciclib (drug)]] 5 µM (-9.3, ⚠ toxic; transcription drop; cell-cycle shift); [[Tucidinostat (drug)]] 0.5 µM (-7.1, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (-5.5, ⚠ toxic; transcription drop; cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (-4.9, ⚠ cell-cycle shift); [[c-Kit-IN-1 (drug)]] 0.05 µM (-4.8, ⚠ unreliable plate only); [[Niclosamide (olamine) (drug)]] 5 µM (-4.6, ⚠ toxic; cell-cycle shift); [[Brivudine (drug)]] 5 µM (-3.9); [[Harringtonine (drug)]] 5 µM (-2.7, ⚠ cell-cycle shift); [[Glycyrrhizic acid (drug)]] 0.5 µM (-2.1); [[Berberine (chloride hydrate) (drug)]] 5 µM (-1.9); [[Tucidinostat (drug)]] 0.05 µM (-1.8); [[Abemaciclib (drug)]] 5 µM (-1.7); [[PF-06260933 (drug)]] 5 µM (-1.7); [[Pyridoxine (drug)]] 5 µM (-1.7); [[Vinblastine (sulfate) (drug)]] 5 µM (-1.6); [[Benproperine (phosphate) (drug)]] 0.05 µM (-1.6) (77 in all, 18 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[SW480 (line)]], [[HOP62 (line)]], [[LoVo (line)]], [[KATO III (line)]], [[NCI-H460 (line)]], [[HEC-1-A (line)]], [[Panc 03.27 (line)]], [[LOX-IMVI (line)]]

## + arm (34)

| Gene | Projection | Name |
|---|---|---|
| [[DNAJC30]] | 0.798 | DnaJ heat shock protein family (Hsp40) member C30 |
| [[SYNRG]] | 0.790 | synergin gamma |
| [[NGDN]] | 0.786 | neuroguidin |
| [[KBTBD4]] | 0.773 | kelch repeat and BTB domain containing 4 |
| [[APPBP2]] | 0.766 | amyloid beta precursor protein binding protein 2 |
| [[IGBP1]] | 0.755 | immunoglobulin binding protein 1 |
| [[TMUB2]] | 0.747 | transmembrane and ubiquitin like domain containing 2 |
| [[EMC3]] | 0.734 | ER membrane protein complex subunit 3 |
| [[CCDC142]] | 0.733 | coiled-coil domain containing 142 |
| [[WBP1L]] | 0.720 | WW domain binding protein 1 like |
| [[FRS2]] | 0.703 | fibroblast growth factor receptor substrate 2 |
| [[ZNF446]] | 0.697 | zinc finger protein 446 |
| [[PRPF18]] | 0.692 | pre-mRNA processing factor 18 |
| [[TFPT]] | 0.689 | TCF3 fusion partner |
| [[CWC25]] | 0.685 | CWC25 spliceosome associated protein |
| [[MED4]] | 0.680 | mediator complex subunit 4 |
| [[PIN4]] | 0.658 | peptidylprolyl cis/trans isomerase, NIMA-interacting 4 |
| [[SCNM1]] | 0.655 | sodium channel modifier 1 |
| [[CNPY2]] | 0.644 | canopy FGF signaling regulator 2 |
| [[USF3]] | 0.636 | upstream transcription factor family member 3 |
| [[ATP6V1E1]] | 0.623 | ATPase H+ transporting V1 subunit E1 |
| [[NDUFS3]] | 0.611 | NADH:ubiquinone oxidoreductase core subunit S3 |
| [[CSNK1G1]] | 0.608 | casein kinase 1 gamma 1 |
| [[ZNF324]] | 0.586 | zinc finger protein 324 |
| [[IP6K2]] | 0.565 | inositol hexakisphosphate kinase 2 |
| [[CWF19L2]] | 0.564 | CWF19 like cell cycle control factor 2 |
| [[PPP6C]] | 0.560 | protein phosphatase 6 catalytic subunit |
| [[KIAA1143]] | 0.554 | KIAA1143 |
| [[KPNA6]] | 0.538 | karyopherin subunit alpha 6 |
| [[GALK2]] | 0.516 | galactokinase 2 |
| [[RTF1]] | 0.515 | RTF1 homolog, Paf1/RNA polymerase II complex component |
| [[ORAI3]] | 0.486 | ORAI calcium release-activated calcium modulator 3 |
| [[C9orf85]] | 0.402 | chromosome 9 open reading frame 85 |
| [[MAVS]] | 0.288 | mitochondrial antiviral signaling protein |

## − arm (7)

| Gene | Projection | Name |
|---|---|---|
| [[NIN]] | -0.592 | ninein |
| [[VPS13A]] | -0.577 | vacuolar protein sorting 13 homolog A |
| [[BCAP29]] | -0.548 | B cell receptor associated protein 29 |
| [[CCND2]] | -0.534 | cyclin D2 |
| [[DENND1A]] | -0.525 | DENN domain containing 1A |
| [[LRRC8B]] | -0.520 | leucine rich repeat containing 8 VRAC subunit B |
| [[HOOK1]] | -0.505 | hook microtubule tethering protein 1 |

## Data

- `graph/nodes.parquet` — module == 118; `graph/modules.parquet` — module == 118; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [117] (drug-dose × line)
