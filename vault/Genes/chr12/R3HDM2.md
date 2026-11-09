---
symbol: "R3HDM2"
type: "gene"
col: 11062
ensembl_id: "ENSG00000179912"
name: "R3H domain containing 2"
location: "12q13.3"
module: 88
arm: "+"
pooled_cpm: 159.94
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 30
n_dd_up_clean: 2
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/088"]
generated_by: "tahoemap"
---

# R3HDM2

*R3H domain containing 2* — 12q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.30× (z +6.9, q 3e-09, up in 28 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 13 lines (C32 4.69×, COLO 205 2.34×, NCI-H1573 2.05×, NCI-H1792 2.35×, …); [[Harringtonine (drug)]] 5 µM in 1 line (A549 2.34×; ⚠ cell-cycle shift, explains ~93% of this change); [[Cobimetinib (drug)]] 5 µM in 1 line (HepG2/C3A 2.97×).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (17 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.344× (z -19.7, q 0e+00, down in 48 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.405× (z -16.7, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OMA1]] (+0.73, fdr 7e-06), [[BPTF]] (+0.68, fdr 1e-05), [[ST7L]] (+0.68, fdr 8e-06); moves opposite to [[NTAN1]] (-0.67, fdr 7e-06), [[USP35]] (-0.66, fdr 7e-06), [[DHRS1]] (-0.63, fdr 2e-05).
> It sits in the **+** arm of [[Module 088]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MICE]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11062.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 13 lines (C32 4.69×, COLO 205 2.34×, NCI-H1573 2.05×, NCI-H1792 2.35×, …); [[Harringtonine (drug)]] 5 µM in 1 line (A549 2.34×; ⚠ cell-cycle shift, explains ~93% of this change); [[Cobimetinib (drug)]] 5 µM in 1 line (HepG2/C3A 2.97×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.30×** | +6.9 | 3e-09 | 28/48 (C32, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.25×** | +3.8 | 0.043 | 27/48 (NCI-H2347, LS 180, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 1.20× | +3.4 | 0.14 | 22/48 (AsPC-1, A498, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.18× | +3.1 | 0.18 | 19/47 (HepG2/C3A, A549, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 1.18× | +3.1 | 0.18 | 19/49 (NCI-H2347, SHP-77, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 20 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11062.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.344×** | -19.7 | 0e+00 | 48/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.405×** | -16.7 | 0e+00 | 47/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.458×** | -14.5 | 4e-45 | 47/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.477×** | -13.7 | 2e-40 | 47/48 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.501×** | -12.8 | 2e-35 | 43/48 (A-427, LoVo, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.519×** | -12.1 | 7e-32 | 45/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.521×** | -11.6 | 3e-29 | 43/47 (C-33 A, LoVo, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.575×** | -10.2 | 1e-22 | 44/48 (LoVo, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.585×** | -9.9 | 2e-21 | 45/48 (PANC-1, A-427, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.589×** | -9.8 | 8e-21 | 42/48 (NCI-H23, LoVo, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.623×** | -8.8 | 1e-16 | 42/48 (LoVo, SW480, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.412×** | -8.6 | 5e-16 | 44/49 (PANC-1, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.617×** | -8.4 | 1e-15 | 46/48 (PANC-1, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.486×** | -7.0 | 1e-10 | 40/45 (A-427, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.766×** | -7.0 | 1e-10 | 34/48 (Panc 03.27, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.538×** | -6.0 | 7e-08 | 37/48 (SW480, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.755×** | -3.7 | 0.005 | 28/49 (PANC-1, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.818×** | -3.7 | 0.005 | 23/48 (A-427, NCI-H2030, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.880× | -3.3 | 0.017 | 10/49 (CFPAC-1, A549, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.721×** | -3.2 | 0.028 | 24/48 (NCI-H23, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | 0.847× | -3.1 | 0.036 | 11/48 (LS 180, J82, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11062. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 301 | 0 | 20 (12 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.359× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.362× (z -16.5) |
| [[PANC-1 (line)]] | alt | 202 | 1 | 18 (10 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.61× (z +12.3) | [[Digitoxin (drug)]] 5 µM 0.155× (z -34.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.200× (z -29.4) |
| [[NCI-H23 (line)]] | alt | 408 | 1 | 17 (11 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +12.4) | [[Dinaciclib (drug)]] 0.05 µM 0.223× (z -19.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.397× (z -12.9) |
| [[NCI-H460 (line)]] | wt | 218 | 1 | 15 (8 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +9.8) | [[Ixazomib citrate (drug)]] 5 µM 0.264× (z -15.4) |
| [[LoVo (line)]] | wt | 259 | 0 | 14 (7 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.267× (z -20.6) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.377× (z -15.9) |
| [[SW480 (line)]] | alt | 162 | 0 | 13 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.191× (z -24.6) |
| [[NCI-H1573 (line)]] | alt | 203 | 1 | 11 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +14.1) | [[Digitoxin (drug)]] 5 µM 0.314× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.373× (z -13.8) |
| [[KATO III (line)]] | alt | 151 | 0 | 11 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.258× (z -19.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.358× (z -14.9) |
| [[HCT15 (line)]] | alt | 199 | 0 | 9 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.291× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.343× (z -12.5) |
| [[C32 (line)]] | wt | 102 | 2 (1 ⚠) | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.69× (z +21.2) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.305× (z -11.5) |
| [[COLO 205 (line)]] | alt | 195 | 1 | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +17.0) | [[Digitoxin (drug)]] 5 µM 0.249× (z -19.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.272× (z -18.5) |
| [[J82 (line)]] | alt | 120 | 0 | 8 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.240× (z -17.2) |
| [[H4 (line)]] | wt | 164 | 0 | 7 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.189× (z -16.4) |
| [[HT-29 (line)]] | alt | 146 | 0 | 7 (3 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.427× (z -11.8) |
| [[NCI-H1792 (line)]] | alt | 267 | 1 | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +12.5) | [[Digitoxin (drug)]] 5 µM 0.282× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.350× (z -10.9) |
| [[Panc 03.27 (line)]] | alt | 184 | 0 | 7 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.315× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.352× (z -11.6) |
| [[SNU-423 (line)]] | alt | 148 | 0 | 7 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.294× (z -14.1) |
| [[HOP62 (line)]] | alt | 127 | 0 | 6 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.193× (z -18.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.231× (z -16.5) |
| [[LOX-IMVI (line)]] | wt | 158 | 1 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +9.4) | [[Digitoxin (drug)]] 5 µM 0.305× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.314× (z -13.2) |
| [[RKO (line)]] | wt | 145 | 1 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +8.7) | [[Digitoxin (drug)]] 5 µM 0.373× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.441× (z -8.9) |
| [[SHP-77 (line)]] | alt | 129 | 0 | 6 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.306× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.309× (z -12.8) |
| [[SW1417 (line)]] | alt | 142 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.343× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.440× (z -10.7) |
| [[C-33 A (line)]] | alt | 208 | 0 | 5 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0794× (z -27.7) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.388× (z -10.8) |
| [[HepG2_C3A (line)]] | wt | 133 | 1 | 3 (2 ⚠) | [[Cobimetinib (drug)]] 5 µM 2.97× (z +10.0) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.360× (z -9.8) |
| [[hTERT-HPNE (line)]] | wt | 106 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.294× (z -10.6) |
| [[LS 180 (line)]] | wt | 126 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.309× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.377× (z -10.8) |
| [[MIA PaCa-2 (line)]] | alt | 149 | 0 | 4 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.311× (z -13.8) |
| [[A-172 (line)]] | wt | 132 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -12.0) ⚠ cell-cycle shift, explains ~20% of this change |
| [[AsPC-1 (line)]] | alt | 112 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +8.5) | [[Digitoxin (drug)]] 5 µM 0.436× (z -9.2) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 153 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.378× (z -11.0) |
| [[CFPAC-1 (line)]] | alt | 112 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.387× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.420× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 133 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.410× (z -12.1) |
| [[RPMI-7951 (line)]] | alt | 98.5 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.294× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.382× (z -9.3) |
| [[SK-MEL-2 (line)]] | alt | 100 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.428× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.453× (z -9.0) |
| [[SNU-1 (line)]] | wt | 149 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.292× (z -10.0) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.363× (z -8.5) |
| [[A549 (line)]] | wt | 195 | 1 (1 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.34× (z +10.3) ⚠ cell-cycle shift, explains ~93% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.485× (z -12.9) ⚠ cell-cycle shift, explains ~20% of this change |
| [[HS-578T (line)]] | alt | 91.1 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.318× (z -10.3) |
| [[NCI-H2030 (line)]] | alt | 138 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.316× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.327× (z -10.7) |
| [[SW 1271 (line)]] | alt | 163 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.136× (z -10.6) |
| [[SW 900 (line)]] | alt | 116 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.181× (z -17.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.330× (z -11.0) |
| [[A498 (line)]] | wt | 113 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.422× (z -8.8) ⚠ toxic |
| [[CHP-212 (line)]] | wt | 157 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.243× (z -8.8) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 106 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.411× (z -9.2) |
| [[SW48 (line)]] | wt | 132 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +10.1) | — |
| [[AN3 CA (line)]] | alt | 153 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 65.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 139 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11062), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OMA1]] | +0.73 | +0.75 / +0.68 | both halves | 7e-06 |  |
| [[BPTF]] | +0.68 | +0.72 / +0.55 | both halves | 1e-05 |  |
| [[ST7L]] | +0.68 | +0.75 / +0.58 | both halves | 8e-06 |  |
| [[LINC00174]] | +0.68 | +0.81 / +0.41 | both halves | 4e-05 |  |
| [[RAB30-DT]] | +0.67 | +0.79 / +0.53 | both halves | 1e-05 |  |
| [[ERCC6L2]] | +0.67 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[GABPB2]] | +0.65 | +0.72 / +0.54 | both halves | 1e-05 |  |
| [[STAC3]] | +0.65 | +0.73 / +0.44 | both halves | 3e-05 | ⚠ **readthrough risk**: STAC3 lies 2.6 kb 3′ of this gene on the same strand (can correlate by spillover, not regulation) |
| [[WARS2-AS1]] | +0.64 | +0.72 / +0.58 | both halves | 7e-06 |  |
| [[KRCC1]] | +0.64 | +0.74 / +0.47 | both halves | 2e-05 |  |
| [[NEPRO-AS1]] | +0.63 | +0.74 / +0.45 | both halves | 3e-05 |  |
| [[STYXL1]] | +0.63 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[LINC02340]] | +0.63 | +0.77 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NTAN1]] | -0.67 | -0.66 / -0.61 | both halves | 7e-06 |  |
| [[USP35]] | -0.66 | -0.68 / -0.58 | both halves | 7e-06 |  |
| [[DHRS1]] | -0.63 | -0.66 / -0.46 | both halves | 2e-05 |  |
| [[SDHAP4]] | -0.63 | -0.71 / -0.44 | both halves | 3e-05 |  |
| [[FBXO44]] | -0.63 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[SNX3]] | -0.62 | -0.66 / -0.56 | both halves | 1e-05 |  |
| [[CDS2]] | -0.62 | -0.73 / -0.44 | both halves | 3e-05 |  |
| [[RNF216P1]] | -0.60 | -0.70 / -0.44 | both halves | 3e-05 |  |
| [[ELL3]] | -0.60 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[SLC9A6]] | -0.60 | -0.69 / -0.31 | both halves | 2e-04 |  |
| [[PLCD1]] | -0.59 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[OTX1]] | -0.59 | -0.49 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MICE]] | B | MICE activity lowers R3HDM2's level | lines that do not express MICE (14) vs lines expressing it (36) | 1.34× higher at baseline in the lines without MICE | 0.039 | ⚠ within organs, on part of the lines; also absent: TRIM2, ACSL5, TNFRSF14-AS1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 088]]; 51 genes; this gene is in the **+** arm (projection on the module's main direction 0.719). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.46).
- **Nodal map** (x, y) = (2.5, -5.1); signed map (17.4, -25.1). **Vector** length 102, 38.7% of its response variance represented; |z| ≥ 3 in 1,444 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +14.0 | +6.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~93% of this change | +9.1 | -3.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +8.9 | -1.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.2 | +2.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | +3.1 | +3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +1.6 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +2.4 | +3.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.1 | +0.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.9 | +0.9 |
| fall | [[Selinexor (drug)]] 5 µM |  | -8.4 | -7.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.9 | -12.8 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -5.5 | -7.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -5.3 | -9.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -5.2 | -8.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.4 | -1.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.8 | -2.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.7 | -0.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.1 | -9.9 |

## What is on record

|  |  |
|---|---|
| Name | R3H domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.3 — chr12:57,253,762-57,431,043 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1002 |
| Matched by | ensembl_id |

UniProt [Q9Y2K5](https://www.uniprot.org/uniprotkb/Q9Y2K5) carries no function annotation.

**Summary**, from NCBI Gene [22864](https://www.ncbi.nlm.nih.gov/gene/22864):

> Enables RNA binding activity. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29167](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29167) · Entrez [22864](https://www.ncbi.nlm.nih.gov/gene/22864) · UniProt [Q9Y2K5](https://www.uniprot.org/uniprotkb/Q9Y2K5) · Ensembl [ENSG00000179912](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179912)

## Data

Gene col 11062: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11062); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11062, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11062]; `tensor/DDL_lfc|DDL_z.npy` [11062]; `embed/gene_vectors.npy` [11062]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11062 or target_col == 11062). Every well: [[R3HDM2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/R3HDM2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
