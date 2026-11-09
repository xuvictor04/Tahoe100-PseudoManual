---
symbol: "ANO6"
type: "gene"
col: 10794
ensembl_id: "ENSG00000177119"
name: "anoctamin 6"
location: "12q12"
module: 13
arm: "+"
pooled_cpm: 328.28
n_lines_expressing: 49
n_dd_up: 1
n_dd_down: 23
n_dd_up_clean: 1
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# ANO6

*anoctamin 6* — 12q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 1.95× (z +5.7, q 7e-06, up in 35 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 7 lines (A549 2.39×, HT-29 2.01×, NCI-H23 2.04×, MIA PaCa-2 2.15×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[TAK-901 (drug)]] 5 µM in 6 lines (SNU-1 5.73×, PANC-1 5.22×, SW480 4.04×, HT-29 3.80×, …); [[Homoharringtonine (drug)]] 0.5 µM in 4 lines (MIA PaCa-2 3.18×, SW48 2.37×, A-427 2.20×, NCI-H23 2.06×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (SNU-1 2.43×).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.333× (z -17.9, q 0e+00, down in 47 of 47 measured lines).
> Its strongest partners by |cos| (89 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VCAN]] (+0.61, fdr 1e-05), [[LAMC1]] (+0.59, fdr 1e-05), [[PLEKHA8P1]] (+0.57, fdr 1e-04, ⚠ same locus), [[NID1]] (+0.54, fdr 2e-04); moves opposite to [[RSAD1]] (-0.58, fdr 5e-05), [[PDPR2P]] (-0.56, fdr 6e-04), [[ASB13]] (-0.52, fdr 1e-04).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10794.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 7 lines (A549 2.39×, HT-29 2.01×, NCI-H23 2.04×, MIA PaCa-2 2.15×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[TAK-901 (drug)]] 5 µM in 6 lines (SNU-1 5.73×, PANC-1 5.22×, SW480 4.04×, HT-29 3.80×, …); [[Homoharringtonine (drug)]] 0.5 µM in 4 lines (MIA PaCa-2 3.18×, SW48 2.37×, A-427 2.20×, NCI-H23 2.06×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (SNU-1 2.43×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **1.95×** | +5.7 | 7e-06 | 35/48 (SNU-1, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | 1.49× | +3.4 | 0.22 | 31/47 (COLO 205, SW480, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 10 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10794.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.333×** | -17.9 | 0e+00 | 47/47 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.344×** | -17.3 | 0e+00 | 47/47 (HOP62, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.415×** | -14.3 | 5e-44 | 47/47 (LOX-IMVI, HOP62, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.449×** | -12.5 | 1e-33 | 46/46 (RKO, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **0.676×** | -6.4 | 2e-08 | 32/48 (NCI-H1573, RKO, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.676×** | -6.3 | 2e-08 | 37/47 (A-172, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.762×** | -6.2 | 4e-08 | 29/48 (NCI-H1792, A549, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **0.675×** | -6.1 | 6e-08 | 32/43 (NCI-H1573, NCI-H23, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.691×** | -5.6 | 2e-06 | 33/44 (CFPAC-1, RKO, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.712×** | -5.5 | 2e-06 | 34/47 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.812×** | -4.8 | 9e-05 | 26/47 (LOX-IMVI, RPMI-7951, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.757×** | -4.5 | 3e-04 | 36/47 (HOP62, RPMI-7951, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.779×** | -4.1 | 0.002 | 32/47 (A-172, HOP62, …) | rises with dose |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.793×** | -3.8 | 0.007 | 27/47 (NCI-H1573, A498, …) | inconsistent across doses | position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.794×** | -3.7 | 0.007 | 29/47 (NCI-H1573, SNU-423, …) | inconsistent across doses |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **0.803×** | -3.6 | 0.013 | 33/47 (A-172, H4, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.814×** | -3.3 | 0.027 | 24/47 (LoVo, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.722×** | -3.1 | 0.059 | 33/47 (RPMI-7951, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.828×** | -3.1 | 0.062 | 23/47 (NCI-H1573, H4, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.816×** | -3.0 | 0.062 | 26/46 (C-33 A, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.876× | -3.0 | 0.062 | 11/47 (A549, PANC-1, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.736×** | -2.9 | 0.084 | 25/46 (SW48, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10794. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 580 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.171× (z -18.2) |
| [[NCI-H23 (line)]] | alt | 564 | 2 (1 ⚠) | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +13.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.06× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.298× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.379× (z -12.5) |
| [[CFPAC-1 (line)]] | alt | 376 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.262× (z -16.6) |
| [[NCI-H1573 (line)]] | alt | 473 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.201× (z -18.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.246× (z -17.2) |
| [[KATO III (line)]] | alt | 277 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.335× (z -14.7) |
| [[MIA PaCa-2 (line)]] | alt | 246 | 2 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.18× (z +13.1) | [[Panobinostat (drug)]] 5 µM 0.339× (z -12.2) |
| [[NCI-H1792 (line)]] | alt | 384 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.260× (z -18.0) |
| [[NCI-H460 (line)]] | wt | 313 | 2 (1 ⚠) | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.96× (z +9.5) | [[Panobinostat (drug)]] 0.5 µM 0.385× (z -12.7) |
| [[PANC-1 (line)]] | alt | 498 | 1 | 5 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.22× (z +10.4) | [[Panobinostat (drug)]] 0.5 µM 0.302× (z -14.5) |
| [[SW 900 (line)]] | alt | 284 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.309× (z -14.7) |
| [[SW480 (line)]] | alt | 365 | 1 | 5 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.04× (z +10.0) | [[Panobinostat (drug)]] 0.5 µM 0.249× (z -19.1) |
| [[A-172 (line)]] | wt | 375 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.300× (z -16.1) |
| [[A549 (line)]] | wt | 397 | 1 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +14.3) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.291× (z -14.3) |
| [[H4 (line)]] | wt | 409 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.203× (z -14.6) |
| [[HEC-1-A (line)]] | alt | 339 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.300× (z -17.5) |
| [[HepG2_C3A (line)]] | wt | 432 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.323× (z -12.9) |
| [[HOP62 (line)]] | alt | 288 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.223× (z -18.4) |
| [[Hs 766T (line)]] | wt | 357 | 1 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +10.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.283× (z -15.1) |
| [[HS-578T (line)]] | alt | 340 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.231× (z -15.2) |
| [[HT-29 (line)]] | alt | 214 | 2 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +13.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.80× (z +9.6) | [[Panobinostat (drug)]] 0.5 µM 0.384× (z -13.1) |
| [[J82 (line)]] | alt | 375 | 1 | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.79× (z +8.8) | [[Panobinostat (drug)]] 0.5 µM 0.246× (z -17.9) |
| [[RKO (line)]] | wt | 429 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.253× (z -18.1) |
| [[C-33 A (line)]] | alt | 208 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.325× (z -14.4) |
| [[hTERT-HPNE (line)]] | wt | 433 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.217× (z -13.2) |
| [[LoVo (line)]] | wt | 300 | 0 | 4 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.485× (z -9.9) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.508× (z -9.7) |
| [[Panc 03.27 (line)]] | alt | 354 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.319× (z -13.7) |
| [[RPMI-7951 (line)]] | alt | 375 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.271× (z -14.8) |
| [[SNU-423 (line)]] | alt | 342 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.244× (z -16.1) |
| [[SW48 (line)]] | wt | 248 | 2 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +12.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.37× (z +10.0) | [[Panobinostat (drug)]] 0.5 µM 0.368× (z -11.5) |
| [[BT-474 (line)]] | alt | 187 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +11.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Lonafarnib (drug)]] 5 µM 0.0913× (z -13.7) ⚠ toxic |
| [[CHP-212 (line)]] | wt | 309 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.240× (z -12.4) |
| [[LS 180 (line)]] | wt | 240 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.404× (z -12.0) |
| [[NCI-H2347 (line)]] | alt | 290 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.303× (z -12.5) |
| [[SNU-1 (line)]] | wt | 239 | 3 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 2.76× (z +12.1) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.73× (z +10.9) | — |
| [[SW 1271 (line)]] | alt | 498 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.190× (z -10.2) |
| [[A498 (line)]] | wt | 225 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.431× (z -10.9) |
| [[AsPC-1 (line)]] | alt | 315 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.417× (z -10.4) |
| [[C32 (line)]] | wt | 361 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.388× (z -9.9) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.439× (z -8.9) |
| [[COLO 205 (line)]] | alt | 201 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.378× (z -10.4) |
| [[NCI-H2030 (line)]] | alt | 297 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.470× (z -9.3) |
| [[SHP-77 (line)]] | alt | 141 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.396× (z -11.3) |
| [[SK-MEL-2 (line)]] | alt | 241 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.368× (z -11.9) |
| [[A-427 (line)]] | wt | 154 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.20× (z +9.4) | — |
| [[SW 1088 (line)]] | alt | 491 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.212× (z -9.2) |
| [[AN3 CA (line)]] | alt | 351 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 26.6 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 332 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 312 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 157 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 185 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10794), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 5 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VCAN]] | +0.61 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[LAMC1]] | +0.59 | +0.49 / +0.68 | both halves | 1e-05 |  |
| [[PLEKHA8P1]] | +0.57 | +0.48 / +0.32 | both halves | 1e-04 | ⚠ same locus (41.3 kb: neighbours can correlate without regulation) |
| [[NID1]] | +0.54 | +0.29 / +0.53 | both halves | 2e-04 |  |
| [[SSPN]] | +0.54 | +0.29 / +0.49 | both halves | 3e-04 |  |
| [[CYFIP1]] | +0.53 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[PRSS23]] | +0.53 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[ATP7A]] | +0.52 | +0.38 / +0.51 | both halves | 6e-05 | pathway: Ion channel transport |
| [[SMAD3]] | +0.51 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[TUG1]] | +0.51 | +0.21 / +0.54 | both halves | 7e-04 |  |
| [[ANAPC1P4]] | +0.51 | +0.42 / +0.49 | both halves | 4e-05 |  |
| [[HIVEP2-DT]] | +0.51 | +0.25 / +0.52 | both halves | 4e-04 |  |
| [[KIAA1217]] | +0.50 | +0.41 / +0.52 | both halves | 4e-05 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 8 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RSAD1]] | -0.58 | -0.40 / -0.64 | both halves | 5e-05 |  |
| [[PDPR2P]] | -0.56 | -0.22 / -0.53 | both halves | 6e-04 |  |
| [[ASB13]] | -0.52 | -0.33 / -0.59 | both halves | 1e-04 |  |
| [[MRPL34]] | -0.52 | -0.27 / -0.58 | both halves | 3e-04 |  |
| [[TADA1]] | -0.52 | -0.23 / -0.54 | both halves | 5e-04 |  |
| [[E4F1]] | -0.52 | -0.32 / -0.46 | both halves | 2e-04 |  |
| [[CDK5RAP1]] | -0.52 | -0.25 / -0.58 | both halves | 4e-04 |  |
| [[ZFAND4]] | -0.51 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[CCZ1P1]] | -0.50 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[SLC2A11]] | -0.49 | -0.45 / -0.59 | both halves | 3e-05 |  |
| [[CCT6P3-1]] | -0.49 | -0.28 / -0.40 | both halves | 3e-04 |  |
| [[TFB2M]] | -0.49 | -0.27 / -0.43 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.388). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (38.2, 7.5); signed map (-5.8, 36.5). **Vector** length 100, 36.6% of its response variance represented; |z| ≥ 3 in 1,375 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +5.6 | +0.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.6 | +2.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +4.9 | -6.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.2 | +5.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | +3.8 | -6.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | -1.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.3 | +0.8 |
|  | [[Lumateperone (tosylate) (drug)]] 0.5 µM |  | +2.0 | +1.5 |
|  | [[Busulfan (drug)]] 5 µM |  | +1.9 | +1.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.8 | +2.1 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.0 | -12.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -4.0 | -6.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.7 | -3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.0 | -4.8 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -2.9 | -3.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.7 | -1.7 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.7 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | anoctamin 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q12 — chr12:45,215,987-45,482,280 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp313M0720; previously TMEM16F |
| Gene groups (HGNC) | Anoctamins |
| Reactome | 16 pathways, smallest: Amplification and propagation of coagulation cascade; Induction of Cell-Cell Fusion; Defects of Coagulation cascade |
| Matched by | ensembl_id |

**Function**, from UniProt [Q4KMQ2](https://www.uniprot.org/uniprotkb/Q4KMQ2) (Anoctamin-6):

> Small-conductance calcium-activated nonselective cation (SCAN) channel which acts as a regulator of phospholipid scrambling in platelets and osteoblasts. Phospholipid scrambling results in surface exposure of phosphatidylserine which in platelets is essential to trigger the clotting system whereas in osteoblasts is essential for the deposition of hydroxyapatite during bone mineralization (By similarity). Has calcium-dependent phospholipid scramblase activity; scrambles phosphatidylserine, …

**Summary**, from NCBI Gene [196527](https://www.ncbi.nlm.nih.gov/gene/196527):

> This gene encodes a multi-pass transmembrane protein that belongs to the anoctamin family. This protein is an essential component for the calcium-dependent exposure of phosphatidylserine on the cell surface. The scrambling of phospholipid occurs in various biological systems, such as when blood platelets are activated, they expose phosphatidylserine to trigger the clotting system. Mutations in this gene are associated with Scott syndrome. Alternatively spliced transcript variants encoding …

**Accessions** — [HGNC:25240](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25240) · Entrez [196527](https://www.ncbi.nlm.nih.gov/gene/196527) · UniProt [Q4KMQ2](https://www.uniprot.org/uniprotkb/Q4KMQ2) · Ensembl [ENSG00000177119](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177119)

## Data

Gene col 10794: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10794); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10794, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10794]; `tensor/DDL_lfc|DDL_z.npy` [10794]; `embed/gene_vectors.npy` [10794]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10794 or target_col == 10794). Every well: [[ANO6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANO6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
