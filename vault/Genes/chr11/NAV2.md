---
symbol: "NAV2"
type: "gene"
col: 9367
ensembl_id: "ENSG00000166833"
name: "neuron navigator 2"
location: "11p15.1"
module: 84
arm: "+"
pooled_cpm: 422.57
n_lines_expressing: 33
n_dd_up: 17
n_dd_down: 48
n_dd_up_clean: 11
n_dd_down_clean: 32
in_vector_space: true
direction_upstream: 9
direction_downstream: 18
tags: ["gene", "module/084"]
generated_by: "tahoemap"
---

# NAV2

*neuron navigator 2* — 11p15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.61× (z +11.4, q 2e-27, up in 22 of 31 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 2.26× (z +7.2, q 2e-10, up in 21 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 48 drug-doses (16 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.250× (z -22.4, q 0e+00, down in 30 of 30 measured lines) ⚠ toxic. The strongest without an alert is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 0.337× (z -18.3, q 0e+00, down in 30 of 31 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RUNX1]] (+0.51, fdr 3e-05), [[SAPCD2]] (+0.51, fdr 9e-05), [[RASA3]] (+0.50, fdr 3e-05); moves opposite to [[ERGIC3]] (-0.48, fdr 5e-05), [[PTS]] (-0.44, fdr 1e-04), [[RNASEL]] (-0.43, fdr 1e-04).
> It is in [[Module 084]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[GALNT18]] → it (grade B ⚠); 18 go from it, the strongest it → [[ZNF697]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9367.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.61×** | +11.4 | 2e-27 | 22/31 (COLO 205, CFPAC-1, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.26×** | +7.2 | 2e-10 | 21/32 (HS-578T, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.45×** | +6.3 | 7e-08 | 25/31 (PANC-1, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.42×** | +5.9 | 4e-07 | 18/31 (A-172, hTERT-HPNE, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 5 µM |  | **1.77×** | +5.0 | 5e-05 | 21/32 (PANC-1, HS-578T, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | **1.76×** | +5.0 | 6e-05 | 23/31 (SW480, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.05 µM |  | **1.34×** | +4.1 | 0.003 | 19/31 (HS-578T, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Temsirolimus (drug)]] 5 µM |  | 1.18× | +4.1 | 0.003 | 14/32 (HS-578T, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.27×** | +4.0 | 0.004 | 19/30 (PANC-1, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.27×** | +3.9 | 0.006 | 18/30 (PANC-1, hTERT-HPNE, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **1.25×** | +3.8 | 0.009 | 15/31 (HS-578T, C32, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.17× | +3.7 | 0.009 | 14/31 (HS-578T, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Larotrectinib sulfate (drug)]] 5 µM | ⚠ unreliable plate only | **1.24×** | +3.6 | 0.012 | 17/31 (HS-578T, C32, …) | rises with dose |  |
| [[4EGI-1 (drug)]] 0.5 µM |  | **1.35×** | +3.5 | 0.020 | 20/31 (HS-578T, PANC-1, …) | two highest doses | cell-cycle shift (explains ~15% here); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.15× | +3.5 | 0.020 | 15/32 (PANC-1, A549, …) | top dose only |  |
| [[Posaconazole (drug)]] 5 µM |  | **1.23×** | +3.3 | 0.029 | 11/31 (C32, RKO, …) | top dose only | plate-row cell shift |
| [[Verteporfin (drug)]] 5 µM |  | **1.22×** | +3.3 | 0.034 | 9/32 (AN3 CA, A498, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.44×** | +3.2 | 0.038 | 14/31 (HOP62, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[AZD-8055 (drug)]] 0.5 µM |  | **1.30×** | +3.1 | 0.056 | 14/31 (HS-578T, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | 1.19× | +2.9 | 0.091 | 10/31 (RPMI-7951, C32, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 59 in all, 21 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 48 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9367.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.250×** | -22.4 | 0e+00 | 30/30 (NCI-H1792, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.312×** | -18.8 | 0e+00 | 25/27 (J82, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.337×** | -18.3 | 0e+00 | 30/31 (C32, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.507×** | -16.1 | 0e+00 | 26/32 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.423×** | -14.4 | 4e-45 | 28/32 (NCI-H1792, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.592×** | -12.4 | 2e-33 | 28/31 (SK-MEL-2, C32, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.543×** | -9.5 | 2e-19 | 23/28 (J82, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.576×** | -9.3 | 1e-18 | 25/31 (HOP62, C32, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.703×** | -8.3 | 5e-15 | 24/31 (HOP62, A549, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.633×** | -7.4 | 9e-12 | 27/31 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.669×** | -6.7 | 8e-10 | 18/31 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.648×** | -6.7 | 8e-10 | 25/30 (C32, SW1417, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.724×** | -6.5 | 3e-09 | 25/31 (SW480, SHP-77, …) | all doses, flat | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.688×** | -6.3 | 2e-08 | 21/31 (SK-MEL-2, C32, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.695×** | -6.1 | 4e-08 | 22/31 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.690×** | -6.0 | 8e-08 | 21/31 (SW480, SHP-77, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.707×** | -5.8 | 2e-07 | 17/32 (SW480, SHP-77, …) | all doses, stronger at high dose |  |
| [[Amsacrine (drug)]] 5 µM |  | **0.792×** | -5.5 | 1e-06 | 20/31 (A549, NCI-H1792, …) | top dose only |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.743×** | -5.4 | 2e-06 | 21/32 (SW480, A498, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.726×** | -5.2 | 6e-06 | 20/30 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.704×** | -4.9 | 2e-05 | 20/31 (HOP62, C32, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.751×** | -4.8 | 4e-05 | 23/32 (PANC-1, HOP62, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.59 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9367. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 1,196 | 0 | 30 (15 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.236× (z -21.4) |
| [[SHP-77 (line)]] | alt | 353 | 0 | 14 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -24.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.300× (z -16.1) |
| [[C32 (line)]] | wt | 950 | 0 | 13 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.183× (z -18.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.192× (z -17.6) |
| [[A-172 (line)]] | wt | 735 | 2 (2 ⚠) | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +15.1) ⚠ cell-cycle shift, explains ~31% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.117× (z -21.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.342× (z -10.8) |
| [[A549 (line)]] | wt | 571 | 0 | 9 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.317× (z -16.2) |
| [[HOP62 (line)]] | alt | 586 | 2 (1 ⚠) | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +15.5) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 7.06× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.190× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.389× (z -12.7) |
| [[SNU-423 (line)]] | alt | 1,049 | 2 (1 ⚠) | 7 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +16.9) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.83× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.181× (z -17.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -15.1) |
| [[A498 (line)]] | wt | 777 | 2 (2 ⚠) | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +11.5) ⚠ cell-cycle shift, explains ~31% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.198× (z -16.8) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.235× (z -15.6) |
| [[HS-578T (line)]] | alt | 654 | 3 (2 ⚠) | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +16.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 7.84× (z +11.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.192× (z -16.5) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.339× (z -11.3) |
| [[J82 (line)]] | alt | 766 | 1 (1 ⚠) | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +12.7) ⚠ cell-cycle shift, explains ~31% of this change | [[Dinaciclib (drug)]] 5 µM 0.171× (z -19.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.427× (z -13.9) |
| [[PANC-1 (line)]] | alt | 521 | 0 | 8 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.306× (z -18.6) |
| [[SK-MEL-2 (line)]] | alt | 676 | 0 | 8 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.273× (z -17.5) |
| [[hTERT-HPNE (line)]] | wt | 517 | 3 (3 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.13× (z +19.4) ⚠ cell-cycle shift, explains ~31% of this change | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.212× (z -12.9) |
| [[NCI-H1792 (line)]] | alt | 895 | 0 | 7 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0968× (z -22.9) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.283× (z -18.2) |
| [[Panc 03.27 (line)]] | alt | 682 | 1 (1 ⚠) | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +13.7) ⚠ cell-cycle shift, explains ~31% of this change | [[Dinaciclib (drug)]] 5 µM 0.208× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.321× (z -10.9) |
| [[RKO (line)]] | wt | 914 | 0 | 7 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.165× (z -17.3) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -14.5) |
| [[RPMI-7951 (line)]] | alt | 555 | 1 | 5 (3 ⚠) | [[Triamcinolone (drug)]] 0.5 µM 2.57× (z +8.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.155× (z -16.4) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.230× (z -13.5) |
| [[Hs 766T (line)]] | wt | 624 | 1 (1 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +8.6) ⚠ cell-cycle shift, explains ~31% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.177× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[MIA PaCa-2 (line)]] | alt | 364 | 1 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +11.5) ⚠ cell-cycle shift, explains ~31% of this change | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.176× (z -13.9) |
| [[NCI-H2347 (line)]] | alt | 713 | 0 | 5 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.304× (z -11.8) ⚠ toxic · without an alert: [[Selinexor (drug)]] 5 µM 0.453× (z -11.5) |
| [[CFPAC-1 (line)]] | alt | 228 | 2 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.84× (z +20.1) ⚠ cell-cycle shift, explains ~31% of this change | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.420× (z -9.1) |
| [[COLO 205 (line)]] | alt | 113 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.10× (z +23.5) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[SW 900 (line)]] | alt | 276 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.236× (z -13.5) |
| [[SW48 (line)]] | wt | 257 | 1 | 2 (1 ⚠) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 3.89× (z +9.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.250× (z -9.4) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.419× (z -8.6) |
| [[SNU-1 (line)]] | wt | 222 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -9.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.221× (z -8.8) |
| [[H4 (line)]] | wt | 385 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.298× (z -9.6) |
| [[SW1417 (line)]] | alt | 283 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.48× (z +8.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A-427 (line)]] | wt | 30.1 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 161 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 77.2 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 67.7 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 37.6 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 176 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 77.6 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 71.9 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 95.4 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 40.0 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 53.7 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 48.1 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 40.8 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 55.4 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 62.6 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 69.4 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 285 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 68.7 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 81.6 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 365 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 42.9 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 320 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 523 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9367), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RUNX1]] | +0.51 | +0.46 / +0.52 | both halves | 3e-05 |  |
| [[SAPCD2]] | +0.51 | +0.36 / +0.45 | both halves | 9e-05 |  |
| [[RASA3]] | +0.50 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[N4BP3]] | +0.50 | +0.52 / +0.34 | both halves | 1e-04 |  |
| [[PALM2AKAP2]] | +0.48 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[SLCO4A1]] | +0.48 | +0.45 / +0.39 | both halves | 5e-05 |  |
| [[FOSL1]] | +0.47 | +0.56 / +0.35 | both halves | 1e-04 |  |
| [[HMGA1]] | +0.47 | +0.43 / +0.45 | both halves | 3e-05 | same gene group |
| [[SLC43A3]] | +0.47 | +0.51 / +0.46 | both halves | 3e-05 |  |
| [[TFB1M]] | +0.47 | +0.47 / +0.29 | both halves | 2e-04 |  |
| [[GALNT18]] | +0.46 | +0.47 / +0.33 | both halves | 1e-04 |  |
| [[CDKN3]] | +0.46 | +0.36 / +0.39 | both halves | 9e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERGIC3]] | -0.48 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[PTS]] | -0.44 | -0.39 / -0.35 | both halves | 1e-04 |  |
| [[RNASEL]] | -0.43 | -0.34 / -0.38 | both halves | 1e-04 |  |
| [[PLAAT4]] | -0.42 | -0.41 / -0.26 | both halves | 4e-04 |  |
| [[ZNF148]] | -0.41 | -0.45 / -0.23 | both halves | 5e-04 |  |
| [[STRN3]] | -0.41 | -0.38 / -0.25 | both halves | 4e-04 | same gene group |
| [[PRKACB]] | -0.40 | -0.40 / -0.32 | both halves | 2e-04 |  |
| [[HFE]] | -0.40 | -0.39 / -0.20 | both halves | 7e-04 |  |
| [[IPP]] | -0.39 | -0.32 / -0.33 | both halves | 1e-04 |  |
| [[TIAL1]] | -0.39 | -0.37 / -0.19 | ⚠ not reproduced | 8e-04 |  |
| [[BEX3]] | -0.38 | -0.25 / -0.33 | both halves | 4e-04 |  |
| [[TNFSF13B]] | -0.38 | -0.37 / -0.21 | both halves | 6e-04 |  |
| [[TMED1]] | -0.38 | -0.37 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 7, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GALNT18]] | B | GALNT18 activity raises NAV2's level | lines that do not express GALNT18 (10) vs lines expressing it (40) | 3.63× lower at baseline in the lines without GALNT18 | 0.014 | ⚠ within organs, on part of the lines; also absent: SERTAD4, ULK2, WNT9A |
| [[TOP2A]] | B | TOP2A activity raises NAV2's level | compounds that target TOP2A: 5 of 5 lower it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 8.4% of all compounds | 0.015 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[G0S2]] | B | G0S2 activity raises NAV2's level | lines that do not express G0S2 (33) vs lines expressing it (17) | 3.14× lower at baseline in the lines without G0S2 | 0.024 | ⚠ within organs, on part of the lines; also absent: IL6, EDNRA, RRAD |
| [[MAP2K1]] | B | MAP2K1 activity raises NAV2's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 8.4% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds |
| [[ICAM1]] | B | ICAM1 activity raises NAV2's level | lines that do not express ICAM1 (19) vs lines expressing it (31) | 2.65× lower at baseline in the lines without ICAM1 | 0.048 | ⚠ within organs, on part of the lines; also absent: ITGB3, ZNF43, ENSG00000259753 |
| [[RASA3]] | B | RASA3 activity raises NAV2's level | lines that do not express RASA3 (9) vs lines expressing it (41) | 3.81× lower at baseline in the lines without RASA3 | 0.074 | ⚠ within organs, on part of the lines; also absent: C13orf46, PRR5L, LINC02100; maybe low, not absent |
| [[MTSS1]] | B | MTSS1 activity raises NAV2's level | lines that do not express MTSS1 (20) vs lines expressing it (30) | 2.18× lower at baseline in the lines without MTSS1 | 0.084 | ⚠ within organs, on part of the lines; also absent: RASD1, GATA3, TREM1 |
| [[SERPINE1]] | C | SERPINE1 activity raises NAV2's level | lines that do not express SERPINE1 (27) vs lines expressing it (23) | 4.05× lower at baseline in the lines without SERPINE1 | 0.006 | ⚠ within organs, on part of the lines; also absent: FRMD4A, SIRLNT, ENSG00000230615; co-absent with the target |
| [[SLC43A3]] | C | SLC43A3 activity raises NAV2's level | lines that do not express SLC43A3 (28) vs lines expressing it (22) | 3.14× lower at baseline in the lines without SLC43A3 | 0.025 | ⚠ within organs, on part of the lines; also absent: ENSG00000254979, FN1, ENSG00000234261; co-absent with the target |

### Downstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 16, C 2. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF697]] | B | NAV2 activity raises ZNF697's level | lines that do not express NAV2 (17) vs lines expressing it (33) | 2.14× lower at baseline in the lines without NAV2 | 0.002 | ⚠ within organs, on part of the lines; also absent: NAV1, ROR1-AS1, CSF1 |
| [[HIVEP3]] | B | NAV2 activity raises HIVEP3's level | lines that do not express NAV2 (17) vs lines expressing it (33) | 2.61× lower at baseline in the lines without NAV2 | 0.003 | ⚠ within organs, on part of the lines; also absent: NAV1, ROR1-AS1, CSF1 |
| [[HPS3]] | B | NAV2 activity raises HPS3's level | lines that do not express NAV2 (17) vs lines expressing it (33) | 1.91× lower at baseline in the lines without NAV2 | 0.011 | ⚠ within organs, on part of the lines; also absent: NAV1, ROR1-AS1, CSF1 |
| [[SUN2]] | B | NAV2 activity raises SUN2's level | lines that do not express NAV2 (17) vs lines expressing it (33) | 1.53× lower at baseline in the lines without NAV2 | 0.011 | ⚠ within organs, on part of the lines; also absent: NAV1, ROR1-AS1, CSF1 |
| [[GALNT18]] | B | NAV2 activity raises GALNT18's level | lines that do not express NAV2 (17) vs lines expressing it (33) | 2.70× lower at baseline in the lines without NAV2 | 0.017 | ⚠ within organs, on part of the lines; also absent: NAV1, ROR1-AS1, CSF1 |
| [[SSH1]] | B | NAV2 activity raises SSH1's level | lines that do not express NAV2 (17) vs lines expressing it (33) | 1.90× lower at baseline in the lines without NAV2 | 0.022 | ⚠ within organs, on part of the lines; also absent: NAV1, ROR1-AS1, CSF1 |
| [[G0S2]] | B | NAV2 activity raises G0S2's level | lines that do not express NAV2 (17) vs lines expressing it (33) | 3.91× lower at baseline in the lines without NAV2 | 0.027 | ⚠ within organs, on part of the lines; also absent: NAV1, ROR1-AS1, CSF1 |
| [[GOLGA7B]] | B | NAV2 activity raises GOLGA7B's level | lines that do not express NAV2 (17) vs lines expressing it (33) | 2.12× lower at baseline in the lines without NAV2 | 0.030 | ⚠ within organs, on part of the lines; also absent: NAV1, ROR1-AS1, CSF1 |
| [[RHBDF2]] | B | NAV2 activity strengthens RHBDF2's drug response | lines that do not express NAV2 (16) vs lines expressing it (27) | the lines without NAV2 respond 0.53× as strongly (z diff +3.22); strongest at Idarubicin (hydrochloride) 5 µM: 0.81x vs 0.40x (z diff +5.3) | 0.033 | ⚠ within organs, on part of the lines; also absent: NAV1, ROR1-AS1, CSF1; target measured in part of the lines; artifact flags |
| [[AFAP1]] | B | NAV2 activity raises AFAP1's level | lines that do not express NAV2 (17) vs lines expressing it (33) | 2.18× lower at baseline in the lines without NAV2 | 0.038 | ⚠ within organs, on part of the lines; also absent: NAV1, ROR1-AS1, CSF1 |
| [[MTSS1]] | B | NAV2 activity raises MTSS1's level | lines that do not express NAV2 (17) vs lines expressing it (33) | 2.36× lower at baseline in the lines without NAV2 | 0.039 | ⚠ within organs, on part of the lines; also absent: NAV1, ROR1-AS1, CSF1 |
| [[SDK1]] | B | NAV2 activity raises SDK1's level | lines that do not express NAV2 (17) vs lines expressing it (33) | 3.20× lower at baseline in the lines without NAV2 | 0.043 | ⚠ within organs, on part of the lines; also absent: NAV1, ROR1-AS1, CSF1 |

## Where it sits

- **Module**: [[Module 084]]; 52 genes; every member is in the + arm (projection on the module's main direction 0.436). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-35.0, -60.7); signed map (1.1, 51.7). **Vector** length 128, 40.4% of its response variance represented; |z| ≥ 3 in 1,417 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +8.0 | +11.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +5.3 | +5.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.2 | -1.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.0 | -0.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.3 | +1.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.1 | +3.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.7 | +3.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.3 | +1.0 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.2 | +1.5 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +2.2 | +5.0 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -6.6 | -18.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.5 | -22.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -5.1 | -9.3 |
|  | [[Selinexor (drug)]] 5 µM |  | -4.6 | -12.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.9 | -6.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.7 | -4.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.6 | -6.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.5 | -5.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.4 | -5.8 |

## What is on record

|  |  |
|---|---|
| Name | neuron navigator 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.1 — chr11:19,350,724-20,121,601 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10633, FLJ11030, HELAD1, KIAA1419, POMFIL2, RAINB1, FLJ23707 |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Hallmark sets | MYOGENESIS, ESTROGEN_RESPONSE_EARLY |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IVL1](https://www.uniprot.org/uniprotkb/Q8IVL1) (Neuron navigator 2):

> Possesses 3' to 5' helicase activity and exonuclease activity. Involved in cytoskeleton organization. Required for neurite outgrowth in response to stimulation by all-trans retinoic acid (atRA). Involved in neuronal development, specifically in the development of different sensory organs. Important for brain and cerebellar development. Involved in the differentiation, migration and axonal extension of granule cells in the developing cerebellum (By similarity). Involved in the development of the …

**Summary**, from NCBI Gene [89797](https://www.ncbi.nlm.nih.gov/gene/89797):

> This gene encodes a member of the neuron navigator gene family, which may play a role in cellular growth and migration. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Oct 2011]

**Accessions** — [HGNC:15997](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15997) · Entrez [89797](https://www.ncbi.nlm.nih.gov/gene/89797) · UniProt [Q8IVL1](https://www.uniprot.org/uniprotkb/Q8IVL1) · Ensembl [ENSG00000166833](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166833)

## Data

Gene col 9367: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9367); `tables/drug_effects.parquet` (82 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9367, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9367]; `tensor/DDL_lfc|DDL_z.npy` [9367]; `embed/gene_vectors.npy` [9367]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9367 or target_col == 9367). Every well: [[NAV2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NAV2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
