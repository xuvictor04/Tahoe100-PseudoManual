---
symbol: "TTC19"
type: "gene"
col: 233
ensembl_id: "ENSG00000011295"
name: "tetratricopeptide repeat domain 19"
location: "17p12"
module: 77
arm: "+"
pooled_cpm: 109.72
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 2
n_dd_up_clean: 12
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/077"]
generated_by: "tahoemap"
---

# TTC19

*tetratricopeptide repeat domain 19* — 17p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.82× (z +16.5, q 0e+00, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Cobimetinib (drug)]] 5 µM: 0.793× (z -6.1, q 3e-07, down in 26 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 7 lines (A498 0.559×, SW1417 0.556×, SW 900 0.410×, BT-474 0.522×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (SNU-1 0.148×, A-427 0.317×, SHP-77 0.309×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (C-33 A 0.524×; ⚠ cell-cycle shift, explains ~29% of this change); [[Sacubitril_Valsartan (drug)]] 5 µM in 1 line (SW 1088 0.0670×); [[Loperamide (hydrochloride) (drug)]] 0.05 µM in 1 line (SW 1088 0.0834×).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ITPR1]] (+0.53, fdr 5e-05), [[EML4]] (+0.53, fdr 4e-05), [[HPCAL1]] (+0.53, fdr 1e-04); moves opposite to [[C7orf31]] (-0.54, fdr 6e-05), [[DECR1]] (-0.51, fdr 4e-04), [[PAXIP1-AS2]] (-0.48, fdr 1e-04).
> It sits in the **+** arm of [[Module 077]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LHX6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 16 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 233.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.82×** | +16.5 | 0e+00 | 43/48 (HS-578T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.64×** | +13.7 | 2e-40 | 43/48 (HS-578T, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.58×** | +12.7 | 1e-34 | 38/48 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.35×** | +11.8 | 7e-30 | 33/48 (LoVo, HOP62, …) | rises with dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.27×** | +9.2 | 4e-18 | 27/48 (LOX-IMVI, RKO, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.37×** | +8.7 | 3e-16 | 30/48 (KATO III, PANC-1, …) | two highest doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.37×** | +8.6 | 7e-16 | 31/48 (NCI-H1573, J82, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.34×** | +8.2 | 2e-14 | 30/48 (C32, HOP62, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.30×** | +7.2 | 5e-11 | 28/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.29×** | +7.0 | 1e-10 | 28/48 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.29×** | +7.0 | 1e-10 | 26/48 (NCI-H1573, J82, …) | two highest doses | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.28×** | +6.6 | 1e-09 | 24/47 (NCI-H460, J82, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~20% of this change | 1.19× | +4.9 | 4e-05 | 22/48 (HS-578T, SW480, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.20×** | +4.9 | 4e-05 | 22/48 (KATO III, AsPC-1, …) | top dose only | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~17% of this change | 1.17× | +4.1 | 0.002 | 20/47 (NCI-H2030, NCI-H460, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **1.30×** | +3.8 | 0.004 | 18/48 (NCI-H460, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.29×** | +3.7 | 0.007 | 18/48 (CFPAC-1, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 1.14× | +3.7 | 0.008 | 11/48 (NCI-H2030, PANC-1, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.28×** | +3.6 | 0.009 | 16/49 (NCI-H23, C32, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.10× | +3.6 | 0.009 | 7/49 (SHP-77, KATO III, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.27×** | +3.5 | 0.013 | 13/48 (NCI-H460, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 1.13× | +3.4 | 0.018 | 15/48 (MIA PaCa-2, Panc 03.27, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.26×** | +3.3 | 0.022 | 14/48 (RPMI-7951, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.23×** | +3.0 | 0.051 | 12/48 (SHP-77, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.22×** | +2.8 | 0.087 | 9/49 (AsPC-1, HS-578T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 233.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 7 lines (A498 0.559×, SW1417 0.556×, SW 900 0.410×, BT-474 0.522×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (SNU-1 0.148×, A-427 0.317×, SHP-77 0.309×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (C-33 A 0.524×; ⚠ cell-cycle shift, explains ~29% of this change); [[Sacubitril_Valsartan (drug)]] 5 µM in 1 line (SW 1088 0.0670×); [[Loperamide (hydrochloride) (drug)]] 0.05 µM in 1 line (SW 1088 0.0834×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **0.793×** | -6.1 | 3e-07 | 26/47 (A-427, LoVo, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.855× | -6.1 | 3e-07 | 20/49 (A498, SW1417, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.829×** | -5.2 | 4e-05 | 22/47 (CFPAC-1, C32, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.948× | -5.0 | 7e-05 | 0/50 | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.858× | -4.8 | 2e-04 | 20/50 (SNU-423, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.866× | -4.7 | 3e-04 | 15/48 (SW1417, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.839× | -4.7 | 3e-04 | 19/48 (SNU-423, A549, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.856× | -4.3 | 0.001 | 16/49 (BT-474, HepG2/C3A, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.897× | -4.2 | 0.002 | 5/48 (HepG2/C3A, MIA PaCa-2, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.865× | -4.1 | 0.003 | 16/49 (COLO 205, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.865× | -3.7 | 0.012 | 13/48 (LoVo, SW480, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.900× | -3.6 | 0.017 | 10/48 (C32, PANC-1, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 233. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 99.7 | 6 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.07× (z +10.7) | — |
| [[HOP62 (line)]] | alt | 135 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +15.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.57× (z +12.8) | — |
| [[NCI-H1573 (line)]] | alt | 89.1 | 5 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.05× (z +11.6) | — |
| [[AsPC-1 (line)]] | alt | 51.4 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +14.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 3.26× (z +11.0) | — |
| [[HS-578T (line)]] | alt | 85.5 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.80× (z +14.3) | — |
| [[KATO III (line)]] | alt | 113 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +12.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 1.96× (z +10.0) | — |
| [[LOX-IMVI (line)]] | wt | 60.4 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.80× (z +11.0) | — |
| [[NCI-H23 (line)]] | alt | 119 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.20× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.504× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 118 | 4 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 1.99× (z +12.3) | — |
| [[C32 (line)]] | wt | 125 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +13.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.16× (z +11.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.646× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 57.0 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.41× (z +9.7) | — |
| [[LoVo (line)]] | wt | 132 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +16.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 1.93× (z +9.7) | — |
| [[Panc 03.27 (line)]] | alt | 66.0 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.35× (z +9.4) | — |
| [[SHP-77 (line)]] | alt | 314 | 2 | 1 (1 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 1.64× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.309× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 128 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.54× (z +9.0) ⚠ cell-cycle shift, explains ~29% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.559× (z -12.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 118 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.40× (z +10.8) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[PANC-1 (line)]] | alt | 104 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 1.91× (z +9.6) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[RKO (line)]] | wt | 116 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +11.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.73× (z +9.9) | — |
| [[SW 1088 (line)]] | alt | 88.4 | 0 | 2 | — | [[Sacubitril_Valsartan (drug)]] 5 µM 0.0670× (z -9.5) |
| [[A-427 (line)]] | wt | 81.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.317× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 114 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.522× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 210 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.524× (z -9.6) ⚠ cell-cycle shift, explains ~29% of this change |
| [[HEC-1-A (line)]] | alt | 130 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.59× (z +9.3) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[Hs 766T (line)]] | wt | 67.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.53× (z +9.4) | — |
| [[LS 180 (line)]] | wt | 189 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.72× (z +8.5) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[RPMI-7951 (line)]] | alt | 75.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.48× (z +8.8) | — |
| [[SNU-1 (line)]] | wt | 101 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.148× (z -17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 122 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.40× (z +9.7) | — |
| [[SW 1271 (line)]] | alt | 254 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.341× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 178 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.410× (z -11.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 103 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.556× (z -11.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 99.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 143 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 115 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 61.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 116 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 92.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 83.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 158 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 88.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 71.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 57.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 91.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 148 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 233), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 5 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITPR1]] | +0.53 | +0.47 / +0.39 | both halves | 5e-05 |  |
| [[EML4]] | +0.53 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[HPCAL1]] | +0.53 | +0.49 / +0.35 | both halves | 1e-04 |  |
| [[ETV5]] | +0.52 | +0.42 / +0.43 | both halves | 4e-05 |  |
| [[PTPRS]] | +0.51 | +0.36 / +0.42 | both halves | 9e-05 |  |
| [[SSBP4]] | +0.50 | +0.40 / +0.32 | both halves | 2e-04 |  |
| [[CD320]] | +0.49 | +0.43 / +0.34 | both halves | 1e-04 |  |
| [[RSAD1]] | +0.48 | +0.29 / +0.36 | both halves | 2e-04 |  |
| [[FAM3C]] | +0.48 | +0.37 / +0.45 | both halves | 8e-05 |  |
| [[SMG1P2]] | +0.48 | +0.46 / +0.34 | both halves | 1e-04 |  |
| [[SLC25A32]] | +0.46 | +0.37 / +0.44 | both halves | 8e-05 |  |
| [[ASL]] | +0.46 | +0.35 / +0.26 | both halves | 3e-04 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C7orf31]] | -0.54 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[DECR1]] | -0.51 | -0.42 / -0.25 | both halves | 4e-04 |  |
| [[PAXIP1-AS2]] | -0.48 | -0.37 / -0.32 | both halves | 1e-04 |  |
| [[C3orf38]] | -0.47 | -0.34 / -0.34 | both halves | 1e-04 |  |
| [[SRP14]] | -0.46 | -0.39 / -0.40 | both halves | 6e-05 |  |
| [[AP5M1]] | -0.46 | -0.40 / -0.12 | ⚠ not reproduced | 0.002 |  |
| [[GAS2]] | -0.46 | -0.35 / -0.22 | both halves | 6e-04 |  |
| [[TAPBPL]] | -0.46 | -0.23 / -0.38 | both halves | 5e-04 |  |
| [[CFLAR]] | -0.45 | -0.23 / -0.34 | both halves | 5e-04 |  |
| [[PSME3IP1]] | -0.45 | -0.34 / -0.27 | both halves | 3e-04 |  |
| [[CASP7]] | -0.45 | -0.40 / -0.27 | both halves | 3e-04 |  |
| [[CCDC117]] | -0.45 | -0.36 / -0.29 | both halves | 2e-04 |  |
| [[UBE3B]] | -0.44 | -0.25 / -0.33 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LHX6]] | B | LHX6 activity raises TTC19's level | lines that do not express LHX6 (16) vs lines expressing it (34) | 1.41× lower at baseline in the lines without LHX6 | 0.077 | ⚠ within organs, on part of the lines; also absent: ENSG00000224905, RADIL, OLFM1; maybe low, not absent |
| [[OTUB2]] | C | OTUB2's natural level weakens TTC19's drug response | OTUB2's natural level across 46 lines (lineage-adjusted; a glimpse) | r -0.66, reverse +0.36; direction not clear | 0.054 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 077]]; 59 genes; this gene is in the **+** arm (projection on the module's main direction 0.409). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.44).
- **Nodal map** (x, y) = (37.2, 8.1); signed map (0.8, 42.3). **Vector** length 97.9, 24.4% of its response variance represented; |z| ≥ 3 in 1,100 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.2 | +9.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.0 | +13.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.9 | +16.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.7 | +12.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.8 | +3.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.3 | +3.3 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +2.3 | +3.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.0 | +2.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.0 | +3.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -7.6 | -6.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.6 | -6.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -4.5 | +4.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.7 | -0.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.7 | -4.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.5 | -4.7 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -3.4 | -5.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.1 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | tetratricopeptide repeat domain 19 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p12 — chr17:15,999,784-16,045,015 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20343, MGC19520 |
| Gene groups (HGNC) | Mitochondrial respiratory chain complex assembly factors; Tetratricopeptide repeat domain containing |
| Reactome | 3 pathways, smallest: Complex III assembly; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6DKK2](https://www.uniprot.org/uniprotkb/Q6DKK2) (Tetratricopeptide repeat protein 19, mitochondrial):

> Required for the preservation of the structural and functional integrity of mitochondrial respiratory complex III by allowing the physiological turnover of the Rieske protein UQCRFS1. Involved in the clearance of UQCRFS1 N-terminal fragments, which are produced upon incorporation of UQCRFS1 into the complex III and whose presence is detrimental for its catalytic activity.

**Summary**, from NCBI Gene [54902](https://www.ncbi.nlm.nih.gov/gene/54902):

> This gene encodes a protein with a tetratricopeptide repeat (TPR) domain containing several TPRs of about 34 aa each. These repeats are found in a variety of organisms including bacteria, fungi and plants, and are involved in a variety of functions including protein-protein interactions. This protein is embedded in the inner mitochondrial membrane and is involved in the formation of the mitochondrial respiratory chain III. It has also been suggested that this protein plays a role in …

**Accessions** — [HGNC:26006](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26006) · Entrez [54902](https://www.ncbi.nlm.nih.gov/gene/54902) · UniProt [Q6DKK2](https://www.uniprot.org/uniprotkb/Q6DKK2) · Ensembl [ENSG00000011295](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000011295)

## Data

Gene col 233: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 233); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 233, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 233]; `tensor/DDL_lfc|DDL_z.npy` [233]; `embed/gene_vectors.npy` [233]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 233 or target_col == 233). Every well: [[TTC19 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TTC19.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
