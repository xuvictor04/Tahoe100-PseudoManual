---
symbol: "AHCTF1"
type: "gene"
col: 7701
ensembl_id: "ENSG00000153207"
name: "AT-hook containing transcription factor 1"
location: "1q44"
module: 33
arm: "+"
pooled_cpm: 133.82
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 3
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# AHCTF1

*AT-hook containing transcription factor 1* — 1q44

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.01× (z +15.4, q 0e+00, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.489× (z -10.8, q 2e-24, down in 39 of 44 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 8 lines (C-33 A 0.0628×, HEC-1-A 0.103×, A-172 0.274×, SK-MEL-2 0.269×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (C32 0.225×, A498 0.281×, HOP62 0.350×, NCI-H460 0.351×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (SNU-1 0.197×, A498 0.298×, NCI-H2347 0.319×; ⚠ toxic; transcription drop); [[Capmatinib (drug)]] 5 µM in 1 line (SW 1271 0.0483×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PMS1]] (+0.69, fdr 7e-06), [[MCMBP]] (+0.69, fdr 7e-06), [[UTP18]] (+0.69, fdr 7e-06); moves opposite to [[ATP6V1D]] (-0.61, fdr 7e-06), [[CD63]] (-0.61, fdr 1e-05), [[MICU1]] (-0.56, fdr 2e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CDCA7]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7701.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.01×** | +15.4 | 0e+00 | 40/48 (C32, COLO 205, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.92×** | +10.1 | 1e-21 | 45/48 (LS 180, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **3.31×** | +9.8 | 3e-20 | 47/48 (RKO, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **3.04×** | +9.1 | 2e-17 | 44/49 (COLO 205, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.81×** | +8.9 | 7e-17 | 43/47 (NCI-H460, COLO 205, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.68×** | +8.1 | 5e-14 | 43/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.58×** | +7.1 | 7e-11 | 40/48 (C32, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.54×** | +6.7 | 1e-09 | 37/48 (LS 180, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.53×** | +6.6 | 2e-09 | 38/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.51×** | +6.4 | 9e-09 | 39/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.43×** | +5.3 | 6e-06 | 32/48 (COLO 205, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.41×** | +5.3 | 6e-06 | 38/48 (Hs 766T, NCI-H460, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.32×** | +4.3 | 7e-04 | 29/47 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.32×** | +4.3 | 8e-04 | 25/48 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.31×** | +4.0 | 0.003 | 32/48 (SNU-423, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **1.23×** | +3.2 | 0.038 | 24/48 (HEC-1-A, NCI-H1573, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.22×** | +3.0 | 0.069 | 21/48 (PANC-1, H4, …) | rises with dose |  |
| [[Tomivosertib (drug)]] 5 µM |  | **1.45×** | +3.0 | 0.073 | 20/48 (MIA PaCa-2, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7701.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 8 lines (C-33 A 0.0628×, HEC-1-A 0.103×, A-172 0.274×, SK-MEL-2 0.269×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (C32 0.225×, A498 0.281×, HOP62 0.350×, NCI-H460 0.351×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (SNU-1 0.197×, A498 0.298×, NCI-H2347 0.319×; ⚠ toxic; transcription drop); [[Capmatinib (drug)]] 5 µM in 1 line (SW 1271 0.0483×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.489×** | -10.8 | 2e-24 | 39/44 (C-33 A, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.538×** | -9.7 | 7e-20 | 40/49 (C32, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.587×** | -7.7 | 2e-12 | 36/45 (SNU-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Carbamazepine (drug)]] 5 µM |  | 0.815× | -3.2 | 0.16 | 21/47 (CFPAC-1, A549, …) | top dose only |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | 0.748× | -3.2 | 0.16 | 25/48 (CHP-212, SNU-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.871× | -3.1 | 0.17 | 19/48 (A498, SW1417, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.873× | -3.1 | 0.17 | 18/49 (SK-MEL-2, A549, …) | top dose only |  |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.827× | -3.0 | 0.17 | 22/48 (AsPC-1, HEC-1-A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7701. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 189 | 6 (3 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +14.2) | [[Dinaciclib (drug)]] 0.5 µM 0.351× (z -10.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 106 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +13.9) | — |
| [[LoVo (line)]] | wt | 95.1 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +18.6) | — |
| [[NCI-H1573 (line)]] | alt | 98.8 | 6 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +17.3) | [[Dinaciclib (drug)]] 5 µM 0.346× (z -10.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 135 | 6 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.03× (z +13.4) | [[Dinaciclib (drug)]] 0.5 µM 0.493× (z -8.6) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 57.9 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.60× (z +18.9) | — |
| [[LS 180 (line)]] | wt | 97.3 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.10× (z +15.9) | — |
| [[A-427 (line)]] | wt | 149 | 2 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 6.14× (z +11.0) | [[Dinaciclib (drug)]] 0.05 µM 0.439× (z -8.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 216 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +14.4) | [[Dinaciclib (drug)]] 0.5 µM 0.281× (z -14.7) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 114 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.49× (z +21.4) | [[Dinaciclib (drug)]] 0.5 µM 0.225× (z -15.2) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 227 | 2 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 8.19× (z +11.1) | [[Dinaciclib (drug)]] 0.05 µM 0.352× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 49.7 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +16.8) | — |
| [[A549 (line)]] | wt | 137 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.217× (z -13.7) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 332 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +13.4) | — |
| [[HEC-1-A (line)]] | alt | 160 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.103× (z -21.2) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 114 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +12.2) | [[Dinaciclib (drug)]] 0.5 µM 0.350× (z -12.2) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 94.9 | 3 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.00× (z +10.7) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.00× (z +9.5) | — |
| [[hTERT-HPNE (line)]] | wt | 80.3 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.77× (z +15.8) | [[Dinaciclib (drug)]] 0.5 µM 0.308× (z -9.9) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 149 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +10.7) | [[Dinaciclib (drug)]] 0.05 µM 0.319× (z -11.4) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 122 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.346× (z -10.7) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 150 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.63× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.360× (z -10.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 180 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.269× (z -14.1) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 173 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 4.18× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.293× (z -10.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 142 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.274× (z -14.4) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 75.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.88× (z +18.5) | — |
| [[H4 (line)]] | wt | 93.0 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.15× (z +9.4) | — |
| [[KATO III (line)]] | alt | 54.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.319× (z -10.5) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 115 | 1 | 1 (1 ⚠) | [[Digitoxin (drug)]] 0.5 µM 2.39× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.307× (z -11.8) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 148 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +16.1) | — |
| [[SNU-1 (line)]] | wt | 180 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.197× (z -13.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 96.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +13.3) | — |
| [[SW 900 (line)]] | alt | 172 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +12.5) | [[Dinaciclib (drug)]] 0.05 µM 0.297× (z -10.5) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 140 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +12.5) | [[Dinaciclib (drug)]] 0.5 µM 0.413× (z -9.3) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 183 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0628× (z -27.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 90.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +13.1) | — |
| [[J82 (line)]] | alt | 136 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.45× (z +9.5) ⚠ toxic | — |
| [[LOX-IMVI (line)]] | wt | 123 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 3.52× (z +9.9) | — |
| [[NCI-H2030 (line)]] | alt | 140 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.317× (z -9.0) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 101 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +14.2) | — |
| [[SW 1088 (line)]] | alt | 95.7 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.0710× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 1271 (line)]] | alt | 285 | 0 | 1 | — | [[Capmatinib (drug)]] 5 µM 0.0483× (z -9.7) |
| [[AN3 CA (line)]] | alt | 171 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 170 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 95.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 105 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 208 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7701), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PMS1]] | +0.69 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[MCMBP]] | +0.69 | +0.73 / +0.58 | both halves | 7e-06 |  |
| [[UTP18]] | +0.69 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[DKC1]] | +0.67 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[UCK2]] | +0.66 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[MACIR]] | +0.65 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[POLR1B]] | +0.64 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[RIOX2]] | +0.63 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[NSUN2]] | +0.63 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[ABCC4]] | +0.63 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[LDLRAD3]] | +0.63 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[GMPS]] | +0.63 | +0.64 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP6V1D]] | -0.61 | -0.58 / -0.59 | both halves | 7e-06 |  |
| [[CD63]] | -0.61 | -0.56 / -0.64 | both halves | 1e-05 |  |
| [[MICU1]] | -0.56 | -0.62 / -0.47 | both halves | 2e-05 |  |
| [[HLA-A]] | -0.54 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[KIAA1217]] | -0.54 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[ATP6V0C]] | -0.53 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[RNASEK]] | -0.53 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[ATP6V1G1]] | -0.53 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[MXD1]] | -0.53 | -0.42 / -0.62 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDCA7]] | B | CDCA7 activity raises AHCTF1's level | lines that do not express CDCA7 (6) vs lines expressing it (44) | 1.46× lower at baseline in the lines without CDCA7 | 0.080 | ⚠ within organs, on part of the lines; also absent: PKMYT1, CHD7, CYP2R1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.674). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-11.5, -39.0); signed map (-6.0, -52.3). **Vector** length 80.8, 27.9% of its response variance represented; |z| ≥ 3 in 1,187 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Major pathway of rRNA processing in the nucleolus and cytosol* (reactome, mean cos +0.55 to 10); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.55 to 10); *rRNA modification in the nucleus and cytosol* (reactome, mean cos +0.58 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +5.9 | +8.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +1.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.0 | -0.3 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +2.6 | +2.2 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +2.4 | +2.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.4 | -0.1 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.7 | +10.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.9 | +6.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.6 | +6.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.5 | +8.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | -3.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | +3.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.5 | -2.6 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.4 | -0.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.3 | +0.5 |

