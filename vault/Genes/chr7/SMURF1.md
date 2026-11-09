---
symbol: "SMURF1"
type: "gene"
col: 12663
ensembl_id: "ENSG00000198742"
name: "SMAD specific E3 ubiquitin protein ligase 1"
location: "7q22.1"
module: 160
arm: "+"
pooled_cpm: 392.31
n_lines_expressing: 49
n_dd_up: 9
n_dd_down: 24
n_dd_up_clean: 7
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/160"]
generated_by: "tahoemap"
---

# SMURF1

*SMAD specific E3 ubiquitin protein ligase 1* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.77× (z +12.3, q 5e-32, up in 42 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.493× (z -14.6, q 1e-45, down in 39 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.667× (z -12.3, q 1e-32, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LUZP1]] (+0.62, fdr 1e-05), [[CLCF1]] (+0.62, fdr 1e-05), [[BAIAP2L1]] (+0.56, fdr 1e-05); moves opposite to [[UBA5]] (-0.66, fdr 1e-05), [[SRP72]] (-0.54, fdr 3e-05), [[SH3BGR]] (-0.53, fdr 2e-05).
> It sits in the **+** arm of [[Module 160]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[BARX2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12663.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.77×** | +12.3 | 5e-32 | 42/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.72×** | +11.7 | 6e-29 | 40/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.65×** | +10.8 | 7e-25 | 43/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.48×** | +10.2 | 2e-22 | 45/48 (SW480, C32, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.58×** | +9.9 | 6e-21 | 44/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.94×** | +7.5 | 7e-12 | 39/47 (C32, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.22×** | +6.0 | 1e-07 | 23/47 (HS-578T, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.24×** | +4.5 | 5e-04 | 28/46 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.9 | 0.006 | 20/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.17× | +3.4 | 0.040 | 18/46 (SW480, LoVo, …) | rises with dose | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.17× | +3.3 | 0.048 | 17/46 (NCI-H460, LoVo, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.33×** | +3.3 | 0.053 | 23/47 (Panc 03.27, CFPAC-1, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 13 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12663.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.493×** | -14.6 | 1e-45 | 39/43 (AsPC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.522×** | -13.9 | 9e-42 | 42/48 (AsPC-1, A498, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.547×** | -13.0 | 4e-36 | 38/47 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.667×** | -12.3 | 1e-32 | 39/48 (NCI-H2347, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.580×** | -11.7 | 2e-29 | 36/47 (A498, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.594×** | -11.2 | 6e-27 | 36/47 (NCI-H2347, CFPAC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.621×** | -9.4 | 3e-19 | 35/44 (A498, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.642×** | -9.1 | 5e-18 | 40/47 (MIA PaCa-2, HOP62, …) | top dose only | cell-cycle shift (explains ~25% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.677×** | -8.0 | 6e-14 | 38/49 (MIA PaCa-2, NCI-H2347, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **0.791×** | -7.1 | 8e-11 | 33/47 (NCI-H2347, A549, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.737×** | -6.5 | 3e-09 | 28/47 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.759×** | -5.9 | 2e-07 | 37/47 (PANC-1, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.773×** | -5.5 | 2e-06 | 27/47 (A-172, SW 900, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.787×** | -5.1 | 1e-05 | 31/47 (BT-474, SNU-423, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.938× | -4.9 | 4e-05 | 1/49 (MIA PaCa-2) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 0.863× | -4.4 | 3e-04 | 13/47 (LoVo, HT-29, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.815×** | -4.2 | 8e-04 | 26/48 (NCI-H1573, A549, …) | all doses, stronger at high dose |  |
| [[Sulfatinib (drug)]] 5 µM |  | **0.815×** | -4.2 | 8e-04 | 27/48 (HEC-1-A, RPMI-7951, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.824×** | -4.1 | 9e-04 | 27/47 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.824×** | -4.1 | 9e-04 | 24/47 (RKO, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.825×** | -4.1 | 0.001 | 22/47 (NCI-H1573, AsPC-1, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.730×** | -3.5 | 0.009 | 24/47 (MIA PaCa-2, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Afatinib (drug)]] 5 µM |  | 0.871× | -3.5 | 0.011 | 12/48 (BT-474, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.892× | -3.4 | 0.012 | 18/47 (NCI-H2347, SW1417, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12663. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 666 | 0 | 17 (10 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.216× (z -24.0) |
| [[NCI-H460 (line)]] | wt | 327 | 7 (3 ⚠) | 7 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.56× (z +13.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.477× (z -14.9) |
| [[SNU-423 (line)]] | alt | 277 | 5 (1 ⚠) | 8 (6 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.23× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.371× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.531× (z -12.2) |
| [[CFPAC-1 (line)]] | alt | 531 | 0 | 12 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.186× (z -20.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.401× (z -16.1) |
| [[NCI-H1573 (line)]] | alt | 482 | 3 (1 ⚠) | 9 (5 ⚠) | [[Digitoxin (drug)]] 5 µM 2.42× (z +10.7) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 2.18× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.444× (z -13.8) |
| [[PANC-1 (line)]] | alt | 373 | 5 (1 ⚠) | 7 (6 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.27× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.304× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.514× (z -13.0) |
| [[MIA PaCa-2 (line)]] | alt | 461 | 0 | 11 (8 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.205× (z -18.8) |
| [[A498 (line)]] | wt | 404 | 1 | 9 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +14.3) | [[Dinaciclib (drug)]] 5 µM 0.275× (z -20.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.495× (z -16.4) |
| [[HOP62 (line)]] | alt | 217 | 5 (1 ⚠) | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +13.9) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.347× (z -14.2) |
| [[NCI-H1792 (line)]] | alt | 352 | 3 (1 ⚠) | 7 (5 ⚠) | [[Digitoxin (drug)]] 5 µM 2.15× (z +9.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.04× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -15.0) |
| [[SK-MEL-2 (line)]] | alt | 310 | 3 | 7 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +13.0) | [[Dinaciclib (drug)]] 5 µM 0.273× (z -18.7) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.624× (z -9.9) |
| [[A-172 (line)]] | wt | 218 | 1 | 8 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.341× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.558× (z -11.9) |
| [[AsPC-1 (line)]] | alt | 5,045 | 3 (1 ⚠) | 6 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.20× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.181× (z -23.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.441× (z -16.4) |
| [[C32 (line)]] | wt | 446 | 6 (1 ⚠) | 3 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 6.65× (z +12.9) | [[Dinaciclib (drug)]] 0.5 µM 0.386× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -9.7) |
| [[SW480 (line)]] | alt | 212 | 6 (1 ⚠) | 3 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 2.27× (z +14.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.27× (z +14.6) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.482× (z -12.5) |
| [[A549 (line)]] | wt | 311 | 0 | 8 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.434× (z -16.5) |
| [[HepG2_C3A (line)]] | wt | 284 | 3 | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +14.3) | [[Panobinostat (drug)]] 5 µM 0.359× (z -13.1) ⚠ cell-cycle shift, explains ~28% of this change |
| [[HS-578T (line)]] | alt | 243 | 1 | 7 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +18.7) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.429× (z -11.5) |
| [[Panc 03.27 (line)]] | alt | 360 | 0 | 8 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.489× (z -12.1) |
| [[SW 900 (line)]] | alt | 276 | 3 (1 ⚠) | 5 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 1.88× (z +8.7) | [[Panobinostat (drug)]] 0.5 µM 0.443× (z -11.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.501× (z -9.0) |
| [[Hs 766T (line)]] | wt | 301 | 3 (1 ⚠) | 4 (4 ⚠) | [[Digitoxin (drug)]] 5 µM 2.18× (z +10.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.17× (z +10.2) | [[Dinaciclib (drug)]] 0.05 µM 0.377× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HT-29 (line)]] | alt | 390 | 0 | 7 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.428× (z -11.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.551× (z -11.4) |
| [[RKO (line)]] | wt | 281 | 1 | 5 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.90× (z +8.8) | [[Homoharringtonine (drug)]] 0.5 µM 0.480× (z -10.0) |
| [[COLO 205 (line)]] | alt | 347 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.468× (z -12.7) |
| [[KATO III (line)]] | alt | 362 | 2 | 3 (2 ⚠) | [[Digitoxin (drug)]] 0.5 µM 2.01× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.434× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.599× (z -10.6) |
| [[LOX-IMVI (line)]] | wt | 189 | 1 | 4 | [[PH-797804 (drug)]] 5 µM 3.50× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.574× (z -11.6) |
| [[BT-474 (line)]] | alt | 234 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.349× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Osimertinib (mesylate) (drug)]] 5 µM 0.498× (z -8.5) |
| [[LS 180 (line)]] | wt | 178 | 2 (1 ⚠) | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.21× (z +9.4) | [[Homoharringtonine (drug)]] 0.5 µM 0.463× (z -9.1) |
| [[J82 (line)]] | alt | 168 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +11.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.640× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 157 | 1 (1 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 1.81× (z +8.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.381× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[hTERT-HPNE (line)]] | wt | 198 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +16.6) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -8.8) |
| [[LoVo (line)]] | wt | 235 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.557× (z -12.4) |
| [[NCI-H23 (line)]] | alt | 196 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.476× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SW1417 (line)]] | alt | 247 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.350× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[A-427 (line)]] | wt | 170 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.174× (z -22.4) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 197 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +8.7) | — |
| [[H4 (line)]] | wt | 196 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +12.9) | — |
| [[RPMI-7951 (line)]] | alt | 183 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +9.9) | — |
| [[C-33 A (line)]] | alt | 157 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 100 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 605 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 366 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 208 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 89.0 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 138 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 343 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 241 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 159 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12663), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*52 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LUZP1]] | +0.62 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[CLCF1]] | +0.62 | +0.52 / +0.71 | both halves | 1e-05 |  |
| [[BAIAP2L1]] | +0.56 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[ZSWIM4]] | +0.56 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[CAB39]] | +0.56 | +0.42 / +0.62 | both halves | 4e-05 |  |
| [[TMEM44]] | +0.55 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[ZBTB46]] | +0.55 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[TIAM1]] | +0.55 | +0.53 / +0.39 | both halves | 6e-05 |  |
| [[FBXO46]] | +0.53 | +0.58 / +0.41 | both halves | 4e-05 |  |
| [[NECTIN2]] | +0.53 | +0.66 / +0.46 | both halves | 3e-05 |  |
| [[PGBD5]] | +0.52 | +0.36 / +0.34 | both halves | 1e-04 |  |
| [[GPR153]] | +0.51 | +0.49 / +0.37 | both halves | 7e-05 |  |

## Genes that move opposite

*48 of its nearest partners move opposite, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBA5]] | -0.66 | -0.50 / -0.58 | both halves | 1e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[SRP72]] | -0.54 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[SH3BGR]] | -0.53 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[TBCK]] | -0.53 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[NFXL1]] | -0.51 | -0.38 / -0.56 | both halves | 6e-05 |  |
| [[ZNF25]] | -0.51 | -0.42 / -0.38 | both halves | 6e-05 |  |
| [[SNX27]] | -0.50 | -0.24 / -0.59 | both halves | 5e-04 |  |
| [[TUBE1]] | -0.48 | -0.39 / -0.52 | both halves | 5e-05 |  |
| [[EIF2A]] | -0.48 | -0.23 / -0.42 | both halves | 5e-04 |  |
| [[TRUB1]] | -0.48 | -0.58 / -0.36 | both halves | 9e-05 |  |
| [[FAM216A]] | -0.48 | -0.54 / -0.35 | both halves | 1e-04 |  |
| [[ACAD11]] | -0.48 | -0.54 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BARX2]] | B | BARX2 activity raises SMURF1's level | lines that do not express BARX2 (29) vs lines expressing it (21) | 1.72× lower at baseline in the lines without BARX2 | 0.057 | ⚠ within organs, on part of the lines; also absent: COL17A1, FXYD3, CEACAM6 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 160]]; 27 genes; this gene is in the **+** arm (projection on the module's main direction 0.660). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (35.8, 5.2); signed map (-3.6, 36.8). **Vector** length 98.4, 35.7% of its response variance represented; |z| ≥ 3 in 1,742 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | +4.8 | +4.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +4.4 | -11.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | +11.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +4.1 | +9.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +4.1 | +3.4 |
|  | [[Rapamycin (drug)]] 5 µM |  | +3.5 | +2.2 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | +2.5 | +2.0 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +2.4 | +0.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +0.5 |
| fall | [[Selinexor (drug)]] 5 µM |  | -5.8 | -7.1 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -3.8 | -4.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.6 | -0.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.2 | -3.3 |
|  | [[NG25 (drug)]] 5 µM |  | -3.2 | -3.1 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.9 | -0.8 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -2.6 | -4.2 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -2.6 | -2.4 |
|  | [[Terfenadine (drug)]] 5 µM |  | -2.5 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | SMAD specific E3 ubiquitin protein ligase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:99,027,440-99,144,108 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1625 |
| Gene groups (HGNC) | Nedd4 family E3 ubiquitin protein ligases |
| Hallmark sets | TGF_BETA_SIGNALING |
| Reactome | 19 pathways, smallest: TGF-beta receptor signaling in EMT (epithelial to mesenchymal transition); Downregulation of TGF-beta receptor signaling; Signaling by BMP |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HCE7](https://www.uniprot.org/uniprotkb/Q9HCE7) (E3 ubiquitin-protein ligase SMURF1):

> E3 ubiquitin-protein ligase that acts as a negative regulator of BMP signaling pathway. Mediates ubiquitination and degradation of SMAD1 and SMAD5, 2 receptor-regulated SMADs specific for the BMP pathway. Promotes ubiquitination and subsequent proteasomal degradation of TRAF family members and RHOA. Promotes ubiquitination and subsequent proteasomal degradation of MAVS. Acts as a positive regulator of smoothened signaling pathway by mediating ubiquitination of PTCH1, leading to endocytosis and …

**Summary**, from NCBI Gene [57154](https://www.ncbi.nlm.nih.gov/gene/57154):

> This gene encodes a ubiquitin ligase that is specific for receptor-regulated SMAD proteins in the bone morphogenetic protein (BMP) pathway. This protein plays a key roll in the regulation of cell motility, cell signalling, and cell polarity. Alternative splicing results in multiple transcript variants encoding different isoforms.[provided by RefSeq, Dec 2010]

**Accessions** — [HGNC:16807](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16807) · Entrez [57154](https://www.ncbi.nlm.nih.gov/gene/57154) · UniProt [Q9HCE7](https://www.uniprot.org/uniprotkb/Q9HCE7) · Ensembl [ENSG00000198742](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198742)

## Data

Gene col 12663: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12663); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12663, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12663]; `tensor/DDL_lfc|DDL_z.npy` [12663]; `embed/gene_vectors.npy` [12663]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12663 or target_col == 12663). Every well: [[SMURF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMURF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
