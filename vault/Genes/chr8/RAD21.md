---
symbol: "RAD21"
type: "gene"
col: 9003
ensembl_id: "ENSG00000164754"
name: "RAD21 cohesin complex component"
location: "8q24.11"
module: 22
arm: "+"
pooled_cpm: 310.09
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 17
n_dd_up_clean: 2
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# RAD21

*RAD21 cohesin complex component* — 8q24.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (12 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.75× (z +9.8, q 5e-20, up in 47 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 12 lines (NCI-H1573 5.84×, COLO 205 6.32×, HT-29 4.71×, HEC-1-A 4.00×, …); [[Ouabain (Octahydrate) (drug)]] 5 µM in 6 lines (KATO III 3.04×, LS 180 3.53×, PANC-1 2.63×, NCI-H1573 3.01×, …; ⚠ cell-cycle shift, explains ~50% of this change); [[Homoharringtonine (drug)]] 5 µM in 5 lines (HEC-1-A 2.19×, A498 2.23×, A549 2.31×, PANC-1 1.80×, …; ⚠ cell-cycle shift, would explain all of this change); [[PH-797804 (drug)]] 5 µM in 2 lines (HEC-1-A 4.56×, C32 7.23×); [[TAK-901 (drug)]] 0.05 µM in 1 line (SW48 2.77×).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.468× (z -14.1, q 2e-42, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HMGB2]] (+0.74, fdr 7e-06), [[KIF11]] (+0.69, fdr 7e-06), [[CCNB2]] (+0.68, fdr 7e-06); moves opposite to [[NCLN]] (-0.54, fdr 3e-05), [[PTDSS2]] (-0.51, fdr 5e-05), [[GPSM1]] (-0.51, fdr 3e-05).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 12 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9003.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 12 lines (NCI-H1573 5.84×, COLO 205 6.32×, HT-29 4.71×, HEC-1-A 4.00×, …); [[Ouabain (Octahydrate) (drug)]] 5 µM in 6 lines (KATO III 3.04×, LS 180 3.53×, PANC-1 2.63×, NCI-H1573 3.01×, …; ⚠ cell-cycle shift, explains ~50% of this change); [[Homoharringtonine (drug)]] 5 µM in 5 lines (HEC-1-A 2.19×, A498 2.23×, A549 2.31×, PANC-1 1.80×, …; ⚠ cell-cycle shift, would explain all of this change); [[PH-797804 (drug)]] 5 µM in 2 lines (HEC-1-A 4.56×, C32 7.23×); [[TAK-901 (drug)]] 0.05 µM in 1 line (SW48 2.77×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.75×** | +9.8 | 5e-20 | 47/49 (NCI-H1573, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.63×** | +8.7 | 9e-16 | 43/47 (LoVo, PANC-1, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.57×** | +8.3 | 2e-14 | 42/48 (KATO III, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.90×** | +6.2 | 7e-08 | 40/48 (HEC-1-A, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.26×** | +5.7 | 1e-06 | 26/48 (HEC-1-A, A498, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.33×** | +5.1 | 4e-05 | 28/48 (A498, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | **1.31×** | +5.0 | 4e-05 | 31/48 (NCI-H1573, LS 180, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **1.30×** | +4.9 | 6e-05 | 29/49 (SW480, KATO III, …) | all doses, flat | composition shift |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **1.63×** | +4.7 | 1e-04 | 41/47 (C32, SHP-77, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.29×** | +4.6 | 2e-04 | 32/48 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.26×** | +4.2 | 0.001 | 27/48 (NCI-H460, SW 900, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.24×** | +4.0 | 0.003 | 29/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.22×** | +3.7 | 0.010 | 24/48 (A498, A549, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | **1.20×** | +3.4 | 0.023 | 25/48 (HT-29, HOP62, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9003.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.468×** | -14.1 | 2e-42 | 48/48 (AsPC-1, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.508×** | -12.6 | 6e-34 | 46/48 (AsPC-1, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.610×** | -9.2 | 6e-18 | 45/48 (AsPC-1, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.681×** | -7.2 | 1e-10 | 39/48 (NCI-H2347, HEC-1-A, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.688×** | -7.0 | 4e-10 | 43/48 (SK-MEL-2, SHP-77, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.653×** | -5.7 | 1e-06 | 46/48 (CHP-212, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.750×** | -5.4 | 7e-06 | 37/48 (HepG2/C3A, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Thymol (drug)]] 0.5 µM |  | **0.753×** | -5.2 | 1e-05 | 39/48 (HT-29, KATO III, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.811×** | -4.9 | 6e-05 | 29/49 (CHP-212, A549, …) | rises with dose | position effect removed |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | **0.795×** | -4.1 | 0.002 | 31/49 (NCI-H1792, CFPAC-1, …) | top dose only | plate-row cell shift |
| [[Belzutifan (drug)]] 5 µM |  | **0.678×** | -3.8 | 0.008 | 35/47 (HepG2/C3A, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~96% of this change | **0.810×** | -3.7 | 0.010 | 23/48 (SW480, KATO III, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.689×** | -3.6 | 0.013 | 31/48 (AsPC-1, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.765×** | -3.6 | 0.014 | 33/48 (SW 900, KATO III, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.704×** | -3.4 | 0.023 | 24/48 (SW480, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.864× | -3.4 | 0.023 | 19/48 (LOX-IMVI, HT-29, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.734×** | -3.0 | 0.081 | 25/48 (AsPC-1, HCT15, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.739×** | -2.9 | 0.095 | 23/48 (KATO III, SW480, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.58 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9003. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 190 | 5 (3 ⚠) | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +14.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[PH-797804 (drug)]] 5 µM 4.56× (z +11.5) | [[Panobinostat (drug)]] 0.5 µM 0.428× (z -12.3) |
| [[PANC-1 (line)]] | alt | 257 | 7 (6 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.63× (z +15.8) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.34× (z +10.3) | [[Panobinostat (drug)]] 5 µM 0.446× (z -13.2) |
| [[KATO III (line)]] | alt | 347 | 5 (4 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.04× (z +16.6) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.07× (z +8.7) | [[Panobinostat (drug)]] 5 µM 0.391× (z -14.0) |
| [[NCI-H1573 (line)]] | alt | 240 | 4 (3 ⚠) | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.01× (z +14.7) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.84× (z +12.3) | [[Panobinostat (drug)]] 5 µM 0.462× (z -10.4) |
| [[NCI-H1792 (line)]] | alt | 168 | 6 (6 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.06× (z +11.9) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[NCI-H460 (line)]] | wt | 160 | 5 (5 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.46× (z +11.4) ⚠ cell-cycle shift, explains ~50% of this change | [[Panobinostat (drug)]] 5 µM 0.511× (z -8.5) |
| [[SW480 (line)]] | alt | 275 | 2 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 1.91× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.11× (z +8.8) | [[Panobinostat (drug)]] 5 µM 0.412× (z -13.2) |
| [[A498 (line)]] | wt | 339 | 3 (3 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +13.7) ⚠ cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 5 µM 0.466× (z -10.1) |
| [[AsPC-1 (line)]] | alt | 429 | 2 (1 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.98× (z +9.8) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.20× (z +8.7) | [[Panobinostat (drug)]] 0.5 µM 0.284× (z -18.1) |
| [[C32 (line)]] | wt | 265 | 5 (2 ⚠) | 0 | [[PH-797804 (drug)]] 5 µM 7.23× (z +11.3) | — |
| [[A549 (line)]] | wt | 232 | 2 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +13.6) ⚠ cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 5 µM 0.457× (z -9.9) |
| [[HOP62 (line)]] | alt | 311 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.355× (z -14.0) |
| [[HS-578T (line)]] | alt | 402 | 2 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +12.1) ⚠ cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 5 µM 0.377× (z -13.5) |
| [[HT-29 (line)]] | alt | 844 | 1 | 3 | [[TAK-901 (drug)]] 5 µM 4.71× (z +11.8) | [[Panobinostat (drug)]] 5 µM 0.396× (z -13.4) |
| [[LoVo (line)]] | wt | 194 | 3 (3 ⚠) | 1 | [[Niclosamide (olamine) (drug)]] 5 µM 3.02× (z +14.7) ⚠ toxic | [[Panobinostat (drug)]] 5 µM 0.497× (z -9.5) |
| [[LOX-IMVI (line)]] | wt | 474 | 2 (1 ⚠) | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.33× (z +11.0) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.70× (z +8.9) | [[Panobinostat (drug)]] 5 µM 0.341× (z -13.9) |
| [[LS 180 (line)]] | wt | 275 | 3 (3 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.53× (z +16.1) ⚠ cell-cycle shift, explains ~50% of this change | [[Panobinostat (drug)]] 5 µM 0.485× (z -9.2) |
| [[NCI-H2347 (line)]] | alt | 607 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.455× (z -11.0) |
| [[Panc 03.27 (line)]] | alt | 355 | 1 | 3 | [[TAK-901 (drug)]] 5 µM 3.28× (z +9.7) | [[Panobinostat (drug)]] 5 µM 0.392× (z -14.5) |
| [[SHP-77 (line)]] | alt | 393 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.435× (z -12.7) |
| [[SW 900 (line)]] | alt | 342 | 1 (1 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.05× (z +9.7) ⚠ cell-cycle shift, explains ~50% of this change | [[Panobinostat (drug)]] 5 µM 0.427× (z -11.6) |
| [[COLO 205 (line)]] | alt | 225 | 3 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.32× (z +11.9) | — |
| [[HepG2_C3A (line)]] | wt | 228 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.318× (z -13.8) |
| [[Hs 766T (line)]] | wt | 249 | 1 (1 ⚠) | 2 | [[Niclosamide (olamine) (drug)]] 5 µM 2.27× (z +10.3) ⚠ toxic | [[Panobinostat (drug)]] 5 µM 0.415× (z -11.6) |
| [[RPMI-7951 (line)]] | alt | 316 | 1 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +8.7) ⚠ cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 0.5 µM 0.441× (z -9.6) |
| [[SK-MEL-2 (line)]] | alt | 239 | 1 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +9.1) ⚠ cell-cycle shift, would explain all of this change | [[Auranofin (drug)]] 5 µM 0.451× (z -11.0) |
| [[SNU-423 (line)]] | alt | 195 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.421× (z -10.7) |
| [[A-172 (line)]] | wt | 212 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.428× (z -11.2) |
| [[CFPAC-1 (line)]] | alt | 231 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.451× (z -10.5) |
| [[J82 (line)]] | alt | 376 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.425× (z -12.1) |
| [[SW1417 (line)]] | alt | 466 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.495× (z -10.2) |
| [[SW48 (line)]] | wt | 282 | 2 | 0 | [[TAK-901 (drug)]] 0.05 µM 2.77× (z +10.1) | — |
| [[CHP-212 (line)]] | wt | 263 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -8.7) ⚠ cell-cycle shift, explains ~28% of this change |
| [[HCT15 (line)]] | alt | 350 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.433× (z -10.0) |
| [[hTERT-HPNE (line)]] | wt | 235 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.470× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 247 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.96× (z +9.9) | — |
| [[RKO (line)]] | wt | 549 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.61× (z +9.3) | — |
| [[A-427 (line)]] | wt | 234 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 371 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 344 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 260 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 208 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 197 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 395 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 245 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 261 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 485 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 268 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 223 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9003), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HMGB2]] | +0.74 | +0.70 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[KIF11]] | +0.69 | +0.67 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[CCNB2]] | +0.68 | +0.62 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 811 |
| [[HP1BP3]] | +0.67 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[TOP2B]] | +0.67 | +0.63 / +0.68 | both halves | 7e-06 | pathway: SUMO E3 ligases SUMOylate target proteins; STRING 620 |
| [[TPX2]] | +0.66 | +0.63 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[HMMR]] | +0.66 | +0.55 / +0.66 | both halves | 1e-05 | pathway: HALLMARK_E2F_TARGETS |
| [[NEK2]] | +0.66 | +0.63 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 433 |
| [[STMN1]] | +0.65 | +0.54 / +0.69 | both halves | 1e-05 | same gene group; pathway: HALLMARK_E2F_TARGETS |
| [[DEPDC1]] | +0.64 | +0.53 / +0.67 | both halves | 1e-05 | pathway: HALLMARK_E2F_TARGETS |
| [[CCNA2]] | +0.64 | +0.62 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 400 |
| [[KIF20A]] | +0.64 | +0.61 / +0.68 | both halves | 7e-06 | pathway: Mitotic Telophase/Cytokinesis |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCLN]] | -0.54 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[PTDSS2]] | -0.51 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[GPSM1]] | -0.51 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[GPR89B]] | -0.51 | -0.39 / -0.54 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.632). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-40.4, -54.5); signed map (-51.1, -45.7). **Vector** length 133, 56.3% of its response variance represented; |z| ≥ 3 in 1,315 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DREAM G2/M down* (control, mean cos +0.56 to 28); *mitotic spindle* (hallmark, mean cos +0.54 to 38); *G2/M Transition* (reactome, mean cos +0.51 to 28).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.5 | +5.7 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | +5.3 | +3.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.2 | -0.4 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | +4.7 | +4.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.2 | +8.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | -3.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.8 | -0.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.8 | +0.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.6 | +0.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -11.3 | -7.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -10.3 | -7.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~96% of this change | -7.4 | -3.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -7.2 | -0.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -6.6 | -2.2 |
|  | [[EX229 (drug)]] 5 µM |  | -6.4 | -3.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -6.1 | -3.6 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -5.8 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | RAD21 cohesin complex component |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.11 — chr8:116,845,934-116,874,776 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0078, hHR21, SCC1 |
| Gene groups (HGNC) | Cohesin complex; Kleisins; MicroRNA protein coding host genes |
| Hallmark sets | G2M_CHECKPOINT, E2F_TARGETS |
| Reactome | 21 pathways, smallest: Cohesin Loading onto Chromatin; Establishment of Sister Chromatid Cohesion; Mitotic Telophase/Cytokinesis |
| Matched by | ensembl_id |

**Function**, from UniProt [O60216](https://www.uniprot.org/uniprotkb/O60216) (Double-strand-break repair protein rad21 homolog):

> [Double-strand-break repair protein rad21 homolog]: As a member of the cohesin complex, involved in sister chromatid cohesion from the time of DNA replication in S phase to their segregation in mitosis, a function that is essential for proper chromosome segregation, post-replicative DNA repair, and the prevention of inappropriate recombination between repetitive regions. The cohesin complex may also play a role in spindle pole assembly during mitosis. In interphase, cohesins may function in the …

**Summary**, from NCBI Gene [5885](https://www.ncbi.nlm.nih.gov/gene/5885):

> The protein encoded by this gene is highly similar to the gene product of Schizosaccharomyces pombe rad21, a gene involved in the repair of DNA double-strand breaks, as well as in chromatid cohesion during mitosis. This protein is a nuclear phospho-protein, which becomes hyperphosphorylated in cell cycle M phase. The highly regulated association of this protein with mitotic chromatin specifically at the centromere region suggests its role in sister chromatid cohesion in mitotic cells. [provided …

**Accessions** — [HGNC:9811](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9811) · Entrez [5885](https://www.ncbi.nlm.nih.gov/gene/5885) · UniProt [O60216](https://www.uniprot.org/uniprotkb/O60216) · Ensembl [ENSG00000164754](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164754)

## Data

Gene col 9003: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9003); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9003, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9003]; `tensor/DDL_lfc|DDL_z.npy` [9003]; `embed/gene_vectors.npy` [9003]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9003 or target_col == 9003). Every well: [[RAD21 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAD21.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
