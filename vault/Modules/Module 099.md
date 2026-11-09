---
module: 99
type: "module"
n_genes: 48
n_plus: 48
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.293888121843338
label: "hypoxia"
label_source: "hallmark"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 099

*hypoxia · 48 genes (single-armed) · [[Module 099.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

Label from the validation stage: **hypoxia** (hallmark, q 1e-17; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | hypoxia | hallmark | 17/48 | 29.3 | 1e-17 |
| + | hypoxia | hallmark | 17/48 | 29.3 | 1e-17 |
| + | mTORC1 signaling | hallmark | 15/48 | 24.0 | 6e-14 |
| all | mTORC1 signaling | hallmark | 15/48 | 24.0 | 6e-14 |
| all | Glycolysis | reactome | 10/48 | 49.1 | 1e-11 |
| + | Glycolysis | reactome | 10/48 | 49.1 | 1e-11 |
| + | Glucose metabolism | reactome | 10/48 | 44.2 | 3e-11 |
| all | Glucose metabolism | reactome | 10/48 | 44.2 | 3e-11 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 98), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Tucidinostat (drug)]] 5 µM (+3.3); [[Tucidinostat (drug)]] 0.5 µM (+2.6, ⚠ cell-cycle shift); [[PF-06260933 (drug)]] 5 µM (+2.4); [[Dimethyl fumarate (drug)]] 5 µM (+1.9); [[Cobimetinib (drug)]] 5 µM (+1.8); [[Fumaric acid (drug)]] 5 µM (+1.7); [[Roxadustat (drug)]] 5 µM (+1.6); [[palbociclib (drug)]] 0.5 µM (+1.5, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (+1.5, ⚠ cell-cycle shift); [[Pravastatin (sodium) (drug)]] 5 µM (+1.4); [[Daidzin (drug)]] 5 µM (+1.1); [[Terfenadine (drug)]] 5 µM (+1.1); [[Cloxacillin (sodium) (drug)]] 0.05 µM (+1.1) (18 in all, 6 with an alert ⚠; shown: the 10 strongest and the 3 next strongest without an alert)
- Lower it: [[Homoharringtonine (drug)]] 5 µM (-16.2, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-11.7, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-11.1, ⚠ cell-cycle shift); [[Niclosamide (olamine) (drug)]] 5 µM (-7.1, ⚠ toxic; cell-cycle shift); [[Topotecan (hydrochloride) (drug)]] 5 µM (-6.8, ⚠ toxic; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (-6.1, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (-5.8, ⚠ toxic; transcription drop; cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (-5.2, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (-4.3, ⚠ toxic; transcription drop; cell-cycle shift); [[Topotecan (hydrochloride) (drug)]] 0.5 µM (-3.9, ⚠ cell-cycle shift); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (-3.4); [[Clobetasol propionate (drug)]] 0.05 µM (-2.6); [[Belumosudil (drug)]] 5 µM (-1.9); [[5-Azacytidine (drug)]] 5 µM (-1.8); [[Amsacrine (drug)]] 5 µM (-1.7); [[GSK1059615 (drug)]] 5 µM (-1.7); [[Retinoic acid (drug)]] 0.05 µM (-1.6); [[Clobetasol propionate (drug)]] 0.5 µM (-1.6); [[Temsirolimus (drug)]] 0.05 µM (-1.5); [[Peretinoin (drug)]] 0.5 µM (-1.3) (54 in all, 24 with an alert ⚠; shown: the 10 strongest and the 10 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[C32 (line)]], [[RPMI-7951 (line)]], [[LOX-IMVI (line)]], [[HCT15 (line)]], [[NCI-H2347 (line)]], [[NCI-H1573 (line)]], [[CFPAC-1 (line)]], [[SW 900 (line)]]

## Candidate new members

*Members not annotated to the set their arm is enriched for, ranked by mean cos to the annotated members (`validation/novel_members.csv`); ⚠ = a reason to doubt the gene's place (in the vector space only through flagged drug-doses), kept in its rank. 24 candidates, none with an alert; shown: the 15 strongest.*

| # | Gene | Set | Mean cos |
|---|---|---|---|
| 1 | [[PGK1]] | Regulation of pyruvate metabolism | +0.66 |
| 2 | [[LDHA]] | Gluconeogenesis | +0.62 |
| 3 | [[INSIG2]] | hypoxia | +0.62 |
| 4 | [[HK2]] | hypoxia | +0.61 |
| 5 | [[ERO1A]] | Glycolysis | +0.60 |
| 6 | [[PDK3]] | hypoxia | +0.58 |
| 7 | [[PFKFB4]] | hypoxia | +0.58 |
| 8 | [[SLC2A1]] | Glycolysis | +0.58 |
| 9 | [[GPI]] | Regulation of pyruvate metabolism | +0.58 |
| 10 | [[EIF4A3]] | hypoxia | +0.57 |
| 11 | [[ALDOA]] | hypoxia | +0.56 |
| 12 | [[PKM]] | Gluconeogenesis | +0.56 |
| 13 | [[ENO1]] | Regulation of pyruvate metabolism | +0.55 |
| 14 | [[GAPDH]] | glycolysis | +0.55 |
| 15 | [[PFKFB3]] | hypoxia | +0.54 |

## + arm (48)

| Gene | Projection | Name |
|---|---|---|
| [[INSIG2]] | 0.902 | insulin induced gene 2 |
| [[PDK3]] | 0.873 | pyruvate dehydrogenase kinase 3 |
| [[ERO1A]] | 0.852 | endoplasmic reticulum oxidoreductase 1 alpha |
| [[HK2]] | 0.838 | hexokinase 2 |
| [[PGK1]] | 0.837 | phosphoglycerate kinase 1 |
| [[PFKFB4]] | 0.828 | 6-phosphofructo-2-kinase/fructose-2,6-biphosphatase 4 |
| [[CDON]] | 0.815 | cell adhesion associated, oncogene regulated |
| [[GPI]] | 0.792 | glucose-6-phosphate isomerase |
| [[TPD52]] | 0.789 | tumor protein D52 |
| [[HDAC3]] | 0.776 | histone deacetylase 3 |
| [[NXPH4]] | 0.757 | neurexophilin 4 |
| [[PDK1]] | 0.754 | pyruvate dehydrogenase kinase 1 |
| [[ALDOA]] | 0.740 | aldolase, fructose-bisphosphate A |
| [[GPR160]] | 0.739 | G protein-coupled receptor 160 |
| [[ALKBH5]] | 0.720 | alkB homolog 5, RNA demethylase |
| [[GAPDH]] | 0.720 | glyceraldehyde-3-phosphate dehydrogenase |
| [[SLC2A1]] | 0.719 | solute carrier family 2 member 1 |
| [[FHIP1A]] | 0.708 | FHF complex subunit HOOK interacting protein 1A |
| [[MLLT3]] | 0.706 | MLLT3 super elongation complex subunit |
| [[BNIP3]] | 0.695 | BCL2 interacting protein 3 |
| [[P4HA2]] | 0.695 | prolyl 4-hydroxylase subunit alpha 2 |
| [[EIF4A3]] | 0.683 | eukaryotic translation initiation factor 4A3 |
| [[FEM1C]] | 0.671 | fem-1 homolog C |
| [[RAB8B]] | 0.669 | RAB8B, member RAS oncogene family |
| [[PFKFB3]] | 0.613 | 6-phosphofructo-2-kinase/fructose-2,6-biphosphatase 3 |
| [[LRP1]] | 0.611 | LDL receptor related protein 1 |
| [[PLOD2]] | 0.601 | procollagen-lysine,2-oxoglutarate 5-dioxygenase 2 |
| [[RAP2A]] | 0.598 | RAP2A, member of RAS oncogene family |
| [[SLC6A6]] | 0.597 | solute carrier family 6 member 6 |
| [[TMEM65]] | 0.595 | transmembrane protein 65 |
| [[UBE2Q2P2]] | 0.595 | UBE2Q2 pseudogene 2 |
| [[BMT2]] | 0.595 | S-adenosylmethionine sensor upstream of mTORC1 |
| [[CDS1]] | 0.592 | CDP-diacylglycerol synthase 1 |
| [[TPI1]] | 0.586 | triosephosphate isomerase 1 |
| [[FAM13A-AS1]] | 0.582 | FAM13A antisense RNA 1 |
| [[BCKDHB]] | 0.579 | branched chain keto acid dehydrogenase E1 subunit beta |
| [[LDHA]] | 0.559 | lactate dehydrogenase A |
| [[ENO1]] | 0.549 | enolase 1 |
| [[TMEM144]] | 0.536 | transmembrane protein 144 |
| [[GBE1]] | 0.533 | 1,4-alpha-glucan branching enzyme 1 |
| [[KLHL32]] | 0.528 | kelch like family member 32 |
| [[PKM]] | 0.516 | pyruvate kinase M1/2 |
| [[LIMCH1]] | 0.507 | LIM and calponin homology domains 1 |
| [[C1RL-AS1]] | -0.497 | C1RL antisense RNA 1 |
| [[EGLN3]] | 0.483 | egl-9 family hypoxia inducible factor 3 |
| [[TEC]] | 0.478 | tec protein tyrosine kinase |
| [[HECTD1]] | -0.447 | HECT domain E3 ubiquitin protein ligase 1 |
| [[HIF1A-AS3]] | 0.389 | HIF1A antisense RNA 1 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 99; `graph/modules.parquet` — module == 99; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [98] (drug-dose × line)
