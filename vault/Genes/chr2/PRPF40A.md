---
symbol: "PRPF40A"
type: "gene"
col: 12223
ensembl_id: "ENSG00000196504"
name: "pre-mRNA processing factor 40A"
location: "2q23.3"
module: 51
arm: "+"
pooled_cpm: 270.75
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 0
n_dd_up_clean: 15
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# PRPF40A

*pre-mRNA processing factor 40A* — 2q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.01× (z +16.6, q 0e+00, up in 48 of 48 measured lines) ⚠ cell-cycle shift, explains ~45% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.13× (z +13.1, q 6e-37, up in 47 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[ULK-101 (drug)]] 0.05 µM in 1 line (NCI-H2122 0.0561×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZFR]] (+0.69, fdr 7e-06), [[UBE3A]] (+0.68, fdr 7e-06), [[U2SURP]] (+0.63, fdr 1e-05); moves opposite to [[FAM118A]] (-0.52, fdr 8e-05), [[BAIAP3]] (-0.51, fdr 4e-05), [[ELK1]] (-0.50, fdr 4e-05).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 15 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12223.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **2.01×** | +16.6 | 0e+00 | 48/48 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.13×** | +13.1 | 6e-37 | 47/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +11.7 | 4e-29 | 45/49 (CFPAC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.99×** | +11.5 | 3e-28 | 48/48 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **1.81×** | +10.3 | 7e-23 | 47/49 (LS 180, SW480, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.85×** | +9.8 | 7e-21 | 43/45 (NCI-H460, NCI-H1792, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.75×** | +9.7 | 2e-20 | 46/48 (NCI-H1792, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **1.71×** | +9.0 | 2e-17 | 36/44 (SW480, Hs 766T, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.60×** | +8.1 | 3e-14 | 48/48 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.36×** | +7.8 | 4e-13 | 45/49 (LS 180, SW1417, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.56×** | +7.7 | 9e-13 | 45/48 (NCI-H460, LS 180, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.55×** | +7.6 | 2e-12 | 48/48 (PANC-1, HOP62, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | **1.54×** | +7.1 | 4e-11 | 41/47 (COLO 205, LoVo, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.50×** | +7.1 | 7e-11 | 43/48 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | **1.45×** | +6.5 | 3e-09 | 39/48 (NCI-H460, LS 180, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +6.2 | 2e-08 | 38/48 (MIA PaCa-2, SNU-423, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.89×** | +5.8 | 3e-07 | 34/48 (LS 180, SW1417, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.40×** | +5.5 | 1e-06 | 42/48 (HOP62, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +4.5 | 2e-04 | 26/48 (SW1417, A-172, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.28×** | +4.0 | 0.002 | 28/47 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.23×** | +3.6 | 0.007 | 25/48 (C32, A-172, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.31×** | +3.1 | 0.042 | 30/49 (SW1417, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Bendamustine (drug)]] 5 µM |  | 1.20× | +3.0 | 0.055 | 22/48 (NCI-H1792, J82, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12223.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[ULK-101 (drug)]] 0.05 µM in 1 line (NCI-H2122 0.0561×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.820× | -3.4 | 0.36 | 27/48 (HEC-1-A, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, +0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12223. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 301 | 14 (11 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.99× (z +15.0) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +12.6) | — |
| [[PANC-1 (line)]] | alt | 273 | 13 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +18.6) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.51× (z +13.9) | — |
| [[LoVo (line)]] | wt | 281 | 10 (8 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.38× (z +12.5) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 1.90× (z +9.3) | — |
| [[LS 180 (line)]] | wt | 273 | 10 (6 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.74× (z +14.9) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.01× (z +10.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 348 | 10 (6 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.77× (z +16.5) | — |
| [[NCI-H1792 (line)]] | alt | 170 | 8 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +20.5) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.07× (z +12.5) | — |
| [[A549 (line)]] | wt | 259 | 7 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +17.6) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.92× (z +12.8) | — |
| [[HOP62 (line)]] | alt | 202 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +15.9) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.75× (z +12.5) | — |
| [[SNU-423 (line)]] | alt | 179 | 7 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +15.5) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +12.3) | — |
| [[SW480 (line)]] | alt | 323 | 7 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.14× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 1.87× (z +10.5) | — |
| [[A498 (line)]] | wt | 404 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +16.3) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.25× (z +11.3) | — |
| [[COLO 205 (line)]] | alt | 182 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +12.2) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.26× (z +9.3) | — |
| [[HS-578T (line)]] | alt | 190 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +14.5) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.54× (z +11.2) | — |
| [[HT-29 (line)]] | alt | 256 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +15.1) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.00× (z +13.0) | — |
| [[LOX-IMVI (line)]] | wt | 267 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +13.0) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.35× (z +11.6) | — |
| [[SK-MEL-2 (line)]] | alt | 221 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +14.3) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.26× (z +9.9) | — |
| [[SW 900 (line)]] | alt | 289 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +13.8) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.89× (z +10.6) | — |
| [[AsPC-1 (line)]] | alt | 286 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +16.6) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.35× (z +15.4) | — |
| [[C32 (line)]] | wt | 175 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +15.5) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.85× (z +12.3) | — |
| [[HEC-1-A (line)]] | alt | 275 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +14.4) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.75× (z +11.5) | — |
| [[HepG2_C3A (line)]] | wt | 337 | 5 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.87× (z +12.3) | — |
| [[Hs 766T (line)]] | wt | 194 | 5 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +13.0) | — |
| [[KATO III (line)]] | alt | 232 | 5 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.69× (z +13.4) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.14× (z +10.3) | — |
| [[RPMI-7951 (line)]] | alt | 265 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +13.4) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +11.5) | — |
| [[SW1417 (line)]] | alt | 371 | 5 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.93× (z +16.0) | — |
| [[A-172 (line)]] | wt | 267 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +12.5) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.07× (z +10.0) | — |
| [[H4 (line)]] | wt | 204 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +13.3) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.89× (z +11.6) | — |
| [[NCI-H1573 (line)]] | alt | 140 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +17.8) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.75× (z +13.2) | — |
| [[NCI-H2030 (line)]] | alt | 394 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +13.5) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.03× (z +10.4) | — |
| [[CFPAC-1 (line)]] | alt | 136 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.81× (z +17.3) | — |
| [[Panc 03.27 (line)]] | alt | 281 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +14.0) | — |
| [[A-427 (line)]] | wt | 282 | 2 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 2.07× (z +9.5) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[HCT15 (line)]] | alt | 322 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +10.1) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.91× (z +9.1) | — |
| [[hTERT-HPNE (line)]] | wt | 185 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +12.2) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.54× (z +9.2) | — |
| [[J82 (line)]] | alt | 311 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.84× (z +11.2) | — |
| [[NCI-H23 (line)]] | alt | 359 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +13.3) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.23× (z +10.9) | — |
| [[NCI-H2347 (line)]] | alt | 214 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.69× (z +10.5) | — |
| [[SNU-1 (line)]] | wt | 278 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +10.3) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.88× (z +8.7) | — |
| [[BT-474 (line)]] | alt | 281 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.59× (z +8.6) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[CHP-212 (line)]] | wt | 313 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +8.5) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[NCI-H2122 (line)]] | alt | 227 | 0 | 1 | — | [[ULK-101 (drug)]] 0.05 µM 0.0561× (z -10.3) |
| [[SHP-77 (line)]] | alt | 157 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.07× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | — |
| [[SW48 (line)]] | wt | 316 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +10.4) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[AN3 CA (line)]] | alt | 333 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 344 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 261 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 413 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 379 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 240 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 327 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12223), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFR]] | +0.69 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[UBE3A]] | +0.68 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[U2SURP]] | +0.63 | +0.67 / +0.55 | both halves | 1e-05 | same gene group; pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 927 |
| [[MTIF2]] | +0.63 | +0.73 / +0.49 | both halves | 1e-05 |  |
| [[ATRX]] | +0.63 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[THOC7]] | +0.62 | +0.69 / +0.55 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[TLK2]] | +0.61 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[DNAJC8]] | +0.60 | +0.68 / +0.52 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 875 |
| [[SNW1]] | +0.59 | +0.67 / +0.47 | both halves | 2e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 524 |
| [[USP47]] | +0.58 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[ZMAT2]] | +0.57 | +0.69 / +0.39 | both halves | 5e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 540 |
| [[CHD6]] | +0.57 | +0.52 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM118A]] | -0.52 | -0.57 / -0.37 | both halves | 8e-05 |  |
| [[BAIAP3]] | -0.51 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[ELK1]] | -0.50 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[CABLES2]] | -0.50 | -0.50 / -0.37 | both halves | 8e-05 |  |
| [[B4GALT3]] | -0.50 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[KYAT1]] | -0.50 | -0.57 / -0.37 | both halves | 9e-05 |  |
| [[ADIPOR1]] | -0.50 | -0.63 / -0.31 | both halves | 2e-04 |  |
| [[FCHO1]] | -0.49 | -0.51 / -0.31 | both halves | 2e-04 |  |
| [[TXNL4A]] | -0.48 | -0.47 / -0.35 | both halves | 1e-04 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[GGCX]] | -0.48 | -0.51 / -0.36 | both halves | 1e-04 |  |
| [[PLPPR2]] | -0.48 | -0.38 / -0.41 | both halves | 7e-05 |  |
| [[MCRIP1]] | -0.47 | -0.49 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PRPF40A's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[FCHO1]] | B | FCHO1 activity raises PRPF40A's level | lines that do not express FCHO1 (5) vs lines expressing it (45) | 1.36× lower at baseline in the lines without FCHO1 | 0.056 | ⚠ within organs, on part of the lines; also absent: AMOTL2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.412). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-21.8, 8.9); signed map (11.2, -32.7). **Vector** length 84.7, 37.5% of its response variance represented; |z| ≥ 3 in 1,225 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.8 | +7.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +11.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +6.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.6 | +9.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.4 | +13.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.1 | +4.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.0 | +7.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.7 | -0.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.6 | +0.5 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -7.3 | -0.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.7 | +2.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | +1.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | -4.3 | +6.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.2 | +3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.7 | -2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.3 | +3.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.3 | -1.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.1 | -0.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.9 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | pre-mRNA processing factor 40A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q23.3 — chr2:152,651,593-152,718,012 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20585, FBP11, HYPA, NY-REN-6, HIP10, FBP-11, FLAF1, Prp40; previously FNBP3 |
| Gene groups (HGNC) | Spliceosomal A complex |
| Reactome | 6 pathways, smallest: mRNA Polyadenylation; mRNA 3'-end processing; mRNA Splicing - Major Pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [O75400](https://www.uniprot.org/uniprotkb/O75400) (Pre-mRNA-processing factor 40 homolog A):

> Binds to WASL/N-WASP and suppresses its translocation from the nucleus to the cytoplasm, thereby inhibiting its cytoplasmic function (By similarity). Plays a role in the regulation of cell morphology and cytoskeletal organization. Required in the control of cell shape and migration. May play a role in cytokinesis. May be involved in pre-mRNA splicing.

**Summary**, from NCBI Gene [55660](https://www.ncbi.nlm.nih.gov/gene/55660):

> Enables RNA binding activity. Predicted to be involved in mRNA splicing, via spliceosome. Located in nuclear matrix and nuclear speck. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:16463](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16463) · Entrez [55660](https://www.ncbi.nlm.nih.gov/gene/55660) · UniProt [O75400](https://www.uniprot.org/uniprotkb/O75400) · Ensembl [ENSG00000196504](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196504)

## Data

Gene col 12223: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12223); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12223, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12223]; `tensor/DDL_lfc|DDL_z.npy` [12223]; `embed/gene_vectors.npy` [12223]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12223 or target_col == 12223). Every well: [[PRPF40A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRPF40A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
