---
symbol: "RAPGEF6"
type: "gene"
col: 8208
ensembl_id: "ENSG00000158987"
name: "Rap guanine nucleotide exchange factor 6"
location: "5q31.1"
module: 171
arm: "-"
pooled_cpm: 234.26
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 7
n_dd_up_clean: 17
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/171"]
generated_by: "tahoemap"
---

# RAPGEF6

*Rap guanine nucleotide exchange factor 6* — 5q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.93× (z +24.6, q 0e+00, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.316× (z -29.4, q 0e+00, down in 43 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Radotinib (drug)]] 5 µM: 0.882× (z -4.7, q 2e-04, down in 15 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 10 lines (PANC-1 0.203×, A-427 0.172×, NCI-H23 0.165×, MIA PaCa-2 0.162×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (SK-MEL-2 0.154×, A-427 0.204×, SW480 0.323×, MIA PaCa-2 0.196×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (C-33 A 0.0344×; ⚠ toxic; transcription drop); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (CFPAC-1 0.549×); [[Homoharringtonine (drug)]] 5 µM in 1 line (HepG2/C3A 0.615×); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (CFPAC-1 0.575×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NSUN6]] (+0.58, fdr 1e-05), [[PIBF1]] (+0.55, fdr 2e-05), [[LINC01572]] (+0.54, fdr 2e-05); moves opposite to [[CIZ1]] (-0.53, fdr 2e-05), [[FHIP2A]] (-0.52, fdr 1e-05), [[SNHG22]] (-0.51, fdr 4e-05).
> It sits in the **-** arm of [[Module 171]] (Sealing of the nuclear envelope (NE) by ESCRT-III).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[EFNB2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8208.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.93×** | +24.6 | 0e+00 | 40/48 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.89×** | +14.7 | 0e+00 | 46/49 (LoVo, COLO 205, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.54×** | +11.5 | 2e-28 | 43/48 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.12×** | +10.4 | 3e-23 | 43/48 (LS 180, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.46×** | +10.1 | 8e-22 | 34/48 (COLO 205, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.44×** | +9.6 | 5e-20 | 41/48 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.38×** | +8.4 | 2e-15 | 40/48 (AsPC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.31×** | +7.2 | 4e-11 | 28/48 (RKO, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.25×** | +5.8 | 3e-07 | 28/48 (PANC-1, AsPC-1, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.24×** | +5.7 | 6e-07 | 25/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.23×** | +5.2 | 9e-06 | 25/48 (NCI-H1573, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[PF-06260933 (drug)]] 5 µM |  | **1.40×** | +4.7 | 2e-04 | 30/48 (SW480, RKO, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.22×** | +4.3 | 7e-04 | 23/47 (Panc 03.27, C32, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~10% of this change | 1.18× | +4.3 | 8e-04 | 19/48 (SW1417, RKO, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change | 1.17× | +4.1 | 0.002 | 19/48 (Hs 766T, NCI-H1573, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.30×** | +3.6 | 0.009 | 22/49 (HS-578T, RPMI-7951, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | **1.30×** | +3.6 | 0.010 | 26/49 (A-427, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | **1.29×** | +3.5 | 0.013 | 19/48 (AsPC-1, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8208.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 10 lines (PANC-1 0.203×, A-427 0.172×, NCI-H23 0.165×, MIA PaCa-2 0.162×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (SK-MEL-2 0.154×, A-427 0.204×, SW480 0.323×, MIA PaCa-2 0.196×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (C-33 A 0.0344×; ⚠ toxic; transcription drop); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (CFPAC-1 0.549×); [[Homoharringtonine (drug)]] 5 µM in 1 line (HepG2/C3A 0.615×); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (CFPAC-1 0.575×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.316×** | -29.4 | 0e+00 | 43/44 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.348×** | -28.0 | 0e+00 | 49/49 (SK-MEL-2, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.421×** | -21.2 | 0e+00 | 44/45 (C-33 A, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.746×** | -7.5 | 1e-11 | 35/47 (HepG2/C3A, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.762×** | -7.2 | 5e-11 | 34/48 (PANC-1, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | 0.882× | -4.7 | 2e-04 | 15/48 (NCI-H23, A-427, …) | rises with dose |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.736×** | -4.3 | 0.002 | 27/49 (NCI-H2347, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 0.873× | -3.6 | 0.021 | 18/48 (A-427, NCI-H23, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.825×** | -3.3 | 0.055 | 19/48 (Hs 766T, CHP-212, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 0.885× | -3.3 | 0.061 | 12/48 (LoVo, SW 900, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.891× | -3.1 | 0.11 | 14/48 (CFPAC-1, HCT15, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.884× | -3.0 | 0.11 | 16/47 (HS-578T, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8208. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 193 | 8 (2 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +20.5) | [[Dinaciclib (drug)]] 5 µM 0.271× (z -19.9) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 210 | 7 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +15.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.20× (z +11.9) | [[Dinaciclib (drug)]] 0.5 µM 0.406× (z -13.6) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 218 | 6 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.07× (z +39.8) | [[Dinaciclib (drug)]] 0.5 µM 0.253× (z -23.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 295 | 4 (1 ⚠) | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +28.4) | [[Dinaciclib (drug)]] 5 µM 0.203× (z -29.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 140 | 6 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +18.8) | [[Dinaciclib (drug)]] 5 µM 0.328× (z -15.8) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 222 | 5 (2 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +25.0) | [[Dinaciclib (drug)]] 0.05 µM 0.277× (z -16.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 347 | 4 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +22.6) | [[Dinaciclib (drug)]] 5 µM 0.162× (z -26.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 128 | 4 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +12.9) | [[Dinaciclib (drug)]] 0.5 µM 0.452× (z -13.3) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 217 | 3 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +16.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.513× (z -15.6) ⚠ cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 230 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.244× (z -23.5) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.549× (z -10.0) |
| [[LoVo (line)]] | wt | 319 | 4 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +23.0) | [[Dinaciclib (drug)]] 5 µM 0.231× (z -25.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 273 | 3 | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 3.50× (z +14.6) | [[Dinaciclib (drug)]] 0.5 µM 0.323× (z -25.2) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 231 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +15.4) | [[Dinaciclib (drug)]] 5 µM 0.315× (z -17.9) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 150 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +15.9) | [[Dinaciclib (drug)]] 0.5 µM 0.549× (z -9.0) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 194 | 2 | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 4.16× (z +12.8) | [[Dinaciclib (drug)]] 5 µM 0.216× (z -25.2) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 199 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +26.3) | [[Dinaciclib (drug)]] 0.5 µM 0.348× (z -15.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 176 | 2 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +32.0) | [[Dinaciclib (drug)]] 0.05 µM 0.185× (z -23.0) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 215 | 1 | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.54× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.231× (z -23.1) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 258 | 5 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.33× (z +12.8) | [[Dinaciclib (drug)]] 0.5 µM 0.557× (z -8.9) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 226 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +12.0) | [[Dinaciclib (drug)]] 0.5 µM 0.312× (z -13.9) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 237 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +20.3) | [[Dinaciclib (drug)]] 0.5 µM 0.247× (z -19.3) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 291 | 2 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.20× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.236× (z -24.8) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 185 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +21.0) | [[Dinaciclib (drug)]] 5 µM 0.291× (z -20.3) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 263 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +28.0) | [[Dinaciclib (drug)]] 5 µM 0.183× (z -25.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 230 | 2 | 3 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 4.14× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.175× (z -26.1) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 211 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +18.7) | [[Dinaciclib (drug)]] 0.5 µM 0.357× (z -16.8) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 259 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +19.2) | [[Dinaciclib (drug)]] 5 µM 0.165× (z -27.6) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 197 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +22.1) | [[Dinaciclib (drug)]] 0.05 µM 0.233× (z -18.3) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 417 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +16.1) | [[Dinaciclib (drug)]] 0.5 µM 0.154× (z -28.5) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 283 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +13.9) | [[Dinaciclib (drug)]] 5 µM 0.163× (z -23.1) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 240 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +22.7) | [[Dinaciclib (drug)]] 0.5 µM 0.282× (z -18.3) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 266 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.96× (z +10.2) | [[Dinaciclib (drug)]] 0.05 µM 0.0344× (z -44.2) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 302 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +16.1) | [[Dinaciclib (drug)]] 5 µM 0.274× (z -15.4) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 293 | 0 | 4 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.271× (z -18.0) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.615× (z -9.9) |
| [[hTERT-HPNE (line)]] | wt | 162 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.79× (z +20.8) | [[Dinaciclib (drug)]] 0.5 µM 0.343× (z -10.0) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 206 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 2.77× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.295× (z -18.7) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 145 | 1 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 1.82× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.429× (z -13.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 396 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.172× (z -28.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 171 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.341× (z -15.2) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 375 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.217× (z -15.5) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 327 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.245× (z -18.8) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 220 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.440× (z -9.5) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 116 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.413× (z -11.1) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 227 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.259× (z -11.9) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 240 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.518× (z -9.0) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 273 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0397× (z -17.1) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 326 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +8.6) | — |
| [[NCI-H2122 (line)]] | alt | 201 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 230 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 174 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8208), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NSUN6]] | +0.58 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[PIBF1]] | +0.55 | +0.54 / +0.46 | both halves | 2e-05 |  |
| [[LINC01572]] | +0.54 | +0.46 / +0.52 | both halves | 2e-05 |  |
| [[USP32]] | +0.51 | +0.41 / +0.49 | both halves | 4e-05 |  |
| [[LINC00659]] | +0.50 | +0.44 / +0.43 | both halves | 3e-05 |  |
| [[NME7]] | +0.49 | +0.51 / +0.41 | both halves | 4e-05 |  |
| [[KDM4C]] | +0.49 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[UBAP2]] | +0.49 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[TXNDC17]] | +0.48 | +0.43 / +0.40 | both halves | 5e-05 |  |
| [[GALE]] | +0.48 | +0.36 / +0.45 | both halves | 1e-04 |  |
| [[BCAN-AS1]] | +0.48 | +0.38 / +0.47 | both halves | 7e-05 |  |
| [[PRAG1]] | +0.48 | +0.37 / +0.37 | both halves | 8e-05 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CIZ1]] | -0.53 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[FHIP2A]] | -0.52 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[SNHG22]] | -0.51 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[FBXO7]] | -0.51 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[TBKBP1]] | -0.50 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[ANGEL2]] | -0.48 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[SMPDL3A]] | -0.48 | -0.35 / -0.52 | both halves | 1e-04 |  |
| [[NDST1]] | -0.48 | -0.44 / -0.39 | both halves | 5e-05 |  |
| [[NAPB]] | -0.48 | -0.49 / -0.39 | both halves | 6e-05 |  |
| [[TSR2]] | -0.47 | -0.32 / -0.43 | both halves | 2e-04 |  |
| [[RCAN3]] | -0.46 | -0.38 / -0.46 | both halves | 7e-05 |  |
| [[SVIL-AS1-1]] | -0.46 | -0.52 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EFNB2]] | B | EFNB2 activity lowers RAPGEF6's level | lines that do not express EFNB2 (15) vs lines expressing it (35) | 1.37× higher at baseline in the lines without EFNB2 | 0.006 | ⚠ within organs, on part of the lines; also absent: FUT2, SATB1, C6orf141 |
| [[MAGEA4]] | B | MAGEA4 activity raises RAPGEF6's level | lines that do not express MAGEA4 (41) vs lines expressing it (9) | 1.22× lower at baseline in the lines without MAGEA4 | 0.079 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: CGA, CALCA, GCG |
| [[PRAG1]] | B | PRAG1 activity lowers RAPGEF6's level | lines that do not express PRAG1 (16) vs lines expressing it (34) | 1.23× higher at baseline in the lines without PRAG1 | 0.084 | ⚠ within organs, on part of the lines; also absent: ANO9, EPS8L2, PDGFB; maybe low, not absent |
| [[SETD7]] | C | SETD7 activity lowers RAPGEF6's level | lines that do not express SETD7 (3) vs lines expressing it (47) | 1.60× higher at baseline in the lines without SETD7 | 0.055 | ⚠ few lines (3 vs 47); across organs; also absent: MAP3K5, SNHG15; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 171]] — Sealing of the nuclear envelope (NE) by ESCRT-III; 24 genes; this gene is in the **-** arm (projection on the module's main direction -0.503). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.41).
- **Nodal map** (x, y) = (-7.2, 8.0); signed map (-35.9, 33.9). **Vector** length 106, 35.7% of its response variance represented; |z| ≥ 3 in 1,359 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +4.7 | +14.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.3 | +11.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +1.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.7 | +10.4 |
|  | [[EX229 (drug)]] 5 µM |  | +2.6 | +3.3 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +2.3 | +0.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.1 | +1.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.1 | +2.4 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -7.3 | -1.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.6 | -7.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -6.0 | -1.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.3 | -3.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -5.2 | -4.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.6 | -3.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.4 | +0.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.2 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | Rap guanine nucleotide exchange factor 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.1 — chr5:131,423,921-131,635,231 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RA-GEF-2, PDZ-GEF2; previously PDZGEF2 |
| Gene groups (HGNC) | PDZ domain containing |
| Hallmark sets | INTERFERON_GAMMA_RESPONSE, MITOTIC_SPINDLE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TEU7](https://www.uniprot.org/uniprotkb/Q8TEU7) (Rap guanine nucleotide exchange factor 6):

> Guanine nucleotide exchange factor (GEF) for Rap1A, Rap2A and M-Ras GTPases. Does not interact with cAMP.

**Summary**, from NCBI Gene [51735](https://www.ncbi.nlm.nih.gov/gene/51735):

> Enables several functions, including GTP-dependent protein binding activity; guanyl-nucleotide exchange factor activity; and phosphatidic acid binding activity. Involved in positive regulation of microvillus assembly. Located in apical plasma membrane; cytosol; and endocytic vesicle. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20655](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20655) · Entrez [51735](https://www.ncbi.nlm.nih.gov/gene/51735) · UniProt [Q8TEU7](https://www.uniprot.org/uniprotkb/Q8TEU7) · Ensembl [ENSG00000158987](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158987)

## Data

Gene col 8208: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8208); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8208, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8208]; `tensor/DDL_lfc|DDL_z.npy` [8208]; `embed/gene_vectors.npy` [8208]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8208 or target_col == 8208). Every well: [[RAPGEF6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAPGEF6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
