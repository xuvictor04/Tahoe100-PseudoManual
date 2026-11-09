---
module: 32
type: "module"
n_genes: 139
n_plus: 139
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.30516913533210754
label: "interferon alpha response"
label_source: "hallmark"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 032

*interferon alpha response · 139 genes (single-armed) · [[Module 032.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

Label from the validation stage: **interferon alpha response** (hallmark, q 1e-89; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | interferon alpha response | hallmark | 56/139 | 66.0 | 1e-89 |
| + | interferon alpha response | hallmark | 56/139 | 66.0 | 1e-89 |
| + | interferon gamma response | hallmark | 60/139 | 38.5 | 1e-78 |
| all | interferon gamma response | hallmark | 60/139 | 38.5 | 1e-78 |
| all | interferon | control | 23/139 | 99.8 | 7e-42 |
| + | interferon | control | 23/139 | 99.8 | 7e-42 |
| all | Interferon Signaling | reactome | 45/139 | 16.9 | 2e-39 |
| + | Interferon Signaling | reactome | 45/139 | 16.9 | 2e-39 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 31), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Cobimetinib (drug)]] 5 µM (+4.5); [[Harringtonine (drug)]] 0.5 µM (+4.2, ⚠ cell-cycle shift); [[Topotecan (hydrochloride) (drug)]] 0.5 µM (+3.2, ⚠ cell-cycle shift); [[Binimetinib (drug)]] 5 µM (+3.2); [[Cobimetinib (drug)]] 0.5 µM (+3.1); [[Binimetinib (drug)]] 0.5 µM (+3.1); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM (+3.0); [[Trametinib (drug)]] 0.5 µM (+3.0); [[Binimetinib (drug)]] 0.05 µM (+2.8); [[venetoclax (drug)]] 0.05 µM (+2.7); [[Elimusertib hydrochloride (drug)]] 0.05 µM (+2.6); [[Trametinib (drug)]] 0.05 µM (+2.6) (79 in all, 13 with an alert ⚠; shown: the 10 strongest and the 2 next strongest without an alert)
- Lower it: [[Tofacitinib (drug)]] 5 µM (-8.8); [[Panobinostat (drug)]] 5 µM (-8.0, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (-7.8, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (-7.2, ⚠ cell-cycle shift); [[Tofacitinib (citrate) (drug)]] 5 µM (-7.0); [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM (-6.2); [[Tofacitinib (citrate) (drug)]] 0.5 µM (-6.1); [[Tofacitinib (drug)]] 0.5 µM (-5.8); [[Selinexor (drug)]] 5 µM (-4.7, ⚠ cell-cycle shift); [[Niclosamide (olamine) (drug)]] 5 µM (-4.7, ⚠ toxic; cell-cycle shift); [[Auranofin (drug)]] 5 µM (-4.5); [[Vinblastine (sulfate) (drug)]] 5 µM (-4.1); [[Ixazomib (drug)]] 5 µM (-3.2); [[Vinblastine (sulfate) (drug)]] 0.5 µM (-3.1); [[Brivudine (drug)]] 5 µM (-2.7) (88 in all, 29 with an alert ⚠; shown: the 10 strongest and the 5 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[LoVo (line)]], [[A-172 (line)]], [[MIA PaCa-2 (line)]], [[A549 (line)]], [[RPMI-7951 (line)]], [[SNU-423 (line)]], [[COLO 205 (line)]], [[BT-474 (line)]]

## Candidate new members

*Members not annotated to the set their arm is enriched for, ranked by mean cos to the annotated members (`validation/novel_members.csv`); ⚠ = a reason to doubt the gene's place (in the vector space only through flagged drug-doses), kept in its rank. 124 candidates, none with an alert; shown: the 15 strongest.*

| # | Gene | Set | Mean cos |
|---|---|---|---|
| 1 | [[RIGI]] | Viral strategies to evade IFIT action | +0.91 |
| 2 | [[MX1]] | IFIT antiviral response | +0.91 |
| 3 | [[STAT1]] | OAS antiviral response | +0.90 |
| 4 | [[RSAD2]] | IFIT antiviral response | +0.90 |
| 5 | [[CMPK2]] | interferon | +0.89 |
| 6 | [[PARP9]] | interferon | +0.89 |
| 7 | [[IFI44]] | IFIT antiviral response | +0.89 |
| 8 | [[USP18]] | IFIT antiviral response | +0.89 |
| 9 | [[IFIH1]] | IFIT antiviral response | +0.89 |
| 10 | [[OASL]] | IFIT antiviral response | +0.87 |
| 11 | [[MX2]] | IFIT antiviral response | +0.87 |
| 12 | [[OAS2]] | ISG15 antiviral mechanism | +0.87 |
| 13 | [[IFI35]] | interferon | +0.87 |
| 14 | [[OAS1]] | ISG15 antiviral mechanism | +0.86 |
| 15 | [[EIF2AK2]] | IFIT antiviral response | +0.86 |

## + arm (139)

| Gene | Projection | Name |
|---|---|---|
| [[PARP9]] | 0.967 | poly(ADP-ribose) polymerase family member 9 |
| [[OAS2]] | 0.963 | 2'-5'-oligoadenylate synthetase 2 |
| [[IFIT3]] | 0.958 | interferon induced protein with tetratricopeptide repeats 3 |
| [[MX1]] | 0.957 | MX dynamin like GTPase 1 |
| [[OAS1]] | 0.957 | 2'-5'-oligoadenylate synthetase 1 |
| [[IFI35]] | 0.956 | interferon induced protein 35 |
| [[CMPK2]] | 0.953 | cytidine/uridine monophosphate kinase 2 |
| [[RSAD2]] | 0.952 | radical S-adenosyl methionine domain containing 2 |
| [[XAF1]] | 0.951 | XIAP associated factor 1 |
| [[IFI44]] | 0.951 | interferon induced protein 44 |
| [[IFIT1]] | 0.950 | interferon induced protein with tetratricopeptide repeats 1 |
| [[PARP14]] | 0.948 | poly(ADP-ribose) polymerase family member 14 |
| [[OAS3]] | 0.935 | 2'-5'-oligoadenylate synthetase 3 |
| [[USP18]] | 0.934 | ubiquitin specific peptidase 18 |
| [[MX2]] | 0.932 | MX dynamin like GTPase 2 |
| [[SAMD9L]] | 0.928 | sterile alpha motif domain containing 9 like |
| [[SLC15A3]] | 0.927 | solute carrier family 15 member 3 |
| [[IFIH1]] | 0.926 | interferon induced with helicase C domain 1 |
| [[HERC6]] | 0.925 | HECT and RLD domain containing E3 ubiquitin protein ligase family member 6 |
| [[DDX60L]] | 0.921 | DExD/H-box 60 like |
| [[RIGI]] | 0.917 | RNA sensor RIG-I |
| [[EPSTI1]] | 0.917 | epithelial stromal interaction 1 |
| [[EIF2AK2]] | 0.914 | eukaryotic translation initiation factor 2 alpha kinase 2 |
| [[IFI44L]] | 0.909 | interferon induced protein 44 like |
| [[TRIM22]] | 0.906 | tripartite motif containing 22 |
| [[STAT1]] | 0.905 | signal transducer and activator of transcription 1 |
| [[BATF2]] | 0.904 | basic leucine zipper ATF-like transcription factor 2 |
| [[DDX60]] | 0.904 | DExD/H-box helicase 60 |
| [[SP110]] | 0.901 | SP110 nuclear body protein |
| [[OASL]] | 0.898 | 2'-5'-oligoadenylate synthetase like |
| [[SAMD9]] | 0.896 | sterile alpha motif domain containing 9 |
| [[PLSCR1]] | 0.896 | phospholipid scramblase 1 |
| [[PARP10]] | 0.896 | poly(ADP-ribose) polymerase family member 10 |
| [[UBE2L6]] | 0.895 | ubiquitin conjugating enzyme E2 L6 |
| [[IFIT2]] | 0.895 | interferon induced protein with tetratricopeptide repeats 2 |
| [[IFIT5]] | 0.890 | interferon induced protein with tetratricopeptide repeats 5 |
| [[SAMHD1]] | 0.887 | SAM and HD domain containing deoxynucleoside triphosphate triphosphohydrolase 1 |
| [[IFI27]] | 0.884 | interferon alpha inducible protein 27 |
| [[HERC5]] | 0.878 | HECT and RLD domain containing E3 ubiquitin protein ligase 5 |
| [[DTX3L]] | 0.877 | deltex E3 ubiquitin ligase 3L |
| [[ZNFX1]] | 0.876 | zinc finger NFX1-type containing 1 |
| [[ADAR]] | 0.874 | adenosine deaminase RNA specific |
| [[IFI6]] | 0.869 | interferon alpha inducible protein 6 |
| [[TMEM140]] | 0.869 | transmembrane protein 140 |
| [[DHX58]] | 0.868 | DExH-box helicase 58 |
| [[FBXO39]] | 0.866 | F-box protein 39 |
| [[TRIM21]] | 0.866 | tripartite motif containing 21 |
| [[NMI]] | 0.866 | N-myc and STAT interactor |
| [[SP100]] | 0.864 | SP100 nuclear body protein |
| [[IFI16]] | 0.863 | interferon gamma inducible protein 16 |
| [[LAP3]] | 0.862 | leucine aminopeptidase 3 |
| [[ZC3HAV1]] | 0.862 | zinc finger CCCH-type containing, antiviral 1 |
| [[PARP12]] | 0.862 | poly(ADP-ribose) polymerase family member 12 |
| [[NRIR]] | 0.861 | negative regulator of interferon response |
| [[IRF9]] | 0.860 | interferon regulatory factor 9 |
| [[PML]] | 0.855 | PML nuclear body scaffold |
| [[TRIM14]] | 0.853 | tripartite motif containing 14 |
| [[PHF11]] | 0.840 | PHD finger protein 11 |
| [[TDRD7]] | 0.839 | tudor domain containing 7 |
| [[SHFL]] | 0.834 | shiftless antiviral inhibitor of ribosomal frameshifting |
| [[PSMB8]] | 0.828 | proteasome 20S subunit beta 8 |
| [[RNF213]] | 0.822 | ring finger protein 213 |
| [[ETV7]] | 0.815 | ETS variant transcription factor 7 |
| [[IFITM3]] | 0.814 | interferon induced transmembrane protein 3 |
| [[PLEKHA4]] | 0.811 | pleckstrin homology domain containing A4 |
| [[NLRC5]] | 0.809 | NLR family CARD domain containing 5 |
| [[HELZ2]] | 0.803 | helicase with zinc finger 2 |
| [[GBP3]] | 0.791 | guanylate binding protein 3 |
| [[CCDC194]] | 0.790 | coiled-coil domain containing 194 |
| [[BST2]] | 0.788 | bone marrow stromal cell antigen 2 |
| [[IFITM1]] | 0.787 | interferon induced transmembrane protein 1 |
| [[PNPT1]] | 0.785 | polyribonucleotide nucleotidyltransferase 1 |
| [[CMTR1]] | 0.775 | cap methyltransferase 1 |
| [[TAP2]] | 0.765 | transporter 2, ATP binding cassette subfamily B member |
| [[CNP]] | 0.752 | 2',3'-cyclic nucleotide 3' phosphodiesterase |
| [[TRIM25]] | 0.750 | tripartite motif containing 25 |
| [[GBP5]] | 0.747 | guanylate binding protein 5 |
| [[UBA7]] | 0.725 | ubiquitin like modifier activating enzyme 7 |
| [[LGALS9]] | 0.722 | galectin 9 |
| [[LAMP3]] | 0.722 | lysosome associated membrane protein 3 |
| [[STAT2]] | 0.718 | signal transducer and activator of transcription 2 |
| [[TRIM69]] | 0.714 | tripartite motif containing 69 |
| [[SCAMP1-AS1]] | 0.711 | SCAMP1 antisense RNA 1 |
| [[TRIM38]] | 0.708 | tripartite motif containing 38 |
| [[TRIM34]] | 0.705 | tripartite motif containing 34 |
| [[MYD88]] | 0.703 | MYD88 innate immune signal transduction adaptor |
| [[APOBEC3F]] | 0.701 | apolipoprotein B mRNA editing enzyme catalytic subunit 3F |
| [[SHISA5]] | 0.700 | shisa family member 5 |
| [[CXCL10]] | 0.700 | C-X-C motif chemokine ligand 10 |
| [[GCA]] | 0.692 | grancalcin |
| [[APOL2]] | 0.688 | apolipoprotein L2 |
| [[MOV10]] | 0.679 | Mov10 RNA helicase |
| [[PPM1K]] | 0.677 | protein phosphatase, Mg2+/Mn2+ dependent 1K |
| [[SP140L]] | 0.674 | SP140 like nuclear body protein |
| [[LINC01285]] | 0.667 | long independently transcribed non-coding RNA 1285 |
| [[REC8]] | 0.665 | REC8 meiotic recombination protein |
| [[IFITM2]] | 0.665 | interferon induced transmembrane protein 2 |
| [[RBM43]] | 0.658 | RNA binding motif protein 43 |
| [[TRIM56]] | 0.658 | tripartite motif containing 56 |
| [[RASGRP3]] | 0.657 | RAS guanyl releasing protein 3 |
| [[SLC25A28]] | 0.650 | solute carrier family 25 member 28 |
| [[LY6E]] | 0.645 | lymphocyte antigen 6 family member E |
| [[MVB12A]] | 0.635 | multivesicular body subunit 12A |
| [[TYMP]] | 0.634 | thymidine phosphorylase |
| [[N4BP1]] | 0.623 | NEDD4 binding protein 1 |
| [[LY6E-DT]] | 0.616 | LY6E divergent transcript |
| [[CASP8]] | 0.610 | caspase 8 |
| [[SCO2]] | 0.603 | synthesis of cytochrome C oxidase 2 |
| [[LIPA]] | 0.601 | lipase A, lysosomal acid type |
| [[ERAP2]] | 0.599 | endoplasmic reticulum aminopeptidase 2 |
| [[C4orf33]] | 0.598 | chromosome 4 open reading frame 33 |
| [[HDX]] | 0.592 | highly divergent homeobox |
| [[SLFN5]] | 0.588 | schlafen family member 5 |
| [[ANKFY1]] | 0.587 | ankyrin repeat and FYVE domain containing 1 |
| [[BTC]] | 0.585 | betacellulin |
| [[GMPR]] | 0.580 | guanosine monophosphate reductase |
| [[STX17]] | 0.579 | syntaxin 17 |
| [[NAPA]] | 0.577 | NSF attachment protein alpha |
| [[ZCCHC2]] | 0.566 | zinc finger CCHC-type containing 2 |
| [[ATRIP]] | 0.557 | ATR interacting protein |
| [[CASP7]] | 0.556 | caspase 7 |
| [[TRIM26]] | 0.552 | tripartite motif containing 26 |
| [[CHROMR]] | 0.552 | cholesterol induced regulator of metabolism RNA |
| [[CYP2J2]] | 0.521 | cytochrome P450 family 2 subfamily J member 2 |
| [[BTN3A3]] | 0.518 | butyrophilin subfamily 3 member A3 |
| [[UNC93B1]] | 0.515 | unc-93B1 regulator of TLR signaling |
| [[LMO2]] | 0.515 | LIM domain only 2 |
| [[ATP10D]] | 0.502 | ATPase phospholipid transporting 10D (putative) |
| [[TMEM62]] | 0.491 | transmembrane protein 62 |
| [[LINC02904]] | 0.472 | LY6S antisense RNA 1 |
| [[LNPEP]] | 0.461 | leucyl and cystinyl aminopeptidase |
| [[DNPEP]] | 0.458 | aspartyl aminopeptidase |
| [[CASP4]] | 0.446 | caspase 4 |
| [[SPATS2L]] | 0.443 | spermatogenesis associated serine rich 2 like |
| [[APOBEC3G]] | 0.428 | apolipoprotein B mRNA editing enzyme catalytic subunit 3G |
| [[DGLUCY]] | 0.421 | D-glutamate cyclase |
| [[GTPBP1]] | 0.420 | GTP binding protein 1 |
| [[PPP2R5C]] | -0.410 | protein phosphatase 2 regulatory subunit B'gamma |
| [[HSD3B7]] | 0.356 | hydroxy-delta-5-steroid dehydrogenase, 3 beta- and steroid delta-isomerase 7 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 32; `graph/modules.parquet` — module == 32; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [31] (drug-dose × line)
