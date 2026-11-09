---
module: 15
type: "module"
n_genes: 210
n_plus: 190
n_minus: 20
arms_opposite: true
mean_cos_between_arms: -0.2673689126968384
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 015

*210 genes (190 in the + arm, 20 in the − arm) · [[Module 015.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27). The + arm rises where the − arm falls. Arm = the side of the module's main direction a gene sits on.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of the + arm minus the − arm (`graph/module_pooled_z.npy`, row 14), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it (+ arm up, − arm down): [[Idarubicin (hydrochloride) (drug)]] 5 µM (+16.6, ⚠ cell-cycle shift); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (+7.0, ⚠ cell-cycle shift); [[Epirubicin (hydrochloride) (drug)]] 5 µM (+5.0, ⚠ cell-cycle shift); [[Topotecan (hydrochloride) (drug)]] 5 µM (+4.4, ⚠ toxic; cell-cycle shift); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+3.2); [[Ponatinib (drug)]] 5 µM (+2.7); [[Selinexor (drug)]] 5 µM (+2.4, ⚠ cell-cycle shift); [[Cabozantinib (S-malate) (drug)]] 5 µM (+2.3); [[Triamcinolone (drug)]] 5 µM (+2.2); [[Idarubicin (hydrochloride) (drug)]] 0.5 µM (+2.2, ⚠ cell-cycle shift); [[Neratinib (maleate) (drug)]] 5 µM (+1.9); [[Ponatinib (drug)]] 0.5 µM (+1.6); [[Cabozantinib (S-malate) (drug)]] 0.05 µM (+1.5); [[ULK-101 (drug)]] 0.05 µM (+1.5); [[Verteporfin (drug)]] 5 µM (+1.5); [[Bimiralisib (drug)]] 0.05 µM (+1.4) (42 in all, 13 with an alert ⚠; shown: the 10 strongest and the 6 next strongest without an alert)
- Lower it: [[Panobinostat (drug)]] 5 µM (-15.6, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (-14.7, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 5 µM (-14.3, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (-12.9, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-10.9, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (-9.2); [[Panobinostat (drug)]] 0.05 µM (-8.3, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-6.6, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (-5.1, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 0.5 µM (-4.9, ⚠ cell-cycle shift); [[Brivudine (drug)]] 5 µM (-4.3); [[Ixazomib citrate (drug)]] 0.5 µM (-3.2); [[Retinoic acid (drug)]] 0.05 µM (-1.6); [[PF-06260933 (drug)]] 5 µM (-1.5); [[Hesperidin (drug)]] 0.05 µM (-1.4); [[HI-TOPK-032 (drug)]] 5 µM (-1.3); [[Cyclosporin A (drug)]] 0.05 µM (-1.3); [[Homoharringtonine (drug)]] 0.05 µM (-1.2); [[Relugolix (drug)]] 0.5 µM (-1.2) (53 in all, 27 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[PANC-1 (line)]], [[SW480 (line)]], [[NCI-H460 (line)]], [[LOX-IMVI (line)]], [[A498 (line)]], [[SW1417 (line)]], [[HEC-1-A (line)]], [[A549 (line)]]

## + arm (190)

| Gene | Projection | Name |
|---|---|---|
| [[ZNF460-AS1]] | 0.861 | ZNF460 antisense RNA 1 |
| [[ZNF213-AS1]] | 0.859 | ZNF213 antisense RNA 1 |
| [[SEC24B-AS1]] | 0.855 | SEC24B antisense RNA 1 |
| [[VPS13B-DT]] | 0.826 | VPS13B divergent transcript |
| [[SPESP1]] | 0.814 | sperm equatorial segment protein 1 |
| [[SAP30L-AS1]] | 0.813 | SAP30L and GALNT10 antisense RNA 1 |
| [[GLUD1P3]] | 0.779 | glutamate dehydrogenase 1 pseudogene 3 |
| [[GTF3C2-AS2]] | 0.779 | GTF3C2 antisense RNA 2 |
| [[FKBP14-AS1]] | 0.779 | FKBP14 antisense RNA 1 |
| [[GOT1-DT]] | 0.777 | GOT1 divergent transcript |
| [[BCL2L2-PABPN1]] | 0.754 | BCL2L2-PABPN1 readthrough |
| [[STARD7-AS1]] | 0.750 | STARD7 antisense RNA 1 |
| [[CAPN10-DT]] | 0.743 | CAPN10 divergent transcript |
| [[ANXA2R-OT1]] | 0.736 | ANXA2R overlapping transcript 1 |
| [[WDR20]] | 0.731 | WD repeat domain 20 |
| [[HLA-DMA]] | 0.729 | major histocompatibility complex, class II, DM alpha |
| [[CDNF]] | 0.722 | cerebral dopamine neurotrophic factor |
| [[ZNF596]] | 0.721 | zinc finger protein 596 |
| [[LINC00115]] | 0.720 | long independently transcribed non-coding RNA 115 |
| [[DARS1-AS1]] | 0.717 | DARS1 antisense RNA 1 |
| [[URM1]] | 0.714 | ubiquitin related modifier 1 |
| [[GATD1-DT]] | 0.710 | GATD1 divergent transcript |
| [[POC1B-AS1]] | 0.710 | POC1B antisense RNA 1 |
| [[PHC2-AS1]] | 0.706 | PHC2 antisense RNA 1 |
| [[KLF3-AS1]] | 0.702 | KLF3 antisense RNA 1 |
| [[LAMTOR5-AS1]] | 0.702 | LAMTOR5 and SLC16A4 antisense RNA 1 |
| [[MIR762HG]] | 0.697 | MIR762 host gene |
| [[PPP1R26-AS1]] | 0.696 | PPP1R26 antisense RNA 1 |
| [[CTTN-DT]] | 0.694 | CTTN divergent transcript |
| [[WASH2P-1]] | 0.693 | — |
| [[SLC25A53]] | 0.693 | solute carrier family 25 member 53 |
| [[SLC12A9]] | 0.692 | solute carrier family 12 member 9 |
| [[CATSPER2P1]] | 0.684 | CATSPER2 pseudogene 1 |
| [[DPY19L2P3]] | 0.683 | DPY19L2 pseudogene 3 |
| [[ZNF529-AS1]] | 0.683 | ZNF529 antisense RNA 1 |
| [[C8orf44-SGK3]] | 0.682 | C8orf44-SGK3 readthrough |
| [[SNHG10]] | 0.681 | small nucleolar RNA host gene 10 |
| [[ANKRD42-DT]] | 0.680 | ANKRD42 divergent transcript |
| [[CCNY-AS1]] | 0.680 | CCNY antisense RNA 1 |
| [[NIFK-AS1]] | 0.679 | NIFK antisense RNA 1 |
| [[TMEM11-DT]] | 0.679 | TMEM11 divergent transcript |
| [[TMEM267]] | 0.675 | transmembrane protein 267 |
| [[PGLS-DT]] | 0.674 | PGLS divergent transcript |
| [[GARS1-DT]] | 0.670 | GARS1 divergent transcript |
| [[DICER1-AS1]] | 0.669 | DICER1 antisense RNA 1 |
| [[ING2-DT]] | 0.669 | ING2 divergent transcript |
| [[GPALPP1]] | 0.667 | GPALPP motifs containing 1 |
| [[NUDT16-DT]] | 0.661 | NUDT16 divergent transcript |
| [[C14orf28]] | 0.661 | dopamine receptor interacting protein 1 |
| [[SDHAF4]] | 0.657 | succinate dehydrogenase complex assembly factor 4 |
| [[BORCS7-ASMT]] | 0.655 | BORCS7-ASMT readthrough (NMD candidate) |
| [[SENP8]] | 0.654 | SUMO peptidase family member, NEDD8 specific |
| [[C2orf76]] | 0.650 | chromosome 2 open reading frame 76 |
| [[POLR1HASP]] | 0.650 | POLR1H antisense, pseudogene |
| [[PCF11-AS1]] | 0.649 | PCF11 antisense RNA 1 |
| [[LENG8-AS1]] | 0.648 | LENG8 antisense RNA 1 |
| [[PEX6]] | 0.636 | peroxisomal biogenesis factor 6 |
| [[NIPBL-DT]] | 0.635 | NIPBL divergent transcript |
| [[MLYCD]] | 0.635 | malonyl-CoA decarboxylase |
| [[DYNLT2]] | 0.634 | dynein light chain Tctex-type 2 |
| [[LEMD3]] | 0.634 | LEM domain containing 3 |
| [[UPP2]] | 0.631 | uridine phosphorylase 2 |
| [[MFSD8]] | 0.631 | major facilitator superfamily domain containing 8 |
| [[RNF217-AS1]] | 0.630 | RNF217 antisense RNA 1 |
| [[RABL2A]] | 0.628 | RAB, member of RAS oncogene family like 2A |
| [[PCMTD1-DT]] | 0.624 | PCMTD1 divergent transcript |
| [[DDX59-AS1]] | 0.623 | DDX59 antisense RNA 1 |
| [[TRAPPC13]] | 0.622 | trafficking protein particle complex subunit 13 |
| [[KPNB1-DT]] | 0.622 | KPNB1 divergent transcript |
| [[FAHD2A]] | 0.612 | fumarylacetoacetate hydrolase domain containing 2A |
| [[ZBTB26]] | 0.612 | zinc finger and BTB domain containing 26 |
| [[H3-3A-DT]] | 0.610 | H3-3A divergent transcript |
| [[SMUG1]] | 0.610 | single-strand-selective monofunctional uracil-DNA glycosylase 1 |
| [[PIGZ]] | 0.606 | phosphatidylinositol glycan anchor biosynthesis class Z (Gwada blood group) |
| [[COPZ2]] | 0.603 | coat protein complex I subunit zeta 2 |
| [[PRDM10]] | 0.603 | PR/SET domain 10 |
| [[ZNF394]] | 0.598 | zinc finger protein 394 |
| [[MSL1]] | 0.598 | MSL complex subunit 1 |
| [[TAGAP-AS1]] | 0.596 | TAGAP antisense RNA 1 |
| [[FAM185A]] | 0.594 | family with sequence similarity 185 member A |
| [[DIDO1]] | 0.594 | death inducer-obliterator 1 |
| [[TMEM68]] | 0.593 | transmembrane protein 68 |
| [[EEF1AKMT3]] | 0.593 | EEF1A lysine methyltransferase 3 |
| [[RNF170]] | 0.593 | ring finger protein 170 |
| [[DHX35]] | 0.592 | DEAH-box helicase 35 |
| [[EMC1-AS1]] | 0.591 | EMC1 antisense RNA 1 |
| [[NUDT13]] | 0.590 | nudix hydrolase 13 |
| [[PGS1]] | 0.590 | phosphatidylglycerophosphate synthase 1 |
| [[TAF11]] | 0.590 | TATA-box binding protein associated factor 11 |
| [[DOCK7-DT]] | 0.588 | DOCK7 divergent transcript |
| [[ORMDL1]] | 0.586 | ORMDL sphingolipid biosynthesis regulator 1 |
| [[TSSK3]] | 0.585 | testis specific serine kinase 3 |
| [[C8orf76]] | 0.585 | chromosome 8 open reading frame 76 |
| [[ZNF514]] | 0.583 | zinc finger protein 514 |
| [[CTC-338M12.4]] | 0.581 | — |
| [[CATSPER2P1-1]] | 0.579 | — |
| [[PTPN9]] | 0.574 | protein tyrosine phosphatase non-receptor type 9 |
| [[PTGR3]] | 0.573 | prostaglandin reductase 3 |
| [[NADSYN1]] | 0.567 | NAD synthetase 1 |
| [[PTS]] | 0.567 | 6-pyruvoyltetrahydropterin synthase |
| [[PPP1CB-DT]] | 0.565 | PPP1CB divergent transcript |
| [[LSM8]] | 0.562 | LSM8 homolog, U6 small nuclear RNA associated |
| [[TMEM187]] | 0.561 | transmembrane protein 187 |
| [[TIGD7]] | 0.559 | tigger transposable element derived 7 |
| [[ZNF418]] | 0.555 | zinc finger protein 418 |
| [[FRG1HP]] | 0.554 | FSHD region gene 1 family member H, pseudogene |
| [[KIAA2026]] | 0.551 | bromodomain containing 10 |
| [[LINC01772]] | 0.551 | long independently transcribed non-coding RNA 1772 |
| [[METTL4]] | 0.550 | methyltransferase 4, N6-adenosine |
| [[ZNF778]] | 0.544 | zinc finger protein 778 |
| [[TIRAP-AS1]] | 0.541 | TIRAP antisense RNA 1 |
| [[KCTD1]] | 0.541 | potassium channel tetramerization domain containing 1 |
| [[LINC02987]] | 0.541 | long independently transcribed non-coding RNA 2987 |
| [[NDUFAF6]] | 0.541 | NADH:ubiquinone oxidoreductase complex assembly factor 6 |
| [[PACRGL]] | 0.539 | parkin coregulated like |
| [[EIF4ENIF1]] | 0.539 | eukaryotic translation initiation factor 4E nuclear import factor 1 |
| [[ERICH2-DT]] | 0.536 | ERICH2 divergent transcript |
| [[SLC16A4-AS1]] | 0.530 | — |
| [[OARD1]] | 0.530 | O-acyl-ADP-ribose deacylase 1 |
| [[CDK2AP1]] | 0.527 | cyclin dependent kinase 2 associated protein 1 |
| [[TRIM7]] | 0.524 | tripartite motif containing 7 |
| [[ZNF528-AS1]] | 0.522 | ZNF528 antisense RNA 1 |
| [[GABPA]] | 0.520 | GA binding protein transcription factor subunit alpha |
| [[ZUP1]] | 0.516 | zinc finger containing ubiquitin peptidase 1 |
| [[ZNF250]] | 0.515 | zinc finger protein 250 |
| [[PSMG4]] | 0.514 | proteasome assembly chaperone 4 |
| [[ANKRD16]] | 0.511 | ankyrin repeat domain 16 |
| [[RABL2B]] | 0.510 | RAB, member of RAS oncogene family like 2B |
| [[SRR]] | 0.508 | serine racemase |
| [[RCC1]] | 0.507 | regulator of chromosome condensation 1 |
| [[BRPF3-AS1]] | 0.507 | BRPF3 antisense RNA 1 |
| [[VAX2]] | 0.502 | ventral anterior homeobox 2 |
| [[ZNF789]] | 0.501 | zinc finger protein 789 |
| [[NUP133]] | 0.501 | nucleoporin 133 |
| [[ZNF862]] | 0.499 | zinc finger protein 862 |
| [[TSBP1-AS1]] | 0.497 | TSBP1 and BTNL2 antisense RNA 1 |
| [[INHA]] | 0.493 | inhibin subunit alpha |
| [[DENND10]] | 0.493 | DENN domain containing 10 |
| [[SRSF5]] | 0.492 | serine and arginine rich splicing factor 5 |
| [[LTB4R]] | 0.489 | leukotriene B4 receptor |
| [[HGSNAT]] | 0.487 | heparan-alpha-glucosaminide N-acetyltransferase |
| [[MRPL11]] | 0.485 | mitochondrial ribosomal protein L11 |
| [[RAD51-AS1]] | 0.484 | RAD51 antisense RNA 1 |
| [[UNC50]] | 0.484 | unc-50 inner nuclear membrane RNA binding protein |
| [[TMEM186]] | 0.482 | transmembrane protein 186 |
| [[DPY19L3-DT]] | 0.478 | DPY19L3 divergent transcript |
| [[ZFYVE27]] | 0.477 | zinc finger FYVE-type containing 27 |
| [[CBR4]] | 0.477 | carbonyl reductase 4 |
| [[LINC02256]] | 0.476 | long independently transcribed non-coding RNA 2256 |
| [[PINK1-AS]] | 0.475 | PINK1 antisense RNA |
| [[MAP3K14-AS1]] | 0.467 | MAP3K14 antisense RNA 1 |
| [[ANXA4]] | 0.465 | annexin A4 |
| [[LINC01409]] | 0.459 | long independently transcribed non-coding RNA 1409 |
| [[NR2C2]] | 0.455 | nuclear receptor subfamily 2 group C member 2 |
| [[CCZ1P1]] | 0.455 | CCZ1 pseudogene 1 |
| [[ERVK13-1]] | 0.455 | endogenous retrovirus group K13 member 1 |
| [[DHRS4-AS1]] | 0.449 | DHRS4 antisense RNA 1 |
| [[ZBTB34]] | 0.449 | zinc finger and BTB domain containing 34 |
| [[CCT6P3-1]] | 0.449 | — |
| [[SLC35D2]] | 0.446 | solute carrier family 35 member D2 |
| [[SLC28A2-AS1]] | 0.445 | SLC28A2 antisense RNA 1 |
| [[ANKRD10]] | 0.440 | ankyrin repeat domain 10 |
| [[CKMT2-AS1]] | 0.438 | CKMT2 antisense RNA 1 |
| [[HLCS-AS1]] | 0.432 | HLCS antisense RNA 1 |
| [[TMED8]] | 0.430 | transmembrane p24 trafficking protein family member 8 |
| [[ANKUB1]] | 0.429 | ankyrin repeat and ubiquitin domain containing 1 |
| [[ZBTB11]] | 0.426 | zinc finger and BTB domain containing 11 |
| [[SMIM12]] | 0.424 | small integral membrane protein 12 |
| [[CCDC18-AS1]] | 0.421 | CCDC18 antisense RNA 1 |
| [[ZNF117]] | 0.420 | zinc finger protein 117 |
| [[ADAT3]] | 0.419 | adenosine deaminase tRNA specific 3 |
| [[RPS10-NUDT3]] | 0.417 | RPS10-NUDT3 readthrough |
| [[MED28]] | 0.405 | mediator complex subunit 28 |
| [[RNF215]] | 0.388 | ring finger protein 215 |
| [[TCTN3]] | 0.382 | tectonic family member 3 |
| [[SLC38A9]] | 0.381 | solute carrier family 38 member 9 |
| [[KHDC1]] | 0.373 | KH domain containing 1 |
| [[FGD1]] | 0.365 | FYVE, RhoGEF and PH domain containing 1 |
| [[ZNF595]] | 0.363 | zinc finger protein 595 |
| [[MED21]] | 0.354 | mediator complex subunit 21 |
| [[GOLGA8N]] | 0.348 | golgin A8 family member N |
| [[CDH26]] | 0.347 | cadherin 26 |
| [[DGCR2]] | 0.339 | DiGeorge syndrome critical region gene 2 |
| [[CCDC92]] | 0.315 | coiled-coil domain containing 92 |
| [[KAZALD1]] | 0.314 | Kazal type serine peptidase inhibitor domain 1 |
| [[ANKRD46]] | 0.313 | ankyrin repeat domain 46 |
| [[MORN1]] | 0.312 | MORN repeat containing 1 |
| [[INTS8]] | 0.288 | integrator complex subunit 8 |
| [[PPIL6]] | 0.243 | peptidylprolyl isomerase like 6 |
| [[ASCC1]] | 0.209 | activating signal cointegrator 1 complex subunit 1 |

## − arm (20)

| Gene | Projection | Name |
|---|---|---|
| [[ALAS1]] | -0.623 | 5'-aminolevulinate synthase 1 |
| [[LMCD1]] | -0.620 | LIM and cysteine rich domains 1 |
| [[DHRS2]] | -0.597 | dehydrogenase/reductase 2 |
| [[POLR2E]] | -0.561 | RNA polymerase II, I and III subunit E |
| [[DPF1]] | -0.539 | double PHD fingers 1 |
| [[ABCD3]] | -0.538 | ATP binding cassette subfamily D member 3 |
| [[GDF11]] | -0.532 | growth differentiation factor 11 |
| [[TPPP]] | -0.516 | tubulin polymerization promoting protein |
| [[ULBP3]] | -0.493 | UL16 binding protein 3 |
| [[NEK1]] | -0.491 | NIMA related kinase 1 |
| [[PPL]] | -0.480 | periplakin |
| [[EPPK1]] | -0.474 | epiplakin 1 |
| [[C1orf226]] | -0.458 | chromosome 1 open reading frame 226 |
| [[MOCS1]] | -0.436 | molybdenum cofactor synthesis 1 |
| [[ZDHHC11B]] | -0.435 | zDHHC palmitoyltransferase 11B (putative) |
| [[USP9X]] | -0.434 | ubiquitin specific peptidase 9 X-linked |
| [[PRDX2]] | -0.432 | peroxiredoxin 2 |
| [[ATP7A]] | -0.399 | ATPase copper transporting alpha |
| [[TRIM37]] | -0.378 | tripartite motif containing 37 |
| [[CAMK1]] | -0.242 | calcium/calmodulin dependent protein kinase I |

## Data

- `graph/nodes.parquet` — module == 15; `graph/modules.parquet` — module == 15; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [14] (drug-dose × line)
