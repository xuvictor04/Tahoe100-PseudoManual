---
symbol: "HEXB"
type: "gene"
col: 557
ensembl_id: "ENSG00000049860"
name: "hexosaminidase subunit beta"
location: "5q13.3"
module: 29
arm: "+"
pooled_cpm: 59.35
n_lines_expressing: 50
n_dd_up: 41
n_dd_down: 1
n_dd_up_clean: 21
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# HEXB

*hexosaminidase subunit beta* — 5q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 41 drug-doses (20 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.20× (z +22.5, q 0e+00, up in 43 of 48 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.87× (z +21.3, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.897× (z -7.5, q 3e-11, down in 2 of 49 measured lines) ⚠ position not correctable. The strongest without an alert is [[Verteporfin (drug)]] 5 µM: 0.741× (z -5.8, q 2e-06, down in 31 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Verteporfin (drug)]] 5 µM in 1 line (hTERT-HPNE 0.244×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (RKO 0.397×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change); [[Selinexor (drug)]] 5 µM in 1 line (Hs 766T 0.478×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[M6PR]] (+0.58, fdr 1e-05), [[IGF2R]] (+0.58, fdr 1e-05), [[LAMP2]] (+0.56, fdr 1e-05); moves opposite to [[ZNHIT3]] (-0.58, fdr 1e-05), [[ZNF500]] (-0.55, fdr 3e-05), [[MRPS26]] (-0.54, fdr 3e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SCRN1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 55 in all, 25 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 41 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 557.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.20×** | +22.5 | 0e+00 | 43/48 (NCI-H460, NCI-H2030, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.87×** | +21.3 | 0e+00 | 47/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.47×** | +18.2 | 0e+00 | 47/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **2.26×** | +16.4 | 0e+00 | 42/49 (NCI-H460, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **2.29×** | +16.0 | 0e+00 | 36/41 (KATO III, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.20×** | +15.9 | 0e+00 | 46/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.16×** | +15.6 | 0e+00 | 45/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +11.6 | 2e-29 | 37/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.78×** | +11.6 | 2e-29 | 43/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.81×** | +11.1 | 6e-27 | 37/44 (NCI-H1573, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.76×** | +10.9 | 4e-26 | 42/48 (NCI-H1573, PANC-1, …) | rises with dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.72×** | +10.9 | 5e-26 | 39/48 (MIA PaCa-2, PANC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.71×** | +10.8 | 2e-25 | 43/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.64×** | +9.9 | 1e-21 | 42/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.62×** | +9.8 | 6e-21 | 34/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +6.5 | 2e-09 | 27/48 (NCI-H2347, SW480, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.82×** | +6.3 | 8e-09 | 34/48 (PANC-1, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +4.7 | 6e-05 | 19/48 (HOP62, A-172, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.54×** | +4.6 | 1e-04 | 24/48 (SW480, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.54×** | +4.5 | 1e-04 | 19/48 (HT-29, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.36×** | +4.4 | 2e-04 | 23/48 (HT-29, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.50×** | +4.3 | 3e-04 | 21/48 (HT-29, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.49×** | +4.2 | 5e-04 | 21/48 (HT-29, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **1.24×** | +4.1 | 7e-04 | 23/48 (RKO, MIA PaCa-2, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 557.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Verteporfin (drug)]] 5 µM in 1 line (hTERT-HPNE 0.244×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (RKO 0.397×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change); [[Selinexor (drug)]] 5 µM in 1 line (Hs 766T 0.478×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.897× | -7.5 | 3e-11 | 2/49 (NCI-H23, CHP-212) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.741×** | -5.8 | 2e-06 | 31/48 (hTERT-HPNE, HS-578T, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | 0.846× | -3.2 | 0.21 | 15/47 (HEC-1-A, J82, …) | top dose only |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.895× | -3.2 | 0.21 | 5/48 (A549, NCI-H23, …) | top dose only |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 0.860× | -3.1 | 0.25 | 13/48 (SW480, RPMI-7951, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 557. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 76.8 | 15 (8 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 8.56× (z +27.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 75.9 | 11 (8 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +20.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.38× (z +13.1) | — |
| [[NCI-H1573 (line)]] | alt | 34.1 | 11 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.93× (z +22.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.84× (z +14.4) | — |
| [[PANC-1 (line)]] | alt | 60.7 | 11 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +21.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.34× (z +17.8) | — |
| [[LOX-IMVI (line)]] | wt | 41.5 | 10 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +19.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.09× (z +12.5) | — |
| [[A-172 (line)]] | wt | 96.4 | 9 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +16.7) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.76× (z +9.8) | — |
| [[A-427 (line)]] | wt | 96.0 | 9 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +16.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.66× (z +11.6) | — |
| [[AsPC-1 (line)]] | alt | 36.5 | 8 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.10× (z +21.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.60× (z +12.5) | — |
| [[SW480 (line)]] | alt | 42.0 | 8 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.33× (z +21.0) | — |
| [[CFPAC-1 (line)]] | alt | 37.7 | 7 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +14.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.71× (z +9.2) | — |
| [[HOP62 (line)]] | alt | 47.5 | 7 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.40× (z +15.9) | — |
| [[Hs 766T (line)]] | wt | 48.6 | 6 (3 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.59× (z +17.0) | [[Selinexor (drug)]] 5 µM 0.478× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 62.3 | 7 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.80× (z +17.8) | — |
| [[KATO III (line)]] | alt | 82.4 | 7 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.55× (z +17.1) | — |
| [[LoVo (line)]] | wt | 72.4 | 6 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.29× (z +13.8) | — |
| [[LS 180 (line)]] | wt | 65.3 | 6 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.97× (z +14.6) | — |
| [[NCI-H23 (line)]] | alt | 34.5 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.42× (z +16.7) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 5.66× (z +13.8) | — |
| [[RKO (line)]] | wt | 95.4 | 5 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +14.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.16× (z +12.0) | [[Dinaciclib (drug)]] 0.5 µM 0.397× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[BT-474 (line)]] | alt | 31.6 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.66× (z +13.0) | — |
| [[SNU-1 (line)]] | wt | 68.6 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.16× (z +13.4) | — |
| [[COLO 205 (line)]] | alt | 79.1 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.04× (z +21.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 9.06× (z +16.2) | — |
| [[A498 (line)]] | wt | 64.1 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.77× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.93× (z +10.4) | — |
| [[C32 (line)]] | wt | 84.6 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.18× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.83× (z +9.5) | — |
| [[J82 (line)]] | alt | 90.2 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +13.7) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.84× (z +13.0) | — |
| [[NCI-H2030 (line)]] | alt | 45.6 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.34× (z +23.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.86× (z +13.6) | — |
| [[SNU-423 (line)]] | alt | 96.7 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.40× (z +9.5) | — |
| [[A549 (line)]] | wt | 47.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +12.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.80× (z +9.7) | — |
| [[H4 (line)]] | wt | 58.0 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.96× (z +9.0) | — |
| [[HEC-1-A (line)]] | alt | 51.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.26× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[HepG2_C3A (line)]] | wt | 38.8 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.43× (z +10.3) | — |
| [[HS-578T (line)]] | alt | 50.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.15× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[NCI-H1792 (line)]] | alt | 27.2 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.44× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.56× (z +9.2) | — |
| [[NCI-H2347 (line)]] | alt | 77.4 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +12.9) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[Panc 03.27 (line)]] | alt | 43.7 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +10.2) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 60.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.24× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 77.3 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.244× (z -10.6) |
| [[RPMI-7951 (line)]] | alt | 57.7 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.89× (z +8.7) | — |
| [[SHP-77 (line)]] | alt | 35.7 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.89× (z +9.9) | — |
| [[SW 900 (line)]] | alt | 49.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +10.4) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[SW1417 (line)]] | alt | 36.2 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.52× (z +10.9) | — |
| [[SW48 (line)]] | wt | 57.0 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.26× (z +10.4) | — |
| [[AN3 CA (line)]] | alt | 131 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 65.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 92.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 87.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 557), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[M6PR]] | +0.58 | +0.58 / +0.50 | both halves | 1e-05 | pathway: Glycosphingolipid catabolism |
| [[IGF2R]] | +0.58 | +0.53 / +0.56 | both halves | 1e-05 | STRING 550 |
| [[LAMP2]] | +0.56 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[OSTM1]] | +0.55 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[PEPD]] | +0.55 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[SLC36A1]] | +0.53 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[GNS]] | +0.52 | +0.54 / +0.46 | both halves | 3e-05 | pathway: Diseases of metabolism; STRING 941 |
| [[TPP1]] | +0.52 | +0.52 / +0.46 | both halves | 2e-05 | STRING 437 |
| [[LAMP1]] | +0.52 | +0.49 / +0.48 | both halves | 2e-05 | STRING 414 |
| [[GNPDA1]] | +0.52 | +0.54 / +0.51 | both halves | 1e-05 | pathway: Metabolism of carbohydrates and carbohydrate derivatives; STRING 460 |
| [[CTNNAL1]] | +0.51 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[ATP6AP1]] | +0.50 | +0.54 / +0.36 | both halves | 9e-05 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNHIT3]] | -0.58 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[ZNF500]] | -0.55 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[MRPS26]] | -0.54 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[TMEM208]] | -0.53 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[TARS2]] | -0.53 | -0.37 / -0.53 | both halves | 8e-05 |  |
| [[CLASRP]] | -0.52 | -0.56 / -0.43 | both halves | 4e-05 |  |
| [[DRG1]] | -0.52 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[MPHOSPH10]] | -0.52 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[ZW10]] | -0.50 | -0.58 / -0.27 | both halves | 3e-04 |  |
| [[CHST12]] | -0.49 | -0.46 / -0.44 | both halves | 3e-05 | pathway: Chondroitin sulfate/dermatan sulfate metabolism |
| [[SCNM1]] | -0.48 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[TFB2M]] | -0.47 | -0.47 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SCRN1]] | B | SCRN1 activity lowers HEXB's level | lines that do not express SCRN1 (8) vs lines expressing it (42) | 1.46× higher at baseline in the lines without SCRN1 | 0.036 | ⚠ within organs, on part of the lines; also absent: PPFIA4 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.324). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-22.1, -20.1); signed map (7.4, -8.4). **Vector** length 92.5, 27.6% of its response variance represented; |z| ≥ 3 in 1,300 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | +9.0 | +16.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | +8.6 | +16.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.6 | +6.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | +6.5 | +11.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +6.0 | +18.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +10.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +4.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.3 | +6.3 |
|  | [[Belzutifan (drug)]] 5 µM |  | +2.7 | +3.4 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -3.8 | +1.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.7 | +3.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.6 | +0.2 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | +1.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.7 | +1.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.6 | -5.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.2 | +0.7 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.0 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | hexosaminidase subunit beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q13.3 — chr5:74,640,023-74,722,647 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Hexosaminidases |
| Reactome | 17 pathways, smallest: Keratan sulfate degradation; Hyaluronan degradation; CS/DS degradation |
| Matched by | ensembl_id |

