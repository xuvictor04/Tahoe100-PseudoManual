---
module: 47
type: "module"
n_genes: 95
n_plus: 95
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.26426973938941956
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 047

*95 genes (single-armed) · [[Module 047.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 46), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Dinaciclib (drug)]] 5 µM (+6.6, ⚠ toxic; transcription drop; cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (+6.2, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 5 µM (+6.0, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+4.3, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (+4.3, ⚠ toxic; transcription drop; cell-cycle shift); [[Panobinostat (drug)]] 5 µM (+4.1, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (+2.9); [[Auranofin (drug)]] 5 µM (+2.8); [[Filgotinib (drug)]] 5 µM (+2.8); [[Panobinostat (drug)]] 0.5 µM (+2.3, ⚠ cell-cycle shift); [[TAK-901 (drug)]] 0.05 µM (+2.1); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+1.9); [[Omeprazole (drug)]] 0.05 µM (+1.4); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM (+1.4); [[Lactate (calcium) (drug)]] 5 µM (+1.3); [[Filgotinib (drug)]] 0.05 µM (+1.3); [[Demeclocycline (drug)]] 5 µM (+1.3) (40 in all, 18 with an alert ⚠; shown: the 10 strongest and the 7 next strongest without an alert)
- Lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM (-5.7, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 0.5 µM (-5.1, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 5 µM (-4.0, ⚠ toxic; transcription drop; cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (-3.9, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 0.05 µM (-2.4, ⚠ cell-cycle shift); [[NG25 (drug)]] 5 µM (-2.4, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (-2.3, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 0.05 µM (-2.2, ⚠ cell-cycle shift); [[Radotinib (drug)]] 5 µM (-2.1); [[HI-TOPK-032 (drug)]] 0.05 µM (-1.8); [[Dimethyl fumarate (drug)]] 5 µM (-1.8); [[Bexarotene (drug)]] 5 µM (-1.5); [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM (-1.3); [[Cabozantinib (S-malate) (drug)]] 5 µM (-1.3); [[Dexamethasone (drug)]] 5 µM (-1.3); [[Pravastatin (sodium) (drug)]] 5 µM (-1.2); [[Homoharringtonine (drug)]] 0.05 µM (-1.2); [[Fumaric acid (drug)]] 5 µM (-1.2) (34 in all, 13 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[NCI-H23 (line)]], [[C-33 A (line)]], [[A-427 (line)]], [[PANC-1 (line)]], [[KATO III (line)]], [[NCI-H460 (line)]], [[AN3 CA (line)]], [[SNU-1 (line)]]

## + arm (95)

| Gene | Projection | Name |
|---|---|---|
| [[PITRM1-AS1]] | 0.884 | PITRM1 antisense RNA 1 |
| [[CHADL]] | 0.866 | chondroadherin like |
| [[LINC02236]] | 0.865 | long independently transcribed non-coding RNA 2236 |
| [[HPX]] | 0.842 | hemopexin |
| [[SPTBN5]] | 0.839 | spectrin beta, non-erythrocytic 5 |
| [[SH2D4B]] | 0.839 | SH2 domain containing 4B |
| [[CHRNA10]] | 0.836 | cholinergic receptor nicotinic alpha 10 subunit |
| [[TMEM25]] | 0.831 | transmembrane protein 25 |
| [[MSANTD1]] | 0.831 | Myb/SANT DNA binding domain containing 1 |
| [[SMIM41]] | 0.831 | small integral membrane protein 41 |
| [[MYO15A]] | 0.827 | myosin XVA |
| [[MMP25]] | 0.825 | matrix metallopeptidase 25 |
| [[ZDHHC11]] | 0.824 | zDHHC palmitoyltransferase 11 |
| [[SGSM3-AS1]] | 0.817 | SGSM3 antisense RNA 1 |
| [[EPHX3]] | 0.812 | epoxide hydrolase 3 |
| [[C19orf38]] | 0.810 | chromosome 19 open reading frame 38 |
| [[ALPK3]] | 0.801 | alpha kinase 3 |
| [[TTC36]] | 0.789 | tetratricopeptide repeat domain 36 |
| [[LINC02133]] | 0.771 | long independently transcribed non-coding RNA 2133 |
| [[CSPG5]] | 0.770 | chondroitin sulfate proteoglycan 5 |
| [[UCKL1-AS1]] | 0.768 | UCKL1 antisense RNA 1 |
| [[LAT2]] | 0.766 | linker for activation of T cells family member 2 |
| [[MYLK2]] | 0.749 | myosin light chain kinase 2 |
| [[SPATA32]] | 0.744 | spermatogenesis associated 32 |
| [[FERMT3]] | 0.743 | FERM domain containing kindlin 3 |
| [[MYH3]] | 0.739 | myosin heavy chain 3 |
| [[NECAB2]] | 0.737 | N-terminal EF-hand calcium binding protein 2 |
| [[LSMEM2]] | 0.733 | leucine rich single-pass membrane protein 2 |
| [[TLL2]] | 0.733 | tolloid like 2 |
| [[SPON2]] | 0.732 | spondin 2 |
| [[A3GALT2]] | 0.731 | alpha 1,3-galactosyltransferase 2 |
| [[TUBA8]] | 0.721 | tubulin alpha 8 |
| [[BLZF2P]] | 0.721 | basic leucine zipper nuclear factor 2, pseudogene |
| [[GAL3ST2]] | 0.720 | galactose-3-O-sulfotransferase 2 |
| [[PTCH2]] | 0.718 | patched 2 |
| [[BMP8A]] | 0.718 | bone morphogenetic protein 8a |
| [[NTRK1]] | 0.714 | neurotrophic receptor tyrosine kinase 1 |
| [[SLC2A9]] | 0.710 | solute carrier family 2 member 9 |
| [[MTNR1A]] | 0.698 | melatonin receptor 1A |
| [[FSCN2]] | 0.689 | fascin actin-bundling protein 2, retinal |
| [[STAC3]] | 0.683 | SH3 and cysteine rich domain 3 |
| [[CFAP161]] | 0.681 | cilia and flagella associated protein 161 |
| [[PIP5KL1]] | 0.670 | phosphatidylinositol-4-phosphate 5-kinase like 1 |
| [[HPN]] | 0.668 | hepsin |
| [[ATP8B5P-1]] | 0.667 | — |
| [[KIAA1614]] | 0.658 | KIAA1614 |
| [[AHRR]] | 0.654 | aryl hydrocarbon receptor repressor |
| [[IL20RB]] | 0.641 | interleukin 20 receptor subunit beta |
| [[KBTBD11-OT1-1]] | 0.639 | — |
| [[DNAH1]] | 0.636 | dynein axonemal heavy chain 1 |
| [[LINC00334]] | 0.635 | long independently transcribed non-coding RNA 334 |
| [[FAM53A]] | 0.631 | family with sequence similarity 53 member A |
| [[SYS1-DBNDD2]] | 0.628 | SYS1-DBNDD2 readthrough (NMD candidate) |
| [[RNF32-AS1]] | 0.626 | RNF32 antisense RNA 1 |
| [[DOK3]] | 0.625 | docking protein 3 |
| [[ZNF34]] | 0.612 | zinc finger protein 34 |
| [[PARVG]] | 0.607 | parvin gamma |
| [[BTBD16]] | 0.607 | BTB domain containing 16 |
| [[LINC01250]] | 0.605 | long independently transcribed non-coding RNA 1250 |
| [[KRT86]] | 0.604 | keratin 86 |
| [[FBXW10B]] | 0.603 | F-box and WD repeat domain containing 10B |
| [[MROH3P]] | 0.596 | maestro heat like repeat family member 3, pseudogene |
| [[HSD17B2-AS1]] | 0.584 | HSD17B2 antisense RNA 1 |
| [[CPLX1]] | 0.573 | complexin 1 |
| [[SRMS]] | 0.571 | src-related kinase lacking C-terminal regulatory tyrosine and N-terminal myristylation sites |
| [[SFXN5]] | 0.570 | sideroflexin 5 |
| [[MYADM-AS1]] | 0.568 | MYADM antisense RNA 1 |
| [[FER1L4]] | 0.565 | fer-1 like family member 4 (pseudogene) |
| [[TNNT2]] | 0.564 | troponin T2, cardiac type |
| [[GALNT8]] | 0.564 | polypeptide N-acetylgalactosaminyltransferase 8 |
| [[GHRLOS]] | 0.563 | ghrelin opposite strand/antisense RNA |
| [[NPAS1]] | 0.547 | neuronal PAS domain protein 1 |
| [[CYP2E1]] | 0.535 | cytochrome P450 family 2 subfamily E member 1 |
| [[LINC01277]] | 0.533 | long independently transcribed non-coding RNA 1277 |
| [[RAPGEFL1]] | 0.533 | Rap guanine nucleotide exchange factor like 1 |
| [[TPTE2P5]] | 0.480 | TPTE2 pseudogene 5 |
| [[HAL]] | 0.478 | histidine ammonia-lyase |
| [[CYP2D7]] | 0.473 | cytochrome P450 family 2 subfamily D member 7 (gene/pseudogene) |
| [[ADSS1]] | 0.470 | adenylosuccinate synthase 1 |
| [[SPON1-AS1]] | 0.458 | SPON1 antisense RNA 1 |
| [[NOTCH3]] | 0.457 | notch receptor 3 |
| [[SCN1B]] | 0.455 | sodium voltage-gated channel beta subunit 1 |
| [[CLCN4]] | 0.442 | Cl-/H+ antiporter 4 |
| [[FAM76A]] | -0.439 | family with sequence similarity 76 member A |
| [[SLC25A27]] | -0.438 | solute carrier family 25 member 27 |
| [[FAM3B]] | 0.438 | FAM3 metabolism regulating signaling molecule B |
| [[LINC00960]] | 0.424 | long independently transcribed non-coding RNA 960 |
| [[MYOM1]] | 0.418 | myomesin 1 |
| [[CCDC169]] | 0.418 | coiled-coil domain containing 169 |
| [[REP15]] | 0.399 | RAB15 effector protein |
| [[SCARF2]] | 0.399 | scavenger receptor class F member 2 |
| [[ATAD3C]] | 0.382 | ATPase family AAA domain containing 3C |
| [[NIPSNAP3A]] | -0.380 | nipsnap homolog 3A |
| [[RINL]] | 0.367 | Ras and Rab interactor like |
| [[SV2A]] | 0.336 | synaptic vesicle glycoprotein 2A |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 47; `graph/modules.parquet` — module == 47; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [46] (drug-dose × line)
