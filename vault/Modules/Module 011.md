---
module: 11
type: "module"
n_genes: 217
n_plus: 183
n_minus: 34
arms_opposite: true
mean_cos_between_arms: -0.32037344574928284
label: "Mitochondrial translation elongation"
label_source: "reactome"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 011

*Mitochondrial translation elongation · 217 genes (183 in the + arm, 34 in the − arm) · [[Module 011.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32). The + arm rises where the − arm falls. Arm = the side of the module's main direction a gene sits on.

Label from the validation stage: **Mitochondrial translation elongation** (reactome, q 0.033; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| + | Mitochondrial translation elongation | reactome | 7/183 | 6.63 | 0.033 |
| + | Mitochondrial translation initiation | reactome | 7/183 | 6.63 | 0.033 |
| + | Mitochondrial translation termination | reactome | 7/183 | 6.55 | 0.035 |
| + | Mitochondrial ribosome-associated quality control | reactome | 7/183 | 6.48 | 0.038 |

## Drugs that move it

*Mean pooled z of the + arm minus the − arm (`graph/module_pooled_z.npy`, row 10), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it (+ arm up, − arm down): [[Homoharringtonine (drug)]] 5 µM (+22.0, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (+18.5, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (+15.6, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (+13.0, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.05 µM (+9.0); [[Topotecan (hydrochloride) (drug)]] 5 µM (+5.6, ⚠ toxic; cell-cycle shift); [[Harringtonine (drug)]] 0.05 µM (+4.6); [[Topotecan (hydrochloride) (drug)]] 0.5 µM (+3.3, ⚠ cell-cycle shift); [[5-Azacytidine (drug)]] 5 µM (+2.7); [[TAK-901 (drug)]] 5 µM (+2.6, ⚠ cell-cycle shift); [[Belumosudil (drug)]] 5 µM (+2.2); [[Clobetasol propionate (drug)]] 0.05 µM (+2.2); [[Clobetasol propionate (drug)]] 0.5 µM (+1.9); [[TAK-733 (drug)]] 5 µM (+1.9); [[Amsacrine (drug)]] 5 µM (+1.8); [[Belzutifan (drug)]] 5 µM (+1.7); [[Betamethasone dipropionate (drug)]] 0.5 µM (+1.6) (63 in all, 14 with an alert ⚠; shown: the 10 strongest and the 7 next strongest without an alert)
- Lower it: [[Dinaciclib (drug)]] 0.5 µM (-10.5, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (-9.5, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (-6.5, ⚠ toxic; transcription drop; cell-cycle shift); [[Panobinostat (drug)]] 5 µM (-5.7, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (-5.6, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (-4.6, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (-3.8, ⚠ cell-cycle shift); [[Niclosamide (olamine) (drug)]] 5 µM (-3.6, ⚠ toxic; cell-cycle shift); [[Epirubicin (hydrochloride) (drug)]] 5 µM (-3.3, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (-3.1, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (-3.1); [[Brivudine (drug)]] 5 µM (-2.9); [[HI-TOPK-032 (drug)]] 5 µM (-1.6); [[Irinotecan (hydrochloride) (drug)]] 0.5 µM (-1.5); [[Dimethyl fumarate (drug)]] 5 µM (-1.4); [[Almonertinib (mesylate) (drug)]] 0.5 µM (-1.3); [[Anethole trithione (drug)]] 0.5 µM (-1.3); [[Piroxicam (drug)]] 0.05 µM (-1.2); [[Ipatasertib (drug)]] 5 µM (-1.2); [[Erlotinib (drug)]] 0.05 µM (-1.2) (43 in all, 21 with an alert ⚠; shown: the 10 strongest and the 10 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[PANC-1 (line)]], [[A-427 (line)]], [[NCI-H1573 (line)]], [[A549 (line)]], [[SW480 (line)]], [[LoVo (line)]], [[A-172 (line)]], [[KATO III (line)]]

*⚠ 2 of its 217 genes are in the vector space only through drug-doses that carry an alert (`embed/genes.parquet` evidence_flagged_only): their place here may reflect what those drug-doses did to the cells. They are marked in the tables of this note.*

## + arm (183)

| Gene | Projection | Name | Alert |
|---|---|---|---|
| [[RPP38]] | 0.878 | ribonuclease P/MRP subunit p38 |  |
| [[MRFAP1L1]] | 0.870 | Morf4 family associated protein 1 like 1 |  |
| [[C1orf131]] | 0.863 | 40S small subunit processome assembly factor 1 |  |
| [[RPP25L]] | 0.861 | ribonuclease P/MRP subunit p25 like |  |
| [[ARL14EP]] | 0.860 | ARF like GTPase 14 effector protein |  |
| [[UTP3]] | 0.851 | UTP3 small subunit processome component |  |
| [[ZNF830]] | 0.847 | zinc finger protein 830 |  |
| [[NAIF1]] | 0.847 | nuclear apoptosis inducing factor 1 |  |
| [[EID2]] | 0.844 | EP300 interacting inhibitor of differentiation 2 |  |
| [[ERCC4]] | 0.839 | ERCC excision repair 4, endonuclease catalytic subunit |  |
| [[FAM200A]] | 0.837 | ZBED8 like |  |
| [[METTL18]] | 0.834 | methyltransferase 18, RPL3 N3(tau)-histidine |  |
| [[MED18]] | 0.831 | mediator complex subunit 18 |  |
| [[ABRAXAS2]] | 0.823 | abraxas 2, BRISC complex subunit |  |
| [[NME6]] | 0.821 | NME/NM23 nucleoside diphosphate kinase 6 |  |
| [[NSMCE3]] | 0.818 | NSE3 component of SMC5/6 complex |  |
| [[SURF6]] | 0.813 | surfeit 6 |  |
| [[CCDC137]] | 0.808 | coiled-coil domain containing 137 |  |
| [[CEBPZ]] | 0.807 | CCAAT enhancer binding protein zeta |  |
| [[ZNF75A]] | 0.807 | zinc finger protein 75A |  |
| [[GSPT2]] | 0.802 | G1 to S phase transition 2 |  |
| [[RPL7L1]] | 0.799 | ribosomal protein L7 like 1 |  |
| [[MRPS18B]] | 0.795 | mitochondrial ribosomal protein S18B |  |
| [[NSRP1]] | 0.788 | nuclear speckle splicing regulatory protein 1 |  |
| [[TOPORS]] | 0.782 | TOP1 binding arginine/serine rich protein, E3 ubiquitin ligase |  |
| [[PBDC1]] | 0.770 | polysaccharide biosynthesis domain containing 1 |  |
| [[ZNF181]] | 0.767 | zinc finger protein 181 |  |
| [[MRM2]] | 0.766 | mitochondrial rRNA methyltransferase 2 |  |
| [[ZCCHC3]] | 0.764 | zinc finger CCHC-type containing 3 |  |
| [[C14orf119]] | 0.764 | chromosome 14 open reading frame 119 |  |
| [[MRPL58]] | 0.764 | mitochondrial ribosomal protein L58 |  |
| [[MRPL38]] | 0.762 | mitochondrial ribosomal protein L38 |  |
| [[LLPH]] | 0.761 | LLP homolog, long-term synaptic facilitation factor |  |
| [[HMGXB4]] | 0.760 | HMG-box containing 4 |  |
| [[TBCC]] | 0.758 | tubulin folding cofactor C |  |
| [[CWC22]] | 0.758 | CWC22 spliceosome associated protein |  |
| [[PDRG1]] | 0.756 | p53 and DNA damage regulated 1 |  |
| [[TMEM70]] | 0.756 | transmembrane protein 70 |  |
| [[PPCS]] | 0.753 | phosphopantothenoylcysteine synthetase |  |
| [[THUMPD3]] | 0.749 | THUMP domain 3 tRNA guanosine methyltransferase |  |
| [[ESF1]] | 0.749 | ESF1 nucleolar pre-rRNA processing protein |  |
| [[ZNF585A]] | 0.746 | zinc finger protein 585A |  |
| [[MRPL46]] | 0.743 | mitochondrial ribosomal protein L46 |  |
| [[TRIM47]] | 0.741 | tripartite motif containing 47 |  |
| [[TP53RK]] | 0.735 | TP53 regulating kinase |  |
| [[OBI1]] | 0.734 | ORC ubiquitin ligase 1 |  |
| [[MAD2L1BP]] | 0.734 | MAD2L1 binding protein |  |
| [[NOL8]] | 0.731 | nucleolar protein 8 |  |
| [[CMTR2]] | 0.730 | cap methyltransferase 2 |  |
| [[RDH14]] | 0.729 | retinol dehydrogenase 14 |  |
| [[ZNF146]] | 0.729 | zinc finger protein 146 |  |
| [[UTP23]] | 0.726 | UTP23 small subunit processome component |  |
| [[ZNF689]] | 0.726 | zinc finger protein 689 |  |
| [[POLR3C]] | 0.721 | RNA polymerase III subunit C |  |
| [[ZNF518A]] | 0.710 | zinc finger protein 518A |  |
| [[USP27X]] | 0.706 | ubiquitin specific peptidase 27 X-linked |  |
| [[ZNF525]] | 0.702 | zinc finger protein 525 |  |
| [[LENG1]] | 0.701 | leukocyte receptor cluster member 1 |  |
| [[THAP1]] | 0.699 | THAP domain containing 1 |  |
| [[ZNF197]] | 0.699 | zinc finger protein 197 |  |
| [[DAXX]] | 0.699 | death domain associated protein |  |
| [[AGGF1]] | 0.698 | angiogenic factor with G-patch and FHA domains 1 |  |
| [[SRSF8]] | 0.697 | serine and arginine rich splicing factor 8 |  |
| [[UQCRFS1]] | 0.696 | ubiquinol-cytochrome c reductase, Rieske iron-sulfur polypeptide 1 |  |
| [[RRP8]] | 0.691 | ribosomal RNA processing 8 |  |
| [[ZNF23]] | 0.687 | zinc finger protein 23 |  |
| [[FDX2]] | 0.686 | ferredoxin 2 |  |
| [[INTS14]] | 0.685 | integrator complex subunit 14 |  |
| [[PDCD7]] | 0.685 | programmed cell death 7 |  |
| [[ZNF593]] | 0.682 | zinc finger protein 593 |  |
| [[KIAA1586]] | 0.678 | KIAA1586 |  |
| [[THUMPD1]] | 0.675 | THUMP domain 1 NAT10 acetyltransferase adaptor |  |
| [[CPT2]] | 0.674 | carnitine palmitoyltransferase 2 |  |
| [[ZNF226]] | 0.671 | zinc finger protein 226 |  |
| [[PRPF38B]] | 0.669 | pre-mRNA processing factor 38B |  |
| [[NT5C]] | 0.667 | 5', 3'-nucleotidase, cytosolic |  |
| [[CRCP]] | 0.663 | CGRP receptor component |  |
| [[MAPK1IP1L]] | 0.662 | mitogen-activated protein kinase 1 interacting protein 1 like |  |
| [[REXO4]] | 0.662 | RNA exonuclease 4 |  |
| [[RBAK]] | 0.660 | RB associated KRAB zinc finger |  |
| [[DPH1]] | 0.659 | diphthamide biosynthesis 1 |  |
| [[NFX1]] | 0.651 | nuclear transcription factor, X-box binding 1 |  |
| [[SCAND1]] | 0.645 | SCAN domain containing 1 |  |
| [[ZNF768]] | 0.642 | zinc finger protein 768 |  |
| [[THAP5]] | 0.642 | THAP domain containing 5 |  |
| [[MPLKIP]] | 0.636 | M-phase specific PLK1 interacting protein |  |
| [[MIER3]] | 0.629 | MIER family member 3 |  |
| [[ZNF182]] | 0.629 | zinc finger protein 182 |  |
| [[C15orf40]] | 0.629 | chromosome 15 open reading frame 40 |  |
| [[ZNF773]] | 0.622 | zinc finger protein 773 |  |
| [[FNTA]] | 0.619 | farnesyltransferase, CAAX box, subunit alpha |  |
| [[MARCHF7]] | 0.619 | membrane associated ring-CH-type finger 7 |  |
| [[ZNF397]] | 0.614 | zinc finger protein 397 |  |
| [[GLRX2]] | 0.613 | glutaredoxin 2 |  |
| [[DDX52]] | 0.610 | DExD-box helicase 52 |  |
| [[URGCP]] | 0.610 | upregulator of cell proliferation |  |
| [[RPF1]] | 0.609 | ribosome production factor 1 homolog |  |
| [[ZNF649]] | 0.606 | zinc finger protein 649 |  |
| [[ZNF286B]] | 0.606 | zinc finger protein 286B (pseudogene) |  |
| [[MRFAP1]] | 0.602 | Morf4 family associated protein 1 |  |
| [[HMG20A]] | 0.597 | high mobility group 20A |  |
| [[CIAPIN1]] | 0.596 | cytokine induced apoptosis inhibitor 1 |  |
| [[KIFBP]] | 0.596 | kinesin family binding protein |  |
| [[ABCF1]] | 0.595 | ATP binding cassette subfamily F member 1 |  |
| [[STYXL1]] | 0.590 | serine/threonine/tyrosine interacting like 1 |  |
| [[TAF7]] | 0.578 | TATA-box binding protein associated factor 7 |  |
| [[ZNF669]] | 0.577 | zinc finger protein 669 |  |
| [[ZNF330]] | 0.577 | nucleolar atypical zinc finger |  |
| [[RBM8A]] | 0.576 | RNA binding motif protein 8A |  |
| [[MRPL36]] | 0.575 | mitochondrial ribosomal protein L36 |  |
| [[THAP6]] | 0.575 | THAP domain containing 6 |  |
| [[ZFP30]] | 0.572 | ZFP30 zinc finger protein |  |
| [[ERCC6]] | 0.568 | ERCC excision repair 6, chromatin remodeling factor |  |
| [[GPANK1]] | 0.567 | G-patch domain and ankyrin repeats 1 |  |
| [[MRPS16]] | 0.564 | mitochondrial ribosomal protein S16 |  |
| [[CDKN2AIP]] | 0.561 | CDKN2A interacting protein |  |
| [[GORASP1]] | 0.558 | golgi reassembly stacking protein 1 |  |
| [[ZNF281]] | 0.557 | zinc finger protein 281 |  |
| [[HOXA10-AS]] | 0.555 | HOXA10 antisense RNA |  |
| [[ZNF347]] | 0.549 | zinc finger protein 347 |  |
| [[AASDH]] | 0.549 | aminoadipate-semialdehyde dehydrogenase |  |
| [[CSTF1]] | 0.548 | cleavage stimulation factor subunit 1 |  |
| [[KRI1]] | 0.548 | KRI1 homolog |  |
| [[FHL3]] | 0.545 | four and a half LIM domains 3 |  |
| [[CHTF8]] | 0.543 | chromosome transmission fidelity factor 8 |  |
| [[NECAP2]] | 0.541 | NECAP endocytosis associated 2 |  |
| [[MRPL32]] | 0.541 | mitochondrial ribosomal protein L32 |  |
| [[OXLD1]] | 0.539 | oxidoreductase like domain containing 1 |  |
| [[ZFP90]] | 0.538 | ZFP90 zinc finger protein |  |
| [[ZNF214]] | 0.537 | zinc finger protein 214 |  |
| [[LINS1]] | 0.537 | lines homolog 1 |  |
| [[ETAA1]] | 0.536 | ETAA1 activator of ATR kinase |  |
| [[ZC3H18]] | 0.535 | zinc finger CCCH-type containing 18 |  |
| [[TAF1]] | 0.532 | TATA-box binding protein associated factor 1 |  |
| [[ZNF616]] | 0.531 | zinc finger protein 616 |  |
| [[ZNF888]] | 0.528 | zinc finger protein 888 |  |
| [[MSL3P1]] | 0.523 | MSL complex subunit 3B |  |
| [[MAGEF1]] | 0.521 | MAGE family member F1 |  |
| [[DDX27]] | 0.516 | DEAD-box helicase 27 |  |
| [[SHROOM1]] | 0.515 | shroom family member 1 |  |
| [[FAM174C]] | 0.504 | family with sequence similarity 174 member C | ⚠ only flagged evidence |
| [[DDX24]] | 0.497 | DEAD-box helicase 24 |  |
| [[MTFP1]] | 0.491 | mitochondrial fission process 1 |  |
| [[OR7E38P]] | 0.491 | olfactory receptor family 7 subfamily E member 38 pseudogene |  |
| [[EGLN2]] | 0.490 | egl-9 family hypoxia inducible factor 2 |  |
| [[SPEN]] | 0.487 | spen family transcriptional repressor |  |
| [[KRT10-AS1]] | 0.484 | KRT10 antisense RNA 1 |  |
| [[KMT2B]] | 0.484 | lysine methyltransferase 2B |  |
| [[SMAD1]] | 0.482 | SMAD family member 1 |  |
| [[ZNF699]] | 0.481 | zinc finger protein 699 |  |
| [[DMAC1]] | 0.476 | distal membrane arm assembly component 1 |  |
| [[RNF169]] | 0.475 | ring finger protein 169 |  |
| [[TNK1]] | 0.473 | tyrosine kinase non receptor 1 |  |
| [[AP4E1]] | 0.451 | adaptor related protein complex 4 subunit epsilon 1 |  |
| [[ZNF415]] | 0.446 | zinc finger protein 415 |  |
| [[FZD7]] | 0.445 | frizzled class receptor 7 |  |
| [[PRKAA2]] | 0.443 | protein kinase AMP-activated catalytic subunit alpha 2 |  |
| [[ZNF160]] | 0.431 | zinc finger protein 160 |  |
| [[POC5]] | 0.426 | POC5 centriolar protein |  |
| [[SFSWAP]] | 0.421 | splicing factor SWAP |  |
| [[RALGAPA1]] | 0.418 | Ral GTPase activating protein catalytic subunit alpha 1 |  |
| [[PRPF4]] | 0.416 | pre-mRNA splicing tri-snRNP complex factor PRPF4 |  |
| [[SMNDC1]] | 0.415 | survival motor neuron domain containing 1 |  |
| [[TOGARAM1]] | 0.414 | TOG array regulator of axonemal microtubules 1 |  |
| [[ID3]] | 0.411 | inhibitor of DNA binding 3 |  |
| [[RFFL]] | 0.400 | ring finger and FYVE like domain containing E3 ubiquitin protein ligase |  |
| [[RSPRY1]] | 0.391 | ring finger and SPRY domain containing 1 |  |
| [[PLEKHJ1]] | 0.390 | pleckstrin homology domain containing J1 |  |
| [[CASKIN2]] | 0.389 | CASK interacting protein 2 |  |
| [[ENDOG]] | 0.381 | endonuclease G |  |
| [[LETMD1]] | 0.377 | LETM1 domain containing 1 |  |
| [[CENPB]] | 0.362 | centromere protein B |  |
| [[METAP2]] | 0.357 | methionyl aminopeptidase 2 |  |
| [[SUPT6H]] | 0.317 | SPT6 homolog, histone chaperone and transcription elongation factor |  |
| [[SIRT3]] | 0.315 | sirtuin 3 |  |
| [[CDK11A]] | 0.314 | cyclin dependent kinase 11A |  |
| [[TMEM129]] | 0.314 | transmembrane protein 129, E3 ubiquitin ligase |  |
| [[CHMP1A]] | 0.270 | charged multivesicular body protein 1A |  |
| [[WASHC4]] | 0.259 | WASH complex subunit 4 |  |
| [[INAFM2]] | 0.242 | InaF motif containing 2 |  |
| [[DMTF1]] | 0.219 | cyclin D binding myb like transcription factor 1 |  |
| [[CDK11B]] | 0.203 | cyclin dependent kinase 11B |  |
| [[TRIR]] | 0.156 | telomerase RNA component interacting RNase | ⚠ only flagged evidence |

## − arm (34)

| Gene | Projection | Name | Alert |
|---|---|---|---|
| [[TMED4]] | -0.689 | transmembrane p24 trafficking protein 4 |  |
| [[TECR]] | -0.684 | trans-2,3-enoyl-CoA reductase |  |
| [[NUTF2]] | -0.667 | nuclear transport factor 2 |  |
| [[LAPTM4A]] | -0.650 | lysosomal protein transmembrane 4 alpha |  |
| [[RCN2]] | -0.643 | reticulocalbin 2 |  |
| [[ILRUN]] | -0.642 | inflammation and lipid regulator with UBA-like and NBR1-like domains |  |
| [[CD46]] | -0.635 | CD46 molecule |  |
| [[MGAT4A]] | -0.632 | alpha-1,3-mannosyl-glycoprotein 4-beta-N-acetylglucosaminyltransferase A |  |
| [[TBCD]] | -0.625 | tubulin folding cofactor D |  |
| [[HDAC1]] | -0.625 | histone deacetylase 1 |  |
| [[RTN3]] | -0.612 | reticulon 3 |  |
| [[TWSG1]] | -0.607 | twisted gastrulation BMP signaling modulator 1 |  |
| [[EIF2S3]] | -0.603 | eukaryotic translation initiation factor 2 subunit gamma |  |
| [[C12orf75]] | -0.603 | chromosome 12 open reading frame 75 |  |
| [[CD81]] | -0.601 | CD81 molecule |  |
| [[PLEKHB2]] | -0.583 | pleckstrin homology domain containing B2 |  |
| [[NPTN]] | -0.573 | neuroplastin |  |
| [[TMBIM6]] | -0.566 | transmembrane BAX inhibitor motif containing 6 |  |
| [[SMARCD2]] | -0.556 | SWI/SNF related BAF chromatin remodeling complex subunit D2 |  |
| [[IMPA2]] | -0.556 | inositol monophosphatase 2 |  |
| [[TPGS2]] | -0.555 | tubulin polyglutamylase complex subunit 2 |  |
| [[ADAM10]] | -0.554 | ADAM metallopeptidase domain 10 |  |
| [[APLP2]] | -0.525 | amyloid beta precursor like protein 2 |  |
| [[VAMP1]] | -0.519 | vesicle associated membrane protein 1 |  |
| [[DPYSL2]] | -0.487 | dihydropyrimidinase like 2 |  |
| [[GLUD1]] | -0.468 | glutamate dehydrogenase 1 |  |
| [[VOPP1]] | -0.457 | VOPP1 WW domain binding protein |  |
| [[SBNO1]] | -0.448 | strawberry notch homolog 1 |  |
| [[CLDND1]] | -0.404 | claudin domain containing 1 |  |
| [[SERINC5]] | -0.386 | serine incorporator 5 |  |
| [[LYRM7]] | -0.377 | LYR motif containing 7 |  |
| [[FBXL8]] | -0.345 | F-box and leucine rich repeat protein 8 |  |
| [[HTRA1]] | -0.340 | HtrA serine peptidase 1 |  |
| [[ARHGAP21]] | -0.242 | Rho GTPase activating protein 21 |  |

## Data

- `graph/nodes.parquet` — module == 11; `graph/modules.parquet` — module == 11; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [10] (drug-dose × line)
