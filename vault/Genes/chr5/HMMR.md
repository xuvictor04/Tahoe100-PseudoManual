---
symbol: "HMMR"
type: "gene"
col: 1023
ensembl_id: "ENSG00000072571"
name: "hyaluronan mediated motility receptor"
location: "5q34"
module: 22
arm: "+"
pooled_cpm: 50.67
n_lines_expressing: 50
n_dd_up: 36
n_dd_down: 29
n_dd_up_clean: 21
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# HMMR

*hyaluronan mediated motility receptor* — 5q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.91× (z +23.6, q 0e+00, up in 46 of 48 measured lines) ⚠ cell-cycle shift, explains ~65% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.20× (z +11.7, q 3e-29, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (16 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.507× (z -7.1, q 8e-10, down in 34 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.520× (z -6.8, q 3e-09, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DEPDC1]] (+0.90, fdr 7e-06), [[ASPM]] (+0.88, fdr 7e-06), [[SPDL1]] (+0.84, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[NDC80]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 15 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1023.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **4.91×** | +23.6 | 0e+00 | 46/48 (LoVo, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **3.46×** | +12.5 | 2e-33 | 45/48 (PANC-1, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **3.14×** | +12.0 | 7e-31 | 42/45 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.20×** | +11.7 | 3e-29 | 40/48 (RKO, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **3.00×** | +11.5 | 2e-28 | 41/48 (RKO, C32, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **3.07×** | +11.3 | 1e-27 | 39/40 (A498, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~88% of this change | **2.09×** | +7.7 | 9e-13 | 40/48 (HOP62, SW1417, …) | all doses, flat | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **2.06×** | +7.6 | 3e-12 | 39/48 (LoVo, C32, …) | all doses, stronger at high dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.63×** | +7.3 | 2e-11 | 43/48 (HOP62, CFPAC-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.12×** | +7.3 | 2e-11 | 32/42 (C-33 A, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.84×** | +6.4 | 8e-09 | 36/48 (C32, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.63×** | +5.1 | 1e-05 | 33/48 (NCI-H2030, HT-29, …) | all doses, flat |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **2.51×** | +5.0 | 2e-05 | 32/47 (PANC-1, J82, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +4.9 | 4e-05 | 29/48 (A-172, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 5 µM |  | **1.38×** | +4.7 | 8e-05 | 29/48 (HT-29, NCI-H2030, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.54×** | +4.2 | 0.001 | 26/47 (C32, A549, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.47×** | +4.0 | 0.002 | 23/47 (HOP62, SW 900, …) | all doses, flat | position effect removed |
| [[HI-TOPK-032 (drug)]] 0.5 µM |  | **1.70×** | +4.0 | 0.002 | 22/48 (HOP62, A549, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.50×** | +3.9 | 0.002 | 25/48 (NCI-H460, SW 900, …) | all doses, flat | position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.43×** | +3.8 | 0.005 | 20/48 (SW 900, HOP62, …) | two highest doses | position effect removed |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.41×** | +3.6 | 0.008 | 19/48 (NCI-H460, LOX-IMVI, …) | inconsistent across doses | position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **1.42×** | +3.6 | 0.009 | 25/47 (HOP62, NCI-H460, …) | all doses, flat | position effect removed |
| [[Mebendazole (drug)]] 0.5 µM |  | **1.40×** | +3.5 | 0.009 | 22/48 (SW 900, HT-29, …) | rises with dose | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **1.40×** | +3.5 | 0.010 | 23/48 (HOP62, NCI-H460, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.39×** | +3.5 | 0.010 | 17/48 (A498, H4, …) | inconsistent across doses | cell-cycle shift (explains ~20% here); position effect removed |
| [[Sodium Salicylate (drug)]] 5 µM |  | **1.26×** | +3.5 | 0.011 | 20/48 (A498, AsPC-1, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 16 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1023.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.507×** | -7.1 | 8e-10 | 34/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.520×** | -6.8 | 3e-09 | 35/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **0.533×** | -6.6 | 8e-09 | 34/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **0.520×** | -6.6 | 8e-09 | 38/48 (NCI-H1573, SHP-77, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~76% of this change | **0.490×** | -6.5 | 1e-08 | 33/48 (PANC-1, A-172, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.542×** | -6.4 | 2e-08 | 36/48 (A498, LS 180, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.565×** | -6.0 | 2e-07 | 30/48 (A498, J82, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.668×** | -5.9 | 2e-07 | 26/48 (A-427, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **0.574×** | -5.8 | 4e-07 | 37/48 (SHP-77, NCI-H1573, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.604×** | -5.2 | 9e-06 | 27/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.631×** | -4.8 | 9e-05 | 26/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Amsacrine (drug)]] 5 µM |  | **0.728×** | -4.7 | 1e-04 | 28/48 (SW48, LoVo, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **0.649×** | -4.5 | 3e-04 | 25/48 (LOX-IMVI, SW48, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~78% of this change | **0.443×** | -4.4 | 4e-04 | 27/43 (SHP-77, SW48, …) | all doses, flat | noisy plate (z scaled) |
| [[Cytarabine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~95% of this change | **0.670×** | -4.2 | 0.001 | 26/48 (PANC-1, SHP-77, …) | all doses, stronger at high dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **0.651×** | -4.1 | 0.001 | 25/48 (NCI-H1573, SHP-77, …) | all doses, flat |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **0.756×** | -4.1 | 0.001 | 27/48 (Hs 766T, CFPAC-1, …) | rises with dose | position effect removed |
| [[PF-06260933 (drug)]] 5 µM |  | **0.486×** | -3.9 | 0.002 | 24/48 (A549, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Gemcitabine (drug)]] 0.05 µM |  | **0.739×** | -3.9 | 0.003 | 23/48 (SW480, HEC-1-A, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **0.733×** | -3.2 | 0.029 | 17/48 (SK-MEL-2, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.723×** | -3.1 | 0.042 | 20/47 (COLO 205, SNU-423, …) | all doses, flat |  |
| [[EX229 (drug)]] 5 µM |  | **0.579×** | -3.0 | 0.064 | 19/48 (SK-MEL-2, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Gallic acid (drug)]] 5 µM |  | **0.824×** | -2.8 | 0.094 | 11/48 (NCI-H661, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Cytarabine (drug)]] 0.05 µM |  | **0.747×** | -2.8 | 0.099 | 15/48 (NCI-H1573, SW 1088, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.44 per unit of S-phase module lfc, +1.52 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1023. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 67.1 | 4 (4 ⚠) | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.11× (z +20.7) ⚠ cell-cycle shift, explains ~65% of this change | [[Digitoxin (drug)]] 5 µM 0.215× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.252× (z -11.1) |
| [[A498 (line)]] | wt | 48.7 | 3 (3 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +11.0) ⚠ cell-cycle shift, explains ~65% of this change | [[Selinexor (drug)]] 5 µM 0.355× (z -11.0) ⚠ cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 35.5 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.6× (z +18.0) ⚠ cell-cycle shift, explains ~65% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 5.92× (z +9.2) | — |
| [[LoVo (line)]] | wt | 59.5 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.87× (z +22.8) ⚠ cell-cycle shift, explains ~65% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +9.2) | — |
| [[SW480 (line)]] | alt | 81.9 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.76× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | [[Digitoxin (drug)]] 5 µM 0.227× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.248× (z -9.8) |
| [[HOP62 (line)]] | alt | 52.7 | 3 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.67× (z +19.7) ⚠ cell-cycle shift, explains ~65% of this change | [[Digitoxin (drug)]] 5 µM 0.271× (z -8.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 37.4 | 3 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.08× (z +16.3) ⚠ cell-cycle shift, explains ~65% of this change | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.173× (z -9.7) ⚠ cell-cycle shift, explains ~91% of this change |
| [[NCI-H2347 (line)]] | alt | 37.3 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.32× (z +17.8) ⚠ cell-cycle shift, explains ~65% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 4.45× (z +8.8) | — |
| [[NCI-H460 (line)]] | wt | 40.2 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.22× (z +15.0) ⚠ cell-cycle shift, explains ~65% of this change | — |
| [[RKO (line)]] | wt | 16.3 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 20.2× (z +20.5) ⚠ cell-cycle shift, explains ~65% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.64× (z +11.8) | — |
| [[SW1417 (line)]] | alt | 54.4 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.96× (z +14.8) ⚠ cell-cycle shift, explains ~65% of this change | — |
| [[A-172 (line)]] | wt | 40.2 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.85× (z +12.9) ⚠ cell-cycle shift, explains ~65% of this change | — |
| [[A-427 (line)]] | wt | 106 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 4.72× (z +12.0) ⚠ cell-cycle shift, explains ~49% of this change | [[Selinexor (drug)]] 5 µM 0.366× (z -11.0) ⚠ cell-cycle shift, would explain all of this change |
| [[Hs 766T (line)]] | wt | 55.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.35× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[HS-578T (line)]] | alt | 47.8 | 2 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 8.24× (z +17.1) ⚠ cell-cycle shift, explains ~65% of this change | [[Digitoxin (drug)]] 0.5 µM 0.182× (z -9.7) |
| [[NCI-H2030 (line)]] | alt | 43.4 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 14.0× (z +22.4) ⚠ cell-cycle shift, explains ~65% of this change | [[Digitoxin (drug)]] 5 µM 0.215× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 63.9 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +9.4) ⚠ cell-cycle shift, explains ~65% of this change | — |
| [[Panc 03.27 (line)]] | alt | 38.7 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.02× (z +15.5) ⚠ cell-cycle shift, explains ~65% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.27× (z +9.4) | — |
| [[AsPC-1 (line)]] | alt | 13.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.0× (z +14.2) ⚠ cell-cycle shift, explains ~65% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.05× (z +10.0) | — |
| [[CFPAC-1 (line)]] | alt | 29.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.22× (z +15.7) ⚠ cell-cycle shift, explains ~65% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.61× (z +10.2) | — |
| [[CHP-212 (line)]] | wt | 26.1 | 0 | 2 | — | [[Pentagastrin (drug)]] 0.05 µM 0.0573× (z -9.4) |
| [[HepG2_C3A (line)]] | wt | 15.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.99× (z +11.1) ⚠ cell-cycle shift, explains ~65% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.04× (z +9.2) | — |
| [[HT-29 (line)]] | alt | 43.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Docetaxel (drug)]] 0.05 µM 4.70× (z +8.5) ⚠ transcription drop; cell-cycle shift, explains ~88% of this change | [[Digitoxin (drug)]] 5 µM 0.174× (z -9.6) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 33.1 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.04× (z +14.1) ⚠ cell-cycle shift, explains ~65% of this change | — |
| [[J82 (line)]] | alt | 46.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.59× (z +13.9) ⚠ cell-cycle shift, explains ~65% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +8.8) | — |
| [[A549 (line)]] | wt | 47.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.15× (z +15.4) ⚠ cell-cycle shift, explains ~65% of this change | — |
| [[BT-474 (line)]] | alt | 23.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +10.6) ⚠ cell-cycle shift, explains ~65% of this change | — |
| [[C-33 A (line)]] | alt | 32.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.59× (z +11.4) ⚠ cell-cycle shift, explains ~65% of this change | — |
| [[HCT15 (line)]] | alt | 48.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.19× (z +11.1) ⚠ cell-cycle shift, explains ~65% of this change | — |
| [[HEC-1-A (line)]] | alt | 83.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +10.4) ⚠ cell-cycle shift, explains ~65% of this change | — |
| [[KATO III (line)]] | alt | 48.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +11.7) ⚠ cell-cycle shift, explains ~65% of this change | — |
| [[LS 180 (line)]] | wt | 40.0 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.237× (z -9.8) ⚠ cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 83.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.93× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H1573 (line)]] | alt | 26.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +9.2) ⚠ cell-cycle shift, explains ~65% of this change | — |
| [[NCI-H1792 (line)]] | alt | 13.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.8× (z +13.7) ⚠ cell-cycle shift, explains ~65% of this change | — |
| [[RPMI-7951 (line)]] | alt | 35.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.46× (z +12.9) ⚠ cell-cycle shift, explains ~65% of this change | — |
| [[SHP-77 (line)]] | alt | 77.5 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0564× (z -9.8) ⚠ toxic; cell-cycle shift, explains ~78% of this change |
| [[SK-MEL-2 (line)]] | alt | 134 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +9.7) ⚠ cell-cycle shift, explains ~65% of this change | — |
| [[SNU-423 (line)]] | alt | 63.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.44× (z +12.9) ⚠ cell-cycle shift, explains ~65% of this change | — |
| [[SW 900 (line)]] | alt | 42.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.09× (z +12.2) ⚠ cell-cycle shift, explains ~65% of this change | — |
| [[AN3 CA (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 36.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 50.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 64.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 43.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1023), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DEPDC1]] | +0.90 | +0.87 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 907 |
| [[ASPM]] | +0.88 | +0.83 / +0.92 | both halves | 7e-06 | STRING 928 |
| [[SPDL1]] | +0.84 | +0.87 / +0.81 | both halves | 7e-06 | STRING 555 |
| [[AURKA]] | +0.84 | +0.81 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 970 |
| [[CCNB2]] | +0.84 | +0.77 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 888 |
| [[KNSTRN]] | +0.82 | +0.75 / +0.86 | both halves | 7e-06 | STRING 403 |
| [[CENPF]] | +0.82 | +0.75 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 927 |
| [[PLK1]] | +0.82 | +0.74 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 683 |
| [[CENPE]] | +0.82 | +0.77 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 926 |
| [[CCNB1]] | +0.81 | +0.70 / +0.87 | both halves | 7e-06 | pathway: G2/M Transition; STRING 942 |
| [[TPX2]] | +0.80 | +0.69 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 979 |
| [[CDKN3]] | +0.79 | +0.79 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 833 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NDC80]] | C | NDC80 activity raises HMMR's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 2.34× lower at baseline in the lines without NDC80 | 0.047 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent |
| [[CDC20]] | C | CDC20 activity raises HMMR's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 2.70× lower at baseline in the lines without CDC20 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.779). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-38.9, -56.8); signed map (-50.9, -44.5). **Vector** length 148, 57.4% of its response variance represented; |z| ≥ 3 in 1,511 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Mitotic Prometaphase* (reactome, mean cos +0.60 to 48); *Mitotic Metaphase and Anaphase* (reactome, mean cos +0.60 to 41); *Mitotic Anaphase* (reactome, mean cos +0.60 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | +13.6 | +23.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | +9.9 | +12.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +9.8 | +11.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +6.9 | +7.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~88% of this change | +5.5 | +7.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.8 | +6.4 |
|  | [[Docetaxel (drug)]] 5 µM |  | +4.0 | +4.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.7 | +4.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.1 | +3.6 |
|  | [[Peretinoin (drug)]] 0.05 µM |  | +3.1 | +3.9 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | -7.6 | -6.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -7.5 | -2.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~97% of this change | -6.4 | -4.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~76% of this change | -6.0 | -6.5 |
|  | [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | -6.0 | -6.6 |
|  | [[Amsacrine (drug)]] 5 µM |  | -5.0 | -4.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -4.2 | -3.1 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | -3.9 | -4.1 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | -3.7 | -3.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.7 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | hyaluronan mediated motility receptor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q34 — chr5:163,460,203-163,491,941 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RHAMM, CD168 |
| Gene groups (HGNC) | CD molecules |
| Hallmark sets | GLYCOLYSIS, G2M_CHECKPOINT, E2F_TARGETS |
| Reactome | 9 pathways, smallest: Hyaluronan degradation; Hyaluronan metabolism; AURKA Activation by TPX2 |
| Matched by | ensembl_id |

**Function**, from UniProt [O75330](https://www.uniprot.org/uniprotkb/O75330) (Hyaluronan mediated motility receptor):

> Receptor for hyaluronic acid (HA) (By similarity). Involved in cell motility (By similarity). When hyaluronan binds to HMMR, the phosphorylation of a number of proteins, including PTK2/FAK1 occurs. May also be involved in cellular transformation and metastasis formation, and in regulating extracellular-regulated kinase (ERK) activity. May act as a regulator of adipogenisis (By similarity).

**Summary**, from NCBI Gene [3161](https://www.ncbi.nlm.nih.gov/gene/3161):

> The protein encoded by this gene is involved in cell motility. It is expressed in breast tissue and together with other proteins, it forms a complex with BRCA1 and BRCA2, thus is potentially associated with higher risk of breast cancer. Alternatively spliced transcript variants encoding different isoforms have been noted for this gene. [provided by RefSeq, Dec 2008]

**Accessions** — [HGNC:5012](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5012) · Entrez [3161](https://www.ncbi.nlm.nih.gov/gene/3161) · UniProt [O75330](https://www.uniprot.org/uniprotkb/O75330) · Ensembl [ENSG00000072571](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000072571)

## Data

Gene col 1023: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1023); `tables/drug_effects.parquet` (65 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1023, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1023]; `tensor/DDL_lfc|DDL_z.npy` [1023]; `embed/gene_vectors.npy` [1023]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1023 or target_col == 1023). Every well: [[HMMR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HMMR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
