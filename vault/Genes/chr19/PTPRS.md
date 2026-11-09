---
symbol: "PTPRS"
type: "gene"
col: 2602
ensembl_id: "ENSG00000105426"
name: "protein tyrosine phosphatase receptor type S"
location: "19p13.3"
module: 82
arm: "+"
pooled_cpm: 52.9
n_lines_expressing: 42
n_dd_up: 10
n_dd_down: 17
n_dd_up_clean: 7
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 9
direction_downstream: 0
tags: ["gene", "module/082"]
generated_by: "tahoemap"
---

# PTPRS

*protein tyrosine phosphatase receptor type S* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.75× (z +18.1, q 0e+00, up in 38 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.519× (z -15.0, q 0e+00, down in 35 of 40 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KIF5C]] (+0.68, fdr 1e-05), [[TOX2]] (+0.66, fdr 1e-05), [[CACNG7]] (+0.63, fdr 3e-05); moves opposite to [[LINC02100]] (-0.62, fdr 4e-05), [[RNF146]] (-0.62, fdr 3e-05), [[PSMB8]] (-0.61, fdr 2e-05).
> It is in [[Module 082]], a single-armed module (Muscle contraction).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[FSD1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2602.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.75×** | +18.1 | 0e+00 | 38/40 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.79×** | +13.4 | 3e-38 | 33/40 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.76×** | +12.9 | 5e-36 | 34/40 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.53×** | +9.4 | 7e-19 | 21/36 (NCI-H1792, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.49×** | +9.2 | 5e-18 | 23/41 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.42×** | +7.9 | 2e-13 | 25/40 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.37×** | +7.2 | 5e-11 | 30/40 (SW480, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.34×** | +6.7 | 2e-09 | 26/40 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.31×** | +5.8 | 5e-07 | 18/37 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.19× | +3.9 | 0.006 | 15/39 (A-172, C-33 A, …) | two highest doses | low cells (technical?) |
| [[Brivudine (drug)]] 5 µM |  | **1.33×** | +3.4 | 0.032 | 13/40 (NCI-H1573, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.5 µM |  | 1.15× | +3.2 | 0.066 | 8/40 (HS-578T, LOX-IMVI, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.14× | +3.1 | 0.090 | 7/40 (HS-578T, PANC-1, …) | top dose only |  |
| [[Bergenin (drug)]] 5 µM |  | 1.10× | +3.0 | 0.10 | 0/40 | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2602.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.519×** | -15.0 | 0e+00 | 35/40 (NCI-H2030, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.630×** | -14.9 | 0e+00 | 30/40 (AN3 CA, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.524×** | -14.2 | 2e-43 | 31/40 (NCI-H2030, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.563×** | -13.1 | 5e-37 | 35/40 (A-172, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.607×** | -11.4 | 5e-28 | 29/40 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.639×** | -10.2 | 2e-22 | 29/40 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.653×** | -9.7 | 2e-20 | 28/40 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.670×** | -9.1 | 5e-18 | 27/40 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.757×** | -9.0 | 2e-17 | 24/40 (SW 900, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.737×** | -7.0 | 2e-10 | 26/40 (LOX-IMVI, C-33 A, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.576×** | -6.6 | 2e-09 | 25/41 (NCI-H460, J82, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.790×** | -5.4 | 4e-06 | 18/40 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.791×** | -5.3 | 4e-06 | 20/39 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.861× | -4.8 | 6e-05 | 16/40 (A-427, C-33 A, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.675×** | -4.7 | 1e-04 | 14/40 (LOX-IMVI, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.813×** | -4.5 | 2e-04 | 19/40 (NCI-H23, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2602. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 117 | 2 | 9 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.06× (z +10.7) | [[Harringtonine (drug)]] 5 µM 0.274× (z -13.0) |
| [[PANC-1 (line)]] | alt | 43.0 | 5 (1 ⚠) | 5 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.77× (z +12.3) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.281× (z -15.3) |
| [[J82 (line)]] | alt | 59.4 | 5 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.57× (z +14.4) | [[Niclosamide (olamine) (drug)]] 5 µM 0.428× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~8% of this change |
| [[NCI-H23 (line)]] | alt | 60.8 | 0 | 6 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.298× (z -12.3) |
| [[SW480 (line)]] | alt | 32.4 | 6 | 0 | [[Tucidinostat (drug)]] 5 µM 3.76× (z +20.6) | — |
| [[HEC-1-A (line)]] | alt | 28.4 | 4 | 1 | [[Tucidinostat (drug)]] 5 µM 3.80× (z +16.3) | [[Harringtonine (drug)]] 0.5 µM 0.298× (z -10.4) |
| [[NCI-H1573 (line)]] | alt | 36.2 | 5 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.22× (z +13.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.33× (z +10.0) | — |
| [[LS 180 (line)]] | wt | 28.5 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 3.20× (z +13.4) | — |
| [[NCI-H2030 (line)]] | alt | 106 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -21.5) |
| [[NCI-H460 (line)]] | wt | 51.8 | 1 | 3 | [[Tucidinostat (drug)]] 5 µM 1.76× (z +10.4) | [[Harringtonine (drug)]] 0.5 µM 0.462× (z -10.0) |
| [[CFPAC-1 (line)]] | alt | 23.8 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.80× (z +9.9) | — |
| [[HOP62 (line)]] | alt | 53.5 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 2.15× (z +12.1) | — |
| [[RPMI-7951 (line)]] | alt | 74.5 | 1 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.39× (z +10.8) | [[Harringtonine (drug)]] 5 µM 0.324× (z -9.4) |
| [[A-172 (line)]] | wt | 89.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.408× (z -10.9) |
| [[HepG2_C3A (line)]] | wt | 99.0 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 2.12× (z +10.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.470× (z -10.2) |
| [[HS-578T (line)]] | alt | 98.3 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 1.84× (z +10.8) | — |
| [[NCI-H1792 (line)]] | alt | 76.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.40× (z +13.0) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 43.7 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 2.47× (z +10.3) | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -10.6) |
| [[SW 900 (line)]] | alt | 71.4 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.419× (z -11.2) |
| [[A-427 (line)]] | wt | 88.1 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.498× (z -11.8) |
| [[A498 (line)]] | wt | 68.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.427× (z -9.4) ⚠ toxic; cell-cycle shift, explains ~8% of this change |
| [[A549 (line)]] | wt | 62.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.354× (z -10.5) |
| [[AN3 CA (line)]] | alt | 119 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0996× (z -22.1) |
| [[AsPC-1 (line)]] | alt | 38.2 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.316× (z -9.3) |
| [[BT-474 (line)]] | alt | 101 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 1.69× (z +8.6) | — |
| [[C-33 A (line)]] | alt | 152 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.423× (z -10.5) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 148 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.210× (z -10.6) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 86.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.261× (z -10.5) ⚠ toxic; cell-cycle shift, explains ~8% of this change |
| [[MIA PaCa-2 (line)]] | alt | 88.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.369× (z -11.4) |
| [[NCI-H2347 (line)]] | alt | 32.4 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.12× (z +11.9) | — |
| [[SK-MEL-2 (line)]] | alt | 62.1 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.38× (z +11.3) | — |
| [[C32 (line)]] | wt | 64.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.00 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 9.96 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.15 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 34.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.3 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 6.72 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 53.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 90.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.96 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 6.32 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 60.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 76.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.2 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 16.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2602), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIF5C]] | +0.68 | +0.51 / +0.69 | both halves | 1e-05 |  |
| [[TOX2]] | +0.66 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[CACNG7]] | +0.63 | +0.61 / +0.46 | both halves | 3e-05 |  |
| [[TNK2]] | +0.63 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[TCF3]] | +0.62 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[COL18A1]] | +0.61 | +0.47 / +0.45 | both halves | 3e-05 | pathway: Extracellular matrix organization |
| [[GPRIN1]] | +0.61 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[ANXA6]] | +0.61 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[JAM3]] | +0.61 | +0.50 / +0.55 | both halves | 1e-05 | pathway: Extracellular matrix organization |
| [[SLC8B1]] | +0.61 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[PTPRF]] | +0.60 | +0.55 / +0.38 | both halves | 6e-05 | same gene group; pathway: Neuronal System |
| [[GNAI2]] | +0.60 | +0.55 / +0.30 | both halves | 2e-04 | pathway: Neuronal System |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02100]] | -0.62 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[RNF146]] | -0.62 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[PSMB8]] | -0.61 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[DNAI4]] | -0.60 | -0.47 / -0.33 | both halves | 1e-04 |  |
| [[TLR3]] | -0.57 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[DECR1]] | -0.56 | -0.48 / -0.39 | both halves | 5e-05 |  |
| [[APOL6]] | -0.56 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[PAXIP1-AS2]] | -0.56 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[INO80D]] | -0.56 | -0.26 / -0.47 | both halves | 4e-04 |  |
| [[PSMB10]] | -0.55 | -0.38 / -0.51 | both halves | 7e-05 |  |
| [[CASC9]] | -0.55 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[LINC00869-1]] | -0.55 | -0.36 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FSD1]] | B | FSD1 activity raises PTPRS's level | lines that do not express FSD1 (17) vs lines expressing it (33) | 3.58× lower at baseline in the lines without FSD1 | 0.006 | ⚠ within organs, on part of the lines; also absent: RFLNB, B4GALNT1, NTNG2 |
| [[BMERB1]] | B | BMERB1 activity raises PTPRS's level | lines that do not express BMERB1 (17) vs lines expressing it (33) | 3.36× lower at baseline in the lines without BMERB1 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: ENSG00000259363, NRG1, NPTX1 |
| [[NOVA2]] | B | NOVA2 activity raises PTPRS's level | lines that do not express NOVA2 (23) vs lines expressing it (27) | 2.73× lower at baseline in the lines without NOVA2 | 0.032 | ⚠ within organs, on part of the lines; also absent: RBM20, RAB39A, NPTX1 |
| [[JAKMIP1]] | B | JAKMIP1 activity raises PTPRS's level | lines that do not express JAKMIP1 (27) vs lines expressing it (23) | 2.32× lower at baseline in the lines without JAKMIP1 | 0.054 | ⚠ within organs, on part of the lines; also absent: CHST8, JPH3, GABBR2 |
| [[ADD2]] | B | ADD2 activity raises PTPRS's level | lines that do not express ADD2 (31) vs lines expressing it (19) | 2.56× lower at baseline in the lines without ADD2 | 0.066 | ⚠ within organs, on part of the lines; also absent: NEFL, CHST8, UCHL1 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers PTPRS's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers PTPRS's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[GPX3]] | B | GPX3 activity lowers PTPRS's level | lines that do not express GPX3 (26) vs lines expressing it (24) | 1.46× higher at baseline in the lines without GPX3 | 0.084 | ⚠ within organs, on part of the lines; also absent: LINC02057, KYNU, C3 |
| [[GNAO1]] | B | GNAO1 activity raises PTPRS's level | lines that do not express GNAO1 (22) vs lines expressing it (28) | 2.62× lower at baseline in the lines without GNAO1 | 0.089 | ⚠ within organs, on part of the lines; also absent: MGAT5B, KCNG1, SLC6A17 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 082]] — Muscle contraction; 55 genes; every member is in the + arm (projection on the module's main direction 0.688). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (34.8, 13.4); signed map (13.0, 35.8). **Vector** length 104, 26.5% of its response variance represented; |z| ≥ 3 in 1,153 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.9 | +18.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.1 | +9.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.7 | +7.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.5 | +9.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +7.1 | +12.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.1 | +3.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.0 | +2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +0.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.7 | +2.1 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -7.0 | -13.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.0 | -15.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.7 | -7.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.1 | -14.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.7 | -9.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.6 | -4.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.2 | -1.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.6 | -3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.6 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | protein tyrosine phosphatase receptor type S |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:5,158,495-5,340,812 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PTPsigma, PTP-sigma |
| Gene groups (HGNC) | Fibronectin type III domain containing; I-set domain containing; Protein tyrosine phosphatases receptor type; LAR protein receptor tyrosine phosphatase family |
| Reactome | 9 pathways, smallest: Receptor-type tyrosine-protein phosphatases; Signaling by NTRK3 (TRKC); Synaptic adhesion-like molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13332](https://www.uniprot.org/uniprotkb/Q13332) (Receptor-type tyrosine-protein phosphatase S):

> Cell surface receptor that binds to glycosaminoglycans, including chondroitin sulfate proteoglycans and heparan sulfate proteoglycan. Binding to chondroitin sulfate and heparan sulfate proteoglycans has opposite effects on PTPRS oligomerization and regulation of neurite outgrowth. Contributes to the inhibition of neurite and axonal outgrowth by chondroitin sulfate proteoglycans, also after nerve transection. Plays a role in stimulating neurite outgrowth in response to the heparan sulfate …

**Summary**, from NCBI Gene [5802](https://www.ncbi.nlm.nih.gov/gene/5802):

> The protein encoded by this gene is a member of the protein tyrosine phosphatase (PTP) family. PTPs are known to be signaling molecules that regulate a variety of cellular processes including cell growth, differentiation, mitotic cycle, and oncogenic transformation. This PTP contains an extracellular region, a single transmembrane segment and two tandem intracytoplasmic catalytic domains, and thus represents a receptor-type PTP. The extracellular region of this protein is composed of multiple …

**Accessions** — [HGNC:9681](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9681) · Entrez [5802](https://www.ncbi.nlm.nih.gov/gene/5802) · UniProt [Q13332](https://www.uniprot.org/uniprotkb/Q13332) · Ensembl [ENSG00000105426](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105426)

## Data

Gene col 2602: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2602); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2602, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2602]; `tensor/DDL_lfc|DDL_z.npy` [2602]; `embed/gene_vectors.npy` [2602]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2602 or target_col == 2602). Every well: [[PTPRS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTPRS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
