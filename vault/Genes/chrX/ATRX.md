---
symbol: "ATRX"
type: "gene"
col: 1418
ensembl_id: "ENSG00000085224"
name: "ATRX chromatin remodeler"
location: "Xq21.1"
module: 51
arm: "+"
pooled_cpm: 376.94
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 11
n_dd_up_clean: 2
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# ATRX

*ATRX chromatin remodeler* — Xq21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.56× (z +12.7, q 5e-34, up in 42 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.05 µM: 1.25× (z +6.4, q 3e-08, up in 31 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (A-172 2.01×, A498 2.13×, HS-578T 2.38×, HT-29 1.85×, …; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H2347 1.98×, A498 1.81×, J82 1.49×; ⚠ cell-cycle shift, explains ~99% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (A-172 2.19×, A498 2.02×, HS-578T 2.23×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.05 µM in 3 lines (NCI-H2347 1.66×, A498 1.81×, A-427 1.53×).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.455× (z -22.6, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C11orf58]] (+0.75, fdr 7e-06), [[ACIN1]] (+0.72, fdr 7e-06), [[ZMYM4]] (+0.71, fdr 7e-06); moves opposite to [[MPG]] (-0.68, fdr 1e-05), [[UBTD1]] (-0.65, fdr 1e-05), [[EEF1AKMT4]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LINC01505]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 9 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1418.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (A-172 2.01×, A498 2.13×, HS-578T 2.38×, HT-29 1.85×, …; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H2347 1.98×, A498 1.81×, J82 1.49×; ⚠ cell-cycle shift, explains ~99% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (A-172 2.19×, A498 2.02×, HS-578T 2.23×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.05 µM in 3 lines (NCI-H2347 1.66×, A498 1.81×, A-427 1.53×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.56×** | +12.7 | 5e-34 | 42/49 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.48×** | +10.7 | 2e-24 | 37/44 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.53×** | +6.4 | 3e-08 | 42/47 (KATO III, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.25×** | +6.4 | 3e-08 | 31/48 (NCI-H2347, A498, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.24×** | +5.7 | 2e-06 | 25/45 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | 1.19× | +4.7 | 2e-04 | 19/47 (SW480, HOP62, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.19× | +4.5 | 5e-04 | 21/47 (LoVo, A498, …) | all doses, flat | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 1.17× | +4.5 | 5e-04 | 19/48 (A-172, A498, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | 1.16× | +4.2 | 0.002 | 17/48 (NCI-H2347, A498, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 1.14× | +3.7 | 0.014 | 17/48 (NCI-H2347, A498, …) | all doses, flat | composition shift |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.09× | +3.5 | 0.027 | 1/49 (SW48) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~99% of this change | 1.09× | +3.4 | 0.027 | 14/48 (NCI-H2347, A498, …) | all doses, flat | composition shift |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.12× | +3.2 | 0.052 | 6/47 (AsPC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 1.12× | +3.2 | 0.056 | 3/49 (SW1417, HS-578T, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.12× | +3.1 | 0.067 | 10/49 (NCI-H23, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Thymol (drug)]] 5 µM |  | 1.08× | +3.1 | 0.067 | 1/48 (SW 1271) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.09× | +3.1 | 0.067 | 3/48 (SK-MEL-2, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.11× | +3.1 | 0.067 | 4/48 (KATO III, RPMI-7951, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.11× | +3.0 | 0.074 | 5/48 (SK-MEL-2, AsPC-1, …) | two highest doses | noisy plate (z scaled) |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | 1.08× | +3.0 | 0.074 | 0/48 | top dose only | position effect removed |
| [[Ixazomib (drug)]] 5 µM |  | **1.22×** | +3.0 | 0.074 | 19/48 (KATO III, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | 1.11× | +2.9 | 0.086 | 4/48 (NCI-H1792, A549, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | 1.11× | +2.9 | 0.099 | 3/48 (KATO III, NCI-H1792, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1418.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.455×** | -22.6 | 0e+00 | 48/48 (SW480, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.458×** | -22.4 | 0e+00 | 48/48 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.482×** | -20.9 | 0e+00 | 48/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.647×** | -12.5 | 1e-33 | 46/48 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.737×** | -12.0 | 3e-31 | 37/49 (A549, SW480, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.648×** | -12.0 | 5e-31 | 44/47 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.687×** | -10.6 | 1e-24 | 45/48 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.691×** | -10.6 | 2e-24 | 46/48 (MIA PaCa-2, KATO III, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change | **0.791×** | -6.7 | 1e-09 | 28/48 (PANC-1, A-427, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 0.835× | -5.2 | 1e-05 | 24/48 (A549, AN3 CA, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | 0.843× | -4.9 | 5e-05 | 22/48 (NCI-H23, HCT15, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.727×** | -4.8 | 9e-05 | 38/49 (SW480, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.877× | -3.8 | 0.007 | 15/48 (SNU-1, PANC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 0.890× | -3.3 | 0.034 | 14/48 (PANC-1, A-427, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.803×** | -3.3 | 0.038 | 23/48 (Hs 766T, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | 0.889× | -3.3 | 0.040 | 7/48 (NCI-H2030, MIA PaCa-2, …) | top dose only |  |
| [[Lopinavir (drug)]] 5 µM |  | 0.896× | -3.2 | 0.052 | 2/47 (HCT15, SW 900) | top dose only |  |
| [[Belinostat (drug)]] 0.05 µM |  | 0.896× | -3.1 | 0.059 | 4/48 (RKO, C32, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1418. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 467 | 0 | 11 (8 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.452× (z -17.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.511× (z -14.9) |
| [[HEC-1-A (line)]] | alt | 414 | 2 (2 ⚠) | 7 (4 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.66× (z +10.4) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.421× (z -17.8) |
| [[NCI-H23 (line)]] | alt | 531 | 0 | 9 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.416× (z -16.0) |
| [[SW480 (line)]] | alt | 587 | 0 | 9 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.331× (z -25.3) |
| [[A-427 (line)]] | wt | 353 | 1 | 7 (2 ⚠) | [[Homoharringtonine (drug)]] 0.05 µM 1.53× (z +8.7) | [[Panobinostat (drug)]] 5 µM 0.427× (z -17.3) |
| [[NCI-H2347 (line)]] | alt | 216 | 4 (3 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +18.9) ⚠ cell-cycle shift, explains ~99% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 1.66× (z +10.1) | [[Panobinostat (drug)]] 0.5 µM 0.508× (z -13.4) |
| [[RKO (line)]] | wt | 273 | 3 (3 ⚠) | 5 | [[Homoharringtonine (drug)]] 0.5 µM 1.87× (z +10.4) ⚠ cell-cycle shift, explains ~48% of this change | [[Belinostat (drug)]] 5 µM 0.385× (z -15.8) |
| [[A-172 (line)]] | wt | 365 | 4 (4 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.19× (z +14.8) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.526× (z -12.6) |
| [[A549 (line)]] | wt | 518 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.346× (z -24.9) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.377× (z -16.6) |
| [[HOP62 (line)]] | alt | 372 | 3 (3 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 1.91× (z +11.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.410× (z -16.2) |
| [[HT-29 (line)]] | alt | 356 | 1 (1 ⚠) | 6 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.85× (z +11.9) ⚠ toxic; transcription drop | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.499× (z -12.9) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.518× (z -12.7) |
| [[SW1417 (line)]] | alt | 387 | 1 (1 ⚠) | 6 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.61× (z +9.4) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.454× (z -15.6) |
| [[A498 (line)]] | wt | 275 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +13.4) ⚠ cell-cycle shift, explains ~99% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 1.81× (z +9.8) | — |
| [[HS-578T (line)]] | alt | 201 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.38× (z +12.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.476× (z -10.3) |
| [[LoVo (line)]] | wt | 269 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 1.77× (z +11.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.465× (z -15.3) |
| [[LOX-IMVI (line)]] | wt | 385 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.381× (z -18.1) |
| [[LS 180 (line)]] | wt | 389 | 1 (1 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.68× (z +9.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.378× (z -18.1) |
| [[MIA PaCa-2 (line)]] | alt | 501 | 1 (1 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.71× (z +10.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.402× (z -17.1) |
| [[NCI-H1573 (line)]] | alt | 342 | 1 (1 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.54× (z +8.8) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.511× (z -13.7) |
| [[NCI-H1792 (line)]] | alt | 230 | 1 (1 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.80× (z +8.6) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.395× (z -13.8) |
| [[RPMI-7951 (line)]] | alt | 477 | 2 (2 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 1.80× (z +10.4) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.531× (z -11.6) |
| [[SHP-77 (line)]] | alt | 282 | 1 (1 ⚠) | 5 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 1.84× (z +9.9) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.512× (z -11.4) |
| [[AN3 CA (line)]] | alt | 435 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.441× (z -13.3) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.351× (z -12.3) |
| [[AsPC-1 (line)]] | alt | 265 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 1.78× (z +8.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.387× (z -14.2) |
| [[C-33 A (line)]] | alt | 450 | 1 (1 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.70× (z +8.5) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.503× (z -11.1) |
| [[CFPAC-1 (line)]] | alt | 319 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.445× (z -14.4) |
| [[HCT15 (line)]] | alt | 411 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.308× (z -18.2) |
| [[Hs 766T (line)]] | wt | 379 | 1 (1 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 1.65× (z +8.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.474× (z -13.6) |
| [[J82 (line)]] | alt | 408 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 1.52× (z +9.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.588× (z -11.8) |
| [[KATO III (line)]] | alt | 476 | 0 | 5 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.435× (z -17.9) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.457× (z -17.5) |
| [[SK-MEL-2 (line)]] | alt | 418 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.370× (z -18.6) |
| [[C32 (line)]] | wt | 254 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 1.80× (z +9.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.421× (z -13.9) |
| [[COLO 205 (line)]] | alt | 315 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.412× (z -15.8) |
| [[NCI-H2030 (line)]] | alt | 173 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.473× (z -11.1) |
| [[NCI-H460 (line)]] | wt | 443 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.426× (z -15.2) |
| [[Panc 03.27 (line)]] | alt | 418 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.441× (z -15.3) |
| [[SNU-423 (line)]] | alt | 718 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 1.70× (z +10.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.439× (z -16.2) |
| [[SW 900 (line)]] | alt | 243 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.380× (z -15.1) |
| [[SW48 (line)]] | wt | 278 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.11× (z +8.8) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.378× (z -12.0) |
| [[CHP-212 (line)]] | wt | 425 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.412× (z -14.3) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.451× (z -9.2) |
| [[H4 (line)]] | wt | 397 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.454× (z -11.5) |
| [[HepG2_C3A (line)]] | wt | 234 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.424× (z -11.9) |
| [[hTERT-HPNE (line)]] | wt | 327 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.432× (z -13.6) |
| [[SNU-1 (line)]] | wt | 385 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.410× (z -14.0) |
| [[BT-474 (line)]] | alt | 276 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.426× (z -13.7) |
| [[SW 1088 (line)]] | alt | 338 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.290× (z -8.5) |
| [[SW 1271 (line)]] | alt | 310 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.300× (z -9.4) |
| [[NCI-H2122 (line)]] | alt | 294 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 370 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 465 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1418), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C11orf58]] | +0.75 | +0.76 / +0.68 | both halves | 7e-06 |  |
| [[ACIN1]] | +0.72 | +0.73 / +0.59 | both halves | 7e-06 |  |
| [[ZMYM4]] | +0.71 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[LARP7]] | +0.70 | +0.73 / +0.55 | both halves | 1e-05 |  |
| [[BPTF]] | +0.69 | +0.74 / +0.59 | both halves | 7e-06 | STRING 709 |
| [[BAZ2B]] | +0.69 | +0.72 / +0.59 | both halves | 7e-06 | STRING 629 |
| [[TIAM2]] | +0.67 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[NIPBL]] | +0.67 | +0.63 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_UV_RESPONSE_DN; STRING 674 |
| [[BCLAF1]] | +0.67 | +0.63 / +0.54 | both halves | 1e-05 | STRING 769 |
| [[THOC7]] | +0.66 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[USP16]] | +0.66 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[RIPK2-DT]] | +0.66 | +0.65 / +0.58 | both halves | 8e-06 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPG]] | -0.68 | -0.67 / -0.56 | both halves | 1e-05 |  |
| [[UBTD1]] | -0.65 | -0.63 / -0.54 | both halves | 1e-05 |  |
| [[EEF1AKMT4]] | -0.64 | -0.56 / -0.61 | both halves | 1e-05 |  |
| [[TMEM120B]] | -0.64 | -0.66 / -0.52 | both halves | 1e-05 |  |
| [[SDHAP1]] | -0.62 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[DNAJC5]] | -0.62 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[TOR1B]] | -0.61 | -0.42 / -0.62 | both halves | 4e-05 |  |
| [[MGAT1]] | -0.61 | -0.52 / -0.62 | both halves | 1e-05 |  |
| [[IMPDH1]] | -0.61 | -0.68 / -0.48 | both halves | 2e-05 |  |
| [[PIGF]] | -0.60 | -0.54 / -0.46 | both halves | 2e-05 |  |
| [[GFOD2]] | -0.60 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[TAF5L]] | -0.60 | -0.54 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01505]] | B | LINC01505 activity raises ATRX's level | lines that do not express LINC01505 (5) vs lines expressing it (45) | 1.43× lower at baseline in the lines without LINC01505 | 0.061 | ⚠ within organs, on part of the lines; also absent: EID2, CENPP, ENSG00000223727; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises ATRX's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.706). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-23.1, 9.4); signed map (11.8, -27.7). **Vector** length 144, 53.0% of its response variance represented; |z| ≥ 3 in 1,315 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~99% of this change | +9.8 | +3.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +9.4 | +4.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +8.7 | +3.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.7 | +12.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.6 | +6.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +6.2 | +4.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.5 | +3.0 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +4.2 | +3.2 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +4.1 | +3.5 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -12.0 | -12.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -8.2 | -12.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -6.5 | -20.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -6.5 | -10.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -4.8 | -12.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -4.4 | -2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.1 | -2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.6 | -4.9 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -2.9 | -2.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.8 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | ATRX chromatin remodeler |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq21.1 — chrX:77,504,880-77,786,233 (-) |
| Ensembl biotype | protein_coding |
| Also known as | XH2, XNP; previously RAD54, JMS, MRX52 |
| Gene groups (HGNC) | SNF2 related family |
| Hallmark sets | UV_RESPONSE_DN, G2M_CHECKPOINT |
| Reactome | 5 pathways, smallest: Inhibition of DNA recombination at telomere; Diseases of mitotic cell cycle; Telomere Maintenance |
| Matched by | ensembl_id |

**Function**, from UniProt [P46100](https://www.uniprot.org/uniprotkb/P46100) (Chromatin remodeler ATRX):

> Involved in transcriptional regulation and chromatin remodeling. Facilitates DNA replication in multiple cellular environments and is required for efficient replication of a subset of genomic loci. Binds to DNA tandem repeat sequences in both telomeres and euchromatin and in vitro binds DNA quadruplex structures. May help stabilizing G-rich regions into regular chromatin structures by remodeling G4 DNA and incorporating H3.3-containing nucleosomes. Catalytic component of the chromatin …

**Summary**, from NCBI Gene [546](https://www.ncbi.nlm.nih.gov/gene/546):

> The protein encoded by this gene contains an ATPase/helicase domain, and thus it belongs to the SWI/SNF family of chromatin remodeling proteins. This protein is found to undergo cell cycle-dependent phosphorylation, which regulates its nuclear matrix and chromatin association, and suggests its involvement in the gene regulation at interphase and chromosomal segregation in mitosis. Mutations in this gene are associated with X-linked syndromes exhibiting cognitive disabilities as well as …

**Accessions** — [HGNC:886](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:886) · Entrez [546](https://www.ncbi.nlm.nih.gov/gene/546) · UniProt [P46100](https://www.uniprot.org/uniprotkb/P46100) · Ensembl [ENSG00000085224](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000085224)

## Data

Gene col 1418: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1418); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1418, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1418]; `tensor/DDL_lfc|DDL_z.npy` [1418]; `embed/gene_vectors.npy` [1418]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1418 or target_col == 1418). Every well: [[ATRX — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATRX.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
