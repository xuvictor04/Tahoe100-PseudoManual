---
module: 140
type: "module"
n_genes: 34
n_plus: 34
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 140

*34 genes (single-armed) · [[Module 140.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 139), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM (+20.8, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (+12.8, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (+12.5, ⚠ toxic; transcription drop; cell-cycle shift); [[Homoharringtonine (drug)]] 5 µM (+10.1, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+9.3, ⚠ toxic; transcription drop; cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (+8.6); [[Idarubicin (hydrochloride) (drug)]] 0.5 µM (+7.8, ⚠ cell-cycle shift); [[Epirubicin (hydrochloride) (drug)]] 5 µM (+5.3, ⚠ cell-cycle shift); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (+5.1, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 0.5 µM (+4.8, ⚠ cell-cycle shift); [[Auranofin (drug)]] 5 µM (+4.5); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+4.3); [[Ipatasertib (drug)]] 0.5 µM (+2.3); [[Docetaxel (Trihydrate) (drug)]] 0.5 µM (+1.9); [[XRK3F2 (drug)]] 0.5 µM (+1.7); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM (+1.7); [[Methylprednisolone succinate (drug)]] 0.5 µM (+1.7); [[Verteporfin (drug)]] 5 µM (+1.6); [[Bendamustine (drug)]] 5 µM (+1.5) (75 in all, 34 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)
- Lower it: [[Adagrasib (drug)]] 0.05 µM (-2.4, ⚠ position not correctable); [[Lucanthone (drug)]] 0.05 µM (-1.8); [[Fenofibrate (drug)]] 0.05 µM (-1.7); [[Digitoxin (drug)]] 0.05 µM (-1.6, ⚠ cell-cycle shift); [[Anethole trithione (drug)]] 0.5 µM (-1.5); [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM (-1.5); [[Goserelin (acetate) (drug)]] 5 µM (-1.5); [[Diphenhydramine (drug)]] 0.05 µM (-1.5); [[Rutin (trihydrate) (drug)]] 0.05 µM (-1.4); [[Ciclopirox (drug)]] 0.5 µM (-1.4); [[Artesunate (drug)]] 0.5 µM (-1.3); [[Dabrafenib (drug)]] 5 µM (-1.3) (37 in all, 3 with an alert ⚠; shown: the 10 strongest and the 2 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[SW480 (line)]], [[SNU-1 (line)]], [[RKO (line)]], [[HOP62 (line)]], [[PANC-1 (line)]], [[C-33 A (line)]], [[A498 (line)]], [[HEC-1-A (line)]]

## + arm (34)

| Gene | Projection | Name |
|---|---|---|
| [[USH2A]] | 0.901 | usherin |
| [[SCHLAP1]] | 0.880 | SWI/SNF complex antagonist associated with prostate cancer 1 |
| [[GALNTL6]] | 0.879 | polypeptide N-acetylgalactosaminyltransferase like 6 |
| [[SORCS3]] | 0.872 | sortilin related VPS10 domain containing receptor 3 |
| [[C8orf34]] | 0.871 | chromosome 8 open reading frame 34 |
| [[SLC27A6]] | 0.857 | solute carrier family 27 member 6 |
| [[CNTN5]] | 0.843 | contactin 5 |
| [[GALNT17]] | 0.831 | polypeptide N-acetylgalactosaminyltransferase 17 |
| [[MEIOC]] | 0.830 | meiosis specific with coiled-coil domain |
| [[AGBL1]] | 0.824 | AGBL carboxypeptidase 1 |
| [[DPYD-AS1]] | 0.813 | DPYD antisense RNA 1 |
| [[SFRP4]] | 0.804 | secreted frizzled related protein 4 |
| [[LINC01579]] | 0.801 | long independently transcribed non-coding RNA 1579 |
| [[CSMD1]] | 0.782 | CUB and Sushi multiple domains 1 |
| [[GABRG3]] | 0.777 | gamma-aminobutyric acid type A receptor subunit gamma3 |
| [[AQP4-AS1]] | 0.769 | AQP4 antisense RNA 1 |
| [[SCN1A-AS1]] | 0.757 | SCN1A and SCN9A antisense RNA 1 |
| [[PTPRO]] | 0.736 | protein tyrosine phosphatase receptor type O |
| [[LINC00922]] | 0.718 | long independently transcribed non-coding RNA 922 |
| [[CUX2]] | 0.703 | cut like homeobox 2 |
| [[FILIP1]] | 0.692 | filamin A interacting protein 1 |
| [[KCNB1]] | 0.665 | potassium voltage-gated channel subfamily B member 1 |
| [[ARL14EP-DT]] | 0.663 | ARL14EP divergent transcript |
| [[SLC25A48]] | 0.617 | solute carrier family 25 member 48 |
| [[ATP8B4]] | 0.615 | ATPase phospholipid transporting 8B4 (putative) |
| [[RBFOX1]] | 0.595 | RNA binding fox-1 homolog 1 |
| [[PAX5]] | 0.572 | paired box 5 |
| [[CLDN10]] | 0.564 | claudin 10 |
| [[SRSF12]] | 0.528 | serine and arginine rich splicing factor 12 |
| [[FSTL4]] | 0.484 | follistatin like 4 |
| [[TRPC6]] | 0.484 | transient receptor potential cation channel subfamily C member 6 |
| [[LINC01429]] | 0.448 | long independently transcribed non-coding RNA 1429 |
| [[CPNE4]] | 0.440 | copine 4 |
| [[FHAD1]] | 0.382 | forkhead associated phosphopeptide binding domain 1 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 140; `graph/modules.parquet` — module == 140; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [139] (drug-dose × line)
