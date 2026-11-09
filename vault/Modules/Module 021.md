---
module: 21
type: "module"
n_genes: 188
n_plus: 188
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.32740435004234314
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 021

*188 genes (single-armed) · [[Module 021.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 20), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM (+11.0, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (+10.0, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (+9.9, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+7.8, ⚠ toxic; transcription drop; cell-cycle shift); [[Homoharringtonine (drug)]] 5 µM (+3.7, ⚠ cell-cycle shift); [[Topotecan (hydrochloride) (drug)]] 5 µM (+3.7, ⚠ toxic; cell-cycle shift); [[Docetaxel (drug)]] 0.05 µM (+3.7, ⚠ transcription drop; cell-cycle shift); [[Epirubicin (hydrochloride) (drug)]] 5 µM (+3.5, ⚠ cell-cycle shift); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (+3.4, ⚠ cell-cycle shift); [[Auranofin (drug)]] 5 µM (+3.0); [[Tucidinostat (drug)]] 5 µM (+2.4); [[Ipatasertib (drug)]] 0.5 µM (+2.2); [[Docetaxel (Trihydrate) (drug)]] 0.5 µM (+2.1); [[Methylprednisolone succinate (drug)]] 0.5 µM (+2.0); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+1.9); [[Verteporfin (drug)]] 5 µM (+1.8); [[Celecoxib (drug)]] 0.5 µM (+1.7); [[XRK3F2 (drug)]] 0.5 µM (+1.6); [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM (+1.6) (68 in all, 28 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)
- Lower it: [[Adagrasib (drug)]] 0.05 µM (-2.8, ⚠ position not correctable); [[Lucanthone (drug)]] 0.05 µM (-1.8); [[PH-797804 (drug)]] 0.05 µM (-1.7); [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM (-1.6); [[Pyridoxine (hydrochloride) (drug)]] 5 µM (-1.5); [[Rutin (trihydrate) (drug)]] 0.05 µM (-1.5); [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM (-1.4); [[Fenofibrate (drug)]] 0.05 µM (-1.4); [[Balsalazide (sodium hydrate) (drug)]] 5 µM (-1.4); [[Diphenhydramine (drug)]] 0.05 µM (-1.4); [[Benproperine (phosphate) (drug)]] 0.05 µM (-1.3) (27 in all, 2 with an alert ⚠; shown: the 10 strongest and the 1 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[LoVo (line)]], [[HEC-1-A (line)]], [[NCI-H460 (line)]], [[A498 (line)]], [[SW480 (line)]], [[HOP62 (line)]], [[PANC-1 (line)]], [[LOX-IMVI (line)]]

*⚠ 2 of its 188 genes are in the vector space only through drug-doses that carry an alert (`embed/genes.parquet` evidence_flagged_only): their place here may reflect what those drug-doses did to the cells. They are marked in the tables of this note.*

## + arm (188)

| Gene | Projection | Name | Alert |
|---|---|---|---|
| [[CHMP3-AS1]] | 0.937 | CHMP3 and RNF103 antisense RNA 1 |  |
| [[C2CD5-AS1]] | 0.927 | C2CD5 antisense RNA 1 |  |
| [[TICAM2-AS1]] | 0.926 | TICAM2 antisense RNA 1 |  |
| [[ZRANB2-AS1]] | 0.925 | ZRANB2 antisense RNA 1 |  |
| [[HSPA2-AS1]] | 0.904 | HSPA2 and ZBTB1 antisense RNA 1 |  |
| [[FLJ40194]] | 0.895 | — |  |
| [[CTDSPL2-DT]] | 0.894 | CTDSPL2 divergent transcript |  |
| [[A2ML1-AS1]] | 0.891 | A2ML1 antisense RNA 1 |  |
| [[FAM217A]] | 0.889 | family with sequence similarity 217 member A |  |
| [[SPATA21]] | 0.885 | spermatogenesis associated 21 |  |
| [[EOGT-DT]] | 0.884 | EOGT divergent transcript |  |
| [[SLC23A1]] | 0.874 | solute carrier family 23 member 1 |  |
| [[RN7SL1]] | 0.874 | RNA component of signal recognition particle 7SL1 |  |
| [[UBOX5-AS1]] | 0.873 | UBOX5 antisense RNA 1 |  |
| [[PKD2L2]] | 0.872 | polycystin 2 like 2, transient receptor potential cation channel |  |
| [[LRRC37A16P]] | 0.872 | leucine rich repeat containing 37 member A16, pseudogene |  |
| [[HRG-AS1]] | 0.871 | HRG and FETUB antisense RNA 1 |  |
| [[C12orf40]] | 0.870 | regulator of DNA class I crossover intermediates 1 |  |
| [[PP2D1]] | 0.865 | protein phosphatase 2C like domain containing 1 |  |
| [[CNGB3]] | 0.860 | cyclic nucleotide gated channel subunit beta 3 |  |
| [[ZNF451-AS1]] | 0.859 | ZNF451 regulatory antisense RNA 1 |  |
| [[BIRC6-AS2-1]] | 0.858 | — |  |
| [[RN7SL2]] | 0.854 | RNA component of signal recognition particle 7SL2 |  |
| [[SLC3A1]] | 0.847 | solute carrier family 3 member 1 |  |
| [[VPS39-DT]] | 0.847 | VPS39 divergent transcript |  |
| [[LANCL1-AS1]] | 0.842 | LANCL1 antisense RNA 1 |  |
| [[MAL2-AS1]] | 0.840 | MAL2 antisense RNA 1 |  |
| [[OMG]] | 0.835 | oligodendrocyte myelin glycoprotein |  |
| [[EHBP1-AS1]] | 0.829 | EHBP1 antisense RNA 1 |  |
| [[SLC13A4]] | 0.827 | solute carrier family 13 member 4 |  |
| [[ABHD15-AS1]] | 0.824 | ABHD15 antisense RNA 1 |  |
| [[ST7-AS2]] | 0.823 | ST7 antisense RNA 2 |  |
| [[TOMM20L-DT]] | 0.821 | TOMM20L divergent transcript |  |
| [[TTC36-AS1]] | 0.820 | TTC36 and KMT2A antisense RNA 1 |  |
| [[CCDC65]] | 0.813 | dynein regulatory complex subunit 2 |  |
| [[CTBP1-AS]] | 0.813 | CTBP1 antisense RNA | ⚠ only flagged evidence |
| [[SPATA1]] | 0.811 | spermatogenesis associated 1 |  |
| [[GEMIN7-AS1]] | 0.800 | GEMIN7 antisense RNA 1 |  |
| [[C1orf56]] | 0.798 | chromosome 1 open reading frame 56 |  |
| [[DNAJC9-AS1-1]] | 0.792 | DNAJC9 and MRPS16 antisense RNA 1 |  |
| [[SYNM-AS1]] | 0.790 | SYNM antisense RNA 1 |  |
| [[CARNMT1-AS1]] | 0.788 | CARNMT1 antisense RNA 1 |  |
| [[ZBTB20-AS5]] | 0.787 | ZBTB20 antisense RNA 5 |  |
| [[ADNP-AS1]] | 0.783 | ADNP antisense RNA 1 |  |
| [[PRKCA-AS1]] | 0.782 | PRKCA antisense RNA 1 |  |
| [[SLC26A5]] | 0.780 | solute carrier family 26 member 5 |  |
| [[SPATC1]] | 0.774 | spermatogenesis and centriole associated 1 |  |
| [[SPTBN1-AS2]] | 0.771 | SPTBN1 antisense RNA 2 |  |
| [[EFCAB14-AS1]] | 0.770 | EFCAB14 antisense RNA 1 |  |
| [[BTG1-DT]] | 0.769 | BTG1 divergent transcript |  |
| [[EAF1-AS1]] | 0.768 | EAF1 antisense RNA 1 |  |
| [[GCNT7]] | 0.768 | glucosaminyl (N-acetyl) transferase family member 7 |  |
| [[ASB14]] | 0.764 | ankyrin repeat and SOCS box containing 14 |  |
| [[MYH11]] | 0.762 | myosin heavy chain 11 |  |
| [[RHOQ-AS1]] | 0.752 | RHOQ antisense RNA 1 |  |
| [[DSG2-AS1]] | 0.752 | DSG2 antisense RNA 1 |  |
| [[OOEP]] | 0.751 | oocyte expressed protein |  |
| [[TP53TG5]] | 0.751 | TP53 target 5 |  |
| [[CFAP20DC-AS1]] | 0.750 | CFAP20DC antisense RNA 1 |  |
| [[AKAP13-AS1]] | 0.748 | AKAP13 antisense RNA 1 |  |
| [[ENO4]] | 0.743 | enolase 4 |  |
| [[C12orf73]] | 0.743 | ubiquinol-cytochrome c reductase complex assembly factor 6 |  |
| [[SEPTIN1]] | 0.732 | septin 1 |  |
| [[LINC02608]] | 0.730 | long independently transcribed non-coding RNA 2608 |  |
| [[OXR1-AS1]] | 0.729 | OXR1 antisense RNA 1 |  |
| [[ZBTB47-AS1]] | 0.727 | ZBTB47 and NKTR antisense RNA 1 |  |
| [[NFATC2IP-AS1]] | 0.724 | NFATC2IP antisense RNA 1 |  |
| [[SNAP25-AS1]] | 0.722 | SNAP25 antisense RNA 1 |  |
| [[NDUFV2-AS1]] | 0.720 | NDUFV2 antisense RNA 1 |  |
| [[MMP24]] | 0.717 | matrix metallopeptidase 24 |  |
| [[COLEC11]] | 0.716 | collectin subfamily member 11 |  |
| [[ABCC11]] | 0.714 | ATP binding cassette subfamily C member 11 |  |
| [[ELOA-AS1]] | 0.711 | ELOA antisense RNA 1 |  |
| [[MROH8]] | 0.704 | maestro heat like repeat family member 8 |  |
| [[RYR1]] | 0.701 | ryanodine receptor 1 |  |
| [[HOXB-AS3]] | 0.698 | HOXB cluster antisense RNA 3 |  |
| [[SYNC]] | 0.698 | syncoilin, intermediate filament protein |  |
| [[SLC51A]] | 0.698 | solute carrier family 51 member A |  |
| [[PLCG1-AS1]] | 0.698 | PLCG1 antisense RNA 1 |  |
| [[AADACL2-AS1]] | 0.697 | AADACL2 antisense RNA 1 |  |
| [[CCNO-DT]] | 0.696 | CCNO divergent transcript |  |
| [[SPDYE5]] | 0.695 | speedy/RINGO cell cycle regulator family member E5 |  |
| [[KIZ-AS1]] | 0.691 | KIZ antisense RNA 1 | ⚠ only flagged evidence |
| [[CCDC39]] | 0.686 | coiled-coil domain 39 molecular ruler complex subunit |  |
| [[C1QTNF7]] | 0.685 | C1q and TNF related 7 |  |
| [[BTNL12P]] | 0.683 | butyrophilin like 12, pseudogene |  |
| [[CRLF1]] | 0.678 | cytokine receptor like factor 1 |  |
| [[STARD13-AS]] | 0.675 | STARD13 antisense RNA |  |
| [[SPAG5-AS1]] | 0.668 | SPAG5 antisense RNA 1 |  |
| [[TSPOAP1-AS1]] | 0.668 | TSPOAP1, SUPT4H1 and RNF43 antisense RNA 1 |  |
| [[LINC00685]] | 0.666 | long independently transcribed non-coding RNA 685 |  |
| [[TNS2-AS1]] | 0.660 | TNS2 antisense RNA 1 |  |
| [[ETFBKMT]] | 0.660 | electron transfer flavoprotein subunit beta lysine methyltransferase |  |
| [[GCC2-AS1]] | 0.658 | GCC2 antisense RNA 1 |  |
| [[MME-AS1]] | 0.658 | MME antisense RNA 1 |  |
| [[EFCAB13-DT]] | 0.657 | EFCAB13 divergent transcript |  |
| [[LINC02603]] | 0.654 | long independently transcribed non-coding RNA 2603 |  |
| [[CLDN18]] | 0.650 | claudin 18 |  |
| [[CMAHP]] | 0.649 | cytidine monophospho-N-acetylneuraminic acid hydroxylase, pseudogene |  |
| [[PROSER2-AS1]] | 0.648 | PROSER2 antisense RNA 1 |  |
| [[MYLK3]] | 0.641 | myosin light chain kinase 3 |  |
| [[KANSL1]] | 0.639 | KAT8 regulatory NSL complex subunit 1 |  |
| [[SNX32]] | 0.639 | sorting nexin 32 |  |
| [[DNAJC3-DT]] | 0.635 | DNAJC3 divergent transcript |  |
| [[PRSS48]] | 0.632 | serine protease 48 |  |
| [[ACSM3]] | 0.631 | acyl-CoA synthetase medium chain family member 3 |  |
| [[SHOC1]] | 0.630 | shortage in chiasmata 1 |  |
| [[PPM1N]] | 0.629 | protein phosphatase, Mg2+/Mn2+ dependent 1N (putative) |  |
| [[SAMD4A-AS1]] | 0.622 | SAMD4A antisense RNA 1 |  |
| [[VCAN-AS1]] | 0.618 | VCAN antisense RNA 1 |  |
| [[RSL1D1-DT]] | 0.618 | RSL1D1 divergent transcript |  |
| [[LINC01019]] | 0.616 | long independently transcribed non-coding RNA 1019 |  |
| [[BMAL2-AS1]] | 0.614 | BMAL2 antisense RNA 1 |  |
| [[APOE]] | 0.614 | apolipoprotein E |  |
| [[MYL6B]] | 0.604 | myosin light chain 6B |  |
| [[C12orf57]] | 0.601 | chromosome 12 open reading frame 57 |  |
| [[HNRNPD-DT]] | 0.600 | HNRNPD divergent transcript |  |
| [[HNRNPK-AS1]] | 0.598 | HNRNPK antisense RNA 1 |  |
| [[NME9]] | 0.597 | NME/NM23 family member 9 |  |
| [[SEM1]] | 0.597 | SEM1 26S proteasome subunit |  |
| [[GMFG]] | 0.594 | glia maturation factor gamma |  |
| [[CNTD1]] | 0.591 | cyclin N-terminal domain containing 1 |  |
| [[EVI2B]] | 0.590 | ecotropic viral integration site 2B |  |
| [[KIAA2012]] | 0.589 | KIAA2012 |  |
| [[DDN-AS1]] | 0.587 | DDN and PRKAG1 antisense RNA 1 |  |
| [[DEPDC4]] | 0.587 | DEP domain containing 4 |  |
| [[GPR84-AS1]] | 0.586 | GPR84, ZNF385A, ITGA5 and GTSF1 antisense RNA 1 |  |
| [[LRRC75A]] | 0.585 | leucine rich repeat containing 75A |  |
| [[MYO1F]] | 0.581 | myosin IF |  |
| [[RIPOR3]] | 0.579 | RIPOR family member 3 |  |
| [[IGF2BP2-AS1]] | 0.579 | IGF2BP2 antisense RNA 1 |  |
| [[PXN-AS1]] | 0.578 | PXN antisense RNA 1 |  |
| [[C3orf49]] | 0.577 | chromosome 3 open reading frame 49 |  |
| [[EPM2AIP1]] | 0.568 | EPM2A interacting protein 1 |  |
| [[FAM177B]] | 0.567 | family with sequence similarity 177 member B |  |
| [[MLANA]] | 0.566 | melan-A |  |
| [[NPW]] | 0.566 | neuropeptide W |  |
| [[SCAMP5]] | 0.557 | secretory carrier membrane protein 5 |  |
| [[RENO1]] | 0.554 | regulator of early neurogenesis 1 |  |
| [[CCN4]] | 0.553 | cellular communication network factor 4 |  |
| [[MAP3K12]] | 0.553 | mitogen-activated protein kinase kinase kinase 12 |  |
| [[CYP2U1-AS1]] | 0.552 | CYP2U1 and SGMS2 antisense RNA 1 |  |
| [[POMZP3]] | 0.546 | POM121 and ZP3 fusion |  |
| [[FAM151B-DT]] | 0.545 | FAM151B divergent transcript |  |
| [[CHMP1B-AS1]] | 0.540 | CHMP1B antisense RNA 1 |  |
| [[PNCK]] | 0.539 | pregnancy up-regulated nonubiquitous CaM kinase |  |
| [[CFL1P1-1]] | 0.537 | — |  |
| [[ATP6V1C2]] | 0.536 | ATPase H+ transporting V1 subunit C2 |  |
| [[S100A13]] | 0.535 | S100 calcium binding protein A13 |  |
| [[GOLGA8A]] | 0.535 | golgin A8 family member A |  |
| [[OSCAR]] | 0.535 | osteoclast associated Ig-like receptor |  |
| [[MTCP1]] | 0.528 | mature T cell proliferation 1 |  |
| [[RPL41]] | 0.516 | ribosomal protein L41 |  |
| [[APEX2]] | -0.514 | apurinic/apyrimidinic endodeoxyribonuclease 2 |  |
| [[PABPN1]] | 0.513 | poly(A) binding protein nuclear 1 |  |
| [[GOLGA8B]] | 0.512 | golgin A8 family member B |  |
| [[PNISR]] | 0.512 | PNN interacting serine and arginine rich protein |  |
| [[HCG25]] | 0.508 | HLA complex group 25 |  |
| [[TCF25]] | 0.508 | TCF25 ribosome quality control complex subunit |  |
| [[ITGAE]] | 0.501 | integrin subunit alpha E |  |
| [[PYGO2]] | -0.497 | pygopus family PHD finger 2 |  |
| [[TNFSF12]] | 0.493 | TNF superfamily member 12 |  |
| [[AP4M1]] | 0.485 | adaptor related protein complex 4 subunit mu 1 |  |
| [[PRMT5-DT]] | 0.485 | PRMT5 divergent transcript |  |
| [[FBXO2]] | 0.473 | F-box protein 2 |  |
| [[COCH]] | 0.466 | cochlin |  |
| [[OVOL2]] | 0.464 | ovo like zinc finger 2 |  |
| [[NCK1-DT]] | 0.463 | NCK1 divergent transcript |  |
| [[CACNG2]] | 0.457 | calcium voltage-gated channel auxiliary subunit gamma 2 |  |
| [[SPACA6]] | 0.455 | sperm acrosome associated 6 |  |
| [[TMA7]] | 0.451 | translation machinery associated 7 homolog |  |
| [[FAXDC2]] | 0.444 | fatty acid hydroxylase domain containing 2 |  |
| [[BEST1]] | 0.442 | bestrophin 1 |  |
| [[HAPLN3]] | 0.436 | hyaluronan and proteoglycan link protein 3 |  |
| [[ARL17A]] | 0.412 | ARF like GTPase 17A |  |
| [[WASL-DT]] | 0.410 | WASL divergent transcript |  |
| [[CSAD]] | 0.404 | cysteine sulfinic acid decarboxylase |  |
| [[AK7]] | 0.402 | adenylate kinase 7 |  |
| [[KLKP1-1]] | 0.402 | — |  |
| [[GDPD4]] | 0.400 | glycerophosphodiester phosphodiesterase domain containing 4 |  |
| [[ARGLU1]] | 0.389 | arginine and glutamate rich 1 |  |
| [[ZC3H3]] | 0.375 | zinc finger CCCH-type containing 3 |  |
| [[SLC16A13]] | 0.362 | solute carrier family 16 member 13 |  |
| [[TCEA2]] | 0.351 | transcription elongation factor A2 |  |
| [[LUC7L3]] | 0.299 | LUC7 like 3 pre-mRNA splicing factor |  |
| [[CCDC183]] | 0.288 | coiled-coil domain containing 183 |  |
| [[CPM]] | 0.280 | carboxypeptidase M |  |
| [[ARMC7]] | 0.101 | armadillo repeat containing 7 |  |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 21; `graph/modules.parquet` — module == 21; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [20] (drug-dose × line)
