---
symbol: "SET"
type: "gene"
col: 4056
ensembl_id: "ENSG00000119335"
name: "SET nuclear proto-oncogene"
location: "9q34.11"
module: 18
arm: "+"
pooled_cpm: 313.65
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 0
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# SET

*SET nuclear proto-oncogene* — 9q34.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.66× (z +18.2, q 0e+00, up in 49 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.70× (z +6.3, q 5e-08, up in 43 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.491×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NCL]] (+0.65, fdr 9e-06), [[ANP32B]] (+0.55, fdr 3e-05), [[PAK2]] (+0.54, fdr 3e-05); moves opposite to [[LINC00888-1]] (-0.48, fdr 4e-05), [[RAB24]] (-0.44, fdr 2e-04), [[JMJD6]] (-0.43, fdr 2e-04).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 10 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4056.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.66×** | +18.2 | 0e+00 | 49/49 (KATO III, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.48×** | +17.0 | 0e+00 | 44/44 (KATO III, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.84×** | +11.4 | 8e-28 | 45/45 (SNU-423, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.70×** | +6.3 | 5e-08 | 43/48 (A-172, MIA PaCa-2, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **1.69×** | +6.2 | 7e-08 | 46/48 (NCI-H460, SW480, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.65×** | +5.7 | 1e-06 | 44/47 (CFPAC-1, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~42% of this change | **1.58×** | +5.2 | 2e-05 | 41/47 (C32, NCI-H1792, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~56% of this change | **1.52×** | +5.0 | 5e-05 | 45/48 (HT-29, BT-474, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **1.47×** | +4.5 | 4e-04 | 37/48 (KATO III, NCI-H460, …) | rises with dose | composition shift |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.32×** | +3.2 | 0.070 | 35/47 (HOP62, A-172, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.31×** | +3.2 | 0.070 | 29/48 (NCI-H460, SW480, …) | rises with dose | position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | **1.31×** | +3.1 | 0.095 | 29/48 (MIA PaCa-2, A549, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **1.20×** | +3.1 | 0.099 | 27/48 (KATO III, RKO, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.05 µM |  | 1.32× | +3.0 | 0.11 | 33/48 (NCI-H460, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4056.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.491×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM |  | 0.739× | -3.6 | 0.17 | 38/49 (KATO III, SW1417, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[GSK1059615 (drug)]] 5 µM |  | 0.575× | -3.4 | 0.17 | 40/49 (BT-474, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.812× | -3.3 | 0.19 | 31/48 (COLO 205, C-33 A, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.832× | -3.1 | 0.26 | 24/48 (KATO III, SW1417, …) | rises with dose |  |
| [[Baicalin (drug)]] 5 µM |  | 0.834× | -3.0 | 0.26 | 23/49 (LS 180, Panc 03.27, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4056. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 270 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.35× (z +17.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.36× (z +8.7) | — |
| [[A-427 (line)]] | wt | 315 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.86× (z +12.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.491× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 168 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.87× (z +12.2) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 364 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.95× (z +18.4) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 290 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.18× (z +11.4) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 236 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.89× (z +16.0) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 345 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.93× (z +16.8) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 284 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.44× (z +16.9) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 162 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.89× (z +13.5) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 474 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.83× (z +14.4) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 232 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.85× (z +17.4) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 167 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.50× (z +15.2) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 310 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.06× (z +17.2) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 239 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.59× (z +14.5) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 564 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.43× (z +15.9) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 256 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.02× (z +15.9) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 321 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.39× (z +14.9) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 250 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.85× (z +16.1) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 496 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.72× (z +14.2) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 175 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.88× (z +17.0) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 198 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.70× (z +12.6) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 340 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.63× (z +15.6) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 286 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.71× (z +15.5) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 318 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.88× (z +16.5) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 194 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.33× (z +13.5) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 160 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.66× (z +13.8) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 347 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +13.7) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 430 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.81× (z +17.2) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 444 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.30× (z +11.6) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 406 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.01× (z +9.5) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 369 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.61× (z +9.4) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 276 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.96× (z +14.0) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 411 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.74× (z +13.4) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 226 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.96× (z +13.1) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 260 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.82× (z +13.0) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 128 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.05× (z +14.4) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 371 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.72× (z +12.9) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 257 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.48× (z +12.4) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 368 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.13× (z +12.4) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 227 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.05× (z +10.7) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 177 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.14× (z +14.5) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 411 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.80× (z +12.7) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 656 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.43× (z +8.6) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 370 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.08× (z +10.5) ⚠ toxic; transcription drop | — |
| [[SW 1271 (line)]] | alt | 376 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.86× (z +9.9) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 559 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 213 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 290 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 351 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 177 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4056), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCL]] | +0.65 | +0.68 / +0.57 | both halves | 9e-06 | STRING 704 |
| [[ANP32B]] | +0.55 | +0.45 / +0.62 | both halves | 3e-05 | STRING 462 |
| [[PAK2]] | +0.54 | +0.61 / +0.44 | both halves | 3e-05 |  |
| [[GSPT1]] | +0.54 | +0.61 / +0.43 | both halves | 3e-05 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[HNRNPU]] | +0.53 | +0.59 / +0.51 | both halves | 1e-05 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 404 |
| [[YBX1]] | +0.52 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[ZC3HAV1L]] | +0.52 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[HMGB1]] | +0.51 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[EIF3A]] | +0.50 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[IPO5]] | +0.48 | +0.51 / +0.39 | both halves | 5e-05 |  |
| [[HDAC2]] | +0.48 | +0.53 / +0.34 | both halves | 1e-04 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[RCN1]] | +0.48 | +0.54 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00888-1]] | -0.48 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[RAB24]] | -0.44 | -0.40 / -0.32 | both halves | 2e-04 |  |
| [[JMJD6]] | -0.43 | -0.47 / -0.29 | both halves | 2e-04 |  |
| [[ACAP1]] | -0.43 | -0.29 / -0.41 | both halves | 3e-04 |  |
| [[DYNLT1]] | -0.43 | -0.32 / -0.36 | both halves | 2e-04 |  |
| [[POLR2C]] | -0.42 | -0.43 / -0.37 | both halves | 9e-05 |  |
| [[AMZ2P1-1]] | -0.42 | -0.30 / -0.39 | both halves | 2e-04 |  |
| [[TBC1D10A]] | -0.41 | -0.40 / -0.39 | both halves | 5e-05 |  |
| [[PELO]] | -0.41 | -0.41 / -0.34 | both halves | 1e-04 |  |
| [[HMSD]] | -0.41 | -0.34 / -0.41 | both halves | 1e-04 |  |
| [[TMCC2]] | -0.40 | -0.29 / -0.45 | both halves | 2e-04 |  |
| [[TNFSF9]] | -0.40 | -0.24 / -0.50 | both halves | 4e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.379). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-31.8, -30.3); signed map (-22.5, -51.2). **Vector** length 74.5, 33.6% of its response variance represented; |z| ≥ 3 in 919 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~75% of this change | +2.7 | +3.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | +2.2 | +4.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +6.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.9 | -0.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.9 | +2.9 |
|  | [[Adenosine (drug)]] 0.5 µM |  | +1.7 | -0.7 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | +1.5 | +0.1 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | -1.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.7 | +18.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -4.3 | -0.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.2 | +17.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.7 | -3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -3.1 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -3.3 | +2.0 |
|  | [[Thymol (drug)]] 0.5 µM |  | -3.1 | -0.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -3.1 | +0.9 |

## What is on record

|  |  |
|---|---|
| Name | SET nuclear proto-oncogene |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.11 — chr9:128,683,424-128,696,400 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PHAPII, 2PP2A, IPP2A2, TAF-IBETA, IGAAD, TAF-I |
| Gene groups (HGNC) | INHAT complex; SET complex; Nucleosome assembly protein superfamily |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 8 pathways, smallest: HuR (ELAVL1) binds and stabilizes mRNA; Condensation of Prophase Chromosomes; Regulation of mRNA stability by proteins that bind AU-rich elements |
| Matched by | ensembl_id |

**Function**, from UniProt [Q01105](https://www.uniprot.org/uniprotkb/Q01105) (Protein SET):

> Multitasking protein, involved in apoptosis, transcription, nucleosome assembly and histone chaperoning. Isoform 2 anti-apoptotic activity is mediated by inhibition of the GZMA-activated DNase, NME1. In the course of cytotoxic T-lymphocyte (CTL)-induced apoptosis, GZMA cleaves SET, disrupting its binding to NME1 and releasing NME1 inhibition. Isoform 1 and isoform 2 are potent inhibitors of protein phosphatase 2A. Isoform 1 and isoform 2 inhibit EP300/CREBBP and PCAF-mediated acetylation of …

**Summary**, from NCBI Gene [6418](https://www.ncbi.nlm.nih.gov/gene/6418):

> The protein encoded by this gene inhibits acetylation of nucleosomes, especially histone H4, by histone acetylases (HAT). This inhibition is most likely accomplished by masking histone lysines from being acetylated, and the consequence is to silence HAT-dependent transcription. The encoded protein is part of a complex localized to the endoplasmic reticulum but is found in the nucleus and inhibits apoptosis following attack by cytotoxic T lymphocytes. This protein can also enhance DNA …

**Accessions** — [HGNC:10760](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10760) · Entrez [6418](https://www.ncbi.nlm.nih.gov/gene/6418) · UniProt [Q01105](https://www.uniprot.org/uniprotkb/Q01105) · Ensembl [ENSG00000119335](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119335)

## Data

Gene col 4056: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4056); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4056, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4056]; `tensor/DDL_lfc|DDL_z.npy` [4056]; `embed/gene_vectors.npy` [4056]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4056 or target_col == 4056). Every well: [[SET — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SET.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
