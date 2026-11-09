---
symbol: "UBXN7"
type: "gene"
col: 8824
ensembl_id: "ENSG00000163960"
name: "UBX domain protein 7"
location: "3q29"
module: 69
arm: "+"
pooled_cpm: 158.36
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 20
n_dd_up_clean: 12
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/069"]
generated_by: "tahoemap"
---

# UBXN7

*UBX domain protein 7* — 3q29

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.63× (z +15.1, q 0e+00, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (7 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.478× (z -16.0, q 0e+00, down in 48 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.422× (z -9.8, q 2e-20, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TCP11L2]] (+0.77, fdr 7e-06), [[KLHL24]] (+0.76, fdr 7e-06), [[CREBRF]] (+0.76, fdr 7e-06); moves opposite to [[ARMC6]] (-0.60, fdr 7e-06), [[WDR4]] (-0.59, fdr 7e-06), [[AGK]] (-0.59, fdr 2e-05).
> It is in [[Module 069]], a single-armed module (FOXO-mediated transcription).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 3 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8824.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.63×** | +15.1 | 0e+00 | 41/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.96×** | +14.6 | 1e-45 | 46/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.68×** | +11.2 | 9e-27 | 37/48 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +9.6 | 8e-20 | 32/49 (PANC-1, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.27×** | +9.3 | 2e-18 | 42/49 (MIA PaCa-2, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.05×** | +8.1 | 4e-14 | 37/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.41×** | +7.4 | 1e-11 | 34/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.41×** | +7.1 | 6e-11 | 33/47 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.39×** | +6.8 | 5e-10 | 33/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.36×** | +6.7 | 1e-09 | 33/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.36×** | +6.6 | 2e-09 | 28/48 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.34×** | +6.4 | 1e-08 | 31/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.22×** | +4.2 | 0.001 | 22/48 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.20×** | +4.0 | 0.003 | 22/48 (LS 180, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 1.18× | +3.6 | 0.010 | 23/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.17× | +3.4 | 0.026 | 18/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[crizotinib (drug)]] 5 µM |  | 1.17× | +3.3 | 0.034 | 14/48 (PANC-1, NCI-H1573, …) | top dose only |  |
| [[Terfenadine (drug)]] 5 µM |  | 1.10× | +3.0 | 0.075 | 0/48 | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8824.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.478×** | -16.0 | 0e+00 | 48/48 (NCI-H2347, AsPC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.501×** | -14.4 | 1e-44 | 40/44 (MIA PaCa-2, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.535×** | -13.5 | 2e-39 | 41/49 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[TAK-733 (drug)]] 5 µM |  | **0.422×** | -9.8 | 2e-20 | 47/48 (HEC-1-A, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.664×** | -8.2 | 3e-14 | 33/45 (CFPAC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[EX229 (drug)]] 5 µM |  | **0.488×** | -8.1 | 5e-14 | 43/48 (AsPC-1, Hs 766T, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.496×** | -7.9 | 2e-13 | 48/48 (NCI-H2347, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.505×** | -7.7 | 8e-13 | 45/48 (CFPAC-1, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.507×** | -7.7 | 9e-13 | 46/48 (AsPC-1, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.749×** | -6.0 | 1e-07 | 36/48 (NCI-H23, SK-MEL-2, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~23% of this change | **0.762×** | -5.7 | 8e-07 | 32/47 (MIA PaCa-2, NCI-H2347, …) | rises with dose |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.707×** | -5.3 | 4e-06 | 39/49 (Hs 766T, NCI-H1792, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.632×** | -5.2 | 9e-06 | 35/47 (HCT15, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.738×** | -4.7 | 1e-04 | 32/48 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.766×** | -4.1 | 0.001 | 30/48 (SW 1271, SNU-423, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.828×** | -3.8 | 0.004 | 23/48 (SW48, PANC-1, …) | all doses, stronger at high dose |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.848× | -3.6 | 0.011 | 19/49 (KATO III, NCI-H1573, …) | inconsistent across doses |  |
| [[Carbamazepine (drug)]] 5 µM |  | 0.863× | -3.2 | 0.042 | 15/47 (PANC-1, HT-29, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.756×** | -3.2 | 0.042 | 24/49 (NCI-H23, SW 1088, …) | top dose only | noisy plate (z scaled) |
| [[Busulfan (drug)]] 0.05 µM |  | 0.870× | -3.0 | 0.062 | 15/49 (HT-29, SNU-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8824. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 114 | 10 (5 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.19× (z +22.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.465× (z -12.0) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.353× (z -8.5) |
| [[PANC-1 (line)]] | alt | 138 | 9 (2 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +26.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.476× (z -13.0) ⚠ unreliable plate only |
| [[SW480 (line)]] | alt | 232 | 8 (2 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.57× (z +17.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.470× (z -13.8) ⚠ unreliable plate only |
| [[LoVo (line)]] | wt | 94.1 | 8 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.29× (z +19.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.420× (z -11.3) ⚠ unreliable plate only |
| [[SW1417 (line)]] | alt | 176 | 6 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +14.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.361× (z -13.9) ⚠ unreliable plate only |
| [[HS-578T (line)]] | alt | 157 | 5 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +11.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.430× (z -11.1) ⚠ unreliable plate only |
| [[HT-29 (line)]] | alt | 136 | 5 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +16.0) | [[Dinaciclib (drug)]] 5 µM 0.386× (z -12.6) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 153 | 6 (3 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +15.6) | [[Dinaciclib (drug)]] 0.5 µM 0.496× (z -9.7) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 131 | 3 (1 ⚠) | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.48× (z +15.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.281× (z -16.0) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.257× (z -9.0) |
| [[NCI-H2347 (line)]] | alt | 207 | 2 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +13.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.333× (z -18.3) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.375× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 206 | 1 | 5 (4 ⚠) | [[PH-797804 (drug)]] 5 µM 3.43× (z +10.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.469× (z -12.6) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.372× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 150 | 2 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +10.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.383× (z -12.7) ⚠ unreliable plate only |
| [[NCI-H1792 (line)]] | alt | 165 | 3 (1 ⚠) | 3 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 2.05× (z +9.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.378× (z -14.0) ⚠ unreliable plate only |
| [[BT-474 (line)]] | alt | 94.4 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.35× (z +13.1) | — |
| [[COLO 205 (line)]] | alt | 122 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.42× (z +14.2) | — |
| [[KATO III (line)]] | alt | 161 | 3 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.40× (z +15.4) | [[Dinaciclib (drug)]] 5 µM 0.282× (z -12.6) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 113 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.25× (z +15.0) | [[Dinaciclib (drug)]] 5 µM 0.318× (z -14.2) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 240 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +13.6) | [[Dinaciclib (drug)]] 5 µM 0.253× (z -20.0) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 241 | 2 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.72× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.304× (z -18.0) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 148 | 3 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.08× (z +11.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.262× (z -13.8) ⚠ unreliable plate only |
| [[A498 (line)]] | wt | 159 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +13.6) | [[Dinaciclib (drug)]] 0.5 µM 0.441× (z -10.9) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 187 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +11.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.412× (z -10.8) ⚠ unreliable plate only |
| [[A549 (line)]] | wt | 91.7 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +15.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.423× (z -10.7) ⚠ unreliable plate only |
| [[CFPAC-1 (line)]] | alt | 179 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.334× (z -13.4) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 203 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.11× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.294× (z -14.4) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 112 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +11.4) | [[EX229 (drug)]] 5 µM 0.236× (z -9.0) |
| [[NCI-H1573 (line)]] | alt | 118 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +13.2) | [[Dinaciclib (drug)]] 0.5 µM 0.424× (z -10.0) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 138 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +11.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.308× (z -11.5) ⚠ unreliable plate only |
| [[SNU-423 (line)]] | alt | 188 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.480× (z -10.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 119 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.517× (z -9.5) |
| [[H4 (line)]] | wt | 170 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.42× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.347× (z -10.1) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 234 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.422× (z -11.6) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 146 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.439× (z -9.7) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 215 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.380× (z -11.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 123 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +13.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.486× (z -8.6) ⚠ unreliable plate only |
| [[SK-MEL-2 (line)]] | alt | 165 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +14.3) | [[Dinaciclib (drug)]] 5 µM 0.349× (z -11.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 211 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.414× (z -12.3) ⚠ unreliable plate only |
| [[C-33 A (line)]] | alt | 87.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.313× (z -10.3) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 80.9 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 6.12× (z +10.3) | — |
| [[CHP-212 (line)]] | wt | 172 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.298× (z -9.4) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 140 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.16× (z +9.1) | — |
| [[RKO (line)]] | wt | 218 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.89× (z +9.0) | — |
| [[SW 1088 (line)]] | alt | 127 | 0 | 1 | — | [[Sulfatinib (drug)]] 0.05 µM 0.0638× (z -11.6) |
| [[SW 900 (line)]] | alt | 152 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.18× (z +9.0) | — |
| [[AN3 CA (line)]] | alt | 189 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 170 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 59.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 188 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8824), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCP11L2]] | +0.77 | +0.69 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[KLHL24]] | +0.76 | +0.62 / +0.80 | both halves | 7e-06 |  |
| [[CREBRF]] | +0.76 | +0.62 / +0.85 | both halves | 7e-06 |  |
| [[SERINC1]] | +0.76 | +0.64 / +0.80 | both halves | 7e-06 |  |
| [[RB1CC1]] | +0.76 | +0.53 / +0.80 | both halves | 1e-05 |  |
| [[SLU7]] | +0.75 | +0.48 / +0.81 | both halves | 2e-05 |  |
| [[ARID4A]] | +0.75 | +0.60 / +0.75 | both halves | 7e-06 |  |
| [[HBP1]] | +0.75 | +0.64 / +0.79 | both halves | 7e-06 |  |
| [[PIK3CA]] | +0.74 | +0.62 / +0.83 | both halves | 7e-06 |  |
| [[SYF2]] | +0.74 | +0.55 / +0.77 | both halves | 1e-05 |  |
| [[FBXL20]] | +0.73 | +0.59 / +0.74 | both halves | 7e-06 | pathway: Neddylation |
| [[WDR48]] | +0.72 | +0.55 / +0.76 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARMC6]] | -0.60 | -0.65 / -0.58 | both halves | 7e-06 |  |
| [[WDR4]] | -0.59 | -0.66 / -0.58 | both halves | 7e-06 |  |
| [[AGK]] | -0.59 | -0.48 / -0.62 | both halves | 2e-05 |  |
| [[NAA15]] | -0.59 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[PUS1]] | -0.57 | -0.60 / -0.59 | both halves | 7e-06 |  |
| [[INTS7]] | -0.57 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[CTPS1]] | -0.57 | -0.67 / -0.50 | both halves | 1e-05 |  |
| [[POLR1A]] | -0.56 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[EFTUD2]] | -0.56 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[SARS2]] | -0.56 | -0.54 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 069]] — FOXO-mediated transcription; 71 genes; every member is in the + arm (projection on the module's main direction 0.853). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-0.4, -44.6); signed map (-14.1, 9.5). **Vector** length 117, 41.7% of its response variance represented; |z| ≥ 3 in 1,469 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.7 | +9.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | +2.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.8 | +0.2 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | +2.6 | +2.3 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +2.6 | +0.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +1.2 |
|  | [[DTP3 (drug)]] 5 µM |  | +2.4 | -0.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -17.6 | -16.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -11.0 | -9.8 |
|  | [[EX229 (drug)]] 5 µM |  | -10.9 | -8.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -10.0 | -7.9 |
|  | [[venetoclax (drug)]] 5 µM |  | -9.7 | -7.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -9.2 | -7.7 |

## What is on record

|  |  |
|---|---|
| Name | UBX domain protein 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q29 — chr3:196,347,662-196,432,430 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0794; previously UBXD7 |
| Gene groups (HGNC) | UBX domain containing |
| Reactome | 5 pathways, smallest: KEAP1-NFE2L2 pathway; Cellular response to chemical stress; Neddylation |
| Matched by | ensembl_id |

**Function**, from UniProt [O94888](https://www.uniprot.org/uniprotkb/O94888) (UBX domain-containing protein 7):

> Ubiquitin-binding adapter that links a subset of NEDD8-associated cullin ring ligases (CRLs) to the segregase VCP/p97, to regulate turnover of their ubiquitination substrates.

**Summary**, from NCBI Gene [26043](https://www.ncbi.nlm.nih.gov/gene/26043):

> Enables RNA polymerase II-specific DNA-binding transcription factor binding activity; ubiquitin binding activity; and ubiquitin protein ligase binding activity. Predicted to be involved in proteasome-mediated ubiquitin-dependent protein catabolic process. Located in nucleoplasm. Part of VCP-NPL4-UFD1 AAA ATPase complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29119](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29119) · Entrez [26043](https://www.ncbi.nlm.nih.gov/gene/26043) · UniProt [O94888](https://www.uniprot.org/uniprotkb/O94888) · Ensembl [ENSG00000163960](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163960)

## Data

Gene col 8824: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8824); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8824, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8824]; `tensor/DDL_lfc|DDL_z.npy` [8824]; `embed/gene_vectors.npy` [8824]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8824 or target_col == 8824). Every well: [[UBXN7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBXN7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
