---
symbol: "SPATS2"
type: "gene"
col: 4424
ensembl_id: "ENSG00000123352"
name: "spermatogenesis associated serine rich 2"
location: "12q13.12"
module: 168
arm: "-"
pooled_cpm: 175.08
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 12
n_dd_up_clean: 6
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/168"]
generated_by: "tahoemap"
---

# SPATS2

*spermatogenesis associated serine rich 2* — 12q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.69× (z +17.8, q 0e+00, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.608× (z -16.9, q 0e+00, down in 37 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.619× (z -16.3, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PHTF1]] (+0.53, fdr 4e-05), [[MARK1]] (+0.51, fdr 1e-04), [[RHBDD3]] (+0.49, fdr 4e-05); moves opposite to [[RNF141]] (-0.49, fdr 1e-04), [[TSFM]] (-0.46, fdr 1e-04), [[TMEM30A-DT]] (-0.45, fdr 6e-04).
> It sits in the **-** arm of [[Module 168]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MAL2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4424.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.69×** | +17.8 | 0e+00 | 41/48 (NCI-H460, COLO 205, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.61×** | +16.3 | 0e+00 | 40/48 (NCI-H460, COLO 205, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.62×** | +15.5 | 0e+00 | 36/48 (NCI-H460, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.33×** | +13.6 | 6e-40 | 33/48 (NCI-H2347, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.30×** | +8.6 | 6e-16 | 30/48 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.37×** | +7.6 | 3e-12 | 31/49 (PANC-1, A498, …) | all doses, flat | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.53×** | +7.6 | 3e-12 | 32/45 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +5.7 | 1e-06 | 24/48 (SW480, NCI-H460, …) | rises with dose | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.12× | +4.0 | 0.004 | 11/49 (A-172, HEC-1-A, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.12× | +3.8 | 0.007 | 11/48 (NCI-H2347, CFPAC-1, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.11× | +3.6 | 0.015 | 11/48 (KATO III, HepG2/C3A, …) | inconsistent across doses |  |
| [[Entecavir (monohydrate) (drug)]] 5 µM |  | 1.10× | +3.2 | 0.071 | 2/48 (HOP62, NCI-H1573) | top dose only | plate-row cell shift |
| [[Verteporfin (drug)]] 5 µM |  | 1.10× | +3.1 | 0.071 | 9/49 (A498, Panc 03.27, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4424.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.608×** | -16.9 | 0e+00 | 37/49 (NCI-H23, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.619×** | -16.3 | 0e+00 | 47/48 (A-427, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.599×** | -16.2 | 0e+00 | 40/45 (SW480, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.633×** | -15.6 | 0e+00 | 42/48 (A-427, HOP62, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.630×** | -15.1 | 0e+00 | 38/44 (SNU-1, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.725×** | -11.0 | 4e-26 | 35/48 (A-427, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.733×** | -10.6 | 3e-24 | 30/48 (SW480, SK-MEL-2, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.786×** | -7.9 | 2e-13 | 31/47 (HOP62, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 0.835× | -6.2 | 5e-08 | 24/48 (NCI-H23, LOX-IMVI, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.890× | -5.6 | 1e-06 | 17/48 (HOP62, A-427, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.855× | -5.3 | 5e-06 | 19/48 (SW48, SW 900, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.852× | -5.3 | 7e-06 | 20/48 (NCI-H1792, C-33 A, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 0.863× | -5.0 | 2e-05 | 22/48 (C32, H4, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.757×** | -5.0 | 3e-05 | 21/48 (KATO III, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~15% of this change | 0.865× | -4.9 | 3e-05 | 20/48 (HOP62, A549, …) | inconsistent across doses | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **0.765×** | -4.8 | 7e-05 | 23/49 (NCI-H23, KATO III, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.877× | -4.1 | 0.001 | 12/47 (SNU-1, NCI-H460, …) | inconsistent across doses | low cells (technical?) |
| [[Radotinib (drug)]] 5 µM |  | 0.918× | -4.1 | 0.001 | 6/48 (LOX-IMVI, A-427, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.899× | -3.6 | 0.008 | 10/48 (NCI-H460, NCI-H23, …) | rises with dose |  |
| [[4EGI-1 (drug)]] 5 µM |  | **0.815×** | -3.6 | 0.008 | 13/48 (PANC-1, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.928× | -3.6 | 0.008 | 4/49 (A498, LS 180, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | 0.872× | -3.3 | 0.021 | 13/47 (NCI-H23, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4424. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 349 | 0 | 12 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.397× (z -20.0) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.450× (z -12.3) |
| [[SW480 (line)]] | alt | 254 | 5 (2 ⚠) | 7 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.92× (z +14.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 1.70× (z +11.8) | [[Dinaciclib (drug)]] 0.05 µM 0.392× (z -19.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.453× (z -17.6) |
| [[A-427 (line)]] | wt | 634 | 0 | 11 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.332× (z -21.2) |
| [[NCI-H23 (line)]] | alt | 231 | 3 | 8 (5 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.11× (z +12.6) | [[Dinaciclib (drug)]] 0.5 µM 0.185× (z -30.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.543× (z -10.9) |
| [[A549 (line)]] | wt | 287 | 2 | 8 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +13.8) | [[Dinaciclib (drug)]] 5 µM 0.325× (z -18.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.377× (z -16.5) |
| [[NCI-H460 (line)]] | wt | 201 | 6 (1 ⚠) | 4 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 2.16× (z +15.8) | [[Dinaciclib (drug)]] 0.05 µM 0.462× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.634× (z -9.7) |
| [[Panc 03.27 (line)]] | alt | 161 | 5 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +22.8) | [[Dinaciclib (drug)]] 0.05 µM 0.473× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.547× (z -10.6) |
| [[HEC-1-A (line)]] | alt | 131 | 5 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +18.3) | [[Dinaciclib (drug)]] 0.05 µM 0.492× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.555× (z -10.5) |
| [[HOP62 (line)]] | alt | 229 | 0 | 9 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.271× (z -21.1) |
| [[PANC-1 (line)]] | alt | 182 | 5 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +26.1) | [[Panobinostat (drug)]] 0.5 µM 0.566× (z -13.8) |
| [[SW1417 (line)]] | alt | 107 | 6 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +14.9) | [[Dinaciclib (drug)]] 0.05 µM 0.501× (z -10.0) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 174 | 2 | 5 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.00× (z +10.0) | [[Dinaciclib (drug)]] 0.05 µM 0.261× (z -18.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.484× (z -10.6) |
| [[Hs 766T (line)]] | wt | 264 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.267× (z -17.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.445× (z -11.0) |
| [[hTERT-HPNE (line)]] | wt | 160 | 3 | 3 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.27× (z +10.6) | [[Panobinostat (drug)]] 0.5 µM 0.426× (z -11.0) |
| [[LoVo (line)]] | wt | 165 | 1 (1 ⚠) | 5 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.61× (z +9.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.537× (z -11.7) |
| [[RPMI-7951 (line)]] | alt | 148 | 3 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +13.2) | [[Dinaciclib (drug)]] 5 µM 0.408× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.537× (z -8.5) |
| [[A498 (line)]] | wt | 112 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +18.4) | — |
| [[C-33 A (line)]] | alt | 274 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.433× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.540× (z -9.1) |
| [[HepG2_C3A (line)]] | wt | 152 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.491× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 87.3 | 4 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +28.5) | [[Dinaciclib (drug)]] 0.5 µM 0.565× (z -8.7) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 115 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +12.4) | — |
| [[KATO III (line)]] | alt | 128 | 3 | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 1.87× (z +10.3) | [[Panobinostat (drug)]] 5 µM 0.584× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 135 | 2 (1 ⚠) | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.65× (z +10.8) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 1.98× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.495× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.540× (z -9.3) |
| [[NCI-H1792 (line)]] | alt | 174 | 1 | 3 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.85× (z +9.2) | [[Dinaciclib (drug)]] 0.05 µM 0.350× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.514× (z -10.1) |
| [[SK-MEL-2 (line)]] | alt | 142 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +19.2) | [[Dinaciclib (drug)]] 5 µM 0.411× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.447× (z -11.9) |
| [[SNU-423 (line)]] | alt | 179 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.412× (z -13.8) |
| [[AN3 CA (line)]] | alt | 245 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.362× (z -9.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.404× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 137 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.13× (z +11.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.68× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.564× (z -8.5) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 87.7 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.95× (z +12.6) | — |
| [[COLO 205 (line)]] | alt | 97.8 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.46× (z +14.3) | — |
| [[H4 (line)]] | wt | 191 | 1 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.21× (z +10.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.447× (z -10.0) ⚠ toxic |
| [[RKO (line)]] | wt | 220 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.503× (z -10.6) ⚠ cell-cycle shift, explains ~13% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.544× (z -9.3) |
| [[A-172 (line)]] | wt | 117 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.04× (z +10.4) | — |
| [[LS 180 (line)]] | wt | 94.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.439× (z -14.6) |
| [[SNU-1 (line)]] | wt | 136 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.112× (z -25.1) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 132 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +13.3) | [[Lonafarnib (drug)]] 5 µM 0.258× (z -10.4) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 85.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +13.8) | — |
| [[HCT15 (line)]] | alt | 153 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.468× (z -9.0) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 92.3 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.03× (z +9.5) | — |
| [[NCI-H1573 (line)]] | alt | 106 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.20× (z +9.5) | — |
| [[NCI-H2030 (line)]] | alt | 146 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.477× (z -10.1) ⚠ toxic |
| [[NCI-H596 (line)]] | alt | 171 | 0 | 1 | — | [[Fulvestrant (drug)]] 5 µM 0.211× (z -10.4) |
| [[NCI-H661 (line)]] | alt | 242 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.246× (z -9.8) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 278 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.241× (z -10.3) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 147 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 107 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4424), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHTF1]] | +0.53 | +0.58 / +0.42 | both halves | 4e-05 |  |
| [[MARK1]] | +0.51 | +0.48 / +0.33 | both halves | 1e-04 |  |
| [[RHBDD3]] | +0.49 | +0.49 / +0.42 | both halves | 4e-05 |  |
| [[NF1]] | +0.49 | +0.41 / +0.38 | both halves | 6e-05 |  |
| [[NR2F1-AS1]] | +0.49 | +0.50 / +0.35 | both halves | 1e-04 |  |
| [[UBB]] | +0.48 | +0.47 / +0.42 | both halves | 4e-05 |  |
| [[KIF21A]] | +0.48 | +0.43 / +0.42 | both halves | 4e-05 |  |
| [[TTC21B]] | +0.47 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[TUBA4A]] | +0.46 | +0.48 / +0.41 | both halves | 4e-05 |  |
| [[ALS2]] | +0.45 | +0.40 / +0.47 | both halves | 4e-05 |  |
| [[CHRNA5]] | +0.44 | +0.61 / +0.40 | both halves | 5e-05 |  |
| [[GLA]] | +0.44 | +0.47 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF141]] | -0.49 | -0.51 / -0.33 | both halves | 1e-04 |  |
| [[TSFM]] | -0.46 | -0.43 / -0.33 | both halves | 1e-04 |  |
| [[TMEM30A-DT]] | -0.45 | -0.33 / -0.22 | both halves | 6e-04 |  |
| [[RFLNA]] | -0.45 | -0.36 / -0.41 | both halves | 1e-04 |  |
| [[HEMK1]] | -0.45 | -0.47 / -0.28 | both halves | 3e-04 |  |
| [[PPP1R15B]] | -0.43 | -0.48 / -0.30 | both halves | 2e-04 |  |
| [[MSTO2P]] | -0.43 | -0.37 / -0.35 | both halves | 1e-04 |  |
| [[DET1]] | -0.41 | -0.46 / -0.31 | both halves | 2e-04 |  |
| [[STT3A]] | -0.41 | -0.36 / -0.35 | both halves | 1e-04 |  |
| [[TSN]] | -0.41 | -0.37 / -0.42 | both halves | 8e-05 |  |
| [[NOMO2]] | -0.41 | -0.31 / -0.29 | both halves | 2e-04 |  |
| [[MMUT]] | -0.41 | -0.47 / -0.26 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAL2]] | B | MAL2 activity lowers SPATS2's level | lines that do not express MAL2 (31) vs lines expressing it (19) | 1.47× higher at baseline in the lines without MAL2 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RAB25, TMEM125, CDH1 |
| [[TUBA4A]] | B | TUBA4A activity lowers SPATS2's level | lines that do not express TUBA4A (13) vs lines expressing it (37) | 1.36× higher at baseline in the lines without TUBA4A | 0.021 | ⚠ within organs, on part of the lines; also absent: TNK1, ETV7, CDCP1; maybe low, not absent |
| [[PSMB5]] | B | PSMB5 activity lowers SPATS2's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 168]]; 25 genes; this gene is in the **-** arm (projection on the module's main direction -0.350). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-14.8, 11.8); signed map (11.6, -6.2). **Vector** length 121, 35.0% of its response variance represented; |z| ≥ 3 in 1,437 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +11.1 | +17.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +10.1 | +15.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +9.9 | +16.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +8.4 | +8.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.6 | +13.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +5.3 | +7.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.7 | +3.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +2.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +1.9 | +2.3 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -8.6 | -16.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -6.0 | -5.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | -6.0 | -4.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.9 | -16.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.9 | -15.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.1 | -5.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.5 | -5.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.4 | -10.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.3 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | spermatogenesis associated serine rich 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.12 — chr12:49,366,584-49,527,425 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SPATA10, SCR59, FLJ13117 |
| Matched by | ensembl_id |

UniProt [Q86XZ4](https://www.uniprot.org/uniprotkb/Q86XZ4) carries no function annotation.

**Summary**, from NCBI Gene [65244](https://www.ncbi.nlm.nih.gov/gene/65244):

> Enables RNA binding activity. Located in cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:18650](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18650) · Entrez [65244](https://www.ncbi.nlm.nih.gov/gene/65244) · UniProt [Q86XZ4](https://www.uniprot.org/uniprotkb/Q86XZ4) · Ensembl [ENSG00000123352](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123352)

## Data

Gene col 4424: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4424); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4424, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4424]; `tensor/DDL_lfc|DDL_z.npy` [4424]; `embed/gene_vectors.npy` [4424]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4424 or target_col == 4424). Every well: [[SPATS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPATS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
