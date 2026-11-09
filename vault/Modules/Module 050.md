---
module: 50
type: "module"
n_genes: 92
n_plus: 92
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.2711232006549835
label: "Extracellular matrix organization"
label_source: "reactome"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 050

*Extracellular matrix organization · 92 genes (single-armed) · [[Module 050.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

Label from the validation stage: **Extracellular matrix organization** (reactome, q 2e-05; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | Neutrophil degranulation | reactome | 17/92 | 7.57 | 8e-08 |
| + | Neutrophil degranulation | reactome | 17/92 | 7.57 | 8e-08 |
| + | Innate Immune System | reactome | 23/92 | 4.85 | 2e-07 |
| all | Innate Immune System | reactome | 23/92 | 4.85 | 2e-07 |
| all | Extracellular matrix organization | reactome | 12/92 | 8.13 | 2e-05 |
| + | Extracellular matrix organization | reactome | 12/92 | 8.13 | 2e-05 |
| + | Glycosphingolipid catabolism | reactome | 5/92 | 28.3 | 5e-04 |
| all | Glycosphingolipid catabolism | reactome | 5/92 | 28.3 | 5e-04 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 49), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Dinaciclib (drug)]] 0.5 µM (+12.1, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (+11.5, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+8.1, ⚠ toxic; transcription drop; cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (+5.2, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (+5.2, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (+4.8, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (+3.9, ⚠ cell-cycle shift); [[Docetaxel (drug)]] 0.05 µM (+3.4, ⚠ transcription drop; cell-cycle shift); [[Epirubicin (hydrochloride) (drug)]] 5 µM (+2.6, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (+2.1, ⚠ cell-cycle shift); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+2.0); [[XRK3F2 (drug)]] 0.5 µM (+1.6); [[Brivudine (drug)]] 5 µM (+1.4); [[9-ING-41 (drug)]] 0.5 µM (+1.3); [[Retinoic acid (drug)]] 0.05 µM (+1.3); [[Bimiralisib (drug)]] 0.5 µM (+1.2); [[Infigratinib (drug)]] 0.05 µM (+1.1); [[Tucidinostat (drug)]] 5 µM (+1.1); [[Entrectinib (drug)]] 5 µM (+1.1); [[Palmatine (chloride) (drug)]] 0.05 µM (+1.0) (28 in all, 18 with an alert ⚠; shown: the 10 strongest and the 10 next strongest without an alert)
- Lower it: [[Homoharringtonine (drug)]] 5 µM (-7.5, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-6.9, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-5.4, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (-3.9, ⚠ cell-cycle shift); [[Verteporfin (drug)]] 5 µM (-3.8); [[Homoharringtonine (drug)]] 0.05 µM (-2.8); [[Harringtonine (drug)]] 0.05 µM (-1.5); [[Digitoxin (drug)]] 0.05 µM (-1.4, ⚠ cell-cycle shift); [[5-Azacytidine (drug)]] 5 µM (-1.4); [[Glycyrrhizic acid (drug)]] 0.5 µM (-1.4); [[Vinblastine (sulfate) (drug)]] 5 µM (-1.3); [[Ciclopirox (drug)]] 5 µM (-1.2); [[Hydroxyurea (drug)]] 0.5 µM (-1.1); [[Sapanisertib (drug)]] 5 µM (-1.1); [[Dihydroartemisinin (drug)]] 5 µM (-1.1) (24 in all, 8 with an alert ⚠; shown: the 10 strongest and the 5 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[PANC-1 (line)]], [[HOP62 (line)]], [[KATO III (line)]], [[A-172 (line)]], [[HEC-1-A (line)]], [[NCI-H460 (line)]], [[J82 (line)]], [[MIA PaCa-2 (line)]]

## Candidate new members

*Members not annotated to the set their arm is enriched for, ranked by mean cos to the annotated members (`validation/novel_members.csv`); ⚠ = a reason to doubt the gene's place (in the vector space only through flagged drug-doses), kept in its rank. 23 candidates, none with an alert; shown: the 15 strongest.*

| # | Gene | Set | Mean cos |
|---|---|---|---|
| 1 | [[GRN]] | Glycosphingolipid catabolism | +0.58 |
| 2 | [[BSG]] | epithelial mesenchymal transition | +0.58 |
| 3 | [[PSAP]] | Degradation of the extracellular matrix | +0.57 |
| 4 | [[LAMP1]] | Degradation of the extracellular matrix | +0.57 |
| 5 | [[NUCB1]] | Degradation of the extracellular matrix | +0.56 |
| 6 | [[PRKCSH]] | Degradation of the extracellular matrix | +0.56 |
| 7 | [[NAGA]] | Extracellular matrix organization | +0.56 |
| 8 | [[ITM2C]] | Degradation of the extracellular matrix | +0.55 |
| 9 | [[PLBD2]] | Degradation of the extracellular matrix | +0.54 |
| 10 | [[SELENON]] | Extracellular matrix organization | +0.54 |
| 11 | [[PCYOX1]] | Glycosphingolipid catabolism | +0.53 |
| 12 | [[ATP6AP1]] | Glycosphingolipid catabolism | +0.53 |
| 13 | [[CTSD]] | Glycosphingolipid catabolism | +0.53 |
| 14 | [[GANAB]] | Extracellular matrix organization | +0.53 |
| 15 | [[MAN2B2]] | Extracellular matrix organization | +0.52 |

## + arm (92)

| Gene | Projection | Name |
|---|---|---|
| [[NAGA]] | 0.850 | alpha-N-acetylgalactosaminidase |
| [[SELENON]] | 0.844 | selenoprotein N |
| [[BSG]] | 0.830 | basigin (Ok blood group) |
| [[MAN2B2]] | 0.809 | mannosidase alpha class 2B member 2 |
| [[LAMP1]] | 0.799 | lysosome associated membrane protein 1 |
| [[PRKCSH]] | 0.790 | PRKCSH beta subunit of glucosidase II |
| [[PLBD2]] | 0.782 | phospholipase B domain containing 2 |
| [[AGPAT1]] | 0.775 | 1-acylglycerol-3-phosphate O-acyltransferase 1 |
| [[ITM2C]] | 0.772 | integral membrane protein 2C |
| [[ADAM15]] | 0.763 | ADAM metallopeptidase domain 15 |
| [[COLGALT1]] | 0.760 | collagen beta(1-O)galactosyltransferase 1 |
| [[CNPY3]] | 0.759 | canopy FGF signaling regulator 3 |
| [[CTSZ]] | 0.754 | cathepsin Z |
| [[SLC25A39]] | 0.751 | solute carrier family 25 member 39 |
| [[GANAB]] | 0.751 | glucosidase II alpha subunit |
| [[LRPAP1]] | 0.731 | LDL receptor related protein associated protein 1 |
| [[CLSTN1]] | 0.725 | calsyntenin 1 |
| [[CDK16]] | 0.723 | cyclin dependent kinase 16 |
| [[PRKACA]] | 0.721 | protein kinase cAMP-activated catalytic subunit alpha |
| [[NOMO1]] | 0.719 | NODAL modulator 1 |
| [[GM2A]] | 0.713 | ganglioside GM2 activator |
| [[ATP6AP1]] | 0.711 | ATPase H+ transporting accessory protein 1 |
| [[NUCB1]] | 0.711 | nucleobindin 1 |
| [[GRN]] | 0.700 | granulin precursor |
| [[PIGT]] | 0.696 | phosphatidylinositol glycan anchor biosynthesis class T |
| [[FAM234A]] | 0.694 | family with sequence similarity 234 member A |
| [[PCYOX1]] | 0.688 | prenylcysteine oxidase 1 |
| [[PLOD1]] | 0.688 | procollagen-lysine,2-oxoglutarate 5-dioxygenase 1 |
| [[MMP2]] | 0.687 | matrix metallopeptidase 2 |
| [[LGALS3BP]] | 0.686 | galectin 3 binding protein |
| [[LAMB2]] | 0.685 | laminin subunit beta 2 |
| [[GAA]] | 0.680 | alpha glucosidase |
| [[CALM3]] | 0.677 | calmodulin 3 |
| [[PIGS]] | 0.674 | phosphatidylinositol glycan anchor biosynthesis class S |
| [[DAG1]] | 0.664 | dystroglycan 1 |
| [[ECM1]] | 0.663 | extracellular matrix protein 1 |
| [[RTL8C]] | 0.654 | retrotransposon Gag like 8C |
| [[POMGNT1]] | 0.653 | protein O-linked mannose N-acetylglucosaminyltransferase 1 (beta 1,2-) |
| [[CELSR2]] | 0.649 | cadherin EGF LAG seven-pass G-type receptor 2 |
| [[NCSTN]] | 0.642 | nicastrin |
| [[RAB5C]] | 0.641 | RAB5C, member RAS oncogene family |
| [[APLP1]] | 0.638 | amyloid beta precursor like protein 1 |
| [[TIPRL]] | -0.629 | TOR signaling pathway regulator |
| [[CTSB]] | 0.620 | cathepsin B |
| [[ARSA]] | 0.619 | arylsulfatase A |
| [[IDS]] | 0.619 | iduronate 2-sulfatase |
| [[MAPK1]] | 0.619 | mitogen-activated protein kinase 1 |
| [[GLB1]] | 0.618 | galactosidase beta 1 |
| [[SIAE]] | 0.615 | sialic acid acetylesterase |
| [[MATN3]] | 0.613 | matrilin 3 |
| [[PSAP]] | 0.612 | prosaposin |
| [[GPC1]] | 0.609 | glypican 1 |
| [[CTSD]] | 0.595 | cathepsin D |
| [[NOMO3]] | 0.595 | NODAL modulator 3 |
| [[BLTP2]] | 0.594 | bridge-like lipid transfer protein family member 2 |
| [[ACADVL]] | 0.586 | acyl-CoA dehydrogenase very long chain |
| [[WRNIP1]] | 0.585 | WRN helicase interacting protein 1 |
| [[TLE5]] | 0.584 | TLE family member 5, transcriptional modulator |
| [[CS]] | 0.574 | citrate synthase |
| [[TIMP2]] | 0.574 | TIMP metallopeptidase inhibitor 2 |
| [[ZDHHC3]] | 0.561 | zDHHC palmitoyltransferase 3 |
| [[SDF4]] | 0.553 | stromal cell derived factor 4 |
| [[ENTREP3]] | 0.549 | endosomal transmembrane epsin interactor 3 |
| [[TP53I11]] | 0.546 | tumor protein p53 inducible protein 11 |
| [[TATDN2]] | 0.545 | TatD DNase domain containing 2 |
| [[STK35]] | 0.545 | serine/threonine kinase 35 |
| [[PLCG1]] | 0.538 | phospholipase C gamma 1 |
| [[EMC10]] | 0.533 | ER membrane protein complex subunit 10 |
| [[PRAF2]] | 0.531 | PRA1 domain family member 2 |
| [[SPRING1]] | 0.521 | SREBF pathway regulator in golgi 1 |
| [[FUCA1]] | 0.519 | alpha-L-fucosidase 1 |
| [[BRD3OS]] | 0.506 | BRD3 opposite strand |
| [[CTSF]] | 0.504 | cathepsin F |
| [[GPX3]] | 0.501 | glutathione peroxidase 3 |
| [[TTLL12]] | 0.497 | tubulin tyrosine ligase like 12 |
| [[PPP1CA]] | 0.491 | protein phosphatase 1 catalytic subunit alpha |
| [[IGF2]] | 0.489 | insulin like growth factor 2 |
| [[SHC1]] | 0.486 | SHC adaptor protein 1 |
| [[PPIA]] | 0.472 | peptidylprolyl isomerase A |
| [[CD302]] | 0.467 | CD302 molecule |
| [[APEH]] | 0.466 | acylaminoacyl-peptide hydrolase |
| [[BACE1]] | 0.457 | beta-secretase 1 |
| [[BCKDK]] | 0.452 | branched chain keto acid dehydrogenase kinase |
| [[GSTM2]] | 0.447 | glutathione S-transferase mu 2 |
| [[GPS1]] | 0.425 | G protein pathway suppressor 1 |
| [[PDHA1]] | 0.399 | pyruvate dehydrogenase E1 subunit alpha 1 |
| [[MAFG]] | -0.398 | MAF bZIP transcription factor G |
| [[SMPD1]] | 0.395 | sphingomyelin phosphodiesterase 1 |
| [[NPTXR]] | 0.368 | neuronal pentraxin receptor |
| [[IQCE]] | 0.360 | IQ motif containing E |
| [[AHI1]] | -0.324 | Abelson helper integration site 1 |
| [[USF2]] | 0.270 | upstream transcription factor 2, c-fos interacting |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 50; `graph/modules.parquet` — module == 50; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [49] (drug-dose × line)
