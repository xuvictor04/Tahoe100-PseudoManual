---
symbol: "FARP2"
type: "gene"
col: 118
ensembl_id: "ENSG00000006607"
name: "FERM, ARH/RhoGEF and pleckstrin domain protein 2"
location: "2q37.3"
module: 28
arm: "-"
pooled_cpm: 93.85
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 2
n_dd_up_clean: 15
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# FARP2

*FERM, ARH/RhoGEF and pleckstrin domain protein 2* — 2q37.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.38× (z +27.8, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.560× (z -13.3, q 2e-37, down in 41 of 49 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (COLO 205 0.235×, LS 180 0.343×, SW1417 0.393×, HepG2/C3A 0.345×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (SHP-77 0.282×, HEC-1-A 0.336×, NCI-H460 0.414×; ⚠ toxic; transcription drop); [[Radotinib (drug)]] 0.5 µM in 1 line (SW 1271 0.0603×); [[Tadalafil (drug)]] 0.05 µM in 1 line (SW 1271 0.0565×); [[Auranofin (drug)]] 5 µM in 1 line (COLO 205 0.440×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MLXIP]] (+0.64, fdr 7e-06), [[GRK6]] (+0.63, fdr 1e-05), [[SMG1P2]] (+0.60, fdr 1e-05); moves opposite to [[RAD52]] (-0.61, fdr 1e-05), [[NDUFA5]] (-0.60, fdr 1e-05), [[LINC00265]] (-0.59, fdr 5e-05).
> It sits in the **-** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CFL2]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 118.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.38×** | +27.8 | 0e+00 | 47/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.72×** | +22.9 | 0e+00 | 47/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.68×** | +22.5 | 0e+00 | 47/48 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.65×** | +11.5 | 3e-28 | 33/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.36×** | +10.0 | 3e-21 | 32/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.44×** | +8.3 | 9e-15 | 36/48 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.29×** | +8.3 | 1e-14 | 26/49 (AsPC-1, NCI-H460, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.42×** | +8.0 | 1e-13 | 34/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.40×** | +7.7 | 9e-13 | 35/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.39×** | +7.6 | 2e-12 | 38/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.34×** | +6.7 | 8e-10 | 28/48 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.34×** | +6.7 | 9e-10 | 34/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.32×** | +6.3 | 1e-08 | 30/48 (NCI-H1573, SW 900, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.67×** | +6.1 | 4e-08 | 36/48 (CFPAC-1, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.62×** | +5.8 | 3e-07 | 31/49 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.48×** | +4.7 | 8e-05 | 25/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.16× | +3.5 | 0.015 | 16/49 (NCI-H2347, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 118.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (COLO 205 0.235×, LS 180 0.343×, SW1417 0.393×, HepG2/C3A 0.345×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (SHP-77 0.282×, HEC-1-A 0.336×, NCI-H460 0.414×; ⚠ toxic; transcription drop); [[Radotinib (drug)]] 0.5 µM in 1 line (SW 1271 0.0603×); [[Tadalafil (drug)]] 0.05 µM in 1 line (SW 1271 0.0565×); [[Auranofin (drug)]] 5 µM in 1 line (COLO 205 0.440×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.560×** | -13.3 | 2e-37 | 41/49 (COLO 205, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.687×** | -8.3 | 4e-14 | 33/44 (SHP-77, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.888× | -3.9 | 0.020 | 15/48 (SNU-1, A-427, …) | rises with dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.834× | -3.6 | 0.042 | 20/45 (LS 180, SW1417, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.857× | -3.5 | 0.043 | 15/48 (A-172, A549, …) | inconsistent across doses |  |
| [[Carbamazepine (drug)]] 5 µM |  | 0.859× | -3.5 | 0.043 | 13/47 (NCI-H460, AsPC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.841× | -3.5 | 0.043 | 18/47 (A549, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Radotinib (drug)]] 5 µM |  | 0.900× | -3.4 | 0.043 | 11/48 (hTERT-HPNE, PANC-1, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~32% of this change | 0.862× | -3.4 | 0.043 | 22/48 (SW1417, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 0.865× | -3.3 | 0.049 | 18/48 (A-172, A-427, …) | inconsistent across doses |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.867× | -3.3 | 0.050 | 14/48 (COLO 205, A549, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.867× | -3.3 | 0.050 | 12/48 (HOP62, A-172, …) | rises with dose |  |
| [[Fingolimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 0.875× | -3.1 | 0.100 | 7/48 (BT-474, RKO, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 118. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 79.6 | 11 (2 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.67× (z +19.2) | [[Dinaciclib (drug)]] 5 µM 0.414× (z -10.6) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 75.1 | 10 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.04× (z +26.9) | — |
| [[COLO 205 (line)]] | alt | 168 | 5 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +15.6) | [[Dinaciclib (drug)]] 0.5 µM 0.235× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.440× (z -8.7) |
| [[AsPC-1 (line)]] | alt | 131 | 6 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.52× (z +18.7) ⚠ cell-cycle shift, explains ~16% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 4.24× (z +15.2) | [[Dinaciclib (drug)]] 5 µM 0.361× (z -10.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 135 | 3 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.49× (z +11.6) | [[Dinaciclib (drug)]] 0.5 µM 0.343× (z -13.6) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 129 | 5 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.16× (z +13.4) | [[Dinaciclib (drug)]] 0.5 µM 0.469× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 68.8 | 5 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.04× (z +13.9) | [[Dinaciclib (drug)]] 0.5 µM 0.410× (z -11.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 87.7 | 5 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.07× (z +15.6) | [[Dinaciclib (drug)]] 5 µM 0.436× (z -9.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 142 | 3 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.56× (z +17.8) | [[Dinaciclib (drug)]] 0.5 µM 0.393× (z -13.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 90.1 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.20× (z +13.2) | [[Harringtonine (drug)]] 0.5 µM 0.422× (z -9.8) ⚠ cell-cycle shift, explains ~12% of this change |
| [[A-427 (line)]] | wt | 80.6 | 2 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.12× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.446× (z -9.2) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 104 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.26× (z +13.2) | [[Dinaciclib (drug)]] 5 µM 0.426× (z -9.3) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 108 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.60× (z +14.0) | [[Dinaciclib (drug)]] 0.5 µM 0.537× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 88.8 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.93× (z +16.6) | — |
| [[NCI-H1792 (line)]] | alt | 72.1 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.42× (z +16.0) | — |
| [[NCI-H23 (line)]] | alt | 105 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.67× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.399× (z -10.5) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 68.7 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.88× (z +13.3) | — |
| [[A498 (line)]] | wt | 65.8 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.43× (z +15.0) | — |
| [[A549 (line)]] | wt | 78.0 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.73× (z +16.0) | [[Dinaciclib (drug)]] 5 µM 0.460× (z -9.1) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 78.0 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.71× (z +14.8) | — |
| [[H4 (line)]] | wt | 74.6 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.68× (z +12.2) | [[Torkinib (drug)]] 5 µM 0.111× (z -9.1) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 80.9 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.34× (z +15.4) | [[Dinaciclib (drug)]] 5 µM 0.336× (z -13.5) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 135 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.02× (z +15.0) | [[Dinaciclib (drug)]] 0.5 µM 0.345× (z -11.6) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 165 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.95× (z +13.3) | [[Dinaciclib (drug)]] 0.5 µM 0.455× (z -9.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 82.7 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.83× (z +19.1) | — |
| [[NCI-H2030 (line)]] | alt | 63.2 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.49× (z +13.9) | [[Dinaciclib (drug)]] 0.5 µM 0.392× (z -10.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 110 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.33× (z +12.4) | [[Dinaciclib (drug)]] 0.5 µM 0.495× (z -10.5) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 83.3 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.53× (z +14.0) | [[Dinaciclib (drug)]] 5 µM 0.282× (z -13.6) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 44.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.48× (z +14.1) | — |
| [[HS-578T (line)]] | alt | 71.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.23× (z +11.8) | — |
| [[hTERT-HPNE (line)]] | wt | 78.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.02× (z +11.4) | — |
| [[J82 (line)]] | alt | 59.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.31× (z +13.4) | — |
| [[LOX-IMVI (line)]] | wt | 61.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.69× (z +13.5) | — |
| [[RPMI-7951 (line)]] | alt | 94.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.78× (z +12.3) | — |
| [[SNU-423 (line)]] | alt | 61.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.49× (z +15.7) | — |
| [[BT-474 (line)]] | alt | 117 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.42× (z +9.3) | — |
| [[HCT15 (line)]] | alt | 87.1 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.46× (z +11.1) | — |
| [[RKO (line)]] | wt | 119 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +12.6) | — |
| [[SK-MEL-2 (line)]] | alt | 216 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.452× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW 1271 (line)]] | alt | 115 | 0 | 2 | — | [[Radotinib (drug)]] 0.5 µM 0.0603× (z -13.8) |
| [[C-33 A (line)]] | alt | 132 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.315× (z -11.4) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 107 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.517× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 78.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.04× (z +8.5) | — |
| [[AN3 CA (line)]] | alt | 119 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 113 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 67.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 83.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 92.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 71.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 118), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*41 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MLXIP]] | +0.64 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[GRK6]] | +0.63 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[SMG1P2]] | +0.60 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[PITPNA]] | +0.57 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[TBC1D16]] | +0.56 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[GATAD2A]] | +0.55 | +0.57 / +0.52 | both halves | 1e-05 | same gene group |
| [[KIAA0232]] | +0.55 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[AXIN1]] | +0.54 | +0.44 / +0.44 | both halves | 3e-05 |  |
| [[VKORC1L1]] | +0.53 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[LMBR1]] | +0.53 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[SH2B2]] | +0.52 | +0.42 / +0.41 | both halves | 4e-05 | same gene group |
| [[TPST2]] | +0.52 | +0.45 / +0.44 | both halves | 3e-05 | same gene group |

## Genes that move opposite

*59 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAD52]] | -0.61 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[NDUFA5]] | -0.60 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[LINC00265]] | -0.59 | -0.56 / -0.39 | both halves | 5e-05 |  |
| [[CLK4]] | -0.58 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[AMZ2P1]] | -0.56 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[SEPSECS]] | -0.55 | -0.46 / -0.48 | both halves | 2e-05 |  |
| [[TRUB1]] | -0.55 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[MIR181A2HG]] | -0.55 | -0.34 / -0.54 | both halves | 1e-04 |  |
| [[OSGIN2]] | -0.54 | -0.54 / -0.46 | both halves | 2e-05 |  |
| [[COMMD3]] | -0.54 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[FAM200B]] | -0.54 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[FAM111A-DT]] | -0.54 | -0.40 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CFL2]] | C | CFL2 activity lowers FARP2's level | lines that do not express CFL2 (4) vs lines expressing it (45) | 1.70× higher at baseline in the lines without CFL2 | 0.089 | ⚠ few lines (4 vs 45); within organs, on part of the lines; also absent: TPST1, SLC35F1, ITGA2B; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **-** arm (projection on the module's main direction -0.578). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-15.7, 7.6); signed map (-47.2, 23.1). **Vector** length 98.5, 28.9% of its response variance represented; |z| ≥ 3 in 1,170 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +3.7 | +27.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.4 | +22.9 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.1 | +22.5 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +2.9 | +5.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.9 | +6.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.7 | +6.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +6.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.2 | +2.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.9 | +2.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.7 | +3.3 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | -6.2 | -3.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -6.0 | +1.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.0 | +2.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.2 | -3.9 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -5.2 | +0.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.3 | -1.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.1 | -3.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.0 | -3.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.2 | -3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | FERM, ARH/RhoGEF and pleckstrin domain protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q37.3 — chr2:241,356,285-241,494,841 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0793, FIR, PLEKHC3, FRG |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Dbl family Rho GEFs; FERM domain containing; MicroRNA protein coding host genes |
| Reactome | 14 pathways, smallest: SEMA3A-Plexin repulsion signaling by inhibiting Integrin adhesion; SRC activates STAT3 in a quantitative manner, through Cadherin-11 (CDH11), RAC1 and gp130 (IL6ST); Semaphorin interactions |
| Matched by | ensembl_id |

