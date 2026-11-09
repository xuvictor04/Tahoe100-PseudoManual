---
symbol: "PPFIA1"
type: "gene"
col: 5227
ensembl_id: "ENSG00000131626"
name: "PPFI scaffold protein A1"
location: "11q13.3"
module: 180
arm: "+"
pooled_cpm: 281.45
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 6
n_dd_up_clean: 17
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/180"]
generated_by: "tahoemap"
---

# PPFIA1

*PPFI scaffold protein A1* — 11q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.05× (z +19.5, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.643× (z -11.6, q 3e-28, down in 35 of 44 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 4 lines (NCI-H2347 0.568×, C32 0.555×, Hs 766T 0.554×, NCI-H1792 0.604×; ⚠ cell-cycle shift, explains ~18% of this change); [[Dinaciclib (drug)]] 5 µM in 4 lines (C-33 A 0.294×, NCI-H1792 0.378×, C32 0.450×, KATO III 0.518×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H1792 0.337×, C32 0.431×; ⚠ toxic; transcription drop); [[Procainamide (hydrochloride) (drug)]] 0.05 µM in 1 line (SW 1088 0.0710×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KDM4B]] (+0.68, fdr 7e-06), [[NGLY1]] (+0.67, fdr 7e-06), [[ENO2]] (+0.64, fdr 1e-05); moves opposite to [[MTMR2]] (-0.64, fdr 1e-05), [[SMG7]] (-0.61, fdr 1e-05), [[CC2D2A]] (-0.59, fdr 2e-05).
> It is in [[Module 180]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAP3K9]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5227.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.05×** | +19.5 | 0e+00 | 47/48 (SW480, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.98×** | +18.6 | 0e+00 | 48/48 (SW480, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.89×** | +17.3 | 0e+00 | 43/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.51×** | +15.9 | 0e+00 | 35/48 (COLO 205, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.70×** | +14.4 | 8e-45 | 46/48 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.60×** | +12.8 | 2e-35 | 40/48 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.54×** | +11.8 | 6e-30 | 38/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.49×** | +10.8 | 2e-25 | 37/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.39×** | +9.0 | 9e-18 | 35/48 (A498, HS-578T, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.37×** | +8.5 | 1e-15 | 40/48 (PANC-1, Hs 766T, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.62×** | +6.9 | 3e-10 | 43/48 (SHP-77, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.26×** | +6.2 | 2e-08 | 31/48 (NCI-H23, SW480, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.20×** | +5.1 | 2e-05 | 23/47 (SW480, NCI-H23, …) | all doses, stronger at high dose |  |
| [[venetoclax (drug)]] 5 µM |  | **1.40×** | +4.8 | 6e-05 | 29/48 (PANC-1, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 1.19× | +4.6 | 2e-04 | 23/50 (LS 180, NCI-H23, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.36×** | +4.4 | 4e-04 | 25/48 (Panc 03.27, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.23×** | +4.1 | 0.001 | 26/48 (LOX-IMVI, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.33×** | +4.0 | 0.002 | 24/49 (COLO 205, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.30×** | +3.8 | 0.004 | 25/48 (Hs 766T, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 1.17× | +3.7 | 0.005 | 11/48 (HCT15, MIA PaCa-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 10 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5227.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 4 lines (NCI-H2347 0.568×, C32 0.555×, Hs 766T 0.554×, NCI-H1792 0.604×; ⚠ cell-cycle shift, explains ~18% of this change); [[Dinaciclib (drug)]] 5 µM in 4 lines (C-33 A 0.294×, NCI-H1792 0.378×, C32 0.450×, KATO III 0.518×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H1792 0.337×, C32 0.431×; ⚠ toxic; transcription drop); [[Procainamide (hydrochloride) (drug)]] 0.05 µM in 1 line (SW 1088 0.0710×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.643×** | -11.6 | 3e-28 | 35/44 (C-33 A, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.773×** | -9.9 | 1e-20 | 36/48 (NCI-H2347, C32, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.712×** | -8.6 | 2e-15 | 30/45 (NCI-H1792, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.744×** | -7.7 | 1e-12 | 36/47 (C32, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.841× | -6.7 | 3e-09 | 22/48 (NCI-H2030, NCI-H2347, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.765×** | -6.3 | 2e-08 | 33/49 (C32, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Filgotinib (drug)]] 5 µM |  | 0.837× | -4.8 | 1e-04 | 21/48 (HOP62, NCI-H1792, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.739×** | -4.3 | 0.001 | 22/38 (C32, BT-474, …) | top dose only | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.958× | -4.3 | 0.001 | 0/50 | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.859× | -4.1 | 0.002 | 16/48 (CFPAC-1, HepG2/C3A, …) | rises with dose |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | 0.875× | -3.6 | 0.014 | 9/48 (NCI-H1573, NCI-H460, …) | top dose only |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.876× | -3.6 | 0.015 | 10/48 (KATO III, LoVo, …) | rises with dose |  |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.881× | -3.5 | 0.023 | 9/48 (NCI-H1573, HOP62, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.867× | -3.4 | 0.028 | 17/48 (LoVo, NCI-H2347, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | 0.883× | -3.4 | 0.028 | 13/48 (NCI-H2347, LoVo, …) | all doses, stronger at high dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.890× | -3.2 | 0.056 | 12/48 (LOX-IMVI, RKO, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.892× | -3.1 | 0.057 | 16/48 (NCI-H1573, CFPAC-1, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.924× | -3.1 | 0.068 | 1/48 (LOX-IMVI) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | 0.896× | -3.0 | 0.079 | 6/49 (A498, LOX-IMVI, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.899× | -2.9 | 0.096 | 9/48 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.896× | -2.9 | 0.096 | 11/48 (RKO, NCI-H1792, …) | top dose only |  |
| [[Larotrectinib (drug)]] 5 µM |  | 0.928× | -2.9 | 0.096 | 1/48 (CHP-212) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5227. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 439 | 11 (5 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.27× (z +14.0) | — |
| [[SW480 (line)]] | alt | 256 | 11 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.33× (z +30.2) | — |
| [[COLO 205 (line)]] | alt | 144 | 10 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.42× (z +22.8) | — |
| [[PANC-1 (line)]] | alt | 270 | 10 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.67× (z +17.6) | — |
| [[HS-578T (line)]] | alt | 214 | 9 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.10× (z +17.9) | — |
| [[LoVo (line)]] | wt | 328 | 6 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.06× (z +15.5) | [[Dinaciclib (drug)]] 0.5 µM 0.540× (z -11.5) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 280 | 2 | 6 (6 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.94× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.334× (z -15.1) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 330 | 8 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.34× (z +15.8) | — |
| [[Hs 766T (line)]] | wt | 229 | 6 (2 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.45× (z +13.0) | [[Selinexor (drug)]] 5 µM 0.554× (z -12.1) ⚠ cell-cycle shift, explains ~18% of this change |
| [[HT-29 (line)]] | alt | 349 | 7 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.10× (z +13.5) | [[Dinaciclib (drug)]] 5 µM 0.549× (z -10.5) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 252 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +19.8) | — |
| [[KATO III (line)]] | alt | 300 | 5 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.54× (z +21.7) | [[Dinaciclib (drug)]] 5 µM 0.518× (z -10.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 267 | 3 (1 ⚠) | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.76× (z +15.3) | [[Dinaciclib (drug)]] 0.05 µM 0.337× (z -15.1) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 325 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +15.2) | [[Dinaciclib (drug)]] 5 µM 0.560× (z -8.6) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 221 | 5 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.57× (z +16.2) | [[Dinaciclib (drug)]] 5 µM 0.546× (z -10.0) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 289 | 4 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.58× (z +13.7) | [[Selinexor (drug)]] 5 µM 0.568× (z -16.8) ⚠ cell-cycle shift, explains ~18% of this change |
| [[SNU-423 (line)]] | alt | 288 | 6 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.12× (z +11.7) | — |
| [[A498 (line)]] | wt | 148 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +18.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 219 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 2.65× (z +14.1) | — |
| [[NCI-H1573 (line)]] | alt | 746 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.10× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.559× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 176 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.99× (z +16.5) | — |
| [[Panc 03.27 (line)]] | alt | 307 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 3.16× (z +23.2) | — |
| [[A549 (line)]] | wt | 224 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.00× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.494× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 207 | 3 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 1.73× (z +9.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.584× (z -9.3) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 961 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +11.9) | — |
| [[SNU-1 (line)]] | wt | 208 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.70× (z +12.5) | — |
| [[SW1417 (line)]] | alt | 317 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.66× (z +21.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.643× (z -9.2) ⚠ toxic |
| [[A-427 (line)]] | wt | 239 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.01× (z +13.7) | — |
| [[BT-474 (line)]] | alt | 313 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +13.9) | — |
| [[H4 (line)]] | wt | 155 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.90× (z +10.3) | — |
| [[HCT15 (line)]] | alt | 258 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.57× (z +12.1) | — |
| [[HEC-1-A (line)]] | alt | 196 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.07× (z +14.5) | — |
| [[HepG2_C3A (line)]] | wt | 182 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.36× (z +10.1) | — |
| [[J82 (line)]] | alt | 373 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.61× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.524× (z -9.2) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 228 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.36× (z +13.8) | — |
| [[RPMI-7951 (line)]] | alt | 162 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +8.9) | — |
| [[SW48 (line)]] | wt | 304 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.15× (z +9.0) | [[Selinexor (drug)]] 5 µM 0.587× (z -9.0) ⚠ cell-cycle shift, explains ~18% of this change |
| [[AN3 CA (line)]] | alt | 257 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.306× (z -10.2) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 291 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.294× (z -14.2) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 254 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.609× (z -8.6) ⚠ cell-cycle shift, explains ~18% of this change |
| [[SW 1088 (line)]] | alt | 144 | 0 | 1 | — | [[Procainamide (hydrochloride) (drug)]] 0.05 µM 0.0710× (z -11.1) |
| [[A-172 (line)]] | wt | 234 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 178 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 213 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 291 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 238 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 293 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 216 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 348 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 260 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5227), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KDM4B]] | +0.68 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[NGLY1]] | +0.67 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[ENO2]] | +0.64 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[PPP2R5B]] | +0.64 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[ARFGAP3]] | +0.62 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[ZXDC]] | +0.61 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[ARFGEF3]] | +0.61 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[TBC1D20]] | +0.61 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[GOLGA6L9]] | +0.59 | +0.41 / +0.55 | both halves | 4e-05 |  |
| [[HILPDA]] | +0.59 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[GAN]] | +0.58 | +0.52 / +0.54 | both halves | 1e-05 | same gene group |
| [[TMEM184B]] | +0.58 | +0.50 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTMR2]] | -0.64 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[SMG7]] | -0.61 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[CC2D2A]] | -0.59 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[SF3B4]] | -0.59 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[ACCS]] | -0.58 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[GTF3C6]] | -0.55 | -0.38 / -0.44 | both halves | 7e-05 |  |
| [[ACADM]] | -0.55 | -0.36 / -0.43 | both halves | 1e-04 |  |
| [[U2AF2]] | -0.55 | -0.41 / -0.36 | both halves | 9e-05 |  |
| [[MTPAP]] | -0.54 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[POMK]] | -0.54 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[EWSR1]] | -0.54 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[QTRT2]] | -0.54 | -0.55 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP3K9]] | B | MAP3K9 activity raises PPFIA1's level | lines that do not express MAP3K9 (8) vs lines expressing it (42) | 1.36× lower at baseline in the lines without MAP3K9 | 0.098 | ⚠ within organs, on part of the lines; also absent: CDKN1C, DAPK2, PRKCZ; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 180]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.755). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (12.8, -15.0); signed map (-36.4, 26.4). **Vector** length 121, 44.7% of its response variance represented; |z| ≥ 3 in 1,473 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +8.1 | +18.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +7.9 | +19.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +7.2 | +14.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.3 | +8.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +4.2 | +6.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.5 | +3.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.1 | +3.5 |
|  | [[EX229 (drug)]] 5 µM |  | +3.0 | +3.1 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +3.0 | +2.9 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | -13.0 | -9.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.5 | -7.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | -6.6 | +4.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -6.5 | +2.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.4 | -8.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.1 | -6.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.3 | -1.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.2 | -4.1 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -3.1 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | PPFI scaffold protein A1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.3 — chr11:70,270,690-70,385,312 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LIP.1, LIPRIN |
| Gene groups (HGNC) | Sterile alpha motif domain containing; MicroRNA protein coding host genes; PPFI scaffold protein family |
| Reactome | 10 pathways, smallest: Acetylcholine Neurotransmitter Release Cycle; Norepinephrine Neurotransmitter Release Cycle; Receptor-type tyrosine-protein phosphatases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13136](https://www.uniprot.org/uniprotkb/Q13136) (Liprin-alpha-1):

> May regulate the disassembly of focal adhesions. May localize receptor-like tyrosine phosphatases type 2A at specific sites on the plasma membrane, possibly regulating their interaction with the extracellular environment and their association with substrates.

**Summary**, from NCBI Gene [8500](https://www.ncbi.nlm.nih.gov/gene/8500):

> The protein encoded by this gene is a member of the LAR protein-tyrosine phosphatase-interacting protein (liprin) family. Liprins interact with members of LAR family of transmembrane protein tyrosine phosphatases, which are known to be important for axon guidance and mammary gland development. This protein binds to the intracellular membrane-distal phosphatase domain of tyrosine phosphatase LAR, and appears to localize LAR to cell focal adhesions. This interaction may regulate the disassembly …

**Accessions** — [HGNC:9245](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9245) · Entrez [8500](https://www.ncbi.nlm.nih.gov/gene/8500) · UniProt [Q13136](https://www.uniprot.org/uniprotkb/Q13136) · Ensembl [ENSG00000131626](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131626)

## Data

Gene col 5227: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5227); `tables/drug_effects.parquet` (61 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5227, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5227]; `tensor/DDL_lfc|DDL_z.npy` [5227]; `embed/gene_vectors.npy` [5227]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5227 or target_col == 5227). Every well: [[PPFIA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPFIA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
