---
symbol: "RAP1B"
type: "gene"
col: 4798
ensembl_id: "ENSG00000127314"
name: "RAP1B, member of RAS oncogene family"
location: "12q15"
module: 101
arm: "+"
pooled_cpm: 315.41
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 8
n_dd_up_clean: 8
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/101"]
generated_by: "tahoemap"
---

# RAP1B

*RAP1B, member of RAS oncogene family* — 12q15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.69× (z +16.6, q 0e+00, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.658× (z -13.3, q 2e-37, down in 36 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 15 lines (NCI-H1792 0.355×, A549 0.437×, PANC-1 0.391×, Hs 766T 0.441×, …); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A549 0.362×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (HT-29 0.387×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DLGAP4]] (+0.67, fdr 8e-06), [[S100A2]] (+0.61, fdr 1e-05), [[MAST4]] (+0.59, fdr 1e-05); moves opposite to [[CIPC]] (-0.58, fdr 3e-05), [[DFFB]] (-0.53, fdr 1e-04), [[NAXD]] (-0.53, fdr 5e-05).
> It is in [[Module 101]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[C11orf91]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4798.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.69×** | +16.6 | 0e+00 | 38/48 (AsPC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.68×** | +11.6 | 1e-28 | 46/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.64×** | +11.0 | 6e-26 | 43/48 (NCI-H460, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.51×** | +9.2 | 6e-18 | 36/48 (MIA PaCa-2, A498, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.09×** | +8.6 | 1e-15 | 42/49 (RKO, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.49×** | +8.5 | 2e-15 | 35/48 (hTERT-HPNE, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.43×** | +7.9 | 2e-13 | 43/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.41×** | +7.6 | 1e-12 | 40/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.70×** | +6.2 | 4e-08 | 37/48 (SW480, A549, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.29×** | +5.4 | 4e-06 | 27/47 (LoVo, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.28×** | +5.4 | 4e-06 | 31/48 (CFPAC-1, LS 180, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.16× | +4.8 | 9e-05 | 18/49 (CFPAC-1, SK-MEL-2, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **1.22×** | +4.2 | 0.001 | 24/47 (RPMI-7951, H4, …) | rises with dose |  |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 1.19× | +3.7 | 0.009 | 17/48 (NCI-H23, HS-578T, …) | top dose only | plate-row cell shift |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.17× | +3.5 | 0.016 | 20/47 (RKO, RPMI-7951, …) | rises with dose | low cells (technical?) |
| [[Peretinoin (drug)]] 5 µM |  | 1.18× | +3.4 | 0.020 | 19/47 (CFPAC-1, HT-29, …) | rises with dose |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.17× | +3.4 | 0.020 | 18/49 (AsPC-1, NCI-H23, …) | top dose only | plate-row cell shift |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.16× | +3.4 | 0.022 | 18/48 (SK-MEL-2, CFPAC-1, …) | rises with dose |  |
| [[Almonertinib (mesylate) (drug)]] 5 µM |  | 1.15× | +3.0 | 0.077 | 9/49 (A549, HOP62, …) | rises with dose | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4798.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 15 lines (NCI-H1792 0.355×, A549 0.437×, PANC-1 0.391×, Hs 766T 0.441×, …); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A549 0.362×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (HT-29 0.387×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.658×** | -13.3 | 2e-37 | 36/49 (NCI-H1792, A549, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.675×** | -8.5 | 6e-15 | 32/44 (HT-29, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.720×** | -7.4 | 3e-11 | 29/49 (LoVo, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.704×** | -7.3 | 5e-11 | 30/45 (A549, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.786×** | -5.4 | 7e-06 | 30/48 (HT-29, NCI-H1792, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.811×** | -4.7 | 2e-04 | 25/48 (AsPC-1, A549, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~46% of this change | **0.819×** | -4.3 | 0.001 | 23/47 (RKO, C-33 A, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.830×** | -4.2 | 0.002 | 24/48 (LoVo, NCI-H1792, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.838× | -4.0 | 0.004 | 22/48 (KATO III, NCI-H1573, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.887× | -3.8 | 0.007 | 3/48 (Panc 03.27, LS 180, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.852× | -3.5 | 0.025 | 17/48 (RKO, Hs 766T, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | 0.858× | -3.5 | 0.025 | 17/48 (AsPC-1, A549, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.858× | -3.4 | 0.025 | 20/48 (HS-578T, NCI-H1792, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | 0.904× | -3.2 | 0.048 | 15/48 (COLO 205, RKO, …) | top dose only | low cells (technical?) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.870× | -3.2 | 0.060 | 15/47 (RKO, Hs 766T, …) | all doses, flat |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.866× | -3.1 | 0.060 | 19/48 (RKO, NCI-H2347, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.873× | -3.1 | 0.069 | 12/49 (PANC-1, J82, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4798. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 289 | 12 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +18.8) | — |
| [[HT-29 (line)]] | alt | 258 | 7 (3 ⚠) | 2 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.54× (z +13.7) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.49× (z +13.4) | [[Dinaciclib (drug)]] 5 µM 0.387× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.566× (z -11.9) |
| [[A549 (line)]] | wt | 416 | 3 (1 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +13.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.437× (z -18.3) |
| [[AsPC-1 (line)]] | alt | 477 | 4 (1 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +21.3) | [[Dinaciclib (drug)]] 5 µM 0.458× (z -11.6) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 429 | 5 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +17.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.504× (z -9.6) ⚠ toxic; cell-cycle shift, explains ~46% of this change |
| [[SW480 (line)]] | alt | 170 | 7 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.58× (z +14.5) | — |
| [[KATO III (line)]] | alt | 178 | 5 (3 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.78× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 1.75× (z +8.7) | [[Dinaciclib (drug)]] 0.05 µM 0.552× (z -8.5) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 560 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -14.5) |
| [[hTERT-HPNE (line)]] | wt | 347 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +19.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.607× (z -10.2) |
| [[A-172 (line)]] | wt | 306 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +15.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.535× (z -14.5) |
| [[A498 (line)]] | wt | 395 | 3 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +17.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.504× (z -13.7) |
| [[COLO 205 (line)]] | alt | 212 | 3 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.36× (z +9.4) | [[Selinexor (drug)]] 5 µM 0.560× (z -9.1) ⚠ cell-cycle shift, explains ~46% of this change |
| [[LoVo (line)]] | wt | 573 | 1 (1 ⚠) | 3 (2 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.29× (z +10.9) ⚠ toxic | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.534× (z -12.2) |
| [[MIA PaCa-2 (line)]] | alt | 157 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +18.7) | — |
| [[RPMI-7951 (line)]] | alt | 221 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +17.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.552× (z -12.4) |
| [[SNU-1 (line)]] | wt | 173 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +11.9) | — |
| [[CFPAC-1 (line)]] | alt | 342 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +20.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.501× (z -14.8) |
| [[HEC-1-A (line)]] | alt | 256 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.51× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.512× (z -15.6) |
| [[HepG2_C3A (line)]] | wt | 211 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.36× (z +11.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.05× (z +9.4) | — |
| [[Hs 766T (line)]] | wt | 420 | 2 (1 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 2.12× (z +10.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.92× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.441× (z -16.4) |
| [[HS-578T (line)]] | alt | 318 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +14.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.578× (z -10.1) |
| [[LOX-IMVI (line)]] | wt | 346 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.20× (z +11.1) | — |
| [[NCI-H1573 (line)]] | alt | 358 | 2 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 3.06× (z +9.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.87× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.301× (z -10.2) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 315 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +13.8) | — |
| [[PANC-1 (line)]] | alt | 462 | 2 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.30× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.391× (z -16.7) |
| [[SW1417 (line)]] | alt | 183 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +13.1) | — |
| [[A-427 (line)]] | wt | 274 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +12.9) | — |
| [[C32 (line)]] | wt | 222 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +13.8) | — |
| [[HOP62 (line)]] | alt | 380 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.526× (z -11.1) |
| [[LS 180 (line)]] | wt | 373 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.353× (z -9.8) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 280 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +14.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.533× (z -12.0) |
| [[SW 900 (line)]] | alt | 308 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +11.7) | — |
| [[SW48 (line)]] | wt | 230 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +11.3) | [[Dinaciclib (drug)]] 0.5 µM 0.355× (z -8.6) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 191 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +10.7) | — |
| [[CHP-212 (line)]] | wt | 286 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.398× (z -11.6) |
| [[J82 (line)]] | alt | 396 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.559× (z -14.3) |
| [[NCI-H1792 (line)]] | alt | 719 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -20.5) |
| [[NCI-H2030 (line)]] | alt | 168 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +10.2) | — |
| [[NCI-H2347 (line)]] | alt | 260 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.554× (z -8.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 182 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +12.3) | — |
| [[BT-474 (line)]] | alt | 185 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 253 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 207 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 344 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 329 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 217 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 275 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 251 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4798), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DLGAP4]] | +0.67 | +0.57 / +0.68 | both halves | 8e-06 |  |
| [[S100A2]] | +0.61 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[MAST4]] | +0.59 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[LUZP1]] | +0.56 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[CTTNBP2NL]] | +0.56 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[PDLIM7]] | +0.56 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[LAMB3]] | +0.56 | +0.50 / +0.54 | both halves | 1e-05 | pathway: MET promotes cell motility |
| [[IER3]] | +0.54 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[ZSWIM4]] | +0.54 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[STK10]] | +0.54 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[COL5A3]] | +0.54 | +0.40 / +0.50 | both halves | 5e-05 | pathway: MET promotes cell motility |
| [[HBEGF]] | +0.54 | +0.51 / +0.50 | both halves | 1e-05 | pathway: MAPK family signaling cascades |

## Genes that move opposite

*24 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CIPC]] | -0.58 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[DFFB]] | -0.53 | -0.35 / -0.63 | both halves | 1e-04 |  |
| [[NAXD]] | -0.53 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[LARP1]] | -0.53 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[TRRAP]] | -0.52 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[RAVER2]] | -0.52 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[TCEANC2]] | -0.51 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[TSN]] | -0.51 | -0.34 / -0.43 | both halves | 1e-04 |  |
| [[SEPHS1]] | -0.51 | -0.46 / -0.38 | both halves | 7e-05 |  |
| [[USP5]] | -0.51 | -0.44 / -0.36 | both halves | 9e-05 |  |
| [[GTF2I]] | -0.51 | -0.43 / -0.37 | both halves | 8e-05 |  |
| [[KAT7]] | -0.50 | -0.40 / -0.42 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C11orf91]] | B | C11orf91 activity raises RAP1B's level | lines that do not express C11orf91 (8) vs lines expressing it (42) | 1.31× lower at baseline in the lines without C11orf91 | 0.025 | ⚠ within organs, on part of the lines; also absent: CD59, ENSG00000284969, ENSG00000255202 |
| [[LAMB3]] | B | LAMB3 activity raises RAP1B's level | lines that do not express LAMB3 (22) vs lines expressing it (28) | 1.27× lower at baseline in the lines without LAMB3 | 0.031 | ⚠ within organs, on part of the lines; also absent: KCNK1, LAMC2, PRSS3 |
| [[FAM107B]] | B | FAM107B activity raises RAP1B's level | lines that do not express FAM107B (11) vs lines expressing it (39) | 1.45× lower at baseline in the lines without FAM107B | 0.037 | ⚠ within organs, on part of the lines; also absent: KIAA1217, ETS2, NRP1 |
| [[KLF7]] | B | KLF7 activity raises RAP1B's level | lines that do not express KLF7 (12) vs lines expressing it (38) | 1.42× lower at baseline in the lines without KLF7 | 0.046 | ⚠ within organs, on part of the lines; also absent: MYOSLID, CTSF, MPDZ |
| [[F3]] | B | F3 activity raises RAP1B's level | lines that do not express F3 (24) vs lines expressing it (26) | 1.31× lower at baseline in the lines without F3 | 0.048 | ⚠ within organs, on part of the lines; also absent: TLR2, KRT7, EDNRA |
| [[DUSP5-DT]] | B | DUSP5-DT activity raises RAP1B's level | lines that do not express DUSP5-DT (7) vs lines expressing it (43) | 1.49× lower at baseline in the lines without DUSP5-DT | 0.055 | ⚠ within organs, on part of the lines; also absent: PRR5L, MAMLD1; maybe low, not absent |
| [[F3]] | B | F3 activity strengthens RAP1B's drug response | lines that do not express F3 (24) vs lines expressing it (25) | the lines without F3 respond 0.95× as strongly (z diff -0.07); strongest at Dinaciclib 5 µM: 0.78x vs 0.57x (z diff +3.6) | 0.098 | ⚠ within organs, on part of the lines; also absent: TLR2, KRT7, EDNRA; target measured in part of the lines; both ways; artifact flags |
| [[HRH1]] | B | HRH1 activity raises RAP1B's level | lines that do not express HRH1 (10) vs lines expressing it (40) | 1.30× lower at baseline in the lines without HRH1 | 0.099 | ⚠ within organs, on part of the lines; also absent: PHLDA2, PLAUR, LRRK1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 101]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.597). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (34.6, 4.1); signed map (1.2, 30.4). **Vector** length 95.6, 31.7% of its response variance represented; |z| ≥ 3 in 1,506 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.5 | +1.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.3 | +16.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.3 | -0.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.7 | -7.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | +4.2 | -3.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.7 | +3.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.1 | +4.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.9 | +3.4 |
|  | [[vincristine (drug)]] 0.5 µM |  | +2.8 | +2.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.3 | -2.2 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -4.1 | -2.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.6 | -4.2 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -3.2 | -1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.2 | -2.5 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.9 | -0.5 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.7 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | RAP1B, member of RAS oncogene family |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q15 — chr12:68,610,855-68,671,901 (+) |
| Ensembl biotype | protein_coding |
| Also known as | K-REV, RAL1B, DKFZp586H0723 |
| Gene groups (HGNC) | RAS type GTPase family |
| Reactome | 32 pathways, smallest: MET activates RAP1 and RAC1; GRB2:SOS provides linkage to MAPK signaling for Integrins; Rap1 signalling |
| Matched by | ensembl_id |

