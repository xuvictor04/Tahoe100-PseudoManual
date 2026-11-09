---
symbol: "SPPL3"
type: "gene"
col: 8105
ensembl_id: "ENSG00000157837"
name: "signal peptide peptidase like 3"
location: "12q24.31"
module: 52
arm: "-"
pooled_cpm: 151.78
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 14
n_dd_up_clean: 9
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# SPPL3

*signal peptide peptidase like 3* — 12q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.68× (z +20.2, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.313× (z -22.9, q 0e+00, down in 44 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.729× (z -6.5, q 1e-08, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDSUB1]] (+0.65, fdr 7e-06), [[RAB9A]] (+0.64, fdr 1e-05), [[MTMR3]] (+0.63, fdr 7e-06); moves opposite to [[LRRC59]] (-0.67, fdr 1e-05), [[GOLGA3]] (-0.64, fdr 1e-05), [[EP400P1]] (-0.63, fdr 1e-05).
> It sits in the **-** arm of [[Module 052]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MDK]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8105.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.68×** | +20.2 | 0e+00 | 46/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.38×** | +17.8 | 0e+00 | 43/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.89×** | +13.1 | 9e-37 | 44/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.45×** | +10.7 | 1e-24 | 40/48 (NCI-H460, J82, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.67×** | +10.5 | 1e-23 | 43/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.54×** | +9.5 | 1e-19 | 46/49 (NCI-H460, NCI-H23, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.24×** | +8.2 | 1e-14 | 41/48 (C32, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.45×** | +7.4 | 1e-11 | 29/48 (NCI-H460, J82, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.25×** | +6.5 | 6e-09 | 32/48 (HT-29, PANC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.30×** | +5.1 | 2e-05 | 33/47 (J82, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.23×** | +4.2 | 0.001 | 28/48 (PANC-1, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 1.14× | +3.9 | 0.004 | 6/48 (SHP-77, SW 900, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.20×** | +3.7 | 0.011 | 17/49 (J82, SNU-423, …) | top dose only |  |
| [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | 1.17× | +3.2 | 0.051 | 15/48 (J82, HOP62, …) | inconsistent across doses |  |
| [[ULK-101 (drug)]] 0.05 µM |  | 1.18× | +3.2 | 0.059 | 17/49 (PANC-1, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 5 µM |  | **1.34×** | +3.0 | 0.092 | 14/49 (NCI-H460, A-427, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8105.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.313×** | -22.9 | 0e+00 | 44/44 (MIA PaCa-2, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.351×** | -21.5 | 0e+00 | 49/49 (CFPAC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.524×** | -12.3 | 3e-32 | 42/45 (LOX-IMVI, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.743×** | -8.6 | 9e-16 | 31/49 (NCI-H2347, LOX-IMVI, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.729×** | -6.5 | 1e-08 | 34/48 (SW480, HOP62, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.746×** | -5.8 | 5e-07 | 38/48 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~24% of this change | **0.755×** | -5.8 | 6e-07 | 31/48 (SW1417, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **0.755×** | -5.6 | 2e-06 | 31/47 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.596×** | -5.3 | 8e-06 | 36/48 (MIA PaCa-2, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 0.835× | -5.2 | 9e-06 | 20/48 (NCI-H23, SW1417, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.782×** | -5.0 | 2e-05 | 30/48 (CFPAC-1, A-172, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.662×** | -4.2 | 0.001 | 26/48 (MIA PaCa-2, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.691×** | -3.8 | 0.007 | 27/48 (CFPAC-1, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.827×** | -3.7 | 0.007 | 24/50 (A-172, RKO, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **0.714×** | -3.4 | 0.021 | 21/48 (MIA PaCa-2, HT-29, …) | all doses, flat | noisy plate (z scaled) |
| [[Mifepristone (drug)]] 0.5 µM |  | 0.849× | -3.4 | 0.026 | 14/48 (NCI-H1573, Panc 03.27, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.866× | -3.0 | 0.098 | 13/48 (PANC-1, LOX-IMVI, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8105. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 137 | 11 (4 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.69× (z +30.5) | [[Dinaciclib (drug)]] 0.5 µM 0.243× (z -21.1) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 136 | 7 (2 ⚠) | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.81× (z +21.5) | [[Dinaciclib (drug)]] 5 µM 0.216× (z -23.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.573× (z -8.9) |
| [[SW1417 (line)]] | alt | 180 | 5 (1 ⚠) | 5 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.17× (z +19.7) | [[Dinaciclib (drug)]] 0.5 µM 0.264× (z -18.5) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 200 | 3 | 6 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +13.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -19.2) ⚠ cell-cycle shift, explains ~23% of this change |
| [[HOP62 (line)]] | alt | 120 | 4 (1 ⚠) | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.76× (z +16.6) | [[Dinaciclib (drug)]] 5 µM 0.360× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.510× (z -8.6) |
| [[NCI-H1792 (line)]] | alt | 145 | 4 (1 ⚠) | 4 (4 ⚠) | [[Digitoxin (drug)]] 5 µM 2.97× (z +13.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.93× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.276× (z -14.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 152 | 5 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.47× (z +14.3) | [[Dinaciclib (drug)]] 0.5 µM 0.259× (z -15.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 145 | 4 (2 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.72× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.284× (z -15.7) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 133 | 5 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.29× (z +21.7) | [[Dinaciclib (drug)]] 5 µM 0.132× (z -25.4) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 183 | 5 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.29× (z +16.6) | [[Dinaciclib (drug)]] 5 µM 0.321× (z -15.2) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 179 | 2 (1 ⚠) | 5 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.60× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.194× (z -18.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 116 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.267× (z -16.7) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 128 | 4 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.96× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.170× (z -15.3) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 110 | 4 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.01× (z +15.5) | [[Dinaciclib (drug)]] 0.5 µM 0.375× (z -11.0) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 214 | 1 | 5 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.16× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.124× (z -24.0) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 149 | 4 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.44× (z +13.6) | [[Dinaciclib (drug)]] 0.5 µM 0.174× (z -19.3) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 118 | 3 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.04× (z +17.2) | [[Dinaciclib (drug)]] 0.5 µM 0.378× (z -10.3) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 168 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.16× (z +14.5) | — |
| [[C32 (line)]] | wt | 147 | 3 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 8.56× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.235× (z -13.8) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 200 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.133× (z -26.0) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 144 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.44× (z +15.1) | [[Dinaciclib (drug)]] 5 µM 0.340× (z -9.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 257 | 2 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.43× (z +14.2) | [[Dinaciclib (drug)]] 5 µM 0.113× (z -24.3) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 178 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0612× (z -33.2) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 189 | 3 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.24× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.189× (z -20.7) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 117 | 3 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.33× (z +18.8) | [[Dinaciclib (drug)]] 0.5 µM 0.335× (z -17.2) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 191 | 4 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.81× (z +12.0) | [[Dinaciclib (drug)]] 0.5 µM 0.314× (z -10.4) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 210 | 3 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.12× (z +12.3) | [[Dinaciclib (drug)]] 0.5 µM 0.410× (z -9.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 188 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.202× (z -20.6) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 99.5 | 3 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.91× (z +10.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.09× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.321× (z -11.1) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 145 | 2 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.47× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.405× (z -11.3) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 149 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.353× (z -16.4) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 75.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +13.4) | — |
| [[NCI-H2030 (line)]] | alt | 159 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.231× (z -15.9) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 142 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.165× (z -22.0) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 159 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.65× (z +11.3) | [[Dinaciclib (drug)]] 0.5 µM 0.196× (z -19.0) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 133 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.22× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.263× (z -14.3) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 157 | 1 | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.47× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.0788× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Proglumide (drug)]] 0.05 µM 0.232× (z -8.5) |
| [[A-427 (line)]] | wt | 144 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.412× (z -10.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 109 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.306× (z -10.1) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 308 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0832× (z -16.9) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 142 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.51× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.390× (z -9.2) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 208 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.161× (z -20.2) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 168 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0793× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SK-MEL-2 (line)]] | alt | 132 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.237× (z -13.8) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 98.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.374× (z -8.7) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 202 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.197× (z -14.8) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 157 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 201 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 115 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8105), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDSUB1]] | +0.65 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[RAB9A]] | +0.64 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[MTMR3]] | +0.63 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[UVRAG]] | +0.63 | +0.47 / +0.64 | both halves | 2e-05 |  |
| [[PAN3]] | +0.63 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[NPC2]] | +0.62 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[CLN8-AS1]] | +0.61 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[AMBRA1]] | +0.61 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[TP53TG1]] | +0.59 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[MED13L]] | +0.59 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[SNX2]] | +0.59 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[PIAS1]] | +0.59 | +0.59 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRC59]] | -0.67 | -0.57 / -0.61 | both halves | 1e-05 |  |
| [[GOLGA3]] | -0.64 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[EP400P1]] | -0.63 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[CCT6A]] | -0.60 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[PRKAG1]] | -0.58 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[SZT2]] | -0.58 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[PDAP1]] | -0.57 | -0.59 / -0.46 | both halves | 3e-05 |  |
| [[GDI2]] | -0.57 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[CYCS]] | -0.56 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[TAF13]] | -0.56 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[TMEM214]] | -0.55 | -0.38 / -0.50 | both halves | 7e-05 |  |
| [[TXLNA]] | -0.55 | -0.43 / -0.51 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MDK]] | B | MDK activity strengthens SPPL3's drug response | lines that do not express MDK (14) vs lines expressing it (35) | the lines without MDK respond 0.82× as strongly (z diff +1.12); strongest at Digitoxin 0.5 µM: 1.29x vs 1.88x (z diff +2.8) | 0.006 | ⚠ within organs, on part of the lines; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **-** arm (projection on the module's main direction -0.599). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (5.7, -28.9); signed map (-8.1, 1.6). **Vector** length 106, 39.4% of its response variance represented; |z| ≥ 3 in 1,232 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +9.9 | +6.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.7 | +17.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | +5.7 | +4.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.2 | +0.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.6 | +5.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.3 | +1.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.0 | +1.6 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +3.9 | +2.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.9 | +0.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.8 | -5.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.8 | -6.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.7 | -4.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.2 | -5.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -4.1 | -1.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.0 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | signal peptide peptidase like 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.31 — chr12:120,762,510-120,904,358 (-) |
| Ensembl biotype | protein_coding |
| Also known as | IMP2, PSL4, MGC90402, MGC126674, MGC126676, DKFZP586C1324 |
| Gene groups (HGNC) | Signal peptide peptidase like family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TCT6](https://www.uniprot.org/uniprotkb/Q8TCT6) (Signal peptide peptidase-like 3):

> Intramembrane-cleaving aspartic protease (I-CLiP) that cleaves type II membrane protein substrates in or close to their luminal transmembrane domain boundaries. Acts like a sheddase by mediating the proteolytic release and secretion of active site-containing ectodomains of glycan-modifying glycosidase and glycosyltransferase enzymes such as MGAT5, B4GAT1 and B4GALT1. Catalyzes the intramembrane cleavage of the envelope glycoprotein gp130 and/or the leader peptide gp18LP of the simian foamy …

**Summary**, from NCBI Gene [121665](https://www.ncbi.nlm.nih.gov/gene/121665):

> Enables aspartic endopeptidase activity, intramembrane cleaving and protein homodimerization activity. Involved in T cell receptor signaling pathway; membrane protein proteolysis; and positive regulation of calcineurin-NFAT signaling cascade. Located in Golgi-associated vesicle membrane; endoplasmic reticulum; and plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30424](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30424) · Entrez [121665](https://www.ncbi.nlm.nih.gov/gene/121665) · UniProt [Q8TCT6](https://www.uniprot.org/uniprotkb/Q8TCT6) · Ensembl [ENSG00000157837](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157837)

## Data

Gene col 8105: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8105); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8105, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8105]; `tensor/DDL_lfc|DDL_z.npy` [8105]; `embed/gene_vectors.npy` [8105]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8105 or target_col == 8105). Every well: [[SPPL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPPL3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
