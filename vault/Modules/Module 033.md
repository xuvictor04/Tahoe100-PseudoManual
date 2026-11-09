---
module: 33
type: "module"
n_genes: 139
n_plus: 129
n_minus: 10
arms_opposite: true
mean_cos_between_arms: -0.27439653873443604
label: "MYC targets v2"
label_source: "hallmark"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 033

*MYC targets v2 · 139 genes (129 in the + arm, 10 in the − arm) · [[Module 033.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27). The + arm rises where the − arm falls. Arm = the side of the module's main direction a gene sits on.

Label from the validation stage: **MYC targets v2** (hallmark, q 2e-05; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| + | MYC targets v2 | hallmark | 8/129 | 16.1 | 2e-05 |
| all | MYC targets v2 | hallmark | 8/139 | 15.0 | 4e-05 |
| + | Major pathway of rRNA processing in the nucleolus and cytosol | reactome | 10/129 | 6.60 | 0.002 |
| + | rRNA processing in the nucleus and cytosol | reactome | 10/129 | 6.25 | 0.002 |
| all | Major pathway of rRNA processing in the nucleolus and cytosol | reactome | 10/139 | 6.13 | 0.003 |
| all | rRNA processing in the nucleus and cytosol | reactome | 10/139 | 5.80 | 0.004 |
| + | rRNA modification in the nucleus and cytosol | reactome | 6/129 | 12.1 | 0.005 |
| + | rRNA processing | reactome | 10/129 | 5.73 | 0.005 |

## Drugs that move it

*Mean pooled z of the + arm minus the − arm (`graph/module_pooled_z.npy`, row 32), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it (+ arm up, − arm down): [[c-Kit-IN-1 (drug)]] 0.05 µM (+7.0, ⚠ unreliable plate only); [[PH-797804 (drug)]] 5 µM (+5.9); [[TAK-901 (drug)]] 5 µM (+5.4, ⚠ cell-cycle shift); [[EX229 (drug)]] 5 µM (+4.5); [[c-Kit-IN-1 (drug)]] 5 µM (+3.9); [[TAK-733 (drug)]] 5 µM (+3.6); [[Belumosudil (drug)]] 5 µM (+3.4); [[venetoclax (drug)]] 5 µM (+3.0); [[Selinexor (drug)]] 5 µM (+2.7, ⚠ cell-cycle shift); [[TAK-901 (drug)]] 0.05 µM (+2.5); [[Abemaciclib (drug)]] 5 µM (+2.5); [[EX229 (drug)]] 0.5 µM (+2.1); [[Clobetasol propionate (drug)]] 0.05 µM (+2.0) (54 in all, 17 with an alert ⚠; shown: the 10 strongest and the 3 next strongest without an alert)
- Lower it: [[Homoharringtonine (drug)]] 5 µM (-11.7, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (-11.6, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (-8.7, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-7.0, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 5 µM (-6.6, ⚠ toxic; transcription drop; cell-cycle shift); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (-6.4, ⚠ cell-cycle shift); [[Epirubicin (hydrochloride) (drug)]] 5 µM (-6.1, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 0.5 µM (-5.5, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (-5.2, ⚠ cell-cycle shift); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (-3.6); [[Pitavastatin (Calcium) (drug)]] 0.5 µM (-2.3); [[Cobimetinib (drug)]] 5 µM (-2.2); [[Auranofin (drug)]] 5 µM (-2.2); [[PF-06260933 (drug)]] 5 µM (-2.0); [[Trametinib (drug)]] 0.5 µM (-1.9); [[Entrectinib (drug)]] 5 µM (-1.8); [[Binimetinib (drug)]] 5 µM (-1.7); [[RMC-6236 (drug)]] 5 µM (-1.6); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM (-1.6) (49 in all, 21 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[PANC-1 (line)]], [[NCI-H460 (line)]], [[SW480 (line)]], [[MIA PaCa-2 (line)]], [[RKO (line)]], [[SW1417 (line)]], [[HOP62 (line)]], [[A498 (line)]]

## Candidate new members

*Members not annotated to the set their arm is enriched for, ranked by mean cos to the annotated members (`validation/novel_members.csv`); ⚠ = a reason to doubt the gene's place (in the vector space only through flagged drug-doses), kept in its rank. 47 candidates, none with an alert; shown: the 15 strongest.*

| # | Gene | Set | Mean cos |
|---|---|---|---|
| 1 | [[POLR1B]] | rRNA modification in the nucleus and cytosol | +0.75 |
| 2 | [[NLE1]] | rRNA modification in the nucleus and cytosol | +0.67 |
| 3 | [[WDR3]] | MYC targets v2 | +0.66 |
| 4 | [[NSUN2]] | rRNA modification in the nucleus and cytosol | +0.65 |
| 5 | [[NOL10]] | rRNA modification in the nucleus and cytosol | +0.65 |
| 6 | [[EIF3B]] | rRNA modification in the nucleus and cytosol | +0.61 |
| 7 | [[POLR3H]] | rRNA modification in the nucleus and cytosol | +0.60 |
| 8 | [[GEMIN5]] | rRNA modification in the nucleus and cytosol | +0.59 |
| 9 | [[NARS2]] | rRNA modification in the nucleus and cytosol | +0.59 |
| 10 | [[EXOSC5]] | rRNA modification in the nucleus and cytosol | +0.59 |
| 11 | [[SNHG17]] | rRNA modification in the nucleus and cytosol | +0.58 |
| 12 | [[AHCTF1]] | rRNA modification in the nucleus and cytosol | +0.58 |
| 13 | [[POLR3B]] | rRNA modification in the nucleus and cytosol | +0.57 |
| 14 | [[WDR36]] | MYC targets v2 | +0.57 |
| 15 | [[USP10]] | rRNA modification in the nucleus and cytosol | +0.57 |

## + arm (129)

| Gene | Projection | Name |
|---|---|---|
| [[NLE1]] | 0.911 | notchless homolog 1 |
| [[POLR1B]] | 0.905 | RNA polymerase I subunit B |
| [[WDR3]] | 0.895 | WD repeat domain 3 |
| [[FXN]] | 0.815 | frataxin |
| [[DHODH]] | 0.810 | dihydroorotate dehydrogenase (quinone) |
| [[GEMIN5]] | 0.808 | gem nuclear organelle associated protein 5 |
| [[TMEM177]] | 0.801 | transmembrane protein 177 |
| [[NOL10]] | 0.791 | nucleolar protein 10 |
| [[MRPL4]] | 0.789 | mitochondrial ribosomal protein L4 |
| [[WDR36]] | 0.788 | WD repeat domain 36 |
| [[POLR3H]] | 0.787 | RNA polymerase III subunit H |
| [[NARS2]] | 0.780 | asparaginyl-tRNA synthetase 2, mitochondrial |
| [[DDX55]] | 0.775 | DEAD-box helicase 55 |
| [[NKRF]] | 0.769 | NFKB repressing factor |
| [[SNHG17]] | 0.768 | small nucleolar RNA host gene 17 |
| [[ASB13]] | 0.762 | ankyrin repeat and SOCS box containing 13 |
| [[UTP18]] | 0.761 | UTP18 small subunit processome component |
| [[POLR3B]] | 0.761 | RNA polymerase III subunit B |
| [[RCL1]] | 0.759 | RNA terminal phosphate cyclase like 1 |
| [[RRP1B]] | 0.758 | ribosomal RNA processing 1B |
| [[EXOSC5]] | 0.756 | exosome component 5 |
| [[ZNF692]] | 0.750 | zinc finger protein 692 |
| [[PDSS1]] | 0.748 | decaprenyl diphosphate synthase subunit 1 |
| [[MRPS23]] | 0.747 | mitochondrial ribosomal protein S23 |
| [[CTU1]] | 0.737 | cytosolic thiouridylase subunit 1 |
| [[NUFIP1]] | 0.727 | nuclear FMR1 interacting protein 1 |
| [[WDR43]] | 0.720 | WD repeat domain 43 |
| [[ALKBH2]] | 0.717 | alkB homolog 2, alpha-ketoglutarate dependent dioxygenase |
| [[RITA1]] | 0.716 | RBPJ interacting and tubulin associated 1 |
| [[NPM3]] | 0.707 | nucleophosmin/nucleoplasmin 3 |
| [[ORC5]] | 0.706 | origin recognition complex subunit 5 |
| [[NUDCD3]] | 0.706 | NudC domain containing 3 |
| [[DCAF4]] | 0.704 | DDB1 and CUL4 associated factor 4 |
| [[TBC1D14]] | 0.704 | TBC1 domain family member 14 |
| [[SLX9]] | 0.703 | SLX9 ribosome biogenesis factor |
| [[FARSA]] | 0.701 | phenylalanyl-tRNA synthetase subunit alpha |
| [[MANEAL]] | 0.697 | mannosidase endo-alpha like |
| [[USP10]] | 0.693 | ubiquitin specific peptidase 10 |
| [[ZNF74]] | 0.692 | zinc finger protein 74 |
| [[DCTPP1]] | 0.690 | dCTP pyrophosphatase 1 |
| [[MCAT]] | 0.688 | malonyl-CoA-acyl carrier protein transacylase |
| [[EMSLR]] | 0.687 | E2F1 mRNA stabilizing lncRNA |
| [[TAMM41]] | 0.687 | TAM41 mitochondrial translocator assembly and maintenance homolog |
| [[MON1A]] | 0.686 | MON1 vesicular trafficking associated A |
| [[HMBS]] | 0.683 | hydroxymethylbilane synthase |
| [[TMEM201]] | 0.682 | transmembrane protein 201 |
| [[PHB1]] | 0.680 | prohibitin 1 |
| [[NSUN2]] | 0.675 | NOP2/Sun RNA methyltransferase 2 |
| [[RRP7BP]] | 0.674 | ribosomal RNA processing 7 homolog B, pseudogene |
| [[AHCTF1]] | 0.674 | AT-hook containing transcription factor 1 |
| [[RPP40]] | 0.673 | ribonuclease P/MRP subunit p40 |
| [[CDC123]] | 0.667 | cell division cycle 123 |
| [[TIMM8A]] | 0.666 | translocase of inner mitochondrial membrane 8A |
| [[EIF3B]] | 0.665 | eukaryotic translation initiation factor 3 subunit B |
| [[RMND1]] | 0.664 | required for meiotic nuclear division 1 homolog |
| [[EIF3M]] | 0.661 | eukaryotic translation initiation factor 3 subunit M |
| [[TMCO6]] | 0.655 | transmembrane and coiled-coil domains 6 |
| [[SNHG15]] | 0.654 | small nucleolar RNA host gene 15 |
| [[STARD7]] | 0.654 | StAR related lipid transfer domain containing 7 |
| [[SCAP]] | 0.651 | SREBF chaperone |
| [[PIGU]] | 0.651 | phosphatidylinositol glycan anchor biosynthesis class U |
| [[C19orf48]] | 0.647 | chromosome 19 open reading frame 48, pseudogene |
| [[UBE3D]] | 0.647 | ubiquitin protein ligase E3D |
| [[PTGES2]] | 0.643 | prostaglandin E synthase 2 |
| [[EARS2]] | 0.641 | glutamyl-tRNA synthetase 2, mitochondrial |
| [[C20orf27]] | 0.638 | adipose secreted signaling protein |
| [[CHST10]] | 0.638 | carbohydrate sulfotransferase 10 |
| [[KAT14]] | 0.637 | lysine acetyltransferase 14 |
| [[ALG3]] | 0.634 | ALG3 alpha-1,3- mannosyltransferase |
| [[NAA20]] | 0.621 | N-alpha-acetyltransferase 20, NatB catalytic subunit |
| [[TRIM27]] | 0.619 | tripartite motif containing 27 |
| [[TIMM23]] | 0.617 | translocase of inner mitochondrial membrane 23 |
| [[SLC46A1]] | 0.611 | solute carrier family 46 member 1 |
| [[MCOLN2]] | 0.609 | mucolipin TRP cation channel 2 |
| [[DCAF13]] | 0.602 | DDB1 and CUL4 associated factor 13 |
| [[NOB1]] | 0.599 | NIN1 (RPN12) binding protein 1 homolog |
| [[FAM222A-AS1]] | 0.594 | FAM222A antisense RNA 1 |
| [[AKAP1]] | 0.592 | A-kinase anchoring protein 1 |
| [[GNL3]] | 0.576 | G protein nucleolar 3 |
| [[ZNF232]] | 0.575 | zinc finger protein 232 |
| [[RABEPK]] | 0.569 | Rab9 effector protein with kelch motifs |
| [[PEX7]] | 0.567 | peroxisomal biogenesis factor 7 |
| [[MRPS2]] | 0.554 | mitochondrial ribosomal protein S2 |
| [[ZNF639]] | 0.553 | zinc finger protein 639 |
| [[XPO6]] | 0.553 | exportin 6 |
| [[CISD3]] | 0.550 | CDGSH iron sulfur domain 3 |
| [[GRHPR]] | 0.546 | glyoxylate and hydroxypyruvate reductase |
| [[DUXAP9]] | 0.544 | double homeobox A pseudogene 9 |
| [[PDCD2L]] | 0.532 | programmed cell death 2 like |
| [[RBFA]] | 0.530 | ribosome binding factor A |
| [[MRPS28]] | 0.524 | mitochondrial ribosomal protein S28 |
| [[TSNARE1]] | 0.523 | t-SNARE domain containing 1 |
| [[AADAT]] | 0.521 | aminoadipate aminotransferase |
| [[UBL4A]] | 0.518 | ubiquitin like 4A |
| [[LSM12]] | 0.512 | LSM12 homolog |
| [[PTRH2]] | 0.511 | peptidyl-tRNA hydrolase 2 |
| [[MPV17L]] | 0.508 | MPV17 mitochondrial inner membrane protein like |
| [[SCFD2]] | 0.505 | sec1 family domain containing 2 |
| [[RNPS1]] | 0.502 | RNA binding protein with serine rich domain 1 |
| [[FYCO1]] | 0.501 | FYVE and coiled-coil domain autophagy adaptor 1 |
| [[CNNM1]] | 0.501 | cyclin and CBS domain divalent metal cation transport mediator 1 |
| [[GPAM]] | 0.492 | glycerol-3-phosphate acyltransferase, mitochondrial |
| [[LINC01237]] | 0.491 | long independently transcribed non-coding RNA 1237 |
| [[DUXAP8]] | 0.489 | double homeobox A pseudogene 8 |
| [[EIF3CL]] | 0.486 | eukaryotic translation initiation factor 3 subunit C like |
| [[MRPS30]] | 0.485 | mitochondrial ribosomal protein S30 |
| [[SNHG16]] | 0.483 | small nucleolar RNA host gene 16 |
| [[NUP35]] | 0.475 | nucleoporin 35 |
| [[SNRNP70]] | 0.473 | small nuclear ribonucleoprotein U1 subunit 70 |
| [[TIMM50]] | 0.472 | translocase of inner mitochondrial membrane 50 |
| [[UBA2]] | 0.469 | ubiquitin like modifier activating enzyme 2 |
| [[FOXO3B]] | 0.461 | forkhead box O3B |
| [[ZNF286A]] | 0.459 | zinc finger protein 286A |
| [[ZFP69]] | 0.458 | ZFP69 zinc finger protein |
| [[GCN1]] | 0.454 | GCN1 activator of EIF2AK4 |
| [[LINC02985]] | 0.452 | long independently transcribed non-coding RNA 2985 |
| [[BTF3L4]] | 0.437 | basic transcription factor 3 like 4 |
| [[HAUS7]] | 0.428 | HAUS augmin like complex subunit 7 |
| [[COPG2IT1]] | 0.394 | COPG2 imprinted transcript 1 |
| [[ANKRD28]] | 0.368 | ankyrin repeat domain 28 |
| [[ZNF587B]] | 0.359 | zinc finger protein 587B |
| [[JPH1]] | 0.330 | junctophilin 1 |
| [[GRSF1]] | 0.327 | G-rich RNA sequence binding factor 1 |
| [[TAF4B]] | 0.287 | TATA-box binding protein associated factor 4b |
| [[NEK6]] | 0.274 | NIMA related kinase 6 |
| [[CCDC124]] | 0.270 | coiled-coil domain containing 124 |
| [[NBEAP2]] | 0.231 | neurobeachin pseudogene 2 |
| [[TMSB15B]] | 0.227 | thymosin beta 15B |
| [[SRSF2]] | 0.210 | serine and arginine rich splicing factor 2 |

## − arm (10)

| Gene | Projection | Name |
|---|---|---|
| [[RO60]] | -0.602 | Ro60, Y RNA binding protein |
| [[MYL6]] | -0.554 | myosin light chain 6 |
| [[MICALL2]] | -0.519 | MICAL like 2 |
| [[RNF19A]] | -0.471 | ring finger protein 19A, RBR E3 ubiquitin protein ligase |
| [[PPP1R11]] | -0.450 | protein phosphatase 1 regulatory inhibitor subunit 11 |
| [[FKBP3]] | -0.435 | FKBP prolyl isomerase 3 |
| [[BMAL1]] | -0.428 | basic helix-loop-helix ARNT like 1 |
| [[ETNK1]] | -0.410 | ethanolamine kinase 1 |
| [[RHBDD2]] | -0.390 | rhomboid domain containing 2 |
| [[LRP10]] | -0.374 | LDL receptor related protein 10 |

## Data

- `graph/nodes.parquet` — module == 33; `graph/modules.parquet` — module == 33; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [32] (drug-dose × line)
