---
symbol: "SAV1"
type: "gene"
col: 7563
ensembl_id: "ENSG00000151748"
name: "salvador family WW domain containing protein 1"
location: "14q22.1"
module: 14
arm: "+"
pooled_cpm: 75.04
n_lines_expressing: 49
n_dd_up: 9
n_dd_down: 13
n_dd_up_clean: 9
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# SAV1

*salvador family WW domain containing protein 1* — 14q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.22× (z +33.6, q 0e+00, up in 43 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.645× (z -12.5, q 2e-33, down in 32 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.705× (z -10.4, q 5e-23, down in 38 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SFR1]] (+0.64, fdr 7e-06), [[CCDC148]] (+0.54, fdr 2e-05), [[TNFAIP8]] (+0.54, fdr 2e-05); moves opposite to [[RPUSD4]] (-0.58, fdr 1e-05), [[ADPGK]] (-0.55, fdr 2e-05), [[C1orf216]] (-0.53, fdr 7e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[EHF]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7563.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.22×** | +33.6 | 0e+00 | 43/47 (CFPAC-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.21×** | +18.2 | 0e+00 | 42/48 (NCI-H2030, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.82×** | +17.3 | 0e+00 | 37/47 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.51×** | +12.3 | 8e-33 | 30/47 (C32, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.40×** | +10.0 | 1e-21 | 31/47 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +8.2 | 2e-14 | 24/47 (A498, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.60×** | +7.3 | 2e-11 | 31/47 (HOP62, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.26×** | +7.0 | 2e-10 | 22/47 (C32, A498, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.24×** | +6.5 | 6e-09 | 24/48 (A498, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 1.19× | +5.3 | 8e-06 | 21/47 (NCI-H460, SW48, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.19× | +4.7 | 1e-04 | 19/46 (H4, C32, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +4.4 | 5e-04 | 15/47 (COLO 205, LS 180, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~60% of this change | 1.15× | +4.3 | 7e-04 | 16/47 (NCI-H23, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.14× | +3.9 | 0.004 | 7/47 (NCI-H2347, SNU-423, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.13× | +3.7 | 0.010 | 18/46 (RKO, hTERT-HPNE, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.09× | +3.6 | 0.014 | 6/48 (HT-29, MIA PaCa-2, …) | rises with dose |  |
| [[Terfenadine (drug)]] 0.5 µM |  | 1.11× | +3.2 | 0.042 | 7/47 (CHP-212, NCI-H661, …) | two highest doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.12× | +3.1 | 0.050 | 10/46 (NCI-H2347, HEC-1-A, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.11× | +3.0 | 0.062 | 8/47 (LoVo, HT-29, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 10 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7563.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.645×** | -12.5 | 2e-33 | 32/42 (SK-MEL-2, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.770×** | -11.0 | 2e-25 | 26/48 (SW1417, LoVo, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.705×** | -10.4 | 5e-23 | 38/47 (LoVo, SK-MEL-2, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.730×** | -9.4 | 1e-18 | 33/47 (LoVo, HEC-1-A, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.800×** | -6.6 | 4e-09 | 25/48 (LoVo, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-733 (drug)]] 5 µM |  | **0.711×** | -5.3 | 1e-05 | 19/47 (LoVo, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 0.837× | -5.1 | 3e-05 | 19/47 (HEC-1-A, NCI-H2347, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.844× | -5.0 | 4e-05 | 15/47 (A-172, NCI-H1573, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.842× | -4.9 | 5e-05 | 19/46 (A549, LoVo, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.729×** | -4.9 | 5e-05 | 19/43 (LoVo, A549, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.734×** | -4.8 | 8e-05 | 15/47 (LoVo, SW1417, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | 0.844× | -4.8 | 9e-05 | 19/47 (A549, Panc 03.27, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~10% of this change | 0.862× | -4.1 | 0.002 | 19/44 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[EX229 (drug)]] 0.5 µM |  | **0.825×** | -4.1 | 0.002 | 15/48 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.770×** | -4.1 | 0.002 | 16/47 (LoVo, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.772×** | -4.0 | 0.002 | 17/47 (LoVo, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.827×** | -4.0 | 0.002 | 11/47 (LoVo, SW1417, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 0.872× | -3.9 | 0.003 | 13/47 (Hs 766T, CFPAC-1, …) | top dose only |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | 0.885× | -3.6 | 0.009 | 11/49 (SW 900, Panc 03.27, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.05 µM |  | 0.888× | -3.5 | 0.013 | 9/47 (Panc 03.27, AsPC-1, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.803×** | -3.4 | 0.018 | 15/47 (LoVo, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Afatinib (drug)]] 5 µM |  | 0.903× | -3.4 | 0.019 | 10/48 (LoVo, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | 0.892× | -3.4 | 0.019 | 9/47 (COLO 205, NCI-H2347, …) | two highest doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.901× | -3.1 | 0.050 | 10/47 (LoVo, C32, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7563. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 174 | 0 | 22 (11 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.176× (z -19.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.210× (z -18.3) |
| [[HEC-1-A (line)]] | alt | 116 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.342× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.571× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 178 | 1 | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +12.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.432× (z -14.5) ⚠ cell-cycle shift, explains ~15% of this change |
| [[CFPAC-1 (line)]] | alt | 91.1 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.85× (z +29.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.599× (z -9.4) ⚠ cell-cycle shift, explains ~15% of this change |
| [[A549 (line)]] | wt | 92.8 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +12.7) | [[Dinaciclib (drug)]] 0.5 µM 0.299× (z -13.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 92.4 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +12.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.517× (z -9.7) ⚠ cell-cycle shift, explains ~15% of this change |
| [[NCI-H2347 (line)]] | alt | 86.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +20.5) | — |
| [[PANC-1 (line)]] | alt | 46.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.69× (z +23.8) | — |
| [[SK-MEL-2 (line)]] | alt | 75.7 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +13.7) | [[Dinaciclib (drug)]] 5 µM 0.145× (z -19.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.373× (z -10.6) |
| [[A498 (line)]] | wt | 35.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +19.8) | — |
| [[C32 (line)]] | wt | 73.9 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +18.6) | [[Dinaciclib (drug)]] 5 µM 0.412× (z -9.2) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 51.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +20.2) | — |
| [[hTERT-HPNE (line)]] | wt | 50.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.87× (z +17.1) | — |
| [[J82 (line)]] | alt | 61.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +17.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 61.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +12.2) | — |
| [[NCI-H1792 (line)]] | alt | 83.4 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +15.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.475× (z -11.8) ⚠ cell-cycle shift, explains ~15% of this change |
| [[NCI-H460 (line)]] | wt | 90.3 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +14.2) | [[Dinaciclib (drug)]] 5 µM 0.332× (z -13.8) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 103 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +9.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.401× (z -8.8) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.413× (z -8.5) |
| [[A-172 (line)]] | wt | 38.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +14.6) | — |
| [[A-427 (line)]] | wt | 53.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +9.9) | — |
| [[AsPC-1 (line)]] | alt | 145 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.329× (z -11.7) ⚠ cell-cycle shift, explains ~15% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.289× (z -9.2) |
| [[COLO 205 (line)]] | alt | 66.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.346× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 67.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +19.3) | — |
| [[RKO (line)]] | wt | 76.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +12.0) | [[Dinaciclib (drug)]] 0.5 µM 0.408× (z -10.0) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 62.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.372× (z -9.6) ⚠ toxic; transcription drop · without an alert: [[Pyridoxine (drug)]] 0.5 µM 0.433× (z -8.5) |
| [[SW1417 (line)]] | alt | 119 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.398× (z -15.3) ⚠ cell-cycle shift, explains ~15% of this change |
| [[SW48 (line)]] | wt | 65.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +10.4) | — |
| [[SW480 (line)]] | alt | 67.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +12.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.642× (z -10.5) ⚠ cell-cycle shift, explains ~15% of this change |
| [[BT-474 (line)]] | alt | 65.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +14.5) | — |
| [[CHP-212 (line)]] | wt | 54.8 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0857× (z -12.5) |
| [[Hs 766T (line)]] | wt | 112 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -10.4) ⚠ cell-cycle shift, explains ~15% of this change |
| [[HS-578T (line)]] | alt | 35.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +12.7) | — |
| [[HT-29 (line)]] | alt | 59.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +14.1) | — |
| [[LS 180 (line)]] | wt | 50.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +11.4) | — |
| [[NCI-H23 (line)]] | alt | 73.9 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.71× (z +9.6) | — |
| [[NCI-H596 (line)]] | alt | 71.7 | 0 | 1 | — | [[Methylthiouracil (drug)]] 0.05 µM 0.195× (z -8.5) |
| [[NCI-H661 (line)]] | alt | 50.4 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.102× (z -8.9) |
| [[RPMI-7951 (line)]] | alt | 41.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +9.5) | — |
| [[SNU-1 (line)]] | wt | 49.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +9.5) | — |
| [[SNU-423 (line)]] | alt | 55.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +11.9) | — |
| [[SW 1271 (line)]] | alt | 83.5 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.143× (z -8.8) ⚠ transcription drop; cell-cycle shift, explains ~60% of this change |
| [[AN3 CA (line)]] | alt | 58.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 82.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 58.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 87.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 56.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.82 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 50.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 73.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 44.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7563), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SFR1]] | +0.64 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[CCDC148]] | +0.54 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[TNFAIP8]] | +0.54 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[COMMD3]] | +0.54 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[C21orf91]] | +0.54 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[IL2RG]] | +0.54 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[BCL10]] | +0.54 | +0.61 / +0.43 | both halves | 3e-05 |  |
| [[NEDD9]] | +0.53 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[TIGD2]] | +0.53 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[BHLHE41]] | +0.53 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[KLF5]] | +0.53 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[BTG1]] | +0.52 | +0.41 / +0.54 | both halves | 4e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPUSD4]] | -0.58 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[ADPGK]] | -0.55 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[C1orf216]] | -0.53 | -0.62 / -0.38 | both halves | 7e-05 |  |
| [[VTI1A]] | -0.52 | -0.38 / -0.62 | both halves | 7e-05 |  |
| [[GLB1]] | -0.51 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[STX16-NPEPL1]] | -0.51 | -0.33 / -0.61 | both halves | 1e-04 |  |
| [[AHSA1]] | -0.51 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[PDS5A]] | -0.51 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[CAPN15]] | -0.51 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[FUBP3]] | -0.51 | -0.33 / -0.59 | both halves | 1e-04 |  |
| [[SERPINH1]] | -0.50 | -0.34 / -0.58 | both halves | 1e-04 |  |
| [[THAP4]] | -0.50 | -0.45 / -0.49 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EHF]] | B | EHF activity raises SAV1's level | lines that do not express EHF (27) vs lines expressing it (23) | 1.27× lower at baseline in the lines without EHF | 0.045 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, IRF6, GJB3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.553). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (33.3, 2.5); signed map (6.6, 23.5). **Vector** length 109, 27.0% of its response variance represented; |z| ≥ 3 in 1,213 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.5 | +33.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.8 | +10.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.7 | +8.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.4 | +17.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.9 | +18.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.9 | +7.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.8 | +4.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.9 | +7.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.1 | +2.7 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.5 | -9.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.9 | -10.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -5.5 | -2.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | -5.2 | -11.0 |
|  | [[EX229 (drug)]] 5 µM |  | -4.8 | -4.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.2 | -5.3 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.1 | -4.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.0 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | salvador family WW domain containing protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q22.1 — chr14:50,632,058-50,668,306 (-) |
| Ensembl biotype | protein_coding |
| Also known as | WW45, WWP4, salvador |
| Reactome | 1 pathways, smallest: Signaling by Hippo |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H4B6](https://www.uniprot.org/uniprotkb/Q9H4B6) (Protein salvador homolog 1):

> Regulator of STK3/MST2 and STK4/MST1 in the Hippo signaling pathway which plays a pivotal role in organ size control and tumor suppression by restricting proliferation and promoting apoptosis. The core of this pathway is composed of a kinase cascade wherein STK3/MST2 and STK4/MST1, in complex with its regulatory protein SAV1, phosphorylates and activates LATS1/2 in complex with its regulatory protein MOB1, which in turn phosphorylates and inactivates YAP1 oncoprotein and WWTR1/TAZ. …

**Summary**, from NCBI Gene [60485](https://www.ncbi.nlm.nih.gov/gene/60485):

> WW domain-containing proteins are found in all eukaryotes and play an important role in the regulation of a wide variety of cellular functions such as protein degradation, transcription, and RNA splicing. This gene encodes a protein with two WW domains, a SARAH domain, and a coiled-coil region and is ubiquitously expressed in adult tissues. This protein binds to MST1 (mammalian sterile 20-like kinase 1) and promotes MST1-induced apoptosis. It has also been shown to bind to HAX1 (hematopoietic …

**Accessions** — [HGNC:17795](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17795) · Entrez [60485](https://www.ncbi.nlm.nih.gov/gene/60485) · UniProt [Q9H4B6](https://www.uniprot.org/uniprotkb/Q9H4B6) · Ensembl [ENSG00000151748](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151748)

## Data

Gene col 7563: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7563); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7563, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7563]; `tensor/DDL_lfc|DDL_z.npy` [7563]; `embed/gene_vectors.npy` [7563]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7563 or target_col == 7563). Every well: [[SAV1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SAV1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