**Function**, from UniProt [P07686](https://www.uniprot.org/uniprotkb/P07686) (Beta-hexosaminidase subunit beta):

> Hydrolyzes the non-reducing end N-acetyl-D-hexosamine and/or sulfated N-acetyl-D-hexosamine of glycoconjugates, such as the oligosaccharide moieties from proteins and neutral glycolipids, or from certain mucopolysaccharides. The isozyme B does not hydrolyze each of these substrates, however hydrolyzes efficiently neutral oligosaccharide. Only the isozyme A is responsible for the degradation of GM2 gangliosides in the presence of GM2A. During fertilization is responsible, at least in part, for …

**Summary**, from NCBI Gene [3074](https://www.ncbi.nlm.nih.gov/gene/3074):

> Hexosaminidase B is the beta subunit of the lysosomal enzyme beta-hexosaminidase that, together with the cofactor GM2 activator protein, catalyzes the degradation of the ganglioside GM2, and other molecules containing terminal N-acetyl hexosamines. Beta-hexosaminidase is composed of two subunits, alpha and beta, which are encoded by separate genes. Both beta-hexosaminidase alpha and beta subunits are members of family 20 of glycosyl hydrolases. Mutations in the alpha or beta subunit genes lead …

**Accessions** — [HGNC:4879](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4879) · Entrez [3074](https://www.ncbi.nlm.nih.gov/gene/3074) · UniProt [P07686](https://www.uniprot.org/uniprotkb/P07686) · Ensembl [ENSG00000049860](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000049860)

## Data

Gene col 557: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 557); `tables/drug_effects.parquet` (60 rows, flagged included); `relations/gene_relations.parquet` (col_a == 557, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 557]; `tensor/DDL_lfc|DDL_z.npy` [557]; `embed/gene_vectors.npy` [557]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 557 or target_col == 557). Every well: [[HEXB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HEXB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
