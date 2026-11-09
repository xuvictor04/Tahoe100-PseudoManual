---
module: 26
type: "module"
n_genes: 163
n_plus: 149
n_minus: 14
arms_opposite: true
mean_cos_between_arms: -0.40119874477386475
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 026

*163 genes (149 in the + arm, 14 in the − arm) · [[Module 026.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40). The + arm rises where the − arm falls. Arm = the side of the module's main direction a gene sits on.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of the + arm minus the − arm (`graph/module_pooled_z.npy`, row 25), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it (+ arm up, − arm down): [[Idarubicin (hydrochloride) (drug)]] 5 µM (+27.4, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 5 µM (+17.5, ⚠ cell-cycle shift); [[Auranofin (drug)]] 5 µM (+14.8); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (+12.1, ⚠ cell-cycle shift); [[Epirubicin (hydrochloride) (drug)]] 5 µM (+11.1, ⚠ cell-cycle shift); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+10.0); [[Homoharringtonine (drug)]] 0.5 µM (+8.7, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+7.2, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (+6.3, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (+4.8, ⚠ toxic; transcription drop; cell-cycle shift); [[Cobimetinib (drug)]] 5 µM (+3.4); [[Binimetinib (drug)]] 5 µM (+2.9); [[Cobimetinib (drug)]] 0.5 µM (+2.7); [[Trametinib (drug)]] 0.5 µM (+2.5); [[Homoharringtonine (drug)]] 0.05 µM (+2.3); [[Binimetinib (drug)]] 0.05 µM (+2.3); [[Filgotinib (drug)]] 5 µM (+2.3); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM (+2.3) (92 in all, 24 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)
- Lower it: [[Panobinostat (drug)]] 0.5 µM (-11.2, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (-10.8, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (-10.1, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (-5.4, ⚠ cell-cycle shift); [[Belinostat (drug)]] 0.5 µM (-4.9, ⚠ cell-cycle shift); [[Topotecan (hydrochloride) (drug)]] 0.5 µM (-4.1, ⚠ cell-cycle shift); [[Brivudine (drug)]] 5 µM (-3.6); [[Topotecan (hydrochloride) (drug)]] 5 µM (-3.1, ⚠ toxic; cell-cycle shift); [[c-Kit-IN-1 (drug)]] 0.05 µM (-2.6, ⚠ unreliable plate only); [[Radotinib (drug)]] 5 µM (-2.5); [[Abemaciclib (drug)]] 0.5 µM (-2.1); [[Dexamethasone (drug)]] 0.5 µM (-2.0); [[Niclosamide (olamine) (drug)]] 0.5 µM (-2.0); [[Dexamethasone (drug)]] 5 µM (-1.8); [[Delamanid (drug)]] 5 µM (-1.8); [[Dimethyl fumarate (drug)]] 5 µM (-1.8); [[Lopinavir (drug)]] 5 µM (-1.7); [[Tirabrutinib (drug)]] 5 µM (-1.7) (73 in all, 10 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[SW480 (line)]], [[NCI-H460 (line)]], [[HOP62 (line)]], [[LoVo (line)]], [[C32 (line)]], [[MIA PaCa-2 (line)]], [[HS-578T (line)]], [[LOX-IMVI (line)]]

## + arm (149)

| Gene | Projection | Name |
|---|---|---|
| [[PSMD7-DT]] | 0.931 | PSMD7 divergent transcript |
| [[CCDC90B-AS1]] | 0.923 | CCDC90B antisense RNA 1 |
| [[NEB]] | 0.909 | nebulin |
| [[ST8SIA5]] | 0.885 | ST8 alpha-N-acetyl-neuraminide alpha-2,8-sialyltransferase 5 |
| [[PKN2-AS1]] | 0.878 | PKN2 antisense RNA 1 |
| [[INTS6-AS1]] | 0.876 | INTS6 antisense RNA 1 |
| [[CPEB2-DT]] | 0.868 | CPEB2 divergent transcript |
| [[MMADHC-DT]] | 0.863 | MMADHC divergent transcript |
| [[DNAH12]] | 0.862 | dynein axonemal heavy chain 12 |
| [[CCDC30]] | 0.856 | coiled-coil domain containing 30 |
| [[CIBAR1-DT]] | 0.854 | CIBAR1 divergent transcript |
| [[LINC01762]] | 0.854 | long independently transcribed non-coding RNA 1762 |
| [[MGAM]] | 0.849 | maltase-glucoamylase |
| [[LINC01208]] | 0.827 | long independently transcribed non-coding RNA 1208 |
| [[SIAH2-AS1]] | 0.826 | SIAH2 and CLRN1 antisense RNA 1 |
| [[H2AZ1-DT]] | 0.820 | H2AZ1 divergent transcript |
| [[DENND6A-AS1]] | 0.814 | DENND6A antisense RNA 1 |
| [[ALG1L9P]] | 0.813 | ALG1 like 9, pseudogene |
| [[LINC02646]] | 0.813 | long independently transcribed non-coding RNA 2646 |
| [[C2orf88]] | 0.810 | A-kinase anchoring protein 19 |
| [[CFAP418-AS1]] | 0.808 | CFAP418 antisense RNA 1 |
| [[HSD17B3]] | 0.807 | hydroxysteroid 17-beta dehydrogenase 3 |
| [[NQO1-DT]] | 0.806 | NQO1 divergent transcript |
| [[HCG17]] | 0.800 | — |
| [[LIX1-AS1]] | 0.800 | LIX1 and RIOK2 antisense RNA 1 |
| [[SOX2-OT]] | 0.796 | SOX2 overlapping transcript |
| [[DRAIC]] | 0.795 | downregulated RNA in cancer, inhibitor of cell invasion and migration |
| [[SAXO1]] | 0.790 | stabilizer of axonemal microtubules 1 |
| [[CHODL]] | 0.786 | chondrolectin |
| [[NEK11]] | 0.784 | NIMA related kinase 11 |
| [[LINC00571]] | 0.784 | long independently transcribed non-coding RNA 571 |
| [[EFCAB5]] | 0.784 | EF-hand calcium binding domain 5 |
| [[LRP2BP]] | 0.784 | LRP2 binding protein |
| [[LINC01618]] | 0.781 | long independently transcribed non-coding RNA 1618 |
| [[MAMDC2-AS1]] | 0.779 | MAMDC2 antisense RNA 1 |
| [[SLC26A7]] | 0.779 | solute carrier family 26 member 7 |
| [[FAM184B]] | 0.777 | family with sequence similarity 184 member B |
| [[AEBP2]] | 0.775 | AE binding protein 2 |
| [[LINC01135]] | 0.774 | JUN divergent transcript |
| [[LINC01340]] | 0.773 | long independently transcribed non-coding RNA 1340 |
| [[PELO-AS1]] | 0.766 | PELO antisense RNA 1 |
| [[FBXL19-AS1]] | 0.766 | FBXL19 antisense RNA 1 |
| [[PTOV1-AS1]] | 0.766 | PTOV1 antisense RNA 1 |
| [[UNC79]] | 0.761 | unc-79 subunit of NALCN channel complex |
| [[ALOX12-AS1]] | 0.757 | mir-497-195 cluster host gene |
| [[PDC-AS1]] | 0.754 | PDC antisense RNA 1 |
| [[CELF6]] | 0.752 | CUGBP Elav-like family member 6 |
| [[ESR2]] | 0.752 | estrogen receptor 2 |
| [[STX17-DT]] | 0.752 | non-protein coding RNA, associated with MAP kinase pathway and growth arrest |
| [[CXCL13]] | 0.751 | C-X-C motif chemokine ligand 13 |
| [[CFAP54]] | 0.744 | cilia and flagella associated protein 54 |
| [[LINC02889]] | 0.734 | long independently transcribed non-coding RNA 2889 |
| [[CATSPERE]] | 0.733 | catsper channel auxiliary subunit epsilon |
| [[LINC02398]] | 0.732 | long independently transcribed non-coding RNA 2398 |
| [[LHFPL3]] | 0.728 | LHFPL tetraspan subfamily member 3 |
| [[PIPOX]] | 0.722 | pipecolic acid and sarcosine oxidase |
| [[UBA6-DT]] | 0.722 | UBA6 divergent transcript |
| [[LINC02641]] | 0.720 | long independently transcribed non-coding RNA 2641 |
| [[ARHGAP15]] | 0.719 | Rho GTPase activating protein 15 |
| [[LINC02763]] | 0.719 | long independently transcribed non-coding RNA 2763 |
| [[ACYP2]] | 0.718 | acylphosphatase 2 |
| [[GUCY1A2]] | 0.718 | guanylate cyclase 1 soluble subunit alpha 2 |
| [[SATB1-AS1]] | 0.713 | SATB1 antisense RNA 1 |
| [[PITX1-AS1]] | 0.710 | PITX1 antisense RNA 1 |
| [[HDAC2-AS2]] | 0.710 | HDAC2 and HS3ST5 antisense RNA 2 |
| [[CCNT2-AS1]] | 0.709 | CCNT2 antisense RNA 1 |
| [[ESRRB]] | 0.707 | estrogen related receptor beta |
| [[THBS4-AS1]] | 0.702 | THBS4 antisense RNA 1 |
| [[LINC02977]] | 0.702 | long independently transcribed non-coding RNA 2977 |
| [[GRK4]] | 0.698 | G protein-coupled receptor kinase 4 |
| [[BAALC-AS1]] | 0.690 | BAALC antisense RNA 1 |
| [[TTC41P]] | 0.688 | tetratricopeptide repeat domain 41, pseudogene |
| [[COLQ]] | 0.688 | collagen like tail subunit of asymmetric acetylcholinesterase |
| [[LNCRNA-IUR]] | 0.685 | lncRNA imatinib upregulated |
| [[STARD4-AS1]] | 0.683 | STARD4 antisense RNA 1 |
| [[IGSF11]] | 0.679 | immunoglobulin superfamily member 11 |
| [[LINC01252]] | 0.677 | long independently transcribed non-coding RNA 1252 |
| [[SGO1-AS1]] | 0.674 | SGO1 antisense RNA 1 |
| [[LINC00907]] | 0.664 | long independently transcribed non-coding RNA 907 |
| [[LINC03048]] | 0.663 | long independently transcribed non-coding RNA 3048 |
| [[TPTE2]] | 0.655 | transmembrane phosphoinositide 3-phosphatase and tensin homolog 2 |
| [[SRGAP3]] | 0.649 | SLIT-ROBO Rho GTPase activating protein 3 |
| [[TM9SF5P]] | 0.649 | transmembrane 9 superfamily member 5, pseudogene |
| [[SLCO1B1]] | 0.647 | solute carrier organic anion transporter family member 1B1 |
| [[DAB1]] | 0.647 | DAB adaptor protein 1 |
| [[TMEM72-AS1]] | 0.646 | TMEM72 antisense RNA 1 |
| [[SEMA6A-AS1]] | 0.644 | SEMA6A antisense RNA 1 |
| [[ZNF382]] | 0.641 | zinc finger protein 382 |
| [[XNDC1N-ZNF705EP-ALG1L9P]] | 0.641 | XNDC1N-ZNF705EP-ALG1L9P readthrough |
| [[FSIP2-AS1]] | 0.640 | FSIP2 antisense RNA 1 |
| [[DLG2]] | 0.639 | discs large MAGUK scaffold protein 2 |
| [[MAP3K7CL]] | 0.637 | MAP3K7 C-terminal like |
| [[HAS2-AS1]] | 0.636 | HAS2 antisense RNA 1 |
| [[RBM15-AS1]] | 0.635 | RBM15 antisense RNA 1 |
| [[LINC02516]] | 0.630 | long independently transcribed non-coding RNA 2516 |
| [[LINC02762]] | 0.627 | long independently transcribed non-coding RNA 2762 |
| [[SGK2]] | 0.625 | serum/glucocorticoid regulated kinase 2 |
| [[C2]] | 0.621 | complement C2 |
| [[PPP1R15B-AS1]] | 0.620 | PPP1R15B and PIK3C2B antisense RNA 1 |
| [[MKLN1]] | 0.619 | muskelin 1 |
| [[CD27-AS1]] | 0.618 | CD27 antisense RNA 1 |
| [[MGC4859]] | 0.614 | — |
| [[PHF8]] | 0.596 | PHD finger protein 8 |
| [[FTX]] | 0.591 | FTX transcript, XIST regulator |
| [[C17orf67]] | 0.577 | chromosome 17 open reading frame 67 |
| [[LINC01170]] | 0.577 | long independently transcribed non-coding RNA 1170 |
| [[UBE2R2-AS1]] | 0.576 | UBE2R2 antisense RNA 1 |
| [[SNHG31]] | 0.573 | small nucleolar RNA host gene 31 |
| [[LINC01917]] | 0.571 | long independently transcribed non-coding RNA 1917 |
| [[TEX21P]] | 0.570 | testis expressed 21, pseudogene |
| [[RORA-AS1]] | 0.568 | RORA antisense RNA 1 |
| [[EOLA2-DT]] | 0.551 | EOLA2 divergent transcript |
| [[PRR4]] | 0.549 | proline rich 4 |
| [[SNHG14]] | 0.544 | small nucleolar RNA host gene 14 |
| [[ANKRD7]] | 0.541 | ankyrin repeat domain 7 |
| [[FGF12]] | 0.535 | fibroblast growth factor 12 |
| [[GPR137C]] | 0.525 | G protein-coupled receptor 137C |
| [[LYRM1]] | 0.524 | LYR motif containing 1 |
| [[LINC01301]] | 0.524 | long independently transcribed non-coding RNA 1301 |
| [[SARM1]] | 0.517 | sterile alpha and TIR motif containing 1 |
| [[RDH5]] | 0.515 | retinol dehydrogenase 5 |
| [[LRGUK]] | 0.511 | leucine rich repeats and guanylate kinase domain containing |
| [[ZNF474]] | 0.511 | zinc finger protein 474 |
| [[SATB1]] | 0.510 | SATB homeobox 1 |
| [[KIF26B]] | 0.510 | kinesin family member 26B |
| [[RAPGEF4]] | 0.501 | Rap guanine nucleotide exchange factor 4 |
| [[MFSD1]] | 0.499 | major facilitator superfamily domain containing 1 |
| [[LINC01239]] | 0.498 | long independently transcribed non-coding RNA 1239 |
| [[LINC01505]] | 0.494 | long independently transcribed non-coding RNA 1505 |
| [[PAX8-AS1]] | 0.487 | PAX8 antisense RNA 1 |
| [[RALY-AS1]] | 0.483 | RALY antisense RNA 1 |
| [[LINC02937]] | 0.476 | long independently transcribed non-coding RNA 2937 |
| [[EPHX1]] | 0.474 | epoxide hydrolase 1 |
| [[FBXL13]] | 0.465 | F-box and leucine rich repeat protein 13 |
| [[LINC02018]] | 0.462 | long independently transcribed non-coding RNA 2018 |
| [[GPATCH2]] | 0.461 | G-patch domain containing 2 |
| [[LINC02456]] | 0.459 | long independently transcribed non-coding RNA 2456 |
| [[ADHFE1]] | 0.444 | alcohol dehydrogenase iron containing 1 |
| [[FANK1]] | 0.442 | fibronectin type III and ankyrin repeat domains 1 |
| [[MIR583HG]] | 0.440 | — |
| [[PRH1]] | 0.438 | proline rich protein HaeIII subfamily 1 |
| [[CEP112]] | 0.437 | centrosomal protein 112 |
| [[NFKBID]] | 0.392 | NFKB inhibitor delta |
| [[PMFBP1]] | 0.385 | polyamine modulated factor 1 binding protein 1 |
| [[VIM-AS1]] | 0.379 | VIM antisense RNA 1 |
| [[SLC6A16]] | 0.378 | solute carrier family 6 member 16 |
| [[MOB3B]] | 0.361 | MOB kinase activator 3B |
| [[C1QTNF7-AS1]] | 0.344 | C1QTNF7 antisense RNA 1 |
| [[NAAA]] | 0.327 | N-acylethanolamine acid amidase |

## − arm (14)

| Gene | Projection | Name |
|---|---|---|
| [[BRAT1]] | -0.732 | BRCA1 associated ATM activator 1 |
| [[RSAD1]] | -0.712 | radical S-adenosyl methionine domain containing 1 |
| [[ACTR5]] | -0.706 | actin related protein 5 |
| [[WRAP73]] | -0.698 | WD repeat containing, antisense to TP73 |
| [[GTPBP3]] | -0.679 | GTP binding protein 3, mitochondrial |
| [[COPG2]] | -0.665 | coat protein complex I subunit gamma 2 |
| [[ZFAND4]] | -0.623 | zinc finger AN1-type containing 4 |
| [[NAA40]] | -0.621 | N-alpha-acetyltransferase 40, NatD catalytic subunit |
| [[TTLL4]] | -0.617 | tubulin tyrosine ligase like 4 |
| [[DENND6A]] | -0.562 | DENN domain containing 6A |
| [[TXNL4A]] | -0.559 | thioredoxin like 4A |
| [[BTBD3]] | -0.547 | BTB domain containing 3 |
| [[MLX]] | -0.527 | MAX dimerization protein MLX |
| [[KDM1B]] | -0.497 | lysine demethylase 1B |

## Data

- `graph/nodes.parquet` — module == 26; `graph/modules.parquet` — module == 26; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [25] (drug-dose × line)
