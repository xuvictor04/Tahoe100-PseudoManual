---
symbol: "SPATA5"
type: "gene"
col: 6984
ensembl_id: "ENSG00000145375"
name: "AAA ATPase AFG2A"
location: "4q28.1"
module: 36
arm: "+"
pooled_cpm: 88.67
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 4
n_dd_up_clean: 13
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# SPATA5

*AAA ATPase AFG2A* — 4q28.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.58× (z +18.5, q 0e+00, up in 48 of 48 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 2.12× (z +10.9, q 1e-25, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.642× (z -9.0, q 8e-17, down in 31 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 9 lines (HepG2/C3A 0.198×, PANC-1 0.387×, A-427 0.370×, LoVo 0.428×, …); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 6 lines (A498 0.351×, NCI-H460 0.406×, HepG2/C3A 0.362×, SK-MEL-2 0.448×, …); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SNU-1 0.0778×, C-33 A 0.156×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRIM2]] (+0.80, fdr 7e-06), [[HERC2]] (+0.79, fdr 7e-06), [[EIPR1]] (+0.74, fdr 7e-06); moves opposite to [[RSRP1]] (-0.67, fdr 7e-06), [[ZNF490]] (-0.64, fdr 1e-05), [[CHCHD7]] (-0.64, fdr 5e-05).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TSEN2]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 6 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6984.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **3.58×** | +18.5 | 0e+00 | 48/48 (NCI-H2347, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **3.02×** | +16.0 | 0e+00 | 48/48 (A549, AsPC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.64×** | +14.1 | 9e-43 | 48/48 (NCI-H2347, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.12×** | +10.9 | 1e-25 | 43/48 (NCI-H1573, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.98×** | +9.9 | 4e-21 | 42/48 (HOP62, NCI-H1573, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.87×** | +9.1 | 1e-17 | 43/48 (hTERT-HPNE, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.89×** | +8.8 | 2e-16 | 40/48 (BT-474, A549, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.71×** | +7.8 | 6e-13 | 42/48 (A-172, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.56×** | +6.4 | 8e-09 | 33/48 (HEC-1-A, A549, …) | all doses, flat | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.49×** | +5.8 | 4e-07 | 37/47 (H4, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.07×** | +5.5 | 2e-06 | 40/49 (A549, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.42×** | +5.1 | 2e-05 | 27/48 (A549, hTERT-HPNE, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.41×** | +4.9 | 3e-05 | 29/48 (HEC-1-A, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.37×** | +4.5 | 2e-04 | 25/48 (A549, HEC-1-A, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.65×** | +3.8 | 0.006 | 26/45 (PANC-1, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~16% here); noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.20× | +3.7 | 0.008 | 22/48 (SNU-423, HS-578T, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.29×** | +3.5 | 0.015 | 22/47 (HEC-1-A, NCI-H2347, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.59×** | +3.5 | 0.015 | 21/49 (NCI-H460, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.25×** | +3.1 | 0.050 | 21/48 (NCI-H1792, NCI-H23, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.23×** | +3.0 | 0.071 | 20/48 (MIA PaCa-2, hTERT-HPNE, …) | top dose only |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.16× | +3.0 | 0.071 | 12/48 (Hs 766T, J82, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6984.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 9 lines (HepG2/C3A 0.198×, PANC-1 0.387×, A-427 0.370×, LoVo 0.428×, …); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 6 lines (A498 0.351×, NCI-H460 0.406×, HepG2/C3A 0.362×, SK-MEL-2 0.448×, …); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SNU-1 0.0778×, C-33 A 0.156×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.642×** | -9.0 | 8e-17 | 31/48 (HepG2/C3A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.676×** | -8.0 | 4e-13 | 34/49 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.816×** | -4.2 | 0.006 | 26/48 (LS 180, A-427, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.776×** | -3.7 | 0.030 | 24/48 (H4, RPMI-7951, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 0.800× | -3.1 | 0.19 | 16/48 (AsPC-1, LOX-IMVI, …) | top dose only | plate-row cell shift; position effect removed |
| [[Entrectinib (drug)]] 5 µM |  | 0.809× | -3.1 | 0.19 | 21/48 (KATO III, LoVo, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.797× | -3.0 | 0.19 | 18/48 (COLO 205, A-427, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.61 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6984. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 49.4 | 8 (5 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.82× (z +13.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 4.14× (z +11.1) | — |
| [[PANC-1 (line)]] | alt | 80.4 | 5 (3 ⚠) | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.59× (z +11.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.24× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -16.3) |
| [[HepG2_C3A (line)]] | wt | 82.6 | 3 (2 ⚠) | 4 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.64× (z +10.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.99× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -18.0) |
| [[HEC-1-A (line)]] | alt | 119 | 5 (2 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.76× (z +9.7) | [[Lonafarnib (drug)]] 5 µM 0.127× (z -10.3) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 142 | 3 (3 ⚠) | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.79× (z +10.1) ⚠ cell-cycle shift, explains ~28% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.202× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.420× (z -12.1) |
| [[HOP62 (line)]] | alt | 60.9 | 5 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.04× (z +13.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 4.48× (z +11.0) | — |
| [[NCI-H1573 (line)]] | alt | 62.3 | 5 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.41× (z +11.7) | — |
| [[NCI-H460 (line)]] | wt | 167 | 3 (2 ⚠) | 2 | [[TAK-901 (drug)]] 5 µM 5.82× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -13.6) |
| [[A-172 (line)]] | wt | 67.2 | 4 (3 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 4.32× (z +11.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 3.05× (z +8.5) | — |
| [[C32 (line)]] | wt | 77.7 | 3 (3 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 5.60× (z +13.2) ⚠ cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -10.4) |
| [[H4 (line)]] | wt | 71.3 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.93× (z +10.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 5.84× (z +9.5) | — |
| [[hTERT-HPNE (line)]] | wt | 49.0 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 8.62× (z +12.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 4.70× (z +9.2) | — |
| [[LoVo (line)]] | wt | 134 | 3 (3 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 3.00× (z +11.4) ⚠ cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -12.5) |
| [[LOX-IMVI (line)]] | wt | 57.1 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.04× (z +13.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.89× (z +8.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 65.6 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.60× (z +13.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.95× (z +9.3) | — |
| [[NCI-H1792 (line)]] | alt | 47.9 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 7.72× (z +15.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 4.64× (z +11.2) | — |
| [[NCI-H2347 (line)]] | alt | 36.7 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.11× (z +15.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.25× (z +9.7) | — |
| [[SW 900 (line)]] | alt | 33.6 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.87× (z +12.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.77× (z +8.6) | — |
| [[SW480 (line)]] | alt | 64.1 | 3 (3 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 2.53× (z +9.9) ⚠ cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.467× (z -11.5) |
| [[A-427 (line)]] | wt | 149 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -15.1) |
| [[AsPC-1 (line)]] | alt | 25.5 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 10.9× (z +15.3) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[BT-474 (line)]] | alt | 46.0 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.07× (z +9.7) | — |
| [[CFPAC-1 (line)]] | alt | 38.1 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.12× (z +13.7) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[HS-578T (line)]] | alt | 41.5 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.21× (z +12.3) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[HT-29 (line)]] | alt | 74.7 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.57× (z +11.7) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[Panc 03.27 (line)]] | alt | 74.2 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.78× (z +12.3) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[RPMI-7951 (line)]] | alt | 61.5 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.08× (z +11.2) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[SNU-1 (line)]] | wt | 127 | 1 (1 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.37× (z +10.7) ⚠ cell-cycle shift, explains ~28% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.0778× (z -17.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 40.9 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.22× (z +12.9) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[C-33 A (line)]] | alt | 213 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.156× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -11.2) |
| [[LS 180 (line)]] | wt | 111 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.15× (z +9.4) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H2030 (line)]] | alt | 104 | 1 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.35× (z +8.9) ⚠ cell-cycle shift, explains ~28% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.422× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 205 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.210× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.560× (z -8.8) |
| [[A498 (line)]] | wt | 139 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -14.5) |
| [[AN3 CA (line)]] | alt | 187 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -12.4) |
| [[HCT15 (line)]] | alt | 92.9 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.79× (z +9.6) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[J82 (line)]] | alt | 125 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.472× (z -10.1) |
| [[KATO III (line)]] | alt | 77.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -9.9) |
| [[NCI-H661 (line)]] | alt | 94.2 | 0 | 1 | — | [[GSK1059615 (drug)]] 0.5 µM 0.0513× (z -9.0) |
| [[RKO (line)]] | wt | 111 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.59× (z +9.3) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[SHP-77 (line)]] | alt | 98.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.414× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 58.3 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.80× (z +8.6) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[SW48 (line)]] | wt | 113 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.33× (z +8.8) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[CHP-212 (line)]] | wt | 71.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 60.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 109 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 68.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 66.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 79.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 90.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6984), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRIM2]] | +0.80 | +0.84 / +0.73 | both halves | 7e-06 |  |
| [[HERC2]] | +0.79 | +0.78 / +0.76 | both halves | 7e-06 |  |
| [[EIPR1]] | +0.74 | +0.77 / +0.69 | both halves | 7e-06 |  |
| [[MRPS27]] | +0.72 | +0.72 / +0.70 | both halves | 7e-06 |  |
| [[CHCHD6]] | +0.71 | +0.64 / +0.76 | both halves | 7e-06 |  |
| [[MTAP]] | +0.69 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[CHCHD3]] | +0.68 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[EXOC2]] | +0.67 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[COA1]] | +0.67 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[FAF1]] | +0.67 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[TCOF1]] | +0.66 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[HERC2P9]] | +0.66 | +0.69 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RSRP1]] | -0.67 | -0.69 / -0.61 | both halves | 7e-06 |  |
| [[ZNF490]] | -0.64 | -0.65 / -0.49 | both halves | 1e-05 |  |
| [[CHCHD7]] | -0.64 | -0.67 / -0.40 | both halves | 5e-05 |  |
| [[ZNF821]] | -0.63 | -0.57 / -0.57 | both halves | 9e-06 |  |
| [[ABCA5]] | -0.63 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[KDM5B]] | -0.62 | -0.69 / -0.57 | both halves | 1e-05 |  |
| [[HMGCL]] | -0.61 | -0.55 / -0.61 | both halves | 1e-05 |  |
| [[TCEAL3]] | -0.60 | -0.63 / -0.49 | both halves | 1e-05 |  |
| [[FAM117A]] | -0.60 | -0.61 / -0.49 | both halves | 1e-05 |  |
| [[ZMYM5]] | -0.60 | -0.59 / -0.58 | both halves | 8e-06 |  |
| [[ZNF425]] | -0.60 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[UPK2]] | -0.59 | -0.45 / -0.59 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TSEN2]] | C | TSEN2 activity raises SPATA5's level | lines that do not express TSEN2 (3) vs lines expressing it (47) | 2.57× lower at baseline in the lines without TSEN2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TMEM9B-AS1, NDC80, CSPG5; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.682). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-8.8, -33.0); signed map (-14.9, -50.8). **Vector** length 147, 52.7% of its response variance represented; |z| ≥ 3 in 1,225 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +9.5 | +10.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +9.4 | +9.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +7.7 | +8.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +6.5 | +6.4 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | +6.0 | +5.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +5.3 | +3.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.7 | +2.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.5 | +3.5 |
|  | [[Acetohexamide (drug)]] 5 µM |  | +3.3 | +2.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -13.5 | -9.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -12.1 | -8.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | -7.3 | -2.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | -5.9 | -2.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.8 | +1.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.0 | +0.7 |
|  | [[Entrectinib (drug)]] 5 µM |  | -3.7 | -3.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.1 | -1.9 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.8 | -3.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.7 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | AAA ATPase AFG2A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q28.1 — chr4:122,923,070-123,319,433 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SPAF, AFG2; previously SPATA5 |
| Gene groups (HGNC) | AAA ATPases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NB90](https://www.uniprot.org/uniprotkb/Q8NB90) (ATPase family gene 2 protein homolog A):

> ATP-dependent chaperone part of the 55LCC heterohexameric ATPase complex which is chromatin-associated and promotes replisome proteostasis to maintain replication fork progression and genome stability. Required for replication fork progression, sister chromatid cohesion, and chromosome stability. The ATPase activity is specifically enhanced by replication fork DNA and is coupled to cysteine protease-dependent cleavage of replisome substrates in response to replication fork damage. Uses ATPase …

**Summary**, from NCBI Gene [166378](https://www.ncbi.nlm.nih.gov/gene/166378):

> This gene encodes a member of the ATPase associated with diverse activities family, whose members are defined by a highly conserved ATPase domain. Members of this family participate in diverse cellular processes that include membrane fusion, DNA replication, microtubule severing, and protein degradation. The protein encoded by this gene has a putative mitochondrial targeting sequence and has been proposed to function in maintenance of mitochondrial function and integrity during mouse …

**Accessions** — [HGNC:18119](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18119) · Entrez [166378](https://www.ncbi.nlm.nih.gov/gene/166378) · UniProt [Q8NB90](https://www.uniprot.org/uniprotkb/Q8NB90) · Ensembl [ENSG00000145375](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145375)

## Data

Gene col 6984: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6984); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6984, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6984]; `tensor/DDL_lfc|DDL_z.npy` [6984]; `embed/gene_vectors.npy` [6984]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6984 or target_col == 6984). Every well: [[SPATA5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPATA5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
