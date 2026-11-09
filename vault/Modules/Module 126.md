---
module: 126
type: "module"
n_genes: 39
n_plus: 39
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.3571648895740509
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 126

*39 genes (single-armed) · [[Module 126.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 125), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Dinaciclib (drug)]] 5 µM (+7.3, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (+7.1, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+5.6, ⚠ toxic; transcription drop; cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (+3.9, ⚠ cell-cycle shift); [[Docetaxel (drug)]] 0.05 µM (+2.7, ⚠ transcription drop; cell-cycle shift); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (+1.6, ⚠ cell-cycle shift); [[Niclosamide (olamine) (drug)]] 5 µM (+1.3, ⚠ toxic; cell-cycle shift); [[Doxycycline (monohydrate) (drug)]] 5 µM (+1.3); [[Bosentan (hydrate) (drug)]] 5 µM (+1.2); [[c-Kit-IN-1 (drug)]] 0.05 µM (+1.2, ⚠ unreliable plate only); [[Auranofin (drug)]] 5 µM (+1.2); [[crizotinib (drug)]] 5 µM (+1.1); [[Imiquimod (hydrochloride) (drug)]] 0.05 µM (+1.1); [[Fluvoxamine (drug)]] 0.5 µM (+1.1); [[Adenine (drug)]] 0.05 µM (+1.0); [[Vismodegib (drug)]] 5 µM (+1.0); [[Altretamine (drug)]] 0.5 µM (+1.0); [[Bendamustine (drug)]] 0.5 µM (+1.0) (25 in all, 13 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)
- Lower it: [[Panobinostat (drug)]] 0.5 µM (-6.4, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (-6.3, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (-5.2, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (-2.8, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-2.6, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-2.6, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (-2.2); [[Harringtonine (drug)]] 0.5 µM (-2.0, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 5 µM (-1.8, ⚠ cell-cycle shift); [[Bosentan (hydrate) (drug)]] 0.5 µM (-1.6); [[Brivudine (drug)]] 5 µM (-1.4); [[Arbutin (drug)]] 5 µM (-1.3); [[Doxycycline (monohydrate) (drug)]] 0.5 µM (-1.3); [[Almonertinib (hydrochloride) (drug)]] 0.05 µM (-1.3); [[Loperamide (hydrochloride) (drug)]] 5 µM (-1.3); [[Thymol (drug)]] 5 µM (-1.2); [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM (-1.1); [[Voriconazole (drug)]] 5 µM (-1.0) (24 in all, 11 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[SW480 (line)]], [[PANC-1 (line)]], [[KATO III (line)]], [[LoVo (line)]], [[HT-29 (line)]], [[NCI-H460 (line)]], [[A498 (line)]], [[J82 (line)]]

## + arm (39)

| Gene | Projection | Name |
|---|---|---|
| [[CERS2]] | 0.851 | ceramide synthase 2 |
| [[INPPL1]] | 0.839 | inositol polyphosphate phosphatase like 1 |
| [[U2AF2]] | 0.827 | U2 small nuclear RNA auxiliary factor 2 |
| [[MTA2]] | 0.811 | metastasis associated 1 family member 2 |
| [[UBQLN4]] | 0.799 | ubiquilin 4 |
| [[LY6G5B]] | 0.786 | lymphocyte antigen 6 family member G5B |
| [[MAN2A2]] | 0.784 | mannosidase alpha class 2A member 2 |
| [[ATN1]] | 0.779 | atrophin 1 |
| [[LDB1]] | 0.767 | LIM domain binding 1 |
| [[PLXNB1]] | 0.742 | plexin B1 |
| [[DVL3]] | 0.733 | dishevelled segment polarity protein 3 |
| [[HCFC1]] | 0.723 | host cell factor C1 |
| [[KLC2]] | 0.722 | kinesin light chain 2 |
| [[BCL2L2]] | 0.718 | BCL2 like 2 |
| [[SNHG22]] | 0.708 | small nucleolar RNA host gene 22 |
| [[RCC2]] | 0.697 | regulator of chromosome condensation 2 |
| [[NPEPL1]] | 0.682 | aminopeptidase like 1 |
| [[GRK2]] | 0.659 | G protein-coupled receptor kinase 2 |
| [[SORBS3]] | 0.648 | sorbin and SH3 domain containing 3 |
| [[CTBP1]] | 0.633 | C-terminal binding protein 1 |
| [[ATXN2L]] | 0.627 | ataxin 2 like |
| [[PPP1R9B]] | 0.610 | protein phosphatase 1 regulatory subunit 9B |
| [[ADCY6]] | 0.597 | adenylate cyclase 6 |
| [[ZNF740]] | 0.596 | zinc finger protein 740 |
| [[CTR9]] | -0.595 | CTR9 component of Paf1/RNA polymerase II complex |
| [[MED22]] | 0.595 | mediator complex subunit 22 |
| [[PCGF2]] | 0.594 | polycomb group ring finger 2 |
| [[VEZT]] | -0.586 | vezatin, adherens junctions transmembrane protein |
| [[KCNIP2]] | 0.578 | potassium voltage-gated channel interacting protein 2 |
| [[CDH24]] | 0.560 | cadherin 24 |
| [[SSH3]] | 0.559 | slingshot protein phosphatase 3 |
| [[SGSM2]] | 0.546 | small G protein signaling modulator 2 |
| [[GAS6]] | 0.528 | growth arrest specific 6 |
| [[MKRN5P]] | 0.519 | makorin ring finger protein 5, pseudogene |
| [[AJM1]] | 0.491 | apical junction component 1 homolog |
| [[PFKFB2]] | 0.461 | 6-phosphofructo-2-kinase/fructose-2,6-biphosphatase 2 |
| [[DUSP22]] | 0.449 | dual specificity phosphatase 22 |
| [[SELENOI]] | 0.371 | selenoprotein I |
| [[OTUD3]] | 0.340 | OTU deubiquitinase 3 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 126; `graph/modules.parquet` — module == 126; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [125] (drug-dose × line)
