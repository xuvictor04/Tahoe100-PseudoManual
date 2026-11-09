---
symbol: "MTMR3"
type: "gene"
col: 1929
ensembl_id: "ENSG00000100330"
name: "myotubularin related protein 3"
location: "22q12.2"
module: 51
arm: "+"
pooled_cpm: 142.06
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 19
n_dd_up_clean: 11
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# MTMR3

*myotubularin related protein 3* — 22q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.80× (z +14.0, q 9e-42, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.267× (z -21.4, q 0e+00, down in 43 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.513× (z -15.9, q 0e+00, down in 46 of 49 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RBM33]] (+0.66, fdr 7e-06), [[CUTALP]] (+0.64, fdr 9e-05), [[TAB2]] (+0.64, fdr 1e-05); moves opposite to [[TOP3A]] (-0.63, fdr 1e-05), [[SMG1P6]] (-0.58, fdr 6e-05), [[LRRC59]] (-0.58, fdr 7e-05).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[NDUFS4]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1929.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.80×** | +14.0 | 9e-42 | 43/48 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.27×** | +13.8 | 5e-41 | 48/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.01×** | +11.7 | 1e-29 | 46/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.63×** | +11.4 | 9e-28 | 47/49 (SW480, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.90×** | +10.8 | 2e-25 | 46/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.64×** | +8.3 | 1e-14 | 39/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.27×** | +7.2 | 4e-11 | 43/48 (SW480, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.54×** | +7.0 | 2e-10 | 39/48 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +5.7 | 9e-07 | 31/47 (LoVo, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.32×** | +4.7 | 1e-04 | 29/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.30×** | +4.4 | 5e-04 | 34/48 (KATO III, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.23×** | +3.4 | 0.030 | 23/48 (A-172, A498, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.22×** | +3.3 | 0.043 | 23/48 (HT-29, PANC-1, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.14× | +3.2 | 0.061 | 16/49 (CFPAC-1, Panc 03.27, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.20×** | +3.1 | 0.067 | 23/47 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 14 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1929.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.267×** | -21.4 | 0e+00 | 43/44 (Panc 03.27, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.328×** | -18.8 | 0e+00 | 49/49 (A-427, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.513×** | -15.9 | 0e+00 | 46/49 (A549, SW 900, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.560×** | -9.8 | 2e-20 | 45/48 (NCI-H1573, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.605×** | -8.5 | 3e-15 | 42/48 (NCI-H1792, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.637×** | -7.6 | 3e-12 | 42/48 (SNU-423, SW480, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.640×** | -7.2 | 4e-11 | 39/50 (C32, HS-578T, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.659×** | -6.5 | 6e-09 | 32/45 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.699×** | -6.0 | 1e-07 | 38/48 (HepG2/C3A, NCI-H1573, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.570×** | -4.9 | 4e-05 | 41/48 (SNU-1, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.756×** | -4.7 | 1e-04 | 35/48 (NCI-H2347, NCI-H1792, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.595×** | -4.6 | 2e-04 | 37/48 (MIA PaCa-2, SNU-1, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~49% of this change | **0.755×** | -4.6 | 2e-04 | 31/47 (MIA PaCa-2, RKO, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.763×** | -4.4 | 5e-04 | 33/48 (HOP62, SNU-423, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.833×** | -4.4 | 5e-04 | 21/48 (HOP62, A-172, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.629×** | -4.1 | 0.002 | 29/48 (NCI-H2347, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Thymol (drug)]] 5 µM |  | 0.870× | -3.3 | 0.025 | 10/48 (MIA PaCa-2, A-172, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.834× | -3.1 | 0.057 | 21/48 (NCI-H1573, NCI-H1792, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.5 µM |  | 0.841× | -2.9 | 0.089 | 22/48 (NCI-H1573, LOX-IMVI, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.42 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1929. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 130 | 7 (1 ⚠) | 7 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 6.49× (z +14.8) | [[Dinaciclib (drug)]] 5 µM 0.247× (z -20.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.468× (z -11.5) |
| [[NCI-H460 (line)]] | wt | 106 | 10 (2 ⚠) | 3 (2 ⚠) | [[Digitoxin (drug)]] 0.5 µM 4.05× (z +17.2) | [[Dinaciclib (drug)]] 5 µM 0.207× (z -18.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.606× (z -8.7) |
| [[NCI-H1792 (line)]] | alt | 182 | 4 (1 ⚠) | 7 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.62× (z +11.6) | [[Dinaciclib (drug)]] 0.5 µM 0.260× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -16.0) |
| [[SW 900 (line)]] | alt | 202 | 5 (1 ⚠) | 6 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.62× (z +11.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.317× (z -19.5) |
| [[NCI-H1573 (line)]] | alt | 200 | 5 (1 ⚠) | 5 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.84× (z +14.0) | [[Dinaciclib (drug)]] 0.5 µM 0.231× (z -19.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 112 | 6 (1 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.83× (z +14.3) | [[Dinaciclib (drug)]] 5 µM 0.359× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.590× (z -10.2) |
| [[C32 (line)]] | wt | 128 | 4 | 4 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 9.39× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.234× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.535× (z -9.1) |
| [[HS-578T (line)]] | alt | 187 | 1 | 7 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +15.7) | [[Dinaciclib (drug)]] 5 µM 0.262× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.430× (z -13.2) |
| [[KATO III (line)]] | alt | 139 | 6 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +15.5) | [[Dinaciclib (drug)]] 5 µM 0.122× (z -24.7) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 116 | 6 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.47× (z +15.3) | [[Dinaciclib (drug)]] 5 µM 0.243× (z -16.7) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 115 | 1 | 7 (6 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.39× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.240× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.387× (z -14.8) |
| [[SNU-423 (line)]] | alt | 150 | 1 | 7 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.342× (z -18.0) |
| [[A498 (line)]] | wt | 119 | 3 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.31× (z +21.0) | [[Dinaciclib (drug)]] 5 µM 0.232× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.482× (z -10.5) |
| [[BT-474 (line)]] | alt | 151 | 6 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +13.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.541× (z -9.4) |
| [[HepG2_C3A (line)]] | wt | 184 | 1 | 6 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 6.03× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.228× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.471× (z -10.8) |
| [[HT-29 (line)]] | alt | 103 | 4 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +13.2) | [[Dinaciclib (drug)]] 5 µM 0.268× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.579× (z -9.5) |
| [[NCI-H2347 (line)]] | alt | 235 | 1 | 6 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.18× (z +8.6) | [[Dinaciclib (drug)]] 0.05 µM 0.138× (z -20.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.318× (z -17.8) |
| [[SW48 (line)]] | wt | 145 | 4 | 3 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 4.85× (z +13.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.272× (z -16.6) |
| [[A-172 (line)]] | wt | 69.3 | 2 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +16.7) | [[Dinaciclib (drug)]] 0.5 µM 0.236× (z -16.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.377× (z -16.1) |
| [[A549 (line)]] | wt | 142 | 1 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +13.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.292× (z -21.9) |
| [[HOP62 (line)]] | alt | 105 | 0 | 6 (4 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.276× (z -13.8) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.485× (z -11.5) |
| [[Hs 766T (line)]] | wt | 122 | 3 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.37× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.284× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.532× (z -10.0) |
| [[MIA PaCa-2 (line)]] | alt | 108 | 2 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.23× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.352× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.459× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 161 | 3 (1 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.42× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.236× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.532× (z -10.5) |
| [[SW1417 (line)]] | alt | 275 | 2 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.235× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.456× (z -11.5) |
| [[AsPC-1 (line)]] | alt | 156 | 2 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -14.1) |
| [[HEC-1-A (line)]] | alt | 147 | 2 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.277× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.540× (z -8.8) |
| [[LS 180 (line)]] | wt | 122 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.91× (z +13.4) | [[Dinaciclib (drug)]] 5 µM 0.336× (z -10.4) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 115 | 2 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.0385× (z -35.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.483× (z -11.5) |
| [[A-427 (line)]] | wt | 103 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +12.0) | [[Dinaciclib (drug)]] 0.5 µM 0.0487× (z -36.6) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 174 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.233× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.484× (z -9.8) |
| [[COLO 205 (line)]] | alt | 142 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.270× (z -14.7) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 179 | 1 | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.35× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.270× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.529× (z -9.0) |
| [[hTERT-HPNE (line)]] | wt | 103 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -14.0) |
| [[J82 (line)]] | alt | 82.2 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +13.5) | [[Dinaciclib (drug)]] 5 µM 0.363× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.506× (z -9.9) |
| [[NCI-H2030 (line)]] | alt | 267 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0916× (z -20.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.453× (z -9.4) |
| [[RKO (line)]] | wt | 193 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +12.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.439× (z -12.0) |
| [[AN3 CA (line)]] | alt | 191 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.270× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.446× (z -8.9) |
| [[C-33 A (line)]] | alt | 147 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.59× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.229× (z -13.8) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 124 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.547× (z -9.2) |
| [[CHP-212 (line)]] | wt | 128 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0683× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.370× (z -8.6) |
| [[H4 (line)]] | wt | 72.4 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +9.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -8.7) |
| [[RPMI-7951 (line)]] | alt | 117 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.252× (z -13.9) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 180 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0273× (z -20.3) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 65.2 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.168× (z -9.3) ⚠ toxic |
| [[SW 1088 (line)]] | alt | 141 | 0 | 1 | — | [[Tetracycline (hydrochloride) (drug)]] 0.05 µM 0.0680× (z -10.4) |
| [[NCI-H2122 (line)]] | alt | 176 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 156 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 179 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 134 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1929), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBM33]] | +0.66 | +0.58 / +0.71 | both halves | 7e-06 |  |
| [[CUTALP]] | +0.64 | +0.36 / +0.66 | both halves | 9e-05 |  |
| [[TAB2]] | +0.64 | +0.49 / +0.70 | both halves | 1e-05 |  |
| [[SPPL3]] | +0.63 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[KAT6A]] | +0.63 | +0.43 / +0.69 | both halves | 3e-05 |  |
| [[LINC01273]] | +0.59 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[BRAF]] | +0.59 | +0.41 / +0.62 | both halves | 4e-05 |  |
| [[DHFR2]] | +0.59 | +0.26 / +0.57 | both halves | 4e-04 |  |
| [[MED13L]] | +0.58 | +0.46 / +0.63 | both halves | 3e-05 | same gene group |
| [[WDR31]] | +0.58 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[ITSN2]] | +0.58 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[VAPA]] | +0.58 | +0.55 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TOP3A]] | -0.63 | -0.52 / -0.67 | both halves | 1e-05 |  |
| [[SMG1P6]] | -0.58 | -0.39 / -0.58 | both halves | 6e-05 |  |
| [[LRRC59]] | -0.58 | -0.38 / -0.55 | both halves | 7e-05 |  |
| [[PMM2]] | -0.55 | -0.30 / -0.61 | both halves | 2e-04 |  |
| [[PDCD6]] | -0.53 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[TMEM181]] | -0.53 | -0.36 / -0.55 | both halves | 1e-04 | same gene group |
| [[ZNG1C]] | -0.53 | -0.40 / -0.55 | both halves | 5e-05 |  |
| [[GDI2]] | -0.53 | -0.37 / -0.48 | both halves | 7e-05 |  |
| [[EARS2]] | -0.53 | -0.35 / -0.56 | both halves | 1e-04 |  |
| [[MAD1L1]] | -0.51 | -0.36 / -0.53 | both halves | 9e-05 | same gene group |
| [[TSR1]] | -0.51 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[TOMM40]] | -0.51 | -0.42 / -0.48 | both halves | 4e-05 | pathway: Autophagy |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises MTMR3's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NDUFS4]] | C | MTMR3's natural level strengthens NDUFS4's drug response | MTMR3's natural level across 50 lines (lineage-adjusted; a glimpse) | r +0.60, reverse -0.10; direction not clear | 0.0995 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.445). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-26.0, 13.8); signed map (7.7, -13.9). **Vector** length 84.2, 32.6% of its response variance represented; |z| ≥ 3 in 1,386 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | +5.6 | -6.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.5 | +0.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.2 | +1.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.2 | +7.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.1 | -18.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.9 | -0.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.8 | -0.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | -2.1 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +2.6 | -1.9 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -8.2 | -4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.4 | -7.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -5.8 | -4.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.6 | -4.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -4.3 | -0.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.3 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | myotubularin related protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.2 — chr22:29,883,169-30,030,868 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0371, ZFYVE10, FYVE-DSP1 |
| Gene groups (HGNC) | Zinc fingers FYVE-type; Myotubularins; Phosphoinositide phosphatases; MicroRNA protein coding host genes |
| Reactome | 6 pathways, smallest: Synthesis of PIPs at the plasma membrane; PI Metabolism; Macroautophagy |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13615](https://www.uniprot.org/uniprotkb/Q13615) (Phosphatidylinositol-3,5-bisphosphate 3-phosphatase MTMR3):

> Lipid phosphatase that specifically dephosphorylates the D-3 position of phosphatidylinositol 3-phosphate and phosphatidylinositol 3,5-bisphosphate, generating phosphatidylinositol and phosphatidylinositol 5-phosphate. Decreases the levels of phosphatidylinositol 3-phosphate, a phospholipid found in cell membranes where it acts as key regulator of both cell signaling and intracellular membrane traffic. Could also have a molecular sequestering/adapter activity and regulate biological processes …

**Summary**, from NCBI Gene [8897](https://www.ncbi.nlm.nih.gov/gene/8897):

> This gene encodes a member of the myotubularin dual specificity protein phosphatase gene family. The encoded protein is structurally similar to myotubularin but in addition contains a FYVE domain and an N-terminal PH-GRAM domain. The protein can self-associate and also form heteromers with another myotubularin related protein. The protein binds to phosphoinositide lipids through the PH-GRAM domain, and can hydrolyze phosphatidylinositol(3)-phosphate and phosphatidylinositol(3,5)-biphosphate in …

**Accessions** — [HGNC:7451](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7451) · Entrez [8897](https://www.ncbi.nlm.nih.gov/gene/8897) · UniProt [Q13615](https://www.uniprot.org/uniprotkb/Q13615) · Ensembl [ENSG00000100330](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100330)

## Data

Gene col 1929: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1929); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1929, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1929]; `tensor/DDL_lfc|DDL_z.npy` [1929]; `embed/gene_vectors.npy` [1929]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1929 or target_col == 1929). Every well: [[MTMR3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTMR3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
