---
module: 125
type: "module"
n_genes: 39
n_plus: 39
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 125

*39 genes (single-armed) · [[Module 125.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 124), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Homoharringtonine (drug)]] 5 µM (+16.0, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (+9.3, ⚠ cell-cycle shift); [[Auranofin (drug)]] 5 µM (+8.5); [[Harringtonine (drug)]] 5 µM (+7.4, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (+7.2); [[Dinaciclib (drug)]] 5 µM (+6.3, ⚠ toxic; transcription drop; cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (+6.0, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+5.8, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (+5.5, ⚠ toxic; transcription drop; cell-cycle shift); [[Tucidinostat (drug)]] 0.5 µM (+4.8, ⚠ cell-cycle shift); [[Ixazomib citrate (drug)]] 0.5 µM (+4.2); [[Homoharringtonine (drug)]] 0.05 µM (+3.1); [[Vinblastine (sulfate) (drug)]] 5 µM (+2.9); [[Peretinoin (drug)]] 5 µM (+2.6); [[Peretinoin (drug)]] 0.5 µM (+2.6); [[Ipatasertib (drug)]] 0.5 µM (+2.4); [[EX229 (drug)]] 5 µM (+2.3); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+2.2) (106 in all, 44 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)
- Lower it: [[Dexamethasone (drug)]] 0.5 µM (-2.5); [[Clobetasol propionate (drug)]] 5 µM (-2.3); [[Adagrasib (drug)]] 0.05 µM (-1.9, ⚠ position not correctable); [[Dexamethasone (drug)]] 5 µM (-1.8); [[Ipatasertib (drug)]] 5 µM (-1.7); [[Budesonide (drug)]] 5 µM (-1.7); [[Dexamethasone (drug)]] 0.05 µM (-1.6); [[Citalopram (hydrobromide) (drug)]] 0.05 µM (-1.6); [[Phenylephrine (hydrochloride) (drug)]] 5 µM (-1.5); [[ERK5-IN-2 (drug)]] 5 µM (-1.5); [[Dabrafenib (drug)]] 5 µM (-1.5) (36 in all, 2 with an alert ⚠; shown: the 10 strongest and the 1 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[A-172 (line)]], [[HOP62 (line)]], [[COLO 205 (line)]], [[A498 (line)]], [[NCI-H460 (line)]], [[MIA PaCa-2 (line)]], [[SNU-1 (line)]], [[PANC-1 (line)]]

## + arm (39)

| Gene | Projection | Name |
|---|---|---|
| [[LINC02154]] | 0.869 | long independently transcribed non-coding RNA 2154 |
| [[SLAMF7]] | 0.831 | SLAM family member 7 |
| [[ROR1-AS1]] | 0.804 | ROR1 antisense RNA 1 |
| [[NGF]] | 0.795 | nerve growth factor |
| [[CRYM]] | 0.792 | crystallin mu |
| [[C12orf50]] | 0.789 | zinc finger CCCH-type containing 11D |
| [[ENTHD1]] | 0.779 | ENTH domain containing 1 |
| [[RPLP0P2]] | 0.773 | ribosomal protein lateral stalk subunit P0 pseudogene 2 |
| [[HDAC9]] | 0.760 | histone deacetylase 9 |
| [[LINC01828]] | 0.760 | long independently transcribed non-coding RNA 1828 |
| [[ANKRD30B]] | 0.760 | ankyrin repeat domain 30B |
| [[CPEB1]] | 0.733 | cytoplasmic polyadenylation element binding protein 1 |
| [[PNLIPRP3]] | 0.731 | pancreatic lipase related protein 3 |
| [[IGFN1]] | 0.711 | immunoglobulin like and fibronectin type III domain containing 1 |
| [[KCP]] | 0.695 | kielin cysteine rich BMP regulator |
| [[LINC00520]] | 0.694 | long independently transcribed non-coding RNA 520 |
| [[SPINK1]] | 0.683 | serine peptidase inhibitor Kazal type 1 |
| [[CREB5]] | 0.675 | cAMP responsive element binding protein 5 |
| [[TRIML2]] | 0.673 | tripartite motif family like 2 |
| [[PSG4]] | 0.661 | pregnancy specific beta-1-glycoprotein 4 |
| [[ACTN2]] | 0.656 | actinin alpha 2 |
| [[PPIF]] | 0.653 | peptidylprolyl isomerase F |
| [[EML5]] | 0.628 | EMAP like 5 |
| [[OSGIN1]] | 0.611 | oxidative stress induced growth inhibitor 1 |
| [[CCL3]] | 0.607 | C-C motif chemokine ligand 3 |
| [[HRK]] | 0.595 | harakiri, BCL2 interacting protein |
| [[PSG9]] | 0.587 | pregnancy specific beta-1-glycoprotein 9 |
| [[HMOX1]] | 0.574 | heme oxygenase 1 |
| [[ABCA15P]] | 0.539 | ATP binding cassette subfamily A member 15, pseudogene |
| [[UPP1]] | 0.488 | uridine phosphorylase 1 |
| [[TMEM40]] | 0.464 | transmembrane protein 40 |
| [[ATP6V0A1]] | 0.456 | ATPase H+ transporting V0 subunit a1 |
| [[SUN3]] | 0.440 | Sad1 and UNC84 domain containing 3 |
| [[NPL]] | 0.438 | N-acetylneuraminate pyruvate lyase |
| [[RPS4Y1]] | 0.424 | ribosomal protein S4 Y-linked 1 |
| [[PCCA-DT]] | 0.422 | PCCA divergent transcript |
| [[ZNF165]] | 0.417 | zinc finger protein 165 |
| [[ROBO3]] | 0.373 | roundabout guidance receptor 3 |
| [[PSG5]] | 0.359 | pregnancy specific beta-1-glycoprotein 5 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 125; `graph/modules.parquet` — module == 125; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [124] (drug-dose × line)
