---
module: 7
type: "module"
n_genes: 235
n_plus: 224
n_minus: 11
arms_opposite: true
mean_cos_between_arms: -0.22182804346084595
label: "Dengue Virus-Host Interactions"
label_source: "reactome"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 007

*Dengue Virus-Host Interactions · 235 genes (224 in the + arm, 11 in the − arm) · [[Module 007.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22). The + arm rises where the − arm falls. Arm = the side of the module's main direction a gene sits on.

Label from the validation stage: **Dengue Virus-Host Interactions** (reactome, q 0.038; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| + | Metabolism of RNA | reactome | 31/224 | 2.86 | 8e-05 |
| all | Metabolism of RNA | reactome | 31/235 | 2.73 | 2e-04 |
| all | Viral Infection Pathways | reactome | 30/235 | 2.10 | 0.036 |
| + | Viral Infection Pathways | reactome | 29/224 | 2.13 | 0.036 |
| + | Dengue Virus-Host Interactions | reactome | 12/224 | 3.71 | 0.038 |

## Drugs that move it

*Mean pooled z of the + arm minus the − arm (`graph/module_pooled_z.npy`, row 6), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it (+ arm up, − arm down): [[Homoharringtonine (drug)]] 5 µM (+9.3, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (+8.8, ⚠ cell-cycle shift); [[Auranofin (drug)]] 5 µM (+6.2); [[Harringtonine (drug)]] 0.5 µM (+5.9, ⚠ cell-cycle shift); [[TAK-901 (drug)]] 5 µM (+5.9, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.05 µM (+5.0); [[Harringtonine (drug)]] 5 µM (+4.8, ⚠ cell-cycle shift); [[Selinexor (drug)]] 5 µM (+4.2, ⚠ cell-cycle shift); [[Topotecan (hydrochloride) (drug)]] 5 µM (+4.1, ⚠ toxic; cell-cycle shift); [[PH-797804 (drug)]] 5 µM (+3.9); [[Harringtonine (drug)]] 0.05 µM (+3.0); [[5-Azacytidine (drug)]] 5 µM (+2.8); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+2.8); [[TAK-901 (drug)]] 0.05 µM (+2.2); [[Larotrectinib (drug)]] 5 µM (+1.8); [[Ixazomib citrate (drug)]] 0.5 µM (+1.8); [[Belzutifan (drug)]] 5 µM (+1.7) (80 in all, 23 with an alert ⚠; shown: the 10 strongest and the 7 next strongest without an alert)
- Lower it: [[Digitoxin (drug)]] 5 µM (-7.3, ⚠ toxic; transcription drop; cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (-5.9, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (-5.0, ⚠ toxic; transcription drop; cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (-4.5, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 0.5 µM (-3.8, ⚠ cell-cycle shift); [[Niclosamide (olamine) (drug)]] 5 µM (-3.5, ⚠ toxic; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (-3.4, ⚠ toxic; transcription drop; cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 0.05 µM (-3.1, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (-2.9, ⚠ toxic; transcription drop; cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (-2.7); [[Verteporfin (drug)]] 5 µM (-2.4); [[Diammonium Glycyrrhizinate (drug)]] 5 µM (-1.7); [[Entecavir (monohydrate) (drug)]] 0.5 µM (-1.6); [[Arbutin (drug)]] 5 µM (-1.6); [[Bosentan (hydrate) (drug)]] 0.5 µM (-1.5); [[Tucidinostat (drug)]] 0.05 µM (-1.5); [[Dimethyl fumarate (drug)]] 5 µM (-1.4); [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM (-1.4); [[Sulfatinib (drug)]] 5 µM (-1.4) (49 in all, 15 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[HOP62 (line)]], [[LOX-IMVI (line)]], [[PANC-1 (line)]], [[HS-578T (line)]], [[LoVo (line)]], [[RKO (line)]], [[NCI-H460 (line)]], [[NCI-H23 (line)]]

## + arm (224)

| Gene | Projection | Name |
|---|---|---|
| [[CBLL1]] | 0.884 | Cbl proto-oncogene like 1 |
| [[SMG8]] | 0.869 | SMG8 nonsense mediated mRNA decay factor |
| [[ZNF629]] | 0.850 | zinc finger protein 629 |
| [[MOCS3]] | 0.841 | molybdenum cofactor synthesis 3 |
| [[GTF3C4]] | 0.830 | general transcription factor IIIC subunit 4 |
| [[ZBTB6]] | 0.829 | zinc finger and BTB domain containing 6 |
| [[CENPBD1P]] | 0.824 | CENPB DNA-binding domain containing 1, pseudogene |
| [[MRM3]] | 0.820 | mitochondrial rRNA methyltransferase 3 |
| [[TSSC4]] | 0.820 | tumor suppressing subtransferable candidate 4 |
| [[POP4]] | 0.818 | POP4 ribonuclease P/MRP subunit |
| [[TACO1]] | 0.805 | translational activator of cytochrome c oxidase I |
| [[ZSCAN29]] | 0.794 | zinc finger and SCAN domain containing 29 |
| [[ZNF646]] | 0.793 | zinc finger protein 646 |
| [[DDX28]] | 0.791 | DEAD-box helicase 28 |
| [[FEM1A]] | 0.786 | fem-1 homolog A |
| [[PSMD7]] | 0.780 | proteasome 26S subunit, non-ATPase 7 |
| [[TMEM199]] | 0.780 | vacuolar ATPase assembly factor VMA12 |
| [[ZNF845]] | 0.771 | zinc finger protein 845 |
| [[KTI12]] | 0.762 | KTI12 chromatin associated homolog |
| [[HCCS]] | 0.758 | holocytochrome c synthase |
| [[ZNF543]] | 0.754 | zinc finger protein 543 |
| [[ZNF614]] | 0.753 | zinc finger protein 614 |
| [[HPS6]] | 0.751 | HPS6 biogenesis of lysosomal organelles complex 2 subunit 3 |
| [[MED7]] | 0.739 | mediator complex subunit 7 |
| [[ERAL1]] | 0.735 | Era like 12S mitochondrial rRNA chaperone 1 |
| [[YTHDF2]] | 0.735 | YTH N6-methyladenosine RNA binding protein F2 |
| [[RBM15B]] | 0.734 | RNA binding motif protein 15B |
| [[ZBTB45]] | 0.732 | zinc finger and BTB domain containing 45 |
| [[C12orf43]] | 0.731 | chromosome 12 open reading frame 43 |
| [[ABT1]] | 0.730 | activator of basal transcription 1 |
| [[ZNF189]] | 0.726 | zinc finger protein 189 |
| [[ZNF426]] | 0.722 | zinc finger protein 426 |
| [[FBXO38]] | 0.720 | F-box protein 38 |
| [[RRN3]] | 0.718 | RNA polymerase I transcription factor RRN3 |
| [[SART3]] | 0.713 | spliceosome associated factor 3, U4/U6 recycling protein |
| [[JAGN1]] | 0.710 | jagunal vesicle mediated transporter 1 |
| [[DNTTIP2]] | 0.710 | deoxynucleotidyltransferase terminal interacting protein 2 |
| [[ZNF408]] | 0.709 | zinc finger protein 408 |
| [[TIMM22]] | 0.709 | translocase of inner mitochondrial membrane 22 |
| [[VCPIP1]] | 0.703 | valosin containing protein interacting protein 1 |
| [[JMJD4]] | 0.699 | jumonji domain containing 4 |
| [[CHD8]] | 0.699 | chromodomain helicase DNA binding protein 8 |
| [[DNAJB12]] | 0.698 | DnaJ heat shock protein family (Hsp40) member B12 |
| [[EXOC8]] | 0.697 | exocyst complex component 8 |
| [[GCC1]] | 0.694 | GRIP and coiled-coil domain containing 1 |
| [[TRMT10C]] | 0.692 | tRNA methyltransferase 10C, mitochondrial RNase P subunit |
| [[ZNF513]] | 0.692 | zinc finger protein 513 |
| [[ZNF623]] | 0.691 | zinc finger protein 623 |
| [[FADD]] | 0.690 | Fas associated via death domain |
| [[ZNF691]] | 0.689 | zinc finger protein 691 |
| [[MCRS1]] | 0.684 | microspherule protein 1 |
| [[ZXDB]] | 0.684 | zinc finger X-linked duplicated B |
| [[ZSWIM1]] | 0.682 | zinc finger SWIM-type containing 1 |
| [[GTF2E1]] | 0.681 | general transcription factor IIE subunit 1 |
| [[TMEM115]] | 0.679 | transmembrane protein 115 |
| [[ZNF701]] | 0.678 | zinc finger protein 701 |
| [[FTSJ3]] | 0.677 | FtsJ RNA 2'-O-methyltransferase 3 |
| [[COMMD5]] | 0.672 | COMM domain containing 5 |
| [[ZNF468]] | 0.664 | zinc finger protein 468 |
| [[TRMT5]] | 0.655 | tRNA methyltransferase 5 |
| [[KEAP1]] | 0.650 | kelch like ECH associated protein 1 |
| [[ZNF746]] | 0.650 | zinc finger protein 746 |
| [[PRKAB1]] | 0.646 | protein kinase AMP-activated non-catalytic subunit beta 1 |
| [[SMCR8]] | 0.646 | SMCR8-C9orf72 complex subunit |
| [[RBM42]] | 0.644 | RNA binding motif protein 42 |
| [[GPKOW]] | 0.643 | G-patch domain and KOW motifs |
| [[RNF25]] | 0.636 | ring finger protein 25 |
| [[ATMIN]] | 0.635 | ATM interactor |
| [[MRPL50]] | 0.635 | mitochondrial ribosomal protein L50 |
| [[MUL1]] | 0.631 | mitochondrial E3 ubiquitin protein ligase 1 |
| [[CDK12]] | 0.627 | cyclin dependent kinase 12 |
| [[PPIE]] | 0.626 | peptidylprolyl isomerase E |
| [[PRCC]] | 0.621 | proline rich mitotic checkpoint control factor |
| [[MRPL20-AS1]] | 0.619 | MRPL20 antisense RNA 1 |
| [[ZNF304]] | 0.619 | zinc finger protein 304 |
| [[CUL1]] | 0.616 | cullin 1 |
| [[PFDN1]] | 0.615 | prefoldin subunit 1 |
| [[ZNF574]] | 0.615 | zinc finger protein 574 |
| [[CD2BP2]] | 0.615 | CD2 cytoplasmic tail binding protein 2 |
| [[TOE1]] | 0.615 | target of EGR1, exonuclease |
| [[SRP68]] | 0.615 | signal recognition particle 68 |
| [[RAE1]] | 0.613 | ribonucleic acid export 1 |
| [[C6orf47]] | 0.612 | chromosome 6 open reading frame 47 |
| [[MRPL20]] | 0.610 | mitochondrial ribosomal protein L20 |
| [[THAP7]] | 0.602 | THAP domain containing 7 |
| [[ACTR8]] | 0.601 | actin related protein 8 |
| [[PHF23]] | 0.599 | PHD finger protein 23 |
| [[WAPL]] | 0.598 | WAPL cohesin release factor |
| [[ZNF564]] | 0.598 | zinc finger protein 564 |
| [[AUP1]] | 0.597 | AUP1 lipid droplet regulating VLDL assembly factor |
| [[MGAT2]] | 0.596 | alpha-1,6-mannosyl-glycoprotein 2-beta-N-acetylglucosaminyltransferase |
| [[FASTKD5]] | 0.592 | FASTK mitochondrial RNA regulator 5 |
| [[ASB6]] | 0.589 | ankyrin repeat and SOCS box containing 6 |
| [[CARD6]] | 0.586 | caspase recruitment domain family member 6 |
| [[RBM12B]] | 0.585 | RNA binding motif protein 12B |
| [[MED11]] | 0.584 | mediator complex subunit 11 |
| [[INTS5]] | 0.581 | integrator complex subunit 5 |
| [[TTC4]] | 0.578 | tetratricopeptide repeat domain 4 |
| [[RAB8A]] | 0.578 | RAB8A, member RAS oncogene family |
| [[CRNKL1]] | 0.576 | crooked neck pre-mRNA splicing factor 1 |
| [[SLC66A1]] | 0.575 | solute carrier family 66 member 1 |
| [[PCBP1]] | 0.572 | poly(rC) binding protein 1 |
| [[RIMOC1]] | 0.571 | RAB7A interacting MON1-CCZ1 complex subunit 1 |
| [[FEM1B]] | 0.565 | fem-1 homolog B |
| [[ZNF816]] | 0.563 | zinc finger protein 816 |
| [[PHF5A]] | 0.558 | PHD finger protein 5A |
| [[ZNF687]] | 0.558 | zinc finger protein 687 |
| [[MRPL49]] | 0.554 | mitochondrial ribosomal protein L49 |
| [[SLC35G2]] | 0.554 | solute carrier family 35 member G2 |
| [[EAF1]] | 0.554 | ELL associated factor 1 |
| [[ZNF561]] | 0.553 | zinc finger protein 561 |
| [[DDX23]] | 0.552 | DEAD-box helicase 23 |
| [[RBM22]] | 0.550 | RNA binding motif protein 22 |
| [[DNAJA2]] | 0.547 | DnaJ heat shock protein family (Hsp40) member A2 |
| [[TSPYL1]] | 0.543 | TSPY like 1 |
| [[CLP1]] | 0.543 | cleavage factor polyribonucleotide kinase subunit 1 |
| [[ZNF808]] | 0.540 | zinc finger protein 808 |
| [[BLOC1S3]] | 0.538 | biogenesis of lysosomal organelles complex 1 subunit 3 |
| [[NKIRAS2]] | 0.537 | NFKB inhibitor interacting Ras like 2 |
| [[GZF1]] | 0.537 | GDNF inducible zinc finger protein 1 |
| [[ZNF252P]] | 0.536 | zinc finger protein 252, pseudogene |
| [[ZNF813]] | 0.536 | zinc finger protein 813 |
| [[MSANTD7]] | 0.535 | Myb/SANT DNA binding domain containing 7 |
| [[SMIM10L1]] | 0.535 | small integral membrane protein 10 like 1 |
| [[VPS25]] | 0.534 | vacuolar protein sorting 25 homolog |
| [[BLOC1S4]] | 0.534 | biogenesis of lysosomal organelles complex 1 subunit 4 |
| [[LRRC14]] | 0.534 | leucine rich repeat containing 14 |
| [[TMEM184C]] | 0.533 | transmembrane protein 184C |
| [[ZBTB39]] | 0.532 | zinc finger and BTB domain containing 39 |
| [[ZBTB33]] | 0.531 | zinc finger and BTB domain containing 33 |
| [[SFT2D3]] | 0.530 | SFT2 domain containing 3 |
| [[AMMECR1L]] | 0.530 | AMMECR1 like |
| [[ZBTB40]] | 0.529 | zinc finger and BTB domain containing 40 |
| [[OTUB1]] | 0.528 | OTU deubiquitinase, ubiquitin aldehyde binding 1 |
| [[MRPL9]] | 0.527 | mitochondrial ribosomal protein L9 |
| [[RRP36]] | 0.526 | ribosomal RNA processing 36 |
| [[L3MBTL2]] | 0.524 | L3MBTL histone methyl-lysine binding protein 2 |
| [[ZNF597]] | 0.523 | zinc finger protein 597 |
| [[EIF2B2]] | 0.522 | eukaryotic translation initiation factor 2B subunit beta |
| [[PSMC2]] | 0.519 | proteasome 26S subunit, ATPase 2 |
| [[TPGS1]] | 0.516 | tubulin polyglutamylase complex subunit 1 |
| [[ZNF222]] | 0.515 | zinc finger protein 222 |
| [[SMIM15]] | 0.508 | small integral membrane protein 15 |
| [[PARP3]] | 0.507 | poly(ADP-ribose) polymerase family member 3 |
| [[TIMM8B]] | 0.506 | translocase of inner mitochondrial membrane 8 homolog B |
| [[KCTD10]] | 0.504 | potassium channel tetramerization domain containing 10 |
| [[RPL26L1]] | 0.500 | ribosomal protein L26 like 1 |
| [[SEPHS2]] | 0.500 | selenophosphate synthetase 2 |
| [[PLPP6]] | 0.499 | phospholipid phosphatase 6 |
| [[COA3]] | 0.499 | cytochrome c oxidase assembly factor 3 |
| [[GEMIN6]] | 0.499 | gem nuclear organelle associated protein 6 |
| [[RPP25]] | 0.498 | ribonuclease P/MRP subunit p25 |
| [[LBHD1]] | 0.497 | LBH domain containing 1 |
| [[ADRM1]] | 0.493 | ADRM1 26S proteasome ubiquitin receptor |
| [[ZNF436]] | 0.492 | zinc finger protein 436 |
| [[PRR14L]] | 0.491 | proline rich 14 like |
| [[ZBED1]] | 0.490 | zinc finger BED-type containing 1 |
| [[EXOSC4]] | 0.490 | exosome component 4 |
| [[TP73-AS1]] | 0.489 | Gfo/Idh/MocA-like oxidoreductase domain containing 3, pseudogene |
| [[PGBD2]] | 0.479 | piggyBac transposable element derived 2 |
| [[LEMD2]] | 0.477 | LEM domain nuclear envelope protein 2 |
| [[TM2D2]] | 0.473 | TM2 domain containing 2 |
| [[ZMAT2]] | 0.466 | zinc finger matrin-type 2 |
| [[EXOC3-AS1]] | 0.461 | EXOC3 antisense RNA 1 |
| [[DCLRE1C]] | 0.454 | DNA cross-link repair 1C |
| [[DOK1]] | 0.454 | docking protein 1 |
| [[CTCF]] | 0.452 | CCCTC-binding factor |
| [[TGS1]] | 0.451 | trimethylguanosine synthase 1 |
| [[SMARCAL1]] | 0.449 | SNF2 related chromatin remodeling annealing helicase 1 |
| [[LAMTOR1]] | 0.446 | late endosomal/lysosomal adaptor, MAPK and MTOR activator 1 |
| [[ZNF256]] | 0.445 | zinc finger protein 256 |
| [[ZNF770]] | 0.443 | zinc finger protein 770 |
| [[THAP11]] | 0.438 | THAP domain containing 11 |
| [[MOB4]] | 0.438 | MOB family member 4, phocein |
| [[KHNYN]] | 0.436 | KH and NYN domain containing |
| [[GTF2F1]] | 0.432 | general transcription factor IIF subunit 1 |
| [[TRAPPC3]] | 0.430 | trafficking protein particle complex subunit 3 |
| [[DOLPP1]] | 0.429 | dolichyldiphosphatase 1 |
| [[MFAP3]] | 0.429 | microfibril associated protein 3 |
| [[BNIP2]] | 0.427 | BCL2 interacting protein 2 |
| [[BORCS8]] | 0.423 | BLOC-1 related complex subunit 8 |
| [[TMEM250]] | 0.420 | transmembrane protein 250 |
| [[UBE2Q1]] | 0.416 | ubiquitin conjugating enzyme E2 Q1 |
| [[DPH3]] | 0.411 | diphthamide biosynthesis 3 |
| [[ARL16]] | 0.411 | ARF like GTPase 16 |
| [[ZNF48]] | 0.404 | zinc finger protein 48 |
| [[NELFE]] | 0.401 | negative elongation factor complex member E |
| [[CCNT1]] | 0.400 | cyclin T1 |
| [[ARRDC1-AS1]] | 0.390 | ARRDC1 antisense RNA 1 |
| [[CNOT11]] | 0.388 | CCR4-NOT transcription complex subunit 11 |
| [[XRCC4]] | 0.388 | X-ray repair cross complementing 4 |
| [[LRRC61]] | 0.383 | leucine rich repeat containing 61 |
| [[SPATA2]] | 0.382 | spermatogenesis associated 2 |
| [[CPTP]] | 0.380 | ceramide-1-phosphate transfer protein |
| [[EIF3G]] | 0.379 | eukaryotic translation initiation factor 3 subunit G |
| [[SPRTN]] | 0.377 | SprT-like N-terminal domain |
| [[SPR]] | 0.376 | sepiapterin reductase |
| [[B3GALT6]] | 0.375 | beta-1,3-galactosyltransferase 6 |
| [[ZNF384]] | 0.373 | zinc finger protein 384 |
| [[CC2D1B]] | 0.361 | coiled-coil and C2 domain containing 1B |
| [[TMEM127]] | 0.360 | transmembrane protein 127 |
| [[SNX21]] | 0.358 | sorting nexin family member 21 |
| [[SBDSP1-1]] | 0.356 | — |
| [[SLC30A1]] | 0.351 | solute carrier family 30 member 1 |
| [[STOML2]] | 0.348 | stomatin like 2 |
| [[MMAA]] | 0.348 | metabolism of cobalamin associated A |
| [[FBXL19]] | 0.343 | F-box and leucine rich repeat protein 19 |
| [[PNMA1]] | 0.328 | PNMA family member 1 |
| [[DGUOK]] | 0.320 | deoxyguanosine kinase |
| [[SLC9A3]] | 0.316 | solute carrier family 9 member A3 |
| [[MSRB1]] | 0.310 | methionine sulfoxide reductase B1 |
| [[IDH3B]] | 0.309 | isocitrate dehydrogenase (NAD(+)) 3 non-catalytic subunit beta |
| [[DLX1]] | 0.299 | distal-less homeobox 1 |
| [[CTDSP1]] | 0.298 | CTD small phosphatase 1 |
| [[UROD]] | 0.296 | uroporphyrinogen decarboxylase |
| [[C18orf25]] | 0.293 | arkadia (RNF111) N-terminal like PKA signaling regulator 2N |
| [[PRAME]] | 0.271 | PRAME nuclear receptor transcriptional regulator |
| [[ABHD15]] | 0.229 | abhydrolase domain containing 15 |
| [[CSNK2B]] | 0.194 | casein kinase 2 beta |
| [[CYBC1]] | 0.183 | cytochrome b-245 chaperone 1 |
| [[TOR1AIP2]] | 0.180 | torsin 1A interacting protein 2 |
| [[ASPSCR1]] | 0.142 | ASPSCR1 tether for SLC2A4, UBX domain containing |
| [[EMD]] | 0.114 | emerin |
| [[KHSRP]] | 0.0819 | KH-type splicing regulatory protein |

## − arm (11)

| Gene | Projection | Name |
|---|---|---|
| [[PTMA]] | -0.645 | prothymosin alpha |
| [[SEPTIN2]] | -0.591 | septin 2 |
| [[AP3S1]] | -0.529 | adaptor related protein complex 3 subunit sigma 1 |
| [[ATP1B3]] | -0.496 | ATPase Na+/K+ transporting subunit beta 3 |
| [[TMSB4X]] | -0.429 | thymosin beta 4 X-linked |
| [[CSPP1]] | -0.413 | centrosome and spindle pole associated protein 1 |
| [[PDE8A]] | -0.396 | phosphodiesterase 8A |
| [[SUMO2]] | -0.310 | small ubiquitin like modifier 2 |
| [[EIF3K]] | -0.302 | eukaryotic translation initiation factor 3 subunit K |
| [[PERP]] | -0.220 | p53 apoptosis effector related to PMP22 |
| [[ODF2L]] | -0.172 | outer dense fiber of sperm tails 2 like |

## Data

- `graph/nodes.parquet` — module == 7; `graph/modules.parquet` — module == 7; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [6] (drug-dose × line)
