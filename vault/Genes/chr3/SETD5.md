---
symbol: "SETD5"
type: "gene"
col: 9603
ensembl_id: "ENSG00000168137"
name: "SET domain containing 5"
location: "3p25.3"
module: 3
arm: "+"
pooled_cpm: 473.05
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 19
n_dd_up_clean: 7
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# SETD5

*SET domain containing 5* — 3p25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.76× (z +18.0, q 0e+00, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.392× (z -23.3, q 0e+00, down in 44 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.603× (z -18.6, q 0e+00, down in 46 of 49 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDC27]] (+0.65, fdr 7e-06), [[NRTN]] (+0.63, fdr 3e-05), [[CCDC110]] (+0.59, fdr 2e-04); moves opposite to [[ELK4]] (-0.58, fdr 5e-05), [[RSC1A1]] (-0.58, fdr 3e-05), [[RBM12]] (-0.54, fdr 3e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9603.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.76×** | +18.0 | 0e+00 | 48/49 (HEC-1-A, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.74×** | +13.6 | 7e-40 | 47/48 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.63×** | +12.6 | 3e-34 | 40/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.59×** | +11.9 | 1e-30 | 41/48 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.32×** | +10.1 | 4e-22 | 31/48 (PANC-1, A549, …) | top dose only | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.36×** | +7.6 | 3e-12 | 31/47 (NCI-H460, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.30×** | +6.8 | 8e-10 | 33/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.60×** | +6.3 | 2e-08 | 28/38 (NCI-H1573, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.27×** | +6.3 | 2e-08 | 32/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.28×** | +6.2 | 4e-08 | 31/48 (PANC-1, A-427, …) | top dose only | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.22×** | +5.2 | 9e-06 | 27/48 (A498, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | 1.17× | +4.0 | 0.003 | 22/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 1.11× | +3.9 | 0.004 | 2/48 (SW480, LS 180) | rises with dose |  |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 1.15× | +3.5 | 0.022 | 3/48 (HepG2/C3A, Hs 766T, …) | inconsistent across doses | plate-row cell shift |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.20×** | +3.4 | 0.027 | 22/49 (MIA PaCa-2, LoVo, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | 1.14× | +3.2 | 0.047 | 9/49 (AN3 CA, C-33 A, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.13× | +3.1 | 0.057 | 12/48 (A498, C32, …) | rises with dose |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.13× | +3.1 | 0.057 | 8/49 (NCI-H460, PANC-1, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 17 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9603.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.392×** | -23.3 | 0e+00 | 44/44 (HEC-1-A, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.444×** | -21.0 | 0e+00 | 48/49 (NCI-H2347, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.603×** | -18.6 | 0e+00 | 46/49 (A-172, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.591×** | -13.1 | 4e-37 | 45/47 (MIA PaCa-2, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.636×** | -11.7 | 1e-29 | 42/48 (SK-MEL-2, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.684×** | -9.9 | 6e-21 | 42/48 (SK-MEL-2, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.685×** | -9.8 | 1e-20 | 48/48 (MIA PaCa-2, HOP62, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.776×** | -9.3 | 1e-18 | 37/48 (A-172, HEC-1-A, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.703×** | -8.8 | 1e-16 | 37/48 (A-172, SNU-423, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.810×** | -7.7 | 6e-13 | 28/48 (J82, NCI-H2347, …) | top dose only | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.726×** | -7.7 | 9e-13 | 31/45 (NCI-H2347, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.749×** | -7.5 | 3e-12 | 35/48 (SK-MEL-2, SW 900, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.750×** | -7.5 | 4e-12 | 37/48 (A549, HEC-1-A, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.754×** | -7.1 | 7e-11 | 36/50 (A-172, SNU-423, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.756×** | -7.0 | 1e-10 | 35/48 (NCI-H2347, NCI-H1573, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.793×** | -5.1 | 9e-06 | 30/48 (PANC-1, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.898× | -3.9 | 0.003 | 4/48 (A549, HOP62, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.874× | -3.5 | 0.013 | 7/49 (NCI-H1792, SW480, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.788×** | -3.2 | 0.028 | 24/49 (SK-MEL-2, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.878× | -3.1 | 0.039 | 10/47 (LoVo, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.889× | -3.1 | 0.047 | 11/48 (RKO, LOX-IMVI, …) | inconsistent across doses |  |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | 0.889× | -3.1 | 0.047 | 4/49 (RKO, NCI-H1573, …) | inconsistent across doses | position effect removed |
| [[Pralsetinib (drug)]] 5 µM |  | **0.799×** | -3.0 | 0.047 | 25/49 (NCI-H2347, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Apalutamide (drug)]] 0.5 µM |  | 0.894× | -2.9 | 0.071 | 5/48 (NCI-H1573, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9603. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 348 | 13 (7 ⚠) | 3 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 3.46× (z +26.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.26× (z +24.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.570× (z -16.7) |
| [[HOP62 (line)]] | alt | 703 | 6 (1 ⚠) | 9 (7 ⚠) | [[TAK-901 (drug)]] 5 µM 4.64× (z +13.7) | [[Dinaciclib (drug)]] 5 µM 0.242× (z -23.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.536× (z -15.1) |
| [[NCI-H1792 (line)]] | alt | 635 | 5 (1 ⚠) | 9 (8 ⚠) | [[Digitoxin (drug)]] 5 µM 2.37× (z +15.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.14× (z +13.7) | [[Dinaciclib (drug)]] 5 µM 0.270× (z -22.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.524× (z -16.5) |
| [[PANC-1 (line)]] | alt | 402 | 9 (4 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +25.3) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.43× (z +17.4) | [[Dinaciclib (drug)]] 5 µM 0.388× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.567× (z -15.7) |
| [[SW 900 (line)]] | alt | 482 | 4 (1 ⚠) | 10 (9 ⚠) | [[PH-797804 (drug)]] 5 µM 3.18× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.364× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.569× (z -14.1) |
| [[SW480 (line)]] | alt | 477 | 7 (2 ⚠) | 7 (6 ⚠) | [[TAK-901 (drug)]] 5 µM 4.60× (z +16.5) | [[Dinaciclib (drug)]] 5 µM 0.406× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.633× (z -13.3) |
| [[A-427 (line)]] | wt | 490 | 5 (3 ⚠) | 8 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +19.7) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.16× (z +13.0) | [[Dinaciclib (drug)]] 0.5 µM 0.266× (z -28.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.539× (z -13.3) |
| [[HEC-1-A (line)]] | alt | 707 | 3 (1 ⚠) | 10 (9 ⚠) | [[PH-797804 (drug)]] 5 µM 4.60× (z +18.2) | [[Dinaciclib (drug)]] 5 µM 0.194× (z -36.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -25.7) |
| [[NCI-H23 (line)]] | alt | 512 | 7 (2 ⚠) | 6 (6 ⚠) | [[TAK-901 (drug)]] 5 µM 4.22× (z +16.0) | [[Dinaciclib (drug)]] 5 µM 0.188× (z -34.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 550 | 2 | 10 (8 ⚠) | [[TAK-901 (drug)]] 5 µM 3.64× (z +13.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -26.5) |
| [[NCI-H2347 (line)]] | alt | 616 | 3 | 9 (8 ⚠) | [[TAK-901 (drug)]] 5 µM 3.26× (z +12.8) | [[Dinaciclib (drug)]] 0.5 µM 0.255× (z -28.4) ⚠ toxic; transcription drop · without an alert: [[Belumosudil (drug)]] 5 µM 0.627× (z -9.4) |
| [[RPMI-7951 (line)]] | alt | 711 | 2 | 10 (9 ⚠) | [[TAK-901 (drug)]] 5 µM 3.72× (z +12.6) | [[Dinaciclib (drug)]] 0.5 µM 0.421× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.589× (z -13.8) |
| [[SK-MEL-2 (line)]] | alt | 530 | 5 (3 ⚠) | 7 (6 ⚠) | [[TAK-901 (drug)]] 5 µM 3.86× (z +13.1) | [[Dinaciclib (drug)]] 5 µM 0.330× (z -19.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.540× (z -16.1) |
| [[KATO III (line)]] | alt | 471 | 3 (1 ⚠) | 8 (7 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.71× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.419× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.594× (z -13.7) |
| [[hTERT-HPNE (line)]] | wt | 582 | 2 | 8 (6 ⚠) | [[TAK-901 (drug)]] 5 µM 4.71× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.280× (z -16.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.458× (z -15.1) |
| [[LOX-IMVI (line)]] | wt | 498 | 6 (2 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +16.1) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.10× (z +15.9) | [[Dinaciclib (drug)]] 5 µM 0.405× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.559× (z -15.3) |
| [[A549 (line)]] | wt | 497 | 3 (2 ⚠) | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +22.0) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.39× (z +12.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.340× (z -25.4) |
| [[C32 (line)]] | wt | 497 | 2 | 7 (6 ⚠) | [[PH-797804 (drug)]] 5 µM 4.39× (z +11.3) | [[Dinaciclib (drug)]] 0.5 µM 0.373× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.544× (z -12.6) |
| [[CFPAC-1 (line)]] | alt | 307 | 1 | 8 (7 ⚠) | [[TAK-901 (drug)]] 5 µM 2.75× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.403× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.620× (z -12.0) |
| [[NCI-H2030 (line)]] | alt | 431 | 5 (2 ⚠) | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.18× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.387× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.605× (z -10.5) |
| [[SW1417 (line)]] | alt | 572 | 4 (1 ⚠) | 5 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.63× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.280× (z -25.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 326 | 1 | 7 (6 ⚠) | [[TAK-901 (drug)]] 5 µM 2.31× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.432× (z -24.6) |
| [[H4 (line)]] | wt | 565 | 1 | 7 (6 ⚠) | [[TAK-901 (drug)]] 5 µM 3.76× (z +11.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.432× (z -19.2) |
| [[NCI-H1573 (line)]] | alt | 365 | 5 (2 ⚠) | 3 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 2.74× (z +15.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.41× (z +13.1) | [[Dinaciclib (drug)]] 5 µM 0.220× (z -21.7) ⚠ toxic; transcription drop · without an alert: [[Belumosudil (drug)]] 5 µM 0.523× (z -9.3) |
| [[RKO (line)]] | wt | 540 | 6 (3 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +17.8) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.50× (z +15.5) | [[Dinaciclib (drug)]] 0.5 µM 0.475× (z -12.8) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 487 | 2 | 6 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 3.31× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.257× (z -25.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -20.9) |
| [[SW48 (line)]] | wt | 493 | 6 (4 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +13.9) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.32× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.396× (z -12.7) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 499 | 2 | 5 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 5.17× (z +14.6) | [[Dinaciclib (drug)]] 5 µM 0.348× (z -17.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.579× (z -13.2) |
| [[J82 (line)]] | alt | 433 | 3 (1 ⚠) | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.76× (z +15.0) | [[Dinaciclib (drug)]] 0.5 µM 0.372× (z -21.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.658× (z -12.9) |
| [[LoVo (line)]] | wt | 480 | 5 (2 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.35× (z +16.8) | [[Dinaciclib (drug)]] 5 µM 0.488× (z -13.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 506 | 4 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.58× (z +13.9) | [[Dinaciclib (drug)]] 5 µM 0.332× (z -15.6) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 392 | 3 (1 ⚠) | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 4.80× (z +15.3) | [[Dinaciclib (drug)]] 5 µM 0.378× (z -17.5) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 353 | 3 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.23× (z +17.0) | [[Dinaciclib (drug)]] 5 µM 0.468× (z -15.4) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 609 | 1 | 5 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 4.10× (z +11.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.568× (z -12.4) |
| [[HT-29 (line)]] | alt | 328 | 4 (2 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.42× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.400× (z -14.3) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 457 | 1 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.09× (z +10.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.607× (z -13.0) |
| [[Hs 766T (line)]] | wt | 361 | 3 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.64× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.369× (z -15.5) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 405 | 2 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.05× (z +14.2) | [[Dinaciclib (drug)]] 5 µM 0.432× (z -15.8) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 556 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.293× (z -20.4) |
| [[COLO 205 (line)]] | alt | 314 | 3 (1 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.54× (z +12.9) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 5.10× (z +12.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.488× (z -9.9) ⚠ toxic |
| [[C-33 A (line)]] | alt | 499 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.25× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.259× (z -21.9) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 371 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.49× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.408× (z -13.2) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 520 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.17× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.443× (z -11.2) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 563 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.217× (z -13.0) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 716 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.19× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.352× (z -10.2) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 296 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -10.4) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H2122 (line)]] | alt | 478 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 530 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 368 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 555 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9603), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDC27]] | +0.65 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[NRTN]] | +0.63 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[CCDC110]] | +0.59 | +0.30 / +0.50 | both halves | 2e-04 |  |
| [[PLEKHH3]] | +0.57 | +0.61 / +0.46 | both halves | 3e-05 |  |
| [[ETFB]] | +0.56 | +0.43 / +0.46 | both halves | 3e-05 |  |
| [[DBP]] | +0.56 | +0.40 / +0.51 | both halves | 5e-05 |  |
| [[NME9]] | +0.56 | +0.31 / +0.51 | both halves | 2e-04 |  |
| [[ASMTL]] | +0.55 | +0.40 / +0.45 | both halves | 5e-05 |  |
| [[FAM13B]] | +0.54 | +0.68 / +0.36 | both halves | 1e-04 |  |
| [[MRPL23]] | +0.54 | +0.42 / +0.41 | both halves | 4e-05 |  |
| [[CUL3]] | +0.53 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[HOOK2]] | +0.53 | +0.31 / +0.57 | both halves | 2e-04 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELK4]] | -0.58 | -0.55 / -0.40 | both halves | 5e-05 |  |
| [[RSC1A1]] | -0.58 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[RBM12]] | -0.54 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[CERS2]] | -0.54 | -0.32 / -0.36 | both halves | 2e-04 |  |
| [[PSME3]] | -0.54 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[TAX1BP3]] | -0.54 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[MYD88]] | -0.52 | -0.53 / -0.40 | both halves | 5e-05 |  |
| [[AVEN]] | -0.51 | -0.57 / -0.38 | both halves | 7e-05 |  |
| [[ABCF2]] | -0.51 | -0.51 / -0.37 | both halves | 8e-05 |  |
| [[TOR1A]] | -0.51 | -0.46 / -0.34 | both halves | 1e-04 |  |
| [[SPOPL-DT]] | -0.50 | -0.59 / -0.44 | both halves | 3e-05 |  |
| [[DDX5]] | -0.50 | -0.54 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises SETD5's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.330). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (8.8, -2.6); signed map (-26.6, 24.4). **Vector** length 101, 42.0% of its response variance represented; |z| ≥ 3 in 1,663 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.3 | -0.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +7.9 | +2.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.0 | +2.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +7.0 | +10.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.6 | +18.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.1 | -0.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +3.6 | +3.2 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +3.3 | +1.2 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -8.5 | -9.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -7.2 | -5.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -6.9 | +6.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.7 | -3.4 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -5.4 | -2.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.6 | -0.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -4.4 | -2.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.7 | -3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.7 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | SET domain containing 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p25.3 — chr3:9,397,615-9,479,240 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10707, SETD5A |
| Gene groups (HGNC) | SET domain containing; Putative lysine methyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9C0A6](https://www.uniprot.org/uniprotkb/Q9C0A6) (Histone-lysine N-methyltransferase SETD5):

> Chromatin regulator required for brain development: acts as a regulator of RNA elongation rate, thereby regulating neural stem cell (NSC) proliferation and synaptic transmission. May act by mediating trimethylation of 'Lys-36' of histone H3 (H3K36me3), which is essential to allow on-time RNA elongation dynamics. Also monomethylates 'Lys-9' of histone H3 (H3K9me1) in vitro. The relevance of histone methyltransferase activity is however subject to discussion.

**Summary**, from NCBI Gene [55209](https://www.ncbi.nlm.nih.gov/gene/55209):

> This function of this gene has yet to be determined but based on sequence similarity to other SET domain proteins it may function as a histone methyltransferase. Mutations in this gene have been associated with an autosomal dominant form of intellectual disability. Alternative splicing results in multiple transcript variants encoding different isoforms. [provided by RefSeq, Jul 2017]

**Accessions** — [HGNC:25566](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25566) · Entrez [55209](https://www.ncbi.nlm.nih.gov/gene/55209) · UniProt [Q9C0A6](https://www.uniprot.org/uniprotkb/Q9C0A6) · Ensembl [ENSG00000168137](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168137)

## Data

Gene col 9603: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9603); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9603, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9603]; `tensor/DDL_lfc|DDL_z.npy` [9603]; `embed/gene_vectors.npy` [9603]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9603 or target_col == 9603). Every well: [[SETD5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SETD5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
