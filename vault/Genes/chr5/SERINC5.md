---
symbol: "SERINC5"
type: "gene"
col: 8922
ensembl_id: "ENSG00000164300"
name: "serine incorporator 5"
location: "5q14.1"
module: 11
arm: "-"
pooled_cpm: 165.38
n_lines_expressing: 49
n_dd_up: 12
n_dd_down: 6
n_dd_up_clean: 11
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 9
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# SERINC5

*serine incorporator 5* — 5q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.52× (z +53.5, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.680× (z -11.6, q 2e-28, down in 30 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC5A3]] (+0.53, fdr 3e-05), [[ETNK1]] (+0.52, fdr 4e-05), [[EPB41L5]] (+0.52, fdr 2e-05); moves opposite to [[RBAK]] (-0.56, fdr 1e-05), [[ZNF510]] (-0.54, fdr 3e-05), [[POLI]] (-0.54, fdr 1e-05).
> It sits in the **-** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[TMPRSS2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 17 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8922.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.52×** | +53.5 | 0e+00 | 44/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.14×** | +22.0 | 0e+00 | 41/47 (NCI-H460, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.01×** | +20.1 | 0e+00 | 40/49 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.38×** | +13.8 | 4e-41 | 27/47 (HOP62, HEC-1-A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.50×** | +12.2 | 2e-32 | 32/47 (NCI-H1573, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.32×** | +8.3 | 1e-14 | 26/47 (NCI-H1573, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | 1.19× | +7.5 | 5e-12 | 24/47 (COLO 205, AsPC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.27×** | +7.1 | 1e-10 | 23/47 (NCI-H2030, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.27×** | +6.8 | 7e-10 | 25/47 (AsPC-1, MIA PaCa-2, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.19× | +5.2 | 1e-05 | 21/48 (NCI-H1573, RKO, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.20× | +5.2 | 1e-05 | 17/41 (NCI-H1573, C-33 A, …) | rises with dose | composition shift |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 1.19× | +5.0 | 2e-05 | 17/46 (H4, HOP62, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~44% of this change | 1.18× | +5.0 | 2e-05 | 16/48 (LS 180, SW 900, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +4.9 | 3e-05 | 17/47 (BT-474, KATO III, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +4.8 | 7e-05 | 20/47 (BT-474, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Rapamycin (drug)]] 5 µM |  | 1.11× | +4.3 | 6e-04 | 4/47 (SK-MEL-2, RPMI-7951, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.42×** | +4.2 | 7e-04 | 8/49 (SW480, AsPC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.35×** | +3.6 | 0.008 | 6/47 (NCI-H2347, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[AZD-8055 (drug)]] 0.5 µM |  | 1.18× | +3.5 | 0.012 | 5/47 (SW480, A-427, …) | two highest doses | noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 1.12× | +3.4 | 0.014 | 10/47 (BT-474, SW1417, …) | top dose only |  |
| [[BAY1125976 (drug)]] 5 µM |  | **1.32×** | +3.4 | 0.015 | 6/47 (MIA PaCa-2, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.12× | +3.3 | 0.018 | 16/46 (LoVo, A-172, …) | rises with dose | low cells (technical?) |
| [[Temsirolimus (drug)]] 5 µM |  | 1.08× | +3.2 | 0.028 | 4/48 (RKO, NCI-H23, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8922.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.680×** | -11.6 | 2e-28 | 30/47 (LoVo, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.398×** | -11.1 | 3e-26 | 36/48 (LoVo, LS 180, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.732×** | -9.4 | 1e-18 | 29/47 (A-172, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.758×** | -8.0 | 2e-13 | 25/47 (LoVo, A-172, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.529×** | -7.7 | 2e-12 | 29/47 (RKO, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 0.854× | -4.8 | 2e-04 | 19/47 (COLO 205, SW1417, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~76% of this change | 0.860× | -4.5 | 5e-04 | 18/47 (KATO III, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[vincristine (drug)]] 0.5 µM |  | 0.836× | -3.9 | 0.008 | 15/47 (SW480, COLO 205, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.05 µM |  | 0.876× | -3.8 | 0.010 | 13/47 (SNU-1, Hs 766T, …) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.885× | -3.7 | 0.013 | 16/47 (H4, A498, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.887× | -3.6 | 0.016 | 15/47 (SW48, A-172, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.881× | -3.5 | 0.019 | 8/46 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.921× | -3.5 | 0.019 | 1/48 (AN3 CA) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.755×** | -3.4 | 0.028 | 9/47 (SW1417, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Raltitrexed (drug)]] 0.5 µM |  | 0.896× | -3.3 | 0.037 | 10/47 (NCI-H23, MIA PaCa-2, …) | rises with dose |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | 0.905× | -3.0 | 0.086 | 14/47 (SNU-423, HOP62, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 0.906× | -3.0 | 0.095 | 9/47 (HOP62, HS-578T, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8922. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 623 | 1 (1 ⚠) | 9 (3 ⚠) | [[Selinexor (drug)]] 5 µM 1.92× (z +11.0) ⚠ cell-cycle shift, explains ~63% of this change | [[Auranofin (drug)]] 5 µM 0.328× (z -13.2) |
| [[SW480 (line)]] | alt | 273 | 10 (1 ⚠) | 0 | [[Cobimetinib (drug)]] 5 µM 2.62× (z +11.8) | — |
| [[NCI-H1573 (line)]] | alt | 75.0 | 9 (6 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.87× (z +23.8) | — |
| [[A-172 (line)]] | wt | 141 | 3 | 4 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.54× (z +15.3) | [[Harringtonine (drug)]] 0.5 µM 0.307× (z -13.7) |
| [[SW48 (line)]] | wt | 563 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.459× (z -11.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.348× (z -11.0) |
| [[A549 (line)]] | wt | 73.3 | 3 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.26× (z +19.4) | [[Homoharringtonine (drug)]] 0.5 µM 0.457× (z -9.1) |
| [[BT-474 (line)]] | alt | 113 | 5 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +12.5) | — |
| [[H4 (line)]] | wt | 80.3 | 5 (2 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 8.16× (z +16.1) | — |
| [[J82 (line)]] | alt | 49.0 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.52× (z +21.5) | — |
| [[LOX-IMVI (line)]] | wt | 66.6 | 4 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.14× (z +27.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.446× (z -8.7) |
| [[MIA PaCa-2 (line)]] | alt | 104 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.31× (z +32.4) | — |
| [[SW1417 (line)]] | alt | 491 | 0 | 5 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.416× (z -13.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.500× (z -11.1) |
| [[HEC-1-A (line)]] | alt | 43.0 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.98× (z +29.0) | — |
| [[HOP62 (line)]] | alt | 59.1 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.21× (z +25.4) | — |
| [[HS-578T (line)]] | alt | 110 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +13.3) | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -15.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.404× (z -10.5) |
| [[LoVo (line)]] | wt | 635 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -18.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.277× (z -14.5) |
| [[NCI-H2347 (line)]] | alt | 239 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +18.1) | [[Dinaciclib (drug)]] 0.05 µM 0.442× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 131 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.54× (z +27.0) | [[Dinaciclib (drug)]] 0.5 µM 0.371× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 69.7 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.80× (z +26.9) | — |
| [[SNU-1 (line)]] | wt | 54.6 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.03× (z +18.2) | — |
| [[SW 900 (line)]] | alt | 83.3 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.80× (z +24.3) | — |
| [[A-427 (line)]] | wt | 98.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.513× (z -12.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.439× (z -10.6) |
| [[A498 (line)]] | wt | 122 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +18.6) | — |
| [[C-33 A (line)]] | alt | 77.0 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.51× (z +14.8) | — |
| [[C32 (line)]] | wt | 179 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.83× (z +15.4) | — |
| [[CFPAC-1 (line)]] | alt | 142 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.46× (z +25.3) | — |
| [[Hs 766T (line)]] | wt | 56.3 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.93× (z +23.0) | — |
| [[hTERT-HPNE (line)]] | wt | 72.2 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.59× (z +19.2) | — |
| [[LS 180 (line)]] | wt | 405 | 2 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.61× (z +9.0) | [[Homoharringtonine (drug)]] 0.5 µM 0.505× (z -9.1) |
| [[NCI-H460 (line)]] | wt | 52.2 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.34× (z +35.7) | — |
| [[RPMI-7951 (line)]] | alt | 44.5 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.82× (z +16.3) | — |
| [[SK-MEL-2 (line)]] | alt | 124 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.32× (z +13.3) | [[Harringtonine (drug)]] 5 µM 0.428× (z -9.1) ⚠ cell-cycle shift, explains ~51% of this change |
| [[SNU-423 (line)]] | alt | 131 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.35× (z +15.2) | — |
| [[AN3 CA (line)]] | alt | 93.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.90× (z +11.8) | — |
| [[AsPC-1 (line)]] | alt | 329 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +12.4) | — |
| [[CHP-212 (line)]] | wt | 93.4 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.64× (z +10.8) | [[Homoharringtonine (drug)]] 0.5 µM 0.224× (z -9.0) |
| [[HCT15 (line)]] | alt | 332 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -12.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.269× (z -11.9) |
| [[NCI-H23 (line)]] | alt | 54.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.18× (z +16.2) | — |
| [[HepG2_C3A (line)]] | wt | 120 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.99× (z +22.8) | — |
| [[HT-29 (line)]] | alt | 388 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.370× (z -10.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 65.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.74× (z +20.1) | — |
| [[NCI-H2030 (line)]] | alt | 61.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.46× (z +20.2) | — |
| [[PANC-1 (line)]] | alt | 118 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +15.7) | — |
| [[SW 1088 (line)]] | alt | 114 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.67× (z +8.7) | — |
| [[SW 1271 (line)]] | alt | 75.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.17× (z +9.4) | — |
| [[KATO III (line)]] | alt | 198 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 179 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 173 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 55.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 31.8 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8922), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*30 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC5A3]] | +0.53 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[ETNK1]] | +0.52 | +0.57 / +0.41 | both halves | 4e-05 |  |
| [[EPB41L5]] | +0.52 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[PEAK1]] | +0.51 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[BCL2L14]] | +0.51 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[ARL15]] | +0.50 | +0.55 / +0.36 | both halves | 1e-04 |  |
| [[ARHGAP21]] | +0.50 | +0.49 / +0.38 | both halves | 6e-05 |  |
| [[TMPRSS2]] | +0.50 | +0.46 / +0.52 | both halves | 3e-05 |  |
| [[CD9]] | +0.49 | +0.43 / +0.48 | both halves | 3e-05 |  |
| [[CTBP2]] | +0.48 | +0.36 / +0.52 | both halves | 9e-05 |  |
| [[YPEL5]] | +0.46 | +0.42 / +0.41 | both halves | 4e-05 |  |
| [[RNF38]] | +0.46 | +0.42 / +0.47 | both halves | 4e-05 |  |

## Genes that move opposite

*70 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBAK]] | -0.56 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[ZNF510]] | -0.54 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[POLI]] | -0.54 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[KBTBD6]] | -0.52 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[ZNF23]] | -0.51 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[MSL3P1]] | -0.51 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[AGGF1]] | -0.50 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[ZNF180]] | -0.50 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[THUMPD3]] | -0.50 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[ZNF155]] | -0.49 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[RANBP6]] | -0.49 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[ZNF22]] | -0.49 | -0.45 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 5, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMPRSS2]] | B | TMPRSS2 activity raises SERINC5's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 2.81× lower at baseline in the lines without TMPRSS2 | 0.002 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6 |
| [[CDHR2]] | B | CDHR2 activity raises SERINC5's level | lines that do not express CDHR2 (30) vs lines expressing it (20) | 2.19× lower at baseline in the lines without CDHR2 | 0.008 | ⚠ within organs, on part of the lines; also absent: VIL1, NPSR1-AS1, EPS8L3; maybe low, not absent |
| [[MUC13]] | B | MUC13 activity raises SERINC5's level | lines that do not express MUC13 (40) vs lines expressing it (10) | 3.10× lower at baseline in the lines without MUC13 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, NPSR1, CDH17 |
| [[TOP2A]] | B | TOP2A activity lowers SERINC5's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[KALRN]] | B | KALRN activity raises SERINC5's level | lines that do not express KALRN (10) vs lines expressing it (40) | 1.31× lower at baseline in the lines without KALRN | 0.098 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[APC]] | C | APC activity strengthens SERINC5's drug response | recorded loss-of-function mutation of APC in 7 lines vs 39 not recorded | the APC-altered lines respond 0.66× as strongly (z diff +2.08); strongest at Idarubicin (hydrochloride) 5 µM: 1.32x vs 3.71x (z diff +7.2) | 0.017 | ⚠ tissue-confounded; across organs; target measured in part of the lines; artifact flags |
| [[ZNF527]] | C | ZNF527 activity strengthens SERINC5's drug response | lines that do not express ZNF527 (3) vs lines expressing it (46) | the lines without ZNF527 respond 0.62× as strongly (z diff +1.89); strongest at Panobinostat 5 µM: 0.66x vs 1.47x (z diff +8.4) | 0.021 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: NME4, ZFP14, ZNF221; target measured in part of the lines; artifact flags |
| [[ZNF527]] | C | ZNF527 activity lowers SERINC5's level | lines that do not express ZNF527 (3) vs lines expressing it (47) | 3.79× higher at baseline in the lines without ZNF527 | 0.036 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: NME4, ZFP14, ZNF221 |
| [[APC]] | C | the direction of APC's effect on SERINC5's drug response is not inferred (the mechanism is not recorded) | recorded alteration (mechanism not recorded) of APC in 10 lines vs 39 not recorded | the APC-altered lines respond 0.70× as strongly (z diff +1.94); strongest at Idarubicin (hydrochloride) 5 µM: 1.48x vs 3.71x (z diff +6.3) | 0.057 | ⚠ tissue-confounded; across organs; mechanism partly not recorded; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **-** arm (projection on the module's main direction -0.386). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-52.1, 7.5); signed map (-15.3, 28.3). **Vector** length 131, 38.9% of its response variance represented; |z| ≥ 3 in 1,419 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.6 | +53.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +9.2 | +22.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +9.2 | +20.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | +5.1 | +3.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | +5.0 | +7.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.3 | +13.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.1 | +3.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.7 | +3.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.6 | +2.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.6 | +2.6 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -8.1 | -11.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.7 | -9.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.7 | -11.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | -6.3 | -8.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.5 | -7.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.5 | -4.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.3 | -3.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.6 | -1.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.5 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | serine incorporator 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q14.1 — chr5:80,111,651-80,256,048 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TPO1; previously C5orf12 |
| Reactome | 2 pathways, smallest: Serine metabolism; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86VE9](https://www.uniprot.org/uniprotkb/Q86VE9) (Serine incorporator 5):

> Restriction factor required to restrict infectivity of lentiviruses, such as HIV-1: acts by inhibiting an early step of viral infection. Impairs the penetration of the viral particle into the cytoplasm. Non-ATP-dependent, non-specific lipid transporter for phosphatidylserine, phosphatidylcholine, and phosphatidylethanolamine. Functions as a scramblase that flips lipids in both directions across the membrane. Phospholipid scrambling results in HIV-1 surface exposure of phosphatidylserine and …

**Summary**, from NCBI Gene [256987](https://www.ncbi.nlm.nih.gov/gene/256987):

> Enables phospholipid scramblase activity. Involved in antiviral innate immune response and plasma membrane phospholipid scrambling. Located in cytosol and plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:18825](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18825) · Entrez [256987](https://www.ncbi.nlm.nih.gov/gene/256987) · UniProt [Q86VE9](https://www.uniprot.org/uniprotkb/Q86VE9) · Ensembl [ENSG00000164300](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164300)

## Data

Gene col 8922: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8922); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8922, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8922]; `tensor/DDL_lfc|DDL_z.npy` [8922]; `embed/gene_vectors.npy` [8922]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8922 or target_col == 8922). Every well: [[SERINC5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SERINC5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
