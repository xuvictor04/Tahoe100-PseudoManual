---
symbol: "AMD1"
type: "gene"
col: 4440
ensembl_id: "ENSG00000123505"
name: "adenosylmethionine decarboxylase 1"
location: "6q21"
module: 77
arm: "+"
pooled_cpm: 100.69
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 3
n_dd_up_clean: 9
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/077"]
generated_by: "tahoemap"
---

# AMD1

*adenosylmethionine decarboxylase 1* — 6q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (17 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 3.47× (z +14.3, q 1e-43, up in 48 of 48 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.91× (z +10.5, q 2e-23, up in 44 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.640× (z -3.8, q 0.091, down in 25 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 0.5 µM: 0.735× (z -3.6, q 0.091, down in 30 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (A-172 0.236×, SW 1271 0.114×, SW1417 0.386×, HepG2/C3A 0.387×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (A-427 0.0938×, SW 900 0.127×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-172 0.325×; ⚠ cell-cycle shift, explains ~76% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-172 0.244×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM41A]] (+0.61, fdr 3e-05), [[SLC16A1]] (+0.61, fdr 1e-05), [[MED26]] (+0.58, fdr 6e-05); moves opposite to [[NDUFS1]] (-0.62, fdr 4e-05), [[ZNF655]] (-0.59, fdr 4e-05), [[OCIAD1]] (-0.59, fdr 2e-05).
> It sits in the **+** arm of [[Module 077]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 18 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4440.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **3.47×** | +14.3 | 1e-43 | 48/48 (LS 180, KATO III, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **3.05×** | +12.8 | 4e-35 | 48/48 (LS 180, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.91×** | +10.5 | 2e-23 | 44/49 (AsPC-1, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **2.36×** | +9.8 | 1e-20 | 45/48 (SW480, HS-578T, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **2.31×** | +9.6 | 9e-20 | 46/48 (SW480, hTERT-HPNE, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **2.16×** | +8.8 | 8e-17 | 46/48 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.09×** | +8.5 | 2e-15 | 45/48 (SW480, KATO III, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.90×** | +7.4 | 1e-11 | 44/48 (SW480, LS 180, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.20× | +6.9 | 3e-10 | 20/50 (LoVo, KATO III, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **1.45×** | +6.0 | 8e-08 | 34/48 (A498, AsPC-1, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.63×** | +5.6 | 1e-06 | 35/48 (SNU-423, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | **1.84×** | +5.1 | 2e-05 | 36/47 (NCI-H1792, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.33×** | +5.1 | 2e-05 | 37/48 (Panc 03.27, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.56×** | +5.1 | 2e-05 | 33/48 (H4, NCI-H460, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.50×** | +4.6 | 1e-04 | 33/48 (Hs 766T, NCI-H1792, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.44×** | +4.2 | 8e-04 | 30/48 (PANC-1, NCI-H23, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.39×** | +3.7 | 0.005 | 28/48 (COLO 205, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +3.2 | 0.031 | 23/48 (HepG2/C3A, NCI-H2347, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.71×** | +3.2 | 0.031 | 26/48 (NCI-H460, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.46×** | +3.1 | 0.045 | 21/49 (SNU-423, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | **1.21×** | +3.0 | 0.048 | 19/49 (CFPAC-1, Panc 03.27, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4440.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (A-172 0.236×, SW 1271 0.114×, SW1417 0.386×, HepG2/C3A 0.387×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (A-427 0.0938×, SW 900 0.127×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-172 0.325×; ⚠ cell-cycle shift, explains ~76% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-172 0.244×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.640×** | -3.8 | 0.091 | 25/44 (A-427, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.735×** | -3.6 | 0.091 | 30/48 (KATO III, CFPAC-1, …) | two highest doses | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.740×** | -3.5 | 0.091 | 25/49 (A-172, SW 1271, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.756× | -3.2 | 0.17 | 24/47 (HepG2/C3A, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.54 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4440. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 94.1 | 8 (8 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 6.64× (z +16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[SW480 (line)]] | alt | 109 | 8 (7 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.45× (z +15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.41× (z +8.9) | — |
| [[HS-578T (line)]] | alt | 66.4 | 7 (6 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.67× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +9.0) | — |
| [[LoVo (line)]] | wt | 158 | 7 (7 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.90× (z +14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[AsPC-1 (line)]] | alt | 89.8 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.51× (z +16.4) ⚠ cell-cycle shift, explains ~76% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.19× (z +12.6) | — |
| [[H4 (line)]] | wt | 47.8 | 6 (5 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 9.77× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.39× (z +9.2) | — |
| [[LS 180 (line)]] | wt | 116 | 5 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.09× (z +18.6) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[PANC-1 (line)]] | alt | 140 | 5 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.52× (z +17.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +10.3) | — |
| [[A-172 (line)]] | wt | 119 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -11.7) ⚠ cell-cycle shift, explains ~76% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.244× (z -10.4) |
| [[BT-474 (line)]] | alt | 122 | 4 (4 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.08× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[COLO 205 (line)]] | alt | 42.0 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.29× (z +15.6) ⚠ cell-cycle shift, explains ~76% of this change | — |
| [[Hs 766T (line)]] | wt | 51.4 | 4 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.57× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +9.2) | — |
| [[hTERT-HPNE (line)]] | wt | 91.6 | 4 (4 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 3.45× (z +9.6) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[SNU-423 (line)]] | alt | 120 | 4 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.45× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +8.6) | — |
| [[SW 900 (line)]] | alt | 92.0 | 3 (2 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 4.84× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.127× (z -9.7) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 109 | 2 (2 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.87× (z +9.1) ⚠ cell-cycle shift, explains ~45% of this change | [[Dinaciclib (drug)]] 5 µM 0.0938× (z -15.1) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 57.5 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.07× (z +11.8) | — |
| [[HT-29 (line)]] | alt | 108 | 3 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.68× (z +14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +8.7) | — |
| [[J82 (line)]] | alt | 91.7 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.99× (z +11.3) | — |
| [[NCI-H1573 (line)]] | alt | 42.6 | 3 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.66× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H1792 (line)]] | alt | 66.9 | 3 (3 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 3.94× (z +9.1) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[NCI-H23 (line)]] | alt | 71.1 | 3 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.30× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H460 (line)]] | wt | 65.3 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.09× (z +11.3) | — |
| [[Panc 03.27 (line)]] | alt | 95.8 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +10.2) ⚠ cell-cycle shift, explains ~76% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.40× (z +10.0) | — |
| [[RPMI-7951 (line)]] | alt | 61.1 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.10× (z +10.6) | — |
| [[SW1417 (line)]] | alt | 92.9 | 2 (2 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 3.37× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.386× (z -8.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 59.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.68× (z +17.1) ⚠ cell-cycle shift, explains ~76% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +9.6) | — |
| [[CFPAC-1 (line)]] | alt | 72.8 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.85× (z +10.0) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[HepG2_C3A (line)]] | wt | 222 | 1 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.57× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.387× (z -8.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 141 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.55× (z +8.6) | — |
| [[SHP-77 (line)]] | alt | 107 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.48× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[A549 (line)]] | wt | 59.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.98× (z +9.9) | — |
| [[RKO (line)]] | wt | 136 | 1 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.79× (z +9.5) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 115 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.57× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[SNU-1 (line)]] | wt | 94.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +9.7) | — |
| [[SW 1271 (line)]] | alt | 128 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.114× (z -10.3) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 121 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 6.56× (z +13.4) | — |
| [[AN3 CA (line)]] | alt | 147 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 125 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 207 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 128 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 91.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 108 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 114 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 97.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 96.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 159 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 80.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4440), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*51 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM41A]] | +0.61 | +0.43 / +0.61 | both halves | 3e-05 |  |
| [[SLC16A1]] | +0.61 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[MED26]] | +0.58 | +0.39 / +0.62 | both halves | 6e-05 |  |
| [[SMG1P2]] | +0.58 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[SH2B2]] | +0.57 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[NR2F6]] | +0.56 | +0.40 / +0.55 | both halves | 5e-05 |  |
| [[BZW2]] | +0.56 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[EIF4A3]] | +0.56 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[PHAF1]] | +0.55 | +0.35 / +0.53 | both halves | 1e-04 |  |
| [[JPT1]] | +0.54 | +0.36 / +0.59 | both halves | 1e-04 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[TSEN54]] | +0.54 | +0.37 / +0.55 | both halves | 8e-05 |  |
| [[AFMID]] | +0.54 | +0.37 / +0.55 | both halves | 8e-05 | pathway: Metabolism of amino acids and derivatives |

## Genes that move opposite

*49 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFS1]] | -0.62 | -0.41 / -0.64 | both halves | 4e-05 |  |
| [[ZNF655]] | -0.59 | -0.42 / -0.61 | both halves | 4e-05 |  |
| [[OCIAD1]] | -0.59 | -0.48 / -0.60 | both halves | 2e-05 |  |
| [[C11orf58]] | -0.56 | -0.46 / -0.63 | both halves | 3e-05 |  |
| [[SLC25A46]] | -0.56 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[HDHD2]] | -0.55 | -0.32 / -0.52 | both halves | 2e-04 |  |
| [[CHURC1]] | -0.55 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[GDAP1]] | -0.54 | -0.49 / -0.37 | both halves | 8e-05 |  |
| [[PSME3IP1]] | -0.54 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[ZNF554]] | -0.54 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[CCDC50]] | -0.53 | -0.33 / -0.53 | both halves | 1e-04 |  |
| [[ZSCAN30]] | -0.53 | -0.48 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 077]]; 59 genes; this gene is in the **+** arm (projection on the module's main direction 0.568). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.44).
- **Nodal map** (x, y) = (-15.0, 6.0); signed map (-46.4, 25.2). **Vector** length 97.0, 35.1% of its response variance represented; |z| ≥ 3 in 1,239 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.6 | +10.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +3.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | +3.8 | +3.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | +1.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | +2.6 | +4.6 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +2.1 | +3.0 |
|  | [[Arbutin (drug)]] 5 µM |  | +2.0 | +1.8 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +1.9 | +1.9 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +1.8 | +2.3 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | -8.1 | +3.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.6 | +3.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -6.1 | +0.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | -5.1 | +6.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.5 | -2.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.1 | -1.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.6 | -2.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.5 | +4.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.1 | -1.9 |
|  | [[Phenylephrine (hydrochloride) (drug)]] 0.5 µM |  | -2.1 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | adenosylmethionine decarboxylase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q21 — chr6:110,874,770-110,898,879 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SAMDC |
| Gene groups (HGNC) | Decarboxylases |
| Hallmark sets | UV_RESPONSE_UP, G2M_CHECKPOINT |
| Reactome | 2 pathways, smallest: Metabolism of polyamines; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [P17707](https://www.uniprot.org/uniprotkb/P17707) (S-adenosylmethionine decarboxylase proenzyme):

> Essential for biosynthesis of the polyamines spermidine and spermine. Promotes maintenance and self-renewal of embryonic stem cells, by maintaining spermine levels.

**Summary**, from NCBI Gene [262](https://www.ncbi.nlm.nih.gov/gene/262):

> This gene encodes an important intermediate enzyme in polyamine biosynthesis. The polyamines spermine, spermidine, and putrescine are low-molecular-weight aliphatic amines essential for cellular proliferation and tumor promotion. Multiple alternatively spliced transcript variants have been identified. Pseudogenes of this gene are found on chromosomes 5, 6, 10, X and Y. [provided by RefSeq, Dec 2013]

**Accessions** — [HGNC:457](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:457) · Entrez [262](https://www.ncbi.nlm.nih.gov/gene/262) · UniProt [P17707](https://www.uniprot.org/uniprotkb/P17707) · Ensembl [ENSG00000123505](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123505)

## Data

Gene col 4440: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4440); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4440, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4440]; `tensor/DDL_lfc|DDL_z.npy` [4440]; `embed/gene_vectors.npy` [4440]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4440 or target_col == 4440). Every well: [[AMD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AMD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
