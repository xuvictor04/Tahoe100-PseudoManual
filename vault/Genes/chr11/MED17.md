---
symbol: "MED17"
type: "gene"
col: 485
ensembl_id: "ENSG00000042429"
name: "mediator complex subunit 17"
location: "11q21"
module: 168
arm: "+"
pooled_cpm: 56.46
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 4
n_dd_up_clean: 16
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/168"]
generated_by: "tahoemap"
---

# MED17

*mediator complex subunit 17* — 11q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (11 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 8.74× (z +18.7, q 0e+00, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.368× (z -16.5, q 0e+00, down in 46 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 0.783× (z -3.9, q 0.012, down in 24 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (SW480 0.156×, SHP-77 0.0936×, HepG2/C3A 0.0603×, NCI-H2347 0.187×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 7 lines (J82 0.112×, NCI-H2347 0.145×, RKO 0.123×, SW 900 0.115×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H2347 0.130×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Temsirolimus (drug)]] 0.5 µM in 1 line (Hs 766T 0.351×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NUP54]] (+0.78, fdr 7e-06), [[MFSD14CP]] (+0.77, fdr 7e-06), [[NDUFAF7]] (+0.73, fdr 7e-06); moves opposite to [[DCAF8]] (-0.62, fdr 1e-05), [[TIA1]] (-0.60, fdr 1e-05), [[THAP5]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 168]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 13 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 485.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **8.74×** | +18.7 | 0e+00 | 48/49 (SW480, PANC-1, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **6.01×** | +15.5 | 0e+00 | 48/48 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.79×** | +9.6 | 2e-19 | 36/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.49×** | +6.6 | 6e-09 | 32/48 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +6.2 | 8e-08 | 31/47 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.01×** | +6.0 | 2e-07 | 26/35 (SW480, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.43×** | +5.9 | 3e-07 | 29/48 (KATO III, LoVo, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.43×** | +5.9 | 3e-07 | 31/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +5.5 | 2e-06 | 29/47 (NCI-H2030, SW1417, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.25×** | +5.2 | 1e-05 | 24/48 (PANC-1, SNU-423, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.37×** | +5.2 | 1e-05 | 30/48 (SW1417, RKO, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.36×** | +5.1 | 2e-05 | 28/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.20×** | +4.3 | 6e-04 | 19/49 (CFPAC-1, HT-29, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.29×** | +4.2 | 0.001 | 24/48 (NCI-H1792, RKO, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.29×** | +4.2 | 0.001 | 25/48 (NCI-H23, RKO, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.25×** | +3.7 | 0.007 | 22/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.32×** | +3.3 | 0.026 | 16/49 (PANC-1, SW1417, …) | all doses, flat | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.23×** | +3.3 | 0.027 | 21/47 (SW48, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.22×** | +3.2 | 0.032 | 21/48 (CFPAC-1, COLO 205, …) | rises with dose |  |
| [[Tomivosertib (drug)]] 5 µM |  | **1.44×** | +3.2 | 0.037 | 14/48 (HEC-1-A, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.21×** | +3.1 | 0.042 | 21/48 (SW480, LoVo, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.5 µM |  | **1.30×** | +3.1 | 0.047 | 15/48 (SW480, PANC-1, …) | all doses, stronger at high dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 485.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (SW480 0.156×, SHP-77 0.0936×, HepG2/C3A 0.0603×, NCI-H2347 0.187×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 7 lines (J82 0.112×, NCI-H2347 0.145×, RKO 0.123×, SW 900 0.115×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H2347 0.130×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Temsirolimus (drug)]] 0.5 µM in 1 line (Hs 766T 0.351×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.368×** | -16.5 | 0e+00 | 46/49 (J82, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.359×** | -16.2 | 0e+00 | 39/42 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.924× | -4.7 | 6e-04 | 1/49 (NCI-H23) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.790×** | -3.9 | 0.012 | 24/48 (CHP-212, SNU-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.783×** | -3.9 | 0.012 | 24/48 (NCI-H2347, NCI-H2030, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.856× | -3.2 | 0.13 | 17/48 (SW480, PANC-1, …) | two highest doses | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.825× | -3.2 | 0.13 | 16/49 (SK-MEL-2, NCI-H2347, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.830× | -3.1 | 0.14 | 10/48 (A498, LS 180, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | 0.831× | -3.1 | 0.14 | 19/48 (NCI-H2347, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 485. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 80.4 | 8 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 14.9× (z +20.2) | [[Dinaciclib (drug)]] 5 µM 0.156× (z -25.4) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 56.5 | 6 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 13.1× (z +13.5) | [[Dinaciclib (drug)]] 5 µM 0.394× (z -9.0) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 45.2 | 7 (2 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 3.65× (z +12.4) | — |
| [[PANC-1 (line)]] | alt | 56.4 | 6 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 14.0× (z +17.1) | [[Dinaciclib (drug)]] 0.5 µM 0.454× (z -9.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 59.5 | 3 (1 ⚠) | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 12.2× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.217× (z -14.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 43.1 | 6 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 14.0× (z +13.5) | — |
| [[LS 180 (line)]] | wt | 60.9 | 4 (1 ⚠) | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 12.4× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.246× (z -11.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 60.7 | 4 (2 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 10.5× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.205× (z -12.4) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 65.6 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.56× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.112× (z -23.6) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 67.4 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 13.9× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.159× (z -14.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 76.7 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 20.1× (z +14.5) | [[Dinaciclib (drug)]] 0.5 µM 0.345× (z -9.9) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 37.7 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 17.5× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.132× (z -13.6) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 46.1 | 4 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 11.4× (z +11.8) | — |
| [[SW 900 (line)]] | alt | 67.0 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 8.74× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.115× (z -19.2) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 47.1 | 3 | 0 | [[PH-797804 (drug)]] 5 µM 11.2× (z +11.0) | — |
| [[C-33 A (line)]] | alt | 82.4 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.87× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.130× (z -17.1) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 44.1 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.06× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.359× (z -8.9) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 48.4 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 10.7× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.261× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Temsirolimus (drug)]] 0.5 µM 0.351× (z -8.6) |
| [[NCI-H2347 (line)]] | alt | 86.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.145× (z -20.7) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 71.9 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 12.4× (z +12.9) | [[Dinaciclib (drug)]] 0.5 µM 0.123× (z -20.5) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 82.1 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 8.90× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.0936× (z -23.3) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 81.6 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 8.62× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.195× (z -16.5) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 71.5 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 8.37× (z +13.2) | [[Dinaciclib (drug)]] 5 µM 0.264× (z -8.5) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 44.5 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 9.76× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.213× (z -11.8) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 55.4 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 9.60× (z +10.2) | — |
| [[CFPAC-1 (line)]] | alt | 63.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.234× (z -11.5) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 36.3 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 21.9× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -9.8) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 57.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.198× (z -12.8) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 51.2 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 9.20× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.325× (z -9.0) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 46.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.132× (z -13.7) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 48.2 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 11.2× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.243× (z -10.2) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 85.3 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 11.0× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.144× (z -14.4) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 105 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CHP-212 (line)]] | wt | 76.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.104× (z -11.3) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 73.2 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 10.3× (z +8.9) | — |
| [[HepG2_C3A (line)]] | wt | 44.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0603× (z -19.4) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 44.0 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 8.05× (z +8.7) | — |
| [[RPMI-7951 (line)]] | alt | 59.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.358× (z -9.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 28.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 11.3× (z +8.6) | — |
| [[SNU-423 (line)]] | alt | 54.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.368× (z -8.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 57.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 57.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 57.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 67.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 69.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 55.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 140 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 485), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUP54]] | +0.78 | +0.78 / +0.71 | both halves | 7e-06 |  |
| [[MFSD14CP]] | +0.77 | +0.78 / +0.67 | both halves | 7e-06 |  |
| [[NDUFAF7]] | +0.73 | +0.74 / +0.66 | both halves | 7e-06 |  |
| [[USPL1]] | +0.73 | +0.79 / +0.61 | both halves | 7e-06 |  |
| [[FOXJ3]] | +0.70 | +0.78 / +0.59 | both halves | 7e-06 |  |
| [[RNF4]] | +0.70 | +0.78 / +0.57 | both halves | 1e-05 |  |
| [[SNX1]] | +0.68 | +0.77 / +0.65 | both halves | 7e-06 |  |
| [[SEC11A]] | +0.68 | +0.76 / +0.57 | both halves | 9e-06 | pathway: Respiratory Syncytial Virus Infection Pathway |
| [[GFOD2]] | +0.68 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[SDHAP4-1]] | +0.67 | +0.69 / +0.57 | both halves | 1e-05 |  |
| [[ASB7]] | +0.66 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[FAM104A]] | +0.66 | +0.66 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCAF8]] | -0.62 | -0.64 / -0.51 | both halves | 1e-05 |  |
| [[TIA1]] | -0.60 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[THAP5]] | -0.60 | -0.66 / -0.53 | both halves | 1e-05 |  |
| [[AKT1S1]] | -0.59 | -0.70 / -0.48 | both halves | 2e-05 |  |
| [[ZC3H11A]] | -0.58 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[LZIC]] | -0.58 | -0.63 / -0.48 | both halves | 2e-05 |  |
| [[JUN]] | -0.57 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[CPSF2]] | -0.57 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[ARCN1]] | -0.57 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[SKIL]] | -0.57 | -0.61 / -0.45 | both halves | 3e-05 |  |
| [[ERCC6L2]] | -0.56 | -0.69 / -0.40 | both halves | 5e-05 |  |
| [[CUX1]] | -0.55 | -0.51 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 168]]; 25 genes; this gene is in the **+** arm (projection on the module's main direction 0.769). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-3.5, -14.0); signed map (-35.2, -9.1). **Vector** length 104, 30.7% of its response variance represented; |z| ≥ 3 in 1,034 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +6.8 | +5.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.7 | +5.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.8 | +18.7 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +5.2 | +6.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.1 | +15.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +0.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.2 | +0.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.6 | +1.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | -0.3 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -8.1 | -0.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -7.8 | -0.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.4 | -3.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -7.1 | -1.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.6 | +6.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.8 | -2.7 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.5 | -0.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.2 | +0.6 |
|  | [[Methylthiouracil (drug)]] 5 µM |  | -2.2 | -2.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.9 | -0.0 |

## What is on record

|  |  |
|---|---|
| Name | mediator complex subunit 17 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q21 — chr11:93,784,227-93,814,963 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CRSP77, TRAP80, DRIP80, SRB4; previously CRSP6 |
| Gene groups (HGNC) | Mediator complex |
| Reactome | 13 pathways, smallest: Transcriptional regulation of white adipocyte differentiation; RSV-host interactions; Epigenetic regulation of adipogenesis genes by MLL3 and MLL4 complexes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NVC6](https://www.uniprot.org/uniprotkb/Q9NVC6) (Mediator of RNA polymerase II transcription subunit 17):

> Component of the Mediator complex, a coactivator involved in the regulated transcription of nearly all RNA polymerase II-dependent genes. Mediator functions as a bridge to convey information from gene-specific regulatory proteins to the basal RNA polymerase II transcription machinery. Mediator is recruited to promoters by direct interactions with regulatory proteins and serves as a scaffold for the assembly of a functional pre-initiation complex with RNA polymerase II and the general …

**Summary**, from NCBI Gene [9440](https://www.ncbi.nlm.nih.gov/gene/9440):

> The activation of gene transcription is a multistep process that is triggered by factors that recognize transcriptional enhancer sites in DNA. These factors work with co-activators to direct transcriptional initiation by the RNA polymerase II apparatus. The protein encoded by this gene is a subunit of the CRSP (cofactor required for SP1 activation) complex, which, along with TFIID, is required for efficient activation by SP1. This protein is also a component of other multisubunit complexes e.g. …

**Accessions** — [HGNC:2375](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2375) · Entrez [9440](https://www.ncbi.nlm.nih.gov/gene/9440) · UniProt [Q9NVC6](https://www.uniprot.org/uniprotkb/Q9NVC6) · Ensembl [ENSG00000042429](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000042429)

## Data

Gene col 485: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 485); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 485, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 485]; `tensor/DDL_lfc|DDL_z.npy` [485]; `embed/gene_vectors.npy` [485]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 485 or target_col == 485). Every well: [[MED17 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MED17.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
