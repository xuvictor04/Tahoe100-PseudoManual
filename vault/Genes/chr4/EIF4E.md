---
symbol: "EIF4E"
type: "gene"
col: 7500
ensembl_id: "ENSG00000151247"
name: "eukaryotic translation initiation factor 4E"
location: "4q23"
module: 4
arm: "+"
pooled_cpm: 56.77
n_lines_expressing: 50
n_dd_up: 37
n_dd_down: 10
n_dd_up_clean: 23
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# EIF4E

*eukaryotic translation initiation factor 4E* — 4q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 37 drug-doses (14 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 9.75× (z +18.2, q 0e+00, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.645× (z -6.4, q 1e-07, down in 27 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM: 0.760× (z -4.0, q 0.012, down in 25 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KPNA1]] (+0.63, fdr 7e-06), [[HEATR3]] (+0.62, fdr 7e-06), [[B3GALT6]] (+0.61, fdr 1e-05); moves opposite to [[SERINC3]] (-0.57, fdr 2e-05), [[FAM117A]] (-0.57, fdr 1e-05), [[TSPYL2]] (-0.54, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[RRS1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 14 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 37 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7500.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **9.75×** | +18.2 | 0e+00 | 48/49 (SW480, PANC-1, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.97×** | +16.6 | 0e+00 | 48/48 (LS 180, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.06×** | +15.6 | 0e+00 | 42/48 (A498, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **7.05×** | +15.6 | 0e+00 | 47/48 (SW480, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.63×** | +14.7 | 0e+00 | 46/47 (LS 180, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.20×** | +12.0 | 4e-31 | 47/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.15×** | +11.7 | 1e-29 | 42/48 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.22×** | +11.5 | 7e-29 | 42/47 (LoVo, LS 180, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.06×** | +11.0 | 3e-26 | 43/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.01×** | +10.1 | 4e-22 | 42/48 (A498, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.93×** | +10.0 | 7e-22 | 44/48 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.67×** | +7.8 | 3e-13 | 41/48 (LS 180, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.64×** | +7.5 | 3e-12 | 35/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.60×** | +7.1 | 5e-11 | 38/48 (NCI-H460, HT-29, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.54×** | +6.1 | 3e-08 | 36/48 (HT-29, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.33×** | +6.1 | 5e-08 | 35/49 (CFPAC-1, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.42×** | +5.4 | 3e-06 | 34/48 (CFPAC-1, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.79×** | +4.6 | 1e-04 | 29/48 (NCI-H460, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.35×** | +4.6 | 1e-04 | 25/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.71×** | +4.3 | 4e-04 | 27/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7500.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.645×** | -6.4 | 1e-07 | 27/44 (LS 180, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.708×** | -5.3 | 3e-05 | 26/48 (SNU-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | **0.760×** | -4.0 | 0.012 | 25/49 (AsPC-1, SW48, …) | top dose only | plate-row cell shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.844× | -3.7 | 0.028 | 21/48 (LS 180, C32, …) | all doses, flat | low cells (technical?) |
| [[Filgotinib (drug)]] 0.05 µM |  | **0.788×** | -3.6 | 0.038 | 17/48 (C32, HOP62, …) | inconsistent across doses |  |
| [[Entecavir (monohydrate) (drug)]] 5 µM |  | **0.791×** | -3.4 | 0.057 | 21/48 (HEC-1-A, NCI-H1573, …) | top dose only | plate-row cell shift |
| [[Entrectinib (drug)]] 5 µM |  | **0.804×** | -3.4 | 0.061 | 14/48 (KATO III, SW 1088, …) | rises with dose |  |
| [[Bestatin (hydrochloride) (drug)]] 0.5 µM |  | **0.809×** | -3.3 | 0.069 | 20/48 (CFPAC-1, LOX-IMVI, …) | inconsistent across doses |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **0.809×** | -3.3 | 0.069 | 17/48 (HEC-1-A, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.812×** | -3.2 | 0.071 | 20/49 (H4, COLO 205, …) | all doses, flat |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | 0.868× | -3.1 | 0.091 | 11/48 (KATO III, Panc 03.27, …) | rises with dose |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **0.818×** | -3.1 | 0.091 | 17/48 (SW48, NCI-H1792, …) | inconsistent across doses |  |
| [[Posaconazole (drug)]] 5 µM |  | 0.814× | -3.0 | 0.10 | 12/48 (AsPC-1, LS 180, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7500. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 48.1 | 15 (7 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.15× (z +16.1) | — |
| [[NCI-H1573 (line)]] | alt | 82.4 | 10 (5 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 26.6× (z +15.0) | [[Dinaciclib (drug)]] 5 µM 0.270× (z -10.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 54.3 | 11 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.31× (z +18.6) | — |
| [[LS 180 (line)]] | wt | 77.3 | 8 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.85× (z +18.7) | [[Dinaciclib (drug)]] 5 µM 0.0501× (z -30.0) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 33.6 | 8 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.07× (z +11.9) | — |
| [[HOP62 (line)]] | alt | 46.6 | 7 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.51× (z +12.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.40× (z +12.2) | — |
| [[KATO III (line)]] | alt | 43.8 | 5 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.91× (z +14.3) | [[Dinaciclib (drug)]] 0.5 µM 0.286× (z -11.3) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 43.7 | 7 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.64× (z +16.1) | — |
| [[HEC-1-A (line)]] | alt | 78.7 | 4 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +12.3) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 10.4× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.219× (z -12.9) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 47.8 | 6 (3 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 15.7× (z +12.7) | — |
| [[LoVo (line)]] | wt | 45.1 | 6 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 4.60× (z +14.0) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 14.2× (z +13.4) | — |
| [[NCI-H1792 (line)]] | alt | 37.3 | 5 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.06× (z +11.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.65× (z +10.8) | — |
| [[NCI-H23 (line)]] | alt | 65.9 | 4 (2 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 12.7× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.219× (z -13.7) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 126 | 5 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.25× (z +10.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.25× (z +10.5) | — |
| [[A-172 (line)]] | wt | 53.6 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +12.2) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 8.75× (z +10.0) | — |
| [[A-427 (line)]] | wt | 85.0 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 8.30× (z +12.3) | [[Dinaciclib (drug)]] 0.05 µM 0.331× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 69.8 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +17.1) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.94× (z +9.2) | — |
| [[AsPC-1 (line)]] | alt | 48.4 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +12.3) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.19× (z +10.6) | — |
| [[BT-474 (line)]] | alt | 69.4 | 3 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 9.30× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.382× (z -8.7) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 40.7 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +14.2) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.37× (z +10.5) | — |
| [[J82 (line)]] | alt | 46.2 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.06× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.355× (z -8.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 64.2 | 4 (2 ⚠) | 0 | [[PH-797804 (drug)]] 5 µM 9.39× (z +10.3) | — |
| [[SW1417 (line)]] | alt | 51.1 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.78× (z +10.3) | — |
| [[A549 (line)]] | wt | 42.0 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +13.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 12.0× (z +9.3) | — |
| [[H4 (line)]] | wt | 41.6 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.51× (z +9.5) | — |
| [[LOX-IMVI (line)]] | wt | 51.2 | 3 | 0 | [[TAK-901 (drug)]] 0.05 µM 3.74× (z +9.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 53.2 | 3 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 12.2× (z +9.8) | — |
| [[RKO (line)]] | wt | 87.1 | 2 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 11.3× (z +12.6) | [[Dinaciclib (drug)]] 0.5 µM 0.349× (z -10.5) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 88.0 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 7.49× (z +9.1) | — |
| [[Hs 766T (line)]] | wt | 27.8 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.01× (z +8.9) | — |
| [[hTERT-HPNE (line)]] | wt | 37.2 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.14× (z +9.9) | — |
| [[Panc 03.27 (line)]] | alt | 48.7 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 11.5× (z +11.3) | — |
| [[SNU-1 (line)]] | wt | 75.5 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 11.0× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.121× (z -16.1) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 22.1 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.07× (z +13.5) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[C32 (line)]] | wt | 63.3 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 17.3× (z +9.8) | — |
| [[CHP-212 (line)]] | wt | 68.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.121× (z -8.6) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 50.8 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 10.2× (z +8.6) | — |
| [[HS-578T (line)]] | alt | 35.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +12.7) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H2030 (line)]] | alt | 92.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.253× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 92.2 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.17× (z +8.5) | — |
| [[RPMI-7951 (line)]] | alt | 48.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.262× (z -8.6) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 96.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 56.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 59.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 77.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 49.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7500), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KPNA1]] | +0.63 | +0.71 / +0.64 | both halves | 7e-06 | pathway: Antimicrobial mechanism of IFN-stimulated genes |
| [[HEATR3]] | +0.62 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[B3GALT6]] | +0.61 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[NAA15]] | +0.58 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[UCK2]] | +0.58 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[WDR43]] | +0.57 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[CDIN1]] | +0.57 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[GTF2F2]] | +0.57 | +0.65 / +0.52 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[USP10]] | +0.56 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[RRS1]] | +0.55 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[NAA25]] | +0.54 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[VWA8]] | +0.54 | +0.60 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SERINC3]] | -0.57 | -0.46 / -0.53 | both halves | 2e-05 |  |
| [[FAM117A]] | -0.57 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[TSPYL2]] | -0.54 | -0.49 / -0.57 | both halves | 1e-05 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE |
| [[LASP1]] | -0.54 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[TOX4]] | -0.53 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[CEP95]] | -0.52 | -0.63 / -0.38 | both halves | 6e-05 |  |
| [[ATG12]] | -0.51 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[SENP2]] | -0.50 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[ACOX1]] | -0.49 | -0.40 / -0.50 | both halves | 4e-05 |  |
| [[SLC35F5]] | -0.49 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[OTUD5]] | -0.49 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[ALDH6A1]] | -0.48 | -0.45 / -0.52 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RRS1]] | C | EIF4E's natural level weakens RRS1's drug response | EIF4E's natural level across 46 lines (lineage-adjusted; a glimpse) | r -0.66, reverse -0.22; direction not clear | 0.049 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.470). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-9.7, -40.5); signed map (-9.6, -52.0). **Vector** length 73.1, 22.4% of its response variance represented; |z| ≥ 3 in 1,387 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +2.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.9 | +4.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.6 | +0.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +2.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +2.8 | +11.5 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.6 | +4.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.4 | +4.6 |
|  | [[EX229 (drug)]] 5 µM |  | +2.4 | +4.3 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.6 | +16.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.4 | +12.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | -2.7 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -2.8 | -3.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.7 | +11.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.7 | -1.9 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.3 | +0.2 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -2.0 | -2.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.0 | -1.7 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.9 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | eukaryotic translation initiation factor 4E |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q23 — chr4:98,879,276-98,929,133 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EIF4E1; previously EIF4EL1, EIF4F |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING, UNFOLDED_PROTEIN_RESPONSE, MYC_TARGETS_V1 |
| Reactome | 29 pathways, smallest: Z-decay: degradation of maternal mRNAs by zygotically expressed factors; mTORC1-mediated signalling; Deadenylation of mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [P06730](https://www.uniprot.org/uniprotkb/P06730) (Eukaryotic translation initiation factor 4E):

> Acts in the cytoplasm to initiate and regulate protein synthesis and is required in the nucleus for export of a subset of mRNAs from the nucleus to the cytoplasm which promotes processes such as RNA capping, processing and splicing. Component of the protein complex eIF4F, which is involved in the recognition of the mRNA cap, ATP-dependent unwinding of 5'-terminal secondary structure and recruitment of mRNA to the ribosome (By similarity). This protein recognizes and binds the 7-methylguanosine …

**Summary**, from NCBI Gene [1977](https://www.ncbi.nlm.nih.gov/gene/1977):

> The protein encoded by this gene is a component of the eukaryotic translation initiation factor 4F complex, which recognizes the 7-methylguanosine cap structure at the 5' end of messenger RNAs. The encoded protein aids in translation initiation by recruiting ribosomes to the 5'-cap structure. Association of this protein with the 4F complex is the rate-limiting step in translation initiation. This gene acts as a proto-oncogene, and its expression and activation is associated with transformation …

**Accessions** — [HGNC:3287](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3287) · Entrez [1977](https://www.ncbi.nlm.nih.gov/gene/1977) · UniProt [P06730](https://www.uniprot.org/uniprotkb/P06730) · Ensembl [ENSG00000151247](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151247)

## Data

Gene col 7500: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7500); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7500, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7500]; `tensor/DDL_lfc|DDL_z.npy` [7500]; `embed/gene_vectors.npy` [7500]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7500 or target_col == 7500). Every well: [[EIF4E — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EIF4E.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
