---
symbol: "ARID3B"
type: "gene"
col: 11023
ensembl_id: "ENSG00000179361"
name: "AT-rich interaction domain 3B"
location: "15q24.1"
module: 136
arm: "+"
pooled_cpm: 59.84
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 40
n_dd_up_clean: 16
n_dd_down_clean: 33
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/136"]
generated_by: "tahoemap"
---

# ARID3B

*AT-rich interaction domain 3B* — 15q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.26× (z +12.0, q 1e-30, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 40 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.309× (z -16.6, q 0e+00, down in 37 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 0.659× (z -8.6, q 1e-15, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYO9B]] (+0.75, fdr 1e-05), [[GIPR]] (+0.73, fdr 7e-06), [[PDLIM7]] (+0.72, fdr 7e-06); moves opposite to [[FUBP1]] (-0.68, fdr 1e-05), [[USP24]] (-0.64, fdr 4e-05), [[PHACTR2]] (-0.63, fdr 4e-05).
> It is in [[Module 136]], a single-armed module (heme metabolism).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[F3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11023.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.26×** | +12.0 | 1e-30 | 38/48 (LoVo, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[TAK-901 (drug)]] 5 µM |  | **4.75×** | +12.0 | 1e-30 | 46/49 (PANC-1, RPMI-7951, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **2.08×** | +10.8 | 7e-25 | 38/48 (RKO, SW1417, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.95×** | +9.8 | 1e-20 | 39/48 (RKO, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[PH-797804 (drug)]] 5 µM |  | **3.25×** | +9.1 | 1e-17 | 35/48 (SW480, BT-474, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.42×** | +7.3 | 3e-11 | 35/48 (C32, PANC-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.61×** | +7.1 | 1e-10 | 27/48 (SW480, SW48, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.46×** | +5.6 | 1e-06 | 37/49 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.45×** | +5.5 | 2e-06 | 26/48 (AsPC-1, SW48, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.35×** | +4.4 | 5e-04 | 23/48 (SW480, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.34×** | +4.4 | 7e-04 | 25/48 (SW480, SNU-1, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.33×** | +4.2 | 0.001 | 22/48 (SW1417, PANC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.21×** | +3.9 | 0.004 | 22/49 (CFPAC-1, LS 180, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.62×** | +3.7 | 0.008 | 22/48 (SW480, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.28×** | +3.6 | 0.011 | 24/48 (SW480, SW48, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 5 µM |  | 1.18× | +3.6 | 0.012 | 15/49 (NCI-H1792, KATO III, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.26×** | +3.4 | 0.018 | 19/48 (LS 180, KATO III, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 40 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11023.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.309×** | -16.6 | 0e+00 | 37/42 (LoVo, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.443×** | -11.9 | 3e-30 | 40/48 (SK-MEL-2, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.659×** | -8.6 | 1e-15 | 36/48 (C32, HS-578T, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.736×** | -5.5 | 5e-06 | 31/48 (AsPC-1, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.709×** | -5.5 | 5e-06 | 31/49 (AsPC-1, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.732×** | -5.4 | 6e-06 | 34/48 (AsPC-1, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.683×** | -5.4 | 7e-06 | 27/47 (AsPC-1, SW48, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.768×** | -5.3 | 7e-06 | 31/49 (SW480, Hs 766T, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.772×** | -5.3 | 9e-06 | 30/48 (AsPC-1, SW480, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.700×** | -5.2 | 1e-05 | 27/48 (HOP62, HS-578T, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.707×** | -5.1 | 2e-05 | 28/49 (AsPC-1, NCI-H1573, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.713×** | -4.7 | 1e-04 | 28/48 (AsPC-1, A549, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.728×** | -4.6 | 2e-04 | 30/47 (A549, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.711×** | -4.6 | 2e-04 | 27/48 (AsPC-1, NCI-H1792, …) | all doses, flat |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.718×** | -4.6 | 2e-04 | 28/48 (AsPC-1, CFPAC-1, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.740×** | -4.4 | 4e-04 | 24/48 (NCI-H1792, HS-578T, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.750×** | -4.0 | 0.002 | 24/48 (NCI-H1792, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11023. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 112 | 0 | 8 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.319× (z -12.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.356× (z -11.3) |
| [[hTERT-HPNE (line)]] | wt | 94.8 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0312× (z -22.0) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.383× (z -8.9) |
| [[AsPC-1 (line)]] | alt | 94.8 | 2 (1 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.40× (z +11.0) | [[Trametinib (drug)]] 0.5 µM 0.316× (z -10.2) |
| [[HS-578T (line)]] | alt | 65.7 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -12.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.343× (z -12.1) |
| [[NCI-H1792 (line)]] | alt | 149 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0514× (z -19.9) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 40.9 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.17× (z +9.9) | — |
| [[SW48 (line)]] | wt | 46.4 | 4 (2 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.09× (z +10.5) | [[Capmatinib (drug)]] 5 µM 0.0603× (z -8.5) |
| [[SW480 (line)]] | alt | 81.1 | 4 (3 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 4.41× (z +11.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.53× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.257× (z -10.3) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 50.2 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.14× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.0682× (z -23.7) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 83.6 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.158× (z -15.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 45.0 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 10.4× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.233× (z -14.1) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 46.8 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.226× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.457× (z -9.9) |
| [[C-33 A (line)]] | alt | 74.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.150× (z -14.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 85.8 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 8.94× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.0775× (z -18.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 69.1 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +11.5) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 5 µM 0.176× (z -15.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 46.0 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 7.82× (z +9.0) | — |
| [[A-427 (line)]] | wt | 50.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.293× (z -10.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.437× (z -10.3) |
| [[C32 (line)]] | wt | 29.7 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 2.73× (z +9.4) | [[Selinexor (drug)]] 5 µM 0.232× (z -13.5) |
| [[CFPAC-1 (line)]] | alt | 109 | 1 | 1 (1 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 2.27× (z +8.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.409× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 26.9 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.38× (z +13.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HCT15 (line)]] | alt | 36.2 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.67× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.181× (z -9.1) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 61.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.210× (z -13.5) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 57.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 3.21× (z +8.5) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 0.5 µM 0.294× (z -8.8) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 60.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.185× (z -11.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 34.6 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.32× (z +8.6) | — |
| [[RPMI-7951 (line)]] | alt | 40.9 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 16.0× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.253× (z -8.8) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 71.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0642× (z -21.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 38.8 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.321× (z -8.7) ⚠ cell-cycle shift, explains ~57% of this change |
| [[A549 (line)]] | wt | 83.5 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.331× (z -11.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 34.4 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.309× (z -8.7) |
| [[HT-29 (line)]] | alt | 36.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +8.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[J82 (line)]] | alt | 41.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.193× (z -13.0) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 44.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.257× (z -9.3) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 50.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.243× (z -11.4) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 74.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.263× (z -12.1) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 33.8 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.64× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SNU-1 (line)]] | wt | 56.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.261× (z -9.2) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 42.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.279× (z -8.5) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 67.8 | 0 | 1 | — | [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM 0.0794× (z -8.9) |
| [[SW 900 (line)]] | alt | 40.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.247× (z -8.9) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 64.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 35.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 98.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 40.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 66.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 74.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 62.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11023), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYO9B]] | +0.75 | +0.79 / +0.56 | both halves | 1e-05 |  |
| [[GIPR]] | +0.73 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[PDLIM7]] | +0.72 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[CSNK1E]] | +0.72 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[TNNT1]] | +0.72 | +0.72 / +0.59 | both halves | 7e-06 |  |
| [[STX1A]] | +0.71 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[PLAUR]] | +0.71 | +0.72 / +0.63 | both halves | 7e-06 |  |
| [[SH3BGRL3]] | +0.69 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[RAC2]] | +0.69 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[PLEKHG5]] | +0.68 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[ABTB3]] | +0.68 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[SH3GL1]] | +0.68 | +0.71 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FUBP1]] | -0.68 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[USP24]] | -0.64 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[PHACTR2]] | -0.63 | -0.67 / -0.42 | both halves | 4e-05 |  |
| [[MCCC2]] | -0.62 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[SNX5]] | -0.61 | -0.62 / -0.37 | both halves | 8e-05 |  |
| [[MGST1]] | -0.61 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[UBAP2L]] | -0.59 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[HDGF]] | -0.59 | -0.55 / -0.38 | both halves | 7e-05 |  |
| [[ADI1]] | -0.59 | -0.56 / -0.35 | both halves | 1e-04 |  |
| [[TBC1D5]] | -0.59 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[IQCH-AS1]] | -0.59 | -0.59 / -0.34 | both halves | 1e-04 |  |
| [[GTF2I]] | -0.59 | -0.36 / -0.51 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[F3]] | B | F3 activity weakens ARID3B's drug response | lines that do not express F3 (24) vs lines expressing it (25) | the lines without F3 respond 1.12× as strongly (z diff -0.64); strongest at Belinostat 5 µM: 2.25x vs 1.60x (z diff -2.7) | 0.054 | ⚠ within organs, on part of the lines; also absent: TLR2, KRT7, EDNRA; target measured in part of the lines; artifact flags |
| [[BCL2A1]] | B | BCL2A1 activity raises ARID3B's level | lines that do not express BCL2A1 (26) vs lines expressing it (24) | 1.35× lower at baseline in the lines without BCL2A1 | 0.069 | ⚠ within organs, on part of the lines; also absent: BASP1-AS1, TMEM156, CSGALNACT1 |
| [[SEMA7A]] | B | SEMA7A activity raises ARID3B's level | lines that do not express SEMA7A (13) vs lines expressing it (37) | 1.23× lower at baseline in the lines without SEMA7A | 0.070 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[FOXG1]] | B | FOXG1 activity raises ARID3B's level | lines that do not express FOXG1 (36) vs lines expressing it (14) | 1.41× lower at baseline in the lines without FOXG1 | 0.094 | ⚠ within organs, on part of the lines; co-absent genes; also absent: LINC02566, MMRN1, GCG |
| [[STAC]] | B | STAC activity raises ARID3B's level | lines that do not express STAC (25) vs lines expressing it (25) | 1.35× lower at baseline in the lines without STAC | 0.095 | ⚠ within organs, on part of the lines; also absent: GUCY1B1, ZNF229, DNAH11 |
| [[HMGA1]] | C | HMGA1 activity raises ARID3B's level | lines that do not express HMGA1 (4) vs lines expressing it (46) | 1.94× lower at baseline in the lines without HMGA1 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: POLR3G, CMTM7, BOK; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 136]] — heme metabolism; 35 genes; every member is in the + arm (projection on the module's main direction 0.854). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (46.4, 1.7); signed map (-0.9, 47.0). **Vector** length 134, 45.5% of its response variance represented; |z| ≥ 3 in 1,685 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +7.9 | +9.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.7 | +7.3 |
|  | [[Belinostat (drug)]] 5 µM |  | +7.5 | +10.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +7.0 | +12.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~9% of this change | +6.7 | +2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.0 | +4.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.8 | +3.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.5 | +2.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.2 | +0.0 |
| fall | [[Selinexor (drug)]] 5 µM |  | -8.2 | -8.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -5.7 | -4.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.6 | +0.4 |
|  | [[Trametinib (drug)]] 5 µM |  | -5.5 | -4.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -5.4 | -5.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -5.3 | -5.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.3 | -5.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -5.1 | -5.1 |

## What is on record

|  |  |
|---|---|
| Name | AT-rich interaction domain 3B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q24.1 — chr15:74,541,206-74,598,131 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BDP, DRIL2 |
| Gene groups (HGNC) | AT-rich interaction domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IVW6](https://www.uniprot.org/uniprotkb/Q8IVW6) (AT-rich interactive domain-containing protein 3B):

> Transcription factor which may be involved in neuroblastoma growth and malignant transformation. Favors nuclear targeting of ARID3A.

**Summary**, from NCBI Gene [10620](https://www.ncbi.nlm.nih.gov/gene/10620):

> This gene encodes a member of the ARID (AT-rich interaction domain) family of DNA-binding proteins. The encoded protein is homologous with two proteins that bind to the retinoblastoma gene product, and also with the mouse Bright and Drosophila dead ringer proteins. A pseudogene on chromosome 1p31 exists for this gene. Members of the ARID family have roles in embryonic patterning, cell lineage gene regulation, cell cycle control, transcriptional regulation and possibly in chromatin structure …

**Accessions** — [HGNC:14350](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14350) · Entrez [10620](https://www.ncbi.nlm.nih.gov/gene/10620) · UniProt [Q8IVW6](https://www.uniprot.org/uniprotkb/Q8IVW6) · Ensembl [ENSG00000179361](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179361)

## Data

Gene col 11023: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11023); `tables/drug_effects.parquet` (62 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11023, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11023]; `tensor/DDL_lfc|DDL_z.npy` [11023]; `embed/gene_vectors.npy` [11023]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11023 or target_col == 11023). Every well: [[ARID3B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARID3B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
