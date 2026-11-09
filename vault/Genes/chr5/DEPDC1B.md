---
symbol: "DEPDC1B"
type: "gene"
col: 429
ensembl_id: "ENSG00000035499"
name: "DEP domain containing 1B"
location: "5q12.1"
module: 22
arm: "+"
pooled_cpm: 47.47
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 27
n_dd_up_clean: 3
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# DEPDC1B

*DEP domain containing 1B* — 5q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.84× (z +16.6, q 0e+00, up in 34 of 48 measured lines) ⚠ cell-cycle shift, explains ~71% of this change. The strongest without an alert is [[Brivudine (drug)]] 5 µM: 1.53× (z +4.3, q 6e-04, up in 11 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (11 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.584× (z -10.4, q 1e-22, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KIF2C]] (+0.92, fdr 7e-06), [[CDK1]] (+0.91, fdr 7e-06), [[AURKB]] (+0.90, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[PIMREG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 20 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 429.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.84×** | +16.6 | 0e+00 | 34/48 (LoVo, NCI-H2347, …) | top dose only | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.67×** | +9.9 | 1e-20 | 34/48 (RKO, A498, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.64×** | +9.6 | 1e-19 | 34/48 (J82, A498, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | **1.52×** | +8.1 | 8e-14 | 32/48 (HT-29, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change | **1.50×** | +7.8 | 6e-13 | 29/47 (CFPAC-1, HT-29, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.48×** | +7.7 | 2e-12 | 30/48 (RKO, A498, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.48×** | +7.6 | 2e-12 | 30/48 (CFPAC-1, SW1417, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.43×** | +7.0 | 2e-10 | 27/48 (RKO, A498, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.41×** | +6.7 | 1e-09 | 25/48 (CFPAC-1, KATO III, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.39×** | +6.4 | 8e-09 | 28/47 (NCI-H23, H4, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.25×** | +6.0 | 1e-07 | 24/48 (LoVo, AsPC-1, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.34×** | +5.6 | 8e-07 | 21/48 (NCI-H23, LoVo, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.73×** | +5.6 | 1e-06 | 19/47 (CFPAC-1, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.57×** | +4.6 | 2e-04 | 22/48 (LoVo, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.53×** | +4.3 | 6e-04 | 11/48 (RKO, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.52×** | +4.3 | 8e-04 | 16/48 (A498, A-172, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 1.16× | +4.0 | 0.002 | 16/48 (RKO, J82, …) | rises with dose |  |
| [[AZD1390 (drug)]] 0.05 µM |  | **1.20×** | +3.4 | 0.019 | 12/48 (Panc 03.27, NCI-H2347, …) | inconsistent across doses |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | 1.16× | +3.0 | 0.071 | 10/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 47 in all, 15 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 429.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.584×** | -10.4 | 1e-22 | 39/48 (AN3 CA, SW480, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **0.692×** | -10.0 | 3e-21 | 28/48 (A-427, LS 180, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.592×** | -9.6 | 1e-19 | 33/48 (PANC-1, A-427, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **0.611×** | -9.6 | 1e-19 | 35/48 (H4, A-427, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.655×** | -8.2 | 2e-14 | 27/48 (NCI-H2030, SW48, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.708×** | -6.7 | 2e-09 | 24/48 (MIA PaCa-2, Hs 766T, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.712×** | -6.6 | 3e-09 | 28/48 (A-427, A498, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.718×** | -6.4 | 1e-08 | 30/48 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.726×** | -6.2 | 3e-08 | 21/48 (H4, LOX-IMVI, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.798×** | -6.1 | 6e-08 | 26/48 (A-427, H4, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.749×** | -5.6 | 1e-06 | 21/48 (SW48, C32, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~55% of this change | **0.624×** | -4.8 | 8e-05 | 21/44 (HCT15, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.796×** | -4.4 | 4e-04 | 19/48 (AN3 CA, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Amsacrine (drug)]] 5 µM |  | 0.859× | -4.1 | 0.001 | 21/48 (LOX-IMVI, A-172, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.803×** | -4.1 | 0.002 | 18/47 (A549, LOX-IMVI, …) | rises with dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **0.814×** | -4.0 | 0.002 | 11/48 (COLO 205, LOX-IMVI, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.812×** | -3.9 | 0.003 | 19/48 (A498, NCI-H1573, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.875× | -3.6 | 0.008 | 11/48 (HCT15, NCI-H460, …) | two highest doses |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.847× | -3.6 | 0.010 | 11/48 (A-427, HCT15, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.828×** | -3.5 | 0.011 | 12/47 (A-172, HOP62, …) | rises with dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | 0.880× | -3.5 | 0.012 | 15/48 (hTERT-HPNE, COLO 205, …) | top dose only |  |
| [[Rapamycin (drug)]] 0.5 µM |  | 0.839× | -3.4 | 0.016 | 11/48 (hTERT-HPNE, SW 1088, …) | inconsistent across doses |  |
| [[palbociclib (drug)]] 5 µM |  | **0.717×** | -3.4 | 0.016 | 14/47 (A-427, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.56 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 429. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AN3 CA (line)]] | alt | 195 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0479× (z -19.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.178× (z -11.3) |
| [[A-427 (line)]] | wt | 134 | 0 | 6 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.297× (z -15.2) ⚠ cell-cycle shift, explains ~82% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.485× (z -9.0) |
| [[LOX-IMVI (line)]] | wt | 44.2 | 1 (1 ⚠) | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +9.6) ⚠ cell-cycle shift, explains ~71% of this change | [[Selinexor (drug)]] 5 µM 0.333× (z -11.4) ⚠ cell-cycle shift, explains ~82% of this change · without an alert: [[Amsacrine (drug)]] 0.5 µM 0.229× (z -10.9) |
| [[A498 (line)]] | wt | 34.0 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +9.4) ⚠ cell-cycle shift, explains ~71% of this change | [[Selinexor (drug)]] 5 µM 0.423× (z -10.7) ⚠ cell-cycle shift, explains ~82% of this change |
| [[H4 (line)]] | wt | 67.3 | 0 | 3 (3 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.103× (z -13.5) ⚠ cell-cycle shift, explains ~38% of this change |
| [[LoVo (line)]] | wt | 44.6 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.83× (z +21.4) ⚠ cell-cycle shift, explains ~71% of this change | — |
| [[LS 180 (line)]] | wt | 30.4 | 0 | 3 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.233× (z -13.0) ⚠ cell-cycle shift, explains ~82% of this change |
| [[NCI-H2030 (line)]] | alt | 58.7 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +15.8) ⚠ cell-cycle shift, explains ~71% of this change | [[Auranofin (drug)]] 5 µM 0.354× (z -9.8) |
| [[A-172 (line)]] | wt | 25.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 4.51× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.278× (z -9.0) ⚠ cell-cycle shift, explains ~38% of this change |
| [[AsPC-1 (line)]] | alt | 15.1 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.40× (z +11.9) ⚠ cell-cycle shift, explains ~71% of this change | — |
| [[CFPAC-1 (line)]] | alt | 89.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.55× (z +9.1) ⚠ cell-cycle shift, explains ~87% of this change | [[Selinexor (drug)]] 5 µM 0.536× (z -8.7) ⚠ cell-cycle shift, explains ~82% of this change |
| [[Panc 03.27 (line)]] | alt | 47.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +14.5) ⚠ cell-cycle shift, explains ~71% of this change | [[Selinexor (drug)]] 5 µM 0.401× (z -10.1) ⚠ cell-cycle shift, explains ~82% of this change |
| [[PANC-1 (line)]] | alt | 48.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +11.5) ⚠ cell-cycle shift, explains ~71% of this change | [[Bortezomib (drug)]] 0.05 µM 0.412× (z -9.5) ⚠ cell-cycle shift, explains ~50% of this change |
| [[A549 (line)]] | wt | 52.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.450× (z -9.1) ⚠ cell-cycle shift, explains ~82% of this change |
| [[HCT15 (line)]] | alt | 52.0 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0487× (z -9.9) ⚠ toxic; cell-cycle shift, explains ~55% of this change |
| [[HOP62 (line)]] | alt | 26.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.453× (z -8.5) ⚠ cell-cycle shift, explains ~82% of this change |
| [[Hs 766T (line)]] | wt | 15.6 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.128× (z -9.9) |
| [[HS-578T (line)]] | alt | 35.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +10.1) ⚠ cell-cycle shift, explains ~71% of this change | — |
| [[HT-29 (line)]] | alt | 34.5 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.84× (z +9.1) ⚠ cell-cycle shift, explains ~87% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 18.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.16× (z +14.1) ⚠ cell-cycle shift, explains ~71% of this change | — |
| [[J82 (line)]] | alt | 42.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +8.6) ⚠ cell-cycle shift, explains ~71% of this change | — |
| [[NCI-H1573 (line)]] | alt | 15.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.17× (z +12.3) ⚠ cell-cycle shift, explains ~71% of this change | — |
| [[NCI-H1792 (line)]] | alt | 31.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +9.5) ⚠ cell-cycle shift, explains ~71% of this change | — |
| [[NCI-H2347 (line)]] | alt | 88.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +16.5) ⚠ cell-cycle shift, explains ~71% of this change | — |
| [[NCI-H460 (line)]] | wt | 56.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +8.9) ⚠ cell-cycle shift, explains ~71% of this change | — |
| [[RKO (line)]] | wt | 47.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +11.5) ⚠ cell-cycle shift, explains ~71% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 53.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.308× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 41.7 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.145× (z -9.0) ⚠ cell-cycle shift, explains ~38% of this change |
| [[SNU-423 (line)]] | alt | 36.2 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.315× (z -8.5) |
| [[SW 900 (line)]] | alt | 47.5 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.286× (z -8.6) |
| [[SW1417 (line)]] | alt | 42.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +11.0) ⚠ cell-cycle shift, explains ~71% of this change | — |
| [[SW480 (line)]] | alt | 63.6 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.370× (z -11.3) |
| [[BT-474 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 75.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 37.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 56.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 62.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 89.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 83.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 48.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 429), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIF2C]] | +0.92 | +0.92 / +0.90 | both halves | 7e-06 | STRING 654 |
| [[CDK1]] | +0.91 | +0.90 / +0.90 | both halves | 7e-06 | STRING 762 |
| [[AURKB]] | +0.90 | +0.88 / +0.86 | both halves | 7e-06 | STRING 682 |
| [[KIF4A]] | +0.89 | +0.90 / +0.85 | both halves | 7e-06 | STRING 597 |
| [[CIT]] | +0.89 | +0.83 / +0.91 | both halves | 7e-06 | pathway: RAC1 GTPase cycle; STRING 492 |
| [[KIFC1]] | +0.89 | +0.84 / +0.87 | both halves | 7e-06 | STRING 427 |
| [[TOP2A]] | +0.88 | +0.88 / +0.85 | both halves | 7e-06 | STRING 685 |
| [[KIF18B]] | +0.88 | +0.86 / +0.86 | both halves | 7e-06 | STRING 413 |
| [[DLGAP5]] | +0.88 | +0.88 / +0.85 | both halves | 7e-06 | STRING 878 |
| [[KIF23]] | +0.88 | +0.87 / +0.87 | both halves | 7e-06 | STRING 654 |
| [[BUB1B]] | +0.88 | +0.86 / +0.86 | both halves | 7e-06 | STRING 797 |
| [[NDC80]] | +0.88 | +0.87 / +0.87 | both halves | 7e-06 | STRING 538 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 3, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIMREG]] | B | PIMREG activity raises DEPDC1B's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 2.10× lower at baseline in the lines without PIMREG | 0.016 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[ANKRD20A4P]] | B | ANKRD20A4P activity raises DEPDC1B's level | lines that do not express ANKRD20A4P (24) vs lines expressing it (26) | 1.56× lower at baseline in the lines without ANKRD20A4P | 0.044 | ⚠ within organs, on part of the lines; also absent: ENSG00000253503, ENSG00000253500, ADGRF5 |
| [[ANKRD20A4P]] | B | ANKRD20A4P activity strengthens DEPDC1B's drug response | lines that do not express ANKRD20A4P (24) vs lines expressing it (24) | the lines without ANKRD20A4P respond 0.95× as strongly (z diff +0.17); strongest at Selinexor 5 µM: 0.73x vs 0.58x (z diff +2.5) | 0.052 | ⚠ within organs, on part of the lines; also absent: ENSG00000253503, ENSG00000253500, ADGRF5; target measured in part of the lines; both ways; artifact flags |
| [[PBK]] | C | PBK activity raises DEPDC1B's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.74× lower at baseline in the lines without PBK | 0.012 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises DEPDC1B's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.21× lower at baseline in the lines without AURKB | 0.082 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[DIAPH3]] | C | DIAPH3 activity raises DEPDC1B's level | lines that do not express DIAPH3 (3) vs lines expressing it (47) | 2.55× lower at baseline in the lines without DIAPH3 | 0.084 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent |
| [[CDCA3]] | C | CDCA3 activity raises DEPDC1B's level | lines that do not express CDCA3 (3) vs lines expressing it (47) | 2.66× lower at baseline in the lines without CDCA3 | 0.085 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TBC1D19, PBK, SNPH; maybe low, not absent |
| [[CDC20]] | C | CDC20 activity raises DEPDC1B's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 2.08× lower at baseline in the lines without CDC20 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.914). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-36.3, -55.2); signed map (-48.6, -42.2). **Vector** length 147, 48.6% of its response variance represented; |z| ≥ 3 in 1,383 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.73 to 60); *DREAM G2/M down* (control, mean cos +0.80 to 28); *Mitotic Prometaphase* (reactome, mean cos +0.69 to 48).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | +5.6 | +16.6 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~58% of this change | +4.3 | +6.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | +4.0 | +7.0 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.9 | +4.2 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | +3.7 | +5.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +4.0 |
|  | [[Docetaxel (drug)]] 5 µM |  | +2.9 | +1.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.7 | +4.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.3 | +4.3 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +2.3 | +1.9 |
| fall | [[Auranofin (drug)]] 5 µM |  | -10.1 | -10.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~50% of this change | -8.2 | -9.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~74% of this change | -7.8 | -9.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | -7.3 | -10.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -7.1 | -8.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.6 | -6.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.4 | -5.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.1 | -3.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -4.0 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | DEP domain containing 1B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q12.1 — chr5:60,596,912-60,700,190 (-) |
| Ensembl biotype | protein_coding |
| Also known as | XTP1, BRCC3 |
| Gene groups (HGNC) | DEP domain containing |
| Reactome | 20 pathways, smallest: RHOV GTPase cycle; RHOU GTPase cycle; RND1 GTPase cycle |
| Matched by | ensembl_id |

UniProt [Q8WUY9](https://www.uniprot.org/uniprotkb/Q8WUY9) carries no function annotation.

**Summary**, from NCBI Gene [55789](https://www.ncbi.nlm.nih.gov/gene/55789):

> Predicted to enable GTPase activator activity. Involved in cell migration and positive regulation of Wnt signaling pathway. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24902](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24902) · Entrez [55789](https://www.ncbi.nlm.nih.gov/gene/55789) · UniProt [Q8WUY9](https://www.uniprot.org/uniprotkb/Q8WUY9) · Ensembl [ENSG00000035499](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000035499)

## Data

Gene col 429: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 429); `tables/drug_effects.parquet` (72 rows, flagged included); `relations/gene_relations.parquet` (col_a == 429, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 429]; `tensor/DDL_lfc|DDL_z.npy` [429]; `embed/gene_vectors.npy` [429]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 429 or target_col == 429). Every well: [[DEPDC1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DEPDC1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
