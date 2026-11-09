---
symbol: "CTTN"
type: "gene"
col: 1438
ensembl_id: "ENSG00000085733"
name: "cortactin"
location: "11q13.3"
module: 17
arm: "-"
pooled_cpm: 189.82
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 7
n_dd_up_clean: 16
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# CTTN

*cortactin* — 11q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.41× (z +26.2, q 0e+00, up in 48 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.58× (z +13.7, q 1e-40, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.677× (z -11.7, q 1e-28, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (86 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 18 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AP2B1]] (+0.57, fdr 4e-05), [[CTTN-DT]] (+0.57, fdr 3e-04, ⚠ same locus), [[CERS2]] (+0.57, fdr 6e-05), [[LY6G5B]] (+0.56, fdr 1e-04); moves opposite to [[ARL4A]] (-0.62, fdr 1e-05), [[GPATCH11]] (-0.61, fdr 2e-05), [[CYC1]] (-0.61, fdr 3e-05).
> It sits in the **-** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 47 in all, 15 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1438.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.41×** | +26.2 | 0e+00 | 48/49 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.28×** | +23.6 | 0e+00 | 44/44 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.07×** | +20.1 | 0e+00 | 43/45 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.58×** | +13.7 | 1e-40 | 42/48 (MIA PaCa-2, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.56×** | +13.2 | 1e-37 | 42/48 (NCI-H1573, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.47×** | +11.4 | 2e-28 | 38/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.41×** | +10.2 | 2e-22 | 37/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.20×** | +7.7 | 7e-13 | 25/48 (LS 180, HOP62, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +7.3 | 1e-11 | 28/50 (LOX-IMVI, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.27×** | +7.2 | 3e-11 | 26/48 (NCI-H1573, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.18× | +7.1 | 8e-11 | 17/49 (HT-29, LS 180, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.56×** | +6.9 | 2e-10 | 34/48 (NCI-H1573, HS-578T, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +6.8 | 5e-10 | 26/48 (LOX-IMVI, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.54×** | +6.8 | 5e-10 | 36/49 (NCI-H1573, A-172, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.27×** | +6.8 | 5e-10 | 30/47 (NCI-H1573, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.15× | +5.9 | 1e-07 | 14/48 (SNU-1, NCI-H460, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.20×** | +5.4 | 2e-06 | 23/48 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.22×** | +5.2 | 5e-06 | 24/48 (LS 180, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.18× | +4.9 | 3e-05 | 21/48 (PANC-1, HT-29, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.34×** | +4.6 | 1e-04 | 22/48 (SW480, A498, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1438.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.677×** | -11.7 | 1e-28 | 41/48 (MIA PaCa-2, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.696×** | -10.8 | 6e-25 | 39/48 (MIA PaCa-2, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.747×** | -8.7 | 5e-16 | 32/48 (MIA PaCa-2, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.832×** | -7.8 | 1e-12 | 22/48 (CFPAC-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.796×** | -6.8 | 9e-10 | 29/48 (SK-MEL-2, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.721×** | -5.1 | 3e-05 | 32/49 (SK-MEL-2, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **0.728×** | -5.0 | 6e-05 | 28/49 (PANC-1, RPMI-7951, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.869× | -4.9 | 7e-05 | 16/48 (NCI-H23, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.840× | -4.6 | 2e-04 | 22/48 (HEC-1-A, A-427, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.877× | -3.9 | 0.005 | 14/47 (NCI-H23, BT-474, …) | two highest doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.891× | -3.6 | 0.014 | 11/50 (HOP62, SW 900, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.885× | -3.5 | 0.019 | 17/48 (HEC-1-A, BT-474, …) | top dose only | composition shift |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.913× | -3.4 | 0.034 | 4/48 (SW480, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.893× | -3.1 | 0.069 | 6/48 (HOP62, NCI-H23, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1438. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 146 | 8 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.96× (z +14.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.02× (z +10.1) | — |
| [[HEC-1-A (line)]] | alt | 179 | 4 (3 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.30× (z +15.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 1.80× (z +10.6) | [[Homoharringtonine (drug)]] 5 µM 0.521× (z -16.8) |
| [[NCI-H460 (line)]] | wt | 97.9 | 7 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.23× (z +16.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.44× (z +12.8) | — |
| [[Hs 766T (line)]] | wt | 228 | 5 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.39× (z +13.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.15× (z +12.2) | [[Panobinostat (drug)]] 5 µM 0.572× (z -8.9) |
| [[J82 (line)]] | alt | 212 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.41× (z +13.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.640× (z -9.5) |
| [[MIA PaCa-2 (line)]] | alt | 189 | 3 (2 ⚠) | 3 | [[Auranofin (drug)]] 5 µM 2.41× (z +11.9) | [[Panobinostat (drug)]] 5 µM 0.368× (z -13.6) |
| [[NCI-H1573 (line)]] | alt | 294 | 6 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.35× (z +13.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.31× (z +12.9) | — |
| [[AsPC-1 (line)]] | alt | 241 | 4 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.63× (z +16.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.89× (z +10.6) | [[Panobinostat (drug)]] 5 µM 0.566× (z -9.5) |
| [[C32 (line)]] | wt | 152 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.70× (z +17.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 1.91× (z +8.7) | — |
| [[LOX-IMVI (line)]] | wt | 205 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.25× (z +19.5) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.02× (z +11.2) | — |
| [[NCI-H2347 (line)]] | alt | 206 | 4 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.38× (z +14.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.609× (z -12.0) |
| [[A-172 (line)]] | wt | 180 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.00× (z +9.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 1.85× (z +9.1) | — |
| [[A-427 (line)]] | wt | 145 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.40× (z +13.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.456× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 112 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.03× (z +15.9) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 173 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.47× (z +14.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.394× (z -20.5) |
| [[LoVo (line)]] | wt | 156 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.33× (z +18.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.504× (z -14.9) |
| [[LS 180 (line)]] | wt | 167 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.10× (z +17.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 1.72× (z +8.7) | — |
| [[NCI-H1792 (line)]] | alt | 85.2 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.91× (z +15.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.468× (z -12.1) |
| [[NCI-H2030 (line)]] | alt | 139 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.20× (z +15.2) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 414 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.25× (z +14.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.646× (z -10.8) |
| [[PANC-1 (line)]] | alt | 268 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.83× (z +23.8) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 135 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.50× (z +16.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.12× (z +10.1) | — |
| [[C-33 A (line)]] | alt | 118 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.17× (z +12.8) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 199 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.26× (z +14.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.531× (z -11.3) |
| [[HOP62 (line)]] | alt | 227 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.28× (z +20.6) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 275 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.71× (z +13.4) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 161 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.00× (z +15.0) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 223 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 2.12× (z +10.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.644× (z -10.1) |
| [[RPMI-7951 (line)]] | alt | 149 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.40× (z +10.4) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 474 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 1.75× (z +9.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.523× (z -11.1) |
| [[SW 900 (line)]] | alt | 136 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.12× (z +14.6) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 211 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.51× (z +16.2) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 134 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.05× (z +13.0) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 170 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.93× (z +16.0) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 115 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.38× (z +11.2) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 118 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.20× (z +9.1) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 259 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.27× (z +12.9) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 187 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.497× (z -10.6) |
| [[SNU-423 (line)]] | alt | 210 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.03× (z +9.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.402× (z -12.3) |
| [[BT-474 (line)]] | alt | 247 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -18.7) |
| [[CHP-212 (line)]] | wt | 124 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.66× (z +9.8) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 166 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.426× (z -9.5) |
| [[H4 (line)]] | wt | 139 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.57× (z +8.9) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 151 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.50× (z +10.5) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 165 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.55× (z +10.1) ⚠ toxic; transcription drop | — |
| [[NCI-H2122 (line)]] | alt | 172 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 182 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 85.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 186 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1438), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*35 of its nearest partners move with it, 5 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AP2B1]] | +0.57 | +0.42 / +0.64 | both halves | 4e-05 | pathway: Clathrin-mediated endocytosis |
| [[CTTN-DT]] | +0.57 | +0.29 / +0.43 | both halves | 3e-04 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[CERS2]] | +0.57 | +0.39 / +0.58 | both halves | 6e-05 |  |
| [[LY6G5B]] | +0.56 | +0.33 / +0.53 | both halves | 1e-04 |  |
| [[SLC25A53]] | +0.55 | +0.42 / +0.45 | both halves | 4e-05 |  |
| [[UBE2V1]] | +0.55 | +0.36 / +0.57 | both halves | 9e-05 |  |
| [[M6PR]] | +0.54 | +0.29 / +0.51 | both halves | 2e-04 | pathway: Clathrin-mediated endocytosis |
| [[ZNF514]] | +0.54 | +0.24 / +0.55 | both halves | 5e-04 |  |
| [[BCL2L2]] | +0.53 | +0.46 / +0.45 | both halves | 3e-05 |  |
| [[APP]] | +0.53 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[CAPN1]] | +0.52 | +0.45 / +0.66 | both halves | 3e-05 | STRING 534 |
| [[CTC-338M12.4]] | +0.52 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[LENG8]] | +0.52 | +0.43 / +0.56 | both halves | 3e-05 |  |

## Genes that move opposite

*65 of its nearest partners move opposite, 13 of them with an alert (⚠; 10 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARL4A]] | -0.62 | -0.51 / -0.64 | both halves | 1e-05 |  |
| [[GPATCH11]] | -0.61 | -0.47 / -0.60 | both halves | 2e-05 |  |
| [[CYC1]] | -0.61 | -0.44 / -0.60 | both halves | 3e-05 |  |
| [[KRTCAP2]] | -0.60 | -0.33 / -0.62 | both halves | 1e-04 |  |
| [[CHD1]] | -0.60 | -0.26 / -0.60 | both halves | 4e-04 |  |
| [[LEO1]] | -0.59 | -0.46 / -0.59 | both halves | 3e-05 |  |
| [[HPF1]] | -0.59 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[ZNF184]] | -0.58 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[RP9]] | -0.56 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[C17orf58]] | -0.56 | -0.37 / -0.56 | both halves | 8e-05 |  |
| [[MRPL57]] | -0.56 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[TPR]] | -0.55 | -0.49 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises CTTN's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **-** arm (projection on the module's main direction -0.434). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-49.6, -15.5); signed map (-17.0, -32.4). **Vector** length 117, 37.5% of its response variance represented; |z| ≥ 3 in 1,396 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.4 | +23.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +9.2 | +13.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.4 | +26.2 |
|  | [[Selinexor (drug)]] 5 µM |  | +8.2 | +7.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +8.1 | +6.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +7.1 | +5.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.5 | +3.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.3 | +3.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.3 | +2.9 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -7.6 | -3.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.1 | -7.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.9 | -4.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.5 | -0.3 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.9 | -10.8 |
|  | [[Arbutin (drug)]] 5 µM |  | -2.1 | +0.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.0 | -4.9 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | -1.9 | -1.5 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -1.9 | -0.5 |
|  | [[Gemcitabine (drug)]] 5 µM |  | -1.8 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | cortactin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.3 — chr11:70,398,404-70,436,584 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously EMS1 |
| Gene groups (HGNC) | SH3 domain containing |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 7 pathways, smallest: RHO GTPases activate PAKs; Clathrin-mediated endocytosis; RHO GTPase Effectors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14247](https://www.uniprot.org/uniprotkb/Q14247) (Src substrate cortactin):

> Contributes to the organization of the actin cytoskeleton and cell shape. Plays a role in the formation of lamellipodia and in cell migration. Plays a role in the regulation of neuron morphology, axon growth and formation of neuronal growth cones (By similarity). Through its interaction with CTTNBP2, involved in the regulation of neuronal spine density (By similarity). Plays a role in focal adhesion assembly and turnover (By similarity). In complex with ABL1 and MYLK regulates cortical …

**Summary**, from NCBI Gene [2017](https://www.ncbi.nlm.nih.gov/gene/2017):

> This gene is overexpressed in breast cancer and squamous cell carcinomas of the head and neck. The encoded protein is localized in the cytoplasm and in areas of the cell-substratum contacts. This gene has two roles: (1) regulating the interactions between components of adherens-type junctions and (2) organizing the cytoskeleton and cell adhesion structures of epithelia and carcinoma cells. During apoptosis, the encoded protein is degraded in a caspase-dependent manner. The aberrant regulation …

**Accessions** — [HGNC:3338](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3338) · Entrez [2017](https://www.ncbi.nlm.nih.gov/gene/2017) · UniProt [Q14247](https://www.uniprot.org/uniprotkb/Q14247) · Ensembl [ENSG00000085733](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000085733)

## Data

Gene col 1438: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1438); `tables/drug_effects.parquet` (61 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1438, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1438]; `tensor/DDL_lfc|DDL_z.npy` [1438]; `embed/gene_vectors.npy` [1438]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1438 or target_col == 1438). Every well: [[CTTN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CTTN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
