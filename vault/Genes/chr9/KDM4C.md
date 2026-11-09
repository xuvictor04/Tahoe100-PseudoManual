---
symbol: "KDM4C"
type: "gene"
col: 2823
ensembl_id: "ENSG00000107077"
name: "lysine demethylase 4C"
location: "9p24.1"
module: 144
arm: "+"
pooled_cpm: 304.96
n_lines_expressing: 49
n_dd_up: 6
n_dd_down: 21
n_dd_up_clean: 6
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/144"]
generated_by: "tahoemap"
---

# KDM4C

*lysine demethylase 4C* — 9p24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 2.12× (z +7.7, q 9e-12, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.396× (z -17.4, q 0e+00, down in 42 of 43 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 0.594× (z -8.4, q 4e-15, down in 45 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FANK1]] (+0.64, fdr 7e-06), [[LMLN]] (+0.57, fdr 1e-05), [[IPMK]] (+0.55, fdr 1e-05); moves opposite to [[ZNF852]] (-0.53, fdr 6e-05), [[CHST10]] (-0.53, fdr 2e-05), [[ANKRD52]] (-0.49, fdr 6e-05).
> It is in [[Module 144]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2823.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.12×** | +7.7 | 9e-12 | 39/48 (NCI-H460, SNU-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.24×** | +5.9 | 1e-06 | 25/47 (AsPC-1, J82, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[PF-06260933 (drug)]] 5 µM |  | **1.60×** | +4.8 | 3e-04 | 37/47 (A-172, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.25×** | +4.3 | 0.003 | 30/46 (A549, LOX-IMVI, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.25×** | +4.2 | 0.003 | 26/49 (RKO, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cepharanthine (drug)]] 5 µM |  | 1.14× | +3.5 | 0.042 | 11/47 (HOP62, NCI-H23, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.22×** | +3.3 | 0.093 | 25/46 (SW48, RKO, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 1.18× | +3.2 | 0.10 | 20/46 (RKO, HT-29, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 16 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2823.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.396×** | -17.4 | 0e+00 | 42/43 (HCT15, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.397×** | -17.4 | 0e+00 | 46/46 (KATO III, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.353×** | -16.8 | 0e+00 | 46/48 (SK-MEL-2, HCT15, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.413×** | -16.0 | 0e+00 | 43/44 (RPMI-7951, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.548×** | -11.3 | 1e-27 | 42/46 (LOX-IMVI, A549, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.594×** | -8.4 | 4e-15 | 45/47 (MIA PaCa-2, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.659×** | -8.1 | 3e-14 | 41/47 (KATO III, HT-29, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.660×** | -8.1 | 3e-14 | 40/47 (SW480, C32, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.759×** | -7.6 | 1e-12 | 33/47 (C32, SK-MEL-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.677×** | -7.6 | 1e-12 | 38/47 (COLO 205, SW480, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.687×** | -7.3 | 1e-11 | 36/47 (SK-MEL-2, C32, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.704×** | -6.9 | 3e-10 | 35/47 (CFPAC-1, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.705×** | -6.8 | 4e-10 | 37/47 (LOX-IMVI, KATO III, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.754×** | -5.3 | 4e-06 | 30/47 (C32, LOX-IMVI, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **0.773×** | -5.0 | 2e-05 | 30/47 (SW480, KATO III, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.796×** | -4.1 | 0.001 | 30/46 (NCI-H2030, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.813×** | -4.0 | 0.002 | 24/47 (CFPAC-1, NCI-H460, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.815×** | -4.0 | 0.002 | 23/47 (CFPAC-1, HOP62, …) | rises with dose |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.718×** | -3.4 | 0.019 | 27/48 (C32, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.817×** | -3.3 | 0.028 | 23/46 (MIA PaCa-2, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.900× | -2.9 | 0.079 | 6/47 (NCI-H1792, LoVo, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2823. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 363 | 0 | 13 (9 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.267× (z -17.9) ⚠ toxic · without an alert: [[Selinexor (drug)]] 5 µM 0.431× (z -16.8) |
| [[KATO III (line)]] | alt | 435 | 0 | 12 (11 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.272× (z -19.0) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.468× (z -9.5) |
| [[LOX-IMVI (line)]] | wt | 537 | 0 | 11 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.179× (z -20.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.469× (z -9.4) |
| [[SK-MEL-2 (line)]] | alt | 406 | 0 | 11 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0615× (z -30.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.247× (z -18.5) |
| [[SW480 (line)]] | alt | 433 | 0 | 10 (7 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.319× (z -16.2) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.488× (z -10.6) |
| [[A549 (line)]] | wt | 349 | 1 | 8 (6 ⚠) | [[TAK-901 (drug)]] 5 µM 3.41× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.307× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.587× (z -10.8) |
| [[LoVo (line)]] | wt | 382 | 2 | 7 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.57× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.244× (z -17.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[HOP62 (line)]] | alt | 336 | 1 | 7 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 4.61× (z +9.7) | [[Dinaciclib (drug)]] 0.05 µM 0.371× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.436× (z -10.1) |
| [[RPMI-7951 (line)]] | alt | 398 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.185× (z -19.8) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.444× (z -10.3) |
| [[SNU-423 (line)]] | alt | 363 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.279× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.552× (z -12.2) |
| [[SW 900 (line)]] | alt | 334 | 0 | 8 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.326× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[A-172 (line)]] | wt | 231 | 3 (1 ⚠) | 4 (3 ⚠) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.36× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.267× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.532× (z -11.7) |
| [[CFPAC-1 (line)]] | alt | 266 | 0 | 7 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.316× (z -15.3) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.343× (z -14.8) |
| [[HS-578T (line)]] | alt | 346 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.326× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.548× (z -10.9) |
| [[J82 (line)]] | alt | 330 | 1 | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.410× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.559× (z -11.2) |
| [[MIA PaCa-2 (line)]] | alt | 504 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.251× (z -17.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.272× (z -14.2) |
| [[NCI-H1792 (line)]] | alt | 185 | 0 | 7 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.353× (z -18.3) ⚠ cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 405 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.199× (z -19.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HT-29 (line)]] | alt | 388 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.288× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.474× (z -9.8) |
| [[LS 180 (line)]] | wt | 509 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.261× (z -17.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[NCI-H1573 (line)]] | alt | 297 | 0 | 6 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.321× (z -13.7) ⚠ toxic · without an alert: [[Selinexor (drug)]] 5 µM 0.540× (z -11.0) |
| [[NCI-H460 (line)]] | wt | 307 | 1 | 5 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 4.18× (z +10.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.350× (z -14.4) ⚠ toxic |
| [[RKO (line)]] | wt | 316 | 3 (1 ⚠) | 3 (2 ⚠) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +12.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.309× (z -14.9) ⚠ toxic · without an alert: [[Selinexor (drug)]] 5 µM 0.577× (z -10.3) |
| [[C-33 A (line)]] | alt | 251 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.263× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.539× (z -8.5) |
| [[COLO 205 (line)]] | alt | 428 | 2 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.18× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.323× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[H4 (line)]] | wt | 265 | 0 | 5 (4 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.371× (z -10.5) |
| [[Hs 766T (line)]] | wt | 324 | 0 | 5 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.277× (z -15.6) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 387 | 1 | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 5.92× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.274× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[A498 (line)]] | wt | 241 | 1 (1 ⚠) | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.71× (z +10.8) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.5 µM 0.406× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[NCI-H23 (line)]] | alt | 174 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.45× (z +8.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.441× (z -10.8) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 250 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.322× (z -13.9) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 433 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.261× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HCT15 (line)]] | alt | 769 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.105× (z -25.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HEC-1-A (line)]] | alt | 231 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.381× (z -13.8) ⚠ toxic |
| [[SW48 (line)]] | wt | 323 | 2 (1 ⚠) | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.46× (z +8.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +8.5) | [[Dinaciclib (drug)]] 0.05 µM 0.231× (z -13.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 267 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.268× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[AN3 CA (line)]] | alt | 351 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.345× (z -9.2) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 135 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +16.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.433× (z -10.8) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 314 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.223× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[PANC-1 (line)]] | alt | 131 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.20× (z +9.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.402× (z -13.0) ⚠ toxic |
| [[SW1417 (line)]] | alt | 221 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.367× (z -12.4) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 190 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.497× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SHP-77 (line)]] | alt | 186 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.488× (z -8.5) ⚠ cell-cycle shift, explains ~91% of this change |
| [[BT-474 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 319 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 68.4 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 361 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 200 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 273 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 168 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2823), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FANK1]] | +0.64 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[LMLN]] | +0.57 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[IPMK]] | +0.55 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[ZSWIM5]] | +0.53 | +0.51 / +0.43 | both halves | 3e-05 |  |
| [[NSUN6]] | +0.53 | +0.49 / +0.39 | both halves | 5e-05 |  |
| [[RBPJ]] | +0.52 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[LINC01135]] | +0.49 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[TMTC2]] | +0.49 | +0.41 / +0.55 | both halves | 4e-05 |  |
| [[GALK2]] | +0.49 | +0.49 / +0.43 | both halves | 3e-05 |  |
| [[RAPGEF6]] | +0.49 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[KDM5B]] | +0.48 | +0.57 / +0.38 | both halves | 7e-05 | same gene group; pathway: Chromatin modifying enzymes |
| [[DIPK2A]] | +0.48 | +0.50 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF852]] | -0.53 | -0.39 / -0.59 | both halves | 6e-05 |  |
| [[CHST10]] | -0.53 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[ANKRD52]] | -0.49 | -0.50 / -0.38 | both halves | 6e-05 |  |
| [[C1orf216]] | -0.47 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[ZNF512]] | -0.46 | -0.36 / -0.44 | both halves | 1e-04 |  |
| [[TRAF6]] | -0.46 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[AP2A2]] | -0.45 | -0.45 / -0.39 | both halves | 5e-05 |  |
| [[PPP5C]] | -0.45 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[CROCCP2]] | -0.44 | -0.36 / -0.41 | both halves | 9e-05 |  |
| [[DFFB]] | -0.44 | -0.44 / -0.37 | both halves | 7e-05 |  |
| [[SPHK2]] | -0.44 | -0.40 / -0.39 | both halves | 6e-05 |  |
| [[C19orf12]] | -0.43 | -0.46 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 144]]; 32 genes; every member is in the + arm (projection on the module's main direction 0.556). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.5, -20.2); signed map (-36.5, 33.3). **Vector** length 118, 46.3% of its response variance represented; |z| ≥ 3 in 1,394 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +7.6 | +4.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +7.2 | +7.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.1 | +2.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.9 | -0.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.4 | +5.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.2 | +4.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.1 | +2.1 |
|  | [[Entrectinib (drug)]] 5 µM |  | +3.0 | +0.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.9 | +4.8 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +2.8 | +3.5 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -9.5 | -17.4 |
|  | [[Selinexor (drug)]] 5 µM |  | -9.1 | -7.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -8.1 | -8.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.3 | -11.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.1 | -3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.0 | -7.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -2.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.1 | -1.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.9 | -2.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.8 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | lysine demethylase 4C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p24.1 — chr9:6,720,863-7,175,648 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GASC1, KIAA0780, TDRD14C; previously JMJD2C |
| Gene groups (HGNC) | PHD finger proteins; Tudor domain containing; Lysine demethylase 4 family |
| Reactome | 10 pathways, smallest: Activated PKN1 stimulates transcription of AR (androgen receptor) regulated genes KLK2 and KLK3; HDMs demethylate histones; M-decay: degradation of maternal mRNAs by maternally stored factors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H3R0](https://www.uniprot.org/uniprotkb/Q9H3R0) (Lysine-specific demethylase 4C):

> Histone demethylase that specifically demethylates 'Lys-9' and 'Lys-36' residues of histone H3, thereby acting as a key regulator of nascent transcription. Does not demethylate histone H3 'Lys-4', H3 'Lys-27' nor H4 'Lys-20'. Demethylates trimethylated H3 'Lys-9' and H3 'Lys-36' residue, while it has no activity on mono- and dimethylated residues.

**Summary**, from NCBI Gene [23081](https://www.ncbi.nlm.nih.gov/gene/23081):

> This gene is a member of the Jumonji domain 2 (JMJD2) family. The encoded protein is a trimethylation-specific demethylase, and converts specific trimethylated histone residues to the dimethylated form. This enzymatic action regulates gene expression and chromosome segregation. Chromosomal aberrations and changes in expression of this gene may be found in tumor cells. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan 2015]

**Accessions** — [HGNC:17071](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17071) · Entrez [23081](https://www.ncbi.nlm.nih.gov/gene/23081) · UniProt [Q9H3R0](https://www.uniprot.org/uniprotkb/Q9H3R0) · Ensembl [ENSG00000107077](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107077)

## Data

Gene col 2823: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2823); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2823, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2823]; `tensor/DDL_lfc|DDL_z.npy` [2823]; `embed/gene_vectors.npy` [2823]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2823 or target_col == 2823). Every well: [[KDM4C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KDM4C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
