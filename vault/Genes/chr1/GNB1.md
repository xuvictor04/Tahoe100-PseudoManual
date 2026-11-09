---
symbol: "GNB1"
type: "gene"
col: 1220
ensembl_id: "ENSG00000078369"
name: "G protein subunit beta 1"
location: "1p36.33"
module: 111
arm: "+"
pooled_cpm: 319.7
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 14
n_dd_up_clean: 2
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/111"]
generated_by: "tahoemap"
---

# GNB1

*G protein subunit beta 1* — 1p36.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.32× (z +7.3, q 2e-10, up in 36 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 1.60× (z +6.4, q 4e-08, up in 34 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Niclosamide (olamine) (drug)]] 5 µM in 4 lines (COLO 205 3.19×, LoVo 2.18×, LS 180 2.06×, SW48 2.29×; ⚠ toxic); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (PANC-1 1.83×, KATO III 1.74×, SK-MEL-2 1.70×, SW480 1.53×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (PANC-1 1.77×, KATO III 1.74×, A-427 1.62×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.519× (z -24.1, q 0e+00, down in 49 of 49 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDC42]] (+0.74, fdr 7e-06), [[ACTR3]] (+0.67, fdr 7e-06), [[CAPZB]] (+0.65, fdr 7e-06); moves opposite to [[WHAMM]] (-0.59, fdr 1e-05), [[HMGCL]] (-0.58, fdr 1e-05), [[TMEM101]] (-0.58, fdr 7e-05).
> It is in [[Module 111]], a single-armed module (Cell-Cell communication).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 8 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1220.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Niclosamide (olamine) (drug)]] 5 µM in 4 lines (COLO 205 3.19×, LoVo 2.18×, LS 180 2.06×, SW48 2.29×; ⚠ toxic); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (PANC-1 1.83×, KATO III 1.74×, SK-MEL-2 1.70×, SW480 1.53×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (PANC-1 1.77×, KATO III 1.74×, A-427 1.62×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.32×** | +7.3 | 2e-10 | 36/49 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.60×** | +6.4 | 4e-08 | 34/49 (C32, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.29×** | +6.3 | 5e-08 | 27/44 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.28×** | +6.1 | 2e-07 | 27/47 (COLO 205, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.56×** | +6.0 | 2e-07 | 35/48 (C32, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.19× | +4.2 | 0.003 | 20/45 (A-427, CHP-212, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.17× | +4.1 | 0.003 | 19/48 (HT-29, Hs 766T, …) | inconsistent across doses |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 1.15× | +3.7 | 0.018 | 5/49 (SW1417, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.14× | +3.4 | 0.049 | 13/47 (H4, SW480, …) | rises with dose | low cells (technical?) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.14× | +3.3 | 0.056 | 12/48 (CFPAC-1, COLO 205, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 1.14× | +3.3 | 0.057 | 12/47 (H4, NCI-H23, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1220.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.519×** | -24.1 | 0e+00 | 49/49 (HEC-1-A, HOP62, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.542×** | -15.9 | 0e+00 | 46/48 (AsPC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.568×** | -14.7 | 0e+00 | 46/48 (AsPC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.624×** | -12.3 | 2e-32 | 45/48 (A-172, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.692×** | -9.6 | 1e-19 | 38/48 (NCI-H1573, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.698×** | -9.3 | 9e-19 | 42/48 (SK-MEL-2, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **0.707×** | -8.7 | 4e-16 | 38/47 (NCI-H1573, hTERT-HPNE, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.725×** | -8.0 | 6e-14 | 36/48 (HOP62, SW480, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.829×** | -6.9 | 3e-10 | 25/48 (HOP62, SW1417, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.837× | -6.6 | 3e-09 | 26/48 (HOP62, RPMI-7951, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.785×** | -6.3 | 2e-08 | 30/48 (HOP62, NCI-H23, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.786×** | -6.3 | 2e-08 | 31/48 (HOP62, MIA PaCa-2, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.809×** | -5.3 | 4e-06 | 27/50 (SW480, KATO III, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.680×** | -5.2 | 6e-06 | 35/49 (AsPC-1, RPMI-7951, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.872× | -5.0 | 2e-05 | 21/48 (NCI-H1792, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Ponatinib (drug)]] 5 µM |  | 0.834× | -4.7 | 8e-05 | 24/48 (H4, HOP62, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.878× | -3.9 | 0.003 | 15/48 (CFPAC-1, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 0.868× | -3.6 | 0.009 | 18/47 (CFPAC-1, SW480, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.829×** | -3.4 | 0.015 | 21/48 (NCI-H23, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.878× | -3.4 | 0.015 | 10/48 (A-172, H4, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1220. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 496 | 0 | 10 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.358× (z -24.8) |
| [[SW480 (line)]] | alt | 304 | 1 (1 ⚠) | 8 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.53× (z +8.5) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.467× (z -21.6) |
| [[A-172 (line)]] | wt | 274 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.420× (z -15.1) |
| [[H4 (line)]] | wt | 460 | 0 | 8 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.468× (z -16.5) |
| [[AsPC-1 (line)]] | alt | 348 | 0 | 7 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -24.8) |
| [[KATO III (line)]] | alt | 220 | 2 (2 ⚠) | 5 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.74× (z +9.7) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.456× (z -19.4) |
| [[NCI-H1573 (line)]] | alt | 245 | 0 | 7 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.391× (z -20.8) |
| [[HEC-1-A (line)]] | alt | 407 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.383× (z -24.9) |
| [[PANC-1 (line)]] | alt | 364 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 1.83× (z +11.4) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.502× (z -18.5) |
| [[SK-MEL-2 (line)]] | alt | 252 | 1 (1 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.70× (z +8.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.395× (z -15.3) |
| [[A-427 (line)]] | wt | 319 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 1.62× (z +8.6) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.439× (z -15.3) |
| [[C-33 A (line)]] | alt | 357 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.506× (z -15.0) |
| [[J82 (line)]] | alt | 453 | 0 | 5 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.519× (z -14.7) |
| [[LoVo (line)]] | wt | 262 | 1 (1 ⚠) | 4 | [[Niclosamide (olamine) (drug)]] 5 µM 2.18× (z +13.5) ⚠ toxic | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.506× (z -17.4) |
| [[LOX-IMVI (line)]] | wt | 241 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.641× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.533× (z -9.8) |
| [[MIA PaCa-2 (line)]] | alt | 398 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.482× (z -18.2) |
| [[NCI-H23 (line)]] | alt | 400 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.392× (z -17.6) |
| [[SW48 (line)]] | wt | 290 | 2 (2 ⚠) | 3 | [[Niclosamide (olamine) (drug)]] 5 µM 2.29× (z +10.6) ⚠ toxic | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.458× (z -14.7) |
| [[A549 (line)]] | wt | 279 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.460× (z -17.3) |
| [[BT-474 (line)]] | alt | 353 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -17.9) |
| [[CFPAC-1 (line)]] | alt | 431 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.356× (z -22.0) |
| [[Hs 766T (line)]] | wt | 398 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.486× (z -10.5) |
| [[NCI-H2347 (line)]] | alt | 362 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.543× (z -15.5) |
| [[NCI-H460 (line)]] | wt | 251 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.446× (z -15.5) |
| [[COLO 205 (line)]] | alt | 219 | 1 (1 ⚠) | 2 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 3.19× (z +14.4) ⚠ toxic | [[Homoharringtonine (drug)]] 5 µM 0.539× (z -11.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.561× (z -10.4) |
| [[hTERT-HPNE (line)]] | wt | 359 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.428× (z -10.5) ⚠ toxic; cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.562× (z -10.5) |
| [[LS 180 (line)]] | wt | 277 | 1 (1 ⚠) | 2 | [[Niclosamide (olamine) (drug)]] 5 µM 2.06× (z +11.3) ⚠ toxic | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.623× (z -11.0) |
| [[NCI-H1792 (line)]] | alt | 315 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -15.9) |
| [[Panc 03.27 (line)]] | alt | 233 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -20.6) |
| [[RKO (line)]] | wt | 277 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.513× (z -15.1) |
| [[SW 900 (line)]] | alt | 287 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.497× (z -14.2) |
| [[SW1417 (line)]] | alt | 225 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.458× (z -18.7) |
| [[A498 (line)]] | wt | 215 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.517× (z -10.3) |
| [[AN3 CA (line)]] | alt | 293 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.361× (z -10.5) |
| [[HS-578T (line)]] | alt | 453 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.595× (z -11.6) |
| [[HT-29 (line)]] | alt | 260 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -22.2) |
| [[SNU-423 (line)]] | alt | 341 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.475× (z -14.8) |
| [[SW 1271 (line)]] | alt | 244 | 0 | 2 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.342× (z -10.1) |
| [[HCT15 (line)]] | alt | 324 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.517× (z -14.1) |
| [[HepG2_C3A (line)]] | wt | 352 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.485× (z -15.3) |
| [[NCI-H2030 (line)]] | alt | 352 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.655× (z -9.5) |
| [[RPMI-7951 (line)]] | alt | 350 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.574× (z -11.9) |
| [[SHP-77 (line)]] | alt | 244 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.615× (z -11.9) |
| [[C32 (line)]] | wt | 226 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 171 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 295 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 297 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 353 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 292 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 421 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1220), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDC42]] | +0.74 | +0.66 / +0.80 | both halves | 7e-06 | pathway: G beta:gamma signalling through CDC42; STRING 782 |
| [[ACTR3]] | +0.67 | +0.62 / +0.75 | both halves | 7e-06 | pathway: Leishmania infection |
| [[CAPZB]] | +0.65 | +0.60 / +0.68 | both halves | 7e-06 | pathway: Sensory Perception |
| [[RSU1]] | +0.63 | +0.68 / +0.44 | both halves | 3e-05 |  |
| [[WDR1]] | +0.61 | +0.35 / +0.71 | both halves | 1e-04 | same gene group; pathway: Platelet activation, signaling and aggregation |
| [[CORO1C]] | +0.60 | +0.61 / +0.58 | both halves | 7e-06 | same gene group |
| [[GATAD2A]] | +0.59 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[ARPC4]] | +0.58 | +0.42 / +0.70 | both halves | 4e-05 | pathway: Leishmania infection |
| [[TPM4]] | +0.58 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[RHOA]] | +0.57 | +0.50 / +0.63 | both halves | 1e-05 | pathway: Beta-catenin independent WNT signaling; STRING 874 |
| [[ARF3]] | +0.57 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[CS]] | +0.56 | +0.51 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WHAMM]] | -0.59 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[HMGCL]] | -0.58 | -0.60 / -0.51 | both halves | 1e-05 |  |
| [[TMEM101]] | -0.58 | -0.38 / -0.49 | both halves | 7e-05 |  |
| [[MBD4]] | -0.57 | -0.49 / -0.64 | both halves | 1e-05 |  |
| [[PEX11A]] | -0.57 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[NKAP]] | -0.57 | -0.53 / -0.61 | both halves | 1e-05 |  |
| [[MRPS18C]] | -0.57 | -0.57 / -0.59 | both halves | 1e-05 |  |
| [[MRPL32]] | -0.56 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[THAP3]] | -0.56 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[CDC37L1]] | -0.55 | -0.53 / -0.56 | both halves | 1e-05 | pathway: Platelet activation, signaling and aggregation |
| [[BET1]] | -0.55 | -0.55 / -0.46 | both halves | 3e-05 |  |
| [[RP9P]] | -0.55 | -0.38 / -0.50 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises GNB1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 111]] — Cell-Cell communication; 43 genes; every member is in the + arm (projection on the module's main direction 0.722). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-36.7, -18.1); signed map (-9.2, 35.3). **Vector** length 108, 38.6% of its response variance represented; |z| ≥ 3 in 1,419 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *RHO GTPase Effectors* (reactome, mean cos +0.54 to 10); *EPHB-mediated forward signaling* (reactome, mean cos +0.58 to 6); *EPH-Ephrin signaling* (reactome, mean cos +0.57 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +10.9 | +6.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +10.6 | +7.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +9.6 | +4.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.1 | -15.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.8 | -14.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.8 | +6.0 |
|  | [[EX229 (drug)]] 5 µM |  | +2.6 | +1.4 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +2.4 | +2.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.4 | +0.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.3 | +3.4 |
| fall | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | -2.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.0 | +0.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.7 | +0.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.7 | -3.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~1% of this change | -3.7 | -3.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.4 | -6.3 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -3.1 | -1.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.0 | -2.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.9 | -3.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.6 | -4.7 |

## What is on record

|  |  |
|---|---|
| Name | G protein subunit beta 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.33 — chr1:1,785,285-1,892,292 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | WD repeat domain containing; G protein subunits beta |
| Reactome | 77 pathways, smallest: Activation of the phototransduction cascade; Olfactory Signaling Pathway; Sensory perception of sweet, bitter, and umami (glutamate) taste |
| Matched by | ensembl_id |

**Function**, from UniProt [P62873](https://www.uniprot.org/uniprotkb/P62873) (Guanine nucleotide-binding protein G(I)/G(S)/G(T) subunit beta-1):

> Beta subunit of the heterotrimeric guanine nucleotide-binding protein (G proteins) that forms complexes with alpha and gamma subunits and participates in signal transduction downstream of G protein-coupled receptors (GPCRs). The beta-gamma dimer stabilizes the GDP-bound inactive alpha subunit by inhibiting spontaneous GDP dissociation. Upon GPCR activation, it facilitates receptor-catalyzed GDP release and GTP binding on the alpha subunit. Following GPCR activation, the released beta-gamma …

**Summary**, from NCBI Gene [2782](https://www.ncbi.nlm.nih.gov/gene/2782):

> Heterotrimeric guanine nucleotide-binding proteins (G proteins), which integrate signals between receptors and effector proteins, are composed of an alpha, a beta, and a gamma subunit. These subunits are encoded by families of related genes. This gene encodes a beta subunit. Beta subunits are important regulators of alpha subunits, as well as of certain signal transduction receptors and effectors. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Sep 2013]

**Accessions** — [HGNC:4396](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4396) · Entrez [2782](https://www.ncbi.nlm.nih.gov/gene/2782) · UniProt [P62873](https://www.uniprot.org/uniprotkb/P62873) · Ensembl [ENSG00000078369](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000078369)

## Data

Gene col 1220: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1220); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1220, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1220]; `tensor/DDL_lfc|DDL_z.npy` [1220]; `embed/gene_vectors.npy` [1220]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1220 or target_col == 1220). Every well: [[GNB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GNB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