**Function**, from UniProt [P61224](https://www.uniprot.org/uniprotkb/P61224) (Ras-related protein Rap-1b):

> GTP-binding protein that possesses intrinsic GTPase activity. Contributes to the polarizing activity of KRIT1 and CDH5 in the establishment and maintenance of correct endothelial cell polarity and vascular lumen. Required for the localization of phosphorylated PRKCZ, PARD3 and TIAM1 to the cell junction. Plays a role in the establishment of basal endothelial barrier function.

**Summary**, from NCBI Gene [5908](https://www.ncbi.nlm.nih.gov/gene/5908):

> This gene encodes a member of the RAS-like small GTP-binding protein superfamily. Members of this family regulate multiple cellular processes including cell adhesion and growth and differentiation. This protein localizes to cellular membranes and has been shown to regulate integrin-mediated cell signaling. This protein also plays a role in regulating outside-in signaling in platelets. Alternate splicing results in multiple transcript variants. Pseudogenes of this gene are found on chromosomes …

**Accessions** — [HGNC:9857](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9857) · Entrez [5908](https://www.ncbi.nlm.nih.gov/gene/5908) · UniProt [P61224](https://www.uniprot.org/uniprotkb/P61224) · Ensembl [ENSG00000127314](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127314)

## Data

Gene col 4798: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4798); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4798, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4798]; `tensor/DDL_lfc|DDL_z.npy` [4798]; `embed/gene_vectors.npy` [4798]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4798 or target_col == 4798). Every well: [[RAP1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAP1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
