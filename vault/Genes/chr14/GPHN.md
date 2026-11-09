---
symbol: "GPHN"
type: "gene"
col: 10152
ensembl_id: "ENSG00000171723"
name: "gephyrin"
location: "14q23.3"
module: 200
arm: "+"
pooled_cpm: 336.12
n_lines_expressing: 49
n_dd_up: 35
n_dd_down: 8
n_dd_up_clean: 23
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/200"]
generated_by: "tahoemap"
---

# GPHN

*gephyrin* — 14q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.87× (z +39.4, q 0e+00, up in 47 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.416× (z -21.7, q 0e+00, down in 45 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.746× (z -7.8, q 8e-13, down in 30 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 12 lines (LoVo 0.358×, SW480 0.457×, SW48 0.320×, RKO 0.402×, …); [[Dinaciclib (drug)]] 5 µM in 9 lines (SK-MEL-2 0.119×, PANC-1 0.276×, SW480 0.260×, NCI-H1573 0.253×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (SNU-1 0.118×, PANC-1 0.280×, A-427 0.245×, LOX-IMVI 0.230×, …; ⚠ toxic; transcription drop); [[Vinblastine (sulfate) (drug)]] 5 µM in 2 lines (LS 180 0.477×, LoVo 0.678×); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (LS 180 0.415×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MICOS10]] (+0.57, fdr 1e-05), [[ANKRD17]] (+0.57, fdr 1e-05), [[ACBD6]] (+0.56, fdr 1e-05); moves opposite to [[POLR2J3]] (-0.53, fdr 1e-04), [[TPD52L2]] (-0.52, fdr 1e-05), [[KCTD21]] (-0.52, fdr 3e-05).
> It is in [[Module 200]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[CACHD1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 58 in all, 18 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10152.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.87×** | +39.4 | 0e+00 | 47/47 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.27×** | +20.8 | 0e+00 | 45/47 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.84×** | +16.0 | 0e+00 | 46/47 (HEC-1-A, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.69×** | +13.8 | 2e-41 | 41/47 (CFPAC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.62×** | +12.7 | 4e-35 | 43/47 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.41×** | +12.2 | 5e-32 | 46/48 (C32, SW48, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.45×** | +9.4 | 5e-19 | 39/47 (NCI-H2347, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.44×** | +9.3 | 9e-19 | 38/47 (NCI-H460, A498, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +9.1 | 9e-18 | 27/47 (A498, NCI-H460, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.41×** | +9.0 | 1e-17 | 34/47 (CFPAC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.38×** | +8.5 | 1e-15 | 36/47 (NCI-H2347, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.38×** | +8.4 | 2e-15 | 30/47 (HOP62, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.24×** | +7.9 | 9e-14 | 25/48 (MIA PaCa-2, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.74×** | +7.6 | 8e-13 | 42/47 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.68×** | +7.2 | 3e-11 | 37/47 (C32, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.29×** | +6.7 | 7e-10 | 29/47 (HOP62, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.23×** | +5.1 | 8e-06 | 22/47 (A549, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.45×** | +5.1 | 1e-05 | 30/48 (CFPAC-1, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.44×** | +5.0 | 1e-05 | 37/47 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 9 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10152.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 12 lines (LoVo 0.358×, SW480 0.457×, SW48 0.320×, RKO 0.402×, …); [[Dinaciclib (drug)]] 5 µM in 9 lines (SK-MEL-2 0.119×, PANC-1 0.276×, SW480 0.260×, NCI-H1573 0.253×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (SNU-1 0.118×, PANC-1 0.280×, A-427 0.245×, LOX-IMVI 0.230×, …; ⚠ toxic; transcription drop); [[Vinblastine (sulfate) (drug)]] 5 µM in 2 lines (LS 180 0.477×, LoVo 0.678×); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (LS 180 0.415×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.416×** | -21.7 | 0e+00 | 45/48 (SNU-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.439×** | -20.9 | 0e+00 | 41/44 (SK-MEL-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.684×** | -10.1 | 1e-21 | 38/47 (SW1417, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.670×** | -9.8 | 1e-20 | 31/45 (A-427, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.702×** | -9.0 | 2e-17 | 35/47 (SW1417, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.746×** | -7.8 | 8e-13 | 30/47 (LoVo, SW480, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.949× | -4.3 | 0.001 | 2/49 (MIA PaCa-2, NCI-H23) | inconsistent across doses |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.901× | -3.9 | 0.006 | 3/48 (C-33 A, SW48, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.866× | -3.8 | 0.008 | 16/47 (LoVo, LS 180, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.816×** | -3.6 | 0.017 | 19/47 (LS 180, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.872× | -3.4 | 0.035 | 14/47 (LS 180, COLO 205, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.885× | -3.3 | 0.052 | 14/47 (LS 180, LoVo, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.881× | -3.2 | 0.069 | 16/47 (NCI-H2030, SW480, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **0.802×** | -3.1 | 0.090 | 16/46 (RKO, NCI-H23, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10152. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 308 | 14 (5 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.54× (z +37.1) | [[Dinaciclib (drug)]] 5 µM 0.419× (z -12.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 289 | 12 (7 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +28.6) | [[Dinaciclib (drug)]] 0.5 µM 0.499× (z -10.3) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 247 | 11 (4 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +21.0) | [[Dinaciclib (drug)]] 0.5 µM 0.408× (z -11.2) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 186 | 12 (5 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.70× (z +34.7) | [[Dinaciclib (drug)]] 0.5 µM 0.496× (z -9.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 283 | 10 (3 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.51× (z +33.0) | [[Dinaciclib (drug)]] 5 µM 0.454× (z -11.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 400 | 6 (1 ⚠) | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +24.5) | [[Dinaciclib (drug)]] 5 µM 0.260× (z -27.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.457× (z -16.5) |
| [[SHP-77 (line)]] | alt | 589 | 4 (1 ⚠) | 7 (6 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.12× (z +13.5) | [[Dinaciclib (drug)]] 5 µM 0.391× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.595× (z -9.3) |
| [[A498 (line)]] | wt | 97.0 | 10 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.61× (z +25.1) | — |
| [[C32 (line)]] | wt | 495 | 6 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +22.6) | [[Dinaciclib (drug)]] 0.5 µM 0.406× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.575× (z -9.8) |
| [[HEC-1-A (line)]] | alt | 317 | 7 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.06× (z +38.7) | [[Dinaciclib (drug)]] 0.5 µM 0.463× (z -14.1) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 215 | 10 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.22× (z +23.8) | — |
| [[Panc 03.27 (line)]] | alt | 398 | 6 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +30.9) | [[Dinaciclib (drug)]] 0.5 µM 0.392× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.565× (z -9.8) |
| [[PANC-1 (line)]] | alt | 365 | 6 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.07× (z +44.0) | [[Dinaciclib (drug)]] 5 µM 0.276× (z -27.4) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 491 | 2 | 7 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +21.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.319× (z -21.0) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.534× (z -12.0) |
| [[A-427 (line)]] | wt | 422 | 5 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +18.7) | [[Dinaciclib (drug)]] 0.5 µM 0.245× (z -24.0) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 137 | 8 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.11× (z +26.8) | — |
| [[LoVo (line)]] | wt | 378 | 4 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +21.0) | [[Dinaciclib (drug)]] 0.5 µM 0.290× (z -20.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.358× (z -17.9) |
| [[LS 180 (line)]] | wt | 766 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.244× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 0.477× (z -11.1) |
| [[NCI-H2030 (line)]] | alt | 247 | 6 (3 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +21.4) | [[Dinaciclib (drug)]] 0.5 µM 0.461× (z -10.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 497 | 4 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +15.8) | [[Dinaciclib (drug)]] 5 µM 0.119× (z -32.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.572× (z -8.8) |
| [[SW 900 (line)]] | alt | 267 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +25.9) | — |
| [[SW48 (line)]] | wt | 936 | 4 | 4 (3 ⚠) | [[TAK-901 (drug)]] 0.05 µM 4.13× (z +14.6) | [[Dinaciclib (drug)]] 5 µM 0.162× (z -23.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.320× (z -15.5) |
| [[COLO 205 (line)]] | alt | 229 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.96× (z +28.2) | — |
| [[LOX-IMVI (line)]] | wt | 523 | 4 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +17.8) | [[Dinaciclib (drug)]] 0.5 µM 0.230× (z -21.8) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 484 | 4 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +26.6) | [[Dinaciclib (drug)]] 5 µM 0.253× (z -24.5) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 657 | 5 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +21.0) | [[Dinaciclib (drug)]] 0.5 µM 0.118× (z -31.5) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 315 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +15.2) | [[Dinaciclib (drug)]] 5 µM 0.409× (z -8.8) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 192 | 4 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +27.3) | [[Auranofin (drug)]] 5 µM 0.460× (z -10.9) |
| [[KATO III (line)]] | alt | 275 | 2 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +21.8) | [[Docetaxel (drug)]] 0.05 µM 0.493× (z -10.3) ⚠ transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.527× (z -9.3) |
| [[MIA PaCa-2 (line)]] | alt | 235 | 5 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.40× (z +27.4) | [[Dinaciclib (drug)]] 0.5 µM 0.501× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 575 | 4 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +23.5) | [[Dinaciclib (drug)]] 5 µM 0.366× (z -14.6) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 549 | 3 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +13.0) | [[Auranofin (drug)]] 5 µM 0.402× (z -13.5) |
| [[RPMI-7951 (line)]] | alt | 243 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +21.7) | — |
| [[SNU-423 (line)]] | alt | 229 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +23.0) | [[Dinaciclib (drug)]] 5 µM 0.453× (z -10.2) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 382 | 2 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +16.0) | [[Dinaciclib (drug)]] 5 µM 0.218× (z -24.0) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 144 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +18.9) | — |
| [[J82 (line)]] | alt | 227 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +26.6) | [[Dinaciclib (drug)]] 0.5 µM 0.345× (z -14.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 370 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +29.7) | [[Dinaciclib (drug)]] 5 µM 0.417× (z -12.4) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 438 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +15.2) | [[Dinaciclib (drug)]] 5 µM 0.256× (z -18.5) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 172 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +19.8) | — |
| [[hTERT-HPNE (line)]] | wt | 492 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +16.7) | [[Dinaciclib (drug)]] 0.5 µM 0.167× (z -16.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 159 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +14.8) | — |
| [[AN3 CA (line)]] | alt | 465 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.269× (z -13.4) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 267 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +10.6) | — |
| [[CHP-212 (line)]] | wt | 241 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +10.5) | — |
| [[SW 1271 (line)]] | alt | 324 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.294× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H2122 (line)]] | alt | 336 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 402 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 308 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 71.3 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10152), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MICOS10]] | +0.57 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[ANKRD17]] | +0.57 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[ACBD6]] | +0.56 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[MYCBP2]] | +0.55 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[UVRAG]] | +0.55 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[PTPRG]] | +0.55 | +0.57 / +0.43 | both halves | 3e-05 |  |
| [[MEIS2]] | +0.54 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[SLC12A2-DT]] | +0.53 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[DNPH1]] | +0.53 | +0.38 / +0.49 | both halves | 6e-05 |  |
| [[TBC1D5]] | +0.53 | +0.44 / +0.48 | both halves | 3e-05 |  |
| [[REV3L]] | +0.53 | +0.59 / +0.39 | both halves | 5e-05 |  |
| [[IMMP2L]] | +0.53 | +0.40 / +0.56 | both halves | 5e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR2J3]] | -0.53 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[TPD52L2]] | -0.52 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[KCTD21]] | -0.52 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[LYSMD4]] | -0.52 | -0.36 / -0.41 | both halves | 1e-04 |  |
| [[FCHSD1]] | -0.51 | -0.57 / -0.39 | both halves | 5e-05 |  |
| [[ORMDL3]] | -0.50 | -0.53 / -0.38 | both halves | 7e-05 |  |
| [[CNEP1R1]] | -0.50 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[GGCX]] | -0.49 | -0.57 / -0.26 | both halves | 4e-04 |  |
| [[HIF1AN]] | -0.49 | -0.50 / -0.32 | both halves | 2e-04 |  |
| [[F11R]] | -0.48 | -0.52 / -0.37 | both halves | 8e-05 |  |
| [[MARF1]] | -0.47 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[ABTB1]] | -0.47 | -0.49 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CACHD1]] | B | CACHD1 activity raises GPHN's level | lines that do not express CACHD1 (7) vs lines expressing it (43) | 1.75× lower at baseline in the lines without CACHD1 | 0.033 | ⚠ within organs, on part of the lines; also absent: KCNK15-AS1 |
| [[TOP2A]] | B | TOP2A activity lowers GPHN's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.0% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CXCL3]] | B | CXCL3 activity lowers GPHN's level | lines that do not express CXCL3 (14) vs lines expressing it (36) | 1.53× higher at baseline in the lines without CXCL3 | 0.066 | ⚠ within organs, on part of the lines; also absent: MGLL, SPTLC3, PCED1B |
| [[NFIA]] | B | NFIA activity raises GPHN's level | lines that do not express NFIA (11) vs lines expressing it (39) | 1.67× lower at baseline in the lines without NFIA | 0.098 | ⚠ within organs, on part of the lines; also absent: CRACD, TSPAN33, PCAT7; maybe low, not absent |
| [[CXCL3]] | C | CXCL3 activity weakens GPHN's drug response | lines that do not express CXCL3 (14) vs lines expressing it (34) | the lines without CXCL3 respond 1.01× as strongly (z diff -1.20); rises at some drug-doses, falls at others (55% from rises): Dinaciclib 0.5 µM: 0.33x vs 0.45x (z diff -2.8); Dinaciclib 5 µM: 0.33x vs 0.48x (z diff -2.5); Homoharringtonine 5 µM: 2.31x vs 3.25x (z diff -1.8) | 0.069 | ⚠ within organs, on part of the lines; also absent: MGLL, SPTLC3, PCED1B; target measured in part of the lines; rises at some drug-doses, falls at others; rests on the correction; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 200]]; 16 genes; every member is in the + arm (projection on the module's main direction 0.589). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-16.3, 16.2); signed map (24.9, -36.3). **Vector** length 133, 50.3% of its response variance represented; |z| ≥ 3 in 1,913 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +10.4 | +12.7 |
|  | [[EX229 (drug)]] 5 µM |  | +6.7 | +7.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +6.6 | +9.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +5.9 | +6.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.7 | +20.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +5.6 | +5.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | +5.4 | +4.6 |
|  | [[venetoclax (drug)]] 5 µM |  | +5.4 | +4.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +5.2 | +4.3 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -9.3 | -2.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -8.6 | -7.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -8.0 | +2.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.6 | -9.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | -5.7 | -10.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -4.5 | -1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -4.3 | -3.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.1 | -2.8 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -3.6 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | gephyrin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q23.3 — chr14:66,507,407-67,181,803 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1385, GEPH, GPH |
| Gene groups (HGNC) | Molybdenum cofactor synthesis proteins |
| Hallmark sets | ADIPOGENESIS |
| Reactome | 3 pathways, smallest: Molybdenum cofactor biosynthesis; Metabolism of water-soluble vitamins and cofactors; Metabolism of vitamins and cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NQX3](https://www.uniprot.org/uniprotkb/Q9NQX3) (Gephyrin):

> Microtubule-associated protein involved in membrane protein-cytoskeleton interactions. It is thought to anchor the inhibitory glycine receptor (GLYR) to subsynaptic microtubules (By similarity). Acts as a major instructive molecule at inhibitory synapses, where it also clusters GABA type A receptors.; Also has a catalytic activity and catalyzes two steps in the biosynthesis of the molybdenum cofactor. In the first step, molybdopterin is adenylated. Subsequently, molybdate is inserted into …

**Summary**, from NCBI Gene [10243](https://www.ncbi.nlm.nih.gov/gene/10243):

> This gene encodes a neuronal assembly protein that anchors inhibitory neurotransmitter receptors to the postsynaptic cytoskeleton via high affinity binding to a receptor subunit domain and tubulin dimers. In nonneuronal tissues, the encoded protein is also required for molybdenum cofactor biosynthesis. Mutations in this gene may be associated with the neurological condition hyperplexia and also lead to molybdenum cofactor deficiency. Numerous alternatively spliced transcript variants encoding …

**Accessions** — [HGNC:15465](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15465) · Entrez [10243](https://www.ncbi.nlm.nih.gov/gene/10243) · UniProt [Q9NQX3](https://www.uniprot.org/uniprotkb/Q9NQX3) · Ensembl [ENSG00000171723](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171723)

## Data

Gene col 10152: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10152); `tables/drug_effects.parquet` (72 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10152, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10152]; `tensor/DDL_lfc|DDL_z.npy` [10152]; `embed/gene_vectors.npy` [10152]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10152 or target_col == 10152). Every well: [[GPHN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GPHN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