**Function**, from UniProt [O94887](https://www.uniprot.org/uniprotkb/O94887) (FERM, ARHGEF and pleckstrin domain-containing protein 2):

> Functions as a guanine nucleotide exchange factor that activates RAC1. May have relatively low activity. Plays a role in the response to class 3 semaphorins and remodeling of the actin cytoskeleton. Plays a role in TNFSF11-mediated osteoclast differentiation, especially in podosome rearrangement and reorganization of the actin cytoskeleton. Regulates the activation of ITGB3, integrin signaling and cell adhesion (By similarity).

**Summary**, from NCBI Gene [9855](https://www.ncbi.nlm.nih.gov/gene/9855):

> Enables guanyl-nucleotide exchange factor activity. Acts upstream of or within Rac protein signal transduction and neuron remodeling. Located in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16460](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16460) · Entrez [9855](https://www.ncbi.nlm.nih.gov/gene/9855) · UniProt [O94887](https://www.uniprot.org/uniprotkb/O94887) · Ensembl [ENSG00000006607](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000006607)

## Data

Gene col 118: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 118); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 118, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 118]; `tensor/DDL_lfc|DDL_z.npy` [118]; `embed/gene_vectors.npy` [118]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 118 or target_col == 118). Every well: [[FARP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FARP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
