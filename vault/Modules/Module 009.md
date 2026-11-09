---
module: 9
type: "module"
n_genes: 222
n_plus: 222
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: "Neuronal System"
label_source: "reactome"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 009

*Neuronal System · 222 genes (single-armed) · [[Module 009.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

Label from the validation stage: **Neuronal System** (reactome, q 0.009; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | Neuronal System | reactome | 15/222 | 3.61 | 0.009 |
| + | Neuronal System | reactome | 15/222 | 3.61 | 0.009 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 8), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM (+12.7, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (+9.9); [[Homoharringtonine (drug)]] 5 µM (+9.4, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (+9.2, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (+8.9, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+6.7, ⚠ toxic; transcription drop; cell-cycle shift); [[Tucidinostat (drug)]] 0.5 µM (+6.0, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (+4.0, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (+4.0, ⚠ cell-cycle shift); [[Auranofin (drug)]] 5 µM (+3.7); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+3.2); [[Cobimetinib (drug)]] 5 µM (+2.6); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM (+2.0); [[Ponatinib (drug)]] 0.5 µM (+2.0); [[Ipatasertib (drug)]] 0.5 µM (+1.9); [[Trametinib (drug)]] 0.5 µM (+1.9); [[Brivudine (drug)]] 5 µM (+1.8); [[XRK3F2 (drug)]] 0.5 µM (+1.7) (78 in all, 33 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)
- Lower it: [[Mebendazole (drug)]] 5 µM (-1.9); [[Adagrasib (drug)]] 0.05 µM (-1.7, ⚠ position not correctable); [[Lucanthone (drug)]] 0.05 µM (-1.7); [[Dexamethasone (drug)]] 0.5 µM (-1.7); [[Digitoxin (drug)]] 0.05 µM (-1.7, ⚠ cell-cycle shift); [[Artesunate (drug)]] 0.5 µM (-1.5); [[Digitoxin (drug)]] 0.5 µM (-1.5, ⚠ cell-cycle shift); [[Fenofibrate (drug)]] 0.05 µM (-1.5); [[Pravastatin (sodium) (drug)]] 5 µM (-1.5); [[Erlotinib (drug)]] 0.05 µM (-1.4); [[Rutin (trihydrate) (drug)]] 0.05 µM (-1.4); [[Diphenhydramine (drug)]] 0.05 µM (-1.3); [[5-Azacytidine (drug)]] 5 µM (-1.3) (40 in all, 8 with an alert ⚠; shown: the 10 strongest and the 3 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[AN3 CA (line)]], [[C-33 A (line)]], [[HOP62 (line)]], [[SHP-77 (line)]], [[A-427 (line)]], [[NCI-H23 (line)]], [[SNU-1 (line)]], [[NCI-H2347 (line)]]

## Candidate new members

*Members not annotated to the set their arm is enriched for, ranked by mean cos to the annotated members (`validation/novel_members.csv`); ⚠ = a reason to doubt the gene's place (in the vector space only through flagged drug-doses), kept in its rank. 18 candidates, none with an alert; shown: the 15 strongest.*

| # | Gene | Set | Mean cos |
|---|---|---|---|
| 1 | [[SRRM4]] | Neuronal System | +0.57 |
| 2 | [[SYT4]] | Neuronal System | +0.57 |
| 3 | [[RALYL]] | Neuronal System | +0.57 |
| 4 | [[LINC02197]] | Neuronal System | +0.56 |
| 5 | [[KHDRBS2]] | Neuronal System | +0.56 |
| 6 | [[RIT2]] | Neuronal System | +0.56 |
| 7 | [[ASCL1]] | Neuronal System | +0.55 |
| 8 | [[CDH12]] | Neuronal System | +0.54 |
| 9 | [[RUNX1T1]] | Neuronal System | +0.54 |
| 10 | [[CDH10]] | Neuronal System | +0.53 |
| 11 | [[NELL1]] | Neuronal System | +0.53 |
| 12 | [[UNC80]] | Neuronal System | +0.52 |
| 13 | [[PCSK1]] | Neuronal System | +0.51 |
| 14 | [[ASXL3]] | Neuronal System | +0.51 |
| 15 | [[PCDH9]] | Neuronal System | +0.51 |

## + arm (222)

| Gene | Projection | Name |
|---|---|---|
| [[CDH12]] | 0.814 | cadherin 12 |
| [[RALYL]] | 0.795 | RALY RNA binding protein like |
| [[CDH10]] | 0.784 | cadherin 10 |
| [[KCNH7]] | 0.777 | potassium voltage-gated channel subfamily H member 7 |
| [[NCAM2]] | 0.773 | neural cell adhesion molecule 2 |
| [[GRIA2]] | 0.770 | glutamate ionotropic receptor AMPA type subunit 2 |
| [[LINC02197]] | 0.760 | long independently transcribed non-coding RNA 2197 |
| [[PCDH9]] | 0.758 | protocadherin 9 |
| [[ADGRL3]] | 0.752 | adhesion G protein-coupled receptor L3 |
| [[MAPK10]] | 0.751 | mitogen-activated protein kinase 10 |
| [[EPHA5]] | 0.742 | EPH receptor A5 |
| [[LINC01695]] | 0.739 | long independently transcribed non-coding RNA 1695 |
| [[ASXL3]] | 0.738 | ASXL transcriptional regulator 3 |
| [[MARCHF1]] | 0.733 | membrane associated ring-CH-type finger 1 |
| [[NRXN1]] | 0.732 | neurexin 1 |
| [[KHDRBS2]] | 0.730 | KH RNA binding domain containing, signal transduction associated 2 |
| [[DMD]] | 0.729 | dystrophin |
| [[CDH18]] | 0.724 | cadherin 18 |
| [[RUNX1T1]] | 0.713 | RUNX1 partner transcriptional co-repressor 1 |
| [[KCND2]] | 0.713 | potassium voltage-gated channel subfamily D member 2 |
| [[LRFN2]] | 0.712 | leucine rich repeat and fibronectin type III domain containing 2 |
| [[SLITRK6]] | 0.711 | SLIT and NTRK like family member 6 |
| [[FMN2]] | 0.709 | formin 2 |
| [[SYT4]] | 0.705 | synaptotagmin 4 |
| [[SCN2A]] | 0.704 | sodium voltage-gated channel alpha subunit 2 |
| [[CRISPLD1]] | 0.704 | cysteine rich secretory protein LCCL domain containing 1 |
| [[MSR1]] | 0.701 | macrophage scavenger receptor 1 |
| [[EGFEM1P]] | 0.700 | EGF like and EMI domain containing 1, pseudogene |
| [[PDGFD]] | 0.700 | platelet derived growth factor D |
| [[CSRNP3]] | 0.696 | cysteine and serine rich nuclear protein 3 |
| [[OFCC1]] | 0.692 | orofacial cleft 1 candidate 1 (pseudogene) |
| [[KCTD8]] | 0.692 | potassium channel tetramerization domain containing 8 |
| [[CDH8]] | 0.691 | cadherin 8 |
| [[EPHA7]] | 0.687 | EPH receptor A7 |
| [[CACNB2]] | 0.686 | calcium voltage-gated channel auxiliary subunit beta 2 |
| [[SRRM4]] | 0.685 | serine/arginine repetitive matrix 4 |
| [[PEX5L]] | 0.683 | peroxisomal biogenesis factor 5 like |
| [[ERBB4]] | 0.683 | erb-b2 receptor tyrosine kinase 4 |
| [[CTNNA2]] | 0.682 | catenin alpha 2 |
| [[CSMD3]] | 0.678 | CUB and Sushi multiple domains 3 |
| [[GRIK1]] | 0.675 | glutamate ionotropic receptor kainate type subunit 1 |
| [[EPHA5-AS1]] | 0.675 | EPHA5 antisense RNA 1 |
| [[SEMA3E]] | 0.675 | semaphorin 3E |
| [[KCNB2]] | 0.673 | potassium voltage-gated channel subfamily B member 2 |
| [[EPHA6]] | 0.673 | EPH receptor A6 |
| [[ASCL1]] | 0.667 | achaete-scute family bHLH transcription factor 1 |
| [[RIT2]] | 0.665 | Ras like without CAAX 2 |
| [[SYT1]] | 0.664 | synaptotagmin 1 |
| [[NPFFR2]] | 0.664 | neuropeptide FF receptor 2 |
| [[GRIK2]] | 0.661 | glutamate ionotropic receptor kainate type subunit 2 |
| [[ATRNL1]] | 0.659 | attractin like 1 |
| [[AKAP6]] | 0.655 | A-kinase anchoring protein 6 |
| [[UNC80]] | 0.653 | unc-80 subunit of NALCN channel complex |
| [[DGKB]] | 0.653 | diacylglycerol kinase beta |
| [[THSD7A]] | 0.651 | thrombospondin type 1 domain containing 7A |
| [[NELL1]] | 0.651 | neural EGFL like 1 |
| [[LINC01287]] | 0.651 | long independently transcribed non-coding RNA 1287 |
| [[TOX]] | 0.650 | thymocyte selection associated high mobility group box |
| [[LINC02484]] | 0.648 | long independently transcribed non-coding RNA 2484 |
| [[FSTL5]] | 0.645 | follistatin like 5 |
| [[MMP16]] | 0.644 | matrix metallopeptidase 16 |
| [[ADAMTS3]] | 0.639 | ADAM metallopeptidase with thrombospondin type 1 motif 3 |
| [[SPOCK3]] | 0.639 | SPARC (osteonectin), cwcv and kazal like domains proteoglycan 3 |
| [[SCN3A]] | 0.638 | sodium voltage-gated channel alpha subunit 3 |
| [[HMCN1]] | 0.637 | hemicentin 1 |
| [[PCDH10]] | 0.636 | protocadherin 10 |
| [[SOX5]] | 0.634 | SRY-box transcription factor 5 |
| [[FUT9]] | 0.630 | fucosyltransferase 9 |
| [[ESRRG]] | 0.629 | estrogen related receptor gamma |
| [[LDB2]] | 0.629 | LIM domain binding 2 |
| [[PCDH18]] | 0.628 | protocadherin 18 |
| [[ADGRV1]] | 0.627 | adhesion G protein-coupled receptor V1 |
| [[POU6F2]] | 0.627 | POU class 6 homeobox 2 |
| [[FAM133A]] | 0.625 | family with sequence similarity 133 member A |
| [[PCSK1]] | 0.624 | proprotein convertase subtilisin/kexin type 1 |
| [[GABRA2]] | 0.623 | gamma-aminobutyric acid type A receptor subunit alpha2 |
| [[SNTG1]] | 0.622 | syntrophin gamma 1 |
| [[CADM2]] | 0.622 | cell adhesion molecule 2 |
| [[SCG2]] | 0.621 | secretogranin II |
| [[PCDH17]] | 0.621 | protocadherin 17 |
| [[UNC5C]] | 0.618 | unc-5 netrin receptor C |
| [[PPARGC1A]] | 0.615 | PPARG coactivator 1 alpha |
| [[DISC1FP1]] | 0.610 | DISC1 fusion partner 1 |
| [[NELL2]] | 0.604 | neural EGFL like 2 |
| [[KLHL13]] | 0.604 | kelch like family member 13 |
| [[TLL1]] | 0.603 | tolloid like 1 |
| [[PIEZO2]] | 0.601 | piezo type mechanosensitive ion channel component 2 |
| [[B3GALT1]] | 0.600 | beta-1,3-galactosyltransferase 1 |
| [[BMP5]] | 0.599 | bone morphogenetic protein 5 |
| [[VAV3]] | 0.599 | vav guanine nucleotide exchange factor 3 |
| [[NKAIN3]] | 0.598 | sodium/potassium transporting ATPase interacting 3 |
| [[LINC01320]] | 0.598 | long independently transcribed non-coding RNA 1320 |
| [[CGA]] | 0.597 | glycoprotein hormones, alpha polypeptide |
| [[LINC02492]] | 0.592 | long independently transcribed non-coding RNA 2492 |
| [[ADARB2]] | 0.591 | adenosine deaminase RNA specific B2 (inactive) |
| [[CA8]] | 0.590 | carbonic anhydrase 8 (inactive) |
| [[LINC01194]] | 0.590 | long independently transcribed non-coding RNA 1194 |
| [[ANGPT1]] | 0.590 | angiopoietin 1 |
| [[TAFA5]] | 0.586 | TAFA chemokine like family member 5 |
| [[PRKG1]] | 0.586 | protein kinase cGMP-dependent 1 |
| [[PPP2R2B]] | 0.578 | protein phosphatase 2 regulatory subunit Bbeta |
| [[MID1]] | 0.577 | midline 1 |
| [[GALNT13]] | 0.573 | polypeptide N-acetylgalactosaminyltransferase 13 |
| [[SLC6A15]] | 0.570 | solute carrier family 6 member 15 |
| [[LINC02241]] | 0.568 | long independently transcribed non-coding RNA 2241 |
| [[MTMR7]] | 0.568 | myotubularin related protein 7 |
| [[TMPRSS15]] | 0.566 | transmembrane serine protease 15 |
| [[TSHZ2]] | 0.566 | teashirt zinc finger homeobox 2 |
| [[FREM2]] | 0.564 | FRAS1 related extracellular matrix 2 |
| [[BHMT2]] | 0.562 | betaine--homocysteine S-methyltransferase 2 |
| [[ZFHX4]] | 0.562 | zinc finger homeobox 4 |
| [[BRINP3]] | 0.561 | BMP/retinoic acid inducible neural specific 3 |
| [[ABCA13]] | 0.560 | ATP binding cassette subfamily A member 13 |
| [[FAM110B]] | 0.560 | family with sequence similarity 110 member B |
| [[GUCY1A1]] | 0.557 | guanylate cyclase 1 soluble subunit alpha 1 |
| [[RBM20]] | 0.554 | RNA binding motif protein 20 |
| [[SOX2]] | 0.549 | SRY-box transcription factor 2 |
| [[LYPD1]] | 0.549 | LY6/PLAUR domain containing 1 |
| [[COL11A1]] | 0.547 | collagen type XI alpha 1 chain |
| [[ADGRL2]] | 0.546 | adhesion G protein-coupled receptor L2 |
| [[MIR99AHG]] | 0.545 | mir-99a-let-7c cluster host gene |
| [[ROBO1]] | 0.544 | roundabout guidance receptor 1 |
| [[VIPR2]] | 0.542 | vasoactive intestinal peptide receptor 2 |
| [[CDH6]] | 0.542 | cadherin 6 |
| [[GAP43]] | 0.541 | growth associated protein 43 |
| [[PLXDC2]] | 0.540 | plexin domain containing 2 |
| [[LINC01885]] | 0.539 | long independently transcribed non-coding RNA 1885 |
| [[RORB]] | 0.536 | RAR related orphan receptor B |
| [[PLCB1]] | 0.534 | phospholipase C beta 1 |
| [[SPTB]] | 0.532 | spectrin beta, erythrocytic |
| [[CALCRL]] | 0.532 | calcitonin receptor like receptor |
| [[MAGEA10]] | 0.527 | MAGE family member A10 |
| [[CALCA]] | 0.526 | calcitonin related polypeptide alpha |
| [[NEGR1]] | 0.524 | neuronal growth regulator 1 |
| [[SOX11]] | 0.522 | SRY-box transcription factor 11 |
| [[MIR4307HG]] | 0.520 | MIR4307 host gene |
| [[PRUNE2]] | 0.518 | prune homolog 2 with BCH domain |
| [[ADAMTS1]] | 0.516 | ADAM metallopeptidase with thrombospondin type 1 motif 1 |
| [[LIN28B]] | 0.513 | lin-28 RNA binding posttranscriptional regulator B |
| [[SFTA3-1]] | 0.511 | — |
| [[PRKD1]] | 0.509 | protein kinase D1 |
| [[AUTS2]] | 0.507 | activator of transcription and developmental regulator AUTS2 |
| [[AR]] | 0.506 | androgen receptor |
| [[FRG1FP]] | 0.505 | FSHD region gene 1 family member F, pseudogene |
| [[FIGN]] | 0.504 | fidgetin, microtubule severing factor |
| [[NR1H4]] | 0.504 | nuclear receptor subfamily 1 group H member 4 |
| [[MCC]] | 0.501 | MCC regulator of Wnt signaling pathway |
| [[AGMO]] | 0.497 | alkylglycerol monooxygenase |
| [[CTNNA3]] | 0.494 | catenin alpha 3 |
| [[LINC02240]] | 0.494 | long independently transcribed non-coding RNA 2240 |
| [[MMRN1]] | 0.493 | multimerin 1 |
| [[CD36]] | 0.492 | CD36 molecule (CD36 blood group) |
| [[FAM13C]] | 0.491 | family with sequence similarity 13 member C |
| [[PDZRN3]] | 0.484 | PDZ domain containing ring finger 3 |
| [[PEG10]] | 0.483 | paternally expressed 10 |
| [[HOXD8]] | 0.480 | homeobox D8 |
| [[ZNF804A]] | 0.479 | zinc finger protein 804A |
| [[LRCH2]] | 0.477 | leucine rich repeats and calponin homology domain containing 2 |
| [[LINC01592]] | 0.477 | long independently transcribed non-coding RNA 1592 |
| [[NCAM1]] | 0.476 | neural cell adhesion molecule 1 |
| [[ZFHX4-AS1]] | 0.474 | ZFHX4 antisense RNA 1 |
| [[ST8SIA6-AS1]] | 0.474 | ST8SIA6 antisense RNA 1 |
| [[BCL11A]] | 0.474 | BCL11 transcription factor A |
| [[GTSF1]] | 0.471 | gametocyte specific factor 1 |
| [[NAA11]] | 0.471 | N-alpha-acetyltransferase 11, NatA catalytic subunit |
| [[LINC02327]] | 0.470 | long independently transcribed non-coding RNA 2327 |
| [[PRLR]] | 0.458 | prolactin receptor |
| [[TENM3]] | 0.458 | teneurin transmembrane protein 3 |
| [[CPE]] | 0.452 | carboxypeptidase E |
| [[LINC01060]] | 0.449 | long independently transcribed non-coding RNA 1060 |
| [[NAALADL2-AS2]] | 0.447 | NAALADL2 antisense RNA 2 |
| [[DPY19L2P1]] | 0.444 | DPY19L2 pseudogene 1 |
| [[CARD18]] | 0.442 | caspase recruitment domain family member 18 |
| [[GPNMB]] | 0.437 | glycoprotein nmb |
| [[TSPAN12]] | 0.437 | tetraspanin 12 |
| [[MAN1C1]] | 0.434 | mannosidase alpha class 1C member 1 |
| [[ADAMTSL3]] | 0.433 | ADAMTS like 3 |
| [[SCN9A]] | 0.433 | sodium voltage-gated channel alpha subunit 9 |
| [[CHST11]] | 0.432 | carbohydrate sulfotransferase 11 |
| [[TP63]] | 0.431 | tumor protein p63 |
| [[SOBP]] | 0.429 | sine oculis binding protein homolog |
| [[MEOX2]] | 0.427 | mesenchyme homeobox 2 |
| [[LINC02360]] | 0.425 | long independently transcribed non-coding RNA 2360 |
| [[CCN3]] | 0.425 | cellular communication network factor 3 |
| [[SNCAIP]] | 0.423 | synuclein alpha interacting protein |
| [[KCTD12]] | 0.422 | potassium channel tetramerization domain containing 12 |
| [[SEMA6A]] | 0.416 | semaphorin 6A |
| [[UBBP4-1]] | 0.416 | — |
| [[LRRIQ1]] | 0.416 | leucine rich repeats and IQ motif containing 1 |
| [[DOK5]] | 0.415 | docking protein 5 |
| [[FSIP2]] | 0.414 | fibrous sheath interacting protein 2 |
| [[COLEC10]] | 0.413 | collectin subfamily member 10 |
| [[HBG2]] | 0.407 | hemoglobin subunit gamma 2 |
| [[LINC01203]] | 0.406 | long independently transcribed non-coding RNA 1203 |
| [[PKIB]] | 0.405 | cAMP-dependent protein kinase inhibitor beta |
| [[LINC00958]] | 0.402 | long independently transcribed non-coding RNA 958 |
| [[LINC01029]] | 0.402 | long independently transcribed non-coding RNA 1029 |
| [[PTPN13]] | 0.401 | protein tyrosine phosphatase non-receptor type 13 |
| [[ENPP2]] | 0.394 | ectonucleotide pyrophosphatase/phosphodiesterase 2 |
| [[AK4P3]] | 0.385 | adenylate kinase 4 pseudogene 3 |
| [[F11-AS1]] | 0.377 | F11 antisense RNA 1 |
| [[SLAIN1]] | 0.375 | SLAIN family member 1 |
| [[GRIA1]] | 0.371 | glutamate ionotropic receptor AMPA type subunit 1 |
| [[SYNM]] | 0.366 | synemin |
| [[LINC02008]] | 0.366 | long independently transcribed non-coding RNA 2008 |
| [[KLRG1]] | 0.353 | killer cell lectin like receptor G1 |
| [[ELOVL4]] | 0.351 | ELOVL fatty acid elongase 4 |
| [[LINC02220]] | 0.348 | long independently transcribed non-coding RNA 2220 |
| [[INA]] | 0.342 | internexin neuronal intermediate filament protein alpha |
| [[FGF9]] | 0.331 | fibroblast growth factor 9 |
| [[OR51B5]] | 0.321 | olfactory receptor family 51 subfamily B member 5 |
| [[DCT]] | 0.314 | dopachrome tautomerase |
| [[SESN3]] | 0.310 | sestrin 3 |
| [[TRIM6]] | 0.298 | tripartite motif containing 6 |
| [[PYDC2-AS1]] | 0.292 | PYDC2 antisense RNA 1 |
| [[DOC2B]] | 0.286 | double C2 domain beta |
| [[H19]] | 0.277 | H19 imprinted maternally expressed transcript |
| [[SIM1]] | 0.264 | SIM bHLH transcription factor 1 |
| [[ECSCR]] | 0.248 | endothelial cell surface expressed chemotaxis and apoptosis regulator |
| [[PTGIS]] | 0.231 | prostaglandin I2 synthase |
| [[MAMDC2]] | 0.209 | MAM domain containing 2 |
| [[LINC00355]] | 0.192 | long independently transcribed non-coding RNA 355 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 9; `graph/modules.parquet` — module == 9; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [8] (drug-dose × line)
