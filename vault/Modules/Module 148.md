---
module: 148
type: "module"
n_genes: 30
n_plus: 24
n_minus: 6
arms_opposite: true
mean_cos_between_arms: -0.37105613946914673
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 148

*30 genes (24 in the + arm, 6 in the − arm) · [[Module 148.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37). The + arm rises where the − arm falls. Arm = the side of the module's main direction a gene sits on.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of the + arm minus the − arm (`graph/module_pooled_z.npy`, row 147), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it (+ arm up, − arm down): [[Idarubicin (hydrochloride) (drug)]] 5 µM (+19.2, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (+15.2, ⚠ toxic; transcription drop; cell-cycle shift); [[Homoharringtonine (drug)]] 5 µM (+14.2, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (+13.3, ⚠ toxic; transcription drop; cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (+12.3, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (+9.6, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+9.4, ⚠ toxic; transcription drop; cell-cycle shift); [[Epirubicin (hydrochloride) (drug)]] 5 µM (+9.3, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (+9.0, ⚠ cell-cycle shift); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (+8.5, ⚠ cell-cycle shift); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+7.6); [[Homoharringtonine (drug)]] 0.05 µM (+6.0); [[Harringtonine (drug)]] 0.05 µM (+3.8); [[Auranofin (drug)]] 5 µM (+2.7); [[Larotrectinib (drug)]] 5 µM (+2.2); [[TAK-733 (drug)]] 5 µM (+1.9); [[Belzutifan (drug)]] 5 µM (+1.9); [[L-Eflornithine (monohydrochloride) (drug)]] 5 µM (+1.9); [[γ-Oryzanol (drug)]] 0.05 µM (+1.8); [[Busulfan (drug)]] 5 µM (+1.8) (71 in all, 23 with an alert ⚠; shown: the 10 strongest and the 10 next strongest without an alert)
- Lower it: [[Panobinostat (drug)]] 5 µM (-12.3, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (-11.4, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (-10.5, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (-8.6); [[Digitoxin (drug)]] 5 µM (-8.1, ⚠ toxic; transcription drop; cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (-7.3, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 0.5 µM (-6.3, ⚠ cell-cycle shift); [[Ixazomib citrate (drug)]] 5 µM (-5.7, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (-5.5, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (-5.3, ⚠ cell-cycle shift); [[Brivudine (drug)]] 5 µM (-4.9); [[Ixazomib citrate (drug)]] 0.5 µM (-2.8); [[Rapamycin (drug)]] 5 µM (-2.7); [[Bortezomib (drug)]] 0.5 µM (-2.6); [[Ipatasertib (drug)]] 0.5 µM (-2.4); [[Tucidinostat (drug)]] 0.05 µM (-1.9); [[Temsirolimus (drug)]] 0.5 µM (-1.8); [[Neratinib (drug)]] 5 µM (-1.8); [[Trametinib (drug)]] 0.05 µM (-1.7) (73 in all, 21 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[SW480 (line)]], [[PANC-1 (line)]], [[NCI-H2347 (line)]], [[LOX-IMVI (line)]], [[HT-29 (line)]], [[Panc 03.27 (line)]], [[NCI-H2030 (line)]], [[SW1417 (line)]]

## + arm (24)

| Gene | Projection | Name |
|---|---|---|
| [[PSME3IP1]] | 0.831 | proteasome activator subunit 3 interacting protein 1 |
| [[C8orf33]] | 0.816 | chromosome 8 open reading frame 33 |
| [[VPS52]] | 0.801 | VPS52 subunit of GARP complex |
| [[PEF1]] | 0.800 | penta-EF-hand domain containing 1 |
| [[UBE3B]] | 0.793 | ubiquitin protein ligase E3B |
| [[MCTS1]] | 0.791 | MCTS1 re-initiation and release factor |
| [[SLC30A9]] | 0.757 | solute carrier family 30 member 9 |
| [[TSTD2]] | 0.756 | thiosulfate sulfurtransferase like domain containing 2 |
| [[POLDIP2]] | 0.753 | DNA polymerase delta interacting protein 2 |
| [[MAGOHB]] | 0.750 | mago homolog B, exon junction complex subunit |
| [[MLH1]] | 0.747 | mutL homolog 1 |
| [[COX18]] | 0.735 | cytochrome c oxidase assembly factor COX18 |
| [[MRPL30]] | 0.733 | mitochondrial ribosomal protein L30 |
| [[TIMMDC1]] | 0.683 | translocase of inner mitochondrial membrane domain containing 1 |
| [[INTS2]] | 0.640 | integrator complex subunit 2 |
| [[HIKESHI]] | 0.627 | heat shock protein nuclear import factor hikeshi |
| [[MTR]] | 0.606 | 5-methyltetrahydrofolate-homocysteine methyltransferase |
| [[RNH1]] | 0.583 | ribonuclease/angiogenin inhibitor 1 |
| [[ALDH16A1]] | 0.578 | aldehyde dehydrogenase 16 family member A1 |
| [[CSRNP2]] | 0.557 | cysteine and serine rich nuclear protein 2 |
| [[CEP164]] | 0.552 | centrosomal protein 164 |
| [[PCNP]] | 0.520 | PEST proteolytic signal containing nuclear protein |
| [[SERPINB6]] | 0.518 | serpin family B member 6 |
| [[CASP3]] | 0.448 | caspase 3 |

## − arm (6)

| Gene | Projection | Name |
|---|---|---|
| [[SNN]] | -0.744 | stannin |
| [[LMTK2]] | -0.688 | lemur tail kinase 2 |
| [[ST3GAL4]] | -0.636 | ST3 beta-galactoside alpha-2,3-sialyltransferase 4 |
| [[CHKA]] | -0.507 | choline kinase alpha |
| [[METTL27]] | -0.504 | methyltransferase like 27 |
| [[ARHGEF10L]] | -0.489 | Rho guanine nucleotide exchange factor 10 like |

## Data

- `graph/nodes.parquet` — module == 148; `graph/modules.parquet` — module == 148; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [147] (drug-dose × line)
