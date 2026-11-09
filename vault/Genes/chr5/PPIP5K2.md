---
symbol: "PPIP5K2"
type: "gene"
col: 7017
ensembl_id: "ENSG00000145725"
name: "diphosphoinositol pentakisphosphate kinase 2"
location: "5q21.1"
module: 20
arm: "+"
pooled_cpm: 85.63
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 22
n_dd_up_clean: 1
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# PPIP5K2

*diphosphoinositol pentakisphosphate kinase 2* — 5q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.71× (z +9.1, q 6e-17, up in 35 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 1.31× (z +4.5, q 9e-04, up in 23 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (LoVo 3.21×, NCI-H460 2.56×, HT-29 2.57×, RKO 2.60×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (LoVo 3.05×, HT-29 2.93×, A549 2.58×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (HT-29 2.42×, SW1417 2.31×, Panc 03.27 1.87×; ⚠ cell-cycle shift, explains ~9% of this change).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (8 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.407× (z -15.7, q 0e+00, down in 47 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.476× (z -13.0, q 4e-36, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TPP2]] (+0.64, fdr 7e-06), [[GDI2]] (+0.61, fdr 1e-05), [[SPTLC1]] (+0.60, fdr 4e-05); moves opposite to [[PIM3]] (-0.62, fdr 3e-05), [[PPP2R2A]] (-0.59, fdr 1e-05), [[MIR210HG]] (-0.52, fdr 5e-05).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7017.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (LoVo 3.21×, NCI-H460 2.56×, HT-29 2.57×, RKO 2.60×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (LoVo 3.05×, HT-29 2.93×, A549 2.58×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (HT-29 2.42×, SW1417 2.31×, Panc 03.27 1.87×; ⚠ cell-cycle shift, explains ~9% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.71×** | +9.1 | 6e-17 | 35/44 (LoVo, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.63×** | +8.5 | 4e-15 | 38/49 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **1.20×** | +4.6 | 7e-04 | 22/49 (HT-29, SW1417, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +4.5 | 9e-04 | 23/48 (HT-29, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.28×** | +4.0 | 0.008 | 23/45 (RPMI-7951, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.1 | 0.21 | 20/50 (HT-29, Panc 03.27, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7017.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.407×** | -15.7 | 0e+00 | 47/48 (PANC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.550×** | -14.8 | 0e+00 | 40/48 (A549, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.476×** | -13.0 | 4e-36 | 48/48 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.514×** | -11.2 | 7e-27 | 43/48 (KATO III, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.539×** | -10.8 | 4e-25 | 44/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.568×** | -9.9 | 6e-21 | 38/48 (A-427, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.599×** | -8.9 | 3e-17 | 42/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.610×** | -8.6 | 4e-16 | 39/48 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.446×** | -7.4 | 1e-11 | 46/49 (A-427, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.503×** | -6.3 | 2e-08 | 43/48 (SW480, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **0.707×** | -5.8 | 3e-07 | 29/47 (KATO III, HCT15, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.752×** | -5.0 | 3e-05 | 29/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.819×** | -4.9 | 4e-05 | 27/48 (SW480, A-427, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.780×** | -4.3 | 6e-04 | 27/48 (HT-29, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~76% of this change | **0.791×** | -4.1 | 0.002 | 26/48 (CFPAC-1, Hs 766T, …) | inconsistent across doses | low cells (technical?) |
| [[Amsacrine (drug)]] 5 µM |  | 0.870× | -3.4 | 0.022 | 11/48 (A498, MIA PaCa-2, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.874× | -3.3 | 0.026 | 13/49 (CFPAC-1, CHP-212, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.766×** | -3.3 | 0.026 | 21/48 (MIA PaCa-2, HT-29, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.831×** | -3.2 | 0.035 | 21/49 (SW480, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[vincristine (drug)]] 5 µM |  | **0.707×** | -3.2 | 0.039 | 18/46 (HCT15, AN3 CA, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7017. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 87.9 | 1 (1 ⚠) | 10 (4 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.56× (z +11.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -16.3) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.286× (z -15.6) |
| [[SW480 (line)]] | alt | 122 | 0 | 9 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.279× (z -17.5) |
| [[A549 (line)]] | wt | 70.3 | 1 (1 ⚠) | 7 (3 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.58× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -18.8) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.211× (z -15.5) |
| [[PANC-1 (line)]] | alt | 105 | 0 | 8 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.264× (z -16.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.336× (z -13.6) |
| [[HOP62 (line)]] | alt | 75.0 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -16.8) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.318× (z -11.0) |
| [[A-427 (line)]] | wt | 131 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.285× (z -16.4) |
| [[AsPC-1 (line)]] | alt | 77.7 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.204× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.254× (z -14.0) |
| [[CFPAC-1 (line)]] | alt | 90.4 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -12.8) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.352× (z -11.3) |
| [[H4 (line)]] | wt | 158 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -11.9) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.362× (z -9.2) |
| [[HT-29 (line)]] | alt | 46.4 | 4 (4 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +12.4) ⚠ cell-cycle shift, explains ~9% of this change | [[Digitoxin (drug)]] 5 µM 0.421× (z -8.7) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 72.1 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.209× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.333× (z -11.3) |
| [[SNU-423 (line)]] | alt | 91.0 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -17.9) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.406× (z -8.9) |
| [[SW 1088 (line)]] | alt | 144 | 0 | 5 (2 ⚠) | — | [[Temsirolimus (drug)]] 0.5 µM 0.0903× (z -10.0) |
| [[A498 (line)]] | wt | 136 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -14.4) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.305× (z -11.3) |
| [[MIA PaCa-2 (line)]] | alt | 93.5 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.354× (z -9.8) |
| [[Panc 03.27 (line)]] | alt | 67.7 | 2 (2 ⚠) | 2 (2 ⚠) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.54× (z +9.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -12.4) ⚠ cell-cycle shift, explains ~44% of this change |
| [[SW1417 (line)]] | alt | 41.2 | 1 (1 ⚠) | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +10.4) ⚠ cell-cycle shift, explains ~9% of this change | [[Digitoxin (drug)]] 5 µM 0.296× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.335× (z -9.6) |
| [[AN3 CA (line)]] | alt | 139 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.278× (z -9.1) |
| [[Hs 766T (line)]] | wt | 142 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -13.5) ⚠ cell-cycle shift, explains ~44% of this change |
| [[hTERT-HPNE (line)]] | wt | 91.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -12.6) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.366× (z -9.2) |
| [[NCI-H1573 (line)]] | alt | 99.6 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.328× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.342× (z -12.0) |
| [[NCI-H1792 (line)]] | alt | 133 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.358× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.416× (z -9.4) |
| [[RPMI-7951 (line)]] | alt | 88.9 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.454× (z -10.4) ⚠ cell-cycle shift, explains ~44% of this change |
| [[SW 900 (line)]] | alt | 60.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.286× (z -11.6) |
| [[A-172 (line)]] | wt | 75.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -14.4) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.366× (z -9.7) |
| [[HepG2_C3A (line)]] | wt | 54.3 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.177× (z -13.4) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 102 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -14.6) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.358× (z -9.0) |
| [[LoVo (line)]] | wt | 55.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.21× (z +13.8) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 79.4 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.432× (z -9.3) |
| [[NCI-H2347 (line)]] | alt | 72.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Selinexor (drug)]] 5 µM 1.90× (z +10.2) ⚠ cell-cycle shift, would explain all of this change | [[Digitoxin (drug)]] 5 µM 0.441× (z -9.2) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 81.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.80× (z +9.1) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.270× (z -11.5) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 42.2 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.285× (z -9.4) |
| [[COLO 205 (line)]] | alt | 85.7 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.345× (z -8.7) |
| [[HCT15 (line)]] | alt | 78.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.196× (z -13.3) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 56.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -12.9) ⚠ cell-cycle shift, explains ~44% of this change |
| [[NCI-H2030 (line)]] | alt | 57.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.56× (z +8.6) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 91.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.60× (z +9.3) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 83.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.350× (z -8.5) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 56.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.10× (z +8.5) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 82.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 53.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 98.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 73.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 91.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 68.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 78.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 75.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 98.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7017), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPP2]] | +0.64 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[GDI2]] | +0.61 | +0.49 / +0.73 | both halves | 1e-05 |  |
| [[SPTLC1]] | +0.60 | +0.41 / +0.63 | both halves | 4e-05 |  |
| [[AP2B1]] | +0.60 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[ACO2]] | +0.56 | +0.42 / +0.62 | both halves | 4e-05 |  |
| [[SELENOF]] | +0.56 | +0.40 / +0.58 | both halves | 5e-05 |  |
| [[RPN1]] | +0.55 | +0.36 / +0.55 | both halves | 1e-04 |  |
| [[ATM]] | +0.55 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[TXNDC5]] | +0.54 | +0.33 / +0.57 | both halves | 1e-04 |  |
| [[STYX]] | +0.53 | +0.38 / +0.56 | both halves | 7e-05 |  |
| [[CMPK1]] | +0.53 | +0.37 / +0.56 | both halves | 7e-05 |  |
| [[SMU1]] | +0.53 | +0.41 / +0.51 | both halves | 4e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIM3]] | -0.62 | -0.44 / -0.65 | both halves | 3e-05 |  |
| [[PPP2R2A]] | -0.59 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[MIR210HG]] | -0.52 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[BBC3]] | -0.52 | -0.38 / -0.54 | both halves | 6e-05 |  |
| [[BIK]] | -0.52 | -0.29 / -0.49 | both halves | 3e-04 |  |
| [[RBM38]] | -0.51 | -0.37 / -0.51 | both halves | 8e-05 |  |
| [[LENG9]] | -0.51 | -0.27 / -0.56 | both halves | 3e-04 |  |
| [[SLC25A4]] | -0.50 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[RNF114]] | -0.49 | -0.32 / -0.52 | both halves | 2e-04 |  |
| [[ARRDC2]] | -0.49 | -0.34 / -0.49 | both halves | 1e-04 |  |
| [[IRF2BPL]] | -0.49 | -0.34 / -0.55 | both halves | 1e-04 |  |
| [[MAP1S]] | -0.49 | -0.27 / -0.55 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.473). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-20.9, -24.9); signed map (-20.2, -31.5). **Vector** length 105, 33.7% of its response variance represented; |z| ≥ 3 in 1,234 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.7 | +0.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.7 | +3.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +3.1 | +0.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.8 | +4.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.7 | +8.5 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +2.6 | +1.8 |
|  | [[EX229 (drug)]] 5 µM |  | +2.5 | +0.5 |
|  | [[Sapanisertib (drug)]] 5 µM |  | +2.4 | +2.2 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | +2.4 | +1.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -10.6 | -4.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -7.8 | -3.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -5.6 | -14.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.6 | -5.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~76% of this change | -5.2 | -4.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.4 | -3.2 |
|  | [[Amsacrine (drug)]] 5 µM |  | -3.4 | -3.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -3.3 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | diphosphoinositol pentakisphosphate kinase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q21.1 — chr5:103,120,149-103,212,799 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0433, VIP2, CFAP160; previously HISPPD1, DFNB100 |
| Gene groups (HGNC) | Cilia and flagella associated; Diphosphoinositol pentakisphosphate kinase family |
| Reactome | 2 pathways, smallest: Synthesis of pyrophosphates in the cytosol; Inositol phosphate metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [O43314](https://www.uniprot.org/uniprotkb/O43314) (Inositol hexakisphosphate and diphosphoinositol-pentakisphosphate kinase 2):

> Bifunctional inositol kinase that acts in concert with the IP6K kinases IP6K1, IP6K2 and IP6K3 to synthesize the diphosphate group-containing inositol pyrophosphates diphosphoinositol pentakisphosphate, PP-InsP5, and bis-diphosphoinositol tetrakisphosphate, (PP)2-InsP4. PP-InsP5 and (PP)2-InsP4, also respectively called InsP7 and InsP8, regulate a variety of cellular processes, including apoptosis, vesicle trafficking, cytoskeletal dynamics, exocytosis, insulin signaling and neutrophil …

**Summary**, from NCBI Gene [23262](https://www.ncbi.nlm.nih.gov/gene/23262):

> This gene encodes a member of the histidine acid phosphatase family of proteins. Despite containing a histidine acid phosphatase domain, the encoded protein functions as an inositol pyrophosphate kinase, and is thought to lack phosphatase activity. This kinase activity is the mechanism by which the encoded protein synthesizes high-energy inositol pyrophosphates, which act as signaling molecules that regulate cellular homeostasis and other processes. This gene may be associated with autism …

**Accessions** — [HGNC:29035](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29035) · Entrez [23262](https://www.ncbi.nlm.nih.gov/gene/23262) · UniProt [O43314](https://www.uniprot.org/uniprotkb/O43314) · Ensembl [ENSG00000145725](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145725)

## Data

Gene col 7017: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7017); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7017, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7017]; `tensor/DDL_lfc|DDL_z.npy` [7017]; `embed/gene_vectors.npy` [7017]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7017 or target_col == 7017). Every well: [[PPIP5K2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPIP5K2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
