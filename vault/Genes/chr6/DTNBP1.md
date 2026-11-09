---
symbol: "DTNBP1"
type: "gene"
col: 518
ensembl_id: "ENSG00000047579"
name: "dystrobrevin binding protein 1"
location: "6p22.3"
module: 36
arm: "+"
pooled_cpm: 45.5
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 22
n_dd_up_clean: 8
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# DTNBP1

*dystrobrevin binding protein 1* — 6p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.05 µM: 1.35× (z +5.0, q 3e-04, up in 26 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.553× (z -15.6, q 0e+00, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DTNB]] (+0.65, fdr 7e-06), [[EXOC2]] (+0.62, fdr 1e-05), [[CMTM8]] (+0.61, fdr 1e-05); moves opposite to [[C12orf60]] (-0.55, fdr 2e-04), [[LRP2BP]] (-0.55, fdr 1e-04), [[KLHL3]] (-0.54, fdr 6e-05).
> It sits in the **+** arm of [[Module 036]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 518.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.05 µM |  | **1.35×** | +5.0 | 3e-04 | 26/48 (SW 900, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Rapamycin (drug)]] 5 µM |  | 1.18× | +4.4 | 0.003 | 16/48 (SNU-423, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.26×** | +4.3 | 0.003 | 21/48 (LoVo, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.24×** | +4.0 | 0.010 | 16/47 (SW480, SK-MEL-2, …) | two highest doses |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.24×** | +3.9 | 0.010 | 15/47 (NCI-H1573, NCI-H460, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **1.48×** | +3.8 | 0.012 | 18/48 (LS 180, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~5% of this change | **1.21×** | +3.5 | 0.034 | 18/47 (SW480, LoVo, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.41×** | +3.4 | 0.056 | 7/48 (LoVo, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Larotrectinib sulfate (drug)]] 5 µM | ⚠ unreliable plate only | 1.19× | +3.3 | 0.070 | 8/48 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[Hydroxyfasudil (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.19× | +3.2 | 0.072 | 9/48 (BT-474, A549, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.21×** | +3.2 | 0.074 | 8/48 (RKO, LoVo, …) | two highest doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 1.19× | +3.1 | 0.077 | 12/48 (A-172, SW480, …) | all doses, flat |  |
| [[Larotrectinib sulfate (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.18× | +3.1 | 0.078 | 10/47 (NCI-H1573, NCI-H2347, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.13× | +3.1 | 0.082 | 11/48 (SW480, NCI-H1792, …) | rises with dose |  |
| [[Rapamycin (drug)]] 0.5 µM |  | 1.18× | +3.1 | 0.084 | 15/47 (NCI-H1573, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[AZD-8055 (drug)]] 5 µM |  | **1.36×** | +3.0 | 0.096 | 5/48 (LoVo, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 518.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.553×** | -15.6 | 0e+00 | 42/48 (SNU-423, NCI-H23, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.585×** | -14.1 | 7e-43 | 34/48 (LOX-IMVI, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.536×** | -11.6 | 6e-29 | 39/47 (SW480, LS 180, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.585×** | -10.0 | 2e-21 | 35/48 (SW480, Panc 03.27, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.591×** | -9.8 | 1e-20 | 38/48 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.594×** | -9.3 | 1e-18 | 31/48 (NCI-H2030, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.430×** | -8.2 | 2e-14 | 29/49 (NCI-H23, C32, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.654×** | -7.9 | 2e-13 | 33/48 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.679×** | -7.2 | 4e-11 | 30/48 (LOX-IMVI, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.671×** | -7.1 | 5e-11 | 30/48 (SNU-423, RKO, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.657×** | -7.1 | 6e-11 | 31/48 (SW480, LoVo, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.678×** | -7.0 | 1e-10 | 26/47 (SNU-423, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.674×** | -6.8 | 4e-10 | 29/44 (C32, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | **0.699×** | -6.7 | 1e-09 | 32/47 (RKO, A-427, …) | all doses, flat | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.511×** | -6.5 | 2e-09 | 28/48 (MIA PaCa-2, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.788×** | -4.3 | 6e-04 | 23/48 (HOP62, LOX-IMVI, …) | top dose only | plate-row cell shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.828×** | -3.5 | 0.011 | 17/48 (LOX-IMVI, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.882× | -3.3 | 0.021 | 14/48 (Hs 766T, BT-474, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.834× | -3.1 | 0.039 | 18/47 (AN3 CA, MIA PaCa-2, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 0.843× | -3.1 | 0.050 | 11/48 (LoVo, NCI-H2030, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 518. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 45.7 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -18.5) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.429× (z -11.4) |
| [[Panc 03.27 (line)]] | alt | 62.6 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -13.3) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.285× (z -11.8) |
| [[SNU-423 (line)]] | alt | 89.1 | 0 | 8 (4 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.161× (z -19.4) |
| [[MIA PaCa-2 (line)]] | alt | 44.9 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.164× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.294× (z -10.9) |
| [[PANC-1 (line)]] | alt | 70.2 | 0 | 6 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.345× (z -15.7) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.574× (z -11.6) |
| [[C32 (line)]] | wt | 54.6 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0630× (z -20.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.259× (z -10.8) |
| [[COLO 205 (line)]] | alt | 81.0 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -14.9) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.391× (z -8.6) |
| [[LoVo (line)]] | wt | 34.1 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.127× (z -19.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.404× (z -8.8) |
| [[NCI-H23 (line)]] | alt | 70.3 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.207× (z -17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.452× (z -12.6) |
| [[SW1417 (line)]] | alt | 44.1 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -14.7) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.485× (z -9.5) |
| [[SW48 (line)]] | wt | 45.0 | 0 | 5 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.172× (z -9.7) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.161× (z -9.7) |
| [[SW480 (line)]] | alt | 46.2 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.266× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.373× (z -12.0) |
| [[A498 (line)]] | wt | 25.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -14.6) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.299× (z -11.1) |
| [[HT-29 (line)]] | alt | 51.1 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.454× (z -10.6) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.380× (z -9.2) |
| [[NCI-H2030 (line)]] | alt | 47.7 | 0 | 4 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.216× (z -12.9) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.429× (z -10.5) |
| [[A-427 (line)]] | wt | 52.9 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.333× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.358× (z -10.6) |
| [[KATO III (line)]] | alt | 61.7 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.279× (z -13.1) ⚠ cell-cycle shift, explains ~39% of this change |
| [[LS 180 (line)]] | wt | 48.8 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.240× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[RKO (line)]] | wt | 63.8 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.195× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.223× (z -13.1) |
| [[AsPC-1 (line)]] | alt | 16.8 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.208× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[BT-474 (line)]] | alt | 52.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -13.0) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.489× (z -8.8) |
| [[C-33 A (line)]] | alt | 48.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.197× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[HEC-1-A (line)]] | alt | 55.1 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -12.6) |
| [[HOP62 (line)]] | alt | 41.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.418× (z -10.4) |
| [[Hs 766T (line)]] | wt | 31.8 | 0 | 2 (1 ⚠) | — | [[AZD2858 (drug)]] 5 µM 0.0639× (z -11.4) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.418× (z -9.7) |
| [[NCI-H1792 (line)]] | alt | 30.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.153× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[NCI-H460 (line)]] | wt | 32.2 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.386× (z -9.3) |
| [[A-172 (line)]] | wt | 36.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -10.7) |
| [[A549 (line)]] | wt | 32.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -10.1) ⚠ cell-cycle shift, explains ~46% of this change |
| [[HepG2_C3A (line)]] | wt | 40.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.184× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[J82 (line)]] | alt | 93.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.512× (z -11.6) |
| [[NCI-H1573 (line)]] | alt | 21.6 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.222× (z -11.0) ⚠ cell-cycle shift, explains ~39% of this change |
| [[SHP-77 (line)]] | alt | 39.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.251× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[SK-MEL-2 (line)]] | alt | 51.9 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.384× (z -8.5) |
| [[SNU-1 (line)]] | wt | 56.9 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.166× (z -11.6) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SW 1271 (line)]] | alt | 73.0 | 0 | 1 | — | [[Simotinib (drug)]] 0.05 µM 0.0894× (z -9.0) |
| [[AN3 CA (line)]] | alt | 76.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 32.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 518), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DTNB]] | +0.65 | +0.59 / +0.60 | both halves | 7e-06 | STRING 919 |
| [[EXOC2]] | +0.62 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[CMTM8]] | +0.61 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[SIMC1]] | +0.58 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[CDIN1]] | +0.58 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[BLVRA]] | +0.58 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[STX8]] | +0.58 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[HERC2P9]] | +0.55 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[RABEP1]] | +0.54 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[CLASP2]] | +0.54 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[VPS8]] | +0.54 | +0.40 / +0.53 | both halves | 5e-05 |  |
| [[EXOC6B]] | +0.54 | +0.49 / +0.42 | both halves | 4e-05 | STRING 420 |

## Genes that move opposite

*38 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C12orf60]] | -0.55 | -0.30 / -0.31 | both halves | 2e-04 |  |
| [[LRP2BP]] | -0.55 | -0.34 / -0.46 | both halves | 1e-04 |  |
| [[KLHL3]] | -0.54 | -0.38 / -0.56 | both halves | 6e-05 |  |
| [[LINC01135]] | -0.53 | -0.31 / -0.47 | both halves | 2e-04 |  |
| [[PAN2]] | -0.52 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[PRKAR1A]] | -0.51 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[SRGAP3]] | -0.51 | -0.32 / -0.32 | both halves | 2e-04 |  |
| [[USP11]] | -0.51 | -0.37 / -0.37 | both halves | 7e-05 |  |
| [[CCT6B]] | -0.51 | -0.33 / -0.37 | both halves | 1e-04 |  |
| [[POLR2A]] | -0.50 | -0.54 / -0.25 | both halves | 4e-04 |  |
| [[CPEB2-DT]] | -0.50 | -0.29 / -0.38 | both halves | 3e-04 |  |
| [[MALINC1]] | -0.50 | -0.37 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.473). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-6.1, -31.9); signed map (-14.8, -53.3). **Vector** length 88.8, 22.8% of its response variance represented; |z| ≥ 3 in 1,048 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +4.4 | -0.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.1 | +0.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.8 | +0.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.5 | +2.4 |
|  | [[Rapamycin (drug)]] 5 µM |  | +3.3 | +4.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.7 | +3.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.6 | +0.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.6 | +1.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.5 | -15.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -7.1 | -7.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.5 | -7.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.1 | -10.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | -4.7 | -6.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.5 | -3.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.5 | -0.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.2 | -3.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.9 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | dystrobrevin binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p22.3 — chr6:15,522,807-15,663,058 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Dysbindin, My031, HPS7, DBND, BLOC1S8 |
| Gene groups (HGNC) | Biogenesis of lysosomal organelles complex 1 subunits |
| Reactome | 4 pathways, smallest: Golgi Associated Vesicle Biogenesis; trans-Golgi Network Vesicle Budding; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96EV8](https://www.uniprot.org/uniprotkb/Q96EV8) (Dysbindin):

> Component of the BLOC-1 complex, a complex that is required for normal biogenesis of lysosome-related organelles (LRO), such as platelet dense granules and melanosomes. In concert with the AP-3 complex, the BLOC-1 complex is required to target membrane protein cargos into vesicles assembled at cell bodies for delivery into neurites and nerve terminals. The BLOC-1 complex, in association with SNARE proteins, is also proposed to be involved in neurite extension. Associates with the BLOC-2 complex …

**Summary**, from NCBI Gene [84062](https://www.ncbi.nlm.nih.gov/gene/84062):

> This gene encodes a protein that may play a role in organelle biogenesis associated with melanosomes, platelet dense granules, and lysosomes. A similar protein in mouse is a component of a protein complex termed biogenesis of lysosome-related organelles complex 1 (BLOC-1), and binds to alpha- and beta-dystrobrevins, which are components of the dystrophin-associated protein complex (DPC). Mutations in this gene are associated with Hermansky-Pudlak syndrome type 7. This gene may also be …

**Accessions** — [HGNC:17328](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17328) · Entrez [84062](https://www.ncbi.nlm.nih.gov/gene/84062) · UniProt [Q96EV8](https://www.uniprot.org/uniprotkb/Q96EV8) · Ensembl [ENSG00000047579](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000047579)

## Data

Gene col 518: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 518); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 518, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 518]; `tensor/DDL_lfc|DDL_z.npy` [518]; `embed/gene_vectors.npy` [518]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 518 or target_col == 518). Every well: [[DTNBP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DTNBP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
