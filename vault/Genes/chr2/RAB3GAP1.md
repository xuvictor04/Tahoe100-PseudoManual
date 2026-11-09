---
symbol: "RAB3GAP1"
type: "gene"
col: 3726
ensembl_id: "ENSG00000115839"
name: "RAB3 GTPase activating protein catalytic subunit 1"
location: "2q21.3"
module: 169
arm: "+"
pooled_cpm: 236.94
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 7
n_dd_up_clean: 14
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/169"]
generated_by: "tahoemap"
---

# RAB3GAP1

*RAB3 GTPase activating protein catalytic subunit 1* — 2q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.18× (z +16.6, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.466× (z -15.7, q 0e+00, down in 43 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.774× (z -7.7, q 1e-12, down in 33 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 9 lines (A549 0.433×, A-172 0.542×, NCI-H1792 0.597×, J82 0.633×, …); [[Dinaciclib (drug)]] 5 µM in 7 lines (SNU-1 0.0579×, C-33 A 0.196×, AsPC-1 0.327×, A-172 0.340×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (RKO 0.142×, CFPAC-1 0.340×, NCI-H2347 0.396×, AsPC-1 0.393×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 1 line (HOP62 0.456×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CNOT4]] (+0.59, fdr 1e-05), [[GPBP1]] (+0.57, fdr 1e-05), [[TXNL1]] (+0.56, fdr 1e-05); moves opposite to [[ZNF850]] (-0.52, fdr 2e-05), [[SUV39H2]] (-0.49, fdr 2e-05), [[NCBP1]] (-0.46, fdr 8e-05).
> It is in [[Module 169]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CCND1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3726.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.18×** | +16.6 | 0e+00 | 48/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.27×** | +13.2 | 3e-37 | 45/49 (SW480, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.76×** | +12.0 | 5e-31 | 47/48 (PANC-1, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.68×** | +11.0 | 5e-26 | 41/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.42×** | +10.6 | 4e-24 | 38/48 (A549, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.60×** | +10.0 | 1e-21 | 46/48 (PANC-1, COLO 205, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.62×** | +9.9 | 3e-21 | 42/47 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.60×** | +9.4 | 3e-19 | 46/48 (PANC-1, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.28×** | +9.2 | 3e-18 | 47/48 (SW480, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.50×** | +8.7 | 2e-16 | 40/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.44×** | +7.8 | 3e-13 | 39/48 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.39×** | +6.7 | 8e-10 | 31/48 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.40×** | +5.1 | 1e-05 | 38/49 (PANC-1, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.23×** | +4.4 | 5e-04 | 26/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.23×** | +4.3 | 5e-04 | 25/48 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tomivosertib (drug)]] 5 µM |  | **1.42×** | +3.9 | 0.003 | 34/48 (LoVo, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 1.18× | +3.5 | 0.015 | 15/47 (SNU-1, HepG2/C3A, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3726.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 9 lines (A549 0.433×, A-172 0.542×, NCI-H1792 0.597×, J82 0.633×, …); [[Dinaciclib (drug)]] 5 µM in 7 lines (SNU-1 0.0579×, C-33 A 0.196×, AsPC-1 0.327×, A-172 0.340×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (RKO 0.142×, CFPAC-1 0.340×, NCI-H2347 0.396×, AsPC-1 0.393×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 1 line (HOP62 0.456×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.466×** | -15.7 | 0e+00 | 43/44 (SNU-1, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.491×** | -15.2 | 0e+00 | 47/49 (RKO, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.563×** | -11.3 | 2e-27 | 41/45 (LOX-IMVI, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.774×** | -7.7 | 1e-12 | 33/49 (A549, A-172, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.767×** | -5.7 | 2e-06 | 37/48 (SW1417, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.787×** | -5.1 | 3e-05 | 27/48 (SW 900, A-427, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.796×** | -4.7 | 2e-04 | 29/47 (CFPAC-1, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Carbamazepine (drug)]] 5 µM |  | 0.854× | -3.4 | 0.051 | 18/47 (SW 1271, SW 900, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.864× | -3.1 | 0.11 | 14/48 (LS 180, LoVo, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 0.868× | -3.0 | 0.14 | 11/48 (NCI-H1573, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3726. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 272 | 13 (3 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.81× (z +19.0) | [[Dinaciclib (drug)]] 0.5 µM 0.386× (z -13.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 219 | 13 (3 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.26× (z +20.8) | [[Dinaciclib (drug)]] 5 µM 0.512× (z -11.3) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 247 | 9 (2 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.08× (z +13.1) | [[Dinaciclib (drug)]] 5 µM 0.0579× (z -31.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 234 | 9 (2 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.68× (z +15.4) | [[Dinaciclib (drug)]] 5 µM 0.421× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.655× (z -9.4) |
| [[HOP62 (line)]] | alt | 206 | 7 (1 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.40× (z +13.6) | [[Auranofin (drug)]] 5 µM 0.456× (z -12.4) |
| [[NCI-H1573 (line)]] | alt | 157 | 8 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.50× (z +18.5) | [[Dinaciclib (drug)]] 5 µM 0.346× (z -12.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 218 | 6 (1 ⚠) | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.10× (z +16.5) | [[Dinaciclib (drug)]] 0.05 µM 0.422× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.597× (z -10.6) |
| [[SW480 (line)]] | alt | 241 | 7 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.37× (z +16.2) | [[Dinaciclib (drug)]] 5 µM 0.450× (z -14.5) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 208 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +16.1) | — |
| [[A-427 (line)]] | wt | 271 | 6 (1 ⚠) | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.15× (z +11.3) | [[Dinaciclib (drug)]] 0.05 µM 0.314× (z -15.8) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 239 | 6 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +18.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -18.3) |
| [[BT-474 (line)]] | alt | 222 | 7 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.46× (z +13.2) | [[Dinaciclib (drug)]] 5 µM 0.441× (z -11.6) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 397 | 4 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 6.65× (z +10.6) | [[Dinaciclib (drug)]] 0.05 µM 0.156× (z -18.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.527× (z -9.6) |
| [[C-33 A (line)]] | alt | 193 | 4 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.57× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.196× (z -19.3) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 268 | 5 (2 ⚠) | 2 (2 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 3.27× (z +16.7) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.04× (z +16.3) | [[Dinaciclib (drug)]] 0.5 µM 0.383× (z -14.1) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 227 | 4 | 3 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 1.97× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.491× (z -10.2) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 292 | 4 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.66× (z +15.0) | [[Dinaciclib (drug)]] 5 µM 0.327× (z -16.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 241 | 5 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.09× (z +12.5) | [[Dinaciclib (drug)]] 0.5 µM 0.535× (z -9.3) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 276 | 4 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +15.1) | [[Dinaciclib (drug)]] 0.5 µM 0.412× (z -12.0) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 343 | 3 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.142× (z -23.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.612× (z -8.5) |
| [[SW 900 (line)]] | alt | 292 | 3 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.71× (z +12.9) | [[Dinaciclib (drug)]] 0.5 µM 0.335× (z -14.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 246 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +14.5) | [[Dinaciclib (drug)]] 5 µM 0.434× (z -11.6) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 287 | 1 | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 3.13× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.340× (z -16.0) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 221 | 2 | 3 (3 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.41× (z +8.8) | [[Dinaciclib (drug)]] 0.05 µM 0.347× (z -10.3) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 234 | 1 | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 3.30× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.396× (z -15.3) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 206 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.340× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.542× (z -13.1) |
| [[HS-578T (line)]] | alt | 156 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +9.6) | — |
| [[HT-29 (line)]] | alt | 254 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.93× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.319× (z -15.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 235 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.51× (z +9.4) | [[Dinaciclib (drug)]] 0.05 µM 0.442× (z -12.2) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 288 | 3 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.71× (z +13.0) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.99× (z +9.3) | — |
| [[hTERT-HPNE (line)]] | wt | 186 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.35× (z +10.6) | — |
| [[Panc 03.27 (line)]] | alt | 227 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.69× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.527× (z -9.9) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 105 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.282× (z -13.3) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 355 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 3.15× (z +8.8) | — |
| [[KATO III (line)]] | alt | 140 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.65× (z +12.1) | — |
| [[LS 180 (line)]] | wt | 297 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.256× (z -11.8) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 91.9 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.12× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.438× (z -9.2) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 275 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.03× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.230× (z -9.9) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 192 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.34× (z +8.8) | — |
| [[HCT15 (line)]] | alt | 257 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.414× (z -10.7) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 204 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.633× (z -10.5) |
| [[SNU-423 (line)]] | alt | 183 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.597× (z -9.5) |
| [[SW48 (line)]] | wt | 254 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.239× (z -13.8) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 202 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 222 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 161 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 264 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 253 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 268 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 220 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3726), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CNOT4]] | +0.59 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[GPBP1]] | +0.57 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[TXNL1]] | +0.56 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[ZNF148]] | +0.54 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[TNKS]] | +0.54 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[RBM27]] | +0.54 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[TENT2]] | +0.53 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[CWC15]] | +0.52 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[UBR2]] | +0.51 | +0.51 / +0.41 | both halves | 4e-05 |  |
| [[SEC24B]] | +0.50 | +0.52 / +0.42 | both halves | 4e-05 |  |
| [[EIF2S2]] | +0.50 | +0.42 / +0.44 | both halves | 4e-05 |  |
| [[MARCHF5]] | +0.50 | +0.55 / +0.38 | both halves | 6e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF850]] | -0.52 | -0.50 / -0.49 | both halves | 2e-05 |  |
| [[SUV39H2]] | -0.49 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[NCBP1]] | -0.46 | -0.43 / -0.37 | both halves | 8e-05 |  |
| [[CCND1]] | -0.45 | -0.45 / -0.36 | both halves | 9e-05 |  |
| [[EIF4EBP2]] | -0.44 | -0.46 / -0.38 | both halves | 6e-05 |  |
| [[PYGO2]] | -0.44 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[MCM7]] | -0.44 | -0.42 / -0.30 | both halves | 2e-04 |  |
| [[ZYX]] | -0.43 | -0.47 / -0.27 | both halves | 3e-04 |  |
| [[SPRY4]] | -0.43 | -0.39 / -0.45 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCND1]] | B | CCND1 activity raises RAB3GAP1's level | lines that do not express CCND1 (7) vs lines expressing it (43) | 1.19× lower at baseline in the lines without CCND1 | 0.073 | ⚠ within organs, on part of the lines; also absent: FSTL3, ADAMTSL5; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 169]]; 25 genes; every member is in the + arm (projection on the module's main direction 0.533). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-13.8, -11.0); signed map (-21.6, 2.6). **Vector** length 86.2, 33.0% of its response variance represented; |z| ≥ 3 in 1,396 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +4.9 | +9.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.8 | +10.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.9 | +12.0 |
|  | [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.6 | +1.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.5 | -15.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.3 | -0.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.3 | -0.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.1 | -0.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.1 | +1.2 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -5.2 | +7.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.8 | -5.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.5 | -7.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.9 | +8.7 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.8 | +2.8 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -2.1 | -1.9 |
|  | [[Fluvoxamine (drug)]] 0.5 µM |  | -2.0 | -0.5 |
|  | [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | -1.8 | -1.6 |
|  | [[Roxadustat (drug)]] 5 µM |  | -1.6 | +0.6 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -1.6 | +1.1 |

## What is on record

|  |  |
|---|---|
| Name | RAB3 GTPase activating protein catalytic subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q21.3 — chr2:135,052,289-135,176,667 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RAB3GAP, KIAA0066, RAB3GAP130, WARBM1 |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 7 pathways, smallest: COPI-independent Golgi-to-ER retrograde traffic; RAB GEFs exchange GTP for GDP on RABs; Rab regulation of trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15042](https://www.uniprot.org/uniprotkb/Q15042) (Rab3 GTPase-activating protein catalytic subunit):

> Catalytic subunit of the Rab3 GTPase-activating (Rab3GAP) complex composed of RAB3GAP1 and RAB3GAP2, which accelerates the otherwise slow GTP hydrolysis catalyzed by Rab proteins. Has GTPase-activating protein (GAP) activity towards various Rab3 subfamily members (RAB3A, RAB3B, RAB3C and RAB3D), RAB5A and RAB43. Additionally, it has guanine nucleotide exchange factor (GEF) activity towards RAB18, promoting GDP release from RAB18 and the conversion of inactive RAB18-GDP to the active form …

**Summary**, from NCBI Gene [22930](https://www.ncbi.nlm.nih.gov/gene/22930):

> This gene encodes the catalytic subunit of a Rab GTPase activating protein. The encoded protein forms a heterodimer with a non-catalytic subunit to specifically regulate the activity of members of the Rab3 subfamily of small G proteins. This protein mediates the hydrolysis of GTP bound Rab3 to the GDP bound form. Mutations in this gene are associated with Warburg micro syndrome. Alternate splicing results in multiple transcript variants.[provided by RefSeq, Feb 2010]

**Accessions** — [HGNC:17063](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17063) · Entrez [22930](https://www.ncbi.nlm.nih.gov/gene/22930) · UniProt [Q15042](https://www.uniprot.org/uniprotkb/Q15042) · Ensembl [ENSG00000115839](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115839)

## Data

Gene col 3726: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3726); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3726, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3726]; `tensor/DDL_lfc|DDL_z.npy` [3726]; `embed/gene_vectors.npy` [3726]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3726 or target_col == 3726). Every well: [[RAB3GAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAB3GAP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
