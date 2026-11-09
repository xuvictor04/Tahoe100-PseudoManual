---
symbol: "MAP2K4"
type: "gene"
col: 794
ensembl_id: "ENSG00000065559"
name: "mitogen-activated protein kinase kinase 4"
location: "17p12"
module: 24
arm: "+"
pooled_cpm: 155.49
n_lines_expressing: 49
n_dd_up: 13
n_dd_down: 10
n_dd_up_clean: 11
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# MAP2K4

*mitogen-activated protein kinase kinase 4* — 17p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.54× (z +10.1, q 2e-21, up in 44 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.344× (z -25.0, q 0e+00, down in 47 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.601× (z -11.9, q 1e-30, down in 39 of 47 measured lines).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NDUFC1]] (+0.62, fdr 3e-05), [[ATAD2B]] (+0.60, fdr 7e-05), [[NDUFA6]] (+0.57, fdr 2e-04); moves opposite to [[HEMK1]] (-0.51, fdr 1e-04), [[TMC3-AS1]] (-0.47, fdr 8e-05), [[ZNF512]] (-0.46, fdr 0.001, ⚠ one half only (not replicated)), [[PPP1R15B]] (-0.46, fdr 4e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 794.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.54×** | +10.1 | 2e-21 | 44/47 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.34×** | +9.8 | 4e-20 | 29/47 (NCI-H23, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.02×** | +8.5 | 3e-15 | 35/48 (A498, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.89×** | +7.7 | 1e-12 | 37/47 (SW480, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.38×** | +7.5 | 9e-12 | 35/47 (NCI-H1573, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.37×** | +7.4 | 1e-11 | 36/47 (KATO III, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.39×** | +7.3 | 3e-11 | 39/47 (KATO III, HT-29, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +7.2 | 4e-11 | 26/48 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.34×** | +6.8 | 5e-10 | 32/47 (NCI-H1573, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.32×** | +6.5 | 4e-09 | 31/47 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.30×** | +5.8 | 3e-07 | 25/47 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.53×** | +5.1 | 1e-05 | 29/44 (HT-29, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.29×** | +4.1 | 0.002 | 24/48 (HT-29, COLO 205, …) | all doses, flat | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.18× | +3.8 | 0.006 | 18/47 (KATO III, COLO 205, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.5 | 0.018 | 14/47 (NCI-H23, BT-474, …) | all doses, stronger at high dose |  |
| [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | 1.14× | +3.0 | 0.088 | 9/47 (MIA PaCa-2, A-172, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 8 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 794.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.344×** | -25.0 | 0e+00 | 47/48 (A-427, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.357×** | -23.2 | 0e+00 | 43/43 (SHP-77, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.404×** | -19.6 | 0e+00 | 42/44 (A-427, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.601×** | -11.9 | 1e-30 | 39/47 (A-427, SNU-423, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.736×** | -7.2 | 7e-11 | 32/47 (A549, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.748×** | -6.8 | 8e-10 | 37/47 (KATO III, A549, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.818×** | -4.7 | 2e-04 | 25/47 (SHP-77, HOP62, …) | all doses, stronger at high dose |  |
| [[Infigratinib (drug)]] 0.05 µM |  | 0.857× | -3.4 | 0.042 | 12/47 (A498, C-33 A, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.813×** | -3.4 | 0.048 | 18/47 (HepG2/C3A, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **0.764×** | -3.3 | 0.059 | 21/44 (RKO, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.907× | -3.2 | 0.060 | 6/47 (SHP-77, MIA PaCa-2, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | 0.870× | -3.2 | 0.072 | 20/46 (NCI-H2347, NCI-H2030, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | 0.879× | -3.1 | 0.092 | 16/47 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.829×** | -3.1 | 0.092 | 19/47 (BT-474, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 794. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 166 | 6 (1 ⚠) | 4 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +17.5) | [[Dinaciclib (drug)]] 5 µM 0.134× (z -28.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.507× (z -10.0) |
| [[NCI-H1573 (line)]] | alt | 189 | 7 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.98× (z +15.9) | [[Dinaciclib (drug)]] 0.5 µM 0.304× (z -17.3) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 122 | 6 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.31× (z +13.1) | [[Dinaciclib (drug)]] 5 µM 0.373× (z -14.8) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 292 | 3 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +15.5) | [[Dinaciclib (drug)]] 5 µM 0.121× (z -32.3) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 185 | 4 (1 ⚠) | 3 (3 ⚠) | [[Digitoxin (drug)]] 5 µM 2.33× (z +10.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.25× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.374× (z -12.0) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 252 | 3 | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.23× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.169× (z -24.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.476× (z -10.7) |
| [[HT-29 (line)]] | alt | 88.1 | 4 (1 ⚠) | 3 (2 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.33× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.386× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.468× (z -10.4) |
| [[KATO III (line)]] | alt | 184 | 3 | 4 (4 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.12× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.180× (z -24.6) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 209 | 3 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.63× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -22.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.544× (z -9.3) |
| [[A-172 (line)]] | wt | 185 | 1 | 5 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 3.25× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.288× (z -18.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.525× (z -9.5) |
| [[A498 (line)]] | wt | 173 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +15.4) | [[Dinaciclib (drug)]] 5 µM 0.312× (z -17.2) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 175 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +16.1) | [[Dinaciclib (drug)]] 0.5 µM 0.321× (z -15.4) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 87.3 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +15.5) | [[Dinaciclib (drug)]] 0.5 µM 0.428× (z -13.6) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 199 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.210× (z -18.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.385× (z -11.5) |
| [[LoVo (line)]] | wt | 212 | 2 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.34× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.322× (z -16.2) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 244 | 1 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.175× (z -22.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.403× (z -11.9) |
| [[A-427 (line)]] | wt | 132 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0744× (z -34.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.430× (z -12.1) |
| [[H4 (line)]] | wt | 107 | 2 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.73× (z +9.6) | [[Dinaciclib (drug)]] 0.05 µM 0.223× (z -13.3) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 226 | 2 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.21× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.0914× (z -26.4) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 149 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.12× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.291× (z -19.0) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 152 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.373× (z -13.2) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 156 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +14.1) | [[Dinaciclib (drug)]] 0.05 µM 0.291× (z -14.9) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 205 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.83× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.0421× (z -45.4) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 146 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.260× (z -18.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.428× (z -11.9) |
| [[SW1417 (line)]] | alt | 153 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.261× (z -18.6) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 237 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 3.61× (z +12.7) | [[Dinaciclib (drug)]] 0.5 µM 0.184× (z -17.8) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 183 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.335× (z -13.2) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 120 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.0682× (z -29.1) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 109 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.285× (z -17.4) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 135 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.323× (z -14.9) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 247 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.192× (z -20.1) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 88.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.387× (z -12.3) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 128 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.291× (z -16.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 193 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.257× (z -17.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.502× (z -8.7) |
| [[AN3 CA (line)]] | alt | 228 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.211× (z -13.0) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 71.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +14.3) | — |
| [[CHP-212 (line)]] | wt | 179 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.169× (z -13.0) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 240 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.352× (z -13.6) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 130 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.331× (z -12.8) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 88.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.365× (z -10.4) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 90.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.435× (z -9.1) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 72.9 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.417× (z -8.9) |
| [[SNU-1 (line)]] | wt | 167 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.378× (z -11.4) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 179 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.213× (z -9.6) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 12.8 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 90.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 174 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 175 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 126 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 794), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 11 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFC1]] | +0.62 | +0.46 / +0.52 | both halves | 3e-05 |  |
| [[ATAD2B]] | +0.60 | +0.38 / +0.63 | both halves | 7e-05 |  |
| [[NDUFA6]] | +0.57 | +0.30 / +0.52 | both halves | 2e-04 |  |
| [[STRN3]] | +0.57 | +0.45 / +0.55 | both halves | 3e-05 | same gene group |
| [[DHX32]] | +0.55 | +0.46 / +0.47 | both halves | 3e-05 |  |
| [[SOS1]] | +0.55 | +0.44 / +0.44 | both halves | 3e-05 | pathway: FCERI mediated MAPK activation |
| [[MED13]] | +0.53 | +0.28 / +0.50 | both halves | 3e-04 |  |
| [[ENDOG]] | +0.52 | +0.19 / +0.43 | ⚠ not reproduced | 8e-04 |  |
| [[GNAQ]] | +0.52 | +0.43 / +0.50 | both halves | 3e-05 |  |
| [[SMIM27]] | +0.52 | +0.31 / +0.42 | both halves | 2e-04 |  |
| [[FRS2]] | +0.52 | +0.44 / +0.39 | both halves | 6e-05 |  |
| [[HECTD4]] | +0.52 | +0.53 / +0.58 | both halves | 1e-05 | same gene group |
| [[SNX13]] | +0.51 | +0.46 / +0.47 | both halves | 3e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HEMK1]] | -0.51 | -0.36 / -0.44 | both halves | 1e-04 |  |
| [[TMC3-AS1]] | -0.47 | -0.37 / -0.43 | both halves | 8e-05 |  |
| [[ZNF512]] | -0.46 | -0.18 / -0.52 | ⚠ one half (not replicated) | 0.001 |  |
| [[PPP1R15B]] | -0.46 | -0.43 / -0.45 | both halves | 4e-05 |  |
| [[ZNF529]] | -0.45 | -0.36 / -0.44 | both halves | 9e-05 |  |
| [[APBB3]] | -0.45 | -0.24 / -0.49 | both halves | 4e-04 | same gene group |
| [[LINC01237]] | -0.45 | -0.37 / -0.35 | both halves | 1e-04 |  |
| [[EXOC3]] | -0.44 | -0.16 / -0.46 | ⚠ not reproduced | 0.001 |  |
| [[MAT2A]] | -0.44 | -0.27 / -0.43 | both halves | 3e-04 |  |
| [[AMDHD2]] | -0.44 | -0.29 / -0.43 | both halves | 2e-04 |  |
| [[PDE4DIP]] | -0.44 | -0.35 / -0.37 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.289). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-6.2, 14.7); signed map (-2.4, 1.8). **Vector** length 88.2, 26.6% of its response variance represented; |z| ≥ 3 in 1,194 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.0 | +7.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.8 | +3.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.7 | +1.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.0 | +7.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.4 | +7.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.0 | +3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +0.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.8 | +4.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.4 | -0.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.4 | +2.6 |
| fall | [[Auranofin (drug)]] 5 µM |  | -8.2 | -11.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.4 | -19.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -3.4 | -4.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.3 | -7.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.3 | -3.2 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -1.8 | +0.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.4 | -1.2 |
|  | [[Baicalin (drug)]] 5 µM |  | -1.3 | +1.4 |

## What is on record

|  |  |
|---|---|
| Name | mitogen-activated protein kinase kinase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p12 — chr17:12,020,829-12,143,830 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MEK4, JNKK1, PRKMK4, MKK4, MAPKK4, SAPKK1, SKK1, JNKK; previously SERK1 |
| Gene groups (HGNC) | Mitogen-activated protein kinase kinases; MicroRNA protein coding host genes |
| Reactome | 34 pathways, smallest: Uptake and function of anthrax toxins; MAP3K8 (TPL2)-dependent MAPK1/3 activation; JNK (c-Jun kinases) phosphorylation and  activation mediated by activated human TAK1 |
| Matched by | ensembl_id |

**Function**, from UniProt [P45985](https://www.uniprot.org/uniprotkb/P45985) (Dual specificity mitogen-activated protein kinase kinase 4):

> Dual specificity protein kinase which acts as an essential component of the MAP kinase signal transduction pathway. Essential component of the stress-activated protein kinase/c-Jun N-terminal kinase (SAP/JNK) signaling pathway. With MAP2K7/MKK7, is the one of the only known kinase to directly activate the stress-activated protein kinase/c-Jun N-terminal kinases MAPK8/JNK1, MAPK9/JNK2 and MAPK10/JNK3. MAP2K4/MKK4 and MAP2K7/MKK7 both activate the JNKs by phosphorylation, but they differ in their …

**Summary**, from NCBI Gene [6416](https://www.ncbi.nlm.nih.gov/gene/6416):

> This gene encodes a member of the mitogen-activated protein kinase (MAPK) family. Members of this family act as an integration point for multiple biochemical signals and are involved in a wide variety of cellular processes such as proliferation, differentiation, transcription regulation, and development. They form a three-tiered signaling module composed of MAPKKKs, MAPKKs, and MAPKs. This protein is phosphorylated at serine and threonine residues by MAPKKKs and subsequently phosphorylates …

**Accessions** — [HGNC:6844](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6844) · Entrez [6416](https://www.ncbi.nlm.nih.gov/gene/6416) · UniProt [P45985](https://www.uniprot.org/uniprotkb/P45985) · Ensembl [ENSG00000065559](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000065559)

## Data

Gene col 794: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 794); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 794, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 794]; `tensor/DDL_lfc|DDL_z.npy` [794]; `embed/gene_vectors.npy` [794]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 794 or target_col == 794). Every well: [[MAP2K4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAP2K4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
