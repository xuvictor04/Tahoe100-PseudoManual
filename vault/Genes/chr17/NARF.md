---
symbol: "NARF"
type: "gene"
col: 6546
ensembl_id: "ENSG00000141562"
name: "nuclear prelamin A recognition factor"
location: "17q25.3"
module: 79
arm: "+"
pooled_cpm: 80.67
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 28
n_dd_up_clean: 10
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/079"]
generated_by: "tahoemap"
---

# NARF

*nuclear prelamin A recognition factor* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.64× (z +28.6, q 0e+00, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (8 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.322× (z -17.7, q 0e+00, down in 48 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.533× (z -9.8, q 2e-20, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANKZF1]] (+0.75, fdr 7e-06), [[KDM4B]] (+0.74, fdr 7e-06), [[ANKRD37]] (+0.73, fdr 7e-06); moves opposite to [[FKTN]] (-0.76, fdr 7e-06), [[COA7]] (-0.74, fdr 7e-06), [[RRP15]] (-0.72, fdr 7e-06).
> It is in [[Module 079]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6546.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.64×** | +28.6 | 0e+00 | 48/49 (AsPC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.92×** | +16.1 | 0e+00 | 46/48 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.38×** | +13.6 | 1e-39 | 45/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.32×** | +13.2 | 1e-37 | 47/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.37×** | +13.0 | 2e-36 | 46/50 (NCI-H460, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.93×** | +10.3 | 5e-23 | 47/48 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.53×** | +9.4 | 3e-19 | 34/48 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +5.1 | 3e-05 | 33/47 (MIA PaCa-2, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.38×** | +5.0 | 3e-05 | 30/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.37×** | +5.0 | 4e-05 | 26/48 (LoVo, COLO 205, …) | top dose only | cell-cycle shift (explains ~13% here); composition shift |
| [[PF-06260933 (drug)]] 5 µM |  | **1.81×** | +4.8 | 7e-05 | 29/48 (BT-474, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +3.3 | 0.048 | 3/50 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | 1.16× | +3.2 | 0.056 | 19/48 (HOP62, A-172, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.22×** | +3.1 | 0.071 | 19/48 (HT-29, SW480, …) | rises with dose |  |
| [[Terfenadine (drug)]] 5 µM |  | 1.15× | +3.1 | 0.071 | 12/48 (J82, HS-578T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6546.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.322×** | -17.7 | 0e+00 | 48/48 (NCI-H1792, LOX-IMVI, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.495×** | -10.6 | 1e-23 | 41/47 (SK-MEL-2, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.533×** | -9.8 | 2e-20 | 39/48 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.537×** | -9.7 | 4e-20 | 37/49 (SK-MEL-2, CHP-212, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.532×** | -9.5 | 3e-19 | 33/43 (SK-MEL-2, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.667×** | -8.9 | 4e-17 | 33/48 (A-172, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.547×** | -8.7 | 3e-16 | 40/45 (A549, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-733 (drug)]] 5 µM |  | **0.394×** | -7.6 | 2e-12 | 45/48 (LOX-IMVI, KATO III, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.614×** | -7.3 | 2e-11 | 34/48 (A549, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.430×** | -6.9 | 3e-10 | 44/48 (KATO III, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.671×** | -6.0 | 1e-07 | 40/48 (SNU-423, SW480, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **0.494×** | -5.8 | 4e-07 | 42/48 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.498×** | -5.7 | 5e-07 | 33/49 (HS-578T, hTERT-HPNE, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.504×** | -5.6 | 9e-07 | 38/48 (NCI-H1792, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.505×** | -5.6 | 9e-07 | 39/48 (LOX-IMVI, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.724×** | -5.0 | 2e-05 | 30/48 (AN3 CA, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.740×** | -4.7 | 9e-05 | 31/48 (C32, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belzutifan (drug)]] 5 µM |  | **0.621×** | -3.9 | 0.003 | 30/47 (SW 900, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.783×** | -3.8 | 0.004 | 25/48 (C32, HS-578T, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.750×** | -3.8 | 0.004 | 27/48 (C-33 A, PANC-1, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6546. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Panc 03.27 (line)]] | alt | 108 | 5 | 5 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.88× (z +21.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.345× (z -10.2) ⚠ unreliable plate only |
| [[A549 (line)]] | wt | 84.1 | 3 | 6 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.39× (z +15.8) | [[Dinaciclib (drug)]] 0.05 µM 0.202× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.378× (z -12.5) |
| [[LOX-IMVI (line)]] | wt | 119 | 2 | 7 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.37× (z +18.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.247× (z -15.3) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.365× (z -11.0) |
| [[SW480 (line)]] | alt | 109 | 6 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.24× (z +20.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.321× (z -14.0) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 70.5 | 6 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.84× (z +18.5) | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -16.3) |
| [[HEC-1-A (line)]] | alt | 61.5 | 7 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.08× (z +19.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.297× (z -12.1) ⚠ unreliable plate only |
| [[KATO III (line)]] | alt | 91.2 | 6 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.21× (z +21.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.280× (z -13.2) ⚠ unreliable plate only |
| [[MIA PaCa-2 (line)]] | alt | 69.0 | 7 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.33× (z +21.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.201× (z -12.1) ⚠ unreliable plate only |
| [[SK-MEL-2 (line)]] | alt | 115 | 2 | 6 (5 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.96× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.0964× (z -22.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.523× (z -9.2) |
| [[HOP62 (line)]] | alt | 107 | 6 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.53× (z +21.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.312× (z -11.7) ⚠ unreliable plate only |
| [[NCI-H460 (line)]] | wt | 52.1 | 6 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.43× (z +22.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.323× (z -10.6) ⚠ unreliable plate only |
| [[SW 900 (line)]] | alt | 90.7 | 3 | 4 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.02× (z +19.2) | [[Dinaciclib (drug)]] 5 µM 0.179× (z -16.1) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 41.4 | 5 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.09× (z +24.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.228× (z -12.3) ⚠ unreliable plate only |
| [[BT-474 (line)]] | alt | 87.8 | 3 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +13.8) | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -11.2) |
| [[C32 (line)]] | wt | 116 | 2 | 4 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.22× (z +12.1) | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -12.6) |
| [[LoVo (line)]] | wt | 56.7 | 5 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.44× (z +24.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.384× (z -8.7) ⚠ unreliable plate only |
| [[LS 180 (line)]] | wt | 107 | 5 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.36× (z +17.8) | [[Dinaciclib (drug)]] 0.05 µM 0.347× (z -10.2) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 68.5 | 5 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.89× (z +18.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.274× (z -10.7) ⚠ unreliable plate only |
| [[SHP-77 (line)]] | alt | 111 | 3 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.32× (z +16.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.311× (z -11.6) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.346× (z -10.5) |
| [[SNU-423 (line)]] | alt | 105 | 4 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.34× (z +16.7) | [[Homoharringtonine (drug)]] 5 µM 0.469× (z -10.3) |
| [[CFPAC-1 (line)]] | alt | 72.3 | 3 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.03× (z +19.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.305× (z -11.5) ⚠ unreliable plate only |
| [[HS-578T (line)]] | alt | 94.9 | 2 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.90× (z +15.1) | [[Homoharringtonine (drug)]] 0.5 µM 0.234× (z -14.7) |
| [[HT-29 (line)]] | alt | 81.6 | 3 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.73× (z +18.5) | [[Dinaciclib (drug)]] 0.05 µM 0.307× (z -10.8) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 105 | 2 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.42× (z +14.0) | [[Dinaciclib (drug)]] 0.05 µM 0.184× (z -12.6) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 67.9 | 3 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.46× (z +19.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.277× (z -11.5) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.362× (z -9.1) |
| [[NCI-H2347 (line)]] | alt | 67.5 | 1 | 4 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +11.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.334× (z -11.6) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.395× (z -9.9) |
| [[SNU-1 (line)]] | wt | 49.9 | 4 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.25× (z +12.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.240× (z -8.9) ⚠ unreliable plate only |
| [[A498 (line)]] | wt | 43.1 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.67× (z +12.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.350× (z -9.6) ⚠ unreliable plate only |
| [[C-33 A (line)]] | alt | 86.5 | 2 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.99× (z +12.7) | [[Homoharringtonine (drug)]] 0.5 µM 0.319× (z -9.5) |
| [[COLO 205 (line)]] | alt | 130 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.74× (z +16.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.296× (z -9.3) ⚠ unreliable plate only |
| [[NCI-H1792 (line)]] | alt | 95.2 | 2 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.41× (z +17.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.189× (z -16.7) ⚠ unreliable plate only |
| [[SW1417 (line)]] | alt | 89.6 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.01× (z +14.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.391× (z -8.5) ⚠ unreliable plate only |
| [[SW48 (line)]] | wt | 67.3 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.99× (z +19.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.280× (z -8.8) ⚠ unreliable plate only |
| [[CHP-212 (line)]] | wt | 208 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.215× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.357× (z -10.4) |
| [[HCT15 (line)]] | alt | 130 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.45× (z +15.4) | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -14.2) |
| [[Hs 766T (line)]] | wt | 73.2 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.96× (z +16.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.281× (z -10.5) ⚠ unreliable plate only |
| [[J82 (line)]] | alt | 76.4 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.07× (z +17.3) | [[Dinaciclib (drug)]] 0.05 µM 0.341× (z -8.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 72.5 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.67× (z +22.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.265× (z -13.5) ⚠ unreliable plate only |
| [[A-427 (line)]] | wt | 76.7 | 1 | 1 (1 ⚠) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 1.88× (z +9.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.320× (z -11.4) ⚠ unreliable plate only |
| [[AN3 CA (line)]] | alt | 111 | 0 | 2 | — | [[Harringtonine (drug)]] 0.5 µM 0.117× (z -14.4) |
| [[H4 (line)]] | wt | 85.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.93× (z +12.9) | — |
| [[NCI-H1573 (line)]] | alt | 56.1 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.12× (z +12.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.305× (z -9.2) |
| [[NCI-H2030 (line)]] | alt | 34.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.83× (z +15.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.297× (z -9.7) ⚠ unreliable plate only |
| [[SW 1271 (line)]] | alt | 98.9 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.36× (z +9.1) | [[Pyridoxine (drug)]] 0.5 µM 0.104× (z -9.9) |
| [[HepG2_C3A (line)]] | wt | 101 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.49× (z +15.0) | — |
| [[NCI-H596 (line)]] | alt | 91.9 | 0 | 1 (1 ⚠) | — | [[Pentoxifylline (drug)]] 0.05 µM 0.0892× (z -10.4) ⚠ transcription drop |
| [[NCI-H661 (line)]] | alt | 78.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -10.2) |
| [[RPMI-7951 (line)]] | alt | 65.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.72× (z +11.6) | — |
| [[SW 1088 (line)]] | alt | 68.7 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0583× (z -9.1) ⚠ unreliable plate only |
| [[NCI-H2122 (line)]] | alt | 105 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6546), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKZF1]] | +0.75 | +0.64 / +0.78 | both halves | 7e-06 |  |
| [[KDM4B]] | +0.74 | +0.81 / +0.67 | both halves | 7e-06 |  |
| [[ANKRD37]] | +0.73 | +0.69 / +0.74 | both halves | 7e-06 |  |
| [[KDM3A]] | +0.73 | +0.80 / +0.61 | both halves | 7e-06 |  |
| [[FBXL20]] | +0.73 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[SAP30-DT]] | +0.72 | +0.75 / +0.68 | both halves | 7e-06 |  |
| [[TESK2]] | +0.70 | +0.51 / +0.75 | both halves | 1e-05 |  |
| [[TAF5]] | +0.70 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[NDUFA2]] | +0.70 | +0.52 / +0.68 | both halves | 1e-05 |  |
| [[HINFP]] | +0.70 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[KMT5C]] | +0.69 | +0.57 / +0.73 | both halves | 1e-05 |  |
| [[AAMDC]] | +0.69 | +0.59 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FKTN]] | -0.76 | -0.72 / -0.75 | both halves | 7e-06 |  |
| [[COA7]] | -0.74 | -0.69 / -0.68 | both halves | 7e-06 |  |
| [[RRP15]] | -0.72 | -0.62 / -0.73 | both halves | 7e-06 |  |
| [[NAA15]] | -0.70 | -0.67 / -0.69 | both halves | 7e-06 |  |
| [[POGK]] | -0.68 | -0.63 / -0.67 | both halves | 7e-06 |  |
| [[TCERG1]] | -0.68 | -0.59 / -0.65 | both halves | 7e-06 |  |
| [[MAK16]] | -0.67 | -0.65 / -0.66 | both halves | 7e-06 |  |
| [[MRRF]] | -0.67 | -0.53 / -0.70 | both halves | 1e-05 |  |
| [[RAD51D]] | -0.66 | -0.63 / -0.62 | both halves | 7e-06 |  |
| [[DNAH14]] | -0.66 | -0.60 / -0.60 | both halves | 7e-06 |  |
| [[PTPN11]] | -0.66 | -0.55 / -0.66 | both halves | 1e-05 |  |
| [[COMMD10]] | -0.66 | -0.54 / -0.68 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers NARF's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.5% of all compounds | 0.008 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SPAG4]] | B | SPAG4 activity raises NARF's level | lines that do not express SPAG4 (6) vs lines expressing it (44) | 1.33× lower at baseline in the lines without SPAG4 | 0.064 | ⚠ within organs, on part of the lines; co-occurs with PRDM2; also absent: ZNF222, ADAL |
| [[DNAH14]] | B | DNAH14 activity raises NARF's level | lines that do not express DNAH14 (10) vs lines expressing it (40) | 1.27× lower at baseline in the lines without DNAH14 | 0.089 | ⚠ within organs, on part of the lines; also absent: ZNF345, ZNF790, ENSG00000289516; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 079]] — hypoxia; 57 genes; every member is in the + arm (projection on the module's main direction 0.729). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (3.2, -39.2); signed map (-34.1, 23.2). **Vector** length 152, 53.3% of its response variance represented; |z| ≥ 3 in 1,420 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *hypoxia* (control, mean cos +0.64 to 5); *glycolysis* (hallmark, mean cos +0.54 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +7.8 | +13.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.3 | +16.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.3 | +28.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +4.3 | +5.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +4.0 | +2.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.5 | +4.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.2 | +2.4 |
|  | [[Fumaric acid (drug)]] 5 µM |  | +3.2 | +2.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +2.9 | +2.6 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -13.3 | -8.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -12.3 | -17.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -11.8 | -9.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -11.2 | -8.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -11.1 | -9.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -8.7 | -7.6 |
|  | [[EX229 (drug)]] 5 µM |  | -8.4 | -5.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -8.0 | -6.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -6.6 | -6.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -6.0 | -5.6 |

## What is on record

|  |  |
|---|---|
| Name | nuclear prelamin A recognition factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:82,458,180-82,490,537 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10067, DKFZp434G0420, IOP2 |
| Hallmark sets | HEME_METABOLISM |
| Matched by | ensembl_id |

UniProt [Q9UHQ1](https://www.uniprot.org/uniprotkb/Q9UHQ1) carries no function annotation.

**Summary**, from NCBI Gene [26502](https://www.ncbi.nlm.nih.gov/gene/26502):

> Several proteins have been found to be prenylated and methylated at their carboxyl-terminal ends. Prenylation was initially believed to be important only for membrane attachment. However, another role for prenylation appears to be its importance in protein-protein interactions. The only nuclear proteins known to be prenylated in mammalian cells are prelamin A- and B-type lamins. Prelamin A is farnesylated and carboxymethylated on the cysteine residue of a carboxyl-terminal CaaX motif. This …

**Accessions** — [HGNC:29916](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29916) · Entrez [26502](https://www.ncbi.nlm.nih.gov/gene/26502) · UniProt [Q9UHQ1](https://www.uniprot.org/uniprotkb/Q9UHQ1) · Ensembl [ENSG00000141562](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141562)

## Data

Gene col 6546: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6546); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6546, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6546]; `tensor/DDL_lfc|DDL_z.npy` [6546]; `embed/gene_vectors.npy` [6546]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6546 or target_col == 6546). Every well: [[NARF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NARF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
