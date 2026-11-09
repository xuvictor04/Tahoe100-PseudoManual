---
symbol: "TMEM134"
type: "gene"
col: 10279
ensembl_id: "ENSG00000172663"
name: "transmembrane protein 134"
location: "11q13.2"
module: 24
arm: "+"
pooled_cpm: 13.06
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 16
n_dd_up_clean: 3
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# TMEM134

*transmembrane protein 134* — 11q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.82× (z +7.2, q 2e-10, up in 33 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.427× (z -10.3, q 4e-22, down in 40 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DDT]] (+0.69, fdr 9e-06), [[FBXL15]] (+0.69, fdr 6e-05), [[FKBP2]] (+0.68, fdr 7e-06, ⚠ FKBP2 in the vector space only through flagged drug-doses), [[OST4]] (+0.68, fdr 1e-05); moves opposite to [[SFPQ]] (-0.63, fdr 9e-05), [[G3BP1]] (-0.62, fdr 3e-05), [[EWSR1]] (-0.60, fdr 4e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10279.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.82×** | +7.2 | 2e-10 | 33/45 (LoVo, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.23×** | +5.9 | 1e-06 | 30/48 (NCI-H1792, A-172, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.67×** | +4.4 | 0.002 | 20/33 (KATO III, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~7% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.63×** | +4.0 | 0.009 | 20/38 (SW1417, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.51×** | +3.5 | 0.045 | 18/40 (AsPC-1, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~25% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.87×** | +3.4 | 0.069 | 17/44 (NCI-H1573, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.86×** | +3.3 | 0.072 | 19/41 (SW1417, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Celecoxib (drug)]] 0.5 µM |  | 1.79× | +3.1 | 0.12 | 9/45 (A-172, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 1.28× | +3.0 | 0.17 | 11/47 (NCI-H1573, PANC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 1 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10279.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.427×** | -10.3 | 4e-22 | 40/46 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.469×** | -6.5 | 3e-08 | 38/47 (C32, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.515×** | -5.7 | 3e-06 | 26/44 (NCI-H1792, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.530×** | -5.4 | 8e-06 | 30/48 (HS-578T, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.304×** | -4.5 | 9e-04 | 31/43 (LoVo, NCI-H2030, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.311×** | -4.4 | 0.001 | 28/48 (Panc 03.27, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.590×** | -4.3 | 0.001 | 20/39 (J82, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.708×** | -4.2 | 0.002 | 25/47 (LS 180, NCI-H1573, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.628×** | -3.8 | 0.008 | 24/46 (NCI-H1792, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.643×** | -3.8 | 0.009 | 20/46 (H4, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.627×** | -3.8 | 0.009 | 23/47 (NCI-H2347, C32, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.658×** | -3.6 | 0.017 | 18/48 (NCI-H1792, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.665×** | -3.5 | 0.022 | 22/46 (SNU-423, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.668×** | -3.4 | 0.023 | 20/47 (J82, H4, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.658×** | -3.4 | 0.028 | 20/44 (SW1417, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~19% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.691×** | -3.2 | 0.057 | 18/46 (BT-474, MIA PaCa-2, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10279. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 12.2 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0843× (z -11.4) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.211× (z -10.5) |
| [[NCI-H1792 (line)]] | alt | 38.9 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.118× (z -11.6) |
| [[A-172 (line)]] | wt | 21.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -15.7) |
| [[BT-474 (line)]] | alt | 17.0 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0520× (z -14.6) |
| [[C32 (line)]] | wt | 19.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -9.3) |
| [[H4 (line)]] | wt | 9.29 | 0 | 1 | — | [[Digitoxin (drug)]] 0.05 µM 0.0615× (z -8.7) |
| [[HOP62 (line)]] | alt | 17.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -10.5) |
| [[HS-578T (line)]] | alt | 10.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -10.7) |
| [[Panc 03.27 (line)]] | alt | 12.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -9.3) |
| [[PANC-1 (line)]] | alt | 18.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -13.1) |
| [[RPMI-7951 (line)]] | alt | 10.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -10.0) |
| [[A-427 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.29 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.96 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.16 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.15 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.47 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.00 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.59 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.92 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.38 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.42 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.64 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.49 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.78 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.92 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 9.01 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10279), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDT]] | +0.69 | +0.57 / +0.78 | both halves | 9e-06 |  |
| [[FBXL15]] | +0.69 | +0.38 / +0.78 | both halves | 6e-05 |  |
| [[FKBP2]] ⚠ | +0.68 | +0.61 / +0.74 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[OST4]] | +0.68 | +0.53 / +0.75 | both halves | 1e-05 |  |
| [[VKORC1]] | +0.67 | +0.57 / +0.80 | both halves | 9e-06 |  |
| [[POLR2H]] | +0.64 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[DNLZ]] | +0.64 | +0.44 / +0.68 | both halves | 3e-05 |  |
| [[GUK1]] | +0.64 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[PHPT1]] | +0.64 | +0.59 / +0.72 | both halves | 7e-06 |  |
| [[FBXL12]] | +0.63 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[TRPT1]] | +0.63 | +0.60 / +0.73 | both halves | 7e-06 |  |
| [[NUDT22]] | +0.63 | +0.46 / +0.70 | both halves | 3e-05 |  |
| [[DCTN6-DT]] | +0.63 | +0.60 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SFPQ]] | -0.63 | -0.37 / -0.66 | both halves | 9e-05 |  |
| [[G3BP1]] | -0.62 | -0.43 / -0.69 | both halves | 3e-05 |  |
| [[EWSR1]] | -0.60 | -0.41 / -0.66 | both halves | 4e-05 |  |
| [[TRIM44]] | -0.58 | -0.42 / -0.63 | both halves | 4e-05 |  |
| [[NONO]] | -0.57 | -0.31 / -0.66 | both halves | 2e-04 |  |
| [[FAT1]] | -0.57 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[EIF4G1]] | -0.54 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[DHX9]] | -0.54 | -0.37 / -0.62 | both halves | 8e-05 |  |
| [[PTPN11]] | -0.54 | -0.37 / -0.57 | both halves | 9e-05 |  |
| [[TUSC3]] | -0.54 | -0.46 / -0.57 | both halves | 2e-05 |  |
| [[OCRL]] | -0.54 | -0.27 / -0.61 | both halves | 3e-04 |  |
| [[PRELID3B]] | -0.54 | -0.35 / -0.61 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.609). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-39.1, -20.1); signed map (-28.7, 10.2). **Vector** length 72.8, 16.5% of its response variance represented; |z| ≥ 3 in 722 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +7.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | +2.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +3.3 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.8 | +1.6 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.8 | +2.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +2.9 |
|  | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM |  | +1.4 | +1.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.9 | -4.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.4 | -3.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.9 | +1.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -2.8 | -4.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -2.6 | +4.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.5 | -0.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.3 | -3.8 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | -1.4 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 134 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.2 — chr11:67,461,710-67,469,272 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ21749 |
| Matched by | ensembl_id |

UniProt [Q9H6X4](https://www.uniprot.org/uniprotkb/Q9H6X4) carries no function annotation.

**Summary**, from NCBI Gene [80194](https://www.ncbi.nlm.nih.gov/gene/80194):

> Located in cytosol and perinuclear region of cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26142](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26142) · Entrez [80194](https://www.ncbi.nlm.nih.gov/gene/80194) · UniProt [Q9H6X4](https://www.uniprot.org/uniprotkb/Q9H6X4) · Ensembl [ENSG00000172663](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172663)

## Data

Gene col 10279: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10279); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10279, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10279]; `tensor/DDL_lfc|DDL_z.npy` [10279]; `embed/gene_vectors.npy` [10279]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10279 or target_col == 10279). Every well: [[TMEM134 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM134.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
