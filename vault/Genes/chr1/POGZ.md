---
symbol: "POGZ"
type: "gene"
col: 6745
ensembl_id: "ENSG00000143442"
name: "pogo transposable element derived with ZNF domain"
location: "1q21.3"
module: 51
arm: "+"
pooled_cpm: 143.65
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 18
n_dd_up_clean: 5
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# POGZ

*pogo transposable element derived with ZNF domain* — 1q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.55× (z +18.1, q 0e+00, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.480× (z -28.2, q 0e+00, down in 47 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SCAF8]] (+0.73, fdr 7e-06), [[ZFHX2]] (+0.67, fdr 7e-06), [[KMT5B]] (+0.67, fdr 7e-06); moves opposite to [[AHSA1]] (-0.65, fdr 7e-06), [[TIMM10B]] (-0.63, fdr 2e-05), [[TPD52L2]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6745.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.55×** | +18.1 | 0e+00 | 47/49 (SW480, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.55×** | +17.0 | 0e+00 | 40/48 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.60×** | +13.6 | 4e-40 | 44/48 (SW480, NCI-H2030, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.59×** | +12.2 | 2e-32 | 40/48 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.34×** | +7.9 | 2e-13 | 32/48 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.21×** | +5.1 | 3e-05 | 21/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 1.20× | +5.0 | 6e-05 | 21/49 (NCI-H2347, LoVo, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 1.19× | +4.8 | 1e-04 | 20/48 (NCI-H460, A549, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.8 | 1e-04 | 21/48 (SW480, HOP62, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | 1.15× | +3.9 | 0.005 | 19/48 (NCI-H460, A549, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.15× | +3.9 | 0.005 | 17/48 (NCI-H2347, KATO III, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.13× | +3.3 | 0.038 | 14/48 (SW480, HOP62, …) | rises with dose |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 1.08× | +3.0 | 0.11 | 1/48 (NCI-H1573) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6745.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.480×** | -28.2 | 0e+00 | 47/49 (A-172, A549, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.512×** | -17.6 | 0e+00 | 45/50 (SW 900, NCI-H23, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.545×** | -16.5 | 0e+00 | 41/49 (NCI-H23, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.571×** | -14.7 | 0e+00 | 45/48 (C32, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.586×** | -14.6 | 0e+00 | 44/48 (SW480, BT-474, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.578×** | -14.4 | 6e-45 | 38/44 (SK-MEL-2, SHP-77, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.656×** | -11.5 | 9e-29 | 42/48 (LOX-IMVI, A-427, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.666×** | -11.1 | 1e-26 | 40/48 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.663×** | -10.4 | 2e-23 | 36/45 (C-33 A, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.696×** | -9.9 | 3e-21 | 37/48 (SW 1088, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.714×** | -9.2 | 2e-18 | 39/48 (SK-MEL-2, BT-474, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.716×** | -8.6 | 3e-16 | 41/48 (HEC-1-A, HT-29, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.603×** | -7.2 | 2e-11 | 34/45 (H4, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.796×** | -6.2 | 2e-08 | 37/48 (A-172, A-427, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.799×** | -6.1 | 3e-08 | 29/48 (HEC-1-A, CFPAC-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.882× | -4.8 | 6e-05 | 16/48 (A-172, NCI-H661, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.756×** | -4.0 | 0.002 | 25/48 (HEC-1-A, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | 0.846× | -3.2 | 0.030 | 20/48 (SNU-1, hTERT-HPNE, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.894× | -3.0 | 0.057 | 8/48 (NCI-H460, LOX-IMVI, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | 0.858× | -3.0 | 0.068 | 13/49 (MIA PaCa-2, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[vincristine (drug)]] 5 µM |  | **0.819×** | -2.8 | 0.093 | 14/46 (NCI-H1792, NCI-H460, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6745. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 177 | 4 | 10 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 5.22× (z +13.2) | [[Dinaciclib (drug)]] 5 µM 0.211× (z -22.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.344× (z -15.7) |
| [[SW480 (line)]] | alt | 120 | 6 (2 ⚠) | 8 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 7.15× (z +21.3) | [[Auranofin (drug)]] 5 µM 0.514× (z -13.8) |
| [[NCI-H460 (line)]] | wt | 179 | 6 (2 ⚠) | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +18.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.401× (z -22.5) |
| [[HOP62 (line)]] | alt | 137 | 3 | 8 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 3.49× (z +10.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.385× (z -21.1) |
| [[LOX-IMVI (line)]] | wt | 142 | 3 | 8 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.34× (z +12.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -20.8) |
| [[NCI-H2030 (line)]] | alt | 180 | 4 | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +14.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -17.6) |
| [[NCI-H23 (line)]] | alt | 247 | 1 | 10 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +14.8) | [[Dinaciclib (drug)]] 0.5 µM 0.333× (z -16.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -16.1) |
| [[SW 900 (line)]] | alt | 199 | 3 | 7 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.55× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.398× (z -20.1) |
| [[A-172 (line)]] | wt | 239 | 0 | 9 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.304× (z -30.3) |
| [[C32 (line)]] | wt | 116 | 3 (1 ⚠) | 6 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 4.36× (z +9.9) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.195× (z -20.3) |
| [[HEC-1-A (line)]] | alt | 206 | 3 | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.58× (z +10.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.497× (z -16.7) |
| [[MIA PaCa-2 (line)]] | alt | 189 | 0 | 9 (5 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.377× (z -13.6) |
| [[RPMI-7951 (line)]] | alt | 146 | 3 | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +10.0) | [[Dinaciclib (drug)]] 0.05 µM 0.297× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.382× (z -11.8) |
| [[A549 (line)]] | wt | 165 | 4 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +20.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -22.9) |
| [[A-427 (line)]] | wt | 175 | 3 | 4 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 3.56× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.407× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.481× (z -11.3) |
| [[LS 180 (line)]] | wt | 101 | 4 | 3 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +12.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -16.4) |
| [[NCI-H2347 (line)]] | alt | 127 | 4 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +14.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -17.6) |
| [[RKO (line)]] | wt | 124 | 3 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +13.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.442× (z -14.7) |
| [[AsPC-1 (line)]] | alt | 140 | 2 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.504× (z -13.1) |
| [[BT-474 (line)]] | alt | 85.2 | 2 | 4 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.34× (z +9.8) | [[Auranofin (drug)]] 5 µM 0.302× (z -13.3) |
| [[HT-29 (line)]] | alt | 119 | 1 | 5 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.62× (z +10.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.495× (z -13.0) |
| [[NCI-H1792 (line)]] | alt | 173 | 1 | 5 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 4.59× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.422× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.585× (z -11.9) |
| [[SNU-1 (line)]] | wt | 203 | 3 | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.85× (z +13.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.462× (z -14.6) |
| [[H4 (line)]] | wt | 132 | 0 | 5 (2 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.113× (z -12.8) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.497× (z -11.1) |
| [[SW48 (line)]] | wt | 100 | 2 | 3 | [[PH-797804 (drug)]] 5 µM 6.09× (z +9.0) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -9.4) |
| [[A498 (line)]] | wt | 125 | 1 | 3 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 1.80× (z +10.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.442× (z -20.5) |
| [[C-33 A (line)]] | alt | 203 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.128× (z -26.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.581× (z -10.5) |
| [[J82 (line)]] | alt | 140 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -16.6) |
| [[KATO III (line)]] | alt | 87.2 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +11.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.559× (z -10.7) |
| [[PANC-1 (line)]] | alt | 134 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +12.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.519× (z -15.3) |
| [[SHP-77 (line)]] | alt | 234 | 1 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.52× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.252× (z -20.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -16.9) |
| [[SNU-423 (line)]] | alt | 113 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -18.4) |
| [[SW1417 (line)]] | alt | 104 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +12.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.396× (z -19.1) |
| [[CFPAC-1 (line)]] | alt | 129 | 2 | 1 | [[TAK-901 (drug)]] 5 µM 5.29× (z +13.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -22.9) |
| [[hTERT-HPNE (line)]] | wt | 111 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.395× (z -14.3) |
| [[LoVo (line)]] | wt | 87.0 | 2 | 1 | [[TAK-901 (drug)]] 5 µM 4.22× (z +11.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.510× (z -14.6) |
| [[Panc 03.27 (line)]] | alt | 120 | 1 | 2 | [[TAK-901 (drug)]] 5 µM 5.04× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.368× (z -17.1) |
| [[AN3 CA (line)]] | alt | 223 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.356× (z -9.3) |
| [[HepG2_C3A (line)]] | wt | 97.4 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 5.40× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.499× (z -10.0) |
| [[Hs 766T (line)]] | wt | 113 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +10.3) | — |
| [[HS-578T (line)]] | alt | 86.8 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.415× (z -15.6) |
| [[NCI-H1573 (line)]] | alt | 103 | 1 | 1 | [[Harringtonine (drug)]] 5 µM 2.26× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.495× (z -11.7) |
| [[COLO 205 (line)]] | alt | 105 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 11.5× (z +13.3) | — |
| [[HCT15 (line)]] | alt | 159 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.597× (z -8.5) |
| [[NCI-H661 (line)]] | alt | 194 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.368× (z -9.1) |
| [[SW 1088 (line)]] | alt | 104 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0741× (z -10.9) |
| [[CHP-212 (line)]] | wt | 198 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 113 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6745), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCAF8]] | +0.73 | +0.61 / +0.76 | both halves | 7e-06 | STRING 532 |
| [[ZFHX2]] | +0.67 | +0.60 / +0.60 | both halves | 7e-06 | same gene group |
| [[KMT5B]] | +0.67 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[TGIF2]] | +0.67 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[DEDD]] | +0.66 | +0.58 / +0.66 | both halves | 8e-06 |  |
| [[TAB2]] | +0.65 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[TEF]] | +0.64 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[GPATCH8]] | +0.63 | +0.62 / +0.62 | both halves | 7e-06 | same gene group |
| [[ZNF776]] | +0.63 | +0.55 / +0.61 | both halves | 1e-05 | same gene group |
| [[CCDC148]] | +0.62 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[BRAF]] | +0.62 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[EPC1]] | +0.62 | +0.59 / +0.57 | both halves | 9e-06 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AHSA1]] | -0.65 | -0.59 / -0.62 | both halves | 7e-06 |  |
| [[TIMM10B]] | -0.63 | -0.48 / -0.67 | both halves | 2e-05 |  |
| [[TPD52L2]] | -0.61 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[ZCCHC17]] | -0.61 | -0.50 / -0.64 | both halves | 1e-05 |  |
| [[MFN1]] | -0.57 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[DGKE]] | -0.57 | -0.42 / -0.63 | both halves | 4e-05 |  |
| [[VPS53]] | -0.56 | -0.40 / -0.62 | both halves | 4e-05 |  |
| [[GDAP2]] | -0.56 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[RARS2]] | -0.55 | -0.43 / -0.60 | both halves | 3e-05 |  |
| [[GOLT1B]] | -0.55 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[GHITM]] | -0.55 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[GPR89A]] | -0.55 | -0.47 / -0.54 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises POGZ's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[BHLHE41]] | C | BHLHE41 activity weakens POGZ's drug response | lines that do not express BHLHE41 (19) vs lines expressing it (31) | the lines without BHLHE41 respond 1.06× as strongly (z diff -0.95); rises at some drug-doses, falls at others (68% from rises): Homoharringtonine 5 µM: 1.71x vs 1.40x (z diff -3.1); Harringtonine 5 µM: 1.66x vs 1.47x (z diff -1.8); Doxorubicin (hydrochloride) 5 µM: 0.58x vs 0.53x (z diff -1.1) | 0.050 | ⚠ within organs, on part of the lines; also absent: RAC2, JHY, ENSG00000289600; rises at some drug-doses, falls at others; rests on the correction; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.688). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-25.7, 12.9); signed map (7.9, -18.3). **Vector** length 121, 40.8% of its response variance represented; |z| ≥ 3 in 1,307 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +12.0 | +12.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +10.3 | +17.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +9.9 | +18.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.6 | +2.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +7.1 | +5.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +7.0 | +13.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +3.4 | +3.9 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +2.9 | +1.0 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.7 | -0.0 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -8.9 | -8.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -8.5 | -9.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -7.2 | -6.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.8 | -14.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -6.7 | -17.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.9 | -3.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.6 | -1.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.4 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | pogo transposable element derived with ZNF domain |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.3 — chr1:151,402,724-151,459,494 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0461, ZNF635, ZNF280E |
| Gene groups (HGNC) | Zinc fingers C2H2-type; Helix-turn-helix CENPB type domain family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z3K3](https://www.uniprot.org/uniprotkb/Q7Z3K3) (Pogo transposable element with ZNF domain):

> Plays a role in mitotic cell cycle progression and is involved in kinetochore assembly and mitotic sister chromatid cohesion. Probably through its association with CBX5 plays a role in mitotic chromosome segregation by regulating aurora kinase B/AURKB activation and AURKB and CBX5 dissociation from chromosome arms. Promotes the repair of DNA double-strand breaks through the homologous recombination pathway.

**Summary**, from NCBI Gene [23126](https://www.ncbi.nlm.nih.gov/gene/23126):

> The protein encoded by this gene appears to be a zinc finger protein containing a transposase domain at the C-terminus. This protein was found to interact with the transcription factor SP1 in a yeast two-hybrid system. Alternatively spliced transcript variants encoding distinct isoforms have been observed. [provided by RefSeq, Aug 2010]

**Accessions** — [HGNC:18801](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18801) · Entrez [23126](https://www.ncbi.nlm.nih.gov/gene/23126) · UniProt [Q7Z3K3](https://www.uniprot.org/uniprotkb/Q7Z3K3) · Ensembl [ENSG00000143442](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143442)

## Data

Gene col 6745: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6745); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6745, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6745]; `tensor/DDL_lfc|DDL_z.npy` [6745]; `embed/gene_vectors.npy` [6745]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6745 or target_col == 6745). Every well: [[POGZ — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POGZ.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
