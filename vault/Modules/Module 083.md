---
module: 83
type: "module"
n_genes: 53
n_plus: 34
n_minus: 19
arms_opposite: true
mean_cos_between_arms: -0.4041532278060913
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 083

*53 genes (34 in the + arm, 19 in the − arm) · [[Module 083.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40). The + arm rises where the − arm falls. Arm = the side of the module's main direction a gene sits on.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of the + arm minus the − arm (`graph/module_pooled_z.npy`, row 82), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it (+ arm up, − arm down): [[Idarubicin (hydrochloride) (drug)]] 5 µM (+19.8, ⚠ cell-cycle shift); [[Auranofin (drug)]] 5 µM (+11.6); [[Homoharringtonine (drug)]] 5 µM (+11.5, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (+10.8, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+8.3, ⚠ toxic; transcription drop; cell-cycle shift); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+7.7); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (+7.6, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (+7.0, ⚠ toxic; transcription drop; cell-cycle shift); [[Topotecan (hydrochloride) (drug)]] 5 µM (+6.7, ⚠ toxic; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (+6.3, ⚠ toxic; transcription drop; cell-cycle shift); [[Homoharringtonine (drug)]] 0.05 µM (+4.4); [[5-Azacytidine (drug)]] 5 µM (+3.1); [[TAK-901 (drug)]] 0.05 µM (+2.9); [[PH-797804 (drug)]] 5 µM (+2.8); [[Filgotinib (drug)]] 5 µM (+2.7); [[c-Kit-IN-1 (drug)]] 5 µM (+2.3); [[Harringtonine (drug)]] 0.05 µM (+2.2); [[EX229 (drug)]] 5 µM (+1.9) (68 in all, 32 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)
- Lower it: [[Panobinostat (drug)]] 5 µM (-16.3, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (-15.6, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (-15.0, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (-11.5); [[Panobinostat (drug)]] 0.05 µM (-11.5, ⚠ cell-cycle shift); [[Belinostat (drug)]] 0.5 µM (-7.1, ⚠ cell-cycle shift); [[Brivudine (drug)]] 5 µM (-6.8); [[Tucidinostat (drug)]] 0.5 µM (-6.8, ⚠ cell-cycle shift); [[Radotinib (drug)]] 5 µM (-3.0); [[Niclosamide (olamine) (drug)]] 5 µM (-2.8, ⚠ toxic; cell-cycle shift); [[Tucidinostat (drug)]] 0.05 µM (-2.1); [[Brivudine (drug)]] 0.5 µM (-1.9); [[HI-TOPK-032 (drug)]] 5 µM (-1.9); [[Verteporfin (drug)]] 5 µM (-1.8); [[Dimethyl fumarate (drug)]] 5 µM (-1.7); [[Binimetinib (drug)]] 5 µM (-1.5); [[HI-TOPK-032 (drug)]] 0.05 µM (-1.4) (48 in all, 12 with an alert ⚠; shown: the 10 strongest and the 7 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[PANC-1 (line)]], [[NCI-H460 (line)]], [[SW480 (line)]], [[HOP62 (line)]], [[LOX-IMVI (line)]], [[NCI-H23 (line)]], [[LoVo (line)]], [[NCI-H1792 (line)]]

## + arm (34)

| Gene | Projection | Name |
|---|---|---|
| [[SMIM15-AS1]] | 0.900 | SMIM15 antisense RNA 1 |
| [[PCBP1-AS1]] | 0.887 | PCBP1 antisense RNA 1 |
| [[CSTF3]] | 0.833 | cleavage stimulation factor subunit 3 |
| [[GLIPR1-AS1]] | 0.827 | GLIPR1 antisense RNA 1 |
| [[ACAD9]] | 0.788 | acyl-CoA dehydrogenase family member 9 |
| [[LINC01134]] | 0.780 | long independently transcribed non-coding RNA 1134 |
| [[UBE2D3-AS1]] | 0.776 | UBE2D3 antisense RNA 1 |
| [[ZNF621]] | 0.773 | zinc finger protein 621 |
| [[SNAPC5]] | 0.758 | small nuclear RNA activating complex polypeptide 5 |
| [[ZNF546]] | 0.750 | zinc finger protein 546 |
| [[DNAAF10]] | 0.744 | dynein axonemal assembly factor 10 |
| [[MPDU1]] | 0.743 | mannose-P-dolichol utilization defect 1 |
| [[LTO1]] | 0.739 | LTO1 maturation factor of ABCE1 |
| [[PSMD6-AS1]] | 0.720 | PSMD6 antisense RNA 1 |
| [[EXOSC3]] | 0.706 | exosome component 3 |
| [[TEX22]] | 0.701 | testis expressed 22 |
| [[SECISBP2]] | 0.697 | SECIS binding protein 2 |
| [[CENPL]] | 0.683 | centromere protein L |
| [[MAEA]] | 0.682 | macrophage erythroblast attacher, E3 ubiquitin ligase |
| [[DNAJB14]] | 0.671 | DnaJ heat shock protein family (Hsp40) member B14 |
| [[ZNF26]] | 0.668 | zinc finger protein 26 |
| [[ZNF577]] | 0.667 | zinc finger protein 577 |
| [[CHMP3]] | 0.663 | charged multivesicular body protein 3 |
| [[PTCD1]] | 0.662 | pentatricopeptide repeat domain 1 |
| [[PSKH1]] | 0.661 | protein serine kinase H1 |
| [[SPART-AS1]] | 0.639 | SPART antisense RNA 1 |
| [[MIRLET7A1HG]] | 0.631 | miRlet-7a-1/let-7f-1/let-7d cluster host gene |
| [[WDR74]] | 0.618 | WD repeat domain 74 |
| [[RABL3]] | 0.569 | RAB, member of RAS oncogene family like 3 |
| [[PPP4R3B]] | 0.541 | protein phosphatase 4 regulatory subunit 3B |
| [[PDCD6P1]] | 0.498 | PDCD6 pseudogene 1 |
| [[HAUS2]] | 0.456 | HAUS augmin like complex subunit 2 |
| [[MIR30DHG]] | 0.366 | — |
| [[TRMT10A]] | 0.285 | tRNA methyltransferase 10A |

## − arm (19)

| Gene | Projection | Name |
|---|---|---|
| [[PAFAH1B3]] | -0.804 | platelet activating factor acetylhydrolase 1b catalytic subunit 3 |
| [[ARRB2]] | -0.767 | arrestin beta 2 |
| [[USP2]] | -0.744 | ubiquitin specific peptidase 2 |
| [[TUBG2]] | -0.713 | tubulin gamma 2 |
| [[KCTD17]] | -0.701 | potassium channel tetramerization domain containing 17 |
| [[FAM102B]] | -0.692 | EEIG family member 2 |
| [[CDC14B]] | -0.691 | cell division cycle 14B |
| [[NOS1AP]] | -0.687 | nitric oxide synthase 1 adaptor protein |
| [[RADX]] | -0.684 | RPA1 related single stranded DNA binding protein, X-linked |
| [[GUSBP18]] | -0.671 | GUSB pseudogene 18 |
| [[RALGAPA2]] | -0.663 | Ral GTPase activating protein catalytic subunit alpha 2 |
| [[STARD5]] | -0.575 | StAR related lipid transfer domain containing 5 |
| [[VWA1]] | -0.563 | von Willebrand factor A domain containing 1 |
| [[AFDN]] | -0.559 | afadin, adherens junction formation factor |
| [[MLF1]] | -0.553 | myeloid leukemia factor 1 |
| [[HERC1]] | -0.548 | HECT and RLD domain containing E3 ubiquitin protein ligase family member 1 |
| [[NUP62CL]] | -0.518 | nucleoporin 62 C-terminal like |
| [[TPST1]] | -0.487 | tyrosylprotein sulfotransferase 1 |
| [[C1QTNF3-AMACR]] | -0.384 | C1QTNF3-AMACR readthrough (NMD candidate) |

## Data

- `graph/nodes.parquet` — module == 83; `graph/modules.parquet` — module == 83; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [82] (drug-dose × line)
