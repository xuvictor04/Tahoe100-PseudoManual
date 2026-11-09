---
symbol: "TPTEP2-CSNK1E"
type: "gene"
col: 16041
ensembl_id: "ENSG00000283900"
name: "TPTEP2-CSNK1E readthrough"
location: "22q13.1"
module: 28
arm: "-"
pooled_cpm: 92.57
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 32
n_dd_up_clean: 6
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# TPTEP2-CSNK1E

*TPTEP2-CSNK1E readthrough* — 22q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.85× (z +15.1, q 0e+00, up in 44 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (15 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.369× (z -16.7, q 0e+00, down in 46 of 48 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.424× (z -14.9, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RABGEF1]] (+0.71, fdr 7e-06), [[PDE6D]] (+0.68, fdr 2e-05), [[TPT1-AS1]] (+0.68, fdr 7e-06); moves opposite to [[NBN]] (-0.69, fdr 7e-06), [[SLX4IP]] (-0.66, fdr 7e-06), [[DDX1]] (-0.64, fdr 7e-06).
> It sits in the **-** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16041.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +15.1 | 0e+00 | 44/49 (NCI-H460, RKO, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +8.3 | 4e-14 | 38/48 (HOP62, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +5.4 | 1e-05 | 29/50 (RKO, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.28×** | +4.3 | 0.002 | 27/48 (SW1417, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.26×** | +4.0 | 0.006 | 23/48 (A498, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.23×** | +3.5 | 0.041 | 20/48 (A498, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.22×** | +3.5 | 0.041 | 22/49 (A-172, SW1417, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.15× | +3.4 | 0.056 | 16/48 (A-172, KATO III, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.20× | +3.2 | 0.10 | 16/47 (SW48, NCI-H2030, …) | rises with dose | low cells (technical?) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 1.20× | +3.1 | 0.11 | 14/49 (NCI-H2347, HepG2/C3A, …) | inconsistent across doses |  |
| [[ULK-101 (drug)]] 0.05 µM |  | 1.21× | +3.1 | 0.11 | 14/49 (A-427, PANC-1, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.13× | +3.0 | 0.12 | 8/48 (A549, SW 900, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 16 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 16041.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.369×** | -16.7 | 0e+00 | 46/48 (HEC-1-A, A-172, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.424×** | -14.9 | 0e+00 | 44/48 (HEC-1-A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.434×** | -14.5 | 1e-45 | 42/49 (NCI-H23, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.204×** | -14.5 | 3e-45 | 47/49 (HEC-1-A, SW 900, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.429×** | -14.2 | 1e-43 | 42/43 (NCI-H1573, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.570×** | -13.9 | 9e-42 | 42/48 (HEC-1-A, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.464×** | -12.9 | 6e-36 | 43/47 (LoVo, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.512×** | -11.7 | 1e-29 | 46/48 (C32, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.558×** | -10.2 | 2e-22 | 43/48 (LS 180, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.335×** | -10.0 | 1e-21 | 41/48 (HEC-1-A, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.596×** | -9.0 | 9e-18 | 41/48 (COLO 205, HOP62, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.575×** | -8.9 | 2e-17 | 33/45 (NCI-H23, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.657×** | -7.3 | 1e-11 | 38/48 (RPMI-7951, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.675×** | -6.9 | 3e-10 | 41/48 (C32, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.681×** | -6.7 | 8e-10 | 39/48 (RPMI-7951, SK-MEL-2, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.736×** | -5.2 | 8e-06 | 29/48 (SK-MEL-2, MIA PaCa-2, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.590×** | -4.8 | 4e-05 | 30/48 (LoVo, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.595×** | -4.7 | 6e-05 | 29/49 (SK-MEL-2, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.641×** | -4.1 | 0.001 | 26/48 (MIA PaCa-2, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.642×** | -4.0 | 0.001 | 27/48 (Hs 766T, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.664×** | -3.7 | 0.004 | 20/48 (MIA PaCa-2, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.822×** | -3.2 | 0.023 | 19/48 (LoVo, NCI-H23, …) | all doses, flat |  |
| [[EX229 (drug)]] 5 µM |  | **0.704×** | -3.2 | 0.026 | 19/48 (MIA PaCa-2, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16041. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 156 | 0 | 10 (6 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.111× (z -21.9) |
| [[HOP62 (line)]] | alt | 96.9 | 2 | 8 (6 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +11.0) | [[Digitoxin (drug)]] 5 µM 0.280× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.355× (z -10.0) |
| [[A-172 (line)]] | wt | 65.6 | 1 | 8 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +11.6) | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -19.5) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.222× (z -14.6) |
| [[BT-474 (line)]] | alt | 113 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -16.9) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.343× (z -10.9) |
| [[HEC-1-A (line)]] | alt | 100 | 1 | 8 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.75× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -21.6) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.272× (z -15.7) |
| [[MIA PaCa-2 (line)]] | alt | 115 | 1 | 8 (6 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.87× (z +9.7) | [[Niclosamide (olamine) (drug)]] 5 µM 0.204× (z -16.5) ⚠ toxic · without an alert: [[PH-797804 (drug)]] 5 µM 0.106× (z -12.7) |
| [[PANC-1 (line)]] | alt | 77.4 | 1 | 8 (6 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +13.0) | [[Digitoxin (drug)]] 5 µM 0.398× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.428× (z -10.6) |
| [[SK-MEL-2 (line)]] | alt | 246 | 0 | 9 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.146× (z -20.7) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.416× (z -9.8) |
| [[SNU-423 (line)]] | alt | 87.5 | 1 | 8 (6 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -15.0) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.131× (z -9.7) |
| [[LoVo (line)]] | wt | 155 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.199× (z -18.7) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.175× (z -11.0) |
| [[NCI-H23 (line)]] | alt | 110 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0734× (z -30.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.346× (z -12.2) |
| [[Panc 03.27 (line)]] | alt | 97.2 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.207× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.295× (z -12.2) |
| [[SW480 (line)]] | alt | 111 | 3 | 5 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.77× (z +10.2) | [[Harringtonine (drug)]] 5 µM 0.377× (z -11.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.420× (z -10.8) |
| [[LS 180 (line)]] | wt | 92.1 | 0 | 7 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.319× (z -12.5) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.171× (z -10.1) |
| [[NCI-H1573 (line)]] | alt | 223 | 1 | 6 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.74× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.106× (z -25.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.445× (z -9.7) |
| [[CFPAC-1 (line)]] | alt | 97.6 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.318× (z -12.7) |
| [[Hs 766T (line)]] | wt | 133 | 1 | 5 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +12.9) | [[Docetaxel (drug)]] 0.05 µM 0.262× (z -12.7) ⚠ transcription drop; cell-cycle shift, explains ~56% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.376× (z -9.2) |
| [[HS-578T (line)]] | alt | 70.3 | 2 | 4 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.53× (z +11.9) | [[Harringtonine (drug)]] 0.5 µM 0.245× (z -12.8) |
| [[LOX-IMVI (line)]] | wt | 57.5 | 0 | 6 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.257× (z -12.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.300× (z -11.7) |
| [[NCI-H460 (line)]] | wt | 32.3 | 3 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +14.8) | [[Harringtonine (drug)]] 5 µM 0.368× (z -9.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.394× (z -9.1) |
| [[RPMI-7951 (line)]] | alt | 72.3 | 1 | 5 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +11.3) | [[Dinaciclib (drug)]] 0.5 µM 0.155× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.114× (z -9.1) |
| [[A-427 (line)]] | wt | 72.4 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -21.4) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.186× (z -9.0) |
| [[A498 (line)]] | wt | 62.4 | 1 | 4 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +12.2) | [[Homoharringtonine (drug)]] 5 µM 0.375× (z -12.5) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.270× (z -11.8) |
| [[A549 (line)]] | wt | 55.7 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -19.1) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.244× (z -13.4) |
| [[C-33 A (line)]] | alt | 161 | 1 | 4 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.83× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.0877× (z -23.8) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.164× (z -9.6) |
| [[COLO 205 (line)]] | alt | 95.8 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.249× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.362× (z -9.6) |
| [[hTERT-HPNE (line)]] | wt | 79.3 | 0 | 5 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.205× (z -11.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.279× (z -9.6) |
| [[J82 (line)]] | alt | 55.2 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -11.6) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.307× (z -11.4) |
| [[SW 900 (line)]] | alt | 77.7 | 1 | 4 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.244× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.0764× (z -11.6) |
| [[AsPC-1 (line)]] | alt | 108 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +10.9) | [[Homoharringtonine (drug)]] 0.5 µM 0.344× (z -10.8) |
| [[H4 (line)]] | wt | 75.3 | 2 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.54× (z +9.3) | [[Dinaciclib (drug)]] 0.05 µM 0.220× (z -9.8) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 71.7 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.85× (z +8.9) | [[Homoharringtonine (drug)]] 0.5 µM 0.364× (z -10.3) |
| [[KATO III (line)]] | alt | 86.7 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.278× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.395× (z -10.4) |
| [[NCI-H2030 (line)]] | alt | 99.5 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.03× (z +9.6) | [[Harringtonine (drug)]] 5 µM 0.290× (z -11.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.392× (z -9.0) |
| [[HCT15 (line)]] | alt | 142 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.228× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[NCI-H1792 (line)]] | alt | 47.5 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.169× (z -13.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.337× (z -8.9) |
| [[NCI-H2347 (line)]] | alt | 69.9 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -14.0) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.198× (z -8.6) |
| [[RKO (line)]] | wt | 95.5 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.00× (z +13.6) | [[Dinaciclib (drug)]] 0.5 µM 0.330× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SHP-77 (line)]] | alt | 72.7 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.261× (z -12.0) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 65.2 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.02× (z +11.3) | [[PH-797804 (drug)]] 5 µM 0.0622× (z -10.5) |
| [[AN3 CA (line)]] | alt | 79.6 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0640× (z -14.7) |
| [[CHP-212 (line)]] | wt | 54.5 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.127× (z -9.8) |
| [[SW 1088 (line)]] | alt | 87.9 | 0 | 1 | — | [[Dexamethasone (drug)]] 0.05 µM 0.0835× (z -8.5) |
| [[SW1417 (line)]] | alt | 54.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +10.8) | — |
| [[SW48 (line)]] | wt | 77.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.286× (z -8.9) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 69.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 99.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 76.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 79.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16041), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*43 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RABGEF1]] | +0.71 | +0.62 / +0.75 | both halves | 7e-06 |  |
| [[PDE6D]] | +0.68 | +0.48 / +0.71 | both halves | 2e-05 |  |
| [[TPT1-AS1]] | +0.68 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[TMEM165]] | +0.65 | +0.61 / +0.66 | both halves | 7e-06 | STRING 519 |
| [[CERS5]] | +0.63 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[CCDC168]] | +0.63 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[ORMDL2]] | +0.63 | +0.44 / +0.68 | both halves | 3e-05 |  |
| [[DNAJC5]] | +0.62 | +0.56 / +0.71 | both halves | 1e-05 |  |
| [[TOR1B]] | +0.60 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[TTLL3]] | +0.60 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[ZFC3H1]] | +0.60 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[NFATC2IP]] | +0.60 | +0.61 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*57 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NBN]] | -0.69 | -0.68 / -0.68 | both halves | 7e-06 |  |
| [[SLX4IP]] | -0.66 | -0.64 / -0.66 | both halves | 7e-06 |  |
| [[DDX1]] | -0.64 | -0.58 / -0.70 | both halves | 7e-06 |  |
| [[PABIR1]] | -0.63 | -0.61 / -0.62 | both halves | 7e-06 |  |
| [[ZNF280D]] | -0.63 | -0.58 / -0.68 | both halves | 7e-06 |  |
| [[N6AMT1]] | -0.63 | -0.57 / -0.59 | both halves | 1e-05 |  |
| [[PIGO]] | -0.63 | -0.44 / -0.66 | both halves | 3e-05 |  |
| [[C2CD5]] | -0.63 | -0.60 / -0.61 | both halves | 7e-06 |  |
| [[DLD]] | -0.62 | -0.55 / -0.68 | both halves | 1e-05 |  |
| [[ZMYM4]] | -0.62 | -0.57 / -0.65 | both halves | 1e-05 |  |
| [[NUDT12]] | -0.62 | -0.63 / -0.60 | both halves | 7e-06 |  |
| [[EXOSC10]] | -0.61 | -0.46 / -0.69 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TPTEP2-CSNK1E's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.4% of all compounds | 0.026 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers TPTEP2-CSNK1E's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **-** arm (projection on the module's main direction -0.553). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-19.0, 1.4); signed map (-16.1, 16.6). **Vector** length 112, 39.5% of its response variance represented; |z| ≥ 3 in 1,390 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.3 | +15.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +8.0 | +8.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +5.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.9 | +0.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.8 | +0.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.5 | +2.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.8 | +0.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.5 | -0.0 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.1 | -14.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.0 | -14.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -6.9 | -16.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | -6.9 | -14.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | -6.7 | -13.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.4 | -10.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -5.1 | -5.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.9 | +0.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.9 | -6.9 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.8 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | TPTEP2-CSNK1E readthrough |
| Locus type | readthrough (other) |
| Location | 22q13.1 — chr22:38,291,918-38,398,522 (-) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [102800317](https://www.ncbi.nlm.nih.gov/gene/102800317):

> This locus represents naturally occurring readthrough transcription between the neighboring LOC400927 (transmembrane phosphoinositide 3-phosphatase and tensin homolog 2 pseudogene) and CSNK1E (casein kinase I isoform epsilon) genes on chromosome 22. The readthrough transcript encodes the same protein as the downstream gene product (casein kinase I isoform epsilon). [provided by RefSeq, Feb 2014]

**Accessions** — [HGNC:53829](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53829) · Entrez [102800317](https://www.ncbi.nlm.nih.gov/gene/102800317) · Ensembl [ENSG00000283900](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000283900)

## Data

Gene col 16041: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16041); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16041, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16041]; `tensor/DDL_lfc|DDL_z.npy` [16041]; `embed/gene_vectors.npy` [16041]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16041 or target_col == 16041). Every well: [[TPTEP2-CSNK1E — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TPTEP2-CSNK1E.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
