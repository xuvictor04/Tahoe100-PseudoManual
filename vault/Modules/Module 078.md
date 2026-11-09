---
module: 78
type: "module"
n_genes: 58
n_plus: 58
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.20196221768856049
label: "apical junction"
label_source: "hallmark"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 078

*apical junction · 58 genes (single-armed) · [[Module 078.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

Label from the validation stage: **apical junction** (hallmark, q 0.002; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | apical junction | hallmark | 7/58 | 11.0 | 0.002 |
| + | apical junction | hallmark | 7/58 | 11.0 | 0.002 |
| all | SARS-CoV-1 targets host intracellular signalling and regulatory pathways | reactome | 3/58 | 48.7 | 0.012 |
| + | SARS-CoV-1 targets host intracellular signalling and regulatory pathways | reactome | 3/58 | 48.7 | 0.012 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 77), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Dinaciclib (drug)]] 0.5 µM (+8.8, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (+8.0, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+6.3, ⚠ toxic; transcription drop; cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (+2.2); [[Lonafarnib (drug)]] 5 µM (+1.8, ⚠ toxic); [[Niclosamide (olamine) (drug)]] 5 µM (+1.8, ⚠ toxic; cell-cycle shift); [[Daptomycin (drug)]] 0.5 µM (+1.7, ⚠ unreliable plate only); [[Auranofin (drug)]] 5 µM (+1.7); [[Daptomycin (drug)]] 5 µM (+1.6, ⚠ unreliable plate only); [[Digitoxin (drug)]] 0.5 µM (+1.5, ⚠ cell-cycle shift); [[PF-06260933 (drug)]] 5 µM (+1.2); [[Peretinoin (drug)]] 5 µM (+1.2); [[vincristine (drug)]] 5 µM (+1.1); [[Mebendazole (drug)]] 5 µM (+1.1); [[Infigratinib (drug)]] 0.05 µM (+1.1); [[Busulfan (drug)]] 0.05 µM (+1.0) (22 in all, 14 with an alert ⚠; shown: the 10 strongest and the 6 next strongest without an alert)
- Lower it: [[Trametinib (drug)]] 5 µM (-4.0, ⚠ cell-cycle shift); [[Trametinib (drug)]] 0.5 µM (-3.4); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM (-3.1); [[Cobimetinib (drug)]] 5 µM (-3.1); [[Ponatinib (drug)]] 5 µM (-3.0); [[Binimetinib (drug)]] 0.5 µM (-3.0); [[Binimetinib (drug)]] 5 µM (-3.0); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM (-2.9); [[Binimetinib (drug)]] 0.05 µM (-2.9); [[Homoharringtonine (drug)]] 5 µM (-2.9, ⚠ cell-cycle shift); [[Trametinib (drug)]] 0.05 µM (-2.8); [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM (-2.8) (50 in all, 14 with an alert ⚠; shown: the 10 strongest and the 2 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[SW480 (line)]], [[C32 (line)]], [[SK-MEL-2 (line)]], [[PANC-1 (line)]], [[NCI-H1792 (line)]], [[NCI-H23 (line)]], [[MIA PaCa-2 (line)]], [[A498 (line)]]

## Candidate new members

*Members not annotated to the set their arm is enriched for, ranked by mean cos to the annotated members (`validation/novel_members.csv`); ⚠ = a reason to doubt the gene's place (in the vector space only through flagged drug-doses), kept in its rank. 10 candidates, none with an alert.*

| # | Gene | Set | Mean cos |
|---|---|---|---|
| 1 | [[CD59]] | apical junction | +0.57 |
| 2 | [[SEPTIN10]] | apical junction | +0.57 |
| 3 | [[MICAL2]] | apical junction | +0.57 |
| 4 | [[CORO1C]] | apical junction | +0.56 |
| 5 | [[NES]] | apical junction | +0.54 |
| 6 | [[BZW1]] | apical junction | +0.53 |
| 7 | [[PLXNA1]] | apical junction | +0.52 |
| 8 | [[TPM3]] | apical junction | +0.52 |
| 9 | [[STK4]] | apical junction | +0.52 |
| 10 | [[RALB]] | apical junction | +0.51 |

## + arm (58)

| Gene | Projection | Name |
|---|---|---|
| [[ACTN1]] | 0.851 | actinin alpha 1 |
| [[ITGA3]] | 0.815 | integrin subunit alpha 3 |
| [[NES]] | 0.781 | nestin |
| [[ITGB1]] | 0.777 | integrin subunit beta 1 |
| [[CORO1C]] | 0.758 | coronin 1C |
| [[MICAL2]] | 0.758 | microtubule associated monooxygenase, calponin and LIM domain containing 2 |
| [[CD59]] | 0.745 | CD59 molecule (CD59 blood group) |
| [[ARPC2]] | 0.739 | actin related protein 2/3 complex subunit 2 |
| [[RALB]] | 0.728 | RAS like proto-oncogene B |
| [[PLXNA1]] | 0.726 | plexin A1 |
| [[SEPTIN10]] | 0.714 | septin 10 |
| [[BZW1]] | 0.714 | basic leucine zipper and W2 domains 1 |
| [[MSN]] | 0.710 | moesin |
| [[PODXL]] | 0.705 | podocalyxin like |
| [[CDC42EP2]] | 0.697 | CDC42 effector protein 2 |
| [[CAP1]] | 0.693 | cyclase associated actin cytoskeleton regulatory protein 1 |
| [[ITPR3]] | 0.692 | inositol 1,4,5-trisphosphate receptor type 3 |
| [[MIR222HG]] | 0.683 | miR222/221 cluster host gene |
| [[COTL1]] | 0.681 | coactosin like F-actin binding protein 1 |
| [[TPM3]] | 0.671 | tropomyosin 3 |
| [[ANXA5]] | 0.670 | annexin A5 |
| [[STMN3]] | 0.670 | stathmin 3 |
| [[LAMC1]] | 0.663 | laminin subunit gamma 1 |
| [[PLEC]] | 0.654 | plectin |
| [[ASPH]] | 0.654 | aspartate beta-hydroxylase |
| [[F2R]] | 0.653 | coagulation factor II thrombin receptor |
| [[F2RL1]] | 0.645 | F2R like trypsin receptor 1 |
| [[EMP1]] | 0.644 | epithelial membrane protein 1 |
| [[ATP13A3]] | 0.643 | ATPase 13A3 |
| [[CLIC1]] | 0.637 | CLIC family member 1 |
| [[CSRP1]] | 0.633 | cysteine and glycine rich protein 1 |
| [[ARHGDIA]] | 0.628 | Rho GDP dissociation inhibitor alpha |
| [[ECE1]] | 0.617 | endothelin converting enzyme 1 |
| [[PLP2]] | 0.609 | proteolipid protein 2 |
| [[NFE2L3]] | 0.578 | NFE2 like bZIP transcription factor 3 |
| [[STK4]] | 0.577 | serine/threonine kinase 4 |
| [[OSBPL8]] | 0.564 | oxysterol binding protein like 8 |
| [[UXS1]] | 0.560 | UDP-glucuronate decarboxylase 1 |
| [[CDC37]] | 0.555 | cell division cycle 37, HSP90 cochaperone |
| [[AP1S2]] | 0.535 | adaptor related protein complex 1 subunit sigma 2 |
| [[GALNT1]] | 0.523 | polypeptide N-acetylgalactosaminyltransferase 1 |
| [[LTBP3]] | 0.502 | latent transforming growth factor beta binding protein 3 |
| [[TSPAN4]] | 0.499 | tetraspanin 4 |
| [[LRWD1]] | 0.494 | leucine rich repeats and WD repeat domain containing 1 |
| [[SMAD3]] | 0.494 | SMAD family member 3 |
| [[TRPV2]] | 0.488 | transient receptor potential cation channel subfamily V member 2 |
| [[ADGRE3]] | 0.483 | adhesion G protein-coupled receptor E3 |
| [[AKR1E2]] | 0.481 | aldo-keto reductase family 1 member E2 |
| [[YWHAB]] | 0.477 | tyrosine 3-monooxygenase/tryptophan 5-monooxygenase activation protein beta |
| [[ELFN2]] | 0.476 | extracellular leucine rich repeat and fibronectin type III domain containing 2 |
| [[ALDH1A3]] | 0.454 | aldehyde dehydrogenase 1 family member A3 |
| [[MYO5A]] | 0.438 | myosin VA |
| [[UBE2I]] | 0.413 | ubiquitin conjugating enzyme E2 I |
| [[ARF6]] | 0.408 | ARF GTPase 6 |
| [[RIPK4]] | 0.358 | receptor interacting serine/threonine kinase 4 |
| [[HSD11B2]] | -0.344 | hydroxysteroid 11-beta dehydrogenase 2 |
| [[PLTP]] | 0.318 | phospholipid transfer protein |
| [[SLC22A4]] | 0.220 | solute carrier family 22 member 4 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 78; `graph/modules.parquet` — module == 78; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [77] (drug-dose × line)
