---
module: 169
type: "module"
n_genes: 25
n_plus: 25
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.24855226278305054
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 169

*25 genes (single-armed) · [[Module 169.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 168), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[TAK-901 (drug)]] 5 µM (+7.6, ⚠ cell-cycle shift); [[PH-797804 (drug)]] 5 µM (+5.9); [[Ixazomib citrate (drug)]] 5 µM (+5.7, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (+5.0, ⚠ cell-cycle shift); [[Bortezomib (drug)]] 0.05 µM (+4.8, ⚠ cell-cycle shift); [[Ixazomib citrate (drug)]] 0.5 µM (+4.2); [[Digitoxin (drug)]] 5 µM (+3.7, ⚠ toxic; transcription drop; cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (+2.7, ⚠ cell-cycle shift); [[Niclosamide (olamine) (drug)]] 5 µM (+2.6, ⚠ toxic; cell-cycle shift); [[Bortezomib (drug)]] 5 µM (+2.5, ⚠ toxic; cell-cycle shift); [[Bortezomib (drug)]] 0.5 µM (+2.3); [[Verteporfin (drug)]] 5 µM (+1.7); [[Glycyrrhizic acid (drug)]] 0.5 µM (+1.4); [[Tomivosertib (drug)]] 5 µM (+1.3); [[Ponatinib (drug)]] 5 µM (+1.3); [[Vinblastine (sulfate) (drug)]] 5 µM (+1.3); [[Neratinib (maleate) (drug)]] 5 µM (+1.3); [[Irinotecan (hydrochloride) (drug)]] 0.5 µM (+1.2) (41 in all, 18 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)
- Lower it: [[Dinaciclib (drug)]] 5 µM (-10.8, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (-10.1, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (-7.4, ⚠ toxic; transcription drop; cell-cycle shift); [[Homoharringtonine (drug)]] 5 µM (-3.0, ⚠ cell-cycle shift); [[Auranofin (drug)]] 5 µM (-3.0); [[Topotecan (hydrochloride) (drug)]] 5 µM (-2.5, ⚠ toxic; cell-cycle shift); [[Docetaxel (drug)]] 0.05 µM (-2.2, ⚠ transcription drop; cell-cycle shift); [[Filgotinib (drug)]] 0.05 µM (-1.8); [[Filgotinib (drug)]] 5 µM (-1.8); [[Darinaparsin (drug)]] 5 µM (-1.7, ⚠ cell-cycle shift); [[Estrone sulfate (potassium) (drug)]] 5 µM (-1.6); [[Carbamazepine (drug)]] 5 µM (-1.5); [[Diphenhydramine (drug)]] 0.5 µM (-1.5); [[Thymol (drug)]] 5 µM (-1.4); [[Mifepristone (drug)]] 0.5 µM (-1.3); [[Retinoic acid (drug)]] 0.05 µM (-1.3); [[Busulfan (drug)]] 0.05 µM (-1.3) (39 in all, 13 with an alert ⚠; shown: the 10 strongest and the 7 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[SW480 (line)]], [[LS 180 (line)]], [[LoVo (line)]], [[HEC-1-A (line)]], [[PANC-1 (line)]], [[Panc 03.27 (line)]], [[A-427 (line)]], [[C-33 A (line)]]

## + arm (25)

| Gene | Projection | Name |
|---|---|---|
| [[SEC24B]] | 0.880 | SEC24 homolog B, COPII component |
| [[ZNF148]] | 0.800 | zinc finger protein 148 |
| [[MARCHF5]] | 0.778 | membrane associated ring-CH-type finger 5 |
| [[CLASP1]] | 0.774 | cytoplasmic linker associated protein 1 |
| [[GAPVD1]] | 0.769 | GTPase activating protein and VPS9 domains 1 |
| [[RELCH]] | 0.762 | RAB11 binding and LisH domain, coiled-coil and HEAT repeat containing |
| [[PPHLN1]] | 0.746 | periphilin 1 |
| [[DCAF5]] | 0.697 | DDB1 and CUL4 associated factor 5 |
| [[NPEPPS]] | 0.657 | aminopeptidase puromycin sensitive |
| [[REXO2]] | 0.645 | RNA exonuclease 2 |
| [[ZDHHC7]] | 0.642 | zDHHC palmitoyltransferase 7 |
| [[ARHGEF7]] | 0.638 | Rho guanine nucleotide exchange factor 7 |
| [[ARMH3]] | 0.637 | armadillo like helical domain containing 3 |
| [[RNF13]] | 0.631 | ring finger protein 13 |
| [[RBM27]] | 0.620 | RNA binding motif protein 27 |
| [[PHB2]] | 0.589 | prohibitin 2 |
| [[MANBA]] | 0.556 | mannosidase beta |
| [[INTS9]] | 0.542 | integrator complex subunit 9 |
| [[RAB3GAP1]] | 0.533 | RAB3 GTPase activating protein catalytic subunit 1 |
| [[MAPK14]] | 0.526 | mitogen-activated protein kinase 14 |
| [[DYNC1LI1]] | 0.522 | dynein cytoplasmic 1 light intermediate chain 1 |
| [[RFX7]] | 0.516 | regulatory factor X7 |
| [[C16orf87]] | 0.499 | HDAC and MIER1 interacting protein 1 |
| [[HLA-K]] | -0.443 | major histocompatibility complex, class I, K (pseudogene) |
| [[EXOC6]] | -0.392 | exocyst complex component 6 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 169; `graph/modules.parquet` — module == 169; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [168] (drug-dose × line)
