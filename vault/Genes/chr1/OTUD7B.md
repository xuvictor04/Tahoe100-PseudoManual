---
symbol: "OTUD7B"
type: "gene"
col: 15440
ensembl_id: "ENSG00000264522"
name: "OTU deubiquitinase 7B"
location: "1q21.2"
module: 149
arm: "+"
pooled_cpm: 109.36
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 3
n_dd_up_clean: 17
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/149"]
generated_by: "tahoemap"
---

# OTUD7B

*OTU deubiquitinase 7B* — 1q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.81× (z +16.7, q 0e+00, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.423× (z -16.5, q 0e+00, down in 39 of 44 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 10 lines (C-33 A 0.109×, HCT15 0.0871×, NCI-H1792 0.171×, A-427 0.238×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (NCI-H2347 0.256×, NCI-H23 0.264×, NCI-H1573 0.233×, A-172 0.297×, …; ⚠ toxic; transcription drop); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-172 0.595×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[YJU2B]] (+0.64, fdr 2e-05), [[RRAGC]] (+0.58, fdr 1e-05), [[PIGP]] (+0.57, fdr 3e-05); moves opposite to [[PRPS2]] (-0.59, fdr 1e-05), [[SNRPA]] (-0.58, fdr 1e-05), [[PARP1]] (-0.57, fdr 3e-05).
> It is in [[Module 149]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → cells under [[Clofarabine (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 12 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15440.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.81×** | +16.7 | 0e+00 | 42/48 (SW1417, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.79×** | +11.5 | 3e-28 | 45/48 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.66×** | +10.1 | 9e-22 | 41/48 (MIA PaCa-2, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.64×** | +10.1 | 1e-21 | 43/48 (SW480, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.62×** | +10.0 | 2e-21 | 41/49 (SW480, NCI-H1792, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.69×** | +10.0 | 2e-21 | 43/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.65×** | +9.9 | 3e-21 | 42/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.59×** | +9.3 | 2e-18 | 43/48 (C32, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.57×** | +8.9 | 3e-17 | 41/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.49×** | +7.9 | 2e-13 | 39/48 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.38×** | +6.4 | 6e-09 | 32/48 (C32, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.38×** | +6.4 | 6e-09 | 36/48 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.24×** | +6.0 | 1e-07 | 29/49 (COLO 205, RKO, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.36×** | +5.8 | 3e-07 | 35/48 (SK-MEL-2, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~19% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.29×** | +5.0 | 2e-05 | 28/48 (LS 180, LoVo, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.17× | +4.4 | 3e-04 | 13/48 (BT-474, CFPAC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15440.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 10 lines (C-33 A 0.109×, HCT15 0.0871×, NCI-H1792 0.171×, A-427 0.238×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (NCI-H2347 0.256×, NCI-H23 0.264×, NCI-H1573 0.233×, A-172 0.297×, …; ⚠ toxic; transcription drop); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-172 0.595×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.423×** | -16.5 | 0e+00 | 39/44 (C-33 A, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.520×** | -13.0 | 3e-36 | 44/49 (NCI-H2347, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.593×** | -9.5 | 3e-19 | 35/45 (A-172, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | 0.837× | -3.5 | 0.056 | 20/48 (CFPAC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 0.885× | -3.4 | 0.067 | 7/48 (NCI-H23, A498, …) | top dose only |  |
| [[Carbamazepine (drug)]] 5 µM |  | 0.844× | -3.4 | 0.067 | 18/47 (hTERT-HPNE, SNU-423, …) | top dose only |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | 0.848× | -3.3 | 0.079 | 15/48 (hTERT-HPNE, SW480, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.5 µM |  | 0.855× | -3.1 | 0.12 | 21/48 (HOP62, NCI-H1792, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 0.858× | -3.1 | 0.12 | 8/48 (HOP62, A549, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | 0.858× | -3.0 | 0.12 | 14/49 (hTERT-HPNE, A-172, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | 0.859× | -3.0 | 0.12 | 18/48 (HOP62, NCI-H1792, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15440. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 85.0 | 8 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +15.5) | [[Dinaciclib (drug)]] 5 µM 0.431× (z -12.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 76.3 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +15.4) | — |
| [[NCI-H460 (line)]] | wt | 129 | 6 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.429× (z -11.3) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 170 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.05 µM 2.36× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.282× (z -14.1) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 138 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.312× (z -13.6) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 138 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +12.4) | [[Dinaciclib (drug)]] 0.5 µM 0.264× (z -16.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 158 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.222× (z -17.0) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.595× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 151 | 3 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.90× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.393× (z -10.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 70.8 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +13.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 151 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +16.3) | [[Dinaciclib (drug)]] 0.5 µM 0.432× (z -10.5) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 227 | 3 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.81× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.171× (z -21.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 106 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.238× (z -17.1) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 95.5 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +13.2) | [[Dinaciclib (drug)]] 5 µM 0.426× (z -9.7) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 70.6 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.441× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 142 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.256× (z -17.7) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 78.6 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +15.1) | [[Dinaciclib (drug)]] 0.5 µM 0.319× (z -12.3) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 77.4 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +18.5) | — |
| [[A549 (line)]] | wt | 98.0 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +10.0) | [[Dinaciclib (drug)]] 0.05 µM 0.356× (z -11.3) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 69.4 | 1 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 6.32× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.366× (z -9.7) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 62.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +13.6) | — |
| [[NCI-H1573 (line)]] | alt | 116 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.88× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.233× (z -16.2) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 110 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +10.1) | — |
| [[RPMI-7951 (line)]] | alt | 96.9 | 1 | 2 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 2.43× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.319× (z -11.3) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 144 | 2 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.68× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.64× (z +8.9) | [[Dinaciclib (drug)]] 0.05 µM 0.348× (z -12.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 108 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.416× (z -9.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 82.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +12.3) | — |
| [[CFPAC-1 (line)]] | alt | 95.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.391× (z -10.7) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 96.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +13.2) | [[Dinaciclib (drug)]] 5 µM 0.291× (z -10.3) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 129 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.244× (z -14.0) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 61.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +14.7) | — |
| [[SK-MEL-2 (line)]] | alt | 192 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +10.0) | — |
| [[SW 900 (line)]] | alt | 187 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.430× (z -9.6) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 114 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.109× (z -22.4) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 179 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.258× (z -9.7) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 74.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0871× (z -21.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 77.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +11.3) | — |
| [[HOP62 (line)]] | alt | 151 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.291× (z -12.3) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 75.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +10.6) | — |
| [[hTERT-HPNE (line)]] | wt | 113 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.326× (z -9.2) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 111 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.375× (z -8.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 123 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 93.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 68.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 95.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 74.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 75.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 65.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15440), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YJU2B]] | +0.64 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[RRAGC]] | +0.58 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[PIGP]] | +0.57 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[APPBP2-DT]] | +0.57 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[SREK1IP1]] | +0.57 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[AGO4]] | +0.57 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[PIN4]] | +0.56 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[ZNF529-AS1]] | +0.56 | +0.54 / +0.41 | both halves | 4e-05 |  |
| [[TEFM]] | +0.56 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[ANKRD49]] | +0.55 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[ZNF627]] | +0.55 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[NSMCE3]] | +0.55 | +0.42 / +0.48 | both halves | 4e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRPS2]] | -0.59 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[SNRPA]] | -0.58 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[PARP1]] | -0.57 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[APMAP]] | -0.57 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[PRKDC]] | -0.56 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[LRPPRC]] | -0.54 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[ATP2A2]] | -0.54 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[ATP1A1]] | -0.54 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[IPO7]] | -0.54 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[TFDP1]] | -0.53 | -0.58 / -0.40 | both halves | 4e-05 |  |
| [[POLA1]] | -0.53 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[TBC1D8]] | -0.53 | -0.50 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Clofarabine (drug)]] 0.5 µM | C | OTUD7B's natural level raises the cells' numbers under Clofarabine 0.5 µM (protects the cells) | OTUD7B's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.66 | 0.339 over the table, 0.028 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 149]]; 30 genes; every member is in the + arm (projection on the module's main direction 0.494). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-31.4, -38.1); signed map (-6.8, -0.6). **Vector** length 88.5, 26.2% of its response variance represented; |z| ≥ 3 in 1,410 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +6.4 | +4.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.0 | +6.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.4 | +9.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +4.5 | +4.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.0 | +1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.0 | +6.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.4 | +2.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.3 | +2.2 |
| fall | [[Budesonide (drug)]] 5 µM |  | -2.8 | -1.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.6 | -1.5 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -2.4 | -2.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.4 | -2.3 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -2.4 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | OTU deubiquitinase 7B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.2 — chr1:149,937,812-150,010,726 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CEZANNE; previously ZA20D1 |
| Gene groups (HGNC) | OTU domain containing; Zinc fingers A20-type |
| Reactome | 7 pathways, smallest: TNFR1-induced proapoptotic signaling; TNFR1-induced NF-kappa-B signaling pathway; Ovarian tumor domain proteases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6GQQ9](https://www.uniprot.org/uniprotkb/Q6GQQ9) (OTU domain-containing protein 7B):

> Negative regulator of the non-canonical NF-kappa-B pathway that acts by mediating deubiquitination of TRAF3, an inhibitor of the NF-kappa-B pathway, thereby acting as a negative regulator of B-cell responses. In response to non-canonical NF-kappa-B stimuli, deubiquitinates 'Lys-48'-linked polyubiquitin chains of TRAF3, preventing TRAF3 proteolysis and over-activation of non-canonical NF-kappa-B (By similarity). Negatively regulates mucosal immunity against infections (By similarity). …

**Summary**, from NCBI Gene [56957](https://www.ncbi.nlm.nih.gov/gene/56957):

> Enables K48-linked deubiquitinase activity and cysteine-type deubiquitinase activity. Involved in several processes, including negative regulation of protein localization to nucleus; protein deubiquitination; and regulation of intracellular signal transduction. Located in cytoplasm and nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16683](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16683) · Entrez [56957](https://www.ncbi.nlm.nih.gov/gene/56957) · UniProt [Q6GQQ9](https://www.uniprot.org/uniprotkb/Q6GQQ9) · Ensembl [ENSG00000264522](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000264522)

## Data

Gene col 15440: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15440); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15440, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15440]; `tensor/DDL_lfc|DDL_z.npy` [15440]; `embed/gene_vectors.npy` [15440]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15440 or target_col == 15440). Every well: [[OTUD7B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OTUD7B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
