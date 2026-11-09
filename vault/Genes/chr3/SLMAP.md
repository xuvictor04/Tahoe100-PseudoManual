---
symbol: "SLMAP"
type: "gene"
col: 8750
ensembl_id: "ENSG00000163681"
name: "sarcolemma associated protein"
location: "3p14.3"
module: 54
arm: "+"
pooled_cpm: 295.15
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 5
n_dd_up_clean: 14
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# SLMAP

*sarcolemma associated protein* — 3p14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.03× (z +26.5, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.443× (z -21.6, q 0e+00, down in 47 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[GSK1059615 (drug)]] 0.5 µM: 0.805× (z -4.1, q 0.003, down in 24 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 10 lines (C-33 A 0.0482×, NCI-H1573 0.104×, NCI-H2030 0.198×, LoVo 0.286×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (LoVo 0.305×, NCI-H2347 0.238×, Panc 03.27 0.267×, AsPC-1 0.280×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H2347 0.262×; ⚠ toxic; transcription drop); [[Arbutin (drug)]] 5 µM in 1 line (SW 1088 0.105×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPBP1]] (+0.54, fdr 3e-05), [[TMCC1]] (+0.52, fdr 3e-05), [[STRN3]] (+0.49, fdr 3e-05); moves opposite to [[ZNF17]] (-0.52, fdr 2e-04), [[BAG6]] (-0.49, fdr 2e-04), [[ZNF256]] (-0.47, fdr 1e-04).
> It sits in the **+** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[DAPP1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8750.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.03×** | +26.5 | 0e+00 | 46/48 (J82, A549, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.44×** | +23.6 | 0e+00 | 48/48 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.23×** | +21.1 | 0e+00 | 46/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.08×** | +19.4 | 0e+00 | 47/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.04×** | +18.9 | 0e+00 | 48/48 (HOP62, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.08×** | +18.2 | 0e+00 | 48/48 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.32×** | +16.6 | 0e+00 | 46/49 (LoVo, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.84×** | +15.4 | 0e+00 | 46/48 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.74×** | +14.6 | 0e+00 | 43/48 (KATO III, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.63×** | +12.8 | 5e-36 | 44/48 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +12.1 | 4e-32 | 40/47 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.56×** | +11.8 | 2e-30 | 40/48 (A549, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.23×** | +11.1 | 8e-27 | 45/48 (LoVo, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.63×** | +9.2 | 1e-18 | 45/49 (PANC-1, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.34×** | +7.6 | 9e-13 | 36/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.22×** | +5.1 | 1e-05 | 26/48 (C32, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.11× | +3.9 | 0.003 | 10/48 (HOP62, SNU-423, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 9 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8750.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 10 lines (C-33 A 0.0482×, NCI-H1573 0.104×, NCI-H2030 0.198×, LoVo 0.286×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (LoVo 0.305×, NCI-H2347 0.238×, Panc 03.27 0.267×, AsPC-1 0.280×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H2347 0.262×; ⚠ toxic; transcription drop); [[Arbutin (drug)]] 5 µM in 1 line (SW 1088 0.105×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.443×** | -21.6 | 0e+00 | 47/49 (LoVo, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.457×** | -20.0 | 0e+00 | 42/44 (C-33 A, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.524×** | -15.8 | 0e+00 | 42/45 (NCI-H2347, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.724×** | -8.3 | 2e-14 | 33/47 (NCI-H2347, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.953× | -4.7 | 3e-04 | 0/50 | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 0.856× | -4.2 | 0.003 | 21/48 (SW1417, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.805×** | -4.1 | 0.003 | 24/48 (MIA PaCa-2, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.861× | -4.0 | 0.005 | 17/48 (AsPC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.865× | -3.9 | 0.007 | 12/48 (HEC-1-A, J82, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.867× | -3.8 | 0.008 | 11/48 (NCI-H1573, A549, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.869× | -3.7 | 0.010 | 18/48 (HOP62, C32, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~4% of this change | 0.871× | -3.7 | 0.011 | 16/48 (NCI-H1573, NCI-H2347, …) | rises with dose |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 0.876× | -3.5 | 0.018 | 6/48 (NCI-H460, CHP-212, …) | inconsistent across doses |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | 0.877× | -3.5 | 0.019 | 10/48 (HEC-1-A, NCI-H1792, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.879× | -3.5 | 0.020 | 18/48 (AsPC-1, HT-29, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | 0.842× | -3.3 | 0.037 | 20/47 (A-427, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Apalutamide (drug)]] 0.5 µM |  | 0.886× | -3.2 | 0.039 | 8/48 (NCI-H460, NCI-H1573, …) | inconsistent across doses |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 0.888× | -3.2 | 0.042 | 7/48 (HOP62, SW 900, …) | top dose only |  |
| [[Mifepristone (drug)]] 0.5 µM |  | 0.889× | -3.1 | 0.048 | 11/48 (NCI-H1573, NCI-H460, …) | inconsistent across doses |  |
| [[Carbamazepine (drug)]] 5 µM |  | 0.890× | -3.1 | 0.051 | 9/47 (HOP62, Hs 766T, …) | top dose only |  |
| [[Budesonide (drug)]] 0.5 µM |  | 0.891× | -3.1 | 0.052 | 11/48 (NCI-H1573, SW 1088, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 5 µM |  | 0.923× | -3.1 | 0.055 | 1/48 (SNU-1) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | 0.894× | -3.0 | 0.064 | 11/48 (NCI-H1573, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8750. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 214 | 17 (4 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +19.8) | [[Dinaciclib (drug)]] 5 µM 0.371× (z -15.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 199 | 16 (3 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +24.0) | [[Dinaciclib (drug)]] 5 µM 0.460× (z -14.7) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 498 | 12 (2 ⚠) | 6 (6 ⚠) | [[TAK-901 (drug)]] 5 µM 7.55× (z +21.3) | [[Dinaciclib (drug)]] 5 µM 0.286× (z -24.4) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 314 | 11 (1 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +26.9) | [[Dinaciclib (drug)]] 5 µM 0.339× (z -16.7) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 212 | 13 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +17.2) | [[Dinaciclib (drug)]] 5 µM 0.390× (z -13.4) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 306 | 12 (3 ⚠) | 3 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.57× (z +18.8) | [[Dinaciclib (drug)]] 0.5 µM 0.513× (z -13.3) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 311 | 11 (2 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.09× (z +18.7) | [[Dinaciclib (drug)]] 5 µM 0.340× (z -17.3) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 482 | 9 (1 ⚠) | 3 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.59× (z +15.8) | [[Dinaciclib (drug)]] 5 µM 0.289× (z -19.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 181 | 12 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.75× (z +19.8) | — |
| [[LS 180 (line)]] | wt | 370 | 9 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.15× (z +15.9) | [[Dinaciclib (drug)]] 5 µM 0.276× (z -17.2) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 362 | 10 (2 ⚠) | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.93× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.107× (z -24.2) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 330 | 9 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +17.5) | [[Dinaciclib (drug)]] 0.5 µM 0.350× (z -13.7) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 123 | 11 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.60× (z +15.4) | — |
| [[HS-578T (line)]] | alt | 217 | 9 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +19.5) | [[Dinaciclib (drug)]] 0.5 µM 0.502× (z -9.6) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 221 | 8 (2 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +27.2) | [[Dinaciclib (drug)]] 0.5 µM 0.443× (z -12.1) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 216 | 8 (2 ⚠) | 3 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.14× (z +16.3) | [[Dinaciclib (drug)]] 5 µM 0.487× (z -9.8) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 188 | 9 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +24.6) | [[Dinaciclib (drug)]] 0.05 µM 0.412× (z -12.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 242 | 8 (1 ⚠) | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.74× (z +17.1) | [[Dinaciclib (drug)]] 5 µM 0.254× (z -22.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 215 | 8 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +27.2) | [[Dinaciclib (drug)]] 5 µM 0.237× (z -20.0) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 260 | 7 (1 ⚠) | 3 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.28× (z +18.5) | [[Dinaciclib (drug)]] 0.5 µM 0.436× (z -13.0) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 222 | 7 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +15.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.423× (z -12.5) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 204 | 9 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.96× (z +17.3) | — |
| [[HCT15 (line)]] | alt | 264 | 7 (1 ⚠) | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.02× (z +14.8) | [[Dinaciclib (drug)]] 0.5 µM 0.431× (z -11.2) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 276 | 7 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +12.0) | [[Dinaciclib (drug)]] 0.5 µM 0.418× (z -10.9) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 271 | 8 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +22.3) | [[Dinaciclib (drug)]] 0.5 µM 0.599× (z -8.7) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 166 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +16.6) | — |
| [[NCI-H1573 (line)]] | alt | 396 | 4 (2 ⚠) | 4 (4 ⚠) | [[Digitoxin (drug)]] 5 µM 3.59× (z +16.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.76× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.104× (z -27.8) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 586 | 3 (1 ⚠) | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +13.8) | [[Dinaciclib (drug)]] 0.5 µM 0.238× (z -22.3) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 429 | 4 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +12.0) | [[Dinaciclib (drug)]] 0.5 µM 0.267× (z -19.7) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 191 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +15.6) | — |
| [[SW1417 (line)]] | alt | 246 | 4 (1 ⚠) | 4 (4 ⚠) | [[Digitoxin (drug)]] 5 µM 1.95× (z +11.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.87× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.508× (z -10.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 166 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +21.2) | — |
| [[CFPAC-1 (line)]] | alt | 359 | 3 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +13.6) | [[Dinaciclib (drug)]] 5 µM 0.310× (z -14.0) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 195 | 7 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.52× (z +15.0) | — |
| [[AsPC-1 (line)]] | alt | 674 | 1 | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +19.8) | [[Dinaciclib (drug)]] 5 µM 0.192× (z -23.0) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 245 | 3 | 3 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.57× (z +13.9) | [[Dinaciclib (drug)]] 0.5 µM 0.400× (z -13.5) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 316 | 4 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +18.9) | [[Dinaciclib (drug)]] 0.5 µM 0.413× (z -10.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 386 | 2 | 4 (4 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.74× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.198× (z -25.4) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 211 | 5 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.55× (z +14.7) | [[Dinaciclib (drug)]] 0.05 µM 0.524× (z -9.3) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 517 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.230× (z -17.7) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 178 | 5 (1 ⚠) | 0 | [[Bortezomib (drug)]] 0.05 µM 2.26× (z +11.3) | — |
| [[A498 (line)]] | wt | 268 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +19.8) | [[Dinaciclib (drug)]] 0.5 µM 0.444× (z -10.4) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 238 | 3 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.38× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.0482× (z -38.6) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 279 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.325× (z -12.1) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 251 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.284× (z -9.3) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 159 | 0 | 1 | — | [[Arbutin (drug)]] 5 µM 0.105× (z -10.9) |
| [[NCI-H2122 (line)]] | alt | 312 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 307 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 233 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 262 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8750), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPBP1]] | +0.54 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[TMCC1]] | +0.52 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[STRN3]] | +0.49 | +0.45 / +0.48 | both halves | 3e-05 | same gene group; STRING 998 |
| [[PAK1]] | +0.47 | +0.49 / +0.42 | both halves | 4e-05 |  |
| [[PSMA2]] | +0.47 | +0.40 / +0.47 | both halves | 5e-05 |  |
| [[MYO6]] | +0.47 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[MAP7]] | +0.47 | +0.48 / +0.39 | both halves | 6e-05 |  |
| [[LSM10]] | +0.47 | +0.41 / +0.35 | both halves | 1e-04 |  |
| [[LRRFIP2]] | +0.47 | +0.51 / +0.39 | both halves | 6e-05 |  |
| [[UBE2R2]] | +0.47 | +0.45 / +0.41 | both halves | 4e-05 |  |
| [[CHMP2B]] | +0.46 | +0.38 / +0.47 | both halves | 6e-05 |  |
| [[CLDN4]] | +0.46 | +0.38 / +0.45 | both halves | 6e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF17]] | -0.52 | -0.32 / -0.55 | both halves | 2e-04 |  |
| [[BAG6]] | -0.49 | -0.49 / -0.32 | both halves | 2e-04 |  |
| [[ZNF256]] | -0.47 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[RAB11B]] | -0.47 | -0.47 / -0.27 | both halves | 3e-04 |  |
| [[ZNF548]] | -0.46 | -0.38 / -0.43 | both halves | 7e-05 |  |
| [[CA5BP1-1]] | -0.45 | -0.28 / -0.47 | both halves | 3e-04 |  |
| [[EIF4EBP2]] | -0.45 | -0.43 / -0.32 | both halves | 2e-04 |  |
| [[ELK1]] | -0.45 | -0.39 / -0.47 | both halves | 6e-05 |  |
| [[SMU1]] | -0.45 | -0.40 / -0.39 | both halves | 5e-05 |  |
| [[ZNF529]] | -0.45 | -0.28 / -0.44 | both halves | 3e-04 |  |
| [[SSU72]] | -0.44 | -0.33 / -0.44 | both halves | 1e-04 |  |
| [[PRPF8]] | -0.44 | -0.25 / -0.35 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DAPP1]] | B | DAPP1 activity raises SLMAP's level | lines that do not express DAPP1 (39) vs lines expressing it (11) | 1.60× lower at baseline in the lines without DAPP1 | 0.006 | ⚠ within organs, on part of the lines; also absent: SLC6A14, CEACAM6, MUC5B |
| [[MSX1]] | B | MSX1 activity lowers SLMAP's level | lines that do not express MSX1 (6) vs lines expressing it (44) | 1.52× higher at baseline in the lines without MSX1 | 0.051 | ⚠ within organs, on part of the lines; also absent: ANAPC1P4, WDR35, TMCC2; maybe low, not absent |
| [[CLDN4]] | B | CLDN4 activity raises SLMAP's level | lines that do not express CLDN4 (26) vs lines expressing it (24) | 1.45× lower at baseline in the lines without CLDN4 | 0.071 | ⚠ within organs, on part of the lines; also absent: CDH1, SCNN1A, ITGB6 |
| [[DAPP1]] | C | DAPP1 activity weakens SLMAP's drug response | lines that do not express DAPP1 (39) vs lines expressing it (10) | the lines without DAPP1 respond 1.04× as strongly (z diff -0.35); strongest at Bortezomib 0.05 µM: 2.18x vs 1.71x (z diff -2.6) | 0.091 | ⚠ within organs, on part of the lines; also absent: SLC6A14, CEACAM6, MUC5B; target measured in part of the lines; rests on the correction; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **+** arm (projection on the module's main direction 0.303). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-32.4, 33.9); signed map (-45.4, 28.8). **Vector** length 96.7, 39.1% of its response variance represented; |z| ≥ 3 in 1,713 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.2 | +5.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.9 | +18.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.7 | +18.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.4 | +23.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.2 | +2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.2 | +3.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +0.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.4 | +9.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +3.1 | +3.7 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.9 | +0.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.7 | +12.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.6 | +21.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -3.7 | -8.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.3 | -15.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.9 | -0.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.5 | -0.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.1 | -1.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.1 | +1.7 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.1 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | sarcolemma associated protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p14.3 — chr3:57,755,450-57,930,003 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SLAP, KIAA1601 |
| Gene groups (HGNC) | STRIPAK complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14BN4](https://www.uniprot.org/uniprotkb/Q14BN4) (Sarcolemmal membrane-associated protein):

> Associates with the striatin-interacting phosphatase and kinase (STRIPAK) core complex, forming the extended (SIKE1:SLMAP)STRIPAK complex. The (SIKE1:SLMAP)STRIPAK complex dephosphorylates STK3 leading to the inhibition of Hippo signaling and the control of cell growth. May play a role during myoblast fusion (By similarity).

**Summary**, from NCBI Gene [7871](https://www.ncbi.nlm.nih.gov/gene/7871):

> This gene encodes a component of a conserved striatin-interacting phosphatase and kinase complex. Striatin family complexes participate in a variety of cellular processes including signaling, cell cycle control, cell migration, Golgi assembly, and apoptosis. The protein encoded by this gene is a coiled-coil, tail-anchored membrane protein with a single C-terminal transmembrane domain that is posttranslationally inserted into membranes. Mutations in this gene are associated with Brugada …

**Accessions** — [HGNC:16643](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16643) · Entrez [7871](https://www.ncbi.nlm.nih.gov/gene/7871) · UniProt [Q14BN4](https://www.uniprot.org/uniprotkb/Q14BN4) · Ensembl [ENSG00000163681](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163681)

## Data

Gene col 8750: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8750); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8750, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8750]; `tensor/DDL_lfc|DDL_z.npy` [8750]; `embed/gene_vectors.npy` [8750]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8750 or target_col == 8750). Every well: [[SLMAP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLMAP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
