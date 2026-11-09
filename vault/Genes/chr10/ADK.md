---
symbol: "ADK"
type: "gene"
col: 7948
ensembl_id: "ENSG00000156110"
name: "adenosine kinase"
location: "10q22.2"
module: 211
arm: "+"
pooled_cpm: 342.98
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 8
n_dd_up_clean: 8
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/211"]
generated_by: "tahoemap"
---

# ADK

*adenosine kinase* — 10q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.40× (z +10.9, q 4e-25, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 0.658× (z -9.6, q 3e-19, down in 39 of 48 measured lines) ⚠ transcription drop; cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.463× (z -9.3, q 5e-18, down in 44 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 8 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (AsPC-1 0.297×, NCI-H2030 0.361×, NCI-H1792 0.472×, J82 0.477×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[TAK-901 (drug)]] 5 µM in 5 lines (MIA PaCa-2 0.215×, PANC-1 0.259×, RKO 0.254×, LOX-IMVI 0.306×, …); [[Topotecan (hydrochloride) (drug)]] 5 µM in 3 lines (MIA PaCa-2 0.301×, NCI-H2030 0.317×, HCT15 0.396×; ⚠ toxic); [[PH-797804 (drug)]] 5 µM in 2 lines (LOX-IMVI 0.331×, A-427 0.298×); [[Radotinib (drug)]] 5 µM in 1 line (AsPC-1 0.510×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SUPT3H]] (+0.67, fdr 7e-06), [[ERC1]] (+0.64, fdr 1e-05), [[SNX29]] (+0.54, fdr 1e-05); moves opposite to [[PEX13]] (-0.50, fdr 3e-05), [[YY1AP1]] (-0.50, fdr 4e-05), [[CDKN1B]] (-0.49, fdr 4e-05).
> It is in [[Module 211]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7948.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.40×** | +10.9 | 4e-25 | 32/48 (HT-29, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.49×** | +9.1 | 2e-17 | 37/48 (COLO 205, C32, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.58×** | +8.8 | 3e-16 | 38/48 (COLO 205, HT-29, …) | all doses, flat | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.43×** | +8.2 | 3e-14 | 30/48 (HT-29, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.36×** | +7.1 | 2e-10 | 36/48 (HT-29, LS 180, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.35×** | +6.9 | 6e-10 | 38/48 (NCI-H460, SW 900, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.20× | +5.9 | 3e-07 | 25/49 (SK-MEL-2, SW 900, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.27×** | +5.5 | 3e-06 | 30/48 (KATO III, Hs 766T, …) | top dose only |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.26×** | +5.3 | 1e-05 | 26/48 (NCI-H1573, SK-MEL-2, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.22×** | +4.4 | 5e-04 | 26/47 (SK-MEL-2, NCI-H1573, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.21×** | +4.4 | 6e-04 | 24/47 (NCI-H1573, SK-MEL-2, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.21×** | +4.3 | 9e-04 | 25/48 (SK-MEL-2, NCI-H1573, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **1.40×** | +4.0 | 0.003 | 29/45 (A498, COLO 205, …) | all doses, flat | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 1.20× | +4.0 | 0.003 | 24/48 (LS 180, NCI-H460, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **1.39×** | +3.9 | 0.003 | 30/48 (NCI-H460, A498, …) | top dose only | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.15× | +3.3 | 0.040 | 17/47 (RKO, RPMI-7951, …) | two highest doses | low cells (technical?) |
| [[BAY1125976 (drug)]] 5 µM |  | **1.31×** | +3.2 | 0.046 | 22/48 (Panc 03.27, Hs 766T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dapagliflozin (drug)]] 0.05 µM |  | 1.14× | +3.0 | 0.081 | 5/48 (J82, NCI-H23, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.10× | +2.9 | 0.087 | 7/48 (SW1417, NCI-H1573, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 9 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7948.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 8 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (AsPC-1 0.297×, NCI-H2030 0.361×, NCI-H1792 0.472×, J82 0.477×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[TAK-901 (drug)]] 5 µM in 5 lines (MIA PaCa-2 0.215×, PANC-1 0.259×, RKO 0.254×, LOX-IMVI 0.306×, …); [[Topotecan (hydrochloride) (drug)]] 5 µM in 3 lines (MIA PaCa-2 0.301×, NCI-H2030 0.317×, HCT15 0.396×; ⚠ toxic); [[PH-797804 (drug)]] 5 µM in 2 lines (LOX-IMVI 0.331×, A-427 0.298×); [[Radotinib (drug)]] 5 µM in 1 line (AsPC-1 0.510×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | **0.658×** | -9.6 | 3e-19 | 39/48 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **0.463×** | -9.3 | 5e-18 | 44/49 (MIA PaCa-2, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.672×** | -8.8 | 2e-16 | 39/47 (MIA PaCa-2, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.723×** | -7.5 | 9e-12 | 35/49 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.744×** | -6.6 | 6e-09 | 29/44 (HCT15, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.785×** | -5.4 | 7e-06 | 28/48 (A498, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.852× | -5.3 | 1e-05 | 23/49 (AsPC-1, NCI-H2030, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.652×** | -5.2 | 2e-05 | 33/48 (LOX-IMVI, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~4% of this change | 0.834× | -3.9 | 0.006 | 22/45 (J82, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.868× | -3.3 | 0.059 | 15/48 (MIA PaCa-2, NCI-H2030, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **0.765×** | -3.2 | 0.061 | 24/47 (RKO, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 0.878× | -3.0 | 0.12 | 11/48 (HOP62, SW 900, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7948. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 271 | 10 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.65× (z +24.0) | — |
| [[HT-29 (line)]] | alt | 209 | 8 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +25.7) | — |
| [[PANC-1 (line)]] | alt | 437 | 1 (1 ⚠) | 7 (6 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 1.65× (z +9.0) ⚠ unreliable plate only | [[Digitoxin (drug)]] 5 µM 0.450× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.259× (z -12.6) |
| [[HepG2_C3A (line)]] | wt | 431 | 6 (6 ⚠) | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +13.8) ⚠ cell-cycle shift, explains ~30% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.479× (z -9.8) ⚠ toxic |
| [[A-172 (line)]] | wt | 264 | 1 (1 ⚠) | 5 (5 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +9.3) ⚠ cell-cycle shift, explains ~30% of this change | [[Niclosamide (olamine) (drug)]] 5 µM 0.392× (z -12.9) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[BT-474 (line)]] | alt | 297 | 5 (4 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.09× (z +16.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.61× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.643× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 270 | 6 (3 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 5.16× (z +23.0) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.13× (z +15.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 423 | 0 | 6 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.301× (z -19.1) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 0.215× (z -13.3) |
| [[SK-MEL-2 (line)]] | alt | 236 | 6 (2 ⚠) | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 1.89× (z +11.8) | — |
| [[SW 900 (line)]] | alt | 358 | 4 (1 ⚠) | 2 (2 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.14× (z +11.4) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.10× (z +11.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.488× (z -10.4) ⚠ toxic |
| [[A498 (line)]] | wt | 258 | 3 (3 ⚠) | 2 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.77× (z +20.2) ⚠ cell-cycle shift, explains ~30% of this change | [[Harringtonine (drug)]] 5 µM 0.385× (z -14.5) ⚠ cell-cycle shift, explains ~65% of this change |
| [[C32 (line)]] | wt | 174 | 5 (5 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.64× (z +19.7) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[COLO 205 (line)]] | alt | 163 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.28× (z +23.6) | — |
| [[HCT15 (line)]] | alt | 554 | 0 | 5 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.396× (z -12.9) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 408 | 0 | 5 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.544× (z -14.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 750 | 0 | 5 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -17.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 305 | 5 (4 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.00× (z +20.7) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.66× (z +11.2) | — |
| [[A-427 (line)]] | wt | 396 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.308× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.298× (z -8.6) |
| [[A549 (line)]] | wt | 274 | 3 (3 ⚠) | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.02× (z +16.3) ⚠ cell-cycle shift, explains ~30% of this change | [[Harringtonine (drug)]] 5 µM 0.534× (z -9.4) ⚠ cell-cycle shift, explains ~65% of this change |
| [[H4 (line)]] | wt | 317 | 3 (2 ⚠) | 1 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.90× (z +11.3) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 1.87× (z +9.8) | [[TAK-901 (drug)]] 5 µM 0.211× (z -9.0) |
| [[HS-578T (line)]] | alt | 291 | 0 | 4 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.542× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 215 | 4 (3 ⚠) | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +10.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.02× (z +10.5) | — |
| [[LoVo (line)]] | wt | 273 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +21.7) | — |
| [[AsPC-1 (line)]] | alt | 461 | 1 (1 ⚠) | 2 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.64× (z +10.0) ⚠ unreliable plate only | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.297× (z -17.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Radotinib (drug)]] 5 µM 0.510× (z -9.8) |
| [[CFPAC-1 (line)]] | alt | 523 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.446× (z -12.4) ⚠ toxic |
| [[HOP62 (line)]] | alt | 322 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.56× (z +9.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.624× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 370 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.477× (z -15.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 182 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +17.0) | — |
| [[NCI-H1792 (line)]] | alt | 396 | 1 (1 ⚠) | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.85× (z +9.2) ⚠ cell-cycle shift, explains ~26% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.472× (z -16.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 272 | 1 | 2 (2 ⚠) | [[Bortezomib (drug)]] 0.05 µM 1.86× (z +8.6) | [[Docetaxel (drug)]] 0.05 µM 0.547× (z -10.1) ⚠ transcription drop; cell-cycle shift, explains ~30% of this change |
| [[LOX-IMVI (line)]] | wt | 330 | 0 | 2 | — | [[TAK-901 (drug)]] 5 µM 0.306× (z -9.6) |
| [[NCI-H2347 (line)]] | alt | 331 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.565× (z -9.1) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 347 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.20× (z +11.4) | — |
| [[RKO (line)]] | wt | 482 | 0 | 2 (1 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.254× (z -9.7) |
| [[SNU-1 (line)]] | wt | 277 | 2 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.05× (z +14.2) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.64× (z +9.2) | — |
| [[SW48 (line)]] | wt | 510 | 1 (1 ⚠) | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +10.2) ⚠ cell-cycle shift, explains ~30% of this change | [[Dinaciclib (drug)]] 5 µM 0.405× (z -10.2) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 457 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.57× (z +9.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.563× (z -12.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 223 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 1.95× (z +9.1) ⚠ cell-cycle shift, explains ~19% of this change | — |
| [[NCI-H23 (line)]] | alt | 217 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 1.93× (z +9.7) | — |
| [[RPMI-7951 (line)]] | alt | 288 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.542× (z -8.5) ⚠ cell-cycle shift, explains ~65% of this change |
| [[SNU-423 (line)]] | alt | 462 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.600× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 375 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 263 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 247 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 310 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 309 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 227 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 220 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 275 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7948), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SUPT3H]] | +0.67 | +0.62 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[ERC1]] | +0.64 | +0.55 / +0.67 | both halves | 1e-05 | **novel candidate** |
| [[SNX29]] | +0.54 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[SLC39A11]] | +0.53 | +0.46 / +0.54 | both halves | 2e-05 |  |
| [[BICD1]] | +0.52 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[SHLD2]] | +0.51 | +0.46 / +0.49 | both halves | 3e-05 |  |
| [[MPP3]] | +0.51 | +0.37 / +0.52 | both halves | 8e-05 |  |
| [[NLN]] | +0.51 | +0.41 / +0.57 | both halves | 4e-05 |  |
| [[ZNF83]] | +0.51 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[ADCY7]] | +0.50 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[EIF3J]] | +0.50 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[NPIPB4]] | +0.49 | +0.51 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PEX13]] | -0.50 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[YY1AP1]] | -0.50 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[CDKN1B]] | -0.49 | -0.41 / -0.58 | both halves | 4e-05 |  |
| [[PEX2]] | -0.47 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[FOXJ2]] | -0.47 | -0.38 / -0.54 | both halves | 6e-05 |  |
| [[PHF21A]] | -0.47 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[RHOXF1]] | -0.47 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[CBX8]] | -0.46 | -0.38 / -0.42 | both halves | 7e-05 |  |
| [[RAB20]] | -0.46 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[SERTAD3]] | -0.46 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[ZMYM3]] | -0.45 | -0.52 / -0.36 | both halves | 9e-05 |  |
| [[PXK]] | -0.45 | -0.48 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 211]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.710). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-2.0, -34.3); signed map (-17.7, 3.2). **Vector** length 143, 50.3% of its response variance represented; |z| ≥ 3 in 1,485 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +9.4 | +6.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +8.5 | +4.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +8.4 | +9.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +7.9 | +5.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +7.9 | +8.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.4 | +7.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +6.3 | +4.3 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +5.1 | +2.7 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -11.2 | -9.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -8.8 | -5.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -8.8 | -8.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | -7.6 | -9.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.2 | -5.3 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -2.5 | -1.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.4 | -0.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.3 | -2.5 |
|  | [[Anethole trithione (drug)]] 0.05 µM |  | -2.2 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | adenosine kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.2 — chr10:74,151,202-74,709,963 (+) |
| Ensembl biotype | protein_coding |
| Also known as | AK |
| Gene groups (HGNC) | Nucleoside/nucleotide kinases |
| Reactome | 5 pathways, smallest: Ribavirin ADME; Purine salvage; Nucleotide salvage |
| Matched by | ensembl_id |

**Function**, from UniProt [P55263](https://www.uniprot.org/uniprotkb/P55263) (Adenosine kinase):

> Adenosine kinase that mediates the phosphorylation of the purine nucleoside adenosine at the 5' position in an ATP-dependent manner: catalyzes phosphorylation of both unmodified and modified adenosines. Plays a key role in the detoxification of modified adenosines containing N(6)-methylated adenine (m6A) post-transcriptional modification. Modified nucleosides are derived from the degradation of RNAs (mRNAs, rRNAs and tRNAs) and possess intrinsic cytotoxicity and must be cleared to prevent …

**Summary**, from NCBI Gene [132](https://www.ncbi.nlm.nih.gov/gene/132):

> This gene an enzyme which catalyzes the transfer of the gamma-phosphate from ATP to adenosine, thereby serving as a regulator of concentrations of both extracellular adenosine and intracellular adenine nucleotides. Adenosine has widespread effects on the cardiovascular, nervous, respiratory, and immune systems and inhibitors of the enzyme could play an important pharmacological role in increasing intravascular adenosine concentrations and acting as anti-inflammatory agents. Multiple transcript …

**Accessions** — [HGNC:257](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:257) · Entrez [132](https://www.ncbi.nlm.nih.gov/gene/132) · UniProt [P55263](https://www.uniprot.org/uniprotkb/P55263) · Ensembl [ENSG00000156110](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156110)

## Data

Gene col 7948: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7948); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7948, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7948]; `tensor/DDL_lfc|DDL_z.npy` [7948]; `embed/gene_vectors.npy` [7948]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7948 or target_col == 7948). Every well: [[ADK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
