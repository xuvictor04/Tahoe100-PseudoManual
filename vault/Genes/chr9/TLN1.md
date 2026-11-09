---
symbol: "TLN1"
type: "gene"
col: 5965
ensembl_id: "ENSG00000137076"
name: "talin 1"
location: "9p13.3"
module: 20
arm: "+"
pooled_cpm: 215.79
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 16
n_dd_up_clean: 3
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# TLN1

*talin 1* — 9p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.70× (z +14.2, q 3e-43, up in 44 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.641× (z -8.7, q 2e-15, down in 37 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.659× (z -8.2, q 9e-14, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AIDA]] (+0.64, fdr 2e-05), [[ARF1]] (+0.64, fdr 1e-05), [[SDF4]] (+0.61, fdr 7e-06); moves opposite to [[MAP2K7]] (-0.58, fdr 5e-05), [[LSM7]] (-0.57, fdr 2e-05), [[NDUFC2]] (-0.57, fdr 3e-05).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5965.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +14.2 | 3e-43 | 44/49 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.05×** | +13.6 | 1e-39 | 42/44 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.92×** | +12.8 | 2e-35 | 44/49 (A498, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.53×** | +7.8 | 1e-12 | 35/45 (SNU-423, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +4.8 | 2e-04 | 31/50 (MIA PaCa-2, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~2% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.25×** | +4.3 | 0.002 | 30/48 (MIA PaCa-2, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5965.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.641×** | -8.7 | 2e-15 | 37/48 (A549, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.659×** | -8.2 | 9e-14 | 43/48 (KATO III, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.716×** | -6.5 | 1e-08 | 40/48 (LoVo, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.716×** | -6.5 | 1e-08 | 33/48 (J82, A-427, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.716×** | -6.3 | 4e-08 | 38/47 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.726×** | -6.3 | 4e-08 | 37/48 (NCI-H23, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.737×** | -6.0 | 2e-07 | 35/48 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.740×** | -5.9 | 3e-07 | 28/48 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.759×** | -5.2 | 2e-05 | 29/48 (J82, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.794×** | -4.5 | 4e-04 | 28/48 (A-172, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.858× | -4.0 | 0.003 | 22/48 (J82, A-172, …) | two highest doses | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.813×** | -4.0 | 0.003 | 26/48 (J82, A498, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.751×** | -4.0 | 0.003 | 30/48 (H4, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.827×** | -3.7 | 0.009 | 23/48 (H4, HOP62, …) | rises with dose |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.830×** | -3.6 | 0.011 | 24/48 (SW 1088, Panc 03.27, …) | inconsistent across doses |  |
| [[Bergenin (drug)]] 0.5 µM |  | 0.843× | -3.3 | 0.030 | 18/48 (Hs 766T, NCI-H1792, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.893× | -2.9 | 0.090 | 13/48 (SW 900, CHP-212, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5965. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 294 | 2 (2 ⚠) | 8 (3 ⚠) | [[Dinaciclib (drug)]] 5 µM 1.93× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -19.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.360× (z -15.0) |
| [[J82 (line)]] | alt | 433 | 2 (2 ⚠) | 6 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.12× (z +10.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -26.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.327× (z -15.7) |
| [[NCI-H23 (line)]] | alt | 478 | 1 | 7 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.57× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.543× (z -13.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.490× (z -10.9) |
| [[A-427 (line)]] | wt | 142 | 2 (2 ⚠) | 5 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.48× (z +12.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.370× (z -13.6) |
| [[HOP62 (line)]] | alt | 295 | 2 (2 ⚠) | 5 (3 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.28× (z +9.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.442× (z -13.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.418× (z -10.2) |
| [[LoVo (line)]] | wt | 134 | 5 (4 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +17.8) | [[Panobinostat (drug)]] 5 µM 0.540× (z -9.1) |
| [[A498 (line)]] | wt | 437 | 3 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.53× (z +15.7) ⚠ toxic; transcription drop | [[Penfluridol (drug)]] 5 µM 0.544× (z -10.0) |
| [[C32 (line)]] | wt | 126 | 3 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.36× (z +9.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.76× (z +8.6) | [[Harringtonine (drug)]] 5 µM 0.371× (z -10.6) |
| [[HS-578T (line)]] | alt | 329 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.20× (z +11.6) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.473× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.513× (z -10.3) |
| [[hTERT-HPNE (line)]] | wt | 368 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.345× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.407× (z -9.9) |
| [[KATO III (line)]] | alt | 165 | 3 (2 ⚠) | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +15.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.392× (z -13.3) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.512× (z -9.9) |
| [[MIA PaCa-2 (line)]] | alt | 162 | 5 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.47× (z +23.3) | — |
| [[PANC-1 (line)]] | alt | 274 | 3 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.84× (z +15.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.85× (z +13.1) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.544× (z -9.6) |
| [[SNU-423 (line)]] | alt | 278 | 3 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.00× (z +14.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.482× (z -13.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.514× (z -8.5) |
| [[A549 (line)]] | wt | 215 | 2 (1 ⚠) | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.85× (z +12.8) | [[Digitoxin (drug)]] 5 µM 0.417× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.535× (z -9.5) |
| [[Hs 766T (line)]] | wt | 244 | 2 (1 ⚠) | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +14.2) | [[Digitoxin (drug)]] 5 µM 0.462× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.539× (z -8.7) |
| [[HT-29 (line)]] | alt | 120 | 3 (2 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +14.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.479× (z -9.5) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 318 | 3 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.99× (z +10.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.65× (z +10.4) | [[Digitoxin (drug)]] 5 µM 0.436× (z -12.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 182 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.73× (z +10.0) | [[Harringtonine (drug)]] 5 µM 0.451× (z -10.2) |
| [[NCI-H1792 (line)]] | alt | 157 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.29× (z +10.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.64× (z +8.9) | — |
| [[NCI-H460 (line)]] | wt | 126 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.11× (z +14.6) | — |
| [[SW480 (line)]] | alt | 161 | 3 (2 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.40× (z +19.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.460× (z -12.3) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 152 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.68× (z +13.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.68× (z +10.1) | — |
| [[Panc 03.27 (line)]] | alt | 133 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +15.1) | — |
| [[RPMI-7951 (line)]] | alt | 268 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.37× (z +11.0) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.502× (z -8.7) |
| [[SNU-1 (line)]] | wt | 186 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.53× (z +9.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.83× (z +8.8) | — |
| [[SW 900 (line)]] | alt | 239 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.63× (z +8.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.453× (z -10.0) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.499× (z -9.1) |
| [[AsPC-1 (line)]] | alt | 312 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.72× (z +10.1) | — |
| [[H4 (line)]] | wt | 346 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.419× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.466× (z -9.0) |
| [[NCI-H2347 (line)]] | alt | 134 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.75× (z +12.2) | — |
| [[RKO (line)]] | wt | 205 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.74× (z +18.3) | [[Homoharringtonine (drug)]] 0.5 µM 0.522× (z -8.6) |
| [[SK-MEL-2 (line)]] | alt | 221 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.30× (z +10.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.68× (z +9.4) | — |
| [[SW48 (line)]] | wt | 145 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +12.4) | — |
| [[AN3 CA (line)]] | alt | 216 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.323× (z -9.7) |
| [[C-33 A (line)]] | alt | 114 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.79× (z +10.0) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 113 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.60× (z +8.5) | — |
| [[CHP-212 (line)]] | wt | 174 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.01× (z +8.9) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 285 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.84× (z +9.0) | — |
| [[NCI-H1573 (line)]] | alt | 124 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.452× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 212 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.11× (z +8.6) ⚠ toxic; transcription drop | — |
| [[SW 1088 (line)]] | alt | 433 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.136× (z -13.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 146 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.82× (z +12.5) | — |
| [[BT-474 (line)]] | alt | 75.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 170 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 180 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 169 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 90.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 170 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5965), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AIDA]] | +0.64 | +0.47 / +0.72 | both halves | 2e-05 |  |
| [[ARF1]] | +0.64 | +0.56 / +0.68 | both halves | 1e-05 | same gene group |
| [[SDF4]] | +0.61 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[STYX]] | +0.61 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[AP2M1]] | +0.59 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[SLC30A9]] | +0.59 | +0.34 / +0.63 | both halves | 1e-04 |  |
| [[RECQL]] | +0.58 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[CANX]] | +0.58 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[TPM3]] | +0.57 | +0.57 / +0.61 | both halves | 1e-05 | pathway: Muscle contraction; STRING 626 |
| [[FLNA]] | +0.57 | +0.49 / +0.61 | both halves | 1e-05 | pathway: Platelet activation, signaling and aggregation; STRING 998 |
| [[KIAA1191]] | +0.57 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[IQGAP1]] | +0.57 | +0.47 / +0.73 | both halves | 2e-05 | pathway: MAP2K and MAPK activation; STRING 893 |

## Genes that move opposite

*40 of its nearest partners move opposite, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAP2K7]] | -0.58 | -0.40 / -0.54 | both halves | 5e-05 |  |
| [[LSM7]] | -0.57 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[NDUFC2]] | -0.57 | -0.43 / -0.60 | both halves | 3e-05 |  |
| [[ZNF790-AS1]] | -0.56 | -0.41 / -0.58 | both halves | 4e-05 |  |
| [[HEXD]] | -0.56 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[TIMM13]] | -0.56 | -0.38 / -0.55 | both halves | 7e-05 |  |
| [[LAMTOR4]] | -0.55 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[SNRPF]] | -0.54 | -0.38 / -0.59 | both halves | 7e-05 |  |
| [[CELF1]] | -0.53 | -0.43 / -0.45 | both halves | 4e-05 |  |
| [[C15orf61]] ⚠ | -0.53 | -0.30 / -0.61 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[YBEY]] | -0.53 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[MRPL14]] | -0.52 | -0.25 / -0.62 | both halves | 4e-04 |  |
| [[SETDB1]] | -0.52 | -0.44 / -0.53 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TLN1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.1% of all compounds | 0.017 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.380). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-23.1, -19.3); signed map (-18.8, -34.0). **Vector** length 140, 47.2% of its response variance represented; |z| ≥ 3 in 1,207 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +13.0 | +14.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +9.1 | +4.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +8.4 | +4.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.9 | +13.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.7 | +12.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | -0.6 |
|  | [[Decitabine (drug)]] 5 µM |  | +2.8 | +1.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | +2.6 | +1.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | +0.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.5 | +2.6 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -8.4 | -8.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.8 | -6.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -6.7 | -6.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -5.9 | -4.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.6 | -3.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.3 | -2.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -4.0 | -2.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -3.6 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | talin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p13.3 — chr9:35,696,948-35,732,195 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ILWEQ; previously TLN |
| Gene groups (HGNC) | FERM domain containing; MicroRNA protein coding host genes |
| Reactome | 35 pathways, smallest: GRB2:SOS provides linkage to MAPK signaling for Integrins; SEMA3A-Plexin repulsion signaling by inhibiting Integrin adhesion; p130Cas linkage to MAPK signaling for integrins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y490](https://www.uniprot.org/uniprotkb/Q9Y490) (Talin-1):

> High molecular weight cytoskeletal protein concentrated at regions of cell-matrix and cell-cell contacts. Involved in connections of major cytoskeletal structures to the plasma membrane. With KANK1 co-organize the assembly of cortical microtubule stabilizing complexes (CMSCs) positioned to control microtubule-actin crosstalk at focal adhesions (FAs) rims.

**Summary**, from NCBI Gene [7094](https://www.ncbi.nlm.nih.gov/gene/7094):

> This gene encodes a cytoskeletal protein that is concentrated in areas of cell-substratum and cell-cell contacts. The encoded protein plays a significant role in the assembly of actin filaments and in spreading and migration of various cell types, including fibroblasts and osteoclasts. It codistributes with integrins in the cell surface membrane in order to assist in the attachment of adherent cells to extracellular matrices and of lymphocytes to other cells. The N-terminus of this protein …

**Accessions** — [HGNC:11845](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11845) · Entrez [7094](https://www.ncbi.nlm.nih.gov/gene/7094) · UniProt [Q9Y490](https://www.uniprot.org/uniprotkb/Q9Y490) · Ensembl [ENSG00000137076](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137076)

## Data

Gene col 5965: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5965); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5965, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5965]; `tensor/DDL_lfc|DDL_z.npy` [5965]; `embed/gene_vectors.npy` [5965]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5965 or target_col == 5965). Every well: [[TLN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TLN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
