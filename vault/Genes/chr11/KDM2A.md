---
symbol: "KDM2A"
type: "gene"
col: 10342
ensembl_id: "ENSG00000173120"
name: "lysine demethylase 2A"
location: "11q13.2"
module: 144
arm: "+"
pooled_cpm: 411.47
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 16
n_dd_up_clean: 8
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/144"]
generated_by: "tahoemap"
---

# KDM2A

*lysine demethylase 2A* — 11q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.08× (z +17.9, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.350× (z -24.7, q 0e+00, down in 43 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.730× (z -7.7, q 2e-12, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IPMK]] (+0.68, fdr 7e-06), [[ZNF654]] (+0.68, fdr 7e-06), [[NARF]] (+0.65, fdr 7e-06); moves opposite to [[POGK]] (-0.63, fdr 1e-05), [[FARSB]] (-0.56, fdr 1e-05), [[PRPF19]] (-0.55, fdr 1e-05).
> It is in [[Module 144]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10342.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.08×** | +17.9 | 0e+00 | 46/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.04×** | +14.2 | 2e-43 | 47/49 (SW480, BT-474, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.67×** | +12.5 | 1e-33 | 44/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.56×** | +10.8 | 3e-25 | 43/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.49×** | +9.9 | 7e-21 | 43/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.99×** | +8.8 | 1e-16 | 42/48 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.70×** | +6.8 | 7e-10 | 46/48 (CFPAC-1, BT-474, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.21×** | +4.6 | 3e-04 | 23/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~3% of this change | 1.19× | +4.0 | 0.004 | 21/48 (PANC-1, HT-29, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.8 | 0.009 | 19/48 (HT-29, LoVo, …) | rises with dose |  |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | 1.11× | +3.6 | 0.018 | 3/48 (NCI-H2030, HS-578T, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.5 | 0.020 | 16/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Tomivosertib (drug)]] 5 µM |  | **1.30×** | +3.3 | 0.039 | 29/48 (NCI-H1573, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.13× | +3.0 | 0.11 | 11/48 (AsPC-1, H4, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 16 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10342.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.350×** | -24.7 | 0e+00 | 43/44 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.389×** | -23.1 | 0e+00 | 49/49 (NCI-H1792, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.480×** | -16.6 | 0e+00 | 43/45 (CFPAC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.730×** | -7.7 | 2e-12 | 40/48 (NCI-H1573, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.813×** | -7.1 | 8e-11 | 27/48 (SNU-423, AsPC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.746×** | -7.1 | 8e-11 | 38/48 (CFPAC-1, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.836× | -6.2 | 5e-08 | 21/48 (SHP-77, LOX-IMVI, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.790×** | -5.7 | 6e-07 | 30/48 (CFPAC-1, C32, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.804×** | -5.3 | 6e-06 | 25/48 (C32, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~14% of this change | **0.812×** | -4.9 | 6e-05 | 25/47 (NCI-H1573, C32, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.821×** | -4.8 | 8e-05 | 25/48 (MIA PaCa-2, SNU-423, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.826×** | -4.7 | 1e-04 | 26/48 (CFPAC-1, HCT15, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.951× | -4.3 | 6e-04 | 0/50 | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | 0.844× | -4.0 | 0.003 | 19/47 (CFPAC-1, C32, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.849× | -3.8 | 0.005 | 21/48 (NCI-H1573, J82, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.861× | -3.6 | 0.010 | 17/48 (NCI-H1573, CFPAC-1, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.754×** | -3.6 | 0.010 | 29/48 (AsPC-1, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.758×** | -3.5 | 0.013 | 30/49 (AsPC-1, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.760×** | -3.5 | 0.013 | 27/47 (SK-MEL-2, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.869× | -3.4 | 0.017 | 16/48 (NCI-H1573, LS 180, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.831×** | -3.2 | 0.034 | 23/47 (SW 900, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | 0.883× | -3.0 | 0.052 | 9/48 (KATO III, LoVo, …) | rises with dose |  |
| [[Infigratinib (drug)]] 0.05 µM |  | 0.877× | -3.0 | 0.054 | 5/48 (SW1417, NCI-H2030, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | 0.844× | -3.0 | 0.059 | 18/48 (SW 900, RPMI-7951, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10342. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 1,363 | 5 (1 ⚠) | 8 (7 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.56× (z +17.4) | [[Dinaciclib (drug)]] 0.5 µM 0.171× (z -32.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.585× (z -10.0) |
| [[NCI-H1573 (line)]] | alt | 588 | 3 (1 ⚠) | 9 (6 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.06× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.124× (z -30.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.506× (z -10.4) |
| [[BT-474 (line)]] | alt | 563 | 7 (1 ⚠) | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 5.04× (z +16.2) | [[Dinaciclib (drug)]] 0.05 µM 0.462× (z -13.8) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 483 | 1 | 10 (8 ⚠) | [[TAK-901 (drug)]] 5 µM 3.08× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.269× (z -21.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.345× (z -17.5) |
| [[HOP62 (line)]] | alt | 479 | 5 (1 ⚠) | 6 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.60× (z +14.5) | [[Dinaciclib (drug)]] 0.5 µM 0.292× (z -18.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.541× (z -9.2) |
| [[SW480 (line)]] | alt | 357 | 8 (2 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.97× (z +22.1) | [[Dinaciclib (drug)]] 0.5 µM 0.482× (z -14.8) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 535 | 1 | 9 (7 ⚠) | [[TAK-901 (drug)]] 5 µM 2.49× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.221× (z -25.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.560× (z -10.2) |
| [[NCI-H460 (line)]] | wt | 259 | 8 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.56× (z +21.4) | [[Dinaciclib (drug)]] 5 µM 0.280× (z -20.6) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 375 | 5 (2 ⚠) | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.18× (z +13.2) | [[Dinaciclib (drug)]] 0.5 µM 0.305× (z -20.2) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 841 | 6 (1 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.92× (z +13.4) | [[Dinaciclib (drug)]] 0.5 µM 0.408× (z -18.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.642× (z -9.0) |
| [[HEC-1-A (line)]] | alt | 310 | 5 (3 ⚠) | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.55× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.332× (z -19.0) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 417 | 5 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.94× (z +19.9) | [[Dinaciclib (drug)]] 5 µM 0.303× (z -21.3) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 335 | 6 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.86× (z +18.5) | [[Dinaciclib (drug)]] 5 µM 0.333× (z -14.5) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 467 | 3 (1 ⚠) | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.12× (z +14.1) | [[Dinaciclib (drug)]] 0.5 µM 0.294× (z -23.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 291 | 5 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.48× (z +22.1) | [[Dinaciclib (drug)]] 0.5 µM 0.330× (z -19.7) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 426 | 5 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.84× (z +20.0) | [[Dinaciclib (drug)]] 5 µM 0.419× (z -16.1) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 383 | 4 (2 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.22× (z +13.7) | [[Dinaciclib (drug)]] 0.5 µM 0.467× (z -12.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 416 | 4 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.47× (z +16.2) | [[Dinaciclib (drug)]] 5 µM 0.383× (z -16.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 393 | 2 | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 3.18× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.311× (z -20.9) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 457 | 3 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.36× (z +14.7) | [[Dinaciclib (drug)]] 0.5 µM 0.303× (z -20.3) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 528 | 2 | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 3.85× (z +13.6) | [[Dinaciclib (drug)]] 0.5 µM 0.305× (z -23.0) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 298 | 5 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.72× (z +13.6) | [[Dinaciclib (drug)]] 5 µM 0.338× (z -14.1) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 433 | 2 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 2.94× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.441× (z -14.0) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 460 | 1 | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 3.36× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.282× (z -17.1) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 450 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.249× (z -22.8) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.653× (z -9.9) |
| [[SW 900 (line)]] | alt | 421 | 2 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.83× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.294× (z -19.8) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 333 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.57× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.282× (z -18.1) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 382 | 2 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.71× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.229× (z -14.3) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 538 | 1 | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.07× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.223× (z -20.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.509× (z -9.6) |
| [[HepG2_C3A (line)]] | wt | 257 | 2 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.22× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.389× (z -12.8) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 336 | 2 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +13.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.10× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.322× (z -14.0) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 410 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.80× (z +10.6) | [[Dinaciclib (drug)]] 0.05 µM 0.403× (z -15.2) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 427 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.68× (z +13.4) | [[Dinaciclib (drug)]] 0.5 µM 0.292× (z -20.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 322 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.37× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.233× (z -22.2) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 332 | 2 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.98× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.354× (z -11.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 291 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.294× (z -19.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 210 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +14.3) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.5 µM 0.532× (z -10.8) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 323 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.20× (z +17.5) | — |
| [[H4 (line)]] | wt | 293 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.58× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.436× (z -10.4) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 393 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.462× (z -13.3) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 367 | 2 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.40× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.286× (z -16.0) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 359 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.325× (z -16.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 405 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.447× (z -8.8) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 336 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.09× (z +8.6) | — |
| [[NCI-H661 (line)]] | alt | 315 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.251× (z -11.1) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 152 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.475× (z -9.9) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 292 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0980× (z -13.6) ⚠ toxic; transcription drop |
| [[NCI-H2122 (line)]] | alt | 406 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 409 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 344 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10342), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IPMK]] | +0.68 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[ZNF654]] | +0.68 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[NARF]] | +0.65 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[EMSY]] | +0.64 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[ZMAT5]] | +0.61 | +0.51 / +0.41 | both halves | 4e-05 |  |
| [[RNF122]] | +0.60 | +0.70 / +0.41 | both halves | 4e-05 |  |
| [[OST4]] | +0.60 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[SOS1]] | +0.59 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[C4orf47]] | +0.59 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[FUT11]] | +0.58 | +0.69 / +0.49 | both halves | 1e-05 |  |
| [[NOL3]] | +0.58 | +0.43 / +0.63 | both halves | 3e-05 |  |
| [[CDK19]] | +0.58 | +0.50 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POGK]] | -0.63 | -0.65 / -0.55 | both halves | 1e-05 |  |
| [[FARSB]] | -0.56 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[PRPF19]] | -0.55 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[ATIC]] | -0.54 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[CCT2]] | -0.53 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[VARS1]] | -0.53 | -0.62 / -0.43 | both halves | 4e-05 |  |
| [[DHX9]] | -0.53 | -0.52 / -0.40 | both halves | 4e-05 |  |
| [[ZDHHC21]] | -0.53 | -0.35 / -0.50 | both halves | 1e-04 |  |
| [[OCRL]] | -0.53 | -0.50 / -0.43 | both halves | 4e-05 |  |
| [[N6AMT1]] | -0.52 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[NLE1]] | -0.52 | -0.38 / -0.56 | both halves | 6e-05 |  |
| [[PFAS]] | -0.52 | -0.51 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 144]]; 32 genes; every member is in the + arm (projection on the module's main direction 0.732). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (2.4, -38.6); signed map (-31.4, 25.7). **Vector** length 115, 47.1% of its response variance represented; |z| ≥ 3 in 1,426 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +7.4 | +1.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.9 | +0.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +4.6 | +17.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.5 | +3.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.4 | +2.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.1 | +1.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.8 | +6.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.8 | +1.5 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +3.4 | +1.3 |
| fall | [[Selinexor (drug)]] 5 µM |  | -8.5 | -7.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~14% of this change | -7.5 | -4.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -7.4 | -16.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.8 | -5.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -6.5 | +0.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.3 | -6.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.0 | -4.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.9 | -3.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.3 | -2.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.2 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | lysine demethylase 2A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.2 — chr11:67,119,263-67,258,082 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1004, FBL11, LILINA, DKFZP434M1735, FBL7, FLJ00115, CXXC8, JHDM1A; previously FBXL11 |
| Gene groups (HGNC) | PHD finger proteins; Zinc fingers CXXC-type; F-box and leucine rich repeat proteins; Lysine demethylase 2 family |
| Reactome | 3 pathways, smallest: HDMs demethylate histones; Chromatin modifying enzymes; Chromatin organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2K7](https://www.uniprot.org/uniprotkb/Q9Y2K7) (Lysine-specific demethylase 2A):

> Histone demethylase that specifically demethylates 'Lys-36' of histone H3, thereby playing a central role in histone code. Preferentially demethylates dimethylated H3 'Lys-36' residue while it has weak or no activity for mono- and tri-methylated H3 'Lys-36'. May also recognize and bind to some phosphorylated proteins and promote their ubiquitination and degradation. Required to maintain the heterochromatic state. Associates with centromeres and represses transcription of small non-coding RNAs …

**Summary**, from NCBI Gene [22992](https://www.ncbi.nlm.nih.gov/gene/22992):

> This gene encodes a member of the F-box protein family which is characterized by an approximately 40 amino acid motif, the F-box. The F-box proteins constitute one of the four subunits of ubiquitin protein ligase complex called SCFs (SKP1-cullin-F-box), which function in phosphorylation-dependent ubiquitination. The F-box proteins are divided into 3 classes: Fbws containing WD-40 domains, Fbls containing leucine-rich repeats, and Fbxs containing either different protein-protein interaction …

**Accessions** — [HGNC:13606](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13606) · Entrez [22992](https://www.ncbi.nlm.nih.gov/gene/22992) · UniProt [Q9Y2K7](https://www.uniprot.org/uniprotkb/Q9Y2K7) · Ensembl [ENSG00000173120](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173120)

## Data

Gene col 10342: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10342); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10342, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10342]; `tensor/DDL_lfc|DDL_z.npy` [10342]; `embed/gene_vectors.npy` [10342]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10342 or target_col == 10342). Every well: [[KDM2A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KDM2A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
