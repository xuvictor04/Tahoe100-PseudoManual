---
symbol: "EYA1"
type: "gene"
col: 2437
ensembl_id: "ENSG00000104313"
name: "EYA transcriptional coactivator and phosphatase 1"
location: "8q13.3"
module: 152
arm: "+"
pooled_cpm: 33.65
n_lines_expressing: 21
n_dd_up: 14
n_dd_down: 23
n_dd_up_clean: 12
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 14
direction_downstream: 5
tags: ["gene", "module/152"]
generated_by: "tahoemap"
---

# EYA1

*EYA transcriptional coactivator and phosphatase 1* — 8q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.03× (z +13.2, q 9e-37, up in 10 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.654× (z -5.3, q 6e-05, down in 15 of 19 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IGFBP5]] (+0.66, fdr 7e-06), [[EPHA3]] (+0.64, fdr 1e-05), [[MLLT3]] (+0.60, fdr 1e-05); moves opposite to [[SLC16A5]] (-0.48, fdr 4e-05), [[BCL2L1]] (-0.47, fdr 6e-05), [[NUTM2A-AS1]] (-0.47, fdr 4e-05).
> It is in [[Module 152]], a single-armed module (Retinoid metabolism and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[ZNF439]] → it (grade B ⚠); 5 go from it, the strongest it → [[VWA5A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2437.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.03×** | +13.2 | 9e-37 | 10/19 (NCI-H2347, CFPAC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.81×** | +7.8 | 1e-12 | 8/19 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[NG25 (drug)]] 5 µM |  | **2.64×** | +6.7 | 5e-09 | 14/18 (LOX-IMVI, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.53×** | +5.6 | 3e-06 | 0/19 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +4.9 | 9e-05 | 0/19 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 0.5 µM |  | **1.36×** | +4.1 | 0.004 | 0/19 | rises with dose | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.37×** | +4.0 | 0.005 | 12/18 (LOX-IMVI, HOP62, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.33×** | +3.8 | 0.012 | 7/19 (C32, PANC-1, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.32×** | +3.7 | 0.013 | 6/19 (NCI-H2030, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **1.34×** | +3.7 | 0.013 | 2/19 (PANC-1, NCI-H2030) | rises with dose | position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.25×** | +3.5 | 0.026 | 6/19 (HOP62, LOX-IMVI, …) | two highest doses | noisy plate (z scaled) |
| [[Ixazomib (drug)]] 5 µM |  | **1.58×** | +3.2 | 0.075 | 7/19 (C32, NCI-H2030, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.27×** | +3.1 | 0.090 | 0/16 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.26×** | +3.1 | 0.090 | 13/19 (HOP62, LOX-IMVI, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2437.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.654×** | -5.3 | 6e-05 | 15/19 (SW 900, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.675×** | -5.1 | 8e-05 | 11/19 (C32, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.679×** | -5.1 | 8e-05 | 14/19 (SK-MEL-2, SW 900, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.688×** | -4.9 | 1e-04 | 11/19 (C32, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.704×** | -4.6 | 4e-04 | 12/19 (SK-MEL-2, CFPAC-1, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.705×** | -4.6 | 4e-04 | 12/19 (H4, HOP62, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.781×** | -4.6 | 4e-04 | 16/19 (HOP62, SK-MEL-2, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.717×** | -4.3 | 1e-03 | 8/19 (HOP62, H4, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.795×** | -4.2 | 0.001 | 10/19 (NCI-H2347, Panc 03.27, …) | rises with dose |  |
| [[Budesonide (drug)]] 5 µM |  | **0.725×** | -4.2 | 0.002 | 12/19 (NCI-H2347, Panc 03.27, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.726×** | -4.2 | 0.002 | 10/19 (NCI-H1573, NCI-H2347, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.799×** | -4.1 | 0.002 | 13/20 (SK-MEL-2, CFPAC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.740×** | -3.9 | 0.004 | 13/19 (PANC-1, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.741×** | -3.9 | 0.004 | 12/19 (SK-MEL-2, CFPAC-1, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.733×** | -3.9 | 0.004 | 12/19 (NCI-H2347, HOP62, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 5 µM |  | **0.809×** | -3.9 | 0.004 | 7/20 (C32, SK-MEL-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2437. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 225 | 0 | 17 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.227× (z -15.5) |
| [[SW 900 (line)]] | alt | 192 | 0 | 14 (10 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.163× (z -17.5) |
| [[C32 (line)]] | wt | 318 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -19.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.143× (z -19.2) |
| [[HOP62 (line)]] | alt | 141 | 1 (1 ⚠) | 9 (5 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.69× (z +10.0) ⚠ position not correctable | [[Dinaciclib (drug)]] 0.5 µM 0.100× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.203× (z -12.4) |
| [[RPMI-7951 (line)]] | alt | 224 | 0 | 10 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0394× (z -21.1) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.140× (z -12.4) |
| [[H4 (line)]] | wt | 254 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -14.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.184× (z -13.8) |
| [[AN3 CA (line)]] | alt | 230 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0386× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.148× (z -9.9) |
| [[LOX-IMVI (line)]] | wt | 115 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0114× (z -21.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.251× (z -9.9) |
| [[LS 180 (line)]] | wt | 20.7 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.81× (z +13.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.97× (z +9.1) | — |
| [[CHP-212 (line)]] | wt | 183 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0459× (z -14.3) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 67.6 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0623× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.227× (z -12.0) |
| [[NCI-H2347 (line)]] | alt | 20.3 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 3.54× (z +11.5) | — |
| [[CFPAC-1 (line)]] | alt | 14.0 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.54× (z +11.1) | — |
| [[NCI-H1573 (line)]] | alt | 9.57 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.84× (z +8.6) | — |
| [[NCI-H2030 (line)]] | alt | 15.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0964× (z -10.6) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 13.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +9.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SHP-77 (line)]] | alt | 32.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 2.87 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 3.07 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 4.62 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.59 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.24 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.88 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.91 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.01 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.40 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.97 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.10 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.26 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.13 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.02 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.34 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 5.40 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.85 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 5.09 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.83 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 5.01 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 50.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.46 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.31 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.11 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.67 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 6.26 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.17 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.82 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.61 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.31 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2437), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IGFBP5]] | +0.66 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[EPHA3]] | +0.64 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[MLLT3]] | +0.60 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[PFKFB4]] | +0.58 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[ZNF521]] | +0.57 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[ZNF331]] | +0.57 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[LRRC7]] | +0.56 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[NLGN1]] | +0.55 | +0.46 / +0.60 | both halves | 3e-05 |  |
| [[RAB30]] | +0.55 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[SNAP25]] | +0.55 | +0.36 / +0.57 | both halves | 1e-04 |  |
| [[MEF2C]] | +0.54 | +0.43 / +0.60 | both halves | 3e-05 |  |
| [[MDGA2]] | +0.53 | +0.49 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC16A5]] | -0.48 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[BCL2L1]] | -0.47 | -0.39 / -0.52 | both halves | 6e-05 |  |
| [[NUTM2A-AS1]] | -0.47 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[DGKH]] | -0.46 | -0.47 / -0.37 | both halves | 8e-05 |  |
| [[RBM19]] | -0.45 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[E2F3]] | -0.45 | -0.52 / -0.31 | both halves | 2e-04 |  |
| [[SLC20A2]] | -0.45 | -0.42 / -0.38 | both halves | 6e-05 |  |
| [[ENOX2]] | -0.45 | -0.47 / -0.37 | both halves | 8e-05 |  |
| [[NDUFAF2]] | -0.44 | -0.46 / -0.38 | both halves | 6e-05 |  |
| [[METTL8]] | -0.44 | -0.48 / -0.30 | both halves | 2e-04 |  |
| [[THSD4]] | -0.44 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[DHX34]] | -0.44 | -0.45 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 6, C 8. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF439]] | B | ZNF439 activity raises EYA1's level | lines that do not express ZNF439 (21) vs lines expressing it (29) | 2.80× lower at baseline in the lines without ZNF439 | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000267383, PPP2R2B, CSF1R |
| [[NR3C1]] | B | NR3C1 activity lowers EYA1's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 4.8% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |
| [[NRN1]] | B | NRN1 activity raises EYA1's level | lines that do not express NRN1 (27) vs lines expressing it (23) | 2.37× lower at baseline in the lines without NRN1 | 0.059 | ⚠ within organs, on part of the lines; also absent: ILDR2, PHACTR1, ENSG00000250137 |
| [[PLOD2]] | B | PLOD2 activity raises EYA1's level | lines that do not express PLOD2 (15) vs lines expressing it (35) | 4.73× lower at baseline in the lines without PLOD2 | 0.069 | ⚠ within organs, on part of the lines; also absent: ITGA1, TMEM92-AS1, RGS17 |
| [[CADM1]] | B | CADM1 activity raises EYA1's level | lines that do not express CADM1 (18) vs lines expressing it (32) | 2.29× lower at baseline in the lines without CADM1 | 0.078 | ⚠ within organs, on part of the lines; also absent: ARNT2-DT, BEND6, ARNT2 |
| [[MEF2C]] | B | MEF2C activity raises EYA1's level | lines that do not express MEF2C (14) vs lines expressing it (36) | 3.48× lower at baseline in the lines without MEF2C | 0.084 | ⚠ within organs, on part of the lines; also absent: MEF2C-AS1, RGS2, MYOSLID |
| [[EDIL3]] | C | EDIL3 activity raises EYA1's level | lines that do not express EDIL3 (28) vs lines expressing it (22) | 3.21× lower at baseline in the lines without EDIL3 | 0.007 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, ENSG00000232949, STAC; co-absent with the target |
| [[NOL4]] | C | NOL4 activity raises EYA1's level | lines that do not express NOL4 (30) vs lines expressing it (20) | 4.14× lower at baseline in the lines without NOL4 | 0.027 | ⚠ within organs, on part of the lines; also absent: KCTD8, ASXL3, DSCAM; maybe low, not absent; co-absent with the target |
| [[ST8SIA4]] | C | ST8SIA4 activity raises EYA1's level | lines that do not express ST8SIA4 (27) vs lines expressing it (23) | 5.01× lower at baseline in the lines without ST8SIA4 | 0.039 | ⚠ within organs, on part of the lines; also absent: ADGRB3, SEMA3E, TRPA1; co-absent with the target |
| [[ZNF521]] | C | ZNF521 activity raises EYA1's level | lines that do not express ZNF521 (27) vs lines expressing it (23) | 4.08× lower at baseline in the lines without ZNF521 | 0.060 | ⚠ within organs, on part of the lines; also absent: LEF1, SNAI2, ITGA4; co-absent with the target |
| [[NLGN1]] | C | NLGN1 activity raises EYA1's level | lines that do not express NLGN1 (30) vs lines expressing it (20) | 3.35× lower at baseline in the lines without NLGN1 | 0.064 | ⚠ within organs, on part of the lines; also absent: EPB41L3, PAX3, NEGR1; co-absent with the target |
| [[FKBP9P1-1]] | C | FKBP9P1-1 activity raises EYA1's level | lines that do not express FKBP9P1-1 (30) vs lines expressing it (20) | 4.16× lower at baseline in the lines without FKBP9P1-1 | 0.095 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000231317, ENSG00000253642, ENSG00000287622; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VWA5A]] | B | EYA1 activity raises VWA5A's level | lines that do not express EYA1 (29) vs lines expressing it (21) | 1.83× lower at baseline in the lines without EYA1 | 0.019 | ⚠ within organs, on part of the lines; also absent: ADAMTS3, ENSG00000233539, NAA11 |
| [[ZNF439]] | B | EYA1 activity raises ZNF439's level | lines that do not express EYA1 (29) vs lines expressing it (21) | 2.32× lower at baseline in the lines without EYA1 | 0.078 | ⚠ within organs, on part of the lines; also absent: ADAMTS3, ENSG00000233539, NAA11 |
| [[PLOD2]] | B | EYA1 activity raises PLOD2's level | lines that do not express EYA1 (29) vs lines expressing it (21) | 2.72× lower at baseline in the lines without EYA1 | 0.086 | ⚠ within organs, on part of the lines; also absent: ADAMTS3, ENSG00000233539, NAA11 |
| [[FAM13A]] | B | EYA1 activity raises FAM13A's level | lines that do not express EYA1 (29) vs lines expressing it (21) | 2.17× lower at baseline in the lines without EYA1 | 0.089 | ⚠ within organs, on part of the lines; also absent: ADAMTS3, ENSG00000233539, NAA11 |
| [[EDIL3]] | C | EYA1 activity raises EDIL3's level | lines that do not express EYA1 (29) vs lines expressing it (21) | 3.37× lower at baseline in the lines without EYA1 | 0.080 | ⚠ within organs, on part of the lines; also absent: ADAMTS3, ENSG00000233539, NAA11; co-absent with the target |

## Where it sits

- **Module**: [[Module 152]] — Retinoid metabolism and transport; 29 genes; every member is in the + arm (projection on the module's main direction 0.687). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (49.2, 28.6); signed map (31.3, 41.6). **Vector** length 85.3, 28.3% of its response variance represented; |z| ≥ 3 in 711 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.1 | +13.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.8 | +5.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.2 | +7.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +3.1 |
|  | [[NG25 (drug)]] 5 µM |  | +3.5 | +6.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | +3.1 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.2 | +3.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.2 | +4.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.1 | +1.1 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -3.0 | -3.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.5 | -3.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.4 | -4.2 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.3 | -4.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.2 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | EYA transcriptional coactivator and phosphatase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q13.3 — chr8:71,197,433-71,592,025 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously BOR |
| Gene groups (HGNC) | EYA transcriptional coactivator and phosphatases |
| Reactome | 6 pathways, smallest: Formation of the ureteric bud; Kidney development; Recruitment and ATM-mediated phosphorylation of repair and signaling proteins at DNA double strand breaks |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99502](https://www.uniprot.org/uniprotkb/Q99502) (Protein phosphatase EYA1):

> Functions both as protein phosphatase and as transcriptional coactivator for SIX1, and probably also for SIX2, SIX4 and SIX5 (By similarity). Tyrosine phosphatase that dephosphorylates 'Tyr-142' of histone H2AX (H2AXY142ph) and promotes efficient DNA repair via the recruitment of DNA repair complexes containing MDC1. 'Tyr-142' phosphorylation of histone H2AX plays a central role in DNA repair and acts as a mark that distinguishes between apoptotic and repair responses to genotoxic stress. Its …

**Summary**, from NCBI Gene [2138](https://www.ncbi.nlm.nih.gov/gene/2138):

> This gene encodes a member of the eyes absent (EYA) family of proteins. The encoded protein may play a role in the developing kidney, branchial arches, eye, and ear. Mutations of this gene have been associated with branchiootorenal dysplasia syndrome, branchiootic syndrome, and sporadic cases of congenital cataracts and ocular anterior segment anomalies. A similar protein in mice can act as a transcriptional activator. Alternatively spliced transcript variants have been identified for this …

**Accessions** — [HGNC:3519](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3519) · Entrez [2138](https://www.ncbi.nlm.nih.gov/gene/2138) · UniProt [Q99502](https://www.uniprot.org/uniprotkb/Q99502) · Ensembl [ENSG00000104313](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104313)

## Data

Gene col 2437: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2437); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2437, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2437]; `tensor/DDL_lfc|DDL_z.npy` [2437]; `embed/gene_vectors.npy` [2437]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2437 or target_col == 2437). Every well: [[EYA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EYA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
