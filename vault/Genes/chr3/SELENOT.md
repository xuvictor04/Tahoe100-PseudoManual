---
symbol: "SELENOT"
type: "gene"
col: 12705
ensembl_id: "ENSG00000198843"
name: "selenoprotein T"
location: "3q25.1"
module: 77
arm: "-"
pooled_cpm: 46.51
n_lines_expressing: 50
n_dd_up: 31
n_dd_down: 0
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/077"]
generated_by: "tahoemap"
---

# SELENOT

*selenoprotein T* — 3q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.18× (z +21.4, q 0e+00, up in 44 of 48 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.70× (z +19.3, q 0e+00, up in 47 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 0.217×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACP2]] (+0.61, fdr 1e-05), [[TRAPPC6B]] (+0.55, fdr 3e-05), [[DECR1]] (+0.53, fdr 6e-05); moves opposite to [[SPATA2L]] (-0.51, fdr 2e-04), [[LINC02935]] (-0.50, fdr 1e-04), [[PHF13]] (-0.49, fdr 5e-05).
> It sits in the **-** arm of [[Module 077]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 17 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12705.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.18×** | +21.4 | 0e+00 | 44/48 (PANC-1, A549, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.70×** | +19.3 | 0e+00 | 47/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.22×** | +15.5 | 0e+00 | 43/47 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.21×** | +15.4 | 0e+00 | 45/47 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.18×** | +14.6 | 0e+00 | 46/48 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.91×** | +12.6 | 3e-34 | 38/47 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.83×** | +11.7 | 7e-30 | 34/48 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.74×** | +10.7 | 7e-25 | 40/48 (BT-474, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.74×** | +10.4 | 2e-23 | 32/40 (PANC-1, A-172, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.64×** | +9.9 | 3e-21 | 44/49 (SW480, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +9.6 | 6e-20 | 34/48 (NCI-H2347, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.56×** | +8.7 | 2e-16 | 35/48 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.57×** | +8.1 | 2e-14 | 30/44 (A549, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.48×** | +7.6 | 9e-13 | 39/48 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.45×** | +7.2 | 2e-11 | 35/48 (PANC-1, LS 180, …) | rises with dose | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +6.5 | 2e-09 | 31/48 (A-172, A-427, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.78×** | +5.9 | 1e-07 | 29/48 (SW480, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.37×** | +5.8 | 2e-07 | 27/48 (NCI-H1573, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.38×** | +4.5 | 2e-04 | 23/48 (PANC-1, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.24×** | +4.2 | 6e-04 | 19/48 (CFPAC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.17× | +4.2 | 6e-04 | 14/48 (CFPAC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.21×** | +3.6 | 0.005 | 19/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12705.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 0.217×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | 0.831× | -3.5 | 0.14 | 19/47 (RKO, CFPAC-1, …) | rises with dose | position effect removed |
| [[9-ING-41 (drug)]] 5 µM |  | 0.721× | -3.3 | 0.14 | 4/48 (HOP62, Hs 766T, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 0.845× | -3.3 | 0.14 | 9/48 (SW 1088, HS-578T, …) | inconsistent across doses |  |
| [[Tetracycline (hydrochloride) (drug)]] 5 µM |  | 0.842× | -3.2 | 0.14 | 7/48 (NCI-H1573, RKO, …) | top dose only | plate-row cell shift |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.848× | -3.2 | 0.14 | 15/48 (CFPAC-1, RPMI-7951, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12705. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 25.3 | 10 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +15.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.26× (z +14.1) | — |
| [[PANC-1 (line)]] | alt | 38.7 | 9 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +16.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.10× (z +15.4) | — |
| [[SW480 (line)]] | alt | 44.3 | 9 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.60× (z +20.3) | — |
| [[NCI-H1573 (line)]] | alt | 41.9 | 7 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.53× (z +17.2) | — |
| [[A549 (line)]] | wt | 34.0 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.69× (z +15.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.02× (z +9.4) | — |
| [[BT-474 (line)]] | alt | 58.1 | 5 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.30× (z +13.5) | — |
| [[NCI-H23 (line)]] | alt | 47.7 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.52× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.05× (z +10.7) | — |
| [[KATO III (line)]] | alt | 62.6 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.87× (z +17.6) | — |
| [[LS 180 (line)]] | wt | 52.4 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.57× (z +14.0) | — |
| [[Panc 03.27 (line)]] | alt | 66.2 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +14.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.60× (z +8.9) | — |
| [[A-172 (line)]] | wt | 47.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.37× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[CFPAC-1 (line)]] | alt | 70.0 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +13.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.58× (z +8.7) | — |
| [[COLO 205 (line)]] | alt | 40.3 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.06× (z +14.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.22× (z +10.3) | — |
| [[HOP62 (line)]] | alt | 37.3 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +10.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.93× (z +10.0) | — |
| [[HT-29 (line)]] | alt | 49.2 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +11.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.88× (z +9.7) | — |
| [[LoVo (line)]] | wt | 32.2 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.95× (z +14.3) | — |
| [[NCI-H2030 (line)]] | alt | 38.5 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +13.1) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[SHP-77 (line)]] | alt | 40.5 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.04× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.217× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[AsPC-1 (line)]] | alt | 27.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +10.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.45× (z +9.3) | — |
| [[C32 (line)]] | wt | 38.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +10.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.27× (z +9.1) | — |
| [[Hs 766T (line)]] | wt | 27.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.50× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 47.1 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +8.6) | — |
| [[NCI-H1792 (line)]] | alt | 41.6 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.26× (z +9.8) | — |
| [[SNU-423 (line)]] | alt | 33.3 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +8.9) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[SW1417 (line)]] | alt | 58.9 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.74× (z +12.7) | — |
| [[SW48 (line)]] | wt | 48.4 | 2 | 0 | [[TAK-901 (drug)]] 0.05 µM 4.26× (z +9.3) | — |
| [[A-427 (line)]] | wt | 89.1 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 2.19× (z +9.3) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[A498 (line)]] | wt | 41.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +9.9) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[HEC-1-A (line)]] | alt | 58.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +11.4) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[HS-578T (line)]] | alt | 53.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.99× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 33.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +8.5) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[LOX-IMVI (line)]] | wt | 38.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +8.8) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H2347 (line)]] | alt | 78.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.70× (z +9.3) | — |
| [[RPMI-7951 (line)]] | alt | 47.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +8.9) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 37.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +9.0) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[SW 900 (line)]] | alt | 45.0 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.82× (z +8.5) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 42.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 47.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 62.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 77.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 38.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 47.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12705), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACP2]] | +0.61 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[TRAPPC6B]] | +0.55 | +0.51 / +0.46 | both halves | 3e-05 |  |
| [[DECR1]] | +0.53 | +0.39 / +0.46 | both halves | 6e-05 |  |
| [[RAP2C]] | +0.52 | +0.44 / +0.39 | both halves | 6e-05 |  |
| [[NCOA4]] | +0.52 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[TAF9B]] | +0.52 | +0.35 / +0.44 | both halves | 1e-04 |  |
| [[TBC1D22B]] | +0.51 | +0.27 / +0.54 | both halves | 3e-04 |  |
| [[ZBED5-AS1]] | +0.51 | +0.49 / +0.37 | both halves | 8e-05 |  |
| [[HNRNPH3]] | +0.51 | +0.37 / +0.51 | both halves | 8e-05 |  |
| [[HHLA3]] | +0.51 | +0.47 / +0.39 | both halves | 5e-05 |  |
| [[PMPCB]] | +0.51 | +0.50 / +0.40 | both halves | 5e-05 |  |
| [[C5orf15]] | +0.50 | +0.26 / +0.46 | both halves | 4e-04 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPATA2L]] | -0.51 | -0.30 / -0.50 | both halves | 2e-04 |  |
| [[LINC02935]] | -0.50 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[PHF13]] | -0.49 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[TSEN54]] | -0.48 | -0.40 / -0.35 | both halves | 1e-04 |  |
| [[PWWP3A]] | -0.48 | -0.30 / -0.49 | both halves | 2e-04 |  |
| [[MPST]] | -0.47 | -0.37 / -0.39 | both halves | 8e-05 |  |
| [[PUSL1]] | -0.47 | -0.32 / -0.34 | both halves | 2e-04 |  |
| [[TMEM120B]] | -0.47 | -0.46 / -0.33 | both halves | 1e-04 |  |
| [[RBAK-RBAKDN]] | -0.47 | -0.29 / -0.50 | both halves | 2e-04 |  |
| [[RMND1]] | -0.47 | -0.20 / -0.42 | ⚠ not reproduced | 7e-04 |  |
| [[TBC1D16]] | -0.47 | -0.36 / -0.41 | both halves | 9e-05 |  |
| [[ANKRD27]] | -0.47 | -0.43 / -0.33 | both halves | 1e-04 |  |
| [[LRRC42]] | -0.46 | -0.42 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 077]]; 59 genes; this gene is in the **-** arm (projection on the module's main direction -0.476). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.44).
- **Nodal map** (x, y) = (-20.5, 21.2); signed map (19.6, -18.2). **Vector** length 62.0, 13.3% of its response variance represented; |z| ≥ 3 in 1,105 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | +4.7 | +12.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | +4.6 | +10.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.1 | +15.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.1 | +3.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | +3.1 | +8.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +3.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.8 | +3.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | -1.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.6 | -3.5 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.6 | +4.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.5 | -1.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | +2.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | +2.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~62% of this change | -2.4 | +4.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | -2.2 | +4.3 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.1 | -0.5 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | -1.0 | -1.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.0 | -0.4 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.0 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | selenoprotein T |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q25.1 — chr3:150,602,875-150,630,436 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SELT |
| Gene groups (HGNC) | Selenoproteins; Oxidoreductases |
| Matched by | ensembl_id |

**Function**, from UniProt [P62341](https://www.uniprot.org/uniprotkb/P62341) (Thioredoxin reductase-like selenoprotein T):

> Selenoprotein with thioredoxin reductase-like oxidoreductase activity (By similarity). Protects dopaminergic neurons against oxidative stress and cell death. Involved in ADCYAP1/PACAP-induced calcium mobilization and neuroendocrine secretion (By similarity). Plays a role in fibroblast anchorage and redox regulation (By similarity). In gastric smooth muscle, modulates the contraction processes through the regulation of calcium release and MYLK activation (By similarity). In pancreatic islets, …

**Summary**, from NCBI Gene [51714](https://www.ncbi.nlm.nih.gov/gene/51714):

> This gene encodes a selenoprotein, containing a selenocysteine (Sec) residue at the active site. Sec is encoded by the UGA codon that normally signals translation termination. The 3' UTRs of selenoprotein mRNAs contain a conserved stem-loop structure, the Sec insertion sequence (SECIS) element, that is necessary for the recognition of UGA as a Sec codon rather than as a stop signal. This protein is localized in the endoplasmic reticulum. It belongs to the SelWTH family that possesses a …

**Accessions** — [HGNC:18136](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18136) · Entrez [51714](https://www.ncbi.nlm.nih.gov/gene/51714) · UniProt [P62341](https://www.uniprot.org/uniprotkb/P62341) · Ensembl [ENSG00000198843](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198843)

## Data

Gene col 12705: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12705); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12705, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12705]; `tensor/DDL_lfc|DDL_z.npy` [12705]; `embed/gene_vectors.npy` [12705]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12705 or target_col == 12705). Every well: [[SELENOT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SELENOT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
