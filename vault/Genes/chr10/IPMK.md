---
symbol: "IPMK"
type: "gene"
col: 7492
ensembl_id: "ENSG00000151151"
name: "inositol polyphosphate multikinase"
location: "10q21.1"
module: 144
arm: "+"
pooled_cpm: 90.26
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 3
n_dd_up_clean: 17
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/144"]
generated_by: "tahoemap"
---

# IPMK

*inositol polyphosphate multikinase* — 10q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.26× (z +27.7, q 0e+00, up in 45 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.596× (z -12.4, q 2e-32, down in 37 of 49 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (HEC-1-A 0.381×, C-33 A 0.208×, H4 0.263×, A549 0.365×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (A-427 0.211×, CFPAC-1 0.375×, C32 0.389×, SNU-423 0.475×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 2 lines (BT-474 0.291×, C32 0.466×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RSBN1]] (+0.72, fdr 7e-06), [[RBPJ]] (+0.70, fdr 1e-05), [[EGLN1]] (+0.69, fdr 7e-06); moves opposite to [[DELE1]] (-0.61, fdr 1e-05), [[POGK]] (-0.55, fdr 1e-05), [[RBM28]] (-0.54, fdr 2e-05).
> It is in [[Module 144]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[RORA]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7492.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.26×** | +27.7 | 0e+00 | 45/49 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[TAK-901 (drug)]] 5 µM |  | **6.19×** | +22.9 | 0e+00 | 48/49 (SW480, NCI-H460, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +13.5 | 2e-39 | 40/48 (SW480, HS-578T, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.66×** | +12.3 | 1e-32 | 39/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.66×** | +12.1 | 9e-32 | 35/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +11.7 | 2e-29 | 38/50 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.35×** | +10.1 | 6e-22 | 27/48 (PANC-1, SW480, …) | inconsistent across doses | composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.46×** | +9.1 | 9e-18 | 31/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +8.9 | 5e-17 | 33/48 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.44×** | +8.8 | 7e-17 | 33/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.41×** | +8.2 | 2e-14 | 34/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.39×** | +8.0 | 7e-14 | 36/48 (NCI-H23, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.75×** | +7.0 | 9e-11 | 29/48 (SNU-423, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.34×** | +6.9 | 1e-10 | 37/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.30×** | +6.3 | 1e-08 | 27/48 (NCI-H23, PANC-1, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.29×** | +6.1 | 3e-08 | 28/48 (J82, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.30×** | +6.1 | 3e-08 | 26/47 (CFPAC-1, LoVo, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.28×** | +6.0 | 7e-08 | 26/48 (NCI-H1792, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7492.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (HEC-1-A 0.381×, C-33 A 0.208×, H4 0.263×, A549 0.365×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (A-427 0.211×, CFPAC-1 0.375×, C32 0.389×, SNU-423 0.475×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 2 lines (BT-474 0.291×, C32 0.466×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.596×** | -12.4 | 2e-32 | 37/49 (A-427, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.623×** | -10.9 | 3e-25 | 33/42 (HEC-1-A, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.946× | -4.6 | 6e-04 | 0/50 | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.819×** | -4.6 | 6e-04 | 22/47 (C32, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.849× | -3.8 | 0.018 | 18/47 (A-427, C32, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | 0.899× | -3.6 | 0.031 | 8/49 (CFPAC-1, NCI-H2347, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.863× | -3.5 | 0.035 | 13/48 (A-427, HS-578T, …) | rises with dose |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.839× | -3.3 | 0.066 | 13/48 (HOP62, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.873× | -3.2 | 0.073 | 10/48 (A-427, C32, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | 0.875× | -3.2 | 0.082 | 18/48 (BT-474, C32, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | 0.783× | -3.1 | 0.11 | 12/48 (CFPAC-1, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 0.876× | -3.0 | 0.11 | 18/48 (C32, CFPAC-1, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | 0.786× | -3.0 | 0.11 | 16/48 (Panc 03.27, COLO 205, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7492. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 104 | 15 (6 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 10.1× (z +21.0) | [[Dinaciclib (drug)]] 5 µM 0.573× (z -9.3) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 81.8 | 13 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +22.0) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.67× (z +20.4) | — |
| [[NCI-H460 (line)]] | wt | 98.0 | 10 (4 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 17.7× (z +16.6) | — |
| [[HS-578T (line)]] | alt | 61.8 | 8 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.83× (z +15.5) | — |
| [[LS 180 (line)]] | wt | 57.5 | 7 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.48× (z +18.7) | — |
| [[C32 (line)]] | wt | 90.3 | 1 | 5 (4 ⚠) | [[PH-797804 (drug)]] 5 µM 5.87× (z +10.2) | [[Niclosamide (olamine) (drug)]] 5 µM 0.302× (z -12.7) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.466× (z -8.5) |
| [[LoVo (line)]] | wt | 52.5 | 6 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.43× (z +23.4) | — |
| [[A-427 (line)]] | wt | 162 | 2 (1 ⚠) | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 7.35× (z +12.9) | [[Dinaciclib (drug)]] 0.5 µM 0.211× (z -19.3) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 98.9 | 4 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.73× (z +14.9) | [[Dinaciclib (drug)]] 5 µM 0.412× (z -8.9) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 176 | 3 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.74× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.444× (z -10.1) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 116 | 2 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.263× (z -11.9) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 57.6 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.17× (z +19.1) | — |
| [[NCI-H1792 (line)]] | alt | 158 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 11.7× (z +16.1) | [[Dinaciclib (drug)]] 5 µM 0.499× (z -8.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 94.8 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.69× (z +14.3) | — |
| [[SW 900 (line)]] | alt | 166 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 10.6× (z +12.8) | [[Dinaciclib (drug)]] 0.5 µM 0.410× (z -9.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 72.5 | 2 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 14.3× (z +15.1) | [[Dinaciclib (drug)]] 5 µM 0.365× (z -10.5) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 160 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.67× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.375× (z -13.3) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 125 | 2 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 5.59× (z +14.5) | [[Dinaciclib (drug)]] 5 µM 0.381× (z -15.0) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 95.6 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.29× (z +15.4) | — |
| [[HT-29 (line)]] | alt | 60.5 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.65× (z +13.6) | — |
| [[KATO III (line)]] | alt | 52.2 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.64× (z +13.8) | — |
| [[NCI-H1573 (line)]] | alt | 62.2 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.14× (z +22.1) | — |
| [[NCI-H23 (line)]] | alt | 44.9 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.83× (z +13.8) | — |
| [[RPMI-7951 (line)]] | alt | 121 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +11.1) | — |
| [[SK-MEL-2 (line)]] | alt | 97.3 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.34× (z +11.0) | [[Selinexor (drug)]] 5 µM 0.524× (z -9.7) ⚠ cell-cycle shift, explains ~90% of this change |
| [[A-172 (line)]] | wt | 87.7 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.72× (z +15.7) | [[Dinaciclib (drug)]] 5 µM 0.374× (z -10.4) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 78.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +10.6) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +10.4) | — |
| [[AsPC-1 (line)]] | alt | 83.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.93× (z +20.8) | — |
| [[BT-474 (line)]] | alt | 66.7 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.291× (z -11.3) |
| [[C-33 A (line)]] | alt | 58.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.208× (z -12.2) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 49.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.78× (z +14.4) | — |
| [[Hs 766T (line)]] | wt | 105 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.92× (z +17.0) | — |
| [[hTERT-HPNE (line)]] | wt | 111 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +10.9) | — |
| [[J82 (line)]] | alt | 73.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.32× (z +12.0) | — |
| [[NCI-H2030 (line)]] | alt | 79.8 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 6.67× (z +12.8) | — |
| [[NCI-H2347 (line)]] | alt | 69.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +13.7) | — |
| [[SW1417 (line)]] | alt | 71.7 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +15.1) | — |
| [[SW48 (line)]] | wt | 37.9 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.227× (z -9.8) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 104 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.194× (z -9.6) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 108 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +10.0) | — |
| [[HepG2_C3A (line)]] | wt | 153 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +11.1) | — |
| [[Panc 03.27 (line)]] | alt | 82.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +11.3) | — |
| [[AN3 CA (line)]] | alt | 160 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 58.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 41.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 82.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 102 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7492), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RSBN1]] | +0.72 | +0.73 / +0.68 | both halves | 7e-06 |  |
| [[RBPJ]] | +0.70 | +0.55 / +0.71 | both halves | 1e-05 |  |
| [[EGLN1]] | +0.69 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[ZNF654]] | +0.69 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[KDM2A]] | +0.68 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[RNF122]] | +0.66 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[SAP30-DT]] | +0.65 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[MXI1]] | +0.64 | +0.53 / +0.73 | both halves | 1e-05 |  |
| [[MLLT3]] | +0.63 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[DIPK2A]] | +0.62 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[AK4]] | +0.62 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[USP28]] | +0.61 | +0.55 / +0.66 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DELE1]] | -0.61 | -0.53 / -0.62 | both halves | 1e-05 |  |
| [[POGK]] | -0.55 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[RBM28]] | -0.54 | -0.46 / -0.53 | both halves | 2e-05 |  |
| [[DMAC2L]] | -0.51 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[BCL7B]] | -0.50 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[GTF2H3]] | -0.50 | -0.32 / -0.56 | both halves | 2e-04 |  |
| [[SLC35C2]] | -0.49 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[EIF2B3]] | -0.48 | -0.38 / -0.48 | both halves | 7e-05 |  |
| [[MIER2]] | -0.48 | -0.36 / -0.49 | both halves | 1e-04 |  |
| [[SMARCB1]] | -0.48 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[ADAMTSL5]] | -0.48 | -0.38 / -0.51 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RORA]] | B | RORA activity raises IPMK's level | lines that do not express RORA (8) vs lines expressing it (42) | 1.45× lower at baseline in the lines without RORA | 0.067 | ⚠ within organs, on part of the lines; also absent: DPF3, TMC3-AS1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 144]]; 32 genes; every member is in the + arm (projection on the module's main direction 0.829). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.6, -18.4); signed map (-34.4, 24.7). **Vector** length 119, 35.8% of its response variance represented; |z| ≥ 3 in 1,255 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.3 | +27.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | +8.4 | +22.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.7 | +11.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.7 | +13.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +5.4 | +6.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.1 | +12.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.2 | +6.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.6 | +2.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.3 | +2.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.3 | +2.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.3 | -3.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.6 | -10.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.3 | -4.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | -4.2 | +10.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.0 | -12.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.0 | -3.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.0 | -3.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.7 | -3.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.7 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | inositol polyphosphate multikinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q21.1 — chr10:58,191,517-58,267,894 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Inositol phosphate kinases |
| Reactome | 2 pathways, smallest: Synthesis of IPs in the nucleus; Inositol phosphate metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NFU5](https://www.uniprot.org/uniprotkb/Q8NFU5) (Inositol polyphosphate multikinase):

> Inositol phosphate kinase with a broad substrate specificity. Phosphorylates inositol 1,4,5-trisphosphate (Ins(1,4,5)P3) first to inositol 1,3,4,5-tetrakisphosphate and then to inositol 1,3,4,5,6-pentakisphosphate (Ins(1,3,4,5,6)P5). Phosphorylates inositol 1,3,4,6-tetrakisphosphate (Ins(1,3,4,6)P4). Phosphorylates inositol 1,4,5,6-tetrakisphosphate (Ins(1,4,5,6)P4) (By similarity). Phosphorylates glycero-3-phospho-1D-myo-inositol 4,5-bisphosphate to glycero-3-phospho-1D-myo-inositol …

**Summary**, from NCBI Gene [253430](https://www.ncbi.nlm.nih.gov/gene/253430):

> This gene encodes a member of the inositol phosphokinase family. The encoded protein has 3-kinase, 5-kinase and 6-kinase activities on phosphorylated inositol substrates. The encoded protein plays an important role in the biosynthesis of inositol 1,3,4,5,6-pentakisphosphate, and has a preferred 5-kinase activity. This gene may play a role in nuclear mRNA export. Pseudogenes of this gene are located on the long arm of chromosome 13 and the short arm of chromosome 19. [provided by RefSeq, Dec …

**Accessions** — [HGNC:20739](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20739) · Entrez [253430](https://www.ncbi.nlm.nih.gov/gene/253430) · UniProt [Q8NFU5](https://www.uniprot.org/uniprotkb/Q8NFU5) · Ensembl [ENSG00000151151](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151151)

## Data

Gene col 7492: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7492); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7492, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7492]; `tensor/DDL_lfc|DDL_z.npy` [7492]; `embed/gene_vectors.npy` [7492]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7492 or target_col == 7492). Every well: [[IPMK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IPMK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
