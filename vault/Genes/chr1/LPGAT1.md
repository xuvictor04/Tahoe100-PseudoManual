---
symbol: "LPGAT1"
type: "gene"
col: 4454
ensembl_id: "ENSG00000123684"
name: "lysophosphatidylglycerol acyltransferase 1"
location: "1q32.3"
module: 25
arm: "+"
pooled_cpm: 145.61
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 15
n_dd_up_clean: 1
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# LPGAT1

*lysophosphatidylglycerol acyltransferase 1* — 1q32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.62× (z +12.3, q 7e-32, up in 41 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[5-Azacytidine (drug)]] 5 µM: 1.16× (z +3.8, q 0.017, up in 20 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (NCI-H1573 6.19×, SW480 2.19×, PANC-1 2.18×, HOP62 2.46×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H1573 4.13×, PANC-1 2.08×, SW480 1.89×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (PANC-1 2.43×; ⚠ cell-cycle shift, would explain all of this change); [[Cobimetinib (drug)]] 5 µM in 1 line (NCI-H1573 2.18×); [[Cobimetinib (drug)]] 0.5 µM in 1 line (C32 2.93×).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.459× (z -19.6, q 0e+00, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (85 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 15 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SGPL1]] (+0.63, fdr 2e-05), [[HACD2]] (+0.62, fdr 2e-05), [[DPY19L4]] (+0.60, fdr 6e-05); moves opposite to [[IMP3]] (-0.62, fdr 3e-05), [[MINCR]] (-0.59, fdr 5e-05), [[EXOSC4]] (-0.54, fdr 3e-04).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SPATC1L]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4454.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (NCI-H1573 6.19×, SW480 2.19×, PANC-1 2.18×, HOP62 2.46×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H1573 4.13×, PANC-1 2.08×, SW480 1.89×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (PANC-1 2.43×; ⚠ cell-cycle shift, would explain all of this change); [[Cobimetinib (drug)]] 5 µM in 1 line (NCI-H1573 2.18×); [[Cobimetinib (drug)]] 0.5 µM in 1 line (C32 2.93×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.62×** | +12.3 | 7e-32 | 41/49 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.59×** | +11.3 | 3e-27 | 32/44 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.29×** | +5.6 | 3e-06 | 25/45 (NCI-H1573, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.16× | +3.8 | 0.017 | 20/48 (NCI-H2030, C-33 A, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.15× | +3.6 | 0.029 | 13/47 (NCI-H460, SHP-77, …) | two highest doses | low cells (technical?) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.10× | +3.6 | 0.029 | 9/48 (C-33 A, NCI-H2030, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 1.17× | +3.5 | 0.032 | 18/50 (NCI-H1573, C32, …) | inconsistent across doses | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.30×** | +3.4 | 0.049 | 14/49 (NCI-H1573, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 0.5 µM |  | 1.14× | +3.4 | 0.049 | 8/48 (PANC-1, NCI-H2030, …) | two highest doses |  |
| [[Ciclopirox (drug)]] 0.5 µM |  | 1.13× | +3.1 | 0.11 | 6/49 (SHP-77, CFPAC-1, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | 1.27× | +3.1 | 0.11 | 12/50 (NCI-H460, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4454.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.459×** | -19.6 | 0e+00 | 43/48 (A549, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.519×** | -16.6 | 0e+00 | 42/48 (AsPC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.548×** | -15.2 | 0e+00 | 41/48 (A549, AsPC-1, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.704×** | -8.9 | 9e-17 | 38/48 (AsPC-1, SNU-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.780×** | -8.9 | 9e-17 | 31/48 (SNU-1, NCI-H460, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.822×** | -7.0 | 3e-10 | 25/49 (A549, AsPC-1, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **0.799×** | -5.7 | 1e-06 | 27/48 (LS 180, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.803×** | -5.5 | 2e-06 | 25/48 (A549, HS-578T, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.649×** | -5.5 | 2e-06 | 26/49 (LoVo, LS 180, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.806×** | -5.4 | 3e-06 | 25/48 (A-427, A-172, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.846× | -4.2 | 0.001 | 21/48 (NCI-H1573, A549, …) | two highest doses |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.805×** | -3.9 | 0.004 | 20/48 (A549, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.757×** | -3.5 | 0.017 | 20/48 (LOX-IMVI, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.758×** | -3.5 | 0.017 | 22/48 (SNU-1, LS 180, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 0.871× | -3.5 | 0.020 | 23/48 (NCI-H1573, LOX-IMVI, …) | all doses, flat |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.827×** | -3.4 | 0.022 | 19/48 (SNU-1, A549, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 0.5 µM |  | **0.831×** | -3.3 | 0.028 | 16/49 (Hs 766T, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.879× | -3.2 | 0.034 | 14/49 (NCI-H2347, SNU-423, …) | top dose only |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | 0.847× | -3.0 | 0.061 | 10/48 (CFPAC-1, NCI-H1573, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[NVP-BHG712 (drug)]] 0.5 µM |  | 0.851× | -2.9 | 0.082 | 9/48 (NCI-H661, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ritonavir (drug)]] 5 µM |  | 0.922× | -2.9 | 0.085 | 0/48 | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4454. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 411 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.188× (z -18.0) |
| [[NCI-H460 (line)]] | wt | 244 | 1 (1 ⚠) | 6 (1 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 2.17× (z +10.2) ⚠ cell-cycle shift, explains ~54% of this change | [[Panobinostat (drug)]] 5 µM 0.332× (z -15.0) |
| [[PANC-1 (line)]] | alt | 152 | 5 (5 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +21.2) ⚠ cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 5 µM 0.543× (z -10.4) |
| [[J82 (line)]] | alt | 111 | 0 | 6 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.415× (z -12.4) |
| [[LS 180 (line)]] | wt | 139 | 0 | 6 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.421× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.450× (z -10.6) |
| [[NCI-H1573 (line)]] | alt | 137 | 5 (4 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 6.19× (z +21.4) ⚠ toxic; transcription drop · without an alert: [[Cobimetinib (drug)]] 5 µM 2.18× (z +8.8) | [[Homoharringtonine (drug)]] 0.5 µM 0.418× (z -10.3) ⚠ cell-cycle shift, explains ~14% of this change |
| [[SW480 (line)]] | alt | 91.2 | 3 (3 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.19× (z +13.8) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.369× (z -17.3) |
| [[CFPAC-1 (line)]] | alt | 159 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.590× (z -10.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.480× (z -10.7) |
| [[HEC-1-A (line)]] | alt | 117 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.557× (z -12.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.495× (z -10.2) |
| [[HS-578T (line)]] | alt | 86.5 | 1 (1 ⚠) | 4 (3 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.19× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.504× (z -12.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.423× (z -10.8) |
| [[NCI-H1792 (line)]] | alt | 181 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -25.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.289× (z -16.9) |
| [[A-172 (line)]] | wt | 181 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.409× (z -12.3) |
| [[A-427 (line)]] | wt | 166 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.381× (z -14.7) |
| [[A549 (line)]] | wt | 294 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.214× (z -20.2) |
| [[BT-474 (line)]] | alt | 80.3 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.350× (z -9.9) |
| [[C32 (line)]] | wt | 55.0 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.52× (z +9.6) ⚠ toxic; transcription drop · without an alert: [[Cobimetinib (drug)]] 0.5 µM 2.93× (z +8.6) | — |
| [[Hs 766T (line)]] | wt | 150 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.336× (z -11.8) |
| [[LoVo (line)]] | wt | 186 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.297× (z -18.4) |
| [[LOX-IMVI (line)]] | wt | 113 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -16.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.469× (z -10.8) |
| [[MIA PaCa-2 (line)]] | alt | 96.2 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.60× (z +11.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.439× (z -10.0) |
| [[SNU-1 (line)]] | wt | 197 | 0 | 4 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.508× (z -11.2) |
| [[A498 (line)]] | wt | 213 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.515× (z -10.5) |
| [[C-33 A (line)]] | alt | 180 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.351× (z -12.9) |
| [[HepG2_C3A (line)]] | wt | 242 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.319× (z -14.9) |
| [[KATO III (line)]] | alt | 92.0 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.35× (z +10.8) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.494× (z -8.9) |
| [[NCI-H2347 (line)]] | alt | 143 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.591× (z -10.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.540× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 112 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.08× (z +9.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.408× (z -11.7) |
| [[SHP-77 (line)]] | alt | 179 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.345× (z -12.8) |
| [[SNU-423 (line)]] | alt | 92.6 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.29× (z +10.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.446× (z -10.3) |
| [[SW1417 (line)]] | alt | 136 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.486× (z -11.0) |
| [[HOP62 (line)]] | alt | 91.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.46× (z +11.7) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 73.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.17× (z +9.8) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 170 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.473× (z -10.3) |
| [[SK-MEL-2 (line)]] | alt | 77.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.65× (z +10.0) ⚠ toxic; transcription drop | — |
| [[SW 1271 (line)]] | alt | 82.3 | 0 | 2 (1 ⚠) | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.106× (z -10.1) |
| [[SW 900 (line)]] | alt | 102 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.45× (z +9.3) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.568× (z -8.6) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SW48 (line)]] | wt | 117 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.392× (z -9.1) ⚠ cell-cycle shift, explains ~14% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.412× (z -8.6) |
| [[AN3 CA (line)]] | alt | 197 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.471× (z -9.2) ⚠ cell-cycle shift, would explain all of this change |
| [[CHP-212 (line)]] | wt | 135 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +8.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[COLO 205 (line)]] | alt | 87.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +10.8) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 133 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -12.2) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 149 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.437× (z -11.7) |
| [[NCI-H23 (line)]] | alt | 82.0 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.452× (z -9.1) |
| [[H4 (line)]] | wt | 97.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 73.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 163 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 69.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 91.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4454), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SGPL1]] | +0.63 | +0.48 / +0.66 | both halves | 2e-05 |  |
| [[HACD2]] | +0.62 | +0.46 / +0.59 | both halves | 2e-05 |  |
| [[DPY19L4]] | +0.60 | +0.39 / +0.62 | both halves | 6e-05 |  |
| [[GMFB]] | +0.59 | +0.42 / +0.59 | both halves | 4e-05 |  |
| [[OCRL]] | +0.56 | +0.42 / +0.59 | both halves | 4e-05 | pathway: Phospholipid metabolism |
| [[OXCT1]] | +0.56 | +0.32 / +0.54 | both halves | 2e-04 |  |
| [[ATL3]] | +0.56 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[ARPP19]] | +0.56 | +0.32 / +0.59 | both halves | 2e-04 |  |
| [[SBDS]] | +0.56 | +0.41 / +0.56 | both halves | 4e-05 |  |
| [[RAB23]] | +0.55 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[DSG2]] | +0.55 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[CFL2]] | +0.55 | +0.38 / +0.53 | both halves | 6e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 13 of them with an alert (⚠; 13 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IMP3]] | -0.62 | -0.46 / -0.64 | both halves | 3e-05 |  |
| [[MINCR]] | -0.59 | -0.40 / -0.59 | both halves | 5e-05 |  |
| [[EXOSC4]] | -0.54 | -0.28 / -0.60 | both halves | 3e-04 |  |
| [[PRKRIP1]] | -0.54 | -0.37 / -0.51 | both halves | 9e-05 |  |
| [[ATG4B]] | -0.53 | -0.25 / -0.60 | both halves | 4e-04 |  |
| [[NUDT22]] | -0.53 | -0.21 / -0.59 | both halves | 7e-04 |  |
| [[C16orf91]] | -0.53 | -0.16 / -0.60 | ⚠ one half (not replicated) | 0.001 |  |
| [[SDHAF1]] | -0.53 | -0.21 / -0.58 | both halves | 6e-04 |  |
| [[SEC61G]] | -0.52 | -0.34 / -0.54 | both halves | 1e-04 |  |
| [[EIF1AD]] | -0.51 | -0.21 / -0.53 | both halves | 7e-04 |  |
| [[NOSIP]] | -0.51 | -0.29 / -0.58 | both halves | 3e-04 |  |
| [[RUNX3]] | -0.50 | -0.40 / -0.55 | both halves | 5e-05 |  |
| [[C19orf81]] | -0.50 | -0.36 / -0.47 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPATC1L]] | B | SPATC1L activity lowers LPGAT1's level | lines that do not express SPATC1L (10) vs lines expressing it (40) | 1.41× higher at baseline in the lines without SPATC1L | 0.079 | ⚠ within organs, on part of the lines; also absent: TIAM1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.569). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-30.3, -18.7); signed map (-17.5, -39.2). **Vector** length 120, 35.2% of its response variance represented; |z| ≥ 3 in 1,355 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +10.6 | +11.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +10.2 | +12.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.3 | +5.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.9 | +0.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.4 | -2.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.2 | +3.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.8 | +2.7 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +3.5 | +3.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.4 | +3.6 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +3.1 | +2.6 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.0 | -8.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.0 | -5.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.9 | -19.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.5 | -16.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.5 | -3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | -8.9 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | -2.9 | -3.3 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -2.8 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | lysophosphatidylglycerol acyltransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.3 — chr1:211,743,457-211,830,763 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0205, FAM34A1, NET8, LPLAT7; previously FAM34A |
| Gene groups (HGNC) | Lysophospholipid acyltransferases |
| Reactome | 4 pathways, smallest: Acyl chain remodelling of PG; Glycerophospholipid biosynthesis; Phospholipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92604](https://www.uniprot.org/uniprotkb/Q92604) (Acyl-CoA:lysophosphatidylglycerol acyltransferase 1):

> Lysophospholipid acyltransferase involved in fatty acyl chain remodeling of glycerophospholipids in the endoplasmic reticulum membrane (By similarity). Selectively catalyzes the transfer and esterification of saturated long-chain fatty acids from acyl-CoA to the sn-1 position of 1-lyso-2-acyl phosphatidylethanolamines (1-lyso-PE, LPE), with a preference for stearoyl CoA over palmitoyl CoA as acyl donor. Acts in concert with an unknown phospholipase A1 to convert palmitate …

**Summary**, from NCBI Gene [9926](https://www.ncbi.nlm.nih.gov/gene/9926):

> This gene encodes a member of the lysophospholipid acyltransferase family. The encoded protein catalyzes the reacylation of lysophosphatidylglycerol to phosphatidylglycerol, a membrane phospholipid that is an important precursor for the synthesis of cardiolipin. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Mar 2016]

**Accessions** — [HGNC:28985](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28985) · Entrez [9926](https://www.ncbi.nlm.nih.gov/gene/9926) · UniProt [Q92604](https://www.uniprot.org/uniprotkb/Q92604) · Ensembl [ENSG00000123684](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123684)

## Data

Gene col 4454: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4454); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4454, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4454]; `tensor/DDL_lfc|DDL_z.npy` [4454]; `embed/gene_vectors.npy` [4454]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4454 or target_col == 4454). Every well: [[LPGAT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LPGAT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
