---
symbol: "HAT1"
type: "gene"
col: 4915
ensembl_id: "ENSG00000128708"
name: "histone acetyltransferase 1"
location: "2q31.1"
module: 6
arm: "+"
pooled_cpm: 56.28
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 6
n_dd_up_clean: 4
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# HAT1

*histone acetyltransferase 1* — 2q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (19 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 5.77× (z +19.5, q 0e+00, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.767× (z -8.1, q 5e-13, down in 33 of 48 measured lines) ⚠ cell-cycle shift, explains ~63% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.782× (z -7.4, q 3e-11, down in 30 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 5 lines (A498 0.437×, A-427 0.382×, A-172 0.432×, AsPC-1 0.471×, …; ⚠ cell-cycle shift, explains ~63% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (A-427 0.359×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Selinexor (drug)]] 0.5 µM in 1 line (A498 0.460×; ⚠ cell-cycle shift, explains ~73% of this change); [[Tucidinostat (drug)]] 5 µM in 1 line (RPMI-7951 0.469×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TCF19]] (+0.79, fdr 7e-06), [[GINS2]] (+0.79, fdr 7e-06), [[TK1]] (+0.78, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 26 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4915.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **5.77×** | +19.5 | 0e+00 | 48/49 (PANC-1, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **2.29×** | +17.6 | 0e+00 | 45/47 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **2.16×** | +16.4 | 0e+00 | 47/48 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **2.05×** | +15.3 | 0e+00 | 48/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.99×** | +14.7 | 0e+00 | 47/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.95×** | +14.3 | 3e-44 | 47/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **3.39×** | +13.6 | 3e-40 | 40/48 (SW480, LOX-IMVI, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.76×** | +12.1 | 1e-31 | 40/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.72×** | +11.5 | 5e-29 | 41/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | **1.71×** | +11.0 | 4e-26 | 42/47 (LoVo, NCI-H460, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.42×** | +7.1 | 5e-11 | 27/48 (NCI-H460, MIA PaCa-2, …) | top dose only | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.42×** | +6.9 | 2e-10 | 26/44 (MIA PaCa-2, NCI-H23, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.38×** | +6.6 | 2e-09 | 23/41 (KATO III, SNU-423, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | **1.23×** | +6.1 | 4e-08 | 23/48 (AsPC-1, A549, …) | top dose only | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **1.33×** | +5.9 | 2e-07 | 29/48 (RPMI-7951, RKO, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.29×** | +5.4 | 2e-06 | 26/48 (SW480, LoVo, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.28×** | +5.2 | 5e-06 | 25/48 (LoVo, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4915.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 5 lines (A498 0.437×, A-427 0.382×, A-172 0.432×, AsPC-1 0.471×, …; ⚠ cell-cycle shift, explains ~63% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (A-427 0.359×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Selinexor (drug)]] 0.5 µM in 1 line (A498 0.460×; ⚠ cell-cycle shift, explains ~73% of this change); [[Tucidinostat (drug)]] 5 µM in 1 line (RPMI-7951 0.469×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.767×** | -8.1 | 5e-13 | 33/48 (A498, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.782×** | -7.4 | 3e-11 | 30/48 (RPMI-7951, NCI-H1573, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **0.721×** | -7.0 | 5e-10 | 35/48 (A498, A-427, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.764×** | -5.8 | 1e-06 | 27/48 (RPMI-7951, LS 180, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.792×** | -5.0 | 7e-05 | 25/48 (RPMI-7951, PANC-1, …) | all doses, stronger at high dose |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.838× | -3.8 | 0.014 | 15/48 (KATO III, SW480, …) | top dose only |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.841× | -3.7 | 0.016 | 8/48 (PANC-1, SW480, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.890× | -3.5 | 0.028 | 16/48 (H4, Hs 766T, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.734×** | -3.5 | 0.031 | 11/49 (A-427, HEC-1-A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | 0.841× | -3.5 | 0.031 | 17/49 (A-427, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Rapamycin (drug)]] 0.5 µM |  | 0.856× | -3.3 | 0.045 | 13/48 (LOX-IMVI, PANC-1, …) | all doses, flat |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | 0.864× | -3.1 | 0.079 | 14/47 (RPMI-7951, H4, …) | all doses, flat |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~96% of this change | 0.860× | -3.1 | 0.097 | 9/48 (LOX-IMVI, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.66 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4915. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 47.1 | 13 (12 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.57× (z +20.3) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 7.45× (z +11.3) | — |
| [[SW480 (line)]] | alt | 61.2 | 9 (7 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.23× (z +17.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 7.65× (z +12.9) | — |
| [[AsPC-1 (line)]] | alt | 71.6 | 7 (6 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 8.85× (z +21.0) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 7.42× (z +10.1) | [[Selinexor (drug)]] 5 µM 0.471× (z -10.2) ⚠ cell-cycle shift, explains ~63% of this change |
| [[LoVo (line)]] | wt | 31.5 | 7 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.40× (z +12.7) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.44× (z +10.1) | — |
| [[LOX-IMVI (line)]] | wt | 41.1 | 7 (5 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 17.3× (z +12.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 46.3 | 6 (5 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.54× (z +11.1) ⚠ cell-cycle shift, explains ~65% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 10.4× (z +10.8) | — |
| [[PANC-1 (line)]] | alt | 65.3 | 6 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.75× (z +19.3) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 8.77× (z +14.1) | — |
| [[A549 (line)]] | wt | 40.5 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +11.1) ⚠ cell-cycle shift, explains ~85% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.96× (z +8.5) | — |
| [[BT-474 (line)]] | alt | 48.3 | 4 (4 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.49× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[RKO (line)]] | wt | 60.7 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +11.1) ⚠ cell-cycle shift, explains ~85% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 8.87× (z +9.5) | — |
| [[J82 (line)]] | alt | 81.7 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.67× (z +12.4) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.98× (z +9.1) | — |
| [[NCI-H1573 (line)]] | alt | 65.6 | 2 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.39× (z +11.2) ⚠ cell-cycle shift, explains ~36% of this change | [[Selinexor (drug)]] 5 µM 0.522× (z -8.5) ⚠ cell-cycle shift, explains ~63% of this change |
| [[NCI-H23 (line)]] | alt | 108 | 3 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.52× (z +11.1) | — |
| [[A-172 (line)]] | wt | 47.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.54× (z +8.8) ⚠ cell-cycle shift, explains ~54% of this change | [[Selinexor (drug)]] 5 µM 0.432× (z -11.3) ⚠ cell-cycle shift, explains ~63% of this change |
| [[A-427 (line)]] | wt | 82.4 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.382× (z -13.4) ⚠ cell-cycle shift, explains ~63% of this change |
| [[A498 (line)]] | wt | 103 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.437× (z -14.4) ⚠ cell-cycle shift, explains ~63% of this change |
| [[HEC-1-A (line)]] | alt | 67.3 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 5.66× (z +10.7) | — |
| [[HepG2_C3A (line)]] | wt | 46.5 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.32× (z +8.9) ⚠ cell-cycle shift, explains ~54% of this change | — |
| [[HOP62 (line)]] | alt | 47.3 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.55× (z +11.0) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[KATO III (line)]] | alt | 43.4 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.70× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.32× (z +8.6) | — |
| [[LS 180 (line)]] | wt | 34.0 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.38× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[RPMI-7951 (line)]] | alt | 54.5 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 7.26× (z +8.8) | [[Tucidinostat (drug)]] 5 µM 0.469× (z -9.2) |
| [[SNU-1 (line)]] | wt | 45.3 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.12× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[SW 900 (line)]] | alt | 56.3 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.43× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[SW1417 (line)]] | alt | 74.4 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.86× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.417× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 80.7 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.59× (z +8.9) | — |
| [[CFPAC-1 (line)]] | alt | 39.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.26× (z +9.3) | — |
| [[COLO 205 (line)]] | alt | 42.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 13.6× (z +10.1) | — |
| [[HT-29 (line)]] | alt | 43.3 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.79× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[NCI-H2030 (line)]] | alt | 95.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.332× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 45.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.35× (z +8.9) | — |
| [[AN3 CA (line)]] | alt | 89.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 43.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 43.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 67.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 51.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4915), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCF19]] | +0.79 | +0.76 / +0.73 | both halves | 7e-06 |  |
| [[GINS2]] | +0.79 | +0.79 / +0.71 | both halves | 7e-06 |  |
| [[TK1]] | +0.78 | +0.76 / +0.75 | both halves | 7e-06 |  |
| [[CDC45]] | +0.78 | +0.73 / +0.78 | both halves | 7e-06 |  |
| [[RAD54L]] | +0.78 | +0.81 / +0.71 | both halves | 7e-06 |  |
| [[PCLAF]] | +0.78 | +0.78 / +0.76 | both halves | 7e-06 |  |
| [[MMS22L]] | +0.77 | +0.74 / +0.75 | both halves | 7e-06 |  |
| [[NCAPD3]] | +0.77 | +0.69 / +0.76 | both halves | 7e-06 |  |
| [[WDR76]] | +0.77 | +0.73 / +0.76 | both halves | 7e-06 |  |
| [[EXO1]] | +0.77 | +0.75 / +0.73 | both halves | 7e-06 |  |
| [[DTL]] | +0.77 | +0.76 / +0.75 | both halves | 7e-06 |  |
| [[ZGRF1]] | +0.76 | +0.72 / +0.77 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.791). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-34.1, -45.1); signed map (-37.8, -43.9). **Vector** length 98.9, 29.8% of its response variance represented; |z| ≥ 3 in 1,357 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.59 to 65); *DNA strand elongation* (reactome, mean cos +0.63 to 28); *DNA Replication* (reactome, mean cos +0.63 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.5 | +19.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | +4.3 | +14.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | +4.0 | +15.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +3.8 | +6.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | +3.8 | +14.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | +13.6 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +1.9 | +0.6 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.8 | +0.6 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +1.8 | +0.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.8 | +2.8 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | -7.9 | -8.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -7.6 | +1.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~73% of this change | -6.1 | -7.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.5 | -7.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | -5.2 | +6.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.8 | -2.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.6 | -0.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.2 | -1.7 |
|  | [[EX229 (drug)]] 5 µM |  | -2.6 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | histone acetyltransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q31.1 — chr2:171,922,448-171,983,686 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KAT1 |
| Gene groups (HGNC) | Lysine acetyltransferases |
| Reactome | 3 pathways, smallest: HATs acetylate histones; Chromatin modifying enzymes; Chromatin organization |
| Matched by | ensembl_id |

**Function**, from UniProt [O14929](https://www.uniprot.org/uniprotkb/O14929) (Histone acetyltransferase type B catalytic subunit):

> Histone acetyltransferase that plays a role in different biological processes including cell cycle progression, glucose metabolism, histone production or DNA damage repair. Coordinates histone production and acetylation via H4 promoter binding. Acetylates histone H4 at 'Lys-5' (H4K5ac) and 'Lys-12' (H4K12ac) and, to a lesser extent, histone H2A at 'Lys-5' (H2AK5ac). Drives H4 production by chromatin binding to support chromatin replication and acetylation. Since transcription of H4 genes is …

**Summary**, from NCBI Gene [8520](https://www.ncbi.nlm.nih.gov/gene/8520):

> The protein encoded by this gene is a type B histone acetyltransferase (HAT) that is involved in the rapid acetylation of newly synthesized cytoplasmic histones, which are in turn imported into the nucleus for de novo deposition onto nascent DNA chains. Histone acetylation, particularly of histone H4, plays an important role in replication-dependent chromatin assembly. Specifically, this HAT can acetylate soluble but not nucleosomal histone H4 at lysines 5 and 12, and to a lesser degree, …

**Accessions** — [HGNC:4821](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4821) · Entrez [8520](https://www.ncbi.nlm.nih.gov/gene/8520) · UniProt [O14929](https://www.uniprot.org/uniprotkb/O14929) · Ensembl [ENSG00000128708](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128708)

## Data

Gene col 4915: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4915); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4915, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4915]; `tensor/DDL_lfc|DDL_z.npy` [4915]; `embed/gene_vectors.npy` [4915]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4915 or target_col == 4915). Every well: [[HAT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HAT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
