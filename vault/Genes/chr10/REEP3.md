---
symbol: "REEP3"
type: "gene"
col: 9126
ensembl_id: "ENSG00000165476"
name: "receptor accessory protein 3"
location: "10q21.3"
module: 143
arm: "+"
pooled_cpm: 119.91
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 13
n_dd_up_clean: 6
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/143"]
generated_by: "tahoemap"
---

# REEP3

*receptor accessory protein 3* — 10q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.35× (z +20.7, q 0e+00, up in 46 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 1.44× (z +8.8, q 2e-16, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.477× (z -17.9, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATE1]] (+0.68, fdr 7e-06), [[WWC3]] (+0.62, fdr 1e-05), [[BCAP29]] (+0.62, fdr 7e-06); moves opposite to [[CDK7]] (-0.68, fdr 7e-06), [[MED26]] (-0.62, fdr 1e-05), [[CNOT8]] (-0.61, fdr 6e-05).
> It is in [[Module 143]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9126.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.35×** | +20.7 | 0e+00 | 46/49 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.33×** | +19.6 | 0e+00 | 38/43 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.00×** | +15.5 | 0e+00 | 37/45 (SNU-423, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.44×** | +8.8 | 2e-16 | 33/48 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.40×** | +8.2 | 3e-14 | 32/48 (KATO III, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.37×** | +7.6 | 2e-12 | 32/48 (COLO 205, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.35×** | +7.2 | 6e-11 | 31/48 (KATO III, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +5.7 | 7e-07 | 20/48 (RPMI-7951, HT-29, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.25×** | +5.2 | 1e-05 | 26/47 (HOP62, HT-29, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **1.24×** | +5.1 | 2e-05 | 21/49 (HT-29, SW480, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.23×** | +4.9 | 4e-05 | 23/48 (KATO III, LoVo, …) | top dose only |  |
| [[vincristine (drug)]] 5 µM |  | **1.36×** | +3.9 | 0.005 | 21/46 (CFPAC-1, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.25×** | +3.8 | 0.006 | 20/48 (HT-29, COLO 205, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~17% of this change | 1.17× | +3.7 | 0.008 | 19/47 (A-172, SW480, …) | all doses, stronger at high dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 1.16× | +3.6 | 0.013 | 12/48 (A-172, PANC-1, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | 1.17× | +3.6 | 0.013 | 16/47 (SHP-77, SW 900, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.16× | +3.5 | 0.016 | 18/47 (SW 900, H4, …) | all doses, stronger at high dose |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | 1.14× | +3.1 | 0.049 | 6/48 (COLO 205, SW1417, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9126.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.477×** | -17.9 | 0e+00 | 44/48 (Panc 03.27, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.482×** | -17.7 | 0e+00 | 44/48 (A498, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.557×** | -14.2 | 2e-43 | 43/48 (A498, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.734×** | -10.5 | 1e-23 | 34/49 (LS 180, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.786×** | -8.2 | 3e-14 | 26/48 (RKO, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.535×** | -7.9 | 2e-13 | 36/49 (RKO, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.769×** | -6.4 | 2e-08 | 29/48 (HepG2/C3A, J82, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.788×** | -5.8 | 5e-07 | 31/48 (A498, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.653×** | -5.4 | 4e-06 | 25/48 (RKO, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.814×** | -5.0 | 3e-05 | 24/48 (PANC-1, BT-474, …) | rises with dose |  |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **0.804×** | -4.9 | 5e-05 | 27/47 (BT-474, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.827×** | -4.4 | 5e-04 | 24/48 (RKO, A-427, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 0.842× | -4.2 | 0.001 | 21/48 (KATO III, RKO, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | 0.888× | -4.0 | 0.002 | 10/48 (RKO, KATO III, …) | all doses, flat | low cells (technical?) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.850× | -4.0 | 0.003 | 15/50 (NCI-H23, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.900× | -3.6 | 0.010 | 5/48 (C32, HEC-1-A, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.762×** | -3.5 | 0.016 | 15/49 (AsPC-1, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | 0.876× | -3.1 | 0.051 | 10/48 (AsPC-1, HEC-1-A, …) | rises with dose |  |
| [[Fumaric acid (drug)]] 5 µM |  | 0.878× | -3.1 | 0.056 | 11/49 (AN3 CA, Panc 03.27, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9126. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 117 | 1 (1 ⚠) | 9 (3 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.91× (z +16.8) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.280× (z -15.7) |
| [[Panc 03.27 (line)]] | alt | 191 | 2 (2 ⚠) | 6 | [[Dinaciclib (drug)]] 0.5 µM 2.15× (z +9.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.224× (z -18.6) |
| [[A-427 (line)]] | wt | 84.6 | 2 (2 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.40× (z +14.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.379× (z -11.1) |
| [[KATO III (line)]] | alt | 113 | 4 (2 ⚠) | 3 | [[Digitoxin (drug)]] 5 µM 2.23× (z +10.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 1.96× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.532× (z -11.9) |
| [[HOP62 (line)]] | alt | 130 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.69× (z +17.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.463× (z -10.2) |
| [[Hs 766T (line)]] | wt | 134 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.35× (z +9.9) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.355× (z -11.9) |
| [[PANC-1 (line)]] | alt | 219 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.88× (z +18.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.456× (z -13.9) |
| [[A549 (line)]] | wt | 79.6 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 5.14× (z +16.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.376× (z -10.3) |
| [[HT-29 (line)]] | alt | 106 | 1 | 4 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.92× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.499× (z -13.8) |
| [[MIA PaCa-2 (line)]] | alt | 114 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.58× (z +11.9) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.317× (z -14.5) |
| [[NCI-H1792 (line)]] | alt | 99.5 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.46× (z +12.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.227× (z -14.5) |
| [[NCI-H460 (line)]] | wt | 107 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 1.83× (z +9.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.484× (z -11.7) |
| [[A498 (line)]] | wt | 112 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.351× (z -17.7) |
| [[AsPC-1 (line)]] | alt | 255 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.327× (z -15.7) |
| [[CFPAC-1 (line)]] | alt | 121 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.49× (z +17.7) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 67.3 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.05× (z +12.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.79× (z +9.4) | — |
| [[HEC-1-A (line)]] | alt | 101 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.73× (z +13.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.481× (z -10.2) |
| [[HS-578T (line)]] | alt | 94.2 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.91× (z +12.9) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.494× (z -8.6) |
| [[J82 (line)]] | alt | 103 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.355× (z -13.0) |
| [[LoVo (line)]] | wt | 116 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.15× (z +10.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.345× (z -14.5) |
| [[LS 180 (line)]] | wt | 163 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.432× (z -15.6) |
| [[NCI-H2030 (line)]] | alt | 95.8 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.79× (z +12.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.386× (z -11.2) |
| [[NCI-H2347 (line)]] | alt | 137 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.54× (z +14.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.400× (z -10.6) |
| [[SNU-423 (line)]] | alt | 167 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.52× (z +16.8) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.466× (z -10.6) |
| [[SW 900 (line)]] | alt | 134 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.25× (z +10.4) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.483× (z -9.4) |
| [[SW1417 (line)]] | alt | 98.3 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.52× (z +11.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.445× (z -10.2) |
| [[SW480 (line)]] | alt | 153 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.375× (z -16.9) |
| [[A-172 (line)]] | wt | 124 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.45× (z +15.6) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 135 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.378× (z -11.1) |
| [[C32 (line)]] | wt | 53.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.34× (z +9.3) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 72.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.30× (z +12.5) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 85.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.88× (z +15.6) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 60.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.06× (z +11.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.344× (z -11.4) |
| [[RPMI-7951 (line)]] | alt | 76.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.54× (z +11.8) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 91.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.48× (z +8.9) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 66.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.80× (z +13.1) ⚠ toxic; transcription drop | [[Lonafarnib (drug)]] 5 µM 0.0812× (z -9.9) ⚠ toxic |
| [[BT-474 (line)]] | alt | 124 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.437× (z -10.0) |
| [[C-33 A (line)]] | alt | 124 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.506× (z -10.6) |
| [[H4 (line)]] | wt | 79.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.30× (z +9.4) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 126 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.36× (z +8.5) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 97.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.31× (z +10.6) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 133 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 45.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 71.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 87.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 104 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9126), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*36 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATE1]] | +0.68 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[WWC3]] | +0.62 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[BCAP29]] | +0.62 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[ARAP2]] | +0.60 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[PAK2]] | +0.59 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[B3GLCT]] | +0.57 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[SLC25A24]] | +0.57 | +0.42 / +0.63 | both halves | 4e-05 |  |
| [[ANAPC7]] | +0.56 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[USP45]] | +0.56 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[MTHFD2L]] | +0.56 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[GALNT10]] | +0.55 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[CDC42BPA]] | +0.55 | +0.50 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*64 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDK7]] | -0.68 | -0.65 / -0.64 | both halves | 7e-06 |  |
| [[MED26]] | -0.62 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[CNOT8]] | -0.61 | -0.39 / -0.67 | both halves | 6e-05 |  |
| [[RANBP10]] | -0.61 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[CCDC115]] | -0.61 | -0.60 / -0.64 | both halves | 7e-06 |  |
| [[PLEKHA2]] | -0.58 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[GGA2]] | -0.58 | -0.46 / -0.56 | both halves | 2e-05 |  |
| [[ACBD3]] | -0.57 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[SPATA7]] | -0.57 | -0.34 / -0.69 | both halves | 1e-04 |  |
| [[VPS37D]] | -0.57 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[MTMR4]] | -0.57 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[UNC119]] | -0.57 | -0.41 / -0.56 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 143]]; 32 genes; every member is in the + arm (projection on the module's main direction 0.622). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-6.9, 3.5); signed map (9.2, -8.5). **Vector** length 126, 39.2% of its response variance represented; |z| ≥ 3 in 1,259 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 0.5 µM |  | +9.2 | +8.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +9.0 | +8.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +7.1 | +7.6 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~17% of this change | +6.9 | +3.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.8 | +19.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.8 | +5.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.7 | +4.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.5 | +3.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.1 | +0.0 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.9 | +2.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.7 | -10.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.2 | -7.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.7 | -17.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.7 | -1.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.6 | -17.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.5 | -3.6 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.4 | -2.2 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -3.0 | -1.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.9 | -5.4 |

## What is on record

|  |  |
|---|---|
| Name | receptor accessory protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q21.3 — chr10:63,521,401-63,625,128 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Yip2b; previously C10orf74 |
| Gene groups (HGNC) | Receptor accessory proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6NUK4](https://www.uniprot.org/uniprotkb/Q6NUK4) (Receptor expression-enhancing protein 3):

> Microtubule-binding protein required to ensure proper cell division and nuclear envelope reassembly by sequestering the endoplasmic reticulum away from chromosomes during mitosis. Probably acts by clearing the endoplasmic reticulum membrane from metaphase chromosomes.

**Summary**, from NCBI Gene [221035](https://www.ncbi.nlm.nih.gov/gene/221035):

> Predicted to enable microtubule binding activity. Involved in mitotic nuclear membrane reassembly. Predicted to be located in membrane and microtubule. Predicted to be active in cytoplasmic microtubule; endoplasmic reticulum membrane; and endoplasmic reticulum tubular network. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23711](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23711) · Entrez [221035](https://www.ncbi.nlm.nih.gov/gene/221035) · UniProt [Q6NUK4](https://www.uniprot.org/uniprotkb/Q6NUK4) · Ensembl [ENSG00000165476](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165476)

## Data

Gene col 9126: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9126); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9126, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9126]; `tensor/DDL_lfc|DDL_z.npy` [9126]; `embed/gene_vectors.npy` [9126]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9126 or target_col == 9126). Every well: [[REEP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/REEP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
