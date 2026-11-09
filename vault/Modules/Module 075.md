---
module: 75
type: "module"
n_genes: 60
n_plus: 60
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 075

*60 genes (single-armed) · [[Module 075.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 74), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM (+20.5, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 5 µM (+15.1, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (+12.4, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (+12.4, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+10.7, ⚠ toxic; transcription drop; cell-cycle shift); [[Auranofin (drug)]] 5 µM (+9.3); [[Tucidinostat (drug)]] 5 µM (+8.5); [[Idarubicin (hydrochloride) (drug)]] 0.5 µM (+6.7, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (+6.6, ⚠ cell-cycle shift); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+5.9); [[Docetaxel (Trihydrate) (drug)]] 0.5 µM (+2.1); [[Ipatasertib (drug)]] 0.5 µM (+2.0); [[Verteporfin (drug)]] 5 µM (+1.8); [[Amsacrine (drug)]] 5 µM (+1.6); [[Ixazomib citrate (drug)]] 0.5 µM (+1.5); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM (+1.5); [[Glycyrrhizic acid (drug)]] 0.05 µM (+1.4) (74 in all, 30 with an alert ⚠; shown: the 10 strongest and the 7 next strongest without an alert)
- Lower it: [[Adagrasib (drug)]] 0.05 µM (-2.4, ⚠ position not correctable); [[Lucanthone (drug)]] 0.05 µM (-1.7); [[Digitoxin (drug)]] 0.5 µM (-1.7, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 0.05 µM (-1.5, ⚠ cell-cycle shift); [[Diphenhydramine (drug)]] 0.05 µM (-1.4); [[Dexamethasone (drug)]] 0.5 µM (-1.4); [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM (-1.4); [[Rutin (trihydrate) (drug)]] 0.05 µM (-1.3); [[Ipatasertib (drug)]] 5 µM (-1.3); [[Fenofibrate (drug)]] 0.05 µM (-1.2); [[Pyridoxine (hydrochloride) (drug)]] 5 µM (-1.2); [[Artesunate (drug)]] 0.5 µM (-1.1); [[Goserelin (acetate) (drug)]] 5 µM (-1.1) (27 in all, 3 with an alert ⚠; shown: the 10 strongest and the 3 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[HOP62 (line)]], [[NCI-H23 (line)]], [[A-172 (line)]], [[PANC-1 (line)]], [[HEC-1-A (line)]], [[A498 (line)]], [[A-427 (line)]], [[C32 (line)]]

## + arm (60)

| Gene | Projection | Name |
|---|---|---|
| [[LRRC4C]] | 0.899 | leucine rich repeat containing 4C |
| [[MIR4300HG]] | 0.898 | MIR4300 host gene |
| [[DPP6]] | 0.897 | dipeptidyl peptidase like 6 |
| [[GRM8]] | 0.875 | glutamate metabotropic receptor 8 |
| [[MYO16]] | 0.869 | myosin XVI |
| [[PPP1R9A-AS1]] | 0.863 | PPP1R9A antisense RNA 1 |
| [[LINC01033]] | 0.837 | long independently transcribed non-coding RNA 1033 |
| [[SLC9C1]] | 0.829 | solute carrier family 9 member C1 |
| [[RBMS3-AS3]] | 0.826 | RBMS3 antisense RNA 3 |
| [[LINC01933]] | 0.825 | long independently transcribed non-coding RNA 1933 |
| [[FER1L6]] | 0.820 | fer-1 like family member 6 |
| [[EYS]] | 0.816 | EGF-like photoreceptor maintenance factor |
| [[RBFOX3]] | 0.813 | RNA binding fox-1 homolog 3 |
| [[LINC02755]] | 0.809 | long independently transcribed non-coding RNA 2755 |
| [[LINC02006]] | 0.809 | long independently transcribed non-coding RNA 2006 |
| [[LINC02932]] | 0.807 | long independently transcribed non-coding RNA 2932 |
| [[LINC02694]] | 0.803 | long independently transcribed non-coding RNA 2694 |
| [[DLEU7]] | 0.798 | deleted in lymphocytic leukemia 7 |
| [[TTN]] | 0.786 | titin |
| [[FEZ1]] | 0.774 | fasciculation and elongation protein zeta 1 |
| [[LINC01811]] | 0.773 | long independently transcribed non-coding RNA 1811 |
| [[HSD11B1-AS1]] | 0.773 | HSD11B1 antisense RNA 1 |
| [[PLB1]] | 0.772 | phospholipase B1 |
| [[PLXNC1]] | 0.761 | plexin C1 |
| [[MALRD1]] | 0.754 | MAM and LDL receptor class A domain containing 1 |
| [[CCDC170]] | 0.754 | coiled-coil domain containing 170 |
| [[MAP3K20-AS1]] | 0.740 | MAP3K20 antisense RNA 1 |
| [[SP140]] | 0.740 | SP140 nuclear body protein |
| [[DKK2]] | 0.713 | dickkopf Wnt signaling pathway inhibitor 2 |
| [[TRD-AS1]] | 0.709 | TRD antisense RNA 1 |
| [[LINC00534]] | 0.704 | long independently transcribed non-coding RNA 534 |
| [[LY96]] | 0.704 | lymphocyte antigen 96 |
| [[CACNA1E]] | 0.702 | calcium voltage-gated channel subunit alpha1 E |
| [[GREB1]] | 0.685 | growth regulating estrogen receptor binding 1 |
| [[CEACAM16-AS1]] | 0.668 | CEACAM16, CEACAM19 and PVR antisense RNA 1 |
| [[TPTE2P6]] | 0.666 | TPTE2 pseudogene 6 |
| [[LINC01226]] | 0.663 | long independently transcribed non-coding RNA 1226 |
| [[FSIP1]] | 0.658 | fibrous sheath interacting protein 1 |
| [[TACR3-AS1]] | 0.657 | TACR3 antisense RNA 1 |
| [[TRPM3]] | 0.654 | transient receptor potential cation channel subfamily M member 3 |
| [[ZFPM2]] | 0.651 | zinc finger protein, FOG family member 2 |
| [[RYR2]] | 0.648 | ryanodine receptor 2 |
| [[DLGAP1]] | 0.636 | DLG associated protein 1 |
| [[KCNIP4]] | 0.631 | potassium voltage-gated channel interacting protein 4 |
| [[CLDN14]] | 0.627 | claudin 14 |
| [[LINC00504]] | 0.619 | long independently transcribed non-coding RNA 504 |
| [[CFAP92]] | 0.593 | cilia and flagella associated protein 92 (putative) |
| [[LINC00536]] | 0.591 | long independently transcribed non-coding RNA 536 |
| [[ZNF774]] | 0.570 | zinc finger protein 774 |
| [[CALCRL-AS1]] | 0.566 | CALCRL and TFPI antisense RNA 1 |
| [[PDE8B]] | 0.563 | phosphodiesterase 8B |
| [[ENPP7P4]] | 0.561 | ectonucleotide pyrophosphatase/phosphodiesterase 7 pseudogene 4 |
| [[KCND3]] | 0.560 | potassium voltage-gated channel subfamily D member 3 |
| [[LINC00592]] | 0.557 | long independently transcribed non-coding RNA 592 |
| [[GALNT9]] | 0.523 | polypeptide N-acetylgalactosaminyltransferase 9 |
| [[CASC8]] | 0.492 | cancer susceptibility 8 |
| [[PKD1L2]] | 0.485 | polycystin 1 like 2 (gene/pseudogene) |
| [[PPP1R3B-DT]] | 0.484 | PPP1R3B divergent transcript |
| [[NCF2]] | 0.437 | neutrophil cytosolic factor 2 |
| [[SLIT1]] | 0.382 | slit guidance ligand 1 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 75; `graph/modules.parquet` — module == 75; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [74] (drug-dose × line)
