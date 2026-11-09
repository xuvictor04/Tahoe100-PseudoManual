---
module: 2
type: "module"
n_genes: 248
n_plus: 240
n_minus: 8
arms_opposite: true
mean_cos_between_arms: -0.2134229987859726
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 002

*248 genes (240 in the + arm, 8 in the − arm) · [[Module 002.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21). The + arm rises where the − arm falls. Arm = the side of the module's main direction a gene sits on.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of the + arm minus the − arm (`graph/module_pooled_z.npy`, row 1), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it (+ arm up, − arm down): [[Panobinostat (drug)]] 5 µM (+22.5, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (+21.8, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (+16.7, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (+16.1, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (+14.3, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+7.7, ⚠ toxic; transcription drop; cell-cycle shift); [[Docetaxel (drug)]] 0.05 µM (+6.1, ⚠ transcription drop; cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (+5.5, ⚠ cell-cycle shift); [[Belinostat (drug)]] 0.5 µM (+4.7, ⚠ cell-cycle shift); [[Topotecan (hydrochloride) (drug)]] 5 µM (+4.5, ⚠ toxic; cell-cycle shift); [[Ipatasertib (drug)]] 0.5 µM (+4.2); [[Vinblastine (sulfate) (drug)]] 0.5 µM (+3.6); [[vincristine (drug)]] 0.5 µM (+3.6); [[Auranofin (drug)]] 5 µM (+3.6); [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM (+3.5); [[Peretinoin (drug)]] 0.5 µM (+3.3); [[vincristine (drug)]] 5 µM (+3.1); [[Vinblastine (sulfate) (drug)]] 5 µM (+3.1); [[Brivudine (drug)]] 5 µM (+3.1); [[9-ING-41 (drug)]] 0.5 µM (+2.8) (111 in all, 23 with an alert ⚠; shown: the 10 strongest and the 10 next strongest without an alert)
- Lower it: [[Homoharringtonine (drug)]] 5 µM (-13.5, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-12.6, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (-9.0, ⚠ cell-cycle shift); [[TAK-901 (drug)]] 5 µM (-7.9, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-6.8, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 5 µM (-6.3, ⚠ toxic; transcription drop; cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (-5.9, ⚠ cell-cycle shift); [[PH-797804 (drug)]] 5 µM (-5.3); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (-5.3, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 0.5 µM (-5.2, ⚠ cell-cycle shift); [[Verteporfin (drug)]] 5 µM (-3.0); [[Anethole trithione (drug)]] 0.5 µM (-2.9); [[Cobimetinib (drug)]] 5 µM (-2.7); [[Erlotinib (drug)]] 0.05 µM (-2.1); [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM (-2.1); [[TAK-901 (drug)]] 0.05 µM (-2.0); [[Artesunate (drug)]] 0.5 µM (-1.9); [[venetoclax (drug)]] 0.5 µM (-1.8); [[Fenofibrate (drug)]] 0.05 µM (-1.7) (86 in all, 24 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[SW480 (line)]], [[PANC-1 (line)]], [[NCI-H2347 (line)]], [[KATO III (line)]], [[NCI-H460 (line)]], [[HEC-1-A (line)]], [[LOX-IMVI (line)]], [[RKO (line)]]

## + arm (240)

| Gene | Projection | Name |
|---|---|---|
| [[SBF1]] | 0.828 | SET binding factor 1 |
| [[ZDHHC8]] | 0.826 | zDHHC palmitoyltransferase 8 |
| [[KLHL17]] | 0.816 | kelch like family member 17 |
| [[SH3GLB2]] | 0.792 | SH3 domain containing GRB2 like, endophilin B2 |
| [[INTS11]] | 0.789 | integrator complex subunit 11 |
| [[ADCK5]] | 0.785 | aarF domain containing kinase 5 |
| [[TCF3]] | 0.779 | transcription factor 3 |
| [[FBRSL1]] | 0.777 | fibrosin like 1 |
| [[STK25]] | 0.773 | serine/threonine kinase 25 |
| [[ABHD17A]] | 0.768 | abhydrolase domain containing 17A, depalmitoylase |
| [[PPP1R12C]] | 0.765 | protein phosphatase 1 regulatory subunit 12C |
| [[TESK1]] | 0.754 | testis associated actin remodelling kinase 1 |
| [[ZNF598]] | 0.752 | zinc finger protein 598, E3 ubiquitin ligase |
| [[FCHSD1]] | 0.750 | FCH and double SH3 domains 1 |
| [[TNK2]] | 0.746 | tyrosine kinase non receptor 2 |
| [[CPSF1]] | 0.743 | cleavage and polyadenylation specific factor 1 |
| [[NSMF]] | 0.739 | NMDA receptor synaptonuclear signaling and neuronal migration factor |
| [[LLGL1]] | 0.736 | LLGL scribble cell polarity complex component 1 |
| [[UCKL1]] | 0.736 | uridine-cytidine kinase 1 like 1 |
| [[PITPNM1]] | 0.732 | phosphatidylinositol transfer protein membrane associated 1 |
| [[NBEAL2]] | 0.730 | neurobeachin like 2 |
| [[TRABD]] | 0.728 | TraB domain containing |
| [[PLCB3]] | 0.727 | phospholipase C beta 3 |
| [[DVL1]] | 0.725 | dishevelled segment polarity protein 1 |
| [[TUBGCP6]] | 0.721 | tubulin gamma complex component 6 |
| [[CAPN10]] | 0.711 | calpain 10 |
| [[AKT1]] | 0.710 | AKT serine/threonine kinase 1 |
| [[ABCA2]] | 0.705 | ATP binding cassette subfamily A member 2 |
| [[ST6GALNAC6]] | 0.705 | ST6 N-acetylgalactosaminide alpha-2,6-sialyltransferase 6 |
| [[GALNS]] | 0.698 | galactosamine (N-acetyl)-6-sulfatase |
| [[CORO7]] | 0.696 | coronin 7 |
| [[INTS1]] | 0.692 | integrator complex subunit 1 |
| [[GPSM1]] | 0.690 | G protein signaling modulator 1 |
| [[GDI1]] | 0.688 | GDP dissociation inhibitor 1 |
| [[NRBP2]] | 0.684 | nuclear receptor binding protein 2 |
| [[TBC1D24]] | 0.678 | TBC1 domain family member 24 |
| [[MAPK12]] | 0.677 | mitogen-activated protein kinase 12 |
| [[GPAT4]] | 0.677 | glycerol-3-phosphate acyltransferase 4 |
| [[TCIRG1]] | 0.676 | T cell immune regulator 1, ATPase H+ transporting V0 subunit a3 |
| [[CSK]] | 0.673 | C-terminal Src kinase |
| [[LIMK1]] | 0.672 | LIM domain kinase 1 |
| [[DPH7]] | 0.671 | diphthamide biosynthesis 7 |
| [[TPD52L2]] | 0.667 | TPD52 like 2 |
| [[TMEM259]] | 0.667 | transmembrane protein 259 |
| [[PACS2]] | 0.664 | phosphofurin acidic cluster sorting protein 2 |
| [[AP2A2]] | 0.664 | adaptor related protein complex 2 subunit alpha 2 |
| [[DGKZ]] | 0.659 | diacylglycerol kinase zeta |
| [[PLA2G4B]] | 0.659 | phospholipase A2 group IVB |
| [[CDR2L]] | 0.658 | cerebellar degeneration related protein 2 like |
| [[LDLRAP1]] | 0.657 | low density lipoprotein receptor adaptor protein 1 |
| [[POLRMT]] | 0.656 | RNA polymerase mitochondrial |
| [[CRAT]] | 0.654 | carnitine O-acetyltransferase |
| [[TELO2]] | 0.654 | telomere maintenance 2 |
| [[DGKQ]] | 0.653 | diacylglycerol kinase theta |
| [[SLC39A13]] | 0.652 | solute carrier family 39 member 13 |
| [[TPST2]] | 0.650 | tyrosylprotein sulfotransferase 2 |
| [[MICAL1]] | 0.649 | microtubule associated monooxygenase, calponin and LIM domain containing 1 |
| [[RHPN1]] | 0.647 | rhophilin Rho GTPase binding protein 1 |
| [[SIN3B]] | 0.643 | SIN3 transcription regulator family member B |
| [[HECTD3]] | 0.642 | HECT domain E3 ubiquitin protein ligase 3 |
| [[KIFC2]] | 0.641 | kinesin family member C2 |
| [[CEP170B]] | 0.640 | centrosomal protein 170B |
| [[CAPN1]] | 0.638 | calpain 1 |
| [[MAPK11]] | 0.637 | mitogen-activated protein kinase 11 |
| [[NPDC1]] | 0.637 | neural proliferation, differentiation and control 1 |
| [[GIT1]] | 0.635 | GIT ArfGAP 1 |
| [[FGFRL1]] | 0.633 | fibroblast growth factor receptor like 1 |
| [[E2F4]] | 0.632 | E2F transcription factor 4 |
| [[RHOT2]] | 0.632 | ras homolog family member T2 |
| [[EPN1]] | 0.630 | epsin 1 |
| [[STX2]] | 0.627 | syntaxin 2 |
| [[PRKCZ]] | 0.626 | protein kinase C zeta |
| [[TSPAN17]] | 0.626 | tetraspanin 17 |
| [[ATP13A2]] | 0.626 | ATPase cation transporting 13A2 |
| [[AP1M1]] | 0.625 | adaptor related protein complex 1 subunit mu 1 |
| [[TRAF7]] | 0.625 | TNF receptor associated factor 7 |
| [[CAMSAP1]] | 0.624 | calmodulin regulated spectrin associated protein 1 |
| [[CDC42BPB]] | 0.623 | CDC42 binding protein kinase beta |
| [[KIF1C]] | 0.620 | kinesin family member 1C |
| [[CROCCP3]] | 0.616 | CROCC pseudogene 3 |
| [[PPP6R1]] | 0.616 | protein phosphatase 6 regulatory subunit 1 |
| [[MIIP]] | 0.615 | migration and invasion inhibitory protein |
| [[COL18A1]] | 0.614 | collagen type XVIII alpha 1 chain |
| [[SPRYD3]] | 0.612 | SPRY domain containing 3 |
| [[CCDC61]] | 0.612 | coiled-coil domain containing 61 |
| [[ADAMTSL5]] | 0.612 | ADAMTS like 5 |
| [[LYSMD4]] | 0.612 | LysM domain containing 4 |
| [[RTN4R]] | 0.610 | reticulon 4 receptor |
| [[HGS]] | 0.609 | hepatocyte growth factor-regulated tyrosine kinase substrate |
| [[PLXNA3]] | 0.608 | plexin A3 |
| [[TPCN2]] | 0.607 | two pore segment channel 2 |
| [[PGGHG]] | 0.603 | protein-glucosylgalactosylhydroxylysine glucosidase |
| [[DIP2A]] | 0.602 | DIP2 acetate--CoA ligase A |
| [[PLSCR3]] | 0.601 | phospholipid scramblase 3 |
| [[ARHGEF1]] | 0.600 | Rho guanine nucleotide exchange factor 1 |
| [[PPM1F]] | 0.598 | protein phosphatase, Mg2+/Mn2+ dependent 1F |
| [[PPP4C]] | 0.598 | protein phosphatase 4 catalytic subunit |
| [[CXXC1]] | 0.595 | CXXC finger protein 1 |
| [[PGAP6]] | 0.594 | post-GPI attachment to proteins 6 |
| [[ESYT1]] | 0.593 | extended synaptotagmin 1 |
| [[ZMYND19]] | 0.592 | zinc finger MYND-type containing 19 |
| [[GRK6]] | 0.591 | G protein-coupled receptor kinase 6 |
| [[INF2]] | 0.588 | inverted formin 2 |
| [[RNF123]] | 0.586 | ring finger protein 123 |
| [[R3HDM4]] | 0.585 | R3H domain containing 4 |
| [[B4GALT3]] | 0.585 | beta-1,4-galactosyltransferase 3 |
| [[PCBP4]] | 0.584 | poly(rC) binding protein 4 |
| [[LMF2]] | 0.583 | lipase maturation factor 2 |
| [[KIAA0930]] | 0.582 | KIAA0930 |
| [[CACNB1]] | 0.582 | calcium voltage-gated channel auxiliary subunit beta 1 |
| [[ZFYVE21]] | 0.580 | zinc finger FYVE-type containing 21 |
| [[SUN1]] | 0.577 | Sad1 and UNC84 domain containing 1 |
| [[ERCC2]] | 0.576 | ERCC excision repair 2, TFIIH core complex helicase subunit |
| [[RPS6KA4]] | 0.573 | ribosomal protein S6 kinase A4 |
| [[DUS1L]] | 0.568 | dihydrouridine synthase 1 like |
| [[FPGS]] | 0.566 | folylpolyglutamate synthase |
| [[LZTS3]] | 0.563 | leucine zipper tumor suppressor family member 3 |
| [[WDR55]] | 0.562 | WD repeat domain 55 |
| [[PACSIN3]] | 0.561 | protein kinase C and casein kinase substrate in neurons 3 |
| [[HDAC10]] | 0.554 | histone deacetylase 10 |
| [[NCOR2]] | 0.554 | nuclear receptor corepressor 2 |
| [[KCTD21]] | 0.553 | potassium channel tetramerization domain containing 21 |
| [[ULK3]] | 0.552 | unc-51 like kinase 3 |
| [[EML3]] | 0.551 | EMAP like 3 |
| [[FAAP100]] | 0.551 | FA core complex associated protein 100 |
| [[MIER2]] | 0.550 | MIER family member 2 |
| [[HYAL3]] | 0.547 | hyaluronidase 3 |
| [[L1CAM]] | 0.545 | L1 cell adhesion molecule |
| [[ABCC10]] | 0.544 | ATP binding cassette subfamily C member 10 |
| [[PHRF1]] | 0.542 | PHD and ring finger domains 1 |
| [[KLF13]] | 0.540 | KLF transcription factor 13 |
| [[ZFPM1]] | 0.539 | zinc finger protein, FOG family member 1 |
| [[PEX5]] | 0.534 | peroxisomal biogenesis factor 5 |
| [[CTU2]] | 0.534 | cytosolic thiouridylase subunit 2 |
| [[PNPLA6]] | 0.532 | patatin like domain 6, lysophospholipase |
| [[MFSD12]] | 0.531 | major facilitator superfamily domain containing 12 |
| [[SGTA]] | 0.530 | small glutamine rich tetratricopeptide repeat co-chaperone alpha |
| [[ABCD1]] | 0.529 | ATP binding cassette subfamily D member 1 |
| [[GNA11]] | 0.529 | G protein subunit alpha 11 |
| [[SLC17A9]] | 0.527 | solute carrier family 17 member 9 |
| [[UBE2F]] | 0.526 | ubiquitin conjugating enzyme E2 F (putative) |
| [[SKIC2]] | 0.522 | SKI2 subunit of superkiller complex |
| [[CROCCP3-1]] | 0.522 | — |
| [[HEMK1]] | 0.519 | HemK methyltransferase 1, mitochondrial release factors N(5)-glutamine |
| [[CYB5R3]] | 0.517 | cytochrome b5 reductase 3 |
| [[CTNNBIP1]] | 0.517 | catenin beta interacting protein 1 |
| [[CARM1]] | 0.516 | coactivator associated arginine methyltransferase 1 |
| [[TBC1D10B]] | 0.513 | TBC1 domain family member 10B |
| [[APBB3]] | 0.511 | amyloid beta precursor protein binding family B member 3 |
| [[FGFR3]] | 0.508 | fibroblast growth factor receptor 3 |
| [[HMG20B]] | 0.508 | high mobility group 20B |
| [[ZDHHC18]] | 0.508 | zDHHC palmitoyltransferase 18 |
| [[SLC41A3]] | 0.506 | solute carrier family 41 member 3 |
| [[BCL7C]] | 0.504 | BAF chromatin remodeling complex subunit BCL7C |
| [[MLLT1]] | 0.498 | MLLT1 super elongation complex subunit |
| [[AXIN1]] | 0.497 | axin 1 |
| [[SAMD4B]] | 0.495 | sterile alpha motif domain containing 4B |
| [[ZDHHC16]] | 0.495 | zDHHC palmitoyltransferase 16 |
| [[ANKRD52]] | 0.495 | ankyrin repeat domain 52 |
| [[RIC8A]] | 0.493 | RIC8 guanine nucleotide exchange factor A |
| [[CEP295NL]] | 0.492 | CEP295 N-terminal like |
| [[SLC27A4]] | 0.492 | solute carrier family 27 member 4 |
| [[MUS81]] | 0.491 | MUS81 structure-specific endonuclease subunit |
| [[NOTCH1]] | 0.489 | notch receptor 1 |
| [[FHIP2B]] | 0.487 | FHF complex subunit HOOK interacting protein 2B |
| [[DGAT1]] | 0.486 | diacylglycerol O-acyltransferase 1 |
| [[MAN1B1]] | 0.486 | mannosidase alpha class 1B member 1 |
| [[KLC1]] | 0.480 | kinesin light chain 1 |
| [[ARRDC1]] | 0.479 | arrestin domain containing 1 |
| [[SPPL2B]] | 0.478 | signal peptide peptidase like 2B |
| [[MAPK7]] | 0.477 | mitogen-activated protein kinase 7 |
| [[NPIPA1]] | 0.476 | nuclear pore complex interacting protein family member A1 |
| [[CDK10]] | 0.475 | cyclin dependent kinase 10 |
| [[AMDHD2]] | 0.474 | amidohydrolase domain containing 2 |
| [[LZTR1]] | 0.474 | leucine zipper like post translational regulator 1 |
| [[SH3BP2]] | 0.471 | SH3 domain binding protein 2 |
| [[ATXN7L3]] | 0.468 | ataxin 7 like 3 |
| [[ITGB1BP1]] | 0.460 | integrin subunit beta 1 binding protein 1 |
| [[EDC4]] | 0.459 | enhancer of mRNA decapping 4 |
| [[PPP1R26]] | 0.455 | protein phosphatase 1 regulatory subunit 26 |
| [[PHETA1]] | 0.454 | PH domain containing endocytic trafficking adaptor 1 |
| [[SLC25A22]] | 0.454 | solute carrier family 25 member 22 |
| [[ACAD8]] | 0.453 | acyl-CoA dehydrogenase family member 8 |
| [[INPP5E]] | 0.451 | inositol polyphosphate-5-phosphatase E |
| [[KLF16]] | 0.451 | KLF transcription factor 16 |
| [[ARHGEF19]] | 0.450 | Rho guanine nucleotide exchange factor 19 |
| [[MAP2K2]] | 0.449 | mitogen-activated protein kinase kinase 2 |
| [[PIP4K2C]] | 0.448 | phosphatidylinositol-5-phosphate 4-kinase type 2 gamma |
| [[IPO13]] | 0.448 | importin 13 |
| [[TTYH3]] | 0.446 | tweety family member 3 |
| [[CCM2]] | 0.444 | CCM2 scaffold protein |
| [[SHKBP1]] | 0.436 | SH3KBP1 binding protein 1 |
| [[PRR36]] | 0.436 | proline rich 36 |
| [[BCAM]] | 0.434 | basal cell adhesion molecule (Lutheran blood group) |
| [[CPNE2]] | 0.433 | copine 2 |
| [[SLC2A8]] | 0.433 | solute carrier family 2 member 8 |
| [[CACNB3]] | 0.433 | calcium voltage-gated channel auxiliary subunit beta 3 |
| [[LAMA5]] | 0.429 | laminin subunit alpha 5 |
| [[MAP3K6]] | 0.429 | mitogen-activated protein kinase kinase kinase 6 |
| [[DDA1]] | 0.425 | DET1 and DDB1 associated 1 |
| [[ATG9A]] | 0.422 | autophagy related 9A |
| [[TMEM8B]] | 0.420 | transmembrane protein 8B |
| [[QARS1]] | 0.419 | glutaminyl-tRNA synthetase 1 |
| [[FAM3A]] | 0.416 | FAM3 metabolism regulating signaling molecule A |
| [[RGS12]] | 0.415 | regulator of G protein signaling 12 |
| [[RPS6KB2]] | 0.414 | ribosomal protein S6 kinase B2 |
| [[TCFL5]] | 0.413 | transcription factor like 5 |
| [[CSNK2A2]] | 0.412 | casein kinase 2 alpha 2 |
| [[DOP1B]] | 0.410 | DOP1 leucine zipper like protein B |
| [[ACAA1]] | 0.407 | acetyl-CoA acyltransferase 1 |
| [[RUSC1]] | 0.405 | RUN and SH3 domain containing 1 |
| [[CBL]] | 0.402 | Cbl proto-oncogene |
| [[CORO1B]] | 0.394 | coronin 1B |
| [[EEF1A2]] | 0.393 | eukaryotic translation elongation factor 1 alpha 2 |
| [[INTS15]] | 0.389 | integrator complex subunit 15 |
| [[MAFK]] | 0.381 | MAF bZIP transcription factor K |
| [[MKNK1]] | 0.379 | MAPK interacting serine/threonine kinase 1 |
| [[RUBCN]] | 0.376 | rubicon autophagy regulator |
| [[GUCD1]] | 0.369 | guanylyl cyclase domain containing 1 |
| [[CENPT]] | 0.367 | centromere protein T |
| [[CLSTN3]] | 0.366 | calsyntenin 3 |
| [[NEURL4]] | 0.363 | neuralized E3 ubiquitin protein ligase 4 |
| [[KCTD13]] | 0.360 | potassium channel tetramerization domain containing 13 |
| [[IDH3G]] | 0.357 | isocitrate dehydrogenase (NAD(+)) 3 non-catalytic subunit gamma |
| [[TTC7A]] | 0.353 | tetratricopeptide repeat domain 7A |
| [[TP53I13]] | 0.349 | tumor protein p53 inducible protein 13 |
| [[NRSN2]] | 0.345 | neurensin 2 |
| [[ACD]] | 0.344 | ACD shelterin complex subunit and telomerase recruitment factor |
| [[APH1A]] | 0.339 | aph-1A gamma-secretase subunit |
| [[ENGASE]] | 0.336 | endo-beta-N-acetylglucosaminidase |
| [[ZMIZ2]] | 0.336 | zinc finger MIZ-type containing 2 |
| [[TINF2]] | 0.327 | TERF1 interacting nuclear factor 2 |
| [[CLN8]] | 0.324 | CLN8 transmembrane ER and ERGIC protein |
| [[CACFD1]] | 0.317 | calcium channel flower domain containing 1 |
| [[LINC02614]] | 0.316 | long independently transcribed non-coding RNA 2614 |
| [[PIAS3]] | 0.306 | protein inhibitor of activated STAT 3 |
| [[GPR161]] | 0.285 | G protein-coupled receptor 161 |
| [[MIEF2]] | 0.255 | mitochondrial elongation factor 2 |
| [[DENND4B]] | 0.190 | DENN domain containing 4B |
| [[ABAT]] | 0.189 | 4-aminobutyrate aminotransferase |

## − arm (8)

| Gene | Projection | Name |
|---|---|---|
| [[MEIS2]] | -0.498 | Meis homeobox 2 |
| [[PARP8]] | -0.460 | poly(ADP-ribose) polymerase family member 8 |
| [[FNDC3A]] | -0.452 | fibronectin type III domain containing 3A |
| [[RBM7]] | -0.437 | RNA binding motif protein 7 |
| [[CGAS]] | -0.395 | cyclic GMP-AMP synthase |
| [[ARID2]] | -0.380 | AT-rich interaction domain 2 |
| [[MBNL3]] | -0.305 | muscleblind like splicing regulator 3 |
| [[YAF2]] | -0.274 | YY1 associated factor 2 |

## Data

- `graph/nodes.parquet` — module == 2; `graph/modules.parquet` — module == 2; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [1] (drug-dose × line)
