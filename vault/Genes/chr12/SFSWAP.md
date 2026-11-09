---
symbol: "SFSWAP"
type: "gene"
col: 704
ensembl_id: "ENSG00000061936"
name: "splicing factor SWAP"
location: "12q24.33"
module: 11
arm: "+"
pooled_cpm: 153.93
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 12
n_dd_up_clean: 15
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# SFSWAP

*splicing factor SWAP* — 12q24.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.03× (z +26.6, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.535× (z -22.7, q 0e+00, down in 37 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.686× (z -20.0, q 0e+00, down in 41 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NMT1]] (+0.68, fdr 7e-06), [[UBE2J2]] (+0.67, fdr 7e-06), [[ZC3H18]] (+0.65, fdr 7e-06); moves opposite to [[NIPBL-DT]] (-0.57, fdr 3e-05), [[EDEM1]] (-0.56, fdr 3e-05), [[EPB41L2]] (-0.56, fdr 2e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 704.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.03×** | +26.6 | 0e+00 | 48/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.57×** | +23.8 | 0e+00 | 43/48 (PANC-1, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.63×** | +18.4 | 0e+00 | 46/48 (LoVo, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.59×** | +17.4 | 0e+00 | 44/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.54×** | +16.1 | 0e+00 | 43/48 (BT-474, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.53×** | +16.0 | 0e+00 | 46/48 (LoVo, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.98×** | +13.4 | 5e-39 | 43/49 (LoVo, COLO 205, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.35×** | +11.4 | 5e-28 | 39/48 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.24×** | +8.2 | 2e-14 | 28/48 (HOP62, HEC-1-A, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.29×** | +7.9 | 1e-13 | 34/48 (PANC-1, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.23×** | +7.7 | 5e-13 | 23/48 (NCI-H2030, MIA PaCa-2, …) | all doses, flat |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.47×** | +7.6 | 1e-12 | 33/48 (LoVo, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~10% of this change | **1.20×** | +6.9 | 2e-10 | 24/47 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~11% of this change | **1.20×** | +6.9 | 3e-10 | 23/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.35×** | +5.8 | 2e-07 | 29/48 (A498, SW1417, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.14× | +5.0 | 2e-05 | 10/48 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | 1.18× | +4.4 | 3e-04 | 21/49 (MIA PaCa-2, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.12× | +4.3 | 5e-04 | 7/48 (LOX-IMVI, SW480, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 1.12× | +4.2 | 8e-04 | 5/48 (A-427, COLO 205, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 704.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.535×** | -22.7 | 0e+00 | 37/44 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.553×** | -22.3 | 0e+00 | 44/49 (COLO 205, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.686×** | -20.0 | 0e+00 | 41/49 (A-172, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.801×** | -11.8 | 5e-30 | 33/48 (J82, HEC-1-A, …) | rises with dose | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.723×** | -11.8 | 7e-30 | 36/48 (A-172, SW480, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.736×** | -11.1 | 1e-26 | 32/50 (SK-MEL-2, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.819×** | -10.6 | 2e-24 | 28/48 (HOP62, HEC-1-A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.743×** | -10.4 | 3e-23 | 31/45 (SW48, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.798×** | -8.5 | 1e-15 | 29/48 (NCI-H1573, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.802×** | -8.3 | 6e-15 | 28/49 (A-172, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~12% of this change | **0.819×** | -7.3 | 2e-11 | 26/47 (NCI-H2030, LoVo, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.782×** | -4.8 | 6e-05 | 22/49 (LOX-IMVI, A549, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 0.907× | -3.7 | 0.009 | 6/48 (C-33 A, SW480, …) | rises with dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.907× | -3.7 | 0.009 | 3/48 (C-33 A, H4, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 0.944× | -3.1 | 0.078 | 0/48 | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 704. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 210 | 8 (1 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.51× (z +21.4) | [[Dinaciclib (drug)]] 5 µM 0.467× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.636× (z -15.0) |
| [[PANC-1 (line)]] | alt | 155 | 9 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +25.0) | [[Dinaciclib (drug)]] 0.5 µM 0.428× (z -16.7) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 214 | 5 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +12.7) | [[Dinaciclib (drug)]] 5 µM 0.325× (z -18.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.505× (z -16.4) |
| [[SW480 (line)]] | alt | 146 | 7 (2 ⚠) | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.45× (z +19.1) | [[Dinaciclib (drug)]] 0.5 µM 0.388× (z -20.3) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.582× (z -11.2) |
| [[NCI-H1573 (line)]] | alt | 206 | 6 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +20.2) | [[Dinaciclib (drug)]] 5 µM 0.347× (z -17.0) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 157 | 6 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.58× (z +14.8) | [[Dinaciclib (drug)]] 0.5 µM 0.522× (z -10.1) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 187 | 1 | 7 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.71× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.522× (z -15.8) |
| [[AsPC-1 (line)]] | alt | 132 | 5 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +17.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.545× (z -12.1) |
| [[COLO 205 (line)]] | alt | 157 | 6 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.77× (z +23.8) | [[Dinaciclib (drug)]] 0.5 µM 0.170× (z -22.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 128 | 4 (1 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.22× (z +13.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.607× (z -12.3) |
| [[NCI-H23 (line)]] | alt | 190 | 5 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +16.8) | [[Dinaciclib (drug)]] 5 µM 0.388× (z -16.2) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 201 | 5 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.05× (z +12.8) | [[Dinaciclib (drug)]] 5 µM 0.328× (z -19.1) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 188 | 5 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.64× (z +15.3) | [[Dinaciclib (drug)]] 0.5 µM 0.293× (z -19.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.602× (z -11.3) |
| [[SNU-1 (line)]] | wt | 161 | 6 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.25× (z +13.5) | [[Dinaciclib (drug)]] 0.5 µM 0.384× (z -10.8) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 116 | 6 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.39× (z +16.7) | [[Dinaciclib (drug)]] 5 µM 0.421× (z -11.4) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 130 | 3 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.72× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.165× (z -35.2) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 136 | 3 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +14.1) | [[Dinaciclib (drug)]] 0.5 µM 0.544× (z -8.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.652× (z -8.7) |
| [[LS 180 (line)]] | wt | 140 | 4 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.70× (z +14.7) | [[Dinaciclib (drug)]] 0.05 µM 0.453× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.626× (z -9.7) |
| [[SNU-423 (line)]] | alt | 167 | 1 | 5 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.73× (z +9.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.582× (z -13.6) |
| [[BT-474 (line)]] | alt | 168 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.95× (z +17.1) | — |
| [[A-172 (line)]] | wt | 124 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -21.6) |
| [[CFPAC-1 (line)]] | alt | 121 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +14.3) | [[Dinaciclib (drug)]] 0.5 µM 0.536× (z -10.0) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 140 | 3 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.08× (z +9.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.617× (z -9.2) |
| [[J82 (line)]] | alt | 144 | 0 | 4 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.617× (z -12.9) ⚠ cell-cycle shift, explains ~14% of this change |
| [[MIA PaCa-2 (line)]] | alt | 130 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +13.0) | [[Dinaciclib (drug)]] 5 µM 0.389× (z -14.6) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 208 | 1 | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.13× (z +9.5) | [[Dinaciclib (drug)]] 0.05 µM 0.280× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.481× (z -8.9) |
| [[A-427 (line)]] | wt | 145 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.06× (z +11.6) | [[Selinexor (drug)]] 5 µM 0.666× (z -9.5) ⚠ cell-cycle shift, explains ~14% of this change |
| [[A498 (line)]] | wt | 139 | 1 | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.60× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.624× (z -12.4) |
| [[A549 (line)]] | wt | 165 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.459× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.665× (z -10.0) |
| [[C-33 A (line)]] | alt | 165 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.250× (z -18.2) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 176 | 2 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.58× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.297× (z -14.6) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 108 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +10.9) | — |
| [[SHP-77 (line)]] | alt | 216 | 2 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.85× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.442× (z -13.4) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 176 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.58× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.499× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.506× (z -9.8) |
| [[hTERT-HPNE (line)]] | wt | 150 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.396× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.554× (z -11.2) |
| [[KATO III (line)]] | alt | 88.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +10.9) | — |
| [[NCI-H2347 (line)]] | alt | 140 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.52× (z +11.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.664× (z -10.8) |
| [[Panc 03.27 (line)]] | alt | 113 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.89× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.387× (z -13.8) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 158 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.509× (z -13.0) |
| [[C32 (line)]] | wt | 142 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.350× (z -13.7) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 172 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.203× (z -13.6) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 98.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.621× (z -8.5) |
| [[SW1417 (line)]] | alt | 151 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.59× (z +8.5) | — |
| [[AN3 CA (line)]] | alt | 182 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 134 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 160 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 188 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 704), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NMT1]] | +0.68 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[UBE2J2]] | +0.67 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[ZC3H18]] | +0.65 | +0.68 / +0.63 | both halves | 7e-06 | STRING 523 |
| [[PIAS4]] | +0.62 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[KMT2B]] | +0.61 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[ESF1]] | +0.61 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[CEBPZ]] | +0.60 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[ECSIT]] | +0.60 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[TTC17]] | +0.59 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[HMGXB4]] | +0.59 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[CHMP1A]] | +0.59 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[CWC22]] | +0.58 | +0.66 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NIPBL-DT]] | -0.57 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[EDEM1]] | -0.56 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[EPB41L2]] | -0.56 | -0.60 / -0.48 | both halves | 2e-05 |  |
| [[ITM2C]] | -0.53 | -0.41 / -0.61 | both halves | 4e-05 |  |
| [[GLUD1]] | -0.52 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[SUMO1]] | -0.52 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[PGRMC1]] | -0.52 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[SPOPL]] | -0.51 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[ANKRD30BL]] | -0.50 | -0.39 / -0.47 | both halves | 5e-05 |  |
| [[FAM199X]] | -0.50 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[RASSF3]] | -0.49 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[CMTM6]] | -0.49 | -0.40 / -0.55 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises SFSWAP's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.421). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-42.8, 2.5); signed map (-4.4, -15.7). **Vector** length 107, 33.8% of its response variance represented; |z| ≥ 3 in 1,319 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.1 | +23.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.5 | +1.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.5 | +17.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +4.4 | +18.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.1 | +0.5 |
|  | [[EX229 (drug)]] 5 µM |  | +4.0 | +5.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.4 | +4.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +5.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.2 | -0.6 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.0 | -0.3 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | -5.9 | -11.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.8 | -11.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.7 | -8.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.6 | -10.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.8 | -11.1 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -3.2 | -0.3 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -3.1 | -1.9 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -2.6 | -0.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.3 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | splicing factor SWAP |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.33 — chr12:131,711,081-131,799,738 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SWAP; previously SFRS8 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12872](https://www.uniprot.org/uniprotkb/Q12872) (Splicing factor, suppressor of white-apricot homolog):

> Plays a role as an alternative splicing regulator. Regulate its own expression at the level of RNA processing. Also regulates the splicing of fibronectin and CD45 genes. May act, at least in part, by interaction with other R/S-containing splicing factors. Represses the splicing of MAPT/Tau exon 10.

**Summary**, from NCBI Gene [6433](https://www.ncbi.nlm.nih.gov/gene/6433):

> This gene encodes a human homolog of Drosophila splicing regulatory protein. This gene autoregulates its expression by control of splicing of its first two introns. In addition, it also regulates the splicing of fibronectin and CD45 genes. Two transcript variants encoding different isoforms have been identified. [provided by RefSeq, May 2012]

**Accessions** — [HGNC:10790](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10790) · Entrez [6433](https://www.ncbi.nlm.nih.gov/gene/6433) · UniProt [Q12872](https://www.uniprot.org/uniprotkb/Q12872) · Ensembl [ENSG00000061936](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000061936)

## Data

Gene col 704: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 704); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 704, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 704]; `tensor/DDL_lfc|DDL_z.npy` [704]; `embed/gene_vectors.npy` [704]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 704 or target_col == 704). Every well: [[SFSWAP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SFSWAP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
