---
symbol: "TAB2"
type: "gene"
col: 624
ensembl_id: "ENSG00000055208"
name: "TGF-beta activated kinase 1 (MAP3K7) binding protein 2"
location: "6q25.1"
module: 28
arm: "+"
pooled_cpm: 151.98
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 15
n_dd_up_clean: 5
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# TAB2

*TGF-beta activated kinase 1 (MAP3K7) binding protein 2* — 6q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 7.03× (z +25.6, q 0e+00, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.622× (z -16.9, q 0e+00, down in 45 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZFHX2]] (+0.66, fdr 1e-05), [[NDUFA5]] (+0.66, fdr 7e-06), [[CFL2]] (+0.66, fdr 1e-05); moves opposite to [[MAD1L1]] (-0.65, fdr 1e-05), [[TOP3A]] (-0.62, fdr 3e-05), [[SENP5]] (-0.61, fdr 1e-04).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 624.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **7.03×** | +25.6 | 0e+00 | 48/49 (SW480, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.65×** | +17.7 | 0e+00 | 43/48 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **3.13×** | +15.0 | 0e+00 | 45/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.81×** | +14.4 | 1e-44 | 43/48 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.46×** | +9.6 | 1e-19 | 35/48 (LoVo, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.30×** | +6.7 | 2e-09 | 36/49 (NCI-H460, PANC-1, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 1.20× | +4.6 | 4e-04 | 24/48 (A-172, A498, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.16× | +3.7 | 0.018 | 14/48 (NCI-H2347, RPMI-7951, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.2 | 0.077 | 16/48 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Erlotinib (drug)]] 0.05 µM |  | 1.14× | +3.0 | 0.13 | 8/48 (HEC-1-A, AsPC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 13 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 624.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.622×** | -16.9 | 0e+00 | 45/49 (CFPAC-1, A549, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.563×** | -14.4 | 1e-44 | 45/48 (AsPC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.576×** | -13.8 | 3e-41 | 46/48 (HEC-1-A, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.632×** | -11.5 | 1e-28 | 43/48 (HOP62, AsPC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **0.696×** | -9.1 | 1e-17 | 39/49 (LoVo, HCT15, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.725×** | -7.8 | 8e-13 | 40/50 (C32, LOX-IMVI, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.728×** | -7.6 | 2e-12 | 36/48 (A-172, C32, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | **0.734×** | -7.5 | 6e-12 | 28/44 (C-33 A, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.744×** | -7.4 | 7e-12 | 37/48 (NCI-H2030, RPMI-7951, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | **0.740×** | -7.3 | 2e-11 | 35/47 (RKO, CFPAC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.829×** | -4.7 | 1e-04 | 24/48 (AsPC-1, SW 900, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 0.846× | -4.2 | 0.001 | 22/48 (Hs 766T, AsPC-1, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.734×** | -4.1 | 0.002 | 24/48 (NCI-H23, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.866× | -3.6 | 0.012 | 16/48 (NCI-H23, SNU-1, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~92% of this change | 0.870× | -3.5 | 0.018 | 15/48 (CFPAC-1, HOP62, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.788×** | -3.1 | 0.058 | 20/48 (PANC-1, CHP-212, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.795×** | -3.0 | 0.083 | 15/48 (RKO, SNU-1, …) | top dose only | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.799×** | -2.9 | 0.099 | 16/47 (HepG2/C3A, hTERT-HPNE, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.37 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 624. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 148 | 6 (2 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.94× (z +32.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.547× (z -14.3) |
| [[A549 (line)]] | wt | 142 | 6 (2 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.80× (z +34.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.452× (z -15.6) |
| [[HOP62 (line)]] | alt | 163 | 4 | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +20.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.554× (z -13.7) |
| [[A498 (line)]] | wt | 119 | 5 (2 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.08× (z +30.1) | [[Panobinostat (drug)]] 0.5 µM 0.451× (z -12.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.598× (z -11.0) |
| [[LOX-IMVI (line)]] | wt | 206 | 3 | 5 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 9.64× (z +16.0) | [[Panobinostat (drug)]] 5 µM 0.436× (z -11.3) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.579× (z -10.5) |
| [[SK-MEL-2 (line)]] | alt | 192 | 3 | 5 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 7.46× (z +16.4) | [[Panobinostat (drug)]] 0.5 µM 0.447× (z -12.6) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.656× (z -9.4) |
| [[AsPC-1 (line)]] | alt | 176 | 2 | 5 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 5.54× (z +12.5) | [[Panobinostat (drug)]] 0.5 µM 0.352× (z -14.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.515× (z -13.0) |
| [[CFPAC-1 (line)]] | alt | 154 | 2 | 5 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 5.77× (z +12.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.412× (z -17.3) |
| [[HEC-1-A (line)]] | alt | 196 | 3 | 4 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 6.57× (z +15.9) | [[Panobinostat (drug)]] 5 µM 0.436× (z -13.3) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.587× (z -12.1) |
| [[NCI-H2347 (line)]] | alt | 150 | 3 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.83× (z +14.1) | [[Panobinostat (drug)]] 0.5 µM 0.421× (z -13.2) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.573× (z -12.0) |
| [[NCI-H460 (line)]] | wt | 116 | 5 (2 ⚠) | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.39× (z +16.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.630× (z -10.3) |
| [[SNU-423 (line)]] | alt | 292 | 3 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +17.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.507× (z -13.8) |
| [[SW480 (line)]] | alt | 182 | 2 | 5 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 10.7× (z +23.2) | [[Dinaciclib (drug)]] 5 µM 0.527× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change |
| [[A-427 (line)]] | wt | 135 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +17.2) | [[Dinaciclib (drug)]] 5 µM 0.353× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change |
| [[Hs 766T (line)]] | wt | 152 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +16.4) | [[Panobinostat (drug)]] 0.5 µM 0.453× (z -11.5) ⚠ cell-cycle shift, explains ~33% of this change |
| [[HS-578T (line)]] | alt | 152 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +23.4) | [[Panobinostat (drug)]] 0.5 µM 0.517× (z -9.3) ⚠ cell-cycle shift, explains ~33% of this change |
| [[NCI-H1573 (line)]] | alt | 124 | 4 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 15.6× (z +18.7) | [[Panobinostat (drug)]] 5 µM 0.486× (z -9.4) ⚠ cell-cycle shift, explains ~40% of this change |
| [[NCI-H1792 (line)]] | alt | 179 | 3 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 11.3× (z +18.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.513× (z -13.8) |
| [[Panc 03.27 (line)]] | alt | 120 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +17.0) | [[Panobinostat (drug)]] 0.5 µM 0.425× (z -11.0) ⚠ cell-cycle shift, explains ~33% of this change |
| [[RKO (line)]] | wt | 189 | 4 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 11.8× (z +16.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.467× (z -9.6) ⚠ toxic; cell-cycle shift, explains ~43% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.597× (z -9.6) |
| [[RPMI-7951 (line)]] | alt | 200 | 4 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.66× (z +14.6) | [[Panobinostat (drug)]] 5 µM 0.488× (z -9.9) ⚠ cell-cycle shift, explains ~40% of this change |
| [[SW 900 (line)]] | alt | 168 | 2 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 6.65× (z +13.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.527× (z -12.7) |
| [[C32 (line)]] | wt | 123 | 2 | 3 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 9.14× (z +14.1) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.342× (z -12.6) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.581× (z -9.4) |
| [[SW1417 (line)]] | alt | 158 | 3 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.59× (z +12.0) | [[Panobinostat (drug)]] 0.5 µM 0.520× (z -9.9) ⚠ cell-cycle shift, explains ~33% of this change |
| [[BT-474 (line)]] | alt | 81.2 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +11.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.475× (z -11.5) |
| [[HCT15 (line)]] | alt | 185 | 1 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.60× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.460× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.586× (z -9.7) |
| [[HT-29 (line)]] | alt | 141 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 9.18× (z +17.2) | [[Panobinostat (drug)]] 5 µM 0.514× (z -9.9) ⚠ cell-cycle shift, explains ~40% of this change |
| [[hTERT-HPNE (line)]] | wt | 142 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +15.5) | — |
| [[LoVo (line)]] | wt | 131 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.44× (z +14.8) | [[Dinaciclib (drug)]] 0.5 µM 0.446× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[NCI-H2030 (line)]] | alt | 105 | 2 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.92× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.442× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.574× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 261 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +18.0) | [[Dinaciclib (drug)]] 0.5 µM 0.571× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[PANC-1 (line)]] | alt | 146 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +34.6) | — |
| [[J82 (line)]] | alt | 164 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +19.5) | — |
| [[C-33 A (line)]] | alt | 173 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.03× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.220× (z -17.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change |
| [[HepG2_C3A (line)]] | wt | 194 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 7.03× (z +12.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -13.8) |
| [[LS 180 (line)]] | wt | 151 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 8.62× (z +15.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 127 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 6.05× (z +13.0) | — |
| [[SNU-1 (line)]] | wt | 176 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 7.39× (z +10.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.470× (z -10.4) |
| [[SW48 (line)]] | wt | 106 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 10.7× (z +11.4) | — |
| [[AN3 CA (line)]] | alt | 253 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.49× (z +8.9) | — |
| [[COLO 205 (line)]] | alt | 75.3 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 10.4× (z +11.5) | — |
| [[H4 (line)]] | wt | 123 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.97× (z +8.9) | — |
| [[SW 1271 (line)]] | alt | 179 | 0 | 1 | — | [[Dorzolamide (hydrochloride) (drug)]] 0.05 µM 0.226× (z -8.7) |
| [[CHP-212 (line)]] | wt | 124 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 196 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 624), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFHX2]] | +0.66 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[NDUFA5]] | +0.66 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[CFL2]] | +0.66 | +0.49 / +0.67 | both halves | 1e-05 |  |
| [[CHURC1]] | +0.65 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[POGZ]] | +0.65 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[DCUN1D1]] | +0.65 | +0.45 / +0.64 | both halves | 3e-05 |  |
| [[MRPS33]] | +0.64 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[MTMR3]] | +0.64 | +0.49 / +0.70 | both halves | 1e-05 |  |
| [[COQ5]] | +0.64 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[KPNA5]] | +0.64 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[ZNF780A]] | +0.63 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[VAPA]] | +0.63 | +0.51 / +0.66 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAD1L1]] | -0.65 | -0.54 / -0.66 | both halves | 1e-05 |  |
| [[TOP3A]] | -0.62 | -0.46 / -0.72 | both halves | 3e-05 |  |
| [[SENP5]] | -0.61 | -0.35 / -0.64 | both halves | 1e-04 |  |
| [[ZMYND19]] | -0.59 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[GPR89A]] | -0.59 | -0.40 / -0.61 | both halves | 5e-05 |  |
| [[PMPCA]] | -0.58 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[SS18L1]] | -0.58 | -0.39 / -0.57 | both halves | 6e-05 |  |
| [[PDCD6]] | -0.58 | -0.41 / -0.62 | both halves | 4e-05 |  |
| [[TMEM104]] | -0.57 | -0.33 / -0.63 | both halves | 1e-04 |  |
| [[ZCCHC17]] | -0.57 | -0.29 / -0.60 | both halves | 3e-04 |  |
| [[FBXW7]] | -0.56 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[AXIN1]] | -0.56 | -0.42 / -0.56 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises TAB2's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.620). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-26.3, 13.3); signed map (9.4, -25.0). **Vector** length 100, 30.8% of its response variance represented; |z| ≥ 3 in 1,176 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +9.2 | +14.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +9.1 | +17.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | +8.7 | +25.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | +7.8 | +6.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.4 | +2.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.4 | +15.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.0 | -0.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.8 | +0.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.7 | +1.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.1 | -3.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.8 | -7.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.8 | +2.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.6 | -4.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -3.3 | -7.8 |
|  | [[EX229 (drug)]] 5 µM |  | -3.1 | -2.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.8 | -3.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.6 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | TGF-beta activated kinase 1 (MAP3K7) binding protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q25.1 — chr6:149,218,641-149,411,613 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0733; previously MAP3K7IP2 |
| Gene groups (HGNC) | Zinc fingers RANBP2-type; CUE domain containing |
| Reactome | 51 pathways, smallest: IRAK2 mediated activation of TAK1 complex; Alpha-protein kinase 1 signaling pathway; TICAM1,TRAF6-dependent induction of TAK1 complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NYJ8](https://www.uniprot.org/uniprotkb/Q9NYJ8) (TGF-beta-activated kinase 1 and MAP3K7-binding protein 2):

> Adapter required to activate the JNK and NF-kappa-B signaling pathways through the specific recognition of 'Lys-63'-linked polyubiquitin chains by its RanBP2-type zinc finger (NZF). Acts as an adapter linking MAP3K7/TAK1 and TRAF6 to 'Lys-63'-linked polyubiquitin chains. The RanBP2-type zinc finger (NZF) specifically recognizes 'Lys-63'-linked polyubiquitin chains unanchored or anchored to the substrate proteins such as RIPK1/RIP1 and RIPK2: this acts as a scaffold to organize a large signaling …

**Summary**, from NCBI Gene [23118](https://www.ncbi.nlm.nih.gov/gene/23118):

> The protein encoded by this gene is an activator of MAP3K7/TAK1, which is required for for the IL-1 induced activation of nuclear factor kappaB and MAPK8/JNK. This protein forms a kinase complex with TRAF6, MAP3K7 and TAB1, and it thus serves as an adaptor that links MAP3K7 and TRAF6. This protein, along with TAB1 and MAP3K7, also participates in the signal transduction induced by TNFSF11/RANKl through the activation of the receptor activator of NF-kappaB (TNFRSF11A/RANK), which may regulate …

**Accessions** — [HGNC:17075](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17075) · Entrez [23118](https://www.ncbi.nlm.nih.gov/gene/23118) · UniProt [Q9NYJ8](https://www.uniprot.org/uniprotkb/Q9NYJ8) · Ensembl [ENSG00000055208](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000055208)

## Data

Gene col 624: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 624); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 624, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 624]; `tensor/DDL_lfc|DDL_z.npy` [624]; `embed/gene_vectors.npy` [624]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 624 or target_col == 624). Every well: [[TAB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TAB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
