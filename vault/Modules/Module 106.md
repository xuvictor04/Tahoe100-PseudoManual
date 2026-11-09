---
module: 106
type: "module"
n_genes: 44
n_plus: 44
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.2481602281332016
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 106

*44 genes (single-armed) · [[Module 106.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 105), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Tucidinostat (drug)]] 5 µM (+7.4); [[Tucidinostat (drug)]] 0.5 µM (+4.9, ⚠ cell-cycle shift); [[Clobetasol propionate (drug)]] 0.05 µM (+3.4); [[Budesonide (drug)]] 0.05 µM (+3.4); [[Panobinostat (drug)]] 0.05 µM (+3.3, ⚠ cell-cycle shift); [[Betamethasone dipropionate (drug)]] 5 µM (+3.1); [[Clobetasol propionate (drug)]] 0.5 µM (+3.1); [[Budesonide (drug)]] 0.5 µM (+2.9); [[Clobetasol propionate (drug)]] 5 µM (+2.7); [[Betamethasone dipropionate (drug)]] 0.5 µM (+2.6); [[Betamethasone dipropionate (drug)]] 0.05 µM (+2.6); [[Citalopram (hydrobromide) (drug)]] 0.05 µM (+2.6) (40 in all, 7 with an alert ⚠; shown: the 10 strongest and the 2 next strongest without an alert)
- Lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM (-2.6, ⚠ toxic; cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-2.6, ⚠ cell-cycle shift); [[Auranofin (drug)]] 5 µM (-2.5); [[Homoharringtonine (drug)]] 0.05 µM (-2.1); [[5-Azacytidine (drug)]] 5 µM (-1.8); [[Harringtonine (drug)]] 0.5 µM (-1.6, ⚠ cell-cycle shift); [[Ixazomib citrate (drug)]] 5 µM (-1.6, ⚠ cell-cycle shift); [[TAK-733 (drug)]] 5 µM (-1.6); [[Daptomycin (drug)]] 0.5 µM (-1.5, ⚠ unreliable plate only); [[c-Kit-IN-1 (drug)]] 0.05 µM (-1.5, ⚠ unreliable plate only); [[Abemaciclib (drug)]] 5 µM (-1.4); [[vincristine (drug)]] 0.5 µM (-1.4); [[Vinblastine (sulfate) (drug)]] 0.5 µM (-1.3); [[Peretinoin (drug)]] 5 µM (-1.2); [[Peretinoin (drug)]] 0.5 µM (-1.2); [[Vinblastine (sulfate) (drug)]] 5 µM (-1.2) (25 in all, 10 with an alert ⚠; shown: the 10 strongest and the 6 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[HOP62 (line)]], [[hTERT-HPNE (line)]], [[NCI-H1792 (line)]], [[HS-578T (line)]], [[NCI-H1573 (line)]], [[A498 (line)]], [[SNU-423 (line)]], [[NCI-H2347 (line)]]

## + arm (44)

| Gene | Projection | Name |
|---|---|---|
| [[PDLIM1]] | 0.794 | PDZ and LIM domain 1 |
| [[ACSL1]] | 0.779 | acyl-CoA synthetase long chain family member 1 |
| [[B4GALT1]] | 0.779 | beta-1,4-galactosyltransferase 1 |
| [[EPS8]] | 0.777 | EGFR pathway substrate 8, signaling adaptor |
| [[TSC22D3]] | 0.773 | TSC22 domain family member 3 |
| [[FLVCR2]] | 0.737 | FLVCR choline and putative heme transporter 2 |
| [[PELI1]] | 0.706 | pellino E3 ubiquitin protein ligase 1 |
| [[SSBP2]] | 0.704 | single stranded DNA binding protein 2 |
| [[CPD]] | 0.671 | carboxypeptidase D |
| [[GAREM1]] | 0.669 | GRB2 associated regulator of MAPK1 subtype 1 |
| [[EDN2]] | 0.661 | endothelin 2 |
| [[PDK4]] | 0.661 | pyruvate dehydrogenase kinase 4 |
| [[SLC44A1]] | 0.655 | solute carrier family 44 member 1 |
| [[ESYT2]] | 0.651 | extended synaptotagmin 2 |
| [[TGFBR3]] | 0.642 | transforming growth factor beta receptor 3 |
| [[TLE1]] | 0.641 | TLE family member 1, transcriptional corepressor |
| [[IFNGR1]] | 0.638 | interferon gamma receptor 1 |
| [[SGPP2]] | 0.635 | sphingosine-1-phosphate phosphatase 2 |
| [[MAP2]] | 0.615 | microtubule associated protein 2 |
| [[PER1]] | 0.608 | period circadian regulator 1 |
| [[PLEKHA7]] | 0.606 | pleckstrin homology domain containing A7 |
| [[TRIM29]] | 0.597 | tripartite motif containing 29 |
| [[SORT1]] | 0.591 | sortilin 1 |
| [[NEBL]] | 0.587 | nebulette |
| [[UGP2]] | 0.558 | UDP-glucose pyrophosphorylase 2 |
| [[LINC00511]] | 0.549 | long independently transcribed non-coding RNA 511 |
| [[HOPX]] | 0.529 | HOP homeobox |
| [[SLC39A8]] | 0.523 | solute carrier family 39 member 8 |
| [[SLC39A14]] | 0.517 | solute carrier family 39 member 14 |
| [[SLC19A2]] | 0.513 | solute carrier family 19 member 2 |
| [[PHF21A]] | 0.504 | PHD finger protein 21A |
| [[ZFAND5]] | 0.493 | zinc finger AN1-type containing 5 |
| [[POLR3GL]] | 0.493 | RNA polymerase III subunit GL |
| [[PPA1]] | 0.463 | inorganic pyrophosphatase 1 |
| [[CTNNB1]] | 0.456 | catenin beta 1 |
| [[FAM227A]] | -0.455 | family with sequence similarity 227 member A |
| [[TPCN1]] | 0.448 | two pore segment channel 1 |
| [[GCNT1]] | 0.442 | glucosaminyl (N-acetyl) transferase 1 |
| [[TNFRSF1A]] | 0.407 | TNF receptor superfamily member 1A |
| [[PAG1]] | 0.382 | phosphoprotein membrane anchor with glycosphingolipid microdomains 1 |
| [[FMN1]] | 0.371 | formin 1 |
| [[TES]] | 0.362 | testin LIM domain protein |
| [[SNCG]] | 0.354 | synuclein gamma |
| [[RHOBTB1]] | 0.304 | Rho related BTB domain containing 1 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 106; `graph/modules.parquet` — module == 106; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [105] (drug-dose × line)
