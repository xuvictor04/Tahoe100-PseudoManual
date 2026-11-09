---
symbol: "PIK3R1"
type: "gene"
col: 7010
ensembl_id: "ENSG00000145675"
name: "phosphoinositide-3-kinase regulatory subunit 1"
location: "5q13.1"
module: 113
arm: "+"
pooled_cpm: 59.82
n_lines_expressing: 48
n_dd_up: 25
n_dd_down: 16
n_dd_up_clean: 18
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/113"]
generated_by: "tahoemap"
---

# PIK3R1

*phosphoinositide-3-kinase regulatory subunit 1* — 5q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.15× (z +24.3, q 0e+00, up in 41 of 46 measured lines) ⚠ position correction uncertain. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.88× (z +19.9, q 0e+00, up in 41 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.417× (z -18.2, q 0e+00, down in 31 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.710× (z -7.7, q 1e-12, down in 31 of 46 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZMYND8]] (+0.65, fdr 1e-05), [[MAP3K1]] (+0.64, fdr 7e-06), [[IRX3]] (+0.58, fdr 1e-05); moves opposite to [[IRGQ]] (-0.50, fdr 3e-05), [[CAMSAP1-DT]] (-0.49, fdr 5e-05), [[RAB22A]] (-0.48, fdr 2e-05).
> It is in [[Module 113]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TLR2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 9 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7010.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ position correction uncertain | **2.15×** | +24.3 | 0e+00 | 41/46 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.88×** | +19.9 | 0e+00 | 41/47 (LoVo, A-172, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.43×** | +19.9 | 0e+00 | 44/46 (NCI-H2030, LoVo, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **2.21×** | +17.8 | 0e+00 | 40/46 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.05×** | +16.1 | 0e+00 | 41/46 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.58×** | +10.2 | 1e-22 | 41/46 (A-427, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.37×** | +10.1 | 4e-22 | 35/47 (SNU-423, A-172, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.59×** | +9.9 | 2e-21 | 36/46 (SW480, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ position correction uncertain | **1.50×** | +8.4 | 3e-15 | 31/46 (SW480, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.44×** | +7.9 | 2e-13 | 28/46 (SW480, A-172, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.38×** | +6.9 | 2e-10 | 23/48 (SW480, A-172, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.76×** | +6.6 | 1e-09 | 29/46 (NCI-H2347, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +6.3 | 1e-08 | 22/46 (NCI-H2347, LOX-IMVI, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.31×** | +6.1 | 6e-08 | 26/46 (A-427, HepG2/C3A, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.31×** | +6.0 | 1e-07 | 28/47 (NCI-H2347, HT-29, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.29×** | +5.7 | 3e-07 | 22/46 (A-172, HS-578T, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.29×** | +5.7 | 4e-07 | 26/46 (LoVo, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.60×** | +5.5 | 1e-06 | 25/47 (LoVo, AsPC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.25×** | +5.0 | 2e-05 | 23/46 (HS-578T, Hs 766T, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.24×** | +4.9 | 3e-05 | 20/46 (Hs 766T, HS-578T, …) | all doses, flat |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +4.8 | 5e-05 | 21/46 (Hs 766T, H4, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.22×** | +4.5 | 1e-04 | 20/46 (HS-578T, LOX-IMVI, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7010.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.417×** | -18.2 | 0e+00 | 31/42 (LS 180, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.437×** | -17.9 | 0e+00 | 34/40 (HEC-1-A, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.493×** | -15.9 | 0e+00 | 38/46 (A498, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.648×** | -9.7 | 3e-20 | 32/46 (COLO 205, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.901× | -8.0 | 1e-13 | 5/47 (HOP62, NCI-H1792, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.710×** | -7.7 | 1e-12 | 31/46 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.711×** | -7.7 | 1e-12 | 27/46 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.807×** | -6.8 | 6e-10 | 23/47 (SK-MEL-2, AN3 CA, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.738×** | -6.4 | 1e-08 | 25/46 (C-33 A, AN3 CA, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.773×** | -5.8 | 4e-07 | 22/46 (PANC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.810×** | -4.8 | 1e-04 | 20/46 (A498, SNU-1, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.827×** | -4.3 | 9e-04 | 19/46 (C32, A498, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.830×** | -4.2 | 0.001 | 17/46 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 0.836× | -4.0 | 0.002 | 20/45 (CFPAC-1, A498, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.833×** | -4.0 | 0.003 | 15/45 (RPMI-7951, A498, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.839× | -3.9 | 0.003 | 15/46 (CFPAC-1, A498, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.846× | -3.8 | 0.006 | 16/45 (SK-MEL-2, RPMI-7951, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 5 µM |  | 0.891× | -3.7 | 0.007 | 3/47 (C-33 A, NCI-H460, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 5 µM |  | **0.731×** | -3.7 | 0.007 | 17/44 (SK-MEL-2, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **0.812×** | -3.3 | 0.022 | 11/46 (AN3 CA, C32, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Ivermectin (drug)]] 5 µM |  | 0.881× | -2.9 | 0.100 | 3/46 (Panc 03.27, NCI-H2347, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7010. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 52.7 | 5 (3 ⚠) | 5 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.22× (z +13.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Belinostat (drug)]] 5 µM 3.12× (z +12.8) | [[Dinaciclib (drug)]] 0.5 µM 0.391× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.425× (z -9.7) |
| [[SW480 (line)]] | alt | 73.4 | 7 (4 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +24.1) ⚠ position correction uncertain · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +14.3) | [[Dinaciclib (drug)]] 0.05 µM 0.358× (z -13.4) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 62.2 | 4 (2 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +19.6) ⚠ position correction uncertain · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.0526× (z -34.7) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 70.6 | 6 | 2 (2 ⚠) | [[Triamcinolone (drug)]] 5 µM 2.34× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.323× (z -10.5) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 56.0 | 8 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.13× (z +19.1) ⚠ position correction uncertain · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.12× (z +12.0) | — |
| [[LOX-IMVI (line)]] | wt | 53.4 | 7 (3 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.92× (z +15.3) | [[Dinaciclib (drug)]] 5 µM 0.264× (z -12.9) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 73.0 | 4 (2 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +18.5) ⚠ position correction uncertain · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.87× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.314× (z -12.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 63.5 | 7 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.37× (z +19.6) ⚠ position correction uncertain · without an alert: [[TAK-901 (drug)]] 5 µM 14.3× (z +13.1) | [[Dinaciclib (drug)]] 5 µM 0.322× (z -10.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 62.3 | 7 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.17× (z +16.5) | — |
| [[A498 (line)]] | wt | 79.5 | 2 (1 ⚠) | 5 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.176× (z -20.3) ⚠ toxic; transcription drop · without an alert: [[5-Azacytidine (drug)]] 5 µM 0.405× (z -10.6) |
| [[HS-578T (line)]] | alt | 71.3 | 6 | 1 (1 ⚠) | [[Clobetasol propionate (drug)]] 0.05 µM 2.96× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.345× (z -9.9) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 96.6 | 3 (2 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +13.4) ⚠ position correction uncertain · without an alert: [[Belinostat (drug)]] 5 µM 2.44× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.324× (z -12.2) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 55.3 | 4 (2 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +15.3) ⚠ position correction uncertain · without an alert: [[Belinostat (drug)]] 5 µM 2.31× (z +9.2) | [[Dinaciclib (drug)]] 0.05 µM 0.346× (z -10.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 64.0 | 4 (3 ⚠) | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +11.5) | [[Trametinib (drug)]] 5 µM 0.413× (z -8.8) ⚠ cell-cycle shift, explains ~72% of this change |
| [[A-427 (line)]] | wt | 41.5 | 4 (2 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.81× (z +12.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Belinostat (drug)]] 5 µM 3.71× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.247× (z -12.4) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 39.5 | 5 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.37× (z +22.3) ⚠ position correction uncertain · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.73× (z +20.0) | [[Dinaciclib (drug)]] 5 µM 0.311× (z -12.0) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 36.8 | 4 (2 ⚠) | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +11.3) | [[Dinaciclib (drug)]] 0.05 µM 0.197× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.289× (z -10.5) |
| [[SW 900 (line)]] | alt | 40.0 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.77× (z +17.2) ⚠ position correction uncertain · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.03× (z +12.2) | — |
| [[AN3 CA (line)]] | alt | 393 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0722× (z -17.9) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.243× (z -9.6) |
| [[AsPC-1 (line)]] | alt | 23.5 | 5 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 7.20× (z +12.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Belinostat (drug)]] 5 µM 5.11× (z +10.7) | — |
| [[NCI-H2347 (line)]] | alt | 55.2 | 4 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +14.9) ⚠ position correction uncertain | [[Dinaciclib (drug)]] 0.5 µM 0.324× (z -11.3) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 98.3 | 4 (3 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.04× (z +12.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.48× (z +10.3) | [[Dinaciclib (drug)]] 0.05 µM 0.354× (z -10.9) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 76.4 | 2 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.93× (z +18.3) ⚠ position correction uncertain · without an alert: [[TAK-901 (drug)]] 5 µM 6.37× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.280× (z -12.1) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 133 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +9.2) ⚠ position correction uncertain | [[Dinaciclib (drug)]] 5 µM 0.151× (z -21.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 19.0 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.82× (z +13.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Belinostat (drug)]] 5 µM 5.45× (z +11.7) | — |
| [[NCI-H23 (line)]] | alt | 24.0 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.47× (z +11.9) | — |
| [[RKO (line)]] | wt | 55.3 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +12.6) | — |
| [[RPMI-7951 (line)]] | alt | 128 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +9.8) ⚠ position correction uncertain | [[Dinaciclib (drug)]] 5 µM 0.198× (z -14.0) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 74.3 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +9.1) ⚠ position correction uncertain | [[Digitoxin (drug)]] 5 µM 0.289× (z -11.1) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 92.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.167× (z -13.0) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 30.6 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.51× (z +11.5) | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.222× (z -9.0) |
| [[C32 (line)]] | wt | 81.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +15.3) ⚠ position correction uncertain | [[Dinaciclib (drug)]] 0.05 µM 0.375× (z -8.7) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 18.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.91× (z +15.8) ⚠ position correction uncertain · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +9.0) | — |
| [[NCI-H1792 (line)]] | alt | 55.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.23× (z +18.6) ⚠ position correction uncertain · without an alert: [[Clobetasol propionate (drug)]] 5 µM 2.93× (z +8.6) | — |
| [[SHP-77 (line)]] | alt | 58.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.156× (z -17.1) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 44.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +12.0) ⚠ position correction uncertain · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.53× (z +11.8) | — |
| [[A549 (line)]] | wt | 39.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +9.7) | — |
| [[CHP-212 (line)]] | wt | 64.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0711× (z -13.6) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 63.6 | 1 | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 4.02× (z +9.6) | — |
| [[KATO III (line)]] | alt | 136 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.321× (z -10.8) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 98.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.147× (z -9.8) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 59.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 41.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.1 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 57.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 60.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 157 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.29 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7010), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZMYND8]] | +0.65 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[MAP3K1]] | +0.64 | +0.61 / +0.63 | both halves | 7e-06 | pathway: Fc epsilon receptor (FCERI) signaling; STRING 472 |
| [[IRX3]] | +0.58 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[MAPK14]] | +0.56 | +0.39 / +0.64 | both halves | 5e-05 | pathway: Platelet activation, signaling and aggregation |
| [[UGP2]] | +0.55 | +0.49 / +0.46 | both halves | 3e-05 |  |
| [[ITGA10]] | +0.55 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[FOXC2]] | +0.53 | +0.38 / +0.57 | both halves | 6e-05 |  |
| [[MT1E]] | +0.53 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[TSC22D3]] | +0.53 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[TNS2]] | +0.53 | +0.44 / +0.48 | both halves | 3e-05 | same gene group |
| [[MT1F]] | +0.52 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[TLR2]] | +0.51 | +0.45 / +0.50 | both halves | 3e-05 | STRING 641 |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IRGQ]] | -0.50 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[CAMSAP1-DT]] | -0.49 | -0.39 / -0.50 | both halves | 5e-05 |  |
| [[RAB22A]] | -0.48 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[DCAKD]] | -0.48 | -0.52 / -0.34 | both halves | 1e-04 |  |
| [[IGFN1]] | -0.48 | -0.30 / -0.49 | both halves | 2e-04 |  |
| [[CASTOR3P-1]] | -0.47 | -0.28 / -0.43 | both halves | 3e-04 |  |
| [[TEKTIP1]] | -0.47 | -0.28 / -0.53 | both halves | 3e-04 |  |
| [[MAFK]] | -0.47 | -0.37 / -0.51 | both halves | 8e-05 |  |
| [[KCTD13]] | -0.47 | -0.38 / -0.38 | both halves | 6e-05 | pathway: RND2 GTPase cycle |
| [[GDI1]] | -0.46 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[FAM229A]] | -0.46 | -0.42 / -0.39 | both halves | 5e-05 |  |
| [[TBILA]] | -0.46 | -0.33 / -0.48 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TLR2]] | B | TLR2 activity raises PIK3R1's level | lines that do not express TLR2 (26) vs lines expressing it (24) | 1.25× lower at baseline in the lines without TLR2 | 0.075 | ⚠ within organs, on part of the lines; also absent: FYB1, DDIT4L, EDNRA |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 113]] — hypoxia; 43 genes; every member is in the + arm (projection on the module's main direction 0.513). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (23.8, 15.0); signed map (15.3, 30.6). **Vector** length 111, 31.4% of its response variance represented; |z| ≥ 3 in 1,643 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ position correction uncertain | +6.6 | +24.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.5 | +9.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.4 | +10.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +4.7 | +3.9 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +4.6 | +3.6 |
|  | [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | +4.4 | +4.8 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +4.3 | +2.4 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +4.3 | +3.1 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -10.0 | -17.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -8.8 | -15.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -8.2 | -18.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.9 | -4.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.2 | +2.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.1 | -6.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.9 | -6.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.7 | -3.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.1 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | phosphoinositide-3-kinase regulatory subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q13.1 — chr5:68,215,740-68,301,821 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GRB1, p85-ALPHA, p85, p85alpha |
| Gene groups (HGNC) | SH2 domain containing; SH3 domain containing |
| Reactome | 150 pathways, smallest: Activated NTRK2 signals through PI3K; Activated NTRK3 signals through PI3K; Co-stimulation by ICOS |
| Matched by | ensembl_id |

**Function**, from UniProt [P27986](https://www.uniprot.org/uniprotkb/P27986) (Phosphatidylinositol 3-kinase regulatory subunit alpha):

> Binds to activated (phosphorylated) protein-Tyr kinases, through its SH2 domain, and acts as an adapter, mediating the association of the p110 catalytic unit to the plasma membrane. Necessary for the insulin-stimulated increase in glucose uptake and glycogen synthesis in insulin-sensitive tissues. Plays an important role in signaling in response to FGFR1, FGFR2, FGFR3, FGFR4, KITLG/SCF, KIT, PDGFRA and PDGFRB. Likewise, plays a role in ITGB2 signaling. Modulates the cellular response to ER …

**Summary**, from NCBI Gene [5295](https://www.ncbi.nlm.nih.gov/gene/5295):

> Phosphatidylinositol 3-kinase phosphorylates the inositol ring of phosphatidylinositol at the 3-prime position. The enzyme comprises a 110 kD catalytic subunit and a regulatory subunit of either 85, 55, or 50 kD. This gene encodes the 85 kD regulatory subunit. Phosphatidylinositol 3-kinase plays an important role in the metabolic actions of insulin, and a mutation in this gene has been associated with insulin resistance. Alternative splicing of this gene results in four transcript variants …

**Accessions** — [HGNC:8979](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8979) · Entrez [5295](https://www.ncbi.nlm.nih.gov/gene/5295) · UniProt [P27986](https://www.uniprot.org/uniprotkb/P27986) · Ensembl [ENSG00000145675](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145675)

## Data

Gene col 7010: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7010); `tables/drug_effects.parquet` (66 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7010, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7010]; `tensor/DDL_lfc|DDL_z.npy` [7010]; `embed/gene_vectors.npy` [7010]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7010 or target_col == 7010). Every well: [[PIK3R1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PIK3R1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
