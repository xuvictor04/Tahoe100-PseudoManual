---
module: 98
type: "module"
n_genes: 48
n_plus: 48
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 098

*48 genes (single-armed) · [[Module 098.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 97), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Clobetasol propionate (drug)]] 0.05 µM (+6.4); [[Idarubicin (hydrochloride) (drug)]] 5 µM (+6.3, ⚠ cell-cycle shift); [[Budesonide (drug)]] 0.5 µM (+6.0); [[Clobetasol propionate (drug)]] 0.5 µM (+5.9); [[Betamethasone dipropionate (drug)]] 0.5 µM (+5.5); [[Budesonide (drug)]] 0.05 µM (+5.4); [[Homoharringtonine (drug)]] 5 µM (+5.4, ⚠ cell-cycle shift); [[Betamethasone dipropionate (drug)]] 0.05 µM (+5.0); [[Triamcinolone (drug)]] 5 µM (+4.9); [[Triamcinolone (drug)]] 0.5 µM (+4.8); [[Betamethasone dipropionate (drug)]] 5 µM (+4.8); [[Budesonide (drug)]] 5 µM (+4.6) (45 in all, 16 with an alert ⚠; shown: the 10 strongest and the 2 next strongest without an alert)
- Lower it: [[Panobinostat (drug)]] 0.5 µM (-3.2, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (-3.2, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (-2.4, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (-1.4, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 0.5 µM (-1.4, ⚠ cell-cycle shift); [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM (-1.3); [[Digitoxin (drug)]] 0.05 µM (-1.2, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (-1.1, ⚠ cell-cycle shift) (8 in all, 7 with an alert ⚠)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[HOP62 (line)]], [[A498 (line)]], [[Hs 766T (line)]], [[NCI-H1573 (line)]], [[AsPC-1 (line)]], [[HS-578T (line)]], [[CFPAC-1 (line)]], [[SNU-423 (line)]]

## + arm (48)

| Gene | Projection | Name |
|---|---|---|
| [[VSTM2L]] | 0.850 | V-set and transmembrane domain containing 2 like |
| [[MAOA]] | 0.833 | monoamine oxidase A |
| [[FKBP5]] | 0.829 | FKBP prolyl isomerase 5 |
| [[KLF9]] | 0.819 | KLF transcription factor 9 |
| [[TLR2]] | 0.778 | toll like receptor 2 |
| [[ADGRG2]] | 0.775 | adhesion G protein-coupled receptor G2 |
| [[MT1M]] | 0.774 | metallothionein 1M |
| [[ITGA10]] | 0.774 | integrin subunit alpha 10 |
| [[RIPOR2]] | 0.757 | RHO family interacting cell polarization regulator 2 |
| [[CCND3]] | 0.752 | cyclin D3 |
| [[MAFB]] | 0.733 | MAF bZIP transcription factor B |
| [[TNS2]] | 0.730 | tensin 2 |
| [[ADPRHL1]] | 0.724 | ADP-ribosylhydrolase like 1 |
| [[STXBP5-AS1]] | 0.711 | STXBP5 antisense RNA 1 |
| [[HIPK2]] | 0.701 | homeodomain interacting protein kinase 2 |
| [[B3GNT5]] | 0.700 | UDP-GlcNAc:betaGal beta-1,3-N-acetylglucosaminyltransferase 5 |
| [[PDZD2]] | 0.682 | PDZ domain containing 2 |
| [[SLC26A2]] | 0.679 | solute carrier family 26 member 2 |
| [[SAMSN1]] | 0.678 | SAM domain, SH3 domain and nuclear localization signals 1 |
| [[FGD4]] | 0.671 | FYVE, RhoGEF and PH domain containing 4 |
| [[ADAMTS9]] | 0.665 | ADAM metallopeptidase with thrombospondin type 1 motif 9 |
| [[FOXC2]] | 0.664 | forkhead box C2 |
| [[LTBR]] | 0.659 | lymphotoxin beta receptor |
| [[STXBP5]] | 0.659 | syntaxin binding protein 5 |
| [[SNAI2]] | 0.655 | snail family transcriptional repressor 2 |
| [[RTN4RL1]] | 0.649 | reticulon 4 receptor like 1 |
| [[GLUL]] | 0.645 | glutamate-ammonia ligase |
| [[FSTL3]] | 0.641 | follistatin like 3 |
| [[BATF]] | 0.641 | basic leucine zipper ATF-like transcription factor |
| [[UBE2E1]] | 0.629 | ubiquitin conjugating enzyme E2 E1 |
| [[DIP2C]] | 0.617 | DIP2 acetate--CoA ligase C (putative) |
| [[TOP1]] | 0.603 | DNA topoisomerase I |
| [[SH3TC1]] | 0.594 | SH3 domain and tetratricopeptide repeats 1 |
| [[TFCP2L1]] | 0.587 | transcription factor CP2 like 1 |
| [[PHACTR3]] | 0.581 | phosphatase and actin regulator 3 |
| [[FOXN2]] | 0.581 | forkhead box N2 |
| [[TBXAS1]] | 0.574 | thromboxane A synthase 1 |
| [[SLCO2A1]] | 0.574 | solute carrier organic anion transporter family member 2A1 |
| [[PANX1]] | 0.573 | pannexin 1 |
| [[KCNG2]] | 0.557 | potassium voltage-gated channel modifier subfamily G member 2 |
| [[FRMD3]] | 0.548 | FERM domain containing 3 |
| [[KRT7]] | 0.529 | keratin 7 |
| [[BIN1]] | 0.526 | bridging integrator 1 |
| [[MARVELD1]] | 0.525 | MARVEL domain containing 1 |
| [[ENOX1]] | 0.507 | ecto-NOX disulfide-thiol exchanger 1 |
| [[CAV1]] | 0.489 | caveolin 1 |
| [[NFIC]] | 0.474 | nuclear factor I C |
| [[CDV3]] | 0.450 | CDV3 homolog |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 98; `graph/modules.parquet` — module == 98; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [97] (drug-dose × line)
