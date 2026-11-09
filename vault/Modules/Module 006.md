---
module: 6
type: "module"
n_genes: 236
n_plus: 231
n_minus: 5
arms_opposite: true
mean_cos_between_arms: -0.3303672969341278
label: "E2F targets"
label_source: "hallmark"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 006

*E2F targets · 236 genes (231 in the + arm, 5 in the − arm) · [[Module 006.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33). The + arm rises where the − arm falls. Arm = the side of the module's main direction a gene sits on.

Label from the validation stage: **E2F targets** (hallmark, q 8e-66; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| + | Cell Cycle | reactome | 99/231 | 10.6 | 1e-72 |
| all | Cell Cycle | reactome | 99/236 | 10.4 | 2e-71 |
| + | E2F targets | hallmark | 65/231 | 21.2 | 8e-66 |
| all | E2F targets | hallmark | 65/236 | 20.8 | 4e-65 |
| + | Cell Cycle, Mitotic | reactome | 81/231 | 11.0 | 1e-58 |
| all | Cell Cycle, Mitotic | reactome | 81/236 | 10.8 | 7e-58 |
| + | DNA strand elongation | reactome | 28/231 | 57.1 | 1e-43 |
| all | DNA strand elongation | reactome | 28/236 | 55.9 | 2e-43 |

## Drugs that move it

*Mean pooled z of the + arm minus the − arm (`graph/module_pooled_z.npy`, row 5), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it (+ arm up, − arm down): [[Topotecan (hydrochloride) (drug)]] 0.5 µM (+4.5, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (+4.3, ⚠ cell-cycle shift); [[Darinaparsin (drug)]] 5 µM (+3.6, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (+3.3, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (+3.3, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (+3.2, ⚠ toxic; transcription drop; cell-cycle shift); [[Trifluridine (drug)]] 0.5 µM (+3.2, ⚠ cell-cycle shift); [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM (+3.2); [[Raltitrexed (drug)]] 5 µM (+2.8, ⚠ cell-cycle shift); [[Bentamapimod (drug)]] 0.05 µM (+2.8); [[Radotinib (drug)]] 5 µM (+2.8); [[Demeclocycline (drug)]] 5 µM (+2.7); [[Retinoic acid (drug)]] 0.05 µM (+2.7); [[Pyridoxine (hydrochloride) (drug)]] 5 µM (+2.5); [[Flumatinib (mesylate) (drug)]] 5 µM (+2.5); [[Bentamapimod (drug)]] 5 µM (+2.5); [[Ralimetinib dimesylate (drug)]] 5 µM (+2.4); [[Olanzapine (drug)]] 5 µM (+2.2) (109 in all, 27 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)
- Lower it: [[Homoharringtonine (drug)]] 5 µM (-22.5, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-14.1, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-11.1, ⚠ cell-cycle shift); [[Auranofin (drug)]] 5 µM (-7.7); [[Selinexor (drug)]] 5 µM (-7.4, ⚠ cell-cycle shift); [[Bortezomib (drug)]] 0.05 µM (-6.6, ⚠ cell-cycle shift); [[Selinexor (drug)]] 0.5 µM (-6.6, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (-5.5, ⚠ cell-cycle shift); [[TAK-901 (drug)]] 5 µM (-5.1, ⚠ cell-cycle shift); [[Artesunate (drug)]] 5 µM (-4.7, ⚠ cell-cycle shift); [[Vinblastine (sulfate) (drug)]] 5 µM (-3.9); [[Pitavastatin (Calcium) (drug)]] 0.5 µM (-3.7); [[Entrectinib (drug)]] 5 µM (-3.7); [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM (-3.6); [[PH-797804 (drug)]] 5 µM (-3.5); [[Almonertinib (mesylate) (drug)]] 5 µM (-3.2); [[Niclosamide (olamine) (drug)]] 0.5 µM (-3.1); [[Neratinib (maleate) (drug)]] 5 µM (-3.0); [[Ixazomib citrate (drug)]] 0.5 µM (-2.8) (129 in all, 33 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[A-427 (line)]], [[A498 (line)]], [[PANC-1 (line)]], [[SW480 (line)]], [[NCI-H23 (line)]], [[NCI-H460 (line)]], [[SNU-1 (line)]], [[A-172 (line)]]

## Candidate new members

*Members not annotated to the set their arm is enriched for, ranked by mean cos to the annotated members (`validation/novel_members.csv`); ⚠ = a reason to doubt the gene's place (in the vector space only through flagged drug-doses), kept in its rank. 188 candidates, none with an alert; shown: the 15 strongest.*

| # | Gene | Set | Mean cos |
|---|---|---|---|
| 1 | [[GINS1]] | Activation of ATR in response to replication stress | +0.78 |
| 2 | [[EXO1]] | DNA strand elongation | +0.77 |
| 3 | [[WDR76]] | E2F G1/S | +0.77 |
| 4 | [[DTL]] | DNA strand elongation | +0.76 |
| 5 | [[MCM10]] | DNA strand elongation | +0.76 |
| 6 | [[CDC45]] | HDR through Homologous Recombination (HRR) or Single Strand Annealing (SSA) | +0.76 |
| 7 | [[WDHD1]] | DNA strand elongation | +0.75 |
| 8 | [[MYBL2]] | E2F G1/S | +0.75 |
| 9 | [[POLE]] | Activation of ATR in response to replication stress | +0.75 |
| 10 | [[CLSPN]] | S Phase | +0.75 |
| 11 | [[GINS2]] | Activation of ATR in response to replication stress | +0.74 |
| 12 | [[CDC25A]] | Activation of the pre-replicative complex | +0.74 |
| 13 | [[CHAF1A]] | S Phase | +0.74 |
| 14 | [[FANCA]] | DNA strand elongation | +0.74 |
| 15 | [[CENPK]] | DNA strand elongation | +0.74 |

## + arm (231)

| Gene | Projection | Name |
|---|---|---|
| [[EXO1]] | 0.961 | exonuclease 1 |
| [[WDR76]] | 0.950 | WD repeat domain 76 |
| [[CDC45]] | 0.944 | cell division cycle 45 |
| [[MYBL2]] | 0.941 | MYB proto-oncogene like 2 |
| [[DTL]] | 0.937 | denticleless E3 ubiquitin protein ligase adapter |
| [[WDHD1]] | 0.937 | WD repeat and HMG-box DNA binding protein 1 |
| [[CENPK]] | 0.932 | centromere protein K |
| [[GINS1]] | 0.927 | GINS complex subunit 1 |
| [[MELK]] | 0.927 | maternal embryonic leucine zipper kinase |
| [[FANCI]] | 0.924 | FA complementation group I |
| [[DSCC1]] | 0.920 | DNA replication and sister chromatid cohesion 1 |
| [[FANCA]] | 0.919 | FA complementation group A |
| [[MCM4]] | 0.918 | minichromosome maintenance complex component 4 |
| [[MCM10]] | 0.916 | minichromosome maintenance 10 replication initiation factor |
| [[POLQ]] | 0.914 | DNA polymerase theta |
| [[RAD54L]] | 0.914 | RAD54 like |
| [[MMS22L]] | 0.913 | MMS22 like, DNA repair protein |
| [[MCM3]] | 0.913 | minichromosome maintenance complex component 3 |
| [[BLM]] | 0.906 | BLM RecQ like helicase |
| [[CLSPN]] | 0.906 | claspin |
| [[CHAF1A]] | 0.899 | chromatin assembly factor 1 subunit A |
| [[NCAPG2]] | 0.898 | non-SMC condensin II complex subunit G2 |
| [[ATAD2]] | 0.897 | ATPase family AAA domain containing 2 |
| [[POLE]] | 0.896 | DNA polymerase epsilon, catalytic subunit |
| [[CENPM]] | 0.895 | centromere protein M |
| [[RAD51]] | 0.895 | RAD51 recombinase |
| [[MCM8]] | 0.893 | minichromosome maintenance 8 homologous recombination repair factor |
| [[RRM1]] | 0.891 | ribonucleotide reductase catalytic subunit M1 |
| [[PCLAF]] | 0.888 | PCNA clamp associated factor |
| [[E2F1]] | 0.884 | E2F transcription factor 1 |
| [[XRCC2]] | 0.884 | X-ray repair cross complementing 2 |
| [[GINS2]] | 0.883 | GINS complex subunit 2 |
| [[RAD51AP1]] | 0.880 | RAD51 associated protein 1 |
| [[RFC4]] | 0.878 | replication factor C subunit 4 |
| [[E2F8]] | 0.877 | E2F transcription factor 8 |
| [[BRIP1]] | 0.876 | BRCA1 interacting DNA helicase 1 |
| [[FANCB]] | 0.876 | FA complementation group B |
| [[HELLS]] | 0.875 | helicase, lymphoid specific |
| [[DDX12P]] | 0.875 | DEAD/H-box helicase 12, pseudogene |
| [[E2F2]] | 0.874 | E2F transcription factor 2 |
| [[PKMYT1]] | 0.874 | protein kinase, membrane associated tyrosine/threonine 1 |
| [[RFC5]] | 0.870 | replication factor C subunit 5 |
| [[TIMELESS]] | 0.869 | timeless circadian regulator |
| [[NCAPD3]] | 0.867 | non-SMC condensin II complex subunit D3 |
| [[VRK1]] | 0.866 | VRK serine/threonine kinase 1 |
| [[CENPU]] | 0.866 | centromere protein U |
| [[XRCC3]] | 0.866 | X-ray repair cross complementing 3 |
| [[MCM5]] | 0.866 | minichromosome maintenance complex component 5 |
| [[CDC6]] | 0.865 | cell division cycle 6 |
| [[RRM2]] | 0.865 | ribonucleotide reductase regulatory subunit M2 |
| [[TCF19]] | 0.862 | transcription factor 19 |
| [[DNA2]] | 0.862 | DNA replication helicase/nuclease 2 |
| [[FANCD2]] | 0.861 | FA complementation group D2 |
| [[CENPH]] | 0.860 | centromere protein H |
| [[MCM2]] | 0.855 | minichromosome maintenance complex component 2 |
| [[ORC1]] | 0.854 | origin recognition complex subunit 1 |
| [[POLA1]] | 0.852 | DNA polymerase alpha 1, catalytic subunit |
| [[CDC25A]] | 0.851 | cell division cycle 25A |
| [[ATAD5]] | 0.850 | ATPase family AAA domain containing 5 |
| [[CDC7]] | 0.850 | cell division cycle 7 |
| [[FAM111B]] | 0.849 | FAM111 trypsin like peptidase B |
| [[PRIM1]] | 0.848 | DNA primase subunit 1 |
| [[UHRF1]] | 0.848 | ubiquitin like with PHD and ring finger domains 1 |
| [[TONSL]] | 0.848 | tonsoku like, DNA repair protein |
| [[TK1]] | 0.842 | thymidine kinase 1 |
| [[MIR924HG]] | 0.842 | MIR924 host gene |
| [[DDX11]] | 0.837 | DEAD/H-box helicase 11 |
| [[KNTC1]] | 0.837 | kinetochore associated 1 |
| [[ZNF367]] | 0.837 | zinc finger protein 367 |
| [[POLD3]] | 0.837 | DNA polymerase delta 3, accessory subunit |
| [[ZWINT]] | 0.835 | ZW10 interacting kinetochore protein |
| [[ZGRF1]] | 0.833 | zinc finger GRF-type containing 1 |
| [[CEP78]] | 0.827 | centrosomal protein 78 |
| [[MND1]] | 0.823 | meiotic nuclear divisions 1 |
| [[RBL1]] | 0.823 | RB transcriptional corepressor like 1 |
| [[RANBP1]] | 0.816 | RAN binding protein 1 |
| [[RFC3]] | 0.816 | replication factor C subunit 3 |
| [[CENPN]] | 0.812 | centromere protein N |
| [[RECQL4]] | 0.808 | RecQ like helicase 4 |
| [[FANCG]] | 0.803 | FA complementation group G |
| [[TYMS]] | 0.802 | thymidylate synthetase |
| [[MSH2]] | 0.801 | mutS homolog 2 |
| [[CHEK1]] | 0.801 | checkpoint kinase 1 |
| [[PASK]] | 0.800 | PAS domain containing serine/threonine kinase |
| [[MCM6]] | 0.798 | minichromosome maintenance complex component 6 |
| [[POLE2]] | 0.794 | DNA polymerase epsilon 2, accessory subunit |
| [[POLA2]] | 0.792 | DNA polymerase alpha 2, accessory subunit |
| [[HAT1]] | 0.791 | histone acetyltransferase 1 |
| [[RNASEH2A]] | 0.789 | ribonuclease H2 subunit A |
| [[BRCA1]] | 0.788 | BRCA1 DNA repair associated |
| [[CDCA7]] | 0.787 | cell division cycle associated 7 |
| [[RFC2]] | 0.787 | replication factor C subunit 2 |
| [[CDK2]] | 0.783 | cyclin dependent kinase 2 |
| [[CSE1L]] | 0.782 | chromosome segregation 1 like |
| [[CCDC150]] | 0.780 | coiled-coil domain containing 150 |
| [[ORC6]] | 0.779 | origin recognition complex subunit 6 |
| [[FEN1]] | 0.775 | flap structure-specific endonuclease 1 |
| [[SHMT1]] | 0.775 | serine hydroxymethyltransferase 1 |
| [[DNMT1]] | 0.766 | DNA methyltransferase 1 |
| [[HAUS1]] | 0.754 | HAUS augmin like complex subunit 1 |
| [[POLD1]] | 0.753 | DNA polymerase delta 1, catalytic subunit |
| [[TRIP13]] | 0.753 | thyroid hormone receptor interactor 13 |
| [[CCNE2]] | 0.751 | cyclin E2 |
| [[EZH2]] | 0.746 | enhancer of zeste 2 polycomb repressive complex 2 subunit |
| [[LIG1]] | 0.745 | DNA ligase 1 |
| [[NCAPH2]] | 0.742 | non-SMC condensin II complex subunit H2 |
| [[TFDP1]] | 0.740 | transcription factor Dp-1 |
| [[RBBP7]] | 0.739 | RB binding protein 7, chromatin remodeling factor |
| [[SMC1A]] | 0.739 | structural maintenance of chromosomes 1A |
| [[PSMC3IP]] | 0.737 | PSMC3 interacting protein |
| [[ZWILCH]] | 0.731 | zwilch kinetochore protein |
| [[TUBGCP3]] | 0.726 | tubulin gamma complex component 3 |
| [[DYNC2I2]] | 0.725 | dynein 2 intermediate chain 2 |
| [[MSH5]] | 0.721 | mutS homolog 5 |
| [[CEP128]] | 0.713 | centrosomal protein 128 |
| [[TUBA1B]] | 0.708 | tubulin alpha 1b |
| [[GINS4]] | 0.707 | GINS complex subunit 4 |
| [[GMPS]] | 0.707 | guanosine monophosphate synthase |
| [[UBR7]] | 0.703 | ubiquitin protein ligase E3 component n-recognin 7 |
| [[RTTN]] | 0.700 | rotatin |
| [[MCM7]] | 0.696 | minichromosome maintenance complex component 7 |
| [[DDX11-AS1]] | 0.694 | DDX11 antisense RNA 1 |
| [[TUBG1]] | 0.690 | tubulin gamma 1 |
| [[RAD18]] | 0.688 | RAD18 E3 ubiquitin protein ligase |
| [[CENPP]] | 0.685 | centromere protein P |
| [[CDT1]] | 0.681 | chromatin licensing and DNA replication factor 1 |
| [[ZNF730]] | 0.677 | zinc finger protein 730 |
| [[PRIM2]] | 0.675 | DNA primase subunit 2 |
| [[CASP2]] | 0.675 | caspase 2 |
| [[PXMP2]] | 0.672 | peroxisomal membrane protein 2 |
| [[FANCC]] | 0.671 | FA complementation group C |
| [[HAUS5]] | 0.671 | HAUS augmin like complex subunit 5 |
| [[SUV39H2]] | 0.670 | SUV39H2 histone lysine methyltransferase |
| [[PCNA]] | 0.670 | proliferating cell nuclear antigen |
| [[BRME1]] | 0.668 | break repair meiotic recombinase recruitment factor 1 |
| [[C4orf46]] | 0.667 | chromosome 4 open reading frame 46 |
| [[MTHFD1]] | 0.664 | methylenetetrahydrofolate dehydrogenase, cyclohydrolase and formyltetrahydrofolate synthetase 1 |
| [[BRI3BP]] | 0.659 | BRI3 binding protein |
| [[PRPS2]] | 0.658 | phosphoribosyl pyrophosphate synthetase 2 |
| [[RPA2]] | 0.653 | replication protein A2 |
| [[LYPD6]] | 0.652 | LY6/PLAUR domain containing 6 |
| [[AUNIP]] | 0.651 | aurora kinase A and ninein interacting protein |
| [[LSM4]] | 0.650 | LSM4 homolog, U6 small nuclear RNA and mRNA degradation associated |
| [[NASP]] | 0.650 | nuclear autoantigenic sperm protein |
| [[CHAF1B]] | 0.648 | chromatin assembly factor 1 subunit B |
| [[DUT]] | 0.648 | deoxyuridine triphosphatase |
| [[CDK5RAP2]] | 0.646 | CDK5 regulatory subunit associated protein 2 |
| [[CHTF18]] | 0.644 | chromosome transmission fidelity factor 18 |
| [[PARP1]] | 0.642 | poly(ADP-ribose) polymerase 1 |
| [[CENPQ]] | 0.641 | centromere protein Q |
| [[FANCL]] | 0.641 | FA complementation group L |
| [[NUP205]] | 0.635 | nucleoporin 205 |
| [[TTF2]] | 0.633 | transcription termination factor 2 |
| [[NUP107]] | 0.632 | nucleoporin 107 |
| [[ERI1]] | 0.631 | exoribonuclease 1 |
| [[HADH]] | 0.630 | hydroxyacyl-CoA dehydrogenase |
| [[SLFN13]] | 0.630 | schlafen family member 13 |
| [[WDR90]] | 0.628 | WD repeat domain 90 |
| [[SAE1]] | 0.627 | SUMO1 activating enzyme subunit 1 |
| [[TMEM109]] | 0.625 | transmembrane protein 109 |
| [[FIGNL1]] | 0.625 | fidgetin like 1 |
| [[TUBB]] | 0.624 | tubulin beta class I |
| [[HAUS6]] | 0.624 | HAUS augmin like complex subunit 6 |
| [[MYO19]] | 0.624 | myosin XIX |
| [[IPO9]] | 0.624 | importin 9 |
| [[MRE11]] | 0.623 | MRE11 double strand break repair nuclease |
| [[TP73]] | 0.607 | tumor protein p73 |
| [[NUDT15]] | 0.605 | nudix hydrolase 15 |
| [[GUSB]] | 0.599 | glucuronidase beta |
| [[UNG]] | 0.599 | uracil DNA glycosylase |
| [[NPAT]] | 0.598 | nuclear protein, coactivator of histone transcription |
| [[CCDC14]] | 0.597 | coiled-coil domain containing 14 |
| [[TBC1D31]] | 0.596 | TBC1 domain family member 31 |
| [[DCK]] | 0.595 | deoxycytidine kinase |
| [[MYCBP]] | 0.593 | MYC binding protein |
| [[GGCT]] | 0.592 | gamma-glutamylcyclotransferase |
| [[POLD2]] | 0.589 | DNA polymerase delta 2, accessory subunit |
| [[NUP210]] | 0.584 | nucleoporin 210 |
| [[CNOT9]] | 0.579 | CCR4-NOT transcription complex subunit 9 |
| [[CEP72]] | 0.579 | centrosomal protein 72 |
| [[SPIN4]] | 0.577 | spindlin family member 4 |
| [[MCMBP]] | 0.575 | minichromosome maintenance complex binding protein |
| [[TMEM106C]] | 0.572 | transmembrane protein 106C |
| [[GINS3]] | 0.571 | GINS complex subunit 3 |
| [[GSTCD]] | 0.570 | glutathione S-transferase C-terminal domain containing |
| [[TERT]] | 0.567 | telomerase reverse transcriptase |
| [[DCLRE1B]] | 0.566 | DNA cross-link repair 1B |
| [[NSMCE4A]] | 0.562 | NSE4A component of SMC5/6 complex |
| [[SNRPA]] | 0.559 | small nuclear ribonucleoprotein polypeptide A |
| [[RBBP8]] | 0.557 | RB binding protein 8, endonuclease |
| [[LRRC45]] | 0.556 | leucine rich repeat containing 45 |
| [[SCARA3]] | 0.556 | scavenger receptor class A member 3 |
| [[ERLIN1]] | 0.555 | ER lipid raft associated 1 |
| [[LINC01036]] | 0.554 | long independently transcribed non-coding RNA 1036 |
| [[ALMS1]] | 0.552 | ALMS1 centrosome and basal body associated protein |
| [[RAD1]] | 0.545 | RAD1 checkpoint DNA exonuclease |
| [[SNRNP40]] | 0.544 | small nuclear ribonucleoprotein U5 subunit 40 |
| [[ACTL6A]] | 0.543 | actin like 6A |
| [[ACYP1]] | 0.543 | acylphosphatase 1 |
| [[EMP2]] | 0.541 | epithelial membrane protein 2 |
| [[ZNF732]] | 0.540 | zinc finger protein 732 |
| [[PRIMPOL]] | 0.539 | primase and DNA directed polymerase |
| [[NEDD1]] | 0.534 | NEDD1 gamma-tubulin ring complex targeting factor |
| [[LRRCC1]] | 0.526 | leucine rich repeat and coiled-coil centrosomal protein 1 |
| [[NUP43]] | 0.525 | nucleoporin 43 |
| [[CCDC15]] | 0.518 | coiled-coil domain containing 15 |
| [[CMTM1]] | 0.515 | CKLF like MARVEL transmembrane domain containing 1 |
| [[CASP8AP2]] | 0.513 | caspase 8 associated protein 2 |
| [[SLBP]] | 0.510 | stem-loop histone mRNA binding protein |
| [[TEDC1]] | 0.503 | tubulin epsilon and delta complex 1 |
| [[MSH6]] | 0.500 | mutS homolog 6 |
| [[MNS1]] | 0.499 | meiosis specific nuclear structural 1 |
| [[ARL6IP6]] | 0.491 | ARF like GTPase 6 interacting protein 6 |
| [[KPNB1]] | 0.488 | karyopherin subunit beta 1 |
| [[PIGX]] | 0.487 | phosphatidylinositol glycan anchor biosynthesis class X |
| [[CDCA7L]] | 0.484 | cell division cycle associated 7 like |
| [[CNOT10]] | 0.484 | CCR4-NOT transcription complex subunit 10 |
| [[PCYOX1L]] | 0.463 | prenylcysteine oxidase 1 like |
| [[IMMT]] | 0.462 | inner membrane mitochondrial protein |
| [[SSRP1]] | 0.460 | structure specific recognition protein 1 |
| [[SYTL4]] | 0.450 | synaptotagmin like 4 |
| [[CCNE1]] | 0.449 | cyclin E1 |
| [[ZNF443]] | 0.431 | zinc finger protein 443 |
| [[DHRS11]] | 0.409 | dehydrogenase/reductase 11 |
| [[E2F7]] | 0.398 | E2F transcription factor 7 |
| [[TBC1D1]] | 0.378 | TBC1 domain family member 1 |
| [[SAPCD1]] | 0.366 | suppressor APC domain containing 1 |
| [[PTPRG-AS1]] | 0.346 | PTPRG antisense RNA 1 |
| [[RPSAP58]] | 0.332 | ribosomal protein SA 2 |
| [[ZNF799]] | 0.318 | zinc finger protein 799 |
| [[ZDHHC13]] | 0.289 | zDHHC palmitoyltransferase 13 |

## − arm (5)

| Gene | Projection | Name |
|---|---|---|
| [[ATP6V1G1]] | -0.609 | ATPase H+ transporting V1 subunit G1 |
| [[CPEB4]] | -0.494 | cytoplasmic polyadenylation element binding protein 4 |
| [[TMEM150A]] | -0.470 | transmembrane protein 150A |
| [[RNF10]] | -0.460 | ring finger protein 10 |
| [[ARHGAP5]] | -0.307 | Rho GTPase activating protein 5 |

## Data

- `graph/nodes.parquet` — module == 6; `graph/modules.parquet` — module == 6; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [5] (drug-dose × line)
