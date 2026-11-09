---
symbol: "NEK7"
type: "gene"
col: 7517
ensembl_id: "ENSG00000151414"
name: "NIMA related kinase 7"
location: "1q31.3"
module: 69
arm: "+"
pooled_cpm: 276.13
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 21
n_dd_up_clean: 1
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/069"]
generated_by: "tahoemap"
---

# NEK7

*NIMA related kinase 7* — 1q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[PH-797804 (drug)]] 5 µM: 1.74× (z +5.3, q 8e-05, up in 37 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[PH-797804 (drug)]] 5 µM in 2 lines (C32 9.89×, SW48 8.46×); [[TAK-901 (drug)]] 5 µM in 2 lines (C32 7.46×, SW48 6.44×); [[TAK-901 (drug)]] 0.05 µM in 2 lines (LOX-IMVI 2.87×, SW48 3.21×).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (9 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.367× (z -17.5, q 0e+00, down in 48 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Abemaciclib (drug)]] 5 µM: 0.360× (z -9.7, q 5e-20, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KDM6A]] (+0.70, fdr 8e-06), [[PCMTD1]] (+0.69, fdr 7e-06), [[TXNDC16]] (+0.67, fdr 4e-05); moves opposite to [[METTL2B]] (-0.54, fdr 2e-05), [[FAM83G]] (-0.52, fdr 2e-05), [[ZNG1F]] (-0.50, fdr 2e-05).
> It is in [[Module 069]], a single-armed module (FOXO-mediated transcription).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7517.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[PH-797804 (drug)]] 5 µM in 2 lines (C32 9.89×, SW48 8.46×); [[TAK-901 (drug)]] 5 µM in 2 lines (C32 7.46×, SW48 6.44×); [[TAK-901 (drug)]] 0.05 µM in 2 lines (LOX-IMVI 2.87×, SW48 3.21×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **1.74×** | +5.3 | 8e-05 | 37/48 (C32, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 1.20× | +3.4 | 0.19 | 21/48 (PANC-1, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 1.13× | +3.2 | 0.29 | 2/48 (SW48, NCI-H661) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.0 | 0.36 | 19/48 (RKO, MIA PaCa-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 12 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7517.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.367×** | -17.5 | 0e+00 | 48/48 (NCI-H2347, HEC-1-A, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.535×** | -11.5 | 4e-28 | 42/49 (NCI-H2347, AsPC-1, …) | all doses, flat | composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **0.360×** | -9.7 | 5e-20 | 48/48 (KATO III, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.565×** | -9.7 | 5e-20 | 35/45 (NCI-H2347, LoVo, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.583×** | -9.5 | 2e-19 | 36/44 (SK-MEL-2, NCI-H1573, …) | all doses, flat | composition shift |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.368×** | -9.5 | 2e-19 | 47/48 (KATO III, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.606×** | -9.2 | 3e-18 | 42/48 (SK-MEL-2, HT-29, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.381×** | -9.2 | 3e-18 | 47/48 (KATO III, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.622×** | -8.7 | 2e-16 | 46/48 (KATO III, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.431×** | -8.0 | 7e-14 | 45/48 (RKO, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.652×** | -7.5 | 2e-12 | 40/47 (HepG2/C3A, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[venetoclax (drug)]] 5 µM |  | **0.455×** | -7.5 | 4e-12 | 45/48 (MIA PaCa-2, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.687×** | -6.9 | 2e-10 | 39/48 (KATO III, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.754×** | -5.2 | 9e-06 | 28/48 (NCI-H23, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~22% of this change | **0.775×** | -4.7 | 1e-04 | 35/48 (NCI-H2347, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.653×** | -4.3 | 5e-04 | 38/48 (SK-MEL-2, A-427, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.656×** | -4.3 | 6e-04 | 40/49 (NCI-H23, KATO III, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.664×** | -3.9 | 0.003 | 26/47 (SNU-1, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.816×** | -3.5 | 0.012 | 27/48 (LoVo, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.730×** | -3.2 | 0.036 | 21/48 (NCI-H23, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.842× | -3.1 | 0.039 | 22/48 (LoVo, NCI-H1573, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.885× | -3.0 | 0.052 | 14/48 (NCI-H460, SW1417, …) | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.847× | -3.0 | 0.052 | 17/48 (hTERT-HPNE, NCI-H1573, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7517. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 391 | 0 | 8 (6 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.270× (z -18.2) ⚠ unreliable plate only · without an alert: [[Abemaciclib (drug)]] 5 µM 0.269× (z -9.9) |
| [[KATO III (line)]] | alt | 251 | 0 | 7 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.236× (z -16.8) ⚠ unreliable plate only · without an alert: [[c-Kit-IN-1 (drug)]] 5 µM 0.200× (z -10.2) |
| [[C32 (line)]] | wt | 403 | 3 | 3 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 9.89× (z +13.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.365× (z -11.1) ⚠ unreliable plate only |
| [[NCI-H23 (line)]] | alt | 150 | 0 | 6 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.258× (z -15.7) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.381× (z -11.7) |
| [[CFPAC-1 (line)]] | alt | 360 | 0 | 5 (5 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.309× (z -13.7) ⚠ unreliable plate only |
| [[HT-29 (line)]] | alt | 268 | 0 | 5 (4 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.393× (z -12.5) |
| [[LoVo (line)]] | wt | 208 | 1 (1 ⚠) | 4 (3 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 1.96× (z +8.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.382× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.532× (z -8.5) |
| [[SW1417 (line)]] | alt | 348 | 0 | 5 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.302× (z -14.7) ⚠ unreliable plate only · without an alert: [[Abemaciclib (drug)]] 5 µM 0.258× (z -9.0) |
| [[SW48 (line)]] | wt | 315 | 3 | 2 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 8.46× (z +10.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.155× (z -16.5) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.344× (z -9.9) |
| [[A-427 (line)]] | wt | 458 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.455× (z -14.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.479× (z -9.6) |
| [[A549 (line)]] | wt | 199 | 0 | 4 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.353× (z -13.4) ⚠ unreliable plate only |
| [[AsPC-1 (line)]] | alt | 393 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.273× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.393× (z -10.4) |
| [[NCI-H1573 (line)]] | alt | 230 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.198× (z -20.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[NCI-H460 (line)]] | wt | 602 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.353× (z -13.5) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.359× (z -9.7) |
| [[RKO (line)]] | wt | 189 | 1 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +9.8) ⚠ cell-cycle shift, would explain all of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.262× (z -14.0) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.218× (z -8.6) |
| [[SK-MEL-2 (line)]] | alt | 240 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.128× (z -26.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.311× (z -15.4) |
| [[SW 900 (line)]] | alt | 374 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.303× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.386× (z -10.1) |
| [[A498 (line)]] | wt | 187 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.451× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[HepG2_C3A (line)]] | wt | 185 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.354× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[Hs 766T (line)]] | wt | 529 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.429× (z -9.8) ⚠ cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 242 | 0 | 3 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.228× (z -17.0) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.380× (z -11.7) |
| [[Panc 03.27 (line)]] | alt | 280 | 0 | 3 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.437× (z -9.5) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.459× (z -9.3) |
| [[PANC-1 (line)]] | alt | 195 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.37× (z +12.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.374× (z -14.0) ⚠ unreliable plate only |
| [[SNU-423 (line)]] | alt | 282 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.379× (z -12.1) |
| [[BT-474 (line)]] | alt | 251 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.390× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[HEC-1-A (line)]] | alt | 198 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.212× (z -17.7) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.482× (z -8.7) |
| [[J82 (line)]] | alt | 384 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -13.1) ⚠ cell-cycle shift, explains ~59% of this change |
| [[LOX-IMVI (line)]] | wt | 280 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.87× (z +11.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.291× (z -13.3) ⚠ unreliable plate only |
| [[NCI-H1792 (line)]] | alt | 273 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.580× (z -9.3) ⚠ cell-cycle shift, explains ~59% of this change |
| [[SNU-1 (line)]] | wt | 202 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.226× (z -13.9) ⚠ unreliable plate only |
| [[AN3 CA (line)]] | alt | 215 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.253× (z -9.8) ⚠ unreliable plate only |
| [[C-33 A (line)]] | alt | 157 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.296× (z -10.8) ⚠ unreliable plate only |
| [[CHP-212 (line)]] | wt | 309 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.287× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[COLO 205 (line)]] | alt | 177 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.382× (z -10.8) ⚠ unreliable plate only |
| [[H4 (line)]] | wt | 161 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.353× (z -9.8) ⚠ unreliable plate only |
| [[HCT15 (line)]] | alt | 175 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.369× (z -10.0) ⚠ unreliable plate only |
| [[HOP62 (line)]] | alt | 179 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.318× (z -13.5) ⚠ unreliable plate only |
| [[HS-578T (line)]] | alt | 179 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.393× (z -10.6) ⚠ unreliable plate only |
| [[NCI-H2030 (line)]] | alt | 275 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.307× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[NCI-H661 (line)]] | alt | 256 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.223× (z -9.1) ⚠ unreliable plate only |
| [[RPMI-7951 (line)]] | alt | 188 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.314× (z -12.1) ⚠ unreliable plate only |
| [[SHP-77 (line)]] | alt | 123 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.352× (z -10.4) ⚠ unreliable plate only |
| [[SW480 (line)]] | alt | 168 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.425× (z -12.3) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 408 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 178 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 231 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 288 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 292 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 176 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7517), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KDM6A]] | +0.70 | +0.58 / +0.79 | both halves | 8e-06 |  |
| [[PCMTD1]] | +0.69 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[TXNDC16]] | +0.67 | +0.43 / +0.60 | both halves | 4e-05 |  |
| [[ELF2]] | +0.64 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[SPOPL]] | +0.63 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[CNOT6L]] | +0.62 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[FBXL20]] | +0.60 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[HBP1]] | +0.60 | +0.48 / +0.67 | both halves | 2e-05 |  |
| [[CCDC28A]] | +0.60 | +0.53 / +0.70 | both halves | 1e-05 | pathway: HALLMARK_HEME_METABOLISM |
| [[TMEM59]] | +0.59 | +0.44 / +0.68 | both halves | 3e-05 |  |
| [[ZBTB44]] | +0.59 | +0.40 / +0.66 | both halves | 4e-05 |  |
| [[SERINC1]] | +0.58 | +0.41 / +0.70 | both halves | 4e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METTL2B]] | -0.54 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[FAM83G]] | -0.52 | -0.59 / -0.46 | both halves | 2e-05 |  |
| [[ZNG1F]] | -0.50 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[DNAJA3]] | -0.50 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[OSGIN1]] | -0.50 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[DNTTIP2]] | -0.49 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[DDX19A]] | -0.48 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[TM9SF4]] | -0.48 | -0.38 / -0.53 | both halves | 6e-05 |  |
| [[ZNF473]] | -0.48 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[ZNF202]] | -0.47 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[SNAPC4]] | -0.47 | -0.44 / -0.43 | both halves | 4e-05 |  |
| [[PUS1]] | -0.47 | -0.46 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 069]] — FOXO-mediated transcription; 71 genes; every member is in the + arm (projection on the module's main direction 0.663). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-0.8, -42.1); signed map (-14.2, 11.4). **Vector** length 121, 44.8% of its response variance represented; |z| ≥ 3 in 1,323 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.6 | +2.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.4 | +3.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | +3.5 | -3.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.3 | +0.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | +0.5 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +2.4 | +2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.3 | +0.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.3 | +0.4 |
|  | [[Alpelisib (drug)]] 5 µM |  | +2.1 | +0.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -15.5 | -17.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -10.7 | -9.7 |
|  | [[EX229 (drug)]] 5 µM |  | -9.4 | -8.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -9.3 | -9.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -9.0 | -9.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -7.9 | -9.2 |

## What is on record

|  |  |
|---|---|
| Name | NIMA related kinase 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q31.3 — chr1:198,156,994-198,322,420 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | NIMA related kinase family |
| Hallmark sets | UV_RESPONSE_DN, HEME_METABOLISM |
| Reactome | 9 pathways, smallest: Activation of NIMA Kinases NEK9, NEK6, NEK7; Nuclear Pore Complex (NPC) Disassembly; Nuclear Envelope Breakdown |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TDX7](https://www.uniprot.org/uniprotkb/Q8TDX7) (Serine/threonine-protein kinase Nek7):

> Protein kinase which plays an important role in mitotic cell cycle progression. Required for microtubule nucleation activity of the centrosome, robust mitotic spindle formation and cytokinesis. Phosphorylates EML4 at 'Ser-146', promoting its dissociation from microtubules during mitosis which is required for efficient chromosome congression. Phosphorylates RPS6KB1 (By similarity). Acts as an essential activator of the NLRP3 inflammasome assembly independently of its kinase activity. Acts by …

**Summary**, from NCBI Gene [140609](https://www.ncbi.nlm.nih.gov/gene/140609):

> NIMA-related kinases share high amino acid sequence identity with the gene product of the Aspergillus nidulans 'never in mitosis A' gene, which controls initiation of mitosis.[supplied by OMIM, Jul 2002]

**Accessions** — [HGNC:13386](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13386) · Entrez [140609](https://www.ncbi.nlm.nih.gov/gene/140609) · UniProt [Q8TDX7](https://www.uniprot.org/uniprotkb/Q8TDX7) · Ensembl [ENSG00000151414](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151414)

## Data

Gene col 7517: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7517); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7517, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7517]; `tensor/DDL_lfc|DDL_z.npy` [7517]; `embed/gene_vectors.npy` [7517]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7517 or target_col == 7517). Every well: [[NEK7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NEK7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
