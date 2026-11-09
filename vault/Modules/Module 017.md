---
module: 17
type: "module"
n_genes: 202
n_plus: 171
n_minus: 31
arms_opposite: true
mean_cos_between_arms: -0.2804427742958069
label: "Intraflagellar transport"
label_source: "reactome"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 017

*Intraflagellar transport · 202 genes (171 in the + arm, 31 in the − arm) · [[Module 017.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28). The + arm rises where the − arm falls. Arm = the side of the module's main direction a gene sits on.

Label from the validation stage: **Intraflagellar transport** (reactome, q 0.002; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | Intraflagellar transport | reactome | 7/202 | 11.1 | 0.002 |
| all | Assembly of the 9+0 primary cilium | reactome | 12/202 | 4.89 | 0.003 |
| + | Assembly of the 9+0 primary cilium | reactome | 11/171 | 5.30 | 0.004 |
| + | Intraflagellar transport | reactome | 6/171 | 11.3 | 0.007 |
| all | Cilium Assembly | reactome | 12/202 | 4.39 | 0.009 |
| + | Cilium Assembly | reactome | 11/171 | 4.75 | 0.009 |
| + | Organelle biogenesis and maintenance | reactome | 12/171 | 3.61 | 0.046 |

## Drugs that move it

*Mean pooled z of the + arm minus the − arm (`graph/module_pooled_z.npy`, row 16), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it (+ arm up, − arm down): [[Panobinostat (drug)]] 0.5 µM (+8.0, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (+8.0, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (+7.5, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (+5.5, ⚠ cell-cycle shift); [[Selinexor (drug)]] 5 µM (+5.3, ⚠ cell-cycle shift); [[TAK-901 (drug)]] 5 µM (+4.6, ⚠ cell-cycle shift); [[Radotinib (drug)]] 5 µM (+4.4); [[Ponatinib (drug)]] 5 µM (+3.9); [[NG25 (drug)]] 5 µM (+3.7, ⚠ cell-cycle shift); [[Selinexor (drug)]] 0.5 µM (+3.6, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (+3.3); [[Brivudine (drug)]] 5 µM (+2.9); [[Flumatinib (mesylate) (drug)]] 5 µM (+2.3); [[PH-797804 (drug)]] 5 µM (+2.2); [[Cabozantinib (S-malate) (drug)]] 5 µM (+2.2); [[Trametinib (drug)]] 0.5 µM (+2.0); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM (+1.9); [[Ponatinib (drug)]] 0.05 µM (+1.8) (81 in all, 29 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)
- Lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM (-18.5, ⚠ cell-cycle shift); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (-9.1, ⚠ cell-cycle shift); [[Auranofin (drug)]] 5 µM (-7.4); [[Epirubicin (hydrochloride) (drug)]] 5 µM (-6.8, ⚠ cell-cycle shift); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (-6.2); [[Digitoxin (drug)]] 0.5 µM (-5.9, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (-5.6, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (-5.4, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 5 µM (-3.1, ⚠ toxic; transcription drop; cell-cycle shift); [[Digitoxin (drug)]] 0.05 µM (-3.0, ⚠ cell-cycle shift); [[5-Azacytidine (drug)]] 5 µM (-2.7); [[PF-06260933 (drug)]] 5 µM (-2.3); [[BAY1125976 (drug)]] 5 µM (-2.2); [[Demeclocycline (drug)]] 5 µM (-2.0); [[Peretinoin (drug)]] 5 µM (-2.0); [[Gefitinib (drug)]] 5 µM (-1.9); [[Pitavastatin (Calcium) (drug)]] 0.5 µM (-1.8); [[Filgotinib (drug)]] 5 µM (-1.7) (82 in all, 22 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[NCI-H460 (line)]], [[SW480 (line)]], [[HOP62 (line)]], [[PANC-1 (line)]], [[RKO (line)]], [[MIA PaCa-2 (line)]], [[LoVo (line)]], [[C32 (line)]]

## Candidate new members

*Members not annotated to the set their arm is enriched for, ranked by mean cos to the annotated members (`validation/novel_members.csv`); ⚠ = a reason to doubt the gene's place (in the vector space only through flagged drug-doses), kept in its rank. 11 candidates, none with an alert.*

| # | Gene | Set | Mean cos |
|---|---|---|---|
| 1 | [[NPHP1]] | Intraflagellar transport | +0.64 |
| 2 | [[BBS5]] | Intraflagellar transport | +0.56 |
| 3 | [[MRPS31P4]] | Intraflagellar transport | +0.56 |
| 4 | [[TBC1D19]] | Assembly of the 9+0 primary cilium | +0.54 |
| 5 | [[GPATCH11]] | Intraflagellar transport | +0.53 |
| 6 | [[POT1]] | Intraflagellar transport | +0.53 |
| 7 | [[TRAPPC11]] | Intraflagellar transport | +0.52 |
| 8 | [[SKIC3]] | Intraflagellar transport | +0.51 |
| 9 | [[ABITRAM]] | Intraflagellar transport | +0.51 |
| 10 | [[THOC1]] | Intraflagellar transport | +0.51 |
| 11 | [[DNAAF4]] | Intraflagellar transport | +0.51 |

## + arm (171)

| Gene | Projection | Name |
|---|---|---|
| [[MRPS31P4]] | 0.902 | mitochondrial ribosomal protein S31 pseudogene 4 |
| [[BBS5]] | 0.844 | Bardet-Biedl syndrome 5 |
| [[TRAPPC11]] | 0.797 | trafficking protein particle complex subunit 11 |
| [[PRPF39]] | 0.796 | pre-mRNA processing factor 39 |
| [[METTL14]] | 0.779 | methyltransferase 14, N6-adenosine-methyltransferase non-catalytic subunit |
| [[SKIC3]] | 0.778 | SKI3 subunit of superkiller complex |
| [[UBXN2B]] | 0.778 | UBX domain protein 2B |
| [[GEMIN2]] | 0.776 | gem nuclear organelle associated protein 2 |
| [[SAAL1]] | 0.776 | serum amyloid A like 1 |
| [[ESD]] | 0.772 | esterase D |
| [[COMMD2]] | 0.767 | COMM domain containing 2 |
| [[ZNF45]] | 0.758 | zinc finger protein 45 |
| [[HEATR6]] | 0.755 | HEAT repeat containing 6 |
| [[FAM133B]] | 0.754 | family with sequence similarity 133 member B |
| [[EHMT2]] | 0.753 | euchromatic histone lysine methyltransferase 2 |
| [[HPF1]] | 0.749 | histone PARylation factor 1 |
| [[SUGT1P4-STRA6LP]] | 0.749 | SUGT1P4-STRA6LP readthrough |
| [[TTC5]] | 0.738 | tetratricopeptide repeat domain 5 |
| [[POT1]] | 0.738 | protection of telomeres 1 |
| [[IRAK1BP1]] | 0.737 | interleukin 1 receptor associated kinase 1 binding protein 1 |
| [[THYN1]] | 0.732 | thymocyte nuclear protein 1 |
| [[THOC1]] | 0.731 | THO complex subunit 1 |
| [[DNAJC19]] | 0.731 | DnaJ heat shock protein family (Hsp40) member C19 |
| [[GPATCH11]] | 0.731 | G-patch domain containing 11 |
| [[NDUFA12]] | 0.725 | NADH:ubiquinone oxidoreductase subunit A12 |
| [[IFTAP]] | 0.724 | intraflagellar transport associated protein |
| [[RNF20]] | 0.723 | ring finger protein 20 |
| [[TTC26]] | 0.719 | intraflagellar transport 56 |
| [[RAD17]] | 0.719 | RAD17 checkpoint clamp loader component |
| [[STRA6LP]] | 0.718 | STRA6 like, pseudogene |
| [[METTL17]] | 0.717 | methyltransferase like 17 |
| [[ZNF14]] | 0.714 | zinc finger protein 14 |
| [[HARS2]] | 0.713 | histidyl-tRNA synthetase 2, mitochondrial |
| [[DYNC2LI1]] | 0.712 | dynein cytoplasmic 2 light intermediate chain 1 |
| [[WDR11]] | 0.706 | WD repeat domain 11 |
| [[NPHP1]] | 0.702 | nephrocystin 1 |
| [[SLC25A12]] | 0.701 | solute carrier family 25 member 12 |
| [[MRPS31P5-1]] | 0.684 | — |
| [[PKIG]] | 0.679 | cAMP-dependent protein kinase inhibitor gamma |
| [[NEPRO]] | 0.671 | ribonuclease MRP subunit p64 |
| [[DDX19B]] | 0.668 | DEAD-box helicase 19B |
| [[RFC1]] | 0.667 | replication factor C subunit 1 |
| [[DYNC2H1]] | 0.664 | dynein cytoplasmic 2 heavy chain 1 |
| [[RBM18]] | 0.661 | RNA binding motif protein 18 |
| [[FPGT]] | 0.657 | fucose-1-phosphate guanylyltransferase |
| [[TBC1D19]] | 0.656 | TBC1 domain family member 19 |
| [[NIPSNAP2]] | 0.656 | nipsnap homolog 2 |
| [[IFT172]] | 0.651 | intraflagellar transport 172 |
| [[FCSK]] | 0.642 | fucose kinase |
| [[ZDHHC17]] | 0.638 | zDHHC palmitoyltransferase 17 |
| [[PARP2]] | 0.636 | poly(ADP-ribose) polymerase 2 |
| [[QDPR]] | 0.636 | quinoid dihydropteridine reductase |
| [[ACTR10]] | 0.635 | actin related protein 10 |
| [[ADH5]] | 0.635 | alcohol dehydrogenase 5 (class III), chi polypeptide |
| [[METTL5]] | 0.627 | methyltransferase 5, N6-adenosine |
| [[MNAT1]] | 0.624 | MNAT1 component of CDK activating kinase |
| [[ZNF30]] | 0.624 | zinc finger protein 30 |
| [[AAAS]] | 0.619 | aladin WD repeat nucleoporin |
| [[MRPL16]] | 0.619 | mitochondrial ribosomal protein L16 |
| [[TTC38]] | 0.618 | tetratricopeptide repeat domain 38 |
| [[CDC73]] | 0.616 | cell division cycle 73 |
| [[ZYG11B]] | 0.615 | zyg-11 family member B, cell cycle regulator |
| [[IMMP1L]] | 0.614 | inner mitochondrial membrane peptidase subunit 1 |
| [[LINC00888]] | 0.614 | small nucleolar RNA host gene 33 |
| [[NECAP1]] | 0.613 | NECAP endocytosis associated 1 |
| [[GTF2H2C]] | 0.613 | GTF2H2 family member C |
| [[ABITRAM]] | 0.613 | actin binding transcription modulator |
| [[ZNF112]] | 0.613 | zinc finger protein 112 |
| [[MFSD13A]] | 0.610 | solute carrier family 68 member 1 |
| [[APC]] | 0.608 | APC regulator of Wnt signaling pathway |
| [[NEK3]] | 0.606 | NIMA related kinase 3 |
| [[ZNF18]] | 0.606 | zinc finger protein 18 |
| [[PLRG1]] | 0.605 | pleiotropic regulator 1 |
| [[DIXDC1]] | 0.602 | DIX domain containing 1 |
| [[COMMD8]] | 0.602 | COMM domain containing 8 |
| [[VTA1]] | 0.601 | vesicle trafficking 1 |
| [[EXOSC9]] | 0.600 | exosome component 9 |
| [[FRG1BP]] | 0.590 | FSHD region gene 1 family member B, pseudogene |
| [[RPAP3]] | 0.585 | RNA polymerase II associated protein 3 |
| [[TTC23]] | 0.585 | tetratricopeptide repeat domain 23 |
| [[DNAAF4]] | 0.575 | dynein axonemal assembly factor 4 |
| [[FITM2]] | 0.572 | fat storage inducing transmembrane protein 2 |
| [[NDUFAF5]] | 0.571 | NADH:ubiquinone oxidoreductase complex assembly factor 5 |
| [[PTCD3]] | 0.563 | pentatricopeptide repeat domain 3 |
| [[MIER1]] | 0.563 | MIER1 transcriptional regulator |
| [[C17orf58]] | 0.562 | chromosome 17 open reading frame 58 |
| [[POTEF]] | 0.561 | POTE ankyrin domain family member F |
| [[CCDC6]] | 0.559 | coiled-coil domain containing 6 |
| [[TTBK2]] | 0.559 | tau tubulin kinase 2 |
| [[TRIT1]] | 0.554 | tRNA isopentenyltransferase 1 |
| [[NSL1]] | 0.550 | NSL1 component of MIS12 kinetochore complex |
| [[COMMD7]] | 0.549 | COMM domain containing 7 |
| [[PRKAA1]] | 0.549 | protein kinase AMP-activated catalytic subunit alpha 1 |
| [[CEPT1]] | 0.545 | choline/ethanolamine phosphotransferase 1 |
| [[DUSP12]] | 0.543 | dual specificity phosphatase 12 |
| [[SRI]] | 0.542 | sorcin |
| [[TMEM254]] | 0.538 | transmembrane protein 254 |
| [[INIP]] | 0.538 | INTS3 and NABP interacting protein |
| [[SNX18]] | 0.536 | sorting nexin 18 |
| [[SUGT1P4-STRA6LP-CCDC180]] | 0.533 | SUGT1P4-STRA6LP-CCDC180 readthrough |
| [[KPNA5]] | 0.532 | karyopherin subunit alpha 5 |
| [[ZC4H2]] | 0.529 | zinc finger C4H2-type containing |
| [[KIFAP3]] | 0.528 | kinesin associated protein 3 |
| [[TTLL1]] | 0.525 | TTL family tubulin polyglutamylase complex subunit L1 |
| [[ELP3]] | 0.522 | elongator acetyltransferase complex subunit 3 |
| [[GTPBP8]] | 0.521 | GTP binding protein 8 |
| [[HNRNPDL]] | 0.521 | heterogeneous nuclear ribonucleoprotein D like |
| [[LYPLAL1]] | 0.520 | lysophospholipase like 1 |
| [[IFT22]] | 0.519 | intraflagellar transport 22 |
| [[TCAF1]] | 0.519 | TRPM8 channel associated factor 1 |
| [[LIAS]] | 0.511 | lipoic acid synthetase |
| [[SNX15]] | 0.506 | sorting nexin 15 |
| [[ZNF445]] | 0.504 | zinc finger protein 445 |
| [[ZNF184]] | 0.503 | zinc finger protein 184 |
| [[GUSBP2-1]] | 0.501 | — |
| [[TRIM32]] | 0.499 | tripartite motif containing 32 |
| [[C3orf14]] | 0.497 | centrosomal protein 15 |
| [[MED20]] | 0.496 | mediator complex subunit 20 |
| [[EIF2B4]] | 0.494 | eukaryotic translation initiation factor 2B subunit delta |
| [[MTMR4]] | 0.491 | myotubularin related protein 4 |
| [[SPIN1]] | 0.489 | spindlin 1 |
| [[PCCA]] | 0.489 | propionyl-CoA carboxylase subunit alpha |
| [[PRXL2C]] | 0.486 | peroxiredoxin like 2C |
| [[SNX11]] | 0.485 | sorting nexin 11 |
| [[BLOC1S5]] | 0.484 | biogenesis of lysosomal organelles complex 1 subunit 5 |
| [[MAP4K5]] | 0.476 | mitogen-activated protein kinase kinase kinase kinase 5 |
| [[TPR]] | 0.475 | translocated promoter region, nuclear basket protein |
| [[ATG3]] | 0.475 | autophagy related 3 |
| [[ROGDI]] | 0.471 | rogdi atypical leucine zipper |
| [[NBDY]] | 0.470 | negative regulator of P-body association |
| [[ARMC1]] | 0.469 | armadillo repeat containing 1 |
| [[BUD13]] | 0.454 | BUD13 spliceosome associated protein |
| [[VWDE]] | 0.454 | von Willebrand factor D and EGF domains |
| [[ARMC2]] | 0.454 | armadillo repeat containing 2 |
| [[PALS1]] | 0.452 | protein associated with LIN7 1, MAGUK p55 family member |
| [[ELAPOR2]] | 0.451 | endosome-lysosome associated apoptosis and autophagy regulator family member 2 |
| [[C1orf50]] | 0.446 | chromosome 1 open reading frame 50 |
| [[DMXL1]] | 0.445 | Dmx like 1 |
| [[CCNC]] | 0.444 | cyclin C |
| [[COX15]] | 0.444 | cytochrome c oxidase assembly factor COX15 |
| [[EBLN2]] | 0.437 | endogenous Bornavirus like nucleoprotein 2 |
| [[ABHD16A]] | 0.434 | abhydrolase domain containing 16A, phospholipase |
| [[ILVBL]] | 0.426 | 2-hydroxyacyl-CoA lyase 2 |
| [[CEP162]] | 0.413 | centrosomal protein 162 |
| [[BPNT1]] | 0.413 | 3'(2'), 5'-bisphosphate nucleotidase 1 |
| [[VPS54]] | 0.412 | VPS54 subunit of GARP complex |
| [[DNAL1]] | 0.412 | dynein axonemal light chain 1 |
| [[BAD]] | 0.411 | BCL2 associated agonist of cell death |
| [[VAPA]] | 0.410 | VAMP associated protein A |
| [[PIP4P1]] | 0.410 | phosphatidylinositol-4,5-bisphosphate 4-phosphatase 1 |
| [[ANKRD24]] | 0.404 | ankyrin repeat domain 24 |
| [[MTMR10]] | 0.399 | myotubularin related protein 10 |
| [[APOOL]] | 0.397 | apolipoprotein O like |
| [[CNOT4]] | 0.397 | CCR4-NOT transcription complex subunit 4 |
| [[PARP6]] | 0.394 | poly(ADP-ribose) polymerase family member 6 |
| [[CD99P1]] | 0.394 | CD99 molecule pseudogene 1 |
| [[RNF141]] | 0.384 | ring finger protein 141 |
| [[AKIP1]] | 0.357 | A-kinase interacting protein 1 |
| [[TBC1D32]] | 0.351 | TBC1 domain family member 32 |
| [[CCDC180]] | 0.350 | coiled-coil domain containing 180 |
| [[ACAT1]] | 0.342 | acetyl-CoA acetyltransferase 1 |
| [[RIDA]] | 0.332 | reactive intermediate imine deaminase A |
| [[DYNC1I2]] | 0.332 | dynein cytoplasmic 1 intermediate chain 2 |
| [[ODAD4]] | 0.320 | outer dynein arm docking complex subunit 4 |
| [[ZNF84]] | 0.297 | zinc finger protein 84 |
| [[FSD1L]] | 0.288 | fibronectin type III and SPRY domain containing 1 like |
| [[SCOC]] | 0.257 | short coiled-coil protein |
| [[SLC25A43]] | 0.253 | solute carrier family 25 member 43 |
| [[ANKRD13A]] | 0.233 | ankyrin repeat domain 13A |
| [[MITF]] | 0.218 | melanocyte inducing transcription factor |
| [[ZNF12]] | 0.207 | zinc finger protein 12 |

## − arm (31)

| Gene | Projection | Name |
|---|---|---|
| [[MIATNB]] | -0.655 | MIAT neighbor |
| [[HCG18]] | -0.648 | HLA complex group 18 |
| [[DDX5]] | -0.646 | DEAD-box helicase 5 |
| [[PDK1-AS1]] | -0.628 | ITGA6 and PDK1 antisense RNA 1 |
| [[ANKMY1]] | -0.625 | ankyrin repeat and MYND domain containing 1 |
| [[ATP11C]] | -0.599 | ATPase phospholipid transporting 11C (ATP11C blood group) |
| [[PLEKHA6]] | -0.598 | pleckstrin homology domain containing A6 |
| [[TLNRD1]] | -0.585 | talin rod domain containing 1 |
| [[SNTB2]] | -0.580 | syntrophin beta 2 |
| [[CDR2]] | -0.578 | cerebellar degeneration related protein 2 |
| [[ZNF800]] | -0.549 | zinc finger protein 800 |
| [[ZNF407]] | -0.538 | zinc finger protein 407 |
| [[KLHL29]] | -0.535 | kelch like family member 29 |
| [[FBXW7]] | -0.532 | F-box and WD repeat domain containing 7 |
| [[RAB22A]] | -0.527 | RAB22A, member RAS oncogene family |
| [[NACC2]] | -0.527 | NACC family member 2 |
| [[BANP]] | -0.516 | BTG3 associated nuclear protein |
| [[LARGE1]] | -0.501 | LARGE xylosyl- and glucuronyltransferase 1 |
| [[CASTOR3P-1]] | -0.496 | — |
| [[MROH1]] | -0.492 | maestro heat like repeat family member 1 |
| [[NUP50-DT]] | -0.489 | NUP50 divergent transcript |
| [[PRKCE]] | -0.486 | protein kinase C epsilon |
| [[LYPLA2]] | -0.472 | lysophospholipase 2 |
| [[MZF1]] | -0.471 | myeloid zinc finger 1 |
| [[MIB1]] | -0.464 | MIB E3 ubiquitin protein ligase 1 |
| [[CTTN]] | -0.434 | cortactin |
| [[TNRC18]] | -0.420 | trinucleotide repeat containing 18 |
| [[NQO1]] | -0.418 | NAD(P)H quinone dehydrogenase 1 |
| [[IFT140]] | -0.373 | intraflagellar transport 140 |
| [[KCNC3]] | -0.327 | potassium voltage-gated channel subfamily C member 3 |
| [[PCNX4]] | -0.231 | pecanex 4 |

## Data

- `graph/nodes.parquet` — module == 17; `graph/modules.parquet` — module == 17; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [16] (drug-dose × line)
