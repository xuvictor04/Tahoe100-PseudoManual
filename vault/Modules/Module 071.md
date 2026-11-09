---
module: 71
type: "module"
n_genes: 70
n_plus: 70
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.25934872031211853
label: "Metabolism of non-coding RNA"
label_source: "reactome"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 071

*Metabolism of non-coding RNA · 70 genes (single-armed) · [[Module 071.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

Label from the validation stage: **Metabolism of non-coding RNA** (reactome, q 0.002; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | Cell Cycle | reactome | 18/70 | 6.37 | 2e-07 |
| + | Cell Cycle | reactome | 18/70 | 6.37 | 2e-07 |
| + | Cell Cycle, Mitotic | reactome | 14/70 | 6.27 | 3e-05 |
| all | Cell Cycle, Mitotic | reactome | 14/70 | 6.27 | 3e-05 |
| all | M Phase | reactome | 10/70 | 6.39 | 0.002 |
| + | M Phase | reactome | 10/70 | 6.39 | 0.002 |
| all | snRNP Assembly | reactome | 5/70 | 20.7 | 0.002 |
| all | Metabolism of non-coding RNA | reactome | 5/70 | 20.7 | 0.002 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 70), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM (+9.4, ⚠ cell-cycle shift); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (+5.6, ⚠ cell-cycle shift); [[Epirubicin (hydrochloride) (drug)]] 5 µM (+4.4, ⚠ cell-cycle shift); [[Topotecan (hydrochloride) (drug)]] 5 µM (+4.0, ⚠ toxic; cell-cycle shift); [[Panobinostat (drug)]] 5 µM (+3.6, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (+3.6, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (+3.0, ⚠ cell-cycle shift); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+2.9); [[Topotecan (hydrochloride) (drug)]] 0.5 µM (+2.7, ⚠ cell-cycle shift); [[Darinaparsin (drug)]] 5 µM (+2.1, ⚠ cell-cycle shift); [[Topotecan (hydrochloride) (drug)]] 0.05 µM (+1.3); [[Irinotecan (hydrochloride) (drug)]] 5 µM (+1.2); [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM (+1.2); [[Epirubicin (hydrochloride) (drug)]] 0.5 µM (+1.2); [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM (+1.1); [[Ponatinib (drug)]] 0.5 µM (+1.1); [[Gemcitabine (drug)]] 0.05 µM (+1.0) (31 in all, 23 with an alert ⚠; shown: the 10 strongest and the 7 next strongest without an alert)
- Lower it: [[Tucidinostat (drug)]] 5 µM (-2.9); [[Homoharringtonine (drug)]] 0.5 µM (-2.8, ⚠ cell-cycle shift); [[Selinexor (drug)]] 0.5 µM (-2.7, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 5 µM (-2.5, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 0.5 µM (-2.2, ⚠ cell-cycle shift); [[palbociclib (drug)]] 0.5 µM (-2.2, ⚠ cell-cycle shift); [[Artesunate (drug)]] 5 µM (-1.8, ⚠ cell-cycle shift); [[Selinexor (drug)]] 0.05 µM (-1.8, ⚠ cell-cycle shift); [[Selinexor (drug)]] 5 µM (-1.8, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (-1.7, ⚠ cell-cycle shift); [[Neratinib (maleate) (drug)]] 5 µM (-1.6); [[palbociclib (drug)]] 5 µM (-1.6); [[Homoharringtonine (drug)]] 0.05 µM (-1.5); [[Pitavastatin (Calcium) (drug)]] 0.5 µM (-1.5); [[Rapamycin (drug)]] 5 µM (-1.4); [[Entrectinib (drug)]] 5 µM (-1.2); [[AZD-8055 (drug)]] 0.5 µM (-1.2); [[Temsirolimus (drug)]] 5 µM (-1.2); [[Niclosamide (olamine) (drug)]] 0.5 µM (-1.1) (29 in all, 16 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[SW480 (line)]], [[HT-29 (line)]], [[Panc 03.27 (line)]], [[NCI-H1792 (line)]], [[CFPAC-1 (line)]], [[PANC-1 (line)]], [[LoVo (line)]], [[MIA PaCa-2 (line)]]

## Candidate new members

*Members not annotated to the set their arm is enriched for, ranked by mean cos to the annotated members (`validation/novel_members.csv`); ⚠ = a reason to doubt the gene's place (in the vector space only through flagged drug-doses), kept in its rank. 23 candidates, none with an alert; shown: the 15 strongest.*

| # | Gene | Set | Mean cos |
|---|---|---|---|
| 1 | [[CENPJ]] | HDR through Homologous Recombination (HRR) | +0.64 |
| 2 | [[C21orf58]] | HDR through Homologous Recombination (HRR) | +0.60 |
| 3 | [[DSN1]] | HDR through Homologous Recombination (HRR) | +0.60 |
| 4 | [[FANCM]] | HDR through Homologous Recombination (HRR) | +0.60 |
| 5 | [[DYRK4]] | HDR through Homologous Recombination (HRR) | +0.59 |
| 6 | [[CENPO]] | IP3 and IP4 transport between cytosol and nucleus | +0.58 |
| 7 | [[HSPA14]] | HDR through Homologous Recombination (HRR) | +0.57 |
| 8 | [[ASF1B]] | HDR through Homologous Recombination (HRR) | +0.56 |
| 9 | [[TOPBP1]] | IP3 and IP4 transport between cytosol and nucleus | +0.56 |
| 10 | [[TRAIP]] | HDR through Homologous Recombination (HRR) | +0.55 |
| 11 | [[GPR19]] | HDR through Homologous Recombination (HRR) | +0.55 |
| 12 | [[LRR1]] | HDR through Homologous Recombination (HRR) | +0.54 |
| 13 | [[RFWD3]] | Metabolism of non-coding RNA | +0.54 |
| 14 | [[MTBP]] | IP3 and IP4 transport between cytosol and nucleus | +0.53 |
| 15 | [[ZNF519]] | IP3 and IP4 transport between cytosol and nucleus | +0.53 |

*⚠ 1 of its 70 genes are in the vector space only through drug-doses that carry an alert (`embed/genes.parquet` evidence_flagged_only): their place here may reflect what those drug-doses did to the cells. They are marked in the tables of this note.*

## + arm (70)

| Gene | Projection | Name | Alert |
|---|---|---|---|
| [[CDCA5]] | 0.917 | cell division cycle associated 5 |  |
| [[CENPO]] | 0.916 | centromere protein O |  |
| [[RFWD3]] | 0.897 | ring finger and WD repeat domain 3 |  |
| [[MTBP]] | 0.870 | MDM2 binding protein |  |
| [[C21orf58]] | 0.864 | chromosome 21 open reading frame 58 |  |
| [[DDIAS]] | 0.851 | DNA damage induced apoptosis suppressor |  |
| [[HAUS8]] | 0.836 | HAUS augmin like complex subunit 8 |  |
| [[FANCM]] | 0.833 | FA complementation group M |  |
| [[LIN9]] | 0.833 | lin-9 DREAM MuvB core complex component |  |
| [[ZNF519]] | 0.828 | zinc finger protein 519 |  |
| [[TOPBP1]] | 0.812 | DNA topoisomerase II binding protein 1 |  |
| [[ASF1B]] | 0.809 | anti-silencing function 1B histone chaperone |  |
| [[LRR1]] | 0.791 | leucine rich repeat protein 1 |  |
| [[TRAIP]] | 0.778 | TRAF interacting protein |  |
| [[EME1]] | 0.750 | essential meiotic structure-specific endonuclease 1 |  |
| [[DBF4B]] | 0.749 | DBF4B-CDC7 kinase regulatory subunit |  |
| [[CENPJ]] | 0.743 | centrosome assembly and centriole elongation protein |  |
| [[ZNF718]] | 0.743 | zinc finger protein 718 |  |
| [[GPR19]] | 0.740 | G protein-coupled receptor 19 |  |
| [[SLF1]] | 0.731 | SMC5/6 complex localization factor 1 |  |
| [[RMI2]] | 0.725 | RecQ mediated genome instability 2 |  |
| [[DSN1]] | 0.722 | DSN1 component of MIS12 kinetochore complex |  |
| [[PPIH]] | 0.715 | peptidylprolyl isomerase H |  |
| [[DYRK4]] | 0.709 | dual specificity tyrosine phosphorylation regulated kinase 4 |  |
| [[HSPA14]] | 0.704 | heat shock protein family A (Hsp70) member 14 |  |
| [[TOP3A]] | 0.693 | DNA topoisomerase III alpha |  |
| [[RAD54B]] | 0.690 | RAD54 homolog B |  |
| [[NUP85]] | 0.684 | nucleoporin 85 |  |
| [[DHRS7B]] | 0.669 | dehydrogenase/reductase 7B |  |
| [[SASS6]] | 0.659 | SAS-6 centriolar assembly protein |  |
| [[C9orf40]] | 0.650 | chromosome 9 open reading frame 40 |  |
| [[DGCR8]] | 0.645 | DGCR8 microprocessor complex subunit |  |
| [[UBL7-DT]] | 0.642 | UBL7 divergent transcript |  |
| [[DONSON]] | 0.639 | DNA replication fork stabilization factor DONSON |  |
| [[XNDC1N]] | 0.636 | XRCC1 N-terminal domain containing 1, N-terminal like |  |
| [[TTI1]] | 0.634 | TELO2 interacting protein 1 |  |
| [[NUP153]] | 0.633 | nucleoporin 153 |  |
| [[DMC1]] | 0.626 | DNA meiotic recombinase 1 |  |
| [[TLCD3B]] | 0.624 | TLC domain containing 3B |  |
| [[LIN52]] | 0.612 | lin-52 DREAM MuvB core complex component |  |
| [[POLE3]] | 0.611 | DNA polymerase epsilon 3, accessory subunit |  |
| [[DNAJC9]] | 0.610 | DnaJ heat shock protein family (Hsp40) member C9 |  |
| [[S100PBP]] | 0.606 | S100P binding protein |  |
| [[NDOR1]] | 0.605 | NADPH dependent diflavin oxidoreductase 1 |  |
| [[ZRANB3]] | 0.603 | zinc finger RANBP2-type containing 3 |  |
| [[SMPD4]] | 0.602 | sphingomyelin phosphodiesterase 4 |  |
| [[ZNF876P]] | 0.592 | zinc finger protein 876, pseudogene |  |
| [[NIF3L1]] | 0.583 | NGG1 interacting factor 3 like 1 |  |
| [[NUP50]] | 0.579 | nucleoporin 50 |  |
| [[MTFR2]] | 0.569 | mitochondrial fission regulator 2 |  |
| [[ZNF850]] | 0.563 | zinc finger protein 850 |  |
| [[SMPD4BP]] | 0.557 | sphingomyelin phosphodiesterase 4B, pseudogene |  |
| [[ASH2L]] | 0.553 | ASH2 like, histone lysine methyltransferase complex subunit |  |
| [[ZNF530]] | 0.545 | zinc finger protein 530 |  |
| [[SUZ12P1]] | 0.541 | SUZ12 pseudogene 1 |  |
| [[RBBP4]] | 0.538 | RB binding protein 4, chromatin remodeling factor |  |
| [[ITGB3BP]] | 0.534 | integrin subunit beta 3 binding protein |  |
| [[ZNF684]] | 0.524 | zinc finger protein 684 |  |
| [[TEX30]] | 0.517 | testis expressed 30 |  |
| [[H2AZ1]] | 0.510 | H2A.Z variant histone 1 |  |
| [[DCAF15]] | 0.503 | DDB1 and CUL4 associated factor 15 |  |
| [[NUP88]] | 0.500 | nucleoporin 88 |  |
| [[SNRPB]] | 0.479 | small nuclear ribonucleoprotein polypeptides B and B1 |  |
| [[PKN3]] | 0.477 | protein kinase N3 |  |
| [[PBX3]] | 0.432 | PBX homeobox 3 |  |
| [[LSM3]] | 0.427 | LSM3 homolog, U6 small nuclear RNA and mRNA degradation associated | ⚠ only flagged evidence |
| [[CCHCR1]] | 0.421 | coiled-coil alpha-helical rod protein 1 |  |
| [[CLIP3]] | -0.415 | CAP-Gly domain containing linker protein 3 |  |
| [[FBXO43]] | 0.396 | F-box protein 43 |  |
| [[FSBP]] | 0.294 | fibrinogen silencer binding protein |  |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 71; `graph/modules.parquet` — module == 71; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [70] (drug-dose × line)
