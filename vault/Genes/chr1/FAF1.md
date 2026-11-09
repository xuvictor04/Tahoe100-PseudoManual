---
symbol: "FAF1"
type: "gene"
col: 11626
ensembl_id: "ENSG00000185104"
name: "Fas associated factor 1"
location: "1p32.3"
module: 4
arm: "+"
pooled_cpm: 334.75
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 9
n_dd_up_clean: 9
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# FAF1

*Fas associated factor 1* — 1p32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.53× (z +13.7, q 6e-40, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.557× (z -13.5, q 8e-39, down in 43 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.691× (z -8.5, q 2e-15, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DDX10]] (+0.70, fdr 7e-06), [[SPATA5]] (+0.67, fdr 7e-06), [[SNRPD1]] (+0.65, fdr 7e-06); moves opposite to [[FAM117A]] (-0.58, fdr 4e-05), [[MTMR11]] (-0.58, fdr 1e-05), [[FAM177B]] (-0.54, fdr 7e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[WWOX]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11626.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.53×** | +13.7 | 6e-40 | 42/48 (COLO 205, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.59×** | +11.4 | 1e-27 | 45/49 (COLO 205, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.61×** | +10.8 | 4e-25 | 43/48 (HS-578T, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.55×** | +10.1 | 1e-21 | 43/48 (COLO 205, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.48×** | +8.9 | 7e-17 | 41/48 (AsPC-1, NCI-H460, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.47×** | +8.8 | 2e-16 | 41/48 (COLO 205, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.96×** | +8.1 | 6e-14 | 38/48 (SW480, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.41×** | +7.9 | 3e-13 | 37/48 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.40×** | +7.7 | 6e-13 | 42/48 (SW480, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.35×** | +6.9 | 3e-10 | 37/48 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.34×** | +6.6 | 2e-09 | 33/48 (H4, HS-578T, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.31×** | +6.2 | 3e-08 | 30/48 (COLO 205, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.26×** | +5.2 | 8e-06 | 30/48 (SNU-423, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.26×** | +4.9 | 4e-05 | 31/48 (COLO 205, NCI-H1792, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.24×** | +4.8 | 5e-05 | 27/48 (COLO 205, SW480, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.40×** | +4.0 | 0.002 | 30/49 (NCI-H460, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 1.15× | +3.0 | 0.068 | 15/48 (NCI-H1573, NCI-H2347, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11626.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.557×** | -13.5 | 8e-39 | 43/49 (HEC-1-A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.570×** | -12.4 | 4e-33 | 41/44 (NCI-H23, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.691×** | -8.5 | 2e-15 | 37/48 (RKO, MIA PaCa-2, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.689×** | -8.3 | 2e-14 | 43/47 (MIA PaCa-2, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.731×** | -7.3 | 5e-11 | 40/48 (J82, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.818×** | -6.6 | 4e-09 | 26/49 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.739×** | -6.5 | 8e-09 | 29/45 (KATO III, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.818×** | -4.7 | 2e-04 | 25/48 (MIA PaCa-2, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.862× | -3.5 | 0.035 | 12/47 (LS 180, COLO 205, …) | two highest doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.820×** | -3.3 | 0.057 | 28/47 (C32, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Vilanterol (drug)]] 5 µM |  | 0.909× | -3.1 | 0.084 | 4/49 (RPMI-7951, Panc 03.27, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11626. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 336 | 4 (1 ⚠) | 7 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.57× (z +11.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.595× (z -12.9) |
| [[SW480 (line)]] | alt | 409 | 6 (1 ⚠) | 5 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.27× (z +15.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.574× (z -14.5) |
| [[COLO 205 (line)]] | alt | 309 | 9 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 14.0× (z +46.8) | — |
| [[HT-29 (line)]] | alt | 308 | 7 (3 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +20.8) | [[Auranofin (drug)]] 5 µM 0.578× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 513 | 4 (1 ⚠) | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.05× (z +11.8) | [[Auranofin (drug)]] 5 µM 0.433× (z -13.8) |
| [[NCI-H460 (line)]] | wt | 250 | 9 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +19.8) | — |
| [[HepG2_C3A (line)]] | wt | 228 | 5 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.63× (z +13.0) | [[Dinaciclib (drug)]] 5 µM 0.385× (z -12.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 293 | 7 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +15.0) | [[Dinaciclib (drug)]] 5 µM 0.424× (z -11.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 224 | 5 (3 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.95× (z +37.7) | [[Dinaciclib (drug)]] 5 µM 0.298× (z -19.4) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 161 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +13.0) | — |
| [[C32 (line)]] | wt | 387 | 3 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.99× (z +13.9) | [[Dinaciclib (drug)]] 0.5 µM 0.379× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.541× (z -10.1) |
| [[H4 (line)]] | wt | 351 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +11.8) | — |
| [[J82 (line)]] | alt | 427 | 2 (1 ⚠) | 5 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.63× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.380× (z -17.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.595× (z -13.4) |
| [[PANC-1 (line)]] | alt | 452 | 3 | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.63× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.428× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.661× (z -10.9) |
| [[SHP-77 (line)]] | alt | 523 | 5 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.79× (z +11.3) | [[Dinaciclib (drug)]] 0.5 µM 0.453× (z -15.5) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 258 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +13.3) | — |
| [[CFPAC-1 (line)]] | alt | 290 | 5 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +12.7) | [[Dinaciclib (drug)]] 0.5 µM 0.577× (z -8.8) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 417 | 1 | 5 (4 ⚠) | [[PH-797804 (drug)]] 5 µM 3.37× (z +12.2) | [[Dinaciclib (drug)]] 0.5 µM 0.352× (z -20.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.589× (z -14.5) |
| [[LOX-IMVI (line)]] | wt | 394 | 4 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 4.46× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.527× (z -9.9) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 407 | 3 | 3 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.20× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.354× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.625× (z -8.5) |
| [[NCI-H2030 (line)]] | alt | 357 | 1 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.56× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.476× (z -11.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 503 | 1 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +14.6) | [[Dinaciclib (drug)]] 5 µM 0.197× (z -26.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.507× (z -11.3) |
| [[Panc 03.27 (line)]] | alt | 300 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +12.0) | [[Dinaciclib (drug)]] 0.5 µM 0.478× (z -11.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 384 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.501× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.651× (z -11.0) |
| [[A549 (line)]] | wt | 213 | 3 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.52× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.604× (z -12.4) |
| [[BT-474 (line)]] | alt | 310 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.19× (z +12.8) | — |
| [[Hs 766T (line)]] | wt | 286 | 3 (2 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.05× (z +10.7) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.55× (z +9.2) | [[Dinaciclib (drug)]] 0.05 µM 0.527× (z -8.9) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 184 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.71× (z +12.4) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.81× (z +10.4) | — |
| [[KATO III (line)]] | alt | 267 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +10.7) | [[Dinaciclib (drug)]] 0.05 µM 0.297× (z -14.7) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 335 | 2 (2 ⚠) | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 1.93× (z +10.3) ⚠ cell-cycle shift, explains ~35% of this change | [[Auranofin (drug)]] 5 µM 0.435× (z -13.1) |
| [[LS 180 (line)]] | wt | 322 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +14.1) | [[Dinaciclib (drug)]] 5 µM 0.241× (z -18.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 252 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.13× (z +9.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.533× (z -10.1) ⚠ toxic |
| [[A-427 (line)]] | wt | 374 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.406× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.581× (z -9.3) |
| [[AN3 CA (line)]] | alt | 548 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.333× (z -12.4) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 524 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.317× (z -14.1) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 324 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.21× (z +12.7) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H1792 (line)]] | alt | 233 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +14.0) | — |
| [[NCI-H2347 (line)]] | alt | 193 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +20.6) | — |
| [[SK-MEL-2 (line)]] | alt | 326 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +11.4) | [[Auranofin (drug)]] 5 µM 0.450× (z -11.4) |
| [[SNU-423 (line)]] | alt | 221 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.11× (z +12.1) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.66× (z +11.7) | — |
| [[RKO (line)]] | wt | 445 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.367× (z -15.2) |
| [[SNU-1 (line)]] | wt | 391 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.356× (z -15.1) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 296 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 1.79× (z +9.3) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[C-33 A (line)]] | alt | 284 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 130 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 275 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 322 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 421 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 302 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 271 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11626), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX10]] | +0.70 | +0.72 / +0.70 | both halves | 7e-06 |  |
| [[SPATA5]] | +0.67 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[SNRPD1]] | +0.65 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[DIS3L2]] | +0.65 | +0.59 / +0.70 | both halves | 7e-06 |  |
| [[SPIDR]] | +0.65 | +0.48 / +0.71 | both halves | 2e-05 |  |
| [[CMSS1]] | +0.65 | +0.54 / +0.69 | both halves | 1e-05 |  |
| [[TASP1]] | +0.64 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[COA1]] | +0.63 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[COMMD10]] | +0.62 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[NUBPL]] | +0.60 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[NAA15]] | +0.60 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[DPH6]] | +0.60 | +0.62 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM117A]] | -0.58 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[MTMR11]] | -0.58 | -0.63 / -0.53 | both halves | 1e-05 |  |
| [[FAM177B]] | -0.54 | -0.38 / -0.51 | both halves | 7e-05 |  |
| [[MXD1]] | -0.54 | -0.64 / -0.57 | both halves | 9e-06 |  |
| [[ADCY10]] | -0.53 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[RNF11]] | -0.52 | -0.48 / -0.46 | both halves | 2e-05 |  |
| [[C14orf28]] | -0.52 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[SH3BGR]] | -0.52 | -0.37 / -0.36 | both halves | 9e-05 |  |
| [[B4GALT4]] | -0.50 | -0.49 / -0.37 | both halves | 8e-05 |  |
| [[CLK1]] | -0.50 | -0.51 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WWOX]] | B | WWOX activity raises FAF1's level | lines that do not express WWOX (5) vs lines expressing it (45) | 1.61× lower at baseline in the lines without WWOX | 0.048 | ⚠ within organs, on part of the lines; also absent: ZFHX2, WARS2-AS1, TMCC1-DT; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.552). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-10.9, -35.2); signed map (-10.0, -49.1). **Vector** length 127, 48.9% of its response variance represented; |z| ≥ 3 in 1,469 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belumosudil (drug)]] 5 µM |  | +5.8 | +3.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +5.3 | +7.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +4.7 | +6.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.6 | +8.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +4.5 | +10.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.5 | +2.5 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +3.6 | +2.3 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +3.5 | +1.2 |
|  | [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | +3.4 | +2.7 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -10.9 | -8.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -9.3 | -8.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.5 | -6.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | -6.3 | -7.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.9 | -1.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.9 | -2.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -3.7 | -2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.5 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | Fas associated factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p32.3 — chr1:50,437,028-50,960,267 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-03, hFAF1, HFAF1s, UBXD12, UBXN3A |
| Gene groups (HGNC) | UBX domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UNN5](https://www.uniprot.org/uniprotkb/Q9UNN5) (FAS-associated factor 1):

> Ubiquitin-binding protein. Required for the progression of DNA replication forks by targeting DNA replication licensing factor CDT1 for degradation. Potentiates but cannot initiate FAS-induced apoptosis (By similarity).

**Summary**, from NCBI Gene [11124](https://www.ncbi.nlm.nih.gov/gene/11124):

> Interaction of Fas ligand (TNFSF6) with the FAS antigen (TNFRSF6) mediates programmed cell death, also called apoptosis, in a number of organ systems. The protein encoded by this gene binds to FAS antigen and can initiate apoptosis or enhance apoptosis initiated through FAS antigen. Initiation of apoptosis by the protein encoded by this gene requires a ubiquitin-like domain but not the FAS-binding domain. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:3578](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3578) · Entrez [11124](https://www.ncbi.nlm.nih.gov/gene/11124) · UniProt [Q9UNN5](https://www.uniprot.org/uniprotkb/Q9UNN5) · Ensembl [ENSG00000185104](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185104)

## Data

Gene col 11626: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11626); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11626, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11626]; `tensor/DDL_lfc|DDL_z.npy` [11626]; `embed/gene_vectors.npy` [11626]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11626 or target_col == 11626). Every well: [[FAF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
