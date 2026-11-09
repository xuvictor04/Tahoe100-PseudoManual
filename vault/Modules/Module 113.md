---
module: 113
type: "module"
n_genes: 43
n_plus: 43
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: "hypoxia"
label_source: "hallmark"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 113

*hypoxia · 43 genes (single-armed) · [[Module 113.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

Label from the validation stage: **hypoxia** (hallmark, q 3e-09; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | hypoxia | hallmark | 11/43 | 21.2 | 3e-09 |
| + | hypoxia | hallmark | 11/43 | 21.2 | 3e-09 |
| + | Metallothioneins bind metals | reactome | 5/43 | 250 | 4e-09 |
| all | Metallothioneins bind metals | reactome | 5/43 | 250 | 4e-09 |
| all | metallothionein | control | 5/43 | 219 | 1e-08 |
| + | metallothionein | control | 5/43 | 219 | 1e-08 |
| + | Response to metal ions | reactome | 5/43 | 195 | 2e-08 |
| all | Response to metal ions | reactome | 5/43 | 195 | 2e-08 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 112), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Tucidinostat (drug)]] 5 µM (+6.3); [[Tucidinostat (drug)]] 0.5 µM (+4.3, ⚠ cell-cycle shift); [[Budesonide (drug)]] 0.5 µM (+3.2); [[Betamethasone dipropionate (drug)]] 5 µM (+2.9); [[Budesonide (drug)]] 0.05 µM (+2.8); [[Betamethasone dipropionate (drug)]] 0.5 µM (+2.7); [[Clobetasol propionate (drug)]] 0.05 µM (+2.6); [[Triamcinolone (drug)]] 0.5 µM (+2.4); [[Clobetasol propionate (drug)]] 0.5 µM (+2.3); [[Phenylephrine (hydrochloride) (drug)]] 5 µM (+2.3); [[Dexamethasone (drug)]] 5 µM (+2.3) (27 in all, 2 with an alert ⚠; shown: the 10 strongest and the 1 next strongest without an alert)
- Lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM (-6.0, ⚠ cell-cycle shift); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (-4.1, ⚠ cell-cycle shift); [[Topotecan (hydrochloride) (drug)]] 5 µM (-3.7, ⚠ toxic; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (-3.4, ⚠ toxic; transcription drop; cell-cycle shift); [[Ponatinib (drug)]] 5 µM (-3.0); [[Dinaciclib (drug)]] 0.5 µM (-2.9, ⚠ toxic; transcription drop; cell-cycle shift); [[Epirubicin (hydrochloride) (drug)]] 5 µM (-2.8, ⚠ cell-cycle shift); [[c-Kit-IN-1 (drug)]] 0.05 µM (-2.7, ⚠ unreliable plate only); [[Topotecan (hydrochloride) (drug)]] 0.5 µM (-2.3, ⚠ cell-cycle shift); [[Selinexor (drug)]] 5 µM (-2.1, ⚠ cell-cycle shift); [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM (-2.1); [[TAK-733 (drug)]] 5 µM (-2.0); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (-1.5); [[c-Kit-IN-1 (drug)]] 5 µM (-1.5); [[Cobimetinib (drug)]] 0.5 µM (-1.4); [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM (-1.4); [[Cabozantinib (S-malate) (drug)]] 5 µM (-1.4); [[venetoclax (drug)]] 5 µM (-1.4); [[Ponatinib (drug)]] 0.5 µM (-1.3) (40 in all, 18 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[MIA PaCa-2 (line)]], [[SNU-423 (line)]], [[HS-578T (line)]], [[A-172 (line)]], [[PANC-1 (line)]], [[SW 900 (line)]], [[CFPAC-1 (line)]], [[NCI-H1792 (line)]]

## Candidate new members

*Members not annotated to the set their arm is enriched for, ranked by mean cos to the annotated members (`validation/novel_members.csv`); ⚠ = a reason to doubt the gene's place (in the vector space only through flagged drug-doses), kept in its rank. 17 candidates, none with an alert; shown: the 15 strongest.*

| # | Gene | Set | Mean cos |
|---|---|---|---|
| 1 | [[ID1]] | Metallothioneins bind metals | +0.67 |
| 2 | [[CEBPB]] | Metallothioneins bind metals | +0.65 |
| 3 | [[IRX3]] | Metallothioneins bind metals | +0.65 |
| 4 | [[ZMYND8]] | Metallothioneins bind metals | +0.64 |
| 5 | [[ANGPTL4]] | Metallothioneins bind metals | +0.64 |
| 6 | [[IRS2]] | Metallothioneins bind metals | +0.63 |
| 7 | [[CCL20]] | Metallothioneins bind metals | +0.62 |
| 8 | [[MT1X]] | hypoxia | +0.61 |
| 9 | [[TANC2]] | Metallothioneins bind metals | +0.60 |
| 10 | [[DUSP1]] | Metallothioneins bind metals | +0.59 |
| 11 | [[ZFP36L1]] | TNF-alpha signaling via NF-kB | +0.56 |
| 12 | [[GLRX]] | Metallothioneins bind metals | +0.53 |
| 13 | [[MT1A]] | hypoxia | +0.53 |
| 14 | [[MT1E]] | TNF-alpha signaling via NF-kB | +0.53 |
| 15 | [[ADAMTSL4]] | Metallothioneins bind metals | +0.52 |

## + arm (43)

| Gene | Projection | Name |
|---|---|---|
| [[MT1X]] | 0.876 | metallothionein 1X |
| [[MT2A]] | 0.823 | metallothionein 2A |
| [[DUSP1]] | 0.817 | dual specificity phosphatase 1 |
| [[MT1A]] | 0.811 | metallothionein 1A |
| [[MT1E]] | 0.796 | metallothionein 1E |
| [[ANGPTL4]] | 0.780 | angiopoietin like 4 |
| [[CEBPB]] | 0.763 | CCAAT enhancer binding protein beta |
| [[TANC2]] | 0.750 | tetratricopeptide repeat, ankyrin repeat and coiled-coil containing 2 |
| [[ID1]] | 0.740 | inhibitor of DNA binding 1 |
| [[ZMYND8]] | 0.737 | zinc finger MYND-type containing 8 |
| [[MT1F]] | 0.736 | metallothionein 1F |
| [[ERRFI1]] | 0.717 | ERBB receptor feedback inhibitor 1 |
| [[CCL20]] | 0.713 | C-C motif chemokine ligand 20 |
| [[IRS2]] | 0.710 | insulin receptor substrate 2 |
| [[IRX3]] | 0.693 | iroquois homeobox 3 |
| [[EPAS1]] | 0.669 | endothelial PAS domain protein 1 |
| [[ZFP36L1]] | 0.667 | ZFP36 like 1 zinc finger CCCH-type |
| [[ADAMTSL4]] | 0.665 | ADAMTS like 4 |
| [[TIPARP]] | 0.657 | TCDD inducible poly(ADP-ribose) polymerase |
| [[SERPINE1]] | 0.629 | serpin family E member 1 |
| [[LINC00540]] | 0.624 | long independently transcribed non-coding RNA 540 |
| [[SGK1]] | 0.620 | serum/glucocorticoid regulated kinase 1 |
| [[A4GALT]] | 0.619 | alpha 1,4-galactosyltransferase (P1PK blood group) |
| [[GLRX]] | 0.616 | glutaredoxin |
| [[UBE2E2]] | 0.610 | ubiquitin conjugating enzyme E2 E2 |
| [[SLC45A1]] | 0.606 | solute carrier family 45 member 1 |
| [[SLC16A3]] | 0.599 | solute carrier family 16 member 3 |
| [[ADRB2]] | 0.558 | adrenoceptor beta 2 |
| [[ELL2]] | 0.546 | elongation factor for RNA polymerase II 2 |
| [[PIK3R1]] | 0.513 | phosphoinositide-3-kinase regulatory subunit 1 |
| [[MYO1E]] | 0.512 | myosin IE |
| [[TREM1]] | 0.502 | triggering receptor expressed on myeloid cells 1 |
| [[GALK1]] | 0.501 | galactokinase 1 |
| [[PRKAG2]] | 0.483 | protein kinase AMP-activated non-catalytic subunit gamma 2 |
| [[SLC38A2]] | 0.482 | solute carrier family 38 member 2 |
| [[AGTPBP1]] | 0.476 | ATP/GTP binding carboxypeptidase 1 |
| [[KLF6]] | 0.468 | KLF transcription factor 6 |
| [[ATP2B4]] | 0.467 | ATPase plasma membrane Ca2+ transporting 4 |
| [[SDK1]] | 0.448 | sidekick cell adhesion molecule 1 |
| [[GADD45B]] | 0.443 | growth arrest and DNA damage inducible beta |
| [[IL6R]] | 0.427 | interleukin 6 receptor |
| [[MYO1B]] | 0.406 | myosin IB |
| [[EREG]] | 0.348 | epiregulin |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 113; `graph/modules.parquet` — module == 113; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [112] (drug-dose × line)
