---
symbol: "QKI"
type: "gene"
col: 3376
ensembl_id: "ENSG00000112531"
name: "QKI, KH domain containing RNA binding"
location: "6q26"
module: 14
arm: "+"
pooled_cpm: 243.59
n_lines_expressing: 43
n_dd_up: 14
n_dd_down: 11
n_dd_up_clean: 12
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# QKI

*QKI, KH domain containing RNA binding* — 6q26

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.03× (z +18.1, q 0e+00, up in 34 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.368× (z -18.2, q 0e+00, down in 41 of 41 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DYRK1A]] (+0.67, fdr 7e-06), [[WAC]] (+0.63, fdr 7e-06), [[CPNE8]] (+0.60, fdr 1e-05); moves opposite to [[SIN3B]] (-0.60, fdr 3e-05), [[ERCC3]] (-0.58, fdr 1e-05), [[VRK3]] (-0.55, fdr 5e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3376.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.03×** | +18.1 | 0e+00 | 34/41 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.37×** | +15.6 | 0e+00 | 40/41 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **5.13×** | +15.5 | 0e+00 | 42/42 (PANC-1, CFPAC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.29×** | +14.5 | 1e-45 | 38/40 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.19×** | +14.2 | 7e-44 | 40/41 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.98×** | +12.5 | 1e-33 | 38/41 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.77×** | +10.4 | 2e-23 | 38/41 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.78×** | +10.1 | 5e-22 | 37/41 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.34×** | +8.1 | 4e-14 | 35/41 (C32, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.51×** | +6.9 | 3e-10 | 31/41 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.35×** | +5.1 | 2e-05 | 25/40 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.27×** | +4.3 | 7e-04 | 21/41 (A-427, C-33 A, …) | rises with dose |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.25×** | +3.9 | 0.005 | 22/42 (NCI-H460, SNU-423, …) | top dose only | plate-row cell shift |
| [[Tomivosertib (drug)]] 5 µM |  | **1.42×** | +3.3 | 0.039 | 24/41 (NCI-H2030, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 1.19× | +3.0 | 0.10 | 15/41 (HOP62, NCI-H460, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3376.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.368×** | -18.2 | 0e+00 | 41/41 (A549, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.382×** | -17.5 | 0e+00 | 41/41 (A549, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.552×** | -10.8 | 5e-25 | 39/41 (A549, Hs 766T, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.616×** | -8.5 | 3e-15 | 38/40 (NCI-H2347, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.671×** | -7.0 | 3e-10 | 28/39 (A-427, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.699×** | -6.5 | 6e-09 | 30/42 (NCI-H2347, SNU-1, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.714×** | -6.1 | 7e-08 | 32/41 (NCI-H2347, LOX-IMVI, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.797×** | -4.1 | 0.002 | 26/41 (SW1417, CFPAC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.821×** | -3.6 | 0.020 | 21/41 (CFPAC-1, NCI-H1792, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.826×** | -3.5 | 0.027 | 20/41 (A549, A-172, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.875× | -3.5 | 0.027 | 12/41 (AN3 CA, A549, …) | top dose only |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 0.838× | -3.2 | 0.052 | 20/41 (NCI-H1792, HOP62, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.827×** | -3.2 | 0.052 | 20/41 (A549, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.843× | -3.1 | 0.070 | 17/42 (CFPAC-1, NCI-H2347, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.844× | -3.1 | 0.071 | 18/41 (CFPAC-1, A549, …) | rises with dose |  |
| [[Apalutamide (drug)]] 0.5 µM |  | 0.847× | -3.0 | 0.076 | 18/41 (A498, LOX-IMVI, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 0.848× | -3.0 | 0.079 | 15/41 (HEC-1-A, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3376. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 198 | 12 (3 ⚠) | 2 | [[Digitoxin (drug)]] 0.5 µM 8.43× (z +30.6) | [[Panobinostat (drug)]] 0.5 µM 0.368× (z -14.4) |
| [[PANC-1 (line)]] | alt | 334 | 11 (4 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.02× (z +24.4) | [[Panobinostat (drug)]] 5 µM 0.411× (z -15.6) |
| [[A-427 (line)]] | wt | 246 | 8 (3 ⚠) | 5 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 3.22× (z +16.7) | [[Dinaciclib (drug)]] 5 µM 0.227× (z -21.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.306× (z -17.6) |
| [[HOP62 (line)]] | alt | 310 | 9 (2 ⚠) | 3 | [[TAK-901 (drug)]] 5 µM 11.7× (z +15.8) | [[Panobinostat (drug)]] 0.5 µM 0.287× (z -15.4) |
| [[Hs 766T (line)]] | wt | 353 | 8 (3 ⚠) | 3 | [[Niclosamide (olamine) (drug)]] 5 µM 3.84× (z +15.6) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.48× (z +15.4) | [[Panobinostat (drug)]] 5 µM 0.209× (z -18.9) |
| [[A549 (line)]] | wt | 328 | 5 (2 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +19.3) | [[Panobinostat (drug)]] 0.5 µM 0.155× (z -25.0) |
| [[AN3 CA (line)]] | alt | 832 | 0 | 10 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.341× (z -12.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.223× (z -12.4) |
| [[AsPC-1 (line)]] | alt | 369 | 5 (2 ⚠) | 5 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 8.22× (z +14.8) | [[Panobinostat (drug)]] 0.5 µM 0.239× (z -19.2) |
| [[C32 (line)]] | wt | 293 | 8 (2 ⚠) | 2 | [[Harringtonine (drug)]] 5 µM 6.33× (z +21.7) | [[Panobinostat (drug)]] 0.5 µM 0.458× (z -9.6) |
| [[NCI-H1792 (line)]] | alt | 275 | 8 (2 ⚠) | 2 | [[Digitoxin (drug)]] 5 µM 3.43× (z +15.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.87× (z +13.0) | [[Panobinostat (drug)]] 0.5 µM 0.432× (z -10.4) |
| [[NCI-H2347 (line)]] | alt | 346 | 4 | 6 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 11.1× (z +16.6) | [[Dinaciclib (drug)]] 5 µM 0.314× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.368× (z -13.2) |
| [[SW 900 (line)]] | alt | 286 | 8 (2 ⚠) | 2 | [[Digitoxin (drug)]] 5 µM 3.74× (z +13.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.50× (z +12.9) | [[Panobinostat (drug)]] 0.5 µM 0.272× (z -13.4) |
| [[H4 (line)]] | wt | 229 | 7 (1 ⚠) | 2 | [[Digitoxin (drug)]] 0.5 µM 3.03× (z +11.7) | [[Panobinostat (drug)]] 5 µM 0.353× (z -11.0) |
| [[HEC-1-A (line)]] | alt | 229 | 5 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +17.7) | [[Panobinostat (drug)]] 0.5 µM 0.382× (z -12.5) |
| [[J82 (line)]] | alt | 281 | 7 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +15.3) | [[Panobinostat (drug)]] 0.5 µM 0.343× (z -13.4) |
| [[LoVo (line)]] | wt | 112 | 7 (3 ⚠) | 2 | [[Niclosamide (olamine) (drug)]] 5 µM 3.92× (z +16.8) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.05× (z +14.3) | [[Panobinostat (drug)]] 5 µM 0.377× (z -12.5) |
| [[NCI-H23 (line)]] | alt | 203 | 6 (2 ⚠) | 3 | [[Digitoxin (drug)]] 5 µM 2.43× (z +13.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.17× (z +12.0) | [[Panobinostat (drug)]] 5 µM 0.321× (z -17.7) |
| [[SNU-423 (line)]] | alt | 563 | 7 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +16.0) | [[Panobinostat (drug)]] 5 µM 0.368× (z -13.0) |
| [[BT-474 (line)]] | alt | 109 | 5 | 3 | [[TAK-901 (drug)]] 5 µM 10.2× (z +12.8) | [[Panobinostat (drug)]] 5 µM 0.294× (z -12.9) |
| [[CFPAC-1 (line)]] | alt | 320 | 3 (1 ⚠) | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +18.8) | [[Panobinostat (drug)]] 0.5 µM 0.306× (z -14.6) |
| [[A498 (line)]] | wt | 274 | 5 (3 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +19.3) | [[Panobinostat (drug)]] 0.5 µM 0.387× (z -10.3) |
| [[C-33 A (line)]] | alt | 376 | 4 (1 ⚠) | 3 | [[Digitoxin (drug)]] 0.5 µM 2.42× (z +10.5) | [[Panobinostat (drug)]] 5 µM 0.286× (z -14.8) |
| [[HepG2_C3A (line)]] | wt | 390 | 4 (1 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.40× (z +13.0) | [[Panobinostat (drug)]] 0.5 µM 0.282× (z -13.5) |
| [[MIA PaCa-2 (line)]] | alt | 332 | 4 (1 ⚠) | 3 | [[Niclosamide (olamine) (drug)]] 5 µM 2.93× (z +13.3) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 2.69× (z +12.3) | [[Panobinostat (drug)]] 5 µM 0.207× (z -20.2) |
| [[Panc 03.27 (line)]] | alt | 157 | 5 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +16.8) | [[Panobinostat (drug)]] 5 µM 0.354× (z -12.0) |
| [[RPMI-7951 (line)]] | alt | 405 | 5 (2 ⚠) | 2 | [[Harringtonine (drug)]] 5 µM 3.15× (z +14.0) | [[Panobinostat (drug)]] 0.5 µM 0.351× (z -13.3) |
| [[hTERT-HPNE (line)]] | wt | 252 | 4 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +18.1) | [[Panobinostat (drug)]] 0.5 µM 0.386× (z -10.0) |
| [[NCI-H1573 (line)]] | alt | 184 | 4 (2 ⚠) | 2 | [[TAK-901 (drug)]] 5 µM 11.8× (z +15.3) | [[Panobinostat (drug)]] 0.5 µM 0.398× (z -11.0) |
| [[SK-MEL-2 (line)]] | alt | 361 | 3 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +15.7) | [[Panobinostat (drug)]] 0.5 µM 0.320× (z -15.3) |
| [[A-172 (line)]] | wt | 191 | 3 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +14.9) | [[Panobinostat (drug)]] 5 µM 0.376× (z -12.6) |
| [[SNU-1 (line)]] | wt | 547 | 3 | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.84× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.215× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.301× (z -10.7) |
| [[HS-578T (line)]] | alt | 357 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +10.9) | — |
| [[LOX-IMVI (line)]] | wt | 432 | 1 | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.46× (z +10.2) | [[Panobinostat (drug)]] 0.5 µM 0.291× (z -14.1) |
| [[SW1417 (line)]] | alt | 103 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +12.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.579× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 138 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.92× (z +10.2) | — |
| [[NCI-H2030 (line)]] | alt | 315 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 5.37× (z +10.4) | — |
| [[CHP-212 (line)]] | wt | 279 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.6 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 75.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.8 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 17.4 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 17.0 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 240 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 255 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 335 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 18.8 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 365 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 295 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 22.8 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 64.9 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3376), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DYRK1A]] | +0.67 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[WAC]] | +0.63 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[CPNE8]] | +0.60 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[LHFPL6]] | +0.56 | +0.50 / +0.43 | both halves | 3e-05 |  |
| [[UVRAG]] | +0.55 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[SIAH1]] | +0.55 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[KDM6A]] | +0.55 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[UPK2]] | +0.55 | +0.36 / +0.40 | both halves | 9e-05 |  |
| [[TBL1XR1]] | +0.54 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[CHASERR]] | +0.54 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[ZBED5-AS1]] | +0.54 | +0.29 / +0.51 | both halves | 3e-04 |  |
| [[ZBTB10]] | +0.54 | +0.54 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SIN3B]] | -0.60 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[ERCC3]] | -0.58 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[VRK3]] | -0.55 | -0.39 / -0.50 | both halves | 5e-05 |  |
| [[SLC30A6]] | -0.54 | -0.45 / -0.61 | both halves | 3e-05 |  |
| [[ZNF229]] | -0.54 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[NUP214]] | -0.53 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[ASCC2]] | -0.53 | -0.36 / -0.48 | both halves | 1e-04 |  |
| [[MIER2]] | -0.53 | -0.32 / -0.56 | both halves | 2e-04 |  |
| [[ZNF473]] | -0.51 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[SDHAF2]] | -0.51 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[HERC2P3]] | -0.51 | -0.31 / -0.44 | both halves | 2e-04 |  |
| [[UBE4A]] | -0.51 | -0.42 / -0.47 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises QKI's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.491). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-1.4, -25.2); signed map (43.6, -0.4). **Vector** length 106, 39.4% of its response variance represented; |z| ≥ 3 in 1,357 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.4 | +1.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +5.7 | +14.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.7 | +0.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.5 | +0.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.9 | -1.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.8 | +1.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.8 | +0.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.8 | -0.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.8 | +0.5 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -7.5 | +0.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -7.0 | -2.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.6 | +0.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.2 | -17.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -3.7 | -8.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.1 | -0.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | -2.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.0 | -1.1 |
|  | [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | -1.9 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | QKI, KH domain containing RNA binding |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q26 — chr6:163,414,000-163,578,592 (+) |
| Ensembl biotype | protein_coding |
| Also known as | QK3 |
| Reactome | 3 pathways, smallest: Signaling by BRAF and RAF1 fusions; Oncogenic MAPK signaling; Diseases of signal transduction by growth factor receptors and second messengers |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96PU8](https://www.uniprot.org/uniprotkb/Q96PU8) (KH domain-containing RNA-binding protein QKI):

> RNA reader protein, which recognizes and binds specific RNAs, thereby regulating RNA metabolic processes, such as pre-mRNA splicing, circular RNA (circRNA) formation, mRNA export, mRNA stability and/or translation. Involved in various cellular processes, such as mRNA storage into stress granules, apoptosis, lipid deposition, interferon response, glial cell fate and development. Binds to the 5'-NACUAAY-N(1,20)-UAAY-3' RNA core sequence. Acts as a mRNA modification reader that specifically …

**Summary**, from NCBI Gene [9444](https://www.ncbi.nlm.nih.gov/gene/9444):

> The protein encoded by this gene is an RNA-binding protein that regulates pre-mRNA splicing, export of mRNAs from the nucleus, protein translation, and mRNA stability. The encoded protein is involved in myelinization and oligodendrocyte differentiation and may play a role in schizophrenia. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2014]

**Accessions** — [HGNC:21100](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21100) · Entrez [9444](https://www.ncbi.nlm.nih.gov/gene/9444) · UniProt [Q96PU8](https://www.uniprot.org/uniprotkb/Q96PU8) · Ensembl [ENSG00000112531](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112531)

## Data

Gene col 3376: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3376); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3376, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3376]; `tensor/DDL_lfc|DDL_z.npy` [3376]; `embed/gene_vectors.npy` [3376]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3376 or target_col == 3376). Every well: [[QKI — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/QKI.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
