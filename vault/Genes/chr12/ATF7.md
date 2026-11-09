---
symbol: "ATF7"
type: "gene"
col: 9992
ensembl_id: "ENSG00000170653"
name: "activating transcription factor 7"
location: "12q13.13"
module: 58
arm: "+"
pooled_cpm: 103.64
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 20
n_dd_up_clean: 1
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/058"]
generated_by: "tahoemap"
---

# ATF7

*activating transcription factor 7* — 12q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.09× (z +6.9, q 2e-09, up in 1 of 50 measured lines) ⚠ position not correctable. The strongest without an alert is [[GSK1059615 (drug)]] 5 µM: 1.36× (z +3.7, q 0.062, up in 17 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (C-33 A 2.69×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (15 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.601× (z -16.4, q 0e+00, down in 44 of 49 measured lines).
> Its strongest partners by |cos| (88 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 14 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POLR2G]] (+0.62, fdr 4e-05, ⚠ POLR2G in the vector space only through flagged drug-doses), [[RBM6]] (+0.57, fdr 1e-04), [[HAUS3]] (+0.50, fdr 2e-04), [[KATNIP]] (+0.50, fdr 3e-05); moves opposite to [[AMPD3]] (-0.54, fdr 1e-04), [[HLA-L-1]] (-0.53, fdr 2e-05), [[SIX4]] (-0.51, fdr 6e-05).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HLA-L-1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9992.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (C-33 A 2.69×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +6.9 | 2e-09 | 1/50 (MIA PaCa-2) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.36×** | +3.7 | 0.062 | 17/49 (HEC-1-A, H4, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 1.16× | +3.2 | 0.15 | 14/47 (NCI-H2030, A498, …) | rises with dose |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.10× | +3.2 | 0.15 | 1/48 (AN3 CA) | top dose only |  |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | 1.16× | +3.2 | 0.15 | 9/48 (HEC-1-A, SK-MEL-2, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.15× | +3.1 | 0.15 | 13/47 (SK-MEL-2, NCI-H2030, …) | rises with dose | low cells (technical?) |
| [[Bimiralisib (drug)]] 5 µM |  | 1.30× | +3.1 | 0.15 | 11/50 (J82, A-427, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 23 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9992.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.601×** | -16.4 | 0e+00 | 44/49 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.659×** | -13.5 | 8e-39 | 43/48 (HS-578T, HOP62, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.517×** | -12.1 | 1e-31 | 38/45 (NCI-H2030, RKO, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.614×** | -11.1 | 1e-26 | 42/48 (MIA PaCa-2, SNU-423, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **0.640×** | -10.2 | 2e-22 | 39/49 (H4, NCI-H1792, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.460×** | -9.3 | 2e-18 | 40/49 (HOP62, A-172, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **0.673×** | -8.7 | 3e-16 | 32/44 (LoVo, SNU-1, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.687×** | -8.6 | 7e-16 | 33/48 (A-427, A-172, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.724×** | -7.1 | 8e-11 | 36/50 (HOP62, NCI-H460, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.727×** | -7.0 | 1e-10 | 31/48 (RKO, H4, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.746×** | -6.7 | 1e-09 | 33/48 (LOX-IMVI, HOP62, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | **0.767×** | -6.1 | 6e-08 | 28/48 (SW 1271, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.779×** | -5.7 | 5e-07 | 29/48 (AN3 CA, HOP62, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.776×** | -5.6 | 1e-06 | 29/48 (AsPC-1, A498, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~20% of this change | **0.778×** | -5.5 | 1e-06 | 29/47 (CFPAC-1, RKO, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.871× | -4.5 | 2e-04 | 17/48 (NCI-H2030, NCI-H1792, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.873× | -4.4 | 3e-04 | 14/49 (NCI-H460, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.837× | -4.1 | 0.001 | 18/47 (NCI-H460, C32, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.842× | -3.9 | 0.002 | 17/48 (CFPAC-1, SK-MEL-2, …) | two highest doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.769×** | -3.1 | 0.034 | 17/49 (NCI-H1792, HOP62, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.872× | -3.1 | 0.034 | 16/48 (LOX-IMVI, SW 900, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 0.5 µM |  | 0.835× | -3.0 | 0.056 | 15/48 (HOP62, SW480, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.919× | -2.8 | 0.095 | 5/48 (PANC-1, NCI-H1792, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.883× | -2.7 | 0.096 | 14/47 (LOX-IMVI, NCI-H460, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9992. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 347 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.317× (z -16.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.515× (z -13.6) |
| [[HOP62 (line)]] | alt | 80.0 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -17.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.458× (z -14.0) |
| [[NCI-H460 (line)]] | wt | 114 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.383× (z -19.9) |
| [[H4 (line)]] | wt | 97.1 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.125× (z -19.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.471× (z -9.9) |
| [[LOX-IMVI (line)]] | wt | 122 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.510× (z -12.0) |
| [[NCI-H2030 (line)]] | alt | 148 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.179× (z -18.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.551× (z -11.1) |
| [[A-172 (line)]] | wt | 81.7 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.455× (z -13.3) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.485× (z -12.2) |
| [[AsPC-1 (line)]] | alt | 95.5 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.464× (z -12.7) |
| [[CFPAC-1 (line)]] | alt | 93.2 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -17.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.440× (z -14.3) |
| [[Panc 03.27 (line)]] | alt | 118 | 0 | 4 (3 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.120× (z -12.9) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.444× (z -9.5) |
| [[A498 (line)]] | wt | 109 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -14.7) |
| [[AN3 CA (line)]] | alt | 110 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.197× (z -10.7) |
| [[HCT15 (line)]] | alt | 114 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.316× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.516× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 90.1 | 0 | 3 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.141× (z -14.8) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.621× (z -9.8) |
| [[J82 (line)]] | alt | 73.3 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.515× (z -10.9) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.596× (z -8.5) |
| [[MIA PaCa-2 (line)]] | alt | 79.8 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.288× (z -13.3) ⚠ toxic; cell-cycle shift, explains ~20% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.347× (z -11.8) |
| [[NCI-H1573 (line)]] | alt | 97.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.335× (z -12.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 90.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.159× (z -16.3) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 90.3 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.399× (z -10.8) |
| [[SW480 (line)]] | alt | 144 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.364× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[A-427 (line)]] | wt | 132 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.447× (z -11.1) |
| [[BT-474 (line)]] | alt | 108 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.434× (z -14.1) |
| [[C32 (line)]] | wt | 90.9 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.371× (z -10.4) |
| [[HepG2_C3A (line)]] | wt | 120 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -13.6) |
| [[HS-578T (line)]] | alt | 84.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -19.7) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.565× (z -9.4) |
| [[hTERT-HPNE (line)]] | wt | 85.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.443× (z -10.3) |
| [[LoVo (line)]] | wt | 95.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.242× (z -20.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[NCI-H23 (line)]] | alt | 149 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.518× (z -12.8) |
| [[PANC-1 (line)]] | alt | 108 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.371× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[SK-MEL-2 (line)]] | alt | 68.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.408× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.428× (z -9.3) |
| [[SW 900 (line)]] | alt | 85.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.207× (z -14.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 99.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.441× (z -14.0) |
| [[C-33 A (line)]] | alt | 92.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.69× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | — |
| [[COLO 205 (line)]] | alt | 93.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.530× (z -9.3) |
| [[Hs 766T (line)]] | wt | 73.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -10.8) |
| [[KATO III (line)]] | alt | 85.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.377× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[LS 180 (line)]] | wt | 94.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.557× (z -10.8) |
| [[NCI-H2347 (line)]] | alt | 75.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.572× (z -9.3) ⚠ cell-cycle shift, explains ~31% of this change |
| [[RPMI-7951 (line)]] | alt | 74.8 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.332× (z -10.2) |
| [[SNU-1 (line)]] | wt | 93.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.184× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[SW 1271 (line)]] | alt | 111 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.122× (z -9.7) ⚠ transcription drop; cell-cycle shift, explains ~38% of this change |
| [[CHP-212 (line)]] | wt | 91.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 81.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 87.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 98.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 96.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 65.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 59.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9992), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*43 of its nearest partners move with it, 10 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR2G]] ⚠ | +0.62 | +0.54 / +0.41 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RBM6]] | +0.57 | +0.62 / +0.32 | both halves | 1e-04 |  |
| [[HAUS3]] | +0.50 | +0.53 / +0.30 | both halves | 2e-04 |  |
| [[KATNIP]] | +0.50 | +0.47 / +0.43 | both halves | 3e-05 |  |
| [[ELP4]] | +0.48 | +0.38 / +0.32 | both halves | 1e-04 |  |
| [[TMED1]] | +0.47 | +0.52 / +0.30 | both halves | 2e-04 |  |
| [[TMEM87A]] | +0.47 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[GALNS]] | +0.45 | +0.63 / +0.16 | ⚠ one half (not replicated) | 0.001 |  |
| [[PPP1R12B]] | +0.43 | +0.47 / +0.22 | both halves | 6e-04 |  |
| [[WIPF2]] | +0.42 | +0.47 / +0.29 | both halves | 3e-04 |  |
| [[ZFYVE19]] | +0.42 | +0.47 / +0.21 | both halves | 6e-04 |  |
| [[ZNF235]] | +0.42 | +0.55 / +0.11 | ⚠ one half (not replicated) | 0.002 | same gene group |
| [[VPS13B]] | +0.42 | +0.30 / +0.47 | both halves | 2e-04 |  |
| [[SMG6]] | +0.42 | +0.49 / +0.25 | both halves | 4e-04 |  |
| [[B9D2]] | +0.42 | +0.57 / +0.34 | both halves | 1e-04 |  |

## Genes that move opposite

*57 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AMPD3]] | -0.54 | -0.55 / -0.33 | both halves | 1e-04 |  |
| [[HLA-L-1]] | -0.53 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[SIX4]] | -0.51 | -0.62 / -0.38 | both halves | 6e-05 |  |
| [[P2RY1]] | -0.50 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[PLAAT1]] | -0.50 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[LHX1-DT]] | -0.49 | -0.34 / -0.55 | both halves | 1e-04 |  |
| [[RASGRP1]] | -0.48 | -0.53 / -0.36 | both halves | 1e-04 |  |
| [[WIPF3]] | -0.48 | -0.46 / -0.50 | both halves | 2e-05 |  |
| [[ZNF774]] | -0.47 | -0.45 / -0.43 | both halves | 3e-05 | same gene group |
| [[LINC00265]] | -0.46 | -0.64 / -0.24 | both halves | 4e-04 |  |
| [[TMSB15B]] | -0.46 | -0.35 / -0.52 | both halves | 1e-04 |  |
| [[SLCO5A1]] | -0.45 | -0.53 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HLA-L-1]] | B | HLA-L-1 activity raises ATF7's level | lines that do not express HLA-L-1 (10) vs lines expressing it (40) | 1.24× lower at baseline in the lines without HLA-L-1 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with ACVR2A, SETD1B; also absent: DNAAF9, NR3C1, RIMKLB; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.275). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (29.5, -1.4); signed map (-49.7, -18.9). **Vector** length 83.7, 21.4% of its response variance represented; |z| ≥ 3 in 1,109 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.0 | +0.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.8 | +0.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.6 | +2.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.3 | -0.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | +3.6 | -5.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.6 | +3.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.6 | +0.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.5 | +2.8 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +1.5 | +3.1 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | +1.4 | +1.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.2 | -16.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -5.9 | -13.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.9 | -11.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.8 | -12.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.9 | -4.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.4 | -4.4 |
|  | [[vincristine (drug)]] 0.5 µM |  | -2.1 | -3.0 |
|  | [[Infigratinib (drug)]] 5 µM |  | -1.8 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | activating transcription factor 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.13 — chr12:53,507,856-53,626,410 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ATFA |
| Gene groups (HGNC) | Zinc fingers C2H2-type; Activating transcription factor 2 family |
| Matched by | ensembl_id |

**Function**, from UniProt [P17544](https://www.uniprot.org/uniprotkb/P17544) (Cyclic AMP-dependent transcription factor ATF-7):

> Stress-responsive chromatin regulator that plays a role in various biological processes including innate immunological memory, adipocyte differentiation or telomerase regulation. In absence of stress, contributes to the formation of heterochromatin and heterochromatin-like structure by recruiting histone H3K9 tri- and di-methyltransferases thus silencing the transcription of target genes such as STAT1 in adipocytes, or genes involved in innate immunity in macrophages and adipocytes (By …

**Summary**, from NCBI Gene [11016](https://www.ncbi.nlm.nih.gov/gene/11016):

> Enables several functions, including DNA-binding transcription repressor activity, RNA polymerase II-specific; mitogen-activated protein kinase binding activity; and transcription coactivator binding activity. Involved in negative regulation of transcription by RNA polymerase II and positive regulation of transcription by RNA polymerase II. Located in nucleus. Biomarker of colorectal cancer. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:792](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:792) · Entrez [11016](https://www.ncbi.nlm.nih.gov/gene/11016) · UniProt [P17544](https://www.uniprot.org/uniprotkb/P17544) · Ensembl [ENSG00000170653](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170653)

## Data

Gene col 9992: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9992); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9992, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9992]; `tensor/DDL_lfc|DDL_z.npy` [9992]; `embed/gene_vectors.npy` [9992]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9992 or target_col == 9992). Every well: [[ATF7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATF7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
