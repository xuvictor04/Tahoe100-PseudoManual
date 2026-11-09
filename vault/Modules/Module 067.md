---
module: 67
type: "module"
n_genes: 73
n_plus: 73
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: "E2F targets"
label_source: "hallmark"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 067

*E2F targets · 73 genes (single-armed) · [[Module 067.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

Label from the validation stage: **E2F targets** (hallmark, q 2e-07; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | Cell Cycle | reactome | 19/73 | 6.44 | 6e-08 |
| + | Cell Cycle | reactome | 19/73 | 6.44 | 6e-08 |
| + | E2F targets | hallmark | 12/73 | 12.4 | 2e-07 |
| all | E2F targets | hallmark | 12/73 | 12.4 | 2e-07 |
| all | Cell Cycle, Mitotic | reactome | 14/73 | 6.01 | 4e-05 |
| + | Cell Cycle, Mitotic | reactome | 14/73 | 6.01 | 4e-05 |
| + | G2/M checkpoint | hallmark | 9/73 | 9.39 | 3e-04 |
| all | G2/M checkpoint | hallmark | 9/73 | 9.39 | 3e-04 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 66), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Belinostat (drug)]] 5 µM (+3.9, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (+3.7, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 5 µM (+3.2, ⚠ toxic; transcription drop; cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (+3.0, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 0.05 µM (+2.7, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (+2.7, ⚠ cell-cycle shift); [[Darinaparsin (drug)]] 5 µM (+2.6, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 0.05 µM (+2.5, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (+2.5, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (+2.2, ⚠ toxic; transcription drop; cell-cycle shift); [[HI-TOPK-032 (drug)]] 5 µM (+1.5); [[HI-TOPK-032 (drug)]] 0.05 µM (+1.4); [[Brivudine (drug)]] 5 µM (+1.4); [[Mebendazole (drug)]] 0.5 µM (+1.3); [[Flumatinib (mesylate) (drug)]] 5 µM (+1.1); [[Retinoic acid (drug)]] 0.05 µM (+1.1); [[Tofacitinib (drug)]] 0.5 µM (+1.1); [[Radotinib (drug)]] 5 µM (+1.1); [[8-Hydroxyquinoline (drug)]] 5 µM (+1.0) (31 in all, 22 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)
- Lower it: [[Homoharringtonine (drug)]] 0.5 µM (-6.2, ⚠ cell-cycle shift); [[Selinexor (drug)]] 5 µM (-6.0, ⚠ cell-cycle shift); [[Selinexor (drug)]] 0.5 µM (-5.0, ⚠ cell-cycle shift); [[Auranofin (drug)]] 5 µM (-4.4); [[Homoharringtonine (drug)]] 5 µM (-4.0, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (-3.7, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.05 µM (-3.4); [[Bortezomib (drug)]] 0.05 µM (-3.2, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-2.9, ⚠ cell-cycle shift); [[Selinexor (drug)]] 0.05 µM (-2.8, ⚠ cell-cycle shift); [[Neratinib (maleate) (drug)]] 5 µM (-2.5); [[palbociclib (drug)]] 5 µM (-1.8); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (-1.8); [[Belumosudil (drug)]] 5 µM (-1.8); [[Rapamycin (drug)]] 5 µM (-1.8); [[Temsirolimus (drug)]] 5 µM (-1.6); [[Lactate (calcium) (drug)]] 0.5 µM (-1.5); [[EX229 (drug)]] 5 µM (-1.5) (48 in all, 21 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[A498 (line)]], [[A-427 (line)]], [[SW480 (line)]], [[MIA PaCa-2 (line)]], [[H4 (line)]], [[LS 180 (line)]], [[NCI-H460 (line)]], [[A-172 (line)]]

## Candidate new members

*Members not annotated to the set their arm is enriched for, ranked by mean cos to the annotated members (`validation/novel_members.csv`); ⚠ = a reason to doubt the gene's place (in the vector space only through flagged drug-doses), kept in its rank. 63 candidates, 1 with an alert ⚠; shown: the 15 strongest.*

| # | Gene | Set | Mean cos | Alert |
|---|---|---|---|---|
| 1 | [[PBK]] | E2F targets | +0.82 |  |
| 2 | [[SPC25]] | G2/M checkpoint | +0.82 |  |
| 3 | [[CIT]] | G2/M checkpoint | +0.82 |  |
| 4 | [[STIL]] | E2F targets | +0.81 |  |
| 5 | [[KIFC1]] | E2F targets | +0.81 |  |
| 6 | [[CDCA3]] | G2/M checkpoint | +0.80 |  |
| 7 | [[NEIL3]] | E2F targets | +0.80 |  |
| 8 | [[TICRR]] | E2F targets | +0.79 |  |
| 9 | [[SPAG5]] | G2/M checkpoint | +0.79 |  |
| 10 | [[PARPBP]] | E2F targets | +0.79 |  |
| 11 | [[CENPI]] | E2F targets | +0.78 |  |
| 12 | [[SPC24]] | G2/M checkpoint | +0.78 |  |
| 13 | [[KIF22]] | Mitotic Prometaphase | +0.78 |  |
| 14 | [[UBE2T]] | G2/M checkpoint | +0.78 |  |
| 15 | [[OIP5]] | E2F targets | +0.77 |  |

*⚠ 1 of its 73 genes are in the vector space only through drug-doses that carry an alert (`embed/genes.parquet` evidence_flagged_only): their place here may reflect what those drug-doses did to the cells. They are marked in the tables of this note.*

## + arm (73)

| Gene | Projection | Name | Alert |
|---|---|---|---|
| [[PBK]] | 0.937 | PDZ binding kinase |  |
| [[CIT]] | 0.936 | citron rho-interacting serine/threonine kinase |  |
| [[KIF22]] | 0.932 | kinesin family member 22 |  |
| [[AURKB]] | 0.924 | aurora kinase B |  |
| [[CDCA3]] | 0.911 | cell division cycle associated 3 |  |
| [[STIL]] | 0.910 | STIL centriolar assembly protein |  |
| [[PARPBP]] | 0.910 | PARP1 binding protein |  |
| [[SPC25]] | 0.903 | SPC25 component of NDC80 kinetochore complex |  |
| [[NEIL3]] | 0.902 | nei like DNA glycosylase 3 |  |
| [[KIFC1]] | 0.901 | kinesin family member C1 |  |
| [[SPAG5]] | 0.895 | sperm associated antigen 5 |  |
| [[CENPI]] | 0.895 | centromere protein I |  |
| [[UBE2T]] | 0.892 | ubiquitin conjugating enzyme E2 T |  |
| [[SPC24]] | 0.891 | SPC24 component of NDC80 kinetochore complex |  |
| [[TICRR]] | 0.891 | TOPBP1 interacting checkpoint and replication regulator |  |
| [[OIP5]] | 0.879 | Opa interacting protein 5 |  |
| [[TTK]] | 0.879 | TTK protein kinase |  |
| [[BARD1]] | 0.867 | BRCA1 associated RING domain 1 |  |
| [[NUF2]] | 0.864 | NUF2 component of NDC80 kinetochore complex |  |
| [[KIF18B]] | 0.863 | kinesin family member 18B |  |
| [[POC1A]] | 0.836 | POC1 centriolar protein A |  |
| [[MPHOSPH9]] | 0.835 | M-phase phosphoprotein 9 |  |
| [[CEP152]] | 0.834 | centrosomal protein 152 |  |
| [[DTYMK]] | 0.833 | deoxythymidylate kinase |  |
| [[MIS18BP1]] | 0.830 | MIS18 binding protein 1 |  |
| [[IQGAP3]] | 0.820 | IQ motif containing GTPase activating protein 3 |  |
| [[ARHGAP11B]] | 0.812 | Rho GTPase activating protein 11B |  |
| [[WDR62]] | 0.809 | WD repeat domain 62 |  |
| [[CEP85]] | 0.793 | centrosomal protein 85 |  |
| [[CKS1B]] | 0.781 | CDC28 protein kinase regulatory subunit 1B |  |
| [[NEURL1B]] | 0.749 | neuralized E3 ubiquitin protein ligase 1B |  |
| [[CEP192]] | 0.749 | centrosomal protein 192 |  |
| [[CDCA4]] | 0.736 | cell division cycle associated 4 |  |
| [[NSD2]] | 0.734 | nuclear receptor binding SET domain protein 2 |  |
| [[CEP57L1]] | 0.723 | centrosomal protein 57 like 1 |  |
| [[CENPW]] | 0.716 | centromere protein W |  |
| [[NUDT1]] | 0.713 | nudix hydrolase 1 |  |
| [[CMC2]] | 0.711 | C-X9-C motif containing 2 |  |
| [[SCML2]] | 0.694 | Scm polycomb group protein like 2 |  |
| [[GMNN]] | 0.694 | geminin DNA replication inhibitor |  |
| [[EFCAB11]] | 0.692 | EF-hand calcium binding domain 11 |  |
| [[CTDSPL2]] | 0.690 | CTD small phosphatase like 2 |  |
| [[SUGP2]] | 0.668 | SURP and G-patch domain containing 2 |  |
| [[IFT122]] | 0.662 | intraflagellar transport 122 |  |
| [[THSD4-AS1]] | 0.658 | THSD4 antisense RNA 1 |  |
| [[CHEK2]] | 0.657 | checkpoint kinase 2 |  |
| [[TDP1]] | 0.645 | tyrosyl-DNA phosphodiesterase 1 |  |
| [[RGS3]] | 0.644 | regulator of G protein signaling 3 |  |
| [[RCCD1]] | 0.641 | RCC1 domain containing 1 |  |
| [[SLC25A40]] | 0.639 | solute carrier family 25 member 40 |  |
| [[CCDC77]] | 0.637 | coiled-coil domain containing 77 |  |
| [[CEP43]] | 0.627 | centrosomal protein 43 |  |
| [[ARHGAP33]] | 0.626 | Rho GTPase activating protein 33 |  |
| [[NRM]] | 0.621 | nurim |  |
| [[CEP97]] | 0.609 | centrosomal protein 97 |  |
| [[GGH]] | 0.608 | gamma-glutamyl hydrolase |  |
| [[PHTF2]] | 0.604 | putative homeodomain transcription factor 2 |  |
| [[LIN54]] | 0.602 | lin-54 DREAM MuvB core complex component |  |
| [[CBX3]] | 0.588 | chromobox 3 |  |
| [[ATL2]] | 0.586 | atlastin GTPase 2 |  |
| [[NMU]] | 0.563 | neuromedin U |  |
| [[HMGB1P5]] | 0.560 | high mobility group box 1 pseudogene 5 | ⚠ only flagged evidence |
| [[RTKN2]] | 0.541 | rhotekin 2 |  |
| [[STAG3L5P-1]] | 0.530 | — |  |
| [[PPP2R3B]] | 0.528 | protein phosphatase 2 regulatory subunit B''beta |  |
| [[FBLN1]] | 0.514 | fibulin 1 |  |
| [[MAZ]] | 0.512 | MYC associated zinc finger protein |  |
| [[CCDC34]] | 0.481 | coiled-coil domain containing 34 |  |
| [[CNTROB]] | 0.481 | centrobin, centriole duplication and spindle assembly protein |  |
| [[HERC2P10]] | 0.445 | HERC2 pseudogene 10 |  |
| [[SAMD1]] | 0.391 | sterile alpha motif domain containing 1 |  |
| [[IVD]] | 0.379 | isovaleryl-CoA dehydrogenase |  |
| [[ATP8B3]] | 0.330 | ATPase phospholipid transporting 8B3 |  |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 67; `graph/modules.parquet` — module == 67; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [66] (drug-dose × line)
