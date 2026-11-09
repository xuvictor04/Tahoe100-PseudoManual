---
symbol: "NDUFA5"
type: "gene"
col: 4905
ensembl_id: "ENSG00000128609"
name: "NADH:ubiquinone oxidoreductase subunit A5"
location: "7q31.32"
module: 28
arm: "+"
pooled_cpm: 46.12
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 1
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# NDUFA5

*NADH:ubiquinone oxidoreductase subunit A5* — 7q31.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.05× (z +17.7, q 0e+00, up in 45 of 48 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.05× (z +12.5, q 5e-34, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.890× (z -6.9, q 4e-09, down in 3 of 49 measured lines) ⚠ position not correctable.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (C32 0.403×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COPS5]] (+0.76, fdr 7e-06), [[CLK4]] (+0.73, fdr 7e-06), [[SCRN3]] (+0.73, fdr 7e-06); moves opposite to [[MAD1L1]] (-0.69, fdr 1e-05), [[CORO7]] (-0.68, fdr 7e-06), [[AXIN1]] (-0.68, fdr 7e-06).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[STRIP2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 8 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4905.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.05×** | +17.7 | 0e+00 | 45/48 (A-172, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.69×** | +17.3 | 0e+00 | 48/48 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.51×** | +15.4 | 0e+00 | 35/38 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.20×** | +12.7 | 5e-35 | 40/42 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.05×** | +12.5 | 5e-34 | 43/48 (A-172, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.98×** | +11.5 | 2e-28 | 41/48 (RKO, NCI-H1573, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.29×** | +7.6 | 3e-12 | 41/49 (LoVo, LS 180, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.53×** | +7.4 | 1e-11 | 36/48 (C32, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.34×** | +7.2 | 3e-11 | 38/48 (A-427, KATO III, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.35×** | +5.3 | 8e-06 | 31/48 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.26×** | +4.1 | 0.002 | 25/48 (NCI-H23, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.27×** | +4.1 | 0.002 | 23/47 (RKO, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~79% of this change | **1.23×** | +3.6 | 0.015 | 23/47 (RPMI-7951, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.21×** | +3.2 | 0.063 | 18/47 (C32, LoVo, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.41×** | +3.1 | 0.066 | 12/47 (A-427, AsPC-1, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Ixazomib (drug)]] 0.05 µM |  | 1.20× | +3.0 | 0.097 | 15/47 (LoVo, LOX-IMVI, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4905.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (C32 0.403×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.890× | -6.9 | 4e-09 | 3/49 (SW 1088, HepG2/C3A, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.742×** | -5.2 | 7e-05 | 31/48 (SW 900, NCI-H2347, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4905. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 32.4 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.31× (z +17.1) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.97× (z +13.2) | — |
| [[A498 (line)]] | wt | 69.2 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.85× (z +12.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.02× (z +8.5) | — |
| [[HEC-1-A (line)]] | alt | 38.0 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.59× (z +12.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.44× (z +8.5) | — |
| [[NCI-H1573 (line)]] | alt | 20.4 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.33× (z +15.2) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.42× (z +10.9) | — |
| [[C32 (line)]] | wt | 110 | 3 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +14.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.94× (z +11.2) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 41.7 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.89× (z +14.8) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 52.2 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.68× (z +12.4) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 33.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.81× (z +12.3) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 34.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.40× (z +10.7) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 36.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +10.6) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 50.4 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +13.5) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[LOX-IMVI (line)]] | wt | 40.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.04× (z +12.8) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 50.3 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.10× (z +11.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.79× (z +10.4) | — |
| [[PANC-1 (line)]] | alt | 35.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.69× (z +12.8) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 40.6 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +10.9) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.48× (z +9.9) | — |
| [[HS-578T (line)]] | alt | 46.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.85× (z +11.6) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 72.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.32× (z +9.0) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 33.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.43× (z +11.6) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 47.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.50× (z +12.1) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 45.5 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +15.2) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[SNU-423 (line)]] | alt | 44.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.91× (z +10.1) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 54.4 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +9.7) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[SW1417 (line)]] | alt | 53.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +13.7) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.53× (z +9.5) | — |
| [[A-427 (line)]] | wt | 31.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +12.3) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[AsPC-1 (line)]] | alt | 29.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +9.5) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[COLO 205 (line)]] | alt | 38.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.81× (z +11.3) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 53.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +8.9) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[Hs 766T (line)]] | wt | 49.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.47× (z +9.6) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 36.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +10.0) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H2030 (line)]] | alt | 41.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.61× (z +8.7) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 41.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.75× (z +8.5) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 59.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.58× (z +12.1) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 42.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +9.7) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[SNU-1 (line)]] | wt | 33.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.57× (z +9.0) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 53.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +8.6) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[AN3 CA (line)]] | alt | 64.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 62.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 49.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 44.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 38.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 67.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 74.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 72.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 54.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4905), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COPS5]] | +0.76 | +0.78 / +0.69 | both halves | 7e-06 | STRING 537 |
| [[CLK4]] | +0.73 | +0.83 / +0.69 | both halves | 7e-06 |  |
| [[SCRN3]] | +0.73 | +0.72 / +0.72 | both halves | 7e-06 |  |
| [[PMPCB]] | +0.71 | +0.71 / +0.69 | both halves | 7e-06 | STRING 927 |
| [[SLC25A46]] | +0.70 | +0.76 / +0.63 | both halves | 7e-06 |  |
| [[CCDC25]] | +0.70 | +0.73 / +0.63 | both halves | 7e-06 |  |
| [[SMARCE1]] | +0.70 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[ZDHHC17]] | +0.69 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[FAM204A]] | +0.68 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[ETFRF1]] | +0.68 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[KPNA5]] | +0.67 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[SF3B1]] | +0.67 | +0.63 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAD1L1]] | -0.69 | -0.50 / -0.76 | both halves | 1e-05 |  |
| [[CORO7]] | -0.68 | -0.77 / -0.61 | both halves | 7e-06 |  |
| [[AXIN1]] | -0.68 | -0.60 / -0.72 | both halves | 7e-06 |  |
| [[SLC27A4]] | -0.66 | -0.65 / -0.62 | both halves | 7e-06 |  |
| [[GATAD2A]] | -0.65 | -0.70 / -0.57 | both halves | 1e-05 |  |
| [[PAQR4]] | -0.64 | -0.63 / -0.60 | both halves | 7e-06 |  |
| [[LMBR1]] | -0.64 | -0.65 / -0.57 | both halves | 9e-06 |  |
| [[TAF4]] | -0.62 | -0.66 / -0.52 | both halves | 1e-05 |  |
| [[ARPC5L]] | -0.62 | -0.44 / -0.69 | both halves | 3e-05 |  |
| [[TRAPPC10]] | -0.62 | -0.64 / -0.55 | both halves | 1e-05 |  |
| [[TPST2]] | -0.61 | -0.73 / -0.57 | both halves | 9e-06 |  |
| [[FOXK2]] | -0.61 | -0.64 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STRIP2]] | B | STRIP2 activity raises NDUFA5's level | lines that do not express STRIP2 (6) vs lines expressing it (44) | 1.29× lower at baseline in the lines without STRIP2 | 0.092 | ⚠ within organs, on part of the lines; also absent: STK31, HLA-F-AS1, MIR181A2HG; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.800). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-22.8, 3.0); signed map (8.4, -25.6). **Vector** length 98.6, 26.2% of its response variance represented; |z| ≥ 3 in 845 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +7.4 | +17.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.1 | +12.5 |
|  | [[Selinexor (drug)]] 5 µM |  | +6.5 | +7.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +6.1 | +11.5 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +5.0 | +4.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.2 | +2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +5.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.3 | +1.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.3 | +1.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.2 | +1.9 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.6 | -0.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.1 | -5.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.8 | -0.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.6 | +1.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.8 | +2.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.7 | -1.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.6 | -2.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.3 | -0.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.2 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | NADH:ubiquinone oxidoreductase subunit A5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q31.32 — chr7:123,536,997-123,557,904 (-) |
| Ensembl biotype | protein_coding |
| Also known as | B13, NUFM, CI-13KD-B, UQOR13, CI-13kB |
| Gene groups (HGNC) | NADH:ubiquinone oxidoreductase supernumerary subunits |
| Hallmark sets | ADIPOGENESIS, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 7 pathways, smallest: Complex I biogenesis; RHOG GTPase cycle; Respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16718](https://www.uniprot.org/uniprotkb/Q16718) (NADH dehydrogenase):

> Accessory subunit of the mitochondrial membrane respiratory chain NADH dehydrogenase (Complex I), that is believed not to be involved in catalysis. Complex I functions in the transfer of electrons from NADH to the respiratory chain. The immediate electron acceptor for the enzyme is believed to be ubiquinone.

**Summary**, from NCBI Gene [4698](https://www.ncbi.nlm.nih.gov/gene/4698):

> This nuclear gene encodes a conserved protein that comprises the B13 subunit of complex I of the mitochondrial respiratory chain. The encoded protein localizes to the inner mitochondrial membrane, where it is thought to aid in the transfer of electrons from NADH to ubiquinone. Alternative splicing results in multiple transcript variants. There are numerous pseudogenes of this gene on chromosomes 1, 3, 6, 8, 9, 11, 12, and 16. [provided by RefSeq, Apr 2014]

**Accessions** — [HGNC:7688](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7688) · Entrez [4698](https://www.ncbi.nlm.nih.gov/gene/4698) · UniProt [Q16718](https://www.uniprot.org/uniprotkb/Q16718) · Ensembl [ENSG00000128609](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128609)

## Data

Gene col 4905: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4905); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4905, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4905]; `tensor/DDL_lfc|DDL_z.npy` [4905]; `embed/gene_vectors.npy` [4905]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4905 or target_col == 4905). Every well: [[NDUFA5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NDUFA5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
