---
symbol: "EPS15L1"
type: "gene"
col: 4818
ensembl_id: "ENSG00000127527"
name: "epidermal growth factor receptor pathway substrate 15 like 1"
location: "19p13.11"
module: 72
arm: "+"
pooled_cpm: 52.4
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 6
n_dd_up_clean: 16
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/072"]
generated_by: "tahoemap"
---

# EPS15L1

*epidermal growth factor receptor pathway substrate 15 like 1* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.36× (z +27.3, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.631× (z -13.6, q 2e-39, down in 34 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 0.830× (z -8.5, q 4e-15, down in 20 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (LS 180 0.0741×, SHP-77 0.115×, A-172 0.135×, HCT15 0.114×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (RKO 0.190×, HCT15 0.214×, A-172 0.391×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 3 lines (SNU-423 0.404×, NCI-H460 0.567×, HOP62 0.515×; ⚠ cell-cycle shift, explains ~64% of this change); [[Selinexor (drug)]] 5 µM in 3 lines (A498 0.517×, SK-MEL-2 0.485×, J82 0.576×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANKRD39]] (+0.72, fdr 1e-05), [[RNF216]] (+0.69, fdr 7e-06), [[TMEM161A]] (+0.69, fdr 1e-05); moves opposite to [[CLN5]] (-0.64, fdr 1e-05), [[FAM200B]] (-0.63, fdr 6e-05), [[FMR1]] (-0.59, fdr 1e-05).
> It is in [[Module 072]], a single-armed module (Degradation of DVL).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[AASS]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4818.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.36×** | +27.3 | 0e+00 | 47/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.22×** | +25.3 | 0e+00 | 47/48 (SW480, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.10×** | +23.5 | 0e+00 | 46/48 (SW480, A-172, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.05×** | +21.5 | 0e+00 | 43/48 (LS 180, A498, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.92×** | +20.7 | 0e+00 | 43/48 (LS 180, A498, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.92×** | +20.6 | 0e+00 | 41/48 (LS 180, A498, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.48×** | +12.4 | 3e-33 | 40/48 (NCI-H460, AsPC-1, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.32×** | +8.7 | 2e-16 | 26/48 (A498, HEC-1-A, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.20×** | +8.1 | 3e-14 | 20/48 (PANC-1, HT-29, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.39×** | +7.5 | 4e-12 | 29/48 (LS 180, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **1.26×** | +7.4 | 7e-12 | 25/48 (A-172, A498, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.68×** | +6.4 | 9e-09 | 22/45 (LS 180, A498, …) | all doses, flat | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.22×** | +6.2 | 2e-08 | 23/48 (A498, HS-578T, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.54×** | +5.3 | 4e-06 | 16/48 (A498, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.27×** | +5.3 | 4e-06 | 15/48 (A498, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.17× | +4.9 | 4e-05 | 10/48 (NCI-H2347, LOX-IMVI, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.43×** | +4.4 | 3e-04 | 9/48 (NCI-H460, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.38×** | +4.0 | 0.002 | 5/48 (A-172, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | 1.14× | +3.9 | 0.002 | 9/48 (Hs 766T, SNU-1, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.12× | +3.7 | 0.006 | 7/48 (CHP-212, NCI-H1792, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4818.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (LS 180 0.0741×, SHP-77 0.115×, A-172 0.135×, HCT15 0.114×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (RKO 0.190×, HCT15 0.214×, A-172 0.391×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 3 lines (SNU-423 0.404×, NCI-H460 0.567×, HOP62 0.515×; ⚠ cell-cycle shift, explains ~64% of this change); [[Selinexor (drug)]] 5 µM in 3 lines (A498 0.517×, SK-MEL-2 0.485×, J82 0.576×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.631×** | -13.6 | 2e-39 | 34/45 (NCI-H460, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.728×** | -10.1 | 9e-22 | 31/49 (RKO, HCT15, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.830×** | -8.5 | 4e-15 | 20/48 (A498, SK-MEL-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.795×** | -7.3 | 3e-11 | 23/48 (MIA PaCa-2, AN3 CA, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | 0.853× | -7.3 | 4e-11 | 21/48 (SNU-423, NCI-H460, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.821×** | -6.1 | 1e-07 | 22/41 (LS 180, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | 0.847× | -5.4 | 7e-06 | 19/47 (HCT15, SW 1088, …) | all doses, flat | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.862× | -4.8 | 1e-04 | 15/48 (RPMI-7951, SK-MEL-2, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.817×** | -4.6 | 2e-04 | 18/48 (Hs 766T, A-172, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[AZD-7648 (drug)]] 0.5 µM |  | 0.847× | -3.8 | 0.008 | 9/48 (C-33 A, HOP62, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 0.901× | -3.4 | 0.037 | 14/48 (SNU-1, AN3 CA, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | 0.875× | -3.1 | 0.097 | 10/47 (SW 1271, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[palbociclib (drug)]] 0.05 µM |  | 0.906× | -3.0 | 0.11 | 8/48 (CFPAC-1, SK-MEL-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4818. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 50.8 | 7 (1 ⚠) | 6 (6 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.66× (z +14.8) | [[Dinaciclib (drug)]] 0.05 µM 0.367× (z -14.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 82.7 | 6 | 4 (4 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.78× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.135× (z -23.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 50.7 | 7 | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.92× (z +15.4) | [[Selinexor (drug)]] 5 µM 0.517× (z -10.5) |
| [[HEC-1-A (line)]] | alt | 71.4 | 6 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.21× (z +11.5) | [[Dinaciclib (drug)]] 0.05 µM 0.469× (z -10.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 65.0 | 5 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 4.19× (z +18.5) | [[Dinaciclib (drug)]] 5 µM 0.0741× (z -32.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 84.0 | 5 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.93× (z +13.1) | [[Homoharringtonine (drug)]] 0.5 µM 0.398× (z -11.3) ⚠ cell-cycle shift, explains ~33% of this change |
| [[SW480 (line)]] | alt | 60.4 | 6 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.75× (z +16.7) | [[Dinaciclib (drug)]] 5 µM 0.369× (z -15.9) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 22.7 | 6 | 0 | [[Bortezomib (drug)]] 0.05 µM 5.39× (z +12.1) | — |
| [[HOP62 (line)]] | alt | 40.3 | 4 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.33× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.515× (z -11.4) ⚠ cell-cycle shift, explains ~64% of this change |
| [[Hs 766T (line)]] | wt | 36.6 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 3.39× (z +11.2) | — |
| [[SNU-423 (line)]] | alt | 90.2 | 3 | 3 (3 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.31× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -15.0) ⚠ cell-cycle shift, explains ~64% of this change |
| [[KATO III (line)]] | alt | 38.2 | 4 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.18× (z +11.3) | [[Dinaciclib (drug)]] 0.5 µM 0.327× (z -10.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 45.4 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 2.99× (z +11.3) | — |
| [[NCI-H2347 (line)]] | alt | 34.1 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 2.54× (z +11.1) | — |
| [[Panc 03.27 (line)]] | alt | 80.4 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.72× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.449× (z -9.9) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 60.0 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.60× (z +10.6) | — |
| [[HT-29 (line)]] | alt | 32.9 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.24× (z +11.0) | — |
| [[hTERT-HPNE (line)]] | wt | 45.1 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.94× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.358× (z -8.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 43.3 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.80× (z +12.3) | — |
| [[CFPAC-1 (line)]] | alt | 43.0 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.43× (z +10.2) | — |
| [[H4 (line)]] | wt | 66.7 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.38× (z +12.2) | — |
| [[HCT15 (line)]] | alt | 73.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.114× (z -19.1) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 55.1 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.36× (z +10.3) | [[Digitoxin (drug)]] 5 µM 0.489× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 53.7 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.31× (z +9.7) | [[Dinaciclib (drug)]] 0.05 µM 0.443× (z -8.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 40.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.43× (z +12.2) | — |
| [[A-427 (line)]] | wt | 48.2 | 2 | 0 | [[Belinostat (drug)]] 5 µM 2.47× (z +9.9) | — |
| [[A549 (line)]] | wt | 39.0 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.69× (z +10.5) | — |
| [[AN3 CA (line)]] | alt | 78.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.168× (z -10.8) ⚠ cell-cycle shift, explains ~33% of this change |
| [[C32 (line)]] | wt | 55.8 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.37× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.513× (z -9.4) ⚠ cell-cycle shift, explains ~64% of this change |
| [[J82 (line)]] | alt | 38.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.554× (z -9.4) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.576× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 46.8 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.25× (z +9.0) | — |
| [[RKO (line)]] | wt | 66.7 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.67× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.190× (z -17.4) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 85.6 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.34× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.115× (z -24.0) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 65.7 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.60× (z +10.4) | — |
| [[C-33 A (line)]] | alt | 87.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.360× (z -9.1) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 68.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.165× (z -9.1) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 76.9 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.06× (z +9.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HepG2_C3A (line)]] | wt | 45.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.232× (z -11.2) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 32.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.294× (z -11.9) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 45.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.01× (z +9.0) | — |
| [[SK-MEL-2 (line)]] | alt | 40.1 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.485× (z -9.1) |
| [[SNU-1 (line)]] | wt | 52.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.246× (z -9.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 46.3 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.53× (z +8.5) | — |
| [[SW1417 (line)]] | alt | 43.1 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.36× (z +9.0) | — |
| [[BT-474 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 59.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4818), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD39]] | +0.72 | +0.76 / +0.56 | both halves | 1e-05 |  |
| [[RNF216]] | +0.69 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[TMEM161A]] | +0.69 | +0.75 / +0.55 | both halves | 1e-05 |  |
| [[TANGO2]] | +0.67 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[ANKRD23]] | +0.65 | +0.71 / +0.60 | both halves | 7e-06 |  |
| [[SNX29]] | +0.64 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[PWWP3A]] | +0.64 | +0.68 / +0.50 | both halves | 1e-05 |  |
| [[PSMB3]] | +0.62 | +0.65 / +0.48 | both halves | 2e-05 |  |
| [[DAP3]] | +0.62 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[HTT]] | +0.61 | +0.61 / +0.40 | both halves | 5e-05 |  |
| [[VPS13D]] | +0.61 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[EXOC6B]] | +0.61 | +0.65 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLN5]] | -0.64 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[FAM200B]] | -0.63 | -0.67 / -0.38 | both halves | 6e-05 |  |
| [[FMR1]] | -0.59 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[HMGN1]] | -0.58 | -0.46 / -0.53 | both halves | 2e-05 |  |
| [[CGGBP1]] | -0.58 | -0.59 / -0.33 | both halves | 1e-04 |  |
| [[TRAM2-AS1]] | -0.57 | -0.52 / -0.39 | both halves | 5e-05 |  |
| [[SLC35A5]] | -0.57 | -0.58 / -0.36 | both halves | 1e-04 |  |
| [[ACADM]] | -0.57 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[KBTBD2]] | -0.57 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[RAP2C]] | -0.56 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[TAPT1]] | -0.55 | -0.60 / -0.36 | both halves | 9e-05 |  |
| [[OGFRL1]] | -0.55 | -0.46 / -0.40 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AASS]] | B | AASS activity raises EPS15L1's level | lines that do not express AASS (7) vs lines expressing it (43) | 1.35× lower at baseline in the lines without AASS | 0.069 | ⚠ within organs, on part of the lines; also absent: LINC00159, ZNF391, DISC1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 072]] — Degradation of DVL; 69 genes; every member is in the + arm (projection on the module's main direction 0.676). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-16.2, -8.6); signed map (-27.2, -26.2). **Vector** length 99.9, 24.0% of its response variance represented; |z| ≥ 3 in 1,134 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +10.5 | +20.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +10.3 | +21.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +9.8 | +20.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.6 | +12.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.9 | +27.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.5 | +7.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +4.1 | +3.3 |
|  | [[EX229 (drug)]] 5 µM |  | +3.5 | +4.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +8.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | -9.7 | -7.3 |
|  | [[Selinexor (drug)]] 5 µM |  | -7.4 | -8.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -6.7 | -7.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.5 | -13.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.4 | -4.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | +0.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.8 | -2.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.6 | -1.0 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | -1.5 | -1.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -1.5 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | epidermal growth factor receptor pathway substrate 15 like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:16,355,225-16,472,085 (-) |
| Ensembl biotype | protein_coding |
| Also known as | eps15R |
| Gene groups (HGNC) | EF-hand domain containing |
| Reactome | 7 pathways, smallest: EGFR downregulation; Signaling by EGFR; Cargo recognition for clathrin-mediated endocytosis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBC2](https://www.uniprot.org/uniprotkb/Q9UBC2) (Epidermal growth factor receptor substrate 15-like 1):

> Seems to be a constitutive component of clathrin-coated pits that is required for receptor-mediated endocytosis. Involved in endocytosis of integrin beta-1 (ITGB1) and transferrin receptor (TFR); internalization of ITGB1 as DAB2-dependent cargo but not TFR seems to require association with DAB2.

**Summary**, from NCBI Gene [58513](https://www.ncbi.nlm.nih.gov/gene/58513):

> Enables cadherin binding activity. Predicted to be involved in endocytosis and endosomal transport. Located in membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24634](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24634) · Entrez [58513](https://www.ncbi.nlm.nih.gov/gene/58513) · UniProt [Q9UBC2](https://www.uniprot.org/uniprotkb/Q9UBC2) · Ensembl [ENSG00000127527](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127527)

## Data

Gene col 4818: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4818); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4818, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4818]; `tensor/DDL_lfc|DDL_z.npy` [4818]; `embed/gene_vectors.npy` [4818]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4818 or target_col == 4818). Every well: [[EPS15L1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EPS15L1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
