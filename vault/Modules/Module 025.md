---
module: 25
type: "module"
n_genes: 171
n_plus: 144
n_minus: 27
arms_opposite: true
mean_cos_between_arms: -0.3046203851699829
label: "oxidative phosphorylation"
label_source: "hallmark"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 025

*oxidative phosphorylation · 171 genes (144 in the + arm, 27 in the − arm) · [[Module 025.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30). The + arm rises where the − arm falls. Arm = the side of the module's main direction a gene sits on.

Label from the validation stage: **oxidative phosphorylation** (hallmark, q 0.010; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| + | oxidative phosphorylation | hallmark | 10/144 | 5.24 | 0.010 |
| + | fatty acid metabolism | hallmark | 8/144 | 6.30 | 0.017 |
| all | oxidative phosphorylation | hallmark | 10/171 | 4.41 | 0.035 |
| all | fatty acid metabolism | hallmark | 8/171 | 5.30 | 0.048 |

## Drugs that move it

*Mean pooled z of the + arm minus the − arm (`graph/module_pooled_z.npy`, row 24), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it (+ arm up, − arm down): [[Dinaciclib (drug)]] 0.5 µM (+16.5, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (+16.0, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+12.5, ⚠ toxic; transcription drop; cell-cycle shift); [[Selinexor (drug)]] 5 µM (+5.0, ⚠ cell-cycle shift); [[Niclosamide (olamine) (drug)]] 5 µM (+4.7, ⚠ toxic; cell-cycle shift); [[c-Kit-IN-1 (drug)]] 0.05 µM (+4.2, ⚠ unreliable plate only); [[TAK-901 (drug)]] 5 µM (+3.6, ⚠ cell-cycle shift); [[Ixazomib citrate (drug)]] 0.5 µM (+3.4); [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM (+3.2); [[Erlotinib (drug)]] 0.05 µM (+3.0); [[PH-797804 (drug)]] 5 µM (+2.9); [[Belumosudil (drug)]] 5 µM (+2.9); [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM (+2.8); [[Benproperine (phosphate) (drug)]] 0.05 µM (+2.8); [[Fenofibrate (drug)]] 0.05 µM (+2.5); [[Auranofin (drug)]] 5 µM (+2.5); [[Lucanthone (drug)]] 0.05 µM (+2.5) (159 in all, 30 with an alert ⚠; shown: the 10 strongest and the 7 next strongest without an alert)
- Lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM (-6.4, ⚠ cell-cycle shift); [[Ipatasertib (drug)]] 0.5 µM (-4.6); [[Celecoxib (drug)]] 0.5 µM (-3.1); [[Homoharringtonine (drug)]] 5 µM (-3.0, ⚠ cell-cycle shift); [[BAY1125976 (drug)]] 0.5 µM (-3.0); [[Docetaxel (Trihydrate) (drug)]] 0.5 µM (-2.8); [[Thymol (drug)]] 0.5 µM (-2.6); [[Methylprednisolone succinate (drug)]] 0.5 µM (-2.6); [[PH-797804 (drug)]] 0.5 µM (-2.6); [[Digitoxin (drug)]] 5 µM (-2.6, ⚠ toxic; transcription drop; cell-cycle shift); [[Lactate (calcium) (drug)]] 5 µM (-2.4); [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM (-2.4); [[Bergenin (drug)]] 0.5 µM (-2.3) (127 in all, 16 with an alert ⚠; shown: the 10 strongest and the 3 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[SK-MEL-2 (line)]], [[PANC-1 (line)]], [[SW480 (line)]], [[A549 (line)]], [[HOP62 (line)]], [[MIA PaCa-2 (line)]], [[NCI-H1792 (line)]], [[SNU-423 (line)]]

## Candidate new members

*Members not annotated to the set their arm is enriched for, ranked by mean cos to the annotated members (`validation/novel_members.csv`); ⚠ = a reason to doubt the gene's place (in the vector space only through flagged drug-doses), kept in its rank. 2 candidates, none with an alert.*

| # | Gene | Set | Mean cos |
|---|---|---|---|
| 1 | [[COPS6]] | oxidative phosphorylation | +0.53 |
| 2 | [[API5]] | oxidative phosphorylation | +0.52 |

## + arm (144)

| Gene | Projection | Name |
|---|---|---|
| [[LIN7C]] | 0.888 | lin-7 cell polarity scaffold C |
| [[EIF4H]] | 0.840 | eukaryotic translation initiation factor 4H |
| [[CAPRIN1]] | 0.830 | cell cycle associated protein 1 |
| [[TWF1]] | 0.819 | twinfilin actin binding protein 1 |
| [[UBQLN1]] | 0.816 | ubiquilin 1 |
| [[NONO]] | 0.800 | non-POU domain containing octamer binding |
| [[OCRL]] | 0.792 | OCRL inositol polyphosphate-5-phosphatase |
| [[DCTN1]] | 0.779 | dynactin subunit 1 |
| [[DLD]] | 0.778 | dihydrolipoamide dehydrogenase |
| [[MOB1A]] | 0.778 | MOB kinase activator 1A |
| [[API5]] | 0.775 | apoptosis inhibitor 5 |
| [[NRAS]] | 0.766 | NRAS proto-oncogene, GTPase |
| [[PRELID3B]] | 0.765 | PRELI domain containing 3B |
| [[MBTPS2]] | 0.762 | membrane bound transcription factor peptidase, site 2 |
| [[MANEA]] | 0.754 | mannosidase endo-alpha |
| [[MMGT1]] | 0.752 | membrane magnesium transporter 1 |
| [[COPS6]] | 0.751 | COP9 signalosome subunit 6 |
| [[DPY19L4]] | 0.747 | dpy-19 like 4 |
| [[IPO8]] | 0.745 | importin 8 |
| [[ARPP19]] | 0.742 | cAMP regulated phosphoprotein 19 |
| [[PFKM]] | 0.736 | phosphofructokinase, muscle |
| [[RAD23B]] | 0.735 | RAD23 nucleotide excision repair protein B |
| [[SCCPDH]] | 0.731 | saccharopine dehydrogenase (putative) |
| [[FAM199X]] | 0.730 | family with sequence similarity 199, X-linked |
| [[FECH]] | 0.728 | ferrochelatase |
| [[ALG10B]] | 0.726 | ALG10 alpha-1,2-glucosyltransferase B |
| [[GMFB]] | 0.724 | glia maturation factor beta |
| [[ZNF664]] | 0.723 | zinc finger protein 664 |
| [[SRP9]] | 0.718 | signal recognition particle 9 |
| [[AP2M1]] | 0.717 | adaptor related protein complex 2 subunit mu 1 |
| [[STX16]] | 0.716 | syntaxin 16 |
| [[COX11]] | 0.714 | cytochrome c oxidase copper chaperone COX11 |
| [[GPN1]] | 0.711 | GPN-loop GTPase 1 |
| [[BTBD1]] | 0.706 | BTB domain containing 1 |
| [[ZDHHC21]] | 0.706 | zDHHC palmitoyltransferase 21 |
| [[AKAP11]] | 0.705 | A-kinase anchoring protein 11 |
| [[ZMPSTE24]] | 0.699 | zinc metallopeptidase STE24 |
| [[AP3M1]] | 0.698 | adaptor related protein complex 3 subunit mu 1 |
| [[ERLIN2]] | 0.697 | ER lipid raft associated 2 |
| [[EXOC5]] | 0.696 | exocyst complex component 5 |
| [[SGPL1]] | 0.692 | sphingosine-1-phosphate lyase 1 |
| [[RBBP9]] | 0.688 | RB binding protein 9, serine hydrolase |
| [[DR1]] | 0.684 | down-regulator of transcription 1 |
| [[NELFCD]] | 0.684 | negative elongation factor complex member C/D |
| [[ALG10]] | 0.684 | ALG10 alpha-1,2-glucosyltransferase |
| [[TMEM237]] | 0.684 | transmembrane protein 237 |
| [[TMEM106B]] | 0.681 | transmembrane protein 106B |
| [[NCKAP1]] | 0.678 | NCK associated protein 1 |
| [[TGOLN2]] | 0.677 | trans-golgi network protein 2 |
| [[AGO1]] | 0.673 | argonaute RISC component 1 |
| [[PTGR2]] | 0.672 | prostaglandin reductase 2 |
| [[ATL3]] | 0.664 | atlastin GTPase 3 |
| [[PAPOLA]] | 0.663 | poly(A) polymerase alpha |
| [[TARDBP]] | 0.663 | TAR DNA binding protein |
| [[RCN1]] | 0.662 | reticulocalbin 1 |
| [[HDHD2]] | 0.661 | haloacid dehalogenase like hydrolase domain containing 2 |
| [[PNPO]] | 0.660 | pyridoxamine 5'-phosphate oxidase |
| [[HUWE1]] | 0.660 | HECT, UBA and WWE domain containing E3 ubiquitin protein ligase 1 |
| [[SPTBN1]] | 0.658 | spectrin beta, non-erythrocytic 1 |
| [[DNAJC13]] | 0.658 | DnaJ heat shock protein family (Hsp40) member C13 |
| [[MTMR2]] | 0.655 | myotubularin related protein 2 |
| [[PEX19]] | 0.654 | peroxisomal biogenesis factor 19 |
| [[XRCC6]] | 0.653 | X-ray repair cross complementing 6 |
| [[UHMK1]] | 0.646 | U2AF homology motif kinase 1 |
| [[SNX17]] | 0.646 | sorting nexin 17 |
| [[SGCB]] | 0.643 | sarcoglycan beta |
| [[EIF3C]] | 0.643 | eukaryotic translation initiation factor 3 subunit C |
| [[SZRD1]] | 0.642 | SUZ RNA binding domain containing 1 |
| [[USP39]] | 0.641 | ubiquitin specific peptidase 39 |
| [[UBE2V1]] | 0.640 | ubiquitin conjugating enzyme E2 V1 |
| [[AIFM1]] | 0.640 | apoptosis inducing factor mitochondria associated 1 |
| [[CRYZ]] | 0.636 | crystallin zeta |
| [[SMU1]] | 0.636 | SMU1 DNA replication regulator and spliceosomal factor |
| [[ELMOD2]] | 0.634 | ELMO domain containing 2 |
| [[TMTC3]] | 0.622 | transmembrane O-mannosyltransferase targeting cadherins 3 |
| [[DYNC1H1]] | 0.614 | dynein cytoplasmic 1 heavy chain 1 |
| [[VAMP3]] | 0.612 | vesicle associated membrane protein 3 |
| [[DLST]] | 0.604 | dihydrolipoamide S-succinyltransferase |
| [[BRCC3]] | 0.600 | BRCA1/BRCA2-containing complex subunit 3 |
| [[SSX2IP]] | 0.598 | SSX family member 2 interacting protein |
| [[PLS3]] | 0.598 | plastin 3 |
| [[PFN2]] | 0.597 | profilin 2 |
| [[SYNJ2BP]] | 0.596 | synaptojanin 2 binding protein |
| [[USP5]] | 0.590 | ubiquitin specific peptidase 5 |
| [[DBN1]] | 0.589 | drebrin 1 |
| [[SFT2D2]] | 0.579 | SFT2 domain containing 2 |
| [[FH]] | 0.578 | fumarate hydratase |
| [[C1orf198]] | 0.578 | chromosome 1 open reading frame 198 |
| [[SMG7]] | 0.576 | SMG7 nonsense mediated mRNA decay factor |
| [[SMARCC2]] | 0.574 | SWI/SNF related BAF chromatin remodeling complex subunit C2 |
| [[OPA1]] | 0.573 | OPA1 mitochondrial dynamin like GTPase |
| [[GSR]] | 0.571 | glutathione-disulfide reductase |
| [[LPGAT1]] | 0.569 | lysophosphatidylglycerol acyltransferase 1 |
| [[BMS1P20]] | 0.564 | BMS1 pseudogene 20 |
| [[MFN2]] | 0.564 | mitofusin 2 |
| [[SBDSP1]] | 0.556 | SBDS pseudogene 1 |
| [[ECHS1]] | 0.555 | enoyl-CoA hydratase, short chain 1 |
| [[STMP1]] | 0.553 | short transmembrane mitochondrial protein 1 |
| [[AIDA]] | 0.551 | axin interactor, dorsalization associated |
| [[HTATSF1]] | 0.544 | HIV-1 Tat specific factor 1 |
| [[KAT7]] | 0.544 | lysine acetyltransferase 7 |
| [[MORF4L1]] | 0.541 | mortality factor 4 like 1 |
| [[FUT10]] | 0.540 | protein O-fucosyltransferase 3 |
| [[PHF6]] | 0.539 | PHD finger protein 6 |
| [[ZC3H14]] | 0.526 | zinc finger CCCH-type containing 14 |
| [[HACD2]] | 0.525 | 3-hydroxyacyl-CoA dehydratase 2 |
| [[GPD2]] | 0.520 | glycerol-3-phosphate dehydrogenase 2 |
| [[CNBP]] | 0.520 | CCHC-type zinc finger nucleic acid binding protein |
| [[ERAP1]] | 0.517 | endoplasmic reticulum aminopeptidase 1 |
| [[ARL5A]] | 0.513 | ARF like GTPase 5A |
| [[CEP20]] | 0.511 | centrosomal protein 20 |
| [[SEC22C]] | 0.511 | SEC22 homolog C, vesicle trafficking protein |
| [[ZBTB37]] | 0.511 | zinc finger and BTB domain containing 37 |
| [[VPS36]] | 0.509 | vacuolar protein sorting 36 homolog |
| [[RFX5]] | 0.506 | regulatory factor X5 |
| [[PTAR1]] | 0.503 | protein prenyltransferase alpha subunit repeat containing 1 |
| [[PGM2]] | 0.502 | phosphoglucomutase 2 |
| [[GTF2A1]] | 0.502 | general transcription factor IIA subunit 1 |
| [[TNPO1]] | 0.500 | transportin 1 |
| [[LRRC58]] | 0.499 | leucine rich repeat containing 58 |
| [[SUDS3]] | 0.498 | SIN3A corepressor complex component SDS3 |
| [[TAS2R30]] | 0.497 | taste 2 receptor member 30 |
| [[RAB23]] | 0.497 | RAB23, member RAS oncogene family |
| [[GFM2]] | 0.491 | GTP dependent ribosome recycling factor mitochondrial GFM2 |
| [[MDH1]] | 0.491 | malate dehydrogenase 1 |
| [[PRTFDC1]] | 0.487 | phosphoribosyl transferase domain containing 1 |
| [[TMEM64]] | 0.474 | transmembrane protein 64 |
| [[NORAD]] | 0.463 | non-coding RNA activated by DNA damage |
| [[SNX7]] | 0.461 | sorting nexin 7 |
| [[UBFD1]] | 0.461 | ubiquitin family domain containing 1 |
| [[AZIN1]] | 0.444 | antizyme inhibitor 1 |
| [[POLR2J3]] | 0.413 | RNA polymerase II subunit J3 |
| [[CAND1]] | 0.405 | cullin associated and neddylation dissociated 1 |
| [[MTFR1L]] | 0.398 | mitochondrial fission regulator 1 like |
| [[PHOSPHO2]] | 0.380 | phosphatase, orphan 2 |
| [[APOO]] | 0.372 | apolipoprotein O |
| [[RNF167]] | 0.366 | ring finger protein 167 |
| [[PDHB]] | 0.342 | pyruvate dehydrogenase E1 subunit beta |
| [[GALNT7]] | 0.342 | polypeptide N-acetylgalactosaminyltransferase 7 |
| [[LONRF2]] | 0.333 | LON peptidase N-terminal domain and ring finger 2 |
| [[GXYLT1]] | 0.295 | glucoside xylosyltransferase 1 |
| [[SLAIN2]] | 0.289 | SLAIN family member 2 |
| [[SNAP23]] | 0.199 | synaptosome associated protein 23 |
| [[DANCR]] | 0.162 | differentiation antagonizing non-protein coding RNA |

## − arm (27)

| Gene | Projection | Name |
|---|---|---|
| [[ZBTB7A]] | -0.772 | zinc finger and BTB domain containing 7A |
| [[HIC2]] | -0.670 | HIC ZBTB transcriptional repressor 2 |
| [[ELL]] | -0.666 | elongation factor for RNA polymerase II |
| [[MARCHF9]] | -0.664 | membrane associated ring-CH-type finger 9 |
| [[DTX2P1-UPK3BP1-PMS2P11]] | -0.652 | DTX2P1-UPK3BP1-PMS2P11 readthrough, transcribed pseudogene |
| [[NOSIP]] | -0.607 | nitric oxide synthase interacting protein |
| [[TNRC6C]] | -0.606 | trinucleotide repeat containing adaptor 6C |
| [[SLC25A37]] | -0.602 | solute carrier family 25 member 37 |
| [[PPP1R13L]] | -0.563 | protein phosphatase 1 regulatory subunit 13 like |
| [[RAB11FIP3]] | -0.555 | RAB11 family interacting protein 3 |
| [[LINC02976]] | -0.547 | long independently transcribed non-coding RNA 2976 |
| [[F12]] | -0.533 | coagulation factor XII |
| [[FBXO11]] | -0.530 | F-box protein 11 |
| [[ZNF816-ZNF321P]] | -0.528 | ZNF816-ZNF321P readthrough |
| [[CATSPER2]] | -0.522 | cation channel sperm associated 2 |
| [[MILIP]] | -0.513 | MYC inducible lncRNA inactivating p53 |
| [[ZNF10]] | -0.483 | zinc finger protein 10 |
| [[EGFL8]] | -0.479 | EGF like domain multiple 8 |
| [[SNX8]] | -0.468 | sorting nexin 8 |
| [[SS18L2]] | -0.421 | SS18 like 2 |
| [[RGP1]] | -0.416 | RGP1 partner of RAB6A GEF complex |
| [[FOXC1]] | -0.393 | forkhead box C1 |
| [[SP4]] | -0.390 | Sp4 transcription factor |
| [[BMS1P1]] | -0.379 | BMS1 pseudogene 1 |
| [[KLHL4]] | -0.377 | kelch like family member 4 |
| [[AACS]] | -0.349 | acetoacetyl-CoA synthetase |
| [[GNG5]] | -0.273 | G protein subunit gamma 5 |

## Data

- `graph/nodes.parquet` — module == 25; `graph/modules.parquet` — module == 25; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [24] (drug-dose × line)