## What is on record

|  |  |
|---|---|
| Name | AT-hook containing transcription factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q44 — chr1:246,839,098-246,931,948 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ELYS |
| Gene groups (HGNC) | Nucleoporins |
| Reactome | 19 pathways, smallest: Postmitotic nuclear pore complex (NPC) reformation; Nuclear Envelope (NE) Reassembly; Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WYP5](https://www.uniprot.org/uniprotkb/Q8WYP5) (Protein ELYS):

> Required for the assembly of a functional nuclear pore complex (NPC) on the surface of chromosomes as nuclei form at the end of mitosis. May initiate NPC assembly by binding to chromatin and recruiting the Nup107-160 subcomplex of the NPC. Also required for the localization of the Nup107-160 subcomplex of the NPC to the kinetochore during mitosis and for the completion of cytokinesis.

**Summary**, from NCBI Gene [25909](https://www.ncbi.nlm.nih.gov/gene/25909):

> Predicted to enable DNA binding activity. Involved in nuclear pore complex assembly and regulation of cytokinesis. Located in chromosome; nuclear body; and nuclear envelope. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24618](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24618) · Entrez [25909](https://www.ncbi.nlm.nih.gov/gene/25909) · UniProt [Q8WYP5](https://www.uniprot.org/uniprotkb/Q8WYP5) · Ensembl [ENSG00000153207](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153207)

## Data

Gene col 7701: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7701); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7701, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7701]; `tensor/DDL_lfc|DDL_z.npy` [7701]; `embed/gene_vectors.npy` [7701]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7701 or target_col == 7701). Every well: [[AHCTF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AHCTF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
