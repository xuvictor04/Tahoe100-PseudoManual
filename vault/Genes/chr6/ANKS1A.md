---
symbol: "ANKS1A"
type: "gene"
col: 767
ensembl_id: "ENSG00000064999"
name: "ankyrin repeat and sterile alpha motif domain containing 1A"
location: "6p21.31"
module: 48
arm: "+"
pooled_cpm: 130.71
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 10
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# ANKS1A

*ankyrin repeat and sterile alpha motif domain containing 1A* — 6p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.50× (z +18.1, q 0e+00, up in 41 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.502× (z -21.6, q 0e+00, down in 45 of 49 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (NCI-H23 0.200×, SHP-77 0.172×, LoVo 0.270×, SW480 0.304×, …; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 5 lines (HS-578T 0.354×, SNU-423 0.356×, A498 0.357×, NCI-H1792 0.330×, …; ⚠ cell-cycle shift, explains ~31% of this change); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (A-427 0.0444×, RKO 0.0708×, LOX-IMVI 0.287×, NCI-H23 0.350×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TAF4]] (+0.62, fdr 3e-05), [[PIGF]] (+0.62, fdr 1e-05), [[MFN1]] (+0.61, fdr 1e-05); moves opposite to [[NBN]] (-0.59, fdr 1e-05), [[SRSF3]] (-0.58, fdr 1e-05), [[GORAB]] (-0.57, fdr 2e-05).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 767.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +18.1 | 0e+00 | 41/49 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.41×** | +10.7 | 2e-24 | 37/48 (MIA PaCa-2, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.39×** | +10.3 | 2e-22 | 36/48 (CFPAC-1, J82, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.36×** | +9.5 | 2e-19 | 35/48 (CFPAC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.29×** | +7.6 | 5e-12 | 34/48 (SNU-423, Panc 03.27, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +7.2 | 7e-11 | 19/48 (SW1417, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.21×** | +6.0 | 1e-07 | 23/48 (CFPAC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.21×** | +6.0 | 2e-07 | 23/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~3% of this change | **1.21×** | +5.9 | 2e-07 | 25/48 (J82, SNU-423, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.17× | +5.0 | 4e-05 | 20/48 (HEC-1-A, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.32×** | +4.6 | 2e-04 | 22/49 (CFPAC-1, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +4.4 | 4e-04 | 21/48 (LS 180, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 1.15× | +4.2 | 0.001 | 21/50 (SW480, Panc 03.27, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.13× | +3.7 | 0.009 | 19/48 (SW480, NCI-H460, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.12× | +3.6 | 0.014 | 11/47 (SW480, LoVo, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.11× | +3.2 | 0.047 | 5/48 (NCI-H23, RKO, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.22×** | +3.2 | 0.047 | 16/48 (LS 180, NCI-H23, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dapagliflozin (drug)]] 0.05 µM |  | 1.10× | +3.1 | 0.060 | 3/48 (HepG2/C3A, A-172, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 12 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 767.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (NCI-H23 0.200×, SHP-77 0.172×, LoVo 0.270×, SW480 0.304×, …; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 5 lines (HS-578T 0.354×, SNU-423 0.356×, A498 0.357×, NCI-H1792 0.330×, …; ⚠ cell-cycle shift, explains ~31% of this change); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (A-427 0.0444×, RKO 0.0708×, LOX-IMVI 0.287×, NCI-H23 0.350×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.502×** | -21.6 | 0e+00 | 45/49 (A-427, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.502×** | -20.7 | 0e+00 | 41/44 (NCI-H23, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.648×** | -19.2 | 0e+00 | 35/48 (HS-578T, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.594×** | -15.1 | 0e+00 | 33/45 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.735×** | -9.6 | 6e-20 | 31/48 (AN3 CA, C32, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | **0.754×** | -8.9 | 8e-17 | 34/48 (SW 1271, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.757×** | -8.4 | 4e-15 | 29/48 (A498, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.796×** | -6.9 | 4e-10 | 25/47 (CFPAC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.830×** | -5.8 | 3e-07 | 23/48 (A498, C32, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.748×** | -4.7 | 1e-04 | 24/49 (A549, SNU-423, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | 0.891× | -3.6 | 0.016 | 6/48 (SNU-423, LoVo, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.903× | -3.2 | 0.061 | 14/48 (CHP-212, A549, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.903× | -3.2 | 0.061 | 13/48 (SW480, KATO III, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | 0.904× | -3.2 | 0.061 | 5/49 (LoVo, LS 180, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 0.5 µM |  | 0.866× | -3.1 | 0.066 | 7/49 (SW480, RKO, …) | two highest doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 767. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 128 | 3 | 5 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.65× (z +12.0) | [[Homoharringtonine (drug)]] 5 µM 0.498× (z -16.9) ⚠ cell-cycle shift, explains ~31% of this change |
| [[HS-578T (line)]] | alt | 135 | 0 | 7 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -22.0) ⚠ cell-cycle shift, explains ~31% of this change |
| [[PANC-1 (line)]] | alt | 111 | 1 | 6 (6 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.66× (z +13.4) | [[Dinaciclib (drug)]] 5 µM 0.355× (z -18.8) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 144 | 1 | 5 (5 ⚠) | [[Tofacitinib (drug)]] 5 µM 1.80× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -18.9) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H460 (line)]] | wt | 91.4 | 5 (4 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.42× (z +15.7) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.52× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.568× (z -10.0) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 195 | 1 | 5 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.53× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.348× (z -17.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 140 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.362× (z -16.2) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 202 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.323× (z -17.7) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 196 | 1 | 4 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.53× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.270× (z -22.9) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 108 | 3 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +15.0) | [[Homoharringtonine (drug)]] 0.5 µM 0.421× (z -12.1) ⚠ cell-cycle shift, explains ~26% of this change |
| [[RPMI-7951 (line)]] | alt | 118 | 1 | 4 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.69× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.329× (z -13.4) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 126 | 2 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.90× (z +12.9) | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -20.7) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SW1417 (line)]] | alt | 148 | 1 | 4 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.58× (z +11.1) | [[Homoharringtonine (drug)]] 5 µM 0.480× (z -17.6) ⚠ cell-cycle shift, explains ~31% of this change |
| [[HEC-1-A (line)]] | alt | 176 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.402× (z -15.1) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 177 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.64× (z +10.0) | [[Dinaciclib (drug)]] 0.05 µM 0.369× (z -13.3) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 151 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.287× (z -19.8) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 152 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0708× (z -35.3) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 149 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 1.56× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.304× (z -22.7) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 60.3 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -20.7) ⚠ cell-cycle shift, explains ~31% of this change |
| [[hTERT-HPNE (line)]] | wt | 91.3 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -14.6) ⚠ cell-cycle shift, explains ~31% of this change |
| [[LS 180 (line)]] | wt | 181 | 1 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.78× (z +9.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.406× (z -13.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 103 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.56× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.251× (z -18.2) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 214 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.58× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.200× (z -27.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 66.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.71× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.534× (z -11.0) ⚠ cell-cycle shift, explains ~31% of this change |
| [[A-427 (line)]] | wt | 115 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0444× (z -44.6) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 111 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.84× (z +11.8) | [[Dinaciclib (drug)]] 0.5 µM 0.501× (z -9.5) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 172 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.366× (z -11.8) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 74.5 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 1.85× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.604× (z -9.8) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H1792 (line)]] | alt | 104 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -20.6) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H2030 (line)]] | alt | 126 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.321× (z -17.0) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 138 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.475× (z -11.9) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 158 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.172× (z -26.7) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 83.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.85× (z +10.3) | [[Homoharringtonine (drug)]] 5 µM 0.550× (z -9.9) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SW48 (line)]] | wt | 231 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.356× (z -11.5) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 80.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.631× (z -9.2) ⚠ cell-cycle shift, explains ~31% of this change |
| [[AN3 CA (line)]] | alt | 159 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0787× (z -19.5) ⚠ cell-cycle shift, explains ~26% of this change |
| [[BT-474 (line)]] | alt | 127 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.500× (z -13.0) ⚠ cell-cycle shift, explains ~31% of this change |
| [[C-33 A (line)]] | alt | 139 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.289× (z -14.3) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 219 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.258× (z -8.5) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 91.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.91× (z +9.6) | — |
| [[H4 (line)]] | wt | 117 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.376× (z -9.9) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 133 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.83× (z +11.1) | — |
| [[Hs 766T (line)]] | wt | 76.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.79× (z +9.1) | — |
| [[SNU-1 (line)]] | wt | 103 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -11.3) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SW 1271 (line)]] | alt | 144 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0848× (z -13.6) ⚠ transcription drop; cell-cycle shift, explains ~30% of this change |
| [[NCI-H2122 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 187 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 85.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 767), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAF4]] | +0.62 | +0.68 / +0.44 | both halves | 3e-05 |  |
| [[PIGF]] | +0.62 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[MFN1]] | +0.61 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[TUSC2]] | +0.61 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[UBL5]] | +0.61 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[FBXW7]] | +0.60 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[SSR4]] | +0.60 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[NEDD8]] | +0.60 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[ATP5MK]] | +0.58 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[PRELID1]] | +0.57 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[HIGD2A]] | +0.57 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[ZNHIT1]] | +0.57 | +0.39 / +0.53 | both halves | 6e-05 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NBN]] | -0.59 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[SRSF3]] | -0.58 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[GORAB]] | -0.57 | -0.63 / -0.47 | both halves | 2e-05 |  |
| [[ZC3H7A]] | -0.57 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[ZSCAN12]] | -0.57 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[SUGT1P3]] | -0.56 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[ZNF510]] | -0.55 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[ZNF678]] | -0.55 | -0.60 / -0.41 | both halves | 4e-05 |  |
| [[ZNF260]] | -0.55 | -0.45 / -0.60 | both halves | 3e-05 |  |
| [[DCLRE1A]] | -0.54 | -0.61 / -0.41 | both halves | 4e-05 |  |
| [[ZNF414]] | -0.54 | -0.64 / -0.36 | both halves | 1e-04 |  |
| [[GDAP1]] | -0.54 | -0.54 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers ANKS1A's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.501). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-27.8, 11.1); signed map (-47.8, -3.7). **Vector** length 112, 31.4% of its response variance represented; |z| ≥ 3 in 1,148 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.5 | +18.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | +6.9 | +7.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | +6.1 | +4.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +5.9 | +3.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +5.0 | +6.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +7.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.8 | +1.4 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +1.7 | +1.3 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +1.7 | +1.7 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.7 | -0.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -11.7 | -19.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -8.7 | -8.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -8.6 | -9.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | -4.6 | -5.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.1 | -15.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.6 | -1.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.1 | -3.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.2 | +1.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.2 | -2.0 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.1 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat and sterile alpha motif domain containing 1A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.31 — chr6:34,889,255-35,091,406 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0229; previously ANKS1 |
| Gene groups (HGNC) | Ankyrin repeat domain containing; Sterile alpha motif domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92625](https://www.uniprot.org/uniprotkb/Q92625) (Ankyrin repeat and SAM domain-containing protein 1A):

> Regulator of different signaling pathways. Regulates EPHA8 receptor tyrosine kinase signaling to control cell migration and neurite retraction (By similarity).

**Summary**, from NCBI Gene [23294](https://www.ncbi.nlm.nih.gov/gene/23294):

> Predicted to enable ephrin receptor binding activity. Predicted to be involved in ephrin receptor signaling pathway; neuron remodeling; and substrate-dependent cell migration. Predicted to be located in neuron projection. Predicted to be active in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20961](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20961) · Entrez [23294](https://www.ncbi.nlm.nih.gov/gene/23294) · UniProt [Q92625](https://www.uniprot.org/uniprotkb/Q92625) · Ensembl [ENSG00000064999](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000064999)

## Data

Gene col 767: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 767); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 767, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 767]; `tensor/DDL_lfc|DDL_z.npy` [767]; `embed/gene_vectors.npy` [767]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 767 or target_col == 767). Every well: [[ANKS1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKS1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
