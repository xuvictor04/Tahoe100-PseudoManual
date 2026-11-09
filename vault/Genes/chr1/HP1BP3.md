---
symbol: "HP1BP3"
type: "gene"
col: 4814
ensembl_id: "ENSG00000127483"
name: "heterochromatin protein 1 binding protein 3"
location: "1p36.12"
module: 22
arm: "+"
pooled_cpm: 236.14
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 15
n_dd_up_clean: 4
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# HP1BP3

*heterochromatin protein 1 binding protein 3* — 1p36.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.58× (z +12.2, q 2e-31, up in 44 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.47× (z +10.3, q 1e-22, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.689× (z -14.0, q 6e-42, down in 42 of 49 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRC1]] (+0.77, fdr 7e-06), [[DEPDC1]] (+0.72, fdr 7e-06), [[KIF4A]] (+0.72, fdr 7e-06); moves opposite to [[MRPS12]] (-0.66, fdr 1e-04), [[EXOSC4]] (-0.60, fdr 4e-05), [[SLIRP]] (-0.58, fdr 2e-04).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 12 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4814.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.58×** | +12.2 | 2e-31 | 44/49 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.38×** | +12.0 | 7e-31 | 33/48 (RKO, LoVo, …) | top dose only | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.53×** | +11.0 | 8e-26 | 39/44 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.47×** | +10.3 | 1e-22 | 41/48 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change | **1.31×** | +7.2 | 8e-11 | 32/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.30×** | +6.9 | 4e-10 | 31/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.32×** | +6.9 | 5e-10 | 33/45 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.27×** | +6.4 | 1e-08 | 31/48 (KATO III, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.25×** | +5.9 | 2e-07 | 31/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.25×** | +5.9 | 2e-07 | 27/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.53×** | +5.6 | 1e-06 | 33/48 (HEC-1-A, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **1.24×** | +5.5 | 2e-06 | 24/48 (PANC-1, RKO, …) | top dose only | composition shift |
| [[crizotinib (drug)]] 5 µM |  | **1.21×** | +4.9 | 4e-05 | 25/48 (HOP62, SNU-423, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.42×** | +4.6 | 2e-04 | 28/49 (MIA PaCa-2, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **1.37×** | +4.1 | 0.002 | 28/47 (C32, RKO, …) | rises with dose | noisy plate (z scaled) |
| [[Crizotinib (hydrochloride) (drug)]] 5 µM |  | 1.12× | +3.1 | 0.067 | 4/49 (LoVo, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 12 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4814.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.689×** | -14.0 | 6e-42 | 42/49 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.621×** | -12.7 | 2e-34 | 47/48 (NCI-H2347, A-427, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.635×** | -12.1 | 2e-31 | 48/48 (A-427, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.707×** | -9.2 | 4e-18 | 47/48 (A-427, NCI-H2347, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.803×** | -8.2 | 2e-14 | 31/48 (NCI-H2347, HOP62, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.827×** | -7.1 | 9e-11 | 22/48 (HOP62, HEC-1-A, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.767×** | -7.1 | 1e-10 | 38/48 (HEC-1-A, NCI-H2347, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.791×** | -6.2 | 3e-08 | 32/48 (NCI-H2347, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.861× | -5.6 | 1e-06 | 13/48 (HT-29, HepG2/C3A, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.820×** | -5.3 | 7e-06 | 28/48 (Panc 03.27, HepG2/C3A, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~71% of this change | 0.846× | -4.4 | 5e-04 | 18/48 (SW480, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.955× | -4.3 | 9e-04 | 0/50 | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | 0.847× | -4.2 | 1e-03 | 21/48 (A498, HS-578T, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | 0.848× | -4.2 | 0.001 | 23/50 (SW 900, LS 180, …) | top dose only |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.730×** | -4.1 | 0.002 | 28/47 (RPMI-7951, CHP-212, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.737×** | -4.0 | 0.002 | 33/48 (NCI-H460, SW480, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[EX229 (drug)]] 5 µM |  | **0.742×** | -3.9 | 0.003 | 25/48 (HEC-1-A, SW1417, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.749×** | -3.8 | 0.005 | 25/48 (A-427, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.757×** | -3.6 | 0.008 | 22/48 (MIA PaCa-2, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.885× | -3.2 | 0.030 | 11/48 (SNU-1, A-427, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | 0.888× | -3.2 | 0.036 | 15/48 (NCI-H460, SW480, …) | top dose only |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | 0.884× | -3.0 | 0.057 | 10/48 (C32, HEC-1-A, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **0.797×** | -3.0 | 0.068 | 14/48 (hTERT-HPNE, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 0.898× | -2.9 | 0.088 | 3/48 (MIA PaCa-2, NCI-H2030, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4814. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 244 | 8 (7 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.14× (z +15.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.99× (z +14.5) | [[Panobinostat (drug)]] 0.5 µM 0.643× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 183 | 5 (5 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 1.62× (z +12.8) ⚠ cell-cycle shift, explains ~68% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.599× (z -13.6) |
| [[NCI-H1573 (line)]] | alt | 199 | 3 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 1.86× (z +10.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.73× (z +9.3) | [[Panobinostat (drug)]] 0.5 µM 0.540× (z -10.4) |
| [[A-427 (line)]] | wt | 269 | 1 (1 ⚠) | 4 (3 ⚠) | [[Dinaciclib (drug)]] 5 µM 1.70× (z +8.8) ⚠ toxic; transcription drop | [[Selinexor (drug)]] 5 µM 0.628× (z -11.4) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.526× (z -11.1) |
| [[HEC-1-A (line)]] | alt | 214 | 4 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.14× (z +14.9) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 2.41× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.614× (z -13.5) |
| [[SW480 (line)]] | alt | 264 | 4 (3 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.65× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.601× (z -13.8) |
| [[A549 (line)]] | wt | 184 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.34× (z +12.0) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.573× (z -11.8) |
| [[C32 (line)]] | wt | 219 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.12× (z +11.0) ⚠ toxic; transcription drop | [[Selinexor (drug)]] 5 µM 0.618× (z -10.5) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.644× (z -9.6) |
| [[KATO III (line)]] | alt | 215 | 4 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 1.84× (z +10.2) ⚠ cell-cycle shift, explains ~19% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.78× (z +9.6) | — |
| [[LoVo (line)]] | wt | 172 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +14.7) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.71× (z +9.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 310 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +12.8) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.05× (z +10.9) | — |
| [[NCI-H2347 (line)]] | alt | 290 | 0 | 4 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.603× (z -12.7) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.543× (z -10.8) |
| [[A-172 (line)]] | wt | 135 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.88× (z +15.5) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 210 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +14.7) ⚠ cell-cycle shift, explains ~68% of this change | [[Panobinostat (drug)]] 5 µM 0.545× (z -8.9) ⚠ cell-cycle shift, explains ~27% of this change |
| [[HS-578T (line)]] | alt | 350 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.622× (z -11.1) |
| [[HT-29 (line)]] | alt | 270 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.78× (z +9.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.565× (z -9.0) |
| [[LOX-IMVI (line)]] | wt | 311 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.563× (z -11.4) |
| [[LS 180 (line)]] | wt | 169 | 2 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 1.96× (z +9.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.90× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.575× (z -11.1) |
| [[NCI-H1792 (line)]] | alt | 192 | 1 (1 ⚠) | 2 | [[Digitoxin (drug)]] 5 µM 1.73× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change | [[Panobinostat (drug)]] 0.5 µM 0.525× (z -10.5) |
| [[SW1417 (line)]] | alt | 208 | 1 | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.86× (z +10.0) | [[Panobinostat (drug)]] 0.5 µM 0.542× (z -9.8) |
| [[CFPAC-1 (line)]] | alt | 197 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.68× (z +8.8) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 214 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +11.9) ⚠ cell-cycle shift, explains ~68% of this change | — |
| [[HepG2_C3A (line)]] | wt | 322 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.520× (z -10.1) |
| [[HOP62 (line)]] | alt | 350 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.620× (z -11.5) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.632× (z -11.1) |
| [[J82 (line)]] | alt | 278 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.660× (z -9.5) ⚠ cell-cycle shift, explains ~54% of this change |
| [[NCI-H2030 (line)]] | alt | 270 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +13.2) ⚠ cell-cycle shift, explains ~68% of this change | [[Panobinostat (drug)]] 5 µM 0.519× (z -8.8) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H23 (line)]] | alt | 291 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +14.5) ⚠ cell-cycle shift, explains ~68% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.652× (z -9.9) |
| [[Panc 03.27 (line)]] | alt | 171 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.77× (z +8.8) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.551× (z -9.1) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SNU-423 (line)]] | alt | 207 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.59× (z +10.1) ⚠ cell-cycle shift, explains ~68% of this change | — |
| [[A498 (line)]] | wt | 175 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +12.3) ⚠ cell-cycle shift, explains ~68% of this change | — |
| [[C-33 A (line)]] | alt | 316 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.664× (z -8.7) |
| [[H4 (line)]] | wt | 240 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.489× (z -11.1) |
| [[HCT15 (line)]] | alt | 248 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.527× (z -11.7) |
| [[Hs 766T (line)]] | wt | 316 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.56× (z +8.7) ⚠ cell-cycle shift, explains ~68% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 265 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.621× (z -9.0) |
| [[RKO (line)]] | wt | 217 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +16.7) ⚠ cell-cycle shift, explains ~68% of this change | — |
| [[RPMI-7951 (line)]] | alt | 268 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +14.0) ⚠ cell-cycle shift, explains ~68% of this change | — |
| [[SHP-77 (line)]] | alt | 231 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.299× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~85% of this change |
| [[SK-MEL-2 (line)]] | alt | 223 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.90× (z +9.5) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 215 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.522× (z -10.1) |
| [[SW 900 (line)]] | alt | 211 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.543× (z -12.1) |
| [[SW48 (line)]] | wt | 284 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.572× (z -10.3) |
| [[AN3 CA (line)]] | alt | 273 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 114 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 190 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 203 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 337 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 282 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 253 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4814), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRC1]] | +0.77 | +0.75 / +0.74 | both halves | 7e-06 |  |
| [[DEPDC1]] | +0.72 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[KIF4A]] | +0.72 | +0.73 / +0.71 | both halves | 7e-06 |  |
| [[TPX2]] | +0.71 | +0.75 / +0.69 | both halves | 7e-06 |  |
| [[BIRC5]] | +0.71 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[TOP2A]] | +0.70 | +0.81 / +0.64 | both halves | 7e-06 |  |
| [[ARHGAP11A]] | +0.68 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[HMGB3]] | +0.68 | +0.65 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[NCAPD2]] | +0.68 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[NUSAP1]] | +0.68 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[PRR11]] | +0.68 | +0.74 / +0.65 | both halves | 7e-06 |  |
| [[ASPM]] | +0.68 | +0.68 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 3 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS12]] | -0.66 | -0.35 / -0.68 | both halves | 1e-04 |  |
| [[EXOSC4]] | -0.60 | -0.42 / -0.59 | both halves | 4e-05 |  |
| [[SLIRP]] | -0.58 | -0.32 / -0.62 | both halves | 2e-04 |  |
| [[MTF1]] | -0.56 | -0.27 / -0.61 | both halves | 3e-04 |  |
| [[NOP10]] ⚠ | -0.55 | -0.26 / -0.68 | both halves | 4e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[NUDT22]] | -0.55 | -0.18 / -0.61 | ⚠ one half (not replicated) | 0.001 |  |
| [[ZNF593]] | -0.54 | -0.30 / -0.59 | both halves | 2e-04 |  |
| [[C16orf91]] | -0.54 | -0.17 / -0.54 | ⚠ one half (not replicated) | 0.001 |  |
| [[IL17RA]] | -0.53 | -0.24 / -0.57 | both halves | 5e-04 |  |
| [[CIAO2B]] | -0.53 | -0.32 / -0.59 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.666). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-39.6, -54.9); signed map (-50.9, -45.0). **Vector** length 128, 44.4% of its response variance represented; |z| ≥ 3 in 1,341 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.53 to 60); *DREAM G2/M down* (control, mean cos +0.60 to 28); *Mitotic Prometaphase* (reactome, mean cos +0.53 to 48).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.4 | +12.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | +9.4 | +12.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.8 | +11.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.3 | +6.9 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | +4.1 | +4.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.1 | +1.2 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +3.1 | +1.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.0 | +0.6 |
|  | [[crizotinib (drug)]] 5 µM |  | +2.8 | +4.9 |
|  | [[RMC-6236 (drug)]] 5 µM |  | +2.8 | +1.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -8.0 | -7.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | -7.2 | -8.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.7 | -14.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~71% of this change | -5.8 | -4.4 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -5.6 | -2.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -5.1 | -3.8 |
|  | [[EX229 (drug)]] 5 µM |  | -4.9 | -3.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.5 | -3.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.5 | -4.0 |
|  | [[Belzutifan (drug)]] 5 µM |  | -4.1 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | heterochromatin protein 1 binding protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.12 — chr1:20,740,266-20,787,323 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HP1-BP74 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5SSJ5](https://www.uniprot.org/uniprotkb/Q5SSJ5) (Heterochromatin protein 1-binding protein 3):

> Component of heterochromatin that maintains heterochromatin integrity during G1/S progression and regulates the duration of G1 phase to critically influence cell proliferative capacity. Mediates chromatin condensation during hypoxia, leading to increased tumor cell viability, radio-resistance, chemo-resistance and self-renewal.

**Summary**, from NCBI Gene [50809](https://www.ncbi.nlm.nih.gov/gene/50809):

> Enables DNA binding activity and nucleosome binding activity. Involved in several processes, including cellular response to hypoxia; heterochromatin organization; and regulation of nucleus size. Located in chromosome and nuclear speck. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24973](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24973) · Entrez [50809](https://www.ncbi.nlm.nih.gov/gene/50809) · UniProt [Q5SSJ5](https://www.uniprot.org/uniprotkb/Q5SSJ5) · Ensembl [ENSG00000127483](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127483)

## Data

Gene col 4814: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4814); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4814, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4814]; `tensor/DDL_lfc|DDL_z.npy` [4814]; `embed/gene_vectors.npy` [4814]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4814 or target_col == 4814). Every well: [[HP1BP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HP1BP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
