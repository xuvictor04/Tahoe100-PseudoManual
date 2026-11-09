---
symbol: "PDIA3"
type: "gene"
col: 9403
ensembl_id: "ENSG00000167004"
name: "protein disulfide isomerase family A member 3"
location: "15q15.3"
module: 42
arm: "+"
pooled_cpm: 426.52
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 19
n_dd_up_clean: 7
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# PDIA3

*protein disulfide isomerase family A member 3* — 15q15.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.47× (z +15.3, q 0e+00, up in 48 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.56× (z +10.7, q 2e-24, up in 43 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.498× (z -16.6, q 0e+00, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDIA6]] (+0.93, fdr 7e-06), [[DDOST]] (+0.83, fdr 7e-06), [[CANX]] (+0.78, fdr 7e-06); moves opposite to [[NSUN5]] (-0.62, fdr 1e-05), [[SNHG11]] (-0.60, fdr 8e-06), [[NT5C]] (-0.59, fdr 3e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MTOR]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9403.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.47×** | +15.3 | 0e+00 | 48/49 (A-427, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.53×** | +15.1 | 0e+00 | 44/44 (SHP-77, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.03×** | +11.1 | 2e-26 | 44/45 (Panc 03.27, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +10.7 | 2e-24 | 43/49 (AsPC-1, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +7.0 | 4e-10 | 37/50 (LOX-IMVI, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.11×** | +6.6 | 4e-09 | 45/49 (LOX-IMVI, C32, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.02×** | +6.2 | 4e-08 | 41/48 (SW48, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.32×** | +4.8 | 1e-04 | 34/48 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.62×** | +4.3 | 0.001 | 28/38 (NCI-H2347, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.27×** | +4.0 | 0.003 | 26/48 (SW480, PANC-1, …) | two highest doses | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.26×** | +4.0 | 0.003 | 29/48 (HT-29, SW480, …) | top dose only |  |
| [[Raltitrexed (drug)]] 0.5 µM |  | **1.23×** | +3.5 | 0.025 | 26/48 (LoVo, PANC-1, …) | two highest doses |  |
| [[Arbutin (drug)]] 5 µM |  | **1.22×** | +3.3 | 0.048 | 30/48 (hTERT-HPNE, SNU-423, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | 1.20× | +3.0 | 0.10 | 23/48 (SNU-423, LOX-IMVI, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9403.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.498×** | -16.6 | 0e+00 | 45/48 (H4, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.588×** | -8.9 | 1e-16 | 37/48 (A-427, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.624×** | -7.6 | 4e-12 | 42/48 (KATO III, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.885× | -7.1 | 1e-10 | 2/50 (NCI-H23, SW 1271) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.787×** | -5.7 | 1e-06 | 31/48 (RPMI-7951, RKO, …) | inconsistent across doses | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.705×** | -5.6 | 2e-06 | 44/47 (SK-MEL-2, C32, …) | rises with dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.729×** | -5.3 | 9e-06 | 35/48 (RPMI-7951, A-172, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.741×** | -5.0 | 3e-05 | 41/48 (RKO, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.583×** | -4.7 | 1e-04 | 41/49 (KATO III, J82, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | **0.828×** | -4.5 | 5e-04 | 30/48 (C32, RPMI-7951, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.790×** | -4.0 | 0.004 | 35/47 (NCI-H2030, LoVo, …) | rises with dose | low cells (technical?); position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.794×** | -3.9 | 0.005 | 34/48 (KATO III, C-33 A, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.791×** | -3.8 | 0.006 | 31/49 (J82, SW 1088, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.791×** | -3.6 | 0.011 | 33/47 (AN3 CA, A-172, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.813×** | -3.5 | 0.019 | 27/48 (KATO III, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.750×** | -3.5 | 0.019 | 30/48 (RPMI-7951, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Allantoin (drug)]] 0.5 µM |  | **0.824×** | -3.2 | 0.039 | 25/48 (A549, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9403. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW48 (line)]] | wt | 433 | 7 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.06× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.03× (z +11.8) | [[Homoharringtonine (drug)]] 5 µM 0.562× (z -9.3) |
| [[SW480 (line)]] | alt | 232 | 7 (6 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.70× (z +17.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.65× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.618× (z -8.9) |
| [[A-172 (line)]] | wt | 517 | 4 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.19× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.65× (z +10.4) | [[Homoharringtonine (drug)]] 5 µM 0.596× (z -10.8) |
| [[A-427 (line)]] | wt | 231 | 4 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 5.22× (z +17.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -16.3) |
| [[HOP62 (line)]] | alt | 538 | 5 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.46× (z +14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.88× (z +10.8) | [[Homoharringtonine (drug)]] 5 µM 0.435× (z -13.9) |
| [[J82 (line)]] | alt | 676 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.55× (z +12.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.427× (z -16.9) |
| [[KATO III (line)]] | alt | 968 | 2 (2 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.26× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -22.7) |
| [[LOX-IMVI (line)]] | wt | 236 | 5 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.30× (z +15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.64× (z +14.9) | [[Homoharringtonine (drug)]] 5 µM 0.439× (z -12.6) |
| [[NCI-H2030 (line)]] | alt | 479 | 4 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.67× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.70× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -24.1) |
| [[PANC-1 (line)]] | alt | 385 | 5 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.24× (z +15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.58× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.514× (z -12.1) |
| [[HCT15 (line)]] | alt | 526 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.35× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -18.8) |
| [[Hs 766T (line)]] | wt | 330 | 4 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.63× (z +11.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.66× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.565× (z -10.0) |
| [[NCI-H2347 (line)]] | alt | 310 | 2 (1 ⚠) | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +15.6) | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -20.4) |
| [[Panc 03.27 (line)]] | alt | 292 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.32× (z +14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.11× (z +12.9) | — |
| [[RPMI-7951 (line)]] | alt | 630 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.25× (z +10.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -24.4) |
| [[SNU-423 (line)]] | alt | 282 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.41× (z +13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +11.5) | — |
| [[A498 (line)]] | wt | 436 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.09× (z +14.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.63× (z +9.2) | — |
| [[C-33 A (line)]] | alt | 291 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.52× (z +16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -14.7) |
| [[C32 (line)]] | wt | 569 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.88× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.523× (z -10.2) |
| [[CFPAC-1 (line)]] | alt | 609 | 3 (2 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.89× (z +11.3) | [[Homoharringtonine (drug)]] 5 µM 0.478× (z -12.7) |
| [[LS 180 (line)]] | wt | 490 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.76× (z +13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.608× (z -8.8) |
| [[MIA PaCa-2 (line)]] | alt | 331 | 3 (2 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.99× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.518× (z -9.6) |
| [[NCI-H1792 (line)]] | alt | 496 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.11× (z +13.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.86× (z +10.6) | — |
| [[NCI-H460 (line)]] | wt | 462 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.84× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -17.5) |
| [[SHP-77 (line)]] | alt | 316 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.47× (z +15.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -19.3) |
| [[A549 (line)]] | wt | 207 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.87× (z +14.9) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 472 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.65× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.519× (z -8.9) |
| [[AsPC-1 (line)]] | alt | 216 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.77× (z +17.0) | — |
| [[H4 (line)]] | wt | 668 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.20× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -26.7) |
| [[HepG2_C3A (line)]] | wt | 366 | 2 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +11.2) | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -15.7) |
| [[HS-578T (line)]] | alt | 448 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.63× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -14.7) |
| [[hTERT-HPNE (line)]] | wt | 539 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.72× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.584× (z -8.8) |
| [[LoVo (line)]] | wt | 558 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.77× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[RKO (line)]] | wt | 505 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.25× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -17.1) |
| [[SNU-1 (line)]] | wt | 331 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.94× (z +11.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -14.9) |
| [[SW 900 (line)]] | alt | 340 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.27× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -15.6) |
| [[CHP-212 (line)]] | wt | 320 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -12.2) |
| [[HEC-1-A (line)]] | alt | 378 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.37× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[HT-29 (line)]] | alt | 694 | 1 | 1 | [[Auranofin (drug)]] 5 µM 2.18× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -15.7) |
| [[NCI-H23 (line)]] | alt | 282 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.30× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -19.9) |
| [[SK-MEL-2 (line)]] | alt | 349 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.92× (z +13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[BT-474 (line)]] | alt | 297 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.61× (z +8.5) | — |
| [[NCI-H1573 (line)]] | alt | 455 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.543× (z -9.4) |
| [[NCI-H661 (line)]] | alt | 487 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.489× (z -8.5) |
| [[SW 1088 (line)]] | alt | 718 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -11.3) |
| [[SW1417 (line)]] | alt | 375 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.25× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[COLO 205 (line)]] | alt | 561 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 408 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 405 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 222 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9403), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDIA6]] | +0.93 | +0.91 / +0.94 | both halves | 7e-06 | same gene group; STRING 916 |
| [[DDOST]] | +0.83 | +0.83 / +0.82 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 678 |
| [[CANX]] | +0.78 | +0.74 / +0.79 | both halves | 7e-06 | pathway: Antigen Presentation: Folding, assembly and peptide loading of class I MHC; STRING 999 |
| [[PDIA4]] | +0.78 | +0.85 / +0.82 | both halves | 7e-06 | same gene group; STRING 784 |
| [[RPN2]] | +0.76 | +0.78 / +0.75 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 671 |
| [[MLEC]] | +0.76 | +0.81 / +0.75 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[HSP90B1]] | +0.75 | +0.81 / +0.81 | both halves | 7e-06 | STRING 985 |
| [[DNAJB11]] | +0.75 | +0.78 / +0.73 | both halves | 7e-06 | pathway: Dengue Virus Genome Translation and Replication; STRING 817 |
| [[RPN1]] | +0.74 | +0.81 / +0.69 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 521 |
| [[HYOU1]] | +0.74 | +0.71 / +0.78 | both halves | 7e-06 | pathway: Dengue Virus Genome Translation and Replication; STRING 877 |
| [[CALR]] | +0.73 | +0.83 / +0.76 | both halves | 7e-06 | pathway: Antigen Presentation: Folding, assembly and peptide loading of class I MHC; STRING 999 |
| [[TMED10]] | +0.72 | +0.73 / +0.70 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |

## Genes that move opposite

*21 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NSUN5]] | -0.62 | -0.51 / -0.66 | both halves | 1e-05 |  |
| [[SNHG11]] | -0.60 | -0.58 / -0.59 | both halves | 8e-06 |  |
| [[NT5C]] | -0.59 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[MRPL58]] | -0.59 | -0.56 / -0.64 | both halves | 1e-05 |  |
| [[PDRG1]] | -0.58 | -0.55 / -0.62 | both halves | 1e-05 |  |
| [[RNF166]] | -0.58 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[KRI1]] | -0.58 | -0.53 / -0.61 | both halves | 1e-05 |  |
| [[SURF2]] | -0.56 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[FBXL6]] | -0.56 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[TNIP2]] | -0.56 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[PPP1R35]] ⚠ | -0.55 | -0.52 / -0.49 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MRPL46]] | -0.55 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[ZNF480]] | -0.55 | -0.55 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTOR]] | B | MTOR activity raises PDIA3's level | compounds that target MTOR: 5 of 8 lower it (Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 3.9% of all compounds | 0.013 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[CKAP4]] | C | CKAP4 activity raises PDIA3's level | lines that do not express CKAP4 (4) vs lines expressing it (46) | 1.55× lower at baseline in the lines without CKAP4 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CAMKK1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.778). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-23.2, -21.9); signed map (-55.5, 6.6). **Vector** length 146, 58.4% of its response variance represented; |z| ≥ 3 in 1,291 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *UPR ER* (control, mean cos +0.69 to 11); *Cargo concentration in the ER* (reactome, mean cos +0.57 to 7); *Cotranslational targeting of proteins to the endoplasmic reticulum* (reactome, mean cos +0.54 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +12.5 | +10.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +9.2 | +7.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +8.0 | +3.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.9 | +6.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.9 | +6.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +0.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.1 | -0.7 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +3.1 | +0.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +0.2 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -11.5 | -7.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -8.9 | -3.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.9 | -8.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -7.6 | -5.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -7.4 | -16.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.9 | -3.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -4.3 | -3.5 |
|  | [[Rapamycin (drug)]] 5 µM |  | -4.1 | -4.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.0 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | protein disulfide isomerase family A member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q15.3 — chr15:43,746,394-43,773,279 (+) |
| Ensembl biotype | protein_coding |
| Also known as | P58, ERp61, ERp57, ERp60, GRP57, PI-PLC, HsT17083; previously GRP58 |
| Gene groups (HGNC) | Protein disulfide isomerases |
| Reactome | 12 pathways, smallest: Calnexin/calreticulin cycle; Antigen Presentation: Folding, assembly and peptide loading of class I MHC; N-glycan trimming in the ER and Calnexin/Calreticulin cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [P30101](https://www.uniprot.org/uniprotkb/P30101) (Protein disulfide-isomerase A3):

> Protein disulfide isomerase that catalyzes the formation, isomerization, and reduction or oxidation of disulfide bonds in client proteins and functions as a protein folding chaperone. Core component of the major histocompatibility complex class I (MHC I) peptide loading complex where it functions as an essential folding chaperone for TAPBP. Through TAPBP, assists the dynamic assembly of the MHC I complex with high affinity antigens in the endoplasmic reticulum. Therefore, plays a crucial role …

**Summary**, from NCBI Gene [2923](https://www.ncbi.nlm.nih.gov/gene/2923):

> This gene encodes a protein of the endoplasmic reticulum that interacts with lectin chaperones calreticulin and calnexin to modulate folding of newly synthesized glycoproteins. The protein was once thought to be a phospholipase; however, it has been demonstrated that the protein actually has protein disulfide isomerase activity. It is thought that complexes of lectins and this protein mediate protein folding by promoting formation of disulfide bonds in their glycoprotein substrates. This …

**Accessions** — [HGNC:4606](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4606) · Entrez [2923](https://www.ncbi.nlm.nih.gov/gene/2923) · UniProt [P30101](https://www.uniprot.org/uniprotkb/P30101) · Ensembl [ENSG00000167004](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167004)

## Data

Gene col 9403: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9403); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9403, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9403]; `tensor/DDL_lfc|DDL_z.npy` [9403]; `embed/gene_vectors.npy` [9403]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9403 or target_col == 9403). Every well: [[PDIA3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDIA3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
