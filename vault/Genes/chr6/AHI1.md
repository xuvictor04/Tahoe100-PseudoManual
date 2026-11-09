---
symbol: "AHI1"
type: "gene"
col: 5723
ensembl_id: "ENSG00000135541"
name: "Abelson helper integration site 1"
location: "6q23.3"
module: 50
arm: "+"
pooled_cpm: 169.72
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 11
n_dd_up_clean: 9
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# AHI1

*Abelson helper integration site 1* — 6q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.14× (z +26.4, q 0e+00, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.428× (z -10.9, q 1e-24, down in 44 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BRAF]] (+0.56, fdr 3e-05), [[CHD2]] (+0.54, fdr 5e-05), [[GOLGA4]] (+0.54, fdr 3e-05); moves opposite to [[RNF4]] (-0.57, fdr 1e-05), [[RNPS1]] (-0.54, fdr 3e-05), [[GRB2]] (-0.53, fdr 2e-04).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5723.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.14×** | +26.4 | 0e+00 | 43/48 (SK-MEL-2, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.78×** | +14.2 | 3e-43 | 41/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.66×** | +12.0 | 6e-31 | 38/48 (NCI-H1573, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.40×** | +8.2 | 3e-14 | 34/48 (BT-474, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.30×** | +6.4 | 2e-08 | 30/48 (BT-474, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 1.20× | +6.3 | 3e-08 | 25/48 (SW1417, J82, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.27×** | +6.0 | 2e-07 | 27/48 (BT-474, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.26×** | +5.7 | 8e-07 | 32/49 (A-172, PANC-1, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.26×** | +5.6 | 1e-06 | 28/48 (BT-474, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.21×** | +4.7 | 1e-04 | 21/48 (SNU-423, C32, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.21×** | +4.6 | 2e-04 | 22/48 (SK-MEL-2, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +4.5 | 4e-04 | 23/48 (C32, SK-MEL-2, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.7 | 0.008 | 19/48 (SNU-1, BT-474, …) | all doses, stronger at high dose |  |
| [[Gefitinib (drug)]] 5 µM |  | 1.16× | +3.7 | 0.010 | 18/48 (C-33 A, HOP62, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.15× | +3.5 | 0.020 | 11/48 (SNU-423, HT-29, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.12× | +3.4 | 0.020 | 11/49 (HEC-1-A, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.31×** | +3.4 | 0.020 | 16/49 (BT-474, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.10× | +3.3 | 0.032 | 6/49 (NCI-H1573, HEC-1-A, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.13× | +3.1 | 0.054 | 6/48 (NCI-H23, MIA PaCa-2, …) | two highest doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.14× | +3.1 | 0.054 | 14/47 (NCI-H23, HEC-1-A, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5723.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.428×** | -10.9 | 1e-24 | 44/49 (RKO, A549, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.521×** | -8.4 | 2e-14 | 41/48 (KATO III, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.741×** | -7.3 | 4e-11 | 33/48 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~22% of this change | **0.745×** | -7.2 | 9e-11 | 33/48 (SW 900, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.621×** | -6.1 | 1e-07 | 25/38 (BT-474, SW 900, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change | **0.805×** | -5.3 | 1e-05 | 23/49 (HCT15, A498, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.805×** | -5.3 | 1e-05 | 24/48 (KATO III, COLO 205, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.796×** | -5.3 | 1e-05 | 28/48 (HT-29, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.859× | -5.2 | 1e-05 | 21/49 (A549, SNU-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change | **0.814×** | -4.8 | 8e-05 | 22/44 (SNU-1, HCT15, …) | rises with dose | composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.697×** | -4.6 | 2e-04 | 27/45 (MIA PaCa-2, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.822×** | -4.6 | 2e-04 | 24/47 (COLO 205, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Infigratinib (drug)]] 0.05 µM |  | 0.864× | -3.4 | 0.033 | 18/48 (HEC-1-A, SW 900, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.873× | -3.3 | 0.037 | 17/48 (NCI-H1573, NCI-H460, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5723. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 372 | 6 (1 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +20.0) | [[Dinaciclib (drug)]] 5 µM 0.130× (z -26.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.645× (z -8.5) |
| [[A-172 (line)]] | wt | 112 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +18.5) | — |
| [[BT-474 (line)]] | alt | 176 | 7 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +18.1) | [[Lonafarnib (drug)]] 5 µM 0.213× (z -10.6) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 135 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +24.5) | — |
| [[RKO (line)]] | wt | 278 | 2 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +12.8) | [[Dinaciclib (drug)]] 0.05 µM 0.231× (z -21.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.155× (z -15.7) |
| [[A498 (line)]] | wt | 169 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.482× (z -14.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.653× (z -8.5) |
| [[C32 (line)]] | wt | 109 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.58× (z +17.0) | — |
| [[COLO 205 (line)]] | alt | 1,087 | 3 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +26.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.404× (z -12.8) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 0.316× (z -8.9) |
| [[HOP62 (line)]] | alt | 175 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +14.2) | — |
| [[NCI-H460 (line)]] | wt | 153 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +20.7) | — |
| [[SK-MEL-2 (line)]] | alt | 96.8 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.84× (z +27.0) | — |
| [[SW480 (line)]] | alt | 177 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +18.5) | [[Digitoxin (drug)]] 0.05 µM 0.570× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 183 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +15.0) | [[Dinaciclib (drug)]] 0.05 µM 0.445× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.515× (z -9.5) |
| [[SW 900 (line)]] | alt | 327 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.310× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.297× (z -8.5) |
| [[A549 (line)]] | wt | 181 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -17.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.287× (z -10.7) |
| [[AsPC-1 (line)]] | alt | 103 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +20.7) | — |
| [[KATO III (line)]] | alt | 147 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +11.3) | [[PH-797804 (drug)]] 5 µM 0.297× (z -8.5) |
| [[LoVo (line)]] | wt | 176 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +13.5) | [[TAK-901 (drug)]] 5 µM 0.261× (z -9.6) |
| [[LS 180 (line)]] | wt | 209 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +17.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.473× (z -8.9) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 214 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +17.2) | [[Bortezomib (drug)]] 5 µM 0.196× (z -10.7) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 114 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +15.1) | [[Ixazomib citrate (drug)]] 5 µM 0.498× (z -10.8) |
| [[A-427 (line)]] | wt | 170 | 1 | 1 | [[Homoharringtonine (drug)]] 0.5 µM 1.78× (z +9.3) | [[TAK-901 (drug)]] 5 µM 0.319× (z -9.6) |
| [[C-33 A (line)]] | alt | 301 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 1.87× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.489× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change |
| [[H4 (line)]] | wt | 143 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +11.1) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -10.7) ⚠ cell-cycle shift, explains ~7% of this change |
| [[HCT15 (line)]] | alt | 197 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.128× (z -22.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change |
| [[HEC-1-A (line)]] | alt | 207 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.54× (z +9.6) | — |
| [[HepG2_C3A (line)]] | wt | 148 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +14.8) | — |
| [[HT-29 (line)]] | alt | 166 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +19.0) | [[Docetaxel (drug)]] 0.05 µM 0.514× (z -8.6) ⚠ transcription drop; cell-cycle shift, explains ~22% of this change |
| [[hTERT-HPNE (line)]] | wt | 207 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.53× (z +8.7) | — |
| [[LOX-IMVI (line)]] | wt | 109 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +16.1) | — |
| [[NCI-H2347 (line)]] | alt | 55.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +14.9) | — |
| [[SW1417 (line)]] | alt | 62.9 | 2 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.00× (z +10.2) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.93× (z +9.6) | — |
| [[SW48 (line)]] | wt | 165 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +14.5) | — |
| [[AN3 CA (line)]] | alt | 211 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.324× (z -9.3) ⚠ cell-cycle shift, explains ~24% of this change |
| [[CFPAC-1 (line)]] | alt | 76.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +12.8) | — |
| [[CHP-212 (line)]] | wt | 167 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0736× (z -20.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change |
| [[Hs 766T (line)]] | wt | 93.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +15.9) | — |
| [[J82 (line)]] | alt | 141 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +14.3) | — |
| [[NCI-H2030 (line)]] | alt | 113 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +15.7) | — |
| [[Panc 03.27 (line)]] | alt | 91.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +11.3) | — |
| [[RPMI-7951 (line)]] | alt | 183 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +16.5) | — |
| [[SHP-77 (line)]] | alt | 199 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.624× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 212 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 196 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 169 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 191 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 213 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 175 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5723), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*46 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BRAF]] | +0.56 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[CHD2]] | +0.54 | +0.52 / +0.40 | both halves | 5e-05 |  |
| [[GOLGA4]] | +0.54 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[XIAP]] | +0.53 | +0.53 / +0.32 | both halves | 2e-04 |  |
| [[APRG1]] | +0.53 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[REL]] | +0.53 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[NFKBIB]] | +0.52 | +0.59 / +0.36 | both halves | 1e-04 |  |
| [[ANKRD20A5P]] | +0.51 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[FNIP1]] | +0.51 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[AKAP9]] | +0.51 | +0.51 / +0.47 | both halves | 2e-05 | pathway: Anchoring of the basal body to the plasma membrane |
| [[DDX43]] | +0.51 | +0.44 / +0.37 | both halves | 8e-05 |  |
| [[ABCA5]] | +0.49 | +0.50 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*54 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF4]] | -0.57 | -0.63 / -0.49 | both halves | 1e-05 |  |
| [[RNPS1]] | -0.54 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[GRB2]] | -0.53 | -0.62 / -0.32 | both halves | 2e-04 | same gene group |
| [[CDC42BPB]] | -0.52 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[BLTP2]] | -0.52 | -0.64 / -0.34 | both halves | 1e-04 |  |
| [[SHANK3]] | -0.52 | -0.53 / -0.40 | both halves | 5e-05 | same gene group |
| [[ZDHHC3]] | -0.51 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[ABCC5]] | -0.51 | -0.41 / -0.39 | both halves | 5e-05 |  |
| [[BCAP31]] | -0.51 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[PSMD2]] | -0.51 | -0.54 / -0.39 | both halves | 6e-05 |  |
| [[VDAC2]] | -0.50 | -0.59 / -0.34 | both halves | 1e-04 |  |
| [[TBC1D14]] | -0.50 | -0.52 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction -0.324). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.7, -32.4); signed map (-7.2, 8.8). **Vector** length 142, 46.1% of its response variance represented; |z| ≥ 3 in 1,409 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.9 | +14.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +7.0 | +8.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.9 | +26.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +6.4 | +6.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.0 | +12.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +4.1 | +5.7 |
|  | [[Gefitinib (drug)]] 5 µM |  | +3.5 | +3.7 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +3.1 | +3.3 |
|  | [[Adagrasib (drug)]] 5 µM |  | +3.0 | +2.7 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +2.9 | +2.6 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -11.0 | -10.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -10.8 | -8.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -7.8 | -5.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -7.6 | -7.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -6.9 | -5.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.0 | -5.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.4 | -2.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -3.7 | -3.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.6 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | Abelson helper integration site 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q23.3 — chr6:135,283,407-135,498,434 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20069, ORF1, JBTS3 |
| Gene groups (HGNC) | WD repeat domain containing; SH3 domain containing |
| Reactome | 4 pathways, smallest: Anchoring of the basal body to the plasma membrane; Assembly of the 9+0 primary cilium; Cilium Assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N157](https://www.uniprot.org/uniprotkb/Q8N157) (Jouberin):

> Involved in vesicle trafficking and required for ciliogenesis, formation of primary non-motile cilium, and recruitment of RAB8A to the basal body of primary cilium. Component of the tectonic-like complex, a complex localized at the transition zone of primary cilia and acting as a barrier that prevents diffusion of transmembrane proteins between the cilia and plasma membranes. Involved in neuronal differentiation. As a positive modulator of classical Wnt signaling, may play a crucial role in …

**Summary**, from NCBI Gene [54806](https://www.ncbi.nlm.nih.gov/gene/54806):

> This gene is apparently required for both cerebellar and cortical development in humans. This gene mutations cause specific forms of Joubert syndrome-related disorders. Joubert syndrome (JS) is a recessively inherited developmental brain disorder with several identified causative chromosomal loci. Alternatively spliced transcript variants encoding different isoforms have been identified. [provided by RefSeq, Oct 2008]

**Accessions** — [HGNC:21575](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21575) · Entrez [54806](https://www.ncbi.nlm.nih.gov/gene/54806) · UniProt [Q8N157](https://www.uniprot.org/uniprotkb/Q8N157) · Ensembl [ENSG00000135541](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135541)

## Data

Gene col 5723: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5723); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5723, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5723]; `tensor/DDL_lfc|DDL_z.npy` [5723]; `embed/gene_vectors.npy` [5723]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5723 or target_col == 5723). Every well: [[AHI1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AHI1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
