---
module: 157
type: "module"
n_genes: 28
n_plus: 28
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 157

*28 genes (single-armed) · [[Module 157.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 156), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Dinaciclib (drug)]] 5 µM (+6.7, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (+6.3, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+5.7, ⚠ toxic; transcription drop; cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (+3.7, ⚠ cell-cycle shift); [[Selinexor (drug)]] 5 µM (+3.0, ⚠ cell-cycle shift); [[Docetaxel (drug)]] 0.05 µM (+2.8, ⚠ transcription drop; cell-cycle shift); [[LY-2584702 (tosylate salt) (drug)]] 5 µM (+2.5, ⚠ toxic); [[Ipatasertib (drug)]] 0.5 µM (+2.2); [[XRK3F2 (drug)]] 0.5 µM (+2.1); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (+2.0, ⚠ cell-cycle shift); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+1.7); [[Topotecan (hydrochloride) (drug)]] 0.05 µM (+1.7); [[Thymol (drug)]] 0.5 µM (+1.6); [[9-ING-41 (drug)]] 0.5 µM (+1.5); [[Bosentan (hydrate) (drug)]] 5 µM (+1.5); [[Bimiralisib (drug)]] 0.5 µM (+1.4); [[Saquinavir (drug)]] 0.5 µM (+1.4); [[GSK1059615 (drug)]] 0.5 µM (+1.4) (36 in all, 14 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)
- Lower it: [[Harringtonine (drug)]] 0.5 µM (-2.5, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-2.4, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-2.2, ⚠ cell-cycle shift); [[Artesunate (drug)]] 0.5 µM (-1.8); [[Belinostat (drug)]] 5 µM (-1.8, ⚠ cell-cycle shift); [[Ixazomib citrate (drug)]] 5 µM (-1.7, ⚠ cell-cycle shift); [[Bortezomib (drug)]] 0.05 µM (-1.5, ⚠ cell-cycle shift); [[Bosentan (hydrate) (drug)]] 0.5 µM (-1.4); [[Doxycycline (monohydrate) (drug)]] 0.5 µM (-1.4); [[Mebendazole (drug)]] 5 µM (-1.3); [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM (-1.2); [[Loperamide (hydrochloride) (drug)]] 5 µM (-1.2); [[Loperamide (hydrochloride) (drug)]] 0.5 µM (-1.2); [[Relugolix (drug)]] 0.5 µM (-1.1); [[Almonertinib (hydrochloride) (drug)]] 0.05 µM (-1.1); [[IQ 1 (drug)]] 0.05 µM (-1.1) (24 in all, 9 with an alert ⚠; shown: the 10 strongest and the 6 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[HEC-1-A (line)]], [[LoVo (line)]], [[LOX-IMVI (line)]], [[SW480 (line)]], [[PANC-1 (line)]], [[J82 (line)]], [[A-172 (line)]], [[RKO (line)]]

## + arm (28)

| Gene | Projection | Name |
|---|---|---|
| [[AKT2]] | 0.805 | AKT serine/threonine kinase 2 |
| [[EME2]] | 0.803 | essential meiotic structure-specific endonuclease subunit 2 |
| [[LENG8]] | 0.798 | leukocyte receptor cluster member 8 |
| [[CCNL2]] | 0.795 | cyclin L2 |
| [[GET4]] | 0.758 | guided entry of tail-anchored proteins factor 4 |
| [[LMNTD2]] | 0.749 | lamin tail domain containing 2 |
| [[SLC9A3-AS1]] | 0.746 | SLC9A3 antisense RNA 1 |
| [[CFAP410]] | 0.722 | cilia and flagella associated protein 410 |
| [[CDK5RAP3]] | 0.720 | CDK5 regulatory subunit associated protein 3 |
| [[SH2B1]] | 0.717 | SH2B adaptor protein 1 |
| [[TMEM198B]] | 0.714 | transmembrane protein 198B (pseudogene) |
| [[PCED1A]] | 0.686 | PC-esterase domain containing 1A |
| [[AP1G2-AS1]] | 0.683 | AP1G2 antisense RNA 1 |
| [[IL11RA]] | 0.680 | interleukin 11 receptor subunit alpha |
| [[RMRP]] | 0.678 | RNA component of mitochondrial RNA processing endoribonuclease |
| [[MIB2]] | 0.668 | MIB E3 ubiquitin protein ligase 2 |
| [[GSK3A]] | 0.647 | glycogen synthase kinase 3 alpha |
| [[NDST2]] | 0.587 | N-deacetylase and N-sulfotransferase 2 |
| [[ALYREF]] | 0.587 | Aly/REF export factor |
| [[HCN3]] | 0.582 | hyperpolarization activated cyclic nucleotide gated potassium channel 3 |
| [[MAMDC4]] | 0.578 | MAM domain containing 4 |
| [[IRGQ]] | 0.560 | immunity related GTPase Q |
| [[CTDNEP1]] | 0.536 | CTD nuclear envelope phosphatase 1 |
| [[AHSA2P]] | 0.523 | activator of HSP90 ATPase homolog 2, pseudogene |
| [[PPM1M]] | 0.515 | protein phosphatase, Mg2+/Mn2+ dependent 1M |
| [[SRRT]] | 0.514 | serrate, RNA effector molecule |
| [[GHDC]] | 0.412 | GH3 domain containing |
| [[VSIG10L]] | 0.333 | V-set and immunoglobulin domain containing 10 like |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 157; `graph/modules.parquet` — module == 157; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [156] (drug-dose × line)
