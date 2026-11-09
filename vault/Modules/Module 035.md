---
module: 35
type: "module"
n_genes: 137
n_plus: 129
n_minus: 8
arms_opposite: true
mean_cos_between_arms: -0.33244097232818604
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 035

*137 genes (129 in the + arm, 8 in the − arm) · [[Module 035.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33). The + arm rises where the − arm falls. Arm = the side of the module's main direction a gene sits on.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of the + arm minus the − arm (`graph/module_pooled_z.npy`, row 34), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it (+ arm up, − arm down): [[Idarubicin (hydrochloride) (drug)]] 5 µM (+20.4, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 5 µM (+14.2, ⚠ cell-cycle shift); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (+6.6, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (+5.8, ⚠ cell-cycle shift); [[Selinexor (drug)]] 5 µM (+5.7, ⚠ cell-cycle shift); [[Epirubicin (hydrochloride) (drug)]] 5 µM (+5.4, ⚠ cell-cycle shift); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+5.2); [[Dinaciclib (drug)]] 0.05 µM (+4.0, ⚠ toxic; transcription drop; cell-cycle shift); [[Auranofin (drug)]] 5 µM (+3.5); [[Harringtonine (drug)]] 5 µM (+3.3, ⚠ cell-cycle shift); [[Cobimetinib (drug)]] 5 µM (+2.7); [[Trametinib (drug)]] 0.5 µM (+2.6); [[Binimetinib (drug)]] 0.05 µM (+2.6); [[Binimetinib (drug)]] 5 µM (+2.5); [[Ipatasertib (drug)]] 0.5 µM (+2.5); [[Verteporfin (drug)]] 5 µM (+2.5); [[Trametinib (drug)]] 0.05 µM (+2.4); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM (+2.4) (77 in all, 23 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)
- Lower it: [[Panobinostat (drug)]] 5 µM (-16.1, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (-16.0, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (-14.8, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (-8.1, ⚠ cell-cycle shift); [[Belinostat (drug)]] 0.5 µM (-6.0, ⚠ cell-cycle shift); [[Brivudine (drug)]] 5 µM (-5.4); [[c-Kit-IN-1 (drug)]] 0.05 µM (-4.5, ⚠ unreliable plate only); [[Digitoxin (drug)]] 0.5 µM (-3.9, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (-3.7); [[Niclosamide (olamine) (drug)]] 5 µM (-2.6, ⚠ toxic; cell-cycle shift); [[Abemaciclib (drug)]] 5 µM (-2.4); [[HI-TOPK-032 (drug)]] 5 µM (-2.3); [[Mebendazole (drug)]] 5 µM (-2.0); [[Radotinib (drug)]] 5 µM (-1.8); [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM (-1.8); [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM (-1.6); [[Ipatasertib (drug)]] 5 µM (-1.5); [[Niclosamide (olamine) (drug)]] 0.5 µM (-1.5) (53 in all, 16 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[NCI-H460 (line)]], [[SW480 (line)]], [[HOP62 (line)]], [[LOX-IMVI (line)]], [[J82 (line)]], [[HS-578T (line)]], [[LoVo (line)]], [[PANC-1 (line)]]

## + arm (129)

| Gene | Projection | Name |
|---|---|---|
| [[PJVK]] | 0.878 | pejvakin |
| [[DDX19A-DT]] | 0.875 | DDX19A divergent transcript |
| [[MALINC1]] | 0.866 | mitosis associated long intergenic non-coding RNA 1 |
| [[PAXBP1-AS1]] | 0.865 | PAXBP1 antisense RNA 1 |
| [[C11orf71]] | 0.857 | chromosome 11 open reading frame 71 |
| [[SPEN-AS1]] | 0.851 | SPEN antisense RNA 1 |
| [[LINC02951]] | 0.844 | long independently transcribed non-coding RNA 2951 |
| [[FAM174B]] | 0.825 | family with sequence similarity 174 member B |
| [[SUMO2P17]] | 0.825 | SUMO2 pseudogene 17 |
| [[PBLD]] | 0.821 | phenazine biosynthesis like protein domain containing |
| [[MED28-DT]] | 0.820 | MED28 divergent transcript |
| [[NUTM2E]] | 0.818 | NUT family member 2E |
| [[RAD9B]] | 0.816 | RAD9 checkpoint clamp component B |
| [[PSMD14-DT]] | 0.815 | PSMD14 divergent transcript |
| [[LINC01090]] | 0.814 | long independently transcribed non-coding RNA 1090 |
| [[PPP1R42]] | 0.814 | protein phosphatase 1 regulatory subunit 42 |
| [[ZC2HC1C]] | 0.813 | zinc finger C2HC-type containing 1C |
| [[LINC00863]] | 0.812 | long independently transcribed non-coding RNA 863 |
| [[CCT6B]] | 0.807 | chaperonin containing TCP1 subunit 6B |
| [[ZCWPW1]] | 0.797 | zinc finger CW-type and PWWP domain containing 1 |
| [[ZFHX2-AS1]] | 0.792 | ZFHX2 antisense RNA 1 |
| [[USP34-DT]] | 0.792 | USP34 divergent transcript |
| [[C2orf49-DT]] | 0.787 | C2orf49 divergent transcript |
| [[LRRC8C-DT]] | 0.786 | LRRC8C divergent transcript |
| [[MYLK4]] | 0.776 | myosin light chain kinase family member 4 |
| [[SRRM2-AS1]] | 0.769 | SRRM2 antisense RNA 1 |
| [[CNPY2-AS1]] | 0.768 | CNPY2 antisense RNA 1 |
| [[LRIG2-DT]] | 0.766 | LRIG2 divergent transcript |
| [[PSMG3-AS1]] | 0.763 | PSMG3 antisense RNA 1 |
| [[GSK3B-DT]] | 0.762 | GSK3B divergent transcript |
| [[PIGP]] | 0.761 | phosphatidylinositol glycan anchor biosynthesis class P |
| [[CCDC73]] | 0.759 | coiled-coil domain containing 73 |
| [[HEATR4]] | 0.753 | HEAT repeat containing 4 |
| [[DLGAP4-AS1]] | 0.752 | DLGAP4 antisense RNA 1 |
| [[UPK2]] | 0.748 | uroplakin 2 |
| [[C1orf54]] | 0.739 | chromosome 1 open reading frame 54 |
| [[APPBP2-DT]] | 0.731 | APPBP2 divergent transcript |
| [[RNPC3-DT]] | 0.730 | RNPC3 divergent transcript |
| [[ATXN7L3-AS1]] | 0.727 | ATXN7L3 antisense RNA 1 |
| [[TFAP2A-AS1]] | 0.724 | TFAP2A antisense RNA 1 |
| [[RELA-DT]] | 0.723 | RELA divergent transcript |
| [[AP4S1]] | 0.717 | adaptor related protein complex 4 subunit sigma 1 |
| [[ZNF236-DT]] | 0.714 | ZNF236 divergent transcript |
| [[SMG1-DT]] | 0.714 | SMG1 divergent transcript |
| [[CREB3L4]] | 0.705 | cAMP responsive element binding protein 3 like 4 |
| [[HSDL2-AS1]] | 0.704 | HSDL2 antisense RNA 1 |
| [[DUSP28]] | 0.700 | dual specificity phosphatase 28 |
| [[MKLN1-AS]] | 0.693 | MKLN1 antisense RNA |
| [[GTF2IP5]] | 0.690 | general transcription factor IIi pseudogene 5 |
| [[ADAP2]] | 0.688 | ArfGAP with dual PH domains 2 |
| [[LMNB1-DT]] | 0.678 | LMNB1 divergent transcript |
| [[PLA2G6]] | 0.675 | phospholipase A2 group VI |
| [[EMSY-DT]] | 0.674 | EMSY divergent transcript |
| [[NINJ2]] | 0.671 | ninjurin 2 |
| [[TMLHE-AS1]] | 0.667 | TMLHE antisense RNA 1 |
| [[PTPN23-DT]] | 0.665 | PTPN23 divergent transcript |
| [[NRL]] | 0.663 | neural retina leucine zipper |
| [[MDP1]] | 0.661 | magnesium dependent phosphatase 1 |
| [[GSTZ1]] | 0.661 | glutathione S-transferase zeta 1 |
| [[GPAT4-AS1]] | 0.659 | GPAT4 and GINS4 antisense RNA 1 |
| [[HOXB-AS1]] | 0.654 | HOXB cluster antisense RNA 1 |
| [[NAPA-AS1]] | 0.653 | NAPA antisense RNA 1 |
| [[HCG27]] | 0.652 | HLA complex group 27 |
| [[RUSC1-AS1]] | 0.651 | RUSC1 antisense RNA 1 |
| [[KCTD21-AS1]] | 0.649 | KCTD21 antisense RNA 1 |
| [[CRTC3-AS1]] | 0.648 | CRTC3 antisense RNA 1 |
| [[ATXN1L]] | 0.647 | ataxin 1 like |
| [[ACTR3-AS1]] | 0.644 | ACTR3 antisense RNA 1 |
| [[SETD9]] | 0.641 | SET domain containing 9 |
| [[WDR45]] | 0.637 | WD repeat domain 45 |
| [[C7orf31]] | 0.635 | sperm microtubule inner protein 4 |
| [[DLL1]] | 0.628 | delta like canonical Notch ligand 1 |
| [[CASC11]] | 0.626 | cancer susceptibility 11 |
| [[SMC5-DT]] | 0.625 | — |
| [[RAB21]] | 0.625 | RAB21, member RAS oncogene family |
| [[WNT3]] | 0.625 | Wnt family member 3 |
| [[ZNF561-AS1]] | 0.624 | ZNF561 antisense RNA 1 |
| [[MYL6B-AS1]] | 0.624 | MYL6B antisense RNA 1 |
| [[SOCS3-DT]] | 0.621 | SOCS3 divergent transcript |
| [[TCEAL1]] | 0.620 | transcription elongation factor A like 1 |
| [[LCA5L]] | 0.619 | lebercilin LCA5 like |
| [[TMEM217]] | 0.615 | transmembrane protein 217 |
| [[ZKSCAN7-AS1]] | 0.614 | ZKSCAN7 ZNF cluster antisense RNA 1 |
| [[NPIPB2]] | 0.612 | nuclear pore complex interacting protein family member B2 |
| [[RTCA-AS1]] | 0.612 | RTCA antisense RNA 1 |
| [[PROCA1]] | 0.609 | protein interacting with cyclin A1 |
| [[MYH7B]] | 0.608 | myosin heavy chain 7B |
| [[PPP2R3C]] | 0.606 | protein phosphatase 2 regulatory subunit B''gamma |
| [[GAPLINC]] | 0.605 | gastric adenocarcinoma associated, positive CD44 regulator, long intergenic non-coding RNA |
| [[TGFB3]] | 0.602 | transforming growth factor beta 3 |
| [[ACKR2]] | 0.600 | atypical chemokine receptor 2 |
| [[EPS15-AS1]] | 0.595 | EPS15 antisense RNA 1 |
| [[DENND3-AS1]] | 0.579 | DENND3 antisense RNA 1 |
| [[YTHDF3]] | 0.578 | YTH N6-methyladenosine RNA binding protein F3 |
| [[PHYH]] | 0.577 | phytanoyl-CoA 2-hydroxylase |
| [[CPB2-AS1]] | 0.565 | CPB2 antisense RNA 1 |
| [[TEKTIP1]] | 0.562 | tektin bundle interacting protein 1 |
| [[CES3]] | 0.560 | carboxylesterase 3 |
| [[MAP3K2-DT]] | 0.559 | MAP3K2 divergent transcript |
| [[ACTG1P17]] | 0.554 | actin gamma 1 pseudogene 17 |
| [[UBXN8]] | 0.553 | UBX domain protein 8 |
| [[PRRT1]] | 0.551 | proline rich transmembrane protein 1 |
| [[STXBP2]] | 0.544 | syntaxin binding protein 2 |
| [[DLGAP1-AS2]] | 0.541 | DLGAP1 antisense RNA 2 |
| [[PDCD6IP-DT]] | 0.540 | PDCD6IP divergent transcript |
| [[CA11]] | 0.537 | carbonic anhydrase 11 (inactive) |
| [[HMGA1P4]] | 0.535 | high mobility group AT-hook 1 pseudogene 4 |
| [[PACRG]] | 0.534 | parkin coregulated |
| [[PLUT]] | 0.508 | PDX1 associated lncRNA, upregulator of transcription |
| [[THAP10]] | 0.500 | THAP domain containing 10 |
| [[MUTYH]] | 0.492 | mutY DNA glycosylase |
| [[ATP6V0D1-DT]] | 0.481 | ATP6V0D1 divergent transcript |
| [[PLEKHF2]] | 0.469 | pleckstrin homology and FYVE domain containing 2 |
| [[PRRT2]] | 0.468 | proline rich transmembrane protein 2 |
| [[LIMS2]] | 0.462 | LIM zinc finger domain containing 2 |
| [[TCTA]] | 0.461 | T cell leukemia translocation altered |
| [[HSBP1L1]] | 0.453 | heat shock factor binding protein 1 like 1 |
| [[TMEM30A-DT]] | 0.448 | TMEM30A divergent transcript |
| [[HESX1]] | 0.447 | HESX homeobox 1 |
| [[MTMR9LP]] | 0.445 | myotubularin related protein 9 like, pseudogene |
| [[RPAP3-DT]] | 0.424 | RPAP3 divergent transcript |
| [[BECN1]] | 0.422 | beclin 1 |
| [[ZNF219]] | 0.421 | zinc finger protein 219 |
| [[WDR13]] | 0.408 | WD repeat domain 13 |
| [[LINC01341]] | 0.385 | long independently transcribed non-coding RNA 1341 |
| [[THBS2-AS1]] | 0.374 | THBS2 antisense RNA 1 |
| [[NFATC4]] | 0.365 | nuclear factor of activated T cells 4 |
| [[SOCS5]] | 0.316 | suppressor of cytokine signaling 5 |
| [[ARMH1]] | 0.293 | armadillo like helical domain containing 1 |

## − arm (8)

| Gene | Projection | Name |
|---|---|---|
| [[THEM6]] | -0.588 | thioesterase superfamily member 6 |
| [[AP3M2]] | -0.574 | adaptor related protein complex 3 subunit mu 2 |
| [[PPP1CC]] | -0.554 | protein phosphatase 1 catalytic subunit gamma |
| [[TEX2]] | -0.550 | testis expressed 2 |
| [[LYPLA1]] | -0.504 | lysophospholipase 1 |
| [[MIA3]] | -0.494 | MIA SH3 domain ER export factor 3 |
| [[IMPDH2]] | -0.477 | inosine monophosphate dehydrogenase 2 |
| [[ALDH3A2]] | -0.473 | aldehyde dehydrogenase 3 family member A2 |

## Data

- `graph/nodes.parquet` — module == 35; `graph/modules.parquet` — module == 35; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [34] (drug-dose × line)
