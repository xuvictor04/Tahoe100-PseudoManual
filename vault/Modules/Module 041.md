---
module: 41
type: "module"
n_genes: 111
n_plus: 102
n_minus: 9
arms_opposite: true
mean_cos_between_arms: -0.30622729659080505
label: "Intra-Golgi and retrograde Golgi-to-ER traffic"
label_source: "reactome"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 041

*Intra-Golgi and retrograde Golgi-to-ER traffic · 111 genes (102 in the + arm, 9 in the − arm) · [[Module 041.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31). The + arm rises where the − arm falls. Arm = the side of the module's main direction a gene sits on.

Label from the validation stage: **Intra-Golgi and retrograde Golgi-to-ER traffic** (reactome, q 3e-06; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | Membrane Trafficking | reactome | 21/111 | 4.97 | 9e-07 |
| + | Membrane Trafficking | reactome | 20/102 | 5.15 | 1e-06 |
| all | Vesicle-mediated transport | reactome | 21/111 | 4.71 | 2e-06 |
| + | Vesicle-mediated transport | reactome | 20/102 | 4.89 | 3e-06 |
| + | Intra-Golgi and retrograde Golgi-to-ER traffic | reactome | 12/102 | 9.59 | 3e-06 |
| all | Intra-Golgi and retrograde Golgi-to-ER traffic | reactome | 12/111 | 8.81 | 9e-06 |
| + | Asparagine N-linked glycosylation | reactome | 12/102 | 6.22 | 3e-04 |
| all | Asparagine N-linked glycosylation | reactome | 12/111 | 5.72 | 7e-04 |

## Drugs that move it

*Mean pooled z of the + arm minus the − arm (`graph/module_pooled_z.npy`, row 40), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it (+ arm up, − arm down): [[Homoharringtonine (drug)]] 5 µM (+11.6, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (+10.0, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (+8.2, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (+7.1, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (+6.9, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (+5.2, ⚠ cell-cycle shift); [[TAK-901 (drug)]] 5 µM (+4.0, ⚠ cell-cycle shift); [[Auranofin (drug)]] 5 µM (+4.0); [[Topotecan (hydrochloride) (drug)]] 5 µM (+3.6, ⚠ toxic; cell-cycle shift); [[Artesunate (drug)]] 5 µM (+3.5, ⚠ cell-cycle shift); [[Terfenadine (drug)]] 5 µM (+3.0); [[Niclosamide (olamine) (drug)]] 0.5 µM (+2.7); [[Fluvoxamine (maleate) (drug)]] 5 µM (+2.6); [[Vilanterol (drug)]] 5 µM (+2.5); [[Docetaxel (Trihydrate) (drug)]] 0.5 µM (+2.1); [[Triamcinolone (drug)]] 5 µM (+2.1); [[Fluvoxamine (maleate) (drug)]] 0.5 µM (+2.0); [[Cloxacillin (sodium) (drug)]] 0.05 µM (+2.0); [[Pasireotide (acetate) (drug)]] 5 µM (+2.0) (130 in all, 24 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)
- Lower it: [[Niclosamide (olamine) (drug)]] 5 µM (-4.8, ⚠ toxic; cell-cycle shift); [[Belumosudil (drug)]] 5 µM (-4.6); [[Dinaciclib (drug)]] 5 µM (-4.4, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (-4.1, ⚠ toxic; transcription drop; cell-cycle shift); [[Digitoxin (drug)]] 0.5 µM (-4.1, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (-3.9); [[Dinaciclib (drug)]] 0.5 µM (-3.8, ⚠ toxic; transcription drop; cell-cycle shift); [[Temsirolimus (drug)]] 0.05 µM (-3.3); [[Berbamine (drug)]] 0.05 µM (-3.3); [[Retinoic acid (drug)]] 0.05 µM (-3.3); [[Busulfan (drug)]] 0.05 µM (-3.2); [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM (-3.1); [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM (-3.0); [[Palmatine (chloride) (drug)]] 0.05 µM (-2.8); [[TAK-901 (drug)]] 0.05 µM (-2.8) (149 in all, 23 with an alert ⚠; shown: the 10 strongest and the 5 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[MIA PaCa-2 (line)]], [[SW480 (line)]], [[PANC-1 (line)]], [[HEC-1-A (line)]], [[NCI-H460 (line)]], [[LOX-IMVI (line)]], [[NCI-H23 (line)]], [[RKO (line)]]

## Candidate new members

*Members not annotated to the set their arm is enriched for, ranked by mean cos to the annotated members (`validation/novel_members.csv`); ⚠ = a reason to doubt the gene's place (in the vector space only through flagged drug-doses), kept in its rank. 24 candidates, none with an alert; shown: the 15 strongest.*

| # | Gene | Set | Mean cos |
|---|---|---|---|
| 1 | [[OSBP]] | ER to Golgi Anterograde Transport | +0.66 |
| 2 | [[SPTY2D1]] | ER to Golgi Anterograde Transport | +0.65 |
| 3 | [[ACBD3]] | ER to Golgi Anterograde Transport | +0.63 |
| 4 | [[GOLGA2]] | Intra-Golgi and retrograde Golgi-to-ER traffic | +0.63 |
| 5 | [[SRP54]] | ER to Golgi Anterograde Transport | +0.63 |
| 6 | [[RAB5A]] | ER to Golgi Anterograde Transport | +0.63 |
| 7 | [[ARFIP2]] | ER to Golgi Anterograde Transport | +0.61 |
| 8 | [[YIPF5]] | ER to Golgi Anterograde Transport | +0.60 |
| 9 | [[TMF1]] | ER to Golgi Anterograde Transport | +0.59 |
| 10 | [[TBC1D23]] | ER to Golgi Anterograde Transport | +0.59 |
| 11 | [[DIS3]] | ER to Golgi Anterograde Transport | +0.57 |
| 12 | [[LYSMD3]] | ER to Golgi Anterograde Transport | +0.57 |
| 13 | [[GOLGA5]] | ER to Golgi Anterograde Transport | +0.57 |
| 14 | [[COQ10B]] | ER to Golgi Anterograde Transport | +0.54 |
| 15 | [[AKAP17A]] | ER to Golgi Anterograde Transport | +0.53 |

## + arm (102)

| Gene | Projection | Name |
|---|---|---|
| [[GOLGA2]] | 0.877 | golgin A2 |
| [[SPTY2D1]] | 0.874 | SPT2 chromatin protein domain containing 1 |
| [[SRP54]] | 0.867 | signal recognition particle 54 |
| [[ACBD3]] | 0.861 | acyl-CoA binding domain containing 3 |
| [[OSBP]] | 0.833 | oxysterol binding protein |
| [[TMF1]] | 0.831 | TATA element modulatory factor 1 |
| [[GOLGA5]] | 0.828 | golgin A5 |
| [[YIPF5]] | 0.826 | Yip1 domain family member 5 |
| [[TBC1D23]] | 0.818 | TBC1 domain family member 23 |
| [[UFL1]] | 0.803 | UFM1 specific ligase 1 |
| [[ERCC5]] | 0.785 | ERCC excision repair 5, endonuclease |
| [[PPIL4]] | 0.775 | peptidylprolyl isomerase like 4 |
| [[AKAP17A]] | 0.773 | A-kinase anchoring protein 17A |
| [[DIS3]] | 0.773 | DIS3 exosome endoribonuclease and 3'-5' exoribonuclease |
| [[RAB5A]] | 0.752 | RAB5A, member RAS oncogene family |
| [[GOLPH3L]] | 0.742 | golgi phosphoprotein 3 like |
| [[ZRSR2]] | 0.736 | zinc finger CCCH-type, RNA binding motif and serine/arginine rich 2 |
| [[KLC4]] | 0.734 | kinesin light chain 4 |
| [[SEC22A]] | 0.723 | SEC22 homolog A, vesicle trafficking protein |
| [[LYSMD3]] | 0.723 | LysM domain containing 3 |
| [[BUD31]] | 0.721 | BUD31 spliceosome associated protein |
| [[MMUT]] | 0.720 | methylmalonyl-CoA mutase |
| [[KLHL28]] | 0.720 | kelch like family member 28 |
| [[COPE]] | 0.716 | coat protein complex I subunit epsilon |
| [[MYNN]] | 0.712 | myoneurin |
| [[MINDY2]] | 0.710 | MINDY lysine 48 deubiquitinase 2 |
| [[ARFIP2]] | 0.707 | ARF interacting protein 2 |
| [[ESCO1]] | 0.706 | establishment of sister chromatid cohesion N-acetyltransferase 1 |
| [[ZMYM6]] | 0.706 | zinc finger MYM-type containing 6 |
| [[OSBPL2]] | 0.697 | oxysterol binding protein like 2 |
| [[STX5-DT]] | 0.695 | STX5 divergent transcript |
| [[SAFB2]] | 0.690 | scaffold attachment factor B2 |
| [[ARF4]] | 0.681 | ARF GTPase 4 |
| [[ZSWIM8]] | 0.667 | zinc finger SWIM-type containing 8 |
| [[GOLGA4]] | 0.666 | golgin A4 |
| [[COQ10B]] | 0.666 | coenzyme Q10B |
| [[COG1]] | 0.663 | component of oligomeric golgi complex 1 |
| [[CCDC9]] | 0.659 | coiled-coil domain containing 9 |
| [[CDK7]] | 0.658 | cyclin dependent kinase 7 |
| [[FAM177A1]] | 0.654 | family with sequence similarity 177 member A1 |
| [[FAM161B]] | 0.652 | FAM161 centrosomal protein B |
| [[ZNF550]] | 0.652 | zinc finger protein 550 |
| [[SCFD1]] | 0.650 | sec1 family domain containing 1 |
| [[SEC23IP]] | 0.647 | SEC23 interacting protein |
| [[SDE2]] | 0.644 | spliceosome associated SDE2 |
| [[LTN1]] | 0.635 | listerin E3 ubiquitin protein ligase 1 |
| [[CFAP36]] | 0.627 | cilia and flagella associated protein 36 |
| [[TVP23B]] | 0.627 | trans-golgi network vesicle protein 23 homolog B |
| [[TXNL4B]] | 0.626 | thioredoxin like 4B |
| [[SENP2]] | 0.624 | SUMO specific peptidase 2 |
| [[PEX13]] | 0.620 | peroxisomal biogenesis factor 13 |
| [[TGDS]] | 0.608 | TDP-glucose 4,6-dehydratase |
| [[MED6]] | 0.606 | mediator complex subunit 6 |
| [[UFSP2]] | 0.606 | UFM1 specific peptidase 2 |
| [[RNF185]] | 0.605 | ring finger protein 185 |
| [[SF3B2]] | 0.598 | splicing factor 3b subunit 2 |
| [[STX5]] | 0.596 | syntaxin 5 |
| [[JMJD6]] | 0.596 | jumonji domain containing 6, arginine demethylase and lysine hydroxylase |
| [[SUPT5H]] | 0.584 | SPT5 homolog, DSIF elongation factor subunit |
| [[STK19]] | 0.582 | winged helix repair factor 1 |
| [[NAGK]] | 0.578 | N-acetylglucosamine kinase |
| [[RAB33B]] | 0.577 | RAB33B, member RAS oncogene family |
| [[CCNK]] | 0.566 | cyclin K |
| [[BBOF1]] | 0.565 | basal body orientation factor 1 |
| [[ISY1]] | 0.561 | ISY1 spliceosome associated protein |
| [[RBBP5]] | 0.559 | RB binding protein 5, histone lysine methyltransferase complex subunit |
| [[ZNF805]] | 0.559 | zinc finger protein 805 |
| [[ALG11]] | 0.555 | ALG11 alpha-1,2-mannosyltransferase |
| [[EBLN3P]] | 0.555 | endogenous Bornavirus like nucleoprotein 3, pseudogene |
| [[DAD1]] | 0.553 | defender against cell death 1 |
| [[TMEM167B]] | 0.551 | transmembrane protein 167B |
| [[ODR4]] | 0.548 | odr-4 GPCR localization factor homolog |
| [[KIAA0319L]] | 0.540 | KIAA0319 like |
| [[BLZF1]] | 0.539 | basic leucine zipper nuclear factor 1 |
| [[KCNK6]] | 0.537 | potassium two pore domain channel subfamily K member 6 |
| [[XRRA1]] | 0.524 | X-ray radiation resistance associated 1 |
| [[TSPYL2]] | 0.523 | TSPY like 2 |
| [[PARP16]] | 0.521 | poly(ADP-ribose) polymerase family member 16 |
| [[ALDH6A1]] | 0.512 | aldehyde dehydrogenase 6 family member A1 |
| [[SNIP1]] | 0.510 | Smad nuclear interacting protein 1 |
| [[SNAP29]] | 0.492 | synaptosome associated protein 29 |
| [[FAM220A]] | 0.492 | family with sequence similarity 220 member A |
| [[RABGEF1]] | 0.458 | RAB guanine nucleotide exchange factor 1 |
| [[ING4]] | 0.452 | inhibitor of growth family member 4 |
| [[ZNF652]] | 0.444 | zinc finger protein 652 |
| [[NKTR]] | 0.433 | natural killer cell triggering receptor |
| [[MFF]] | 0.431 | mitochondrial fission factor |
| [[ZZEF1]] | 0.429 | zinc finger ZZ-type and EF-hand domain containing 1 |
| [[MGRN1]] | 0.424 | mahogunin ring finger 1 |
| [[ZBTB41]] | 0.414 | zinc finger and BTB domain containing 41 |
| [[PRPF38A]] | 0.403 | pre-mRNA processing factor 38A |
| [[MAGED2]] | 0.403 | MAGE family member D2 |
| [[KIF16B]] | 0.395 | kinesin family member 16B |
| [[ARV1]] | 0.383 | ARV1 fatty acid homeostasis modulator |
| [[ARL2BP]] | 0.381 | ARF like GTPase 2 binding protein |
| [[NMD3]] | 0.371 | NMD3 ribosome export adaptor |
| [[ZBTB5]] | 0.348 | zinc finger and BTB domain containing 5 |
| [[MNT]] | 0.344 | MAX network transcriptional repressor |
| [[MAGED1]] | 0.320 | MAGE family member D1 |
| [[SERTAD3]] | 0.220 | SERTA domain containing 3 |
| [[VPS4B]] | 0.184 | vacuolar protein sorting 4 homolog B |
| [[PRKAR2A]] | 0.142 | protein kinase cAMP-dependent type II regulatory subunit alpha |

## − arm (9)

| Gene | Projection | Name |
|---|---|---|
| [[UBE2E3]] | -0.621 | ubiquitin conjugating enzyme E2 E3 |
| [[CHN1]] | -0.613 | chimerin 1 |
| [[PTK2]] | -0.560 | protein tyrosine kinase 2 |
| [[ABCC1]] | -0.540 | ATP binding cassette subfamily C member 1 (ABCC1 blood group) |
| [[LINC00342]] | -0.524 | long independently transcribed non-coding RNA 342 |
| [[APPAT]] | -0.509 | atherosclerotic plaque pathogenesis associated transcript |
| [[CUEDC1]] | -0.506 | CUE domain containing 1 |
| [[SMAD2]] | -0.478 | SMAD family member 2 |
| [[CHML]] | -0.427 | CHM like Rab escort protein |

## Data

- `graph/nodes.parquet` — module == 41; `graph/modules.parquet` — module == 41; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [40] (drug-dose × line)
