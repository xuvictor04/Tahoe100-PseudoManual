---
symbol: "ZNRF3"
type: "gene"
col: 11419
ensembl_id: "ENSG00000183579"
name: "zinc and ring finger 3"
location: "22q12.1"
module: 5
arm: "+"
pooled_cpm: 85.87
n_lines_expressing: 48
n_dd_up: 23
n_dd_down: 4
n_dd_up_clean: 15
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 10
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# ZNRF3

*zinc and ring finger 3* — 22q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (8 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 2.18× (z +15.3, q 0e+00, up in 37 of 46 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.42× (z +9.7, q 1e-19, up in 28 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.688× (z -7.1, q 8e-10, down in 24 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[GSK1059615 (drug)]] 0.5 µM: 0.744× (z -4.2, q 0.006, down in 21 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (LS 180 0.0922×, SW480 0.147×, SHP-77 0.134×, Panc 03.27 0.120×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (LS 180 0.125×, SW480 0.162×, COLO 205 0.0895×, SW1417 0.224×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (SW1417 0.489×, SW480 0.438×, SW48 0.351×, COLO 205 0.339×); [[Auranofin (drug)]] 5 µM in 3 lines (SW480 0.250×, SW1417 0.396×, SW48 0.289×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SW48 0.228×, SW480 0.374×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AXIN2]] (+0.60, fdr 1e-05), [[UCK2]] (+0.60, fdr 1e-05), [[CTDSPL]] (+0.58, fdr 1e-05); moves opposite to [[SERINC3]] (-0.55, fdr 2e-05), [[SERINC1]] (-0.53, fdr 1e-05), [[PJA2]] (-0.52, fdr 1e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[AXIN2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11419.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.18×** | +15.3 | 0e+00 | 37/46 (A498, HT-29, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +9.7 | 1e-19 | 28/47 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.40×** | +9.2 | 5e-18 | 26/46 (A498, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[venetoclax (drug)]] 5 µM |  | **2.34×** | +8.7 | 6e-16 | 35/45 (A498, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.98×** | +7.0 | 3e-10 | 33/46 (A498, HT-29, …) | all doses, flat | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.95×** | +6.8 | 8e-10 | 34/46 (A498, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.95×** | +6.8 | 8e-10 | 31/46 (HT-29, A498, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.40×** | +6.6 | 3e-09 | 25/46 (SW 900, NCI-H1573, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.38×** | +6.3 | 1e-08 | 26/46 (SW 900, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.32×** | +5.5 | 2e-06 | 25/46 (CFPAC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.30×** | +5.1 | 2e-05 | 21/46 (NCI-H23, C32, …) | two highest doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.57×** | +4.6 | 2e-04 | 18/47 (CFPAC-1, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.27×** | +4.6 | 2e-04 | 18/46 (NCI-H460, HS-578T, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~11% of this change | **1.26×** | +4.6 | 2e-04 | 22/46 (NCI-H2347, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.26×** | +4.5 | 2e-04 | 19/46 (HOP62, A549, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.26×** | +4.4 | 4e-04 | 22/46 (NCI-H460, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **1.48×** | +4.0 | 0.002 | 19/46 (HT-29, A498, …) | rises with dose | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.43×** | +3.7 | 0.007 | 23/46 (MIA PaCa-2, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **1.26×** | +3.2 | 0.034 | 15/47 (A498, SW 900, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 5 µM |  | 1.17× | +3.1 | 0.053 | 9/46 (A498, HOP62, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 0.5 µM |  | **1.25×** | +3.0 | 0.053 | 8/46 (HT-29, PANC-1, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11419.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (LS 180 0.0922×, SW480 0.147×, SHP-77 0.134×, Panc 03.27 0.120×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (LS 180 0.125×, SW480 0.162×, COLO 205 0.0895×, SW1417 0.224×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (SW1417 0.489×, SW480 0.438×, SW48 0.351×, COLO 205 0.339×); [[Auranofin (drug)]] 5 µM in 3 lines (SW480 0.250×, SW1417 0.396×, SW48 0.289×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SW48 0.228×, SW480 0.374×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.688×** | -7.1 | 8e-10 | 24/39 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.736×** | -6.0 | 5e-07 | 25/46 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.744×** | -4.2 | 0.006 | 21/46 (Panc 03.27, LS 180, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.833×** | -3.5 | 0.071 | 19/48 (SW48, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | 0.802× | -3.1 | 0.18 | 15/44 (AN3 CA, RPMI-7951, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 0.855× | -3.1 | 0.18 | 18/46 (COLO 205, KATO III, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.848× | -3.0 | 0.21 | 13/45 (A549, RKO, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11419. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW1417 (line)]] | alt | 485 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.224× (z -19.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.489× (z -13.3) |
| [[SW48 (line)]] | wt | 484 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.144× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -12.7) |
| [[SW480 (line)]] | alt | 333 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.147× (z -20.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.250× (z -15.4) |
| [[COLO 205 (line)]] | alt | 275 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0895× (z -20.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -12.7) |
| [[LS 180 (line)]] | wt | 237 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0922× (z -24.2) ⚠ toxic; transcription drop · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 0.562× (z -8.6) |
| [[A498 (line)]] | wt | 48.2 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +16.4) | — |
| [[HEC-1-A (line)]] | alt | 56.6 | 3 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.95× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.376× (z -11.1) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 36.0 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +15.0) | — |
| [[SHP-77 (line)]] | alt | 64.9 | 1 (1 ⚠) | 3 (3 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.68× (z +9.6) ⚠ unreliable plate only | [[Dinaciclib (drug)]] 5 µM 0.134× (z -18.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 30.2 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +15.5) | — |
| [[C-33 A (line)]] | alt | 103 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0982× (z -19.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 113 | 1 (1 ⚠) | 2 (2 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.73× (z +14.6) ⚠ unreliable plate only | [[Dinaciclib (drug)]] 0.5 µM 0.265× (z -14.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 128 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.177× (z -14.3) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 39.3 | 1 (1 ⚠) | 2 (2 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.21× (z +10.0) ⚠ unreliable plate only | [[Dinaciclib (drug)]] 0.05 µM 0.358× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 46.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +11.9) | — |
| [[AN3 CA (line)]] | alt | 79.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.117× (z -11.8) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 206 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.209× (z -12.2) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 69.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.265× (z -12.4) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 31.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +14.9) | — |
| [[Panc 03.27 (line)]] | alt | 50.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.36× (z +10.7) ⚠ unreliable plate only | [[Dinaciclib (drug)]] 5 µM 0.120× (z -18.1) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 33.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +9.5) | — |
| [[A-427 (line)]] | wt | 74.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.152× (z -17.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 44.3 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.62× (z +9.5) ⚠ unreliable plate only | — |
| [[CFPAC-1 (line)]] | alt | 24.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +11.3) | — |
| [[CHP-212 (line)]] | wt | 53.4 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 7.87× (z +9.7) ⚠ unreliable plate only | — |
| [[H4 (line)]] | wt | 35.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.68× (z +10.9) | — |
| [[HepG2_C3A (line)]] | wt | 133 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.360× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~59% of this change |
| [[HOP62 (line)]] | alt | 29.4 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.58× (z +8.6) ⚠ unreliable plate only | — |
| [[Hs 766T (line)]] | wt | 24.7 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 4.27× (z +9.6) ⚠ unreliable plate only | — |
| [[HS-578T (line)]] | alt | 48.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +14.9) | — |
| [[J82 (line)]] | alt | 39.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.179× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 56.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +12.8) | — |
| [[NCI-H596 (line)]] | alt | 107 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 5 µM 0.0933× (z -11.6) |
| [[RKO (line)]] | wt | 85.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.360× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 79.5 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.448× (z -8.8) |
| [[SNU-423 (line)]] | alt | 52.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +11.8) | — |
| [[AsPC-1 (line)]] | alt | 16.0 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 36.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 21.4 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 75.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11419), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AXIN2]] | +0.60 | +0.56 / +0.60 | both halves | 1e-05 | pathway: Signaling by WNT; STRING 649 |
| [[UCK2]] | +0.60 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[CTDSPL]] | +0.58 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[WDR4]] | +0.58 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[LINC01622]] | +0.58 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[DHX33]] | +0.57 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[NOP2]] | +0.57 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[UTP4]] | +0.57 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[CHDH]] | +0.57 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[HUNK]] | +0.56 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[BMP4]] | +0.56 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[KLHDC4]] | +0.56 | +0.54 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SERINC3]] | -0.55 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[SERINC1]] | -0.53 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[PJA2]] | -0.52 | -0.50 / -0.59 | both halves | 1e-05 | same gene group |
| [[PNPLA8]] | -0.52 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[FAM161B]] | -0.52 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[CRIPT]] | -0.50 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[PAIP2]] | -0.49 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[OGA]] | -0.48 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[SARAF]] | -0.48 | -0.46 / -0.40 | both halves | 4e-05 |  |
| [[FAM8A1]] | -0.47 | -0.37 / -0.47 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AXIN2]] | B | AXIN2 activity raises ZNRF3's level | lines that do not express AXIN2 (32) vs lines expressing it (18) | 3.36× lower at baseline in the lines without AXIN2 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LGR5, LINC02253, LINC02964 |
| [[COLGALT2]] | B | COLGALT2 activity raises ZNRF3's level | lines that do not express COLGALT2 (23) vs lines expressing it (27) | 1.57× lower at baseline in the lines without COLGALT2 | 0.017 | ⚠ within organs, on part of the lines; also absent: PRRX1, SYT11, GNAT3 |
| [[WNK2]] | B | WNK2 activity raises ZNRF3's level | lines that do not express WNK2 (16) vs lines expressing it (34) | 2.29× lower at baseline in the lines without WNK2 | 0.026 | ⚠ within organs, on part of the lines; also absent: NUP210, SLC27A2, CHDH |
| [[NKD1]] | B | NKD1 activity raises ZNRF3's level | lines that do not express NKD1 (34) vs lines expressing it (16) | 3.03× lower at baseline in the lines without NKD1 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000265554, VSNL1, ENSG00000213981 |
| [[VWA2]] | B | VWA2 activity raises ZNRF3's level | lines that do not express VWA2 (36) vs lines expressing it (14) | 3.04× lower at baseline in the lines without VWA2 | 0.057 | ⚠ within organs, on part of the lines; also absent: LINC01559, SLC5A1, SKAP1 |
| [[LGR5]] | B | LGR5 activity raises ZNRF3's level | lines that do not express LGR5 (39) vs lines expressing it (11) | 2.58× lower at baseline in the lines without LGR5 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PCK1, DSG4, ENSG00000260573 |
| [[VSNL1]] | B | VSNL1 activity raises ZNRF3's level | lines that do not express VSNL1 (34) vs lines expressing it (16) | 2.55× lower at baseline in the lines without VSNL1 | 0.095 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02964, EDAR, VWA2 |
| [[CHDH]] | B | CHDH activity raises ZNRF3's level | lines that do not express CHDH (22) vs lines expressing it (28) | 2.16× lower at baseline in the lines without CHDH | 0.097 | ⚠ within organs, on part of the lines; also absent: IL17RB, ESRP2, PRSS22 |
| [[HSD11B2]] | B | HSD11B2 activity raises ZNRF3's level | lines that do not express HSD11B2 (16) vs lines expressing it (34) | 2.06× lower at baseline in the lines without HSD11B2 | 0.098 | ⚠ within organs, on part of the lines; also absent: MCF2L, CHDH, IL17RB; maybe low, not absent |
| [[APCDD1]] | B | APCDD1 activity raises ZNRF3's level | lines that do not express APCDD1 (40) vs lines expressing it (10) | 2.05× lower at baseline in the lines without APCDD1 | 0.098 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: APOB, MUC6, ENSG00000285751 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.522). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-6.2, 39.7); signed map (-3.3, -56.4). **Vector** length 123, 34.5% of its response variance represented; |z| ≥ 3 in 1,205 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +11.5 | +15.3 |
|  | [[EX229 (drug)]] 5 µM |  | +7.4 | +6.8 |
|  | [[venetoclax (drug)]] 5 µM |  | +6.3 | +8.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +6.1 | +7.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | +5.9 | +6.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +5.0 | +4.0 |
| fall | [[GSK1059615 (drug)]] 0.5 µM |  | -2.4 | -4.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -2.3 | -3.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.2 | -2.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | +2.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.9 | -2.4 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.7 | -1.7 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -1.7 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | zinc and ring finger 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.1 — chr22:28,883,572-29,057,488 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1133, BK747E2.3, FLJ22057, RNF203 |
| Gene groups (HGNC) | Ring finger proteins; RING finger E3 ubiquitin protein ligases |
| Reactome | 3 pathways, smallest: Regulation of FZD by ubiquitination; TCF dependent signaling in response to WNT; Signaling by WNT |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9ULT6](https://www.uniprot.org/uniprotkb/Q9ULT6) (E3 ubiquitin-protein ligase ZNRF3):

> E3 ubiquitin-protein ligase that acts as a negative regulator of the Wnt signaling pathway by mediating the ubiquitination and subsequent degradation of Wnt receptor complex components Frizzled and LRP6. Acts on both canonical and non-canonical Wnt signaling pathway. Acts as a tumor suppressor in the intestinal stem cell zone by inhibiting the Wnt signaling pathway, thereby restricting the size of the intestinal stem cell zone. Along with RSPO2 and RNF43, constitutes a master switch that …

**Summary**, from NCBI Gene [84133](https://www.ncbi.nlm.nih.gov/gene/84133):

> Enables frizzled binding activity and ubiquitin-protein transferase activity. Involved in negative regulation of Wnt signaling pathway; protein ubiquitination; and ubiquitin-dependent protein catabolic process. Located in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:18126](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18126) · Entrez [84133](https://www.ncbi.nlm.nih.gov/gene/84133) · UniProt [Q9ULT6](https://www.uniprot.org/uniprotkb/Q9ULT6) · Ensembl [ENSG00000183579](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183579)

## Data

Gene col 11419: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11419); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11419, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11419]; `tensor/DDL_lfc|DDL_z.npy` [11419]; `embed/gene_vectors.npy` [11419]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11419 or target_col == 11419). Every well: [[ZNRF3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNRF3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
