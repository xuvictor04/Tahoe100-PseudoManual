---
module: 154
type: "module"
n_genes: 29
n_plus: 29
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.35438069701194763
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 154

*29 genes (single-armed) · [[Module 154.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 153), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Tucidinostat (drug)]] 5 µM (+4.4); [[Belinostat (drug)]] 5 µM (+4.1, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (+3.9, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (+3.2, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (+2.8, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 0.5 µM (+2.5, ⚠ cell-cycle shift); [[PF-06260933 (drug)]] 5 µM (+2.0); [[Belinostat (drug)]] 0.5 µM (+1.8, ⚠ cell-cycle shift); [[Brivudine (drug)]] 5 µM (+1.7); [[Daptomycin (drug)]] 5 µM (+1.4, ⚠ unreliable plate only); [[Pitavastatin (Calcium) (drug)]] 0.5 µM (+1.4); [[Fumaric acid (drug)]] 5 µM (+1.3); [[Dimethyl fumarate (drug)]] 5 µM (+1.1); [[Ipatasertib (drug)]] 0.5 µM (+1.1); [[HI-TOPK-032 (drug)]] 5 µM (+1.0); [[Radotinib (drug)]] 5 µM (+1.0); [[Vilanterol (drug)]] 0.5 µM (+1.0) (19 in all, 9 with an alert ⚠; shown: the 10 strongest and the 7 next strongest without an alert)
- Lower it: [[Homoharringtonine (drug)]] 0.5 µM (-5.4, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-4.1, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 5 µM (-3.7, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (-3.2, ⚠ toxic; transcription drop; cell-cycle shift); [[Niclosamide (olamine) (drug)]] 5 µM (-2.9, ⚠ toxic; cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (-2.9, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (-2.9, ⚠ toxic; transcription drop; cell-cycle shift); [[Clobetasol propionate (drug)]] 0.05 µM (-2.6); [[Ouabain (Octahydrate) (drug)]] 5 µM (-2.4, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (-2.4, ⚠ toxic; transcription drop; cell-cycle shift); [[Auranofin (drug)]] 5 µM (-2.3); [[Clobetasol propionate (drug)]] 0.5 µM (-2.0); [[Clobetasol propionate (drug)]] 5 µM (-1.9); [[Triamcinolone (drug)]] 5 µM (-1.8); [[Betamethasone dipropionate (drug)]] 5 µM (-1.8); [[5-Azacytidine (drug)]] 5 µM (-1.7); [[Budesonide (drug)]] 0.05 µM (-1.7); [[Triamcinolone (drug)]] 0.5 µM (-1.7); [[Betamethasone dipropionate (drug)]] 0.05 µM (-1.6) (51 in all, 22 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[NCI-H23 (line)]], [[A549 (line)]], [[SK-MEL-2 (line)]], [[Hs 766T (line)]], [[LOX-IMVI (line)]], [[NCI-H460 (line)]], [[NCI-H1792 (line)]], [[CFPAC-1 (line)]]

## + arm (29)

| Gene | Projection | Name |
|---|---|---|
| [[UBA6]] | 0.821 | ubiquitin like modifier activating enzyme 6 |
| [[ZNRF1]] | 0.799 | zinc and ring finger 1 |
| [[TNFRSF11A]] | 0.786 | TNF receptor superfamily member 11a |
| [[KHDRBS3]] | 0.768 | KH RNA binding domain containing, signal transduction associated 3 |
| [[GALNT12]] | 0.760 | polypeptide N-acetylgalactosaminyltransferase 12 |
| [[GRK5]] | 0.757 | G protein-coupled receptor kinase 5 |
| [[CIB1]] | 0.753 | calcium and integrin binding 1 |
| [[C7orf57]] | 0.717 | chromosome 7 open reading frame 57 |
| [[SEMA4B]] | 0.702 | semaphorin 4B |
| [[DTNA]] | 0.692 | dystrobrevin alpha |
| [[SMS]] | 0.688 | spermine synthase |
| [[ATG16L2]] | 0.674 | autophagy related 16 like 2 |
| [[EPN2]] | 0.672 | epsin 2 |
| [[ETHE1]] | 0.633 | ETHE1 persulfide dioxygenase |
| [[FGFR1]] | 0.626 | fibroblast growth factor receptor 1 |
| [[ADI1]] | -0.622 | acireductone dioxygenase 1 |
| [[MPP2]] | 0.610 | MAGUK p55 scaffold protein 2 |
| [[IFFO2]] | 0.589 | intermediate filament family orphan 2 |
| [[CMIP]] | 0.587 | c-Maf inducing protein |
| [[FOXG1]] | -0.581 | forkhead box G1 |
| [[LFNG]] | 0.564 | LFNG O-fucosylpeptide 3-beta-N-acetylglucosaminyltransferase |
| [[UBTD2]] | 0.561 | ubiquitin domain containing 2 |
| [[HSPG2]] | 0.557 | heparan sulfate proteoglycan 2 |
| [[TAF8]] | -0.554 | TATA-box binding protein associated factor 8 |
| [[TMEM51]] | 0.551 | transmembrane protein 51 |
| [[LHX1-DT]] | 0.551 | LHX1 divergent transcript |
| [[TTYH2]] | 0.542 | tweety family member 2 |
| [[ZMIZ1]] | 0.533 | zinc finger MIZ-type containing 1 |
| [[ALDH4A1]] | 0.350 | aldehyde dehydrogenase 4 family member A1 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 154; `graph/modules.parquet` — module == 154; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [153] (drug-dose × line)
