---
module: 52
type: "module"
n_genes: 89
n_plus: 76
n_minus: 13
arms_opposite: true
mean_cos_between_arms: -0.2614804208278656
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 052

*89 genes (76 in the + arm, 13 in the − arm) · [[Module 052.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26). The + arm rises where the − arm falls. Arm = the side of the module's main direction a gene sits on.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of the + arm minus the − arm (`graph/module_pooled_z.npy`, row 51), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it (+ arm up, − arm down): [[Panobinostat (drug)]] 0.5 µM (+5.0, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (+4.2, ⚠ cell-cycle shift); [[Auranofin (drug)]] 5 µM (+4.0); [[Dinaciclib (drug)]] 5 µM (+4.0, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (+3.4, ⚠ toxic; transcription drop; cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (+3.0, ⚠ cell-cycle shift); [[Adagrasib (drug)]] 0.05 µM (+2.4, ⚠ position not correctable); [[Belinostat (drug)]] 5 µM (+2.3, ⚠ cell-cycle shift); [[Lactate (calcium) (drug)]] 0.5 µM (+2.0); [[TAK-733 (drug)]] 5 µM (+1.9); [[TAK-733 (drug)]] 0.05 µM (+1.6); [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM (+1.6); [[Abemaciclib (drug)]] 5 µM (+1.6); [[c-Kit-IN-1 (drug)]] 5 µM (+1.6); [[EX229 (drug)]] 0.5 µM (+1.6); [[Sapanisertib (drug)]] 0.5 µM (+1.5); [[Methylthiouracil (drug)]] 0.5 µM (+1.5) (45 in all, 11 with an alert ⚠; shown: the 10 strongest and the 7 next strongest without an alert)
- Lower it: [[Homoharringtonine (drug)]] 5 µM (-17.1, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-13.4, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (-13.0, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 5 µM (-12.4, ⚠ toxic; transcription drop; cell-cycle shift); [[Niclosamide (olamine) (drug)]] 5 µM (-8.5, ⚠ toxic; cell-cycle shift); [[Digitoxin (drug)]] 0.5 µM (-8.3, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (-8.2, ⚠ cell-cycle shift); [[Selinexor (drug)]] 5 µM (-6.9, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (-6.8); [[TAK-901 (drug)]] 5 µM (-5.6, ⚠ cell-cycle shift); [[PH-797804 (drug)]] 5 µM (-3.8); [[Ponatinib (drug)]] 5 µM (-2.2); [[Tucidinostat (drug)]] 0.05 µM (-2.2); [[Verteporfin (drug)]] 5 µM (-2.1); [[Ixazomib citrate (drug)]] 0.5 µM (-2.1); [[Homoharringtonine (drug)]] 0.05 µM (-2.1); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM (-1.9); [[Cobimetinib (drug)]] 5 µM (-1.9); [[Belumosudil (drug)]] 5 µM (-1.8) (71 in all, 28 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[NCI-H460 (line)]], [[SW 900 (line)]], [[PANC-1 (line)]], [[SW480 (line)]], [[H4 (line)]], [[KATO III (line)]], [[HOP62 (line)]], [[AsPC-1 (line)]]

## + arm (76)

| Gene | Projection | Name |
|---|---|---|
| [[RER1]] | 0.837 | retention in endoplasmic reticulum sorting receptor 1 |
| [[GOLGA3]] | 0.817 | golgin A3 |
| [[PMM2]] | 0.814 | phosphomannomutase 2 |
| [[TMEM104]] | 0.805 | solute carrier family 38 member 12 |
| [[CHFR]] | 0.787 | checkpoint with forkhead and ring finger domains |
| [[GOSR2]] | 0.783 | golgi SNAP receptor complex member 2 |
| [[BET1L]] | 0.775 | Bet1 golgi vesicular membrane trafficking protein like |
| [[SZT2]] | 0.773 | SZT2 subunit of KICSTOR complex |
| [[DPP9]] | 0.768 | dipeptidyl peptidase 9 |
| [[YKT6]] | 0.759 | YKT6 vesicular SNARE protein |
| [[SEC16A]] | 0.750 | SEC16 homolog A, endoplasmic reticulum export factor |
| [[C11orf24]] | 0.745 | chromosome 11 open reading frame 24 |
| [[PDCD6]] | 0.732 | programmed cell death 6 |
| [[SENP5]] | 0.725 | SUMO specific peptidase 5 |
| [[FOXRED1]] | 0.721 | FAD dependent oxidoreductase domain containing 1 |
| [[BLCAP]] | 0.718 | BLCAP apoptosis inducing factor |
| [[B4GALT7]] | 0.712 | beta-1,4-galactosyltransferase 7 |
| [[FUBP3]] | 0.709 | far upstream element binding protein 3 |
| [[GAK]] | 0.700 | cyclin G associated kinase |
| [[SRA1]] | 0.700 | steroid receptor RNA activator 1 |
| [[UVSSA]] | 0.697 | UV stimulated scaffold protein A |
| [[ATG101]] | 0.697 | autophagy related 101 |
| [[PIGG]] | 0.695 | phosphatidylinositol glycan anchor biosynthesis class G (EMM blood group) |
| [[ZNF587]] | 0.691 | zinc finger protein 587 |
| [[VPS53]] | 0.690 | VPS53 subunit of GARP complex |
| [[TAF13]] | 0.684 | TATA-box binding protein associated factor 13 |
| [[GON4L]] | 0.680 | gon-4 like |
| [[ZNF275]] | 0.677 | zinc finger protein 275 |
| [[PRKAG1]] | 0.664 | protein kinase AMP-activated non-catalytic subunit gamma 1 |
| [[CHPF2]] | 0.653 | chondroitin polymerizing factor 2 |
| [[ZNF841]] | 0.652 | zinc finger protein 841 |
| [[EP400P1]] | 0.650 | EP400 pseudogene 1 |
| [[XPNPEP3]] | 0.626 | X-prolyl aminopeptidase 3 |
| [[MAP3K7]] | 0.618 | mitogen-activated protein kinase kinase kinase 7 |
| [[DIABLO]] | 0.611 | diablo IAP-binding mitochondrial protein |
| [[ANKS3]] | 0.610 | ankyrin repeat and sterile alpha motif domain containing 3 |
| [[LRRC59]] | 0.610 | leucine rich repeat containing 59 |
| [[FBH1]] | 0.602 | F-box DNA helicase 1 |
| [[DRD4]] | 0.597 | dopamine receptor D4 |
| [[C19orf25]] | 0.597 | chromosome 19 open reading frame 25 |
| [[ASCC2]] | 0.597 | activating signal cointegrator 1 complex subunit 2 |
| [[EIF1AD]] | 0.592 | eukaryotic translation initiation factor 1A domain containing |
| [[SPG7]] | 0.585 | SPG7 matrix AAA peptidase subunit, paraplegin |
| [[DDX19A]] | 0.576 | DEAD-box helicase 19A |
| [[GMPPB]] | 0.576 | GDP-mannose pyrophosphorylase B |
| [[POLR3D]] | 0.576 | RNA polymerase III subunit D |
| [[GNL2]] | 0.574 | G protein nucleolar 2 |
| [[POLG]] | 0.571 | DNA polymerase gamma, catalytic subunit |
| [[DCAKD]] | 0.562 | dephospho-CoA kinase domain containing |
| [[USP20]] | 0.557 | ubiquitin specific peptidase 20 |
| [[MBD1]] | 0.553 | methyl-CpG binding domain protein 1 |
| [[SLC25A44]] | 0.544 | solute carrier family 25 member 44 |
| [[GLYR1]] | 0.539 | glyoxylate reductase 1 homolog |
| [[EVI5L]] | 0.530 | ecotropic viral integration site 5 like |
| [[SLC25A16]] | 0.517 | solute carrier family 25 member 16 |
| [[SLC38A10]] | 0.513 | solute carrier family 38 member 10 |
| [[EDC3]] | 0.512 | enhancer of mRNA decapping 3 |
| [[SART1]] | 0.500 | spliceosome associated factor 1, recruiter of U4/U6.U5 tri-snRNP |
| [[PITPNA]] | 0.495 | phosphatidylinositol transfer protein alpha |
| [[C19orf47]] | 0.487 | chromosome 19 open reading frame 47 |
| [[SHPK]] | 0.487 | sedoheptulokinase |
| [[FTSJ1]] | 0.482 | FtsJ RNA 2'-O-methyltransferase 1 |
| [[UAP1]] | 0.477 | UDP-N-acetylglucosamine pyrophosphorylase 1 |
| [[AP3D1]] | 0.476 | adaptor related protein complex 3 subunit delta 1 |
| [[TMEM92-AS1]] | 0.475 | TMEM92 antisense RNA 1 |
| [[TMEM230]] | 0.459 | transmembrane protein 230 |
| [[STX16-NPEPL1]] | 0.440 | STX16-NPEPL1 readthrough (NMD candidate) |
| [[DDX50]] | 0.439 | DExD-box helicase 50 |
| [[TTLL11]] | 0.428 | tubulin tyrosine ligase like 11 |
| [[RABEP2]] | 0.426 | rabaptin, RAB GTPase binding effector protein 2 |
| [[SLC10A3]] | 0.401 | solute carrier family 10 member 3 |
| [[LINC02935]] | 0.396 | long independently transcribed non-coding RNA 2935 |
| [[CEP104]] | 0.377 | centrosomal protein 104 |
| [[SNF8]] | 0.331 | SNF8 subunit of ESCRT-II |
| [[CFDP1]] | 0.305 | chromatin remodeling protein CFDP1 |
| [[U2AF1]] | 0.285 | U2 small nuclear RNA auxiliary factor 1 |

## − arm (13)

| Gene | Projection | Name |
|---|---|---|
| [[SPPL3]] | -0.599 | signal peptide peptidase like 3 |
| [[MED13L]] | -0.592 | mediator complex subunit 13L |
| [[PUM1]] | -0.562 | pumilio RNA binding family member 1 |
| [[RPS6KA6]] | -0.544 | ribosomal protein S6 kinase A6 |
| [[KAT6A]] | -0.543 | lysine acetyltransferase 6A |
| [[NOTCH2NLR]] | -0.528 | notch 2 N-terminal like R |
| [[ISOC1]] | -0.470 | isochorismatase domain containing 1 |
| [[FAM171B]] | -0.452 | family with sequence similarity 171 member B |
| [[COX20]] | -0.393 | cytochrome c oxidase assembly factor COX20 |
| [[CEBPZOS]] | -0.366 | CEBPZ opposite strand |
| [[PPP6R3]] | -0.320 | protein phosphatase 6 regulatory subunit 3 |
| [[B3GALNT2]] | -0.230 | beta-1,3-N-acetylgalactosaminyltransferase 2 |
| [[ZNF670]] | -0.226 | zinc finger protein 670 |

## Data

- `graph/nodes.parquet` — module == 52; `graph/modules.parquet` — module == 52; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [51] (drug-dose × line)
