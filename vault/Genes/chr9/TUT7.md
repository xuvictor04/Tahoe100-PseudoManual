---
symbol: "TUT7"
type: "gene"
col: 1365
ensembl_id: "ENSG00000083223"
name: "terminal uridylyl transferase 7"
location: "9q21.33"
module: 182
arm: "-"
pooled_cpm: 162.13
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 13
n_dd_up_clean: 15
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/182"]
generated_by: "tahoemap"
---

# TUT7

*terminal uridylyl transferase 7* — 9q21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.95× (z +22.9, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.581× (z -13.2, q 9e-37, down in 42 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Radotinib (drug)]] 5 µM: 0.791× (z -8.0, q 1e-13, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SETX]] (+0.77, fdr 7e-06), [[TANK]] (+0.69, fdr 7e-06), [[GPATCH2L]] (+0.67, fdr 7e-06); moves opposite to [[KDM1A]] (-0.76, fdr 7e-06), [[ALG9]] (-0.70, fdr 7e-06), [[SNRPA1]] (-0.66, fdr 7e-06).
> It sits in the **-** arm of [[Module 182]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[AP3B2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 1 with an alert ⚠; shown: the 15 strongest. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1365.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.95×** | +22.9 | 0e+00 | 45/48 (A498, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.15×** | +18.6 | 0e+00 | 47/48 (HEC-1-A, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.05×** | +17.3 | 0e+00 | 45/48 (A498, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.08×** | +14.5 | 3e-45 | 45/48 (A498, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.48×** | +9.4 | 5e-19 | 35/48 (SNU-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.40×** | +7.7 | 2e-12 | 28/48 (HT-29, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.34×** | +7.1 | 1e-10 | 30/48 (HT-29, HEC-1-A, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.32×** | +6.8 | 9e-10 | 31/48 (HepG2/C3A, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.28×** | +6.0 | 1e-07 | 26/48 (HT-29, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.24×** | +5.1 | 2e-05 | 29/48 (HepG2/C3A, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.23×** | +4.9 | 4e-05 | 25/48 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.48×** | +4.4 | 4e-04 | 26/48 (SW480, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | **1.38×** | +3.6 | 0.013 | 21/48 (AsPC-1, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.11× | +3.5 | 0.022 | 12/48 (MIA PaCa-2, NCI-H2347, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.34×** | +3.3 | 0.033 | 18/49 (AsPC-1, RPMI-7951, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1365.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.581×** | -13.2 | 9e-37 | 42/49 (NCI-H1792, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.566×** | -11.2 | 8e-27 | 35/44 (A-427, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.604×** | -9.5 | 3e-19 | 39/45 (SK-MEL-2, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **0.791×** | -8.0 | 1e-13 | 31/48 (RKO, NCI-H23, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.746×** | -7.1 | 1e-10 | 38/48 (HepG2/C3A, C32, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.813×** | -7.1 | 1e-10 | 25/48 (C32, SK-MEL-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.712×** | -6.7 | 2e-09 | 32/47 (H4, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.761×** | -6.6 | 3e-09 | 26/48 (NCI-H1792, RKO, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **0.624×** | -5.3 | 6e-06 | 33/48 (AsPC-1, RKO, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | 0.857× | -5.3 | 7e-06 | 21/49 (A498, A549, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.627×** | -5.3 | 8e-06 | 36/48 (AsPC-1, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.660×** | -4.7 | 1e-04 | 30/48 (NCI-H1792, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.882× | -4.3 | 9e-04 | 14/48 (NCI-H23, HOP62, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.873× | -4.1 | 0.001 | 16/48 (RKO, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.863× | -4.1 | 0.002 | 17/48 (NCI-H23, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | 0.860× | -4.1 | 0.002 | 17/49 (NCI-H23, RKO, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.849× | -4.0 | 0.002 | 20/49 (NCI-H23, C32, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.853× | -3.9 | 0.003 | 16/47 (NCI-H23, RKO, …) | inconsistent across doses |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | 0.848× | -3.8 | 0.004 | 18/48 (SK-MEL-2, HOP62, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.897× | -3.6 | 0.008 | 10/49 (HOP62, NCI-H23, …) | all doses, flat |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | 0.834× | -3.6 | 0.008 | 17/48 (SK-MEL-2, SNU-1, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1365. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 131 | 8 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.82× (z +18.0) | [[Dinaciclib (drug)]] 5 µM 0.396× (z -13.1) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 102 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +16.1) | — |
| [[A-172 (line)]] | wt | 205 | 5 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +18.1) | [[Dinaciclib (drug)]] 0.5 µM 0.433× (z -12.3) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 254 | 2 | 6 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.209× (z -16.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 277 | 4 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.82× (z +23.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -15.1) ⚠ cell-cycle shift, explains ~9% of this change |
| [[AsPC-1 (line)]] | alt | 228 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +21.7) | [[Dinaciclib (drug)]] 0.5 µM 0.453× (z -11.2) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 161 | 5 (1 ⚠) | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.60× (z +17.0) | [[Dinaciclib (drug)]] 0.5 µM 0.463× (z -13.6) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 88.8 | 6 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.54× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 2.38× (z +9.6) | — |
| [[HepG2_C3A (line)]] | wt | 130 | 4 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +15.6) | [[Ponatinib (drug)]] 5 µM 0.299× (z -13.4) |
| [[HT-29 (line)]] | alt | 199 | 4 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.28× (z +12.2) | [[Dinaciclib (drug)]] 0.5 µM 0.459× (z -11.7) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 204 | 3 | 3 (3 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 1.80× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.339× (z -14.4) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 175 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +13.6) | [[Dinaciclib (drug)]] 5 µM 0.438× (z -8.9) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 303 | 4 | 2 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.82× (z +12.8) | [[Dinaciclib (drug)]] 0.5 µM 0.417× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Radotinib (drug)]] 5 µM 0.582× (z -9.4) |
| [[A549 (line)]] | wt | 203 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +16.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.445× (z -14.4) ⚠ cell-cycle shift, explains ~9% of this change |
| [[C32 (line)]] | wt | 159 | 3 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +11.8) | [[Ponatinib (drug)]] 5 µM 0.365× (z -12.2) |
| [[COLO 205 (line)]] | alt | 266 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +14.6) | [[Panobinostat (drug)]] 5 µM 0.471× (z -9.6) ⚠ cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 146 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.461× (z -9.0) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 198 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +14.4) | [[Dinaciclib (drug)]] 5 µM 0.339× (z -13.7) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 181 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +21.2) | [[Dinaciclib (drug)]] 0.5 µM 0.481× (z -9.4) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 177 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +15.1) | [[Dinaciclib (drug)]] 5 µM 0.417× (z -9.2) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 226 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.90× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.308× (z -12.9) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 157 | 4 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 1.95× (z +9.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 128 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +21.6) | — |
| [[NCI-H1573 (line)]] | alt | 132 | 4 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.33× (z +16.1) | — |
| [[Panc 03.27 (line)]] | alt | 168 | 1 | 3 (3 ⚠) | [[Auranofin (drug)]] 5 µM 2.21× (z +10.5) | [[Lonafarnib (drug)]] 5 µM 0.0877× (z -15.0) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 100 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +16.3) | — |
| [[SK-MEL-2 (line)]] | alt | 145 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +13.2) | [[Dinaciclib (drug)]] 0.05 µM 0.241× (z -13.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 73.2 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.84× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.155× (z -17.4) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 176 | 2 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.75× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.214× (z -12.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 163 | 1 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.25× (z +12.8) | [[Dinaciclib (drug)]] 5 µM 0.352× (z -13.4) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 147 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +11.5) | — |
| [[NCI-H2347 (line)]] | alt | 79.5 | 3 | 0 | [[Auranofin (drug)]] 5 µM 2.62× (z +10.2) | — |
| [[SNU-423 (line)]] | alt | 266 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +12.3) | [[Dinaciclib (drug)]] 0.05 µM 0.260× (z -10.4) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 148 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.49× (z +10.6) | [[Dinaciclib (drug)]] 0.5 µM 0.463× (z -8.9) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 121 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +14.2) | — |
| [[H4 (line)]] | wt | 198 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.182× (z -13.2) ⚠ toxic |
| [[HS-578T (line)]] | alt | 133 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.21× (z +11.7) | — |
| [[NCI-H2030 (line)]] | alt | 86.4 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.13× (z +12.1) | — |
| [[RPMI-7951 (line)]] | alt | 185 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.54× (z +11.0) | — |
| [[SHP-77 (line)]] | alt | 85.3 | 2 | 0 | [[Auranofin (drug)]] 5 µM 2.33× (z +9.2) | — |
| [[CFPAC-1 (line)]] | alt | 103 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +15.6) | — |
| [[NCI-H661 (line)]] | alt | 68.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0699× (z -9.2) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 154 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.17× (z +10.7) | — |
| [[AN3 CA (line)]] | alt | 153 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 123 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 111 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 198 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 220 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1365), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*41 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SETX]] | +0.77 | +0.74 / +0.80 | both halves | 7e-06 |  |
| [[TANK]] | +0.69 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[GPATCH2L]] | +0.67 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[FAM32A]] | +0.65 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[MCL1]] | +0.65 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[CRK]] | +0.65 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[ERCC1]] | +0.62 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[WDR26]] | +0.61 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[BCL10]] | +0.61 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[BACH1]] | +0.61 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[NSRP1]] | +0.60 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[ZNF274]] | +0.60 | +0.59 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*59 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KDM1A]] | -0.76 | -0.77 / -0.69 | both halves | 7e-06 |  |
| [[ALG9]] | -0.70 | -0.61 / -0.77 | both halves | 7e-06 |  |
| [[SNRPA1]] | -0.66 | -0.66 / -0.61 | both halves | 7e-06 |  |
| [[PEBP1]] | -0.65 | -0.66 / -0.56 | both halves | 1e-05 |  |
| [[COPS7B]] | -0.64 | -0.65 / -0.60 | both halves | 7e-06 |  |
| [[HSF2]] | -0.64 | -0.64 / -0.61 | both halves | 7e-06 |  |
| [[MLLT10]] | -0.64 | -0.68 / -0.58 | both halves | 7e-06 |  |
| [[NDC1]] | -0.64 | -0.65 / -0.61 | both halves | 7e-06 |  |
| [[SEC61A2]] | -0.64 | -0.62 / -0.63 | both halves | 7e-06 |  |
| [[FAR1]] | -0.63 | -0.62 / -0.64 | both halves | 7e-06 |  |
| [[MRS2]] | -0.62 | -0.57 / -0.62 | both halves | 8e-06 |  |
| [[ABCB10]] | -0.62 | -0.64 / -0.58 | both halves | 8e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AP3B2]] | B | AP3B2 activity lowers TUT7's level | lines that do not express AP3B2 (15) vs lines expressing it (35) | 1.41× higher at baseline in the lines without AP3B2 | 0.013 | ⚠ within organs, on part of the lines; also absent: MAPK8IP2, MED12L, HRK; maybe low, not absent |
| [[CD163L1]] | B | CD163L1 activity raises TUT7's level | lines that do not express CD163L1 (24) vs lines expressing it (26) | 1.13× lower at baseline in the lines without CD163L1 | 0.070 | ⚠ within organs, on part of the lines; also absent: ENSG00000236212, ENSG00000230647, CNRIP1; maybe low, not absent |
| [[LINC02804]] | C | LINC02804's natural level strengthens TUT7's drug response | LINC02804's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.61, reverse +0.32; direction not clear | 0.093 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 182]]; 21 genes; this gene is in the **-** arm (projection on the module's main direction -0.837). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-7.3, -12.8); signed map (5.7, 24.6). **Vector** length 146, 52.9% of its response variance represented; |z| ≥ 3 in 1,361 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +13.4 | +18.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.4 | +14.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.7 | +17.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.3 | +22.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.2 | +7.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.9 | +3.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.9 | +7.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.7 | +4.4 |
|  | [[Mifepristone (drug)]] 0.5 µM |  | +2.9 | +1.3 |
| fall | [[Radotinib (drug)]] 5 µM |  | -6.9 | -8.0 |
|  | [[Selinexor (drug)]] 5 µM |  | -6.6 | -7.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -6.3 | -7.1 |
|  | [[venetoclax (drug)]] 5 µM |  | -5.8 | -5.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.8 | -6.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -5.4 | -3.4 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -4.9 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | terminal uridylyl transferase 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q21.33 — chr9:86,287,733-86,354,454 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1711, FLJ13409, PAPD6, TENT3B; previously ZCCHC6 |
| Gene groups (HGNC) | Zinc fingers CCHC-type; Non-canonical poly(A) polymerases; Terminal nucleotidyltransferases |
| Reactome | 6 pathways, smallest: Zygotic genome activation (ZGA); Z-decay: degradation of maternal mRNAs by zygotically expressed factors; Deadenylation of mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5VYS8](https://www.uniprot.org/uniprotkb/Q5VYS8) (Terminal uridylyltransferase 7):

> Uridylyltransferase that mediates the terminal uridylation of mRNAs with short (less than 25 nucleotides) poly(A) tails, hence facilitating global mRNA decay. Essential for both oocyte maturation and fertility. Through 3' terminal uridylation of mRNA, sculpts, with TUT7, the maternal transcriptome by eliminating transcripts during oocyte growth (By similarity). Involved in microRNA (miRNA)-induced gene silencing through uridylation of deadenylated miRNA targets. Also functions as an integral …

**Summary**, from NCBI Gene [79670](https://www.ncbi.nlm.nih.gov/gene/79670):

> Enables RNA uridylyltransferase activity and miRNA binding activity. Involved in RNA metabolic process and transposable element silencing by mRNA destabilization. Located in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25817](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25817) · Entrez [79670](https://www.ncbi.nlm.nih.gov/gene/79670) · UniProt [Q5VYS8](https://www.uniprot.org/uniprotkb/Q5VYS8) · Ensembl [ENSG00000083223](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000083223)

## Data

Gene col 1365: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1365); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1365, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1365]; `tensor/DDL_lfc|DDL_z.npy` [1365]; `embed/gene_vectors.npy` [1365]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1365 or target_col == 1365). Every well: [[TUT7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TUT7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
